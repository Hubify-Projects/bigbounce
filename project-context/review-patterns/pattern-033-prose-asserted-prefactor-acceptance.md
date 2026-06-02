---
status: confirmed
proposed_by: r-round-pattern-mine
proposed_date: 2026-05-08
confirmed_date: 2026-06-02
review_target: catalog
source: CCAI-cluster-pattern-021 CCAI-prose-asserted-prefactor-acceptance
severity_class: meta
---

# Pattern 033 — CCAI accepts prose-asserted prefactors / OOM estimates without derivation

**First seen**: CCAI cluster 2026-05-08 — OOOOO round caught 2 BLOCKER-tier
prefactor/OOM cases (B4 prefactor, M1 OOM convention) that all CCAI
sub-agents accepted as "fine, the paper says it's right."
**Severity**: high (load-bearing prefactors / OOM estimates are exactly the
class of claim a journal reviewer will challenge)
**Frequency**: 2+ confirmed instances in one OOOOO round; structural
prediction is that every paper carries 1-3 such claims

**Detection**: any prefactor (factor of 2, 4π, π/8, ½, 1/N) or OOM estimate
that is asserted in body prose without derivation. CCAI reads "we obtain
a factor of 2 from in-in commutator" as a satisfactory derivation; an
adversarial-math reviewer reads it as an assertion.

This is the reviewer-side mirror of pattern-022 (closure-narrative-
instead-of-derivation) and pattern-025 (mathematically-impossible
attribution). Pattern-022 is the AUTHOR side; pattern-033 is the
REVIEWER side. Both must be addressed in the pre-review check.

## What it looks like

> OOOOO-B4 (BLOCKER, external; CCAI MISSED): "The factor of 2 in the
> bispectrum normalization (paper Eq 3.4) is asserted to come from the
> in-in commutator. No derivation is given; no reference is given. CCAI
> rounds R43-R47 accepted this without flag. This factor is load-bearing
> — it changes σ from 12 to 24."

> OOOOO-M1 (MAJOR, external; CCAI MISSED): "Order-of-magnitude estimate
> for primordial-spectrum amplitude (Eq 2.7) uses (k/aH)² convention
> without stating it. The opposite convention is also in use in the
> literature. Result differs by π². CCAI accepted."

## Truth-audit verdict

VERIFIED. Both prefactor and OOM-convention cases trivially resolve once
the derivation is demanded.

## Examples observed

- OOOOO-B4 (in-in commutator factor of 2)
- OOOOO-M1 ((k/aH)² convention)
- (predicted) every paper with load-bearing prefactors in body prose

## Root cause

CCAI sub-agents read the paper as a paper, not as a proof. They check
that prose flows, citations exist, conclusions match results — they do
NOT run a symbolic derivation engine on every equation. Any prefactor
or OOM estimate asserted in body prose is accepted.

## Pre-review check

```bash
# Step 1: grep for prefactor assertions in equations
grep -nE '(factor of [0-9]+|prefactor|\\frac\{[0-9]+\}\{[0-9]+\}|coefficient of [0-9]+|2π|4π|π/[0-9]+|[0-9]+!)' <paper.tex>

# Step 2: for each hit, verify there is EITHER:
#   - an explicit derivation in an appendix
#   - a citation to a published derivation
#   - a Wolfram-verified symbolic check committed alongside the paper
# Pattern matches with NEITHER → flag as pattern-033 / pattern-022

# Step 3: for OOM estimates, verify the convention is explicitly stated
#   in Methods. Acceptable: "We use the (k/aH)² convention throughout."
#   Unacceptable: assuming convention from context.

# Step 4: route any unsatisfied prefactor to /wolfram-deepseek-verify for
#   symbolic check BEFORE external dispatch.
```

Operational rule: every load-bearing prefactor / OOM estimate in body
prose must carry one of:
- `% derivation: \ref{app:foo}` inline comment
- `% citation: \cite{foo:bar}` inline comment
- `% wolfram-verified: <commit-sha>` inline comment

Closures without one of these survive CCAI but fail external.

## Related patterns

- Pattern 022 (closure-narrative-instead-of-derivation) — author-side
  mirror: 022 writes prose instead of derivation; 033 accepts prose as
  derivation
- Pattern 025 (mathematically-impossible attribution) — sibling: 025 is
  prose that contradicts math; 033 is prose that asserts math without
  proof
- Pattern 031 (self-review severity under-classification) — explains
  WHY CCAI accepts these: severity floor is too low
- `/wolfram-deepseek-verify` — implements the symbolic-derivation harness
