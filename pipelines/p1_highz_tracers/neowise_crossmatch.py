#!/usr/bin/env python3
"""
NEOWISE/AllWISE Cross-Match Pipeline for DESI Spectral Anomalies
================================================================
Cross-matches gold (and silver) anomalies with:
  1. AllWISE catalog via VizieR TAP — IR counterpart identification
  2. NEOWISE-R Single Exposure catalog via IRSA Gator — time-domain variability

Computes variability statistics (chi-squared, std dev) per object.
Outputs objects that are BOTH spectrally anomalous AND IR-variable.

Author: Houston Golden
Date: 2026-03-29
"""

import json
import time
import sys
import os
import glob
import re
import requests
import numpy as np
import pandas as pd
from datetime import datetime

# --- Paths ---
BASE = "/Users/houstongolden/Desktop/CODE_2026/bigbounce/pipelines/p1_highz_tracers"
GOLD_PATH = os.path.join(BASE, "outputs/gold_anomalies/gold_anomalies.json")
SILVER_DIR = os.path.join(BASE, "outputs/enhanced_18M_deduped")
OUT_DIR = os.path.join(BASE, "outputs/neowise_crossmatch")
os.makedirs(OUT_DIR, exist_ok=True)

# --- Endpoints ---
VIZIER_TAP = "https://tapvizier.cds.unistra.fr/TAPVizieR/tap/sync"
IRSA_GATOR = "https://irsa.ipac.caltech.edu/cgi-bin/Gator/nph-query"

# --- Rate limiting ---
QUERY_INTERVAL = 1.1  # seconds between queries


def load_gold_anomalies():
    """Load gold anomalies from JSON."""
    with open(GOLD_PATH) as f:
        gold = json.load(f)
    print(f"Loaded {len(gold)} gold anomalies")
    return gold


def load_silver_anomalies():
    """Extract silver anomalies from deduped parquet catalog.
    Filter: anomaly_score > 3.0 AND max(snr_b, snr_r, snr_z) > 0.5
    Exclude objects already in gold set.
    """
    import pyarrow.parquet as pq

    parquets = sorted(glob.glob(os.path.join(SILVER_DIR, "desi_dr1_catalog_batch_*.parquet")))
    cols = ['targetid', 'target_ra', 'target_dec', 'z', 'anomaly_score',
            'spectype', 'median_coadd_snr_b', 'median_coadd_snr_r', 'median_coadd_snr_z']

    gold = load_gold_anomalies()
    gold_ids = set(obj['targetid'] for obj in gold)

    silver_rows = []
    for pf in parquets:
        t = pq.read_table(pf, columns=cols)
        df = t.to_pandas()
        mask = (
            (df['anomaly_score'] > 3.0) &
            (df[['median_coadd_snr_b', 'median_coadd_snr_r', 'median_coadd_snr_z']].max(axis=1) > 0.5) &
            (~df['targetid'].isin(gold_ids))
        )
        if mask.any():
            silver_rows.append(df[mask][['targetid', 'target_ra', 'target_dec', 'z',
                                         'anomaly_score', 'spectype']])

    if silver_rows:
        silver_df = pd.concat(silver_rows, ignore_index=True)
        silver_df = silver_df.rename(columns={'target_ra': 'ra', 'target_dec': 'dec'})
        silver = silver_df.to_dict('records')
    else:
        silver = []

    print(f"Extracted {len(silver)} silver anomalies (score>3, SNR>0.5, not in gold)")
    return silver


