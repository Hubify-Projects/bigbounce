---
status: confirmed
proposed_by: r-round-pattern-mine
proposed_date: 2026-05-15
confirmed_date: 2026-06-02
review_target: catalog
source: P4-pattern-022 paper-side-arithmetic-vs-cited-literature
---

# Pattern 028 — Paper-side arithmetic disagrees with cited literature

**First seen**: P4 v1.0.66 external — B6 flagged "10× larger than Shamir+2022"
claim. Shamir+2022 catalog is 77,840 galaxies; P4 is 26,636. 26,636/77,840
= 0.34, i.e. P4 is ~3× SMALLER, not 10× larger.
**Severity**: high (every "Nx larger / Y% improvement / outperforms" claim
is checkable and load-bearing)
**Frequency**: 3+ instances
- P4 v1.0.66 B6: "10× larger than Shamir+2022" (actually 3× smaller)
- P3: "twice the sensitivity of [Author Year]" (sensitivity numbers from
  cited paper disagreed; flagged R42 R2)
- P1A: "100× tighter constraint than [Author Year]" (intermittent flag
  across rounds; sometimes correct, sometimes off by an order of magnitude)

**Detection**: for every "Nx larger than [X]", "Y% improvement over [X]",
"twice the [metric] of [X]", "outperforms [X] by Z" claim, fetch the cited
paper's abstract/Table-1 and verify the comparison number. Mismatch =
BLOCKER.

## What it looks like

> P4 v1.0.66 B6 (Grok-4 brutal-honesty): "Abstract: 'Our catalog is 10×
> larger than Shamir+2022.' Shamir+2022 MNRAS 516, 2281 reports a
> classification catalog of 77,840 galaxies. P4 reports 26,636. 26,636 is
> ~3× SMALLER than 77,840, not 10× larger. Either the comparison is
> against a different Shamir catalog (then say which), or the comparison
> direction is reversed (then fix), or the numerator is wrong."

## Truth-audit verdict

VERIFIED in 2 of 3 instances; the third (P1A 100× constraint) resolved
to a unit-system confusion (σ vs σ²) once the comparison was traced.

## Examples observed

(See "Frequency" list above.)

## Root cause

LLM-author tendency to write punchy comparisons ("10× larger", "tightest
constraint to date") without fetching the cited paper's numbers. Closure
pipeline accepts the prose; only reviewers who actually fetch the cited
paper catch the error.

## Pre-review check

```bash
# Step 1: extract every comparative claim
grep -nE '\b([0-9]+(\.[0-9]+)?|several|order(s)? of magnitude)\s*(x|×|times|fold|percent|%)\s*(larger|smaller|tighter|looser|better|worse|more|less|sensitive|improvement)' <paper.tex>

# Step 2: for each hit, identify the cited paper and the cited value
# Step 3: fetch the cited paper's abstract / table-1 via:
#   - AlphaXiv (preferred; cacheable, no rate limit)
#   - NASA ADS / arXiv API
# Step 4: recompute the comparison; if direction or magnitude is wrong
#   → BLOCKER. Closure must include both the recomputed number and the
#   inline comment recording the cited value.

# Step 5: standing format for comparison claims:
#   "26,636 galaxies, ~3× the Shamir+2022 catalog of 77,840 [n_shamir22]"
#   with footnote pointing to the Table 1 in Shamir+2022.
```

## Related patterns

- Pattern 007 (reviewer arithmetic confab) — opposite-direction sibling:
  007 is reviewer math wrong, 028 is author math wrong
- Pattern 025 (mathematically-impossible attribution) — sibling: 025 is
  math against your own equation; 028 is math against literature
- Pattern 005 (overclaim language) — overlapping: "outperforms" /
  "tightest" claims often trigger both 005 and 028
- `/wolfram-deepseek-verify` skill — implements arithmetic cross-check
  for any quantitative comparison
