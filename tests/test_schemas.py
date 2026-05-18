from pathlib import Path

from scripts.validate.csv_validator import validate_all


def test_all_schemas_pass() -> None:
    schema_dir = Path(__file__).resolve().parents[1] / "data" / "schemas"
    errors = validate_all(schema_dir)
    assert errors == []
