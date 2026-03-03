# BigBounce Research Tools Integration Plan

**Created:** 2026-03-03
**Updated:** 2026-03-03
**Status:** Phase 1 COMPLETE, Phase 2 in progress
**Goal:** Integrate all relevant science/AI tools for autonomous and assisted research on the BigBounce paper and future physics work.

---

## Integration Summary

| # | Tool | Type | API? | Key? | Status | Who |
|---|------|------|------|------|--------|-----|
| **LLM / Deep Reasoning** |
| 1 | Anthropic Claude | REST API | Yes | Have | READY | Claude can integrate |
| 2 | OpenAI GPT | REST API | Yes | Have | READY | Claude can integrate |
| 3 | Google Gemini (Deep Think) | REST API | Yes | Have | READY | Claude can integrate |
| 4 | DeepSeek R1 | REST API | Yes | Have | READY | Claude can integrate |
| 5 | xAI Grok | REST API | Yes | Have | READY | Claude can integrate |
| 6 | OpenRouter (multi-model) | REST API | Yes | Have | READY | Claude can integrate |
| 7 | Perplexity (web-grounded) | REST API | Yes | Have | READY | Claude can integrate |
| **Science & Literature** |
| 8 | NASA ADS | REST API | Yes | Have | READY | Claude can integrate |
| 9 | Semantic Scholar | REST API | Yes | Pending | WAITING | Houston: submit form |
| 10 | arXiv | REST API | No key | Free | READY | Claude can integrate |
| 11 | MAST Archive (JWST/HST) | REST + Python | Optional | Free | READY | Claude can integrate |
| 12 | Gaia DR3 | TAP+ / Python | Optional | Free | READY | Claude can integrate |
| 13 | Wolfram Alpha | REST API | AppID | Have | READY | Claude can integrate |
| **Data & Models** |
| 14 | Multimodal Universe (MMU) | HuggingFace | HF token | Have | READY | Claude can integrate |
| 15 | Polymathic AI (Walrus/AION-1) | HuggingFace | HF token | Have | NEEDS GPU | Houston: cloud GPU |
| 16 | AstroML | Python lib | No key | Free | READY | Claude can integrate |
| 17 | Astroquery | Python lib | No key | Free | READY | Claude can integrate |
| 18 | Jdaviz | Python lib | No key | Free | READY | Claude can install |
| **Formal Verification** |
| 19 | Lean 4 + Mathlib | Local install | No key | Free | INSTALLED (v4.28.0) | Done |
| 20 | AlphaProof | CLOSED | N/A | N/A | UNAVAILABLE | Not released by Google |
| **Web-Only Tools (Manual Use)** |
| 21 | ResearchRabbit | Web only | No API | Free | MANUAL | Houston: use browser |
| 22 | Consensus | Web (API waitlisted) | Waitlisted | TBD | MANUAL (+waitlist) | Houston: join waitlist |
| 23 | SciSpace | Web only | No API | Free | MANUAL | Houston: use browser |
| 24 | Elicit | Web (API enterprise) | Enterprise | Paid | MANUAL | Houston: web use |
| 25 | NotebookLM | Web (API alpha) | Enterprise | Paid | MANUAL | Houston: upload PDFs |
| 26 | Paperpal | Web only | No API | Free tier | MANUAL | Houston: use browser |
| 27 | Trinka | Web (API enterprise) | Enterprise | Paid | MANUAL | Houston: use browser |
| 28 | NASA Fornax | Cloud JupyterLab | Registration | Free | NEEDS SIGNUP | Houston: register |
| 29 | SciCode | Benchmark (not tool) | N/A | N/A | REFERENCE | N/A |

---

## Phase 1: Claude Can Integrate Now (Local Scripts)

These have API keys ready and can be wired into Python research scripts immediately.

### 1.1 Multi-Model Reasoning Router

**File:** `research/agents/reasoning_router.py`

A unified interface that routes research questions to the best model based on task type.

```
Task Type → Model
─────────────────────────────────
Tensor derivation check    → DeepSeek R1 (highest math rigor)
Multimodal analysis        → Gemini Deep Think (images + math)
Scientific writing         → Claude Opus (academic voice)
General reasoning          → GPT / OpenRouter (high ELO)
Live literature search     → Perplexity (web-grounded)
Quick computation          → Wolfram Alpha (exact answers)
Alternative perspective    → Grok (fast, different angle)
```

**Keys needed:** All 7 LLM keys (have all)
**Effort:** ~200 lines Python. OpenAI-compatible format for most.

