#!/usr/bin/env python3
"""
Download DESI DR1 spectra for 12 z>6 QSOs from the gold anomalies catalog,
extract individual spectra, plot them with spectral line identifications,
and save individual + grid plots.
"""

import json
import os
import sys
import numpy as np
import pandas as pd
import pyarrow.parquet as pq
import healpy as hp
import urllib.request
import ssl
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Paths
BASE = '/Users/houstongolden/Desktop/CODE_2026/bigbounce/pipelines/p1_highz_tracers'
GOLD_JSON = os.path.join(BASE, 'outputs/gold_anomalies/gold_anomalies.json')
GOLD_PARQUET = os.path.join(BASE, 'outputs/gold_anomalies/gold_anomalies_83.parquet')
OUTDIR = os.path.join(BASE, 'outputs/gold_anomalies/spectra')
TMPDIR = os.path.join(BASE, 'outputs/gold_anomalies/spectra/fits_cache')
DESI_BASE = 'https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/healpix/main/dark'

os.makedirs(OUTDIR, exist_ok=True)
os.makedirs(TMPDIR, exist_ok=True)

# DESI healpix nside
NSIDE = 64  # DESI DR1 uses nside=64 for healpix grouping

# ------------------------------------------------------------------
# 1. Load the 12 z>6 QSOs
# ------------------------------------------------------------------
print("Loading gold anomalies catalog...")
with open(GOLD_JSON) as f:
    gold = json.load(f)

z6_qsos = [obj for obj in gold if obj['spectype'] == 'QSO' and obj['z'] > 6.0]
z6_qsos.sort(key=lambda x: -x['anomaly_score'])
print(f"Found {len(z6_qsos)} QSOs with z > 6")

# Load full parquet for enriched data
df_gold = pq.read_table(GOLD_PARQUET).to_pandas()
z6_tids = set(obj['targetid'] for obj in z6_qsos)
df_z6 = df_gold[df_gold['targetid'].isin(z6_tids)].copy()
print(f"Matched {len(df_z6)} in parquet")

# ------------------------------------------------------------------
# 2. Compute healpix pixels and group downloads
# ------------------------------------------------------------------
print("\nComputing healpix pixels for each target...")
targets = []
for obj in z6_qsos:
    ra, dec = obj['ra'], obj['dec']
    # Convert to healpix pixel (DESI uses NESTED ordering, nside=64)
    theta = np.radians(90.0 - dec)
    phi = np.radians(ra)
    pix = hp.ang2pix(NSIDE, theta, phi, nest=True)
    group = pix // 100  # DESI groups pixels by first digits
    targets.append({
        'targetid': obj['targetid'],
        'ra': ra,
        'dec': dec,
        'z': obj['z'],
        'anomaly_score': obj['anomaly_score'],
        'peak_residual_wavelength': obj['peak_residual_wavelength'],
        'worst_band': obj['worst_band'],
        'healpix_pixel': int(pix),
        'healpix_group': int(group),
    })
    print(f"  TID {obj['targetid']}: (RA={ra:.4f}, Dec={dec:.4f}) -> pixel={pix}, group={group}")

# Group by healpix pixel to minimize downloads
pixel_groups = {}
for t in targets:
    pix = t['healpix_pixel']
    if pix not in pixel_groups:
        pixel_groups[pix] = []
    pixel_groups[pix].append(t)

print(f"\n{len(pixel_groups)} unique healpix pixels to download")

# ------------------------------------------------------------------
# 3. Download FITS files and extract spectra
# ------------------------------------------------------------------
# Create SSL context that doesn't verify (DESI data server sometimes has cert issues)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

extracted_spectra = {}

