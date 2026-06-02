---
status: confirmed
proposed_by: r-round-pattern-mine
proposed_date: 2026-04-30
confirmed_date: 2026-06-02
review_target: catalog
merges: [R42-NEW-023 trivial-fix-refused-with-false-cost-excuse, P4-pattern-024 unjustified-compute-bound-defer]
---

# Pattern 023 — Trivial fix refused with false-cost / data-engineering-laziness excuse

**First seen**: P3 R42 B10 — paper claims 100k OOD validation "requires ~2×
full-survey budget"; at stated throughput (1,142 spec/s) the cost is 87.5 s
of GPU time.
**Severity**: high (Houston "/eat-the-frog" standing directive; this pattern
is the exact failure mode that memo names)
**Frequency**: 6+ observed across 2 papers
- P3 R42 B10: 100k OOD = 87.5 s GPU (paper says "~2× survey budget")
- P4 R42 B19: b/a<0.3 edge-on filter = one pandas.merge join (paper says
  "not executed in present analysis")
- P4 R42 B20: GZ1-only accuracy = subset 6,637 of 26,636 labels (refused)
- P4 v1.0.66 B10/M10: HF cross-vendor dataset card re-upload deferred to
  "next revision" — 5-min op
- P4 v1.0.66 misc.: "left to future work" closures on 1-day data-engineering
  tasks (covered by /no-future-work-defer)

**Detection**: for every "not executed", "deferred to future", "requires
substantial compute", "beyond the scope of this paper", "leave to future
work" → compute the actual cost from throughput / data volume / known
compute rates. Flag if actual cost < 1 GPU-day OR < 1 day of human time.

## What it looks like

> R42 P3 B10: "Validation on the 100k OOD held-out set is deferred to
> forthcoming work; it would require approximately twice the full-survey
> compute budget." (Paper section IX.E.)
> R42 R3 B10 closure: 100k specs / 1,142 specs/s ≈ 87.5 s of GPU. That is
> ~$0.001 of compute, not "2× survey budget". Run it.

> R42 P4 B19: "An edge-on filter b/a < 0.3 would remove ~2,500 edge-on
> galaxies. This filter is not executed in the present analysis."
> R42 R3 B19 closure: this is one line of pandas (df[df.ba < 0.3]). Cost
> is seconds. Refusing is the data-engineering equivalent of "future work."

## Truth-audit verdict

VERIFIED in all 6 instances. Houston's R42 master directive at the top of
the round explicitly named this pattern: "this is what I'm calling data-
engineering laziness — if the math fix is identified and the cost is
< 1 GPU-day, the closure is to RUN IT, not to defer it."

## Examples observed

(See "Frequency" list above.)

## Root cause

LLM-author tendency to inflate compute cost in self-defense against
reviewer demands; Houston Method v2 §RUN gate not enforced at closure
write-time. The deferral language has cost-of-zero — costs only land at
re-review.

## Pre-review check

```bash
# Step 1: grep paper for deferral language
grep -niE '(not executed|left to future work|deferred to (future|next|forthcoming|forthcoming work|revision)|requires substantial compute|beyond the scope of (this|the) (paper|present|current))' <paper.tex>

# Step 2: for each hit, extract the named operation and estimate cost
#   - "100k OOD validation" → throughput * count = seconds → BLOCKER
#   - "b/a < 0.3 filter" → pandas one-liner → BLOCKER
#   - "GZ1-only accuracy" → subset existing labels → BLOCKER
#   - "MCMC chain on H200" → ~few hours → DO-NOW per Houston budget
#
# Step 3: any "deferral" whose actual cost is < 1 GPU-day or < 1 day of
#   human time → BLOCKER. Closure is to EXECUTE the operation, not to
#   reword the deferral.
```

Standing rule (`/eat-the-frog` + `/no-future-work-defer`): default
disposition for any "future work" hit is DO-NOW; only TRULY-BLOCKED
(hardware/data does not exist) survives.

## Related patterns

- Pattern 022 (closure-narrative-instead-of-derivation) — sibling: 022 is
  prose closure of math demands; 023 is "decline to do it" closure of
  cheap engineering tasks
- Pattern 029 (estimator-multiplicity-no-preregistration) — overlapping:
  refusing to pre-register often comes with "leave to revision" framing
- (Standing skill) `/no-future-work-defer` — implements this pattern's
  prevention rule across all skills, not just papers
