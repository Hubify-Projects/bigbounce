#!/usr/bin/env python3
"""
Path A — exhaustive signal hunt on Catalog C.

Four independent estimators that COULD reveal a positive signal hiding
in the data (or confirm the null result more strongly):

  (1) Confidence-stratified dipole: 5 confidence bins. If dipole grows
      with confidence, that's a signal; if it shrinks, that's noise.
  (2) Sky-quadrant dipole: split into 4 RA quadrants, redo dipole in
      each, look at consistency.
  (3) Galactic-hemisphere CW asymmetry: north vs south galactic.
  (4) Two-point correlation w_theta(theta) on the chirality field:
      CW-CW vs CW-CCW pair counts at angular scales 0.1-10 deg;
      excess at any scale = primordial-spin-correlation signal.

Result: one JSON artifact + summary printout for paper integration.
"""
from __future__ import annotations
import json, time, sys
from pathlib import Path
import numpy as np
import pandas as pd
import healpy as hp
from huggingface_hub import hf_hub_download

NSIDE = 64
N_MC = 1000
SEED = 42
OUT = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p2_chirality/outputs/canonical_provenance/pathA_signal_hunt_results.json")
RESULTS: dict = {}


def assign_pix(ra, dec):
    theta = np.radians(90.0 - dec)
    phi = np.radians(ra)
    return hp.ang2pix(NSIDE, theta, phi)


def dipole_amplitude(n_total, n_cw):
    """Full-amplitude A in p = 0.5*(1 + A cos theta)."""
    npix = len(n_total)
    nside = hp.npix2nside(npix)
    nz = n_total > 0
    if nz.sum() < 10:
        return 0.0
    pix_idx = np.where(nz)[0]
    th, ph = hp.pix2ang(nside, pix_idx)
    nx = np.sin(th) * np.cos(ph)
    ny = np.sin(th) * np.sin(ph)
    nz_ = np.cos(th)
    p = n_cw[nz] / n_total[nz]
    w = n_total[nz].astype(float)
    X = np.column_stack([nx, ny, nz_, np.ones(len(nx))])
    A_mat = (X * w[:, None]).T @ X
    b = (X * w[:, None]).T @ p
    try:
        c = np.linalg.solve(A_mat, b)
    except np.linalg.LinAlgError:
        return 0.0
    return float(2.0 * np.sqrt(c[0]**2 + c[1]**2 + c[2]**2))


def dipole_significance(df_sub, p_iso=0.5, n_mc=N_MC, seed=SEED, label=""):
    """Returns A_obs (%), sigma_iso, sigma_mono, p_iso, p_mono."""
    rng = np.random.default_rng(seed)
    pix = assign_pix(df_sub["ra"].values, df_sub["dec"].values)
    n_total = np.bincount(pix, minlength=hp.nside2npix(NSIDE))
    cw_mask = df_sub["class_eq"].values == "CW"
    n_cw_obs = np.bincount(pix[cw_mask], minlength=hp.nside2npix(NSIDE))
    n_spirals = int(n_total.sum())
    p_cw = n_cw_obs.sum() / max(n_spirals, 1)
    A_obs = dipole_amplitude(n_total, n_cw_obs)

    A_iso = np.zeros(n_mc)
    A_mono = np.zeros(n_mc)
    for i in range(n_mc):
        n_iso = rng.binomial(n_total, p_iso)
        A_iso[i] = dipole_amplitude(n_total, n_iso)
        n_mono = rng.binomial(n_total, p_cw)
        A_mono[i] = dipole_amplitude(n_total, n_mono)
    sigma_iso = (A_obs - A_iso.mean()) / (A_iso.std(ddof=1) + 1e-30)
    sigma_mono = (A_obs - A_mono.mean()) / (A_mono.std(ddof=1) + 1e-30)
    p_iso_val = (np.sum(A_iso >= A_obs) + 1) / (n_mc + 1)
    p_mono_val = (np.sum(A_mono >= A_obs) + 1) / (n_mc + 1)
    return {
        "label": label,
        "N_spiral": n_spirals,
        "p_CW": float(p_cw),
        "A_obs_pct": A_obs * 100,
        "sigma_isotropic": float(sigma_iso),
        "sigma_monopole_preserving": float(sigma_mono),
        "p_value_isotropic": float(p_iso_val),
        "p_value_monopole_preserving": float(p_mono_val),
    }


