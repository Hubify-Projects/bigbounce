# Hubify Lab Platform — Development Prompt

**Use this prompt to start a conversation (in the Hubify repo or a new project) focused on building the Hubify Lab research platform.**

---

## THE PROMPT

```
I'm Houston Golden, building Hubify Lab — a scalable AI-powered research platform that orchestrates multiple scientific research missions simultaneously. Think of it as "Claude Code for science at scale."

## What Already Works (proven in the BigBounce project)

I have a working prototype of this approach in my BigBounce cosmology research program (github.com/Hubify-Projects/bigbounce). Here's what we've built and proven:

- **4 papers** in 3 months from a solo researcher + AI agents
- **195,829 spectral anomalies** found in 17.65M DESI DR1 spectra (99.8% uncataloged)
- **8.47M galaxy chirality catalog** (40x larger than prior work)
- **424K MCMC posterior samples** across 4 dataset combinations
- **$400 total compute cost** for all of the above
- **Multi-model review loop**: Claude Code (executor) + ChatGPT (theorist) + Gemini (challenger)
- **Automated backup protocol**: every artifact in 3+ locations (local + B2 + HuggingFace + Convex)
- **Real-time web dashboards**: anomaly explorer, galaxy explorer, data explorer, status page, 40+ pages

The full technical stack is documented at: bigbounce.hubify.app/infrastructure.html
The research methodology is documented at: project-context/houstons-approach.md
The vision essay: bigbounce.hubify.app/articles/the-window.html
The speculative research paths: bigbounce.hubify.app/speculations.html
The Hubify Lab strategy: project-context/hubify_lab_vision.md

## What I Want to Build

A platform where I can:

### 1. Multi-Project Research Orchestration
- Each research project (DESI anomalies, chirality, SDSS scan, eROSITA scan, Planck CMB, etc.) has its own **agent-orchestrator**
- Each orchestrator manages sub-agents for: data acquisition, GPU inference, cross-matching, analysis, paper drafting
- Projects run independently but can cross-reference each other's results
- Central dashboard shows all projects' status, progress, costs, discoveries

### 2. Human-in-the-Loop Chat Interface
- **Global research chat**: discuss new ideas, review cross-project insights, strategic planning
- **Project-specific chats**: dive into one project's details, debug issues, review results
- Terminal-style clean UI (like Claude Code but in browser)
- Chat history preserved, searchable, taggable

### 3. Agent Personality System
- **Houston's Soul Agent** ("houston-relentless"): embodies the methodology from houstons-approach.md — pushes past conservative recommendations, demands more columns/rows/databases, refuses "publish the failure," insists on exploring all paths before stopping
- **Skeptical Reviewer Agent**: challenges claims, checks for overclaiming, verifies novelty against literature
- **Optimizer Agent**: looks for parallelization opportunities, speed improvements, cost reductions
- **Infrastructure Agent**: manages GPU pods, backups, deployments, monitoring
- These agents communicate with each other and the human to create a multi-perspective research environment

### 4. Feedback Loop Guards
- **Anti-premature-closure**: When any agent says "ready to publish" or "this is good enough," trigger a review asking "what else could we add?"
- **Anti-conservative-default**: When any agent suggests "this is too hard, do something easier," flag it for human review
- **Pro-optimization**: After any pipeline succeeds, automatically ask "how can this be faster/cheaper/more comprehensive?"
- **Multi-model validation**: Important results get cross-checked by at least 2 different AI models

### 5. Infrastructure I Already Have
- **Fly.io machines** with OpenClaw/Paperclip agent framework (already provisioned)
- **Convex** real-time database (already integrated)
- **RunPod** GPU pods (API access, SSH keys, automated provisioning)
- **Backblaze B2** cloud storage (already integrated)
- **HuggingFace** model/dataset hosting (already integrated)
- **GitHub** repos (Hubify-Projects org)
- **Netlify** auto-deploy for static sites
- **Claude Code** as the primary driver (this is what works best)

### 6. The Six Immediate Survey Targets
Once the platform is running, these are ready to launch:
1. SDSS DR18 — 5M spectra, same autoencoder methodology (~$50)
2. LAMOST DR10 — 20M spectra, largest pre-DESI survey (~$100)
3. eROSITA — 710K X-ray sources, first all-sky X-ray since 1990s (~$50)
4. Planck CMB — full-sky patch anomaly detection (~$50)
5. NEOWISE/unTimely — 170B rows, time-domain variability (~$300)
6. Gaia epoch photometry — 1.8B stars × 70 epochs (~$500)

## Key Technical Question

How should I architect this? Options I'm considering:
- **Claude Code terminals on Fly.io machines** — essentially replicate what works (me + Claude Code), but with multiple instances running different projects
- **OpenClaw/Paperclip framework** — already installed on my Fly.io machines, could be customized for research orchestration
- **Custom agent system** — build something purpose-built using Claude API / AI SDK
- **Hybrid** — Claude Code as the brain, Fly.io machines as the hands, Convex as the memory, custom UI as the interface

I want to start simple and scale. What's the fastest path to having 2-3 research projects running simultaneously with a clean human-in-the-loop interface?
```

---

## Context Files to Reference

When starting this conversation, have these files accessible:

### In the BigBounce repo (github.com/Hubify-Projects/bigbounce):
- `project-context/houstons-approach.md` — Research methodology & decision heuristics
- `project-context/hubify_lab_vision.md` — Full strategic vision & scaling plan
- `project-context/h200_research_opportunities.md` — 29 ranked GPU runs
- `project-context/additional_datasets_and_pipelines.md` — 12 survey datasets ranked
- `project-context/pipeline1_tracer_purification_plan.md` — Example of a complete execution plan
- `CLAUDE.md` — The working Claude Code instructions that drive the research
- `infrastructure.html` — Complete technical stack documentation

### On the BigBounce website:
- https://bigbounce.hubify.app/articles/the-window.html — "The Window" essay
- https://bigbounce.hubify.app/speculations.html — 25+ research paths
- https://bigbounce.hubify.app/status.html — Live research status
- https://bigbounce.hubify.app/infrastructure.html — Technical infrastructure

### In the Hubify repo:
- Whatever agent framework code is already in place
- Fly.io machine configs
- Existing OpenClaw/Paperclip setup