for pix, pixel_targets in pixel_groups.items():
    group = pixel_targets[0]['healpix_group']
    fname = f'coadd-main-dark-{pix}.fits'
    fpath = os.path.join(TMPDIR, fname)
    url = f'{DESI_BASE}/{group}/{pix}/{fname}'

    print(f"\nDownloading pixel {pix} (group {group}): {url}")

    try:
        if not os.path.exists(fpath):
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, context=ctx, timeout=120) as response:
                with open(fpath, 'wb') as out:
                    out.write(response.read())
            print(f"  Downloaded {os.path.getsize(fpath) / 1e6:.1f} MB")
        else:
            print(f"  Using cached file ({os.path.getsize(fpath) / 1e6:.1f} MB)")

        # Open and extract spectra
        with fits.open(fpath) as hdul:
            # Print all HDU names for debugging
            print(f"  HDU list: {[h.name for h in hdul]}")

            fibermap = hdul['FIBERMAP'].data
            target_ids = fibermap['TARGETID']

            # DESI wavelength grids per arm
            wave_b = hdul['B_WAVELENGTH'].data
            wave_r = hdul['R_WAVELENGTH'].data
            wave_z = hdul['Z_WAVELENGTH'].data

            flux_b = hdul['B_FLUX'].data
            flux_r = hdul['R_FLUX'].data
            flux_z = hdul['Z_FLUX'].data

            ivar_b = hdul['B_IVAR'].data
            ivar_r = hdul['R_IVAR'].data
            ivar_z = hdul['Z_IVAR'].data

            for t in pixel_targets:
                tid = t['targetid']
                idx = np.where(target_ids == tid)[0]
                if len(idx) == 0:
                    print(f"  WARNING: TID {tid} not found in pixel {pix}!")
                    continue
                idx = idx[0]

                # Concatenate wavelength and flux
                wave = np.concatenate([wave_b, wave_r, wave_z])
                flux = np.concatenate([flux_b[idx], flux_r[idx], flux_z[idx]])
                ivar = np.concatenate([ivar_b[idx], ivar_r[idx], ivar_z[idx]])

                # Sort by wavelength
                sort_idx = np.argsort(wave)
                wave = wave[sort_idx]
                flux = flux[sort_idx]
                ivar = ivar[sort_idx]

                extracted_spectra[tid] = {
                    'wave': wave,
                    'flux': flux,
                    'ivar': ivar,
                    'z': t['z'],
                    'anomaly_score': t['anomaly_score'],
                    'ra': t['ra'],
                    'dec': t['dec'],
                    'peak_residual_wavelength': t['peak_residual_wavelength'],
                }
                print(f"  Extracted TID {tid}: {len(wave)} pixels, "
                      f"flux range [{np.nanmin(flux):.2f}, {np.nanmax(flux):.2f}]")

    except Exception as e:
        print(f"  ERROR downloading pixel {pix}: {e}")
        # Try alternate URLs
        for alt_program in ['bright']:
            alt_fname = f'coadd-main-{alt_program}-{pix}.fits'
            alt_url = f'https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/healpix/main/{alt_program}/{group}/{pix}/{alt_fname}'
            try:
                print(f"  Trying alternate: {alt_url}")
                if not os.path.exists(os.path.join(TMPDIR, alt_fname)):
                    req = urllib.request.Request(alt_url, headers={'User-Agent': 'Mozilla/5.0'})
                    with urllib.request.urlopen(req, context=ctx, timeout=120) as response:
                        with open(os.path.join(TMPDIR, alt_fname), 'wb') as out:
                            out.write(response.read())
                    print(f"  Downloaded alternate")
                break
            except:
                continue

print(f"\n{'='*60}")
print(f"Successfully extracted {len(extracted_spectra)} / {len(z6_qsos)} spectra")
print(f"{'='*60}")

# ------------------------------------------------------------------
# 4. Plot individual spectra
# ------------------------------------------------------------------
# Key QSO emission lines (rest wavelengths in Angstroms)
LINES = {
    'Ly-alpha': 1215.67,
    'Ly-beta': 1025.72,
    'Lyman break': 912.0,
    'NV': 1240.14,
    'SiIV': 1396.76,
    'CIV': 1549.06,
    'CIII]': 1908.73,
    'MgII': 2798.75,
}

