#!/usr/bin/env python3
"""
Mask pixel-count threshold robustness sweep — ChatGPT external review v1.0.122
MAJOR M3 closure.

ChatGPT M3 requested a compact robustness table showing ℓ=1 MASTER
results across canonical mask, subsample mask, apodized canonical mask,
and a few objective pixel-count thresholds, plus a clear pre-specified
estimator hierarchy.

The existing artifacts already cover the canonical (+3.64σ), subsample
(-0.12σ), and apodized canonical (+3.57σ) variants. This script fills
in the missing axis: the canonical mask redefined under per-pixel
count thresholds n_total > {1, 5, 10, 20, 50} galaxies/pixel. For each
threshold:
    1. Rebuild the mask (canonical = n_total > threshold).
    2. Compute the MASTER coupling matrix on the new mask.
    3. Decouple the chirality C_ℓ with proper galaxy-weighted monopole
       subtraction (matches v1.0.107+ convention).
    4. Run 200 per-pixel-shuffle null realizations and record sigma.

If the +3.64σ canonical-mask residual is robust to objective
pixel-count threshold choice, then the result is not driven by
low-count edge pixels. Conversely, if higher thresholds attenuate the
signal toward null, then the residual is concentrated in the
low-count edge of the canonical mask (i.e., partially edge-driven).

Cost: ~3-5 min wall on a 32 GB laptop.

Output: outputs/canonical_provenance/mask_threshold_robustness_sweep.json
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np
import pandas as pd
import healpy as hp
import pymaster as nmt
from huggingface_hub import hf_hub_download

NSIDE = 64
LMAX = 3 * NSIDE - 1
N_MC = 200
SEED = 42
THRESHOLDS = [1, 5, 10, 20, 50]  # per-pixel galaxy-count cutoffs

REPO = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
OUT = REPO / "pipelines/p2_chirality/outputs/canonical_provenance/mask_threshold_robustness_sweep.json"


def main() -> int:
    t0 = time.time()
    print(f"[{time.time()-t0:.1f}s] mask-threshold robustness sweep starting", flush=True)

    cat_path = hf_hub_download("bamfai/galaxy-chirality-catalog",
                                "catalog_production.parquet", repo_type="dataset")
    df = pd.read_parquet(cat_path, columns=["ra", "dec", "class_eq"])
    spirals = df[df["class_eq"].isin(["CW", "CCW"])].reset_index(drop=True)
    print(f"[{time.time()-t0:.1f}s] spirals: {len(spirals):,}", flush=True)
    ra = spirals["ra"].values.astype(np.float64)
    dec = spirals["dec"].values.astype(np.float64)
    iscw = (spirals["class_eq"].values == "CW").astype(np.int8)
    p_cw_global = float(iscw.sum() / len(iscw))

    npix = hp.nside2npix(NSIDE)
    pix = hp.ang2pix(NSIDE, np.radians(90.0 - dec), np.radians(ra)).astype(np.int64)
    n_total = np.bincount(pix, minlength=npix).astype(np.float64)
    n_cw_obs = np.bincount(pix[iscw.astype(bool)], minlength=npix).astype(np.float64)

    # Pre-build custom NmtBin that includes ℓ=1 (mirrors master_decoupled_monopole_null.py)
    bpws = np.full(LMAX+1, -1, dtype=np.int32)
    for ell in range(1, LMAX+1):
        bpws[ell] = ell - 1
    ells_arr = np.arange(LMAX+1, dtype=np.int32)
    weights_arr = np.ones(LMAX+1, dtype=np.float64)
    b_custom = nmt.NmtBin(bpws=bpws, ells=ells_arr, weights=weights_arr, lmax=LMAX)

    results: dict = {
        "purpose": ("Mask pixel-count-threshold robustness sweep for the canonical-mask "
                    "+3.64σ ℓ=1 result. ChatGPT v1.0.122 MAJOR M3 closure."),
        "version": "v1.0.124-mask-threshold-sweep",
        "config": {"nside": NSIDE, "lmax": LMAX, "n_mc": N_MC, "seed": SEED, "thresholds": THRESHOLDS},
        "n_spirals_input": int(len(spirals)),
        "per_threshold": [],
    }

    rng = np.random.default_rng(SEED)

    for thr in THRESHOLDS:
        t_start = time.time()
        mask = (n_total > thr).astype(np.float64)
        f_sky = float(mask.mean())
        n_in_mask = int((n_total * mask).sum())
        n_pix_in = int(mask.sum())
        print(f"\n[{time.time()-t0:.1f}s] threshold n_total > {thr}: f_sky={f_sky:.5f}, "
              f"in-mask pixels={n_pix_in:,}, in-mask galaxies={n_in_mask:,}", flush=True)

        # Build CW-fraction map under this mask
        A = np.zeros(npix, dtype=np.float64)
        nz = mask.astype(bool)
        A[nz] = (n_cw_obs[nz] / np.maximum(n_total[nz], 1.0)) - 0.5
        A_gw = float((A[nz] * n_total[nz]).sum() / n_total[nz].sum())
        A_sub = A.copy()
        A_sub[nz] -= A_gw

        # MASTER coupling matrix for this mask
        dummy_map = np.zeros(npix, dtype=np.float64)
        f0_dummy = nmt.NmtField(mask, [dummy_map], lite=True)
        w = nmt.NmtWorkspace()
        w.compute_coupling_matrix(f0_dummy, f0_dummy, b_custom)
        print(f"[{time.time()-t0:.1f}s]   coupling matrix done ({time.time()-t_start:.1f}s)",
              flush=True)

        # Data-side decouple at this mask
        f0_data = nmt.NmtField(mask, [A_sub], lite=True)
        cl_coupled = nmt.compute_coupled_cell(f0_data, f0_data)
        cl_decoupled = w.decouple_cell(cl_coupled)
        C1_data = float(cl_decoupled[0][0])
        print(f"[{time.time()-t0:.1f}s]   data decoupled C_1 = {C1_data:.4e}", flush=True)

        # Per-pixel-shuffle null × N_MC
        C1_null = np.zeros(N_MC, dtype=np.float64)
        for k in range(N_MC):
            # Shuffle CW/CCW labels among the in-mask galaxies only
            iscw_shuf = rng.binomial(1, p_cw_global, size=len(iscw)).astype(np.bool_)
            n_cw_shuf = np.bincount(pix[iscw_shuf], minlength=npix).astype(np.float64)
            A_shuf = np.zeros(npix, dtype=np.float64)
            A_shuf[nz] = (n_cw_shuf[nz] / np.maximum(n_total[nz], 1.0)) - 0.5
            A_gw_shuf = float((A_shuf[nz] * n_total[nz]).sum() / n_total[nz].sum())
            A_shuf_sub = A_shuf.copy()
            A_shuf_sub[nz] -= A_gw_shuf
            f0_shuf = nmt.NmtField(mask, [A_shuf_sub], lite=True)
            cl_shuf = nmt.compute_coupled_cell(f0_shuf, f0_shuf)
            cl_d_shuf = w.decouple_cell(cl_shuf)
            C1_null[k] = float(cl_d_shuf[0][0])
            if (k+1) % 50 == 0:
                print(f"[{time.time()-t0:.1f}s]     null {k+1}/{N_MC}", flush=True)

        null_mean = float(np.mean(C1_null))
        null_std = float(np.std(C1_null, ddof=1))
        sigma = (C1_data - null_mean) / null_std if null_std > 0 else float("nan")
        emp_rank_p = 2 * float(np.minimum(
            (C1_null >= C1_data).mean(),
            (C1_null <= C1_data).mean()
        ))
        print(f"[{time.time()-t0:.1f}s]   sigma = {sigma:+.3f}, empirical p = {emp_rank_p:.3f} "
              f"(in {time.time()-t_start:.1f}s)", flush=True)

        results["per_threshold"].append({
            "threshold_min_n_total": thr,
            "f_sky": f_sky,
            "n_pix_in_mask": n_pix_in,
            "n_galaxies_in_mask": n_in_mask,
            "data_C1": C1_data,
            "null_mean": null_mean,
            "null_std": null_std,
            "sigma_from_null": sigma,
            "empirical_p_value": emp_rank_p,
        })

    OUT.write_text(json.dumps(results, indent=2))
    print(f"\n[{time.time()-t0:.1f}s] wrote {OUT.relative_to(REPO)}", flush=True)
    print("\nSUMMARY:")
    for r in results["per_threshold"]:
        print(f"  n>{r['threshold_min_n_total']:>3}  f_sky={r['f_sky']:.4f}  "
              f"σ={r['sigma_from_null']:+.2f}  p={r['empirical_p_value']:.3f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
