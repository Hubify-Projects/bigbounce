#!/usr/bin/env python3
"""
Generate publication-quality chirality figures from catalog data.
Houston Golden — Big Bounce research program.

Expects:
  /workspace/chirality/catalog_production.parquet
  /workspace/chirality/deeper_analysis.json
  /workspace/chirality/dipole_catalog_c.json

Outputs 5 PNG figures to /workspace/chirality/figures/
"""

import json
import numpy as np
import pandas as pd
import healpy as hp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.patches import FancyBboxPatch
import matplotlib.ticker as mticker
import os

# ── Style setup ──────────────────────────────────────────────────────────
rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Times New Roman', 'Times'],
    'font.sans-serif': ['DejaVu Sans', 'Helvetica', 'Arial'],
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.facecolor': 'white',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': False,
    'axes.linewidth': 0.8,
    'xtick.major.width': 0.8,
    'ytick.major.width': 0.8,
    'lines.linewidth': 1.5,
    'text.usetex': False,
})

OUTDIR = '/workspace/chirality/figures'
os.makedirs(OUTDIR, exist_ok=True)

# ── Load data ────────────────────────────────────────────────────────────
print("Loading catalog...")
df = pd.read_parquet('/workspace/chirality/catalog_production.parquet')
print(f"  {len(df):,} total galaxies")

with open('/workspace/chirality/deeper_analysis.json') as f:
    analysis = json.load(f)

with open('/workspace/chirality/dipole_catalog_c.json') as f:
    dipole = json.load(f)

# ── Filter to equivariant spirals with confidence > 0.6 ─────────────────
spirals = df[
    (df['class_eq'].isin(['CW', 'CCW'])) & (df['confidence_eq'] > 0.6)
].copy()
print(f"  {len(spirals):,} spirals (equivariant, conf > 0.6)")

n_cw = (spirals['class_eq'] == 'CW').sum()
n_ccw = (spirals['class_eq'] == 'CCW').sum()
print(f"  CW: {n_cw:,}, CCW: {n_ccw:,}")

# Also load all equivariant spirals (no confidence cut) for some plots
all_spirals = df[df['class_eq'].isin(['CW', 'CCW'])].copy()
print(f"  {len(all_spirals):,} spirals (equivariant, all conf)")


# ═══════════════════════════════════════════════════════════════════════════
# FIGURE 1: Mollweide sky map of CW-CCW asymmetry
# ═══════════════════════════════════════════════════════════════════════════
print("\n[1/5] Generating sky map...")

NSIDE = 32
NPIX = hp.nside2npix(NSIDE)

# Convert RA/DEC to healpix pixels
theta = np.radians(90.0 - spirals['dec'].values)
phi = np.radians(spirals['ra'].values)
pixels = hp.ang2pix(NSIDE, theta, phi)

# Count CW and CCW per pixel
cw_map = np.zeros(NPIX)
ccw_map = np.zeros(NPIX)

cw_mask = spirals['class_eq'].values == 'CW'
for pix in pixels[cw_mask]:
    cw_map[pix] += 1
for pix in pixels[~cw_mask]:
    ccw_map[pix] += 1

total_map = cw_map + ccw_map
# Asymmetry: (CW - CCW) / (CW + CCW), masked where no data
asymmetry = np.full(NPIX, hp.UNSEEN)
occupied = total_map > 10  # require at least 10 galaxies per pixel
asymmetry[occupied] = (cw_map[occupied] - ccw_map[occupied]) / total_map[occupied]

fig = plt.figure(figsize=(10, 5.5))
hp.mollview(
    asymmetry,
    fig=fig.number,
    title="Galaxy Chirality Asymmetry Map (8.47M galaxies, equivariant)",
    unit=r"$(N_{\rm CW} - N_{\rm CCW}) / (N_{\rm CW} + N_{\rm CCW})$",
    cmap='RdBu_r',  # red = CCW excess (positive after flip), blue = CW excess
    min=-0.08,
    max=0.08,
    coord=['C'],
    xsize=1600,
)
hp.graticule(dpar=30, dmer=30, alpha=0.3)
fig.savefig(f'{OUTDIR}/fig_sky_map.png', dpi=300, facecolor='white',
            bbox_inches='tight', pad_inches=0.1)
