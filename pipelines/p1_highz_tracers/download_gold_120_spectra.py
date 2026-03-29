#!/usr/bin/env python3
"""
Download DESI DR1 spectra for all 120 gold anomalies and create plots.

Gold anomalies: anomaly_score > 5.0, max(SNR_b, SNR_r, SNR_z) > 0.5
"""
import os
import sys
import json
import time
import hashlib
import numpy as np
import pandas as pd
import healpy as hp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from astropy.io import fits
from scipy.ndimage import uniform_filter1d
import urllib.request
import urllib.error
import ssl
import warnings
warnings.filterwarnings('ignore')

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GOLD_CSV = os.path.join(BASE_DIR, 'outputs/gold_anomalies/gold_120_snr05.csv')
OUTPUT_DIR = os.path.join(BASE_DIR, 'outputs/gold_anomalies/spectra/all_120')
CACHE_DIR = os.path.join(BASE_DIR, 'outputs/gold_anomalies/spectra/fits_cache')
GRID_DIR = os.path.join(BASE_DIR, 'outputs/gold_anomalies/spectra')

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(CACHE_DIR, exist_ok=True)

# DESI base URL
DESI_BASE = 'https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/healpix'

# Survey/program combos to try (in order of likelihood)
SURVEY_PROGRAMS = [
    ('main', 'dark'),
    ('main', 'bright'),
    ('sv3', 'dark'),
    ('sv3', 'bright'),
    ('sv1', 'dark'),
    ('sv1', 'bright'),
    ('special', 'dark'),
    ('special', 'bright'),
]

# SSL context that doesn't verify (DESI server sometimes has cert issues)
ssl_ctx = ssl.create_default_context()
ssl_ctx.check_hostname = False
ssl_ctx.verify_mode = ssl.CERT_NONE


def compute_healpix(ra, dec, nside=64):
    """Compute HEALPix pixel for given RA, DEC."""
    pixel = hp.ang2pix(nside, ra, dec, lonlat=True, nest=True)
    group = str(pixel // 100)
    return int(pixel), group


def download_fits(pixel, group, survey, program, cache_dir):
    """Download a coadd FITS file from DESI, return local path or None."""
    filename = f'coadd-{survey}-{program}-{pixel}.fits'
    cache_path = os.path.join(cache_dir, filename)

    if os.path.exists(cache_path) and os.path.getsize(cache_path) > 1000:
        return cache_path

    url = f'{DESI_BASE}/{survey}/{program}/{group}/{pixel}/{filename}'

    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'BigBounce-Research/1.0')
        response = urllib.request.urlopen(req, timeout=60, context=ssl_ctx)
        data = response.read()

        with open(cache_path, 'wb') as f:
            f.write(data)

        return cache_path
    except (urllib.error.HTTPError, urllib.error.URLError, Exception) as e:
        # Clean up partial downloads
        if os.path.exists(cache_path):
            os.remove(cache_path)
        return None


def extract_spectrum(fits_path, targetid):
    """Extract spectrum for a specific targetid from a coadd FITS file."""
    try:
        with fits.open(fits_path) as hdul:
            # Find the target in FIBERMAP
            fibermap = hdul['FIBERMAP'].data
            target_ids = fibermap['TARGETID']

            # Match targetid
            mask = target_ids == targetid
            if not np.any(mask):
                return None

            idx = np.where(mask)[0][0]

            result = {'bands': {}}

            for band in ['B', 'R', 'Z']:
                wave_ext = f'{band}_WAVELENGTH'
                flux_ext = f'{band}_FLUX'
                ivar_ext = f'{band}_IVAR'

                if wave_ext in [h.name for h in hdul] and flux_ext in [h.name for h in hdul]:
                    wave = hdul[wave_ext].data
                    flux = hdul[flux_ext].data

                    if flux.ndim == 2:
                        flux_row = flux[idx]
                    else:
                        flux_row = flux

                    # Get ivar if available
                    ivar = None
                    if ivar_ext in [h.name for h in hdul]:
                        ivar_data = hdul[ivar_ext].data
                        if ivar_data.ndim == 2:
                            ivar = ivar_data[idx]
                        else:
                            ivar = ivar_data

                    result['bands'][band] = {
                        'wavelength': wave,
                        'flux': flux_row,
                        'ivar': ivar
                    }

            return result if result['bands'] else None
    except Exception as e:
        print(f'  Error extracting spectrum: {e}')
        return None


