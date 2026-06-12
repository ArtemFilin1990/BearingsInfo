#!/usr/bin/env python3
"""Build a Bitrix24 Knowledge Base import ZIP (manifest.json) from a Landing site export.

Offline/dry-run usage (no Bitrix24 credentials required):

    python kb-archive-builder.py --input site-export.json --output kb_everest.zip

Live export usage (requires an explicit confirmation gate):

    BITRIX24_WEBHOOK_URL=https://example.bitrix24.ru/rest/1/<token> \\
    BITRIX24_EXPORT_CONFIRM=true \\
    python kb-archive-builder.py --site-id 109 --execute --output kb_everest.zip

The resulting ZIP contains a single ``manifest.json`` file ready for
"Сотрудники → База знаний → ⚙️ → Импорт Базы знаний → Загрузить ZIP".
"""

from __future__ import annotations

import argparse
import html
import json
import os
import zipfile
from pathlib import Path
from typing import Any

from kb_common import GENERATED_DIR, SOURCE_DIR, call_bitrix, read_json, require_https_webhook

DEFAULT_SECTIONS = SOURCE_DIR / "kb_archive_sections.json"
DEFAULT_OUTPUT = GENERATED_DIR / "bitrix24" / "kb_everest_podshipniki.zip"
DEFAULT_BASE_URL = "https://ewerest.bitrix24.ru/everest-bearing-kb/"
DEFAULT_SCOPE = "knowledge"
DEFAULT_NAME = "Технический справочник: подшипники и промышленная продукция"
DEFAULT_DESCRIPTION = "Внутренний справочник ООО «Эверест». Для менеджеров, снабжения и технических специалистов."
DEFAULT_THEME: dict[str, str] = {
    "BACKGROUND_USE": "Y",
    "BACKGROUND_COLOR": "#ffffff",
    "THEME_COLOR": "#EE690B",
    "THEMEFONTS_CODE_H": "Roboto",
    "THEMEFONTS_CODE": "Open Sans",
    "THEMEFONTS_COLOR": "#333333",
    "THEMEFONTS_COLOR_H": "#1a1a1a",
}
CONTENT_BLOCK_CODE = "08.3.one_col_fix_title_and_text"
WRAPPER_STYLE = {"#wrapper": ["landing-block g-pt-30 g-pb-30"]}

NAV_TEMPLATE = (
    '<div style="margin-top:24px;padding-top:16px;border-top:1px solid #e0e0e0;">'
    '<div style="font-size:11px;font-family:monospace;color:#999;margin-bottom:8px;">НАВИГАЦИЯ</div>'
    '<a href="/" style="color:#EE690B;text-decoration:none;font-size:12px;">← Главная</a>'
    "{breadcrumb}"
    "</div>"
)


def load_export(path: Path) -> dict[str, Any]:
    return read_json(path)


def fetch_export(site_id: int, scope: str, timeout: float) -> dict[str, Any]:
    if os.environ.get("BITRIX24_EXPORT_CONFIRM", "").strip().lower() != "true":
        raise RuntimeError("Live export is blocked. Required environment: BITRIX24_EXPORT_CONFIRM=true")
    webhook_url = require_https_webhook()
    response = call_bitrix(
        webhook_url,
        "landing.site.fullExport",
        {"id": site_id, "params": {"scope": scope}},
        timeout,
    )
    result = response.get("result")
    if not isinstance(result, dict) or not result:
        raise RuntimeError(f"landing.site.fullExport returned no data for site {site_id}")
    return result


def apply_metadata(export: dict[str, Any], name: str, description: str, theme: dict[str, str]) -> None:
    export["type"] = "knowledge"
    export["name"] = name
    export["description"] = description
    fields = export.setdefault("fields", {})
    additional_fields = fields.setdefault("ADDITIONAL_FIELDS", {})
    additional_fields.update(theme)


def fix_internal_links(export: dict[str, Any], base_url: str) -> dict[str, Any]:
    if not base_url:
        return export
    serialized = json.dumps(export, ensure_ascii=False)
    serialized = serialized.replace(base_url, "/")
    return json.loads(serialized)


def iter_navigation_pages(sections: dict[str, Any]):
    for group in sections["groups"]:
        for page in group["pages"]:
            yield group["title"], page["code"], page["title"]


def page_section_titles(sections: dict[str, Any]) -> dict[str, str]:
    return {code: group_title for group_title, code, _ in iter_navigation_pages(sections)}


def page_titles(sections: dict[str, Any]) -> dict[str, str]:
    return {code: title for _, code, title in iter_navigation_pages(sections)}


