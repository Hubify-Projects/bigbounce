"""Shared multipole limits for the P1B NaMaster production suite."""

from __future__ import annotations

import numpy as np


def field_harmonic_kwargs(*, lmax: int, purify_b: bool) -> dict[str, int]:
    """Return NaMaster field limits consistent with the production spectrum.

    Purification internally transforms the mask. Its harmonic limit must
    therefore match the field limit instead of using NaMaster's default.
    """
    kwargs = {"lmax": lmax}
    if purify_b:
        kwargs["lmax_mask"] = lmax
    return kwargs


def bandpower_edges(*, nside: int, lmax: int, n_bins: int, ell_min: int = 30):
    """Return bin edges whose inclusive maximum is exactly ``lmax``.

    ``NmtBin.from_edges`` treats each upper edge as exclusive, so the last
    edge must be ``lmax + 1``.  Every ``NmtField`` using these bins must also
    receive ``lmax=lmax``; leaving the field at its HEALPix default
    ``3*nside-1`` creates an inconsistent workspace.
    """
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
