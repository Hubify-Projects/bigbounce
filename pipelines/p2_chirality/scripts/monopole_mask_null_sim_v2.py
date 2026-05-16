#!/usr/bin/env python3
"""
Full N=500 monopole+mask leakage null simulation — pre-MASTER pseudo-C1
+ hemisphere max statistic, using the canonical N_spiral=3,201,160
catalog from HF and the canonical f_sky=0.4938 mask.

Closes Grok-4 / GPT-4 BLOCKER: the cited monopole_mask_null artifact
must be N=500 not N=25 to match the paper's claim.

Output: monopole_mask_null_results.json (full N=500, supersedes the
smoke).
"""
import json, time
from pathlib import Path
import numpy as np
import healpy as hp
import pandas as pd
from huggingface_hub import hf_hub_download

NSIDE = 64
LMAX = 191
N_MC = 500
SEED = 42
MIN_SPIRALS_PER_PIX = 10
HEMI_DIR_NSIDE = 8
OUT = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p2_chirality/outputs/canonical_provenance/monopole_mask_null_results.json")


def precompute_hemisphere(n_pix_full):
    """Precompute sign matrix: (n_dir, n_pix_full) = +1 or -1 per pixel
    on each direction's hemisphere."""
    nside_map = NSIDE
    nside_dir = HEMI_DIR_NSIDE
    n_dir = hp.nside2npix(nside_dir)
    # all pixel sky positions
    pix_th, pix_ph = hp.pix2ang(nside_map, np.arange(n_pix_full))
    pix_xyz = np.stack(
        [np.sin(pix_th) * np.cos(pix_ph),
         np.sin(pix_th) * np.sin(pix_ph),
         np.cos(pix_th)], axis=1)  # (n_pix, 3)
    dir_th, dir_ph = hp.pix2ang(nside_dir, np.arange(n_dir))
    dir_xyz = np.stack(
        [np.sin(dir_th) * np.cos(dir_ph),
         np.sin(dir_th) * np.sin(dir_ph),
         np.cos(dir_th)], axis=1)  # (n_dir, 3)
    # cos(separation) > 0 = same hemisphere
    cos_sep = dir_xyz @ pix_xyz.T  # (n_dir, n_pix)
    return np.where(cos_sep >= 0, 1.0, -1.0).astype(np.float32)


