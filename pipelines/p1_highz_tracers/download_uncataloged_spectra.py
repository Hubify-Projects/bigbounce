#!/usr/bin/env python3
"""
Download and characterize DESI spectra for top 50 uncataloged anomalies.

Steps:
1. Load silver cross-match results, filter to uncataloged (not in SIMBAD AND not in NED)
2. Sort by anomaly_score descending, take top 50
3. Compute HEALPix pixels for DESI file paths
4. Download coadd FITS files from DESI DR1
5. Extract individual spectra from FITS
6. Plot each spectrum with emission line markers
7. Create 5x10 grid summary plot
8. Auto-classify each spectrum and save results
"""

import json
import os
import sys
import time
import warnings
from pathlib import Path

import healpy as hp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
from astropy.io import fits
from scipy.ndimage import uniform_filter1d
from urllib.request import urlretrieve
from urllib.error import HTTPError, URLError

warnings.filterwarnings('ignore', category=RuntimeWarning)

# Paths
BASE = Path("/Users/houstongolden/Desktop/CODE_2026/bigbounce/pipelines/p1_highz_tracers")
CROSSMATCH = BASE / "outputs/silver_crossmatch/silver_crossmatch_results.json"
OUTDIR = BASE / "outputs/uncataloged_spectra"
CACHE = BASE / "outputs/fits_cache"
OUTDIR.mkdir(parents=True, exist_ok=True)
CACHE.mkdir(parents=True, exist_ok=True)

# Common emission/absorption lines (vacuum wavelengths in Angstroms)
LINES = {
    'Ly-alpha': 1215.67,
    'CIV': 1549.48,
    'CIII]': 1908.73,
    'MgII': 2799.12,
    '[OII]': 3727.09,
    'H-delta': 4102.89,
    'H-gamma': 4341.68,
    'H-beta': 4862.68,
    '[OIII]4959': 4960.30,
    '[OIII]5007': 5008.24,
    '[NII]6548': 6549.86,
    'H-alpha': 6564.61,
    '[NII]6583': 6585.27,
    '[SII]6717': 6718.29,
    '[SII]6731': 6732.67,
}

# DESI arm wavelength ranges (approx)
ARM_RANGES = {
    'B': (3600, 5800),
    'R': (5760, 7620),
    'Z': (7520, 9824),
}
ARM_COLORS = {'B': '#3366cc', 'R': '#cc3333', 'Z': '#666666'}


def load_uncataloged_top50():
    """Load cross-match results, filter uncataloged, return top 50 by score."""
    with open(CROSSMATCH) as f:
        data = json.load(f)

    uncataloged = [
        d for d in data
        if not d['simbad']['found'] and not d['ned']['found']
    ]
    uncataloged.sort(key=lambda x: x['anomaly_score'], reverse=True)
    top50 = uncataloged[:50]

    print(f"Total entries: {len(data)}")
    print(f"Uncataloged: {len(uncataloged)}")
    print(f"Top 50 score range: {top50[0]['anomaly_score']:.2f} - {top50[-1]['anomaly_score']:.2f}")
    return top50


