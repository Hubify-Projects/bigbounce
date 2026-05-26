#!/usr/bin/env python3
"""
ChatGPT-B5 closure: Full-catalog injection-recovery sweep.

The paper currently reports the empirical 50%-recovery-at-3σ injection
threshold as 0.75% based on the HIGH-CONFIDENCE subsample (N_HC=471,049,
canonical+pixel-count>=10 mask). The ChatGPT reviewer flagged that
this is an HC-subsample-only number whereas the abstract advertises
"sub-percent sensitivity" and is internally inconsistent with the
0.29% Fisher floor + 1.19% symmetric-error-corrected threshold.

The cleanest closure: inject a real cosmological dipole on the FULL
3.2M-spiral catalog (canonical NSIDE=64 mask) at amplitudes
A = {0.005, 0.0075, 0.010, 0.015, 0.020, 0.030}, run the standard
MASTER ℓ=1 decoupling pipeline, and report the empirical 50%-recovery-
at-3σ amplitude on the FULL catalog (not the HC subsample).

Injection model: per-pixel
  A_p^injected(p) = A_p^obs(p) + A_inj * (hat_d . hat_n(p))
where hat_d is the injected dipole axis (default: random per
realization) and hat_n(p) is the unit vector to pixel p.

For each amplitude A:
  - N_MC realizations with random dipole axes drawn isotropically
  - Run MASTER decoupling on each realization
  - Compute σ_inj = (C_1^injected - mean_null) / std_null
  - Record fraction of realizations with σ_inj >= 3.0
  - Median σ and 16/84 percentiles

50%-recovery-at-3σ amplitude is the smallest A where >=50% of
realizations recover σ>=3.

Companion artifact:
  outputs/canonical_provenance/full_catalog_injection_recovery.json
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np
import healpy as hp
import pandas as pd
import pymaster as nmt
from huggingface_hub import hf_hub_download

NSIDE = 64
LMAX = 191
AMPLITUDES = [0.005, 0.0075, 0.010, 0.015, 0.020, 0.030]
N_MC_PER_AMP = 50  # 50 random dipole axes per amplitude
N_NULL = 200  # binomial null realizations for sigma estimation
SEED = 42
OUT = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p2_chirality/outputs/canonical_provenance/full_catalog_injection_recovery.json")


def canonical_mask(nside: int) -> np.ndarray:
    npix = hp.nside2npix(nside)
    theta, phi = hp.pix2ang(nside, np.arange(npix))
    coords = hp.Rotator(coord=["C", "G"])
    theta_g, _ = coords(theta, phi)
    b_deg = 90.0 - np.degrees(theta_g)
    return (np.abs(b_deg) > 15.0).astype(float)


def build_data_maps():
    print(f"[{time.time()-t0:.1f}s] downloading catalog from HF cache ...", flush=True)
    cat_path = hf_hub_download(
        "bamfai/galaxy-chirality-catalog", "catalog_production.parquet", repo_type="dataset"
    )
    df = pd.read_parquet(cat_path, columns=["ra", "dec", "class_eq"])
    df = df.loc[df["class_eq"].isin(["CW", "CCW"])].reset_index(drop=True)
    is_cw = (df["class_eq"].values == "CW").astype(np.int8)
    n_spi = len(df)
    print(f"[{time.time()-t0:.1f}s] spirals: {n_spi:,}", flush=True)

    theta = np.radians(90.0 - df["dec"].values)
    phi = np.radians(df["ra"].values)
    pix = hp.ang2pix(NSIDE, theta, phi)
    npix = hp.nside2npix(NSIDE)
    n_cw = np.bincount(pix, weights=is_cw.astype(np.float64), minlength=npix)
    n_total = np.bincount(pix, minlength=npix).astype(np.float64)
    A_p = np.zeros(npix, dtype=np.float64)
    valid = n_total > 0
    A_p[valid] = 2.0 * (n_cw[valid] / n_total[valid]) - 1.0
    return A_p, n_total, n_spi


def main():
    global t0
    t0 = time.time()
    print(f"[{t0:.1f}s] full-catalog injection-recovery sweep — canonical NSIDE={NSIDE}", flush=True)
    rng = np.random.default_rng(SEED)

    A_p, n_total, n_spi = build_data_maps()
    mask = canonical_mask(NSIDE)
    in_mask = mask > 0
    f_sky = float(in_mask.mean())
    npix = hp.nside2npix(NSIDE)
    print(f"[{time.time()-t0:.1f}s] f_sky={f_sky:.5f} canonical mask", flush=True)

    # Galaxy-weighted mask-mean subtraction
    A_p_corr = A_p - np.average(A_p[in_mask], weights=n_total[in_mask])

    # Per-pixel unit vectors (for cos(theta) injection)
    theta_pix, phi_pix = hp.pix2ang(NSIDE, np.arange(npix))
    n_hat = np.stack([
        np.sin(theta_pix) * np.cos(phi_pix),
        np.sin(theta_pix) * np.sin(phi_pix),
        np.cos(theta_pix),
    ], axis=0)  # shape (3, npix)

    # MASTER coupling matrix
    print(f"[{time.time()-t0:.1f}s] computing MASTER coupling matrix ...", flush=True)
    nmtb = nmt.NmtBin.from_edges(np.arange(1, LMAX + 1), np.arange(2, LMAX + 2))
    wsp = nmt.NmtWorkspace()
    f0_mask = nmt.NmtField(mask, [np.zeros_like(mask)])
    wsp.compute_coupling_matrix(f0_mask, f0_mask, nmtb)
    print(f"[{time.time()-t0:.1f}s] coupling matrix done", flush=True)

    # Build the binomial-monopole null distribution for sigma estimation
    print(f"[{time.time()-t0:.1f}s] building binomial null ({N_NULL} realizations) ...", flush=True)
    p_global = 0.4974  # global CW fraction
    null_C1 = np.zeros(N_NULL, dtype=np.float64)
    n_total_int = n_total.astype(np.int64)
    for k in range(N_NULL):
        n_cw_null = rng.binomial(n_total_int, p_global)
        A_null = np.where(n_total > 0, 2.0 * (n_cw_null / np.maximum(n_total, 1)) - 1.0, 0.0)
        A_null -= np.average(A_null[in_mask], weights=n_total[in_mask])
        f_n = nmt.NmtField(mask, [A_null * mask])
        coupled = nmt.compute_coupled_cell(f_n, f_n)
        null_C1[k] = float(wsp.decouple_cell(coupled)[0][0])
    null_mean = float(null_C1.mean())
    null_std = float(null_C1.std())
    print(f"[{time.time()-t0:.1f}s] null mean={null_mean:.3e} std={null_std:.3e}", flush=True)

    # Data baseline
    f_data = nmt.NmtField(mask, [A_p_corr * mask])
    coupled = nmt.compute_coupled_cell(f_data, f_data)
    C1_data = float(wsp.decouple_cell(coupled)[0][0])
    sigma_data = (C1_data - null_mean) / null_std
    print(f"[{time.time()-t0:.1f}s] data C_1={C1_data:.3e} σ={sigma_data:+.3f}", flush=True)

    # Sweep over amplitudes
    results_per_amp = []
    for amp in AMPLITUDES:
        sigmas = np.zeros(N_MC_PER_AMP, dtype=np.float64)
        for k in range(N_MC_PER_AMP):
            # Random isotropic dipole axis
            v = rng.standard_normal(3)
            d_hat = v / np.linalg.norm(v)
            # Inject A_p^injected(p) = A_p^obs(p) + amp * (d_hat . n_hat(p))
            inj = amp * (d_hat @ n_hat)  # shape (npix,)
            A_inj = A_p_corr + inj
            A_inj_corr = A_inj - np.average(A_inj[in_mask], weights=n_total[in_mask])
            f_inj = nmt.NmtField(mask, [A_inj_corr * mask])
            coupled = nmt.compute_coupled_cell(f_inj, f_inj)
            C1_inj = float(wsp.decouple_cell(coupled)[0][0])
            sigmas[k] = (C1_inj - null_mean) / null_std
        frac_recovered_3sig = float((sigmas >= 3.0).mean())
        median_sigma = float(np.median(sigmas))
        p16, p84 = float(np.percentile(sigmas, 16)), float(np.percentile(sigmas, 84))
        results_per_amp.append({
            "amplitude": amp,
            "n_realizations": N_MC_PER_AMP,
            "median_sigma": median_sigma,
            "p16_sigma": p16,
            "p84_sigma": p84,
            "frac_recovered_at_3sigma": frac_recovered_3sig,
        })
        print(f"[{time.time()-t0:.1f}s]   A={amp:.4f}: median σ={median_sigma:+.2f} "
              f"[{p16:+.2f}, {p84:+.2f}]  frac(σ≥3)={frac_recovered_3sig:.2f}", flush=True)

    # Find 50%-recovery-at-3σ threshold by linear interpolation
    fracs = np.array([r["frac_recovered_at_3sigma"] for r in results_per_amp])
    amps = np.array(AMPLITUDES)
    if (fracs >= 0.5).any() and (fracs < 0.5).any():
        idx_above = np.argmax(fracs >= 0.5)
        a_above = amps[idx_above]
        f_above = fracs[idx_above]
        if idx_above > 0:
            a_below = amps[idx_above - 1]
            f_below = fracs[idx_above - 1]
            threshold_50 = a_below + (0.5 - f_below) * (a_above - a_below) / (f_above - f_below)
        else:
            threshold_50 = a_above
    elif (fracs >= 0.5).all():
        threshold_50 = float(amps[0])
    else:
        threshold_50 = None

    results = {
        "version": "v1.0.134+",
        "purpose": (
            "ChatGPT-B5 closure: full-catalog injection-recovery sweep on the "
            "FULL 3.2M-spiral canonical NSIDE=64 mask via MASTER decoupling. "
            "Closes the abstract 'sub-percent sensitivity' framing by computing "
            "the empirical 50%-recovery-at-3sigma amplitude on the full catalog "
            "rather than the HC subsample (N=471,049). Resolves ChatGPT-B5 "
            "internal-inconsistency flag between 0.29% Fisher / 0.75% HC-subsample "
            "/ 1.19% symmetric-error-corrected thresholds."
        ),
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "config": {
            "nside": NSIDE, "lmax": LMAX,
            "amplitudes": AMPLITUDES,
            "n_mc_per_amplitude": N_MC_PER_AMP,
            "n_null": N_NULL,
            "n_spirals": n_spi,
            "f_sky_canonical": f_sky,
            "seed": SEED,
        },
        "baseline": {
            "data_decoupled_C1": C1_data,
            "null_mean_C1": null_mean,
            "null_std_C1": null_std,
            "data_sigma_from_null": sigma_data,
        },
        "per_amplitude": results_per_amp,
        "threshold_50pct_recovery_at_3sigma_full_catalog": threshold_50,
        "interpretation": (
            "If threshold_50pct_recovery_at_3sigma_full_catalog <= 0.75%, the "
            "abstract 'sub-percent sensitivity' framing holds on the full catalog "
            "and is not an HC-subsample-only claim. If > 0.75% or > 1.0%, the "
            "abstract must downgrade the sensitivity claim accordingly."
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(results, indent=2))
    print(f"\n[{time.time()-t0:.1f}s] FINAL threshold 50%-recovery-at-3σ (full catalog): "
          f"{threshold_50:.5f} ({100*threshold_50:.3f}%)" if threshold_50 else
          f"\n[{time.time()-t0:.1f}s] threshold not bracketed by amplitude grid",
          flush=True)
    print(f"[{time.time()-t0:.1f}s] wrote {OUT}", flush=True)


if __name__ == "__main__":
    main()
