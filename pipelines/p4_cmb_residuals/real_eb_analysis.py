#!/usr/bin/env python3
"""
Analysis 4: REAL EB Cross-Spectrum from Planck PR3 Maps

Downloads actual Planck frequency maps, computes the EB cross-spectrum
using NaMaster, and estimates the cosmic birefringence angle β.

This is a REAL map-level analysis, not a literature recast.

Steps:
1. Download Planck PR3 HFI 143+217 GHz Q/U maps + polarization mask
2. Downgrade to NSIDE=256 for computational tractability
3. Compute C_l^EB using NaMaster pseudo-Cl with mode decoupling
4. Estimate β from EB/EE ratio
5. Null test: if half-mission maps available, check β_null = 0
"""

import os
import sys
import time
import json
import numpy as np

OUTPUT_DIR = "/workspace/analysis4_outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("="*70)
print("ANALYSIS 4: REAL PLANCK EB CROSS-SPECTRUM")
print("="*70)

# ============================================================
# Phase 0: Install dependencies
# ============================================================
print("\n[Phase 0] Installing dependencies...")
os.system("pip install -q healpy numpy scipy matplotlib astropy")

# Try NaMaster — if it fails, we'll use a simpler estimator
try:
    os.system("pip install -q pymaster 2>/dev/null")
    import pymaster as nmt
    HAS_NAMASTER = True
    print("  NaMaster available")
except:
    HAS_NAMASTER = False
    print("  NaMaster not available, using simplified EB estimator")

import healpy as hp

# ============================================================
# Phase 1: Download Planck Maps
# ============================================================
print("\n[Phase 1] Downloading Planck PR3 maps...")

PLANCK_BASE = "https://irsa.ipac.caltech.edu/data/Planck/release_3/all-sky-maps/maps/HFI_SkyMap"
MAP_DIR = "/workspace/planck_maps"
os.makedirs(MAP_DIR, exist_ok=True)

# We need 143 and 217 GHz full-mission maps
# These are ~1.5 GB each at NSIDE=2048
# For speed, try the lower-resolution versions first

maps_to_download = {
    '143': f"{PLANCK_BASE}_143-field-IQU_2048_R3.01_full.fits",
    '217': f"{PLANCK_BASE}_217-field-IQU_2048_R3.01_full.fits",
}

# Also need the common polarization mask
mask_url = "https://irsa.ipac.caltech.edu/data/Planck/release_3/ancillary-data/masks/COM_Mask_CMB-common-Mask-Pol_2048_R3.00.fits"

downloaded_maps = {}
for freq, url in maps_to_download.items():
    outfile = f"{MAP_DIR}/HFI_{freq}_full.fits"
    if os.path.exists(outfile):
        print(f"  {freq} GHz: already downloaded")
        downloaded_maps[freq] = outfile
    else:
        print(f"  Downloading {freq} GHz map (~1.5 GB)...")
        try:
            ret = os.system(f"wget -q --timeout=300 -O {outfile} '{url}'")
            if ret == 0 and os.path.getsize(outfile) > 1e8:
                downloaded_maps[freq] = outfile
                print(f"  {freq} GHz: downloaded ({os.path.getsize(outfile)/1e9:.1f} GB)")
            else:
                print(f"  {freq} GHz: download failed or too small")
                os.remove(outfile) if os.path.exists(outfile) else None
        except Exception as e:
            print(f"  {freq} GHz: download error: {e}")

# Download mask
mask_file = f"{MAP_DIR}/pol_mask.fits"
if not os.path.exists(mask_file):
    print("  Downloading polarization mask...")
    os.system(f"wget -q --timeout=120 -O {mask_file} '{mask_url}'")

# ============================================================
# Phase 2: Load and Process Maps
# ============================================================
print("\n[Phase 2] Loading and processing maps...")

NSIDE_OUT = 256  # Downgrade for speed (full analysis uses 512 or 1024)
LMAX = 3 * NSIDE_OUT - 1  # = 767

