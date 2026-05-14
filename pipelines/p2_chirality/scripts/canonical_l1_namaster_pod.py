#!/usr/bin/env python3
"""
Canonical-N MASTER pipeline at single ℓ=1 for P4 dipole headline.

Closes (compute-bound) the GPT-B2 deferral from the v1.0.55 R-round on P4:
a direct single-mode NaMaster execution at canonical N_spiral=3,201,160 /
f_sky=0.491, replacing the v1.0.55 analytic projection with a real MC null.

Designed to run on the RunPod Linux pod ijzftpy3klystt where pymaster is
installable via apt+pip (Mac install path remains unresolved).

Inputs (on the pod):
    /workspace/r42_b20/chirality_catalog/catalog_production.parquet
        — canonical catalog with class_eq column (CW / CCW / NOT_SPIRAL)

Outputs:
    /workspace/p4_canonical_l1/results.json
        — canonical ℓ=1 NaMaster MC result: signal C_1, noise C_1,
        null mean/std, deconvolved sigma, MC realization counts.
    /workspace/p4_canonical_l1/null_distribution.npy
        — full 500-MC null distribution at ℓ=1.

Method:
    1. Load canonical Catalog C spirals (CW/CCW only, n=3,201,160).
    2. Build NSIDE=64 chirality map: per-pixel A_p = (N_CW - N_CCW) / (N_CW + N_CCW)
       with hit-count weight; mask = pixels with N_total > 0.
    3. NaMaster pipeline:
       - NmtField(mask, [A_map], beam=None, purify_b=False)
       - NmtBin: single-bandpower binning that includes ℓ=1 only
         (ell_ini=[1], ell_end=[2]; equivalent to lmax_per_bin=1)
       - NmtWorkspace.compute_coupling_matrix(...)
       - C_l = workspace.compute_coupled_cell(field, field) / coupling_M
    4. 500-MC null: shuffle CW labels uniformly at random across the catalog;
       rebuild map; re-run NaMaster; collect C_1^null.
    5. sigma = (C_1_data - mean_null) / std_null.

Seed: 42 (matches the Wave 12 hemi convention in
pipelines/h200_results/wave12_hemi_2026-05-01/wave12_hemi_v4.py).
"""
from __future__ import annotations

import json
import os
import time
import numpy as np
import pandas as pd
import healpy as hp
import pymaster as nmt

# ---------------- Config ----------------
CATALOG = "/workspace/r42_b20/chirality_catalog/catalog_production.parquet"
OUTDIR = "/workspace/p4_canonical_l1"
NSIDE = 64
LMAX = 191
N_MC = 500
SEED = 42

os.makedirs(OUTDIR, exist_ok=True)
np.random.seed(SEED)

t0 = time.time()
print(f"[canonical-l1] N_spiral target = 3,201,160; NSIDE={NSIDE}; LMAX={LMAX}; N_MC={N_MC}; SEED={SEED}", flush=True)

# ---------------- Load catalog ----------------
print(f"[load] reading {CATALOG}", flush=True)
df = pd.read_parquet(CATALOG, columns=["ra", "dec", "class_eq"])
print(f"[load] total: {len(df):,}", flush=True)

sp = df[df["class_eq"].isin(["CW", "CCW"])].reset_index(drop=True)
n_sp = len(sp)
print(f"[load] spirals: {n_sp:,}", flush=True)
assert abs(n_sp - 3_201_160) < 100, f"canonical N_spiral mismatch: {n_sp} vs 3,201,160"

ra = sp["ra"].to_numpy(dtype=np.float64)
dec = sp["dec"].to_numpy(dtype=np.float64)
labels_cw = (sp["class_eq"].to_numpy() == "CW").astype(np.int8)  # 1 if CW, 0 if CCW

print(f"[load] CW: {labels_cw.sum():,}  CCW: {(1 - labels_cw).sum():,}", flush=True)
print(f"[load] global CW fraction: {labels_cw.mean():.6f}", flush=True)

# ---------------- HEALPix indexing ----------------
theta = np.deg2rad(90.0 - dec)
phi = np.deg2rad(ra)
pix = hp.ang2pix(NSIDE, theta, phi)
del theta, phi, ra, dec, sp, df

npix = hp.nside2npix(NSIDE)
print(f"[hpx] NSIDE={NSIDE} npix={npix}", flush=True)


