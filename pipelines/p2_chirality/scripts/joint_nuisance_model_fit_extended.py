#!/usr/bin/env python3
"""
Extended joint nuisance-marginalized model fit including leg × confidence
interaction templates (Gemini-M4 closure).

Builds on joint_nuisance_model_fit.py by adding 15 leg × confidence-bin
interaction templates (3 imaging legs × 5 confidence strata) as
additional nuisance amplitudes. This addresses Gemini's Major-4 ask
from the Houston-shared v1.0.132 external review: "include imaging
leg and its interactions with morphology/confidence as nuisance
templates in the primary systematic model".

Design matrix columns (24 total):
   1: dipole_x
   2: dipole_y
   3: dipole_z
   4: leg_BASS
   5: leg_DECaLS
   6: leg_DES
   7-21: 15 leg × confidence-bin interaction templates:
        BASS_c0, BASS_c1, BASS_c2, BASS_c3, BASS_c4,
        DECaLS_c0, DECaLS_c1, DECaLS_c2, DECaLS_c3, DECaLS_c4,
        DES_c0, DES_c1, DES_c2, DES_c3, DES_c4
   22: pixel_density
   23: pixel_density_sq
   24: constant

Conf bins: [0, 0.2), [0.2, 0.4), [0.4, 0.6), [0.6, 0.8), [0.8, 1.0]
where confidence = max(p_CW_eq, p_CCW_eq).

Output: outputs/canonical_provenance/joint_nuisance_model_fit_extended.json
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np
import healpy as hp
import pandas as pd
from huggingface_hub import hf_hub_download

NSIDE = 64
OUT = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p2_chirality/outputs/canonical_provenance/joint_nuisance_model_fit_extended.json")
SEED = 42
DEC_LEG_BOUNDARIES = (-20.0, 32.0)
CONF_EDGES = [0.0, 0.2, 0.4, 0.6, 0.8, 1.01]
CONF_LABELS = ["c0_0.0_0.2", "c1_0.2_0.4", "c2_0.4_0.6", "c3_0.6_0.8", "c4_0.8_1.0"]
LEG_LABELS = ["BASS+MzLS", "DECaLS", "DES"]


def canonical_mask(nside: int) -> np.ndarray:
    npix = hp.nside2npix(nside)
    theta, phi = hp.pix2ang(nside, np.arange(npix))
    coords = hp.Rotator(coord=["C", "G"])
    theta_g, _ = coords(theta, phi)
    b_deg = 90.0 - np.degrees(theta_g)
    return (np.abs(b_deg) > 15.0).astype(float)


def main():
    global t0
    t0 = time.time()
    print(
        f"[{t0:.1f}s] extended joint nuisance-marginalized model fit "
        f"with leg × confidence interactions (canonical NSIDE={NSIDE})",
        flush=True,
    )

    print(f"[{time.time()-t0:.1f}s] downloading catalog from HF cache ...", flush=True)
    cat_path = hf_hub_download(
        "bamfai/galaxy-chirality-catalog",
        "catalog_production.parquet",
        repo_type="dataset",
    )
    df = pd.read_parquet(
        cat_path, columns=["ra", "dec", "class_eq", "p_cw_eq", "p_ccw_eq"]
    )
    df = df.loc[df["class_eq"].isin(["CW", "CCW"])].reset_index(drop=True)
    is_cw = (df["class_eq"].values == "CW").astype(np.int8)
    n_spi = len(df)
    confidence = np.maximum(df["p_cw_eq"].values, df["p_ccw_eq"].values)
    conf_bin = np.digitize(confidence, CONF_EDGES[1:-1])  # 0..4
    dec_g = df["dec"].values
    leg_idx = np.where(
        dec_g > DEC_LEG_BOUNDARIES[1],
        0,  # BASS+MzLS
        np.where(dec_g < DEC_LEG_BOUNDARIES[0], 2, 1),  # DES else DECaLS
    )
    print(f"[{time.time()-t0:.1f}s] spirals: {n_spi:,}", flush=True)
    print(
        f"[{time.time()-t0:.1f}s] confidence-bin distribution (over all spirals):",
        flush=True,
    )
    for i, lbl in enumerate(CONF_LABELS):
        n_bin = int((conf_bin == i).sum())
        print(f"    {lbl}: n={n_bin:,} ({100*n_bin/n_spi:.1f}%)", flush=True)

    npix = hp.nside2npix(NSIDE)
    theta = np.radians(90.0 - df["dec"].values)
    phi = np.radians(df["ra"].values)
    pix = hp.ang2pix(NSIDE, theta, phi)
    n_total = np.bincount(pix, minlength=npix).astype(np.float64)
    n_cw = np.bincount(pix, weights=is_cw.astype(np.float64), minlength=npix)

    # Per-pixel leg-fraction maps
    n_BASS = np.bincount(pix, weights=(leg_idx == 0).astype(np.float64), minlength=npix)
    n_DECaLS = np.bincount(pix, weights=(leg_idx == 1).astype(np.float64), minlength=npix)
    n_DES = np.bincount(pix, weights=(leg_idx == 2).astype(np.float64), minlength=npix)

    # 15 per-pixel leg×conf-bin fraction maps
    leg_conf_maps = np.zeros((3, 5, npix), dtype=np.float64)
    for li in range(3):
        for ci in range(5):
            sel = (leg_idx == li) & (conf_bin == ci)
            leg_conf_maps[li, ci] = np.bincount(
                pix, weights=sel.astype(np.float64), minlength=npix
            )

    A_p = np.zeros(npix, dtype=np.float64)
    valid = n_total > 0
    A_p[valid] = 2.0 * (n_cw[valid] / n_total[valid]) - 1.0

    mask = canonical_mask(NSIDE)
    in_mask = mask > 0
    f_sky = float(in_mask.mean())
    n_in = int(in_mask.sum())
    print(f"[{time.time()-t0:.1f}s] f_sky={f_sky:.5f} n_pix in mask={n_in:,}", flush=True)

    A_p_corr = A_p - np.average(A_p[in_mask], weights=n_total[in_mask])

    theta_pix, phi_pix = hp.pix2ang(NSIDE, np.arange(npix))
    n_hat_x = np.sin(theta_pix) * np.cos(phi_pix)
    n_hat_y = np.sin(theta_pix) * np.sin(phi_pix)
    n_hat_z = np.cos(theta_pix)

    safe_n = np.maximum(n_total, 1.0)
    f_BASS = n_BASS / safe_n
    f_DECaLS = n_DECaLS / safe_n
    f_DES = n_DES / safe_n
    for f in (f_BASS, f_DECaLS, f_DES):
        f -= np.average(f[in_mask], weights=n_total[in_mask])

    # Leg × confidence interaction templates as per-pixel fractions
    leg_conf_frac = np.zeros((3, 5, npix), dtype=np.float64)
    for li in range(3):
        for ci in range(5):
            lcf = leg_conf_maps[li, ci] / safe_n
            lcf -= np.average(lcf[in_mask], weights=n_total[in_mask])
            leg_conf_frac[li, ci] = lcf

    rho_p = n_total / np.maximum(n_total[in_mask].mean(), 1.0)
    rho_p_centered = rho_p - np.average(rho_p[in_mask], weights=n_total[in_mask])
    rho_sq_centered = rho_p_centered ** 2 - np.average(
        rho_p_centered[in_mask] ** 2, weights=n_total[in_mask]
    )

    cols = [n_hat_x, n_hat_y, n_hat_z, f_BASS, f_DECaLS, f_DES]
    col_names = ["dipole_x", "dipole_y", "dipole_z",
                 "leg_BASS", "leg_DECaLS", "leg_DES"]
    for li, ll in enumerate(LEG_LABELS):
        for ci, cl in enumerate(CONF_LABELS):
            cols.append(leg_conf_frac[li, ci])
            col_names.append(f"{ll}_X_{cl}")
    cols += [rho_p_centered, rho_sq_centered, np.ones_like(n_hat_x)]
    col_names += ["pixel_density", "pixel_density_sq", "constant"]

    M_full = np.stack(cols, axis=1)  # (npix, 24)
    M = M_full[in_mask]
    y = A_p_corr[in_mask]
    w = n_total[in_mask]

    # Weighted least squares using pseudoinverse to handle collinearity
    # gracefully (the leg × conf-bin columns + leg + constant span a
    # high-degeneracy null subspace; pinv resolves it via SVD truncation).
    Mw = M * w[:, None]
    MtM = M.T @ Mw
    Mty = M.T @ (w * y)
    a_hat, *_ = np.linalg.lstsq(MtM, Mty, rcond=None)
    residual = y - M @ a_hat
    sigma2_resid = float(np.average(residual ** 2, weights=w))
    Cov_a = sigma2_resid * np.linalg.pinv(MtM, rcond=1e-10)
    sigma_a = np.sqrt(np.maximum(np.diag(Cov_a), 0.0))

    a_dipole_vec = a_hat[:3]
    A_dipole_best = float(np.linalg.norm(a_dipole_vec))
    Cov_dipole = Cov_a[:3, :3]
    if A_dipole_best > 0:
        n_unit = a_dipole_vec / A_dipole_best
        sigma_A_dipole = float(np.sqrt(n_unit @ Cov_dipole @ n_unit))
    else:
        sigma_A_dipole = float(np.sqrt(np.trace(Cov_dipole) / 3))

    A_ref_paper = 0.034
    z_dipole = A_dipole_best / sigma_A_dipole if sigma_A_dipole > 0 else 0.0
    z_from_017 = (
        (A_dipole_best - A_ref_paper) / sigma_A_dipole
        if sigma_A_dipole > 0
        else 0.0
    )

    print(f"\n[{time.time()-t0:.1f}s] DIPOLE POSTERIOR (24-template fit):", flush=True)
    print(f"  A_dipole_best  = {A_dipole_best:.4e}  ({100*A_dipole_best/2:.3f}% in f_CW)", flush=True)
    print(f"  σ_A_dipole     = {sigma_A_dipole:.4e}  ({100*sigma_A_dipole/2:.3f}% in f_CW)", flush=True)
    print(f"  z_data_vs_0    = {z_dipole:+.2f}", flush=True)
    print(f"  z_data_vs_017  = {z_from_017:+.2f}", flush=True)

    # Print the leg × conf interaction z-scores
    print(f"\n[{time.time()-t0:.1f}s] LEG × CONF interaction z-scores:", flush=True)
    print(f"  {'leg/conf':16s}", end="")
    for cl in CONF_LABELS:
        print(f" {cl[:8]:>8s}", end="")
    print()
    for li, ll in enumerate(LEG_LABELS):
        print(f"  {ll:16s}", end="")
        for ci, cl in enumerate(CONF_LABELS):
            name = f"{ll}_X_{cl}"
            i = col_names.index(name)
            z = a_hat[i] / sigma_a[i] if sigma_a[i] > 0 else 0.0
            print(f" {z:+8.2f}", end="")
        print()

    print(f"\n[{time.time()-t0:.1f}s] PRIMARY NUISANCE z-scores:", flush=True)
    for n in ["pixel_density", "pixel_density_sq", "constant"]:
        i = col_names.index(n)
        z = a_hat[i] / sigma_a[i] if sigma_a[i] > 0 else 0.0
        print(f"  {n:18s} a_hat={a_hat[i]:+.4e}  σ={sigma_a[i]:.4e}  z={z:+.2f}", flush=True)

    A_dipole_99 = (
        max(0.0, A_dipole_best - 2.576 * sigma_A_dipole),
        A_dipole_best + 2.576 * sigma_A_dipole,
    )

    if A_ref_paper > A_dipole_99[1]:
        excl = "99%"
    elif A_ref_paper > A_dipole_best + 1.96 * sigma_A_dipole:
        excl = "95%"
    else:
        excl = "<95%"

    results = {
        "version": "v1.0.137+",
        "purpose": (
            "Gemini-M4 closure: extended joint nuisance-marginalized fit including "
            "15 leg × confidence-bin interaction templates as nuisance amplitudes "
            "on top of the dipole + leg + density + density^2 + constant basis. "
            "Tests whether the v1.0.137 single-leg-fraction nuisance is sufficient "
            "or whether the DECaLS-concentrated +4.50σ low-confidence cell of "
            "Table IX absorbs additional residual when given a dedicated nuisance "
            "amplitude."
        ),
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "config": {
            "nside": NSIDE,
            "n_spirals": n_spi,
            "f_sky_canonical": f_sky,
            "n_pix_in_mask": n_in,
            "design_columns": col_names,
            "n_templates": len(col_names),
            "conf_edges": CONF_EDGES,
            "conf_labels": CONF_LABELS,
            "leg_labels": LEG_LABELS,
            "fit_method": "weighted_least_squares_pinv_SVD_collinearity_safe",
            "A_ref_paper_dipole_in_A_p_units": A_ref_paper,
        },
        "amplitudes": {
            name: {
                "a_hat": float(a_hat[i]),
                "sigma": float(sigma_a[i]),
                "z": float(a_hat[i] / sigma_a[i]) if sigma_a[i] > 0 else 0.0,
            }
            for i, name in enumerate(col_names)
        },
        "dipole_posterior": {
            "A_dipole_best_A_p_units": A_dipole_best,
            "A_dipole_best_pct_fCW": 100 * A_dipole_best / 2,
            "sigma_A_dipole_A_p_units": sigma_A_dipole,
            "sigma_A_dipole_pct_fCW": 100 * sigma_A_dipole / 2,
            "z_data_vs_zero": z_dipole,
            "z_data_vs_017_pct": z_from_017,
            "CI_99_A_p_units": list(A_dipole_99),
            "interpretation_i_017pct_excluded_at": excl,
            "residual_variance": sigma2_resid,
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(results, indent=2))
    print(f"\n[{time.time()-t0:.1f}s] interpretation-(i) 1.7% excluded at: {excl}", flush=True)
    print(f"[{time.time()-t0:.1f}s] wrote {OUT}", flush=True)


if __name__ == "__main__":
    main()
