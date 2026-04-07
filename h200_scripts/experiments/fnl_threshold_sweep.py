#!/usr/bin/env python3
"""
Phase 4 Experiment: f_NL Score Threshold Sensitivity Sweep

Sweep anomaly score thresholds and compute sigma(f_NL) at each threshold.
Shows how the optimal threshold balances sample size vs purity (bias).

Key insight: Higher threshold -> fewer objects but higher bias ->
  the optimal threshold maximizes the f_NL Fisher information = n * b^2 * (b-p)^2

Thresholds tested: 5, 7, 10, 15, 20, 25, 30
For each threshold:
  - Count objects above threshold
  - Estimate effective bias from clustering amplitude (or model)
  - Compute Fisher information and sigma(f_NL)
  - Determine SNR for f_NL = -4.375 (matter bounce prediction)

Output: /workspace/bigbounce/outputs/fnl_threshold_sweep/fnl_threshold_sweep_summary.json
"""

import json
import os
import sys
import time
import numpy as np
from pathlib import Path

# ============================================================
# NumpyEncoder
# ============================================================

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (np.integer,)): return int(obj)
        if isinstance(obj, (np.floating,)): return float(obj)
        if isinstance(obj, (np.bool_,)): return bool(obj)
        if isinstance(obj, np.ndarray): return obj.tolist()
        return super().default(obj)

# ============================================================
# Configuration
# ============================================================

OUTPUT_DIR = "/workspace/bigbounce/outputs/fnl_threshold_sweep"
os.makedirs(OUTPUT_DIR, exist_ok=True)

THRESHOLDS = [5, 7, 10, 15, 20, 25, 30]
FNL_BOUNCE = -4.375  # matter bounce prediction (f_NL = -35/8)

# Fisher forecast baseline parameters
SIGMA_FNL_BASELINE = 8.98  # DESI single-tracer
N_DESI_QSO = 1_600_000
B_DESI_QSO = 2.5

print("=" * 70)
print("PHASE 4: f_NL Score Threshold Sensitivity Sweep")
print("=" * 70)

# ============================================================
# Load data
# ============================================================

def load_anomalies():
    """Load anomaly catalog or generate synthetic."""
    candidates = [
        "/workspace/dr1_all_anomalies.json",
        "/workspace/bigbounce/outputs/desi_dr1/dr1_all_anomalies.json",
    ]
    for path in candidates:
        if os.path.exists(path):
            print(f"Loading: {path}")
            with open(path) as f:
                data = json.load(f)
            print(f"  Loaded {len(data)} anomalies")
            return data, False

    # Synthetic
    print("Generating synthetic anomalies...")
    np.random.seed(42)
    n = 195829  # DESI DR1 anomaly count
    scores = 5 + np.random.exponential(3, n)
    z = np.random.uniform(0.3, 4.5, n)
    ra = np.random.uniform(0, 360, n)
    sin_dec = np.random.uniform(np.sin(np.radians(-20)), np.sin(np.radians(80)), n)
    dec = np.degrees(np.arcsin(sin_dec))

    data = [{'score': float(scores[i]), 'z': float(z[i]),
             'ra': float(ra[i]), 'dec': float(dec[i])} for i in range(n)]
    print(f"  Generated {n} synthetic anomalies")
    return data, True

anomalies, is_synthetic = load_anomalies()

# ============================================================
# Bias model
# ============================================================

def estimate_bias(score_threshold, z_mean):
    """
    Estimate effective bias for anomalies above a score threshold.

    Model: Objects with higher anomaly scores tend to be rarer, more extreme
    objects (e.g., high-z QSOs, unusual AGN) that live in more massive halos.

    Bias scaling with score:
      b(score) ~ b_0 + alpha * log(score/5)
    where b_0 = 2.5 (typical QSO bias) and alpha ~ 1.0 (empirical slope).

    Additional z-dependence:
      b(z) ~ 1 + (b_0 - 1) * D(0)/D(z)
    where D(z) is the growth factor. Approximate: b(z) ~ b_0 * (1 + 0.2*(z-1.5))
    """
    b_0 = 2.5
    alpha = 1.0

    # Score-dependent bias enhancement
    b_score = b_0 + alpha * np.log(max(score_threshold, 5) / 5.0)

    # Redshift correction
    z_correction = 1 + 0.2 * (z_mean - 1.5)

    return float(b_score * max(z_correction, 0.5))

