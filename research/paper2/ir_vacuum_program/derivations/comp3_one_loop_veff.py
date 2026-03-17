#!/usr/bin/env python3
"""
Computation 4: One-Loop Effective Potential with Curvature Corrections
======================================================================

Reference: Canonical Problem Statement §Q3 Step 3, §Q6 Gate 1
Input: Fierz-rearranged interaction in S/P channels (Computation 3)
Output: V_eff(σ, π; R) at one loop, including gravitational catalysis

THE KEY QUESTION: Can curvature corrections at R ~ M_Pl² overcome
the tree-level repulsion in the scalar/pseudoscalar channel at γ = 0.274?

Status: APPROXIMATION (one-loop semiclassical truncation + heat-kernel expansion)

Key references:
  - Inagaki, Muta, Odintsov (1997) — NJL gap equation in curved spacetime
  - Gorbar, Gusynin (2008) — gravitational catalysis
  - Parker, Toms (2009) — QFT in curved spacetime, heat-kernel methods
  - Elizalde, Odintsov, Romeo (1994) — improved effective potential
"""

import numpy as np
from scipy.optimize import fsolve, minimize_scalar, minimize
from scipy.integrate import quad
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

print("=" * 70)
print("COMPUTATION 4: ONE-LOOP EFFECTIVE POTENTIAL")
print("Including curvature corrections (gravitational catalysis)")
print("=" * 70)

# =============================================================================
# PHYSICAL SETUP
# =============================================================================
#
# After Fierz rearrangement and Hubbard-Stratonovich, the action is:
#
#   S = ∫ d⁴x √-g [ψ̄(iγ^μD_μ - m - σ - iγ⁵π)ψ + V_tree(σ,π)]
#
# where V_tree comes from the HS transformation of the four-fermion interaction.
#
# From Computation 3, the scalar/pseudoscalar interaction for single-flavor is:
#
#   L_SP = G_SP [(ψ̄ψ)² + (ψ̄iγ⁵ψ)²]
#
# where G_SP = G_eff × (1 - 1/γ²) with G_eff = (3κ²/16) × γ²/(γ²+1)
#
# So: G_SP = (3κ²/16) × γ²/(γ²+1) × (γ²-1)/γ² = (3κ²/16) × (γ²-1)/(γ²+1)
#
# At γ = 0.274: G_SP < 0 (in the convention where L = +G_SP × bilinear²)
#
# After HS transformation with auxiliary fields σ, π:
#
#   V_tree(σ, π) = (σ² + π²) / (4|G_SP|)     [for repulsive G_SP]
#
# The effective fermion mass in the σ, π background is:
#   M_eff² = (m + σ)² + π²
#
# The one-loop effective potential (fermion determinant) is:
#   V_1loop = -(N_c N_f / 2) × Tr ln[-D² + M_eff² + ξR]
#
# where D² is the covariant d'Alembertian and ξR is the curvature coupling.
#
# For a Dirac fermion, after squaring the Dirac operator:
#   (iγ^μD_μ - M_eff)(-iγ^νD_ν - M_eff) = -D² + M_eff² + (R/4)
#
# The R/4 comes from the spin connection (it's the standard spin-curvature
# coupling for Dirac fermions in curved spacetime).

# =============================================================================
# PARAMETERS
# =============================================================================

# Barbero-Immirzi parameter
gamma_BI = 0.274

# Gravitational coupling
# κ² = 8πG = 1/M_Pl²
# We work in Planck units: M_Pl = 1, so κ² = 1

kappa_sq = 1.0  # In Planck units
M_Pl = 1.0

# Effective four-fermion coupling in S/P channel
# G_SP = (3κ²/16) × (γ²-1)/(γ²+1)
G_SP = (3 * kappa_sq / 16) * (gamma_BI**2 - 1) / (gamma_BI**2 + 1)

print(f"\nParameters:")
print(f"  γ = {gamma_BI}")
print(f"  κ² = {kappa_sq} (Planck units)")
print(f"  G_SP = {G_SP:.6f} (negative = repulsive in S/P channel)")
print(f"  |G_SP| = {abs(G_SP):.6f}")

# Number of colors and flavors
N_c = 1   # gravitational coupling is color-blind
N_f = 1   # single flavor first (we'll scan N_f later)

# Bare fermion mass (set to 0 for chiral limit first)
m_bare = 0.0

# UV cutoff (for proper-time regularization cross-check)
# In dim reg we don't need this, but for the NJL model it's natural
Lambda_UV = 1.0  # Planck scale

print(f"  N_c = {N_c}, N_f = {N_f}")
print(f"  m_bare = {m_bare}")

