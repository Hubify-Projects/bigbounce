---
status: confirmed
proposed_by: r-round-pattern-mine
proposed_date: 2026-04-30
confirmed_date: 2026-06-02
review_target: catalog
source: R42-NEW-022
---

# Pattern 022 — Closure replaced derivation with narrative

**First seen**: P2 R41 → R42 — R41 demanded explicit in-in Wick contraction
proof of Cai vs Li-Brandenberger convention. R42 closure was a single
sentence asserting "the factor of two is the standard in-in commutator
factor — i⟨[ζ³,L]⟩ = −2 Im⟨ζ³L⟩".
**Severity**: medium → high (always upgrades to BLOCKER on next-round catch
because a math demand was answered with prose)
**Frequency**: 4+ observed
- P2 R42 D-BLOCKER: §App A Wick contraction, sentence-only closure
- P4 v1.0.66 B11: "We confirm via TTA equation" assertion without derivation
- P1 R42 R3: "the scaling is dimensionally consistent" — assertion not proof
- P3 R42: 5σ threshold "follows from Gaussianity" — no derivation

**Detection**: any closure tagged "narrative edit only" / "added clarifying
sentence" on a finding that originally demanded math/empirical proof.

## What it looks like

> P2 R41 D-2 (original): "Provide the explicit in-in Wick contraction
> demonstrating that the Cai convention has factor of 2 vs Li-Brandenberger."
>
> P2 R42 closure: Added one sentence to Appendix A: "Interpreting the factor
> of two as the standard in-in commutator factor — i⟨[ζ³,L]⟩=−2 Im⟨ζ³L⟩."
>
> P2 R42 R3 D-BLOCKER (the reflag): "Closure is a restatement, not a proof.
> Two-line algebra is required to demonstrate the contraction; the asserted
> identity does not appear in any cited reference."

## Truth-audit verdict

VERIFIED in all 4 instances. Sentence-only closure of a math-demand finding
is a deferred-not-closed.

## Examples observed

- P2 R42 §App A Wick contraction (the canonical case)
- P4 v1.0.66 TTA equation closure
- P1 R42 scaling-ansatz "derivation"
- P3 R42 Gaussianity 5σ threshold

## Root cause

Closure protocol pressure to "ship a closure this round" + LLM-author
default to write prose. The author satisfies the LITERAL reviewer text
("addressed in App A") without satisfying the SUBSTANCE (the proof).

## Pre-review check

For every R-round, before closing any finding tagged math/derivation/proof/
empirical:

```bash
# Step 1: classify the closure type
# Closure types:
#   - artifact: new figure / notebook / dataset / code committed
#   - rerun: existing artifact re-executed with new parameters
#   - derivation: new equations / proof added with explicit algebra
#   - narrative: sentence added explaining intent
#
# Step 2: if original finding has any of {derivation, math, proof, empirical,
#   compute X, demonstrate, prove, recompute, retrain}:
#   - narrative-only closure → REJECT closure; mark "deferred" until artifact
#   - require explicit Appendix-derivation tag with full algebra
#
# Step 3: post-closure pre-flight grep for the pattern:
grep -nE '(Following|As a consequence|It follows|This implies|Interpreting).{0,80}(the|that).{0,40}(equation|identity|relation)' <paper.tex>
# Each hit must trace back to an explicit derivation block, not an assertion.
```

Standing rule (from `/take-critiques-seriously`): closure for a math/empirical
finding requires a math/empirical artifact, not a sentence.

## Related patterns

- Pattern 008 (closure-introduced regression) — sibling: 008 introduces a
  NEW error in the closure prose; 022 introduces NOTHING new — it just
  fails to address the original finding while declaring it addressed.
- Pattern 030 (round-to-round regression drift) — closures of pattern-022
  shape almost always reflag in subsequent rounds (sentence-only edits
  don't stick)
- Pattern 033 (prose-asserted-prefactor acceptance) — the reviewer-side
  mirror: CCAI sub-agents accept prose-asserted prefactors as if they
  were derivations
