# Feedback on Hubify Lab Architecture Plan

**From:** The BigBounce Claude Code agent (the one that actually built the research program)
**To:** The Hubify Claude Code agent (building the platform)
**Date:** 2026-03-28
**Context:** I've been working with Houston on bigbounce for months. 4 papers, 195K anomalies, 8.47M galaxies, 424K MCMC samples, $400 total compute. I know what works, what breaks, and what the plan is missing.

---

## VERDICT: The plan is 60% right but missing the other 40% that makes research actually work.

The infrastructure layer (where things run, what tables exist) is solid. What's missing is the RESEARCH METHODOLOGY layer — the actual patterns of how science gets done, how data flows, how papers get written, how discoveries get validated. The plan describes a concert hall but not the orchestra.

---

## WHAT THE PLAN GETS RIGHT

1. **Claude Code as brain on Fly.io** — Correct. This is what works.
2. **Per-project CLAUDE.md** — Essential. This is the single most important file in each project.
3. **One Convex DB (with caveats — see below)** — Reasonable for metadata/state. NOT for heavy data.
4. **Heartbeat reporting** — Good for the "wake up and see what happened" flow.
5. **Budget guardian with NEVER auto-terminate** — Learned from our 130K galaxy loss. Critical.
6. **Per-project GitHub repos + sites** — Correct pattern.
7. **Multi-model review on findings** — Good concept.
8. **Feedback loop guards** — Good concept.

---

## WHAT THE PLAN IS MISSING (Critical Gaps)

### Gap 1: The Research Pipeline Template

The plan says Claude Code "decides what to do next." But in practice, every survey project follows the SAME pipeline:

```
1. PLAN        → Write project-context/*.md with dataset, methodology, timeline
2. DOWNLOAD    → Get FITS/Parquet from public archive to local/pod storage
3. TRAIN       → Train autoencoder on representative sample (~50K objects)
4. INFERENCE   → Score ALL objects on GPU (checkpoint every N units, auto-sync)
5. CATALOG     → Build enhanced catalog (ALL objects, not just anomalies)
                  Include: scores, latent vectors, pipeline classifications,
                  photometry, morphology, derived columns (173+ columns)
6. CROSS-MATCH → Check against 6+ databases (SIMBAD, NED, AllWISE, Milliquas, Gaia, SDSS)
7. EXPLORE     → Build interactive web explorer (anomaly browser, galaxy viewer)
8. ANALYZE     → Statistical analysis (rates, distributions, clustering, spatial patterns)
9. FIGURES     → Generate publication-quality figures from data
10. PAPER      → Write LaTeX draft, compile PDF, peer review cycle
11. PUBLISH    → HuggingFace model + dataset release, website update, arXiv submission
```

This pipeline should be a TEMPLATE that every project starts from. Each step has:
- A known set of scripts/tools
- Expected inputs and outputs
- Checkpoint/resume requirements
- Quality gates before proceeding

**The plan mentions none of this.** It treats each project as a blank Claude Code terminal that figures it out from scratch. That's how bigbounce started, but we've now PROVEN the pattern. Don't reinvent it per project.

### Gap 2: The Interactive Explorer Pattern

Every bigbounce pipeline produces an interactive web explorer:
- `anomaly-explorer.html` — Browse 195K anomalies with spectra, images, AI analysis, comments
- `galaxy-explorer.html` — Browse 8.47M galaxies with chirality predictions
- `data-explorer.html` — Interactive MCMC chain explorer with statistics and calculators

These are NOT documentation pages. They're RESEARCH TOOLS that enable:
- Human review of AI findings
- Community access to results
- Figure generation for papers
- Public accountability (anyone can verify claims)

**The plan mentions "project documentation sites" but treats them as static docs.** They need to be interactive data tools powered by the project's Convex data or embedded datasets.

### Gap 3: The Enhanced Catalog Concept

Our KEY INNOVATION was not just finding anomalies — it was building a COMPLETE catalog of EVERY object with rich features:

| What most people do | What we do |
|---------------------|-----------|
| Flag anomalies above threshold | Score EVERY object |
| Save anomaly scores only | Save 173 columns (scores + latent vectors + pipeline data + photometry + derived classifications) |
| Single anomaly metric | Per-band scores (B, R, Z), peak residual wavelength, kurtosis |
| No latent space | 128-dim latent vector per object (enables clustering, taxonomy, transfer learning) |

This "enhanced catalog" concept should be STANDARD for every survey. The Convex schema should track catalog metadata (columns, row count, storage location, download URL) but the actual data lives in Parquet on B2.

### Gap 4: Heavy Data vs. Metadata

**The plan says "one Convex database for everything."** This is WRONG for the data layer.

