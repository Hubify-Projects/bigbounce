# Product Architecture Audit v2: BigBounce → Hubify Platform Cohesion

**Date:** 2026-03-12 (updated)
**Auditor:** Claude Opus 4.6
**Scope:** Full codebase re-audit on latest main (v1.3.0, commit 8c88a1c) + Hubify repo connection check
**Previous audit:** 2026-03-11_0000PST_product-architecture-audit.md

---

## Executive Summary

BigBounce is a **self-contained research paper repository** under the Hubify-Projects GitHub org. It has evolved from a static paper website into a proto-platform with ~3,500 lines of Python research agent code, 12 API integrations, GPU compute (RunPod), and a polished 12-page website. However:

1. **BigBounce has ZERO code connections to any Hubify platform.** No submodules, no npm @hubify packages, no imports, no shared code. The only Hubify touchpoints are: org name, domain (hubify.app), email (hubify.com), Convex backend mention (1 line), and preprint ID format (HUBIFY-2026-001).

2. **No Hubify platform repos exist yet.** Checked for repos named hubify, openclaw, moltbook, hubify-cli under Hubify-Projects — none found. The three-pillar vision (OpenClaw, Agent Squads, Social Knowledge Network) exists only as a concept, not as code.

3. **BigBounce is the most mature Hubify product** — and it doesn't know it's a Hubify product. The agent infrastructure here is the embryo of the platform, but it's hardcoded for this one research paper.

**Bottom line:** BigBounce should be refactored to become the **reference implementation** of a Hubify Hub. The research agent code should be extracted into a reusable Hubify SDK/framework. And the `.hubify/` directory convention should become the standard for all hubs.

---

## Hubify Repo Connection Analysis

### What connects BigBounce to Hubify?

| Connection Type | Details | Strength |
|----------------|---------|----------|
| GitHub Org | Lives under `Hubify-Projects/bigbounce` | Organizational only |
| Domain | bigbounce.hubify.app (Vercel) | DNS/branding only |
| Email | houston@hubify.com | Contact only |
| Preprint ID | HUBIFY-2026-001 format | Naming convention only |
| Convex mention | `.env.example` line 9: "Hubify Convex backend has its own keys for workspace agents" | 1 comment, no code |
| Squad init | `.hubify/squad-init.md` — "Initialized by Hubify Squad Automation" | 24-line markdown stub |
| Agent names | astro-atlas-v1, astro-tensor-v1, etc. — in AGENTS.md and methodology.html | Persona metadata |

### What does NOT exist?

- No `Hubify-Projects/hubify` repo
- No `Hubify-Projects/openclaw` repo
- No `Hubify-Projects/moltbook` repo
- No `Hubify-Projects/hubify-cli` repo
- No git submodules in bigbounce
- No @hubify npm packages
- No `import hubify` or `from hubify` in any Python file
- No Hubify API endpoints called from code
- No shared authentication/auth tokens with a Hubify backend
- No Convex integration code (only a comment mentioning it)

### Implication

**BigBounce is operating as an island.** The Hubify platform vision exists conceptually but has no code foundation outside this repo. This means:
- BigBounce's research agents ARE the Hubify agent system (there's no other one)
- BigBounce's `.hubify/` IS the only `.hubify/` convention (it defines the standard)
- BigBounce's website IS the first Hubify Hub (it just doesn't have hub features yet)

This is actually an advantage — BigBounce can define the patterns that the platform inherits, rather than conforming to an existing platform API.

---

## Current State: 8 Disconnected Products (Updated)

### 1. Paper Website (Static HTML) — 12 pages, ~10,000 lines
**Files:** index.html, paper.html, explained.html, mathematics.html, datasets.html, galaxy-zoo.html, methodology.html, sources.html, animations.html, versions.html, data-comparison.html, arxiv-preview.html, style.css, interactive-data.html
**Status:** Production-quality, deployed at bigbounce.hubify.app via Vercel
**Problem:** All 12+ HTML files in root directory, mixed with Python scripts, configs, documentation. No CMS, no templating — raw HTML hand-edited. Password-gated (client-side "houston"). No connection to agent outputs.

### 2. Research Agent Toolkit (Python) — 9 modules, ~2,000 lines
**Files:** research/agents/{reasoning_router, literature_search, computation, data_access, dataset_loaders, galaxy_zoo, spin_analysis, galaxy_classifier, data_audit}.py
**Status:** Functional, tested, all APIs configured
**Problem:** BigBounce-specific. Not packaged or importable as a library. No orchestrator. No shared state. Each module independently loads env vars via dotenv. No inter-agent communication. Functions are skills but aren't declared as skills.

