#!/usr/bin/env python3
"""
Pipeline 1 — Step 2: Full cross-match of 195,829 DESI DR1 anomalies.

Runs locally using astroquery + CDS xMatch.
Catalogs: AllWISE, CatWISE2020, Gaia DR3, SDSS DR16, Milliquas v8.

Expected runtime: ~30-60 minutes.
Expected match rates (from 1000-object test):
  AllWISE:     ~6.3%  (~12K matches, W1/W2 IR photometry)
  CatWISE2020: ~13.5% (~26K matches, deeper W1/W2)
  Gaia DR3:    ~1.6%  (~3K matches, proper motions, parallax)
  SDSS DR16:   ~25.7% (~50K matches, ugriz photometry)
  Milliquas:   ~0%    (known QSO identification)
"""

import json
import os
import csv
import time
import sys
import logging

from astroquery.xmatch import XMatch
from astropy.table import Table
from astropy import units as u
import numpy as np

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('pipelines/p1_highz_tracers/outputs/step2_crossmatch/step2.log'),
    ]
)
log = logging.getLogger()

ANOMALY_FILE = 'pipelines/p1_highz_tracers/outputs/desi_dr1/dr1_all_anomalies.json'
OUTPUT_DIR = 'pipelines/p1_highz_tracers/outputs/step2_crossmatch'
CHUNK_SIZE = 5000  # Smaller chunks = more reliable with CDS
MAX_RETRIES = 3
MATCH_RADIUS = 5.0  # arcsec

CATALOGS = [
    ('vizier:II/328/allwise', 'AllWISE', ['W1mag', 'W2mag', 'W3mag', 'W4mag',
     'e_W1mag', 'e_W2mag', 'Jmag', 'Hmag', 'Kmag', 'ccf', 'ex', 'var']),
    ('vizier:II/365/catwise', 'CatWISE2020', ['W1mproPM', 'W2mproPM',
     'e_W1mproPM', 'e_W2mproPM', 'pmRA', 'pmDE']),
    ('vizier:I/355/gaiadr3', 'Gaia_DR3', ['Plx', 'e_Plx', 'pmRA', 'pmDE',
     'Gmag', 'BPmag', 'RPmag', 'RUWE']),
    ('vizier:V/154/sdss16', 'SDSS_DR16', ['umag', 'gmag', 'rmag', 'imag',
     'zmag', 'e_umag', 'e_gmag', 'e_rmag', 'e_imag', 'e_zmag', 'cl']),
    ('vizier:VII/290/catalog', 'Milliquas', ['Name', 'Type', 'Rmag', 'Bmag', 'z']),
]


def load_anomalies():
    log.info(f'Loading {ANOMALY_FILE}...')
    with open(ANOMALY_FILE) as f:
        data = json.load(f)
    log.info(f'Loaded {len(data):,} anomalies')
    return data


def xmatch_catalog(anomalies, cat_id, label, key_cols):
    """Cross-match all anomalies against one catalog."""
    log.info(f'\n{"="*60}')
    log.info(f'{label} ({cat_id})')
    log.info(f'{"="*60}')

    all_matches = {}
    total = len(anomalies)
    n_chunks = (total + CHUNK_SIZE - 1) // CHUNK_SIZE
    t0 = time.time()

    for ci in range(n_chunks):
        start = ci * CHUNK_SIZE
        end = min(start + CHUNK_SIZE, total)
        chunk = anomalies[start:end]

        t = Table()
        t['ra'] = [a['ra'] for a in chunk]
        t['dec'] = [a['dec'] for a in chunk]
        t['tid'] = [str(a['tid']) for a in chunk]

        for attempt in range(MAX_RETRIES):
            try:
                result = XMatch.query(
                    cat1=t, cat2=cat_id,
                    max_distance=MATCH_RADIUS * u.arcsec,
                    colRA1='ra', colDec1='dec'
                )
                for row in result:
                    tid = str(row['tid'])
                    match_data = {'angDist': float(row['angDist'])}
                    for col in key_cols:
                        if col in result.colnames:
                            val = row[col]
                            try:
                                match_data[col] = float(val) if val != '--' else None
                            except (ValueError, TypeError):
                                match_data[col] = str(val) if val != '--' else None
                    all_matches[tid] = match_data

                log.info(f'  chunk {ci+1}/{n_chunks}: {len(result)} matches (running total: {len(all_matches)})')
                break
            except Exception as e:
                log.warning(f'  chunk {ci+1} attempt {attempt+1} failed: {e}')
                if attempt < MAX_RETRIES - 1:
                    time.sleep(10)
                else:
                    log.error(f'  chunk {ci+1} FAILED after {MAX_RETRIES} attempts')

        # Rate limit
        time.sleep(2)

    elapsed = time.time() - t0
    pct = len(all_matches) / total * 100
    log.info(f'{label}: {len(all_matches):,}/{total:,} ({pct:.1f}%) in {elapsed:.0f}s')

    # Save per-catalog result
    cat_file = os.path.join(OUTPUT_DIR, f'xmatch_{label.lower()}.json')
    with open(cat_file, 'w') as f:
        json.dump({
            'catalog': label,
            'catalog_id': cat_id,
            'match_radius_arcsec': MATCH_RADIUS,
            'n_total': total,
            'n_matched': len(all_matches),
            'match_pct': round(pct, 2),
            'elapsed_seconds': round(elapsed),
            'matched_tids': list(all_matches.keys()),
        }, f, indent=2, default=str)
    log.info(f'Saved: {cat_file}')

    return all_matches


