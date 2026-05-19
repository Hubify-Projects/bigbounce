# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## PAPER STATUS — ALWAYS CHECK THE SSOT FIRST

**Canonical status for all 4 papers lives in `project-context/SSOT/`.** Before doing any paper-related work:

1. Read [`project-context/SSOT/index.md`](project-context/SSOT/index.md) — cross-paper dashboard (one-line status, % ready, gaps, canonical source files).
2. Read the relevant [`project-context/SSOT/paper-N/status.md`](project-context/SSOT/) — every paper number traced to a data file, plus a "Close the gap to 100 %" section.
3. Check [`project-context/SSOT/queue.md`](project-context/SSOT/queue.md) before inventing a task — you may be duplicating a queued item or starting something lower-priority than what's open.

**Do NOT rely on `CURRENT_STATUS.md`, `wiki/entities/paper-*.md`, or site HTML for paper status.** Those are downstream surfaces that go stale. They should mirror the SSOT, not drive it.

**When you finish work that changes a paper's state** (new result, new compile, new figure, new site sync, new cross-match, closed queue task): update the relevant SSOT `status.md` AND mark the queue row AND the `index.md` headline IN THE SAME COMMIT. The SSOT protocol is in [`project-context/SSOT/README.md`](project-context/SSOT/README.md).

**Drive-to-100 loop may be active.** If you see recent `chore(drive-to-100): fire #N` commits on `main`, an autonomous cron is driving `SSOT/queue.md` to exit criteria. Read [`project-context/SSOT/drive-to-100.md`](project-context/SSOT/drive-to-100.md) "Loop log" and "POD DEPLOY BLOCKER" before starting parallel work on the same queue rows.

---

## CRITICAL RESEARCH DIRECTIVE

**DO NOT suggest "write up the results and publish" or "document the barriers as a paper" as a next step.** The goal of this project is continued active research toward positive scientific discoveries — specifically, finding meaningful evidence that bounce cosmology fits observational and mathematical constraints better than ΛCDM + inflation. After negative results, always propose the next research direction that could yield a positive discovery. Treat barriers as constraints that narrow the search space, not as conclusions. Continue researching until genuine positive results are found.

## Project Overview

This repository contains a comprehensive spin-torsion cosmology research program by Houston Golden, including a scientific paper, a full companion website, MCMC reproducibility infrastructure, and a project intelligence dossier.

**Current versions (May 2026), 5-paper portfolio:**
- **P1A** v1A.0.33 — cascaded-loop EXIT (first paper to satisfy AGENT_RULES §4.4.1; 9th-consec Gemini 0-BLOCKER); external-review-ready
- **P1B** v1B.0.20 — R16 Grok-only BLOCKERs falsified via stale-comment audit
- **P2** v1.7.30 — needs more R-rounds before external review
- **P3** v3.1.56 — R16 + multi-round 9,576-dedup deferral closed via on-disk artifact
- **P4** v1.0.117 — multi-null battery + cross-spectrum smoking gun + paper-wide +3.64σ convention + Houston-approved D4-TTA partial-harvest closure
- **P5** bootstrap-2026-05-15 — **separate companion**: Environmental dependence of spiral chirality across DESI LSS. Matched catalog (2.23M rows) + first-pass analyses on disk; cosmic-web headline analysis blocked on missing DESI environmental VAC ("187 DESI-derived attributes" file confirmed not in repo). Pipeline at `pipelines/p5_desi_chirality/`. Paper is 9KB LaTeX scaffold. SSOT: `project-context/SSOT/paper-5/status.md`.

The legacy long-form Paper 1 `arxiv/main.tex` v2.2.0 (March 2026) is deprecated; current canonical sources are `arxiv/paper1a_ech_nogo.tex`, `arxiv/paper1b_mcmc_companion.tex`, `research/focused_paper_source_integration/02_full_draft.tex` (P2), `pipelines/p3_anomaly_engine/paper3_draft.tex` (P3), `pipelines/p2_chirality/chirality_catalog_paper.tex` (P4), and `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` (P5). R-round 5-vendor loop blocked at R17 on OpenRouter top-up.

