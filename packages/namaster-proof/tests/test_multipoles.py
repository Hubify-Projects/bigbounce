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


@pytest.mark.parametrize("value", [512.5, np.float64(512.0), True])
def test_field_limit_rejects_non_integer_inputs(value: object) -> None:
    with pytest.raises(ValueError, match="lmax must be an integer"):
        field_harmonic_kwargs(lmax=value, purify_b=True)  # type: ignore[arg-type]


@pytest.mark.parametrize(
    ("name", "kwargs"),
    [
        ("nside", {"nside": 8.0, "lmax": 10, "n_bins": 2}),
        ("lmax", {"nside": 8, "lmax": 10.5, "n_bins": 2}),
        ("n_bins", {"nside": 8, "lmax": 10, "n_bins": 2.0}),
        ("ell_min", {"nside": 8, "lmax": 10, "n_bins": 2, "ell_min": 3.5}),
    ],
)
def test_edges_reject_non_integer_inputs(
    name: str, kwargs: dict[str, object]
) -> None:
    with pytest.raises(ValueError, match=rf"{name} must be an integer"):
        bandpower_edges(**kwargs)  # type: ignore[arg-type]


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
