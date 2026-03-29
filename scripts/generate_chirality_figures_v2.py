#!/usr/bin/env python3
"""
Generate 8 publication-quality chirality catalog figures (v2).
Runs on H200 pod with access to catalog_production.parquet.

Outputs 8 PNG figures at 300 DPI to /workspace/chirality/figures_v2/

Houston Golden — Big Bounce research program, March 2026.
"""

import os
import time
import io
import json
import warnings
import urllib.request
import urllib.error

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib import gridspec
from PIL import Image

warnings.filterwarnings('ignore')

# ── Style setup ──────────────────────────────────────────────────────────────
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Times New Roman', 'serif'],
    'font.size': 10,
    'axes.titlesize': 13,
    'axes.labelsize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'savefig.facecolor': 'white',
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.grid': False,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

# Color palette
CW_COLOR = '#2563eb'
CCW_COLOR = '#dc2626'
NS_COLOR = '#6b7280'

OUTDIR = '/workspace/chirality/figures_v2'
os.makedirs(OUTDIR, exist_ok=True)

# ── Load catalog ─────────────────────────────────────────────────────────────
print("Loading catalog...")
df = pd.read_parquet('/workspace/chirality/catalog_production.parquet')
print(f"  Loaded {len(df):,} galaxies")

spirals = df[df['class_eq'].isin(['CW', 'CCW'])].copy()
print(f"  {len(spirals):,} spirals (eq)")


def download_cutout(ra, dec, size=256):
    """Download a Legacy Survey JPEG cutout. Returns PIL Image or None."""
    url = (f"https://www.legacysurvey.org/viewer/jpeg-cutout"
           f"?ra={ra}&dec={dec}&size={size}&layer=ls-dr9")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = resp.read()
        img = Image.open(io.BytesIO(data)).convert('RGB')
        return img
    except Exception as e:
        print(f"    Download failed for ra={ra:.4f}, dec={dec:.4f}: {e}")
        return None


def download_gallery(subset, n=16, label=""):
    """Download n cutout images from subset DataFrame. Returns list of (img, row)."""
    results = []
    tried = 0
    for _, row in subset.iterrows():
        if len(results) >= n:
            break
        tried += 1
        if tried > n * 4:
            break
        print(f"    [{label}] Downloading {len(results)+1}/{n}: "
              f"dr8_id={row['dr8_id']}")
        img = download_cutout(row['ra'], row['dec'], size=256)
        if img is not None:
            results.append((img, row))
            time.sleep(0.5)
    return results


def add_border(img_arr, color_rgb, width=4):
    """Add a colored border to an image array in-place and return it."""
    out = img_arr.copy()
    out[:width, :] = color_rgb
    out[-width:, :] = color_rgb
    out[:, :width] = color_rgb
    out[:, -width:] = color_rgb
    return out


# ══════════════════════════════════════════════════════════════════════════════
# FIGURE 1: Gallery of High-Confidence CW Spirals (4x4)
# ══════════════════════════════════════════════════════════════════════════════
print("\n[1/8] fig_gallery_cw.png")
cw_high = (df[(df['class_eq'] == 'CW') & (df['confidence_eq'] > 0.95)]
           .sort_values('confidence_eq', ascending=False)
           .head(200)
           .sample(n=48, random_state=42))

cw_gallery = download_gallery(cw_high, n=16, label="CW")

if len(cw_gallery) >= 16:
    fig, axes = plt.subplots(4, 4, figsize=(10, 10.8))
    fig.subplots_adjust(hspace=0.32, wspace=0.08)
    fig.suptitle("High-Confidence Clockwise Spirals",
                 fontsize=16, fontweight='bold', y=0.98)
    for ax, (img, row) in zip(axes.flat, cw_gallery[:16]):
        img_arr = add_border(np.array(img), [37, 99, 235], width=5)
        ax.imshow(img_arr)
        ax.set_title(f"{row['dr8_id']}\nconf = {row['confidence_eq']:.3f}",
                     fontsize=7, pad=2)
        ax.axis('off')
    fig.savefig(f'{OUTDIR}/fig_gallery_cw.png', dpi=300)
    plt.close(fig)
    print("  Saved fig_gallery_cw.png")
