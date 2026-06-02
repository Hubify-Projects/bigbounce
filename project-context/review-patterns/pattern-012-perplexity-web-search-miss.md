# Pattern 012 — Perplexity web search misses recent (within ~6 months) arXiv papers

**First seen**: P1B R-multi-true95 PER-B1 (Liu 2507.04265 flagged fictional; real)
**Severity**: medium (high false-positive rate; consumes audit time)
**Frequency**: 20+ across 19 rounds (Liu, DESI DR2, DiegoPalazuelos, Cai-Zhu, ASTRA, TWebDESI)
**Detection**: Perplexity flags a `\bibitem{}` with an arXiv ID where YY is
within ~6 months of the round date.
**Prevention**: cross-verify any Perplexity "fictional citation" claim
against arxiv.org directly (WebFetch, not Perplexity).

## What it looks like

> PER-B1 (BLOCKER): The citation `Liu2025ECTorsionDESI` for arXiv:2507.04265
> is not discoverable through standard databases. Either fabricated or
> wrongly attributed.

When verified via direct WebFetch on `arxiv.org/abs/2507.04265`:
> Liu, Li, Xu, Biesiada, Wang. "Torsion cosmology in the light of DESI,
> supernovae and CMB observational constraints." Eur. Phys. J. C 85, 1351
> (2025), arXiv:2507.04265.

Real paper. Perplexity's web search index didn't have it.

## Truth-audit verdict

Almost always FALSIFIED when arXiv ID year-month is within ~6 months of round
date. Cross-verify before any action.

## Examples observed

- **Liu et al. ECTorsionDESI2025 (2507.04265)**: flagged fictional in P1B
  rounds 1, 2, 3, 4, 5, 6, 7 — all 7 FALSIFIED. Paper exists, published EPJC.
- **DESI DR2 (2503.14738)**: flagged fictional in P1B R1 — FALSIFIED, real.
- **DiegoPalazuelos+Komatsu 2025 (2509.13654)**: flagged fictional in P1B
  R1, R3, R4, R5, R6, R7 — all FALSIFIED. Paper exists.
- **Cai-Zhu echoes 2026 (2603.13924)**: flagged "future-dated / does not exist"
  in P2 R3 — FALSIFIED. Real preprint from 2026-March, posted before round date.
- **ASTRA 2604.01456 / TWebDESI 2604.02463**: flagged fictional in P5 R1 —
  both FALSIFIED via WebFetch on arxiv.org.
- **Legner 2025 (2507.09228), Alam 2025 (2509.03508), Papanikolaou 2024
  (2404.03779)**: flagged fictional in P1A R4 — all FALSIFIED via WebFetch.

## Root cause

Perplexity Sonar Pro's web index has a lag for fresh arXiv submissions —
papers within ~6 months of round date are particularly vulnerable. The
indexing pipeline doesn't always pick up new preprints quickly. The model
defaults to "I can't find this" → "this might be fabricated", which gets
graded BLOCKER/MAJOR.

## Pre-review check

When processing any Perplexity "fictional citation" finding:

1. Extract the arXiv ID from the finding (YYMM.NNNNN format).
2. Parse YY (year) and MM (month) from the ID.
3. Compute the age: round_date - paper_date.
4. If age < 6 months → **default classification FALSIFIED-PENDING-WEBFETCH**.
   Do a direct WebFetch on `arxiv.org/abs/<id>` and only escalate to VERIFIED
   if the WebFetch returns 404 or returns a paper that doesn't match the
   bib metadata (then it's pattern 011, not pattern 012).
5. If age ≥ 6 months → still WebFetch first, but lower prior on FALSIFIED.

This check alone saves ~30 minutes per round of audit time once a paper has
2+ recent citations.
