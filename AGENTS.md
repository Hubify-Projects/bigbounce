# AGENTS.md — Universal AI Agent Context for BigBounce

This file provides complete context for any AI agent (Claude Code, Cursor, Codex, Windsurf, Copilot, etc.) working on this repository. Read this file in full before making any changes.

---

## Quick Context

**What:** A theoretical physics paper + companion website exploring geometric dark energy from spin-torsion cosmology.

**Repo:** `Hubify-Projects/bigbounce` on GitHub

**Website:** [bigbounce.hubify.app](https://bigbounce.hubify.app) — auto-deploys from `main` via Vercel

**Paper:** `arxiv/main.tex` (LaTeX, revtex4-2 format) — compiled to `arxiv/main.pdf`

**Author:** Houston Golden (houston@hubify.com) — THE author. AI agents are research assistants, not co-authors.

**Current version:** Check `version.json` at repo root for the live version number and date.

**This repo is fully self-contained.** No external dependencies on any other repo, monorepo, or infrastructure. Clone it, work on it, push it.

---

## The Golden Rule

**`arxiv/main.tex` is the single source of truth.** Every number, claim, and caveat in the HTML pages must match the LaTeX source. When in doubt, the LaTeX wins.

---

## Architecture

### Paper (LaTeX)

```
arxiv/
├── main.tex              # The paper (~1,500 lines, revtex4-2)
├── main.pdf              # Compiled output
├── references.bib        # Bibliography (46 entries)
├── figures/              # 9 PNG figures
├── README-SUBMISSION.txt # arXiv submission metadata
└── reproducibility/      # MCMC reproducibility package
    ├── cobaya_config.yaml
    ├── camb_modifications.diff
    ├── params_bestfit.ini
    └── README.md
```

Custom LaTeX commands defined at top of `main.tex`:
- `\Leff` — effective cosmological constant (Lambda_eff)
- `\MPl` — reduced Planck mass
- `\Dinf` — inflationary dilution factor
- `\Xi` — geometric dilution parameter (dimensionless)
- `\paperVersion` / `\paperTimestamp` — version macros (KEEP THESE UPDATED)

### Website (Static HTML)

```
index.html          # Homepage — abstract, comparison table, signature cards
paper.html          # Full paper HTML (mirrors main.tex)
explained.html      # Plain-language explainer
mathematics.html    # Mathematical derivations
methodology.html    # Methods and validation
datasets.html       # Data sources, scorecard, honest assessment
galaxy-zoo.html     # Galaxy Zoo data explorer (8.67M galaxies)
data-comparison.html # Interactive Chart.js visualizations
versions.html       # Version history
style.css           # Site-wide styles
```

The website is purely static. No build step. MathJax and Chart.js loaded from CDN.

**Deployment:** Push to `main` → Vercel auto-deploys. Config in `vercel.json`.

### Peer Review System

```
project-context/peer-reviews/
├── REVISION_TRACKER.md                        # Master tracker
├── 2026-03-02_1917PST_comprehensive-audit.md  # Round 1 audit
├── 2026-03-02_1917PST_claims-table.md         # Claims classification
└── (future audits go here)
```

**Naming convention:** `YYYY-MM-DD_HHMMtz_description.md`

### Versioning

- `version.json` at repo root — current version + date
- `versions/manifest.json` — full version history
- `\paperVersion` and `\paperTimestamp` macros in `main.tex`
- `\date{...}` in `main.tex` — the date printed on the PDF

**All four must be updated together when incrementing versions.**

---

## How to Compile the PDF

Docker (recommended):
```bash
cd arxiv
docker run --rm -v "$(pwd):/work" -w /work texlive/texlive:latest \
  sh -c "pdflatex -interaction=nonstopmode main.tex && \
         bibtex main && \
         pdflatex -interaction=nonstopmode main.tex && \
         pdflatex -interaction=nonstopmode main.tex"
```

Native texlive:
```bash
cd arxiv
pdflatex main && bibtex main && pdflatex main && pdflatex main
```

Verify: `grep -c "undefined" arxiv/main.log` — must be 0.

---

## Scientific Status and Constraints

This paper has been through 3 rounds of rigorous peer review (30+ issues addressed). The current posture is **maximum honesty** — every limitation is disclosed. When editing, you MUST maintain this honesty. Never strengthen claims beyond what the body text supports.

### What the paper claims (and what it doesn't):

| Claim | Status | Where |
|-------|--------|-------|
| Dark energy "derived from" torsion | NO — "modeled as arising from" | Abstract, line 63 |
| w = -1 equation of state | ASSUMED, not derived | Sec II.C.2 |
| H0 = 69.2, sigma8 = 0.785 | MCMC fits, not predictions | Abstract, Sec III.C |
| Omega_k in MCMC | REMOVED — fixed to 0 (92 e-folds) | Sec III.C, tables |
| Birefringence beta = 0.30 deg | NOT PREDICTED — Planck measurement, no photon coupling | Sec III.A |
| Galaxy spin A0 ~ 0.003 | EMPIRICAL — 9-12 order gap from coupling | Sec II.C.3 |
| Forecast/detection timeline | DELETED — premature without derived amplitudes | (removed) |
| Fine-tuning "solved" | NO — "reparameterized" from 10^120 to 10^5 | Sec II.C.1 |

### Language rules:

- "derives" / "predicts" → use "models as arising from" / "accommodates" / "yields (from MCMC)"
- "resolves tensions" → "partially reduces tensions"
- "predictions" → "testable outputs" or "expected signatures"
- "comprehensive framework" → "phenomenological framework"
- Never add β=0.30° as a model prediction (it's a Planck measurement)
- Never claim Omega_k as a model parameter (it's fixed to 0)
- Never add forecast/detection timeline content back

---

## Editing Workflow

### Paper edits:
1. Edit `arxiv/main.tex`
2. Recompile PDF (3-pass + bibtex)
3. Verify 0 undefined references
4. Sync changed claims/numbers to HTML pages (see table below)
5. Update `version.json` — increment version, update date
6. Update `\paperVersion`, `\paperTimestamp`, `\date{}` in main.tex
7. Commit with descriptive message
8. Push to main (auto-deploys website)

### Which HTML pages to sync after main.tex changes:

| If you changed... | Sync these pages |
|-------------------|-----------------|
| Abstract | `index.html`, `paper.html` |
| H0/sigma8 values | `index.html`, `paper.html`, `datasets.html`, `methodology.html` |
| Birefringence claims | `index.html`, `paper.html`, `explained.html`, `methodology.html` |
| Galaxy spin claims | `index.html`, `paper.html`, `explained.html`, `datasets.html` |
| Tension sigma values | `index.html`, `paper.html`, `datasets.html` |
| Any claim language | All HTML pages — grep to verify |

### Verification grep commands after edits:
```bash
# No stale "7 sigma" birefringence claims
grep -r "7.*sigma\|~7σ\|7σ" *.html

# No "deriving dark energy"
grep -n "deriving dark energy" arxiv/main.tex

# No forecast references (section was deleted)
grep -n "\\\\ref{sec:timeline}\|\\\\ref{app:forecast}" arxiv/main.tex

# No floating Omega_k
grep -n "Omega_k.*free\|Omega_k.*prior\|Omega_k.*Flat" arxiv/main.tex

# Version date is current
grep "paperTimestamp" arxiv/main.tex
cat version.json
```

---

## Peer Review Protocol

When conducting or receiving a review:

1. **Save the review** to `project-context/peer-reviews/YYYY-MM-DD_HHMMtz_description.md`
2. **Update the tracker** at `project-context/peer-reviews/REVISION_TRACKER.md`
3. **Fix issues in main.tex** (canonical source)
4. **Recompile PDF** and verify
5. **Sync HTML pages** for any changed claims
6. **Update tracker** with resolution status and commit hash

Every issue gets tracked from identification through resolution. No issues are "lost."

---

## Key Files Reference

| File | Purpose |
|------|---------|
| `arxiv/main.tex` | Canonical paper source |
| `arxiv/main.pdf` | Compiled PDF |
| `arxiv/references.bib` | Bibliography |
| `arxiv/reproducibility/` | MCMC config, params, CAMB description |
| `version.json` | Current version + date |
| `index.html` | Website homepage |
| `paper.html` | Full paper HTML |
| `project-context/peer-reviews/REVISION_TRACKER.md` | Issue tracker |
| `CLAUDE.md` | Claude Code specific instructions |
| `AGENTS.md` | This file — universal agent context |
| `README.md` | Human-readable project overview |

---

## Revision History Summary

| Version | Date | Changes |
|---------|------|---------|
| v0.1.0–v0.6.0 | 2025–2026 | Initial development through v0.6.0 |
| v0.7.0 | 2026-02-28 | Cross-artifact sync, 7sigma→2.4-2.7sigma, TB fix, EB formula |
| v0.7.0-r1 | 2026-03-02 | Round 1: 10 critical issues fixed (arithmetic, theory, tone) |
| v0.7.0-r2 | 2026-03-03 | Round 2: title demoted, dimensional appendix, reproducibility |
| v0.8.0 | 2026-03-03 | Round 3 nuclear option: Omega_k removed, forecast deleted, abstract demoted, galaxy spin gap quantified |

Full issue-by-issue history: `project-context/peer-reviews/REVISION_TRACKER.md`

---

## Research Tools & Agents

This project has a multi-model research toolkit at `research/agents/`. API keys are in `.env.local` (gitignored). See `.env.example` for setup.

### Quick Start

```python
# Load all agents (auto-loads .env.local)
from research.agents.reasoning_router import query, multi_query
from research.agents.literature_search import search, search_ads, search_arxiv
from research.agents.computation import wolfram, deepseek_verify, verify_equation
from research.agents.data_access import search_jwst, search_gaia, query_catalog
from research.agents.dataset_loaders import load_mmu, load_astroml
```

### 1. Reasoning Router (`research/agents/reasoning_router.py`)

Routes questions to the best model for the task type.

```python
# Math verification (DeepSeek R1 — highest rigor)
result = query("Verify: [α/M] has mass dimension -1", task="math_rigor")

# Scientific writing (Claude Opus — best academic voice)
result = query("Write an abstract for...", task="writing")

# Live literature search (Perplexity — web-grounded)
result = query("Latest cosmic birefringence measurements 2026", task="literature")

# Multimodal analysis (Gemini — images + math)
result = query("Analyze this CMB power spectrum...", task="multimodal")

# Compare across models
results = multi_query("Is the Hubble tension resolved?", models=["math_rigor", "reasoning", "literature"])
```

**Available task types:** `math_rigor`, `tensor_check`, `sign_error`, `derivation`, `writing`, `abstract`, `paper_edit`, `reasoning`, `general`, `literature`, `search`, `recent_papers`, `fast`, `quick`, `multimodal`, `plot_analysis`, `compare`

**Model routing:**

| Task | Model | Why |
|------|-------|-----|
| `math_rigor` / `tensor_check` / `sign_error` | DeepSeek R1 | Catches sign errors, highest skepticism |
| `multimodal` / `plot_analysis` | Gemini Deep Think | Best at images + math combined |
| `writing` / `abstract` / `paper_edit` | Claude Opus | Most natural academic voice |
| `reasoning` / `general` | GPT-4o | Highest ELO general reasoning |
| `literature` / `search` / `recent_papers` | Perplexity sonar-pro | Web-grounded, cites real papers |
| `fast` / `quick` | Grok | Fast alternative perspective |
| `compare` | OpenRouter | Multi-model routing |

### 2. Literature Search (`research/agents/literature_search.py`)

Unified search across NASA ADS, Semantic Scholar, arXiv, and Perplexity.

```python
# Unified search (all configured sources)
results = search("spin-torsion dark energy", max_results=5, category="gr-qc")

# NASA ADS (astrophysics-specific, citation-aware)
papers = search_ads("cosmic birefringence Planck", rows=10, year_range="2024-2026")

# arXiv (latest preprints)
papers = search_arxiv("loop quantum cosmology bounce", max_results=5, category="gr-qc")

# Citation analysis
citing = ads_citations("2020PhRvL.125v1301M")  # Papers citing Minami & Komatsu 2020
refs = ads_references("2020PhRvL.125v1301M")    # Papers referenced by M&K 2020

# Perplexity (synthesized answer with live web search)
answer = search_perplexity("What is the latest DESI dark energy result?")

# Semantic Scholar (cross-field discovery, citation graphs)
papers = search_s2("Einstein-Cartan torsion cosmology")
graph = s2_citation_graph("DOI:10.1103/PhysRevLett.125.221301")
```

### 3. Computation & Verification (`research/agents/computation.py`)

```python
# Wolfram Alpha — exact computation
result = wolfram("Planck mass in GeV")                    # Short answer
result = wolfram("integrate x^2 sin(x) dx", format="full") # Full pods
result = wolfram("solve H^2 = Lambda/3 for H", format="llm") # Agent-friendly

# Verify equation numerically
check = wolfram_verify("e^(-3*92) * (10^15/10^16)^(3/2)", "~10^{-121}")

# DeepSeek R1 — rigorous logical verification
verdict = deepseek_verify(
    "The operator ε^{μνρσ} e^I_μ e^J_ν F_{IJρσ} has mass dimension +1",
    context="In Einstein-Cartan theory with Holst term"
)

# Combined: Wolfram + DeepSeek
report = verify_equation("(alpha/M) * M_Pl", "~10^{-2}", context="one-loop estimate")

# Multi-model cross-check
consensus = cross_check("The dilution factor D_inf ~ e^{-3N} for N=92 gives ~10^{-121}")
```

### 4. Data Access (`research/agents/data_access.py`)

JWST, HST, Gaia, SDSS, and 20,000+ catalogs. All free, no keys needed.

```python
# JWST observations
obs = search_jwst("NGC 1365", radius_arcmin=5)
obs = search_jwst(ra=53.23, dec=-36.14, radius_arcmin=3)
s3_path = jwst_s3_uri("jw02107-o001_t001_nircam_clear-f200w")  # Direct S3 access

# MAST (any mission)
obs = search_mast("Crab Nebula", collection="HST")

# Gaia DR3 (1.8 billion stars)
stars = search_gaia(ra=266.4, dec=-29.0, radius_deg=0.5)
custom = gaia_adql("SELECT TOP 10 source_id, parallax FROM gaiadr3.gaia_source WHERE parallax > 100")

# VizieR catalogs
data = query_catalog("II/246", target="M31", radius_arcmin=10)  # 2MASS

# NED (extragalactic)
info = search_ned("NGC 4993")  # GW170817 host galaxy
```

**JWST data access methods:**
1. **MAST API** (`search_jwst()`) — query metadata, download FITS files
2. **AWS S3** (`jwst_s3_uri()`) — direct access to `s3://stpubdata/jwst/public/`, free, no auth
3. **MAST REST API** (`mast_api_query()`) — custom programmatic queries

### 5. Dataset Loaders (`research/agents/dataset_loaders.py`)

```python
# Multimodal Universe (100TB on HuggingFace, streaming)
light_curves = load_mmu("plasticc", streaming=True, max_samples=1000)
galaxy_images = load_mmu("legacysurvey", streaming=True)
jwst_data = load_mmu("jwst_ceers", streaming=True)

# AstroML (local datasets)
spectra = load_astroml("sdss_spectra")
quasars = load_astroml("dr7_quasar")

# List all available
print(list_mmu_datasets())      # 12 HuggingFace datasets
print(list_astroml_datasets())  # 8 local datasets
print(list_polymathic_models()) # 3 GPU models (need Colab Pro)
```

### Environment Validation

```bash
python3 research/env_check.py          # Check which keys are configured
python3 research/env_check.py --test   # Also run connectivity tests
```

### API Keys Status

| Key | Source | Status |
|-----|--------|--------|
| ANTHROPIC_API_KEY | Anthropic | Configured |
| OPENAI_API_KEY | OpenAI | Configured |
| GOOGLE_AI_API_KEY | Google (Gemini) | Configured |
| DEEPSEEK_API_KEY | DeepSeek | Configured |
| XAI_API_KEY | xAI (Grok) | Configured |
| OPENROUTER_API_KEY | OpenRouter | Configured |
| NASA_ADS_API_KEY | NASA ADS | Configured |
| SEMANTIC_SCHOLAR_API_KEY | Semantic Scholar | Pending approval |
| PERPLEXITY_API_KEY | Perplexity | Configured |
| WOLFRAM_ALPHA_APP_ID | Wolfram Alpha | Configured |
| HUGGINGFACE_TOKEN | HuggingFace | Configured |
| FIRECRAWL_API_KEY | Firecrawl | Configured |

Keys are stored in `.env.local` (gitignored) and loaded automatically by all agents.
Also mirrored to Convex cloud for Hubify workspace agents.

### GPU Compute (RunPod)

GPU research runs on RunPod (RTX 6000 Ada, 48GB VRAM). Persistent workspace at `/workspace/`.

**Quick start:**
```bash
# From local machine — manage pod
python3 research/runpod_cloud.py status       # Check pod status
python3 research/runpod_cloud.py ssh           # Get SSH command
python3 research/runpod_cloud.py setup         # Full environment setup
python3 research/runpod_cloud.py push-keys     # Push .env.local to pod
python3 research/runpod_cloud.py stop          # Stop pod (keeps data)
python3 research/runpod_cloud.py start         # Restart pod

# On the pod
ssh root@<ip> -p <port> -i ~/.ssh/id_ed25519
cd /workspace/bigbounce
python3 research/runpod_gpu_session.py         # Run full GPU session
```

**JupyterLab:** Available at port 8888 on RunPod. Use `research/notebooks/runpod_gpu_session.ipynb`.

**Data persists** across pod stop/start in `/workspace/`. Only `terminate` destroys data.

**Legacy Colab notebook:** `research/notebooks/bigbounce_gpu.ipynb` still works on Google Colab Pro as fallback.

### Lean 4 (Formal Proofs)

Lean 4 v4.28.0 is installed locally. For formalizing BigBounce theorems:
```bash
export PATH="$HOME/.elan/bin:$PATH"
lean --version
```

### Full Integration Plan

See `project-context/RESEARCH_TOOLS_INTEGRATION.md` for the complete 29-tool checklist.

---

## Galaxy Zoo Data Agent

The `research/agents/galaxy_zoo.py` module provides programmatic access to Galaxy Zoo catalogs for galaxy spin asymmetry analysis.

### Available Datasets

| Dataset | Galaxies | Access |
|---------|----------|--------|
| Galaxy Zoo DESI | 8,670,000 | `load_gz_desi()` via HuggingFace |
| Galaxy Zoo 2 | 304,122 | `query_gz2()` via VizieR |
| Galaxy Zoo DECaLS | 314,000 | `query_gz_decals()` via VizieR |
| TNG50-CEERS | 10,000 | `load_tng50_ceers()` via HuggingFace |
| Zoobot Encoders | 4M-197M params | `load_zoobot_encoder()` via timm |

### Usage Examples

```python
from research.agents.galaxy_zoo import *

# List all datasets
list_gz_datasets()

# Load GZ DESI (streaming)
ds = load_gz_desi(streaming=True, max_samples=10000)

# Compute spin asymmetry in redshift bins
result = compute_spin_asymmetry(catalog, z_bins=20)

# Compute HEALPix sky map
sky_map = compute_spin_dipole(catalog, nside=16)

# Save analysis results
save_gz_data(result, "my_analysis.json")
```

### Data Pipeline

```bash
# Download and process Galaxy Zoo data for the website
python3 scripts/download_galaxy_zoo.py --sample-size 100000

# Output: public/data/galaxy_zoo/
#   gz_desi_spin_summary.json
#   gz_desi_sky_map.json
#   gz2_spin_asymmetry.json
#   catalog_metadata.json
```

---

## Contact

Houston Golden — houston@hubify.com

---

# CLAUDE.md (Claude Code Specific Instructions)

*The following section is included so this file is self-contained for all agents. Claude Code also reads the standalone `CLAUDE.md` file.*

## Project Overview

This repository contains a scientific research paper titled "Geometric Dark Energy from Spin-Torsion Cosmology: Phenomenological Constraints and Correlated Signatures" by Houston Golden. The project is a theoretical physics paper exploring dark energy through quantum gravitational effects in spin-torsion cosmology.

## Repository Structure

- `bigbounce.md` - Complete research paper content in Markdown format (~35,000 words)
- `index.html` - Interactive web presentation of the research paper
- `paper/` - Individual sections of the paper organized as separate Markdown files
- `public/images/` - Scientific figures and illustrations (PNG format, Git LFS tracked)
- `public/spreadsheets/` - Supporting data tables (Excel format)
- `interactive-data.html` & `interactive-data-simple.html` - Interactive data visualizations using Chart.js
- `server.js` - Express server for local development

## Commands

### Local Development
```bash
npm install
node server.js          # http://localhost:3000
# or: python -m http.server 8000
# or: open index.html
```

### Compile PDF
```bash
cd arxiv
docker run --rm -v "$(pwd):/work" -w /work texlive/texlive:latest \
  sh -c "pdflatex -interaction=nonstopmode main.tex && bibtex main && \
         pdflatex -interaction=nonstopmode main.tex && pdflatex -interaction=nonstopmode main.tex"
```

### Deployment
- Vercel auto-deploys from `main` branch
- No build step required — purely static site

## Project Dependencies

- **Express.js**: Optional local dev server
- **MathJax**: CDN — mathematical rendering
- **Chart.js**: CDN — data visualizations
- **texlive**: PDF compilation (Docker image `texlive/texlive:latest`)
- No build tools or preprocessors required

## Working with the Content

- Mathematical expressions use LaTeX syntax within `$$` or `$` delimiters
- Figures are referenced as `public/images/figure_name.png`
- The HTML pages should be kept in sync with `arxiv/main.tex`
- Maintain academic writing style and scientific rigor
- Images are tracked with Git LFS — ensure Git LFS is installed when cloning

## Peer Review & Revision Workflow

**CRITICAL: All peer reviews, audits, and revision requests MUST be saved to `project-context/peer-reviews/`.**

### File Naming Convention
```
YYYY-MM-DD_HHMMtz_description.md
```

### Tracking Revisions
- `project-context/peer-reviews/REVISION_TRACKER.md` tracks all issues across rounds
- Update issue status as revisions are completed
- After each revision round:
  1. Recompile PDF and verify 0 undefined references
  2. Run dimensional consistency checks
  3. Grep for removed language patterns
  4. Verify claims table against revised text
  5. Sync website if applicable
  6. Update REVISION_TRACKER.md

### Canonical Source of Truth
- `arxiv/main.tex` is the canonical source — everything else mirrors it
- `version.json` at repo root tracks current version
- `versions/manifest.json` tracks version history

## Contact

Author: Houston Golden
Email: houston@hubify.com
