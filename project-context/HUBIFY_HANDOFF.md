# Hubify Agent Handoff: BigBounce Research Infrastructure Extraction

## Context for the Hubify Repo Agent

You are working on the main Hubify platform repository. A sister repo (`Hubify-Projects/bigbounce`) contains a fully operational research infrastructure that has been built over months for a theoretical physics paper. This infrastructure needs to be extracted into reusable Hubify platform components so future research hubs can be spun up using the same setup.

**DO NOT modify the BigBounce repo.** Read from it as a reference. All new code goes into the Hubify platform repo.

---

## What BigBounce Has Built (Read from `Hubify-Projects/bigbounce`)

### Key Documents to Read First
1. `project-context/RESEARCH_ARCHITECTURE.md` — **998-line complete technical reference** of every pipeline, API, function, and data flow. This is your primary source of truth.
2. `project-context/peer-reviews/2026-03-12_0000PST_product-architecture-audit-v2.md` — Product architecture audit mapping BigBounce to the three-pillar Hubify vision.
3. `.env.example` — All 12 API keys with documentation.
4. `.hubify/squad-init.md` — Current (minimal) squad definition.

### What Exists in BigBounce (Summary)

**9 Python agent modules** (`research/agents/`):
- `reasoning_router.py` — Routes to 7 LLMs (Claude, GPT-4o, DeepSeek R1, Gemini, Perplexity, Grok, OpenRouter) by task type
- `literature_search.py` — Unified search across NASA ADS, Semantic Scholar, arXiv, Perplexity
- `computation.py` — Wolfram Alpha verification + DeepSeek R1 mathematical claim checking
- `data_access.py` — MAST/JWST, Gaia DR3, VizieR (20K catalogs), NED queries
- `dataset_loaders.py` — HuggingFace MMU (100TB streaming), AstroML, Polymathic AI models
- `galaxy_zoo.py` — Galaxy catalog queries, spin asymmetry analysis, HEALPix dipole fitting
- `spin_analysis.py` — End-to-end galaxy spin pipeline
- `galaxy_classifier.py` — Zoobot + vision API (Claude/GPT-4o) galaxy classification

**GPU Compute** (`research/`):
- `runpod_cloud.py` — Full RunPod pod lifecycle via GraphQL (create/start/stop/terminate/SSH/SCP)
- `runpod_gpu_session.py` — 11-cell GPU session runner with platform detection (RunPod/Colab/Lambda/local)
- `env_check.py` — API key validation and connectivity testing

**MCMC Pipeline** (`reproducibility/`):
- 4 Cobaya YAML configs for cosmological parameter estimation
- Stan hierarchical Bayesian model for galaxy spin fitting
- MCMC monitor for real-time chain convergence tracking
- Full GPU run snapshot with hardware/software manifest

**Data Pipelines** (`scripts/`):
- `build_data.py` — CSV → validated JSON/JSONP/XLSX with CI
- `eb_forecast.py` — CMB birefringence detection forecast
- `download_galaxy_zoo.py` — Stream + process Galaxy Zoo for web
- `figure_checks.py` — CI data integrity validation

**20 External Service Integrations** with 12 API keys.

---

## What to Build in Hubify

### Phase 1: Hub Specification (`.hubify/` Convention)

Define the `.hubify/` directory spec that ALL Hubify Hubs will follow. BigBounce is the reference implementation.

Create these files in the Hubify platform repo:

#### `packages/hub-spec/schema/hub.yaml.schema.json`
JSON Schema for `.hubify/hub.yaml`:
```yaml
# Every Hubify Hub has this file at .hubify/hub.yaml
name: bigbounce                          # Hub identifier
display_name: "Geometric Dark Energy"    # Human-readable
type: research-paper                     # Hub template type
version: "1.3.0"
visibility: public                       # public | private | team
author:
  name: "Houston Golden"
  email: "houston@hubify.com"
domain: bigbounce.hubify.app
repo: Hubify-Projects/bigbounce
tags: [cosmology, dark-energy, spin-torsion, mcmc]
pillars:
  agents: true                           # Has agent squad
  compute: true                          # Has GPU/compute jobs
  knowledge: true                        # Has public knowledge output
```

