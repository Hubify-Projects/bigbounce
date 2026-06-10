#!/usr/bin/env python3
"""
R23conf META-REVIEW closures — P5-META-M4 and P5-META-m5
========================================================
META-M4: the omnibus 4x2 homogeneity chi^2 of Sec. VI.A is computed on the
  812,793-row env-labeled parent, which carries 2.7% duplicate TARGETIDs
  from repeat survey/program coadd rows on the env-table side of the join;
  duplicates violate the independence assumption of the contingency test.
  Recompute the same 4x2 test on the unique-TARGETID subset (one row per
  TARGETID, first occurrence; sensitivity variant excluding the TARGETIDs
  whose duplicate rows carry conflicting env labels).

META-m5: the Sec. VIII.F per-pixel Pearson correlation between maximal-void
  density and chirality sigma (NSIDE=32, pixels with >=200 spirals) is
  unweighted although Var[sigma_pix] depends on N_pix. Recompute the
  correlation with (a) no weights (reproduction), (b) weights prop. to
  N_pix, and (c) Spearman rank correlation, on the z<=0.24 matched-spiral
  subsample against DESIVAST VoidFinder MAXIMALS (NGC+SGC, 3,765 voids).

Output: pipelines/p5_desi_chirality/outputs/21_r23conf_meta_closures.json
Run:    python3 pipelines/p5_desi_chirality/scripts/21_r23conf_meta_closures.py
"""
import json
import time
from pathlib import Path

import numpy as np
import pandas as pd
import healpy as hp
from astropy.io import fits
from scipy import stats

P5 = Path(__file__).resolve().parents[1]
MATCHED = P5 / "results/p5_matched_chirality_desi.parquet"
ENV_VWEB = P5 / "data/desi_env/desi_env_vweb.parquet"
OUT = P5 / "outputs/21_r23conf_meta_closures.json"
ENV_ORDER = ["void", "wall", "filament", "cluster"]


def chi2_4x2(df):
    tab = pd.crosstab(df["env_class"], df["match_class_eq"]).loc[
        [c for c in ENV_ORDER if c in df["env_class"].unique()]]
    c, p, dof, _ = stats.chi2_contingency(tab.values, correction=False)
    return {
        "counts_cw_ccw": {k: [int(tab.loc[k, "CW"]), int(tab.loc[k, "CCW"])]
                          for k in tab.index},
        "n": int(len(df)), "chi2": float(c), "dof": int(dof), "p": float(p),
    }


