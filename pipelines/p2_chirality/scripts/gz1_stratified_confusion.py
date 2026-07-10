#!/usr/bin/env python3
"""Stratified human-vs-classifier CW/CCW confusion matrix on the GZ1 overlap.

Motivation (referee item, P4 + P5)
----------------------------------
The recurring hardest reviewer item on P4 (chirality_catalog_paper.tex) and P5
(p5_desi_chirality.tex) is:

    "No confusion matrix for the science sample as a function of sky position /
     imaging leg (P4) or environment (P5). Differential classification error
     (CW->CCW vs CCW->CW mislabelling rates that vary across strata) could
     manufacture or erase the reported chirality signal."

The P4 GZ1-human-label overlap used for the independence check
(`outputs/gz1only_fullN_dipole_result.json`, N=46,017 matched) gives us, per
galaxy, BOTH a human CW/CCW label (Galaxy Zoo 1 Table 2 vote fractions,
Lintott+2011) AND the pipeline classifier label (`class_eq` from
`catalog_production.parquet`). That is exactly a labelled test set on which the
human-vs-classifier confusion matrix can be measured directly -- no model in the
label chain on the human side, so the two labels are independent.

This script builds that confusion matrix on the GZ1 overlap and STRATIFIES it by:

  (a) imaging leg / sky region:
        BASS+MzLS  (dec > +32 deg)   vs   DECaLS (dec < +32 deg)
      -- the exact P4 split (paper: "DR8 comprises BASS+MzLS (delta>+32),
         DECaLS (delta<+32), and a DES overlap region").
  (b) classifier confidence bin:  confidence_eq > 0.6  vs  <= 0.6
      (the paper's p_eq>0.6 / qc_flag==0 science cut vs below it).

For each stratum it reports:
  N, accuracy, CW->CCW error rate, CCW->CW error rate, the *asymmetry* of the two
  directional error rates (this is the quantity that can bias a CW/CCW fraction),
  and binomial 95% CIs (Wilson) on every rate.

It then runs two-proportion z-tests asking whether the CW/CCW error asymmetry
DIFFERS between the strata at a level that could produce the papers' bounds
(P4 A_p ~ 0.7 %; P5 Delta f_CW ~ 0.2-1 pp).

P5 environment (void / non-void) stratum
-----------------------------------------
The void/non-void split needs, per galaxy, (i) a redshift and (ii) DESIVAST
void-sphere membership. GZ1 Table 2 carries NO redshift, and the P5 matched
chirality x DESI-redshift parquet
(`pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet`) plus
the DESIVAST void-sphere catalogs (`data/desivast/`) are gitignored / not present
in the local checkout. If those artifacts ARE present the script joins the GZ1
overlap through them and adds a void/non-void confusion stratum; otherwise it
records the void stratum as DATA-UNAVAILABLE with an explicit reason rather than
fabricating it.

Deterministic and re-runnable: no random component; all cuts are fixed
thresholds. Cross-match recipe is byte-identical to
`run_dipole_gz1only_fullN.py` (KDTree unit-vector nearest, <= 1 arcsec).

Output: pipelines/p2_chirality/outputs/gz1_stratified_confusion.json
        (+ pipelines/p5_desi_chirality/outputs/gz1_stratified_confusion.json
         pointer copy when the void stratum computes).
"""
from __future__ import annotations

import glob
import gzip
import json
import os
import time
import urllib.request
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.spatial import cKDTree

HERE = Path(__file__).resolve().parent
P2 = HERE.parent
REPO = P2.parent.parent
OUT_PATH = P2 / "outputs" / "gz1_stratified_confusion.json"
P5_OUT_PATH = REPO / "pipelines" / "p5_desi_chirality" / "outputs" / "gz1_stratified_confusion.json"

# --- cross-match / cut constants (identical to run_dipole_gz1only_fullN.py) ---
CONF_CUT = 0.6          # winning-class prob cut used for the human-side selection
MATCH_ARCSEC = 1.0
LEG_DEC_SPLIT = 32.0    # BASS+MzLS (dec>+32) vs DECaLS (dec<+32); P4 definition
CLF_CONF_CUT = 0.6      # classifier confidence_eq science cut (p_eq>0.6)

GZ1_URL = "https://data.galaxyzoo.org/data/gz1/GalaxyZoo1_DR_table2.csv.gz"
Z_CRIT_95 = 1.959963984540054


# ---------------------------------------------------------------- coord helpers
def _hms_to_deg(s):
    p = str(s).strip().split(":")
    return (float(p[0]) + float(p[1]) / 60 + float(p[2]) / 3600) * 15.0


def _dms_to_deg(s):
    s = str(s).strip()
    sign = -1 if s.startswith("-") else 1
    p = s.lstrip("+-").split(":")
    return sign * (float(p[0]) + float(p[1]) / 60 + float(p[2]) / 3600)