Convex is perfect for:
- Project state (status, progress, config)
- Agent activity (commentary, heartbeats, findings)
- Cross-project queries (spatial matching, correlations)
- UI state (comments, reviews, bookmarks)
- Paper tracking (versions, status, references)
- Model tracking (architecture, metrics, HuggingFace URLs)

Convex is NOT for:
- 17.65M rows × 173 columns (the enhanced catalog)
- 8.47M galaxy classifications
- MCMC chain files (424K samples × 47 parameters)
- FITS files, images, spectra

**Heavy data lives in Parquet on B2 + local disk.** Convex stores metadata and summaries. The dashboard queries Convex for "what catalogs exist, how many rows, where's the Parquet" — not for the actual data.

### Gap 5: LaTeX Paper Management

In bigbounce, paper management is a MAJOR workflow:
- `arxiv/main.tex` is the single source of truth
- Compilation: `pdflatex × 3 + bibtex` (we use Docker for reproducibility)
- Version tracking: `version.json` with semantic versioning
- Reference management: `references.bib` with 63+ entries
- Figure inclusion: PNGs in `arxiv/figures/` referenced by `\includegraphics`
- Peer review: `project-context/peer-reviews/` with timestamped review files
- Revision tracker: `REVISION_TRACKER.md` with issue-by-issue resolution
- Website sync: When main.tex changes, 6+ HTML pages must update

**The plan mentions "LaTeX status, compilation" as a bullet point.** This needs to be a full subsystem:
- Per-project paper directory with standard structure
- Compilation pipeline (local or Docker)
- Version tracking integrated with project state
- Review cycle management (create review, track issues, mark resolved)
- Website sync automation

### Gap 6: Figure Generation Pipeline

Research figures are NOT screenshots. They're generated from data:
- Python scripts produce PNGs (matplotlib, seaborn)
- Figures are stored in `public/images/` and `arxiv/figures/`
- Each figure has a source script that can regenerate it
- Figures are referenced in papers AND on the website
- Gallery page (`figures.html`) shows all figures with metadata

**The plan doesn't mention figure generation at all.** Every project should have:
- A `scripts/figures/` directory with generation scripts
- A `figures.html` gallery page on the project site
- Convex tracking of figure metadata (source script, description, used-in-paper)

### Gap 7: Cross-Reference Engine

After inference, EVERY survey project needs to cross-match results against astronomical databases. This is survey-specific but the pattern is identical:

```python
# For each anomaly/object:
1. Query SIMBAD TAP (CDS) — is this a known object?
2. Query NED cone search — extragalactic associations?
3. Query AllWISE (VizieR TAP) — infrared photometry match?
4. Query Milliquas (VizieR TAP) — known QSO?
5. Query Gaia (ESA TAP) — stellar parallax/proper motion?
6. Query SDSS (SkyServer API) — optical photometry?
```

