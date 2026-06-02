---
status: confirmed
proposed_by: r-round-pattern-mine
proposed_date: 2026-04-30
confirmed_date: 2026-06-02
review_target: catalog
source: R42-NEW-020
---

# Pattern 020 — Load-bearing disclosure buried in appendix / footnote / caveat

**First seen**: P1 R42 (2026-04-30) — "scaling ansatz dimensionally correct
on-shell" admission buried in Appendix B while abstract treats
ρ_Λ = Ξ M_Pl⁴ as a derivation.
**Severity**: high (Houston Method v2 Principle 12: every caveat that changes
the headline claim must live at the headline)
**Frequency**: 3+ observed
- P1 (R42): appendix-only "ansatz, not derivation" admission (B3)
- P3 (R42): Caveat (i) of §VI.D admits 5-fold CV ran ONLY on training pool;
  intro §II.B markets CV as catalog-wide stability (M8 / R3 Ethics)
- P3 (R42): Table I footnote admits LAMOST 5.8% recovery FAIL while body
  label reads "PASS-with-diagnostic"

**Detection**: audit every appendix / footnote / "Caveat" subsection for
sentences containing {"not", "only", "limited", "restricted to", "not include",
"ansatz", "not derived", "not validated"}. For each hit, check whether the
abstract + intro + headline carries the same caveat. Asymmetry = pattern-020 hit.

## What it looks like

> R42 P1 B3: Sec II asserts "we derive ρ_Λ = Ξ M_Pl⁴ from the geometric
> bounce framework." Appendix B states "the scaling is a dimensionally-
> consistent ansatz, not derived from a microscopic Lagrangian." External
> reviewers reading abstract only will mis-grade the result.

## Truth-audit verdict

VERIFIED across all 3 R42 instances. Where appendix says "X is an ansatz",
body must also say "X is an ansatz" — not "X is derived".

## Examples observed

- P1 R42: Appendix B ansatz disclosure vs body "derivation" framing
- P3 R42: Caveat (i) §VI.D vs §II.B CV-stability marketing
- P3 R42: Table I footnote LAMOST FAIL vs body PASS-with-diagnostic label
- (predicted, not yet verified) P5: any "supporting, not load-bearing"
  Caveat surviving while §IX.G headline reads "primary evidence"

## Root cause

Asymmetric closure: an honest admission written in revision survives in the
appendix or footnote where it was first added. The summary surfaces (abstract,
intro, conclusion) were written earlier and never re-walked. The result is a
paper that's honest if you read it cover-to-cover and overclaim-y if you read
only the abstract.

## Pre-review check

```bash
# Step 1: extract every Caveat/Limitation/footnote/appendix sentence
grep -nE '(Caveat \([ivx]+\)|Limitation|Footnote|^\\footnote\{)' <paper.tex>

# Step 2: for each sentence, find the matching claim in abstract + intro +
#   conclusion. Run a sentence-similarity check or grep on the key noun
#   phrase. If the caveat-language ("only", "ansatz", "not derived", "FAIL")
#   does NOT appear at the headline location → BLOCKER.

# Step 3: for every "PASS-with-diagnostic", "supporting", "consistent-with",
#   verify a corresponding appendix caveat does NOT contradict the label.
```

Standing rule (Houston Method v2 Principle 12): every load-bearing caveat
must appear at the headline at the SAME confidence level as the appendix
admission. No "appendix-only" exemption for claims that change the result.

## Related patterns

- Pattern 019 (title overclaim vs body) — sibling, different surface
- Pattern 005 (overclaim language) — overclaim at the headline level
- Pattern 017 (review-log in body prose) — different content shape, same
  asymmetric-surface failure mode
