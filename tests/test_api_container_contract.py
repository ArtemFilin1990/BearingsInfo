"""Static protections for the startup contract; runtime smoke executes separately."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_root_container_starts_fastapi_instead_of_exit_one_cli():
    root = (ROOT / "Dockerfile").read_text(encoding="utf-8")
    assert 'CMD ["python", "manage.py"]' not in root
    assert "uvicorn main:app --app-dir src/api" in root
    assert "USER appuser" in root
    assert "HEALTHCHECK" in root
    assert "/health" in root


def test_compose_publishes_api_and_does_not_override_entrypoint():
    text = (ROOT / "docker-compose.yml").read_text(encoding="utf-8")
    first = text.split("\n  dev:", 1)[0]
    assert "command: python manage.py" not in first
    assert '"8000:8000"' in first


def test_standalone_container_is_nonroot_and_isolated():
    text = (ROOT / "deploy/docker/Dockerfile.api").read_text(encoding="utf-8")
    assert "USER bearingapi" in text
    assert "src/api" in text
    assert "HEALTHCHECK" in text
    assert "COPY --chown=bearingapi:bearingapi src/api/" in text


def test_api_does_not_report_mock_100_percent_analogues():
    text = (ROOT / "src/api/app/api.py").read_text(encoding="utf-8")
    assert '"compatibility": "100%"' not in text
    assert "ENGINEERING_APPROVAL_BACKEND_NOT_CONNECTED" in text
