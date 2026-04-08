# Lab #1 — Bounce Cosmology Lab Migration Plan

**Status:** SPEC COMPLETE · awaiting execution
**Priority:** #1 (super super super clear main goal per Houston)
**Target lab slug:** `bigbounce-hubify` (final name TBD — see §0.3 below)
**Target repo:** `Hubify-Labs/bigbounce-hubify` (post org rename from `Hubify-Projects`)
**Target subdomain:** `bigbounce2.hubify.app` (placeholder, see §0.3 below)
**Author:** Houston Golden + Claude
**Date:** 2026-04-08
**Linked from:** PRD §40 (Hierarchy v2 lock) + PRD §1 (Safety-first repo strategy)

---

## 0. The promise

This document is the **complete migration plan** for moving Houston's BigBounce research (4 papers, 53 experiments, 328K anomalies, 8 surveys, 142 wiki entries, 16 contributions, 3 pipelines, ~3 months of work, ~$400 of GPU compute, ~424,181 MCMC posterior samples, the live `bigbounce.hubify.app` site, the github.com/Hubify-Projects/bigbounce repo, the H200 RunPod pod, all backups, all peer reviews) into a NEW Lab repo inside the Hubify Labs platform — without losing anything, without touching the original repo, and with the new Lab fully operational under the §40 hierarchy from day one.

This migration is the **#1 priority** for Hubify Labs. The platform is not real until Houston can use it to fully replace his current local Claude-Code-only workflow for managing the H200 pod, the papers, and the research. Shipping this migration is the proof that the platform works for at least one real researcher.

### 0.1 Hard rules (the iron laws of this migration)

1. **NEVER touch the original BigBounce repo.** `github.com/Hubify-Projects/bigbounce` (now `Hubify-Labs/bigbounce` after the org rename) is read-only. The original directory `~/Desktop/CODE_2025/bigbounce/` is read-only. The live `bigbounce.hubify.app` site is read-only. None of these change during migration.
2. **The new Lab repo is a fresh clone-and-import**, not a fork. We do NOT use `git fork` or `git mv`. We use `cp -r` from the original directory into a new repo's working tree, then `git init` + first commit. Provenance is documented in the new repo's `MIGRATION_PROVENANCE.md` file (also copied here).
3. **The original site keeps serving** until the new lab's site is verified fully working. There is no DNS cutover until Houston explicitly approves it.
4. **Every migrated artifact gets a `migrated_from:` field** in its frontmatter or metadata pointing back to the source path in the original repo. Auditable forever.
5. **Backup before, backup after.** Per Houston Method, we back up the original repo + the new lab repo at three checkpoints: pre-migration, post-import, post-bootstrap.
6. **Everything tested before cutover.** The new lab's orchestrator runs at least one full standup, one experiment cycle, and one chat-to-project graduation BEFORE we declare the migration complete.

### 0.2 What "migration complete" means

The migration is complete when ALL of the following are true:

- [ ] `Hubify-Labs/bigbounce-hubify` repo exists, is private, contains all migrated content
- [ ] `bigbounce2.hubify.app` (or final subdomain) serves the new Hubify Labs UI for this lab
- [ ] All 4 papers are migrated as Project deliverables under the right Projects
- [ ] All 53 experiments are migrated as Experiment entities under the right Projects
- [ ] All 3 pipelines (P1 highz tracers, P2 chirality, P3 anomaly engine) are migrated as Pipeline entities
- [ ] All 8 surveys + their anomaly catalogs are migrated as Datasets
- [ ] All 16 contributions are migrated with their full novelty audit history (N-scores intact)
- [ ] All 142 wiki entries are migrated into the lab's knowledge base
- [ ] The H200 RunPod pod is registered to this lab as its primary compute resource
- [ ] All ~21 BigBounce agents (per PRD §3) are bootstrapped under the new lab's orchestrator
- [ ] All peer reviews from `project-context/peer-reviews/` are migrated as comm-events
- [ ] The lab's first standup runs successfully
- [ ] The lab's orchestrator can dispatch one new experiment end-to-end
- [ ] The lab's `/chat` flow works and one chat is graduated to a Project successfully
- [ ] The original `bigbounce.hubify.app` is still serving (sanity check)
- [ ] Houston signs off

### 0.3 Open subdomain decision

Houston flagged in his 2026-04-08 batch that `bigbounce2.hubify.app` is a placeholder. The options:

| Option | Subdomain | Pros | Cons |
|---|---|---|---|
| **(a) `bigbounce2.hubify.app`** | the placeholder | obvious naming, no conflict | "v2" feels temporary, ugly |
| **(b) `bb.hubify.app`** | shortest | clean, memorable | too cryptic for first-time visitors |
| **(c) `bounce.hubify.app`** | short + readable | clean | doesn't say "big bounce" |
| **(d) Repurpose `bigbounce.hubify.app`** post-cutover | aggressive | best long-term name | requires retiring the original site |

**My recommendation: (d)** — repurpose `bigbounce.hubify.app` after cutover. The original repo becomes the historical canonical archive (frozen, untouched on disk + GitHub). The DNS for `bigbounce.hubify.app` flips to the new lab's Vercel deploy. The original site can be archived to `bigbounce-original.hubify.app` or just left in the repo without a public URL. This is the most aggressive but the cleanest long-term outcome.

**Conservative alternative: (a)** — `bigbounce2.hubify.app`. Both sites run in parallel forever. Less risk, uglier URL.

**Houston decision required before §3 (DNS cutover step) executes.**

---

## 1. Inventory — what's actually being migrated

This section documents EVERY artifact in the original BigBounce repo so the migration can be verified comprehensive.

### 1.1 Papers (4)

| # | Title | Path in original repo | Status | Target Project |
|---|---|---|---|---|
| 1 | Spin-Torsion Cosmology: 14 ECH Barriers, ALP Birefringence | `arxiv/main.tex` + `arxiv/main.pdf` | v2.2.1, 99% ready, ~24 pp, 63 refs | Project: "14 ECH Barriers" |
| 2 | Parameter-Free f_NL = -35/8 Prediction · SPHEREx 2028 | `research/focused_paper_source_integration/02_full_draft.tex` | v1.3.0, 100% ready, ~12 pp | Project: "f_NL Tracer Pipeline" |
| 3 | DESI DR1 Spectral Anomaly Catalog · 195,829 objects | `pipelines/p3_anomaly_engine/` | v1.0, 95% ready, ~35 pp | Project: "Multi-Survey Anomaly Engine" |
| 4 | Galaxy Chirality Catalog · 8.47M galaxies | `pipelines/p2_chirality/chirality_catalog_paper.tex` + `public/papers/chirality_catalog_paper.pdf` | v1.0, 85% ready, ~20 pp | Project: "Galaxy Chirality" |

**Many-to-many associations** (per PRD §40.4):
- Paper 1 ↔ Project "14 ECH Barriers" (primary), Project "ALP Birefringence" (contributing), Project "Combined PTA Bayes" (contributing)
- Paper 2 ↔ Project "f_NL Tracer Pipeline" (primary)
- Paper 3 ↔ Project "Multi-Survey Anomaly Engine" (primary)
- Paper 4 ↔ Project "Galaxy Chirality" (primary)

