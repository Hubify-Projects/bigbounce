from __future__ import annotations

import numpy as np
import pytest

from namaster_proof import bandpower_edges, field_harmonic_kwargs


def test_edges_bind_declared_lmax() -> None:
    edges = bandpower_edges(nside=256, lmax=512, n_bins=10)
    assert edges[0] == 30
    assert edges[-1] == 513
    assert len(np.unique(edges)) == len(edges)


def test_purification_binds_mask_limit() -> None:
    assert field_harmonic_kwargs(lmax=512, purify_b=True) == {
        "lmax": 512,
        "lmax_mask": 512,
    }
    assert field_harmonic_kwargs(lmax=512, purify_b=False) == {"lmax": 512}


@pytest.mark.parametrize(
    "kwargs",
    [
        {"nside": 0, "lmax": 0, "n_bins": 1},
        {"nside": 8, "lmax": 24, "n_bins": 1},
        {"nside": 8, "lmax": 10, "n_bins": 0},
        {"nside": 8, "lmax": 10, "n_bins": 20},
    ],
)
def test_invalid_edges_fail_closed(kwargs: dict[str, int]) -> None:
    with pytest.raises(ValueError):
        bandpower_edges(**kwargs)
