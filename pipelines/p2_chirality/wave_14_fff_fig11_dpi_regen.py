"""
R42 Wave 14-FFF: m6 P4 Fig 11 DPI Regen
Regenerate fig_raw_vs_eq.png at 300 DPI (publication quality).

Fig 11 (fig_raw_vs_eq.png) shows raw CW fraction vs equivariant TTA CW fraction
across the sky footprint. The current version was generated at lower DPI.
This script regenerates it at 300 DPI for arXiv submission.
"""
import json
import os
import time
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import healpy as hp

t0 = time.time()
print("=== m6 Fig 11 DPI Regen (Wave 14-FFF) ===")

# Load catalog
print("Loading chirality catalog...")
cat = pd.read_parquet('/workspace/r42_b20/chirality_catalog/catalog_production.parquet',
                      columns=['dr8_id', 'ra', 'dec', 'p_cw_raw_x', 'p_ccw_raw_x',
                               'p_ns_raw_x', 'class_raw_x', 'class_eq', 'confidence_eq',
                               'p_cw_eq', 'p_ccw_eq', 'p_ns_eq'])
print(f"  Rows: {len(cat):,}")

# Build HEALPix CW fraction maps: raw vs equivariant
NSIDE = 64
NPIX = hp.nside2npix(NSIDE)

# Raw classification
cat['pix'] = hp.ang2pix(NSIDE, np.radians(90 - cat['dec']), np.radians(cat['ra']))
is_spiral_raw = cat['class_raw_x'].isin(['CW', 'CCW'])
is_spiral_eq = cat['class_eq'].isin(['CW', 'CCW'])

# Raw CW fraction map
cw_raw = np.full(NPIX, np.nan)
for pix, grp in cat[is_spiral_raw].groupby('pix'):
    n_cw = (grp['class_raw_x'] == 'CW').sum()
    n_total = len(grp)
    if n_total >= 5:
        cw_raw[pix] = n_cw / n_total

# Equivariant CW fraction map
cw_eq = np.full(NPIX, np.nan)
for pix, grp in cat[is_spiral_eq].groupby('pix'):
    n_cw = (grp['class_eq'] == 'CW').sum()
    n_total = len(grp)
    if n_total >= 5:
        cw_eq[pix] = n_cw / n_total

print(f"  Raw map: {np.sum(~np.isnan(cw_raw)):,} valid pixels")
print(f"  Equivariant map: {np.sum(~np.isnan(cw_eq)):,} valid pixels")
print(f"  Raw CW mean: {np.nanmean(cw_raw):.4f}")
print(f"  Equivariant CW mean: {np.nanmean(cw_eq):.4f}")

# Replace NaN with UNSEEN for healpy
cw_raw_hp = cw_raw.copy()
cw_raw_hp[np.isnan(cw_raw_hp)] = hp.UNSEEN
cw_eq_hp = cw_eq.copy()
cw_eq_hp[np.isnan(cw_eq_hp)] = hp.UNSEEN

# Generate Fig 11: 2-panel figure, raw vs equivariant CW fraction maps
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Use healpy mollview but via matplotlib
from matplotlib.colors import Normalize

def healpix_to_image(m, nside, cmap='RdBu_r', vmin=0.47, vmax=0.53):
    """Convert HEALPix map to 2D image for matplotlib"""
    # Use orthographic projection at theta/phi grid
    theta = np.linspace(0, np.pi, 300)
    phi = np.linspace(0, 2*np.pi, 600)
    PHI, THETA = np.meshgrid(phi, theta)
    pix = hp.ang2pix(nside, THETA, PHI)
    img = m[pix]
    img[img == hp.UNSEEN] = np.nan
    return img, PHI * 180 / np.pi - 180, 90 - THETA * 180 / np.pi

img_raw, lon, lat = healpix_to_image(cw_raw_hp, NSIDE)
img_eq, _, _ = healpix_to_image(cw_eq_hp, NSIDE)

norm = Normalize(vmin=0.47, vmax=0.53)
cmap = plt.cm.RdBu_r

for ax, img, title in [(axes[0], img_raw, 'Raw ViT-Small\n(Catalog A)'),
                        (axes[1], img_eq, 'Equivariant TTA\n(Catalog C)')]:
    im = ax.imshow(img, extent=[-180, 180, -90, 90], origin='lower',
                   cmap=cmap, norm=norm, aspect='auto', interpolation='nearest')
    ax.set_xlabel('RA (deg)', fontsize=11)
    ax.set_ylabel('Dec (deg)', fontsize=11)
    ax.set_title(title, fontsize=12, fontweight='bold')
    ax.set_xlim(-180, 180)
    ax.set_ylim(-90, 90)
    ax.tick_params(labelsize=9)

# Shared colorbar
cbar = fig.colorbar(im, ax=axes, orientation='vertical', fraction=0.02, pad=0.04)
cbar.set_label('CW fraction', fontsize=11)
cbar.ax.tick_params(labelsize=9)

fig.suptitle('Fig. 11: Raw vs Equivariant CW Fraction Sky Maps (NSIDE=64)',
             fontsize=13, y=1.02)

outpath = '/workspace/r42_results/fig_raw_vs_eq_300dpi.png'
plt.tight_layout()
plt.savefig(outpath, dpi=300, bbox_inches='tight', facecolor='white')
plt.close()

sz = os.path.getsize(outpath)
wall = time.time() - t0
print(f"  Saved: {outpath} ({sz/1e3:.1f} KB)")
print(f"Wall time: {wall:.1f}s")
print("=== m6 Fig 11 DPI Regen DONE ===")
