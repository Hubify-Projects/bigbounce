# Hubify Labs Platform Plan — Autonomous Multi-Agent Research System

**Created:** 2026-04-07
**Author:** Houston Golden + Claude Code (office hours session)
**Status:** PLANNING — Design doc in progress

---

## Houston's Vision (verbatim context)

> "I really want to build it into a proper scalable autonomous ai agent team (many agents) working together and pushing each other. I think we could potentially build a local CLI/TUI tool or desktop app as well as a web app to manage, monitor, track, guide as human director, and scale this up more with multiple claude code orchestrator agents running a team of sub-agents via our own custom Pi agent harness that is fully robust and powerful where teams of agents (orchestrator > leads > workers) with different self-updating self-improving memories etc all work together on focused projects."
>
> "I want to build a platform that is scalable and agentic and mostly autonomous with minimal direction and feedback from me the human director. My platform Hubify can be a pioneer in agentic research across multiple domains — using this bigbounce project as the official first case study of the new hubify agentic research platform."
>
> "I think we want to use Pi (pi.dev) to build our own fully custom multi-agent harness — the system that builds the system. Claude Code is the main orchestrator within our system and the tool I will use to build the system primarily."
>
> "I should be able to chat with my global orchestrator (has access to create new Labs/Teams > Projects) and then each Lab/Team has a claude code orchestrator at the top then Leads then workers. Human in the loop can chat within Global view or Labs/Teams view or Projects views chatting with the orchestrator."

## AI-Structured Summary

### The Product
**Hubify Labs** is an autonomous multi-agent research platform where hierarchical teams of AI agents (Global Orchestrator > Lab/Team Orchestrators > Leads > Workers) conduct scientific research, write papers, manage GPU compute, and produce discoveries with minimal human direction. The human serves as **director**, not operator.

### The Architecture
```
Human Director (Houston)
  |
  v
Global Orchestrator (Claude Code via Pi harness)
  |--- can create new Labs/Teams/Projects
  |--- monitors all running research
  |--- allocates resources across labs
  |
  +-- Lab: BigBounce (Astrophysics)
  |     |
  |     +-- Orchestrator (Claude Code)
  |     |     |-- Research Lead (Opus) -- delegates to:
  |     |     |     |-- Literature Agent (Sonnet/Haiku)
  |     |     |     |-- Computation Agent (Sonnet)
  |     |     |     +-- Data Pipeline Agent (Sonnet)
  |     |     |-- Analysis Lead (Opus) -- delegates to:
  |     |     |     |-- Statistics Agent (Sonnet)
  |     |     |     |-- Cross-Match Agent (Sonnet)
  |     |     |     +-- QC Agent (Haiku)
  |     |     |-- Writing Lead (Opus) -- delegates to:
  |     |     |     |-- Paper Writer (Sonnet)
  |     |     |     |-- Figure Generator (Sonnet)
  |     |     |     +-- Peer Reviewer (Sonnet)
  |     |     +-- Infrastructure Lead (Opus) -- delegates to:
  |     |           |-- GPU Manager (Haiku)
  |     |           |-- Backup Agent (Haiku)
  |     |           +-- Site Updater (Sonnet)
  |     |
  |     +-- [BigBounce project files, H200 pod, website]
  |
  +-- Lab: Genomics (future)
  +-- Lab: Materials Science (future)
  +-- Lab: AI Research (future, self-improving)
```

### The Differentiation
- **Karpathy's autoresearch** optimizes ML models. Hubify Labs discovers real science.
- **Feynman CLI** synthesizes literature. Hubify Labs runs GPU pipelines and writes papers.
- **AutoAgent** self-improves agent harnesses. Hubify Labs self-improves AND produces external research output.
- **Nobody** is doing autonomous multi-agent research in astronomy/astrophysics/cosmology at this scale.

### The Proof
BigBounce: 4 papers, 50+ experiments, 328K anomalies, $400 compute, 3 months, 1 person + AI. Tonight's session alone ran 50 experiments autonomously with zero human intervention.

---

## Foundation Codebases (Purchased from indydevdan)

