# Canonical Problem Statement — Freeze Log

**Frozen:** 2026-03-13
**Version:** v3 (final)
**File:** `06_canonical_problem_statement.md`
**Status:** LOCKED — changes only by versioned addendum

---

## What Is Frozen

The canonical problem statement defines:
- The exact microscopic action (EC + Holst + Dirac, γ fixed)
- The integration order and approximation stack
- The order parameter Φ = ⟨ψ̄ iγ⁵ψ⟩ as primary channel
- The symmetry logic (Possibility A vs B, to be resolved by Computation 3)
- Three quantitative gates (existence, persistence, vacuum-like stress-energy)
- Success/failure criteria with predeclared thresholds
- Renormalization strategy and scheme-independence requirements

These definitions are the reference point for all downstream computations. Results are evaluated against this memo, not against later prose.

---

## What Would Justify Reopening

The memo should be reopened (as a new version, not an edit) only if:

1. **Computation 2 reveals the coupling structure is qualitatively different** from the G_V / G_A / G_VA form assumed here (e.g., additional independent couplings from tensor torsion components)

2. **Computation 3 (Fierz analysis) shows the pseudoscalar channel is not the leading attractive channel**, requiring a change of primary order parameter

3. **A literature result appears that invalidates the starting action** (e.g., proof that the Holst term does not contribute to the reduced four-fermion sector, or that boundary terms cannot be neglected)

4. **The approximation stack turns out to be insufficient** in a way that changes the gate definitions (e.g., if one-loop is qualitatively wrong and two-loop is needed for Gate 1)

---

## What Does NOT Justify Reopening

- Numerical results that fail a gate (that is the memo working as designed)
- Difficulty of the computation (that is expected)
- Desire to weaken success criteria after seeing partial results
- New phenomenological motivations unrelated to the three gates

---

## Change Log

| Date | Version | Change | Reason |
|------|---------|--------|--------|
| 2026-03-13 | v1 | Initial draft | 7 questions answered |
| 2026-03-13 | v2 | Incorporated first pressure-test (9 points) | Symmetry overclaim, tetrad status, approximation labels, competing channels, gate precision, regulator invariants, counterterms, skeptic box |
| 2026-03-13 | v3 (frozen) | Line-by-line red-team revisions (17 fixes) | Hessian unification, channel truncation qualifiers, hypothetical language in Possibility A, ΔV sign separation, scheme-independence scope, a_transition definition, auxiliary-field status, w-failure modes |

---

## Branching Protocol

If a computation forces a genuine change to the problem definition:

1. Create `06_canonical_problem_statement_v4.md` (do not edit v3)
2. Document the specific computation result that forced the change
3. Update this change log
4. Reference both versions in downstream work so the reasoning trail is preserved
