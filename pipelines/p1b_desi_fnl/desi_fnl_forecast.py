#!/usr/bin/env python3
"""
Pipeline 1B: DESI DR1 + Planck f_NL Combination

Combines DESI DR1 scale-dependent bias constraints with Planck bispectrum
to tighten the f_NL constraint on the matter-bounce benchmark.

DESI DR1 published results (Chaussidon et al. 2025, arXiv:2411.17623):
- LRG+QSO combined: f_NL = -3.6 (+9.0, -9.1)
- QSO-only (alternative bias): f_NL = 3.5 (+10.7, -7.4)

Planck 2018 (from Pipeline 1A recast):
- f_NL^bounce = -3.89 ± 4.76

Combined via inverse-variance weighting.
"""

import numpy as np
import json
import os

print("="*70)
print("PIPELINE 1B: DESI DR1 + PLANCK f_NL COMBINATION")
print("="*70)

# ============================================================
# Input constraints
# ============================================================

# From Pipeline 1A
planck_fnl = -3.89
planck_sigma = 4.76

# DESI DR1 published results
# Using the LRG+QSO combined result (most constraining)
desi_fnl = -3.6
desi_sigma_plus = 9.0
desi_sigma_minus = 9.1
desi_sigma = (desi_sigma_plus + desi_sigma_minus) / 2  # symmetrize

# DESI DR1 reanalysis (Ivanov et al. 2025, arXiv:2512.04266)
# Power spectrum + bispectrum combined
desi_reanalysis_fnl = -0.1
desi_reanalysis_sigma = 7.4

# DESI QSO × Planck CMB lensing (Piccirilli et al. 2025)
desi_lensing_fnl = -0.0
desi_lensing_sigma = 4.1  # Combined CMB+LSS

print("\nInput constraints:")
print(f"  Planck bispectrum (bounce recast): {planck_fnl:.2f} ± {planck_sigma:.2f}")
print(f"  DESI DR1 LRG+QSO (SDB):           {desi_fnl:.1f} ± {desi_sigma:.1f}")
print(f"  DESI DR1 reanalysis (P+B):         {desi_reanalysis_fnl:.1f} ± {desi_reanalysis_sigma:.1f}")
print(f"  DESI QSO × CMB lensing:            {desi_lensing_fnl:.1f} ± {desi_lensing_sigma:.1f}")

# ============================================================
# Combination 1: Planck + DESI DR1 (SDB)
# ============================================================
def combine_gaussian(measurements):
    """Inverse-variance weighted combination of Gaussian measurements."""
    weights = [1.0/s**2 for _, s in measurements]
    total_weight = sum(weights)
    combined_mean = sum(m * w for (m, _), w in zip(measurements, weights)) / total_weight
    combined_sigma = 1.0 / np.sqrt(total_weight)
    return combined_mean, combined_sigma

combo1_mean, combo1_sigma = combine_gaussian([
    (planck_fnl, planck_sigma),
    (desi_fnl, desi_sigma),
])

print(f"\n--- Combination 1: Planck + DESI DR1 (SDB) ---")
print(f"  f_NL = {combo1_mean:.2f} ± {combo1_sigma:.2f}")
print(f"  Improvement over Planck: {planck_sigma/combo1_sigma:.2f}×")

# ============================================================
# Combination 2: Planck + DESI reanalysis (P+B)
# ============================================================
combo2_mean, combo2_sigma = combine_gaussian([
    (planck_fnl, planck_sigma),
    (desi_reanalysis_fnl, desi_reanalysis_sigma),
])

print(f"\n--- Combination 2: Planck + DESI reanalysis (P+B) ---")
print(f"  f_NL = {combo2_mean:.2f} ± {combo2_sigma:.2f}")
print(f"  Improvement over Planck: {planck_sigma/combo2_sigma:.2f}×")

# ============================================================
# Combination 3: Planck + DESI QSO×lensing (strongest)
# ============================================================
combo3_mean, combo3_sigma = combine_gaussian([
    (planck_fnl, planck_sigma),
    (desi_lensing_fnl, desi_lensing_sigma),
])

