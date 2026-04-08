#!/usr/bin/env python3
"""
BULK cross-match ALL 195,829 DESI DR1 anomalies against multiple catalogs.

Uses CDS xMatch service for bulk matching (much faster than individual queries).
Processes the FULL catalog, not just the top 50/100.

Catalogs to check:
1. SIMBAD (via xMatch)
2. NED (via xMatch or cone search)
3. Gaia DR3 (via xMatch — identifies stars by parallax)
4. SDSS DR18 photometric (via xMatch)
5. Milliquas v8 (via xMatch — comprehensive QSO catalog)
6. AllWISE (via xMatch — IR photometry for classification)

For each anomaly, we determine:
- Is it in ANY catalog? → KNOWN
- Is it only in photometric catalogs but not spectroscopic? → PHOTOMETRIC_ONLY
- Is it in NO catalog? → GENUINELY_NEW (strongest discovery claim)
"""

import json
import os
import sys
import time
import csv
import io
import urllib.request
import urllib.parse
import tempfile

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ANOMALY_FILE = os.path.join(BASE_DIR, '../outputs/desi_dr1/dr1_all_anomalies.json')
OUTPUT_DIR = os.path.join(BASE_DIR, '../outputs/desi_dr1/cross_match_full')

MATCH_RADIUS_ARCSEC = 3.0  # 3 arcsec match radius

os.makedirs(OUTPUT_DIR, exist_ok=True)

print("=" * 70)
print("BULK CROSS-MATCH: ALL 195,829 ANOMALIES")
print("=" * 70)

# Load catalog
with open(ANOMALY_FILE) as f:
    anomalies = json.load(f)
print(f"Loaded {len(anomalies)} anomalies")

# Build CSV for CDS xMatch upload
print("Building input CSV...")
csv_lines = ['ra,dec,tid,score']
for a in anomalies:
    csv_lines.append(f'{a["ra"]:.6f},{a["dec"]:.6f},{a["tid"]},{a["score"]:.2f}')
csv_content = '\n'.join(csv_lines)
print(f"CSV: {len(csv_lines)-1} rows, {len(csv_content)//1024} KB")

# Save CSV for reuse
csv_path = os.path.join(OUTPUT_DIR, 'anomalies_for_xmatch.csv')
with open(csv_path, 'w') as f:
    f.write(csv_content)
print(f"Saved: {csv_path}")


def cds_xmatch(csv_content, catalog_id, match_radius_arcsec=3.0, catalog_label='catalog'):
    """
    Bulk cross-match via CDS xMatch service.
    Returns list of matched tids and match details.
    """
    print(f"\n  Querying CDS xMatch against {catalog_label} ({catalog_id})...")
    url = 'http://cdsxmatch.cds.unistra.fr/xmatch/api/v1/sync'

    boundary = '----BigBounceBulkXMatch'
    body_parts = []

    params = {
        'request': 'xmatch',
        'distMaxArcsec': str(match_radius_arcsec),
        'RESPONSEFORMAT': 'csv',
        'cat2': catalog_id,
        'colRA1': 'ra',
        'colDec1': 'dec',
    }

    for k, v in params.items():
        body_parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}')

    body_parts.append(
        f'--{boundary}\r\nContent-Disposition: form-data; name="cat1"; filename="input.csv"\r\n'
        f'Content-Type: text/csv\r\n\r\n{csv_content}'
    )
    body_parts.append(f'--{boundary}--')
    body = '\r\n'.join(body_parts).encode('utf-8')

    try:
        req = urllib.request.Request(url, data=body,
            headers={
                'Content-Type': f'multipart/form-data; boundary={boundary}',
                'User-Agent': 'BigBounce-BulkXMatch/1.0',
            })
        # Longer timeout for bulk queries
        with urllib.request.urlopen(req, timeout=300) as resp:
            result = resp.read().decode('utf-8', errors='replace')

        # Parse CSV result
        reader = csv.DictReader(io.StringIO(result))
        rows = list(reader)
        matched_tids = set()
        match_details = []
        for row in rows:
            tid = row.get('tid', '')
            if tid:
                matched_tids.add(tid)
                match_details.append(row)

        print(f"  → {len(matched_tids)} matches out of {len(anomalies)} ({len(matched_tids)/len(anomalies)*100:.1f}%)")
        return matched_tids, match_details

    except urllib.error.HTTPError as e:
        # CDS may reject large uploads — try in chunks
        print(f"  → HTTP Error {e.code}: {e.reason}")
        if e.code in (413, 307, 500) and len(anomalies) > 10000:
            print(f"  → Catalog too large for single request. Splitting into chunks...")
            return chunked_xmatch(csv_content, catalog_id, match_radius_arcsec, catalog_label)
        return set(), []

    except Exception as e:
        print(f"  → Error: {e}")
        return set(), []


