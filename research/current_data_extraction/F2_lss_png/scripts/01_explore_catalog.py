#!/usr/bin/env python3.8
"""
Pipeline B Step 1: Explore the DESI EDR catalog structure.

Before building any model, understand:
- How many objects of each type (QSO, GALAXY, STAR)?
- What columns are available?
- What is the redshift distribution?
- What spectral data format is used?
- What quality flags exist?
"""
import numpy as np
from astropy.io import fits
import json, os

DATA = '/dev/shm/bigbounce/pipeline_B/data'
OUT = '/dev/shm/bigbounce/pipeline_B/outputs'
os.makedirs(OUT, exist_ok=True)

print('='*60)
print('PIPELINE B STEP 1: DESI EDR CATALOG EXPLORATION')
print('='*60)

f = DATA + '/desi_edr_zcatalog.fits'
if not os.path.exists(f):
    print('Catalog not yet downloaded. Waiting...')
    import time
    for i in range(60):
        if os.path.exists(f) and os.path.getsize(f) > 1e9:
            break
        time.sleep(10)
        print('.', end='', flush=True)
    print()

if not os.path.exists(f) or os.path.getsize(f) < 1e9:
    print('ERROR: Catalog not available or incomplete')
    exit(1)

print('Loading catalog...')
hdu = fits.open(f)
print('HDU list:', [h.name for h in hdu])

data = hdu[1].data
cols = hdu[1].columns
print(f'\nTotal objects: {len(data):,}')
print(f'Columns ({len(cols)}):')
for c in cols:
    print(f'  {c.name:30s} {c.format:10s} {str(c.unit or ):10s}')

# Object type distribution
if 'SPECTYPE' in [c.name for c in cols]:
    types, counts = np.unique(data['SPECTYPE'], return_counts=True)
    print('\nObject types:')
    for t, c in sorted(zip(types, counts), key=lambda x: -x[1]):
        print(f'  {t.strip():15s} {c:>10,} ({100*c/len(data):.1f}%)')

# Redshift distribution
if 'Z' in [c.name for c in cols]:
    z = data['Z']
    z_good = z[(z > 0) & (z < 10)]
    print(f'\nRedshift: median={np.median(z_good):.3f}, mean={np.mean(z_good):.3f}')
    print(f'  z < 0.5: {np.sum(z_good < 0.5):,}')
    print(f'  0.5 < z < 1.0: {np.sum((z_good >= 0.5) & (z_good < 1.0)):,}')
    print(f'  1.0 < z < 2.0: {np.sum((z_good >= 1.0) & (z_good < 2.0)):,}')
    print(f'  z > 2.0: {np.sum(z_good >= 2.0):,}')

# Quality flags
for flag_col in ['ZWARN', 'DELTACHI2']:
    if flag_col in [c.name for c in cols]:
        vals = data[flag_col]
        print(f'\n{flag_col}: min={np.min(vals)}, max={np.max(vals)}, median={np.median(vals):.1f}')
        if flag_col == 'ZWARN':
            print(f'  ZWARN=0 (good): {np.sum(vals == 0):,} ({100*np.sum(vals==0)/len(vals):.1f}%)')

# Save summary
summary = {
    'total_objects': int(len(data)),
    'columns': [c.name for c in cols],
    'n_columns': len(cols),
}
with open(OUT + '/step1_catalog_summary.json', 'w') as fp:
    json.dump(summary, fp, indent=2)
print(f'\nSaved: {OUT}/step1_catalog_summary.json')

hdu.close()
