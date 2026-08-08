---
pattern_id: ppattern-stale-bbl
status: seeded
first_seen: P1-2026-06-19
papers_observed: []
proposed_by: paper-packaging-round 2026-06-19
---

# ppattern-stale-bbl — Tarball ships a stale .bbl (not regenerated from current .bib)

## Defect

The arXiv submission tarball contains a `.bbl` file that was generated from a
previous version of the `.bib` file. Entries added, removed, or edited after the
last `bibtex` run are missing or incorrect in the tarball's bibliography. arXiv
compiles from the tarball's `.bbl` directly (it does not re-run BibTeX), so the
published paper has wrong or missing references.

## How to detect

```bash
# Compare .bbl mtime vs .bib mtime
ls -lt paper.bbl paper.bib

# Or diff the .bbl against a fresh bibtex run
cp paper.bbl paper.bbl.old
bibtex paper
diff paper.bbl.old paper.bbl
```

Any diff output means the `.bbl` is stale.

## Fix

As the first step of every P-round tarball rebuild:
1. Run `bibtex paper` (or `biber paper` for biblatex) from scratch in the paper directory.
2. Run `pdflatex` twice to resolve cross-references.
3. Confirm `paper.bbl` mtime is newer than `paper.bib`.
4. Include the freshly-generated `.bbl` (not `.bib`) in the tarball.
5. STANDALONE-compile-verify: extract the tarball into a fresh temp dir and
   run `pdflatex` from zero — confirm 0 undefined citation warnings.