# =============================================================================
# STEP 1: TREE-LEVEL POTENTIAL
# =============================================================================

print("\n" + "=" * 70)
print("STEP 1: TREE-LEVEL POTENTIAL")
print("=" * 70)

# For the HS transformation of a REPULSIVE interaction (G_SP < 0):
#
# The four-fermion term is: G_SP [(ψ̄ψ)² + (ψ̄iγ⁵ψ)²]
# with G_SP < 0 (repulsive).
#
# HS transformation:
#   exp(G_SP ∫ [(ψ̄ψ)² + (ψ̄iγ⁵ψ)²])
#   = ∫ Dσ Dπ exp(-∫ [σ²+π²]/(4|G_SP|) + √(|G_SP|)(σ ψ̄ψ + π ψ̄iγ⁵ψ))
#
# Wait — the HS transformation requires the interaction to be ATTRACTIVE
# (negative coupling in the exponent) for the Gaussian integral to converge.
# For a REPULSIVE interaction, the HS transformation doesn't work in the
# standard way.
#
# This is actually the fundamental issue: the HS transformation of a
# repulsive four-fermion interaction does NOT produce a bounded effective
# potential. The Gaussian integral diverges.
#
# HOWEVER: the standard NJL approach is to introduce the auxiliary fields
# regardless, with the understanding that:
# 1. The tree-level potential is an INVERTED parabola (unstable)
# 2. The one-loop fermion determinant may stabilize it
#
# For an attractive interaction (G > 0):
#   V_tree = (σ² + π²) / (4G)  [bowl — stable at origin]
#   V_1loop = -f(M_eff)         [negative, deepens at large M_eff]
#   V_total may have minimum away from origin → condensation
#
# For a repulsive interaction (G < 0):
#   V_tree = -(σ² + π²) / (4|G|)  [inverted bowl — unstable at origin]
#   V_1loop = -f(M_eff)             [negative]
#   V_total is unbounded below → NO condensation via standard NJL
#
# So the repulsive S/P channel DEFINITELY cannot condense via standard NJL.
#
# BUT: with curvature corrections, the situation changes.
# The curvature R effectively shifts the mass²:
#   m² → m² + ξR
# For Dirac fermions, ξ = 1/4.
# At the bounce, R ~ M_Pl² ~ 1 (in Planck units).
#
# This means the fermion is effectively MASSIVE even in the chiral limit.
# The one-loop potential then has a different structure.
#
# Let me compute both cases and compare.

# Actually, let me reconsider. The problem is more subtle.
#
# The STANDARD approach to gravitational catalysis (Gorbar & Gusynin 2008,
# Inagaki, Muta & Odintsov 1997) works as follows:
#
# Start with an ATTRACTIVE four-fermion interaction (G > 0).
# In flat spacetime, condensation requires G > G_crit.
# In curved spacetime, the critical coupling is LOWERED:
#   G_crit(R) < G_crit(R=0)
#
# So curvature helps an already-attractive channel condense more easily.
#
# But in our case, the channel is REPULSIVE (G < 0). Curvature cannot
# make a repulsive channel attractive — it can only lower the threshold
# for an already-attractive channel.
#
# HOWEVER: there's a different mechanism. Even without the four-fermion
# interaction, the one-loop effective potential in curved spacetime can
# generate a nonzero vacuum expectation value for a scalar field through
# the curvature coupling. This is "curvature-induced symmetry breaking"
# (not catalysis of an existing interaction).
#
# For a scalar field φ with mass m and coupling ξ to R:
#   V_1loop ∝ ... + (R/12 - ξR) φ² + ...
# If (1/12 - ξ) R < 0, the effective mass² becomes negative → symmetry breaking.
# For conformal coupling ξ = 1/6, this is marginal.
# For minimal coupling ξ = 0, this gives m²_eff = m² + R/12.
#
# But our σ, π are AUXILIARY fields, not fundamental scalars.
# Their mass term comes entirely from the HS transformation.
# The curvature coupling arises through the fermion loop.

print()
print("The standard NJL condensation route is BLOCKED for repulsive G_SP.")
print("Investigating whether CURVATURE ALONE can induce condensation.")
print()

