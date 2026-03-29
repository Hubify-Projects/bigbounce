#!/usr/bin/env python3
"""
NEOWISE/AllWISE Cross-Match — SILVER TIER
==========================================
Processes top-N silver anomalies (by anomaly_score) through
the same AllWISE + NEOWISE pipeline as gold tier.

Author: Houston Golden
Date: 2026-03-29
"""

import json
import time
import sys
import os
import requests
import numpy as np
from datetime import datetime

BASE = "/Users/houstongolden/Desktop/CODE_2026/bigbounce/pipelines/p1_highz_tracers"
OUT_DIR = os.path.join(BASE, "outputs/neowise_crossmatch")
SILVER_CATALOG = os.path.join(OUT_DIR, "silver_anomalies_catalog.json")

VIZIER_TAP = "https://tapvizier.cds.unistra.fr/TAPVizieR/tap/sync"
IRSA_GATOR = "https://irsa.ipac.caltech.edu/cgi-bin/Gator/nph-query"
QUERY_INTERVAL = 1.1

# How many silver to process (top-N by anomaly_score)
MAX_SILVER = 200


def query_vizier_allwise(ra, dec, radius_deg=0.00139):
    adql = (
        f"SELECT TOP 1 AllWISE, RAJ2000, DEJ2000, W1mag, W2mag, W3mag, W4mag, pmRA, pmDE "
        f"FROM \"II/328/allwise\" "
        f"WHERE CONTAINS(POINT('ICRS', RAJ2000, DEJ2000), "
        f"CIRCLE('ICRS', {ra:.6f}, {dec:.6f}, {radius_deg})) = 1"
    )
    params = {'REQUEST': 'doQuery', 'LANG': 'ADQL', 'FORMAT': 'json', 'QUERY': adql}
    try:
        resp = requests.get(VIZIER_TAP, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        if 'data' in data and len(data['data']) > 0:
            meta = [col['name'] for col in data['metadata']]
            return dict(zip(meta, data['data'][0]))
        return None
    except Exception as e:
        return None


def parse_ipac_table(text):
    lines = text.strip().split('\n')
    header_line = None
    data_start = None
    for i, line in enumerate(lines):
        if line.startswith('\\') or line.strip() == '':
            continue
        if line.startswith('|'):
            if header_line is None:
                header_line = line
            continue
        if header_line is not None and data_start is None:
            data_start = i
            break
    if header_line is None or data_start is None:
        return []
    cols = [c.strip() for c in header_line.split('|') if c.strip()]
    rows = []
    for line in lines[data_start:]:
        if line.startswith('\\') or line.startswith('|') or line.strip() == '':
            continue
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
    params = {
        'catalog': 'neowiser_p1bs_psd',
        'spatial': 'cone',
        'objstr': f'{ra:.6f} {dec:.6f}',
        'radius': str(radius_arcsec),
        'radunits': 'arcsec',
        'outfmt': '1',
        'selcols': 'mjd,w1mpro,w1sigmpro,w2mpro,w2sigmpro,qual_frame,cc_flags,ph_qual',
        'orderby': 'mjd',
    }
    try:
        resp = requests.get(IRSA_GATOR, params=params, timeout=120)
        resp.raise_for_status()
        rows = parse_ipac_table(resp.text)
        return [r for r in rows if r.get('w1mpro') is not None or r.get('w2mpro') is not None]
    except Exception as e:
        return []


def compute_variability(lightcurve):
    if not lightcurve:
        return None
    mjds, w1_mags, w1_errs, w2_mags, w2_errs = [], [], [], [], []
    for pt in lightcurve:
        if pt.get('mjd') is not None:
            mjds.append(float(pt['mjd']))
        if pt.get('w1mpro') is not None and pt.get('w1sigmpro') is not None:
            try:
                m, e = float(pt['w1mpro']), float(pt['w1sigmpro'])
                if 0 < e < 1.0:
                    w1_mags.append(m); w1_errs.append(e)
            except: pass
        if pt.get('w2mpro') is not None and pt.get('w2sigmpro') is not None:
            try:
                m, e = float(pt['w2mpro']), float(pt['w2sigmpro'])
                if 0 < e < 1.0:
                    w2_mags.append(m); w2_errs.append(e)
            except: pass

    result = {
        'n_epochs': len(lightcurve),
        'mjd_min': min(mjds) if mjds else None,
        'mjd_max': max(mjds) if mjds else None,
        'time_baseline_days': round(max(mjds) - min(mjds), 1) if len(mjds) > 1 else 0,
    }

    for band, mags, errs in [('w1', w1_mags, w1_errs), ('w2', w2_mags, w2_errs)]:
        if len(mags) >= 3:
            arr, earr = np.array(mags), np.array(errs)
            mean = np.mean(arr)
            chi2 = float(np.sum((arr - mean)**2 / earr**2))
            dof = len(arr) - 1
            result.update({
                f'{band}_n_pts': len(mags),
                f'{band}_mean': round(float(mean), 4),
                f'{band}_std': round(float(np.std(arr)), 4),
                f'{band}_chi2': round(chi2, 2),
                f'{band}_dof': dof,
                f'{band}_chi2_per_dof': round(chi2/dof, 3) if dof > 0 else None,
                f'{band}_variable': bool(chi2 > 3 * dof),
                f'{band}_amplitude': round(float(np.max(arr) - np.min(arr)), 4),
            })
        else:
            result.update({f'{band}_n_pts': len(mags), f'{band}_variable': False})

    result['is_variable'] = result.get('w1_variable', False) or result.get('w2_variable', False)
    return result


def main():
    print("=" * 70)
    print(f"NEOWISE/AllWISE Cross-Match — SILVER TIER (top {MAX_SILVER})")
    print(f"Started: {datetime.now().isoformat()}")
    print("=" * 70)

    with open(SILVER_CATALOG) as f:
        silver_all = json.load(f)
    print(f"Total silver catalog: {len(silver_all)}")

    # Already sorted by score, take top N
    silver = silver_all[:MAX_SILVER]
    print(f"Processing top {len(silver)} (score range: "
          f"{silver[-1]['anomaly_score']:.2f} - {silver[0]['anomaly_score']:.2f})")

    results = []
    for i, obj in enumerate(silver):
        ra, dec = obj['ra'], obj['dec']
        tid = obj['targetid']
        score = obj.get('anomaly_score', 0)
        print(f"  [{i+1}/{len(silver)}] SILVER tid={tid} "
              f"(RA={ra:.4f}, Dec={dec:.4f}, z={obj.get('z','?')}, "
              f"score={score:.2f}, type={obj.get('spectype','?')})", end='')

        result = {
            'targetid': tid, 'ra': ra, 'dec': dec,
            'z': obj.get('z'), 'anomaly_score': score,
            'spectype': obj.get('spectype'), 'tier': 'silver',
        }

        allwise = query_vizier_allwise(ra, dec)
        time.sleep(QUERY_INTERVAL)

        if allwise:
            result['allwise_match'] = True
            result['allwise_id'] = allwise.get('AllWISE')
            result['w1mag'] = allwise.get('W1mag')
            result['w2mag'] = allwise.get('W2mag')
            result['w3mag'] = allwise.get('W3mag')
            result['w4mag'] = allwise.get('W4mag')
            if allwise.get('W1mag') is not None and allwise.get('W2mag') is not None:
                try:
                    w1w2 = float(allwise['W1mag']) - float(allwise['W2mag'])
                    result['w1w2_color'] = round(w1w2, 3)
                    result['agn_ir_color'] = w1w2 > 0.8
                except: pass

            nw_ra = float(allwise.get('RAJ2000', ra))
            nw_dec = float(allwise.get('DEJ2000', dec))
            lc = query_neowise_gator(nw_ra, nw_dec)
            time.sleep(QUERY_INTERVAL)

            if lc:
                var = compute_variability(lc)
                if var:
                    result['neowise_match'] = True
                    result.update(var)
                    flag = " *** VARIABLE ***" if var['is_variable'] else ""
                    print(f" -> {var['n_epochs']}ep chi2/dof W1={var.get('w1_chi2_per_dof','?')} "
                          f"W2={var.get('w2_chi2_per_dof','?')}{flag}")
                else:
                    result['neowise_match'] = True
                    result['is_variable'] = False
                    print(f" -> {len(lc)} epochs (insuff)")
            else:
                result['neowise_match'] = False
                result['is_variable'] = False
                print(f" -> no NEOWISE")
        else:
            result['allwise_match'] = False
            result['neowise_match'] = False
            result['is_variable'] = False
            print(f" -> no AllWISE")

        results.append(result)

        if (i + 1) % 25 == 0:
            n_var = sum(1 for r in results if r.get('is_variable'))
            print(f"  --- Checkpoint: {i+1}/{len(silver)}, {n_var} variable ---")
            with open(os.path.join(OUT_DIR, "silver_crossmatch_checkpoint.json"), 'w') as f:
                json.dump(results, f, indent=2, default=str)

    # Save results
    silver_results_path = os.path.join(OUT_DIR, "silver_crossmatch.json")
    with open(silver_results_path, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nSaved: {silver_results_path}")

    variable = [r for r in results if r.get('is_variable', False)]
    silver_var_path = os.path.join(OUT_DIR, "silver_variable_anomalies.json")
    with open(silver_var_path, 'w') as f:
        json.dump(variable, f, indent=2, default=str)
    print(f"Saved: {silver_var_path} ({len(variable)} objects)")

    # Merge gold + silver variable
    with open(os.path.join(OUT_DIR, "variable_anomalies.json")) as f:
        gold_var = json.load(f)
    all_var = gold_var + variable
    all_var_path = os.path.join(OUT_DIR, "all_variable_anomalies.json")
    with open(all_var_path, 'w') as f:
        json.dump(all_var, f, indent=2, default=str)
    print(f"Saved merged: {all_var_path} ({len(all_var)} total variable)")

    # Summary
    n = len(results)
    n_aw = sum(1 for r in results if r.get('allwise_match'))
    n_nw = sum(1 for r in results if r.get('neowise_match'))
    n_var = len(variable)
    print(f"\n{'='*70}")
    print(f"SILVER TIER SUMMARY")
    print(f"{'='*70}")
    print(f"Processed:        {n}")
    print(f"AllWISE matches:  {n_aw} ({100*n_aw/n:.1f}%)")
    print(f"NEOWISE det:      {n_nw} ({100*n_nw/n:.1f}%)")
    print(f"Variable:         {n_var} ({100*n_var/n:.1f}%)")

    if variable:
        print(f"\nTop silver variables:")
        vs = sorted(variable, key=lambda x: max(
            x.get('w1_chi2_per_dof',0) or 0,
            x.get('w2_chi2_per_dof',0) or 0
        ), reverse=True)
        for v in vs[:10]:
            mc = max(v.get('w1_chi2_per_dof',0) or 0, v.get('w2_chi2_per_dof',0) or 0)
            print(f"  tid={v['targetid']} z={v.get('z','?')} type={v.get('spectype','?')} "
                  f"score={v.get('anomaly_score',0):.2f} chi2/dof={mc:.1f} epochs={v.get('n_epochs','?')}")

    # Update combined summary
    summary = {
        'timestamp': datetime.now().isoformat(),
        'gold_processed': 83,
        'gold_variable': len(gold_var),
        'silver_processed': n,
        'silver_variable': n_var,
        'total_variable': len(all_var),
    }
    with open(os.path.join(OUT_DIR, "combined_summary.json"), 'w') as f:
        json.dump(summary, f, indent=2)

    print(f"\nFinished: {datetime.now().isoformat()}")


if __name__ == "__main__":
    main()
