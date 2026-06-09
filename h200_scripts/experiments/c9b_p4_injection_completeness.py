#!/usr/bin/env python3
"""
C9b — injection-recovery completeness through the apodized-footprint MASTER
ell=1 diagnostic channel (the +7.28 sigma channel).

Channel conventions copied verbatim from c3_p4_wp_invariance_fsky.py /
c6_p4_depth_stratified_null.py: mask N_all >= 1 (NSIDE=64), C2 2-deg
apodization, weights Wp = N_all, A_p = (N_CW - N_CCW)/N_spiral with
weight-map-weighted mask-mean subtraction, custom single-ell NmtBin
including ell=1, lite NmtFields, seed 42.

Injection model copied from the repo's established convention
(pipelines/p2_chirality/scripts/full_catalog_injection_recovery.py):
per-pixel additive A_p dipole on a label-shuffle background,
    A_p^inj(p) = A_p^shuffle(p) + A * (hat_d . hat_n(p)),
applied on the field support BEFORE the weight-map-weighted mask-mean
subtraction (pipeline order: monopole subtraction is the last data-vector
construction step). A is the A_p-field dipole amplitude, i.e. an f_CW
modulation of amplitude A/2 (A_p = 2 f_CW - 1).

Amplitudes: A in {0.005, 0.0075, 0.017, 0.03}.
Axes: fixed fiducial z-hat (equatorial Dec=+90) + x-hat (RA=0,Dec=0) +
y-hat (RA=90,Dec=0); per-axis and 3-axis-averaged completeness reported.
N_inj = 1000 label-shuffle backgrounds per (amplitude, axis).
Detection: sigma = (C1_inj - null_mean)/null_std against a 500-MC
per-galaxy label-shuffle null (same channel, same script);
P(detect) at sigma >= 3 and sigma >= 5.

Run on pod:
  tmux new -s c9b -d 'cd /workspace && C9_NPROC=4 python3 c9b_p4_injection_completeness.py 2>&1 | tee c9b.log'
Output: /workspace/c9_results/c9b_injection_completeness.json
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
SEED = 42
APOD_DEG = 2.0
APOD_TYPE = "C2"
MASK_DEFINITION = "N_all >= 1"
AMPLITUDES = [0.005, 0.0075, 0.017, 0.03]
AXES = {"z_fiducial": np.array([0.0, 0.0, 1.0]),
        "x": np.array([1.0, 0.0, 0.0]),
        "y": np.array([0.0, 1.0, 0.0])}
N_INJ = 1000
N_NULL = 500
NPROC = int(os.environ.get("C9_NPROC", max(1, (os.cpu_count() or 2) - 1)))
OUTDIR = Path(os.environ.get("C9_OUTDIR", "/workspace/c9_results"))
OUT = OUTDIR / "c9b_injection_completeness.json"
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


def build_A_sub(labels: np.ndarray, A_inj: float, axis: np.ndarray | None) -> np.ndarray:
    """c6 build_A_sub (W = W_nall) + optional additive dipole injection
    applied on the field support before the mask-mean subtraction."""
    npix = G["npix"]
    n_cw = np.bincount(G["pix_sp"][labels == 1], minlength=npix).astype(np.float64)
    n_ccw = np.bincount(G["pix_sp"][labels == 0], minlength=npix).astype(np.float64)
    nz = G["nz"]
    A = np.zeros(npix)
    A[nz] = (n_cw[nz] - n_ccw[nz]) / G["n_spiral_pix"][nz]
    wsel = G["wsel"]
    if A_inj != 0.0 and axis is not None:
        A[wsel] += A_inj * (G["n_hat"][:, wsel].T @ axis)
    W = G["W_nall"]
    A_gw = float((A[wsel] * W[wsel]).sum() / W[wsel].sum())
    A_sub = np.zeros(npix)
    A_sub[wsel] = A[wsel] - A_gw
    return A_sub


def _init_worker(ws_path: str) -> None:
    w = nmt.NmtWorkspace()
    w.read_from(ws_path)
    _W["w"] = w


def _one(args):
    """One realization: (tag, k, A_inj, axis_idx). tag 0 = null, 1 = injection."""
    tag, k, A_inj, axis_idx = args
    # axis_idx + 1 keeps all seed-sequence entries non-negative (null uses -1)
    rng = np.random.default_rng([SEED, tag, axis_idx + 1, k])
    labels_perm = G["labels_cw"][rng.permutation(G["n_sp"])]
    axis = G["axis_list"][axis_idx] if axis_idx >= 0 else None
    A = build_A_sub(labels_perm, A_inj, axis)
    f = nmt.NmtField(G["W_eff"], [A], lite=True)
    c1 = float(_W["w"].decouple_cell(nmt.compute_coupled_cell(f, f))[0][0])
    return k, c1


def run_batch(pool, jobs, label, t0):
    out = np.zeros(len(jobs))
    done = 0
    tb = time.time()
    for k, c1 in pool.imap_unordered(_one, jobs, chunksize=8):
        out[k] = c1
        done += 1
        if done % 100 == 0:
            el = time.time() - tb
            eta = el / done * (len(jobs) - done)
            print(f"[{time.time()-t0:.1f}s]  {label} {done}/{len(jobs)} "
                  f"mean={out[out != 0].mean():.4e} ETA {eta:.0f}s", flush=True)
    return out


def main() -> int:
    t0 = time.time()
    OUTDIR.mkdir(parents=True, exist_ok=True)
    WS_DIR.mkdir(parents=True, exist_ok=True)
    print(f"[{time.time()-t0:.1f}s] C9b injection-completeness job starting  "
          f"NPROC={NPROC}", flush=True)

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
    W_nall = n_all_pix * mask_binary
    W_eff = W_nall * mask_apod

    theta_pix, phi_pix = hp.pix2ang(NSIDE, np.arange(npix))
    n_hat = np.stack([np.sin(theta_pix) * np.cos(phi_pix),
                      np.sin(theta_pix) * np.sin(phi_pix),
                      np.cos(theta_pix)], axis=0)  # (3, npix), equatorial

    nz = n_spiral_pix > 0
    G.update({
        "npix": npix, "pix_sp": pix_sp, "labels_cw": labels_cw, "n_sp": n_sp,
        "n_spiral_pix": n_spiral_pix, "nz": nz, "wsel": mask_bool & nz,
        "W_nall": W_nall, "W_eff": W_eff, "n_hat": n_hat,
        "axis_list": list(AXES.values()),
    })
    axis_names = list(AXES.keys())

    # Custom NmtBin including ell=1 (single-ell bandpowers), identical to C3/C6
    bpws = np.full(LMAX + 1, -1, dtype=np.int32)
    for ell in range(1, LMAX + 1):
        bpws[ell] = ell - 1
    b_custom = nmt.NmtBin(bpws=bpws, ells=np.arange(LMAX + 1, dtype=np.int32),
                          weights=np.ones(LMAX + 1), lmax=LMAX)

    print(f"[{time.time()-t0:.1f}s] coupling matrix ...", flush=True)
    f_dummy = nmt.NmtField(W_eff, [np.zeros(npix)], lite=True)
    w = nmt.NmtWorkspace()
    w.compute_coupling_matrix(f_dummy, f_dummy, b_custom)
    ws_path = str(WS_DIR / "c9b_ws.fits")
    if os.path.exists(ws_path):
        os.remove(ws_path)
    w.write_to(ws_path)

    A_data = build_A_sub(labels_cw, 0.0, None)
    f_data = nmt.NmtField(W_eff, [A_data], lite=True)
    C1_data = float(w.decouple_cell(nmt.compute_coupled_cell(f_data, f_data))[0][0])
    print(f"[{time.time()-t0:.1f}s] data decoupled C1 = {C1_data:.4e} "
          f"(c3 reference 2.348e-05)", flush=True)

    ctx = get_context("fork")
    with ctx.Pool(NPROC, initializer=_init_worker, initargs=(ws_path,)) as pool:
        # ---- 500-MC label-shuffle null (detection reference) ----
        print(f"\n[{time.time()-t0:.1f}s] === null: {N_NULL} label-shuffle MC ...", flush=True)
        null_c1 = run_batch(pool, [(0, k, 0.0, -1) for k in range(N_NULL)], "null", t0)
        null_mean = float(null_c1.mean())
        null_std = float(null_c1.std(ddof=1))
        sigma_data = (C1_data - null_mean) / null_std
        print(f"[{time.time()-t0:.1f}s] null mean={null_mean:.4e} std={null_std:.4e} "
              f"data sigma={sigma_data:+.3f} (c3 ref +7.28)", flush=True)

        # ---- injections ----
        completeness = {}
        for ai, A_inj in enumerate(AMPLITUDES):
            per_axis = {}
            for xi, ax_name in enumerate(axis_names):
                label = f"A={A_inj} axis={ax_name}"
                print(f"\n[{time.time()-t0:.1f}s] === inject {label}: {N_INJ} MC ...", flush=True)
                # tag encodes (1 + amplitude index) so every (amp, axis, k)
                # has an independent deterministic stream
                jobs = [(1 + ai, k, A_inj, xi) for k in range(N_INJ)]
                c1_inj = run_batch(pool, jobs, label, t0)
                sigmas = (c1_inj - null_mean) / null_std
                per_axis[ax_name] = {
                    "n_inj": N_INJ,
                    "p_detect_3sigma": float((sigmas >= 3.0).mean()),
                    "p_detect_5sigma": float((sigmas >= 5.0).mean()),
                    "sigma_median": float(np.median(sigmas)),
                    "sigma_p16": float(np.percentile(sigmas, 16)),
                    "sigma_p84": float(np.percentile(sigmas, 84)),
                    "C1_inj_mean": float(c1_inj.mean()),
                }
                print(f"[{time.time()-t0:.1f}s] {label}: P(>=3sig)="
                      f"{per_axis[ax_name]['p_detect_3sigma']:.3f} P(>=5sig)="
                      f"{per_axis[ax_name]['p_detect_5sigma']:.3f} "
                      f"median sigma={per_axis[ax_name]['sigma_median']:+.2f}", flush=True)
            completeness[f"A_{A_inj}"] = {
                "amplitude_Ap": A_inj,
                "amplitude_fcw_modulation": A_inj / 2.0,
                "per_axis": per_axis,
                "axis_averaged": {
                    "p_detect_3sigma": float(np.mean(
                        [per_axis[a]["p_detect_3sigma"] for a in axis_names])),
                    "p_detect_5sigma": float(np.mean(
                        [per_axis[a]["p_detect_5sigma"] for a in axis_names])),
                    "sigma_median": float(np.mean(
                        [per_axis[a]["sigma_median"] for a in axis_names])),
                },
            }

    out = {
        "job": "C9b-P4-injection-recovery-completeness",
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "purpose": ("Injection-recovery completeness through the apodized-footprint "
                    "MASTER ell=1 diagnostic channel: P(detect at >=3sigma and "
                    ">=5sigma | A) for A_p dipole amplitudes A injected on "
                    "label-shuffle backgrounds."),
        "config": {
            "nside": NSIDE, "lmax": LMAX, "seed": SEED,
            "apodization": f"{APOD_TYPE} {APOD_DEG} deg",
            "mask_definition": MASK_DEFINITION,
            "weights": "Wp = N_all (x apodized mask)",
            "field": ("A_p=(N_CW-N_CCW)/N_spiral, weight-map-weighted mask-mean "
                      "subtracted (c3/c6 convention)"),
            "injection": ("per-pixel additive A_p dipole on label-shuffle background "
                          "(full_catalog_injection_recovery.py convention): "
                          "A_p^inj = A_p^shuffle + A*(d_hat . n_hat), applied before "
                          "mask-mean subtraction; A = A_p amplitude = 2 x f_CW "
                          "modulation amplitude"),
            "amplitudes_Ap": AMPLITUDES,
            "axes_equatorial_cartesian": {k: v.tolist() for k, v in AXES.items()},
            "fiducial_axis": "z_fiducial",
            "n_inj_per_amp_axis": N_INJ,
            "n_null": N_NULL,
            "rng": "np.random.default_rng([42, tag, axis_idx, k]) per realization",
            "nproc": NPROC,
        },
        "null": {
            "C1_data_decoupled": C1_data,
            "null_mean": null_mean, "null_std": null_std,
            "sigma_data": sigma_data,
            "c3_reference_sigma": 7.28,
        },
        "completeness": completeness,
        "wallclock_s": time.time() - t0,
    }
    OUT.write_text(json.dumps(out, indent=2))
    print(f"\n=== C9b RESULTS ===", flush=True)
    for amp_key, r in completeness.items():
        aa = r["axis_averaged"]
        print(f"  {amp_key}: axis-avg P(>=3sig)={aa['p_detect_3sigma']:.3f} "
              f"P(>=5sig)={aa['p_detect_5sigma']:.3f} "
              f"median sigma={aa['sigma_median']:+.2f}", flush=True)
    print(f"wrote {OUT}  ({time.time()-t0:.0f}s)", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