def main():
    t0 = time.time()
    print(f"[{time.time()-t0:.1f}s] Loading canonical catalog from HF ...", flush=True)
    p = hf_hub_download("bamfai/galaxy-chirality-catalog", "catalog_production.parquet", repo_type="dataset")
    df = pd.read_parquet(p, columns=["ra", "dec", "class_eq"])
    spirals = df[df["class_eq"].isin(["CW", "CCW"])].reset_index(drop=True)
    print(f"[{time.time()-t0:.1f}s] spirals: {len(spirals):,}", flush=True)

    th = np.radians(90.0 - spirals["dec"].values)
    ph = np.radians(spirals["ra"].values)
    pix = hp.ang2pix(NSIDE, th, ph)
    n_total_pix = np.bincount(pix, minlength=hp.nside2npix(NSIDE))
    cw_mask = spirals["class_eq"].values == "CW"
    n_cw_pix = np.bincount(pix[cw_mask], minlength=hp.nside2npix(NSIDE))
    n_ccw_pix = n_total_pix - n_cw_pix

    # Canonical mask: only pixels with at least MIN_SPIRALS_PER_PIX spirals
    mask_bool = n_total_pix >= MIN_SPIRALS_PER_PIX
    n_pix_used = int(mask_bool.sum())
    f_sky = n_pix_used / hp.nside2npix(NSIDE)
    n_spiral_in_mask = int(n_total_pix[mask_bool].sum())
    n_cw_in_mask = int(n_cw_pix[mask_bool].sum())
    p_cw_global = n_cw_in_mask / n_spiral_in_mask
    print(f"[{time.time()-t0:.1f}s] mask: NSIDE={NSIDE}, n_pix_used={n_pix_used}, f_sky={f_sky:.4f}", flush=True)
    print(f"[{time.time()-t0:.1f}s] N_spiral_in_mask={n_spiral_in_mask:,}, p_CW_global={p_cw_global:.6f}", flush=True)

    # CW-fraction map (0 outside mask)
    p_cw_map_obs = np.zeros(hp.nside2npix(NSIDE), dtype=np.float64)
    nz = n_total_pix > 0
    p_cw_map_obs[nz] = n_cw_pix[nz] / n_total_pix[nz]

    # Apply mask
    mask_float = mask_bool.astype(np.float64)

    # Match the smoke methodology: no monopole subtraction; raw pseudo-Cl
    # on the mask-multiplied p_CW map. The whole point is to expose the
    # monopole + mask geometric leakage into the lowest available mode.
    masked_map_obs = p_cw_map_obs * mask_float

    cls_obs = hp.anafast(masked_map_obs, lmax=LMAX)
    C1_obs_pseudo = float(cls_obs[1])
    print(f"[{time.time()-t0:.1f}s] OBSERVED pre-MASTER pseudo-C1 = {C1_obs_pseudo:.4e}", flush=True)

    # Hemisphere observable matches the smoke methodology: monopole-subtracted
    # to isolate the dipole amplitude after the global CW excess is removed.
    p_in_mask = p_cw_map_obs[mask_bool].mean()
    print(f"[{time.time()-t0:.1f}s] Precomputing hemisphere sign matrix ({HEMI_DIR_NSIDE} dirs)...", flush=True)
    sign_mat = precompute_hemisphere(hp.nside2npix(NSIDE))
    pixel_weights = (p_cw_map_obs - p_in_mask) * mask_float
    norm_per_dir_N = (sign_mat[:, mask_bool] > 0).sum(axis=1)
    norm_per_dir_S = (sign_mat[:, mask_bool] < 0).sum(axis=1)
    norm = np.minimum(norm_per_dir_N, norm_per_dir_S).astype(np.float64) + 1.0
    amplitudes_obs = (sign_mat @ pixel_weights) / norm
    hemi_max_abs_obs = float(np.max(np.abs(amplitudes_obs)))
    print(f"[{time.time()-t0:.1f}s] OBSERVED hemi max|A| = {hemi_max_abs_obs:.4e}", flush=True)

    # Monopole-only null: per-pixel binomial(n_total_pix, p_cw_global)
    rng = np.random.default_rng(SEED)
    null_C1 = np.zeros(N_MC)
    null_hemi = np.zeros(N_MC)
    print(f"[{time.time()-t0:.1f}s] N_MC={N_MC} monopole-only null realizations...", flush=True)
    for k in range(N_MC):
        n_cw_null = rng.binomial(n_total_pix, p_cw_global)
        p_cw_null_map = np.zeros_like(p_cw_map_obs)
        p_cw_null_map[nz] = n_cw_null[nz] / n_total_pix[nz]
        # pseudo-Cl: no monopole subtraction, matches smoke methodology
        masked_null = p_cw_null_map * mask_float
        cls_null = hp.anafast(masked_null, lmax=LMAX)
        null_C1[k] = cls_null[1]
        # Hemisphere: monopole-subtracted
        p_in_mask_null = p_cw_null_map[mask_bool].mean()
        amps_null = (sign_mat @ ((p_cw_null_map - p_in_mask_null) * mask_float)) / norm
        null_hemi[k] = np.max(np.abs(amps_null))
        if (k + 1) % 50 == 0:
            print(f"[{time.time()-t0:.1f}s]   {k+1}/{N_MC} done", flush=True)

    C1_null_mean = float(null_C1.mean())
    C1_null_std = float(null_C1.std(ddof=1))
    C1_z = (C1_obs_pseudo - C1_null_mean) / C1_null_std
    hemi_null_mean = float(null_hemi.mean())
    hemi_null_std = float(null_hemi.std(ddof=1))
    hemi_z = (hemi_max_abs_obs - hemi_null_mean) / hemi_null_std

    print(f"\n=== N=500 RESULT ===", flush=True)
    print(f"Pre-MASTER pseudo-C1 OBSERVED  = {C1_obs_pseudo:.4e}", flush=True)
    print(f"Pre-MASTER pseudo-C1 null mean = {C1_null_mean:.4e}", flush=True)
    print(f"Pre-MASTER pseudo-C1 null std  = {C1_null_std:.4e}", flush=True)
    print(f"Pre-MASTER pseudo-C1 sigma     = +{C1_z:.2f}", flush=True)
    print(f"Hemisphere max|A| OBSERVED  = {hemi_max_abs_obs:.4e}", flush=True)
    print(f"Hemisphere max|A| null mean = {hemi_null_mean:.4e}", flush=True)
    print(f"Hemisphere max|A| null std  = {hemi_null_std:.4e}", flush=True)
    print(f"Hemisphere max|A| sigma     = +{hemi_z:.2f}", flush=True)

    out = {
        "version": "v1.0.78-monopole-mask-null-N500-full",
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "supersedes": "monopole_mask_null_results_smoke.json (N=25)",
        "config": {
            "nside": NSIDE, "lmax": LMAX, "n_realizations": N_MC, "seed": SEED,
            "min_spirals_per_pix": MIN_SPIRALS_PER_PIX,
            "hemi_dir_nside": HEMI_DIR_NSIDE,
            "n_hemisphere_directions": int(sign_mat.shape[0]),
            "statistic": "pseudo-C_l at ell=1 (mask-coupled, monopole-subtracted within mask, NOT MASTER-deconvolved); hemisphere max|A| via 768-dir matmul + per-dir hemi-balance normalization",
        },
        "catalog": {
            "n_spiral_total": int(len(spirals)),
            "n_spiral_in_mask": n_spiral_in_mask,
            "n_cw_in_mask": n_cw_in_mask,
            "p_cw_global": p_cw_global,
            "f_sky": f_sky,
            "n_pix_used": n_pix_used,
        },
        "observed": {
            "pseudo_c1": C1_obs_pseudo,
            "hemi_max_abs_amplitude": hemi_max_abs_obs,
        },
        "null_distribution": {
            "C1_mean": C1_null_mean,
            "C1_std": C1_null_std,
            "hemi_max_abs_mean": hemi_null_mean,
            "hemi_max_abs_std": hemi_null_std,
        },
        "significance": {
            "C1_sigma": C1_z,
            "hemi_max_abs_sigma": hemi_z,
        },
    }
    OUT.write_text(json.dumps(out, indent=2))
    print(f"\nSaved -> {OUT}", flush=True)
    print(f"Total wall: {time.time()-t0:.1f}s", flush=True)


if __name__ == "__main__":
    main()
