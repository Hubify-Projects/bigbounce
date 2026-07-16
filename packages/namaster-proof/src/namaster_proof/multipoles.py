"""Deterministic harmonic limits shared by NaMaster fields and bins."""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray


def field_harmonic_kwargs(*, lmax: int, purify_b: bool) -> dict[str, int]:
    """Return field limits that keep purification on the declared support."""
    if lmax < 0:
        raise ValueError("lmax must be non-negative")
    kwargs = {"lmax": lmax}
    if purify_b:
        kwargs["lmax_mask"] = lmax
    return kwargs


def bandpower_edges(
    *, nside: int, lmax: int, n_bins: int, ell_min: int = 30
) -> NDArray[np.int_]:
    """Return integer bin edges whose final exclusive edge is ``lmax + 1``."""
    if nside <= 0:
        raise ValueError("nside must be positive")
    if not 0 <= lmax <= 3 * nside - 1:
        raise ValueError("lmax must lie inside the HEALPix harmonic support")
    if not 0 <= ell_min <= lmax:
        raise ValueError("ell_min must not exceed lmax")
    if n_bins <= 0:
        raise ValueError("n_bins must be positive")
    edges = np.linspace(ell_min, lmax + 1, n_bins + 1, dtype=int)
    if len(np.unique(edges)) != len(edges):
        raise ValueError("requested bin count creates duplicate integer edges")
    return edges
