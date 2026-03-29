#!/usr/bin/env python3
"""
Silver-tier anomaly cross-match against SIMBAD (Harvard mirror) and NED.
2,145 objects with anomaly_score > 3.0 and max_SNR > 0.5.

Uses SIMBAD script interface (TAP is broken) and NED XML.
Runs SIMBAD and NED in parallel threads to halve wall-clock time.
Checkpoints every 50 queries for resume capability.
"""

import pandas as pd
import numpy as np
import os, glob, json, time, threading
import requests
from xml.etree import ElementTree
from datetime import datetime

# Paths
BASE = '/Users/houstongolden/Desktop/CODE_2026/bigbounce/pipelines/p1_highz_tracers'
DEDUPED = os.path.join(BASE, 'outputs/enhanced_18M_deduped')
OUTPUT = os.path.join(BASE, 'outputs/silver_crossmatch')
CHECKPOINT_SIMBAD = os.path.join(OUTPUT, 'checkpoint_simbad.json')
CHECKPOINT_NED = os.path.join(OUTPUT, 'checkpoint_ned.json')

# Endpoints
SIMBAD_SCRIPT = 'https://simbad.harvard.edu/simbad/sim-script'
NED_URL = 'https://ned.ipac.caltech.edu/cgi-bin/objsearch'

# Search radius
NED_RADIUS_ARCMIN = 0.08  # ~5 arcsec


def extract_silver():
    """Extract 2,145 silver-tier anomalies from the deduped catalog."""
    files = sorted(glob.glob(os.path.join(DEDUPED, 'desi_dr1_catalog_batch_*.parquet')))
    cols = ['targetid', 'target_ra', 'target_dec', 'z', 'anomaly_score', 'spectype', 'zwarn',
            'median_coadd_snr_b', 'median_coadd_snr_r', 'median_coadd_snr_z']
    dfs = []
    for f in files:
        df = pd.read_parquet(f, columns=cols)
        df['max_snr'] = df[['median_coadd_snr_b', 'median_coadd_snr_r', 'median_coadd_snr_z']].max(axis=1)
        mask = (df['anomaly_score'] > 3.0) & (df['max_snr'] > 0.5)
        filtered = df[mask]
        if len(filtered) > 0:
            dfs.append(filtered)
    silver = pd.concat(dfs, ignore_index=True)
    silver = silver.sort_values('anomaly_score', ascending=False).reset_index(drop=True)
    return silver


def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f)

def load_json(path):
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {}


# ─── SIMBAD via script interface ───

def query_simbad_all(objects):
    """
    Query SIMBAD via the script interface at Harvard.
    One query per object, rate limited to 1/sec.
    """
    results = load_json(CHECKPOINT_SIMBAD)
    session = requests.Session()
    session.headers.update({'User-Agent': 'BigBounce-CrossMatch/1.0 (houston@hubify.com)'})

    total = len(objects)
    queried = 0
    errors = 0

    for i, (tid, ra, dec) in enumerate(objects):
        tid_str = str(tid)
        if tid_str in results:
            continue

        # SIMBAD script: query cone, return closest match only (nbobj=1)
        script = (
            'output console=off script=off error=off\n'
            'format object "%MAIN_ID|%OTYPE(V)|%OTYPE(S)"\n'
            f'query coo {ra} {dec:+f} radius=5s frame=ICRS nbobj=1'
        )

        try:
            resp = session.post(SIMBAD_SCRIPT, data={'script': script}, timeout=30)

            if resp.status_code == 200:
                text = resp.text.strip()
                if text and '|' in text:
                    # Successful match: "MAIN_ID|otype_verbose|otype_short"
                    line = text.split('\n')[0].strip()
                    parts = line.split('|')
                    if len(parts) >= 3:
                        results[tid_str] = {
                            'found': True,
                            'main_id': parts[0].strip(),
                            'otype_txt': parts[1].strip(),
                            'otype': parts[2].strip()
                        }
                    else:
                        results[tid_str] = {'found': False}
                else:
                    results[tid_str] = {'found': False}
            else:
                results[tid_str] = {'found': False, 'error': f'HTTP {resp.status_code}'}
                errors += 1

        except requests.exceptions.Timeout:
            results[tid_str] = {'found': False, 'error': 'timeout'}
            errors += 1
        except requests.exceptions.ConnectionError:
            results[tid_str] = {'found': False, 'error': 'connection_error'}
            errors += 1
        except Exception as e:
            results[tid_str] = {'found': False, 'error': str(e)}
            errors += 1

        queried += 1

        if queried % 50 == 0:
            found = sum(1 for v in results.values() if v.get('found'))
            print(f"  SIMBAD: {len(results)}/{total} ({100*len(results)/total:.1f}%) | found={found} | errors={errors}")
            save_json(CHECKPOINT_SIMBAD, results)

        time.sleep(1.0)

    # Final save
    save_json(CHECKPOINT_SIMBAD, results)
    found = sum(1 for v in results.values() if v.get('found'))
    print(f"  SIMBAD DONE: {len(results)}/{total} | found={found} | errors={errors}")
    return results