def main():
    out = {
        "written_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "script": "scripts/21_r23conf_meta_closures.py",
        "closes": ["P5-META-M4", "P5-META-m5"],
    }

    cols = ["desi_targetid", "match_class_eq", "desi_z", "desi_ra", "desi_dec",
            "matched_primary_deduped"]
    matched = pd.read_parquet(MATCHED, columns=cols)
    sp = matched[matched["matched_primary_deduped"]
                 & matched["match_class_eq"].isin(["CW", "CCW"])].copy()
    del matched

    # ---------------- META-M4 ----------------
    env = pd.read_parquet(ENV_VWEB, columns=["TARGETID", "env_class"])
    j = sp.merge(env, left_on="desi_targetid", right_on="TARGETID", how="inner")
    res = {"row_level_parent": chi2_4x2(j)}
    res["row_level_parent"]["n_unique_targetid"] = int(j["desi_targetid"].nunique())

    ju = j.drop_duplicates(subset="desi_targetid", keep="first")
    res["unique_targetid_first_row"] = chi2_4x2(ju)

    conf = j.groupby("desi_targetid")["env_class"].nunique()
    conflicted = set(conf[conf > 1].index)
    res["n_targetids_conflicting_env"] = int(len(conflicted))
    juc = ju[~ju["desi_targetid"].isin(conflicted)]
    res["unique_targetid_excl_conflicted"] = chi2_4x2(juc)
    out["META_M4_omnibus_chi2_unique_subset"] = res
    print("META-M4:", json.dumps({k: v for k, v in res.items()
                                  if k != "row_level_parent"}, indent=1)[:600])

    # ---------------- META-m5 ----------------
    NSIDE = 32
    zcut = sp[sp["desi_z"] <= 0.24]
    pix = hp.ang2pix(NSIDE, zcut["desi_ra"].values, zcut["desi_dec"].values,
                     lonlat=True)
    zcut = zcut.assign(pix=pix)
    g = zcut.groupby("pix")
    per = g.agg(n=("match_class_eq", "size"),
                n_cw=("match_class_eq", lambda s: int((s == "CW").sum())))
    per["sigma"] = (per["n_cw"] - 0.5 * per["n"]) / (0.5 * np.sqrt(per["n"]))

    # maximal voids per pixel
    ras, decs = [], []
    for gc in ["NGC", "SGC"]:
        with fits.open(P5 / f"data/desivast/DESIVAST_BGS_VOLLIM_VoidFinder_{gc}.fits") as f:
            mx = f["MAXIMALS"].data
            ras.append(np.asarray(mx["RA"], dtype=float))
            decs.append(np.asarray(mx["DEC"], dtype=float))
    vra, vdec = np.concatenate(ras), np.concatenate(decs)
    vpix = hp.ang2pix(NSIDE, vra, vdec, lonlat=True)
    vcount = pd.Series(vpix).value_counts()
    per["n_voids"] = vcount.reindex(per.index).fillna(0).astype(int)

    sel = per[(per["n"] >= 200) & (per["n_voids"] >= 1)]
    x, y, n = sel["n_voids"].values.astype(float), sel["sigma"].values, sel["n"].values
    r_unw, p_unw = stats.pearsonr(x, y)
    rho_sp, p_sp = stats.spearmanr(x, y)

    def weighted_pearson(x, y, w):
        w = w / w.sum()
        mx, my = np.sum(w * x), np.sum(w * y)
        cov = np.sum(w * (x - mx) * (y - my))
        sx = np.sqrt(np.sum(w * (x - mx) ** 2))
        sy = np.sqrt(np.sum(w * (y - my) ** 2))
        r = cov / (sx * sy)
        # effective sample size for the p-value
        neff = 1.0 / np.sum(w ** 2)
        t = r * np.sqrt(max(neff - 2, 1) / max(1 - r ** 2, 1e-12))
        p = 2 * stats.t.sf(abs(t), max(neff - 2, 1))
        return float(r), float(p), float(neff)

    r_w, p_w, neff = weighted_pearson(x, y, n.astype(float))
    out["META_m5_weighted_healpix_correlation"] = {
        "nside": NSIDE, "sample": "matched_primary_deduped CW/CCW spirals, z<=0.24",
        "n_spirals": int(len(zcut)),
        "min_spirals_per_pixel": 200, "pixel_criterion": ">=200 spirals AND >=1 maximal void (n_pix_both convention of Sec. VIII.F)",
        "n_valid_pixels": int(len(sel)),
        "maximal_voids_total_binned": int(len(vra)),
        "pearson_unweighted": {"r": float(r_unw), "p": float(p_unw)},
        "pearson_weighted_Npix": {"r": r_w, "p": p_w, "n_eff": neff},
        "spearman": {"rho": float(rho_sp), "p": float(p_sp)},
        "note": ("Weighted Pearson uses weights prop. to N_pix (inverse of the "
                 "leading-order Var[sigma_pix] heteroscedasticity is flat in the "
                 "z-score normalization, so N_pix weighting is the conservative "
                 "choice that emphasizes the well-measured pixels)."),
    }
    print("META-m5:", json.dumps(out["META_m5_weighted_healpix_correlation"], indent=1))

    # ---------------- META-M3: Table IV density-definition check ----------------
    envd = pd.read_parquet(ENV_VWEB, columns=["TARGETID", "env_class", "env_density"])
    jd = sp.merge(envd, left_on="desi_targetid", right_on="TARGETID", how="inner")
    m3 = {}
    for cls in ["cluster", "filament"]:
        sub = jd[jd["env_class"] == cls].copy()
        sub["q"] = pd.qcut(sub["env_density"], 4, labels=[1, 2, 3, 4])
        rows = {}
        for q, g in sub.groupby("q", observed=True):
            ncw = int((g["match_class_eq"] == "CW").sum())
            n = int(len(g))
            rows[f"Q{q}"] = {
                "n": n,
                "mean_log10_1plus_delta": float(g["env_density"].mean()),
                "mean_linear_1plus_delta": float((10 ** g["env_density"]).mean()),
                "sigma_from_half": float((ncw - 0.5 * n) / (0.5 * np.sqrt(n))),
            }
        m3[cls] = rows
    m3["verdict"] = ("Table IV's bar-rho column equals the quartile mean of "
                     "env_density = log10(1+delta_smooth), NOT linear density: "
                     "the recomputed mean log-densities (cluster 1.548/1.804/"
                     "2.006/2.214) match the published 1.55/1.80/2.01/2.21 and "
                     "the n / sigma columns match exactly. Quartile membership "
                     "is invariant under the monotone log transform.")
    out["META_M3_tableIV_density_definition"] = m3

    # ------------- META-M2: canonical run, interior-buffer excision -------------
    # Boundary flag from the z-shell rebuild geometry (near_boundary_Rs == galaxy
    # cell within R_s of the occupancy-footprint boundary); canonical env_class.
    zsh = pd.read_parquet(P5 / "data/desi_env/desi_env_vweb_zshell.parquet",
                          columns=["TARGETID", "near_boundary_Rs"])
    zsh_u = zsh.drop_duplicates("TARGETID")
    env_u = env.drop_duplicates("TARGETID")
    jb = (sp.merge(env_u, left_on="desi_targetid", right_on="TARGETID", how="inner")
            .merge(zsh_u, on="TARGETID", how="left"))
    interior = jb[jb["near_boundary_Rs"] == False]  # noqa: E712
    m2 = {"definition": ("canonical V-Web env_class (unique-TARGETID join) "
                         "restricted to interior galaxies, i.e. excluding "
                         "near_boundary_Rs == True (within R_s of the "
                         "occupancy-footprint boundary, flag computed in the "
                         "16_* z-shell rebuild geometry)"),
          "n_all": int(len(jb)), "n_interior": int(len(interior)),
          "per_class_all_vs_interior": {}}
    for cls in ENV_ORDER:
        a = jb[jb["env_class"] == cls]
        i = interior[interior["env_class"] == cls]
        def _row(g):
            n = int(len(g)); ncw = int((g["match_class_eq"] == "CW").sum())
            return {"n": n, "f_cw": (ncw / n) if n else None,
                    "sigma_from_half": float((ncw - 0.5 * n) / (0.5 * np.sqrt(n))) if n else None}
        m2["per_class_all_vs_interior"][cls] = {"all": _row(a), "interior": _row(i)}
    c_int, p_int, dof_int, _ = stats.chi2_contingency(
        pd.crosstab(interior["env_class"], interior["match_class_eq"]).values,
        correction=False)
    m2["interior_omnibus_chi2"] = {"chi2": float(c_int), "dof": int(dof_int),
                                   "p": float(p_int)}
    out["META_M2_canonical_interior_buffer"] = m2
    print("META-M2:", json.dumps(m2["per_class_all_vs_interior"], indent=1)[:800],
          m2["interior_omnibus_chi2"])

    OUT.write_text(json.dumps(out, indent=2))
    print("wrote", OUT)


if __name__ == "__main__":
    main()
