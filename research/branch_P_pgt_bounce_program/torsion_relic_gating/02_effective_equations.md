# 02 — Background Equations for the Pseudoscalar Torsion Mode on FRW

**Date:** 2026-03-16
**Depends on:** 01_frw_pseudoscalar_mode.md (mode is allowed but not forced)

---

## 1. Setup

We work with the PGT Sector II (spin-0^-, ghost-free) restricted to FRW.

Dynamical variables:
- a(t): scale factor
- phi(t) = S_0(t): pseudoscalar torsion mode (time component of axial vector)

Metric: ds^2 = -dt^2 + a(t)^2 (dx^2 + dy^2 + dz^2)

The propagating Sector II mode gets its kinetic term from the curvature-squared
part of the PGT Lagrangian. After reduction to FRW, the effective action for
phi(t) is:

## 2. Effective action on FRW

The PGT Lagrangian (torsion sector, quadratic):

    L_T = (1/2kappa) [t_1 T^a_{mu nu} T_a^{mu nu} + t_2 T^a_{mu nu} T^{mu nu}_a + t_3 T^a_{mu a} T^{mu b}_b]

Ghost-free conditions: t_2 = -2t_1, t_3 < 0.

The curvature-squared terms that give propagation to the spin-0^- mode have
the schematic form (after gauge fixing and using the ghost-free constraints):

    L_R^2 ~ (alpha_i / kappa) R_{mu nu rho sigma} R^{mu nu rho sigma} terms

After FRW reduction, these yield (for the axial mode only):

    L_eff = a^3 [(1/2) f(t_i, alpha_i) phi-dot^2 - (1/2) m_T^2 phi^2]

where:
- f(t_i, alpha_i) is a function of PGT parameters that sets the kinetic normalization
- m_T^2 = M_Pl^2 / (4|t_3|) is the torsion mass squared

For the canonical analysis, we define the canonically normalized field:

    chi = sqrt(f) * phi

so that L_eff = a^3 [(1/2) chi-dot^2 - (1/2) m_eff^2 chi^2 + ...]

**Key structural point:** The precise form of f depends on which curvature-squared
terms are included. For the minimal Sector II model, the result is equivalent
to a massive pseudoscalar with gravitational-strength coupling. We proceed
with the canonical form assuming f has been absorbed into the field definition.

## 3. Coupled equations of motion

### Friedmann equation (modified):

    H^2 = (8piG/3) [rho_matter + rho_phi]

where the torsion energy density is:

    rho_phi = (1/2) phi-dot^2 + (1/2) m_T^2 phi^2

and the torsion pressure is:

    p_phi = (1/2) phi-dot^2 - (1/2) m_T^2 phi^2

**Important:** The bounce modification H^2 = (8piG/3) rho (1 - rho/rho_crit)
comes from the CONTACT interaction (spin-density)^2 in the matter sector.
This is a SEPARATE contribution from the propagating mode. The full equation is:

    H^2 = (8piG/3) [rho_m (1 - rho_m/rho_crit) + rho_phi]

where rho_m is the matter density and rho_phi is the propagating torsion
density. This assumes rho_phi << rho_crit (the propagating mode does not
contribute to the bounce mechanism itself in the regime where it is
subdominant).

If rho_phi ~ rho_crit, then the full nonlinear coupling must be retained.
But this requires phi ~ M_Pl, which is the scenario we are testing.

### Klein-Gordon equation for phi:

    phi-ddot + 3H phi-dot + m_T^2 phi = 0

There is NO source term on the right-hand side for parity-even matter.
The Hubble friction term 3H phi-dot arises from the FRW expansion.

### Raychaudhuri equation:

    H-dot = -4piG [rho_m + p_m + rho_phi + p_phi] (1 - 2rho_total/rho_crit)
          = -4piG [(rho_m + p_m)(1 - 2rho_m/rho_crit) + phi-dot^2]

(The last line assumes rho_phi << rho_crit.)

## 4. Structure of the coupled system

The system is:

    (i)   H^2 = (8piG/3) [rho_m(1 - rho_m/rho_crit) + (1/2)phi-dot^2 + (1/2)m_T^2 phi^2]
    (ii)  phi-ddot + 3H phi-dot + m_T^2 phi = 0
    (iii) rho_m-dot + 3H(rho_m + p_m) = 0

with p_m = w_m rho_m (e.g., w_m = 1/3 for radiation).

### Ghost-free check:

The kinetic term for phi is (1/2) phi-dot^2 with POSITIVE sign. This is
guaranteed by the Sector II ghost-free conditions (t_2 = -2t_1, t_3 < 0).
The mode is NOT a ghost.

### Equation of state:

    w_phi = p_phi / rho_phi = (phi-dot^2 - m_T^2 phi^2) / (phi-dot^2 + m_T^2 phi^2)

- Kinetic dominated (phi-dot >> m_T phi): w_phi -> +1 (stiff matter)
- Potential dominated (phi-dot << m_T phi): w_phi -> -1 (cosmological constant-like)
- Oscillating (H << m_T): time-averaged <w_phi> = 0 (pressureless matter)

## 5. Coupling between phi and the bounce

**This is the critical question: does the bounce excite phi?**

Examining equation (ii): phi-ddot + 3H phi-dot + m_T^2 phi = 0.

During the bounce:
- H goes through zero (H = 0 at the bounce point)
- H-dot > 0 at the bounce (deceleration reverses to acceleration)
- H changes sign: H < 0 (contraction) -> H = 0 (bounce) -> H > 0 (expansion)

The friction term 3H phi-dot changes sign at the bounce:
- Contracting phase: 3H < 0, so this is ANTI-friction (amplification)
- Expanding phase: 3H > 0, so this is friction (damping)

**But if phi = 0 and phi-dot = 0 initially, then phi-ddot = 0 by equation (ii).
The field stays at zero. The bounce does NOT excite phi from zero initial conditions.**

This is a direct consequence of the Z_2 parity symmetry: phi -> -phi leaves
the equations invariant, and phi = 0 is a fixed point.

## 6. Parametric resonance check

Could the time-varying H(t) during the bounce parametrically excite phi?

The equation phi-ddot + 3H(t) phi-dot + m_T^2 phi = 0 has time-dependent
coefficients. For the HOMOGENEOUS mode (k=0), this is a damped harmonic
oscillator with time-dependent damping. Parametric resonance requires
INHOMOGENEOUS modes (k != 0) where the effective frequency
omega_k^2 = k^2/a^2 + m_T^2 varies periodically.

For the bounce background, a(t) = a_b (1 + 4 alpha^2 t^2)^{1/4}:
- a(t) has a minimum at t = 0
- omega_k^2(t) = k^2/a(t)^2 + m_T^2 varies in time
- This is NOT periodic — it's a single transient event

**Conclusion:** There is no parametric resonance for the homogeneous mode.
Inhomogeneous modes (k != 0) can be excited by the time-varying scale factor,
but this is particle production, not a background VEV. The BACKGROUND phi(t)
remains at zero if it starts there.

## 7. Summary of equation structure

| Feature | Result |
|---------|--------|
| Kinetic sign | Positive (ghost-free) |
| Mass term | m_T^2 > 0 (stable) |
| Source term | Zero for parity-even matter |
| Coupling to bounce | Only through H(t) in friction term |
| phi = 0 stability | Stable fixed point, not excited by bounce |
| EOS (oscillating) | w = 0 (matter-like) |

**The equations confirm: phi = 0 is a consistent, stable, unforced solution
throughout the bounce. The bounce does not excite the pseudoscalar mode
from zero initial conditions.**
