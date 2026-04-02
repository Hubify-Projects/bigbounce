#!/usr/bin/env python3
"""
SDSS × DESI Cross-Survey Anomaly Correlation

Cross-match anomalies found in SDSS DR18 with those found in DESI DR1.
Objects flagged as anomalous in BOTH independent surveys are highest priority.

This is experiment #9 in the research queue.
Blocked until: SDSS DR18 scan complete ✓
"""
import numpy as np
import json
import os
import time
from pathlib import Path

try:
    import pyarrow.parquet as pq
    import pandas as pd
    HAS_PARQUET = True
except ImportError:
    HAS_PARQUET = False
    print("ERROR: Need pyarrow and pandas. pip install pyarrow pandas")
    exit(1)

# Sky cross-match radius in arcseconds
MATCH_RADIUS_ARCSEC = 3.0


def angular_separation(ra1, dec1, ra2, dec2):
    """Angular separation in arcseconds between two sets of coordinates (vectorized)."""
    ra1, dec1, ra2, dec2 = map(np.radians, [ra1, dec1, ra2, dec2])
    cos_sep = (np.sin(dec1) * np.sin(dec2) +
               np.cos(dec1) * np.cos(dec2) * np.cos(ra1 - ra2))
    cos_sep = np.clip(cos_sep, -1, 1)
    return np.degrees(np.arccos(cos_sep)) * 3600  # arcseconds


def load_desi_anomalies(desi_dir):
    """Load DESI DR1 anomaly catalog."""
    print(f"Loading DESI anomalies from {desi_dir}...")
    desi_files = sorted(Path(desi_dir).glob("*.parquet"))
    if not desi_files:
        # Try the enhanced catalog
        desi_files = sorted(Path(desi_dir).glob("enhanced_batch_*.parquet"))
    if not desi_files:
        print(f"  No parquet files found in {desi_dir}")
        return None

    dfs = []
    for f in desi_files:
        df = pq.read_table(f).to_pandas()
        dfs.append(df)
    desi = pd.concat(dfs, ignore_index=True)
    print(f"  Loaded {len(desi):,} DESI spectra")

    # Filter to anomalies (score > 5.0)
    if 'anomaly_score' in desi.columns:
        desi_anom = desi[desi['anomaly_score'] > 5.0].copy()
        print(f"  DESI anomalies (score > 5): {len(desi_anom):,}")
        return desi_anom
    return desi


def load_sdss_anomalies(sdss_dir):
    """Load SDSS DR18 anomaly catalog."""
    print(f"Loading SDSS anomalies from {sdss_dir}...")
    sdss_files = sorted(Path(sdss_dir).glob("sdss_batch_*.parquet"))
    if not sdss_files:
        print(f"  No parquet files found in {sdss_dir}")
        return None

    dfs = []
    for f in sdss_files:
        df = pq.read_table(f).to_pandas()
        dfs.append(df)
    sdss = pd.concat(dfs, ignore_index=True)
    print(f"  Loaded {len(sdss):,} SDSS spectra")

    # SDSS has plate/mjd/fiberid but may not have RA/DEC directly
    # Need to derive RA/DEC from the plate catalog or use a mapping
    if 'ra' not in sdss.columns and 'RA' not in sdss.columns:
        print("  WARNING: No RA/DEC in SDSS catalog. Need plate→coord mapping.")
        return sdss

    # Normalize column names
    if 'RA' in sdss.columns:
        sdss = sdss.rename(columns={'RA': 'ra', 'DEC': 'dec'})

    # Filter to anomalies
    if 'anomaly_score' in sdss.columns:
        sdss_anom = sdss[sdss['anomaly_score'] > 5.0].copy()
        print(f"  SDSS anomalies (score > 5): {len(sdss_anom):,}")
        return sdss_anom
    return sdss


