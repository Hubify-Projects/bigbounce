# Paper 1.2 — Submission Checklist

**Date:** 2026-03-14

---

## arXiv Package

| Item | Status |
|------|--------|
| Source file (`main.tex`) present | **DONE** |
| Compiles with tectonic (TeX Live) | **DONE** — 0 errors, 187 KiB |
| No external figure files needed | **DONE** — no figures |
| No external .bib file needed | **DONE** — inline bibliography |
| No custom .sty files needed | **DONE** — all standard packages |
| Unused package `bbold` removed | **DONE** |
| Unused macro `\paperVersion` removed | **DONE** |
| No TODO/FIXME/draft markers | **DONE** |
| Metadata file prepared | **DONE** — `arxiv_metadata.md` |
| Compilation check documented | **DONE** — `arxiv_compile_check.md` |
| Primary category: gr-qc | **DONE** |
| Cross-lists: hep-th, astro-ph.CO | **DONE** |

**arXiv bundle location:** `submission/arxiv_paper_1_2/`

---

## Journal Package (JCAP)

| Item | Status |
|------|--------|
| Source file (`paper_1_2.tex`) present | **DONE** |
| Compiled PDF present | **DONE** — `paper_1_2.pdf` |
| Cover letter prepared | **DONE** — `cover_letter.md` |
| revtex4-2 format (JCAP accepts) | **DONE** |

**Journal bundle location:** `submission/journal_paper_1_2/`

---

## Bibliography Verification

| Item | Status |
|------|--------|
| 29 bibitems, all cited | **DONE** |
| No orphan bibliography entries | **DONE** |
| All `\cite` keys have matching `\bibitem` | **DONE** |
| DiegoPalazuelos2025 — arXiv ID | **OPEN** — entry reads "(2025)", no ID |
| Legner2025 — arXiv ID verification | **OPEN** — 2507.09228 flagged for verification |
| Golden2026supplement — companion note | **OPEN** — must be posted to arXiv before/with submission |
| Golden2026v1 — superseded preprint | OK — internal reference |

---

## Cross-Reference Verification

| Reference type | Count | Status |
|----------------|-------|--------|
| Equation labels (`\label{eq:*}`) | 10 | All referenced or contextually adjacent |
| Table labels (`\label{tab:*}`) | 6 | All referenced or contextually adjacent |
| Section labels (`\label{sec:*}`) | 17 | All referenced |
| Appendix labels (`\label{app:*}`) | 3 | All referenced |

**No undefined references. No orphan labels.**

---

## Figure Format Check

No figures in the paper. All data presented in tables. N/A.

---

## Abstract Consistency

| Claim in abstract | Verified in body? |
|-------------------|-------------------|
| Five closures reported | Yes — Secs. 5.1-5.4 + 8.1 |
| Fine-tuning 10^120 → 10^5 | Yes — Sec. 3.1, Table IV |
| H₀ and σ₈ tension reduction | Yes — Eqs. 6-8, Sec. 3.2.3 |
| Mass-coupling lock (10^29 suppression) | Yes — Sec. 6.6, Eq. 9, Sec. 8.1 |
| Six structural lessons | Yes — Sec. 6 |
| Requirements framework | Yes — Sec. 7 (DR1-DR5) |

---

## Companion Closure Paper

| Item | Status |
|------|--------|
| Cited in introduction | **DONE** — line 167 |
| Cited in Sec. 2.3 (perfect-square structure) | **DONE** — line 228 |
| Cited in Sec. 4 (derivation program) | **DONE** — lines 480, 510 |
| Bibitem entry exists | **DONE** — line 1342 |
| arXiv ID for companion note | **OPEN** — must be posted first |

---

## Pre-Submission Actions Required

1. **Fix DiegoPalazuelos2025 citation** — add arXiv ID when available
2. **Verify Legner2025 arXiv ID** — confirm 2507.09228 is correct
3. **Upload companion technical note** to arXiv before or simultaneously
4. **Update Golden2026supplement bibitem** with arXiv ID once posted
5. **Collect circulation feedback** and incorporate if any

---

## Submission Sequence

```
1. Post companion note to arXiv
2. Update bibitem with companion arXiv ID
3. Fix DiegoPalazuelos2025 if ID available
4. Verify Legner2025 ID
5. Recompile main.tex
6. Submit to arXiv (gr-qc, cross-list hep-th + astro-ph.CO)
7. Submit to JCAP with cover letter
```

---

## Summary

| Component | Ready? |
|-----------|--------|
| arXiv source bundle | **YES** |
| arXiv metadata | **YES** |
| Journal source + PDF | **YES** |
| Cover letter | **YES** |
| Bibliography | **YES** (2 IDs to verify) |
| Cross-references | **YES** |
| Abstract consistency | **YES** |
| Companion paper link | **NEEDS arXiv ID** |

**Overall status: READY TO SUBMIT** pending companion note upload and two citation verifications.
