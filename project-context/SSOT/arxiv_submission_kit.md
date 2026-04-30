# arXiv Submission Kit — Houston's 15-min web-form cheat sheet

**Generated:** fire #55 (2026-04-18) from `project-context/peer-reviews/autonomous-2026-04-18/06_arxiv_production_editor.md`

For each paper: trimmed plain-text abstract lives **alongside the tarball** as `abstract_for_webform.txt`. This file aggregates titles (with `\\` stripped), categories, comment strings, and the post-submission checklist so Houston can copy-paste through all four web forms without leaving this document.

**Submission order — relaxed as of R41 (2026-04-30).** All 4 papers were decoupled in R41 — 28 `\cite{Golden:2026...}` cross-references were eliminated and replaced with primary-source citations (Heinrich+2023, Lentati+2013/2023, WilsonEwing+2012, Mercuri+2006, Freidel+2005, Poplawski+2012/2016, Eskilt+2022, Diego-Palazuelos+2025, Minami+2020, Cai+2026, Baron+2017, Liang+2023). Each paper stands on its own; the editor's earlier "submit Paper 1 first to anchor IDs for Papers 2/3/4" recommendation is no longer load-bearing. Houston may submit in any order. The historical `arxiv_id_substitution_plan.md` workflow is obsolete for these four papers — no `Golden:2026*` placeholders remain in any of the four `.tex` files or bibliographies.

---

## Paper 1 — Spin-Torsion Cosmology

- **Tarball:** `arxiv/main_arxiv_submission.tar.gz` (441 KB)
- **Abstract webform:** `arxiv/abstract_for_webform.txt` (1,536 chars, 384 headroom)
- **Title (paste, `\\` stripped):**
  ```
  Spin-Torsion Cosmology and the Search for Geometric Dark Energy: Structural Barriers, Perturbation Transparency, and Surviving Predictions
  ```
- **Authors:** `Houston Golden`
- **Primary:** `astro-ph.CO`
- **Cross-list:** `gr-qc`, `hep-th`
- **License:** arXiv.org perpetual, non-exclusive license
- **Comment (paste):**
  ```
  27 pages, 3 figures, 1 table, 57 references. MCMC chains + code at https://github.com/Hubify-Projects/bigbounce.
  ```
- **Readiness (editor grade):** A (ready to submit today; no blockers; R41 decoupled — self-contained)

---

## Paper 2 — f_NL Forecast

