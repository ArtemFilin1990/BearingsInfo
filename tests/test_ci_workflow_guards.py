"""Static regression checks protecting unreviewed data from CI mutation.

Tests are intentionally dependency-free and do not contact Cloudflare.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def workflow(name: str) -> str:
    return (ROOT / ".github" / "workflows" / name).read_text(encoding="utf-8")


def test_ci_does_not_rewrite_source_catalogue():
    ci = workflow("ci.yml")
    assert "run: python tools/scripts/deduplicate_nomenclature.py" not in ci
    assert "run: python tools/scripts/update_repo.py" not in ci
    assert "git diff --exit-code -- data/" in ci


def test_pr_validation_does_not_silence_type_errors():
    pr = workflow("pr-checks.yml")
    assert "mypy tools/scripts/ sources/ tests/ --ignore-missing-imports || true" not in pr
    assert "git diff --exit-code -- data/" in pr
    assert "All checks completed" not in pr


def test_security_audit_fails_on_vulnerable_dependencies():
    security = workflow("security.yml")
    assert "pip-audit --requirement requirements.txt || true" not in security
    assert "pip-audit --requirement requirements.txt\n" in security


def test_remote_d1_write_requires_explicit_manual_selection():
    seed = workflow("seed-database.yml")
    header = seed.split("permissions:", 1)[0]
    assert "\n  push:" not in header
    assert "workflow_dispatch:" in header
    assert "confirm_remote_write:" in seed
    assert "github.event.inputs.confirm_remote_write == 'true'" in seed
    assert "default: 'true'" in seed
    assert "          ref: main" not in seed


def test_ci_preserves_least_privilege():
    ci = workflow("ci.yml")
    assert "permissions:\n  contents: read" in ci
    pr = workflow("pr-checks.yml")
    assert "permissions:\n  contents: read" in pr
    assert "pull-requests: write" not in pr
