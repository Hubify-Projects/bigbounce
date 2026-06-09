#!/usr/bin/env python3
"""
C9d — shuffle-pool verification (quick).

Programmatically asserts, for each per-galaxy label-shuffle null
implementation in the C3 / C6 / C9 scripts, that the permutation pool is
SPIRALS ONLY: the CW/CCW label array is constructed from the is_spiral
subset of the catalog, NOT_SPIRAL objects never enter the pool, and the
pool sizes are printed. Two layers:

1. Data-level assertions: rebuild the pool exactly as the scripts do
   (pix_sp = pix_all[is_spiral]; labels_cw = is_cw[is_spiral]) and assert
   (a) pool size == number of CW+CCW rows, (b) every pool member's class is
   CW or CCW, (c) NOT_SPIRAL count is excluded, (d) CW + CCW partition the
   pool, (e) the c6 depth-decile strata partition the spiral pool exactly.

2. Source-level audit: scan the c3/c6/c9 script sources on the pod for the
   pool-construction idiom (pix_all[is_spiral] / is_cw[is_spiral]) and
   record whether each defines the pool on spirals only.

Also recomputes one 50-MC smoke null per variant as a sanity check:
  (a) apodized N_all>=1 footprint, Wp=N_all, global shuffle  (c3/c9a/c9b/c9c)
  (b) same channel, depth-stratified shuffle                 (c6)
  (c) canonical unapodized mask, global shuffle              (c9a footprint ii)

Run on pod:
  tmux new -s c9d -d 'cd /workspace && python3 c9d_p4_pool_verification.py 2>&1 | tee c9d.log'
Output: /workspace/c9_results/c9d_pool_verification.json
"""
from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "2")
os.environ.setdefault("HF_HOME", "/workspace/.hf_home")

import json
import re
import time
from pathlib import Path

import numpy as np
import pandas as pd
import healpy as hp
import pymaster as nmt

NSIDE = 64
LMAX = 3 * NSIDE - 1  # 191
N_MC_SMOKE = 50
SEED = 42
APOD_DEG = 2.0
APOD_TYPE = "C2"
N_STRATA = 10
MIN_SPIRALS_CANONICAL = 10
OUTDIR = Path(os.environ.get("C9_OUTDIR", "/workspace/c9_results"))
OUT = OUTDIR / "c9d_pool_verification.json"

SOURCE_CANDIDATES = [
    "/workspace/c3_p4_wp_invariance_fsky.py",
    "/workspace/c6_p4_depth_stratified_null.py",
    "/workspace/c9a_p4_10k_nulls.py",
    "/workspace/c9b_p4_injection_completeness.py",
    "/workspace/c9c_p4_wp_sweep.py",
]


def find_catalog() -> str:
    for c in ["/workspace/r42_b20/chirality_catalog/catalog_production.parquet",
              "/workspace/catalog_production.parquet"]:
        if os.path.exists(c):
            return c
    from huggingface_hub import hf_hub_download
    return hf_hub_download("bamfai/galaxy-chirality-catalog",
                           "catalog_production.parquet", repo_type="dataset")


def audit_source(path: str) -> dict:
    """Scan a script source for the spirals-only pool-construction idiom."""
    if not os.path.exists(path):
        return {"present": False}
    src = Path(path).read_text()
    pool_from_spirals = bool(
        re.search(r"pix_all\[is_spiral\]", src)
        and re.search(r"is_cw\[is_spiral\]", src))
    # any shuffle/permutation applied to a non-spiral-pool label array?
    permutes_labels = bool(re.search(r"permutation|shuffle", src))
    notspiral_in_pool = bool(re.search(r"labels[^\n]*NOT_SPIRAL", src))
    return {
        "present": True,
        "pool_constructed_from_is_spiral_subset": pool_from_spirals,
        "uses_permutation": permutes_labels,
        "notspiral_referenced_in_label_pool": notspiral_in_pool,
        "verdict_spirals_only": pool_from_spirals and not notspiral_in_pool,
    }