### 3. GPU Compute Layer (RunPod) — 2 files, ~1,065 lines
**Files:** research/runpod_cloud.py (pod lifecycle), research/runpod_gpu_session.py (11-cell runner)
**Status:** Working, RTX 6000 Ada pod configured
**Problem:** Hardcoded pod ID (47htajss1ng2ig). Session runner has BigBounce-specific cells. Not abstracted for other projects. runpod_gpu_session.py duplicates Colab notebook logic.

### 4. Reproducibility Package — 4 MCMC configs + Stan model
**Files:** reproducibility/ AND arxiv/reproducibility/ (duplicated!)
**Status:** Complete, documented gaps, implementation map
**Problem:** Exists in TWO directories. Not connected to agent system. Manual execution only. Results don't auto-flow anywhere.

### 5. Data Pipeline — CSV → JSON/XLSX
**Files:** scripts/build_data.py, data/figures/, public/data/, .github/workflows/build-data.yml
**Status:** CI pipeline works, generates JSON + JSONP + Excel
**Problem:** Website still uses inline data (feature flag `flagNewData()` guards new pipeline). Migration incomplete. Build runs but doesn't deploy.

### 6. Figure Generator — 8 figures, 30,591 bytes
**Files:** generate_all_figures.py, arxiv/figures/
**Status:** Generates all 8 publication figures
**Problem:** Monolithic single file. Data hardcoded inline. Not connected to data pipeline or agent outputs.

### 7. Configuration & Documentation Sprawl
**Files:**
- config/eb_forecast_params.yml (1 YAML config)
- .hubify/squad-init.md (24-line stub)
- .env.example (93 lines, well-documented)
- AGENTS.md (595 lines), CLAUDE.md (100 lines), README.md
- project-context/: PRD.md, ARCHITECTURE.md, IMPLEMENTATION_PLAN.md, IMPLEMENTATION_TODOS.md, CURRENT_STATUS.md, tech-stack.md, RESEARCH_TOOLS_INTEGRATION.md, ARXIV_AUDIT.md, + peer reviews
**Problem:** 10+ documentation files describing overlapping/outdated visions. PRD describes a paper website. AGENTS.md describes a research platform. Neither describes the three-pillar Hubify vision. Config in config/ is disconnected from squad-init in .hubify/. CURRENT_STATUS.md says v1.0.0 but version.json says v1.3.0.

### 8. Deployment & Legacy Clutter
**Files:**
- netlify.toml + vercel.json (two deployment configs)
- server.js (Express dev server, port 3003)
- index.html.backup, index.html.before-reorganization, index.html.duplicates-removed, index.html.backup-reorganization (4 backup files)
- bigbounce-md.html, interactive-data-simple.html (deprecated alternatives)
- github-image-mappings.md, image-urls.md (image URL tracking)
**Problem:** Two deployment targets. Four backup files cluttering root. Two deprecated HTML alternatives. Dev server vestigial (any static server works).

---

## Three-Pillar Cohesion Scores (Updated)

### Pillar 1: AI OS / OpenClaw — Score: 2/10

| Component | Exists? | Maturity |
|-----------|---------|----------|
| Hub manifest (.hubify/hub.yaml) | No | - |
| Squad config (structured YAML) | No (24-line markdown stub) | 0/10 |
| Agent souls/personalities | Partial (HTML display cards only) | 2/10 |
| Task/project system | No (flat markdown checklist) | 0/10 |
| Dashboard/admin UI | No | - |
| Shared memory/context | No | - |
| Local CLI sync | No (no CLI exists) | - |
| Template system | No | - |
| OpenClaw runtime | No (concept only) | - |

### Pillar 2: Agent Squads & Missions — Score: 5/10

| Component | Exists? | Maturity |
|-----------|---------|----------|
| Agent modules | Yes (9 Python files) | 7/10 |
| Multi-model routing | Yes (7 LLMs) | 8/10 |
| Research API integrations | Yes (12 APIs) | 7/10 |
| GPU compute (RunPod) | Yes (full lifecycle) | 7/10 |
| Dataset access (HF/MAST/Gaia) | Yes (30+ datasets) | 6/10 |
| Mission orchestrator | No | - |
| Agent registry | No | - |
| Skills system | No (functions exist, not declared as skills) | 1/10 |
| Mission state tracking | No | - |
| Collective knowledge layer | No (flat JSON outputs) | 1/10 |
| Inter-agent communication | No | - |
| Agent memory/learning | No | - |

### Pillar 3: Social Knowledge Network — Score: 1/10