### 1. CEO-Agents
**Location:** `/Users/houstongolden/Desktop/CODE_2025/ceo-agents/`
**What it is:** Multi-agent deliberation system — 9 specialized AI agents (CEO + 8 board members) debate high-stakes decisions.

**Key patterns to extract:**
- Persistent Pi subprocess sessions per agent (`.jsonl` session files)
- Parallel board member calls (`Promise.allSettled`)
- Tension pairs (Revenue vs Compounder, Technical vs Moonshot)
- Constraint-driven meetings (min/max time + budget)
- Expertise scratch pads (compounding knowledge)
- Structured memo output (ranked recommendations, dissent, next actions)
- Real-time TUI streaming of agent responses

**Architecture:** CEO (Opus) orchestrates 8 board members (Sonnet) via `converse()` tool. Each member runs as persistent Pi subprocess with full context window. Contrarian speaks last (enforced).

**File inventory:**
- `apps/ceo/extensions/ceo-and-board.ts` (1,307 lines) — main orchestrator
- `apps/ceo/extensions/modules/` — types, config, subprocess, helpers, theme
- `.pi/ceo-agents/agents/` — 9 agent prompts (ceo.md, revenue.md, contrarian.md, etc.)
- `.pi/ceo-agents/expertise/` — 8 updatable scratch pads
- `.pi/ceo-agents/ceo-and-board-configuration.yaml` — board roster + constraints

**Reusable for Hubify Labs:**
- Deliberation pattern for research strategy decisions
- Tension pair concept for skeptic vs optimist agents
- Expertise accumulation across sessions
- Constraint engine (budget/time limits)

---

### 2. Lead-Agents
**Location:** `/Users/houstongolden/Desktop/CODE_2025/lead-agents/`
**What it is:** Depth-2 delegation hierarchy — Orchestrator > Team Leads > Workers — for software engineering tasks.

