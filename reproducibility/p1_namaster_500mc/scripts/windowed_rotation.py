"""Exact NaMaster bandpower-window response for a rotated spin-2 field."""

from __future__ import annotations

import numpy as np


def _pad_spectrum(cl: np.ndarray, n_ell: int) -> np.ndarray:
    out = np.zeros(n_ell, dtype=float)
    n_copy = min(len(cl), n_ell)
    out[:n_copy] = cl[:n_copy]
    return out


def build_rotation_response(workspace, cl_ee: np.ndarray, cl_bb: np.ndarray):
    """Precompute the exact MASTER-windowed response to a uniform rotation.

    NaMaster orders two-spin spectra as ``[EE, EB, BE, BB]`` and returns
    bandpower windows with shape ``[4, n_band, 4, lmax+1]``.  For initially
    vanishing EB, a rotation by beta can be written as a constant term plus
    cos(4 beta) and sin(4 beta) terms.  Contracting those three components
    through the workspace windows is exactly equivalent to
    ``decouple_cell(couple_cell(cls_theory))`` while avoiding any
    effective-ell or bin-centre approximation.
    """
    windows = workspace.get_bandpower_windows()
    n_ell = windows.shape[-1]
    ee = _pad_spectrum(np.asarray(cl_ee, dtype=float), n_ell)
    bb = _pad_spectrum(np.asarray(cl_bb, dtype=float), n_ell)
    sum_cl = ee + bb
    diff_cl = ee - bb

    base = np.array([0.5 * sum_cl, np.zeros(n_ell), np.zeros(n_ell),
                     0.5 * sum_cl])
    cos4 = np.array([0.5 * diff_cl, np.zeros(n_ell), np.zeros(n_ell),
                     -0.5 * diff_cl])
    sin4 = np.array([np.zeros(n_ell), 0.5 * diff_cl, 0.5 * diff_cl,
                     np.zeros(n_ell)])

    responses = np.einsum(
        "ibjl,kjl->kib", windows, np.stack([base, cos4, sin4]), optimize=True
    )
    return {
        "base": responses[0],
        "cos4": responses[1],
        "sin4": responses[2],
        "n_ell": n_ell,
        "window_shape": tuple(int(x) for x in windows.shape),
        "_base_cls": base,
        "_cos4_cls": cos4,
        "_sin4_cls": sin4,
    }


def windowed_bandpowers(response, beta_rad):
    """Return all four windowed bandpowers at one or more rotation angles."""
    beta = np.asarray(beta_rad, dtype=float)
    return (
        response["base"]
        + np.cos(4.0 * beta)[..., None, None] * response["cos4"]
        + np.sin(4.0 * beta)[..., None, None] * response["sin4"]
    )


def recover_beta_deg(cl_eb, response, grid_deg=None, weights=None, selection=None):
    """Fit beta using the exact windowed EB theory evaluated on a fixed grid."""
    grid = np.linspace(-1.0, 1.0, 2001) if grid_deg is None else np.asarray(grid_deg)
    templates = windowed_bandpowers(response, np.deg2rad(grid))[:, 1, :]
    measured = np.asarray(cl_eb, dtype=float)
    select = np.ones(measured.shape[-1], dtype=bool) if selection is None else selection
    residual = measured[..., None, select] - templates[None, :, select]
    if measured.ndim == 1:
        residual = residual[0]
    w = np.ones(np.count_nonzero(select)) if weights is None else np.asarray(weights)[select]
    chi2 = np.sum(w * residual**2, axis=-1)
    return grid[np.argmin(chi2, axis=-1)]


def validate_window_equivalence(workspace, response, beta_rad):
    """Numerically verify window contraction against couple+decouple."""
    beta = float(beta_rad)
    cls = (
        response["_base_cls"]
        + np.cos(4.0 * beta) * response["_cos4_cls"]
        + np.sin(4.0 * beta) * response["_sin4_cls"]
    )
    via_windows = windowed_bandpowers(response, beta)
    via_operator = workspace.decouple_cell(workspace.couple_cell(cls))
    return float(np.max(np.abs(via_windows - via_operator)))


def rotate_eb_spectra(cls, beta_rad):
    """Rotate an [EE, EB, BE, BB] spectrum matrix without new SHTs.

    A uniform Q/U rotation commutes with a scalar sky mask.  Therefore the
    coupled spectra of one noisy realization can be rotated algebraically and
    passed through the same linear decoupling workspace for several beta
    values.  This is exact for the convention used by ``apply_birefringence``
    in the production script and avoids repeating the expensive spherical
    harmonic transforms for identical-seed realizations.
    """
    values = np.asarray(cls, dtype=float)
    if values.shape[0] != 4:
        raise ValueError("expected NaMaster [EE, EB, BE, BB] spectrum order")
    beta = float(beta_rad)
    c = np.cos(2.0 * beta)
    s = np.sin(2.0 * beta)
    ee, eb, be, bb = values
    return np.array([
        c * c * ee - c * s * (eb + be) + s * s * bb,
        c * s * ee + c * c * eb - s * s * be - c * s * bb,
        c * s * ee - s * s * eb + c * c * be - c * s * bb,
        s * s * ee + c * s * (eb + be) + c * c * bb,
    ])
