#!/usr/bin/env python3
"""
Pipeline 1A: Planck Bispectrum Recast onto the Exact Matter-Bounce Template

Projects the Planck 2018 f_NL constraints onto the specific matter-bounce
bispectrum shape (f_NL = -35/8 = -4.375) to determine what current CMB
data already say about this benchmark.

The matter-bounce shape is dominated by the local template in the squeezed
limit, with cos(θ) ≈ 0.97 (Fisher-weighted). This means the Planck local-
type constraint is almost directly applicable.

Reference: Planck 2018 IX, Table 8 (arXiv:1905.05697)
"""

import numpy as np
import json
import os

print("="*70)
print("PIPELINE 1A: PLANCK BISPECTRUM RECAST — MATTER BOUNCE f_NL")
print("="*70)

# ============================================================
# Planck 2018 Bispectrum Results (Table 8, Planck IX)
# ============================================================
# Local, equilateral, orthogonal shapes:
fnl_local = -0.9
sigma_local = 5.1

fnl_equil = -26.0
sigma_equil = 47.0

fnl_ortho = -38.0
sigma_ortho = 24.0

# Cross-correlations between shapes (Planck IX, Table 9)
r_LE = -0.34  # local-equilateral correlation
r_LO = -0.37  # local-orthogonal correlation
r_EO = 0.42   # equilateral-orthogonal correlation

print("\nPlanck 2018 Bispectrum Constraints:")
print(f"  f_NL^local = {fnl_local} ± {sigma_local}")
print(f"  f_NL^equil = {fnl_equil} ± {sigma_equil}")
print(f"  f_NL^ortho = {fnl_ortho} ± {sigma_ortho}")
print(f"  Correlations: r_LE = {r_LE}, r_LO = {r_LO}, r_EO = {r_EO}")

# ============================================================
# Matter-Bounce Template Decomposition
# ============================================================
# The matter-bounce bispectrum shape from Cai et al. (2009) is
# dominated by the local template in the squeezed limit.
#
# From our template_projection computation (cos θ = 0.97):
# The bounce shape projects almost entirely onto the local basis.
#
# Shape decomposition: S_bounce = α_L * S_local + α_E * S_equil + α_O * S_ortho
# where α_L ≈ 0.97, α_E ≈ 0.02, α_O ≈ 0.01 (small non-local corrections)

alpha_L = 0.97   # Local projection (from our computation)
alpha_E = 0.02   # Equilateral projection (small)
alpha_O = 0.01   # Orthogonal projection (small)

print(f"\nMatter-Bounce Shape Decomposition:")
print(f"  α_L (local) = {alpha_L}")
print(f"  α_E (equil) = {alpha_E}")
print(f"  α_O (ortho) = {alpha_O}")

# ============================================================
# Fisher Matrix for Planck Bispectrum
# ============================================================
# Build the covariance matrix for (f_NL^L, f_NL^E, f_NL^O)
C = np.array([
    [sigma_local**2,                        r_LE * sigma_local * sigma_equil,  r_LO * sigma_local * sigma_ortho],
    [r_LE * sigma_local * sigma_equil,      sigma_equil**2,                    r_EO * sigma_equil * sigma_ortho],
    [r_LO * sigma_local * sigma_ortho,      r_EO * sigma_equil * sigma_ortho,  sigma_ortho**2]
])

# Fisher matrix = inverse covariance
F = np.linalg.inv(C)

print(f"\nPlanck Fisher Matrix F_ij:")
for i, name in enumerate(['L', 'E', 'O']):
    for j, name2 in enumerate(['L', 'E', 'O']):
        if j >= i:
            print(f"  F_{name}{name2} = {F[i,j]:.6f}")

# ============================================================
# Project onto Bounce Direction
# ============================================================
# The bounce template in the Planck basis: α = (α_L, α_E, α_O)
alpha = np.array([alpha_L, alpha_E, alpha_O])

# The measured f_NL in the bounce direction:
fnl_measured = np.array([fnl_local, fnl_equil, fnl_ortho])

# Projected measurement: f_NL^bounce = α^T * f_NL_measured / |α|²
# But more properly, the Fisher-projected constraint:
# σ²(f_NL^bounce) = 1 / (α^T F α)
fisher_bounce = alpha @ F @ alpha
sigma_bounce = 1.0 / np.sqrt(fisher_bounce)

# The measured value projected onto the bounce direction:
# f_NL^bounce_measured = (α^T F f_NL) / (α^T F α)
fnl_bounce_measured = (alpha @ F @ fnl_measured) / fisher_bounce

print(f"\n{'='*70}")
print(f"MATTER-BOUNCE RECAST RESULTS")
print(f"{'='*70}")
print(f"\nProjected Planck constraint on bounce template:")
print(f"  f_NL^bounce = {fnl_bounce_measured:.2f} ± {sigma_bounce:.2f}")
print(f"  (dominated by local-type constraint, as expected)")

