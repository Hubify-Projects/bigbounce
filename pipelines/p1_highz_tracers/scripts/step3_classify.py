#!/usr/bin/env python3
"""
Pipeline 1 — Step 3: Classify 195,829 DESI DR1 anomalies.

Uses Step 2 cross-match data to separate anomalies into:
  1. HIGH-Z QSO CANDIDATES: W1-W2 > 0.8, not a star → useful for f_NL
  2. LIKELY STARS: Gaia parallax SNR > 3, or stellar colors
  3. KNOWN QSOs: Already in Milliquas → not "missed"
  4. IR-DETECTED NON-QSO: Has WISE match but W1-W2 < 0.8
  5. OPTICALLY-DETECTED ONLY: Has SDSS but no WISE match
  6. UNDETECTED: No photometric counterpart in any catalog

Within HIGH-Z QSO candidates, further classify by confidence:
  - GOLD: W1-W2 > 0.8 AND high anomaly score (>10) AND no Gaia parallax
  - SILVER: W1-W2 > 0.8 AND anomaly score 5-10
  - BRONZE: 0.5 < W1-W2 < 0.8 (ambiguous color region)
"""

import json
import os
import csv
import numpy as np
import pandas as pd
import logging
import sys

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
log = logging.getLogger()

BASE_DIR = 'pipelines/p1_highz_tracers/outputs'
CROSSMATCH_FILE = os.path.join(BASE_DIR, 'step2_crossmatch/anomaly_crossmatch.csv')
OUTPUT_DIR = os.path.join(BASE_DIR, 'step3_classification')
os.makedirs(OUTPUT_DIR, exist_ok=True)

log.info('Loading cross-match data...')
df = pd.read_csv(CROSSMATCH_FILE)
log.info(f'Loaded {len(df):,} anomalies with {len(df.columns)} columns')

# ============================================================
# Classification logic
# ============================================================

def classify(row):
    """Apply decision tree to classify each anomaly."""
    # Known QSO
    if row.get('known_qso') == 1:
        return 'KNOWN_QSO'

    # Likely star (Gaia parallax SNR > 3)
    if row.get('likely_star') == 1:
        return 'LIKELY_STAR'

    # Has WISE data
    has_wise = row.get('has_wise') == 1
    w1w2 = row.get('W1_W2')

    if has_wise and pd.notna(w1w2):
        if w1w2 > 0.8:
            return 'QSO_CANDIDATE'  # Strong QSO-like IR color
        elif w1w2 > 0.5:
            return 'AMBIGUOUS_IR'   # Could be AGN or late-type star
        else:
            return 'IR_NON_QSO'     # IR-detected but not QSO color
    elif has_wise:
        return 'IR_NOCOLOR'  # Has WISE match but couldn't compute W1-W2

    # SDSS only
    if row.get('has_sdss') == 1:
        return 'OPTICAL_ONLY'

    # Gaia only (without significant parallax)
    if row.get('has_gaia') == 1:
        return 'GAIA_ONLY'

    # No match in any catalog
    return 'UNDETECTED'


def qso_confidence(row, classification):
    """Assign confidence tier to QSO candidates."""
    if classification != 'QSO_CANDIDATE':
        return ''

    score = row.get('anomaly_score', 0)
    likely_star = row.get('likely_star', 0)
    w1w2 = row.get('W1_W2', 0)

    if likely_star == 1:
        return 'CONTAMINATED'  # Has parallax but also QSO color — confused

    if w1w2 > 1.0 and score > 10:
        return 'GOLD'
    elif w1w2 > 0.8 and score > 7:
        return 'SILVER'
    else:
        return 'BRONZE'


log.info('Classifying anomalies...')
df['classification'] = df.apply(classify, axis=1)
df['qso_confidence'] = df.apply(lambda r: qso_confidence(r, r['classification']), axis=1)

# ============================================================
# Summary statistics
# ============================================================

log.info('\n' + '='*60)
log.info('CLASSIFICATION RESULTS')
log.info('='*60)

class_counts = df['classification'].value_counts()
for cls, count in class_counts.items():
    pct = count / len(df) * 100
    log.info(f'  {cls:20s}: {count:>8,} ({pct:5.1f}%)')

log.info(f'\n  {"TOTAL":20s}: {len(df):>8,}')

