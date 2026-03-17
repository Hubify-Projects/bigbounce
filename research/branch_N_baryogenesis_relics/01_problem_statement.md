# Branch N: Baryogenesis and Relic Production from the Spin-Torsion Bounce

## Problem Statement

**Date:** 2026-03-16

---

## Motivation: Why Relics Instead of DE

The program A-M has conclusively demonstrated that the spin-torsion
bounce cannot produce late-time (DE, low-energy) observables. Twelve
structural barriers block every bounce-to-DE route.

However, the bounce IS a genuine physical event: a brief, violent,
Planck-density epoch with a specific four-fermion interaction
L_eff = -(3/16)(kappa^2/(1-3gamma^2 kappa xi^2))(J^5)^2 that
couples directly to fermion chirality. The question is whether this
event can affect EARLY-UNIVERSE relics (baryon asymmetry, dark matter
abundance, relic populations) that ARE observable today.

### Why this route is better aligned than DE derivation

1. **Timescale match:** The bounce occurs at or near the Planck epoch.
   Baryogenesis/leptogenesis mechanisms also operate at high energies.
   No 10^28-order scale separation needed.

2. **Interaction type:** The (J^5)^2 four-fermion interaction couples
   to CHIRALITY, which is precisely the quantum number relevant to
   baryon/lepton asymmetry (B-L is tied to chiral anomalies).

3. **Out-of-equilibrium:** The bounce is a transient, non-thermal,
   far-from-equilibrium event -- satisfying the third Sakharov
   condition automatically.

4. **Density scale:** At rho ~ M_Pl^4 (ECH) or rho ~ m_T^2 M_Pl^2
   (PGT), particle production and non-perturbative effects are
   maximally strong.

### Why skepticism is still warranted

1. The bounce duration is t_bounce ~ t_Pl ~ 10^{-43} s (ECH), so
   any process must act within a single Planck time.

2. The (J^5)^2 interaction is PARITY-EVEN. It does not violate C or
   CP by itself. Any asymmetry generation requires either:
   - pre-existing CP phases in the matter sector, or
   - coupling to a CP-odd background that torsion does NOT provide
     on FRW (R-tilde R = 0, Pontryagin density vanishes).

3. Gravitational particle production at a bounce is GENERIC -- any
   bounce produces particles via nonadiabatic expansion. The question
   is whether the spin-torsion mechanism adds anything specific.

4. The mass-coupling lock (Barrier 1) means propagating torsion
   effects are suppressed by g_eff ~ m_T/M_Pl^2.

---

## What Counts as a Real Early-to-Late Bridge

A genuine bridge must satisfy ALL of:

1. **The bounce drives or significantly modifies the mechanism.**
   Removing the bounce (replacing with, e.g., inflation or a
   different bounce) must change the prediction. If the effect is
   the same for any high-energy epoch, it fails.

2. **The mechanism uses genuine spin-torsion / axial / bounce physics.**
   The (J^5)^2 interaction, the modified Friedmann equation
   H^2 = (8piG/3)rho(1-rho/rho_crit), or the specific bounce
   profile a(t) = a_b(1+4alpha^2 t^2)^{1/4} must enter the
   calculation in a way that affects the output.

3. **The result is not standard gravitational particle production
   with torsion language.** Bogoliubov coefficients from nonadiabatic
   expansion exist for ANY bounce. Dressing this in torsion notation
   does not make it spin-torsion specific.

4. **The outcome is testable or constraining.** The prediction must
   either (a) match an observed quantity (eta_B, Omega_DM), or
   (b) produce a constraint on model parameters, or (c) predict a
   distinctive signature.

---

## Success Criteria

### Strong success (BRANCH_N_PROMISING)

- A mechanism where the spin-torsion (J^5)^2 interaction or the
  axial chemical potential mu_5 ~ G xi n_5 quantitatively determines
  or significantly modifies a relic abundance or asymmetry.
- The result depends on ECH/PGT parameters (gamma, rho_crit, m_T)
  in a non-trivial way.
- The predicted value is within the observationally interesting
  range.

### Moderate success (BRANCH_N_MIXED)

- A mechanism survives structural tests but the predicted abundance
  is either too small by a few orders of magnitude or depends on
  unknown pre-bounce initial conditions.
- A meaningful constraint on model parameters emerges.

### Weak success (BRANCH_N_WEAK_BUT_WORTH_ONE_TEST)

- One candidate survives cheap-kill screening and a single focused
  calculation could yield a clean kill or a positive result.
- The mechanism is genuinely torsion-specific even if quantitatively
  marginal.

### Failure (BRANCH_N_CLOSED)

- All candidates fail structural tests.
- Effects are either too weak, generic to any bounce, or require
  physics beyond the model.
- No calculation target remains.

---

## Failure Criteria (Quick Kills)

A candidate is DEAD if any of the following hold:

1. **Too weak:** The effect produces eta_B < 10^{-20} or
   Omega_DM h^2 < 10^{-10} (more than 10 orders below target).

2. **Generic:** The same effect occurs for any bounce at the same
   energy scale, with no dependence on spin-torsion specifics.

3. **Absurd couplings:** Requires coupling constants orders of
   magnitude beyond natural values or masses in excluded ranges.

4. **No predictive yield:** The mechanism has enough free parameters
   to accommodate any value of the target observable (tunable
   storytelling).

5. **Decorative torsion:** The calculation would proceed identically
   if the word "torsion" were replaced by "generic Planck-scale
   physics."

---

## Key Physical Parameters

| Quantity | ECH value | PGT value |
|----------|-----------|-----------|
| rho_crit | 0.21 M_Pl^4 | m_T^2 M_Pl^2 |
| H_bounce | ~M_Pl | ~m_T M_Pl / M_Pl = m_T |
| t_bounce | ~t_Pl ~ 5x10^{-44} s | ~1/m_T |
| T_bounce | ~M_Pl ~ 10^{19} GeV | ~(m_T M_Pl)^{1/2} |
| G_torsion | ~G ~ M_Pl^{-2} | ~G |
| mu_5 (axial chemical potential) | ~G n_5 ~ M_Pl^3 / M_Pl^2 = M_Pl | ~m_T (if n_5 ~ m_T^3) |
| Bounce scale factor profile | a_b(1+4alpha^2 t^2)^{1/4} | Same form, different alpha |
| (J^5)^2 coupling | kappa^2/(1-3gamma^2 kappa xi^2) ~ G | Same |

---

## Scope of This Investigation

This Branch N investigation will:

1. Enumerate candidate mechanisms (File 02)
2. Define structural tests (File 03)
3. Build toy frameworks with actual numbers (File 04)
4. Perform cheap-kill OOM screening (File 05)
5. Identify the best Phase 2 target, if any (File 06)
6. Render a verdict (File 07)

No paper writing. No MCMC. Just physics.
