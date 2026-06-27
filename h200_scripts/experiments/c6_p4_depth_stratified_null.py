#!/usr/bin/env python3
"""
C6 — Depth-stratified per-galaxy label-shuffle null for the P4 real-footprint
subsample-mask MASTER ell=1 excess.

Background: C3 (c3_p4_wp_invariance_fsky.py) found the real-catalog
subsample-mask (N_all >= 1, NSIDE=64) MASTER-deconvolved single-mode ell=1
measurement gives +7.28 sigma (Wp=N_all) / +9.78 sigma (Wp=N_spiral) against
a GLOBAL per-galaxy CW/CCW label-shuffle null (500 MC, seed 42).

Question: is that excess absorbed when the null PRESERVES the depth/sampling
structure of the catalog? If yes, the excess is a depth-correlated systematic,
consistent with the paper's interpretation-(ii) attribution.

This job is identical to C3 (same data load, same mask = N_all >= 1 at
NSIDE=64, same C^2 2-deg apodization, same A_p field with galaxy-weighted
mask-mean subtraction, same single-mode MASTER ell=1, seed 42) with ONE
change: the 500-MC null permutes per-galaxy CW/CCW labels WITHIN 10
pixel-density deciles (deciles of N_all(p) over in-mask pixels; each galaxy
belongs to its pixel's decile) instead of globally. This mirrors the
canonical-mask density-stratified null methodology in
pipelines/p2_chirality/scripts/systematics_preserving_null.py, lifted from
pixel-level A_p permutation to galaxy-level label permutation.

Run on pod:
  tmux new -s c6 -d 'cd /workspace && python3 c6_p4_depth_stratified_null.py 2>&1 | tee c6.log'
Output: /workspace/c6_results/c6_depth_stratified_null.json
ETA: comparable to C3 (2 x (1+500) NaMaster decouples at NSIDE=64).
"""
from __future__ import annotations

import json
import os
import time
from pathlib import Path

import numpy as np
import pandas as pd
import healpy as hp
import pymaster as nmt
from huggingface_hub import hf_hub_download

NSIDE = 64
LMAX = 3 * NSIDE - 1  # 191
N_MC = 500
N_STRATA = 10  # pixel-density deciles
SEED = 42
APOD_DEG = 2.0
APOD_TYPE = "C2"
MASK_DEFINITION = "N_all >= 1"
C3_REFERENCE_SIGMA = {"Wp_Nall": 7.28, "Wp_Nspiral": 9.78}  # global-shuffle null
OUTDIR = Path(os.environ.get("C6_OUTDIR", "/workspace/c6_results"))
OUT = OUTDIR / "c6_depth_stratified_null.json"


