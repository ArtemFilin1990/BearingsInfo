"""Shared pytest fixtures for all tests."""

import sys
from pathlib import Path

import pytest

# Add src to path for pipeline imports
repo_root = Path(__file__).resolve().parents[1]
src_path = repo_root / "src"
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))


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
    return repo_root / "schemas"
