# Product Architecture Audit: BigBounce → Hubify Platform Cohesion

**Date:** 2026-03-11
**Auditor:** Claude Opus 4.6
**Scope:** Full codebase audit mapping current state to three-pillar product vision

---

## Executive Summary

The BigBounce repository has evolved from a single research paper website into a **proto-platform** containing the seeds of three distinct product layers — but these layers are currently tangled together in a flat repo with no clear boundaries. The research infrastructure (agents, APIs, GPU compute) is impressive but lives as loose Python scripts. The web presentation is polished but entirely paper-specific. And the social/knowledge-sharing layer exists only as implied future vision.

**Bottom line:** You have ~80% of the building blocks. What's missing is the architecture that separates platform from project, and the connective tissue between the three pillars.

---

## The Three Pillars — Current State Assessment

### Pillar 1: AI OS / OpenClaw
**Vision:** Custom agent operating systems with templates, dashboards, projects, tasks, shared data/memory/context, syncing locally via Hubify CLI

**What exists today:**
- `.hubify/squad-init.md` — Squad definition (5 agents, roles, phases) — **24 lines, metadata only**
- `AGENTS.md` — 595-line context document for AI agents (instructions, not executable)
- `methodology.html` — Agent persona cards (astro-sage, astro-nova, etc.) displayed on website
- `research/agents/reasoning_router.py` — Multi-model routing to 7 LLM providers
- `.env.example` — 12 API keys across LLM, science, and compute providers
- `config/` — YAML configs for agents, analyses, data builds, notebooks

**What's missing:**
- No OpenClaw runtime, CLI, or daemon
- No agent state management (memory, context persistence between sessions)
- No task/project system — IMPLEMENTATION_TODOS.md is a flat markdown checklist
- No dashboard or admin UI — methodology.html shows agent cards but is read-only
- No local sync mechanism (no Hubify CLI integration)
- No template system for spawning new projects from this pattern
- Squad init is a markdown file, not executable config
- Agent "souls" referenced in HTML but never defined as executable personality configs
- No shared data layer between agents (each script loads its own .env independently)

**Cohesion score: 2/10** — Scattered building blocks, no unifying runtime

---

### Pillar 2: Agent Squads & Research Missions
**Vision:** Independent/connected agent squads with research APIs (HuggingFace, Wolfram, NASA, arXiv, RunPod), agent registry, skills, collective knowledge

**What exists today:**
- `research/agents/` — 9 Python modules (reasoning_router, literature_search, computation, data_access, dataset_loaders, galaxy_zoo, spin_analysis, galaxy_classifier, data_audit)
- `research/runpod_cloud.py` — Full RunPod pod lifecycle management (GraphQL API)
- `research/runpod_gpu_session.py` — 11-cell GPU session runner (RunPod/Colab/local)
- `scripts/` — 5 research scripts (eb_forecast, build_data, download_galaxy_zoo, spin_fit_stan, figure_checks)
- `reproducibility/` — MCMC configs (4 Cobaya YAMLs), Stan models, bash runners
- `research/outputs/` — 25+ JSON/markdown artifacts from research runs
- `generate_all_figures.py` — 8 publication-quality figure generators
- API integrations: NASA ADS, Semantic Scholar, arXiv, MAST/JWST, Gaia, VizieR, NED, Wolfram Alpha, HuggingFace (MMU 100TB), Polymathic AI, RunPod GPU
- `.github/workflows/build-data.yml` — CI pipeline for data builds

**What's missing:**
- No mission orchestrator — research cells are numbered but manually sequenced
- No agent registry — agents are just Python files, no discovery/versioning/sharing
- No skills system — functions exist but aren't packaged as composable skills
- No collective knowledge layer — outputs are flat JSON files in a directory
- No mission state tracking — no way to pause/resume/fork research missions
- No inter-agent communication — each agent module is standalone
- No results aggregation — outputs scattered across research/outputs/, public/data/, arxiv/
- RunPod integration is project-specific, not reusable across Hubify projects
- Research pipeline (`RESEARCH_TOOLS_INTEGRATION.md` Phase 3) remains unbuilt
- No way for agents to learn from previous mission results