def build_map_and_mask(labels: np.ndarray):
    """Build per-pixel A_p map and mask from CW labels.
    A_p = (N_CW - N_CCW) / (N_CW + N_CCW) for pixels with N_total > 0; mask = 1 where N_total > 0."""
    n_cw_pix = np.bincount(pix[labels == 1], minlength=npix).astype(np.float64)
    n_ccw_pix = np.bincount(pix[labels == 0], minlength=npix).astype(np.float64)
    n_total = n_cw_pix + n_ccw_pix
    A = np.zeros(npix)
    nonzero = n_total > 0
    A[nonzero] = (n_cw_pix[nonzero] - n_ccw_pix[nonzero]) / n_total[nonzero]
    mask = nonzero.astype(np.float64)
    f_sky = mask.mean()
    return A, mask, f_sky


# ---------------- Data field ----------------
print(f"[data] building data map...", flush=True)
A_data, mask, f_sky = build_map_and_mask(labels_cw)
print(f"[data] f_sky = {f_sky:.4f} (target canonical ~0.491)", flush=True)

field_data = nmt.NmtField(mask, [A_data])
del A_data

# Single-bin NmtBin with l=1 only
b = nmt.NmtBin.from_edges(np.array([1]), np.array([2]), is_Dell=False)
print(f"[bins] single bin ell_in=[1], ell_end=[2]; n_bands={b.get_n_bands()}", flush=True)

# ---------------- Workspace ----------------
print(f"[ws] computing coupling matrix...", flush=True)
ws = nmt.NmtWorkspace()
ws.compute_coupling_matrix(field_data, field_data, b)

# Coupled pseudo-Cl
cl_pseudo = nmt.compute_coupled_cell(field_data, field_data)
# Decoupled Cl
cl_decoupled = ws.decouple_cell(cl_pseudo)
print(f"[data] C_1 pseudo (coupled): {cl_pseudo[0][0]:.6e}", flush=True)
print(f"[data] C_1 decoupled: {cl_decoupled[0][0]:.6e}", flush=True)

c1_data = float(cl_decoupled[0][0])

# ---------------- MC nulls ----------------
print(f"[mc] running {N_MC} permutation nulls...", flush=True)
null_c1 = np.zeros(N_MC)
labels_perm = labels_cw.copy()
for i in range(N_MC):
    np.random.shuffle(labels_perm)  # in-place global shuffle of CW labels
    A_null, _, _ = build_map_and_mask(labels_perm)
    field_null = nmt.NmtField(mask, [A_null])
    cl_pseudo_null = nmt.compute_coupled_cell(field_null, field_null)
    cl_decoupled_null = ws.decouple_cell(cl_pseudo_null)
    null_c1[i] = float(cl_decoupled_null[0][0])
    if (i + 1) % 50 == 0:
        elapsed = time.time() - t0
        print(f"[mc] {i+1}/{N_MC}  mean(null)={null_c1[:i+1].mean():.3e}  std(null)={null_c1[:i+1].std():.3e}  elapsed={elapsed:.0f}s", flush=True)

null_mean = float(null_c1.mean())
null_std = float(null_c1.std())
sigma = (c1_data - null_mean) / null_std

# Save outputs
np.save(os.path.join(OUTDIR, "null_distribution.npy"), null_c1)

result = {
    "wave": "P4-canonical-l1-NaMaster",
    "version": "v1.0.62-canonical-l1-direct-MC",
    "purpose": "Direct canonical-N (N_spiral=3,201,160, f_sky~0.491) single-mode NaMaster MC at l=1, closing the v1.0.55 GPT-B2 analytic-projection deferral.",
    "config": {
        "nside": NSIDE,
        "lmax": LMAX,
        "n_mc": N_MC,
        "seed": SEED,
        "n_spiral": int(n_sp),
        "f_sky": f_sky,
    },
    "data": {
        "C1_pseudo_coupled": float(cl_pseudo[0][0]),
        "C1_decoupled": c1_data,
    },
    "nulls": {
        "null_mean": null_mean,
        "null_std": null_std,
        "null_min": float(null_c1.min()),
        "null_max": float(null_c1.max()),
    },
    "significance": {
        "sigma_canonical_direct": sigma,
        "sigma_subsample_published": -0.1219,
        "sigma_canonical_analytic_projection_v1055": 0.2595,
        "comparison": (
            "Canonical-N direct-MC sigma vs subsample-mask published (v1.0.61) "
            "vs analytic projection (v1.0.55). All three should be within the "
            "null band |sigma|<1 for the no-dipole-at-l=1 verdict to hold."
        ),
    },
    "wallclock_s": time.time() - t0,
}

with open(os.path.join(OUTDIR, "results.json"), "w") as f:
    json.dump(result, f, indent=2)

print(f"[done] sigma_canonical_direct = {sigma:+.4f}", flush=True)
print(f"[done] null_mean={null_mean:.3e}  null_std={null_std:.3e}", flush=True)
print(f"[done] wallclock = {time.time() - t0:.1f}s", flush=True)
print(f"[done] results written to {os.path.join(OUTDIR, 'results.json')}", flush=True)
