"""Read-only, bearer-protected catalog lookup tests (standard library only)."""

import csv
import io
import json
import sqlite3
import tempfile
import unittest
from contextlib import closing
from pathlib import Path
from urllib.parse import urlencode

from catalog_read_api import SnapshotReader, make_handler
from normalize_snapshot import build


TOKEN = "t" * 48


class InMemorySocket:
    """Exercise the real HTTP request handler without binding a network port."""

    def __init__(self, request):
        self.request = io.BytesIO(request)
        self.response = io.BytesIO()

    def makefile(self, mode, *args):
        return self.request if "r" in mode else self.response

    def sendall(self, data):
        self.response.write(data)


class CatalogLookupTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        root = Path(self.temp.name)
        source = root / "source.csv"
        with source.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.writer(stream)
            writer.writerow(["Brand", "Product Name", "Product Link", "Analog Name", "Analog Link", "Factory"])
            writer.writerow(["GPZ", "(70)32134Л", "https://example.invalid/a", "32134", "", "factory"])
            writer.writerow(["SKF", "ШС12", "", "ШС14", "", "factory"])
            writer.writerow(["GPZ", "6205", "", "6305", "", "factory"])
        snapshot = root / "snapshot.sqlite"
        build(source, snapshot, root / "report.json", min_rows=3, min_brands=2)
        self.reader = SnapshotReader(snapshot)
        self.handler = make_handler(self.reader, TOKEN)

    def tearDown(self):
        self.temp.cleanup()

    def call(self, path, token=TOKEN):
        authorization = (f"Authorization: Bearer {token}\r\n" if token is not None else "")
        request = f"GET {path} HTTP/1.1\r\nHost: localhost\r\n{authorization}\r\n"
        transport = InMemorySocket(request.encode("ascii"))
        self.handler(transport, ("127.0.0.1", 1), object())
        head, body = transport.response.getvalue().split(b"\r\n\r\n", 1)
        status = int(head.split(b"\r\n", 1)[0].split()[1])
        payload = json.loads(body)
        return status, payload

    def test_token_required_for_catalog_and_status(self):
        for path in ("/v1/staging/search?q=6205", "/v1/staging/status"):
            self.assertEqual(self.call(path, token=None)[0], 401)
            self.assertEqual(self.call(path, token="wrong")[0], 401)
        status, health = self.call("/health", token=None)
        self.assertEqual((status, health["status"]), (200, "ok"))

    def test_approved_prices_and_analogs_are_never_returned(self):
        status, result = self.call("/v1/staging/search?" + urlencode({"q": "70-32134Л"}))
        self.assertEqual(status, 200)
        self.assertEqual(result["returned"], 1)
        self.assertFalse(result["commercial_use_allowed"])
        self.assertFalse(result["approved_analogues_available"])
        self.assertFalse(result["prices_available"])
        item = result["results"][0]
        self.assertEqual(item["normalized_designation"], "70-32134Л")
        self.assertEqual(item["semantic_status"], "UNVERIFIED")
        self.assertEqual(item["body"], "32134")
        self.assertNotIn("analogue_raw", item)
        self.assertNotIn("factory_raw", item)
        self.assertNotIn("price", item)

    def test_cyrillic_and_body_search_with_brand_filter(self):
        status, data = self.call("/v1/staging/search?" + urlencode({"q": "шс12", "brand": "SKF"}))
        self.assertEqual(status, 200)
        self.assertEqual(data["results"][0]["body"], "ШС12")
        status, data = self.call("/v1/staging/search?" + urlencode({"q": "32134", "brand": "GPZ"}))
        self.assertEqual((status, data["returned"]), (200, 1))
        status, data = self.call("/v1/staging/search?" + urlencode({"q": "32134", "brand": "SKF"}))
        self.assertEqual((status, data["returned"]), (200, 0))

    def test_wildcards_and_bad_limits_not_interpreted_as_search(self):
        for q in ("%", "_", "\\"):
            status, data = self.call("/v1/staging/search?" + urlencode({"q": q}))
            self.assertEqual((status, data["returned"]), (200, 0))
        for path in ("/v1/staging/search?q=", "/v1/staging/search?q=6205&limit=51",
                     "/v1/staging/search?q=6205&limit=oops",
                     "/v1/staging/search?q=6205&q=6305"):
            self.assertEqual(self.call(path)[0], 400)

    def test_database_is_immutable_and_status_accurate(self):
        status, value = self.call("/v1/staging/status")
        self.assertEqual(status, 200)
        self.assertEqual((value["rows"], value["brands"]), (3, 2))
        self.assertEqual(value["catalog_state"], "ALL_UNVERIFIED")
        with closing(self.reader._connect()) as conn:
            with self.assertRaises(sqlite3.OperationalError):
                conn.execute("DELETE FROM stage_designations")


if __name__ == "__main__":
    unittest.main()