# =============================================================================
# STEP 2: ONE-LOOP EFFECTIVE POTENTIAL IN CURVED SPACETIME
# =============================================================================
#
# For the NJL model in curved spacetime (Inagaki, Muta, Odintsov 1997):
#
# The one-loop effective potential for a Dirac fermion with effective mass
# M in a background with constant curvature R (de Sitter) is:
#
#   V_1loop(M; R) = -(N_c N_f / 16π²) × {
#       Λ² M² - (M⁴/2) ln(M²/μ²) + M⁴/4
#       - (R/12) [M² ln(M²/μ²) - M²]
#       + (R²/2880) [2 ln(M²/μ²) + ...]
#       + O(R³/M²)
#   }
#
# In dimensional regularization (our primary scheme):
#
#   V_1loop(M; R) = -(N_c N_f / 16π²) × {
#       (M⁴/2) [ln(M²/μ²) - 3/2]
#       + (R/12) M² [1 - ln(M²/μ²)]
#       + (11R²/720π²) [ln(M²/μ²) - const]
#       + O(R³)
#   }
#
# Wait, I need to be more careful. Let me use the standard Schwinger-DeWitt
# expansion for the effective potential.
#
# For a Dirac fermion with squared operator D² = -□ + M² + E
# where E = R/4 (spin-curvature coupling for Dirac), the effective potential is:
#
# V_eff = V_tree + V_1loop
#
# V_1loop = -(1/2) × (1/16π²) × 4 × N_c × N_f × {
#     (M² + R/4)² [ln((M² + R/4)/μ²) - 3/2]
#     + (a₂ terms involving R², R_μν², etc.)
# }
#
# The factor of 4 comes from the Dirac trace (4 spinor components).
# The factor of 1/2 would be for a real scalar; for Dirac it's different.
#
# Actually, for Dirac fermions:
# V_1loop = +(N_c N_f / 16π²) × 2 × {
#     (M_eff²)² [ln(M_eff²/μ²) - 3/2]
# }
#
# where M_eff² = M² + R/4 at leading order in the adiabatic expansion.
#
# NO WAIT. I need to get this right. Let me use the STANDARD result.
#
# For a Dirac fermion of mass M in d=4 with dim reg:
#
# V_1loop = -2 N_c N_f / (16π²) × M⁴ × [ln(M²/μ²) - 3/2]  [FLAT SPACE]
#
# The -2 accounts for: -1 (fermion) × 4 (Dirac trace) / 2 (the 1/2 in dim reg)
# = -2. CHECK: this matches Coleman-Weinberg for fermions.
#
# In curved spacetime, M² → M² + R/4 at leading order, plus higher-order
# curvature corrections.
#
# The leading curvature correction to the gap equation is through the
# shift M² → M² + R/4 in the fermion propagator. This is the
# "gravitational catalysis" effect.

print("=" * 70)
print("STEP 2: ONE-LOOP EFFECTIVE POTENTIAL")
print("=" * 70)

# =============================================================================
# THE EFFECTIVE POTENTIAL (PROPER-TIME REGULARIZATION)
# =============================================================================
#
# For the NJL model in curved spacetime, the proper-time regulated
# effective potential is (Inagaki et al. 1997, eq. 3.3):
#
#   V_eff(M; R) = (M - m)² / (4G)
#                 - (N_c / 4π²) ∫_{1/Λ²}^∞ ds/s³ × exp(-M²s) × [1 + (R/12)s + ...]
#
# where M = m + σ (for the scalar channel, with π = 0 by O(2) symmetry)
# and G > 0 is the ATTRACTIVE coupling.
#
# For our case with REPULSIVE coupling:
#   V_tree = -(M - m)² / (4|G_SP|)
#
# But let me think about this differently.
#
# The correct approach for the one-loop potential with curvature:
# Use the FULL expression, not separated into tree + loop.
#
# Actually, the key insight from Gorbar & Gusynin (2008) and Inagaki et al. (1997)
# is that gravitational catalysis works by modifying the GAP EQUATION, not by
# changing the sign of the coupling. Let me work with the gap equation directly.