print(f"\n--- Combination 3: Planck + DESI QSO×CMB lensing ---")
print(f"  f_NL = {combo3_mean:.2f} ± {combo3_sigma:.2f}")
print(f"  Improvement over Planck: {planck_sigma/combo3_sigma:.2f}×")

# ============================================================
# Combination 4: ALL three (Planck + DESI SDB + DESI lensing)
# ============================================================
# Note: DESI SDB and DESI lensing use overlapping data, so they're
# not fully independent. We present this as an optimistic upper bound.
combo4_mean, combo4_sigma = combine_gaussian([
    (planck_fnl, planck_sigma),
    (desi_fnl, desi_sigma),
    (desi_lensing_fnl, desi_lensing_sigma),
])

print(f"\n--- Combination 4: ALL (optimistic, correlated) ---")
print(f"  f_NL = {combo4_mean:.2f} ± {combo4_sigma:.2f}")
print(f"  Improvement over Planck: {planck_sigma/combo4_sigma:.2f}×")
print(f"  NOTE: DESI SDB and lensing are partially correlated")

# ============================================================
# Distance to bounce prediction for each combination
# ============================================================
fnl_predicted = -4.375

print(f"\n{'='*70}")
print(f"DISTANCE TO BOUNCE PREDICTION (f_NL = {fnl_predicted})")
print(f"{'='*70}")

combos = [
    ("Planck alone (1A)", planck_fnl, planck_sigma),
    ("Planck + DESI SDB", combo1_mean, combo1_sigma),
    ("Planck + DESI P+B", combo2_mean, combo2_sigma),
    ("Planck + DESI lensing", combo3_mean, combo3_sigma),
    ("ALL combined", combo4_mean, combo4_sigma),
]

print(f"\n{'Combination':<25} {'f_NL':<12} {'σ':<8} {'Dist from -4.375':<18} {'BF vs null'}")
print("-" * 75)

results_table = []
for name, mean, sigma in combos:
    dist = abs(mean - fnl_predicted) / sigma
    chi2_bounce = ((mean - fnl_predicted) / sigma)**2
    chi2_null = (mean / sigma)**2
    bf = np.exp(-0.5 * (chi2_bounce - chi2_null))
    print(f"{name:<25} {mean:<12.2f} {sigma:<8.2f} {dist:<18.2f}σ {bf:.2f}")
    results_table.append({
        'name': name, 'fnl': round(mean, 3), 'sigma': round(sigma, 3),
        'distance_from_prediction': round(dist, 3), 'bayes_factor_vs_null': round(bf, 3)
    })

# ============================================================
# SPHEREx comparison
# ============================================================
print(f"\n{'='*70}")
print(f"COMPARISON WITH FUTURE SURVEYS")
print(f"{'='*70}")

surveys = [
    ("Current best (Planck + DESI lensing)", combo3_sigma),
    ("SPHEREx bispectrum (Heinrich et al.)", 0.7),
    ("MegaMapper SDB (ideal)", 0.5),
]

for name, sigma in surveys:
    significance = abs(fnl_predicted) / sigma
    print(f"  {name}: σ = {sigma:.2f} → {significance:.1f}σ detection")

# ============================================================
# Save results
# ============================================================
results = {
    'input_constraints': {
        'planck_bounce_recast': {'fnl': planck_fnl, 'sigma': planck_sigma},
        'desi_dr1_sdb': {'fnl': desi_fnl, 'sigma': desi_sigma},
        'desi_reanalysis_pb': {'fnl': desi_reanalysis_fnl, 'sigma': desi_reanalysis_sigma},
        'desi_lensing': {'fnl': desi_lensing_fnl, 'sigma': desi_lensing_sigma},
    },
    'combinations': results_table,
    'bounce_prediction': fnl_predicted,
    'best_current_sigma': round(combo3_sigma, 3),
    'improvement_over_planck': round(planck_sigma / combo3_sigma, 2),
}

outfile = os.path.join(os.path.dirname(__file__), 'outputs', 'combined_fnl_constraint.json')
os.makedirs(os.path.dirname(outfile), exist_ok=True)
with open(outfile, 'w') as f:
    json.dump(results, f, indent=2)
print(f"\nResults saved to {outfile}")

print(f"\n{'='*70}")
print(f"PIPELINE 1B COMPLETE")
print(f"{'='*70}")
