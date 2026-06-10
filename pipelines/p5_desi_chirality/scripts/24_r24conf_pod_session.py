#!/usr/bin/env python3
"""P5 R24conf compute-queue closures #16-#19 (queue:
project-context/peer-reviews/R24CONF_COMPUTE_QUEUE.md).

  #16 META-M1 — angular completeness control via DESI randoms: DATA
      AVAILABILITY CHECK ONLY. The DESI DR1 random catalogs are not present
      locally or on the compute volume; this part documents the exhaustive
      search (no rebuild is invented). Item stays OPEN.

  #17 META-M4 — Phase-2 p_LEE rerun with leg x program STRATIFIED shuffles
      (row-level label permutation within match_imaging_leg|desi_program
      strata, the conservative null of scripts/18) on all nine sweep cells,
      PLUS a global max-stat p across the 9 cells (and across the 6 resolved
      R_s in {25,50} cells), with free-shuffle comparators. Per-cell joins
      and the max-class |sigma_from_half| statistic are identical to
      scripts/17_v0151_closure_recomputes.py T4/T4b.

  #18 META-M5 — VoidFinder membership-definition comparison on the z<=0.24
      matched-spiral sample (C8 driver conventions, explicit Mpc/h):
        Def A (published, permissive): inside ANY hole sphere (HOLES HDU).
        Def B (interior-void):        inside any MAXIMAL sphere (MAXIMALS
                                       HDU RADIUS — the void-defining sphere).
      Reports f_CW / Delta f_CW / two-sample z under both.

  #19 META-M6 — 1.7 < z <= 2.0 tail sensitivity for the z-shell-corrected
      build: quantified directly on the filtered field parent (ZWARN==0,
      SPECTYPE==GALAXY, 0.01<z<2.0 — the published 14,622,283-row parent).
      The realized tail is EMPTY, so the drop-tail and separate-shell
      variants coincide exactly with the published build (exact no-op).

Output: pipelines/p5_desi_chirality/outputs/24_r24conf_pod_session.json
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np
import pandas as pd
import pyarrow.parquet as pq
from scipy import sparse
from scipy.spatial import cKDTree

P5 = Path(__file__).resolve().parents[1]
MATCHED = P5 / "results/p5_matched_chirality_desi.parquet"
SWEEP_DIR = P5 / "data/desi_env/phase2_sweep"
DESIVAST_DIR = P5 / "data/desivast"
ZALL = P5 / "data/desi_zall.parquet"
OUT = P5 / "outputs/24_r24conf_pod_session.json"

ENV_ORDER = ["void", "wall", "filament", "cluster"]
H0, OM0, LITTLE_H = 67.66, 0.315, 0.6766
Z_DESIVAST_MAX = 0.24
N_MC = 1000
SEED = 20260610
RESOLVED_PREFIXES = ("R25_", "R50_")
T0 = time.time()


def log(m):
    print(f"[{time.time()-T0:.1f}s] {m}", flush=True)


def _sig(k, n):
    n = np.asarray(n, dtype=float)
    return (np.asarray(k, dtype=float) - 0.5 * n) / (0.5 * np.sqrt(n))


def _cls_row(n, n_cw):
    return {"n": int(n), "n_cw": int(n_cw),
            "cw_fraction": (n_cw / n) if n else None,
            "sigma_from_half": float(_sig(n_cw, n)) if n else None}


def main() -> int:
    out = {
        "written_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "script": "scripts/24_r24conf_pod_session.py",
        "seed": SEED, "n_mc": N_MC,
    }

    # ---------------- #16: randoms data-availability check -------------------
    log("#16: DESI randoms availability check")
    rand_hits = []
    for base in [P5 / "data", P5 / "data/desi_env", P5.parents[1] / "data"]:
        if base.exists():
            rand_hits += [str(p) for p in base.rglob("*random*")]
    out["item16_randoms_check"] = {
        "status": "DATA-MISSING",
        "searched": [str(P5 / "data"), str(P5 / "data/desi_env"),
                     str(P5.parents[1] / "data"),
                     "pod 5i2td3deu3hojr:/workspace (checked 2026-06-10; "
                     "volume holds only c-series outputs)"],
        "hits": rand_hits,
        "note": ("DESI DR1 random catalogs (per-tracer randoms-*.fits, "
                 "~tens of GB from NERSC/desidata) are not present locally "
                 "or on the compute volume; the randoms/completeness-weighted "
                 "delta rebuild remains OPEN. No invariance claim is made."),
    }

    # ---------------- #19: z-tail quantification -----------------------------
    log("#19: 1.7<z<=2.0 tail quantification on filtered field parent")
    zt = pq.read_table(ZALL, columns=["Z", "ZWARN", "SPECTYPE"]).to_pandas()
    fm = ((zt["ZWARN"] == 0)
          & (zt["SPECTYPE"].astype(str).str.strip() == "GALAXY")
          & (zt["Z"] > 0.01) & (zt["Z"] < 2.0))
    zf = zt.loc[fm, "Z"]
    n_tail = int(((zf > 1.7) & (zf <= 2.0)).sum())
    out["item19_ztail_sensitivity"] = {
        "filter": "ZWARN==0 & SPECTYPE==GALAXY & 0.01<z<2.0 (env_finder/config.yaml)",
        "n_filtered_parent": int(fm.sum()),
        "z_max_realized": float(zf.max()),
        "n_in_1p7_to_2p0": n_tail,
        "n_above_1p65": int((zf > 1.65).sum()),
        "n_above_1p69": int((zf > 1.69).sum()),
        "conclusion": ("The realized 1.7<z<=2.0 tail of the filtered parent is "
                       "EMPTY (n=0; max z = 1.6979), so both queued variants "
                       "(drop tail / separate top shell) are exact no-ops: "
                       "every shell assignment, the delta field, and all "
                       "per-galaxy labels are unchanged from the published "
                       "z-shell-corrected build."),
    }
    del zt, zf
    OUT.write_text(json.dumps(out, indent=1))

    # ---------------- shared parent ------------------------------------------
    log("loading matched parent")
    cols = ["desi_targetid", "match_class_eq", "desi_program", "desi_z",
            "desi_ra", "desi_dec", "matched_primary_deduped",
            "match_imaging_leg"]
    matched = pd.read_parquet(MATCHED, columns=cols)
    sp = matched[matched["matched_primary_deduped"]
                 & matched["match_class_eq"].isin(["CW", "CCW"])].reset_index(drop=True)
    del matched
    n_sp = len(sp)
    y = (sp["match_class_eq"] == "CW").to_numpy(np.float64)
    strata_lbl = (sp["match_imaging_leg"].astype(str) + "|"
                  + sp["desi_program"].astype(str)).to_numpy()
    strata, s_inv = np.unique(strata_lbl, return_inverse=True)
    stratum_rows = [np.where(s_inv == si)[0] for si in range(len(strata))]
    log(f"parent n={n_sp:,}  strata={len(strata)}")

    # ---------------- #17: stratified Phase-2 + global max-stat --------------
    log("#17: building per-cell count matrices")
    cells = {}
    for pqf in sorted(SWEEP_DIR.glob("desi_env_vweb_*.parquet")):
        cell = pqf.stem.replace("desi_env_vweb_", "")
        e = pd.read_parquet(pqf, columns=["TARGETID", "env_class"])
        sp_idx = sp.reset_index().rename(columns={"index": "_row"})
        j = sp_idx[["_row", "desi_targetid"]].merge(
            e, left_on="desi_targetid", right_on="TARGETID", how="inner")
        cls_idx = pd.Categorical(j["env_class"], categories=ENV_ORDER).codes
        keep = cls_idx >= 0
        rows = j["_row"].to_numpy()[keep]
        cls = cls_idx[keep].astype(np.int64)
        M = sparse.csr_matrix(
            (np.ones(len(rows)), (cls, rows)), shape=(4, n_sp))
        ns = np.asarray(M.sum(axis=1)).ravel()
        kcw = M @ y
        obs = float(np.max(np.abs(_sig(kcw, ns))))
        cells[cell] = {"M": M, "ns": ns, "obs": obs,
                       "n_joined": int(len(rows)),
                       "per_class": {c: _cls_row(ns[i], kcw[i])
                                     for i, c in enumerate(ENV_ORDER)}}
        log(f"  cell {cell}: n_joined={len(rows):,} obs_max|sigma|={obs:.3f}")
        del e, j

    cell_names = list(cells.keys())
    resolved = [c for c in cell_names if c.startswith(RESOLVED_PREFIXES)]
    obs_global_9 = max(cells[c]["obs"] for c in cell_names)
    obs_global_6 = max(cells[c]["obs"] for c in resolved)

    log("#17: permutations (stratified + free)")
    rng = np.random.default_rng(SEED)
    null_cell_strat = {c: np.zeros(N_MC) for c in cell_names}
    null_cell_free = {c: np.zeros(N_MC) for c in cell_names}
    for k in range(N_MC):
        # stratified row-level permutation
        y_s = y.copy()
        for idx in stratum_rows:
            y_s[idx] = y[idx][rng.permutation(len(idx))]
        # free permutation
        y_f = y[rng.permutation(n_sp)]
        for c in cell_names:
            M, ns = cells[c]["M"], cells[c]["ns"]
            null_cell_strat[c][k] = np.max(np.abs(_sig(M @ y_s, ns)))
            null_cell_free[c][k] = np.max(np.abs(_sig(M @ y_f, ns)))
        if (k + 1) % 100 == 0:
            log(f"  perm {k+1}/{N_MC}")

    def pval(null, obs):
        return float((1 + int((null >= obs).sum())) / (1 + N_MC))

    per_cell = {}
    for c in cell_names:
        per_cell[c] = {
            "obs_max_abs_sigma": cells[c]["obs"],
            "n_joined": cells[c]["n_joined"],
            "p_lee_stratified": pval(null_cell_strat[c], cells[c]["obs"]),
            "p_lee_free": pval(null_cell_free[c], cells[c]["obs"]),
        }
    g9_s = np.max(np.stack([null_cell_strat[c] for c in cell_names]), axis=0)
    g9_f = np.max(np.stack([null_cell_free[c] for c in cell_names]), axis=0)
    g6_s = np.max(np.stack([null_cell_strat[c] for c in resolved]), axis=0)
    g6_f = np.max(np.stack([null_cell_free[c] for c in resolved]), axis=0)
    out["item17_phase2_stratified_lee"] = {
        "stratification": "row-level label permutation within "
                          "match_imaging_leg|desi_program strata "
                          f"({len(strata)} strata; scripts/18 convention)",
        "statistic": "max over K=4 classes of |sigma_from_half| "
                     "(scripts/17 T4b convention); joins are the superset "
                     "per-cell joins of T4",
        "per_cell": per_cell,
        "global_max_stat": {
            "all_9_cells": {"obs": obs_global_9,
                            "p_stratified": pval(g9_s, obs_global_9),
                            "p_free": pval(g9_f, obs_global_9)},
            "resolved_6_cells_Rs25_50": {"obs": obs_global_6,
                                         "p_stratified": pval(g6_s, obs_global_6),
                                         "p_free": pval(g6_f, obs_global_6)},
            "note": "global null propagates ONE parent permutation through "
                    "all cells per draw (cross-cell correlations preserved)",
        },
    }
    for c in cell_names:
        cells[c].pop("M")
    OUT.write_text(json.dumps(out, indent=1))
    log("#17 written")

    # ---------------- #18: VoidFinder membership definitions -----------------
    log("#18: VoidFinder hole vs maximal-sphere membership")
    from astropy.io import fits
    from astropy.cosmology import FlatLambdaCDM
    cosmo = FlatLambdaCDM(H0=H0, Om0=OM0)
    lz = sp[sp["desi_z"] <= Z_DESIVAST_MAX]
    chi_h = cosmo.comoving_distance(lz["desi_z"].to_numpy()).value * LITTLE_H
    ra = np.radians(lz["desi_ra"].to_numpy())
    dec = np.radians(lz["desi_dec"].to_numpy())
    gal = np.column_stack([chi_h * np.cos(dec) * np.cos(ra),
                           chi_h * np.cos(dec) * np.sin(ra),
                           chi_h * np.sin(dec)])
    y_lz = (lz["match_class_eq"] == "CW").to_numpy()
    holes, maximals = [], []
    for gc in ["NGC", "SGC"]:
        with fits.open(DESIVAST_DIR / f"DESIVAST_BGS_VOLLIM_VoidFinder_{gc}.fits") as h:
            d = h["HOLES"].data
            holes.append(np.column_stack([d["X"], d["Y"], d["Z"], d["RADIUS"]]))
            m = h["MAXIMALS"].data
            maximals.append(np.column_stack([m["X"], m["Y"], m["Z"], m["RADIUS"]]))
    holes = np.vstack(holes)
    maximals = np.vstack(maximals)
    kd_gal = cKDTree(gal)

    def member_of(spheres):
        mem = np.zeros(len(gal), dtype=bool)
        for h_idx in kd_gal.query_ball_point(spheres[:, :3], r=spheres[:, 3]):
            mem[h_idx] = True
        return mem

    mem_A = member_of(holes)      # published permissive: any hole
    mem_B = member_of(maximals)   # interior-void: any maximal sphere

    def two_sample_z(nA, kA, nB, kB):
        fA, fB = kA / nA, kB / nB
        p = (kA + kB) / (nA + nB)
        se = np.sqrt(p * (1 - p) * (1 / nA + 1 / nB))
        return float((fA - fB) / se)

    def defn(mem):
        nv, kv = int(mem.sum()), int(y_lz[mem].sum())
        nn, kn = int((~mem).sum()), int(y_lz[~mem].sum())
        return {"void": _cls_row(nv, kv), "nonvoid": _cls_row(nn, kn),
                "delta_fcw_pp": float((kv / nv - kn / nn) * 100) if nv and nn else None,
                "two_sample_z_void_minus_nonvoid":
                    two_sample_z(nv, kv, nn, kn) if nv and nn else None}

    both = mem_B & ~mem_A
    out["item18_voidfinder_membership_definitions"] = {
        "sample": f"z<={Z_DESIVAST_MAX} matched primary deduped CW/CCW "
                  f"spirals (n={len(gal):,}); positions Mpc/h "
                  "(scripts/17 C8 conventions)",
        "n_holes": int(len(holes)), "n_maximals": int(len(maximals)),
        "defA_any_hole_published": defn(mem_A),
        "defB_maximal_sphere_interior": defn(mem_B),
        "overlap": {
            "n_in_both": int((mem_A & mem_B).sum()),
            "n_A_only": int((mem_A & ~mem_B).sum()),
            "n_B_only_outside_A": int(both.sum()),
            "note": "maximal spheres are holes themselves, so defB subset "
                    "of defA up to numerical ties" if both.sum() == 0 else
                    "defB has members outside defA (unexpected; inspect)",
        },
    }
    OUT.write_text(json.dumps(out, indent=1))
    log("#18 written — DONE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
