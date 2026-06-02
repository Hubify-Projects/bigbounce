# Pattern 013 — Perplexity catches real issue but proposes wrong fix

**First seen**: P1B R-multi-round3 PER3-B2 (Eskilt PR4 → PR3 wrong fix proposal)
**Severity**: high (closure-prose-author trusts the reviewer's fix and
introduces a new regression — pattern 008 territory)
**Frequency**: 5 (P1B R3, P1B R5-R7 reversion attempts, P5 R4 ApJ vol "962")
**Detection**: Perplexity flags a real attribution / dataset / version
problem but proposes a fix that, when verified against the actual source,
is itself wrong.
**Prevention**: when Perplexity proposes a citation/dataset fix, verify
against the ACTUAL paper source (repo README, paper abstract, ADS metadata) —
not just the reviewer's wording.

## What it looks like

> PER3-B2 (MAJOR, VERIFIED upgraded): The R2 closure prose "joint WMAP+Planck
> value (the PR4 NPIPE + WMAP analysis)" is wrong. Eskilt 2022 uses Planck
> 2018 PR3, not PR4 NPIPE. Fix: relabel to "WMAP9 + Planck 2018 (PR3) analysis".

Accepted as closure prose in R3. R4 then catches the new regression: the
Eskilt+Komatsu 2022 reproduction repo README says **Planck Data Release 4
(NPIPE)**. So Perplexity caught the real prose drift, but its proposed fix
swung in the wrong direction.

## Truth-audit verdict

Verify the reviewer's PROPOSED FIX against an independent source before
accepting. The reviewer is often correct that prose-A is wrong but wrong
about prose-B being right.

## Examples observed

- **P1B R3 PER3-B2**: real prose drift caught, proposed PR3 fix was wrong;
  correct fix per Eskilt repo is PR4/NPIPE + WMAP9 (landed in R4).
- **P1B R5/R6/R7 PER-B1**: same Perplexity reviewer tried to revert R4's
  correct PR4/NPIPE fix back to PR3 three more consecutive times — each
  reversal FALSIFIED via the same repo cross-check.
- **P5 R4 PER-B1**: Perplexity caught that we were citing DESIVAST ApJ
  volume, proposed correction to "962". Actual ApJ volume (verified via
  doi.org/10.3847/1538-4357/adb559) is **982**. Proposed fix wrong.
- **P1B R1 PER-B2**: caught that Eskilt prose said "joint Planck+ACT" (wrong;
  Eskilt is WMAP+Planck). R2 closure adopted "joint WMAP+Planck" correctly.
  Original Perplexity finding was correct on the diagnosis; R2 author chose
  the right fix path.
- **P3 R1 PER-B1**: Perplexity claimed mata-bounce f_NL = -35/8 should be
  cited to Quintin2014/Cai2014 instead of Cai:2009fn. Audit: Cai:2009fn is
  the correct primary source per the actual derivation chain. Perplexity's
  proposed fix was wrong.

## Root cause

Perplexity Sonar Pro's citation-forensics persona scans for inconsistencies
in the prose and proposes a fix based on its best-guess of what the cited
paper actually says. When the model's knowledge of the cited paper's data
is itself wrong, the proposed fix introduces a different (often equally wrong)
attribution.

## Pre-review check

For every Perplexity-proposed citation/dataset fix:

1. **Don't apply the fix verbatim.** Treat the finding as
   "DIAGNOSIS-CORRECT, FIX-UNVERIFIED" by default.
2. **Verify the proposed fix against a primary source**:
   - Public reproduction repo (GitHub) — preferred
   - Paper's own abstract on arXiv (literal text)
   - NASA-ADS metadata
   - The published journal's actual PDF
3. **Document both the diagnosis and the verified fix** in the closure
   audit-log block, including the source consulted (e.g.
   "fix verified via github.com/LilleJohs/Cosmic_Birefringence README").
4. **Cross-vendor check** if available: independent verification with a
   second reviewer (Grok or GPT) on the same finding catches divergent
   fix proposals.

For P1B Eskilt thread specifically: the in-tex audit-log block at L65-99
documents the full PR3 ↔ PR4/NPIPE oscillation, so future rounds reject
the wrong-direction fix without re-running verification each time. This
audit-log-in-tex pattern is the operational defence against pattern 013.
