# Pattern 009 — GPT-5→gpt-4o fallback produces low-rigor generic BLOCKERs

**First seen**: P4 R1 GPT B1-B6 (all generic prose-clarity asks)
**Severity**: medium (BLOCKER-graded findings, but content is OPINION-tier)
**Frequency**: 30+ across 6 papers (every single round; GPT-4o fallback persists)
**Detection**: GPT B-prefixed findings that ask for "more discussion of X" or
"expand on Y" without citing on-disk content or a falsifiable defect.
**Prevention**: classify GPT B-findings as OPINION/MINOR by default; promote
to VERIFIED only when the request cites a specific numerical or attribution
defect on-disk.

## What it looks like

> GPT-B1 (BLOCKER): The parity-odd term in §II.B.2 introduces a phenomenological
> ansatz without rigorous derivation; expand the limitation discussion.
>
> GPT-B5 (BLOCKER): Perturbation-transparency result presented as central but
> observational implications not fully explored; expand on implications for
> future observational tests.

## Truth-audit verdict

Almost always STALE or OPINION. Across 19 rounds, GPT-4o fallback produced
**zero** VERIFIED closures that were not already produced by Grok or Perplexity
on the same paper.

## Examples observed

- **P4 R1 GPT-B1-B6**: all 6 BLOCKER asks "develop quantitative model", "justify
  weight via ablation", "discuss effective sample size", "develop monopole
  model", "look-elsewhere correction", "transfer function" — all 6 OPINION
  or STALE.
- **P2 R3 GPT-B1-B6**: 100% verbatim duplicates of R1/R2 already-closed
  findings.
- **P1A R3 GPT-B1-B6**: all 6 BLOCKERs identical reflag of round-1 findings.
- **P3 R1-R3 GPT-B1-B6**: same 6 findings across 3 consecutive rounds, all
  STALE against §pathc_caveats (a)-(j).
- **P1B every round**: GPT-B1-B6 reflag "AIC/BIC/ln B model-comparison",
  "NaMaster pipeline validation", "ALP-not-ECH context" verbatim.

GPT-4o fallback's median behaviour: 6 BLOCKER-level findings per round, all
generic prose-clarity asks, all already addressed on-disk.

## Root cause

The model received the same prompt across rounds; the GPT-4o-fallback
methodology persona is biased toward 6-bucket output (one per major section).
Without a `\paperVersion`-aware prompt or a "did the closure update?" check,
the model produces the same 6 buckets every round.

Additionally, gpt-4o (fallback from gpt-5 when the API rejects) is less
rigorous than gpt-5 would be. The fallback note appears in every
synthesis ("GPT-4o (FALLBACK from gpt-5)").

## Pre-review check

For each GPT B-prefixed finding, before truth-audit:

1. Does the finding cite a **specific numerical claim** or **specific
   attribution** in the paper? If NO → classify OPINION/MINOR by default.
2. Does the finding cite a **specific line number** or **section**? If NO →
   classify OPINION/MINOR by default.
3. Does the finding's request resolve to text **already on-disk** with a
   single grep? If YES → STALE.
4. If GPT-fallback (from gpt-5) is the persona → apply 2σ-stricter promotion
   threshold compared to Grok or Perplexity.

A useful rule: if the GPT-B1-B6 set is **identical** to GPT-B1-B6 from a
prior round on the same paper, the round's GPT contribution can be marked
fully convergent-silent without per-finding processing (saves ~30 minutes
of audit time per round).
