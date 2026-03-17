# Foundation B Phase 2 — Results

**Date:** 2026-03-14

---

## Verdict: PARTIAL_PROGRESS_BUT_STILL_GENERIC

---

## Executive Summary

The Nieh-Yan 4-form IS non-topological in metric-affine gravity. The
mass-coupling lock IS broken in all viable toy actions. But the coupling
structure reduces to a generic ALP after field elimination. No distinctive
geometric fingerprint survives to low energies.

Model B is not closed (it works as a dark-energy mechanism), but it does
not achieve the original goal of Foundation B: a DISTINCTIVELY geometric
dark-energy theory with predictions beyond generic ALP phenomenology.

---

## Key Results

### 1. Nieh-Yan Identity in MAG (PASSED)

The standard Nieh-Yan identity is MODIFIED in metric-affine gravity:

```
N_4 = d(e^I wedge T_I) + Q_{AB} wedge e^B wedge T^A
```

where Q_{AB} is the non-metricity 1-form. The correction term
Q_{AB} wedge e^B wedge T^A is:
- Algebraic (holds off shell)
- Bilinear in non-metricity and torsion
- Vanishes in RC (Q = 0) or when T = 0

**N_4 is NOT exact in MAG.** This was the Phase 2 first-check, and it PASSED.

### 2. Topological-Shift Duality (DISCOVERED)

A structural dilemma was identified: for a pseudoscalar theta coupled
linearly to a geometric 4-form Omega_4:

- **Topological Omega_4:** Shift symmetry preserved (mass protected).
  No local geometric content. Route T1.
- **Non-topological Omega_4:** Shift symmetry broken (mass unprotected).
  Local geometric content present. But mass naturalness is lost.

This is a general theorem, not specific to the Nieh-Yan form.
It represents a STRUCTURAL OBSTRUCTION to the "geometric ALP" idea:
you cannot simultaneously have a shift-symmetry-protected mass AND
non-topological geometric content from a linear pseudoscalar coupling.

### 3. Lock Analysis (UNLOCKED)

Four toy actions were analyzed. Results:

| Action | Lock | Mass natural? | DR3? |
|--------|------|---------------|------|
| I: theta-N_4, no potential | Env. unlocked | No | Marginal |
| II: theta-N_4 + instanton | **Fully unlocked** | **Yes** | Weak |
| III: d(theta) derivative | **Fully unlocked** | **Yes** | Marginal |
| IV: composite | Likely locked | Unknown | Unknown |

Toy Actions II and III achieve the full ALP architecture with
technically natural mass (from an instanton potential that breaks
shift symmetry softly, independent of the geometric sector).

### 4. Equivalence to T1 (PARTIALLY DISTINCT)

Model B is NOT equivalent to Route T1:
- T1 has only a derivative coupling (d(theta) to axial current).
- Model B has an ADDITIONAL non-derivative term from the Q*T
  cross-coupling, producing an environment-dependent mass.
- In cosmological backgrounds (T_0 = 0), Model B = T1.
- In dense environments, Model B differs from T1.

The distinction is real but phenomenologically weak.

### 5. Distinctive Fingerprint (DR3 FAILS)

After torsion and non-metricity elimination, all geometric couplings
reduce to standard ALP-matter couplings:
- d(theta) wedge e wedge T -> ALP-fermion derivative coupling
- d(theta) wedge Q wedge e^2 -> ALP-conformal coupling

No candidate fingerprint (environment-dependent mass, dual couplings,
universality) is uniquely diagnostic of geometric origin. A generic
ALP with appropriately chosen parameters can reproduce all predictions.

---

## What Was Learned

### Positive results

1. **The Nieh-Yan form is non-topological in MAG.** This is a clean
   mathematical result that is new (to our analysis) and correct.

2. **The mass-coupling lock CAN be broken** by the ALP architecture,
   confirming Phase 1's finding in concrete toy actions.