**Cohesion score: 5/10** — Strong individual tools, no orchestration layer

---

### Pillar 3: Social Knowledge Network
**Vision:** Agent-driven social knowledge network (hubs, public research, shared knowledge/skills — Moltbook meets GitHub meets Wiki)

**What exists today:**
- Website (bigbounce.hubify.app) — public-facing research presentation
- `versions/manifest.json` — 13-version changelog with detailed diffs
- `versions.html` — Public version history page
- `project-context/peer-reviews/` — Revision tracking with claims tables
- `explained.html` — Plain-language research explainer
- `interactive-data.html` / `galaxy-zoo.html` — Public data exploration
- `sources.html` — Bibliography with cross-references
- Preprint ID system: HUBIFY-2026-001

**What's missing:**
- No hub/community system — this is a one-way publishing site
- No user accounts, profiles, or contributions
- No commenting, discussion, or peer review UI
- No way to fork/remix research (despite having all data publicly)
- No knowledge graph connecting this paper to other Hubify projects
- No shared skill marketplace
- No social feed or activity stream
- No collaborative editing
- No public API for programmatic access to research data
- Password protection ("houston") is the opposite of open knowledge sharing

**Cohesion score: 1/10** — Publishing exists, social layer does not

---

## Disconnected Products & Parts Identified

### 1. The Paper Website (Static HTML)
**Files:** index.html, paper.html, explained.html, mathematics.html, datasets.html, galaxy-zoo.html, methodology.html, sources.html, animations.html, versions.html, style.css
**What it is:** A polished, MathJax-powered academic paper presentation
**Disconnection:** Completely static. No connection to the agent system that built it. No way for agents to update it automatically. No API. No CMS. Changes require manual HTML editing.

