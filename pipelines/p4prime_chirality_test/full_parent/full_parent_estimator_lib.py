#!/usr/bin/env python3
"""Shared estimator/injection machinery for the row-16(i) full-parent dipole
test. Imports build_projector() VERBATIM from the committed P4 strict-primary
generator so the estimator is byte-identical to the one P4' cites (NSIDE=64,
support>=10, unweighted healpy.fit_dipole amplitude of per-pixel asymmetry).
No re-derivation of the estimator itself.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

import healpy as hp
import numpy as np

HERE = Path(__file__).resolve().parent
P2 = HERE.parents[1] / "p2_chirality"
_GEN_PATH = P2 / "generate_p4_primary_label_shuffle_strict_v1_0_257.py"
_spec = importlib.util.spec_from_file_location("p4_strict_gen_reuse", _GEN_PATH)
gen = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gen)

NSIDE = gen.NSIDE
MIN_PIXEL_COUNT = gen.MIN_PIXEL_COUNT
build_projector = gen.build_projector


def maps_from_radec(ra: np.ndarray, dec: np.ndarray, is_cw: np.ndarray):
    npix = hp.nside2npix(NSIDE)
    pix = hp.ang2pix(NSIDE, np.radians(90.0 - dec), np.radians(ra % 360.0))
    total = np.bincount(pix, minlength=npix).astype(np.int64)
    cw = np.bincount(pix[is_cw], minlength=npix).astype(np.int64)
    return total, cw


def fixed_occupancy_null(capacities: np.ndarray, projector: np.ndarray,
                          n_cw: int, n_draws: int, seed: int) -> np.ndarray:
    """EXACT null convention as generate_p4_primary_label_shuffle_strict_v1_0_257.py."""
    rng = np.random.default_rng(seed)
    amps = np.empty(n_draws, dtype=np.float64)
    for i in range(n_draws):
        shuffled_cw = rng.multivariate_hypergeometric(capacities, n_cw, method="marginals")
        coeff = projector @ ((2.0 * shuffled_cw - capacities) / capacities)
        amps[i] = np.linalg.norm(coeff[1:])
    return amps


def detection_fraction(A: float, capacities: np.ndarray, n_hat: np.ndarray,
                        projector: np.ndarray, p_global: float,
                        null_sorted: np.ndarray, n_axes: int, rng,
                        alpha: float = 0.05, chunk: int = 250) -> float:
    """EXACT injection convention as a95_observed_label_upper_limit_v1_0_265.py."""
    capf = capacities.astype(np.float64)
    Nnull = null_sorted.size
    detected = np.zeros(n_axes, dtype=bool)
    done = 0
    while done < n_axes:
        m = min(chunk, n_axes - done)
        u = rng.standard_normal((3, m))
        u /= np.linalg.norm(u, axis=0, keepdims=True)
        cos = n_hat @ u
        p = p_global + 0.5 * A * cos
        np.clip(p, 1e-6, 1.0 - 1e-6, out=p)
        n_cw = rng.binomial(capacities[:, None], p)
        mapvals = (2.0 * n_cw - capf[:, None]) / capf[:, None]
        coef = projector @ mapvals
        amp = np.linalg.norm(coef[1:4, :], axis=0)
        ge = Nnull - np.searchsorted(null_sorted, amp, side="left")
        rank_p = (ge + 1.0) / (Nnull + 1.0)
        detected[done:done + m] = rank_p < alpha
        done += m
    return float(detected.mean())


def invert_a95(grid: np.ndarray, pdet: np.ndarray, target: float = 0.95):
    order = np.argsort(grid)
    g, pv = grid[order], pdet[order]
    for i in range(len(g) - 1):
        if pv[i] < target <= pv[i + 1] and pv[i + 1] > pv[i]:
            frac = (target - pv[i]) / (pv[i + 1] - pv[i])
            return float(g[i] + frac * (g[i + 1] - g[i])), [float(g[i]), float(g[i + 1]), float(pv[i]), float(pv[i + 1])]
    return None, None
