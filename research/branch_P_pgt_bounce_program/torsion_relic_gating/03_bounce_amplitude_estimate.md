# 03 — Bounce Amplitude Estimate for the Pseudoscalar Torsion Mode

**Date:** 2026-03-16
**Depends on:** 01 (mode allowed), 02 (equations derived)

---

## 1. The population problem

Files 01 and 02 established:
- phi(t) = S_0(t) is allowed on FRW but not forced
- phi = 0 is a stable fixed point of the field equations
- The bounce does not classically excite phi from zero

The question is now: what sets phi(0)?

## 2. Scenario A: phi(0) as a free initial condition

If phi(0) is a free initial condition with no dynamical determination, then
we need a PRIOR on its value. The natural scales in the problem are:

- M_Pl ~ 2.4 x 10^18 GeV (reduced Planck mass)
- m_T = M_Pl / (2 sqrt(|t_3|)) (torsion mass)
- rho_crit = m_T^2 M_Pl^2 (critical density for bounce)
- T_bounce ~ sqrt(rho_crit) ~ m_T M_Pl (bounce temperature)

**If phi(0) ~ M_Pl (maximal initial condition):**

    rho_phi(0) = (1/2) m_T^2 phi(0)^2 ~ (1/2) m_T^2 M_Pl^2 ~ rho_crit/2

The torsion mode would carry O(1) fraction of the critical density. This
is the scenario needed for the relic program. But there is no mechanism to
SELECT this initial condition. It is pure assumption.

**If phi(0) ~ m_T (natural for a massive field):**

    rho_phi(0) ~ (1/2) m_T^4

    rho_phi/rho_crit ~ m_T^4 / (m_T^2 M_Pl^2) = m_T^2/M_Pl^2 = 1/(4|t_3|)

For |t_3| >> 1 (low bounce scale), this is tiny. For example:
- m_T = 10^{-3} M_Pl: rho_phi/rho_crit ~ 10^{-6}
- m_T = 10^{-6} M_Pl: rho_phi/rho_crit ~ 10^{-12}
- m_T = 10^{-9} M_Pl: rho_phi/rho_crit ~ 10^{-18}

**Result:** Unless phi(0) ~ M_Pl, the torsion relic is negligible.

## 3. Scenario B: Quantum fluctuations during the bounce

During the bounce, the effective Hubble parameter is H ~ alpha = m_T sqrt(8pi/3).
Quantum fluctuations of a massive scalar in de Sitter-like backgrounds have
amplitude:

    delta_phi ~ H_bounce / (2pi) ~ m_T / (2pi)   (if m_T << H_bounce)

But at the bounce, H = 0 exactly! The bounce is NOT de Sitter. The relevant
scale for quantum production is the bounce RATE, characterized by:

    |H-dot|^{1/2} at the bounce ~ alpha ~ m_T (up to O(1) factors)

Particle production by the changing geometry (analogous to Schwinger pair
production) gives:

    <phi^2> ~ m_T^2 / (4pi)^2    (one-loop estimate, massive field)

This gives phi_rms ~ m_T / (4pi), which falls in Scenario A with phi ~ m_T.
The relic fraction is negligible for m_T << M_Pl.

**More careful estimate:** The Bogoliubov coefficient for particle production
during the bounce is:

    |beta_k|^2 ~ exp(-pi k^2 / (a_b^2 |H-dot_bounce|))

For the homogeneous mode (k = 0), this does NOT give a condensate. Particle
production creates PAIRS of particles with opposite momenta, not a
homogeneous VEV. The background phi(t) is not excited by quantum effects.

## 4. Scenario C: Self-consistent bounce requiring phi != 0

Could the bounce solution REQUIRE phi != 0 for self-consistency?

The bounce comes from the modified Friedmann equation:

    H^2 = (8piG/3) rho_m (1 - rho_m/rho_crit)

This equation uses rho_crit = m_T^2 M_Pl^2, which comes from integrating out
the ALGEBRAIC torsion constraint (contact interaction). The propagating mode
phi adds to the energy budget but is NOT required for the bounce.

The bounce occurs when rho_m = rho_crit, regardless of phi. Adding phi to
the energy changes the total density but does NOT change the bounce condition,
which depends only on the matter-torsion contact interaction.

