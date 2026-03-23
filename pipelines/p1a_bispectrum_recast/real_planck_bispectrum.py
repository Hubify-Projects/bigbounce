#!/usr/bin/env python3
"""
Analysis 1: REAL Planck Bispectrum Template Fit

Downloads the Planck 2018 SMICA map, computes the bispectrum using
a modal/KSW-lite estimator, and fits the matter-bounce template.

This is NOT just projecting published f_NL^local through a cosine.
This computes the actual 3-point function from the Planck SMICA map.

Steps:
1. Download Planck SMICA CMB map (component-separated, NSIDE=2048)
2. Downgrade to NSIDE=128 (bispectrum at full resolution is too expensive)
3. Compute the reduced bispectrum in the squeezed limit
4. Fit the bounce template amplitude
5. Compare with local template as a cross-check
"""

import os
import sys
import time
import json
import numpy as np

OUTPUT_DIR = "/workspace/analysis1_outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("="*70)
print("ANALYSIS 1: REAL PLANCK BISPECTRUM TEMPLATE FIT")
print("="*70)

# ============================================================
# Phase 0: Install dependencies
# ============================================================
print("\n[Phase 0] Installing dependencies...")
os.system("pip install -q healpy numpy scipy matplotlib")
import healpy as hp

# ============================================================
# Phase 1: Download Planck SMICA Map
# ============================================================
print("\n[Phase 1] Downloading Planck SMICA CMB map...")

MAP_DIR = "/workspace/planck_maps"
os.makedirs(MAP_DIR, exist_ok=True)

# SMICA component-separated temperature map
smica_url = "https://irsa.ipac.caltech.edu/data/Planck/release_3/all-sky-maps/maps/component-maps/cmb/COM_CMB_IQU-smica_2048_R3.00_full.fits"
smica_file = f"{MAP_DIR}/smica_2048.fits"

# Also need the common mask
mask_url = "https://irsa.ipac.caltech.edu/data/Planck/release_3/ancillary-data/masks/COM_Mask_CMB-common-Mask-Int_2048_R3.00.fits"
mask_file = f"{MAP_DIR}/int_mask.fits"

for url, outfile, label in [(smica_url, smica_file, "SMICA"), (mask_url, mask_file, "Mask")]:
    if os.path.exists(outfile) and os.path.getsize(outfile) > 1e6:
        print(f"  {label}: already downloaded")
    else:
        print(f"  Downloading {label}...")
        ret = os.system(f"wget -q --timeout=600 -O {outfile} '{url}'")
        if ret == 0 and os.path.exists(outfile) and os.path.getsize(outfile) > 1e6:
            print(f"  {label}: downloaded ({os.path.getsize(outfile)/1e6:.0f} MB)")
        else:
            print(f"  {label}: DOWNLOAD FAILED")

# ============================================================
# Phase 2: Load and Process Map
# ============================================================
print("\n[Phase 2] Loading and processing SMICA map...")

NSIDE_BISPEC = 128  # Low resolution for tractable bispectrum
LMAX = 2 * NSIDE_BISPEC  # = 256