def main():
    t0 = time.time()
    print(f"[{time.time()-t0:.1f}s] Loading catalog ...", flush=True)
    p = hf_hub_download("bamfai/galaxy-chirality-catalog", "catalog_production.parquet", repo_type="dataset")
    df = pd.read_parquet(p, columns=["ra", "dec", "class_eq", "p_cw_eq", "p_ccw_eq", "confidence_eq"])
    print(f"[{time.time()-t0:.1f}s] {len(df):,} rows", flush=True)
    spirals = df[df["class_eq"].isin(["CW", "CCW"])].reset_index(drop=True)
    print(f"[{time.time()-t0:.1f}s] spirals: {len(spirals):,}", flush=True)
    spirals["max_eq"] = spirals[["p_cw_eq", "p_ccw_eq"]].max(axis=1)

    # ---------- (1) Confidence-stratified dipole ----------
    print(f"\n[{time.time()-t0:.1f}s] === (1) Confidence-stratified dipole ===", flush=True)
    bins = [(0.4, 0.5), (0.5, 0.6), (0.6, 0.7), (0.7, 0.8), (0.8, 1.0)]
    conf_results = []
    for lo, hi in bins:
        sub = spirals[(spirals["max_eq"] >= lo) & (spirals["max_eq"] < hi)]
        if len(sub) < 1000:
            continue
        r = dipole_significance(sub, label=f"max_p_eq_in_[{lo:.1f},{hi:.1f})")
        conf_results.append(r)
        print(f"  bin [{lo:.1f},{hi:.1f}) N={r['N_spiral']:>9,}  p_CW={r['p_CW']:.5f}  |A|={r['A_obs_pct']:.3f}%  σ_iso={r['sigma_isotropic']:+.2f}  σ_mono={r['sigma_monopole_preserving']:+.2f}", flush=True)
    RESULTS["confidence_stratified"] = {
        "interpretation": "If the dipole grows monotonically with confidence, that's a primordial signal (lower-confidence galaxies dilute it). If it shrinks or stays flat, it's noise/systematics.",
        "bins": conf_results,
    }

    # ---------- (2) RA-quadrant dipole ----------
    print(f"\n[{time.time()-t0:.1f}s] === (2) RA-quadrant dipole ===", flush=True)
    quad_results = []
    for q, (ra_lo, ra_hi) in enumerate([(0, 90), (90, 180), (180, 270), (270, 360)]):
        sub = spirals[(spirals["ra"] >= ra_lo) & (spirals["ra"] < ra_hi)]
        if len(sub) < 10000:
            continue
        r = dipole_significance(sub, label=f"RA_quadrant_[{ra_lo},{ra_hi})")
        quad_results.append(r)
        print(f"  Q{q+1} RA=[{ra_lo:3d},{ra_hi:3d})  N={r['N_spiral']:>9,}  p_CW={r['p_CW']:.5f}  |A|={r['A_obs_pct']:.3f}%  σ_iso={r['sigma_isotropic']:+.2f}", flush=True)
    RESULTS["ra_quadrants"] = {
        "interpretation": "Per-quadrant dipoles should be consistent if signal is cosmological; large variance = systematic (footprint/imaging).",
        "quadrants": quad_results,
    }

    # ---------- (3) Galactic hemisphere ----------
    print(f"\n[{time.time()-t0:.1f}s] === (3) Galactic hemisphere ===", flush=True)
    # convert (ra,dec) to galactic latitude
    eq = np.stack([spirals["ra"].values, spirals["dec"].values], axis=1)
    rot = hp.Rotator(coord=["C", "G"])
    th_eq = np.radians(90.0 - eq[:, 1])
    ph_eq = np.radians(eq[:, 0])
    th_gal, ph_gal = rot(th_eq, ph_eq)
    b_gal = 90.0 - np.degrees(th_gal)
    spirals = spirals.assign(b_gal=b_gal)
    gal_results = []
    for side, mask in [("NGP_b>0", b_gal > 0), ("SGP_b<0", b_gal < 0)]:
        sub = spirals[mask]
        r = dipole_significance(sub, label=f"galactic_{side}")
        gal_results.append(r)
        print(f"  {side:>10s}  N={r['N_spiral']:>9,}  p_CW={r['p_CW']:.5f}  |A|={r['A_obs_pct']:.3f}%  σ_iso={r['sigma_isotropic']:+.2f}", flush=True)
    RESULTS["galactic_hemispheres"] = {
        "interpretation": "Galactic-correlated CW excess would indicate dust/extinction systematic; isotropy across NGP/SGP is good.",
        "hemispheres": gal_results,
    }

    OUT.write_text(json.dumps(RESULTS, indent=2))
    print(f"\n[{time.time()-t0:.1f}s] Phase 1 saved -> {OUT}", flush=True)
    print(f"[{time.time()-t0:.1f}s] (Two-point correlation runs separately)", flush=True)


if __name__ == "__main__":
    main()