# =============================================================================
# THE GAP EQUATION IN CURVED SPACETIME
# =============================================================================
#
# The gap equation is ∂V_eff/∂M = 0, which gives:
#
#   M = m + 2G × ⟨ψ̄ψ⟩
#
# where the condensate in curved spacetime is:
#
#   ⟨ψ̄ψ⟩ = -(N_c / 4π²) ∫ ds/s² × M × exp(-M²s) × [1 + (R/12)s + ...]
#
# In proper-time regularization with cutoff Λ:
#
#   ⟨ψ̄ψ⟩ = -(N_c M / 4π²) × [Λ² - M² ln(1 + Λ²/M²) + (R/12) ln(1 + Λ²/M²) + ...]
#
# The gap equation then becomes:
#
#   M = m + (N_c G M / 2π²) × [Λ² - M² ln(1 + Λ²/M²) + (R/12) ln(1 + Λ²/M²)]
#
# For the chiral limit (m = 0), dividing by M:
#   1 = (N_c G / 2π²) × [Λ² - M² ln(1 + Λ²/M²) + (R/12) ln(1 + Λ²/M²)]
#
# This has a nontrivial solution M ≠ 0 if the RHS > 1 at M = 0.
# At M = 0: RHS = (N_c G / 2π²) × [Λ² + (R/12) × ∞]
#
# The R/12 × ln(Λ²/M²) diverges as M → 0! This means:
#
# FOR ANY G > 0 (no matter how small), in the presence of curvature R > 0,
# the gap equation ALWAYS has a nontrivial solution.
#
# THIS IS GRAVITATIONAL CATALYSIS.
#
# But for G < 0 (repulsive), the gap equation is:
#   1 = (N_c G / 2π²) × [...]  with G < 0
#   → LHS = 1 > 0, RHS < 0
#   → NO SOLUTION
#
# So gravitational catalysis DOES NOT HELP with a repulsive coupling.
# The gap equation for the scalar/pseudoscalar channel has no nontrivial
# solution when G_SP < 0, regardless of curvature.

print()
print("THE GAP EQUATION ANALYSIS:")
print()
print("For ATTRACTIVE G > 0:")
print("  Gap equation: 1 = (N_c G / 2π²) × f(M, Λ, R)")
print("  where f > 0 and diverges logarithmically at M = 0 for R > 0")
print("  → Nontrivial solution ALWAYS exists (gravitational catalysis)")
print()
print("For REPULSIVE G < 0 (our case at γ = 0.274):")
print("  Gap equation: 1 = (N_c G / 2π²) × f(M, Λ, R)")
print("  LHS = 1 > 0, RHS < 0 for all M, R")
print("  → NO nontrivial solution exists")
print("  → Gravitational catalysis CANNOT help")
print()
print("★★★ GRAVITATIONAL CATALYSIS IS BLOCKED FOR REPULSIVE CHANNELS ★★★")
print()
print("This is because catalysis lowers the THRESHOLD for condensation,")
print("but it cannot reverse the SIGN of the coupling.")

# =============================================================================
# HOWEVER: CHECK THE FULL V_eff NUMERICALLY
# =============================================================================
#
# Let me still compute V_eff numerically to make absolutely sure.
# Maybe there's a subtlety I'm missing.

print("\n" + "=" * 70)
print("NUMERICAL CHECK: FULL V_eff(M; R) IN PROPER-TIME REGULARIZATION")
print("=" * 70)

def V_eff_flat(M, G_coupling, Lambda, N_c_val, m=0.0):
    """
    NJL effective potential in flat spacetime, proper-time regularization.

    V = (M-m)²/(4G) - (N_c/8π²)[Λ²M² - M⁴ ln(1 + Λ²/M²)/2 + ...]

    For G < 0 (repulsive), V_tree = -(M-m)²/(4|G|)
    """
    M2 = M**2
    if M2 < 1e-30:
        M2 = 1e-30

    # Tree-level
    V_tree = (M - m)**2 / (4 * G_coupling)
    # Note: for G < 0, this is -(M-m)²/(4|G|), i.e., an inverted parabola

    # One-loop (proper-time regularized)
    L2 = Lambda**2
    V_loop = -(N_c_val / (8 * np.pi**2)) * (
        L2 * M2
        - (M2**2 / 2) * np.log(1 + L2/M2)
        - L2 * M2 / 2  # Subtraction
        + M2**2 / 4
    )

    return V_tree + V_loop

def V_eff_curved(M, G_coupling, Lambda, N_c_val, R, m=0.0):
    """
    NJL effective potential in curved spacetime (leading curvature correction).

    Additional term from R/4 shift in fermion propagator (Dirac spin coupling)
    and R/12 from heat-kernel a₁ coefficient.

    The leading curvature correction adds:
    δV = -(N_c/8π²) × (R/12) × [M² ln(1+Λ²/M²) - Λ²]  (approximate)

    More precisely, following Inagaki et al. (1997):
    The effective mass² in the fermion loop gets shifted M² → M² + R/4
    (for minimal coupling in EC gravity, the Dirac fermion has ξ = 1/4).
    """
    M2 = M**2
    if M2 < 1e-30:
        M2 = 1e-30

    # Effective mass including curvature
    M2_eff = M2 + R / 4  # Dirac spin-curvature coupling

    if M2_eff < 1e-30:
        M2_eff = 1e-30

    # Tree-level (unchanged — involves the bare auxiliary field)
    V_tree = (M - m)**2 / (4 * G_coupling)

    # One-loop with effective mass
    L2 = Lambda**2
    V_loop = -(N_c_val / (8 * np.pi**2)) * (
        L2 * M2_eff
        - (M2_eff**2 / 2) * np.log(1 + L2/M2_eff)
        - L2 * M2_eff / 2
        + M2_eff**2 / 4
    )

    return V_tree + V_loop