def compute_healpix(ra, dec, nside=64):
    """Compute HEALPix pixel index (NESTED) from RA/DEC."""
    pixel = hp.ang2pix(nside, ra, dec, lonlat=True, nest=True)
    group = str(pixel // 100)
    return int(pixel), group


def download_fits(pixel, group, cache_dir):
    """Download DESI DR1 coadd FITS file, trying dark then bright survey."""
    for survey in ['dark', 'bright']:
        fname = f"coadd-main-{survey}-{pixel}.fits"
        cache_path = cache_dir / fname

        if cache_path.exists():
            print(f"  [cached] {fname}")
            return cache_path, survey

        url = (
            f"https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/"
            f"healpix/main/{survey}/{group}/{pixel}/{fname}"
        )

        try:
            print(f"  Downloading {fname} ...")
            urlretrieve(url, cache_path)
            print(f"  [downloaded] {fname} ({cache_path.stat().st_size / 1e6:.1f} MB)")
            return cache_path, survey
        except (HTTPError, URLError) as e:
            print(f"  [{survey}] HTTP error: {e}")
            if cache_path.exists():
                cache_path.unlink()
            continue

    return None, None


def extract_spectrum(fits_path, targetid):
    """Extract B/R/Z spectra for a specific TARGETID from coadd FITS."""
    spectra = {}

    with fits.open(fits_path) as hdul:
        # Find target index in FIBERMAP
        fibermap = hdul['FIBERMAP'].data
        target_mask = fibermap['TARGETID'] == targetid

        if not np.any(target_mask):
            print(f"  WARNING: TARGETID {targetid} not found in {fits_path}")
            return None

        idx = np.where(target_mask)[0][0]

        for arm in ['B', 'R', 'Z']:
            try:
                wave = hdul[f'{arm}_WAVELENGTH'].data
                flux = hdul[f'{arm}_FLUX'].data[idx]
                ivar = hdul[f'{arm}_IVAR'].data[idx]

                # Handle 1D vs 2D wavelength arrays
                if wave.ndim > 1:
                    wave = wave[idx]

                spectra[arm] = {
                    'wave': wave.astype(float),
                    'flux': flux.astype(float),
                    'ivar': ivar.astype(float),
                }
            except (KeyError, IndexError) as e:
                print(f"  WARNING: Arm {arm} not available: {e}")

    return spectra if spectra else None


def classify_spectrum(spectra, z, spectype, max_snr):
    """Auto-classify a spectrum based on features."""
    if not spectra:
        return "No spectrum extracted"

    # Combine all arms
    all_wave = np.concatenate([spectra[arm]['wave'] for arm in sorted(spectra.keys())])
    all_flux = np.concatenate([spectra[arm]['flux'] for arm in sorted(spectra.keys())])
    all_ivar = np.concatenate([spectra[arm]['ivar'] for arm in sorted(spectra.keys())])

    # Sort by wavelength
    order = np.argsort(all_wave)
    all_wave = all_wave[order]
    all_flux = all_flux[order]
    all_ivar = all_ivar[order]

    # Mask bad pixels
    good = np.isfinite(all_flux) & np.isfinite(all_ivar) & (all_ivar > 0)
    if good.sum() < 50:
        return f"Low-quality spectrum ({good.sum()} good pixels), {spectype} at z={z:.3f}"

    flux_good = all_flux[good]
    wave_good = all_wave[good]
    ivar_good = all_ivar[good]

    # Compute median SNR
    snr = np.median(np.abs(flux_good) * np.sqrt(ivar_good))

    # Check for emission lines at expected positions
    detected_lines = []
    for name, rest_wave in LINES.items():
        obs_wave = rest_wave * (1 + z)
        if obs_wave < wave_good.min() or obs_wave > wave_good.max():
            continue

        # Check for emission in a window around the line
        window = np.abs(wave_good - obs_wave) < 10  # 10 Angstrom window
        if window.sum() < 3:
            continue

        line_flux = np.median(flux_good[window])

        # Compare to local continuum
        cont_window = (np.abs(wave_good - obs_wave) > 20) & (np.abs(wave_good - obs_wave) < 60)
        if cont_window.sum() < 5:
            continue
        cont_flux = np.median(flux_good[cont_window])

        if cont_flux > 0 and line_flux > 1.5 * cont_flux:
            detected_lines.append(name)
        elif cont_flux > 0 and line_flux < 0.5 * cont_flux:
            detected_lines.append(f"{name}(abs)")

    # Check for broad features (BAL)
    smooth = uniform_filter1d(flux_good, size=50)
    residual = flux_good - smooth
    rms = np.std(residual)

    # Check continuum slope
    if len(wave_good) > 100:
        p = np.polyfit(wave_good, flux_good, 1)
        slope = p[0]
    else:
        slope = 0

    # Build classification
    if spectype == 'STAR':
        if z < 0.001:
            return f"Stellar spectrum (v={z*3e5:.0f} km/s), SNR={snr:.1f}"
        else:
            return f"Misclassified star? z={z:.4f}, SNR={snr:.1f}"

    if spectype == 'QSO':
        broad_lines = [l for l in detected_lines if 'abs' not in l]
        abs_lines = [l for l in detected_lines if 'abs' in l]

        if abs_lines and broad_lines:
            return f"BAL QSO candidate at z={z:.3f}, emission: {', '.join(broad_lines)}, absorption: {', '.join(abs_lines)}"
        elif broad_lines:
            return f"QSO at z={z:.3f} with {', '.join(broad_lines)}"
        elif snr < 2:
            return f"Low-SNR QSO at z={z:.3f}, featureless continuum"
        else:
            return f"QSO at z={z:.3f}, no strong lines detected, SNR={snr:.1f}"

    if spectype == 'GALAXY':
        emission = [l for l in detected_lines if 'abs' not in l]
        absorption = [l for l in detected_lines if 'abs' in l]

        if '[OIII]5007' in emission or '[OIII]4959' in emission:
            if 'H-beta' in emission:
                return f"Strong emission-line galaxy at z={z:.3f} with [OIII]+H-beta"
            return f"Strong [OIII] emission galaxy at z={z:.3f}"

        if 'H-alpha' in emission:
            if '[NII]6583' in emission:
                return f"Star-forming galaxy at z={z:.3f} with H-alpha+[NII]"
            return f"H-alpha emission galaxy at z={z:.3f}"

        if '[OII]' in emission:
            return f"[OII] emission galaxy at z={z:.3f}"

        if emission:
            return f"Emission-line galaxy at z={z:.3f} with {', '.join(emission)}"

        if absorption:
            return f"Absorption-line galaxy at z={z:.3f} with {', '.join(absorption)}"

        if snr < 1.5:
            return f"Low-SNR galaxy at z={z:.3f}, likely faint continuum"

        return f"Galaxy at z={z:.3f}, weak/no detected features, SNR={snr:.1f}"

    return f"{spectype} at z={z:.3f}, SNR={snr:.1f}"


def plot_spectrum(spectra, obj, classification, save_path):
    """Plot a single spectrum with B/R/Z arms, smoothed overlay, and line markers."""
    fig, ax = plt.subplots(figsize=(12, 4.5))

    z = obj['z']

    all_fluxes = []
    for arm in ['B', 'R', 'Z']:
        if arm not in spectra:
            continue
        wave = spectra[arm]['wave']
        flux = spectra[arm]['flux']
        ivar = spectra[arm]['ivar']

        # Mask bad pixels
        good = np.isfinite(flux) & np.isfinite(ivar) & (ivar > 0)
        if good.sum() < 5:
            continue

        ax.plot(wave[good], flux[good], color=ARM_COLORS[arm], alpha=0.4, linewidth=0.5, label=f'{arm}-arm')

        # Smoothed overlay
        if good.sum() > 20:
            smooth_flux = uniform_filter1d(flux[good], size=15)
            ax.plot(wave[good], smooth_flux, color=ARM_COLORS[arm], alpha=0.9, linewidth=1.5)

        all_fluxes.extend(flux[good])

    if not all_fluxes:
        plt.close()
        return

    # Set y limits robustly
    flux_arr = np.array(all_fluxes)
    flux_finite = flux_arr[np.isfinite(flux_arr)]
    if len(flux_finite) > 0:
        p5, p95 = np.percentile(flux_finite, [2, 98])
        margin = max(0.3 * (p95 - p5), 0.1)
        ax.set_ylim(p5 - margin, p95 + margin)

    # Mark emission lines at observed wavelengths
    ymin, ymax = ax.get_ylim()
    line_y = ymax - 0.08 * (ymax - ymin)
    for name, rest_wave in LINES.items():
        obs_wave = rest_wave * (1 + z)
        if 3500 < obs_wave < 10000:
            ax.axvline(obs_wave, color='green', alpha=0.3, linewidth=0.8, linestyle='--')
            ax.text(obs_wave, line_y, name, fontsize=5, rotation=90,
                    ha='right', va='top', color='green', alpha=0.7)

    # Zero line
    ax.axhline(0, color='gray', linewidth=0.5, alpha=0.5)

    tid = obj['targetid']
    score = obj['anomaly_score']
    spectype = obj['spectype']
    ax.set_title(
        f"TARGETID {tid}  |  z={z:.4f}  |  score={score:.2f}  |  {spectype}  |  UNCATALOGED",
        fontsize=10, fontweight='bold'
    )
    ax.set_xlabel('Wavelength (A)', fontsize=9)
    ax.set_ylabel('Flux (10$^{-17}$ erg/s/cm$^2$/A)', fontsize=9)
    ax.legend(fontsize=7, loc='upper right')
    ax.tick_params(labelsize=8)

    # Add classification text
    ax.text(0.02, 0.95, classification, transform=ax.transAxes, fontsize=7,
            verticalalignment='top', style='italic',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    fig.tight_layout()
    fig.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close(fig)


def plot_spectrum_mini(ax, spectra, obj, classification):
    """Plot a mini spectrum for the grid."""
    z = obj['z']

    for arm in ['B', 'R', 'Z']:
        if arm not in spectra:
            continue
        wave = spectra[arm]['wave']
        flux = spectra[arm]['flux']
        ivar = spectra[arm]['ivar']

        good = np.isfinite(flux) & np.isfinite(ivar) & (ivar > 0)
        if good.sum() < 5:
            continue

        if good.sum() > 20:
            smooth_flux = uniform_filter1d(flux[good], size=15)
            ax.plot(wave[good], smooth_flux, color=ARM_COLORS[arm], linewidth=0.7)
        else:
            ax.plot(wave[good], flux[good], color=ARM_COLORS[arm], linewidth=0.5)

    # Mark key lines
    for name, rest_wave in [('[OIII]', 5008.24), ('H-alpha', 6564.61), ('Ly-a', 1215.67), ('[OII]', 3727.09)]:
        obs_wave = rest_wave * (1 + z)
        if 3500 < obs_wave < 10000:
            ax.axvline(obs_wave, color='green', alpha=0.25, linewidth=0.5, linestyle='--')

    ax.axhline(0, color='gray', linewidth=0.3, alpha=0.4)

    # Set y-limits
    all_flux = []
    for arm in ['B', 'R', 'Z']:
        if arm in spectra:
            good = np.isfinite(spectra[arm]['flux']) & (spectra[arm]['ivar'] > 0)
            all_flux.extend(spectra[arm]['flux'][good])
    if all_flux:
        fa = np.array(all_flux)
        fa = fa[np.isfinite(fa)]
        if len(fa) > 0:
            p5, p95 = np.percentile(fa, [3, 97])
            m = max(0.3 * (p95 - p5), 0.1)
            ax.set_ylim(p5 - m, p95 + m)

    score = obj['anomaly_score']
    tid = obj['targetid']
    # Use short classification
    short_class = classification[:50] + '...' if len(classification) > 50 else classification
    ax.set_title(f"TID ...{str(tid)[-6:]} z={z:.3f} s={score:.1f}", fontsize=5, pad=2)
    ax.text(0.02, 0.92, short_class, transform=ax.transAxes, fontsize=3.5,
            va='top', style='italic', color='#333')
    ax.tick_params(labelsize=4)
    ax.set_xticks([])
    ax.set_yticks([])


def main():
    print("=" * 70)
    print("DESI DR1 Spectra Download for Top 50 Uncataloged Anomalies")
    print("=" * 70)

    # Step 1-2: Load and filter
    print("\n[Step 1-2] Loading cross-match results...")
    top50 = load_uncataloged_top50()

    # Step 3: Compute HEALPix pixels
    print("\n[Step 3] Computing HEALPix pixels...")
    for obj in top50:
        pixel, group = compute_healpix(obj['target_ra'], obj['target_dec'])
        obj['healpix_pixel'] = pixel
        obj['healpix_group'] = group

    # Deduplicate FITS files needed
    unique_pixels = {}
    for obj in top50:
        p = obj['healpix_pixel']
        if p not in unique_pixels:
            unique_pixels[p] = {'group': obj['healpix_group'], 'targets': []}
        unique_pixels[p]['targets'].append(obj['targetid'])

    print(f"Need {len(unique_pixels)} unique FITS files for {len(top50)} targets")

    # Step 4: Download FITS files
    print("\n[Step 4] Downloading DESI DR1 coadd FITS files...")
    fits_paths = {}
    download_count = 0
    for i, (pixel, info) in enumerate(unique_pixels.items()):
        print(f"\n  [{i+1}/{len(unique_pixels)}] Pixel {pixel} (group {info['group']}, {len(info['targets'])} targets)")

        fpath, survey = download_fits(pixel, info['group'], CACHE)
        if fpath:
            fits_paths[pixel] = (fpath, survey)
            download_count += 1
        else:
            print(f"  FAILED to download pixel {pixel}")

        # Rate limit: 1 second between downloads
        time.sleep(1.0)

    print(f"\n  Downloaded/cached: {download_count}/{len(unique_pixels)} FITS files")

    # Step 5-6: Extract and plot spectra
    print("\n[Step 5-6] Extracting spectra and creating plots...")
    results = []
    all_spectra = {}

    for i, obj in enumerate(top50):
        tid = obj['targetid']
        pixel = obj['healpix_pixel']

        print(f"\n  [{i+1}/50] TARGETID {tid} (pixel {pixel})")

        if pixel not in fits_paths:
            print(f"  SKIPPED: No FITS file for pixel {pixel}")
            classification = "No FITS file available for this HEALPix pixel"
            results.append({
                'rank': i + 1,
                'targetid': tid,
                'ra': obj['target_ra'],
                'dec': obj['target_dec'],
                'z': obj['z'],
                'anomaly_score': obj['anomaly_score'],
                'spectype': obj['spectype'],
                'zwarn': obj.get('zwarn', 0),
                'max_snr': obj.get('max_snr', 0),
                'healpix_pixel': pixel,
                'classification': classification,
                'spectrum_extracted': False,
            })
            continue

        fpath, survey = fits_paths[pixel]
        spectra = extract_spectrum(fpath, tid)

        if spectra is None:
            print(f"  SKIPPED: Target not found in FITS")
            classification = f"Target not found in coadd-main-{survey}-{pixel}.fits"
            results.append({
                'rank': i + 1,
                'targetid': tid,
                'ra': obj['target_ra'],
                'dec': obj['target_dec'],
                'z': obj['z'],
                'anomaly_score': obj['anomaly_score'],
                'spectype': obj['spectype'],
                'zwarn': obj.get('zwarn', 0),
                'max_snr': obj.get('max_snr', 0),
                'healpix_pixel': pixel,
                'classification': classification,
                'spectrum_extracted': False,
            })
            continue

        # Classify
        classification = classify_spectrum(
            spectra, obj['z'], obj['spectype'], obj.get('max_snr', 0)
        )
        print(f"  Classification: {classification}")

        # Plot individual
        plot_path = OUTDIR / f"spectrum_{i+1:02d}_tid{tid}.png"
        plot_spectrum(spectra, obj, classification, plot_path)
        print(f"  Saved: {plot_path.name}")

        all_spectra[i] = (spectra, obj, classification)

        results.append({
            'rank': i + 1,
            'targetid': tid,
            'ra': obj['target_ra'],
            'dec': obj['target_dec'],
            'z': obj['z'],
            'anomaly_score': obj['anomaly_score'],
            'spectype': obj['spectype'],
            'zwarn': obj.get('zwarn', 0),
            'max_snr': obj.get('max_snr', 0),
            'healpix_pixel': pixel,
            'survey': survey,
            'classification': classification,
            'spectrum_extracted': True,
        })

    # Step 7: Create 5x10 grid
    print("\n[Step 7] Creating 5x10 grid plot...")
    fig = plt.figure(figsize=(30, 24))
    gs = gridspec.GridSpec(10, 5, figure=fig, hspace=0.4, wspace=0.2)

    for i in range(50):
        row = i // 5
        col = i % 5
        ax = fig.add_subplot(gs[row, col])

        if i in all_spectra:
            spectra, obj, classification = all_spectra[i]
            plot_spectrum_mini(ax, spectra, obj, classification)
        else:
            ax.text(0.5, 0.5, f"#{i+1}\nNo spectrum",
                    ha='center', va='center', fontsize=6, color='gray',
                    transform=ax.transAxes)
            ax.set_xticks([])
            ax.set_yticks([])

    fig.suptitle(
        "Top 50 Uncataloged DESI DR1 Anomalies (Sorted by Anomaly Score)",
        fontsize=16, fontweight='bold', y=0.995
    )

    grid_path = OUTDIR / "uncataloged_top50_grid.png"
    fig.savefig(grid_path, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"  Saved: {grid_path}")

    # Step 8: Save classifications
    print("\n[Step 8] Saving classifications...")
    class_path = OUTDIR / "uncataloged_top50_classifications.json"

    # Summary stats
    extracted = sum(1 for r in results if r['spectrum_extracted'])
    spectypes = {}
    for r in results:
        st = r['spectype']
        spectypes[st] = spectypes.get(st, 0) + 1

    output = {
        'metadata': {
            'description': 'Top 50 uncataloged DESI DR1 anomalies by anomaly score',
            'source': 'silver_crossmatch_results.json',
            'criteria': 'simbad_found=false AND ned_found=false',
            'n_total_uncataloged': 1127,
            'n_selected': 50,
            'n_spectra_extracted': extracted,
            'score_range': [
                round(top50[0]['anomaly_score'], 3),
                round(top50[-1]['anomaly_score'], 3),
            ],
            'spectype_distribution': spectypes,
            'generated': time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime()),
        },
        'classifications': results,
    }

    with open(class_path, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"  Saved: {class_path}")

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"  Spectra extracted: {extracted}/50")
    print(f"  FITS files downloaded/cached: {download_count}")
    print(f"  Spectype distribution: {spectypes}")
    print(f"  Individual plots: {OUTDIR}")
    print(f"  Grid plot: {grid_path}")
    print(f"  Classifications: {class_path}")

    # Print classification summary
    print("\n  Classification summary:")
    for r in results:
        status = "OK" if r['spectrum_extracted'] else "MISS"
        print(f"    #{r['rank']:2d} [{status}] {r['classification']}")

    # Cleanup note
    cache_size = sum(f.stat().st_size for f in CACHE.iterdir() if f.is_file()) / 1e6
    print(f"\n  FITS cache size: {cache_size:.1f} MB in {CACHE}")
    print("  To clean up: rm -rf", CACHE)


if __name__ == '__main__':
    main()
