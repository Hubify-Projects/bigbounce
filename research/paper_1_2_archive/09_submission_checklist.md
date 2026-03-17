# Paper 1.2 — Submission Checklist

**Date:** 2026-03-14

---

## arXiv Submission

| Item | Status | Notes |
|------|--------|-------|
| Primary category | `gr-qc` | General Relativity and Quantum Cosmology |
| Cross-list categories | `astro-ph.CO`, `hep-th` | Cosmology; High Energy Theory |
| Source format | Single .tex + .bbl | revtex4-2, no external figures |
| Title finalized | YES | "Geometric Dark Energy: Phenomenological Viability, Systematic Closures, and Requirements for Completion" |
| Abstract finalized | YES | 4 paragraphs, ~150 words |
| Author / affiliation | Houston Golden, Independent Researcher, Los Angeles, CA | |
| ORCID | NEEDED | Add if available |
| License | CC-BY-4.0 recommended | |
| Comments field | "31 pages, 6 tables, companion technical note referenced" | |

---

## Journal Submission (PRD)

| Item | Status | Notes |
|------|--------|-------|
| Target journal | Physical Review D | |
| Manuscript type | Regular Article | |
| PACS numbers | 98.80.-k, 04.50.Kd, 04.60.Pp, 95.36.+x | Already in .tex |
| Cover letter | NEEDED | Brief, emphasize mass-coupling lock as new result |
| Suggested referees | NEEDED | 3–4 names in EC/PGT/geometric DE |
| Page limit | None for Regular Article | Currently ~16 PRD pages |

---

## Pre-submission Checks

### Content
- [x] No TODO/FIXME/DRAFT markers
- [x] No placeholder text (except acknowledgments — update before submit)
- [ ] Acknowledgments finalized
- [ ] DiegoPalazuelos2025 arXiv ID added
- [ ] Legner2025 arXiv ID (2507.09228) verified
- [x] All cross-references resolve (10 equations, 6 tables, all sections)
- [x] No orphan bibliography entries
- [x] Claims table (Appendix C) consistent with text

### Figures / Tables
- [x] No external figure files required
- [x] 6 tables compile correctly
- [x] Table captions are self-contained
- [x] No color-dependent content (accessible in B&W)

### Bibliography
- [x] 29 bibitems, all cited
- [x] No orphan entries (Hehl1976 removed)
- [ ] DiegoPalazuelos2025: add arXiv ID when available
- [ ] Legner2025: verify arXiv:2507.09228
- [x] Fabbri2025: arXiv:2502.17979 confirmed
- [x] All journal refs have volume/page/year

### Compilation
- [x] Compiles with tectonic (0 errors)
- [x] Compiles with revtex4-2
- [x] PDF size: 184 KiB
- [x] Only cosmetic warnings (underfull hbox, duplicate table labels from multi-pass)

---

## Reproducibility

| Claim | Artifact | Location |
|-------|----------|----------|
| MCMC fits | Cobaya configs + chain summaries | `reproducibility/cosmology/` |
| Convergence diagnostics | CSV + chain diagnostics | `reproducibility/cosmology/` |
| Foundation A Phase 1 | 6 analysis docs + notebook | `research/foundation_A_pgt/` |
| Foundation A Phase 2 | 13 analysis docs | `research/foundation_A_pgt/phase2/` |
| Minimal-model closures | Companion technical note | Cited as Golden2026supplement |

---

## Companion Paper Cross-reference

The companion technical note (Golden2026supplement) is cited 3 times:
1. Section 2.3 — perfect-square structure of four-fermion term
2. Section 4 — detailed closure documentation
3. Section 5 — closure results reference

**Before submission:** Ensure the companion note is available (arXiv preprint or supplemental material upload). If submitted as supplemental material to PRD, update the bibitem to reflect this.

---

## Submission Sequence

1. Finalize acknowledgments
2. Fix DiegoPalazuelos2025 citation
3. Verify Legner2025 arXiv ID
4. Final prose read-through
5. Circulate to 1–2 readers (1 week)
6. Incorporate feedback
7. Upload companion note to arXiv
8. Submit paper to arXiv (gr-qc, cross-list astro-ph.CO + hep-th)
9. Submit to PRD with cover letter
