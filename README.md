# BigBounce — Geometric Dark Energy from Spin-Torsion Cosmology

**Author:** Houston Golden
**Version:** v0.7.0
**Paper:** 28 pages, 46 references, 9 appendices
**Website:** [bigbounce.hubify.app](https://bigbounce.hubify.app)
**Preprint ID:** HUBIFY-2026-001

---

## What This Is

A theoretical physics paper and companion website exploring dark energy through quantum gravitational effects in Einstein-Cartan-Holst spin-torsion cosmology. The framework connects Loop Quantum Gravity, torsion-regulated bounces, and cosmic rotation to produce testable observational signatures.

This repository is **fully self-contained** — no external dependencies on any other repo, monorepo, or infrastructure. Clone it, work on it, push it.

---

## Repository Structure

```
bigbounce/
├── arxiv/                          # LaTeX paper (canonical source of truth)
│   ├── main.tex                    # The paper (~1,500 lines)
│   ├── main.pdf                    # Compiled PDF (28 pages)
│   ├── references.bib              # Bibliography (46 entries)
│   ├── figures/                    # Paper figures (9 PNGs)
│   ├── README-SUBMISSION.txt       # arXiv submission metadata
│   └── reproducibility/            # MCMC reproducibility package
│       ├── cobaya_config.yaml      # Cobaya v3.3 MCMC configuration
│       ├── camb_modifications.diff # CAMB v1.5 modification description
│       ├── params_bestfit.ini      # Best-fit parameters + 68% CI
│       └── README.md               # Reproducibility instructions
│
├── index.html                      # Homepage
├── paper.html                      # Full paper (HTML mirror of main.tex)
├── explained.html                  # Plain-language explainer
├── mathematics.html                # Mathematical derivations
├── methodology.html                # Methods and validation
├── datasets.html                   # Data sources and comparison
├── data-comparison.html            # Interactive Chart.js visualizations
├── versions.html                   # Version history
├── style.css                       # Site-wide styles
│
├── project-context/
│   └── peer-reviews/               # Audit history and revision tracking
│       ├── REVISION_TRACKER.md     # Master tracker (3 rounds, 30+ issues)
│       ├── 2026-03-02_*.md         # Individual audit files
│       └── ...
│
├── version.json                    # Current version metadata
├── versions/manifest.json          # Full version history
├── vercel.json                     # Vercel deployment config
├── CLAUDE.md                       # AI agent instructions
└── README.md                       # This file
```

### Key Principle

**`arxiv/main.tex` is the single source of truth.** All HTML pages, the PDF, and the website content must mirror the LaTeX source. When editing the paper, always start with `main.tex` and then sync the website pages.

---

## Setup

### Prerequisites

- **Git** (with Git LFS for images)
- **Docker** (for LaTeX compilation) — or a native texlive installation
- **Node.js** (optional, for local dev server)
- **Python 3.9+** (optional, for data pipeline)

### Clone

```bash
git lfs install  # if not already done
git clone https://github.com/Hubify-Projects/bigbounce.git
cd bigbounce
```

### Compile the PDF

Using Docker (recommended — no local TeX install needed):

```bash
cd arxiv
docker run --rm -v "$(pwd):/work" -w /work texlive/texlive:latest \
  sh -c "pdflatex -interaction=nonstopmode main.tex && \
         bibtex main && \
         pdflatex -interaction=nonstopmode main.tex && \
         pdflatex -interaction=nonstopmode main.tex"
```

Or with a native texlive installation:

```bash
# macOS: brew install --cask mactex (then reopen terminal)
# Ubuntu: apt install texlive-full
cd arxiv
pdflatex main && bibtex main && pdflatex main && pdflatex main
```

The output is `arxiv/main.pdf`. Verify 0 undefined references:

```bash
grep -c "undefined" arxiv/main.log  # should be 0
```

### Preview the Website Locally

Any of these work (it's a static site, no build step):

```bash
# Option 1: Python
python3 -m http.server 8000

# Option 2: Node
npx serve .

# Option 3: Express (requires npm install first)
npm install && node server.js

# Option 4: Just open index.html in a browser
open index.html
```

### Deploy

Push to `main` — Vercel auto-deploys to [bigbounce.hubify.app](https://bigbounce.hubify.app).

```bash
git push origin main
```

---

## Working on the Paper

### Editing main.tex

The paper uses `revtex4-2` (APS Physical Review D format) with standard LaTeX packages. Custom commands are defined at the top of the file:

- `\Leff` — effective cosmological constant
- `\MPl` — reduced Planck mass
- `\Dinf` — inflationary dilution factor
- `\Xi` — geometric dilution parameter
- `\paperVersion` / `\paperTimestamp` — version macros

### After Editing main.tex

1. Recompile PDF (3-pass + bibtex)
2. Verify 0 undefined references
3. Sync any changed claims/numbers to the HTML pages
4. Update `version.json` if incrementing version
5. Commit and push

### Syncing Website Pages

The following HTML pages mirror content from `main.tex` and must be kept in sync:

| HTML Page | What It Mirrors |
|-----------|----------------|
| `paper.html` | Full paper (abstract, tables, figures, conclusions) |
| `index.html` | Abstract, comparison table, signature cards |
| `explained.html` | Plain-language summary of key claims |
| `datasets.html` | Data sources, scorecard, honest assessment |
| `methodology.html` | Methods, validation, signatures |
| `mathematics.html` | Derivation details |

Key values to grep when syncing: `2.9\sigma` (H0 tension), `1.5\sigma` (sigma8), `2.4--2.7\sigma` (birefringence), `0.003` (A0 amplitude), parameter counts, and any claim language ("derives" vs "models", "predicts" vs "accommodates").

---

## Peer Review & Revision Workflow

All audits and revisions are tracked in `project-context/peer-reviews/`.

### Revision History

| Round | Date | Issues | Status |
|-------|------|--------|--------|
| Round 1 | 2026-03-02 | 10 critical/major issues (5 FATAL) | All resolved |
| Round 2 | 2026-03-03 | 5 structural issues | All resolved |
| Round 3 | 2026-03-03 | 10 issues (nuclear option) | All resolved |

See `project-context/peer-reviews/REVISION_TRACKER.md` for the full issue-by-issue breakdown.

### Adding a New Review

1. Save the review to `project-context/peer-reviews/YYYY-MM-DD_HHMMtz_description.md`
2. Add a new section to `REVISION_TRACKER.md`
3. Address issues in `arxiv/main.tex` (canonical source)
4. Recompile PDF
5. Sync website pages
6. Update tracker with resolution status

---

## Reproducibility

The `arxiv/reproducibility/` directory contains materials for reproducing the MCMC analysis:

- **`cobaya_config.yaml`** — Full Cobaya v3.3 sampler configuration with priors
- **`params_bestfit.ini`** — Best-fit parameters with uncertainties
- **`camb_modifications.diff`** — Description of required CAMB v1.5 modifications (descriptive, not a working patch — this is disclosed in the paper)

To reproduce:

```bash
pip install cobaya==3.3 camb==1.5
cobaya-install cosmo -p /path/to/packages
# Apply CAMB modifications per camb_modifications.diff
cobaya-run arxiv/reproducibility/cobaya_config.yaml
```

---

## Current Scientific Status (v0.7.0)

### What the paper claims (honestly):
- Dark energy **modeled as arising from** (not "derived from") a parity-odd quantum correction
- w = -1 is **assumed, not derived** (IR effective action calculation is an open problem)
- H0 = 69.2 +/- 0.8 and sigma8 = 0.785 +/- 0.016 from MCMC fits (partially reducing tensions)
- Omega_k **fixed to 0** (92 e-folds of inflation mandates this)
- Birefringence: qualitatively consistent with Planck 2.4-2.7 sigma, but **rotation angle not derived** (requires photon-torsion coupling)
- Galaxy spin amplitude A0 ~ 0.003 is **empirical** with a 9-12 order-of-magnitude gap from the coupling

### Known open problems:
- No photon-torsion coupling derived
- Galaxy spin amplitude gap (alpha/M too small)
- IR effective vacuum term not derived from first principles
- Reproducibility code bundle not yet fully public (CAMB patch is descriptive)

---

## Data Pipeline (Optional)

The repo includes an optional data pipeline for interactive charts:

```bash
pip3 install -r requirements.txt
npm run build:data  # or: python3 scripts/build_data.py
```

Outputs go to `public/data/` (JSON) and `public/downloads/` (XLSX). The pipeline is independent of the paper and website — it's for the interactive data comparison page only.

---

## Contact

**Houston Golden**
houston@hubify.com
[bigbounce.hubify.app](https://bigbounce.hubify.app)
