#!/usr/bin/env python3
"""Dry-run first Bitrix24 Landing/Knowledge Base webhook importer."""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from kb_common import GENERATED_DIR, REPORTS_DIR

DEFAULT_EXPORT = GENERATED_DIR / "json" / "bitrix24-import.json"
DEFAULT_DRY_RUN_REPORT = REPORTS_DIR / "bitrix24-import-dry-run.md"
DEFAULT_SITE_TITLE = "Технический справочник «Эверест»"
DEFAULT_SITE_CODE = "everest-technical-handbook"
DEFAULT_SCOPE = "knowledge"
DEFAULT_BLOCK_CODE = "0.menu_24"

REQUIRED_GENERIC_ENV = (
    "BITRIX24_WEBHOOK_URL",
    "BITRIX24_KB_IMPORT_METHOD",
    "BITRIX24_IMPORT_CONFIRM=true",
)
REQUIRED_LANDING_ENV = (
    "BITRIX24_WEBHOOK_URL",
    "BITRIX24_KB_SITE_ID",
    "BITRIX24_IMPORT_CONFIRM=true",
)


@dataclass(frozen=True)
class ImportAction:
    method: str
    params: dict[str, Any]
    label: str


def mask_url(url: str) -> str:
    parsed = urlparse(url)
    if not parsed.scheme or not parsed.netloc:
        return "<invalid-url>"
    return f"{parsed.scheme}://{parsed.netloc}/***"


def load_payload(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def iter_articles(payload: dict[str, Any]):
    for section in payload["sections"]:
        for article in section["articles"]:
            yield section, article


def slugify(value: str) -> str:
    value = value.casefold().replace("ё", "е")
    translit = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "й": "y",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "h",
        "ц": "c",
        "ч": "ch",
        "ш": "sh",
        "щ": "sch",
        "ъ": "",
        "ы": "y",
        "ь": "",
        "э": "e",
        "ю": "yu",
        "я": "ya",
    }
    value = "".join(translit.get(char, char) for char in value)
    value = re.sub(r"[^0-9a-z]+", "-", value).strip("-")
    return value or "item"


def markdown_inline(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"`(.+?)`", r"<code>\1</code>", escaped)
    return escaped


def flush_paragraph(lines: list[str], paragraph: list[str]) -> None:
    if paragraph:
        lines.append(f"<p>{markdown_inline(' '.join(paragraph))}</p>")
        paragraph.clear()


def flush_list(lines: list[str], list_items: list[str]) -> None:
    if list_items:
        lines.append("<ul>")
        lines.extend(f"<li>{markdown_inline(item)}</li>" for item in list_items)
        lines.append("</ul>")
        list_items.clear()


def markdown_table_to_html(table_lines: list[str]) -> str:
    rows: list[list[str]] = []
    for line in table_lines:
        stripped = line.strip().strip("|")
        cells = [cell.strip() for cell in stripped.split("|")]
        if cells and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            continue
        rows.append(cells)
    if not rows:
        return ""
    header, body = rows[0], rows[1:]
    output = ["<table>", "<thead><tr>"]
    output.extend(f"<th>{markdown_inline(cell)}</th>" for cell in header)
    output.append("</tr></thead>")
    if body:
        output.append("<tbody>")
        for row in body:
            output.append("<tr>")
            output.extend(f"<td>{markdown_inline(cell)}</td>" for cell in row)
            output.append("</tr>")
        output.append("</tbody>")
    output.append("</table>")
    return "\n".join(output)