def plot_spectrum(spectrum, target_info, output_path):
    """Plot a single spectrum with all bands."""
    fig, ax = plt.subplots(1, 1, figsize=(14, 5))

    band_colors = {'B': '#3B82F6', 'R': '#EF4444', 'Z': '#8B5CF6'}
    band_labels = {'B': 'B-arm (3600-5800A)', 'R': 'R-arm (5760-7620A)', 'Z': 'Z-arm (7520-9824A)'}

    all_flux = []
    all_wave = []

    for band in ['B', 'R', 'Z']:
        if band in spectrum['bands']:
            wave = spectrum['bands'][band]['wavelength']
            flux = spectrum['bands'][band]['flux']

            # Remove bad values
            good = np.isfinite(flux) & np.isfinite(wave) & (wave > 0)
            wave = wave[good]
            flux = flux[good]

            if len(wave) == 0:
                continue

            all_flux.extend(flux)
            all_wave.extend(wave)

            # Plot raw spectrum
            ax.plot(wave, flux, color=band_colors[band], alpha=0.4, linewidth=0.5)

            # Plot smoothed version
            if len(flux) > 20:
                smooth = uniform_filter1d(flux, size=15)
                ax.plot(wave, smooth, color=band_colors[band], linewidth=1.5,
                       label=band_labels[band])

    if not all_flux:
        plt.close()
        return False

    # Compute plot limits
    all_flux = np.array(all_flux)
    all_wave = np.array(all_wave)
    good_flux = all_flux[np.isfinite(all_flux)]

    if len(good_flux) > 0:
        p5, p95 = np.percentile(good_flux, [2, 98])
        flux_range = p95 - p5
        ymin = p5 - 0.3 * flux_range
        ymax = p95 + 0.3 * flux_range
        ax.set_ylim(ymin, ymax)

    # Mark emission lines based on redshift
    z = target_info['z']
    lines = {
        'Ly-alpha': 1215.67,
        'N V': 1240.14,
        'Si IV': 1396.76,
        'C IV': 1549.06,
        'C III]': 1908.73,
        'Mg II': 2798.75,
        'O II': 3727.09,
        'H-beta': 4861.33,
        'O III': 4958.91,
        'O III': 5006.84,
        'H-alpha': 6562.80,
    }

    for line_name, rest_wave in lines.items():
        obs_wave = rest_wave * (1 + z)
        if min(all_wave) < obs_wave < max(all_wave):
            ax.axvline(obs_wave, color='gray', linestyle='--', alpha=0.5, linewidth=0.8)
            ax.text(obs_wave, ax.get_ylim()[1] * 0.95, line_name,
                   rotation=90, fontsize=7, alpha=0.7, va='top', ha='right')

    # Mark peak residual wavelength
    prw = target_info.get('peak_residual_wavelength', 0)
    if prw > 0 and min(all_wave) < prw < max(all_wave):
        ax.axvline(prw, color='orange', linestyle='-', alpha=0.8, linewidth=1.5)
        ax.text(prw + 20, ax.get_ylim()[1] * 0.9, 'peak\nresidual',
               fontsize=7, color='orange', va='top')

    ax.set_xlabel('Wavelength (Angstrom)', fontsize=11)
    ax.set_ylabel('Flux (10$^{-17}$ erg/s/cm$^2$/A)', fontsize=11)

    tid = target_info['targetid']
    score = target_info['anomaly_score']
    spectype = target_info['spectype']
    zwarn = target_info.get('zwarn', -1)
    max_snr = target_info.get('max_snr', 0)

    title = (f'DESI DR1 Gold Anomaly: TARGETID={tid}\n'
             f'z={z:.4f}  |  score={score:.2f}  |  {spectype}  |  '
             f'ZWARN={zwarn}  |  max_SNR={max_snr:.1f}')
    ax.set_title(title, fontsize=11, fontweight='bold')

    ax.legend(loc='upper right', fontsize=8)
    ax.grid(True, alpha=0.2)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    return True


