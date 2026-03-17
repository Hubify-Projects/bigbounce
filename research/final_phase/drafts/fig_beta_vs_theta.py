#!/usr/bin/env python3
"""
Figure: β vs θ_i prediction plot for the spectator ALP model.

Shows:
- Blue line: β = (C α_em / 4π) × θ_i  for C=8, η=1
- Orange horizontal band: β_obs = 0.342 ± 0.094°
- Green vertical band: θ_i = 1.36 ± 0.44 (MCMC posterior 68% CI)
- Gray shading: "natural" region θ_i ∈ [0, π]
- Dashed lines: η = 0.5 and η = 0.8 curves

This is the "money plot" — Figure 4 in the paper plan.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# ── Constants ──
alpha_em = 1.0 / 137.036
C_agamma = 8.0
coeff = C_agamma * alpha_em / (4.0 * np.pi)  # ≈ 0.00465 rad ≈ 0.2665°

# Convert to degrees
coeff_deg = np.degrees(coeff)  # β per unit θ_i, in degrees

# ── Data ──
beta_obs = 0.342   # degrees
sigma_beta = 0.094  # degrees

theta_i_mean = 1.36
theta_i_sigma = 0.44

# ── Axes ──
theta_arr = np.linspace(0, np.pi, 500)

beta_eta1 = coeff_deg * theta_arr          # η = 1.0
beta_eta08 = coeff_deg * theta_arr * 0.8   # η = 0.8
beta_eta05 = coeff_deg * theta_arr * 0.5   # η = 0.5

# ── Figure ──
fig, ax = plt.subplots(figsize=(7, 5))

# Gray background for "natural" region
ax.axvspan(0, np.pi, alpha=0.04, color='gray', zorder=0)

# Observation band (horizontal)
ax.axhspan(beta_obs - sigma_beta, beta_obs + sigma_beta,
           alpha=0.25, color='#E8833A', zorder=1,
           label=r'$\beta_\mathrm{obs} = 0.342 \pm 0.094°$')
ax.axhspan(beta_obs - 2*sigma_beta, beta_obs + 2*sigma_beta,
           alpha=0.10, color='#E8833A', zorder=0)
ax.axhline(beta_obs, color='#E8833A', lw=1.0, ls='-', alpha=0.7, zorder=2)

# Posterior band (vertical)
ax.axvspan(theta_i_mean - theta_i_sigma, theta_i_mean + theta_i_sigma,
           alpha=0.20, color='#4DAF4A', zorder=1,
           label=r'$\theta_i = 1.36 \pm 0.44$ (68\% CI)')
ax.axvspan(theta_i_mean - 2*theta_i_sigma, theta_i_mean + 2*theta_i_sigma,
           alpha=0.08, color='#4DAF4A', zorder=0)
ax.axvline(theta_i_mean, color='#4DAF4A', lw=1.0, ls='-', alpha=0.7, zorder=2)

# Prediction lines
ax.plot(theta_arr, beta_eta1, color='#377EB8', lw=2.5, zorder=5,
        label=r'$\beta = \frac{C\alpha}{4\pi}\,\theta_i$  ($\eta = 1$, $C = 8$)')
ax.plot(theta_arr, beta_eta08, color='#377EB8', lw=1.5, ls='--', alpha=0.6,
        zorder=4, label=r'$\eta = 0.8$')
ax.plot(theta_arr, beta_eta05, color='#377EB8', lw=1.5, ls=':', alpha=0.5,
        zorder=4, label=r'$\eta = 0.5$')

# Intersection marker
beta_at_posterior = coeff_deg * theta_i_mean
ax.plot(theta_i_mean, beta_at_posterior, 'o', color='#377EB8',
        markersize=8, markeredgecolor='white', markeredgewidth=1.5, zorder=10)

# Null line
ax.axhline(0, color='black', lw=0.5, ls='-', alpha=0.3)

# ── Annotations ──
ax.annotate(r'$\beta = 0.27° \times \theta_i$',
            xy=(2.4, coeff_deg * 2.4), xytext=(2.6, 0.80),
            fontsize=10, color='#377EB8',
            arrowprops=dict(arrowstyle='->', color='#377EB8', lw=1.2))

ax.annotate(r'$\beta = 0$  (null)',
            xy=(2.8, 0.0), xytext=(2.8, -0.08),
            fontsize=9, color='gray', ha='center')

# Mark π
ax.axvline(np.pi, color='gray', lw=0.5, ls='--', alpha=0.5)
ax.text(np.pi + 0.03, -0.05, r'$\pi$', fontsize=10, color='gray')

# ── Formatting ──
ax.set_xlabel(r'Initial misalignment angle $\theta_i$', fontsize=13)
ax.set_ylabel(r'Birefringence angle $\beta$ [deg]', fontsize=13)
ax.set_xlim(0, np.pi + 0.15)
ax.set_ylim(-0.15, 1.05)
ax.tick_params(labelsize=11)
ax.legend(loc='upper left', fontsize=9, framealpha=0.9)

# Title (optional — remove for publication)
# ax.set_title('Spectator ALP Birefringence Prediction', fontsize=13)

fig.tight_layout()

# ── Save ──
outdir = '/Users/houstongolden/Desktop/CODE_2026/bigbounce/research/final_phase/drafts'
fig.savefig(f'{outdir}/fig_beta_vs_theta.png', dpi=300, bbox_inches='tight')
fig.savefig(f'{outdir}/fig_beta_vs_theta.pdf', dpi=300, bbox_inches='tight')
print(f"Saved to {outdir}/fig_beta_vs_theta.png and .pdf")
print(f"Fiducial: β(θ_i=1) = {coeff_deg:.4f}°")
print(f"Posterior: β(θ_i=1.36) = {coeff_deg * 1.36:.4f}°")
print(f"Observed: β = {beta_obs} ± {sigma_beta}°")
