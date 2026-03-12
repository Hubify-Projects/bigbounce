#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
P6 Tier 2: Map-Level EB Estimator (OPTIONAL)
=============================================

Computes EB cross-power spectrum from Planck PR4/NPIPE frequency maps
and estimates the cosmic birefringence angle beta.

IMPORTANT: This is Tier 2 — it only runs if Planck maps are available
locally and healpy/NaMaster are installed. If any dependency is missing,
the script exits gracefully with a clear message.

Requirements:
  - healpy >= 1.16
  - pymaster >= 1.6 (NaMaster)
  - astropy >= 5.3
  - Planck PR4 maps in data/planck_pr4/ (see tier2_download_maps.sh)

Method:
  1. Load Q/U maps for two frequency channels (e.g., 143 + 217 GHz)
  2. Apply Galactic mask (fsky ~ 0.6)
  3. Compute pseudo-C_l^EB using NaMaster (mode-decoupled)
  4. Fit beta from: C_l^EB = (1/2) sin(4*beta) * (C_l^EE - C_l^BB)
  5. In small-angle limit: beta ~ C_l^EB / (2 * C_l^EE)
  6. Compare with Tier 1 literature values

Null tests:
  - A-B detector split: should give beta consistent with 0
  - Half-ring cross: noise cross-check

Author: Houston Golden (2026)