def plot_spectrum(tid, spec, outpath):
    """Plot a single QSO spectrum with line identifications."""
    wave = spec['wave']
    flux = spec['flux']
    ivar = spec['ivar']
    z = spec['z']
    score = spec['anomaly_score']

    fig, axes = plt.subplots(2, 1, figsize=(14, 8),
                              gridspec_kw={'height_ratios': [3, 1]})

    # --- Top panel: Full spectrum ---
    ax = axes[0]

    # Smooth flux for visibility
    from scipy.ndimage import uniform_filter1d
    flux_smooth = uniform_filter1d(flux, size=7)

    # Error bars from ivar
    err = np.where(ivar > 0, 1.0 / np.sqrt(ivar), 0)

    # Plot raw flux as light gray
    ax.plot(wave, flux, color='#cccccc', alpha=0.3, linewidth=0.5, label='Raw')
    # Plot smoothed flux
    ax.plot(wave, flux_smooth, color='#1a1a2e', linewidth=0.8, label='Smoothed (7px)')

    # Shade DESI arm boundaries
    ax.axvspan(3600, 5800, alpha=0.05, color='blue', label='B arm')
    ax.axvspan(5760, 7620, alpha=0.05, color='green', label='R arm')
    ax.axvspan(7520, 9824, alpha=0.05, color='red', label='Z arm')

    # Mark emission lines
    obs_lya = LINES['Ly-alpha'] * (1 + z)
    obs_lyb = LINES['Ly-beta'] * (1 + z)
    obs_ly_break = LINES['Lyman break'] * (1 + z)

    line_colors = {
        'Ly-alpha': '#e63946',
        'Ly-beta': '#457b9d',
        'Lyman break': '#2a9d8f',
        'NV': '#e9c46a',
        'SiIV': '#f4a261',
        'CIV': '#264653',
        'CIII]': '#6a4c93',
        'MgII': '#b5838d',
    }

    for name, rest_lam in LINES.items():
        obs_lam = rest_lam * (1 + z)
        if 3500 < obs_lam < 10000:
            color = line_colors.get(name, 'gray')
            ls = '--' if name != 'Lyman break' else ':'
            ax.axvline(obs_lam, color=color, linestyle=ls, alpha=0.7, linewidth=1.2)
            # Place label at top of plot
            ax.text(obs_lam + 20, ax.get_ylim()[1] * 0.85 if ax.get_ylim()[1] > 0 else 5,
                    f'{name}\n({obs_lam:.0f} A)', fontsize=7, color=color,
                    rotation=90, va='top', ha='left')

    # Shade Gunn-Peterson trough region (below Ly-alpha in observed frame)
    gp_start = max(3600, obs_ly_break)
    gp_end = obs_lya
    if gp_start < gp_end:
        ax.axvspan(gp_start, gp_end, alpha=0.08, color='#264653',
                   label=f'GP trough ({gp_start:.0f}-{gp_end:.0f} A)')

    # Mark peak residual wavelength
    prw = spec['peak_residual_wavelength']
    ax.axvline(prw, color='#e63946', linestyle='-', linewidth=2, alpha=0.5)
    ax.text(prw + 30, ax.get_ylim()[1] * 0.6 if ax.get_ylim()[1] > 0 else 3,
            f'Peak residual\n({prw:.0f} A)', fontsize=7, color='#e63946',
            fontweight='bold')

    ax.set_ylabel('Flux (10$^{-17}$ erg/s/cm$^2$/A)', fontsize=11)
    ax.set_title(f'TARGETID {tid}  |  z = {z:.4f}  |  anomaly score = {score:.2f}  |  '
                 f'RA={spec["ra"]:.4f}, Dec={spec["dec"]:.4f}',
                 fontsize=12, fontweight='bold')
    ax.legend(loc='upper right', fontsize=7, ncol=3)
    ax.set_xlim(3500, 10000)
    ax.grid(True, alpha=0.15)

    # --- Bottom panel: SNR per pixel ---
    ax2 = axes[1]
    snr = flux * np.sqrt(np.maximum(ivar, 0))
    snr_smooth = uniform_filter1d(snr, size=15)
    ax2.plot(wave, snr_smooth, color='#264653', linewidth=0.7)
    ax2.axhline(0, color='gray', linewidth=0.5)
    ax2.axhline(2, color='red', linewidth=0.5, linestyle='--', alpha=0.5, label='SNR=2')
    ax2.set_xlabel('Observed Wavelength (A)', fontsize=11)
    ax2.set_ylabel('SNR per pixel', fontsize=11)
    ax2.set_xlim(3500, 10000)
    ax2.legend(fontsize=7)
    ax2.grid(True, alpha=0.15)

    plt.tight_layout()
    plt.savefig(outpath, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {outpath}")


# If we got spectra, plot them
if extracted_spectra:
    from scipy.ndimage import uniform_filter1d

    print("\nPlotting individual spectra...")
    for tid, spec in extracted_spectra.items():
        outpath = os.path.join(OUTDIR, f'spectrum_{tid}_z{spec["z"]:.2f}.png')
        plot_spectrum(tid, spec, outpath)

    # ------------------------------------------------------------------
    # 5. Grid plot (4x3)
    # ------------------------------------------------------------------
    print("\nCreating 4x3 grid plot...")
    fig = plt.figure(figsize=(20, 16))
    gs = GridSpec(4, 3, figure=fig, hspace=0.35, wspace=0.25)

    sorted_specs = sorted(extracted_spectra.items(),
                          key=lambda x: -x[1]['anomaly_score'])

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
        ax.plot(wave, flux, color='#cccccc', alpha=0.2, linewidth=0.3)
        ax.plot(wave, flux_smooth, color='#1a1a2e', linewidth=0.6)

        # Ly-alpha
        obs_lya = LINES['Ly-alpha'] * (1 + z)
        obs_ly_break = LINES['Lyman break'] * (1 + z)
        ax.axvline(obs_lya, color='#e63946', linestyle='--', alpha=0.7, linewidth=1)
        ax.text(obs_lya + 50, ax.get_ylim()[1] * 0.8 if ax.get_ylim()[1] > 0 else 3,
                'Ly-a', fontsize=6, color='#e63946')

        # GP trough
        gp_start = max(3600, obs_ly_break)
        if gp_start < obs_lya:
            ax.axvspan(gp_start, obs_lya, alpha=0.08, color='#264653')

        # CIV if visible
        obs_civ = LINES['CIV'] * (1 + z)
        if obs_civ < 9800:
            ax.axvline(obs_civ, color='#264653', linestyle='--', alpha=0.5, linewidth=0.8)
            ax.text(obs_civ + 30, ax.get_ylim()[1] * 0.6 if ax.get_ylim()[1] > 0 else 2,
                    'CIV', fontsize=6, color='#264653')

        ax.set_title(f'TID ...{str(tid)[-6:]}  z={z:.4f}  score={score:.2f}',
                     fontsize=9, fontweight='bold')
        ax.set_xlim(3500, 10000)
        ax.grid(True, alpha=0.1)
        ax.tick_params(labelsize=7)

        if row == 3:
            ax.set_xlabel('Wavelength (A)', fontsize=8)
        if col == 0:
            ax.set_ylabel('Flux', fontsize=8)

    fig.suptitle('12 z > 6 QSO Anomalies from DESI DR1 Gold Catalog',
                 fontsize=16, fontweight='bold', y=0.98)

    grid_path = os.path.join(OUTDIR, 'z6_qso_spectra_grid.png')
    plt.savefig(grid_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved grid: {grid_path}")

else:
    print("\nNo spectra were downloaded from DESI. Trying alternate approach...")

# ------------------------------------------------------------------
# 6. Save detailed JSON for all 12 objects regardless
# ------------------------------------------------------------------
print("\nSaving detailed z6_qsos_detailed.json...")
detailed = []
for _, row in df_z6.iterrows():
    obj = {}
    for col in df_z6.columns:
        if col.startswith('lat_'):
            continue  # Skip latent vectors for JSON
        val = row[col]
        if isinstance(val, (np.float32, np.float64)):
            obj[col] = float(val)
        elif isinstance(val, (np.int32, np.int64)):
            obj[col] = int(val)
        elif isinstance(val, np.bool_):
            obj[col] = bool(val)
        else:
            obj[col] = val

    tid = int(row['targetid'])
    # Add healpix info
    ra, dec = float(row['target_ra']), float(row['target_dec'])
    theta = np.radians(90.0 - dec)
    phi = np.radians(ra)
    pix = hp.ang2pix(NSIDE, theta, phi, nest=True)
    obj['healpix_pixel'] = int(pix)
    obj['healpix_group'] = int(pix // 100)

    # Add latent vector summary
    lat_cols = [c for c in df_z6.columns if c.startswith('lat_')]
    lat_vec = [float(row[c]) for c in lat_cols]
    obj['latent_vector_norm'] = float(np.linalg.norm(lat_vec))
    obj['latent_vector_mean'] = float(np.mean(lat_vec))
    obj['latent_vector_std'] = float(np.std(lat_vec))

    # Add DESI viewer URLs
    obj['desi_spectrum_url'] = (
        f'https://www.legacysurvey.org/viewer/desi-spectrum/daily/'
        f'targetid{tid}'
    )
    obj['legacy_survey_url'] = (
        f'https://www.legacysurvey.org/viewer?ra={ra:.6f}&dec={dec:.6f}'
        f'&layer=ls-dr10&zoom=15'
    )

    # Mark whether we got actual spectrum
    obj['spectrum_downloaded'] = tid in extracted_spectra

    detailed.append(obj)

# Sort by anomaly score
detailed.sort(key=lambda x: -x['anomaly_score'])

output_json = os.path.join(OUTDIR, 'z6_qsos_detailed.json')
with open(output_json, 'w') as f:
    json.dump(detailed, f, indent=2)
print(f"Saved: {output_json}")

# ------------------------------------------------------------------
# 7. Summary table
# ------------------------------------------------------------------
print(f"\n{'='*80}")
print(f"SUMMARY: 12 z > 6 QSO Anomalies from DESI DR1")
print(f"{'='*80}")
print(f"{'TID':>20} {'z':>8} {'Score':>7} {'RA':>10} {'Dec':>10} {'SNR_z':>7} {'deltachi2':>10} {'Spectrum':>10}")
print(f"{'-'*20} {'-'*8} {'-'*7} {'-'*10} {'-'*10} {'-'*7} {'-'*10} {'-'*10}")
for obj in detailed:
    downloaded = 'YES' if obj['spectrum_downloaded'] else 'NO'
    print(f"{obj['targetid']:>20} {obj['z']:>8.4f} {obj['anomaly_score']:>7.2f} "
          f"{obj['target_ra']:>10.4f} {obj['target_dec']:>10.4f} "
          f"{obj.get('median_coadd_snr_z', 0):>7.2f} {obj.get('deltachi2', 0):>10.2f} "
          f"{downloaded:>10}")

print(f"\nSpectra downloaded: {len(extracted_spectra)} / {len(z6_qsos)}")
print(f"Output directory: {OUTDIR}")
print(f"Done!")
