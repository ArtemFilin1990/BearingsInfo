#!/usr/bin/env python3
"""
build_bearings_seed.py — генератор seed SQL для Cloudflare D1.

Читает CSV-источники из репозитория BearingsInfo и генерирует
SQL-файлы для wrangler d1 execute. Совместим с SQLite-диалектом D1.

Источники:
  - data/csv/master_catalog.csv      → таблица bearings
  - data/brands/brands.csv           → таблица manufacturers
  - data/analogs/import_analogs.csv  → таблица analogs
  - data/nomenclature.csv            → таблица nomenclature
"""

import csv
import json
import sys
import textwrap
from pathlib import Path
from datetime import datetime, timezone

# ── Пути ────────────────────────────────────────────────────────────────────
REPO_ROOT    = Path(__file__).parent
DATA_DIR     = REPO_ROOT / "data"
OUTPUT_DIR   = REPO_ROOT / "seed"
SCHEMA_FILE  = REPO_ROOT / "data" / "schema" / "d1_schema.sql"

OUTPUT_DIR.mkdir(exist_ok=True)

# ── Утилиты ──────────────────────────────────────────────────────────────────
def esc(value: str) -> str:
    """Экранирует одиночные кавычки для SQL."""
    if value is None:
        return "NULL"
    s = str(value).strip()
    if s == "" or s.lower() in ("none", "nan", "null", "#n/a", "n/a"):
        return "NULL"
    return "'" + s.replace("'", "''") + "'"

def num(value: str) -> str:
    """Возвращает число или NULL."""
    if value is None:
        return "NULL"
    s = str(value).strip().replace(",", ".")
    if s == "" or s.lower() in ("none", "nan", "null", "#n/a", "n/a"):
        return "NULL"
    try:
        float(s)
        return s
    except ValueError:
        return "NULL"

def write_sql_file(name: str, statements: list[str], batch_size: int = 500) -> list[Path]:
    """
    Записывает SQL-файлы батчами (D1 ограничен ~1 МБ на запрос).
    Возвращает список созданных файлов.
    """
    files = []
    for i, chunk_start in enumerate(range(0, len(statements), batch_size)):
        chunk = statements[chunk_start : chunk_start + batch_size]
        suffix = f"_{i+1:03d}" if len(statements) > batch_size else ""
        out = OUTPUT_DIR / f"{name}{suffix}.sql"
        out.write_text("\n".join(chunk) + "\n", encoding="utf-8")
        files.append(out)
        print(f"  ✓ {out.name}  ({len(chunk)} строк)")
    return files

