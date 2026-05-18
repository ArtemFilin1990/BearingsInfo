"""Shared pytest fixtures for all tests."""

import sys
from pathlib import Path

import pytest

# Allow tests to import from tools/scripts/ as `scripts.*`
_tools_dir = str(Path(__file__).resolve().parents[1] / "tools")
if _tools_dir not in sys.path:
    sys.path.insert(0, _tools_dir)


@pytest.fixture
def repo_root():
    """Return the repository root directory."""
    return Path(__file__).resolve().parents[1]


@pytest.fixture
def data_dir(repo_root):
    """Return the data directory."""
    return repo_root / "data"


@pytest.fixture
def schemas_dir(repo_root):
    """Return the schemas directory."""
    return repo_root / "data" / "schemas"
