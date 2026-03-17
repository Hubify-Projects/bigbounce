# Foundation A — Phase 1 Verdict

**Date:** 2026-03-13
**Program:** Propagating Torsion in Poincare Gauge Theory
**Phase:** 1 (Ghost-free spectrum, mass analysis, cosmological relevance)

---

## VERDICT: FOUNDATION_A_SURVIVES_BUT_NO_DE

---

## Three Questions Answered

### Question 1: Does a ghost-free PGT parameter region exist?

**Answer: YES.**

Three clean single-mode ghost-free models exist within the quadratic PGT action (torsion-squared sector, curvature-squared set to zero):

| Model | Coupling | Propagating mode | Spin-parity | Ghost-free condition |
|-------|----------|-----------------|-------------|---------------------|
| A | t_2 > 0 | Torsion trace | 0+ (scalar) | Positive kinetic term |
| B | t_3 < 0 | Torsion axial | 0- (pseudoscalar) | Sign flip from epsilon contraction |
| C | t_1 < 0 | Torsion tensor | 2+ (tensor) | Positive kinetic term |

These results are confirmed by multiple independent analyses spanning four decades:
- Sezgin & van Nieuwenhuizen (1980): particle spectrum
- Yo & Nester (1999, 2002): Hamiltonian analysis
- Nikiforova, Randjbar-Daemi & Rubakov (2009): IR-modified gravity
- Karananas (2015): unitarity analysis
- Blagojevic & Cvetkovic (2018): complete Hamiltonian analysis
- Lin, Hobson & Sherrill (2019): computational scan

**Confidence: HIGH.** This is established physics, not a new claim.

### Question 2: What is the mass spectrum of the torsion modes?

**Answer: m = M_Pl / (4 sqrt(pi |t_I|))**

All three ghost-free models share the same functional form. The mass is determined by a single dimensionless coupling constant:

| |t_I| | Mass (eV) | Physical scale |
|-------|-----------|----------------|
| 1 | 3.4 x 10^26 | ~0.14 M_Pl |
| 10^10 | 3.4 x 10^21 | ~TeV |
| 10^50 | 3.4 x 10^1 | ~34 eV |
| 10^55 | 1.1 x 10^-1 | ~meV (DE scale) |
| 10^58 | 7.1 x 10^-3 | ~rho_Lambda^{1/4} |
| 10^118 | 3.4 x 10^-33 | ~H_0 |

**Confidence: HIGH.** Direct computation from the linearized PGT action.

### Question 3: Are any modes light enough to be cosmologically relevant?

**Answer: PARAMETRICALLY YES, but requires |t_I| >> 1 with no demonstrated naturalness mechanism.**

A cosmologically relevant torsion mass requires:
- m ~ meV (DE scale): |t_I| ~ 10^58
- m ~ H_0 (Hubble scale): |t_I| ~ 10^118

These are enormous dimensionless couplings. The mass hierarchy is not solved — it is transferred from "why is Lambda ~ 10^{-122} M_Pl^4?" to "why is |t_I| ~ 10^{58-118}?"

No symmetry or dynamical mechanism has been demonstrated that makes this natural within the quadratic PGT framework.

**Confidence: HIGH** for the parametric statement; **LOW** for naturalness assessment (requires Phase 2 investigation of shift symmetries).

---

## What Survives

1. **Ghost-free propagating torsion is real.** The PGT framework eliminates the algebraic-torsion wash-out (Lesson 1 from the closure program) by construction. Torsion is dynamical, propagating, and carries information into the IR.

2. **Model B (0- pseudoscalar axial torsion) is structurally promising.** It scores 5/6 on the decision-rule assessment:
   - DR1 (survives reduction): PASS
   - DR2 (scale naturalness): OPEN (shift symmetry conceivable)
   - DR3 (distinctive observable): PROMISING (GW birefringence, spin-dependent force)
   - DR4 (clean failure): PASS
   - Nonlinear safety: OK (no Boulware-Deser ghost)
   - Parity connection: STRONG (axial current = ECH Holst coupling)

3. **The PGT 0- mode connects to the broader program.** Its axial-current coupling is the same structure that appears in the ECH Holst term. Its parity-odd nature connects to the birefringence program. If a photon coupling can be derived (not assumed), it would produce a non-generic birefringence prediction.

## What Does NOT Survive

1. **No dark energy from first principles.** The torsion mass is a free parameter, not a prediction. Setting it to m ~ H_0 requires fine-tuning comparable to the CC problem itself.

2. **Model C (2+ tensor) is fragile.** Massive spin-2 fields generically develop the Boulware-Deser ghost at the nonlinear level. Model C is linearized-ghost-free but unreliable beyond perturbation theory.

3. **Model A (0+ scalar) is generic.** It has no parity connection, no mass protection, and its phenomenology (spin-independent fifth force) is indistinguishable from a generic scalar field added to GR.

4. **The hierarchy problem persists.** PGT does not solve the cosmological constant problem; it provides a framework in which the problem can be reformulated as a torsion-mass hierarchy.

---

## Comparison with Closure Program Lessons

| Lesson from closures | Foundation A status |
|---------------------|---------------------|
| L1: Algebraic torsion washes out | **RESOLVED** — torsion propagates in PGT |
| L2: Fixed gamma leaves no IR fingerprint | **RESOLVED** — torsion mass is a new IR parameter |
| L3: Dynamical gamma reduces to ALP | **PARTIALLY RESOLVED** — 0- torsion is geometric, not generic ALP, IF non-topological structure survives reduction (untested) |
| L4: Parity alone is not a mechanism | **UNCHANGED** — still true; need derived coupling |
| L5: No scale protection in minimal model | **UNCHANGED** — still true; need shift symmetry |

Foundation A resolves the most basic structural failure (L1, L2) but does not address the deeper issues (L4, L5).

---

## Phase 2 Roadmap

If Foundation A is pursued further, the critical tests are:

1. **Shift symmetry investigation** (highest priority): Can a PGT extension set t_3 = 0 at tree level via a symmetry? Candidates: conformal PGT, Weyl-Cartan geometry.

2. **Unitarity bounds on |t_I|**: Do tree-level scattering amplitudes constrain |t_I| < O(1)? If so, light masses are excluded.

3. **Radiative stability**: Does the one-loop graviton correction generate delta m^2 ~ M_Pl^2/(16 pi^2) regardless of tree-level mass?

4. **Reduced action comparison**: Does the PGT 0- mode retain non-generic structure after integrating out all other fields, or does it reduce to GR + generic pseudoscalar?

5. **FRW cosmology**: What equation of state w(z) does a massive 0- torsion mode produce in an expanding universe?

**Estimated effort for Phase 2:** 2-4 weeks focused work, primarily literature review + one-loop calculation.

---

## Files Produced in Phase 1

| File | Content |
|------|---------|
| 01_pgt_action_definition.md | General quadratic PGT action, notation, parameter counting |
| 02_parameter_space.md | Ghost-free conditions from literature, mass hierarchy analysis |
| 03_mode_decomposition.md | Spin-parity decomposition, mode propagation in each model |
| 04_mass_spectrum_calculation.md | Explicit mass formulas, spectrum table, hierarchy comparison |
| 05_cosmological_relevance.md | Scenario analysis, shift-symmetry argument, signatures |
| 06_failure_modes.md | Gate definitions, closure conditions, Phase 2 test plan |
| pgt_mode_analysis.ipynb | Computational verification of all mass formulas, visualizations |
| fig_pgt_parameter_space.png | Three-panel figure: ghost-free regions, mass spectrum, hierarchy |
| phase1_verdict.md | This document |
