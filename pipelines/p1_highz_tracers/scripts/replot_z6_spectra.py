#!/usr/bin/env python3
"""
Improved plotting of 12 z>6 QSO spectra from cached DESI DR1 FITS files.
Better label placement, spectral feature identification, and analysis.
"""

import json
import os
import sys
import numpy as np
import pyarrow.parquet as pq
import healpy as hp
from astropy.io import fits
from scipy.ndimage import uniform_filter1d
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import matplotlib.patches as mpatches

BASE = '/Users/houstongolden/Desktop/CODE_2026/bigbounce/pipelines/p1_highz_tracers'
GOLD_JSON = os.path.join(BASE, 'outputs/gold_anomalies/gold_anomalies.json')
GOLD_PARQUET = os.path.join(BASE, 'outputs/gold_anomalies/gold_anomalies_83.parquet')
OUTDIR = os.path.join(BASE, 'outputs/gold_anomalies/spectra')
TMPDIR = os.path.join(BASE, 'outputs/gold_anomalies/spectra/fits_cache')

NSIDE = 64

# Key QSO emission lines (rest wavelengths in Angstroms)
LINES = {
    'Ly-alpha': 1215.67,
    'Ly-beta': 1025.72,
    'Lyman limit': 912.0,
    'NV 1240': 1240.14,
    'SiIV 1397': 1396.76,
    'CIV 1549': 1549.06,
    'CIII] 1909': 1908.73,
    'MgII 2799': 2798.75,
}

LINE_COLORS = {
    'Ly-alpha': '#e63946',
    'Ly-beta': '#457b9d',
    'Lyman limit': '#2a9d8f',
    'NV 1240': '#e9c46a',
    'SiIV 1397': '#f4a261',
    'CIV 1549': '#264653',
    'CIII] 1909': '#6a4c93',
    'MgII 2799': '#b5838d',
}

# ------------------------------------------------------------------
# Load catalog
# ------------------------------------------------------------------
with open(GOLD_JSON) as f:
    gold = json.load(f)
z6_qsos = sorted([obj for obj in gold if obj['spectype'] == 'QSO' and obj['z'] > 6.0],
                  key=lambda x: -x['anomaly_score'])
df_gold = pq.read_table(GOLD_PARQUET).to_pandas()

print(f"Re-plotting {len(z6_qsos)} z>6 QSO spectra from cached FITS files...")

# ------------------------------------------------------------------
# Extract spectra from cached FITS
# ------------------------------------------------------------------
extracted = {}

for obj in z6_qsos:
    tid = obj['targetid']
    ra, dec = obj['ra'], obj['dec']
    theta = np.radians(90.0 - dec)
    phi = np.radians(ra)
    pix = hp.ang2pix(NSIDE, theta, phi, nest=True)

    fname = f'coadd-main-dark-{pix}.fits'
    fpath = os.path.join(TMPDIR, fname)

    if not os.path.exists(fpath):
        print(f"  FITS file not found for TID {tid} (pixel {pix})")
        continue

    with fits.open(fpath) as hdul:
        fibermap = hdul['FIBERMAP'].data
        target_ids = fibermap['TARGETID']
        idx = np.where(target_ids == tid)[0]
        if len(idx) == 0:
            print(f"  TID {tid} not found in pixel {pix}")
            continue
        idx = idx[0]

        wave_b = hdul['B_WAVELENGTH'].data
        wave_r = hdul['R_WAVELENGTH'].data
        wave_z = hdul['Z_WAVELENGTH'].data
        flux_b = hdul['B_FLUX'].data[idx]
        flux_r = hdul['R_FLUX'].data[idx]
        flux_z = hdul['Z_FLUX'].data[idx]
        ivar_b = hdul['B_IVAR'].data[idx]
        ivar_r = hdul['R_IVAR'].data[idx]
        ivar_z = hdul['Z_IVAR'].data[idx]

        wave = np.concatenate([wave_b, wave_r, wave_z])
        flux = np.concatenate([flux_b, flux_r, flux_z])
        ivar = np.concatenate([ivar_b, ivar_r, ivar_z])

        sort_idx = np.argsort(wave)
        wave = wave[sort_idx]
        flux = flux[sort_idx]
        ivar = ivar[sort_idx]

        extracted[tid] = {
            'wave': wave, 'flux': flux, 'ivar': ivar,
            'z': obj['z'], 'anomaly_score': obj['anomaly_score'],
            'ra': obj['ra'], 'dec': obj['dec'],
            'peak_residual_wavelength': obj['peak_residual_wavelength'],
            'worst_band': obj['worst_band'],
        }

