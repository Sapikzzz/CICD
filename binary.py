"""This module contains utility functions for binary conversion and validation."""


def convert(a: int) -> str:
    """Converts an integer to its binary representation as a string."""
    if not isinstance(a, int):
        return False
    if a < 0 or a > 100:
        return False

    return format(a, "07b")