#### `packages/hub-spec/schema/squad.yaml.schema.json`
JSON Schema for `.hubify/squad.yaml`:
```yaml
# Agent squad definition
squad:
  name: "Astrophysics Research Squad"
  agents:
    - id: astro-atlas-v1
      name: Atlas
      role: literature
      model: perplexity/sonar-pro        # Default model for this agent
      fallback_model: anthropic/claude-opus-4-6
      capabilities: [literature_search, citation_graph, paper_discovery]
      tools: [nasa_ads, semantic_scholar, arxiv, perplexity]
    - id: astro-tensor-v1
      name: Tensor
      role: computation
      model: deepseek/deepseek-reasoner
      capabilities: [equation_verify, dimensional_check, wolfram_query]
      tools: [wolfram_alpha, deepseek_r1]
    - id: astro-nova-v1
      name: Nova
      role: explorer
      model: google/gemini-2.5-pro
      capabilities: [multimodal_analysis, data_exploration]
      tools: [data_access, dataset_loaders, galaxy_zoo]
    - id: astro-keane-v1
      name: Professor Keane
      role: reviewer
      model: anthropic/claude-opus-4-6
      capabilities: [peer_review, writing, argument_structure]
      tools: [reasoning_router]
    - id: astro-sage-v1
      name: Sage
      role: synthesizer
      model: openai/gpt-4o
      capabilities: [synthesis, general_reasoning]
      tools: [reasoning_router, literature_search]
  workflow:
    phases: [literature_review, mathematical_validation, data_analysis, paper_synthesis, peer_review]
```

#### `packages/hub-spec/schema/mission.yaml.schema.json`
```yaml
# Research mission definition
id: mcmc-verification
title: "Independent MCMC Verification"
status: completed                        # planned | active | completed | failed
started: "2026-03-04T08:47:00Z"
completed: "2026-03-05T08:25:00Z"
squad_config: default                    # Use hub's default squad
compute:
  provider: runpod
  gpu: "NVIDIA RTX 6000 Ada"
  vram_gb: 48
  estimated_hours: 24
skills_used:
  - mcmc_run
  - convergence_monitor
  - equation_verify
outputs:
  - path: reproducibility/cosmology/mcmc_results_latest.txt
    type: results
  - path: reproducibility/cosmology/convergence_latest.csv
    type: diagnostics
```

---

### Phase 2: Research SDK (`packages/hubify-sdk/`)

Extract BigBounce's reusable code into a pip-installable SDK.

#### Directory Structure
```
packages/hubify-sdk/
├── hubify_sdk/
│   ├── __init__.py
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── router.py              # FROM: bigbounce/research/agents/reasoning_router.py
│   │   └── registry.py            # NEW: Agent discovery + capability matching
│   ├── skills/
│   │   ├── __init__.py
│   │   ├── literature.py          # FROM: bigbounce/research/agents/literature_search.py
│   │   ├── computation.py         # FROM: bigbounce/research/agents/computation.py
│   │   ├── data_access.py         # FROM: bigbounce/research/agents/data_access.py
│   │   ├── dataset_loader.py      # FROM: bigbounce/research/agents/dataset_loaders.py
│   │   └── vision_classify.py     # FROM: bigbounce/research/agents/galaxy_classifier.py (generic parts)
│   ├── compute/
│   │   ├── __init__.py
│   │   ├── runpod.py              # FROM: bigbounce/research/runpod_cloud.py (parameterized)
│   │   ├── gpu_session.py         # FROM: bigbounce/research/runpod_gpu_session.py (framework only)
│   │   └── storage.py             # NEW: Network volume management + backup (see lessons learned below)
│   ├── config/
│   │   ├── __init__.py
│   │   ├── env_check.py           # FROM: bigbounce/research/env_check.py
│   │   └── keys.py                # NEW: Centralized API key management
│   ├── data/
│   │   ├── __init__.py
│   │   └── builder.py             # FROM: bigbounce/scripts/build_data.py (generic pipeline)
│   └── hub/
│       ├── __init__.py
│       ├── manifest.py            # NEW: Parse/validate .hubify/ directory
│       ├── knowledge.py           # NEW: CRUD for claims/findings/questions YAML
│       └── missions.py            # NEW: Mission state management
├── pyproject.toml
├── README.md
└── tests/
```

#### Key Extraction Notes

**reasoning_router.py → agents/router.py:**
- Remove BigBounce-specific defaults
- Make MODELS dict configurable via YAML (load from .hubify/squad.yaml)
- Keep all 3 provider protocols (OpenAI-compatible, Anthropic, Google)
- Add model cost tracking

**runpod_cloud.py → compute/runpod.py:**
- Remove hardcoded `DEFAULT_POD_ID = "47htajss1ng2ig"`
- Make pod config loadable from .hubify/mission.yaml compute block
- Add `backup_workspace()` function (see storage lessons below)
- Add `snapshot_volume()` for pre-termination safety

**runpod_gpu_session.py → compute/gpu_session.py:**
- Keep: environment detection, API key loading, repo cloning framework
- Remove: BigBounce-specific cells (4-11)
- Add: cell registration system so each hub defines its own cells
- Pattern: `@gpu_session.cell(name="load_model", gpu_required=True, min_vram_gb=4)`

**literature_search.py → skills/literature.py:**
- 100% reusable as-is
- Add: result caching (same query within 1hr returns cached)
- Add: structured output format for knowledge layer

---