def main() -> int:
    t0 = time.time()
    OUTDIR.mkdir(parents=True, exist_ok=True)
    print(f"[{time.time()-t0:.1f}s] C6 depth-stratified null job starting", flush=True)

    cat_path = hf_hub_download("bamfai/galaxy-chirality-catalog",
                               "catalog_production.parquet", repo_type="dataset")
    df = pd.read_parquet(cat_path, columns=["ra", "dec", "class_eq"])
    print(f"[{time.time()-t0:.1f}s] catalog rows (all classes): {len(df):,}", flush=True)

    npix = hp.nside2npix(NSIDE)
    pix_all = hp.ang2pix(NSIDE,
                         np.radians(90.0 - df["dec"].values.astype(np.float64)),
                         np.radians(df["ra"].values.astype(np.float64))).astype(np.int64)
    is_cw = (df["class_eq"].values == "CW")
    is_ccw = (df["class_eq"].values == "CCW")
    is_spiral = is_cw | is_ccw

    n_all_pix = np.bincount(pix_all, minlength=npix).astype(np.float64)
    n_spiral_pix = np.bincount(pix_all[is_spiral], minlength=npix).astype(np.float64)

    # Spiral-level arrays for the label-shuffle null
    pix_sp = pix_all[is_spiral]
    labels_cw = is_cw[is_spiral].astype(np.int8)
    n_sp = len(labels_cw)
    print(f"[{time.time()-t0:.1f}s] spirals: {n_sp:,}  p_CW={labels_cw.mean():.6f}", flush=True)

    # ---------- Subsample mask: N_all >= 1 (same as C3 selected mask) ----------
    mask_bool = n_all_pix >= 1
    mask_binary = mask_bool.astype(np.float64)
    n_pix_mask = int(mask_bool.sum())
    fsky_raw = float(mask_binary.mean())
    print(f"[{time.time()-t0:.1f}s] mask {MASK_DEFINITION}: n_pix={n_pix_mask} "
          f"f_sky={fsky_raw:.5f}", flush=True)

    print(f"[{time.time()-t0:.1f}s] apodizing mask ({APOD_TYPE}, {APOD_DEG} deg) ...", flush=True)
    mask_apod = nmt.mask_apodization(mask_binary, APOD_DEG, apotype=APOD_TYPE)

    W_nall = n_all_pix * mask_binary
    W_nsp = n_spiral_pix * mask_binary

    # ---------- Depth stratification: deciles of N_all(p) over in-mask pixels ----------
    # Mirrors systematics_preserving_null.py: quantile edges over positive in-mask
    # counts, digitize each in-mask pixel into a decile.
    n_in = n_all_pix[mask_bool]
    strata_edges = np.quantile(n_in[n_in > 0], np.linspace(0, 1, N_STRATA + 1))
    strata_edges[0] = -1.0  # include any zero-count pixels in stratum 0
    strata_edges[-1] = n_in.max() + 1.0
    pix_strata = np.full(npix, -1, dtype=np.int8)
    pix_strata[mask_bool] = np.digitize(n_all_pix[mask_bool], strata_edges[1:-1])
    strata_pix_sizes = [int((pix_strata == s).sum()) for s in range(N_STRATA)]
    print(f"[{time.time()-t0:.1f}s] strata pixel sizes: {strata_pix_sizes}", flush=True)

    # Each galaxy belongs to its pixel's decile
    gal_strata = pix_strata[pix_sp]
    if (gal_strata < 0).any():
        # By construction every spiral's pixel has N_all >= 1, so this should be empty.
        n_bad = int((gal_strata < 0).sum())
        raise RuntimeError(f"{n_bad} spirals fall outside the mask strata — mask logic error")
    stratum_to_gal = [np.where(gal_strata == s)[0] for s in range(N_STRATA)]
    strata_gal_sizes = [len(g) for g in stratum_to_gal]
    strata_cw_frac = [float(labels_cw[g].mean()) if len(g) else float("nan")
                      for g in stratum_to_gal]
    print(f"[{time.time()-t0:.1f}s] strata galaxy counts: {strata_gal_sizes}", flush=True)
    print(f"[{time.time()-t0:.1f}s] strata CW fractions: "
          f"{[f'{f:.4f}' for f in strata_cw_frac]}", flush=True)

    # ---------- Field construction (identical to C3) ----------
    nz = n_spiral_pix > 0

    def build_A_sub(labels: np.ndarray, weight_pix: np.ndarray) -> np.ndarray:
        """A_p = (N_CW - N_CCW)/N_spiral with weight-map-weighted mask-mean
        subtraction (galaxy-weighted convention, weights = W_p)."""
        n_cw = np.bincount(pix_sp[labels == 1], minlength=npix).astype(np.float64)
        n_ccw = np.bincount(pix_sp[labels == 0], minlength=npix).astype(np.float64)
        A = np.zeros(npix)
        A[nz] = (n_cw[nz] - n_ccw[nz]) / n_spiral_pix[nz]
        wsel = mask_bool & nz
        A_gw = float((A[wsel] * weight_pix[wsel]).sum() / weight_pix[wsel].sum())
        A_sub = np.zeros(npix)
        A_sub[wsel] = A[wsel] - A_gw
        return A_sub

    # Custom NmtBin including ell=1 (single-ell bandpowers), identical to C3
    bpws = np.full(LMAX + 1, -1, dtype=np.int32)
    for ell in range(1, LMAX + 1):
        bpws[ell] = ell - 1
    b_custom = nmt.NmtBin(bpws=bpws, ells=np.arange(LMAX + 1, dtype=np.int32),
                          weights=np.ones(LMAX + 1), lmax=LMAX)

    variants = {}
    for name, W in [("Wp_Nall", W_nall), ("Wp_Nspiral", W_nsp)]:
        tv = time.time()
        W_eff = W * mask_apod
        print(f"\n[{time.time()-t0:.1f}s] === variant {name}: coupling matrix ...", flush=True)
        f_dummy = nmt.NmtField(W_eff, [np.zeros(npix)], lite=True)
        w = nmt.NmtWorkspace()
        w.compute_coupling_matrix(f_dummy, f_dummy, b_custom)

        A_data = build_A_sub(labels_cw, W)
        f_data = nmt.NmtField(W_eff, [A_data], lite=True)
        C1_data = float(w.decouple_cell(nmt.compute_coupled_cell(f_data, f_data))[0][0])
        print(f"[{time.time()-t0:.1f}s] {name} data decoupled C1 = {C1_data:.4e}", flush=True)

        # 500-MC depth-stratified per-galaxy label-shuffle null:
        # permute CW/CCW labels WITHIN each pixel-density decile (preserves the
        # per-decile CW count, i.e. any depth-correlated label fraction trend).
        rng = np.random.default_rng(SEED)  # same seed per variant for paired comparison
        labels_perm = labels_cw.copy()
        C1_null = np.zeros(N_MC)
        for k in range(N_MC):
            for g_idx in stratum_to_gal:
                labels_perm[g_idx] = labels_perm[g_idx][rng.permutation(len(g_idx))]
            A_n = build_A_sub(labels_perm, W)
            f_n = nmt.NmtField(W_eff, [A_n], lite=True)
            C1_null[k] = float(w.decouple_cell(nmt.compute_coupled_cell(f_n, f_n))[0][0])
            if (k + 1) % 25 == 0:
                el = time.time() - tv
                eta = el / (k + 1) * (N_MC - k - 1)
                print(f"[{time.time()-t0:.1f}s]  {name} null {k+1}/{N_MC} "
                      f"mean={C1_null[:k+1].mean():.4e} ETA {eta:.0f}s", flush=True)

        m, s = float(C1_null.mean()), float(C1_null.std(ddof=1))
        sigma = (C1_data - m) / s
        n_exceed = int((C1_null >= C1_data).sum())
        p_one_sided = (1 + n_exceed) / (N_MC + 1)
        p_two_sided = 2.0 * min(n_exceed, N_MC - n_exceed) / N_MC
        variants[name] = {
            "C1_data_decoupled": C1_data,
            "null_mean": m, "null_std": s,
            "sigma": sigma,
            "n_exceed_null": n_exceed,
            "empirical_rank_p_one_sided": p_one_sided,
            "empirical_rank_p_two_sided": p_two_sided,
            "n_mc": N_MC,
            "c3_global_shuffle_sigma_reference": C3_REFERENCE_SIGMA[name],
            "wallclock_s": time.time() - tv,
        }
        print(f"[{time.time()-t0:.1f}s] {name} sigma = {sigma:+.4f} "
              f"(C3 global-shuffle reference {C3_REFERENCE_SIGMA[name]:+.2f}) "
              f"p_one_sided = {p_one_sided:.4f}", flush=True)

    result = {
        "job": "C6-P4-depth-stratified-null",
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "purpose": ("Depth-stratified per-galaxy label-shuffle null for the C3 "
                    "real-footprint subsample-mask MASTER ell=1 excess "
                    "(+7.28 sigma Wp=N_all / +9.78 sigma Wp=N_spiral vs global "
                    "shuffle). If sigma vs this null is small, the excess is a "
                    "depth/sampling systematic, consistent with the paper's "
                    "interpretation-(ii) attribution."),
        "config": {
            "nside": NSIDE, "lmax": LMAX, "n_mc": N_MC, "seed": SEED,
            "apodization": f"{APOD_TYPE} {APOD_DEG} deg",
            "mask_definition": MASK_DEFINITION,
            "mask_n_pix": n_pix_mask,
            "f_sky": fsky_raw,
            "field": "A_p=(N_CW-N_CCW)/N_spiral, weight-map-weighted mask-mean subtracted",
            "null": ("per-galaxy CW-label permutation WITHIN 10 pixel-density "
                     "deciles (deciles of N_all(p) over in-mask pixels; each "
                     "galaxy assigned its pixel's decile); 500 MC, seed 42"),
            "stratification": {
                "scheme": "N_all(p) deciles over in-mask pixels",
                "n_strata": N_STRATA,
                "strata_edges": [float(e) for e in strata_edges],
                "strata_pixel_sizes": strata_pix_sizes,
                "strata_galaxy_counts": strata_gal_sizes,
                "strata_cw_fractions": strata_cw_frac,
                "methodology_reference":
                    "pipelines/p2_chirality/scripts/systematics_preserving_null.py",
            },
            "n_spirals": n_sp,
        },
        "results": variants,
        "c3_reference": {
            "job": "C3-P4-Wp-invariance-and-fsky-eff",
            "null": "global per-galaxy label shuffle",
            "sigma": C3_REFERENCE_SIGMA,
        },
        "wallclock_s": time.time() - t0,
    }
    OUT.write_text(json.dumps(result, indent=2))
    print(f"\n=== C6 RESULTS ===", flush=True)
    for name, v in variants.items():
        print(f"  {name}: sigma = {v['sigma']:+.4f} (global-shuffle ref "
              f"{C3_REFERENCE_SIGMA[name]:+.2f}) p1s={v['empirical_rank_p_one_sided']:.4f}",
              flush=True)
    print(f"wrote {OUT}  ({time.time()-t0:.0f}s)", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
