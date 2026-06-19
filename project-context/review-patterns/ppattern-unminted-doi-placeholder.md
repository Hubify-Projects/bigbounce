---
pattern_id: ppattern-unminted-doi-placeholder
status: seeded
first_seen: P1-2026-06-19
papers_observed: []
proposed_by: paper-packaging-round 2026-06-19
---

# ppattern-unminted-doi-placeholder — Paper ships with TODO/TBD/placeholder DOI or arXiv ID

## Defect

The paper contains a placeholder where a real DOI or arXiv ID should be:
`\cite{Golden2026P2}` resolving to `(in preparation)`, `arXiv:XXXX.XXXXX`,
`DOI: 10.5281/zenodo.TBD`, or a literal `TODO` in the bibliography. When the
paper is submitted to arXiv, these placeholders are visible to readers as broken
references or editorial artifacts.

## How to detect

```bash
# Find placeholder patterns in the .bbl / .bib
grep -inE 'in preparation|TBD|TODO|XXXX|arXiv:0000|DOI.*TBD|placeholder' paper.bbl paper.bib

# Find companion-paper self-cites that lack real IDs
grep -n 'Golden2026\|golden_.*2026\|in prep' paper.bbl
```

## Fix

Before P-round closes, for each placeholder:
1. **Companion paper already on arXiv**: update the `.bib` entry with the real
   arXiv ID + DOI; regenerate `.bbl`.
2. **Data release not yet minted**: mint the Zenodo release, update the DOI.
3. **True in-prep**: the `.bbl` entry should carry `(in preparation)` literally
   — NOT `arXiv:XXXX` or `DOI: TBD`. Update the cite text in the paper to
   "Golden et al. (in preparation)" and ensure the `.bbl` entry matches.
4. **Cross-citation submission order**: if Paper A cites Paper B's arXiv ID,
   Paper B must be submitted first (see `ppattern-cross-cite-submission-order`).
