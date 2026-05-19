#!/usr/bin/env python3
"""P5 env_finder Phase 1 MVP — V-Web cosmic-web classifier on DESI DR1.

Algorithm (Hahn+ 2007, Hoffman+ 2012, Cautun+ 2014):
  1. Filter DESI DR1 zall to ZWARN==0 GALAXY in z=[0.01, 2.0].
  2. Compute comoving distance chi(z) via Planck 2018 cosmology.
  3. Map to Cartesian (X, Y, Z) = chi * (cos(Dec)cos(RA), cos(Dec)sin(RA), sin(Dec)).
  4. CIC (Cloud-In-Cell) deposit onto a 256^3 comoving grid covering the
     galaxy bounding box (+ pad).
  5. Convert count field to overdensity delta = rho/rho_mean - 1.
  6. Gaussian-smooth delta in Fourier space with kernel R_s.
  7. Solve Poisson eq. (k-space): Phi(k) = -delta_k / k^2 (k=0 mode set to 0).
  8. Tidal tensor in k-space: T_ij(k) = k_i k_j Phi(k); inverse-FFT each of
     the 6 unique components (T_xx, T_yy, T_zz, T_xy, T_xz, T_yz).
  9. At each grid cell, diagonalize the 3x3 symmetric tidal-tensor matrix
     to get eigenvalues lambda_1 >= lambda_2 >= lambda_3.
 10. Classify: count of eigenvalues > lambda_th gives the V-Web class:
     0 -> void; 1 -> wall; 2 -> filament; 3 -> cluster.
 11. NN-interpolate the per-cell label + smoothed log-density back to each
     galaxy's position.
 12. Write parquet matching the schema contract enforced by
     pipelines/p5_desi_chirality/scripts/08_analysis_cosmic_web.py.

Output (parquet):
  TARGETID:       int64
  env_class:      category {"void", "wall", "filament", "cluster"}
  env_density:    float64  (log10(1 + delta_smoothed) at galaxy position)
  vac_provenance: str       (env_finder-vweb-v0.1-{git_sha}-{config_hash})
  env_lambda1:    float64
  env_lambda2:    float64
  env_lambda3:    float64

Phase 1 MVP. Cost: ~10-15 min wall on a 32 GB laptop.
"""
from __future__ import annotations

import hashlib
import json
import sys
import time
import os
import subprocess
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import yaml
from astropy.cosmology import Planck18
from scipy.fft import fftfreq, ifftn, rfftn, irfftn

REPO_ROOT = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
CONFIG_PATH = REPO_ROOT / "pipelines/p5_desi_chirality/env_finder/config.yaml"
ENV_CLASSES = ["void", "wall", "filament", "cluster"]


def utc_now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def git_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short=12", "HEAD"],
            cwd=str(REPO_ROOT),
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
    except Exception:
        return "unknown"


def config_hash(cfg: dict[str, Any]) -> str:
    blob = json.dumps(cfg, sort_keys=True).encode()
    return hashlib.sha256(blob).hexdigest()[:16]


def step(t0: float, msg: str) -> None:
    print(f"[{time.time() - t0:7.1f}s] {msg}", flush=True)


def load_zall(cfg: dict[str, Any], t0: float) -> pd.DataFrame:
    p = REPO_ROOT / cfg["input"]["zall_path"]
    step(t0, f"Loading {p.name} ...")
    cols = ["TARGETID", "TARGET_RA", "TARGET_DEC", "Z", "ZWARN", "SPECTYPE"]
    df = pq.read_table(str(p), columns=cols).to_pandas()
    step(t0, f"  raw rows: {len(df):,}")
    fcfg = cfg["input"]["filter"]
    mask = (
        (df["ZWARN"] == fcfg["zwarn_max"])
        & (df["SPECTYPE"].astype(str).str.strip() == fcfg["spectype"])
        & (df["Z"] > fcfg["z_min"])
        & (df["Z"] < fcfg["z_max"])
    )
    df = df.loc[mask, ["TARGETID", "TARGET_RA", "TARGET_DEC", "Z"]].reset_index(drop=True)
    step(t0, f"  filtered rows: {len(df):,}")
    return df


