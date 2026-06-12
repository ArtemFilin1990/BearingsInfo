from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run_script(path: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(ROOT / path)],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )


def test_everest_generator_and_validator() -> None:
    generated = run_script("knowledge-base/everest/scripts/generate-knowledge-base.py")
    assert generated.returncode == 0, generated.stderr + generated.stdout

    validated = run_script("knowledge-base/everest/scripts/validate-knowledge-base.py")
    assert validated.returncode == 0, validated.stderr + validated.stdout
    assert "Validation passed" in validated.stdout


def test_bitrix24_import_defaults_to_dry_run() -> None:
    imported = run_script("knowledge-base/everest/scripts/bitrix24-import.py")
    assert imported.returncode == 0, imported.stderr + imported.stdout
    assert "DRY-RUN: Bitrix24 API was not called." in imported.stdout
    assert "Articles: 148" in imported.stdout


def test_everest_source_structure_has_required_counts_and_related_articles() -> None:
    sections = json.loads((ROOT / "knowledge-base/everest/source/sections.json").read_text(encoding="utf-8"))[
        "sections"
    ]
    articles = json.loads((ROOT / "knowledge-base/everest/source/articles.json").read_text(encoding="utf-8"))[
        "articles"
    ]
    article_numbers = {article["number"] for article in articles}

    assert len(sections) == 8
    assert len(articles) == 148
    assert len(article_numbers) == 148
    for article in articles:
        assert len(article["related_articles"]) == 3
        assert len(set(article["related_articles"])) == 3
        assert set(article["related_articles"]).issubset(article_numbers)