# ── Схема D1 (SQLite) ────────────────────────────────────────────────────────
D1_SCHEMA = textwrap.dedent("""\
-- Cloudflare D1 / SQLite schema for BearingsInfo
-- Генерируется автоматически: build_bearings_seed.py
-- SQLite не поддерживает SERIAL → INTEGER PRIMARY KEY AUTOINCREMENT
--                      TIMESTAMP → TEXT (ISO-8601)
--                      BOOLEAN   → INTEGER (0/1)
--                      DECIMAL   → REAL

CREATE TABLE IF NOT EXISTS bearings (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    gost_designation    TEXT,
    iso_designation     TEXT NOT NULL,
    skf_designation     TEXT,
    fag_designation     TEXT,
    nsk_designation     TEXT,
    ntn_designation     TEXT,
    koyo_designation    TEXT,
    bearing_type        TEXT NOT NULL,
    bore_diameter_d     REAL NOT NULL,
    outer_diameter_D    REAL NOT NULL,
    width_B             REAL NOT NULL,
    chamfer_r_min       REAL,
    weight_kg           REAL,
    dynamic_load_C_kN   REAL,
    static_load_C0_kN   REAL,
    limiting_speed_rpm  INTEGER,
    reference_speed_rpm INTEGER,
    category            TEXT,
    status              TEXT DEFAULT 'active',
    created_at          TEXT DEFAULT (datetime('now')),
    updated_at          TEXT DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_bearings_gost ON bearings(gost_designation);
CREATE INDEX IF NOT EXISTS idx_bearings_iso  ON bearings(iso_designation);
CREATE INDEX IF NOT EXISTS idx_bearings_type ON bearings(bearing_type);
CREATE INDEX IF NOT EXISTS idx_bearings_dim  ON bearings(bore_diameter_d, outer_diameter_D, width_B);

CREATE TABLE IF NOT EXISTS manufacturers (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    brand               TEXT NOT NULL UNIQUE,
    country             TEXT,
    company_name        TEXT,
    manufacturer_type   TEXT,
    quality_level       TEXT,
    specialization      TEXT,
    website             TEXT,
    notes               TEXT,
    created_at          TEXT DEFAULT (datetime('now')),
    updated_at          TEXT DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_manufacturers_brand   ON manufacturers(brand);
CREATE INDEX IF NOT EXISTS idx_manufacturers_country ON manufacturers(country);

CREATE TABLE IF NOT EXISTS analogs (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    source_standard     TEXT NOT NULL,
    source_designation  TEXT NOT NULL,
    target_standard     TEXT NOT NULL,
    target_designation  TEXT NOT NULL,
    bearing_type        TEXT,
    is_direct_analog    INTEGER DEFAULT 1,
    limitations         TEXT,
    notes               TEXT,
    source_reference    TEXT,
    created_at          TEXT DEFAULT (datetime('now')),
    updated_at          TEXT DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_analogs_src    ON analogs(source_designation);
CREATE INDEX IF NOT EXISTS idx_analogs_target ON analogs(target_designation);

CREATE TABLE IF NOT EXISTS nomenclature (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    brand       TEXT NOT NULL,
    product     TEXT NOT NULL,
    category    TEXT,
    prefix      TEXT,
    number      TEXT,
    suffix      TEXT,
    analog      TEXT,
    d_mm        REAL,
    D_mm        REAL,
    B_mm        REAL,
    source      TEXT,
    created_at  TEXT DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_nomenclature_brand   ON nomenclature(brand);
CREATE INDEX IF NOT EXISTS idx_nomenclature_product ON nomenclature(product);
CREATE INDEX IF NOT EXISTS idx_nomenclature_analog  ON nomenclature(analog);

CREATE TABLE IF NOT EXISTS search_history (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id         TEXT,
    query           TEXT NOT NULL,
    results_count   INTEGER,
    clicked_result  TEXT,
    session_id      TEXT,
    created_at      TEXT DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_search_query   ON search_history(query);
CREATE INDEX IF NOT EXISTS idx_search_session ON search_history(session_id);
""")

# ── Генераторы INSERT ────────────────────────────────────────────────────────