### 1.2 Projects (the research threads — derived from inspecting the work)

The original repo doesn't have an explicit "project" concept — the work is organized by `research/foundation_*/` and `research/branch_*/` directories. The migration **groups these into Projects** per the §40 hierarchy.

**Initial Project list (8 projects, derived from the actual research threads):**

1. **14 ECH Barriers** — closes all ECH-specific routes from bounce to dark energy. Primary deliverable: Paper 1. Source dirs: `research/foundation_*` + `research/branch_*`.
2. **ALP Birefringence** — predicts β = 0.27° matching 3.6σ Planck observation. Primary deliverable: Paper 1 §2.4. Source dirs: `research/branch_alp/`.
3. **Combined PTA Bayes** — combined NANOGrav+EPTA+PPTA+IPTA Bayes factor 27.6 for bounce vs SMBHB. Source dirs: `projects/nanograv/`.
4. **f_NL Tracer Pipeline** — parameter-free f_NL = -35/8 prediction, SPHEREx 2028 forecast, multi-tracer recompute. Primary deliverable: Paper 2. Source dirs: `pipelines/p1_highz_tracers/`, `research/paper2/`.
5. **Multi-Survey Anomaly Engine** — 8-survey anomaly detection sweep, 328K anomalies, 12,920 high-z QSOs. Primary deliverable: Paper 3. Source dirs: `pipelines/p3_anomaly_engine/`, `projects/desi-dr1-anomalies/`, `projects/sdss-dr18/`, `projects/erosita-xray/`.
6. **Galaxy Chirality** — 8.47M galaxy handedness catalog, 32x GPU speedup. Primary deliverable: Paper 4. Source dirs: `pipelines/p2_chirality/`.
7. **Quintom-B Discrimination** — w0-wa MCMC favoring quintom-B at 2.3σ, P(quintom-B) = 98.6%. Source dirs: `reproducibility/cosmology/paper1_clean_restart_sync/chains/`.
8. **Spin-Torsion Foundations** — Einstein-Cartan-Holst gravity, the geometric foundation. Source dirs: `research/foundation_*/foundation_a_*` through `foundation_g_*`.

Each Project gets:
- `projects/<slug>/goal.md` (the qualitative target)
- `projects/<slug>/deliverable.md` (the concrete artifact)
- `projects/<slug>/measurable.md` (the metric)
- `projects/<slug>/README.md` (the auto-maintained Overview, per PRD §40.12)
- `projects/<slug>/MIGRATION_PROVENANCE.md` (where it came from in the original repo)

### 1.3 Experiments (53 — derived from `research/` + `pipelines/` runs)

The original repo doesn't have explicit EXP-### IDs. The migration **assigns IDs sequentially based on chronological order** (earliest first) and groups them under the right Project.

**Approach:** walk all directories under `research/`, `pipelines/`, `projects/`, `reproducibility/`. Each subdirectory that contains: a `run.sh` OR a `*.py` driver script OR a `chains/` output dir OR a `results/` output dir gets registered as an Experiment.

**Naming convention:** `EXP-001` through `EXP-053`, with the original directory path preserved in `provenance.path`.

### 1.4 Pipelines (3, explicitly named in the original)

| Pipeline | Path | Steps |
|---|---|---|
| **P1 highz tracers** | `pipelines/p1_highz_tracers/` | 6 steps: cross-match → classify → bias-validate → recompute σ(f_NL) → paper update → release |
| **P2 chirality** | `pipelines/p2_chirality/` | 4 steps: photometry → CNN train → catalog → paper |
| **P3 anomaly engine** | `pipelines/p3_anomaly_engine/` | 5 steps: spectra ingest → autoencoder train → anomaly score → catalog export → paper draft |