plt.close(fig)
print("  Saved fig_sky_map.png")


# ═══════════════════════════════════════════════════════════════════════════
# FIGURE 2: Angular power spectrum (multipole bar chart)
# ═══════════════════════════════════════════════════════════════════════════
print("\n[2/5] Generating multipole spectrum...")

mp = analysis['analyses']['1_multipoles']
ells = []
Cl_data = []
Cl_null = []
Cl_err = []
sigmas = []

for l in range(1, 6):
    key = f'l={l}'
    d = mp[key]
    ells.append(l)
    Cl_data.append(d['C_l_data'])
    Cl_null.append(d['C_l_null_mean'])
    Cl_err.append(d['C_l_null_std'])
    sigmas.append(d['sigma'])

ells = np.array(ells)
Cl_data = np.array(Cl_data)
Cl_null = np.array(Cl_null)
Cl_err = np.array(Cl_err)
sigmas = np.array(sigmas)

fig, ax = plt.subplots(figsize=(7, 4.5))

bar_width = 0.35
x = np.arange(len(ells))

# Null expectation bars
bars_null = ax.bar(x - bar_width/2, Cl_null * 1e6, bar_width,
                   yerr=Cl_err * 1e6, capsize=4, color='#D4D4D4',
                   edgecolor='#888888', linewidth=0.6,
                   label='Null expectation (1000 shuffles)', zorder=2)

# Data bars - highlight l=1 and l=5
colors = []
for i, l in enumerate(ells):
    if l == 1:
        colors.append('#2166AC')  # blue for dipole
    elif l == 5:
        colors.append('#B2182B')  # red for l=5
    else:
        colors.append('#6BAED6')  # lighter blue for others

bars_data = ax.bar(x + bar_width/2, Cl_data * 1e6, bar_width,
                   color=colors, edgecolor='#333333', linewidth=0.6,
                   label='Measured', zorder=2)

# Annotate significance
for i, (l, sig) in enumerate(zip(ells, sigmas)):
    if abs(sig) > 2.0:
        ax.annotate(f'{sig:.1f}$\\sigma$',
                    xy=(x[i] + bar_width/2, Cl_data[i] * 1e6),
                    xytext=(0, 8), textcoords='offset points',
                    ha='center', va='bottom', fontsize=9, fontweight='bold',
                    color='#B2182B' if l == 5 else '#2166AC')

ax.set_xlabel('Multipole $\\ell$')
ax.set_ylabel('$C_\\ell$ ($\\times 10^{-6}$)')
ax.set_title('Angular Power Spectrum of Chirality Asymmetry')
ax.set_xticks(x)
ax.set_xticklabels([f'$\\ell={l}$' for l in ells])
ax.legend(frameon=False, loc='upper right')
ax.set_ylim(bottom=0)

fig.tight_layout()
fig.savefig(f'{OUTDIR}/fig_multipoles.png', dpi=300, facecolor='white')
plt.close(fig)
print("  Saved fig_multipoles.png")


# ═══════════════════════════════════════════════════════════════════════════
# FIGURE 3: CW fraction by sky region (RA quadrants + DEC bands)
# ═══════════════════════════════════════════════════════════════════════════
print("\n[3/5] Generating sky regions comparison...")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))

# -- RA quadrants --
ra_bins = [(0, 90), (90, 180), (180, 270), (270, 360)]
ra_labels = ['0-90', '90-180', '180-270', '270-360']

def cw_frac_and_err(subset):
    n = len(subset)
    if n == 0:
        return 0.5, 0
    f = (subset['class_eq'] == 'CW').sum() / n
    se = np.sqrt(f * (1-f) / n)
    return f, se