def fill_empty_pages(export: dict[str, Any], sections: dict[str, Any]) -> None:
    titles = page_titles(sections)
    for page_code, page in export.get("items", {}).items():
        if page.get("items"):
            continue
        title = titles.get(page_code, page.get("name", page_code))
        description = page.get("description") or "нет данных"
        block_id = f"#block_{page_code.replace('-', '_')}"
        page["items"] = {
            block_id: {
                "code": CONTENT_BLOCK_CODE,
                "access": "X",
                "nodes": {
                    ".landing-block-node-title": [title],
                    ".landing-block-node-text": [
                        f"<p><strong>Назначение:</strong> {html.escape(description)}</p>"
                        "<p><em>Статус: нет данных. Заполнить техническим специалистом.</em></p>"
                    ],
                },
                "style": dict(WRAPPER_STYLE),
            }
        }


def build_index_page(export: dict[str, Any], sections: dict[str, Any]) -> None:
    index_code = export.get("fields", {}).get("LANDING_ID_INDEX")
    page = export.get("items", {}).get(index_code) if index_code else None
    if page is None:
        return

    toc_parts = []
    for group in sections["groups"]:
        items_html = "".join(
            f'<li><a href="/{page_item["code"]}/" style="color:#EE690B;text-decoration:none;">'
            f'{html.escape(page_item["title"])}</a></li>'
            for page_item in group["pages"]
        )
        toc_parts.append(f"<h3>{html.escape(group['title'])}</h3><ul>{items_html}</ul>")

    toc_block = {
        "code": CONTENT_BLOCK_CODE,
        "access": "X",
        "nodes": {
            ".landing-block-node-title": ["Содержание справочника"],
            ".landing-block-node-text": ["".join(toc_parts)],
        },
        "style": dict(WRAPPER_STYLE),
    }
    page["items"] = {"#block_toc_index": toc_block, **page.get("items", {})}


def add_navigation(export: dict[str, Any], sections: dict[str, Any]) -> None:
    section_titles = page_section_titles(sections)
    for page_code, page in export.get("items", {}).items():
        blocks = page.get("items", {})
        text_blocks = [block for block in blocks.values() if ".landing-block-node-text" in block.get("nodes", {})]
        if not text_blocks:
            continue
        section_title = section_titles.get(page_code)
        breadcrumb = (
            f'<span style="color:#999;font-size:12px;"> / {html.escape(section_title)}</span>' if section_title else ""
        )
        text_blocks[-1]["nodes"][".landing-block-node-text"].append(NAV_TEMPLATE.format(breadcrumb=breadcrumb))


def build_zip(export: dict[str, Any], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("manifest.json", json.dumps(export, ensure_ascii=False, indent=2))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input", type=Path, help="Local landing.site.fullExport JSON for offline/dry-run use.")
    parser.add_argument("--site-id", type=int, help="Landing site ID for a live landing.site.fullExport call.")
    parser.add_argument("--execute", action="store_true", help="Allow a live landing.site.fullExport call.")
    parser.add_argument("--scope", default=DEFAULT_SCOPE, help="Landing scope for the live export request.")
    parser.add_argument("--sections", type=Path, default=DEFAULT_SECTIONS, help="Navigation sections JSON.")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Output ZIP path.")
    parser.add_argument("--name", default=DEFAULT_NAME, help="Knowledge base title.")
    parser.add_argument("--description", default=DEFAULT_DESCRIPTION, help="Knowledge base description.")
    parser.add_argument(
        "--base-url",
        default=DEFAULT_BASE_URL,
        help="Old absolute base URL to strip from internal links (empty string disables link fixing).",
    )
    parser.add_argument("--timeout", type=float, default=60.0, help="HTTP timeout for the live export request.")
    args = parser.parse_args()

    if args.input:
        export = load_export(args.input)
    elif args.execute:
        if args.site_id is None:
            parser.error("--execute requires --site-id")
        export = fetch_export(args.site_id, args.scope, args.timeout)
    else:
        parser.error(
            "Specify --input <file> for offline mode, or --execute --site-id <id> with "
            "BITRIX24_WEBHOOK_URL and BITRIX24_EXPORT_CONFIRM=true for a live export."
        )
        return 2

    sections = read_json(args.sections)

    apply_metadata(export, args.name, args.description, DEFAULT_THEME)
    export = fix_internal_links(export, args.base_url)
    fill_empty_pages(export, sections)
    build_index_page(export, sections)
    add_navigation(export, sections)

    build_zip(export, args.output)

    print(f"ZIP: {args.output} ({args.output.stat().st_size // 1024} KB)")
    print(f"Pages: {len(export.get('items', {}))}")
    print("Импорт: Сотрудники → База знаний → ⚙️ → Импорт Базы знаний → Загрузить ZIP")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
