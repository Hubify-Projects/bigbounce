#!/usr/bin/env python3
"""
Pipeline 1 — Step 4: Bias Validation via Angular Clustering

Uses Step 3 classified QSO candidates to test whether anomaly-recovered
QSOs have enhanced clustering (higher effective bias) compared to:
  (a) a random subsample of all anomalies
  (b) theoretical expectations for DESI QSOs

Method: Landy-Szalay estimator for w(theta) with uniform random catalog.

If QSO candidates cluster MORE strongly → higher bias → useful for f_NL.
If they cluster at the SAME rate → marginal improvement from sample size only.
If they cluster LESS → not useful for f_NL (still publishable as catalog).

References:
- Landy & Szalay (1993), ApJ 412, 64
- Dalal et al. (2008), PRD 77, 123514
"""

import json
import os
import sys
import time
import numpy as np
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
log = logging.getLogger()

BASE_DIR = 'pipelines/p1_highz_tracers/outputs'
CLASSIFIED_FILE = os.path.join(BASE_DIR, 'step3_classification/anomaly_classified.csv')
QSO_FILE = os.path.join(BASE_DIR, 'step3_classification/qso_candidates.csv')
GOLD_FILE = os.path.join(BASE_DIR, 'step3_classification/qso_gold.csv')
OUTPUT_DIR = os.path.join(BASE_DIR, 'step4_bias_validation')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Angular bins (degrees) — 12 log-spaced bins from 0.02 to 5 degrees
THETA_EDGES = np.logspace(np.log10(0.02), np.log10(5.0), 13)
THETA_CENTERS = np.sqrt(THETA_EDGES[:-1] * THETA_EDGES[1:])

N_RANDOM = 50000  # Random catalog size
MAX_SAMPLE = 5000  # Max objects per sample for O(n^2) pair counting
SEED = 42

# ============================================================
# Helper functions
# ============================================================

def angular_sep_deg(ra1, dec1, ra2, dec2):
    """Vectorized angular separation in degrees (Vincenty formula)."""
    r1, d1, r2, d2 = map(np.radians, [ra1, dec1, ra2, dec2])
    dra = r1 - r2
    num = np.sqrt((np.cos(d2) * np.sin(dra))**2 +
                  (np.cos(d1) * np.sin(d2) - np.sin(d1) * np.cos(d2) * np.cos(dra))**2)
    den = np.sin(d1) * np.sin(d2) + np.cos(d1) * np.cos(d2) * np.cos(dra)
    return np.degrees(np.arctan2(num, den))


def count_pairs(ra, dec, theta_edges):
    """Count DD pairs in angular bins. O(n^2) brute force, vectorized inner loop."""
    n = len(ra)
    counts = np.zeros(len(theta_edges) - 1)
    for i in range(n - 1):
        seps = angular_sep_deg(ra[i], dec[i], ra[i+1:], dec[i+1:])
        h, _ = np.histogram(seps, bins=theta_edges)
        counts += h
    return counts


def count_cross_pairs(ra1, dec1, ra2, dec2, theta_edges):
    """Count DR cross-pairs. All i from sample 1 against all j from sample 2."""
    counts = np.zeros(len(theta_edges) - 1)
    for i in range(len(ra1)):
        seps = angular_sep_deg(ra1[i], dec1[i], ra2, dec2)
        h, _ = np.histogram(seps, bins=theta_edges)
        counts += h
    return counts


def generate_randoms(n, ra_range=(0, 360), dec_range=(-19.5, 79.5)):
    """Uniform random positions on the sphere within DESI-like footprint."""
    rng = np.random.default_rng(SEED)
    ra = rng.uniform(ra_range[0], ra_range[1], n)
    sin_min = np.sin(np.radians(dec_range[0]))
    sin_max = np.sin(np.radians(dec_range[1]))
    sin_dec = rng.uniform(sin_min, sin_max, n)
    dec = np.degrees(np.arcsin(sin_dec))
    return ra, dec


def landy_szalay(dd, dr, rr, nd, nr):
    """
    Landy-Szalay estimator: w(theta) = (DD - 2*DR + RR) / RR
    where DD, DR, RR are normalized pair counts.
    """
    # Normalize
    dd_norm = dd / (nd * (nd - 1) / 2) if nd > 1 else dd
    dr_norm = dr / (nd * nr)
    rr_norm = rr / (nr * (nr - 1) / 2) if nr > 1 else rr

    with np.errstate(divide='ignore', invalid='ignore'):
        w = np.where(rr_norm > 0, (dd_norm - 2 * dr_norm + rr_norm) / rr_norm, 0.0)
    return w