# Scan V_eff as a function of M for different R values
M_range = np.linspace(0.001, 2.0, 500)

# Case 1: Repulsive coupling (our case, γ = 0.274)
print(f"\nCase 1: Repulsive coupling G_SP = {G_SP:.4f}")

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Flat spacetime
V_flat = [V_eff_flat(M, G_SP, Lambda_UV, N_c, m_bare) for M in M_range]
V_flat = np.array(V_flat)
V_flat -= V_flat[0]  # Normalize to V(M≈0) = 0

axes[0].plot(M_range, V_flat, 'b-', linewidth=2, label='R = 0 (flat)')

# Curved spacetime at various R
R_values = [0.1, 0.5, 1.0, 2.0, 5.0]
colors = ['g', 'orange', 'r', 'purple', 'brown']

for R_val, col in zip(R_values, colors):
    V_curved = [V_eff_curved(M, G_SP, Lambda_UV, N_c, R_val, m_bare) for M in M_range]
    V_curved = np.array(V_curved)
    V_curved -= V_curved[0]
    axes[0].plot(M_range, V_curved, color=col, linewidth=1.5,
                label=f'R = {R_val} M_Pl²')

axes[0].set_xlabel('M (effective mass) [M_Pl]')
axes[0].set_ylabel('V_eff(M) - V_eff(0) [M_Pl⁴]')
axes[0].set_title(f'REPULSIVE channel (γ={gamma_BI}, G_SP={G_SP:.4f})')
axes[0].legend(fontsize=8)
axes[0].set_ylim([-1, 2])
axes[0].axhline(y=0, color='k', linewidth=0.5, linestyle='--')
axes[0].grid(True, alpha=0.3)

# Case 2: For comparison, attractive coupling (what γ > 1 would give)
gamma_attractive = 2.0
G_SP_attr = (3 * kappa_sq / 16) * (gamma_attractive**2 - 1) / (gamma_attractive**2 + 1)
print(f"\nCase 2: Attractive coupling at γ = {gamma_attractive}, G_SP = {G_SP_attr:.4f}")

V_flat_attr = [V_eff_flat(M, G_SP_attr, Lambda_UV, N_c, m_bare) for M in M_range]
V_flat_attr = np.array(V_flat_attr)
V_flat_attr -= V_flat_attr[0]

axes[1].plot(M_range, V_flat_attr, 'b-', linewidth=2, label='R = 0 (flat)')

for R_val, col in zip(R_values, colors):
    V_curved_attr = [V_eff_curved(M, G_SP_attr, Lambda_UV, N_c, R_val, m_bare) for M in M_range]
    V_curved_attr = np.array(V_curved_attr)
    V_curved_attr -= V_curved_attr[0]
    axes[1].plot(M_range, V_curved_attr, color=col, linewidth=1.5,
                label=f'R = {R_val} M_Pl²')

axes[1].set_xlabel('M (effective mass) [M_Pl]')
axes[1].set_ylabel('V_eff(M) - V_eff(0) [M_Pl⁴]')
axes[1].set_title(f'ATTRACTIVE channel (γ={gamma_attractive}, G_SP={G_SP_attr:.4f})')
axes[1].legend(fontsize=8)
axes[1].set_ylim([-1, 2])
axes[1].axhline(y=0, color='k', linewidth=0.5, linestyle='--')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/Users/houstongolden/Desktop/CODE_2026/bigbounce/research/paper2/ir_vacuum_program/figures/veff_repulsive_vs_attractive.png', dpi=150)
print("\nFigure saved: figures/veff_repulsive_vs_attractive.png")

# =============================================================================
# STEP 3: SCAN OVER γ — WHERE DOES CONDENSATION BECOME POSSIBLE?
# =============================================================================

print("\n" + "=" * 70)
print("STEP 3: γ SCAN — CRITICAL γ FOR CONDENSATION")
print("=" * 70)

def has_nontrivial_minimum(gamma_val, R_val, Lambda, N_c_val, m=0.0):
    """Check if V_eff has a minimum at M > 0."""
    G = (3 * kappa_sq / 16) * (gamma_val**2 - 1) / (gamma_val**2 + 1)

    M_test = np.linspace(0.01, 3.0, 1000)
    V_test = np.array([V_eff_curved(M, G, Lambda, N_c_val, R_val, m) for M in M_test])
    V_test -= V_test[0]

    # Look for a minimum below zero
    min_idx = np.argmin(V_test)
    if min_idx > 0 and min_idx < len(V_test) - 1:
        if V_test[min_idx] < -1e-10:
            return True, M_test[min_idx], V_test[min_idx]

    return False, 0.0, 0.0

