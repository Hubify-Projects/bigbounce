# arXiv Production Editor — Readiness Audit

**Auditor:** Autonomous arXiv production editor (agent pass 06, 2026-04-18)
**Scope:** Tarball integrity, figure resolution, bibliography completeness, package compatibility, category selection, submission-form checklist.
**Source of ground-truth status:** `project-context/SSOT/index.md` + per-paper `SSOT/paper-N/status.md` (all timestamped 2026-04-17, fire #9).

**Global observations on the program:**
- All four `.tex` sources use `revtex4-2` (PRD style). Good — consistent production look.
- All four have Houston Golden / Independent Researcher / `houston@hubify.com` author block. Good.
- `\usepackage{hyperref}` is standard — arXiv renders metadata from `\title{}` + `\author{}` directly; no extra `\hypersetup{}` needed.
- No `minted`, no `shell-escape`, no custom local `.sty` files. All packages are in `revtex4-2` + standard TeX Live (amsmath, amssymb, amsfonts, graphicx, bm, hyperref, xcolor, booktabs, multirow, dcolumn, enumitem, mathtools, bbold, inputenc, float, slashed). arXiv TeX Live has all of these. The only not-quite-universal entry is `bbold` (Paper 1) — arXiv has it, but a pod compile of Paper 1 in fire #9 had to explicitly pull `texlive-fonts-extra` for `bbold.sty`. On arXiv's AutoTeX this is resolved automatically.
- No EPS figures in any paper — all `.pdf` or `.png`. Good — no EPS-to-PDF conversion needed.
- `\date` fields are mixed: P1 April 13 2026, P2 `\today`, P3 April 15 2026, P4 March 28 2026 — arXiv re-stamps on submission, so these are cosmetic but Houston may want to unify to submission date during form fill.

---

## Per-paper checklist

### Paper 1 — Spin-Torsion Cosmology (`arxiv/main.tex`)

- **Tarball path:** `arxiv/main_arxiv_submission.tar.gz` (441 KB, 2026-04-17, built fire #9)
- **Files included (verified via `tar tzf`):**
  - `main.tex`
  - `main.bbl` (40 KB, 57 bibitems)
  - `references.bib` (NOT strictly needed by arXiv once .bbl is present — arXiv prefers .bbl; either is fine but having both is safe)
  - `figures/figure1_lqg_holst_derivation_enhanced.png`
  - `figures/consistency_window_birefringence.pdf`
  - `figures/paper1_corner_full_tension.pdf`
- **Missing:** None of the 3 `\includegraphics` targets are missing. All resolve. **However:** `arxiv/figures/` on disk has 14 figures — only 3 are referenced by the current `main.tex` (the paper was trimmed). Good — tarball is minimal. Unreferenced figures are NOT included — no bloat.
- **Extras to flag:** The tarball includes `references.bib`. arXiv will re-run BibTeX if it sees a `.bib`. Since the `.bbl` is already committed, having `.bib` is redundant but not harmful. Recommend keeping `.bbl` + `.bib` both (safer against AutoTeX quirks).
- **Predicted clean compile:** `pdflatex → bibtex → pdflatex × 2` on arXiv AutoTeX. SSOT says fire #9 on-pod smoke test (440 KB tarball → 945 KB PDF) passed with 0 undefined refs. `bbold` is in standard arXiv TeX Live — fine. Figures embedded: confirmed by 945 KB PDF size.
- **Predicted warnings:** Possible overfull/underfull hboxes in revtex two-column layout with long URLs in bibitems — cosmetic, not a reject.
- **Primary category:** `astro-ph.CO` (cosmology + MCMC is the load-bearing content)
  - **Secondary (cross-list):** `gr-qc` (Einstein-Cartan gravity, LQC, Barbero-Immirzi is core), `hep-th` (parity-violation + Holst action is theoretical physics framing)
  - **Justification:** Paper is a synthesis of (a) theoretical GR/quantum-gravity structure, (b) observational cosmology MCMC, and (c) particle-physics-adjacent spectator-ALP calc. Primary `astro-ph.CO` is correct because the falsifiable output is a cosmological observable ($f_{\rm NL}$, $\Delta N_{\rm eff}$, $\beta$). `gr-qc` is the proper home for the spin-torsion/LQC formalism. `hep-th` for spectator-ALP + parity.
- **Abstract char count:** **1,641 chars** (body between `\begin{abstract}`/`\end{abstract}`, verbatim, LaTeX macros included). arXiv limit is 1,920. **PASS** with ~280-char headroom. LaTeX macros (`$\rho_{\rm crit}$`, `$\Delta\Neff$`) should render safely — arXiv's abstract box accepts simple math; if it rejects, strip macros to plain text for the web form only.
- **Comment string (ready to paste):**

  > 27 pages, 3 figures, 1 table, 57 references; companion to arXiv:PAPER2-ID (f_NL forecast), arXiv:PAPER3-ID (anomaly catalog), arXiv:PAPER4-ID (chirality catalog). MCMC chains + code at https://github.com/Hubify-Projects/bigbounce.

- **Data-availability statement:** ✓ PRESENT (GitHub + MCMC chains + chirality catalog HF link referenced in §VI). Strength: 4/5. Could add explicit line-item for the Cobaya YAML configs in `reproducibility/cosmology/` — minor polish.
- **License recommendation:** `arXiv.org perpetual, non-exclusive` + code/data already CC-BY-4.0 on HuggingFace. For arXiv's license menu, choose "arXiv.org perpetual, non-exclusive license" (the default). Do not pick `CC BY 4.0` on the arXiv form itself unless you want the PDF itself to be CC-BY — the bibliography/code/data being CC-BY is separate and documented in the data-availability block.
- **PDF metadata (title/author) macro safety:** `\title{Spin-Torsion Cosmology and the Search for Geometric Dark Energy:\\ ...}` — has `\\` inside title. arXiv's metadata scraper sometimes trips on `\\`; safer to replace the `\\` with a space when filling the web form's title field (do not edit the `.tex` title — just the form field).
- **Blockers:** None. The tarball passed a clean-revtex smoke test on 2026-04-17. Recommend minor cosmetic refresh of `\paperTimestamp` from 2026-04-13 to submission date (30-sec edit), but not a blocker.
- **Readiness grade:** **A (ready to submit today).**

---

### Paper 2 — f_NL Forecast (`research/focused_paper_source_integration/02_full_draft.tex`)

- **Tarball path:** `research/focused_paper_source_integration/paper2_arxiv_submission.tar.gz` (311 KB, 2026-04-17)
- **Files included (verified):**
  - `02_full_draft.tex`
  - `focused_paper_refs.bib` (7.1 KB)
  - `fig1_shape_function.png`, `fig2_survey_comparison.png`, `fig3_kmin_cliff.png`, `fig4_decision_thresholds.png`, `fig5_inflation_comparison.png`
  - `bphi_sensitivity.pdf`
- **Missing:**
  - **No `.bbl` in tarball.** The `.tex` uses `\bibliography{focused_paper_refs}` (external .bib) — so arXiv will need to run bibtex. If the `.bib` entries have no errors, this is fine, but it adds a failure mode (a mistyped bibkey can silently become `[?]`). **Recommend rebuilding the tarball to include `02_full_draft.bbl`** (exists on disk at 10 KB, generated 2026-04-17) so arXiv can bypass bibtex entirely. SIMPLE FIX: add `.bbl` to tarball.
- **Extras to flag:** None.
- **Predicted clean compile:** Fire #9 SSOT confirms on-pod compile produced a 614 KB PDF with 0 undefined references. On arXiv AutoTeX: `pdflatex → bibtex → pdflatex × 2` should match. Risk: an arXiv AutoTeX bibtex run disagrees with the pod's local run. Mitigation: ship the .bbl.
- **Primary category:** `astro-ph.CO` (Fisher forecast for a cosmological observable)
  - **Secondary (cross-list):** `astro-ph.IM` (methodology: multi-tracer bispectrum, systematic-fragility analysis is instrumentation-adjacent)
  - **Justification:** This is a targeted forecast for a specific cosmological prediction ($f_{\rm NL} = -35/8$) against SPHEREx + MegaMapper. Primary `astro-ph.CO` is unambiguous. `astro-ph.IM` is the correct cross-list because the paper's §7 systematic-fragility treatment is method-heavy (photo-z degradation, $b_\phi$ sensitivity). Do NOT cross-list `gr-qc` — the bounce-theory is companion-paper material, not this paper's content.
- **Abstract char count:** **2,273 chars.** **⚠ OVER LIMIT.** Arxiv abstract form field limit is 1,920 chars. This abstract will need a ~353-char trim before form submission. The LaTeX abstract in the PDF can stay verbatim — only the arXiv web-form field needs trimming. **BLOCKER for form submission — 15-min fix.** Trim targets: the 600K-MC Bayesian-sample detail (move to body only), the "assumptions (a)–(e)" coda, the photo-z/degradation list.
- **Comment string (ready to paste):**

  > 14 pages, 6 figures, 4 tables, 23 references; companion to arXiv:PAPER1-ID (spin-torsion framework), arXiv:PAPER3-ID (anomaly tracer catalog). Tests the matter-bounce prediction f_NL = -35/8 with SPHEREx + MegaMapper. Code + Fisher config at https://github.com/Hubify-Projects/bigbounce.

- **Data-availability statement:** ✓ PRESENT per SSOT (GitHub URL, explicit script list). Strength: 4/5.
- **License recommendation:** arXiv perpetual non-exclusive. Code + data already CC-BY-4.0.
- **PDF metadata:** `\title{Testing the Matter Bounce with Primordial Non-Gaussianity:\\ ...}` — same `\\` issue as Paper 1; strip `\\` from the web form's title field.
- **Blockers:**
  1. Abstract > 1920 chars — trim before filling the arXiv web form.
  2. Tarball should include `.bbl` (exists on disk; just needs to be added).
- **Readiness grade:** **B+ (ready after 30-min fix: trim abstract + rebuild tarball with .bbl).**

---

### Paper 3 — Multi-Survey Anomaly Catalog (`pipelines/p3_anomaly_engine/paper3_draft.tex`)

- **Tarball path:** **NONE EXISTS.** SSOT queue P3-TARBALL implied but not yet built. The 27 MB PDF is in `public/papers/paper3_anomaly_catalog.pdf` but no `.tar.gz` companion exists under `pipelines/p3_anomaly_engine/`.
- **Files that need to be in the tarball (when built):**
  - `paper3_draft.tex` (80.6 KB, 1,032 lines)
  - **38 embedded `\bibitem` entries** (no external .bib — bibliography is inlined; **NO `.bbl` needed**)
  - `figures/` — **21 PDF files + 1 PNG** referenced by `\includegraphics`:
    - `figures/fig_architecture.pdf`
    - `figures/fig_example_spectra.pdf`
    - `figures/fig_skymap_all_surveys.pdf`
    - `figures/fig_score_distributions.pdf`
    - `figures/fig_gallery_A1_highz_qso.pdf`
    - `figures/fig_sdss_umap.png` (only PNG)
    - `figures/fig_lamost_blue_excess.pdf`
    - `figures/fig_neowise_top_anomaly.pdf`
    - `figures/fig_novelty_fractions.pdf`
    - `figures/fig_cross_survey_matches.pdf`
    - `figures/fig_fnl_improvement.pdf`
    - `figures/fig_nanograv_fit.pdf`
    - `figures/fig_gallery_top10.pdf`
    - `figures/fig_gallery_a2_qso.pdf`
    - `figures/fig_gallery_a3_agn.pdf`
    - `figures/fig_gallery_a4_bal_qso.pdf`
    - `figures/fig_gallery_a5_elg.pdf`
    - `figures/fig_gallery_a6_lrg.pdf`
    - `figures/fig_gallery_a7_post_starburst.pdf`
    - `figures/fig_gallery_a8_blue_compact.pdf`
    - `figures/fig_gallery_a9_star.pdf`
    - `figures/fig_gallery_a10_unknown.pdf`
- **Missing:** All referenced figures EXIST on disk in `pipelines/p3_anomaly_engine/figures/`. The directory additionally contains `.png` duplicates of every `.pdf` figure (used by site/html surface) and a `_cutout_cache` subdirectory — these should NOT be in the tarball. When building the tarball, be selective: include only the 22 files enumerated above.
- **Extras to exclude on build:**
  - `paper3_draft.aux`, `paper3_draft.log`, `paper3_draft.out`, `paper3_draftNotes.bib` (empty stub, 104 B), `paper3_draft.pdf` itself
  - `figures/*.png` duplicates where `.pdf` exists
  - `figures/_cutout_cache/` (scratch dir)
- **Predicted clean compile:** SSOT says fire #9 on-pod produced 27 MB / 27 pp / 0 undef. Embedded `\bibitem` (no external bib) means arXiv AutoTeX only runs `pdflatex × 2` — no bibtex step, lower failure surface. Good.
- **Predicted warnings:** The PDF is 27 MB — well under arXiv's 50 MB tarball limit but figures should be checked for unnecessarily large raster fallbacks. The 21 PDF figures already total ~25 MB (file-level audit). Acceptable but near arXiv's soft "please compress" threshold.
- **Primary category:** `astro-ph.IM` (methodology-forward: BigAE architecture, training regime, cross-survey pipeline, validation)
  - **Secondary (cross-list):** `astro-ph.CO` ($f_{\rm NL}$ multi-tracer forecast § 5 + NANOGrav GWB analysis § 6 are cosmology), `astro-ph.GA` (DESI/SDSS/LAMOST anomaly science is extragalactic objects)
  - **Justification:** Primary `astro-ph.IM` because the paper's load-bearing novelty is the autoencoder + cross-survey methodology applied at 37M-source scale. The cosmology results (§5, §6) are downstream applications. `astro-ph.CO` cross-list is mandatory to reach the f_NL/PTA audience. `astro-ph.GA` cross-list is appropriate because the galaxy-anomaly catalog is of direct interest to extragalactic readers.
- **Abstract char count:** **2,194 chars.** **⚠ OVER LIMIT** (arXiv 1,920). Needs ~274-char trim for the web form field only. Tightest targets: the survey-by-survey breakdown ("195,829 from 22.5M spectra..." etc.) can be moved from abstract prose to Table 1 in the body, leaving a one-line aggregate in the abstract. 20-min fix.
- **Comment string (ready to paste):**

  > 27 pages, 21 figures, 4 tables, 38 references; first multi-survey anomaly catalog at >37M-source scale; companion to arXiv:PAPER1-ID (bounce framework), arXiv:PAPER2-ID (f_NL forecast), arXiv:PAPER4-ID (chirality catalog). Catalog available at https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog (CC-BY-4.0); code at https://github.com/Hubify-Projects/bigbounce.

  **Caveat:** SSOT says `P3-HF-UPLOAD` is NOT yet done. The abstract and data-availability statement currently say "will be released as a community data product." Either upload to HF before submission (preferred) or change the URL in the comment to `https://github.com/Hubify-Projects/bigbounce` only.
- **Data-availability statement:** ✓ PRESENT (GitHub + "publicly available upon acceptance" language). **⚠ Recommend:** strengthen by going live with HF catalog before submission (SSOT task `P3-HF-UPLOAD`). "Upon acceptance" is weak — better to have the URL live on day 1.
- **License recommendation:** arXiv perpetual non-exclusive. HF catalog CC-BY-4.0.
- **PDF metadata:** `\title{Multi-Survey Spectral Anomaly Detection: 319{,}000 Uncataloged Objects\\ ...}` — `\\` present; strip from web-form title. The `{,}` around 319,000 will render fine in the PDF but may display as literal braces in the arXiv title listing — safer to write "319,000" plain in the web form.
- **Blockers:**
  1. Tarball does not exist — must be built. Task `P3-TARBALL-BUILD` (P1).
  2. Abstract > 1920 chars — trim for web form.
  3. `P3-HF-UPLOAD` not done — data-availability link is promissory; make it live.
- **Readiness grade:** **B (ready after 2-hour fix: build tarball + trim abstract + upload HF dataset).**

---

### Paper 4 — Galaxy Chirality Catalog (`pipelines/p2_chirality/chirality_catalog_paper.tex`)

- **Tarball path:** **NONE EXISTS.** The 25 MB PDF is in `public/papers/chirality_catalog_paper.pdf` but no `.tar.gz` companion exists.
- **Files that need to be in the tarball (when built):**
  - `chirality_catalog_paper.tex` (48.8 KB, 1,099 lines)
  - `chirality_catalog_paper.bbl` (2.0 KB, present on disk at `pipelines/p2_chirality/chirality_catalog_paper.bbl` — `apsrev4-2.bst` hand-edited format)
  - **OR** embedded bibliography: 23 `\bibitem` entries ARE inlined in the `.tex` (including `Golden:2026framework` at L1040). Since both exist, arXiv will prefer the `.bbl` for faster processing. Ship the `.bbl`.
  - `fig_class_pie.png`
  - `fig_confidence_dist.png`
  - `fig_equivariance_demo.png`
  - `fig_gallery_ccw.png`
  - `fig_gallery_cw.png`
  - `fig_hemisphere.png`
  - `fig_multipoles.png`
  - `fig_raw_vs_eq.png`
  - `fig_sky_map.png`
  - `fig_sky_regions.png`
  - `fig_spiral_density.png`
- **Missing (CRITICAL):** **All 11 figures are referenced as `\includegraphics[width=\columnwidth]{fig_*.png}` with NO `figures/` prefix.** The `.tex` assumes figures are co-located with the `.tex`. **NONE of the figures exist in `pipelines/p2_chirality/` on disk.** They live in `public/images/chirality/`. The 25 MB PDF was compiled on-pod where figures were `cp`'d alongside the `.tex` at build time. **BLOCKER for tarball build:** must `cp public/images/chirality/fig_*.png pipelines/p2_chirality/` before tarring, OR build the tarball from a staging directory that contains both.
- **Extras to exclude:** `.aux`, `.log`, `.out`, `.toc`, `.blg`, `paper2_chirality_section.tex` (belongs to Paper 2 not Paper 4), `BENCHMARK_REPORT.md`, `BIAS_AUDIT_REPORT.md`, all `.py` scripts, `outputs/` dir. The chirality directory is a pipeline workspace, not a paper-only folder.
- **Predicted clean compile:** SSOT says fire #9 on-pod produced 25 MB / 11 pp / 0 undef. Assuming figures are staged alongside tex, AutoTeX `pdflatex × 2` (no bibtex if shipping .bbl) should be clean.
- **Primary category:** `astro-ph.CO` (the paper's headline result is a cosmological null — refuting claimed large-scale parity violation; dipole + multipole power spectrum + hemisphere asymmetry testing is cosmology)
  - **Secondary (cross-list):** `astro-ph.GA` (galaxy morphology / ViT classifier / 8.47M galaxy catalog is extragalactic), `astro-ph.IM` (bias-hardening suite + TTA equivariance is methodology)
  - **Justification:** Primary `astro-ph.CO` because the paper's framing is a test of parity symmetry at cosmological scales — the dipole null and the Shamir refutation are the headline. `astro-ph.GA` cross-list is mandatory (it's a galaxy morphology catalog). `astro-ph.IM` optional but recommended (the bias-hardening suite is a reusable methodology contribution).
- **Abstract char count:** **2,067 chars.** **⚠ OVER LIMIT** (arXiv 1,920). Needs ~147-char trim. Tightest targets: drop the `\sigmaunit` macro values from the abstract (keep them in body only); consolidate the three dipole-test statements into one line.
- **Comment string (ready to paste):**

  > 11 pages, 11 figures, 4 tables, 23 references; 8.47M-galaxy chirality catalog with D4 test-time equivariance; dipole null 0.43σ; Shamir 2020/2022 3% asymmetry claim refuted at 7×. Catalog at https://huggingface.co/datasets/bamfai/galaxy-chirality-catalog (CC-BY-4.0, v2026.04); model at https://huggingface.co/bamfai/galaxy-chirality-v2; companion to arXiv:PAPER1-ID (bounce framework).

- **Data-availability statement:** ✓ PRESENT with pinned `v2026.04` HF tags per SSOT `P4-HF-DOI`. Strength: 5/5. Zenodo mirror note included.
- **License recommendation:** arXiv perpetual non-exclusive. HF catalog + model CC-BY-4.0.
- **PDF metadata:** `\title{No Evidence for Large-Scale Parity Violation in Galaxy Morphology:\\ ...}` — `\\` present; strip from web-form title.
- **Blockers:**
  1. Tarball does not exist — must be built. Task `P4-TARBALL-BUILD` (P1).
  2. Figures NOT co-located with `.tex` — must stage (`cp public/images/chirality/fig_*.png pipelines/p2_chirality/`) before tarring.
  3. Abstract > 1920 chars — trim for web form.
  4. Post-Paper-1 cross-cite: `\bibitem{Golden:2026framework}` is currently a URL placeholder pointing to `bigbounce.hubify.app`; after Paper 1 arXiv ID is assigned, update bibitem to arXiv:PAPER1-ID.
- **Readiness grade:** **B (ready after 1-hour fix: stage figures, build tarball, trim abstract).**

---

## ArXiv-ID substitution plan (post-submission cross-cite rewiring)

See companion file: [`arxiv_id_substitution_plan.md`](arxiv_id_substitution_plan.md).

High-level summary: four papers share three `\bibitem`/`\cite` keys that currently resolve to "companion paper (2026)" placeholders. Once any paper is assigned an arXiv ID, the corresponding `\bibitem` in the other three must be rewritten to cite the arXiv ID. Recommended submission order (from SSOT `index.md`): **Paper 4 → Paper 3 → Paper 1 → Paper 2**, because Paper 2 has the most cross-cites to resolve and Paper 4 has the fewest. After each submission, update the in-flight papers' `.tex` before submitting the next.

---

## Houston submission checklist — exact sequence (per paper)

For each of the 4 papers, Houston's 15-min arXiv web-form flow is identical:

**Pre-submission (Houston agent or this editor does this once):**

1. Confirm tarball exists and is minimal (only `.tex` + `.bbl` + referenced figures).
2. Confirm tarball compiles clean via `mkdir /tmp/pN_smoke && tar xzf PATH -C /tmp/pN_smoke && cd /tmp/pN_smoke && pdflatex -interaction=nonstopmode BASE && bibtex BASE (if no .bbl) && pdflatex BASE && pdflatex BASE`. Verify 0 undefined references and PDF ≥ expected size.
3. Confirm abstract trimmed copy ready (≤ 1,920 chars, plain text — no `\\` linebreaks, no macros that arXiv's web form can't parse). Keep this as a separate `abstract_for_webform.txt` alongside each tarball.
4. Confirm comment string ready (copy-paste from this file's per-paper section above).

**On arXiv.org/submit (per paper, ~15 min):**

1. **Login.** arxiv.org/user/login.
2. **Start new submission.** Click "Start a new submission".
3. **License selection.** Choose **arXiv.org perpetual, non-exclusive license to distribute** (default). Do NOT pick CC-BY unless Houston wants the PDF itself CC-BY — code/data are already CC-BY on HuggingFace separately.
4. **Primary archive.** Select per table:
   - Paper 1: `astro-ph` → `astro-ph.CO`
   - Paper 2: `astro-ph` → `astro-ph.CO`
   - Paper 3: `astro-ph` → `astro-ph.IM`
   - Paper 4: `astro-ph` → `astro-ph.CO`
5. **Cross-lists** (add all that apply):
   - Paper 1: `gr-qc`, `hep-th`
   - Paper 2: `astro-ph.IM`
   - Paper 3: `astro-ph.CO`, `astro-ph.GA`
   - Paper 4: `astro-ph.GA`, `astro-ph.IM`
6. **Upload tarball.** Select the paper's `.tar.gz`. AutoTeX will run.
7. **Wait for AutoTeX.** Usually 30–90 s. If it fails, read the log — most common causes (per fire #9 experience) are (a) missing bbl, (b) figure-path mismatch, (c) obscure package.
8. **Preview PDF.** Click "Preview" — confirm figure count, page count, references all resolved.
9. **Metadata page:**
   - **Title:** paste the paper title but replace `\\` with a space. Example for Paper 1: "Spin-Torsion Cosmology and the Search for Geometric Dark Energy: A Null Result, an ALP Birefringence Prediction, and the Matter-Bounce f_NL = -35/8 Testable by SPHEREx" (or paper's actual subtitle).
   - **Authors:** "Houston Golden"
   - **Abstract:** paste from `abstract_for_webform.txt` (plain text, trimmed to ≤ 1,920 chars).
   - **Comment:** paste the comment string from this audit's per-paper section. Replace `PAPER1-ID`/`PAPER2-ID`/`PAPER3-ID`/`PAPER4-ID` with actual arXiv IDs for already-submitted papers; leave as `forthcoming` for not-yet-submitted ones (edit via replacement later).
   - **Report-no / MSC / ACM:** leave blank (not applicable).
   - **Journal-ref / DOI:** leave blank (pre-publication).
10. **Final review.** Scan the summary page. Confirm categories are correct.
11. **Submit.** Click submit. Record the arXiv submission ID in `project-context/SSOT/paper-N/status.md` under a new "arXiv submission" section.
12. **Wait for announcement.** arXiv announces daily at 20:00 UTC (00:00 UTC on Mondays). Paper goes live ~20 min after that.
13. **Post-announcement:** Record final arXiv ID in SSOT, update `paper.html`, `activity.html`, `CURRENT_STATUS.md`, and — **critically** — update the other papers' `\bibitem{Golden:2026...}` placeholders to cite the new arXiv ID before those other papers are submitted. See `arxiv_id_substitution_plan.md`.

---

## Proposed new tasks for SSOT/queue.md

| Task ID | Priority | Owner | Est. time | Description |
|---|---|---|---|---|
| `P2-ABSTRACT-TRIM-FOR-WEBFORM` | P1 | agent | 15 min | Trim Paper 2 abstract from 2,273 to ≤ 1,920 chars for arXiv web form. Body abstract in `.tex` stays verbatim. Save as `research/focused_paper_source_integration/abstract_for_webform.txt`. |
| `P2-TARBALL-REBUILD-INCLUDE-BBL` | P1 | agent | 10 min | Rebuild `paper2_arxiv_submission.tar.gz` to include `02_full_draft.bbl` (already on disk) alongside `.tex` + `.bib` + 6 figures. Eliminates arXiv AutoTeX bibtex-step failure mode. Smoke-test via `/tmp/p2_smoke` clean compile. |
| `P3-TARBALL-BUILD-MISSING` | P1 | agent | 20 min | Build Paper 3 arXiv tarball — does not exist. Contents: `paper3_draft.tex` + 22 referenced figures (21 PDF + 1 PNG) under `figures/`. Exclude `.aux`, `.log`, `.out`, `.png` duplicates of `.pdf`, `_cutout_cache/`, `paper3_draftNotes.bib`. Smoke-test via `/tmp/p3_smoke`. |
| `P3-ABSTRACT-TRIM-FOR-WEBFORM` | P1 | agent | 20 min | Trim Paper 3 abstract from 2,194 to ≤ 1,920 chars for arXiv web form. Targets: move per-survey breakdown to Table 1 ref, keep aggregate 319,443 / 37.3M / 58.8%. Save as `pipelines/p3_anomaly_engine/abstract_for_webform.txt`. |
| `P3-HF-UPLOAD-BEFORE-SUBMIT` | P1 | agent | 2 h | Publish aggregated 319,443-anomaly catalog to HuggingFace `bamfai/bigbounce-anomaly-catalog` (or similar) BEFORE arXiv submission so data-availability link is live on day 1. Pin version tag `v2026.04`. Update Paper 3 `.tex` data-availability block to match. |
| `P4-STAGE-FIGURES-AND-TARBALL-BUILD` | P1 | agent | 20 min | Stage 11 chirality figures in `pipelines/p2_chirality/` via `cp public/images/chirality/fig_*.png pipelines/p2_chirality/`. Build Paper 4 arXiv tarball: `chirality_catalog_paper.tex` + `.bbl` + 11 figures. Exclude all `.py`, `.md`, `outputs/`, `paper2_chirality_section.tex`. Smoke-test via `/tmp/p4_smoke`. |
| `P4-ABSTRACT-TRIM-FOR-WEBFORM` | P1 | agent | 10 min | Trim Paper 4 abstract from 2,067 to ≤ 1,920 chars for arXiv web form. Save as `pipelines/p2_chirality/abstract_for_webform.txt`. |
| `P-COMMENT-STRING-DRAFT` | P2 | agent | 30 min | (DONE in this file — adopt verbatim.) Four per-paper comment strings ready. After each submission, update in-flight versions by replacing `PAPERN-ID` with real arXiv ID. |
| `P-ARXIV-CATEGORIES-CONFIRM` | P2 | Houston | 5 min | Houston reviews this audit's category recommendations. Confirm or override before form submission. |
| `P1-PAPERTIMESTAMP-REFRESH` | P3 | agent | 2 min | Bump `\paperTimestamp` in `arxiv/main.tex` from 2026-04-13 to submission date. Cosmetic. Non-blocker. |
| `P-POST-SUBMISSION-XREF-REWIRE` | P1 | agent | 20 min / paper | After each paper is announced with arXiv ID: update the 3 companion papers' `\bibitem{Golden:2026...}` entries to cite the real arXiv ID. See `arxiv_id_substitution_plan.md`. |

---

## Verdict

**Readiness for arXiv submission, per paper, as of 2026-04-18:**

| Paper | Grade | Time-to-submit | Blockers |
|---|---|---|---|
| Paper 1 (spin-torsion) | **A** | 15 min (web form only) | None |
| Paper 2 (f_NL forecast) | **B+** | 45 min | Abstract trim + tarball rebuild to include .bbl |
| Paper 3 (anomaly catalog) | **B** | 3 h | Tarball must be built + abstract trim + HF upload |
| Paper 4 (chirality catalog) | **B** | 1 h 15 min | Tarball must be built + figures must be staged + abstract trim |

**Recommended submission order (updating SSOT `index.md`'s order):**

1. **Paper 4** (chirality) — fewest companion cross-cites (only 1: `Golden:2026framework`), cleanest story
2. **Paper 1** (spin-torsion) — the citation root; once it has an arXiv ID, three other papers can rewire
3. **Paper 3** (anomaly catalog) — cites Paper 1 (now resolved) + has 3 companion cross-cites that need rewiring
4. **Paper 2** (f_NL forecast) — cites Paper 1 + Paper 3 (both now resolved), submitted last

**Program-wide wall-clock to all-four-submitted:** ~6 hours work across Houston + agent + one arXiv-announcement cycle per paper (arXiv is 1-per-day-per-submitter announcement rate-limited, so allow ~1 announcement cycle = 1 business day between submissions to get the arXiv ID before submitting the next dependent paper). **Full program submission window: ~5 business days** if sequenced serially. Can be compressed to ~3 days if Houston is comfortable with "companion paper (arXiv: forthcoming)" placeholders in the last-submitted papers and uses arXiv's `replace` function to fix cross-cites after announcement.

**No showstoppers. All four papers are near-submit-ready.** The per-paper work is mechanical: abstract trim, tarball build or rebuild, figure staging. Total elapsed time to submit-all-four is single-digit business days, not weeks.
