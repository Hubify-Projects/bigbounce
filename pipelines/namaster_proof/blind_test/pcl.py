"""Honest MASTER pseudo-C_l on a masked sphere, plus named shortcut variants.

The honest path is the full spin-0 MASTER estimator: measure the pseudo
spectrum of the masked map, build the mode-coupling matrix

    M_{l1 l2} = (2 l2 + 1)/(4 pi) * sum_l3 (2 l3 + 1) W_l3 (l1 l2 l3; 0 0 0)^2

from the mask power spectrum W, and solve M C = pseudo-C.  Every shortcut
variant below produces a *bandpower answer of the same shape*; the blind test
asks whether the receipts alone reveal which path was taken.
"""

from __future__ import annotations

import numpy as np

import wigner


def make_mask(nside: int, seed: int = 11) -> np.ndarray:
    """Galactic-cut-plus-patches binary mask, smoothed to soften ringing."""
    import healpy as hp

    npix = hp.nside2npix(nside)
    theta, phi = hp.pix2ang(nside, np.arange(npix))
    mask = np.ones(npix)
    mask[np.abs(np.pi / 2 - theta) < 0.18] = 0.0
    rng = np.random.default_rng(seed)
    for _ in range(12):
        vec = rng.normal(size=3)
        vec /= np.linalg.norm(vec)
        mask[hp.query_disc(nside, vec, 0.12)] = 0.0
    return mask


def make_map(nside: int, lmax: int, seed: int) -> np.ndarray:
    """Gaussian realisation of a power-law signal spectrum."""
    import healpy as hp

    ell = np.arange(lmax + 1)
    cl = np.zeros(lmax + 1)
    cl[2:] = 1.0e-3 * (ell[2:] / 10.0) ** -2.0
    return hp.synfast(cl, nside, lmax=lmax, new=True)


def pseudo_cl(sky: np.ndarray, mask: np.ndarray, lmax: int) -> np.ndarray:
    import healpy as hp

    return hp.anafast(sky * mask, lmax=lmax)


def mask_power(mask: np.ndarray, lmax: int) -> np.ndarray:
    import healpy as hp

    return hp.anafast(mask, lmax=lmax)


def coupling_matrix(w_l: np.ndarray, lmax: int, rows: np.ndarray | None = None,
                    bandwidth: int | None = None) -> np.ndarray:
    """Mode-coupling matrix.  `rows` restricts evaluated l1; `bandwidth`
    restricts |l1-l2| (both are shortcut knobs, not honest options)."""
    m = np.zeros((lmax + 1, lmax + 1))
    row_iter = range(lmax + 1) if rows is None else [int(r) for r in rows]
    for l1 in row_iter:
        for l2 in range(lmax + 1):
            if bandwidth is not None and abs(l1 - l2) > bandwidth:
                continue
            total = 0.0
            for l3 in wigner.triangle_range(l1, l2, lmax):
                total += (2 * l3 + 1) * w_l[l3] * wigner.wigner3j_000_sq(l1, l2, l3)
            m[l1, l2] = (2 * l2 + 1) / (4.0 * np.pi) * total
    return m


def decouple(m: np.ndarray, pcl: np.ndarray, lmin: int = 2) -> np.ndarray:
    """Solve M C = pseudo-C on l >= lmin (l<2 is degenerate under the cut)."""
    sub = m[lmin:, lmin:]
    out = np.zeros_like(pcl)
    out[lmin:] = np.linalg.solve(sub + 1e-12 * np.eye(sub.shape[0]), pcl[lmin:])
    return out
