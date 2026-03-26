#!/usr/bin/env python3
"""
Pipeline 1 Step 4: Bias Validation

Compute angular auto-correlation function w(theta) for anomaly sub-samples
and compare with the standard DESI QSO/LRG samples to determine if anomalous
objects have enhanced clustering (higher effective bias).

If anomalies cluster more strongly than standard tracers:
  → They sit in more massive halos → higher bias b₁
  → Better for f_NL scale-dependent bias measurement
  → Adding them to the tracer pool IMPROVES σ(f_NL)

If anomalies cluster at the same rate:
  → Same bias as standard tracers → marginal improvement from sample size only

If anomalies cluster LESS:
  → Lower bias → NOT useful for f_NL → still publishable as anomaly catalog

Method: Landy-Szalay estimator for w(theta) with random catalog generation.

References:
- Landy & Szalay (1993) — LS estimator
- Dalal et al. (2008) — scale-dependent bias from PNG
- DESI DR1 LSS catalogs — https://data.desi.lbl.gov/doc/releases/dr1/
"""

import json
import os
import sys
import numpy as np
from collections import Counter

# ============================================================
# Configuration
# ============================================================

ANOMALY_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
    '../outputs/desi_dr1/dr1_all_anomalies.json')
CLASS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
    '../outputs/desi_dr1/anomaly_classification.json')
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../outputs/desi_dr1')

# Angular bins (degrees)
THETA_BINS = np.logspace(-2, 0.5, 15)  # 0.01 to ~3 degrees
N_RANDOM = 100000  # Random catalog size for LS estimator

print("=" * 70)
print("PIPELINE 1 STEP 4: Bias Validation via Angular Clustering")
print("=" * 70)

# ============================================================
# Load data
# ============================================================

with open(ANOMALY_FILE) as f:
    anomalies = json.load(f)
print(f"Loaded {len(anomalies)} anomalies")

with open(CLASS_FILE) as f:
    classification = json.load(f)
print(f"Classification loaded: {list(classification['summary'].keys())}")

# ============================================================
# Generate random catalog (uniform on sky within DESI footprint)
# ============================================================

def generate_randoms(n, ra_range=(0, 360), dec_range=(-20, 80)):
    """Generate uniform random positions on the sphere within DESI footprint."""
    ra = np.random.uniform(ra_range[0], ra_range[1], n)
    # Uniform in sin(dec) for uniform on sphere
    sin_dec_min = np.sin(np.radians(dec_range[0]))
    sin_dec_max = np.sin(np.radians(dec_range[1]))
    sin_dec = np.random.uniform(sin_dec_min, sin_dec_max, n)
    dec = np.degrees(np.arcsin(sin_dec))
    return ra, dec

def angular_separation(ra1, dec1, ra2, dec2):
    """Compute angular separation in degrees between two sets of points."""
    ra1, dec1, ra2, dec2 = map(np.radians, [ra1, dec1, ra2, dec2])
    cos_sep = (np.sin(dec1) * np.sin(dec2) +
               np.cos(dec1) * np.cos(dec2) * np.cos(ra1 - ra2))
    cos_sep = np.clip(cos_sep, -1, 1)
    return np.degrees(np.arccos(cos_sep))

def pair_counts(ra, dec, theta_bins, max_sep=None):
    """Count pairs in angular separation bins. Brute force for small catalogs."""
    n = len(ra)
    counts = np.zeros(len(theta_bins) - 1)
    for i in range(n):
        # Vectorized separation from point i to all j > i
        seps = angular_separation(ra[i], dec[i], ra[i+1:], dec[i+1:])
        hist, _ = np.histogram(seps, bins=theta_bins)
        counts += hist
    return counts

def landy_szalay(dd, dr, rr, n_data, n_random):
    """Landy-Szalay estimator for w(theta)."""
    f = n_random / n_data
    w = (f * f * dd - 2 * f * dr + rr) / rr
    return w

# ============================================================
# Compute w(theta) for anomaly sub-samples
# ============================================================

# Use score tiers as sub-samples
tiers = {
    'extreme_15+': [a for a in anomalies if a['score'] >= 15],
    'high_10_15': [a for a in anomalies if 10 <= a['score'] < 15],
    'medium_7_10': [a for a in anomalies if 7 <= a['score'] < 10],
}

# For computational feasibility, subsample large tiers
MAX_SAMPLE = 5000
for name, objs in tiers.items():
    if len(objs) > MAX_SAMPLE:
        np.random.seed(42)
        indices = np.random.choice(len(objs), MAX_SAMPLE, replace=False)
        tiers[name] = [objs[i] for i in indices]

print(f"\nSub-samples for clustering:")
for name, objs in tiers.items():
    print(f"  {name}: {len(objs)} objects")

# Generate randoms
print(f"\nGenerating {N_RANDOM} random points...")
ra_rand, dec_rand = generate_randoms(N_RANDOM)

# Compute RR (random-random) pair counts once
print("Computing RR pair counts (this takes a minute)...")
# For speed, subsample randoms for pair counting
RR_SUBSAMPLE = 10000
ra_rr = ra_rand[:RR_SUBSAMPLE]
dec_rr = dec_rand[:RR_SUBSAMPLE]
rr_counts = pair_counts(ra_rr, dec_rr, THETA_BINS)

results = {}

