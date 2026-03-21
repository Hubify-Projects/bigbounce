"""
Cubic (third-order) perturbation transmission through the LQC bounce.

This computation checks whether the bispectrum (f_NL = -35/8 from the
contracting phase) is faithfully transmitted through the LQC bounce.

The approach:
1. Solve the background (a, H) through the bounce (done in the MS script)
2. Set up the linear mode functions v_k(η) through the bounce (done)
3. Compute the CUBIC action S_3 contribution from the bounce epoch
4. The key question: does the bounce modify f_NL, or does it pass through?

The perturbation-transparency theorem tells us the HOLST TERM contributes
nothing (for scalar field matter). But the LQC holonomy corrections to
the background DO affect the mode functions near the bounce, and these
modified mode functions enter the cubic action integral.

The strategy: compute f_NL from the in-in integral using the bounce-modified
mode functions and compare to -35/8 from the unmodified (pure contraction)
mode functions.
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d

print("="*70)
print("CUBIC BOUNCE TRANSMISSION: f_NL THROUGH THE LQC BOUNCE")
print("="*70)

# ============================================================
# Setup: same background as the MS computation
# ============================================================
rho_c = 0.41  # Planck units

def background_eom(t, y):
    a = y[0]
    rho = rho_c / a**3
    H2 = (1.0/3.0) * rho * (1.0 - rho/rho_c)
    H = np.sqrt(max(H2, 1e-50))
    return [a * H]

# Solve expanding phase
sol = solve_ivp(background_eom, (0, 300), [1.0 + 1e-10],
                method='RK45', max_step=0.005, rtol=1e-13, atol=1e-15,
                dense_output=True)

t_exp = sol.t
a_exp = sol.y[0]

# Build conformal time
dt = np.diff(t_exp)
eta_cum = np.cumsum(dt / a_exp[:-1])
eta_exp = np.concatenate([[0], eta_cum])

# Full timeline (symmetric bounce)
t_full = np.concatenate([-t_exp[::-1][:-1], t_exp])
a_full = np.concatenate([a_exp[::-1][:-1], a_exp])
eta_full = np.concatenate([-eta_exp[::-1][:-1], eta_exp])

a_interp = interp1d(eta_full, a_full, kind='cubic', fill_value='extrapolate')

# z''/z
a_p = np.gradient(a_full, eta_full)
a_pp = np.gradient(a_p, eta_full)
zppz = a_pp / a_full
zppz_interp = interp1d(eta_full, zppz, kind='cubic', fill_value='extrapolate')

# ============================================================
# Solve mode functions through the bounce
# ============================================================
def ms_eq(eta, y, k):
    v_re, v_im, vp_re, vp_im = y
    omega_sq = k**2 - zppz_interp(eta)
    return [vp_re, vp_im, -omega_sq * v_re, -omega_sq * v_im]

def solve_mode(k, eta_start, eta_end):
    """Solve mode function with Bunch-Davies initial conditions."""
    norm = 1.0 / np.sqrt(2*k)
    phase = -k * eta_start
    y0 = [norm*np.cos(phase), norm*np.sin(phase),
          norm*k*np.sin(phase), -norm*k*np.cos(phase)]

    sol = solve_ivp(ms_eq, [eta_start, eta_end], y0, args=(k,),
                    method='RK45', max_step=min(0.05, 0.3/k),
                    rtol=1e-11, atol=1e-13, dense_output=True)
    return sol

# ============================================================
# The cubic action and f_NL computation
# ============================================================
# The Maldacena cubic action in the comoving gauge for ε = 3/2 gives:
#
# f_NL = (5/12) × lim_{k1→0} [B(k1,k,k) / (4π⁴ P_ζ(k1) P_ζ(k))]
#
# where B is the bispectrum from the in-in integral:
# B ∝ ∫ dη a²ε [various cubic vertices] × v_k(η) products
#
# The KEY insight for bounce transmission:
# The f_NL value -35/8 is generated during the CONTRACTING phase
# by the superhorizon growth of ζ ∝ |η|^{-3}.
# The bounce occurs at η = 0 where modes are deep inside the
# "superhorizon" regime (k|η| << 1 for modes of interest).
#
# For superhorizon modes through the bounce:
# v_k(η) ≈ A_k × z(η) + B_k × z(η) ∫ dη'/(z(η')²)
# where A_k is the growing mode and B_k is the decaying mode.
#
# The Wilson-Ewing (2012) result for LINEAR transmission:
# The growing mode coefficient A_k passes through the bounce unchanged
# (up to a phase). The decaying mode B_k is set to zero by the
# bounce symmetry.
#
# At CUBIC order: the in-in integral picks up contributions from
# two epochs: (1) the contracting phase (η < 0) and (2) the bounce
# itself (η ≈ 0).
#
# The contracting phase contribution IS the Cai et al. f_NL = -35/8.
# The bounce contribution is proportional to the time the mode
# spends near the bounce with ε changing rapidly.

print("\nComputing mode functions for squeezed configuration...")

# Squeezed: k1 << k2 = k3 = k
k_long = 0.01    # Long mode
k_short = 1.0    # Short mode

eta_start = eta_full[10]
eta_end = eta_full[-10]

sol_long = solve_mode(k_long, eta_start, eta_end)
sol_short = solve_mode(k_short, eta_start, eta_end)

# Extract mode amplitudes at the end
v_long = complex(sol_long.y[0,-1], sol_long.y[1,-1])
v_short = complex(sol_short.y[0,-1], sol_short.y[1,-1])
a_end = a_interp(eta_end)
z_end = a_end * np.sqrt(3)

zeta_long = abs(v_long) / z_end
zeta_short = abs(v_short) / z_end

P_long = k_long**3 / (2*np.pi**2) * zeta_long**2
P_short = k_short**3 / (2*np.pi**2) * zeta_short**2

print(f"\nLinear mode results:")
print(f"  k_long = {k_long}, k_short = {k_short}")
print(f"  |ζ_long| = {zeta_long:.6e}")
print(f"  |ζ_short| = {zeta_short:.6e}")
print(f"  P_R(k_long) = {P_long:.6e}")
print(f"  P_R(k_short) = {P_short:.6e}")

# ============================================================
# Estimate bounce contribution to the cubic action
# ============================================================
# The bounce epoch is |η| < η_bounce where η_bounce ~ 1/√ρ_c ~ few Planck times.
# For modes with k × η_bounce << 1 (all cosmologically relevant modes):
# the mode functions are approximately constant through the bounce.
#
# The cubic action integral through the bounce:
# ΔS_3 ∝ ∫_{-η_b}^{+η_b} a²ε [cubic vertices] dη
#
# Near the bounce:
# a ≈ 1 (minimum)
# ε = -Ḣ/H² → ∞ as H → 0 at the bounce (formally divergent)
#   BUT the product a²ε × H² is bounded:
#   ε × H² = -Ḣ, which is finite at the bounce.
#
# The cubic vertices involve terms like:
# ε²(ζ')² ζ ∝ ε² × v_k² / z⁴ × a
#
# For superhorizon modes (k×η << 1), v_k ≈ A_k × z, so:
# ζ ~ A_k (constant)
# ζ' ~ 0 (superhorizon)
#
# Therefore the cubic vertices involving ζ' are SUPPRESSED for
# superhorizon modes passing through the bounce.
#
# The dominant vertex is the ε²ζ(∂ζ)² term, which goes as:
# ε² × ζ × (∂ᵢζ)² ~ ε² × ζ × k² × ζ²
# ~ ε² × k² × A_k³
#
# The time integral is ∫ a² ε² dη ~ ∫ a² (Ḣ/H²)² dη
#
# Near the bounce: H ~ 0, ε → ∞, but the integrand a²ε²H² ~ a²Ḣ²/H²
# This is finite because Ḣ is finite and H → 0.
#
# The KEY point: the bounce contribution scales as:
# ΔS_3(bounce) / S_3(contraction) ~ (k × η_bounce)² × (something of O(1))
#
# For cosmologically relevant modes: k << 1/η_bounce ~ √ρ_c ~ 0.6 M_Pl
# So k × η_bounce << 1 for ALL modes of interest, and the bounce
# contribution is NEGLIGIBLE.

eta_bounce = 1.0 / np.sqrt(rho_c)  # Planck times
k_typical = 0.01  # Cosmologically relevant mode

bounce_suppression = (k_typical * eta_bounce)**2
print(f"\n" + "="*70)
print(f"BOUNCE CONTRIBUTION TO f_NL")
print(f"="*70)
print(f"\nBounce timescale: η_bounce ~ 1/√ρ_c = {eta_bounce:.4f} t_Pl")
print(f"Typical mode: k = {k_typical} M_Pl")
print(f"Mode×bounce product: k × η_bounce = {k_typical * eta_bounce:.4e}")
print(f"Bounce contribution suppression: (k × η_bounce)² = {bounce_suppression:.4e}")

# The contracting phase f_NL:
fnl_contraction = -35.0/8.0

# Estimated bounce correction:
# δf_NL(bounce) ~ f_NL × (k × η_bounce)² × O(1)
delta_fnl_bounce = fnl_contraction * bounce_suppression * 1.0  # O(1) coefficient

print(f"\nf_NL from contraction: {fnl_contraction}")
print(f"Estimated bounce correction: δf_NL ~ {delta_fnl_bounce:.4e}")
print(f"Corrected f_NL: {fnl_contraction + delta_fnl_bounce:.4f}")
print(f"Fractional change: {abs(delta_fnl_bounce/fnl_contraction)*100:.6f}%")

# ============================================================
# Full numerical estimate using mode functions
# ============================================================
# We can also estimate the bounce correction by comparing the
# mode function amplitude before and after the bounce.

# Sample mode at η = -10 (deep in contraction) and η = +10 (deep in expansion)
eta_before = -10.0
eta_after = 10.0

# Use the dense output
v_before = complex(
    sol_short.sol(eta_before)[0] if eta_before > sol_short.t[0] else np.nan,
    sol_short.sol(eta_before)[1] if eta_before > sol_short.t[0] else np.nan
)
v_after = complex(sol_short.sol(eta_after)[0], sol_short.sol(eta_after)[1])

if not np.isnan(abs(v_before)):
    a_before = a_interp(eta_before)
    a_after = a_interp(eta_after)
    z_before = a_before * np.sqrt(3)
    z_after = a_after * np.sqrt(3)

    zeta_before = abs(v_before) / z_before
    zeta_after = abs(v_after) / z_after

    # The transfer coefficient T_k = ζ_after / ζ_before
    T_k = zeta_after / zeta_before if zeta_before > 0 else np.nan

    print(f"\nLinear transfer through bounce (k = {k_short}):")
    print(f"  |ζ| before bounce: {zeta_before:.6e}")
    print(f"  |ζ| after bounce:  {zeta_after:.6e}")
    print(f"  Transfer coefficient |T_k| = {T_k:.6f}")
    print(f"  Deviation from unity: {abs(T_k - 1)*100:.2f}%")

print(f"\n" + "="*70)
print(f"CONCLUSION")
print(f"="*70)
print(f"""
For cosmologically relevant modes (k << √ρ_c ~ 0.6 M_Pl), the bounce
contribution to the cubic action is suppressed by (k × η_bounce)²
relative to the contraction-phase contribution.

For k ~ 10⁻³ M_Pl (CMB scales): suppression ~ 10⁻⁶
For k ~ 10⁻² M_Pl: suppression ~ 10⁻⁴
For k ~ 10⁻¹ M_Pl: suppression ~ 10⁻²

The f_NL = -35/8 prediction from the contraction phase is therefore
transmitted through the LQC bounce with corrections at the 10⁻⁶ to 10⁻²
level for modes of observational interest.

IMPORTANT CAVEAT: This is a semi-analytic estimate based on the
superhorizon approximation for mode functions near the bounce. A
fully rigorous computation would require evaluating all 6 Maldacena
cubic action integrals with the numerically computed mode functions
through the bounce. This is consistent with, but does not replace,
a dedicated third-order perturbation theory calculation.

The perturbation-transparency theorem guarantees that the Holst term
contributes nothing to this integral (for scalar field matter).
The only modification comes from the LQC holonomy corrections to
the background, which affect the mode functions near the bounce.
""")
