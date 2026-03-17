# Paper 1.2 — Status Decision Memo

**Date:** 2026-03-13
**Author:** Houston Golden (via Claude session)
**Document:** `paper_1_2_draft.tex` (v1.2.0-draft, 178 KiB compiled)

---

## Question: Is Paper 1.2 publishable?

### Option 1: Publishable reframing paper
### Option 2: Conceptual bridge manuscript pending stronger next-gen model

**Assessment: Option 2 — conceptual bridge, not yet publishable.**

---

## Strongest contribution

The **closure program + structural lessons** are the paper's primary scientific contribution. No prior work has:
- Systematically tested and closed four minimal first-principles routes to geometric dark energy
- Extracted five structural lessons explaining why the minimal model class fails
- Formulated four concrete decision rules (DR1–DR4) for evaluating successor models
- Produced a claims classification table distinguishing derived/phenomenological/retired claims

This is genuine negative-results science with landscape-mapping value.

## Biggest weakness

**The paper has no first-principles result.** Every positive result is phenomenological:
- The scaling ansatz assumes w = −1 rather than deriving it
- The MCMC fits are standard ΛCDM+ΔNeff analyses available to anyone
- The birefringence consistency is not a prediction (no photon coupling)
- The galaxy spin signal is empirical (order-of-magnitude gap unresolved)
- The fine-tuning reduction is parametric, not mechanistic

A paper whose main message is "here is a phenomenological framework that works, but we can't derive its central assumption" needs either (a) a strong positive result elsewhere or (b) a compelling reason why the negative results alone are worth publishing. The standalone closure paper (supplement_negative_results.tex) already handles (b). Paper 1.2 tries to do both positive and negative together, and the positive side is thin.

## What prevents submission

1. **Part I is a description of a model, not a derivation.** The ECH framework section presents established equations; the scaling ansatz is parameterized, not derived. A referee would ask: "What is the new physics result in Part I?" The honest answer is: there isn't one — it's a well-motivated parameterization.

2. **Part III has no new calculation.** The candidate foundations are surveyed but not tested. Foundation A, B, and C each have a "first check" that hasn't been performed. Until at least one first check is executed, Part III is a research proposal, not a research result.

3. **The Related Work section positions the framework relative to others, but the framework itself has no advantage over generic ΛCDM+ΔNeff** in terms of data fits. The scaling argument is the unique contribution, but it's an ansatz, not a mechanism.

4. **Overlap with the closure paper.** Part II of Paper 1.2 substantially overlaps with the standalone closure paper. Publishing both creates a redundancy problem. Either Paper 1.2 must add significant new content beyond the closures, or the closure paper should be the primary publication.

## Most impactful single improvement

**Execute Foundation A first check: map the ghost-free PGT parameter subspace and compute the torsion mass spectrum.**

If a ghost-free, cosmologically light torsion mode exists:
- Part III becomes a concrete result, not a proposal
- The paper's narrative becomes: "minimal model fails → structural reason → propagating torsion resolves it → here's the viable parameter space"
- This would make Paper 1.2 genuinely publishable (Option 1)

If no such mode exists:
- Foundation A closes cleanly (DR4)
- The paper's negative-results content strengthens
- But the paper remains a bridge manuscript (Option 2) unless Foundation B or C produces a result

## Recommended next move

### Immediate (this week)
1. **Submit the closure paper** (`supplement_negative_results.tex`) to arXiv as a standalone. It is publication-ready. Primary: gr-qc, cross-list: hep-th, astro-ph.CO.
2. **Hold Paper 1.2.** Do not submit. It is not ready.

### Short-term (2–4 weeks)
3. **Execute Foundation A first check.** This is a focused literature review + calculation:
   - Map ghost-free PGT parameter subspace (Sezgin-van Nieuwenhuizen conditions)
   - For each ghost-free point, compute torsion mass eigenvalues
   - Determine if any mode has $m \lesssim H_0$
   - Write up as a technical note (1–2 pages)
   - Estimated effort: 1–2 weeks of focused work

### Medium-term (1–3 months)
4. **Based on Foundation A outcome:**
   - If positive: incorporate into Paper 1.2 Part III, upgrade to publishable reframing paper
   - If negative: close Foundation A, move to Foundation B first check (Nieh-Yan topological question), then Foundation C
   - If all three close: Paper 1.2 becomes a comprehensive negative-results paper — still publishable but with a different narrative ("the landscape of geometric dark energy is more constrained than assumed")

---

## Decision summary

| Criterion | Current Status |
|---|---|
| Scientific completeness | Partial — Part I (phenom) ✓, Part II (closures) ✓, Part III (directions) ✗ |
| Novel result | Closure program (already in standalone paper) |
| First-principles derivation | None |
| Publishable as-is | **No** |
| Publishable after Foundation A check | **Likely yes** (if positive) or **Possible** (if negative, as expanded negative-results paper) |
| Recommended action | Submit closure paper now; hold Paper 1.2; execute Foundation A first check |

---

## Comparison of publication vehicles

| Paper | Status | Action |
|---|---|---|
| Closure paper (`supplement_negative_results.tex`) | Publication-ready | Submit to arXiv now |
| Paper 1.2 (`paper_1_2_draft.tex`) | Bridge manuscript | Hold pending Foundation A result |
| Paper 1.01 (`paper_1_01_archive/`) | Archived | Do not submit; superseded |