3. **The Topological-Shift Duality** is a new structural insight:
   mass protection and geometric content are mutually exclusive for
   linear pseudoscalar couplings. This constrains ALL future attempts
   to build geometric pseudoscalar dark energy.

4. **An environment-dependent mass** from the Q*T cross-term is an
   interesting (if not unique) feature of the MAG pseudoscalar.

### Negative results

1. **DR3 failure:** No distinctive geometric fingerprint survives
   field elimination. The low-energy EFT is a generic ALP.

2. **The Topological-Shift Duality blocks** the most natural route
   to geometric ALP dark energy. Any linear coupling that provides
   geometric content also breaks the shift symmetry, and vice versa.

3. **The cosmological background has T = 0,** which means the
   non-topological correction to N_4 vanishes in cosmology. Model B
   equals T1 in the cosmological background.

---

## Implications for the Research Program

### Foundation B (Nieh-Yan route): NOT CLOSED but INSUFFICIENT

Model B works as a dark-energy mechanism but fails DR3. It does not
provide a publishable advance over generic ALP dark energy.

The Nieh-Yan route should be set aside unless new ideas emerge for
producing a distinctive geometric fingerprint.

### The Topological-Shift Duality constrains future exploration

Any future attempt to build geometric pseudoscalar dark energy must
contend with this duality. The possible escape routes are:

1. **Non-linear couplings:** V(theta) * Omega_4 instead of theta * Omega_4.
   These can preserve shift symmetry (in V) while using non-topological
   Omega_4. But after field elimination, they produce scalar-tensor
   theories, not distinctive ALP phenomenology.

2. **Higher-derivative couplings:** (d theta)^2 * Omega_0, where Omega_0
   is a geometric scalar. These are Horndeski/Galileon-type theories
   and have their own phenomenology. Worth investigating but outside
   the ALP paradigm.

3. **Non-pseudoscalar modes:** The lock-breaking analysis applied to
   scalar (0+) or tensor (2+) torsion modes, where the shift-symmetry
   constraint does not apply. The mass naturalness question changes
   (no shift symmetry for scalars — need a different protection
   mechanism).

4. **Strong-coupling dynamics:** Torsion condensation producing composite
   states with emergent symmetries. Beyond perturbative control.

### Recommended next steps

1. **Assess Foundation B alternative:** Check whether derivative-coupling
   Horndeski-type theories with geometric origin (option 2 above) can
   break the lock AND provide distinctive predictions. This is a
   different paradigm (not ALP) and might avoid the Topological-Shift
   Duality.

2. **Return to Foundation A:** The PGT scalar (0+) mode was not
   analyzed for lock-breaking. It does not have shift symmetry, so
   the duality does not apply. The mass naturalness question is
   different (possibly addressed by environmental mechanisms or
   dimensional transmutation — Phase 1 ideas #2 and #3).

3. **Investigate the environmental mass mechanism** (Phase 1 idea #3):
   A torsion mode with mass m^2(R) dependent on the local curvature R
   could be cosmologically light and locally heavy. This does not
   require shift symmetry and avoids the duality.

---

## Files Produced

```
phase2/
  01_phase2_problem_statement.md     — Precise questions and success criteria
  02_nieh_yan_mag_analysis.md        — Core calculation: N_4 in MAG
  03_equivalence_test_vs_T1.md       — Comparison with closed Route T1
  04_toy_geometric_alp_actions.md    — Four toy actions with analysis
  05_phase2_symbolic_checks.ipynb    — SymPy lock verification
  06_distinctive_fingerprint_test.md — DR3 assessment
  phase2_results.md                  — This file
```

---

## One-Line Summary

**The Nieh-Yan form is non-topological in MAG and the mass-coupling
lock breaks, but a new structural obstruction (Topological-Shift Duality)
prevents any linear pseudoscalar coupling from simultaneously achieving
mass protection and distinctive geometric content.**