# Catalog A (raw)
raw_spirals = df[
    (df['class_raw_x'].isin(['CW', 'CCW'])) & (df['confidence_raw'] > 0.6)
].copy()

frac_eq_ra, err_eq_ra = [], []
frac_raw_ra, err_raw_ra = [], []
for lo, hi in ra_bins:
    sub_eq = spirals[(spirals['ra'] >= lo) & (spirals['ra'] < hi)]
    f, e = cw_frac_and_err(sub_eq)
    frac_eq_ra.append(f)
    err_eq_ra.append(e)

    sub_raw = raw_spirals[(raw_spirals['ra'] >= lo) & (raw_spirals['ra'] < hi)]
    if len(sub_raw) > 0:
        f_raw = (sub_raw['class_raw_x'] == 'CW').sum() / len(sub_raw)
        e_raw = np.sqrt(f_raw * (1-f_raw) / len(sub_raw))
    else:
        f_raw, e_raw = 0.5, 0
    frac_raw_ra.append(f_raw)
    err_raw_ra.append(e_raw)

x_ra = np.arange(len(ra_labels))
w = 0.32
ax1.bar(x_ra - w/2, frac_raw_ra, w, yerr=err_raw_ra, capsize=3,
        color='#FDAE61', edgecolor='#333', linewidth=0.5, label='Raw (Catalog A)')
ax1.bar(x_ra + w/2, frac_eq_ra, w, yerr=err_eq_ra, capsize=3,
        color='#2166AC', edgecolor='#333', linewidth=0.5, label='Equivariant (Catalog C)')
ax1.axhline(0.5, color='#999', linestyle='--', linewidth=0.8, zorder=0)
ax1.set_xlabel('Right Ascension quadrant (deg)')
ax1.set_ylabel('CW fraction')
ax1.set_title('CW Fraction by RA Quadrant')
ax1.set_xticks(x_ra)
ax1.set_xticklabels(ra_labels)
ax1.legend(frameon=False, fontsize=9)
ax1.set_ylim(0.488, 0.508)

# -- DEC bands --
dec_bins = [(-90, -20), (-20, 20), (20, 90)]
dec_labels = ['South\n($-90$ to $-20$)', 'Equatorial\n($-20$ to $+20$)', 'North\n($+20$ to $+90$)']

frac_eq_dec, err_eq_dec = [], []
frac_raw_dec, err_raw_dec = [], []
for lo, hi in dec_bins:
    sub_eq = spirals[(spirals['dec'] >= lo) & (spirals['dec'] < hi)]
    f, e = cw_frac_and_err(sub_eq)
    frac_eq_dec.append(f)
    err_eq_dec.append(e)

    sub_raw = raw_spirals[(raw_spirals['dec'] >= lo) & (raw_spirals['dec'] < hi)]
    if len(sub_raw) > 0:
        f_raw = (sub_raw['class_raw_x'] == 'CW').sum() / len(sub_raw)
        e_raw = np.sqrt(f_raw * (1-f_raw) / len(sub_raw))
    else:
        f_raw, e_raw = 0.5, 0
    frac_raw_dec.append(f_raw)
    err_raw_dec.append(e_raw)

x_dec = np.arange(len(dec_labels))
ax2.bar(x_dec - w/2, frac_raw_dec, w, yerr=err_raw_dec, capsize=3,
        color='#FDAE61', edgecolor='#333', linewidth=0.5, label='Raw (Catalog A)')
ax2.bar(x_dec + w/2, frac_eq_dec, w, yerr=err_eq_dec, capsize=3,
        color='#2166AC', edgecolor='#333', linewidth=0.5, label='Equivariant (Catalog C)')
ax2.axhline(0.5, color='#999', linestyle='--', linewidth=0.8, zorder=0)
ax2.set_xlabel('Declination band (deg)')
ax2.set_ylabel('CW fraction')
ax2.set_title('CW Fraction by DEC Band')
ax2.set_xticks(x_dec)
ax2.set_xticklabels(dec_labels, fontsize=9)
ax2.legend(frameon=False, fontsize=9)
ax2.set_ylim(0.488, 0.508)