print(f"Extracted {len(extracted)} spectra")

# ------------------------------------------------------------------
# Spectral feature identification
# ------------------------------------------------------------------
def identify_features(wave, flux, ivar, z):
    """Identify spectral features and return annotations."""
    features = []
    flux_smooth = uniform_filter1d(flux, size=11)
    snr = flux * np.sqrt(np.maximum(ivar, 0))
    snr_smooth = uniform_filter1d(snr, size=15)

    # Check each expected emission line
    for name, rest_lam in LINES.items():
        obs_lam = rest_lam * (1 + z)
        if obs_lam < 3600 or obs_lam > 9800:
            continue

        # Check for emission in a window around the expected position
        window = (wave > obs_lam - 30) & (wave < obs_lam + 30)
        if np.sum(window) == 0:
            continue

        local_flux = flux_smooth[window]
        local_snr = snr_smooth[window]
        peak_snr = np.max(local_snr)
        peak_flux = np.max(local_flux)

        # Continuum estimate from nearby
        cont_mask = ((wave > obs_lam - 200) & (wave < obs_lam - 50)) | \
                    ((wave > obs_lam + 50) & (wave < obs_lam + 200))
        if np.sum(cont_mask) > 10:
            continuum = np.median(flux_smooth[cont_mask])
        else:
            continuum = 0

        line_excess = peak_flux - continuum

        if name == 'Ly-alpha':
            # Ly-alpha is often the strongest line in z>6 QSOs
            features.append({
                'name': name,
                'obs_lam': obs_lam,
                'peak_snr': peak_snr,
                'peak_flux': peak_flux,
                'line_excess': line_excess,
                'detected': peak_snr > 2 or peak_flux > 1,
                'type': 'emission'
            })
        elif name == 'Lyman limit':
            features.append({
                'name': name,
                'obs_lam': obs_lam,
                'peak_snr': 0,
                'peak_flux': 0,
                'line_excess': 0,
                'detected': True,  # Always present at z>6
                'type': 'break'
            })
        else:
            features.append({
                'name': name,
                'obs_lam': obs_lam,
                'peak_snr': peak_snr,
                'peak_flux': peak_flux,
                'line_excess': line_excess,
                'detected': peak_snr > 1.5 and line_excess > 0.3,
                'type': 'emission'
            })

    # Check for GP trough - flux should be near zero blueward of Ly-alpha
    obs_lya = LINES['Ly-alpha'] * (1 + z)
    blue_mask = (wave > 3700) & (wave < obs_lya - 100)
    if np.sum(blue_mask) > 50:
        blue_flux = np.median(np.abs(flux_smooth[blue_mask]))
        features.append({
            'name': 'Gunn-Peterson trough',
            'obs_lam': (3700 + obs_lya) / 2,
            'peak_snr': 0,
            'peak_flux': blue_flux,
            'line_excess': 0,
            'detected': blue_flux < 0.5,
            'type': 'absorption'
        })

    return features


# ------------------------------------------------------------------
# Plot individual spectra (improved)
# ------------------------------------------------------------------
print("\nPlotting individual spectra (improved)...")

all_features = {}

