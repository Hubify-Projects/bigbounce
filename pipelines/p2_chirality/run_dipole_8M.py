#!/usr/bin/env python3
"""Full dipole analysis on 8.47M galaxy chirality catalog."""
import pandas as pd
import numpy as np
import healpy as hp
import json
import time
from scipy.special import expit

WORK = "/workspace/chirality"

print("Loading Catalog A with coords...")
df = pd.read_parquet(f"{WORK}/catalog_a_with_coords.parquet")
n_total = len(df)
n_coords = df['ra'].notna().sum()
print(f"  {n_total:,} galaxies, {n_coords:,} with coords")

# Spirals only, high confidence
spirals = df[(df['class'].isin(['CW', 'CCW'])) & (df['confidence'] > 0.6) & (df['ra'].notna())]
n_spirals = len(spirals)
cw_frac = (spirals['class'] == 'CW').mean()
print(f"  High-conf spirals: {n_spirals:,}")
print(f"  CW fraction (raw): {cw_frac:.4f}")

# Apply Platt calibration for Catalog B
print("\nApplying Platt calibration (bias=1.58, temp=4.65)...")
logits = np.log(spirals['p_cw'].values / (spirals['p_ccw'].values + 1e-10) + 1e-10)
cal_pcw = expit((logits - 1.5793) / 4.6549)
cal_cw_frac = (cal_pcw > 0.5).mean()
print(f"  CW fraction (calibrated): {cal_cw_frac:.4f}")

# === DIPOLE ON RAW CATALOG A ===
print("\n" + "=" * 60)
print("DIPOLE ANALYSIS: Catalog A (raw)")
print("=" * 60)

NSIDE = 64
npix = hp.nside2npix(NSIDE)
cw_map = np.zeros(npix)
ccw_map = np.zeros(npix)
theta = np.radians(90 - spirals['dec'].values)
phi = np.radians(spirals['ra'].values % 360)
pix = hp.ang2pix(NSIDE, theta, phi)
is_cw = (spirals['class'] == 'CW').values
np.add.at(cw_map, pix, is_cw.astype(float))
np.add.at(ccw_map, pix, (~is_cw).astype(float))

tot = cw_map + ccw_map
mask = tot > 10
asym = np.zeros(npix)
asym[mask] = (cw_map[mask] - ccw_map[mask]) / tot[mask]

n_pix = mask.sum()
print(f"  Pixels used: {n_pix}/{npix}")

asym_full = np.full(npix, hp.UNSEEN)
asym_full[mask] = asym[mask]
mono, dip = hp.fit_dipole(asym_full, gal_cut=0)
amp = np.sqrt(np.sum(dip**2))
l_deg = np.degrees(np.arctan2(dip[1], dip[0])) % 360
b_deg = np.degrees(np.arcsin(dip[2] / amp)) if amp > 0 else 0

print(f"  Monopole: {mono:.5f}")
print(f"  Dipole amplitude: {amp:.5f}")
print(f"  Direction: (l, b) = ({l_deg:.1f}, {b_deg:.1f})")

# Bootstrap 10K
print("  Running 10K bootstrap...")
t0 = time.time()
valid = asym[mask].copy()
boots = []
for _ in range(10000):
    np.random.shuffle(valid)
    asym_shuf = np.full(npix, hp.UNSEEN)
    asym_shuf[mask] = valid
    _, d = hp.fit_dipole(asym_shuf, gal_cut=0)
    boots.append(np.sqrt(np.sum(d**2)))
boots = np.array(boots)
sigma = (amp - np.mean(boots)) / np.std(boots)
pval = np.mean(boots >= amp)
print(f"  Bootstrap ({time.time()-t0:.0f}s): {sigma:.2f}σ (p={pval:.4f})")

# === DIPOLE ON CALIBRATED CATALOG B ===
print("\n" + "=" * 60)
print("DIPOLE ANALYSIS: Catalog B (Platt calibrated)")
print("=" * 60)

cw_map_cal = np.zeros(npix)
ccw_map_cal = np.zeros(npix)
is_cw_cal = cal_pcw > 0.5
np.add.at(cw_map_cal, pix, is_cw_cal.astype(float))
np.add.at(ccw_map_cal, pix, (~is_cw_cal).astype(float))

tot_cal = cw_map_cal + ccw_map_cal
mask_cal = tot_cal > 10
asym_cal = np.zeros(npix)
asym_cal[mask_cal] = (cw_map_cal[mask_cal] - ccw_map_cal[mask_cal]) / tot_cal[mask_cal]

