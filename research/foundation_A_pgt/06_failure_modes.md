# 06 — Failure Modes and Closure Conditions

**Date:** 2026-03-13
**Purpose:** Explicitly define the conditions under which Foundation A must be closed, partially closed, or left open for further investigation.
**Status:** Gate definitions (predeclared before conclusions are drawn)

---

## 1. Decision Framework

Following the methodology established in the closure program (DR4: "fails cleanly if it doesn't work"), we define explicit gates for Foundation A.

Foundation A has three nested questions:
1. Do ghost-free PGT models exist? (Gate 1)
2. Can any torsion mode be cosmologically light? (Gate 2)
3. Can a light torsion mode drive dark energy? (Gate 3)

---

## 2. Gate Definitions

### Gate 1: Ghost Freedom

**Question:** Does a ghost-free, tachyon-free propagating torsion theory exist within quadratic PGT?

**Pass condition:** At least one parameter choice (t_I, r_I) yields:
- Positive-definite kinetic matrix for all propagating modes
- Non-negative mass-squared for all propagating modes
- No higher-derivative instabilities

**Fail condition:** No parameter choice satisfies all three conditions simultaneously.

**Current status: GATE 1 PASSED.**

Evidence: Multiple independent analyses (Sezgin-van Nieuwenhuizen 1980; Yo-Nester 1999, 2002; Nikiforova et al. 2009; Karananas 2015; Blagojevic-Cvetkovic 2018; Lin-Hobson-Sherrill 2019) confirm ghost-free models exist. Three clean single-mode models identified: scalar 0+ (t_2 > 0), pseudoscalar 0- (t_3 < 0), tensor 2+ (t_1 < 0).

### Gate 2: Light Mass Viability

**Question:** Can any ghost-free torsion mode have a mass parametrically below the Planck scale, and specifically at or below the dark energy scale?

**Pass condition:** There exists a mechanism (symmetry, dynamical, or otherwise) that makes |t_I| >> 1 natural, stable under quantum corrections, and consistent with all observational bounds.

**Partial pass condition:** The mass CAN be small parametrically (no obstruction), but naturalness requires a protecting mechanism not yet demonstrated.

**Fail condition:** A no-go theorem or structural obstruction proves that |t_I| >> 1 is inconsistent with PGT (e.g., unitarity bounds force |t_I| < O(1), or radiative corrections drive the mass to the Planck scale regardless of the tree-level value).

**Current status: GATE 2 PARTIAL PASS.**

No obstruction to light masses has been found. The mass formula m = M_Pl/sqrt(|t_I|) allows any mass. But no mechanism has been demonstrated that makes |t_I| >> 1 natural. The situation is analogous to quintessence: the mass is a free parameter, not a prediction.

### Gate 3: Dark Energy Mechanism

**Question:** Can a light propagating torsion mode produce w = -1 (or w close to -1) dark energy dynamics?

**Pass condition:** An explicit model exists in which:
- The torsion mode has a potential V(chi) with a minimum at V(chi_0) = rho_Lambda
- The mode is frozen or slowly rolling today (w ~ -1)
- The mass/potential is protected against radiative corrections
- The model produces at least one prediction distinguishable from generic quintessence (DR3)

**Fail condition:** Any of:
- The torsion mode's cosmological dynamics inevitably give w != -1 (e.g., w = 0 from oscillation, w = +1 from kinetic domination)
- The potential V(chi) cannot have a minimum at the required scale without fine-tuning equivalent to the CC problem
- The model reduces to generic quintessence with no distinctive geometric signature (DR3 failure)

**Current status: GATE 3 NOT YET TESTED.**

This gate requires Phase 2 work: constructing an explicit torsion dark energy model and testing it against Gates 1-3 simultaneously.

---

## 3. Specific Closure Conditions

Foundation A **closes completely** if ANY of the following are established:

| Closure condition | What it means | How to test |
|-------------------|---------------|-------------|
| C1: All ghost-free models have m > M_Pl | No propagating mode below Planck scale | Already excluded — masses are parametric |
| C2: Unitarity bounds force |t_I| < O(1) | Light masses inconsistent with unitarity | Check tree-level unitarity bounds on t_I |
| C3: Radiative corrections destabilize light mass | Loop corrections drive m -> M_Pl regardless of tree-level | Compute one-loop mass correction to torsion modes |
| C4: Torsion dynamics give w = +1 or w = 0 only | No dark energy equation of state achievable | Study FRW cosmology with massive torsion |
| C5: 0- mode reduces to generic ALP after reduction | No geometric fingerprint survives | Compare reduced PGT action with GR + ALP |
| C6: Boulware-Deser ghost kills 2+ at nonlinear level AND 0+ and 0- also fail | All modes unviable | Nonlinear analysis of each mode |

Foundation A **survives but does not deliver dark energy** if:

| Condition | What it means |
|-----------|---------------|
| S1: Ghost-free models exist but all have m > eV | Torsion propagates but is too heavy for cosmology |
| S2: Light mass is possible but no protecting symmetry found | Generic quintessence, no geometric advantage |
| S3: Torsion mode produces w != -1 only | Modified dynamics, not CC |

Foundation A **survives with dark energy potential** if:

| Condition | What it means |
|-----------|---------------|
| V1: Ghost-free, light, w ~ -1 torsion model exists | Candidate dark energy theory |
| V2: The model has a distinctive prediction beyond generic quintessence | DR3 satisfied |

---

## 4. Assessment Against Current Evidence

| Gate | Status | Evidence |
|------|--------|----------|
| Gate 1 (ghost freedom) | **PASSED** | Literature consensus |
| Gate 2 (light mass) | **PARTIAL PASS** | No obstruction found; no mechanism demonstrated |
| Gate 3 (dark energy) | **NOT TESTED** | Requires Phase 2 |

| Closure condition | Status |
|-------------------|--------|
| C1 | Excluded (masses are parametric) |
| C2 | Not tested (no unitarity bound analysis for large |t_I|) |
| C3 | Not tested (no loop correction computed) |
| C4 | Not tested (no PGT FRW cosmology computed) |
| C5 | Not tested (reduced action comparison needed) |
| C6 | Not tested (nonlinear analysis needed) |

**No closure condition has been triggered. Foundation A remains open.**

---

## 5. Phase 2 Required Tests

If Foundation A is to progress, Phase 2 must address:

1. **C2 test:** Compute tree-level unitarity bounds on |t_I| from graviton-torsion scattering. Does unitarity force |t_I| < O(1)?

2. **C3 test:** Compute the one-loop correction to the torsion mass. Specifically, does the graviton loop generate delta m^2 ~ M_Pl^2 / (16 pi^2) regardless of the tree-level mass? If so, light masses are radiatively unstable (as for the electroweak hierarchy problem).

3. **C5 test:** Write down the reduced PGT action after integrating out all non-torsion degrees of freedom. Does the surviving 0- mode retain any coupling structure not reproducible by GR + generic pseudoscalar?

4. **Shift symmetry investigation:** Is there a natural PGT extension in which the axial torsion mass vanishes at tree level due to a symmetry? Candidates: conformal PGT, Weyl-Cartan geometry, metric-affine extensions.

5. **FRW cosmology:** Solve the modified Friedmann equations with a massive 0- torsion mode in an expanding universe. What is the equation of state w(z)?

---

## 6. Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| C2 triggers (unitarity kills large t_I) | Moderate | Fatal | Test first — this is the cheapest check |
| C3 triggers (radiative instability) | Moderate-High | Fatal | One-loop calculation |
| C5 triggers (reduces to ALP) | Low-Moderate | Fatal | Careful reduction analysis |
| C4 triggers (wrong w) | Low | Fatal | FRW solution |
| Phase 2 shows shift symmetry impossible in PGT | Moderate | Redirects to Foundation B | Continue to Foundation B |
| All gates pass but no distinctive prediction | Moderate | Downgrades to generic quintessence | Weak outcome but not failure |

**Highest-priority test for Phase 2:** C2 (unitarity bounds on |t_I|). This is the cheapest computation and could immediately close or clear the path.
