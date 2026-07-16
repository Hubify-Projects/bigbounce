#!/usr/bin/env python3
"""Exact-window rerun of the declared f_sky sweep and negative-beta check.

Historical ``c1_fsky_sweep.json`` and ``c9f_negative_beta.json`` used an
effective-ell theory template.  This battery preserves their exact simulation
design (pure Galactic-cut masks at f_sky 0.85/0.65/0.32, 2-degree smoothing,
500 identical-seed realizations) while fitting the full NaMaster bandpower
window operator.
"""

from __future__ import annotations

import argparse
import json
import os
import time
from multiprocessing import Pool
from pathlib import Path

import healpy as hp
import numpy as np
import pymaster as nmt

from windowed_rotation import (
    build_rotation_response,
    recover_beta_deg,
    validate_window_equivalence,
    windowed_bandpowers,
)
from checkpoint_io import publish_json, validate_json_receipt
from physical_spectra import load_camb_lensed_spectra
from multipole_contract import bandpower_edges


NSIDE = 512
LMAX = 2 * NSIDE
N_REAL = int(os.environ.get("DECLARED_NREAL", "500"))
SEED_BASE = 42
NOISE_LEVEL_UKARMIN = 10.0
OUTPUT = (
    Path(__file__).resolve().parent.parent
    / "results"
    / "physical_spectrum_v2"
    / "declared_fsky_sign_battery.json"
)

CONFIGS = [
    {"name": "fsky_0p85", "fsky_target": 0.85, "gal_cut_deg": 8.62692655867864, "beta_deg": 0.27},
    {"name": "fsky_0p65", "fsky_target": 0.65, "gal_cut_deg": 20.487315114722662, "beta_deg": 0.27},
    {"name": "negative_beta_fsky_0p32", "fsky_target": 0.32, "gal_cut_deg": 42.84364304359634, "beta_deg": -0.27},
]


