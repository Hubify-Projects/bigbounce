#!/usr/bin/env python3
"""
Pipeline 1 Step 5: f_NL Improvement Estimate

Given the bias validation results from Step 4, compute the expected
improvement in σ(f_NL) from adding anomaly-discovered tracers to the
DESI QSO sample.

The scale-dependent bias signal from f_NL is:
  Δb(k) = (b₁ - 1) · f_NL · δ_c / (α(k) · k²)

σ(f_NL) scales as:
  σ(f_NL) ∝ 1 / sqrt( n_eff · (b₁ - 1)² · V_eff )

Adding higher-bias tracers improves σ(f_NL) through both
increased sample size AND enhanced bias weight.
"""

import json
import os
import numpy as np

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../outputs/desi_dr1')

print("=" * 70)
print("PIPELINE 1 STEP 5: f_NL Improvement Estimate")
print("=" * 70)

# Load bias validation results
with open(os.path.join(OUTPUT_DIR, 'bias_validation.json')) as f:
    bias_data = json.load(f)

# ============================================================
# Baseline constraints (from published literature)
# ============================================================

# DESI DR1 scale-dependent bias constraint
sigma_fnl_desi_sdb = 9.05  # from DESI QSO SDB
sigma_fnl_planck = 5.1     # Planck bispectrum (local)
n_desi_qso = 1_600_000     # DESI QSO count
b_desi_qso = 2.5           # effective QSO bias at z ~ 1.5

# Our prediction
fnl_prediction = -4.375    # = -35/8

print(f"\nBaseline constraints:")
print(f"  DESI SDB: σ(f_NL) = {sigma_fnl_desi_sdb}")
print(f"  Planck bispectrum: σ(f_NL) = {sigma_fnl_planck}")
print(f"  Combined (inverse variance): σ(f_NL) = {1/np.sqrt(1/sigma_fnl_desi_sdb**2 + 1/sigma_fnl_planck**2):.2f}")

# ============================================================
# Anomaly-enhanced sample
# ============================================================

# From Step 4: extreme anomalies have 1.19x relative bias
# Conservative: assume 10% of all anomalies are genuine high-z QSOs
# Aggressive: assume 30% are genuine
# The rest are artifacts/stars/normal galaxies

scenarios = {
    'conservative_10pct': {
        'qso_fraction': 0.10,
        'bias_enhancement': 1.19,
        'description': '10% are genuine QSOs with 1.19x bias',
    },
    'moderate_20pct': {
        'qso_fraction': 0.20,
        'bias_enhancement': 1.15,
        'description': '20% are genuine QSOs with 1.15x bias',
    },
    'aggressive_30pct': {
        'qso_fraction': 0.30,
        'bias_enhancement': 1.10,
        'description': '30% are genuine QSOs with 1.10x bias',
    },
    'sample_size_only': {
        'qso_fraction': 0.10,
        'bias_enhancement': 1.00,
        'description': '10% are QSOs with same bias (no enhancement)',
    },
}

n_anomalies = 195829

print(f"\nAnomaly catalog: {n_anomalies} objects")
print(f"Baseline DESI QSO: {n_desi_qso} objects, b = {b_desi_qso}")

print(f"\n{'Scenario':<25s} {'New QSOs':>10s} {'b_eff':>8s} {'σ_new':>8s} {'σ_combined':>12s} {'Improvement':>12s}")
print("-" * 80)

results = {}

