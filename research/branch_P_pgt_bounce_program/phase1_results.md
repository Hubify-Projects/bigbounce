# Branch P Phase 1 Results: PGT Lower-Scale Bounce Phenomenology

**Date:** 2026-03-16

---

## Verdict: BRANCH_P_MIXED

---

## What Was Done

A comprehensive survey of ALL surviving observable channels for the
PGT lower-scale bounce, building on the 13 structural barriers
established in Branches A--O.

Eight observable channels were assessed:

| # | Channel | Status |
|---|---------|--------|
| 1 | Vacuum GW background | DEAD (10^{17} gap, Branch M) |
| 2a | Torsion oscillation GW | DEAD ((m_T/M_Pl)^3) |
| 2b | Parametric resonance | DEAD (too brief) |
| 2c | Phase transition GW | Alive but NOT bounce-specific |
| 2d | Pre-bounce contraction GW | Alive but NOT PGT-specific |
| 3 | Scalar perturbations | TRANSPARENT (T(k) = 1) |
| 4 | **Torsion decay / reheating** | **ALIVE (gated on energy fraction)** |
| 5 | **Dark radiation (N_eff)** | **ALIVE (gated on energy fraction)** |
| 6a | Graviton N_eff | DEAD ((m_T/M_Pl)^2) |
| 6b | Spectral distortions | Conditional (narrow window) |
| 7 | Consistency relations | Conditional (requires Channel 4/5) |
| 8 | Modified expansion history | DEAD (exponentially small) |

---

## Strongest Positive Channel

**Torsion relic cosmology (Channels 4 + 5).**

The propagating torsion mode in PGT Sector II is a massive pseudoscalar
(mass m_T). After the bounce, it oscillates and decays gravitationally
with lifetime tau ~ M_Pl^4 / m_T^5.

If the torsion carries O(1) of the bounce energy (Scenario A), this
creates a standard "cosmological moduli problem":

- **m_T < ~3 x 10^9 GeV:** torsion decays after BBN, EXCLUDED
- **m_T ~ 10^9 -- 10^{10} GeV:** marginal, constrained by BBN + N_eff
- **m_T > ~10^{10} GeV:** torsion decays well before BBN, safe

This would give a concrete, data-facing constraint on the PGT
parameter space.

If the torsion carries only (m_T/M_Pl)^2 of the bounce energy
(Scenario B), no meaningful constraint exists and the program
is effectively closed.

**Which scenario is correct is the single most important
question for PGT bounce phenomenology.**

---

## Why MIXED (Not PROMISING or WEAK)

### Not PROMISING because:

1. The strongest channel (torsion relic) has not been confirmed.
   The torsion energy fraction is unknown and could be sub-dominant
   (Scenario B), killing the last surviving channel.

2. Even in the best case (Scenario A), the constraint is an EXCLUSION
   (lower bound on m_T), not a DETECTION. There is no positive signal
   to discover -- only parameter regions to rule out.

3. The PGT bounce still predicts nothing for CMB observables (n_s, r,
   f_NL). It cannot compete with inflation on predictive power.

4. The GW background is permanently undetectable (10^{17} gap).

### Not WEAK because:

1. The torsion relic channel is genuinely new: it has not been worked
   out in the literature for PGT cosmology.

2. If Scenario A holds, the BBN/CMB constraint is sharp and publishable.

3. The torsion relic is PGT-SPECIFIC: no other bounce model (EC, LQC,
   ekpyrotic) has a propagating torsion mode with these properties.

4. The calculation is tractable (coupled ODEs, analytically solvable).

---

## Does the Program Have a Real Positive Center?

**Conditionally yes.**

If the torsion energy fraction is O(1) (Scenario A), then PGT bounce
phenomenology has a genuine positive center:

> "The PGT bounce in ghost-free Sector II produces a massive
> torsion relic that must decay before BBN, requiring m_T > ~10^9 GeV.
> This is a concrete, data-facing constraint on the bounce scale
> from cosmological observations."