def _radec_to_xyz(ra_deg, dec_deg):
    ra = np.radians(ra_deg)
    dec = np.radians(dec_deg)
    return np.stack(
        [np.cos(dec) * np.cos(ra), np.cos(dec) * np.sin(ra), np.sin(dec)],
        axis=1,
    )


# ------------------------------------------------------------------ statistics
def _wilson_ci(k, n, z=Z_CRIT_95):
    """Wilson score 95% CI for a binomial proportion. Returns (lo, hi)."""
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    denom = 1.0 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = (z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n))) / denom
    return (float(centre - half), float(centre + half))


def _two_prop_z(k1, n1, k2, n2):
    """Two-proportion z-test (pooled). Returns dict with diff, se, z, p_two."""
    if n1 == 0 or n2 == 0:
        return {"diff": None, "se": None, "z": None, "p_two_sided": None,
                "ci95": [None, None]}
    p1, p2 = k1 / n1, k2 / n2
    p_pool = (k1 + k2) / (n1 + n2)
    se_pool = np.sqrt(p_pool * (1 - p_pool) * (1 / n1 + 1 / n2))
    z = (p1 - p2) / se_pool if se_pool > 0 else 0.0
    # normal two-sided p
    from math import erfc, sqrt
    p_two = erfc(abs(z) / sqrt(2.0))
    se_unp = np.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
    return {
        "diff": float(p1 - p2),
        "se_pooled": float(se_pool),
        "se_unpooled": float(se_unp),
        "z": float(z),
        "p_two_sided": float(p_two),
        "ci95_diff": [float((p1 - p2) - Z_CRIT_95 * se_unp),
                      float((p1 - p2) + Z_CRIT_95 * se_unp)],
    }


def _confusion(sub):
    """Human-vs-classifier CW/CCW confusion on a subframe.

    sub must have integer columns 'gz1_cw' (human: 1=CW,0=CCW) and
    'clf_cw' (classifier among CW/CCW rows: 1=CW,0=CCW). Rows where the
    classifier called NOT_SPIRAL are handled by the caller.
    """
    n = int(len(sub))
    h_cw = sub["gz1_cw"].values.astype(bool)
    c_cw = sub["clf_cw"].values.astype(bool)

    # confusion counts (human -> classifier)
    cw_cw = int(np.sum(h_cw & c_cw))      # human CW, clf CW  (correct)
    cw_ccw = int(np.sum(h_cw & ~c_cw))    # human CW, clf CCW (CW->CCW error)
    ccw_ccw = int(np.sum(~h_cw & ~c_cw))  # human CCW, clf CCW (correct)
    ccw_cw = int(np.sum(~h_cw & c_cw))    # human CCW, clf CW (CCW->CW error)

    n_h_cw = cw_cw + cw_ccw               # human-CW total
    n_h_ccw = ccw_ccw + ccw_cw            # human-CCW total
    correct = cw_cw + ccw_ccw

    # directional error rates conditioned on the TRUE (human) class
    err_cw_to_ccw = (cw_ccw / n_h_cw) if n_h_cw else float("nan")
    err_ccw_to_cw = (ccw_cw / n_h_ccw) if n_h_ccw else float("nan")
    asym = (err_cw_to_ccw - err_ccw_to_cw) if (n_h_cw and n_h_ccw) else float("nan")

    return {
        "n": n,
        "n_human_cw": n_h_cw,
        "n_human_ccw": n_h_ccw,
        "confusion_counts": {
            "human_CW__clf_CW": cw_cw,
            "human_CW__clf_CCW": cw_ccw,
            "human_CCW__clf_CW": ccw_cw,
            "human_CCW__clf_CCW": ccw_ccw,
        },
        "accuracy": (correct / n) if n else float("nan"),
        "accuracy_ci95": _wilson_ci(correct, n),
        "err_CW_to_CCW": err_cw_to_ccw,
        "err_CW_to_CCW_ci95": _wilson_ci(cw_ccw, n_h_cw),
        "err_CCW_to_CW": err_ccw_to_cw,
        "err_CCW_to_CW_ci95": _wilson_ci(ccw_cw, n_h_ccw),
        "error_asymmetry_CWtoCCW_minus_CCWtoCW": asym,
        # 95% CI on the asymmetry via unpooled two-proportion SE
        "error_asymmetry_ci95": (
            _two_prop_z(cw_ccw, n_h_cw, ccw_cw, n_h_ccw)["ci95_diff"]
            if (n_h_cw and n_h_ccw) else [None, None]
        ),
        # net induced CW-fraction bias from differential error, first order:
        # d f_CW ~= (ccw_cw - cw_ccw)/n  (galaxies flipped INTO CW minus OUT of CW)
        "induced_delta_fCW": (
            float((ccw_cw - cw_ccw) / n) if n else float("nan")
        ),
        "induced_delta_fCW_ci95": _wilson_ci_diff_counts(cw_ccw, ccw_cw, n),
    }


