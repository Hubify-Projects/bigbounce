#!/usr/bin/env python3
"""
Pipeline 1C: Current-Data Birefringence Inference

Combines all published cosmic birefringence measurements into a
definitive current-data constraint, maps to ALP parameter space,
and compares with the bounce-motivated prediction β ≈ 0.27°.

Measurements used:
- Planck HFI (Minami & Komatsu 2020): β = 0.35 ± 0.14°
- Planck NPIPE (Eskilt 2022): β = 0.30 ± 0.11°
- ACT DR6 (Diego-Palazuelos & Komatsu 2025): β = 0.215 ± 0.074°
- Eskilt et al. joint analysis: β = 0.342 ± 0.094°
- SPIDER+Planck+ACT combined: β = 0.30 ± 0.043° (total α+β rotation)
"""

import numpy as np
import json
import os

print("="*70)
print("PIPELINE 1C: CURRENT-DATA BIREFRINGENCE INFERENCE")
print("="*70)

# ============================================================
# Published β measurements
# ============================================================
measurements = [
    {"name": "Planck HFI (Minami & Komatsu 2020)", "beta": 0.35, "sigma": 0.14, "independent": True},
    {"name": "Planck NPIPE (Eskilt 2022)", "beta": 0.30, "sigma": 0.11, "independent": True},
    {"name": "ACT DR6 (Diego-Palazuelos 2025)", "beta": 0.215, "sigma": 0.074, "independent": True},
]

# Note: Eskilt joint analysis (0.342 ± 0.094) uses full EB spectrum,
# not just the point estimate — we use it for MCMC comparison but not
# in the simple inverse-variance combination.

# SPIDER+Planck+ACT (0.30 ± 0.043) is for total rotation α+β, not
# clean cosmological β alone — noted but not used in primary combination.

print("\nIndependent β measurements:")
for m in measurements:
    sig = m['beta'] / m['sigma']
    print(f"  {m['name']}: β = {m['beta']:.3f} ± {m['sigma']:.3f}° ({sig:.1f}σ)")

# ============================================================
# Inverse-variance weighted combination
# ============================================================
# Using Planck NPIPE + ACT DR6 (most independent pair)
primary = [m for m in measurements if "NPIPE" in m['name'] or "ACT" in m['name']]

weights = [1.0/m['sigma']**2 for m in primary]
total_weight = sum(weights)
beta_combined = sum(m['beta'] * w for m, w in zip(primary, weights)) / total_weight
sigma_combined = 1.0 / np.sqrt(total_weight)
significance_combined = beta_combined / sigma_combined

print(f"\n--- Primary combination (Planck NPIPE + ACT DR6) ---")
print(f"  β_combined = {beta_combined:.3f} ± {sigma_combined:.3f}° ({significance_combined:.1f}σ)")

# Using ALL three
weights_all = [1.0/m['sigma']**2 for m in measurements]
total_weight_all = sum(weights_all)
beta_all = sum(m['beta'] * w for m, w in zip(measurements, weights_all)) / total_weight_all
sigma_all = 1.0 / np.sqrt(total_weight_all)
significance_all = beta_all / sigma_all

print(f"\n--- Full combination (all three) ---")
print(f"  β_combined = {beta_all:.3f} ± {sigma_all:.3f}° ({significance_all:.1f}σ)")
print(f"  NOTE: Planck HFI and NPIPE are partially correlated (same data, different cleaning)")

# ============================================================
# Comparison with bounce prediction
# ============================================================
beta_predicted = 0.27  # degrees, from ALP with natural parameters

print(f"\n{'='*70}")
print(f"COMPARISON WITH BOUNCE-MOTIVATED PREDICTION")
print(f"{'='*70}")

for label, beta_c, sigma_c in [
    ("Primary (NPIPE+ACT)", beta_combined, sigma_combined),
    ("Full (all three)", beta_all, sigma_all),
]:
    dist = abs(beta_c - beta_predicted) / sigma_c
    # BF: P(data | β = 0.27) / P(data | β = 0)
    chi2_pred = ((beta_c - beta_predicted) / sigma_c)**2
    chi2_null = (beta_c / sigma_c)**2
    bf = np.exp(-0.5 * (chi2_pred - chi2_null))

    print(f"\n  {label}:")
    print(f"    β_measured = {beta_c:.3f} ± {sigma_c:.3f}°")
    print(f"    β_predicted = {beta_predicted}°")
    print(f"    Distance: {dist:.2f}σ")
    print(f"    BF(prediction vs null): {bf:.2f}")

