#!/usr/bin/env python3.8
"""
F3.2 — EB Estimator Null Baseline

Compute the EB cross-power spectrum from the Planck SMICA map
and verify it is consistent with zero (the null hypothesis).

This is the FIRST real map-level computation in the F3 pipeline.
It must pass before any birefringence claims.

Steps:
1. Load SMICA Q/U maps and polarization mask
2. Compute pseudo-Cl EB using NaMaster with B-mode purification
3. Verify EB is consistent with zero
4. Estimate beta (polarization rotation angle) from EB/EE ratio
5. Compare against published Planck values

Level: MAP_LEVEL_WIP (first pass, needs null simulations for calibration)
"""

import numpy as np
import healpy as hp
import json
import os

DATA = '/root/bigbounce/F3_cmb_residuals_eb/data/planck_pr3'
OUT = '/root/bigbounce/F3_cmb_residuals_eb/outputs'
os.makedirs(OUT, exist_ok=True)

print('='*70)
print('F3.2 — EB NULL BASELINE')
print('='*70)

# 1. Load maps
print('\nLoading SMICA maps...')
maps = hp.read_map(f'{DATA}/smica_full.fits', field=[0,1,2], verbose=False)
T, Q, U = maps
nside = hp.get_nside(T)
print(f'  NSIDE = {nside}, Npix = {len(T)}')

# 2. Load mask
print('Loading polarization mask...')
mask = hp.read_map(f'{DATA}/mask_pol.fits', field=0, verbose=False)
fsky = np.mean(mask > 0.5)
print(f'  f_sky = {fsky:.4f} ({fsky*100:.1f}% of sky)')

# Apply mask
Q_masked = Q * (mask > 0.5)
U_masked = U * (mask > 0.5)

# 3. Compute pseudo-Cl using healpy (simpler than NaMaster for first pass)
print('\nComputing pseudo-Cl power spectra...')
lmax = 1500  # reasonable for Planck SMICA at NSIDE=2048

# healpy.anafast computes auto/cross spectra
# For polarization: input (T, Q, U), returns TT, EE, BB, TE, EB, TB
cls = hp.anafast([T*mask, Q_masked, U_masked], lmax=lmax)
# cls shape: (6, lmax+1) = [TT, EE, BB, TE, EB, TB]
ell = np.arange(lmax+1)

CL_TT = cls[0]
CL_EE = cls[1]
CL_BB = cls[2]
CL_TE = cls[3]
CL_EB = cls[4]
CL_TB = cls[5]

# Correct for mask (naive fsky correction)
CL_TT /= fsky
CL_EE /= fsky
CL_BB /= fsky
CL_TE /= fsky
CL_EB /= fsky
CL_TB /= fsky

print(f'  Computed Cl up to lmax = {lmax}')

# 4. Estimate beta from EB/EE ratio
# Cosmic birefringence rotates E into B: EB = sin(4β) × (EE-BB)/2 ≈ 2β × EE
# So β ≈ (1/2) × EB/EE (in radians) for small β

# Use ell range 50-1000 (avoid noise at high ell, cosmic variance at low ell)
ell_min, ell_max = 50, 1000
mask_ell = (ell >= ell_min) & (ell <= ell_max)

# Weighted average
weights = (2*ell[mask_ell] + 1)  # cosmic variance weighting
EB_avg = np.average(CL_EB[mask_ell], weights=weights)
EE_avg = np.average(CL_EE[mask_ell], weights=weights)

beta_rad = 0.5 * EB_avg / EE_avg
beta_deg = np.degrees(beta_rad)

print(f'\n  EB/EE analysis (ell = {ell_min}-{ell_max}):')
print(f'    <EB> = {EB_avg:.4e}')
print(f'    <EE> = {EE_avg:.4e}')
print(f'    β = {beta_deg:.4f}° ({beta_rad:.6f} rad)')

# 5. Uncertainty estimate (crude, from scatter)
EB_values = CL_EB[mask_ell]
EE_values = CL_EE[mask_ell]

# Bootstrap uncertainty on β
n_boot = 1000
beta_boots = []
rng = np.random.default_rng(42)
for _ in range(n_boot):
    idx = rng.choice(len(EB_values), size=len(EB_values), replace=True)
    eb_b = np.average(EB_values[idx], weights=weights[idx])
    ee_b = np.average(EE_values[idx], weights=weights[idx])
    beta_boots.append(0.5 * np.degrees(eb_b / ee_b))

beta_boots = np.array(beta_boots)
beta_mean = np.mean(beta_boots)
beta_std = np.std(beta_boots)

print(f'    β (bootstrap) = {beta_mean:.4f} ± {beta_std:.4f}°')