Each Pipeline gets:
- `projects/<parent-project>/pipelines/<pipeline-slug>/goal.md`
- `projects/<parent-project>/pipelines/<pipeline-slug>/output.md`
- `projects/<parent-project>/pipelines/<pipeline-slug>/steps/<step-slug>/` (one subdir per step, each containing the experiment's files)

### 1.5 Datasets (8 surveys + ~12 derived datasets)

**8 surveys (raw inputs):**

| Survey | Catalog file | Anomalies |
|---|---|---|
| DESI DR1 | `pipelines/p3_anomaly_engine/desi_dr1_anomalies.csv` (14.2 MB, 195,829 rows) | 195,829 (0.87%) — 12,920 high-z QSOs at 97% precision after Step 3 |
| SDSS DR18 | `projects/sdss-dr18/sdss_dr18_anomalies.csv` | 77,905 (3.4%) |
| LAMOST DR10 | `pipelines/p3_anomaly_engine/lamost_dr10_anomalies.parquet` | 44,075 (0.39%) — QC: 98% blue-excess bias |
| eROSITA DR1 | `projects/erosita-xray/erosita_dr1_anomalies.csv` | 9,303 (1%) — 73% novel |
| Planck CMB | `projects/planck/planck_cmb_anomalies.csv` | 200 — QC FAIL: needs galactic mask |
| ACT DR6 | `projects/act/act_dr6_anomalies.csv` | 200 — QC FAIL: undertrained val_loss=22420 |
| Gaia DR3 | `projects/gaia/gaia_dr3_anomalies.csv` | 500 — needs 10x expansion |
| NEOWISE | `projects/neowise/neowise_anomalies.csv` | 436 — QC FAIL: ecliptic systematic |

**~12 derived datasets** (not exhaustive — discovered during the import walk):
- Galaxy chirality catalog (`pipelines/p2_chirality/chirality_catalog_8.47M.h5`)
- Spin-torsion MCMC chains (`reproducibility/cosmology/.../spin_torsion.*.txt`)
- High-z QSO candidates (`/workspace/bigbounce/outputs/p1-qso-classifier/highz_qso_candidates.csv` — currently on H200 pod)
- f_NL Fisher matrix outputs
- Combined PTA chains
- Galaxy spin counts
- Anomaly cross-match tables (DESI×eROSITA, SDSS×LAMOST, etc.)

Each dataset gets:
- `projects/<parent-project>/datasets/<dataset-slug>/data` (the file or symlink)
- `projects/<parent-project>/datasets/<dataset-slug>/metadata.json` (provenance, schema, QC status, N rows, derived from)
- `projects/<parent-project>/datasets/<dataset-slug>/README.md` (auto-maintained description)

### 1.6 Contributions (16, with N-scores intact)

The original repo's `contributions.html` page is the canonical list. Each contribution gets migrated as a `contribution` entity with:
- `n_score` (N0-N4 per PRD §40.6 / Houston's existing nomenclature)
- `paper_refs` (which papers this lives in)
- `experiment_refs` (which experiments produced it)
- `novelty_audit_history` (initial review, 7-day re-review, 30-day re-review, etc.)
- `next_review_date`
- `validated_by` (cross-provider reviewers who confirmed it)

**Top 5 contributions by N-score (verbatim from the existing dossier):**
1. f_NL = -35/8 prediction — N3 (the strongest claim, parameter-free)
2. 14 ECH structural barriers framework — N3 (the framework contribution)
3. ALP cosmic birefringence β = 0.27° — N3 (matches observation)
4. Combined PTA Bayes factor 27.6 — N2 (first computation in this combination)
5. Quintom-B w-crossing 2.3σ — N2 (within an existing framework)

(Plus 11 more — full list in `bigbounce/contributions.html`.)

**N4 status:** intentionally NEVER claimed. Houston is underrating to avoid overclaim per PRD §40.6.

### 1.7 Wiki entries (142)

Source: `bigbounce/wiki/` (Karpathy-style structured knowledge base).

Migration: copy verbatim into `lab/wiki/` in the new repo. Schema preserved per `bigbounce/wiki/SCHEMA.md`. The wiki is the lab's persistent knowledge base — entities, concepts, sources, comparisons.

### 1.8 Peer reviews (~30+ files, growing)

Source: `bigbounce/project-context/peer-reviews/`. Each peer review file is named `YYYY-MM-DD_HHMMtz_description.md` and contains the full review from a non-Anthropic provider (GPT, Gemini, Grok, Perplexity, Claude skeptic-mode).

Migration: copy verbatim into `lab/peer-reviews/` in the new repo. Each file gets registered as a `comm-event` in the lab's activity feed with:
- `from_agent`: the cross-provider reviewer (e.g. `peer-review-gpt`)
- `to_agent`: the relevant lead (usually `paper-lead` or `research-lead`)
- `target`: the paper or claim being reviewed
- `verdict`: APPROVE / REQUEST CHANGES / REJECT
- `attached_file`: the original review markdown

### 1.9 Standups (auto-generated, archive)

Source: `bigbounce/standups/` (if exists, else generated from `project-context/`).

Migration: copy verbatim. Each standup becomes a `standup` entity in the new lab's activity timeline. New standups (post-migration) start fresh in the new lab's standup cron.

### 1.10 Compute resources

**The H200 pod** (`o76k3jfzbfh25e` "sleepy_blush_crane", `root@205.196.19.52:11452`):
- Currently active per `project-context/active_pods_and_pipelines.md`
- Migrated as a `compute_resource` entity registered to the new lab
- The lab's `gpu-manager-lead` agent takes over pod monitoring duties from the current Claude session
- SSH credentials migrate from local `~/.ssh/id_ed25519` to the lab's secrets store (Convex env vars OR a secrets vault — TBD)
- Pod state preserved: any in-flight experiments continue running; the new orchestrator picks them up via the heartbeat watchdog

**Backups** (currently 4 destinations per `feedback_external_backups.md`):
- Backblaze B2 (cold, daily) → migrated as a backup destination
- Local external SSD → migrated
- iCloud (selected dirs only) → migrated
- GitHub LFS (large binaries via git-lfs) → already part of the repo migration

### 1.11 Live website assets

Source: `bigbounce/*.html`, `bigbounce/style.css`, `bigbounce/articles/`, `bigbounce/public/`, `bigbounce/research/project_master_dossier/`.

Migration: copy verbatim into `lab/site/` in the new repo. The new lab's Vercel deploy serves from this directory. The original site keeps serving from the original repo until cutover (per §3 below).

### 1.12 What does NOT migrate (stays in the original repo only)

- `.git/` history of the original repo (the new repo gets a fresh git history starting with the import commit)
- Backup directories (`bigbounce-backup-20260407/`)
- Build artifacts (`*.aux`, `*.log`, `*.out`, `*.toc` from LaTeX compiles)
- Cache directories (`__pycache__/`, `.pytest_cache/`, `node_modules/` if any)
- Temporary scratch files in `/tmp/`
- Personal local config (`.env`, `.envrc`, `~/.ssh/`)

These are explicitly listed in `.gitignore` of the new repo and verified absent post-import.

---

## 2. The migration steps (executable order)

This section is the literal step-by-step plan. Each step has a checklist, an estimated time, and a rollback plan.

### Step 0 — Pre-migration safety backups (1 hour)

**Goal:** Ensure the original repo can be restored to its current exact state if anything goes wrong.

```bash
# 0.1 — Local snapshot
cp -r ~/Desktop/CODE_2025/bigbounce ~/Desktop/CODE_2025/bigbounce-pre-migration-2026-04-08
ls -la ~/Desktop/CODE_2025/bigbounce-pre-migration-2026-04-08/CLAUDE.md  # verify

# 0.2 — GitHub archive (rename-safe via fork)
gh repo fork Hubify-Projects/bigbounce \
  --org Hubify-Projects \
  --fork-name bigbounce-pre-migration-archive-2026-04-08 \
  --clone=false
gh repo view Hubify-Projects/bigbounce-pre-migration-archive-2026-04-08  # verify

# 0.3 — Backblaze B2 snapshot (the original cold backup)
cd ~/Desktop/CODE_2025/bigbounce
b2 sync . b2://bigbounce-bb/pre-migration-2026-04-08/

# 0.4 — H200 pod state snapshot
ssh -p 11452 root@205.196.19.52 'tar czf /workspace/pre-migration-snapshot-$(date +%F).tar.gz /workspace/bigbounce/'
# Pull it back to local for safety
scp -P 11452 root@205.196.19.52:/workspace/pre-migration-snapshot-2026-04-08.tar.gz ~/Desktop/CODE_2025/

# 0.5 — Verification gate
echo "All 4 backups exist:"
ls -la ~/Desktop/CODE_2025/bigbounce-pre-migration-2026-04-08
ls -la ~/Desktop/CODE_2025/pre-migration-snapshot-2026-04-08.tar.gz
gh repo view Hubify-Projects/bigbounce-pre-migration-archive-2026-04-08
b2 ls bigbounce-bb/pre-migration-2026-04-08/ | head
echo "ALL 4 BACKUPS VERIFIED — safe to proceed to Step 1"
```

**Rollback:** if anything goes wrong from this point on, the original repo can be restored from any of these 4 backups in <30 min.

### Step 1 — Create the new lab repo (15 min)

**Goal:** A fresh `Hubify-Labs/bigbounce-hubify` GitHub repo + a local working tree at `~/Desktop/CODE_2025/bigbounce-hubify/`.

```bash
# 1.1 — Create local directory
mkdir ~/Desktop/CODE_2025/bigbounce-hubify
cd ~/Desktop/CODE_2025/bigbounce-hubify
git init
git checkout -b main

# 1.2 — Create GitHub repo
gh repo create Hubify-Labs/bigbounce-hubify \
  --private \
  --description "Bounce cosmology research lab — Houston Golden — migrated to Hubify Labs 2026-04-08" \
  --source=. \
  --remote=origin

# (post org rename: this command targets the new org)
# (pre org rename: temporarily uses Hubify-Projects, will be auto-redirected after rename)

# 1.3 — Initial commit (empty .gitignore + LICENSE + README)
cat > .gitignore <<'EOF'
# Python
__pycache__/
*.pyc
.pytest_cache/
.venv/

# LaTeX build artifacts
*.aux
*.log
*.out
*.toc
*.synctex.gz
*.bbl
*.blg

# Editor / OS
.DS_Store
.vscode/
.idea/
*.swp

# Secrets / env
.env
.envrc

# Backup snapshots
*-backup-*/
*-pre-migration-*/

# Node (if any)
node_modules/
EOF

cat > README.md <<'EOF'
# Bounce Cosmology Lab (Hubify Labs)

> Migrated from `Hubify-Projects/bigbounce` on 2026-04-08 — see `MIGRATION_PROVENANCE.md`.

**Mission:** Demonstrate that bounce cosmology fits observational and mathematical
constraints better than ΛCDM + inflation.

**North star:** Verified novel scientific contributions toward the bounce-vs-inflation
question per month, weighted by N-score (N0 → N4).

**Director:** Houston Golden  ·  houston@hubify.com
**Site:** [bigbounce2.hubify.app](https://bigbounce2.hubify.app) (or final subdomain)
**Hubify Labs:** [hubify-labs.com](https://hubify-labs.com)
EOF

git add .
git commit -m "init: bigbounce-hubify lab repo bootstrap"
git push -u origin main
```

**Rollback:** delete the new repo on GitHub + delete `~/Desktop/CODE_2025/bigbounce-hubify/`. Original is untouched.

### Step 2 — File-system import (2-3 hours)

**Goal:** Walk the original repo, copy each artifact into the right place under the new lab structure, attach provenance metadata.

This is the largest step. It runs as a Python script that:
1. Reads `~/Desktop/CODE_2025/bigbounce/` recursively
2. Classifies each file/directory by content + path heuristics into one of: paper, project, pipeline, experiment, dataset, contribution, wiki entry, peer review, standup, site asset, ignore
3. Generates the new lab directory structure under `~/Desktop/CODE_2025/bigbounce-hubify/`
4. Copies the file with `cp` (preserving timestamps via `cp -p`)
5. Writes a `MIGRATION_PROVENANCE.md` for each migrated artifact pointing back to the original path
6. Generates `goal.md` / `deliverable.md` / `measurable.md` for each Project from a hand-curated config (see below)
7. Generates the inventory tables from §1 of this doc as `lab/INVENTORY.md`

**The hand-curated Project config** (the import script reads this):

```yaml
# projects.yaml — the 8 Projects derived from the original repo's structure
projects:
  - slug: ech-barriers
    name: "14 ECH Barriers"
    goal: "Close all ECH-specific routes from bounce to dark energy by direct calculation."
    deliverable: "Paper 1 — Spin-Torsion Cosmology: 14 ECH Barriers, ALP Birefringence (revtex4-2 / PRD)"
    measurable: "Number of barriers closed = 14 (target 14 — DONE). Bounce-vs-inflation Bayes factor (target > 10)."
    source_dirs:
      - research/foundation_a_*
      - research/foundation_b_*
      - research/foundation_c_*
      - research/foundation_d_*
      - research/foundation_e_*
      - research/foundation_f_*
      - research/foundation_g_*
      - research/branch_h_*
      - research/branch_*  # all post-AG branches
    primary_paper: 1
    contributing_papers: []

  - slug: alp-birefringence
    name: "ALP Birefringence"
    goal: "Predict and confirm the cosmic birefringence angle β from axion-like particles in matter-bounce."
    deliverable: "§2.4 of Paper 1 + the β prediction file"
    measurable: "β prediction = 0.27° vs observed 0.342 ± 0.094° (target: within 1σ)."
    source_dirs:
      - research/branch_alp/
      - research/branch_v_*  # birefringence-related branches
    primary_paper: null
    contributing_papers: [1]

  - slug: combined-pta-bayes
    name: "Combined PTA Bayes"
    goal: "Combine NANOGrav + EPTA + PPTA + IPTA data into a single Bayes factor for bounce vs SMBHB."
    deliverable: "§4.3 of Paper 1 + the combined PTA chain output"
    measurable: "Combined Bayes factor (target: > 10 for bounce). Currently: 27.6, SMBHB excluded at 2.7σ."
    source_dirs:
      - projects/nanograv/
      - reproducibility/cosmology/.../chains/dneff/  # PTA-related chains
    primary_paper: null
    contributing_papers: [1]

  - slug: fnl-tracer-pipeline
    name: "f_NL Tracer Pipeline"
    goal: "Achieve σ(f_NL) ≈ 0.95 for SPHEREx 2028 forecast via multi-tracer high-z QSO purification."
    deliverable: "Paper 2 — Parameter-Free f_NL = -35/8 Prediction (revtex4-2 / PRL)"
    measurable: "σ(f_NL) target ≈ 0.95 multi-tracer; current σ(f_NL) = 8.12 multi-tracer pre-purification → target post-purification."
    source_dirs:
      - pipelines/p1_highz_tracers/
      - research/paper2/
      - research/focused_paper_source_integration/
    primary_paper: 2
    contributing_papers: []

  - slug: anomaly-engine
    name: "Multi-Survey Anomaly Engine"
    goal: "Detect, classify, and cross-match spectral anomalies across all 8 surveys at scale."
    deliverable: "Paper 3 — DESI DR1 Spectral Anomaly Catalog (ApJS) + the public catalog files"
    measurable: "Total anomalies catalogued (currently 328,448). QC pass rate per survey (target: 7/8 PASS, currently 4/8 PASS — Planck/ACT/NEOWISE/Gaia need work)."
    source_dirs:
      - pipelines/p3_anomaly_engine/
      - projects/desi-dr1-anomalies/
      - projects/sdss-dr18/
      - projects/erosita-xray/
      - projects/cross_survey/
    primary_paper: 3
    contributing_papers: []

  - slug: galaxy-chirality
    name: "Galaxy Chirality"
    goal: "Build the largest galaxy handedness catalog and test for chirality asymmetry."
    deliverable: "Paper 4 — Galaxy Chirality Catalog (MNRAS) + the 8.47M galaxy catalog"
    measurable: "Catalog size (currently 8,470,000 galaxies). Symmetry test result (currently 0.4σ — null result)."
    source_dirs:
      - pipelines/p2_chirality/
    primary_paper: 4
    contributing_papers: []

  - slug: quintom-b-discrimination
    name: "Quintom-B Discrimination"
    goal: "Discriminate quintom-B (w-crossing) from ΛCDM and other dark-energy models via DESI Y1 BAO."
    deliverable: "§5.2 of Paper 1 + the quintom MCMC chains"
    measurable: "P(quintom-B | data) — currently 98.6%. w-crossing significance — currently 2.3σ."
    source_dirs:
      - reproducibility/cosmology/paper1_clean_restart_sync/
      - research/branch_quintom*
    primary_paper: null
    contributing_papers: [1]

  - slug: spin-torsion-foundations
    name: "Spin-Torsion Foundations"
    goal: "Establish the geometric foundation of Einstein-Cartan-Holst gravity with fermionic torsion."
    deliverable: "§3 of Paper 1 + the Foundation studies A-G writeup"
    measurable: "Foundation studies completed (target: A through G — DONE)."
    source_dirs:
      - research/foundation_*
    primary_paper: null
    contributing_papers: [1]
```

The import script generates the directory tree:

```
~/Desktop/CODE_2025/bigbounce-hubify/
├── README.md
├── MIGRATION_PROVENANCE.md         ← top-level migration log
├── lab/
│   ├── lab.yaml                    ← Mission, North Star, Director, etc.
│   ├── INVENTORY.md                ← generated from §1 of this doc
│   ├── projects/
│   │   ├── ech-barriers/
│   │   │   ├── goal.md
│   │   │   ├── deliverable.md
│   │   │   ├── measurable.md
│   │   │   ├── README.md           ← auto-maintained Overview
│   │   │   ├── MIGRATION_PROVENANCE.md
│   │   │   ├── pipelines/
│   │   │   ├── experiments/
│   │   │   ├── datasets/
│   │   │   ├── chats/
│   │   │   └── notes/
│   │   ├── alp-birefringence/
│   │   ├── combined-pta-bayes/
│   │   ├── fnl-tracer-pipeline/
│   │   ├── anomaly-engine/
│   │   ├── galaxy-chirality/
│   │   ├── quintom-b-discrimination/
│   │   └── spin-torsion-foundations/
│   ├── papers/                     ← canonical paper sources, M:M with projects via project_papers.yaml
│   │   ├── 1-spin-torsion-14-barriers/
│   │   ├── 2-fnl-prediction/
│   │   ├── 3-desi-anomaly-catalog/
│   │   └── 4-galaxy-chirality/
│   ├── project_papers.yaml         ← M:M join table
│   ├── wiki/                       ← migrated from bigbounce/wiki/
│   ├── peer-reviews/               ← migrated peer review files
│   ├── standups/                   ← migrated standup files
│   ├── compute/
│   │   ├── pods.yaml               ← H200 pod registration
│   │   └── credentials/            ← (gitignored — Convex env vars hold the real secrets)
│   ├── agents/                     ← per-agent .md / .soul.md / .skills/ etc per PRD §34
│   │   ├── bigbounce-orchestrator/
│   │   ├── research-lead/
│   │   ├── paper-lead/
│   │   ├── anomaly-lead/
│   │   ├── gpu-manager-lead/
│   │   ├── publishing-lead/
│   │   ├── peer-review-gpt/
│   │   ├── peer-review-gemini/
│   │   ├── peer-review-grok/
│   │   ├── fact-check-perplexity/
│   │   ├── skeptic-cross/
│   │   ├── anomaly-worker/
│   │   ├── pdf-qa-worker/
│   │   ├── claims-audit-worker/
│   │   ├── figure-package-worker/
│   │   ├── arxiv-format-worker/
│   │   ├── storage-map-worker/
│   │   ├── crossmatch-worker/
│   │   ├── cosmology-worker/
│   │   ├── figure-worker/
│   │   └── ... (~21 total per PRD §3)
│   ├── chats/                      ← lab-wide chats (not project-scoped)
│   ├── notes/                      ← Houston's lab-wide journal (per PRD §38)
│   ├── memory/                     ← 4-layer memory store (user/agent/lab/global)
│   ├── routines/                   ← cron schedules
│   ├── backups/                    ← backup destination configs
│   └── site/                       ← migrated bigbounce.hubify.app HTML/CSS/JS
└── .gitignore
```

**The import script** (`scripts/import_bigbounce.py`) is implemented post-spec — see Step 2.5 below for its high-level pseudocode.

**Step 2 checklist:**
- [ ] `projects.yaml` exists and matches §1.2 inventory
- [ ] `lab/projects/` has 8 subdirectories
- [ ] Each project subdir has `goal.md`, `deliverable.md`, `measurable.md`, `README.md`, `MIGRATION_PROVENANCE.md`
- [ ] `lab/papers/` has 4 subdirectories with the source `.tex` + compiled `.pdf`
- [ ] `lab/project_papers.yaml` join table is correct (Paper 1 ↔ multiple projects, Paper 2/3/4 ↔ single primary project)
- [ ] All 53 experiments are placed under their right project (or pipeline step)
- [ ] All 3 pipelines are correctly structured under their parent project
- [ ] All 8 surveys are migrated as datasets with metadata
- [ ] All 16 contributions are migrated with N-scores intact
- [ ] All 142 wiki entries copied verbatim
- [ ] All peer reviews copied verbatim
- [ ] H200 pod registered in `lab/compute/pods.yaml`
- [ ] Site assets copied to `lab/site/`
- [ ] `lab/INVENTORY.md` generated and matches §1 of this doc
- [ ] First commit + push: `git commit -am "import: full BigBounce migration from Hubify-Projects/bigbounce@<sha>"`

**Rollback:** delete `~/Desktop/CODE_2025/bigbounce-hubify/` and the GitHub repo. Original is still untouched. Re-run from Step 1 with fixes to the import script.

### Step 2.5 — Import script pseudocode

```python
# scripts/import_bigbounce.py — runs ONCE during migration
# Reads ~/Desktop/CODE_2025/bigbounce, writes to ~/Desktop/CODE_2025/bigbounce-hubify

import yaml, shutil, json
from pathlib import Path

SRC = Path.home() / "Desktop/CODE_2025/bigbounce"
DST = Path.home() / "Desktop/CODE_2025/bigbounce-hubify"

# 1. Load the hand-curated project config
projects = yaml.safe_load((Path(__file__).parent / "projects.yaml").read_text())["projects"]

# 2. Bootstrap directory tree
for p in projects:
    proj_dir = DST / "lab/projects" / p["slug"]
    proj_dir.mkdir(parents=True, exist_ok=True)
    (proj_dir / "goal.md").write_text(f"# Goal\n\n{p['goal']}\n")
    (proj_dir / "deliverable.md").write_text(f"# Deliverable\n\n{p['deliverable']}\n")
    (proj_dir / "measurable.md").write_text(f"# Measurable\n\n{p['measurable']}\n")
    # README is auto-maintained by orchestrator post-import
    (proj_dir / "README.md").write_text(f"# {p['name']}\n\n{p['goal']}\n\n*Auto-maintained by orchestrator.*\n")

# 3. Copy each source dir into the right project
for p in projects:
    proj_dir = DST / "lab/projects" / p["slug"]
    for src_pattern in p["source_dirs"]:
        for src_path in SRC.glob(src_pattern):
            if not src_path.exists():
                continue
            # Determine target subdir based on what kind of artifact this is
            if "pipeline" in str(src_path):
                target = proj_dir / "pipelines" / src_path.name
            elif "chains" in str(src_path) or "results" in str(src_path):
                target = proj_dir / "datasets" / src_path.name
            else:
                target = proj_dir / "experiments" / src_path.name
            shutil.copytree(src_path, target, dirs_exist_ok=True)
            # Write provenance
            (target / "MIGRATION_PROVENANCE.md").write_text(
                f"# Migration provenance\n\n"
                f"**Source:** `{src_path.relative_to(SRC)}` in `Hubify-Projects/bigbounce`\n"
                f"**Migrated:** 2026-04-08\n"
                f"**Migration script:** `scripts/import_bigbounce.py`\n"
            )

# 4. Copy papers
papers_src = SRC / "arxiv"
shutil.copytree(papers_src, DST / "lab/papers/1-spin-torsion-14-barriers", dirs_exist_ok=True)
# ... (other 3 papers)

# 5. Copy wiki, peer reviews, standups, site assets
shutil.copytree(SRC / "wiki", DST / "lab/wiki", dirs_exist_ok=True)
shutil.copytree(SRC / "project-context/peer-reviews", DST / "lab/peer-reviews", dirs_exist_ok=True)
# ... (standups, site)

# 6. Generate the M:M project_papers join table
join = {
    "papers": [
        {"id": 1, "title": "Spin-Torsion 14 Barriers", "primary_project": "ech-barriers",
         "contributing_projects": ["alp-birefringence", "combined-pta-bayes", "spin-torsion-foundations", "quintom-b-discrimination"]},
        {"id": 2, "title": "f_NL Prediction", "primary_project": "fnl-tracer-pipeline", "contributing_projects": []},
        {"id": 3, "title": "DESI Anomaly Catalog", "primary_project": "anomaly-engine", "contributing_projects": []},
        {"id": 4, "title": "Galaxy Chirality", "primary_project": "galaxy-chirality", "contributing_projects": []},
    ]
}
(DST / "lab/project_papers.yaml").write_text(yaml.safe_dump(join))

# 7. Generate top-level lab.yaml
lab_yaml = {
    "name": "Bounce Cosmology Lab",
    "slug": "bigbounce-hubify",
    "mission": "Demonstrate that bounce cosmology fits observational and mathematical constraints better than ΛCDM + inflation.",
    "north_star": "Verified novel scientific contributions toward the bounce-vs-inflation question per month, weighted by N-score.",
    "director": "Houston Golden",
    "director_email": "houston@hubify.com",
    "subdomain": "bigbounce2.hubify.app",  # or final
    "repo": "Hubify-Labs/bigbounce-hubify",
    "migrated_from": "Hubify-Projects/bigbounce",
    "migrated_at": "2026-04-08",
    "platform_version": "1.0.0",  # Hubify Labs platform version at time of migration
}
(DST / "lab/lab.yaml").write_text(yaml.safe_dump(lab_yaml))

# 8. Print summary
print("Migration import complete:")
print(f"  Projects: {len(projects)}")
print(f"  Papers: 4")
print(f"  Wiki entries: {len(list((DST / 'lab/wiki').glob('**/*.md')))}")
print(f"  Peer reviews: {len(list((DST / 'lab/peer-reviews').glob('*.md')))}")
print(f"\nNext: bootstrap the orchestrator + leads (Step 3)")
```

This is rough pseudocode — the real script will need more error handling, dry-run mode, and verification gates. But the shape is right.

### Step 3 — Bootstrap the lab orchestrator + agents (1-2 hours)

**Goal:** The new lab has a working orchestrator + leads + workers, identical roster to the BigBounce agents per PRD §3, with each agent's `agent.md`, `soul.md`, `skills/`, `learnings.jsonl`, etc. populated per PRD §34.

**Sub-steps:**

1. **Generate agent files** for all ~21 agents under `lab/agents/<agent-name>/`:
   - `agent.md` — README/identity (auto-generated from PRD §34 templates + per-agent customization)
   - `soul.md` — system prompt (use the prompts from the existing mockup's agent dict as starting points, plus any extensions)
   - `skills/<skill-name>.md` — one file per registered skill
   - `learnings.jsonl` — operational learnings (start empty for new agents, OR copy any existing learnings from the original repo's `project-context/`)
   - `episodes/` — empty initially, populated as the agent runs
   - `tools.json` — available tools list per PRD §34
   - `permissions.json` — file/network/exec scopes per PRD §40.11
2. **Wire the orchestrator's heartbeat cron** — `routines/heartbeat.yaml` schedules a 5-minute orchestrator check that:
   - Pings the H200 pod (via `gpu-manager-lead`)
   - Checks for stale tasks
   - Reports any anomalies to the Director
3. **Wire the standup cron** — 3x/day (morning/midday/evening) per PRD §27
4. **Wire the publish-ready loop trigger** — listens for any paper-status change to "ready_for_review" and kicks off the 5-round loop per PRD §37
5. **First test boot:** the orchestrator wakes up, reads `lab.yaml` + project files, introduces itself, and runs the first standup. The output goes to `lab/standups/<timestamp>.md`.

**Step 3 checklist:**
- [ ] All ~21 agents have their full file structure under `lab/agents/`
- [ ] `routines/heartbeat.yaml` exists and is registered
- [ ] `routines/standups.yaml` exists with 3 cron schedules
- [ ] First standup runs successfully and writes a transcript
- [ ] First heartbeat check runs and reports H200 pod status correctly
- [ ] Orchestrator reads the projects + papers + datasets and produces a valid status summary

**Rollback:** if the orchestrator fails to boot, the issue is almost certainly in the agent prompts or the lab.yaml. Fix and re-run. The repo state is preserved.

### Step 4 — Site deploy (30 min)

**Goal:** The new lab's site (migrated from `bigbounce/*.html`) is live at the chosen subdomain.

```bash
# 4.1 — Configure Vercel project
cd ~/Desktop/CODE_2025/bigbounce-hubify
vercel link --yes  # creates a new Vercel project linked to this repo

# 4.2 — Configure subdomain
vercel domains add bigbounce2.hubify.app  # or final subdomain

# 4.3 — First deploy
vercel deploy --prod

# 4.4 — Verify
curl -I https://bigbounce2.hubify.app/  # should return 200
```

**Step 4 checklist:**
- [ ] Vercel project linked to the new repo
- [ ] Subdomain configured (DNS A or CNAME via Cloudflare or whichever DNS provider)
- [ ] Production deploy succeeds
- [ ] Site loads at the new URL
- [ ] All page routes work (/, /papers, /research, /contributions, etc.)
- [ ] All static assets (PDFs, images, datasets) load correctly
- [ ] **The original `bigbounce.hubify.app` is STILL serving** (sanity check)

**Rollback:** unlink Vercel project. Subdomain DNS reverts to NXDOMAIN. Original site unaffected.

### Step 5 — Compute handoff (1 hour)

**Goal:** The H200 pod is now managed by the new lab's `gpu-manager-lead` agent instead of any local Claude Code session.

**Sub-steps:**

1. **Register the pod** in `lab/compute/pods.yaml`:
   ```yaml
   pods:
     - id: o76k3jfzbfh25e
       name: sleepy_blush_crane
       provider: runpod
       gpu: H200
       host: 205.196.19.52
       ssh_port: 11452
       ssh_user: root
       status: active
       cost_per_hour: 3.50
       attached_volume: workspace-vol-001
       primary_workdir: /workspace/bigbounce
   ```
2. **Migrate SSH credentials** from `~/.ssh/id_ed25519` to the lab's secrets store. Decision pending (per PRD §40.16): Convex env vars vs HashiCorp Vault vs 1Password CLI integration. **Default for v1: Convex env vars** (simplest, secure enough for solo-researcher use case).
3. **Test SSH connectivity** from the orchestrator agent: orchestrator runs `ssh -p 11452 root@205.196.19.52 'nvidia-smi'` and parses the output. If success, the pod is handed off.
4. **Stop any local cron / watchdog** that was monitoring the pod from a Claude Code session. The lab's `gpu-manager-lead` heartbeat cron takes over.
5. **First in-lab experiment dispatch:** orchestrator dispatches a no-op experiment to the pod (just `python -c 'print("hello from in-lab dispatch")'`) to verify the dispatch path works end-to-end.

**Step 5 checklist:**
- [ ] Pod registered in `lab/compute/pods.yaml`
- [ ] SSH credentials migrated to lab secrets store
- [ ] Orchestrator can SSH to pod successfully
- [ ] Local Claude Code pod-watchdog cron is stopped
- [ ] First in-lab dispatch works
- [ ] H200 status visible in the new lab's Compute view

### Step 6 — First end-to-end research cycle (2-4 hours)

**Goal:** Prove the new lab actually does research. Run one full experiment cycle from chat → graduation → experiment → result → contribution.

**Sub-steps:**

1. **Open a new chat** in the lab via the chat composer.
2. **Brain dump:** "Let's recompute σ(f_NL) using the new 12,920 high-z QSOs from Pipeline 1 step 3."
3. **Orchestrator drafts the spec:**
   - Goal: "Recompute the f_NL Fisher matrix using the purified high-z QSO catalog."
   - Deliverable: "Updated σ(f_NL) measurement + a rerun of `p1_fnl_recompute.py`."
   - Measurable: "σ(f_NL) multi-tracer (target: improve from 8.12 toward 0.95)."
   - Mini-plan: 5-7 tasks
4. **Houston says "y"**, orchestrator graduates the chat to a new Project (or attaches to existing `fnl-tracer-pipeline` project — orchestrator decides which is more appropriate).
5. **Orchestrator dispatches the experiment** to the H200 pod via `gpu-manager-lead`.
6. **Experiment runs end-to-end** on the pod, writes outputs to `/workspace/bigbounce/outputs/p1-fnl-recompute-v2/`, and the pod reports completion.
7. **Houston Method post-experiment protocol** runs automatically:
   - QC gate (does the output exist? are the numbers reasonable?)
   - Scientific analysis (paper-lead writes a 3-paragraph interpretation)
   - Cross-survey connection (research-lead checks if this affects other papers)
   - Site sync (the contribution table on the new site updates)
   - Queue expansion (5-15 new tasks generated)
   - Backup (the new outputs go to Backblaze)
   - Standup notes (the next standup mentions this cycle)
8. **One contribution is created** for the result, with N-score TBD (likely N2 — first computation in the new framework).

**Step 6 checklist:**
- [ ] Chat opened, brain dump entered
- [ ] Orchestrator drafted spec with all 4 fields
- [ ] Houston approved
- [ ] Project graduated (or attached to existing)
- [ ] Experiment dispatched to pod
- [ ] Experiment completed successfully
- [ ] All 8 Houston Method post-experiment steps ran
- [ ] One contribution created
- [ ] Standup transcript references this cycle

**This is the proof.** If Step 6 succeeds, the new lab is real and Houston can use it.

### Step 7 — DNS cutover decision (5 min — Houston only)

**Goal:** Decide whether to flip `bigbounce.hubify.app` from the original site to the new lab's site, OR keep both running in parallel.

**Decision:** Houston-only. Deferred from §0.3 above.

If cutover:
- Update DNS A record / CNAME to point `bigbounce.hubify.app` → new Vercel deployment
- Original site moves to `bigbounce-original.hubify.app` (or no public URL)
- Update all backlinks in the new lab's docs and the README

If parallel:
- Both `bigbounce.hubify.app` and `bigbounce2.hubify.app` (or whatever the new subdomain is) keep running
- New work shows on the new site, old archive stays at the old site
- Document the split clearly in both sites' headers

### Step 8 — Post-migration verification (1 hour)

**Goal:** Verify ALL of §0.2's "migration complete" criteria are met. Sign off.

**Run the verification script:**

```bash
cd ~/Desktop/CODE_2025/bigbounce-hubify
python scripts/verify_migration.py
```

The script checks:
- All papers exist with correct metadata
- All projects have goal/deliverable/measurable filled
- All experiments + pipelines + datasets exist
- All contributions have N-scores
- Wiki entry count matches original (142)
- Peer review count matches original
- H200 pod is reachable
- Orchestrator + all agents respond to ping
- First standup transcript exists
- Site is live
- One contribution created via the in-lab cycle (Step 6 result)

**Output:** `verification_report_2026-04-08.md` with a green/red status for each check.

**Sign-off:** Houston reviews the report, runs the new lab through one more chat-and-experiment cycle to confirm it feels right, and signs off in `lab/MIGRATION_SIGNED_OFF.md`.

### Step 9 — Backup the new lab (30 min)

**Goal:** The new lab is now backed up to all 4 destinations per PRD §1.

```bash
cd ~/Desktop/CODE_2025/bigbounce-hubify

# 9.1 — Local backup
cp -r . ~/Desktop/CODE_2025/bigbounce-hubify-backup-2026-04-08

# 9.2 — GitHub (already done via push)

# 9.3 — Backblaze B2
b2 sync . b2://bigbounce-hubify-bb/initial-2026-04-08/

# 9.4 — Hugging Face (for any public model + dataset assets — if applicable)
# Only the public-facing assets, not the whole repo

# 9.5 — Verify
ls -la ~/Desktop/CODE_2025/bigbounce-hubify-backup-2026-04-08/lab/lab.yaml
b2 ls bigbounce-hubify-bb/initial-2026-04-08/ | head
echo "All backups verified — migration officially complete"
```

---

## 3. The order of operations (one-pager summary)

```
Day 1 — Migration day (estimated 8-12 hours total)

Hour 0      Step 0   Pre-migration backups (1h)             [SAFETY GATE]
Hour 1      Step 1   Create new repo (15min)
Hour 1.25   Step 2   File-system import (2-3h)
Hour 4      Step 3   Bootstrap orchestrator + agents (1-2h)
Hour 6      Step 4   Site deploy (30min)
Hour 6.5    Step 5   Compute handoff (1h)
Hour 7.5    Step 6   First end-to-end research cycle (2-4h)  [REAL PROOF]
Hour 11     Step 7   DNS cutover decision (Houston, 5min)
Hour 11     Step 8   Post-migration verification (1h)
Hour 12     Step 9   Backup the new lab (30min)
Hour 12.5   DONE     Houston sign-off
```

---

## 4. Cross-lab sharing setup (per PRD §40.11)

After the migration, the new BigBounce Lab gets its sharing settings configured:

**Default for the migrated lab:**
- Internal cross-lab share: `read-only` (other Hubify Labs labs can read this lab's files)
- Public share: `published-only` (only papers explicitly marked as published are visible to the world)

**Pre-configured sharing relationships** (set up during Step 3 of the migration):
- Lab #1 (Bounce Cosmology) ↔ Lab #3 (Dark Energy) — read-only both directions, when Lab #3 is created. The Dark Energy lab inherits the relevant chunks of the Bounce Cosmology research (quintom-B, w-crossing, dark-energy-relevant findings) by reference, not by copy. See `LAB_DARK_ENERGY.md`.
- Lab #1 ↔ Lab #2 (Hubify Self-Improving) — Lab #2 has read-only access to Lab #1's structure for self-improvement learning. Lab #1 does NOT have access to Lab #2 (no need).

---

## 5. Risk register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Original repo accidentally modified | Low | Catastrophic (irreplaceable research) | Iron rule + 4 pre-migration backups + git pre-commit hook on the original repo that blocks commits |
| Import script misclassifies a file (puts it in wrong project) | Medium | Low (re-runnable) | Dry-run mode + verification script + manual spot-check |
| Orchestrator fails to boot in the new lab | Medium | Medium (delays Step 6) | Test agent prompts in isolation first; have rollback to previous PRD §3 prompts |
| Subdomain DNS doesn't propagate in time | Low | Low (just delays Step 4 verification) | Configure DNS the day before, leaving 24h propagation window |
| H200 pod becomes unreachable mid-migration | Low | Medium (Step 5 + 6 blocked) | Verify pod is up before starting; have a fallback plan to use a fresh RunPod instance if needed |
| Houston's BigBounce work goes stale (new commits to the original repo while migration runs) | Medium | Low (just need to re-run import script) | Migrate during a quiet day; freeze new commits to the original repo for 24h |
| The first in-lab research cycle (Step 6) fails to produce a real result | Medium | Medium (proves the platform isn't ready) | Pre-validate the whole pipeline in a smaller end-to-end test on a different lab first (e.g., a tiny test lab with synthetic data) |

---

## 6. Open questions for Houston

These need answers before Day 1 of the migration:

1. **Subdomain decision** (per §0.3): which option (a/b/c/d)?
2. **SSH credentials store** (per Step 5): Convex env vars vs HashiCorp Vault vs 1Password CLI? Default = Convex env vars.
3. **DNS cutover timing** (per Step 7): same day as migration, or wait 24-48h to let the new lab burn in?
4. **Quiet day for migration** — when can Houston commit to a full day with no other research happening on the H200?
5. **Test-lab pre-validation** — should we build a tiny test lab with synthetic data first, to validate the whole import + bootstrap + Step 6 pipeline before risking it on the real BigBounce data? My recommendation: **yes**, ~1 day of work, prevents catastrophe.
6. **Mintlify docs port** (per PRD §40.17 Tier 3) — does this happen during the migration or as a separate post-migration project? My recommendation: **separate post-migration**, the docs aren't load-bearing for the lab's first cycle.

---

## 7. Post-migration roadmap (the first month after Day 1)

Once the migration is complete and signed off, the next 30 days:

- **Week 1** — Houston uses the new lab daily. Reports any UX issues. Mockup polish work continues to fix the issues.
- **Week 2** — First chat-to-project graduation in earnest (something Houston actually wants to research, not just the test cycle from Step 6). The chat-graduation flow gets battle-tested.
- **Week 3** — First publish-ready loop run on Paper 1 in the new lab. The 5-round loop per PRD §37 runs end-to-end. Any failures in the loop become priority bug fixes.
- **Week 4** — Cross-lab sharing test: create Lab #3 (Dark Energy) using the platform's "create new lab" flow, share Bounce Cosmology with it, verify the read-only access + comm gateway work. This is the second platform stress test.
- **End of month** — retrospective. What worked, what didn't, what needs to ship in v1.1.

---

## 8. Appendix — file paths cheat sheet

For Houston (and future agents) to find things during and after the migration:

| Thing | Original repo path | New lab path |
|---|---|---|
| Paper 1 source | `arxiv/main.tex` | `lab/papers/1-spin-torsion-14-barriers/main.tex` |
| Paper 1 PDF | `arxiv/main.pdf` | `lab/papers/1-spin-torsion-14-barriers/main.pdf` |
| Paper 2 source | `research/focused_paper_source_integration/02_full_draft.tex` | `lab/papers/2-fnl-prediction/main.tex` |
| Paper 3 sources | `pipelines/p3_anomaly_engine/` | `lab/papers/3-desi-anomaly-catalog/` |
| Paper 4 source | `pipelines/p2_chirality/chirality_catalog_paper.tex` | `lab/papers/4-galaxy-chirality/main.tex` |
| references.bib | `arxiv/references.bib` | `lab/papers/1-spin-torsion-14-barriers/references.bib` (each paper has its own copy) |
| MCMC chains | `reproducibility/cosmology/.../chains/` | `lab/projects/quintom-b-discrimination/datasets/chains/` |
| DESI anomaly catalog | `pipelines/p3_anomaly_engine/desi_dr1_anomalies.csv` | `lab/projects/anomaly-engine/datasets/desi-dr1-anomalies/data.csv` |
| 12,920 high-z QSOs | `/workspace/bigbounce/outputs/p1-qso-classifier/highz_qso_candidates.csv` (on H200 pod) | Same path on pod, registered in `lab/projects/fnl-tracer-pipeline/datasets/highz-qso-12920/` |
| Wiki | `wiki/` | `lab/wiki/` |
| Peer reviews | `project-context/peer-reviews/` | `lab/peer-reviews/` |
| CLAUDE.md | `CLAUDE.md` | `CLAUDE.md` (rewritten for the new lab structure) |
| Project context | `project-context/` | `lab/project-context/` (lab-specific bits) + `lab/projects/<slug>/` (project-specific bits) |
| Site HTML | `*.html`, `style.css`, `articles/` | `lab/site/` |
| Dossier | `research/project_master_dossier/index.html` | `lab/site/dossier/index.html` |

---

## 9. Final word

This migration is the proof that Hubify Labs is a real product, not a mockup. The bar is: Houston can wake up the day after the migration, open the new lab, and continue his research without missing a beat — same papers, same data, same pod, same agents, but now organized under the §40 hierarchy with the orchestrator running standups and the publish-ready loop and the cross-model peer review and everything else the platform promises.

If the migration succeeds, Hubify Labs is real.

If the migration fails, we fix it and try again. The original BigBounce repo never changes, so the cost of failure is just time, not data.

**Houston's super-super-clear #1 priority. Let's ship it.**
