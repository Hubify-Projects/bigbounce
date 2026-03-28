# Hubify Lab — UI/UX Vision: The Agentic Research OS

**Created:** 2026-03-28
**Purpose:** Guide the Hubify agent on exactly what to build. This is the product spec.

---

## The One-Line Pitch

**A black terminal where you command a fleet of AI research agents running real science across multiple projects simultaneously — and every discovery, failure, and insight is logged transparently in real time.**

---

## Design Philosophy

- **Terminal-first, not dashboard-first.** The primary interaction is typing commands and reading output, not clicking widgets. Think `htop` meets research lab, not Notion meets Jira.
- **Black and white.** Monospace. No gradients, no illustrations, no marketing. The aesthetic is a working research terminal, not a SaaS product.
- **Information-dense.** Every pixel earns its place. Status bars, live logs, progress indicators — all visible at a glance without clicking into subpages.
- **Multiple panes.** Like tmux splits. You should see 2-4 research projects running simultaneously with live output.

---

## Screen Layout

```
┌──────────────────────────────────────────────────────────────────────────────┐
│  HUBIFY LAB  ▸ 6 projects ▸ 3 active ▸ $47.20 today ▸ 2 pods running      │
│  ◉ bigbounce (88%)  ◉ sdss-scan (queued)  ◉ erosita (planning)            │
├────────────────────────────────┬─────────────────────────────────────────────┤
│                                │                                             │
│  GLOBAL RESEARCH CHAT          │  PROJECT: bigbounce                         │
│  ─────────────────────         │  ──────────────────                         │
│                                │                                             │
│  houston > what's the status   │  [H200] enhanced_18M ████████████░░ 88.2%  │
│  across all projects?          │  Pixels: 17378/27488 | ETA: 5.0h           │
│                                │  Rows: 15.6M/17.7M | Errors: 2            │
│  lab > 3 projects active:      │  Batch: 29 | Disk: 5.6GB/10GB             │
│  • bigbounce: H200 at 88%,    │                                             │
│    enhanced 18M finishing in   │  [COMPLETE] chirality 8.47M galaxies       │
│    ~5h. chirality done.        │  [COMPLETE] anomaly scan 195K objects      │
│  • sdss-scan: queued, waiting  │  [COMPLETE] mcmc w0wa 50880 samples        │
│    for bigbounce H200 to free  │                                             │
│  • erosita: planning phase,    │  ── Recent Activity ──                      │
│    houston-relentless flagged  │  03:41 batch_0029.parquet written (367MB)   │
│    "why not start download     │  03:38 checkpoint: 17378 pixels done       │
│    while H200 is busy?"        │  02:15 auto-sync: 3 batches downloaded     │
│                                │  01:30 batch_0028.parquet written           │
│  houston > good point, start   │                                             │
│  erosita data download on      │  ── Backups ──                              │
│  local machine now             │  Local: 29 batches (10.7GB) ✓              │
│                                │  B2: 22 batches (7.6GB) ✓                  │
│  lab > starting erosita        │  HuggingFace: model ✓ dataset pending     │
│  download. 710K sources,       │  Convex: metadata ✓                        │
│  ~8GB. ETA 20 min on your      │                                             │
│  connection.                   │                                             │
│                                │                                             │
│  ░░░░░░░░░░░░░░░░░░░░░░░░░░░  │                                             │
│  > _                           │  > _                                        │
│                                │                                             │
├────────────────────────────────┴─────────────────────────────────────────────┤
│  AGENT FEED                                                                  │
│  ────────────                                                                │
│  [houston-relentless] "erosita download can run in parallel with H200       │
│   inference — different machine, different network. why wait?"               │
│  [skeptic] "the erosita autoencoder needs retraining for X-ray spectra.     │
│   DESI model won't transfer. budget 4h training before inference."          │
│  [optimizer] "RunPod spot H100 available at $1.89/hr — 37% cheaper than    │
│   current on-demand. want me to migrate the next job?"                       │
│  [infra] "auto-sync cycle 7 complete. 3 new batches downloaded. disk at    │
│   5.6GB, safe. next sync in 1h47m."                                         │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## The Four Panels

### 1. Global Research Chat (left pane)

Your primary interface. Talk to the lab like talking to Claude Code, but it knows about ALL projects.

**Capabilities:**
- Ask about status across projects: "what's running?"
- Give strategic direction: "prioritize erosita over lamost"
- Brainstorm: "what if we cross-matched our anomalies with the ZTF alert stream?"
- Review: "show me the top 10 anomalies from the latest batch"
- Human-in-the-loop decisions: "the skeptic agent flagged this claim — I've reviewed it, proceed"

**Under the hood:** This is Claude Code (or equivalent) with context on all active projects, access to all project directories, RunPod API, Convex, GitHub, B2, etc. The same capabilities as our current working setup, but with awareness of multiple projects.

### 2. Project Pane (right pane, switchable)

Shows the focused view of one project. Click project tabs at top to switch. Shows:
- **Live pipeline status**: progress bars, ETA, error count, disk usage
- **Recent activity log**: timestamped events (batch writes, checkpoints, syncs, errors)
- **Backup status**: green checkmarks for each backup location
- **Quick actions**: "open explorer", "view latest batch", "SSH to pod", "view paper draft"

Each project has its own terminal you can type into for project-specific commands.

### 3. Agent Feed (bottom strip)

A scrolling feed of agent commentary. The four agent personalities are always running in the background:

| Agent | Role | Voice |
|-------|------|-------|
| **houston-relentless** | Pushes forward. Asks "why not more?" Suggests parallelization. Refuses conservative defaults. | "We have 4 hours of GPU idle time while downloading. Why not train the eROSITA autoencoder during that window?" |
| **skeptic** | Challenges claims. Checks novelty. Flags overclaiming. | "The anomaly rate of 0.75% could be explained by DESI pipeline ZWARN flags. Have we ruled that out?" |
| **optimizer** | Watches costs, speeds, efficiency. Suggests RunPod spot instances, batch sizes, caching. | "Switching to prefetch=4 cut download time 6x. Should we benchmark prefetch=8 on the next survey?" |
| **infra** | Monitors pods, disk, backups, deployments. Alerts on issues before they crash things. | "Pod disk at 8.2GB. Auto-sync running in 12 minutes. If it doesn't free space, I'll trigger early." |

**Key feature:** These agents don't just observe — they write their observations to a log that feeds into the next Claude Code decision. The houston-relentless agent's suggestions become part of the prompt. The skeptic's concerns get flagged for human review.

### 4. Top Status Bar

One-line summary always visible:
```
HUBIFY LAB  ▸ 6 projects ▸ 3 active ▸ $47.20 today ▸ 2 pods running
◉ bigbounce (88%)  ◉ sdss-scan (queued)  ◉ erosita (planning)  ○ lamost  ○ planck  ○ neowise
```

Color coding: ◉ green = active, ◉ yellow = queued, ◉ blue = planning, ○ gray = not started

---

## The Multi-Model Review Loop (Automated)

This is the system that replicates what Houston does manually today (copying reports between Claude/ChatGPT/Gemini):

```
Claude Code produces a research report or finding
    │
    ├──→ ChatGPT o3 (extended thinking): "What's the theoretical significance?
    │    Are we overclaiming? What literature supports or contradicts this?"
    │
    ├──→ Gemini Deep Think: "Alternative interpretation? What would a skeptic say?
    │    Is there a simpler explanation?"
    │
    ├──→ DeepSeek R1 (math validation): "Are the equations dimensionally consistent?
    │    Does the numerical result match the analytical prediction?"
    │
    └──→ Synthesis Agent: Combines all responses, flags disagreements,
         highlights consensus, presents to human with:
         "3/4 models agree this is novel. Gemini flagged a potential
          confound with dust extinction. Want to investigate?"
              │
              └──→ Human reviews, decides, pushes forward or investigates
