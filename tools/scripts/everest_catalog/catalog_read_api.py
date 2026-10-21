#!/usr/bin/env python3
"""Private, read-only HTTP access to an UNVERIFIED EVEREST staging snapshot.

This deliberately does not implement pricing, stock, approved analogues or
product compatibility. It must not be exposed as a customer quotation API.
"""

import hmac
import json
import os
import re
import sqlite3
import unicodedata
from contextlib import closing
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, quote, urlsplit


def canonical_query(value: str) -> str:
    """Apply the same harmless text cleanup as the staging normalizer."""
    result = unicodedata.normalize("NFKC", value).upper().strip()
    return re.sub(r"\s+", " ", result.translate(str.maketrans("–—−‑", "----")))


def like_literal(value: str) -> str:
    """Escape LIKE metacharacters: designation queries are literal strings."""
    return value.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")


class SnapshotReader:
    """Open the immutable staging SQLite database exclusively in read-only mode."""

    def __init__(self, path: Path):
        self.path = path.resolve(strict=True)
        with closing(self._connect()) as db:
            self.rows = db.execute("SELECT COUNT(*) FROM stage_designations").fetchone()[0]
            self.brands = db.execute("SELECT COUNT(DISTINCT brand) FROM stage_designations").fetchone()[0]
            invalid = db.execute(
                "SELECT COUNT(*) FROM stage_designations WHERE semantic_status IS NULL OR semantic_status != 'UNVERIFIED'"
            ).fetchone()[0]
            if invalid:
                raise ValueError("Snapshot contains promoted or non-staging rows")
            provenance = db.execute(
                "SELECT ruleset, origin_blob_sha FROM stage_designations LIMIT 1"
            ).fetchone()
            if provenance is None:
                raise ValueError("Empty staging snapshot")
            self.ruleset, self.source_blob_sha = provenance

    def _connect(self):
        uri = f"file:{quote(str(self.path))}?mode=ro&immutable=1"
        db = sqlite3.connect(uri, uri=True, timeout=5)
        db.row_factory = sqlite3.Row
        db.execute("PRAGMA query_only=ON")
        return db

    def search(self, query: str, brand: str | None = None, limit: int = 20):
        needle = canonical_query(query)
        if not needle or len(needle) > 128:
            raise ValueError("q must contain 1–128 characters")
        if not (1 <= limit <= 50):
            raise ValueError("limit must be between 1 and 50")
        if brand is not None and (not brand.strip() or len(brand) > 100):
            raise ValueError("brand must contain 1–100 characters")

        pattern = like_literal(needle) + "%"
        sql = """
            SELECT source_line, brand, original_designation, normalized_designation,
                   prefix, body, suffix, bearing_type_hint, parse_status, semantic_status
            FROM stage_designations
            WHERE (normalized_designation = ? COLLATE NOCASE
                   OR body = ? COLLATE NOCASE
                   OR normalized_designation LIKE ? ESCAPE '\\'
                   OR body LIKE ? ESCAPE '\\')
        """
        args = [needle, needle, pattern, pattern]
        if brand is not None:
            sql += " AND brand = ? COLLATE NOCASE"
            args.append(brand.strip())
        sql += """
            ORDER BY CASE WHEN normalized_designation = ? COLLATE NOCASE THEN 0
                          WHEN body = ? COLLATE NOCASE THEN 1 ELSE 2 END,
                     brand, normalized_designation, source_line
            LIMIT ?
        """
        args.extend([needle, needle, limit])
        with closing(self._connect()) as db:
            rows = [dict(row) for row in db.execute(sql, args).fetchall()]
        return {
            "query": query,
            "brand_filter": brand,
            "returned": len(rows),
            "catalog_state": "UNVERIFIED",
            "commercial_use_allowed": False,
            "approved_analogues_available": False,
            "prices_available": False,
            "results": rows,
        }

    def status(self):
        return {
            "rows": self.rows,
            "brands": self.brands,
            "ruleset": self.ruleset,
            "source_blob_sha": self.source_blob_sha,
            "catalog_state": "ALL_UNVERIFIED",
            "commercial_use_allowed": False,
        }


def make_handler(reader: SnapshotReader, bearer_token: str):
    """Return a handler bound to its own reader and credential, for isolated tests."""

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, fmt, *args):
            # No user-designation query strings or Authorization headers in logs.
            pass

        def respond(self, status, value):
            content = json.dumps(value, ensure_ascii=False).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.end_headers()
            self.wfile.write(content)

        def do_GET(self):
            path = urlsplit(self.path)
            if path.path == "/health":
                self.respond(200, {"status": "ok", "service": "everest-staging-catalog"})
                return
            auth = self.headers.get("Authorization", "")
            if not hmac.compare_digest(auth, "Bearer " + bearer_token):
                self.respond(401, {"error": "Unauthorized"})
                return
            if path.path == "/v1/staging/status":
                self.respond(200, reader.status())
                return
            if path.path != "/v1/staging/search":
                self.respond(404, {"error": "Not found"})
                return
            try:
                if len(path.query) > 2048:
                    raise ValueError("Query string too long")
                params = parse_qs(path.query, keep_blank_values=True)
                if any(len(params.get(key, [])) != 1 for key in ("q",)):
                    raise ValueError("Exactly one q parameter is required")
                if len(params.get("brand", [])) > 1 or len(params.get("limit", [])) > 1:
                    raise ValueError("Duplicate filter parameter")
                brand = params["brand"][0] if "brand" in params else None
                limit = int(params.get("limit", ["20"])[0])
                self.respond(200, reader.search(params["q"][0], brand, limit))
            except (ValueError, KeyError) as exc:
                self.respond(400, {"error": str(exc)})

    return Handler


def main():
    bearer_token = os.environ.get("CATALOG_API_TOKEN", "")
    if len(bearer_token) < 32:
        raise SystemExit("CATALOG_API_TOKEN must be configured (minimum 32 characters)")
    path = Path(os.environ.get("CATALOG_SNAPSHOT_PATH", "/app/data/catalog.sqlite"))
    reader = SnapshotReader(path)
    if reader.rows < 42585 or reader.brands < 74:
        raise SystemExit("Incomplete staging snapshot: refusing to serve")
    port = int(os.environ.get("PORT", "10000"))
    server = ThreadingHTTPServer(("0.0.0.0", port), make_handler(reader, bearer_token))
    server.daemon_threads = True
    print(f"EVEREST staging lookup ready: {reader.rows} rows, {reader.brands} brands", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
