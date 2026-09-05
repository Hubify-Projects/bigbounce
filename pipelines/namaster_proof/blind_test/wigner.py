"""Wigner 3j symbols with all-zero magnetic quantum numbers.

Closed form (Edmonds 1957, eq. 3.7.17) for (l1 l2 l3; 0 0 0), evaluated in
log-gamma space so that l ~ few hundred does not overflow.  The module keeps a
process-global evaluation counter: the blind shortcut-detection test uses it as
an *instrumented* trace field, i.e. a measured consequence of the code path
taken rather than an analyst-typed assertion.
"""

from __future__ import annotations

from math import lgamma, exp, sqrt

_COUNTER = {"n": 0}


def reset_counter() -> None:
    _COUNTER["n"] = 0


def counter() -> int:
    return _COUNTER["n"]


def _lfact(n: int) -> float:
    return lgamma(n + 1.0)


def wigner3j_000(l1: int, l2: int, l3: int) -> float:
    """Return (l1 l2 l3; 0 0 0).  Counts one evaluation per call."""
    _COUNTER["n"] += 1
    if l3 < abs(l1 - l2) or l3 > l1 + l2:
        return 0.0
    L = l1 + l2 + l3
    if L % 2:
        return 0.0
    g = L // 2
    log = 0.5 * (
        _lfact(L - 2 * l1) + _lfact(L - 2 * l2) + _lfact(L - 2 * l3) - _lfact(L + 1)
    )
    log += _lfact(g) - _lfact(g - l1) - _lfact(g - l2) - _lfact(g - l3)
    return (-1.0) ** g * exp(log)


def wigner3j_000_sq(l1: int, l2: int, l3: int) -> float:
    v = wigner3j_000(l1, l2, l3)
    return v * v


def triangle_range(l1: int, l2: int, lmax3: int) -> range:
    return range(abs(l1 - l2), min(l1 + l2, lmax3) + 1)


__all__ = [
    "reset_counter",
    "counter",
    "wigner3j_000",
    "wigner3j_000_sq",
    "triangle_range",
    "sqrt",
]