```

**Implementation:** API calls to each model with structured prompts. Results stored in Convex per-project. The synthesis happens in Claude Code which has the full context.

---

## Project Lifecycle

```
1. IDEATION        Houston types: "let's scan eROSITA"
   │                Lab agent creates project scaffold
   │
2. PLANNING        Auto-generates: data source, model architecture,
   │                estimated cost, timeline, novelty check vs literature
   │                houston-relentless: "why not also cross-match with our DESI anomalies?"
   │                skeptic: "eROSITA X-ray spectra need different preprocessing than optical"
   │
3. PROVISIONING    Creates: new GitHub repo, new Convex app, new Netlify site
   │                Allocates: RunPod pod (spot if available), B2 bucket path
   │                Copies: pipeline template from bigbounce patterns
   │
4. EXECUTION       Claude Code terminal runs the pipeline
   │                Auto-checkpoint, auto-sync, auto-backup
   │                Agent feed comments in real time
   │                Multi-model review on key findings
   │
5. DISCOVERY       Results flow to project dashboard
   │                Cross-project correlations flagged automatically
   │                "Object X is anomalous in BOTH DESI spectra AND eROSITA X-ray"
   │
6. PUBLICATION     LaTeX draft auto-generated from results
   │                Figures auto-generated from data
   │                Multi-model peer review before human review
   │                HuggingFace data release prepared
   │