def run_config(config: dict) -> dict:
    started = time.time()
    beta_deg = float(config["beta_deg"])
    beta = np.deg2rad(beta_deg)
    npix = hp.nside2npix(NSIDE)
    _, latitude = hp.pix2ang(NSIDE, np.arange(npix), lonlat=True)
    mask = (np.abs(latitude) >= config["gal_cut_deg"]).astype(float)
    mask = np.clip(hp.smoothing(mask, fwhm=np.deg2rad(2.0)), 0, 1)
    fsky = float(np.mean(mask))

    cl_ee, cl_bb, spectrum_metadata = load_camb_lensed_spectra(LMAX)
    edges = bandpower_edges(nside=NSIDE, lmax=LMAX, n_bins=20)
    bins = nmt.NmtBin.from_edges(edges[:-1], edges[1:])
    zero = np.zeros(npix)
    dummy = nmt.NmtField(mask, [zero, zero], lmax=LMAX)
    workspace = nmt.NmtWorkspace()
    workspace.compute_coupling_matrix(dummy, dummy, bins)
    response = build_rotation_response(workspace, cl_ee, cl_bb)
    equivalence = validate_window_equivalence(workspace, response, beta)
    if not np.isfinite(equivalence) or equivalence > 1e-10:
        raise RuntimeError(f"window equivalence failed: {equivalence:.6e}")

    pixel_area_arcmin2 = hp.nside2pixarea(NSIDE, degrees=True) * 3600
    noise_sigma = NOISE_LEVEL_UKARMIN / np.sqrt(pixel_area_arcmin2)
    c, s = np.cos(2 * beta), np.sin(2 * beta)
    ensemble = []
    for index in range(N_REAL):
        np.random.seed(SEED_BASE + index)
        maps = hp.synfast(
            [np.zeros(LMAX + 1), cl_ee, cl_bb, np.zeros(LMAX + 1)],
            NSIDE,
            lmax=LMAX,
            new=True,
        )
        q, u = maps[1], maps[2]
        q += np.random.normal(0, noise_sigma, npix)
        u += np.random.normal(0, noise_sigma, npix)
        field = nmt.NmtField(
            mask, [c * q - s * u, s * q + c * u], lmax=LMAX
        )
        ensemble.append(
            workspace.decouple_cell(nmt.compute_coupled_cell(field, field))[1]
        )

    ensemble = np.asarray(ensemble)
    mean_eb = np.mean(ensemble, axis=0)
    std_eb = np.std(ensemble, axis=0)
    recovered = float(recover_beta_deg(mean_eb, response))
    per_real = recover_beta_deg(ensemble, response)
    beta_std = float(np.std(per_real, ddof=1))
    theory = windowed_bandpowers(response, beta)[1]
    theory_null = windowed_bandpowers(response, 0.0)[1]
    snr = float(np.sqrt(np.sum(((theory - theory_null) / (std_eb + 1e-20)) ** 2)))
    result = {
        **config,
        "fsky_actual_apodized": fsky,
        "nside": NSIDE,
        "lmax": LMAX,
        "n_real": N_REAL,
        "seed_base": SEED_BASE,
        "physical_spectra": spectrum_metadata,
        "recovered_beta_deg": recovered,
        "signed_bias_deg": recovered - beta_deg,
        "per_realization_beta_std_deg": beta_std,
        "mc_mean_standard_error_deg": beta_std / np.sqrt(N_REAL),
        "snr_exact_window": snr,
        "window_shape": list(response["window_shape"]),
        "window_equivalence_max_abs": equivalence,
        "runtime_s": time.time() - started,
    }
    print(f"[{config['name']}] {recovered:+.4f} deg in {result['runtime_s']:.1f}s", flush=True)
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--only-config", choices=[item["name"] for item in CONFIGS])
    parser.add_argument("--output", type=Path)
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    started = time.time()
    selected = CONFIGS
    if args.only_config:
        selected = [item for item in CONFIGS if item["name"] == args.only_config]
    requested = os.environ.get("DECLARED_CONFIGS", "").strip()
    if requested and not args.only_config:
        names = {name.strip() for name in requested.split(",") if name.strip()}
        selected = [item for item in CONFIGS if item["name"] in names]
        missing = names - {item["name"] for item in selected}
        if missing:
            raise ValueError(f"unknown DECLARED_CONFIGS names: {sorted(missing)}")
    if args.output is not None:
        output = args.output
    elif args.only_config:
        output = OUTPUT.parent / "shards" / f"declared_{args.only_config}.json"
    else:
        output = Path(os.environ.get("DECLARED_OUTPUT", str(OUTPUT)))
    config_names = [item["name"] for item in selected]
    if not args.force and output.exists():
        try:
            validate_json_receipt(
                output,
                expected_suite="declared_fsky_sign",
                expected_configs=config_names,
                expected_config_metadata=selected,
                expected_n_real=N_REAL,
                expected_seed_start=SEED_BASE,
                expected_seed_end=SEED_BASE + N_REAL - 1,
            )
        except (FileNotFoundError, ValueError, json.JSONDecodeError):
            pass
        else:
            print(f"validated existing shard; skipping: {output}")
            return
    pool_size = min(int(os.environ.get("DECLARED_POOL", "3")), len(CONFIGS))
    if len(selected) == 1:
        results = [run_config(selected[0])]
    else:
        with Pool(min(pool_size, len(selected))) as pool:
            results = pool.map(run_config, selected)
    payload = {
        "experiment": "declared NaMaster f_sky and sign checks with exact bandpower windows",
        "status_of_historical_outputs": "superseded effective-ell-template evidence preserved at top-level results",
        "software": {"numpy": np.__version__, "healpy": hp.__version__, "pymaster": nmt.__version__},
        "results": results,
        "total_runtime_s": time.time() - started,
    }
    receipt = publish_json(
        output,
        payload,
        {
            "suite": "declared_fsky_sign",
            "config_names": config_names,
            "configs": selected,
            "n_real": N_REAL,
            "seed_start": SEED_BASE,
            "seed_end": SEED_BASE + N_REAL - 1,
            "runtime_s": payload["total_runtime_s"],
            "theory_operator": "NmtWorkspace.get_bandpower_windows exact tensor contraction",
            "window_equivalence_max_abs": max(
                item["window_equivalence_max_abs"] for item in results
            ),
            "software": payload["software"],
        },
    )
    print(json.dumps(payload, indent=2))
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