fig.tight_layout()
fig.savefig(f'{OUTDIR}/fig_sky_regions.png', dpi=300, facecolor='white')
plt.close(fig)
print("  Saved fig_sky_regions.png")


# ═══════════════════════════════════════════════════════════════════════════
# FIGURE 4: Confidence distribution + class balance
# ═══════════════════════════════════════════════════════════════════════════
print("\n[4/5] Generating confidence distribution...")

fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(11, 4.5),
                                         gridspec_kw={'width_ratios': [1, 1.15]})

bins = np.linspace(0.33, 1.0, 50)

# Filter by class
cw_all = df[df['class_eq'] == 'CW']['confidence_eq'].values
ccw_all = df[df['class_eq'] == 'CCW']['confidence_eq'].values
ns_all = df[df['class_eq'] == 'NOT_SPIRAL']['confidence_eq'].values

# -- Left panel: all three classes (log scale) --
ax_left.hist(ns_all, bins=bins, alpha=0.5, color='#AAAAAA',
             label=f'Not spiral ({len(ns_all):,.0f})', zorder=1)
ax_left.hist(cw_all, bins=bins, alpha=0.7, color='#2166AC',
             label=f'CW ({len(cw_all):,.0f})', zorder=2)
ax_left.hist(ccw_all, bins=bins, alpha=0.7, color='#B2182B',
             label=f'CCW ({len(ccw_all):,.0f})', zorder=3)
ax_left.set_yscale('log')
ax_left.set_xlabel('Equivariant confidence')
ax_left.set_ylabel('Galaxy count')
ax_left.set_title('All Classifications (log scale)')
ax_left.legend(frameon=False, fontsize=9, loc='upper left')

# -- Right panel: spirals only (linear) with CW fraction inset --
ax_right.hist(cw_all, bins=bins, alpha=0.7, color='#2166AC',
              label=f'CW ({len(cw_all):,.0f})', zorder=2)
ax_right.hist(ccw_all, bins=bins, alpha=0.7, color='#B2182B',
              label=f'CCW ({len(ccw_all):,.0f})', zorder=3)
ax_right.set_xlabel('Equivariant confidence')
ax_right.set_ylabel('Galaxy count')
ax_right.set_title('Spiral Galaxies Only')
ax_right.legend(frameon=False, fontsize=9, loc='upper left')

# Inset: CW fraction vs confidence
ax_in = ax_right.inset_axes([0.45, 0.42, 0.50, 0.42])
conf_bins = np.linspace(0.33, 1.0, 15)
cw_fracs = []
cw_errs = []
conf_mids = []
for i in range(len(conf_bins)-1):
    lo, hi = conf_bins[i], conf_bins[i+1]
    sub = all_spirals[(all_spirals['confidence_eq'] >= lo) & (all_spirals['confidence_eq'] < hi)]
    if len(sub) > 50:
        f = (sub['class_eq'] == 'CW').sum() / len(sub)
        e = np.sqrt(f * (1-f) / len(sub))
        cw_fracs.append(f)
        cw_errs.append(e)
        conf_mids.append(0.5*(lo+hi))

ax_in.errorbar(conf_mids, cw_fracs, yerr=cw_errs, fmt='o-', color='#2166AC',
               markersize=3, linewidth=1, capsize=2)
ax_in.axhline(0.5, color='#999', linestyle='--', linewidth=0.7)
ax_in.set_xlabel('Confidence', fontsize=8)
ax_in.set_ylabel('CW fraction', fontsize=8)
ax_in.set_title('CW frac. vs. confidence', fontsize=8, pad=2)
ax_in.tick_params(labelsize=7)
ax_in.set_ylim(0.490, 0.505)
ax_in.patch.set_alpha(0.9)

fig.tight_layout()
fig.savefig(f'{OUTDIR}/fig_confidence_dist.png', dpi=300, facecolor='white')
plt.close(fig)
print("  Saved fig_confidence_dist.png")


