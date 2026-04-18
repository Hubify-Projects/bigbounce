# arXiv Submission Kit — Houston's 15-min web-form cheat sheet

**Generated:** fire #55 (2026-04-18) from `project-context/peer-reviews/autonomous-2026-04-18/06_arxiv_production_editor.md`

For each paper: trimmed plain-text abstract lives **alongside the tarball** as `abstract_for_webform.txt`. This file aggregates titles (with `\\` stripped), categories, comment strings, and the post-submission checklist so Houston can copy-paste through all four web forms without leaving this document.

**Recommended submission order** (per editor audit §Verdict): Paper 4 → Paper 1 → Paper 3 → Paper 2. Paper 4 has the fewest cross-cites (1: `Golden:2026framework`); Paper 1 is the citation root; submit Papers 3 + 2 after Paper 1 has an arXiv ID so their cross-cites can be rewired (see `arxiv_id_substitution_plan.md`).

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
  27 pages, 3 figures, 1 table, 57 references; companion to arXiv:PAPER2-ID (f_NL forecast), arXiv:PAPER3-ID (anomaly catalog), arXiv:PAPER4-ID (chirality catalog). MCMC chains + code at https://github.com/Hubify-Projects/bigbounce.
  ```
- **Readiness (editor grade):** A (ready to submit today; no blockers)

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
  14 pages, 6 figures, 4 tables, 23 references; companion to arXiv:PAPER1-ID (spin-torsion framework), arXiv:PAPER3-ID (anomaly tracer catalog). Tests the matter-bounce prediction f_NL = -35/8 with SPHEREx + MegaMapper. Code + Fisher config at https://github.com/Hubify-Projects/bigbounce.
  ```
- **Readiness:** B+ per editor; fire #36 trimmed abstract + fire #42 tarball-with-bbl closed blockers — effectively A now.

---

## Paper 3 — Multi-Survey Anomaly Catalog

- **Tarball:** `pipelines/p3_anomaly_engine/paper3_arxiv_submission.tar.gz` (27.6 MB)
- **Abstract webform:** `pipelines/p3_anomaly_engine/abstract_for_webform.txt` (1,480 chars, 440 headroom)
- **Title (paste, `\\` stripped and `{,}` replaced with plain comma):**
  ```
  Multi-Survey Spectral Anomaly Detection: 319,000 Uncataloged Objects from 37 Million Sources Across Eight Astronomical Archives
  ```
- **Authors:** `Houston Golden`
- **Primary:** `astro-ph.IM`
- **Cross-list:** `astro-ph.CO`, `astro-ph.GA`
- **License:** arXiv.org perpetual, non-exclusive license
- **Comment (paste):**
  ```
  27 pages, 21 figures, 4 tables, 38 references; first multi-survey anomaly catalog at >37M-source scale; companion to arXiv:PAPER1-ID (bounce framework), arXiv:PAPER2-ID (f_NL forecast), arXiv:PAPER4-ID (chirality catalog). Catalog available at https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog (CC-BY-4.0); code at https://github.com/Hubify-Projects/bigbounce.
  ```
- **Readiness:** B per editor; tarball built fire #43 + abstract trimmed fire #37 — effectively A-. Remaining open: `P3-HF-UPLOAD` (HF dataset not yet live; can still submit and update data-availability after HF upload).
- **Caveat:** If `P3-HF-UPLOAD` not done at submit time, change comment URL to github only.

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
  11 pages, 11 figures, 4 tables, 23 references; 8.47M-galaxy chirality catalog with D4 test-time equivariance; dipole null 0.43σ; Shamir 2020/2022 3% asymmetry claim refuted at 7×. Catalog at https://huggingface.co/datasets/bamfai/galaxy-chirality-catalog (CC-BY-4.0, v2026.04); model at https://huggingface.co/bamfai/galaxy-chirality-v2; companion to arXiv:PAPER1-ID (bounce framework).
  ```
- **Readiness:** B per editor; fire #39 tarball build + fire #38 abstract trim closed the two P1 blockers — effectively A. Remaining open: Houston-owned `P4-D4-VS-Z2-RENAME` (mechanical rename decision).

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
   - **Comment:** paste from per-paper section above (replace `PAPERN-ID` with real arXiv IDs for already-submitted companion papers)
   - **Report-no / MSC / ACM / Journal-ref / DOI:** blank
9. **Final review** → submit
10. **Record arXiv ID** in `project-context/SSOT/paper-N/status.md` under new "arXiv submission" section
11. **After announcement** (daily at 20:00 UTC; Monday 00:00 UTC): update remaining in-flight papers' `\bibitem{Golden:2026...}` placeholders per `arxiv_id_substitution_plan.md`

---

## References

- Editor audit: `project-context/peer-reviews/autonomous-2026-04-18/06_arxiv_production_editor.md`
- Cross-cite rewire plan: `project-context/peer-reviews/autonomous-2026-04-18/arxiv_id_substitution_plan.md`
- SSOT dashboard: `project-context/SSOT/index.md`
- Per-paper status: `project-context/SSOT/paper-{1,2,3,4}/status.md`
