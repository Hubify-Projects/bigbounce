#!/usr/bin/env python3
"""
EDGE-ON-ISOLATED argmax tie-break spatial-coherence statistic (P4).

Closes the one remaining pod-gated piece of Gemini's App E MAJOR (v1.0.215):
"a direct quantification of the spatial coherence of the argmax tie-break on
edge-on systems is required." The committed
`per_leg_confidence_familywise_maxstat.json` gives the coherence of the whole
borderline confidence band (p_eq in [0.5,0.6]); this script ISOLATES the
edge-on (b/a < 0.30) subset of that band -- the systems where the CW/CCW
argmax is genuinely ambiguous because disc spin sense is unresolvable near
edge-on -- and measures the same per-leg l=1 dipole significance against an
isotropic (global-monopole) label-shuffle null.

DATA (all committed / HF-cached, NO pod, NO fabrication):
  - catalog_production.parquet  (bamfai/galaxy-chirality-catalog HF cache):
      dr8_id, class_eq, p_cw_eq, p_ccw_eq, ra, dec   (8.47M; 3.20M spirals)
  - spiral_morphology_dr8.parquet (committed in repo):
      BRICKID, OBJID, TYPE, FRACDEV, SHAPEDEV_E1/E2, SHAPEEXP_E1/E2 -> b/a
  join key: dr8_id == f"{BRICKID}_{OBJID}"

METHOD: identical dipole statistic + null construction as
  per_leg_confidence_familywise_maxstat.py (weighted-LSQ direction fit,
  A = 2|(cx,cy,cz)|, sigma vs binomial-monopole shuffle at the population
  p_CW), only the sample is restricted to edge-on borderline galaxies.

Output: outputs/canonical_provenance/edgeon_isolated_tiebreak_coherence.json
"""
from __future__ import annotations
import json, time, os
from pathlib import Path
import numpy as np
import pandas as pd
import healpy as hp

NSIDE = 64
SEED = 42
N_MC = 2000
BA_EDGEON = 0.30            # edge-on cut (axis ratio b/a < 0.30)
BORDERLINE = (0.5, 0.6)     # argmax tie-break confidence band (p_eq in [0.5,0.6])
LEGS = ["BASS+MzLS", "DECaLS", "DES"]

REPO = Path(__file__).resolve().parents[3]
MORPH = REPO / "pipelines/p2_chirality/outputs/spiral_morphology_dr8.parquet"
OUT = REPO / "pipelines/p2_chirality/outputs/canonical_provenance/edgeon_isolated_tiebreak_coherence.json"

t0 = time.time()
def log(m): print(f"[{time.time()-t0:6.1f}s] {m}", flush=True)


def assign_leg(ra, dec):
    """DESI Legacy DR8 imaging-leg cuts (identical to per_leg_*_maxstat.py)."""
    leg = np.full(len(ra), "DECaLS", dtype=object)
    leg[dec > 32.375] = "BASS+MzLS"
    des = (dec < -10) & (((ra >= 0) & (ra <= 60)) | ((ra >= 300) & (ra <= 360)))
    leg[des] = "DES"
    return leg


def ba_from(e1, e2):
    e = np.sqrt(np.asarray(e1, float) ** 2 + np.asarray(e2, float) ** 2)
    e = np.clip(e, 0, 0.999)
    return (1.0 - e) / (1.0 + e)


def dipole_amp(n_total, n_cw, X, nz_idx):
    """A = 2|(cx,cy,cz)| from weighted-LSQ p=n_cw/n_total direction fit."""
    w = n_total[nz_idx].astype(float)
    p = n_cw[nz_idx].astype(float) / w
    XtW = X.T * w
    A = XtW @ X
    b = XtW @ p
    try:
        c = np.linalg.solve(A, b)
    except np.linalg.LinAlgError:
        return 0.0
    return float(2.0 * np.sqrt(c[0] ** 2 + c[1] ** 2 + c[2] ** 2))