def compute_w_theta(ra_data, dec_data, ra_rand, dec_rand, theta_edges, label=''):
    """Full Landy-Szalay w(theta) computation for one sample."""
    nd = len(ra_data)
    nr = len(ra_rand)

    log.info(f'  [{label}] DD pairs ({nd} objects)...')
    t0 = time.time()
    dd = count_pairs(ra_data, dec_data, theta_edges)
    log.info(f'  [{label}] DD done in {time.time()-t0:.1f}s, {dd.sum():.0f} pairs')

    log.info(f'  [{label}] DR cross-pairs...')
    t0 = time.time()
    dr = count_cross_pairs(ra_data, dec_data, ra_rand, dec_rand, theta_edges)
    log.info(f'  [{label}] DR done in {time.time()-t0:.1f}s')

    w = landy_szalay(dd, dr, rr_counts, nd, nr_for_rr)
    mean_w = float(np.mean(w[w > 0])) if np.any(w > 0) else 0.0
    median_w = float(np.median(w)) if len(w) > 0 else 0.0

    return {
        'n_objects': nd,
        'theta_deg': THETA_CENTERS.tolist(),
        'w_theta': w.tolist(),
        'dd_total': float(dd.sum()),
        'mean_w_positive': mean_w,
        'median_w': median_w,
    }


# ============================================================
# Load data
# ============================================================

log.info('Loading classified anomaly catalog...')
df_all = pd.read_csv(CLASSIFIED_FILE)
log.info(f'Loaded {len(df_all):,} classified anomalies')

df_qso = pd.read_csv(QSO_FILE)
log.info(f'Loaded {len(df_qso):,} QSO candidates')

df_gold = pd.read_csv(GOLD_FILE)
log.info(f'Loaded {len(df_gold):,} GOLD QSO candidates')

# ============================================================
# Define samples for clustering comparison
# ============================================================

rng = np.random.default_rng(SEED)

# Sample 1: All QSO candidates (GOLD + SILVER + BRONZE), subsample if needed
qso_all = df_qso[['ra', 'dec', 'anomaly_score', 'W1_W2', 'qso_confidence']].dropna(subset=['ra', 'dec'])
if len(qso_all) > MAX_SAMPLE:
    qso_all = qso_all.sample(MAX_SAMPLE, random_state=SEED)

# Sample 2: GOLD + SILVER only (high-confidence QSOs)
gold_silver = df_qso[df_qso['qso_confidence'].isin(['GOLD', 'SILVER'])][['ra', 'dec', 'anomaly_score', 'W1_W2']].dropna(subset=['ra', 'dec'])

# Sample 3: GOLD only
gold_only = df_gold[['ra', 'dec', 'anomaly_score', 'W1_W2']].dropna(subset=['ra', 'dec'])

# Sample 4: Baseline — random subset of ALL anomalies (including non-QSO)
baseline = df_all[['ra', 'dec', 'anomaly_score']].dropna(subset=['ra', 'dec']).sample(
    min(MAX_SAMPLE, len(df_all)), random_state=SEED)

# Sample 5: IR_NON_QSO (negative control — should cluster less than QSOs)
ir_non_qso = df_all[df_all['classification'] == 'IR_NON_QSO'][['ra', 'dec', 'anomaly_score']].dropna(subset=['ra', 'dec'])
if len(ir_non_qso) > MAX_SAMPLE:
    ir_non_qso = ir_non_qso.sample(MAX_SAMPLE, random_state=SEED)

samples = {
    'qso_all': qso_all,
    'gold_silver': gold_silver,
    'gold_only': gold_only,
    'baseline_all': baseline,
    'ir_non_qso': ir_non_qso,
}

log.info('\nSamples for clustering:')
for name, s in samples.items():
    log.info(f'  {name}: {len(s)} objects')

# ============================================================
# Generate randoms and compute RR (once)
# ============================================================

log.info(f'\nGenerating {N_RANDOM} random catalog points...')
ra_rand, dec_rand = generate_randoms(N_RANDOM)

# RR: subsample randoms to 10K for manageable pair counting
RR_N = 10000
ra_rr = ra_rand[:RR_N]
dec_rr = dec_rand[:RR_N]
nr_for_rr = RR_N

