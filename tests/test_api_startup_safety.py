"""API smoke regressions: use the real FastAPI app, no network/database mutation."""
from __future__ import annotations

import importlib
import sys
from pathlib import Path

from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[1]
API_DIR = str(ROOT / "src" / "api")
if API_DIR not in sys.path:
    sys.path.insert(0, API_DIR)


def load_api(monkeypatch, origins: str = ""):
    monkeypatch.setenv("BEARINGS_CORS_ORIGINS", origins)
    if "main" in sys.modules:
        return importlib.reload(sys.modules["main"]).app
    return importlib.import_module("main").app


def test_health_and_docs(monkeypatch):
    client = TestClient(load_api(monkeypatch))
    assert client.get("/health").json() == {"status": "healthy"}
    assert client.get("/").status_code == 200
    assert client.get("/openapi.json").status_code == 200


def test_no_wildcard_cross_origin_by_default(monkeypatch):
    client = TestClient(load_api(monkeypatch))
    r = client.options(
        "/health",
        headers={"Origin": "https://untrusted.example", "Access-Control-Request-Method": "GET"},
    )
    assert r.headers.get("access-control-allow-origin") != "*"
    assert r.headers.get("access-control-allow-origin") != "https://untrusted.example"


def test_explicit_cors_allowlist_only(monkeypatch):
    client = TestClient(load_api(monkeypatch, "https://staging.ewerest.ru"))
    r = client.get("/health", headers={"Origin": "https://staging.ewerest.ru"})
    assert r.headers["access-control-allow-origin"] == "https://staging.ewerest.ru"
    outside = client.get("/health", headers={"Origin": "https://untrusted.example"})
    assert outside.headers.get("access-control-allow-origin") != "https://untrusted.example"


def test_reject_wildcard_credentialed_cors(monkeypatch):
    import pytest

    with pytest.raises(RuntimeError, match="concrete origins"):
        load_api(monkeypatch, "*")


def test_unverified_analogue_export_never_claims_100_percent(monkeypatch):
    client = TestClient(load_api(monkeypatch))
    for extension in ("json", "csv", "xlsx"):
        response = client.get(f"/analogs/6205/export?export_format={extension}")
        assert response.status_code == 503
        payload = response.json()["detail"]
        assert payload["auto_replace_allowed"] is False
        assert payload["code"] == "ENGINEERING_APPROVAL_BACKEND_NOT_CONNECTED"
        assert "100%" not in response.text


def test_search_endpoint_available_without_catalogue_seed(monkeypatch):
    client = TestClient(load_api(monkeypatch))
    r = client.get("/search?q=6205")
    assert r.status_code == 200
    assert "results" in r.json()


def test_catalogue_readiness_requires_loaded_indexes(monkeypatch):
    app = load_api(monkeypatch)
    api_module = importlib.import_module("main")
    monkeypatch.setattr(api_module.search_engine, "documents", {})
    monkeypatch.setattr(api_module.autocomplete_engine, "terms", [])
    client = TestClient(app)
    assert client.get("/health").status_code == 200
    response = client.get("/ready")
    assert response.status_code == 503
    assert response.json() == {
        "status": "not_ready",
        "catalogue_index": False,
        "autocomplete_index": False,
        "auto_replace_allowed": False,
    }


def test_catalogue_ready_only_with_both_indexes(monkeypatch):
    app = load_api(monkeypatch)
    api_module = importlib.import_module("main")
    monkeypatch.setattr(api_module.search_engine, "documents", {"6205": {"title": "6205"}})
    monkeypatch.setattr(api_module.autocomplete_engine, "terms", [{"value": "6205"}])
    response = TestClient(app).get("/ready")
    assert response.status_code == 200
    assert response.json()["status"] == "ready"
    assert response.json()["auto_replace_allowed"] is False