def load_catalog():
    """Load catalog_production from HF cache (or hf download)."""
    from huggingface_hub import hf_hub_download
    path = hf_hub_download("bamfai/galaxy-chirality-catalog",
                           "catalog_production.parquet", repo_type="dataset")
    return pd.read_parquet(path, columns=["dr8_id", "class_eq", "p_cw_eq",
                                          "p_ccw_eq", "ra", "dec"])


def main():
    log("loading catalog_production (HF cache)")
    df = load_catalog()
    df = df[df["class_eq"].isin(["CW", "CCW"])].reset_index(drop=True)
    log(f"spirals: {len(df):,}")

    # --- join b/a from committed DR8-sweep morphology ---
    bo = df["dr8_id"].str.split("_", expand=True)
    df["BRICKID"] = bo[0].astype("int64")
    df["OBJID"] = bo[1].astype("int64")
    m = pd.read_parquet(MORPH, columns=["BRICKID", "OBJID", "TYPE", "FRACDEV",
                                        "SHAPEDEV_E1", "SHAPEDEV_E2",
                                        "SHAPEEXP_E1", "SHAPEEXP_E2"])
    typ = m["TYPE"].astype(str).str.upper().values
    dev_like = np.isin(typ, ["DEV", "COMP", "SER"]) | (m["FRACDEV"].values >= 0.5)
    ba_dev = ba_from(m["SHAPEDEV_E1"], m["SHAPEDEV_E2"])
    ba_exp = ba_from(m["SHAPEEXP_E1"], m["SHAPEEXP_E2"])
    m["b_over_a"] = np.where(dev_like, ba_dev, ba_exp)
    m = m[["BRICKID", "OBJID", "b_over_a"]]
    df = df.merge(m, on=["BRICKID", "OBJID"], how="inner")   # inner = only measured b/a
    log(f"spirals with measured b/a: {len(df):,}")

    conf = np.maximum(df["p_cw_eq"].values.astype(np.float64),
                      df["p_ccw_eq"].values.astype(np.float64))
    ba = df["b_over_a"].values.astype(np.float64)
    ra = df["ra"].values.astype(np.float64)
    dec = df["dec"].values.astype(np.float64)
    is_cw = (df["class_eq"].values == "CW").astype(np.int8)
    leg = assign_leg(ra, dec)
    pix_full = hp.ang2pix(NSIDE, np.radians(90.0 - dec), np.radians(ra)).astype(np.int64)
    npix = hp.nside2npix(NSIDE)

    # --- edge-on borderline (tie-break) population ---
    edgeon = ba < BA_EDGEON
    band = (conf >= BORDERLINE[0]) & (conf < BORDERLINE[1])
    sel = edgeon & band
    log(f"edge-on (b/a<{BA_EDGEON}): {int(edgeon.sum()):,}; "
        f"borderline band [{BORDERLINE[0]},{BORDERLINE[1]}): {int(band.sum()):,}; "
        f"edge-on & borderline (tie-break-isolated): {int(sel.sum()):,}")
    p_cw_pop = float(is_cw[sel].mean()) if sel.sum() else float("nan")
    log(f"edge-on tie-break population p_CW = {p_cw_pop:.4f}")

    rng = np.random.default_rng(SEED)

    def cell_stat(mask, label):
        n_in = int(mask.sum())
        if n_in < 100:
            return {"label": label, "N": n_in, "valid": False}
        sub_pix = pix_full[mask]
        sub_cw = is_cw[mask].astype(bool)
        n_total = np.bincount(sub_pix, minlength=npix)
        n_cw = np.bincount(sub_pix[sub_cw], minlength=npix)
        nz = n_total > 0
        nz_idx = np.where(nz)[0]
        th, ph = hp.pix2ang(NSIDE, nz_idx)
        X = np.column_stack([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph),
                             np.cos(th), np.ones(len(nz_idx))]).astype(np.float64)
        A_obs = dipole_amp(n_total, n_cw, X, nz_idx)
        # isotropic null: binomial-monopole shuffle at this population's p_CW
        p_cw = float(sub_cw.mean())
        w = n_total[nz_idx].astype(float)
        XtW = X.T * w
        AtA_inv = np.linalg.inv(XtW @ X)
        A_null = np.empty(N_MC)
        for k in range(N_MC):
            shuf = rng.binomial(1, p_cw, size=len(sub_pix)).astype(bool)
            ncw_s = np.bincount(sub_pix[shuf], minlength=npix)
            b = XtW @ (ncw_s[nz_idx].astype(float) / w)
            c = AtA_inv @ b
            A_null[k] = 2.0 * np.sqrt(c[0] ** 2 + c[1] ** 2 + c[2] ** 2)
        mu, sd = float(A_null.mean()), float(A_null.std(ddof=1))
        sig = (A_obs - mu) / max(sd, 1e-12)
        # empirical one-sided p (A_obs >= null)
        p_emp = float(((A_null >= A_obs).sum() + 1) / (N_MC + 1))
        log(f"  {label:22s} N={n_in:>7d}  A_obs={A_obs:.5f}  z={sig:+.2f}  p_emp={p_emp:.4f}")
        return {"label": label, "N": n_in, "valid": True, "p_CW": p_cw,
                "A_obs": A_obs, "A_null_mean": mu, "A_null_std": sd,
                "z": sig, "p_emp_one_sided": p_emp}

    log("computing edge-on-isolated tie-break dipole per leg + aggregate")
    cells = {}
    cells["ALL_edgeon_borderline"] = cell_stat(sel, "ALL edge-on tie-break")
    for L in LEGS:
        cells[L] = cell_stat(sel & (leg == L), f"{L} edge-on tie-break")

    # family-wise max|z| joint null over the per-leg cells (global label shuffle
    # within the edge-on tie-break population, preserving total CW count)
    valid_legs = [L for L in LEGS if cells[L].get("valid")]
    fam = None
    if valid_legs:
        log(f"family-wise joint max|z| null over legs {valid_legs} (N_MC={N_MC})")
        sub_idx = np.where(sel)[0]
        n_sub = len(sub_idx)
        n_cw_sub = int(is_cw[sub_idx].sum())
        # precompute per-leg design once
        legdata = {}
        for L in valid_legs:
            lm = sel & (leg == L)
            sp = pix_full[lm]
            nt = np.bincount(sp, minlength=npix)
            nz = nt > 0
            nz_idx = np.where(nz)[0]
            th, ph = hp.pix2ang(NSIDE, nz_idx)
            X = np.column_stack([np.sin(th)*np.cos(ph), np.sin(th)*np.sin(ph),
                                 np.cos(th), np.ones(len(nz_idx))]).astype(np.float64)
            w = nt[nz_idx].astype(float)
            XtW = X.T * w
            legdata[L] = {"local_idx": np.searchsorted(sub_idx, np.where(lm)[0]),
                          "pix": sp, "nz_idx": nz_idx, "w": w, "XtW": XtW,
                          "AtA_inv": np.linalg.inv(XtW @ X),
                          "mu": cells[L]["A_null_mean"], "sd": cells[L]["A_null_std"]}
        rng2 = np.random.default_rng(SEED + 7)
        maxz = np.empty(N_MC)
        for k in range(N_MC):
            perm = np.zeros(n_sub, dtype=bool)
            perm[rng2.choice(n_sub, size=n_cw_sub, replace=False)] = True
            zz = []
            for L in valid_legs:
                d = legdata[L]
                cw_leg = perm[d["local_idx"]]
                ncw = np.bincount(d["pix"][cw_leg], minlength=npix)
                b = d["XtW"] @ (ncw[d["nz_idx"]].astype(float) / d["w"])
                c = d["AtA_inv"] @ b
                A = 2.0 * np.sqrt(c[0]**2 + c[1]**2 + c[2]**2)
                zz.append(abs((A - d["mu"]) / max(d["sd"], 1e-12)))
            maxz[k] = max(zz)
        obs_maxz = max(abs(cells[L]["z"]) for L in valid_legs)
        n_exc = int((maxz >= obs_maxz).sum())
        fam = {"legs": valid_legs, "obs_max_abs_z": obs_maxz,
               "joint_p_value": (n_exc + 1) / (N_MC + 1),
               "null_max_abs_z_p99": float(np.quantile(maxz, 0.99)),
               "argmax_leg": max(valid_legs, key=lambda L: abs(cells[L]["z"]))}
        log(f"  family-wise obs max|z|={obs_maxz:.2f}  joint p={fam['joint_p_value']:.4f}")

    # verdict
    if fam is not None:
        coherent = fam["joint_p_value"] < 0.05
        argmax_leg = fam["argmax_leg"]
        leg_selective = coherent and (
            sum(1 for L in valid_legs if abs(cells[L]["z"]) > 3.0) <= 1)
        if not coherent:
            verdict = "EDGEON_TIEBREAK_ISOTROPIC"
            vtext = ("The edge-on-isolated argmax tie-break shows NO spatially-coherent "
                     f"l=1 dipole (family-wise joint p={fam['joint_p_value']:.3f}); it is "
                     "consistent with an isotropic label-shuffle null. The argmax step on "
                     "edge-on systems does not introduce a directional bias.")
        elif leg_selective:
            verdict = "EDGEON_TIEBREAK_LEG_SELECTIVE_SYSTEMATIC"
            vtext = (f"The edge-on-isolated tie-break carries coherence concentrated in the "
                     f"{argmax_leg} leg (z={cells[argmax_leg]['z']:+.2f}), leg-selective "
                     "(depth/imaging-tracking) -- a survey-systematic signature, not an "
                     "isotropic-random or genuine-sky dipole. A cosmological tie-break bias "
                     "would not track a single imaging leg.")
        else:
            verdict = "EDGEON_TIEBREAK_COHERENT_MULTILEG"
            vtext = ("The edge-on-isolated tie-break is spatially coherent across multiple "
                     "legs -- flag for follow-up.")
    else:
        verdict = "INSUFFICIENT_EDGEON_STATISTICS"
        vtext = ("Too few edge-on borderline galaxies per leg (N<100) to form a per-leg "
                 "dipole; report the aggregate only.")

    result = {
        "script": "pipelines/p2_chirality/scripts/edgeon_isolated_tiebreak_coherence.py",
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "purpose": ("Direct spatial-coherence of the argmax tie-break ISOLATED to edge-on "
                    "(b/a<0.30) borderline (p_eq in [0.5,0.6]) systems -- closes the pod-gated "
                    "piece of Gemini App E MAJOR (v1.0.215)."),
        "config": {"nside": NSIDE, "n_mc": N_MC, "seed": SEED,
                   "ba_edgeon_cut": BA_EDGEON, "borderline_band": list(BORDERLINE),
                   "ba_definition": "(1-|e|)/(1+|e|), |e|=sqrt(e1^2+e2^2), deV shape if TYPE in {DEV,COMP,SER} or FRACDEV>=0.5 else EXP",
                   "join": "catalog_production.dr8_id == f'{BRICKID}_{OBJID}' of spiral_morphology_dr8"},
        "population": {"n_spirals_with_ba": int(len(df)),
                       "n_edgeon": int(edgeon.sum()),
                       "n_borderline_band": int(band.sum()),
                       "n_edgeon_tiebreak": int(sel.sum()),
                       "p_CW_edgeon_tiebreak": p_cw_pop},
        "cells": cells,
        "family_wise": fam,
        "verdict": verdict,
        "verdict_text": vtext,
        "integrity_note": ("All numbers computed from committed spiral_morphology_dr8.parquet + "
                           "HF-cached catalog_production.parquet. No pod, no fabrication. b/a from "
                           "real DR8-sweep ellipticities."),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, default=float))
    log(f"wrote {OUT}")
    print("\n=== EDGE-ON-ISOLATED TIE-BREAK COHERENCE VERDICT ===")
    print(f"  edge-on tie-break N = {int(sel.sum()):,}")
    for k, c in cells.items():
        if c.get("valid"):
            print(f"  {c['label']:22s} N={c['N']:>7d}  z={c['z']:+.2f}  p={c['p_emp_one_sided']:.4f}")
    if fam:
        print(f"  family-wise joint p = {fam['joint_p_value']:.4f} (max|z|={fam['obs_max_abs_z']:.2f} @ {fam['argmax_leg']})")
    print(f"  VERDICT: {verdict}")


if __name__ == "__main__":
    main()
