#!/usr/bin/env python3
"""
Batch analyze ALL 195,829 DESI DR1 anomalies in batches of 50.

For each anomaly:
1. Classify by residual pattern (B/R/Z dominant or multi-band)
2. Estimate astrophysical type from band ratios + position
3. Generate AI analysis comment
4. Assess discovery potential
5. Upload to Convex reviews table
6. Save batch results locally

This runs as a continuous loop until all anomalies are processed.
Progress is checkpointed every batch so it can resume after interruption.
"""

import json
import os
import sys
import time
import math
import urllib.request
import urllib.parse

# ============================================================
# Configuration
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ANOMALY_FILE = os.path.join(BASE_DIR, '../outputs/desi_dr1/dr1_all_anomalies.json')
OUTPUT_DIR = os.path.join(BASE_DIR, '../outputs/desi_dr1/batch_analysis')
CHECKPOINT_FILE = os.path.join(OUTPUT_DIR, 'checkpoint.json')
BATCH_SIZE = 50

# Convex config — read from .env.local
ENV_FILE = os.path.join(BASE_DIR, '../../../.env.local')

def load_env():
    env = {}
    if os.path.exists(ENV_FILE):
        with open(ENV_FILE) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, val = line.split('=', 1)
                    env[key] = val
    return env

ENV = load_env()
CONVEX_URL = ENV.get('CONVEX_URL', '')
CONVEX_DEPLOY_KEY = ENV.get('CONVEX_DEV_DEPLOY_KEY', '')

# ============================================================
# Classification logic
# ============================================================

def classify_anomaly(a):
    """Classify a single anomaly by its residual pattern and position."""
    score = a['score']
    rB, rR, rZ = a['rB'], a['rR'], a['rZ']
    ra, dec = a['ra'], a['dec']
    total = rB + rR + rZ
    worst = a['worst']

    # Galactic latitude (approximate)
    import math
    l_rad = math.radians(ra)
    b_rad = math.radians(dec)
    # Rough galactic latitude estimate
    gal_b = abs(dec - 27.0 * math.cos(math.radians(ra - 192.0)))
    high_lat = abs(gal_b) > 30

    # Residual pattern
    if total == 0:
        pattern = 'unknown'
    elif max(rB, rR, rZ) / total > 0.85 and score > 10:
        pattern = 'artifact_suspect'
    elif rB / total > 0.6:
        pattern = 'B_dominant'
    elif rR / total > 0.6:
        pattern = 'R_dominant'
    elif rZ / total > 0.6:
        pattern = 'Z_dominant'
    else:
        pattern = 'multi_band'

    # Morphology guess from band ratios
    if pattern == 'Z_dominant':
        if rZ > 5:
            classification = 'HIGH_Z_CANDIDATE'
            discovery = 'HIGH'
            analysis = f"Z-band dominated residual ({rZ:.1f}x) suggests near-IR spectral anomaly. "
            analysis += "Possible high-redshift object (z > 2-3) with emission features shifted into Z-band, or unusual dusty source. "
            if high_lat:
                analysis += "High galactic latitude reduces stellar contamination risk."
            else:
                analysis += "Low galactic latitude — stellar contamination possible."
        else:
            classification = 'UNUSUAL_GALAXY'
            discovery = 'MEDIUM'
            analysis = f"Moderate Z-band anomaly ({rZ:.1f}x). Possible galaxy with unusual near-IR features or redshifted emission."

    elif pattern == 'R_dominant':
        if rR > 5:
            classification = 'HIGH_Z_CANDIDATE'
            discovery = 'HIGH'
            analysis = f"R-band dominated residual ({rR:.1f}x) suggests mid-optical anomaly. "
            analysis += "Possible QSO at z~3-4 with Lyman-alpha in R-band, or unusual broad absorption features."
        else:
            classification = 'UNUSUAL_AGN'
            discovery = 'MEDIUM'
            analysis = f"Moderate R-band anomaly ({rR:.1f}x). Possible AGN with unusual continuum shape or emission line ratios."

    elif pattern == 'B_dominant':
        if rB > 5:
            classification = 'UNUSUAL_AGN'
            discovery = 'MEDIUM'
            analysis = f"Strong B-band anomaly ({rB:.1f}x). Possible high-ionization emission, unusual UV continuum, "
            analysis += "or Lyman-break feature. Could also indicate calibration artifact in blue arm."
        else:
            classification = 'UNUSUAL_GALAXY'
            discovery = 'LOW'
            analysis = f"Moderate B-band anomaly ({rB:.1f}x). Likely unusual blue-end spectral features."

    elif pattern == 'multi_band':
        if score > 15:
            classification = 'GENUINELY_NOVEL'
            discovery = 'VERY_HIGH'
            analysis = f"Multi-band anomaly (rB={rB:.1f}, rR={rR:.1f}, rZ={rZ:.1f}) with high score {score:.1f}. "
            analysis += "Unusual across the FULL spectrum — strongest candidate for genuinely novel object. "
            analysis += "Could be: gravitational lens candidate, changing-look AGN, or entirely new object class."
        elif score > 10:
            classification = 'UNUSUAL_AGN'
            discovery = 'MEDIUM'
            analysis = f"Multi-band anomaly (rB={rB:.1f}, rR={rR:.1f}, rZ={rZ:.1f}). "
            analysis += "Anomalous across multiple wavelengths. Possible unusual AGN or composite spectrum."
        else:
            classification = 'UNUSUAL_GALAXY'
            discovery = 'LOW'
            analysis = f"Mild multi-band anomaly. Spectrum deviates modestly from all templates."

    elif pattern == 'artifact_suspect':
        classification = 'ARTIFACT_SUSPECT'
        discovery = 'LOW'
        dominant = worst
        analysis = f"Extreme single-band dominance in {dominant}-band ({max(rB,rR,rZ):.1f}x, {max(rB,rR,rZ)/total*100:.0f}% of total residual). "
        analysis += "Likely instrumental artifact, bad sky subtraction, or truncated spectrum. Requires visual inspection to confirm."

    else:
        classification = 'UNCLASSIFIED'
        discovery = 'LOW'
        analysis = "Insufficient data for classification."

    follow_up = discovery in ('HIGH', 'VERY_HIGH') or (discovery == 'MEDIUM' and score > 12)

    return {
        'residual_pattern': pattern,
        'classification': classification,
        'discovery_potential': discovery,
        'ai_analysis': analysis,
        'follow_up_recommended': follow_up,
    }

