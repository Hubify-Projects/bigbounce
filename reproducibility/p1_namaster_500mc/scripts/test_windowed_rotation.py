#!/usr/bin/env python3
"""Small deterministic regression tests for exact rotation/window operators."""

from __future__ import annotations

import numpy as np
import healpy as hp
import pymaster as nmt

from windowed_rotation import (
    build_rotation_response,
    rotate_eb_spectra,
    validate_window_equivalence,
)


def main() -> None:
    nside = 32
    npix = hp.nside2npix(nside)
    rng = np.random.default_rng(20260714)
    q = rng.normal(size=npix)
    u = rng.normal(size=npix)
    _, latitude = hp.pix2ang(nside, np.arange(npix), lonlat=True)
    mask = (np.abs(latitude) > 20.0).astype(float)

    field = nmt.NmtField(mask, [q, u])
    coupled = nmt.compute_coupled_cell(field, field)
    rotation_errors = []
    for beta_deg in (-0.342, 0.0, 0.27, 0.342):
        beta = np.deg2rad(beta_deg)
        c, s = np.cos(2 * beta), np.sin(2 * beta)
        direct = nmt.compute_coupled_cell(
            nmt.NmtField(mask, [c * q - s * u, s * q + c * u]),
            nmt.NmtField(mask, [c * q - s * u, s * q + c * u]),
        )
        rotation_errors.append(float(np.max(np.abs(direct - rotate_eb_spectra(coupled, beta)))))

    bins = nmt.NmtBin.from_nside_linear(nside, 8)
    workspace = nmt.NmtWorkspace()
    workspace.compute_coupling_matrix(field, field, bins)
    ell = np.arange(2 * nside + 1, dtype=float)
    cl_ee = np.exp(-0.5 * ((ell - 30.0) / 12.0) ** 2)
    cl_bb = 0.05 * cl_ee
    response = build_rotation_response(workspace, cl_ee, cl_bb)
    window_error = validate_window_equivalence(workspace, response, np.deg2rad(0.27))

    max_rotation_error = max(rotation_errors)
    print(f"max coupled-spectrum rotation error: {max_rotation_error:.6e}")
    print(f"max bandpower-window equivalence error: {window_error:.6e}")
    if max_rotation_error > 1e-12 or window_error > 1e-10:
        raise SystemExit("exact-operator regression failed")


if __name__ == "__main__":
    main()
