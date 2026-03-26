#!/usr/bin/env python3
"""
Download and Plot DESI DR1 Spectra for Top 50 Anomalies

Fetches actual coadd FITS files from the DESI public data release,
extracts the spectrum for each anomalous TARGETID, and produces:
  1. Individual spectrum plots for the top 50 anomalies
  2. A 2x5 mosaic of the top 10 most anomalous spectra

DESI DR1 coadd files are organized by HEALPix (nside=64, nested):
  https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/healpix/
    {survey}/{program}/{group}/{pixel}/coadd-{survey}-{program}-{pixel}.fits

Each coadd FITS contains:
  FIBERMAP  — table with TARGETID, TARGET_RA, TARGET_DEC, etc.
  B_FLUX    — blue-arm flux array  (nspec x 2751), wavelength ~3600-5800 A
  R_FLUX    — red-arm flux array   (nspec x 2326), wavelength ~5760-7620 A
  Z_FLUX    — NIR-arm flux array   (nspec x 2881), wavelength ~7520-9824 A
  B_WAVELENGTH, R_WAVELENGTH, Z_WAVELENGTH — 1D wavelength grids (Angstroms)
  B_IVAR, R_IVAR, Z_IVAR — inverse-variance arrays

Usage:
  python download_and_plot_spectra.py [--top N] [--skip-download]
"""

import json
import os
import sys
import time
import tempfile
import shutil
from pathlib import Path
from collections import defaultdict

import numpy as np
import healpy as hp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from astropy.io import fits
import requests

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
ANOMALY_FILE = BASE_DIR / "outputs" / "desi_dr1" / "dr1_all_anomalies.json"
SPECTRA_DIR = BASE_DIR / "outputs" / "desi_dr1" / "spectra"
MOSAIC_DIR = BASE_DIR.parent.parent / "public" / "images"
CACHE_DIR = BASE_DIR / "outputs" / "desi_dr1" / "fits_cache"

DESI_BASE = "https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/healpix"
NSIDE = 64

# Survey/program combinations to try (in order of priority)
# Negative TARGETIDs are almost always in 'bright' program, so try that first
SURVEY_PROGRAMS_BRIGHT_FIRST = [
    ("main", "bright"),
    ("main", "dark"),
    ("sv3", "bright"),
    ("sv3", "dark"),
    ("sv1", "bright"),
    ("sv1", "dark"),
]
SURVEY_PROGRAMS_DARK_FIRST = [
    ("main", "dark"),
    ("main", "bright"),
    ("sv3", "dark"),
    ("sv3", "bright"),
    ("sv1", "dark"),
    ("sv1", "bright"),
]


def load_anomalies(top_n=50):
    """Load anomaly catalog and return top N sorted by score."""
    with open(ANOMALY_FILE) as f:
        data = json.load(f)
    # Already sorted by score descending
    return data[:top_n]


def compute_healpix(ra, dec):
    """Compute HEALPix pixel and group for given RA/Dec."""
    pixel = hp.ang2pix(NSIDE, ra, dec, lonlat=True, nest=True)
    group = pixel // 100
    return int(pixel), int(group)


def build_download_plan(anomalies):
    """Group anomalies by (survey, program, pixel) for efficient downloading.

    Returns dict: pixel -> list of anomaly dicts (with 'pixel' and 'group' added).
    """
    pixel_map = defaultdict(list)
    for a in anomalies:
        pixel, group = compute_healpix(a['ra'], a['dec'])
        entry = dict(a, pixel=pixel, group=group)
        pixel_map[pixel].append(entry)
    return pixel_map