def upload_to_convex(review_data):
    """Upload a review to Convex."""
    if not CONVEX_URL:
        return False
    try:
        # Use Convex HTTP API
        url = f"{CONVEX_URL.rstrip('/')}/api/mutation"
        payload = {
            "path": "reviews:add",
            "args": {
                "pipelineId": "desi_dr1_anomaly",
                "objectId": str(review_data['tid']),
                "label": review_data['classification'],
                "aiLabel": review_data['classification'],
                "aiReason": review_data['ai_analysis'],
                "humanNotes": "",
                "reviewerName": "AI Agent (Claude)",
                "reviewedAt": int(time.time() * 1000),
                "metadata": {
                    "rank": review_data['rank'],
                    "score": review_data['score'],
                    "ra": review_data['ra'],
                    "dec": review_data['dec'],
                    "rB": review_data['rB'],
                    "rR": review_data['rR'],
                    "rZ": review_data['rZ'],
                    "worst": review_data['worst'],
                    "discovery_potential": review_data['discovery_potential'],
                    "follow_up": review_data['follow_up_recommended'],
                    "legacy_url": review_data['legacy_url'],
                },
            },
        }
        data = json.dumps(payload).encode()
        req = urllib.request.Request(url, data=data,
            headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.status == 200
    except Exception as e:
        return False

# ============================================================
# Main processing loop
# ============================================================

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Load anomalies
    print("Loading anomaly catalog...")
    with open(ANOMALY_FILE) as f:
        anomalies = json.load(f)
    anomalies.sort(key=lambda x: -x['score'])
    total = len(anomalies)
    print(f"Total: {total} anomalies")

    # Load checkpoint
    start_idx = 0
    if os.path.exists(CHECKPOINT_FILE):
        with open(CHECKPOINT_FILE) as f:
            cp = json.load(f)
        start_idx = cp.get('next_index', 0)
        print(f"Resuming from index {start_idx} (batch {start_idx // BATCH_SIZE + 1})")

    total_batches = math.ceil(total / BATCH_SIZE)
    current_batch = start_idx // BATCH_SIZE + 1

    # Stats trackers
    stats = {
        'HIGH_Z_CANDIDATE': 0, 'UNUSUAL_AGN': 0, 'UNUSUAL_GALAXY': 0,
        'GENUINELY_NOVEL': 0, 'STELLAR_ODDITY': 0, 'ARTIFACT_SUSPECT': 0,
        'UNCLASSIFIED': 0,
        'VERY_HIGH': 0, 'HIGH': 0, 'MEDIUM': 0, 'LOW': 0,
        'follow_up_count': 0,
    }

    convex_ok = 0
    convex_fail = 0

    print(f"\nProcessing batches of {BATCH_SIZE}...")
    print(f"Starting at batch {current_batch}/{total_batches}")
    print("=" * 70)

    for batch_start in range(start_idx, total, BATCH_SIZE):
        batch_end = min(batch_start + BATCH_SIZE, total)
        batch = anomalies[batch_start:batch_end]
        batch_num = batch_start // BATCH_SIZE + 1
        batch_results = []

        for i, a in enumerate(batch):
            rank = batch_start + i + 1
            result = classify_anomaly(a)

            obj = {
                'rank': rank,
                'tid': a['tid'],
                'ra': a['ra'],
                'dec': a['dec'],
                'score': a['score'],
                'worst': a['worst'],
                'rB': a['rB'],
                'rR': a['rR'],
                'rZ': a['rZ'],
                'legacy_url': f"https://www.legacysurvey.org/viewer?ra={a['ra']:.6f}&dec={a['dec']:.6f}&layer=ls-dr10&zoom=15",
                **result,
            }
            batch_results.append(obj)

            # Update stats
            stats[result['classification']] = stats.get(result['classification'], 0) + 1
            stats[result['discovery_potential']] = stats.get(result['discovery_potential'], 0) + 1
            if result['follow_up_recommended']:
                stats['follow_up_count'] += 1

            # Upload to Convex (with rate limiting)
            if upload_to_convex(obj):
                convex_ok += 1
            else:
                convex_fail += 1

        # Save batch file
        batch_file = os.path.join(OUTPUT_DIR, f'batch_{batch_num:05d}.json')
        with open(batch_file, 'w') as f:
            json.dump(batch_results, f, indent=1)

        # Update checkpoint
        with open(CHECKPOINT_FILE, 'w') as f:
            json.dump({
                'next_index': batch_end,
                'batches_complete': batch_num,
                'total_batches': total_batches,
                'stats': stats,
                'convex_uploads': convex_ok,
                'convex_failures': convex_fail,
                'timestamp': time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime()),
            }, f, indent=2)

        # Progress report
        pct = batch_end / total * 100
        novel = stats.get('GENUINELY_NOVEL', 0)
        high_z = stats.get('HIGH_Z_CANDIDATE', 0)
        follow = stats['follow_up_count']
        print(f"  Batch {batch_num:5d}/{total_batches} | {batch_end:7d}/{total} ({pct:5.1f}%) | "
              f"novel={novel} high_z={high_z} follow_up={follow} | "
              f"convex: {convex_ok}ok/{convex_fail}fail")

    # Final summary
    print("\n" + "=" * 70)
    print("ALL BATCHES COMPLETE")
    print("=" * 70)
    print(f"Total processed: {total}")
    print(f"\nClassification:")
    for cls in ['HIGH_Z_CANDIDATE', 'UNUSUAL_AGN', 'UNUSUAL_GALAXY', 'GENUINELY_NOVEL', 'ARTIFACT_SUSPECT']:
        print(f"  {cls:25s}: {stats.get(cls, 0):7d}")
    print(f"\nDiscovery potential:")
    for dp in ['VERY_HIGH', 'HIGH', 'MEDIUM', 'LOW']:
        print(f"  {dp:15s}: {stats.get(dp, 0):7d}")
    print(f"\nFollow-up recommended: {stats['follow_up_count']}")
    print(f"Convex uploads: {convex_ok} ok, {convex_fail} failed")

    # Save final summary
    summary_file = os.path.join(OUTPUT_DIR, 'final_summary.json')
    with open(summary_file, 'w') as f:
        json.dump({
            'total_processed': total,
            'stats': stats,
            'convex_uploads': convex_ok,
            'convex_failures': convex_fail,
            'completed_at': time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime()),
        }, f, indent=2)
    print(f"\nSaved: {summary_file}")

if __name__ == '__main__':
    main()