gamma_scan = np.linspace(0.1, 3.0, 100)
R_test_values = [0.0, 0.5, 1.0, 2.0, 5.0]

print(f"\nScanning γ from 0.1 to 3.0 for nontrivial minima...")
print(f"{'γ':>8} | " + " | ".join([f"R={R:.1f}" for R in R_test_values]))
print("-" * 70)

fig2, ax2 = plt.subplots(figsize=(10, 6))

for R_val in R_test_values:
    condensation_gamma = []
    for g in gamma_scan:
        has_min, M_min, V_min = has_nontrivial_minimum(g, R_val, Lambda_UV, N_c)
        if has_min:
            condensation_gamma.append(g)

    if condensation_gamma:
        gamma_crit = min(condensation_gamma)
        print(f"  R = {R_val:.1f}: condensation for γ > {gamma_crit:.3f}")
        ax2.axvline(x=gamma_crit, linestyle='--', alpha=0.5,
                    label=f'γ_crit(R={R_val:.1f}) = {gamma_crit:.2f}')
    else:
        print(f"  R = {R_val:.1f}: NO condensation in scanned range")

# Also plot G_SP(γ)
G_SP_scan = [(3 * kappa_sq / 16) * (g**2 - 1) / (g**2 + 1) for g in gamma_scan]
ax2.plot(gamma_scan, G_SP_scan, 'b-', linewidth=2, label='G_SP(γ)')
ax2.axhline(y=0, color='k', linewidth=1, linestyle='-')
ax2.axvline(x=1.0, color='r', linewidth=1, linestyle=':', label='γ=1 (sign change)')
ax2.axvline(x=0.274, color='green', linewidth=2, linestyle='--', label='γ=0.274 (LQG)')
ax2.set_xlabel('Barbero-Immirzi parameter γ')
ax2.set_ylabel('G_SP [M_Pl⁻²]')
ax2.set_title('Scalar/Pseudoscalar coupling vs γ')
ax2.legend()
ax2.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('/Users/houstongolden/Desktop/CODE_2026/bigbounce/research/paper2/ir_vacuum_program/figures/G_SP_vs_gamma.png', dpi=150)
print("\nFigure saved: figures/G_SP_vs_gamma.png")

# =============================================================================
# STEP 4: THE VECTOR/AXIAL CHANNEL — IS IT VIABLE?
# =============================================================================

print("\n" + "=" * 70)
print("STEP 4: VECTOR/AXIAL CHANNEL ANALYSIS")
print("=" * 70)
print()
print("From Computation 3, the VV and AA channels ARE attractive:")
print("  c_VV = -32 - 32/γ²  (always negative → always attractive)")
print("  c_AA = -32 - 32/γ²  (same)")
print()
print("A vector condensate ⟨ψ̄γ^μψ⟩ ≠ 0 would:")
print("  1. Break Lorentz invariance (picks a preferred direction)")
print("  2. NOT produce a simple cosmological constant")
print("  3. Generate anisotropic stress-energy")
print()
print("This is NOT what we want for dark energy (which requires isotropy).")
print()
print("HOWEVER: In a cosmological setting with an FRW background,")
print("the preferred direction is the cosmic time direction.")
print("A timelike vector condensate ⟨ψ̄γ⁰ψ⟩ = n (number density)")
print("is compatible with spatial isotropy.")
print()
print("But this is just the fermion number density, which is NOT")
print("a vacuum quantity — it's a matter density that dilutes as a⁻³.")
print()
print("So the vector channel does not help for late-time dark energy.")

# =============================================================================
# STEP 5: MULTI-FLAVOR ANALYSIS
# =============================================================================