def markdown_to_html(markdown: str) -> str:
    lines: list[str] = []
    paragraph: list[str] = []
    list_items: list[str] = []
    table_lines: list[str] = []

    def flush_table() -> None:
        if table_lines:
            lines.append(markdown_table_to_html(table_lines))
            table_lines.clear()

    for raw in markdown.splitlines():
        line = raw.rstrip()
        if line.startswith("|") and line.endswith("|"):
            flush_paragraph(lines, paragraph)
            flush_list(lines, list_items)
            table_lines.append(line)
            continue
        flush_table()
        if not line.strip():
            flush_paragraph(lines, paragraph)
            flush_list(lines, list_items)
            continue
        if line.startswith("# "):
            flush_paragraph(lines, paragraph)
            flush_list(lines, list_items)
            lines.append(f"<h1>{markdown_inline(line[2:].strip())}</h1>")
        elif line.startswith("## "):
            flush_paragraph(lines, paragraph)
            flush_list(lines, list_items)
            lines.append(f"<h2>{markdown_inline(line[3:].strip())}</h2>")
        elif line.startswith("### "):
            flush_paragraph(lines, paragraph)
            flush_list(lines, list_items)
            lines.append(f"<h3>{markdown_inline(line[4:].strip())}</h3>")
        elif line.startswith("- "):
            flush_paragraph(lines, paragraph)
            list_items.append(line[2:].strip())
        elif re.match(r"^\d+\.\s+", line):
            flush_paragraph(lines, paragraph)
            list_items.append(re.sub(r"^\d+\.\s+", "", line).strip())
        else:
            paragraph.append(line.strip())
    flush_table()
    flush_paragraph(lines, paragraph)
    flush_list(lines, list_items)
    return "\n".join(line for line in lines if line)


def require_https_webhook() -> str:
    webhook_url = os.environ.get("BITRIX24_WEBHOOK_URL", "").strip()
    if not webhook_url:
        raise RuntimeError("Real import is blocked. Required environment: BITRIX24_WEBHOOK_URL")
    parsed = urlparse(webhook_url)
    if parsed.scheme != "https" or not parsed.netloc:
        raise RuntimeError("BITRIX24_WEBHOOK_URL must be a valid HTTPS webhook base URL")
    return webhook_url.rstrip("/")


def require_confirm() -> None:
    confirm = os.environ.get("BITRIX24_IMPORT_CONFIRM", "").strip().lower()
    if confirm != "true":
        raise RuntimeError("Real import is blocked. Required environment: BITRIX24_IMPORT_CONFIRM=true")


def require_generic_env() -> tuple[str, str]:
    require_confirm()
    webhook_url = require_https_webhook()
    method = os.environ.get("BITRIX24_KB_IMPORT_METHOD", "").strip()
    if not method:
        raise RuntimeError("Real generic import is blocked. Required environment: BITRIX24_KB_IMPORT_METHOD")
    return webhook_url, method.lstrip("/")


def require_landing_env() -> tuple[str, str, str]:
    require_confirm()
    webhook_url = require_https_webhook()
    site_id = os.environ.get("BITRIX24_KB_SITE_ID", "").strip()
    if not site_id:
        raise RuntimeError("Real landing import is blocked. Required environment: BITRIX24_KB_SITE_ID")
    scope = os.environ.get("BITRIX24_KB_SCOPE", DEFAULT_SCOPE).strip() or DEFAULT_SCOPE
    return webhook_url, site_id, scope


def post_json(url: str, payload: dict[str, Any], timeout: float) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:  # noqa: S310 - explicit operator-provided webhook URL.
        return json.loads(response.read().decode("utf-8"))


def call_bitrix(webhook_url: str, method: str, params: dict[str, Any], timeout: float) -> dict[str, Any]:
    endpoint = f"{webhook_url}/{method}.json"
    response = post_json(endpoint, params, timeout)
    if "error" in response:
        error_description = response.get("error_description", response["error"])
        raise RuntimeError(f"{method}: {error_description}")
    return response


def extract_result_id(response: dict[str, Any]) -> Any:
    result = response.get("result")
    if isinstance(result, dict):
        for key in ("ID", "id", "LID", "lid"):
            if key in result:
                return result[key]
    return result


def build_generic_payload(payload: dict[str, Any], section: dict[str, Any], article: dict[str, Any]) -> dict[str, Any]:
    return {
        "knowledgeBase": payload["knowledge_base"],
        "section": {"number": section["number"], "title": section["title"], "order": section["order"]},
        "article": article,
    }