log.info(f'Computing RR pair counts ({RR_N} randoms)...')
t0 = time.time()
rr_counts = count_pairs(ra_rr, dec_rr, THETA_EDGES)
log.info(f'RR done in {time.time()-t0:.1f}s, {rr_counts.sum():.0f} pairs')

# ============================================================
# Compute w(theta) for each sample
# ============================================================

# Use a subset of randoms for DR to keep runtime reasonable
DR_N = min(20000, N_RANDOM)
ra_dr = ra_rand[:DR_N]
dec_dr = dec_rand[:DR_N]

results = {}
for name, sample_df in samples.items():
    log.info(f'\n{"="*50}')
    log.info(f'Computing w(theta) for {name}...')

    ra_d = sample_df['ra'].values
    dec_d = sample_df['dec'].values

    r = compute_w_theta(ra_d, dec_d, ra_dr, dec_dr, THETA_EDGES, label=name)
    results[name] = r

    log.info(f'  {name}: mean_w(positive) = {r["mean_w_positive"]:.4f}, median_w = {r["median_w"]:.4f}')

# ============================================================
# Bias estimation: relative to baseline
# ============================================================

log.info(f'\n{"="*60}')
log.info('RELATIVE BIAS ESTIMATION')
log.info('='*60)

# w(theta) ~ b^2 * w_matter(theta)
# So b_A / b_B = sqrt(w_A / w_B) at the same angular scales
# Use mean of w(theta) at large angles (theta > 0.1 deg) where we have good S/N

large_scale_mask = THETA_CENTERS > 0.1  # degrees

def mean_w_large_scale(result):
    w = np.array(result['w_theta'])
    vals = w[large_scale_mask]
    positive = vals[vals > 0]
    return float(np.mean(positive)) if len(positive) > 0 else 0.0

baseline_w = mean_w_large_scale(results['baseline_all'])
log.info(f'\nBaseline (all anomalies) mean w(>0.1 deg): {baseline_w:.6f}')

bias_results = {}
for name, r in results.items():
    w_large = mean_w_large_scale(r)
    if baseline_w > 0 and w_large > 0:
        relative_bias = np.sqrt(w_large / baseline_w)
    else:
        relative_bias = 0.0

    bias_results[name] = {
        'mean_w_large_scale': w_large,
        'relative_bias_vs_baseline': float(relative_bias),
        'n_objects': r['n_objects'],
    }

    log.info(f'  {name:20s}: w = {w_large:.6f}, b/b_baseline = {relative_bias:.3f} (n={r["n_objects"]})')

# ============================================================
# f_NL sensitivity impact
# ============================================================

log.info(f'\n{"="*60}')
log.info('f_NL SENSITIVITY IMPACT')
log.info('='*60)

# Published constraints
sigma_fnl_desi = 9.05       # DESI QSO scale-dependent bias
sigma_fnl_planck = 5.1      # Planck bispectrum (bounce template)
n_desi_qso = 1_600_000
b_desi_qso = 2.5            # effective DESI QSO bias
fnl_prediction = -4.375     # -35/8

# Combined baseline
sigma_combined_baseline = 1 / np.sqrt(1/sigma_fnl_desi**2 + 1/sigma_fnl_planck**2)

# Actual QSO candidate counts from Step 3
n_qso_all = len(df_qso)         # 5,384
n_gold_silver = len(gold_silver) # GOLD + SILVER
n_gold = len(df_gold)           # 116

log.info(f'\nBaseline:')
log.info(f'  DESI QSO sample: {n_desi_qso:,}, b = {b_desi_qso}')
log.info(f'  σ(f_NL) DESI SDB: {sigma_fnl_desi}')
log.info(f'  σ(f_NL) Planck: {sigma_fnl_planck}')
log.info(f'  σ(f_NL) combined: {sigma_combined_baseline:.2f}')
log.info(f'  Detection significance: {abs(fnl_prediction)/sigma_combined_baseline:.2f}σ')