def compute_clustering_amplitude(ra, dec, n_subsample=2000):
    """Quick clustering amplitude estimate via pair excess at small separations."""
    if len(ra) < 20:
        return 0.0

    # Subsample for speed
    if len(ra) > n_subsample:
        idx = np.random.choice(len(ra), n_subsample, replace=False)
        ra = ra[idx]
        dec = dec[idx]

    n = len(ra)

    # Count pairs within 0.1 degrees
    ra_rad = np.radians(ra)
    dec_rad = np.radians(dec)

    n_pairs_small = 0
    n_pairs_total = 0

    # Vectorized: compute all pairs in batches
    batch = min(500, n)
    for i in range(0, n, batch):
        i_end = min(i + batch, n)
        for ii in range(i, i_end):
            cos_sep = (np.sin(dec_rad[ii]) * np.sin(dec_rad[ii+1:]) +
                       np.cos(dec_rad[ii]) * np.cos(dec_rad[ii+1:]) *
                       np.cos(ra_rad[ii] - ra_rad[ii+1:]))
            cos_sep = np.clip(cos_sep, -1, 1)
            seps_deg = np.degrees(np.arccos(cos_sep))

            n_pairs_small += np.sum(seps_deg < 0.1)
            n_pairs_total += len(seps_deg)

    # Expected pairs for uniform distribution within 0.1 deg
    # Fraction of sky within 0.1 deg ~ pi * 0.1^2 / 41253 ~ 7.6e-7
    sky_frac = np.pi * 0.1**2 / 41253.0
    expected = n_pairs_total * sky_frac

    if expected > 0:
        excess = (n_pairs_small - expected) / expected
        return float(max(excess, 0))
    return 0.0

# ============================================================
# Sweep thresholds
# ============================================================

print(f"\nSweeping {len(THRESHOLDS)} thresholds...")
print(f"Total anomalies: {len(anomalies)}")

sweep_results = []

for threshold in THRESHOLDS:
    print(f"\n--- Threshold = {threshold} ---")

    # Filter anomalies
    above = [a for a in anomalies if a.get('score', 0) >= threshold]
    n_above = len(above)

    if n_above < 5:
        print(f"  Only {n_above} objects above threshold, skipping")
        sweep_results.append({
            'threshold': threshold,
            'n_objects': n_above,
            'skipped': True,
            'reason': 'too few objects',
        })
        continue

    # Statistics
    scores = np.array([a['score'] for a in above])
    redshifts = np.array([a.get('z', 1.5) for a in above])
    z_mean = float(np.mean(redshifts))
    z_median = float(np.median(redshifts))

    # Estimate bias
    bias_model = estimate_bias(threshold, z_mean)

    # Quick clustering check (for a subsample)
    ra = np.array([a['ra'] for a in above])
    dec = np.array([a['dec'] for a in above])

    t0 = time.time()
    clustering_excess = compute_clustering_amplitude(ra, dec)
    cluster_time = time.time() - t0

    # Empirical bias correction from clustering
    bias_empirical = bias_model * (1 + 0.5 * min(clustering_excess, 2.0))

    # Assume 10% are genuine high-z tracers
    qso_frac = 0.10
    n_tracers = int(n_above * qso_frac)

    # Fisher information contribution
    # F propto n * b^2 for single-tracer
    # Multi-tracer: F propto n * b^2 * (b - b_ref)^2 for cosmic variance cancellation
    fisher_single = n_tracers * bias_empirical**2
    fisher_multi = n_tracers * bias_empirical**2 * (bias_empirical - B_DESI_QSO)**2

    # Combined with DESI QSOs
    fisher_total_single = N_DESI_QSO * B_DESI_QSO**2 + fisher_single
    fisher_total_multi = N_DESI_QSO * B_DESI_QSO**2 + fisher_multi

    # sigma(f_NL) scaling: sigma propto 1/sqrt(F)
    sigma_fnl_single = SIGMA_FNL_BASELINE * np.sqrt(N_DESI_QSO * B_DESI_QSO**2 / fisher_total_single)
    sigma_fnl_multi = SIGMA_FNL_BASELINE * np.sqrt(N_DESI_QSO * B_DESI_QSO**2 / fisher_total_multi)

    # Detection significance for matter bounce
    snr_single = abs(FNL_BOUNCE) / sigma_fnl_single
    snr_multi = abs(FNL_BOUNCE) / sigma_fnl_multi

    result = {
        'threshold': threshold,
        'n_objects': n_above,
        'n_tracers_10pct': n_tracers,
        'score_mean': float(np.mean(scores)),
        'score_median': float(np.median(scores)),
        'z_mean': z_mean,
        'z_median': z_median,
        'bias_model': float(bias_model),
        'clustering_excess': float(clustering_excess),
        'bias_empirical': float(bias_empirical),
        'fisher_single_tracer': float(fisher_single),
        'fisher_multi_tracer': float(fisher_multi),
        'sigma_fnl_with_anomalies': float(sigma_fnl_single),
        'sigma_fnl_multi_tracer': float(sigma_fnl_multi),
        'improvement_pct_single': float((1 - sigma_fnl_single / SIGMA_FNL_BASELINE) * 100),
        'improvement_pct_multi': float((1 - sigma_fnl_multi / SIGMA_FNL_BASELINE) * 100),
        'snr_bounce_single': float(snr_single),
        'snr_bounce_multi': float(snr_multi),
        'cluster_time_s': float(cluster_time),
        'skipped': False,
    }

    sweep_results.append(result)

    print(f"  N objects: {n_above:,} (tracers: {n_tracers:,})")
    print(f"  z_mean: {z_mean:.2f}, bias: {bias_empirical:.2f}")
    print(f"  Clustering excess: {clustering_excess:.4f}")
    print(f"  sigma(f_NL) single: {sigma_fnl_single:.2f} ({(1-sigma_fnl_single/SIGMA_FNL_BASELINE)*100:.2f}% improvement)")
    print(f"  sigma(f_NL) multi:  {sigma_fnl_multi:.2f} ({(1-sigma_fnl_multi/SIGMA_FNL_BASELINE)*100:.2f}% improvement)")
    print(f"  SNR(f_NL=-4.375): {snr_single:.3f} (single), {snr_multi:.3f} (multi)")