for tid, spec in extracted.items():
    wave = spec['wave']
    flux = spec['flux']
    ivar = spec['ivar']
    z = spec['z']
    score = spec['anomaly_score']

    flux_smooth = uniform_filter1d(flux, size=7)
    snr = flux * np.sqrt(np.maximum(ivar, 0))
    snr_smooth = uniform_filter1d(snr, size=15)

    # Identify features
    features = identify_features(wave, flux, ivar, z)
    all_features[tid] = features

    fig, axes = plt.subplots(2, 1, figsize=(16, 9),
                              gridspec_kw={'height_ratios': [3, 1]})

    # --- Top panel ---
    ax = axes[0]

    # Plot raw + smoothed flux
    ax.fill_between(wave, flux, alpha=0.08, color='#1a1a2e')
    ax.plot(wave, flux, color='#cccccc', alpha=0.25, linewidth=0.3)
    ax.plot(wave, flux_smooth, color='#1a1a2e', linewidth=0.8, label='Smoothed (7px)')

    # Auto y-limits from data
    valid = (wave > 3600) & (wave < 9900)
    flux_valid = flux_smooth[valid]
    y_lo = max(np.percentile(flux_valid, 1) - 1, np.min(flux_valid) - 0.5)
    y_hi = np.percentile(flux_valid, 99) + 2
    ax.set_ylim(y_lo, y_hi)

    # Shade Gunn-Peterson trough
    obs_lya = LINES['Ly-alpha'] * (1 + z)
    obs_ly_break = LINES['Lyman limit'] * (1 + z)
    gp_start = max(3600, obs_ly_break)
    if gp_start < obs_lya:
        ax.axvspan(gp_start, obs_lya, alpha=0.12, color='#264653',
                   label=f'Gunn-Peterson trough')

    # Mark expected emission lines
    label_y_positions = np.linspace(y_hi * 0.95, y_hi * 0.55, 8)
    label_idx = 0
    for name, rest_lam in LINES.items():
        obs_lam = rest_lam * (1 + z)
        if obs_lam < 3500 or obs_lam > 10000:
            continue
        color = LINE_COLORS.get(name, 'gray')
        ls = '--' if name != 'Lyman limit' else ':'
        lw = 1.5 if name == 'Ly-alpha' else 1.0

        # Check if this line was detected
        detected = False
        for feat in features:
            if feat['name'] == name and feat['detected']:
                detected = True
                break

        alpha = 0.8 if detected else 0.3
        ax.axvline(obs_lam, color=color, linestyle=ls, alpha=alpha, linewidth=lw)

        # Label
        y_pos = label_y_positions[min(label_idx, len(label_y_positions)-1)]
        marker = '*' if detected else ''
        ax.annotate(f'{marker}{name}\n{obs_lam:.0f}A',
                    xy=(obs_lam, y_pos), fontsize=7, color=color,
                    ha='left', va='top',
                    bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                              alpha=0.7, edgecolor=color, linewidth=0.5))
        label_idx += 1

    # Mark peak residual from autoencoder
    prw = spec['peak_residual_wavelength']
    ax.axvline(prw, color='#e63946', linestyle='-', linewidth=2.5, alpha=0.3)

    ax.set_ylabel('Flux (10$^{-17}$ erg/s/cm$^2$/A)', fontsize=11)
    ax.set_title(f'TARGETID {tid}  |  z = {z:.4f}  |  anomaly_score = {score:.2f}  |  '
                 f'RA = {spec["ra"]:.4f}, Dec = {spec["dec"]:.4f}',
                 fontsize=12, fontweight='bold')
    ax.legend(loc='upper right', fontsize=8)
    ax.set_xlim(3500, 10000)
    ax.grid(True, alpha=0.1)

    # Feature detection summary
    detected_names = [f['name'] for f in features if f['detected']]
    det_text = 'Detected: ' + ', '.join(detected_names) if detected_names else 'No confirmed lines'
    ax.text(0.02, 0.05, det_text, transform=ax.transAxes, fontsize=8,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    # --- Bottom panel: SNR ---
    ax2 = axes[1]
    ax2.plot(wave, snr_smooth, color='#264653', linewidth=0.7)
    ax2.axhline(0, color='gray', linewidth=0.5)
    ax2.axhline(2, color='red', linewidth=0.5, linestyle='--', alpha=0.5)
    ax2.axhline(5, color='orange', linewidth=0.5, linestyle='--', alpha=0.5)
    ax2.text(9850, 2.2, 'SNR=2', fontsize=7, color='red', va='bottom', ha='right')
    ax2.text(9850, 5.2, 'SNR=5', fontsize=7, color='orange', va='bottom', ha='right')
    ax2.set_xlabel('Observed Wavelength (A)', fontsize=11)
    ax2.set_ylabel('SNR per pixel', fontsize=11)
    ax2.set_xlim(3500, 10000)
    ax2.grid(True, alpha=0.1)

    # Shade GP trough in SNR panel too
    if gp_start < obs_lya:
        ax2.axvspan(gp_start, obs_lya, alpha=0.08, color='#264653')

    plt.tight_layout()
    outpath = os.path.join(OUTDIR, f'spectrum_{tid}_z{z:.2f}.png')
    plt.savefig(outpath, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {os.path.basename(outpath)}")

# ------------------------------------------------------------------
# Grid plot (4x3) - improved
# ------------------------------------------------------------------
print("\nCreating improved 4x3 grid plot...")
fig = plt.figure(figsize=(22, 18))
gs = GridSpec(4, 3, figure=fig, hspace=0.4, wspace=0.25)

sorted_specs = sorted(extracted.items(), key=lambda x: -x[1]['anomaly_score'])

for idx, (tid, spec) in enumerate(sorted_specs[:12]):
    row = idx // 3
    col = idx % 3
    ax = fig.add_subplot(gs[row, col])

    wave = spec['wave']
    flux = spec['flux']
    z = spec['z']
    score = spec['anomaly_score']

    flux_smooth = uniform_filter1d(flux, size=7)

    # Plot
    ax.fill_between(wave, flux_smooth, alpha=0.1, color='#1a1a2e')
    ax.plot(wave, flux, color='#cccccc', alpha=0.15, linewidth=0.2)
    ax.plot(wave, flux_smooth, color='#1a1a2e', linewidth=0.6)

    # Auto y-limits
    valid = (wave > 3600) & (wave < 9900)
    fv = flux_smooth[valid]
    y_lo = max(np.percentile(fv, 2) - 0.5, np.min(fv) - 0.3)
    y_hi = np.percentile(fv, 98) + 1.5
    ax.set_ylim(y_lo, y_hi)

    # Ly-alpha marker
    obs_lya = LINES['Ly-alpha'] * (1 + z)
    obs_ly_break = LINES['Lyman limit'] * (1 + z)
    ax.axvline(obs_lya, color='#e63946', linestyle='--', alpha=0.7, linewidth=1.2)
    ax.text(obs_lya + 60, y_hi * 0.85, 'Ly-a', fontsize=7, color='#e63946',
            fontweight='bold')

    # CIV marker
    obs_civ = LINES['CIV 1549'] * (1 + z)
    if obs_civ < 9800:
        ax.axvline(obs_civ, color='#264653', linestyle='--', alpha=0.5, linewidth=0.8)
        ax.text(obs_civ + 40, y_hi * 0.65, 'CIV', fontsize=6, color='#264653')

    # NV marker
    obs_nv = LINES['NV 1240'] * (1 + z)
    if 3600 < obs_nv < 9800:
        ax.axvline(obs_nv, color='#e9c46a', linestyle='--', alpha=0.5, linewidth=0.8)
        ax.text(obs_nv + 40, y_hi * 0.75, 'NV', fontsize=6, color='#e9c46a')

    # GP trough
    gp_start = max(3600, obs_ly_break)
    if gp_start < obs_lya:
        ax.axvspan(gp_start, obs_lya, alpha=0.1, color='#264653')

    # Subtype info
    row_gold = df_gold[df_gold['targetid'] == tid]
    subtype = row_gold['subtype'].values[0] if len(row_gold) > 0 else ''
    snr_z_val = row_gold['median_coadd_snr_z'].values[0] if len(row_gold) > 0 else 0

    ax.set_title(f'TID ...{str(tid)[-8:]}  |  z={z:.4f}  |  score={score:.2f}  |  SNR_z={snr_z_val:.1f}',
                 fontsize=8, fontweight='bold')
    ax.set_xlim(3500, 10000)
    ax.grid(True, alpha=0.08)
    ax.tick_params(labelsize=7)

    if row == 3:
        ax.set_xlabel('Wavelength (A)', fontsize=9)
    if col == 0:
        ax.set_ylabel('Flux', fontsize=9)

fig.suptitle('12 z > 6 QSO Anomalies from DESI DR1 Gold Catalog\n'
             'Spectra downloaded from data.desi.lbl.gov/public/dr1/',
             fontsize=14, fontweight='bold', y=0.99)

# Add legend
legend_elements = [
    mpatches.Patch(facecolor='#264653', alpha=0.15, label='Gunn-Peterson trough'),
    plt.Line2D([0], [0], color='#e63946', linestyle='--', label='Ly-alpha (1216 A rest)'),
    plt.Line2D([0], [0], color='#264653', linestyle='--', label='CIV (1549 A rest)'),
    plt.Line2D([0], [0], color='#e9c46a', linestyle='--', label='NV (1240 A rest)'),
]
fig.legend(handles=legend_elements, loc='lower center', ncol=4, fontsize=9,
           bbox_to_anchor=(0.5, 0.005))

grid_path = os.path.join(OUTDIR, 'z6_qso_spectra_grid.png')
plt.savefig(grid_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"  Saved grid: {grid_path}")

# ------------------------------------------------------------------
# Print spectral feature analysis
# ------------------------------------------------------------------
print(f"\n{'='*80}")
print("SPECTRAL FEATURE ANALYSIS")
print(f"{'='*80}")

for tid, features in all_features.items():
    spec = extracted[tid]
    z = spec['z']
    print(f"\nTID {tid} (z={z:.4f}, score={spec['anomaly_score']:.2f}):")

    for feat in features:
        status = 'DETECTED' if feat['detected'] else 'not detected'
        if feat['type'] == 'emission':
            print(f"  {feat['name']:20s} @ {feat['obs_lam']:.0f}A: "
                  f"peak_SNR={feat['peak_snr']:.1f}, "
                  f"peak_flux={feat['peak_flux']:.2f}, "
                  f"excess={feat['line_excess']:.2f} -> {status}")
        elif feat['type'] == 'break':
            print(f"  {feat['name']:20s} @ {feat['obs_lam']:.0f}A: "
                  f"spectral break -> {status}")
        elif feat['type'] == 'absorption':
            print(f"  {feat['name']:20s}: "
                  f"median |flux| blueward = {feat['peak_flux']:.3f} -> {status}")

# ------------------------------------------------------------------
# Save feature analysis JSON
# ------------------------------------------------------------------
def make_serializable(obj):
    """Convert numpy types to Python natives for JSON."""
    if isinstance(obj, dict):
        return {k: make_serializable(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [make_serializable(v) for v in obj]
    elif isinstance(obj, (np.float32, np.float64)):
        return float(obj)
    elif isinstance(obj, (np.int32, np.int64)):
        return int(obj)
    elif isinstance(obj, np.bool_):
        return bool(obj)
    return obj

feature_output = {}
for tid, features in all_features.items():
    spec = extracted[tid]
    feature_output[str(tid)] = make_serializable({
        'z': spec['z'],
        'anomaly_score': spec['anomaly_score'],
        'ra': spec['ra'],
        'dec': spec['dec'],
        'features': features,
        'lya_observed_wavelength': LINES['Ly-alpha'] * (1 + spec['z']),
        'lyman_break_observed': LINES['Lyman limit'] * (1 + spec['z']),
        'n_detected_features': sum(1 for f in features if f['detected']),
    })

feat_path = os.path.join(OUTDIR, 'z6_qso_spectral_features.json')
with open(feat_path, 'w') as f:
    json.dump(feature_output, f, indent=2)
print(f"\nSaved feature analysis: {feat_path}")

print("\nDone!")