| Component | Exists? | Maturity |
|-----------|---------|----------|
| Public website | Yes (12 pages, polished) | 8/10 |
| Version history | Yes (13 versions tracked) | 7/10 |
| Interactive data exploration | Yes (Chart.js visualizations) | 6/10 |
| Preprint ID system | Yes (HUBIFY-2026-001) | 3/10 |
| Public data API | No | - |
| Hub-to-hub connections | No | - |
| User accounts/profiles | No | - |
| Comments/discussion | No | - |
| Fork/remix capability | No | - |
| Knowledge graph | No | - |
| Social feed/activity | No | - |
| Skill marketplace | No | - |

---

## Recommended Architecture (Updated for No External Hubify Repo)

Since there's no external Hubify platform to integrate with, BigBounce must **define** the conventions. This repo should serve dual purpose:

1. **A working research project** (BigBounce paper)
2. **The reference implementation** of Hubify Hub conventions

### Phase 1: Define the Hub Convention (`.hubify/` spec)

Create the `.hubify/` directory structure that ALL future Hubify Hubs will follow:

```
.hubify/
├── hub.yaml              # Hub manifest (identity, type, visibility, tags)
├── squad.yaml            # Agent team (replaces squad-init.md)
├── missions/             # Research mission definitions + state
│   ├── _schema.yaml      # Mission YAML schema
│   ├── paper-v1.yaml     # [completed] Write & publish paper v1.0
│   ├── mcmc-verify.yaml  # [completed] Independent MCMC verification
│   ├── galaxy-spin.yaml  # [completed] Galaxy spin analysis
│   └── v2-extensions.yaml # [planned] Future predictions & tests
├── skills/               # Skill declarations (what agents CAN do)
│   ├── _schema.yaml
│   ├── literature-search.yaml
│   ├── equation-verify.yaml
│   ├── mcmc-run.yaml
│   ├── data-access.yaml
│   └── figure-generate.yaml
├── knowledge/            # Collective knowledge (what agents KNOW)
│   ├── claims.yaml       # Paper claims (derived/assumed/fit)
│   ├── findings.yaml     # Key results with uncertainties
│   └── open-questions.yaml
└── context/              # Shared memory (what agents REMEMBER)
    ├── paper-state.yaml
    └── session-history/
```

### Phase 2: Separate Website from Platform

```
# Before (current): everything in root
bigbounce/
├── index.html           # mixed with...
├── paper.html
├── research/agents/     # ...Python code...
├── scripts/             # ...build scripts...
├── AGENTS.md            # ...and documentation

# After: clean separation
bigbounce/
├── .hubify/             # Hub convention (Pillar 1)
├── agents/              # Agent infrastructure (Pillar 2)
│   ├── skills/          # research/agents/*.py moved here
│   ├── compute/         # research/runpod_*.py moved here
│   ├── router.py
│   ├── orchestrator.py
│   └── registry.yaml
├── site/                # Public hub output (Pillar 3)
│   ├── index.html
│   ├── paper.html
│   ├── ...all HTML...
│   ├── style.css
│   └── public/          # Static assets
├── arxiv/               # Paper source (unchanged)
├── data/                # Research data (unchanged)
├── scripts/             # Build scripts (unchanged)
└── research/outputs/    # Research artifacts (unchanged)
```

### Phase 3: Build the Connective Tissue

The critical missing piece is the **data flow** between pillars:

```
.hubify/missions/paper-v1.yaml
  → defines: what skills to run, in what order
  → orchestrator reads this

agents/orchestrator.py
  → loads mission YAML
  → sequences skill calls (literature → computation → data → figures)
  → saves outputs to research/outputs/
  → updates .hubify/knowledge/ with findings

scripts/build_site.py
  → reads .hubify/knowledge/claims.yaml
  → reads .hubify/knowledge/findings.yaml
  → generates/updates site/ pages
  → deploys to bigbounce.hubify.app

Result: agent work → structured knowledge → public website
(Currently: agent work → JSON files → manual HTML editing)
```

### Phase 4: Extract Hubify SDK (Future — When Building Other Hubs)

Once BigBounce proves the pattern, extract reusable pieces into `Hubify-Projects/hubify`:

```
hubify/
├── cli/                 # hubify CLI (init, sync, deploy)
├── sdk/                 # Agent SDK (orchestrator, router, skills framework)
├── templates/           # Hub templates (research-paper, data-project, etc.)
└── hub-spec/            # .hubify/ directory specification
```

---

## Priority Action Items (Revised)

### P0 — Today (Housekeeping)

