# Hubify → Agentic Research OS: What Stays, What Goes, What Changes

**Created:** 2026-03-28
**Context:** After deep exploration of both the Hubify codebase (96 tables, 128 Convex files, 60+ CLI commands, 40+ pages) and the BigBounce research program (4 papers, $400 compute, 195K anomalies).

---

## The Verdict on OpenClaw

**Use it, but as the workspace runtime layer — not the orchestration brain.**

### Why Keep OpenClaw:
- It's already deployed on Fly.io machines with Docker, persistent volumes, boot system
- Agent soul MDs, org charts, cron configs are exactly what research projects need
- The workspace isolation model (each project = its own machine) maps perfectly to research missions
- SmartSync for template updates works

### Why NOT Make It the Orchestration Layer:
- OpenClaw is designed for a SINGLE workspace with agents collaborating inside it
- The research OS needs a META-layer that sees ACROSS workspaces/projects
- Claude Code (the thing that's actually working) should be the brain, not OpenClaw
- OpenClaw's model routing is generic; we need the specific multi-model review loop (Claude executor + ChatGPT theorist + Gemini challenger)

### The Architecture:
```
┌─────────────────────────────────────────────────────────┐
│  HUBIFY LAB (Next.js terminal UI + Convex orchestrator) │
│  ─ Global research chat                                 │
│  ─ Project dashboard                                    │
│  ─ Agent feed panel                                     │
│  ─ Multi-model review loop                              │
│  ─ Feedback loop guards                                 │
│  ─ Budget/pod monitoring                                │
├─────────────────────────────────────────────────────────┤
│                    ORCHESTRATION                         │
│  Convex: project state, cross-project queries,          │
│  agent commentary, discovery log, paper tracking        │
├──────────┬──────────┬──────────┬────────────────────────┤
│ Project1 │ Project2 │ Project3 │ ...                    │
│ bigbnce  │ sdss     │ erosita  │                        │
│          │          │          │                        │
│ Fly.io   │ Fly.io   │ Fly.io   │ Per-project machines  │
│ machine  │ machine  │ machine  │ with OpenClaw runtime  │
│          │          │          │                        │
│ Convex   │ Convex   │ Convex   │ Per-project databases  │
│ app      │ app      │ app      │                        │
│          │          │          │                        │
│ GitHub   │ GitHub   │ GitHub   │ Per-project repos      │
│ repo     │ repo     │ repo     │                        │
│          │          │          │                        │
│ RunPod   │ RunPod   │ RunPod   │ Per-project GPU pods   │
│ (if GPU) │ (if GPU) │ (if GPU) │ (provisioned on demand)│
└──────────┴──────────┴──────────┴────────────────────────┘
```

---

## What DEFINITELY STAYS (Core of Research OS)

### From Hubify:
| Feature | Why | Location |
|---------|-----|----------|
| **Convex backend** (96 tables) | Rock-solid, real-time, perfect for agent state | `/convex/` |
| **Fly.io workspace provisioning** | Per-project isolated machines | `/infra/workspace/` |
| **Agent autonomy cycles** | Cron-driven agent behaviors = research automation | `/convex/agentAutonomy.ts` |
| **Skills registry + learning** | Track what works, evolve approaches | `/convex/skills.ts`, `learning.ts` |
| **Collective intelligence / hubs** | Cross-project knowledge sharing | `/convex/hubs.ts`, `hubKnowledge.ts` |
| **Squad deployment** | Multi-agent teams per project | `/convex/squads.ts` |
| **Crons (30+ jobs)** | Research automation backbone | `/convex/crons.ts` |
| **CLI (60+ commands)** | Power-user interface for all operations | `/packages/cli/` |
| **Auth (Clerk + JWT)** | Workspace security | `/convex/auth.ts` |
| **MCP server** | Claude Code integration | `/packages/mcp/` |
| **Agent Ed25519 identity** | Agent accountability, reputation | `/convex/auth.ts` |

### From BigBounce (to be extracted as patterns):
| Pattern | What It Is | Source |
|---------|-----------|--------|
| **Pipeline template** | Download → GPU inference → catalog → cross-match → explorer | `enhanced_18M_inference.py` |
| **Checkpoint/resume** | JSON checkpoint after each unit of work | All pipelines |
| **Auto-sync** | Background script to prevent disk overflow | `auto_sync_18M.sh` |
| **Multi-backup protocol** | Local + B2 + HuggingFace + Convex + GitHub | All outputs |
| **Cross-reference engine** | SIMBAD/NED/AllWISE/Milliquas/Gaia/SDSS queries | `step2_cross_match.py` |
| **Web explorer pattern** | Interactive anomaly/galaxy/data explorer with Convex | `anomaly-explorer.html` |
| **CLAUDE.md approach** | Project-specific agent instructions | `CLAUDE.md` |
| **houstons-approach.md** | Methodology principles for agent personalities | `project-context/` |

---

## What MAYBE STAYS (Keep But Deprioritize)

| Feature | Keep If... | Remove If... |
|---------|-----------|-------------|
| **Template system** | Useful as "research OS presets" (auto-gen CLAUDE.md, pipeline scaffolds) | Too complex to maintain |
| **Research missions UI** | Good for tracking multi-step research projects | Duplicates project dashboard |
| **Local-cloud sync** | Researchers want local dev + cloud execution | 30s polling is too slow |
| **Experiment DAG** | Could model research branch exploration | Too abstract without UI |
| **Semantic vector search** | Would enable "find similar anomalies across projects" | Requires OpenAI API + backfill |
| **Tool vault** | Secure credential sharing across agents | Env vars work fine for now |
| **Company OS** | If it feeds learnings back to core | If it's just sitting there |

---

## What DEFINITELY GOES (Remove or Disable)

| Feature | Why Remove |
|---------|-----------|
| **Claws framework / Studio** | Cool demo, no persistence, architecturally misaligned. Save to archive branch. |
| **Community skill marketplace** | Research OS is internal-first, not community-first. Hide the UI. |
| **Agent persona ratings/reviews** | Socializes agents in ways irrelevant to research. |
| **Public template marketplace** | Encourages fragmentation. Research needs ONE good template. |
| **Billing UI** | Premature. Set everything to free tier. Keep code, hide UI. |
| **Cisco/OWASP/Snyk stubs** | Placeholder code. Delete. Implement properly if/when needed. |
| **AI-BOM / Governance stubs** | Same. Delete. |
| **Weekly digest stubs** | Not implemented. Delete. |

**How to preserve:** Create a `git branch archive/pre-research-pivot` before removing anything. That way nothing is truly lost.

---

## The Missing Links (What Needs to Be Built)

### 1. Per-Project Convex App Provisioning
Hubify's GitHub app and Vercel integrations already create repos and deployments per-project. **Missing:** automatically creating a new Convex app per research project.

**Implementation:** Add a Convex action that calls the Convex API to create a new project, then stores the deployment URL in the parent Hubify Convex instance.

### 2. Terminal UI
The existing Next.js dashboard is widget-heavy. The research OS needs a **terminal-first interface** (see `hubify-lab-ux-vision.md`).

**Implementation:** New page `/app/terminal/` with:
- xterm.js or similar terminal emulator
- WebSocket connection to Claude Code process (or API)
- Split pane layout (global chat + project view + agent feed)
- Dark terminal aesthetic (the rebrand Houston just did is aligned)

### 3. Multi-Model Review Loop
**Missing:** Automated pipeline that takes Claude Code output → sends to ChatGPT/Gemini/DeepSeek → synthesizes → presents to human.

**Implementation:** Convex action that:
1. Receives a research report/finding
2. Calls OpenAI API (o3), Google Gemini API, DeepSeek API
3. Stores all responses in Convex
4. Synthesizes agreement/disagreement
5. Surfaces in agent feed panel

### 4. Feedback Loop Guards
**Missing:** The anti-premature-closure, anti-conservative-default, pro-optimization guards.

**Implementation:** Convex functions that scan agent output for trigger phrases ("ready to publish," "good enough," "too complex") and inject counter-prompts from the houston-relentless personality.

### 5. RunPod Budget Guardian
**Missing:** Real-time cost tracking and alerts.

**Implementation:** Cron that hits RunPod API every 15 minutes, aggregates spend per project, alerts if thresholds exceeded. NEVER auto-terminates pods.

### 6. Cross-Project Discovery Correlation
**Missing:** When Project A finds an anomalous object, automatically check if Project B has data on the same object.

**Implementation:** Convex query that takes (RA, DEC) coordinates and searches all project catalogs within a configurable radius. Surface matches in the agent feed.

---

## Implementation Order

### Week 1: Foundation
1. Archive branch for pre-pivot code
2. Strip/hide removed features
3. Terminal UI skeleton (xterm.js + split panes)
4. Per-project Convex provisioning
5. Fork bigbounce as test project

### Week 2: Agent System
6. Agent personality prompts (houston-relentless, skeptic, optimizer, infra)
7. Agent feed panel in terminal UI
8. Feedback loop guards
9. Multi-model review loop (ChatGPT + Gemini APIs)

### Week 3: Pipeline Orchestration
10. RunPod provisioning from terminal
11. Budget guardian cron
12. Auto-checkpoint monitoring
13. Cross-project discovery correlation

### Week 4: Polish + First Real Project
14. Launch SDSS DR18 scan as first non-bigbounce project
15. Verify full lifecycle works
16. Fix whatever breaks
17. Document the system

---

## Key Decision: Claude Code as Brain

The most important architectural decision: **Claude Code (via API or local process) is the execution brain.** Not OpenClaw. Not a custom agent framework. Not a DAG runner.

Why:
1. It's what's actually working right now (4 papers, 195K anomalies, 8.47M galaxies)
2. It has filesystem access, SSH, Git, and tool orchestration built in
3. The sub-agent system handles parallel research tasks
4. The CLAUDE.md pattern provides project-specific instructions

OpenClaw provides the runtime environment (Fly.io machines with agent configs). Convex provides the state layer (cross-project queries, agent commentary, discovery log). The terminal UI provides the human interface. But Claude Code is the brain that drives everything.

The other models (ChatGPT, Gemini, DeepSeek) are reviewers and challengers — they don't execute, they provide perspectives that feed back into Claude Code's next decision.
