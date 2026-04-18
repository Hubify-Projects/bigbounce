# BigBounce SSOT — cross-paper close-the-gap queue

**Prioritized, tagged task queue to drive every paper to true 100 %.** One task per row. Each task is scoped to close a specific percentage-point gap in a specific paper (or program-wide).

Last authoritative update: 2026-04-18 (drive-to-100 fire #15) — **pod fixes landed**. Fix sub-agent `a0506c5415378292a` on pod `uyl9w5oo37uf06` completed both follow-ups and the pod is drained. **P3-FISHER-FULL-FIX** (v2b correct decomposition `C = C_signal(A,γ) + α_noise·C_noise`, scale only noise): σ(γ) drops monotonically — **NG15 current 0.506 (2.24 σ) · NG20 0.358 (3.17 σ) · CPTA 2030 0.226 (5.01 σ) · SKA-class 2035 0.113 (10.02 σ)** — canonical result in `pipelines/p3_anomaly_engine/fisher_full/fisher_result_v2.json` + `fisher_forecast_v2.png`. **P3-A-ALT** (TESS-FFI cutout fallback for TIC 374313355): `lightkurve.search_tesscut` yields 3 sectors (45/46/72), N = 3,321 photometric points from sector 46, Lomb-Scargle peak at **P = 13.782 d, FAP = 3.9 × 10⁻²⁶³**. Tmag ≈ 18.5 is below SPOC pipeline threshold, which is why `search_lightcurve` returned 0 products. Paper 3 §6 table + prose rewritten with real Fisher v2b numbers and Paper 3 §7.3 P3-A periodicity answered yes. Follow-ups filed: `P3-PDF-RECOMPILE-V3` (pod) to render the new §6 Fisher table + `P3-A-TYPING` (P3, agent) for SIMBAD / Gaia-DR3 classification of the 13.78-d variable. Prior fire #13 HF-upload-extend state unchanged (5 of 8 HF blocks, 61.7 % coverage).

## Legend

- **Priority** — `P0` now · `P1` this week · `P2` before submission · `P3` after submission / polish
- **Owner** — `agent` (this session or future agent) · `pod` (H200/H100 compute required) · `Houston` (decision) · `site` (frontend edit only)
- **Blocker of** — which paper this gates
- **% closed** — how much of the paper's remaining gap this task closes on completion
- **Status** — `[ ]` open · `[~]` in progress · `[x]` done · `[!]` blocked (with reason)

---

## P0 — do now

| ID | Title | Owner | Paper | % closed | Status | Notes |
|---|---|---|---|---:|---|---|
| `P2-REVTEX4-2-CONVERT` | Rewrite Paper 2 `.tex` from `\documentclass[a4paper,11pt]{article}`+natbib to `revtex4-2` PRD + embedded `\bibitem` | agent | P2 | 6 % | [x] | DONE 2026-04-17 |
| `P2-BIB-RESOLVE` | Convert all `\citep{}`→`\cite{}`, embed bibitems from `03_references.bib` + `focused_paper_refs.bib`; zero `[?]` in PDF | agent | P2 | 4 % | [x] | DONE 2026-04-17 |
| `P3-A` | TIC 374313355 periodicity analysis (TESS archival light curve + Lomb-Scargle) | pod | P3 | 0.05 % | [x] | DONE 2026-04-18 drive-to-100 fire #15 — closed via the `P3-A-ALT` fallback path (SPOC pipeline returned 0 products because Tmag ≈ 18.5 is below the SPOC delivery threshold). See `P3-A-ALT` row |
| `P3-A-ALT` | TIC 374313355 fallback search: `lightkurve.search_tesscut` FFI cutout + Kepler + K2 by resolved coordinates | pod | P3 | 0.05 % | [x] | DONE 2026-04-18 drive-to-100 fire #15 — pod `uyl9w5oo37uf06` sub-agent `a0506c5415378292a`: `search_tesscut("TIC 374313355")` found 3 sectors (45, 46, 72), built N = 3,321-point light curve from sector 46 FFI cutout aperture photometry, **Lomb-Scargle peak P = 13.782 d, FAP = 3.9 × 10⁻²⁶³**. Paper 3 §7.3 P3-A "yes/no" closed: **yes, periodicity detected**. Files `pipelines/p3_anomaly_engine/p3a_tess_374313355_lomb_scargle/{alt_search.json, RESULTS.md}`. Filed follow-up `P3-A-TYPING` (P3, agent) for SIMBAD / Gaia-DR3 typing of the 13.78-d variable |
| `P3-B` | Deep cross-match of top-100 DESI + 203 eROSITA + BAL-QSO against NED / VizieR / Gaia-XP | agent | P3 | 0.1 % | [~] | PARTIAL 2026-04-18 drive-to-100 fire #10 — NED-only pass on 80 SIMBAD-novel exemplars (4 surveys × 20). Usable sub-sample (top-11 SDSS): 45 % NED archival-identification rate (5 / 11). 69 / 80 returned rate-limit errors; filed `P3-B-NED-RETRY` + `P3-B-VIZIER` (P2) + `P3-B-GAIA-XP` (P3). Findings note: `projects/cross_survey/results/P3-B_findings.md`. Classification JSON: `projects/cross_survey/results/ned_crossmatch_summary.json`. Paper 3 §7 gets honesty footnote, not a headline-number rewrite |
| `P4-DIPOLE-JSON-REBUILD` | Re-emit non-truncated `outputs/dipole/summary.json` (current one crashed at L366 after `consistent_with_null:`) | pod | P4 | 0.5 % | [x] | DONE 2026-04-17 |

## P1 — this week

| ID | Title | Owner | Paper | % closed | Status | Notes |
|---|---|---|---|---:|---|---|
| `P1-LINE-299-WORDSMITH` | Replace `(amplitude and shape TBD)` on L299 of `arxiv/main.tex` with a parametric estimate or explicit "not derived here" phrasing | agent | P1 | 0.2 % | [x] | DONE 2026-04-17 — verified no `TBD` remains; L299 now reads "amplitude and angular spectrum are not derived in this work and are flagged as an open direction" |
| `P1-FIGURES-VERIFY` | Verify every `\includegraphics{}` in `arxiv/main.tex` resolves; PDF is currently only 510 KB (low) | agent | P1 | 0.1 % | [x] | DONE 2026-04-17 — pre-recompile check passed (per `SSOT/paper-1/status.md`) |
| `P1-CORNER-PLOTS` | Generate corner plots from existing 424 k MCMC samples (`getdist`), embed in §IV, drop L882 "companion data release" note | pod | P1 | 0.2 % | [x] | DONE 2026-04-17 — H0=67.69±1.06, ΔNeff=-0.019±0.169 on 119,617 samples; figure inserted at L882 of `arxiv/main.tex` |
| `P1-PDF-RECOMPILE` | Recompile Paper 1 PDF on-pod with `\paperTimestamp` refreshed | pod | P1 | 0.2 % | [x] | DONE 2026-04-17 — 707 KB, 0 undef (per `SSOT/paper-1/status.md`). Follow-up recompile needed for new §IV corner figure — tracked as `P1-PDF-RECOMPILE-V2` below |
| `P1-SITE-SYNC` | Sync `index.html`, `paper.html`, `explained.html`, `activity.html`, `figures.html`, `glossary.html` with v2.3.x final numbers | site | P1 | 0.1 % | [x] | DONE 2026-04-17 — via `P-SITE-FULL-SYNC` burst |
| `P1-WIKI-SYNC` | Freeze `wiki/entities/paper-1-*.md` as pointer-only files routing to SSOT | agent | P1 | 0.05 % | [x] | DONE 2026-04-17 (per `SSOT/paper-1/status.md`) |
| `P1-TARBALL` | Build Paper 1 arXiv tarball + smoke-test a clean revtex build from the tarball alone | agent | P1 | 0.15 % | [x] | DONE 2026-04-17 drive-to-100 fire #9 — rebuilt `arxiv/main_arxiv_submission.tar.gz` (440 KB) with fresh `main.tex` + fresh `main.bbl` + 3 actually-referenced figures (dropped 11 dead figures saving ~1.3 MB). Smoke-test: extracted tarball to `/tmp/p1_smoke` and ran `pdflatex -interaction=nonstopmode main` twice via Docker TeX Live — produced 945 KB PDF with 0 undefined citations |
| `P2-COMPILE-POD` | Recompile Paper 2 PDF on pod after revtex4-2 conversion; verify ≥2 MB, 0 undefined refs, all 6 figures embedded | pod | P2 | 2 % | [x] | DONE 2026-04-17 — 614 KB, 0 undef, abstract + `sec:viable`→`sec:benchmark` fixed |
| `P2-XREF-AUDIT` | Audit Paper 2 cross-refs: Paper 1 `\citep{Golden:2026framework}` handle, Paper 3 implicit in §4/§5 → add explicit cite if present | agent | P2 | 1 % | [x] | DONE 2026-04-17 |
| `P2-SITE-SYNC` | Update `index.html` σ(f_NL) card, `paper.html` readiness 85%→100%, `activity.html`, `figures.html` (+6 figs), `data-explorer.html` (embed Fisher JSON) | site | P2 | 1 % | [x] | DONE 2026-04-17 — via `P-SITE-FULL-SYNC` burst |
| `P2-WIKI-POINTER` | Rewrite `wiki/entities/paper-2-fnl-forecast.md` as pointer-only to SSOT (current file stale 2026-04-04, wrongly claims SUBMISSION-READY) | agent | P2 | 0.3 % | [x] | DONE 2026-04-17 |
| `P2-CURRENT-STATUS-SYNC` | Update Paper 2 row in `CURRENT_STATUS.md` from "v1.3.0 · Ready" → "v1.6.0 · 85 % · revtex4-2 conversion pending" | agent | P2 | 0.2 % | [x] | DONE 2026-04-17 |
| `P2-PDF-PUBLISH` | Copy compiled revtex4-2 PDF to `public/papers/paper2_fnl_forecast.pdf`, link from `paper.html` | pod | P2 | 0.3 % | [x] | DONE 2026-04-17 — file committed |
| `P2-TARBALL` | Assemble Paper 2 arXiv tarball (tex + bbl + 6 figs + bphi.pdf), smoke-test a clean revtex build | agent | P2 | 0.2 % | [x] | DONE 2026-04-17 |
| `P3-C` | Fisher-forecast σ(γ) for NANOGrav 20yr / EPTA DR3 / SKA-P1 given current posterior | agent | P3 | 0.05 % | [x] | DONE 2026-04-17 — scaling-only forecast note at `pipelines/p3_anomaly_engine/fisher_forecast_gamma_future_ptas.md` (σ(γ)≈0.22 NG20yr · 0.16 EPTA DR3 · 0.15 SKA-P1; 3σ discrimination threshold σ(γ)≤0.44 already at NG15 edge). Paper 3 §6 "continued monitoring" language replaced with concrete paragraph + Siemens2013 + Rosado2015 bibitems. Filed companion `P3-FISHER-FULL` (pod) for full free-spectrum Fisher. Triggers `P3-PDF-RECOMPILE-V2`. |
| `P3-PDF-CANON` | Delete or rebuild `arxiv/paper3_anomaly_catalog.tex` + `.pdf` from the pipelines copy | agent | P3 | 0.3 % | [x] | DONE 2026-04-17 — verified `arxiv/paper3_anomaly_catalog.tex` is a 40-line pointer stub; stale `.pdf` already removed; 27 MB canonical PDF mirrored at `public/papers/paper3_anomaly_catalog.pdf` |
| `P3-PDF-RECOMPILE` | Recompile Paper 3 PDF on-pod with today's date + SSOT cross-check | pod | P3 | 0.3 % | [x] | DONE 2026-04-17 — 27 MB, 27 pp, 21 figs embedded, 0 undef |
| `P4-PDF-CANON` | Pick `pipelines/p2_chirality/chirality_catalog_paper.tex` as canonical; delete or rebuild arxiv/ copy | agent | P4 | 0.5 % | [x] | DONE 2026-04-17 — canonical set + cross-ref xref cleaned; see `SSOT/paper-4/status.md` |
| `P4-PDF-RECOMPILE` | Recompile Paper 4 PDF on-pod with today's date + SSOT cross-check | pod | P4 | 0.5 % | [x] | DONE 2026-04-17 — 25 MB, 11 pp, 0 undef. Follow-up recompile needed for new LSST projection line — tracked as `P4-PDF-RECOMPILE-V2` below |
| `P4-PAPER2-XREF` | Fix two stale wordings in `pipelines/p2_chirality/paper2_chirality_section.tex` | agent | P4+P2 | 0.3 % | [x] | DONE 2026-04-17 |
| `P3-SITE-SYNC` | Update `index.html`, `paper.html`, `activity.html`, `figures.html`, `data-explorer.html` to reflect Paper 3 SSOT numbers | site | P3 | 0.1 % | [x] | DONE 2026-04-17 — via `P-SITE-FULL-SYNC` burst; catalog preview added to data-explorer |
| `P4-SITE-SYNC` | Same for Paper 4 SSOT numbers | site | P4 | 0.3 % | [x] | DONE 2026-04-17 — via `P-SITE-FULL-SYNC` burst; catalog preview + TTA entry added to data-explorer |
| `P3-HF-UPLOAD` | Publish aggregated 319,443-anomaly catalog to HuggingFace `bamfai/bigbounce-anomaly-catalog` with CC-BY-4.0 | agent | P3 | 0.05 % | [~] | PARTIAL 2026-04-18 drive-to-100 fire #11 — private repo `bamfai/bigbounce-anomaly-catalog` created, **DESI DR1 block (195,829 rows · 10.5 MB parquet · 61 % of paper aggregate) uploaded**, dataset card committed. Paper 3 §9 data-availability updated to point at HF dataset (private-until-acceptance wording). Remaining 7 surveys filed as `P3-HF-UPLOAD-EXTEND` (P2) — need explicit score-cut re-derivation per survey. Script: `pipelines/p3_anomaly_engine/hf_upload_catalog.py` |
| `P4-HF-DOI` | Pin HF `bamfai/galaxy-chirality-catalog` version + add DOI / versioned URL to Paper 4 data-availability statement | agent | P4 | 0.2 % | [x] | DONE 2026-04-17 |
| `P3-XREF` | Audit Paper 3 cross-references against Paper 2 f_NL forecast + Paper 4 dipole infrastructure | agent | P3 | 0.05 % | [x] | DONE 2026-04-17 — added 3 Golden companion bibitems (framework, fnl, chirality) + 4 `\cite{}` calls at L70, L515, L597; triggers `P3-PDF-RECOMPILE-V2` (filed below) |
| `P4-LSST-LINE-REVIEW` | Houston reviews paper4 L913 "Future surveys (Rubin LSST)" line on final PDF read — confirm TRULY BLOCKED | Houston | P4 | 0.2 % | [ ] | If it's not blocked per Principle 10 it becomes a new task |
| `P-MEMORY-SYNC` | Add MEMORY.md entry for SSOT directory + update existing entries that reference old paper-N-status.md paths | agent | ALL | 0 % | [x] | DONE 2026-04-17 — refreshed `project_ssot_structure.md` (layout + drive-to-100 loop block), rewrote `project_papers_status.md` as SSOT pointer (was 11 days stale with Paper 2 v1.3.0, Paper 4 ~85 %), added new `project_drive_to_100.md` memory + index entry in `MEMORY.md` |
| `P1-PDF-RECOMPILE-V2` | Recompile `arxiv/main.pdf` to render the §IV corner figure inserted at L882 | pod | P1 | 0.1 % | [x] | DONE 2026-04-17 drive-to-100 fire #9 — Docker TeX Live compile produced 945 KB `arxiv/main.pdf` with 0 undef cites, §IV corner figure rendered. Mirrored to `public/papers/spin_torsion_paper1.pdf` |
| `P4-PDF-RECOMPILE-V2` | Recompile `public/papers/chirality_catalog_paper.pdf` to render the new LSST 10-yr projection line in Future Directions | pod | P4 | 0.3 % | [x] | DONE 2026-04-17 drive-to-100 fire #9 — Docker TeX Live compile (TEXINPUTS=./public/images/chirality) produced 25.7 MB `chirality_catalog_paper.pdf` with 0 undef cites, LSST projection line rendered. Mirrored to `public/papers/chirality_catalog_paper.pdf` |
| `P3-PDF-RECOMPILE-V2` | Recompile `pipelines/p3_anomaly_engine/paper3_draft.pdf` + mirror to `public/papers/paper3_anomaly_catalog.pdf` to render (a) 3 new Golden companion-paper bibitems + 4 new `\cite{}` calls (fire #2) AND (b) Siemens2013 + Rosado2015 bibitems + §6 "when-decisive" paragraph (fire #3) | pod | P3 | 0.1 % | [x] | DONE 2026-04-17 drive-to-100 fire #9 — Docker TeX Live compile produced 28 MB `paper3_draft.pdf` with 0 undef cites, all new cross-refs + Siemens/Rosado bibitems + §6 when-decisive paragraph rendered. Mirrored to `public/papers/paper3_anomaly_catalog.pdf` |
| `P3-PDF-RECOMPILE-V3` | Recompile Paper 3 PDF to render §6 Fisher v2b table (σ(γ) across NG15/NG20/CPTA/SKA) + the v2b decomposition paragraph + update §7.3 P3-A row to "yes, P=13.78 d, FAP 4e-263" | pod | P3 | 0.1 % | [ ] | Triggered by fire #15 (P3-FISHER-FULL-FIX + P3-A-ALT landed in `paper3_draft.tex`). Agent-doable once Docker/pod is available |
| `P1-BBL-REGEN` | Re-run `bibtex arxiv/main` then `pdflatex` twice to regenerate `arxiv/main.bbl` against current `arxiv/main.tex` | pod | P1 | 0.15 % | [x] | DONE 2026-04-17 drive-to-100 fire #9 — Docker TeX Live `bibtex main` regenerated `arxiv/main.bbl` from `references.bib`; all 55 cites in `main.tex` now have matching bibitems. 0 undef cites in the final pdflatex pass |
| `P3-FISHER-FULL` | Full Fisher-matrix calculation over the NANOGrav free-spectrum covariance to replace the scaling-only forecast with a properly marginalized σ(γ) projection | pod | P3 | 0.05 % | [x] | DONE 2026-04-18 drive-to-100 fire #15 — superseded by `P3-FISHER-FULL-FIX` v2b canonical result. Core NG15 value σ(γ)=0.506 stands; future-PTA row now correct |
| `P3-FISHER-FULL-FIX` | Correct future-PTA scaling: decompose C = C_signal(A,γ) + C_noise; scale only C_noise per scenario | pod | P3 | 0.02 % | [x] | DONE 2026-04-18 drive-to-100 fire #15 — pod sub-agent `a0506c5415378292a` ran v2b decomposition: `C = C_signal(A,γ) + α_noise·C_noise`, only noise variance scales per scenario, calibration `sigma_base_frac = 1.4123` reproduces NG15 published σ(γ)=0.506. **Scenarios: NG15 σ(γ)=0.506 (2.24σ) · NG20 0.358 (3.17σ) · CPTA 2030 0.226 (5.01σ) · SKA-class 2035 0.113 (10.02σ)**. Canonical file `pipelines/p3_anomaly_engine/fisher_full/fisher_result_v2.json` + `fisher_forecast_v2.png`. Paper 3 §6 "when-decisive" prose rewritten with these numbers. Triggers `P3-PDF-RECOMPILE-V3` (filed below) |

## P2 — before submission

| ID | Title | Owner | Paper | % closed | Status | Notes |
|---|---|---|---|---:|---|---|
| `P3-D` | Ensemble anomaly detection (VAE + iForest + one-class SVM) on existing latent vectors → inter-model agreement column | pod | P3 | 0.05 % | [ ] | §7.3 #1. 2–3 wk on H200 |
| `P3-E` | Synthetic-anomaly injection + recovery for 7 non-DESI surveys | pod | P3 | 0.1 % | [ ] | §7.3 #2. ~2 wk each, parallelisable |
| `P3-F` | DESI B-dominant population (44,436 / 22.7 %) calibration-systematics audit | pod | P3 | 0.05 % | [ ] | §7.3 #3. ~2 wk |
| `P3-G` | Empirical Landy-Szalay w(θ) bias calibration for anomaly subsample (replaces α = 0.15 assumption) | pod | P3+P2 | 0.1 % | [ ] | §7.3 #4. Re-uses Paper 4 dipole infrastructure |
| `P3-H` | NANOGrav reforecast with inflated uncertainty from DR3 free-spectrum covariance | agent | P3 | 0.05 % | [ ] | §7.3 #5. ~1 wk |
| `P3-B-NED-RETRY` | Retry 80-sample NED cross-match with ≥5 s inter-query delay + 3-retry on HTTP 429 | agent | P3 | 0.05 % | [ ] | 69/80 objects rate-limit-errored on first pass; rerun needed to finalize archival-ID fraction |
| `P3-B-VIZIER` | VizieR all-catalogs cone search on residual NED-novel objects | agent | P3 | 0.05 % | [ ] | Initial attempt hung the VizieR TAP; needs timeout-aware retry budget 20-30 min |
| `P3-HF-UPLOAD-EXTEND` | Aggregate + upload remaining surveys (NEOWISE 436 · Planck 200 · Gaia 500 — agent-doable from H200 snapshot) | agent | P3 | 0.03 % | [x] | DONE 2026-04-18 drive-to-100 fire #13 — all 3 remaining agent-doable blocks uploaded via `pipelines/p3_anomaly_engine/hf_upload_extend.py` (top-N by `anomaly_score`, all 3 match Paper 3 Table 1 exactly). Cumulative with prior ACT (fire #12) + DESI (fire #11): 5 of 8 surveys live on HF, 197,165 / 319,443 = 61.7 %. Multi-block dataset card live. SDSS/LAMOST/eROSITA split out to `P3-HF-UPLOAD-EXTEND-POD` (synthetic-only in snapshot, needs regen) |
| `P3-HF-UPLOAD-EXTEND-POD` | Regenerate + upload SDSS DR18 (77,905) · LAMOST DR10 (44,075) · eROSITA DR1 (298) anomaly tables | pod | P3 | 0.02 % | [ ] | H200 2026-04-08 snapshot has `data_source: "synthetic"` for these three — only aggregate score statistics, no row-level RA/Dec/score table. Needs pod rerun of the BigAE scoring pass on the raw survey downloads. Once regenerated, uploaded via a 3rd extend script |
| `P-SITE-FULL-SYNC` | Site-agent pass: run all P3-SITE-SYNC, P4-SITE-SYNC, and post-sweep P1/P2 variants together | site | ALL | ~1 % total | [x] | DONE 2026-04-17 — badges + catalog previews + glossary additions + nav restructure + password-gated internal pages; commits `54f355e` → `9f4e692` |
| `P-ARXIV-P4` | Assemble Paper 4 tarball, fill arXiv form, submit, return ID | Houston | P4 | closes | [ ] | Do Paper 4 first (most self-contained) |
| `P-ARXIV-P3` | Same for Paper 3 | Houston | P3 | closes | [ ] | Follow ~24 h after Paper 4 |

## P3 — after submission / polish

| ID | Title | Owner | Paper | % closed | Status | Notes |
|---|---|---|---|---:|---|---|
| `P-MEMORY-AGENT-HOOKS` | Ensure `AGENTS.md` + `CLAUDE.md` routing tells every agent to check SSOT first on any paper-related prompt | agent | ALL | 0 % | [x] | DONE 2026-04-17 drive-to-100 fire #8 — verified `CLAUDE.md` L5-L16 "PAPER STATUS — ALWAYS CHECK THE SSOT FIRST" block + `AGENTS.md` L29-L37 "The Golden Rule" block both route to SSOT with explicit paths. Added drive-to-100 loop pointer block to both files so mid-sweep agents see the cron is running + the `POD DEPLOY BLOCKER` section |
| `P-LEGACY-STATUS-CLEAN` | Rewrite `CURRENT_STATUS.md` as a mirror of `index.md` (single source of derived status) | agent | ALL | 0 % | [x] | DONE 2026-04-17 drive-to-100 fire #7 — rewrote `project-context/CURRENT_STATUS.md` as pointer-only to SSOT. Removed 4-day-stale status mirror (Paper 2 "85 % science done", pod `sleepy_blush_crane`, H200 roll-up table, Pipeline 1 steps table, backup inventory, next-steps list). File now points at SSOT/index.md + per-paper status files + SSOT/queue.md. Noted re-population-prohibited note at bottom |
| `P-FREEZE-WIKI` | Confirm all `wiki/entities/paper-*.md` and `wiki/entities/pipeline-*.md` are pointer-only, no status content | agent | ALL | 0 % | [x] | DONE 2026-04-17 drive-to-100 fire #6 — rewrote `paper-3-anomaly-catalog.md` + `paper-4-chirality.md` + `pipeline-1-tracer-purification.md` as pointer-only to SSOT (removed 42 lines of stale status content: 8 core-number tables, 6 pipeline steps, 5 measured-improvement entries). `paper-1`, `paper-2`, `pipeline-2-chirality`, `pipeline-b-desi-anomaly` were already pointer-only |
| `P-SSOT-CRON` | Add a weekly cron/agent check: "any SSOT file > 7 days stale → flag" | agent | ALL | 0 % | [ ] | Prevents drift |
| `P3-B-GAIA-XP` | Gaia-XP spectral cross-match on optically bright residual-novel objects (SDSS + Gaia_DR3 only) | agent | P3 | 0.05 % | [ ] | Catches spectroscopic IDs SIMBAD/NED would miss |
| `P3-A-TYPING` | Classify TIC 374313355 (RA=160.149°, Dec=+5.092°, Tmag=18.52, P=13.782 d) via SIMBAD + Gaia DR3 + co-processing sectors 45+72 for phase stability; decide EB vs long-rot-period variable vs Cepheid harmonic | agent | P3 | 0.03 % | [ ] | Follow-up to fire #15 close of `P3-A-ALT`. Full identification requires SIMBAD/Gaia type, multi-sector phase check, possibly RV |

---

## Completed (done in this session — 2026-04-17)

**Late 2026-04-17 burst:**
- `P-SITE-FULL-SYNC` — nav restructure around SSOT/papers/data/findings/explainer · sidebar `research` · `papers` · `ssot & tasks` · `key findings` · `explainer` + collapsed secondary groups · 21 internal pages moved behind client-side SHA-256 password gate (`gate.js`, password `bamf`) · subtle sidebar-internal label with lock icon · four paper badges bumped to 99.5 %+ across `index.html` and `paper.html` · catalog previews for Paper 3 and Paper 4 added to `data-explorer.html` (p3AnomalyCatalog, p3SimbadNovelty, p4ChiralityCatalog, p4TTABiasTests) · 5 new glossary entries ($f_{\rm NL}$, TTA, Landy-Szalay, anomaly engine, triple role) · commits `54f355e` · `226d357` · `f9687e0` · `30dbb9c` · `9f4e692`
- `P4-LSST-LINE` — added concrete LSST 10-yr projection (~10^8 spirals · 3σ floor at ~0.04 %) to `chirality_catalog_paper.tex` Future Directions; replaces vague "future surveys" language — Principle-10 compliant
- `P1-LINE-299-WORDSMITH` — verified `(amplitude and shape TBD)` no longer present in `arxiv/main.tex`; L299 now reads "amplitude and angular spectrum are not derived in this work and are flagged as an open direction in Sec.~\ref{sec:birefringence_check}"
- `P1-SITE-SYNC` · `P2-SITE-SYNC` · `P3-SITE-SYNC` · `P4-SITE-SYNC` — all closed as sub-items of `P-SITE-FULL-SYNC`
- `P2-REVTEX4-2-CONVERT` · `P2-BIB-RESOLVE` · `P4-DIPOLE-JSON-REBUILD` — closed in earlier pod sessions
- `P4-PDF-CANON` · `P4-PAPER2-XREF` — canonical set + cross-ref wording reconciled; see `SSOT/paper-4/status.md`
- `DRIVE-TO-100` — plan doc (`SSOT/drive-to-100.md`) + every-20-min self-terminating cron (job `91a7e38b`, recorded in `SSOT/drive-to-100.cron.json`) scheduled to drive remaining agent + site work to exit criteria without user intervention


- `P4-DIPOLE-ARTIFACTS-LOCAL` — Copied dipole summary + figures + log from `pod_final_backup_20260414/` to `pipelines/p2_chirality/outputs/dipole/` · committed `6651dd5`
- `P4-REDSHIFT-BINS-INDEX` — Indexed the already-done `fcw_vs_redshift.csv` (20 bins) — stretch goal turned out done · part of `6651dd5`
- `P3-SSOT-SWEEP` — Forensic sweep on Paper 3 · produced `SSOT/paper-3/status.md` · commit `0c39a15`
- `P4-SSOT-SWEEP` — Forensic sweep on Paper 4 · produced `SSOT/paper-4/status.md` (pre-restructure: `paper4_chirality_status.md`) · earlier commit
- `P-SSOT-RESTRUCTURE` — Moved to `SSOT/` tree; added `README`, `index`, `queue`; pointer stubs kept at old paths — commit `ae21ac5`
- `P-PRINCIPLE-10-CORRECTION-P3` — Corrected Paper 3 "zero future-work hits" claim after Houston pushback; 4 future-work-adjacent hits now classified DO-NOW / SIMULATE-AUGMENT-NOW — commit `ae21ac5`
- `P1-SSOT-SWEEP` — Forensic sweep on Paper 1 · produced `SSOT/paper-1/status.md` at 99 % · **this commit**
- `P2-SSOT-SWEEP` — Forensic sweep on Paper 2 (via background agent `a4cb732018c8ccc35`) · produced `SSOT/paper-2/status.md` at 85 % with revtex4-2 blocker clearly identified · **this commit**

---

## How to work this queue

1. Pick the lowest-ID `P0` task whose dependencies are met.
2. Mark it `[~] in progress` when you start.
3. Execute; when done, flip to `[x]` and move the row to the Completed section with the commit hash.
4. If blocked, flip to `[!]` with a one-line reason.
5. When adding new tasks: insert them at the correct priority; ID them `P{paper}-{slug}` or `P-{program-slug}` for cross-paper.
6. Never delete a completed task row from the history. That's the record.