This would be:
- Novel (not in the literature)
- PGT-specific (distinguishes PGT from EC, LQC, generic bounces)
- Observationally grounded (BBN + CMB data)
- Part of a complete characterization (combined with the 13 barriers
  and the GW spectrum from Branch M)

If Scenario B holds instead, the positive center collapses and the
verdict should be downgraded to BRANCH_P_WEAK.

---

## The 13 + 0 Barrier Count

Branch P does NOT add a new structural barrier. Instead, it identifies
a potential ESCAPE from the existing barriers:

- The torsion relic channel is NOT blocked by any of the 13 barriers
- It does not rely on vacuum amplification (Barrier 12)
- It does not require bounce-specific baryogenesis (Barrier 13)
- It does not require scale separation (Barrier 5)
- It is a DIRECT consequence of the propagating torsion mode

This is why it is the most promising remaining channel.

---

## Complete Branch Status (A--P)

| Branch | Sector | Verdict | Root cause |
|--------|--------|---------|-----------|
| A--G | Direct bounce -> DE | CLOSED | 7 barriers |
| H | Tensor spectrum/parity | CLOSED | Amplitude + parity-even |
| I | Bounce-compatible DE | WEAK | Scale separation |
| J | State selection | CLOSED | Liouville |
| K | Scalar perturbations | GENERIC | Time-reversal symmetry |
| L | UV-IR bridge | MIXED | Specificity dilemma |
| M | PGT GW spectrum | GENERIC | Vacuum amplification ceiling |
| N | Baryogenesis/relics | CLOSED | Gravitational democracy |
| O | Hidden-sector vacuum | CLOSED | Bounce-vacuum decoupling |
| **P** | **PGT bounce program** | **MIXED** | **Torsion relic: TBD** |

---

## Exact Next Move

**Calculate the torsion energy fraction at the PGT Sector II bounce.**

Specifically:

1. Write the coupled Friedmann + pseudoscalar torsion field equations
   for homogeneous FRW in PGT Sector II

2. Determine the self-consistent bounce solution: what is phi(0) at
   the bounce? Is it ~ M_Pl (Scenario A) or ~ m_T (Scenario B)?

3. If Scenario A: compute T_decay(m_T), Delta N_eff(m_T), and the
   BBN exclusion boundary

4. If Scenario B: document the closure and downgrade to BRANCH_P_WEAK

**Quick kills to check first:**
- Does the PGT field equation force phi = 0 on FRW? (If yes: Scenario B wins trivially)
- Does phi redshift as matter or radiation? (If radiation: no growth, weak constraint)
- Is the answer already in the literature (Yo, Nester, Baekler)?

**Estimated scope:** One focused calculation session. The coupled ODEs
are 2nd-order with known background. Analytic estimates should determine
which scenario applies.

---

## Summary

| Item | Result |
|------|--------|
| Observable channels surveyed | 8 |
| Channels alive (bounce-specific) | 2 (torsion decay, dark radiation) |
| Channels alive (not bounce-specific) | 2 (phase transition GW, pre-bounce scalars) |
| Channels dead | 4 (vacuum GW, parametric resonance, graviton N_eff, modified expansion) |
| Strongest channel | Torsion relic cosmology |
| Gating question | Torsion energy fraction at bounce: O(1) or (m_T/M_Pl)^2? |
| PGT-distinctive prediction? | YES if Scenario A, NO if Scenario B |
| New barrier? | None (this is a potential escape, not a new block) |
| Phase 2 needed? | YES: torsion energy fraction calculation |
| Branch P verdict | **BRANCH_P_MIXED** |
| Conditional upgrade | -> PROMISING if torsion energy fraction ~ O(1) |
| Conditional downgrade | -> WEAK if torsion energy fraction ~ (m_T/M_Pl)^2 |