# 6. Null test: is EB consistent with zero?
# Chi-squared: sum of (EB_l / sigma_l)^2
# Rough sigma_l ≈ sqrt(EE_l * BB_l) / sqrt(2l+1) / sqrt(fsky)
sigma_EB = np.sqrt(np.abs(CL_EE[mask_ell] * CL_BB[mask_ell])) / np.sqrt(2*ell[mask_ell]+1) / np.sqrt(fsky)
sigma_EB = np.where(sigma_EB > 0, sigma_EB, 1e-30)

chi2 = np.sum((CL_EB[mask_ell] / sigma_EB)**2)
ndof = np.sum(mask_ell)
chi2_per_dof = chi2 / ndof

print(f'\n  Null test (EB = 0):')
print(f'    χ²/dof = {chi2:.1f}/{ndof} = {chi2_per_dof:.3f}')
if chi2_per_dof < 2.0:
    print(f'    CONSISTENT WITH ZERO (χ²/dof < 2)')
    null_pass = True
else:
    print(f'    POSSIBLE SIGNAL or SYSTEMATICS (χ²/dof > 2)')
    null_pass = False

# 7. Binned EB spectrum for plotting
n_bins = 20
bin_edges = np.logspace(np.log10(ell_min), np.log10(ell_max), n_bins+1).astype(int)
binned_ell = []
binned_EB = []
binned_EE = []
binned_err = []

for i in range(n_bins):
    mask_bin = (ell >= bin_edges[i]) & (ell < bin_edges[i+1])
    if np.sum(mask_bin) == 0:
        continue
    w = 2*ell[mask_bin] + 1
    binned_ell.append(np.average(ell[mask_bin], weights=w))
    binned_EB.append(np.average(CL_EB[mask_bin], weights=w))
    binned_EE.append(np.average(CL_EE[mask_bin], weights=w))
    s = np.sqrt(np.abs(np.average(CL_EE[mask_bin]*CL_BB[mask_bin], weights=w))) / np.sqrt(np.sum(w)) / np.sqrt(fsky)
    binned_err.append(s)

# 8. Summary
print(f'\n' + '='*70)
print(f'SUMMARY')
print(f'='*70)
print(f'''
  Map: Planck PR3 SMICA (2018 Legacy)
  Sky fraction: {fsky*100:.1f}%
  ell range: {ell_min}-{ell_max}

  β estimate: {beta_mean:.3f} ± {beta_std:.3f}°
  Published Planck 2018: β ≈ 0.3 ± 0.3° (Minami & Komatsu)
  Our prediction: β = 0.27°

  Null test (EB=0): χ²/dof = {chi2_per_dof:.3f} — {"PASS" if null_pass else "POSSIBLE SIGNAL"}

  Level: MAP_LEVEL_WIP
  Caveats:
    - Pseudo-Cl with naive fsky correction (no NaMaster purification)
    - No miscalibration angle marginalization
    - No foreground subtraction beyond SMICA
    - No simulation-calibrated uncertainty
    - Bootstrap uncertainty is approximate

  Next steps:
    - F3.3: Injection recovery (inject known β, verify recovery)
    - Upgrade to NaMaster with B-mode purification
    - Run on frequency maps for consistency
    - Simulate null EB from FFP10 for calibrated uncertainty
''')

# 9. Save results
result = {
    'pipeline': 'F3',
    'stage': 'F3.2',
    'level': 'MAP_LEVEL_WIP',
    'map': 'Planck PR3 SMICA 2018',
    'nside': int(nside),
    'fsky': float(fsky),
    'ell_range': [int(ell_min), int(ell_max)],
    'beta_deg': float(beta_mean),
    'beta_err_deg': float(beta_std),
    'beta_rad': float(np.radians(beta_mean)),
    'chi2_per_dof': float(chi2_per_dof),
    'null_test_pass': null_pass,
    'prediction_beta': 0.27,
    'tension_with_prediction': float(abs(beta_mean - 0.27) / beta_std) if beta_std > 0 else None,
    'binned_ell': [float(x) for x in binned_ell],
    'binned_EB': [float(x) for x in binned_EB],
    'binned_EE': [float(x) for x in binned_EE],
    'binned_err': [float(x) for x in binned_err],
    'caveats': [
        'Pseudo-Cl with naive fsky correction',
        'No miscalibration angle marginalization',
        'No NaMaster B-mode purification',
        'Bootstrap uncertainty approximate',
        'No foreground subtraction beyond SMICA',
    ],
}

outfile = f'{OUT}/F3_eb_null_baseline.json'
with open(outfile, 'w') as f:
    json.dump(result, f, indent=2)
print(f'  Saved: {outfile}')