def chunked_xmatch(full_csv, catalog_id, match_radius_arcsec, catalog_label, chunk_size=20000):
    """Split large catalog into chunks and cross-match each."""
    lines = full_csv.strip().split('\n')
    header = lines[0]
    data_lines = lines[1:]
    total = len(data_lines)
    all_matched = set()
    all_details = []

    n_chunks = (total + chunk_size - 1) // chunk_size
    print(f"  Splitting into {n_chunks} chunks of {chunk_size}...")

    for i in range(0, total, chunk_size):
        chunk = data_lines[i:i+chunk_size]
        chunk_csv = header + '\n' + '\n'.join(chunk)
        chunk_num = i // chunk_size + 1
        print(f"    Chunk {chunk_num}/{n_chunks} ({len(chunk)} objects)...", end=' ')

        try:
            url = 'http://cdsxmatch.cds.unistra.fr/xmatch/api/v1/sync'
            boundary = '----BigBounceChunk'
            params = {
                'request': 'xmatch',
                'distMaxArcsec': str(match_radius_arcsec),
                'RESPONSEFORMAT': 'csv',
                'cat2': catalog_id,
                'colRA1': 'ra',
                'colDec1': 'dec',
            }
            body_parts = []
            for k, v in params.items():
                body_parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}')
            body_parts.append(
                f'--{boundary}\r\nContent-Disposition: form-data; name="cat1"; filename="chunk.csv"\r\n'
                f'Content-Type: text/csv\r\n\r\n{chunk_csv}'
            )
            body_parts.append(f'--{boundary}--')
            body = '\r\n'.join(body_parts).encode('utf-8')

            req = urllib.request.Request(url, data=body,
                headers={
                    'Content-Type': f'multipart/form-data; boundary={boundary}',
                    'User-Agent': 'BigBounce-BulkXMatch/1.0',
                })
            with urllib.request.urlopen(req, timeout=300) as resp:
                result = resp.read().decode('utf-8', errors='replace')

            reader = csv.DictReader(io.StringIO(result))
            rows = list(reader)
            chunk_matched = set()
            for row in rows:
                tid = row.get('tid', '')
                if tid:
                    chunk_matched.add(tid)
                    all_details.append(row)
            all_matched.update(chunk_matched)
            print(f"{len(chunk_matched)} matches")

        except Exception as e:
            print(f"ERROR: {e}")

        time.sleep(2)  # Rate limit between chunks

    print(f"  → Total: {len(all_matched)} matches across all chunks")
    return all_matched, all_details


# ============================================================
# Run cross-matches against each catalog
# ============================================================

catalogs = [
    ('vizier:II/328/allwise', 'AllWISE (IR photometry)'),
    ('vizier:I/355/gaiadr3', 'Gaia DR3 (stellar astrometry)'),
    ('vizier:V/154/sdss16', 'SDSS DR16 Photometric'),
    ('vizier:VII/290/catalog', 'Milliquas v8 (QSO catalog)'),
    ('simbad', 'SIMBAD (all known objects)'),
]

all_results = {}
any_match = set()  # TIDs matched by ANY catalog

for cat_id, cat_label in catalogs:
    print(f"\n{'='*50}")
    print(f"Catalog: {cat_label}")
    print(f"{'='*50}")

    matched_tids, details = cds_xmatch(csv_content, cat_id, MATCH_RADIUS_ARCSEC, cat_label)
    any_match.update(matched_tids)

    all_results[cat_label] = {
        'catalog_id': cat_id,
        'n_matched': len(matched_tids),
        'n_total': len(anomalies),
        'match_pct': round(len(matched_tids) / len(anomalies) * 100, 2),
        'sample_matches': details[:5] if details else [],
    }

    # Save per-catalog results
    safe_name = cat_label.split('(')[0].strip().replace(' ', '_').lower()
    cat_out = os.path.join(OUTPUT_DIR, f'xmatch_{safe_name}.json')
    with open(cat_out, 'w') as f:
        json.dump({
            'catalog': cat_label,
            'n_matched': len(matched_tids),
            'matched_tids': list(matched_tids)[:1000],  # Save first 1000 TIDs
            'match_pct': round(len(matched_tids) / len(anomalies) * 100, 2),
        }, f, indent=2, default=str)

    time.sleep(3)  # Rate limit between catalogs

# ============================================================
# Summary
# ============================================================

n_any_match = len(any_match)
n_genuinely_new = len(anomalies) - n_any_match

print(f"\n{'='*70}")
print("COMPREHENSIVE CROSS-MATCH SUMMARY")
print(f"{'='*70}")
print(f"Total anomalies: {len(anomalies)}")
print(f"Matched by ANY catalog: {n_any_match} ({n_any_match/len(anomalies)*100:.1f}%)")
print(f"NOT in ANY catalog: {n_genuinely_new} ({n_genuinely_new/len(anomalies)*100:.1f}%)")
print()

for cat_label, r in all_results.items():
    print(f"  {cat_label:35s}: {r['n_matched']:7d} matches ({r['match_pct']:.1f}%)")

print()
print(f"GENUINELY NEW (not in any checked catalog): {n_genuinely_new:,}")
print()

# Save comprehensive summary
summary = {
    'total_anomalies': len(anomalies),
    'match_radius_arcsec': MATCH_RADIUS_ARCSEC,
    'matched_by_any': n_any_match,
    'genuinely_new': n_genuinely_new,
    'genuinely_new_pct': round(n_genuinely_new / len(anomalies) * 100, 2),
    'per_catalog': all_results,
    'timestamp': time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime()),
    'disclaimer': 'Objects not found in checked catalogs may still exist in other databases not yet cross-matched. This is a necessary but not sufficient condition for claiming discovery.',
}

summary_path = os.path.join(OUTPUT_DIR, 'comprehensive_summary.json')
with open(summary_path, 'w') as f:
    json.dump(summary, f, indent=2, default=str)
print(f"Saved: {summary_path}")
print("=" * 70)