def _wilson_ci_diff_counts(a, b, n):
    """Approx 95% CI on (b-a)/n treating (b-a) as a mean of {-1,0,+1} draws.

    a = # human-CW->clf-CCW (subtract), b = # human-CCW->clf-CW (add).
    Variance of per-galaxy contribution estimated empirically.
    """
    if n == 0:
        return [None, None]
    p_a = a / n
    p_b = b / n
    mean = p_b - p_a
    # var of x in {-1,0,+1}: E[x^2]-E[x]^2 = (p_a+p_b) - (p_b-p_a)^2
    var = (p_a + p_b) - mean * mean
    se = np.sqrt(max(var, 0.0) / n)
    return [float(mean - Z_CRIT_95 * se), float(mean + Z_CRIT_95 * se)]


# --------------------------------------------------------------------- loaders
def _default_cat_path():
    env = os.environ.get("CAT_C_PATH")
    if env:
        return env
    hits = glob.glob(
        os.path.expanduser(
            "~/.cache/huggingface/hub/datasets--bamfai--galaxy-chirality-catalog/"
            "snapshots/*/catalog_production.parquet"
        )
    )
    if hits:
        return hits[0]
    return "/workspace/chirality/catalog_production.parquet"


def _get_gz1_csv():
    env = os.environ.get("GZ1_CSV")
    if env and Path(env).exists():
        return env
    dest = Path("/tmp/gz1_table2.csv.gz")
    if not dest.exists():
        print(f"Downloading GZ1 Table 2 -> {dest} ...", flush=True)
        urllib.request.urlretrieve(GZ1_URL, dest)
    return str(dest)


# ------------------------------------------------------------------- P5 void join
# DESIVAST-analysis cosmology (P5 tex sec:desivast_xmatch; identical to
# pipelines/p5_desi_chirality/scripts/17_v0151_closure_recomputes.py): flat LCDM,
# H0 = 67.66, Om = 0.315; galaxy positions in h^-1 Mpc to match the DESIVAST hole
# catalog X/Y/Z convention (multiply comoving Mpc by h = H0/100).
P5_H0, P5_OM0, P5_LITTLE_H = 67.66, 0.315, 0.6766
Z_DESIVAST_MAX = 0.24  # DESIVAST BGS VOLLIM redshift cap (P5 primary)


def _asymmetry_two_prop_diff(cw_ccw_a, n_hcw_a, ccw_cw_a, n_hccw_a,
                             cw_ccw_b, n_hcw_b, ccw_cw_b, n_hccw_b):
    """Two-proportion test that the CW/CCW error *asymmetry* differs between
    strata A and B. Asymmetry_i = err(CW->CCW)_i - err(CCW->CW)_i. The SE of
    each per-stratum asymmetry combines two independent binomials; the
    between-strata difference-of-asymmetries SE adds all four in quadrature.
    """
    def _rate(k, n):
        return (k / n) if n else float("nan")
    asym_a = (_rate(cw_ccw_a, n_hcw_a) - _rate(ccw_cw_a, n_hccw_a))
    asym_b = (_rate(cw_ccw_b, n_hcw_b) - _rate(ccw_cw_b, n_hccw_b))
    def _var(k, n):
        if not n:
            return float("nan")
        p = k / n
        return p * (1 - p) / n
    var = (_var(cw_ccw_a, n_hcw_a) + _var(ccw_cw_a, n_hccw_a)
           + _var(cw_ccw_b, n_hcw_b) + _var(ccw_cw_b, n_hccw_b))
    se = float(np.sqrt(var)) if np.isfinite(var) else float("nan")
    diff = asym_a - asym_b
    z = (diff / se) if (se and np.isfinite(se) and se > 0) else float("nan")
    from math import erfc, sqrt
    p_two = float(erfc(abs(z) / sqrt(2.0))) if np.isfinite(z) else None
    return {
        "asymmetry_stratumA": float(asym_a) if np.isfinite(asym_a) else None,
        "asymmetry_stratumB": float(asym_b) if np.isfinite(asym_b) else None,
        "diff_A_minus_B": float(diff) if np.isfinite(diff) else None,
        "se_diff": se if np.isfinite(se) else None,
        "z": float(z) if np.isfinite(z) else None,
        "p_two_sided": p_two,
        "ci95_diff": ([float(diff - Z_CRIT_95 * se), float(diff + Z_CRIT_95 * se)]
                      if np.isfinite(diff) and np.isfinite(se) else [None, None]),
    }


