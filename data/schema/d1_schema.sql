-- ============================================================
-- Cloudflare D1 / SQLite schema — BearingsInfo
-- Совместим с wrangler d1 execute (SQLite диалект)
-- Генерируется: build_bearings_seed.py
-- ============================================================

-- SQLite: нет SERIAL → INTEGER PRIMARY KEY AUTOINCREMENT
--         нет TIMESTAMP → TEXT (ISO-8601)
--         нет BOOLEAN   → INTEGER (0/1)
--         нет DECIMAL   → REAL

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

-- ────────────────────────────────────────────────────────────

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

-- ────────────────────────────────────────────────────────────

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

-- ────────────────────────────────────────────────────────────

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

-- ────────────────────────────────────────────────────────────

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
