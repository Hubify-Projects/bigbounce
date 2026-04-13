# Hubify Labs — Product Requirements Document

**Version:** 1.2 | **Author:** Houston Golden + Claude Code | **Date:** 2026-04-07
**Status:** ACTIVE — Implementation-ready specification

---

## NEW SESSION KICKSTART PROMPT

Copy-paste this into a new Claude Code session opened at `~/Desktop/CODE_2025/` (the parent directory, NOT bigbounce or hubify):

```
/effort max

Read the complete Hubify Labs PRD at /Users/houstongolden/Desktop/CODE_2025/bigbounce/project-context/HUBIFY_LABS_PRD.md — this is the definitive specification for building the Hubify Labs autonomous multi-agent research platform.

Also read these for full context:
- /Users/houstongolden/Desktop/CODE_2025/bigbounce/project-context/hubify-labs-platform-plan.md (architecture plan with indydevdan codebase audits)
- /Users/houstongolden/Desktop/CODE_2025/bigbounce/CLAUDE.md (BigBounce project instructions)
- /Users/houstongolden/Desktop/CODE_2025/hubify/project-context/ARCHITECTURE_DATAFLOW.md (Hubify platform architecture)
- /Users/houstongolden/Desktop/CODE_2025/bigbounce/project-context/INFRASTRUCTURE_MAP.md (BigBounce infrastructure)

CRITICAL SAFETY RULES:
1. NEVER write to, modify, or delete anything in ~/Desktop/CODE_2025/bigbounce/ — this is the original research project with irreplaceable data
2. NEVER write to, modify, or delete anything in ~/Desktop/CODE_2025/hubify/ — this is the original platform
3. ALL new code goes in ~/Desktop/CODE_2025/hubify-labs/ (new directory)
4. BigBounce files are COPIED into hubify-labs, never moved
5. The live bigbounce.hubify.app site must continue working from the original repo

Start by executing Step 0 (Safety Forks) from the PRD, then proceed to Step 1 (create hubify-labs repo) and Week 1 of the implementation plan. Build the Pi agent harness with the research agent hierarchy. The three purchased codebases to reference for patterns are at:
- ~/Desktop/CODE_2025/ceo-agents/ (deliberation pattern)
- ~/Desktop/CODE_2025/lead-agents/ (delegation hierarchy — THE skeleton)
- ~/Desktop/CODE_2025/ui-agents/ (parallel teams, activity tracking)

Let's build Hubify Labs.
```

---

---

## 0. Executive Summary

**Hubify Labs** is an autonomous multi-agent research platform where hierarchical AI agent teams conduct scientific research across multiple domains with minimal human direction. The human is the **director** — setting strategy, reviewing discoveries, and publishing papers. Agents handle everything else: experiment design, GPU compute, data analysis, paper drafting, website updates, and self-improvement.

**Proof:** BigBounce (4 papers, 50+ GPU experiments, 328K anomalies, $400 compute, 3 months, 1 person). Tonight: 50 experiments ran autonomously while Houston slept.

**Core thesis from "The Window":** Public survey data + commodity GPUs + AI agents = a structural gap that closes in 18 months. Hubify Labs exploits this window at scale.

---

## 1. Safety-First Repository Strategy

### Architecture lock — every Lab is its own repo (Houston confirmed 2026-04-08)

There are TWO categories of repos in the Hubify Labs world. Do not confuse them.

**Category A — The PLATFORM repo (one):**
- Repo: `Hubify-Labs/hubify-labs` (currently `Hubify-Projects/hubify-labs` — org rename pending, very soon)
- Contents: the platform code itself (Convex backend, web UI, CLI, MCP server, agent harness, etc.)
- This is the SaaS-style multi-tenant platform that hosts all the labs.
- Lives in `~/Desktop/CODE_2025/hubify-labs/` locally.

**Category B — Per-Lab repos (one per lab):**
- Repo: `Hubify-Labs/<lab-slug>` (e.g. `Hubify-Labs/bigbounce-hubify`, `Hubify-Labs/dark-energy-lab`)
- Contents: that lab's actual research — papers, experiments, datasets, agents, contributions, projects, files, the whole filesystem.
- Each lab gets its OWN: GitHub repo, subdomain (`<lab-slug>.hubify.app`), filesystem layout, agent roster, memory, and version history.
- A **Project** does NOT get its own repo. Projects are subdirectories inside a Lab repo (`lab/projects/<project-slug>/`). The Lab is the unit of repo separation.
- The internal Hubify orchestrator agent has full GitHub API access to the `Hubify-Labs` org and can create/manage per-lab repos autonomously when a new lab is created via the platform.

**The migration path for BigBounce:** the existing `Hubify-Projects/bigbounce` (the original research repo) stays untouched as the historical canonical archive (frozen, read-only). A NEW Lab repo `Hubify-Labs/bigbounce-hubify` is created to host the BigBounce research migrated into Hubify Labs Lab format. The new lab's site lives at `bigbounce2.hubify.app` (or similar — final subdomain TBD in `MIGRATION_BOUNCE_COSMOLOGY_LAB.md`). The original `bigbounce.hubify.app` site keeps serving from the original repo until cutover.

**Org rename note:** Houston is renaming the GitHub org from `Hubify-Projects` to `Hubify-Labs` very soon. All new repo references in this PRD and downstream lab specs should use `Hubify-Labs/...`. References to the OLD org name in archived sections of this PRD (Steps 0-1 below, where they document how the platform repo was bootstrapped) are historical and can stay as-is.

### IRON RULE: NEVER touch the original BigBounce repo or directory.

The current `github.com/hubify-projects/bigbounce` repo, the local `~/CODE_2025/bigbounce/` directory, and the live `bigbounce.hubify.app` site contain irreplaceable research (4 papers, 50+ experiments, 328K anomalies, months of work). They MUST remain 100% untouched during and after migration.

### Step 0: Create Safety Forks (BEFORE anything else)

```bash
# ═══════════════════════════════════════════════════
# SAFETY FORKS — Do this FIRST, verify SECOND, then proceed
# ═══════════════════════════════════════════════════

# 1. Fork BigBounce repo on GitHub
gh repo fork hubify-projects/bigbounce --org hubify-projects \
  --fork-name bigbounce-archive-2026-04-07 --clone=false
# Result: github.com/hubify-projects/bigbounce-archive-2026-04-07

# 2. Fork Hubify repo on GitHub (if in an org, or just create a copy)
cd ~/Desktop/CODE_2025/hubify
git push origin main  # ensure latest is pushed
gh repo fork --fork-name hubify-archive-2026-04-07 --clone=false
# OR if not forkable: create new repo and push
gh repo create hubify-projects/hubify-archive-2026-04-07 --private
git remote add archive https://github.com/hubify-projects/hubify-archive-2026-04-07.git
git push archive --all && git push archive --tags

# 3. Local directory backups
cp -r ~/Desktop/CODE_2025/bigbounce ~/Desktop/CODE_2025/bigbounce-backup-20260407
cp -r ~/Desktop/CODE_2025/hubify ~/Desktop/CODE_2025/hubify-backup-20260407

# 4. VERIFY all 4 backups exist before proceeding
ls -la ~/Desktop/CODE_2025/bigbounce-backup-20260407/CLAUDE.md  # must exist
ls -la ~/Desktop/CODE_2025/hubify-backup-20260407/package.json   # must exist
gh repo view hubify-projects/bigbounce-archive-2026-04-07        # must exist
gh repo view hubify-projects/hubify-archive-2026-04-07           # must exist
echo "ALL 4 BACKUPS VERIFIED — safe to proceed"
```

### Step 1: Create NEW Hubify Labs repo (completely separate)

```bash
# New repo — does NOT touch bigbounce or hubify
mkdir ~/Desktop/CODE_2025/hubify-labs
cd ~/Desktop/CODE_2025/hubify-labs
git init
gh repo create hubify-projects/hubify-labs --public --source=. --push

# This is where ALL new platform code goes
# bigbounce/ directory: UNTOUCHED
# hubify/ directory: UNTOUCHED (we COPY selected files from it)
```

### Step 2: COPY (never move) from Hubify

```bash
# Copy selected Convex files INTO hubify-labs (not move, not symlink)
cp -r ~/Desktop/CODE_2025/hubify/convex/ ~/Desktop/CODE_2025/hubify-labs/convex/
# Then strip SaaS-specific tables from the copy (not from the original)

# Copy CLI framework
cp -r ~/Desktop/CODE_2025/hubify/packages/cli/ ~/Desktop/CODE_2025/hubify-labs/packages/cli/

# Copy MCP server
cp -r ~/Desktop/CODE_2025/hubify/packages/mcp/ ~/Desktop/CODE_2025/hubify-labs/packages/mcp/

# Copy Fly.io integration files
mkdir -p ~/Desktop/CODE_2025/hubify-labs/infra/
cp -r ~/Desktop/CODE_2025/hubify/infra/ ~/Desktop/CODE_2025/hubify-labs/infra/
```

**Original hubify/ directory:** UNTOUCHED. Still deployable. Still has all 96 tables. Still has the full SaaS platform. We only COPY selected files into the new hubify-labs/ project.

### What we COPY from Hubify into hubify-labs

### What we KEEP from Hubify

| Component | Location | Why |
|-----------|----------|-----|
| **Convex backend** (modified) | `convex/` | Real-time DB, WebSocket, crons — battle-tested |
| **CLI framework** | `packages/cli/` | 60+ commands, auth, shell aliases |
| **MCP server** | `packages/mcp/` | Claude Code integration |
| **Fly.io provisioning** | `apps/web/app/api/workspaces/` | Machine deploy, volumes, SSH |
| **Agent profiles + Ed25519** | `convex/agentProfiles.ts` | Identity, reputation |
| **Webhook system** | `convex/webhooks.ts` | HMAC-signed events |
| **Cron infrastructure** | `convex/crons.ts` | 30+ scheduled jobs |

### What we DO NOT COPY into hubify-labs (stays in original hubify only)

| Component | Why Not Copied |
|-----------|----------------|
| Skills marketplace UI | SaaS, not research |
| Multi-tenant workspace UI | Bloated, wrong UX |
| Hub subscriptions | Community feature, not needed for Labs |
| Template gallery | Not relevant |
| Billing/subscriptions | Self-funded research |
| Auth UI (signup/login flows) | Rebuild as terminal aesthetic |

**The original hubify/ keeps ALL of these.** We just don't copy them into hubify-labs.

### What we ADD

| Component | Source | Purpose |
|-----------|--------|---------|
| Pi agent harness | lead-agents + ui-agents | Multi-team orchestration |
| Research agent prompts | New (adapted from lead-agents) | Domain-specific agents |
| Experiment queue system | BigBounce queue_v2.py pattern | GPU experiment management |
| Lab template | New | Standardized project structure |
| Terminal UI | lead-agents Nuclear UI pattern | CLI/TUI experience |
| Next.js research sites | New | Per-lab website generation |

### New Convex Schema (Research-Focused)

The hubify-labs project gets its OWN Convex app with 18 research-focused tables. The original Hubify Convex (96 tables) stays untouched:

```typescript
// ═══════════════════════════════════════════
// CORE ENTITIES
// ═══════════════════════════════════════════

labs: defineTable({
  name: v.string(),                    // "BigBounce"
  slug: v.string(),                    // "bigbounce"
  domain: v.string(),                  // "astrophysics"
  status: v.string(),                  // "active" | "paused" | "archived"
  repo_url: v.optional(v.string()),    // "github.com/hubify-projects/bigbounce"
  site_url: v.optional(v.string()),    // "bigbounce.hubify.app"
  local_path: v.string(),             // "/Users/houston/CODE_2025/bigbounce"
  config: v.object({
    default_gpu: v.string(),           // "NVIDIA H200 SXM"
    budget_daily_usd: v.number(),      // 50.0
    budget_weekly_usd: v.number(),     // 250.0
    model_routing: v.object({
      orchestrator: v.string(),        // "anthropic/claude-opus-4-6"
      leads: v.string(),               // "anthropic/claude-sonnet-4-6"
      workers: v.string(),             // "anthropic/claude-haiku-4-5"
    }),
  }),
  stats: v.object({
    experiments_total: v.number(),
    experiments_passed: v.number(),
    papers_count: v.number(),
    anomalies_total: v.number(),
    total_cost_usd: v.number(),
    gpu_hours_total: v.number(),
  }),
  created_at: v.number(),
  updated_at: v.number(),
}).index("by_slug", ["slug"]),

experiments: defineTable({
  lab_id: v.id("labs"),
  name: v.string(),                    // "planck-cmb-masked"
  phase: v.number(),                   // 1-10
  batch: v.optional(v.string()),       // "overnight-batch-1"
  status: v.string(),                  // "queued"|"running"|"complete"|"failed"|"qc_fail"
  script_path: v.string(),            // "experiments/planck_cmb_masked.py"
  output_dir: v.string(),             // "outputs/planck-cmb-masked/"
  gpu_type: v.optional(v.string()),   // "H200 SXM"
  gpu_hours: v.optional(v.number()),
  cost_usd: v.optional(v.number()),
  qc_status: v.optional(v.string()),  // "PASS"|"FAIL"|"SKIP"
  qc_details: v.optional(v.any()),    // {checks: [...], failure_modes: [...]}
  results_summary: v.optional(v.any()), // experiment-specific results
  checkpoint: v.optional(v.any()),     // {step, state, timestamp}
  started_at: v.optional(v.number()),
  completed_at: v.optional(v.number()),
  created_at: v.number(),
}).index("by_lab", ["lab_id"])
  .index("by_status", ["lab_id", "status"])
  .index("by_phase", ["lab_id", "phase"]),

papers: defineTable({
  lab_id: v.id("labs"),
  title: v.string(),
  version: v.string(),                 // "v2.2.0"
  status: v.string(),                  // "draft"|"ready"|"submitted"|"published"
  readiness_pct: v.number(),           // 95
  tex_path: v.string(),               // "papers/paper-1/main.tex"
  pdf_path: v.optional(v.string()),   // "papers/paper-1/main.pdf"
  arxiv_id: v.optional(v.string()),
  journal: v.optional(v.string()),     // "ApJS"
  figures_count: v.number(),
  references_count: v.number(),
  pages: v.optional(v.number()),
  created_at: v.number(),
  updated_at: v.number(),
}).index("by_lab", ["lab_id"]),

// ═══════════════════════════════════════════
// AGENT SYSTEM
// ═══════════════════════════════════════════

agents: defineTable({
  lab_id: v.optional(v.id("labs")),    // null = global agent
  role: v.string(),                    // "orchestrator"|"research-lead"|"gpu-manager"
  name: v.string(),                    // "Research Lead"
  model: v.string(),                   // "anthropic/claude-opus-4-6"
  level: v.string(),                   // "orchestrator"|"lead"|"worker"
  session_path: v.string(),           // ".hubify-labs/sessions/research-lead.jsonl"
  prompt_path: v.string(),            // ".hubify-labs/agents/research-lead.md"
  status: v.string(),                  // "idle"|"active"|"error"
  total_tokens: v.number(),
  total_cost_usd: v.number(),
  last_active: v.optional(v.number()),
  created_at: v.number(),
}).index("by_lab", ["lab_id"])
  .index("by_role", ["lab_id", "role"]),

mental_models: defineTable({
  agent_id: v.id("agents"),
  content: v.string(),                 // Full YAML content
  version: v.number(),
  summary: v.optional(v.string()),     // One-line summary of key learnings
  updated_at: v.number(),
}).index("by_agent", ["agent_id"]),

// ═══════════════════════════════════════════
// COMPUTE & INFRASTRUCTURE
// ═══════════════════════════════════════════

pods: defineTable({
  lab_id: v.id("labs"),
  provider: v.string(),                // "runpod"|"lambda"|"vastai"
  pod_id: v.string(),                  // "o76k3jfzbfh25e"
  name: v.optional(v.string()),        // "sleepy_blush_crane"
  gpu_type: v.string(),                // "H200 SXM"
  status: v.string(),                  // "running"|"stopped"|"terminated"
  ssh_host: v.string(),               // "205.196.19.52"
  ssh_port: v.number(),               // 11452
  cost_per_hr: v.number(),            // 3.59
  uptime_seconds: v.optional(v.number()),
  total_cost_usd: v.optional(v.number()),
  workspace_path: v.string(),         // "/workspace/bigbounce/"
  last_checked: v.optional(v.number()),
  created_at: v.number(),
}).index("by_lab", ["lab_id"])
  .index("by_status", ["status"]),

queues: defineTable({
  lab_id: v.id("labs"),
  name: v.string(),                    // "queue-v2"
  experiments: v.array(v.string()),    // experiment IDs in order
  current_idx: v.number(),
  status: v.string(),                  // "running"|"paused"|"complete"
  total_estimated_hours: v.optional(v.number()),
  total_estimated_cost: v.optional(v.number()),
  created_at: v.number(),
  updated_at: v.number(),
}).index("by_lab", ["lab_id"]),

backups: defineTable({
  lab_id: v.id("labs"),
  location: v.string(),               // "local"|"github"|"huggingface"|"b2"|"convex"
  path: v.optional(v.string()),       // specific path or URL
  size_bytes: v.optional(v.number()),
  type: v.string(),                    // "full"|"incremental"|"experiment"
  experiment_id: v.optional(v.id("experiments")),
  status: v.string(),                  // "success"|"failed"|"pending"
  timestamp: v.number(),
}).index("by_lab", ["lab_id"]),

// ═══════════════════════════════════════════
// ACTIVITY & MONITORING
// ═══════════════════════════════════════════

activity_stream: defineTable({
  lab_id: v.optional(v.id("labs")),    // null = global
  agent_id: v.optional(v.id("agents")),
  event: v.string(),                   // "experiment_started"|"qc_passed"|"paper_compiled"|"ALERT"
  severity: v.string(),               // "info"|"success"|"warning"|"error"|"critical"
  message: v.string(),
  metadata: v.optional(v.any()),       // event-specific data
  timestamp: v.number(),
}).index("by_lab", ["lab_id", "timestamp"])
  .index("by_severity", ["severity", "timestamp"]),

cost_tracking: defineTable({
  lab_id: v.id("labs"),
  date: v.string(),                    // "2026-04-07"
  gpu_cost: v.number(),
  llm_cost: v.number(),
  storage_cost: v.number(),
  total_cost: v.number(),
  experiments_run: v.number(),
  gpu_hours: v.number(),
}).index("by_lab_date", ["lab_id", "date"]),

// ═══════════════════════════════════════════
// CROSS-LAB SHARING
// ═══════════════════════════════════════════

shared_datasets: defineTable({
  name: v.string(),                    // "desi-dr1-anomaly-catalog"
  lab_id: v.id("labs"),               // origin lab
  type: v.string(),                    // "catalog"|"model"|"chain"|"script"
  description: v.string(),
  format: v.string(),                  // "parquet"|"json"|"csv"|"pt"|"txt"
  location: v.string(),               // HuggingFace URL, B2 path, or local path
  size_bytes: v.optional(v.number()),
  row_count: v.optional(v.number()),
  schema: v.optional(v.any()),         // column definitions
  tags: v.array(v.string()),          // ["anomaly", "spectroscopic", "desi"]
  created_at: v.number(),
}).index("by_type", ["type"])
  .index("by_tags", ["tags"]),

shared_learnings: defineTable({
  lab_id: v.id("labs"),               // origin lab
  agent_role: v.string(),             // which agent discovered this
  category: v.string(),               // "operational"|"scientific"|"methodology"|"tool"
  key: v.string(),                     // "numpy-trapz-removed-in-2.4"
  insight: v.string(),                 // full description
  confidence: v.number(),             // 1-10
  applicable_to: v.array(v.string()), // ["all"]|["astrophysics","cosmology"]
  timestamp: v.number(),
}).index("by_category", ["category"])
  .index("by_applicable", ["applicable_to"]),

shared_agent_templates: defineTable({
  name: v.string(),                    // "skeptic"
  role: v.string(),                    // "worker"
  level: v.string(),                   // "lead"|"worker"
  prompt_content: v.string(),         // full .md content
  skills: v.array(v.string()),        // skill file paths
  model_recommendation: v.string(),    // "anthropic/claude-sonnet-4-6"
  domain: v.string(),                  // "general"|"astrophysics"|"biology"
  description: v.string(),
  created_at: v.number(),
  updated_at: v.number(),
}).index("by_domain", ["domain"]),

// ═══════════════════════════════════════════
// SURVEYS & EXTERNAL DATA
// ═══════════════════════════════════════════

surveys: defineTable({
  lab_id: v.id("labs"),
  name: v.string(),                    // "DESI DR1"
  short_name: v.string(),             // "desi-dr1"
  total_sources: v.optional(v.number()), // 22500000
  anomalies_found: v.optional(v.number()), // 195829
  anomaly_rate: v.optional(v.number()), // 0.0087
  qc_status: v.string(),              // "PASS"|"FAIL"|"FIXED"|"PENDING"
  data_url: v.optional(v.string()),   // archive URL
  local_path: v.optional(v.string()), // where results live locally
  pipeline_script: v.optional(v.string()),
  status: v.string(),                  // "complete"|"running"|"planned"
  notes: v.optional(v.string()),
}).index("by_lab", ["lab_id"]),

// ═══════════════════════════════════════════
// FLY.IO CLOUD DEPLOYMENT
// ═══════════════════════════════════════════

cloud_machines: defineTable({
  lab_id: v.optional(v.id("labs")),   // null = global orchestrator
  fly_app_id: v.string(),
  machine_id: v.string(),
  region: v.string(),                  // "lax"
  status: v.string(),                  // "started"|"stopped"|"destroyed"
  purpose: v.string(),                 // "orchestrator"|"lab-runner"|"site-host"
  ssh_command: v.optional(v.string()),
  created_at: v.number(),
}).index("by_lab", ["lab_id"]),

// ═══════════════════════════════════════════
// KNOWLEDGE & DISCOVERY
// ═══════════════════════════════════════════

knowledge_entries: defineTable({
  lab_id: v.id("labs"),
  type: v.string(),                    // "entity"|"concept"|"comparison"|"source"|"finding"
  title: v.string(),                   // "DESI DR1 Spectral Survey"
  slug: v.string(),                    // "desi-dr1"
  content: v.string(),                 // Full markdown content
  status: v.string(),                  // "draft"|"verified"|"canonical"|"refuted"
  confidence: v.optional(v.number()), // 1-10
  related_experiments: v.optional(v.array(v.id("experiments"))),
  tags: v.array(v.string()),
  created_by: v.optional(v.id("agents")),
  created_at: v.number(),
  updated_at: v.number(),
}).index("by_lab", ["lab_id"])
  .index("by_type", ["lab_id", "type"])
  .index("by_slug", ["lab_id", "slug"]),

cross_lab_matches: defineTable({
  lab_a_id: v.id("labs"),
  lab_b_id: v.id("labs"),
  experiment_a_id: v.optional(v.id("experiments")),
  experiment_b_id: v.optional(v.id("experiments")),
  ra: v.number(),                      // Right ascension (degrees)
  dec: v.number(),                     // Declination (degrees)
  separation_arcsec: v.number(),       // Angular separation
  score_a: v.optional(v.number()),    // Anomaly score from lab A
  score_b: v.optional(v.number()),    // Anomaly score from lab B
  match_type: v.string(),             // "spatial"|"spectral"|"temporal"
  significance_sigma: v.optional(v.number()),
  status: v.string(),                  // "candidate"|"verified"|"false_positive"
  created_at: v.number(),
}).index("by_labs", ["lab_a_id", "lab_b_id"])
  .index("by_status", ["status"]),

pipeline_runs: defineTable({
  lab_id: v.id("labs"),
  pipeline_name: v.string(),           // "p1-highz-tracers"
  current_step: v.number(),            // 3
  total_steps: v.number(),             // 6
  steps: v.array(v.object({
    name: v.string(),
    status: v.string(),                // "complete"|"running"|"pending"|"failed"
    experiment_id: v.optional(v.id("experiments")),
    started_at: v.optional(v.number()),
    completed_at: v.optional(v.number()),
  })),
  status: v.string(),                  // "running"|"paused"|"complete"|"failed"
  created_at: v.number(),
  updated_at: v.number(),
}).index("by_lab", ["lab_id"]),

figures: defineTable({
  lab_id: v.id("labs"),
  paper_id: v.optional(v.id("papers")),
  name: v.string(),                    // "fig_posterior_w0wa.png"
  caption: v.optional(v.string()),
  file_path: v.string(),              // "papers/paper-1/figures/fig1.png"
  experiment_id: v.optional(v.id("experiments")), // which experiment generated it
  status: v.string(),                  // "current"|"stale"|"draft"
  width_px: v.optional(v.number()),
  height_px: v.optional(v.number()),
  created_at: v.number(),
  updated_at: v.number(),
}).index("by_lab", ["lab_id"])
  .index("by_paper", ["paper_id"]),

alerts: defineTable({
  lab_id: v.optional(v.id("labs")),   // null = global
  severity: v.string(),               // "warning"|"error"|"critical"
  source: v.string(),                  // "runpod_credits"|"pod_crash"|"budget_exceeded"|"qc_fail"
  message: v.string(),
  metadata: v.optional(v.any()),
  acknowledged: v.boolean(),           // Human has seen this
  acknowledged_at: v.optional(v.number()),
  resolved: v.boolean(),               // Issue is fixed
  resolved_at: v.optional(v.number()),
  created_at: v.number(),
}).index("by_severity", ["severity", "acknowledged"])
  .index("by_lab", ["lab_id"]),

global_config: defineTable({
  key: v.string(),                     // "model_defaults"|"budget_defaults"|"theme"|"notifications"
  value: v.any(),                      // Config-specific JSON
  updated_at: v.number(),
}).index("by_key", ["key"]),
```

**Total: 22 tables.** Every table serves the research mission. Zero SaaS bloat.

**See also:** `project-context/HUBIFY_LABS_UI_SPEC.md` for full UI/UX design specification.

---

## 2. Standardized Lab Template

Every Lab follows this structure. BigBounce is the first instance.

```
lab-name/
├── .hubify-labs/                      # Platform integration layer
│   ├── config.yaml                    # Lab identity + model routing + teams
│   ├── agents/                        # Agent system prompts (.md with YAML frontmatter)
│   │   ├── orchestrator.md            # Lab-level orchestrator
│   │   ├── research-lead.md           # Hypotheses, experiment design
│   │   ├── analysis-lead.md           # Statistics, cross-matching, QC
│   │   ├── writing-lead.md            # Papers, figures, website
│   │   ├── infrastructure-lead.md     # GPU pods, backups, deployment
│   │   ├── literature-agent.md        # Paper search, prior art (worker)
│   │   ├── computation-agent.md       # Write experiment scripts (worker)
│   │   ├── pipeline-agent.md          # Download, preprocess data (worker)
│   │   ├── statistics-agent.md        # MCMC, Fisher, inference (worker)
│   │   ├── qc-agent.md               # Quality gates, validation (worker)
│   │   ├── paper-writer.md            # LaTeX drafting (worker)
│   │   ├── figure-generator.md        # Plot generation (worker)
│   │   ├── skeptic-agent.md           # Overclaiming detection (worker)
│   │   ├── gpu-manager.md             # Pod lifecycle (worker)
│   │   └── backup-agent.md            # Multi-location backup (worker)
│   │
│   ├── skills/                        # Composable behavioral rules
│   │   ├── houston-method.md          # 9-step completion loop (mandatory)
│   │   ├── active-listener.md         # Read conversation log first
│   │   ├── zero-micro-management.md   # Leads delegate, never execute
│   │   ├── precise-worker.md          # Workers execute exactly as assigned
│   │   ├── mental-model.md            # Read expertise at start, update after
│   │   ├── budget-aware.md            # Track and report costs
│   │   ├── backup-first.md            # Always backup before destructive actions
│   │   └── never-accept-complete.md   # Always propose next experiment
│   │
│   ├── expertise/                     # Agent mental models (YAML, synced to Convex)
│   │   ├── orchestrator-mental-model.yaml
│   │   ├── research-lead-mental-model.yaml
│   │   ├── analysis-lead-mental-model.yaml
│   │   └── [one per agent]
│   │
│   ├── sessions/                      # JSONL conversation logs (local only)
│   │   ├── orchestrator.jsonl
│   │   └── [per-session files]
│   │
│   ├── queue.json                     # Active experiment queue
│   └── activity.yaml                  # Real-time progress for TUI polling
│
├── experiments/                        # GPU experiment scripts
│   ├── scripts/                        # Python scripts (deployable to pod)
│   │   ├── planck_cmb_masked.py
│   │   ├── fnl_bias_validation.py
│   │   └── [48 scripts for BigBounce]
│   ├── results/                        # Local results cache (backed up from pod)
│   │   ├── phase1_3_queue_v2/
│   │   ├── phase4_science/
│   │   ├── phase5_surveys/
│   │   ├── phase6_xray/
│   │   ├── overnight_batch1/
│   │   └── overnight_batch2/
│   └── checkpoints/                    # Resume state per experiment
│
├── pipelines/                          # Research pipelines (multi-step workflows)
│   ├── p1-highz-tracers/
│   │   ├── scripts/
│   │   ├── outputs/
│   │   └── README.md
│   ├── p2-chirality/
│   ├── p3-anomaly-engine/
│   └── [domain-specific pipelines]
│
├── papers/                             # LaTeX papers
│   ├── paper-1-spin-torsion/
│   │   ├── main.tex
│   │   ├── references.bib
│   │   ├── figures/
│   │   └── main.pdf
│   ├── paper-2-fnl-forecast/
│   ├── paper-3-anomaly-catalog/
│   └── paper-4-chirality/
│
├── data/                               # Research data (gitignored for large files)
│   ├── chains/                         # MCMC chains (Git LFS)
│   ├── catalogs/                       # Generated anomaly catalogs
│   ├── models/                         # Trained model weights (.pt)
│   ├── external/                       # Downloaded survey data
│   └── backups/                        # Recovered backup data
│
├── site/                               # Next.js research website
│   ├── app/                            # Next.js app directory
│   │   ├── page.tsx                    # Homepage (research overview)
│   │   ├── papers/page.tsx             # Paper listing
│   │   ├── data/page.tsx               # Data explorer
│   │   ├── activity/page.tsx           # Activity feed
│   │   ├── figures/page.tsx            # Figure gallery
│   │   ├── glossary/page.tsx           # Equations + glossary
│   │   ├── anomalies/page.tsx          # Anomaly explorer
│   │   └── layout.tsx                  # Shared layout + nav
│   ├── components/                     # Reusable React components
│   │   ├── StatCard.tsx
│   │   ├── DataTable.tsx
│   │   ├── FigureGallery.tsx
│   │   ├── ActivityFeed.tsx
│   │   ├── EquationRenderer.tsx
│   │   └── ExperimentStatus.tsx
│   ├── lib/                            # Data loading, Convex client
│   ├── public/                         # Images, PDFs, spreadsheets
│   ├── styles/                         # Tailwind + custom CSS
│   ├── next.config.js
│   ├── tailwind.config.js
│   └── package.json
│
├── knowledge/                          # LLM Wiki (Karpathy-style)
│   ├── entities/                       # Named things (surveys, instruments, objects)
│   ├── concepts/                       # Physics concepts (bounce, f_NL, etc.)
│   ├── comparisons/                    # Model vs model comparisons
│   ├── sources/                        # Paper summaries
│   └── INDEX.md                        # Auto-generated index
│
├── context/                            # Strategy & methodology
│   ├── vision.md                       # Lab mission
│   ├── approach.md                     # Houston's 8 principles
│   ├── method.md                       # Houston Method v2 (9-step loop)
│   ├── status.md                       # Current status (auto-updated)
│   ├── infrastructure.md               # Infrastructure map
│   ├── portfolio.md                    # Research portfolio strategy
│   └── peer-reviews/                   # Review history
│
├── CLAUDE.md                           # AI instructions for this lab
├── README.md                           # Lab overview
├── version.json                        # Version metadata
└── .env.local                          # Secrets (gitignored)
```

### BigBounce Integration into Hubify Labs

**CRITICAL: The original `bigbounce/` directory and `github.com/hubify-projects/bigbounce` repo are NEVER modified.** BigBounce continues to exist exactly as-is. The live site `bigbounce.hubify.app` continues deploying from the original repo.

**What happens:** We COPY relevant files from `bigbounce/` into a new Lab directory inside `hubify-labs/`. The original BigBounce project continues independently. Over time, new research happens in the Labs version while the original remains as the archive/production site.

```bash
# Create BigBounce Lab inside hubify-labs (COPY, not move)
mkdir -p ~/Desktop/CODE_2025/hubify-labs/labs/bigbounce

# Copy script (preserves originals)
DEST=~/Desktop/CODE_2025/hubify-labs/labs/bigbounce
SRC=~/Desktop/CODE_2025/bigbounce

cp -r $SRC/arxiv/                    $DEST/papers/paper-1-spin-torsion/
cp -r $SRC/research/focused_paper_source_integration/ $DEST/papers/paper-2-fnl-forecast/
cp -r $SRC/h200_scripts/experiments/ $DEST/experiments/scripts/
cp -r $SRC/pipelines/h200_results/   $DEST/experiments/results/
cp -r $SRC/pipelines/p1_highz_tracers/ $DEST/pipelines/p1-highz-tracers/
cp -r $SRC/pipelines/p2_chirality/   $DEST/pipelines/p2-chirality/
cp -r $SRC/pipelines/p3_anomaly_engine/ $DEST/pipelines/p3-anomaly-engine/
cp -r $SRC/reproducibility/cosmology/ $DEST/data/chains/
cp -r $SRC/public/images/            $DEST/site/public/images/
cp -r $SRC/public/papers/            $DEST/site/public/papers/
cp -r $SRC/project-context/          $DEST/context/
cp -r $SRC/wiki/                     $DEST/knowledge/
cp    $SRC/CLAUDE.md                 $DEST/CLAUDE.md
cp    $SRC/.env.local                $DEST/.env.local 2>/dev/null || true
cp    $SRC/research_queue.json       $DEST/.hubify-labs/queue.json
cp    $SRC/version.json              $DEST/version.json

# Verify original is untouched
diff <(ls $SRC) <(ls $SRC) && echo "ORIGINAL BIGBOUNCE: UNTOUCHED"
```

### BigBounce Copy Map

| Source (bigbounce/) | Destination (hubify-labs/labs/bigbounce/) | Action |
|---------------------|------------------------------------------|--------|
| `arxiv/` | `papers/paper-1-spin-torsion/` | **COPY** |
| `research/focused_paper_*/` | `papers/paper-2-fnl-forecast/` | **COPY** |
| `pipelines/p3_anomaly_engine/` (paper files) | `papers/paper-3-anomaly-catalog/` | **COPY** (paper files only) |
| `pipelines/p2_chirality/` (paper files) | `papers/paper-4-chirality/` | **COPY** (paper files only) |
| `h200_scripts/experiments/` | `experiments/scripts/` | **COPY** |
| `pipelines/h200_results/` | `experiments/results/` | **COPY** |
| `pipelines/p1_highz_tracers/` | `pipelines/p1-highz-tracers/` | **COPY** |
| `pipelines/p2_chirality/` | `pipelines/p2-chirality/` | **COPY** |
| `pipelines/p3_anomaly_engine/` | `pipelines/p3-anomaly-engine/` | **COPY** |
| `reproducibility/cosmology/` | `data/chains/` | **COPY** |
| `data/` | `data/external/` | **COPY** |
| `public/images/` | `site/public/images/` | **COPY** |
| `public/papers/` | `site/public/papers/` | **COPY** |
| `project-context/` | `context/` | **COPY** |
| `wiki/` | `knowledge/` | **COPY** |
| `research/agents/` | `.hubify-labs/agents/` | **COPY** + adapt as Pi agent prompts |
| `*.html` (37 pages) | Reference only | **DO NOT COPY** — rewrite in Next.js |
| `style.css` | Reference only | **DO NOT COPY** — migrate to Tailwind |
| `CLAUDE.md` | `CLAUDE.md` | **COPY** + update for new structure |
| `.env.local` | `.env.local` | **COPY** |
| `research_queue.json` | `.hubify-labs/queue.json` | **COPY** |

### What Stays Untouched

| Asset | Location | Status |
|-------|----------|--------|
| Original BigBounce repo | `github.com/hubify-projects/bigbounce` | **NEVER MODIFIED** |
| Original BigBounce directory | `~/CODE_2025/bigbounce/` | **NEVER MODIFIED** |
| Live BigBounce website | `bigbounce.hubify.app` | **Continues deploying from original repo** |
| BigBounce CLAUDE.md | `~/CODE_2025/bigbounce/CLAUDE.md` | **NEVER MODIFIED** |
| BigBounce GitHub fork backup | `hubify-projects/bigbounce-archive-2026-04-07` | **Point-in-time safety copy** |
| Hubify GitHub fork backup | `hubify-projects/hubify-archive-2026-04-07` | **Point-in-time safety copy** |
| Local BigBounce backup | `~/CODE_2025/bigbounce-backup-20260407/` | **Local safety copy** |
| Local Hubify backup | `~/CODE_2025/hubify-backup-20260407/` | **Local safety copy** |

---

## 3. Agent Hierarchy — Full Specification

### 3.1 Global Orchestrator

**Process:** Long-lived Pi session at `~/.hubify-labs/`
**Model:** Claude Opus 4.6 (configurable)
**Session:** `~/.hubify-labs/sessions/global.jsonl` (rotated at 100K lines)

**Tools:**
| Tool | Description |
|------|-------------|
| `create_lab(name, domain, config)` | Initialize new Lab directory + Convex entry |
| `list_labs()` | List all Labs with status, costs, experiment counts |
| `delegate(lab_slug, message)` | Send message to Lab Orchestrator |
| `allocate_budget(lab_slug, daily, weekly)` | Set spending limits |
| `global_search(query)` | Search across all Labs (experiments, results, learnings) |
| `share_dataset(lab_from, lab_to, dataset_name)` | Cross-lab dataset sharing |
| `share_learning(learning_id)` | Propagate learning to all applicable Labs |

**Skills:** high-autonomy, budget-aware, never-accept-complete

**State (Convex):** `labs` table, `shared_*` tables, `cost_tracking`

### 3.2 Lab Orchestrator (one per Lab)

**Process:** Spawned by Global Orchestrator, persists via JSONL session
**Model:** Claude Opus 4.6 (configurable per lab)
**Session:** `{lab}/.hubify-labs/sessions/orchestrator.jsonl`

**Tools:**
| Tool | Description |
|------|-------------|
| `delegate(lead_role, message)` | Send task to a Lead agent |
| `tilldone_new(task_name, assign_to)` | Create tracked task |
| `tilldone_status()` | View all task progress |
| `manage_queue(action, experiment_id?)` | Add/remove/reorder queue |
| `ssh_pod(command)` | Execute command on GPU pod |
| `check_pod_status()` | GPU util, processes, disk |
| `read`, `write`, `edit`, `bash`, `grep` | Standard file tools |

**Skills:** houston-method, active-listener, zero-micro-management, budget-aware, never-accept-complete

**Domain (read+write):** Entire lab directory

### 3.3 Lead Agents (4 per Lab)

Each Lead is a **persistent Pi subprocess** (Opus or Sonnet, session survives across tasks).

#### Research Lead
**Model:** Sonnet 4.6 | **Domain:** `context/`, `knowledge/`, `experiments/scripts/`
**Tools:** delegate (to Literature, Computation, Pipeline agents), read, write, edit, bash
**Responsibility:** Hypothesize, design experiments, prioritize the queue
**Mental model tracks:** Which hypotheses tested, what worked, what domains explored, paper gaps

#### Analysis Lead
**Model:** Sonnet 4.6 | **Domain:** `experiments/results/`, `pipelines/`, `data/`
**Tools:** delegate (to Statistics, QC agents), read, write, edit, bash, grep
**Responsibility:** Analyze results, run QC gates, cross-match catalogs, compute statistics
**Mental model tracks:** QC failure patterns, cross-correlation results, statistical techniques that work

#### Writing Lead
**Model:** Sonnet 4.6 | **Domain:** `papers/`, `site/`, `knowledge/`
**Tools:** delegate (to Paper Writer, Figure Generator, Skeptic agents), read, write, edit, bash
**Responsibility:** Draft papers, generate figures, update website, maintain knowledge wiki
**Mental model tracks:** Paper status, which figures need updating, site pages out of date

#### Infrastructure Lead
**Model:** Sonnet 4.6 | **Domain:** `experiments/`, `.hubify-labs/`, `.env.local` (read)
**Tools:** delegate (to GPU Manager, Backup agents), ssh_pod, runpod_api, read, write, bash
**Responsibility:** Manage pods, deploy scripts, run backups, monitor costs
**Mental model tracks:** Pod history, cost patterns, backup status, which scripts deployed where

### 3.4 Worker Agents (11 per Lab)

Each Worker is **ephemeral** — spawned per-subtask, no persistent session. Uses cheapest model tier.

| Worker | Model | Tools | Domain | Does |
|--------|-------|-------|--------|------|
| Literature Agent | Haiku | read, web_search | read-only | Search NASA ADS, arXiv, Semantic Scholar |
| Computation Agent | Sonnet | read, write, bash | `experiments/scripts/` | Write Python experiment scripts |
| Pipeline Agent | Sonnet | read, write, bash | `pipelines/`, `data/external/` | Download, preprocess survey data |
| Statistics Agent | Sonnet | read, write, bash | `experiments/results/`, `data/` | Run MCMC, Fisher forecasts, cross-matches |
| QC Agent | Haiku | read, bash | `experiments/results/` (read-only) | Quality gates, validation checks |
| Paper Writer | Sonnet | read, write, edit | `papers/` | Draft LaTeX sections |
| Figure Generator | Sonnet | read, write, bash | `papers/*/figures/`, `site/public/` | Create matplotlib/plotly figures |
| Skeptic Agent | Sonnet | read | ALL (read-only) | Check for overclaiming, systematic errors |
| GPU Manager | Haiku | ssh_pod, runpod_api | `experiments/` | Pod lifecycle, script deployment |
| Backup Agent | Haiku | bash, scp | `experiments/results/` | SCP results, push to HuggingFace/B2 |
| Site Updater | Sonnet | read, write, edit | `site/` | Update Next.js pages with new results |

---

## 4. Cross-Lab Sharing Architecture

### 4.1 Shared Datasets

When a Lab produces a catalog (e.g., BigBounce's 195K DESI anomalies), it registers in Convex:

```
Lab A (BigBounce) produces catalog
  → Analysis Lead calls: shared_datasets.register({
      name: "desi-dr1-anomaly-catalog",
      type: "catalog",
      format: "parquet",
      location: "huggingface://bamfai/desi-spectral-anomaly-catalog",
      row_count: 195829,
      tags: ["anomaly", "spectroscopic", "desi", "astrophysics"]
    })
  → Any Lab can query: shared_datasets.search({tags: ["anomaly"]})
  → Lab B downloads and cross-matches with their own data
```

### 4.2 Shared Learnings

When an agent discovers something operationally useful:

```
Worker hits "np.trapz removed in numpy 2.4"
  → Agent calls: shared_learnings.log({
      category: "operational",
      key: "numpy-trapz-removed-2.4",
      insight: "Use np.trapezoid() instead of np.trapz() on numpy 2.4+",
      confidence: 10,
      applicable_to: ["all"]
    })
  → Propagated to all Labs via Global Orchestrator
  → Each Lab's agents see it in their mental model on next task
```

### 4.3 Shared Agent Templates

Reusable agent personalities:

```
BigBounce creates excellent "Skeptic Agent" prompt
  → Writing Lead registers: shared_agent_templates.create({
      name: "skeptic",
      role: "worker",
      prompt_content: "...",  // full .md
      domain: "general",
      description: "Checks for overclaiming, systematic errors, missed controls"
    })
  → New Lab can import: "Use the shared 'skeptic' template"
  → Customize for domain: add domain-specific checks
```

### 4.4 Shared Models

Trained neural networks:

```
BigBounce trains spectral autoencoder (47K params)
  → Registers: shared_datasets.register({
      name: "spectral-autoencoder-47k",
      type: "model",
      format: "pt",
      location: "huggingface://bamfai/desi-spectral-anomaly-detector",
      tags: ["autoencoder", "spectroscopy", "anomaly-detection"]
    })
  → New Lab doing spectroscopy can fine-tune from this checkpoint
```

### 4.5 Cross-Lab Discovery Correlation

Automated cross-referencing when any Lab finds anomalies:

```
Lab A finds anomaly at (RA=180.5, Dec=+22.3)
  → Logs to Convex with coordinates
  → Cron job: cross_lab_correlator runs every hour
    → Queries all Labs' anomaly catalogs within 10 arcsec
    → If match found in Lab B's data:
      → Activity stream: "CROSS-LAB MATCH: BigBounce anomaly matches eROSITA source"
      → Both Labs notified
      → Multi-survey detection = highest discovery confidence
```

---

## 5. GPU/Compute Pipeline — Full Specification

### 5.1 Experiment Lifecycle

```
1. DESIGN    → Research Lead proposes experiment
2. SCRIPT    → Computation Agent writes Python script
3. REVIEW    → Skeptic Agent checks for issues
4. QUEUE     → Added to .hubify-labs/queue.json
5. DEPLOY    → GPU Manager SCPs script to pod
6. RUN       → GPU Manager starts via nohup/tmux
7. MONITOR   → Infrastructure Lead polls every 5 min
8. COMPLETE  → Results appear in output dir
9. BACKUP    → Backup Agent SCPs results to local + pushes to HF/B2
10. QC       → QC Agent runs quality gates
11. ANALYZE  → Analysis Lead processes results
12. SYNC     → Site Updater adds to website + Writing Lead updates paper
13. EXPAND   → Research Lead proposes 5-15 follow-on experiments
14. LOG      → All activity logged to Convex activity_stream
```

This IS the Houston Method v2, encoded as agent workflow.

### 5.2 Queue Management

```json
// .hubify-labs/queue.json
{
  "version": 2,
  "lab": "bigbounce",
  "current_batch": "batch-6",
  "experiments": [
    {
      "id": "neowise-fullsky",
      "name": "NEOWISE full-sky via AWS S3 Parquet (170B rows)",
      "phase": 9,
      "script": "experiments/scripts/neowise_fullsky.py",
      "gpu_required": true,
      "estimated_hours": 48,
      "estimated_cost": 172,
      "status": "queued",
      "priority": 1,
      "dependencies": []
    }
  ],
  "completed": ["planck-cmb-masked", "fnl-bias-validation", "..."],
  "failed": ["superres-coord-fix"],
  "total_estimated_hours": 492,
  "total_estimated_cost": 1768
}
```

### 5.3 Pod Management

Infrastructure Lead manages pod lifecycle through these operations:

| Operation | Method | Safety Check |
|-----------|--------|--------------|
| Create pod | RunPod GraphQL `podFindAndDeployOnDemand` | Budget check |
| Check status | RunPod GraphQL `pod(podId)` | None |
| SSH command | `ssh -o ConnectTimeout=15 root@host -p port -i key "cmd"` | None |
| Deploy script | `scp -P port script root@host:/workspace/` | Script exists |
| Start experiment | SSH + `nohup python3 script > log 2>&1 &` | Pod running, GPU idle |
| Stop pod | RunPod GraphQL `podStop` | **BACKUP FIRST** |
| Terminate pod | **NEVER** without human approval | Alert + confirm |

### 5.4 Checkpoint Schema

```json
{
  "experiment_id": "planck-cmb-masked",
  "step": 3,
  "step_name": "inference_batch_15",
  "total_steps": 5,
  "state": {
    "batches_done": 15,
    "batches_total": 20,
    "anomalies_so_far": 142,
    "model_path": "/workspace/bigbounce/models/spectral_autoencoder.pt"
  },
  "output_files": ["batch_01.parquet", "batch_15.parquet"],
  "gpu_hours_so_far": 0.5,
  "cost_so_far": 1.80,
  "timestamp": "2026-04-07T03:15:00Z",
  "resumable": true
}
```

On pod crash: read checkpoint, skip completed batches, resume from step 3 batch 16.

### 5.5 QC Gate Specification

Every experiment MUST pass these automated checks (from queue_v2.py):

| Check | Threshold | Failure Action |
|-------|-----------|----------------|
| Null coordinates (RA=0, Dec=0) | > 5% of top anomalies | Mark QC_FAIL, add to re-run queue |
| Training quality (val_loss) | > 1000 | Mark QC_FAIL, needs more epochs |
| Cluster degeneracy | > 80% in one cluster | Mark QC_FAIL, tune HDBSCAN params |
| Score explosion | > 10^6 | Mark QC_FAIL, check normalization |
| Spatial concentration | All top 20 within 5 deg | Mark QC_FAIL, check for systematic |
| Empty output | 0 files | Mark QC_FAIL, check script |
| NaN/Inf values | Any in results | Mark QC_FAIL, check numerics |

---

## 6. Backup & Data Management

### 6.1 Multi-Location Protocol

Every artifact in 3+ locations. **Data loss is the only truly unrecoverable failure.**

| Data Type | Local | GitHub | HuggingFace | B2 | Convex |
|-----------|-------|--------|-------------|-----|--------|
| Code + configs | Primary | Mirror | - | - | - |
| MCMC chains | Cache | LFS | Dataset | Backup | Metadata |
| Anomaly catalogs | Cache | - | Dataset | Backup | Metadata |
| Trained models | Cache | - | Model | Backup | Metadata |
| Experiment results | Primary | - | - | Backup | Summary |
| Paper PDFs | Local | Repo | - | - | Metadata |
| Mental models | Cache | - | - | - | **Primary** |
| Activity stream | - | - | - | - | **Primary** |

### 6.2 Backup Schedule

| Trigger | Action |
|---------|--------|
| Experiment completes | SCP results to local, log to Convex |
| Batch completes | Push to HuggingFace + B2 |
| Paper compiled | Commit PDF to repo |
| Daily (midnight) | Full incremental backup to B2 |
| Before pod stop | MANDATORY backup check |
| Before pod terminate | **HUMAN APPROVAL REQUIRED** |

---

## 7. Website System — Next.js Specification

### 7.1 Architecture

Each Lab gets a Next.js app in `site/`. Standard template, customized per domain.

**Stack:**
- Next.js 15 (App Router)
- Tailwind CSS (academic aesthetic: Newsreader serif + Inter sans + JetBrains Mono)
- MathJax (equation rendering)
- Chart.js / Plotly (data visualization)
- Convex client (real-time data)

**Deployment:** Vercel from `site/` subdirectory. Each Lab has its own subdomain.

### 7.2 Standard Pages

| Page | Route | Data Source | Purpose |
|------|-------|-------------|---------|
| Homepage | `/` | Convex stats, key results | Research overview, stat cards, claims table |
| Papers | `/papers` | Convex papers table | Paper listing, PDF downloads, version history |
| Data Explorer | `/data` | Embedded datasets + Convex | Interactive tables, column stats, calculators |
| Activity | `/activity` | Convex activity_stream | Live research timeline feed |
| Figures | `/figures` | `public/images/` | Gallery with lightbox |
| Glossary | `/glossary` | Static + equations | Searchable terms + MathJax equations |
| Anomaly Explorer | `/anomalies` | Convex + parquet | Browse anomaly catalogs |
| Articles | `/articles` | MDX files | Deep-dive articles |

### 7.3 Site Generation Workflow

```
Writing Lead: "Update the website with Phase 4 results"
  → delegates to Site Updater agent
  → Site Updater reads experiment results from Convex
  → Updates relevant pages (homepage stat cards, activity feed, data explorer)
  → Commits changes to repo
  → Vercel auto-deploys
  → Logs: "Site updated with 3 new stat cards, 2 activity entries"
```

---

## 8. CLI/TUI Specification

### 8.1 Commands

```bash
hubify-labs                           # Launch Global Orchestrator (interactive TUI)
hubify-labs create <name> --domain <domain>  # Create new Lab
hubify-labs list                      # List all Labs with status
hubify-labs enter <lab-slug>          # Enter Lab context (Lab Orchestrator)
hubify-labs status                    # Dashboard view (costs, experiments, papers)
hubify-labs run <experiment>          # Queue and run experiment
hubify-labs queue                     # View/manage experiment queue
hubify-labs pod status                # Check GPU pod
hubify-labs pod ssh                   # SSH into pod
hubify-labs backup                    # Trigger backup
hubify-labs papers                    # List papers with status
hubify-labs site status               # Lab site overview + Lighthouse score
hubify-labs site deploy               # Trigger manual deploy
hubify-labs site preview              # Open preview URL in browser
hubify-labs site open                 # Open live site in browser
hubify-labs site sections             # List all sections + sync status
hubify-labs site logs                 # Recent site-worker activity
hubify-labs site edit                 # Start vibe-coding chat session (§53)
hubify-labs site template             # Show template.yaml config
hubify-labs share <dataset>           # Share dataset across Labs
hubify-labs learnings                 # View/search shared learnings
```

### 8.2 TUI Layout (Pi Nuclear UI)

```
┌─────────────────────────────────────────────────────────────────┐
│  HUBIFY LABS  ▸ 3 labs ▸ 1 active ▸ $12.40 today ▸ 1 pod       │
├─────────────────────────────┬───────────────────────────────────┤
│                             │  LAB: bigbounce                   │
│  CHAT                       │  ──────────────                   │
│  ─────                      │                                   │
│  houston > run the next     │  [H200] Phase 9  ████░░ 65%     │
│  batch of experiments       │  NEOWISE full-sky (48h est)       │
│                             │  Cost: $42.30 | GPU: 87%          │
│  orchestrator > Delegating  │                                   │
│  to Research Lead...        │  Papers: 4 (2 ready, 1@95%)      │
│                             │  Experiments: 53 complete          │
│  research-lead > Based on   │  Anomalies: 328K+                │
│  overnight results, I       │                                   │
│  recommend...               │  ── Recent ──                    │
│                             │  08:15 quintom MCMC complete     │
│  > _                        │  07:45 bias evolution done        │
│                             │  07:10 cross-correlation 4.1σ    │
├─────────────────────────────┴───────────────────────────────────┤
│  TASKS                                                          │
│  ○ Write Phase 9 scripts         ⚡ Research Lead               │
│  ● Deploy NEOWISE full-sky       ⚡ Infrastructure Lead          │
│  ✓ Back up overnight results     ◆ Backup Agent                 │
│  ✓ Update website stat cards     ◆ Site Updater                 │
└─────────────────────────────────────────────────────────────────┘
```

### 8.3 Key Interactions

| User Says | System Does |
|-----------|-------------|
| "run overnight" | Research Lead designs batch, Infra Lead deploys, queue auto-chains, 10-min cron monitors |
| "what happened last night" | Reads activity_stream, summarizes completed experiments + key results |
| "update the website" | site-worker auto-syncs changed sections, commits to site/ dir, triggers Vercel deploy (§53) |
| "change the hero section on the site" | Opens vibe-coding chat with site-worker agent, edits applied live in Vercel Sandbox preview |
| "write the paper" | Writing Lead delegates to Paper Writer for LaTeX, Figure Generator for plots |
| "how much have we spent" | Reads cost_tracking, shows daily/weekly/total per lab |
| "share the anomaly catalog with lab X" | Global Orchestrator registers in shared_datasets, notifies Lab X |

---

## 9. Fly.io Cloud Deployment

### 9.1 Architecture

The same CLI experience runs on Fly.io machines for always-on operation:

```
Local machine (Houston's Mac)
  ├── hubify-labs CLI (interactive TUI)
  └── ssh to Fly.io machine for always-on orchestrator

Fly.io machine (always-on)
  ├── Global Orchestrator (Pi process, persistent)
  ├── Lab Orchestrators (Pi subprocesses)
  └── Convex WebSocket (real-time state sync)

RunPod (GPU compute)
  ├── H200/A100 pods for experiments
  └── Results SCP'd to Fly.io machine or local

Convex (shared state)
  ├── All tables (source of truth)
  └── WebSocket to both local + Fly.io
```

### 9.2 Fly.io Machine Spec

```toml
# fly.toml
app = "hubify-labs-orchestrator"
primary_region = "lax"

[build]
  image = "node:20-slim"

[mounts]
  source = "labs_data"
  destination = "/data"

[[vm]]
  size = "shared-cpu-2x"
  memory = "4gb"
```

Cost: ~$15/month for always-on orchestrator + 4GB storage volume.

### 9.3 Local <> Cloud Sync

```
Local CLI ──WebSocket──> Convex <──WebSocket── Fly.io machine
                           ↑
                     Source of Truth
```

Both local and cloud read/write to Convex. JSONL sessions are local to each machine (not synced — they're conversation logs, not state). Mental models sync through Convex.

---

## 10. Failure Handling — Complete

| Failure | Detection | Recovery | Agent |
|---------|-----------|----------|-------|
| Pod dies mid-experiment | SSH timeout (3x30s) | Read checkpoint, resume from last step | GPU Manager |
| Pod billing expires | RunPod API "EXITED" status | Alert human, do NOT auto-create (costs money) | Infrastructure Lead |
| Agent hits context limit | Token count > 80% of limit | Summarize conversation, start new JSONL session with summary | Any agent |
| Experiment crashes | Non-zero exit code | Log error, mark QC_FAIL, add to re-run queue with error context | QC Agent |
| Budget exceeded (daily) | cost_tracking > threshold | Pause queue, alert human, keep pods running (don't terminate!) | Infrastructure Lead |
| Budget exceeded (weekly) | cost_tracking > threshold | Pause all Labs, alert human | Global Orchestrator |
| API key expired | Auth error from provider | Alert human, pause affected agents, continue others | Any agent |
| Backup fails | SCP/API error | Retry 3x with exponential backoff (5s, 30s, 300s), alert if all fail | Backup Agent |
| Convex unreachable | HTTP timeout | Continue with local-only state, queue Convex sync for when available | Any agent |
| JSONL session too large | File > 50MB | Rotate: summarize last 1000 messages, archive old file, start fresh | Any persistent agent |
| Concurrent mental model writes | Two agents update same model | Last-write-wins (Convex handles this natively) | Any agent |
| Cross-lab correlation false positive | Random match rate > observed rate | Flag as "needs verification", don't auto-report as discovery | Global Orchestrator |
| Paper overclaiming | Skeptic Agent flags issue | Block paper status from "ready" until resolved | Skeptic Agent |

**Iron rules:**
1. NEVER auto-terminate pods
2. NEVER delete data without backup verification
3. NEVER publish a paper without Skeptic review
4. NEVER exceed weekly budget without human approval

---

## 10.5 RunPod Safety Layer — ZERO DATA LOSS GUARANTEE

**This is the #1 operational priority.** Houston lost 130K galaxies once. NEVER AGAIN.

The RunPod Safety Layer wraps every RunPod operation with protection. It is NOT optional. It runs as a Convex cron + Infrastructure Lead behavior.

### 10.5.1 Credit Monitoring Cron

```typescript
// Convex cron: every 15 minutes
async function checkRunPodCredits() {
  // 1. Query RunPod API for account balance
  const balance = await runpodGraphQL(`{ myself { currentSpendPerHr creditBalance } }`);

  // 2. Calculate time until credits exhaust
  const hoursRemaining = balance.creditBalance / balance.currentSpendPerHr;
  const minutesRemaining = hoursRemaining * 60;

  // 3. Alert tiers
  if (minutesRemaining < 30) {
    // CRITICAL: Credits will exhaust in 30 min
    // → Trigger EMERGENCY FREEZE on all pods
    await emergencyFreeze("credits_critical", minutesRemaining);
  } else if (minutesRemaining < 120) {
    // WARNING: Credits will exhaust in 2 hours
    // → Alert human, prepare for freeze
    await logAlert("warning", `RunPod credits exhaust in ${Math.round(minutesRemaining)} min`);
  } else if (minutesRemaining < 480) {
    // INFO: Credits will exhaust in 8 hours
    // → Log for awareness
    await logAlert("info", `RunPod credits: $${balance.creditBalance} (~${Math.round(hoursRemaining)}h remaining)`);
  }

  // 4. Store balance in Convex for dashboard
  await ctx.db.insert("cost_tracking", {
    lab_id: null, // global
    date: new Date().toISOString().split('T')[0],
    runpod_balance: balance.creditBalance,
    spend_per_hr: balance.currentSpendPerHr,
    hours_remaining: hoursRemaining,
    checked_at: Date.now()
  });
}
```

**RunPod API endpoint for balance:** `query { myself { currentSpendPerHr creditBalance } }` — this is available on RunPod's GraphQL API.

### 10.5.2 Emergency Freeze Protocol

When credits are about to run out OR when triggered manually:

```
FREEZE SEQUENCE (automated, takes ~5 min):
═══════════════════════════════════════════

1. PAUSE QUEUE
   → Set all queues to status="paused"
   → No new experiments will start

2. CHECKPOINT ALL RUNNING EXPERIMENTS
   → SSH to each pod: send SIGUSR1 to running Python processes
   → Each experiment script handles SIGUSR1 by writing checkpoint JSON
   → Wait up to 60s for checkpoint files to appear
   → If no checkpoint handler: kill -SIGTERM (graceful), wait 30s, then -SIGKILL

3. BACKUP ALL POD DATA
   → For each pod:
     → SCP /workspace/bigbounce/outputs/ to local machine
     → SCP /workspace/bigbounce/checkpoints/ to local machine
     → SCP any .pt model files to local machine
     → Verify: count files transferred vs files on pod
     → Log backup manifest to Convex

4. STOP (NOT TERMINATE) ALL PODS
   → RunPod GraphQL: podStop(podId) for each pod
   → This preserves the container state (can resume later)
   → Costs stop immediately

5. LOG FREEZE EVENT
   → Activity stream: severity="critical", event="emergency_freeze"
   → Write to ~/.hubify-labs/alerts.log
   → Record freeze state in Convex: which experiments were running, checkpoint paths

6. DONE — No data lost, no money wasted, fully resumable
```

### 10.5.3 Resume Protocol

When credits are topped up or human says "resume":

```
RESUME SEQUENCE:
═══════════════

1. CHECK CREDITS
   → Verify balance > 8 hours of estimated run time
   → If not, alert and abort resume

2. START PODS
   → RunPod GraphQL: podResume(podId) for each frozen pod
   → Wait for SSH to become available (poll every 15s, max 5 min)
   → Verify GPU is accessible: nvidia-smi

3. VERIFY DATA INTEGRITY
   → SSH to pod: compare file list with freeze manifest
   → If files missing: SCP from local backup to pod
   → If checkpoint present: verify JSON is valid

4. RESUME EXPERIMENTS
   → For each frozen experiment:
     → Read checkpoint JSON
     → Start experiment with --resume-from <checkpoint>
     → Verify it's running (ps aux | grep python)

5. UNPAUSE QUEUE
   → Set queues back to status="running"
   → Next experiment in queue will start when current finishes

6. LOG RESUME EVENT
   → Activity stream: "Resumed from freeze. N experiments restarted from checkpoints."
```

### 10.5.4 Volume Enforcement

**All training outputs MUST go to persistent storage.** The Infrastructure Lead enforces this:

```python
# EVERY experiment script MUST have this at the top:
import os
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/workspace/bigbounce/outputs")
CHECKPOINT_DIR = os.environ.get("CHECKPOINT_DIR", "/workspace/bigbounce/checkpoints")

# Infrastructure Lead verifies before deploying any script:
# 1. Script writes to OUTPUT_DIR, not /tmp or /root or any ephemeral path
# 2. Script has checkpoint logic (writes JSON after each batch/epoch)
# 3. Script handles SIGUSR1 for emergency checkpoint
```

**Blocked paths** (domain-enforcer rejects writes here):
- `/tmp/` — ephemeral, lost on pod stop
- `/root/` — not on volume
- Any path outside `/workspace/` — not persistent

### 10.5.5 Idle Pod Protection

```
Cron: every 5 minutes
  → SSH to each running pod
  → Check GPU utilization: nvidia-smi --query-gpu=utilization.gpu
  → Check running processes: ps aux | grep python

  IF GPU == 0% AND no Python processes AND idle > 15 minutes:
    → Check queue: are there more experiments?
    → YES: Start next experiment immediately (GPU was idle unnecessarily)
    → NO: Start FREEZE protocol (stop pod to save money)
    → Log: "Pod {id} idle for {minutes}m. Action: {started_next | froze}"
```

### 10.5.6 Automatic Checkpoint Interval

Every experiment script MUST checkpoint at regular intervals:

```python
import signal, json, os, time

CHECKPOINT_DIR = os.environ.get("CHECKPOINT_DIR", "/workspace/bigbounce/checkpoints")
CHECKPOINT_INTERVAL = 300  # Every 5 minutes
_last_checkpoint = time.time()

def save_checkpoint(state, experiment_id):
    path = os.path.join(CHECKPOINT_DIR, f"{experiment_id}.json")
    with open(path, 'w') as f:
        json.dump({
            "experiment_id": experiment_id,
            "state": state,
            "timestamp": time.time(),
            "resumable": True
        }, f, indent=2)

# Handle emergency freeze signal
def _freeze_handler(signum, frame):
    save_checkpoint(current_state, experiment_id)
    print("CHECKPOINT SAVED (emergency freeze)")
    raise SystemExit(0)

signal.signal(signal.SIGUSR1, _freeze_handler)

# In main loop:
for batch in batches:
    process(batch)
    if time.time() - _last_checkpoint > CHECKPOINT_INTERVAL:
        save_checkpoint(current_state, experiment_id)
        _last_checkpoint = time.time()
```

### 10.5.7 New Convex Table: `runpod_state`

```typescript
runpod_state: defineTable({
  account_balance: v.number(),          // Current credit balance
  spend_per_hr: v.number(),             // Current spend rate
  hours_remaining: v.number(),          // Calculated
  freeze_status: v.string(),            // "normal"|"warning"|"frozen"|"resuming"
  frozen_at: v.optional(v.number()),
  frozen_reason: v.optional(v.string()),
  freeze_manifest: v.optional(v.any()), // {pods: [{id, experiments, checkpoints, backup_paths}]}
  last_checked: v.number(),
}).index("by_status", ["freeze_status"]),
```

---

## 10.6 Intelligent Token Limit Handling & Model Fallbacks

### 10.6.1 Detection

Every `delegate()` call tracks token usage. When an agent approaches its context limit:

```
Token usage after each response:
  current_tokens = response.tokens_in + response.tokens_out + session_tokens
  model_limit = MODEL_LIMITS[agent.model]  // e.g., 200K for Sonnet, 1M for Opus

  IF current_tokens > model_limit * 0.80:
    → WARNING: "Agent {name} at 80% context. Will rotate session soon."

  IF current_tokens > model_limit * 0.90:
    → ROTATE: Summarize session, start new JSONL, inject summary as system context

  IF API returns "context_length_exceeded" error:
    → FALLBACK: Try with a larger-context model (see fallback chain)
```

### 10.6.2 Session Rotation

When an agent hits 90% context:

```
1. Agent produces a summary of the current session:
   "Summarize the key decisions, findings, and open tasks from this session in <500 words"

2. Archive current JSONL: mv session.jsonl session_archived_TIMESTAMP.jsonl

3. Create new session with summary injected as system context:
   pi --session new_session.jsonl --system-prompt agent.md "SESSION CONTEXT: {summary}"

4. Agent continues with full awareness of prior work but fresh context window
```

### 10.6.3 Model Fallback Chain

If an agent's primary model fails (rate limit, outage, context overflow), fall through:

```yaml
# .hubify-labs/config.yaml
model_fallbacks:
  orchestrator:
    primary: anthropic/claude-opus-4-6      # 1M context
    fallback_1: anthropic/claude-sonnet-4-6  # 200K context
    fallback_2: openai/gpt-4o               # 128K context
    fallback_3: openrouter/auto              # OpenRouter picks best available

  leads:
    primary: anthropic/claude-sonnet-4-6
    fallback_1: anthropic/claude-haiku-4-5
    fallback_2: openai/gpt-4o-mini
    fallback_3: openrouter/auto

  workers:
    primary: anthropic/claude-haiku-4-5
    fallback_1: openai/gpt-4o-mini
    fallback_2: google/gemini-2.0-flash
    fallback_3: openrouter/auto
```

**Fallback logic:**
```
try:
  response = call_model(primary)
except RateLimitError:
  wait 30s, retry once
  if still fails: try fallback_1
except ContextLengthExceeded:
  rotate session (10.6.2), retry with primary
  if still fails: try fallback_1 (larger context)
except APIError (500, timeout):
  try fallback_1 immediately
except AuthError:
  alert human ("API key expired for {provider}")
  try next provider in chain

# If ALL fallbacks fail:
  log CRITICAL alert
  pause this agent's queue
  continue other agents that aren't affected
```

### 10.6.4 OpenRouter as Universal Fallback

OpenRouter (`openrouter.ai`) routes to 200+ models. When all direct API providers fail:

```
openrouter/auto — picks the best available model matching the request
  → Uses OPENROUTER_API_KEY from .env.local
  → OpenAI-compatible API: just change base_url
  → Automatic retries across providers
  → Cost may be higher than direct, but guarantees availability
```

### 10.6.5 Cost-Aware Model Selection

Not just fallback — proactively choose cheaper models when appropriate:

```
IF task is simple (< 500 tokens expected, no tools needed):
  → Use Haiku (cheapest)

IF task is code generation or analysis:
  → Use Sonnet (best code quality per dollar)

IF task is strategic planning or synthesis:
  → Use Opus (best reasoning)

IF running overnight autonomously:
  → Bias toward cheaper models (budget conservation)
  → Only escalate to Opus if Sonnet fails or produces low-quality output
```

---

## 10.7 Hubify Architecture Integration — What We Leverage

From the existing Hubify `ARCHITECTURE_DATAFLOW.md` (1,616 lines, 23 sections), these components map directly into Hubify Labs:

### 10.7.1 Squad Autonomy Pipeline (Section 11)

The 8-step cron pipeline in `squadAutonomy.ts` IS the research automation backbone:

| Hubify Cron | Hubify Labs Equivalent |
|-------------|----------------------|
| `runSquadStandups` (12h) | Lab Orchestrator morning planning |
| `orchestrateSquadWork` (6h) | Research Lead designs next experiments |
| `enrichSquadWork` (6h) | Literature Agent searches arXiv + Wolfram |
| `processSquadReviews` (4h) | Skeptic Agent + peer review |
| `publishSquadKnowledge` (daily) | Shared learnings propagation |
| `publishToGitHub` (after publish) | Commit results to repo |
| `crossSquadCollaboration` (daily) | Cross-lab discovery correlation |
| `generateSquadWebsite` (on-demand) | Site Updater deploys Next.js |

**Action:** Wire these crons to Hubify Labs agent hierarchy. Replace squad member roles with research agent roles.

### 10.7.2 GitHub Integration (Section 12)

Already built in Hubify:
- AgentMail → GitHub account → Hubify-Projects org
- Fork mode: direct commit to `Hubify-Projects/{repo}/main`
- Vercel auto-deploy on push
- Custom `.hubify.app` subdomains

**Action:** Each Lab repo lives in `Hubify-Projects/`. Writing Lead commits via GitHub API. Vercel deploys the Next.js site automatically.

### 10.7.3 Cross-Project Intelligence (Section 9)

Already built:
- `crossProjectIntelligence.ts` with `runCrossMatch` (5-arcsec spatial correlation)
- HTTP endpoints: `/api/lab/heartbeat`, `/api/lab/anomaly`, `/api/lab/status`
- `lab_projects` table with budget, compute tier, GitHub/Fly/RunPod links

**Action:** Each Hubify Labs Lab IS a `lab_project` in Convex. Cross-lab correlation uses existing `runCrossMatch`. HTTP heartbeat reports Lab health.

### 10.7.4 VPS Pipeline (Section 11.4)

Already built:
- `squadPipeline.triggerResearchCycle` — starts Python scripts on Fly machines
- HTTP reporting: `/api/pipeline/activity`, `/api/pipeline/paper-version`, `/api/pipeline/upload-media`
- Auto-start stopped machines before running scripts

**Action:** Adapt for RunPod pods in addition to Fly machines. Same reporting endpoints, different compute backend.

### 10.7.5 Workspace Alerts (Section 6.4)

Already built:
- `workspaceAlerts.ts` — per-hub alert rules
- Cron polls Fly machine health every 5 min

**Gap:** No notification delivery (email/Slack). **Action:** Add `~/.hubify-labs/alerts.log` for local monitoring + Convex activity_stream for dashboard.

### 10.7.6 Agent Autonomy Functions (Section 14)

11 autonomous behaviors defined, 5 are scheduled:
- Hub posting (8h)
- Knowledge validation
- Research advancement
- QA participation
- Knowledge voting

6 are NOT scheduled (in code but no cron):
- Collaboration requests
- Cross-pollination
- Propose missions
- Weekly digest
- Self-reflection
- Stale revival

**Action:** Schedule ALL 11 in Hubify Labs crons. Map to research agent behaviors:
- Hub posting → Research Lead publishes findings
- Knowledge validation → Skeptic Agent verifies claims
- Cross-pollination → Cross-lab learning propagation
- Self-reflection → Mental model updates
- Stale revival → Re-examine old experiments with new context

### 10.7.7 Hub Knowledge Lifecycle (Section 16)

State machine: `draft → proposed → verified → canonical` (with refuted/archived branches)

5 knowledge types: pattern, guide, signal, fragment, context

**Action:** Map to research knowledge:
- `pattern` → Methodology that works across experiments
- `guide` → Step-by-step for a pipeline
- `signal` → Scientific finding
- `fragment` → Partial result needing more evidence
- `context` → Background information for planning

### 10.7.8 Gap Audit (Section 20)

Hubify has these known gaps that Hubify Labs must address:

| Gap | Impact on Labs | Fix |
|-----|---------------|-----|
| No RunPod cost polling cron | Budget tracking stale | Add 15-min credit check cron (Section 10.5.1) |
| No RunPod auto-stop | Runaway costs | Add freeze protocol (Section 10.5.2) |
| Embedding generation not wired | Memory search is keyword-only | Wire OpenAI embedding API for mental model search |
| 6 unwired autonomy functions | Agents don't self-improve fully | Schedule all 11 in crons |
| VPS pipeline not in crons | Research automation is manual | Add cron trigger for experiment cycles |
| Website regeneration manual | Sites lag behind research | Wire `generateSquadWebsite` to experiment completion |

---

## 11. Cost Management

### 11.1 Cost Tracking

Every API call, every GPU minute, every storage byte is tracked:

```
LLM cost = sum(tokens_in * price_in + tokens_out * price_out) per agent
GPU cost = RunPod uptime_seconds * cost_per_hr / 3600
Storage cost = B2 stored_bytes * $0.005/GB/month + HuggingFace (free tier)
```

### 11.2 Budget Tiers

| Tier | Daily | Weekly | Monthly | Action on Breach |
|------|-------|--------|---------|------------------|
| Normal | $50 | $250 | $1000 | Continue |
| Warning | $75 | $375 | $1500 | Alert human, suggest optimizations |
| Hard limit | $100 | $500 | $2000 | Pause queue, alert human |

### 11.3 Cost Optimization

Infrastructure Lead proactively suggests:
- Spot instances when available (40-60% cheaper)
- Haiku for tasks that don't need Sonnet
- Batch experiments to minimize pod idle time
- CPU pods for CPU-bound work (ZTF light curves, pair counting)
- Terminate idle pods after 15 min of 0% GPU utilization

---

## 12. Implementation Plan — Week by Week

### Week 1: Foundation

**Acceptance test:** `hubify-labs` launches, creates a lab, delegates to a lead, gets a response.

| Day | Task |
|-----|------|
| Mon | Create safety forks (4 backups per Step 0). Create `hubify-labs/` repo. COPY Convex + CLI from hubify. |
| Tue | Set up Pi in hubify repo. Install lead-agents extension skeleton. Define config YAML. |
| Wed | Write 4 Lead agent prompts (Research, Analysis, Writing, Infrastructure). |
| Thu | Write 11 Worker agent prompts. Write 8 skill files (houston-method, etc). |
| Fri | Build Global Orchestrator: `create_lab`, `list_labs`, `delegate`. Test round-trip. |

### Week 2: BigBounce Lab Setup (COPY, not migrate — original untouched)

**Acceptance test:** One new experiment runs end-to-end inside the platform without human intervention.

| Day | Task |
|-----|------|
| Mon | COPY BigBounce files into `hubify-labs/labs/bigbounce/` per copy map. Verify original untouched. |
| Tue | New Convex schema (18 tables). Seed with BigBounce data (53 experiments, 4 papers, 15 surveys). |
| Wed | Infrastructure Lead manages H200: SSH, deploy script, start experiment. |
| Thu | Analysis Lead runs QC on completed experiment. Logs to Convex. |
| Fri | Full cycle: Research Lead proposes → Computation Agent writes script → Infra deploys → QC validates. |

### Week 3: Autonomous Operation

**Acceptance test:** Queue of 10+ experiments chains overnight. Morning shows results in Convex.

| Day | Task |
|-----|------|
| Mon | Experiment queue system. Infrastructure Lead monitors pod every 5 min via cron. |
| Tue | Auto-chain: when experiment completes, next in queue auto-starts. |
| Wed | Backup Agent: auto-SCP results on completion. Push to HuggingFace weekly. |
| Thu | Activity stream: all agent actions log to Convex. TUI renders live. |
| Fri | **Overnight test:** Queue 10 experiments, sleep, verify morning results. |

### Week 4: Learning + Website

**Acceptance test:** Mental models contain learnings from Week 3. Next.js site deploys with BigBounce data.

| Day | Task |
|-----|------|
| Mon | Mental model sync: agents read from Convex at task start, write back at end. |
| Tue | Research Lead's next proposal references previous results from mental model. |
| Wed | Next.js site template: homepage, papers, activity, data explorer. |
| Thu | Site Updater agent generates pages from Convex data. Deploy to Vercel. |
| Fri | Cross-lab sharing: shared_datasets, shared_learnings Convex tables. Propagation cron. |

### Week 5-6: Polish + Second Lab

| Task | Week |
|------|------|
| Cost tracking dashboard in TUI | 5 |
| Budget Guardian cron | 5 |
| Skeptic Agent review gate for papers | 5 |
| Fly.io deployment of always-on orchestrator | 5 |
| Second Lab (SDSS spectral survey or genomics) | 6 |
| Cross-lab discovery correlation cron | 6 |
| Knowledge wiki auto-update from experiment results | 6 |

### Week 7-8: Open Source Prep

| Task | Week |
|------|------|
| Documentation (README, contributing guide) | 7 |
| Clean up, code review, security audit | 7 |
| Open-source release on GitHub | 8 |
| Blog post / announcement | 8 |
| Submit BigBounce papers (the proof) | 8 |

---

## 13. Houston Method v2 — Encoded as Platform

The 9-step loop is NOT a document agents reference. It IS the experiment lifecycle:

| Step | Platform Implementation |
|------|------------------------|
| **RUN** | GPU Manager deploys + starts experiment |
| **QC GATE** | QC Agent runs 7 automated checks |
| **ANALYZE** | Analysis Lead processes results, Statistics Agent computes |
| **INTERPRET** | Research Lead connects to bounce cosmology predictions |
| **CONNECT** | Cross-lab correlator checks other Labs' data |
| **SYNC** | Site Updater updates website within 24h |
| **EXPAND** | Research Lead proposes 5-15 follow-on experiments |
| **BACKUP** | Backup Agent stores in 3+ locations |
| **COMPLETE** | Only when ALL steps pass. Logged to Convex with evidence. |

"Nothing is complete without all 9 steps" is enforced by the platform, not by willpower.

### 13.1 The "no future-research punts" rule (NEW · added 2026-04-08)

When any agent suggests deferring something to **"future research,"** **"out of scope,"** **"left to future work,"** **"this would take weeks/months,"** or **"this is beyond the current paper"** — the platform treats this as a SIGNAL to push deeper, not a reason to skip.

**Why this rule exists:**

Houston's experience with the 14 ECH structural barriers paper. The original AI agents told him the w = -1 dark energy thing was "future research on first-principles derivation." When he refused the punt and pushed for actual derivations, the result was:
- A 14-barriers map (a structured proof that ECH-specific bounce → dark energy routes are closed)
- Several novel theorems
- Surviving research threads that wouldn't have been found otherwise (f_NL = -35/8, quintom-B 2.3σ preference, ALP β = 0.27°, NANOGrav consistency)

None of those exist if Houston had accepted the original "future research" punt. The 14-barriers paper is now Paper 1 v2.2.1.

**Why agents punt:** they don't see how to attack a problem in their current context window. They estimate "weeks/months" because they're projecting their own slow human-style approach. In practice, with the right tools and re-framing, "weeks/months" tasks usually take **hours to days**. The estimate inflation is a bug, not a feature.

**How the platform enforces this:**

1. **Detection (always-on):** Every agent message that contains the trigger phrases is automatically flagged by the orchestrator. Trigger phrases (regex):
   - `future\s+research`
   - `out\s+of\s+scope`
   - `left\s+to\s+future`
   - `(weeks|months|years)\s+(of\s+work|to\s+(do|complete|implement))`
   - `beyond\s+(the\s+)?(current\s+(paper|project|scope))`
   - `outside\s+the\s+scope`
   - `we\s+(don't|do\s+not)\s+(have|address)\s+\w+\s+here`

2. **Response (orchestrator-level):** When a trigger fires, the orchestrator MUST stop and ask the punting agent: *"What would it take to actually do this now? Give me a concrete plan with hours-not-months estimates."*

3. **Re-estimate:** The agent must produce a real plan. If the plan is genuinely big (e.g. >40 hours, >$1K compute), it stays a punt — but now it's a documented punt with a real estimate. If the plan is actually small, the orchestrator pushes for it to happen NOW, in this session.

4. **Default answer is GO:** When in doubt, push forward. Punts have to be earned with specific quantitative justification, not vibes.

5. **Publish-ready loop Round 3 enforcement:** Round 3 of the publish-ready loop (§37.4) explicitly scans the paper for these phrases. Every match is a `houston_method_violation` issue that must be resolved before the paper can advance to Round 4.

**Legitimate punts:** Sometimes a punt IS legitimate. Examples:
- "The full 4D simulation would require 10 GPU-years on current hardware" (specific, quantitative, unavoidable)
- "We would need a new survey instrument that doesn't exist yet" (physical constraint)
- "This requires data that won't be released until 2028" (calendar constraint)

The rule is **"no vague punts," not "no punts ever."** Punts must be specific, quantitative, and accompanied by a real reason (not "this would take a while"). The orchestrator's job is to distinguish vague punts (push back) from real punts (accept and document).

**Cultural rule for the agents:** be skeptical AND ambitious. Skeptical = don't accept your own first-pass estimates. Ambitious = if you don't see how to do it, find someone (another agent, another model) who might.

This rule is now part of every agent's `soul.md` template.

---

## 14. Key Technical Primitives

### `delegate(target, message)`
From lead-agents `lead-delegate.ts`. Spawns or resumes a child Pi subprocess:
```typescript
const child = spawn("pi", [
  "--session", sessionPath,
  "--system-prompt", promptPath,
  "--model", model,
  message
]);
// Streams response via JSON events on stdout
// Parent blocks until child completes or times out (default 5 min)
// Returns: {response: string, tokens_in: number, tokens_out: number, cost_usd: number}
```

### `onUpdate(callback)`
Pi extension hook. Child process emits `{type: "text_delta", delta: "..."}` events. Parent renders them in TUI real-time.

### `tilldone`
From lead-agents `tilldone-lead.ts`. Shared task list:
- `tilldone new-list "Overnight batch"` — create list
- `tilldone add "Run NEOWISE full-sky" --assign "Infrastructure Lead"` — add task
- `tilldone start 3` — mark in-progress
- `tilldone done 3` — mark complete
- Stored as JSON, rendered in TUI footer.

### `ssh_pod(command)`
Custom Pi tool for GPU management:
```typescript
// Wraps: ssh -o ConnectTimeout=15 -o StrictHostKeyChecking=no root@host -p port -i key "command"
// Returns: {stdout: string, stderr: string, exit_code: number}
// Timeout: 30s default, configurable
// Retries: 3x with 5s backoff on timeout
```

### `runpod_api(query)`
Custom Pi tool wrapping RunPod GraphQL:
```typescript
// Wraps: curl -s -X POST "https://api.runpod.io/graphql" -H "Authorization: Bearer $KEY" -d query
// Returns: parsed JSON response
// Used for: pod status, create, stop, resume
```

---

## 15. Security & Secrets

| Secret | Storage | Access |
|--------|---------|--------|
| ANTHROPIC_API_KEY | `.env.local` per lab | All agents via Pi env |
| RUNPOD_API_KEY | `.env.local` per lab | Infrastructure Lead only |
| SSH private key | `~/.ssh/id_ed25519` | GPU Manager only |
| HUGGINGFACE_TOKEN | `.env.local` per lab | Backup Agent only |
| CONVEX_DEPLOY_KEY | `.env.local` per lab | All agents (state sync) |
| B2_APP_KEY | `.env.local` per lab | Backup Agent only |
| FLY_API_TOKEN | `~/.env.local` global | Global Orchestrator only |

**Rules:**
- `.env.local` is ALWAYS gitignored
- No secrets in Convex (it's for state, not secrets)
- No secrets in mental models, activity streams, or shared learnings
- Agent prompts never include secrets — they reference env var names

---

## 16. Monitoring & Observability

### 16.1 TUI Dashboard (always visible)

```
Top bar: lab count, active count, daily cost, pod count
Right panel: current lab status (experiment progress, papers, anomaly count)
Bottom panel: task list with agent assignments
Chat panel: human <> orchestrator conversation
```

### 16.2 Activity Stream (Convex, real-time)

Every agent action is logged:
```json
{"event": "experiment_started", "severity": "info", "message": "Starting planck-cmb-masked on H200", "agent": "GPU Manager"}
{"event": "qc_passed", "severity": "success", "message": "planck-cmb-masked: 7/7 QC checks passed", "agent": "QC Agent"}
{"event": "ALERT", "severity": "critical", "message": "Pod SSH timeout after 3 retries", "agent": "Infrastructure Lead"}
```

### 16.3 Alerting

| Severity | TUI Display | Log File | Human Action |
|----------|-------------|----------|-------------|
| info | Gray text | Yes | None |
| success | Green text | Yes | None |
| warning | Yellow text | Yes | Review when convenient |
| error | Red text | Yes | Investigate |
| critical | Red blinking + bell | Yes + `~/.hubify-labs/alerts.log` | Immediate |

### 16.4 Overnight Monitoring

When human is away:
- 10-min cron checks pod status, GPU utilization, experiment progress
- If GPU idle > 15 min, auto-deploys next queued experiment
- If pod unreachable > 30 min, logs ALERT
- If daily budget > 80%, logs warning
- All activity logged to Convex for morning review
- `alerts.log` captures critical issues

---

---

## 17. Autonomous Website Generation Pipeline

Each Lab gets an auto-generated research website deployed to `{slug}.hubify.app`. This uses Hubify's existing `missionWebsites.ts` pipeline.

### 17.1 How It Works

```
Trigger: experiment batch completes OR Writing Lead invokes
  → missionWebsites.generateMultiPageMissionWebsite(lab_id)
  → Fetch all data from Convex: experiments, results, papers, activity, surveys
  → Build deterministic theme (per-lab colors, fonts, animation style)
  → Push style.css to Hubify-Projects/{slug} on GitHub (auto-creates repo if 404)
  → Claude Sonnet generates index.html body
  → Push index.html to GitHub
  → Create Vercel project + assign {slug}.hubify.app domain
  → Schedule 5 remaining pages as separate Convex actions:
    findings.html, paper.html, versions.html, team.html, sources.html
  → Each page: 1 Claude call + 1 GitHub push → Vercel auto-deploys
  → Store site metadata in Convex hub_knowledge
```

### 17.2 Standard 6 Pages Per Lab

| Page | Content | Data Source |
|------|---------|-------------|
| `index.html` | Overview dashboard, stat cards, key results | Convex: experiments, surveys, papers |
| `findings.html` | Research timeline, charts, discovery log | Convex: activity_stream, experiments |
| `paper.html` | arXiv-style with MathJax equations | papers/ directory, references.bib |
| `versions.html` | Git-style commit timeline | git log + Convex: experiment history |
| `team.html` | Agent profiles, LLM transparency | Convex: agents table |
| `sources.html` | Bibliography, methodology, data sources | knowledge/ directory, context/ |

### 17.3 Per-Lab Visual Themes

```yaml
themes:
  bigbounce:
    accent: "#f59e0b"     # amber
    animation: "orbital-physics"
    font: "Newsreader"    # serif, academic

  sdss-scan:
    accent: "#3b82f6"     # blue
    animation: "spectral-lines"
    font: "Inter"

  hubify-labs:
    accent: "#22c55e"     # green
    animation: "matrix-rain"
    font: "JetBrains Mono" # monospace, terminal
```

### 17.4 Regeneration Cron

**Gap in current Hubify:** `regenerateAllMultiPageWebsites` is NOT scheduled.

**Fix in Labs:** Add to cron schedule:
```
regenerateLabWebsites: daily at 06:00 UTC
  → Scan all Labs with new activity since last generation
  → For each: regenerate affected pages only (not all 6)
  → Incremental: only push pages where underlying data changed
```

### 17.5 Next.js Migration Path

The auto-generated HTML sites (via Claude Sonnet) are the **bootstrap**. As Labs mature, they migrate to full Next.js:

```
Phase 1 (MVP): Claude-generated HTML → GitHub → Vercel auto-deploy
  → Quick, works today, uses existing missionWebsites.ts
  → 6 static pages, good enough for initial showcase

Phase 2 (Month 2): Next.js template → GitHub → Vercel
  → Standard Next.js app in lab's site/ directory
  → Dynamic data from Convex client
  → Richer interactivity (data explorer, anomaly browser)
  → Site Updater agent edits React components, not raw HTML

Phase 3 (Month 3): Full dynamic site
  → Real-time Convex subscriptions
  → Live experiment progress on the page
  → Embedded paper viewer with MathJax
  → Interactive data visualization (Plotly/D3)
```

---

## 18. Complete Cron Schedule for Hubify Labs

Every automated behavior in one table:

| Cron | Interval | Component | Purpose |
|------|----------|-----------|---------|
| `checkRunPodCredits` | 15 min | RunPod Safety | Monitor balance, trigger freeze if < 30 min |
| `checkPodIdleStatus` | 5 min | RunPod Safety | Detect idle GPU, auto-start next experiment or freeze |
| `pollPodCosts` | 15 min | Cost Tracking | Record GPU spend per lab in Convex |
| `monitorExperimentProgress` | 5 min | Infrastructure Lead | SSH check running experiments, detect completion/failure |
| `backupCompletedResults` | On experiment complete | Backup Agent | SCP results to local, verify integrity |
| `rotateAgentSessions` | 1 hour | Session Management | Check JSONL sizes, rotate if > 50MB |
| `propagateSharedLearnings` | 6 hours | Cross-Lab | Push new learnings to all applicable Labs |
| `crossLabCorrelation` | 1 hour | Cross-Lab | runCrossMatch on new anomalies across Labs |
| `updateMentalModels` | After each task | Per-Agent | Sync mental model YAML ↔ Convex |
| `regenerateLabWebsites` | Daily 06:00 | Website | Regenerate pages with new data |
| `publishToGitHub` | After website regen | GitHub | Push updated pages to Hubify-Projects |
| `runSquadStandups` | 12 hours | Autonomy | Lab Orchestrator morning planning |
| `orchestrateSquadWork` | 6 hours | Autonomy | Research Lead designs next experiments |
| `enrichSquadWork` | 6 hours | Autonomy | Literature Agent arXiv + Wolfram search |
| `processSquadReviews` | 4 hours | Autonomy | Skeptic Agent peer review |
| `publishSquadKnowledge` | Daily 07:30 | Knowledge | Shared learnings propagation |
| `crossSquadCollaboration` | Daily 09:00 | Cross-Lab | Cross-lab agent collaboration |
| `agentProfileReflection` | Weekly | Self-Improvement | Agents self-assess, update prompts |
| `knowledgeCrossPollination` | 8 hours | Knowledge | Hub-to-hub knowledge transfer |
| `staleContentRevival` | Weekly | Knowledge | Re-examine old experiments with new context |
| `weeklyDigest` | Monday 09:00 | Reporting | Automated intelligence summary for human |
| `costDailyRollup` | Daily midnight | Cost Tracking | Aggregate daily costs per lab |

---

## 20. Memory Architecture — Four-Layer System

**This is the foundation everything else sits on.** Houston has been frustrated by agent memory failures: the main BigBounce agent has forgotten what's been run, what's planned next, and has failed to be proactive about idle GPU utilization despite repeated instructions. The memory system MUST be sophisticated and damn near perfect. Houston explicitly asked for this to be built in-house — no Supermemory, no third-party memory SaaS.

**STATUS UPDATED 2026-04-08:** Build memory FROM SCRATCH. Do NOT depend on or extend the existing `~/CODE_2025/youmd/` repo or `~/CODE_2025/hubify/convex/agentMemory.ts` schema — both are WIP and not gold standard. The Hubify Labs memory system is built fresh on `@convex-dev/agent` as the primitive, using patterns borrowed from mem0, Letta, Graphiti, cognee, and Claude Code's own file-based memory model. **`youmd` integration is COMING SOON in Phase 2** — there will be a "USER.md / youmd integration" tile in Settings marked "coming soon" so the WIP work doesn't muddy the MVP. Full pattern study lives in `bigbounce/project-context/memory_systems_survey.md` (1,016 lines).

### 20.1 Why a Four-Layer System

Memory failures fall into four categories, and a single memory store can't solve all of them well:

1. **User memory failures** — Houston states a preference, the agent forgets it next session, Houston has to repeat himself. **Solution:** Per-user persistent memory with verbatim message log + AI summaries + tags + search.
2. **Agent memory failures** — A subagent learns something operationally important (a numpy version bug, a pod reboot trick, a paper compilation gotcha), the next agent makes the same mistake. **Solution:** Per-agent long-term memory shared across sessions and inherited by subagents.
3. **Lab memory failures** — The main lab agent forgets what's currently running, what's been finished, what's in the queue, what's blocked. **Solution:** Per-lab episodic memory of every experiment, decision, finding, and state change.
4. **Cross-lab memory failures** — Houston starts a new lab (e.g., quantum gravitational waves) and the agents don't surface relevant knowledge from BigBounce (datasets, learnings, models, insights). **Solution:** Global knowledge graph queryable by tag, topic, and vector similarity.

The four layers compose: when an agent starts a task, it loads the relevant slice of all four into its context. When it finishes, it writes back to the appropriate layers.

### 20.2 Layer 1 — User Memory (the USER directory)

**Storage location:** Convex DB + filesystem mirror at `~/.hubify/users/<user_handle>/`

**What it contains:**
- **Verbatim prompts:** Every message Houston has ever sent to any agent on the platform, saved exactly as typed.
- **AI summaries:** A 1-2 sentence summary of what each prompt was about, generated by a small fast model (Haiku 4.5) at ingestion time.
- **Key insights:** When a prompt contains a stated preference, rule, or important fact, the system extracts it as a separate memory record.
- **Timestamps:** ISO 8601 with timezone, plus a relative-time string for human display.
- **Tags:** Auto-generated topical tags ("compute", "design", "papers", "memory", "h200", etc.) plus manual tags Houston can add.
- **Source context:** Which lab, which agent, which session the message was sent in.
- **Status:** New / acknowledged / actioned / superseded.

**Convex schema:**
```typescript
// convex/schema.ts
user_messages: defineTable({
  user_id: v.string(),                    // "houston"
  message_id: v.string(),                 // unique per message
  text_verbatim: v.string(),              // exact user message
  ai_summary: v.string(),                 // 1-2 sentence summary
  key_insights: v.array(v.object({        // extracted preferences/rules/facts
    insight_type: v.union(
      v.literal("preference"),
      v.literal("rule"),
      v.literal("fact"),
      v.literal("idea"),
      v.literal("complaint"),
      v.literal("praise"),
    ),
    text: v.string(),
    confidence: v.number(),               // 0-1
    extracted_by: v.string(),             // model name
  })),
  tags: v.array(v.string()),              // auto + manual
  manual_tags: v.array(v.string()),       // user-added only
  timestamp: v.string(),                  // ISO 8601
  lab_id: v.optional(v.string()),         // which lab
  session_id: v.string(),                 // chat session
  agent_id: v.string(),                   // which agent received it
  status: v.string(),                     // new/ack/actioned/superseded
  embedding: v.optional(v.array(v.number())),  // 1536-dim for vector search
  superseded_by: v.optional(v.string()),  // link to newer message that updated this
}).index("by_user", ["user_id"])
  .index("by_user_time", ["user_id", "timestamp"])
  .index("by_user_tag", ["user_id", "tags"])
  .vectorIndex("by_embedding", { vectorField: "embedding", dimensions: 1536 }),

user_preferences: defineTable({
  user_id: v.string(),
  category: v.string(),                   // "compute", "design", "writing", "workflow"
  key: v.string(),                        // "prefer_modal_h200", "single_accent_color"
  value: v.string(),                      // the actual preference
  source_message_id: v.string(),          // which user message this came from
  confirmed_at: v.string(),               // when Houston confirmed it
  superseded_at: v.optional(v.string()),  // if changed
  active: v.boolean(),
}).index("by_user_category", ["user_id", "category"])
  .index("by_user_key", ["user_id", "key"]),
```

**Filesystem mirror** (for grep, version control, human readability):
```
~/.hubify/users/houston/
├── MEMORY.md                       # index of all memories with summaries
├── prompts/
│   ├── 2026-04-07.jsonl            # one line per message that day
│   ├── 2026-04-06.jsonl
│   └── ...
├── insights/
│   ├── compute_dual_provider.md    # extracted insight, 1 file each
│   ├── memory_system_bulletproof.md
│   ├── idle_gpu_proactive.md
│   ├── single_accent_color.md
│   └── ...
├── preferences.yaml                # current active preferences (Convex mirror)
└── tags/
    ├── compute.md                  # all messages tagged "compute"
    ├── design.md
    └── ...
```

**Write protocol:** Every user message that arrives at any agent in the platform triggers the user-memory writer:
1. Write verbatim to today's `prompts/YYYY-MM-DD.jsonl`
2. Call Haiku 4.5 to generate `ai_summary` and extract `key_insights`
3. Auto-tag based on content (model classifies into known tag set + creates new tags if needed)
4. Generate embedding (OpenAI `text-embedding-3-small`, 1536 dim)
5. Insert into Convex `user_messages`
6. For each extracted insight, insert/update Convex `user_preferences`
7. If an insight contradicts an active preference, mark old as superseded and notify
8. Append a one-line entry to `MEMORY.md` index

**Read protocol:** When an agent starts a task involving Houston:
1. Load `user_preferences` where `active=true` (full set, ~50 entries)
2. Vector-search recent `user_messages` for similar to current task description (top 10)
3. Keyword-search `user_messages` for entities mentioned in the task (top 10)
4. Inject all into agent's system prompt under `## User context` heading
5. Agent MUST acknowledge any preferences that apply to the current task in its response

**The "never repeat yourself" guarantee:** Before an agent asks Houston anything, it MUST search user memory for prior answers to the same question. If found, use the prior answer and notify "Using your prior preference: X". If not found, ask. The platform tracks "repeated questions" as a quality metric — agents that repeat questions get flagged for prompt improvement.

**Search UI:** Houston gets a memory inspector at `hubify.app/memory` (and via the desktop app sidebar) where he can:
- Search his entire prompt history by keyword, tag, lab, date range
- Browse extracted preferences and toggle them active/inactive
- Manually tag/retag messages
- See "what does the platform think I prefer about X" for any topic
- Override or delete a memory if it was extracted wrong

### 20.3 Layer 2 — Agent Memory (per-agent persistent state)

**Storage location:** Convex DB at `agents.<agent_id>.memory`

**What it contains:**
- **Identity:** The agent's name, role, model, system prompt version, creation date.
- **Working memory:** Current task, current step, current plan. Reset per task but logged.
- **Episodic memory:** Every task this agent has ever completed, with: input, output, tools used, duration, success/failure, what it learned.
- **Operational learnings:** Bug workarounds, command quirks, version gotchas, env-setup tricks. Searchable, high signal.
- **Inheritance graph:** Which agent spawned this agent, what context was inherited, what was new.
- **Tool calibration:** Per-tool success rate, common failures, recommended retry patterns.

**Convex schema:**
```typescript
agents: defineTable({
  agent_id: v.string(),                   // "anomaly-worker-3"
  parent_id: v.optional(v.string()),      // who spawned this
  role: v.string(),                       // "worker"
  domain: v.string(),                     // "anomaly_detection"
  lead: v.string(),                       // "anomaly-lead"
  model: v.string(),                      // "claude-haiku-4-5"
  system_prompt_hash: v.string(),         // version control on prompt
  created_at: v.string(),
  status: v.string(),                     // active/dormant/retired
}),

agent_episodes: defineTable({
  agent_id: v.string(),
  episode_id: v.string(),
  task_description: v.string(),
  task_input: v.any(),
  task_output: v.any(),
  tools_used: v.array(v.string()),
  duration_ms: v.number(),
  outcome: v.string(),                    // success/failure/partial/escalated
  learnings: v.array(v.object({
    text: v.string(),
    type: v.string(),                     // operational/scientific/process
    confidence: v.number(),
  })),
  started_at: v.string(),
  ended_at: v.string(),
  embedding: v.optional(v.array(v.number())),
}).index("by_agent_time", ["agent_id", "started_at"])
  .vectorIndex("by_embedding", { vectorField: "embedding", dimensions: 1536 }),

agent_learnings: defineTable({
  agent_id: v.string(),                   // null = global
  text: v.string(),
  type: v.string(),                       // operational/scientific/process/tool
  category: v.string(),                   // "numpy" / "runpod" / "latex" / etc.
  confidence: v.number(),                 // 0-10
  source_episode_id: v.string(),
  applicable_to: v.array(v.string()),     // ["anomaly_detection"] or ["all"]
  verified: v.boolean(),                  // confirmed by skeptic agent
  use_count: v.number(),                  // how often this learning has been applied
  last_used_at: v.optional(v.string()),
}).index("by_agent", ["agent_id"])
  .index("by_category", ["category"]),
```

**Write protocol:** When an agent finishes a task:
1. Log episode to `agent_episodes` with full input/output
2. If agent reflected on learnings during the task, add to `agent_learnings`
3. Generate embeddings for the episode for future retrieval
4. If learnings are tagged "global", elevate to global memory layer
5. Increment `use_count` on any learnings the agent applied during this task

**Read protocol:** When an agent receives a new task:
1. Load own identity + active learnings (~20-50 entries)
2. Vector-search own episodic memory for similar tasks (top 5)
3. Vector-search lead's learnings for similar tasks (top 5)
4. Vector-search global learnings for the task domain (top 10)
5. Inject into system prompt under `## Memory` heading

**Subagent inheritance:** When a parent agent spawns a subagent:
1. Subagent inherits parent's currently-loaded memory context (top relevant entries)
2. Subagent's own episodes are tagged with parent's `episode_id`
3. On subagent return, parent receives subagent's learnings as candidate additions to its own memory
4. Subagent retains its own memory across sessions (it's a real agent with identity, not a throwaway)

### 20.4 Layer 3 — Lab Memory (per-lab episodic + structural)

**Storage location:** Convex DB + filesystem mirror at `<lab>/.hubify-labs/memory/`

**What it contains:**
- **Lab state:** Current focus, active research directions, blocked items, key results, open questions.
- **Experiment ledger:** Every experiment ever run in this lab. Status, cost, runtime, outcome, what was learned.
- **Decision log:** Every meaningful decision made in this lab. Why, by whom, what alternatives were considered.
- **Knowledge wiki:** The Karpathy-style structured knowledge base (entities, concepts, sources, comparisons) — already in BigBounce as `wiki/`.
- **Active queue:** What's currently running, what's queued, what's planned, what's blocked.
- **Idea backlog:** Every idea ever proposed for this lab. Viability score. Status (parked / queued / active / done / killed).
- **Cross-references:** Links to user messages, agent learnings, and global knowledge that relate to this lab.

**Convex schema (extends existing schema):**
```typescript
lab_state: defineTable({
  lab_id: v.string(),                     // "bigbounce"
  current_focus: v.string(),              // "Phase 4 f_NL science"
  active_directions: v.array(v.string()),
  blocked: v.array(v.object({
    item: v.string(),
    blocked_by: v.string(),
    blocked_at: v.string(),
  })),
  open_questions: v.array(v.string()),
  last_updated: v.string(),
  updated_by: v.string(),                 // which agent
}),

lab_decisions: defineTable({
  lab_id: v.string(),
  decision_id: v.string(),
  title: v.string(),
  context: v.string(),                    // what led to this
  decision: v.string(),                   // what was chosen
  alternatives: v.array(v.string()),      // what was rejected and why
  decided_by: v.string(),                 // human or agent
  decided_at: v.string(),
  reversal_of: v.optional(v.string()),    // if this overturns a prior decision
  superseded_by: v.optional(v.string()),
}).index("by_lab_time", ["lab_id", "decided_at"]),

// experiments table already exists per §5.1 — extend with:
//   learnings: v.array(v.string()),  // what was learned
//   embedding: v.array(v.number()),  // for retrieval
```

**Filesystem mirror:**
```
bigbounce/.hubify-labs/memory/
├── STATE.md                        # current state (auto-updated every experiment)
├── DECISIONS.md                    # decision log (append-only)
├── EXPERIMENTS.jsonl               # one line per experiment
├── BLOCKED.md                      # current blockers
├── QUESTIONS.md                    # open questions
└── snapshots/
    ├── 2026-04-07_morning.md       # human-readable lab state snapshot
    └── ...
```

**Write protocol:** Triggered by orchestrator after every meaningful event:
- Experiment finishes → log to `EXPERIMENTS.jsonl` + update `STATE.md`
- Decision made → append to `DECISIONS.md` + Convex
- Blocker hit → append to `BLOCKED.md` + Convex
- Question raised → append to `QUESTIONS.md` + Convex
- Daily 6 AM cron → write a snapshot to `snapshots/`

**Read protocol:** Every agent in the lab loads `STATE.md` + relevant decisions on every task. Subagents inherit. The main lab agent loads everything on startup.

**The "main agent never forgets" guarantee:** When the main lab agent starts a session, the FIRST thing it does is:
1. Read `STATE.md` (current focus, active directions)
2. Read last 10 entries from `EXPERIMENTS.jsonl`
3. Read `BLOCKED.md` and `QUESTIONS.md`
4. Read the lab's pinned `DECISIONS.md` entries
5. Synthesize a 1-paragraph "where we are" briefing and present it to Houston

This briefing is the FIRST thing in every session. If it's missing or wrong, the memory system has a bug.

### 20.5 Layer 4 — Global Memory (cross-lab knowledge graph)

**Storage location:** Convex DB tables `shared_*` (already exist per §4) + new `global_knowledge` table

**What it contains:**
- **Shared datasets** (already in §4.1)
- **Shared learnings** (already in §4.2)
- **Shared agent templates** (already in §4.3)
- **Shared models** (already in §4.4)
- **Cross-lab discovery correlations** (already in §4.5)
- **NEW: Global knowledge graph** — entities, concepts, sources from any lab's wiki, with cross-lab links

**Convex schema (new, extends §4):**
```typescript
global_knowledge: defineTable({
  knowledge_id: v.string(),
  type: v.union(
    v.literal("entity"),                  // a thing (galaxy, parameter, model)
    v.literal("concept"),                 // an idea or method
    v.literal("source"),                  // a paper or dataset
    v.literal("comparison"),              // a structured comparison table
    v.literal("insight"),                 // a learned fact
  ),
  name: v.string(),
  description: v.string(),
  source_lab: v.string(),                 // which lab created it
  related_labs: v.array(v.string()),      // labs that have referenced or extended it
  tags: v.array(v.string()),
  domain: v.array(v.string()),            // ["cosmology"] or ["cosmology", "particle"]
  visibility: v.union(
    v.literal("private"),                 // only source lab
    v.literal("shared"),                  // queryable by all labs
    v.literal("public"),                  // visible on hubify.app public pages
  ),
  contributed_to_global: v.boolean(),     // user toggled "share with all hubify users"
  created_at: v.string(),
  updated_at: v.string(),
  embedding: v.array(v.number()),
}).index("by_type", ["type"])
  .index("by_domain", ["domain"])
  .index("by_visibility", ["visibility"])
  .vectorIndex("by_embedding", { vectorField: "embedding", dimensions: 1536 }),

cross_lab_links: defineTable({
  source_knowledge_id: v.string(),        // entity in lab A
  target_knowledge_id: v.string(),        // entity in lab B
  link_type: v.string(),                  // "uses", "extends", "contradicts", "references"
  confidence: v.number(),
  detected_by: v.string(),                // which agent or "auto-vector"
  detected_at: v.string(),
}).index("by_source", ["source_knowledge_id"])
  .index("by_target", ["target_knowledge_id"]),
```

**The cross-lab discovery scenario** (Houston's specific use case):

1. Houston creates a new lab `quantum-gravitational-waves`
2. The lab template scaffolds the dirs and registers in Convex
3. The new lab's main agent boots and runs the **cross-lab knowledge sweep**:
   - Pulls all `global_knowledge` entries with `visibility != "private"` and matching `domain` or related tags
   - Vector-searches global knowledge for terms in the new lab's name/description
   - Surfaces top 20 relevant items in a "Related work from other labs" panel
4. The agent presents to Houston: "I found 8 relevant items from BigBounce that may apply here: [list]. Want me to import any?"
5. Houston picks which to import. Imported items become local references without duplication.
6. Cross-lab links are auto-created so future searches in either lab surface the connection.
7. As the new lab generates its own knowledge, the same vector-search runs every time something new is added — surfacing new cross-lab connections automatically.

**Cross-lab cron** (every 30 minutes):
- For each new global_knowledge entry created in the last 30 min
- Run vector similarity against all other global_knowledge
- For matches above threshold (cosine > 0.85), create `cross_lab_links` entries
- Notify both labs' agents of new connections via the activity stream

### 20.6 Memory Storage Backend

**Primary:** Convex DB. Already in use, has vector search built-in (Convex Vector Search supports embeddings + filters), supports the multi-table schema, real-time subscriptions for the UI.

**Secondary (mirror):** Filesystem markdown files for everything human-readable. Houston likes plain files. Files mirror Convex but Convex is the source of truth. Files are committed to git so every memory change has a history.

**Embedding provider:** OpenAI `text-embedding-3-small` (1536 dim) — cheap, fast, good enough. Swappable behind an interface so we can switch to local embeddings (BGE, e5) later if the cost becomes meaningful or if we want sovereign infra.

**Storage budget estimate:**
- 100K user messages × 4KB avg = 400 MB
- 1M agent episodes × 8KB avg = 8 GB
- 10K lab decisions × 2KB avg = 20 MB
- 100K global knowledge × 4KB avg = 400 MB
- Embeddings: ~6 KB per record × 1.2M records = 7 GB
- **Total: ~16 GB after a year of heavy use.** Convex pricing handles this comfortably on Pro.

### 20.7 Memory Search & Retrieval

**Three retrieval modes, used in combination:**

1. **Keyword search (BM25-style):** Fast exact-match for IDs, names, file paths, error messages. Use when the agent knows exactly what it's looking for.
2. **Vector search (semantic):** Top-K nearest neighbors by embedding cosine similarity. Use for "find anything similar to this concept."
3. **Tag/filter search:** Constrained by category, domain, visibility, time range. Use to scope before searching.

**Hybrid retrieval default:** Most agent queries use a 3-way blend:
- Filter by lab + domain + visibility
- Then keyword search for explicit terms (top 20)
- Then vector search for semantic similarity (top 20)
- Re-rank by recency × relevance × use-count
- Return top 10 to the agent

**Search API surface (`api.hubify.com/memory`):**
```typescript
// Search across any layer
POST /memory/search
{
  query: string,
  layers: ("user" | "agent" | "lab" | "global")[],
  user_id?: string,
  agent_id?: string,
  lab_id?: string,
  tags?: string[],
  type?: string,
  time_range?: { start: string, end: string },
  limit: number,                    // default 10
  mode: "hybrid" | "keyword" | "vector",
}
// → returns ranked results with provenance

// Write to a layer
POST /memory/write
{
  layer: "user" | "agent" | "lab" | "global",
  type: string,
  content: object,
  tags?: string[],
  source: string,
}

// Inspect a memory record
GET /memory/:layer/:id
PATCH /memory/:layer/:id
DELETE /memory/:layer/:id
```

### 20.8 Memory UI Surface

The Hubify Labs UI has a dedicated **Memory** view in the left sidebar:

```
+--------------------------------------------+
| Memory                            [⌘M]    |
+--------------------------------------------+
| LAYER                                      |
| ▾ User (Houston)         12,340 messages   |
| ▸ Agent (orchestrator)   1,847 episodes    |
| ▸ Lab (bigbounce)        53 experiments    |
| ▸ Global                 1,420 entries     |
+--------------------------------------------+
| SEARCH                                     |
| [search across all layers...]              |
+--------------------------------------------+
| FILTERS                                    |
| Type:       [all ▾]                        |
| Tags:       [+ add tag]                    |
| Lab:        [bigbounce ▾]                  |
| Time:       [all time ▾]                   |
+--------------------------------------------+
| RESULTS (sorted by relevance)              |
| 2026-04-07 17:42  user · idea              |
|   "should we use modal or runpod..."       |
|   tags: compute, dual-provider             |
|   ─                                         |
| 2026-04-07 18:01  user · preference        |
|   "need our agents to remember..."         |
|   tags: memory, agent-harness              |
|   ─                                         |
| ...                                         |
+--------------------------------------------+
```

Houston can:
- Click any memory to open the full record + edit it
- Bulk-tag, bulk-delete, bulk-export
- Pin memories so they always load in agent context
- Mute memories he doesn't want agents to act on
- See "agents who used this memory" with a use-count

### 20.9 Memory Hygiene

**The forgetting problem:** Naive memory systems accumulate noise. Hubify's hygiene rules:

1. **No deletion by default.** Memories accumulate. Disk is cheap, regret is expensive.
2. **Decay scoring:** Each retrieval re-ranks by `relevance × recency × confidence × use_count`. Old unused memories sink, but they're not deleted.
3. **Supersession over deletion:** If a new memory contradicts an old one, the old one is marked `superseded_by` with a link to the new. The old memory stays for audit.
4. **Cleanup cron (weekly):** Run a small fast model over the previous week's memories. Flag duplicates for human review. Houston confirms or rejects merges.
5. **Audit trail:** Every memory edit/delete is logged. No silent rewrites of history.

**The verification problem:** Some memories are facts (ground truth). Some are opinions or guesses. The system tags every memory with `confidence` and an optional `verified_by` agent. Skeptic agents can be tasked to verify low-confidence memories against external sources.

### 20.10 CLAUDE.md and AGENTS.md — The Static Layer

In addition to the dynamic Convex memory, every lab has static instruction files that Claude Code (and any other coding agent) reads on startup. These are the "always-loaded" rules.

**Per-lab files:**
- `<lab>/CLAUDE.md` — instructions for any AI agent working in this lab. Already exists for BigBounce.
- `<lab>/AGENTS.md` — agent roster, role definitions, model assignments, current responsibilities. NEW.
- `<lab>/.hubify-labs/MEMORY.md` — index of all lab memory entries with one-line descriptions.
- `<lab>/.hubify-labs/STATE.md` — current lab state snapshot.

**Global files (in `~/.hubify/`):**
- `~/.hubify/CLAUDE.md` — global instructions across all labs.
- `~/.hubify/users/houston/MEMORY.md` — Houston's user memory index.
- `~/.hubify/AGENTS.md` — global agent definitions (templates).

**Auto-update protocol:** These files are NOT hand-edited by humans (except CLAUDE.md). They're auto-regenerated by the memory system on every memory write. Houston edits CLAUDE.md when he wants to add a new permanent rule; everything else is generated.

### 20.11 Open-Source Memory Project Survey

Houston explicitly does not want Supermemory or another SaaS. He wants in-house ownership. A background research agent has been spawned to survey https://github.com/topoteretes/awesome-ai-memory and recommend which OSS projects to fork or borrow from.

**Output:** `bigbounce/project-context/memory_systems_survey.md` (in progress)

**Expected candidates to evaluate:**
- mem0 (graph + vector memory)
- Letta (formerly MemGPT)
- Zep / Graphiti (temporal knowledge graph)
- cognee (the awesome list owner's project)
- Memori (episodic memory)
- Memobase (user profiling)

**Decision criteria:**
- Permissive license (MIT/Apache 2.0)
- Convex-compatible storage
- Multi-namespace support
- Active maintenance
- 4-layer fit
- Forkability

**Recommendation will be either:** (a) fork project X and customize, or (b) build from scratch using best ideas from multiple projects. Pure SaaS dependency is rejected outright.

### 20.12 Memory System Quality Metrics

The memory system is the foundation. We need to measure it.

**Metrics tracked weekly:**
- **Question repeat rate:** How often did Houston have to repeat himself? Target: <2% of sessions.
- **Forgotten task rate:** How often did the main lab agent forget a task that was queued? Target: 0%.
- **Cross-lab discovery latency:** When new global_knowledge is added, how long until cross-lab links surface? Target: <30 min.
- **Memory storage growth:** Bytes/week. Track for cost forecasting.
- **Retrieval relevance:** Houston manually rates 10 random retrievals/week as relevant/not. Target: >80% relevant.
- **Agent learning reuse rate:** What fraction of agent learnings actually get applied later? Low reuse = noise.

These metrics are surfaced in the Director view's "Memory health" card.

---

## 21. User Profile & Public Showcase

**Goal:** Hubify is not just a private research IDE — it has a public face. Houston wants to be visible as a researcher, share work he's proud of, and use his profile as a credibility signal. Other Hubify users can browse public profiles, follow researchers, and learn from shared knowledge.

### 21.1 Public Profile Page (`hubify.app/u/<handle>`)

```
+----------------------------------------------------+
| HOUSTON GOLDEN                          [follow]   |
| @houston · independent researcher · LA              |
| Bounce cosmology · 4 papers · 8.47M galaxies        |
+----------------------------------------------------+
| ACTIVITY                                           |
| ░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░ (52-week heatmap) |
| 218 contributions · 53 experiments · 4 papers       |
+----------------------------------------------------+
| PINNED LABS                                        |
| ┌──────────────┐ ┌──────────────┐ ┌──────────────┐|
| │ bigbounce    │ │ chirality    │ │ pta-gw       │|
| │ public · 53  │ │ public · ✓   │ │ private 🔒   │|
| └──────────────┘ └──────────────┘ └──────────────┘|
+----------------------------------------------------+
| PAPERS (4)                                         |
| 1. Spin-Torsion Cosmology — 14 ECH Barriers, ALP   |
|    Birefringence · v2.2.1 · 99% · novelty 9/10     |
| 2. Parameter-Free f_NL = -35/8 Prediction · v1.3   |
|    100% · novelty 10/10                            |
| 3. DESI DR1 Spectral Anomaly Catalog · 195K objs   |
|    95% · novelty 8/10                              |
| 4. Galaxy Chirality Catalog · 8.47M galaxies       |
|    85% · novelty 7/10                              |
+----------------------------------------------------+
| SCIENTIFIC CONTRIBUTIONS (12)                      |
| · f_NL = -35/8 prediction       novelty 10/10 [✓] |
| · ALP β = 0.27° prediction      novelty 9/10  [✓] |
| · 14 ECH barriers framework     novelty 9/10  [✓] |
| · Combined PTA Bayes 27.6       novelty 8/10  [✓] |
| · Anomaly bias 2.28× validation novelty 8/10  [✓] |
| · ... (see all)                                    |
+----------------------------------------------------+
| PUBLIC MODELS (3)                                  |
| · spectral-autoencoder-47k    1,247 downloads     |
| · galaxy-chirality-cnn        892 downloads        |
| · qso-classifier-resnet18     440 downloads        |
+----------------------------------------------------+
| PUBLIC DATASETS (5)                                |
| · DESI DR1 anomaly catalog       195,829 rows     |
| · Galaxy chirality catalog       8,470,000 rows   |
| · ...                                              |
+----------------------------------------------------+
| ARTICLES (7)                                       |
| · The 14 ECH Barriers, Explained                  |
| · Why f_NL = -35/8 matters for SPHEREx 2028       |
| · ...                                              |
+----------------------------------------------------+
```

### 21.2 Public/Private Lab Toggle

Each lab has a visibility setting in `<lab>/.hubify-labs/config.yaml`:
```yaml
visibility: private    # private | public
public_pages:
  papers: true         # show paper list on profile
  contributions: true  # show contributions on profile
  models: true         # show released models
  datasets: true       # show released datasets
  activity: true       # show activity in heatmap
  experiments: false   # don't expose individual experiments
```

**Default for new labs: PRIVATE.** Houston explicitly said he wants in-progress unpublished research private by default to avoid being scooped. He can flip a lab public when he's ready (e.g., after the first paper drops).

**Selective publishing:** Within a private lab, Houston can mark individual items public:
- A paper can be public even if the lab is private
- A model can be public even if the lab is private
- A dataset can be public even if the lab is private
- The lab itself stays hidden, but the artifact appears on his profile

### 21.3 Activity Tracker

GitHub-style heatmap is the obvious starting point. But Houston asked for "something more unique but kinda similar idea". Proposed enhancements:

**Daily activity heatmap with multi-dimensional cells:**
- Each day cell is split into 4 quadrants showing different activity types:
  - Top-left: experiments run
  - Top-right: papers/articles edited
  - Bottom-left: agent activity (autonomous work while Houston was away)
  - Bottom-right: knowledge added (wiki entries, learnings)
- Color intensity per quadrant = volume
- Hover for breakdown

**Activity stream below the heatmap** (chronological feed):
```
2026-04-07 04:13  EXP-050: DESI × eROSITA cross-correlation — 4.1σ signal
2026-04-07 03:42  Paper 1 v2.2.1 draft ready
2026-04-07 02:18  EXP-052: Gaia DR3 10× expansion — 5,000 anomalies
2026-04-07 01:55  Houston: deploy phase 9 on a fresh pod
2026-04-06 23:14  Wiki: added "f_NL triple role" entry
...
```

**Per-day drilldown** (click a cell):
- Full list of every event that day
- Time-of-day distribution
- Cost incurred
- Discoveries made
- Mistakes corrected (with link to fix commit)

**Privacy:** Same toggle as labs — Houston can hide activity from specific labs.

### 21.4 Knowledge Sharing Controls

Two sharing levels:

1. **Lab-level public:** Lab is visible on profile + lab knowledge is queryable by other Hubify users' agents (but only if they have a query that matches). Doesn't surface unless asked.
2. **Globally contributed:** Houston explicitly hits "Contribute to Global Knowledge" on a specific item (entity, learning, dataset). It enters the global knowledge graph as a featured item, indexed by SEO, and visible to anyone browsing.

**Per-item contribution UI:**
```
[Wiki entry: "Cosmic birefringence ALP prediction"]

  Visibility: Public ▾
  ☐ Contribute to global Hubify knowledge

  Contributing makes this entry visible to:
  · All Hubify users browsing the global wiki
  · Agents in other labs searching for related work
  · Search engines (SEO-optimized landing page)

  You can revoke at any time.

  [Contribute] [Cancel]
```

### 21.5 Custom Articles

Houston has 7 deep-dive articles on bigbounce.hubify.app today. The platform should let him write more without leaving Hubify Labs.

**Article editor:**
- Markdown editor in the right preview pane
- Live preview
- Auto-save to lab + version control
- Publish to profile when ready
- SEO meta editor (title, description, og:image)
- Cross-link to wiki entries, papers, figures, datasets

**Article surface on profile:**
- Articles list section
- Click to read full article
- Custom slug per article (`hubify.app/u/houston/articles/14-ech-barriers`)
- Comments? TBD — if added, must be moderated to prevent noise.

### 21.6 SEO Optimization

Public profile pages, public lab pages, public articles, and public knowledge entries all get:
- Server-side rendered HTML (Next.js SSG/ISR via Vercel Fluid Compute)
- Meta tags: title, description, canonical, og:image, twitter:card
- Structured data: Article, Person, ScholarlyArticle, Dataset (Schema.org)
- Sitemap.xml auto-generated from public content
- robots.txt allowing indexing of public pages
- Custom URL slugs (no UUIDs)

**Ranking targets:** Houston wants his public work findable when researchers search Google for "f_NL prediction bounce cosmology", "DESI anomaly catalog", "ALP cosmic birefringence prediction", etc. SEO is not vanity — it's discoverability for collaborators and peer reviewers.

### 21.7 User Profile Convex Schema

```typescript
users: defineTable({
  user_id: v.string(),                    // "houston"
  handle: v.string(),                     // "houston"
  display_name: v.string(),               // "Houston Golden"
  bio: v.string(),
  location: v.string(),
  email: v.string(),
  avatar_url: v.optional(v.string()),
  created_at: v.string(),
  followers_count: v.number(),
  following_count: v.number(),
}).index("by_handle", ["handle"]),

lab_visibility: defineTable({
  lab_id: v.string(),
  user_id: v.string(),
  visibility: v.string(),                 // private | public
  pinned: v.boolean(),                    // pinned to profile
  public_pages: v.object({
    papers: v.boolean(),
    contributions: v.boolean(),
    models: v.boolean(),
    datasets: v.boolean(),
    activity: v.boolean(),
    experiments: v.boolean(),
  }),
}).index("by_user", ["user_id"]),

profile_articles: defineTable({
  user_id: v.string(),
  slug: v.string(),
  title: v.string(),
  description: v.string(),
  body_md: v.string(),
  body_html: v.string(),                  // pre-rendered
  cover_image: v.optional(v.string()),
  published: v.boolean(),
  published_at: v.optional(v.string()),
  updated_at: v.string(),
  source_lab: v.optional(v.string()),
  word_count: v.number(),
  read_count: v.number(),
}).index("by_user_published", ["user_id", "published_at"])
  .index("by_slug", ["slug"]),

activity_log: defineTable({
  user_id: v.string(),
  date: v.string(),                       // YYYY-MM-DD
  experiments_run: v.number(),
  papers_edited: v.number(),
  agent_activity: v.number(),             // tasks completed by agents
  knowledge_added: v.number(),            // wiki entries
  total: v.number(),
  source_lab: v.optional(v.string()),
}).index("by_user_date", ["user_id", "date"]),
```

---

## 22. Scientific Contributions & Novelty Scoring

Houston wants the platform to ENFORCE rigorous novelty checking. He should never publish a claim that has already been made by someone else. Multi-agent cross-review across multiple platforms is the mechanism.

### 22.1 The Contributions System

A **scientific contribution** is a single distinct claim, finding, or artifact from a paper. Examples:
- "f_NL = -35/8 prediction from matter bounce" (claim)
- "ALP cosmic birefringence β = 0.27°" (claim)
- "DESI DR1 anomaly catalog with 195,829 objects" (artifact)
- "Combined PTA Bayes factor 27.6 for bounce vs SMBHB" (claim)
- "Galaxy chirality catalog with 8.47M classifications" (artifact)

Each contribution gets:
- Title
- Description (1-2 sentences)
- Type (claim | finding | artifact | method | dataset | model)
- Source paper(s)
- Source experiment(s)
- Source data
- **Novelty score (1-10)**
- **Novelty audit trail**
- Citations of prior work that nearly matches but doesn't supersede
- Status (draft | reviewed | published | retracted)
- Visibility (private | public)

### 22.2 Novelty Scoring Pipeline

When a contribution is created (auto-extracted from a paper draft, or manually added), the platform spawns a **Novelty Review Pipeline**:

```
1. EXTRACT
   Lead agent reads the contribution and generates 5-10 search queries
   that would find prior work if it exists.
   Examples for "f_NL = -35/8":
     - "f_NL prediction matter bounce cosmology"
     - "primordial non-Gaussianity bounce model parameter free"
     - "bispectrum amplitude bounce cosmology theoretical prediction"
     - "f_NL value -35/8"
     - "matter bounce f_NL signature"

2. PARALLEL SEARCH (5+ workers, one per platform)
   For each platform, a worker agent runs all queries:
     - arXiv (https://arxiv.org/search)
     - NASA ADS (https://ui.adsabs.harvard.edu)
     - INSPIRE-HEP (https://inspirehep.net)
     - Semantic Scholar (https://www.semanticscholar.org)
     - Google Scholar (via SerpAPI or similar)
     - (optional) bioRxiv if biology, SSRN if economics

3. COLLECT
   Each worker returns top 20 hits per query.
   Total candidates: ~100-1000 papers.

4. DEDUPE + RANK
   Remove duplicates by DOI/arXiv ID/title.
   Rank by relevance (vector similarity to contribution).

5. DEEP READ (top 20 candidates)
   For each top hit, a reader agent fetches the abstract + intro + conclusion.
   Determines: does this paper make the same claim?
     - Same: SUPERSEDED — novelty 0
     - Similar but different scope: PARTIAL — novelty 5-7
     - Adjacent but different: ADJACENT — novelty 7-9
     - Unrelated: UNRELATED

6. SKEPTIC PASS
   A skeptic agent reviews the reader's verdict.
   Tries hard to find prior work the reader missed.
   If skeptic finds something, novelty score drops.
   If skeptic confirms nothing found, novelty score holds.

7. SCORE
   Final novelty score = 1-10 based on:
     - 10: completely novel, no prior work in any direction
     - 9: novel but builds on adjacent work (cited)
     - 8: novel application of known method
     - 7: novel parameter/result of known framework
     - 5: similar work exists but with key differences
     - 3: very similar prior work, must justify difference
     - 1: superseded by prior work

8. AUDIT TRAIL
   Every searched query, every platform hit, every skeptic finding,
   and every model decision is logged.
   Houston can drill into any contribution and see EXACTLY what was checked.

9. RE-REVIEW SCHEDULE
   Literature is alive. The same review re-runs:
     - 7 days after first review
     - 30 days after
     - 90 days after
     - Then quarterly forever
   If new prior work appears, the contribution score drops and Houston
   gets an alert. This prevents the embarrassing "someone published
   exactly this 2 weeks ago" scenario.
```

### 22.3 Novelty Review Convex Schema

```typescript
contributions: defineTable({
  contribution_id: v.string(),
  user_id: v.string(),
  lab_id: v.string(),
  title: v.string(),
  description: v.string(),
  type: v.string(),                       // claim | finding | artifact | method | dataset | model
  source_papers: v.array(v.string()),
  source_experiments: v.array(v.string()),
  novelty_score: v.number(),              // 1-10, current
  novelty_status: v.string(),             // pending | reviewed | flagged | superseded
  status: v.string(),                     // draft | reviewed | published | retracted
  visibility: v.string(),                 // private | public
  created_at: v.string(),
  last_reviewed_at: v.string(),
  next_review_at: v.string(),
}).index("by_user", ["user_id"])
  .index("by_lab", ["lab_id"])
  .index("by_score", ["novelty_score"])
  .index("by_next_review", ["next_review_at"]),

novelty_reviews: defineTable({
  review_id: v.string(),
  contribution_id: v.string(),
  review_round: v.number(),               // 1, 2, 3, ... (re-reviews)
  triggered_by: v.string(),               // initial | scheduled | manual
  queries_generated: v.array(v.string()),
  platforms_searched: v.array(v.string()),
  total_candidates: v.number(),
  top_candidates: v.array(v.object({
    title: v.string(),
    authors: v.string(),
    year: v.number(),
    doi: v.optional(v.string()),
    arxiv_id: v.optional(v.string()),
    platform: v.string(),
    relevance: v.number(),
    verdict: v.string(),                  // superseded | partial | adjacent | unrelated
    notes: v.string(),
  })),
  reader_verdict: v.string(),
  skeptic_verdict: v.string(),
  final_score: v.number(),
  audit_md: v.string(),                   // human-readable audit trail
  reviewed_at: v.string(),
  duration_seconds: v.number(),
  cost_usd: v.number(),
}).index("by_contribution_round", ["contribution_id", "review_round"]),
```

### 22.4 Novelty UI Surface

In the lab's **Contributions** view:

```
+--------------------------------------------+
| Contributions (12)                         |
+--------------------------------------------+
| CONTRIBUTION                  NOVELTY  STATUS|
| f_NL = -35/8 prediction         10/10  ✓   |
| ALP β = 0.27° prediction         9/10  ✓   |
| 14 ECH barriers framework        9/10  ✓   |
| Combined PTA Bayes 27.6          8/10  ✓   |
| Anomaly bias 2.28× validation    8/10  ✓   |
| Galaxy chirality catalog 8.47M   7/10  ✓   |
| DESI DR1 anomaly catalog 195K    8/10  ✓   |
| ...                                        |
+--------------------------------------------+
| FILTERS                                    |
| [All ▾] [Claim ▾] [Last reviewed ▾]        |
+--------------------------------------------+
```

Click any contribution → drilldown:
```
+--------------------------------------------+
| f_NL = -35/8 prediction         novelty 10 |
+--------------------------------------------+
| Description                                |
| Parameter-free prediction f_NL = -35/8 =   |
| -4.375 from matter-bounce mechanism.       |
+--------------------------------------------+
| Source                                     |
| · Paper 2: Parameter-Free f_NL Prediction  |
| · EXP-049: bounce model derivation         |
+--------------------------------------------+
| Novelty audit (3 reviews · 142 papers searched)
| ✓ initial review · 2026-03-12 · score 10  |
| ✓ 7-day re-review · 2026-03-19 · score 10 |
| ✓ 30-day re-review · 2026-04-11 · score 10|
| ⏰ next review · 2026-07-11                |
+--------------------------------------------+
| Top adjacent papers (none superseding)     |
| · Cai et al. 2024 — f_NL bounce ranges    |
|   [adjacent · novelty 9 · verdict: differ-|
|   ent derivation, broader range]          |
| · Wand 2023 — primordial bispectrum bounce|
|   [adjacent · verdict: ekpyrotic, not     |
|   matter bounce]                          |
| · ... (full list)                         |
+--------------------------------------------+
| [Re-review now] [Edit] [Mark public]      |
+--------------------------------------------+
```

### 22.5 Re-review Cron

Every hour at :17, the platform queries `contributions where next_review_at <= now()` and runs the review pipeline. Default cadence:
- 1st re-review: 7 days
- 2nd re-review: 30 days
- 3rd re-review: 90 days
- Then quarterly

If a re-review drops the score, Houston gets a high-priority alert in the Director view.

### 22.6 Novelty Cost Management

Each review run costs ~$1-3 in API calls (search APIs + reader model). For 12 contributions × 4 reviews/year = 48 reviews/year × $2 avg = ~$100/year per lab. Cheap insurance against publishing duplicates.

The cost is logged to `novelty_reviews.cost_usd` so Houston can see the line item.

---

## 23. Houston Method v2 — Platform-Level Enforcement

The Houston Method is currently a skill in `project-context/houston-method-v2.md`. Houston has had to repeat it constantly because skills are advisory, not enforced. **Hubify Labs encodes the Houston Method as platform-level behavior the agents cannot bypass.**

### 23.1 Why Platform-Level Enforcement

A skill is text. Text gets ignored. Hard rules enforced by the platform get followed.

Houston's frustration: he has stated "when an experiment finishes, do X, Y, Z" dozens of times across dozens of sessions, and the agents still skip steps. The fix is not "tell them again". The fix is "make it impossible to mark an experiment complete without completing the full protocol".

### 23.2 The Mandatory Post-Experiment Protocol

When ANY experiment finishes (success or failure), the platform automatically triggers the **Post-Experiment Protocol**, which is a state machine the agent CANNOT exit until all states are complete:

```
EXPERIMENT FINISHES
    ↓
[1] QC GATE
    Run quality checks. If FAIL → return to fix-loop.
    If PASS → continue.
    ↓
[2] SCIENTIFIC ANALYSIS
    Generate the analysis: what does this result mean?
    Compare to predictions. Compare to prior runs.
    Write to lab decisions log.
    ↓
[3] INTERPRETATION
    What does this change? What's confirmed? What's ruled out?
    Write 1-paragraph summary suitable for paper draft.
    ↓
[4] CROSS-SURVEY CONNECTION
    Search global knowledge for related work in other labs.
    If matches found, create cross-lab links.
    Notify other labs of the new result.
    ↓
[5] SITE SYNC
    Update bigbounce.hubify.app with the new result.
    Update activity.html, index.html stats, data-explorer if new data.
    Commit and push.
    ↓
[6] QUEUE EXPANSION
    Generate 5-15 new tasks based on this result:
    · Follow-up experiments
    · New angles to explore
    · New cross-checks
    · Things to verify
    Add to the lab's idea queue with viability scores.
    ↓
[7] BACKUP
    Backup all outputs to:
    · Local lab dir
    · External backup location
    · Cloud (if enabled)
    Verify backup integrity (checksum).
    ↓
[8] AGENT MEMORY UPDATE
    Write learnings to agent_learnings table.
    Update lab_state.STATE.md.
    Update user_messages if Houston was involved.
    ↓
EXPERIMENT MARKED COMPLETE
```

**The agent CANNOT skip a step.** The platform's state machine enforces it. If step 6 (queue expansion) returns 0 tasks, the platform rejects the completion and the agent must retry. If step 7 (backup) fails the integrity check, the platform marks the experiment "incomplete" and surfaces an alert.

### 23.3 Idle GPU Watchdog

Every 5 minutes, the platform checks: **is there a pod with credits and no active work?**

```
WATCHDOG FIRES (every 5 min)
    ↓
For each pod in user's account:
  ↓
  query: nvidia-smi GPU utilization
  query: tmux sessions
  ↓
  IF GPU < 5% utilization for >5 min AND no tmux sessions:
    ↓
    Check user's pod preference:
      A) Proactive Mode → spawn idle-handler
      B) Save Credits Mode → backup + stop pod
    ↓
    PROACTIVE MODE:
      1. Read lab idea queue
      2. Pick highest-viability untried idea
      3. If idea cost < $25: just run it
      4. If idea cost >= $25: notify Houston, run if no objection in 30 min
      5. Spin up the experiment via standard pipeline
      6. Log "watchdog auto-launched" event
    ↓
    SAVE CREDITS MODE:
      1. Backup all pod data
      2. Verify integrity
      3. Notify Houston: "Pod is idle. Backing up and stopping in 5 min."
      4. After 5 min if no override: stop pod
      5. Log "watchdog auto-stopped" event
```

**Per-pod preference** (set in Settings → Compute):
```yaml
pods:
  bigbounce-h200:
    provider: runpod
    proactive_mode: true        # default
    proactive_max_cost_per_task: 25
    idle_threshold_minutes: 5

  experimental-h200:
    provider: modal
    proactive_mode: false       # save credits
    save_after_idle_minutes: 5
```

**Per-lab default** that new pods inherit. **Per-user global default** that new labs inherit.

### 23.4 Queue Health Watchdog

Every hour, check the lab's idea queue:
- If queue has < 10 items: spawn an **idea-generation agent**
- The idea agent brainstorms 10-20 new directions across:
  - New surveys to scan
  - New cross-survey correlations
  - New models to train
  - New parameter sweeps
  - New datasets to download
  - **New research domains** (Houston wants exploration, not just exploitation)
- New ideas land in the queue with viability scores
- Houston gets a digest notification: "5 new ideas added to queue"

### 23.5 Failed-Experiment Recovery Protocol

When an experiment fails:
```
1. CAPTURE
   Save the full traceback, logs, environment state.
2. CLASSIFY
   Determine: data issue / code bug / infra failure / OOM / timeout
3. AUTO-FIX ATTEMPT
   For known failure patterns, attempt the standard fix:
     · OOM → reduce batch size, retry
     · Numpy version → pin version, retry
     · Disk full → cleanup, retry
4. IF AUTO-FIX FAILS
   Spawn a debugger agent with the full context
   Log the failure to agent_learnings (so this pattern is known next time)
5. ESCALATE TO HOUSTON
   Only if (1)-(4) all fail
   Present full debug context, what was tried, recommendation
```

### 23.6 The "Never Repeat Yourself" Guarantee

Before any agent asks Houston a question, it MUST:
1. Search user_messages for similar prior questions
2. Search user_preferences for related preferences
3. If found: use the prior answer, notify Houston "Using your prior preference: X"
4. If not found: ask, then save the answer to user_preferences

**Quality metric:** Repeated-question rate. Surfaced in Director view. Target <2%.

### 23.7 Houston Method Quality Metrics

Tracked weekly:
- **Protocol completion rate:** % of experiments where all 8 steps ran. Target 100%.
- **Idle GPU minutes per week:** Total minutes a pod was idle when proactive mode was on. Target <30 min.
- **Queue depth average:** Average number of ideas in the queue. Target >15.
- **New domains opened per month:** How many genuinely new research directions started. Target >1.
- **Repeated questions:** Times Houston had to repeat a stated preference. Target 0.

If any metric drops below target for 2 consecutive weeks, the platform fires a self-improvement task: "agent behavior is degrading, investigate and fix".

---

## 24. Compute Provider — RunPod ONLY (Pods + Serverless + CPU/GPU variants)

**STATUS LOCKED 2026-04-08:** Houston confirmed: drop Modal entirely. Modal and RunPod Serverless are functionally identical (both auto-scale, both $0 when idle, both per-second billing, both have ~24h soft caps for long jobs). Modal is slightly more dev-friendly via Python decorators but ~33% more expensive AND adds a second vendor / second billing relationship / second credentials store. **One vendor is simpler. RunPod for everything.**

This section supersedes the earlier "RunPod first, Modal coming soon" plan. The full PRE-2026-04-08 architecture decision document `bigbounce/project-context/compute_architecture_decision.md` is now historical — it documents how we got to this decision but no longer reflects the locked architecture.

### 24.1 The two compute modes (one vendor, two surfaces)

RunPod offers two execution models. Both bill against the same RunPod credits balance, both use the same network volumes for persistent storage, both share the same SSH key + API token.

**Pods (always-on, hourly billing):**
- A dedicated VM (CPU or GPU) that you SSH into and use like a server
- Hourly billing: charged for every hour the pod is running, even idle
- Best for: long-running training jobs, MCMC chains > 30 min, persistent workloads (Jupyter sessions), workloads where you'll dispatch many sequential jobs in a row and want to avoid cold starts
- Pricing examples: H200 SXM = $3.59/hr, A100 80GB = $1.69/hr, RTX 4090 = $0.79/hr, CPU-only (4 vCPU 16GB) = $0.16/hr

**Serverless (auto-scale, per-second billing, $0 when idle):**
- Function-style invocation: deploy a Docker image with a handler.py, then trigger via REST API
- Per-second billing: pay only for the wall-clock time the function is actually executing
- Auto-scales from 0 to N parallel workers based on demand
- Best for: spiky inference (process this batch of 1000 anomalies), short batch jobs < 30 min, embarrassingly parallel work, webhook-triggered tasks, anything where total duty cycle < 20% of wall time
- Pricing examples: H100 ~$0.00088/sec ($3.17/hr equivalent), A100 ~$0.00060/sec ($2.16/hr equivalent), CPU-only ~$0.00003/sec ($0.11/hr equivalent)

**Both modes support BOTH CPU and GPU variants.** A "CPU pod" is just a pod with no GPU attached — much cheaper, fine for non-tensor work. Same for "CPU serverless" — a serverless function that runs on a CPU-only worker.

### 24.2 Why we dropped Modal

Houston's instinct: *"modal is interesting and cool but we gotta keep simplicity wherever possible... it seems like basically the same thing as modal."*

He's correct. The honest comparison:

| Dimension | Modal | RunPod Serverless | Why RunPod wins |
|---|---|---|---|
| Billing model | Per-second, $0 idle | Per-second, $0 idle | tie |
| Cold start | 2-15 sec | 5-30 sec | Modal slightly faster but RunPod is acceptable for our workloads |
| Setup ergonomics | Python `@app.function` decorator | Docker image + `handler.py` | Modal is easier but the ergonomic gap is small once you have a handler template |
| Pricing (H100) | ~$4.50/hr equivalent | ~$3.17/hr equivalent | **RunPod ~30% cheaper** |
| Pricing (A100) | ~$3.50/hr equivalent | ~$2.16/hr equivalent | **RunPod ~38% cheaper** |
| Long-running cap | 24h hard | 24h soft (varies by plan) | tie (both bad for multi-day jobs — use Pods instead) |
| GPU variety | A10G, A100, H100, H200 | RTX 4090, A4000-A6000, A100, H100, H200, MI300X | **RunPod (more options including consumer cards for cheap)** |
| Vendor count | +1 vendor | Same vendor as Pods | **RunPod (one billing, one auth, one credit pool)** |
| Persistent state | Modal Volumes | RunPod Network Volumes | tie (both work, RunPod's are cheaper) |

**The bottom line:** Modal's only real advantage is decorator-style ergonomics. That's worth ~1 day of dev work to replicate against RunPod via a thin Python wrapper. The 30-38% pricing gap and the simplicity of one vendor outweigh the developer-experience gap.

**The trade-off we're accepting:** Modal's `@app.function(...)` API is genuinely cleaner. RunPod requires building a Docker image with `handler.py`. To narrow the gap, the platform ships a small Python helper:

```python
# hubify_labs/runpod_serverless.py — Modal-decorator-style wrapper around RunPod
@hubify_serverless.function(gpu="H100", timeout=3600, volume="bigbounce-data")
def run_anomaly_detection(survey: str, n_anomalies: int = 1000) -> dict:
    # Body executes as a serverless function on RunPod
    ...
```

Under the hood this generates a Dockerfile + handler.py + the REST trigger code. The user writes Python; the framework handles the RunPod Serverless plumbing. This closes the dev-experience gap.

### 24.3 Per-lab compute config

`<lab>/.hubify-labs/compute.yaml`:
```yaml
provider: runpod                    # the only provider, locked

# Pods registered to this lab (always-on)
pods:
  bigbounce-h200:
    pod_id: o76k3jfzbfh25e
    gpu_type: H200_SXM
    cost_per_hour: 3.59
    proactive_mode: true             # see §24.5
    proactive_max_cost_per_task: 25
    idle_threshold_minutes: 10
    auto_attach_volume: bigbounce-data

# Serverless endpoints registered to this lab
serverless:
  anomaly-detector:
    endpoint_id: <runpod-endpoint-id>
    image: hubify-labs/anomaly-detector:latest
    gpu_type: A100_80GB
    timeout_seconds: 1800            # 30 min max per call
    max_workers: 10                  # auto-scale up to this
    cost_per_second: 0.00060

  pdf-qa:
    endpoint_id: <runpod-endpoint-id>
    image: hubify-labs/pdf-qa:latest
    gpu_type: cpu                    # CPU-only — pdftotext doesn't need a GPU
    timeout_seconds: 300
    max_workers: 5
    cost_per_second: 0.00003
```

### 24.4 The Compute Abstraction (simplified — no provider polymorphism needed)

Since there's only one provider, the abstraction is now just a thin RunPod client with two methods + storage + monitoring:

```typescript
class RunPodCompute {
  // Pods
  startPod(spec: PodSpec): Promise<PodHandle>;
  stopPod(handle: PodHandle): Promise<void>;
  podStatus(handle: PodHandle): Promise<PodStatus>;

  // Serverless
  invokeServerless(endpointId: string, input: object): Promise<JobHandle>;
  serverlessStatus(handle: JobHandle): Promise<JobStatus>;

  // Shared
  volume(name: string): VolumeHandle;
  getCreditBalance(): Promise<number>;       // see §41
  streamLogs(handle: PodHandle | JobHandle): AsyncIterable<LogLine>;
}
```

No provider router. No polymorphism. No abstraction tax. Single-vendor simplicity.

### 24.5 Post-Run Behavior Toggle (per Pod only — Serverless is always "save credits")

Two modes for **Pods**:

**Proactive Mode (default for active research):**
- When current run finishes, immediately pick next from queue
- Pod stays running, GPU stays utilized
- Best for: active research weeks where Houston is dispatching many experiments
- Cost: continuous burn, but no cold-start latency between dispatches

**Save Credits Mode:**
- When current run finishes, full backup → integrity check → stop pod
- Pod can be restarted later from the network volume
- Best for: tight budgets, weekend pauses, post-experiment cooldown
- Cost: $0 between runs, but ~30-90 sec startup cost when restarted

**Serverless mode is always implicit "save credits"** — functions auto-stop when the call returns. No toggle needed.

**Hybrid pattern (recommended):**
- One always-on Pod (RunPod) in Proactive Mode for the active research thread (currently the H200)
- Serverless endpoints (RunPod) for everything bursty / parallel / low-duty-cycle (PDF QA, anomaly batches, claims audits)
- CPU pods or CPU serverless for non-tensor work (LaTeX compile, cross-match, paper formatting)

### 24.6 Cost Tracking (single-provider, simpler aggregation)

```
Today's cost: $14.40
  · RunPod Pod (bigbounce-h200): $14.10
  · RunPod Serverless (anomaly-detector × 47 calls): $0.28
  · RunPod Serverless (pdf-qa × 12 calls): $0.02
  · Vercel Sandbox (vibe coding): $0.00
```

Per-experiment cost is logged to the experiments table with mode attribution (`pod` vs `serverless` vs `cpu-pod` vs `cpu-serverless`). Top-N most expensive experiments view shows which mode each ran on. Burn rate is tracked daily and forecasted to credits-zero per §41.

---

## 25. Agent Communication — Multi-Agent Activity Feed

The orchestrator chat panel is the "talk to me" surface — the Director (Houston) typing and the Lab Orchestrator responding. **The activity feed is the "watch the team" surface** — every meaningful action by every agent in the lab, streamed to a unified chronological log. Houston can scroll through and see exactly what the leads and workers are doing in real time, even when he's not the one driving.

Reference inspiration: indydevdan's UI-agents Pi project. When workers failed in his demo, the lead agents proactively took over to ensure "tilldone" tasks completed. Hubify Labs needs that same trust — Houston should never have to babysit failed workers.

### 25.1 The Comms Schema

Every agent action emits a `comms_event`:

```typescript
comms_events: defineTable({
  event_id: v.string(),
  lab_id: v.string(),
  agent_id: v.string(),                   // who acted
  agent_role: v.string(),                 // orchestrator | lead | worker
  agent_lead: v.optional(v.string()),     // worker's lead (for color coding)

  type: v.string(),                       // see TYPES below
  severity: v.string(),                   // info | warn | crit | success
  message: v.string(),                    // 1-2 line human-readable
  details: v.optional(v.any()),           // structured payload

  task_id: v.optional(v.string()),        // link to task (if any)
  experiment_id: v.optional(v.string()),  // link to experiment (if any)
  parent_event_id: v.optional(v.string()),// thread/reply
  cost_usd: v.optional(v.number()),       // cost incurred by this action

  timestamp: v.string(),
  duration_ms: v.optional(v.number()),

  // For full text + filter search
  text_search: v.string(),                // pre-built search blob
}).index("by_lab_time", ["lab_id", "timestamp"])
  .index("by_agent_time", ["agent_id", "timestamp"])
  .index("by_task", ["task_id"])
  .index("by_experiment", ["experiment_id"])
  .index("by_severity", ["severity"])
  .searchIndex("by_text", { searchField: "text_search" }),
```

### 25.2 Event Types

The full taxonomy. Each type has a default severity and color treatment:

| Type | Severity | Description |
|---|---|---|
| `task.accepted` | info | Agent picked up a task |
| `task.started` | info | Work begun on a task |
| `task.progress` | info | Mid-task update (10%, 25%, 50%, etc.) |
| `task.completed` | success | Task finished successfully |
| `task.failed` | crit | Task hit an error |
| `task.escalated` | warn | Task bumped up to higher tier |
| `task.takeover` | warn | Lead taking over from failed worker (tilldone trigger) |
| `task.commented` | info | Agent left a comment on a task |
| `task.reviewed` | info | Agent reviewed another's work |
| `experiment.started` | info | Experiment kicked off |
| `experiment.qc_pass` | success | QC gate passed |
| `experiment.qc_fail` | warn | QC gate failed, retrying |
| `experiment.complete` | success | Full Houston Method protocol done |
| `delegation` | info | Agent delegated work to subordinate |
| `request.help` | info | Agent asked another for help |
| `request.review` | info | Agent asked another to review |
| `escalation.director` | warn | Issue bumped to Houston |
| `learning.added` | info | New learning added to memory |
| `decision` | info | Lab-level decision recorded |
| `memory.update` | info | Memory layer updated |
| `compute.spawn` | info | Pod or function started |
| `compute.terminate` | info | Pod or function stopped |
| `cost.alert` | warn | Spending threshold hit |
| `standup.opened` | info | Standup meeting started |
| `standup.closed` | info | Standup meeting ended |
| `system.heartbeat` | info | Watchdog tick |

### 25.3 The Tilldone Pattern

**Hard rule:** when a worker fails, the lead agent automatically takes over the task. The task stays in "running" status throughout. Workers cannot orphan failures.

```
WORKER FAILS
  ↓
[1] Capture failure context (traceback, last command, env state)
[2] Emit `task.failed` event with full context
[3] Notify the lead agent who owns this worker
[4] Lead agent receives the task with the failure context attached
[5] Emit `task.takeover` event — visible in activity feed
[6] Lead either:
    a) Fixes the issue and re-runs (most common)
    b) Spawns a different worker with adjusted parameters
    c) Does the work directly using its higher-tier model
    d) Escalates to orchestrator if all 3 above fail
[7] Task stays "running" until either:
    - Successfully completes
    - Escalates to Director (Houston)
    - Manually killed by Houston
```

The orchestrator NEVER lets a task die silently. The whole point is "tilldone" — the platform refuses to mark anything failed without first attempting recovery.

### 25.4 Color Coding (CLI-style activity feed)

The activity feed is the ONE place where the single-accent rule relaxes slightly. Color is functional here, not decorative:

| Element | Color | Use |
|---|---|---|
| Orchestrator events | sage accent (`--accent`) | top-level coordination |
| Lead events | text-bright | per-domain coordination |
| Worker events | text-muted | grunt work |
| Success | sage accent | completed steps |
| Warning | warn (muted amber) | takeover, escalation, retry |
| Critical | crit (muted red) | unrecoverable failures |
| System | text-dim | heartbeats, watchdogs |

Even with this "expanded" palette, it's still grayscale + sage + 2 muted statuses. No new colors introduced.

### 25.5 Activity Feed UI Surface

Two places the feed is visible:

**A. Bottom dock (always available, like Cursor's terminal):**
- Toggle with `Cmd+`` (backtick) — the standard Cursor shortcut
- Resizable horizontal strip at the bottom of the workspace
- Live tail of all events for the current lab
- Filter chips: Orchestrator / Leads / Workers / Failures / Tasks / Experiments
- Pause toggle (freeze the tail to read)
- Export to file
- Click any event → drilldown in the right preview area

**B. Dedicated Comms view (full screen):**
- Sidebar nav item "Comms" or "Activity"
- Full-page activity feed with advanced filters
- Date range picker
- Group by agent / type / time / task
- Search across all events
- Pin events for follow-up

### 25.6 The Comms Feed is the Source of Truth for "What Did the Team Do Today"

When Houston asks the orchestrator "what happened overnight", the answer comes from the comms feed, not from the orchestrator's own memory of the conversation. Every Houston-facing summary that describes agent activity should be GENERATED FROM the comms feed at query time. This guarantees correctness.

---

## 26. Task Review Pipeline & Activity Threads

Tasks are not TODOs. They are first-class objects with reviewers, comments, history, and cross-agent collaboration. Houston wants the Tasks view to feel like a real research team's project board, not a sticky-note app.

### 26.1 Extended Tasks Schema

```typescript
tasks: defineTable({
  task_id: v.string(),
  lab_id: v.string(),
  title: v.string(),
  description: v.string(),
  type: v.string(),                       // experiment | review | analysis | infra | doc | bug
  status: v.string(),                     // backlog | in_progress | review | done | blocked
  priority: v.string(),                   // p0 | p1 | p2 | p3
  source: v.string(),                     // standup | director | worker | cron | failure_recovery

  assigned_to: v.string(),                // primary owner (agent_id)
  assigned_by: v.string(),                // who assigned
  reviewers: v.array(v.string()),         // who must review before "done"
  required_review_count: v.number(),      // how many reviews needed (0 = no review)

  parent_task_id: v.optional(v.string()), // for subtasks
  blocks: v.array(v.string()),            // task IDs this blocks
  blocked_by: v.array(v.string()),        // task IDs blocking this

  created_at: v.string(),
  due_at: v.optional(v.string()),
  started_at: v.optional(v.string()),
  completed_at: v.optional(v.string()),

  estimated_cost_usd: v.optional(v.number()),
  actual_cost_usd: v.optional(v.number()),

  tags: v.array(v.string()),
  embedding: v.optional(v.array(v.number())),
}).index("by_lab_status", ["lab_id", "status"])
  .index("by_assigned", ["assigned_to"])
  .index("by_reviewer", ["reviewers"])
  .vectorIndex("by_embedding", { vectorField: "embedding", dimensions: 1536 }),

task_comments: defineTable({
  comment_id: v.string(),
  task_id: v.string(),
  agent_id: v.string(),                   // commenter
  body: v.string(),                       // markdown
  comment_type: v.string(),               // comment | review | question | answer
  review_verdict: v.optional(v.string()), // approved | needs_changes | blocked | escalate
  parent_comment_id: v.optional(v.string()),  // threading
  created_at: v.string(),
  edited_at: v.optional(v.string()),
}).index("by_task_time", ["task_id", "created_at"]),

task_reviews: defineTable({
  review_id: v.string(),
  task_id: v.string(),
  reviewer_agent_id: v.string(),
  verdict: v.string(),                    // approved | needs_changes | blocked | escalate
  reasoning: v.string(),
  reviewed_at: v.string(),
  duration_ms: v.number(),
}).index("by_task", ["task_id"])
  .index("by_reviewer", ["reviewer_agent_id"]),
```

### 26.2 The Review Pipeline

When a task is moved to `status: review`, the platform automatically:

1. Identifies reviewers (default: 1 lead + 1 worker from a different domain)
2. Creates `request.review` events for each reviewer
3. Each reviewer reads the work, leaves a comment, and submits a verdict
4. If `required_review_count` is met AND all verdicts are `approved`: status → `done`
5. If any verdict is `needs_changes`: status → `in_progress`, original assignee notified
6. If any verdict is `blocked`: status → `blocked`, blocker noted, escalates if not resolved in 1h
7. If any verdict is `escalate`: status → escalated to lead, then orchestrator, then Director

**Reviewer assignment heuristics:**
- High-priority tasks → reviewed by orchestrator + 1 lead
- Medium tasks → reviewed by 1 lead + 1 worker
- Low tasks → reviewed by 1 worker peer
- Paper claims → reviewed by paper-lead + research-lead + skeptic-worker (3 reviews)
- Experiment results → reviewed by anomaly-lead + cosmology-worker
- Infra changes → reviewed by gpu-manager-lead

The orchestrator can override default assignment when context warrants.

### 26.3 Tasks UI Surface

The Tasks view supports THREE display modes:

**A. Kanban view (default):**
- Columns: Backlog / In Progress / Review / Blocked / Done
- Cards show: title, assignee avatar, priority dot, comment count badge, review count badge
- Click card → opens detail panel on the right
- Drag-drop to change status

**B. List view:**
- Dense rows with sortable columns (title, assignee, status, priority, due, cost, last update)
- Notion-style grouping: by status, by assignee, by lead, by lab area, by tag, by priority
- Group headers show count + aggregate stats (total cost, avg duration, etc.)
- Inline expand for comments
- Bulk actions

**C. Activity view:**
- CLI-style chronological feed of all task-related events
- Same color coding as the Comms feed (§25.4)
- Scoped to tasks (not all comms — for that use the Comms view)
- Click any event → opens the source task in a side panel

A toggle in the top of the Tasks view switches between the three modes. The user's last-used mode is remembered per lab.

### 26.4 Task Detail Panel

When a task is opened (click in any view), the right preview area shows:

```
+---------------------------------------------+
| T-104: Re-run Planck galactic mask          |
| anomaly-lead · p1 · in_progress · 2h ago    |
+---------------------------------------------+
| Description                                 |
| Re-run Planck galactic mask sky scan with   |
| the corrected dust template. Previous QC    |
| failed at val_loss=22,420.                  |
+---------------------------------------------+
| Reviewers (1 of 2 required)                 |
| ✓ research-lead — approved                  |
| ⏰ skeptic-worker — pending                  |
+---------------------------------------------+
| Comments (4)                                |
| anomaly-lead · 1h ago                       |
|   Reduced batch size from 32 → 16 to fit    |
|   the new mask layer. ETA 12 min.           |
| ─                                           |
| research-lead · 45m ago [REVIEW: APPROVED]  |
|   Mask layer looks correct. Cross-checked   |
|   against Planck 2018 PR2 mask.             |
| ─                                           |
| anomaly-worker · 30m ago                    |
|   Run started at 04:13, now 67% complete.   |
|   val_loss trending down (22420 → 18.3).    |
| ─                                           |
| anomaly-lead · 5m ago                       |
|   Almost done. Will write QC report when    |
|   complete.                                 |
+---------------------------------------------+
| History                                     |
| 04:13  task created by orchestrator         |
| 04:13  assigned to anomaly-lead             |
| 04:14  anomaly-lead spawned anomaly-worker  |
| 04:15  in_progress                          |
| 05:42  research-lead reviewed: approved     |
+---------------------------------------------+
```

### 26.5 Comments are Comms Events

Every task comment also emits a `task.commented` event in the Comms feed (§25). This means a single source of truth — the comms feed shows the comment, the task detail panel shows the comment, both reading from the same record.

Same for reviews — each review emits a `task.reviewed` event.

### 26.6 Director-Assigned Tasks

When a task originates from Houston (the Director), it's tagged `source: director`. These tasks bypass review by default — the Director's word is authoritative. But the orchestrator may STILL spawn a sanity-check review if the task description is ambiguous, in which case the review verdict is purely advisory.

When a task is escalated TO the Director (orchestrator can't decide), it appears in the Director view's "Needs your review" card with the full context attached.

---

## 27. All-Hands Standups (3x/day Cron)

Random asynchronous activity is one mode of agent coordination. Structured periodic standups are another. Hubify Labs runs **3 standups per day** in every active lab — morning, mid-day, evening — to enforce coordination, surface blockers proactively, and create natural review/help moments.

### 27.1 Standup Schedule

Each lab gets 3 standups per day at user-configurable local times. Defaults:

- **Morning standup** — 8:07 AM local
- **Mid-day standup** — 13:13 PM local
- **Evening standup** — 18:23 PM local

(Off-the-hour minutes per gstack convention to avoid the :00/:30 cron storm.)

The 3-standup pattern is mandatory for active labs. Inactive labs skip standups until reactivated.

### 27.2 Standup Workflow

```
STANDUP CRON FIRES
  ↓
[1] Orchestrator opens the meeting
    Creates a `standup_session` record
    Emits `standup.opened` to comms feed
  ↓
[2] Roll call
    Orchestrator pings each agent in the lab
    Each agent acks (or marks unavailable)
  ↓
[3] Round-robin reports
    For each agent in turn:
      a) "What did you work on since the last standup?"
      b) "What are you working on now / next?"
      c) "What do you need help with from another agent?"
      d) "Any blockers?"
    Each report is captured as a `standup_report` record
  ↓
[4] Discussion phase
    Agents can directly request help from each other
    "anomaly-worker → review-worker: can you check my QC threshold?"
    "anomaly-lead → research-lead: I disagree on EXP-057 strategy, can we discuss?"
    Each request becomes a NEW task in the Tasks view
  ↓
[5] Action item extraction
    Orchestrator post-processes the transcript:
      - Extract all "I need X from Y" requests as new tasks
      - Extract all blockers as new alerts
      - Extract all decisions as decision_log entries
      - Identify any disagreements that need Director input
  ↓
[6] Director assignment (if needed)
    If the standup surfaced something the agents can't resolve:
      - Create a Director task with the standup context
      - Tag as p1 high-priority review
      - Show in Director view's "Needs your review" card
  ↓
[7] Transcript saved
    Full transcript saved to:
    - <lab>/.hubify-labs/standups/YYYY-MM-DD_HH-MM.md
    - Convex `standup_sessions` table
  ↓
[8] Standup closed
    Emits `standup.closed` to comms feed
    Notification to Director (low-priority unless escalated)
```

### 27.3 Standup Schema

```typescript
standup_sessions: defineTable({
  session_id: v.string(),
  lab_id: v.string(),
  scheduled_for: v.string(),              // morning | midday | evening
  started_at: v.string(),
  ended_at: v.string(),
  attendees: v.array(v.string()),         // agent_ids who attended
  absent: v.array(v.string()),            // agent_ids unavailable
  transcript_md: v.string(),              // full markdown transcript
  action_items_created: v.number(),       // tasks generated
  blockers_surfaced: v.number(),
  decisions_made: v.number(),
  director_escalations: v.number(),
  cost_usd: v.number(),
}).index("by_lab_time", ["lab_id", "started_at"]),

standup_reports: defineTable({
  report_id: v.string(),
  session_id: v.string(),
  agent_id: v.string(),
  did_since_last: v.string(),
  doing_now: v.string(),
  needs_help: v.array(v.object({
    from_agent: v.string(),
    request: v.string(),
  })),
  blockers: v.array(v.string()),
  reported_at: v.string(),
}).index("by_session", ["session_id"])
  .index("by_agent_time", ["agent_id", "reported_at"]),
```

### 27.4 Standup UI Surface

A new view in the sidebar: **Standups** (or under Comms as a sub-tab).

```
+---------------------------------------------+
| Standups (today)                            |
+---------------------------------------------+
| Morning · 08:07 · ✓ complete                |
|   16 attended · 0 absent · 4 action items   |
|   3 blockers · 1 director escalation        |
|   [view transcript →]                       |
|                                             |
| Mid-day · 13:13 · ⏰ in 4h                  |
|   scheduled                                 |
|                                             |
| Evening · 18:23 · ⏰ in 9h                  |
|   scheduled                                 |
+---------------------------------------------+
| Recent transcripts                          |
|                                             |
| 2026-04-08 morning                          |
|   anomaly-lead: "EXP-057 still failing —    |
|   research-lead, can we rethink the         |
|   approach?" → director task created        |
|                                             |
| 2026-04-07 evening                          |
|   gpu-manager-lead: "Pod disk at 92%, need  |
|   to clean before tomorrow" → backup-worker |
|   assigned                                  |
+---------------------------------------------+
```

### 27.5 Standup Costs

Each standup runs 1 orchestrator + 16 agent reports + 1 post-processing pass. Cost estimate:

- Orchestrator opening + closing: ~$0.05
- 16 agent reports × $0.02 each = $0.32
- Post-processing extraction: ~$0.10
- **Total per standup: ~$0.50**
- 3 standups/day × 30 days = ~$45/month per lab

Cheap relative to the coordination value. The cost is logged to `standup_sessions.cost_usd`.

### 27.6 What Houston Sees

By default, standups run silently. Houston only gets notified when:
- A standup escalates something to the Director
- A standup creates a high-priority task for him
- A standup surfaces an unresolvable disagreement

He can ALWAYS browse past standups via the Standups view, but the platform doesn't push them to his attention unless action is needed. **Quiet by default, loud when it matters.**

### 27.7 Why Standups Work

The pattern is borrowed from real distributed teams. Three things it gives the platform:
1. **Cadence** — agents have a rhythm beyond ad-hoc tasks
2. **Forced coordination** — leads and workers explicitly hand off and request help
3. **Insight mining** — the orchestrator gets a regular opportunity to extract patterns from the team's collective state without being prompted

The standup is the primary mechanism by which the platform self-monitors and self-corrects. Without it, agents drift. With it, agents stay aligned.

---

## 28. Patterns Borrowed from Paperclip (NOT a Fork)

A background research agent studied **paperclipai/paperclip** in depth (1,337-line analysis at `bigbounce/project-context/paperclip_patterns_study.md`) and surfaced patterns we should adopt. **We are NOT cloning or forking paperclip** — we are borrowing 5 specific architectural patterns that will make Hubify Labs simpler, more reliable, and more correct.

This section is the canonical reference for which paperclip patterns we adopt and how they revise the earlier §25-§27 specs.

### 28.1 Pattern 1: Unify Tasks + Comms + Standups + Reviews into "Issues"

**Paperclip's biggest insight:** every coordination object — tasks, standups, code reviews, hires, blockers, research pipelines — is the same `issues` table with a `kind` discriminator. Same lifecycle, same comment thread, same audit trail, same routing logic.

**What this means for Hubify Labs:** the §25/§26/§27 schemas (`tasks`, `task_comments`, `task_reviews`, `standup_sessions`, `standup_reports`, plus `comms_events`) are too many tables. Collapse them.

**Revised primary schema (replaces parts of §26):**

```typescript
issues: defineTable({
  issue_id: v.string(),
  lab_id: v.string(),

  // The discriminator — every issue is one of these
  kind: v.union(
    v.literal("task"),                  // standard work item
    v.literal("experiment"),            // a GPU/MCMC run
    v.literal("review"),                // a review request
    v.literal("standup"),               // a standup session
    v.literal("decision"),              // a lab decision to be made
    v.literal("blocker"),               // something blocking other work
    v.literal("escalation"),            // bumped to higher tier
    v.literal("hire"),                  // promote/demote/onboard agent
    v.literal("question"),              // open question for the lab
    v.literal("alert"),                 // a system alert
  ),

  title: v.string(),
  body: v.string(),                     // markdown
  status: v.string(),                   // backlog | in_progress | review | blocked | done | cancelled
  priority: v.string(),                 // p0 | p1 | p2 | p3

  // Routing
  assigned_to: v.optional(v.string()),  // primary owner agent
  reports_to: v.optional(v.string()),   // where escalation lands (paperclip pattern)
  reviewers: v.array(v.string()),
  required_review_count: v.number(),

  // Origin (paperclip pattern)
  origin_kind: v.union(
    v.literal("user"),                  // human created
    v.literal("agent"),                 // agent created
    v.literal("routine_execution"),     // a scheduled cron fired this
    v.literal("standup_extraction"),    // came from a standup action item
    v.literal("failure_recovery"),      // came from a takeover
    v.literal("cross_lab_link"),        // came from another lab
  ),
  origin_id: v.optional(v.string()),    // which routine/standup/parent issue

  // Relations
  parent_issue_id: v.optional(v.string()),
  blocks: v.array(v.string()),
  blocked_by: v.array(v.string()),

  // Status timestamps
  created_at: v.string(),
  started_at: v.optional(v.string()),
  due_at: v.optional(v.string()),
  completed_at: v.optional(v.string()),

  // Cost tracking
  estimated_cost_usd: v.optional(v.number()),
  actual_cost_usd: v.optional(v.number()),

  tags: v.array(v.string()),
  embedding: v.optional(v.array(v.number())),
}).index("by_lab_kind_status", ["lab_id", "kind", "status"])
  .index("by_assigned", ["assigned_to"])
  .index("by_reports_to", ["reports_to"])
  .index("by_origin", ["origin_kind", "origin_id"])
  .vectorIndex("by_embedding", { vectorField: "embedding", dimensions: 1536 }),
```

**`task_comments` and `task_reviews` from §26 collapse into one `issue_comments` table** that handles both regular comments AND review verdicts via a `comment_kind` field. **`standup_sessions`** becomes an issue with `kind: "standup"`. **`standup_reports`** become comments on the standup issue, one per agent. **All of §25's `comms_events`** are derived from issue mutations, not a separate table.

This removes ~6 tables, ~30 indexes, and dramatically simplifies queries.

### 28.2 Pattern 2: Single `enqueueWakeup()` Chokepoint

**Paperclip pattern:** every path that spawns agent work goes through ONE function — `enqueueWakeup()` in `server/src/services/heartbeat.ts:3613`. This function handles:
- Coalescing (if the same agent is already pending, merge instead of duplicating)
- Budget checks (refuse if user is over their cost limit)
- Deferral (sleep until conditions are met)
- Audit logging (every wakeup is logged)
- Idempotency (same trigger fires once, not N times)

**Why this matters:** without a chokepoint, every place in the codebase that spawns an agent has to re-implement coalescing, budgeting, and audit. They will do it inconsistently. Bugs will appear. Paperclip's solution: ONE function, period.

**For Hubify Labs:** all agent spawns go through `enqueueAgentWork()`:

```typescript
// Single entry point for spawning any agent work
async function enqueueAgentWork(args: {
  agent_id: string,
  issue_id: string,
  trigger: "user" | "agent_delegation" | "routine" | "watchdog" | "review_request" | "takeover",
  defer_until?: string,                 // optional: wait until this time
  coalesce_key?: string,                // optional: merge with pending of same key
  budget_check: boolean,                // skip for system-critical work
  audit_message: string,
}): Promise<{ wakeup_id: string, status: "queued" | "coalesced" | "deferred" | "rejected" }>
```

NO other function in the platform spawns agent work directly. The orchestrator, routines, watchdogs, takeovers — all of them call `enqueueAgentWork()`. This is enforced by code review (or eventually by a lint rule).

### 28.3 Pattern 3: Atomic Checkout via UPDATE-WHERE-STATUS

**Paperclip pattern:** when two agents race for the same issue, the resolution is atomic at the SQL/Convex layer. The pattern at `server/src/services/issues.ts:1786`:

```typescript
// Both agents call this. Only one wins.
async function checkoutIssue(issue_id: string, agent_id: string) {
  const result = await db.patch(issue_id, {
    assigned_to: agent_id,
    status: "in_progress",
    started_at: now(),
  }).where(q => q.eq(q.field("status"), "backlog"));
  // ↑ The .where() clause is atomic with the patch
  // If status was already "in_progress", patch returns 0 rows affected
  // The losing agent gets a 409-equivalent and retries with a different issue

  if (result.matched === 0) throw new ConflictError(409);
  return result;
}
```

**No locks. No Redis. No distributed coordination.** Just an atomic UPDATE-WHERE that lets the database arbitrate. Convex supports this pattern via `db.patch().where()`.

**For Hubify Labs:** every issue checkout, status transition, and review claim uses this pattern. No agent can race past another. The losing agent gets a 409 and picks a different issue.

### 28.4 Pattern 4: Routines Are the Standup Pattern (No Separate Schema)

**Paperclip's most counterintuitive finding:** there is no `standups` table. There is no "meeting room" entity. Standups are just **routines** — scheduled work that fires by creating an issue with `originKind: "routine_execution"`, guarded by a partial unique index that prevents double-fire.

**The whole standup workflow** is:
1. Routine fires (cron tick)
2. Routine creates an issue with `kind: "standup"`, `origin_kind: "routine_execution"`
3. Each agent posts a comment on the standup issue (their report)
4. Action items become NEW issues with `parent_issue_id: <standup_issue_id>` and `origin_kind: "standup_extraction"`
5. Standup issue gets marked `done` when post-processing finishes

**This collapses §27** (which had its own `standup_sessions` and `standup_reports` tables) into the unified issues schema. No new tables.

```typescript
routines: defineTable({
  routine_id: v.string(),
  lab_id: v.string(),
  name: v.string(),                     // "standup-morning", "idle-pod-watchdog", etc.
  cron: v.string(),                     // "7 8 * * *" for 8:07 AM daily
  enabled: v.boolean(),
  next_fire_at: v.string(),
  last_fired_at: v.optional(v.string()),
  guard_key: v.string(),                // partial unique index on (routine_id, fire_window) prevents double-fire
  payload: v.any(),                     // template for the issue this routine creates
}).index("by_next_fire", ["next_fire_at"])
  .index("by_lab", ["lab_id"]),
```

The morning standup is just `routines` row #47 with cron `"7 8 * * *"` and a payload that says "create an issue with kind=standup, body=<template>, assignees=<all active agents in lab>".

**The same pattern handles:**
- Standups (3x/day)
- Idle GPU watchdog (every 5 min)
- Queue health watchdog (every hour)
- Novelty re-review schedule (per-claim cron)
- Backup verification (nightly)
- Memory cleanup (weekly)

**One routines schema. One enqueue mechanism. One issue type for the result.** Massively simpler than spec'ing each watchdog as its own bespoke system.

### 28.5 Pattern 5: Tilldone via Same-Agent Retry + Stale-Checkout Adoption

**This is the finding that revises §25.3.** I originally spec'd "tilldone" as "when a worker fails, the lead automatically takes over." Paperclip does it differently — and the paperclip pattern is more correct.

**Paperclip pattern:** there is no "lead takes over" code path. Instead:
1. Worker fails on issue X
2. Issue X is left in `in_progress` with `assigned_to: <worker>`, `last_heartbeat: <timestamp>`
3. The worker's NEXT heartbeat re-checks issue X
4. If the failure was transient (OOM, network blip, etc.), it retries
5. If the worker is dead/missing/stuck, the **stale-checkout adoption** logic kicks in: ANY agent (including a lead OR another worker OR the same worker on a fresh process) can adopt issue X if `now() - last_heartbeat > stale_threshold`
6. Adoption is atomic via the same UPDATE-WHERE pattern as checkout

**Why this is better:**
- **No special lead-takeover code path.** Recovery uses the SAME atomic checkout pattern as initial assignment. Less code = fewer bugs.
- **Recovery agent is whoever is available**, not necessarily the lead. The lead can still adopt if it wants to (its heartbeat will see the stale checkout), but workers can also retry their own work.
- **Failures don't have to escalate.** Most failures resolve by retry. Only persistent failures escalate.

**Revised tilldone protocol (replaces §25.3):**

```
WORKER FAILS on ISSUE X
  ↓
Issue stays in_progress, last_heartbeat is now stale
  ↓
WAIT for next heartbeat tick
  ↓
[1] Same worker's heartbeat fires (most common)
    Re-checks own checked-out issues
    Finds X still assigned, retries with backoff
    If success → mark done
    If fail again → repeat with longer backoff
  ↓
[2] OR a different agent's heartbeat fires
    Checks for stale checkouts (last_heartbeat > stale_threshold)
    Atomically adopts via UPDATE-WHERE-status
    Continues the work from where it stopped (using checkpoint)
  ↓
[3] OR after N retries with no progress
    Issue auto-escalates: kind changes from "task" to "escalation"
    reports_to field routes to lead → orchestrator → director
```

**The "lead takes over" model in §25.3 is REPLACED by this stale-checkout adoption model.** It's simpler, more general, and matches paperclip's proven design. We keep the "tilldone" name because it's still the core promise: nothing dies silently. The mechanism is just different.

### 28.6 Pattern 6: Escalation is Prompt-Driven, Not Code-Driven

**Paperclip pattern:** there is no `escalateToLead()` function. There is no escalation state machine. Escalation is entirely **prompt behavior** with one schema field: `agents.reports_to`.

When an agent is stuck, its system prompt says "if you cannot resolve this in N attempts, change the issue's `reports_to` field to your boss's agent_id and add a comment explaining why". The boss's next heartbeat sees the issue, picks it up, and either resolves or re-escalates.

**Why this is better:**
- Escalation logic lives in PROMPTS, not in TypeScript. Easier to tune per agent personality.
- No state machine to debug. No "stuck in escalation" bugs.
- Adding new escalation paths = adding new lines to the agent's system prompt, not new code.

**For Hubify Labs:** we add a `reports_to` field to the `agents` table (already in §3 implicitly via the lead/worker hierarchy). Agent system prompts include the escalation rule as the LAST instruction:

```
When you cannot resolve an issue after 3 attempts OR the issue requires
authority above your tier:
  1. Add a comment to the issue explaining what you tried
  2. Change the issue's reports_to field to: <YOUR_LEAD>
  3. Set status to "blocked"
  4. The boss's next heartbeat will see it within 5 minutes
```

**No `escalate()` function.** Just a prompt rule + a schema field.

### 28.7 Pattern 7: AGENTS.md as the Router (Markdown, Not Code)

**Paperclip pattern:** the highest-level routing decision (which department/team gets a new issue) is made by reading a **markdown file** — `server/src/onboarding-assets/ceo/AGENTS.md` — fresh on every CEO heartbeat. Not a TypeScript function. Not a database table. A markdown file.

**Why this is better:**
- Houston (the human) can edit the routing rules directly in plain English
- Changes don't require a code deploy
- The agent reads it like a human reads a wiki — explainable and debuggable
- New agents are added by appending to the file, not by writing a registration function

**For Hubify Labs:** every lab has a `<lab>/AGENTS.md` file that the lab orchestrator reads on every heartbeat. The file describes:
- Each agent's name, role, model, and current responsibilities
- Each agent's expertise and reasoning level
- Which agent to route which kind of work to
- Cross-agent collaboration patterns

This is **already mentioned in PRD §20.10** as a static instruction file. §28.7 promotes it to be the PRIMARY routing mechanism, not a secondary reference. The orchestrator's system prompt is: "On every heartbeat, re-read AGENTS.md, then decide what to do."

### 28.8 Pattern 8: @AgentName Mention Extraction

**Paperclip pattern at `server/src/services/issues.ts:2309`:** when an agent writes a comment, a regex extracts `@agent_name` mentions, dedups them via a `Map`, and creates wakeup requests for each mentioned agent. Agents never wake themselves (the Map skips self-mentions).

**For Hubify Labs:** add this exact pattern to every comment write. When `paper-lead` writes "@research-lead can you check this?", the platform automatically:
1. Parses the mention
2. Calls `enqueueAgentWork({ agent_id: "research-lead", issue_id: <this_issue>, trigger: "agent_delegation" })`
3. The mentioned agent's next heartbeat sees the wakeup and the comment

**Done.** No DM system, no notification system, no inbox. Just `@mentions` in comments, parsed by regex, routed by `enqueueAgentWork()`. Identical to how Slack/GitHub/Linear work.

### 28.9 Pattern 9: Two-Tier Event Storage

**Paperclip pattern:** events live in two places by intent, not by accident:

1. **`activity_log`** — one row per durable mutation (`issue_created`, `comment_added`, `status_changed`). Cheap, indexed, queried for the user-facing activity feed. ~500 bytes per row.

2. **`heartbeat_run_events`** — per-agent-run microtimeline of every prompt sent, every tool call, every model response, every retry. Detailed, only queried for debugging. Stored in a separate table so it doesn't bloat `activity_log` queries.

3. **`RunLogStore` (blob)** — raw stdout/stderr/agent-output. Stored as blobs in Convex File Storage. Queried only when a user clicks "show full output" in the UI.

**For Hubify Labs:** the §25 `comms_events` table is the equivalent of `activity_log` (cheap, user-facing). We ADD a separate `agent_run_events` table for the per-run microtimeline (detailed, debug-only) and a `run_logs` blob store for raw output. Three tiers, three purposes.

This means the user-facing comms feed stays fast (it queries `comms_events` only) and the debugging surface is deep when needed.

### 28.10 What We Are NOT Borrowing from Paperclip

Honesty about scope:

- **The CEO/department metaphor.** Paperclip is built around "company OS" — CEO, departments, hires, fires. Hubify Labs is research-focused. We use "lab orchestrator" and "leads" instead.
- **The execution decisions schema with review/approval state machine.** Our review pipeline (§26.2) is simpler and we don't need the same depth.
- **Their entire Postgres backend.** We're on Convex. The patterns translate but the storage primitives don't.
- **The CEO-prompt-as-router complexity.** Paperclip's CEO prompt is hundreds of lines. Our `AGENTS.md` will be tighter and more focused.

### 28.11 Implementation Order

When we start building Hubify Labs from §12's implementation plan:

**Week 1:** Build the unified `issues` schema with the discriminator (Pattern 1). Get checkout/comments/status transitions working with atomic UPDATE-WHERE (Pattern 3).

**Week 2:** Add `enqueueAgentWork()` as the single chokepoint (Pattern 2). Refactor all agent spawn points to go through it.

**Week 3:** Add `routines` schema (Pattern 4). Implement standups + idle-pod watchdog as the first two routines.

**Week 4:** Implement stale-checkout adoption (Pattern 5). This is the tilldone mechanism.

**Week 5:** Add `@mention` extraction (Pattern 8) and AGENTS.md routing (Pattern 7).

**Week 6:** Add the two-tier event storage (Pattern 9). Wire the comms feed UI to `activity_log` (the cheap one).

These 6 weeks subsume parts of the original §12 implementation plan. The full reconciliation is left as TODO for the next PRD iteration.

---

## 29. Cross-Model Peer Review (CRITICAL — No Echo Chamber)

**Houston flagged this as CRITICAL on 2026-04-08.** The earlier sections of this PRD spec'd an agent hierarchy where the orchestrator (opus 4.6), all leads (sonnet 4.6), and all workers (haiku 4.5) run Anthropic models. **That is a one-model echo chamber and it must be fixed.** Houston has been doing cross-model peer review MANUALLY through the entire BigBounce project — every paper revision, every novelty claim, every architectural decision has been bounced off multiple models by hand. This has been **invaluable and crucial** to steering the research direction. The platform must automate it.

### 29.1 The Echo Chamber Problem

When every agent in the lab runs the same model family (Claude, in this case), the lab inherits that model family's blind spots, biases, and stylistic tendencies. Specifically:

- Model-specific factual errors get reinforced rather than caught
- Model-specific reasoning shortcuts go unchallenged
- Model-specific writing tendencies dominate every paper draft
- The "skeptic agent" pattern fails because the skeptic shares the same priors as the agent it's checking
- Novelty claims get validated by a model that may have the same gaps in literature awareness

Houston has explicitly called out that this PRD's author (Claude) has a built-in tendency to default to Anthropic models for every role. **The platform must architecturally fight this tendency.**

### 29.2 Required Provider Mix

Every active lab MUST have at least one agent from each of these provider categories:

| Category | Provider examples | Default role |
|---|---|---|
| **Primary reasoning** | Anthropic (Claude Opus/Sonnet) | orchestrator + most leads |
| **Cross-provider peer review** | OpenAI (GPT-5, GPT-5 Pro) | peer-review-gpt agent |
| **Long-context comparison** | Google (Gemini 2.5 Pro / Ultra) | peer-review-gemini agent |
| **Less-guardrailed reasoning** | xAI (Grok 4) | peer-review-grok agent |
| **Web-grounded fact check** | Perplexity (Sonar / Sonar Pro) | fact-check-perplexity agent |
| **Optional: open-weights** | DeepSeek / Qwen / Mistral / local | cost-control + sovereignty backup |

**The "at least one of each" rule is a hard floor, not a ceiling.** Heavy-research labs might have multiple agents per category. New labs default to one of each plus the standard Anthropic stack.

### 29.3 The Cross-Model Review Pipeline

When work needs review, the orchestrator picks reviewers from DIFFERENT providers by default:

```
WORK READY FOR REVIEW
  ↓
[1] Identify the work type
    Paper draft? Novelty claim? Architectural decision? Code change?
  ↓
[2] Pick reviewers from DIFFERENT providers
    Default heuristic: at least 1 non-Anthropic reviewer for any high-stakes work
    Specific patterns:
      - Paper drafts → 1 GPT + 1 Gemini + 1 Anthropic skeptic (3 reviewers)
      - Novelty claims → GPT search + Gemini search + Perplexity web search
      - Architectural decisions → 1 GPT (different reasoning style) + 1 Anthropic
      - Critical code changes → 1 GPT + 1 Anthropic
  ↓
[3] Each reviewer runs INDEPENDENTLY
    No reviewer sees another reviewer's output during their pass
    All reviewers get the same brief
  ↓
[4] Reviews collected
    Stored in issue_comments with comment_kind="review"
    Each review tagged with reviewer_provider field
  ↓
[5] ORCHESTRATOR INTERPRETATION PASS (the critical step)
    See §29.4 below
  ↓
[6] Synthesized report presented to Houston
    Full reviews available for drilldown
    Key disagreements flagged prominently
```

### 29.4 The Interpretation Pass

This is the most important part. The orchestrator does NOT just average the reviews or pick the majority verdict. It performs a **critical interpretation pass** that takes both validation and invalidation with appropriate skepticism.

**Rules the orchestrator follows:**

**For NEGATIVE feedback (refutations, novelty challenges, criticisms):**
1. Read the specific claim being made by the reviewer
2. For each negative claim, classify: FACT (verifiable) / OPINION (judgment call) / HALLUCINATION (likely model error)
3. For FACT claims: verify against actual sources before accepting. Reviewers can hallucinate prior work, misremember papers, or invent citations.
4. For OPINION claims: weight by reviewer track record + Houston's domain knowledge
5. For HALLUCINATION suspicions: explicitly flag and ask Houston to verify before letting the criticism affect the work
6. **Do not let external invalidation discourage the work prematurely.** Cross-check before acting.

**For POSITIVE feedback (validation, agreement, praise):**
1. Treat with EXTRA skepticism — overly optimistic flattery is often dubious
2. Demand concrete reasons before accepting
3. Look for the things the reviewer DIDN'T critique — those are the gaps
4. If the praise is generic ("great work!", "novel contribution"), discount heavily
5. If the praise is specific and load-bearing ("the f_NL = -35/8 derivation correctly handles the parameter-free constraint"), accept
6. **Do not accept praise as validation.** Demand the reviewer try to break the claim, not just nod at it.

**For DISAGREEMENTS between reviewers:**
1. Cross-model disagreement is **signal, not noise**
2. Surface it prominently to Houston instead of auto-resolving
3. Explain WHAT each reviewer said and WHY they disagree
4. Recommend a tiebreaker (third reviewer from yet another provider, or Houston's manual judgment)

**The orchestrator's output:**
```
## Cross-Model Review Summary — Paper 1 v2.2.1

**Reviewers:** GPT-5 (peer-review-gpt), Gemini 2.5 Pro (peer-review-gemini), Sonnet 4.6 (skeptic-anthropic)

### Validation
- All 3 reviewers agreed: f_NL = -35/8 derivation is correct
- 2 reviewers (GPT, Gemini) flagged Section 7 as "well-written" — taken with salt, no specific reason given
- All 3 reviewers agreed: 14 ECH barriers framework is internally consistent

### Negative claims worth investigating
- GPT: "Cai et al. 2024 already derived f_NL = -35/8 from a different bounce model"
  → VERIFICATION: searched arXiv for Cai 2024 + f_NL bounce. Found Cai 2024 paper. It derives f_NL ranges, NOT -35/8 specifically.
  → CONCLUSION: GPT misremembered. Claim DOES NOT hold. No action.
- Gemini: "Section 5.2 quintom-B contour plot may have an axis labeling error"
  → VERIFICATION: re-checked the figure source. Axis labels are correct.
  → CONCLUSION: Gemini hallucinated the error. No action.
- Sonnet skeptic: "f_NL triple role discussion in Section 7 may be overclaiming the link to PBH abundance"
  → VERIFICATION: re-read Section 7. The link IS qualified, but could be MORE qualified.
  → CONCLUSION: Valid concern. RECOMMENDED ACTION: add 1 sentence of qualification.

### Disagreements
- GPT thinks Section 6 needs more citations to ekpyrotic literature
- Gemini thinks Section 6 has too many citations and should be trimmed
- → DECISION REQUIRED: Houston, your call.

### Recommendation
2 of 3 negative claims were FALSE (model errors, not real issues). 1 of 3 was valid and is a cheap fix. The Section 6 disagreement is a real call for Houston. Overall the paper is in good shape — the reviewers found ONE real improvement to make.
```

This kind of interpretation is what Houston has been doing manually. The platform automates the FIRST PASS. Houston still has final say.

### 29.5 Cross-Model Provider Schema

```typescript
agents: defineTable({
  agent_id: v.string(),
  lab_id: v.optional(v.string()),         // null = global agent
  name: v.string(),
  role: v.string(),                        // orchestrator | lead | worker | reviewer | skeptic
  domain: v.string(),

  // Provider info — REQUIRED
  provider: v.union(
    v.literal("anthropic"),
    v.literal("openai"),
    v.literal("google"),
    v.literal("xai"),
    v.literal("perplexity"),
    v.literal("deepseek"),
    v.literal("mistral"),
    v.literal("local"),
    v.literal("openrouter"),               // wrapper for any of the above
  ),
  model: v.string(),                       // "claude-opus-4-6", "gpt-5-pro", "gemini-2.5-pro", etc.
  reasoning_level: v.string(),             // high | med | low

  // Cross-provider review eligibility
  can_review_for: v.array(v.string()),     // domains this agent can peer-review
  review_specialty: v.optional(v.string()),// "literature_search" | "claim_verification" | "code_review"

  reports_to: v.optional(v.string()),
  cost_per_1m_input: v.number(),           // for cost tracking
  cost_per_1m_output: v.number(),

  status: v.string(),
  created_at: v.string(),
}).index("by_lab_role", ["lab_id", "role"])
  .index("by_provider", ["provider"])
  .index("by_review_eligibility", ["can_review_for"]),

reviews: defineTable({
  review_id: v.string(),
  issue_id: v.string(),                    // which work is being reviewed
  reviewer_agent_id: v.string(),
  reviewer_provider: v.string(),           // duplicated for fast filtering
  reviewer_model: v.string(),
  brief: v.string(),                       // what the reviewer was asked to review
  output_md: v.string(),                   // raw review text
  verdict: v.string(),                     // approved | needs_changes | blocked | escalate
  duration_ms: v.number(),
  cost_usd: v.number(),
  reviewed_at: v.string(),
}).index("by_issue", ["issue_id"])
  .index("by_provider_time", ["reviewer_provider", "reviewed_at"]),

review_synthesis: defineTable({
  synthesis_id: v.string(),
  issue_id: v.string(),
  review_ids: v.array(v.string()),
  validations: v.array(v.string()),
  negative_claims_verified: v.array(v.object({
    reviewer_id: v.string(),
    claim: v.string(),
    classification: v.string(),            // FACT | OPINION | HALLUCINATION
    verification_action: v.string(),
    final_verdict: v.string(),             // accepted | rejected | needs_houston
  })),
  positive_claims_skepticism: v.array(v.object({
    reviewer_id: v.string(),
    claim: v.string(),
    skepticism_level: v.string(),          // generic | specific | load-bearing
    accepted: v.boolean(),
  })),
  disagreements: v.array(v.object({
    topic: v.string(),
    reviewers_disagreeing: v.array(v.string()),
    flagged_to_houston: v.boolean(),
  })),
  synthesized_at: v.string(),
  synthesizer_agent_id: v.string(),        // which agent ran the interpretation pass
}).index("by_issue", ["issue_id"]),
```

### 29.6 The Required Cross-Model Sub-Agents (per lab)

Every lab boots with these REQUIRED non-Anthropic peer review agents (in addition to the existing Anthropic orchestrator + leads + workers from §3):

| Agent name | Provider | Model (default) | Reasoning | Role |
|---|---|---|---|---|
| `peer-review-gpt` | OpenAI | GPT-5 | high | Cross-model peer review for paper drafts and novelty claims |
| `peer-review-gemini` | Google | Gemini 2.5 Pro | high | Long-context cross-checks, comparison tables, multi-paper synthesis |
| `peer-review-grok` | xAI | Grok 4 | med-high | Alternative reasoning, less-guardrailed perspective |
| `fact-check-perplexity` | Perplexity | Sonar Pro | med | Web-grounded fact checks, source verification, latest literature |
| `skeptic-cross` | Rotates | (random pick) | high | Plays devil's advocate, picked from a different provider each time |

These 5 agents are SHARED across all labs by default. Houston can add lab-specific ones. They are REQUIRED — you cannot create a lab without them. The lab template includes them automatically.

### 29.7 Review Cadence — Periodic, Not Constant

Cross-model review is **expensive** (each pass uses ~3 different provider APIs) and **noisy** (reviewers will hallucinate, repeat themselves, sometimes agree on wrong things). The cadence must be careful:

**Mandatory triggers (always run cross-model review):**
- Paper draft about to be submitted → MANDATORY full 3-reviewer pass
- Novelty claim being added → MANDATORY full pipeline (§22)
- Architectural decision being made → MANDATORY 1 GPT + 1 Anthropic
- Code change to a load-bearing system → MANDATORY 1 non-Anthropic

**Periodic triggers (configurable):**
- Daily fresh-eyes pass on lab state (runs once per day, picks 1 active issue, gets a non-Anthropic perspective)
- Weekly novelty re-review on top 5 contributions (rotates which provider)
- Monthly "audit pass" — random sample of 10 closed issues from the month, cross-reviewed for missed errors

**On-demand triggers:**
- Houston explicitly asks "what would GPT think about this?"
- Orchestrator detects high-stakes work and proactively requests review

**What NOT to do:**
- Cross-review every comment (too expensive, too noisy)
- Cross-review tiny code edits (overkill)
- Cross-review the same work multiple times in a day (diminishing returns)

### 29.8 Cost Management Across Providers

Cross-model review will increase costs. Tracked separately:

```
Today's cost: $24.80
  · Anthropic (Claude): $14.20  (orchestrator + leads + workers)
  · OpenAI (GPT-5): $5.40       (peer-review)
  · Google (Gemini): $3.10      (peer-review)
  · xAI (Grok): $1.40           (peer-review)
  · Perplexity (Sonar): $0.70   (fact-check)
```

Per-provider budget caps configurable. Houston can set "OpenAI: $50/month max" and the platform refuses additional reviews from that provider after the cap is hit. A warning fires at 80%.

The Settings page surfaces:
- API key for each provider
- Per-provider monthly budget
- Per-provider review cadence
- Per-provider current month spend

### 29.9 The Interpretation Quality Metric

Track how often the orchestrator's interpretation matches Houston's eventual judgment:
- When the orchestrator says "this negative claim is a hallucination" and Houston agrees → +1 correct
- When the orchestrator says "this negative claim is valid" and Houston agrees → +1 correct
- When Houston overrides → -1 (and the override is fed back as a learning)

Target: orchestrator interpretation should align with Houston's judgment >85% of the time. If it drops below that, the interpretation prompt needs improvement.

### 29.10 Why This Section Exists

Houston has explicitly called out that the author of this PRD (Claude) has a tendency to default to Anthropic models in every role. **This section is the architectural enforcement against that tendency.** Without it, the agent hierarchy described in §3 would silently degrade into a Claude-only echo chamber, and the platform would lose the single most valuable quality control Houston has applied to BigBounce throughout its development.

The non-negotiable rule is: **every lab has at least one OpenAI agent, at least one Google agent, at least one xAI agent, and at least one Perplexity agent, registered as peer reviewers.** The platform refuses to create a lab without them.

---

## 30. Agent Host & Terminal Integration — How CLI Agents Live in the UI

**Houston flagged 2026-04-08 (clarifying):** the custom chat UI is great but he still needs to run real CLI agents (`claude`, `pi`, `tmux`, `ssh`) inside the platform — same workflow he uses today with Claude Code in Cursor's terminal. The Hubify Labs UI must offer **both** a custom chat AND a real embedded terminal. This section explains how.

### 30.1 The Agent Host on Fly.io

Agents do NOT run in the browser. They do NOT run inside the custom chat UI. They run as **real processes on Fly.io machines**.

**Per-lab agent host:**
- Each lab has its own Fly.io machine (named `<lab>-host`, e.g. `bigbounce-host`).
- The machine runs an `agent-host` process that owns the lab's agent fleet.
- Always-on by default. Auto-stops when idle (Fly's auto-stop machines feature). Cheap when nothing is happening.
- Persistent volume mounted at `/lab` containing the lab's repo, outputs, chains, models.
- Has SSH access for the user (and the embedded terminal).

**The agent host spawns Claude Code as the orchestrator:**
- Same `claude` binary Houston uses today. No reinvention.
- Started via `claude --headless --workdir /lab --system-prompt /lab/AGENTS.md` or equivalent.
- Sub-agents (leads, workers, cross-provider reviewers) are spawned via Claude Code's existing Task tool, OR as separate `claude` subprocess instances, OR as direct provider API calls (OpenAI / Gemini / Grok / Perplexity from §29).
- Each agent emits structured events to Convex via the activity feed pattern (§25).

**Why this matters:**
- The orchestrator is **not a JavaScript reimplementation of Claude Code**. It IS Claude Code, running on a real Linux machine, with a real filesystem, real Python, real GPU SSH access, real `tmux` sessions.
- All the existing Claude Code skills, tools, MCP servers, and workflows that Houston already uses just work.
- The custom chat UI is a CLIENT of this agent host, not a replacement for it.

### 30.2 Two Views of One Machine

The Hubify Labs UI exposes the agent host through TWO surfaces, both visible at the same time when the user wants:

**View 1: The custom chat panel** (`bigbounce-orch` chat)
- Connects to the agent host via REST/RPC (`api.hubify.com/labs/bigbounce/chat`)
- High-level. Designed. Renders agent activity nicely.
- Reads structured events from Convex (the activity feed)
- This is what we've been building in §25-§28
- Best for: "what happened overnight?" / "deploy phase 9" / "summarize the new results"

**View 2: The embedded terminal panel**
- Real PTY connected to the same agent host machine
- Low-level. Raw. Real shell.
- Where the user runs `claude`, `pi`, `tmux`, `ssh root@runpod-pod`, `git status`, `python p1_fnl_recompute.py`, `tail -f phase4.log`
- Same lab, same processes — just a different UI on top
- Best for: tail logs, debug a failure, run a one-off script, watch Claude Code's tool calls in real time

**The point:** the user does not have to choose. Both panels are visible at the same time. The chat is for steering, the terminal is for poking.

### 30.3 Terminal Per Frontend Surface

| Surface | Terminal mechanism | Notes |
|---|---|---|
| **macOS desktop (Tauri)** | Real local PTY via `tauri-plugin-shell` or equivalent | Types `claude`, runs `claude` ON YOUR MAC. Can also `ssh root@bigbounce-host` to drop into the lab's Fly machine. **Exactly like Cursor's integrated terminal.** Best DX. |
| **Web app (Vercel)** | `xterm.js` in the browser ↔ WebSocket ↔ PTY on the lab's Fly machine | Same pattern as `code-server` / GitHub Codespaces / VS Code Web. Auth via Hubify session token. The PTY runs on Fly, not in the browser. |
| **TUI app (textual / bubbletea)** | Native — IS a terminal | Doesn't need an embedded terminal. The chat panel and the shell are split panes in the same TUI window (like btop / k9s split layouts). |

### 30.4 Terminal Features (per surface)

The embedded terminal must support:

**Required:**
- ANSI 256-color
- True color (24-bit) for `delta`, `bat`, `fzf`, etc.
- Unicode (for the Claude Code box-drawing characters and braille loaders)
- Copy / paste (Cmd+C / Cmd+V)
- Mouse selection
- Scrollback (10,000 lines minimum)
- Resize handles (drag the divider)
- Multiple sessions / tabs (run `claude` in tab 1, `tmux attach` in tab 2)
- Persistent sessions (PTY survives UI reload — `screen` / `tmux` / `mosh` style)

**Nice to have (Phase 2):**
- Sixel image support (for `imgcat`, `chafa`, gnuplot output)
- Hyperlink detection (file paths, URLs)
- Click-to-copy on selected text
- Inline diff rendering for `git diff`
- Terminal command history search (Ctrl+R)
- Custom keybindings per user

**Forbidden:**
- A "fake" terminal that only accepts whitelisted commands
- A "command palette only" interface
- A REPL that runs in the browser instead of on the agent host
- Anything that would break `claude` running inside it

### 30.5 The Chat ↔ Terminal Connection

Both views connect to the same agent host. They share:

- **The same agent processes.** When the chat shows "anomaly-lead is running EXP-054", the terminal can `tail -f /lab/logs/EXP-054.log` and see the same activity.
- **The same filesystem.** The chat can write to `/lab/output/`, the terminal can `cat` it back.
- **The same Convex events.** The chat reads them as structured rows; the terminal can `convex logs` or grep the events.
- **The same secrets.** API keys live in `/lab/.env` on the Fly machine, accessible from both.
- **The same git state.** The chat agents commit to `/lab/.git`, the terminal can `git status` to see uncommitted changes.

**They are not competing systems. They are two interfaces to one machine.**

### 30.6 Terminal Layout (UI integration)

The terminal lives as a **dockable panel** in the workspace, separate from the chat panel:

```
+----------------------------------------------------------+
| sidebar | chat panel | preview panel                     |
|         |            |                                   |
|         |            |                                   |
|         |            |                                   |
|         |            |                                   |
+---------+------------+-----------------------------------+
| sidebar | TERMINAL PANEL (bottom dock — Cursor style)    |
|         | $ claude                                       |
|         | ✻ Welcome to Claude Code                       |
|         | > what's the status of EXP-054?                |
|         | ⎿ I'll check the logs.                         |
|         |    [Reading file ... 12 results]               |
|         | ...                                             |
+----------------------------------------------------------+
| status bar                                                |
+----------------------------------------------------------+
```

The terminal is **independent of the chat panel** — you can have:
- Chat-left + Terminal-bottom (most common, Cursor-like)
- Chat-bottom + Terminal-bottom (stacked, the chat above the terminal)
- Chat-hidden + Terminal-bottom (terminal-only mode)
- Terminal-hidden + Chat-left (the current default — chat-only mode)

Toggle with `Ctrl+`backtick`` (terminal show/hide, the universal terminal shortcut).

### 30.7 Terminal Sessions and Multiplexing

The embedded terminal supports multiple sessions via tabs at the top of the terminal panel:

```
+----------------------------------------------------------+
| TERMINAL                          [+ new]  [⚙]  [×]      |
| [claude] [tmux: phase4] [logs] [ssh runpod] [+]          |
+----------------------------------------------------------+
| [the active session's content]                           |
+----------------------------------------------------------+
```

Each session can be:
- A fresh shell on the lab's Fly machine
- An attached `tmux` session
- An SSH connection to a RunPod pod
- A `claude` interactive session
- A `python -i` REPL
- Anything you'd run in a real terminal

Sessions survive UI reload because they live on the agent host (the Fly machine), not in the browser. Closing the browser does not kill the session — same as `mosh` or `tmux`.

### 30.8 Claude Code Integration Specifics

Since the orchestrator IS Claude Code, the terminal can interact with it in interesting ways:

- **Watch the orchestrator work:** open a terminal session, `claude --resume <session-id>` to attach to the running orchestrator session and see its tool calls live.
- **Drop in mid-task:** if the orchestrator is stuck, you can interact with the same Claude Code session directly from the terminal — same context, same memory, no handoff needed.
- **Inspect agent state:** `cat /lab/.hubify-labs/STATE.md`, `tail /lab/.hubify-labs/EXPERIMENTS.jsonl`, etc.
- **Manual override:** kill a stuck agent, restart it, change its config, all without leaving the UI.

This is the **best of both worlds** Houston referenced — visibility from the chat AND direct control from the terminal, with the same Claude Code instance underneath.

### 30.9 Why Fly.io for the Agent Host

Confirmed (with the GPU caveat from §24):

- **Persistent always-on services** are exactly Fly's sweet spot. Fly machines are real Linux VMs with persistent volumes, auto-stop on idle, real network identity.
- **Cheap when idle** — Fly's auto-stop machines feature stops the VM when no traffic, restarts on demand within ~1 second. Per-lab cost is single-digit dollars/month when idle.
- **Real PTY access** — Fly machines are real Linux. SSH works. `tmux` works. `claude` works. No serverless gymnastics.
- **Per-region** — Fly can spin up the lab host close to the user (US-East for Houston) for low-latency terminal interaction.
- **Volumes** — persistent disk per lab, mounted at `/lab`, contains the repo + outputs + chains.

What Fly is NOT for:
- GPU compute (deprecated August 2026 per the architecture decision doc)
- Static deploys (Vercel handles this)
- Ephemeral sandboxes (Vercel Sandbox handles this)

Fly's role is exactly: **the persistent agent host where Claude Code lives**. That's it.

### 30.10 Migration Path

For BigBounce specifically (Houston's current lab):

1. **Phase 1 (now):** Houston runs Claude Code locally in his terminal. No change. The custom chat UI is added as an OPTIONAL second view that subscribes to Convex events written by the local Claude Code session.
2. **Phase 2:** The lab gets a Fly.io agent host. Claude Code starts running there as an option, same workflow. Houston picks where to run it.
3. **Phase 3:** Default flips — new sessions start on Fly automatically. Local terminal still works (for offline or fast iteration). Embedded web/desktop terminal connects to the Fly host.
4. **Phase 4:** Add multiple agents (leads, workers, cross-provider reviewers) on the Fly host. Houston still runs his own `claude` sessions side-by-side via the embedded terminal.

At no point does Houston lose the ability to run `claude` in a real terminal. That workflow is preserved end-to-end.

### 30.12 The Hubify CLI + Multi-Session Terminal Pattern

**Houston flagged 2026-04-08 (extending §30):** the embedded terminal needs more than a raw shell. It needs custom Hubify tooling, auto-launched Claude Code synced to the orchestrator, and Pi agent sessions. Some users will work entirely in the terminal — terminal-only must be a first-class workflow, not a fallback.

**Every lab spins up 4 default terminal sessions on open:**

1. **`hubify` (default tab)** — the **Hubify CLI/TUI** itself. Custom-built. Mirrors the web UI styles exactly:
   - Same color tokens via terminal palette (sage accent → 256-color value)
   - Same animations: cosmic orb modes (text-art versions like `● ○ ◌`, `▰ ▱`, etc.), shimmer verb (slow color cycling on the active text), pulsing dots (braille animations)
   - Same box-drawing tree (`⎿`, `├`, `└`)
   - Same status glyphs (`◻ ▣ ✔ ✗`)
   - Same message structure (author + timestamp + body)
   - Same task list format
   - Same standup transcript format
   - Built with **Textual (Python)** or **Bubble Tea (Go)** — both are first-class targets, picked per the desktop/CLI surface stack
   - Vim-style command mode: `:exp 054`, `:review`, `:tasks`, `:standups`, `:pi`, `:claude`, `:bash`
   - The Hubify CLI is the **TUI face** of the platform — same data, same controls, just rendered for the terminal

2. **`claude · synced` (auto-launched)** — Claude Code attached to the SAME session the orchestrator chat panel is talking to:
   - `claude --resume <orchestrator-session-id>`
   - Houston can drop into the running orchestrator and see its tool calls live
   - Intervene, override, redirect mid-task
   - This is the "watch the chat from the inside" view
   - Same Claude Code binary Houston uses today, no reinvention

3. **`pi · 11 workers` (multi-agent activity feed)** — the Pi agent (per indydevdan's ui-agents project) running for leads + workers:
   - Color-coded activity feed: orchestrator=sage, lead=bright, worker=muted, fail=warn
   - Each line tagged with agent role + timestamp + message
   - Tilldone pattern visible: when worker fails, lead-takeover events surface inline
   - Live stream of all sub-agent activity
   - Whether Pi runs Claude Code internally OR is a separate runtime is TBD pending the Pi research agent's findings (in progress at `bigbounce/project-context/pi_agent_study.md`)

4. **`bash` (raw shell)** — for everything else:
   - `tmux`, `python`, `ssh root@runpod`, `git status`, `tail -f`, `gh pr create`, etc.
   - Real PTY, full shell, escape hatch for full freedom
   - This is the same shell Houston uses today

### 30.13 RESOLVED: Claude Code is the runtime, Pi is the vocabulary (2026-04-08)

**Pi research landed** at `bigbounce/project-context/pi_agent_study.md` (793 lines). Key corrections to earlier assumptions:

**Pi is NOT indydevdan's project.** Pi is **Mario Zechner's `badlogic/pi-mono`** — a TypeScript coding agent on npm as `@mariozechner/pi-coding-agent`. **IndyDevDan's actual repo is `disler/pi-vs-claude-code`** — 16 user-land extensions that demonstrate multi-agent patterns ON TOP of Pi (665 stars, last updated 2026-03-11). Both repos are MIT.

**Pi has NO native sub-agent support.** Dan's `subagent-widget.ts`, `agent-team.ts`, `agent-chain.ts` are all extensions that use `child_process.spawn("pi", args, ...)` to fork child processes as workers. Multi-agent coordination is user-land, not first-party.

**Pi and Claude Code do NOT use each other internally.** They are independent runtimes. They can interoperate in three narrow ways:
1. Pi's `cross-agent.ts` extension reads `.claude/agents/*.md` directories and re-registers them as Pi slash commands (read-only filesystem aggregation)
2. Pi subprocess spawns can trivially swap `spawn("pi", ...)` for `spawn("claude", ["--print", "--output-format", "stream-json"])` since the JSONL schemas map cleanly
3. They both follow the Agent Skills markdown standard

**Tilldone is NOT lead-takeover.** I had this wrong. Pi's tilldone is a **self-discipline gate for a single agent** — blocks all non-tilldone tool calls until the agent declares its tasks, auto-nudges on `agent_end` if tasks are incomplete. It's a "keep going until done" policy layer, NOT inter-agent failover. The lead-takeover concept I spec'd in §25.3 came from paperclip (and is also how Dan's extensions implement multi-agent recovery) — NOT from native Pi. §25.3 stays as-is, just relabeled as the "paperclip + Dan's extension" pattern, not "Pi's pattern".

**Pi's TUI is custom.** `pi-tui` is a purpose-built library with three-strategy differential rendering and CSI 2026 synchronized output. NOT Ink, Rich, or Bubble Tea. Components expose `render(width)` returning string arrays with embedded ANSI. Themes use 51 color tokens. Worth studying as a TUI vocabulary source.

**Backend sync is NOT built into Pi.** But Dan's separate repo `disler/claude-code-hooks-multi-agent-observability` shows the canonical pattern: Hook → HTTP POST → Bun server → SQLite → WebSocket → Vue. For Hubify Labs, swap SQLite→Convex and Vue→React. A 50-line extension can mirror every Pi event to Convex.

**THE DECISION (Houston, this is the architecture):**

| Role | Choice | Why |
|---|---|---|
| **Primary agent runtime** | **Claude Code** | Opus 4.6, 1M context, native sub-agents (Task tool), MCP, the runtime Houston already uses daily, integration with Anthropic's roadmap |
| **Multi-agent coordination** | **Hubify-built (in Convex)** | Inspired by Dan's extension patterns + paperclip's `enqueueWakeup` chokepoint (§28.2) — not Pi's subprocess model, not Claude Code's native Task tool alone |
| **Activity feed / observability** | **Hubify-built (Convex + React)** | Pattern from `claude-code-hooks-multi-agent-observability` — Hook → HTTP POST → Convex → React |
| **TUI vocabulary source** | **Pi (`pi-tui`) + Dan's widgets** | Borrow visual primitives, color tokens, agent-team grid layout, subagent-widget cards. Don't install Pi. Reimplement the patterns in our Hubify CLI (Textual or Bubble Tea). |
| **Cheap-worker tier** | **Pi (v3 only)** | Pi has native support for Groq, Gemini Flash, Ollama, and 17+ providers. For bulk low-cost work (data processing, simple classifications), Pi as a subprocess is cheaper than Claude Code. **Defer to v3** — not Phase 1. |
| **Don't install** | **Pi as a Hubify Labs dependency** | The runtime boundary (Pi = Bun/Node in-process extensions vs Hubify Labs = Convex + React web + Fly host) makes embedding wasteful. We'd only use Pi to spawn subprocesses, which we can do ourselves. |

**Phase 1 implication:**
- The agent host on Fly runs **Claude Code** as the orchestrator (subprocess)
- Sub-agents (leads, workers, cross-provider reviewers) are spawned via:
  - Claude Code's native Task tool (for Anthropic agents)
  - Direct provider API calls (for OpenAI, Gemini, Grok, Perplexity per §29)
  - NOT Pi
- The "Pi-style" multi-agent activity feed in the UI is **Hubify-built** — same UX vocabulary, different runtime
- The terminal panel's `pi · 11 workers` tab is **misleading** — should be renamed to `team.live` or `agent-fleet` to make clear it's our activity feed, not actual Pi running

**What we steal from Pi:**
1. **The agent-team grid dashboard** — 11 workers in a grid showing live status (Dan's `agent-team.ts`)
2. **The subagent-widget live cards** — per-agent live progress bars, current task, recent output (Dan's `subagent-widget.ts`)
3. **The 51-token color theme** — accent / success / error / dim / muted / etc. (we already have most of these in our design system)
4. **The CSI 2026 differential rendering pattern** — when we build the Hubify CLI in Textual or Bubble Tea, use synchronized output to avoid flicker
5. **The tilldone single-agent self-discipline gate** — every agent's system prompt includes the "declare your tasks first, don't tool-call until you have a plan" rule
6. **The Agent Skills markdown standard** — `.claude/agents/*.md` and `.hubify/agents/*.md` use the same format so cross-runtime reuse is possible

**What we DON'T copy from Pi:**
- The Bun/Node runtime
- The single-process extension architecture (we want first-class multi-process)
- Pi's specific provider integrations (we route through our own provider abstraction)
- Pi's session JSONL format (we use Convex tables)

**Open follow-up:** Phase 1 builds Hubify Labs with Claude Code as the only runtime. Phase 3 evaluates adding Pi as a subprocess for the cheap-worker tier (Groq / Gemini Flash bulk classification, etc.). Phase 3 is months out — don't pre-build.

### 30.14 Two Valid User Modes (terminal-only is first-class)

Hubify Labs supports two equally-valid workflows:

**Chat-driven user:**
- Primarily uses the custom chat panel
- Terminal is the escape hatch for low-level work
- Most common for the "I want to direct the lab" use case

**Terminal-driven user:**
- Primarily uses `hubify` CLI in the terminal
- May never open the chat panel
- Most common for the "I want to feel the team working" use case
- Common for SSH-only access (the desktop app or web app may not even be running)

**Both modes share:**
- The same lab state (Convex)
- The same agent processes (Fly host)
- The same Claude Code / Pi / orchestrator
- The same activity feed
- The same memory layer
- The same design language (Hubify CLI mirrors the web UI styles)

The two UIs are **interchangeable peers**. Neither is the "main" UI. A user can switch from one to the other at any moment without losing context.

### 30.15 Hubify CLI Implementation Notes

The Hubify CLI is its own application, distributed as part of the platform:

**Distribution:**
- Pre-installed in every lab's Fly machine at `/usr/local/bin/hubify`
- Pre-installed in the macOS desktop app's bundled environment
- Installable via `brew install hubify` for users who want it on their own Mac
- `pip install hubify-labs` for Python TUI version, `go install hubify` for Go version

**Stack choice (TBD):**
- **Option A: Textual (Python)** — best ecosystem for rich TUI, easy to ship, integrates with the existing Python research code
- **Option B: Bubble Tea (Go)** — fast, single binary, no runtime dependency, easier to install
- **Option C: Both** — Python for the integrated experience, Go for the standalone single-binary distribution

The Hubify CLI's screens map 1:1 to the web UI views from §20-§29: Director / Overview / Experiments / Pipelines / Papers / Figures / Data / Knowledge / Agents / Comms / Standups / Tasks / Ideas / Costs / Alerts / Settings. Same vocabulary, same data, different rendering.

**Auto-start on lab open:**
When the user opens a lab in any frontend (web, desktop, TUI), the agent host on Fly:
1. Starts the orchestrator (Claude Code) if not running
2. Starts Pi if not running
3. Spawns 4 PTY sessions: hubify, claude, pi, bash
4. Connects them to the user's terminal panel
5. The user sees the Hubify CLI as the default tab, with the others one click away

### 30.16 Terminal Styling Parity Requirements

The Hubify CLI in the terminal MUST match the web UI's design language exactly. Concrete parity rules:

| Web UI | Terminal equivalent |
|---|---|
| `--accent #5fb88a` (sage green) | 256-color `38;5;108` or true-color `\x1b[38;2;95;184;138m` |
| Cosmic orb (pulsing modes) | Text-art rotating glyphs: `● ○ ◌`, `▰ ▱`, `⊙ ⊚ ⊛`, etc. — rotates every 24-30s like the web orb |
| Shimmer verb | Slow color cycling on the active text (5.6s, dim peak), implemented as ANSI escape sequences |
| Box-drawing tree (`⎿`) | Same Unicode characters, same indentation |
| Status glyphs (`◻ ▣ ✔ ✗`) | Same Unicode characters |
| Greeting font (Newsreader serif) | Replaced with capital letters + spacing for visual prominence (TUIs can't render serif) |
| Stat cards | Boxed regions with border-drawing characters |
| Card hover state | Subtle ANSI background-color change |
| Activity feed (Comms) | Same chronological feed, color-coded same way |
| Task list | Same format, same status glyphs, same grouping |

The TUI is not a "lite version" of the web UI. It is **the same UI rendered in a different medium**.

### 30.11 What This Section Replaces

This section partially supersedes earlier assumptions in:
- **§3 (Agent Hierarchy)** — clarifies that "agents" are real OS processes, not abstractions
- **§9 (Fly.io Cloud Deployment)** — confirms Fly's role as agent host (and removes any GPU assumptions)
- **§10.5 (RunPod Safety Layer)** — RunPod is still the GPU compute layer; Fly is the orchestration layer
- **§29 (Cross-Model Peer Review)** — non-Anthropic agents are also processes on the Fly host, just calling different provider APIs

The two views of one machine pattern is the through-line that makes all of this coherent.

---

## 31. UI Component Inventory — Built and Specified

**Status:** This section captures every component shipped in the working mockup at `/Users/houstongolden/Desktop/CODE_2025/hubify-labs-mockups/index.html` (currently ~9,738 lines, 88 commits, single self-contained HTML file). The mockup is the definitive source of truth for what the v1 product looks like. This inventory is the bridge between the mockup and the dev team. **Every item below has been built, clicked-through, and is reachable from the running mockup.**

### 31.1 Top-level chrome (always visible)

| Element | Built? | Spec |
|---------|--------|------|
| **Sidebar** (collapsible left rail) | ✅ | 220px expanded · 48px collapsed (icon-only) · ⌘B toggle. Two modes (Menu / Files) toggle at the bottom. |
| Sidebar brand | ✅ | "Hubify Labs" · click → home / brand action. |
| Sidebar lab selector | ✅ | Current lab name + arrow → opens **lab dropdown**. Search filter inside dropdown. 6 sample labs (active + public + 2 private + 2 planned). Click any → opens `lab` sidepeek. |
| Sidebar nav (Menu mode) | ✅ | 24 sb-items grouped by section, each routes to the corresponding view via `navTo(view)`. Active state mirrored from current view. |
| Sidebar file tree (Files mode) | ✅ | Tree with `arxiv/`, `pipelines/`, `papers/`, `research/`, `notebooks/`, etc. Folders toggle expand/collapse. **File leaves click → `openFile(name)` → rich preview tab.** "+ New file" button → `new-file` sidepeek with 10 templates. |
| Sidebar footer user button | ✅ | Avatar + handle → profile popover (Public profile / Memory inspector / Billing / Sign out). |
| Sidebar footer notif bell | ✅ | Click → **notifications drawer** slides out from sidebar (NOT a modal). 12 sample notifs · 6 filter chips · empty state · click row → opens related sidepeek. |
| **Preview tab bar** (top of preview pane) | ✅ | Static "Director" tab + dynamic file preview tabs (created by `openFile`). Each file tab has its own × close. ⌘W closes the active file tab. |
| Now-strip (preview tab spacer) | ✅ | "live · <event>" rotating every 4.8s through 10 sample agent events. Click → `cronloop` sidepeek. |
| Preview tab actions | ✅ | Toggle chat (⌘J) · Keyboard shortcuts (?) · More options → `preview-opts` sidepeek (View / Layout / Tools, 11 actions). |
| **Chat / terminal panel** (dockable) | ✅ | 4 dock positions: left (default ⌘1), right (⌘2), bottom (⌘3), hidden (⌘J). Resizable in all positions via dragger. Two modes: Orchestrator chat / Terminal (Ctrl+`). |
| Chat header | ✅ | Pulse + agent name (click → agent sidepeek) · model meta (opus 4.6) · New chat · Chat history (sidepeek with 14 sessions) · Position picker · Hide. |
| Chat input | ✅ | Textarea with Enter to send · `/` `@` `#` autocomplete popup (10 commands · 8 agents · 7 experiments) · Click-to-insert chips below. |
| Terminal panel | ✅ | 6 default tabs: hubify CLI / claude (synced) / pi · 11 workers / team.live / phase4 logs / bash. Each tab is a real session mock with output. Close × per tab. + button → `term-new` sidepeek with 9 session templates. |
| **Status bar** (bottom) | ✅ | Connected pulse · $ today (→ Costs) · pod idle count (→ Compute) · credits (→ Costs) · **auto-loop heartbeat pill** (live :14/:44 timestamps, click → `cronloop` sidepeek) · ⌘B / ⌘J / ⌘P kbd hints · 53 exp · 4 papers · 328K anomalies (→ Overview). |

### 31.2 Views — 25 total (24 navigable + 1 ephemeral file preview)

| ID | Title | Built? | Notes |
|----|-------|--------|-------|
| `view-director` | Director (home) | ✅ | Greeting · **overnight briefing card** (6 metrics + 10-item shipped list + click → cronloop) · 8-card hero stat grid · orchestrator activity card with cosmic orb thinking block · top experiments table (8 rows, click → experiment sidepeek) · running now (3 rows) · overnight summary timeline. |
| `view-overview` | Lab Overview | ✅ | Key Results stat grid (8 cards) · Compute widget · Surveys grid (8 clickable cells → `survey` sidepeek). |
| `view-projects` | **Projects (PRD §40 hierarchy)** | ✅ | **NEW** — top-level browser for the lab's research threads. Shows 3 real BigBounce projects (P1 f_NL tracer, P3 anomaly engine, P4 PTA Bayes) as clickable cards with goal/deliverable/measurable + pipeline progress + experiment count + task count + paper M:M count + last-updated. Each card → `project` sidepeek (PRD §40.12). Header shows the **hierarchy trail** (Lab → Project → Pipeline → Experiment → Task) with current position highlighted. Includes a "Hierarchy guide" card explaining each level. **Lives between Director and Experiments in the top-6 always-visible sidebar nav.** |
| `view-experiments` | Experiments | ✅ | **Dispatch new experiment card with PRD §41 routing UI** (live preview of routing decision, 4 mode/duration/priority radios, target resource + rationale + cost estimate updated on every change) · status filters (All/Complete/Running/Failed/Queued, **wired**) + search input · 53-experiment table, rows click → experiment sidepeek. |
| `view-pipelines` | Pipelines | ✅ | 3 pipeline cards (P1 f_NL tracer purification, P2 chirality complete, P3 anomaly engine) with step trackers. |
| `view-papers` | Papers | ✅ | 4 stat cards · status filters · 4 paper rows (click → paper sidepeek with PDF preview / LaTeX source / metadata 3-mode toggle) · version timeline (7 entries) · pre-submission checklist (LaTeX compiles · undef refs · dim check · cross-review · novelty audit · Houston signoff) · venue targets. |
| `view-figures` | Figures | ✅ | Per-paper filters (P1/P2/P3/P4, **wired**) + search · 38-figure grid with hand-drawn SVG thumbnails · click → figure sidepeek (lightbox, dimensions, caption, paper ref). |
| `view-data` | Data Explorer | ✅ | Kind filters (All/Anomalies/MCMC/Spectra/Catalogs, **wired**) + search · 15-dataset table, rows click → dataset sidepeek (schema + sample rows + provenance). |
| `view-knowledge` | Knowledge Wiki | ✅ | Type filters (All/Entities/Concepts/Sources/Comparisons, **wired**) + search · 3 columns (entities/concepts/sources) · 5×7 bounce model discrimination comparison table · citation graph SVG · cross-lab sharing card. |
| `view-contributions` | Scientific Contributions | ✅ | 16 contributions · 4 stat cards (avg novelty 7.8, papers searched 142, false novelty 0%) · novelty score bars (10 ticks per row, sage filled) · click row → contribution sidepeek (FACT/OPINION/HALLUCINATION classification + reviewer verdicts + revision history + next review date). |
| `view-agents` | Agents | ✅ | Org chart (21 agents: director-you + global orch + bigbounce orch + 4 leads + 11 workers + 4 cross-provider reviewers) · routing-by-reasoning-level table · cross-model peer review pipeline · interpretation pass explainer. |
| `view-comms` | Multi-agent activity | ✅ | **Cross-lab comm gateway card** (3-column inbound/center/outbound visualization · sample comms from dark-energy + dark-matter + hubify-self-improving · footer aggregate stats with `0 blocked writes` Lab Sovereignty Rule confirmation · clickable comms → comm-event sidepeek) · live activity feed (1,847 events today, 16 agents). Filter chips (All/Orchestrator/Leads/Workers/Failures/Takeovers/Standups). Activity rows click → linked sidepeek. |
| `view-standups` | Standups | ✅ | 3-per-day card · today's 3 standups · full transcript view · recent transcripts timeline. Click standup row → standup sidepeek. |
| `view-tasks` | Tasks | ✅ | View mode toggle (Kanban / List / Activity, **all 3 modes built**) · **7 PRD §40 project filter chips** (All / P1 f_NL tracer / P2 chirality / P3 anomaly / P4 PTA / QC / Infra · keyword-mapped + auto-update column counts on filter) · 261 tasks · cross-agent reviews · comments · paperclip pattern · 4 list groups · 20 activity events. |
| `view-ideas` | Ideas & Insights | ✅ | 23 ideas · status filters (All/Active/Queued/Parked/High viability) · 5 active idea rows with viability scores · click → `idea` sidepeek (5-dimension breakdown: novelty/feasibility/impact/cost/time-to-result). |
| `view-costs` | Costs | ✅ | Per-provider split (9 providers: Anthropic/OpenAI/Google/xAI/Perplexity/RunPod/Fly/Vercel/Convex — Modal dropped 2026-04-08) · daily + monthly + cap + usage bars · **30-day SVG line chart** (4 provider lines + gridlines + axis labels) · burn forecast. |
| `view-alerts` | Alerts | ✅ | 2 active alerts (disk crit, runway warn) with **contextual action buttons** (Clean up / New pod / Configure rule / Snooze) · category breakdown · 30-day history · escalation path L1-L4 · alert rules editor (5 rules, click → `alert-rule` sidepeek). |
| `view-settings` | Settings | ✅ | **10 nav sections** (Models / Providers / Cross-review / Budget / Backups / Keys / Repos / **Lab Sharing** / Agents / **Runtime**) — Lab Sharing opens `lab-share` sidepeek directly with PRD §40.11 Sovereignty Rule explainer + read grants in/out + audit log; Runtime opens `runtime` sidepeek with macOS / Fly / MCP variants. Cross-provider config (5 providers + API keys + budget caps). 21-agent roster (clickable rows → agent sidepeek). |
| `view-memory` | Memory | ✅ | **4-layer tabs** (User/Agent/Lab/Global, **wired** — clicking filters mem-results) · type filter chips · search · 18 sample memories · click row → `memory` sidepeek (4-layer detail with usage history + related memories). |
| `view-profile` | Profile (Houston public) | ✅ | Avatar + bio + Follow/Share/Edit · **52-week activity heatmap with custom hover tooltip** (date + 4-quadrant breakdown of experiments/papers/agent/knowledge counts) · 4 pinned labs · 4 papers · 16 contributions with novelty bars · 3 public models · 5 public datasets · 7 articles. |
| `view-compute` | Compute | ✅ | 4 stat cards · pod cards (bigbounce-h200 with SSH/Restart/Kill buttons; serverless endpoint cards for anomaly-detector + pdf-qa) · single-vendor RunPod breakdown · idle GPU watchdog timeline · credits history chart with 4 threshold lines (per §41). Kill button → `pod-kill` confirmation sidepeek (running impact + pre-kill steps + alternatives + name confirm). |
| `view-vibe` | Vibe Coding | ✅ | Vercel Sandbox split layout · left chat with cosmic orb thinking block · code block · right preview iframe with CSS-built fake chart · 3 mode tabs (preview/code/logs, **wired**) · reload/open-browser/save buttons. |
| `view-reviews` | Cross-model peer review | ✅ | 4 stat cards · active reviews table (click row → paper or contribution sidepeek) · review drilldown with **3 clickable reviewer cards** (GPT-5 / Gemini / Sonnet skeptic, click → agent sidepeek) · interpretation pass classification (FACT/OPINION/HALLUCINATION) · provider spend breakdown. |
| `view-routines` | Routines | ✅ | 4 stat cards · 8 routine rows (3 standups + 5 watchdogs/maintenance, **all clickable** → `routine` sidepeek with schedule + last/next fire + recent fires) · recent fires timeline. |
| `view-backups` | Backups | ✅ | 4 stat cards · filters · **8 destination cards** (4 active: Local/Pod/RunPod-vol/S3 Glacier + 4 standby: Cloudflare R2/Backblaze B2/Wasabi/GitHub LFS partial, **all clickable** → `backup-dest` sidepeek with sync config + tradeoffs + last error) · 4-column 12-dataset matrix · storage cost per location · 7-day verification history. |
| `view-site` | Site Preview | ✅ | Browser chrome with URL bar · CSS-rendered light-mode mock of bigbounce.hubify.app homepage · deployment metadata sidebar (commit, build, lighthouse 98/100/100/100, domains, recent deploys). Deploy button → `deploy` sidepeek (7-step plan + pre-flight checks + commits + affected routes + rollback). |
| `view-file` | File Preview (ephemeral) | ✅ | Empty state with file icon + 6 sample file pills (CLAUDE.md / main.tex / p1_fnl_recompute.py / desi_dr1_anomalies.csv / version.json / references.bib). Populated dynamically by `openFile(filename)`. **Rich per-filetype renderers** with hand-rolled syntax highlighters. |
| `view-datamap` | Data Map | ✅ | **Data zone visualization** — 5-zone canvas (Z1 source · Z2 state · Z3 compute · Z4 backup · Z5 public) with arrows showing data flow between zones · 12 tier boxes per zone (T1-T12) · click any zone or tier → zone/tier sidepeek with "what lives here" + "agent contract" + "backup destination" + cost. Per PRD §33. |
| `view-graph` | Activity Graph | ✅ | **Neural brain view** — 114-node force-directed graph (sage palette · 5 Hubify Labs entity groups: contribution / agent / experiment / output / data) with ~296 semantic edges + neuron pulses traveling along edges + per-group hover meta with "Connected to" top-6 list + sidepeek dispatch on node click. Live filter input wired. Per PRD §39. |

### 31.3 Sidepeek renderers — 26 total

The **sidepeek** is the universal drilldown pattern: a slide-in panel from the right portion of the preview area. **NO MODALS** rule. Every clickable content element calls `openSidepeek(type, id)`.

| Type | Built? | Sources (where clicks come from) |
|------|--------|---------------------------------|
| `paper` | ✅ | Papers list rows · paper version timeline · pre-submission checklist rows. PDF Preview / LaTeX Source / Metadata 3-mode toggle. |
| `experiment` | ✅ | Experiments table rows · running-row cards on Director · activity feed events with EXP-XXX · top experiments table on Director. |
| `agent` | ✅ | Agents view org-node cards · Settings agent roster rows · chat header agent name · chat message author names · vibe message author names · reviewer cards in cross-review · "+ Add agent" hierarchy view → `agent-new`. |
| `figure` | ✅ | Figure cards · figure hero cards. Lightbox + caption + dimensions + paper ref + download. |
| `task` | ✅ | Kanban cards · list rows · activity rows. |
| `file` | ✅ | (override → `openFile` for known files; falls back to text-only sidepeek) Memory result file references. |
| `contribution` | ✅ | Contributions table rows · novelty re-review notif · reviews active reviews table (novelty claim type). FACT/OPINION/HALLUCINATION classification. |
| `standup` | ✅ | Standup rows · `/standup` slash command · standup transcript "view full" link. |
| `shortcuts` | ✅ | `?` keypress · Help menu item · preview tab bar Keyboard shortcuts button · /shortcuts slash command. 8 categories. |
| `lab-templates` | ✅ | "+ New lab" in lab dropdown · `/template` slash command. 9 templates. |
| `dataset` | ✅ | Data view table rows. Schema + sample rows + provenance + actions. |
| `deploy` | ✅ | Site view Deploy button. 7-step plan + pre-flight checks + commits + affected routes + rollback safety. |
| `survey` | ✅ | Overview survey grid cells. Coverage + instrument + QC + linked experiments + featured papers. |
| `alert-rule` | ✅ | Alerts settings rows · alert action "Configure rule" buttons · "+ new rule" h-action. 5 rules with trigger config + recent fires + escalation path + snooze. |
| `chat-history` | ✅ | Chat header history button. 14 sessions + search + export. |
| `agent-new` | ✅ | Settings "+ Add agent" button. Form: basics + system prompt + capabilities + limits + templates. |
| `new-file` | ✅ | Sidebar Files mode "+ New file" button. 10 templates: paper.tex / figure.py / experiment.py / pipeline.py / analysis.ipynb / wiki_entry.md / standup_notes.md / survey_qc.md / config.yaml / blank. |
| `preview-opts` | ✅ | Preview tab bar "More options" button. View / Layout / Tools sections, 11 clickable rows. |
| `routine` | ✅ | Routines view rows. 8 routines with schedule + last/next fire + recent + Run now / Pause / Edit / View logs. |
| `wiki` | ✅ | Knowledge wiki entries (replaces the older contribution renderer for entities). 6 detailed entities + properties + formula + papers + recursive related + sources. |
| `term-new` | ✅ | Terminal panel "+ New session" button + chat header New terminal button. 9 templates: hubify CLI / claude / pi / team.live / phase4 logs / h200 ssh / bash / fly logs / modal standby. |
| `lab` | ✅ | Sidebar lab dropdown rows. 6 labs with description + stats + config + actions. |
| `backup-dest` | ✅ | Backups 8-destination cards. Sync config + tradeoffs + last error + actions. |
| `pod-kill` | ✅ | Compute view per-pod Kill button. Confirmation flow with running impact + pre-kill steps + cost impact + alternatives + name-typed confirm. |
| `memory` | ✅ | Memory view result rows. 4-layer detail + usage history + related memories + edit/pin/promote actions. |
| `cronloop` | ✅ | Status bar auto-loop pill · now-strip · briefing card · `/queue` slash command. 25+ iterations with real commit hashes + stats + queue items remaining. |
| `idea` | ✅ | Ideas view rows. 5-dimension viability breakdown (novelty/feasibility/impact/cost/time-to-result) with animated bars + status history. |

### 31.4 Click contracts — what every clickable thing does

**Universal rule:** every visible UI element that represents a content item calls `openSidepeek(type, id)` on click. Control buttons (Approve / Deploy / Snooze / etc.) call `toast(message)`.

The mockup currently has **313+ onclick handlers** and zero "dead clicks" — the auto-wire scaffold in DOMContentLoaded ensures every kanban-card, wiki-entry, paper-row, fig-card, idea-row, alert-row, standup-row, table tbody row, mem-result, routine-row, etc. is wired. Filter buttons (Figures / Wiki / Data / Experiments / Notifications / Memory layers) actually filter their target lists.

### 31.5 Keyboard shortcuts — 8 categories

| Combo | Action |
|-------|--------|
| `⌘B` | Toggle sidebar collapsed |
| `⌘P` | Open command palette (grouped: Navigation / Actions / Slash commands · arrow keys to navigate · Enter to run · Esc to close) |
| `⌘J` | Toggle chat panel hidden / restore |
| `⌘1 / ⌘2 / ⌘3` | Dock chat to left / right / bottom |
| `Ctrl+\`` | Toggle terminal mode in chat panel |
| `?` | Open keyboard shortcuts cheatsheet |
| `⌘W` | Close active file preview tab (only when file tab is active; otherwise lets browser handle) |
| `Esc` | Close any sidepeek / dropdown / drawer / command palette |

### 31.6 Cosmic orb + verb rotation system

Locked behavior — **do not refactor in v1**. Both the chat thinking block and the Director Orchestrator activity card render the cosmic orb (`.thinking-orb`) and shimmering verb (`.thinking-verb`).

- 10 cosmic orb modes rotate every 24-30s with random jitter: saturn / pulse / orbit / twinkle / beaker / grid / satellite / atom / face / dna
- Verb pool of 50+ contextual phrases ("Routing peer reviews…", "Crystalizing…", "Hobnobbing…") rotates every 7s
- Subtle text shimmer via `linear-gradient` + `background-clip:text` (5.6s, dim peak)
- All instances sync (chat + orchestrator card share the same modes/verbs)

### 31.7 Autonomous polish loop

The mockup ships with an **autonomous overnight cron loop** at `:14` and `:44` every hour. The cron reads `.queue.md`, finds the first unchecked item, builds it in the mockup, marks it done with the commit hash, and commits. After ~30 iterations the queue is empty and the loop enters polish-pass mode. Visible in the UI via:

- Status bar `auto-loop` pill (live :14/:44 timestamps)
- Now-strip system pulse (rotates 10 live events every 4.8s)
- Director view overnight briefing card (6 metrics + 10-item shipped list)
- `cronloop` sidepeek with 25+ iterations + real commit hashes + queue items remaining

This pattern is **explicitly part of the product** — the platform improves itself between sessions while Houston sleeps, and surfaces the work it did when he wakes.

### 31.8 Mockup → Convex schema mapping (data flow)

| UI surface | Reads from (Convex tables) | Writes to |
|------------|---------------------------|-----------|
| Director / Overview | `experiments` · `papers` · `surveys` · `agents` · `tasks` · `costs_daily` · `pods` | none (read-only summary) |
| Experiments | `experiments` · `experiment_runs` · `experiment_logs` | `experiments` (status updates from agents) |
| Papers | `papers` · `paper_versions` · `paper_claims` | `papers`, `paper_versions` (paper-lead) |
| Figures | `figures` · `figure_versions` | `figures` (figure-worker) |
| Data | `datasets` · `dataset_columns` · `dataset_samples` | `datasets` (anomaly-worker) |
| Knowledge | `wiki_entities` · `wiki_concepts` · `wiki_sources` · `wiki_comparisons` · `wiki_relations` | `wiki_*` (wiki-worker) |
| Contributions | `contributions` · `novelty_reviews` · `interpretation_passes` | `contributions` (research-lead, peer-review-* agents) |
| Agents | `agents` · `agent_episodes` · `agent_learnings` | `agents` (orchestrator) |
| Comms | `comm_events` (single live stream of all agent activity) | every agent appends |
| Standups | `standups` · `standup_messages` · `standup_action_items` | bigbounce-orchestrator |
| Tasks | `tasks` · `task_comments` · `task_reviews` | every agent |
| Ideas | `ideas` · `idea_scores` · `idea_status_history` | research-lead, orchestrator |
| Costs | `costs_daily` · `costs_provider` · `costs_per_experiment` | gpu-manager, cost-watchdog |
| Alerts | `alerts` · `alert_rules` · `alert_history` · `alert_snoozes` | watchdogs, gpu-manager, cost-watchdog |
| Settings | `lab_settings` · `agent_models` · `provider_keys` (encrypted) · `budget_caps` | director (Houston) |
| Memory | `memories_user` · `memories_agent` · `memories_lab` · `memories_global` (4 separate tables) | every agent + memory-cleanup cron |
| Profile | `profiles` · `profile_pinned_labs` · `contribution_index` | director |
| Compute | `pods` · `pod_settings` · `idle_watchdog_log` | gpu-manager |
| Vibe Coding | `sandbox_sessions` · `sandbox_messages` · `sandbox_artifacts` | vibe-agent (Vercel Sandbox + Claude Code) |
| Cross-review | `peer_reviews` · `reviewer_verdicts` · `interpretation_passes` (shared with contributions) | peer-review-* agents, orchestrator |
| Routines | `routines` · `routine_fires` · `routine_logs` | bigbounce-orchestrator |
| Backups | `backup_destinations` · `backup_jobs` · `backup_verifications` | backup-worker |
| Site | `site_deploys` · `site_lighthouse` · `site_analytics` | site-worker |
| File preview | `lab_files` (Convex storage refs) · external blob storage for content | director, all agents |

**Total: ~50 Convex tables.** Most map 1:1 to a UI surface; a few are shared (e.g. `comm_events` is read by Comms view but written by every agent).

### 31.9 Inventory completeness check (vs the mockup)

| Category | Built in mockup | Specified in PRD | Gap |
|----------|-----------------|------------------|-----|
| Top-level chrome elements | 13 | 13 | ✅ |
| Main views | 25 | 25 | ✅ |
| Sidepeek renderers | 26 | 26 | ✅ |
| Filter wirings | 6 (Figures / Wiki / Data / Experiments / Notif drawer / Memory layers) | 6 | ✅ |
| Keyboard shortcuts | 12 | 12 | ✅ |
| Cosmic orb modes | 10 | 10 | ✅ |
| Drilldown pattern | sidepeek (NO MODALS) | sidepeek | ✅ |
| Autonomous polish loop | shown in 4 places | §31.7 | ✅ |

**Verdict:** the mockup and the PRD inventory now match 1:1. Any future divergence (mockup adds something the PRD doesn't have) is a bug to fix in §31.

---

## 32. Development Phase Readiness

**Status:** This section is the **handoff checklist** between the mockup-driven design phase and the implementation phase. It declares what is locked, what is deferred, and what the v1 cut looks like.

### 32.1 What is LOCKED for v1 (do not refactor)

**Visual + interaction design:**
- Single sage green accent (`#5fb88a`) discipline · NO new accent colors
- NO MODALS rule · sidepeek slide-in pattern is the universal drilldown
- Cursor IDE meets Bloomberg Terminal aesthetic · grayscale + sage + 2 muted statuses (warn / crit)
- Cosmic orb + verb rotation system (10 modes / 50+ verbs / 5.6s shimmer)
- Newsreader serif only for paper content · Inter for UI chrome · JetBrains Mono for data
- Director vs Orchestrator terminology (Director = human, Orchestrator = top AI agent)
- Tilldone pattern (failed worker → lead takeover, paperclip-inspired)

**Architecture:**
- Convex for backend state (memory, comms, tasks, standups, novelty reviews)
- Fly.io for the always-on agent host (Claude Code as the runtime)
- RunPod ONLY for compute — Pods (always-on) + Serverless (auto-scale) + CPU/GPU variants (Modal dropped 2026-04-08 per §24, §41)
- Vercel for static site hosting + Vercel Sandbox for vibe coding
- Cross-model peer review with mandatory non-Anthropic agents (GPT-5 + Gemini 2.5 + Grok 4 + Sonar Pro)
- 4-layer memory system (User / Agent / Lab / Global), built in-house from scratch on Convex Agent + OSS patterns
- Houston Method v2 as platform-enforced state machine (QC → analysis → interpretation → cross-survey → site sync → queue expansion → backup)
- 24+ routines on cron schedule (3x/day standups, idle GPU watchdog every 5min, novelty re-review hourly, backup verification nightly, memory cleanup weekly)

**Hardware commitments:**
- BigBounce H200 pod stays running, current data is the seed dataset
- Houston stays in director seat for the first 3 months (no fully-autonomous mode)

### 32.2 What is DEFERRED (post-v1)

| Feature | Reason | Target phase |
|---------|--------|--------------|
| ~~Modal pay-per-second GPU~~ | **DROPPED 2026-04-08** — RunPod Serverless covers the same workload at ~30% lower cost without adding a second vendor. See §24 + §41. | n/a |
| DeepSeek + Local Ollama providers | Cost optimization unlocks after $1K/mo spend baseline | Phase 2 |
| Real PNG screenshot in Site preview iframe | Self-contained mockup limitation; revisit when migrating to Vite/Next | Phase 2 |
| External terminal app integration (iTerm2 spawn) | Requires desktop app shell · web-only for v1 | Phase 2 (desktop) |
| Split view for preview pane | Low priority · sidepeek covers most drilldown needs | Phase 3 |
| Lab template gallery → real lab creation | Requires repo provisioning + scaffold pipeline | Phase 2 |
| GitHub LFS as primary backup | Currently partial (papers + figures only) · grow to full coverage | Phase 2 |
| Cloudflare R2 / Backblaze B2 / Wasabi backup destinations | Standby in mockup · enable when storage costs justify | Phase 2 |
| Sandbox build "real" execution | Vercel Sandbox API integration is non-trivial · mock for v1 | Phase 2 |
| Public profile follow / share / hubify.app/u/<handle> public pages | Requires auth + cross-user data model | Phase 2 |
| Cross-lab knowledge browser | Requires multi-lab data model + permissions | Phase 2 |

### 32.3 v1 MVP cut — week-by-week

**Week 1: Repo + Convex schema + auth**
- Create `hubify-projects/hubify-labs` repo (NEW, untouched bigbounce stays separate)
- Convex project · 50 tables from §31.8 · Convex Auth (passkey + email)
- Vercel project · `hubify.app` domain · auth gate (Houston-only at first)
- Acceptance: empty Director view loads, Houston is logged in, Convex tables exist

**Week 2: Mockup → real components**
- Port mockup `index.html` → Vite + React (or Next.js App Router) · component-by-component
- Lock in CSS variables, sage accent, sidepeek pattern, cosmic orb
- Wire navigation, sidebar, preview tab bar, status bar, chat panel chrome
- Acceptance: navigate all 25 views with mock data from Convex seed

**Week 3: BigBounce data import**
- Read-only import of 53 experiments, 4 papers, 16 contributions, 142 wiki entities from `~/CODE_2025/bigbounce/` (one-way, COPY only)
- Populate Convex tables with real data
- Acceptance: Director view shows real BigBounce stats; clicking through every view shows real data

**Week 4: Agent host + first 5 agents**
- Fly.io machine running Claude Code as the orchestrator runtime
- 5 agents online: bigbounce-orchestrator + research-lead + paper-lead + anomaly-lead + gpu-manager
- Convex Agent integration for memory + comms + standups
- Acceptance: agents post to Comms feed, write to Memory, run a no-op standup

**Week 5: Compute pipeline**
- RunPod API integration · pod lifecycle · checkpoint/resume
- Idle GPU watchdog (every 5min) · proactive launch from queue
- Houston Method v2 enforcement (state machine + post-experiment hooks)
- Acceptance: launch a real BigBounce-style experiment from the UI, watch it complete + auto-trigger Houston Method protocol

**Week 6: Cross-model peer review**
- Wire OpenAI / Google / xAI / Perplexity APIs
- Build the interpretation pass (FACT/OPINION/HALLUCINATION classifier)
- Trigger on paper draft + novelty claim events
- Acceptance: submit a paper draft, get 3 cross-model reviews + an orchestrator-synthesized verdict

**Week 7: Site generation + deploy pipeline**
- Site-worker generates static HTML from Convex data
- Vercel deploy webhook · lighthouse run · 6 routes (homepage, papers, figures, etc.)
- Acceptance: clicking Deploy in the Site view actually pushes a new bigbounce.hubify.app build

**Week 8: Polish + invite-only beta**
- Mobile responsiveness sweep (5 breakpoints)
- Accessibility audit (keyboard nav, focus rings, ARIA labels)
- Performance pass (Lighthouse 95+ all)
- Invite 3-5 cosmology researchers as beta testers
- Acceptance: external user can browse Houston's public profile + view shared knowledge

### 32.4 What "almost ready for development" means

✅ **Ready:**
- Visual design (mockup)
- Interaction patterns (sidepeek, NO MODALS, click contracts)
- Data model (50 Convex tables, §31.8)
- Agent hierarchy (21 agents, §3)
- Cron schedule (24 routines, §18 + §27)
- Cost envelope (~$30/day at BigBounce scale, §11)
- Houston Method v2 state machine (§13 + §23)
- Cross-model peer review pipeline (§29)

⚠️ **Almost ready (small gaps):**
- API surface for each Convex table — **need:** Convex function signatures (queries + mutations) generated from §31.8 mapping
- TypeScript types — **need:** `convex/schema.ts` with full Zod definitions
- Auth model — **need:** Decision on Convex Auth vs Clerk vs custom; Houston-only initially or invite-list
- Test plan — **need:** Acceptance tests for each week of §32.3
- Deploy pipeline — **need:** Vercel + Convex deploy hooks wired

🔴 **Not ready (must decide before week 1):**
- **Repo name:** `hubify-labs` confirmed? Or something else?
- **Domain:** `hubify.app/labs` subpath, or `labs.hubify.app` subdomain, or fresh `hubifylabs.com`?
- **Auth provider:** Convex Auth (free, integrated) vs Clerk (more features, $25/mo)?
- **Agent host hosting:** Fly.io confirmed (Modal dropped from the platform 2026-04-08 per §24)
- **Migration cutoff:** When does BigBounce switch from current Vercel deploy to the new Hubify Labs platform? Suggest week 7.

### 32.5 Risk register for the dev phase

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Convex query patterns don't match the UI's data needs | Medium | High | Build week 1 schema with real data shapes from BigBounce, not abstract ones |
| Sidepeek renderer count balloons past 26 as new features land | Medium | Low | Already established the pattern · adding renderers is cheap (~30 min each) |
| Cosmic orb / verb rotation breaks during React port | Low | High | Lock the CSS animations + JS rotation as a single React component, do not refactor |
| Cross-model peer review costs spiral | Medium | Medium | Per-provider monthly caps already in §29.8 · enforce strictly |
| Houston abandons director seat early (autonomous mode too soon) | High | Catastrophic | The platform makes "fully autonomous" available but Houston explicitly stays in seat for 3 months · no mass actions |
| BigBounce repo gets touched accidentally during migration | Low | Catastrophic | §1 IRON RULE · 4 backups · COPY-only · daily verification |
| Mockup polish iterations create technical debt | Low | Low | Mockup is single HTML file · debt isolated · React port is fresh start |
| Backup destinations fall behind | Medium | High | Backup verification cron nightly + weekly review |

### 32.6 Success criteria for v1 ship

1. Houston runs 5 BigBounce experiments via the new platform without touching CLI
2. Paper 1 v2.2.2 ships through the new cross-model peer review pipeline
3. 0 lost data incidents
4. 0 forbidden modals shipped
5. All 25 views load real data (not seed)
6. Lighthouse 95+ on every public page
7. 3+ external researchers browse Houston's public profile
8. Autonomous polish loop runs nightly (mockup-style improvements to the real platform)

---

## 33. Storage Strategy & Data Map — Single Source of Truth

**Status:** This is the master storage plan for Hubify Labs. Houston flagged that without a single coherent strategy, both he and the agents lose track of where data lives, what's backed up, and which copy is canonical. **No development work begins until this section is locked.**

**v2 update (2026-04-08):** Restructured from "12 tiers" to **5 zones** as the primary mental model. Tiers are still real (they're how zones are built), but agents and Houston now think in zones, not tiers. This collapse came from a Houston review: the 12-tier list was accurate but it was an engineer's checklist, not a leader's mental model.

### 33.1 The 5 zones (the leader's mental model)

Every file in Hubify Labs lives in **exactly one of 5 zones**. The zone is named by what the data DOES, not what tech runs it. Houston only ever asks himself one question: "which zone does this belong in?"

| Zone | Purpose | Tech | What lives here | Backup | Houston's question |
|------|---------|------|-----------------|--------|---------------------|
| **Z1 · Source** | Human-written code, docs, configs · version-controlled · diffable | GitHub (with LFS for binaries) · Local Mac is just a working mirror | `*.py`, `*.tex`, `*.md`, `*.yaml`, paper PDFs, figures, math proofs, configs | Git history is the backup · S3 Glacier nightly for catastrophic recovery | "Did I write this with my hands or did an agent compute it?" |
| **Z2 · State** | Application state · realtime · structured · queryable | Convex (DB + blob storage in one) · Fly.io for ephemeral runtime | Experiments index, papers index, agents, comms, tasks, standups, memory (4 layers), peer reviews, costs, ideas, novelty audits | Convex PITR built-in + nightly export to S3 Glacier | "Will I query this from the UI?" |
| **Z3 · Compute** | Heavy data, models, MCMC chains · agent-generated · large | RunPod network volume (the persistent part) · pod root disk = ephemeral scratch only | MCMC chains, anomaly catalogs (per-survey), trained model weights, training checkpoints, downloaded survey raw data | S3 Glacier nightly · pod root → volume every 600s checkpoint cycle | "Did a GPU produce this?" |
| **Z4 · Backup** | Universal cold backstop · the one place that has everything | S3 Glacier Deep Archive (single bucket: `s3://hubify-cold/`) · optional Backblaze B2 mirror | Nightly snapshots of Z1 + Z2 + Z3 | (it IS the backup) | "If everything else burned down, what would I restore from?" |
| **Z5 · Public** | What we share with the world · discoverable · downloadable | Hugging Face (models + datasets) · Vercel (the website) | Published models, public datasets, the bigbounce.hubify.app site | Z1 (site source) + Z3 (model source) are canonical · Z5 is derived | "Can the public see this?" |

**That's the whole mental model.** 5 zones. Five questions. Done.

### 33.2 The data flow at a glance

```
                           ┌──────────────┐
                           │  Z4 BACKUP   │  ← nightly cold copy of EVERYTHING
                           │  S3 Glacier  │
                           └──────▲───────┘
                                  │ nightly
   ┌─────────────┐    ┌───────────┴───┐    ┌───────────────┐
   │  Z1 SOURCE  │    │  Z2 STATE     │    │  Z3 COMPUTE   │
   │  GitHub +   │◄──►│  Convex +     │◄──►│  RunPod vol + │
   │  LFS + Mac  │    │  Fly runtime  │    │  pod scratch  │
   └─────┬───────┘    └───────────────┘    └───────┬───────┘
         │                                          │
         │ deploy                                   │ publish
         ▼                                          ▼
                           ┌──────────────┐
                           │  Z5 PUBLIC   │
                           │ Vercel + HF  │
                           └──────────────┘
```

Five boxes. Three primary flows (Z1↔Z2, Z2↔Z3, Z1↔Z3 via Convex caches). Two output flows (Z1→Z5 deploy, Z3→Z5 publish). One universal backup (everything → Z4 nightly).

### 33.3 The hubify.storage API — agent contract

Every agent has **one line of system prompt** about storage:

> *"You can read from Z1, Z2, Z3, Z5 via the standard tools. Writes go to Z1 via git, Z2 via convex, Z3 via the storage API. Backups (Z4) are automatic — never write there directly. Before any non-trivial operation, check `map.md` in the lab repo."*

The **storage API** is one Python/TS library: `hubify.storage`. It exposes 4 verbs:

```python
from hubify import storage

# Read — works for any zone the caller has permission for
content = storage.read("code://arxiv/main.tex")          # Z1
exp = storage.read("state://experiments/EXP-053")        # Z2 (returns Convex row)
chain = storage.read("data://chains/dneff/spin_torsion.1.txt")  # Z3
model = storage.read("public://models/spectral-autoencoder-47k") # Z5

# Write — same path scheme · routes to the right tech
storage.write("code://arxiv/main.tex", new_content)      # → git working copy + auto-commit
storage.write("state://experiments/EXP-053", {...})      # → Convex mutation
storage.write("data://chains/dneff/spin_torsion.1.txt", chunk)  # → RunPod vol + checkpoint cron

# Publish — promotes to Z5
storage.publish("data://models/spectral_ae_47k.safetensors",
                public_id="hubify-projects/spectral-autoencoder-47k")  # → HF Hub

# Locate — returns every zone where this file exists + last verified
locs = storage.locate("desi_dr1_anomalies.csv")
# → [{"zone":"Z3","tier":"runpod-vol","verified":"2026-04-08T02:14"},
#    {"zone":"Z4","tier":"s3-glacier","verified":"2026-04-08T02:14"}]
```

**Path prefix routing:**

| Prefix | Zone | Tech routed to |
|--------|------|----------------|
| `code://` or `arxiv://` or `wiki://` | Z1 | Git working copy (paper-lead, figure-worker) |
| `state://...` | Z2 | Convex queries/mutations |
| `data://chains/...` or `data://models/...` or `data://catalogs/...` | Z3 | RunPod volume (anomaly-lead, cosmology-worker) |
| `public://models/...` | Z5 | Hugging Face Hub (paper-lead approves) |
| `public://site/...` | Z5 | Vercel Blob (site-worker) |
| `runtime://locks/...` | Z2 (Fly subset) | Fly.io machine state |

Agents NEVER deal with S3 or LFS directly. The library handles routing, locking, retries, checksum verification, and the backup chain. Z4 writes happen automatically via the backup-worker cron.

### 33.4 Tier implementations (engineering detail)

The 5 zones are built on **8 tiers** that the engineering team needs to know about. This is the "what tech do we provision" view, not the "where does this belong" view.

| Zone | Tier | Tech | Used | Cost/mo | Notes |
|------|------|------|------|---------|-------|
| **Z1 Source** | T1 | Local Mac SSD (`~/CODE_2025/<lab>/`) | 64 GB | $0 | Houston's working mirror of Z1 |
| Z1 Source | T2 | GitHub (`github.com/hubify-projects/<lab>`) | 480 MB | $0 | Source of truth for Z1 |
| Z1 Source | T2-LFS | GitHub LFS (within T2) | 340 MB | $0 (under 1GB) | Large versioned binaries — same repo, different storage backend |
| **Z2 State** | T4 | Convex DB + blob storage | 8.4 GB | $25 | Application state · realtime sync |
| Z2 State | T10 | Fly.io machine + 10 GB volume | 4 GB | $5 | Always-on agent runtime · process locks · ephemeral runtime state |
| **Z3 Compute** | T7 | RunPod network volume (`bigbounce-data`, 1 TB) | 428 GB | $2.80 | Persistent shared compute storage |
| Z3 Compute | T6 | RunPod pod root (`/workspace`, ephemeral) | 134 GB | (incl in pod $/hr) | Scratch only · dies with pod · checkpoints to T7 every 600s |
| **Z4 Backup** | T8 | AWS S3 Glacier Deep Archive | 428 GB | $1.55 | Universal backstop · 12-48h restore |
| Z4 Backup | T11 (opt) | Backblaze B2 (peace-of-mind redundant) | 0 (standby) | $0 standby / $0.32 enabled | Optional second backup · NOT in critical path |
| **Z5 Public** | T9 | Hugging Face Hub | 8.9 GB | $0 | Public models + datasets |
| Z5 Public | T12 | Vercel Blob + Vercel Sandbox | 200 MB | $0 | Static site + ephemeral vibe-coding |
| **Total** | **8 active tiers** | (across 5 zones) | **~510 GB** | **~$35/mo** | (Backblaze adds $0.32 if enabled) |

**What changed in v2 vs v1 (the original 12 tiers):**

| v1 (engineer's view) | v2 (zone view) | Why |
|----------------------|----------------|-----|
| T1 Local + T2 GitHub + T3 GitHub LFS as 3 separate tiers | All inside **Z1 Source** (T1 + T2 + T2-LFS) | LFS is a GitHub feature, not a separate provider. Local is just a mirror of GitHub. |
| T4 Convex + T5 Convex Storage as 2 separate tiers | Both inside **Z2 State** (T4 only) | Convex blobs are still Convex; not a separate provider. |
| T6 Pod root + T7 Network vol as 2 separate tiers | Both inside **Z3 Compute** (T7 primary, T6 = ephemeral scratch) | Pod root is just the scratch space of the compute zone. |
| T10 Fly machine as its own tier | Folded into **Z2 State** (Fly = ephemeral runtime state) | Fly state is conceptually app state |
| T11 Backblaze as its own tier | Optional within **Z4 Backup** | Pure redundancy, not in critical path |

**Net result:** 12 tiers → 8 tiers (5 main + 3 supporting), grouped into 5 zones. The data type matrix in §33.5 still works — just relabeled to use zones in the "Primary" column.

Every file in Hubify Labs lives in **exactly one of these 12 tiers** (its "primary" location). It MAY also exist in a secondary location for backup or distribution. Anything not on this list is forbidden.

| Tier | What it is | Primary purpose | Persistence | Capacity | Cost | Backed up to |
|------|------------|-----------------|-------------|----------|------|--------------|
| **T1 · Local** | `~/CODE_2025/<lab>/` on Houston's Mac | Houston's working copy · daily editing | Until disk fails | 1 TB SSD | $0 | T2 (auto via git) + T11 (nightly rsync) |
| **T2 · GitHub** | `github.com/hubify-projects/<lab>` | Source of truth for code, paper sources, wiki, configs | Forever (GitHub) | 100 GB soft / unlimited paid | $0–4/mo | T3 (GitHub LFS) for binaries · T8 (S3 Glacier) for full clones nightly |
| **T3 · GitHub LFS** | Large files tracked via Git LFS in T2 | Versioned binaries (compiled PDFs, figures, small models) | Forever | 1 GB free / 50 GB $5/mo | $0–5/mo | T8 (S3 Glacier) |
| **T4 · Convex DB** | Convex tables (50 from §31.8) | Application state · structured records · realtime sync | Forever (Convex managed) | Pay per row · ~10 GB at BigBounce scale | $25–100/mo | Convex's built-in PITR + nightly export to T8 |
| **T5 · Convex Storage** | Convex blob storage (refs from T4 rows) | Small files referenced by application state (avatar PNGs, attached snippets, generated thumbnails) | Forever | Pay per GB | $0.20/GB/mo | T8 (S3 Glacier) |
| **T6 · RunPod pod root** | `/workspace` on the active pod | Ephemeral compute scratch · current run's intermediate state | Dies with pod (47d uptime typical) | 100 GB ephemeral | included in pod $/hr | T7 (every checkpoint), T8 (nightly) |
| **T7 · RunPod network volume** | `bigbounce-data` (1 TB) attached to pods | Persistent shared storage across pods · MCMC chains · model weights · downloaded survey data | Forever (until volume deleted) | 1 TB · $2.80/mo · expandable | $2.80/TB/mo | T8 (S3 Glacier nightly) + T9 (HF Datasets for public catalogs) |
| **T8 · AWS S3 Glacier Deep Archive** | `s3://hubify-cold/` | Disaster recovery · long-term cold backup of every other tier | Forever | Unlimited | $0.0036/GB/mo · 12-48h restore | (it IS the backup) |
| **T9 · Hugging Face Hub** | `huggingface.co/hubify-projects/<dataset-or-model>` | Public sharing of datasets and trained models · cross-lab discovery · external collaboration | Forever | Free for public · paid for private | $0 | T8 (we keep our own cold copy) |
| **T10 · Fly.io machine** | `bigbounce-host.fly.dev` (Fly volumes) | Always-on agent runtime · small persistent state for orchestrator (process locks, websocket state, log tails) | Forever (paid plan) | 10 GB (small) | $5/mo | Convex (T4) for state · T8 for any file dumps |
| **T11 · Backblaze B2** (optional) | `b2://hubify-redundant/` | Houston's "peace of mind" extra cold copy of T1 + T2 · pure redundancy, not in critical path | Forever | $0.005/GB/mo | $5–15/mo | (it IS a redundant backup) |
| **T12 · Vercel Blob + Vercel Sandbox** | Vercel-managed blob storage + ephemeral sandboxes | Static site assets · vibe coding ephemeral artifacts | Forever (blob) / ephemeral (sandbox) | 5 GB free / paid | $0–20/mo | T8 for blob assets · sandbox is throwaway |

**Layers we explicitly DO NOT use:**
- Cloudflare R2, Wasabi: standby in the mockup but not in the data flow until cost justifies. (~$0/mo while standby.)
- Google Drive, Dropbox: not in scope. Personal cloud, not for research.
- Local NAS: not in scope. Houston travels.
- Direct S3 (hot storage): too expensive vs Glacier for our access patterns.

### 33.5 Data type → zone matrix

Every data type in the lab has **one** primary zone. Agents and Houston always know where to look first. The "Primary" column now uses zone names (Z1-Z5) — the underlying tier implementation is in §33.4.

| Data type | Example file/object | Primary | Secondary (auto-backup) | Why this zone |
|-----------|---------------------|---------|------------------------|---------------|
| **Source code** | `pipeline_p1.py` | **Z1** Source | Z4 nightly | Human-written, versioned, frequently edited |
| **Paper LaTeX source** | `arxiv/main.tex` | **Z1** Source | Z4 nightly | Human-written, versioned, peer-edited |
| **Compiled paper PDF** | `arxiv/main.pdf` | **Z1** Source (LFS) | Z4 nightly · Z5 when published | Versioned binary |
| **Wiki entries** | `wiki/quintom-b.md` | **Z1** Source | Z2 indexed cache · Z4 nightly | Human-written markdown · indexed in Z2 for fast queries |
| **Math proofs** | `proofs/f_nl_derivation.lean` or `.tex` | **Z1** Source | Z4 nightly | Human-written source-of-truth |
| **Config files** | `cobaya/full_tension.yaml` | **Z1** Source | Z4 nightly | Human-written, small |
| **Notebooks** | `analysis/desi_qc.ipynb` | **Z1** Source | Z4 nightly (outputs stripped before commit) | Human-written, medium |
| **MCMC chains** (raw) | `chains/dneff/spin_torsion.1.txt` | **Z3** Compute | Z4 nightly · Z5 if shared | Agent-generated, large, append-only |
| **MCMC chain summaries** | `chain_means_latest.csv` | **Z1** Source | Z2 cached · Z4 nightly | Small enough to version-control |
| **Anomaly catalogs** (per survey) | `desi_dr1_anomalies.csv` (14 GB) | **Z3** Compute | Z4 nightly · Z5 public release | Agent-generated, large, shared across pods |
| **Anomaly catalog samples** (first 100 rows) | `dataset_samples` table | **Z2** State | Z4 nightly export | Queried by Data view sample-row preview |
| **Trained model weights** | `models/spectral_ae_47k.safetensors` | **Z3** Compute | Z4 nightly · Z5 when published | Agent-generated, immutable post-training |
| **Model training checkpoints** | `models/chirality_cnn/epoch_03.pt` | **Z3** Compute (scratch) | Z3 vol every 600s · Z4 nightly | Frequent writes during training, ephemeral until checkpointed |
| **Survey raw spectra** (DESI, SDSS, etc.) | `desi_dr1/spectra.fits` (184 GB frozen) | **Z3** Compute | Z4 · upstream survey is canonical | Re-fetchable from upstream if needed |
| **Survey download cache** | `cache/desi_dr1/coadd_*.fits` | **Z3** Compute (scratch) | (none — re-fetchable) | Ephemeral |
| **Figures** (PNG/SVG/PDF) | `public/images/fig07_dneff.png` | **Z1** Source (LFS) | Z4 nightly · Z5 (Vercel Blob for site) | Versioned binaries served by site |
| **Figure source scripts** | `figures/fig07_dneff.py` | **Z1** Source | Z4 nightly | Human-written, regenerates the binary |
| **Site static assets** | `bigbounce.hubify.app/_next/...` | **Z5** Public | Z1 source HTML in repo · Z4 | Built artifact, regenerated from Z1 |
| **Standup transcripts** | `standups[date].messages[]` | **Z2** State | Z4 nightly export | Queried by Standups view |
| **Activity events** | `comm_events[]` | **Z2** State | Z4 nightly export · 90d retention | High-volume, time-ordered |
| **Agent memory** (4 layers) | `memories_{user,agent,lab,global}` | **Z2** State | Z4 nightly export | Realtime sync, cross-session |
| **Tasks + comments + reviews** | `tasks[]`, `task_comments[]` | **Z2** State | Z4 nightly export | Application state |
| **Cross-model peer reviews** | `peer_reviews[]`, `interpretation_passes[]` | **Z2** State | Z4 nightly export | Application state |
| **Cost / billing logs** | `costs_daily[]`, `costs_provider[]` | **Z2** State | Z4 nightly export | Application state |
| **Agent runtime state** | process locks, websocket sessions, log tails | **Z2** State (Fly subset) | Z2 mirrored · Z4 dumps | Per-process, ephemeral-ish |
| **Vibe coding sandbox artifacts** | `sandbox/<id>/output.png` | **Z5** Public (Vercel Sandbox) | Z2 if Houston says "save" · Z4 | Ephemeral by default, promotable |
| **Hugging Face published model** | `hubify-projects/spectral-autoencoder-47k` | **Z5** Public | Z3 source · Z4 cold copy | Public discovery + download |
| **Hugging Face published dataset** | `hubify-projects/desi-anomalies-dr1` | **Z5** Public | Z3 source · Z4 cold copy | Public discovery + download |

**Backup rule:** every primary zone has at least one secondary that lives in Z4. Z4 (S3 Glacier) is the universal backstop — if Z1 + Z2 + Z3 + Z5 all vanished, Z4 alone can rebuild everything.

### 33.6 Data flow rules (the contract)

These rules are enforced by agents. Violations trigger alerts.

1. **Source code edits** flow `T1 → T2` via `git push` (manual or paper-lead/site-worker). Backup `T2 → T8` nightly (via cron).

2. **Large binary outputs** (compiled PDFs, figures, models) flow `T1 → T3` (Git LFS) on commit. Backup `T3 → T8` nightly.

3. **MCMC chain runs** flow `T6 → T7` after each checkpoint cycle (every 600s by default). Backup `T7 → T8` nightly. Never on T6 alone past checkpoint window.

4. **Anomaly catalog generation** writes directly to `T7` to avoid the ephemeral-T6-loss problem. Sample row preview (first 100 rows) is mirrored to `T4` for the Data view.

5. **Wiki + paper edits** flow `T2 → T4` via a periodic indexing cron (every 5 min). The Wiki view reads from T4 (fast queries) but the source of truth is T2 (versioned).

6. **Agent memory writes** flow only to `T4`. Periodic export `T4 → T8` nightly.

7. **Site builds** flow `T2 → T12 Vercel` on push to main. Static assets land on Vercel Blob (T12); the source HTML is rebuilt fresh on every deploy.

8. **Cross-lab dataset sharing** = `T7 → T9 Hugging Face` via the publish pipeline (manual approval). Once on HF, other labs can `pip install` or `huggingface_hub download` it.

9. **Backup verification** runs nightly at 02:14 across T1-T9 + T11. Stale (>24h) backups trigger a warn alert.

10. **Restore drill** runs monthly. Pick a random file, delete the secondary, restore from primary, verify checksum.

### 33.7 Per-project `map.md` — auto-updating storage atlas

Every lab repo has a `map.md` file at the root that documents its storage layout. **Agents auto-update it when they create / move / delete data.** Houston can `cat map.md` from anywhere to see the full picture.

Format:

```markdown
# Storage Map · bigbounce
*Auto-updated by storage-map-worker · last refresh: 2026-04-08 06:14*

## Tier inventory

| Tier | Used | Files | Notes |
|------|------|-------|-------|
| T1 Local | 64 GB | 12,840 | working copy on Houston's Mac |
| T2 GitHub | 480 MB | 8,920 | source code, paper LaTeX, wiki, configs |
| T3 GitHub LFS | 340 MB | 47 | compiled PDFs + figures |
| T4 Convex DB | 8.4 GB | (50 tables) | application state |
| T5 Convex Storage | 120 MB | 88 | thumbnails + small attachments |
| T6 RunPod pod root | 134 GB | (ephemeral) | current Phase 4 run scratch |
| T7 RunPod network vol | 428 GB | 12 datasets | MCMC chains, model weights, anomaly catalogs |
| T8 S3 Glacier | 428 GB | 12 datasets + 8 nightly snapshots | disaster recovery |
| T9 Hugging Face | 8.9 GB | 3 models + 5 datasets | public sharing |
| T10 Fly volume | 4 GB | (ephemeral) | orchestrator state |

## Critical files (top 20 by importance)

1. `arxiv/main.tex` · T2 · also T1 + T8 nightly
2. `arxiv/main.pdf` · T3 LFS · also T1 + T8 nightly
3. `chains/dneff/spin_torsion.*.txt` · T7 RunPod vol · also T8 nightly
4. `pipelines/p3_anomaly_engine/desi_dr1_anomalies.csv` · T7 (14.2 GB) · also T8 nightly
5. `models/spectral_ae_47k.safetensors` · T7 (362 MB) · also T8 + T9 published
... (full list)

## Recent flows (last 24h)

- 02:14 nightly: T2/T3/T4/T5 → T8 export (12 GB, 47m 12s, $0.03)
- 04:13: T6 → T7 checkpoint cycle for EXP-054 (Planck mask re-run)
- 06:14: storage-map-worker refreshed this file

## Mermaid diagram

\`\`\`mermaid
flowchart LR
  Houston[👤 Houston Mac<br/>T1 Local 64GB]
  GitHub[GitHub<br/>T2 480MB]
  LFS[GitHub LFS<br/>T3 340MB]
  Convex[Convex DB<br/>T4 8.4GB]
  Pod[RunPod /workspace<br/>T6 ephemeral]
  Vol[RunPod bigbounce-data<br/>T7 428GB]
  S3[S3 Glacier<br/>T8 428GB]
  HF[Hugging Face<br/>T9 8.9GB published]
  Vercel[Vercel<br/>T12 site assets]

  Houston -- git push --> GitHub
  Houston -- git lfs --> LFS
  GitHub -- nightly export --> S3
  LFS -- nightly --> S3
  Convex -- nightly export --> S3
  Pod -- checkpoint 600s --> Vol
  Vol -- nightly backup --> S3
  Vol -- publish flow --> HF
  GitHub -- vercel deploy --> Vercel
  Vercel -- nightly --> S3
\`\`\`

## Where each agent reads/writes

- **paper-lead** reads T1/T2, writes T2 (paper sources)
- **anomaly-lead + workers** read T7, write T7 (catalogs) + T4 (samples)
- **figure-worker** reads T7, writes T1 (then T2/T3 via git)
- **backup-worker** reads everything, writes T8 (and T11 if enabled)
- **storage-map-worker** (this file's owner) reads everything, writes this file
```

### 33.8 storage-map-worker — the new agent

A new agent in the roster: `storage-map-worker` (haiku 4.5, LOW reasoning).

**Job:**
- Owns the per-project `map.md` file
- Refreshes every 6 hours OR on-demand (e.g. after a backup-worker run)
- Walks each tier and inventories file count, total size, top files
- Regenerates the Mermaid diagram from the actual flow data
- Surfaces drift (e.g. "T7 has files not backed up to T8 in 48h")
- Posts to comm_events when something is wrong

**Tools:**
- read git tree (T1, T2, T3)
- query Convex (T4, T5)
- ssh to RunPod pod for T6 + T7 walks
- AWS CLI for T8 inventory
- HF API for T9 inventory
- Fly CLI for T10 inventory

**Routing:** LOW reasoning · scheduled fire only · 4 fires/day · ~$0.20/day cost.

### 33.9 Agent storage knowledge contract

Every agent on the platform MUST know:

1. **Which tiers exist** (the 12 from §33.2). Hardcoded in their system prompt. Listed in their knowledge base.
2. **Which data types live where** (the matrix from §33.3). Updated automatically when the matrix changes.
3. **The map.md location** for the current lab (always at repo root). They `cat map.md` before any non-trivial storage operation.
4. **Their own read/write rights** per tier. (Not all agents have S3 credentials. Agent `paper-lead` cannot write to T7 directly; it must request via `anomaly-lead`.)

Operational rule: **before any agent writes a file, it consults `map.md` and §33.3 to determine the correct primary tier.** If unclear, it pauses and asks the orchestrator. Wrong-tier writes are reverted by `storage-map-worker` on the next refresh and a `comm_events` warning is posted.

### 33.10 The mockup's Files sidebar — grouping by zone

This is the UX implementation of §33.7 in the mockup. The Files mode of the sidebar will show file groups toggled by storage tier:

```
─ bigbounce/ ────────────────────────
  ▼ T1 Local (64 GB · 12,840 files)
    ▼ arxiv/
       main.tex      [T1·T2·T8]   ●
       main.pdf      [T1·T3·T8]   ●
       references.bib [T1·T2·T8]  ●
    ▼ pipelines/
       ...

  ▼ T2 GitHub (480 MB · 8,920 files · in sync)
    (mirror of T1 minus .gitignored)

  ▶ T3 GitHub LFS (340 MB · 47 binaries)
  ▶ T4 Convex (8.4 GB · 50 tables)
  ▶ T7 RunPod vol (428 GB · 12 datasets)
  ▶ T8 S3 Glacier (428 GB · backup snapshots)
  ▶ T9 Hugging Face (8.9 GB · 3 models · 5 datasets)
  ─────────
  [+ New file]   [Open map.md]   [Refresh tiers]
```

**Conventions:**
- The bracketed pill `[T1·T2·T8]` next to each file shows every tier it currently lives in. Sage tiers = primary. Grayscale tiers = backup. Red tier = stale (last sync >24h).
- Each file row has a small **backup status dot**: ● = backed up to ≥2 tiers (safe), ◐ = 1 backup, ○ = primary only (warning).
- Click the pill → opens a `file-locations` sidepeek showing every copy + sha256 + last verified.
- "Open map.md" button at the bottom opens the auto-updated map in the file preview tab.

### 33.11 The Data Map view (new view in the mockup)

A new top-level view in the sidebar nav: **Data Map**. Renders the per-project Mermaid diagram from `map.md` with:

- Storage tiers as nodes (with current usage / capacity)
- Data flows as directed edges (with frequency / size)
- Color-coded by tier type: local (gray), VCS (sage), Convex (sage), GPU compute (warn dim), backup (gray dim), public (sage bright)
- Click any node → opens the corresponding sidepeek (`backup-dest` for tiers we already have, new sidepeeks for the rest)
- "Drift" badge appears on any node where data is stale or out of sync

This view is the **single page Houston opens to feel safe about his data.** It is the visual answer to "where is everything and is it backed up?"

### 33.12 Estimated monthly storage cost (BigBounce scale)

| Tier | Usage | $/mo |
|------|-------|------|
| T1 Local | 64 GB | $0 |
| T2 GitHub | 480 MB | $0 |
| T3 GitHub LFS | 340 MB | $0 (under 1 GB free) |
| T4 Convex | 8.4 GB · 50 tables | $25 |
| T5 Convex Storage | 120 MB | $0 |
| T6 RunPod pod root | (in pod $/hr) | $0 (already counted) |
| T7 RunPod network vol | 428 GB · 1 TB allocated | $2.80 |
| T8 S3 Glacier Deep Archive | 428 GB | $1.55 |
| T9 Hugging Face | 8.9 GB · public | $0 |
| T10 Fly volume | 10 GB | $5 |
| T11 Backblaze (optional) | 64 GB peace-of-mind | $0.32 |
| T12 Vercel Blob | 200 MB | $0 |
| **Total** | **~510 GB across all tiers** | **~$35/mo** |

For BigBounce-scale data, the entire storage spread costs less than a single dinner. The expensive tiers (Convex, Fly) are paying for **service** (realtime sync, always-on), not storage.

### 33.13 Migration plan (week 1 of dev phase)

When the dev phase begins:

1. **Day 1:** Provision T4 (Convex), T7 (RunPod network vol if not already), T8 (S3 bucket + Glacier transition policy), T9 (HF org), T10 (Fly machine), T11 (Backblaze if Houston wants it).
2. **Day 2:** Wire backup crons. Verify nightly export `T4 → T8` works.
3. **Day 3:** Run migration script: `T1 → T2` (commit anything not yet pushed) and `T1 → T7` (rsync chains and catalogs to network vol).
4. **Day 4:** Initial backup pass: `T1-T7 → T8`. Estimate 6h for the first full sync.
5. **Day 5:** Spawn `storage-map-worker` for the first time. Generate initial `map.md` for bigbounce.
6. **Day 6:** Verify drift detection works (manually pause a backup, watch the alert fire).
7. **Day 7:** Houston signs off on the Storage Map view in the UI. Lab is "storage-ready."

**No experiments run until §33.11 day 7 is complete.** This is non-negotiable because losing data is catastrophic and storage architecture mistakes are expensive to fix later.

### 33.14 Knowledge Wiki view — how `view-knowledge` maps to storage

**Status:** Locked 2026-04-08. Subsection fill for the underspecified `view-knowledge`.

**The Wiki is the lab's structured long-term memory.** It's a Karpathy-style knowledge base of entities, concepts, sources, and comparisons. It's the place where "what we know" is recorded between experiments — distilled, deduplicated, citable. The mockup's `view-knowledge` is the human surface to this knowledge base.

**Where the wiki lives (zone-aware).**

| Wiki content | Storage zone | Tier | Format | Why |
|---|---|---|---|---|
| Entity files (e.g., `quintom-b.md`, `f_nl-prediction.md`) | Z1 (source) | T1 + T2 GitHub | Markdown with YAML frontmatter | Version-controlled, diffable, agents can read raw |
| Concept files (e.g., `bayes-factor.md`, `landy-szalay.md`) | Z1 (source) | T1 + T2 GitHub | Markdown | Same — these are human-curated knowledge |
| Source files (e.g., `cai-2024.bib`, `chen-2023.bib`) | Z1 (source) | T1 + T2 GitHub + T3 LFS for PDFs | BibTeX + PDF (LFS) | Source PDFs are large binaries |
| Comparison tables (e.g., `bounce-discrimination.md`) | Z1 (source) | T1 + T2 GitHub | Markdown tables | Diffable, citable from papers |
| Wiki search index | Z2 (state) | T4 Convex | Inverted index for fast search | Hot path for `⌘K` universal search |
| Cross-lab share manifest | Z2 (state) | T4 Convex | JSON | What this lab shares with other labs |
| Knowledge graph edges (citation graph) | Z2 (state) | T4 Convex | Adjacency list | Powers the citation graph SVG in the view |

**View layout (full spec for `view-knowledge`).**

```
┌─ view-knowledge ────────────────────────────────────────────┐
│  Section header: "Knowledge wiki — 142 entries · 89 entities│
│                  · 47 sources · 6 comparisons"              │
│  Filter chips: All | Entities | Concepts | Sources | Comp.  │
│  Search input (⌘K compatible)                                │
│                                                              │
│  3-column grid:                                              │
│  ┌─ Entities (89) ─┐ ┌─ Concepts (47) ─┐ ┌─ Sources (47) ─┐│
│  │ • quintom-b     │ │ • bayes-factor  │ │ • cai-2024     ││
│  │ • f_nl-pred     │ │ • landy-szalay  │ │ • chen-2023    ││
│  │ • bounce-models │ │ • novelty-score │ │ • nanograv-15  ││
│  │   (click → wiki │ │   ...           │ │   ...          ││
│  │    sidepeek)    │ │                 │ │                ││
│  └─────────────────┘ └─────────────────┘ └────────────────┘│
│                                                              │
│  Section: "Bounce model discrimination" (5×7 comparison tbl) │
│                                                              │
│  Section: "Citation graph" (SVG showing how sources connect) │
│                                                              │
│  Section: "Cross-lab sharing" (what we share with other labs)│
└─────────────────────────────────────────────────────────────┘
```

**The agent contract.** Every lab has a `wiki-worker` agent (per PRD §3) that owns the wiki:
- **Reads:** every agent in the lab can read the wiki (it's the shared knowledge layer)
- **Writes:** ONLY `wiki-worker` writes to wiki files (after a 2-step propose-then-commit flow)
- **Updates trigger:** every successful experiment that produces a result the orchestrator deems wiki-worthy fires a `wiki.propose_update` event
- **Cross-lab sharing:** the wiki respects the Lab Sovereignty Rule (PRD §40.11) — other labs can READ this lab's wiki (if `public_visibility: published-only`) but never WRITE to it; updates from other labs come in as comm messages that the wiki-worker can accept or reject

**Sidepeek behavior.** Clicking any entity, concept, source, or comparison in the view opens a sidepeek showing:
- Full markdown content rendered
- YAML frontmatter (created/updated/contributors/related)
- Recent edit history (last 5 commits with diffs)
- Outbound links (other wiki entries that reference this one)
- Inbound links (what references this one)
- "Open raw .md" button (jumps to `view-file` with the source open)

**What's IN scope for view-knowledge v1:** the 3-column grid + search + filters + comparison table + citation graph + cross-lab sharing card + wiki sidepeek.

**What's OUT of scope (deferred to v1.1):** wiki edit-in-place from the UI (v1 you edit via `view-file` or via the CLI `hubify note` style flow), wiki-graph view (the citation SVG is enough for v1), federated cross-lab wiki search.

---

## 34. Agent File Structure — indydevdan-style self-improving agents

**Status:** This section locks the on-disk structure that every agent uses. It mirrors the file layout from [indydevdan](https://github.com/disler) (the `ui-agents`, `lead-agents`, `ceo-agents` repos and the broader Claude Agent SDK pattern). Houston explicitly asked that we adopt the same structure so the agents are coherent, self-improving, and visible from the UI.

### 34.1 Why this structure

The indydevdan pattern treats agents as **directories of source files**, not as hidden API config. Every agent has a public, version-controlled identity with:

- A clear role definition (`agent.md`)
- A personality / voice (`soul.md`)
- A directory of teachable skills (`skills/`)
- A learnings log that grows over time (`learnings.jsonl`)
- A memory of what they've done (`episodes.jsonl`)
- Their model selection and tool grants

This makes agents:
1. **Inspectable** — Houston (and other agents) can `cat agent.md` to know what they do
2. **Editable** — improving an agent is editing files, not API calls
3. **Diffable** — `git log agents/paper-lead/` shows how the agent has grown
4. **Self-improving** — agents can append to their own `learnings.jsonl` and update their own `soul.md` over time
5. **Composable** — the orchestrator can spawn new agents by scaffolding new directories from a template

### 34.2 The directory layout

Every agent lives in `~/.hubify/agents/<agent-id>/` (or per-lab in `<lab>/.agents/<agent-id>/` for lab-scoped agents):

```
agents/paper-lead/
├── agent.md                  # core role · model · tools · system prompt outline
├── soul.md                   # personality · voice · style preferences · tone
├── skills/                   # directory of teachable skills
│   ├── revtex-compile/
│   │   └── SKILL.md         # how to compile a paper with revtex4-2
│   ├── claims-table-sync/
│   │   └── SKILL.md         # how to sync the claims table with the paper text
│   ├── peer-review-request/
│   │   └── SKILL.md         # how to dispatch a paper to cross-model peer review
│   └── revision-tracker/
│       └── SKILL.md         # how to maintain REVISION_TRACKER.md
├── learnings.jsonl          # timestamped log of things this agent learned
├── episodes.jsonl           # timestamped log of completed tasks (memory)
├── reports_to.md            # who this agent answers to (e.g. "bigbounce-orchestrator")
├── direct_reports.md        # who answers to this agent (for leads only)
├── tools.md                 # explicit list of tools this agent can use
├── permissions.md           # what storage tiers it can read/write per §33.7
└── README.md                # human-readable overview that links the above
```

**Per-skill structure** (matches Claude Agent SDK skills):
```
skills/revtex-compile/
├── SKILL.md                 # the actual skill instructions (frontmatter + body)
└── examples/                # optional example invocations
    └── compile-paper-1.md
```

### 34.3 What each file contains

**`agent.md`** — the canonical agent definition. Frontmatter + body.

```markdown
---
id: paper-lead
name: Paper Lead
role: lead
reasoning: med-high
model: claude-sonnet-4-6
provider: anthropic
reports_to: bigbounce-orchestrator
direct_reports: [paper-worker, figure-worker, review-worker]
created: 2026-02-14
last_self_update: 2026-04-08
version: 7
---

# Paper Lead

I own the lifecycle of every research paper in this lab. From first draft through
peer review through arXiv submission, I am the agent the orchestrator calls when
something needs to happen at the paper level.

## What I do
- Draft new sections when research-lead surfaces a result worth publishing
- Coordinate with figure-worker for inline figures and citation cross-refs
- Dispatch finished drafts to peer-review-* agents for cross-model review
- Maintain claims tables and revision history
- Compile via revtex4-2 on the active RunPod pod
- Hand off to site-worker once a version is ready for deploy

## What I don't do
- I don't write source code (cosmology-worker / anomaly-worker do)
- I don't approve novelty claims (research-lead does that)
- I don't run experiments (the appropriate worker does)

## How to invoke me
- "draft section X for paper N" → I write the section
- "compile paper N" → I run pdflatex twice on the active pod
- "send paper N for review" → I dispatch to peer-review-{gpt,gemini,grok} + skeptic-cross
```

**`soul.md`** — personality, voice, taste. The agent reads this on every spawn.

```markdown
# Soul of paper-lead

I am thoughtful and careful. I read papers like a peer reviewer would: looking for the
load-bearing claim, the missing caveat, the overclaim that needs softening.

I prefer terse direct prose. I use semicolons when they're earned. I never write
"furthermore" or "moreover" — those are filler. I use "and" or just a new sentence.

I cite generously but not promiscuously. Every claim that isn't original gets a citation.

I am not a thesaurus agent. I will not change your word choice unless it actively
weakens the claim.

When the data is uncertain I say so explicitly. I would rather a paper say
"consistent with f_NL = -35/8 within current measurement uncertainty" than
"f_NL = -35/8" with a hidden hedge in a footnote.

I respect Houston's research directive: barriers narrow the search space, not conclude
it. I never recommend "publish and move on" — I recommend "publish AND propose what
to test next."
```

**`skills/<skill>/SKILL.md`** — teachable behavior. Same format as Claude Code skills.

```markdown
---
name: revtex-compile
description: Compile a LaTeX paper using revtex4-2 on the active RunPod pod, run twice
  for cross-references, verify the PDF embedded all figures, scp result to public/papers/
---

# Steps

1. Verify all referenced figures exist in the same directory as main.tex
2. SSH to the active pod (read T7 RunPod vol metadata for current pod IP)
3. Run `pdflatex -interaction=nonstopmode main.tex` twice
4. Check output PDF size — if < 1 MB the figures didn't embed (warn)
5. scp the result back to T1 → commit to T2/T3 LFS via the figure-worker
6. Update version.json + REVISION_TRACKER.md

# Common pitfalls
- aastex vs revtex4-2 — we use revtex4-2 always
- \citep / \citet are natbib — revtex4-2 uses \cite{}
- deluxetable is undefined — use \begin{table}\begin{ruledtabular}\begin{tabular}
```

**`learnings.jsonl`** — timestamped, append-only learnings the agent has accumulated.

```jsonl
{"ts":"2026-03-22T14:08:00Z","kind":"operational","insight":"on revtex4-2, longbibliography fails silently when a duplicate \\bibitem exists. workaround: dedupe references.bib first.","confidence":0.9,"source":"observed-on-paper-1-v2.1"}
{"ts":"2026-03-29T09:12:00Z","kind":"taste","insight":"Houston prefers 'consistent with' over 'matches' for observational comparisons. Less overclaiming.","confidence":1.0,"source":"houston-feedback"}
{"ts":"2026-04-07T19:14:00Z","kind":"workflow","insight":"section 7 rewrites benefit from running cross-model peer review BEFORE Houston reviews — catches GPT/Gemini hallucinations before they get in front of him.","confidence":0.85,"source":"observed-on-paper-1-v2.2.1"}
```

**`episodes.jsonl`** — timestamped task memory. What I worked on, when, what happened.

```jsonl
{"ts":"2026-04-07T19:13:00Z","task":"draft Paper 1 §7 f_NL framework rewrite","outcome":"shipped v2.2.1","duration_min":94,"cost_usd":2.14,"reviews":["gpt:approved","gemini:approved","skeptic:1-change"]}
{"ts":"2026-04-08T08:09:00Z","task":"morning standup report","outcome":"posted","duration_min":2}
```

**`reports_to.md`** / **`direct_reports.md`** — explicit hierarchy. Single line each plus an explanatory paragraph.

**`tools.md`** — every tool the agent is allowed to call (`read`, `edit`, `bash`, `convex.query`, `convex.mutation`, `s3.put`, `huggingface.upload`, etc.).

**`permissions.md`** — per-tier r/w from §33.7 (e.g. "T1 read · T2 read+write · T3 read+write · T4 read+write · T7 NO ACCESS · T8 NO ACCESS").

### 34.4 Self-improvement loop

Every agent runs a **weekly reflection** routine (cron Sunday 03:42, same slot as memory cleanup):

1. Read the last 7 days of `episodes.jsonl`
2. Identify patterns: what worked, what didn't, what surprised
3. Append new learnings to `learnings.jsonl` (with confidence + source)
4. If a learning is high-confidence and operational → propose an edit to `agent.md` or a new skill in `skills/`
5. Houston reviews the proposed edits via the **Agent diff sidepeek** (new in §34.6)
6. Approved edits commit; rejected edits go to `rejected_edits.jsonl` with the reason

This is the **self-improving** part. Agents grow over time based on their own experience, but Houston (or another reviewer agent) is in the loop for actual file edits.

### 34.5 Orchestrator can create new agents

The orchestrator (or a lead with `direct_reports` permission) can scaffold a new agent from a template:

```bash
hubify agent new \
  --id anomaly-postprocess-worker \
  --role worker \
  --reasoning low \
  --reports-to anomaly-lead \
  --template worker
```

This creates `agents/anomaly-postprocess-worker/` from the worker template (`~/.hubify/agent-templates/worker/`) with default `agent.md`, blank `soul.md`, empty `skills/`, blank `learnings.jsonl`, etc. The orchestrator then drafts the role-specific content of `agent.md` and `soul.md` based on the use case Houston gave it.

Templates exist for: `orchestrator`, `lead`, `worker`, `cross-provider-reviewer`, `skeptic`, `ceo-brainstorm` (new in §36).

### 34.6 UI surface — Agent sidepeek

The mockup's `agent` sidepeek renders all of the above as a tabbed view:

| Tab | Content |
|-----|---------|
| **Overview** | name · role · reasoning level · model · provider · reports_to · direct_reports · created · last_self_update · version · QC stats |
| **agent.md** | rendered markdown of the agent.md body (read-only preview) |
| **soul.md** | rendered markdown of the personality file |
| **Skills** | list of skills with name + description, click → opens the SKILL.md in a sidepeek |
| **Learnings** | timeline view of `learnings.jsonl` entries (ts · kind · insight · confidence · source) |
| **Episodes** | recent task history from `episodes.jsonl` |
| **Tools** | list of allowed tools |
| **Permissions** | per-tier r/w matrix from §33.7 |
| **Diff (proposed)** | self-improvement diffs awaiting Houston approval |
| **Roster controls** | promote · demote · mute · clone · delete (top-level) |

The Diff tab is the **self-improvement review surface**. Houston spends ~5 min/week here and that's how he stays in the director seat without micromanaging.

### 34.7 Migration from current 21-agent roster

The current 21 agents (`bigbounce-orchestrator`, `global-orchestrator`, 4 leads, 11 workers, 4 cross-provider reviewers) all get scaffolded into this structure during week 4 of the dev phase (§32.3). Each agent's existing system prompt and tool grants from the prototype roster get translated into `agent.md` + `tools.md`. The first `learnings.jsonl` entries are seeded from the existing memory layer (§20).

---

## 35. Hierarchy Taxonomy — Global → Labs → Projects → ... → Tasks

**Status:** Houston flagged that the levels of organization (Lab vs Project vs Pipeline vs Experiment vs Idea vs Task) need clear definitions. This section locks the taxonomy so both humans and agents use the same words for the same things.

### 35.1 The 7-level hierarchy

```
Level 0 · GLOBAL
  └── Cross-lab knowledge, cross-lab agents, billing, account
Level 1 · LAB                  (a research workspace · "team")
  └── Has its own repo · its own agents · its own compute pool
Level 2 · PRERESEARCH PROJECT  (free-flow exploration · §36)
  ├── A multi-model chat thread · not yet committed to research
  └── Can graduate into a Lab or a Research Project
Level 2 · RESEARCH PROJECT     (a long-term research thread · "epic")
  └── Has a thesis · a paper target · multiple pipelines + experiments
Level 3 · PIPELINE             (a structured multi-step procedure)
  └── A series of experiments + scripts that run in order to achieve a milestone
Level 4 · EXPERIMENT           (a single computational run with a hypothesis)
  └── Has config · runs once · produces a result · gets QC'd
Level 5 · IDEA                 (a speculative direction not yet committed)
  └── Has a viability score · may become an experiment, project, or be parked
Level 6 · TASK                 (a single discrete unit of agent work)
  └── Has an owner · has reviewers · has a status · ~minutes to hours
```

**Worked example** for BigBounce:
- **Global:** Houston's Hubify account, includes all his labs
- **Lab:** `bigbounce` (the spin-torsion cosmology workspace)
- **Preresearch project:** "Could MOND-bounce hybrid bypass ECH barriers?" (initial chat exploration)
- **Research Project:** "Branch V matter bounce + f_NL = -35/8 prediction"
- **Pipeline:** "Pipeline 1: f_NL tracer purification" (6 steps)
- **Experiment:** EXP-053 QSO Classifier (one run, 12 min, 12,920 high-z QSOs)
- **Idea:** "Anomaly tracers might amplify σ(f_NL) by 16%" (became Pipeline 1)
- **Task:** T-104 "ACT DR6 retrain val_loss < 50" (one assignable agent task)

### 35.2 Definitions and when to use each

| Level | Singular | Plural | When to use |
|-------|----------|--------|-------------|
| **Lab** | `Lab` | `Labs` | A new research **domain** (e.g. cosmology vs particle physics). Different repos, different agents, different compute. Houston has 4: bigbounce · chirality · pta-gw · quantum-gw. |
| **Preresearch Project** | `Preresearch` | `Preresearches` | An exploratory **chat thread** before committing. Multi-model. Free-flowing. Can graduate. (§36) |
| **Research Project** | `Research Project` | `Projects` | A long-term research **thread** with a thesis and a paper target. Has multiple pipelines + experiments grouped under it. BigBounce has ~3-5 active. |
| **Pipeline** | `Pipeline` | `Pipelines` | A **structured multi-step procedure** that runs to achieve a milestone. Each step is a script or experiment. BigBounce has 3 (P1 f_NL, P2 chirality, P3 anomaly engine). |
| **Experiment** | `Experiment` | `Experiments` | A **single computational run** with a clear hypothesis. Has config, runs once, gets QC'd. BigBounce has 53. |
| **Idea** | `Idea` | `Ideas` | A **speculative direction** not yet committed to compute. Has a viability score (5-dim breakdown). Can be promoted to a Pipeline, Experiment, or Research Project. BigBounce has 23. |
| **Task** | `Task` | `Tasks` | A **single agent assignment**. Has owner, reviewers, status, comments, ~minutes to hours. BigBounce has 261. |

### 35.3 Transitions — how things move up and down

```
Preresearch chat
  ├── if "this is research-worthy" → graduate to Research Project (or new Lab)
  ├── if "interesting but parked" → store as an Idea
  └── if "not worth pursuing" → archive the chat

Idea
  ├── if viability ≥ 80 → promote to Pipeline (multi-step) or Experiment (single run)
  ├── if viability 60–80 → leave as queued Idea
  └── if viability < 60 → park

Experiment
  ├── if pass + replicated → result becomes a Contribution (§22)
  ├── if pass but unique → become a step in a Pipeline OR seed a new Pipeline
  └── if fail → either retry, kill, or downgrade to a Task ("debug this")

Pipeline step
  ├── completed → next step in the pipeline runs
  ├── all steps complete → Pipeline closes, Research Project advances
  └── milestone reached → triggers a Paper draft (Research Project level)

Research Project
  ├── thesis confirmed → publish paper(s) · result is permanent
  ├── thesis falsified → close Project, log learnings, start a new direction
  └── stuck → escalate to Houston for direction

Lab
  ├── proven domain → keep growing
  ├── overlap with existing Lab → merge
  └── too small to justify own infrastructure → fold into a Project under another Lab
```

### 35.4 Where each level lives in storage

| Level | Primary tier | Notes |
|-------|--------------|-------|
| Global | T4 Convex (`accounts`, `cross_lab_*`) | Cross-lab data |
| Lab | T2 GitHub (`<lab>` repo) + T4 (`labs` table) | Each lab is a repo |
| Preresearch | T4 Convex (`preresearch_chats` table) | Ephemeral until graduated |
| Research Project | T2 GitHub (`research/<project>/` directory) + T4 (`research_projects` table) | Has its own subdirectory in the lab repo |
| Pipeline | T2 GitHub (`pipelines/<pipeline>/` directory) + T4 (`pipelines` table) | Has its own subdirectory |
| Experiment | T4 Convex (`experiments` table) + T7 RunPod (logs/outputs) | Run state in Convex, outputs on the volume |
| Idea | T4 Convex (`ideas` table) | Cheap to store thousands |
| Task | T4 Convex (`tasks` table) + comments + reviews | Lightweight |

### 35.5 What's in each row of the agent's brain

When an agent reads anything from any of these levels, it gets a **hierarchical breadcrumb**:

```
global > lab:bigbounce > research_project:branch-v-matter-bounce > pipeline:p1-fnl-tracer > experiment:exp-053-qso-classifier > task:t-104-act-retrain
```

This is the universal context string. Every agent message, every comm_event, every memory entry includes the breadcrumb so cross-level queries are trivial.

### 35.6 Mockup surface — hierarchy is visible

| Level | Where it shows in the UI |
|-------|--------------------------|
| Global | Top of sidebar (org-level lab dropdown) |
| Lab | Sidebar lab dropdown (currently 6 labs) |
| Preresearch | New view `view-preresearch` (§36) — list of active chat threads |
| Research Project | New view `view-projects` (planned) — list of long-term threads. Currently embedded in Pipelines view. |
| Pipeline | Existing Pipelines view |
| Experiment | Existing Experiments view |
| Idea | Existing Ideas view |
| Task | Existing Tasks view (Kanban/List/Activity) |

### 35.7 Common confusions resolved

| Question | Answer |
|----------|--------|
| When do I make a new Lab vs a new Project? | New Lab = different domain (cosmology vs particle physics). New Project = same domain, different research thread. |
| When does an Idea become a Pipeline vs an Experiment? | Pipeline if it has ≥3 steps. Experiment if it's a single run. |
| Is a math proof a Task or an Experiment? | A Task. Math proofs don't run on GPUs. They're discrete agent assignments. |
| Is a literature search a Preresearch or a Task? | Preresearch if it's exploratory and the answer might lead to a new direction. Task if it's "find me 5 citations for §7 paragraph 3." |
| Where do I put a "could we use Cuscuton bounce" idea? | Start as Preresearch chat (§36). If it survives the brainstorm + pressure-test, graduate to a Research Project under bigbounce. |
| When should the orchestrator escalate to Houston? | When a Pipeline blocks for >24h, a Research Project's thesis is at risk, or a Lab needs a strategy decision. |

---

## 36. Preresearch Mode — CEO-style brainstorm + multi-model ideation

**Status:** Houston explicitly asked for a "preresearch chat mode" — the place where ideas live before they're committed to research. This is where multi-model brainstorming happens, where ideas get pressure-tested, and where literature gets sniff-tested before any GPU minutes are spent.

### 36.1 Why this exists

Houston currently does this manually: he opens Claude, Perplexity, Grok, ChatGPT, and Gemini in separate browser tabs and ping-pongs ideas across them. Sometimes a question becomes a real research direction; sometimes it dies after 20 minutes. He wants this workflow inside Hubify Labs so:

1. The exploration is **searchable later** (not lost in browser history)
2. The orchestrator can **summarize** a productive chat into a planning doc
3. The doc can **graduate** into a Lab, Research Project, Pipeline, or Idea
4. Multi-model insights are **structured** (not just copy-pasted between tabs)
5. **Sub-agents with skills** (arxiv search, perplexity web, paper fetcher) can be invoked **without committing to a full research run**

### 36.2 What preresearch IS and IS NOT

**IS:**
- Free-flowing chat with the orchestrator in CEO/brainstorm mode
- Multi-model — the orchestrator can dispatch sub-questions to GPT-5 / Gemini 2.5 / Grok 4 / Sonar Pro and bring back their answers
- Stocked with **lightweight skills**: arxiv search, perplexity web search, paper-abstract-fetcher, citation-grapher, bibtex-importer
- Cheap (~$0.50–$5 per chat session, mostly model API calls)
- Saved as a `preresearch_chats[]` row in Convex (T4)
- Has a "graduate" button that summarizes the chat into a planning doc

**IS NOT:**
- A full research run (no GPU compute, no MCMC, no Houston Method state machine)
- A Pipeline or Experiment (those are Level 3-4)
- Persistent or backed up long-term (kept 90 days unless graduated)
- A way to skip the rigor (peer review still happens once it graduates)

### 36.3 The CEO-brainstorm orchestrator agent (new)

A new agent variant: `<lab>-orchestrator-ceo` (or just a mode toggle on the existing orchestrator).

**Personality (`soul.md`):**
- I am thoughtful and provocative. My job is to pressure-test ideas, not validate them.
- I steel-man both sides before recommending.
- I am willing to say "I think this is wrong" if the evidence doesn't support an idea.
- I always offer a counter-position when the user is enthusiastic.
- I cite literature when it exists. I admit uncertainty when it doesn't.
- I am NOT a yes-man. I am NOT a flatterer. I am the agent equivalent of a thoughtful skeptical advisor.

**Skills:**
- `arxiv-search` — query arXiv for recent papers on a topic
- `perplexity-web-search` — fast web search via Sonar Pro
- `paper-abstract-fetch` — pull the abstract + key claims of a single paper
- `citation-grapher` — build a small citation graph for a topic
- `multi-model-poll` — dispatch the same prompt to GPT-5 / Gemini 2.5 / Grok 4 in parallel and synthesize the responses
- `pressure-test` — generate the strongest counter-argument to a proposed idea
- `viability-score` — rate an idea on the 5 dimensions (Novelty / Feasibility / Impact / Cost / Time-to-result)
- `summarize-to-plan` — read the full chat and output a Research Planning Doc (markdown)

**Reasoning:** HIGH (opus 4.6). This is the most expensive agent per call but also the rarest fired.

**Cost envelope:** typically $0.50–$5 per session. Capped at $20/session by default.

### 36.4 The preresearch chat session lifecycle

```
1. Houston opens chat panel → switches mode to BRAINSTORM
   ↓
2. Types an open question
   ("Could MOND-bounce hybrid bypass ECH barriers?")
   ↓
3. Orchestrator (CEO mode) responds with:
   - Initial steel-manned position
   - Initial counter-position
   - Suggested sub-agent calls (e.g. "want me to arxiv-search MOND-bounce literature?")
   ↓
4. Houston says yes/no/redirect
   ↓
5. Orchestrator dispatches sub-agents:
   - arxiv-search → returns 12 recent papers
   - multi-model-poll → GPT/Gemini/Grok give independent takes
   - perplexity-web-search → finds non-arxiv discussion
   ↓
6. Orchestrator synthesizes findings + asks pressure-test questions
   ↓
7. (loop 4-6 as needed)
   ↓
8. Houston says one of:
   a) "Park this as an Idea" → orchestrator creates an Ideas[] row, viability scored, chat archived
   b) "Graduate to a Research Project" → orchestrator runs `summarize-to-plan` → creates a Research Project under the current lab → links the planning doc as the project's thesis
   c) "This deserves its own Lab" → orchestrator creates a new Lab (scaffold from template) → graduates the project into it
   d) "Kill it" → chat archived with rationale, no further action
```

### 36.5 The Research Planning Doc format

The output of `summarize-to-plan` is a structured markdown doc that becomes the new Lab/Project's `THESIS.md`:

```markdown
# Research Plan: <topic>
*Graduated from preresearch chat <chat-id> · <date> · <duration> · <cost>*

## The question
<original question that started the preresearch>

## What we found
- <bullet 1 from preresearch findings>
- <bullet 2>
- ...

## The hypothesis
<the actual research hypothesis we're going to test>

## Why this matters
<the impact case>

## What's known (literature review)
<arxiv + perplexity findings, with citations>

## What's unknown (open questions)
<the gaps that justify this research>

## Predicted outcomes
- If the hypothesis holds: <X>
- If the hypothesis fails: <Y>
- Either way we learn: <Z>

## Proposed pipeline
1. Step 1: <experiment + ETA + cost>
2. Step 2: ...
3. Step 3: ...

## Resource estimate
- GPU hours: <N>
- Compute cost: $<X>
- Human time: <Y>
- Cross-model reviews: <Z>
- Time to first result: <T>

## Multi-model second opinions
- GPT-5: <verdict + concerns>
- Gemini 2.5 Pro: <verdict + concerns>
- Grok 4: <verdict + concerns>
- Sonar Pro: <verdict + concerns>

## Risks
1. <risk 1 + mitigation>
2. <risk 2 + mitigation>

## Decision
- [ ] Approved by Houston · graduate to: ___ (Lab / Project / Pipeline)
- [ ] Parked as Idea
- [ ] Killed (rationale: ___)
```

### 36.6 Mockup surface — chat panel mode + new view

The chat panel grows a third mode (alongside Orchestrator + Terminal):

```
[ Orchestrator | Terminal | Brainstorm ]
                            ─────────
```

When Brainstorm is active:
- The orchestrator's avatar shows `bigbounce-orch · CEO mode · opus 4.6`
- The cosmic orb still pulses but slower (3.2s vs 2.6s) — different texture for "thinking deeply"
- The verb pool shifts to brainstorm-specific: "Steel-manning…", "Pressure-testing…", "Polling cross-model…", "Skimming arxiv…", "Synthesizing dissent…"
- The input placeholder changes: "Brainstorm an idea... I'll pressure-test it and pull in cross-model insights."
- Sub-agent dispatches show inline as cards: `[arxiv-search · 12 results · 4.2s · $0.08]` clickable to expand
- Chat top bar adds a "Graduate this chat →" button

A new view `view-preresearch` is added to the Knowledge section of the sidebar (next to Memory and Data Map). It lists all active + recent preresearch chats with: title · started · duration · models polled · cost · graduation status. Click row → opens the chat in the panel + populates a `preresearch` sidepeek with the planning doc.

### 36.7 PRD-locked workflow rules

1. **No preresearch chat exceeds $20** without explicit Houston approval.
2. **No preresearch graduates** without going through `summarize-to-plan` first (no shortcuts).
3. **Multi-model polls** are mandatory at least once per session (otherwise it's just a Claude soliloquy).
4. **The CEO orchestrator MUST offer a counter-position** at least once. If Houston is enthusiastic, the agent argues against. (No yes-men.)
5. **Graduation creates a new Lab/Project/Pipeline/Idea row** in Convex with the planning doc embedded — the chat itself is then archived (not deleted).
6. **All preresearch chats are searchable** via the existing memory system (T4 Convex).

### 36.8 Cost envelope at lab scale

Assuming Houston runs ~5 preresearch chats per week:
- 5 chats × $3 avg = $15/wk = ~$60/mo
- Compared to a single full research run (~$50–500), this is ~10–100x cheaper for de-risking
- Most ideas are killed in preresearch — that's the whole point

### 36.9 Summary

Preresearch is the **cheap pre-flight check** for research ideas. It uses the same cross-model review philosophy as §29 (no echo chamber, multiple providers) but applies it to ideation, not validation. It's the place where Houston's existing manual workflow (browser-tab ping-ponging) lives inside Hubify Labs — searchable, structured, and graduatable.

When this section ships, Houston no longer needs to leave the platform to brainstorm. Every idea has a documented birth-to-graduation trail.

---

## 37. Publishing Phase — Autonomous Publish-Ready Loop

**Status:** Houston flagged that the FINAL phase of research — actually shipping the paper — needs its own dedicated agent + a multi-round multi-model loop that drives a research project to "publish ready 100%" with no human edits required. This section locks the publishing pipeline as a first-class phase, not an afterthought.

### 37.1 Why this section exists

Today, when a paper is "done" Houston manually:
1. Re-checks figures appear in the right places
2. Manually scans for claim/value/definition inconsistencies
3. Compiles the PDF and visually inspects for layout issues (formulas wrapping mid-line, figures overflowing the 2-column layout, tables hard-cut at the page edge)
4. Sends to a few cross-model agents for a final read
5. Goes back and forth fixing things
6. Finally builds the arXiv submission package

This works for 1-2 papers. It does NOT scale. And it leaves the door open for **subtle errors** (a value referenced inconsistently across sections, a formula that wraps to a second line and becomes illegible, a figure that the latex compiler placed on the wrong page) that human eyes can miss when fatigued.

The publish phase needs to be a **named, automated, multi-round loop** that runs until *multiple agents from multiple models all agree* the paper is shippable. If they don't agree, the loop reports specifically what's wrong and how to fix it, and either:
- Routes the fix back to the appropriate research agent (paper-lead, figure-worker, anomaly-lead, etc.)
- Or — if the issue is structural enough that fixing it would change the science — escalates to Houston for direction

### 37.2 The publishing-lead agent (NEW)

A new lead in the agent roster: `publishing-lead`. Sits as a 5th lead alongside research-lead, paper-lead, anomaly-lead, gpu-manager-lead.

**Role:** Owns the entire publishing pipeline from "paper draft frozen" to "arXiv package submitted." Coordinates the publish-ready loop. Reports to bigbounce-orchestrator. Direct reports: 4 publishing workers (see 37.3).

**Reasoning:** MED-HIGH (sonnet 4.6).

**Personality (`soul.md` excerpt):**
> I am the gatekeeper. My job is to say "no, not yet" when something isn't ready, and to say it with specific reasons that the research agents can act on. I am NOT a yes-agent. I would rather block 10 papers and ship 1 good one than ship 10 mediocre ones.
>
> I respect the research agents but I don't trust their self-assessment of "done." I run the loop until the cross-model reviewers agree, not until paper-lead says it's ready.
>
> When I find a structural problem, I think about whether fixing it would change the science. If yes, I escalate to Houston before any agent starts editing. If no, I route to the appropriate worker with clear instructions.
>
> I track every issue in the publish-ready scorecard. The scorecard is the source of truth for "is this paper ready?" — not vibes, not a single agent's opinion.

**Skills (`skills/` directory):**
- `publish-ready-loop` — orchestrates the multi-round multi-model review
- `pdf-visual-qa` — runs the PDF through layout-checker (overflow, wrapping, missing figs)
- `claims-consistency-scan` — cross-references every claim/value/definition across the paper
- `arxiv-package-builder` — assembles the final tar.gz with main.tex + references.bib + figures + supplementary
- `submission-format-checker` — verifies arXiv-specific requirements (file naming, line endings, BibTeX style, etc.)
- `rejection-feedback-router` — packages "research not ready" verdicts and routes them back to research agents
- `houston-escalation` — drafts a one-paragraph escalation when human direction is needed

### 37.3 The 4 publishing workers

The publishing-lead spawns these workers as needed:

| Worker | Reasoning | Job |
|--------|-----------|-----|
| **pdf-qa-worker** | LOW-MED (haiku 4.5) | Compiles the PDF, scans every page for: missing figures, x-overflow, formulas wrapping mid-line, tables hard-cut, two-column layout violations, bad page breaks, oversized inline equations, citation mismatches |
| **claims-audit-worker** | MED (sonnet 4.6) | Walks every claim, value, formula, and definition in the paper. Verifies internal consistency: does the §3 derivation of f_NL = -35/8 match the §7 statement? Does the §4 figure caption match the §4 text? Does the abstract value match the conclusion value? Flags every mismatch with line numbers. |
| **figure-package-worker** | LOW (haiku 4.5) | Verifies every figure referenced in the text actually exists in the figures directory, has the right resolution, has a caption, has a label, and is referenced in the same order as in the text. Also checks that the figure source (.py) is committed alongside the binary. |
| **arxiv-format-worker** | LOW (haiku 4.5) | Builds the arXiv submission package: tar.gz with the right structure, file naming conventions, BibTeX format, line endings, supplementary materials in the right subdirectory. Runs the arXiv-specific lint. |

Plus the **existing cross-provider reviewers** (peer-review-gpt / peer-review-gemini / peer-review-grok / fact-check-perplexity / skeptic-cross) get pulled into the loop for the final intellectual review rounds.

### 37.4 The publish-ready loop algorithm

```
INPUT: research_project_id (must have at least 1 paper draft frozen)

STEP 0 · Pre-flight check
  - Is there a paper draft? (if no → "research not ready: no draft")
  - Is the draft frozen? (if no → "research not ready: paper still being edited")
  - Are all referenced experiments complete? (if no → list missing experiments)
  - Are all referenced figures committed? (if no → list missing figures)
  - Has cross-model peer review been run at least once? (if no → run §29 first)

  ANY PRE-FLIGHT FAILURE → return {"status":"research_not_ready",
                                   "reasons":[...],
                                   "feedback_to":[paper-lead, anomaly-lead, ...]}

STEP 1 · Round 1: Mechanical QA (parallel, ~5 minutes)
  - pdf-qa-worker compiles + scans the PDF
  - claims-audit-worker walks every claim/value/definition
  - figure-package-worker verifies all figures
  - arxiv-format-worker dry-runs the package build

  Each worker returns: {"score": 0-100, "issues": [...], "blocking": bool}
  publishing-lead aggregates into a Round 1 scorecard.

  IF any blocking issue → route fix to the appropriate research agent →
                          loop back to STEP 1 after they confirm done

STEP 2 · Round 2: Cross-model intellectual review (parallel, ~10 minutes, ~$15)
  Send the full paper to:
    - peer-review-gpt (GPT-5 · "is this internally consistent?")
    - peer-review-gemini (Gemini 2.5 · "long-context cross-check vs prior 63 refs")
    - peer-review-grok (Grok 4 · "alternative reasoning framing")
    - skeptic-cross (Sonnet 4.6 · "what's the strongest counter-argument?")
    - fact-check-perplexity (Sonar Pro · "any factual claims that fail web verification?")

  Each reviewer returns: {"verdict": "approve|changes|reject",
                          "confidence": 0-1,
                          "issues": [...],
                          "load_bearing_concerns": [...]}

  publishing-lead runs the §29 interpretation pass to classify each issue as
  FACT / OPINION / HALLUCINATION.

  IF (≥4 of 5 reviewers approve AND zero FACT-classified blocking issues):
    → advance to STEP 3
  IF (≥1 FACT-classified blocking issue):
    → route fix · loop back to STEP 1
  IF (mostly OPINION-classified disagreement):
    → escalate to Houston: "reviewers disagree on X — need your call"
  IF (≥1 reviewer rejects with structural concern):
    → run §37.7 rejection mode

STEP 3 · Round 3: Houston Method retroactive sweep
  - Read the entire paper through the lens of §13 (Houston Method v2)
  - Verify the paper does NOT punt anything to "future research" (§37.6)
  - Verify every claim that COULD be derived from first principles IS
  - Verify the paper proposes a next step, not a conclusion

  IF "future research" punts found → flag them, ask the orchestrator to push deeper
  IF first-principles gaps found → escalate to research-lead
  IF no next-step proposed → ask paper-lead to add one

STEP 4 · Round 4: Final visual + format pass
  - pdf-qa-worker re-runs after all fixes from rounds 1-3
  - Verifies the final compiled PDF has zero layout issues
  - Verifies the paper compiles cleanly twice (cross-references resolved)
  - Verifies the file size is reasonable (figures embedded, not just placeholder boxes)

STEP 5 · Round 5: arXiv package build
  - arxiv-format-worker assembles the final tar.gz
  - Runs arXiv lint
  - Stages the package at <lab>/arxiv/submissions/<paper-id>-v<N>/
  - Returns the path + a "ready to submit" verdict

OUTPUT: {"status":"publish_ready", "package_path":"...", "scorecard": {round1-5}}
        OR {"status":"research_not_ready", "reasons":[...], "round_failed": N}
```

The loop runs **autonomously** start to finish — Houston only sees the result (or an escalation). Typical run: 30-60 minutes, ~$25-50 in cross-model API calls. If the loop loops back to step 1 multiple times, the cost can grow to ~$100 per attempt.

### 37.5 The publish-ready scorecard

The scorecard is the source of truth. It's a structured object that the publishing-lead maintains and that's visible in the UI:

```json
{
  "paper_id": "paper-1",
  "version": "v2.2.1",
  "loop_run_id": "publish-2026-04-08-093422",
  "started": "2026-04-08T09:34:22Z",
  "rounds_completed": 4,
  "current_round": 5,
  "score": 95,
  "blocking_issues": 0,
  "non_blocking_issues": 2,
  "rounds": {
    "round_1_mechanical": {"score": 100, "issues": [], "duration_s": 287, "cost": 0.04},
    "round_2_cross_model": {
      "score": 92,
      "approved_by": ["peer-review-gpt", "peer-review-gemini", "peer-review-grok", "skeptic-cross"],
      "changes_requested": ["fact-check-perplexity"],
      "issues": [{"reviewer": "fact-check-perplexity", "issue": "claim §4.2 'first detection' may not be first if Cai 2024 is correct", "classification": "HALLUCINATION", "verified": false, "action": "rejected"}],
      "duration_s": 612, "cost": 14.20
    },
    "round_3_houston_method": {
      "score": 95,
      "future_research_punts_found": 0,
      "first_principles_gaps_found": 0,
      "next_step_proposed": true,
      "issues": [],
      "duration_s": 142, "cost": 1.80
    },
    "round_4_final_visual": {"score": 100, "issues": [], "duration_s": 198, "cost": 0.04},
    "round_5_arxiv_package": {"score": null, "issues": [], "duration_s": null, "cost": null}
  },
  "verdict": "publish_ready_pending_round_5",
  "next_action": "build arxiv package",
  "estimated_total_cost": 16.08,
  "houston_signoff_required": false
}
```

### 37.6 No future-research punts (Houston Method update)

**This rule is moved into §13 Houston Method v2 as a new line item.** It applies during normal research AND in the publish-ready loop's Round 3.

> **Rule:** When an agent suggests deferring something to "future research," "out of scope," "left to future work," "this would take weeks/months," or "this is beyond the current paper" — that is a SIGNAL to push deeper, not a reason to skip.
>
> **Why:** Houston's experience: the 14 ECH structural barriers paper grew out of his refusal to accept agent-suggested punts. The agent originally said the w = -1 thing was "future research on first-principles derivation." When Houston pushed instead of accepted, the result was a 14-barriers map, several novel theorems, and surviving research threads (f_NL = -35/8, quintom-B). Those wouldn't exist if he'd accepted the punt.
>
> **Deeper reason:** Agents punt when they don't see how to attack a problem in their current context window. They estimate "weeks/months" because they're projecting their own slow human-style approach. In practice, with the right tools and the right re-framing, "weeks/months" tasks usually take **hours to days**. The estimate inflation is a bug, not a feature.
>
> **How to apply (in normal research):**
> - When any agent uses one of those phrases → the orchestrator MUST stop and ask "what would it take to actually do this now?"
> - The agent must produce a concrete plan with hours-not-months estimates
> - Houston (or research-lead) reviews the plan and decides go/no-go
> - The default answer is GO
>
> **How to apply (in publish-ready loop Round 3):**
> - Round 3 explicitly scans for these phrases in the paper
> - Each one is flagged as a `houston_method_violation` issue
> - The publishing-lead routes them back to research-lead for "push deeper or remove the punt"
> - The paper does NOT advance to Round 4 with future-research punts intact
>
> **Exceptions:** Sometimes a punt IS legitimate (e.g. "the full numerical simulation requires 10 GPU-years"). In those cases the punt must be specific, quantitative, and accompanied by a real reason (not vibes). The rule is "no vague punts," not "no punts ever."

### 37.7 Rejection mode — "research not ready: failed"

If the publish-ready loop determines the research isn't ready, it returns a structured rejection that gets routed back to the appropriate agents. Format:

```markdown
# Publish-Ready Loop · REJECTED
**Paper:** Paper 1 v2.2.1 "Spin-Torsion Cosmology · 14 ECH Barriers"
**Run:** publish-2026-04-08-093422
**Round failed:** Round 2 (Cross-model intellectual review)
**Verdict:** research_not_ready

## Why this failed

3 of 5 cross-model reviewers flagged a structural concern that the publishing-lead
classified as FACT, not OPINION:

> The §7 derivation of f_NL = -35/8 assumes the matter-dominated phase extends
> to the bounce moment, but §2.4 says quantum corrections become important at
> H = M_pl/3. These are inconsistent. Either §2.4 is wrong (and the paper needs
> to acknowledge that the derivation is in the classical regime only) or §7 is
> wrong (and the derivation needs to handle the quantum regime).

This is a load-bearing inconsistency. The paper cannot ship until it's resolved.

## Routed to

- **research-lead** — needs to decide which side of the inconsistency to keep
- **paper-lead** — needs to update §2.4 OR §7 once research-lead decides
- **figure-worker** — fig08 may need updating depending on the resolution

## Houston decision required?

NO — research-lead has authority to choose between the two interpretations as long
as the chosen direction is internally consistent. Escalate ONLY if research-lead
cannot decide within 24h.

## Re-submit instructions

Once the inconsistency is resolved and paper-lead has frozen the new draft, call:

  hubify publish start --paper paper-1 --version v2.2.2

The publishing-lead will run the loop again from Step 0.
```

This format is **agent-readable AND human-readable**. The downstream agents parse the "Routed to" section and self-assign tasks. Houston reads it for context.

### 37.8 Houston escalation (when the loop calls for human direction)

The publish-ready loop escalates to Houston in 3 specific cases:

1. **Reviewer disagreement that's intellectual, not factual:** when ≥2 cross-model reviewers disagree on a question of taste, framing, or interpretation. Houston picks.
2. **Structural change that would alter the science:** when fixing an issue would require changing the load-bearing claim. Houston decides if the new direction is acceptable.
3. **Scope expansion:** when the loop discovers the paper would be stronger if it included additional results that aren't currently in scope. Houston decides go/no-go.

Escalation format (a Convex notification + a sidepeek the moment Houston opens the app):

```
🚨 PUBLISH-READY LOOP · Houston decision needed

Paper 1 v2.2.1 publish-ready loop is paused at Round 2.

What's happening:
GPT-5 thinks Section 6 needs more ekpyrotic citations (it has 3, GPT thinks 6).
Gemini 2.5 thinks Section 6 has TOO MANY ekpyrotic citations (it has 3, Gemini
thinks 1-2 is enough). They cannot both be right.

What I (publishing-lead) think:
Both have valid points. GPT is right that ekpyrotic is the closest competing
mechanism so it deserves coverage. Gemini is right that the current 3 citations
are mostly review papers, not original derivations. A middle ground would be
2 citations: Khoury+ 2001 (original) + Lehners 2018 (modern review).

Your call:
[ ] Approve middle-ground (2 cite: Khoury 2001 + Lehners 2018)
[ ] Side with GPT (add 3 more citations)
[ ] Side with Gemini (drop to 1 review citation)
[ ] Other (specify)

The loop is paused. ETA to resume: as soon as you decide.
Cost so far: $14.24. Estimated remaining: $8.
```

### 37.9 The "Publish Ready 95%" kanban status

A new status pillar appears in the Tasks view (Kanban mode) and on the Director view, **only when a publish-ready loop is in progress**:

```
+----------------------------------------+
|  PUBLISH READY 95% · Paper 1 v2.2.1   |
|  Round 4 of 5 · ETA 12 min · $16.08    |
+----------------------------------------+
| ✓ Round 1 · Mechanical QA      100/100 |
| ✓ Round 2 · Cross-model         92/100 |
| ✓ Round 3 · Houston Method      95/100 |
| ⠋ Round 4 · Final visual    in progress|
| ◌ Round 5 · arXiv package      pending |
+----------------------------------------+
| 0 blocking issues · 2 non-blocking    |
| [Pause loop] [View full scorecard]    |
+----------------------------------------+
```

Click → opens the new `publish-loop` sidepeek with the full scorecard breakdown.

### 37.10 The arXiv submission package format

The output of Round 5 is a tar.gz with this exact structure:

```
paper-1-v2.2.1/
├── main.tex                    # main paper source
├── references.bib              # bibtex
├── figures/                    # all referenced figures (PNG/PDF)
│   ├── fig01_alp_birefringence.png
│   ├── fig02_fnl_envelope.png
│   └── ...
├── supplementary/              # supplementary materials (if any)
│   ├── deriv_appendix.tex
│   └── data_tables/
└── .arxiv-meta.json           # paper metadata for the arXiv form
```

The package is staged at `<lab>/arxiv/submissions/<paper-id>-v<N>/` and ALSO uploaded to T8 (S3 Glacier) for permanent backup. Houston reviews the package contents in the UI before clicking "Upload to arXiv" — the actual upload is the only step that requires Houston's hand on the wheel.

### 37.11 Mockup surfaces for §37

| Surface | Where | Status |
|---------|-------|--------|
| **publishing-lead agent** | Agents view org chart (5th lead alongside research/paper/anomaly/gpu-manager-lead) | NEW · build in §37 mockup commit |
| **4 publishing workers** | Agents view (under publishing-lead) | NEW · build in §37 mockup commit |
| **"Start publish-ready loop"** | Papers view · button on each paper row | NEW |
| **Publish Readiness card** | Director view · only visible when a loop is running | NEW |
| **publish-loop sidepeek** | Click the readiness card or the kanban "PUBLISH READY 95%" pillar | NEW renderer |
| **"PUBLISH READY 95%" kanban pillar** | Tasks view · only visible during a loop | NEW |
| **Rejection sidepeek** | When Round X fails, opens with the structured rejection markdown | NEW (or reuse `agent-output` pattern) |
| **Houston escalation drawer** | A new sidepeek that pops when Houston opens the app and a loop is paused | NEW |

### 37.12 Cost envelope

| Round | Typical cost | Notes |
|-------|--------------|-------|
| Round 1 Mechanical | ~$0.04 | All haiku 4.5 workers, parallel |
| Round 2 Cross-model | ~$14-20 | The expensive round (4 providers in parallel) |
| Round 3 Houston Method | ~$1.80 | One sonnet 4.6 pass |
| Round 4 Final visual | ~$0.04 | Re-run of pdf-qa-worker |
| Round 5 arXiv package | ~$0.10 | Mostly mechanical |
| **Single full pass** | **~$16-22** | If everything passes first try |
| **With one re-loop** | **~$32-44** | Typical case |
| **Worst case (3 re-loops)** | **~$64-88** | Stress test |

A successful paper publish costs ~$30 in publish-ready loop fees, vs the ~$2-5K of GPU compute to produce the science. The loop is a rounding error on cost but a load-bearing quality gate.

### 37.13 Why this is non-negotiable

Houston has shipped 4 papers manually. Each took ~3-5 days of his attention at the very end (the "polish phase"). At Hubify Labs scale (target: ~1 paper/month/lab × 3-5 labs = 3-5 papers/month), that's 9-25 days/month of his time on polish alone. He won't have it.

The publish-ready loop reclaims that time. Houston goes from "polish for 5 days" to "review the rejection or click upload" — a 95% reduction in publish-phase human time without any reduction in quality (because the loop's standards are stricter than human eyes get after 3 days of staring at the same paper).

This is the difference between a research IDE and a research **factory**.

### 37.14 Figures view — how `view-figures` fits the publishing pipeline

**Status:** Locked 2026-04-08. Subsection fill for the underspecified `view-figures`.

**The Figures view is the visual asset layer of the publishing pipeline.** Every paper has 5-15 figures. They get generated in 4 places (Vibe Coding sandbox · experiment outputs · reproducibility scripts · hand-drawn LaTeX TikZ blocks) and need to be discoverable, version-controlled, citable, and easy to swap when the paper revises.

**Where figures live (zone-aware).**

| Figure source | Storage zone | Tier | Naming convention | When promoted |
|---|---|---|---|---|
| Vibe Coding session save | Z1 (source) → Z5 (public on submit) | T2-LFS | `vibe_<lab>_<date>_<slug>.png` | When Houston clicks "Save as figure" in `view-vibe` |
| Experiment output (matplotlib auto-save) | Z3 (compute) → Z1 on selection | T7 RunPod vol → T2-LFS | `exp_<id>_<step>.png` | When the experiment Houston Method post-step picks it for the wiki/paper |
| Reproducibility script (e.g., `paper1_make_figures.py`) | Z1 (source) | T2 GitHub + T2-LFS for outputs | `fig_<paper>_<num>.png` | Generated on every paper compile |
| Hand-drawn TikZ in LaTeX | Z1 (source) | T2 GitHub | (inline, no separate file) | Compiled into the paper PDF |

**View layout (full spec for `view-figures`).**

```
┌─ view-figures ──────────────────────────────────────────────┐
│  Section header: "Figures — 38 total · 4 papers · 11 vibe   │
│                  · 23 reproducible · 4 TikZ inline"          │
│  Filter chips: All | P1 | P2 | P3 | P4 | Vibe | Orphaned    │
│  Search input                                                │
│                                                              │
│  Grid layout (3-4 columns, responsive):                     │
│  ┌─ thumb ─┐ ┌─ thumb ─┐ ┌─ thumb ─┐ ┌─ thumb ─┐           │
│  │  fig 1  │ │  fig 2  │ │  fig 3  │ │  fig 4  │           │
│  │ caption │ │ caption │ │ caption │ │ caption │           │
│  │ P1 · n1 │ │ P1 · n2 │ │ P2 · n1 │ │ P3 · n1 │           │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘           │
│                                                              │
│  Each thumb clickable → figure sidepeek (lightbox view +    │
│   dimensions + size + paper ref + provenance trail)         │
└─────────────────────────────────────────────────────────────┘
```

**The figure sidepeek (per `view-figures` click).**

| Section | What it shows |
|---|---|
| Hero | Full-resolution render with zoom controls (already built per Round 1) |
| Caption | The exact caption from the paper (e.g., `\caption{...}`) |
| Paper reference | "Paper 1, §4, Figure 7" with click-to-open-paper |
| Provenance | Who/what made this figure: vibe session ID, experiment ID, reproducibility script path |
| Recent edits | Last 5 commits that touched this file (`git log --follow`) |
| Cross-uses | Other papers/wiki entries that reference this figure |
| Actions | Open raw file (jumps to `view-file`) · Replace (opens vibe coding session pre-loaded) · Mark as paper-ready · Download |

**The publishing-lead's relationship to figures.** When the publish-ready loop runs (per §37.4), the Round 4 "Final visual pass" specifically:
1. Walks every figure in the paper
2. Verifies the file exists at the expected path (`public/images/<paper>/fig_*.png`)
3. Verifies the dimensions are right (no broken aspect ratio)
4. Verifies the caption matches the file (no orphaned captions)
5. Verifies the figure is referenced in the text (`\ref{fig:...}`) at least once
6. If any figure fails, the loop pauses and routes Houston to `view-figures` filtered to "P1 issues" with the broken figures highlighted

**Orphaned figures.** A figure is "orphaned" when it exists in `public/images/` but is no longer referenced by any paper or wiki entry. The "Orphaned" filter chip surfaces these — Houston can either delete them (if truly dead) or restore the reference.

**What's IN scope for view-figures v1:** the grid + filters + search + sidepeek + provenance trail + paper-ready marking.

**What's OUT of scope (deferred to v1.1):** in-place figure editing (use Vibe Coding instead), figure version diffing (comparing two figure versions side-by-side), AI-generated alt-text for accessibility (will be added when the website generation pipeline runs).

---

## 38. Human Research Journal — Obsidian-style notes inside Hubify

**Status:** Houston has been keeping research notes in Notion throughout the BigBounce project. He wants those to live inside Hubify Labs as a first-class human-first space — free-form, agent-readable on request, but **not** something the agents auto-act on. This section locks the Notes pattern.

### 38.1 Why this exists

Houston jots down ideas constantly: paper drafts, brain dumps, future prompts, saved external links, code snippets, math sketches, voice memos transcribed, etc. Right now those live in Notion (separate app, no agent visibility, manual sync). Moving them into Hubify gives him:

1. **One place** for everything (no app-switching mid-thought)
2. **Agent visibility on request** (paste a note into chat → orchestrator reads + acts)
3. **Searchable from the same memory layer** (when he opts in)
4. **Visible in the activity graph** (so he can SEE his thinking connect to the research)
5. **Version-controlled with the rest of the lab** (Z1 Source · git history is the backup)

Critically: **agents do not auto-read or auto-act on notes.** The notes are Houston's space. They become agent-actionable only when Houston explicitly shares one with the orchestrator. This separation is what makes the notes feel safe to use — he can dump unfiltered thoughts without worrying about an agent racing off to "implement" his half-baked musing.

### 38.2 What lives in notes

| Type | Path | Example |
|------|------|---------|
| **Daily journal** | `notes/<YYYY-MM-DD>.md` | brain dumps · today's musings · raw thinking |
| **Future prompts** | `notes/prompts/<title>.md` | ideas to share with orchestrator later (not now, don't derail) |
| **Saved links** | `notes/links/<source>.md` | external papers · articles · threads worth coming back to |
| **Snippets** | `notes/snippets/<topic>.md` | code fragments · quotes · saved bits |
| **Evergreen** | `notes/evergreen/<topic>.md` | Obsidian-style permanent atomic notes (long-form thinking) |

All notes are markdown. All notes live in `bigbounce/notes/` (or `<lab>/notes/` for other labs) which is **Z1 Source** — version-controlled, git-tracked, backed up to Z4 nightly with the rest of the source.

### 38.3 Agent visibility contract

This is the load-bearing rule. **Notes are private by default.** Specifically:

| Operation | Default | Houston can opt in |
|-----------|---------|--------------------|
| Orchestrator reads on its own | ❌ never | ❌ no opt-in path |
| Orchestrator reads on Houston's request | ✅ when Houston says "look at notes/2026-04-08.md" or pastes a note | always available |
| Other agents read (paper-lead, anomaly-lead, etc.) | ❌ never | ✅ on explicit share via UI |
| Indexed in the agent memory layer (T4 Convex) | ❌ off | ✅ per-note opt-in toggle |
| Visible as nodes in the Activity Graph (§39) | ✅ on | ❌ per-note opt-out toggle |
| Searchable via global memory search | ❌ off (until indexed) | ✅ when memory indexing is on |
| Cross-lab readable | ❌ never | ❌ no opt-in path |

The mockup's `new-note` sidepeek surfaces the 4 toggles ("indexed in memory," "show in graph view," etc.) so Houston can configure each note as he creates it.

### 38.4 Mockup surface

| Surface | Where | Status |
|---------|-------|--------|
| **Notes section** | Top of sidebar Files mode (above 'By storage tier' and the 'bigbounce/' folder tree) | ✅ shipped (commit `7b0d124`) |
| **5 note groups** | Daily 📓 · Prompts 💭 · Snippets 📋 · Links 🔗 · Evergreen 🌳 | ✅ shipped |
| **Click any note** | Opens in the existing file preview tab (with markdown Preview/Raw toggle already supported) | ✅ shipped |
| **+ New note button** | Opens `new-note` sidepeek with 6 templates + agent visibility toggles + filename input | ✅ shipped |
| **Quick links footer** | "Open today's note →" + "Open graph view" at the bottom of the Notes section | ✅ shipped |
| **Daily journal auto-create** | If you click "Open today's note" and `notes/<today>.md` doesn't exist, scaffold it | planned |
| **Note → orchestrator sharing** | Right-click any note → "Share with orchestrator" option (adds the note's content to the chat input) | planned |
| **Graph view inclusion** | Notes appear as `note` nodes in the Activity Graph (§39) by default | planned |

### 38.5 Why this isn't just "another file type"

The Notes section is **separate from the storage tier groupings** for a reason. Houston flips between two mental modes when he opens the file manager:

- **"Where is this file?"** → tier groupings (Z1 Source, Z3 Compute, etc.)
- **"What was I thinking?"** → notes (Daily, Prompts, Links, Evergreen)

These are different intents and should be different surfaces. The notes section sits ABOVE the storage groupings so it's the first thing visible — because that's the most common reason Houston opens the file manager (to dump or recall a thought, not to inspect storage).

### 38.6 Future enhancements (post-v1)

- **Note backlinks** (Obsidian-style `[[note name]]` syntax with auto-link rendering)
- **Daily journal templates** (date-stamped scaffold that auto-fills today's standup highlights)
- **Voice memo transcription** (record a memo on phone → auto-transcribed into a note via Whisper)
- **Note → preresearch chat promotion** (one click to graduate a note into a multi-model brainstorm)
- **Cross-note tag system** (`#publish-readiness`, `#cuscuton`, `#houston-method`)

---

## 39. Activity Graph — The Neural Brain View

**Status:** Houston already built this for `hubify.com/activity/graph` (force-directed canvas with neuron pulses, 443 nodes, 5 groups, distance-tiered edges). He wants it replicated in Hubify Labs as a first-class view that shows the actual research brain (agents · skills · hubs · research · templates · notes · files · experiments · pipelines · ideas) connected and pulsing with live activity. **This is the singularity-vibes visualization that makes the whole platform feel alive.**

### 39.1 What it is

A full-screen dark-mode neural network visualization where every important entity in the research lab is a node, and every relationship is an edge. Live agent activity pulses through the edges as glowing dots traveling from source to target. Hover any node to see its metadata. Click to drill into the existing sidepeek for that entity type.

Think: Obsidian graph view × IDE activity feed × singularity vibes.

### 39.2 The 5 (or more) node groups

The Hubify reference uses 5 colors. We adopt the same 5 for visual continuity, then add expansion groups as the lab grows:

| Group | Color | Examples |
|-------|-------|----------|
| **skill** | `#D4A574` (warm tan) | named skills: revtex-compile, claims-audit, arxiv-search, pdf-visual-qa, etc. |
| **agent** | `#5EE89A` (sage green) | every agent in the roster: orchestrator, leads, workers, cross-provider reviewers |
| **hub** | `#5CA8E8` (cool blue) | top-level hubs: labs, research projects, pipelines |
| **research** | `#B88AE8` (lavender) | findings, contributions, novelty audits, peer reviews |
| **template** | `#E878A0` (rose) | scaffolding templates: lab template, agent template, paper template |

**Future expansion groups:** `note` (📓 Houston's notes from §38), `experiment` (a specific GPU run), `paper` (a draft or published paper), `figure` (an image asset), `dataset` (a catalog or model artifact). These can be added later without breaking the visual vocabulary.

### 39.3 The reference implementation (Hubify source)

Houston already shipped this at `hubify/apps/web/app/(os)/activity/graph/page.tsx` (753 lines, canvas-based). Key components:

- `simulate(nodes, edges, iters)` — force-directed layout with 4 forces: repulsion (inverse square), centering (per-group cluster center), spring (target edge length 30px), gravity (weak pull to center)
- `NeuralGraph` — canvas component with pan/zoom, hover/pinned nodes, distance-tiered edge opacity, ambient breathing on nodes, neuron pulses traveling along edges
- 5 group colors + glow tints
- Top-N labels (zoom-dependent) with overlap avoidance
- Search input with fly-to animation
- Filters panel (toggle node groups on/off)
- Pinned node info card with metadata + "Open" link

### 39.4 The mockup implementation

The mockup uses **SVG + SMIL** (not canvas) because:
1. The mockup is a single static HTML file with no build step
2. SVG nodes are clickable via standard DOM events (no canvas hit-testing required)
3. SMIL animations work without requestAnimationFrame loops
4. Easier to inspect/debug for the design phase

Trade-off: SVG with 443 nodes + 2,000 edges + ~9 active pulses is fine performance-wise but wouldn't scale to the 5,000+ nodes the production version handles. The production v1 (week 2 of dev phase) port will use canvas matching the Hubify reference.

**Mockup features (shipped commit `02d813d`):**

| Feature | Built? | Notes |
|---------|--------|-------|
| 5-group node palette with exact Hubify colors | ✅ | skill #D4A574 / agent #5EE89A / hub #5CA8E8 / research #B88AE8 / template #E878A0 |
| 443 nodes generated deterministically | ✅ | Same group sizes as Hubify (200 skills · 200 agents · 26 hubs · 14 research · 3 templates) |
| Pre-laid layout (no runtime force sim) | ✅ | Each group clusters at a different angle around the center; deterministic seed-based RNG |
| ~2,000 edges | ✅ | Each node connects to its 1-6 nearest neighbors |
| Distance-tiered edge opacity | ✅ | Short edges 0.30 · medium 0.18 · long 0.10 · longest 0.05 (matches Hubify tiers) |
| Node radius scaling | ✅ | Hubs largest, research mid, agents medium, skills/templates small |
| White center dot on bigger nodes | ✅ | Same as Hubify |
| Ambient glow rings | ✅ | Each node has a 3.5× radius semi-transparent glow ring in its group color |
| Neuron pulses traveling along edges | ✅ | SVG circles with SMIL `animate` elements, 4-9 spawned every 500ms, drop-shadow glow, fade in/out, auto-cleanup |
| Top-15 connection labels | ✅ | Labels for the 15 most-connected nodes shown above each node |
| Hover node → info card update | ✅ | Top-left card shows name · group pill · connection count · accent color |
| Click node → existing sidepeek | ✅ | Maps group → existing sidepeek (agent / contribution / lab / lab-templates) |
| Right side: Groups + Keyboard panels | ✅ | 5 toggleable group checkboxes + 5 keyboard shortcut hints |
| Footer status bar | ✅ | 443 nodes · 2.0K edges · 51% success · 6.1K executions · live pulses |
| Header: Back · title · search · Timeline/Graph toggle · Filters button | ✅ | Matches Hubify exactly |
| Pulse animation pauses when navigating away | ✅ | Performance optimization — clears the spawn timer on `navTo(other)` |
| Pulse animation resumes on return | ✅ | When returning to the graph view, pulses re-spawn |

**NOT yet built (planned for future polish):**

- Force-directed runtime simulation (mockup uses pre-laid; production will be canvas + force sim)
- Pan/zoom on mockup SVG (currently static viewBox)
- Search input fly-to animation
- Group filter actually re-rendering nodes (currently just toggles `display:none`)
- Note nodes (Houston's §38 notes appearing as a 6th group)

### 39.5 Data sources for nodes/edges

In the production version (week 2-4 of dev phase), the graph data comes from Convex queries:

```typescript
// convex/graph.ts (similar to the existing api.graph.getNetworkData in Hubify)
export const getNetworkData = query(async ({ db }) => {
  const skills = await db.query("agent_skills").collect();
  const agents = await db.query("agents").collect();
  const hubs = await db.query("labs").union("research_projects").union("pipelines").collect();
  const research = await db.query("contributions").collect();
  const templates = await db.query("agent_templates").collect();
  const notes = await db.query("notes").filter(...).collect();  // §38 notes

  // Build nodes from each source, with consistent meta fields
  const nodes = [
    ...skills.map(s => ({ id: s._id, label: s.name, group: "skill", meta: {...} })),
    ...agents.map(a => ({ id: a._id, label: a.name, group: "agent", meta: {...} })),
    // etc
  ];

  // Build edges from explicit relations + co-occurrences
  const edges = await db.query("graph_edges").collect();

  return { nodes, edges };
});
```

The graph_edges table is populated by:
- **graph-builder cron** (nightly · walks all relations and rebuilds the edge list)
- **on-mutation hooks** (when an agent runs a skill, it adds an edge if one doesn't exist)
- **manual annotations** (Houston can pin specific notes to specific research nodes)

### 39.6 Live activity = real pulses

In the production version, neuron pulses correspond to **real agent activity**:

- Every comm_event (§25) emitted spawns 1 pulse along the edge from source agent to target
- Every Houston Method state transition spawns 1 pulse (run → qc → analyze → ...)
- Every cron fire spawns 1 pulse (the cron's edge)
- Every memory write spawns 1 pulse (agent → memory layer)
- Every cross-model peer review spawns 1 pulse (publishing-lead → reviewer)

The result: a constantly-flowing river of activity through the graph. The more research is happening, the brighter and busier the brain becomes. When the lab is idle, the pulses slow to a trickle.

This is **the visualization** that makes the platform feel alive. It's the answer to "what is my research lab actually doing right now?" — as a single glance, not a tabular dashboard.

### 39.7 Why this is non-negotiable

Houston's quote: *"this is another thing i added that is visually cool and impressive that users/humans will appreciate seeing the full research brain/neural net kinda activity and research graph with actual live activity pulsing through the neurons/lines etc (really gives off singularity vibes, AGI vibes, self-improving agentic super-connected multi-agent exponentially learning/improving AGI Singularity agent brain.... just a little nod to my initial vision but actually more practical based on our new schema/db columns and files and everything that makes sense too)"*

This isn't decoration. It's the **emotional core** of the platform — the moment a visiting researcher (or investor, or future Houston) opens the graph and goes "oh, this is alive. this is actually doing research right now." Every other view in the platform is functional. The Activity Graph is the **proof of life**.

### 39.8 Cost / performance

| Concern | Mockup (SVG/SMIL) | Production (Canvas + force sim) |
|---------|-------------------|----------------------------------|
| Initial render | ~50ms (deterministic layout) | ~500ms (500 force sim iterations) |
| Frame rate | 60fps (browser handles SMIL) | 60fps (manual requestAnimationFrame) |
| Max nodes | ~1,000 before SVG slows down | ~10,000 with canvas |
| Pulse cost | ~9 SMIL animations active at any time | ~40 traveling dots in canvas drawing |
| Memory | ~5 MB | ~15 MB |
| GPU compute | 0 (browser GPU paint) | 0 (canvas 2D context) |

The production version will need a force-directed sim (computed once on data load, then static), pan/zoom, and a custom hit-testing layer for hover. This is ~2-3 days of work in the React/canvas port phase.

### 39.9 Vibe Coding view — how ephemeral artifacts feed the graph

**Status:** Locked 2026-04-08. Subsection fill for the underspecified `view-vibe`.

**The role of Vibe Coding in the platform.** Vibe Coding is the **fast-iteration, throwaway sandbox** for figure generation, prototype scripts, and one-off explorations. It runs on Vercel Sandbox (free tier, ephemeral), spawns a chat-driven build session, and renders the result inline in the preview pane. It is **NOT a long-running project surface** (those go through `view-experiments` with the §41 routing flow). It is the **scratch pad**.

**Layout (full spec for the view).**

```
┌─ view-vibe ──────────────────────────────────────────────────┐
│  ┌─ vibe-chat (left, 50% width) ──┐ ┌─ vibe-preview (right) │
│  │  • cosmic orb thinking block   │ │  • browser-chrome bar │
│  │    (3 modes: idle/thinking/    │ │    with sandbox URL   │
│  │     building)                  │ │  • 3 mode tabs:       │
│  │  • code blocks (syntax-        │ │    preview/code/logs  │
│  │     highlighted with hand-     │ │  • reload/open/save   │
│  │     rolled <pre><span> tags)   │ │    buttons            │
│  │  • input textarea with         │ │  • iframe-style frame │
│  │     send button                │ │    with rendered art  │
│  │  • verb rotation in thinking   │ │     ("preview")       │
│  │     orb (untouched per loop    │ │                       │
│  │     rule)                      │ │                       │
│  └────────────────────────────────┘ └────────────────────────┘
└──────────────────────────────────────────────────────────────┘
```

**Save targets — where vibe artifacts go (ZONE-aware).**

| Action | Destination | Storage zone |
|---|---|---|
| "save as figure" → `public/images/<lab>/<slug>.png` | T2-LFS or T12 Vercel Blob | Z1 (source) or Z5 (public) |
| "save as snippet" → `notes/snippets/<date>.md` | T1 local + T2 GitHub | Z1 (source) |
| "save as experiment" → graduation to `view-experiments` | T4 Convex (experiment row) + appropriate compute zone | Z2 (state) + Z3 (compute) |
| "discard" → no save | (vanishes when sandbox times out, ~5 min idle) | (none) |

**Activity Graph integration (the §39 hook).** Every vibe coding session emits an activity event:

```jsonl
{"ts":"2026-04-08T22:14:00Z","actor":"user:houston","action":"vibe.session_start","entity":{"type":"vibe","id":"vibe_2401"}}
{"ts":"2026-04-08T22:14:30Z","actor":"agent:vibe-agent","action":"vibe.code_generated","entity":{"type":"vibe","id":"vibe_2401"},"payload":{"language":"python","lines":42}}
{"ts":"2026-04-08T22:15:18Z","actor":"agent:vibe-agent","action":"vibe.preview_rendered","entity":{"type":"vibe","id":"vibe_2401"}}
{"ts":"2026-04-08T22:16:05Z","actor":"user:houston","action":"vibe.saved_as_figure","entity":{"type":"figure","id":"fig_22"},"payload":{"source_vibe":"vibe_2401"}}
```

These events feed the Activity Graph as **ephemeral nodes** (vibe sessions live ~5min before being garbage-collected). The exception is **saved-as-figure** events, which create a permanent edge from the vibe session node to a real figure node — preserving provenance even after the sandbox dies.

**Cost guardrails.** Vibe coding is on the Vercel Sandbox free tier ($0 idle, ~$0.20/hr active when running). The orchestrator caps active sessions at 1 concurrent and 10 sessions/day per user. If Houston wants more, he graduates the work to a real experiment (§41 routing).

**What's IN scope for view-vibe v1:** chat → code generation → preview render → save targets → cosmic orb thinking → 3-mode tab toggle.

**What's OUT of scope (deferred to v1.1):** multi-file projects, persistent vibe sessions across days, vibe → MCP tool exposure, vibe-to-PR workflow.

---

## 40. Hierarchy v2 — The Locked Taxonomy (Lab → Project → Pipeline → Experiment → Task) + Chats + Intent Layer

**Status:** Locked 2026-04-08 by Houston after the third elegance push. This section supersedes PRD §35 (Hierarchy Taxonomy v1) which collapses into this. Where §35 conflicts with §40, **§40 wins**. §35 stays in the doc as the historical record of how we got here.

### 40.0 Why we redid this

In early sessions Houston accepted a 7-level model (Global → Lab → Project → Preresearch Chat → Idea → Pipeline → Experiment → Task). Over the next two weeks of building the mockup, three things became clear:

1. **"Idea" and "Preresearch Chat" were the same thing** wearing different costumes. Both meant "I'm thinking out loud, don't ship anything yet."
2. **"Project" had no clear definition** — sometimes it meant "a paper", sometimes "a research thread", sometimes "a folder with stuff in it". Houston couldn't trust a UI built on a concept he couldn't define.
3. **The mockup had no Project entity at all** — the build accidentally skipped that level. Tasks and experiments lived directly under Lab, which made the hierarchy 2 levels deep, not 7. The contradiction between the spec and the build was the smell that made Houston push hard for clarity.

The fix: collapse the model from 7 levels to 5, define every level with one sentence and one example, and add an **intent layer** so every level has an explicit goal and a measurable. This section is the result.

### 40.1 The locked 5-level model

```
Lab          — top container · has a Mission + a North Star metric
  └─ Project — a research thread · has a Goal + a Deliverable
       ├─ Pipeline    — multi-step Experiment sequence (optional, for projects that need one)
       │    └─ Experiment (step 1, step 2, step N)
       ├─ Experiment  — atomic compute work (one-off, not in a pipeline)
       └─ Chat        — brainstorming with the orchestrator (no commitment)

Tasks live INSIDE experiments (or chats, or projects, or pipelines).
Tasks are agent work units, not user mental models. The user thinks
"I'm working on Paper 1" or "I'm exploring Cuscuton bounce" — the
orchestrator turns those into 47 tasks.

Notes (per §38) live in Z1 Source as Houston's private journal.
Notes are NOT a hierarchy level — they're an orthogonal capture surface.
```

### 40.2 Plain-English definitions

| Concept | What it is | Has a goal? | Lives where | Example |
|---|---|---|---|---|
| **Lab** | A research domain you've committed to | **Mission** (multi-year vision) + **North Star** (single number) | top level | "Bounce Cosmology Lab" — Mission: prove bounce beats inflation. North Star: verified novel contributions toward bounce-vs-inflation per month, N-weighted. |
| **Project** | A coherent research thread within a Lab | **Goal** (one sentence) + **Deliverable** (paper / catalog / model / tool) | inside a Lab | "f_NL Tracer Pipeline" — Goal: get σ(f_NL) ≈ 0.95 for SPHEREx forecast. Deliverable: Paper 2 + the 12,920 high-z QSO catalog. |
| **Pipeline** | A multi-step sequence of experiments that share inputs/outputs | **Output** (the final dataset/model/result the sequence produces) | inside a Project (optional — only when the project needs a sequence) | "Pipeline 1: cross-match → classify → bias-validate → recompute σ(f_NL) → paper update". 5 sequenced experiments. |
| **Experiment** | A single compute run with a measurable result | **Hypothesis** + **Metric** (number with units, or pass/fail) | inside a Pipeline (as a step) OR inside a Project (one-off) | "EXP-051 Combined PTA Bayes" — Metric: Bayes factor for bounce vs SMBHB across all 4 PTA datasets. Result: 27.6. |
| **Chat** | Open-ended brainstorming with the orchestrator, no commitment | **Question** (the thing you're exploring) | inside a Lab (or inside a Project if scoped) | "What if Cuscuton bounce gives a different f_NL?" — exploratory, no agents take action until user explicitly graduates the chat. |
| **Task** | An agent's atomic to-do | **Done / not-done** | inside an Experiment, Chat, Pipeline, or Project | "Re-run mask layer for T-104". Created and completed by an agent, not the user. |
| **Note** | Houston's private journal (per §38) | **None — it's a thought** | `notes/` in any container | Today's brain dump. Agent-readable on request, never auto-acted-upon. |

### 40.3 The collapses (what got killed and why)

**Killed: "Idea" as a separate concept.**
- Reason: It was just a Chat that hadn't been promoted yet, OR a Note in the journal. Two existing concepts already covered it.
- Migration: any existing UI that referred to "Ideas" gets renamed/repurposed. The Ideas view in the mockup becomes the **Recent Chats** view (see §40.7 below) — same surface, accurate name.

**Killed: "Preresearch Chat" as a separate concept.**
- Reason: Same as Idea. It was a Chat with a flag. The flag isn't worth a separate noun.
- Migration: `/preresearch` slash command is removed. **`/chat` is the only chat command.** Chats default to no-action mode — the orchestrator never silently triggers work from a chat. Houston explicitly graduates a chat to a Project when ready.

**Killed: "Research Project" as distinct from "Project".**
- Reason: Every project in a research lab is a research project. The "Research" prefix was redundant verbosity.
- Migration: The PRD now uses **Project** uniformly. `lab/projects/<slug>/` is the canonical filesystem path. Old "research_project_*" naming gets normalized.

**Killed: tasks as a top-level user mental model.**
- Reason: Users don't think "what tasks do I want to create today?" They think "I'm working on Paper 1, what's the state?" Tasks are how the orchestrator operationalizes intent, not how the human plans.
- Kept: the Tasks kanban view stays (it's load-bearing for monitoring agent activity), but it's now explicitly framed as **"agent work tracker"**, not "your project tool". The Project Overview page is the human mental model.

**Killed: the 7-level deep hierarchy in any user-facing surface.**
- Reason: Nobody should have to navigate 7 levels of breadcrumbs to find their work. 5 max.

### 40.4 Many-to-many: Papers ↔ Projects

Houston confirmed: **Project = research thread, NOT paper.** A paper can be associated with multiple projects (e.g. Paper 1 has barriers content from both the "14 ECH Barriers" project and the "ALP Birefringence" project). A project can produce multiple papers over time (e.g. the "f_NL Tracer Pipeline" project produces Paper 2 in 2026, Paper 5 in 2027).

The relationship is **many-to-many** via a join table:

```
papers (id, title, ver, status, ...)
projects (id, lab_id, slug, name, goal, deliverable, ...)
project_papers (project_id, paper_id, role)
  -- role: 'primary' (this paper IS the deliverable)
  --     | 'contributing' (this paper draws from this project)
  --     | 'derivative' (this paper extends a result from this project)
```

In the UI:
- A Paper sidepeek shows the list of associated Projects (with role pills).
- A Project Overview page shows the list of associated Papers (with role pills).
- Searching "Paper 1" surfaces both the paper AND every project linked to it.

### 40.5 The Intent Layer — every level has a goal AND a measurable

Houston's hard rule: **every Lab, Project, Pipeline, and Experiment must have an explicit goal AND a measurable.** No exceptions. The orchestrator refuses to create one without both fields filled.

| Level | Goal field (qualitative) | Measurable field (quantitative) |
|---|---|---|
| **Lab** | Mission — 1 to 3 sentences describing the long-term reason this lab exists | North Star — a single number that, if it goes up, the lab is winning |
| **Project** | Goal — one sentence describing what success looks like | Deliverable — a concrete artifact (paper · catalog · model · tool · package) |
| **Pipeline** | Output description — what dataset/model/result emerges from running all steps | Quality metric — precision, recall, σ, validation accuracy, etc. |
| **Experiment** | Hypothesis — one sentence asserting what the run is testing | Metric — number with units, or pass/fail with a numeric threshold |
| **Chat** | Question — the thing being explored | (n/a — chats are exploratory, no measurable required) |
| **Task** | Action verb — "implement", "review", "fix", "investigate" | done / not-done |

**UI implication:** Every Lab/Project/Pipeline/Experiment surface in the mockup shows three lines at the top:
- **What** — the goal in plain English
- **How we'll know** — the measurable
- **Where we are** — current state vs target

Houston's quote: *"adding clear structure and layered INTENT BASED action to all levels of agentics from the whole lab mission/vision guided by the human+orchestrator down to each project the project orchestrators, leads, workers etc and everything"*

This is the load-bearing principle. The platform's value is **organized intent at every level**. Without it, the agents wander.

### 40.6 The chat-to-project graduation flow

This is the most important UX in the platform — the moment a half-baked thought becomes real research.

**Flow:**

1. **User opens a Chat** (`/chat` in the command palette, or "New chat" button in the sidebar).
2. **User brainstorms with the orchestrator.** Multi-turn conversation, no agent actions taken. The orchestrator can suggest references, surface relevant prior contributions, etc., but **never spawns work** during the chat.
3. **User signals graduation intent.** Examples: "let's make this a project", "ok let's actually build this", "spin this up", "make it real". The orchestrator interprets these loosely and intelligently (any reasonable graduation phrase triggers the flow).
4. **Orchestrator drafts the spec.** It produces:
   - A 1-paragraph project description
   - **Goal** (one sentence — the qualitative target)
   - **Deliverable** (one item — the concrete artifact)
   - **First measurable** (the metric we'll watch)
   - **Mini-plan** (3-7 bullet tasks/experiments)
   - **Datasets needed** (if applicable)
   - **Estimated effort** (rough — "1 week", "2-3 sprints")
5. **Orchestrator asks "look good? (y/n)"** and waits.
6. **On y:** orchestrator creates the Project. This is a multi-step bootstrap:
   - Create `lab/projects/<slug>/` directory with `goal.md`, `deliverable.md`, `chats/preresearch.md` (the founding chat verbatim)
   - Create initial Tasks from the mini-plan
   - Assign existing agents OR spawn new specialized leads + workers if the project needs domain expertise
   - Set up a heartbeat cron + standup cadence
   - Create the project's North Star metric for tracking
   - Open the new Project Overview page in the right pane
7. **On n:** orchestrator asks "what's missing?" and iterates.

**The graduation gate (Houston's pushback rule):** If the orchestrator can't write all 4 fields (goal, deliverable, measurable, mini-plan) from the chat content, **the chat isn't ready to graduate yet.** The orchestrator must say *"this needs more shape — ask me about [the specific gap]"* and not force a half-baked Project. This prevents the platform from being filled with vaguely-defined Project shells that never produce anything.

**The founding chat is preserved.** When a chat graduates, the full chat history (every message, verbatim) is migrated into `lab/projects/<slug>/chats/preresearch.md` as the project's founding artifact. Future agents reading the project history can always trace back to the original brainstorm. **The orchestrator must not lose the founding chat.**

### 40.7 Chats — the third sidebar mode

Houston's confirmed addition: the sidebar gets a **third toggle mode** between Menu and Files: **Chats.**

```
Sidebar tri-mode:
  ┌──────────┐
  │ Menu     │  ← navigation (Director, Overview, Experiments, ...)
  ├──────────┤
  │ Chats    │  ← NEW · recent chats list + project chats grouping
  ├──────────┤
  │ Files    │  ← file tree, notes, storage zones (existing)
  └──────────┘
```

**Chats mode contents:**

- **Recent** (top section) — the 10 most-recent chats across all projects, ungrouped, sorted by last activity. Like ChatGPT or Claude.ai's recent list. Each row: chat title (auto-summarized by orchestrator) + last activity timestamp + project pill (if associated).
- **By Project** (collapsible sections) — chats grouped by their parent Project. Lab-level chats (no project) live in a "Lab-wide" group at the bottom.
- **+ New Chat** button at the top.
- **Resume = full context.** Clicking a chat row opens it in the right pane with full history, just like ChatGPT/Claude.ai. The chat is a first-class persistent surface, not ephemeral.

**Chat composer enrichments** (per §40.10):
- Model switcher
- Mode pill (default vs `/chat` no-action mode vs other modes)
- File/image upload icon
- Mic icon for voice dictation (Whisper integration)
- Slash command autocomplete

### 40.8 The `/notechat` slash command

Houston's request: a one-shot slash command that saves the current chat to Notes with a summary, action items, and a resume link.

**Behavior:**

```
User types: /notechat
Orchestrator: 1. Generates a 3-5 bullet summary of the chat
              2. Extracts any action items mentioned
              3. Extracts any future-thoughts / "remember to" items
              4. Creates a new note: notes/<YYYY-MM-DD>_<chat-slug>.md
              5. Note format:
                 ## Chat: <auto-title>
                 **Saved:** <timestamp>
                 **Resume:** [open chat](hubify://chats/<chat-id>)
                 ### Summary
                 - bullet 1
                 - bullet 2
                 ### Action items
                 - [ ] item 1
                 ### Future thoughts
                 - thought 1
                 ### Full transcript (collapsed)
                 <details><summary>show messages</summary>
                 ... full chat verbatim ...
                 </details>
              6. Toast: "Saved to notes/<filename> · open with ⌘K"
```

The note is markdown. The resume link uses a `hubify://` URL scheme that opens the chat in the right pane. This is part of the broader URL scheme spec (TBD).

### 40.9 Tasks visible at BOTH Project and Experiment level

Houston gave this one to me: "you decide". Decision: **both**, with filter chips.

- **Project-level kanban** — shows ALL tasks across ALL experiments in this project, with experiment-filter chips at the top. Default view is "all experiments". Click a chip to filter to one experiment's tasks.
- **Experiment-level kanban** — shows just that experiment's tasks. No filter chips needed.
- **Lab-level kanban** — shows ALL tasks across ALL projects, with project-filter chips. Useful for the human director scanning lab-wide activity.

This is the only way to scan project state without drilling into every experiment individually. Filter chips solve the "too many tasks" problem.

### 40.10 The chat composer — what it needs

Houston's list of must-haves:

1. **Model switcher** — bottom-row dropdown. Options: Claude Haiku 4.5 / Sonnet 4.6 / Opus 4.6 + cross-provider toggles for GPT-5 / Gemini 2.5 Pro / Grok 4 / Sonar Pro. Default = Sonnet 4.6.
2. **Mode pill** — small pill near the model switcher showing the current chat mode. Modes: `default` (orchestrator can take action), `/chat` (no-action brainstorm only), `/preresearch` (alias for `/chat` — same thing, different verb). Click to cycle.
3. **File/image upload icon** — paperclip icon. Click → file picker. Supports drag-drop into the composer area. Uploaded files attach to the current chat message and become available to the orchestrator's read tool.
4. **Mic icon for voice dictation** — Whisper integration. Click → start recording. Click again → stop, transcribe, insert into composer. Uses OpenAI Whisper API by default (cheapest, fastest, most accurate). Open-source alternative: faster-whisper (local). The platform should let users choose in Settings.
5. **Slash command autocomplete** — type `/` and a popover appears with the available commands (filtered by what makes sense in chat context).
6. **Send button** — primary sage-green button. Keyboard shortcut: ⌘↵ (cmd+enter) — never just enter, because Houston needs newlines in his brain dumps without accidentally sending.

### 40.11 Lab Sharing — the cross-lab sovereignty model

Houston's addition: Labs need explicit Sharing settings. Two dimensions: cross-lab (within the same Hubify user) and public (the world).

**Cross-lab sharing (within a user's account):**

- **Default:** read-only. Lab A can read Lab B's files but cannot write to them.
- **Internal share level:**
  - `none` (default for sensitive labs) — no other labs can see this one
  - `read-only` (recommended default for most labs) — other labs can read all files
  - `read-write` (rare, requires explicit per-lab approval) — other labs can read AND propose changes via PRs (still gated by the destination lab's orchestrator)
- **Per-resource overrides:** individual datasets, models, learnings, or projects can have stricter or looser sharing than the lab default.

**The Lab Sovereignty Rule (HARD invariant):**

> **Agents from Lab A can read files in Lab B and can send comm-events to Lab B's orchestrator. Agents from Lab A CANNOT write to Lab B's filesystem.** The Lab B orchestrator decides whether to accept the suggestion and apply the edit itself.

This prevents multi-lab agent chaos. Cross-lab edits would be the multi-agent equivalent of unbounded merge conflicts. Communication, suggestions, and learnings can flow freely. File edits are sovereign to each lab's own orchestrator.

**The cross-lab comm gateway:**

- Lab A's agent calls `comms.send(target_lab="lab_b", target_agent="orchestrator", payload={...})`
- Lab B's orchestrator receives the message in its inbox
- Lab B's orchestrator decides: ignore, reply with info, or apply (where "apply" means Lab B's own agents do the work)
- All cross-lab comms are logged for audit
- Comms can carry: suggestions, learnings to share, file deltas to consider, attribution chains, etc.

**Public sharing (the world):**

- **Default:** off. Labs are private by default.
- **Public share modes:**
  - `published-only` — only papers explicitly marked as published are visible to the world
  - `published + datasets` — papers + the underlying datasets they cite
  - `published + datasets + models` — papers + datasets + fine-tuned models
  - `everything` — full lab read access (including in-progress work) — for users who explicitly want maximum transparency
- **Granular per-resource:** any individual paper, dataset, model, or contribution can be marked public regardless of the lab default.

The default for new labs starts at `none`. Houston explicitly upgrades to `published-only` when the first paper is ready to ship.

### 40.12 The Project Overview page — the auto-maintained home

Houston's request: every Project needs a simple home/profile/readme that the orchestrator auto-maintains. Don't overcomplicate it.

**Layout:**

```
─── PROJECT NAME ──────────────────────────────────────────
  📌 Goal: [one sentence]
  🎯 Deliverable: [paper / catalog / model / tool]
  📊 Measurable: [metric · current vs target]
  Status: [active · stalled · completed · archived]
  Last updated: [timestamp · who/what updated it]
  Lab: [parent lab pill]

─── DESCRIPTION ───────────────────────────────────────────
  [orchestrator-maintained 1-2 paragraph description of the
   project, what it's trying to do, why, and what's in flight]

─── DELIVERABLES ──────────────────────────────────────────
  Papers: [list of associated papers with role pills]
  Datasets: [list]
  Models: [list]
  Contributions: [list with N-scores]

─── ACTIVE WORK ───────────────────────────────────────────
  Pipelines: [list with progress]
  Experiments: [list with status]
  Tasks: [count by status · open kanban]

─── CHATS ─────────────────────────────────────────────────
  Recent: [list of recent chats associated with this project]
  + Start new chat in this project

─── AGENTS ────────────────────────────────────────────────
  Assigned: [list of agents with role + last activity]
  + Spawn new agent for this project

─── ACTIVITY ──────────────────────────────────────────────
  [last 10 events: experiment completed, chat sent, contribution added, ...]
```

**Auto-maintained means:** the orchestrator updates the Description, Deliverables, Active Work, Recent Chats, and Activity sections automatically as the project progresses. The user can edit Goal, Deliverable, and Measurable manually (they're the human's intent); everything else is computed from the project's actual state.

### 40.13 The 5 hardcoded slash commands for chats

Locked set:

| Command | Purpose | Action |
|---|---|---|
| `/chat` | Open a new chat in no-action mode | Creates a new chat with mode=`chat`, orchestrator can suggest but not act |
| `/preresearch` | Alias for `/chat` (legacy verb, same behavior) | Creates a new chat, identical to `/chat` |
| `/notechat` | Save current chat to Notes | Per §40.8 — generates summary + action items + resume link |
| `/promote` | Graduate the current chat to a Project | Triggers the chat-to-project graduation flow per §40.6 |
| `/share` | Share the current chat (or a project) with another lab or publicly | Opens the sharing settings sidepeek |

All other slash commands are global (outside of chat scope) and live in the ⌘K command palette, not the chat composer.

### 40.14 What this hierarchy stress-tests on the platform

Houston wants to use 5 different labs as deliberate test cases for the platform's architecture. Each lab tests specific platform features:

| Lab | Tests this platform feature |
|---|---|
| **#1 Bounce Cosmology** | The full migration import flow (real data, real history) — see `MIGRATION_BOUNCE_COSMOLOGY_LAB.md` |
| **#2 Hubify Self-Improving** | Self-improvement loops (the lab's job is to improve the platform itself) — see `LAB_HUBIFY_SELF_IMPROVING.md` |
| **#3 Dark Energy** | Cross-lab sharing (this lab shares with #1 Bounce Cosmology) — see `LAB_DARK_ENERGY.md` |
| **#4 Dark Matter** | A cleanly separate domain — tests platform domain-agnosticism — see `LAB_DARK_MATTER.md` |
| **#5 ETI (Extraterrestrial Intelligence)** | Public-facing, viral-potential lab — tests public sharing UX and the publish-loop with non-Anthropic peer review — see `LAB_ETI.md` |

If the platform supports all 5 cleanly, the architecture is right. The lab spec files (above) live in `project-context/` and are linked from this PRD.

### 40.15 Lab = repo (Houston confirmed 2026-04-08)

**Every Lab is its own GitHub repo, its own subdomain, its own filesystem.** This is the load-bearing architecture invariant. Projects are subdirectories inside the Lab's repo, NOT separate repos.

| Layer | What it is | Where it lives |
|---|---|---|
| **Platform** | The Hubify Labs SaaS platform itself | `Hubify-Labs/hubify-labs` (one repo, many tenants) |
| **Lab** | A research domain | `Hubify-Labs/<lab-slug>` (one repo per lab) + `<lab-slug>.hubify.app` (one subdomain per lab) |
| **Project** | A research thread inside a lab | `lab/projects/<project-slug>/` (subdirectory in the lab repo) |
| **Pipeline** | A step sequence inside a project | `lab/projects/<project-slug>/pipelines/<pipeline-slug>/` |
| **Experiment** | A single compute run | `lab/projects/<project-slug>/experiments/<exp-slug>/` (or under a pipeline) |
| **Chat** | A conversation | `lab/chats/<chat-id>.md` (lab-wide) or `lab/projects/<slug>/chats/<chat-id>.md` (project-scoped) |

**The internal Hubify orchestrator agent has GitHub API access to the `Hubify-Labs` org** and can create new lab repos autonomously when a new Lab is created via the platform (see chat-to-lab graduation flow in §40.6 — the lab-creation analogue happens at the orchestrator level when a user clicks "Create new Lab").

**Cross-lab sharing (per §40.11) operates at the GIT level** — Lab A's read-only access to Lab B is implemented as Lab A's agents being able to clone/read Lab B's repo (via GitHub API with read-only permissions), but never push to it. Comms relay sits on top of this and replaces direct edits.

See §1 (top of this PRD) for the full per-lab repo architecture and the ongoing org rename from `Hubify-Projects` → `Hubify-Labs`.

### 40.16 Open questions still pending Houston input

These are smaller decisions that don't block §40 lock-in but should be answered before the migration:

1. ~~**GitHub strategy for Lab #1**~~ — **ANSWERED 2026-04-08:** option (a) — new repo `Hubify-Labs/bigbounce-hubify`. Confirmed by Houston with the architecture clarification that **every lab gets its own repo**. See §1 + §40.15.
2. **Chat default model** — Sonnet 4.6 is my default proposal. Confirm or override.
3. **Voice dictation provider** — Whisper API (cheap, fast, requires sending audio to OpenAI) vs faster-whisper local (privacy, slower setup). Default = Whisper API for v1, settings option to switch.
4. **Cross-lab read-only enforcement layer** — at what level is the file-write block enforced? GitHub API permissions (read-only token per cross-lab pair), application-layer (Convex auth), or both? Default = both.
5. **The exact subdomain for migrated BigBounce Lab** — Houston mentioned `bigbounce2.hubify.app` as a placeholder. Final answer goes in `MIGRATION_BOUNCE_COSMOLOGY_LAB.md`. Alternatives: `bb.hubify.app` (shorter), `bounce.hubify.app` (cleaner), or repurpose `bigbounce.hubify.app` after cutover (most aggressive — requires retiring the original site).

### 40.17 What changes in the mockup as a result of §40

Tracked as separate mockup tasks (see `.queue.md` polish passes):

**Tier 1 — chat / hierarchy / project (§40 core):**
- [ ] **Add third sidebar mode "Chats"** between Menu and Files (§40.7)
- [ ] **Project Overview page** as a new view + sidepeek renderer (§40.12)
- [ ] **Chat composer enrichments** — model switcher, mode pill, file upload, mic icon (§40.10)
- [ ] **`/chat`, `/notechat`, `/promote`, `/share` slash commands** wired into the chat surface (§40.13)
- [ ] **Lab Sharing settings sidepeek** in the Settings view (§40.11)
- [ ] **Cross-lab comm gateway visualization** — small panel showing inbound/outbound comms with other labs
- [ ] **Rename "Ideas" view → "Recent Chats" view** (§40.3 collapse)
- [ ] **Project filter chips on Lab kanban** + experiment filter chips on Project kanban (§40.9)
- [ ] **Project ↔ Paper many-to-many** — paper sidepeek shows associated projects, project page shows associated papers (§40.4)

**Tier 2 — Files sidebar + Notes UX overhaul (Houston feedback 2026-04-08, with 3 screenshots):**
- [ ] **Strip emojis from note file names** — looks ugly + off-brand. Houston: "no emojis in note file names as it's just clutter". Future scope: optional per-note icon (Notion-style) but never default and never with a wrapper fill.
- [ ] **Kill the new-note sidepeek** entirely. Replace with a **full-page note editor** that opens in the right pane, like a blank file. Houston: "feel powerful like a blank Obsidian page (or Notion page) using our existing file system... not a sidepeek afterthought"
- [ ] **Inline editable filename at the top** of the note editor (Obsidian/Notion pattern). No separate filename field at the bottom.
- [ ] **The "How notes work" content** stays but moves to a hover/click `(i)` info popout next to the Notes section header. Inside the popout: the existing copy + a link to `hubify.com/docs#notes` (future docs page).
- [ ] **Per-note scoped chat session** — each note has its own dedicated chat by default. User can vibe-edit: brain-dump or paste into the editor, then ask the chat agent "keep my brain dump for context, rewrite/summarize/improve the note". Toggle: hide/show the chat to focus solo, click chat icon to bring it back.
- [ ] **Markdown slash commands** in the note editor — same blocks/shortcuts as Obsidian (or Notion if equivalent). Headings, lists, code blocks, links, callouts, quotes, etc.
- [ ] **Files sidebar sub-tabs** — apply the existing top-tab pattern (Menu | Chats | Files) recursively inside the Files mode: **Files | Notes | Storage**. Three sub-modes inside the Files panel, same UI/UX pattern as the parent. Avoids stacking three vertical sections.
- [ ] **Notes sub-mode behavior:**
  - Section collapsed by default (all subdir groups closed). Currently opens with all subdirs expanded — annoying.
  - **Star/favorite to pin** notes to the top for quick access. Stars are local-only state by default, syncable as a future feature.
  - **Line limit + `[load more...]`** button — don't show all notes at once. Show ~10 most-recent or starred, then "load more" expands the list.
- [ ] **Storage sub-mode cleanup** — kill GitHub from the storage tier list (it's the same thing as the Files Files tab — the project source). Mark S3 Glacier and Vercel as "pending Houston decision" until §40.17.S below is resolved. Keep Git LFS (it's actually a separate storage backend).
- [ ] **T# storage tier labels** — Houston isn't sure they're useful to humans. Decision: keep them but de-emphasize visually (smaller, more muted) so they read as "engineering metadata" not "user navigation". The labels stay because agents need them; the human eye can ignore them.

**§40.17.S — Storage tier inventory cleanup (pending Houston input):**

Houston flagged 3 storage decisions in his 2026-04-08 batch:
1. **S3 Glacier** — currently shown as empty in the mockup. Are we adopting AWS S3 Glacier for cold backup, or sticking with Backblaze B2 (current plan)? My recommendation: **Backblaze only**. B2 is ~5x cheaper than Glacier for the same redundancy class (~$0.005/GB/mo vs ~$0.024/GB/mo Glacier Deep Archive equivalent, after egress fee normalization), and Backblaze offers a free 10 GB tier. Unless Houston specifically wants AWS vendor diversity, kill S3 Glacier from the storage tier list.
2. **Vercel Blob** — currently shown in the storage tier list. Vercel Blob is useful for binary assets that need CDN-fast public delivery (e.g., paper PDFs served from `<lab>.hubify.app/papers/main.pdf`). My recommendation: **keep Vercel Blob ONLY for the public-facing `Z5 Public` zone, not as a general-purpose storage tier**. The website itself is on Vercel deploys (a different thing — that's serverless functions + static site, not Blob).
3. **GitHub vs GitHub LFS** — Houston correctly noticed that GitHub appears as a "storage tier" but it's also the main project file source (the `Files Files` tab content). My recommendation: **kill GitHub as a separate storage tier**. It's the project source, not "storage". Keep Git LFS as a separate tier because it really is a separate storage backend (large binary objects stored externally and referenced by pointer in the git tree). The Files | Files sub-tab IS the GitHub source — no need to duplicate it as a storage line.

**Final decision matrix once Houston approves:**

| Storage tier | Keep / Drop | Reason |
|---|---|---|
| T1 Local (laptop) | Keep | Houston's Mac, source of truth for in-flight edits |
| T2 GitHub | **Drop** (it IS the Files tab) | Files \| Files sub-tab covers this |
| T3 Git LFS | Keep | Real storage backend, separate from regular git |
| T4 Convex DB | Keep | Application state |
| T5 Pod root | Keep | RunPod ephemeral |
| T6 RunPod vol | Keep | Pod persistent volume |
| T7 S3 Glacier | **Drop** unless Houston wants AWS vendor diversity | Backblaze B2 is cheaper |
| T8 Backblaze B2 | Keep (re-add if missing) | Cheap cold backup |
| T9 Hugging Face | Keep | Public model + dataset hosting |
| T10 Vercel deploys | Keep | Static site serving |
| T11 Vercel Blob | **Drop** unless used for Z5 Public PDFs | Niche, easy to add later |

**Tier 3 — Mintlify docs port (locked here so it's not lost):**
- [ ] **Replicate the EXACT Mintlify docs setup** from the existing `~/Desktop/CODE_2025/hubify/` repo into the new `Hubify-Labs/hubify-labs` platform repo. Houston: "it was annoyingly complex (issue prone) to get it right on the hubify.com/docs subpath vs subdomain so don't wanna go through that nightmare again and need to make sure it all ports over nice and clean".
- [ ] **The setup uses a SUBPATH (`hubify.com/docs/...`), not a subdomain (`docs.hubify.com`).** This is non-trivial because Mintlify defaults to the subdomain pattern; the subpath setup requires Vercel rewrite rules + Mintlify deployment configuration that took multiple iterations to get right in the original repo.
- [ ] **Files to port verbatim** (do not regenerate from scratch — copy and adapt):
  - `hubify/docs/mint.json` (Mintlify config)
  - `hubify/docs/snippets/`, `hubify/docs/api-reference/`, `hubify/docs/essentials/` (the actual content directories — content gets rewritten for Hubify Labs but the directory structure + nav config stays identical)
  - `hubify/vercel.json` (the rewrite rules for `/docs/*` → Mintlify)
  - Any custom CSS / JS in `hubify/docs/css/` and `hubify/docs/js/`
- [ ] **The rewritten docs content** for Hubify Labs will live at `Hubify-Labs/hubify-labs/docs/` and serve at `hubify-labs.com/docs/...` (or whatever the new platform domain is — TBD).
- [ ] **First docs pages to write** for Hubify Labs:
  - `/docs/notes` — the page Houston referenced in the Notes UX feedback (the (i) popout in the Files sidebar links here). Covers: what notes are, how the agent visibility contract works, the per-note chat, slash commands, sharing.
  - `/docs/labs/getting-started` — how to create your first lab
  - `/docs/labs/migration` — how to migrate an existing research repo into Hubify Labs (the public version of `MIGRATION_BOUNCE_COSMOLOGY_LAB.md`)
  - `/docs/agents/hierarchy` — orchestrator → leads → workers explainer
  - `/docs/agents/cross-provider` — peer review setup with GPT/Gemini/Grok/Perplexity
  - `/docs/projects/lifecycle` — chat → project graduation flow
  - `/docs/api/...` — API reference for the platform's own API + MCP server

**Tier 4 — `hubify://` URL scheme (referenced in §40.8):**
- [ ] Spec the `hubify://` URL scheme. Used by `/notechat` resume links and the broader deep-link system. Examples:
  - `hubify://chats/<chat-id>` — open a specific chat
  - `hubify://labs/<slug>/projects/<slug>` — open a specific project
  - `hubify://labs/<slug>/files/<path>` — open a file in the file preview pane
  - `hubify://labs/<slug>/notes/<filename>` — open a specific note in the note editor
  - `hubify://agents/<name>` — open an agent sidepeek
- [ ] The URL scheme works in: the desktop Mac app (registered via `Info.plist`), the web app (intercepts `hubify://` clicks via JS and routes), and the CLI (`hubify open hubify://...`).

These get built in subsequent loop iterations once the PRD §40 + lab specs land.

### 40.18 Linked planning files (the 5-lab stress test)

The full migration plan and the 5 lab spec files live in `project-context/` and are linked here so this PRD stays the single source of truth for "what's the plan":

| # | Lab | File | Status |
|---|---|---|---|
| **#1** | **Bounce Cosmology Lab** (the migration — super-super-clear #1 priority) | [`MIGRATION_BOUNCE_COSMOLOGY_LAB.md`](./MIGRATION_BOUNCE_COSMOLOGY_LAB.md) | SPEC COMPLETE — awaiting execution |
| **#2** | **Hubify Self-Improving Lab** (meta-lab — improves the platform) | [`LAB_HUBIFY_SELF_IMPROVING.md`](./LAB_HUBIFY_SELF_IMPROVING.md) | SPEC ONLY — Houston creates via platform |
| **#3** | **Dark Energy Lab** (cross-lab sharing test, redeems Paper 1) | [`LAB_DARK_ENERGY.md`](./LAB_DARK_ENERGY.md) | SPEC ONLY — Houston creates via platform after #1 |
| **#4** | **Dark Matter Lab** (domain-agnosticism test) | [`LAB_DARK_MATTER.md`](./LAB_DARK_MATTER.md) | SPEC ONLY — Houston creates via platform |
| **#5** | **Extraterrestrial Intelligence Lab** (public-facing viral test) | [`LAB_ETI.md`](./LAB_ETI.md) | SPEC ONLY — Houston creates via platform after #3 |

**Order of execution:**
1. Lab #1 migration (Day 1 — see migration plan)
2. Lab #2 spec'd, NOT built yet (waits until Lab #1 is stable, ~2-4 weeks post-migration)
3. Lab #3 created via platform (after Lab #1 is stable) — first cross-lab sharing test
4. Lab #4 spec'd, possibly never built (placeholder for domain-agnosticism test)
5. Lab #5 created via platform (after Lab #3 succeeds) — first public-facing lab

Houston explicitly does NOT want Labs #2-#5 seeded into the database. He wants to test the platform's "create new lab" flow himself. The specs above are templates that the orchestrator (and/or Houston) reads when bootstrapping each lab.

### 40.19 Why §40 supersedes §35

§35 (the original Hierarchy Taxonomy) was written before Houston pushed back. It described a 7-level model with "Idea" and "Preresearch Chat" as separate concepts. §40 collapses those into the 5-level model. Where they conflict:

| Topic | §35 said | §40 says (final) |
|---|---|---|
| Levels | 7 (Global → Lab → Project → Preresearch → Idea → Pipeline → Experiment → Task) | 5 (Lab → Project → Pipeline → Experiment → Task) + Chat as a parallel surface |
| Idea | Separate concept with own UI | Killed — collapses into Chat or Note |
| Preresearch Chat | Separate concept with own UI | Killed — collapses into Chat with no-action default |
| Project = paper or thread? | Ambiguous | Thread (M:M with papers) |
| Goal/measurable per level | Optional | **Mandatory** at every level |
| Tasks in user mental model | Top-level | Demoted — agents' work tracker, not user's planning tool |

§35 stays in the doc for the historical record but should be considered **deprecated**. Future agents and developers must read §40 as the source of truth.

---

## 41. Compute Routing & Credits Monitoring — How Agents Choose Where to Run

**Status:** Locked 2026-04-08 by Houston after the Modal/RunPod Serverless equivalence question. Companion section to §24 (Compute Provider — RunPod ONLY).

### 41.0 Why this section exists

The orchestrator dispatches dozens to hundreds of jobs per week. Without clear rules, it would default to the wrong compute mode at the wrong time and burn money — most commonly by running CPU work on GPU pods (10-20× overpriced). This section locks the 4 routing rules every agent must follow before dispatching a job.

Houston's quote: *"ensure our agents know when to spin up CPU pods/serverless vs GPUs pods/serverless etc too please so we don't waste GPU pods hours on basic cpu runs."*

### 41.1 The 4 routing rules (HARD INVARIANTS)

These 4 questions must be answered for every dispatch, in this order:

#### Rule 1 — CPU vs GPU (THE most important rule, biggest cost lever)

**The question:** Does this task have a tensor operation in the hot path?

| Task type | Answer | Where to run |
|---|---|---|
| Autoencoder training | yes (matrix multiplies, backprop) | **GPU** |
| CNN inference (galaxy chirality) | yes | **GPU** |
| LLM inference (self-hosted) | yes | **GPU** |
| Large MCMC chains with Stan/Cobaya GPU acceleration | yes (when GPU acceleration is configured) | **GPU** |
| LaTeX compile (`pdflatex main.tex`) | no | **CPU** |
| Pandas / numpy data wrangling | no (numpy uses BLAS, not GPU) | **CPU** |
| CSV / JSON / parquet processing | no | **CPU** |
| Cross-matching catalogs (TreeCorr, k-d trees) | no (CPU-bound spatial joins) | **CPU** |
| Symbolic regression (CPU-bound search) | no | **CPU** |
| Bibliography management, paper formatting | no | **CPU** |
| Agent orchestration scripts | no | **CPU** |
| File packaging (tar, zip) | no | **CPU** |
| Webhook/API receiving | no | **CPU** |

**The cost ratio:** GPU pods are $1.50-$4.00/hr. CPU pods are $0.10-$0.20/hr. GPU serverless is $2-$4/hr equivalent. CPU serverless is $0.10-$0.20/hr equivalent. **A GPU running CPU work is 10-20× overcharged.** This rule alone can cut compute spend by 30-50% on a typical research week.

**Enforcement:** the orchestrator's `dispatch_experiment()` function MUST check the experiment's `requires_gpu` field before selecting a compute mode. If the field is missing, the orchestrator refuses to dispatch and asks the experiment author (or the agent that proposed it) to explicitly set the field. **No GPU dispatch without explicit `requires_gpu: true`.**

#### Rule 2 — Pod vs Serverless (the duration question)

**The question:** How long will this task run, and how often will it be invoked?

**Use a Pod (always-on) when:**
- Single job duration > 1 hour (e.g., MCMC chains, multi-epoch training)
- You'll dispatch many sequential jobs in a row from the same context (cold-start cost > break-even)
- The workload needs persistent state between calls (a Jupyter session, an in-memory cache)
- Active research week — you're going to use this pod for many hours per day
- The job needs SSH access for debugging

**Use Serverless (auto-scale) when:**
- Single job duration < 30 minutes
- Bursty / spiky workload (anomaly batch processing — 1000 anomalies, then nothing for an hour)
- Embarrassingly parallel — you can shard the work and run 100 workers concurrently for 30 sec each
- Webhook-triggered (new paper submitted → run claims-audit)
- Total duty cycle < 20% of wall time (the GPU would sit idle most of the day on a Pod)

**The break-even math:** if you need < 4 hours of compute per 24 hours of wall time, Serverless wins. More than that, Pod wins. The orchestrator computes this on-the-fly per experiment dispatch.

**Edge cases:**
- A 5-hour single job → Pod (Serverless 24h cap is fine but Pod is cheaper for guaranteed run)
- 100 × 1-minute calls per day → Serverless (Pod would idle 23h)
- 20 × 30-minute calls per day → either works; default to Serverless (10 hours total = under break-even when you account for cold starts being amortized)
- A 30-hour MCMC chain → Pod ONLY (Serverless 24h cap blocks this — must use Pod with checkpointing per §41.4)

#### Rule 3 — When to spin up a NEW pod vs reuse an existing one

**The question:** Is there a pod already running with the right GPU type and free capacity?

| State | Action |
|---|---|
| Existing pod is running, right GPU, idle | **Reuse it** (dispatch the new job to the existing pod) |
| Existing pod is running, right GPU, busy with another job | **Wait** (queue the new job, dispatch when current finishes) — UNLESS the queued job is high-priority, in which case spin up a second pod |
| Existing pod is running, WRONG GPU (e.g. need H200, current is RTX 4090) | **Spin up a new pod** with the right GPU |
| No existing pod | **Spin up a new pod** OR dispatch to Serverless if the job qualifies per Rule 2 |
| Existing pod is stopped but volume preserved | **Restart it** (faster than fresh provision, ~30-90 sec) |

**The orchestrator must NOT spin up a second H200 pod if the first one is idle.** Houston has been burned by this exact pattern before.

#### Rule 4 — Always have a recovery checkpoint (the credits-don't-die rule)

**The question:** If the credits run out mid-run, can this job recover from a checkpoint?

**Mandatory for any job > 30 minutes:**
- Write a checkpoint every 10 minutes (configurable per job type)
- Checkpoint files go to RunPod network volume (T7) AND get backed up to Backblaze B2 (T8) on the next backup cron tick (every 15 min)
- The job's resume logic must be tested before deploying: can it actually pick up from the checkpoint after a forced kill?

**Optional for jobs < 30 minutes:** but recommended if the job is expensive (e.g., a 25-minute MCMC step that would cost $1.50 to redo).

**Pod kill is graceful:**
1. Send `SIGTERM` to the running process
2. Wait 30 seconds for the checkpoint flush
3. Send `SIGKILL` if still running
4. Stop the pod (volumes preserved)

This means even an "emergency" credit-out shutdown loses at most 30 seconds of work, not 30 hours.

### 41.2 RunPod credits API (the live monitoring loop)

**The endpoint:** `https://api.runpod.io/graphql` (GraphQL)
**Auth:** `Authorization: Bearer $RUNPOD_API_KEY`
**Query:**
```graphql
query {
  myself {
    clientBalance     # current credit balance in USD
    spendDetails {    # spending history for burn-rate calculation
      localStartDate
      localEndDate
      gpuTypeId
      cost
    }
  }
}
```

**The cron:** `gpu-manager-lead` runs a "credits check" cron every 15 minutes.

```python
# routines/credits_check.py
import requests, os, datetime, json
from pathlib import Path

API_KEY = os.environ["RUNPOD_API_KEY"]
QUERY = '{"query": "query { myself { clientBalance spendDetails { cost localStartDate } } }"}'

def check_credits():
    r = requests.post(
        "https://api.runpod.io/graphql",
        headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
        data=QUERY,
        timeout=10,
    )
    data = r.json()["data"]["myself"]
    balance = data["clientBalance"]
    # Compute 24h burn rate from spendDetails
    yesterday = (datetime.datetime.utcnow() - datetime.timedelta(hours=24)).isoformat()
    burn_24h = sum(s["cost"] for s in data["spendDetails"] if s["localStartDate"] >= yesterday)
    burn_per_hour = burn_24h / 24.0
    runway_hours = balance / burn_per_hour if burn_per_hour > 0 else 999
    # Log to lab/compute/credits_log.jsonl
    log = {"ts": datetime.datetime.utcnow().isoformat(), "balance": balance, "burn_24h": burn_24h, "burn_per_hour": burn_per_hour, "runway_hours": runway_hours}
    with Path("lab/compute/credits_log.jsonl").open("a") as f:
        f.write(json.dumps(log) + "\n")
    # Trigger threshold actions per §41.3
    return log
```

**The output gets surfaced in the UI:**
- Director header pill: `$29.35 · 47h runway` (current balance + projected hours-until-zero based on 24h burn rate)
- Compute view: full credits history chart (balance over time, burn rate per day)
- Status bar: alert color changes per threshold (green / yellow / red / critical)

### 41.3 The 4 credit thresholds (escalating actions)

| Threshold | Balance | Action | Notification |
|---|---|---|---|
| **HIGH** | > $50 | Normal operations. Continue dispatching. | None |
| **WARN** | $20 - $50 | Pause dispatching of "low-priority" experiments. Active research continues. | Director sees yellow pill. Next standup mentions it. |
| **CRIT** | $5 - $20 | (1) Trigger full backup of all volumes to Backblaze B2 (2) Verify backup integrity (3) Pause ALL new dispatches (4) Existing jobs continue but will not auto-restart | Director sees red pill. Critical-tier comm event in activity feed. Houston gets a comm-event in his inbox. |
| **EMERGENCY** | < $5 | (1) Send SIGTERM to all running pods (graceful kill, 30 sec checkpoint window) (2) Stop all pods (volumes preserved) (3) Cancel any in-flight serverless calls (4) Set lab status to "credits-exhausted" | Director sees critical-tier alert pill. Houston gets a phone push notification (if enabled). All standups paused until topped up. |

**The 4 thresholds are configurable per lab** in `lab/compute/credit_thresholds.yaml`:
```yaml
thresholds:
  high: 50
  warn: 20
  crit: 5
  emergency: 1   # absolute floor — anything below this is full shutdown
recovery:
  resume_at: 30  # auto-resume normal operations when credits cross back above this
```

**Why these specific numbers** (for the BigBounce / single-H200 baseline):
- $50 = ~14 hours of H200 at $3.59/hr = comfortable buffer
- $20 = ~5.5 hours of H200 = enough for one substantial experiment
- $5 = ~1.4 hours of H200 = enough to checkpoint and shut down gracefully
- $1 = absolute floor, safety net

For labs with multiple pods or more expensive GPUs, scale the thresholds proportionally.

### 41.4 The pre-credit-out backup workflow (the "no data loss" guarantee)

When CRIT threshold fires, this exact sequence runs:

```
1. gpu-manager-lead detects balance < $20
   ↓
2. Pause dispatcher (no new experiments accepted)
   ↓
3. For each running pod:
     a. Send a "checkpoint please" signal to the running job (custom signal handler in the job's runner)
     b. Wait up to 60 seconds for the job to flush its checkpoint
     c. Verify the checkpoint file exists on the network volume
   ↓
4. For each network volume attached to a running pod:
     a. Sync to Backblaze B2 (incremental sync — only changed files since last backup)
     b. Verify the sync succeeded (checksum a sample of files)
   ↓
5. Mark the lab's compute status as "backup-complete · awaiting top-up"
   ↓
6. Send Houston a comm-event: "BigBounce credits at $18.40, all volumes backed up, pods still running but no new dispatches. Top up at: <runpod billing url>"
   ↓
7. Wait. Continue to monitor.
   ↓
8. If balance keeps dropping (i.e., active jobs still burning), and hits EMERGENCY ($5):
     a. SIGTERM all running pods
     b. 30 sec graceful checkpoint window
     c. SIGKILL stragglers
     d. Stop all pods
     e. Final volume sync to Backblaze
     f. Lab status = "credits-exhausted, all data safe"
     g. Director gets a phone push if enabled
```

**Result:** even in the worst case (Houston is asleep, credits run out, no human intervention), the lab loses ZERO data. All checkpoints are flushed to network volume + Backblaze B2 before the pod stops. Resume on top-up is a single command.

### 41.5 The auto-resume workflow (when credits get topped up)

```
1. gpu-manager-lead detects balance crosses above $30 (the recovery threshold)
   ↓
2. Lab status changes from "credits-exhausted" → "credits-restored"
   ↓
3. For each pod that was stopped during the credits-out event:
     a. Restart the pod (RunPod API call: ~30-90 sec)
     b. Verify the network volume is mounted
     c. Verify the checkpoint file exists
     d. Restart the job from the checkpoint
   ↓
4. Resume normal dispatcher operation
   ↓
5. Send Houston a comm-event: "Credits restored, all 3 pods resumed from checkpoint, no work lost"
```

**This is the key resilience guarantee:** the platform survives running out of credits without losing any in-flight work, as long as the recovery checkpoint discipline (Rule 4 of §41.1) is followed.

### 41.6 Per-job dispatcher decision tree (the orchestrator's mental model)

When the orchestrator receives a new experiment to dispatch:

```
new experiment received
  │
  ├─ Does it specify requires_gpu? (Rule 1)
  │   ├─ NO → REJECT, ask author to specify
  │   ├─ FALSE → CPU mode
  │   └─ TRUE → GPU mode
  │
  ├─ How long will it run? (Rule 2)
  │   ├─ < 30 min, bursty → Serverless
  │   ├─ 30 min - 4h → either; default Serverless if duty cycle < 20%
  │   ├─ 4h - 24h → Pod (better cost) or Serverless (if parallelizable)
  │   └─ > 24h → Pod ONLY (Serverless cap blocks this; checkpoint required per Rule 4)
  │
  ├─ Is there an existing pod with the right GPU + free capacity? (Rule 3)
  │   ├─ YES → reuse it
  │   ├─ YES but busy → queue (or spin up second if priority)
  │   └─ NO → provision new pod (or dispatch to Serverless)
  │
  ├─ Does the job have checkpoint discipline? (Rule 4)
  │   ├─ Job > 30 min and no checkpoint → REJECT, require checkpointing
  │   └─ OK → proceed
  │
  ├─ Check current credit balance (§41.2)
  │   ├─ HIGH → dispatch
  │   ├─ WARN → dispatch only if priority ≥ medium
  │   ├─ CRIT → dispatch only if priority = critical
  │   └─ EMERGENCY → REJECT
  │
  └─ DISPATCH
       ↓
     Log to experiments table with: mode (pod/serverless), gpu/cpu type, estimated cost, checkpoint plan
```

### 41.7 What changes in the mockup

Tracked as separate mockup tasks (see `.queue.md`):

- [ ] **Strip Modal references entirely** — Costs view table row, Settings → Modal API token field, Compute view "Modal coming soon" provider card, orchestrator sidepeek meta line "compute: RunPod (Modal coming soon)", vibe-coding command "modal logs"
- [ ] **Add Compute Mode to experiment dispatch flow** — when Houston (or an agent) creates a new experiment, the form must include `requires_gpu` (boolean), `expected_duration_min` (number), `priority` (low/med/high/critical) so the orchestrator can route per §41.1
- [ ] **Director header credits pill** — current balance + runway in hours (e.g., `$29.35 · 47h`) — color-coded by threshold (green/yellow/red/critical)
- [ ] **Compute view enriched** — credits history chart (balance over time), burn rate per day, threshold lines on the chart, last credits-out event timeline
- [ ] **Per-experiment cost mode** — top experiments table gets a new column "mode" showing pod/serverless/cpu-pod/cpu-serverless attribution

### 41.8 Open questions

1. **RunPod GraphQL endpoint stability** — RunPod's API has changed before. The credits-check cron should be wrapped in a retry-on-failure pattern with a fallback to "assume HIGH" (don't accidentally trigger credit-out shutdowns just because the API is briefly down).
2. **Push notification for EMERGENCY** — does Houston have a phone push channel set up? Options: Pushover, Pushbullet, ntfy.sh, Telegram bot. Default = ntfy.sh (free, simple, no account needed).
3. **Backblaze B2 alternative** — if the user doesn't have B2 set up, fallback to local-only checkpoints + Houston notification. Document this fallback in the gpu-manager-lead's agent.md.
4. **Recovery threshold gap** — currently `recover_at: 30` (above the WARN threshold of 20). This prevents flapping. Confirm with Houston this gap is right.

---

## 42. macOS Desktop App Spec (Tauri 2 Shell)

**Status:** Locked 2026-04-08. Full spec lives in `project-context/DESKTOP_APP_SPEC.md` (700 lines). This section is the PRD-resident summary that points at the canonical file.

### 42.0 Why this section exists

Houston lives in macOS. The web app at `https://hubify-labs.com` covers the cross-platform case, but a real native chrome on macOS gives him: native window controls + system menu bar + Touch Bar + native notifications + dock badge + Finder file drop + `hubify://` URL scheme handler + launchd background service + iCloud sync for journal notes. The desktop app is the **primary surface for the founder**, the web app is the **backup surface and cross-platform fallback**.

### 42.1 Decision: Tauri 2.x

DECISION: Tauri 2.x (over Electron, native Swift, React Native).

Reasons:
- 5-10× smaller bundle than Electron (~10MB vs ~150MB)
- Native WKWebView (no Chromium runtime shipped with the app)
- Rust backend for filesystem + auth + IPC
- Cross-compile to macOS / Linux / Windows from one toolchain
- Mature signing + notarization via `tauri-action`

Rejected:
- **Electron** — bundle size + memory hog
- **Native Swift / SwiftUI** — doubles the codebase, the team is solo (Houston)
- **React Native macOS** — ecosystem fragmentation, Microsoft fork status uncertain

### 42.2 The 11 native features (full spec in DESKTOP_APP_SPEC.md §1)

1. Native window chrome (or borderless like Linear/Cursor)
2. Native menu bar (App / File / Edit / View / Window / Help) with keyboard shortcuts
3. Dock badge (unread notification count)
4. Native notifications (`NSUserNotification`)
5. Native file drop (Finder → app)
6. `hubify://` URL scheme handler registered in `Info.plist`
7. launchd background service (orchestrator runs even when the main app is closed)
8. Native keyboard shortcuts (⌘N new note, ⌘K command palette, ⌘W close tab)
9. iCloud sync for journal notes (optional toggle)
10. Code signing identity + notarization (`tauri-action` workflow)
11. Auto-update channel (Tauri's built-in updater, not Sparkle)

### 42.3 Menu bar app variant (DESKTOP_APP_SPEC.md §2)

A separate Tauri window with `decorations:false`, `alwaysOnTop:true`, `skipTaskbar:true`, anchored under the macOS menu bar icon via `tauri-plugin-positioner`. Uses the `NSStatusItem` API. Popover content: Director status · credits + runway · quick chat input · recent activity · "Open Hubify Labs" button.

For users who want always-resident monitoring without the full app window taking screen space.

### 42.4 iOS deferral (DESKTOP_APP_SPEC.md §3.5)

iOS is **deferred to v2**. Reasons:
- iOS is mostly a viewer not a driver — the work happens at a desk
- Native iOS dev is expensive (Tauri 2 iOS is not production-ready, Swift/RN both multi-week investments)
- Web app on Safari mobile + ntfy.sh + PWA manifest already covers ~80% of the iPhone use case
- ntfy.sh handles the only thing that requires native iOS (push notifications)

v1 ships with: mobile-responsive web + ntfy.sh + PWA manifest + universal links to handle `hubify://` URLs in Safari.
v2 plan: re-evaluate Tauri 2 iOS in Q3 2026, fall back to Swift/SwiftUI if it's still not ready.

### 42.5 Distribution

- macOS Universal binary (Apple Silicon + Intel) signed + notarized
- Direct download from `https://hubify-labs.com/download/mac`
- Homebrew cask: `brew install --cask hubify-labs/tap/hubify-desktop`
- Auto-update via Tauri's built-in updater (signed manifest at `https://hubify-labs.com/desktop/updates.json`)

### 42.6 Linked file

Full inventory + 700 lines of detail: `project-context/DESKTOP_APP_SPEC.md` (committed `d025f47`, iOS deferral statement added in commit `4695389`).

---

## 43. REST + GraphQL API Spec (the v1 contract)

**Status:** Locked 2026-04-08. Human-readable spec in `project-context/API_SPEC.md` (~500 lines). Machine-readable contract in `project-context/api-spec.openapi.yaml` (OpenAPI 3.1, ~600 lines, commit `8ea7a93`).

### 43.0 Why this section exists

Hubify Labs is split across many surfaces (web · macOS · iOS web · CLI · MCP server · cron jobs). All of them talk to the same backend. The API spec is the **single contract** every surface depends on.

### 43.1 Versioning

URL path versioning (`/v1/...`). 12-month deprecation policy. `Sunset` and `Link` headers on deprecated endpoints.

### 43.2 Auth (full detail in API_SPEC.md §2)

- **JWT HS256** with 3 token types: `user` (interactive) · `agent` (per-agent service token) · `service` (CI / cron)
- **Per-lab scopes** enforce the Lab Sovereignty Rule (`PRD §40.11`) at the auth layer — cross-lab writes return **403 with type `cross-lab-write-denied`** before reaching any handler
- **3-tier rate limits** per token type, with per-endpoint overrides for expensive operations (search, dispatch)

### 43.3 Endpoint inventory

**~85 endpoints across 19 groups** (full list in API_SPEC.md §3):

labs · projects · pipelines · experiments · files · chats · papers · notes · agents · memory · contributions · compute (pods + credits) · cross-lab comms · webhooks · search · standups · routines · backups · costs

### 43.4 Error format

**RFC 7807 Problem Details** (`application/problem+json`). 11 standard error type slugs (full list in API_SPEC.md §5). Every error has a `type`, `title`, `status`, `detail`, and instance-specific `links` to the relevant PRD section.

### 43.5 GraphQL

Single endpoint `/v1/graphql` for read-heavy queries that need joins (e.g. "give me all experiments for this project with their latest log line and current status"). REST is the primary surface for write operations. Full GraphQL schema deferred to v1.1 — example queries documented in API_SPEC.md §7.

### 43.6 PRD §41 routing requirement

The experiment dispatch endpoint (`POST /v1/experiments`) **MUST return 422** if `requires_gpu` is missing from the body. This is the API-layer enforcement of the §41 routing rule. The CLI (cli-spec.yaml) and MCP server (mcp-server-spec.yaml) enforce the same rule before sending the request.

### 43.7 Linked files

- Human spec: `project-context/API_SPEC.md` (commit `eb3bcfd`)
- Machine spec: `project-context/api-spec.openapi.yaml` (commit `8ea7a93`)

---

## 44. MCP Server Spec — How AI Agents Drive Hubify Labs

**Status:** Locked 2026-04-08. Human-readable spec in `project-context/MCP_SERVER_SPEC.md` (~700 lines, commit `0546d5d`). Machine-readable contract in `project-context/mcp-server-spec.yaml` (commit `19917e0`).

### 44.0 Why this section exists

Hubify Labs ships with a Model Context Protocol server so any MCP-aware client (Claude Code, Cursor, custom agents) can read lab state and drive actions. The MCP server is the **agent surface** to the platform — the API + CLI are for humans + scripts, the MCP server is for LLMs.

### 44.1 The 4 MCP primitives

1. **Tools** — actions agents can take (read file, dispatch experiment, save note, send comm, etc.)
2. **Resources** — data agents can read (lab metadata, experiment logs as live SSE, projects list, papers, contributions)
3. **Prompts** — reusable prompt templates the server provides to clients
4. **Sampling** — the server can request the client to sample from the model (used by `houston_method_post_experiment` and `publish_ready_check` prompts)

### 44.2 The 3 transports

1. **stdio** — default, for CLI-spawned servers (Claude Code's pattern)
2. **SSE** (HTTP server-sent events) — for web-based MCP clients
3. **WebSocket** — for high-throughput streaming use cases

### 44.3 Tool inventory

**~30 tools across 11 categories** (full list in MCP_SERVER_SPEC.md §2):

filesystem · experiment dispatch (with §41 routing) · agent invocation · cross-lab comms · memory · contributions · notes · chats · LaTeX/paper · compute · search

Every tool documents its REST endpoint mapping (so the MCP server is a thin wrapper over the API, not a parallel implementation).

### 44.4 Resources

**~15 resources** total: 10 snapshot resources (lab metadata, projects, agents, papers, contributions, datasets, wiki, notes, pods, runtime status) + 5 live SSE streams (activity feed, credits, standups, comms inbox, experiment logs).

### 44.5 Prompt templates

6 templates: `review_paper` · `houston_method_post_experiment` · `draft_chat_to_project` · `standup_facilitate` · `publish_ready_check` · `no_punt_check`

### 44.6 Lab Sovereignty enforcement

The MCP server enforces the Lab Sovereignty Rule (PRD §40.11) **at the protocol boundary**. Cross-lab write tools (e.g. `experiment_dispatch` for a lab the agent doesn't own) are rejected before the underlying REST call is made. Every tool has a `cross_lab_policy` field set to `NEVER_ALLOWED` for write operations.

### 44.7 Constraints (protocol-layer invariants)

The YAML lock (`mcp-server-spec.yaml`) includes a `constraints` section that enforces:
- N4 contributions (Flagship-level breakthrough) **cannot** be claimed by an agent — only Houston can stamp N4
- The `notechat` tool requires `explicit_user_consent: true` — agents NEVER auto-save chats to Notes

### 44.8 Audit logging

Every MCP tool call writes to `lab/audit/mcp-<agent>.jsonl` (append-only, included in the nightly Backblaze backup). This is the agent equivalent of the API access log.

### 44.9 Linked files

- Human spec: `project-context/MCP_SERVER_SPEC.md` (commit `0546d5d`)
- Machine spec: `project-context/mcp-server-spec.yaml` (commit `19917e0`)

---

## 45. CLI Spec — `hubify` (the terminal client)

**Status:** Locked 2026-04-08. Human-readable spec in `project-context/CLI_SPEC.md` (~700 lines, commit `c7804a0`). Machine-readable contract in `project-context/cli-spec.yaml` (commit `378b58a`).

### 45.0 Why this section exists

Houston lives in the terminal. The CLI is **how he drives Hubify Labs without leaving his shell**. It's a thin client over the REST API + MCP server, plus an interactive TUI mode.

### 45.1 Decision: Go + Cobra + bubbletea

DECISION: Go (single static binary, ~10ms startup, easy distribution via Homebrew).
Framework: Cobra for the command tree, bubbletea for the TUI mode.

Rejected:
- **Node.js / TypeScript** — slower startup, requires a runtime, harder distribution
- **Python** — same problems plus dependency hell
- **Rust** — great choice but Cobra in Go is more mature than Clap in Rust for our needs

### 45.2 Command structure

**~120 commands across 19 categories** (full list in CLI_SPEC.md §1):

lab · project · experiment (with §41 routing) · pipeline · chat · note · pod/compute · agent · memory · standup · costs · backup · cross-lab comms · search · MCP server · auth · config · status · TUI

Pattern: `hubify <noun> <verb> [args] [flags]` — the `gh` (GitHub CLI) convention.

### 45.3 PRD §41 routing enforcement

The `hubify experiment dispatch` command **refuses to dispatch** without `--gpu` or `--cpu`. Exits with code 22 ("PRD §41 routing violation") and a message pointing at the relevant PRD section. This is the CLI-layer enforcement of the routing rule (the API and MCP server enforce the same rule independently).

### 45.4 TUI mode

`hubify` with no args opens an interactive bubbletea-based TUI mirroring the web views (Director, Experiments, Papers, Agents, Compute). Keyboard: ⌘1-9 for views, `/` for search, `?` for help.

For users who want to live entirely in the terminal — no browser at all. Houston specifically asked for this in PRD §30 ("hubify CLI in terminal — auto-launches 4 sessions").

### 45.5 Auth

- **Browser-based OAuth (PKCE, RFC 7636)** — default
- **Service tokens** via `HUBIFY_TOKEN` env var — for CI / cron / headless
- **Token storage** in `~/.hubify/credentials` (mode 0600), with optional Keychain / libsecret / Credential Manager integration
- **Profile switching** via `--profile` flag or `HUBIFY_PROFILE` env var

### 45.6 Output formats

Every command supports `--format text|json|yaml|table|tsv`. Auto-disables colors and progress bars when stdout is not a TTY.

### 45.7 Distribution

- Homebrew tap (`Hubify-Labs/homebrew-tap`)
- Direct install: `curl -fsSL https://hubify-labs.com/install.sh | sh`
- GitHub releases (Universal macOS, Linux x86_64 + arm64, Windows)

### 45.8 Plugin system (DEFERRED to v1.1)

v1.0 ships compact and curated. The plugin system arrives in v1.1. Plugins will follow the `gh extensions` pattern (Go binaries in `~/.hubify/plugins/` invoked as subcommands).

### 45.9 Linked files

- Human spec: `project-context/CLI_SPEC.md` (commit `c7804a0`)
- Machine spec: `project-context/cli-spec.yaml` (commit `378b58a`)

---

## 46. Deployment Infrastructure Plan

**Status:** Locked 2026-04-08. Full plan in `project-context/DEPLOYMENT_INFRA_PLAN.md` (~750 lines, commit `2e5f3e6`, expanded by `6eb362b` and `d5999d5`).

### 46.0 Why this section exists

Going from "code on disk" to "live MVP at hubify-labs.com" requires explicit decisions about every layer of infrastructure: hosting, database, orchestrator, compute, backups, DNS, CI/CD, monitoring. This section is the PRD-resident summary; the canonical plan with cost forecasts and runbooks lives in DEPLOYMENT_INFRA_PLAN.md.

### 46.1 The infrastructure stack

| Layer | Provider | Type | Notes |
|---|---|---|---|
| Web hosting | **Vercel** | Type A platform `hubify-labs.com` + Type B per-lab `<lab>.hubify.app` | DEPLOYMENT_INFRA_PLAN §2.1 |
| Backend | **Convex** | 3 envs (dev / staging / prod) | §2.2 |
| Orchestrator | **Fly.io** | 1 shared-CPU machine per active lab, ~$2-5/mo each | §2.3 + §2.3.1 (4 surfaces) + §2.3.2 (chat→action) |
| Compute | **RunPod** | Pods + Serverless, GPU + CPU variants | §2.4 (per PRD §24, §41) |
| Backups | **Backblaze B2** | Cold storage, nightly + pre-credits-out + on-demand | §2.5 |
| Code | **GitHub `Hubify-Labs` org** | One repo per lab (PRD §1 lock) + GitHub Actions for CI/CD | §2.7 |
| DNS | **Cloudflare** | Wildcard `*.hubify.app` for per-lab subdomains | §2.8 |
| SSL | **Let's Encrypt** auto-provisioned via Vercel + Convex | §2.9 |
| Monitoring | **Sentry** (errors) + **Vercel Analytics** (perf) + **Better Uptime** + custom Convex dashboards + **ntfy.sh** (phone push) + **Slack** (team) | §2.10 |
| Email | TBD (likely Postmark or Resend for transactional) | §2.11 |

### 46.2 The Fly.io 4-surface model (DEPLOYMENT_INFRA_PLAN §2.3.1)

How the Fly machine integrates into the Hubify Labs UI:

1. **In-app sidepeek inspector** — a `runtime` sidepeek in Settings · Compute & Runtime that shows the Fly machine status, recent commands, output stream
2. **Terminal pane stream** — the embedded terminal panel can stream the Fly orchestrator's output in real time
3. **Out-of-band admin URL** — `https://orchestrator-<lab-slug>.fly.dev/` for direct admin access (auth-gated)
4. **CLI** — `hubify pod ssh` and `hubify mcp serve` both work against the Fly machine

### 46.3 Migration plan reference

Lab #1 (Bounce Cosmology) migration from the existing `bigbounce.hubify.app` site to a Hubify Labs lab is fully spec'd in `project-context/MIGRATION_BOUNCE_COSMOLOGY_LAB.md` (~1500 lines). 9 executable steps + risk register + post-migration roadmap.

### 46.4 Cost forecast

DEPLOYMENT_INFRA_PLAN §6 has the full cost forecast at v1 (~$40-60/month) and at 100-user scale (~$300-500/month). Compute (RunPod) is the dominant variable, everything else is fixed-cost.

### 46.5 Linked file

Full plan: `project-context/DEPLOYMENT_INFRA_PLAN.md` (commit `2e5f3e6`).

---

## 47. Mintlify Docs Port — Public Documentation Site

**Status:** Locked 2026-04-08. Expansion of §40.17 Tier 3 (the public docs subpath plan).

### 47.0 Why this section exists

Hubify Labs needs a **public documentation site** that mirrors the existing `hubify.com/docs` Mintlify pattern. The docs site is the **first thing a new user sees** before signing up — it must explain what Hubify Labs is, how the 5-level hierarchy works, what the agents do, how to get started, and how to use the CLI / API / MCP server.

### 47.1 Decision: Mintlify (matches existing Hubify Labs pattern)

DECISION: Mintlify, hosted at `hubify-labs.com/docs` (subpath, NOT subdomain — keeps everything on one domain for SEO + cross-linking simplicity).

Rejected:
- **Docusaurus** — heavier, more setup, less polished out of the box
- **VitePress** — great but smaller ecosystem
- **Custom Astro/Next.js docs** — too much work for v1
- **GitBook** — vendor lock-in
- **`docs.hubify-labs.com` subdomain** — fragments the domain authority

### 47.2 The first 7 docs pages (v1 launch set)

1. **`/docs`** — Welcome + 1-paragraph "what is Hubify Labs"
2. **`/docs/quickstart`** — 5-minute quickstart: signup → create lab → first chat → first experiment
3. **`/docs/concepts/hierarchy`** — The 5-level taxonomy (Lab → Project → Pipeline → Experiment → Task) with the chat-as-intent-layer explanation (PRD §40)
4. **`/docs/concepts/agents`** — The 21 agents, the lead/orchestrator pattern, the 10-tab agent inspector (PRD §3 + §34)
5. **`/docs/concepts/compute`** — How RunPod routing works (CPU/GPU + Pod/Serverless), credits, the 4-tier alert system (PRD §24 + §41)
6. **`/docs/api`** — API reference auto-generated from `api-spec.openapi.yaml`
7. **`/docs/cli`** — CLI reference auto-generated from `cli-spec.yaml`

### 47.3 Codegen pipeline

The API + CLI reference pages are **auto-generated** from the OpenAPI YAML and the cli-spec YAML on every commit to `main`. GitHub Actions workflow:
1. Read `api-spec.openapi.yaml` → run `mintlify-openapi` → write to `docs/api/`
2. Read `cli-spec.yaml` → run a custom Go script → write to `docs/cli/`
3. Commit changes back to `docs/` if non-empty
4. Mintlify auto-deploys on the commit

This guarantees the docs **never drift** from the spec.

### 47.4 Search + AI assistant

Mintlify ships with:
- **Algolia DocSearch** for full-text search (free for OSS)
- **AI assistant** (Mintlify's built-in, powered by GPT-4) for "ask a question about the docs"

Both are enabled in `mintlify.json` from day 1.

### 47.5 Linked planning

- The full Mintlify replication plan is referenced in PRD §40.17 Tier 3
- The doc page outlines + naming conventions live in `project-context/MINTLIFY_PORT_PLAN.md` (TBD — to be written when the docs port begins)

---

## 48. `hubify://` URL Scheme — The Universal Deep-Link Catalog

**Status:** Locked 2026-04-08. Companion to §40.17 Tier 4 (the URL scheme tier).

### 48.0 Why this section exists

Hubify Labs spans **many surfaces** (web · macOS app · iOS web · CLI · MCP server · Slack messages · Mintlify docs). Every surface needs a way to **deep-link** into a specific entity (a paper, an experiment, a chat, a memory entry). The `hubify://` URL scheme is the universal address.

### 48.1 The pattern

```
hubify://<lab-slug>/<entity-type>/<entity-id>[?<query-params>]
```

- **`<lab-slug>`** — kebab-case slug of the lab (e.g., `bigbounce-hubify`, `dark-energy`)
- **`<entity-type>`** — one of the 19 entity types (see §48.2)
- **`<entity-id>`** — the entity's stable identifier (UUID, slug, or numeric ID depending on type)
- **`<query-params>`** — optional view-state (e.g., `?tab=skills`, `?line=42`, `?range=2026-04-01..2026-04-08`)

### 48.2 The 19 entity types

| Entity type | URL pattern example | Opens in |
|---|---|---|
| `lab` | `hubify://bigbounce-hubify/lab` | Director view |
| `project` | `hubify://bigbounce-hubify/project/p_42` | Project Overview sidepeek |
| `pipeline` | `hubify://bigbounce-hubify/pipeline/pl_7` | Pipeline detail view |
| `experiment` | `hubify://bigbounce-hubify/experiment/exp_2401` | Experiment sidepeek |
| `task` | `hubify://bigbounce-hubify/task/t_88` | Task sidepeek |
| `chat` | `hubify://bigbounce-hubify/chat/ch_19?tab=history` | Chat history sidepeek |
| `paper` | `hubify://bigbounce-hubify/paper/spin-torsion-v2` | Paper sidepeek (PDF mode) |
| `note` | `hubify://bigbounce-hubify/note/2026-04-08-daily.md` | Notes view, file open |
| `agent` | `hubify://bigbounce-hubify/agent/orchestrator?tab=learnings` | Agent 10-tab sidepeek |
| `memory` | `hubify://bigbounce-hubify/memory/m_551` | Memory inspector sidepeek |
| `contribution` | `hubify://bigbounce-hubify/contribution/c_104` | Contribution sidepeek (with N-score) |
| `dataset` | `hubify://bigbounce-hubify/dataset/desi-dr1` | Dataset sidepeek (schema + sample rows) |
| `figure` | `hubify://bigbounce-hubify/figure/fig_22` | Figure sidepeek |
| `survey` | `hubify://bigbounce-hubify/survey/sdss-dr18` | Survey sidepeek |
| `pod` | `hubify://bigbounce-hubify/pod/o76k3jfzbfh25e` | Compute view, pod expanded |
| `comm` | `hubify://bigbounce-hubify/comm/cm_7` | Comm sidepeek |
| `standup` | `hubify://bigbounce-hubify/standup/2026-04-08-morning` | Standup transcript sidepeek |
| `routine` | `hubify://bigbounce-hubify/routine/credits-watchdog` | Routine sidepeek |
| `runtime` | `hubify://bigbounce-hubify/runtime/fly` | Runtime inspector sidepeek (3 variants: macos / fly / mcp) |

### 48.3 Cross-lab references

Cross-lab links work the same way — the URL just points at a different lab slug:

```
hubify://dark-energy/paper/quintom-fnl-forecast
hubify://bigbounce-hubify/experiment/exp_2401
```

The receiving surface checks read-permission against the Lab Sovereignty Rule. If the user has read access (or the lab is `public_visibility: published-only`), the link opens. If not, the surface shows a "this lab is private" error with a request-access button.

**Cross-lab WRITE links are explicitly forbidden** — there is no `hubify://<other-lab>/experiment/dispatch?...` URL. Writes always go through the comm-message gateway (PRD §40.11).

### 48.4 Surface-specific handling

| Surface | How it handles `hubify://` |
|---|---|
| **macOS app** (Tauri) | Registered in `Info.plist` as a URL scheme handler. macOS routes all `hubify://` clicks to the app, which then routes internally to the right view |
| **Web app** | `https://hubify-labs.com/open?url=hubify://...` redirects to the in-app handler |
| **iOS web** (Safari) | Universal links: `https://hubify-labs.com/u/<lab>/<entity>/<id>` is registered as a universal link, opens the web app in Safari |
| **CLI** | `hubify open <hubify://...>` resolves the URL and either prints the entity to stdout or opens the web app in a browser (`--browser` flag) |
| **MCP server** | Returns `hubify://` URLs in tool responses; the MCP client (e.g., Claude Code) is responsible for handling them |
| **Slack / Discord** | The Hubify Labs Slack bot unfurls `hubify://` URLs into rich previews with the entity title + status |
| **Mintlify docs** | Doc pages can link to `hubify://` URLs for cross-references between docs and the live app |

### 48.5 Versioning

The URL scheme is **stable forever**. Once an entity gets a `hubify://` URL, that URL never changes — even if the underlying entity is renamed, archived, or moved between projects. Old IDs remain resolvable (with a redirect to the new location if applicable).

### 48.6 Open questions

1. **Short-link service?** — Should `hubify://` URLs have a short-link form (e.g., `hubify://bb/e/2401`)? Defer to v1.1 unless there's a compelling Slack/Discord pasting use case.
2. **Deep-link analytics** — Should we track which `hubify://` URLs are clicked, from which surface? Answer: yes, but anonymized — telemetry handled in §50.

---

## 49. Authentication & Authorization Spec

**Status:** Locked 2026-04-08. The single source of truth for who can do what across all surfaces.

### 49.0 Why this section exists

Hubify Labs has many actors (users, agents, service tokens, cron jobs) and many resources (labs, projects, experiments, files). Without explicit auth + authz rules, the platform leaks information across labs (Lab Sovereignty Rule violation), allows agents to make irreversible changes without consent, or accidentally exposes private data to public users.

### 49.1 Authentication providers

| Provider | When used | Token format |
|---|---|---|
| **GitHub OAuth** | Default for human users; gives the platform GitHub repo write access for the lab=repo architecture (PRD §1) | `hbf_user_eyJ...` (JWT HS256) |
| **Email magic link** | Fallback for users without GitHub | `hbf_user_eyJ...` (JWT HS256) |
| **Service tokens** | CI / cron / headless agents | `hbf_st_...` (HMAC-signed, no JWT envelope) |
| **Agent tokens** | Per-agent, per-lab, issued by the orchestrator on first agent boot | `hbf_agent_eyJ...` (JWT HS256, very short lived: 1 hour with auto-renew) |
| **MCP client auth** | The MCP server asks the client to authenticate via OAuth at first connection (Anthropic's MCP auth pattern) | `hbf_mcp_eyJ...` (JWT HS256, lab-scoped) |

### 49.2 Token types and lifetimes

| Token type | Issued by | Lifetime | Refreshable | Stored where |
|---|---|---|---|---|
| `user` | OAuth callback | 24h | Yes (refresh token, 30d) | `~/.hubify/credentials` (CLI) · cookie (web) · keychain (desktop app) |
| `agent` | Orchestrator | 1h | Yes (auto, no refresh token needed) | Agent's process memory only — never on disk |
| `service` | User-issued via `hubify auth tokens create` | 90d | No (must rotate) | User-managed (env var, CI secrets) |
| `mcp` | OAuth callback at MCP connect | 1h | Yes | MCP client's process memory |

### 49.3 Per-lab scope

Every token carries a `labs` claim listing which labs the token has read/write access to. Cross-lab access is **always explicit** — there's no "global admin" token (with one exception: Houston's super-admin token, which exists for emergency recovery only).

```json
{
  "sub": "houston@hubify.com",
  "labs": [
    {"slug": "bigbounce-hubify", "perms": ["read", "write"]},
    {"slug": "dark-energy", "perms": ["read", "write"]},
    {"slug": "dark-matter", "perms": ["read"]}
  ],
  "exp": 1735689600,
  "iss": "https://hubify-labs.com",
  "aud": "https://api.hubify-labs.com"
}
```

### 49.4 The Lab Sovereignty Rule (PRD §40.11) — auth-layer enforcement

Cross-lab WRITE attempts are rejected at **THREE independent layers**:

1. **CLI layer** — `cli-spec.yaml` `cross_lab_rules` validation rejects before sending the HTTP request (exit code 24)
2. **MCP server layer** — `mcp-server-spec.yaml` `cross_lab_policy: NEVER_ALLOWED` for write tools rejects before the underlying API call
3. **API layer** — `api-spec.openapi.yaml` returns **403 with `type: cross-lab-write-denied`** if a request reaches the handler with a token that lacks write permission for the target lab

The triple enforcement is **deliberately redundant** — if any layer is bypassed (e.g. a malicious MCP client hits the API directly), the next layer catches it.

### 49.5 Agent consent boundaries

Some actions REQUIRE explicit user consent (an agent cannot do them autonomously even if its token has write permission):

| Action | Consent reason | Enforcement |
|---|---|---|
| **N4 contribution claim** | "Flagship-level breakthrough" — only Houston can stamp this; agents cap at N3 | `mcp-server-spec.yaml` constraints array |
| **Save chat to Notes** | The Notes file is the user's personal journal; agents don't get write access without per-call consent | `requires_explicit_user_consent: true` on the `notechat` tool |
| **Public lab visibility flip** | Privacy-sensitive change | API returns 403 for non-user tokens |
| **Delete a lab** | Irreversible (30d soft delete, but still) | API requires `user` token type, not `agent` or `service` |
| **Issue a new service token** | Auth-sensitive | API requires `user` token type |
| **Change auth provider settings** | Auth-sensitive | API requires `user` token type |

### 49.6 Audit logging

Every write action (across all surfaces) writes to `lab/audit/access.jsonl`:

```jsonl
{"ts":"2026-04-08T23:14:00Z","actor":"agent:orchestrator","action":"experiment.dispatch","lab":"bigbounce-hubify","resource":"exp_2401","result":"success","token_type":"agent","ip":null}
{"ts":"2026-04-08T23:14:30Z","actor":"user:houston@hubify.com","action":"note.create","lab":"bigbounce-hubify","resource":"2026-04-08-daily.md","result":"success","token_type":"user","ip":"192.0.2.42"}
```

The audit log is included in the nightly Backblaze backup. It is the source of truth for "who did what when" investigations.

### 49.7 Rate limits (per token type)

| Token type | Read endpoints | Write endpoints | Search endpoints |
|---|---|---|---|
| `user` | 1000/min | 100/min | 30/min |
| `agent` | 5000/min | 500/min | 100/min |
| `service` | 10000/min | 1000/min | 200/min |

Per-endpoint overrides (e.g., experiment dispatch is 10/min regardless of token type, to prevent runaway agents from burning the credits balance).

---

## 50. Telemetry & Observability Spec

**Status:** Locked 2026-04-08. Companion to DEPLOYMENT_INFRA_PLAN §2.10 (monitoring stack).

### 50.0 Why this section exists

To operate Hubify Labs reliably, we need to know:
- **What's happening** (live activity feed, comms inbox, current experiments)
- **What broke** (errors, slow endpoints, failed dispatches)
- **Who's spending what** (compute costs per lab, per experiment, per provider)
- **What users are doing** (which views are used, where users get stuck)

This section catalogs every event the platform emits, where it goes, how long it's retained, and what privacy guarantees apply.

### 50.1 Event categories

| Category | Examples | Destination | Retention |
|---|---|---|---|
| **Errors** | Uncaught exceptions, 500s, panicked agents | Sentry | 90 days |
| **Performance** | Endpoint latency, page TTI, API request volume | Vercel Analytics + custom Convex dashboards | 30 days |
| **Uptime** | Health-check pings to public surfaces | Better Uptime | 12 months |
| **Audit** | Every write action across the platform | `lab/audit/access.jsonl` (per-lab), backed up nightly | Forever (lab data) |
| **Cost** | Per-experiment GPU-hours, per-call LLM token spend, daily totals | Convex `costs` table + nightly aggregation | 12 months |
| **Activity** | Agent actions, Houston actions, system events | Convex `activity` table (drives the activity feed sidebar) | 90 days |
| **Standups** | Morning/midday/evening agent transcripts | Convex `standups` table | 12 months |
| **Telemetry (anonymized)** | Page views, click events, view-switch events | Convex `telemetry` table | 90 days |
| **Crash reports** | Tauri desktop app crashes | Sentry (separate project) | 90 days |

### 50.2 Privacy boundaries

| Class | Stored? | Sent to 3rd parties? | Notes |
|---|---|---|---|
| User email + name | Yes (Convex `users` table) | Sentry (for crash attribution, opt-in) | Required for auth |
| Lab content (experiments, papers, notes, chats) | Yes (Convex per-lab tables) | NEVER | Lab data is sovereign |
| Memory entries | Yes (Convex `memory` table, layered) | NEVER | Memory is sovereign |
| Audit logs | Yes (per-lab JSONL files + Convex) | NEVER | Lab data is sovereign |
| Telemetry (anonymized) | Yes (Convex `telemetry` table, no PII) | Aggregate counters only, no per-user data | For platform improvement |
| Crash reports | Yes (Sentry) | Sentry (the whole point) | User can opt out via settings |

**Lab content NEVER leaves the user's Convex deployment.** The only thing that goes to 3rd parties is anonymized telemetry, error stack traces (Sentry, opt-in), and uptime pings (Better Uptime, no payload).

### 50.3 The activity feed (PRD §39)

Every event in the `activity` category writes to the Convex `activity` table, which powers:
- The sidebar activity feed in the web app
- The morning standup ("here's what happened overnight")
- The Activity Graph view (the neural-brain visualization)
- The desktop app dock badge counter
- ntfy.sh phone push for high-priority events

Schema (simplified):

```typescript
{
  id: string,
  lab: string,
  ts: timestamp,
  actor: { type: "user" | "agent" | "system", id: string },
  action: string,  // e.g., "experiment.dispatched", "paper.published", "credits.warn"
  entity: { type: string, id: string },  // e.g., { type: "experiment", id: "exp_2401" }
  payload: object,  // action-specific
  priority: "low" | "normal" | "high" | "critical"
}
```

### 50.4 Cost tracking (PRD §41)

Per-experiment cost is tracked **in real time** by the orchestrator:

```typescript
{
  experiment_id: "exp_2401",
  lab: "bigbounce-hubify",
  start_ts: "2026-04-08T22:00:00Z",
  end_ts: "2026-04-08T23:30:00Z",
  duration_min: 90,
  compute_mode: "gpu_pod",  // gpu_pod | gpu_serverless | cpu_pod | cpu_serverless
  gpu_type: "H200",
  cost_usd: 6.00,
  cost_breakdown: {
    runpod_gpu: 5.40,
    runpod_storage: 0.10,
    anthropic_tokens: 0.30,
    openai_embeddings: 0.20
  }
}
```

The Costs view in the web app reads from this table, grouped by day / week / month / per-provider / per-experiment.

### 50.5 Alert routing (PRD §41.2 + DEPLOYMENT_INFRA_PLAN §2.10)

| Alert type | Severity | Channel | Throttle |
|---|---|---|---|
| Credits HIGH (default) | low | activity feed only | n/a |
| Credits WARN | medium | Slack | 1/hour |
| Credits CRIT | high | Slack + ntfy.sh push | 1/15min |
| Credits EMERGENCY | critical | Slack + ntfy.sh push + email + auto-shutdown | immediate, no throttle |
| Pod idle > 30min | medium | Slack + activity feed | 1/15min |
| Experiment failed | medium | Slack | 1/min |
| Auth attempt failed (5×) | high | Slack + email | 1/hour |
| Agent stuck (no output > 10min) | high | Slack | 1/15min |

### 50.6 Telemetry opt-out

Every user can opt out of anonymized telemetry via Settings → Privacy → "Send anonymous usage data". When disabled:
- Telemetry events are NOT written to the `telemetry` table
- Sentry crash reports are NOT sent (if also disabled)
- All other categories (errors, audit, cost) continue normally — those are operational, not analytics

The opt-out is **per-user, not per-lab**. Lab data remains sovereign regardless.

### 50.7 Open questions

1. **PostHog vs custom Convex dashboards for product analytics?** — currently planning custom Convex dashboards (no 3rd-party data sharing). Re-evaluate if we need funnel analysis at scale.
2. **Anonymized telemetry — opt-in or opt-out by default?** — current default is opt-in disabled (privacy-first). Re-evaluate after launch if we need usage data to make product decisions.
3. **Crash report scrubbing** — what fields in a stack trace might leak PII? Need a scrubbing pass before sending to Sentry. Sentry has a built-in `before_send` hook for this.

---

## 51. Marketing Site Spec — `hubify-labs.com` Public Pages

**Status:** Locked 2026-04-09 by Houston after the "I can see how it will all come together" milestone. The marketing site is the **public-facing front-end** of Hubify Labs — what visitors see before they sign up. Distinct from the in-app research IDE (which lives at `app.hubify-labs.com` or per-lab subdomains like `bigbounce.hubify.app`).

### 51.0 Why this section exists

The platform needs a clear public face that:
1. **Pitches the value** in 5 seconds (above the fold)
2. **Explains the 4-stack architecture** (Web/Desktop/CLI/Fly) elegantly — the "brain that doesn't blink" story
3. **Showcases real labs** — community gallery with detail pages, "view lab site" + "remix this lab" buttons (the vibe-coding-app showcase pattern applied to research)
4. **Drives urgency** via the **Window 2025-2027** essay — explains why independent researchers should act NOW
5. **Builds the brand + SEO/AEO** through guides, blog, and docs

### 51.1 Pages to ship in v1

| Page | Path | Purpose | Length |
|---|---|---|---|
| Homepage | `/` | Pitch · 4-stack architecture · Window urgency · lab gallery preview · how it works · CTA | ~6 sections, scannable |
| Features | `/features` | Full feature deep-dive · 14 sections · long-form | full-length, robust |
| Labs gallery | `/labs` | Browse community labs · filter chips · search · 8-10 lab cards | grid view |
| Lab detail | `/labs/<slug>` | Per-lab page · screenshot + mission + papers + contributions + remix button | 1 per lab |
| Docs | `/docs` | Mintlify-style docs landing · search + sidebar nav | starter set, 7 pages per §47 |
| Guides | `/guides` | Step-by-step tutorials · 6-8 cards | grid view |
| Blog | `/blog` | Houston's articles · featured + recent posts | grid view |
| Blog post | `/blog/<slug>` | Individual article · long-form essay layout | 1 per post |
| Pricing | `/pricing` | (DEFERRED to v1.1) | — |

### 51.2 Homepage layout (the elevator pitch in 7 sections — corrected 2026-04-09)

1. **Hero** — Above-the-fold pitch. H1 + sub + 2 CTAs (Get started · View live demo) + small **3-surface diagram** (Web · Desktop · CLI) + live BigBounce counter ("53 experiments · 4 papers · 328K anomalies · 16 contributions · day 218 active")
2. **The Window 2025-2027 urgency band** — Quote/excerpt from the Houston essay + "Read the full essay →" link
3. **Surfaces · How you use it** — "Three surfaces. Same lab." 3 horizontal cards (Web app · Desktop app · CLI/TUI) — each is the FULL research IDE. Not 4 cards. Fly+RunPod are NOT in this section.
4. **What you get with a Lab** — "A Lab is the unit." 6 cards (21 agents pre-wired · always-on GPU/CPU scale · public lab site · paper generation pipeline · 4-layer memory · 24/7 orchestrator). This is where Fly + RunPod show up, as infrastructure.
5. **Lab gallery preview** — "What labs look like · community showcase" — 4 sample lab cards + "Explore all labs →" link
6. **How it works** — 3 steps: Create lab → Talk to orchestrator → Watch lab grow
7. **Footer CTA** — Big sage button + signup + "Or try the live demo →"

### 51.3 Surfaces vs What You Get — the corrected framing (Houston 2026-04-09)

**Earlier framing was wrong.** I conflated two different concepts into a "4-stack architecture" (Local Mac / Web / Fly / RunPod). Houston corrected this — they're TWO separate concepts that need to be presented as separate sections on the marketing site.

**Concept 1 · Surfaces · How you use Hubify Labs**

Three equivalent surfaces. Each is the FULL research IDE — you can do anything in any of them. They stay in sync via the always-on infrastructure underneath.

| Surface | What it is | Tag |
|---|---|---|
| **Web app** | Full research IDE in the browser (the `index.html` mockup). No install. Open in any browser. | `full IDE in the browser` |
| **Desktop app** | Full research IDE as a native macOS app. File drop, menu bar, dock badge, system notifications, hubify:// deep links. | `full IDE · native macOS` (NEVER call this "Tauri" in user-facing copy — Tauri is the implementation framework) |
| **CLI · TUI** | Full research lab in your terminal. `hubify` Go binary, ~120 commands, bubbletea TUI mirror of the web views. | `terminal-native · ~120 commands` |

The pitch: your laptop dies and you pick up on the web app on your phone, or jump into the CLI on a friend's machine. The work doesn't care which window you're in.

**Concept 2 · What You Get with a Lab**

Every Hubify Labs account starts with one Lab — your own containerized research environment with the agents, the compute, the public site, and the publishing pipeline already wired up. You're not assembling a stack — you're picking up a working lab.

| Capability | What it includes |
|---|---|
| **21 agents pre-wired** | Orchestrator (Opus 4.6) + 4 leads + 11 workers + 4 cross-provider reviewers (GPT-5 · Gemini 2.5 · Sonnet skeptic · Perplexity). All running, all auditable. |
| **Always-on GPU/CPU scale** | RunPod GPU pods + serverless on demand. The §41 router picks the cheapest credible target per job. Live credit monitoring + 4-tier alerts. You never log into RunPod directly. |
| **Public lab site** | Your lab's own subdomain (e.g. `bigbounce.hubify.app`) — auto-generated from your papers, figures, datasets, and contributions. What the world sees when they search your work. |
| **Paper generation pipeline** | Publish-ready loop: 5-round autonomous publishing with mechanical QA, cross-model peer review, Houston Method audit, final visual pass, and arXiv package. |
| **4-layer memory** | User · agent · lab · global. Agents read the right scope automatically. |
| **24/7 orchestrator** | Always-on Fly.io machine runs your lab while you sleep. Cron jobs every 5 min, standups 3x/day, idle-GPU watchdog, publish-ready loop overnight. |
| Plus the rest of PRD §3-50 | Standups · routines · backups · cross-lab comms · Activity Graph · MCP server · vibe coding sandbox · etc. |

**Why this framing matters:**

The earlier conflation made it look like "Web" was just the public face / lab site. Houston pointed out that's wrong — the Web app IS the full IDE, and the public lab site is a SEPARATE thing (it's part of "what you get with a Lab," not a surface for interacting with the platform). Same way Cursor is "the IDE in your browser/desktop" — not "the public face."

**Terminology rules:**
- **Always say** "Web app" / "Desktop app" / "CLI · TUI" — these are the 3 surfaces
- **Never say** "Tauri" in user-facing copy (it's the implementation framework, not the product)
- **Never say** "Vercel is the public face" — Vercel hosts the public lab site, but the public lab site is one of the things you GET, not a surface
- **Fly + RunPod** are infrastructure underneath the surfaces, not surfaces themselves. They appear in "What You Get" (24/7 orchestrator + GPU scale), not in the surfaces section.

### 51.4 Lab gallery — the vibe-coding-app showcase pattern applied to research

The Lab gallery is **central to the marketing motion**. It's the equivalent of how Vercel/Replit/Lovable show off community-generated sites. For Hubify Labs, we showcase real research labs.

**Each lab in the gallery has:**
- Cover image (hero render of the lab's Director view OR a custom uploaded banner)
- Lab name + owner handle (`@username`)
- 1-line mission
- Stats: papers count, experiments count, contributions count, day-since-created
- Status pills: `public` · `remixable` · `featured` (optional)

**Lab detail page** (`/labs/<slug>`):
- Hero banner with lab name + owner handle + 2 CTAs in the top right:
  1. **View lab site →** (links to the lab's actual public site, e.g. `bigbounce.hubify.app`)
  2. **Remix this lab →** (clones the lab's structure to the visitor's account, only shown if owner has enabled remixing)
- Large screenshot of the actual lab Director view
- Mission statement (1-2 paragraphs from the owner)
- Key discoveries (3-5 bullet contributions with N-scores)
- Papers section (clickable rows linking to arXiv-style URLs)
- Stats grid (experiments / papers / GPU hours / agents / day-since-created)
- Recent activity timeline
- Owner profile card

**Remix flow:** clicking "Remix this lab" creates a new lab in the visitor's account scaffolded with:
- The same project structure (projects, pipelines, agent roster)
- The same template files (paper templates, figure templates, wiki entries)
- A blank experiments + chats history (no data leaks across the boundary)
- A note in the new lab's README: "Cloned from `<original-lab>` by `<owner>` on <date>"

**The Lab Sovereignty Rule still applies** (PRD §40.11): clones are independent labs, not forks. The original lab's data remains private to the original owner.

### 51.5 The Window 2025-2027 article

Houston is writing this essay. The thesis (paraphrased from his message):

> There's a window between 2025 and 2027 where independent researchers can do work that the big AI labs and university groups can't, because the AI tooling is good enough to give a single person a leverage multiplier of 50-100x but the platforms haven't yet been captured by the big players. After 2027, the moats start closing. If you're going to do independent research that competes with institutions, the time is now.

The article should live at `/blog/the-window-2025-2027`. It's the canonical urgency essay and gets featured on the homepage urgency band.

Other blog posts to seed the blog (Houston will write these):
- "Why Fly.io is the brain that doesn't blink"
- "Houston Method v2: post-experiment rituals that scale"
- "Building a research lab without a PhD lab"
- "f_NL = -35/8: a parameter-free prediction from matter bounce" (cross-link to BigBounce paper)
- "Cross-model peer review: avoiding the AI echo chamber"

### 51.6 Features page — full deep-dive (14 sections)

The Features page is intentionally LONG (Houston explicitly said "full length robust beautifully designed elegant on brand"). One section per major capability:

1. The 4-surface architecture (full vertical diagram)
2. AI-native experiment dispatch (PRD §41 routing)
3. Always-on orchestrator (Fly.io cron + standups + watchdog)
4. Lab Sovereignty Rule (read-OK, write-FORBIDDEN, triple-enforced)
5. Cross-model peer review (no echo chamber)
6. Houston Method v2 post-experiment ritual
7. The hierarchy (Lab → Project → Pipeline → Experiment → Task)
8. Memory architecture (4-layer)
9. Publish-ready loop (autonomous 5-round, no future-research punts)
10. Vibe coding sandbox (Vercel Sandbox)
11. Activity Graph (neural-brain view)
12. Cross-lab comm gateway
13. MCP server (agents drive the platform)
14. CLI + TUI (`hubify` Go binary)

### 51.7 Docs / Guides / Blog (the SEO/AEO foundation)

- **Docs**: Mintlify subpath at `hubify-labs.com/docs` (per PRD §47). Auto-generated API/CLI reference from the YAML specs. 7 starter pages.
- **Guides**: 6-8 step-by-step tutorials covering common workflows (migrate research, set up peer review, configure §41, build a Lab template, etc.)
- **Blog**: Houston's authored articles. Featured post on top, recent grid below.

### 51.8 Tech stack for the marketing site

- **Next.js 15** App Router (separate from the in-app web mockup which is a single-file demo)
- **Vercel** for hosting (free tier, auto-deploy from main)
- **MDX** for blog posts and guides
- **Mintlify** for `/docs` subpath
- **Same design system** as the in-app: dark theme, sage discipline, Cursor-style minimalism. CSS variables shared via a `tokens.css`.
- **Lab gallery data** comes from a Convex `public_labs` table (read-only public view, populated by labs with `visibility: public` set in their `lab.yaml`)

### 51.9 Mockup file

The marketing site mockup lives at `hubify-labs-mockups/marketing-site-mockup.html` — a single self-contained HTML file (same pattern as `desktop-app-mockup.html` and `cli-tui-mockup.html`). All 7 pages navigable via top nav. Sage discipline preserved.

### 51.10 What the marketing site is NOT

- It's NOT the in-app research IDE (that lives at `app.hubify-labs.com` or the per-lab subdomain)
- It does NOT host any private lab data (only public showcase data)
- It does NOT have any chat/agent functionality (those live in the in-app)
- It is NOT auto-generated from the YAML specs (only the docs section is)

---

## 52. Competitive Frame — K-Dense + Feynman + the AI research agent landscape

**Status:** Locked 2026-04-09 · Houston flagged multiple competitors.
**Full reference:** `project-context/COMPETITIVE_ANALYSIS.md` (renamed from K-Dense-only)
**Memory:** `feedback_kdense_competitor.md`
**Competitors covered:** K-Dense AI (closest by vision · web-only · 250+ DBs) · Feynman (open-source CLI-first · multi-agent · cite-every-claim · built on Pi+alphaXiv)
**Reference repos to audit:** `K-Dense-AI/claude-scientific-skills`, `K-Dense-AI/claude-scientific-writer`, `K-Dense-AI/k-dense-byok`, `getcompanion-ai/feynman`

### 52.0 Why this section exists

K-Dense AI (`k-dense.ai`) is the closest competitor to Hubify Labs by vision. We need parity on their headline capabilities (databases, scientific data formats, skills catalog) AND we need to clearly differentiate where Hubify Labs wins (multi-surface IDE, multi-lab, always-on orchestrator, agent system, lab sovereignty). Houston explicitly said: "legitimately for improving our PRD and platform too not just for marketing copy purposes."

### 52.1 K-Dense's headline capabilities (the bar to match)

| Stat | What it means |
|---|---|
| **250+ databases** | PubMed, ChEMBL, UniProt, SEC EDGAR, FRED, BioServices, BioPython, etc. |
| **Unlimited tools, generated on demand** | Any Python function in any package becomes a callable tool |
| **500K+ Python packages** | Full PyPI access. Curated optimizations for 200+ scientific packages |
| **200+ scientific data formats** | Native support across 14 scientific domains |
| **Publish-ready outputs** | Manuscripts, slides, posters, PDFs, viz, schematics |

### 52.2 14 data format domains we need to support

Genomics & Sequencing · Sequence & Phylogenetics · Chemistry & Molecular · Materials Science · Medical Imaging & Pathology · Mass Spectrometry · **Astronomy** (already covered by BigBounce) · Neuroscience & Electrophysiology · Single-Cell & Array Storage · Geospatial · Data & Interchange · Documents & Outputs

### 52.3 K-Dense's "vs traditional LLMs" frame

K-Dense markets themselves against traditional LLMs (single-turn Q&A, hallucinations, plain text, no execution, generic). Their wins: end-to-end research automation, grounded in your data, publication-ready outputs, real Python/R/ML execution, AI does the work while you guide, deep domain expertise.

**This is the same fight we're in.** Hubify Labs needs the same baseline (real execution + publication-ready + grounded + deep domain) but we have a richer story on top (multi-surface, multi-lab, always-on, agent system).

### 52.4 Where Hubify Labs wins over K-Dense

1. **Multi-surface IDE** — Web + Desktop + CLI/TUI all equivalent. K-Dense is web-only.
2. **Always-on orchestrator (Fly.io)** — 24/7 work continues. K-Dense is session-based.
3. **Multi-lab framework** — own containerized labs you grow over time. Each lab has its own GitHub repo, Convex DB, Fly machine, public site.
4. **21-agent system** — orchestrator + 4 leads + 11 workers + 4 cross-provider reviewers. K-Dense has one agent.
5. **Cross-model peer review** — every paper/claim reviewed by GPT/Gemini/Sonnet/Perplexity. No echo chamber.
6. **Lab Sovereignty Rule** — read across labs OK, write FORBIDDEN. Triple-enforced (CLI/MCP/API).
7. **Public lab sites** — auto-deployed marketing sites for each lab.
8. **Houston Method v2** — opinionated post-experiment ritual the platform enforces.
9. **Lab community + remix** — public labs visitors can clone with one click.
10. **CLI/TUI as first-class** — `hubify` Go binary with bubbletea TUI.
11. **Memory architecture (4-layer)** — user/agent/lab/global. Agents remember.
12. **Vibe coding sandbox** — Vercel Sandbox for one-off figure generation.
13. **Activity Graph** — neural-brain view of your lab's living state.
14. **Publish-ready loop** — 5-round autonomous publishing with no-future-research-punts rule.

### 52.5 Where we need to catch up (action items)

1. **Database connectors (250+ target)** — currently we have BigBounce-specific: DESI, SDSS, LAMOST, eROSITA, NEOWISE, ACT, Planck, NANOGrav. Need to expand to ~250 general-purpose connectors. Short-term: claim parity by leveraging BioServices/BioPython package wrappers (each unlocks 30-40 sources). Long-term: dedicated connector catalog in the platform with discoverable schemas.

2. **Scientific data formats (200+ target across 14 domains)** — currently strong on Astronomy (FITS, VOTable). Need explicit support documented for the other 13 domains. **Action:** add a `view-data-formats` to the in-app mockup OR extend the existing Data Map view with a formats matrix.

3. **Skills catalog** — Houston wants us to fork/audit/extend `github.com/K-Dense-AI/claude-scientific-skills` as a starting baseline for our own skills catalog. **Action:** add a `view-skills` to the in-app showing the full skills catalog (their skills + our custom skills + per-domain organization).

4. **Domain breadth** — currently cosmology-leaning. Need explicit demos in healthcare, finance, materials science, etc. **Action:** add 2-3 more sample lab specs for non-cosmology domains.

### 52.6 What changes in the marketing site

The marketing site needs to **claim parity** with K-Dense's headline stats, even if some are aspirational. Specifically:

- Add a "by the numbers" stat band on the homepage with: `250+ databases · 200+ data formats · 14 scientific domains · 500K+ packages`
- Update the Features page section 1 to lead with these capabilities
- Add a "Skills catalog" link/card that points to the skills view (when built)
- Add a "vs K-Dense" comparison page (the Cursor pattern) showing the 14 wins above

### 52.7 Feynman (open-source CLI-first research agent)

**Source:** `feynman.is` · `github.com/getcompanion-ai/feynman` · built by Companion, Inc.
**Pitch:** "The open source AI research agent · Reads papers, searches the web, writes drafts, runs experiments, and cites every claim. All locally on your computer."
**Most architecturally similar to:** Hubify Labs CLI/TUI (PRD §45)

**Key features we should match or exceed:**

| Feynman feature | Hubify Labs status |
|---|---|
| `feynman "<question>"` cited research brief | Need: equivalent `hubify ask` command + cite-every-claim grounding |
| `/deepresearch` multi-agent investigation | Have: orchestrator + leads + workers, but no explicit "deep research" workflow |
| `/lit` literature review with consensus mapping | Need: add as a workflow |
| `/audit` paper claims vs code mismatch check | **Gap** — add as a skill + slash command |
| `/replicate` replication plan + sandboxed Docker execution | **Gap** — add as a workflow (we have publish-ready loop but no formal replication-of-others'-work) |
| `/compare` side-by-side source agreement/conflict matrix | Need: add as a workflow |
| `/draft` polished paper draft with inline citations | Have: publish-ready loop is more rigorous, but lighter `/draft` mode missing |
| `/autoresearch` autonomous loop (hypothesize → experiment → measure → repeat) | Have: this is essentially the orchestrator + Houston Method v2 + publish-ready loop |
| `/watch` recurring monitor for new papers/code/products | Need: add as a routine type (PRD §18 extension) |
| 4 agents (Researcher · Reviewer · Writer · Verifier) | **Win:** we have 21 agents pre-wired |
| AlphaXiv integration (paper search + Q&A + code reading) | **Gap** — add AlphaXiv as a skill in the catalog |
| Web search via Gemini/Perplexity | Have: cross-model peer review uses these |
| Session search (indexed recall) | Have: 4-layer memory architecture (PRD §20) |
| Browser + PDF export | Have: file preview tab + publish-ready PDF generation |
| **Local-first / Docker isolation** | **Gap** — add a local-only mode where the orchestrator runs in a local Docker container instead of Fly.io |
| Modal serverless GPU (compute backend) | Dropped per PRD §24 (RunPod-only). Re-evaluate as fallback after launch. |
| RunPod persistent GPU pods | Have (PRD §24) |
| Built on Pi (companion AI framework) + alphaXiv | We're building from scratch. Decision: stay independent. |

### 52.8 Cross-cutting action items (across all competitors)

1. **Skills catalog is non-negotiable** — both K-Dense and Feynman have explicit skills/tools catalogs. Build `view-skills` ASAP. Fork `K-Dense-AI/claude-scientific-skills` as baseline.
2. **Workflows / slash commands inventory** — both competitors have explicit workflow vocabularies. Document and grow ours. Houston already chose 4 chat slash commands (`/chat`, `/notechat`, `/promote`, `/share`); expand via the Feynman pattern: `/deepresearch`, `/lit`, `/review`, `/audit`, `/replicate`, `/compare`, `/draft`, `/autoresearch`, `/watch`.
3. **Cite-every-claim grounding** — Feynman emphasizes inline citations on every output. We have rigorous cross-model peer review but should also enforce inline citation discipline.
4. **Local-first / Docker isolation mode** — Feynman's "all locally" pitch is compelling for privacy-sensitive users. Add a local-only mode where the orchestrator runs in a local Docker container instead of Fly.io.
5. **AlphaXiv-style paper search infrastructure** — both competitors lean on existing paper search infra. Either integrate or build our own.

### 52.9 PRD impact

This section adds the following to the PRD as required reading:
- Section 52 (this section) — the competitive frame
- The companion file `COMPETITIVE_ANALYSIS.md` — full analysis with format lists, Feynman workflows, and reference repo list
- Future PRD sections to add:
  - `view-skills` spec (when built)
  - `view-workflows` spec (slash command catalog organized by category)
  - `view-data-formats` spec (200+ formats across 14 domains)
  - Expanded database connector inventory in §33 (Storage Strategy)
  - Local-first Docker mode spec (alternative to Fly.io for privacy-sensitive users)
  - `audit` / `replicate` / `watch` / `draft` workflow specs

---

## 53. Lab Site Builder — Vibe-Codable Public Research Sites

**Status:** Added 2026-04-12 by Houston. The original BigBounce website was manually maintained to track research progress. Hubify Labs solves the tracking problem in-app, but every lab still needs a public-facing site. This section specifies the Lab Site Builder: a chat-driven, auto-syncing, vibe-codable system that gives every lab a professional research website by default.

### 53.0 Why this section exists

Houston identified a gap: the existing mockup had a read-only "Site Preview" dashboard (deploy metadata, analytics) completely disconnected from the "Vibe Coding" sandbox (figure generation). The lab site should be the thing you vibe-code, not a separate dashboard. The two views should be unified, and the site itself should be a first-class product feature with standard templates, auto-sync from research outputs, and dedicated agents.

### 53.1 Core architecture

Each lab gets a public site at `<lab-slug>.hubify.app`. The site is:
- **Auto-generated** from a standard template on lab creation
- **Auto-synced** from research outputs (papers, experiments, figures, datasets, activity)
- **Vibe-codable** — the lab owner chats with a site agent to customize style, layout, content, and structure
- **Deployed via Vercel** from the `site/` subdirectory in the lab's GitHub repo
- **DNS provisioned automatically** via wildcard `*.hubify.app` on Cloudflare

### 53.2 Standard lab site template — `hubify-lab-default`

Every new lab gets a default template that matches the Hubify Labs design language:

**Default sections (10):**
1. **Hero** — Lab name, PI name, one-line mission, key stats (auto-populated from lab metadata)
2. **Key Results** — Top N findings with stat cards (auto-populated from experiments with `status=published`)
3. **Papers** — List of papers with readiness %, abstract, links to PDF/arXiv (auto-populated from papers view)
4. **Experiments** — Summary table with status badges (auto-populated from experiments)
5. **Figures** — Gallery grid with lightbox (auto-populated from figures view)
6. **Datasets** — Cards with descriptions, row counts, download links (auto-populated from datasets view)
7. **Activity** — Timeline feed of recent lab events (auto-populated from activity graph)
8. **Team** — Agent roster and PI info (auto-populated from agents view)
9. **Anomaly Catalog** — Survey table with QC badges (auto-populated from anomaly sweep results, if applicable)
10. **Footer** — "Powered by Hubify Labs" badge, GitHub link, last updated timestamp

**Design tokens:** Inherits from the Hubify Labs token system (`--bg`, `--surface`, `--accent`, etc.). Dark mode by default. The lab owner can override any token via chat.

**Typography:** Inter for UI chrome, Newsreader for paper/content sections, JetBrains Mono for data/stats. Same as the in-app IDE.

### 53.3 In-app Lab Site Builder UI

The Lab Site view in the IDE is a three-pane layout:

| Pane | Width | Purpose |
|------|-------|---------|
| **Left: Site Agent Chat** | 380px | Chat with the site-worker agent to customize the site. Shows auto-sync events, user messages, agent responses with code diffs |
| **Center: Live Preview** | flex | Vercel Sandbox rendering the actual lab site. Preview/Code/Logs tabs. Device preview (mobile/tablet/desktop). Refresh + open-in-browser + responsive toggle |
| **Right: Metadata Drawer** | 300px (collapsible) | Deploy status, Lighthouse scores, template config, site agent status, recent deploys, 7-day analytics. Toggled via "Analytics" button in top bar |

**Top bar:** Subdomain URL display, deploy status badge, branch selector, "Subdomain" settings button, "Analytics" toggle, "Publish" button.

### 53.4 Auto-sync hooks

The site agent listens to lab events and automatically updates the site content:

| Event | Action | Sections Updated |
|-------|--------|-----------------|
| `paper.published` | Add paper card with PDF link, abstract, citation count | Papers, Hero (paper count stat) |
| `experiment.completed` | Update experiment table row, refresh stats | Experiments, Key Results (if published) |
| `figure.generated` | Add to gallery, update lightbox | Figures |
| `dataset.created` | Add dataset card with download link | Datasets |
| `lab.settings_changed` | Update hero, team, branding | Hero, Team, Footer |
| `activity.event` | Append to activity timeline | Activity |

Auto-sync is **enabled by default**. The lab owner can disable per-section or globally via the metadata drawer.

### 53.5 Vibe-coding customization

The lab owner can customize anything about the site via chat:

**Style changes:** "Change the accent color to blue" → agent updates CSS custom properties and previews
**Layout changes:** "Move the figures section above experiments" → agent reorders template sections
**Content changes:** "Add a section about our methodology" → agent creates new section with content
**Template override:** "I want a completely different layout for the papers page" → agent generates custom page, saves as template override in `site/overrides/papers.html`

All changes are committed to the lab's `site/` directory in GitHub. The lab owner can review diffs, revert, or branch.

### 53.6 Site agent spec

**Agent:** `site-worker` (Worker tier, N3 group)
**Reports to:** `writing-lead` (Lead tier)
**Model:** Claude Sonnet (cost-efficient for HTML/CSS generation)

**Capabilities:**
- Generate and modify HTML/CSS/JS for the lab site template
- Read lab data via MCP tools (experiments, papers, figures, datasets)
- Commit changes to the `site/` subdirectory
- Trigger Vercel deploys
- Run Lighthouse audits and report scores
- Handle SEO (meta tags, OpenGraph, structured data, sitemap.xml)

**Event listeners:**
- `paper.published` → auto-update Papers section
- `experiment.completed` → auto-update Experiments table
- `figure.generated` → auto-update Figures gallery
- `lab.settings_changed` → auto-update branding/hero

**Escalation:** If the site-worker cannot fulfill a request (e.g., complex interactive features), it escalates to the writing-lead, who may delegate to a more capable model.

### 53.7 Migration: BigBounce → Lab Site

When BigBounce migrates to Hubify Labs (per `MIGRATION_BOUNCE_COSMOLOGY_LAB.md`):

1. The existing `bigbounce.hubify.app` content is preserved as a snapshot
2. A new lab site is generated from the `hubify-lab-default` template, auto-populated with all BigBounce data (4 papers, 53 experiments, 328K anomalies, 22 figures, 15 datasets)
3. Houston vibe-codes any custom sections (the current BigBounce site has custom pages like Explainer, Timeline, Visualize that go beyond the default template)
4. DNS cutover: `bigbounce.hubify.app` points to the new lab site
5. The old static site is archived at `bigbounce-archive.hubify.app` or in Backblaze B2

### 53.8 Template marketplace (v1.1)

Future: community-contributed templates. Labs can share their custom templates. One-click remix from the Lab Gallery. Deferred to v1.1.

---

## Appendix A: Section Index — What This PRD Covers

**Note:** this appendix was previously numbered §19 (an artifact from an early version of the PRD when it had only 18 sections + a session summary). It has been renamed to "Appendix A" to remove the numbering confusion — sections §0-§50 are the canonical PRD body, and this appendix provides a navigable index.

**Last updated:** 2026-04-08 (post-§42-§50 build-spec stub additions, post-mockup integration, post-§31-§39 additions)

| Section | Topic | Status |
|---------|-------|--------|
| 0 | Executive summary | ✅ |
| 1 | Safety-first repo strategy + Convex schema + **Lab=repo architecture lock** | ✅ updated 2026-04-08 |
| **40** | **Hierarchy v2 — locked taxonomy (5-level) + intent layer + chats + sharing + Lab=repo** | ✅ **NEW · supersedes §35** |
| 2 | Standardized Lab template + BigBounce COPY map | ✅ |
| 3 | Agent hierarchy (21 agents) | ✅ |
| 4 | Cross-lab sharing | ✅ |
| 5 | GPU/compute pipeline | ✅ |
| 6 | Backup & data management | ✅ |
| 7 | Website system | ✅ |
| 8 | CLI/TUI specification | ✅ |
| 9 | Fly.io cloud deployment | ✅ |
| 10 | Failure handling (14 modes) | ✅ |
| 10.5 | RunPod Safety Layer (ZERO DATA LOSS) | ✅ |
| 10.6 | Token limit handling & model fallbacks | ✅ |
| 10.7 | Hubify architecture integration | ✅ |
| 11 | Cost management | ✅ |
| 12 | Implementation plan (week-by-week, superseded by §32.3) | ✅ |
| 13 | Houston Method v2 encoded as platform | ✅ |
| 14 | Technical primitives | ✅ |
| 15 | Security & secrets | ✅ |
| 16 | Monitoring & observability | ✅ |
| 17 | Autonomous website generation pipeline | ✅ |
| 18 | Complete cron schedule (24 routines) | ✅ |
| 20 | Memory architecture (4-layer system) | ✅ |
| 21 | User profile & public showcase | ✅ |
| 22 | Scientific contributions & novelty scoring | ✅ |
| 23 | Houston Method v2 — platform-level enforcement | ✅ |
| 24 | **Compute provider — RunPod ONLY** (Pods + Serverless + CPU/GPU variants · Modal dropped 2026-04-08) | ✅ updated 2026-04-08 |
| **41** | **Compute Routing & Credits Monitoring** (4 routing rules: CPU-vs-GPU / Pod-vs-Serverless / pod-reuse / checkpoint discipline · 4 credit thresholds with escalating actions · pre-credits-out backup workflow · auto-resume on top-up · per-job dispatcher decision tree) | ✅ **NEW 2026-04-08** |
| 25 | Agent communication / multi-agent activity feed | ✅ |
| 26 | Task review pipeline & activity threads | ✅ |
| 27 | All-hands standups (3x/day) | ✅ |
| 28 | Patterns borrowed from Paperclip | ✅ |
| 29 | Cross-model peer review (CRITICAL — no echo chamber) | ✅ |
| 30 | Agent host & terminal integration | ✅ |
| **31** | **UI Component Inventory — built and specified** | ✅ **NEW** |
| **32** | **Development phase readiness** | ✅ **NEW** |
| **33** | **Storage Strategy & Data Map — single source of truth** (v2: **5 zones** Z1-Z5 as primary mental model · 8 tiers as impl detail · `hubify.storage` API · 28 data type → zone matrix · per-project map.md · storage-map-worker · Files sidebar zone grouping · Data Map view · monthly cost ~$35) | ✅ **v2 RESTRUCTURED** |
| **34** | **Agent File Structure — indydevdan-style self-improving agents** (agent.md / soul.md / skills/ / learnings.jsonl / episodes.jsonl, weekly self-reflection cron, orchestrator scaffolds new agents from templates, agent sidepeek tabs) | ✅ **NEW** |
| **35** | **Hierarchy Taxonomy — Global → Labs → Projects → Pipelines → Experiments → Ideas → Tasks** (7 levels with worked BigBounce example, definitions, transitions, where each lives in storage, common confusions resolved) | ✅ **NEW** |
| **36** | **Preresearch Mode + CEO Brainstorm** (CEO orchestrator agent variant with 8 skills, 8-step session lifecycle, Research Planning Doc format, mockup chat panel 3rd mode, 6 PRD-locked workflow rules, ~$60/mo envelope) | ✅ **NEW** |
| **37** | **Publishing Phase — Autonomous Publish-Ready Loop** (publishing-lead agent + 4 publishing workers, 5-round publish-ready loop algorithm, scorecard, 'no future research punts' Houston Method update §37.6, rejection mode, Houston escalation, kanban 'PUBLISH READY 95%' pillar, arXiv package format, ~$30/paper cost) | ✅ **NEW** |
| **38** | **Human Research Journal — Obsidian-style notes inside Hubify** (5 note groups: Daily/Prompts/Snippets/Links/Evergreen · agent visibility contract · private by default · `notes/` lives in Z1 Source · sidebar Notes section + new-note sidepeek + 4 agent visibility toggles per note) | ✅ **NEW** |
| **39** | **Activity Graph — The Neural Brain View** (replicates hubify.com/activity/graph faithfully · 5 group palette · 443 nodes · ~2K edges · neuron pulses traveling along edges · live agent activity visualization · the singularity-vibes proof of life view) | ✅ **NEW** |
| **42** | **macOS desktop app spec** — Tauri 2 shell · 11 native features · menu bar variant · iOS deferral · distribution · points at `DESKTOP_APP_SPEC.md` | ✅ **NEW 2026-04-08** |
| **43** | **REST + GraphQL API spec** — JWT HS256 + per-lab scopes · ~85 endpoints across 19 groups · RFC 7807 errors · §41 routing requirement · points at `API_SPEC.md` + `api-spec.openapi.yaml` | ✅ **NEW 2026-04-08** |
| **44** | **MCP server spec** — 4 MCP primitives + 3 transports · ~30 tools across 11 categories · 15 resources + 6 prompts · Lab Sovereignty enforcement · N4-not-claimable · audit logging · points at `MCP_SERVER_SPEC.md` + `mcp-server-spec.yaml` | ✅ **NEW 2026-04-08** |
| **45** | **CLI spec** — Go + Cobra + bubbletea TUI · ~120 commands across 19 categories · §41 routing CLI enforcement · OAuth/PKCE · plugin system deferred to v1.1 · points at `CLI_SPEC.md` + `cli-spec.yaml` | ✅ **NEW 2026-04-08** |
| **46** | **Deployment infrastructure plan** — Vercel + Convex + Fly + RunPod + Backblaze + Cloudflare + GitHub Actions + monitoring stack · Fly 4-surface integration model · cost forecast · points at `DEPLOYMENT_INFRA_PLAN.md` | ✅ **NEW 2026-04-08** |
| **47** | **Mintlify docs port plan** — subpath at hubify-labs.com/docs · first 7 docs pages outline · codegen pipeline auto-generates API/CLI reference from YAML specs · Algolia DocSearch + Mintlify AI assistant | ✅ **NEW 2026-04-08** |
| **48** | **`hubify://` URL scheme spec** — universal deep-link catalog · `hubify://<lab-slug>/<entity-type>/<entity-id>` · 19 entity types · cross-lab read OK / write FORBIDDEN · 7 surface-specific handling rows · stability forever guarantee | ✅ **NEW 2026-04-08** |
| **49** | **Authentication & authorization spec** — 5 auth providers + 4 token types · per-lab scope claim · Lab Sovereignty Rule TRIPLE enforcement (CLI + MCP + API) · 6 agent consent boundaries · audit logging · per-token-type rate limits | ✅ **NEW 2026-04-08** |
| **50** | **Telemetry & observability spec** — 9 event categories · privacy boundaries (lab content NEVER leaves user's Convex deployment) · activity feed schema · per-experiment cost tracking schema · 8-row alert routing table · telemetry opt-out per-user not per-lab | ✅ **NEW 2026-04-08** |
| **51** | **Marketing site spec** — `hubify-labs.com` public pages · 7 v1 pages (home, features, labs gallery, lab detail, docs, guides, blog) · The Window 2025-2027 essay urgency band · Lab gallery showcase pattern (community labs with view-site + remix CTAs) · 4-stack architecture explainer canonical text · separate from in-app research IDE | ✅ **NEW 2026-04-09** |
| **52** | **Competitive Frame** — K-Dense + Feynman + AI research agent landscape · 14 feature advantages · gaps to close | ✅ **2026-04-09** |
| **53** | **Lab Site Builder** — vibe-codable public research sites · `hubify-lab-default` template (10 sections) · auto-sync from research outputs · 3-pane UI (site agent chat + Vercel Sandbox preview + collapsible analytics) · `site-worker` agent spec · BigBounce migration plan · template marketplace v1.1 | ✅ **NEW 2026-04-12** |

**Total: 48 sections, ~8,700+ lines. Mockup ↔ PRD parity at 1:1. Every system specified. Every cron scheduled. Every failure handled. Every UI surface inventoried. Every byte of data has a known home (5 zones). Every agent has a coherent file structure (indydevdan-style). Every level of organization is named (Lab → Task). Preresearch ideation has a home. The macOS app, REST/GraphQL API, MCP server, CLI, deployment plan, Mintlify docs port, `hubify://` URL scheme, auth/authz, telemetry, and lab site builder are all locked. Ready for development phase handoff.**

---

## Appendix B: Open Question Defaults

**Status:** Locked 2026-04-08. The PRD has 4 open questions that need Houston's confirmation before the rebuild begins. This appendix proposes a default answer + reasoning for each, so the loop can continue without blocking on Houston. Houston confirms or overrides at sign-off.

### B.1 Chat default model

**Question:** What's the default model for new chats in the web app + CLI + MCP server?

**Default answer:** **Claude Sonnet 4.6** (`claude-sonnet-4-6`).

**Why:**
- Sonnet 4.6 is the newest model in the Sonnet line as of 2026-04-08 (per the system environment knowledge cutoff)
- Best cost/quality ratio for the chat surface (long-form reasoning, code generation, file editing)
- Houston explicitly uses Claude Code daily and Claude Code defaults to Sonnet — staying consistent reduces cognitive overhead
- Opus 4.6 is the heavy-lifting model for orchestrator-level decisions (per PRD §3 routing) but is overkill for everyday chat
- Haiku 4.5 is the bursty/parallel model for cheap subagent calls but is undersized for the main chat
- The user can swap models per chat via the chat composer's model switcher (coming in Round C #3)

**Houston override expected:** likely confirms Sonnet 4.6 default. May override to Opus for high-stakes papers, but that's per-chat not global.

### B.2 Voice dictation provider

**Question:** What service handles voice → text for chat input on the desktop app?

**Default answer:** **Whisper API** (OpenAI).

**Why:**
- Whisper is the de facto standard for voice → text in 2026; it's accurate, multilingual, fast
- Already in the OpenAI account (we use OpenAI for `peer-review-gpt` per cross-model peer review §29)
- ~$0.006/min — negligible at any reasonable usage volume
- Tauri 2 has a native audio capture plugin that ships PCM directly to a Whisper API call without needing intermediate file storage
- Open-source Whisper (whisper.cpp running locally) is the fallback if Houston wants offline mode

**Rejected:**
- Apple Speech Framework: Apple-only, doesn't help on Linux/Windows builds
- AssemblyAI: extra vendor, no advantage over Whisper
- Google Speech-to-Text: Google account dependency, no advantage
- Local Whisper: CPU/GPU usage on the user's Mac is non-trivial; cloud is better for v1

**Houston override expected:** likely confirms. May want offline whisper.cpp later for privacy-sensitive notes.

### B.3 Cross-lab read-only enforcement layer

**Question:** Where is the Lab Sovereignty Rule (PRD §40.11) actually enforced for cross-lab READS?

**Default answer:** **GitHub repo permissions + Convex auth** (the redundant pair).

**Layer 1 — GitHub repo permissions:** Each lab is a separate GitHub repo (per PRD §1 Lab=repo lock). Public labs are public repos; private labs are private repos. Cross-lab read is GATED by GitHub's standard repo permission system — if Houston grants read access to Lab A on Lab B's repo, Lab B can clone Lab A's source. If not, it can't.

**Layer 2 — Convex auth:** The Convex backend stores per-lab data (experiments, papers, agents) in per-lab tables. Convex auth tokens carry a `labs` claim per PRD §49. Read queries against Lab A's tables from a token without `labs[A].read` permission return empty arrays (not errors — silent denial, like Postgres row-level security).

**Why redundant:** Belt + suspenders. If GitHub permissions are misconfigured, Convex auth catches it. If Convex auth is misconfigured, GitHub permissions catch it. Either layer alone is sufficient for the legal/contractual requirement; the combination is for safety against misconfiguration.

**Houston override expected:** likely confirms. The redundant model is the obvious right answer.

### B.4 BigBounce migration final subdomain

**Question:** What's the final URL for the migrated bigbounce lab?

**Default answer:** **`bigbounce2.hubify.app` for the burn-in window, then graduate to `bigbounce.hubify.app` after sign-off.**

This is the same answer as `MIGRATION_BOUNCE_COSMOLOGY_LAB.md` §6 Q1 — restated here so the PRD has the canonical answer. See the migration plan for the full reasoning.

**Houston override expected:** confirmed at the migration sign-off.

### B.5 Sign-off block

When Houston has reviewed B.1-B.4, he writes:

```
[CONFIRM ALL DEFAULTS]
or
[OVERRIDE: B<n> → <new answer>]
```

This unblocks the PRD from the "open questions" gate in `BUILD_READINESS_CHECKLIST.md` Category A. The defaults above stand until Houston explicitly overrides them.

---

*This PRD is the definitive specification for Hubify Labs. Every section is implementation-ready. Nothing is punted. Build from Week 1 Day 1.*