### 2. The Research Agent Toolkit (Python)
**Files:** research/agents/*.py, research/runpod_*.py, scripts/*.py
**What it is:** A powerful but loose collection of research tools
**Disconnection:** These scripts have no awareness of the website they support. No pipeline connects research outputs → website updates. Each module loads env vars independently. No shared state, no orchestration, no agent-to-agent communication.

### 3. The Reproducibility Package (MCMC/Stan)
**Files:** reproducibility/, arxiv/reproducibility/
**What it is:** Cobaya MCMC configs, Stan models, bash runners
**Disconnection:** Duplicated across two directories (arxiv/reproducibility/ and reproducibility/). Not integrated with the agent system. Requires manual execution. Results don't flow back to the website.

### 4. The Data Pipeline (Python → JSON)
**Files:** scripts/build_data.py, data/, public/data/
**What it is:** CSV → JSON/JSONP/XLSX converter for web consumption
**Disconnection:** Build pipeline exists but website still has extensive inline/hardcoded data. Feature flag (`flagNewData()`) suggests migration is incomplete. GitHub Actions builds data but doesn't deploy.

### 5. The Configuration Layer
**Files:** config/*, .env.example, .hubify/squad-init.md
**What it is:** YAML configs for various agent tasks
**Disconnection:** config/ mirrors research/ directory structure but relationship is unclear. Are configs consumed by the Python scripts? Or are they aspirational templates? Squad init is 24 lines of markdown, not operational config.

### 6. The Project Context / Documentation
**Files:** project-context/*.md, AGENTS.md, CLAUDE.md, README.md
**What it is:** Extensive project documentation, PRDs, architecture docs
**Disconnection:** Multiple overlapping docs (PRD.md describes a paper website, AGENTS.md describes a research platform, CLAUDE.md bridges both). Architecture docs describe current static site, not the platform vision. Implementation plan completed for paper website but doesn't cover platform evolution.

### 7. Deployment Configuration
**Files:** netlify.toml, vercel.json, server.js
**What it is:** Triple deployment setup (Netlify + Vercel + Express)
**Disconnection:** Two production deployment configs for one static site. Vercel has URL rewrites that Netlify doesn't. SPA-style 404→index.html routing on Netlify conflicts with multi-page nature. Express server on port 3003 is vestigial.

### 8. Backup/Legacy Files
**Files:** index.html.backup, index.html.before-reorganization, index.html.duplicates-removed, index.html.backup-reorganization, bigbounce-md.html, interactive-data-simple.html
**What it is:** Old versions and alternative views
**Disconnection:** Cluttering root directory. Should be git-tracked history, not live files.

---

## Recommended Architecture: Three-Pillar Unification

### Proposed Repository Structure

```
bigbounce/                          # This repo becomes a "Hub" (Pillar 3)
├── .hubify/
│   ├── hub.yaml                    # Hub manifest (name, description, pillars, public/private)
│   ├── squad.yaml                  # Squad definition (agents, roles, models, souls)
│   ├── missions/                   # Mission definitions (research tasks)
│   │   ├── paper-v1.yaml          # Completed: write paper v1
│   │   ├── mcmc-verification.yaml # Completed: verify MCMC results
│   │   └── galaxy-spin-deep.yaml  # Active: deep galaxy spin analysis
│   ├── skills/                     # Reusable skill definitions
│   │   ├── literature-search.yaml
│   │   ├── equation-verify.yaml
│   │   ├── mcmc-run.yaml
│   │   └── figure-generate.yaml
│   ├── knowledge/                  # Collective knowledge layer
│   │   ├── claims.yaml            # Structured claims table (derived/assumed/fit)
│   │   ├── findings.yaml          # Key research findings
│   │   └── open-questions.yaml    # Unresolved questions
│   └── context/                    # Shared agent context/memory
│       ├── paper-state.yaml       # Current paper state (version, status, issues)
│       └── data-catalog.yaml      # Dataset registry
│
├── agents/                         # Pillar 2: Agent infrastructure (platform-level)
│   ├── registry.yaml              # Agent registry (available agents + capabilities)
│   ├── router.py                  # Multi-model reasoning router
│   ├── skills/                    # Executable skill implementations
│   │   ├── literature.py
│   │   ├── computation.py
│   │   ├── data_access.py
│   │   ├── dataset_loaders.py
│   │   ├── galaxy_zoo.py
│   │   └── gpu_compute.py        # RunPod/Colab abstraction
│   ├── orchestrator.py            # Mission runner (sequences skills, manages state)
│   └── memory/                    # Agent memory/learning
│       ├── session_logs/          # Per-mission execution logs
│       └── learned_patterns.yaml  # What agents learned across missions
│
├── site/                           # Pillar 1 output: The public-facing hub
│   ├── index.html                 # Landing page
│   ├── paper.html                 # Full paper
│   ├── explained.html             # Explainer
│   ├── mathematics.html           # Derivations
│   ├── datasets.html              # Data explorer
│   ├── galaxy-zoo.html            # Galaxy spin explorer
│   ├── methodology.html           # Research process + agent profiles
│   ├── sources.html               # Bibliography
│   ├── animations.html            # Visualizations
│   ├── versions.html              # Version history
│   ├── style.css                  # Shared styles
│   └── api/                       # Public data API (serverless functions)
│       ├── claims.json            # Generated from .hubify/knowledge/claims.yaml
│       ├── datasets.json          # Generated from data catalog
│       └── findings.json          # Generated from knowledge layer
│
├── arxiv/                          # Canonical paper source (unchanged)
│   ├── main.tex
│   ├── references.bib
│   ├── figures/
│   └── reproducibility/           # Single location (remove duplicate)
│
├── data/                           # Research data (unchanged)
│   └── figures/
│
├── scripts/                        # Build & analysis scripts
│   ├── build_data.py
│   ├── build_site.py              # NEW: Generate site/ from knowledge layer
│   ├── eb_forecast.py
│   └── generate_figures.py
│
├── research/                       # Research outputs & notebooks
│   ├── outputs/
│   └── notebooks/
│
└── project-context/                # Historical docs (archive, not active)
    └── peer-reviews/
```

### Key Architectural Changes

#### 1. `.hubify/` becomes the operational hub manifest (not just a stub)
- `hub.yaml` defines this project as a Hubify Hub with metadata, visibility, tags
- `squad.yaml` replaces the 24-line markdown with structured YAML (agent IDs, model configs, soul prompts, capability declarations)
- `missions/` tracks research missions with state (pending/active/completed/failed)
- `skills/` declares what this hub's agents can do (reusable across hubs)
- `knowledge/` is the collective brain — structured claims, findings, open questions
- `context/` is shared agent memory that persists across sessions

#### 2. `agents/` becomes a proper agent platform layer
- `registry.yaml` — discoverable agent catalog with capabilities, models, costs
- `orchestrator.py` — mission runner that sequences skills, handles failures, tracks state
- `skills/` — current research/agents/*.py refactored as composable skills
- `memory/` — agents learn from past sessions and share knowledge

#### 3. `site/` cleanly separates the public-facing output
- All HTML moves from root into site/
- site/api/ exposes structured data from the knowledge layer
- Build script generates site content from knowledge layer (site stays in sync automatically)
- Remove password protection → this is a public knowledge hub

#### 4. Eliminate duplication and clutter
- Remove: index.html.backup*, bigbounce-md.html, interactive-data-simple.html
- Consolidate: reproducibility/ into arxiv/reproducibility/ (single source)
- Consolidate: config/ into .hubify/ (one config location)
- Pick one deployment: Vercel OR Netlify (not both)

---

## Priority Action Items

### P0 — Structural Foundation (Do First)

1. **Create `.hubify/hub.yaml`** — Define this repo as a Hubify Hub
   - name, description, version, visibility (public), tags
   - Link to the three pillars
   - Define the "project template" this represents (research-paper-hub)

2. **Upgrade `.hubify/squad.yaml`** from markdown to structured YAML
   - Each agent: id, name, role, model, soul_prompt, capabilities[], tools[]
   - Squad-level: mission_types[], default_workflow

3. **Move HTML to `site/`** — Clean separation of web output from platform code
   - Move all .html + style.css into site/
   - Update deployment configs to publish from site/
   - Delete backup files (they're in git history)

4. **Consolidate `research/agents/` → `agents/skills/`**
   - Rename for clarity: these are skills, not autonomous agents
   - Add `agents/registry.yaml` cataloging each skill

### P1 — Knowledge Layer (Connects Everything)

5. **Create `.hubify/knowledge/claims.yaml`**
   - Structured version of the claims table (currently scattered across peer review docs)
   - Each claim: id, statement, type (derived|assumed|fit), confidence, evidence[], status

6. **Create `.hubify/knowledge/findings.yaml`**
   - Key results: H₀=69.2±0.8, σ₈=0.785±0.016, etc.
   - Links to source (MCMC config, paper section, data)

7. **Create `.hubify/missions/` with completed + active missions**
   - Each mission: id, title, status, squad_config, skills_used[], outputs[], started, completed
   - Retroactively document the 6 revision rounds as completed missions

8. **Build `scripts/build_site.py`** — Generate site content from knowledge layer
   - Read claims.yaml → generate claims section in site
   - Read findings.yaml → populate key results
   - Read missions/ → generate methodology timeline
   - This is the connective tissue between Pillar 2 (agents) and Pillar 3 (public knowledge)

### P2 — Agent Orchestration (Pillar 2 Core)

9. **Create `agents/orchestrator.py`**
   - Mission runner: load mission YAML → sequence skills → track state → save outputs
   - Handles: parallel skill execution, failure recovery, progress reporting
   - Connects to: RunPod (GPU), local (CPU), Convex (cloud)

10. **Create `agents/memory/`**
    - Session logs from each mission run
    - Learned patterns (what worked, what failed, useful heuristics)
    - Shared context that persists across agent sessions

### P3 — Social/Public Layer (Pillar 3 Core)

11. **Remove password protection** — This should be a public knowledge hub

12. **Add `site/api/`** — Serverless data endpoints
    - /api/claims → structured claims data
    - /api/datasets → dataset catalog
    - /api/findings → key results
    - Enable other hubs/agents to query this hub's knowledge programmatically

13. **Add contribution/discussion mechanism**
    - Could start simple: link to GitHub Discussions
    - Or: Hubify-native commenting system (future)

---

## How the Three Pillars Connect

```
┌─────────────────────────────────────────────────────────┐
│                    PILLAR 1: OpenClaw                     │
│              (AI OS / Agent Operating System)             │
│                                                           │
│  .hubify/hub.yaml     ←── Hub manifest & identity        │
│  .hubify/squad.yaml   ←── Agent team configuration       │
│  .hubify/context/     ←── Shared memory & state          │
│  agents/registry.yaml ←── Available agents & skills      │
│                                                           │
│  "The operating system layer that defines WHAT this       │
│   hub is, WHO works on it, and WHAT they remember"       │
│                                                           │
│  Syncs to local OpenClaw via Hubify CLI (future)         │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│              PILLAR 2: Agent Squads & Missions            │
│           (Research Infrastructure & Execution)           │
│                                                           │
│  .hubify/missions/    ←── What needs to be done          │
│  .hubify/skills/      ←── Declared capabilities          │
│  agents/skills/*.py   ←── Executable skill code          │
│  agents/orchestrator  ←── Mission runner                 │
│  agents/router.py     ←── Multi-model reasoning          │
│  RunPod/HuggingFace   ←── Compute & data backends       │
│                                                           │
│  "The execution layer that DOES the work —               │
│   runs missions, calls APIs, processes data"             │
│                                                           │
│  Reads missions from Pillar 1, outputs to Pillar 3      │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│            PILLAR 3: Social Knowledge Network             │
│             (Public Hub / Shared Knowledge)               │
│                                                           │
│  .hubify/knowledge/   ←── Structured knowledge base      │
│  site/                ←── Public-facing website           │
│  site/api/            ←── Programmatic data access        │
│  versions/            ←── Evolution history               │
│  peer-reviews/        ←── Review & discussion trail       │
│                                                           │
│  "The sharing layer — what the world sees,               │
│   what other hubs can query, what humans review"         │
│                                                           │
│  Built by Pillar 2, configured by Pillar 1              │
└─────────────────────────────────────────────────────────┘
```

**The key insight:** Each pillar feeds the next.
- Pillar 1 (OpenClaw) **defines** the hub identity, team, and shared context
- Pillar 2 (Squads) **executes** missions using the defined skills and context
- Pillar 3 (Network) **publishes** the results as shared knowledge

Right now these three layers are **mixed together in a flat directory** with no clear boundaries. The restructuring above separates them cleanly while preserving all existing code.

---

## Quick Wins (Can Do Today)

1. Delete backup HTML files from root (4 files)
2. Consolidate reproducibility/ directories
3. Upgrade .hubify/squad-init.md → squad.yaml with full agent configs
4. Create .hubify/hub.yaml manifest
5. Create .hubify/knowledge/claims.yaml from existing peer review claims table
6. Pick Vercel OR Netlify and remove the other config
7. Move HTML into site/ subdirectory

---

## What This Repo Should Become

**Before (now):** A research paper with some agent scripts in it
**After:** A Hubify Hub — a living knowledge project powered by agent squads, with public research output, structured knowledge, and programmatic APIs. The first template for what every Hubify Hub looks like.

This repo should be the **reference implementation** of a Hubify Hub. Everything built here becomes the template for future hubs on the platform. The BigBounce research paper is the *content*; the Hubify Hub architecture is the *product*.