print("\n" + "=" * 70)
print("STEP 5: MULTI-FLAVOR EFFECTS")
print("=" * 70)
print()
print("With N_f flavors, the four-fermion interaction from torsion is:")
print()
print("  L_4f = -G_eff × [Σ_i (ψ̄_i γ^μ γ⁵ ψ_i) + (1/γ)(ψ̄_i γ^μ ψ_i)]²")
print()
print("This is a SUM over flavors inside the square, so it generates")
print("INTER-FLAVOR interactions:")
print()
print("  (Σ_i J^μ_i)² = Σ_i (J^μ_i)² + Σ_{i≠j} (J^μ_i)(J_{μ,j})")
print()
print("For the intra-flavor terms (i=i): our single-flavor Fierz applies.")
print("  → S/P channels repulsive at γ = 0.274 (as computed)")
print()
print("For the inter-flavor terms (i≠j): the Fierz identity for DIFFERENT")
print("fermion species has NO anticommutation sign!")
print("  (ψ̄_i M ψ_i)(ψ̄_j N ψ_j) does NOT get a Fierz minus sign")
print("  because ψ_i and ψ_j are different fields.")
print()
print("The inter-flavor VA cross-term:")
print("  (ψ̄_i γ^μ ψ_i)(ψ̄_j γ_μ γ⁵ ψ_j)")
print("does NOT vanish for i ≠ j.")
print()
print("However, in the S/P Fierz decomposition of the INTER-FLAVOR terms,")
print("the signs change. Let me compute this.")
print()

# For inter-flavor: (ψ̄_i M ψ_i)(ψ̄_j N ψ_j) — NO Fierz rearrangement needed
# This is already in the desired form (products of single-flavor bilinears).
# We just need to identify which composites couple to which.
#
# The inter-flavor four-fermion interaction:
# (ψ̄_i γ^μ γ⁵ ψ_i)(ψ̄_j γ_μ γ⁵ ψ_j) — this is a product of two axial currents
#
# In the HS decomposition, we introduce FLAVOR-SINGLET auxiliary fields:
#   σ ~ Σ_i ψ̄_i ψ_i (flavor-singlet scalar)
#   π ~ Σ_i ψ̄_i iγ⁵ ψ_i (flavor-singlet pseudoscalar)
#
# The coupling is then:
#   N_f × (single-flavor coupling) for the diagonal terms
# + (N_f² - N_f) × (inter-flavor coupling) for the off-diagonal terms
#
# The total effective coupling in the flavor-singlet S/P channel is:
#   G_SP^eff = N_f × G_SP^(intra) + ...
#
# BUT: the intra-flavor Fierz rearrangement gives G_SP^(intra) < 0.
# The inter-flavor terms don't need Fierz rearrangement — they directly
# contribute to the flavor-singlet channels.
#
# For the inter-flavor AA term:
#   (ψ̄_i γ^μ γ⁵ ψ_i)(ψ̄_j γ_μ γ⁵ ψ_j)
#   This already couples flavor-singlet axial currents.
#   It does NOT need Fierz rearrangement to contribute to the gap equation.
#
# The gap equation for the flavor-singlet condensate σ = Σ_i ⟨ψ̄_i ψ_i⟩/N_f:
#
# In the mean-field approximation:
#   σ = 2 G_eff^total × N_f × ⟨ψ̄ψ⟩_per_flavor
#
# where G_eff^total includes both intra- and inter-flavor contributions.
#
# The key question: does the total effective S/P coupling (intra + inter)
# become attractive for large enough N_f?

# For the flavor-singlet S/P channel:
# The total four-fermion coupling in the S/P channel after Fierz is:
#
# Intra-flavor: N_f × G_SP^(single-flavor Fierz)
#             = N_f × G_eff × (1 - 1/γ²)
#
# Inter-flavor: For i ≠ j, (ψ̄_i Γ ψ_i)(ψ̄_j Γ ψ_j) does not need Fierz.
# The coupling of the flavor-singlet scalar σ = Σ_i σ_i to each flavor
# comes from the ORIGINAL current-current interaction, not the Fierz-rearranged one.
#
# Actually wait — I need to think about this more carefully.
# The HS transformation is applied BEFORE Fierz rearrangement.
# The HS transformation can be applied directly to the current-current form:
#
# L = -G_eff × (J_total^μ)(J_total,μ)
# where J_total^μ = Σ_i (ψ̄_i γ^μ γ⁵ ψ_i + (1/γ) ψ̄_i γ^μ ψ_i)
#
# This is a SINGLE squared current. The HS transformation introduces a
# VECTOR auxiliary field:
#
# V^μ ~ J_total^μ
#
# NOT scalar/pseudoscalar auxiliary fields.
#
# To get scalar/pseudoscalar auxiliary fields, we FIRST Fierz-rearrange
# from current-current to scalar channels, THEN do HS.
#
# For multi-flavor, the Fierz rearrangement of (J_total)² gives:
#
# (Σ_i J^μ_i)² = Σ_i (J^μ_i)² + 2 Σ_{i<j} J^μ_i J_{μ,j}
#
# The intra-flavor (J_i)² Fierz-rearranges with the MINUS sign (identical fermions).
# The inter-flavor J_i · J_j Fierz-rearranges WITHOUT the minus sign.
#
# So the S/P Fierz coefficient for inter-flavor is the OPPOSITE sign
# of the intra-flavor result!

