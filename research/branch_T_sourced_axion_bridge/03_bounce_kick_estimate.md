# Branch T: Bounce Kick Estimate — Central Calculation

**Date:** 2026-03-16

---

## Setup and conventions

- Natural units: hbar = c = 1
- M_Pl = (8 pi G)^{-1/2} = 2.4 x 10^{18} GeV (reduced Planck mass)
- Bounce scale (minimal ECH): rho_crit = 0.21 M_Pl^4
- Bounce scale (PGT): rho_crit = m_T^2 M_Pl^2, with m_T << M_Pl
- Temperature at bounce: T_b ~ rho_crit^{1/4}
- Bounce duration: t_b ~ 1/H_max ~ (M_Pl / rho_crit^{1/2})
- Modified Friedmann: H^2 = (8 pi G / 3) rho (1 - rho/rho_crit)
- At bounce: H = 0, rho = rho_crit
- Maximum H: H_max = M_Pl / (2 sqrt{3}) * (rho_crit / M_Pl^4)^{1/2} for radiation

For minimal ECH: H_max ~ 0.13 M_Pl, t_b ~ 8 / M_Pl ~ 3.3 x 10^{-44} s
For PGT: H_max ~ 0.13 m_T, t_b ~ 8 / m_T

---

## Candidate A: Derivative coupling to axial current

### Equation of motion

    a-ddot + 3 H a-dot + m_a^2 a = (1/f_a) [J-dot^5_0 + 3 H J^5_0]

During the bounce, m_a^2 a is negligible (m_a << H_max for any relevant ALP). The 3H a-dot term changes sign at the bounce. Focus on the source.

### Source strength

The source is S_A = (1/f_a) (d/dt)(J^5_0) + (3H/f_a) J^5_0.

**Case 1: Pre-existing chiral asymmetry n_5**

If there exists a chiral chemical potential mu_5, then:

    J^5_0 = n_5 ~ mu_5 T^2 / 6  (for T >> mu_5, fermion species ~ 1)

At the bounce, T ~ rho_crit^{1/4}. The time derivative J-dot^5_0 arises from the change in T(t) and the compression/decompression:

    J-dot^5_0 ~ n_5 * (3 T-dot/T) ~ n_5 * 3 |H|

(using T-dot/T ~ -H in radiation era, with |H| ~ H_max near the bounce).

Near the bounce, J-dot^5_0 changes sign (from increasing to decreasing density). The NET kick to a-dot is:

    Delta(a-dot) ~ integral S_A dt ~ (1/f_a) * integral [J-dot^5_0 + 3H J^5_0] dt

The integral of J-dot^5_0 over a symmetric bounce: integral J-dot^5_0 dt = J^5_0(after) - J^5_0(before).

If the bounce is symmetric (same temperature before and after at the same |H|), then J^5_0(after) = J^5_0(before) and the integral of J-dot^5_0 VANISHES.

The integral of 3H J^5_0 dt: H < 0 before bounce, H > 0 after. If J^5_0 is roughly constant through the bounce:

    integral 3H J^5_0 dt ~ 3 J^5_0 * integral H dt = 3 J^5_0 * [ln a(t_f) - ln a(t_i)]

For a symmetric bounce, a(t_f) = a(t_i) at corresponding times, so this integral is also ~ 0 over the full bounce.

**This is a critical result: for a symmetric bounce, the net axion kick from Candidate A is zero to leading order.**

The kick comes from ASYMMETRY of the bounce. In the spin-torsion bounce, the contraction and expansion phases are exactly symmetric under t -> -t (time-reversal). So Delta(a-dot) = 0 at leading order.

### Subleading contributions

The bounce is not perfectly symmetric when:
- Entropy is produced (dissipation)
- Particle species change (thresholds)
- The axion back-reacts

These are higher-order effects. The leading correction from entropy production:

    Delta(a-dot) ~ (1/f_a) * n_5 * (Delta s / s) * H_max * t_b

where Delta s / s is the fractional entropy increase through the bounce. For a nearly-adiabatic bounce, Delta s / s << 1.

Even optimistically with Delta s / s ~ 1 (maximal dissipation):

    Delta(a-dot) ~ n_5 / f_a

Then:

    xi = Delta(a-dot) / (2 f_a H) = n_5 / (2 f_a^2 H)

### Numerical evaluation (minimal ECH bounce)

T_b ~ (0.21)^{1/4} M_Pl ~ 0.68 M_Pl
H_max ~ 0.13 M_Pl

For MAXIMAL chiral asymmetry: n_5 ~ T_b^3 ~ 0.31 M_Pl^3

    xi = 0.31 M_Pl^3 / (2 f_a^2 * 0.13 M_Pl) = 0.31 / (0.26) * M_Pl^2 / f_a^2

    xi ~ 1.2 * (M_Pl / f_a)^2