### Phase 3: Compute Storage & Resilience (CRITICAL LESSONS LEARNED)

BigBounce learned these the hard way with RunPod. Build these into the SDK:

#### RunPod Storage Architecture
```
Pod Types:
├── On-Demand: ~$0.74/hr for RTX 6000 Ada (48GB)
├── Spot: Cheaper but can be preempted
└── Serverless: Per-second billing, auto-scale

Storage:
├── Container Disk (20GB default): EPHEMERAL — lost on stop/terminate
├── Network Volume (50GB default): PERSISTENT across stop/start
│   └── Mounted at /workspace
│   └── BUT: destroyed on terminate or billing failure
└── S3/Cloud backup: Must be configured manually
```

#### Critical Storage Rules (Build Into SDK)

1. **Never store irreplaceable data only on RunPod volumes.**
   - MCMC chains take 4-12 hours to generate. If billing lapses, volume is destroyed.
   - BigBounce lost chains during billing issues and had to re-run.

2. **Auto-backup strategy** (implement in `compute/storage.py`):
   ```python
   # After every significant computation:
   def backup_outputs(workspace_dir="/workspace", destinations=["git", "s3"]):
       """
       1. Git commit + push results to repo (small files)
       2. SCP large files to local machine
       3. Upload to S3/R2 bucket (optional)
       """

   # Before any pod stop/terminate:
   def pre_shutdown_backup():
       """
       1. List all files modified since last backup
       2. Compress chains/ directory
       3. Push to configured backup destination
       4. Only then allow shutdown
       """
   ```

3. **Volume snapshot before terminate:**
   ```python
   # NEVER terminate without confirmation + backup
   def safe_terminate(pod_id):
       print("Checking for unbackedup data...")
       unbackedup = find_unbackedup_files()
       if unbackedup:
           print(f"WARNING: {len(unbackedup)} files not backed up")
           backup_outputs()
       # Then terminate
   ```

4. **Workspace organization standard:**
   ```
   /workspace/
   ├── {project}/              # Git repo (recoverable)
   ├── outputs/                # Research outputs (MUST BACKUP)
   │   ├── chains/             # MCMC chains (large, expensive to regenerate)
   │   ├── models/             # Downloaded model weights (recoverable from HF)
   │   └── results/            # Analysis results (MUST BACKUP)
   ├── .env.local              # API keys (recoverable from local machine)
   └── .backup_manifest.json   # What's been backed up and when
   ```

5. **Cost monitoring:**
   ```python
   def check_billing_status():
       """Alert if RunPod balance is low enough to risk volume termination"""
       pod = get_pod()
       cost_per_hr = pod['costPerHr']
       # If uptime > 24h, warn about costs
       # If approaching billing threshold, auto-backup
   ```

---

### Phase 4: Hub Templates

Create a `hubify init` command that scaffolds new research hubs using BigBounce as the reference:

```
packages/hub-templates/
├── research-paper/
│   ├── .hubify/
│   │   ├── hub.yaml.template
│   │   ├── squad.yaml.template
│   │   ├── missions/
│   │   │   └── _example.yaml
│   │   ├── skills/
│   │   ├── knowledge/
│   │   │   ├── claims.yaml
│   │   │   ├── findings.yaml
│   │   │   └── open-questions.yaml
│   │   └── context/
│   ├── research/
│   │   └── agents/               # Symlinks or imports from hubify-sdk
│   ├── reproducibility/
│   │   └── README.md
│   ├── scripts/
│   │   └── build_data.py
│   ├── site/                     # Public hub website
│   │   └── index.html
│   ├── .env.example
│   ├── .gitignore
│   ├── CLAUDE.md.template
│   ├── AGENTS.md.template
│   └── requirements.txt
├── data-analysis/
│   └── ... (future template)
└── ml-experiment/
    └── ... (future template)
```

---

## External API Setup Guide (For New Hubs)

When spinning up a new research hub, these APIs need to be configured:

### Required (2 keys)
| Service | Sign Up | Cost | Key Name |
|---------|---------|------|----------|
| Anthropic Claude | console.anthropic.com | Pay-per-token | `ANTHROPIC_API_KEY` |
| NASA ADS | ui.adsabs.harvard.edu/user/settings/token | Free | `NASA_ADS_API_KEY` |

### Recommended (5 keys)
| Service | Sign Up | Cost | Key Name |
|---------|---------|------|----------|
| DeepSeek R1 | platform.deepseek.com | Pay-per-token (cheap) | `DEEPSEEK_API_KEY` |
| Wolfram Alpha | developer.wolframalpha.com | Free (2K/mo) | `WOLFRAM_ALPHA_APP_ID` |
| HuggingFace | huggingface.co/settings/tokens | Free | `HUGGINGFACE_TOKEN` |
| Perplexity | perplexity.ai/settings/api | Pay-per-token | `PERPLEXITY_API_KEY` |
| RunPod | runpod.io/console/user/settings | ~$0.74/hr GPU | `RUNPOD_API_KEY` |

