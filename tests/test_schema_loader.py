from pathlib import Path

import pytest

from scripts.validate import csv_validator


def test_load_schema_payload_without_yaml(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    schema_path = tmp_path / "schema.yaml"
    schema_path.write_text(
        '{"tables":[{"name":"sample","path":"data/example.csv","columns":{"a":"string"},"unique":["a"],"sort_by":["a"]}]}',
        encoding="utf-8",
    )
    monkeypatch.setattr(csv_validator, "yaml", None)

    payload = csv_validator._load_schema_payload(schema_path)

    assert payload["tables"][0]["name"] == "sample"
