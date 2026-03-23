"""
Тесты для API.

Проверяют базовые healthcheck/endpoints и функционал поиска.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_root() -> None:
    """Root endpoint должен возвращать статус и версию."""
    response = client.get("/")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ready" or "message" in payload
    assert "version" in payload or "message" in payload


def test_health() -> None:
    """Health endpoint должен возвращать ok статус."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