# Three scenarios using ACTUAL Step 3 numbers
scenarios = {}
for sample_name, n_new, bias_rel in [
    ('all_qso_candidates', n_qso_all, bias_results.get('qso_all', {}).get('relative_bias_vs_baseline', 1.0)),
    ('gold_silver_only', n_gold_silver, bias_results.get('gold_silver', {}).get('relative_bias_vs_baseline', 1.0)),
    ('gold_only', n_gold, bias_results.get('gold_only', {}).get('relative_bias_vs_baseline', 1.0)),
]:
    # Effective bias of new tracers
    b_new = b_desi_qso * max(bias_rel, 1.0)  # at least baseline bias

    # Multi-tracer improvement: σ ∝ 1/sqrt(n*(b-1)^2)
    weight_old = n_desi_qso * (b_desi_qso - 1)**2
    weight_new = n_new * (b_new - 1)**2
    improvement = np.sqrt(weight_old / (weight_old + weight_new))

    sigma_desi_new = sigma_fnl_desi * improvement
    sigma_combined_new = 1 / np.sqrt(1/sigma_desi_new**2 + 1/sigma_fnl_planck**2)
    pct_improve = (1 - sigma_combined_new / sigma_combined_baseline) * 100
    significance = abs(fnl_prediction) / sigma_combined_new

    scenarios[sample_name] = {
        'n_new_tracers': n_new,
        'relative_bias': float(bias_rel),
        'b_effective': float(b_new),
        'sigma_desi_improved': float(sigma_desi_new),
        'sigma_combined_improved': float(sigma_combined_new),
        'improvement_pct': float(pct_improve),
        'detection_significance': float(significance),
    }

    log.info(f'\n  {sample_name}:')
    log.info(f'    N new tracers: {n_new:,}')
    log.info(f'    Relative bias: {bias_rel:.3f} → b_eff = {b_new:.2f}')
    log.info(f'    σ(f_NL) DESI improved: {sigma_desi_new:.2f}')
    log.info(f'    σ(f_NL) combined: {sigma_combined_new:.2f} ({pct_improve:.1f}% improvement)')
    log.info(f'    Detection: {significance:.2f}σ')

# ============================================================
# Save results
# ============================================================

output = {
    'metadata': {
        'step': 4,
        'description': 'Bias validation via angular auto-correlation (Landy-Szalay)',
        'theta_edges_deg': THETA_EDGES.tolist(),
        'theta_centers_deg': THETA_CENTERS.tolist(),
        'n_random_catalog': N_RANDOM,
        'n_rr_subsample': RR_N,
        'n_dr_subsample': DR_N,
        'seed': SEED,
        'note': 'Preliminary — uses uniform randoms, not DESI survey window function',
    },
    'clustering': {name: r for name, r in results.items()},
    'bias_estimation': bias_results,
    'fnl_impact': {
        'baseline': {
            'sigma_desi_sdb': sigma_fnl_desi,
            'sigma_planck': sigma_fnl_planck,
            'sigma_combined': float(sigma_combined_baseline),
            'n_desi_qso': n_desi_qso,
            'b_desi_qso': b_desi_qso,
            'detection_significance': float(abs(fnl_prediction) / sigma_combined_baseline),
        },
        'scenarios': scenarios,
        'fnl_prediction': fnl_prediction,
    },
    'step3_inputs': {
        'qso_candidates_total': int(len(df_qso)),
        'gold_count': int(len(df_gold)),
        'gold_silver_count': int(n_gold_silver),
        'classifications': df_all['classification'].value_counts().to_dict(),
    },
}

out_path = os.path.join(OUTPUT_DIR, 'bias_validation.json')
with open(out_path, 'w') as f:
    json.dump(output, f, indent=2, default=str)
log.info(f'\nSaved: {out_path}')

# Save w(theta) table as CSV for plotting
import csv
csv_path = os.path.join(OUTPUT_DIR, 'w_theta_comparison.csv')
with open(csv_path, 'w', newline='') as f:
    writer = csv.writer(f)
    header = ['theta_deg'] + [f'w_{name}' for name in results]
    writer.writerow(header)
    for i, theta in enumerate(THETA_CENTERS):
        row = [f'{theta:.4f}'] + [f'{results[name]["w_theta"][i]:.6f}' for name in results]
        writer.writerow(row)
log.info(f'Saved: {csv_path}')

log.info(f'\n{"="*60}')
log.info('STEP 4 KEY RESULTS:')
for name, s in scenarios.items():
    log.info(f'  {name}: {s["n_new_tracers"]:,} tracers, b_rel={s["relative_bias"]:.3f}, '
             f'σ(f_NL)={s["sigma_combined_improved"]:.2f} ({s["improvement_pct"]:.1f}% better), '
             f'{s["detection_significance"]:.2f}σ detection')
log.info(f'{"="*60}')
log.info('STEP 4 COMPLETE')