**The bounce is self-consistent with phi = 0.** The propagating mode is a
SPECTATOR.

## 5. Scenario D: Pre-bounce cosmology seeds phi

If there is a contracting phase before the bounce (as in cyclic or
matter-bounce scenarios), could the dynamics of that phase seed phi?

In the contracting phase with H < 0, the friction term 3H phi-dot becomes
anti-friction. If phi has ANY small initial displacement, it grows
exponentially during contraction. However:

- If phi = 0 exactly at early times, it stays at zero (stable fixed point)
- Quantum fluctuations in the contracting phase do generate delta_phi ~ H/2pi,
  but the BACKGROUND remains at zero
- The k = 0 mode of phi is not excited by the contraction (same parity argument)

The anti-friction during contraction amplifies EXISTING oscillations of phi
but cannot CREATE a VEV from zero. This is the same Z_2 symmetry argument.

## 6. Scenario E: Explicit parity breaking

If the matter sector has explicit parity violation (e.g., chiral fermions
with unequal left/right densities), then there IS a source term:

    phi-ddot + 3H phi-dot + m_T^2 phi = kappa * J^5

where J^5 is the axial current density of matter. In the early universe with
chiral asymmetry:

    J^5 ~ n_L - n_R ~ eta_5 * T^3

where eta_5 is the chiral asymmetry parameter and T is the temperature.

At the bounce (T ~ T_bounce ~ sqrt(m_T M_Pl)):

    phi_sourced ~ kappa J^5 / m_T^2 ~ (J^5 / M_Pl^2) / m_T^2

For J^5 ~ T_bounce^3 ~ (m_T M_Pl)^{3/2}:

    phi_sourced ~ (m_T M_Pl)^{3/2} / (M_Pl^2 m_T^2) = (m_T/M_Pl)^{-1/2} / M_Pl

Wait, let me redo this carefully:

    phi ~ kappa J^5 / m_T^2 = (8piG) J^5 / m_T^2 = (8pi/M_Pl^2) J^5 / m_T^2

With J^5 ~ eta_5 T^3 ~ eta_5 (m_T M_Pl)^{3/2}:

    phi ~ (8pi eta_5 / M_Pl^2) * (m_T M_Pl)^{3/2} / m_T^2
        = 8pi eta_5 * m_T^{3/2} M_Pl^{3/2} / (M_Pl^2 m_T^2)
        = 8pi eta_5 * M_Pl^{-1/2} m_T^{-1/2}
        = 8pi eta_5 / sqrt(m_T M_Pl)

For m_T = 10^{-3} M_Pl: phi ~ 8pi eta_5 / (sqrt(10^{-3}) M_Pl) ~ 250 eta_5 / M_Pl
For m_T = 10^{-6} M_Pl: phi ~ 8pi eta_5 / (10^{-3} M_Pl) ~ 2.5 x 10^4 eta_5 / M_Pl

This is tiny unless eta_5 ~ O(1), and even then phi << M_Pl.

**Even with maximal chiral asymmetry (eta_5 ~ 1), the sourced amplitude is
phi << M_Pl. The relic energy density is negligible.**

## 7. Summary of amplitude estimates

| Scenario | phi(0) | rho_phi/rho_crit | Mechanism |
|----------|--------|------------------|-----------|
| A: phi ~ M_Pl | M_Pl | O(1) | Free IC, no justification |
| A: phi ~ m_T | m_T | m_T^2/M_Pl^2 | Natural scale, negligible |
| B: Quantum | m_T/(4pi) | m_T^2/(16pi^2 M_Pl^2) | Particle production, negligible |
| C: Self-consistent | 0 | 0 | Bounce works without phi |
| D: Contraction | 0 | 0 | Parity protects phi = 0 |
| E: Chiral source | << M_Pl | << 1 | Even maximal source is weak |

## 8. Verdict

**There is no known mechanism to populate phi to O(M_Pl) at the bounce.**

The ONLY way to get a significant torsion relic is to ASSUME phi(0) ~ M_Pl
as an initial condition. This is:
- Not required by self-consistency
- Not generated by the bounce dynamics
- Not produced by quantum effects
- Not sourced by matter (unless wildly beyond known chiral asymmetry)

The amplitude phi(0) is a completely free parameter, and the natural value
is phi = 0.

**This is a serious problem for the relic program.**