def cross_match_catalogs(cat1, cat2, radius_arcsec=3.0, cat1_name="DESI", cat2_name="SDSS"):
    """Cross-match two catalogs by sky position."""
    print(f"\nCross-matching {cat1_name} ({len(cat1):,}) × {cat2_name} ({len(cat2):,})...")
    print(f"  Match radius: {radius_arcsec} arcsec")

    ra1 = np.array(cat1['ra'])
    dec1 = np.array(cat1['dec'])
    ra2 = np.array(cat2['ra'])
    dec2 = np.array(cat2['dec'])

    matches = []
    t0 = time.time()

    # Use a coarse grid for efficiency
    dec_bins = np.arange(-90, 91, 1.0)

    for i_bin in range(len(dec_bins) - 1):
        dec_lo, dec_hi = dec_bins[i_bin], dec_bins[i_bin + 1]
        # Include buffer for match radius
        buffer = radius_arcsec / 3600 + 0.01
        idx1 = np.where((dec1 >= dec_lo - buffer) & (dec1 < dec_hi + buffer))[0]
        idx2 = np.where((dec2 >= dec_lo - buffer) & (dec2 < dec_hi + buffer))[0]

        if len(idx1) == 0 or len(idx2) == 0:
            continue

        for i in idx1:
            # Quick RA filter
            cos_dec = np.cos(np.radians(dec1[i]))
            ra_tol = radius_arcsec / 3600 / max(cos_dec, 0.01)
            ra_mask = np.abs(ra2[idx2] - ra1[i]) < ra_tol
            candidates = idx2[ra_mask]

            for j in candidates:
                sep = angular_separation(ra1[i], dec1[i], ra2[j], dec2[j])
                if sep <= radius_arcsec:
                    matches.append({
                        f'{cat1_name}_idx': int(i),
                        f'{cat2_name}_idx': int(j),
                        'separation_arcsec': float(sep),
                        'ra': float(ra1[i]),
                        'dec': float(dec1[i]),
                        f'{cat1_name}_score': float(cat1.iloc[i].get('anomaly_score', 0)),
                        f'{cat2_name}_score': float(cat2.iloc[j].get('anomaly_score', 0)),
                    })

    elapsed = time.time() - t0
    print(f"  Found {len(matches):,} matches in {elapsed:.1f}s")
    return matches


def main():
    project_root = Path(__file__).resolve().parent.parent.parent

    # Paths to anomaly catalogs
    desi_dir = project_root / "pipelines" / "p1_highz_tracers" / "outputs" / "enhanced_18M"
    sdss_dir = project_root / "pipelines" / "h200_results" / "sdss_dr18"

    # Fallback paths
    if not desi_dir.exists():
        desi_dir = project_root / "pipelines" / "h200_results" / "outputs"

    out_dir = Path(__file__).resolve().parent
    os.makedirs(out_dir, exist_ok=True)

    print('='*60)
    print('SDSS × DESI Cross-Survey Anomaly Correlation')
    print('='*60)

    # Load catalogs
    desi_anom = load_desi_anomalies(desi_dir)
    sdss_anom = load_sdss_anomalies(sdss_dir)

    if desi_anom is None or sdss_anom is None:
        print("\nERROR: Could not load one or both catalogs.")
        print("Make sure the SDSS and DESI parquet files are backed up locally.")
        return

    # Check if SDSS has coordinates
    if 'ra' not in sdss_anom.columns:
        print("\nSDSS catalog lacks RA/DEC — checking for plate/fiberid columns...")
        print(f"  Available columns: {list(sdss_anom.columns[:10])}")
        print("  Need to add RA/DEC from SDSS plate catalog. Skipping cross-match for now.")

        # Still produce a useful summary
        summary = {
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'sdss_total': len(sdss_anom) if sdss_anom is not None else 0,
            'desi_total': len(desi_anom) if desi_anom is not None else 0,
            'status': 'NEEDS_COORDINATES',
            'note': 'SDSS catalog has plate/mjd/fiberid but no RA/DEC. Need coordinate lookup.',
        }
        with open(out_dir / 'cross_survey_summary.json', 'w') as f:
            json.dump(summary, f, indent=2)
        print(f"\nSaved summary to {out_dir / 'cross_survey_summary.json'}")
        return

    # Cross-match
    matches = cross_match_catalogs(desi_anom, sdss_anom, MATCH_RADIUS_ARCSEC)

    # Analyze matches
    if matches:
        match_df = pd.DataFrame(matches)

        # Sort by combined score
        match_df['combined_score'] = match_df['DESI_score'] + match_df['SDSS_score']
        match_df = match_df.sort_values('combined_score', ascending=False)

        print(f'\nTop 20 cross-survey anomalies:')
        for _, row in match_df.head(20).iterrows():
            print(f"  RA={row['ra']:.4f} DEC={row['dec']:.4f}  "
                  f"DESI={row['DESI_score']:.2f} SDSS={row['SDSS_score']:.2f} "
                  f"sep={row['separation_arcsec']:.2f}\"")

        if HAS_PARQUET:
            match_df.to_parquet(out_dir / 'cross_survey_matches.parquet', index=False)

    # Summary
    summary = {
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
        'sdss_anomalies': len(sdss_anom),
        'desi_anomalies': len(desi_anom),
        'cross_matches': len(matches),
        'match_radius_arcsec': MATCH_RADIUS_ARCSEC,
        'top_10': [
            {
                'ra': m['ra'], 'dec': m['dec'],
                'desi_score': m['DESI_score'], 'sdss_score': m['SDSS_score'],
                'separation': m['separation_arcsec']
            }
            for m in sorted(matches, key=lambda x: x['DESI_score'] + x['SDSS_score'], reverse=True)[:10]
        ] if matches else [],
    }

    with open(out_dir / 'cross_survey_summary.json', 'w') as f:
        json.dump(summary, f, indent=2)

    print(f'\n{"="*60}')
    print(f'COMPLETE: {len(matches):,} cross-survey matches')
    print(f'{"="*60}')


if __name__ == '__main__':
    main()
