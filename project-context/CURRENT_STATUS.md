# Current Status: BigBounce Research Paper

**Last updated: 2026-03-03**

## Project Overview

The BigBounce project presents a novel framework for dark energy through Einstein-Cartan-Holst spin-torsion cosmology. The paper is at **v0.9.0** after 5 comprehensive revision rounds. All known critical issues have been addressed.

**Author:** Houston Golden (Independent Researcher, Los Angeles, California, USA)
**Preprint ID:** HUBIFY-2026-001
**GitHub:** `Hubify-Projects/bigbounce`
**Website:** `bigbounce.hubify.app`
**Deployment:** Vercel

## Paper Status: v0.9.0 (Active)

### What's Complete
- **29-page manuscript** in RevTeX4-2 (Physical Review D format), 0 undefined references
- **7 MCMC parameters** fit to Planck+BAO+SN data via Cobaya v3.5 with stock CAMB
- **Inflationary Suppression Factor** (ξ) — phenomenological parameter for spin-torsion dilution
- **Claims Classification Table** (Appendix K) — honest categorization of all claims
- **Reproducibility bundle** — 4 Cobaya YAMLs, Stan galaxy spin model, reproduce scripts
- **IMPLEMENTATION_MAP.md** and **KNOWN_GAPS.md** documenting what exists vs what doesn't
- **Literature-only CMB analysis** — all birefringence values from Minami & Komatsu 2020, Eskilt 2022
- **Galaxy spin asymmetry** reframed as "contested anomaly" with null-result paragraph

### Version History (9 versions tracked)
| Version | Date | Summary |
|---------|------|---------|
| v0.1.0 | 2025-07-15 | Initial draft — core ECH framework |
| v0.2.0 | 2025-11-10 | Critical review, professional tone |
| v0.3.0 | 2026-02-15 | Research squad integration (4 AI agents) |
| v0.4.0 | 2026-02-18 | Expansion to 35 sections + 4 appendices |
| v0.5.0 | 2026-02-18 | Interactive website + visualizations |
| v0.6.0 | 2026-02-18 | Deep research + adversarial review |
| v0.7.0 | 2026-03-01 | Cross-artifact sync, scientific corrections |
| v0.8.0 | 2026-03-03 | Nuclear option — maximum credibility revision |
| v0.9.0 | 2026-03-03 | Reproducibility bundle + claim downgrades |

### 5 Revision Rounds Completed
1. **Comprehensive audit** — 14 issues identified and fixed
2. **arXiv readiness** — operator formalism, one-loop scope, EB prediction
3. **Nuclear option** — deleted forecast section, dropped Ω_k, softened all claims
4. **Skeptical coauthor** — 8 task groups addressing fatal contradictions
5. **Reproducibility captain** — Route 2 (Conservative), stock CAMB, honest artifacts

## Website Status

### Multi-page site at bigbounce.hubify.app
| Page | Status | Description |
|------|--------|-------------|
| `index.html` | Synced to v0.9.0 | Overview with key results |
| `paper.html` | Synced to v0.9.0 | Full paper rendering with MathJax |
| `explained.html` | Synced to v0.9.0 | Accessible explainer |
| `datasets.html` | Synced to v0.9.0 | Data comparison with Chart.js |
| `methodology.html` | Synced to v0.9.0 | Methods and AI-assisted QA |
| `mathematics.html` | Synced to v0.9.0 | Full derivations with expandable sections |
| `versions.html` | Synced to v0.9.0 | Version history with changelogs |
| `data-comparison.html` | Active | 6 interactive Chart.js charts |
| `animations.html` | Active | SVG/Canvas visualizations |

### Downloadable PDF
- Located at `public/downloads/golden-2026-geometric-dark-energy-spin-torsion.pdf`
- 29 pages, compiled via Docker texlive, 0 undefined references

## Key Architecture

### Repository Structure
```
bigbounce/
├── arxiv/              # LaTeX source (canonical)
│   ├── main.tex        # Paper source of truth
│   ├── main.bbl        # Bibliography
│   └── README-SUBMISSION.txt
├── reproducibility/    # Working artifacts
│   ├── cobaya_baseline.yaml
│   ├── cobaya_ech_model.yaml
│   ├── cobaya_ech_extended.yaml
│   ├── cobaya_model_comparison.yaml
│   ├── galaxy_spin_model.stan
│   ├── reproduce_mcmc.sh
│   ├── reproduce_galaxy_spins.sh
│   ├── data/
│   ├── IMPLEMENTATION_MAP.md
│   └── KNOWN_GAPS.md
├── versions/           # Version tracking
│   └── manifest.json
├── public/             # Static assets
│   ├── downloads/      # PDF
│   ├── images/
│   └── spreadsheets/
├── project-context/    # Documentation
│   └── peer-reviews/   # All review rounds
├── *.html              # Website pages
└── version.json        # Root version metadata
```

### Canonical Source of Truth
`arxiv/main.tex` → all website pages mirror it. Any change to the paper must be synced to HTML.

## What's NOT in the Paper (Honest Gaps)

Per `KNOWN_GAPS.md`:
- No custom CAMB module (uses stock CAMB with N_eff as free parameter)
- No actual MCMC chain files (methodology described, runs not yet executed)
- No original CMB map analysis (all values from published literature)
- No CNN galaxy spin classifier (uses published catalog labels)
- Galaxy spin signal has 37-order-of-magnitude gap from torsion coupling

## Next Steps for arXiv Submission

1. **Execute MCMC runs** — Run the 4 Cobaya YAMLs to produce actual chain files
2. **Final proofread** — One more pass for typos, formatting
3. **arXiv category selection** — gr-qc (primary), astro-ph.CO (cross-list)
4. **Submission** — Upload main.tex + .bbl + figures

## Peer Review Documentation

All reviews saved in `project-context/peer-reviews/`:
- `2026-03-02_1917PST_comprehensive-audit.md`
- `2026-03-02_1917PST_claims-table.md`
- `REVISION_TRACKER.md` — tracks all 5 rounds with issue resolution
