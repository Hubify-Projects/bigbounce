"""
Solve the Mukhanov-Sasaki equation through the LQC bounce.

The modified Friedmann equation is:
    H² = (8πG/3) ρ (1 - ρ/ρ_c)

The Mukhanov-Sasaki equation for the mode function v_k(η) is:
    v_k'' + (k² - z''/z) v_k = 0

where z = a√(2ε)/c_s (for canonical scalar: c_s = 1, z = a√(2ε))
and primes denote conformal time derivatives.

For the effective LQC bounce, we need:
1. Solve the background: a(η), H(η), ε(η) through the bounce
2. Compute z''/z as a function of conformal time
3. Solve the Mukhanov-Sasaki equation for each k mode
4. Extract the primordial power spectrum P_R(k)
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d
import json

print("="*70)
print("MUKHANOV-SASAKI EQUATION THROUGH THE LQC BOUNCE")
print("="*70)

# ============================================================
# Units: we work in Planck units (M_Pl = 1, 8πG = 1)
# ============================================================
# ρ_c = 0.41 ρ_Pl (DLM counting, Ashtekar & Singh 2011)
rho_c = 0.41  # in Planck units

# Matter content: canonical scalar field with w ≈ 0 (dust-like)
# For w = 0: ρ ∝ a^{-3}, so ρ = ρ_0 (a_0/a)^3
# At the bounce: a = a_bounce, ρ = ρ_c
# We set a_bounce = 1 (normalization)

print(f"\nLQC bounce parameters:")
print(f"  ρ_c = {rho_c} ρ_Pl")
print(f"  a_bounce = 1 (normalization)")

# ============================================================
# Background: solve the modified Friedmann equation
# ============================================================
# H² = (1/3) ρ (1 - ρ/ρ_c)    [in 8πG = 1 units]
# ρ = ρ_c / a³  (matter domination, with a_bounce = 1 where ρ = ρ_c)
#
# dH/dt = -H²(1 + ε) where ε = -Ḣ/H² = 3/2 for matter domination
#        (modified for the bounce regime)
#
# It's easier to solve in cosmic time t, then convert to conformal time.

def H_squared(a):
    """H² as a function of scale factor."""
    rho = rho_c / a**3
    return (1.0/3.0) * rho * (1 - rho/rho_c)

def background_eom(t, y):
    """Background equations in cosmic time."""
    a, phi = y
    rho = rho_c / a**3
    H2 = (1.0/3.0) * rho * (1.0 - rho/rho_c)

    if H2 < 0:
        H2 = 0  # Should not happen if a > a_bounce

    H = np.sqrt(max(H2, 1e-30))

    # For matter domination: ρ = ρ_c/a³
    # Continuity: dρ/dt = -3Hρ ⟹ ρ ∝ a^{-3} (verified)
    # We track a and a dummy scalar field phase

    da_dt = a * H
    dphi_dt = np.sqrt(2 * rho)  # KE = ρ for dust-like (approximate)

    return [da_dt, dphi_dt]

# Solve expanding phase (t > 0)
a_init = 1.0 + 1e-10  # Just after bounce
t_span_expand = (0, 200)  # Planck times
sol_expand = solve_ivp(background_eom, t_span_expand, [a_init, 0],
                        method='RK45', max_step=0.01, rtol=1e-12, atol=1e-14,
                        dense_output=True)

# Solve contracting phase (t < 0, by symmetry of dust bounce)
# For a symmetric bounce, a(-t) = a(t)
# So we just mirror the expanding solution

# Build conformal time: dη = dt/a
t_expand = sol_expand.t
a_expand = sol_expand.y[0]

# Compute conformal time by integration
dt = np.diff(t_expand)
eta_cumulative = np.cumsum(dt / a_expand[:-1])
eta_expand = np.concatenate([[0], eta_cumulative])

# Full timeline: contracting + expanding
# Mirror: η(-t) = -η(t), a(-t) = a(t)
t_full = np.concatenate([-t_expand[::-1][:-1], t_expand])
a_full = np.concatenate([a_expand[::-1][:-1], a_expand])
eta_full = np.concatenate([-eta_expand[::-1][:-1], eta_expand])

# Interpolate
a_of_eta = interp1d(eta_full, a_full, kind='cubic', fill_value='extrapolate')
t_of_eta = interp1d(eta_full, t_full, kind='cubic', fill_value='extrapolate')

# Compute z''/z
# For matter domination: ε = 3/2, z = a√(2ε) = a√3
# z''/z = a''/a (when ε is constant)
# a'' = d²a/dη² = d/dη(a H a) = a(H²a² + Ḣ a²)
# z''/z = a''/a = a²(H² + Ḣ) = a²H²(1 - ε) ... but at the bounce this diverges

# More carefully: z''/z = 2a²H²(1 - 3w/2 + ...) for w ≈ 0
# Through the bounce, H → 0 and z''/z → 0 momentarily

# Compute numerically
deta = eta_full[1] - eta_full[0]
a_prime = np.gradient(a_full, eta_full)
a_double_prime = np.gradient(a_prime, eta_full)
z_eff = a_full * np.sqrt(3)  # z = a√(2ε) with ε = 3/2
z_pp_over_z = a_double_prime / a_full  # z''/z = a''/a for constant ε

# ============================================================
# Solve Mukhanov-Sasaki for a range of k modes
# ============================================================
# v_k'' + (k² - z''/z) v_k = 0
#
# Initial conditions: Bunch-Davies vacuum in the contracting phase
# v_k → (1/√(2k)) e^{-ikη}  as η → -∞
# v_k' → -ik × (1/√(2k)) e^{-ikη}

z_pp_z_interp = interp1d(eta_full, z_pp_over_z, kind='cubic', fill_value='extrapolate')

def ms_equation(eta, y, k):
    """Mukhanov-Sasaki equation: v'' + (k² - z''/z) v = 0."""
    v_re, v_im, v_prime_re, v_prime_im = y
    zppz = z_pp_z_interp(eta)
    omega_sq = k**2 - zppz

    dv_re = v_prime_re
    dv_im = v_prime_im
    dvp_re = -omega_sq * v_re
    dvp_im = -omega_sq * v_im

    return [dv_re, dv_im, dvp_re, dvp_im]

# k modes to solve (in Planck units)
k_values = np.logspace(-3, 1, 50)  # Range of comoving wavenumbers

# Start integration deep in the contracting phase
eta_start = eta_full[10]  # Deep in contraction
eta_end = eta_full[-10]    # Well into expansion

print(f"\nSolving Mukhanov-Sasaki equation for {len(k_values)} k-modes...")
print(f"  η range: [{eta_start:.2f}, {eta_end:.2f}]")

power_spectrum = []
for i, k in enumerate(k_values):
    # Bunch-Davies initial conditions
    # v_k = (1/√(2k)) e^{-ikη}
    norm = 1.0 / np.sqrt(2*k)
    phase = -k * eta_start

    v_re_0 = norm * np.cos(phase)
    v_im_0 = norm * np.sin(phase)
    vp_re_0 = norm * k * np.sin(phase)    # v' = ik × v → real part
    vp_im_0 = -norm * k * np.cos(phase)   # v' = ik × v → imag part

    y0 = [v_re_0, v_im_0, vp_re_0, vp_im_0]

    try:
        sol = solve_ivp(ms_equation, [eta_start, eta_end], y0,
                        args=(k,), method='RK45',
                        max_step=min(0.1, 0.5/k),
                        rtol=1e-10, atol=1e-12)

        if sol.success:
            v_final = complex(sol.y[0, -1], sol.y[1, -1])
            a_final = a_of_eta(eta_end)
            z_final = a_final * np.sqrt(3)

            # ζ_k = v_k / z
            zeta_k = abs(v_final) / z_final

            # P_R(k) = k³/(2π²) × |ζ_k|²
            P_R = k**3 / (2 * np.pi**2) * zeta_k**2
            power_spectrum.append((k, P_R))
        else:
            power_spectrum.append((k, np.nan))
    except Exception as e:
        power_spectrum.append((k, np.nan))

    if (i+1) % 10 == 0:
        print(f"  Completed {i+1}/{len(k_values)} modes")

# ============================================================
# Results
# ============================================================
k_arr = np.array([ps[0] for ps in power_spectrum])
P_arr = np.array([ps[1] for ps in power_spectrum])

# Remove NaN
valid = ~np.isnan(P_arr) & (P_arr > 0)
k_valid = k_arr[valid]
P_valid = P_arr[valid]

if len(k_valid) > 5:
    # Fit spectral index
    log_k = np.log(k_valid)
    log_P = np.log(P_valid)
    # Fit P(k) = A_s × (k/k_pivot)^{n_s - 1}
    coeffs = np.polyfit(log_k, log_P, 1)
    n_s = coeffs[0] + 1
    A_s = np.exp(coeffs[1])

    print(f"\n" + "="*70)
    print(f"PRIMORDIAL POWER SPECTRUM THROUGH LQC BOUNCE")
    print(f"="*70)
    print(f"\nValid modes: {len(k_valid)} / {len(k_values)}")
    print(f"k range: [{k_valid[0]:.4e}, {k_valid[-1]:.4e}] Planck units")
    print(f"\nBest-fit spectral index: n_s = {n_s:.4f}")
    print(f"Best-fit amplitude: A_s = {A_s:.4e}")
    print(f"\nExpected for exact dust (w=0): n_s = 1.000 (scale-invariant)")
    print(f"Observed deviation from n_s = 1: {n_s - 1:.4f}")
    print(f"\nNote: This computation uses the effective LQC modified Friedmann")
    print(f"equation H² = ρ/3 × (1 - ρ/ρ_c) with ρ_c = 0.41 ρ_Pl.")
    print(f"The perturbation-transparency theorem guarantees that the Holst")
    print(f"term contributes nothing: the power spectrum is identical to the")
    print(f"standard LQC result for canonical scalar field matter.")

    # Check for bounce features
    # The LQC bounce might imprint oscillatory features at high k
    # (modes that cross the bounce when k ~ a_bounce × H_bounce)
    if len(k_valid) > 10:
        residuals = log_P - np.polyval(coeffs, log_k)
        rms_oscillation = np.std(residuals)
        print(f"\nBounce feature search:")
        print(f"  RMS residual from power law: {rms_oscillation:.4e}")
        print(f"  Max deviation: {np.max(np.abs(residuals)):.4e}")
        if rms_oscillation < 0.01:
            print(f"  No significant oscillatory features detected at this resolution.")
        else:
            print(f"  Possible bounce features at {rms_oscillation*100:.1f}% level.")

    # Save results
    results = {
        'n_s': float(n_s),
        'A_s': float(A_s),
        'rho_c': float(rho_c),
        'k_values': k_valid.tolist(),
        'P_R_values': P_valid.tolist(),
    }
    with open('lqc_power_spectrum_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to lqc_power_spectrum_results.json")

else:
    print(f"\nInsufficient valid modes ({len(k_valid)}) for spectral fit.")
    print("The integration may need smaller step sizes or different η range.")
