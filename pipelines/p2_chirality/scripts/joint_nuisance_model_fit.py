#!/usr/bin/env python3
"""
Joint nuisance-marginalized model fit (the canonical formal-exclusion
path for interpretation (i) "real cosmological dipole at ~1.7%").

The paper currently characterizes interpretation (i) as "disfavored,
but does not formally exclude" because the bootstrap variance is too
wide and three discriminators (ℓ=2 > ℓ=1, p_eq quartile washout,
cross-spectrum quadrupole anti-alignment) are EACH suggestive rather
than confirmatory under proper multiplicity treatment.

The canonical formal-exclusion path Gemini-B2 + ChatGPT-B3 asked
for is a JOINT linear-regression fit where:
  data:    A_p (the demonopole-subtracted chirality asymmetry map)
  design:  M[N_pixels, N_templates]
              cols = {dipole_x, dipole_y, dipole_z, leg_BASS,
                      leg_DECaLS, leg_DES, pixel_density,
                      pixel_density^2, constant}
  fit:     min ||A_p - M @ a||^2 over coefficient vector a
  result:  posterior on (a_x, a_y, a_z) → posterior on
           A_dipole = sqrt(a_x^2 + a_y^2 + a_z^2)

Marginalizing over the nuisance amplitudes (leg, pixel_density,
constant) gives the formal posterior on the primordial dipole
amplitude WITH the depth/leg/density nuisance modeled as joint
competing components. If A_dipole's posterior CI excludes 1.7%,
interpretation (i) is formally excluded. If it INCLUDES 1.7%,
interpretation (i) is not formally excluded by the linear-regression
treatment.

This is CPU-feasible LOCAL: just numpy linear-algebra on ~30K
in-mask pixels × 9 templates. Wall time < 1 second.

Output:
  pipelines/p2_chirality/outputs/canonical_provenance/
    joint_nuisance_model_fit.json
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
OUT = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p2_chirality/outputs/canonical_provenance/joint_nuisance_model_fit.json")
SEED = 42

# DR8 imaging-leg boundaries (RA/Dec rough approximation):
#   BASS+MzLS  : Dec > +32 deg
#   DECaLS     : -20 < Dec < +32 deg
#   DES        : Dec < -20 deg
DEC_LEG_BOUNDARIES = (-20.0, 32.0)


def canonical_mask(nside: int) -> np.ndarray:
    npix = hp.nside2npix(nside)
    theta, phi = hp.pix2ang(nside, np.arange(npix))
    coords = hp.Rotator(coord=["C", "G"])
    theta_g, _ = coords(theta, phi)
    b_deg = 90.0 - np.degrees(theta_g)
    return (np.abs(b_deg) > 15.0).astype(float)


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

    npix = hp.nside2npix(NSIDE)
    theta = np.radians(90.0 - df["dec"].values)
    phi = np.radians(df["ra"].values)
    pix = hp.ang2pix(NSIDE, theta, phi)
    n_cw = np.bincount(pix, weights=is_cw.astype(np.float64), minlength=npix)
    n_total = np.bincount(pix, minlength=npix).astype(np.float64)

    # Per-leg galaxy counts (BASS+MzLS / DECaLS / DES) by per-galaxy declination
    dec_g = df["dec"].values
    leg_BASS_mask_g = dec_g > DEC_LEG_BOUNDARIES[1]
    leg_DES_mask_g = dec_g < DEC_LEG_BOUNDARIES[0]
    leg_DECaLS_mask_g = ~(leg_BASS_mask_g | leg_DES_mask_g)
    n_BASS = np.bincount(pix, weights=leg_BASS_mask_g.astype(np.float64), minlength=npix)
    n_DECaLS = np.bincount(pix, weights=leg_DECaLS_mask_g.astype(np.float64), minlength=npix)
    n_DES = np.bincount(pix, weights=leg_DES_mask_g.astype(np.float64), minlength=npix)

    # Asymmetry map
    A_p = np.zeros(npix, dtype=np.float64)
    valid = n_total > 0
    A_p[valid] = 2.0 * (n_cw[valid] / n_total[valid]) - 1.0

    return A_p, n_total, n_BASS, n_DECaLS, n_DES, n_spi


def main():
    global t0
    t0 = time.time()
    print(
        f"[{t0:.1f}s] joint nuisance-marginalized model fit "
        f"(canonical NSIDE={NSIDE})",
        flush=True,
    )
    rng = np.random.default_rng(SEED)

    A_p, n_total, n_BASS, n_DECaLS, n_DES, n_spi = build_data_and_templates()
    mask = canonical_mask(NSIDE)
    in_mask = mask > 0
    pix_idx = np.where(in_mask)[0]
    n_in = len(pix_idx)
    f_sky = float(in_mask.mean())
    print(f"[{time.time()-t0:.1f}s] f_sky={f_sky:.5f}, n_pix in mask={n_in:,}",
          flush=True)

    # Galaxy-weighted mask-mean subtraction (canonical convention)
    A_p_corr = A_p - np.average(A_p[in_mask], weights=n_total[in_mask])

    # Per-pixel unit vectors
    theta_pix, phi_pix = hp.pix2ang(NSIDE, np.arange(hp.nside2npix(NSIDE)))
    n_hat_x = np.sin(theta_pix) * np.cos(phi_pix)
    n_hat_y = np.sin(theta_pix) * np.sin(phi_pix)
    n_hat_z = np.cos(theta_pix)

    # Per-leg fractional indicator (avoiding divide-by-zero on empty pixels)
    safe_n = np.maximum(n_total, 1.0)
    f_BASS = n_BASS / safe_n
    f_DECaLS = n_DECaLS / safe_n
    f_DES = n_DES / safe_n
    # Make leg fractions zero-mean inside the mask so they're orthogonal-ish
    # to a constant offset
    for f in (f_BASS, f_DECaLS, f_DES):
        f -= np.average(f[in_mask], weights=n_total[in_mask])

    # Pixel-density normalized + centered
    rho_p = n_total / np.maximum(n_total[in_mask].mean(), 1.0)
    rho_p_centered = rho_p - np.average(rho_p[in_mask], weights=n_total[in_mask])
    rho_sq_centered = (
        rho_p_centered ** 2
        - np.average(rho_p_centered[in_mask] ** 2, weights=n_total[in_mask])
    )

    # Design matrix columns
    col_names = [
        "dipole_x",
        "dipole_y",
        "dipole_z",
        "leg_BASS",
        "leg_DECaLS",
        "leg_DES",
        "pixel_density",
        "pixel_density_sq",
        "constant",
    ]
    M_full = np.stack(
        [
            n_hat_x,
            n_hat_y,
            n_hat_z,
            f_BASS,
            f_DECaLS,
            f_DES,
            rho_p_centered,
            rho_sq_centered,
            np.ones_like(n_hat_x),
        ],
        axis=1,
    )  # shape (npix, 9)

    # Restrict to in-mask pixels for fit; weight by per-pixel inverse Poisson
    # variance ∝ n_total (more galaxies in pixel → tighter constraint)
    M = M_full[in_mask]                          # (n_in, 9)
    y = A_p_corr[in_mask]                        # (n_in,)
    w = n_total[in_mask]                          # (n_in,) galaxy counts
    # Weighted least squares: argmin sum_i w_i (y_i - M_i @ a)^2
    # → solve (M^T W M) a = M^T W y
    W = w / w.sum()
    Mw = M * w[:, None]
    MtM = M.T @ Mw            # (9, 9)  weighted normal matrix
    Mty = M.T @ (w * y)        # (9,)    weighted RHS
    a_hat = np.linalg.solve(MtM, Mty)
    # Residual variance estimate
    residual = y - M @ a_hat
    sigma2_resid = float(np.average(residual ** 2, weights=w))
    # Parameter covariance
    Cov_a = sigma2_resid * np.linalg.inv(MtM)
    sigma_a = np.sqrt(np.diag(Cov_a))

    # Dipole amplitude posterior: A_dipole = sqrt(a_x^2 + a_y^2 + a_z^2)
    # Use linearized error propagation around the best-fit dipole vector
    a_dipole_vec = a_hat[:3]
    A_dipole_best = float(np.linalg.norm(a_dipole_vec))
    Cov_dipole = Cov_a[:3, :3]
    if A_dipole_best > 0:
        n_unit = a_dipole_vec / A_dipole_best
        sigma_A_dipole = float(np.sqrt(n_unit @ Cov_dipole @ n_unit))
    else:
        sigma_A_dipole = float(np.sqrt(np.trace(Cov_dipole) / 3))

    # Convert A_dipole into the convention the paper uses:
    # dipole amplitude in units of A_p (so the test against A=1.7% is direct)
    # Here a_hat already lives in the A_p map's natural units (f_CW - 0.5
    # times factor 2 → equivalent to 2(f_CW - 0.5)), so A_dipole IS the
    # dipole magnitude in the same A_p units. Convert to f_CW-amplitude
    # (A in "2*(f_CW - 0.5)" convention is already the dipole's
    # peak-to-trough amplitude on A_p scale).

    # Marginalized z-score: data vs zero-dipole hypothesis
    z_dipole = A_dipole_best / sigma_A_dipole if sigma_A_dipole > 0 else 0.0

    # Distance from interpretation (i) reference amplitude A_ref = 0.017
    # in 2*(f_CW - 0.5) units. 1.7% f_CW dipole = 0.034 in A_p amplitude.
    A_ref_paper = 0.034
    z_from_017 = (A_dipole_best - A_ref_paper) / sigma_A_dipole if sigma_A_dipole > 0 else 0.0

    # Nuisance amplitudes
    nuisance = {
        col_names[i]: {
            "a_hat": float(a_hat[i]),
            "sigma": float(sigma_a[i]),
            "z": float(a_hat[i] / sigma_a[i]) if sigma_a[i] > 0 else 0.0,
        }
        for i in range(len(col_names))
    }
    print(
        f"\n[{time.time()-t0:.1f}s] FIT RESULTS:",
        flush=True,
    )
    for name, vals in nuisance.items():
        print(
            f"  {name:18s} a_hat = {vals['a_hat']:+.4e}  σ = {vals['sigma']:.4e}  z = {vals['z']:+.2f}",
            flush=True,
        )

    print(
        f"\n[{time.time()-t0:.1f}s] DIPOLE POSTERIOR (marginalized over nuisance):",
        flush=True,
    )
    print(
        f"  A_dipole_best  = {A_dipole_best:.4e}  ({100*A_dipole_best/2:.2f}% in f_CW)",
        flush=True,
    )
    print(
        f"  σ_A_dipole     = {sigma_A_dipole:.4e}  ({100*sigma_A_dipole/2:.2f}% in f_CW)",
        flush=True,
    )
    print(
        f"  z_data_vs_0    = {z_dipole:+.2f}",
        flush=True,
    )
    print(
        f"  Reference A_ref (1.7% f_CW dipole = 0.034 A_p amplitude):",
        flush=True,
    )
    print(
        f"    z_data_vs_017 = {z_from_017:+.2f}  "
        f"(if |z|>3, interpretation (i) at 1.7% f_CW formally excluded)",
        flush=True,
    )

    # Confidence interval on A_dipole at 68% / 95% / 99%
    A_dipole_68 = (
        max(0.0, A_dipole_best - 1.0 * sigma_A_dipole),
        A_dipole_best + 1.0 * sigma_A_dipole,
    )
    A_dipole_95 = (
        max(0.0, A_dipole_best - 1.96 * sigma_A_dipole),
        A_dipole_best + 1.96 * sigma_A_dipole,
    )
    A_dipole_99 = (
        max(0.0, A_dipole_best - 2.576 * sigma_A_dipole),
        A_dipole_best + 2.576 * sigma_A_dipole,
    )

    interpretation_i_excluded_at = None
    if A_ref_paper > A_dipole_99[1]:
        interpretation_i_excluded_at = "99%"
    elif A_ref_paper > A_dipole_95[1]:
        interpretation_i_excluded_at = "95%"
    elif A_ref_paper > A_dipole_68[1]:
        interpretation_i_excluded_at = "68%"
    else:
        interpretation_i_excluded_at = (
            "NOT FORMALLY EXCLUDED at 68% (A_ref within 1σ posterior)"
        )

    results = {
        "version": "v1.0.136+",
        "purpose": (
            "Joint nuisance-marginalized linear-regression model fit for the "
            "primordial dipole amplitude, with depth/leg/density templates as "
            "competing nuisance components. This is the formal-exclusion path "
            "Gemini-B2 + ChatGPT-B3 requested. Marginalizing over the nuisance "
            "amplitudes yields the posterior on the primordial dipole amplitude "
            "A_dipole = sqrt(a_x^2 + a_y^2 + a_z^2)."
        ),
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "config": {
            "nside": NSIDE,
            "n_spirals": n_spi,
            "f_sky_canonical": f_sky,
            "n_pix_in_mask": n_in,
            "design_columns": col_names,
            "fit_method": "weighted_least_squares_galaxy_count",
            "A_ref_paper_dipole_in_A_p_units": A_ref_paper,
        },
        "fit": {
            "nuisance_amplitudes": nuisance,
            "residual_variance": sigma2_resid,
        },
        "dipole_posterior": {
            "A_dipole_best_A_p_units": A_dipole_best,
            "A_dipole_best_pct_fCW": 100 * A_dipole_best / 2,
            "sigma_A_dipole_A_p_units": sigma_A_dipole,
            "sigma_A_dipole_pct_fCW": 100 * sigma_A_dipole / 2,
            "z_data_vs_zero": z_dipole,
            "z_data_vs_017_pct": z_from_017,
            "CI_68_A_p_units": list(A_dipole_68),
            "CI_95_A_p_units": list(A_dipole_95),
            "CI_99_A_p_units": list(A_dipole_99),
            "interpretation_i_017pct_excluded_at": interpretation_i_excluded_at,
        },
        "interpretation": (
            "If |z_data_vs_017_pct| > 3, the joint nuisance-marginalized fit "
            "formally excludes interpretation (i) at the 1.7% f_CW dipole "
            "reference. If z is comparable to the discriminator strengths "
            "elsewhere in the paper (~2-3σ), interpretation (i) is suggestively "
            "but not formally excluded. The nuisance-amplitude z-scores show "
            "which template absorbs the most residual."
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(results, indent=2))
    print(
        f"\n[{time.time()-t0:.1f}s] CI 68%: [{100*A_dipole_68[0]/2:.3f}%, {100*A_dipole_68[1]/2:.3f}%]",
        flush=True,
    )
    print(
        f"[{time.time()-t0:.1f}s] CI 95%: [{100*A_dipole_95[0]/2:.3f}%, {100*A_dipole_95[1]/2:.3f}%]",
        flush=True,
    )
    print(
        f"[{time.time()-t0:.1f}s] CI 99%: [{100*A_dipole_99[0]/2:.3f}%, {100*A_dipole_99[1]/2:.3f}%]",
        flush=True,
    )
    print(
        f"[{time.time()-t0:.1f}s] Interpretation (i) 1.7% f_CW reference: "
        f"{interpretation_i_excluded_at}",
        flush=True,
    )
    print(f"[{time.time()-t0:.1f}s] wrote {OUT}", flush=True)


if __name__ == "__main__":
    main()