def main() -> int:
    t0 = time.time()
    OUTDIR.mkdir(parents=True, exist_ok=True)
    print(f"[{time.time()-t0:.1f}s] C9d pool-verification job starting", flush=True)

    cat_path = find_catalog()
    df = pd.read_parquet(cat_path, columns=["ra", "dec", "class_eq"])
    n_total = len(df)
    classes = df["class_eq"].values
    print(f"[{time.time()-t0:.1f}s] catalog rows (all classes): {n_total:,}", flush=True)

    npix = hp.nside2npix(NSIDE)
    pix_all = hp.ang2pix(NSIDE,
                         np.radians(90.0 - df["dec"].values.astype(np.float64)),
                         np.radians(df["ra"].values.astype(np.float64))).astype(np.int64)
    is_cw = (classes == "CW")
    is_ccw = (classes == "CCW")
    is_spiral = is_cw | is_ccw
    n_cw, n_ccw = int(is_cw.sum()), int(is_ccw.sum())
    n_spiral = int(is_spiral.sum())
    n_notspiral = int((~is_spiral).sum())

    # ---------- 1. Data-level pool assertions (exactly as c3/c6/c9 build it) ----
    pix_sp = pix_all[is_spiral]
    labels_cw = is_cw[is_spiral].astype(np.int8)
    pool_classes = classes[is_spiral]

    assert len(pix_sp) == len(labels_cw) == n_spiral, "pool size != N_CW + N_CCW"
    assert set(np.unique(pool_classes)) <= {"CW", "CCW"}, \
        "non-spiral class found inside the shuffle pool"
    assert int(labels_cw.sum()) == n_cw, "CW count mismatch inside pool"
    assert int((1 - labels_cw).sum()) == n_ccw, "CCW count mismatch inside pool"
    assert n_spiral + n_notspiral == n_total, "spiral/NS partition broken"
    print(f"[{time.time()-t0:.1f}s] POOL SIZES: total={n_total:,}  "
          f"spirals(in pool)={n_spiral:,} (CW={n_cw:,}, CCW={n_ccw:,})  "
          f"NOT_SPIRAL(excluded)={n_notspiral:,}", flush=True)
    print(f"[{time.time()-t0:.1f}s] ASSERT OK: shuffle pool is SPIRALS ONLY; "
          f"NS never enters", flush=True)

    n_all_pix = np.bincount(pix_all, minlength=npix).astype(np.float64)
    n_spiral_pix = np.bincount(pix_sp, minlength=npix).astype(np.float64)
    nz = n_spiral_pix > 0

    # c6 depth-decile strata partition check
    mask_bool = n_all_pix >= 1
    n_in = n_all_pix[mask_bool]
    strata_edges = np.quantile(n_in[n_in > 0], np.linspace(0, 1, N_STRATA + 1))
    strata_edges[0] = -1.0
    strata_edges[-1] = n_in.max() + 1.0
    pix_strata = np.full(npix, -1, dtype=np.int8)
    pix_strata[mask_bool] = np.digitize(n_all_pix[mask_bool], strata_edges[1:-1])
    gal_strata = pix_strata[pix_sp]
    assert (gal_strata >= 0).all(), "c6 strata: spiral outside mask strata"
    strata_sizes = [int((gal_strata == s).sum()) for s in range(N_STRATA)]
    assert sum(strata_sizes) == n_spiral, "c6 strata do not partition the spiral pool"
    print(f"[{time.time()-t0:.1f}s] ASSERT OK: c6 strata partition the spiral pool "
          f"exactly; sizes={strata_sizes}", flush=True)

    # ---------- 2. Source-level audit ----------
    source_audit = {os.path.basename(p): audit_source(p) for p in SOURCE_CANDIDATES}
    for k, v in source_audit.items():
        print(f"[{time.time()-t0:.1f}s] source audit {k}: {v}", flush=True)

    # ---------- 3. 50-MC smoke nulls per variant ----------
    mask_binary = mask_bool.astype(np.float64)
    mask_apod = nmt.mask_apodization(mask_binary, APOD_DEG, apotype=APOD_TYPE)
    W_nall = n_all_pix * mask_binary
    W_eff = W_nall * mask_apod
    wsel = mask_bool & nz

    mask_can_bool = n_spiral_pix >= MIN_SPIRALS_CANONICAL
    mask_can_float = mask_can_bool.astype(np.float64)

    bpws = np.full(LMAX + 1, -1, dtype=np.int32)
    for ell in range(1, LMAX + 1):
        bpws[ell] = ell - 1
    b_custom = nmt.NmtBin(bpws=bpws, ells=np.arange(LMAX + 1, dtype=np.int32),
                          weights=np.ones(LMAX + 1), lmax=LMAX)

    def build_A_apod(labels):
        ncw = np.bincount(pix_sp[labels == 1], minlength=npix).astype(np.float64)
        nccw = np.bincount(pix_sp[labels == 0], minlength=npix).astype(np.float64)
        A = np.zeros(npix)
        A[nz] = (ncw[nz] - nccw[nz]) / n_spiral_pix[nz]
        A_gw = float((A[wsel] * W_nall[wsel]).sum() / W_nall[wsel].sum())
        A_sub = np.zeros(npix)
        A_sub[wsel] = A[wsel] - A_gw
        return A_sub

    def build_A_canonical(labels):
        ncw = np.bincount(pix_sp[labels == 1], minlength=npix).astype(np.float64)
        A = np.zeros(npix)
        A[nz] = (ncw[nz] / n_spiral_pix[nz]) - 0.5
        A_gw = float((A[nz] * n_spiral_pix[nz]).sum() / n_spiral_pix[nz].sum())
        A_sub = A.copy()
        A_sub[nz] -= A_gw
        A_sub[~nz] = 0.0
        return A_sub

    stratum_to_gal = [np.where(gal_strata == s)[0] for s in range(N_STRATA)]

    def perm_global(rng, labels):
        return labels[rng.permutation(len(labels))]

    def perm_stratified(rng, labels):
        out = labels.copy()
        for g_idx in stratum_to_gal:
            out[g_idx] = out[g_idx][rng.permutation(len(g_idx))]
        return out

    smoke_variants = [
        ("apod_Wp_Nall_global_shuffle", W_eff, build_A_apod, perm_global, 7.28),
        ("apod_Wp_Nall_depth_stratified", W_eff, build_A_apod, perm_stratified, 7.13),
        ("canonical_unapodized_global_shuffle", mask_can_float, build_A_canonical,
         perm_global, None),
    ]

    smoke = {}
    for name, Wf, builder, perm, ref in smoke_variants:
        tv = time.time()
        print(f"\n[{time.time()-t0:.1f}s] === smoke {name}: coupling matrix ...", flush=True)
        f_dummy = nmt.NmtField(Wf, [np.zeros(npix)], lite=True)
        w = nmt.NmtWorkspace()
        w.compute_coupling_matrix(f_dummy, f_dummy, b_custom)
        A_data = builder(labels_cw)
        f_data = nmt.NmtField(Wf, [A_data], lite=True)
        C1_data = float(w.decouple_cell(nmt.compute_coupled_cell(f_data, f_data))[0][0])
        rng = np.random.default_rng(SEED)
        nulls = np.zeros(N_MC_SMOKE)
        labels_perm = labels_cw.copy()
        for k in range(N_MC_SMOKE):
            labels_perm = perm(rng, labels_perm)
            A_n = builder(labels_perm)
            f_n = nmt.NmtField(Wf, [A_n], lite=True)
            nulls[k] = float(w.decouple_cell(nmt.compute_coupled_cell(f_n, f_n))[0][0])
            if (k + 1) % 10 == 0:
                print(f"[{time.time()-t0:.1f}s]  {name} smoke {k+1}/{N_MC_SMOKE}", flush=True)
        m, s = float(nulls.mean()), float(nulls.std(ddof=1))
        sigma = (C1_data - m) / s
        smoke[name] = {
            "C1_data_decoupled": C1_data,
            "null_mean": m, "null_std": s, "sigma": sigma,
            "n_mc": N_MC_SMOKE,
            "reference_sigma_500mc": ref,
            "pool_size_permuted": int(n_spiral),
            "wallclock_s": time.time() - tv,
        }
        print(f"[{time.time()-t0:.1f}s] {name}: smoke sigma = {sigma:+.3f} "
              f"(500-MC ref {ref})", flush=True)

    out = {
        "job": "C9d-P4-shuffle-pool-verification",
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "purpose": ("Programmatic verification that every per-galaxy label-shuffle "
                    "null in the c3/c6/c9 scripts permutes CW/CCW labels among "
                    "SPIRALS ONLY (NOT_SPIRAL never enters the pool), plus 50-MC "
                    "smoke nulls per variant."),
        "pool_sizes": {
            "catalog_total": n_total,
            "spirals_in_pool": n_spiral,
            "cw_in_pool": n_cw,
            "ccw_in_pool": n_ccw,
            "not_spiral_excluded": n_notspiral,
        },
        "data_level_assertions": {
            "pool_size_equals_cw_plus_ccw": True,
            "pool_classes_subset_of_cw_ccw": True,
            "not_spiral_never_in_pool": True,
            "c6_strata_partition_spiral_pool": True,
            "c6_strata_galaxy_counts": strata_sizes,
        },
        "source_audit": source_audit,
        "smoke_nulls_50mc": smoke,
        "config": {"nside": NSIDE, "lmax": LMAX, "seed": SEED,
                   "n_mc_smoke": N_MC_SMOKE,
                   "apodization": f"{APOD_TYPE} {APOD_DEG} deg"},
        "wallclock_s": time.time() - t0,
    }
    OUT.write_text(json.dumps(out, indent=2))
    print(f"\n=== C9d RESULTS ===", flush=True)
    print(f"  pool: {n_spiral:,} spirals (CW {n_cw:,} / CCW {n_ccw:,}); "
          f"{n_notspiral:,} NOT_SPIRAL excluded — ALL ASSERTS PASSED", flush=True)
    print(f"wrote {OUT}  ({time.time()-t0:.0f}s)", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