DISCLAIMER: This is a pipeline development exercise. The estimator is
a simplified version of the full analysis in Minami & Komatsu (2020).
It does NOT include the self-calibration method for separating cosmic
beta from miscalibration angles. The output should be compared with,
not used to replace, the published literature values in Tier 1.
"""

from __future__ import division, print_function
import argparse
import json
import os
import sys
import warnings

import numpy as np

# Check optional dependencies
TIER2_AVAILABLE = True
MISSING_DEPS = []

try:
    import healpy as hp
except ImportError:
    TIER2_AVAILABLE = False
    MISSING_DEPS.append("healpy")

try:
    import pymaster as nmt
except ImportError:
    TIER2_AVAILABLE = False
    MISSING_DEPS.append("pymaster (NaMaster)")

try:
    from astropy.io import fits as astropy_fits
except ImportError:
    # healpy can read FITS directly, astropy is optional
    pass

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


# ===========================================================================
# Configuration
# ===========================================================================

# Planck PR4 frequency channels available for polarization
FREQ_CHANNELS = {
    70: {"nside": 1024, "instrument": "LFI",
         "file": "LFI_SkyMap_070_1024_R4.00_full.fits"},
    100: {"nside": 2048, "instrument": "HFI",
          "file": "HFI_SkyMap_100_2048_R4.00_full.fits"},
    143: {"nside": 2048, "instrument": "HFI",
          "file": "HFI_SkyMap_143_2048_R4.00_full.fits"},
    217: {"nside": 2048, "instrument": "HFI",
          "file": "HFI_SkyMap_217_2048_R4.00_full.fits"},
    353: {"nside": 2048, "instrument": "HFI",
          "file": "HFI_SkyMap_353_2048_R4.00_full.fits"},
}

# Default analysis multipole range
LMIN = 2
LMAX = 1500

# Default mask: use 60% sky fraction (Galactic plane removed)
DEFAULT_FSKY = 0.6


def check_tier2_ready(data_dir):
    """
    Check if Tier 2 prerequisites are met.

    Returns (ready, message).
    """
    if not TIER2_AVAILABLE:
        return False, ("Tier 2 dependencies missing: %s. "
                        "Install with: pip install %s" % (
                            ", ".join(MISSING_DEPS),
                            " ".join(MISSING_DEPS)))

    # Check for at least 2 frequency maps
    map_dir = os.path.join(data_dir, "planck_pr4")
    if not os.path.isdir(map_dir):
        return False, ("Planck PR4 map directory not found: %s. "
                        "Run tier2_download_maps.sh first." % map_dir)

    available_freqs = []
    for freq, info in FREQ_CHANNELS.items():
        path = os.path.join(map_dir, info["file"])
        if os.path.isfile(path):
            available_freqs.append(freq)

    if len(available_freqs) < 2:
        return False, ("Need at least 2 frequency maps for cross-spectrum. "
                        "Found %d: %s" % (len(available_freqs), available_freqs))

    return True, "Tier 2 ready with frequencies: %s" % available_freqs


def load_polarization_maps(data_dir, freq, nside_out=None):
    """
    Load Q, U polarization maps for a given frequency.

    Parameters
    ----------
    data_dir : str
        Base data directory.
    freq : int
        Frequency in GHz.
    nside_out : int or None
        If set, downgrade to this NSIDE.

    Returns
    -------
    Q, U : ndarray
        Polarization maps.
    """
    info = FREQ_CHANNELS[freq]
    path = os.path.join(data_dir, "planck_pr4", info["file"])

    print("Loading %d GHz map: %s" % (freq, path))
    # Planck maps: field 0 = I, field 1 = Q, field 2 = U
    maps = hp.read_map(path, field=[1, 2], dtype=float)
    Q_map = maps[0]
    U_map = maps[1]

    if nside_out is not None and nside_out != info["nside"]:
        print("  Downgrading from NSIDE=%d to %d" % (info["nside"], nside_out))
        Q_map = hp.ud_grade(Q_map, nside_out)
        U_map = hp.ud_grade(U_map, nside_out)

    return Q_map, U_map


def load_or_create_mask(data_dir, nside, fsky_target=DEFAULT_FSKY):
    """
    Load Galactic mask or create a simple latitude-based mask.

    Parameters
    ----------
    data_dir : str
        Base data directory.
    nside : int
        NSIDE of the output mask.
    fsky_target : float
        Target sky fraction.

    Returns
    -------
    mask : ndarray
        Binary mask (1 = observed, 0 = masked).
    fsky : float
        Actual sky fraction.
    """
    # Try loading a Planck common mask
    mask_path = os.path.join(data_dir, "planck_pr4", "common_mask_pol.fits")
    if os.path.isfile(mask_path):
        print("Loading mask: %s" % mask_path)
        mask = hp.read_map(mask_path, dtype=float)
        if hp.get_nside(mask) != nside:
            mask = hp.ud_grade(mask, nside)
        mask = (mask > 0.5).astype(float)
        fsky = np.mean(mask)
        print("  Mask fsky = %.3f" % fsky)
        return mask, fsky

    # Fallback: simple Galactic latitude cut
    print("No mask file found. Creating latitude-based mask for fsky ~ %.2f" %
          fsky_target)
    npix = hp.nside2npix(nside)
    theta, phi = hp.pix2ang(nside, np.arange(npix))
    lat = np.pi / 2.0 - theta  # Galactic latitude in radians

    # Find latitude cut that gives desired fsky
    # fsky = 1 - 2*sin(b_cut)/pi ... approximate, iterate
    b_cut = np.arcsin((1.0 - fsky_target) * np.pi / 2.0)
    mask = (np.abs(lat) > b_cut).astype(float)
    fsky = np.mean(mask)

    # Apodize with a cosine taper (5 degree transition)
    taper_width = np.radians(5.0)
    transition = np.abs(lat) - b_cut
    in_taper = (transition > 0) & (transition < taper_width)
    mask[in_taper] = 0.5 * (1.0 - np.cos(np.pi * transition[in_taper] / taper_width))

    fsky = np.mean(mask)
    print("  Latitude cut b > %.1f deg, fsky = %.3f" % (np.degrees(b_cut), fsky))
    return mask, fsky


def compute_eb_spectrum(Q1, U1, Q2, U2, mask, nside, lmax=LMAX):
    """
    Compute the EB cross-power spectrum between two frequency channels
    using NaMaster for pseudo-C_l estimation with mode decoupling.

    Parameters
    ----------
    Q1, U1 : ndarray
        Polarization maps for frequency 1.
    Q2, U2 : ndarray
        Polarization maps for frequency 2.
    mask : ndarray
        Apodized binary mask.
    nside : int
        NSIDE of the maps.
    lmax : int
        Maximum multipole.

    Returns
    -------
    ells : ndarray
        Multipole centers of the bandpowers.
    cl_eb : ndarray
        EB cross-power spectrum bandpowers.
    cl_ee : ndarray
        EE cross-power spectrum bandpowers (for beta estimation).
    """
    # NaMaster binning
    bin_size = 30
    b = nmt.NmtBin.from_lmax_linear(lmax, bin_size)
    ells = b.get_effective_ells()

    # Create NaMaster fields
    # field_a = [Q1, U1], field_b = [Q2, U2] with spin-2
    f1 = nmt.NmtField(mask, [Q1, U1], purify_b=True)
    f2 = nmt.NmtField(mask, [Q2, U2], purify_b=True)

    # Compute workspace (coupling matrix)
    w = nmt.NmtWorkspace()
    w.compute_coupling_matrix(f1, f2, b)

    # Compute pseudo-C_l and decouple
    cl_coupled = nmt.compute_coupled_cell(f1, f2)
    cl_decoupled = w.decouple_cell(cl_coupled)

    # cl_decoupled has shape (4, n_ells) for spin-2 x spin-2:
    # [EE, EB, BE, BB]
    cl_ee = cl_decoupled[0]
    cl_eb = cl_decoupled[1]

    return ells, cl_eb, cl_ee


def estimate_beta(ells, cl_eb, cl_ee, lmin=50, lmax_fit=1000):
    """
    Estimate cosmic birefringence angle beta from EB/EE ratio.

    In the small-angle approximation:
        C_l^EB ~ 2*beta * C_l^EE  (in radians)

    We fit beta as the inverse-variance weighted ratio.

    Parameters
    ----------
    ells : ndarray
        Multipole centers.
    cl_eb : ndarray
        EB bandpowers.
    cl_ee : ndarray
        EE bandpowers.
    lmin : int
        Minimum multipole for fit.
    lmax_fit : int
        Maximum multipole for fit.

    Returns
    -------
    result : dict
        beta_rad, beta_deg, sigma_rad, sigma_deg, ells_used
    """
    # Select ell range
    mask = (ells >= lmin) & (ells <= lmax_fit) & (cl_ee > 0)
    ells_used = ells[mask]
    eb = cl_eb[mask]
    ee = cl_ee[mask]

    if len(ells_used) == 0:
        return {"beta_rad": 0.0, "beta_deg": 0.0,
                "sigma_rad": float("inf"), "sigma_deg": float("inf"),
                "ells_used": 0, "warning": "No valid ell bins in range"}

    # beta = sum(EB * EE / var) / sum(EE^2 / var)
    # Simplified: assume var ~ EE^2 (sample variance dominated)
    # Then beta ~ sum(EB/EE) / N_bins ... but better to use proper weights

    # Weight by EE^2 (signal-to-noise proxy)
    weights = ee**2
    beta_rad = np.sum(weights * eb / ee) / (2.0 * np.sum(weights))

    # Uncertainty: scatter of EB/EE across bins
    ratios = eb / (2.0 * ee)
    sigma_rad = np.std(ratios) / np.sqrt(len(ratios))

    beta_deg = np.degrees(beta_rad)
    sigma_deg = np.degrees(sigma_rad)

    return {
        "beta_rad": float(beta_rad),
        "beta_deg": float(beta_deg),
        "sigma_rad": float(sigma_rad),
        "sigma_deg": float(sigma_deg),
        "ells_used": int(len(ells_used)),
        "ell_range": [int(ells_used[0]), int(ells_used[-1])],
    }


def make_eb_spectrum_plot(ells, cl_eb, cl_ee, beta_result, output_dir):
    """Plot the EB spectrum and the best-fit beta model."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8), sharex=True)

    # Top: EB spectrum
    ax1.plot(ells, ells * (ells + 1) * cl_eb / (2.0 * np.pi) * 1e12,
             "o-", markersize=3, color="C0", label="D_l^EB (measured)")

    # Model: EB = 2*beta * EE
    beta_rad = beta_result["beta_rad"]
    model_eb = 2.0 * beta_rad * cl_ee
    ax1.plot(ells, ells * (ells + 1) * model_eb / (2.0 * np.pi) * 1e12,
             "--", color="C1", alpha=0.7,
             label="Model: beta = %.3f deg" % beta_result["beta_deg"])

    ax1.axhline(0, color="gray", linestyle=":", linewidth=0.5)
    ax1.set_ylabel("D_l^EB (uK^2)")
    ax1.set_title("EB Cross-Power Spectrum (Tier 2 Estimator)")
    ax1.legend(fontsize=9)

    # Bottom: EE spectrum for reference
    ax2.plot(ells, ells * (ells + 1) * cl_ee / (2.0 * np.pi) * 1e12,
             "o-", markersize=3, color="C2", label="D_l^EE")
    ax2.set_ylabel("D_l^EE (uK^2)")
    ax2.set_xlabel("Multipole l")
    ax2.set_yscale("log")
    ax2.legend(fontsize=9)

    plt.tight_layout()
    for ext in ["pdf", "png"]:
        path = os.path.join(output_dir, "eb_spectrum.%s" % ext)
        fig.savefig(path, dpi=300, bbox_inches="tight")
        print("Saved: %s" % path)
    plt.close(fig)