def _void_strata_confusion(j, void_mask, definition):
    """Build the {void, non_void} confusion strata + asymmetry-difference test.

    `j` is the GZ1-overlap CW/CCW subframe (has gz1_cw + clf_cw) restricted to
    the DESIVAST volume; `void_mask` is a boolean array over j.
    """
    void = j[void_mask]
    nonvoid = j[~void_mask]
    cv = _confusion(void) if len(void) else {"status": "EMPTY", "n": 0}
    cn = _confusion(nonvoid) if len(nonvoid) else {"status": "EMPTY", "n": 0}
    out = {"definition": definition, "void": cv, "non_void": cn,
           "n_total_in_desivast_volume": int(len(j))}
    if len(void) and len(nonvoid) and cv.get("n_human_cw") and cn.get("n_human_cw"):
        cc = "confusion_counts"
        out["asymmetry_diff_void_vs_nonvoid"] = _asymmetry_two_prop_diff(
            cv[cc]["human_CW__clf_CCW"], cv["n_human_cw"],
            cv[cc]["human_CCW__clf_CW"], cv["n_human_ccw"],
            cn[cc]["human_CW__clf_CCW"], cn["n_human_cw"],
            cn[cc]["human_CCW__clf_CW"], cn["n_human_ccw"],
        )
        # also a direct two-prop test on the induced-delta-fCW between strata
        out["induced_delta_fCW_void_vs_nonvoid"] = {
            "void": cv["induced_delta_fCW"], "non_void": cn["induced_delta_fCW"],
            "diff_void_minus_nonvoid": (cv["induced_delta_fCW"] - cn["induced_delta_fCW"]),
        }
    return out


def _voidfinder_membership(desi_ra, desi_dec, desi_z, desivast_dir):
    """VoidFinder point-in-sphere membership (NGC+SGC), footprint-restricted.

    Returns (member_bool, footprint_bool, meta). A galaxy is 'in footprint' if
    it lies within the on-sky+radial coverage of the union of VoidFinder holes
    (approximated conservatively as being within r_max of at least one hole
    centre in 3D h^-1 Mpc); non-footprint galaxies are dropped so the void /
    non-void contrast is measured only where the void catalog has coverage --
    identical footprint-restriction intent to the P5 primary.
    """
    from astropy.cosmology import FlatLambdaCDM
    cosmo = FlatLambdaCDM(H0=P5_H0, Om0=P5_OM0)
    chi_h = cosmo.comoving_distance(desi_z).value * P5_LITTLE_H  # h^-1 Mpc
    ra = np.radians(desi_ra)
    dec = np.radians(desi_dec)
    gal = np.column_stack([chi_h * np.cos(dec) * np.cos(ra),
                           chi_h * np.cos(dec) * np.sin(ra),
                           chi_h * np.sin(dec)])
    from astropy.io import fits
    holes = []
    for gc in ["NGC", "SGC"]:
        fpath = desivast_dir / f"DESIVAST_BGS_VOLLIM_VoidFinder_{gc}.fits"
        with fits.open(fpath) as h:
            d = h["HOLES"].data
            holes.append(np.column_stack([d["X"], d["Y"], d["Z"], d["RADIUS"]]))
    holes = np.vstack(holes)
    r_max = float(holes[:, 3].max())
    kd_holes = cKDTree(holes[:, :3])
    # footprint proxy: within r_max of a hole centre (union coverage envelope)
    nearest_hole_dist, _ = kd_holes.query(gal, k=1)
    footprint = nearest_hole_dist <= r_max
    # exact point-in-sphere membership: query galaxy tree per hole radius,
    # vectorised over holes (identical to P5 script 17 C8 membership driver)
    kd_gal = cKDTree(gal)
    member = np.zeros(len(gal), dtype=bool)
    hits = kd_gal.query_ball_point(holes[:, :3], r=holes[:, 3])
    for h_idx in hits:
        member[h_idx] = True
    meta = {
        "n_holes": int(len(holes)),
        "max_hole_radius_mpc_h": r_max,
        "cosmology": {"H0": P5_H0, "Om0": P5_OM0, "little_h": P5_LITTLE_H},
    }
    return member, footprint, meta