For f_a = M_Pl: xi ~ 1.2 (barely O(1))
For f_a = 10^{16} GeV: xi ~ 1.2 * (2.4 x 10^{18} / 10^{16})^2 ~ 690
For f_a = 10^{12} GeV: xi ~ 1.2 * (2.4 x 10^{18} / 10^{12})^2 ~ 7 x 10^{12}

**BUT** this requires:
1. Maximal chiral asymmetry n_5 ~ T^3 (complete chiral polarization)
2. Maximal dissipative asymmetry Delta s/s ~ 1
3. Both are free parameters, not predictions

For a THERMAL chiral fluctuation (no pre-existing asymmetry):

    n_5 ~ T_b^{3/2} / V^{1/2} (per Hubble volume, V ~ H_max^{-3})

    n_5,fluct ~ T_b^{3/2} * H_max^{3/2} ~ (0.68 M_Pl)^{3/2} * (0.13 M_Pl)^{3/2} ~ 0.17 M_Pl^3

This is actually not far from maximal because at the Planck scale, there are O(1) particles per Planck volume. But these fluctuations are STOCHASTIC, not coherent across the entire universe. They would produce a stochastic axion kick, varying from patch to patch.

### Numerical evaluation (PGT bounce, m_T << M_Pl)

T_b ~ (m_T M_Pl)^{1/2}
H_max ~ 0.13 m_T
n_5,max ~ T_b^3 ~ (m_T M_Pl)^{3/2}

    xi = (m_T M_Pl)^{3/2} / (2 f_a^2 * 0.13 m_T)

    xi = (m_T M_Pl)^{3/2} / (0.26 f_a^2 m_T)

    xi = M_Pl^{3/2} m_T^{1/2} / (0.26 f_a^2)

For f_a = M_Pl:

    xi = (m_T / M_Pl)^{1/2} / 0.26

For m_T = 10^{-3} M_Pl: xi ~ 0.12
For m_T = 10^{-6} M_Pl: xi ~ 0.004
For m_T = 10^{-10} M_Pl: xi ~ 1.2 x 10^{-5}

**The PGT bounce makes xi WORSE.** Lower bounce scale -> smaller kick. This is because both n_5 and H_max decrease, and n_5 decreases faster than H.

### For f_a << M_Pl with PGT bounce

    xi = M_Pl^{3/2} m_T^{1/2} / (0.26 f_a^2)

Setting xi = 1: f_a^2 = M_Pl^{3/2} m_T^{1/2} / 0.26

    f_a = (M_Pl^{3/2} m_T^{1/2} / 0.26)^{1/2} = M_Pl^{3/4} m_T^{1/4} / 0.51

For m_T = 10^{-3} M_Pl: f_a ~ 0.35 M_Pl^{3/4} (10^{-3} M_Pl)^{1/4} ~ 0.062 M_Pl ~ 1.5 x 10^{17} GeV
For m_T = 10^{-6} M_Pl: f_a ~ 7.8 x 10^{16} GeV
For m_T = 10^{-10} M_Pl: f_a ~ 1.1 x 10^{16} GeV

So xi >= 1 requires f_a <= 10^{17} GeV even for PGT, which is within the standard ALP window. But this still requires maximal n_5 and maximal dissipation.

---

## Candidates B-G: Non-starters

All other candidates have ZERO source on FRW (see File 02):

- B: R-tilde-R = 0 on FRW. Source = 0.
- C: Reduces to A after torsion elimination.
- D: Immirzi drops out on-shell. Source = 0.
- E: Reduces to C in RC geometry. Source = 0.
- F: No oscillatory H in spin-torsion bounce. No parametric resonance.
- G: No dynamical n_5 generation (FRW parity symmetry). Source = 0.

---

## Critical assessment

The ONLY viable source term is Candidate A, and it has three compounding problems:

1. **Symmetric bounce cancellation:** The time-reversal symmetry of the bounce means the leading-order net kick vanishes. Only the dissipative asymmetry contributes, and this is a free parameter.

2. **Chiral asymmetry as input:** n_5 is not predicted by the bounce. It is an initial condition from before the bounce (or generated by unknown pre-bounce physics). The bounce acts as a transmitter, not a generator.

3. **Only works at Planck scale:** The kick scales as xi ~ (T_b/f_a)^2 * (n_5/T_b^3). For sub-Planckian bounces (PGT), xi decreases as (m_T/M_Pl)^{1/2}.

**Honest verdict:** The axion bridge does not produce a bounce-specific, parameter-free kick. The signal requires both a pre-existing chiral asymmetry AND a dissipative bounce, neither of which is a prediction of spin-torsion cosmology.
