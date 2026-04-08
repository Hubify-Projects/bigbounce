# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## CRITICAL RESEARCH DIRECTIVE

**DO NOT suggest "write up the results and publish" or "document the barriers as a paper" as a next step.** The goal of this project is continued active research toward positive scientific discoveries — specifically, finding meaningful evidence that bounce cosmology fits observational and mathematical constraints better than ΛCDM + inflation. After negative results, always propose the next research direction that could yield a positive discovery. Treat barriers as constraints that narrow the search space, not as conclusions. Continue researching until genuine positive results are found.

## Project Overview

This repository contains a comprehensive spin-torsion cosmology research program by Houston Golden, including a scientific paper, a full companion website, MCMC reproducibility infrastructure, and a project intelligence dossier.

**Current version: v2.2.0** (March 2026) — ~24 pages (focused version), 63+ bibliography entries, 10+ revision rounds complete.

**Live website:** https://bigbounce.hubify.app

**Research stance:** Bounce-model agnostic. The goal is proving bounce cosmology beats inflation, not proving one specific model. See `project-context/bounce_portfolio_strategy.md`.

**Key scientific results:**
- 14 structural barriers close all ECH-specific routes from bounce to dark energy (other bounce models like quintom can bypass these)
- ALP birefringence prediction β = 0.27° matches 3.6σ observed signal (0.342 ± 0.094°)
- Branch V matter bounce: f_NL = -35/8 = -4.375 (parameter-free, SPHEREx testable, mechanism-independent across all bounce models)
- Bounce model discrimination table: matter bounce vs Cuscuton vs ekpyrotic vs quintom vs inflation
- f_NL triple role: galaxy bispectrum + PBH abundance regulator + induced GW spectral shape
- NANOGrav 15yr consistency: matter bounce γ = 3.0 vs observed 3.2 ± 0.6 (0.33σ)
- w0-wa MCMC: quintom-B (w-crossing) favored at 2.3σ, P(quintom-B) = 98.6%
- MCMC verification: ΔNeff ≈ 0 in all datasets; H₀ = 67.68 (standard ΛCDM)
- 424,181+ MCMC posterior samples across 3 frozen dataset combinations
- Multi-survey anomaly sweep (8 surveys, 33.5M sources, 328,448 anomalies total):
  - DESI DR1: 22.5M spectra, 195,829 anomalies (0.87%), 2,145 SNR-filtered, 1,127 uncataloged
  - SDSS DR18: 2.3M spectra, 77,905 anomalies (3.4%) — QC: domain shift scores
  - eROSITA DR1: 930K sources, 9,303 anomalies (1%), 73% novel
  - LAMOST DR10: 11.4M spectra, 44,075 anomalies (0.39%) — QC: 98% blue-excess bias
  - Planck CMB: 20K patches, 200 anomalies — QC FAIL: needs galactic mask
  - ACT DR6: 20K patches, 200 anomalies — QC FAIL: undertrained (val_loss=22,420)
  - NEOWISE: 43.5K sources, 436 anomalies — QC FAIL: ecliptic systematic
  - Gaia DR3: 50K sources, 500 anomalies — needs 10x expansion
- f_NL Fisher forecast (corrected): σ(f_NL) = 8.98 standard, 8.12 multi-tracer
- f_NL multi-tracer improvement: 6.1% (DESI), 16.4% (DESI+SDSS). SPHEREx 4.38σ forecast.
- f_NL bias validation: extreme anomalies show 2.28x clustering bias vs baseline (Landy-Szalay w(θ))
- Combined PTA (NANOGrav+EPTA+PPTA+IPTA): γ = 3.32 ± 0.37, bounce at 0.9σ, SMBHB excluded at 2.7σ, Bayes factor 27.6

**Pod status (as of 2026-04-06):** H200 pod `o76k3jfzbfh25e` (sleepy_blush_crane) ACTIVE. SSH: `root@205.196.19.52 -p 11452`. Phases 1-3 COMPLETE (17/18 experiments). Phase 4 RUNNING (f_NL science + NANOGrav, 5 experiments in tmux `phase4`). See `project-context/active_pods_and_pipelines.md`.

**Houston Method v2:** See `project-context/houston-method-v2.md` — MANDATORY completion protocol for all experiments. Nothing is "complete" without: QC gate → scientific analysis → interpretation → cross-survey connection → site sync → queue expansion → backup. Every experiment must generate 5-15 new tasks.

**Pipeline 1 next steps:** See `project-context/pipeline1_tracer_purification_plan.md` — Steps 2-6 (cross-match, classify, validate bias, re-measure σ(f_NL), paper) are the novel work. NOT STARTED.

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
Papers must be compiled on a machine with `texlive-publishers` installed (for `revtex4-2`). Local Mac does NOT have LaTeX — compile on RunPod pods.

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