# Inter-flavor Fierz: (ψ̄_i M ψ_i)(ψ̄_j N ψ_j) (i ≠ j)
# = (1/16) Σ_AB tr(M Γ_A) tr(N Γ_B) (ψ̄_i Γ_A ψ_i)(ψ̄_j Γ_B ψ_j)
#
# Note: NO MINUS SIGN (no anticommutation needed for different species)
# and the trace FACTORIZES (no exchange).
#
# For the S channel: tr(M × 1) × tr(N × 1) / 16
# For M = γ^μ γ⁵, N = γ_μ γ⁵:
#   tr(γ^μ γ⁵) = 0 for each μ
# So: inter-flavor AA → S = 0
#
# For M = γ^μ, N = γ_μ:
#   tr(γ^μ) = 0 for each μ (traceless)
# So: inter-flavor VV → S = 0
#
# Hmm, ALL inter-flavor Fierz coefficients into scalar/pseudoscalar
# channels vanish because tr(γ^μ) = 0 and tr(γ^μ γ⁵) = 0!

print("Inter-flavor Fierz into S/P channels:")
print("  tr(γ^μ) = 0 for all μ")
print("  tr(γ^μ γ⁵) = 0 for all μ")
print("  → All inter-flavor contributions to S/P channels VANISH")
print("     (traces factorize and each trace is zero)")
print()
print("This means: multi-flavor does NOT help the S/P channel.")
print("The inter-flavor four-fermion terms contribute only to")
print("vector/axial channels (where traces don't factorize in the")
print("same way due to Lorentz structure).")
print()
print("★★★ MULTI-FLAVOR RESCUE ROUTE IS CLOSED FOR S/P CHANNELS ★★★")

# =============================================================================
# STEP 6: ASSESSMENT
# =============================================================================

print("\n" + "=" * 70)
print("ASSESSMENT: STATUS OF GATE 1")
print("=" * 70)
print()
print("FINDINGS:")
print()
print("1. The S/P channel coupling is REPULSIVE at γ = 0.274 (tree level)")
print("   G_SP = (3κ²/16)(γ²-1)/(γ²+1) < 0 for γ < 1")
print()
print("2. Gravitational catalysis CANNOT flip a repulsive channel to attractive.")
print("   It only lowers the threshold for already-attractive channels.")
print()
print("3. Multi-flavor effects do NOT help the S/P channel.")
print("   Inter-flavor traces vanish for current-current interactions.")
print()
print("4. The vector/axial channels ARE attractive but produce")
print("   Lorentz-breaking condensates, not vacuum energy.")
print()
print("5. The critical γ for S/P condensation is γ = 1.")
print("   The LQG value γ = 0.274 is well below this.")
print()
print("CONCLUSION FOR GATE 1:")
print()
print("  At the current level of analysis (single-flavor or multi-flavor,")
print("  with or without curvature, in the S/P channel), the pseudoscalar")
print("  condensate Φ = ⟨ψ̄iγ⁵ψ⟩ DOES NOT FORM at γ = 0.274.")
print()
print("  Gate 1 is FAILED for the pseudoscalar order parameter as defined")
print("  in the canonical problem statement.")
print()
print("REMAINING POSSIBILITIES:")
print()
print("  (a) The overall prefactor (3/16 vs 3/32) matters. If the correct")
print("      prefactor changes the γ-dependence qualitatively, the result")
print("      could change. [UNLIKELY — the γ² vs 1/γ² structure is robust]")
print()
print("  (b) Higher-order corrections (two-loop, non-perturbative) could")
print("      change the channel structure. [SPECULATIVE]")
print()
print("  (c) The order parameter is WRONG. The correct condensate may be")
print("      something other than ψ̄iγ⁵ψ. For example:")
print("      - A composite involving the curvature (e.g., R × ψ̄ψ)")
print("      - A topological condensate (related to the Nieh-Yan term)")
print("      - A non-local condensate")
print()
print("  (d) The mechanism is fundamentally different from NJL-type")
print("      condensation. The vacuum energy may arise from a different")
print("      sector entirely (e.g., the gravitational effective action")
print("      itself, not from fermion condensation).")
print()
print("  (e) γ is not 0.274. If γ > 1 (which some approaches to black")
print("      hole entropy allow), the S/P channel becomes attractive")
print("      and the standard NJL route works.")
print()
print("PER THE CANONICAL PROBLEM STATEMENT (06a_frozen_assumptions):")
print("  This result may warrant a versioned update to the problem statement,")
print("  not casual editing. The order parameter choice needs revision.")