# ═══════════════════════════════════════════════════════════════════════════
# FIGURE 5: North vs South hemisphere comparison
# ═══════════════════════════════════════════════════════════════════════════
print("\n[5/5] Generating hemisphere comparison...")

hemi = analysis['analyses']['4_shamir_comparison']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5))

# -- Panel A: Galactic hemisphere comparison --
north_f = hemi['north_galactic']['cw_fraction']
south_f = hemi['south_galactic']['cw_fraction']
north_n = hemi['north_galactic']['n_galaxies']
south_n = hemi['south_galactic']['n_galaxies']
north_e = np.sqrt(north_f * (1 - north_f) / north_n)
south_e = np.sqrt(south_f * (1 - south_f) / south_n)

diff = hemi['hemisphere_comparison']['difference']
z_score = hemi['hemisphere_comparison']['z_score']

bar_colors = ['#4393C3', '#D6604D']
bars = ax1.bar(['Galactic North', 'Galactic South'],
               [north_f, south_f],
               yerr=[north_e, south_e],
               capsize=5, color=bar_colors, edgecolor='#333', linewidth=0.6,
               width=0.5, zorder=2)
ax1.axhline(0.5, color='#999', linestyle='--', linewidth=0.8, zorder=0)

# Annotate the difference
ymax = max(north_f + north_e, south_f + south_e) + 0.0005
ax1.annotate('', xy=(0, ymax + 0.0002), xytext=(1, ymax + 0.0002),
             arrowprops=dict(arrowstyle='<->', color='#333', lw=1.2))
ax1.text(0.5, ymax + 0.0005, f'$\\Delta = {diff:.4f}$ ({z_score:.2f}$\\sigma$)',
         ha='center', va='bottom', fontsize=10, fontweight='bold', color='#B2182B')

ax1.set_ylabel('CW fraction')
ax1.set_title('Galactic Hemisphere CW Fraction')
ax1.set_ylim(0.493, 0.502)

# Count annotations
for bar, n in zip(bars, [north_n, south_n]):
    ax1.text(bar.get_x() + bar.get_width()/2, 0.4935,
             f'$n = {n:,}$', ha='center', va='bottom', fontsize=8, color='#555')

# -- Panel B: Bootstrap visualization of the difference --
# Simulate bootstrap distribution of the difference
np.random.seed(42)
n_boot = 10000
boot_north = np.random.normal(north_f, north_e, n_boot)
boot_south = np.random.normal(south_f, south_e, n_boot)
boot_diff = boot_north - boot_south

ax2.hist(boot_diff, bins=60, density=True, alpha=0.7, color='#92C5DE',
         edgecolor='#4393C3', linewidth=0.3, zorder=2)

# Mark observed difference
ax2.axvline(diff, color='#B2182B', linewidth=2, linestyle='-', zorder=3,
            label=f'Observed: $\\Delta = {diff:.4f}$')
ax2.axvline(0, color='#333', linewidth=0.8, linestyle='--', zorder=1,
            label='No asymmetry')

# Shade p-value region
x_range = np.linspace(diff, boot_diff.max(), 200)
from scipy.stats import norm
mu_diff = 0
sigma_diff = np.sqrt(north_e**2 + south_e**2)
y_norm = norm.pdf(x_range, mu_diff, sigma_diff)
ax2.fill_between(x_range, y_norm, alpha=0.3, color='#B2182B', zorder=2)

ax2.set_xlabel('$\\Delta$ CW fraction (North $-$ South)')
ax2.set_ylabel('Density')
ax2.set_title(f'N-S Hemisphere Difference (3.05$\\sigma$)')
ax2.legend(frameon=False, loc='upper left', fontsize=9)

fig.tight_layout()
fig.savefig(f'{OUTDIR}/fig_hemisphere.png', dpi=300, facecolor='white')
plt.close(fig)
print("  Saved fig_hemisphere.png")


print("\n" + "="*60)
print("All 5 figures generated successfully in", OUTDIR)
print("="*60)
