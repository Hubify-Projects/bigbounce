#!/usr/bin/env python3
"""
C9c — W_p weight-map sweep for the P4 apodized-footprint MASTER ell=1
diagnostic: recompute the ell=1 channel with W_p in {N_all, N_spiral,
uniform (binary mask)}, each against its own 500-MC per-galaxy
label-shuffle null.

Conventions copied verbatim from c3_p4_wp_invariance_fsky.py /
c6_p4_depth_stratified_null.py: mask N_all >= 1 (NSIDE=64), C2 2-deg
apodization, A_p = (N_CW - N_CCW)/N_spiral with weight-map-weighted
mask-mean subtraction (weights = the variant's W_p), custom single-ell
NmtBin including ell=1, lite NmtFields, seed 42. The only new variant is
W_p = uniform binary (W = mask), which weights the mean subtraction and the
NaMaster weight map uniformly across the footprint.

Parallel deviation from the serial c3/c6 RNG stream: each realization k uses
an independent deterministic stream np.random.default_rng([SEED, vi, k]).

Run on pod:
  tmux new -s c9c -d 'cd /workspace && C9_NPROC=2 python3 c9c_p4_wp_sweep.py 2>&1 | tee c9c.log'
Output: /workspace/c9_results/c9c_wp_sweep.json
"""
from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("HF_HOME", "/workspace/.hf_home")

import json
import time
from multiprocessing import get_context
from pathlib import Path

import numpy as np
import pandas as pd
import healpy as hp
import pymaster as nmt

NSIDE = 64
LMAX = 3 * NSIDE - 1  # 191
N_MC = 500
SEED = 42
APOD_DEG = 2.0
APOD_TYPE = "C2"
MASK_DEFINITION = "N_all >= 1"
C3_REFERENCE_SIGMA = {"Wp_Nall": 7.28, "Wp_Nspiral": 9.78}  # global-shuffle null
NPROC = int(os.environ.get("C9_NPROC", max(1, (os.cpu_count() or 2) - 1)))
OUTDIR = Path(os.environ.get("C9_OUTDIR", "/workspace/c9_results"))
OUT = OUTDIR / "c9c_wp_sweep.json"
WS_DIR = Path("/workspace/c9_tmp")

G: dict = {}
_W: dict = {}


def find_catalog() -> str:
    for c in ["/workspace/r42_b20/chirality_catalog/catalog_production.parquet",
              "/workspace/catalog_production.parquet"]:
        if os.path.exists(c):
            return c
    from huggingface_hub import hf_hub_download
    return hf_hub_download("bamfai/galaxy-chirality-catalog",
                           "catalog_production.parquet", repo_type="dataset")


def build_A_sub(labels: np.ndarray, vi: int) -> np.ndarray:
    """A_p = (N_CW - N_CCW)/N_spiral with weight-map-weighted mask-mean
    subtraction (galaxy-weighted convention, weights = the variant's W_p) —
    copied from c6 build_A_sub."""
    npix = G["npix"]
    n_cw = np.bincount(G["pix_sp"][labels == 1], minlength=npix).astype(np.float64)
    n_ccw = np.bincount(G["pix_sp"][labels == 0], minlength=npix).astype(np.float64)
    nz = G["nz"]
    A = np.zeros(npix)
    A[nz] = (n_cw[nz] - n_ccw[nz]) / G["n_spiral_pix"][nz]
    wsel = G["wsel"]
    W = G["W_list"][vi]
    A_gw = float((A[wsel] * W[wsel]).sum() / W[wsel].sum())
    A_sub = np.zeros(npix)
    A_sub[wsel] = A[wsel] - A_gw
    return A_sub


def _init_worker(ws_path: str) -> None:
    w = nmt.NmtWorkspace()
    w.read_from(ws_path)
    _W["w"] = w


def _null_one(args):
    vi, k = args
    rng = np.random.default_rng([SEED, vi, k])
    labels_perm = G["labels_cw"][rng.permutation(G["n_sp"])]
    A = build_A_sub(labels_perm, vi)
    f = nmt.NmtField(G["Weff_list"][vi], [A], lite=True)
    c1 = float(_W["w"].decouple_cell(nmt.compute_coupled_cell(f, f))[0][0])
    return k, c1


