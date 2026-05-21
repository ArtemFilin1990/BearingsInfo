"""
Генератор энциклопедии по подшипникам в PDF.

Использует контент из enc_chapters_*.py (собранных субагентами)
и данные напрямую из CSV/nomenclature для сводного каталога.

Запуск:
    python tools/scripts/generate_encyclopedia_pdf.py
Результат:
    out/encyclopedia_bearings.pdf
"""

from __future__ import annotations

import csv
import importlib.util
import os
import sys
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# ReportLab imports
# ---------------------------------------------------------------------------
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm, mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
OUT_DIR = REPO_ROOT / "out"
OUT_DIR.mkdir(parents=True, exist_ok=True)
PDF_PATH = OUT_DIR / "encyclopedia_bearings.pdf"

# ---------------------------------------------------------------------------
# Font registration — try system DejaVu, fall back to Helvetica
# ---------------------------------------------------------------------------
FONT_NAME = "Helvetica"
FONT_BOLD = "Helvetica-Bold"
FONT_ITALIC = "Helvetica-Oblique"

def _register_fonts() -> None:
    global FONT_NAME, FONT_BOLD, FONT_ITALIC
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/TTF/DejaVuSans.ttf",
    ]
    bold_candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf",
    ]
    for reg, bold in zip(candidates, bold_candidates):
        if Path(reg).exists() and Path(bold).exists():
            try:
                pdfmetrics.registerFont(TTFont("DejaVuSans", reg))
                pdfmetrics.registerFont(TTFont("DejaVuSans-Bold", bold))
                FONT_NAME = "DejaVuSans"
                FONT_BOLD = "DejaVuSans-Bold"
                FONT_ITALIC = "DejaVuSans"
                print(f"  Font: DejaVuSans from {reg}")
                return
            except Exception:
                pass
    print("  Font: Helvetica (Cyrillic may not render — DejaVu not found)")

_register_fonts()

# ---------------------------------------------------------------------------
# Styles
# ---------------------------------------------------------------------------
def _build_styles() -> dict[str, ParagraphStyle]:
    s: dict[str, ParagraphStyle] = {}

    s["title"] = ParagraphStyle(
        "enc_title",
        fontName=FONT_BOLD,
        fontSize=28,
        leading=34,
        alignment=TA_CENTER,
        spaceAfter=12,
        textColor=colors.HexColor("#1a1a2e"),
    )
    s["subtitle"] = ParagraphStyle(
        "enc_subtitle",
        fontName=FONT_NAME,
        fontSize=14,
        leading=20,
        alignment=TA_CENTER,
        spaceAfter=6,
        textColor=colors.HexColor("#3d3d5c"),
    )
    s["h1"] = ParagraphStyle(
        "enc_h1",
        fontName=FONT_BOLD,
        fontSize=18,
        leading=24,
        spaceBefore=18,
        spaceAfter=8,
        textColor=colors.HexColor("#1a1a2e"),
        borderPad=4,
    )
    s["h2"] = ParagraphStyle(
        "enc_h2",
        fontName=FONT_BOLD,
        fontSize=13,
        leading=18,
        spaceBefore=12,
        spaceAfter=6,
        textColor=colors.HexColor("#2d2d5e"),
    )
    s["body"] = ParagraphStyle(
        "enc_body",
        fontName=FONT_NAME,
        fontSize=10,
        leading=15,
        spaceBefore=4,
        spaceAfter=4,
        alignment=TA_JUSTIFY,
    )
    s["toc_h1"] = ParagraphStyle(
        "enc_toc_h1",
        fontName=FONT_BOLD,
        fontSize=11,
        leading=16,
        spaceBefore=4,
        spaceAfter=2,
        leftIndent=0,
    )
    s["toc_h2"] = ParagraphStyle(
        "enc_toc_h2",
        fontName=FONT_NAME,
        fontSize=10,
        leading=14,
        spaceBefore=2,
        spaceAfter=1,
        leftIndent=16,
    )
    s["caption"] = ParagraphStyle(
        "enc_caption",
        fontName=FONT_ITALIC,
        fontSize=9,
        leading=12,
        spaceBefore=2,
        spaceAfter=6,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#555555"),
    )
    s["footer"] = ParagraphStyle(
        "enc_footer",
        fontName=FONT_NAME,
        fontSize=8,
        leading=10,
        textColor=colors.HexColor("#888888"),
        alignment=TA_CENTER,
    )
    return s


STYLES = _build_styles()

# ---------------------------------------------------------------------------
# Page templates
# ---------------------------------------------------------------------------
PAGE_W, PAGE_H = A4
MARGIN = 2.0 * cm
INNER_W = PAGE_W - 2 * MARGIN

TITLE_FRAME = Frame(MARGIN, MARGIN, INNER_W, PAGE_H - 2 * MARGIN, id="title")
BODY_FRAME = Frame(MARGIN, MARGIN + 1.2 * cm, INNER_W, PAGE_H - 2 * MARGIN - 1.4 * cm, id="body")


