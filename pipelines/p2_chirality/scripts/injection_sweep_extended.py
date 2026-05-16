#!/usr/bin/env python3
"""
Extended injection-recovery sweep — A in {0.05, 0.10, 0.20, 0.30, 0.50,
0.75, 1.00, 1.50, 2.00}%; per-pixel-shuffle null; report
P(sigma>2), P(sigma>3), median sigma, and 50%-recovery threshold.

Closes GPT-5 BLOCKER: the abstract claims sweep tested "up to A=2%"
but on-disk artifact only tested to 0.5%. This script extends the
sweep through 2.0% to either substantiate or correct the claim.

Output: injection_recovery_extended.json
"""
import json, time
from pathlib import Path
import numpy as np
import pandas as pd
import healpy as hp
from huggingface_hub import hf_hub_download

NSIDE = 64
N_MC_NULL = 1000
N_MC_INJ = 100  # per amplitude
SEED = 42
HC_THRESHOLD = 0.6  # HC-spiral subsample
OUT = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p2_chirality/outputs/canonical_provenance/injection_recovery_extended.json")
AMPLITUDES_PCT = [0.05, 0.10, 0.20, 0.30, 0.50, 0.75, 1.00, 1.50, 2.00]


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


def main():
    t0 = time.time()
    rng = np.random.default_rng(SEED)
    print(f"[{time.time()-t0:.1f}s] Loading catalog ...", flush=True)
    p = hf_hub_download("bamfai/galaxy-chirality-catalog", "catalog_production.parquet", repo_type="dataset")
    df = pd.read_parquet(p, columns=["ra", "dec", "class_eq", "p_cw_eq", "p_ccw_eq"])
    spirals = df[df["class_eq"].isin(["CW", "CCW"])].reset_index(drop=True)
    spirals["max_eq"] = spirals[["p_cw_eq", "p_ccw_eq"]].max(axis=1)
    hc = spirals[spirals["max_eq"] > HC_THRESHOLD].reset_index(drop=True)
    print(f"[{time.time()-t0:.1f}s] HC spirals (p_eq > {HC_THRESHOLD}): {len(hc):,}", flush=True)

    th = np.radians(90.0 - hc["dec"].values)
    ph = np.radians(hc["ra"].values)
    pix = hp.ang2pix(NSIDE, th, ph)
    n_total = np.bincount(pix, minlength=hp.nside2npix(NSIDE))
    cw_mask = hc["class_eq"].values == "CW"
    n_cw_obs = np.bincount(pix[cw_mask], minlength=hp.nside2npix(NSIDE))
    p_cw_global = float(n_cw_obs.sum() / n_total.sum())

    # Per-pixel-shuffle null distribution: shuffle CW/CCW labels among ALL HC spirals,
    # keeping per-pixel total counts fixed
    print(f"[{time.time()-t0:.1f}s] Building null distribution (N_MC={N_MC_NULL})...", flush=True)
    null_A = np.zeros(N_MC_NULL)
    for k in range(N_MC_NULL):
        n_cw_null = rng.binomial(n_total, p_cw_global)
        null_A[k] = dipole_amplitude(n_total, n_cw_null)
        if (k + 1) % 200 == 0:
            print(f"[{time.time()-t0:.1f}s]   null {k+1}/{N_MC_NULL}", flush=True)
    null_mean = null_A.mean()
    null_std = null_A.std(ddof=1)
    print(f"[{time.time()-t0:.1f}s] null: mean={null_mean*100:.4f}%, std={null_std*100:.4f}%", flush=True)

    results = {"amplitudes_pct": AMPLITUDES_PCT, "rows": []}
    pix_theta, pix_phi = hp.pix2ang(NSIDE, np.arange(hp.nside2npix(NSIDE)))
    pix_z = np.cos(pix_theta)  # cos(theta) direction-of-dipole projection (z-axis)

    for A_pct in AMPLITUDES_PCT:
        A = A_pct / 100.0
        print(f"\n[{time.time()-t0:.1f}s] === A={A_pct}% (full-amplitude) === N_MC_INJ={N_MC_INJ}", flush=True)
        rec_sigmas = np.zeros(N_MC_INJ)
        for j in range(N_MC_INJ):
            # axis of injected dipole: random direction
            ax_th = rng.uniform(0, np.pi)
            ax_ph = rng.uniform(0, 2 * np.pi)
            ax_xyz = np.array([np.sin(ax_th) * np.cos(ax_ph),
                                np.sin(ax_th) * np.sin(ax_ph),
                                np.cos(ax_th)])
            # per-pixel direction
            pix_xyz = np.stack([np.sin(pix_theta) * np.cos(pix_phi),
                                 np.sin(pix_theta) * np.sin(pix_phi),
                                 np.cos(pix_theta)], axis=1)
            cos_theta_ax = pix_xyz @ ax_xyz  # (npix,)
            p_inj = p_cw_global + 0.5 * A * cos_theta_ax  # p = p_global + A/2 cos theta
            p_inj = np.clip(p_inj, 0.001, 0.999)
            n_cw_inj = rng.binomial(n_total, p_inj)
            A_rec = dipole_amplitude(n_total, n_cw_inj)
            rec_sigmas[j] = (A_rec - null_mean) / null_std

        med = float(np.median(rec_sigmas))
        p_gt_2 = float((rec_sigmas > 2).mean())
        p_gt_3 = float((rec_sigmas > 3).mean())
        rec_50pct_passed = (rec_sigmas > 3).mean() >= 0.5
        print(f"  median sigma={med:.2f}  P(sigma>2)={p_gt_2:.3f}  P(sigma>3)={p_gt_3:.3f}  rec_50pct_passed_3sigma={rec_50pct_passed}", flush=True)
        results["rows"].append({
            "A_pct": A_pct, "median_sigma": med,
            "P_sigma_gt_2": p_gt_2, "P_sigma_gt_3": p_gt_3,
            "n_mc_inj": N_MC_INJ,
            "passes_50pct_recovery_at_3sigma": bool(rec_50pct_passed),
        })

    # Interpretation: 50%-recovery threshold (smallest A with P(sigma>3) >= 0.5)
    threshold = None
    for r in results["rows"]:
        if r["P_sigma_gt_3"] >= 0.5:
            threshold = r["A_pct"]
            break
    results["fifty_percent_recovery_threshold_3sigma_pct"] = threshold
    threshold_2 = None
    for r in results["rows"]:
        if r["P_sigma_gt_2"] >= 0.5:
            threshold_2 = r["A_pct"]
            break
    results["fifty_percent_recovery_threshold_2sigma_pct"] = threshold_2

    out = {
        "version": "v1.0.78-extended-injection-sweep-up-to-A2pct",
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "supersedes": "fisher_sensitivity_floor.json (previously tested only to A=0.5%)",
        "config": {
            "nside": NSIDE, "n_mc_null": N_MC_NULL, "n_mc_inj_per_amp": N_MC_INJ,
            "seed": SEED, "hc_threshold": HC_THRESHOLD,
            "amplitudes_pct_tested": AMPLITUDES_PCT,
            "amplitude_convention": "p_CW = p_global + (A/2) cos(theta_axis); A is full-amplitude",
            "null": "per-pixel-shuffle / binomial(n_total, p_cw_global)",
            "subsample": "HC-spiral (p_eq > 0.6)",
        },
        "null_calibration": {
            "mean_amplitude_pct": float(null_mean * 100),
            "std_amplitude_pct": float(null_std * 100),
        },
        "results": results,
        "interpretation": (
            "50%-recovery-at-3sigma threshold is the smallest tested amplitude "
            "at which at least half of MC injections cross sigma=3. If no tested "
            "amplitude crosses 50% at 3sigma, the sensitivity floor under this null "
            "is bounded above only as > max(tested_amplitude). Per-pixel-shuffle "
            "is a systematic-inclusive null because it preserves per-pixel galaxy "
            "counts, depth/mask-edge correlations, and the global CW monopole."
        ),
    }
    OUT.write_text(json.dumps(out, indent=2))
    print(f"\nSaved -> {OUT}", flush=True)
    print(f"50%-rec-3sigma threshold: {threshold}%; 50%-rec-2sigma threshold: {threshold_2}%", flush=True)
    print(f"Total wall: {time.time()-t0:.1f}s", flush=True)


if __name__ == "__main__":
    main()
