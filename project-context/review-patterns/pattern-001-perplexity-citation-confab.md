# Pattern 001 — Perplexity citation confabulation (real-arXiv-flagged-fake)

**First seen**: P1A R-multi-true95 (PER-B1 `Golden2026P2`)
**Severity**: high (BLOCKER/MAJOR-graded by reviewer)
**Frequency**: 38 occurrences across rounds 1-8 over 6 papers
**Detection**: Perplexity Sonar Pro flags `\bibitem{X}` as "fabricated",
"does not exist", "synthetic", "arXiv ID unverifiable", or proposes a different
arXiv ID with mismatched metadata.
**Prevention**: Run a programmatic bib audit (arXiv API + ADS) for every
`\bibitem{}` BEFORE dispatching any cross-vendor R-round.

## What it looks like

> PER-B1 (BLOCKER): The citation `\bibitem{Liu...ECTorsionDESI2025}` for
> arXiv:2507.04265 does not resolve through standard databases (arXiv, NASA
> ADS, INSPIRE-HEP). The Liu+ et al. 2025 EPJC paper as described appears
> fabricated.

## Truth-audit verdict

**Almost always FALSIFIED.** Of 38 instances, 0 surfaced a citation that
was actually fabricated when checked against arXiv directly via WebFetch.
All 38 resolved to real published papers.

## Examples observed

- P1A R3 PER-B1: `ShapiroTeixeira2014` flagged fictional → arXiv:1402.4854 real
- P1A R4 PER-BLOCKER-1: same paper reflagged → still real
- P1A R4 PER-MAJOR-1/2/3/4: Liu, Legner, Alam, Cai-Zhu, Papanikolaou all flagged fictional → all 5 verified real
- P1B R1 PER-B1: `Liu...ECTorsionDESI2025` (2507.04265) → real EPJC 2025
- P1B R1 PER-B2: `Eskilt2022b` flagged fictional → real PRD 106:063503
- P1B R1 PER-B3: `DiegoPalazuelos` PRL 128:091302 → real
- P1B R1 PER-B4: `Fujita+Murai+Nakatsuka+Tsujikawa` → real PRD 103:043509
- P1B R2-R7: Liu, ACT-DR6, DESI-DR2 reflagged 6 consecutive rounds → all real
- P2 R1 PER-B1: `Zhu:2026echoes` (2603.13924) → real arXiv 2026-March
- P2 R3 PER-B2: `Wands:2010` (1004.0818) → real CQG 27:124002
- P3 R1 PER-B1 / R2 PER-B1 / R3 PER-R3-B1: `Heinrich2023` (2311.13082) → real JCAP 2024
- P4 R1 PER-B1-M4: `Shamir:2022DESI` PASP-confab chain → real MNRAS 516, 2281
- P5 R1 PER-B1: `TWebDESI2026` + `ASTRADESI2026` arXiv:2604.* → both real

## Root cause

Perplexity Sonar Pro's web search depends on its real-time index. Three
known failure modes feed this pattern:

1. **Recent papers** (preprint within ~6 months of round date) not yet
   indexed (covered in detail by pattern 012)
2. **In-prep companions** (`Golden2026P*`, `golden_chirality_2026`) with
   no externally-resolvable identity (covered by pattern 006)
3. **Author-name fusion**: Perplexity sometimes finds a paper with similar
   title at a different venue and asserts that the bib entry is "fused"
   when it is actually correct

## Pre-review check

Before any R-round, run this audit:

```bash
# Pseudocode for /paper-pre-review-check skill:
for entry in $(grep '^\\bibitem' paper.bbl | extract_arxiv_ids); do
    expected_metadata=$(curl arxiv.org/abs/$id | parse_metadata)
    bib_metadata=$(grep_authors_title $entry)
    diff $expected $bib || flag_real_drift
done
# Then any Perplexity "fabricated" finding for an arXiv-resolved entry
# is automatically classified FALSIFIED before truth-audit.
```

For in-prep companions, ensure the bbl carries the literal string
"(in preparation)" — Perplexity findings that flag those entries are
classified FALSIFIED automatically (pattern 006).