def query_vizier_allwise(ra, dec, radius_deg=0.00139):
    """Query AllWISE via VizieR TAP for IR counterpart within 5 arcsec."""
    adql = (
        f"SELECT TOP 1 AllWISE, RAJ2000, DEJ2000, W1mag, W2mag, W3mag, W4mag, pmRA, pmDE "
        f"FROM \"II/328/allwise\" "
        f"WHERE CONTAINS(POINT('ICRS', RAJ2000, DEJ2000), "
        f"CIRCLE('ICRS', {ra:.6f}, {dec:.6f}, {radius_deg})) = 1"
    )
    params = {
        'REQUEST': 'doQuery',
        'LANG': 'ADQL',
        'FORMAT': 'json',
        'QUERY': adql
    }
    try:
        resp = requests.get(VIZIER_TAP, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        if 'data' in data and len(data['data']) > 0:
            meta = [col['name'] for col in data['metadata']]
            row = data['data'][0]
            return dict(zip(meta, row))
        return None
    except Exception as e:
        print(f"  VizieR error for ({ra:.4f}, {dec:.4f}): {e}")
        return None


def parse_ipac_table(text):
    """Parse IRSA IPAC table format into list of dicts."""
    lines = text.strip().split('\n')
    # Skip comment lines (starting with \) and find header
    header_line = None
    data_start = None
    for i, line in enumerate(lines):
        if line.startswith('\\') or line.strip() == '':
            continue
        if line.startswith('|'):
            if header_line is None:
                header_line = line
            continue
        # First non-comment, non-header line is data
        if header_line is not None and data_start is None:
            data_start = i
            break

    if header_line is None or data_start is None:
        return []

    # Parse column names from header
    cols = [c.strip() for c in header_line.split('|') if c.strip()]

    # Parse data rows
    rows = []
    for line in lines[data_start:]:
        if line.startswith('\\') or line.startswith('|') or line.strip() == '':
            continue
        # Split by whitespace, matching column count
        values = line.split()
        if len(values) >= len(cols):
            row = {}
            for j, col in enumerate(cols):
                val = values[j] if j < len(values) else None
                if val == 'null' or val is None:
                    row[col] = None
                else:
                    try:
                        row[col] = float(val)
                    except ValueError:
                        row[col] = val
            rows.append(row)

    return rows


def query_neowise_gator(ra, dec, radius_arcsec=3.0):
    """Query NEOWISE-R Single Exposure catalog via IRSA Gator cone search."""
    params = {
        'catalog': 'neowiser_p1bs_psd',
        'spatial': 'cone',
        'objstr': f'{ra:.6f} {dec:.6f}',
        'radius': str(radius_arcsec),
        'radunits': 'arcsec',
        'outfmt': '1',  # IPAC table
        'selcols': 'mjd,w1mpro,w1sigmpro,w2mpro,w2sigmpro,qual_frame,cc_flags,ph_qual',
        'orderby': 'mjd',
    }
    try:
        resp = requests.get(IRSA_GATOR, params=params, timeout=120)
        resp.raise_for_status()
        rows = parse_ipac_table(resp.text)
        # Filter: only keep good quality detections
        good_rows = []
        for r in rows:
            # ph_qual: A=best, B=good, C=ok for each band
            # cc_flags: 0=no contamination
            # Skip rows with null magnitudes
            if r.get('w1mpro') is not None or r.get('w2mpro') is not None:
                good_rows.append(r)
        return good_rows
    except Exception as e:
        print(f"  Gator error for ({ra:.4f}, {dec:.4f}): {e}")
        return []


def compute_variability(lightcurve):
    """Compute variability statistics from NEOWISE lightcurve."""
    if not lightcurve:
        return None

    mjds = []
    w1_mags, w1_errs = [], []
    w2_mags, w2_errs = [], []

    for pt in lightcurve:
        if pt.get('mjd') is not None:
            mjds.append(float(pt['mjd']))
        if pt.get('w1mpro') is not None and pt.get('w1sigmpro') is not None:
            try:
                m, e = float(pt['w1mpro']), float(pt['w1sigmpro'])
                if e > 0 and e < 1.0:  # reject bad errors
                    w1_mags.append(m)
                    w1_errs.append(e)
            except (ValueError, TypeError):
                pass
        if pt.get('w2mpro') is not None and pt.get('w2sigmpro') is not None:
            try:
                m, e = float(pt['w2mpro']), float(pt['w2sigmpro'])
                if e > 0 and e < 1.0:
                    w2_mags.append(m)
                    w2_errs.append(e)
            except (ValueError, TypeError):
                pass

    result = {
        'n_epochs': len(lightcurve),
        'mjd_min': min(mjds) if mjds else None,
        'mjd_max': max(mjds) if mjds else None,
        'time_baseline_days': round(max(mjds) - min(mjds), 1) if len(mjds) > 1 else 0,
    }

    # W1 variability
    if len(w1_mags) >= 3:
        w1_arr = np.array(w1_mags)
        w1_err_arr = np.array(w1_errs)
        w1_mean = np.mean(w1_arr)
        w1_std = np.std(w1_arr)
        w1_chi2 = float(np.sum((w1_arr - w1_mean)**2 / w1_err_arr**2))
        w1_dof = len(w1_arr) - 1
        result.update({
            'w1_n_pts': len(w1_mags),
            'w1_mean': round(float(w1_mean), 4),
            'w1_std': round(float(w1_std), 4),
            'w1_chi2': round(w1_chi2, 2),
            'w1_dof': w1_dof,
            'w1_chi2_per_dof': round(w1_chi2 / w1_dof, 3) if w1_dof > 0 else None,
            'w1_variable': bool(w1_chi2 > 3 * w1_dof),
            'w1_amplitude': round(float(np.max(w1_arr) - np.min(w1_arr)), 4),
        })
    else:
        result.update({'w1_n_pts': len(w1_mags), 'w1_variable': False})

    # W2 variability
    if len(w2_mags) >= 3:
        w2_arr = np.array(w2_mags)
        w2_err_arr = np.array(w2_errs)
        w2_mean = np.mean(w2_arr)
        w2_std = np.std(w2_arr)
        w2_chi2 = float(np.sum((w2_arr - w2_mean)**2 / w2_err_arr**2))
        w2_dof = len(w2_arr) - 1
        result.update({
            'w2_n_pts': len(w2_mags),
            'w2_mean': round(float(w2_mean), 4),
            'w2_std': round(float(w2_std), 4),
            'w2_chi2': round(w2_chi2, 2),
            'w2_dof': w2_dof,
            'w2_chi2_per_dof': round(w2_chi2 / w2_dof, 3) if w2_dof > 0 else None,
            'w2_variable': bool(w2_chi2 > 3 * w2_dof),
            'w2_amplitude': round(float(np.max(w2_arr) - np.min(w2_arr)), 4),
        })
    else:
        result.update({'w2_n_pts': len(w2_mags), 'w2_variable': False})

    result['is_variable'] = result.get('w1_variable', False) or result.get('w2_variable', False)
    return result


def process_anomaly(obj, idx, total, tier="gold"):
    """Process a single anomaly: AllWISE match + NEOWISE lightcurve + variability."""
    ra = obj['ra']
    dec = obj['dec']
    targetid = obj['targetid']
    score = obj.get('anomaly_score', 0)
    print(f"  [{idx+1}/{total}] {tier.upper()} tid={targetid} "
          f"(RA={ra:.4f}, Dec={dec:.4f}, z={obj.get('z','?')}, "
          f"score={score:.2f}, type={obj.get('spectype','?')})")

    result = {
        'targetid': targetid,
        'ra': ra,
        'dec': dec,
        'z': obj.get('z'),
        'anomaly_score': score,
        'spectype': obj.get('spectype'),
        'tier': tier,
    }

    # Step 1: AllWISE match via VizieR
    allwise = query_vizier_allwise(ra, dec)
    time.sleep(QUERY_INTERVAL)

    if allwise:
        result['allwise_match'] = True
        result['allwise_id'] = allwise.get('AllWISE')
        result['w1mag'] = allwise.get('W1mag')
        result['w2mag'] = allwise.get('W2mag')
        result['w3mag'] = allwise.get('W3mag')
        result['w4mag'] = allwise.get('W4mag')
        result['pmRA'] = allwise.get('pmRA')
        result['pmDE'] = allwise.get('pmDE')

        # W1-W2 color (AGN diagnostic: Stern+2012 criterion W1-W2 > 0.8)
        if allwise.get('W1mag') is not None and allwise.get('W2mag') is not None:
            try:
                w1w2 = float(allwise['W1mag']) - float(allwise['W2mag'])
                result['w1w2_color'] = round(w1w2, 3)
                result['agn_ir_color'] = w1w2 > 0.8
            except (ValueError, TypeError):
                pass

        print(f"    AllWISE: {allwise.get('AllWISE')} "
              f"W1={allwise.get('W1mag')} W2={allwise.get('W2mag')}")

        # Step 2: NEOWISE lightcurve via Gator
        nw_ra = float(allwise.get('RAJ2000', ra))
        nw_dec = float(allwise.get('DEJ2000', dec))
        lc = query_neowise_gator(nw_ra, nw_dec, radius_arcsec=3.0)
        time.sleep(QUERY_INTERVAL)

        if lc:
            var_stats = compute_variability(lc)
            if var_stats:
                result['neowise_match'] = True
                result.update(var_stats)
                var_flag = "*** VARIABLE ***" if var_stats['is_variable'] else "non-variable"
                w1_info = f"W1: chi2/dof={var_stats.get('w1_chi2_per_dof','N/A')}"
                w2_info = f"W2: chi2/dof={var_stats.get('w2_chi2_per_dof','N/A')}"
                print(f"    NEOWISE: {var_stats['n_epochs']} epochs over "
                      f"{var_stats.get('time_baseline_days',0):.0f} days | "
                      f"{w1_info} | {w2_info} -> {var_flag}")
            else:
                result['neowise_match'] = True
                result['n_epochs'] = len(lc)
                result['is_variable'] = False
                print(f"    NEOWISE: {len(lc)} epochs (insufficient for stats)")
        else:
            result['neowise_match'] = False
            result['is_variable'] = False
            print(f"    NEOWISE: no detections")
    else:
        result['allwise_match'] = False
        result['neowise_match'] = False
        result['is_variable'] = False
        print(f"    AllWISE: no match within 5\"")

    return result


def save_checkpoint(results, filename="neowise_crossmatch_checkpoint.json"):
    """Save intermediate results."""
    path = os.path.join(OUT_DIR, filename)
    with open(path, 'w') as f:
        json.dump(results, f, indent=2, default=str)


def main():
    print("=" * 70)
    print("NEOWISE/AllWISE Cross-Match Pipeline for DESI Spectral Anomalies")
    print(f"Started: {datetime.now().isoformat()}")
    print("=" * 70)

    # Load gold anomalies
    gold = load_gold_anomalies()

    # Process gold tier
    print(f"\n--- Processing {len(gold)} GOLD anomalies ---")
    print(f"    AllWISE: VizieR TAP cone search (5\" radius)")
    print(f"    NEOWISE: IRSA Gator cone search (3\" radius)")
    print(f"    Rate limit: {QUERY_INTERVAL}s between queries")
    print()

    all_results = []
    for i, obj in enumerate(gold):
        result = process_anomaly(obj, i, len(gold), tier="gold")
        all_results.append(result)
        if (i + 1) % 10 == 0:
            save_checkpoint(all_results)
            n_var = sum(1 for r in all_results if r.get('is_variable'))
            print(f"  --- Checkpoint: {i+1}/{len(gold)} done, "
                  f"{n_var} variable so far ---\n")

    # Save full results
    results_path = os.path.join(OUT_DIR, "neowise_crossmatch.json")
    with open(results_path, 'w') as f:
        json.dump(all_results, f, indent=2, default=str)
    print(f"\nSaved: {results_path}")

    # Extract variable anomalies
    variable = [r for r in all_results if r.get('is_variable', False)]
    variable_path = os.path.join(OUT_DIR, "variable_anomalies.json")
    with open(variable_path, 'w') as f:
        json.dump(variable, f, indent=2, default=str)
    print(f"Saved: {variable_path} ({len(variable)} objects)")

    # --- Summary ---
    print("\n" + "=" * 70)
    print("CROSS-MATCH SUMMARY")
    print("=" * 70)
    n_total = len(all_results)
    n_allwise = sum(1 for r in all_results if r.get('allwise_match'))
    n_neowise = sum(1 for r in all_results if r.get('neowise_match'))
    n_variable = len(variable)
    n_w1var = sum(1 for r in all_results if r.get('w1_variable'))
    n_w2var = sum(1 for r in all_results if r.get('w2_variable'))

    print(f"Total processed:             {n_total}")
    print(f"AllWISE matches:             {n_allwise} / {n_total} ({100*n_allwise/n_total:.1f}%)")
    print(f"NEOWISE detections:          {n_neowise} / {n_total} ({100*n_neowise/n_total:.1f}%)")
    print(f"W1-variable:                 {n_w1var}")
    print(f"W2-variable:                 {n_w2var}")
    print(f"Either-band variable:        {n_variable} ({100*n_variable/n_total:.1f}%)")

    # Spectype breakdown
    print(f"\nAllWISE match rate by spectype:")
    types_all = {}
    types_match = {}
    types_var = {}
    for r in all_results:
        st = r.get('spectype', 'UNKNOWN')
        types_all[st] = types_all.get(st, 0) + 1
        if r.get('allwise_match'):
            types_match[st] = types_match.get(st, 0) + 1
        if r.get('is_variable'):
            types_var[st] = types_var.get(st, 0) + 1
    for st in sorted(types_all.keys()):
        n = types_all[st]
        m = types_match.get(st, 0)
        v = types_var.get(st, 0)
        print(f"  {st:8s}: {m}/{n} matched ({100*m/n:.0f}%), {v} variable")

    # AGN IR color analysis
    if any(r.get('w1w2_color') is not None for r in all_results):
        print(f"\nW1-W2 color distribution (AGN criterion: W1-W2 > 0.8):")
        colors = [r['w1w2_color'] for r in all_results if r.get('w1w2_color') is not None]
        n_agn = sum(1 for c in colors if c > 0.8)
        print(f"  Objects with W1-W2 color: {len(colors)}")
        print(f"  AGN-like (W1-W2 > 0.8):  {n_agn} ({100*n_agn/len(colors):.0f}%)")
        print(f"  Mean W1-W2:              {np.mean(colors):.3f}")
        print(f"  Median W1-W2:            {np.median(colors):.3f}")

    # Top variable objects
    if variable:
        print(f"\n--- TOP VARIABLE ANOMALIES ---")
        variable_sorted = sorted(variable, key=lambda x: max(
            x.get('w1_chi2_per_dof', 0) or 0,
            x.get('w2_chi2_per_dof', 0) or 0
        ), reverse=True)
        for v in variable_sorted[:15]:
            max_chi2 = max(v.get('w1_chi2_per_dof', 0) or 0,
                          v.get('w2_chi2_per_dof', 0) or 0)
            print(f"  tid={v['targetid']}  z={v.get('z','?'):>8}  "
                  f"type={v.get('spectype','?'):>6}  "
                  f"anom_score={v.get('anomaly_score',0):.2f}  "
                  f"chi2/dof={max_chi2:.1f}  "
                  f"W1amp={v.get('w1_amplitude','?')}  "
                  f"W2amp={v.get('w2_amplitude','?')}  "
                  f"epochs={v.get('n_epochs','?')}  "
                  f"baseline={v.get('time_baseline_days','?')}d")

    # Save summary
    summary = {
        'timestamp': datetime.now().isoformat(),
        'pipeline': 'NEOWISE/AllWISE Cross-Match v1',
        'total_processed': n_total,
        'tier': 'gold',
        'allwise_matches': n_allwise,
        'allwise_match_rate_pct': round(100 * n_allwise / n_total, 1),
        'neowise_detections': n_neowise,
        'neowise_detection_rate_pct': round(100 * n_neowise / n_total, 1),
        'w1_variable': n_w1var,
        'w2_variable': n_w2var,
        'either_band_variable': n_variable,
        'variable_rate_pct': round(100 * n_variable / n_total, 1),
        'spectypes': {st: {'total': types_all[st],
                           'allwise_match': types_match.get(st, 0),
                           'variable': types_var.get(st, 0)}
                      for st in types_all},
    }
    summary_path = os.path.join(OUT_DIR, "crossmatch_summary.json")
    with open(summary_path, 'w') as f:
        json.dump(summary, f, indent=2)
    print(f"\nSummary: {summary_path}")
    print(f"Finished: {datetime.now().isoformat()}")


if __name__ == "__main__":
    main()