for tier_name, tier_objs in tiers.items():
    print(f"\nComputing w(theta) for {tier_name} ({len(tier_objs)} objects)...")

    ra_data = np.array([a['ra'] for a in tier_objs])
    dec_data = np.array([a['dec'] for a in tier_objs])

    # DD (data-data)
    dd_counts = pair_counts(ra_data, dec_data, THETA_BINS)

    # DR (data-random) — cross-correlate data with randoms
    dr_counts = np.zeros(len(THETA_BINS) - 1)
    # Subsample randoms for DR
    ra_dr = ra_rand[:min(20000, N_RANDOM)]
    dec_dr = dec_rand[:min(20000, N_RANDOM)]
    for i in range(len(ra_data)):
        seps = angular_separation(ra_data[i], dec_data[i], ra_dr, dec_dr)
        hist, _ = np.histogram(seps, bins=THETA_BINS)
        dr_counts += hist

    # Landy-Szalay
    n_data = len(ra_data)
    n_rand_dd = RR_SUBSAMPLE
    n_rand_dr = len(ra_dr)

    # Normalize pair counts
    dd_norm = dd_counts / (n_data * (n_data - 1) / 2)
    dr_norm = dr_counts / (n_data * n_rand_dr)
    rr_norm = rr_counts / (n_rand_dd * (n_rand_dd - 1) / 2)

    # w(theta) = (DD/RR - 2*DR/RR + 1) approximately
    w_theta = np.where(rr_norm > 0, (dd_norm - 2 * dr_norm + rr_norm) / rr_norm, 0)

    theta_centers = np.sqrt(THETA_BINS[:-1] * THETA_BINS[1:])

    results[tier_name] = {
        'n_objects': len(tier_objs),
        'theta_deg': theta_centers.tolist(),
        'w_theta': w_theta.tolist(),
        'dd_counts': dd_counts.tolist(),
        'mean_w': float(np.mean(w_theta[w_theta > 0])) if np.any(w_theta > 0) else 0,
    }

    print(f"  Mean w(theta) = {results[tier_name]['mean_w']:.4f}")
    print(f"  DD pairs: {dd_counts.sum():.0f}")

# ============================================================
# Bias estimation
# ============================================================

# The bias is related to w(theta) via: w_obs(theta) = b^2 * w_matter(theta)
# For a rough estimate, compare the amplitude of w(theta) across tiers
# Higher w → higher bias

print("\n" + "=" * 70)
print("BIAS COMPARISON")
print("=" * 70)

baseline_w = results.get('medium_7_10', {}).get('mean_w', 0.01)
for tier_name, r in results.items():
    if baseline_w > 0:
        relative_bias_sq = r['mean_w'] / baseline_w
        relative_bias = np.sqrt(max(0, relative_bias_sq))
        print(f"  {tier_name}: w_mean = {r['mean_w']:.4f}, relative b/b_medium = {relative_bias:.2f}")
    else:
        print(f"  {tier_name}: w_mean = {r['mean_w']:.4f}")

# ============================================================
# f_NL impact estimate
# ============================================================

print("\n" + "=" * 70)
print("f_NL IMPACT ESTIMATE")
print("=" * 70)

# Scale-dependent bias: Δb(k) = (b₁ - 1) * f_NL * δ_c / (α(k) * k²)
# Improvement in σ(f_NL) from adding tracers scales as:
#   σ(f_NL) ∝ 1 / sqrt(n_eff * b_eff²)
# where n_eff is effective number density and b_eff is effective bias

n_extreme = len(tiers.get('extreme_15+', []))
n_high = len(tiers.get('high_10_15', []))
n_total_anomalies = len(anomalies)
n_desi_qso = 1_600_000  # approximate DESI QSO count

print(f"DESI QSO baseline: ~{n_desi_qso:,} objects")
print(f"Anomalies (all): {n_total_anomalies:,} objects")
print(f"If 10% are genuine high-z QSOs: ~{n_total_anomalies//10:,} new tracers")
print(f"  → Sample size increase: {n_total_anomalies/10/n_desi_qso*100:.1f}%")
print(f"  → σ(f_NL) improvement (sample size only): {1/np.sqrt(1 + n_total_anomalies/10/n_desi_qso):.4f}x")
print(f"If anomaly QSOs have 1.5x bias: improvement factor {1/np.sqrt(1 + (n_total_anomalies/10/n_desi_qso) * 1.5**2):.4f}x")

# ============================================================
# Save results
# ============================================================

output = {
    'metadata': {
        'n_anomalies': len(anomalies),
        'n_random': N_RANDOM,
        'theta_bins': THETA_BINS.tolist(),
        'method': 'Landy-Szalay estimator',
        'note': 'Preliminary clustering analysis. Full analysis requires DESI LSS randoms and proper window function.',
    },
    'clustering_by_tier': results,
    'fnl_impact': {
        'desi_qso_baseline': n_desi_qso,
        'anomaly_count': n_total_anomalies,
        'assumed_qso_fraction': 0.1,
        'sample_size_improvement': float(1/np.sqrt(1 + n_total_anomalies/10/n_desi_qso)),
        'with_bias_enhancement': float(1/np.sqrt(1 + (n_total_anomalies/10/n_desi_qso) * 1.5**2)),
    },
}

out_path = os.path.join(OUTPUT_DIR, 'bias_validation.json')
with open(out_path, 'w') as f:
    json.dump(output, f, indent=2, default=str)
print(f"\nSaved: {out_path}")
print("=" * 70)
