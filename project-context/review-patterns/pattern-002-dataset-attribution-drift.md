# Pattern 002 — Dataset attribution drift across closures

**First seen**: P1B R-multi-round2 (PER2-M1 Eskilt2022b "Planck+ACT" → "WMAP+Planck")
**Severity**: high (introduces NEW factual errors via closure prose)
**Frequency**: 6 (P1B rounds 1-4 Eskilt2022b oscillation; P1A round-3 Planck/ACT DR6 attribution)
**Detection**: Same dataset attribution sentence is corrected in successive
rounds, with each "fix" introducing a new (different) error.
**Prevention**: When correcting any dataset label in closure prose, cross-check
against the cited paper's PUBLIC REPRODUCTION REPO or NASA-ADS metadata, NOT
against neighbouring citations in the same paragraph.

## What it looks like

The canonical Eskilt2022b oscillation:
- v1B.0.31: "joint Planck+ACT value" (WRONG — Eskilt is WMAP+Planck, no ACT)
- v1B.0.32 closure: "joint WMAP+Planck value (PR4 NPIPE + WMAP)" (CORRECT)
- v1B.0.33 closure (round-3 PER3-B2): regressed to "WMAP9 + Planck 2018 (PR3)"
  because round-3 audit assumed Eskilt used Planck-2018-PR3 like the DiegoPalazuelos
  2022 reference next to it — WRONG, Eskilt actually used PR4/NPIPE
- v1B.0.34 closure (round-4 PER4-B2): corrected back to "WMAP9 + Planck PR4/NPIPE"
  via WebFetch on github.com/LilleJohs/Cosmic_Birefringence README
- v1B.0.34 stable through rounds 5, 6, 7 (Perplexity tried to reverse 3 more times — all FALSIFIED)

## Truth-audit verdict

The original drift IS VERIFIED (genuine prose-attribution error). But each
*proposed fix* must be independently audited — a reviewer's proposed fix can
be the wrong fix.

## Examples observed

- P1B R1 PER-B2 → R2 PER2-M1 (VERIFIED) → R3 PER3-B2 (VERIFIED, regression
  introduced by R2) → R4 PER4-B2 (VERIFIED, corrected via repo cross-check) →
  R5/R6/R7 PER5/6/7-B1 (FALSIFIED — reviewer trying to reverse the correct fix)
- P1A R3 PER-m1: "Planck/ACT DR6 3.6σ joint signal" — conflated Eskilt 2022
  (WMAP+Planck, 3.6σ) with DiegoPalazuelos 2025 (ACT DR6, 2.9σ). CLOSED in v1A.0.39
  with full disambiguation at 3 sites + mechanical sed pass on remaining loose
  references.

## Root cause

Closure prose for a dataset attribution often borrows the dataset description
from a neighbouring citation in the same paragraph. When the neighbouring
citation uses a different dataset (e.g. DiegoPalazuelos 2022 = NPIPE,
DiegoPalazuelos 2025 = ACT DR6, Eskilt 2022 = PR4 NPIPE + WMAP9), the closure
introduces a new mis-attribution that the next round catches.

## Pre-review check

Before any closure that edits a dataset label:

1. Find the cited paper's **public reproduction repository or code release**
   (look for GitHub link in arXiv abs page, NASA-ADS "Data" tab, or paper §Data
   Availability section).
2. Read the README / data-loading script to determine the *actual* dataset.
3. If no repo exists, fall back to the paper's abstract literal text.
4. NEVER copy the dataset label from a neighbouring citation in the same
   paragraph — they are different papers using different data.
5. After the closure lands, GREP THE ENTIRE PAPER for the dataset label and
   verify all occurrences match (pattern 008 prevention).

The canonical proof-of-concept artifact is the Eskilt+Komatsu 2022 reproduction
repo: `github.com/LilleJohs/Cosmic_Birefringence` — used to catch the round-3
regression on P1B.