- **Tarball:** `research/focused_paper_source_integration/paper2_arxiv_submission.tar.gz` (311 KB, includes `.bbl` per fire #42)
- **Abstract webform:** `research/focused_paper_source_integration/abstract_for_webform.txt` (1,690 chars, 230 headroom)
- **Title (paste, `\\` stripped):**
  ```
  Testing the Matter Bounce with Primordial Non-Gaussianity: Forecasts for SPHEREx and MegaMapper
  ```
- **Authors:** `Houston Golden`
- **Primary:** `astro-ph.CO`
- **Cross-list:** `astro-ph.IM`
- **License:** arXiv.org perpetual, non-exclusive license
- **Comment (paste):**
  ```
  14 pages, 6 figures, 4 tables, 23+ references. Tests the matter-bounce prediction f_NL = -35/8 with SPHEREx + MegaMapper. Code + Fisher config at https://github.com/Hubify-Projects/bigbounce.
  ```
- **Readiness:** A (R41 decoupled — self-contained; trimmed abstract + tarball-with-bbl closed all earlier editor blockers).

---

## Paper 3 — Multi-Survey Anomaly Catalog

- **Tarball:** `pipelines/p3_anomaly_engine/paper3_arxiv_submission.tar.gz` (27.6 MB)
- **Abstract webform:** `pipelines/p3_anomaly_engine/abstract_for_webform.txt` (1,480 chars, 440 headroom)
- **Title (paste, `\\` stripped and `{,}` replaced with plain comma):**
  ```
  Multi-Survey Spectral Anomaly Detection: 378,000 Anomalous Sources from 37 Million Objects Across Eight Astronomical Archives
  ```
- **Authors:** `Houston Golden`
- **Primary:** `astro-ph.IM`
- **Cross-list:** `astro-ph.CO`, `astro-ph.GA`
- **License:** arXiv.org perpetual, non-exclusive license
- **Comment (paste):**
  ```
  27 pages, 21 figures, 4 tables, 38 references. First multi-survey anomaly catalog at >37M-source scale. Catalog available at https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog (CC-BY-4.0); code at https://github.com/Hubify-Projects/bigbounce.
  ```
- **Readiness:** A (R41 decoupled — self-contained; tarball + trimmed abstract closed earlier editor concerns). Remaining: HF dataset upload (can still submit and update data-availability after).
- **Caveat:** If HF dataset not live at submit time, change comment URL to github only.

---

## Paper 4 — Galaxy Chirality Catalog

- **Tarball:** `pipelines/p2_chirality/chirality_catalog_paper_arxiv_submission.tar.gz` (19 MB, includes `.bbl` + 11 figures per fire #39)
- **Abstract webform:** `pipelines/p2_chirality/abstract_for_webform.txt` (1,656 chars, 264 headroom)
- **Title (paste, `\\` stripped):**
  ```
  No Evidence for Large-Scale Parity Violation in Galaxy Morphology: A Survey-Scale Chirality Catalog of 8.47 Million Galaxies
  ```
- **Authors:** `Houston Golden`
- **Primary:** `astro-ph.CO`
- **Cross-list:** `astro-ph.GA`, `astro-ph.IM`
- **License:** arXiv.org perpetual, non-exclusive license
- **Comment (paste):**
  ```
  11 pages, 11 figures, 4 tables, 23 references. 8.47M-galaxy chirality catalog with D4 test-time equivariance; dipole null 0.43σ; Shamir 2020/2022 3% asymmetry claim refuted by factor of 9 (paper-canonical max regional asymmetry 0.32%). Catalog at https://huggingface.co/datasets/bamfai/galaxy-chirality-catalog (CC-BY-4.0, v2026.04); model at https://huggingface.co/bamfai/galaxy-chirality-v2.
  ```
- **Readiness:** A (R41 decoupled — self-contained; tarball + trimmed abstract closed earlier blockers). Remaining open: Houston-owned `P4-D4-VS-Z2-RENAME` (mechanical rename decision).

---

## On-form submission sequence (identical for all 4)

1. **Login** → arxiv.org/user/login
2. **Start new submission**
3. **License:** arXiv.org perpetual, non-exclusive (default)
4. **Primary archive:** per table above → `astro-ph` → subcategory
5. **Cross-lists:** add all from per-paper list above
6. **Upload tarball** → AutoTeX runs 30-90s
7. **Preview PDF** → verify figure count + page count + refs
8. **Metadata page:**
   - **Title:** paste from this file (already has `\\` stripped)
   - **Authors:** `Houston Golden`
   - **Abstract:** paste from the paper's `abstract_for_webform.txt`
   - **Comment:** paste from per-paper section above (R41 decoupled — no `PAPERN-ID` placeholders; comment is final as-is)
   - **Report-no / MSC / ACM / Journal-ref / DOI:** blank
9. **Final review** → submit
10. **Record arXiv ID** in `project-context/SSOT/paper-N/status.md` under new "arXiv submission" section
11. **After announcement** (daily at 20:00 UTC; Monday 00:00 UTC): no cross-paper bibitem rewiring needed — papers are decoupled (R41, 2026-04-30). The `arxiv_id_substitution_plan.md` workflow is obsolete for these four papers.

---

## References

- Editor audit: `project-context/peer-reviews/autonomous-2026-04-18/06_arxiv_production_editor.md`
- Cross-cite rewire plan: `project-context/peer-reviews/autonomous-2026-04-18/arxiv_id_substitution_plan.md`
- SSOT dashboard: `project-context/SSOT/index.md`
- Per-paper status: `project-context/SSOT/paper-{1,2,3,4}/status.md`