if len(downloaded_maps) >= 2:
    print("  Loading 143 GHz and 217 GHz maps...")

    # Load IQU maps
    maps_143 = hp.read_map(downloaded_maps['143'], field=[0, 1, 2])
    maps_217 = hp.read_map(downloaded_maps['217'], field=[0, 1, 2])
    nside_in = hp.get_nside(maps_143)
    print(f"  Input NSIDE: {nside_in}")

    # Load mask
    if os.path.exists(mask_file):
        mask = hp.read_map(mask_file)
        mask = hp.ud_grade(mask, NSIDE_OUT)
        mask[mask < 0.5] = 0
        mask[mask >= 0.5] = 1
        fsky = np.mean(mask)
        print(f"  Mask loaded: f_sky = {fsky:.3f}")
    else:
        mask = np.ones(hp.nside2npix(NSIDE_OUT))
        fsky = 1.0
        print("  No mask — using full sky")

    # Downgrade
    print(f"  Downgrading to NSIDE={NSIDE_OUT}...")
    q143 = hp.ud_grade(maps_143[1], NSIDE_OUT)
    u143 = hp.ud_grade(maps_143[2], NSIDE_OUT)
    q217 = hp.ud_grade(maps_217[1], NSIDE_OUT)
    u217 = hp.ud_grade(maps_217[2], NSIDE_OUT)

    # Apply mask
    q143 *= mask
    u143 *= mask
    q217 *= mask
    u217 *= mask

    # Free memory
    del maps_143, maps_217

    # ============================================================
    # Phase 3: Compute EB Cross-Spectrum
    # ============================================================
    print("\n[Phase 3] Computing EB cross-spectrum...")

    if HAS_NAMASTER:
        print("  Using NaMaster pseudo-Cl estimator...")

        # Create NaMaster fields
        f143 = nmt.NmtField(mask, [q143, u143], purify_b=True)
        f217 = nmt.NmtField(mask, [q217, u217], purify_b=True)

        # Create binning
        b = nmt.NmtBin.from_nside_linear(NSIDE_OUT, 30)
        ell_eff = b.get_effective_ells()

        # Compute workspace (mode coupling matrix)
        print("  Computing mode coupling matrix...")
        w = nmt.NmtWorkspace()
        w.compute_coupling_matrix(f143, f217, b)

        # Compute pseudo-Cl and decouple
        print("  Computing and decoupling spectra...")
        cl_coupled = nmt.compute_coupled_cell(f143, f217)
        cl_decoupled = w.decouple_cell(cl_coupled)

        # cl_decoupled has 4 components: [EE, EB, BE, BB]
        cl_EE = cl_decoupled[0]
        cl_EB = cl_decoupled[1]
        cl_BE = cl_decoupled[2]
        cl_BB = cl_decoupled[3]

    else:
        print("  Using simplified anafast estimator...")

        # Compute alm from Q, U maps
        alm_E143, alm_B143 = hp.map2alm_spin([q143, u143], 2, lmax=LMAX)
        alm_E217, alm_B217 = hp.map2alm_spin([q217, u217], 2, lmax=LMAX)

        # Cross-spectra
        cl_EE = hp.alm2cl(alm_E143, alm_E217)
        cl_EB = hp.alm2cl(alm_E143, alm_B217)
        cl_BE = hp.alm2cl(alm_B143, alm_E217)
        cl_BB = hp.alm2cl(alm_B143, alm_B217)

        ell_eff = np.arange(len(cl_EE))

        # Apply f_sky correction (simplified)
        cl_EE /= fsky
        cl_EB /= fsky
        cl_BE /= fsky
        cl_BB /= fsky

    print(f"  Spectra computed: {len(ell_eff)} ell bins")

    # ============================================================
    # Phase 4: Estimate β
    # ============================================================
    print("\n[Phase 4] Estimating birefringence angle β...")

    # β from EB/EE ratio:
    # C_l^EB ≈ sin(4β)/2 × (C_l^EE - C_l^BB) ≈ 2β × C_l^EE  (for small β)
    # β ≈ C_l^EB / (2 × C_l^EE)  in radians

    # Use ell range 50-500 (where EE signal is strong)
    if HAS_NAMASTER:
        ell_mask = (ell_eff > 50) & (ell_eff < 500)
    else:
        ell_mask = (ell_eff > 50) & (ell_eff < 500)

    if np.sum(ell_mask) > 0:
        # Weighted average: β = Σ(EB_l × EE_l) / Σ(2 × EE_l²)
        numerator = np.sum(cl_EB[ell_mask] * cl_EE[ell_mask])
        denominator = np.sum(2 * cl_EE[ell_mask]**2)

        if denominator > 0:
            beta_rad = numerator / denominator
            beta_deg = np.degrees(beta_rad)

            # Error estimate from scatter in ell bins
            beta_per_ell = cl_EB[ell_mask] / (2 * cl_EE[ell_mask] + 1e-30)
            beta_std = np.std(beta_per_ell) / np.sqrt(np.sum(ell_mask))
            beta_std_deg = np.degrees(beta_std)

            print(f"  β (143×217 cross) = {beta_deg:.3f} ± {beta_std_deg:.3f} degrees")
            print(f"  Significance: {abs(beta_deg)/beta_std_deg:.1f}σ")
        else:
            beta_deg = 0
            beta_std_deg = 999
            print("  WARNING: EE power too low for β estimation")
    else:
        beta_deg = 0
        beta_std_deg = 999
        print("  WARNING: No valid ell bins for β estimation")

    # ============================================================
    # Phase 5: Save Results
    # ============================================================
    print("\n[Phase 5] Saving results...")

    results = {
        'methodology': 'REAL_MAP_LEVEL_EB_ANALYSIS',
        'maps_used': list(downloaded_maps.keys()),
        'nside_analysis': NSIDE_OUT,
        'lmax': int(LMAX),
        'fsky': float(fsky),
        'estimator': 'NaMaster' if HAS_NAMASTER else 'anafast_simplified',
        'beta_deg': float(beta_deg),
        'beta_sigma_deg': float(beta_std_deg),
        'significance_sigma': float(abs(beta_deg) / beta_std_deg) if beta_std_deg > 0 else 0,
        'ell_range': '50-500',
        'comparison': {
            'prediction': 0.27,
            'planck_eskilt': {'beta': 0.30, 'sigma': 0.11},
            'act_dr6': {'beta': 0.215, 'sigma': 0.074},
        },
        'caveat': 'This is a simplified single-cross EB estimator without self-calibration. The result is degenerate with instrumental polarization angle miscalibration. Multi-frequency self-calibration needed for a clean measurement.',
    }

    # Save spectra
    np.savez(f"{OUTPUT_DIR}/eb_spectra.npz",
             ell=ell_eff, cl_EE=cl_EE, cl_EB=cl_EB, cl_BE=cl_BE, cl_BB=cl_BB)

    with open(f"{OUTPUT_DIR}/eb_results.json", 'w') as f:
        json.dump(results, f, indent=2)

    print(f"  Results saved to {OUTPUT_DIR}/")
    print(f"\n  β = {beta_deg:.3f} ± {beta_std_deg:.3f}°")
    print(f"  Bounce prediction: β = 0.27°")
    print(f"  Distance: {abs(beta_deg - 0.27)/beta_std_deg:.1f}σ")

else:
    print("\n  ERROR: Could not download Planck maps.")
    print("  Planck PR3 maps may require registration at PLA.")
    print("  Try: https://pla.esac.esa.int/ or https://irsa.ipac.caltech.edu/data/Planck/")

    # Save error state
    results = {
        'methodology': 'FAILED_DOWNLOAD',
        'error': 'Could not download Planck PR3 maps from IRSA',
        'suggestion': 'Try downloading manually from PLA (pla.esac.esa.int)',
    }
    with open(f"{OUTPUT_DIR}/eb_results.json", 'w') as f:
        json.dump(results, f, indent=2)

print(f"\n{'='*70}")
print(f"ANALYSIS 4 COMPLETE")
print(f"{'='*70}")
