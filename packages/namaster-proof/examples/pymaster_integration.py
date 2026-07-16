#!/usr/bin/env python3
"""Independent real-PyMaster integration and shortcut comparison."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import healpy as hp
import numpy as np
import pymaster as nmt

from namaster_proof import (
    build_rotation_response,
    publish_json,
    recover_beta_deg,
    validate_window_equivalence,
    windowed_bandpowers,
)


def run(output: Path, injected_beta_deg: float = 0.25) -> dict:
    nside = 16
    lmax = 32
    npix = hp.nside2npix(nside)
    theta, _ = hp.pix2ang(nside, np.arange(npix))
    latitude_deg = 90.0 - np.rad2deg(theta)
    mask = (np.abs(latitude_deg) >= 25.0).astype(float)

    zeros = np.zeros(npix)
    field = nmt.NmtField(mask, [zeros, zeros], lmax=lmax)
    edges = np.array([2, 6, 11, 17, 24, lmax + 1])
    bins = nmt.NmtBin.from_edges(edges[:-1], edges[1:])
    workspace = nmt.NmtWorkspace()
    workspace.compute_coupling_matrix(field, field, bins)

    ell = np.arange(lmax + 1, dtype=float)
    cl_ee = np.zeros_like(ell)
    cl_bb = np.zeros_like(ell)
    cl_ee[2:] = 2.0e-4 / (ell[2:] * (ell[2:] + 1.0))
    cl_bb[2:] = 0.04 * cl_ee[2:]

    response = build_rotation_response(workspace, cl_ee, cl_bb)
    beta_rad = np.deg2rad(injected_beta_deg)
    measured_eb = windowed_bandpowers(response, beta_rad)[1]
    grid = np.linspace(-1.0, 1.0, 2001)
    exact_recovered = float(
        recover_beta_deg(measured_eb, response, grid_deg=grid)
    )
    equivalence = validate_window_equivalence(workspace, response, beta_rad)

    ell_eff = bins.get_effective_ells()
    diff_at_eff = np.interp(ell_eff, ell, cl_ee - cl_bb)
    shortcut_templates = (
        0.5
        * np.sin(4.0 * np.deg2rad(grid))[:, None]
        * diff_at_eff[None, :]
    )
    shortcut_recovered = float(
        grid[np.argmin(np.sum((measured_eb[None, :] - shortcut_templates) ** 2, axis=1))]
    )

    payload = {
        "suite": "namaster-proof-pymaster-integration-v1",
        "pymaster_version": nmt.__version__,
        "nside": nside,
        "lmax": lmax,
        "window_shape": list(response["window_shape"]),
        "injected_beta_deg": injected_beta_deg,
        "exact_recovered_beta_deg": exact_recovered,
        "effective_ell_shortcut_recovered_beta_deg": shortcut_recovered,
        "exact_operator_equivalence_max_abs": equivalence,
    }
    publish_json(
        output,
        payload,
        {
            "suite": payload["suite"],
            "pymaster_version": nmt.__version__,
            "deterministic": True,
        },
    )
    if exact_recovered != injected_beta_deg:
        raise RuntimeError("exact-window integration did not recover the grid injection")
    if not np.isfinite(equivalence) or equivalence > 1e-10:
        raise RuntimeError("window contraction failed the real-PyMaster equivalence gate")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("pymaster_integration_result.json"),
    )
    parser.add_argument("--beta-deg", type=float, default=0.25)
    args = parser.parse_args()
    print(json.dumps(run(args.output, args.beta_deg), sort_keys=True))


if __name__ == "__main__":
    main()