def create_summary_grid(gold_df, success_list, spectype_filter, grid_path, max_per_grid=30):
    """Create a summary grid of spectra for a given spectype."""
    filtered = [s for s in success_list if s['spectype'] == spectype_filter]

    if not filtered:
        print(f'  No {spectype_filter} spectra to grid')
        return

    # Sort by anomaly score descending
    filtered.sort(key=lambda x: x['anomaly_score'], reverse=True)

    # Split into pages if needed
    n_pages = (len(filtered) + max_per_grid - 1) // max_per_grid

    for page in range(n_pages):
        page_items = filtered[page*max_per_grid : (page+1)*max_per_grid]
        n = len(page_items)

        ncols = min(5, n)
        nrows = (n + ncols - 1) // ncols

        fig, axes = plt.subplots(nrows, ncols, figsize=(5*ncols, 3.5*nrows))
        if nrows == 1 and ncols == 1:
            axes = np.array([[axes]])
        elif nrows == 1:
            axes = axes.reshape(1, -1)
        elif ncols == 1:
            axes = axes.reshape(-1, 1)

        for i, item in enumerate(page_items):
            row, col = divmod(i, ncols)
            ax = axes[row, col]

            spectrum = item['spectrum']
            band_colors = {'B': '#3B82F6', 'R': '#EF4444', 'Z': '#8B5CF6'}

            all_flux = []
            all_wave = []

            for band in ['B', 'R', 'Z']:
                if band in spectrum['bands']:
                    wave = spectrum['bands'][band]['wavelength']
                    flux = spectrum['bands'][band]['flux']
                    good = np.isfinite(flux) & np.isfinite(wave) & (wave > 0)
                    wave = wave[good]
                    flux = flux[good]

                    if len(wave) == 0:
                        continue

                    all_flux.extend(flux)
                    all_wave.extend(wave)

                    if len(flux) > 20:
                        smooth = uniform_filter1d(flux, size=15)
                        ax.plot(wave, smooth, color=band_colors[band], linewidth=0.8, alpha=0.9)
                    else:
                        ax.plot(wave, flux, color=band_colors[band], linewidth=0.5, alpha=0.7)

            if all_flux:
                af = np.array(all_flux)
                good_f = af[np.isfinite(af)]
                if len(good_f) > 0:
                    p5, p95 = np.percentile(good_f, [2, 98])
                    fr = p95 - p5
                    ax.set_ylim(p5 - 0.3*fr, p95 + 0.3*fr)

            # Mark Lya if z > 2
            z = item['z']
            if z > 2:
                lya_obs = 1215.67 * (1 + z)
                if all_wave and min(all_wave) < lya_obs < max(all_wave):
                    ax.axvline(lya_obs, color='cyan', alpha=0.5, linewidth=0.8, linestyle='--')

            tid_short = str(item['targetid'])
            if len(tid_short) > 10:
                tid_short = tid_short[:5] + '..' + tid_short[-4:]

            ax.set_title(f'{tid_short}\nz={z:.3f} s={item["anomaly_score"]:.1f}',
                        fontsize=7, fontweight='bold')
            ax.tick_params(labelsize=6)
            ax.grid(True, alpha=0.15)

        # Hide empty subplots
        for i in range(n, nrows * ncols):
            row, col = divmod(i, ncols)
            axes[row, col].set_visible(False)

        suffix = f'_page{page+1}' if n_pages > 1 else ''
        stype_lower = spectype_filter.lower()

        fig.suptitle(f'Gold Anomalies: {spectype_filter} ({len(filtered)} objects){" - Page " + str(page+1) if n_pages > 1 else ""}',
                    fontsize=14, fontweight='bold', y=1.02)
        plt.tight_layout()

        out_path = os.path.join(GRID_DIR, f'gold_grid_{stype_lower}{suffix}.png')
        plt.savefig(out_path, dpi=150, bbox_inches='tight')
        plt.close()
        print(f'  Saved grid: {out_path}')


