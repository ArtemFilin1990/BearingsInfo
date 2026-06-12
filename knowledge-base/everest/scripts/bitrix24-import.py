#!/usr/bin/env python3
"""Dry-run first Bitrix24 REST webhook importer for the Everest knowledge base."""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

from kb_common import GENERATED_DIR

DEFAULT_EXPORT = GENERATED_DIR / "json" / "bitrix24-import.json"


def mask_url(url: str) -> str:
    parsed = urlparse(url)
    if not parsed.scheme or not parsed.netloc:
        return "<invalid-url>"
    return f"{parsed.scheme}://{parsed.netloc}/***"


def load_payload(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def iter_articles(payload: dict):
    for section in payload["sections"]:
        for article in section["articles"]:
            yield section, article


def require_real_import_env() -> tuple[str, str]:
    webhook_url = os.environ.get("BITRIX24_WEBHOOK_URL", "").strip()
    method = os.environ.get("BITRIX24_KB_IMPORT_METHOD", "").strip()
    confirm = os.environ.get("BITRIX24_IMPORT_CONFIRM", "").strip().lower()
    missing = []
    if not webhook_url:
        missing.append("BITRIX24_WEBHOOK_URL")
    if not method:
        missing.append("BITRIX24_KB_IMPORT_METHOD")
    if confirm != "true":
        missing.append("BITRIX24_IMPORT_CONFIRM=true")
    if missing:
        raise RuntimeError("Real import is blocked. Required environment: " + ", ".join(missing))
    parsed = urlparse(webhook_url)
    if parsed.scheme != "https" or not parsed.netloc:
        raise RuntimeError("BITRIX24_WEBHOOK_URL must be a valid HTTPS webhook base URL")
    return webhook_url.rstrip("/"), method.lstrip("/")


def post_json(url: str, payload: dict, timeout: float) -> dict:
    request = urllib.request.Request(
        url,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:  # noqa: S310 - URL is explicit operator-provided env input.
        return json.loads(response.read().decode("utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Import Everest knowledge base into Bitrix24 via REST webhook.")
    parser.add_argument("--input", type=Path, default=DEFAULT_EXPORT, help="Path to generated JSON export.")
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Allow real HTTP import when BITRIX24_IMPORT_CONFIRM=true.",
    )
    parser.add_argument("--timeout", type=float, default=15.0, help="HTTP timeout for real import.")
    parser.add_argument("--sleep", type=float, default=0.2, help="Pause between real import requests.")
    args = parser.parse_args()

    payload = load_payload(args.input)
    articles = list(iter_articles(payload))
    if not args.execute:
        print("DRY-RUN: Bitrix24 API was not called.")
        print(f"Knowledge base: {payload['knowledge_base']}")
        print(f"Sections: {len(payload['sections'])}")
        print(f"Articles: {len(articles)}")
        print("Use --execute and BITRIX24_IMPORT_CONFIRM=true for real import.")
        return 0

    try:
        webhook_url, method = require_real_import_env()
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    endpoint = f"{webhook_url}/{method}.json"
    print(f"EXECUTE: importing {len(articles)} articles to {mask_url(endpoint)}")
    for section, article in articles:
        request_payload = {
            "knowledgeBase": payload["knowledge_base"],
            "section": {"number": section["number"], "title": section["title"], "order": section["order"]},
            "article": article,
        }
        try:
            response = post_json(endpoint, request_payload, args.timeout)
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            print(f"Import failed for article {article['number']}: {exc}", file=sys.stderr)
            return 1
        if "error" in response:
            error_description = response.get("error_description", response["error"])
            print(
                f"Bitrix24 returned error for article {article['number']}: {error_description}",
                file=sys.stderr,
            )
            return 1
        print(f"Imported candidate: {article['number']}. {article['title']}")
        time.sleep(args.sleep)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
