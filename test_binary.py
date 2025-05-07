"""This is a test file for the utils module."""

import pytest
import binary


@pytest.mark.parametrize(
    "a, expected ", [(1, "0000001"), (2, "0000010"), (64, "1000000"), (79, "1001111")]
)
def test_convert(a, expected):
    """Tests the convert function from the binary module."""
    result = binary.convert(a)
    assert result == expected


@pytest.mark.parametrize("a, expected ", [(1, "0000001"), (101, False), (-1, False)])
def test_range(a, expected):
    """Tests the convert function from the binary module."""
    result = binary.convert(a)
    assert result == expected


@pytest.mark.parametrize("a, expected ", [(1, "0000001"), (1.1, False), (10.0, False)])
def test_natural(a, expected):
    """Tests the convert function from the binary module."""
    result = binary.convert(a)
    assert result == expected