for name, scenario in scenarios.items():
    n_new_qso = int(n_anomalies * scenario['qso_fraction'])
    b_new = b_desi_qso * scenario['bias_enhancement']

    # Multi-tracer σ(f_NL) improvement
    # σ ∝ 1 / sqrt(n * (b-1)²)
    # Old: n_old * (b_old - 1)²
    # New: n_old * (b_old - 1)² + n_new * (b_new - 1)²
    weight_old = n_desi_qso * (b_desi_qso - 1)**2
    weight_new = n_new_qso * (b_new - 1)**2
    improvement_factor = np.sqrt(weight_old / (weight_old + weight_new))

    sigma_sdb_new = sigma_fnl_desi_sdb * improvement_factor
    sigma_combined_new = 1 / np.sqrt(1/sigma_sdb_new**2 + 1/sigma_fnl_planck**2)

    sigma_combined_old = 1 / np.sqrt(1/sigma_fnl_desi_sdb**2 + 1/sigma_fnl_planck**2)
    pct_improvement = (1 - sigma_combined_new / sigma_combined_old) * 100

    results[name] = {
        'n_new_qso': n_new_qso,
        'b_new': float(b_new),
        'sigma_sdb_new': float(sigma_sdb_new),
        'sigma_combined_new': float(sigma_combined_new),
        'improvement_pct': float(pct_improvement),
        'significance': float(abs(fnl_prediction) / sigma_combined_new),
    }

    print(f"{name:<25s} {n_new_qso:>10,d} {b_new:>8.2f} {sigma_sdb_new:>8.2f} {sigma_combined_new:>12.2f} {pct_improvement:>11.1f}%")

# ============================================================
# Detection significance
# ============================================================

print(f"\n{'='*70}")
print(f"DETECTION SIGNIFICANCE FOR f_NL = {fnl_prediction}")
print(f"{'='*70}")

sigma_combined_old = 1 / np.sqrt(1/sigma_fnl_desi_sdb**2 + 1/sigma_fnl_planck**2)
print(f"\n  Baseline (Planck + DESI SDB): σ = {sigma_combined_old:.2f}, detection at {abs(fnl_prediction)/sigma_combined_old:.2f}σ")

for name, r in results.items():
    print(f"  {name}: σ = {r['sigma_combined_new']:.2f}, detection at {r['significance']:.2f}σ")

print(f"\n  SPHEREx forecast: σ ≈ 0.7-2.0, detection at {abs(fnl_prediction)/1.5:.1f}-{abs(fnl_prediction)/0.7:.1f}σ")

# ============================================================
# Honest assessment
# ============================================================

print(f"\n{'='*70}")
print("HONEST ASSESSMENT")
print(f"{'='*70}")
print(f"""
The anomaly-enhanced tracer catalog provides a modest improvement in σ(f_NL):
- Best case (30% QSO fraction, 1.10x bias): {results['aggressive_30pct']['improvement_pct']:.1f}% improvement
- Conservative (10% QSO fraction, 1.19x bias): {results['conservative_10pct']['improvement_pct']:.1f}% improvement
- Sample size only (no bias enhancement): {results['sample_size_only']['improvement_pct']:.1f}% improvement

This is INCREMENTAL, not transformative. The primary value of this work is:
1. The anomaly catalog itself (195K previously unidentified objects)
2. The methodology (AI → tracer purification → cosmological measurement)
3. The proof-of-concept for the closed loop approach
4. The detection significance goes from {abs(fnl_prediction)/sigma_combined_old:.2f}σ to {results['conservative_10pct']['significance']:.2f}σ

The transformative improvement comes from SPHEREx (~2028): σ ≈ 0.7-2.0.
""")

# ============================================================
# Save results
# ============================================================

output = {
    'baseline': {
        'sigma_desi_sdb': sigma_fnl_desi_sdb,
        'sigma_planck': sigma_fnl_planck,
        'sigma_combined': float(sigma_combined_old),
        'n_desi_qso': n_desi_qso,
        'b_desi_qso': b_desi_qso,
        'detection_significance': float(abs(fnl_prediction) / sigma_combined_old),
    },
    'anomaly_enhanced': results,
    'fnl_prediction': fnl_prediction,
    'honest_assessment': 'Incremental improvement. Primary value is catalog + methodology, not σ(f_NL) breakthrough.',
}

out_path = os.path.join(OUTPUT_DIR, 'fnl_improvement_estimate.json')
with open(out_path, 'w') as f:
    json.dump(output, f, indent=2, default=str)
print(f"Saved: {out_path}")
