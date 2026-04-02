# RESUME PROJECT HERE — BigBounce Research Program

**Date snapshot:** 2026-04-02
**Reason:** MacBook dying, transferring to other machine.
**Repo:** https://github.com/Hubify-Projects/bigbounce (main branch)
**Site:** https://bigbounce.hubify.app (Netlify auto-deploy from main)

---

## WHAT IS THIS PROJECT

Bounce cosmology research program by Houston Golden. Goal: prove bounce cosmology beats inflation using observational data. Bounce-model AGNOSTIC (not tied to one model). 4 papers, 5 AI pipelines, MCMC infrastructure.

## CURRENT STATE (April 2, 2026)

### Papers
| # | Title | Status | Location |
|---|-------|--------|----------|
| 1 | Spin-Torsion Cosmology (ECH barriers + transparency) | v2.2.0, 24pp, ready for submission | `arxiv/main.tex` |
| 2 | f_NL Forecast (SPHEREx testable) | v1.3.0, 12pp, ready for submission | `research/focused_paper_source_integration/02_full_draft.tex` |
| 3 | DESI DR1 Spectral Anomaly Catalog (195K objects) | v0.1 draft | In pipeline outputs |
| 4 | Galaxy Chirality Catalog (8.47M galaxies) | Draft in progress | `pipelines/p2_chirality/chirality_catalog_paper.tex` |

### Key Scientific Results
- **14 structural barriers** close all ECH-specific routes (other bounce models bypass these)
- **f_NL = -35/8 = -4.375** — parameter-free matter bounce prediction, SPHEREx testable 2028
- **ALP birefringence** β = 0.27° matches 3.6σ observed signal
- **w0-wa MCMC** — quintom-B w-crossing favored at 2.3σ, P(quintom-B) = 98.6%
- **NANOGrav** — matter bounce γ=3.0 vs observed 3.2±0.6 (0.33σ consistent)
- **Chirality** — 8.47M galaxies, CW/(CW+CCW)=0.4974, dipole=0.43σ (null result)
- **424,181+ MCMC samples** across 3 frozen dataset combinations

### Running Compute (H200 pod)
- **Pod ID:** `7zong4jdj46yjp` — SSH: `root@103.196.86.169 -p 34546 -i ~/.ssh/id_ed25519`
- **LAMOST DR10** was downloading (~11.4M spectra), may still be running
- **Completed:** SDSS DR18 (77K anomalies), eROSITA DR1 (9K anomalies)
- **Queued on pod:** Planck CMB, NEOWISE, Gaia DR3, ACT DR6, SDSS×DESI cross-match, super-resolution
- **Cost:** $3.59/hr — CHECK IF STILL RUNNING, stop if idle

### Stopped/Done Pods
- H100 chirality pod (`ulfxypratod4vr`) — catalog COMPLETE
- RTX A4000 MCMC pod (`fn19oivkjowmq4`) — w0-wa CONVERGED, chains frozen
- CPU pipeline B pod (`kqo1b4e4igycra`) — redundant with H200

### What Was Just Committed (last commit before this file)
- Corrected f_NL Fisher forecast σ values (were too optimistic)
- Chirality paper figure formatting fixes
- NANOGrav bounce fit results + chain (γ=6.7 free fit vs γ=3.0 predicted — 7.5σ tension in FREE fit, but Papanikolaou 2025 shows consistency via different analysis)
- `best_model_47k.pt` — trained spectral anomaly model (47K params)
- `download_uncataloged_spectra.py` — script to get spectra not in catalogs

## IMMEDIATE NEXT STEPS (resume here)

### Priority 1: Pipeline 1 — f_NL Tracer Purification (THE NOVEL WORK)
Steps 2-6 in `project-context/pipeline1_tracer_purification_plan.md`:
1. ~~Anomaly catalog~~ DONE (195K anomalies)
2. **Cross-match anomalies with Legacy Survey + unWISE** — NOT STARTED
3. **Classify: which are high-z QSOs?** — NOT STARTED
4. **Validate bias enhancement** — NOT STARTED
5. **Re-compute σ(f_NL)** — NOT STARTED
6. **Paper 3 draft** — v0.1 exists

### Priority 2: Multi-Survey Anomaly Sweep
- Check H200 pod — is LAMOST done? Start next queued experiments
- Cross-correlate SDSS anomalies with DESI anomalies (`projects/cross_survey/`)

### Priority 3: Quintom Bounce Track
- Compute f_NL for Lee-Wick quintom bounce (literature gap — nobody has done this)
- If f_NL = -35/8 is mechanism-independent across matter bounce AND quintom, that's a major result

### Priority 4: Update Website
- `activity.html` needs new timeline entries for April work
- `index.html` stat cards may need updating
- Papers page needs chirality paper progress update

## KEY FILE LOCATIONS

### Research Strategy
- `project-context/bounce_portfolio_strategy.md` — THE STRATEGY (multi-model portfolio)
- `project-context/pipeline1_tracer_purification_plan.md` — exact next steps for f_NL
- `project-context/active_pods_and_pipelines.md` — pod status (update when resuming)
- `project-context/gpu-inference-playbook.md` — USE DataLoader, 32x speedup

### Data & Results
- `pipelines/h200_results/sdss_dr18/` — 46 parquet batches of SDSS anomalies
- `pipelines/h200_results/erosita/` — eROSITA anomaly results
- `projects/nanograv/` — NANOGrav bounce fit (chain + results JSON)
- `projects/sdss-dr18/` — SDSS scan scripts, model, checkpoint
- `pipelines/p1_highz_tracers/outputs/` — f_NL forecast, tracer selection
- `pipelines/p2_chirality/` — chirality paper + all figures
- `reproducibility/cosmology/` — MCMC chains, Cobaya configs

### Claude Memory
- `.claude/projects/-Users-houstongolden-Desktop-CODE-2026-bigbounce/memory/MEMORY.md` — full memory index
- All memory files have frontmatter with descriptions
- `project_full_research_roadmap.md` in memory — THE MASTER PLAN

### External Backups
- **GitHub:** everything committed to main
- **HuggingFace:** `bamfai/bigbounce-mcmc` (chains), `bamfai/desi-spectral-anomaly-detector` (model)
- **Convex:** galaxy explorer data (schema in `convex/schema.ts`)

## CRITICAL RULES (from CLAUDE.md)
1. **NEVER suggest "write up failures and publish"** — always propose next research direction
2. **Bounce-model AGNOSTIC** — not tied to ECH, explore quintom/cuscuton/PBH bounces
3. **NEVER kill pods without saving state** — lost 130K galaxies once
4. **USE DataLoader** for GPU inference (32x speedup)
5. **All papers use revtex4-2** (PRD style), compile on RunPod (local Mac has no LaTeX)
6. **Website must stay in sync** with research — see CLAUDE.md sync protocol

## RunPod API
- API key in `.env.local`
- Management script: `research/runpod_cloud.py`
- SSH key: `~/.ssh/id_ed25519`

---

*Generated 2026-04-02 to preserve project state before MacBook battery death.*