**Live website:** https://bigbounce.hubify.app

**Research stance:** Bounce-model agnostic. The goal is proving bounce cosmology beats inflation, not proving one specific model. See `project-context/bounce_portfolio_strategy.md`.

**Key scientific results:**
- 14 structural barriers close all ECH-specific routes from bounce to dark energy (other bounce models like quintom can bypass these)
- ALP birefringence prediction β = 0.27° matches 3.6σ observed signal (0.342 ± 0.094°)
- Branch V matter bounce: f_NL = -35/8 = -4.375 (parameter-free, SPHEREx testable, mechanism-independent across all bounce models)
- Bounce model discrimination table: matter bounce vs Cuscuton vs ekpyrotic vs quintom vs inflation
- f_NL triple role: galaxy bispectrum + PBH abundance regulator + induced GW spectral shape
- NANOGrav 15yr consistency: matter bounce γ = 3.0 vs observed 3.2 ± 0.6 (0.33σ)
- w0-wa bound discussed theoretically only — not implemented computationally in this program (Paper 1 §VII.H explicitly: zero free-w0-wa samples among the 309,789 frozen posterior samples; earlier "quintom-B at 98.6%" bookkeeping was fire-#21 confabulation, corrected fire #25)
- MCMC verification: ΔNeff ≈ 0 in all datasets; H₀ = 67.68 (standard ΛCDM)
- 424,781+ MCMC posterior samples across 3 frozen dataset combinations (Paper 1 abstract canonical figure: 176,840 + 132,949 + 114,992 = 424,781; supersedes earlier 424,181 arithmetic mismatch corrected fire #25)
- Multi-survey anomaly sweep (7 retained surveys + ACT-DR6 quarantined as cross-transfer artifact, 37.3M sources, **378,280 anomalies headline** = 378,080 point-source tier + 200 Planck CMB-patch tier after Path-C native retrains + 7-way 5″ positional deduplication; matches Paper 3 v3.1.56 abstract canonical. The earlier 319,443 figure was the pre-Path-C cross-transfer-scan baseline, superseded by the Path-C rebuild's 388,493 survey-level detections collapsing to 378,280 after dedup (compression 10,213 total = 637 multi-survey cluster collapses + 9,576 intra-survey duplicate collapses by global friends-of-friends union-find at 5″; closes the R3→R16 GRO-B3 multi-round dedup-arithmetic deferral per P3 v3.1.56 against `pathc_dedup_summary_no_act.json`):
  - DESI DR1: 22.5M spectra, 195,829 anomalies (0.87%), 2,145 SNR-filtered, 1,127 uncataloged
  - SDSS DR18: 2.3M spectra, 77,905 anomalies (3.4%) — QC: domain shift scores
  - eROSITA DR1: 930K sources, 298 anomalies (0.03%, BigAE top cut — Paper 3 Table 1 canonical; earlier 9,303 figure was a 1% placeholder before the top-cut policy was applied)
  - LAMOST DR10: 11.4M spectra, 44,075 anomalies (0.39%) — QC: 98% blue-excess bias
  - Planck CMB: 20K patches, 200 anomalies — QC FAIL: needs galactic mask
  - ACT DR6: 20K patches, 200 anomalies — QC FAIL: undertrained (val_loss=22,420)
  - NEOWISE: 43.5K sources, 436 anomalies — QC FAIL: ecliptic systematic
  - Gaia DR3: 50K sources, 500 anomalies — needs 10x expansion
- f_NL Fisher forecast (Paper 2 canonical, externalized to Heinrich+2023): σ(f_NL) = 0.7 (Heinrich et al. 2023 SPHEREx multi-tracer bispectrum); detection significance 3-5σ after systematic budget (noise-weighted shape mismatch, ε-correction, b_φ marginalization, GR projection); 5.2-5.5σ optimistic before GR/b_φ degradation. NOTE: earlier CLAUDE.md numbers σ=16.85/12.72/11.71 were confabulated from a non-paper source (fire #25 / skeptical-statistician P2-FISHER MAJOR); corrected 2026-05-05; paper 02_full_draft.tex uses Heinrich+2023 σ=0.7 throughout.
- f_NL bias validation: Pipeline-1 Gold+Silver tracers show 1.58× enhanced clustering bias vs baseline (Landy-Szalay w(θ) on 5,384 QSO candidates). Earlier "2.28×" CLAUDE.md figure had no paper anchor (theorist peer review 2026-04-18) — corrected to the on-disk 1.58× number from `projects/cross_survey/results/bias_validation.json`
- SPHEREx f_NL forecast (2026-04-10): σ=0.36 (Fisher ideal) / 0.93 (Munchmeyer+2019 conservative) → 4.7-12σ detection of f_NL=-4.375 (bounce) by 2027
- NaMaster birefringence (Pod 1 production 500MC, 2026-04-29): β=0.27° (bounce prediction) recovered as 0.238° (bias 0.032°), SNR=20.32σ at ACT sensitivity (f_sky=0.32, n_side=512, ℓ_max=1024, noise 10 µK·arcmin); β=0.342° (Planck+ACT observed) recovered as 0.302° at SNR=25.71σ; null β=0 at SNR=0.0; consistency P1-prediction vs observation = 0.77σ. Earlier 50MC pilot value SNR=20.74 was at higher MC variance; superseded. Canonical source: `pipelines/h200_results/pod1_namaster_umap_2026-04-29/results/namaster-birefringence/summary.json`
- Combined PTA GPU MCMC: γ = 3.20 ± 0.42 (Paper 3 §6 canonical — 2026-04-17 v2b Fisher recompute), bounce γ=3.0 at 0.48σ, SMBHB excluded at ≳2σ. (Earlier 2026-04-10 CLAUDE.md figure γ = 3.33 ± 0.40 predated the v2b Fisher; corrected fire #25 per theorist peer review.)
- PBH abundance from f_NL=-4.375 (2026-04-10): Edgeworth expansion correction to Press-Schechter; matter bounce naturally suppresses PBH formation; GW spectral index bounce γ=3.0 at 0.48σ from Paper 3 §6 canonical γ=3.20±0.42 (fire #50 2026-04-18: was stale γ=3.33±0.40 / 0.83σ predating the v2b Fisher recompute; harmonized with line-58 PTA GPU MCMC figure); f_NL triple role confirmed
- Second-level AE on 195,829 DESI DR1 anomalies (2026-04-10): 16D latent, max ultra-rare score=53.4 (99.9995th percentile), found ~20 objects anomalous within the anomaly pool
- Emission line finder on DESI DR1 anomalies (2026-04-10): 5,000 anomaly spectra → 4,526 redshifts (Δz<0.05: 80.8%), 96.9% AGN fraction by BPT classification
- Dyson sphere search (2026-04-08): Gaia+AllWISE 7-band AE + RF, 100K stars, 50 planted; precision=1.0, recall=0.9; top discriminators G-W4, W2-W3 colors
- FRB CHIME anomaly detection (2026-04-10): AUC=0.997 ensemble AE+IF; periodic repeaters, ultra-high DM, spectral anomalies classified
- GW echo LIGO (2026-04-10): 1D CNN on ringdowns, AUC=0.975, accuracy=95%, 5σ detection significance; methodology validated for LIGO O4
- ZTF DR21 light curve anomaly search (2026-04-10): 100K synthetic light curves (synthetic — ZTF DR21 API RMSMAGPSF column absent), Lomb-Scargle + AE; running

**Pod status (as of 2026-04-10):** H200 pod `o76k3jfzbfh25e` ACTIVE. SSH: `root@205.196.19.52 -p 11452`. Sessions 1-5 running: SDSS native AE, corrected f_NL, NaMaster birefringence, NANOGrav Bayesian, SPHEREx forecast, PBH abundance (complete), quintom MCMC v2 (running), ZTF DR21 (running). Self-extending chain on iteration 270 (frb_chime, dyson_sphere, emission_line_finder, second_level_AE, bigae_production). See `project-context/active_pods_and_pipelines.md`.

**Houston Method v2:** See `project-context/houston-method-v2.md` — MANDATORY completion protocol for all experiments. Nothing is "complete" without: QC gate → scientific analysis → interpretation → cross-survey connection → site sync → queue expansion → backup. Every experiment must generate 5-15 new tasks.

**Pipeline 1 status:** See `project-context/pipeline1_tracer_purification_plan.md` — Steps 1-5 COMPLETE (2026-04-11). 5,384 QSO candidates classified (116 GOLD, 1,006 SILVER). Gold+Silver show 1.58x enhanced clustering bias but sample too small for σ(f_NL) improvement. Step 6 (Paper 3) remains.

**CURRENT WORK: AgenticUI → v4 Polish Sprint.** See `project-context/agenticui_v4_polish_plan.md`. 4-pass plan: Token foundation → Component swap → Spacing/density → Typography polish. Working on `/Users/houstongolden/Desktop/CODE_2025/hubify-labs-mockups/v4/` files. Reference: `hubify-labs-mockups/agenticui/` (26 components). Figma MCP for screenshot cross-checks only. Houston must approve DONE. Cron-looped until complete.

**Wiki:** See `wiki/SCHEMA.md` — Karpathy-style structured knowledge base with entities, concepts, sources, and comparisons. Updated on every research result.

## Website Architecture

The website at bigbounce.hubify.app is a multi-page static site deployed via Vercel from the `main` branch.

### Site Pages (all must stay in sync with research)

| Page | File | Purpose |
|------|------|---------|
| Homepage | `index.html` | Research overview, key results, stat cards, 14 barriers, ALP prediction, MCMC table, figures, claims table, falsification criteria |
| Papers | `paper.html` | Paper listing (2 papers with readiness %), version history timeline, full inline paper text |
| Explainer | `explained.html` | Accessible non-technical explanation of the research |
| Data Explorer | `data-explorer.html` | Interactive MCMC data tool with 15 embedded datasets, sortable tables, column stats, 6 equation calculators, node-tree visualization |
| Figures | `figures.html` | Gallery of 22 figures with lightbox viewer |
| Glossary | `glossary.html` | 13 equations gallery + 28-entry searchable glossary with pronunciations |
| Articles | `articles.html` | Index of 7 deep-dive articles |
| Activity | `activity.html` | Live research status banner, priority queue, chronological timeline feed |
| Timeline | `timeline.html` | Visual cosmological timeline from parent universe through bounce to SPHEREx 2028 |
| Visualize | `visualize.html` | Interactive dark-mode cosmic simulation of the Big Bounce |
| Dossier | `research/project_master_dossier/index.html` | Full project intelligence dashboard (integrated with site nav) |
| Datasets | `datasets.html` | Dataset descriptions and Cobaya config details |
| Articles (7) | `articles/*.html` | Individual article pages |

### Navigation

All pages share a consistent nav bar:
```
BigBounce | Research | Papers | Explainer | Data | Figures | Glossary | Articles | Timeline | Visualize | Activity | Dossier
```

The nav includes a mobile hamburger menu (`<button class="nav-toggle">`).

**Brand "BigBounce"** links to `index.html`. All nav links use `data-page` attributes for active-state highlighting.

**When adding or modifying pages:** Ensure the nav is consistent across ALL pages. Root pages use direct paths. Article subpages use `../` prefixes. Dossier uses `../../` prefixes.

### Styling

- `style.css` — shared CSS for the entire site (Newsreader serif + Inter sans + JetBrains Mono)
- Light mode, academic/technical aesthetic
- Uses CSS custom properties (--bg, --text, --border, --accent-link, etc.)
- Responsive with mobile breakpoints at 768px and 480px

## WEBSITE SYNC PROTOCOL

**CRITICAL: The website must always reflect the current state of the research.**

When ANY of the following change, the corresponding website pages MUST be updated:

### When research results change:
1. **`index.html`** — Update stat cards, key results, MCMC table, claims table, barrier count
2. **`explained.html`** — Update all scientific claims to match current findings
3. **`activity.html`** — Add new timeline entry at the top, update "Current Focus" banner and "Up Next" queue
4. **`data-explorer.html`** — If new MCMC chains complete or new datasets are created, embed the new data
5. **`paper.html`** — Update paper readiness percentages and version history

### When new data is generated:
1. **`data-explorer.html`** — Embed new dataset (chain samples, analysis results, etc.)
2. **`figures.html`** — Add any new figures to the gallery
3. **`glossary.html`** — Add any new parameters or equations
4. **`activity.html`** — Log the data generation event

### When new research branches open or close:
1. **`activity.html`** — Add timeline entry with appropriate color (green=positive, red=closed, blue=active)
2. **`index.html`** — Update stat cards if barrier count or positive result count changes
3. **`research/project_master_dossier/index.html`** — Update branch status table
4. **`data-explorer.html`** — Update branch results dataset

### When the paper manuscript changes:
1. **`paper.html`** — Update version history, readiness percentages
2. Recompile PDF and place in `arxiv/main.pdf`
3. Update `version.json`

### Quick-sync command:
When the user says **"update the site"** or **"sync the website"** or **"update the paper"**:
1. Check what has changed since the last git commit
2. Identify which pages are affected
3. Update all affected pages
4. Commit and push to deploy

## Repository Structure

### Canonical Sources
- `arxiv/main.tex` — canonical paper source (LaTeX)
- `arxiv/main.pdf` — compiled PDF
- `arxiv/references.bib` — bibliography
- `version.json` — current version metadata

### Research
- `research/foundation_*/` — Foundation studies A-G (7 structural barriers)
- `research/branch_*/` — Research branches H-W (17 branches)
- `research/paper2/` — Paper 2 tracks (WP4, WP5, P6, P7)
- `research/extensions/` — Observable extensions program
- `research/post_AG_pivot/` — Strategic pivot documents
- `research/final_phase/` — Paper structure, claims lock, figure plan
- `research/project_master_dossier/` — Full project intelligence dossier (12 markdown files + HTML dashboard)

### Projects & Pipelines
- `projects/` — Per-survey and per-topic research projects (nanograv, sdss-dr18, cross_survey, h200_scripts, desi-dr1-anomalies, erosita-xray, etc.)
- `pipelines/h200_results/` — H200 anomaly sweep outputs across all surveys
- `pipelines/p1_highz_tracers/` — High-z tracer purification for f_NL
- `pipelines/p2_chirality/` — Galaxy chirality catalog (8.47M galaxies, complete)
- `pipelines/p3_anomaly_engine/` — Multi-survey anomaly detection engine

### Reproducibility
- `reproducibility/cosmology/` — Cobaya YAML configs, MCMC chains, convergence diagnostics
- `reproducibility/cosmology/paper1_clean_restart_sync/chains/dneff/` — 4 datasets × 6-7 chains
- `reproducibility/galaxy_spins/` — Stan hierarchical model
- `reproducibility/docs/` — IMPLEMENTATION_MAP.md, KNOWN_GAPS.md

### Website
- `style.css` — shared stylesheet
- `*.html` — all site pages (root level)
- `articles/` — article subpages
- `articles/images/` — article images
- `public/images/` — publication figures (PNG, LFS-tracked)
- `public/spreadsheets/` — backing data (Excel/CSV)

### Data Files (for embedding in data explorer)
- Chain files: `reproducibility/cosmology/.../spin_torsion.1.txt` (space-delimited, 34-47 columns)
- **IMPORTANT column offset:** Header row starts with `#` which shifts column indices by +1. In data rows, column 1 = weight. In header, column 1 = `#`, column 2 = `weight`. So `H0` at header position 22 is at data position 21 for full_tension, and position 20 for other datasets (which have fewer columns).
- Summary CSVs: `convergence_latest.csv`, `chain_means_latest.csv`, `dataset_chain_map.csv`
- Parameter JSON: `research/final_paper_prep/full_tension_physical_parameters.json`
- Galaxy spin: `research/paper2/wp5_spin_amplitude/data/galaxy_spin_counts.csv`
- Spreadsheets: `public/spreadsheets/*.xlsx` and `*.csv`

## GPU Inference Playbook

**READ BEFORE any large-scale GPU inference job:** `project-context/gpu-inference-playbook.md`

Key rule: Always use `torch.utils.data.DataLoader` with `num_workers=16, pin_memory=True, prefetch_factor=4` for image inference. This gave us a **32x speedup** (29 min → 65s per 44K-image shard) on the galaxy chirality pipeline. Never use serial PIL decoding, `ProcessPoolExecutor`, or HuggingFace streaming for production inference.

## Paper Compilation & PDF Workflow

**All papers use `revtex4-2` (Physical Review D style).** This is critical for consistency — every paper from this lab must look identical in formatting.

### Document Class (MUST match across all papers)
```latex
\documentclass[aps,prd,twocolumn,superscriptaddress,showpacs,preprintnumbers,nofootinbib,longbibliography,floatfix]{revtex4-2}
```

### Author Format (same for all papers)
```latex
\author{Houston Golden}
\email{houston@hubify.com}
\affiliation{Independent Researcher, Los Angeles, California, USA}
```

### Compilation
Papers must be compiled on a machine with `texlive-publishers` installed (for `revtex4-2`). **As of 2026-05-12 the local Mac DOES have LaTeX via Homebrew TeX Live 2026** (`/opt/homebrew/bin/pdflatex`) and is the preferred local-compile path for fast iteration. RunPod pods can also compile if `texlive-publishers` is installed; cobaya-only pods do not have LaTeX pre-installed.

```bash
# On RunPod pod (H200 or H100):
apt-get install -y texlive-latex-extra texlive-fonts-recommended texlive-science texlive-publishers

# Compile (run twice for cross-references):
cd /workspace/chirality   # or wherever the .tex file is
pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex
```

### Figure Handling
- All figures MUST be in the SAME directory as the `.tex` file (or symlinked there)
- Use `\includegraphics[width=\columnwidth]{fig_name.png}` — NOT full paths
- Check PDF file size: if < 1MB, figures are NOT embedded (they showed as empty boxes)
- A paper with 11 figures should be ~15-25MB

### Paper Locations
| Paper | Source | PDF | Figures |
|-------|--------|-----|---------|
| Paper 1 (Spin-Torsion) | `arxiv/main.tex` | `arxiv/main.pdf` | `public/images/` |
| Paper 2 (f_NL Forecast) | `research/focused_paper_source_integration/02_full_draft.tex` | — | — |
| Paper 3 (Anomaly Catalog) | `pipelines/p3_anomaly_engine/` | — | — |
| Paper 4 (Chirality Catalog) | `pipelines/p2_chirality/chirality_catalog_paper.tex` | `public/papers/chirality_catalog_paper.pdf` | `public/images/chirality/` |

### Publishing PDFs to the Website
PDFs go in `public/papers/` and are linked from `paper.html`, `galaxy-explorer.html`, etc.
```bash
# After compiling on pod:
scp -P {PORT} -i ~/.ssh/id_ed25519 root@{IP}:/path/to/paper.pdf public/papers/
git add public/papers/paper.pdf
git commit -m "feat: compiled paper PDF"
git push origin main  # auto-deploys to Vercel
```

### Common Pitfalls
- **Empty figure boxes in PDF**: Figures not in same directory as .tex. Symlink or copy them.
- **`aastex631` class errors**: Do NOT use aastex. Use `revtex4-2` for all papers.
- **`\citep`/`\citet` undefined**: revtex4-2 uses `\cite{}` — not natbib commands.
- **`deluxetable` undefined**: Use `\begin{table}\begin{ruledtabular}\begin{tabular}` instead.
- **364KB PDF**: Figures not embedded. Recompile with figures in the same directory.
- **Text overflowing the column / overlapping the other column** → see [`AGENT_RULES.md` §4.7](AGENT_RULES.md). Mandatory post-compile visual audit, use `\artifact{}` for every repo path, `table*`/`figure*` for anything wider than a column, never stuff long notes into `\date{}`.

## Commands

### Local Development
```bash
npm install        # Only Express needed
node server.js     # http://localhost:3000
```

### Deployment
- Vercel auto-deploys from `main` branch
- `git push origin main` triggers deployment
- No build step — purely static

### After any research session:
```bash
# 1. Update affected website pages
# 2. Commit research + website changes together
git add [changed files]
git commit -m "feat: [description]"
git push origin main   # Auto-deploys to bigbounce.hubify.app
```

## Peer Review & Revision Workflow

**All peer reviews saved to `project-context/peer-reviews/`.**

File naming: `YYYY-MM-DD_HHMMtz_description.md`

Revision tracker: `project-context/peer-reviews/REVISION_TRACKER.md`

After each revision round:
1. Recompile PDF (0 undefined references)
2. Run dimensional consistency checks
3. Verify claims table against revised text
4. **Sync website** (update index.html, explained.html, activity.html, data-explorer.html as needed)
5. Update REVISION_TRACKER.md
6. Commit and push

## Prompt History Log — CRITICAL: Houston worries about losing his thoughts to compaction

**File:** `project-context/prompt-history.md`

This is the canonical running log of every substantive Houston message across all Claude Code sessions. Houston spends a lot of time writing brain dumps and strategic thoughts here that he cannot afford to lose. **The file is the safety net against context compaction.**

### Save protocol — proactive, not deferred (Houston flagged 2026-04-08)

**Save EVERY substantive Houston message immediately, verbatim, before continuing other work.** Do NOT batch. Do NOT wait for end-of-session. Compaction can happen at any time and the messages must already be on disk before that point.

A "substantive" Houston message is one that contains:
- Strategic direction, vision, or roadmap
- Feature requests or design feedback
- Architectural decisions or definitions
- Brain dumps, musings, "thinking out loud"
- Pushback, course-correction, or emphasis

Do NOT save:
- Cron-fired autonomous loop prompts (those are not Houston's words)
- One-line acknowledgements ("ok", "yes", "go")
- Pure tool invocations (`/loop`, `/qa`, etc.) unless they contain free-text context
- Pod watchdog auto-prompts

### Workflow — every iteration

1. **When Houston sends a substantive message:** Append it to `project-context/prompt-history.md` BEFORE doing the work he asked for. The append takes ~2 seconds; doing it first guarantees survival.
2. **At the START of every session:** Read the most recent section of `prompt-history.md` to recover context. If you need full history, scan `.jsonl` session files in `~/.claude/projects/-Users-houstongolden-Desktop-CODE-2025-bigbounce/`.
3. **After context compaction:** Re-append any messages that came in DURING the work that was compacted (the summary may have lost the verbatim text).

### Format

Each session gets a `## YYYY-MM-DD — <session topic>` header. Within a session:
- Brief framing line about the session
- A sub-header `### Houston substantive messages, verbatim`
- Each message prefixed with `**HH:MM PT — <one-line context>**` and blockquoted with `>`
- Long messages stay verbatim — do NOT truncate Houston's brain dumps. The whole point is preservation. If a message is over 1500 chars, save it whole anyway. Disk is cheap.

### Why this matters

Houston has been writing detailed strategic messages for weeks. Several were lost in earlier sessions when compaction happened mid-conversation and the verbatim text only existed in the compacted summary. Each lost message is a real cost to him because he has to re-type the same idea. The file is the lossless backup. **Treat the save as load-bearing, not optional.**

## Skill routing

When the user's request matches an available skill, ALWAYS invoke it using the Skill
tool as your FIRST action. Do NOT answer directly, do NOT use other tools first.
The skill has specialized workflows that produce better results than ad-hoc answers.

Key routing rules:
- Product ideas, "is this worth building", brainstorming → invoke office-hours
- Bugs, errors, "why is this broken", 500 errors → invoke investigate
- Ship, deploy, push, create PR → invoke ship
- QA, test the site, find bugs → invoke qa
- Code review, check my diff → invoke review
- Update docs after shipping → invoke document-release
- Weekly retro → invoke retro
- Design system, brand → invoke design-consultation
- Visual audit, design polish → invoke design-review
- Architecture review → invoke plan-eng-review
- Save progress, checkpoint, resume → invoke checkpoint
- Code quality, health check → invoke health

## Contact

Author: Houston Golden
Email: houston@hubify.com
Website: https://bigbounce.hubify.app
GitHub: https://github.com/Hubify-Projects/bigbounce
