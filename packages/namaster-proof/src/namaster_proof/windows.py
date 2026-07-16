"""Exact NaMaster bandpower-window responses for rotated spin-2 fields."""

from __future__ import annotations

from typing import Any

import numpy as np
from numpy.typing import ArrayLike, NDArray


def _validate_spectrum(
    cl: ArrayLike, n_ell: int, *, name: str
) -> NDArray[np.float64]:
    values = np.asarray(cl, dtype=float)
    if values.ndim != 1:
        raise ValueError(f"{name} must be one-dimensional")
    if values.shape != (n_ell,):
        raise ValueError(
            f"{name} length {values.size} does not match workspace support {n_ell}"
        )
    if not np.all(np.isfinite(values)):
        raise ValueError(f"{name} must contain only finite values")
    return values


def build_rotation_response(
    workspace: Any, cl_ee: ArrayLike, cl_bb: ArrayLike
) -> dict[str, Any]:
    """Precompute the exact MASTER-windowed uniform-rotation response.

    The workspace must return two-spin bandpower windows with shape
    ``[4, n_band, 4, n_ell]``. For initially vanishing EB, the rotated theory
    is decomposed into constant, ``cos(4 beta)``, and ``sin(4 beta)`` terms.
    """
    windows = np.asarray(workspace.get_bandpower_windows(), dtype=float)
    if windows.ndim != 4 or windows.shape[0] != 4 or windows.shape[2] != 4:
        raise ValueError(
            "expected two-spin windows shaped [4, n_band, 4, n_ell]"
        )
    if not np.all(np.isfinite(windows)):
        raise ValueError("bandpower windows must contain only finite values")
    n_ell = windows.shape[-1]
    ee = _validate_spectrum(cl_ee, n_ell, name="cl_ee")
    bb = _validate_spectrum(cl_bb, n_ell, name="cl_bb")
    sum_cl = ee + bb
    diff_cl = ee - bb

    base = np.array(
        [0.5 * sum_cl, np.zeros(n_ell), np.zeros(n_ell), 0.5 * sum_cl]
    )
    cos4 = np.array(
        [0.5 * diff_cl, np.zeros(n_ell), np.zeros(n_ell), -0.5 * diff_cl]
    )
    sin4 = np.array(
        [np.zeros(n_ell), 0.5 * diff_cl, 0.5 * diff_cl, np.zeros(n_ell)]
    )
    components = np.stack([base, cos4, sin4])
    responses = np.einsum("ibjl,kjl->kib", windows, components, optimize=True)
    return {
        "base": responses[0],
        "cos4": responses[1],
        "sin4": responses[2],
        "n_ell": n_ell,
        "window_shape": tuple(int(value) for value in windows.shape),
        "_base_cls": base,
        "_cos4_cls": cos4,
        "_sin4_cls": sin4,
    }


def windowed_bandpowers(
    response: dict[str, Any], beta_rad: ArrayLike
) -> NDArray[np.float64]:
    """Return all four exact-window bandpowers at one or more angles."""
    beta = np.asarray(beta_rad, dtype=float)
    if not np.all(np.isfinite(beta)):
        raise ValueError("beta_rad must contain only finite values")
    return (
        response["base"]
        + np.cos(4.0 * beta)[..., None, None] * response["cos4"]
        + np.sin(4.0 * beta)[..., None, None] * response["sin4"]
    )


def recover_beta_deg(
    cl_eb: ArrayLike,
    response: dict[str, Any],
    grid_deg: ArrayLike | None = None,
    weights: ArrayLike | None = None,
    selection: ArrayLike | None = None,
) -> NDArray[np.float64] | np.float64:
    """Fit beta from exact-window EB templates evaluated on a fixed grid."""
    grid = (
        np.linspace(-1.0, 1.0, 2001)
        if grid_deg is None
        else np.asarray(grid_deg, dtype=float)
    )
    if grid.ndim != 1 or grid.size == 0:
        raise ValueError("grid_deg must be a non-empty one-dimensional array")
    if not np.all(np.isfinite(grid)):
        raise ValueError("grid_deg must contain only finite values")
    templates = windowed_bandpowers(response, np.deg2rad(grid))[:, 1, :]
    measured = np.asarray(cl_eb, dtype=float)
    if measured.ndim not in (1, 2):
        raise ValueError("cl_eb must be one- or two-dimensional")
    if not np.all(np.isfinite(measured)):
        raise ValueError("cl_eb must contain only finite values")
    if measured.shape[-1] != templates.shape[-1]:
        raise ValueError(
            "cl_eb band count does not match the window response band count"
        )
    select = (
        np.ones(measured.shape[-1], dtype=bool)
        if selection is None
        else np.asarray(selection, dtype=bool)
    )
    if select.shape != (measured.shape[-1],) or not np.any(select):
        raise ValueError("selection must select at least one measured band")
    residual = measured[..., None, select] - templates[None, :, select]
    if measured.ndim == 1:
        residual = residual[0]
    if weights is None:
        selected_weights = np.ones(np.count_nonzero(select))
    else:
        all_weights = np.asarray(weights, dtype=float)
        if all_weights.shape != (measured.shape[-1],):
            raise ValueError("weights must match the measured band count")
        if not np.all(np.isfinite(all_weights)):
            raise ValueError("weights must contain only finite values")
        if np.any(all_weights < 0):
            raise ValueError("weights must be non-negative")
        selected_weights = all_weights[select]
        if not np.any(selected_weights > 0):
            raise ValueError("selected weights must contain a positive value")
    chi2 = np.sum(selected_weights * residual**2, axis=-1)
    return grid[np.argmin(chi2, axis=-1)]


def validate_window_equivalence(
    workspace: Any, response: dict[str, Any], beta_rad: float
) -> float:
    """Compare exact window contraction with couple-then-decouple."""
    beta = float(beta_rad)
    cls = (
        response["_base_cls"]
        + np.cos(4.0 * beta) * response["_cos4_cls"]
        + np.sin(4.0 * beta) * response["_sin4_cls"]
    )
    via_windows = windowed_bandpowers(response, beta)
    via_operator = workspace.decouple_cell(workspace.couple_cell(cls))
    return float(np.max(np.abs(via_windows - via_operator)))


def rotate_eb_spectra(cls: ArrayLike, beta_rad: float) -> NDArray[np.float64]:
    """Rotate a NaMaster ``[EE, EB, BE, BB]`` spectrum matrix algebraically."""
    values = np.asarray(cls, dtype=float)
    if values.ndim != 2 or values.shape[0] != 4:
        raise ValueError("expected NaMaster [EE, EB, BE, BB] spectrum order")
    if not np.all(np.isfinite(values)):
        raise ValueError("spectra must contain only finite values")
    beta = float(beta_rad)
    if not np.isfinite(beta):
        raise ValueError("beta_rad must be finite")
    cosine = np.cos(2.0 * beta)
    sine = np.sin(2.0 * beta)
    ee, eb, be, bb = values
    return np.array(
        [
            cosine**2 * ee - cosine * sine * (eb + be) + sine**2 * bb,
            cosine * sine * ee + cosine**2 * eb - sine**2 * be - cosine * sine * bb,
            cosine * sine * ee - sine**2 * eb + cosine**2 * be - cosine * sine * bb,
            sine**2 * ee + cosine * sine * (eb + be) + cosine**2 * bb,
        ]
    )
