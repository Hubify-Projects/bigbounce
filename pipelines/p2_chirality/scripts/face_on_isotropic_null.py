#!/usr/bin/env python3
"""
Compute HC-spiral / HC-strict dipole sigma under the SAME isotropic-p=0.5
null used for the paper's headline 0.43-sigma result, for like-for-like
comparison with the monopole-preserving null in tab:face_on.

Closes GPT-M1 / Grok-B2 convergent finding: 'recompute the HC-spiral dipole
under the isotropic p=0.5 null used everywhere else'.
"""
import json
import numpy as np
import pandas as pd
import healpy as hp
from huggingface_hub import hf_hub_download

NSIDE = 64
N_MC = 1000
SEED = 42

print("Loading catalog ...", flush=True)
p = hf_hub_download("bamfai/galaxy-chirality-catalog", "catalog_production.parquet", repo_type="dataset")
df = pd.read_parquet(p, columns=["ra", "dec", "class_eq", "p_cw_eq", "p_ccw_eq"])
print(f"  full catalog: {len(df):,}", flush=True)
df = df[df["class_eq"].isin(["CW", "CCW"])].reset_index(drop=True)
print(f"  spirals: {len(df):,}", flush=True)


def assign_pix(ra, dec):
    theta = np.radians(90.0 - dec)
    phi = np.radians(ra)
    return hp.ang2pix(NSIDE, theta, phi)


def cw_count_map(df_sub):
    pix = assign_pix(df_sub["ra"].values, df_sub["dec"].values)
    n_total = np.bincount(pix, minlength=hp.nside2npix(NSIDE))
    cw_mask = df_sub["class_eq"].values == "CW"
    n_cw = np.bincount(pix[cw_mask], minlength=hp.nside2npix(NSIDE))
    return n_total, n_cw


def dipole_amplitude_from_map(n_total, n_cw):
    """Weighted dipole fit. Returns full-amplitude A in p = 0.5*(1+A cos theta).
    Solve A cos theta + monopole = (p_pix - 0.5) by weighted least squares
    in (n_x, n_y, n_z, 1) using each pixel's spiral count as weight."""
    npix = len(n_total)
    nside = hp.npix2nside(npix)
    nz = n_total > 0
    if nz.sum() < 10:
        return 0.0
    pix_idx = np.where(nz)[0]
    theta, phi = hp.pix2ang(nside, pix_idx)
    nx = np.sin(theta) * np.cos(phi)
    ny = np.sin(theta) * np.sin(phi)
    nz_axis = np.cos(theta)
    p_pix = n_cw[nz] / n_total[nz]
    w = n_total[nz].astype(float)
    # weighted least squares
    X = np.column_stack([nx, ny, nz_axis, np.ones(len(nx))])
    W = w
    XW = X * W[:, None]
    A_mat = XW.T @ X
    b = XW.T @ p_pix
    try:
        coef = np.linalg.solve(A_mat, b)
    except np.linalg.LinAlgError:
        return 0.0
    dx, dy, dz, mono = coef
    # p = mono + dx*nx + dy*ny + dz*nz; the dipole amplitude in p-space is sqrt(dx^2+dy^2+dz^2).
    # In the full-amplitude convention p = 0.5*(1 + A cos theta), A = 2 * |dipole|.
    A_dipole = 2.0 * np.sqrt(dx**2 + dy**2 + dz**2)
    return float(A_dipole)


def isotropic_null_realization(n_total, rng, p_iso=0.5):
    n_cw_null = rng.binomial(n_total, p_iso)
    return n_cw_null


def run_subsample(df_sub, label):
    print(f"\n--- {label}: N={len(df_sub):,} ---", flush=True)
    n_total, n_cw_obs = cw_count_map(df_sub)
    n_spirals = int(n_total.sum())
    n_cw_global = int(n_cw_obs.sum())
    p_cw = n_cw_global / n_spirals
    A_obs = dipole_amplitude_from_map(n_total, n_cw_obs)
    print(f"  N_spiral={n_spirals:,}, p_CW={p_cw:.5f}, |A_obs|={A_obs*100:.3f}%", flush=True)

    rng = np.random.default_rng(SEED)
    null_A = np.zeros(N_MC)
    for i in range(N_MC):
        n_cw_null = isotropic_null_realization(n_total, rng, p_iso=0.5)
        null_A[i] = dipole_amplitude_from_map(n_total, n_cw_null)
        if (i + 1) % 200 == 0:
            print(f"  MC {i+1}/{N_MC}", flush=True)
    null_mean = null_A.mean()
    null_std = null_A.std(ddof=1)
    sigma = (A_obs - null_mean) / null_std
    # one-sided rank p-value
    rank = int((null_A >= A_obs).sum())
    p_value = (rank + 1) / (N_MC + 1)
    print(f"  isotropic-null: mean={null_mean*100:.3f}%, std={null_std*100:.3f}%", flush=True)
    print(f"  -> sigma_iso = {sigma:+.2f}, p = {p_value:.3f}", flush=True)
    return {"label": label, "N_spiral": n_spirals, "p_CW": p_cw,
            "A_obs_pct": A_obs * 100, "null_mean_pct": null_mean * 100,
            "null_std_pct": null_std * 100,
            "sigma_isotropic": sigma, "p_value_isotropic": p_value}


results = {}
results["Catalog_C_full"] = run_subsample(df, "Catalog C full")

max_eq = df[["p_cw_eq", "p_ccw_eq"]].max(axis=1)
hc06 = df[max_eq > 0.6].reset_index(drop=True)
results["HC_spiral_p_gt_0p6"] = run_subsample(hc06, "HC-spiral (p_eq > 0.6)")

hc08 = df[max_eq > 0.8].reset_index(drop=True)
results["HC_strict_p_gt_0p8"] = run_subsample(hc08, "HC-strict (p_eq > 0.8)")

out_path = "/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p2_chirality/outputs/canonical_provenance/face_on_isotropic_null_results.json"
with open(out_path, "w") as f:
    json.dump({"config": {"NSIDE": NSIDE, "N_MC": N_MC, "SEED": SEED, "null": "isotropic p=0.5"},
               "results": results}, f, indent=2)
print(f"\nSaved -> {out_path}")