# ─── NED via XML ───

def query_ned_all(objects):
    """
    Query NED one at a time, rate limited to 1/sec.
    """
    results = load_json(CHECKPOINT_NED)
    session = requests.Session()
    session.headers.update({'User-Agent': 'BigBounce-CrossMatch/1.0 (houston@hubify.com)'})

    total = len(objects)
    queried = 0
    errors = 0

    for i, (tid, ra, dec) in enumerate(objects):
        tid_str = str(tid)
        if tid_str in results:
            continue

        try:
            resp = session.get(NED_URL, params={
                'search_type': 'Near Position Search',
                'in_csys': 'Equatorial',
                'in_equinox': 'J2000.0',
                'lon': f'{ra}d',
                'lat': f'{dec}d',
                'radius': str(NED_RADIUS_ARCMIN),
                'out_csys': 'Equatorial',
                'out_equinox': 'J2000.0',
                'of': 'xml_main'
            }, timeout=30)

            if resp.status_code == 200:
                try:
                    root = ElementTree.fromstring(resp.content)
                    rows = root.findall('.//TR')
                    if rows:
                        cells = rows[0].findall('TD')
                        if cells and len(cells) >= 5:
                            obj_name = (cells[1].text or '').strip()
                            obj_type = (cells[4].text or '').strip()
                            ned_ra = (cells[2].text or '').strip()
                            ned_dec = (cells[3].text or '').strip()
                            sep = (cells[9].text or '').strip() if len(cells) > 9 else ''
                            results[tid_str] = {
                                'found': True,
                                'ned_name': obj_name,
                                'ned_type': obj_type,
                                'ned_ra': ned_ra,
                                'ned_dec': ned_dec,
                                'sep_arcmin': sep,
                                'n_matches': len(rows)
                            }
                        else:
                            results[tid_str] = {'found': False}
                    else:
                        results[tid_str] = {'found': False}
                except ElementTree.ParseError:
                    if 'no object' in resp.text.lower():
                        results[tid_str] = {'found': False}
                    else:
                        results[tid_str] = {'found': False, 'error': 'xml_parse_error'}
                        errors += 1
            else:
                results[tid_str] = {'found': False, 'error': f'HTTP {resp.status_code}'}
                errors += 1

        except requests.exceptions.Timeout:
            results[tid_str] = {'found': False, 'error': 'timeout'}
            errors += 1
        except requests.exceptions.ConnectionError:
            results[tid_str] = {'found': False, 'error': 'connection_error'}
            errors += 1
        except Exception as e:
            results[tid_str] = {'found': False, 'error': str(e)}
            errors += 1

        queried += 1

        if queried % 50 == 0:
            found = sum(1 for v in results.values() if v.get('found'))
            print(f"  NED:    {len(results)}/{total} ({100*len(results)/total:.1f}%) | found={found} | errors={errors}")
            save_json(CHECKPOINT_NED, results)

        time.sleep(1.0)

    # Final save
    save_json(CHECKPOINT_NED, results)
    found = sum(1 for v in results.values() if v.get('found'))
    print(f"  NED DONE:    {len(results)}/{total} | found={found} | errors={errors}")
    return results