def build_manufacturers(csv_path: Path) -> list[str]:
    """data/brands/brands.csv → INSERT INTO manufacturers"""
    if not csv_path.exists():
        print(f"  ⚠ Не найден: {csv_path} — пропускаю")
        return []

    stmts = []
    with csv_path.open(encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            brand   = esc(row.get("brand") or row.get("Brand") or "")
            country = esc(row.get("country") or row.get("Country") or "")
            company = esc(row.get("company_name") or row.get("Company") or row.get("brand") or "")
            mtype   = esc(row.get("manufacturer_type") or row.get("type") or "")
            quality = esc(row.get("quality_level") or row.get("segment") or "")
            spec    = esc(row.get("specialization") or row.get("categories") or "")
            web     = esc(row.get("website") or row.get("url") or "")
            notes   = esc(row.get("notes") or row.get("Notes") or "")

            if brand == "NULL":
                continue

            stmts.append(
                f"INSERT OR IGNORE INTO manufacturers "
                f"(brand,country,company_name,manufacturer_type,quality_level,specialization,website,notes) "
                f"VALUES ({brand},{country},{company},{mtype},{quality},{spec},{web},{notes});"
            )
    print(f"  manufacturers: {len(stmts)} строк")
    return stmts


def build_analogs(csv_path: Path) -> list[str]:
    """data/analogs/import_analogs.csv → INSERT INTO analogs"""
    if not csv_path.exists():
        print(f"  ⚠ Не найден: {csv_path} — пробую gost_iso.csv")
        csv_path = csv_path.parent / "gost_iso.csv"
    if not csv_path.exists():
        print(f"  ⚠ Не найден: {csv_path} — пропускаю")
        return []

    stmts = []
    with csv_path.open(encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        for row in reader:
            # Поддерживаем разные форматы колонок
            src_std  = esc(row.get("source_standard") or row.get("standard") or "GOST")
            src_des  = esc(row.get("source_designation") or row.get("gost") or row.get("from") or "")
            tgt_std  = esc(row.get("target_standard") or row.get("iso_standard") or "ISO")
            tgt_des  = esc(row.get("target_designation") or row.get("iso") or row.get("to") or "")
            btype    = esc(row.get("bearing_type") or row.get("type") or "")
            direct   = "1" if str(row.get("is_direct_analog", "1")).lower() in ("1", "true", "yes", "да") else "0"
            notes    = esc(row.get("notes") or "")
            src_ref  = esc(row.get("source_reference") or row.get("source") or "")

            if src_des == "NULL" or tgt_des == "NULL":
                continue

            stmts.append(
                f"INSERT OR IGNORE INTO analogs "
                f"(source_standard,source_designation,target_standard,target_designation,"
                f"bearing_type,is_direct_analog,notes,source_reference) "
                f"VALUES ({src_std},{src_des},{tgt_std},{tgt_des},"
                f"{btype},{direct},{notes},{src_ref});"
            )
    print(f"  analogs: {len(stmts)} строк")
    return stmts


def build_nomenclature(csv_path: Path) -> list[str]:
    """data/nomenclature.csv → INSERT INTO nomenclature"""
    if not csv_path.exists():
        print(f"  ⚠ Не найден: {csv_path} — пропускаю")
        return []

    stmts = []
    with csv_path.open(encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            brand   = esc(row.get("Brand") or row.get("brand") or row.get("Бренд") or "")
            product = esc(row.get("Product Name") or row.get("product") or row.get("продукция") or "")
            cat     = esc(row.get("Category") or row.get("категория") or "")
            prefix  = esc(row.get("prefix") or row.get("префикс") or "")
            number  = esc(row.get("number") or row.get("номер") or "")
            suffix  = esc(row.get("suffix") or row.get("суффикс") or "")
            analog  = esc(row.get("Аналог") or row.get("analog") or "")
            d_mm    = num(row.get("d_mm") or row.get("d") or "")
            D_mm    = num(row.get("D_mm") or row.get("D") or "")
            B_mm    = num(row.get("B_mm") or row.get("B") or "")
            source  = esc(row.get("source") or row.get("источник") or "")

            if brand == "NULL" and product == "NULL":
                continue

            stmts.append(
                f"INSERT INTO nomenclature "
                f"(brand,product,category,prefix,number,suffix,analog,d_mm,D_mm,B_mm,source) "
                f"VALUES ({brand},{product},{cat},{prefix},{number},{suffix},{analog},{d_mm},{D_mm},{B_mm},{source});"
            )
    print(f"  nomenclature: {len(stmts)} строк")
    return stmts


def build_bearings_from_master(csv_path: Path) -> list[str]:
    """data/csv/master_catalog.csv → INSERT INTO bearings"""
    if not csv_path.exists():
        print(f"  ⚠ Не найден: {csv_path} — пропускаю")
        return []

    stmts = []
    with csv_path.open(encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            gost = esc(row.get("gost_designation") or row.get("gost") or "")
            iso  = esc(row.get("iso_designation")  or row.get("iso")  or
                       row.get("designation") or row.get("part_number") or "")
            skf  = esc(row.get("skf_designation")  or "")
            fag  = esc(row.get("fag_designation")  or "")
            nsk  = esc(row.get("nsk_designation")  or "")
            ntn  = esc(row.get("ntn_designation")  or "")
            koyo = esc(row.get("koyo_designation") or "")
            btype = esc(row.get("bearing_type") or row.get("type") or "Unknown")
            d    = num(row.get("bore_diameter_d") or row.get("d_mm") or row.get("d") or "0")
            D    = num(row.get("outer_diameter_D") or row.get("D_mm") or row.get("D") or "0")
            B    = num(row.get("width_B") or row.get("B_mm") or row.get("B") or "0")
            r    = num(row.get("chamfer_r_min") or "")
            w    = num(row.get("weight_kg") or "")
            C    = num(row.get("dynamic_load_C_kN") or "")
            C0   = num(row.get("static_load_C0_kN") or "")
            sp   = num(row.get("limiting_speed_rpm") or "")
            rsp  = num(row.get("reference_speed_rpm") or "")
            cat  = esc(row.get("category") or "")
            stat = esc(row.get("status") or "active")

            if iso == "NULL" or d == "NULL":
                continue

            stmts.append(
                f"INSERT INTO bearings "
                f"(gost_designation,iso_designation,skf_designation,fag_designation,"
                f"nsk_designation,ntn_designation,koyo_designation,bearing_type,"
                f"bore_diameter_d,outer_diameter_D,width_B,chamfer_r_min,weight_kg,"
                f"dynamic_load_C_kN,static_load_C0_kN,limiting_speed_rpm,reference_speed_rpm,"
                f"category,status) "
                f"VALUES ({gost},{iso},{skf},{fag},{nsk},{ntn},{koyo},{btype},"
                f"{d},{D},{B},{r},{w},{C},{C0},{sp},{rsp},{cat},{stat});"
            )
    print(f"  bearings: {len(stmts)} строк")
    return stmts


# ── Точка входа ──────────────────────────────────────────────────────────────
def main():
    print("=" * 60)
    print(f"build_bearings_seed.py  —  {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print("=" * 60)

    # 1. Схема D1
    schema_out = OUTPUT_DIR / "00_schema.sql"
    schema_out.write_text(D1_SCHEMA, encoding="utf-8")
    print(f"  ✓ {schema_out.name}  (схема D1)")

    # 2. manufacturers
    print("\n[manufacturers]")
    mfr_stmts = build_manufacturers(DATA_DIR / "brands" / "brands.csv")
    if mfr_stmts:
        write_sql_file("01_manufacturers", mfr_stmts)

    # 3. analogs
    print("\n[analogs]")
    ana_stmts = build_analogs(DATA_DIR / "analogs" / "import_analogs.csv")
    if ana_stmts:
        write_sql_file("02_analogs", ana_stmts)

    # 4. nomenclature
    print("\n[nomenclature]")
    nom_stmts = build_nomenclature(DATA_DIR / "nomenclature.csv")
    if nom_stmts:
        write_sql_file("03_nomenclature", nom_stmts, batch_size=1000)

    # 5. bearings (master catalog)
    print("\n[bearings master_catalog]")
    brg_stmts = build_bearings_from_master(DATA_DIR / "csv" / "master_catalog.csv")
    if brg_stmts:
        write_sql_file("04_bearings", brg_stmts, batch_size=500)

    # 6. Манифест
    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "files": [str(p.name) for p in sorted(OUTPUT_DIR.glob("*.sql"))],
        "counts": {
            "manufacturers": len(mfr_stmts),
            "analogs":       len(ana_stmts),
            "nomenclature":  len(nom_stmts),
            "bearings":      len(brg_stmts),
        }
    }
    manifest_out = OUTPUT_DIR / "manifest.json"
    manifest_out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n  ✓ {manifest_out.name}")

    total = len(mfr_stmts) + len(ana_stmts) + len(nom_stmts) + len(brg_stmts)
    print(f"\n✅ Готово: {total} INSERT-выражений → {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