def build_landing_actions(payload: dict[str, Any], site_id: str | None, scope: str) -> list[ImportAction]:
    actions: list[ImportAction] = []
    if site_id:
        actions.append(
            ImportAction(
                "landing.site.getList",
                {"params": {"filter": {"ID": site_id}}, "scope": scope},
                f"Проверить сайт базы знаний SITE_ID={site_id}",
            )
        )
    else:
        actions.append(
            ImportAction(
                "landing.site.getList",
                {
                    "params": {
                        "filter": {
                            "CODE": os.environ.get("BITRIX24_KB_SITE_CODE", DEFAULT_SITE_CODE),
                            "TITLE": os.environ.get("BITRIX24_KB_SITE_TITLE", DEFAULT_SITE_TITLE),
                        }
                    },
                    "scope": scope,
                },
                "Найти сайт базы знаний по коду или названию",
            )
        )

    for section in payload["sections"]:
        section_code = f"{section['number']}-{slugify(section['title'])}"
        actions.append(
            ImportAction(
                "landing.site.addFolder",
                {
                    "fields": {
                        "SITE_ID": site_id or "<BITRIX24_KB_SITE_ID>",
                        "TITLE": f"{section['number']}. {section['title']}",
                        "CODE": section_code,
                        "INDEX": section["order"],
                    },
                    "scope": scope,
                },
                f"Создать или проверить раздел {section['number']}. {section['title']}",
            )
        )
        for article in section["articles"]:
            article_code = f"{article['number'].replace('.', '-')}-{slugify(article['title'])}"
            article_title = f"{article['number']}. {article['title']}"
            html_content = markdown_to_html(article["markdown"])
            actions.extend(
                [
                    ImportAction(
                        "landing.landing.add",
                        {
                            "fields": {
                                "SITE_ID": site_id or "<BITRIX24_KB_SITE_ID>",
                                "TITLE": article_title,
                                "CODE": article_code,
                                "FOLDER_ID": f"<folder:{section_code}>",
                            },
                            "scope": scope,
                        },
                        f"Создать страницу статьи {article_title}",
                    ),
                    ImportAction(
                        "landing.landing.addblock",
                        {
                            "lid": f"<landing:{article_code}>",
                            "fields": {"CODE": os.environ.get("BITRIX24_KB_BLOCK_CODE", DEFAULT_BLOCK_CODE)},
                            "scope": scope,
                        },
                        f"Добавить контентный блок для статьи {article_title}",
                    ),
                    ImportAction(
                        "landing.block.updatecontent",
                        {
                            "block": f"<block:{article_code}>",
                            "content": html_content,
                            "scope": scope,
                        },
                        f"Заполнить HTML-контент статьи {article_title}",
                    ),
                    ImportAction(
                        "landing.landing.publication",
                        {"lid": f"<landing:{article_code}>", "scope": scope},
                        f"Опубликовать страницу статьи {article_title}",
                    ),
                ]
            )
    actions.append(
        ImportAction(
            "landing.site.publication",
            {"id": site_id or "<BITRIX24_KB_SITE_ID>", "scope": scope},
            "Опубликовать сайт базы знаний",
        )
    )
    return actions


def write_dry_run_report(payload: dict[str, Any], actions: list[ImportAction], path: Path) -> None:
    sections_count = len(payload["sections"])
    articles_count = sum(len(section["articles"]) for section in payload["sections"])
    lines = [
        "# Bitrix24 dry-run import report — Технический справочник «Эверест»",
        "",
        "## Результат",
        "",
        "- HTTP-запросы в Bitrix24: не выполнялись",
        f"- Разделов в плане: {sections_count}",
        f"- Статей в плане: {articles_count}",
        f"- REST-действий в плане: {len(actions)}",
        "- Реальный импорт заблокирован без `--execute` и `BITRIX24_IMPORT_CONFIRM=true`",
        "",
        "## Первые действия плана",
        "",
    ]
    for action in actions[:20]:
        lines.append(f"- `{action.method}` — {action.label}")
    if len(actions) > 20:
        lines.append(f"- ... ещё {len(actions) - 20} действий")
    lines.append("")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def run_dry_run(payload: dict[str, Any], adapter: str, report_path: Path, scope: str) -> int:
    articles = list(iter_articles(payload))
    if adapter == "landing":
        actions = build_landing_actions(payload, os.environ.get("BITRIX24_KB_SITE_ID"), scope)
    else:
        actions = [
            ImportAction("<BITRIX24_KB_IMPORT_METHOD>", build_generic_payload(payload, section, article), article["title"])
            for section, article in articles
        ]
    write_dry_run_report(payload, actions, report_path)
    print("DRY-RUN: Bitrix24 API was not called.")
    print(f"Knowledge base: {payload['knowledge_base']}")
    print(f"Sections: {len(payload['sections'])}")
    print(f"Articles: {len(articles)}")
    print(f"Adapter: {adapter}")
    print(f"Planned REST actions: {len(actions)}")
    print(f"Dry-run report: {report_path}")
    print("Use --execute and BITRIX24_IMPORT_CONFIRM=true for real import.")
    return 0