7. MAINTENANCE     Model + catalog on HuggingFace
                    Explorer UI on project website
                    Cross-references updated when new surveys complete
```

---

## Data Architecture (Per Project)

```
GitHub repo: Hubify-Projects/{project-name}
├── CLAUDE.md              (project-specific agent instructions)
├── pipeline/              (inference scripts, model code)
├── project-context/       (plans, approach, status)
├── convex/                (project-specific Convex app)
├── arxiv/                 (paper LaTeX + figures)
├── public/                (website assets)
└── .env.local             (project-specific credentials)

Convex app: {project-name}-{hash}.convex.cloud
├── anomalies table        (scored objects)
├── pipelineState table    (checkpoint, progress)
├── reviews table          (human + agent comments)
└── crossMatches table     (links to other projects' objects)

RunPod: per-project pods (provisioned on demand)
B2: b2://hubify-lab/{project-name}/
HuggingFace: hubify-lab/{project-name}-model, hubify-lab/{project-name}-catalog
```

---

## The Key Differentiator: Feedback Loop Guards

These are the automated systems that prevent the AI from being too conservative or too hasty:

### Guard 1: Anti-Premature-Closure
When any agent output contains phrases like "ready to publish," "sufficient for a paper," "we can stop here," "this is good enough" → automatically trigger:
- houston-relentless response: "What else could we add? More columns? More cross-references? Higher resolution?"
- Flag for human review with the question: "Is this actually done, or should we push further?"

### Guard 2: Anti-Conservative-Default
When any agent suggests "this is too complex," "we should simplify," "let's do the easier version" → automatically trigger:
- Optimizer response: "Here's how we could do the hard version: [parallelization plan, cost estimate, timeline]"
- Flag for human: "The agent suggested the easy path. Here's what the hard path would give us."

### Guard 3: Pro-Optimization
After any pipeline completes successfully → automatically trigger:
- Optimizer: "This ran at X speed. With [specific optimization], we could do it Y% faster next time."
- houston-relentless: "Good. Now what's the NEXT survey we can run the same pipeline on?"

### Guard 4: Multi-Model Validation
When any finding is flagged as "novel" or "first of its kind" → automatically trigger:
- Literature search (Semantic Scholar API, ADS, arXiv)
- ChatGPT fact-check: "Has anyone published this before?"
- Flag for human with evidence either way

### Guard 5: Budget Guardian
When RunPod spend exceeds daily/weekly threshold → automatically trigger:
- infra agent: "Spend at $X today. At current rate, weekly total will be $Y. Budget is $Z."
- Suggest: spot instances, pausing non-critical pods, optimizing batch sizes
- NEVER auto-terminate a pod — always flag for human decision (learned from the 130K galaxy incident)

---

## Implementation Priority

### Phase 1: Core Terminal (Week 1)
- Black terminal UI with split panes
- Global chat connected to Claude Code (via API or local Claude Code process)
- Project list with status indicators
- Basic project creation (fork template, create repo, create Convex app)

### Phase 2: Agent Feed + Multi-Model Loop (Week 2)
- Agent personality prompts running on cron (every 30 min)
- ChatGPT/Gemini API integration for cross-validation
- Agent feed panel with timestamped commentary
- Feedback loop guards (anti-premature-closure, etc.)

### Phase 3: Pipeline Orchestration (Week 3)
- RunPod provisioning from the UI
- Auto-checkpoint monitoring
- Auto-sync setup per project
- Backup verification dashboard

### Phase 4: Cross-Project Intelligence (Week 4)
- Cross-match objects across project catalogs
- "This object is anomalous in 2+ surveys" alerts
- Unified discovery dashboard
- LaTeX + figure auto-generation

---

## What This Is NOT

- Not a generic AI agent framework
- Not a SaaS product for other users (yet)
- Not a dashboard with charts and widgets
- Not a project management tool

**It IS:** A personal research operating system built for one person (Houston) to run multiple scientific research missions simultaneously with AI assistance, multi-model review, and transparent logging. If it works, THEN we can consider opening it up.

---

## The Feeling

When you sit down at this terminal, it should feel like:
- Commanding a fleet of research ships from a bridge
- Each ship (project) is autonomous but reports back
- Your agents are your crew — some push forward, some check the work, some watch the instruments
- You're the captain making strategic decisions and pushing past the conservative defaults
- Everything is logged, everything is backed up, nothing is lost
- The universe's data is streaming through your terminal and you're finding things no one has found before

That's the feeling. Build that.
