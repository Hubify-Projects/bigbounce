#!/usr/bin/env python3
"""
NEOWISE Path-C ecliptic-latitude distribution figure — P3-PATHC-NEOWISE-ECLIPTIC-MASK
======================================================================================
Produces a reviewer-grade figure that motivates the |b_ecl| < 80 deg mask
applied to the 436-row raw NEOWISE anomaly catalog. Plots:
  (a) Histogram of |ecliptic_lat| for all 436 raw anomalies with the 17
      rejected objects highlighted.
  (b) Uniform-sphere null expectation (area-weighted cos(b_ecl) density)
      overlaid as the dashed reference curve.
  (c) Annotation stating the 2.566× pole excess (observed 3.9% vs
      uniform-null 1.5%) and the retained count (419/436 = 96.1%).

This figure is committed as supplementary reviewer evidence for
`sec:pathc_caveats` footnote (†) — not added to the paper main body
(that would trigger a PDF recompile gated on criterion #9). The figure is
available at `pipelines/p3_anomaly_engine/figures/fig_pathc_neowise_ecliptic.{png,pdf}`
for referees and the public HF/GitHub audience.

Run (local CPU, ~5 s):
    python3 pipelines/p3_anomaly_engine/pathc_neowise_ecliptic/plot_ecliptic_latitude_distribution.py
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent
RAW_PATH = ROOT / '..' / 'hf_staging' / 'neowise_anomalies.parquet'
MASKED_PATH = ROOT / 'neowise_pathc_masked_anomalies.parquet'
REJECTED_PATH = ROOT / 'neowise_pathc_rejected_anomalies.parquet'
FIG_DIR = ROOT / '..' / 'figures'
FIG_DIR.mkdir(parents=True, exist_ok=True)

# Reconstruct ecliptic_lat for the raw set (masked/rejected already have it;
# the raw hf_staging parquet is pre-ecliptic-transform).
from astropy.coordinates import SkyCoord, BarycentricTrueEcliptic
import astropy.units as u

raw = pd.read_parquet(RAW_PATH)
masked = pd.read_parquet(MASKED_PATH)
rejected = pd.read_parquet(REJECTED_PATH)

sc = SkyCoord(ra=raw['ra'].values * u.deg, dec=raw['dec'].values * u.deg, frame='icrs')
elat_all = sc.transform_to(BarycentricTrueEcliptic()).lat.deg
raw_with_elat = raw.assign(ecliptic_lat=elat_all)
elat_rej = rejected['ecliptic_lat'].values

# --- Figure --------------------------------------------------------------
fig, ax = plt.subplots(1, 1, figsize=(7.5, 4.5), dpi=150)

bins = np.linspace(0, 90, 19)  # 5-degree bins
abs_all = np.abs(elat_all)
abs_rej = np.abs(elat_rej)

# Observed histogram (all 436 raw anomalies)
ax.hist(abs_all, bins=bins, color='#2c7fb8', alpha=0.75, edgecolor='white',
        label=f'All raw anomalies (N={len(raw)})')

# Rejected overlay (17 objects with |b_ecl| > 80 deg)
ax.hist(abs_rej, bins=bins, color='#d7301f', alpha=0.95, edgecolor='white',
        label=f'Path-C rejected (|b_ecl| > 80 deg, N={len(rejected)})')

# Uniform-sphere null: density(|b_ecl|) = cos(b) / (sum_bin cos(b)) * N_total
bin_centers = 0.5 * (bins[:-1] + bins[1:])
null_density = np.cos(np.radians(bin_centers))
null_density /= null_density.sum()
null_counts = null_density * len(raw)
ax.plot(bin_centers, null_counts, linestyle='--', color='black', linewidth=1.3,
        label='Uniform-sphere null (cos(b_ecl))')

# |b_ecl| = 80 deg cut line
ax.axvline(80, color='#d7301f', linestyle=':', linewidth=1.5, alpha=0.8)
ax.text(80.3, ax.get_ylim()[1] * 0.90, '|b_ecl| = 80°\ncut', color='#d7301f',
        fontsize=9, ha='left', va='top')

ax.set_xlabel(r'$|\beta_{\rm ecliptic}|$  (degrees)', fontsize=12)
ax.set_ylabel('N anomalies per 5° bin', fontsize=12)
ax.set_title('NEOWISE Path-C ecliptic-mask motivation — 2.57× pole excess', fontsize=12)
ax.set_xlim(0, 92)
ax.grid(axis='y', alpha=0.25)
ax.legend(loc='upper left', fontsize=9, framealpha=0.9)

# Annotation box
obs_pct = 100 * len(rejected) / len(raw)
uniform_pct_pole = 100 * (1 - np.sin(np.radians(80)))  # sphere area with |b_ecl| > 80 deg = 1 - sin(80)
excess_factor = obs_pct / uniform_pct_pole
txt = (f'Observed rejection:\n  {len(rejected)}/{len(raw)} = {obs_pct:.2f}%\n'
       f'Uniform-sphere expectation:\n  {uniform_pct_pole:.2f}%\n'
       f'Excess factor: {excess_factor:.2f}×\n'
       f'Retained (Path-C): {len(masked)}/{len(raw)} = {100*len(masked)/len(raw):.1f}%')
ax.text(0.98, 0.55, txt, transform=ax.transAxes, fontsize=9,
        ha='right', va='top',
        bbox=dict(facecolor='white', edgecolor='#bbbbbb', boxstyle='round,pad=0.5',
                  alpha=0.95))

fig.tight_layout()

png_path = FIG_DIR / 'fig_pathc_neowise_ecliptic.png'
pdf_path = FIG_DIR / 'fig_pathc_neowise_ecliptic.pdf'
fig.savefig(png_path, bbox_inches='tight', dpi=150)
fig.savefig(pdf_path, bbox_inches='tight')
print(f'wrote {png_path}')
print(f'wrote {pdf_path}')
print(f'  N_raw={len(raw)}  N_masked={len(masked)}  N_rejected={len(rejected)}')
print(f'  observed={obs_pct:.2f}%  uniform-null={uniform_pct_pole:.2f}%  excess={excess_factor:.2f}x')
