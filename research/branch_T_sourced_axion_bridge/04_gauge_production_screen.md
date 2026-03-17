# Branch T: Gauge Field Production Screen

**Date:** 2026-03-16

---

## Can xi_b reach O(1)?

From File 03, the answer is: **conditionally yes, but only with two free parameters.**

The instability parameter:

    xi = n_5 / (2 f_a^2 H)

reaches O(1) when:
- n_5 ~ T_b^3 (maximal chiral polarization) — free parameter
- Delta s / s ~ 1 (maximal dissipation) — free parameter
- f_a <= M_Pl (for ECH bounce) or f_a <= 10^{17} GeV (for PGT bounce)

Under these optimistic assumptions, we can ask: what gauge amplification would result?

---

## Gauge mode equation through the bounce

For a gauge field A_mu coupled to the axion via (alpha_X / 4 f_a) a F F-tilde, the mode equation for the positive helicity in conformal time eta is:

    A_+''(k, eta) + [k^2 - 2 k xi a_conf H_conf] A_+(k, eta) = 0

where a_conf is the scale factor and H_conf = a_conf H is the conformal Hubble parameter.

**At the bounce:** H = 0, so a_conf H_conf = a_conf * 0 = 0. The tachyonic term VANISHES at the exact bounce point.

**Before the bounce (contraction):** H < 0. If a-dot > 0, then xi < 0 during contraction. The tachyonic instability occurs for the NEGATIVE helicity, not the positive one (or vice versa depending on sign conventions).

**After the bounce (expansion):** H > 0. Standard tachyonic amplification for xi > 0.

**Key point:** The amplification is NOT concentrated at the bounce. It occurs in the epochs where |H| is significant and xi has a definite sign. The bounce itself is a node of the tachyonic term.

---

## Integrated amplification estimate

The standard result for constant xi during slow-roll inflation:

    A_+(k) ~ exp(pi xi) for k/(aH) ~ 2 xi

This exponential amplification occurs over one e-fold of expansion.

For the bounce, xi is NOT constant. It changes sign and magnitude on a timescale ~ t_b.

The effective number of e-folds of amplification:

    N_eff ~ H_max * t_b ~ 1 (for ECH bounce)

(The bounce lasts about one Hubble time at maximum expansion rate.)

So the amplification is roughly:

    A_+ / A_+^{vac} ~ exp(pi xi_max * N_eff) ~ exp(pi xi_max)

For xi_max ~ 1: amplification factor ~ exp(pi) ~ 23
For xi_max ~ 3: amplification factor ~ exp(3 pi) ~ 8000
For xi_max ~ 10: amplification factor ~ exp(10 pi) ~ 10^{14}

**Energy density in gauge fields:**

    rho_X ~ (H_max^4 / (8 pi^2)) * exp(2 pi xi_max) * (2 xi_max)^4

For xi_max = 1, H_max = 0.13 M_Pl:

    rho_X ~ (0.13 M_Pl)^4 / (8 pi^2) * e^{2pi} * 16
    rho_X ~ 2.9 x 10^{-4} M_Pl^4 * 535 * 16
    rho_X ~ 2.5 M_Pl^4

This EXCEEDS rho_crit = 0.21 M_Pl^4. Backreaction is catastrophic.

**This means xi_max ~ 1 at the Planck-scale bounce is actually TOO MUCH gauge production.** The produced gauge fields would dominate the energy density and invalidate the background solution.

---

## Backreaction constraint

Requiring rho_X < rho_crit:

    (H_max^4 / (8 pi^2)) * exp(2 pi xi) * (2 xi)^4 < rho_crit

For ECH bounce (H_max ~ 0.13 M_Pl, rho_crit ~ 0.21 M_Pl^4):

    exp(2 pi xi) * (2 xi)^4 < 0.21 / (2.9 x 10^{-4} / 16) ~ 1.2 x 10^4

    For xi = 1: LHS ~ 535 * 16 = 8560 < 1.2 x 10^4. Barely OK.
    For xi = 1.5: LHS ~ e^{3pi} * 81 ~ 8000 * 81 ~ 6.5 x 10^5. VIOLATES.

So the backreaction constraint limits xi_max < 1.1 at the Planck-scale bounce.

This is a CONSISTENCY problem: the parameter space where xi is large enough to produce significant gauge amplification is also where backreaction destroys the bounce.

---

## For PGT bounce (lower scale)

H_max = 0.13 m_T, rho_crit = m_T^2 M_Pl^2.

    rho_X ~ (0.13 m_T)^4 / (8 pi^2) * exp(2 pi xi) * (2 xi)^4

Backreaction constraint: rho_X < m_T^2 M_Pl^2

    (0.13 m_T)^4 * exp(2 pi xi) * (2 xi)^4 / (8 pi^2) < m_T^2 M_Pl^2

    exp(2 pi xi) * (2 xi)^4 < 8 pi^2 * (M_Pl / m_T)^2 / 0.13^4 ~ 2.8 x 10^5 * (M_Pl/m_T)^2

For m_T = 10^{-3} M_Pl: RHS ~ 2.8 x 10^{11}. Allows xi up to ~ 4.
For m_T = 10^{-6} M_Pl: RHS ~ 2.8 x 10^{17}. Allows xi up to ~ 6.5.

But from File 03, the PGT bounce gives xi ~ (m_T/M_Pl)^{1/2} << 1 for f_a ~ M_Pl. The PGT bounce relaxes the backreaction constraint but simultaneously reduces xi. These trends work against each other, and the NET result is still xi << 1 for the PGT bounce unless f_a << M_Pl.

---

## Verdict on gauge production

1. **ECH (Planck-scale) bounce:** xi ~ 1 is achievable with maximal free parameters, but backreaction limits xi < 1.1. The narrow window xi in [0.5, 1.1] produces moderate gauge amplification (factor ~ 5-25) but this is a one-shot event lasting ~ 1 Planck time. The produced gauge field energy is at most comparable to the background — not a clean perturbative signal.

2. **PGT bounce:** xi << 1 for natural parameters. No significant gauge production.

3. **The fundamental problem:** The bounce is too short (~ 1/H_max) for sustained amplification. Unlike inflation (which provides 50-60 e-folds of amplification time), the bounce provides ~ 1 e-fold. To compensate, you need xi >> 1, but backreaction prevents this.

**Gauge production from the bounce is not viable as a clean, perturbative observable channel.**