def run_null_test(data_dir, freq, mask, nside, lmax, output_dir):
    """
    Run A-B detector split null test.

    If A/B split maps are available, compute EB from (A-B) x (A-B).
    This should be consistent with zero (pure noise).
    """
    info = FREQ_CHANNELS[freq]
    base = info["file"].replace("_full.fits", "")
    path_a = os.path.join(data_dir, "planck_pr4", base + "_A.fits")
    path_b = os.path.join(data_dir, "planck_pr4", base + "_B.fits")

    if not (os.path.isfile(path_a) and os.path.isfile(path_b)):
        print("  A/B split maps not available for %d GHz. Skipping null test." % freq)
        return None

    print("Running A-B null test for %d GHz..." % freq)
    maps_a = hp.read_map(path_a, field=[1, 2], dtype=float)
    maps_b = hp.read_map(path_b, field=[1, 2], dtype=float)

    Q_diff = maps_a[0] - maps_b[0]
    U_diff = maps_a[1] - maps_b[1]

    # EB of difference map with itself
    ells, cl_eb_null, cl_ee_null = compute_eb_spectrum(
        Q_diff, U_diff, Q_diff, U_diff, mask, nside, lmax
    )

    beta_null = estimate_beta(ells, cl_eb_null, cl_ee_null)
    print("  Null test beta: %.4f +/- %.4f deg (should be consistent with 0)" % (
        beta_null["beta_deg"], beta_null["sigma_deg"]))

    return {
        "freq_ghz": freq,
        "beta_null_deg": beta_null["beta_deg"],
        "sigma_null_deg": beta_null["sigma_deg"],
        "consistent_with_zero": abs(beta_null["beta_deg"]) < 2.0 * beta_null["sigma_deg"],
    }