def comoving_xyz_mpc_h(z: np.ndarray, ra_deg: np.ndarray, dec_deg: np.ndarray, t0: float) -> np.ndarray:
    """Comoving Cartesian positions in Mpc/h (h=H0/100)."""
    step(t0, "Computing comoving distances (Planck18) ...")
    # astropy returns chi in Mpc with H0=67.66 -> h ~ 0.6766
    chi_mpc = Planck18.comoving_distance(z).value.astype(np.float32)
    h = Planck18.H0.value / 100.0
    chi = chi_mpc * h  # convert to Mpc/h
    ra = np.deg2rad(ra_deg).astype(np.float32)
    dec = np.deg2rad(dec_deg).astype(np.float32)
    cd = np.cos(dec)
    pos = np.empty((len(z), 3), dtype=np.float32)
    pos[:, 0] = chi * cd * np.cos(ra)
    pos[:, 1] = chi * cd * np.sin(ra)
    pos[:, 2] = chi * np.sin(dec)
    return pos


def cic_deposit(pos: np.ndarray, origin: np.ndarray, cell_size: float, N: int, t0: float) -> np.ndarray:
    """Cloud-In-Cell deposit of unit-weight particles onto an N^3 grid.

    Returns count field (float32) of shape (N, N, N).
    """
    step(t0, f"CIC deposit onto {N}^3 grid (cell = {cell_size:.3f} Mpc/h) ...")
    # Position in grid units (continuous index 0..N).
    u = (pos - origin) / cell_size
    # In-bounds (should be by construction since origin was set from min - pad).
    in_bounds = np.all((u >= 0.0) & (u < N - 1), axis=1)
    n_in = int(in_bounds.sum())
    n_out = len(pos) - n_in
    if n_out > 0:
        step(t0, f"  WARNING: {n_out:,} of {len(pos):,} galaxies fall outside grid (clamping)")
    u = u[in_bounds]

    grid = np.zeros((N, N, N), dtype=np.float32)
    i0 = np.floor(u).astype(np.int64)
    f = (u - i0).astype(np.float32)
    i1 = i0 + 1

    # 8 corners of the cell.
    for dx, fx_idx in [(0, "0"), (1, "1")]:
        for dy, fy_idx in [(0, "0"), (1, "1")]:
            for dz, fz_idx in [(0, "0"), (1, "1")]:
                wx = (1 - f[:, 0]) if dx == 0 else f[:, 0]
                wy = (1 - f[:, 1]) if dy == 0 else f[:, 1]
                wz = (1 - f[:, 2]) if dz == 0 else f[:, 2]
                w = (wx * wy * wz).astype(np.float32)
                ix = i0[:, 0] if dx == 0 else i1[:, 0]
                iy = i0[:, 1] if dy == 0 else i1[:, 1]
                iz = i0[:, 2] if dz == 0 else i1[:, 2]
                np.add.at(grid, (ix, iy, iz), w)
    step(t0, f"  CIC done; sum(grid) = {grid.sum():,.0f} (expected ~{n_in:,})")
    return grid


def gaussian_smooth_fft(field: np.ndarray, cell_size: float, R_s: float, t0: float) -> np.ndarray:
    """Gaussian smoothing of a 3D field in Fourier space with kernel R_s (Mpc/h)."""
    step(t0, f"Gaussian smoothing in k-space (R_s = {R_s:.2f} Mpc/h) ...")
    N = field.shape[0]
    # Use rfftn for memory efficiency (assumes real input).
    fhat = rfftn(field)
    kx = 2 * np.pi * fftfreq(N, d=cell_size).astype(np.float32)
    ky = kx
    kz = 2 * np.pi * np.fft.rfftfreq(N, d=cell_size).astype(np.float32)
    KX, KY, KZ = np.meshgrid(kx, ky, kz, indexing="ij")
    k2 = KX * KX + KY * KY + KZ * KZ
    smooth = np.exp(-0.5 * k2 * (R_s ** 2)).astype(np.float32)
    fhat *= smooth
    out = irfftn(fhat, s=field.shape).astype(np.float32)
    return out, KX, KY, KZ, k2


