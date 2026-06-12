#!/usr/bin/env python3
"""Dry-run first Bitrix24 Knowledge Base 2.0 hierarchy creator for the Everest knowledge base.

Creates (or reuses) the KNOWLEDGE-scope landing site, one folder per top-level
section and one page per article, then publishes folders and pages so they
become visible in Bitrix24. Progress is persisted so the script can be
re-run safely without creating duplicates.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from urllib.parse import urlparse

from kb_common import GENERATED_DIR, KB_TITLE, load_articles, load_sections

SCOPE = "KNOWLEDGE"
STATE_PATH = GENERATED_DIR / "json" / "bitrix24-hierarchy-ids.json"


def mask_url(url: str) -> str:
    parsed = urlparse(url)
    if not parsed.scheme or not parsed.netloc:
        return "<invalid-url>"
    return f"{parsed.scheme}://{parsed.netloc}/***"


def require_real_import_env() -> str:
    webhook_url = os.environ.get("BITRIX24_WEBHOOK_URL", "").strip()
    confirm = os.environ.get("BITRIX24_IMPORT_CONFIRM", "").strip().lower()
    missing = []
    if not webhook_url:
        missing.append("BITRIX24_WEBHOOK_URL")
    if confirm != "true":
        missing.append("BITRIX24_IMPORT_CONFIRM=true")
    if missing:
        raise RuntimeError("Real run is blocked. Required environment: " + ", ".join(missing))
    parsed = urlparse(webhook_url)
    if parsed.scheme != "https" or not parsed.netloc:
        raise RuntimeError("BITRIX24_WEBHOOK_URL must be a valid HTTPS webhook base URL")
    return webhook_url.rstrip("/")


def call(webhook_url: str, method: str, payload: dict, timeout: float) -> dict:
    url = f"{webhook_url}/{method}.json"
    request = urllib.request.Request(
        url,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:  # noqa: S310 - URL is explicit operator-provided env input.
        return json.loads(response.read().decode("utf-8"))


def checked_call(webhook_url: str, method: str, payload: dict, timeout: float, context: str) -> dict:
    try:
        response = call(webhook_url, method, payload, timeout)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"{method} failed for {context}: {exc}") from exc
    if "error" in response:
        error_description = response.get("error_description", response["error"])
        raise RuntimeError(f"{method} returned error for {context}: {error_description}")
    return response


def load_state() -> dict:
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text(encoding="utf-8"))
    return {"site_id": None, "sections": {}}


def save_state(state: dict) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def group_articles_by_section(articles: list[dict]) -> dict[str, list[dict]]:
    by_section: dict[str, list[dict]] = {}
    for article in articles:
        by_section.setdefault(article["section_number"], []).append(article)
    for group in by_section.values():
        group.sort(key=lambda a: a["order"])
    return by_section


def print_plan(sections: list[dict], by_section: dict[str, list[dict]]) -> None:
    total_articles = sum(len(items) for items in by_section.values())
    print("DRY-RUN: Bitrix24 API was not called.")
    print(f"Knowledge base: {KB_TITLE}")
    print(f"Sections: {len(sections)}")
    print(f"Articles: {total_articles}")
    print("Planned calls:")
    print("  1. landing.site.getList (scope=KNOWLEDGE) - find existing site by TITLE")
    print("  2. landing.site.add (scope=KNOWLEDGE, TYPE=KNOWLEDGE) - create site if not found")
    for section in sections:
        items = by_section.get(section["number"], [])
        print(f"  3. landing.site.addFolder - folder '{section['number']}. {section['title']}' ({len(items)} articles)")
        for article in items:
            print(f"     landing.landing.add - page '{article['number']}. {article['title']}'")
    print("  4. landing.landing.publication for each created folder and page")
    print("Use --execute and BITRIX24_IMPORT_CONFIRM=true with a https BITRIX24_WEBHOOK_URL for the real run.")


def ensure_site(webhook_url: str, state: dict, timeout: float) -> int:
    if state.get("site_id"):
        return state["site_id"]
    response = checked_call(
        webhook_url,
        "landing.site.getList",
        {"scope": SCOPE, "params": {"select": ["ID", "TITLE"], "filter": {"=TITLE": KB_TITLE}}},
        timeout,
        "find knowledge base site",
    )
    existing = response.get("result") or []
    if existing:
        site_id = int(existing[0]["ID"])
    else:
        response = checked_call(
            webhook_url,
            "landing.site.add",
            {
                "scope": SCOPE,
                "fields": {
                    "TITLE": KB_TITLE,
                    "TYPE": SCOPE,
                    "DESCRIPTION": "База знаний 2.0 — Технический справочник «Эверест»",
                },
            },
            timeout,
            "create knowledge base site",
        )
        site_id = response["result"]
    state["site_id"] = site_id
    save_state(state)
    return site_id


def ensure_folder(webhook_url: str, site_id: int, section: dict, section_state: dict, timeout: float) -> int:
    if section_state.get("folder_id"):
        return section_state["folder_id"]
    response = checked_call(
        webhook_url,
        "landing.site.addFolder",
        {
            "scope": SCOPE,
            "siteId": site_id,
            "fields": {"TITLE": f"{section['number']}. {section['title']}", "ACTIVE": "Y"},
        },
        timeout,
        f"create folder for section {section['number']}",
    )
    folder_id = response["result"]
    section_state["folder_id"] = folder_id
    return folder_id


def ensure_article_page(
    webhook_url: str, site_id: int, folder_id: int, article: dict, section_state: dict, timeout: float
) -> int:
    existing = section_state["articles"].get(article["number"])
    if existing:
        return existing
    response = checked_call(
        webhook_url,
        "landing.landing.add",
        {
            "scope": SCOPE,
            "fields": {
                "LANDING": {
                    "TITLE": f"{article['number']}. {article['title']}",
                    "SITE_ID": site_id,
                    "FOLDER_ID": folder_id,
                }
            },
        },
        timeout,
        f"create page for article {article['number']}",
    )
    page_id = response["result"]
    section_state["articles"][article["number"]] = page_id
    return page_id


def publish(webhook_url: str, lid: int, timeout: float, context: str) -> None:
    checked_call(webhook_url, "landing.landing.publication", {"scope": SCOPE, "lid": lid}, timeout, context)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create the Bitrix24 Knowledge Base 2.0 hierarchy for the Everest knowledge base."
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Allow real HTTP calls when BITRIX24_IMPORT_CONFIRM=true.",
    )
    parser.add_argument("--timeout", type=float, default=15.0, help="HTTP timeout for real calls.")
    parser.add_argument("--sleep", type=float, default=0.3, help="Pause between real requests.")
    args = parser.parse_args()

    sections = sorted(load_sections(), key=lambda s: s["order"])
    by_section = group_articles_by_section(load_articles())

    if not args.execute:
        print_plan(sections, by_section)
        return 0

    try:
        webhook_url = require_real_import_env()
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    state = load_state()

    try:
        site_id = ensure_site(webhook_url, state, args.timeout)
        print(f"Site ID: {site_id} ({mask_url(webhook_url)})")

        for section in sections:
            section_state = state["sections"].setdefault(section["number"], {"folder_id": None, "articles": {}})
            folder_id = ensure_folder(webhook_url, site_id, section, section_state, args.timeout)
            save_state(state)
            time.sleep(args.sleep)

            for article in by_section.get(section["number"], []):
                page_id = ensure_article_page(webhook_url, site_id, folder_id, article, section_state, args.timeout)
                save_state(state)
                publish(webhook_url, page_id, args.timeout, f"publish article {article['number']}")
                time.sleep(args.sleep)
                print(f"Created/verified: {article['number']}. {article['title']} (page {page_id})")

            publish(webhook_url, folder_id, args.timeout, f"publish section {section['number']}")
            print(f"Section ready: {section['number']}. {section['title']} (folder {folder_id})")
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        print(f"Progress saved to {STATE_PATH}; re-run to resume.", file=sys.stderr)
        return 1

    print("Hierarchy creation complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
