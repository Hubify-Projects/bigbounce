#!/usr/bin/env python3
"""
Block-bootstrap σ on A_dipole for the joint nuisance-marginalized fit.

The headline result in joint_nuisance_model_fit.json reports σ(A_dipole) =
0.006% f_CW with z(data vs 1.7% reference) = -264.5σ under the textbook
WLS estimator Cov_a = σ²_resid · (MᵀWM)⁻¹. That estimator assumes per-pixel
residuals are uncorrelated.

The paper itself documents (§VI.D, multiple anchors) that the canonical-mask
residual is spatially coherent on scales >> 1 pixel (cross-spectrum ℓ=2
r=-0.65, leg-stratified ℓ=1, density-stratified +3.80σ, monopole-leakage
88% unexplained). Under coherent residuals at correlation scale θ_corr,
the effective independent-sample count N_eff drops from N_pix=36,418 toward
O(N_modes_in_systematic), and σ_A_dipole inflates by sqrt(N_pix/N_eff).

This script estimates σ_A_dipole non-parametrically via block-bootstrap
over HEALPix super-pixels at NSIDE=8 (768 super-pixels at ~7.3° each),
which respects spatial coherence on scales smaller than the super-pixel
while sampling the residual systematic's mode structure on scales larger.

Output:
  pipelines/p2_chirality/outputs/canonical_provenance/
    joint_nuisance_bootstrap_sigma.json
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np
import healpy as hp
import pandas as pd
from huggingface_hub import hf_hub_download

NSIDE_DATA = 64
NSIDE_BLOCK = 8
N_BOOTSTRAP = 1000
SEED = 42
A_REF_PAPER_PCT = 1.7

OUT = Path(
    "/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p2_chirality/"
    "outputs/canonical_provenance/joint_nuisance_bootstrap_sigma.json"
)
DEC_LEG_BOUNDARIES = (-20.0, 32.0)


def canonical_mask(nside: int) -> np.ndarray:
    npix = hp.nside2npix(nside)
    theta, phi = hp.pix2ang(nside, np.arange(npix))
    coords = hp.Rotator(coord=["C", "G"])
    theta_g, _ = coords(theta, phi)
    b_deg = 90.0 - np.degrees(theta_g)
    return (np.abs(b_deg) > 15.0).astype(float)


t0 = time.time()


def build_data_and_templates():
    print(f"[{time.time()-t0:.1f}s] downloading catalog from HF cache ...", flush=True)
    cat_path = hf_hub_download(
        "bamfai/galaxy-chirality-catalog",
        "catalog_production.parquet",
        repo_type="dataset",
    )
    df = pd.read_parquet(cat_path, columns=["ra", "dec", "class_eq"])
    df = df.loc[df["class_eq"].isin(["CW", "CCW"])].reset_index(drop=True)
    is_cw = (df["class_eq"].values == "CW").astype(np.int8)
    n_spi = len(df)
    print(f"[{time.time()-t0:.1f}s] spirals: {n_spi:,}", flush=True)

    theta = np.deg2rad(90.0 - df["dec"].values)
    phi = np.deg2rad(df["ra"].values)
    pix = hp.ang2pix(NSIDE_DATA, theta, phi)
    npix = hp.nside2npix(NSIDE_DATA)
    n_total = np.bincount(pix, minlength=npix).astype(np.float64)
    n_cw = np.bincount(pix[is_cw == 1], minlength=npix).astype(np.float64)

    dec_lo, dec_hi = DEC_LEG_BOUNDARIES
    bass = (df["dec"].values > dec_hi).astype(np.int8)
    des = (df["dec"].values < dec_lo).astype(np.int8)
    decals = ((df["dec"].values >= dec_lo) & (df["dec"].values <= dec_hi)).astype(np.int8)
    n_BASS = np.bincount(pix[bass == 1], minlength=npix).astype(np.float64)
    n_DECaLS = np.bincount(pix[decals == 1], minlength=npix).astype(np.float64)
    n_DES = np.bincount(pix[des == 1], minlength=npix).astype(np.float64)

    A_p = np.zeros(npix)
    valid = n_total > 0
    A_p[valid] = 2.0 * (n_cw[valid] / n_total[valid]) - 1.0
    return A_p, n_total, n_BASS, n_DECaLS, n_DES, n_spi


def joint_fit_dipole(A_p, n_total, in_mask, ipix_in, design_cols):
    """Solve weighted least squares; return (a_x, a_y, a_z) on the dipole-only sub-vector."""
    n_in = len(ipix_in)
    M = np.column_stack([col[ipix_in] for col in design_cols])
    w = n_total[ipix_in]
    sw = np.sqrt(w)
    Mw = M * sw[:, None]
    yw = A_p[ipix_in] * sw
    MtM = Mw.T @ Mw
    Mty = Mw.T @ yw
    a_hat = np.linalg.solve(MtM, Mty)
    return a_hat[:3]


def main():
    rng = np.random.default_rng(SEED)
    A_p, n_total, n_BASS, n_DECaLS, n_DES, n_spi = build_data_and_templates()
    npix = hp.nside2npix(NSIDE_DATA)
    cm = canonical_mask(NSIDE_DATA)
    in_mask = (cm > 0) & (n_total > 0)
    ipix_in = np.where(in_mask)[0]
    print(f"[{time.time()-t0:.1f}s] in-mask pixels: {ipix_in.size:,}", flush=True)

    A_p_corr = A_p - np.average(A_p[in_mask], weights=n_total[in_mask])

    theta, phi = hp.pix2ang(NSIDE_DATA, np.arange(npix))
    n_x = np.sin(theta) * np.cos(phi)
    n_y = np.sin(theta) * np.sin(phi)
    n_z = np.cos(theta)

    safe_n = np.maximum(n_total, 1.0)
    f_BASS = n_BASS / safe_n
    f_DECaLS = n_DECaLS / safe_n
    f_DES = n_DES / safe_n
    for f in (f_BASS, f_DECaLS, f_DES):
        f -= np.average(f[in_mask], weights=n_total[in_mask])

    rho_p = n_total / np.maximum(n_total[in_mask].mean(), 1.0)
    rho_p_c = rho_p - np.average(rho_p[in_mask], weights=n_total[in_mask])
    rho_p_sq = rho_p_c ** 2
    rho_p_sq -= np.average(rho_p_sq[in_mask], weights=n_total[in_mask])
    const = np.ones(npix)

    design_cols = [n_x, n_y, n_z, f_BASS, f_DECaLS, f_DES, rho_p_c, rho_p_sq, const]

    a_hat_full = joint_fit_dipole(A_p_corr, n_total, in_mask, ipix_in, design_cols)
    A_dipole_full = float(np.linalg.norm(a_hat_full))
    print(
        f"[{time.time()-t0:.1f}s] full-sample a_hat (x,y,z) = "
        f"({a_hat_full[0]:+.4e}, {a_hat_full[1]:+.4e}, {a_hat_full[2]:+.4e})  "
        f"|A_dipole| = {A_dipole_full:.4e}  ({100*A_dipole_full/2:.3f}% f_CW)",
        flush=True,
    )

    super_pix = hp.ang2pix(NSIDE_BLOCK, theta[ipix_in], phi[ipix_in])
    unique_super = np.unique(super_pix)
    n_super = unique_super.size
    print(
        f"[{time.time()-t0:.1f}s] in-mask spans {n_super} super-pixels (NSIDE={NSIDE_BLOCK})",
        flush=True,
    )

    super_to_local = {sp: np.where(super_pix == sp)[0] for sp in unique_super}

    a_x_boots = np.empty(N_BOOTSTRAP)
    a_y_boots = np.empty(N_BOOTSTRAP)
    a_z_boots = np.empty(N_BOOTSTRAP)
    A_dipole_boots = np.empty(N_BOOTSTRAP)

    print(f"[{time.time()-t0:.1f}s] running {N_BOOTSTRAP} block-bootstrap iterations ...", flush=True)
    for b in range(N_BOOTSTRAP):
        chosen = rng.choice(unique_super, size=n_super, replace=True)
        local_indices = np.concatenate([super_to_local[sp] for sp in chosen])
        ipix_b = ipix_in[local_indices]

        try:
            a_b = joint_fit_dipole(A_p_corr, n_total, in_mask, ipix_b, design_cols)
        except np.linalg.LinAlgError:
            a_b = np.full(3, np.nan)
        a_x_boots[b] = a_b[0]
        a_y_boots[b] = a_b[1]
        a_z_boots[b] = a_b[2]
        A_dipole_boots[b] = float(np.linalg.norm(a_b))
        if (b + 1) % 100 == 0:
            print(
                f"[{time.time()-t0:.1f}s]   {b+1}/{N_BOOTSTRAP}  "
                f"A_dipole_b = {A_dipole_boots[b]:.4e}",
                flush=True,
            )

    valid = ~np.isnan(A_dipole_boots)
    A_boots = A_dipole_boots[valid]
    a_x_v = a_x_boots[valid]
    a_y_v = a_y_boots[valid]
    a_z_v = a_z_boots[valid]
    n_valid = int(valid.sum())

    sigma_A_boot = float(A_boots.std(ddof=1))
    sigma_a_x_boot = float(a_x_v.std(ddof=1))
    sigma_a_y_boot = float(a_y_v.std(ddof=1))
    sigma_a_z_boot = float(a_z_v.std(ddof=1))

    sigma_A_boot_pct = 100 * sigma_A_boot / 2
    A_dipole_pct = 100 * A_dipole_full / 2
    z_vs_1p7_naive = float((A_dipole_full - A_REF_PAPER_PCT/100 * 2) / 1.11e-4)
    z_vs_1p7_boot = float((A_dipole_full - A_REF_PAPER_PCT/100 * 2) / sigma_A_boot) if sigma_A_boot > 0 else float("nan")

    inflation_factor = sigma_A_boot / 1.11e-4

    p16, p50, p84 = np.percentile(A_boots, [16, 50, 84])
    p2p5, p97p5 = np.percentile(A_boots, [2.5, 97.5])
    p0p5, p99p5 = np.percentile(A_boots, [0.5, 99.5])

    result = {
        "script": "joint_nuisance_bootstrap_sigma.py",
        "purpose": "BL-1 (subagent review 2026-05-28): block-bootstrap σ on A_dipole respecting spatial coherence",
        "mask": "(|b_gal| > 15 deg) & (n_total > 0)",
        "n_in_mask_pixels": int(ipix_in.size),
        "n_super_pixels": int(n_super),
        "NSIDE_block": NSIDE_BLOCK,
        "n_bootstrap": int(N_BOOTSTRAP),
        "n_valid_bootstrap": n_valid,
        "seed": SEED,
        "full_sample": {
            "a_x": float(a_hat_full[0]),
            "a_y": float(a_hat_full[1]),
            "a_z": float(a_hat_full[2]),
            "A_dipole_A_p_units": A_dipole_full,
            "A_dipole_pct_fCW": A_dipole_pct,
        },
        "bootstrap": {
            "sigma_a_x": sigma_a_x_boot,
            "sigma_a_y": sigma_a_y_boot,
            "sigma_a_z": sigma_a_z_boot,
            "sigma_A_dipole_A_p_units": sigma_A_boot,
            "sigma_A_dipole_pct_fCW": sigma_A_boot_pct,
            "A_dipole_percentiles": {
                "p0.5": float(p0p5), "p2.5": float(p2p5), "p16": float(p16),
                "p50": float(p50), "p84": float(p84), "p97.5": float(p97p5),
                "p99.5": float(p99p5),
            },
        },
        "comparison": {
            "naive_WLS_sigma_A_dipole_A_p_units": 1.11e-4,
            "naive_WLS_sigma_A_dipole_pct_fCW": 0.006,
            "inflation_factor_boot_over_naive": float(inflation_factor),
            "z_vs_1pct7_reference_naive": z_vs_1p7_naive,
            "z_vs_1pct7_reference_bootstrap": z_vs_1p7_boot,
        },
        "interpretation": (
            "If inflation_factor > ~3 and z_bootstrap < ~10, the 'formally excluded at "
            "264.5σ' rhetoric collapses to a more modest 'excluded at z_bootstrap σ' "
            "and the paper text should be revised."
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2))
    print(f"[{time.time()-t0:.1f}s] wrote {OUT}", flush=True)
    print("\n=== HEADLINE ===")
    print(f"  σ_A_dipole (naive WLS): 0.006% f_CW  (assumed per-pixel independent)")
    print(f"  σ_A_dipole (bootstrap): {sigma_A_boot_pct:.4f}% f_CW  (respects spatial coherence)")
    print(f"  inflation factor:        {inflation_factor:.2f}×")
    print(f"  z(data vs 1.7%) naive:   {z_vs_1p7_naive:+.2f}σ")
    print(f"  z(data vs 1.7%) boot:    {z_vs_1p7_boot:+.2f}σ")


if __name__ == "__main__":
    main()