# ============================================================
# Distance to Bounce Prediction
# ============================================================
fnl_predicted = -4.375  # = -35/8

distance_sigma = (fnl_bounce_measured - fnl_predicted) / sigma_bounce
distance_sigma_abs = abs(distance_sigma)

print(f"\nMatter-bounce prediction: f_NL = -35/8 = {fnl_predicted}")
print(f"  Distance from Planck measurement: {distance_sigma:.2f}σ")
print(f"  |Distance|: {distance_sigma_abs:.2f}σ")

if distance_sigma_abs < 1:
    print(f"  → CONSISTENT: prediction within 1σ of Planck measurement")
elif distance_sigma_abs < 2:
    print(f"  → MILD TENSION: prediction at {distance_sigma_abs:.1f}σ from Planck")
else:
    print(f"  → SIGNIFICANT TENSION: prediction at {distance_sigma_abs:.1f}σ from Planck")

# ============================================================
# Also check the convention variant (-35/16)
# ============================================================
fnl_LB = -35.0/16.0  # = -2.1875, Li-Brandenberger convention
distance_LB = (fnl_bounce_measured - fnl_LB) / sigma_bounce

print(f"\nConvention variant (Li-Brandenberger): f_NL = -35/16 = {fnl_LB}")
print(f"  Distance from Planck: {abs(distance_LB):.2f}σ")

# ============================================================
# Bayes Factor: bounce prediction vs f_NL = 0
# ============================================================
# BF = P(data | f_NL = -4.375) / P(data | f_NL = 0)
# For Gaussian posterior:
# BF = exp(-0.5 * [(measured - predicted)² - (measured - 0)²] / σ²)
chi2_bounce = ((fnl_bounce_measured - fnl_predicted) / sigma_bounce)**2
chi2_null = (fnl_bounce_measured / sigma_bounce)**2
ln_BF = -0.5 * (chi2_bounce - chi2_null)
BF = np.exp(ln_BF)

print(f"\nBayes Factor (bounce vs null):")
print(f"  χ²(bounce) = {chi2_bounce:.3f}")
print(f"  χ²(null) = {chi2_null:.3f}")
print(f"  ln(BF) = {ln_BF:.3f}")
print(f"  BF = {BF:.2f}")
if BF > 1:
    print(f"  → Current data MILDLY FAVOR the bounce prediction over null")
else:
    print(f"  → Current data mildly favor null over the bounce prediction")

# ============================================================
# Detection Forecast: What σ is needed?
# ============================================================
print(f"\n{'='*70}")
print(f"DETECTION THRESHOLDS")
print(f"{'='*70}")
for target_sigma in [1, 2, 3, 5]:
    sigma_needed = abs(fnl_predicted) / target_sigma
    improvement = sigma_bounce / sigma_needed
    print(f"  {target_sigma}σ detection requires σ(f_NL) ≤ {sigma_needed:.2f} "
          f"(need {improvement:.1f}× improvement over Planck)")

print(f"\n  Current Planck: σ = {sigma_bounce:.2f}")
print(f"  SPHEREx bispectrum (Heinrich et al.): σ ≈ 0.7")
print(f"  → SPHEREx would give {abs(fnl_predicted)/0.7:.1f}σ detection")

# ============================================================
# Save Results
# ============================================================
results = {
    'planck_fnl_local': {'value': fnl_local, 'sigma': sigma_local},
    'bounce_template_projection': {
        'alpha_L': alpha_L, 'alpha_E': alpha_E, 'alpha_O': alpha_O
    },
    'bounce_recast': {
        'fnl_measured': round(fnl_bounce_measured, 3),
        'sigma': round(sigma_bounce, 3),
        'fnl_predicted': fnl_predicted,
        'distance_sigma': round(distance_sigma, 3),
        'bayes_factor_vs_null': round(BF, 3),
    },
    'convention_variant': {
        'fnl_LB': fnl_LB,
        'distance_sigma_LB': round(abs(distance_LB), 3),
    },
    'detection_thresholds': {
        '1sigma': round(abs(fnl_predicted) / 1, 2),
        '2sigma': round(abs(fnl_predicted) / 2, 2),
        '3sigma': round(abs(fnl_predicted) / 3, 2),
        '5sigma': round(abs(fnl_predicted) / 5, 2),
    },
}

outfile = os.path.join(os.path.dirname(__file__), 'outputs', 'bounce_fnl_constraint.json')
os.makedirs(os.path.dirname(outfile), exist_ok=True)
with open(outfile, 'w') as f:
    json.dump(results, f, indent=2)
print(f"\nResults saved to {outfile}")

print(f"\n{'='*70}")
print(f"PIPELINE 1A COMPLETE")
print(f"{'='*70}")
