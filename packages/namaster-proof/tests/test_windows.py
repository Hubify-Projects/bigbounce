from __future__ import annotations

import numpy as np
import pytest

from namaster_proof.windows import (
    build_rotation_response,
    recover_beta_deg,
    rotate_eb_spectra,
    validate_window_equivalence,
    windowed_bandpowers,
)


class IdentityWorkspace:
    """One-band linear operator with an exact window representation."""

    def __init__(self, n_ell: int = 6) -> None:
        self.windows = np.zeros((4, n_ell, 4, n_ell))
        for spectrum in range(4):
            self.windows[spectrum, :, spectrum, :] = np.eye(n_ell)

    def get_bandpower_windows(self):
        return self.windows

    def couple_cell(self, cls):
        return np.asarray(cls)

    def decouple_cell(self, coupled):
        return np.asarray(coupled)


def test_window_response_matches_linear_operator():
    workspace = IdentityWorkspace()
    ee = np.linspace(1.0, 2.0, 6)
    bb = np.linspace(0.1, 0.2, 6)
    response = build_rotation_response(workspace, ee, bb)
    assert response["window_shape"] == (4, 6, 4, 6)
    assert validate_window_equivalence(workspace, response, 0.27) < 1e-14


def test_recover_beta_on_exact_grid():
    workspace = IdentityWorkspace()
    response = build_rotation_response(
        workspace, np.linspace(1.0, 2.0, 6), np.linspace(0.1, 0.2, 6)
    )
    grid = np.array([-0.25, 0.0, 0.25])
    measured = windowed_bandpowers(response, np.deg2rad(0.25))[1]
    assert recover_beta_deg(measured, response, grid_deg=grid) == pytest.approx(0.25)


def test_rotate_eb_spectra_preserves_total_auto_power():
    cls = np.array(
        [
            [4.0, 3.0],
            [0.0, 0.0],
            [0.0, 0.0],
            [1.0, 0.5],
        ]
    )
    rotated = rotate_eb_spectra(cls, 0.3)
    np.testing.assert_allclose(rotated[0] + rotated[3], cls[0] + cls[3])
    np.testing.assert_allclose(rotated[1], rotated[2])


def test_invalid_window_and_spectrum_shapes_fail_closed():
    class BadWorkspace:
        def get_bandpower_windows(self):
            return np.zeros((2, 3, 4))

    with pytest.raises(ValueError, match="two-spin windows"):
        build_rotation_response(BadWorkspace(), [1.0], [0.0])
    with pytest.raises(ValueError, match=r"\[EE, EB, BE, BB\]"):
        rotate_eb_spectra(np.zeros((3, 4)), 0.0)