def _galzone_native_membership(desi_targetid, algo, desivast_dir):
    """GALZONE catalog-native void membership for a V2 algorithm (per script 30).

    void = OUT==0 & ZONE>=0 & VOID0>=0. Returns a bool array aligned to
    desi_targetid (True=void, False=non-void), plus n_joined (galaxies present
    in the GALZONE table). Galaxies not in GALZONE are returned as NaN (drop).
    """
    from astropy.io import fits
    gzs, zvs = [], []
    zone_offset = 0
    for gc in ["NGC", "SGC"]:
        fpath = desivast_dir / f"DESIVAST_BGS_VOLLIM_{algo}_{gc}.fits"
        with fits.open(fpath) as fh:
            gz = fh["GALZONE"].data
            zv = fh["ZONEVOID"].data
            gd = pd.DataFrame({
                "TARGET": np.asarray(gz["TARGET"], dtype=np.int64),
                "ZONE": np.asarray(gz["ZONE"], dtype=np.int64),
                "OUT": np.asarray(gz["OUT"], dtype=np.int64),
            })
            zd = pd.DataFrame({
                "ZONE": np.asarray(zv["ZONE"], dtype=np.int64),
                "VOID0": np.asarray(zv["VOID0"], dtype=np.int64),
            })
            gd.loc[gd["ZONE"] >= 0, "ZONE"] += zone_offset
            zd["ZONE"] += zone_offset
            zone_offset += int(zd["ZONE"].max()) + 1
            gzs.append(gd)
            zvs.append(zd)
    gal = pd.concat(gzs, ignore_index=True)
    zone = pd.concat(zvs, ignore_index=True)
    gal = gal.merge(zone, on="ZONE", how="left")
    gal["VOID0"] = gal["VOID0"].fillna(-1).astype(np.int64)
    gal["is_void"] = (gal["OUT"] == 0) & (gal["ZONE"] >= 0) & (gal["VOID0"] >= 0)
    lut = gal.drop_duplicates("TARGET").set_index("TARGET")["is_void"]
    mapped = pd.Series(desi_targetid).map(lut)
    return mapped.values, int(mapped.notna().sum())


def _try_void_stratum(matched):
    """P5 void / non-void human-vs-classifier confusion stratum on the GZ1 overlap.

    Recipe (identical definitions to the P5 primary,
    pipelines/p5_desi_chirality/scripts/17 + 30):
      1. join the GZ1-overlap CW/CCW subframe to the P5 matched-chirality x
         DESI-z parquet on dr8_id == match_dr8_id (gives desi_z, desi_targetid,
         desi_ra/dec for each GZ1-overlap galaxy), restricted to
         matched_primary_deduped.
      2. restrict to the DESIVAST volume z <= 0.24.
      3. VoidFinder point-in-sphere membership (NGC+SGC), footprint-restricted.
      4. optional GALZONE-native split (V2_REVOLVER / V2_VIDE) if V2 files exist.
      5. per {void, non_void} stratum: N, accuracy, err(CW->CCW), err(CCW->CW),
         error asymmetry +/-95% CI, and a two-proportion test of the asymmetry
         DIFFERENCE between the strata.

    Returns a DATA-UNAVAILABLE record (never fabricated) if inputs are absent
    or if no shared join key exists.
    """
    reason_missing = []
    p5_matched = REPO / "pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet"
    desivast_dir = REPO / "pipelines/p5_desi_chirality/data/desivast"
    vf_files = [desivast_dir / f"DESIVAST_BGS_VOLLIM_VoidFinder_{gc}.fits" for gc in ("NGC", "SGC")]
    if not p5_matched.exists():
        reason_missing.append(f"P5 matched chirality x DESI-z parquet absent: {p5_matched}")
    if not all(f.exists() for f in vf_files):
        reason_missing.append(f"DESIVAST VoidFinder NGC+SGC FITS absent under {desivast_dir}/")

    if reason_missing:
        return {
            "status": "DATA-UNAVAILABLE",
            "reason": reason_missing,
            "note": (
                "GZ1 Table 2 carries no redshift; the void/non-void split for the "
                "GZ1-overlap galaxies requires the P5 matched chirality x DESI-redshift "
                "parquet plus the DESIVAST VoidFinder void-sphere catalogs. Rebuild the "
                "parquet via pipelines/p5_desi_chirality/scripts/{01,02,03} and fetch "
                "DESIVAST from https://data.desi.lbl.gov/public/dr1/vac/dr1/desivast/v1.0/, "
                "then re-run with P5_VOID=1."
            ),
        }

    if "dr8_id" not in matched.columns:
        return {"status": "DATA-UNAVAILABLE",
                "reason": ["GZ1 overlap frame carries no dr8_id (catalog dr8_id column "
                           "was unavailable during cross-match); cannot join to P5 parquet"]}

    try:
        cols = ["match_dr8_id", "desi_z", "desi_targetid", "desi_ra", "desi_dec",
                "match_class_eq", "matched_primary_deduped"]
        pm = pd.read_parquet(p5_matched, columns=cols)
        pm = pm[pm["matched_primary_deduped"]].copy()
        pm = pm.rename(columns={"match_dr8_id": "dr8_id"})
        # dedupe P5 side to unique dr8_id (nearest already picked in pipeline)
        pm = pm.drop_duplicates("dr8_id", keep="first")

        j = matched.merge(
            pm[["dr8_id", "desi_z", "desi_targetid", "desi_ra", "desi_dec"]],
            on="dr8_id", how="inner")
        n_join_total = int(len(j))
        # DESIVAST volume cut
        j = j[j["desi_z"] <= Z_DESIVAST_MAX].reset_index(drop=True)
        n_lowz = int(len(j))
        if n_lowz == 0:
            return {"status": "COMPUTED-EMPTY",
                    "reason": ["no GZ1-overlap galaxies with desi_z <= 0.24 after join"],
                    "n_joined_to_p5": n_join_total, "n_z_leq_0p24": 0}

        member, footprint, vf_meta = _voidfinder_membership(
            j["desi_ra"].values, j["desi_dec"].values, j["desi_z"].values, desivast_dir)

        result = {
            "status": "COMPUTED",
            "join": {
                "key": "dr8_id (GZ1 overlap) == match_dr8_id (P5 matched parquet, deduped primary)",
                "n_gz1_overlap_cw_ccw": int(len(matched)),
                "n_joined_to_p5_matched": n_join_total,
                "n_z_leq_0p24": n_lowz,
            },
            "voidfinder_meta": vf_meta,
        }

        # PRIMARY: VoidFinder point-in-sphere, footprint-restricted
        jf = j[footprint].reset_index(drop=True)
        member_f = member[footprint]
        result["desivast_voidfinder_footprint_restricted"] = _void_strata_confusion(
            jf, member_f,
            "DESIVAST VoidFinder point-in-sphere; galaxies restricted to within "
            "r_max of a hole centre (footprint proxy); void = inside any hole sphere")
        result["desivast_voidfinder_footprint_restricted"]["n_in_footprint"] = int(footprint.sum())
        result["desivast_voidfinder_footprint_restricted"]["n_outside_footprint_dropped"] = int((~footprint).sum())

        # SECONDARY (unrestricted): all z<=0.24 galaxies, non-void = not in any hole
        result["desivast_voidfinder_all_lowz"] = _void_strata_confusion(
            j, member,
            "DESIVAST VoidFinder point-in-sphere over ALL z<=0.24 GZ1-overlap "
            "galaxies (no footprint restriction; non-void includes non-covered sky)")

        # OPTIONAL: GALZONE-native split for V2 algorithms if files present + cheap
        galzone = {}
        for algo in ("V2_REVOLVER", "V2_VIDE"):
            files = [desivast_dir / f"DESIVAST_BGS_VOLLIM_{algo}_{gc}.fits" for gc in ("NGC", "SGC")]
            if not all(f.exists() for f in files):
                galzone[algo] = {"status": "DATA-UNAVAILABLE",
                                 "reason": [f"{algo} NGC+SGC FITS absent"]}
                continue
            try:
                is_void, n_joined = _galzone_native_membership(
                    j["desi_targetid"].values, algo, desivast_dir)
                gmask = ~pd.isna(is_void)
                jg = j[gmask].reset_index(drop=True)
                vmask = is_void[gmask].astype(bool)
                res = _void_strata_confusion(
                    jg, vmask,
                    f"{algo} GALZONE catalog-native: void = OUT==0 & ZONE>=0 & VOID0>=0")
                res["n_joined_galzone"] = int(n_joined)
                galzone[algo] = res
            except Exception as e:  # pragma: no cover
                galzone[algo] = {"status": "DATA-UNAVAILABLE",
                                 "reason": [f"exception during {algo} GALZONE join: {e!r}"]}
        result["galzone_native_split"] = galzone
        return result
    except Exception as e:  # pragma: no cover - defensive
        return {"status": "DATA-UNAVAILABLE", "reason": [f"exception during void join: {e!r}"]}