else:
    print(f"  Only got {len(cw_gallery)} images, skipping")


# ══════════════════════════════════════════════════════════════════════════════
# FIGURE 2: Gallery of High-Confidence CCW Spirals (4x4)
# ══════════════════════════════════════════════════════════════════════════════
print("\n[2/8] fig_gallery_ccw.png")
ccw_high = (df[(df['class_eq'] == 'CCW') & (df['confidence_eq'] > 0.95)]
            .sort_values('confidence_eq', ascending=False)
            .head(200)
            .sample(n=48, random_state=43))

ccw_gallery = download_gallery(ccw_high, n=16, label="CCW")

if len(ccw_gallery) >= 16:
    fig, axes = plt.subplots(4, 4, figsize=(10, 10.8))
    fig.subplots_adjust(hspace=0.32, wspace=0.08)
    fig.suptitle("High-Confidence Counter-Clockwise Spirals",
                 fontsize=16, fontweight='bold', y=0.98)
    for ax, (img, row) in zip(axes.flat, ccw_gallery[:16]):
        img_arr = add_border(np.array(img), [220, 38, 38], width=5)
        ax.imshow(img_arr)
        ax.set_title(f"{row['dr8_id']}\nconf = {row['confidence_eq']:.3f}",
                     fontsize=7, pad=2)
        ax.axis('off')
    fig.savefig(f'{OUTDIR}/fig_gallery_ccw.png', dpi=300)
    plt.close(fig)
    print("  Saved fig_gallery_ccw.png")
else:
    print(f"  Only got {len(ccw_gallery)} images, skipping")


# ══════════════════════════════════════════════════════════════════════════════
# FIGURE 3: Gallery of NOT_SPIRAL galaxies (4x4)
# ══════════════════════════════════════════════════════════════════════════════
print("\n[3/8] fig_gallery_notspi.png")
ns_high = (df[(df['class_eq'] == 'NOT_SPIRAL') & (df['confidence_eq'] > 0.98)]
           .sample(n=48, random_state=44))

ns_gallery = download_gallery(ns_high, n=16, label="NS")

if len(ns_gallery) >= 16:
    fig, axes = plt.subplots(4, 4, figsize=(10, 10.8))
    fig.subplots_adjust(hspace=0.32, wspace=0.08)
    fig.suptitle("NOT_SPIRAL Classifications (Ellipticals, Mergers, Edge-on)",
                 fontsize=15, fontweight='bold', y=0.98)
    for ax, (img, row) in zip(axes.flat, ns_gallery[:16]):
        img_arr = add_border(np.array(img), [107, 114, 128], width=5)
        ax.imshow(img_arr)
        ax.set_title(f"{row['dr8_id']}\nconf = {row['confidence_eq']:.3f}",
                     fontsize=7, pad=2)
        ax.axis('off')
    fig.savefig(f'{OUTDIR}/fig_gallery_notspi.png', dpi=300)
    plt.close(fig)
    print("  Saved fig_gallery_notspi.png")
else:
    print(f"  Only got {len(ns_gallery)} images, skipping")


# ══════════════════════════════════════════════════════════════════════════════
# FIGURE 4: Raw vs Equivariant Asymmetry Mollweide — THE KEY FIGURE
# ══════════════════════════════════════════════════════════════════════════════
print("\n[4/8] fig_raw_vs_eq.png — Raw vs Equivariant asymmetry")

N_RA, N_DEC = 72, 36