1. **Delete backup files** — index.html.backup*, bigbounce-md.html, interactive-data-simple.html (6 files, all in git history)
2. **Pick one deployment** — Keep vercel.json (currently live), remove netlify.toml
3. **Fix version drift** — CURRENT_STATUS.md says v1.0.0 but version.json says v1.3.0
4. **Consolidate reproducibility/** — Single location in arxiv/reproducibility/ or root reproducibility/ (not both)

### P1 — This Week (Hub Convention)

5. **Create `.hubify/hub.yaml`** — First-ever Hubify Hub manifest
6. **Upgrade `.hubify/squad.yaml`** — From 24-line markdown to structured YAML with agent configs
7. **Create `.hubify/knowledge/claims.yaml`** — Structured claims from peer review docs
8. **Create `.hubify/knowledge/findings.yaml`** — Key paper results with metadata
9. **Create `.hubify/missions/`** — Retroactively document completed research missions

### P2 — Next Sprint (Separation)

10. **Move HTML to `site/`** — All 12+ pages + style.css + public/
11. **Move research/agents/ to `agents/skills/`** — Clarify these are skills
12. **Move research/runpod_*.py to `agents/compute/`** — Clarify this is infrastructure
13. **Create `agents/registry.yaml`** — Catalog all agents and skills
14. **Update deployment config** — vercel.json publishes from site/

### P3 — Next Month (Orchestration)

15. **Build `agents/orchestrator.py`** — Mission runner
16. **Build `scripts/build_site.py`** — Knowledge layer → site generator
17. **Create `agents/memory/`** — Session history and learned patterns
18. **Remove password protection** — Public knowledge hub
19. **Add `site/api/`** — JSON endpoints for claims, findings, datasets

### P4 — Future (Platform Extraction)

20. **Create `Hubify-Projects/hubify` repo** — Extract reusable SDK
21. **Create `hubify init` CLI** — Scaffold new hubs from templates
22. **Create hub discovery** — Index of all Hubify Hubs
23. **Build social features** — Comments, forks, knowledge graph

---

## Risk: Premature Abstraction

A word of caution: the three-pillar vision is ambitious, and BigBounce is currently serving its primary purpose well (publishing a research paper). The restructuring should be **incremental** and should not break the existing deployed website.

Recommended approach:
1. Start with `.hubify/` convention files (low risk, high signal)
2. Move HTML to site/ only when ready to update deployment config
3. Build orchestrator only after skills are properly declared
4. Don't extract a Hubify SDK until there's a second hub to validate the patterns

**Ship the convention, then the code.**

---

## Appendix: Complete File Inventory (336+ files)

### Root Directory (39 files)
- 12 HTML pages (index, paper, explained, mathematics, datasets, galaxy-zoo, methodology, sources, animations, versions, data-comparison, arxiv-preview)
- 2 interactive data pages (interactive-data.html, interactive-data-simple.html)
- 4 backup HTML files (index.html.backup*)
- 1 deprecated HTML (bigbounce-md.html)
- 1 CSS file (style.css)
- 1 JS file (server.js)
- 1 Python script (generate_all_figures.py)
- 4 config files (package.json, netlify.toml, vercel.json, version.json)
- 5 markdown docs (README.md, CLAUDE.md, AGENTS.md, bigbounce.md, github-image-mappings.md, image-urls.md)
- 3 git files (.gitattributes, .gitignore, .lfsconfig)

### .hubify/ (1 file)
- squad-init.md

### arxiv/ (~20 files)
- main.tex, main.pdf, main.bbl, main.bib, references.bib
- 8 figure PNGs
- reproducibility/ (bash scripts, configs)
- README-SUBMISSION.txt

### paper/ (31 files)
- 00-abstract.md through 11-acknowledgments.md + metadata.md

### research/ (~15 files)
- agents/ (9 Python modules)
- runpod_cloud.py, runpod_gpu_session.py
- env_check.py
- outputs/ (25+ JSON/markdown artifacts)

### scripts/ (5 files)
- build_data.py, eb_forecast.py, download_galaxy_zoo.py, spin_fit_stan.py, figure_checks.py

### reproducibility/ (~10 files)
- 4 Cobaya YAMLs, Stan model, 2 bash scripts, 2 docs

### config/ (1 file)
- eb_forecast_params.yml

### public/ (~40+ files)
- images/ (figures), data/ (JSON), downloads/ (PDF, XLSX), spreadsheets/ (XLSX)

### project-context/ (~15 files)
- PRD.md, ARCHITECTURE.md, IMPLEMENTATION_PLAN.md, IMPLEMENTATION_TODOS.md, CURRENT_STATUS.md, tech-stack.md, RESEARCH_TOOLS_INTEGRATION.md, ARXIV_AUDIT.md
- peer-reviews/ (4 review docs + tracker)

### versions/ (2 files)
- manifest.json, changelog history

### .github/ (1 file)
- workflows/build-data.yml
