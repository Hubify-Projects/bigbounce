# Pattern 005 — Overclaim language draws challenge

**First seen**: P2 R1 MAJOR-1 ("for the first time" template overlap claim)
**Severity**: medium (real prose problem; usually a real closure)
**Frequency**: 9 (P2 R1 MAJOR-1, P5 R1 PER-M2 + GRO-B1, P5 R3 GRO-M1, P5 R5 GRO-m2 + PER-M2, P1A R5/R6 GRO-M1 STALE, plus minor reflags)
**Detection**: grep paper for {first, novel, unprecedented, publication-grade,
load-bearing, definitive, authoritative, clean, smoking-gun, decisive,
landmark, breakthrough}. Each hit needs explicit justification or softening.
**Prevention**: pre-submission grep pass with auto-fail on any unhedged
superlative.

## What it looks like

> PER-M2 (MAJOR): "Publication-grade independent external validation" overclaim
> — TWebDESI2026 is at submitted-MNRAS stage, not peer-reviewed.

> GRO-m2 (minor, VERIFIED): residual superlatives "cleanest single-test
> publication-grade" + "cleanest single-statistic" at §IX.G must be softened.

## Truth-audit verdict

When the superlative is unjustified by quantitative comparison, VERIFIED.
When the superlative is quantitatively justified ("strongest piece of
evidence" because n=56,981 vs n=428), STALE/OPINION on reflag.

## Examples observed

- P2 R1 MAJOR-1: "for the first time" template overlap — closed in v1.7.32
- P5 R1 PER-M2 VERIFIED: "publication-grade independent external validation" →
  "independent contemporaneous DR1 cosmic-web analysis"
- P5 R1 GRO-B1 VERIFIED: "clean null" → "no evidence for environment-dependent
  chirality beyond catalog-monopole offset"
- P5 R3 GRO-M1 VERIFIED: "load-bearing concordance result" → "highest-N
  concordance result (supporting, not load-bearing)"
- P5 R5 GRO-m2 VERIFIED: "cleanest single-test publication-grade" → "direct
  single-test demonstration"; "cleanest single-statistic confirmation" →
  "direct single-statistic confirmation"
- P5 R5 PER-M2 VERIFIED: "the first public DESI cosmic-web catalog" →
  "a DESI-EDR-based probabilistic environment catalog"
- P1A R5/R6 GRO-M1: "Strip 'first/novel/unprecedented' bounds are textbook" —
  STALE because P1A already cites prior literature for each barrier
- P3 R1 GRO-B2 STALE: "first multi-survey" already qualified inline

## Root cause

LLM reviewers (especially Grok-4 brutal-honesty persona) trained to challenge
superlatives. Every "first/novel/load-bearing" claim invites a finding even
when justified.

## Pre-review check

Before any R-round:

```bash
egrep -in '\b(first|novel|unprecedented|publication[- ]grade|load[- ]bearing|definitive|authoritative|cleanest|smoking[- ]gun|decisive|landmark|breakthrough|state[- ]of[- ]the[- ]art)\b' *.tex
```

For each hit:
- If justified by quantitative comparison (n=X vs n=Y, σ=A vs σ=B): KEEP, add inline justification ("strongest because n=56,981 vs n=428").
- If qualitative-only: SOFTEN to "to our knowledge", "the largest in this paper",
  "direct demonstration".

This is a 5-minute pre-submission pass that closes a predictable
review-yield channel.