def compute_asymmetry_grid(ra_vals, dec_vals, class_vals, n_ra=72, n_dec=36,
                           min_count=20):
    """Compute CW fraction excess on a RA/DEC grid."""
    ra_bins = np.linspace(0, 360, n_ra + 1)
    dec_bins = np.linspace(-90, 90, n_dec + 1)

    mask_spiral = np.isin(class_vals, ['CW', 'CCW'])
    ra_s = ra_vals[mask_spiral]
    dec_s = dec_vals[mask_spiral]
    cls_s = class_vals[mask_spiral]

    ri = np.clip(np.digitize(ra_s, ra_bins) - 1, 0, n_ra - 1)
    di = np.clip(np.digitize(dec_s, dec_bins) - 1, 0, n_dec - 1)

    n_total = np.zeros(n_dec * n_ra)
    n_cw = np.zeros(n_dec * n_ra)

    is_cw = cls_s == 'CW'
    # Use np.add.at for fast binning
    flat_idx = di * n_ra + ri
    np.add.at(n_total, flat_idx, 1)
    np.add.at(n_cw, flat_idx[is_cw], 1)
    n_total = n_total.reshape(n_dec, n_ra)
    n_cw = n_cw.reshape(n_dec, n_ra)

    asym = np.full((n_dec, n_ra), np.nan)
    ok = n_total >= min_count
    asym[ok] = n_cw[ok] / n_total[ok] - 0.5

    ra_centers = 0.5 * (ra_bins[:-1] + ra_bins[1:])
    dec_centers = 0.5 * (dec_bins[:-1] + dec_bins[1:])
    return ra_centers, dec_centers, asym, n_total


print("  Computing raw asymmetry (class_raw_y)...")
ra_c, dec_c, asym_raw, cnt_raw = compute_asymmetry_grid(
    df['ra'].values, df['dec'].values, df['class_raw_y'].values,
    n_ra=N_RA, n_dec=N_DEC
)

print("  Computing equivariant asymmetry (class_eq)...")
_, _, asym_eq, cnt_eq = compute_asymmetry_grid(
    df['ra'].values, df['dec'].values, df['class_eq'].values,
    n_ra=N_RA, n_dec=N_DEC
)

# Mollweide grid
lon = np.deg2rad(ra_c - 180)
lat = np.deg2rad(dec_c)
LON, LAT = np.meshgrid(lon, lat)

# Common color scale
vmax_raw = np.nanmax(np.abs(asym_raw))
vmax_eq = np.nanmax(np.abs(asym_eq))
vmax_common = max(vmax_raw, 0.05)

cmap = plt.cm.RdBu_r

fig, (ax1, ax2) = plt.subplots(
    1, 2, figsize=(16, 5.5),
    subplot_kw={'projection': 'mollweide'}
)
fig.subplots_adjust(wspace=0.08, top=0.85, bottom=0.18)

# Raw
im1 = ax1.pcolormesh(LON, LAT, asym_raw, cmap=cmap,
                      vmin=-vmax_common, vmax=vmax_common,
                      shading='auto', rasterized=True)
ax1.set_title("Raw Classifier (Catalog A)\n94.6$\\sigma$ Survey Systematic",
              fontsize=13, fontweight='bold', pad=12)
ax1.grid(True, alpha=0.3, linewidth=0.5)

# Equivariant
im2 = ax2.pcolormesh(LON, LAT, asym_eq, cmap=cmap,
                      vmin=-vmax_common, vmax=vmax_common,
                      shading='auto', rasterized=True)
ax2.set_title("Equivariant Average (Catalog C)\nClean Null",
              fontsize=13, fontweight='bold', pad=12)
ax2.grid(True, alpha=0.3, linewidth=0.5)

# Shared colorbar
cbar_ax = fig.add_axes([0.25, 0.08, 0.50, 0.025])
cbar = fig.colorbar(im1, cax=cbar_ax, orientation='horizontal')
cbar.set_label('CW Fraction Excess  (CW/total $-$ 0.5)', fontsize=11)
cbar.ax.tick_params(labelsize=9)

fig.suptitle("Equivariant Averaging Eliminates the Survey Systematic",
             fontsize=16, fontweight='bold', y=0.97)

fig.savefig(f'{OUTDIR}/fig_raw_vs_eq.png', dpi=300)
plt.close(fig)
print("  Saved fig_raw_vs_eq.png")


# ══════════════════════════════════════════════════════════════════════════════
# FIGURE 5: Spiral Density Map (Mollweide)
# ══════════════════════════════════════════════════════════════════════════════
print("\n[5/8] fig_spiral_density.png — Spiral density Mollweide")

spiral_mask = df['class_eq'].isin(['CW', 'CCW'])
ra_s = df.loc[spiral_mask, 'ra'].values
dec_s = df.loc[spiral_mask, 'dec'].values