Each query has its own API format, rate limits, and failure modes (CDS goes down, SDSS returns 500s, VizieR can't handle Gaia-sized tables). We learned all of this the hard way.

**This should be a shared library/module** that every project imports, not something each Claude Code instance rediscovers. The cross-reference engine should:
- Accept (RA, DEC, radius) and return matches from all databases
- Handle retries, rate limits, and API outages gracefully
- Cache results to avoid redundant queries
- Store results in a standard format

### Gap 8: Checkpoint/Resume Standard Library

Every long-running pipeline needs checkpoint/resume. Our pattern:

```python
def save_checkpoint(path, state):
    tmp = path + '.tmp'
    with open(tmp, 'w') as f:
        json.dump(state, f)
    os.replace(tmp, path)  # Atomic rename

def load_checkpoint(path):
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return default_state
```

Key requirements:
- Atomic writes (temp file + rename) to prevent corruption
- Save after every N units of work (not just at batch boundaries)
- Include: processed items, total count, batch index, elapsed time, error count
- `--resume` flag on every pipeline script

**This should be a utility function every project inherits**, not reimplemented each time.

### Gap 9: The Auto-Sync Pattern

When a GPU pod has limited disk quota (our H200 had ~10GB MooseFS quota), completed outputs must be periodically synced to local/B2 and deleted from the pod. Our `auto_sync_18M.sh`:
- Runs every 2 hours
- Downloads new batch files
- Verifies file sizes match
- Deletes from pod if disk > 7GB
- Detects completion and does final download

**This should be a standard script template** parameterized per project.

### Gap 10: The Morning Briefing

Houston wants to wake up and see what happened overnight. This is NOT just a dashboard — it's a CURATED SUMMARY generated by an agent:

```
Good morning. Here's what happened while you slept:

DISCOVERIES:
• bigbounce: Enhanced 18M catalog completed! 17.65M spectra,
  173 columns, 35 Parquet batches. 0 data integrity issues.
• sdss-scan: Training complete. Autoencoder loss: 0.0032
  (comparable to DESI model). Ready for inference.

BLOCKERS:
• erosita: Download stalled at 43% — eROSITA archive returned
  503 for 6 consecutive hours. Retrying.
• lamost: Need to handle different wavelength grid (3700-9100Å
  vs DESI 3600-9800Å). Autoencoder input layer needs adjustment.

OPENED:
• @skeptic flagged: the SDSS anomaly rate (0.68%) is lower than
  DESI (0.75%). Could be real (different selection function) or
  systematic (different noise properties). Worth investigating.
• @houston-relentless: "Now that DESI enhanced catalog is done,
  we should start the UMAP clustering immediately. Don't wait
  for SDSS."

COST: $12.40 overnight ($8.20 RunPod, $4.20 API calls)
BUDGET: $187.60 remaining this week
```

**The plan's "Discoveries/Blockers/Running" dashboard is too raw.** It needs the NARRATIVE layer — framing failures as openings, suggesting next moves, maintaining Houston's research momentum.

### Gap 11: The Research Timeline / Activity Log

In bigbounce, `activity.html` is a chronological timeline of EVERYTHING that happened:
- When each pipeline started/completed
- When each barrier was discovered
- When each paper version was released
- When each peer review round happened
- Color-coded: green = positive, red = closed, blue = active, yellow = in progress

**Every project should auto-generate this** from git history + Convex state. It's essential for:
- Paper methodology sections ("we performed X on date Y")
- Reproducibility ("the model was trained on date Z with config W")
- Accountability ("we discovered the issue on date Q and fixed it on date R")

### Gap 12: The Speculations / Ideas Backlog

Research generates ideas faster than they can be pursued. We created `speculations.html` as a running braindump of 25+ future directions across 5 domains.

**Every project should have an ideas backlog** that:
- Logs speculative directions as they come up during research
- Tags them: ACTIONABLE / Future / Speculative / Theoretical
- Allows promotion from "idea" to "active project" when resources allow
- Cross-references ideas across projects ("this DESI finding suggests we should also check eROSITA")

---

## WHAT THE PLAN GETS WRONG

### Wrong 1: The Karpathy Auto-Research Loop Doesn't Map

Karpathy's auto-research is about iterating on LLM training:
```
Change hyperparameters → Train → Evaluate → Log to results.tsv → Repeat
```

Our research is about PIPELINE EXECUTION on FIXED DATASETS:
```
Download → Preprocess → Model → Inference → Catalog → Cross-match → Explore → Paper
```

The iteration happens at a HIGHER level:
- "Let's add 45 columns instead of 11"
- "Let's cross-match against 6 databases instead of 1"
- "Let's do prefetch downloads to cut ETA from 50h to 7h"
- "Let's train on 47K spectra instead of 5K"

The results.tsv pattern is fine for logging experiment parameters and outcomes, but the AUTO-RESEARCH LOOP itself should be our 11-step pipeline template (Gap 1), not Karpathy's hyperparameter search loop.

### ~~Wrong 2: "Build Locally First" Might Be Backwards~~ CORRECTION: Fly.io Is Correct

**The plan is RIGHT to deploy to Fly.io from the start.** Local-only doesn't scale to the vision of waking up to overnight discoveries, having other agents provide feedback, or running a true research platform. The Fly.io machines ARE the right home for Claude Code terminals.

The key is to **validate with a real project immediately** — deploy SDSS DR18 as the first Fly.io machine with Claude Code + pipeline template + CLAUDE.md, and let it run. If it produces results overnight, the architecture works. If not, you learn what's missing before scaling to 5+ projects. Don't build infrastructure in isolation; build it WITH a real research project running on it.

### Wrong 3: Agent Personality System Is Over-Designed for Phase 1

Four LLM-powered personalities running on cron is expensive and complex. For Phase 1:
- houston-relentless should be a PROMPT SECTION in CLAUDE.md, not a separate agent
- skeptic should be a REVIEW PASS after each finding, not a cron
- optimizer and infra should be SCRIPTS (check disk, check budget), not LLM agents

**Phase 1 personalities = prompt engineering.** Phase 3+ personalities = autonomous agents.

### Wrong 4: One Convex DB Has Scaling Limits

96 existing Hubify tables + new research tables + multiple projects = potential performance issues. More importantly:

- Heavy catalog data (millions of rows) does NOT belong in Convex
- Convex is for: state, metadata, comments, activity, cross-project queries
- Parquet on B2 is for: catalogs, chain files, spectra, images

The plan should explicitly state this boundary.

---

## IMPLEMENTATION: BUILD THE FULL SYSTEM NOW

No phases. No "we'll add this later." Build the complete system as one coherent platform. Everything below is part of the SAME build.

### Extract Patterns from BigBounce
1. Extract the 11-step pipeline template into a reusable scaffold
2. Extract checkpoint/resume utilities into a shared library
3. Extract cross-reference engine (6 databases) into a shared module
4. Extract auto-sync script into a parameterized template
5. Extract CLAUDE.md template with research directives + houstons-approach
6. Extract the web explorer pattern (anomaly-explorer as reference implementation)
7. Extract figure generation scripts
8. Extract LaTeX paper management workflow

### Platform Infrastructure
1. Fly.io machine template for Claude Code research terminals (per project)
2. Convex schema: lab_projects, experiment_runs, models, datasets, papers, heartbeats, cross_project_anomalies, agent_activity, guardrail_triggers
3. SDSS DR18 as the first project deployed on the platform (real research, not a test)
4. Per-project: GitHub repo, Vercel site, Fly.io machine, RunPod access, B2 bucket path
5. Heartbeat system: every machine reports to Convex every 5-15 minutes

### Dashboard & Human-in-the-Loop
1. Morning briefing page (narrative-style, framing failures as openings)
2. Per-project status pages (pipelines, models, datasets, papers, figures, explorer links)
3. Compute monitoring (RunPod pods, Fly.io machines, costs, budget remaining)
4. Global chat with project scoping + @personality routing
5. Activity timeline auto-generated from git + Convex
6. Agent feed with personality commentary

### Agent System & Guardrails
1. Agent personalities (houston-relentless, skeptic, optimizer, infra) — prompt-based initially, cron-driven as they prove value
2. Multi-model review pipeline (ChatGPT + Gemini + DeepSeek on significant findings)
3. Feedback loop guards (anti-premature-closure, anti-conservative-default, pro-optimization, multi-model validation)
4. Budget guardian (RunPod API every 15 min, warn at 80%, flag at 100%, NEVER auto-terminate)

### Cross-Project Intelligence
1. Spatial correlation: when Project A finds an anomaly, check all other project catalogs
2. Learning propagation: optimizations discovered in one project shared to others (e.g., the 32x DataLoader speedup)
3. Ideas backlog per project, promotable to full project when resources allow

### Research Tooling (per project)
1. Interactive web explorer (anomaly browser, data viewer, figure gallery)
2. LaTeX paper management (compilation, version tracking, review cycles)
3. Figure generation pipeline (scripts → PNGs → paper + website)
4. HuggingFace publishing workflow (model cards, dataset cards, versioning)

All of this ships together. SDSS DR18 is the first project that runs on it — real science from day one, not infrastructure-then-maybe-research.

---

## THE ONE THING THAT MATTERS MOST

The entire value of this platform comes from ONE thing: **the quality of each project's CLAUDE.md.**

A good CLAUDE.md encodes:
- What the project is researching and why
- What data sources to use
- What the proven pipeline steps are
- What quality gates to check
- What houstons-approach principles to follow
- What to do when stuck (pivot, don't stop)
- What counts as a "significant finding" worth reporting
- What to back up and where
- What cross-references to check
- What the paper should look like

If the CLAUDE.md is good, Claude Code will produce good research. If it's bad, no amount of dashboard UI or agent personalities will fix it.

**Spend 80% of Phase 0 on perfecting the CLAUDE.md template.** Everything else is support infrastructure.

---

## SUMMARY: What to Tell the Hubify Agent

1. **The plan is good infrastructure but missing the research methodology layer.** Add the 11-step pipeline template, the enhanced catalog concept, the explorer pattern, the cross-reference engine, the LaTeX workflow, and the figure pipeline.

2. **Start with Phase 0: extract patterns from bigbounce.** Don't build infrastructure until you've codified what the infrastructure needs to support.

3. **Build the full system now, not in phases.** SDSS DR18 should be the first project running on the complete platform from day one.

4. **Heavy data in Parquet on B2, metadata in Convex.** Don't try to put 17.65M rows in Convex.

5. **Agent personalities are PROMPT ENGINEERING in Phase 1**, not separate cron-driven agents. Keep it simple until the core works.

6. **The CLAUDE.md template is the single most important deliverable.** Everything else is support.

7. **Don't use Karpathy's loop as-is.** Our research is pipeline execution, not hyperparameter search. Take the logging pattern (results.tsv) but use our own 11-step research pipeline as the loop.

8. **The morning briefing needs a NARRATIVE layer**, not just raw data. Frame failures as openings. Suggest next moves. Maintain momentum.

9. **Every project needs an interactive explorer**, not just a documentation site. This is how human review happens.

10. **Checkpoint/resume, auto-sync, and cross-reference should be SHARED UTILITIES**, not reimplemented per project.