def run_generic_import(payload: dict[str, Any], timeout: float, sleep: float) -> int:
    webhook_url, method = require_generic_env()
    articles = list(iter_articles(payload))
    endpoint = f"{webhook_url}/{method}.json"
    print(f"EXECUTE: importing {len(articles)} articles to {mask_url(endpoint)}")
    for section, article in articles:
        try:
            response = call_bitrix(webhook_url, method, build_generic_payload(payload, section, article), timeout)
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, RuntimeError) as exc:
            print(f"Import failed for article {article['number']}: {exc}", file=sys.stderr)
            return 1
        print(f"Imported candidate: {article['number']}. {article['title']} -> {extract_result_id(response)}")
        time.sleep(sleep)
    return 0


def run_landing_import(payload: dict[str, Any], timeout: float, sleep: float, limit: int | None) -> int:
    webhook_url, site_id, scope = require_landing_env()
    actions = build_landing_actions(payload, site_id, scope)
    if limit is not None:
        actions = actions[:limit]
    print(f"EXECUTE: running {len(actions)} landing REST actions against {mask_url(webhook_url)}")
    for index, action in enumerate(actions, start=1):
        try:
            response = call_bitrix(webhook_url, action.method, action.params, timeout)
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, RuntimeError) as exc:
            print(f"Import failed at action {index}: {action.method} — {action.label}: {exc}", file=sys.stderr)
            return 1
        print(f"{index}/{len(actions)} {action.method}: {action.label} -> {extract_result_id(response)}")
        time.sleep(sleep)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Import Everest knowledge base into Bitrix24 via REST webhook.")
    parser.add_argument("--input", type=Path, default=DEFAULT_EXPORT, help="Path to generated JSON export.")
    parser.add_argument("--adapter", choices=("landing", "generic"), default="landing", help="Import adapter.")
    parser.add_argument("--dry-run-report", type=Path, default=DEFAULT_DRY_RUN_REPORT, help="Dry-run report path.")
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Allow real HTTP import when required environment variables are set.",
    )
    parser.add_argument("--timeout", type=float, default=15.0, help="HTTP timeout for real import.")
    parser.add_argument("--sleep", type=float, default=0.2, help="Pause between real import requests.")
    parser.add_argument(
        "--limit-actions",
        type=int,
        default=None,
        help="Limit real landing REST actions for controlled test imports.",
    )
    args = parser.parse_args()

    payload = load_payload(args.input)
    scope = os.environ.get("BITRIX24_KB_SCOPE", DEFAULT_SCOPE).strip() or DEFAULT_SCOPE
    if not args.execute:
        return run_dry_run(payload, args.adapter, args.dry_run_report, scope)

    try:
        if args.adapter == "generic":
            return run_generic_import(payload, args.timeout, args.sleep)
        return run_landing_import(payload, args.timeout, args.sleep, args.limit_actions)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        if args.adapter == "generic":
            print("Required environment: " + ", ".join(REQUIRED_GENERIC_ENV), file=sys.stderr)
        else:
            print("Required environment: " + ", ".join(REQUIRED_LANDING_ENV), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
