#!/usr/bin/env python3
"""
C9e — shot-noise estimate for the P4 A_p auto-spectrum (quick).

Analytic per-pixel binomial shot noise for the spiral-denominator chirality
field A_p = (N_CW - N_CCW)/N_spiral(p): with f the CW fraction, the binomial
variance of the estimated fraction is sigma_f^2(p) = f(1-f)/N_spiral(p);
since A_p = 2*f_hat - 1, the per-pixel A_p noise variance is
    sigma_A^2(p) = 4 * f(1-f) / N_spiral(p).
Both conventions are reported (N_ell for the A_p field is exactly 4x the
f_hat-field N_ell).

Propagation through the weighted pseudo-Cl / MASTER pipeline is implemented
via 100 pure-noise realizations: per-pixel independent Gaussian draws
g(p) ~ N(0, sigma_A(p)) on the field support, passed through the IDENTICAL
mask / weights / monopole-subtraction / MASTER chain as the +7.28 sigma
diagnostic channel (c3/c6 conventions: N_all>=1 mask, C2 2-deg apodization,
Wp = N_all, weight-map-weighted mask-mean subtraction, Table III banding).

Two f choices for sigma_A^2(p):
  primary:  f = global p_CW (stable in low-N pixels)
  variant:  f = per-pixel f_hat(p) (zero-variance in pure-CW/CCW pixels)

Run on pod:
  tmux new -s c9e -d 'cd /workspace && python3 c9e_p4_shot_noise.py 2>&1 | tee c9e.log'
Output: /workspace/c9e_results/c9e_shot_noise.json
"""
from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "2")
os.environ.setdefault("HF_HOME", "/workspace/.hf_home")

import json
import time
from pathlib import Path

import numpy as np
import pandas as pd
import healpy as hp
import pymaster as nmt

NSIDE = 64
LMAX = 3 * NSIDE - 1  # 191
N_REAL = 100
SEED = 42
APOD_DEG = 2.0
APOD_TYPE = "C2"
MASK_DEFINITION = "N_all >= 1"
REPORT_BANDS = [0, 1, 2, 3, 4, 5]
BAND_LABELS = ["ell=1 (single mode)", "ell in [2,6]", "ell in [7,11]",
               "ell in [12,16]", "ell in [17,21]", "ell in [22,26]"]
OUTDIR = Path(os.environ.get("C9E_OUTDIR", "/workspace/c9e_results"))
OUT = OUTDIR / "c9e_shot_noise.json"


def find_catalog() -> str:
    for c in ["/workspace/r42_b20/chirality_catalog/catalog_production.parquet",
              "/workspace/catalog_production.parquet"]:
        if os.path.exists(c):
            return c
    from huggingface_hub import hf_hub_download
    return hf_hub_download("bamfai/galaxy-chirality-catalog",
                           "catalog_production.parquet", repo_type="dataset")


def make_bins() -> nmt.NmtBin:
    """Table III banding: band 0 = ell=1; bands b>=1 = 5-wide from ell=2."""
    bpws = np.full(LMAX + 1, -1, dtype=np.int32)
    bpws[1] = 0
    for ell in range(2, LMAX + 1):
        bpws[ell] = 1 + (ell - 2) // 5
    return nmt.NmtBin(bpws=bpws, ells=np.arange(LMAX + 1, dtype=np.int32),
                      weights=np.ones(LMAX + 1), lmax=LMAX)