# ============================================================
# ALP parameter space mapping
# ============================================================
print(f"\n{'='*70}")
print(f"ALP PARAMETER SPACE")
print(f"{'='*70}")

alpha_EM = 1/137.036
M_Pl = 2.435e18  # GeV

# For standard ALP coupling: g_aγ = α_EM * C_aγ / (2π f_a)
# β = g_aγ/2 × Δφ where Δφ/f_a ≈ 0.65 (from our numerical computation)
delta_phi_over_fa = 0.65

print(f"\n  Using computed Δφ/f_a = {delta_phi_over_fa} (from ALP ODE integration)")
print(f"\n  For f_a = M_Pl:")

for C_agamma in [1, 2, 4, 8, 12]:
    g_agamma = alpha_EM * C_agamma / (2 * np.pi * M_Pl)
    beta_deg = np.degrees(g_agamma / 2 * delta_phi_over_fa * M_Pl)
    print(f"    C_aγ = {C_agamma:>2}: g_aγ = {g_agamma:.2e} GeV⁻¹, β = {beta_deg:.4f}°")

# What C_aγ matches the observed combined β?
# β = α_EM × C_aγ / (4π) × Δφ/f_a (in radians)
beta_rad = np.radians(beta_combined)
C_needed = beta_rad * 4 * np.pi / (alpha_EM * delta_phi_over_fa)
print(f"\n  To match observed β = {beta_combined:.3f}°:")
print(f"    C_aγ needed = {C_needed:.1f}")
print(f"    This is {'natural (O(1)-O(10))' if C_needed < 20 else 'requires tuning'}")

# ============================================================
# LiteBIRD forecast
# ============================================================
print(f"\n{'='*70}")
print(f"LITEBIRD FORECAST")
print(f"{'='*70}")

sigma_litebird = 0.03  # degrees (JAXA target)
sig_litebird = beta_predicted / sigma_litebird

print(f"  σ(β) = {sigma_litebird}° (LiteBIRD target, JAXA JFY2032)")
print(f"  If β = {beta_predicted}°: detection at {sig_litebird:.0f}σ")
print(f"  If β = {beta_combined:.3f}° (current central): detection at {beta_combined/sigma_litebird:.0f}σ")
print(f"  If β = 0: exclusion of prediction at {beta_predicted/sigma_litebird:.0f}σ")

# ============================================================
# Bayes factor sensitivity to prior
# ============================================================
print(f"\n{'='*70}")
print(f"BAYES FACTOR PRIOR SENSITIVITY")
print(f"{'='*70}")

for prior_width in [0.5, 1.0, 2.0, 5.0]:
    # Savage-Dickey: BF = prior_density(0) / posterior_density(0)
    # For flat prior [0, prior_width]: prior_density = 1/prior_width
    # Posterior at β=0: N(β_c, σ_c) evaluated at 0
    posterior_at_zero = np.exp(-0.5 * (beta_combined / sigma_combined)**2) / (sigma_combined * np.sqrt(2*np.pi))
    prior_at_zero = 1.0 / prior_width
    bf = prior_at_zero / posterior_at_zero
    ln_bf = np.log(bf)
    print(f"  Prior [0°, {prior_width}°]: ln(BF) = {ln_bf:.2f} (BF = {bf:.1f})")

# ============================================================
# Save results
# ============================================================
results = {
    'measurements': [{'name': m['name'], 'beta': m['beta'], 'sigma': m['sigma']}
                     for m in measurements],
    'primary_combination': {
        'datasets': 'Planck NPIPE + ACT DR6',
        'beta': round(beta_combined, 4),
        'sigma': round(sigma_combined, 4),
        'significance': round(significance_combined, 2),
    },
    'full_combination': {
        'datasets': 'Planck HFI + NPIPE + ACT DR6',
        'beta': round(beta_all, 4),
        'sigma': round(sigma_all, 4),
        'significance': round(significance_all, 2),
    },
    'bounce_prediction': {
        'beta': beta_predicted,
        'distance_from_primary': round(abs(beta_combined - beta_predicted) / sigma_combined, 3),
        'C_agamma_needed': round(C_needed, 1),
    },
    'litebird_forecast': {
        'sigma_beta': sigma_litebird,
        'significance_if_predicted': sig_litebird,
    },
}

outfile = os.path.join(os.path.dirname(__file__), 'outputs', 'combined_beta.json')
os.makedirs(os.path.dirname(outfile), exist_ok=True)
with open(outfile, 'w') as f:
    json.dump(results, f, indent=2)
print(f"\nResults saved to {outfile}")

print(f"\n{'='*70}")
print(f"PIPELINE 1C COMPLETE")
print(f"{'='*70}")