### 1.2 Literature Search Pipeline

**File:** `research/agents/literature_search.py`

Unified search across NASA ADS + Semantic Scholar + arXiv.

| Endpoint | Use Case |
|----------|----------|
| NASA ADS `/search/query` | Citation-aware astrophysics search |
| Semantic Scholar `/paper/search` | Cross-field discovery, citation graphs |
| arXiv API | Latest preprints, category filtering |
| Perplexity `sonar-pro` | Natural language research questions |

**Keys needed:** NASA_ADS (have), SEMANTIC_SCHOLAR (pending), arXiv (free)
**Effort:** ~150 lines Python

### 1.3 Computation & Verification

**File:** `research/agents/computation.py`

| Tool | Use Case |
|------|----------|
| Wolfram Alpha Full Results API | Verify equations, unit conversions, integrals |
| Wolfram Alpha LLM API | Agent-friendly natural language math |
| DeepSeek R1 | Cross-check tensor derivations |

**Keys needed:** WOLFRAM_ALPHA_APP_ID (have), DEEPSEEK_API_KEY (have)
**Effort:** ~100 lines Python

### 1.4 Astronomical Data Access

**File:** `research/agents/data_access.py`

| Source | Access Method | Data |
|--------|---------------|------|
| MAST Archive | `astroquery.mast` | JWST, HST, TESS observations |
| Gaia DR3 | `astroquery.gaia` | 1.8B stars, parallax, proper motion |
| SDSS | `astroquery.sdss` | Galaxy spectra, photometry |
| VizieR | `astroquery.vizier` | 20,000+ catalogs |
| NED | `astroquery.ned` | Extragalactic distances, redshifts |

**Keys needed:** None (all free/anonymous)
**Effort:** ~200 lines Python. Requires `pip install astroquery`.

### 1.5 Dataset Loaders (MMU + AstroML)

**File:** `research/agents/dataset_loaders.py`

| Dataset | Access | Size |
|---------|--------|------|
| MMU PLAsTiCC | `load_dataset('MultimodalUniverse/plasticc', streaming=True)` | Light curves |
| MMU Legacy Survey | `load_dataset('MultimodalUniverse/legacysurvey', streaming=True)` | Galaxy images |
| MMU APOGEE | `load_dataset('MultimodalUniverse/apogee', streaming=True)` | Spectra |
| AstroML SDSS | `astroML.datasets.fetch_sdss_spectra()` | Local spectra |

**Keys needed:** HUGGINGFACE_TOKEN (have)
**Effort:** ~100 lines Python. Requires `pip install datasets astroML`.

---

## Phase 2: Houston Action Required

### 2.1 Semantic Scholar API Key
- **Status:** Form submitted, awaiting approval
- **Action:** Paste key into `.env.local` when received
- **Impact:** Enables citation graph analysis, paper recommendations

### 2.2 NASA Fornax Registration
- **URL:** https://fornax.sciencecloud.nasa.gov/
- **Action:** Register with NASA credentials (free)
- **What you get:** Free JupyterLab with direct JWST/Hubble/Chandra data access
- **Compute tiers:** Up to 512GB RAM / 128 CPU (free!)
- **Impact:** Run MCMC chains co-located with data (no download needed)

### 2.3 Consensus API Waitlist
- **URL:** https://consensus.app/ → API access page
- **Action:** Join the API waitlist (enterprise/developer access)
- **Alternative:** Use Perplexity `sonar-pro` for similar web-grounded research queries
- **Impact:** Fact-checking claims against peer-reviewed literature

### 2.4 Lean 4 Installation (Formal Proofs) — DONE
- **Status:** Installed v4.28.0 via elan
- **Next:** Install VS Code + Lean 4 extension
- **Then:** `lake new bigbounce-proofs` to create a proof project
- **Impact:** Formalize and machine-verify key BigBounce theorems
- **Priority equations to formalize:**
  1. Bounce density: ρ_crit = 0.27 ρ_Pl (from LQC parameters)
  2. Dilution chain: D_inf = e^{-3N}(T_reh/M_GUT)^{3/2}
  3. Dimensional analysis: [α/M · F^{on-shell}] = +4

### 2.5 Cloud GPU for Polymathic AI Models — DONE
- **Chosen:** Google Colab Pro ($10/mo) — A100 access
- **Notebook:** `research/notebooks/bigbounce_gpu.ipynb`
- **Secrets to add in Colab:** HUGGINGFACE_TOKEN, ANTHROPIC_API_KEY, GOOGLE_AI_API_KEY, DEEPSEEK_API_KEY
- **Impact:** Physics-informed inference on astronomical data

