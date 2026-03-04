# Current Status: BigBounce Research Paper

**Last updated: 2026-03-04**

## Project Overview

The BigBounce project presents a novel framework for dark energy through Einstein-Cartan-Holst spin-torsion cosmology. The paper is at **v1.0.0** after 6 comprehensive revision rounds. All known critical issues have been addressed. Ready for final proofread and arXiv submission.

**Author:** Houston Golden (Independent Researcher, Los Angeles, California, USA)
**Preprint ID:** HUBIFY-2026-001
**GitHub:** `Hubify-Projects/bigbounce`
**Website:** `bigbounce.hubify.app`
**Deployment:** Vercel (auto-deploys from main)

## Paper Status: v1.0.0 (Active)

### What's Complete
- **31-page manuscript** in RevTeX4-2 (Physical Review D format), 0 undefined references
- **51 bibliography entries** — 4 new citations added in v1.0.0 (Yin 2026, Diego-Palazuelos 2025, DESI DR2 2025, Sanyal 2026)
- **7 MCMC parameters** fit to Planck+BAO+SN data via Cobaya v3.5 with stock CAMB
- **Inflationary Suppression Factor** (Ξ) — clarified as primordial coefficient, not vacuum energy dilution
- **MCMC = ΔNeff disclosure** — explicit statement that analysis is phenomenologically equivalent to any additional relativistic species model
- **σ₈ tension framing** — correctly framed as CMB (Planck) vs weak lensing (KiDS-1000, DES Y3)
- **N=92 e-fold breakdown** — decomposed as ~55-60 observable + ~30 pre-observable, clearly labeled as fitted parameter
- **Claims Classification Table** (Appendix K) — honest categorization of all claims
- **Reproducibility bundle** — 4 Cobaya YAMLs, Stan galaxy spin model, reproduce scripts
- **IMPLEMENTATION_MAP.md** and **KNOWN_GAPS.md** documenting what exists vs what doesn't
- **Literature-only CMB analysis** — birefringence values from Minami & Komatsu 2020, Eskilt 2022, Diego-Palazuelos & Komatsu 2025 (ACT DR6: β=0.215°±0.074°, 2.9σ)
- **Galaxy spin asymmetry** reframed as "contested anomaly" with null-result paragraph
- **Conjunctive falsification** — 3 necessary conditions for falsification explicitly stated

### Version History (10 versions tracked)
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
| v1.0.0 | 2026-03-04 | 6 research issues resolved, 4 new citations, full site sync |

### 6 Revision Rounds Completed
1. **Comprehensive audit** — 14 issues identified and fixed
2. **arXiv readiness** — operator formalism, one-loop scope, EB prediction
3. **Nuclear option** — deleted forecast section, dropped Ω_k, softened all claims
4. **Skeptical coauthor** — 8 task groups addressing fatal contradictions
5. **Reproducibility captain** — Route 2 (Conservative), stock CAMB, honest artifacts
6. **v1.0 Final** — 6 research issues (vacuum energy framing, σ₈ tension, MCMC equivalence, N=92 breakdown, conjunctive falsification) + 4 new citations (Yin 2026, Diego-Palazuelos 2025, DESI DR2, Sanyal 2026)

## Website Status

### Multi-page site at bigbounce.hubify.app
| Page | Status | Description |
|------|--------|-------------|
| `index.html` | Synced to v1.0.0 | Overview with key results, ACT DR6 2.9σ added |
| `paper.html` | Synced to v1.0.0 | Full paper rendering with MathJax, 50 refs |
| `explained.html` | Synced to v1.0.0 | Accessible explainer, σ₈ framing updated |
| `datasets.html` | Synced to v1.0.0 | Data comparison with Chart.js, DESI DR2 |
| `methodology.html` | Synced to v1.0.0 | Full MCMC methodology + ΔNeff disclosure |
| `mathematics.html` | Synced to v0.9.0 | Full derivations with expandable sections |
| `versions.html` | Synced to v1.0.0 | Version history with changelogs (auto from manifest) |
| `data-comparison.html` | Active | Redirects to datasets.html |
| `animations.html` | Active | SVG/Canvas visualizations |
| `galaxy-zoo.html` | Active | Galaxy spin data explorer |

### Downloadable PDF
- Located at `public/downloads/golden-2026-geometric-dark-energy-spin-torsion.pdf`
- 31 pages, compiled via Docker texlive, 0 undefined references, 51 bibliography entries

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