def main() -> int:
    t0 = time.time()
    OUTDIR.mkdir(parents=True, exist_ok=True)
    WS_DIR.mkdir(parents=True, exist_ok=True)
    print(f"[{time.time()-t0:.1f}s] C9c Wp sweep job starting  NPROC={NPROC}", flush=True)

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
    pix_sp = pix_all[is_spiral]
    labels_cw = is_cw[is_spiral].astype(np.int8)
    n_sp = len(labels_cw)
    print(f"[{time.time()-t0:.1f}s] spirals: {n_sp:,}  p_CW={labels_cw.mean():.6f}", flush=True)

    mask_bool = n_all_pix >= 1
    mask_binary = mask_bool.astype(np.float64)
    print(f"[{time.time()-t0:.1f}s] mask {MASK_DEFINITION}: n_pix={int(mask_bool.sum())} "
          f"f_sky={mask_binary.mean():.5f}", flush=True)
    mask_apod = nmt.mask_apodization(mask_binary, APOD_DEG, apotype=APOD_TYPE)

    W_list = [n_all_pix * mask_binary,        # Wp_Nall
              n_spiral_pix * mask_binary,     # Wp_Nspiral
              mask_binary]                    # Wp_uniform_binary
    Weff_list = [W * mask_apod for W in W_list]
    names = ["Wp_Nall", "Wp_Nspiral", "Wp_uniform_binary"]

    nz = n_spiral_pix > 0
    G.update({
        "npix": npix, "pix_sp": pix_sp, "labels_cw": labels_cw, "n_sp": n_sp,
        "n_spiral_pix": n_spiral_pix, "nz": nz, "wsel": mask_bool & nz,
        "W_list": W_list, "Weff_list": Weff_list,
    })

    # Custom NmtBin including ell=1 (single-ell bandpowers), identical to C3/C6
    bpws = np.full(LMAX + 1, -1, dtype=np.int32)
    for ell in range(1, LMAX + 1):
        bpws[ell] = ell - 1
    b_custom = nmt.NmtBin(bpws=bpws, ells=np.arange(LMAX + 1, dtype=np.int32),
                          weights=np.ones(LMAX + 1), lmax=LMAX)

    variants = {}
    ctx = get_context("fork")
    for vi, name in enumerate(names):
        tv = time.time()
        W_eff = Weff_list[vi]
        fsky_eff = float(W_eff.mean() ** 2 / (W_eff ** 2).mean())
        print(f"\n[{time.time()-t0:.1f}s] === variant {name}: coupling matrix ... "
              f"(fsky_eff={fsky_eff:.4f})", flush=True)
        f_dummy = nmt.NmtField(W_eff, [np.zeros(npix)], lite=True)
        w = nmt.NmtWorkspace()
        w.compute_coupling_matrix(f_dummy, f_dummy, b_custom)
        ws_path = str(WS_DIR / f"c9c_ws_{name}.fits")
        if os.path.exists(ws_path):
            os.remove(ws_path)
        w.write_to(ws_path)

        A_data = build_A_sub(labels_cw, vi)
        f_data = nmt.NmtField(W_eff, [A_data], lite=True)
        C1_data = float(w.decouple_cell(nmt.compute_coupled_cell(f_data, f_data))[0][0])
        print(f"[{time.time()-t0:.1f}s] {name} data decoupled C1 = {C1_data:.4e}", flush=True)

        C1_null = np.zeros(N_MC)
        done = 0
        with ctx.Pool(NPROC, initializer=_init_worker, initargs=(ws_path,)) as pool:
            for k, c1 in pool.imap_unordered(
                    _null_one, [(vi, k) for k in range(N_MC)], chunksize=8):
                C1_null[k] = c1
                done += 1
                if done % 50 == 0:
                    el = time.time() - tv
                    eta = el / done * (N_MC - done)
                    print(f"[{time.time()-t0:.1f}s]  {name} null {done}/{N_MC} "
                          f"mean={C1_null[C1_null != 0].mean():.4e} ETA {eta:.0f}s",
                          flush=True)

        m, s = float(C1_null.mean()), float(C1_null.std(ddof=1))
        sigma = (C1_data - m) / s
        n_exceed = int((C1_null >= C1_data).sum())
        variants[name] = {
            "C1_data_decoupled": C1_data,
            "null_mean": m, "null_std": s,
            "sigma": sigma,
            "n_exceed_null": n_exceed,
            "empirical_rank_p_one_sided": (1 + n_exceed) / (N_MC + 1),
            "empirical_rank_p_two_sided": 2.0 * min(n_exceed, N_MC - n_exceed) / N_MC,
            "n_mc": N_MC,
            "fsky_eff_apodized": fsky_eff,
            "c3_global_shuffle_sigma_reference": C3_REFERENCE_SIGMA.get(name),
            "wallclock_s": time.time() - tv,
        }
        print(f"[{time.time()-t0:.1f}s] {name} sigma = {sigma:+.4f} "
              f"(c3 ref {C3_REFERENCE_SIGMA.get(name)}) "
              f"p1s={variants[name]['empirical_rank_p_one_sided']:.4f}", flush=True)

    out = {
        "job": "C9c-P4-Wp-sweep",
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "purpose": ("W_p weight-map sweep for the apodized-footprint MASTER ell=1 "
                    "diagnostic: Wp in {N_all, N_spiral, uniform binary}, each with "
                    "its own 500-MC per-galaxy label-shuffle null. Tests whether the "
                    "+7.28/+9.78 sigma excess persists under uniform weighting."),
        "config": {
            "nside": NSIDE, "lmax": LMAX, "n_mc": N_MC, "seed": SEED,
            "apodization": f"{APOD_TYPE} {APOD_DEG} deg",
            "mask_definition": MASK_DEFINITION,
            "field": ("A_p=(N_CW-N_CCW)/N_spiral, weight-map-weighted mask-mean "
                      "subtracted (weights = variant W_p; c3/c6 convention)"),
            "null": ("per-galaxy CW/CCW label permutation, pool = spirals only; "
                     "independent stream per realization "
                     "np.random.default_rng([42, variant_idx, k])"),
            "n_spirals": n_sp,
            "nproc": NPROC,
        },
        "results": variants,
        "c3_reference": {"null": "global per-galaxy label shuffle (serial stream)",
                         "sigma": C3_REFERENCE_SIGMA},
        "wallclock_s": time.time() - t0,
    }
    OUT.write_text(json.dumps(out, indent=2))
    print(f"\n=== C9c RESULTS ===", flush=True)
    for name, v in variants.items():
        print(f"  {name}: sigma = {v['sigma']:+.4f} "
              f"p1s={v['empirical_rank_p_one_sided']:.4f}", flush=True)
    print(f"wrote {OUT}  ({time.time()-t0:.0f}s)", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
