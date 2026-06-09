#!/usr/bin/env python3
"""
C9a — 10,000-permutation per-galaxy label-shuffle MASTER nulls for the P4
ell=1 diagnostic + Table III bandpowers, on BOTH analysis footprints.

Footprint (i): apodized N_all >= 1 subsample footprint, Wp = N_all
  (the +7.28 sigma diagnostic channel; conventions copied verbatim from
  c3_p4_wp_invariance_fsky.py / c6_p4_depth_stratified_null.py: C2 2-deg
  apodization, A_p = (N_CW - N_CCW)/N_spiral with weight-map-weighted
  mask-mean subtraction, lite NmtFields, seed 42).

Footprint (ii): canonical unapodized mask (pixels with >= 10 spirals,
  f_sky = 0.49005; conventions copied verbatim from
  c2_p4_nall_binomial_null.py post-MASTER block / v1.0.121 convention:
  A_p = N_CW/N_spiral - 0.5 with galaxy-weighted (N_spiral) monopole
  subtraction over all N_spiral > 0 pixels, binary unapodized mask).

Binning: Table III bands — band 0 = single-mode ell=1, then 5-wide linear
bands ell in [2,6],[7,11],[12,16],[17,21],[22,26], ... continuing 5-wide to
lmax=191 (38 five-wide bands; bands 0..5 are the reported Table III rows).

Null: 10,000 per-galaxy CW/CCW label permutations (pool = SPIRALS ONLY).
Parallel deviation from the serial c3/c6 RNG stream: each realization k uses
an independent deterministic stream np.random.default_rng([SEED, vi, k])
(seed 42 base) instead of one sequential stream — distributionally identical.

Run on pod:
  tmux new -s c9a -d 'cd /workspace && C9_NPROC=4 python3 c9a_p4_10k_nulls.py 2>&1 | tee c9a.log'
Output: /workspace/c9_results/c9a_10k_nulls.json (+ full null .npy arrays)
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
N_MC = 10_000
SEED = 42
APOD_DEG = 2.0
APOD_TYPE = "C2"
MASK_DEFINITION_SUB = "N_all >= 1"
MIN_SPIRALS_CANONICAL = 10  # canonical mask: pixels with >= 10 spirals
REPORT_BANDS = [0, 1, 2, 3, 4, 5]
BAND_LABELS = ["ell=1 (single mode)", "ell in [2,6]", "ell in [7,11]",
               "ell in [12,16]", "ell in [17,21]", "ell in [22,26]"]
NPROC = int(os.environ.get("C9_NPROC", max(1, (os.cpu_count() or 2) - 1)))
OUTDIR = Path(os.environ.get("C9_OUTDIR", "/workspace/c9_results"))
OUT = OUTDIR / "c9a_10k_nulls.json"
WS_DIR = Path("/workspace/c9_tmp")

# ---------------- module-level state (fork-inherited by workers) ----------------
G: dict = {}
_W: dict = {}  # per-worker workspace


def find_catalog() -> str:
    for c in ["/workspace/r42_b20/chirality_catalog/catalog_production.parquet",
              "/workspace/catalog_production.parquet"]:
        if os.path.exists(c):
            return c
    from huggingface_hub import hf_hub_download
    return hf_hub_download("bamfai/galaxy-chirality-catalog",
                           "catalog_production.parquet", repo_type="dataset")


def make_bins() -> nmt.NmtBin:
    """Table III banding: band 0 = ell=1 single mode; bands b>=1 are 5-wide
    linear bands starting at ell=2 (band 1 = [2,6] -> ell_eff 4, etc.)."""
    bpws = np.full(LMAX + 1, -1, dtype=np.int32)
    bpws[1] = 0
    for ell in range(2, LMAX + 1):
        bpws[ell] = 1 + (ell - 2) // 5
    return nmt.NmtBin(bpws=bpws, ells=np.arange(LMAX + 1, dtype=np.int32),
                      weights=np.ones(LMAX + 1), lmax=LMAX)


def build_A_sub_apod(labels: np.ndarray) -> np.ndarray:
    """Footprint (i) field — copied from c6 build_A_sub with W = W_nall:
    A_p = (N_CW - N_CCW)/N_spiral with weight-map-weighted mask-mean
    subtraction (galaxy-weighted convention, weights = W_p)."""
    npix = G["npix"]
    n_cw = np.bincount(G["pix_sp"][labels == 1], minlength=npix).astype(np.float64)
    n_ccw = np.bincount(G["pix_sp"][labels == 0], minlength=npix).astype(np.float64)
    nz = G["nz_spiral"]
    A = np.zeros(npix)
    A[nz] = (n_cw[nz] - n_ccw[nz]) / G["n_spiral_pix"][nz]
    wsel = G["wsel"]
    W = G["W_nall"]
    A_gw = float((A[wsel] * W[wsel]).sum() / W[wsel].sum())
    A_sub = np.zeros(npix)
    A_sub[wsel] = A[wsel] - A_gw
    return A_sub


def build_A_sub_canonical(labels: np.ndarray) -> np.ndarray:
    """Footprint (ii) field — copied from c2_p4_nall_binomial_null.py
    post-MASTER block (v1.0.121 convention): A = N_CW/N_spiral - 0.5 with
    galaxy-weighted (N_spiral) monopole subtraction over N_spiral > 0 pixels."""
    npix = G["npix"]
    n_cw = np.bincount(G["pix_sp"][labels == 1], minlength=npix).astype(np.float64)
    nz = G["nz_spiral"]
    nsp = G["n_spiral_pix"]
    A = np.zeros(npix)
    A[nz] = (n_cw[nz] / nsp[nz]) - 0.5
    A_gw = float((A[nz] * nsp[nz]).sum() / nsp[nz].sum())
    A_sub = A.copy()
    A_sub[nz] -= A_gw
    A_sub[~nz] = 0.0
    return A_sub


VARIANTS = [
    ("apod_footprint_Wp_Nall", build_A_sub_apod),
    ("canonical_unapodized", build_A_sub_canonical),
]


def _init_worker(ws_path: str) -> None:
    w = nmt.NmtWorkspace()
    w.read_from(ws_path)
    _W["w"] = w


def _null_one(args):
    vi, k = args
    rng = np.random.default_rng([SEED, vi, k])
    labels_perm = G["labels_cw"][rng.permutation(G["n_sp"])]
    A = VARIANTS[vi][1](labels_perm)
    f = nmt.NmtField(G["weights"][vi], [A], lite=True)
    cl = _W["w"].decouple_cell(nmt.compute_coupled_cell(f, f))[0]
    return k, cl.astype(np.float64)


def main() -> int:
    t0 = time.time()
    OUTDIR.mkdir(parents=True, exist_ok=True)
    WS_DIR.mkdir(parents=True, exist_ok=True)
    print(f"[{time.time()-t0:.1f}s] C9a 10k-null job starting  NPROC={NPROC}", flush=True)

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
    print(f"[{time.time()-t0:.1f}s] spirals (shuffle pool): {n_sp:,}  "
          f"p_CW={labels_cw.mean():.6f}", flush=True)

    # Footprint (i): N_all >= 1, C2 2-deg apodized, weights Wp = N_all
    mask_sub_bool = n_all_pix >= 1
    mask_sub_binary = mask_sub_bool.astype(np.float64)
    print(f"[{time.time()-t0:.1f}s] subsample mask {MASK_DEFINITION_SUB}: "
          f"n_pix={int(mask_sub_bool.sum())} f_sky={mask_sub_binary.mean():.5f}", flush=True)
    mask_apod = nmt.mask_apodization(mask_sub_binary, APOD_DEG, apotype=APOD_TYPE)
    W_nall = n_all_pix * mask_sub_binary
    W_eff_apod = W_nall * mask_apod

    # Footprint (ii): canonical mask = pixels with >= 10 spirals, unapodized
    mask_can_bool = n_spiral_pix >= MIN_SPIRALS_CANONICAL
    mask_can_float = mask_can_bool.astype(np.float64)
    print(f"[{time.time()-t0:.1f}s] canonical mask N_spiral>={MIN_SPIRALS_CANONICAL}: "
          f"n_pix={int(mask_can_bool.sum())} f_sky={mask_can_float.mean():.5f} "
          f"(published 0.49005)", flush=True)

    nz_spiral = n_spiral_pix > 0
    G.update({
        "npix": npix, "pix_sp": pix_sp, "labels_cw": labels_cw, "n_sp": n_sp,
        "n_spiral_pix": n_spiral_pix, "nz_spiral": nz_spiral,
        "wsel": mask_sub_bool & nz_spiral, "W_nall": W_nall,
        "weights": [W_eff_apod, mask_can_float],
    })

    b = make_bins()
    eff = b.get_effective_ells()
    n_bands = b.get_n_bands()
    print(f"[{time.time()-t0:.1f}s] bins: {n_bands} bands; "
          f"eff ells of report bands: {[float(eff[i]) for i in REPORT_BANDS]}", flush=True)

    results = {}
    for vi, (name, builder) in enumerate(VARIANTS):
        tv = time.time()
        W_field = G["weights"][vi]
        print(f"\n[{time.time()-t0:.1f}s] === variant {name}: coupling matrix ...", flush=True)
        f_dummy = nmt.NmtField(W_field, [np.zeros(npix)], lite=True)
        w = nmt.NmtWorkspace()
        w.compute_coupling_matrix(f_dummy, f_dummy, b)
        ws_path = str(WS_DIR / f"c9a_ws_{name}.fits")
        if os.path.exists(ws_path):
            os.remove(ws_path)
        w.write_to(ws_path)

        A_data = builder(labels_cw)
        f_data = nmt.NmtField(W_field, [A_data], lite=True)
        cl_data = w.decouple_cell(nmt.compute_coupled_cell(f_data, f_data))[0]
        print(f"[{time.time()-t0:.1f}s] {name} data bands "
              f"{[f'{cl_data[i]:.4e}' for i in REPORT_BANDS]}", flush=True)

        nulls = np.zeros((N_MC, n_bands))
        done = 0
        ctx = get_context("fork")
        with ctx.Pool(NPROC, initializer=_init_worker, initargs=(ws_path,)) as pool:
            for k, cl in pool.imap_unordered(
                    _null_one, [(vi, k) for k in range(N_MC)], chunksize=8):
                nulls[k] = cl
                done += 1
                if done % 250 == 0:
                    el = time.time() - tv
                    eta = el / done * (N_MC - done)
                    print(f"[{time.time()-t0:.1f}s]  {name} null {done}/{N_MC} "
                          f"l1 mean={nulls[:, 0][nulls[:, 0] != 0].mean():.4e} "
                          f"ETA {eta:.0f}s", flush=True)

        np.save(OUTDIR / f"c9a_nulls_{name}.npy", nulls)
        bands_out = {}
        for bi in REPORT_BANDS:
            nb = nulls[:, bi]
            m, s = float(nb.mean()), float(nb.std(ddof=1))
            d = float(cl_data[bi])
            n_ge = int((nb >= d).sum())
            bands_out[f"band_{bi}"] = {
                "label": BAND_LABELS[bi],
                "ell_eff": float(eff[bi]),
                "C_data_decoupled": d,
                "null_mean": m, "null_std": s,
                "sigma": (d - m) / s,
                "n_null_ge_data": n_ge,
                "empirical_rank_p_one_sided": (1 + n_ge) / (N_MC + 1),
                "empirical_rank_p_two_sided": 2.0 * min(n_ge, N_MC - n_ge) / N_MC,
            }
        results[name] = {
            "bands": bands_out,
            "n_mc": N_MC,
            "null_array_npy": str(OUTDIR / f"c9a_nulls_{name}.npy"),
            "wallclock_s": time.time() - tv,
        }
        print(f"[{time.time()-t0:.1f}s] {name} done: "
              + "  ".join(f"b{bi} sigma={bands_out[f'band_{bi}']['sigma']:+.3f} "
                          f"p1s={bands_out[f'band_{bi}']['empirical_rank_p_one_sided']:.2e}"
                          for bi in REPORT_BANDS), flush=True)

    out = {
        "job": "C9a-P4-10k-permutation-nulls",
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "purpose": ("10,000-permutation per-galaxy label-shuffle MASTER nulls for "
                    "the Table III bandpowers on (i) the apodized N_all>=1 footprint "
                    "with Wp=N_all (the +7.28 sigma diagnostic channel) and (ii) the "
                    "canonical unapodized mask, with empirical rank-p per band."),
        "config": {
            "nside": NSIDE, "lmax": LMAX, "n_mc": N_MC, "seed": SEED,
            "binning": ("band 0 = single-mode ell=1; bands b>=1 = 5-wide linear "
                        "bands from ell=2 (Table III rows = bands 0..5); "
                        f"{n_bands} bands total to lmax={LMAX}"),
            "report_bands": REPORT_BANDS,
            "effective_ells_report_bands": [float(eff[i]) for i in REPORT_BANDS],
            "footprint_i": {
                "mask": MASK_DEFINITION_SUB,
                "apodization": f"{APOD_TYPE} {APOD_DEG} deg",
                "weights": "Wp = N_all (x apodized mask)",
                "field": ("A_p=(N_CW-N_CCW)/N_spiral, weight-map-weighted "
                          "mask-mean subtracted (c3/c6 convention)"),
            },
            "footprint_ii": {
                "mask": f"canonical: N_spiral >= {MIN_SPIRALS_CANONICAL}, unapodized binary",
                "weights": "binary mask",
                "field": ("A_p = N_CW/N_spiral - 0.5, galaxy-weighted (N_spiral) "
                          "monopole subtraction (c2 post-MASTER / v1.0.121 convention)"),
            },
            "null": ("per-galaxy CW/CCW label permutation, pool = spirals only; "
                     "independent stream per realization: "
                     "np.random.default_rng([42, variant_idx, k])"),
            "n_spirals": n_sp,
            "nproc": NPROC,
        },
        "results": results,
        "c3_c6_references": {
            "apod_Wp_Nall_global_shuffle_sigma_500mc": 7.28,
            "apod_Wp_Nall_depth_stratified_sigma_500mc": 7.13,
            "canonical_direct_mc_l1_sigma_500mc": 3.64,
        },
        "wallclock_s": time.time() - t0,
    }
    OUT.write_text(json.dumps(out, indent=2))
    print(f"\n=== C9a RESULTS ===", flush=True)
    for name, r in results.items():
        for bi in REPORT_BANDS:
            bb = r["bands"][f"band_{bi}"]
            print(f"  {name} {bb['label']}: sigma={bb['sigma']:+.4f} "
                  f"p1s={bb['empirical_rank_p_one_sided']:.3e}", flush=True)
    print(f"wrote {OUT}  ({time.time()-t0:.0f}s)", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