asym_cal_full = np.full(npix, hp.UNSEEN)
asym_cal_full[mask_cal] = asym_cal[mask_cal]
mono_cal, dip_cal = hp.fit_dipole(asym_cal_full, gal_cut=0)
amp_cal = np.sqrt(np.sum(dip_cal**2))
l_cal = np.degrees(np.arctan2(dip_cal[1], dip_cal[0])) % 360
b_cal = np.degrees(np.arcsin(dip_cal[2] / amp_cal)) if amp_cal > 0 else 0

print(f"  Monopole: {mono_cal:.5f}")
print(f"  Dipole amplitude: {amp_cal:.5f}")
print(f"  Direction: (l, b) = ({l_cal:.1f}, {b_cal:.1f})")

valid_cal = asym_cal[mask_cal].copy()
boots_cal = []
print("  Running 10K bootstrap...")
t0 = time.time()
for _ in range(10000):
    np.random.shuffle(valid_cal)
    asym_cal_shuf = np.full(npix, hp.UNSEEN)
    asym_cal_shuf[mask_cal] = valid_cal
    _, d = hp.fit_dipole(asym_cal_shuf, gal_cut=0)
    boots_cal.append(np.sqrt(np.sum(d**2)))
boots_cal = np.array(boots_cal)
sigma_cal = (amp_cal - np.mean(boots_cal)) / np.std(boots_cal)
pval_cal = np.mean(boots_cal >= amp_cal)
print(f"  Bootstrap ({time.time()-t0:.0f}s): {sigma_cal:.2f}σ (p={pval_cal:.4f})")

# === Per-quadrant balance ===
print("\n" + "=" * 60)
print("CW/CCW BALANCE BY SKY REGION")
print("=" * 60)
for ra_lo, ra_hi, name in [(0, 90, 'Q1'), (90, 180, 'Q2'), (180, 270, 'Q3'), (270, 360, 'Q4')]:
    m = (spirals['ra'] >= ra_lo) & (spirals['ra'] < ra_hi)
    if m.sum() > 1000:
        cw_q = (spirals.loc[m, 'class'] == 'CW').mean()
        print(f"  RA [{ra_lo:>3d}-{ra_hi:>3d}): n={m.sum():>8,} CW={cw_q:.4f}")

for dec_lo, dec_hi, name in [(-90, -30, 'South'), (-30, 30, 'Equatorial'), (30, 90, 'North')]:
    m = (spirals['dec'] >= dec_lo) & (spirals['dec'] < dec_hi)
    if m.sum() > 1000:
        cw_q = (spirals.loc[m, 'class'] == 'CW').mean()
        print(f"  DEC [{dec_lo:>+3d},{dec_hi:>+3d}): n={m.sum():>8,} CW={cw_q:.4f}")

# Save
results = {
    'catalog_a_raw': {
        'n_spirals': n_spirals, 'cw_frac': float(cw_frac),
        'monopole': float(mono), 'dipole_amp': float(amp),
        'l': float(l_deg), 'b': float(b_deg),
        'sigma': float(sigma), 'p_value': float(pval),
        'n_pixels': int(n_pix),
    },
    'catalog_b_calibrated': {
        'n_spirals': n_spirals, 'cw_frac': float(cal_cw_frac),
        'monopole': float(mono_cal), 'dipole_amp': float(amp_cal),
        'l': float(l_cal), 'b': float(b_cal),
        'sigma': float(sigma_cal), 'p_value': float(pval_cal),
    },
}
with open(f"{WORK}/dipole_results_8M.json", 'w') as f:
    json.dump(results, f, indent=2)

print("\n" + "=" * 60)
print("DIPOLE SUMMARY (8.47M galaxies)")
print("=" * 60)
print(f"  Cat A (raw):        {sigma:.2f}σ, amp={amp:.5f}, (l,b)=({l_deg:.1f},{b_deg:.1f})")
print(f"  Cat B (calibrated): {sigma_cal:.2f}σ, amp={amp_cal:.5f}, (l,b)=({l_cal:.1f},{b_cal:.1f})")
if max(sigma, sigma_cal) > 3:
    print("  *** SIGNIFICANT DIPOLE DETECTED ***")
elif max(sigma, sigma_cal) > 2:
    print("  ** Marginal signal — needs Catalog C confirmation **")
else:
    print("  No significant dipole at current sensitivity")
print("=" * 60)
print(f"\nSaved: {WORK}/dipole_results_8M.json")
