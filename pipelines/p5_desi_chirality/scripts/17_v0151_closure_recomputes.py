#!/usr/bin/env python3
"""P5 v0.1.51 closure-wave recomputes (R22prov truth-audit work order).

Items covered (audit IDs in project-context/peer-reviews/R22prov_P5_TRUTH_AUDIT.md):

  T2 / OAI-E6 + OAI-E2 + OAI-m17  — bright/dark per-V-Web-class split recomputed on
      ONE declared parent: the env-labeled superset (matched_primary_deduped CW/CCW
      spirals inner-joined to desi_env_vweb.parquet; n = 812,793). The prior
      filament decomposition artifact mixed parents (filament bright 416,701 >
      class total 408,187). Includes per-class bright-vs-dark two-sample z and
      the 4x2 class-x-program contingency chi^2 on the same parent.
  C1 / META-M6 — omnibus 4x2 homogeneity chi^2 (CW/CCW x class) from the exact
      counts in outputs/16_cosmic_web_zshell_corrected.json (canonical + z-shell).
  C2 / OAI-E3 — Tempel filament concordance recomputed on the Tempel-overlap
      sample only (V-Web side restricted to the same overlap galaxies).
  C8 / OAI-M7 — KDTree k=20 sufficiency guard for the DESIVAST point-in-sphere
      membership test + full (k-unbounded) membership recompute. This section
      also serves as the committed DESIVAST membership driver (Perpl-m3 /
      META-E3): galaxy Mpc -> Mpc/h conversion is explicit below.
  T4 / OAI-E1 — Phase-2 sweep recomputed on the declared matched-spiral parent
      (the archived sweep CSV used the un-filtered nearest-label join,
      n_cw+n_ccw = 5,571,152 rows incl. duplicates/non-primary; recomputed here
      on the deduped chirality-relevant parent joined per sweep cell).
  META-E1 diagnosis — empirical decomposition of the 812,793 vs 791,635 parent
      difference (duplicate TARGETID rows on the env side of the join).

Output: pipelines/p5_desi_chirality/outputs/17_v0151_closure_recomputes.json
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats
from scipy.spatial import cKDTree

P5 = Path(__file__).resolve().parents[1]
MATCHED = P5 / "results/p5_matched_chirality_desi.parquet"
ENV_VWEB = P5 / "data/desi_env/desi_env_vweb.parquet"
TEMPEL = P5 / "data/desi_env/tempel/tempel_2014_fof.parquet"
ZSHELL_JSON = P5 / "outputs/16_cosmic_web_zshell_corrected.json"
SWEEP_DIR = P5 / "data/desi_env/phase2_sweep"
DESIVAST_DIR = P5 / "data/desivast"
OUT = P5 / "outputs/17_v0151_closure_recomputes.json"

ENV_ORDER = ["void", "wall", "filament", "cluster"]

# DESIVAST-analysis cosmology (tex \S sec:desivast_xmatch): flat LCDM,
# H0 = 67.66 km/s/Mpc, Om = 0.315; positions in h^-1 Mpc to match the
# DESIVAST hole catalog X/Y/Z convention.
H0, OM0, LITTLE_H = 67.66, 0.315, 0.6766
Z_DESIVAST_MAX = 0.24


def _sig(n_cw: int, n: int) -> float:
    return float((n_cw - 0.5 * n) / (0.5 * np.sqrt(n))) if n else float("nan")


def _cls_row(sub: pd.DataFrame) -> dict:
    n = int(len(sub))
    n_cw = int((sub["match_class_eq"] == "CW").sum())
    return {
        "n": n,
        "n_cw": n_cw,
        "cw_fraction": (n_cw / n) if n else None,
        "sigma_from_half": _sig(n_cw, n),
    }


def two_sample_z(n1, k1, n2, k2) -> float:
    """Two-proportion pooled z (f1 - f2)."""
    f1, f2 = k1 / n1, k2 / n2
    p = (k1 + k2) / (n1 + n2)
    se = np.sqrt(p * (1 - p) * (1 / n1 + 1 / n2))
    return float((f1 - f2) / se)


def main() -> int:
    t0 = time.time()
    out: dict = {
        "written_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "script": "scripts/17_v0151_closure_recomputes.py",
        "closes": [
            "OAI-E6", "OAI-E2", "OAI-m17", "OAI-M4", "META-M6", "META-M1",
            "META-m4", "OAI-E3", "OAI-m7", "OAI-M7", "OAI-E1", "META-E1(diag)",
            "Perpl-m3(driver)", "META-E3(driver-unit-doc)",
        ],
    }

    cols = ["desi_targetid", "match_class_eq", "desi_program", "desi_z",
            "desi_ra", "desi_dec", "matched_primary_deduped", "match_confidence"]
    matched = pd.read_parquet(MATCHED, columns=cols)
    sp = matched[matched["matched_primary_deduped"]
                 & matched["match_class_eq"].isin(["CW", "CCW"])].copy()
    del matched
    out["parent_catalog_matched"] = {
        "definition": "matched_primary_deduped & match_class_eq in {CW,CCW}",
        "n_rows": int(len(sp)),
        "n_unique_targetid": int(sp["desi_targetid"].nunique()),
        "program_split": {
            str(k): _cls_row(v) for k, v in sp.groupby("desi_program")
        },
    }

    # ---- env join: declared superset parent (META-E1 diagnosis) ----
    env = pd.read_parquet(ENV_VWEB, columns=["TARGETID", "env_class"])
    n_env_rows = len(env)
    n_env_unique = env["TARGETID"].nunique()
    j = sp.merge(env, left_on="desi_targetid", right_on="TARGETID", how="inner")
    dup_consistent = int(
        j.groupby("desi_targetid")["env_class"].nunique().gt(1).sum()
    )
    out["parent_env_superset"] = {
        "definition": ("parent_catalog_matched inner-joined to desi_env_vweb "
                       "on TARGETID (join is 1-to-many: the env table carries "
                       "duplicate TARGETIDs from repeat zall survey/program "
                       "coadd rows)"),
        "env_table_rows": int(n_env_rows),
        "env_table_unique_targetid": int(n_env_unique),
        "n_rows": int(len(j)),
        "n_unique_targetid": int(j["desi_targetid"].nunique()),
        "excess_rows_over_catalog_parent": int(len(j) - len(sp)),
        "n_targetids_with_conflicting_env_class": dup_consistent,
        "per_class": {c: _cls_row(j[j["env_class"] == c]) for c in ENV_ORDER},
        "ALL": _cls_row(j),
    }

    # ---- T2: bright/dark per class on the declared superset parent ----
    t2 = {}
    for c in ENV_ORDER:
        sub = j[j["env_class"] == c]
        progs = {str(k): _cls_row(v) for k, v in sub.groupby("desi_program")}
        b, d = sub[sub["desi_program"] == "bright"], sub[sub["desi_program"] == "dark"]
        z_bd = two_sample_z(len(b), (b["match_class_eq"] == "CW").sum(),
                            len(d), (d["match_class_eq"] == "CW").sum()) \
            if len(b) and len(d) else None
        t2[c] = {"class_total": int(len(sub)), "by_program": progs,
                 "sum_over_programs": int(sum(p["n"] for p in progs.values())),
                 "bright_vs_dark_two_sample_z": z_bd}
    out["T2_bright_dark_per_class_superset"] = t2

    # contingency chi2 class x bright/dark on the same parent
    bd = j[j["desi_program"].isin(["bright", "dark"])]
    ct = pd.crosstab(bd["env_class"], bd["desi_program"]).loc[ENV_ORDER]
    chi2, p, dof, _ = stats.chi2_contingency(ct)
    bright_frac = (ct["bright"] / ct.sum(axis=1))
    out["T2_contingency_class_x_program"] = {
        "n_bright_plus_dark": int(len(bd)),
        "table": ct.to_dict(),
        "chi2": float(chi2), "dof": int(dof), "p": float(p),
        "log10_p": float(np.log10(p)) if p > 0 else "<-300 (underflow)",
        "per_class_bright_fraction": {k: float(v) for k, v in bright_frac.items()},
        "overall_bright_fraction": float(ct["bright"].sum() / len(bd)),
    }

    # ---- C1: omnibus 4x2 homogeneity chi2 from the 16_* artifact counts ----
    art = json.loads(ZSHELL_JSON.read_text())
    omni = {}
    for key in ["canonical_recomputed", "zshell_corrected"]:
        rows = [r for r in art["cw_fraction_by_env"][key] if r["env_class"] != "ALL"]
        tab = np.array([[r["n_cw"], r["n_ccw"]] for r in rows])
        chi2, p, dof, _ = stats.chi2_contingency(tab)
        omni[key] = {
            "counts": {r["env_class"]: [r["n_cw"], r["n_ccw"]] for r in rows},
            "chi2": float(chi2), "dof": int(dof), "p": float(p),
        }
    out["C1_omnibus_chi2"] = omni

    # ---- C2: Tempel concordance on the overlap sample only ----
    from astropy.coordinates import SkyCoord
    import astropy.units as u
    tp = pd.read_parquet(TEMPEL)
    mult_col = "multiplicity" if "multiplicity" in tp.columns else None
    c_sp = SkyCoord(sp["desi_ra"].to_numpy() * u.deg, sp["desi_dec"].to_numpy() * u.deg)
    c_tp = SkyCoord(tp["ra"].to_numpy() * u.deg, tp["dec"].to_numpy() * u.deg)
    idx, sep, _ = c_sp.match_to_catalog_sky(c_tp)
    ov = sp[sep.arcsec <= 1.0].copy()
    ov["multiplicity"] = tp[mult_col].to_numpy()[idx[sep.arcsec <= 1.0]]

    def tempel_class(m):
        if m == 1:
            return "isolated"
        if m < 5:
            return "small_group"
        if m < 20:
            return "filament_like"
        return "cluster_like"

    ov["tempel_class"] = ov["multiplicity"].map(tempel_class)
    # V-Web label for the SAME overlap galaxies (dedup env to unique TARGETID;
    # duplicate rows carry identical env_class per the diagnosis above)
    env_u = env.drop_duplicates("TARGETID")
    ov = ov.merge(env_u, left_on="desi_targetid", right_on="TARGETID", how="left")
    pairing = {"isolated": "void", "small_group": "wall",
               "filament_like": "filament", "cluster_like": "cluster"}
    c2 = {"n_overlap": int(len(ov)), "pairs": {}}
    for tcls, vcls in pairing.items():
        a = _cls_row(ov[ov["tempel_class"] == tcls])
        b = _cls_row(ov[ov["env_class"] == vcls])
        c2["pairs"][f"{tcls}_vs_{vcls}"] = {
            "tempel_on_overlap": a, "vweb_on_overlap": b,
            "concordance_pp": (abs(a["cw_fraction"] - b["cw_fraction"]) * 100
                               if a["n"] and b["n"] else None),
        }
    out["C2_tempel_overlap_concordance"] = c2

    # ---- C8: DESIVAST membership driver + KDTree k-sufficiency guard ----
    from astropy.io import fits
    from astropy.cosmology import FlatLambdaCDM
    cosmo = FlatLambdaCDM(H0=H0, Om0=OM0)
    lz = sp[sp["desi_z"] <= Z_DESIVAST_MAX]
    # Explicit unit documentation (META-E3): astropy comoving_distance returns
    # Mpc; multiply by h = H0/100 to convert to h^-1 Mpc (DESIVAST X/Y/Z units).
    chi_h = cosmo.comoving_distance(lz["desi_z"].to_numpy()).value * LITTLE_H
    ra, dec = np.radians(lz["desi_ra"].to_numpy()), np.radians(lz["desi_dec"].to_numpy())
    gal = np.column_stack([chi_h * np.cos(dec) * np.cos(ra),
                           chi_h * np.cos(dec) * np.sin(ra),
                           chi_h * np.sin(dec)])
    holes = []
    for gc in ["NGC", "SGC"]:
        with fits.open(DESIVAST_DIR / f"DESIVAST_BGS_VOLLIM_VoidFinder_{gc}.fits") as h:
            d = h["HOLES"].data
            holes.append(np.column_stack([d["X"], d["Y"], d["Z"], d["RADIUS"]]))
    holes = np.vstack(holes)
    r_max = float(holes[:, 3].max())
    kd_holes = cKDTree(holes[:, :3])
    cand_counts = kd_holes.query_ball_point(gal, r=r_max, return_length=True)
    # exact (k-unbounded) membership: per-hole radius query on galaxy tree
    kd_gal = cKDTree(gal)
    member = np.zeros(len(gal), dtype=bool)
    hits = kd_gal.query_ball_point(holes[:, :3], r=holes[:, 3])
    for h_idx in hits:
        member[h_idx] = True
    sanity_z02 = float(cosmo.comoving_distance(0.2).value * LITTLE_H)
    lz_void = lz[member]
    out["C8_desivast_kdtree_guard"] = {
        "n_lz": int(len(lz)),
        "n_holes": int(len(holes)),
        "max_hole_radius_mpc_h": r_max,
        "chi_z0p2_mpc_h_sanity": sanity_z02,
        "max_candidate_holes_within_rmax": int(cand_counts.max()),
        "n_galaxies_gt20_candidates": int((cand_counts > 20).sum()),
        "frac_galaxies_gt20_candidates": float((cand_counts > 20).mean()),
        "n_void_exact_recompute": int(member.sum()),
        "n_nonvoid_exact_recompute": int((~member).sum()),
        "void_class": _cls_row(lz_void),
        "nonvoid_class": _cls_row(lz[~member]),
    }

    # ---- T4: Phase-2 sweep recompute on the declared catalog parent ----
    sweep = {}
    for pq in sorted(SWEEP_DIR.glob("desi_env_vweb_*.parquet")):
        cell = pq.stem.replace("desi_env_vweb_", "")
        e = pd.read_parquet(pq, columns=["TARGETID", "env_class"])
        jj = sp.merge(e, left_on="desi_targetid", right_on="TARGETID", how="inner")
        per = {c: _cls_row(jj[jj["env_class"] == c]) for c in ENV_ORDER}
        fr = [per[c]["cw_fraction"] for c in ENV_ORDER if per[c]["n"]]
        sweep[cell] = {"per_class": per, "n_total": int(len(jj)),
                       "range_pp": float((max(fr) - min(fr)) * 100)}
        del e, jj
    out["T4_phase2_sweep_on_catalog_parent"] = {
        "parent": "parent_catalog_matched joined per sweep cell (superset join, "
                  "same convention as canonical Table II)",
        "cells": sweep,
        "max_range_pp": float(max(v["range_pp"] for v in sweep.values())),
        "archived_sweep_basis_note": (
            "env_finder/reports/02_phase2_sweep.csv was computed without the "
            "matched_primary_deduped/acceptance filter (5,571,152 CW/CCW rows "
            "incl. duplicate & non-primary nearest-label rows); superseded by "
            "this recompute."),
    }

    # ---- T4b: per-cell label-shuffle max-|sigma| p on the recomputed sweep ----
    rng = np.random.default_rng(20260515)
    n_mc = 1000
    t4b = {}
    for cell, v in sweep.items():
        ns = np.array([v["per_class"][c]["n"] for c in ENV_ORDER])
        kcw = np.array([v["per_class"][c]["n_cw"] for c in ENV_ORDER])
        obs = np.max(np.abs((kcw - 0.5 * ns) / (0.5 * np.sqrt(ns))))
        k_tot = int(kcw.sum())
        draws = rng.multivariate_hypergeometric(ns, k_tot, size=n_mc)
        null = np.max(np.abs((draws - 0.5 * ns) / (0.5 * np.sqrt(ns))), axis=1)
        t4b[cell] = {"obs_max_abs_sigma": float(obs),
                     "p_lee": float((1 + (null >= obs).sum()) / (1 + n_mc))}
    out["T4b_sweep_label_shuffle_p"] = {
        "n_mc": n_mc, "seed": 20260515,
        "note": ("Label-shuffle preserves the total CW count, so the catalog "
                 "monopole is in both observed and null max-|sigma|."),
        "cells": t4b,
        "p_range": [min(x["p_lee"] for x in t4b.values()),
                    max(x["p_lee"] for x in t4b.values())],
    }

    # ---- catalog-level bright-vs-dark two-sample z (for the sec:systematics table) ----
    pb = out["parent_catalog_matched"]["program_split"]
    out["catalog_bright_vs_dark_z"] = two_sample_z(
        pb["bright"]["n"], pb["bright"]["n_cw"], pb["dark"]["n"], pb["dark"]["n_cw"])

    # ---- META-m3: logistic regression with SEs (IRLS, no statsmodels dep) ----
    y = (sp["match_class_eq"] == "CW").to_numpy(float)
    X = np.column_stack([
        np.ones(len(sp)),
        sp["desi_z"].to_numpy(float),
        np.abs(np.sin(np.radians(sp["desi_dec"].to_numpy(float)))),
        np.cos(np.radians(sp["desi_ra"].to_numpy(float))),
        sp["match_confidence"].to_numpy(float),
    ])
    beta = np.zeros(X.shape[1])
    for _ in range(25):
        eta = X @ beta
        mu = 1.0 / (1.0 + np.exp(-eta))
        w = mu * (1 - mu)
        H = X.T @ (X * w[:, None])
        g = X.T @ (y - mu)
        step_v = np.linalg.solve(H, g)
        beta = beta + step_v
        if np.max(np.abs(step_v)) < 1e-10:
            break
    cov = np.linalg.inv(H)
    se = np.sqrt(np.diag(cov))
    names = ["intercept", "z", "abs_sin_dec", "cos_ra", "confidence"]
    out["META_m3_logistic_regression"] = {
        nm: {"coef": float(b), "se": float(s), "z": float(b / s),
             "p": float(2 * stats.norm.sf(abs(b / s)))}
        for nm, b, s in zip(names, beta, se)
    }

    # ---- OAI-m11: recover the '1,821 valid pixels' cut ----
    import healpy as hp
    m11 = {}
    for label, frame in [("catalog_791635", sp), ("superset_812793", j)]:
        pix = hp.ang2pix(32, frame["desi_ra"].to_numpy(),
                         frame["desi_dec"].to_numpy(), lonlat=True)
        counts = pd.Series(pix).value_counts()
        m11[label] = {f"min_{thr}": int((counts >= thr).sum())
                      for thr in (50, 100, 150, 200)}
    out["OAI_m11_nside32_pixel_counts"] = m11

    # per-pixel sigma_vs_monopole stats, NSIDE 32, >=200 spirals/pixel,
    # superset parent (traceable replacement for the unreproducible
    # 1,821-pixel statistic in p4_monopole_residual_analysis.json)
    f_mono = out["parent_env_superset"]["ALL"]["cw_fraction"]
    pix = hp.ang2pix(32, j["desi_ra"].to_numpy(), j["desi_dec"].to_numpy(),
                     lonlat=True)
    g = pd.DataFrame({"pix": pix, "cw": (j["match_class_eq"] == "CW")})
    agg = g.groupby("pix")["cw"].agg(["size", "sum"])
    agg = agg[agg["size"] >= 200]
    sig_pix = (agg["sum"] - f_mono * agg["size"]) / (0.5 * np.sqrt(agg["size"]))
    out["OAI_m11_residual_stats_min200_superset"] = {
        "nside": 32, "min_spirals_per_pixel": 200,
        "n_valid_pixels": int(len(agg)),
        "monopole_f_cw": float(f_mono),
        "mean": float(sig_pix.mean()), "std": float(sig_pix.std(ddof=0)),
        "skew": float(stats.skew(sig_pix)),
        "excess_kurtosis": float(stats.kurtosis(sig_pix)),
    }

    # ---- C7 / Grok-M3: grid-resolution convergence (N_grid 128/256/384) ----
    gc_dir = P5 / "data/desi_env/grid_convergence"
    c7 = {}
    for tag, pq_name in [("N128", "desi_env_vweb_R25_N128_L0.parquet"),
                         ("N384", "desi_env_vweb_R25_N384_L0.parquet")]:
        pq_path = gc_dir / pq_name
        if not pq_path.exists():
            c7[tag] = {"skipped": "parquet missing"}
            continue
        e = pd.read_parquet(pq_path, columns=["TARGETID", "env_class"])
        jj = sp.merge(e, left_on="desi_targetid", right_on="TARGETID",
                      how="inner")
        per = {c: _cls_row(jj[jj["env_class"] == c]) for c in ENV_ORDER}
        fr = [per[c]["cw_fraction"] for c in ENV_ORDER if per[c]["n"]]
        c7[tag] = {"per_class": per, "n_total": int(len(jj)),
                   "range_pp": float((max(fr) - min(fr)) * 100)}
        del e, jj
    c7["N256_canonical"] = {
        "per_class": out["parent_env_superset"]["per_class"],
        "n_total": out["parent_env_superset"]["n_rows"],
        "range_pp": float((max(v["cw_fraction"] for v in
                               out["parent_env_superset"]["per_class"].values())
                           - min(v["cw_fraction"] for v in
                                 out["parent_env_superset"]["per_class"].values()))
                          * 100),
    }
    out["C7_grid_convergence"] = {
        "config": "R_s=25 Mpc/h, lambda_th=0, canonical pipeline "
                  "(env_finder/01_compute_vweb.py), N_grid in {128,256,384}",
        "cells": c7,
    }

    out["runtime_seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=2))
    print(f"[done] wrote {OUT} in {out['runtime_seconds']}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