def _page_header_footer(canvas, doc):
    canvas.saveState()
    if doc.page > 1:
        # Top rule
        canvas.setStrokeColor(colors.HexColor("#cccccc"))
        canvas.setLineWidth(0.5)
        canvas.line(MARGIN, PAGE_H - MARGIN + 4 * mm, PAGE_W - MARGIN, PAGE_H - MARGIN + 4 * mm)
        # Header text
        canvas.setFont(FONT_NAME, 8)
        canvas.setFillColor(colors.HexColor("#888888"))
        canvas.drawString(MARGIN, PAGE_H - MARGIN + 6 * mm, "Энциклопедия подшипников")
        canvas.drawRightString(PAGE_W - MARGIN, PAGE_H - MARGIN + 6 * mm, str(doc.page))
        # Bottom rule
        canvas.line(MARGIN, MARGIN - 4 * mm, PAGE_W - MARGIN, MARGIN - 4 * mm)
        canvas.drawCentredString(PAGE_W / 2, MARGIN - 8 * mm, "© BearingsInfo")
    canvas.restoreState()


# ---------------------------------------------------------------------------
# Table style helpers
# ---------------------------------------------------------------------------
TABLE_HEADER_BG = colors.HexColor("#2d2d5e")
TABLE_ALT_BG = colors.HexColor("#f0f0f8")


def _table_style(n_rows: int, n_cols: int) -> TableStyle:
    row_bgs = []
    for i in range(1, n_rows + 1):
        if i % 2 == 0:
            row_bgs.append(("BACKGROUND", (0, i), (-1, i), TABLE_ALT_BG))
    return TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEADER_BG),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), FONT_BOLD),
            ("FONTSIZE", (0, 0), (-1, -1), 8),
            ("FONTNAME", (0, 1), (-1, -1), FONT_NAME),
            ("ROWBACKGROUND", (0, 1), (-1, -1), [colors.white, TABLE_ALT_BG]),
            ("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#cccccc")),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 3),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ]
        + row_bgs
    )


def _make_table(headers: list[str], rows: list[list[str]], max_rows: int = 40) -> list:
    """Return a list of Table flowables (split if > max_rows)."""
    flowables = []
    chunk_size = max_rows
    for start in range(0, max(1, len(rows)), chunk_size):
        chunk = rows[start : start + chunk_size]
        data = [[Paragraph(str(h), STYLES["caption"]) for h in headers]]
        for row in chunk:
            data.append([Paragraph(str(c or ""), STYLES["body"]) for c in row])
        col_count = len(headers)
        col_w = INNER_W / col_count
        t = Table(data, colWidths=[col_w] * col_count, repeatRows=1)
        t.setStyle(_table_style(len(chunk), col_count))
        flowables.append(t)
        flowables.append(Spacer(1, 4 * mm))
    return flowables


# ---------------------------------------------------------------------------
# Load chapter module helper
# ---------------------------------------------------------------------------
def _load_chapter_module(path: Path, varname: str) -> list[dict] | None:
    if not path.exists():
        print(f"  WARNING: {path.name} not found — skipping")
        return None
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    try:
        spec.loader.exec_module(mod)  # type: ignore[union-attr]
    except Exception as exc:
        print(f"  WARNING: failed to load {path.name}: {exc}")
        return None
    return getattr(mod, varname, None)