# ============================================================
# Find optimal threshold
# ============================================================

print("\n" + "=" * 70)
print("OPTIMAL THRESHOLD ANALYSIS")
print("=" * 70)

valid_results = [r for r in sweep_results if not r.get('skipped', False)]

if valid_results:
    # Optimal for single-tracer: minimize sigma
    best_single = min(valid_results, key=lambda r: r['sigma_fnl_with_anomalies'])
    # Optimal for multi-tracer: minimize sigma
    best_multi = min(valid_results, key=lambda r: r['sigma_fnl_multi_tracer'])
    # Optimal for SNR: maximize
    best_snr = max(valid_results, key=lambda r: r['snr_bounce_multi'])

    print(f"Best threshold (single-tracer sigma): {best_single['threshold']} "
          f"-> sigma={best_single['sigma_fnl_with_anomalies']:.2f}")
    print(f"Best threshold (multi-tracer sigma): {best_multi['threshold']} "
          f"-> sigma={best_multi['sigma_fnl_multi_tracer']:.2f}")
    print(f"Best threshold (SNR): {best_snr['threshold']} "
          f"-> SNR={best_snr['snr_bounce_multi']:.3f}")

    optimal = {
        'best_single_tracer': {
            'threshold': best_single['threshold'],
            'sigma_fnl': float(best_single['sigma_fnl_with_anomalies']),
        },
        'best_multi_tracer': {
            'threshold': best_multi['threshold'],
            'sigma_fnl': float(best_multi['sigma_fnl_multi_tracer']),
        },
        'best_snr': {
            'threshold': best_snr['threshold'],
            'snr': float(best_snr['snr_bounce_multi']),
        },
    }
else:
    optimal = {'note': 'No valid results'}

# ============================================================
# SPHEREx projection
# ============================================================

print("\n" + "=" * 70)
print("SPHEREx PROJECTION")
print("=" * 70)

if valid_results:
    # SPHEREx will improve by ~2x over DESI for f_NL
    for r in valid_results:
        r['sigma_fnl_spherex_multi'] = float(r['sigma_fnl_multi_tracer'] * 0.5)
        r['snr_spherex_multi'] = float(abs(FNL_BOUNCE) / r['sigma_fnl_spherex_multi'])

    best_spherex = max(valid_results, key=lambda r: r['snr_spherex_multi'])
    print(f"Best threshold for SPHEREx: {best_spherex['threshold']}")
    print(f"  sigma(f_NL) = {best_spherex['sigma_fnl_spherex_multi']:.2f}")
    print(f"  SNR = {best_spherex['snr_spherex_multi']:.2f} sigma")

    optimal['best_spherex'] = {
        'threshold': best_spherex['threshold'],
        'sigma_fnl': float(best_spherex['sigma_fnl_spherex_multi']),
        'snr': float(best_spherex['snr_spherex_multi']),
    }

# ============================================================
# Save results
# ============================================================

summary = {
    'experiment_id': 'fnl_threshold_sweep',
    'phase': 4,
    'description': 'Anomaly score threshold sensitivity sweep for f_NL optimization',
    'data_source': 'synthetic' if is_synthetic else 'real DESI DR1 anomalies',
    'config': {
        'thresholds': THRESHOLDS,
        'fnl_bounce_prediction': FNL_BOUNCE,
        'sigma_fnl_baseline': SIGMA_FNL_BASELINE,
        'n_desi_qso': N_DESI_QSO,
        'b_desi_qso': B_DESI_QSO,
        'qso_fraction_assumed': 0.10,
    },
    'sweep_results': valid_results,
    'optimal_thresholds': optimal,
    'conclusions': {
        'optimal_threshold_exists': len(valid_results) > 1,
        'tradeoff': (
            'Higher thresholds yield fewer but more biased tracers. '
            'The optimal threshold balances sample size vs bias enhancement.'
        ),
        'recommendation': (
            f"Use threshold={best_multi['threshold']} for multi-tracer analysis "
            f"(sigma_fnl={best_multi['sigma_fnl_multi_tracer']:.2f})"
            if valid_results else 'Insufficient data'
        ),
    },
}

out_path = os.path.join(OUTPUT_DIR, 'fnl_threshold_sweep_summary.json')
with open(out_path, 'w') as f:
    json.dump(summary, f, indent=2, cls=NumpyEncoder)

print(f"\nSaved: {out_path}")
print("=" * 70)
print("COMPLETE")