def main():
    print("=" * 60)
    print("Silver-Tier Anomaly Cross-Match")
    print(f"Started: {datetime.now().isoformat()}")
    print("=" * 60)

    # Step 1: Extract silver tier
    print("\n[Step 1] Extracting silver-tier anomalies...")
    silver = extract_silver()
    print(f"  {len(silver)} objects to cross-match")
    print(f"  Spectype: {dict(silver.spectype.value_counts())}")
    print(f"  Score range: {silver.anomaly_score.min():.2f} - {silver.anomaly_score.max():.2f}")

    objects = list(zip(
        silver['targetid'].values,
        silver['target_ra'].values,
        silver['target_dec'].values
    ))

    # Step 2 & 3: Query SIMBAD and NED in parallel threads
    print(f"\n[Step 2+3] Querying SIMBAD and NED in parallel — {len(objects)} objects each...")
    print(f"  Estimated wall-clock: ~{len(objects)//60} minutes (parallel)")

    simbad_results = {}
    ned_results = {}

    def run_simbad():
        nonlocal simbad_results
        simbad_results = query_simbad_all(objects)

    def run_ned():
        nonlocal ned_results
        ned_results = query_ned_all(objects)

    t_simbad = threading.Thread(target=run_simbad, name='simbad')
    t_ned = threading.Thread(target=run_ned, name='ned')

    t_simbad.start()
    t_ned.start()

    t_simbad.join()
    t_ned.join()

    # Step 4: Combine and save
    print("\n[Step 4] Combining results...")

    full_results = []
    for _, row in silver.iterrows():
        tid_str = str(int(row['targetid']))
        entry = {
            'targetid': int(row['targetid']),
            'target_ra': float(row['target_ra']),
            'target_dec': float(row['target_dec']),
            'z': float(row['z']),
            'anomaly_score': float(row['anomaly_score']),
            'spectype': row['spectype'],
            'zwarn': int(row['zwarn']),
            'max_snr': float(row['max_snr']),
            'simbad': simbad_results.get(tid_str, {'found': False, 'error': 'not_queried'}),
            'ned': ned_results.get(tid_str, {'found': False, 'error': 'not_queried'})
        }
        full_results.append(entry)

    with open(os.path.join(OUTPUT, 'silver_crossmatch_results.json'), 'w') as f:
        json.dump(full_results, f, indent=2, default=str)
    print(f"  Saved: silver_crossmatch_results.json ({len(full_results)} entries)")

    # Step 5: Summary
    print("\n[Step 5] Computing summary...")

    in_simbad = sum(1 for r in full_results if r['simbad'].get('found'))
    in_ned = sum(1 for r in full_results if r['ned'].get('found'))
    in_both = sum(1 for r in full_results if r['simbad'].get('found') and r['ned'].get('found'))
    in_either = sum(1 for r in full_results if r['simbad'].get('found') or r['ned'].get('found'))
    in_neither = sum(1 for r in full_results if not r['simbad'].get('found') and not r['ned'].get('found'))

    simbad_errors = sum(1 for r in full_results if 'error' in r['simbad'])
    ned_errors = sum(1 for r in full_results if 'error' in r['ned'])

    # Type breakdowns
    simbad_types = {}
    for r in full_results:
        if r['simbad'].get('found'):
            otype = r['simbad'].get('otype_txt', 'Unknown')
            simbad_types[otype] = simbad_types.get(otype, 0) + 1

    ned_types = {}
    for r in full_results:
        if r['ned'].get('found'):
            ntype = r['ned'].get('ned_type', 'Unknown')
            ned_types[ntype] = ned_types.get(ntype, 0) + 1

    uncataloged_by_spectype = {}
    for r in full_results:
        if not r['simbad'].get('found') and not r['ned'].get('found'):
            st = r['spectype']
            uncataloged_by_spectype[st] = uncataloged_by_spectype.get(st, 0) + 1

    uncataloged_scores = [r['anomaly_score'] for r in full_results
                          if not r['simbad'].get('found') and not r['ned'].get('found')]

    # Cataloged by spectype
    cataloged_by_spectype = {}
    for r in full_results:
        if r['simbad'].get('found') or r['ned'].get('found'):
            st = r['spectype']
            cataloged_by_spectype[st] = cataloged_by_spectype.get(st, 0) + 1

    summary = {
        'total_objects': len(full_results),
        'in_simbad': in_simbad,
        'in_ned': in_ned,
        'in_both': in_both,
        'in_either': in_either,
        'in_neither_uncataloged': in_neither,
        'fraction_in_simbad': round(in_simbad / len(full_results), 4),
        'fraction_in_ned': round(in_ned / len(full_results), 4),
        'fraction_uncataloged': round(in_neither / len(full_results), 4),
        'simbad_errors': simbad_errors,
        'ned_errors': ned_errors,
        'simbad_type_breakdown': dict(sorted(simbad_types.items(), key=lambda x: -x[1])),
        'ned_type_breakdown': dict(sorted(ned_types.items(), key=lambda x: -x[1])),
        'uncataloged_by_spectype': uncataloged_by_spectype,
        'cataloged_by_spectype': cataloged_by_spectype,
        'uncataloged_score_stats': {
            'count': len(uncataloged_scores),
            'mean': round(np.mean(uncataloged_scores), 2) if uncataloged_scores else 0,
            'median': round(np.median(uncataloged_scores), 2) if uncataloged_scores else 0,
            'max': round(max(uncataloged_scores), 2) if uncataloged_scores else 0,
            'min': round(min(uncataloged_scores), 2) if uncataloged_scores else 0
        },
        'timestamp': datetime.now().isoformat()
    }

    with open(os.path.join(OUTPUT, 'silver_crossmatch_summary.json'), 'w') as f:
        json.dump(summary, f, indent=2)
    print(f"  Saved: silver_crossmatch_summary.json")

    # Print summary
    print("\n" + "=" * 60)
    print("CROSS-MATCH SUMMARY")
    print("=" * 60)
    print(f"Total silver-tier anomalies: {len(full_results)}")
    print()
    print(f"In SIMBAD:     {in_simbad:4d} ({100*in_simbad/len(full_results):.1f}%)")
    print(f"In NED:        {in_ned:4d} ({100*in_ned/len(full_results):.1f}%)")
    print(f"In both:       {in_both:4d} ({100*in_both/len(full_results):.1f}%)")
    print(f"In either:     {in_either:4d} ({100*in_either/len(full_results):.1f}%)")
    print(f"In NEITHER:    {in_neither:4d} ({100*in_neither/len(full_results):.1f}%) <-- genuinely uncataloged")
    print()
    print(f"SIMBAD errors: {simbad_errors}")
    print(f"NED errors:    {ned_errors}")
    print()
    if simbad_types:
        print("SIMBAD type breakdown (top 20):")
        for t, c in sorted(simbad_types.items(), key=lambda x: -x[1])[:20]:
            print(f"  {t:35s}: {c:4d}")
    print()
    if ned_types:
        print("NED type breakdown (top 20):")
        for t, c in sorted(ned_types.items(), key=lambda x: -x[1])[:20]:
            print(f"  {t:35s}: {c:4d}")
    print()
    print("Uncataloged by DESI spectype:")
    for st, c in sorted(uncataloged_by_spectype.items(), key=lambda x: -x[1]):
        print(f"  {st:10s}: {c}")
    print()
    print("Cataloged by DESI spectype:")
    for st, c in sorted(cataloged_by_spectype.items(), key=lambda x: -x[1]):
        print(f"  {st:10s}: {c}")
    if uncataloged_scores:
        print(f"\nUncataloged anomaly score stats:")
        print(f"  Mean:   {np.mean(uncataloged_scores):.2f}")
        print(f"  Median: {np.median(uncataloged_scores):.2f}")
        print(f"  Max:    {max(uncataloged_scores):.2f}")
        print(f"  Min:    {min(uncataloged_scores):.2f}")

    print(f"\nCompleted: {datetime.now().isoformat()}")

    # Cleanup checkpoints
    for cp in [CHECKPOINT_SIMBAD, CHECKPOINT_NED]:
        if os.path.exists(cp):
            os.remove(cp)


if __name__ == '__main__':
    main()
