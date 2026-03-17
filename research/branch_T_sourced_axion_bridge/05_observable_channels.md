# Branch T: Observable Channels Assessment

**Date:** 2026-03-16

---

## Summary from Files 03-04

Gauge production through the bounce is not viable:
- ECH bounce: xi <= 1.1 (backreaction), amplification ~ 5-25x, single Planck-time event
- PGT bounce: xi << 1, negligible amplification
- Fundamental limitation: ~ 1 e-fold of amplification time vs. ~ 60 for inflation

Given this, we assess whether ANY observable channel survives.

---

## Channel 1: Gravitational waves from gauge field production

Even in the optimistic case (ECH bounce, xi ~ 1):

    Omega_GW ~ (H_max / M_Pl)^2 * exp(4 pi xi) / (some numerical factor)

For xi = 1, H_max = 0.13 M_Pl:

    Omega_GW ~ 0.017 * exp(4 pi) ~ 0.017 * 2.9 x 10^5 ~ 5000

This is nonsensical (Omega_GW > 1), which confirms the backreaction problem. In the self-consistent regime (backreaction limits the amplitude), Omega_GW is at most O(1) at the bounce frequency, which is:

    f_bounce ~ H_max / (2 pi) * (a_bounce / a_0) ~ 10^{43} Hz * (a_bounce / a_0)

The redshift factor a_bounce/a_0 depends on the entire post-bounce expansion history. For a Planck-scale bounce followed by standard Big Bang:

    a_bounce / a_0 ~ T_0 / T_bounce ~ 2.7 K / (10^{32} K) ~ 10^{-32}

    f_bounce,today ~ 10^{43} * 10^{-32} ~ 10^{11} Hz

This is far above any GW detector bandwidth:
- LIGO/Virgo/KAGRA: 10 - 10^4 Hz
- LISA: 10^{-4} - 10^{-1} Hz
- PTA: 10^{-9} - 10^{-7} Hz
- BBO/DECIGO: 10^{-1} - 10 Hz

**Verdict: UNOBSERVABLE.** The bounce GW signal is at 10^{11} Hz, 7 orders of magnitude above any planned detector.

---

## Channel 2: Magnetic field generation

Amplified gauge fields during the bounce could seed primordial magnetic fields.

Coherence length at production: l_bounce ~ 1/H_max ~ l_Pl
Redshifted to today: l_today ~ l_Pl * (a_0/a_bounce) ~ 10^{-35} m * 10^{32} ~ 10^{-3} m

This is ~ 1 mm. Primordial magnetic field observations require coherence on Mpc scales (~ 10^{22} m). The bounce-produced fields are 25 orders of magnitude too small in coherence length.

Subsequent MHD evolution can transfer power to larger scales (inverse cascade), but the maximum coherence length achievable is limited by causality and the magnetic helicity spectrum. Even optimistically, inverse cascade gains ~ 3-4 orders of magnitude.

**Verdict: UNOBSERVABLE.** Coherence scale 22+ orders too small.

---

## Channel 3: CMB birefringence

If the axion has a net displacement Delta a through the bounce, this could source cosmic birefringence:

    beta = (alpha_EM / 4 f_a) * Delta a

From the bounce kick: Delta a ~ a-dot_b * t_b ~ (xi * 2 f_a H_max) * (1/H_max) = 2 xi f_a

    beta = (alpha_EM / 4 f_a) * 2 xi f_a = alpha_EM xi / 2

For xi ~ 1: beta ~ alpha_EM / 2 ~ 0.004 rad ~ 0.2 degrees

This is in the range of current CMB birefringence measurements (beta ~ 0.3 degrees from Minami-Komatsu). BUT:

1. The birefringence angle depends on the NET axion displacement from the bounce to recombination, not just the bounce kick.
2. After the bounce, the axion oscillates (when H drops below m_a) and the displacement averages to zero — unless the axion is ultra-light (m_a < H_recomb ~ 10^{-29} eV).
3. For ultra-light axions (m_a < 10^{-29} eV), f_a is unconstrained by the bounce — the axion's value at recombination is set by its initial misalignment, not by the bounce kick.
4. The bounce kick to a is of order f_a (as computed above), which is the SAME ORDER as the generic misalignment initial condition theta_i * f_a.

**Verdict: DEGENERATE.** The bounce kick is indistinguishable from a generic initial misalignment angle. No distinctive bounce signature.

---

## Channel 4: Baryon asymmetry from axiogenesis

If the axion kick sources a chemical potential for baryons (axiogenesis, Co-Harigaya 2020):

    n_B/s ~ (a-dot / f_a) / T ~ xi * H / T

At the bounce: n_B/s ~ xi * H_max / T_b ~ xi * 0.13 M_Pl / (0.68 M_Pl) ~ 0.19 xi

For xi ~ 1: n_B/s ~ 0.2

This is ~ 10^{10} times the observed value (n_B/s ~ 10^{-10}). Overproduction by 10 orders of magnitude.

This could be diluted by subsequent entropy production, but this requires additional model-building unrelated to the bounce.

**Verdict: OVERPRODUCTION.** Not a viable observable without fine-tuned dilution.

---

## Channel 5: Dark matter production

The gauge fields amplified during the bounce could produce dark matter particles. But the production is localized at the bounce frequency ~ M_Pl, producing particles with mass ~ M_Pl. These are over-dense and would dominate the universe immediately — the same backreaction problem.

**Verdict: OVERCLOSURE.** Same as backreaction problem.

---

## What would need to change

For the axion bridge to work, we would need:

1. **A longer bounce:** N_eff >> 1 e-folds of tachyonic amplification. This requires a non-standard bounce (e.g., matter-bounce scenario with extended contraction phase). But this is not the spin-torsion bounce — it's a different model entirely.

2. **A lower-frequency signal:** The bounce would need to occur at energies << M_Pl to redshift into observable bands. The PGT bounce can achieve this, but xi << 1 at lower scales.

3. **A distinctive spectral shape:** Even if the amplitude were detectable, we would need a spectral feature that distinguishes "bounce + axion" from "generic ALP cosmology." No such feature has been identified.

4. **Parametric decoupling from initial conditions:** The signal should depend on bounce physics (rho_crit, spin density), not on the pre-existing chiral asymmetry n_5. Currently, n_5 is the dominant parameter.

None of these are achievable within the spin-torsion framework as defined.