def main():
    parser = argparse.ArgumentParser(
        description="P6 Tier 2: Map-level EB estimator (requires Planck PR4 maps)"
    )
    parser.add_argument("--data_dir", type=str, default="data/",
                        help="Base data directory containing planck_pr4/ subdir")
    parser.add_argument("--output_dir", type=str, default="outputs/tier2/",
                        help="Output directory for Tier 2 results")
    parser.add_argument("--freq1", type=int, default=143,
                        help="First frequency channel in GHz (default: 143)")
    parser.add_argument("--freq2", type=int, default=217,
                        help="Second frequency channel in GHz (default: 217)")
    parser.add_argument("--nside", type=int, default=512,
                        help="Analysis NSIDE (default: 512, downgraded from 2048)")
    parser.add_argument("--lmax", type=int, default=LMAX,
                        help="Maximum multipole (default: %d)" % LMAX)
    parser.add_argument("--fsky", type=float, default=DEFAULT_FSKY,
                        help="Target sky fraction for mask (default: %.1f)" % DEFAULT_FSKY)
    args = parser.parse_args()

    print("=" * 60)
    print("P6 CMB EB Pipeline — Tier 2: Map-Level Estimator")
    print("=" * 60)

    # Check prerequisites
    ready, message = check_tier2_ready(args.data_dir)
    if not ready:
        print("\nTier 2 NOT available: %s" % message)
        print("Falling back to Tier 1 only (run beta_registry.py).")
        sys.exit(0)

    print(message)
    os.makedirs(args.output_dir, exist_ok=True)

    # Load maps
    print("\nLoading polarization maps...")
    Q1, U1 = load_polarization_maps(args.data_dir, args.freq1, nside_out=args.nside)
    Q2, U2 = load_polarization_maps(args.data_dir, args.freq2, nside_out=args.nside)

    # Load or create mask
    print("\nPreparing mask...")
    mask, fsky = load_or_create_mask(args.data_dir, args.nside, args.fsky)

    # Compute EB cross-spectrum
    print("\nComputing EB cross-spectrum (%d x %d GHz)..." % (args.freq1, args.freq2))
    ells, cl_eb, cl_ee = compute_eb_spectrum(
        Q1, U1, Q2, U2, mask, args.nside, args.lmax
    )

    # Estimate beta
    print("\nEstimating birefringence angle beta...")
    beta_result = estimate_beta(ells, cl_eb, cl_ee)

    print("\n" + "-" * 40)
    print("TIER 2 RESULT (SIMPLIFIED ESTIMATOR)")
    print("-" * 40)
    print("  beta = %.4f +/- %.4f deg" % (
        beta_result["beta_deg"], beta_result["sigma_deg"]))
    print("  ell range: %s" % beta_result.get("ell_range", "N/A"))
    print("  WARNING: This does NOT include self-calibration.")
    print("  Compare with Tier 1 literature values for validation.")
    print("-" * 40)

    # Save results
    output = {
        "tier": 2,
        "method": "simplified EB/EE ratio estimator",
        "disclaimer": (
            "This is a simplified estimator that does NOT include the "
            "Minami & Komatsu self-calibration method for separating "
            "cosmic birefringence from miscalibration angles. The result "
            "should be compared with, not used to replace, published "
            "literature values."
        ),
        "frequencies_ghz": [args.freq1, args.freq2],
        "nside": args.nside,
        "lmax": args.lmax,
        "fsky": float(fsky),
        "beta_estimate": beta_result,
        "spectra": {
            "ells": ells.tolist(),
            "cl_eb": cl_eb.tolist(),
            "cl_ee": cl_ee.tolist(),
        },
    }

    path = os.path.join(args.output_dir, "tier2_beta_estimate.json")
    with open(path, "w") as f:
        json.dump(output, f, indent=2)
    print("\nSaved: %s" % path)

    # Generate plots
    print("\nGenerating EB spectrum plot...")
    make_eb_spectrum_plot(ells, cl_eb, cl_ee, beta_result, args.output_dir)

    # Run null test if A/B splits available
    print("\nRunning null tests...")
    for freq in [args.freq1, args.freq2]:
        null_result = run_null_test(
            args.data_dir, freq, mask, args.nside, args.lmax, args.output_dir
        )
        if null_result is not None:
            null_path = os.path.join(
                args.output_dir, "null_test_%dGHz.json" % freq)
            with open(null_path, "w") as f:
                json.dump(null_result, f, indent=2)

    print("\nTier 2 complete.")


if __name__ == "__main__":
    main()
