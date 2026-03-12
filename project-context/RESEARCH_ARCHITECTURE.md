# BigBounce Research Architecture — Complete Extraction Guide

**Purpose:** Document every research pipeline, external API, compute infrastructure, data flow, and agent system in BigBounce for extraction into the Hubify platform.

**Date:** 2026-03-12
**Version:** v1.3.0 (commit 8c88a1c)

---

## Table of Contents

1. [System Overview](#1-system-overview)
2. [Agent Modules — Complete API Reference](#2-agent-modules)
3. [GPU Compute Infrastructure (RunPod)](#3-gpu-compute)
4. [MCMC Verification Pipeline](#4-mcmc-pipeline)
5. [Data Pipelines](#5-data-pipelines)
6. [External API Registry](#6-external-api-registry)
7. [Dataset Catalog](#7-dataset-catalog)
8. [ML Model Registry](#8-ml-model-registry)
9. [Environment & Authentication](#9-environment)
10. [CI/CD & Deployment](#10-cicd)
11. [Extraction Plan for Hubify](#11-extraction-plan)

---

## 1. System Overview <a name="1-system-overview"></a>

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        ORCHESTRATION LAYER                              │
│  (Currently manual — no orchestrator exists)                           │
│                                                                         │
│  Entry points:                                                          │
│  • research/runpod_gpu_session.py  (11-cell GPU session runner)        │
│  • research/runpod_cloud.py        (pod lifecycle CLI)                 │
│  • scripts/*.py                    (individual pipelines)              │
│  • reproducibility/reproduce_*.sh  (MCMC/Stan runners)                │
└───────┬──────────┬──────────┬──────────┬──────────┬────────────────────┘
        │          │          │          │          │
        ▼          ▼          ▼          ▼          ▼
┌──────────┐┌──────────┐┌──────────┐┌──────────┐┌──────────┐
│ Reasoning ││Literature││Computation│ Data     ││ Galaxy   │
│ Router   ││ Search   ││ Verify   ││ Access   ││ Zoo      │
│          ││          ││          ││          ││          │
│ 7 LLMs   ││ 4 APIs   ││ Wolfram  ││ 5 APIs   ││ 4 cats   │
│          ││          ││ DeepSeek ││          ││ HEALPix  │
└────┬─────┘└────┬─────┘└────┬─────┘└────┬─────┘└────┬─────┘
     │           │           │           │           │
     ▼           ▼           ▼           ▼           ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                        EXTERNAL SERVICES                                │
│                                                                         │
│  LLM APIs:  Anthropic │ OpenAI │ Google │ DeepSeek │ xAI │ Perplexity │
│  Science:   NASA ADS │ Semantic Scholar │ arXiv │ Wolfram Alpha        │
│  Data:      MAST/JWST │ Gaia DR3 │ VizieR │ NED │ HuggingFace        │
│  Compute:   RunPod GPU │ (Colab │ Lambda)                              │
│  ML:        Polymathic AI │ Zoobot │ AstroML                           │
└─────────────────────────────────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                        OUTPUT LAYER                                     │
│                                                                         │
│  research/outputs/     → JSON/markdown research artifacts              │
│  public/data/          → Website-ready JSON/JSONP/XLSX                 │
│  arxiv/figures/        → Publication PNG figures                        │
│  chains/               → MCMC chain samples (generated on RunPod)      │
│  results/              → Stan posterior samples                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### File Inventory

| Directory | Files | Lines | Purpose |
|-----------|-------|-------|---------|
| `research/agents/` | 9 Python modules | ~2,200 | Agent skills (reasoning, search, compute, data) |
| `research/` | 3 Python files | ~1,200 | GPU infrastructure (RunPod, env check) |
| `scripts/` | 5 Python files | ~1,100 | Build & analysis pipelines |
| `reproducibility/` | 4 MCMC configs + Stan + monitor + shell scripts | ~800 | Reproducible science |
| `generate_all_figures.py` | 1 file | ~800 | Publication figure generation |

**Total extractable Python:** ~6,100 lines across 22 files

---

## 2. Agent Modules — Complete API Reference <a name="2-agent-modules"></a>

### 2.1 Reasoning Router (`research/agents/reasoning_router.py`)

**Purpose:** Route prompts to the optimal LLM based on task type.

**Model Registry:**

| Key | Model | Provider | Base URL | Env Key | Strength |
|-----|-------|----------|----------|---------|----------|
| `math_rigor` | `deepseek-reasoner` | DeepSeek | `https://api.deepseek.com/v1` | `DEEPSEEK_API_KEY` | Catches sign errors in tensor math |
| `multimodal` | `gemini-2.5-pro` | Google | `https://generativelanguage.googleapis.com/v1beta` | `GOOGLE_AI_API_KEY` | Images + equations + long-form math |
| `writing` | `claude-opus-4-6` | Anthropic | `https://api.anthropic.com/v1` | `ANTHROPIC_API_KEY` | Academic voice, argument structuring |
| `reasoning` | `gpt-4o` | OpenAI | `https://api.openai.com/v1` | `OPENAI_API_KEY` | High ELO general reasoning |
| `literature` | `sonar-pro` | Perplexity | `https://api.perplexity.ai` | `PERPLEXITY_API_KEY` | Web-grounded live search |
| `fast` | `grok-3` | xAI | `https://api.x.ai/v1` | `XAI_API_KEY` | Fast reasoning |
| `multi` | `anthropic/claude-sonnet-4` | OpenRouter | `https://openrouter.ai/api/v1` | `OPENROUTER_API_KEY` | Multi-model fallback |

**Task Routing Table:**

| Task Keywords | Routes To |
|---------------|-----------|
| `math_rigor`, `tensor_check`, `sign_error`, `derivation` | DeepSeek R1 |
| `multimodal`, `plot_analysis`, `image` | Gemini |
| `writing`, `abstract`, `paper_edit` | Claude Opus |
| `reasoning`, `general` | GPT-4o |
| `literature`, `search`, `recent_papers` | Perplexity |
| `fast`, `quick` | Grok |
| `compare` | OpenRouter |

**Functions:**

```python
# Route single prompt to best model for task
query(prompt: str, task: str = "general", system: str = None,
      model_override: str = None, max_tokens: int = 4096,
      temperature: float = 0.1) -> dict
# Returns: {content, model, usage, provider, task}

# Send same prompt to multiple models for consensus
multi_query(prompt: str, models: list[str] = None, system: str = None,
            max_tokens: int = 4096) -> list[dict]
# Returns: [{content, model, usage, provider, task}, ...]

# List models with configured API keys
available_models() -> dict
```

**Protocol Details:**
- OpenAI-compatible endpoints (DeepSeek, OpenAI, Perplexity, xAI, OpenRouter): Bearer token auth, `/chat/completions`
- Anthropic: `x-api-key` header, `/v1/messages`, `anthropic-version: 2023-06-01`
- Google: API key as query param, `/v1beta/models/{model}:generateContent`
- All calls: 120s timeout, temperature 0.1 default

---

### 2.2 Literature Search (`research/agents/literature_search.py`)

**Purpose:** Unified search across 4 academic literature sources.

**Functions:**

```python
# NASA ADS — astrophysics-specific literature
search_ads(query: str, rows: int = 10, sort: str = "date desc",
           year_range: str = None,
           fields: str = "title,author,year,bibcode,abstract,citation_count,doi") -> list[dict]
ads_citations(bibcode: str, rows: int = 50) -> list[dict]
ads_references(bibcode: str, rows: int = 50) -> list[dict]

# Semantic Scholar — cross-field paper graphs
search_s2(query: str, limit: int = 10,
          fields: str = "title,authors,year,abstract,citationCount,url,externalIds") -> list[dict]
s2_paper(paper_id: str, fields: str = "...") -> dict
s2_citation_graph(paper_id: str, depth: int = 1) -> dict
# Returns: {paper, citations[:50], references[:50]}

# arXiv — latest preprints
search_arxiv(query: str, max_results: int = 10, sort_by: str = "submittedDate",
             category: str = None) -> list[dict]
# Rate limit: 3s sleep enforced between calls

# Perplexity — web-grounded LLM search
search_perplexity(query: str, model: str = "sonar-pro") -> dict
# Returns: {content, model, citations}

# Unified multi-source search
search(query: str, sources: list[str] = None, max_results: int = 5,
       category: str = None) -> dict
# Default sources: ["ads", "arxiv", "s2" (if key), "perplexity" (if key)]
# Returns: {ads: [...], arxiv: [...], s2: [...], perplexity: {...}}

save_results(results: dict, filename: str = None) -> str
```

**API Endpoints:**

| Service | URL | Auth | Timeout | Rate Limit |
|---------|-----|------|---------|------------|
| NASA ADS | `https://api.adsabs.harvard.edu/v1/search/query` | Bearer `NASA_ADS_API_KEY` | 30s | — |
| Semantic Scholar | `https://api.semanticscholar.org/graph/v1/paper/search` | `x-api-key` header (optional) | 30s | — |
| arXiv | `http://export.arxiv.org/api/query` | None | 30s | 1 req/3s |
| Perplexity | `https://api.perplexity.ai/chat/completions` | Bearer `PERPLEXITY_API_KEY` | 60s | — |

---

### 2.3 Computation & Verification (`research/agents/computation.py`)

**Purpose:** Verify mathematical claims using Wolfram Alpha + DeepSeek R1.

**Functions:**

```python
# Wolfram Alpha — symbolic computation
wolfram(query: str, format: str = "full") -> dict
# Formats: "full" (structured pods), "short" (one-line), "llm" (agent-friendly)
# Returns full: {format, success, pods: [{title, text}, ...]}
# Returns short/llm: {answer, format}

wolfram_verify(expression: str, expected: str) -> dict
# Returns: {expression, computed, expected, match: bool}

# DeepSeek R1 — deep mathematical reasoning
deepseek_verify(claim: str, context: str = None, max_tokens: int = 4096) -> dict
# Checks: dimensional consistency, sign errors, index symmetry, approximations
# Returns: {verdict: "CORRECT"|"ERROR FOUND"|"UNCLEAR"|"INCOMPLETE", content, model}

# Combined verification
verify_equation(equation: str, expected: str, context: str = None) -> dict
# Returns: {equation, expected, wolfram: {...}, deepseek: {...}}

# Multi-model consensus
cross_check(claim: str, models: list[str] = None) -> dict
# Default models: ["math_rigor", "reasoning", "writing"]
# Returns: {claim, responses: [...], verdicts: [...], consensus: str}
```

**API Endpoints:**

| Service | URL | Auth | Timeout |
|---------|-----|------|---------|
| Wolfram (short) | `https://api.wolframalpha.com/v1/result` | `appid` query param | 30s |
| Wolfram (full) | `https://api.wolframalpha.com/v2/query` | `appid` query param | 30s |
| Wolfram (LLM) | `https://api.wolframalpha.com/v1/llm-api` | `appid` query param | 30s |
| DeepSeek R1 | `https://api.deepseek.com/v1/chat/completions` | Bearer token | 180s |

---

### 2.4 Data Access (`research/agents/data_access.py`)

**Purpose:** Query astronomical archives (JWST, Gaia, VizieR, NED).

**Functions:**

```python
# JWST / HST / TESS (Space Telescope via MAST)
search_jwst(target: str = None, ra: float = None, dec: float = None,
            radius_arcmin: float = 3, filters: dict = None, max_results: int = 50) -> list[dict]
# Returns: [{obs_id, target_name, instrument, filters, proposal_id, obs_date, exposure_time, ra, dec, dataproduct_type}]

search_mast(target=None, ra=None, dec=None, radius_arcmin=3,
            collection=None, max_results=50) -> list[dict]

jwst_s3_uri(obs_id: str) -> str
# Returns: "s3://stpubdata/jwst/public/{obs_id}/"

mast_api_query(service: str, params: dict) -> dict
# Direct REST: POST https://mast.stsci.edu/api/v0/invoke

# Gaia DR3 (1.8 billion stars)
search_gaia(ra: float, dec: float, radius_deg: float = 0.1,
            max_results: int = 100, columns: str = None) -> list[dict]
# Default columns: source_id, ra, dec, parallax, pmra, pmdec, phot_g_mean_mag, bp_rp, radial_velocity

gaia_adql(query: str, async_mode: bool = False) -> list[dict]
# Run arbitrary ADQL queries against Gaia DR3

# VizieR (20,000+ catalogs)
query_catalog(catalog_id: str, target: str = None, ra: float = None,
              dec: float = None, radius_arcmin: float = 5, max_results: int = 100) -> list[dict]
# Examples: "II/246" (2MASS), "V/147" (SDSS DR12)

# NED (Extragalactic Database)
search_ned(target: str) -> list[dict]

save_data(data, filename: str = None) -> str
```

**API Endpoints:**

| Service | URL/Method | Auth | Notes |
|---------|-----------|------|-------|
| MAST | `https://mast.stsci.edu/api/v0/invoke` | None | 60s timeout |
| JWST S3 | `s3://stpubdata/jwst/public/` | None | Public bucket |
| Gaia DR3 | Via `astroquery.gaia.Gaia` | None | Supports async for large queries |
| VizieR | Via `astroquery.vizier.Vizier` | None | 20,000+ catalogs |
| NED | Via `astroquery.ned.Ned` | None | — |

**Dependencies:** `astroquery`, `astropy`

---

### 2.5 Dataset Loaders (`research/agents/dataset_loaders.py`)

**Purpose:** Load streaming astronomical datasets from HuggingFace and AstroML.

**Functions:**

```python
# HuggingFace Multimodal Universe (100TB total)
load_mmu(name: str, split: str = "train", streaming: bool = True,
         max_samples: int = None) -> Dataset | IterableDataset
list_mmu_datasets() -> dict
mmu_info(name: str) -> dict

# AstroML built-in datasets
load_astroml(name: str, **kwargs) -> np.ndarray
list_astroml_datasets() -> dict

# Polymathic AI foundation models
load_polymathic(model_name: str, device: str = "auto") -> model
list_polymathic_models() -> dict
```

**HuggingFace MMU Dataset Registry:**

| Name | HF ID | Description |
|------|-------|-------------|
| `plasticc` | `MultimodalUniverse/plasticc` | PLAsTiCC supernova light curves |
| `jwst_ceers` | `MultimodalUniverse/jwst` | JWST CEERS galaxy images |
| `legacysurvey` | `MultimodalUniverse/legacysurvey` | Legacy Survey images |
| `sdss_spectra` | `MultimodalUniverse/sdss` | SDSS spectra |
| `apogee` | `MultimodalUniverse/apogee` | APOGEE stellar spectra |
| `des` | `MultimodalUniverse/des` | Dark Energy Survey |
| `vipers` | `MultimodalUniverse/vipers` | VIPERS galaxy spectra |
| `manga` | `MultimodalUniverse/manga` | MaNGA IFU spectroscopy |
| `swift_uvot` | `MultimodalUniverse/swift_uvot_sne` | Swift UVOT supernovae |
| `chandra_agn` | `MultimodalUniverse/chandra_agn` | Chandra AGN X-ray |
| `gaia_xp` | `MultimodalUniverse/gaia_xp` | Gaia XP spectra |

**AstroML Dataset Registry:**

| Name | Function | Description |
|------|----------|-------------|
| `sdss_spectra` | `fetch_sdss_corrected_spectra` | Corrected spectra |
| `sdss_specgals` | `fetch_sdss_specgals` | Spectroscopic galaxies |
| `sdss_photometry` | `fetch_sdss_sspp` | SSPP photometry |
| `rrlyrae` | `fetch_rrlyrae_combined` | RR Lyrae variables |
| `moving_objects` | `fetch_moving_objects` | Solar system objects |
| `great_wall` | `fetch_great_wall` | Great Wall structure |
| `dr7_quasar` | `fetch_dr7_quasar` | DR7 quasar catalog |

---

### 2.6 Galaxy Zoo (`research/agents/galaxy_zoo.py`)

**Purpose:** Galaxy morphology catalogs, spin asymmetry analysis, dipole fitting.

**Constants:**
```python
DIPOLE_DIRECTION = {"l": 52.0, "b": 68.0}  # Galactic coordinates
A0_PAPER = 0.003  # Empirical amplitude at z=0
```

**Functions:**

```python
# VizieR catalog queries
query_gz2(target=None, ra=None, dec=None, radius_arcmin=10, max_results=1000) -> list[dict]
# Catalog: J/MNRAS/435/2835 — 304,122 galaxies

query_gz_decals(target=None, ra=None, dec=None, radius_arcmin=10, max_results=1000) -> list[dict]
# Catalog: J/MNRAS/509/3966 — 314,000 galaxies

# HuggingFace datasets
load_gz_desi(streaming=True, max_samples=None)
# Dataset: "mwalmsley/gz_desi" — 8.67M galaxies

load_tng50_ceers(split="train", max_samples=None)
# Dataset: "StarThomas1002/TNG50-CEERS" — 10K simulated galaxies

# ML classification
load_zoobot_encoder(model_name="convnext_nano")
# Options: convnext_nano (4M), convnext_small (50M), convnext_base (89M), convnext_large (197M)

# Analysis
compute_spin_asymmetry(catalog, z_bins=20, cw_key, ccw_key, z_key) -> dict
# Formula: A(z) = (N_CW - N_CCW) / (N_CW + N_CCW)
# Model:   A(z) = A₀(1+z)^{-p} e^{-qz}
# Returns: {z_centers, asymmetry, errors, n_galaxies, model_fit}

compute_spin_dipole(catalog, nside=16, ra_key, dec_key, cw_key, ccw_key) -> dict
# HEALPix sky map → dipole fit
# Returns: {nside, npix, pixel_values, counts, dipole_direction, dipole_amplitude, monopole}

# Zooniverse citizen science stats
zooniverse_project_stats(project_slug="zookeeper/galaxy-zoo") -> dict
# API: https://www.zooniverse.org/api/projects?slug={slug}

list_gz_datasets() -> dict
save_gz_data(data, filename=None) -> str  # Saves to public/data/galaxy_zoo/
```

---

### 2.7 Spin Analysis Pipeline (`research/agents/spin_analysis.py`)

**Purpose:** End-to-end galaxy spin analysis with paper comparison.

**Constants:** `PAPER_A0 = 0.003`, `PAPER_P = 0.5`, `PAPER_Q = 0.5`, `PAPER_DIPOLE = {"l": 52.0, "b": 68.0}`

**Functions:**

```python
run_spin_analysis(sample_size=100000, z_bins=20, nside=16,
                  classify_ambiguous=False, classifier_method="zoobot",
                  output_dir=None) -> dict
# Full pipeline: load GZ DESI → filter spirals → compute asymmetry → fit dipole → compare
# Saves: public/data/galaxy_zoo/spin_analysis_results.json

compare_with_paper(asymmetry: dict, sky_map: dict) -> dict
# Checks: asymmetry ratio (0.1 < ratio < 10), dipole angular separation (< 30°)

quick_check(n_galaxies=10000) -> dict
# Fast validation with reduced parameters
```

---

### 2.8 Galaxy Classifier (`research/agents/galaxy_classifier.py`)

**Purpose:** Classify galaxy spin direction using ML or vision APIs.

**Functions:**

```python
# Zoobot encoder + heuristic probe
classify_with_zoobot(image_paths: list[str], model_name="convnext_nano",
                     batch_size=32) -> list[dict]
# Returns: [{path, cw_prob, ccw_prob, predicted_direction, embedding_dim, model}]

# Frontier vision model (Claude or GPT-4o)
classify_with_vision_api(image_paths: list[str], provider="anthropic",
                         model=None, max_concurrent=5) -> list[dict]
# Claude: "claude-sonnet-4-20250514", Anthropic API with base64 image
# GPT-4o: "gpt-4o", OpenAI API with data: URI
# Cost: ~$0.01/image
# Returns: [{path, cw_prob, ccw_prob, predicted_direction, confidence, morphology, reasoning}]

# Method comparison
compare_methods(image_paths: list[str], zoobot_model="convnext_nano",
                api_provider="anthropic") -> dict
# Returns: {n_images, zoobot_results, api_results, agreement_rate}
```

---

### 2.9 Data Audit (`research/agents/data_audit.py`)

**Status:** File does not exist (referenced in __init__.py but not implemented).

---

## 3. GPU Compute Infrastructure (RunPod) <a name="3-gpu-compute"></a>

### 3.1 Pod Management (`research/runpod_cloud.py`)

**API:** RunPod GraphQL — `https://api.runpod.io/graphql`
**Auth:** API key as query parameter (`?api_key={key}`)

**Default Pod Configuration:**
```
Pod ID:        47htajss1ng2ig
GPU:           NVIDIA RTX 6000 Ada Generation (48GB VRAM)
Docker Image:  runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04
Volume:        50 GB persistent at /workspace
Container:     20 GB ephemeral
GPU Count:     1
SSH:           Enabled (ED25519 key at ~/.ssh/id_ed25519)
```

**CLI Commands:**

| Command | Action | GraphQL Mutation/Query |
|---------|--------|----------------------|
| `status` | Show pod metrics, GPU util, cost, SSH | `query Pod($podId)` |
| `ssh` | Print SSH command | `query Pod($podId)` → extract port 22 |
| `stop` | Pause pod (saves volume) | `mutation { podStop }` |
| `start` | Resume paused pod | `mutation { podResume }` |
| `setup` | Full environment bootstrap | SSH + pip install + git clone |
| `push-keys` | SCP .env.local to pod | SCP to `/workspace/bigbounce/.env.local` |
| `run <cmd>` | Execute remote command | SSH exec (120s timeout) |
| `gpus` | List available GPU types + pricing | `query GpuTypes` |
| `terminate` | Destroy pod + volume (irreversible) | `mutation { podTerminate }` |

**Setup installs these packages on pod:**
```
transformers datasets astroML astroquery anthropic openai
google-generativeai python-dotenv scipy matplotlib seaborn
huggingface_hub timm cobaya camb healpy getdist requests pandas
```

**GraphQL Operations:**

```graphql
# List all pods
query { myself { pods { id name desiredStatus runtime { uptimeInSeconds gpus { id gpuUtilPercent memoryUtilPercent } ports { ip isIpPublic privatePort publicPort type } } machine { gpuDisplayName } gpuCount vcpuCount memoryInGb volumeInGb containerDiskInGb imageName costPerHr } } }

# Get single pod
query Pod($podId: String!) { pod(input: { podId: $podId }) { ... } }

# Create pod
mutation { podFindAndDeployOnDemand(input: { name: $name, imageName: $image, gpuTypeId: $gpuType, volumeInGb: $volume, containerDiskInGb: $disk, gpuCount: 1, startSsh: true }) { id costPerHr } }

# Lifecycle
mutation { podStop(input: { podId: $podId }) { id desiredStatus } }
mutation { podResume(input: { podId: $podId, gpuCount: 1 }) { id desiredStatus } }
mutation { podTerminate(input: { podId: $podId }) }

# List GPU types
query GpuTypes { gpuTypes { id displayName memoryInGb secureCloud communityCloud lowestPrice(input: { gpuCount: 1 }) { minimumBidPrice uninterruptablePrice } } }
```

---

### 3.2 GPU Session Runner (`research/runpod_gpu_session.py`)

**Purpose:** Execute 11-cell research workflow on GPU pods (RunPod/Colab/Lambda/local).

**Environment Detection Priority:**
1. `/workspace` exists → **RunPod** (`/workspace/bigbounce`, `/workspace/outputs`)
2. `/lambda/nfs` exists → **Lambda** (`/lambda/nfs`)
3. `COLAB_GPU` env var OR `/content` exists → **Colab** (`/content/bigbounce`)
4. Default → **Local** (find repo by checking for `arxiv/` subdirectory)

**Session Cells:**

| Cell | Name | GPU? | What It Does |
|------|------|------|--------------|
| 0 | `verify_environment` | No | Print platform, GPU name, VRAM, workspace paths |
| 1 | `load_keys` | No | Load .env.local (or Colab Secrets fallback), display masked keys |
| 2 | `clone_repo` | No | `git clone https://github.com/Hubify-Projects/bigbounce.git` if needed |
| 3 | `import_agents` | No | Import all research agent modules, verify availability |
| 4 | `load_walrus` | **Yes (4GB+)** | Load Polymathic AI Walrus 1.3B model (pytorch_model.bin or safetensors) |
| 5 | `plasticc` | No* | Stream 100 PLAsTiCC light curves via HuggingFace |
| 6 | `jwst_ceers` | No* | Stream 10 JWST CEERS galaxy images via HuggingFace |
| 7 | `sdss_spectra` | No | Load SDSS spectra via AstroML |
| 8 | `jwst_query` | No | Query JWST observations of NGC 1365 (5 arcmin radius) |
| 9 | `gaia` | No | Query Gaia DR3 at Galactic Center (ra=266.4, dec=-29.0) |
| 10 | `cmb_parity` | No | Query MAST for Planck collection |
| 11 | `deepseek_verify` | No | Verify inflationary suppression factor equation with DeepSeek R1 |

*Streaming datasets benefit from GPU for processing but don't require it for loading.

**Output:** JSON session report saved as `gpu_session_{YYYYMMDD_HHMMSS}.json` to workspace outputs directory.

**CLI:** `python3 research/runpod_gpu_session.py [cell_numbers...]`

---

## 4. MCMC Verification Pipeline <a name="4-mcmc-pipeline"></a>

### 4.1 Cosmological MCMC (Cobaya + CAMB)

**Location:** `reproducibility/cosmology/`

**Model:** LCDM + ΔN_eff (standard CAMB, N_eff as free parameter)
**Sampler:** Metropolis-Hastings MCMC with dragging
**Theory code:** Stock CAMB v1.5+ (no custom modifications)

**4 Dataset Configurations:**

| Config | Likelihoods | Key Constraint |
|--------|-------------|----------------|
| `cobaya_planck.yaml` | Planck TT+TE+EE+lensing | CMB only |
| `cobaya_planck_bao.yaml` | + 6dFGS, SDSS DR7/DR16 BAO | + geometric distances |
| `cobaya_planck_bao_sn.yaml` | + Pantheon+ SNe | + luminosity distances |
| `cobaya_full_tension.yaml` | + SH0ES H₀ prior + DES Y3 S₈ Gaussian | Full tension test |

**Sampled Parameters:**

| Parameter | Prior | Reference | Proposal |
|-----------|-------|-----------|----------|
| `logA` | [1.61, 3.91] | N(3.044, 0.014) | 0.001 |
| `ns` | [0.8, 1.2] | N(0.9649, 0.0042) | 0.002 |
| `theta_MC_100` | [0.5, 10] | N(1.04092, 0.00031) | 0.0002 |
| `ombh2` | [0.005, 0.1] | N(0.02237, 0.00015) | 0.0001 |
| `omch2` | [0.001, 0.99] | N(0.1200, 0.0012) | 0.0005 |
| `tau` | [0.01, 0.8] | N(0.054, 0.007) | 0.003 |
| `nnu` | [2.046, 5.046] | N(3.346, 0.2) | 0.05 |

**Derived Parameters:** `delta_neff = nnu - 3.046`, `sigma8`, `S8 = sigma8*sqrt(omegam/0.3)`, `omegam`, `H0`, `age`

**DES Y3 S₈ prior (full_tension only):**
```python
S8_DES: external: "lambda sigma8, omegam: stats.norm.logpdf(sigma8*np.sqrt(omegam/0.3), loc=0.776, scale=0.017)"
```

**Convergence criteria:** `Rminus1_stop: 0.01`, `Rminus1_cl_stop: 0.2`, `burn_in: 0.3`
**Runtime:** ~4-12 hours per config on 4 CPU cores
**Output:** `chains/{dataset}/spin_torsion.*` files

**Prerequisites:**
```bash
pip install cobaya==3.5.4
cobaya-install cosmo -p ./packages
```

**Latest Results (from mcmc_results_latest.txt):**

| Dataset | Chains | Effective Samples | H₀ | ΔN_eff | SH0ES Tension |
|---------|--------|-------------------|-----|--------|---------------|
| Planck Only | 7 | 2,850 | 68.94 ± 1.49 | 0.164 ± 0.159 (1.03σ) | 2.25σ |
| Planck+BAO | 7 | 3,139 | 68.72 ± 1.07 | 0.168 ± 0.111 (1.51σ) | 2.90σ |
| Planck+BAO+SN | 7 | 3,232 | 68.49 ± 1.34 | 0.135 ± 0.134 (1.00σ) | 2.68σ |
| Full Tension | 7 | 7,891 | 68.67 ± 0.64 | 0.129 ± 0.076 (1.69σ) | 3.58σ |

---

### 4.2 MCMC Monitor (`reproducibility/cosmology/archives/gpu_run_snapshot_20260305_0824/mcmc_monitor_v6.py`)

**Purpose:** Read-only monitoring of running MCMC chains on RunPod GPU.

**Config:**
```python
CHAINS_DIR    = "/workspace/bigbounce/reproducibility/chains"
OUT_DIR       = "/workspace/bigbounce/reproducibility/cosmology"
DATASETS      = ["planck_only", "planck_bao", "planck_bao_sn", "full_tension"]
CORE_PARAMS   = ["H0", "delta_neff", "omegam", "ombh2", "ns", "tau", "sigma8"]
TARGET        = 0.01     # R̂-1 target
TARGET_TAU    = 0.02     # relaxed for tau
DRIFT_THRESH  = 0.2      # sigma units
MIN_HISTORY_H = 24       # hours before computing ETA
OUTLIER_THRESH = 1.0     # sigma for per-chain outlier detection
```

**Outputs:**
- `status_latest.txt` — Current chain status summary
- `convergence_latest.csv` — R̂, ESS, drift per parameter per dataset
- `chain_means_latest.csv` — Per-chain parameter means
- `bottlenecks_latest.txt` — Top 3 bottleneck parameters per dataset
- `freeze_check.txt` — Chain freeze detection
- `trend_monitor_latest.txt` — Convergence trends
- `trace_*.png` — Trace plots for H₀, ΔN_eff

**ETA Model:**
- Stage A: R̂-1 > 0.3 → "EARLY MIXING", no ETA
- Stage B: 0.3 ≥ R̂-1 > 0.05 → exponential decay fit (12-24h window)
- Stage C: R̂-1 ≤ 0.05 → linear ETA (near-convergence)

---

### 4.3 Galaxy Spin Hierarchical Bayesian Fit (Stan)

**Location:** `reproducibility/galaxy_spins/spin_fit_stan.py`

**Tool:** PyStan (Stan probabilistic programming language)
**Data source:** Published aggregate CW/CCW counts from Shamir (2024), arXiv:2401.09450

**Stan Model Structure:**
```
Data:        S surveys, B total bins, redshift centers, CW/CCW counts, selection weights
Parameters:  A₀ ∈ [0, 0.02], p ∈ [0, 2], q ∈ [0, 2], survey offsets δ, label-noise ε
Model:       A(z) = A₀(1+z)^{-p} e^{-qz}
             π = 0.5(1 + δ + b·A(z)), corrected for label noise
Likelihood:  Binomial(N_cw | N, π_corrected)
Priors:      δ ~ N(0, σ_δ), ε ~ Beta(2, 20)
```

**Pipeline:**
1. `load_spin_data(csv_path)` — Parse verified aggregate counts
2. `prepare_stan_data(df, sigma_delta=0.02)` — Format for Stan
3. `run_mcmc(data, n_chains=4, n_samples=2000, n_warmup=1000)` — Stan MCMC
4. `extract_results(fit, df)` — ArviZ summary + A(z) posterior
5. `plot_results(results, df, output_path)` — Diagnostic plots
6. `save_results(results, output_dir)` — CSV export

**Runtime:** 10-30 minutes on modern laptop
**Dependencies:** `stan`, `arviz`, `pandas`, `numpy`, `matplotlib`

---

## 5. Data Pipelines <a name="5-data-pipelines"></a>

### 5.1 Figure Data Builder (`scripts/build_data.py`)

**Purpose:** Convert CSV research data → validated JSON + JSONP + Excel for web consumption.

**Process:**
1. Scan `data/figures/` for subdirectories with `meta.yml` configs
2. Read CSV data files referenced in each meta.yml
3. Validate against schema (required columns, types, ranges, formulas)
4. Output:
   - `public/data/figure_{id}/{panel_id}.json` — Raw JSON with metadata
   - `public/data/figure_{id}/{panel_id}.js` — JSONP: `window.__FIG_DATA__[key] = {...}`
   - `public/downloads/figure_{id}.xlsx` — Excel workbook with data + README sheet

**Data Figures:**

| Figure | Panels | Description |
|--------|--------|-------------|
| `figure_2` | `panel_a` | Galaxy spin asymmetry across surveys |
| `figure_3a` | `panel_a` | H₀ tension resolution |
| `figure_3b` | `panel_a` | Comprehensive tension (H₀ + σ₈) |
| `figure_6` | `panel_c`, `panel_d` | Parameter naturalness (RG running + fine-tuning) |
| `figure_7` | `panel_c` | Detection significance forecast |

**CI:** `.github/workflows/build-data.yml` runs on push to main + PRs. Uploads artifacts.

---

### 5.2 E-B Forecast (`scripts/eb_forecast.py`)

**Purpose:** CMB birefringence detection significance forecast.

**Process:**
1. Load theory EE spectrum
2. Load instrument specs (noise, beam, f_sky)
3. Compute C_ℓ^EB ≈ 2β·C_ℓ^EE for birefringence angles 0°-0.5°
4. Compute per-bin variance and SNR
5. Compare experiments: Planck, LiteBIRD, CMB-S4, AliCPT

**Config:** `config/eb_forecast_params.yml`
**Output:** `eb_forecast_binned.csv`, `eb_forecast_summary.csv`, plots

---

### 5.3 Galaxy Zoo Download (`scripts/download_galaxy_zoo.py`)

**Purpose:** Stream GZ DESI catalog → compute spin asymmetry → generate website JSON.

**Output:** `public/data/galaxy_zoo/` (JSON for interactive explorer)

---

### 5.4 Publication Figures (`generate_all_figures.py`)

**Purpose:** Generate all 8 paper figures from inline data.

**Figures:**
1. LQG-Holst derivation chain (conceptual flowchart)
2. Galaxy spin asymmetry (multi-survey data)
3a. H₀ tension resolution
3b. Comprehensive tension resolution (H₀ + σ₈)
4. Distance impact of Λ_eff modification
5. Rotation component effect on H(z)
6. Parameter naturalness (RG running + fine-tuning)
7. Observational detection timeline
8. Detection significance forecast

**Output:** PNG → `arxiv/figures/` (300 DPI, seaborn-whitegrid style)
**Dependencies:** matplotlib, numpy (no external data dependencies)

---

## 6. External API Registry <a name="6-external-api-registry"></a>

### Complete API Inventory

| # | Service | Category | Endpoint | Auth Method | Env Key | Required? | Rate Limit | Cost |
|---|---------|----------|----------|-------------|---------|-----------|------------|------|
| 1 | **Anthropic Claude** | LLM | `https://api.anthropic.com/v1/messages` | `x-api-key` header | `ANTHROPIC_API_KEY` | **Yes** | — | Per-token |
| 2 | **OpenAI GPT** | LLM | `https://api.openai.com/v1/chat/completions` | Bearer token | `OPENAI_API_KEY` | No | — | Per-token |
| 3 | **Google Gemini** | LLM | `https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent` | `?key=` query param | `GOOGLE_AI_API_KEY` | No | — | Per-token |
| 4 | **DeepSeek R1** | LLM | `https://api.deepseek.com/v1/chat/completions` | Bearer token | `DEEPSEEK_API_KEY` | No | — | Per-token |
| 5 | **xAI Grok** | LLM | `https://api.x.ai/v1/chat/completions` | Bearer token | `XAI_API_KEY` | No | — | Per-token |
| 6 | **OpenRouter** | LLM | `https://openrouter.ai/api/v1/chat/completions` | Bearer token | `OPENROUTER_API_KEY` | No | — | Per-token |
| 7 | **Perplexity** | LLM/Search | `https://api.perplexity.ai/chat/completions` | Bearer token | `PERPLEXITY_API_KEY` | No | — | Per-token |
| 8 | **NASA ADS** | Literature | `https://api.adsabs.harvard.edu/v1/search/query` | Bearer token | `NASA_ADS_API_KEY` | **Yes** | — | Free |
| 9 | **Semantic Scholar** | Literature | `https://api.semanticscholar.org/graph/v1/paper/search` | `x-api-key` header | `SEMANTIC_SCHOLAR_API_KEY` | No | — | Free |
| 10 | **arXiv** | Literature | `http://export.arxiv.org/api/query` | None | — | — | 1 req/3s | Free |
| 11 | **Wolfram Alpha** | Compute | `https://api.wolframalpha.com/v{1,2}/{result,query,llm-api}` | `appid` query param | `WOLFRAM_ALPHA_APP_ID` | No | 2,000/mo free | Free tier |
| 12 | **MAST/JWST** | Data | `https://mast.stsci.edu/api/v0/invoke` | None | — | — | — | Free |
| 13 | **JWST S3** | Data | `s3://stpubdata/jwst/public/` | None | — | — | — | Free |
| 14 | **Gaia DR3** | Data | Via astroquery (TAP) | None | — | — | — | Free |
| 15 | **VizieR** | Data | Via astroquery | None | — | — | — | Free |
| 16 | **NED** | Data | Via astroquery | None | — | — | — | Free |
| 17 | **HuggingFace Hub** | Data/ML | Hub API | Token (optional) | `HUGGINGFACE_TOKEN` | No | — | Free |
| 18 | **Zooniverse** | Data | `https://www.zooniverse.org/api/projects` | None | — | — | — | Free |
| 19 | **RunPod** | Compute | `https://api.runpod.io/graphql` | `?api_key=` query param | `RUNPOD_API_KEY` | No | — | ~$0.76/hr GPU |
| 20 | **Firecrawl** | Web | (not yet used in code) | Bearer token | `FIRECRAWL_API_KEY` | No | — | Paid |

**Total: 20 external service integrations, 12 requiring API keys**

---

## 7. Dataset Catalog <a name="7-dataset-catalog"></a>

### Accessible Datasets (30+ sources)

**HuggingFace Multimodal Universe (streaming, 100TB total):**
- PLAsTiCC, JWST CEERS, Legacy Survey, SDSS spectra, APOGEE, DES, VIPERS, MaNGA, Swift UVOT, Chandra AGN, Gaia XP

**HuggingFace Galaxy Zoo:**
- GZ DESI (8.67M galaxies), TNG50-CEERS (10K simulated)

**VizieR Catalogs:**
- Galaxy Zoo 2 (304K), Galaxy Zoo DECaLS (314K), 2MASS, SDSS DR12, 20,000+ more

**Space Telescope Archives:**
- JWST observations (via MAST), HST, TESS, Kepler, Planck

**Stellar Catalogs:**
- Gaia DR3 (1.8B stars, supports ADQL queries)

**Extragalactic:**
- NED (redshifts, classifications)

**AstroML Built-in:**
- SDSS spectra, photometry, spectroscopic galaxies, RR Lyrae, quasars, solar system objects

---

## 8. ML Model Registry <a name="8-ml-model-registry"></a>

| Model | HF ID | Parameters | GPU Required | VRAM | Purpose |
|-------|-------|------------|--------------|------|---------|
| Walrus | `polymathic-ai/walrus` | 1.3B | Yes | 4+ GB | Physics foundation model |
| AION Base | `polymathic-ai/aion-base` | 0.3B | Yes | 2+ GB | Astronomical omnimodal network |
| AION Large | `polymathic-ai/aion-large` | 3.1B | Yes | 8+ GB | Astronomical omnimodal network |
| Zoobot Nano | `mwalmsley/zoobot-encoder-convnext_nano` | 4M | No | — | Galaxy morphology encoder |
| Zoobot Small | `mwalmsley/zoobot-encoder-convnext_small` | 50M | No | — | Galaxy morphology encoder |
| Zoobot Base | `mwalmsley/zoobot-encoder-convnext_base` | 89M | No | — | Galaxy morphology encoder |
| Zoobot Large | `mwalmsley/zoobot-encoder-convnext_large` | 197M | Optional | — | Galaxy morphology encoder |

---

## 9. Environment & Authentication <a name="9-environment"></a>

### API Key Management

**Storage:** `.env.local` (gitignored, loaded by python-dotenv)
**Template:** `.env.example` (93 lines, well-documented)

**Key hierarchy:**
1. `.env.local` in project root (primary)
2. Environment variables (fallback)
3. Google Colab Secrets (Colab-only fallback for HF_TOKEN, ANTHROPIC, GOOGLE, DEEPSEEK)

**Required keys (2):** `ANTHROPIC_API_KEY`, `NASA_ADS_API_KEY`
**Optional keys (10):** OPENAI, GOOGLE_AI, DEEPSEEK, XAI, OPENROUTER, SEMANTIC_SCHOLAR, PERPLEXITY, WOLFRAM_ALPHA, HUGGINGFACE, FIRECRAWL

**Validation:** `python3 research/env_check.py [--test]`
- Lists all configured/missing keys
- `--test` flag: connectivity test for Anthropic (claude-haiku-4-5) and NASA ADS

### Hybrid Model Note

From `.env.example`:
> "Keys here are used directly by local research scripts. Hubify Convex backend has its own keys for workspace agents. This keeps BigBounce research independent of Hubify infra."

**Current reality:** No Convex integration code exists. The "Hubify Convex backend" is aspirational.

---

## 10. CI/CD & Deployment <a name="10-cicd"></a>

### GitHub Actions

**`.github/workflows/build-data.yml`:**
- Triggers: push to main, pull requests
- Steps: checkout → Python 3.11 → pip install requirements.txt → python scripts/build_data.py
- Artifacts: `public/data/` + `public/downloads/`
- **Note:** Does not auto-deploy — artifacts are uploaded but not pushed

### Deployment (Vercel — Active)

**`vercel.json`:**
- URL rewrites for clean paths
- Live at: bigbounce.hubify.app

### Deployment (Netlify — Inactive/Redundant)

**`netlify.toml`:**
- No build command, publish from root
- Security headers (X-Frame-Options, XSS protection, etc.)
- Asset caching (1 year for /public/*)
- SPA fallback (404 → index.html)

### Local Dev

**`server.js`:** Express.js static file server on port 3003

---

## 11. Extraction Plan for Hubify <a name="11-extraction-plan"></a>

### What's Reusable vs. Project-Specific

| Component | Lines | Reusable? | Extraction Path |
|-----------|-------|-----------|-----------------|
| **reasoning_router.py** | 300 | **100% reusable** | → `hubify-sdk/agents/router.py` |
| **literature_search.py** | 200 | **100% reusable** | → `hubify-sdk/skills/literature.py` |
| **computation.py** | 252 | **100% reusable** | → `hubify-sdk/skills/computation.py` |
| **data_access.py** | 289 | **95% reusable** (remove astro-specific defaults) | → `hubify-sdk/skills/data_access.py` |
| **dataset_loaders.py** | 263 | **80% reusable** (datasets are astro-specific but pattern is general) | → `hubify-sdk/skills/dataset_loader.py` |
| **galaxy_zoo.py** | 200 | **20% reusable** (analysis logic is domain-specific) | → stays in BigBounce |
| **spin_analysis.py** | 150 | **0% reusable** (BigBounce-specific) | → stays in BigBounce |
| **galaxy_classifier.py** | 200 | **50% reusable** (vision API pattern is general) | → `hubify-sdk/skills/vision_classify.py` |
| **runpod_cloud.py** | 541 | **90% reusable** (remove hardcoded pod ID) | → `hubify-sdk/compute/runpod.py` |
| **runpod_gpu_session.py** | 524 | **30% reusable** (session runner pattern, cells are project-specific) | → `hubify-sdk/compute/gpu_session.py` (framework only) |
| **env_check.py** | 146 | **100% reusable** | → `hubify-sdk/config/env_check.py` |
| **build_data.py** | 200 | **80% reusable** (CSV→JSON pipeline pattern) | → `hubify-sdk/data/builder.py` |
| **eb_forecast.py** | 297 | **0% reusable** (physics-specific) | → stays in BigBounce |
| **spin_fit_stan.py** | 290 | **0% reusable** (model-specific) | → stays in BigBounce |
| **generate_all_figures.py** | 800 | **0% reusable** (figure-specific) | → stays in BigBounce |

**Summary:** ~2,700 lines (65%) are directly extractable into a Hubify SDK. ~1,400 lines are BigBounce-specific science code.

### Proposed Hubify SDK Structure

```
hubify-sdk/
├── agents/
│   ├── router.py              # Multi-model reasoning router (from reasoning_router.py)
│   ├── orchestrator.py        # NEW: Mission runner
│   └── memory.py              # NEW: Session state/learning
├── skills/
│   ├── literature.py          # Literature search (from literature_search.py)
│   ├── computation.py         # Wolfram + DeepSeek verify (from computation.py)
│   ├── data_access.py         # Archive queries (from data_access.py)
│   ├── dataset_loader.py      # HuggingFace + AstroML (from dataset_loaders.py)
│   └── vision_classify.py     # Vision API classification (from galaxy_classifier.py)
├── compute/
│   ├── runpod.py              # RunPod pod management (from runpod_cloud.py)
│   ├── gpu_session.py         # GPU session framework (from runpod_gpu_session.py)
│   └── providers.py           # NEW: Multi-cloud abstraction (RunPod, Lambda, Colab)
├── config/
│   ├── env_check.py           # Environment validation (from env_check.py)
│   └── keys.py                # API key management
├── data/
│   ├── builder.py             # CSV→JSON pipeline (from build_data.py)
│   └── catalog.py             # NEW: Dataset registry
└── hub/
    ├── manifest.py            # NEW: .hubify/ directory management
    ├── knowledge.py           # NEW: Claims/findings/questions YAML management
    └── missions.py            # NEW: Mission state tracking
```

### What Needs to Be Built (Not in BigBounce)

| Component | Purpose | Priority |
|-----------|---------|----------|
| **Orchestrator** | Sequence skills into missions, manage state, handle failures | P0 |
| **Agent Memory** | Persist learnings across sessions, shared context | P1 |
| **Mission State** | Track mission progress (pending/active/completed/failed) | P1 |
| **Hub Manifest** | Parse/manage .hubify/ directory convention | P1 |
| **Knowledge Layer** | CRUD for claims.yaml, findings.yaml, questions.yaml | P1 |
| **Multi-Cloud Compute** | Abstract RunPod/Lambda/Colab behind single interface | P2 |
| **Dataset Catalog** | Register + discover datasets across hubs | P2 |
| **Hubify CLI** | `hubify init`, `hubify sync`, `hubify deploy` | P2 |
| **Site Builder** | Knowledge layer → static site generation | P3 |
| **Hub Discovery** | Index of all Hubify Hubs, search, browse | P3 |

---

## Appendix A: Python Dependencies

### requirements.txt (CI/build)
```
pandas
xlsxwriter
pyyaml
python-dotenv
anthropic
requests
```

### Full research environment (RunPod setup)
```
transformers datasets astroML astroquery anthropic openai
google-generativeai python-dotenv scipy matplotlib seaborn
huggingface_hub timm cobaya camb healpy getdist requests pandas
```

### MCMC-specific
```
cobaya==3.5.4          # MCMC sampler
camb                   # Boltzmann solver (installed via cobaya)
getdist                # Chain analysis
```

### Stan-specific
```
stan                   # PyStan (Stan MCMC)
arviz                  # Bayesian analysis
```

---

## Appendix B: Known Reproducibility Gaps

1. **No custom CAMB modifications** — MCMC uses stock CAMB with N_eff parameter, not a custom spin-torsion theory module
2. **No pre-computed MCMC chains** — Must generate (~4-12h per config, ~1GB per run)
3. **No Bayes factors** — Would require PolyChord nested sampling (~10x cost)
4. **No CNN galaxy classifier** — Hierarchical fit uses published catalog counts, not CNN outputs
5. **No CMB EB/TB from maps** — All birefringence values are literature citations

---

## Appendix C: Hardcoded Values to Parameterize

| Value | Location | Purpose |
|-------|----------|---------|
| `47htajss1ng2ig` | runpod_cloud.py:16 | Default RunPod pod ID |
| `"houston"` | index.html | Client-side password |
| `3003` | server.js | Express port |
| `https://github.com/Hubify-Projects/bigbounce.git` | runpod_gpu_session.py | Repo clone URL |
| `/workspace/bigbounce` | runpod_gpu_session.py, mcmc_monitor_v6.py | RunPod workspace path |
| `DIPOLE_DIRECTION = {"l": 52.0, "b": 68.0}` | galaxy_zoo.py | Paper-specific physics constant |
| `A0_PAPER = 0.003` | galaxy_zoo.py, spin_analysis.py | Paper-specific result |
