"""
Numerical computation of ALP field evolution in ΛCDM and resulting birefringence angle.

This solves the exact ALP equation of motion:
    φ'' + 3H(a) φ' + m² sin(φ/f_a) f_a = 0

in an expanding ΛCDM background with H(a) from Planck 2018 best-fit parameters.

The birefringence angle is:
    β = (g_aγ / 2) × Δφ = (C₀ / (2 f_a)) × Δφ

where Δφ = φ(a=1) - φ(a_rec) is the field displacement from recombination to today.
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d

# =============================================================
# Cosmological parameters (Planck 2018 best-fit)
# =============================================================
H0_km = 67.36  # km/s/Mpc
H0 = H0_km * 1e3 / 3.0857e22  # Convert to 1/s
Omega_m = 0.3153
Omega_r = 9.14e-5  # radiation (photons + neutrinos)
Omega_Lambda = 1 - Omega_m - Omega_r

# Planck mass
M_Pl = 2.435e18  # GeV (reduced Planck mass)
hbar = 6.582e-25  # GeV·s
H0_GeV = H0 * hbar  # H0 in GeV

print(f"H0 = {H0_km} km/s/Mpc = {H0_GeV:.4e} GeV")
print(f"Omega_m = {Omega_m}, Omega_Lambda = {Omega_Lambda}")

# =============================================================
# ALP parameters
# =============================================================
f_a = M_Pl  # Planck-scale decay constant
theta_i_values = [0.5, 1.0, 1.5, 2.0]  # Initial misalignment angles

# Mass range: m/H0 from 0.1 to 10
m_over_H0_values = [0.3, 0.5, 1.0, 2.0, 3.0, 5.0]

# Coupling: C_0 is the anomaly coefficient
# In standard axion conventions: g_aγ = (α_EM / (2π f_a)) × C_aγ
# where C_aγ is a model-dependent integer
# For a KSVZ-like ALP: C_aγ ~ 1-8
# The "C_0" in our paper absorbs α_EM/(2π), so C_0 ~ α_EM/(2π) × C_aγ
alpha_EM = 1/137.036
C_aγ_values = [1, 2, 4, 8]  # Anomaly coefficient

# =============================================================
# Hubble rate in ΛCDM
# =============================================================
def H_LCDM(a):
    """Hubble rate H(a) in units of H0."""
    return np.sqrt(Omega_r / a**4 + Omega_m / a**3 + Omega_Lambda)

# =============================================================
# ALP equation of motion
# =============================================================
# We use conformal time derivative notation but solve in terms of ln(a).
# Let x = ln(a), so da/dt = a H, and d/dt = aH d/dx
#
# The EOM is: d²φ/dt² + 3H dφ/dt + m² f_a sin(φ/f_a) = 0
#
# In terms of x = ln(a):
#   dφ/dx = (1/(aH)) dφ/dt  →  dφ/dt = aH dφ/dx
#   d²φ/dt² = (aH)² d²φ/dx² + (aH)(a dH/da H + aH²) dφ/dx
#            = (aH)² [d²φ/dx² + (1 + H'/H) dφ/dx]
#   where H' = dH/dx = (d ln H/d ln a) H
#
# Actually, it's simpler to use the variable θ = φ/f_a:
#   θ'' + (3 + H'/H) θ' + (m/H)² / a² × sin(θ) × (1/a²) ...
#
# Let me use the standard approach: solve in terms of N = ln(a).
#
# θ = φ/f_a
# dθ/dN = (1/(aH)) dφ/dt / f_a = (dφ/dt) / (aH f_a)
# Let ω = dθ/dN
# Then: dω/dN + (3 + d ln H / dN) ω + (m/(aH))² sin(θ) = 0
#
# d ln H / dN = (1/(2H²)) × (-4 Ω_r/a⁴ - 3 Ω_m/a³)  [using H² = ...]
#            = (-4 Ω_r/a⁴ - 3 Ω_m/a³) / (2(Ω_r/a⁴ + Ω_m/a³ + Ω_Λ))

def dlnH_dN(a):
    """d ln H / d ln a"""
    num = -4 * Omega_r / a**4 - 3 * Omega_m / a**3
    den = 2 * (Omega_r / a**4 + Omega_m / a**3 + Omega_Lambda)
    return num / den

def alp_eom(N, y, m_over_H0):
    """
    ALP equation of motion in terms of N = ln(a).
    y = [θ, ω] where θ = φ/f_a and ω = dθ/dN.
    """
    theta, omega = y
    a = np.exp(N)
    H_ratio = H_LCDM(a)  # H/H0

    # Effective mass squared over (aH)²
    mass_term = (m_over_H0 / (a * H_ratio))**2

    # Friction term
    friction = 3 + dlnH_dN(a)

    dtheta_dN = omega
    domega_dN = -friction * omega - mass_term * np.sin(theta)

    return [dtheta_dN, domega_dN]

# =============================================================
# Solve and compute birefringence
# =============================================================
a_rec = 1 / 1101.0  # Recombination: z ≈ 1100
N_rec = np.log(a_rec)
N_today = 0.0  # a = 1

print("\n" + "="*80)
print("ALP FIELD EVOLUTION IN ΛCDM: NUMERICAL RESULTS")
print("="*80)

print(f"\nRecombination: a_rec = {a_rec:.6e}, N_rec = {N_rec:.2f}")
print(f"Integration: N = [{N_rec:.2f}, {N_today}]")

# Results storage
results = []

for m_over_H0 in m_over_H0_values:
    for theta_i in theta_i_values:
        # Initial conditions: field frozen at recombination (ω ≈ 0)
        y0 = [theta_i, 0.0]

        # Solve
        sol = solve_ivp(
            alp_eom, [N_rec, N_today], y0,
            args=(m_over_H0,),
            method='RK45',
            max_step=0.01,
            rtol=1e-10, atol=1e-12
        )

        if not sol.success:
            print(f"  FAILED: m/H0={m_over_H0}, θ_i={theta_i}")
            continue

        theta_final = sol.y[0, -1]
        delta_theta = theta_i - theta_final  # Field displacement in units of f_a

        # Store result
        results.append({
            'm_over_H0': m_over_H0,
            'theta_i': theta_i,
            'delta_theta': delta_theta,
            'delta_phi_over_fa': delta_theta,
            'theta_final': theta_final,
        })

# =============================================================
# Print results table
# =============================================================
print(f"\n{'m/H0':>6} {'θ_i':>6} {'Δθ=Δφ/f_a':>12} {'β (C₀=1)':>12} {'β (C_aγ=8)':>12}")
print("-" * 60)

for r in results:
    # β = (C₀ / 2) × Δφ/f_a  where C₀ = α_EM/(2π) × C_aγ for standard coupling
    # But in our paper's convention, C₀ is the full effective coupling
    # For C₀ = 1 (paper convention): β = Δφ/(2f_a) radians
    beta_C0_1 = r['delta_theta'] / 2  # radians, if C_0 = 1
    beta_C0_1_deg = np.degrees(beta_C0_1)

    # For standard axion: g_aγ = α/(2π f_a) × C_aγ
    # β = g_aγ/2 × Δφ = α/(4π) × C_aγ × Δφ/f_a
    beta_standard_8 = (alpha_EM / (4 * np.pi)) * 8 * r['delta_theta']  # radians
    beta_standard_8_deg = np.degrees(beta_standard_8)

    if r['theta_i'] == 1.0:  # Print key cases
        print(f"{r['m_over_H0']:>6.1f} {r['theta_i']:>6.1f} {r['delta_theta']:>12.6f} "
              f"{beta_C0_1_deg:>12.6f}° {beta_standard_8_deg:>12.6f}°")

# =============================================================
# The key question: what value of C₀ gives β = 0.27°?
# =============================================================
print("\n" + "="*80)
print("KEY QUESTION: What coupling gives β = 0.27°?")
print("="*80)

target_beta_deg = 0.27
target_beta_rad = np.radians(target_beta_deg)

print(f"\nFor m/H0 = 1.0, θ_i = 1.0:")
for r in results:
    if r['m_over_H0'] == 1.0 and r['theta_i'] == 1.0:
        delta_theta = r['delta_theta']
        print(f"  Δφ/f_a = {delta_theta:.6f}")

        # Paper convention: β = C₀ × Δφ/(2f_a)
        # → C₀ = 2 × β / (Δφ/f_a)
        C0_needed = 2 * target_beta_rad / delta_theta
        print(f"  To get β = {target_beta_deg}°:")
        print(f"    Paper C₀ needed = {C0_needed:.4f}")

        # Standard convention: β = (α/(4π)) × C_aγ × Δφ/f_a
        # → C_aγ = 4π × β / (α × Δφ/f_a)
        C_agamma_needed = 4 * np.pi * target_beta_rad / (alpha_EM * delta_theta)
        print(f"    Standard C_aγ needed = {C_agamma_needed:.2f}")

        print(f"\n  Interpretation:")
        print(f"    If C₀ absorbs α/(2π): C₀ = α/(2π) × C_aγ = {alpha_EM/(2*np.pi) * C_agamma_needed:.6f}")
        print(f"    This means C_aγ ~ {C_agamma_needed:.0f}, which is {'natural (O(1)-O(10))' if C_agamma_needed < 20 else 'fine-tuned'}")

# =============================================================
# Comprehensive scan: β(m/H0, θ_i) with C_aγ = 8
# =============================================================
print("\n" + "="*80)
print("COMPREHENSIVE: β in degrees for C_aγ = 8 (standard coupling)")
print("="*80)
print(f"\n{'':>8}", end="")
for theta_i in theta_i_values:
    print(f"{'θ_i='+str(theta_i):>10}", end="")
print()
print("-" * 50)

for m_over_H0 in m_over_H0_values:
    print(f"m/H0={m_over_H0:>3.1f}", end="")
    for theta_i in theta_i_values:
        for r in results:
            if r['m_over_H0'] == m_over_H0 and r['theta_i'] == theta_i:
                beta = (alpha_EM / (4 * np.pi)) * 8 * r['delta_theta']
                beta_deg = np.degrees(beta)
                print(f"{beta_deg:>10.4f}", end="")
                break
    print()

# =============================================================
# The actual Δφ/f_a value our paper uses
# =============================================================
print("\n" + "="*80)
print("PAPER VALIDATION")
print("="*80)

for r in results:
    if r['m_over_H0'] == 1.0 and r['theta_i'] == 1.0:
        delta = r['delta_theta']
        print(f"\nFor m = H0, θ_i = 1:")
        print(f"  Δφ/f_a = {delta:.6f}")
        print(f"  Paper claimed 'Δφ/f_a ~ 10⁻²': {'CONFIRMED' if 0.001 < abs(delta) < 0.1 else 'WRONG'}")
        print(f"  J₀(1) = {float(np.cos(1)*0 + 0.7651976865579666):.6f}")  # J0(1) ≈ 0.7652
        print(f"  1 - J₀(1) = {1 - 0.7651976865579666:.6f}")
        print(f"  Bessel approx Δφ/f_a ≈ θ_i × (1-J₀(m/H₀)) = {1.0 * (1 - 0.7651976865579666):.6f}")
        print(f"  Numerical Δφ/f_a = {delta:.6f}")
        print(f"  Ratio (numerical/Bessel) = {delta / (1.0 * (1 - 0.7651976865579666)):.4f}")

print("\n" + "="*80)
print("DONE — All computations complete")
print("="*80)
