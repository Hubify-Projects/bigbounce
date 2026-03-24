#!/usr/bin/env python3
"""Preliminary dipole analysis on the first shard (319K galaxies)."""
import pandas as pd
import numpy as np
import healpy as hp
import json

df = pd.read_parquet("/workspace/analysis3_outputs/chirality_catalog_v2_full.parquet")
print(f"Catalog: {len(df):,} galaxies")

n_cw = (df['class'] == 'CW').sum()
n_ccw = (df['class'] == 'CCW').sum()
n_ns = (df['class'] == 'NOT_SPIRAL').sum()
print(f"CW: {n_cw:,}  CCW: {n_ccw:,}  NS: {n_ns:,}")

spirals = df[(df['class'].isin(['CW','CCW'])) & (df['confidence'] > 0.7)]
print(f"High-conf spirals: {len(spirals):,}")
cw_frac = (spirals['class'] == 'CW').mean()
print(f"CW frac (raw): {cw_frac:.4f}")

NSIDE = 32
npix = hp.nside2npix(NSIDE)
cw_map = np.zeros(npix)
ccw_map = np.zeros(npix)

theta = np.radians(90 - spirals['dec'].values)
phi = np.radians(spirals['ra'].values % 360)
pix = hp.ang2pix(NSIDE, theta, phi)
for p, c in zip(pix, spirals['class'].values):
    if c == 'CW':
        cw_map[p] += 1
    else:
        ccw_map[p] += 1

tot = cw_map + ccw_map
mask = tot > 3
asym = np.full(npix, hp.UNSEEN)
asym[mask] = (cw_map[mask] - ccw_map[mask]) / tot[mask]

print(f"\nPixels used: {mask.sum()}/{npix}")

# Dipole via alm
alm = hp.map2alm(asym, lmax=1)
mono = alm[0].real / np.sqrt(4 * np.pi)
d0 = alm[1].real
d1r = alm[2].real
d1i = alm[2].imag
dip_amp = np.sqrt(d0**2 + 2*d1r**2 + 2*d1i**2) / np.sqrt(4*np.pi/3)

print(f"Monopole: {mono:.4f}")
print(f"Dipole amplitude: {dip_amp:.4f}")

# Bootstrap
n_boot = 5000
boot_amps = []
for i in range(n_boot):
    s = asym.copy()
    v = s[s != hp.UNSEEN]
    np.random.shuffle(v)
    s[s != hp.UNSEEN] = v
    a = hp.map2alm(s, lmax=1)
    ba = np.sqrt(a[1].real**2 + 2*a[2].real**2 + 2*a[2].imag**2) / np.sqrt(4*np.pi/3)
    boot_amps.append(ba)

boot_amps = np.array(boot_amps)
sigma = (dip_amp - np.mean(boot_amps)) / np.std(boot_amps)
pval = np.mean(boot_amps >= dip_amp)

print(f"\nBootstrap: {sigma:.2f}σ (p={pval:.4f})")
print(f"\n{'='*60}")
print(f"PRELIMINARY DIPOLE (319K galaxies, raw v2, NOT equivariant)")
print(f"{'='*60}")
print(f"Monopole:  {mono:.4f}")
print(f"Dipole:    {dip_amp:.4f} ({sigma:.1f}σ)")

if sigma > 3:
    print("STRONG SIGNAL — needs confirmation with full catalog + equivariance")
elif sigma > 2:
    print("INTERESTING — possible signal, needs full catalog + equivariance")
elif sigma > 1:
    print("MARGINAL — inconclusive at this sample size")
else:
    print("NO SIGNIFICANT DIPOLE detected at this sample size")

results = {
    'n_galaxies': len(df),
    'n_spirals_highconf': len(spirals),
    'cw_frac_raw': float(cw_frac),
    'monopole': float(mono),
    'dipole_amplitude': float(dip_amp),
    'sigma': float(sigma),
    'p_value': float(pval),
    'nside': NSIDE,
    'n_bootstrap': n_boot,
    'caveat': 'Preliminary — 1 shard only, raw model (not equivariant), partial sky coverage'
}
with open("/workspace/analysis3_outputs/preliminary_dipole.json", 'w') as f:
    json.dump(results, f, indent=2)
print(f"\nSaved: preliminary_dipole.json")
