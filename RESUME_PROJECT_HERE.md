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

### H200 Pod Live Status (checked 2026-04-02 ~7:15 PM)
- **LAMOST DR10 scan ACTIVELY RUNNING** — `lamost_scan_v2.py` in tmux
- **Progress:** 710/1177 nights (60%), 7.7M spectra scored, 23K anomalies (0.3%)
- **Rate:** 58 nights/hr, **ETA: ~8 hours** (~3 AM Apr 3)
- **GPU idle** (0% util) — LAMOST is CPU-bound download+scoring
- **95 LAMOST batch parquets** already saved (522 MB in `/workspace/bigbounce/outputs/lamost/`)
- **Cost to finish:** ~$29 more at $3.59/hr

### H200 Pod Data Inventory (20 GB total on `/workspace/bigbounce/`)
| Directory | Size | Contents |
|---|---|---|
| `outputs/sdss_batch_*.parquet` (46 files) | 1.8 GB | SDSS DR18 anomaly scan — 77K anomalies from 2.3M spectra |
| `outputs/erosita/` | 1.7 GB | eROSITA DR1 X-ray anomaly scan — 9.3K anomalies |
| `outputs/lamost/` (95+ batches, growing) | 522 MB | LAMOST DR10 partial — 7.7M spectra, 23K anomalies so far |
| `temp/sdss/` | 15 GB | Raw SDSS FITS spectra (downloaded, can re-download) |
| `temp_lamost/` | 508 MB | LAMOST temp download cache |
| `outputs/injection_recovery_real/` | ~1 MB | Injection recovery test |
| `outputs/multi_resolution/` | ~1 MB | Multi-resolution anomaly test |
| `outputs/recursive_anomalies/` | ~4 MB | Recursive anomaly detection |
| Scripts | ~150 KB | `sdss_dr18_scan.py`, `lamost_scan_v2.py`, `erosita_scan.py`, `planck_cmb_scan.py`, etc. |
| `best_model_47k.pt` | 3.4 MB | Trained spectral autoencoder (also in local repo) |

**CRITICAL:** When LAMOST finishes (~3 AM Apr 3), SSH in from other Mac and run:
```bash
scp -P 34546 -i ~/.ssh/id_ed25519 -r root@103.196.86.169:/workspace/bigbounce/outputs/ ./pipelines/h200_results/
```
Then stop the pod to save money.

### What Was Just Committed (last 2 commits)
- Corrected f_NL Fisher forecast σ values (were too optimistic)
- Chirality paper figure formatting fixes
- NANOGrav bounce fit results + chain (γ=6.7 free fit vs γ=3.0 predicted — 7.5σ tension in FREE fit, but Papanikolaou 2025 shows consistency via different analysis)
- `best_model_47k.pt` — trained spectral anomaly model (47K params)
- `download_uncataloged_spectra.py` — script to get spectra not in catalogs
- This resume file + local data inventory

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

## LOCAL-ONLY DATA — NOT IN GIT (must recover separately)

**Total local-only data: ~4.8 GB**

### Critical (gitignored, not pushed)
| What | Size | Where to recover |
|---|---|---|
| `data/runpod_backups/` | **2.2 GB** | 176 parquet files: chirality catalogs (full 8.47M), bispectrum results, eq shards, audit results. **Also on HuggingFace `bamfai/bigbounce-mcmc` + Backblaze B2** |
| `pipelines/h200_results/sdss_dr18/` (46 parquets) | **~1.8 GB** | SDSS anomaly batches. **Still on H200 pod `/workspace/`** |
| `pipelines/h200_results/erosita/` | **~100 MB** | eROSITA anomalies. **Still on H200 pod** |
| `reproducibility/cosmology/archives/` | **15 MB** | GPU run snapshot tar.gz. **Also on Backblaze B2** |
| `data/public_mirror/galaxy_zoo_decals/` | **Large** | Galaxy Zoo parquet. **Re-download from Zenodo** |

### Credentials & Keys (MUST recreate on new Mac)
| What | How to recover |
|---|---|
| **`.env.local`** | Contains: RUNPOD_API_KEY, HF_TOKEN, CONVEX keys (dev+prod deploy keys + URLs), B2 keys (KEY_ID + APP_KEY + BUCKET + ENDPOINT). Get from respective dashboards: runpod.io, huggingface.co, convex.dev, backblaze.com |
| **`~/.ssh/id_ed25519`** | SSH key for RunPod pods. Generate new keypair and add to RunPod console, OR copy from this Mac before it dies |
| **RunPod pod SSH configs** | In `.env.local` — H200 pod `7zong4jdj46yjp` at `103.196.86.169:34546` |

### Safe to regenerate (don't worry about these)
| What | How |
|---|---|
| `node_modules/` (56 MB) | `npm install` |
| LaTeX build artifacts (`arxiv/main.aux` etc.) | Recompile on RunPod |
| `__pycache__/`, `.ipynb_checkpoints/` | Auto-generated |

### In Git via LFS (will clone automatically with `git lfs pull`)
| What | Size |
|---|---|
| `reproducibility/cosmology/frozen/` | **257 MB** — frozen MCMC chains (full_tension + planck_bao_sn) |
| `reproducibility/cosmology/chains/w0wa_quintom/` | **42 MB** — quintom w0-wa chains |
| All chain `.txt` and `.covmat` files | Tracked by Git LFS |

### Data also backed up externally
| Backup location | What's there | How to access |
|---|---|---|
| **HuggingFace** `bamfai/bigbounce-mcmc` | MCMC chains + chirality catalog | `huggingface-cli download bamfai/bigbounce-mcmc` |
| **HuggingFace** `bamfai/desi-spectral-anomaly-detector` | Trained anomaly model | `huggingface-cli download bamfai/desi-spectral-anomaly-detector` |
| **Backblaze B2** bucket (in .env.local) | MCMC chains + scripts + figures | Use `b2` CLI with keys from .env.local |
| **Convex** (convex.dev dashboard) | Galaxy explorer data | Schema in `convex/schema.ts` |
| **H200 RunPod pod** | All pipeline results, SDSS/eROSITA/LAMOST data | SSH in and `scp` back |

## SETUP ON NEW MAC

```bash
# 1. Clone
git clone https://github.com/Hubify-Projects/bigbounce.git
cd bigbounce
git lfs pull  # Gets the 300MB of MCMC chains

# 2. Install deps
npm install

# 3. Recreate .env.local (get keys from respective dashboards)
cp .env.example .env.local
# Fill in: RUNPOD_API_KEY, HF_TOKEN, CONVEX_*, B2_*

# 4. Generate SSH key for RunPod
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519
# Add public key to RunPod console

# 5. Recover local-only data from H200 pod
ssh root@103.196.86.169 -p 34546 -i ~/.ssh/id_ed25519
# scp back: /workspace/sdss_dr18/, /workspace/erosita/, etc.

# 6. Recover from HuggingFace
pip install huggingface-cli
huggingface-cli download bamfai/bigbounce-mcmc --local-dir data/runpod_backups/

# 7. Test site
node server.js  # http://localhost:3000

# 8. Read this file + CLAUDE.md + project-context/ to get oriented
```

## RunPod API
- API key in `.env.local`
- Management script: `research/runpod_cloud.py`
- SSH key: `~/.ssh/id_ed25519`

---

*Generated 2026-04-02 to preserve project state before MacBook battery death.*
