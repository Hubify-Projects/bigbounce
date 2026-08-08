#!/usr/bin/env python3
"""Run an exact-window recovery without PyMaster or BigBounce data."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from namaster_proof import (
    build_rotation_response,
    publish_json,
    recover_beta_deg,
    validate_json_receipt,
    validate_window_equivalence,
    windowed_bandpowers,
)


class SyntheticWorkspace:
    """Deterministic linear workspace with nontrivial band mixing."""

    def __init__(self, n_ell: int = 12, n_band: int = 4) -> None:
        windows = np.zeros((4, n_band, 4, n_ell), dtype=float)
        edges = np.linspace(0, n_ell, n_band + 1, dtype=int)
        for spectrum in range(4):
            for band, (start, stop) in enumerate(zip(edges[:-1], edges[1:])):
                windows[spectrum, band, spectrum, start:stop] = 1.0 / (stop - start)
        self.windows = windows

    def get_bandpower_windows(self):
        return self.windows

    def couple_cell(self, cls):
        return np.asarray(cls)

    def decouple_cell(self, coupled):
        return np.einsum("ibjl,jl->ib", self.windows, coupled, optimize=True)


def run(output: Path, injected_beta_deg: float) -> dict:
    workspace = SyntheticWorkspace()
    ell = np.arange(12, dtype=float)
    cl_ee = 1.0 / (ell + 1.0)
    cl_bb = 0.05 / (ell + 1.0)
    response = build_rotation_response(workspace, cl_ee, cl_bb)
    equivalence_error = validate_window_equivalence(
        workspace, response, np.deg2rad(injected_beta_deg)
    )
    measured_eb = windowed_bandpowers(
        response, np.deg2rad(injected_beta_deg)
    )[1]
    grid = np.linspace(-1.0, 1.0, 2001)
    recovered_beta_deg = float(
        recover_beta_deg(measured_eb, response, grid_deg=grid)
    )
    payload = {
        "injected_beta_deg": injected_beta_deg,
        "recovered_beta_deg": recovered_beta_deg,
        "equivalence_error": equivalence_error,
        "window_shape": list(response["window_shape"]),
    }
    publish_json(
        output,
        payload,
        {
            "suite": "namaster-proof-synthetic-window-v1",
            "deterministic": True,
        },
    )
    validate_json_receipt(
        output,
        expected={
            "suite": "namaster-proof-synthetic-window-v1",
            "deterministic": True,
        },
    )
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("synthetic_result.json"))
    parser.add_argument("--beta-deg", type=float, default=0.25)
    args = parser.parse_args()
    result = run(args.output, args.beta_deg)
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
