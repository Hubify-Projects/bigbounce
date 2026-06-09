#!/usr/bin/env python3
"""
C3 — P4 weight-map (W_p) invariance test + effective-f_sky accounting for the
headline subsample-mask MASTER ell=1 measurement.

The published headline (chirality_catalog_paper.tex Appendix A) is the
MASTER-deconvolved single-mode pseudo-C1 on the strict-superset subsample
mask (n_weighted=5,547,858, f_sky=0.659), weight map W_p = N_all(p)
(CW+CCW+NOT_SPIRAL per-pixel count), C^2 2-deg apodization, field
A_p = (N_CW - N_CCW)/N_spiral(p) with galaxy-weighted mask-mean
subtraction, 500-MC label-shuffle null, seed 42 -> -0.122 sigma.

This job reruns that measurement twice:
  (a) W_p = N_all(p)     [published convention]
  (b) W_p = N_spiral(p)  [invariance check]
and reports, for the subsample mask:
  - raw pixel f_sky (binary mask mean)
  - f_sky_eff = <W>^2 / <W^2> for the apodized and unapodized weight maps,
    for both W_p choices.

Mask reconstruction note: the original -0.122 sigma run was a pod artifact
(pod2 2026-04-29; 32,384 unmasked pixels / f_sky=0.6589 on an n=5,547,858
analysis subsample). The exact subsample is not in the repo, so the mask is
reconstructed from the production catalog as the candidate threshold mask
(pixels with N_all(p) >= k, k swept over 1..50; and N_spiral(p) >= 1)
whose pixel count is closest to the published 32,384. All candidates are
recorded in the output JSON for full disclosure.

Run on pod:
  tmux new -s c3 -d 'cd /workspace && python3 c3_p4_wp_invariance_fsky.py 2>&1 | tee c3.log'
Output: /workspace/c3_results/c3_wp_invariance_fsky.json
ETA: ~1-3 h CPU (2 x (1+500) NaMaster decouples at NSIDE=64).
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
APOD_DEG = 2.0
APOD_TYPE = "C2"
PUBLISHED_NPIX = 32384      # pod2 subsample mask pixel count
PUBLISHED_FSKY = 0.6588541666666666
PUBLISHED_SIGMA_NALL = -0.12189879362126763
OUTDIR = Path(os.environ.get("C3_OUTDIR", "/workspace/c3_results"))
OUT = OUTDIR / "c3_wp_invariance_fsky.json"


def fsky_eff(wmap: np.ndarray) -> float:
    """Effective sky fraction <W>^2/<W^2> over the full sphere."""
    mw = float(np.mean(wmap))
    mw2 = float(np.mean(wmap ** 2))
    return mw * mw / mw2 if mw2 > 0 else 0.0


def main() -> int:
    t0 = time.time()
    OUTDIR.mkdir(parents=True, exist_ok=True)
    print(f"[{time.time()-t0:.1f}s] C3 Wp-invariance + fsky_eff job starting", flush=True)

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

    # ---------- Subsample-mask reconstruction ----------
    candidates = []
    for k in [1, 2, 3, 5, 10, 20, 50]:
        m = n_all_pix >= k
        candidates.append({"definition": f"N_all >= {k}", "n_pix": int(m.sum()),
                           "f_sky": float(m.mean())})
    m_sp1 = n_spiral_pix >= 1
    candidates.append({"definition": "N_spiral >= 1", "n_pix": int(m_sp1.sum()),
                       "f_sky": float(m_sp1.mean())})
    best = min(candidates, key=lambda c: abs(c["n_pix"] - PUBLISHED_NPIX))
    print(f"[{time.time()-t0:.1f}s] mask candidates:", flush=True)
    for c in candidates:
        tag = "  <-- selected" if c is best else ""
        print(f"   {c['definition']:>14}: n_pix={c['n_pix']:>6} f_sky={c['f_sky']:.5f}{tag}", flush=True)

    if best["definition"].startswith("N_all"):
        kk = int(best["definition"].split(">=")[1])
        mask_bool = n_all_pix >= kk
    else:
        mask_bool = m_sp1
    mask_binary = mask_bool.astype(np.float64)
    fsky_raw = float(mask_binary.mean())

    # C^2 2-deg apodization of the binary subsample mask
    print(f"[{time.time()-t0:.1f}s] apodizing mask ({APOD_TYPE}, {APOD_DEG} deg) ...", flush=True)
    mask_apod = nmt.mask_apodization(mask_binary, APOD_DEG, apotype=APOD_TYPE)

    # ---------- fsky accounting ----------
    W_nall = n_all_pix * mask_binary
    W_nsp = n_spiral_pix * mask_binary
    fsky_numbers = {
        "raw_pixel_fsky_binary_mask": fsky_raw,
        "fsky_binary_mask_apodized_mean": float(mask_apod.mean()),
        "fsky_eff_Wp_Nall_unapodized": fsky_eff(W_nall),
        "fsky_eff_Wp_Nall_apodized": fsky_eff(W_nall * mask_apod),
        "fsky_eff_Wp_Nspiral_unapodized": fsky_eff(W_nsp),
        "fsky_eff_Wp_Nspiral_apodized": fsky_eff(W_nsp * mask_apod),
        "fsky_eff_binary_unapodized": fsky_eff(mask_binary),
        "fsky_eff_binary_apodized": fsky_eff(mask_apod),
        "sum_Wp_Nall_in_mask": float(W_nall.sum()),
        "sum_Wp_Nspiral_in_mask": float(W_nsp.sum()),
        "published_n_weighted": 5547858,
    }
    for k, v in fsky_numbers.items():
        print(f"   {k}: {v:.6g}", flush=True)

    # ---------- Field construction helpers ----------
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

    # Custom NmtBin including ell=1 (single-ell bandpowers)
    bpws = np.full(LMAX + 1, -1, dtype=np.int32)
    for ell in range(1, LMAX + 1):
        bpws[ell] = ell - 1
    b_custom = nmt.NmtBin(bpws=bpws, ells=np.arange(LMAX + 1, dtype=np.int32),
                          weights=np.ones(LMAX + 1), lmax=LMAX)

    variants = {}
    rng_master = np.random.default_rng(SEED)
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

        # 500-MC per-galaxy label-shuffle null (permutation; preserves global CW count)
        rng = np.random.default_rng(SEED)  # same seed per variant for paired comparison
        labels_perm = labels_cw.copy()
        C1_null = np.zeros(N_MC)
        for k in range(N_MC):
            rng.shuffle(labels_perm)
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
        variants[name] = {
            "C1_data_decoupled": C1_data,
            "null_mean": m, "null_std": s,
            "sigma": sigma,
            "n_mc": N_MC,
            "wallclock_s": time.time() - tv,
        }
        print(f"[{time.time()-t0:.1f}s] {name} sigma = {sigma:+.4f}", flush=True)

    result = {
        "job": "C3-P4-Wp-invariance-and-fsky-eff",
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "purpose": ("Headline subsample-mask MASTER ell=1 rerun under both weight-map "
                    "choices Wp=N_all (published, -0.122 sigma) and Wp=N_spiral, plus "
                    "raw and effective f_sky accounting for the apodized and "
                    "unapodized weight maps."),
        "config": {
            "nside": NSIDE, "lmax": LMAX, "n_mc": N_MC, "seed": SEED,
            "apodization": f"{APOD_TYPE} {APOD_DEG} deg",
            "mask_definition_selected": best["definition"],
            "mask_n_pix": best["n_pix"],
            "published_mask_n_pix": PUBLISHED_NPIX,
            "published_fsky": PUBLISHED_FSKY,
            "mask_candidates": candidates,
            "null": "per-galaxy CW-label permutation shuffle (500 MC, seed 42)",
            "field": "A_p=(N_CW-N_CCW)/N_spiral, weight-map-weighted mask-mean subtracted",
        },
        "fsky_numbers": fsky_numbers,
        "results": variants,
        "published_reference": {"sigma_Wp_Nall": PUBLISHED_SIGMA_NALL},
        "wallclock_s": time.time() - t0,
    }
    OUT.write_text(json.dumps(result, indent=2))
    print(f"\n=== C3 RESULTS ===", flush=True)
    for name, v in variants.items():
        print(f"  {name}: sigma = {v['sigma']:+.4f}", flush=True)
    print(f"  raw pixel fsky = {fsky_raw:.5f} (published {PUBLISHED_FSKY:.5f})", flush=True)
    print(f"wrote {OUT}  ({time.time()-t0:.0f}s)", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