def main() -> int:
    t0 = time.time()
    OUTDIR.mkdir(parents=True, exist_ok=True)
    print(f"[{time.time()-t0:.1f}s] C9e shot-noise job starting", flush=True)

    cat_path = find_catalog()
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
    n_cw_pix = np.bincount(pix_all[is_cw], minlength=npix).astype(np.float64)
    p_cw_global = float(is_cw.sum() / is_spiral.sum())
    print(f"[{time.time()-t0:.1f}s] spirals: {int(is_spiral.sum()):,}  "
          f"p_CW_global={p_cw_global:.6f}", flush=True)

    mask_bool = n_all_pix >= 1
    mask_binary = mask_bool.astype(np.float64)
    print(f"[{time.time()-t0:.1f}s] mask {MASK_DEFINITION}: n_pix={int(mask_bool.sum())} "
          f"f_sky={mask_binary.mean():.5f}", flush=True)
    mask_apod = nmt.mask_apodization(mask_binary, APOD_DEG, apotype=APOD_TYPE)
    W_nall = n_all_pix * mask_binary
    W_eff = W_nall * mask_apod

    nz = n_spiral_pix > 0
    wsel = mask_bool & nz
    n_support = int(wsel.sum())
    print(f"[{time.time()-t0:.1f}s] field support (mask & N_spiral>0): "
          f"{n_support} pixels", flush=True)

    # Per-pixel A_p shot-noise std on the field support
    f_hat = np.zeros(npix)
    f_hat[nz] = n_cw_pix[nz] / n_spiral_pix[nz]
    sigma_A = {}
    var_global = np.zeros(npix)
    var_global[wsel] = 4.0 * p_cw_global * (1.0 - p_cw_global) / n_spiral_pix[wsel]
    sigma_A["f_global"] = np.sqrt(var_global)
    var_pix = np.zeros(npix)
    var_pix[wsel] = 4.0 * f_hat[wsel] * (1.0 - f_hat[wsel]) / n_spiral_pix[wsel]
    sigma_A["f_per_pixel"] = np.sqrt(var_pix)
    for k, v in sigma_A.items():
        print(f"[{time.time()-t0:.1f}s] sigma_A[{k}]: support mean="
              f"{v[wsel].mean():.5f} max={v[wsel].max():.5f}", flush=True)

    b = make_bins()
    eff = b.get_effective_ells()
    n_bands = b.get_n_bands()
    print(f"[{time.time()-t0:.1f}s] coupling matrix ({n_bands} bands) ...", flush=True)
    f_dummy = nmt.NmtField(W_eff, [np.zeros(npix)], lite=True)
    w = nmt.NmtWorkspace()
    w.compute_coupling_matrix(f_dummy, f_dummy, b)

    results = {}
    rng = np.random.default_rng(SEED)
    for variant, sig in sigma_A.items():
        tv = time.time()
        print(f"\n[{time.time()-t0:.1f}s] === {variant}: {N_REAL} pure-noise "
              f"realizations ...", flush=True)
        cls = np.zeros((N_REAL, n_bands))
        for k in range(N_REAL):
            g = np.zeros(npix)
            g[wsel] = rng.normal(0.0, sig[wsel])
            # identical monopole treatment as the data vector (gw mask-mean sub)
            g_gw = float((g[wsel] * W_nall[wsel]).sum() / W_nall[wsel].sum())
            g_sub = np.zeros(npix)
            g_sub[wsel] = g[wsel] - g_gw
            f_n = nmt.NmtField(W_eff, [g_sub], lite=True)
            cls[k] = w.decouple_cell(nmt.compute_coupled_cell(f_n, f_n))[0]
            if (k + 1) % 20 == 0:
                print(f"[{time.time()-t0:.1f}s]  {variant} {k+1}/{N_REAL} "
                      f"l1 mean={cls[:k+1, 0].mean():.4e}", flush=True)
        bands = {}
        for bi in REPORT_BANDS:
            bands[f"band_{bi}"] = {
                "label": BAND_LABELS[bi],
                "ell_eff": float(eff[bi]),
                "N_ell_Ap_field": float(cls[:, bi].mean()),
                "N_ell_Ap_field_std": float(cls[:, bi].std(ddof=1)),
                "N_ell_fcw_field": float(cls[:, bi].mean() / 4.0),
            }
        results[variant] = {
            "bands": bands,
            "N_ell_all_bands_Ap": cls.mean(axis=0).tolist(),
            "wallclock_s": time.time() - tv,
        }
        print(f"[{time.time()-t0:.1f}s] {variant} N_l1(A_p) = "
              f"{bands['band_0']['N_ell_Ap_field']:.4e} +/- "
              f"{bands['band_0']['N_ell_Ap_field_std']:.4e}", flush=True)

    out = {
        "job": "C9e-P4-Ap-shot-noise",
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "purpose": ("Analytic per-pixel binomial shot noise N_ell for the "
                    "spiral-denominator A_p field, propagated through the "
                    "apodized-footprint Wp=N_all MASTER pipeline via 100 "
                    "pure-noise Gaussian realizations."),
        "config": {
            "nside": NSIDE, "lmax": LMAX, "n_realizations": N_REAL, "seed": SEED,
            "apodization": f"{APOD_TYPE} {APOD_DEG} deg",
            "mask_definition": MASK_DEFINITION,
            "weights": "Wp = N_all (x apodized mask)",
            "binning": "Table III bands (band 0 = ell=1; 5-wide from ell=2)",
            "effective_ells_report_bands": [float(eff[i]) for i in REPORT_BANDS],
            "noise_model": ("per-pixel independent Gaussian g(p)~N(0, sigma_A(p)); "
                            "sigma_f^2 = f(1-f)/N_spiral(p) for the CW fraction, "
                            "sigma_A^2 = 4 f(1-f)/N_spiral(p) for A_p = 2f-1; "
                            "same gw mask-mean subtraction as the data vector"),
            "f_choices": {"f_global": p_cw_global,
                          "f_per_pixel": "f_hat(p) = N_CW(p)/N_spiral(p)"},
            "field_support_n_pix": n_support,
        },
        "results": results,
        "reference": {
            "c3_data_C1_decoupled_Wp_Nall": 2.348e-05,
            "c3_null_mean_l1": 1.713e-06,
            "c3_null_std_l1": 2.989e-06,
            "note": ("Compare N_l1(A_p) against the c3 label-shuffle null mean: "
                     "the shuffle null IS the empirical shot-noise floor of this "
                     "channel, so agreement validates the analytic model."),
        },
        "wallclock_s": time.time() - t0,
    }
    OUT.write_text(json.dumps(out, indent=2))
    print(f"\n=== C9e RESULTS ===", flush=True)
    for variant, r in results.items():
        b0 = r["bands"]["band_0"]
        print(f"  {variant}: N_l1(A_p)={b0['N_ell_Ap_field']:.4e} "
              f"(c3 shuffle-null mean 1.713e-06)", flush=True)
    print(f"wrote {OUT}  ({time.time()-t0:.0f}s)", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