ra_bins_d = np.linspace(0, 360, N_RA + 1)
dec_bins_d = np.linspace(-90, 90, N_DEC + 1)

ri = np.clip(np.digitize(ra_s, ra_bins_d) - 1, 0, N_RA - 1)
di = np.clip(np.digitize(dec_s, dec_bins_d) - 1, 0, N_DEC - 1)

density = np.zeros(N_DEC * N_RA)
np.add.at(density, di * N_RA + ri, 1)
density = density.reshape(N_DEC, N_RA)

density_masked = np.ma.masked_where(density == 0, density)

fig, ax = plt.subplots(figsize=(10, 5.5),
                        subplot_kw={'projection': 'mollweide'})
fig.subplots_adjust(top=0.88, bottom=0.18)

im = ax.pcolormesh(LON, LAT, np.log10(density_masked + 1),
                    cmap='inferno', shading='auto', rasterized=True)
ax.grid(True, alpha=0.3, linewidth=0.5)
ax.set_title("Spiral Galaxy Density Map (Equivariant Catalog)\n"
             f"8.47M galaxies, {len(spirals):,.0f} spirals",
             fontsize=14, fontweight='bold', pad=12)

cbar_ax = fig.add_axes([0.25, 0.08, 0.50, 0.025])
cbar = fig.colorbar(im, cax=cbar_ax, orientation='horizontal')
cbar.set_label('log$_{10}$(N spirals per pixel + 1)', fontsize=11)
cbar.ax.tick_params(labelsize=9)

fig.savefig(f'{OUTDIR}/fig_spiral_density.png', dpi=300)
plt.close(fig)
print("  Saved fig_spiral_density.png")


# ══════════════════════════════════════════════════════════════════════════════
# FIGURE 6: CW Fraction Heatmap (RA vs DEC)
# ══════════════════════════════════════════════════════════════════════════════
print("\n[6/8] fig_cw_fraction_heatmap.png — CW fraction 2D heatmap")

BIN = 5  # degrees
ra_bins_h = np.arange(0, 360 + BIN, BIN)
dec_bins_h = np.arange(-70, 85 + BIN, BIN)
n_ra_h = len(ra_bins_h) - 1
n_dec_h = len(dec_bins_h) - 1

sp = df[df['class_eq'].isin(['CW', 'CCW'])].copy()
ra_sp = sp['ra'].values
dec_sp = sp['dec'].values
cls_sp = sp['class_eq'].values

ri_h = np.clip(np.digitize(ra_sp, ra_bins_h) - 1, 0, n_ra_h - 1)
di_h = np.clip(np.digitize(dec_sp, dec_bins_h) - 1, 0, n_dec_h - 1)

n_total_h = np.zeros(n_dec_h * n_ra_h)
n_cw_h = np.zeros(n_dec_h * n_ra_h)
flat_h = di_h * n_ra_h + ri_h
np.add.at(n_total_h, flat_h, 1)
np.add.at(n_cw_h, flat_h[cls_sp == 'CW'], 1)
n_total_h = n_total_h.reshape(n_dec_h, n_ra_h)
n_cw_h = n_cw_h.reshape(n_dec_h, n_ra_h)

cw_frac = np.full((n_dec_h, n_ra_h), np.nan)
ok = n_total_h >= 30
cw_frac[ok] = n_cw_h[ok] / n_total_h[ok]

fig, ax = plt.subplots(figsize=(14, 5))
fig.subplots_adjust(right=0.92)

im = ax.pcolormesh(ra_bins_h, dec_bins_h, cw_frac,
                    cmap='RdBu_r', vmin=0.45, vmax=0.55,
                    shading='flat', rasterized=True)

ax.set_xlabel('Right Ascension ($^\\circ$)', fontsize=12)
ax.set_ylabel('Declination ($^\\circ$)', fontsize=12)
ax.set_title('CW Fraction Across the Sky (Equivariant Catalog)\n'
             'Blue = CW excess, Red = CCW excess, '
             f'{BIN}$^\\circ$ $\\times$ {BIN}$^\\circ$ bins',
             fontsize=14, fontweight='bold')