# --------------------------------------------------------------------------- main
def main():
    t0 = time.time()
    print("=" * 72, flush=True)
    print("GZ1-OVERLAP STRATIFIED HUMAN-vs-CLASSIFIER CONFUSION MATRIX", flush=True)
    print("=" * 72, flush=True)

    # 1. GZ1 human labels (confident CW/CCW spirals)
    gz1_csv = _get_gz1_csv()
    print(f"Loading GZ1 Table 2: {gz1_csv}", flush=True)
    with gzip.open(gz1_csv, "rt") as f:
        gz1 = pd.read_csv(f)
    n_gz1_total = len(gz1)
    gz1["ra_deg"] = gz1["RA"].apply(_hms_to_deg)
    gz1["dec_deg"] = gz1["DEC"].apply(_dms_to_deg)
    spir = gz1[gz1["SPIRAL"] == 1].copy()
    spir["max_cw_acw"] = spir[["P_CW", "P_ACW"]].max(axis=1)
    conf = spir[spir["max_cw_acw"] > CONF_CUT].copy()
    conf["gz1_cw"] = (conf["P_CW"] > conf["P_ACW"]).astype(int)
    print(f"  GZ1 total / spirals / confident: {n_gz1_total:,} / {len(spir):,} / {len(conf):,}",
          flush=True)

    # 2. classifier catalog with the label + confidence columns
    cat_path = _default_cat_path()
    print(f"Loading catalog: {cat_path}", flush=True)
    cat_cols = ["ra", "dec", "class_eq", "p_cw_eq", "p_ccw_eq", "confidence_eq"]
    cat = pd.read_parquet(cat_path, columns=cat_cols)
    cat = cat[cat["ra"].notna() & cat["dec"].notna()].reset_index(drop=True)
    print(f"  catalog rows: {len(cat):,}", flush=True)

    # 3. cross-match GZ1 confident spirals -> catalog (<= 1 arcsec, KDTree)
    print("Cross-matching (<=1 arcsec)...", flush=True)
    cat_xyz = _radec_to_xyz(cat["ra"].values, cat["dec"].values)
    gz1_xyz = _radec_to_xyz(conf["ra_deg"].values, conf["dec_deg"].values)
    tree = cKDTree(cat_xyz)
    tol = MATCH_ARCSEC / 3600.0 * np.pi / 180.0
    dist, idx = tree.query(gz1_xyz, k=1, distance_upper_bound=tol)
    ok = np.isfinite(dist)
    n_match = int(ok.sum())
    print(f"  matched: {n_match:,} / {len(conf):,}", flush=True)

    m = conf[ok].copy().reset_index(drop=True)
    ci = idx[ok]
    m["cat_dec"] = cat["dec"].values[ci]
    m["class_eq"] = cat["class_eq"].values[ci]
    m["p_cw_eq"] = cat["p_cw_eq"].values[ci]
    m["p_ccw_eq"] = cat["p_ccw_eq"].values[ci]
    m["confidence_eq"] = cat["confidence_eq"].values[ci]

    # classifier CW/CCW label among spiral calls; NOT_SPIRAL handled separately
    n_before = len(m)
    m["clf_notspiral"] = (m["class_eq"].astype(str).str.upper().str.startswith("NOT"))
    n_notspiral = int(m["clf_notspiral"].sum())
    spir_m = m[~m["clf_notspiral"]].copy()
    spir_m["clf_cw"] = (spir_m["class_eq"].astype(str).str.upper() == "CW").astype(int)
    print(f"  classifier NOT_SPIRAL on matched: {n_notspiral:,} / {n_before:,} "
          f"(excluded from CW/CCW confusion, reported separately)", flush=True)

    # ---------------------------------------------------- overall + strata
    def _leg(sub):
        north = sub["cat_dec"] > LEG_DEC_SPLIT
        return sub[north], sub[~north]

    overall = _confusion(spir_m)

    bass, decals = _leg(spir_m)
    strat_leg = {
        "BASS_MzLS_dec_gt_+32": _confusion(bass) if len(bass) else {"status": "EMPTY"},
        "DECaLS_dec_lt_+32": _confusion(decals) if len(decals) else {"status": "EMPTY"},
    }
    # two-prop tests between legs on each directional error + on the asymmetry
    def _cell(c, key_num, key_den):
        return c["confusion_counts"][key_num], c[key_den]
    if len(bass) and len(decals):
        cb, cd = _confusion(bass), _confusion(decals)
        strat_leg["compare_BASS_vs_DECaLS"] = {
            "err_CW_to_CCW": _two_prop_z(
                cb["confusion_counts"]["human_CW__clf_CCW"], cb["n_human_cw"],
                cd["confusion_counts"]["human_CW__clf_CCW"], cd["n_human_cw"]),
            "err_CCW_to_CW": _two_prop_z(
                cb["confusion_counts"]["human_CCW__clf_CW"], cb["n_human_ccw"],
                cd["confusion_counts"]["human_CCW__clf_CW"], cd["n_human_ccw"]),
            "induced_delta_fCW_diff": {
                "bass": cb["induced_delta_fCW"], "decals": cd["induced_delta_fCW"],
                "diff": cb["induced_delta_fCW"] - cd["induced_delta_fCW"],
            },
        }

    hi = spir_m[spir_m["confidence_eq"] > CLF_CONF_CUT]
    lo = spir_m[spir_m["confidence_eq"] <= CLF_CONF_CUT]
    strat_conf = {
        "confidence_eq_gt_0.6": _confusion(hi) if len(hi) else {"status": "EMPTY"},
        "confidence_eq_le_0.6": _confusion(lo) if len(lo) else {"status": "EMPTY"},
    }
    if len(hi) and len(lo):
        ch, cl = _confusion(hi), _confusion(lo)
        strat_conf["compare_hi_vs_lo_conf"] = {
            "err_CW_to_CCW": _two_prop_z(
                ch["confusion_counts"]["human_CW__clf_CCW"], ch["n_human_cw"],
                cl["confusion_counts"]["human_CW__clf_CCW"], cl["n_human_cw"]),
            "err_CCW_to_CW": _two_prop_z(
                ch["confusion_counts"]["human_CCW__clf_CW"], ch["n_human_ccw"],
                cl["confusion_counts"]["human_CCW__clf_CW"], cl["n_human_ccw"]),
        }

    # P5 void stratum (attempt; honest DATA-UNAVAILABLE if artifacts absent)
    # m has no dr8_id column from catalog cols; add it if present for the join.
    try:
        cat_id = pd.read_parquet(cat_path, columns=["dr8_id"])
        m_ids = cat_id["dr8_id"].values[ci]
        spir_m = spir_m.copy()
        spir_m["dr8_id"] = m_ids[~m["clf_notspiral"].values]
    except Exception:
        pass
    void_stratum = _try_void_stratum(spir_m if "dr8_id" in spir_m.columns else spir_m)

    result = {
        "job": "GZ1-overlap stratified human-vs-classifier CW/CCW confusion matrix (P4+P5 referee closure)",
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "label_sources": {
            "human": "Galaxy Zoo 1 Table 2 P_CW/P_ACW human votes (Lintott+2011), confident spirals max(P_CW,P_ACW)>0.6",
            "classifier": "catalog_production.parquet class_eq / p_cw_eq / p_ccw_eq / confidence_eq (equivariant CE-ResNet pipeline)",
        },
        "cross_match": {"tol_arcsec": MATCH_ARCSEC, "method": "KDTree unit-vector nearest",
                        "n_confident_gz1": int(len(conf)), "n_matched": n_match},
        "definitions": {
            "imaging_leg": f"BASS+MzLS = dec>+{LEG_DEC_SPLIT} deg; DECaLS = dec<+{LEG_DEC_SPLIT} deg (P4 split)",
            "confidence_bin": f"classifier confidence_eq>{CLF_CONF_CUT} vs <=",
            "error_asymmetry": "err(CW->CCW) - err(CCW->CW); nonzero => differential mislabelling that can bias f_CW",
            "induced_delta_fCW": "(#CCW->CW - #CW->CCW)/N; first-order net bias the classifier adds to the CW fraction",
            "ci": "Wilson 95% for single rates; unpooled two-proportion 95% for differences",
        },
        "classifier_not_spiral_on_matched": {
            "n": n_notspiral, "of": n_before,
            "note": "GZ1-confident spirals the classifier called NOT_SPIRAL; excluded from the CW/CCW confusion (completeness, not chirality-error)",
        },
        "overall": overall,
        "stratified_by_imaging_leg": strat_leg,
        "stratified_by_confidence": strat_conf,
        "stratified_by_environment_void_P5": void_stratum,
        "wall_seconds": round(time.time() - t0, 1),
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\nWrote {OUT_PATH}", flush=True)

    # P5 pointer copy only when the void stratum actually computed
    if isinstance(void_stratum, dict) and void_stratum.get("status") == "COMPUTED":
        P5_OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(P5_OUT_PATH, "w") as f:
            json.dump(result, f, indent=2)
        print(f"Wrote P5 copy {P5_OUT_PATH}", flush=True)

    # short console verdict
    a = overall["error_asymmetry_CWtoCCW_minus_CCWtoCW"]
    d = overall["induced_delta_fCW"]
    print(f"\nOVERALL: N={overall['n']:,}  acc={overall['accuracy']:.4f}  "
          f"err(CW->CCW)={overall['err_CW_to_CCW']:.4f}  err(CCW->CW)={overall['err_CCW_to_CW']:.4f}",
          flush=True)
    print(f"OVERALL error asymmetry={a:+.4f}  induced dfCW={d:+.4f} "
          f"(95% CI {overall['induced_delta_fCW_ci95'][0]:+.4f}..{overall['induced_delta_fCW_ci95'][1]:+.4f})",
          flush=True)

    # void stratum verdict
    if isinstance(void_stratum, dict) and void_stratum.get("status") == "COMPUTED":
        vf = void_stratum.get("desivast_voidfinder_footprint_restricted", {})
        v, nv = vf.get("void", {}), vf.get("non_void", {})
        ad = vf.get("asymmetry_diff_void_vs_nonvoid", {})
        print("\nP5 VOID STRATUM (DESIVAST VoidFinder, footprint-restricted):", flush=True)
        print(f"  void:     N={v.get('n')}  acc={v.get('accuracy')}  "
              f"asym={v.get('error_asymmetry_CWtoCCW_minus_CCWtoCW')}", flush=True)
        print(f"  non_void: N={nv.get('n')}  acc={nv.get('accuracy')}  "
              f"asym={nv.get('error_asymmetry_CWtoCCW_minus_CCWtoCW')}", flush=True)
        if ad:
            print(f"  asymmetry diff (void-nonvoid)={ad.get('diff_A_minus_B')}  "
                  f"z={ad.get('z')}  p={ad.get('p_two_sided')}  "
                  f"95% CI {ad.get('ci95_diff')}", flush=True)
    else:
        print(f"\nP5 VOID STRATUM: {void_stratum.get('status')} "
              f"-- {void_stratum.get('reason')}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
