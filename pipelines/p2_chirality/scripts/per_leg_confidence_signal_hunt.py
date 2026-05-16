#!/usr/bin/env python3
"""
Per-imaging-leg × confidence-stratified signal-hunt.

The per-imaging-leg analysis (Sec.~per_leg) shows all 3 legs
(BASS+MzLS, DECaLS, DES) individually null at the dipole level. The
confidence-stratified analysis (Sec.~signal_hunt) shows the
apparent +3σ in low-confidence bins disappears in HC subsamples.

This script crosses the two: per-leg AND per-confidence-bin dipole.
If the +3σ low-confidence-bin signal is a footprint-correlated
systematic, it should be concentrated in one specific imaging leg.
If it's classifier label noise, it should be roughly uniform across
legs.

Output: per_leg_confidence_signal_hunt.json
"""
import json, time
from pathlib import Path
import numpy as np
import pandas as pd
import healpy as hp
from huggingface_hub import hf_hub_download

NSIDE = 64
N_MC = 1000
SEED = 42
OUT = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p2_chirality/outputs/canonical_provenance/per_leg_confidence_signal_hunt.json")

# DESI Legacy DR8 imaging leg cuts from the paper (Sec.~per_leg):
#   BASS+MzLS:  dec > +32.375°
#   DES:        dec < -10° AND (ra in the DES RA ranges)
#   DECaLS:     everything else
DES_RA_RANGES = [(0, 60), (300, 360)]  # rough DES south galactic cap


def assign_leg(ra, dec):
    leg = np.full(len(ra), "DECaLS", dtype=object)
    leg[dec > 32.375] = "BASS+MzLS"
    des_mask = (dec < -10) & (
        ((ra >= 0) & (ra <= 60)) | ((ra >= 300) & (ra <= 360))
    )
    leg[des_mask] = "DES"
    return leg


def dipole_amplitude(n_total, n_cw):
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
    A = (X * w[:, None]).T @ X
    b = (X * w[:, None]).T @ p
    try:
        c = np.linalg.solve(A, b)
    except np.linalg.LinAlgError:
        return 0.0
    return float(2.0 * np.sqrt(c[0]**2 + c[1]**2 + c[2]**2))


def dipole_significance(df_sub):
    rng = np.random.default_rng(SEED)
    pix = hp.ang2pix(NSIDE, np.radians(90.0 - df_sub["dec"].values),
                     np.radians(df_sub["ra"].values))
    n_total = np.bincount(pix, minlength=hp.nside2npix(NSIDE))
    cw_mask = df_sub["class_eq"].values == "CW"
    n_cw_obs = np.bincount(pix[cw_mask], minlength=hp.nside2npix(NSIDE))
    n_spirals = int(n_total.sum())
    p_cw = n_cw_obs.sum() / max(n_spirals, 1)
    A_obs = dipole_amplitude(n_total, n_cw_obs)

    # Monopole-preserving null
    A_null = np.zeros(N_MC)
    for i in range(N_MC):
        n_null = rng.binomial(n_total, p_cw)
        A_null[i] = dipole_amplitude(n_total, n_null)
    null_mean = A_null.mean()
    null_std = A_null.std(ddof=1)
    sigma_mono = (A_obs - null_mean) / (null_std + 1e-30)

    # Isotropic-p=0.5 null
    rng2 = np.random.default_rng(SEED + 1)
    A_iso = np.zeros(N_MC)
    for i in range(N_MC):
        n_iso = rng2.binomial(n_total, 0.5)
        A_iso[i] = dipole_amplitude(n_total, n_iso)
    sigma_iso = (A_obs - A_iso.mean()) / (A_iso.std(ddof=1) + 1e-30)

    return {
        "N_spiral": n_spirals,
        "p_CW": float(p_cw),
        "A_obs_pct": A_obs * 100,
        "sigma_monopole_preserving": float(sigma_mono),
        "sigma_isotropic": float(sigma_iso),
    }


def main():
    t0 = time.time()
    print(f"[{time.time()-t0:.1f}s] Loading catalog ...", flush=True)
    p = hf_hub_download("bamfai/galaxy-chirality-catalog", "catalog_production.parquet", repo_type="dataset")
    df = pd.read_parquet(p, columns=["ra", "dec", "class_eq", "p_cw_eq", "p_ccw_eq"])
    spirals = df[df["class_eq"].isin(["CW", "CCW"])].reset_index(drop=True)
    spirals["max_eq"] = spirals[["p_cw_eq", "p_ccw_eq"]].max(axis=1)
    spirals["leg"] = assign_leg(spirals["ra"].values, spirals["dec"].values)
    print(f"[{time.time()-t0:.1f}s] spirals: {len(spirals):,}", flush=True)
    print(f"  per-leg counts: {spirals['leg'].value_counts().to_dict()}", flush=True)

    confidence_bins = [(0.4, 0.5), (0.5, 0.6), (0.6, 0.7), (0.7, 0.8), (0.8, 1.0)]
    legs = ["BASS+MzLS", "DECaLS", "DES"]

    results = {}
    print(f"\n[{time.time()-t0:.1f}s] === per-leg × confidence-bin dipole sweep ===", flush=True)
    print(f"  {'leg':>10s} {'bin':>14s} {'N':>10s} {'p_CW':>9s} {'|A| (%)':>10s} {'σ_iso':>8s} {'σ_mono':>8s}", flush=True)
    for leg in legs:
        for lo, hi in confidence_bins:
            sub = spirals[
                (spirals["leg"] == leg)
                & (spirals["max_eq"] >= lo)
                & (spirals["max_eq"] < hi)
            ]
            if len(sub) < 5000:
                continue
            r = dipole_significance(sub)
            key = f"{leg}_p_eq_{lo:.1f}_{hi:.1f}"
            results[key] = {
                "leg": leg,
                "bin": f"[{lo:.1f},{hi:.1f})",
                **r,
            }
            print(f"  {leg:>10s} [{lo:.1f},{hi:.1f}) {r['N_spiral']:>10,} {r['p_CW']:>9.5f} {r['A_obs_pct']:>10.3f} {r['sigma_isotropic']:>+8.2f} {r['sigma_monopole_preserving']:>+8.2f}", flush=True)

    out = {
        "version": "v1.0.83-per-leg-confidence-signal-hunt",
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "config": {
            "nside": NSIDE,
            "n_mc": N_MC,
            "seed": SEED,
            "confidence_bins": confidence_bins,
            "legs": legs,
            "leg_assignment_rule": "dec>32.375°=BASS+MzLS; dec<-10° AND ra∈[0,60]∪[300,360]=DES; else=DECaLS",
            "rationale": "Cross of per-leg (Sec.~per_leg) and confidence-stratified (Sec.~signal_hunt) signal-hunt. If +3σ low-confidence-bin signal is footprint-correlated systematic, it concentrates in one leg. If it's classifier label noise, roughly uniform across legs.",
        },
        "results": results,
    }
    OUT.write_text(json.dumps(out, indent=2))
    print(f"\nSaved -> {OUT}", flush=True)
    print(f"Total wall: {time.time()-t0:.1f}s", flush=True)


if __name__ == "__main__":
    main()
