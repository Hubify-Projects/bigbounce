# Branch G Canonical Problem Statement — Freeze Log

**Frozen:** 2026-03-13
**Version:** v2 (final)
**Status:** LOCKED — changes only by versioned addendum
**File:** `08_branchG_canonical_problem_statement.md`

---

## What Is Defined (Pending Freeze)

The canonical problem statement defines:
- The exact microscopic action (same as Track B: EC + Holst + Dirac)
- The target object: one-loop gravitational effective action Γ_eff[e]
- The integration order: torsion elimination (exact) → fermion integration (one-loop) → heat-kernel expansion
- The key technical question: Approach A (Hubbard-Stratonovich) vs Approach B (direct loop expansion)
- The role of the Holst sector at one loop (Question 4)
- Three quantitative gates (G1: structural generation, G2: IR physicality, G3: DE viability)
- Six predeclared failure modes (FM-G1 through FM-G6)
- Renormalization strategy and scheme-independence requirements
- Four-phase computation sequence with internal Gate 0

---

## What Would Justify Reopening (After Freeze)

1. **Phase 1 reveals the one-loop operator has qualitatively different structure** than assumed (e.g., the torsion-eliminated Dirac operator has unexpected terms that change the heat-kernel analysis)

2. **Chattopadhyay (2023) already answers the central question** — either positively or negatively — making the computation redundant. In this case, Branch G may be reclassified as a literature review rather than a computation program.

3. **The Approach A / Approach B distinction** turns out to be more consequential than anticipated, requiring a fundamental change to the computation sequence

4. **A new result appears** showing that the Holst term contributes to the one-loop fermion determinant in a way not captured by background dependence alone

---

## What Does NOT Justify Reopening

- Results that fail a gate (that is the program working as designed)
- Difficulty of the heat-kernel calculation (expected)
- Desire to weaken success criteria after seeing partial results
- The Track B negative result (already incorporated)
- Desire to include two-loop or non-perturbative effects without a clear argument that one-loop is qualitatively wrong

---

## Change Log

| Date | Version | Change | Reason |
|------|---------|--------|--------|
| 2026-03-13 | v1 (draft) | Initial draft | 6 questions answered, modeled on Track B's frozen v3 |
| 2026-03-13 | v2 (frozen) | Pressure-test revisions | (1) Explicit Approach A/B scope control — Branch G v1 restricted to Approach B only. (2) Question 4 rewritten with three candidate γ-entry channels, novel Holst content criterion, and explicit kill logic. (3) Gate G1 upgraded to finite-γ gate — generic vacuum divergences cannot pass. (4) FM-G6 promoted to first-class Phase 1 early kill. (5) Bare-Λ caveat added. (6) Tetrad/metric language clarified. (7) Predeclared expectation added. |

---

## Branching Protocol

If a computation forces a genuine change to the problem definition:

1. Create `08_branchG_canonical_problem_statement_v2.md` (do not edit v1)
2. Document the specific result that forced the change
3. Update this change log
4. Reference both versions in downstream work

---

## Note on Approach A / B Labels

The labels "Approach A" (Hubbard-Stratonovich + saddle) and "Approach B" (strict one-loop) are **local to the Branch G canonical problem statement**. They do not correspond to "Possibility A" and "Possibility B" from the Track B canonical statement (which referred to symmetry structures of V_eff). The naming overlap is unfortunate but does not create ambiguity within either document.

---

## Relationship to Track B

Branch G is a **new program**, not a continuation of Track B. Key differences:

| Aspect | Track B | Branch G |
|--------|---------|----------|
| Target object | Condensate order parameter Φ = ⟨ψ̄iγ⁵ψ⟩ | Effective action Γ_eff[e] |
| Mechanism | NJL dynamical symmetry breaking | One-loop fermion determinant |
| Where γ enters | Four-fermion coupling structure | Background geometry + possible parity-odd sector |
| Most likely failure | Subcritical coupling (realized) | Pure renormalization only (FM-G1) |
| Computation tools | Gap equation, Fierz, V_eff | Heat kernel, Seeley-DeWitt coefficients |

Track B's negative result does not predict Branch G's outcome. The mechanisms are structurally independent.
