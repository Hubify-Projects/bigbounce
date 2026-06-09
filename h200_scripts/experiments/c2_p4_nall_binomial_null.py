#!/usr/bin/env python3
"""
C2 — P4 N_all-trial binomial monopole-only generative null (500 MC).

Closes the in-queue item declared in chirality_catalog_paper.tex
footnote (fn:binomial_nspiral, Sec. sec:monopole_mask_null):
"A parallel rerun on N(p)_all-trial draws is in queue for the
canonical-mask sensitivity-budget recompute."

Replicates the monopole-only generative null of
pipelines/p2_chirality/scripts/monopole_mask_null_sim_v2.py
(N=500 realizations, canonical mask = pixels with >=10 spirals,
f_sky=0.49005, seed 42) but with the per-pixel CW count drawn from
    Binomial(N_all(p), p_CW_global)
instead of
    Binomial(N_spiral(p), p_CW_global),
where N_all(p) = N_CW + N_CCW + N_NOT_SPIRAL per pixel.

Reference values from the published N_spiral-trial run
(outputs/canonical_provenance/monopole_mask_null_results.json):
  - pre-MASTER pseudo-C1 reproduction = 99.322 %
  - pre-MASTER residual sigma         = +1.691

Additionally runs the MASTER-decoupled version of the same null
(mirroring scripts/master_decoupled_monopole_null.py, v1.0.121
convention: galaxy-weighted monopole subtraction, custom NmtBin
including ell=1) so both the pre-MASTER and post-MASTER residuals
are reported under the N_all trial pool.

Fraction convention: the null CW-fraction map is
  p_null(p) = n_cw_null(p) / N_all(p)
(keeps the null monopole at p_CW_global; the trial-count inflation
factor <N_all/N_spiral> ~ 1.49 enters through the binomial variance).
For completeness the (non-self-consistent) alternative normalization
n_cw_null(p)/N_spiral(p) is also recorded.

Run on pod:
  tmux new -s c2 -d 'cd /workspace && python3 c2_p4_nall_binomial_null.py 2>&1 | tee c2.log'
Output: /workspace/c2_results/c2_nall_binomial_null.json
ETA: ~30-90 min CPU.
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
SEED = 42
MIN_SPIRALS_PER_PIX = 10
OUTDIR = Path(os.environ.get("C2_OUTDIR", "/workspace/c2_results"))
OUT = OUTDIR / "c2_nall_binomial_null.json"

# Published N_spiral-trial reference values (monopole_mask_null_results.json)
REF_NSPIRAL = {
    "pre_master_reproduction_pct": 99.322,
    "pre_master_residual_sigma": 1.691017811745476,
}


def main() -> int:
    t0 = time.time()
    OUTDIR.mkdir(parents=True, exist_ok=True)
    print(f"[{time.time()-t0:.1f}s] C2 N_all-trial binomial monopole-only null x {N_MC}", flush=True)

    cat_path = hf_hub_download("bamfai/galaxy-chirality-catalog",
                               "catalog_production.parquet", repo_type="dataset")
    df = pd.read_parquet(cat_path, columns=["ra", "dec", "class_eq"])
    n_catalog_total = len(df)
    print(f"[{time.time()-t0:.1f}s] catalog rows (all classes): {n_catalog_total:,}", flush=True)

    npix = hp.nside2npix(NSIDE)
    pix_all = hp.ang2pix(NSIDE,
                         np.radians(90.0 - df["dec"].values.astype(np.float64)),
                         np.radians(df["ra"].values.astype(np.float64))).astype(np.int64)
    is_cw = (df["class_eq"].values == "CW")
    is_ccw = (df["class_eq"].values == "CCW")
    is_spiral = is_cw | is_ccw

    n_all_pix = np.bincount(pix_all, minlength=npix).astype(np.int64)
    n_spiral_pix = np.bincount(pix_all[is_spiral], minlength=npix).astype(np.int64)
    n_cw_pix = np.bincount(pix_all[is_cw], minlength=npix).astype(np.int64)

    # Canonical mask: pixels with at least MIN_SPIRALS_PER_PIX spirals
    mask_bool = n_spiral_pix >= MIN_SPIRALS_PER_PIX
    mask_float = mask_bool.astype(np.float64)
    f_sky = float(mask_bool.mean())
    n_spiral_in_mask = int(n_spiral_pix[mask_bool].sum())
    n_cw_in_mask = int(n_cw_pix[mask_bool].sum())
    n_all_in_mask = int(n_all_pix[mask_bool].sum())
    p_cw_global = n_cw_in_mask / n_spiral_in_mask
    infl = float((n_all_pix[mask_bool] / np.maximum(n_spiral_pix[mask_bool], 1)).mean())
    print(f"[{time.time()-t0:.1f}s] canonical mask: f_sky={f_sky:.5f} "
          f"(published 0.49005), n_pix={int(mask_bool.sum())}", flush=True)
    print(f"[{time.time()-t0:.1f}s] N_spiral_in_mask={n_spiral_in_mask:,} "
          f"N_all_in_mask={n_all_in_mask:,} p_CW_global={p_cw_global:.6f} "
          f"<N_all/N_spiral>={infl:.3f}", flush=True)

    # ---------- Observed maps ----------
    nz = n_spiral_pix > 0
    # CW-fraction map over spirals (the field the null reproduces)
    p_cw_map_obs = np.zeros(npix, dtype=np.float64)
    p_cw_map_obs[nz] = n_cw_pix[nz] / n_spiral_pix[nz]

    # --- Pre-MASTER observed pseudo-C1 (un-monopole-subtracted, matches v2 script) ---
    masked_map_obs = p_cw_map_obs * mask_float
    C1_obs_pseudo = float(hp.anafast(masked_map_obs, lmax=LMAX)[1])
    print(f"[{time.time()-t0:.1f}s] OBSERVED pre-MASTER pseudo-C1 = {C1_obs_pseudo:.4e}", flush=True)

    # --- Post-MASTER observed (galaxy-weighted monopole subtraction, v1.0.107+ conv.) ---
    A_obs = np.zeros(npix, dtype=np.float64)
    A_obs[nz] = (n_cw_pix[nz] / n_spiral_pix[nz]) - 0.5
    w_spiral = n_spiral_pix.astype(np.float64)
    A_gw = float((A_obs[nz] * w_spiral[nz]).sum() / w_spiral[nz].sum())
    A_obs_sub = A_obs.copy()
    A_obs_sub[nz] -= A_gw
    A_obs_sub[~nz] = 0.0

    print(f"[{time.time()-t0:.1f}s] building MASTER workspace (custom ell=1 bin) ...", flush=True)
    bpws = np.full(LMAX + 1, -1, dtype=np.int32)
    for ell in range(1, LMAX + 1):
        bpws[ell] = ell - 1
    b_custom = nmt.NmtBin(bpws=bpws, ells=np.arange(LMAX + 1, dtype=np.int32),
                          weights=np.ones(LMAX + 1), lmax=LMAX)
    f0_dummy = nmt.NmtField(mask_float, [np.zeros(npix)], lite=True)
    w = nmt.NmtWorkspace()
    w.compute_coupling_matrix(f0_dummy, f0_dummy, b_custom)
    f0_data = nmt.NmtField(mask_float, [A_obs_sub], lite=True)
    C1_obs_master = float(w.decouple_cell(nmt.compute_coupled_cell(f0_data, f0_data))[0][0])
    print(f"[{time.time()-t0:.1f}s] OBSERVED post-MASTER decoupled C1 = {C1_obs_master:.4e}", flush=True)

    # ---------- N_all-trial binomial monopole-only null x N_MC ----------
    rng = np.random.default_rng(SEED)
    null_C1_pre = np.zeros(N_MC)          # pre-MASTER, fraction = n_cw/N_all
    null_C1_pre_altnorm = np.zeros(N_MC)  # pre-MASTER, fraction = n_cw/N_spiral (diagnostic)
    null_C1_post = np.zeros(N_MC)         # post-MASTER decoupled
    nz_all = n_all_pix > 0
    print(f"[{time.time()-t0:.1f}s] running {N_MC} Binomial(N_all(p), p_CW_global) realizations ...",
          flush=True)
    for k in range(N_MC):
        n_cw_null = rng.binomial(n_all_pix, p_cw_global)

        # Pre-MASTER (self-consistent normalization by N_all)
        p_null = np.zeros(npix)
        p_null[nz_all] = n_cw_null[nz_all] / n_all_pix[nz_all]
        null_C1_pre[k] = hp.anafast(p_null * mask_float, lmax=LMAX)[1]

        # Pre-MASTER diagnostic alternative normalization by N_spiral
        p_null_alt = np.zeros(npix)
        p_null_alt[nz] = n_cw_null[nz] / n_spiral_pix[nz]
        null_C1_pre_altnorm[k] = hp.anafast(p_null_alt * mask_float, lmax=LMAX)[1]

        # Post-MASTER (galaxy-weighted monopole-subtracted, decoupled)
        A_n = np.zeros(npix)
        A_n[nz_all] = (n_cw_null[nz_all] / n_all_pix[nz_all]) - 0.5
        A_gw_n = float((A_n[nz_all] * n_all_pix[nz_all]).sum() / n_all_pix[nz_all].sum())
        A_n_sub = A_n.copy()
        A_n_sub[nz_all] -= A_gw_n
        A_n_sub[~nz_all] = 0.0
        f0_n = nmt.NmtField(mask_float, [A_n_sub], lite=True)
        null_C1_post[k] = float(w.decouple_cell(nmt.compute_coupled_cell(f0_n, f0_n))[0][0])

        if (k + 1) % 25 == 0:
            el = time.time() - t0
            print(f"[{el:.1f}s]  {k+1}/{N_MC}  pre mean={null_C1_pre[:k+1].mean():.4e}  "
                  f"post mean={null_C1_post[:k+1].mean():.4e}", flush=True)

    def stats(obs, nulls):
        m, s = float(np.mean(nulls)), float(np.std(nulls, ddof=1))
        return {
            "observed": float(obs), "null_mean": m, "null_std": s,
            "residual_sigma": (float(obs) - m) / s,
            "reproduction_pct": 100.0 * m / float(obs),
        }

    pre = stats(C1_obs_pseudo, null_C1_pre)
    pre_alt = stats(C1_obs_pseudo, null_C1_pre_altnorm)
    post = stats(C1_obs_master, null_C1_post)

    result = {
        "job": "C2-P4-Nall-trial-binomial-monopole-null",
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "purpose": ("fn:binomial_nspiral in-queue closure: rerun the monopole-only "
                    "generative null with Binomial(N_all(p), p_CW_global) trial draws "
                    "instead of Binomial(N_spiral(p), p_CW_global)."),
        "config": {
            "nside": NSIDE, "lmax": LMAX, "n_mc": N_MC, "seed": SEED,
            "min_spirals_per_pix": MIN_SPIRALS_PER_PIX, "f_sky": f_sky,
            "n_catalog_total": n_catalog_total,
            "n_spiral_in_mask": n_spiral_in_mask,
            "n_all_in_mask": n_all_in_mask,
            "p_cw_global": p_cw_global,
            "trial_count_inflation_mean_nall_over_nspiral": infl,
            "null_fraction_normalization": "n_cw_null(p) / N_all(p) (primary); n_cw_null(p)/N_spiral(p) recorded as diagnostic",
            "monopole_subtraction_post_master": "galaxy-weighted mask-mean (v1.0.107+ convention; weights = trial pool N_all for null, N_spiral for data)",
        },
        "results": {
            "pre_master_pseudo_C1": pre,
            "pre_master_pseudo_C1_altnorm_nspiral_denominator": pre_alt,
            "post_master_decoupled_C1": post,
        },
        "reference_nspiral_trial_run": REF_NSPIRAL,
        "wallclock_s": time.time() - t0,
    }
    OUT.write_text(json.dumps(result, indent=2))
    print(f"\n=== C2 RESULTS ===", flush=True)
    print(f"pre-MASTER reproduction = {pre['reproduction_pct']:.3f}% "
          f"(N_spiral ref 99.322%)", flush=True)
    print(f"pre-MASTER residual sigma = {pre['residual_sigma']:+.3f} (N_spiral ref +1.69)", flush=True)
    print(f"post-MASTER residual sigma = {post['residual_sigma']:+.3f}", flush=True)
    print(f"wrote {OUT}  ({time.time()-t0:.0f}s)", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
