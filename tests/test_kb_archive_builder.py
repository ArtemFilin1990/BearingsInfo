from __future__ import annotations

import json
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "knowledge-base/everest/scripts/kb-archive-builder.py"
BASE_URL = "https://ewerest.bitrix24.ru/everest-bearing-kb/"


def make_export() -> dict:
    return {
        "charset": "UTF-8",
        "type": "page",
        "name": "Старый сайт",
        "description": "Старое описание",
        "fields": {
            "TITLE": "Старый сайт",
            "LANDING_ID_INDEX": "index",
            "ADDITIONAL_FIELDS": {"THEME_USE": "N"},
        },
        "items": {
            "index": {
                "old_id": "1",
                "code": "index",
                "name": "Главная",
                "description": "Главная страница",
                "items": {},
            },
            "p11-oboznacheniya-gost-sistema": {
                "old_id": "2",
                "code": "p11-oboznacheniya-gost-sistema",
                "name": "Система обозначений по ГОСТ",
                "description": "Описание",
                "items": {
                    "#block1": {
                        "code": "08.3.one_col_fix_title_and_text",
                        "nodes": {
                            ".landing-block-node-title": ["Система обозначений по ГОСТ"],
                            ".landing-block-node-text": [
                                f'<p>См. также <a href="{BASE_URL}p12-analogi-gost-iso/">аналоги</a>.</p>'
                            ],
                        },
                        "style": {"#wrapper": ["landing-block g-pt-30 g-pb-30"]},
                    }
                },
            },
            "soput-s-rti-salniki": {
                "old_id": "3",
                "code": "soput-s-rti-salniki",
                "name": "Сальники и манжеты",
                "description": "",
                "items": {},
            },
        },
    }


def run_builder(input_path: Path, output_path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), "--input", str(input_path), "--output", str(output_path)],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )


def test_kb_archive_builder_produces_manifest(tmp_path: Path) -> None:
    input_path = tmp_path / "export.json"
    output_path = tmp_path / "kb_everest.zip"
    input_path.write_text(json.dumps(make_export(), ensure_ascii=False), encoding="utf-8")

    result = run_builder(input_path, output_path)
    assert result.returncode == 0, result.stderr + result.stdout
    assert "Импорт:" in result.stdout

    with zipfile.ZipFile(output_path) as archive:
        assert archive.namelist() == ["manifest.json"]
        manifest = json.loads(archive.read("manifest.json").decode("utf-8"))

    # Metadata
    assert manifest["type"] == "knowledge"
    assert manifest["name"] == "Технический справочник: подшипники и промышленная продукция"
    assert manifest["fields"]["ADDITIONAL_FIELDS"]["THEME_COLOR"] == "#EE690B"
    assert manifest["fields"]["ADDITIONAL_FIELDS"]["THEME_USE"] == "N"

    items = manifest["items"]

    # Internal links rewritten to relative paths
    article_text = items["p11-oboznacheniya-gost-sistema"]["items"]["#block1"]["nodes"][".landing-block-node-text"]
    assert any("/p12-analogi-gost-iso/" in node for node in article_text)
    assert not any(BASE_URL in node for node in article_text)

    # Navigation appended to the last text block, with breadcrumb to its section
    last_text = article_text[-1]
    assert "НАВИГАЦИЯ" in last_text
    assert "← Главная" in last_text
    assert "1. Маркировка подшипников" in last_text

    # Empty page filled with the template
    filled = items["soput-s-rti-salniki"]["items"]
    assert filled
    filled_block = next(iter(filled.values()))
    assert filled_block["nodes"][".landing-block-node-title"] == ["Сальники и манжеты"]
    assert "нет данных" in filled_block["nodes"][".landing-block-node-text"][0]

    # Index page gets a table of contents covering all navigation sections
    index_items = items["index"]["items"]
    toc_block = index_items["#block_toc_index"]
    toc_html = toc_block["nodes"][".landing-block-node-text"][0]
    assert "Содержание справочника" in toc_block["nodes"][".landing-block-node-title"]
    assert "/p11-oboznacheniya-gost-sistema/" in toc_html
    assert "/soput-s-rti-salniki/" in toc_html
    assert "Сопутствующая продукция" in toc_html


def test_kb_archive_builder_requires_input_or_execute(tmp_path: Path) -> None:
    output_path = tmp_path / "kb_everest.zip"
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--output", str(output_path)],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )
    assert result.returncode != 0
    assert "BITRIX24_EXPORT_CONFIRM" in result.stderr
    assert not output_path.exists()