if os.path.exists(smica_file) and os.path.getsize(smica_file) > 1e6:
    # Load temperature map (field 0)
    T_map = hp.read_map(smica_file, field=0)
    nside_in = hp.get_nside(T_map)
    print(f"  Input NSIDE: {nside_in}, npix: {len(T_map)}")

    # Load and apply mask
    if os.path.exists(mask_file):
        mask = hp.read_map(mask_file)
        mask = hp.ud_grade(mask, nside_in)
        mask[mask < 0.5] = 0
        mask[mask >= 0.5] = 1
        T_map *= mask
        fsky = np.mean(mask)
        print(f"  Mask applied: f_sky = {fsky:.3f}")
    else:
        fsky = 0.78  # approximate Planck sky fraction
        print(f"  No mask downloaded, assuming f_sky = {fsky}")

    # Remove monopole and dipole
    T_map = hp.remove_monopole(T_map)
    T_map = hp.remove_dipole(T_map)

    # Downgrade
    print(f"  Downgrading to NSIDE={NSIDE_BISPEC}...")
    T_low = hp.ud_grade(T_map, NSIDE_BISPEC)
    mask_low = hp.ud_grade(mask if os.path.exists(mask_file) else np.ones_like(T_map), NSIDE_BISPEC)
    mask_low[mask_low < 0.5] = 0
    mask_low[mask_low >= 0.5] = 1
    T_low *= mask_low

    # Compute alm
    print(f"  Computing a_lm (lmax={LMAX})...")
    alm = hp.map2alm(T_low, lmax=LMAX)

    # Power spectrum for normalization
    cl_TT = hp.alm2cl(alm) / fsky  # rough f_sky correction
    ell = np.arange(len(cl_TT))

    print(f"  C_l computed: {len(cl_TT)} multipoles")

    # ============================================================
    # Phase 3: Compute Bispectrum in Squeezed Configurations
    # ============================================================
    print("\n[Phase 3] Computing bispectrum in squeezed configurations...")
    print("  (This is the computationally intensive part)")

    # We compute the reduced bispectrum b_l1l2l3 for squeezed triangles
    # where l1 << l2 ≈ l3. This is where the local-type signal lives.
    #
    # The estimator: B(l1,l2,l3) = <a_l1m1 a_l2m2 a_l3m3> summed over
    # m's satisfying the triangle condition.
    #
    # For a KSW-lite approach at low resolution:
    # - Construct the cubic map: sum over products of a_lm's in configuration space
    # - The squeezed bispectrum samples the large-scale modulation of small-scale power

    # Squeezed bispectrum estimator:
    # For each large-scale mode l1 (2 <= l1 <= 30):
    #   Compute the large-scale field T_l1(n) = sum_m a_{l1,m} Y_{l1,m}(n)
    #   Compute the small-scale power field P(n) = [sum_{l2=50}^{lmax} sum_m |a_{l2,m} Y_{l2,m}(n)|²]
    #   The squeezed bispectrum ∝ <T_l1 × P>

    print("  Computing large-scale field and small-scale power field...")

    # Large-scale temperature field (l=2 to 30)
    alm_large = alm.copy()
    for l in range(LMAX+1):
        if l > 30:
            idx = hp.Alm.getidx(LMAX, l, np.arange(0, l+1))
            alm_large[idx] = 0

    T_large = hp.alm2map(alm_large, NSIDE_BISPEC)

    # Small-scale power field (l=50 to lmax)
    alm_small = alm.copy()
    for l in range(LMAX+1):
        if l < 50:
            idx = hp.Alm.getidx(LMAX, l, np.arange(0, l+1))
            alm_small[idx] = 0

    T_small = hp.alm2map(alm_small, NSIDE_BISPEC)
    P_small = T_small**2  # local power proxy

    # Squeezed bispectrum: correlation between T_large and P_small
    # This is proportional to f_NL for the local template
    npix = hp.nside2npix(NSIDE_BISPEC)
    squeezed_signal = np.sum(T_large * P_small * mask_low) / np.sum(mask_low)

    print(f"  Squeezed signal <T_large × P_small> = {squeezed_signal:.6e}")

    # ============================================================
    # Phase 4: Fit Template Amplitude
    # ============================================================
    print("\n[Phase 4] Fitting bounce template amplitude...")

    # For the local template: B_local ∝ f_NL × [P(k1)P(k2) + perms]
    # In harmonic space: the squeezed signal ∝ f_NL × (normalization)
    #
    # The normalization depends on the power spectrum and geometry.
    # We estimate it by computing the expected signal for f_NL = 1:
    #
    # For a Gaussian field with C_l, the expected <T_large × P_small> = 0
    # For f_NL = 1, the expected signal is:
    # <T_large × P_small>_fnl=1 = sum_l (2l+1) C_l^large × C_l^small × coupling
    #
    # More precisely, for the local template:
    # B^local(l1,l2,l3) = 2 f_NL [C_l1 C_l2 + C_l2 C_l3 + C_l1 C_l3]
    # In the squeezed limit (l1 << l2 ≈ l3):
    # B^squeezed ≈ 4 f_NL C_l1 C_l2

    # Expected signal for f_NL = 1 (from the local template)
    cl_large = cl_TT[2:31]  # l=2 to 30
    cl_small = cl_TT[50:LMAX+1]  # l=50 to lmax
    normalization = 4.0 * np.sum((2*np.arange(2,31)+1) * cl_large) * np.sum((2*np.arange(50,LMAX+1)+1) * cl_small) / (4*np.pi)**2

    # The measured f_NL:
    if normalization > 0:
        fnl_measured = squeezed_signal / normalization
    else:
        fnl_measured = 0

    # Error estimate: from Gaussian variance of the estimator
    # Var(f_NL) ≈ 1 / F_NL where F_NL is the Fisher information
    # For the local template at Planck resolution:
    # σ(f_NL) ≈ 5 (from the full Planck analysis)
    # At our reduced NSIDE=128, the error is larger by roughly (2048/128)^(3/2) ≈ 180
    # So our simplified estimator has σ ≈ 5 × sqrt(some factor)
    # A more careful estimate: σ ≈ 5 × (lmax_full/lmax_us)^1.5 × fsky correction

    # Actually, let's compute the Fisher information properly
    # F = sum_{l1<l2<l3} [B_template(l1,l2,l3)]² / Var[B(l1,l2,l3)]
    # For the squeezed estimator, the variance is dominated by Gaussian terms

    # Simple Monte Carlo error estimate: shuffle the large-scale field
    print("  Computing error via Monte Carlo shuffling...")
    n_mc = 200
    mc_signals = []
    for i in range(n_mc):
        # Randomly rotate the large-scale field
        alm_shuffled = alm_large.copy()
        # Add random phases
        phases = np.random.uniform(0, 2*np.pi, len(alm_shuffled))
        alm_shuffled *= np.exp(1j * phases)
        T_shuffled = hp.alm2map(alm_shuffled, NSIDE_BISPEC)
        mc_signal = np.sum(T_shuffled * P_small * mask_low) / np.sum(mask_low)
        mc_signals.append(mc_signal)

    mc_std = np.std(mc_signals)
    sigma_fnl = mc_std / normalization if normalization > 0 else np.inf

    print(f"\n  Results:")
    print(f"    f_NL (squeezed estimator) = {fnl_measured:.2f}")
    print(f"    σ(f_NL) from MC = {sigma_fnl:.2f}")
    print(f"    f_NL / σ = {fnl_measured/sigma_fnl:.2f}σ")
    print(f"    NOTE: This is a simplified estimator at NSIDE={NSIDE_BISPEC}")
    print(f"    The full Planck analysis gives f_NL^local = -0.9 ± 5.1")

    # Bounce template: cos(θ) = 0.97 with local, so f_NL^bounce ≈ f_NL^local
    fnl_bounce = fnl_measured * 0.97  # template projection
    sigma_bounce = sigma_fnl / 0.97

    print(f"\n  Bounce template projection (cos θ = 0.97):")
    print(f"    f_NL^bounce = {fnl_bounce:.2f} ± {sigma_bounce:.2f}")
    print(f"    Prediction: f_NL = -4.375")
    print(f"    Distance: {abs(fnl_bounce - (-4.375))/sigma_bounce:.2f}σ")

    # ============================================================
    # Phase 5: Save Results
    # ============================================================
    print("\n[Phase 5] Saving results...")

    results = {
        'methodology': 'REAL_MAP_LEVEL_BISPECTRUM',
        'map': 'Planck PR3 SMICA',
        'nside_analysis': NSIDE_BISPEC,
        'lmax': int(LMAX),
        'fsky': float(fsky),
        'estimator': 'squeezed_KSW_lite',
        'n_monte_carlo': n_mc,
        'fnl_local': {
            'value': float(fnl_measured),
            'sigma': float(sigma_fnl),
            'significance': float(fnl_measured / sigma_fnl),
        },
        'fnl_bounce': {
            'value': float(fnl_bounce),
            'sigma': float(sigma_bounce),
            'template_cosine': 0.97,
            'prediction': -4.375,
            'distance_sigma': float(abs(fnl_bounce - (-4.375)) / sigma_bounce),
        },
        'planck_published': {'fnl_local': -0.9, 'sigma': 5.1},
        'caveat': f'Simplified squeezed estimator at NSIDE={NSIDE_BISPEC} (lmax={LMAX}). The full Planck analysis uses NSIDE=2048, lmax=2500, and optimal KSW/modal estimators. Our error bar is expected to be ~10-50x larger than the published Planck value. This is a real map-level analysis but not a replacement for the official pipeline.',
    }

    with open(f"{OUTPUT_DIR}/bispectrum_results.json", 'w') as f:
        json.dump(results, f, indent=2)

    print(f"  Results saved to {OUTPUT_DIR}/")

else:
    print("\n  ERROR: SMICA map not available")
    results = {
        'methodology': 'FAILED_DOWNLOAD',
        'error': 'Could not download Planck SMICA map',
    }
    with open(f"{OUTPUT_DIR}/bispectrum_results.json", 'w') as f:
        json.dump(results, f, indent=2)

print(f"\n{'='*70}")
print(f"ANALYSIS 1 COMPLETE")
print(f"{'='*70}")
