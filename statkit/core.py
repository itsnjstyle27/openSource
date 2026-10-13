"""Core descriptive statistics."""

from __future__ import annotations

from collections.abc import Iterable


def mean(values: Iterable[float]) -> float:
    """Return the arithmetic mean of ``values``.

    >>> mean([1, 2, 3])
    2.0
    """
    data = list(values)
    return sum(data) / len(data)
