"""Tests for molanalysis."""

from __future__ import annotations

import molanalysis


def test_version() -> None:
    """Test that version is defined."""
    assert hasattr(molanalysis, "__version__")
    assert isinstance(molanalysis.__version__, str)


def test_all_exports() -> None:
    """Test that __all__ is defined."""
    assert hasattr(molanalysis, "__all__")
    assert isinstance(molanalysis.__all__, list)
