#!/usr/bin/env python3
"""
Pipeline 1 Step 2: Cross-match DESI DR1 anomalies against SIMBAD, NED, and Legacy Survey.

This script takes the 195,829 anomalies from the H200 run and cross-matches the top
objects against astronomical databases to determine:
1. Which are known objects (in SIMBAD/NED)
2. What types they are (QSO, AGN, star, galaxy, etc.)
3. Which are genuinely new / previously unidentified
4. Which have photometric data from Legacy Survey / unWISE

References:
- Liang et al. (2023) - Prior DESI EDR anomaly work (arXiv:2307.07664)
- Nicolaou et al. (2026) - Prior DESI EDR VAE work (arXiv:2506.17376)
"""

import json
import os
import sys
import time
import urllib.request
import urllib.parse
import urllib.error
from collections import Counter

# ============================================================
# Configuration
# ============================================================

ANOMALY_FILE = os.path.join(os.path.dirname(__file__),
    '../outputs/desi_dr1/dr1_all_anomalies.json')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '../outputs/desi_dr1')
MATCH_RADIUS_ARCSEC = 5.0  # arcseconds
TOP_N = 500  # Cross-match top N by score
SIMBAD_DELAY = 0.5  # seconds between queries (rate limiting)

# ============================================================
# Load anomaly catalog
# ============================================================

print("=" * 70)
print("PIPELINE 1 STEP 2: Cross-Match Anomalies")
print("=" * 70)

with open(ANOMALY_FILE) as f:
    anomalies = json.load(f)

print(f"Loaded {len(anomalies)} anomalies")

# Sort by score descending
anomalies.sort(key=lambda x: -x['score'])
top = anomalies[:TOP_N]
print(f"Cross-matching top {TOP_N} (scores {top[0]['score']:.1f} to {top[-1]['score']:.1f})")

# ============================================================
# SIMBAD cross-match via TAP
# ============================================================