ax.set_xlim(0, 360)
ax.set_ylim(-70, 85)
ax.set_aspect('auto')

cbar = fig.colorbar(im, ax=ax, orientation='vertical',
                     fraction=0.02, pad=0.02)
cbar.set_label('CW Fraction', fontsize=11)
cbar.ax.tick_params(labelsize=9)
cbar.ax.axhline(y=0.5, color='black', linewidth=1, linestyle='--')

fig.savefig(f'{OUTDIR}/fig_cw_fraction_heatmap.png', dpi=300)
plt.close(fig)
print("  Saved fig_cw_fraction_heatmap.png")


# ══════════════════════════════════════════════════════════════════════════════
# FIGURE 7: Classification Donut Chart
# ══════════════════════════════════════════════════════════════════════════════
print("\n[7/8] fig_class_pie.png — Donut chart")

counts = df['class_eq'].value_counts()
n_cw = counts.get('CW', 0)
n_ccw = counts.get('CCW', 0)
n_ns = counts.get('NOT_SPIRAL', 0)
total = n_cw + n_ccw + n_ns

labels = ['CW Spirals', 'CCW Spirals', 'Not Spiral']
sizes = [n_cw, n_ccw, n_ns]
colors = [CW_COLOR, CCW_COLOR, NS_COLOR]

fig, ax = plt.subplots(figsize=(7, 7))

wedges, texts, autotexts = ax.pie(
    sizes, labels=None, colors=colors,
    explode=(0.02, 0.02, 0.02),
    autopct=lambda pct: f'{pct:.1f}%\n({int(round(pct / 100 * total)):,})',
    pctdistance=0.72, startangle=90, counterclock=False,
    wedgeprops=dict(width=0.45, edgecolor='white', linewidth=2.5),
    textprops={'fontsize': 9, 'fontweight': 'bold'}
)

for t in autotexts:
    t.set_color('white')

ax.legend(wedges,
          [f'{l}: {s:,}' for l, s in zip(labels, sizes)],
          loc='lower center', fontsize=11, frameon=False,
          bbox_to_anchor=(0.5, -0.05))

ax.text(0, 0, f'{total:,}\ngalaxies', ha='center', va='center',
        fontsize=16, fontweight='bold', color='#1f2937')

ax.set_title('Equivariant Classification Breakdown\n'
             'Catalog C  |  8.47M Galaxies',
             fontsize=15, fontweight='bold', pad=15)

fig.savefig(f'{OUTDIR}/fig_class_pie.png', dpi=300)
plt.close(fig)
print("  Saved fig_class_pie.png")


# ══════════════════════════════════════════════════════════════════════════════
# FIGURE 8: Equivariance Demonstration
# ══════════════════════════════════════════════════════════════════════════════
print("\n[8/8] fig_equivariance_demo.png — Equivariant averaging demo")

# Pick 2 CW and 2 CCW galaxies where raw and eq agree, high confidence
demo_cw = (df[(df['class_eq'] == 'CW') &
              (df['class_raw_y'] == 'CW') &
              (df['confidence_eq'] > 0.90) &
              (df['confidence_raw'] > 0.90)]
           .head(200)
           .sample(6, random_state=55))

demo_ccw = (df[(df['class_eq'] == 'CCW') &
               (df['class_raw_y'] == 'CCW') &
               (df['confidence_eq'] > 0.90) &
               (df['confidence_raw'] > 0.90)]
            .head(200)
            .sample(6, random_state=56))

demo_galaxies = pd.concat([demo_cw.head(2), demo_ccw.head(2)])

demo_images = []
for _, row in demo_galaxies.iterrows():
    print(f"    Downloading demo galaxy {row['dr8_id']}...")
    img = download_cutout(row['ra'], row['dec'], size=256)
    if img is not None:
        demo_images.append((img, row))
        time.sleep(0.5)

