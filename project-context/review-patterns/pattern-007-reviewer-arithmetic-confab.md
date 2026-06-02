# Pattern 007 — Reviewer arithmetic / sign / numerical confabulation

**First seen**: P2 R3 PER-B1 (Maldacena (5/12)(1-n_s) sign wrong)
**Severity**: high (reviewer asserts a falsifiable numerical claim that is wrong)
**Frequency**: 4 (P2 R3 PER-B1, P3 R4 PER-B1 vol "962", P5 R4 PER-B1 ApJ vol "962", P1B R5/6/7 PR4-vs-PR3 dataset claim)
**Detection**: reviewer cites a specific number, sign, journal volume, or
arithmetic expression and claims the paper is wrong about it.
**Prevention**: when a reviewer asserts a numerical or sign error, ALWAYS
recompute / re-verify against the cited source before accepting.

## What it looks like

> PER-B1 (BLOCKER): Maldacena's f_NL_local = (5/12)(1-n_s) at n_s=0.9649 gives
> (5/12)(0.0351), which is negative. The paper's claim of positive +0.015 is
> a sign error.

Recomputing: (1 - 0.9649) = +0.0351, so (5/12)(0.0351) = +0.0146. The
reviewer's arithmetic was wrong.

## Truth-audit verdict

When recomputed → paper-on-disk matches: FALSIFIED. When the paper genuinely
has the sign/number error: VERIFIED (rare).

## Examples observed

- **P2 R3 PER-B1 FALSIFIED**: claimed (5/12)(1-0.9649) is negative;
  recompute → +0.0146 positive. Paper's "in absolute value" hedge already
  protects against sign ambiguity in the contrast ratio.
- **P3 R4 PER-B1 FALSIFIED**: claimed Heinrich 2023 PRD volume "962";
  actual published volume = 109 (article 123511), arXiv:2311.13082.
- **P5 R4 PER-B1 FALSIFIED**: claimed DESIVAST ApJ volume = 962; WebFetch on
  doi.org/10.3847/1538-4357/adb559 → IOPscience returns ApJ **982**, 38.
- **P1B R5/R6/R7 PER-B1 FALSIFIED**: 3 consecutive rounds Perplexity asserted
  Eskilt 2022 used Planck PR3, not PR4/NPIPE. Verified via Eskilt's public
  reproduction repo README — actual data is PR4/NPIPE + WMAP9.

## Root cause

LLM reviewers (Perplexity especially) sometimes mis-compute simple arithmetic
or confabulate journal volume numbers. Without an internal "recompute before
accepting" rule, these get accepted as VERIFIED closures and introduce false
edits.

## Pre-review check

When any reviewer finding contains:
- A literal number (`σ = 8.14`, `volume 962`, `n_s = 0.9649`)
- A sign assertion (`should be negative`, `is positive`)
- An arithmetic expression (`(5/12)(1-n_s)`)
- A journal volume / page number claim

Add an automated check before acceptance:

1. **Number checks**: pull the paper's reported value, do the arithmetic
   in Python, compare to the reviewer's claim.
2. **Sign checks**: explicitly compute the sign of the contested expression.
3. **Bib metadata checks**: WebFetch the cited arXiv ID or DOI and read the
   journal-volume-page directly.
4. **Dataset version claims**: cross-check against the paper's public
   reproduction repository (pattern 002).

For Perplexity findings of this shape, default classification is
**RECOMPUTE-BEFORE-ACCEPT**. Only after recompute confirms the reviewer's
claim is the finding promoted to VERIFIED.