def tidal_eigenvalues(delta_smooth: np.ndarray, KX: np.ndarray, KY: np.ndarray, KZ: np.ndarray, k2: np.ndarray, t0: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Compute the three sorted eigenvalues of the tidal tensor T_ij = d^2 Phi / dx_i dx_j.

    Poisson: nabla^2 Phi = delta  =>  Phi(k) = -delta_k / k^2.
    Tidal:   T_ij(k) = -k_i k_j / k^2 * delta_k.
    """
    step(t0, "Computing tidal tensor T_ij = d^2 Phi / dx_i dx_j (k-space) ...")
    N = delta_smooth.shape[0]
    delta_k = rfftn(delta_smooth)
    # Avoid divide-by-zero at k=0: set Phi(k=0) := 0, equivalent to choosing
    # the gauge in which <Phi> = 0.
    inv_k2 = np.where(k2 > 0, 1.0 / k2, 0.0).astype(np.float32)
    phi_k = -delta_k * inv_k2  # shape (N, N, N//2+1) complex64

    components = {}
    pairs = [("xx", KX, KX), ("yy", KY, KY), ("zz", KZ, KZ),
             ("xy", KX, KY), ("xz", KX, KZ), ("yz", KY, KZ)]
    for name, A, B in pairs:
        # T_ij(k) = k_i k_j phi(k); inverse-FFT to real space.
        comp_k = -A * B * phi_k  # T_ij = -k_i k_j * (-delta_k/k^2) = k_i k_j delta_k/k^2; with phi=-delta/k^2, T_ij = -k_i k_j phi_k... wait.
        # Re-derive: Phi(k) = -delta_k / k^2.  d^2 Phi / dx_i dx_j  <->  (ik_i)(ik_j) Phi(k) = -k_i k_j Phi(k).
        # So T_ij(k) = -k_i k_j * (-delta_k / k^2) = k_i k_j delta_k / k^2 = -k_i k_j Phi(k).
        # Comp_k = -k_i k_j phi_k is correct.
        comp = irfftn(comp_k, s=delta_smooth.shape).astype(np.float32)
        components[name] = comp
        step(t0, f"  T_{name} done")

    # Build 3x3 symmetric matrix at each grid cell and diagonalize.
    step(t0, "Diagonalizing 3x3 tidal tensor at each grid cell ...")
    T = np.empty((N, N, N, 3, 3), dtype=np.float32)
    T[..., 0, 0] = components["xx"]
    T[..., 1, 1] = components["yy"]
    T[..., 2, 2] = components["zz"]
    T[..., 0, 1] = T[..., 1, 0] = components["xy"]
    T[..., 0, 2] = T[..., 2, 0] = components["xz"]
    T[..., 1, 2] = T[..., 2, 1] = components["yz"]
    del components
    # Vectorized eigvalsh: numpy treats leading axes as batch.
    eigs = np.linalg.eigvalsh(T)  # shape (N, N, N, 3); ascending order
    del T
    # Reverse to descending: lambda1 >= lambda2 >= lambda3.
    lambda1 = eigs[..., 2].astype(np.float32)
    lambda2 = eigs[..., 1].astype(np.float32)
    lambda3 = eigs[..., 0].astype(np.float32)
    del eigs
    return lambda1, lambda2, lambda3


def classify_vweb(lambda1: np.ndarray, lambda2: np.ndarray, lambda3: np.ndarray, lambda_th: float) -> np.ndarray:
    """Count eigenvalues > lambda_th at each cell to give env_class index (0-3)."""
    cnt = ((lambda1 > lambda_th).astype(np.uint8)
           + (lambda2 > lambda_th).astype(np.uint8)
           + (lambda3 > lambda_th).astype(np.uint8))
    return cnt  # 0 void, 1 wall, 2 filament, 3 cluster


def interpolate_to_galaxies(pos: np.ndarray, origin: np.ndarray, cell_size: float, N: int, cell_class: np.ndarray, cell_log1pd: np.ndarray, cell_eigs: tuple[np.ndarray, np.ndarray, np.ndarray]) -> dict:
    """Nearest-neighbor cell lookup for each galaxy."""
    u = (pos - origin) / cell_size
    idx = np.clip(np.floor(u + 0.5).astype(np.int64), 0, N - 1)
    ix, iy, iz = idx[:, 0], idx[:, 1], idx[:, 2]
    return {
        "env_class_idx": cell_class[ix, iy, iz],
        "env_density": cell_log1pd[ix, iy, iz],
        "env_lambda1": cell_eigs[0][ix, iy, iz],
        "env_lambda2": cell_eigs[1][ix, iy, iz],
        "env_lambda3": cell_eigs[2][ix, iy, iz],
    }


def main() -> int:
    t0 = time.time()
    cfg = yaml.safe_load(open(CONFIG_PATH))
    cfg_hash = config_hash(cfg)
    sha = git_sha()
    provenance_tag = f"env_finder-vweb-v0.1-{sha}-{cfg_hash}"
    step(t0, f"Config v{cfg['config_version']} hash={cfg_hash} git={sha}")

    # 1. Load + filter zall.
    df = load_zall(cfg, t0)

    # 2-3. Comoving Cartesian positions.
    pos = comoving_xyz_mpc_h(df["Z"].values, df["TARGET_RA"].values, df["TARGET_DEC"].values, t0)

    # 4. Bounding box.
    pad = float(cfg["grid"]["bounding_box_pad_mpc_h"])
    mins = pos.min(axis=0) - pad
    maxs = pos.max(axis=0) + pad
    # Pick a single cubic box that fits the bounding box (square cell).
    box_side = float(np.max(maxs - mins))
    origin = mins.astype(np.float32)
    N = int(cfg["grid"]["n"])
    cell_size = box_side / N
    step(t0, f"Bounding box side: {box_side:.1f} Mpc/h; grid {N}^3; cell {cell_size:.2f} Mpc/h")

    # 5. CIC deposit.
    count = cic_deposit(pos, origin, cell_size, N, t0)
    # 6. Survey-footprint mask + overdensity field.
    # The DESI footprint is a thin spherical shell on the sky, so most cells
    # in the Cartesian bounding cube lie OUTSIDE the survey volume and have
    # count == 0 not because the volume is empty but because we don't observe it.
    # Naive delta = count/rho_mean - 1 sets those cells to -1, which biases
    # smoothing near the survey edge toward "void" mis-classification.
    # Fix: build a survey-footprint mask via a buffered dilation of cells
    # with galaxies, compute rho_mean over the masked region, and treat
    # outside-mask cells as mean-density (delta = 0) for the FFT step.
    from scipy.ndimage import binary_dilation
    step(t0, "Building survey-footprint mask (dilated filled-cell region) ...")
    occupied = count > 0
    n_occupied = int(occupied.sum())
    # Dilate by ~R_s cells (R_s in Mpc/h / cell_size in Mpc/h, ceil).
    R_s_cfg = float(cfg["smoothing"]["R_s_mpc_h"])
    dilate_radius_cells = int(np.ceil(R_s_cfg / cell_size)) + 1
    mask = binary_dilation(occupied, iterations=dilate_radius_cells)
    n_mask = int(mask.sum())
    step(t0, f"  {n_occupied:,} occupied cells; dilated mask = {n_mask:,} cells ({100*n_mask/mask.size:.1f}% of {mask.size:,})")

    rho_mean_mask = float(count[mask].mean())
    step(t0, f"  rho_mean (galaxies/cell, masked region) = {rho_mean_mask:.3f}")
    delta = np.zeros_like(count, dtype=np.float32)
    delta[mask] = (count[mask] / rho_mean_mask - 1.0).astype(np.float32)
    del count

    # 7. Gaussian smooth delta.
    R_s = R_s_cfg
    delta_smooth, KX, KY, KZ, k2 = gaussian_smooth_fft(delta, cell_size, R_s, t0)
    del delta

    # 8-9. Tidal eigenvalues.
    lambda1, lambda2, lambda3 = tidal_eigenvalues(delta_smooth, KX, KY, KZ, k2, t0)
    del KX, KY, KZ, k2

    # log10(1+delta) for env_density column.
    log1pd_cell = np.log10(np.maximum(1.0 + delta_smooth, 1e-6)).astype(np.float32)
    del delta_smooth

    # 10. Classify.
    lambda_th = float(cfg["classify"]["lambda_th"])
    step(t0, f"Classifying with lambda_th = {lambda_th} ...")
    cell_class = classify_vweb(lambda1, lambda2, lambda3, lambda_th)

    # Volume fractions sanity check — report INSIDE-MASK fractions (the
    # survey volume) rather than the full cube (which includes empty
    # outside-footprint cells).
    total_mask = int(mask.sum())
    fracs = {ENV_CLASSES[i]: float(((cell_class == i) & mask).sum()) / max(total_mask, 1) for i in range(4)}
    fracs_fullcube = {ENV_CLASSES[i]: float((cell_class == i).sum()) / cell_class.size for i in range(4)}
    step(t0, f"  Volume fractions (in-footprint): void={fracs['void']:.3f} wall={fracs['wall']:.3f} filament={fracs['filament']:.3f} cluster={fracs['cluster']:.3f}")
    step(t0, f"  Volume fractions (full cube):    void={fracs_fullcube['void']:.3f} wall={fracs_fullcube['wall']:.3f} filament={fracs_fullcube['filament']:.3f} cluster={fracs_fullcube['cluster']:.3f}")

    # 11. Interpolate to galaxies.
    step(t0, "Interpolating env_class + density to galaxy positions ...")
    interp = interpolate_to_galaxies(pos, origin, cell_size, N, cell_class, log1pd_cell, (lambda1, lambda2, lambda3))

    # 12. Write parquet matching schema contract.
    env_class_str = pd.Categorical.from_codes(interp["env_class_idx"], categories=ENV_CLASSES)
    out_df = pd.DataFrame({
        "TARGETID": df["TARGETID"].values,
        "env_class": env_class_str,
        "env_density": interp["env_density"].astype(np.float64),
        "vac_provenance": np.full(len(df), provenance_tag, dtype=object),
    })
    if cfg["output"]["include_eigenvalues"]:
        out_df["env_lambda1"] = interp["env_lambda1"].astype(np.float64)
        out_df["env_lambda2"] = interp["env_lambda2"].astype(np.float64)
        out_df["env_lambda3"] = interp["env_lambda3"].astype(np.float64)

    out_path = REPO_ROOT / cfg["output"]["env_parquet"]
    out_path.parent.mkdir(parents=True, exist_ok=True)
    step(t0, f"Writing parquet to {out_path} ...")
    out_df.to_parquet(out_path, index=False)
    step(t0, f"  wrote {len(out_df):,} rows; {out_path.stat().st_size:,} bytes")

    # Provenance sidecar.
    prov = {
        "output": str(out_path.name),
        "written_utc": utc_now(),
        "git_sha": sha,
        "config_version": cfg["config_version"],
        "config_hash": cfg_hash,
        "provenance_tag": provenance_tag,
        "n_galaxies": int(len(df)),
        "grid_n": N,
        "cell_size_mpc_h": cell_size,
        "box_side_mpc_h": box_side,
        "smoothing_R_s_mpc_h": R_s,
        "lambda_th": lambda_th,
        "volume_fractions": fracs,
    }
    (out_path.parent / f"{out_path.stem}.provenance.json").write_text(json.dumps(prov, indent=2))

    # Volume-fractions report.
    rpt_path = REPO_ROOT / cfg["output"]["volume_fractions_json"]
    rpt_path.parent.mkdir(parents=True, exist_ok=True)
    rpt = {
        "written_utc": utc_now(),
        "provenance_tag": provenance_tag,
        "grid_n": N,
        "cell_size_mpc_h": cell_size,
        "smoothing_R_s_mpc_h": R_s,
        "lambda_th": lambda_th,
        "survey_mask_fill_fraction": float(total_mask) / cell_class.size,
        "n_occupied_cells": n_occupied,
        "n_mask_cells": total_mask,
        "rho_mean_galaxies_per_cell_in_mask": rho_mean_mask,
        "volume_fractions_in_footprint": fracs,
        "volume_fractions_full_cube": fracs_fullcube,
        "literature_baseline_at_lambda_th_0": {
            "void": 0.70, "wall": 0.15, "filament": 0.12, "cluster": 0.03,
            "_note": "Approximate; Cautun+ 2014 N-body baseline. Compare to volume_fractions_in_footprint.",
        },
        "galaxy_class_fractions": {
            ENV_CLASSES[i]: float((interp["env_class_idx"] == i).sum()) / len(df) for i in range(4)
        },
    }
    rpt_path.write_text(json.dumps(rpt, indent=2))
    step(t0, f"Wrote volume-fractions report to {rpt_path}")

    step(t0, "DONE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