if len(demo_images) >= 4:
    fig = plt.figure(figsize=(14, 12))
    gs = fig.add_gridspec(4, 4, hspace=0.4, wspace=0.3,
                          left=0.06, right=0.96, top=0.92, bottom=0.04)

    col_headers = ['Original Image', 'Horizontally Flipped',
                   'Raw Predictions', 'Equivariant Predictions']

    for row_idx, (img, row) in enumerate(demo_images[:4]):
        img_arr = np.array(img)
        img_flipped = np.fliplr(img_arr)

        clr = [37, 99, 235] if row['class_eq'] == 'CW' else [220, 38, 38]

        # Col 0: Original
        ax0 = fig.add_subplot(gs[row_idx, 0])
        ax0.imshow(add_border(img_arr, clr, width=4))
        ax0.set_ylabel(f"{row['dr8_id']}\n{row['class_eq']}",
                       fontsize=8, fontweight='bold')
        ax0.set_xticks([]); ax0.set_yticks([])
        if row_idx == 0:
            ax0.set_title(col_headers[0], fontsize=11, fontweight='bold',
                          pad=8)

        # Col 1: Flipped
        ax1 = fig.add_subplot(gs[row_idx, 1])
        ax1.imshow(add_border(img_flipped, clr, width=4))
        ax1.set_xticks([]); ax1.set_yticks([])
        if row_idx == 0:
            ax1.set_title(col_headers[1], fontsize=11, fontweight='bold',
                          pad=8)

        # Col 2: Raw predictions (horizontal bar)
        ax2 = fig.add_subplot(gs[row_idx, 2])
        raw_p = [row['p_cw_raw_y'], row['p_ccw_raw_y'], row['p_ns_raw_y']]
        bars2 = ax2.barh(['CW', 'CCW', 'NS'], raw_p,
                         color=[CW_COLOR, CCW_COLOR, NS_COLOR],
                         edgecolor='white', height=0.6)
        ax2.set_xlim(0, 1.05)
        for b, v in zip(bars2, raw_p):
            if v > 0.08:
                ax2.text(v - 0.03, b.get_y() + b.get_height() / 2,
                         f'{v:.3f}', ha='right', va='center',
                         fontsize=8, color='white', fontweight='bold')
            elif v > 0.001:
                ax2.text(v + 0.02, b.get_y() + b.get_height() / 2,
                         f'{v:.3f}', ha='left', va='center',
                         fontsize=7, color='#333')
        if row_idx == 0:
            ax2.set_title(col_headers[2], fontsize=11, fontweight='bold',
                          pad=8)
        ax2.tick_params(labelsize=8)

        # Col 3: Equivariant predictions
        ax3 = fig.add_subplot(gs[row_idx, 3])
        eq_p = [row['p_cw_eq'], row['p_ccw_eq'], row['p_ns_eq']]
        bars3 = ax3.barh(['CW', 'CCW', 'NS'], eq_p,
                         color=[CW_COLOR, CCW_COLOR, NS_COLOR],
                         edgecolor='white', height=0.6)
        ax3.set_xlim(0, 1.05)
        for b, v in zip(bars3, eq_p):
            if v > 0.08:
                ax3.text(v - 0.03, b.get_y() + b.get_height() / 2,
                         f'{v:.3f}', ha='right', va='center',
                         fontsize=8, color='white', fontweight='bold')
            elif v > 0.001:
                ax3.text(v + 0.02, b.get_y() + b.get_height() / 2,
                         f'{v:.3f}', ha='left', va='center',
                         fontsize=7, color='#333')
        if row_idx == 0:
            ax3.set_title(col_headers[3], fontsize=11, fontweight='bold',
                          pad=8)
        ax3.tick_params(labelsize=8)

    fig.suptitle("Equivariant Averaging: Original vs. Flipped Predictions",
                 fontsize=16, fontweight='bold')

    fig.savefig(f'{OUTDIR}/fig_equivariance_demo.png', dpi=300)
    plt.close(fig)
    print("  Saved fig_equivariance_demo.png")
else:
    print(f"  Only got {len(demo_images)} demo images, skipping")


# ══════════════════════════════════════════════════════════════════════════════
# Summary
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("ALL 8 FIGURES COMPLETE")
print(f"Output directory: {OUTDIR}")
for f in sorted(os.listdir(OUTDIR)):
    fpath = os.path.join(OUTDIR, f)
    size = os.path.getsize(fpath)
    print(f"  {f:40s} {size / 1024:.0f} KB")
print("=" * 60)