### 2.6 Web-Only Tools (Browser Use)

These tools have no API. Use them directly in your browser:

| Tool | URL | Best For |
|------|-----|----------|
| ResearchRabbit | https://researchrabbit.ai/ | Visual citation trees, related paper discovery |
| SciSpace | https://scispace.com/ | Reading/summarizing dense papers |
| Elicit | https://elicit.com/ | Systematic literature extraction |
| NotebookLM | https://notebooklm.google.com/ | Upload BigBounce PDFs, find contradictions |
| Paperpal | https://paperpal.com/ | Citation-aware grammar checking |
| Trinka | https://trinka.ai/ | Scientific grammar/style checking |

**Recommended workflow:**
1. Upload `arxiv/main.pdf` to **NotebookLM** → ask it to find internal contradictions
2. Run `arxiv/main.tex` through **Paperpal** → fix grammar while preserving LaTeX/BibTeX
3. Use **ResearchRabbit** → create collection from our 46 references → discover missed papers
4. Use **Consensus** → fact-check each "This work shows..." claim

---

## Phase 3: Full Pipeline Integration

Once Phase 1 scripts exist and Phase 2 keys are in place, wire everything into an automated research pipeline:

```
research/
├── agents/
│   ├── reasoning_router.py      # Multi-model LLM routing
│   ├── literature_search.py     # ADS + S2 + arXiv unified search
│   ├── computation.py           # Wolfram + DeepSeek verification
│   ├── data_access.py           # MAST + Gaia + SDSS queries
│   ├── dataset_loaders.py       # MMU + AstroML data loading
│   └── paper_checker.py         # Claim verification pipeline
├── outputs/                     # Generated reports, plots
├── env_check.py                 # Environment validator (exists)
└── run_pipeline.py              # Orchestrator
```

### Pipeline: Automated Pre-Submission Check

```
1. literature_search.py → Find all papers citing our 46 refs since v0.9.0
2. paper_checker.py → For each claim in Table XI, verify against Consensus/Perplexity
3. computation.py → Verify all equations via Wolfram Alpha
4. reasoning_router.py → Send key derivations to DeepSeek R1 for sign-error check
5. reasoning_router.py → Send full abstract to Gemini for novelty assessment
6. Output → research/outputs/pre_submission_report_{date}.md
```

---

## Python Dependencies

Add to `requirements.txt`:
```
# LLM SDKs
anthropic
openai
google-generativeai

# Science
astroquery
astroML
datasets          # HuggingFace
transformers      # For Polymathic AI models

# Utilities
python-dotenv
requests
pandas
numpy
scipy
matplotlib
```

---

## .env.local Status (as of 2026-03-03)

| Key | Status |
|-----|--------|
| ANTHROPIC_API_KEY | CONFIGURED |
| OPENAI_API_KEY | CONFIGURED |
| GOOGLE_AI_API_KEY | CONFIGURED |
| DEEPSEEK_API_KEY | CONFIGURED |
| XAI_API_KEY | CONFIGURED |
| OPENROUTER_API_KEY | CONFIGURED |
| NASA_ADS_API_KEY | CONFIGURED |
| SEMANTIC_SCHOLAR_API_KEY | PENDING (form submitted) |
| HUGGINGFACE_TOKEN | CONFIGURED |
| FIRECRAWL_API_KEY | CONFIGURED |
| PERPLEXITY_API_KEY | CONFIGURED |
| WOLFRAM_ALPHA_APP_ID | CONFIGURED |

**11/12 keys configured. 1 pending (Semantic Scholar). 2 not needed yet (Consensus waitlist, Trinka enterprise).**

Also configured: `DEFAULT_RESEARCH_MODEL=claude-opus-4-6`, `MAX_REASONING_TOKENS=16384`, `RESEARCH_OUTPUT_DIR=./research/outputs`

---

## Priority Order

1. ~~**NOW:** Claude builds Phase 1 scripts~~ — **DONE** (5 scripts, all tested)
2. ~~**THIS WEEK:** Lean 4~~ — **DONE** (v4.28.0). ~~Cloud GPU~~ — **DONE** (Colab Pro). Semantic Scholar key — **PENDING**
3. **NEXT:** Wire Phase 1 into automated pre-submission pipeline (`paper_checker.py` + `run_pipeline.py`)
4. **LATER:** Lean 4 proof formalization, Fornax registration