# ---------------------------------------------------------------------------
# Nomenclature sample table (Chapter 5 supplement)
# ---------------------------------------------------------------------------
def _nomenclature_sample(n: int = 100) -> tuple[list[str], list[list[str]]]:
    csv_path = REPO_ROOT / "data" / "nomenclature.csv"
    headers = ["Бренд", "Артикул", "Аналог", "Завод"]
    rows: list[list[str]] = []
    if not csv_path.exists():
        return headers, rows
    try:
        with open(csv_path, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            seen: set[str] = set()
            for row in reader:
                art = str(row.get("Product Name", "") or "").strip()
                brand = str(row.get("Brand", "") or "").strip()
                analog = str(row.get("Analog Name", "") or "").strip()
                factory = str(row.get("Factory", "") or "").strip()
                key = f"{brand}|{art}"
                if key in seen or not art:
                    continue
                seen.add(key)
                rows.append([brand[:20], art[:30], analog[:30], factory[:25]])
                if len(rows) >= n:
                    break
    except Exception as exc:
        print(f"  WARNING: could not read nomenclature.csv: {exc}")
    return headers, rows


# ---------------------------------------------------------------------------
# Cover page content
# ---------------------------------------------------------------------------
def _cover_flowables() -> list:
    items = []
    items.append(Spacer(1, 6 * cm))
    items.append(Paragraph("ЭНЦИКЛОПЕДИЯ ПОДШИПНИКОВ", STYLES["title"]))
    items.append(Spacer(1, 0.5 * cm))
    items.append(HRFlowable(width="80%", thickness=2, color=colors.HexColor("#2d2d5e"), spaceAfter=10))
    items.append(Paragraph("Полный справочник: типы, обозначения, стандарты,", STYLES["subtitle"]))
    items.append(Paragraph("размеры, аналоги, производители, монтаж и эксплуатация", STYLES["subtitle"]))
    items.append(Spacer(1, 1.5 * cm))
    items.append(Paragraph("На основе базы данных BearingsInfo · 42 000+ записей", STYLES["subtitle"]))
    items.append(Spacer(1, 4 * cm))
    items.append(HRFlowable(width="60%", thickness=1, color=colors.HexColor("#cccccc"), spaceAfter=8))
    items.append(Paragraph("ГОСТ · ISO · DIN · ANSI · SKF · FAG · NSK · NTN и др.", STYLES["subtitle"]))
    items.append(PageBreak())
    return items


# ---------------------------------------------------------------------------
# Chapter flowables
# ---------------------------------------------------------------------------
def _chapter_flowables(chapter: dict, chapter_num: int, doc_story: list) -> list:
    items: list = []
    title = chapter.get("title", f"Глава {chapter_num}")
    items.append(Paragraph(f"{chapter_num}. {title}", STYLES["h1"]))
    items.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#cccccc"), spaceAfter=6))

    for para in chapter.get("body", []):
        if para.strip():
            items.append(Paragraph(para, STYLES["body"]))

    for tbl in chapter.get("tables", []):
        headers = tbl.get("headers", [])
        rows = tbl.get("rows", [])
        caption = tbl.get("caption", "")
        if headers and rows:
            items.append(Spacer(1, 4 * mm))
            if caption:
                items.append(Paragraph(caption, STYLES["caption"]))
            items.extend(_make_table(headers, rows))

    items.append(PageBreak())
    return items


# ---------------------------------------------------------------------------
# Nomenclature catalog chapter (Chapter 5 supplement)
# ---------------------------------------------------------------------------
def _catalog_chapter() -> list:
    items: list = []
    items.append(Paragraph("Приложение А. Фрагмент каталога подшипников", STYLES["h1"]))
    items.append(
        Paragraph(
            "Ниже приведён фрагмент из более чем 42 000 позиций базы данных BearingsInfo. "
            "Полный каталог доступен в файле data/nomenclature.csv репозитория.",
            STYLES["body"],
        )
    )
    items.append(Spacer(1, 4 * mm))
    headers, rows = _nomenclature_sample(200)
    if rows:
        items.extend(_make_table(headers, rows, max_rows=40))
    items.append(PageBreak())
    return items


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    print("=== Генерация энциклопедии подшипников ===")
    scripts_dir = REPO_ROOT / "tools" / "scripts"

    # Load chapter data produced by sub-agents
    ch1_3 = _load_chapter_module(scripts_dir / "enc_chapters_1_3.py", "CHAPTERS_1_3") or []
    ch4_6 = _load_chapter_module(scripts_dir / "enc_chapters_4_6.py", "CHAPTERS_4_6") or []
    ch7_8 = _load_chapter_module(scripts_dir / "enc_chapters_7_8.py", "CHAPTERS_7_8") or []
    ch9_10 = _load_chapter_module(scripts_dir / "enc_chapters_9_10.py", "CHAPTERS_9_10") or []

    all_chapters = ch1_3 + ch4_6 + ch7_8 + ch9_10
    print(f"  Загружено глав: {len(all_chapters)}")

    # Build story
    story: list = []

    # Cover
    story.extend(_cover_flowables())

    # TOC placeholder (manual — ReportLab TOC requires 2-pass)
    story.append(Paragraph("Содержание", STYLES["h1"]))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#cccccc"), spaceAfter=6))
    for i, ch in enumerate(all_chapters, 1):
        story.append(Paragraph(f"{i}. {ch.get('title', '')}", STYLES["toc_h1"]))
    story.append(Paragraph("Приложение А. Фрагмент каталога подшипников", STYLES["toc_h1"]))
    story.append(PageBreak())

    # Chapters
    for i, ch in enumerate(all_chapters, 1):
        print(f"  Глава {i}: {ch.get('title', '?')}")
        story.extend(_chapter_flowables(ch, i, story))

    # Catalog appendix
    print("  Приложение А: фрагмент каталога 200 позиций")
    story.extend(_catalog_chapter())

    # Build PDF
    doc = BaseDocTemplate(
        str(PDF_PATH),
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=MARGIN + 1.0 * cm,
        bottomMargin=MARGIN + 0.8 * cm,
        title="Энциклопедия подшипников",
        author="BearingsInfo",
        subject="Справочник по подшипникам",
        creator="BearingsInfo PDF Generator",
    )

    body_template = PageTemplate(
        id="body",
        frames=[BODY_FRAME],
        onPage=_page_header_footer,
    )
    title_template = PageTemplate(
        id="title_page",
        frames=[TITLE_FRAME],
    )
    doc.addPageTemplates([title_template, body_template])

    # Insert template switch after cover
    story.insert(len(_cover_flowables()), NextPageTemplate("body"))

    print(f"  Сборка PDF → {PDF_PATH}")
    doc.build(story)
    size_mb = PDF_PATH.stat().st_size / (1024 * 1024)
    print(f"  Готово! Размер: {size_mb:.2f} МБ")
    print(f"  Путь: {PDF_PATH}")


if __name__ == "__main__":
    main()
