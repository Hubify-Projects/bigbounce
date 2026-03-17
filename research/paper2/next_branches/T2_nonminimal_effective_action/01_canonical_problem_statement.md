# Branch T2 — Canonical Problem Statement: Non-Minimal Effective-Action Route

**Version:** v1 (DRAFT — NOT FROZEN)
**Date:** 2026-03-13
**Status:** CONDITIONAL — opens only after T1 results are available
**Prerequisite:** Track B closed, Branch G v1 closed, T1 assessed

---

## Motivation

Branch G v1 showed that the strict one-loop fermion determinant in the minimal EC+Holst+Dirac model is γ-independent. However, γ-dependent quantum corrections CAN appear through:

1. **Graviton loops with fermion currents** (Shapiro & Teixeira 2014): γ enters through graviton vertices after torsion elimination. Fermions are external currents.
2. **Two-loop / Approach A**: The four-fermion interaction S_4f contributes as a vertex at two loops. Hubbard-Stratonovich resummation (Approach A) may reintroduce γ-dependent structure.
3. **Non-minimal couplings**: Additional torsion-matter interactions beyond minimal coupling (e.g., non-minimal curvature-fermion terms, Nieh-Yan coupling to matter).

T2 targets the smallest controlled extension beyond the dead minimal route that could generate nontrivial finite-γ content.

**Important:** This branch should NOT be opened speculatively. It should only be pursued if T1 results provide structural guidance about which non-minimal terms are worth computing, OR if a specific literature result motivates a concrete computation.

---

## The Central Question

> Does a controlled non-minimal extension of the EC+Holst+Dirac effective action, at a specified approximation order beyond strict one-loop, produce a finite-γ vacuum-like term that satisfies the novel Holst content criterion and is not merely a standard renormalization artifact?

---

## Candidate Extensions (To Be Selected After T1)

### Candidate A: Graviton one-loop (Shapiro-Teixeira approach)
- Quantize the metric fluctuations h_μν in the presence of external fermion currents modified by γ-dependent torsion elimination
- γ enters through modified graviton vertices
- Much harder computation than Branch G v1
- Already has γ-dependent divergences in the literature

### Candidate B: Two-loop fermion effective action
- S_4f vertices contribute at two loops
- γ enters through the four-fermion vertex
- Combinatorially complex
- May not yield anything IR-physical

### Candidate C: Non-minimal curvature-fermion couplings
- Add ξ R ψ̄ψ or similar non-minimal terms to the starting action
- Breaks the minimal model assumption
- Must be theoretically motivated (not arbitrary)

### Candidate D: Insights from T1
- If T1 reveals specific θ-dependent structures, T2 could test whether analogous structures appear in the effective action with constant γ + non-minimal couplings

**Selection criterion:** Choose the candidate with the smallest departure from the minimal model that is still structurally different from the closed branches.

---

## Gate Structure

### Gate T2-1: Nontrivial finite-γ content
The computed effective action contains at least one finite or regulator-robust term whose existence depends nontrivially on finite γ and disappears or changes qualitatively as γ → ∞.

### Gate T2-2: IR physicality
The term survives as R → 0 and is scheme-robust in existence/sign.

### Gate T2-3: Dark energy viability
Positive vacuum energy, |1 + w| < 10⁻², or at least a parity-odd observable prediction.

---

## Predeclared Failure Modes

| Code | Failure mode |
|------|-------------|
| FM-T2-1 | Only ordinary renormalization (no novel finite-γ content) |
| FM-T2-2 | Novelty only on special backgrounds (not general) |
| FM-T2-3 | No IR persistence (curvature-local terms only) |
| FM-T2-4 | Wrong-sign vacuum structure |
| FM-T2-5 | Unstable or unphysical effective sector |
| FM-T2-6 | Result depends on arbitrary non-minimal choices with no predictive power |
| FM-T2-7 | Computation intractable at the required order |

---

## Why T2 Waits for T1

1. T1 explores the most structurally motivated extension (dynamical γ). If T1 finds new physics, T2 may become unnecessary. If T1 closes, its closure may reveal which non-minimal terms are most worth computing.
2. Without input from T1, the choice of "which non-minimal extension" is arbitrary. T2 should not be a fishing expedition.
3. If T1 shows that the dynamical Immirzi field reduces to standard ALP physics, then T2 should focus on non-ALP extensions (Candidates A or B).

---

## Estimated Difficulty

| Candidate | Difficulty | Compute | Likelihood of new physics |
|-----------|-----------|---------|--------------------------|
| A (graviton loop) | Very high | Symbolic + numerical | 15% |
| B (two-loop fermion) | High | Symbolic | 10% |
| C (non-minimal coupling) | Medium | Symbolic | 5% (arbitrary) |
| D (T1-informed) | Depends on T1 | Depends | Unknown |

---

## Closure Criteria

T2 closes if:
1. All candidate extensions fail their respective Gate T2-1, OR
2. The computation is assessed as intractable at the required order (FM-T2-7), OR
3. T1 results make T2 unnecessary (T1 opens a viable route), OR
4. After 8 weeks of work, no concrete candidate has been selected (scope failure).

---

## Open Questions

1. Which candidate to pursue? (Awaits T1 results)
2. Is Candidate A (graviton loop) tractable? The Shapiro-Teixeira computation is already published for divergences; what about finite parts?
3. Is there a way to distinguish "genuine non-minimal" from "arbitrary addition"?

These must be answered before this statement can be frozen.