def merge_and_save(anomalies, catalog_results):
    """Merge all cross-match results into a single CSV."""
    log.info(f'\n{"="*60}')
    log.info('Merging all results...')
    log.info(f'{"="*60}')

    allwise = catalog_results.get('AllWISE', {})
    catwise = catalog_results.get('CatWISE2020', {})
    gaia = catalog_results.get('Gaia_DR3', {})
    sdss = catalog_results.get('SDSS_DR16', {})
    milliquas = catalog_results.get('Milliquas', {})

    rows = []
    for a in anomalies:
        tid = str(a['tid'])
        row = {
            'tid': a['tid'],
            'ra': round(a['ra'], 6),
            'dec': round(a['dec'], 6),
            'anomaly_score': round(a['score'], 3),
            'worst_band': a['worst'],
            'residual_B': round(a['rB'], 4),
            'residual_R': round(a['rR'], 4),
            'residual_Z': round(a['rZ'], 4),
        }

        # AllWISE / CatWISE (prefer AllWISE, fall back to CatWISE)
        w = allwise.get(tid) or catwise.get(tid)
        if w:
            if tid in allwise:
                row['W1mag'] = w.get('W1mag', '')
                row['W2mag'] = w.get('W2mag', '')
                row['W3mag'] = w.get('W3mag', '')
                row['W4mag'] = w.get('W4mag', '')
                row['wise_source'] = 'AllWISE'
            else:
                row['W1mag'] = w.get('W1mproPM', '')
                row['W2mag'] = w.get('W2mproPM', '')
                row['W3mag'] = ''
                row['W4mag'] = ''
                row['wise_source'] = 'CatWISE2020'
            try:
                w1 = float(row['W1mag'])
                w2 = float(row['W2mag'])
                row['W1_W2'] = round(w1 - w2, 3)
            except (ValueError, TypeError):
                row['W1_W2'] = ''

        # Gaia DR3
        if tid in gaia:
            g = gaia[tid]
            row['gaia_Plx'] = g.get('Plx', '')
            row['gaia_e_Plx'] = g.get('e_Plx', '')
            row['gaia_pmRA'] = g.get('pmRA', '')
            row['gaia_pmDE'] = g.get('pmDE', '')
            row['gaia_Gmag'] = g.get('Gmag', '')
            try:
                plx = float(g.get('Plx', 0) or 0)
                eplx = float(g.get('e_Plx', 1) or 1)
                row['likely_star'] = 1 if (plx > 0 and plx / eplx > 3) else 0
            except:
                row['likely_star'] = ''

        # SDSS DR16
        if tid in sdss:
            s = sdss[tid]
            row['sdss_umag'] = s.get('umag', '')
            row['sdss_gmag'] = s.get('gmag', '')
            row['sdss_rmag'] = s.get('rmag', '')
            row['sdss_imag'] = s.get('imag', '')
            row['sdss_zmag'] = s.get('zmag', '')
            row['sdss_class'] = s.get('cl', '')  # 3=galaxy, 6=star

        # Milliquas
        row['known_qso'] = 1 if tid in milliquas else 0
        if tid in milliquas:
            m = milliquas[tid]
            row['qso_type'] = m.get('Type', '')
            row['qso_z'] = m.get('z', '')

        # Flags
        row['has_wise'] = 1 if (tid in allwise or tid in catwise) else 0
        row['has_gaia'] = 1 if tid in gaia else 0
        row['has_sdss'] = 1 if tid in sdss else 0
        row['in_any_catalog'] = 1 if any(tid in c for c in
            [allwise, catwise, gaia, sdss, milliquas]) else 0

        rows.append(row)

    # Save CSV
    cols = [
        'tid', 'ra', 'dec', 'anomaly_score', 'worst_band',
        'residual_B', 'residual_R', 'residual_Z',
        'W1mag', 'W2mag', 'W3mag', 'W4mag', 'W1_W2', 'wise_source',
        'gaia_Plx', 'gaia_e_Plx', 'gaia_pmRA', 'gaia_pmDE', 'gaia_Gmag', 'likely_star',
        'sdss_umag', 'sdss_gmag', 'sdss_rmag', 'sdss_imag', 'sdss_zmag', 'sdss_class',
        'known_qso', 'qso_type', 'qso_z',
        'has_wise', 'has_gaia', 'has_sdss', 'in_any_catalog',
    ]
    csv_path = os.path.join(OUTPUT_DIR, 'anomaly_crossmatch.csv')
    with open(csv_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=cols, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)

    size_mb = os.path.getsize(csv_path) / 1024 / 1024
    log.info(f'Saved: {csv_path} ({size_mb:.1f} MB)')

    # Also save as parquet if pyarrow available
    try:
        import pyarrow as pa
        import pyarrow.csv as pcsv
        import pyarrow.parquet as pq
        table = pcsv.read_csv(csv_path)
        pq_path = os.path.join(OUTPUT_DIR, 'anomaly_crossmatch.parquet')
        pq.write_table(table, pq_path)
        log.info(f'Saved: {pq_path} ({os.path.getsize(pq_path)/1024/1024:.1f} MB)')
    except Exception as e:
        log.warning(f'Parquet save failed: {e}')

    # Summary
    n = len(rows)
    n_wise = sum(1 for r in rows if r.get('has_wise'))
    n_gaia = sum(1 for r in rows if r.get('has_gaia'))
    n_sdss = sum(1 for r in rows if r.get('has_sdss'))
    n_qso = sum(1 for r in rows if r.get('known_qso') == 1)
    n_star = sum(1 for r in rows if r.get('likely_star') == 1)
    n_any = sum(1 for r in rows if r.get('in_any_catalog'))
    n_new = n - n_any
    w12_vals = [r['W1_W2'] for r in rows if isinstance(r.get('W1_W2'), (int, float))]
    n_qso_color = sum(1 for w in w12_vals if w > 0.8)

    summary = {
        'total_anomalies': n,
        'match_radius_arcsec': MATCH_RADIUS,
        'with_wise': n_wise,
        'with_gaia': n_gaia,
        'with_sdss': n_sdss,
        'known_qsos_milliquas': n_qso,
        'likely_stars_gaia': n_star,
        'in_any_catalog': n_any,
        'genuinely_new': n_new,
        'wise_w1w2_gt_0.8_qso_color': n_qso_color,
        'wise_w1w2_available': len(w12_vals),
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime()),
    }

    summary_path = os.path.join(OUTPUT_DIR, 'crossmatch_summary.json')
    with open(summary_path, 'w') as f:
        json.dump(summary, f, indent=2)

    log.info(f'\n{"="*60}')
    log.info('STEP 2 CROSS-MATCH SUMMARY')
    log.info(f'{"="*60}')
    log.info(f'Total anomalies:          {n:>8,}')
    log.info(f'With WISE (AllWISE+CatW): {n_wise:>8,} ({n_wise/n*100:.1f}%)')
    log.info(f'With Gaia DR3:            {n_gaia:>8,} ({n_gaia/n*100:.1f}%)')
    log.info(f'With SDSS DR16:           {n_sdss:>8,} ({n_sdss/n*100:.1f}%)')
    log.info(f'Known QSOs (Milliquas):   {n_qso:>8,} ({n_qso/n*100:.1f}%)')
    log.info(f'Likely stars (Gaia plx):  {n_star:>8,} ({n_star/n*100:.1f}%)')
    log.info(f'In ANY catalog:           {n_any:>8,} ({n_any/n*100:.1f}%)')
    log.info(f'Genuinely new:            {n_new:>8,} ({n_new/n*100:.1f}%)')
    log.info(f'W1-W2 > 0.8 (QSO color): {n_qso_color:>8,}')
    log.info(f'{"="*60}')

    return summary


def main():
    t_start = time.time()

    anomalies = load_anomalies()

    # Cross-match against each catalog
    catalog_results = {}
    for cat_id, label, key_cols in CATALOGS:
        result = xmatch_catalog(anomalies, cat_id, label, key_cols)
        catalog_results[label] = result

        # Save checkpoint after each catalog
        checkpoint = {
            'completed_catalogs': list(catalog_results.keys()),
            'match_counts': {k: len(v) for k, v in catalog_results.items()},
            'elapsed_seconds': round(time.time() - t_start),
        }
        with open(os.path.join(OUTPUT_DIR, 'checkpoint.json'), 'w') as f:
            json.dump(checkpoint, f, indent=2)

    # Merge and save
    summary = merge_and_save(anomalies, catalog_results)

    elapsed = time.time() - t_start
    log.info(f'\nTotal elapsed: {elapsed/60:.1f} minutes')
    log.info('STEP 2 COMPLETE')

    return summary


if __name__ == '__main__':
    os.chdir('/Users/houstongolden/Desktop/CODE_2025/bigbounce')
    main()
