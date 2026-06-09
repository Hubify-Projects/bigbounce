#!/usr/bin/env python3
"""P5 v0.1.51 wave computes C3 + C4 (R22prov truth-audit).

C3 / META-M2 — stratified label-shuffle nulls. The paper's permutation nulls
    shuffle CW/CCW labels freely; given the per-leg / per-program residual
    structure the paper itself reports, a stratified shuffle (labels permuted
    only WITHIN imaging-leg x DESI-program strata) is the conservative null.
    Re-runs the headline scans' max-|sigma_from_half| statistics under both
    nulls: V-Web env classes (superset parent), redshift quintiles, and
    HEALPix NSIDE in {16,32,64} (full catalog parent, min 200 spirals/pixel,
    matching tab:healpix). Permutation draws are exact stratified
    multivariate-hypergeometric label re-assignments.

C4 / META-M3 — parent-tracer projected-density proxy. The paper's k=5 NN
    density proxy is computed among spirals only (endogenous). Recompute the
    proxy as the angular distance to the 5th-nearest matched primary galaxy
    (all 2,232,212 deduped primaries, any chirality class), re-bin the
    chirality-relevant spirals into quintiles of that exogenous proxy, and
    re-run the per-quintile sigma_obs / sigma_pred residual table.

Output: pipelines/p5_desi_chirality/outputs/18_v0151_stratified_and_density.json
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import healpy as hp
import numpy as np
import pandas as pd
from scipy.spatial import cKDTree

P5 = Path(__file__).resolve().parents[1]
MATCHED = P5 / "results/p5_matched_chirality_desi.parquet"
ENV_VWEB = P5 / "data/desi_env/desi_env_vweb.parquet"
OUT = P5 / "outputs/18_v0151_stratified_and_density.json"

ENV_ORDER = ["void", "wall", "filament", "cluster"]
SEED = 20260515
N_MC = 1000
DF_CW_P4 = -0.0026


def _sig(k, n):
    n = np.asarray(n, float)
    return (np.asarray(k, float) - 0.5 * n) / (0.5 * np.sqrt(n))


def perm_pvals(bin_ids: np.ndarray, strata_ids: np.ndarray, y: np.ndarray,
               rng: np.random.Generator, n_mc: int = N_MC) -> dict:
    """Max-|sigma_from_half| over bins: free vs stratified label-shuffle p."""
    bins, bin_inv = np.unique(bin_ids, return_inverse=True)
    n_b = np.bincount(bin_inv)
    k_b = np.bincount(bin_inv, weights=y)
    obs = float(np.max(np.abs(_sig(k_b, n_b))))

    # free shuffle: multivariate hypergeometric across bins
    draws = rng.multivariate_hypergeometric(n_b.astype(int), int(y.sum()),
                                            size=n_mc)
    null_free = np.max(np.abs(_sig(draws, n_b)), axis=1)
    p_free = float((1 + (null_free >= obs).sum()) / (1 + n_mc))

    # stratified shuffle: within each stratum, distribute that stratum's CW
    # count across bins by the stratum's bin occupancy (exact MVH), then sum.
    strata, s_inv = np.unique(strata_ids, return_inverse=True)
    null_strat = np.zeros((n_mc, len(bins)))
    for si in range(len(strata)):
        m = s_inv == si
        n_sb = np.bincount(bin_inv[m], minlength=len(bins))
        k_s = int(y[m].sum())
        if k_s == 0 or n_sb.sum() == 0:
            continue
        nz = n_sb > 0
        d = rng.multivariate_hypergeometric(n_sb[nz].astype(int), k_s,
                                            size=n_mc)
        null_strat[:, nz] += d
    null_s = np.max(np.abs(_sig(null_strat, n_b)), axis=1)
    p_strat = float((1 + (null_s >= obs).sum()) / (1 + n_mc))
    return {"n_bins": int(len(bins)), "obs_max_abs_sigma": obs,
            "p_free_shuffle": p_free, "p_stratified_shuffle": p_strat}


def main() -> int:
    t0 = time.time()
    rng = np.random.default_rng(SEED)
    out = {"written_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
           "script": "scripts/18_v0151_stratified_and_density.py",
           "closes": ["META-M2(C3)", "META-M3(C4)"],
           "seed": SEED, "n_mc": N_MC}

    cols = ["desi_targetid", "match_class_eq", "desi_program", "desi_z",
            "desi_ra", "desi_dec", "matched_primary_deduped",
            "match_imaging_leg"]
    matched = pd.read_parquet(MATCHED, columns=cols)
    prim = matched[matched["matched_primary_deduped"]].copy()
    del matched
    sp = prim[prim["match_class_eq"].isin(["CW", "CCW"])].copy()
    y = (sp["match_class_eq"] == "CW").to_numpy(float)
    strata = (sp["match_imaging_leg"].astype(str) + "|"
              + sp["desi_program"].astype(str)).to_numpy()
    out["n_primaries"] = int(len(prim))
    out["n_spirals"] = int(len(sp))
    out["n_strata"] = int(len(np.unique(strata)))

    # ---- C3a: V-Web env classes (superset join parent) ----
    env = pd.read_parquet(ENV_VWEB, columns=["TARGETID", "env_class"])
    j = sp.merge(env, left_on="desi_targetid", right_on="TARGETID",
                 how="inner")
    del env
    yj = (j["match_class_eq"] == "CW").to_numpy(float)
    sj = (j["match_imaging_leg"].astype(str) + "|"
          + j["desi_program"].astype(str)).to_numpy()
    out["C3_env_class"] = perm_pvals(j["env_class"].to_numpy(), sj, yj, rng)

    # ---- C3b: redshift quintiles (catalog parent) ----
    zq = pd.qcut(sp["desi_z"], 5, labels=False).to_numpy()
    out["C3_z_quintiles"] = perm_pvals(zq, strata, y, rng)

    # ---- C3c: HEALPix scans at min {50, 200} spirals/pixel ----
    for thr in (50, 200):
        c3c = {}
        for nside in (16, 32, 64):
            pix = hp.ang2pix(nside, sp["desi_ra"].to_numpy(),
                             sp["desi_dec"].to_numpy(), lonlat=True)
            counts = pd.Series(pix).value_counts()
            keep = counts[counts >= thr].index
            m = np.isin(pix, keep)
            c3c[f"nside_{nside}"] = perm_pvals(pix[m], strata[m], y[m], rng)
        out[f"C3_healpix_min{thr}"] = c3c

    # ---- C4: exogenous k=5 NN density proxy on all matched primaries ----
    def unit_xyz(ra, dec):
        ra, dec = np.radians(ra), np.radians(dec)
        return np.column_stack([np.cos(dec) * np.cos(ra),
                                np.cos(dec) * np.sin(ra), np.sin(dec)])

    xyz_all = unit_xyz(prim["desi_ra"].to_numpy(), prim["desi_dec"].to_numpy())
    kd = cKDTree(xyz_all)
    xyz_sp = unit_xyz(sp["desi_ra"].to_numpy(), sp["desi_dec"].to_numpy())
    # spirals are members of the primary set -> 6th neighbour = 5th other
    d, _ = kd.query(xyz_sp, k=6, workers=-1)
    ang5 = 2.0 * np.arcsin(np.clip(d[:, 5] / 2.0, 0, 1))
    q = pd.qcut(ang5, 5, labels=False)  # quintile 0 = smallest separation
    # NOTE: smallest k-NN separation = HIGHEST density; report in density
    # order (1 = lowest density = largest separation) to match Table III.
    dens_quint = 4 - q
    rows = {}
    for qi in range(5):
        m = dens_quint == qi
        n = int(m.sum())
        k = int(y[m].sum())
        s_obs = float(_sig(k, n))
        s_pred = float(2 * DF_CW_P4 * np.sqrt(n))
        rows[f"Q{qi+1}_lowest_density_first"] = {
            "n": n, "n_cw": k, "cw_fraction": k / n,
            "sigma_obs": s_obs, "sigma_pred": s_pred,
            "abs_residual": abs(s_obs - s_pred),
        }
    out["C4_density_quintiles_parent_tracer"] = {
        "proxy": ("angular distance to 5th-nearest matched primary "
                  "(n=%d, any chirality class); quintiles on spirals"
                  % len(prim)),
        "rows": rows,
        "max_abs_sigma_obs": float(max(abs(r["sigma_obs"])
                                       for r in rows.values())),
        "max_abs_residual": float(max(r["abs_residual"]
                                      for r in rows.values())),
    }

    out["runtime_seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=2))
    print(f"[done] wrote {OUT} in {out['runtime_seconds']}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