def query_simbad(ra, dec, radius_arcsec=5.0):
    """Query SIMBAD by coordinates. Returns list of matches."""
    url = "https://simbad.cds.unistra.fr/simbad/sim-coo"
    params = {
        'Coord': f'{ra} {dec}',
        'CooFrame': 'ICRS',
        'CooEpoch': '2000',
        'CooEqui': '2000',
        'CooDefinedFrames': 'none',
        'Radius': str(radius_arcsec),
        'Radius.unit': 'arcsec',
        'submit': 'submit query',
        'output.format': 'ASCII',
    }
    query_url = url + '?' + urllib.parse.urlencode(params)
    try:
        req = urllib.request.Request(query_url, headers={'User-Agent': 'BigBounce/1.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            text = resp.read().decode('utf-8', errors='replace')
        # Parse SIMBAD ASCII response
        if 'No astronomical object found' in text:
            return None
        # Try to extract object type and name
        lines = text.split('\n')
        for line in lines:
            if 'Object' in line and '---' not in line:
                # Extract object name and type
                parts = line.strip().split('--')
                if len(parts) >= 2:
                    return {'name': parts[0].strip(), 'type': parts[1].strip(), 'raw': line.strip()}
                return {'name': line.strip(), 'type': 'unknown', 'raw': line.strip()}
        return None
    except Exception as e:
        return {'error': str(e)}


def query_simbad_tap(ra, dec, radius_arcsec=5.0):
    """Query SIMBAD via TAP for more structured results."""
    radius_deg = radius_arcsec / 3600.0
    adql = f"""
    SELECT TOP 3 main_id, otype, ra, dec, rvz_redshift, rvz_type
    FROM basic
    WHERE CONTAINS(POINT('ICRS', ra, dec), CIRCLE('ICRS', {ra}, {dec}, {radius_deg})) = 1
    ORDER BY rvz_redshift DESC
    """
    url = "https://simbad.u-strasbg.fr/simbad/sim-tap/sync"
    params = {
        'request': 'doQuery',
        'lang': 'adql',
        'format': 'json',
        'query': adql
    }
    try:
        data = urllib.parse.urlencode(params).encode()
        req = urllib.request.Request(url, data=data, headers={'User-Agent': 'BigBounce/1.0'})
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode())
        if 'data' in result and len(result['data']) > 0:
            row = result['data'][0]
            columns = result.get('metadata', [])
            col_names = [c.get('name', f'col{i}') for i, c in enumerate(columns)]
            obj = dict(zip(col_names, row))
            return {
                'name': obj.get('main_id', 'unknown'),
                'type': obj.get('otype', 'unknown'),
                'redshift': obj.get('rvz_redshift'),
                'matched_ra': obj.get('ra'),
                'matched_dec': obj.get('dec'),
            }
        return None
    except Exception as e:
        return {'error': str(e)}


def query_legacy_survey(ra, dec):
    """Get Legacy Survey DR10 catalog info at position."""
    url = f"https://www.legacysurvey.org/viewer/cat.json?ra={ra}&dec={dec}&zoom=16"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'BigBounce/1.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            result = json.loads(resp.read().decode())
        if result and len(result) > 0:
            # Find closest object
            closest = result[0]
            return {
                'ls_type': closest.get('type', 'unknown'),
                'ls_mag_r': closest.get('mag_r'),
                'ls_mag_g': closest.get('mag_g'),
                'ls_mag_z': closest.get('mag_z'),
            }
        return None
    except:
        return None


# ============================================================
# Run cross-match
# ============================================================

print(f"\nQuerying SIMBAD TAP for top {TOP_N} anomalies...")
print(f"Rate limit: {SIMBAD_DELAY}s between queries")
print()

results = []
simbad_matches = 0
simbad_misses = 0
simbad_errors = 0
type_counts = Counter()

for i, anom in enumerate(top):
    ra, dec = anom['ra'], anom['dec']
    score = anom['score']

    # Query SIMBAD
    match = query_simbad_tap(ra, dec, MATCH_RADIUS_ARCSEC)
    time.sleep(SIMBAD_DELAY)

    result = {
        'rank': i + 1,
        'tid': anom['tid'],
        'ra': ra,
        'dec': dec,
        'score': score,
        'worst': anom['worst'],
        'rB': anom['rB'],
        'rR': anom['rR'],
        'rZ': anom['rZ'],
        'legacy_url': f"https://www.legacysurvey.org/viewer?ra={ra:.6f}&dec={dec:.6f}&layer=ls-dr10&zoom=15",
    }

    if match and 'error' not in match:
        simbad_matches += 1
        result['simbad_match'] = True
        result['simbad_name'] = match.get('name', 'unknown')
        result['simbad_type'] = match.get('type', 'unknown')
        result['simbad_redshift'] = match.get('redshift')
        otype = match.get('type', 'unknown')
        type_counts[otype] += 1
        status = 'KNOWN'
    elif match and 'error' in match:
        simbad_errors += 1
        result['simbad_match'] = False
        result['simbad_error'] = match['error']
        status = 'ERROR'
    else:
        simbad_misses += 1
        result['simbad_match'] = False
        status = 'NEW'
        type_counts['NOT_IN_SIMBAD'] += 1

    result['status'] = status
    results.append(result)

    if (i + 1) % 25 == 0 or i < 10:
        z_str = f"z={match.get('redshift', '?')}" if match and 'redshift' in match else ""
        name = match.get('name', '') if match and 'error' not in match else ''
        print(f"  [{i+1}/{TOP_N}] score={score:.1f} | {status:6s} | {name[:30]:30s} | {z_str}")

# ============================================================
# Summary
# ============================================================

print()
print("=" * 70)
print("CROSS-MATCH SUMMARY")
print("=" * 70)
print(f"Total queried: {len(results)}")
print(f"SIMBAD matches: {simbad_matches} ({100*simbad_matches/len(results):.1f}%)")
print(f"NOT in SIMBAD: {simbad_misses} ({100*simbad_misses/len(results):.1f}%)")
print(f"Errors: {simbad_errors}")
print()
print("Object types found:")
for otype, count in type_counts.most_common(20):
    print(f"  {otype:25s}: {count}")

# Classify by our categories
high_z_qso = [r for r in results if r.get('simbad_type') in ('QSO', 'AGN', 'Sy1', 'Sy2', 'BLA', 'BLL')
              and r.get('simbad_redshift') and r['simbad_redshift'] > 1.5]
any_qso = [r for r in results if r.get('simbad_type') in ('QSO', 'AGN', 'Sy1', 'Sy2', 'BLA', 'BLL')]
stars = [r for r in results if r.get('simbad_type') in ('Star', '*', 'PM*', 'V*', 'EB*', 'WD*', 'pMS*')]
galaxies = [r for r in results if r.get('simbad_type') in ('G', 'GiG', 'GiP', 'EmG', 'SBG', 'AG?')]
new_objects = [r for r in results if r['status'] == 'NEW']

print()
print("CLASSIFICATION:")
print(f"  High-z QSOs (z > 1.5): {len(high_z_qso)}")
print(f"  Any QSO/AGN:           {len(any_qso)}")
print(f"  Stars:                 {len(stars)}")
print(f"  Galaxies:              {len(galaxies)}")
print(f"  NOT IN SIMBAD (new?):  {len(new_objects)}")

# ============================================================
# Save results
# ============================================================

output = {
    'metadata': {
        'total_anomalies': len(anomalies),
        'top_n_queried': TOP_N,
        'match_radius_arcsec': MATCH_RADIUS_ARCSEC,
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime()),
        'simbad_matches': simbad_matches,
        'simbad_misses': simbad_misses,
        'simbad_errors': simbad_errors,
    },
    'type_counts': dict(type_counts.most_common()),
    'classification': {
        'high_z_qso': len(high_z_qso),
        'any_qso_agn': len(any_qso),
        'stars': len(stars),
        'galaxies': len(galaxies),
        'not_in_simbad': len(new_objects),
    },
    'results': results,
}

out_path = os.path.join(OUTPUT_DIR, 'cross_match_results.json')
with open(out_path, 'w') as f:
    json.dump(output, f, indent=2, default=str)
print(f"\nSaved: {out_path}")

# Save top NEW objects separately
new_path = os.path.join(OUTPUT_DIR, 'new_objects_not_in_simbad.json')
with open(new_path, 'w') as f:
    json.dump(new_objects, f, indent=2, default=str)
print(f"Saved: {new_path} ({len(new_objects)} objects)")

print()
print("Next: Step 3 (classification) and Step 4 (bias validation)")
print("=" * 70)