# QSO candidate breakdown
qso_df = df[df['classification'] == 'QSO_CANDIDATE']
log.info(f'\nQSO CANDIDATE BREAKDOWN ({len(qso_df):,} objects):')
if len(qso_df) > 0:
    conf_counts = qso_df['qso_confidence'].value_counts()
    for tier, count in conf_counts.items():
        log.info(f'  {tier:20s}: {count:>6,}')

    # W1-W2 distribution
    w12 = qso_df['W1_W2'].dropna()
    log.info(f'\n  W1-W2 range: {w12.min():.2f} - {w12.max():.2f} (median: {w12.median():.2f})')

    # Score distribution
    scores = qso_df['anomaly_score']
    log.info(f'  Anomaly score range: {scores.min():.1f} - {scores.max():.1f} (median: {scores.median():.1f})')

    # Wise source breakdown
    wise_src = qso_df['wise_source'].value_counts()
    log.info(f'  WISE source: {dict(wise_src)}')

# Stars breakdown
star_df = df[df['classification'] == 'LIKELY_STAR']
if len(star_df) > 0:
    log.info(f'\nLIKELY STARS ({len(star_df):,}):')
    plx = star_df['gaia_Plx'].dropna()
    log.info(f'  Parallax range: {plx.min():.2f} - {plx.max():.2f} mas')

# Ambiguous IR
ambig_df = df[df['classification'] == 'AMBIGUOUS_IR']
if len(ambig_df) > 0:
    log.info(f'\nAMBIGUOUS IR ({len(ambig_df):,}):')
    w12 = ambig_df['W1_W2'].dropna()
    log.info(f'  W1-W2 range: {w12.min():.2f} - {w12.max():.2f}')

# ============================================================
# Save classified catalog
# ============================================================

# Save full classified catalog
csv_path = os.path.join(OUTPUT_DIR, 'anomaly_classified.csv')
df.to_csv(csv_path, index=False)
log.info(f'\nSaved: {csv_path} ({os.path.getsize(csv_path)/1024/1024:.1f} MB)')

# Save parquet
try:
    pq_path = os.path.join(OUTPUT_DIR, 'anomaly_classified.parquet')
    df.to_parquet(pq_path, index=False)
    log.info(f'Saved: {pq_path} ({os.path.getsize(pq_path)/1024/1024:.1f} MB)')
except Exception as e:
    log.warning(f'Parquet save failed: {e}')

# Save QSO candidates separately (for Step 4)
qso_path = os.path.join(OUTPUT_DIR, 'qso_candidates.csv')
qso_df.to_csv(qso_path, index=False)
log.info(f'Saved: {qso_path} ({len(qso_df):,} QSO candidates)')

# Save Gold QSOs
gold_df = qso_df[qso_df['qso_confidence'] == 'GOLD']
gold_path = os.path.join(OUTPUT_DIR, 'qso_gold.csv')
gold_df.to_csv(gold_path, index=False)
log.info(f'Saved: {gold_path} ({len(gold_df):,} Gold QSO candidates)')

# Save classification summary
summary = {
    'total_anomalies': len(df),
    'classifications': class_counts.to_dict(),
    'qso_candidates_total': len(qso_df),
    'qso_confidence_tiers': qso_df['qso_confidence'].value_counts().to_dict() if len(qso_df) > 0 else {},
    'qso_w1w2_median': float(qso_df['W1_W2'].median()) if len(qso_df) > 0 else None,
    'qso_score_median': float(qso_df['anomaly_score'].median()) if len(qso_df) > 0 else None,
    'likely_stars': len(star_df),
    'known_qsos': int(class_counts.get('KNOWN_QSO', 0)),
    'genuinely_new_no_match': int(class_counts.get('UNDETECTED', 0)),
    'for_step4_bias_validation': len(qso_df),
}

summary_path = os.path.join(OUTPUT_DIR, 'classification_summary.json')
with open(summary_path, 'w') as f:
    json.dump(summary, f, indent=2, default=str)
log.info(f'Saved: {summary_path}')

log.info(f'\n{"="*60}')
log.info('KEY RESULT FOR STEP 4:')
log.info(f'  {len(qso_df):,} QSO candidates (W1-W2 > 0.8, not stars)')
if len(gold_df) > 0:
    log.info(f'  {len(gold_df):,} GOLD tier (W1-W2 > 1.0, score > 10)')
log.info(f'  These go to Step 4 for bias validation (angular correlation)')
log.info(f'{"="*60}')
log.info('STEP 3 COMPLETE')
