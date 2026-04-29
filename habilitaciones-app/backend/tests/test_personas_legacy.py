"""Legacy integration tests preserved for traceability.

These tests were written against a previous structure and must be rewritten
to match the current SGH-V1 API contracts before being re-enabled.
"""

import pytest

pytestmark = pytest.mark.skip(
    reason="Legacy test set; rewrite required for current routes/schemas."
)


def test_legacy_placeholder():
    """Placeholder to keep pytest collection stable."""
    assert True