### Optional (5 keys)
| Service | Sign Up | Cost | Key Name |
|---------|---------|------|----------|
| OpenAI GPT | platform.openai.com | Pay-per-token | `OPENAI_API_KEY` |
| Google Gemini | aistudio.google.com | Free tier | `GOOGLE_AI_API_KEY` |
| xAI Grok | console.x.ai | Pay-per-token | `XAI_API_KEY` |
| OpenRouter | openrouter.ai/keys | Pay-per-token | `OPENROUTER_API_KEY` |
| Semantic Scholar | semanticscholar.org/product/api#api-key | Free | `SEMANTIC_SCHOLAR_API_KEY` |

### Free (No Key Required)
- arXiv API (rate limited: 1 req/3s)
- MAST/JWST archive
- Gaia DR3 (via astroquery)
- VizieR catalogs (20,000+)
- NED extragalactic database
- JWST S3 public bucket (`s3://stpubdata/jwst/public/`)

---

## RunPod GPU Setup Playbook (For New Hubs)

### 1. Create Pod
```bash
# Via CLI (from hubify-sdk)
hubify compute create \
  --gpu "NVIDIA RTX 6000 Ada Generation" \
  --volume-gb 50 \
  --image "runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04"

# Or via existing script:
python3 research/runpod_cloud.py create
```

### 2. Setup Environment
```bash
# Push API keys to pod
hubify compute push-keys

# Install dependencies
hubify compute run "pip install hubify-sdk[all]"

# Clone project repo
hubify compute run "cd /workspace && git clone https://github.com/Hubify-Projects/{repo}.git"
```

### 3. Run Research Session
```bash
# Run all cells
hubify compute session --all

# Run specific cells
hubify compute session --cells 0,1,4,5

# Monitor MCMC chains
hubify compute run "python3 mcmc_monitor.py"
```

### 4. Backup Before Stopping
```bash
# Auto-backup all outputs
hubify compute backup

# Then safe to stop (preserves volume)
hubify compute stop

# NEVER terminate without backup
hubify compute terminate  # Will auto-backup first, then confirm
```

---

## Three-Pillar Integration Points

### Pillar 1 (OpenClaw) ↔ Hubify Platform
- `.hubify/` directory is the interface contract
- Hub manifest, squad config, mission state all live in the hub repo
- Hubify platform reads these to display dashboards, track progress
- Local OpenClaw reads these for CLI operations

### Pillar 2 (Agent Squads) ↔ Hubify SDK
- `hubify-sdk` is the execution engine
- Skills are pip-installable and composable
- Mission orchestrator reads .hubify/missions/ and sequences skill calls
- Research outputs flow back to .hubify/knowledge/

### Pillar 3 (Social Network) ↔ Hub Website
- Knowledge layer (.hubify/knowledge/) is the structured data source
- Site builder generates public website from knowledge layer
- API endpoints expose data for cross-hub queries
- Version history enables research timeline visualization

---

## Files to Reference in BigBounce Repo

For the complete technical details, read these files from `Hubify-Projects/bigbounce`:

| File | Lines | What It Documents |
|------|-------|-------------------|
| `project-context/RESEARCH_ARCHITECTURE.md` | 998 | Every function, API, endpoint, auth method |
| `project-context/peer-reviews/2026-03-12_0000PST_product-architecture-audit-v2.md` | 382 | Product audit, pillar scores, restructuring plan |
| `research/agents/reasoning_router.py` | 300 | Multi-model routing (EXTRACT THIS) |
| `research/agents/literature_search.py` | 200 | Literature search (EXTRACT THIS) |
| `research/agents/computation.py` | 252 | Wolfram + DeepSeek verification (EXTRACT THIS) |
| `research/agents/data_access.py` | 289 | Astronomical archive queries (EXTRACT THIS) |
| `research/agents/dataset_loaders.py` | 263 | HuggingFace + AstroML loaders (EXTRACT THIS) |
| `research/runpod_cloud.py` | 541 | RunPod GraphQL API (EXTRACT THIS) |
| `research/runpod_gpu_session.py` | 524 | GPU session runner (EXTRACT FRAMEWORK) |
| `research/env_check.py` | 146 | API key validation (EXTRACT THIS) |
| `reproducibility/cosmology/cobaya_full_tension.yaml` | 117 | MCMC config example |
| `reproducibility/cosmology/archives/gpu_run_snapshot_20260305_0824/MANIFEST.md` | 111 | GPU run snapshot with hardware/software specs |
| `.env.example` | 93 | Complete API key template |

**Total extractable code: ~2,700 lines (65% of BigBounce research code)**
**BigBounce-specific code that stays: ~1,400 lines (physics-specific analysis)**