def main():
    # Load gold catalog
    gold = pd.read_csv(GOLD_CSV)
    print(f'Loaded {len(gold)} gold anomalies')
    print(f'Spectype distribution: {gold["spectype"].value_counts().to_dict()}')

    # Compute healpix pixels
    gold['pixel'] = gold.apply(
        lambda r: hp.ang2pix(64, r['target_ra'], r['target_dec'], lonlat=True, nest=True),
        axis=1
    )
    gold['group'] = gold['pixel'].apply(lambda p: str(p // 100))

    # Track results
    success_list = []
    failed_list = []
    skipped_list = []
    fits_cache = {}  # pixel -> (fits_path, survey, program)

    # Progress tracking
    total = len(gold)

    for idx, row in gold.iterrows():
        tid = int(row['targetid'])
        ra = row['target_ra']
        dec = row['target_dec']
        z = row['z']
        score = row['anomaly_score']
        spectype = row['spectype']
        pixel = int(row['pixel'])
        group = row['group']

        # Check if already plotted
        plot_name = f'spectrum_{tid}_z{z:.2f}.png'
        plot_path = os.path.join(OUTPUT_DIR, plot_name)

        print(f'[{idx+1}/{total}] TID={tid} z={z:.4f} {spectype} score={score:.2f} pixel={pixel}')

        # Try to find FITS file
        fits_path = None
        matched_survey = None
        matched_program = None

        # Check cache first
        if pixel in fits_cache:
            cached_path, cached_survey, cached_program = fits_cache[pixel]
            if os.path.exists(cached_path):
                fits_path = cached_path
                matched_survey = cached_survey
                matched_program = cached_program
                print(f'  Using cached FITS: {os.path.basename(cached_path)}')

        if fits_path is None:
            # Try each survey/program combination
            for survey, program in SURVEY_PROGRAMS:
                print(f'  Trying {survey}/{program}...', end='', flush=True)
                result = download_fits(pixel, group, survey, program, CACHE_DIR)
                if result:
                    fits_path = result
                    matched_survey = survey
                    matched_program = program
                    fits_cache[pixel] = (fits_path, survey, program)
                    print(f' OK ({os.path.getsize(result)/1e6:.1f} MB)')
                    break
                else:
                    print(' not found')
                time.sleep(0.5)  # Rate limit between attempts

        if fits_path is None:
            print(f'  FAILED: No FITS file found for pixel {pixel}')
            failed_list.append({
                'targetid': tid, 'z': z, 'spectype': spectype,
                'score': score, 'pixel': pixel, 'reason': 'no_fits'
            })
            continue

        # Extract spectrum
        spectrum = extract_spectrum(fits_path, tid)

        if spectrum is None:
            # Try with absolute value of targetid for negative ids
            if tid < 0:
                spectrum = extract_spectrum(fits_path, abs(tid))

            if spectrum is None:
                print(f'  FAILED: TARGETID {tid} not found in FITS')
                failed_list.append({
                    'targetid': tid, 'z': z, 'spectype': spectype,
                    'score': score, 'pixel': pixel, 'reason': 'targetid_not_in_fits',
                    'fits_file': os.path.basename(fits_path)
                })
                continue

        # Plot
        target_info = row.to_dict()
        success = plot_spectrum(spectrum, target_info, plot_path)

        if success:
            print(f'  Plotted: {plot_name}')
            success_list.append({
                'targetid': tid, 'z': z, 'spectype': spectype,
                'anomaly_score': score, 'spectrum': spectrum,
                'plot_path': plot_path
            })
        else:
            print(f'  FAILED: Empty spectrum')
            failed_list.append({
                'targetid': tid, 'z': z, 'spectype': spectype,
                'score': score, 'reason': 'empty_spectrum'
            })

        # Rate limit
        time.sleep(1.0)

    # Summary
    print(f'\n{"="*60}')
    print(f'DOWNLOAD SUMMARY')
    print(f'{"="*60}')
    print(f'Total gold anomalies: {total}')
    print(f'Successfully plotted:  {len(success_list)}')
    print(f'Failed:               {len(failed_list)}')
    print(f'Skipped (existing):   {len(skipped_list)}')

    if failed_list:
        print(f'\nFailed targets:')
        for f in failed_list:
            print(f'  TID={f["targetid"]} z={f["z"]:.4f} {f["spectype"]} - {f["reason"]}')

    # Create summary grids
    print(f'\nCreating summary grids...')
    for spectype in ['QSO', 'GALAXY', 'STAR']:
        create_summary_grid(gold, success_list, spectype, GRID_DIR)

    # Save results JSON
    results = {
        'total': total,
        'success': len(success_list),
        'failed': len(failed_list),
        'success_targets': [
            {'targetid': s['targetid'], 'z': s['z'], 'spectype': s['spectype'],
             'score': s['anomaly_score']}
            for s in success_list
        ],
        'failed_targets': failed_list,
    }

    results_path = os.path.join(GRID_DIR, 'download_results.json')
    with open(results_path, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    print(f'\nResults saved to {results_path}')


if __name__ == '__main__':
    main()
