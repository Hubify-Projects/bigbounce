#!/usr/bin/env python3
"""
P(k) Feature Window Analysis

Determines allowed/excluded regions in (k_*, A_bump) parameter space
for a primordial power spectrum feature from a bounce cosmology.

Three constraint/target layers:
1. SMBH seed helpful: A_bump large enough that P_R ~ 10^{-2} → PBH seeds form
2. PBH excluded: f_PBH(M(k_*)) exceeds observational upper limits
3. mu-distortion: FIRAS mu < 9e-5 constrains features at k < 10^4 Mpc^{-1}

Additionally marks the framework-predicted feature scale from N_tot = 92.

Author: Houston Golden (automated analysis)
Date: 2026-03-13
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from scipy.special import erfc, erfcinv

# ============================================================
# Physical constants
# ============================================================
A_s = 2.1e-9       # Standard scalar amplitude (Planck 2018)
n_s = 0.965         # Scalar spectral index
k_pivot = 0.05      # Mpc^{-1}
delta_c = 0.45       # PBH collapse threshold (radiation domination)
gamma_pbh = 0.2      # Fraction of horizon mass that collapses

# Framework parameters
N_tot = 92           # Total e-folds (from dark energy constraint)
N_pivot = 55         # e-folds before end when pivot scale exits

# ============================================================
# PBH mass <-> wavenumber mapping
# ============================================================
def k_to_M_solar(k):
    """Comoving wavenumber to PBH mass. Carr+ (2020) normalization."""
    return 33.0 * (k / 1e6)**(-2)

def M_solar_to_k(M):
    """PBH mass to comoving wavenumber."""
    return 1e6 * np.sqrt(33.0 / M)

# ============================================================
# PBH observational constraints: f_PBH upper limits
# ============================================================
def fpbh_upper_limit(log10_M_solar):
    """
    Simplified but representative PBH constraints on f_PBH = Omega_PBH/Omega_DM.
    Based on Carr, Kohri, Sendouda, Yokoyama (2020) and Green & Kavanagh (2021).
    """
    M = log10_M_solar
    if M < -19:
        return 0.0       # Fully evaporated (Hawking radiation)
    elif M < -16.5:
        return 1e-4      # Extra-galactic gamma-ray background from evaporation
    elif M < -13:
        return 1.0       # Asteroid-mass window: weakly constrained
    elif M < -11:
        return 0.3       # Kepler transit (Griest+ 2014)
    elif M < -6:
        return 0.05      # HSC/Subaru microlensing (Niikura+ 2019)
    elif M < -1:
        return 0.01      # EROS/MACHO microlensing
    elif M < 1.5:
        return 1e-3      # CMB accretion (Serpico+ 2020, Ali-Haimoud & Kamionkowski 2017)
    elif M < 4:
        return 1e-4      # CMB accretion + X-ray background
    elif M < 5:
        return 1e-3      # Wide binaries + ultra-faint dwarfs
    else:
        return 0.01      # Dynamical constraints

fpbh_upper_limit_vec = np.vectorize(fpbh_upper_limit)

# ============================================================
# P(k) → f_PBH mapping
# ============================================================
def PR_to_sigma(PR, Delta=1.0):
    """
    Smoothed variance of density perturbations from a Gaussian P(k) feature.

    sigma^2 ~ (16/81) * PR * W_eff * Delta * sqrt(2*pi)

    For a monochromatic feature at the horizon scale, W_eff ~ 0.09 (W(1)^2).
    For a Gaussian feature with width Delta in ln(k):
    sigma^2 ~ (16/81) * 0.4 * PR * Delta

    The prefactor 0.4 accounts for the window function convolution.
    See Byrnes+ (2018), Ando+ (2018) for calibrations.
    """
    # Effective prefactor calibrated to match literature threshold P_R ~ 10^{-2}
    # at sigma ~ delta_c ~ 0.45
    prefactor = 0.4 * (16.0 / 81.0) * Delta
    return np.sqrt(prefactor * PR)

def sigma_to_beta(sigma):
    """PBH formation fraction from Press-Schechter."""
    if sigma <= 0:
        return 0.0
    arg = delta_c / (np.sqrt(2) * sigma)
    if arg > 8:
        return 0.0  # Numerically zero
    return 0.5 * erfc(arg)

sigma_to_beta_vec = np.vectorize(sigma_to_beta)

def beta_to_fpbh(beta, M_solar):
    """Convert collapse fraction to present-day PBH abundance."""
    if beta <= 0 or M_solar <= 0:
        return 0.0
    return 1.3e8 * M_solar**(-0.5) * beta

# ============================================================
# mu-distortion constraint
# ============================================================
def mu_from_feature(log10_k_star, log10_A_bump, Delta=1.0):
    """
    Approximate mu-distortion from a P(k) feature.

    mu ~ 2.27 * integral of [P_R(k) - P_R_std(k)] * W_mu(k) * dk/k

    W_mu(k) is the mu-distortion window function, sensitive to
    k ~ 1 to ~10^4 Mpc^{-1} (modes dissipating at 5e4 < z < 2e6).

    For a Gaussian feature: mu ~ 2.27 * A_bump * A_s * Delta * sqrt(2*pi) * overlap
    where overlap is the fraction of the feature within the mu-sensitive range.
    """
    k_star = 10**log10_k_star
    A_bump = 10**log10_A_bump

    # mu-sensitive range
    k_mu_min = 1.0    # Mpc^{-1}
    k_mu_max = 1e4    # Mpc^{-1}

    # Fraction of Gaussian feature overlapping with mu-sensitive range
    ln_k_star = np.log(k_star)
    ln_k_min = np.log(k_mu_min)
    ln_k_max = np.log(k_mu_max)

    from scipy.special import erf
    overlap = 0.5 * (erf((ln_k_max - ln_k_star) / (np.sqrt(2) * Delta)) -
                     erf((ln_k_min - ln_k_star) / (np.sqrt(2) * Delta)))

    # P_R at feature peak
    PR_peak = A_s * (k_star / k_pivot)**(n_s - 1) * A_bump

    # mu contribution
    mu = 2.27 * PR_peak * Delta * np.sqrt(2 * np.pi) * overlap

    return mu

# ============================================================
# SMBH seed minimum P_R threshold
# ============================================================
def min_PR_for_seeds(log10_k_star):
    """
    Minimum P_R for direct PBH seed formation at mass M(k_*).

    We need f_PBH > f_PBH_min where f_PBH_min gives at least
    ~1 PBH seed per Gpc^3 (to match observed high-z SMBH density).

    n_PBH = f_PBH * rho_DM / M_PBH
    rho_DM = Omega_DM * rho_crit = 0.26 * 1.27e11 M_sun/Mpc^3

    Need n_PBH > 1e-9 Mpc^{-3} (i.e., ~1 per Gpc^3)
    """
    k_star = 10**log10_k_star
    M_solar = k_to_M_solar(k_star)

    if M_solar < 1e2 or M_solar > 1e6:
        return np.inf  # Outside SMBH seed mass range

    rho_DM = 0.26 * 1.27e11  # M_sun / Mpc^3
    n_target = 1e-9  # Mpc^{-3}, i.e. ~1 per Gpc^3

    f_pbh_min = n_target * M_solar / rho_DM

    # Invert: f_PBH = 1.3e8 * M^{-0.5} * beta
    beta_min = f_pbh_min / (1.3e8 * M_solar**(-0.5))

    if beta_min <= 0 or beta_min >= 0.5:
        return np.inf

    # Invert: beta = 0.5 * erfc(delta_c / (sqrt(2) * sigma))
    # erfc_inv(2*beta) = delta_c / (sqrt(2) * sigma)
    sigma_min = delta_c / (np.sqrt(2) * erfcinv(2 * beta_min))

    # Invert: sigma = sqrt(prefactor * P_R)
    Delta = 1.0
    prefactor = 0.4 * (16.0 / 81.0) * Delta
    PR_min = sigma_min**2 / prefactor

    return PR_min

# ============================================================
# Maximum P_R from PBH constraints
# ============================================================
def max_PR_from_pbh(log10_k_star):
    """
    Maximum P_R before violating PBH observational constraints.
    """
    k_star = 10**log10_k_star
    M_solar = k_to_M_solar(k_star)
    log10_M = np.log10(M_solar)

    f_max = fpbh_upper_limit(log10_M)

    if f_max <= 0:
        return 0.0  # Completely excluded (evaporated)

    # Invert: f_PBH = 1.3e8 * M^{-0.5} * beta
    beta_max = f_max / (1.3e8 * M_solar**(-0.5))

    if beta_max >= 0.5:
        return np.inf  # No meaningful constraint
    if beta_max <= 0:
        return 0.0

    # Invert beta → sigma
    sigma_max = delta_c / (np.sqrt(2) * erfcinv(2 * beta_max))

    # Invert sigma → P_R
    Delta = 1.0
    prefactor = 0.4 * (16.0 / 81.0) * Delta
    PR_max = sigma_max**2 / prefactor

    return PR_max

# ============================================================
# Main computation
# ============================================================

# Grid
log10_k_grid = np.linspace(1, 18, 500)
log10_PR_grid = np.linspace(-9, 0, 400)

# Framework-predicted scale
k_bounce = k_pivot * np.exp(N_tot - N_pivot)
log10_k_bounce = np.log10(k_bounce)

# SMBH seed mass range
k_smbh_min = M_solar_to_k(1e5)  # 10^5 M_sun
k_smbh_max = M_solar_to_k(1e2)  # 10^2 M_sun
log10_k_smbh_min = np.log10(k_smbh_min)
log10_k_smbh_max = np.log10(k_smbh_max)

print("=" * 60)
print("P(k) FEATURE WINDOW ANALYSIS")
print("=" * 60)
print(f"\nFramework-predicted feature scale:")
print(f"  k_bounce = {k_bounce:.2e} Mpc^-1")
print(f"  log10(k_bounce) = {log10_k_bounce:.1f}")
print(f"  M_bounce = {k_to_M_solar(k_bounce):.2e} M_sun")
print(f"\nSMBH seed scales:")
print(f"  k_SMBH = {k_smbh_min:.2e} to {k_smbh_max:.2e} Mpc^-1")
print(f"  log10(k_SMBH) = {log10_k_smbh_min:.1f} to {log10_k_smbh_max:.1f}")
print(f"\nScale mismatch:")
print(f"  Delta log10(k) = {log10_k_bounce - log10_k_smbh_max:.1f}")
print(f"  Factor = 10^{log10_k_bounce - log10_k_smbh_max:.1f}")

# Compute PBH constraint curve (max P_R vs k)
pbh_max_curve = np.array([max_PR_from_pbh(lk) for lk in log10_k_grid])
log10_pbh_max = np.where(pbh_max_curve > 0, np.log10(np.clip(pbh_max_curve, 1e-20, None)), -20)

# Compute SMBH seed threshold curve (min P_R vs k for direct PBH seeds)
smbh_min_curve = np.array([min_PR_for_seeds(lk) for lk in log10_k_grid])
log10_smbh_min = np.where(np.isfinite(smbh_min_curve), np.log10(np.clip(smbh_min_curve, 1e-20, None)), 20)

# Compute mu-distortion exclusion (for features at k < 10^4)
mu_firas_limit = 9e-5
mu_max_PR = []
for lk in log10_k_grid:
    # Binary search for max A_bump that satisfies mu < mu_firas_limit
    lo, hi = -9, 10
    for _ in range(50):
        mid = (lo + hi) / 2
        # A_bump is defined as multiplicative factor on P_R
        # So P_R_peak = A_s * (k/k_pivot)^(ns-1) * A_bump
        # We want P_R_peak directly
        k_star = 10**lk
        PR_test = 10**mid
        # Effective A_bump for this P_R
        A_bump_eff = PR_test / (A_s * (k_star / k_pivot)**(n_s - 1))
        if A_bump_eff < 1:
            A_bump_eff = 1
        mu_val = mu_from_feature(lk, np.log10(A_bump_eff))
        if mu_val < mu_firas_limit:
            lo = mid
        else:
            hi = mid
    mu_max_PR.append(lo)
mu_max_PR = np.array(mu_max_PR)

# ============================================================
# Identify allowed window
# ============================================================
# At SMBH scales, check if min_seed < max_pbh
smbh_mask = (log10_k_grid > log10_k_smbh_min) & (log10_k_grid < log10_k_smbh_max)
if np.any(smbh_mask):
    smbh_k_vals = log10_k_grid[smbh_mask]
    smbh_floor = log10_smbh_min[smbh_mask]
    smbh_ceiling = log10_pbh_max[smbh_mask]
    window_width = smbh_ceiling - smbh_floor

    # Also apply mu constraint
    mu_ceiling = mu_max_PR[smbh_mask]
    effective_ceiling = np.minimum(smbh_ceiling, mu_ceiling)
    effective_window = effective_ceiling - smbh_floor

    has_window = np.any(effective_window > 0)
    if has_window:
        max_window = np.max(effective_window)
        best_k_idx = np.argmax(effective_window)
        best_k = smbh_k_vals[best_k_idx]
        best_floor = smbh_floor[best_k_idx]
        best_ceil = effective_ceiling[best_k_idx]
        print(f"\n{'=' * 60}")
        print(f"PHENOMENOLOGICAL WINDOW EXISTS")
        print(f"{'=' * 60}")
        print(f"  Best scale: log10(k) = {best_k:.1f}")
        print(f"  P_R range: 10^{best_floor:.2f} to 10^{best_ceil:.2f}")
        print(f"  Window width: {max_window:.2f} decades in P_R")
        print(f"  PBH mass at best scale: {k_to_M_solar(10**best_k):.1e} M_sun")
    else:
        print(f"\nNO WINDOW: seed threshold > PBH constraint at all SMBH scales")
else:
    print(f"\nSMBH scales not in grid range")

# Framework prediction
print(f"\n{'=' * 60}")
print(f"FRAMEWORK PREDICTION vs WINDOW")
print(f"{'=' * 60}")
print(f"  Framework k_bounce: log10(k) = {log10_k_bounce:.1f}")
print(f"  SMBH window: log10(k) = {log10_k_smbh_min:.1f} to {log10_k_smbh_max:.1f}")
print(f"  Mismatch: {log10_k_bounce - log10_k_smbh_max:.1f} decades in k")
print(f"  Framework feature is at M ~ {k_to_M_solar(k_bounce):.1e} M_sun (sub-asteroid)")
print(f"  VERDICT: Framework does NOT predict features in the SMBH window")

# ============================================================
# FIGURE 1: Main window analysis plot
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(12, 8))

# Background: standard P_R level
ax.axhline(y=np.log10(A_s), color='gray', ls=':', alpha=0.5, label=r'Standard $\mathcal{P}_\mathcal{R}$ = 2.1×10⁻⁹')

# PBH constraint ceiling
valid_pbh = log10_pbh_max > -15
ax.plot(log10_k_grid[valid_pbh], log10_pbh_max[valid_pbh], 'r-', lw=2.5,
        label='PBH overproduction limit')
ax.fill_between(log10_k_grid[valid_pbh], log10_pbh_max[valid_pbh], 0,
                color='red', alpha=0.15)

# mu-distortion ceiling (only at k < 10^5)
mu_relevant = log10_k_grid < 5
ax.plot(log10_k_grid[mu_relevant], mu_max_PR[mu_relevant], 'b--', lw=2,
        label=r'FIRAS $\mu$ < 9×10⁻⁵')
ax.fill_between(log10_k_grid[mu_relevant], mu_max_PR[mu_relevant], 0,
                color='blue', alpha=0.1)

# SMBH seed threshold (only at SMBH scales)
smbh_valid = np.isfinite(smbh_min_curve) & (log10_smbh_min < 10)
ax.plot(log10_k_grid[smbh_valid], log10_smbh_min[smbh_valid], 'g-', lw=2.5,
        label='Min P(k) for PBH seeds (~1 per Gpc³)')

# SMBH seed mass range
ax.axvspan(log10_k_smbh_min, log10_k_smbh_max, color='green', alpha=0.08,
           label=f'SMBH seed masses (10²–10⁵ M☉)')

# Framework predicted scale
ax.axvline(x=log10_k_bounce, color='purple', ls='--', lw=2.5,
           label=f'Framework: k(N_tot=92) = 10^{{{log10_k_bounce:.0f}}} Mpc⁻¹')

# Asteroid-mass PBH window
ax.axvspan(13, 16, color='orange', alpha=0.05, label='Asteroid-mass PBH window')

# Allowed window (if exists) - shade in green
if np.any(smbh_mask):
    for i in range(len(smbh_k_vals)):
        if effective_window[i] > 0:
            ax.fill_between([smbh_k_vals[i] - 0.05, smbh_k_vals[i] + 0.05],
                           smbh_floor[i], effective_ceiling[i],
                           color='green', alpha=0.3)

# Labels and formatting
ax.set_xlabel(r'log$_{10}$(k / Mpc$^{-1}$)', fontsize=14)
ax.set_ylabel(r'log$_{10}$($\mathcal{P}_\mathcal{R}$)', fontsize=14)
ax.set_title('P(k) Feature Window Analysis: SMBH Seeds vs PBH + μ Constraints', fontsize=14)
ax.set_xlim(1, 18)
ax.set_ylim(-9.5, 0)
ax.legend(loc='upper left', fontsize=10, framealpha=0.9)
ax.grid(True, alpha=0.3)

# Add mass scale axis on top
ax2 = ax.twiny()
mass_ticks_log = [6, 4, 2, 0, -2, -4, -6, -8, -10, -12, -14, -16, -18]
mass_ticks_k = [np.log10(M_solar_to_k(10**m)) for m in mass_ticks_log]
# Filter to range
valid_ticks = [(k, m) for k, m in zip(mass_ticks_k, mass_ticks_log) if 1 <= k <= 18]
if valid_ticks:
    ax2.set_xlim(1, 18)
    ax2.set_xticks([k for k, m in valid_ticks])
    ax2.set_xticklabels([f'10$^{{{m}}}$' for k, m in valid_ticks], fontsize=9)
    ax2.set_xlabel(r'PBH mass ($M_\odot$)', fontsize=12)

# Annotation: scale mismatch arrow
ax.annotate('', xy=(log10_k_smbh_max, -1.5), xytext=(min(log10_k_bounce, 17.5), -1.5),
            arrowprops=dict(arrowstyle='<->', color='purple', lw=2))
mismatch_mid = (log10_k_smbh_max + min(log10_k_bounce, 17.5)) / 2
ax.text(mismatch_mid, -1.2, f'~10$^{{{log10_k_bounce - log10_k_smbh_max:.0f}}}$ scale mismatch',
        ha='center', fontsize=11, color='purple', fontweight='bold')

# Add text box with key findings
textstr = (f'Framework feature: k ≈ 10$^{{{log10_k_bounce:.0f}}}$ Mpc$^{{-1}}$ (M ≈ 10$^{{-16}}$ M$_☉$)\n'
           f'SMBH seeds need: k ≈ 10$^{{4-6}}$ Mpc$^{{-1}}$ (M ≈ 10$^{{2-5}}$ M$_☉$)\n'
           f'Mismatch: ~10$^{{{log10_k_bounce - log10_k_smbh_max:.0f}}}$ in k, ~10$^{{20}}$ in mass')
props = dict(boxstyle='round', facecolor='lightyellow', alpha=0.9, edgecolor='orange')
ax.text(0.98, 0.02, textstr, transform=ax.transAxes, fontsize=10,
        verticalalignment='bottom', horizontalalignment='right', bbox=props)

plt.tight_layout()
plt.savefig('pk_feature_window_analysis.pdf', dpi=150, bbox_inches='tight')
plt.savefig('pk_feature_window_analysis.png', dpi=150, bbox_inches='tight')
print(f"\nFigure saved: pk_feature_window_analysis.pdf/png")

# ============================================================
# FIGURE 2: Zoomed SMBH window with seed threshold detail
# ============================================================
fig2, ax3 = plt.subplots(1, 1, figsize=(10, 7))

# Zoom to SMBH-relevant range
k_zoom_min, k_zoom_max = 3.5, 6.5
pr_zoom_min, pr_zoom_max = -4, 0

zoom_mask = (log10_k_grid > k_zoom_min) & (log10_k_grid < k_zoom_max)

# PBH constraint
ax3.plot(log10_k_grid[zoom_mask], log10_pbh_max[zoom_mask], 'r-', lw=2.5,
         label='PBH overproduction limit')
ax3.fill_between(log10_k_grid[zoom_mask], log10_pbh_max[zoom_mask], pr_zoom_max,
                 color='red', alpha=0.2, label='PBH excluded')

# SMBH seed threshold
smbh_zoom = zoom_mask & smbh_valid
ax3.plot(log10_k_grid[smbh_zoom], log10_smbh_min[smbh_zoom], 'g-', lw=2.5,
         label='Min P(k) for 1 PBH seed per Gpc³')

# Allowed window (green shading between green and red curves)
for i, lk in enumerate(log10_k_grid):
    if k_zoom_min < lk < k_zoom_max and smbh_valid[i]:
        if log10_smbh_min[i] < log10_pbh_max[i] and log10_smbh_min[i] < 10:
            ax3.fill_between([lk - 0.02, lk + 0.02],
                            log10_smbh_min[i], log10_pbh_max[i],
                            color='green', alpha=0.15)

# Standard P_R level
ax3.axhline(y=np.log10(A_s), color='gray', ls=':', alpha=0.5, label=r'Standard $\mathcal{P}_\mathcal{R}$')

# mu-distortion ceiling
mu_zoom = zoom_mask & mu_relevant
if np.any(mu_zoom):
    ax3.plot(log10_k_grid[mu_zoom], mu_max_PR[mu_zoom], 'b--', lw=2,
             label=r'FIRAS $\mu$-distortion limit')

ax3.set_xlabel(r'log$_{10}$(k / Mpc$^{-1}$)', fontsize=14)
ax3.set_ylabel(r'log$_{10}$($\mathcal{P}_\mathcal{R}$)', fontsize=14)
ax3.set_title('Zoomed: Phenomenological SMBH Seed Window\n(Framework does NOT predict features here)', fontsize=13)
ax3.set_xlim(k_zoom_min, k_zoom_max)
ax3.set_ylim(pr_zoom_min, pr_zoom_max)
ax3.legend(loc='upper left', fontsize=10, framealpha=0.9)
ax3.grid(True, alpha=0.3)

# Add mass labels
for M_label in [1e2, 1e3, 1e4, 1e5]:
    k_label = np.log10(M_solar_to_k(M_label))
    if k_zoom_min < k_label < k_zoom_max:
        ax3.axvline(x=k_label, color='gray', ls=':', alpha=0.3)
        ax3.text(k_label, pr_zoom_max - 0.1, f'{M_label:.0e} M☉', rotation=90,
                va='top', ha='right', fontsize=9, color='gray')

# Key result annotation
ax3.text(0.5, 0.05,
         'Narrow phenomenological window exists (~1-2 decades in P(k))\n'
         'BUT: framework predicts features at k ~ 10¹⁵, not here',
         transform=ax3.transAxes, fontsize=11, ha='center',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9, edgecolor='red'))

plt.tight_layout()
plt.savefig('pk_feature_smbh_zoom.pdf', dpi=150, bbox_inches='tight')
plt.savefig('pk_feature_smbh_zoom.png', dpi=150, bbox_inches='tight')
print(f"Figure saved: pk_feature_smbh_zoom.pdf/png")

# ============================================================
# Summary statistics
# ============================================================
print(f"\n{'=' * 60}")
print(f"SUMMARY")
print(f"{'=' * 60}")
print(f"\n1. SCALE MISMATCH:")
print(f"   Framework predicts k_feature ~ 10^{log10_k_bounce:.0f} Mpc^-1")
print(f"   SMBH seeds need k ~ 10^{log10_k_smbh_min:.0f} to 10^{log10_k_smbh_max:.0f} Mpc^-1")
print(f"   Mismatch: ~10^{log10_k_bounce - log10_k_smbh_max:.0f} in wavenumber")
print(f"             ~10^{2*(log10_k_bounce - log10_k_smbh_max):.0f} in mass")

print(f"\n2. PHENOMENOLOGICAL WINDOW (ignoring framework scale prediction):")
if has_window:
    print(f"   EXISTS: P_R ~ 10^{best_floor:.1f} to 10^{best_ceil:.1f} at k ~ 10^{best_k:.1f}")
    print(f"   Width: ~{max_window:.1f} decades in P_R amplitude")
    print(f"   This is a NARROW window (erfc threshold is steep)")
else:
    print(f"   NO WINDOW found")

print(f"\n3. FRAMEWORK PREDICTION AT BOUNCE SCALE:")
M_at_bounce = k_to_M_solar(k_bounce)
log10_M_bounce = np.log10(M_at_bounce)
f_limit_bounce = fpbh_upper_limit(log10_M_bounce)
print(f"   M_PBH ~ {M_at_bounce:.1e} M_sun (sub-asteroid)")
print(f"   PBH constraint: f_PBH < {f_limit_bounce}")
if f_limit_bounce >= 0.3:
    print(f"   -> In the weakly constrained asteroid-mass window")
    print(f"   -> Potentially interesting for PBH dark matter, NOT for SMBH seeds")

print(f"\n4. VERDICT:")
print(f"   The framework does NOT naturally produce SMBH-relevant features.")
print(f"   The scale mismatch is ~10^{log10_k_bounce - log10_k_smbh_max:.0f} and cannot be")
print(f"   bridged without abandoning the N_tot = 92 dark energy constraint.")
print(f"   A phenomenological window exists but the framework doesn't target it.")

# Save summary to text file
with open('window_analysis_summary.txt', 'w') as f:
    f.write("P(k) FEATURE WINDOW ANALYSIS SUMMARY\n")
    f.write(f"Date: 2026-03-13\n")
    f.write(f"{'=' * 50}\n\n")
    f.write(f"Framework feature scale: k = {k_bounce:.2e} Mpc^-1\n")
    f.write(f"Framework feature mass: M = {k_to_M_solar(k_bounce):.2e} M_sun\n")
    f.write(f"SMBH seed scales: k = {10**log10_k_smbh_min:.2e} to {10**log10_k_smbh_max:.2e} Mpc^-1\n")
    f.write(f"Scale mismatch: 10^{log10_k_bounce - log10_k_smbh_max:.0f} in k\n")
    f.write(f"Mass mismatch: 10^{2*(log10_k_bounce - log10_k_smbh_max):.0f} in mass\n\n")
    if has_window:
        f.write(f"Phenomenological window: EXISTS (narrow)\n")
        f.write(f"  Best scale: k ~ 10^{best_k:.1f} Mpc^-1\n")
        f.write(f"  P_R range: 10^{best_floor:.2f} to 10^{best_ceil:.2f}\n")
        f.write(f"  Width: {max_window:.2f} decades\n")
    else:
        f.write(f"Phenomenological window: NONE\n")
    f.write(f"\nVERDICT: Framework scale mismatch prevents SMBH seed connection.\n")
    f.write(f"Feature at k ~ 10^15 is in asteroid-mass PBH window (weakly constrained).\n")
    f.write(f"Possibly relevant for PBH dark matter, NOT for early SMBH seeds.\n")

print(f"\nSummary saved: window_analysis_summary.txt")
