# Hubify Labs/Research SDK — BigBounce Infrastructure Extraction

## Important: Scope & Limitations of This Document

**This document was written from inside the BigBounce repo (`Hubify-Projects/bigbounce`).** The author has:
- Full knowledge of every file, function, and API in BigBounce
- **ZERO visibility into the main Hubify repo** — no knowledge of its current architecture, directory structure, frameworks, conventions, or state

**Therefore:** This document describes WHAT exists in BigBounce and WHAT is extractable. It does NOT prescribe WHERE or HOW to integrate it into the Hubify codebase. That's your job — adapt these patterns to whatever architecture already exists in your project.

**Naming:** We're calling this the **Hubify Labs SDK** (or Hubify Research SDK) — this is the research/labs infrastructure layer, not the core Hubify platform SDK. It covers: multi-model AI agent routing, external research APIs, GPU compute management, data pipelines, and operational lessons learned.

---

## What This Document Covers

1. [Complete inventory of extractable code from BigBounce](#1-extractable-code)
2. [Every external API integration with auth details](#2-external-apis)
3. [GPU compute setup and critical storage/billing lessons](#3-gpu-compute)
4. [MCMC and scientific compute pipelines](#4-compute-pipelines)
5. [The `.hubify/` directory convention (proposed, not yet standard)](#5-hubify-convention)
6. [What stays BigBounce-specific vs. what generalizes](#6-what-stays)
7. [Prompt you can give a Hubify repo coding agent](#7-agent-prompt)

---

## 1. Extractable Code from BigBounce <a name="1-extractable-code"></a>

BigBounce has ~6,100 lines of Python research infrastructure. About ~2,700 lines (65%) are general-purpose and could power any research hub. Here's exactly what exists:

### Agent Modules (research/agents/) — 9 files, ~2,200 lines

#### reasoning_router.py (300 lines) — **100% EXTRACTABLE**
Multi-model LLM routing. Routes prompts to the best model for the task.

**7 model integrations:**

| Key | Model | Provider | Base URL | Auth |
|-----|-------|----------|----------|------|
| `math_rigor` | deepseek-reasoner | DeepSeek | `https://api.deepseek.com/v1` | Bearer token |
| `multimodal` | gemini-2.5-pro | Google | `https://generativelanguage.googleapis.com/v1beta` | `?key=` param |
| `writing` | claude-opus-4-6 | Anthropic | `https://api.anthropic.com/v1` | `x-api-key` header |
| `reasoning` | gpt-4o | OpenAI | `https://api.openai.com/v1` | Bearer token |
| `literature` | sonar-pro | Perplexity | `https://api.perplexity.ai` | Bearer token |
| `fast` | grok-3 | xAI | `https://api.x.ai/v1` | Bearer token |
| `multi` | claude-sonnet-4 | OpenRouter | `https://openrouter.ai/api/v1` | Bearer token |

**Key functions:**
- `query(prompt, task, system, model_override, max_tokens, temperature)` → routes to best model
- `multi_query(prompt, models, system, max_tokens)` → sends to multiple models for consensus
- `available_models()` → returns models with configured API keys

**3 provider protocols implemented:**
- OpenAI-compatible (DeepSeek, OpenAI, Perplexity, xAI, OpenRouter): Bearer token, `/chat/completions`
- Anthropic: `x-api-key` header, `/v1/messages`, `anthropic-version: 2023-06-01`
- Google: API key as query param, `/v1beta/models/{model}:generateContent`

---

#### literature_search.py (200 lines) — **100% EXTRACTABLE**
Unified search across 4 academic literature sources.

| Source | Endpoint | Auth | Notes |
|--------|----------|------|-------|
| NASA ADS | `https://api.adsabs.harvard.edu/v1/search/query` | Bearer `NASA_ADS_API_KEY` | Astrophysics-specific, 30s timeout |
| Semantic Scholar | `https://api.semanticscholar.org/graph/v1/paper/search` | `x-api-key` (optional) | Cross-field, citation graphs |
| arXiv | `http://export.arxiv.org/api/query` | None | XML feed, enforced 3s rate limit |
| Perplexity | `https://api.perplexity.ai/chat/completions` | Bearer token | Web-grounded LLM search, 60s timeout |

**Key functions:**
- `search_ads(query, rows, sort, year_range, fields)` — ADS query with full syntax support
- `ads_citations(bibcode)` / `ads_references(bibcode)` — citation graph traversal
- `search_s2(query, limit, fields)` — Semantic Scholar search
- `s2_paper(paper_id)` / `s2_citation_graph(paper_id, depth)` — paper details + graph
- `search_arxiv(query, max_results, sort_by, category)` — category-filtered preprint search
- `search_perplexity(query, model)` — web-grounded search with citations
- `search(query, sources, max_results, category)` — **unified multi-source search**

---

#### computation.py (252 lines) — **100% EXTRACTABLE**
Mathematical claim verification using Wolfram Alpha + DeepSeek R1.

| Service | Endpoints | Auth |
|---------|-----------|------|
| Wolfram Alpha | `/v1/result`, `/v2/query`, `/v1/llm-api` | `appid` query param, `WOLFRAM_ALPHA_APP_ID` |
| DeepSeek R1 | `https://api.deepseek.com/v1/chat/completions` | Bearer token, 180s timeout |

**Key functions:**
- `wolfram(query, format)` — 3 formats: "full" (pods), "short" (one-line), "llm" (agent-friendly)
- `wolfram_verify(expression, expected)` — compare computed vs expected
- `deepseek_verify(claim, context, max_tokens)` — deep reasoning check (dimensional consistency, sign errors, index symmetry)
- `verify_equation(equation, expected, context)` — combined Wolfram + DeepSeek dual check
- `cross_check(claim, models)` — multi-model consensus via reasoning router

---

#### data_access.py (289 lines) — **95% EXTRACTABLE** (remove astro-specific default params)
Query astronomical data archives. Pattern generalizes to any domain with archive APIs.

| Service | Method | Auth |
|---------|--------|------|
| MAST/JWST/HST/TESS | REST: `https://mast.stsci.edu/api/v0/invoke` | None |
| JWST S3 | `s3://stpubdata/jwst/public/{obs_id}/` | None (public) |
| Gaia DR3 | astroquery TAP (sync/async ADQL) | None |
| VizieR | astroquery (20,000+ catalogs) | None |
| NED | astroquery | None |

**Key functions:**
- `search_jwst(target, ra, dec, radius_arcmin, filters, max_results)`
- `search_mast(target, ra, dec, collection, max_results)`
- `search_gaia(ra, dec, radius_deg, max_results, columns)`
- `gaia_adql(query, async_mode)` — arbitrary ADQL queries
- `query_catalog(catalog_id, target, ra, dec, radius_arcmin, max_results)` — any VizieR catalog
- `search_ned(target)` — extragalactic object lookup

---

#### dataset_loaders.py (263 lines) — **80% EXTRACTABLE** (datasets are astro-specific but loader pattern is general)
Stream large datasets from HuggingFace + load from AstroML.

**HuggingFace Multimodal Universe (11 datasets, 100TB total):** plasticc, jwst_ceers, legacysurvey, sdss_spectra, apogee, des, vipers, manga, swift_uvot, chandra_agn, gaia_xp

**AstroML (9 datasets):** sdss_spectra, sdss_specgals, sdss_photometry, rrlyrae, moving_objects, linear_sample, great_wall, dr7_quasar

**Polymathic AI Models (3 models):** walrus (1.3B), aion_base (0.3B), aion_large (3.1B) — physics foundation models on HuggingFace

**Key pattern:** Streaming datasets via `datasets.load_dataset(name, streaming=True, max_samples=N)` — avoids downloading 100TB.

---

#### galaxy_classifier.py (200 lines) — **50% EXTRACTABLE** (vision API classification pattern is general)
Galaxy spin classification via ML encoder + frontier vision APIs.

**Extractable pattern:** Send images to Claude or GPT-4o for structured classification:
- Anthropic: base64 image + text prompt → JSON response
- OpenAI: data: URI + text prompt → JSON response
- Cost: ~$0.01/image
- Zoobot: timm model encoder → embedding → heuristic probe

---

#### galaxy_zoo.py (200 lines), spin_analysis.py (150 lines) — **BIGBOUNCE-SPECIFIC**
These are domain-specific analysis code. The patterns (HEALPix dipole fitting, redshift binning, hierarchical Bayesian models) might inspire similar analysis in other hubs but the code itself is physics-specific.

---

### GPU Infrastructure (research/) — 3 files, ~1,200 lines

#### runpod_cloud.py (541 lines) — **90% EXTRACTABLE** (remove hardcoded pod ID)

Full RunPod pod lifecycle management via GraphQL API.

**API:** `https://api.runpod.io/graphql` with `?api_key=` query param auth

**Current hardcoded default (MUST PARAMETERIZE):**
```python
DEFAULT_POD_ID = "47htajss1ng2ig"  # BigBounce-specific, remove this
```

**Default pod spec:**
- GPU: NVIDIA RTX 6000 Ada Generation (48GB VRAM)
- Image: `runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04`
- Volume: 50GB persistent at `/workspace`
- Container disk: 20GB ephemeral
- Cost: ~$0.74/hr
- SSH: ED25519 key at `~/.ssh/id_ed25519`

**GraphQL operations implemented:**
- `list_pods()` / `get_pod(pod_id)` — status, GPU util, cost, uptime
- `create_pod(gpu_type, name, image, volume_gb, container_disk_gb)` — deploy new pod
- `stop_pod(pod_id)` — pause (keeps volume)
- `start_pod(pod_id)` — resume paused pod
- `terminate_pod(pod_id)` — destroy pod + volume (IRREVERSIBLE)
- `list_gpu_types()` — available GPUs with pricing
- `get_ssh_command(pod_id)` — generate SSH command
- `push_keys(pod_id)` — SCP .env.local to pod
- `run_command(pod_id, cmd)` — SSH exec (120s timeout)
- `setup_pod(pod_id)` — full env bootstrap (pip install, git clone, push keys, validate)

**Setup installs:**
```
transformers datasets astroML astroquery anthropic openai
google-generativeai python-dotenv scipy matplotlib seaborn
huggingface_hub timm cobaya camb healpy getdist requests pandas
```

---

#### runpod_gpu_session.py (524 lines) — **30% EXTRACTABLE** (framework only, cells are project-specific)

**Extractable: Environment detection + key loading + repo cloning pattern**

Platform detection:
1. `/workspace` exists → RunPod (`/workspace/{project}`, `/workspace/outputs`)
2. `/lambda/nfs` exists → Lambda
3. `COLAB_GPU` env var or `/content` exists → Colab
4. Default → Local (finds repo by checking for known subdirectory)

Key loading: .env.local → environment variables → Colab Secrets fallback

**11 session cells are BigBounce-specific** (load Walrus model, query JWST, etc.) but the cell-based session runner pattern is reusable.

---

#### env_check.py (146 lines) — **100% EXTRACTABLE**
API key validation with masked display + optional connectivity testing.

---

### Data Pipelines (scripts/) — 5 files, ~1,100 lines

| File | Lines | Extractable | Description |
|------|-------|-------------|-------------|
| `build_data.py` | ~200 | **80%** | CSV → validated JSON/JSONP/XLSX with meta.yml schema |
| `eb_forecast.py` | ~297 | 0% | CMB birefringence forecast (physics-specific) |
| `download_galaxy_zoo.py` | ~200 | 30% | HF streaming → website JSON (pattern is general) |
| `spin_fit_stan.py` | ~290 | 0% | Stan hierarchical Bayesian model (physics-specific) |
| `figure_checks.py` | ~100 | 50% | CI data integrity validation (pattern is general) |

---

### MCMC / Reproducibility — ~800 lines

| File | Extractable | Description |
|------|-------------|-------------|
| 4 Cobaya YAML configs | 0% | Physics-specific parameter estimation |
| Stan model (in spin_fit_stan.py) | 0% | Physics-specific hierarchical fit |
| `reproduce_cosmology.sh` | 30% | Cobaya runner pattern is reusable |
| `reproduce_spins.sh` | 30% | Stan runner pattern is reusable |
| `mcmc_monitor_v6.py` | 60% | Real-time chain convergence monitor — pattern generalizes to any MCMC |

---

## 2. External API Registry <a name="2-external-apis"></a>

### Complete inventory: 20 service integrations

**LLM APIs (7) — all use chat completions format:**

| # | Service | Auth Method | Env Key | Cost |
|---|---------|-------------|---------|------|
| 1 | Anthropic Claude | `x-api-key` header | `ANTHROPIC_API_KEY` | Per-token |
| 2 | OpenAI GPT | Bearer token | `OPENAI_API_KEY` | Per-token |
| 3 | Google Gemini | `?key=` query param | `GOOGLE_AI_API_KEY` | Free tier available |
| 4 | DeepSeek R1 | Bearer token | `DEEPSEEK_API_KEY` | Per-token (cheap) |
| 5 | xAI Grok | Bearer token | `XAI_API_KEY` | Per-token |
| 6 | OpenRouter | Bearer token | `OPENROUTER_API_KEY` | Per-token |
| 7 | Perplexity | Bearer token | `PERPLEXITY_API_KEY` | Per-token |

**Science & Literature APIs (4):**

| # | Service | Auth Method | Env Key | Cost |
|---|---------|-------------|---------|------|
| 8 | NASA ADS | Bearer token | `NASA_ADS_API_KEY` | Free |
| 9 | Semantic Scholar | `x-api-key` header (optional) | `SEMANTIC_SCHOLAR_API_KEY` | Free |
| 10 | arXiv | None | — | Free (1 req/3s limit) |
| 11 | Wolfram Alpha | `appid` query param | `WOLFRAM_ALPHA_APP_ID` | Free (2K/mo) |

**Data Archives (6) — all free, no auth:**

| # | Service | Method |
|---|---------|--------|
| 12 | MAST (JWST/HST/TESS) | REST API |
| 13 | JWST S3 bucket | `s3://stpubdata/jwst/public/` |
| 14 | Gaia DR3 | astroquery TAP |
| 15 | VizieR (20K+ catalogs) | astroquery |
| 16 | NED | astroquery |
| 17 | Zooniverse | REST API |

**ML & Data (1):**

| # | Service | Auth Method | Env Key |
|---|---------|-------------|---------|
| 18 | HuggingFace Hub | Token (optional) | `HUGGINGFACE_TOKEN` |

**Compute & Web (2):**

| # | Service | Auth Method | Env Key | Cost |
|---|---------|-------------|---------|------|
| 19 | RunPod | `?api_key=` query param | `RUNPOD_API_KEY` | ~$0.74/hr GPU |
| 20 | Firecrawl | Bearer token | `FIRECRAWL_API_KEY` | Paid (not yet used in code) |

### API Key Setup for New Research Hubs

**Required (minimum viable):**
- `ANTHROPIC_API_KEY` — console.anthropic.com
- `NASA_ADS_API_KEY` — ui.adsabs.harvard.edu/user/settings/token (free)

**Recommended for full research capability:**
- `DEEPSEEK_API_KEY` — platform.deepseek.com (math verification)
- `WOLFRAM_ALPHA_APP_ID` — developer.wolframalpha.com (free 2K/mo)
- `HUGGINGFACE_TOKEN` — huggingface.co/settings/tokens (dataset access)
- `PERPLEXITY_API_KEY` — perplexity.ai/settings/api (live web search)
- `RUNPOD_API_KEY` — runpod.io/console/user/settings (GPU compute)

---

## 3. GPU Compute: Setup & Critical Lessons Learned <a name="3-gpu-compute"></a>

### RunPod Architecture

```
Pod Types:
├── On-Demand: ~$0.74/hr for RTX 6000 Ada (48GB VRAM)
├── Spot: Cheaper but can be preempted mid-computation
└── Serverless: Per-second billing, auto-scale

Storage:
├── Container Disk (20GB): EPHEMERAL — lost on pod stop
├── Network Volume (50GB): PERSISTENT across stop/start
│   └── Mounted at /workspace/
│   └── DESTROYED on pod terminate OR billing failure
└── External backup: Must be configured manually (git push, SCP, S3)
```

### CRITICAL LESSONS LEARNED (from BigBounce operations)

**1. Network volumes are destroyed on billing failure.**
MCMC chains take 4-12 hours per configuration to generate. If RunPod billing lapses (card issue, balance runs out), the volume is terminated and ALL data on `/workspace/` is lost. BigBounce experienced this.

**Mitigation that needs to be built into the Labs SDK:**
- Auto-backup after every significant computation completes
- Pre-shutdown backup check before any `stop` or `terminate` operation
- Billing balance monitoring with alerts
- Never store irreplaceable data only on RunPod volumes

**2. Stop vs. Terminate — users confuse these.**
- `stop` = pause pod, volume persists, no GPU billing, small storage cost continues
- `terminate` = destroy everything, volume gone, no cost. IRREVERSIBLE.

BigBounce's current code has a "type yes" confirmation for terminate but no auto-backup before it runs.

**3. Workspace organization matters.**
```
/workspace/                          # RunPod network volume
├── {project}/                       # Git repo (recoverable via clone)
├── outputs/                         # Research results (BACKUP THESE)
│   ├── chains/                      # MCMC chains (4-12h to regenerate each)
│   ├── models/                      # HF model weights (recoverable but slow)
│   └── results/                     # Analysis outputs
├── .env.local                       # API keys (recoverable from local machine)
└── .last_backup                     # Timestamp of last backup (should be tracked)
```

**4. GPU session should be resumable.**
Current BigBounce session runner runs cells 0-11 sequentially. If cell 7 fails, you restart from cell 0. Should support: `--resume-from 7` and checkpoint state between cells.

**5. Pod setup takes ~10 minutes and is fragile.**
pip install of all dependencies on a fresh pod takes time. The Docker image should be customized with pre-installed deps, or a setup script should cache the environment on the network volume.

**6. Snapshot GPU run state for reproducibility.**
BigBounce created `reproducibility/cosmology/archives/gpu_run_snapshot_20260305_0824/MANIFEST.md` documenting: hardware (RTX 6000 Ada, 128 cores, 503Gi RAM), software versions (Cobaya 3.6.1, CAMB 1.6.5), chain counts (28 chains across 4 datasets), convergence status, and config diffs. This pattern should be automated.

---

## 4. Compute Pipelines <a name="4-compute-pipelines"></a>

### MCMC (Cobaya + CAMB)
- 4 dataset configurations (Planck, +BAO, +SN, Full Tension)
- Model: LCDM + ΔN_eff (standard CAMB, no custom modifications)
- Sampler: Metropolis-Hastings with dragging
- Runtime: ~4-12 hours per config on 4 CPU cores (or GPU)
- Convergence: R̂-1 < 0.01 target, burn-in 30%
- Monitor: Real-time convergence tracking with ETA model (3-stage: early/exponential/linear)
- Output: chains/ directory with MCMC samples, convergence CSVs, trace plots

### Stan Hierarchical Bayesian Fit
- Galaxy spin asymmetry A(z) = A₀(1+z)^{-p} e^{-qz}
- Data: Published aggregate CW/CCW counts (Shamir 2024)
- PyStan MCMC: 4 chains, 2000 samples, 1000 warmup
- Runtime: 10-30 minutes
- Output: parameter posteriors, A(z) curves, diagnostic plots

### Figure Generation
- 8 publication figures from inline data (no external deps)
- matplotlib, 300 DPI, seaborn-whitegrid style
- Output: PNG to arxiv/figures/

---

## 5. The `.hubify/` Directory Convention (Proposed) <a name="5-hubify-convention"></a>

**NOTE:** This is a convention proposed based on BigBounce patterns. It does NOT currently exist as a standard. The Hubify team should decide whether to adopt, modify, or replace this.

BigBounce currently has `.hubify/squad-init.md` (24-line markdown stub). The proposed evolution:

```
.hubify/
├── hub.yaml              # Hub identity (name, type, version, visibility, author, tags)
├── squad.yaml            # Agent team (agents with roles, models, capabilities, tools)
├── missions/             # Research mission definitions + state tracking
├── skills/               # Declared capabilities (what this hub's agents can do)
├── knowledge/            # Collective findings (structured claims, results, open questions)
└── context/              # Shared agent memory that persists across sessions
```

Each hub repo would have a `.hubify/` directory. The Hubify platform reads these to:
- Display hub dashboards
- Track mission progress
- Enable cross-hub discovery
- Sync with local CLI tools

---

## 6. What Stays BigBounce-Specific <a name="6-what-stays"></a>

| Stays in BigBounce | Why |
|--------------------|-----|
| `galaxy_zoo.py` | Domain-specific catalog analysis |
| `spin_analysis.py` | Physics-specific spin asymmetry pipeline |
| `eb_forecast.py` | CMB birefringence forecast |
| `spin_fit_stan.py` | Stan model for galaxy spin fit |
| `generate_all_figures.py` | Paper-specific figure generation |
| `cobaya_*.yaml` | Cosmological parameter configs |
| Website HTML (12 pages) | Paper presentation |
| `arxiv/` directory | LaTeX paper source |

| Extracts to Hubify Labs SDK | Why |
|-----------------------------|-----|
| `reasoning_router.py` | Any research hub needs multi-model routing |
| `literature_search.py` | Any research hub needs literature search |
| `computation.py` | Any research hub needs equation verification |
| `data_access.py` | Archive query patterns generalize |
| `dataset_loaders.py` | HuggingFace streaming pattern generalizes |
| `runpod_cloud.py` | Any compute-heavy hub needs GPU management |
| `runpod_gpu_session.py` (framework) | Session runner pattern generalizes |
| `env_check.py` | Universal API key management |
| `build_data.py` (pipeline) | CSV→JSON validation pattern generalizes |
| `galaxy_classifier.py` (vision pattern) | Image classification via LLM generalizes |
| MCMC monitor (pattern) | Convergence monitoring generalizes to any MCMC |

---

## 7. Prompt for Hubify Repo Coding Agent <a name="7-agent-prompt"></a>

Copy-paste the block below into your Hubify repo Claude Code session:

---

> ### Task: Extract BigBounce research infrastructure into Hubify Labs SDK
>
> **Background:** The `Hubify-Projects/bigbounce` repo contains a fully operational research infrastructure (~6,100 lines Python) built for a theoretical physics paper. About 2,700 lines (65%) of this code is general-purpose and should be extracted into a reusable "Hubify Labs SDK" (or "Hubify Research SDK") that allows spinning up new research hubs with the same capabilities.
>
> **Your first step:** Clone or read from the BigBounce repo. The key reference documents are:
> - `project-context/RESEARCH_ARCHITECTURE.md` (998 lines) — Complete technical reference: every function signature, API endpoint, auth method, data flow
> - `project-context/HUBIFY_HANDOFF.md` (this document) — Extraction plan, what's reusable vs. project-specific, operational lessons learned
> - `.env.example` — All 12 API keys with signup URLs and documentation
>
> **IMPORTANT CONTEXT:** This handoff document was written from inside BigBounce with NO visibility into the current Hubify repo structure. Do NOT blindly follow directory structure suggestions — adapt the extractable code to whatever architecture already exists in this project. The document tells you WHAT to extract and WHY, not WHERE to put it.
>
> **What to extract (in priority order):**
>
> 1. **Multi-model reasoning router** (`bigbounce/research/agents/reasoning_router.py`, 300 lines) — Routes prompts to 7 LLMs by task type. 3 provider protocols (OpenAI-compatible, Anthropic, Google). Fully self-contained.
>
> 2. **Literature search** (`bigbounce/research/agents/literature_search.py`, 200 lines) — Unified search across NASA ADS, Semantic Scholar, arXiv, Perplexity. Single `search()` function queries all sources.
>
> 3. **Computation verification** (`bigbounce/research/agents/computation.py`, 252 lines) — Wolfram Alpha + DeepSeek R1 for verifying mathematical claims. Dual-check pattern.
>
> 4. **RunPod GPU management** (`bigbounce/research/runpod_cloud.py`, 541 lines) — Full pod lifecycle via GraphQL. MUST remove hardcoded `DEFAULT_POD_ID = "47htajss1ng2ig"` and parameterize. Read the "Critical Lessons Learned" section in HUBIFY_HANDOFF.md — storage backup/resilience is critical.
>
> 5. **Data access patterns** (`bigbounce/research/agents/data_access.py`, 289 lines) — Archive queries (MAST, Gaia, VizieR, NED). Remove astronomy-specific defaults but keep the query patterns.
>
> 6. **Dataset loader pattern** (`bigbounce/research/agents/dataset_loaders.py`, 263 lines) — HuggingFace streaming + AstroML. The streaming pattern (`load_dataset(name, streaming=True)`) is key.
>
> 7. **Environment/key management** (`bigbounce/research/env_check.py`, 146 lines) — API key validation, masked display, connectivity testing.
>
> 8. **GPU session framework** (`bigbounce/research/runpod_gpu_session.py`, 524 lines) — Extract only: environment detection, key loading, repo cloning pattern. The 11 research cells are BigBounce-specific.
>
> **Critical operational lesson to build into compute layer:**
> RunPod network volumes are DESTROYED on billing failure. MCMC chains take 4-12 hours to regenerate. The SDK MUST include auto-backup before any pod stop/terminate, billing monitoring, and a workspace backup strategy. See HUBIFY_HANDOFF.md section 3 for full details.
>
> **What NOT to extract (stays in BigBounce):**
> - `galaxy_zoo.py`, `spin_analysis.py` — physics-specific
> - `eb_forecast.py`, `spin_fit_stan.py` — physics-specific
> - `generate_all_figures.py` — paper-specific
> - Cobaya YAML configs — cosmology-specific
> - All HTML/website code — paper presentation

---
