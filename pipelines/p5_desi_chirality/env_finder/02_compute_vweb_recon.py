#!/usr/bin/env python3
"""V-Web on reconstructed (Zel'dovich-displaced) positions at R_s = 8 Mpc/h.

Reads pyrecon output parquet (RECON_X/Y/Z columns), runs the same
V-Web tidal-tensor pipeline as 01_compute_vweb.py at finer resolution.

Output env catalog is then merged against the P5 matched-spiral catalog
to produce the §sec:recon_robustness panel for the P5 paper.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
import pyarrow.parquet as pq
import yaml
from scipy.fft import fftfreq, rfftn, irfftn

# Import shared utilities from sibling V-Web script.
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from _compute_vweb_lib import (  # noqa: E402
    cic_deposit, gaussian_smooth_fft, tidal_eigenvalues,
    classify_vweb, interpolate_to_galaxies, ENV_CLASSES,
)

REPO_ROOT = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
DEFAULT_CONFIG = SCRIPT_DIR / "recon_config.yaml"


def step(t0, msg):
    print(f"[{time.time()-t0:8.1f}s] {msg}", flush=True)


def git_sha():
    try:
        return subprocess.check_output(["git", "rev-parse", "--short=12", "HEAD"], cwd=str(REPO_ROOT), text=True).strip()
    except Exception:
        return "unknown"


def config_hash(cfg):
    return hashlib.sha256(json.dumps(cfg, sort_keys=True).encode()).hexdigest()[:16]


def main() -> int:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    parser.add_argument("--repo-root", default=str(REPO_ROOT))
    args = parser.parse_args()
    repo_root = Path(args.repo_root)
    t0 = time.time()
    cfg = yaml.safe_load(open(args.config))
    cfg_hash = config_hash(cfg)
    sha = git_sha()
    provenance_tag = f"env_finder-vweb-recon-v0.2-{sha}-{cfg_hash}"
    step(t0, f"Config v{cfg['config_version']} hash={cfg_hash} git={sha}")
    step(t0, f"  R_s = {cfg['smoothing']['R_s_mpc_h']} Mpc/h, grid N = {cfg['grid']['n']}")

    # 1. Load reconstructed positions parquet.
    recon_path = repo_root / cfg["input"]["recon_parquet"]
    step(t0, f"Loading {recon_path} ...")
    df = pq.read_table(str(recon_path), columns=["TARGETID", "TRACER", "RECON_X", "RECON_Y", "RECON_Z"]).to_pandas()
    step(t0, f"  rows: {len(df):,}")
    step(t0, f"  per-tracer: {df['TRACER'].value_counts().to_dict()}")
    pos = df[["RECON_X", "RECON_Y", "RECON_Z"]].to_numpy(dtype=np.float32)

    # 2. Bounding box.
    pad = float(cfg["grid"]["bounding_box_pad_mpc_h"])
    mins = pos.min(axis=0) - pad
    maxs = pos.max(axis=0) + pad
    box_side = float((maxs - mins).max())
    origin = mins.astype(np.float32)
    N = int(cfg["grid"]["n"])
    cell_size = box_side / N
    step(t0, f"Bounding box {box_side:.1f} Mpc/h; grid {N}^3; cell {cell_size:.2f} Mpc/h")
    step(t0, f"  R_s / cell = {cfg['smoothing']['R_s_mpc_h'] / cell_size:.2f} (should be >= ~1 for well-resolved smoothing)")

    # 3. CIC deposit.
    count = cic_deposit(pos, origin, cell_size, N, t0)

    # 4. Survey-footprint mask + overdensity.
    from scipy.ndimage import binary_dilation
    step(t0, "Building dilated footprint mask ...")
    occupied = count > 0
    R_s_cfg = float(cfg["smoothing"]["R_s_mpc_h"])
    dilate_radius_cells = int(np.ceil(R_s_cfg / cell_size)) + 1
    mask = binary_dilation(occupied, iterations=dilate_radius_cells)
    n_mask = int(mask.sum())
    step(t0, f"  occupied {int(occupied.sum()):,}, dilated mask {n_mask:,} cells ({100*n_mask/mask.size:.1f}% of cube)")
    rho_mean = float(count[mask].mean())
    step(t0, f"  rho_mean (masked) = {rho_mean:.3f}")
    delta = np.zeros_like(count, dtype=np.float32)
    delta[mask] = (count[mask] / rho_mean - 1.0).astype(np.float32)
    del count

    # 5. Smooth.
    R_s = R_s_cfg
    delta_smooth, KX, KY, KZ, k2 = gaussian_smooth_fft(delta, cell_size, R_s, t0)
    del delta

    # 6. Tidal eigenvalues.
    lambda1, lambda2, lambda3 = tidal_eigenvalues(delta_smooth, KX, KY, KZ, k2, t0)
    del KX, KY, KZ, k2

    log1pd_cell = np.log10(np.maximum(1.0 + delta_smooth, 1e-6)).astype(np.float32)
    del delta_smooth

    # 7. Classify.
    lambda_th = float(cfg["classify"]["lambda_th"])
    cell_class = classify_vweb(lambda1, lambda2, lambda3, lambda_th)
    total_mask = int(mask.sum())
    fracs = {ENV_CLASSES[i]: float(((cell_class == i) & mask).sum()) / max(total_mask, 1) for i in range(4)}
    step(t0, f"  Volume fractions (in-footprint): {fracs}")

    # 8. Interpolate.
    interp = interpolate_to_galaxies(pos, origin, cell_size, N, cell_class, log1pd_cell, (lambda1, lambda2, lambda3))
    env_class_str = pd.Categorical.from_codes(interp["env_class_idx"], categories=ENV_CLASSES)

    out_df = pd.DataFrame({
        "TARGETID": df["TARGETID"].values,
        "env_class": env_class_str,
        "env_density": interp["env_density"].astype(np.float64),
        "vac_provenance": np.full(len(df), provenance_tag, dtype=object),
        "env_lambda1": interp["env_lambda1"].astype(np.float64),
        "env_lambda2": interp["env_lambda2"].astype(np.float64),
        "env_lambda3": interp["env_lambda3"].astype(np.float64),
    })
    out_path = repo_root / cfg["output"]["env_parquet"]
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_df.to_parquet(out_path, index=False)
    step(t0, f"Wrote {out_path} ({len(out_df):,} rows)")

    # Volume fractions JSON.
    vol_path = repo_root / cfg["output"]["volume_fractions_json"]
    vol_path.parent.mkdir(parents=True, exist_ok=True)
    with vol_path.open("w") as fh:
        json.dump({
            "written_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "provenance_tag": provenance_tag,
            "grid_n": N,
            "cell_size_mpc_h": cell_size,
            "smoothing_R_s_mpc_h": R_s,
            "lambda_th": lambda_th,
            "input": str(recon_path),
            "n_galaxies": int(len(df)),
            "volume_fractions_in_footprint": fracs,
            "wall_seconds": time.time() - t0,
        }, fh, indent=2)
    step(t0, f"Wrote {vol_path}")
    step(t0, "DONE.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
