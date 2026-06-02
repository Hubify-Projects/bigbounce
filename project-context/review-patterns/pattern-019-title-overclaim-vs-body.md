---
status: confirmed
proposed_by: r-round-pattern-mine
proposed_date: 2026-04-30
confirmed_date: 2026-06-02
review_target: catalog
merges: [R42-NEW-019 title-overclaim-vs-body, P4-pattern-025 content-title-framing-drift]
---

# Pattern 019 — Title/abstract still markets a hypothesis the body has killed (bait-and-switch)

**First seen**: P1 R42 (2026-04-30) — title "Search for Geometric Dark Energy"
survived Sec XV.E unanimous-4-reviewer 92-efold no-go closure.
**Severity**: high (BLOCKER-grade per external; reads as bait-and-switch)
**Frequency**: ≥5 cross-paper observations
- R42: P1 title vs §XV.E no-go (3-reviewer unanimous);
  P3 "spectral sources from 37M" vs catalog that includes CMB patches / X-ray /
  IR; P1 §III.D "spin-torsion MCMC inference" while code is stock CAMB
- P4 v1.0.66 external: B12, M9 — "chirality / parity-violation" framing on a
  catalog paper that does not test parity
- P1A 2026-06-02 external: Gemini/ChatGPT both flagged title-vs-body framing
  drift (subset of M9 cluster)

**Detection**: for every BLOCKER-level no-go, null result, or major caveat in the
body, grep title + abstract + section headers for the marketing language of the
hypothesis being killed. Any survival = pattern-019 hit. Also: read title alone,
predict body; mismatch is the same pattern from the other direction.

## What it looks like

> R42 P1 R3 BLOCKER: "Title 'Search for Geometric Dark Energy' contradicts
> Sec XV.E proof that no choice of Ξ-prefactor survives a 92-efold inflationary
> dynamics. Title invites readers expecting a discovery; body delivers a no-go."

> P4 v1.0.66 GPT-B12: "Title frames this as a chirality / parity-violation
> result. Catalog labels are CW/CCW probabilities only — no null test or
> consistency-with-isotropy quantification is reported. Reframe as
> 'morphology catalog' or add the parity quantification."

## Truth-audit verdict

VERIFIED in 4 of 5 cross-paper instances. The fifth (P1 §III.D MCMC framing)
was a closure-introduced regression already covered by pattern-008.

## Examples observed

- P1 (R42): title "Search for Geometric Dark Energy" + §XV.E no-go
- P3 (R42): "spectral sources from 37M" + catalog containing CMB patches/X-ray
- P1A (§III.D, R42): "spin-torsion MCMC inference" + stock-CAMB pipeline
- P4 v1.0.66: parity-violation framing on a catalog without parity test
- P1A 2026-06-02 external: title/abstract drift relative to nogo body

## Root cause

Title is set before the no-go lands; closure pipeline edits body sections but
no skill walks the title/abstract for the same claim. Standing instinct to
"keep the marketing story together" survives even after empirical evidence
has killed the headline hypothesis.

## Pre-review check

Before any external submission OR cross-vendor R-round:

```bash
# Step 1: extract title + abstract + section headers
grep -nE '^\\title\{|^\\begin\{abstract\}|^\\section\{|^\\subsection\{' <paper.tex>

# Step 2: for every BLOCKER closure landed since prior version, grep title/abs
#   for the marketing language of the killed hypothesis
# Step 3: any survival → BLOCKER. Either update title to reflect what paper
#   actually shows, or add explicit qualifier ("Bound on …", "No-go for …").
```

Operational rule: if §pathc_caveats contains "no-go", "excluded", "ruled out",
"non-detection", or "null result" → title must explicitly contain at least
one of {"bound", "constraint", "no-go", "exclusion", "null", "limit"}.

## Related patterns

- Pattern 005 (overclaim language) — overlapping but distinct; 005 is
  superlatives anywhere, 019 is specifically title-vs-body mismatch
- Pattern 020 (load-bearing disclosure buried in appendix) — sibling: same
  framing-drift family, different location
- Pattern 018 (internal-rounds blind to editorial) — explains why 8 internal
  rounds did not catch P1A title/abstract drift