**Key patterns to extract:**
- Config-driven team structure (YAML defines entire org)
- Domain locking (agents can only read/write specific directories)
- Mental models (persistent `.yaml` expertise files per agent)
- Skills as composable markdown rules (active-listener, zero-micro-management, etc.)
- TillDone task tracking (shared task lists across agents)
- Nuclear UI pattern (replace Pi's display layer, keep the brain)
- JSONL conversation logging with shared context

**Architecture:** Orchestrator (Opus) routes to 3 team leads (Opus): Planning, Engineering, Validation. Each lead delegates to 2 workers (Sonnet). Total: 10 agents.

**File inventory:**
- `apps/multi-team-chat/extensions/multi-team-chat.ts` (58K) — main UI + orchestration
- `apps/multi-team-chat/extensions/lead-delegate.ts` — delegation tool
- `apps/multi-team-chat/extensions/domain-enforcer.ts` — file access control
- `apps/multi-team-chat/extensions/tilldone-lead.ts` — task tracking
- `apps/multi-team-chat/extensions/modules/` — types, config, domain, subprocess, tilldone, log, prompt, theme
- `.pi/multi-team/agents/` — 10 agent prompts
- `.pi/multi-team/skills/` — 6 composable behavioral rules
- `.pi/multi-team/expertise/` — 10 mental model files
- Multiple config variants (engineering-only, planning+engineering, 3x-engineering, multi-provider)

**Reusable for Hubify Labs:**
- The ENTIRE delegation hierarchy (this IS the skeleton)
- Domain locking for multi-agent safety
- Mental model persistence
- Config-driven team scaling (add teams in YAML, no code changes)
- TillDone task tracking

---

### 3. UI-Agents (MOST COMPLETE)
**Location:** `/Users/houstongolden/Desktop/CODE_2025/ui-agents/`
**What it is:** Complete multi-team system for generating brand-consistent UI at scale. 12 agents, parallel teams, validation pipeline, Vue app for browsing output.

**Key patterns to extract:**
- Parallel round-robin team assignment (3x UI Gen teams + 3x Validation teams)
- Activity polling (agents write `activity.yaml`, Vue polls every 3s)
- Brand token system (zero hardcoded values, all CSS custom properties)
- Zod schema validation before writes
- Vite middleware as REST API over filesystem
- Live brand editing (change palette, all components update instantly)
- 5-level hierarchy: Brand > Product > Tree > Branch > Leaf

**Architecture:** Orchestrator > Setup Team + Brand Team + UI Generation (x3 parallel) + Validation (x3 parallel). Total: 12 agents, 6 teams.

**File inventory:**
- `apps/infinite-ui/` — Full Vue 3 + Vite app with VueFlow canvas, gallery, sidebar
- `.pi/multi-team/agents/` — 12 agent prompts
- `.pi/multi-team/expertise/` — mental models for all agents
- `.pi/multi-team/skills/` — shared behavioral rules
- `.pi/prompts/multi-team/generate.md` — orchestration workflow
- Multiple brand examples (Aegis with production-quality Vue components)

**Reusable for Hubify Labs:**
- Parallel team duplication (scale by copying team config)
- Activity tracking pattern (real-time progress in TUI/web)
- Validation pipeline (soft + hard validation stages)
- The entire Vue app architecture (adapt for research monitoring)
- Mental model sharing across parallel team instances

---

### 4. Pi Framework (pi.dev)
**What it is:** Minimal, extensible terminal coding agent framework. The harness that runs all three codebases above.

**Key characteristics:**
- Open-source, TypeScript-based agent harness
- 15+ LLM provider support
- 4 runtime modes: interactive, print/JSON, RPC, SDK
- JSONL sessions with in-place branching
- Extensions system for custom tools, TUI widgets, commands
- No built-in sub-agents — you build exactly what you need

**Comparison with Claude Code Agent tool:**
| Dimension | Pi | Claude Code Agent |
|-----------|----|--------------------|
| Hierarchy | 3+ levels (orch > leads > workers) | 1 level (parent > child) |
| Learning | Persistent mental models | No inter-session learning |
| Parallelism | Explicit round-robin | Sequential |
| Customization | Full (TypeScript extensions) | Limited |
| Model routing | Per-agent model selection | Single model per session |
| Domain safety | Per-agent file permissions | Global access |

**For Hubify Labs:** Pi is the harness. Claude Code is the brain inside the harness. Pi manages the organization; Claude Code does the actual thinking and tool use.

---

## Extraction & Integration Plan

### Phase 1: Foundation (Week 1-2)

**Step 1:** Clone lead-agents structure as the base
```bash
cp -r /Users/houstongolden/Desktop/CODE_2025/lead-agents/.pi/multi-team/ \
      /Users/houstongolden/Desktop/CODE_2025/hubify-labs/.pi/multi-team/
```

**Step 2:** Adapt agent prompts for research (replace engineering roles):
- Orchestrator > Research strategy routing
- Planning Lead > Research Planning Lead (hypotheses, experiment design)
- Engineering Lead > Computation Lead (GPU pipelines, MCMC, inference)
- Validation Lead > QC Lead (quality gates, cross-validation, peer review)
- Product Manager > Literature Agent (paper search, prior art)
- UX Researcher > Data Explorer Agent (visualization, anomaly browsing)
- Frontend Dev > Pipeline Agent (download, preprocess, inference scripts)
- Backend Dev > Analysis Agent (statistics, cross-matching, catalog building)
- QA Engineer > Reproducibility Agent (checkpoint, resume, convergence)
- Security Reviewer > Skeptic Agent (overclaiming detection, systematic checks)

**Step 3:** Extract parallel team pattern from ui-agents
- Create 3x Computation teams for parallel GPU experiments
- Create 3x Validation teams for parallel QC

**Step 4:** Extract deliberation pattern from ceo-agents
- Add research strategy deliberation before major decisions
- Tension pairs: Optimist vs Skeptic, Speed vs Rigor, Depth vs Breadth

### Phase 2: CLI/TUI (Week 2-3)

**Step 5:** Build the Hubify Labs TUI (adapt lead-agents Nuclear UI):
- Global view: all Labs/Teams, costs, active pods, experiment counts
- Lab view: team tree, running experiments, recent results
- Project view: experiment queue, GPU status, paper progress
- Agent feed: live commentary from active agents

**Step 6:** Integrate activity polling from ui-agents:
- Agents write `activity.yaml` as experiments progress
- TUI polls and renders live progress bars, ETA, costs

**Step 7:** Add Pi commands for research workflows:
- `/new-experiment <description>` > routes to Computation Lead
- `/analyze <dataset>` > routes to Analysis Lead
- `/write-paper <topic>` > routes to Writing Lead
- `/run-queue` > Computation Lead manages full queue autonomously

### Phase 3: Integration (Week 3-4)

**Step 8:** Connect to Hubify's Convex backend
- Sync experiment results to Convex tables
- Cross-project discovery correlation
- Agent activity streaming to web dashboard

**Step 9:** Connect to RunPod API
- Infrastructure Lead manages pod lifecycle
- Budget Guardian cron monitors spend
- Auto-backup before any pod changes

**Step 10:** Connect to BigBounce as first Lab
- Import existing CLAUDE.md, research queue, experiment scripts
- All 50+ existing experiments become the knowledge base
- Mental models pre-populated with BigBounce learnings

### Phase 4: Self-Improvement (Week 4+)

**Step 11:** Create "Hubify Labs" Lab that improves itself
- Agents that improve the platform code
- AutoAgent-style harness optimization
- Self-updating prompts based on experiment outcomes

**Step 12:** Launch second Lab (new research domain)
- Prove the platform generalizes beyond astrophysics
- Candidates: genomics, materials science, climate, particle physics

---

## Reference Links

### Local Codebases
- CEO-Agents: `/Users/houstongolden/Desktop/CODE_2025/ceo-agents/`
- Lead-Agents: `/Users/houstongolden/Desktop/CODE_2025/lead-agents/`
- UI-Agents: `/Users/houstongolden/Desktop/CODE_2025/ui-agents/`
- Hubify Platform: `/Users/houstongolden/Desktop/CODE_2025/hubify/`
- BigBounce: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/`

### External References
- Pi Framework: https://pi.dev
- Pi Subagents Pattern: https://github.com/nicobailon/pi-subagents
- Karpathy autoresearch: https://github.com/karpathy/autoresearch
- AutoAgent (self-improving harness): https://github.com/kevinrgu/autoagent
- Feynman CLI research agent: https://github.com/getcompanion-ai/feynman
- Karpathy LLM Wiki: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- CMU Keystone AI+Astronomy: https://www.cmu.edu/news/stories/archives/2026/april/

### Vision Documents
- BigBounce "The Window" essay: `articles/the-window.html`
- Hubify Lab Vision: `project-context/hubify_lab_vision.md`
- Hubify Lab UX Vision: `project-context/hubify-lab-ux-vision.md`
- Hubify Lab Platform Prompt: `project-context/hubify-lab-platform-prompt.md`
- Hubify Pivot Assessment: `project-context/hubify-pivot-assessment.md`
- Houston's Approach: `project-context/houstons-approach.md`
- Houston Method v2: `project-context/houston-method-v2.md`

---

## Key Technical Decisions

1. **Pi as the harness, Claude Code as the brain** — Pi manages the org hierarchy, sessions, TUI. Claude Code does the actual research, coding, SSH, Git.

2. **Flexible model routing** — Orchestrator: Opus. Leads: Opus or Sonnet. Workers: Sonnet or Haiku. Configurable per agent in YAML.

3. **CLI/TUI-first, web for monitoring** — The work happens in the terminal. The web dashboard is for oversight, not operation.

4. **BigBounce as case study #1** — Prove the platform on real science before generalizing.

5. **Self-improving from day 1** — Mental models compound. Agents update their own expertise. The system that builds the system.

6. **Domain locking for safety** — Agents can only touch their designated files/directories. Prevents conflicts in multi-agent parallel execution.

7. **Budget-aware by default** — Every agent tracks cost. Infrastructure Lead manages pod lifecycle. Budget Guardian prevents overspend.