def download_coadd(pixel, group, cache_dir):
    """Try to download the coadd FITS file for the given pixel.

    Tries multiple survey/program combinations.
    Returns (filepath, survey, program) or (None, None, None).
    """
    cache_dir = Path(cache_dir)
    cache_dir.mkdir(parents=True, exist_ok=True)

    for survey, program in SURVEY_PROGRAMS:
        fname = f"coadd-{survey}-{program}-{pixel}.fits"
        cached = cache_dir / fname
        if cached.exists():
            print(f"    [cache hit] {fname}")
            return str(cached), survey, program

        url = f"{DESI_BASE}/{survey}/{program}/{group}/{pixel}/{fname}"
        print(f"    Trying {url} ...", end=" ", flush=True)
        try:
            resp = requests.get(url, timeout=120, stream=True)
            if resp.status_code == 200:
                # Stream to disk
                tmp = cached.with_suffix('.tmp')
                with open(tmp, 'wb') as f:
                    for chunk in resp.iter_content(chunk_size=1 << 20):
                        f.write(chunk)
                tmp.rename(cached)
                size_mb = cached.stat().st_size / 1e6
                print(f"OK ({size_mb:.1f} MB)")
                return str(cached), survey, program
            else:
                print(f"HTTP {resp.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"FAIL ({e})")

    return None, None, None


def extract_spectrum(fits_path, target_id):
    """Extract B/R/Z flux and wavelength for a given TARGETID from a coadd file.

    Returns dict with keys: wave_b, wave_r, wave_z, flux_b, flux_r, flux_z,
                            ivar_b, ivar_r, ivar_z, idx, z_best, spectype
    or None if TARGETID not found.
    """
    with fits.open(fits_path) as hdul:
        # List available HDUs for debugging
        hdu_names = [h.name for h in hdul]

        # Find TARGETID in FIBERMAP
        fibermap = hdul['FIBERMAP'].data
        tids = fibermap['TARGETID']
        mask = tids == target_id

        if not np.any(mask):
            return None

        idx = np.where(mask)[0][0]

        result = {
            'idx': int(idx),
            'target_id': int(target_id),
        }

        # Try to get redshift info
        if 'REDSHIFTS' in hdu_names:
            rz = hdul['REDSHIFTS'].data
            if len(rz) > idx:
                result['z_best'] = float(rz['Z'][idx]) if 'Z' in rz.dtype.names else None
                result['spectype'] = rz['SPECTYPE'][idx].strip() if 'SPECTYPE' in rz.dtype.names else None
                result['deltachi2'] = float(rz['DELTACHI2'][idx]) if 'DELTACHI2' in rz.dtype.names else None

        # Extract wavelengths (1D arrays)
        for arm in ['B', 'R', 'Z']:
            wkey = f'{arm}_WAVELENGTH'
            fkey = f'{arm}_FLUX'
            ikey = f'{arm}_IVAR'

            if wkey in hdu_names and fkey in hdu_names:
                result[f'wave_{arm.lower()}'] = hdul[wkey].data.copy()
                result[f'flux_{arm.lower()}'] = hdul[fkey].data[idx].copy()
                if ikey in hdu_names:
                    result[f'ivar_{arm.lower()}'] = hdul[ikey].data[idx].copy()

        return result


def smooth_spectrum(flux, window=7):
    """Simple boxcar smoothing for cleaner plots."""
    kernel = np.ones(window) / window
    return np.convolve(flux, kernel, mode='same')


def plot_single_spectrum(spec, anomaly, outpath, rank):
    """Plot a single spectrum with B/R/Z arms color-coded."""
    fig, ax = plt.subplots(figsize=(12, 4.5), dpi=150)

    # Arm colors
    arm_styles = {
        'b': {'color': '#3366cc', 'label': 'B arm (3600-5800 A)', 'alpha': 0.25},
        'r': {'color': '#33aa55', 'label': 'R arm (5760-7620 A)', 'alpha': 0.25},
        'z': {'color': '#cc3333', 'label': 'Z arm (7520-9824 A)', 'alpha': 0.25},
    }
    smooth_colors = {
        'b': '#1a3d7a',
        'r': '#1a6633',
        'z': '#7a1a1a',
    }

    ymin, ymax = np.inf, -np.inf

    for arm in ['b', 'r', 'z']:
        wkey = f'wave_{arm}'
        fkey = f'flux_{arm}'
        if wkey in spec and fkey in spec:
            wave = spec[wkey]
            flux = spec[fkey]

            # Mask bad pixels
            good = np.isfinite(flux) & (flux != 0)
            if np.sum(good) < 10:
                continue

            # Plot raw (faint)
            ax.plot(wave, flux,
                    color=arm_styles[arm]['color'],
                    alpha=arm_styles[arm]['alpha'],
                    linewidth=0.5)

            # Plot smoothed (bold)
            flux_smooth = smooth_spectrum(flux, window=11)
            ax.plot(wave, flux_smooth,
                    color=smooth_colors[arm],
                    linewidth=1.2,
                    label=arm_styles[arm]['label'])

            # Track y range from smoothed data
            valid = np.isfinite(flux_smooth) & good
            if np.sum(valid) > 0:
                p1, p99 = np.percentile(flux_smooth[valid], [1, 99])
                ymin = min(ymin, p1)
                ymax = max(ymax, p99)

    # Y-axis limits with padding
    if np.isfinite(ymin) and np.isfinite(ymax):
        margin = (ymax - ymin) * 0.15
        ax.set_ylim(ymin - margin, ymax + margin)

    ax.set_xlabel('Wavelength (Angstroms)', fontsize=11)
    ax.set_ylabel('Flux (10$^{-17}$ erg/s/cm$^2$/A)', fontsize=11)

    # Title with metadata
    tid = anomaly['tid']
    score = anomaly['score']
    worst = anomaly['worst']
    z_str = ""
    if spec.get('z_best') is not None:
        z_str = f"  z={spec['z_best']:.4f}"
    type_str = ""
    if spec.get('spectype'):
        type_str = f"  [{spec['spectype']}]"

    ax.set_title(
        f"Rank #{rank}  |  TARGETID {tid}  |  Anomaly Score {score:.2f}  |  "
        f"Worst Arm: {worst}{z_str}{type_str}",
        fontsize=10, fontweight='bold', pad=10
    )

    # Per-arm residual annotations
    res_text = f"rB={anomaly['rB']:.2f}  rR={anomaly['rR']:.2f}  rZ={anomaly['rZ']:.2f}"
    ax.text(0.98, 0.96, res_text, transform=ax.transAxes,
            fontsize=8, ha='right', va='top',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', alpha=0.8))

    # RA/Dec
    coord_text = f"RA={anomaly['ra']:.5f}  Dec={anomaly['dec']:.5f}"
    ax.text(0.02, 0.96, coord_text, transform=ax.transAxes,
            fontsize=8, ha='left', va='top',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='lightcyan', alpha=0.8))

    ax.legend(loc='lower right', fontsize=8, framealpha=0.8)
    ax.grid(True, alpha=0.2)

    fig.tight_layout()
    fig.savefig(outpath, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"    Saved: {outpath}")


def create_mosaic(spectra_data, anomalies, outpath, n=10):
    """Create a 2x5 mosaic of the top N anomalous spectra."""
    nrows, ncols = 2, 5
    fig = plt.figure(figsize=(24, 10), dpi=200)
    gs = GridSpec(nrows, ncols, hspace=0.35, wspace=0.25,
                  left=0.04, right=0.98, top=0.93, bottom=0.06)

    smooth_colors = {
        'b': '#1a3d7a',
        'r': '#1a6633',
        'z': '#7a1a1a',
    }
    raw_colors = {
        'b': '#3366cc',
        'r': '#33aa55',
        'z': '#cc3333',
    }

    plotted = 0
    for i in range(min(n, len(spectra_data))):
        if plotted >= nrows * ncols:
            break

        spec = spectra_data[i]
        anom = anomalies[i]

        if spec is None:
            continue

        row = plotted // ncols
        col = plotted % ncols
        ax = fig.add_subplot(gs[row, col])

        ymin, ymax = np.inf, -np.inf

        for arm in ['b', 'r', 'z']:
            wkey = f'wave_{arm}'
            fkey = f'flux_{arm}'
            if wkey in spec and fkey in spec:
                wave = spec[wkey]
                flux = spec[fkey]
                good = np.isfinite(flux) & (flux != 0)
                if np.sum(good) < 10:
                    continue

                # Raw faint
                ax.plot(wave, flux, color=raw_colors[arm], alpha=0.2, linewidth=0.3)
                # Smoothed
                flux_s = smooth_spectrum(flux, window=15)
                ax.plot(wave, flux_s, color=smooth_colors[arm], linewidth=1.0)

                valid = np.isfinite(flux_s) & good
                if np.sum(valid) > 0:
                    p1, p99 = np.percentile(flux_s[valid], [1, 99])
                    ymin = min(ymin, p1)
                    ymax = max(ymax, p99)

        if np.isfinite(ymin) and np.isfinite(ymax):
            margin = (ymax - ymin) * 0.2
            ax.set_ylim(ymin - margin, ymax + margin)

        # Compact title
        z_str = f"z={spec['z_best']:.3f}" if spec.get('z_best') is not None else ""
        type_str = spec.get('spectype', '')
        title = f"#{plotted+1}  Score={anom['score']:.1f}  {z_str}"
        if type_str:
            title += f"  [{type_str}]"
        ax.set_title(title, fontsize=8, fontweight='bold', pad=4)

        ax.tick_params(labelsize=7)
        if row == nrows - 1:
            ax.set_xlabel('Wavelength (A)', fontsize=8)
        if col == 0:
            ax.set_ylabel('Flux', fontsize=8)

        ax.grid(True, alpha=0.15)
        plotted += 1

    fig.suptitle(
        "Top 10 Spectral Anomalies from DESI DR1  |  BigBounce Autoencoder Pipeline",
        fontsize=14, fontweight='bold', y=0.98
    )

    fig.savefig(outpath, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f"\nMosaic saved: {outpath}")


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Download and plot DESI DR1 anomaly spectra")
    parser.add_argument('--top', type=int, default=50, help='Number of top anomalies to process')
    parser.add_argument('--skip-download', action='store_true', help='Use cached FITS only')
    parser.add_argument('--mosaic-only', action='store_true', help='Only regenerate mosaic from cached data')
    parser.add_argument('--cache-dir', type=str, default=str(CACHE_DIR), help='FITS cache directory')
    args = parser.parse_args()

    print("=" * 70)
    print("  DESI DR1 Anomaly Spectrum Downloader & Plotter")
    print("=" * 70)

    # Create output directories
    SPECTRA_DIR.mkdir(parents=True, exist_ok=True)
    MOSAIC_DIR.mkdir(parents=True, exist_ok=True)
    Path(args.cache_dir).mkdir(parents=True, exist_ok=True)

    # Load anomalies
    print(f"\nLoading anomaly catalog: {ANOMALY_FILE}")
    anomalies = load_anomalies(args.top)
    print(f"  Top {len(anomalies)} anomalies loaded (scores {anomalies[0]['score']:.2f} - {anomalies[-1]['score']:.2f})")

    # Build download plan
    pixel_map = build_download_plan(anomalies)
    print(f"  Unique HEALPix pixels needed: {len(pixel_map)}")

    # Track results
    spectra_results = [None] * len(anomalies)
    success_count = 0
    fail_count = 0
    not_found_count = 0

    # Download and extract
    print(f"\n{'='*70}")
    print("  Phase 1: Download FITS + Extract Spectra")
    print(f"{'='*70}\n")

    # Create a lookup: tid -> index in anomalies list
    tid_to_idx = {a['tid']: i for i, a in enumerate(anomalies)}

    processed_pixels = 0
    total_pixels = len(pixel_map)

    for pixel, pixel_anomalies in sorted(pixel_map.items()):
        processed_pixels += 1
        group = pixel_anomalies[0]['group']
        tids_in_pixel = [a['tid'] for a in pixel_anomalies]
        remaining_tids = set(tids_in_pixel)

        print(f"\n[{processed_pixels}/{total_pixels}] Pixel {pixel} (group {group}) — "
              f"{len(tids_in_pixel)} targets: {tids_in_pixel}")

        # Choose survey/program order based on TID sign
        # Negative TIDs are almost always in 'bright'
        all_negative = all(t < 0 for t in tids_in_pixel)
        sp_order = SURVEY_PROGRAMS_BRIGHT_FIRST if all_negative else SURVEY_PROGRAMS_DARK_FIRST

        # Try ALL survey/program combos for this pixel until all TIDs found
        for survey, program in sp_order:
            if not remaining_tids:
                break

            fname = f"coadd-{survey}-{program}-{pixel}.fits"
            cached = Path(args.cache_dir) / fname

            if args.skip_download and not cached.exists():
                continue

            if cached.exists():
                fpath = str(cached)
                print(f"    [cache] {fname}")
            else:
                url = f"{DESI_BASE}/{survey}/{program}/{group}/{pixel}/{fname}"
                print(f"    Trying {url} ...", end=" ", flush=True)
                try:
                    resp = requests.get(url, timeout=120, stream=True)
                    if resp.status_code == 200:
                        tmp = cached.with_suffix('.tmp')
                        with open(tmp, 'wb') as f:
                            for chunk in resp.iter_content(chunk_size=1 << 20):
                                f.write(chunk)
                        tmp.rename(cached)
                        size_mb = cached.stat().st_size / 1e6
                        print(f"OK ({size_mb:.1f} MB)")
                        fpath = str(cached)
                    else:
                        print(f"HTTP {resp.status_code}")
                        continue
                except requests.exceptions.RequestException as e:
                    print(f"FAIL ({e})")
                    continue

            # Try extracting all remaining TIDs from this file
            for pa in pixel_anomalies:
                tid = pa['tid']
                if tid not in remaining_tids:
                    continue
                idx_in_list = tid_to_idx[tid]
                print(f"    Extracting TARGETID {tid} from {survey}/{program} ...", end=" ")
                spec = extract_spectrum(fpath, tid)
                if spec is None:
                    print("not in this file")
                    continue

                spectra_results[idx_in_list] = spec
                success_count += 1
                remaining_tids.discard(tid)
                z_str = f"z={spec['z_best']:.4f}" if spec.get('z_best') is not None else "z=?"
                t_str = spec.get('spectype', '?')
                print(f"OK ({z_str}, {t_str})")

            # Brief pause to be nice to the server
            if not args.skip_download:
                time.sleep(0.5)

        # Count remaining TIDs as not found
        if remaining_tids:
            not_found_count += len(remaining_tids)
            for tid in remaining_tids:
                print(f"    TARGETID {tid}: NOT FOUND in any survey/program")

    print(f"\n{'='*70}")
    print(f"  Phase 1 Summary:")
    print(f"    Spectra extracted: {success_count}")
    print(f"    Download failures: {fail_count}")
    print(f"    TARGETID not found: {not_found_count}")
    print(f"{'='*70}")

    if success_count == 0:
        print("\nNo spectra extracted. Exiting.")
        sys.exit(1)

    # Phase 2: Plot individual spectra
    print(f"\n{'='*70}")
    print("  Phase 2: Plot Individual Spectra")
    print(f"{'='*70}\n")

    for i, (spec, anom) in enumerate(zip(spectra_results, anomalies)):
        if spec is None:
            continue
        rank = i + 1
        outname = f"rank{rank:03d}_tid{anom['tid']}_score{anom['score']:.1f}.png"
        outpath = SPECTRA_DIR / outname
        plot_single_spectrum(spec, anom, outpath, rank)

    # Phase 3: Mosaic of top 10
    print(f"\n{'='*70}")
    print("  Phase 3: Top 10 Mosaic")
    print(f"{'='*70}\n")

    # Collect spectra in rank order (only those successfully extracted)
    mosaic_specs = []
    mosaic_anoms = []
    for i, (spec, anom) in enumerate(zip(spectra_results, anomalies)):
        if spec is not None:
            mosaic_specs.append(spec)
            mosaic_anoms.append(anom)
        if len(mosaic_specs) >= 10:
            break

    if len(mosaic_specs) > 0:
        mosaic_path = MOSAIC_DIR / "top10_anomaly_spectra.png"
        create_mosaic(mosaic_specs, mosaic_anoms, mosaic_path, n=10)
    else:
        print("No spectra available for mosaic.")

    # Summary report
    print(f"\n{'='*70}")
    print("  FINAL SUMMARY")
    print(f"{'='*70}")
    print(f"  Anomalies requested: {len(anomalies)}")
    print(f"  Spectra downloaded:  {success_count}")
    print(f"  Download failures:   {fail_count}")
    print(f"  TID not found:       {not_found_count}")
    print(f"  Individual plots:    {SPECTRA_DIR}/")
    if len(mosaic_specs) > 0:
        print(f"  Mosaic (top 10):     {MOSAIC_DIR / 'top10_anomaly_spectra.png'}")
    print(f"  FITS cache:          {args.cache_dir}")
    print(f"{'='*70}")

    # Save extraction metadata
    meta = []
    for i, (spec, anom) in enumerate(zip(spectra_results, anomalies)):
        entry = {
            'rank': i + 1,
            'tid': anom['tid'],
            'ra': anom['ra'],
            'dec': anom['dec'],
            'score': anom['score'],
            'worst_arm': anom['worst'],
            'extracted': spec is not None,
        }
        if spec is not None:
            entry['z_best'] = spec.get('z_best')
            entry['spectype'] = spec.get('spectype')
            entry['deltachi2'] = spec.get('deltachi2')
        meta.append(entry)

    meta_path = SPECTRA_DIR / "extraction_metadata.json"
    with open(meta_path, 'w') as f:
        json.dump(meta, f, indent=2)
    print(f"\n  Metadata saved: {meta_path}")


if __name__ == '__main__':
    main()
