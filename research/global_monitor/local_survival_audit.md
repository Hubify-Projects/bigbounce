# Local Survival Audit — BigBounce MCMC Recovery Assets

**Date:** 2026-03-10 22:00 UTC
**Mode:** READ-ONLY — no files modified or deleted
**Context:** All 3 Paper-1 RunPod pods terminated. This audit catalogs every
surviving local artifact to determine what can be resumed vs restarted.

---

## Executive Summary

| Source | Samples at Shutdown | Locally Preserved | Classification |
|--------|--------------------|--------------------|----------------|
| GPU chains | ~140,342 | 14,021 (10%) | WARM RESTART |
| CPU#1 chains | 48,820 | 0 (0%) | COLD RESTART |
| CPU#2 chains | 49,643 | 0 (0%) | COLD RESTART |
| **Total** | **236,622** | **14,021 (5.9%)** | |

**Key finding:** GPU chains can warm-restart from surviving covmats + early chain
files. CPU chains must cold-restart but can borrow GPU covmats. All convergence
diagnostics from the final 2026-03-09 audit survive intact.

---

## 1. GPU Surviving Assets

### Primary Snapshot: `gpu_run_snapshot_20260305_0824`
**Location:** `reproducibility/cosmology/archives/gpu_run_snapshot_20260305_0824/`
**Tarball:** `gpu_run_snapshot_20260305_0824.tar.gz` (3.5 MB)
**Snapshot date:** 2026-03-05 08:24 UTC (~24h into GPU run)

#### Chain Files (28 chains, 4 datasets x 7 chains)

| Dataset | ch1 | ch2 | ch3 | ch4 | ch5 | ch6 | ch7 | Total |
|---------|-----|-----|-----|-----|-----|-----|-----|-------|
| full_tension | 240 | 752 | 593 | 787 | 730 | 896 | 601 | **4,599** |
| planck_only | 122 | 299 | 337 | 308 | 372 | 412 | 358 | **2,208** |
| planck_bao | 97 | 422 | 404 | 280 | 287 | 370 | 380 | **2,240** |
| planck_bao_sn | 90 | 323 | 332 | 411 | 480 | 441 | 410 | **2,487** |
| **All** | | | | | | | | **11,534** |

Note: The 20260304 snapshot (2,814 total samples) is a strict subset — superseded.

#### Covmats (28 files — ALL CHAINS)
Every chain directory contains `spin_torsion.covmat` (~6.5-7.5 KB each).
These are the **learned proposal covariance matrices** — the single most valuable
asset for reconvergence speed. They encode the posterior shape discovered during
the initial run and allow Cobaya to skip the burn-in exploration phase entirely.

**Impact:** Using these covmats, new chains will sample at the post-burn-in rate
from step 1, cutting reconvergence time by an estimated 60-80%.

#### YAML Configs (56 files — 28 input + 28 updated)
- `spin_torsion.input.yaml` — original Cobaya config per chain
- `spin_torsion.updated.yaml` — Cobaya's runtime-updated config
- Both survive for all 28 chains

#### Original Cobaya Configs (4 files — top-level)
- `cobaya_full_tension.yaml` (3,184 B)
- `cobaya_planck.yaml` (2,660 B)
- `cobaya_planck_bao.yaml` (2,539 B)
- `cobaya_planck_bao_sn.yaml` (2,576 B)

These are the base configs used to generate per-chain configs. Essential for
reproducing the exact same run setup.

#### Checkpoints
- **Extracted snapshot (20260305):** 0 checkpoint files present
- **Earlier tarball (20260304):** 28 checkpoint files inside `chains.tar.gz`
- The 20260304 checkpoints are from an even earlier state but could enable
  `cobaya-run --resume` if extracted and placed alongside chain files

#### Monitor Scripts (complete evolution)
- `mcmc_monitor_v2.py` through `mcmc_monitor_v6.py` (14-34 KB each)
- `analyze_chains.py`, `launch_parallel_chains.sh`, `monitor_convergence.sh`

#### Trace Plots (16 figures)
- 8 trace plots from `traces/` directory (2026-03-04)
- 8 trace plots from archived `cosmology/` (2026-03-05)
- H0 and delta_neff traces for all 4 datasets

#### MANIFEST
- `MANIFEST.md` — documents hardware, software versions, chain counts, config diffs

### Earlier Snapshot: `runpod_snapshot_20260304`
**Location:** `reproducibility/cosmology/runpod_snapshot_20260304/`
- `chains.tar.gz` (502 KB) — 28 chains, 2,814 total samples
  - **Includes 28 checkpoint files and 28 covmats** (inside tarball)
- `outputs.tar.gz` (51 KB) — Cobaya log files for all chains
- `analysis.txt` (8 KB) — early analysis
- `RECOVERY_README.md` — recovery instructions

---

## 2. CPU#1 Surviving Assets

**Chain files:** ZERO
**Covmats:** ZERO
**Checkpoints:** ZERO
**YAML configs:** ZERO

**Only surviving artifact:**

| File | Path | Size | Date | Rows |
|------|------|------|------|------|
| Convergence CSV | `cpu1_diagnostics/convergence_latest.csv` | 1,335 B | 2026-03-09 | 28 |

Contents: R-hat, ESS, and drift for all 7 parameters across 4 datasets.
This confirms the CPU#1 chains were well-converged at time of loss (e.g.,
full_tension H0 Rm1=0.004, planck_only H0 Rm1=0.008).

**48,820 samples irrecoverably lost. Must cold-restart.**

---

## 3. CPU#2 Surviving Assets

**Chain files:** ZERO
**Covmats:** ZERO
**Checkpoints:** ZERO
**YAML configs:** ZERO

**Only surviving artifact:**

| File | Path | Size | Date | Rows |
|------|------|------|------|------|
| Convergence CSV | `cpu2_diagnostics/convergence_latest.csv` | 1,115 B | 2026-03-09 | 24 |

Contents: R-hat and ESS for LCDM parameters (no delta_neff). CPU#2 LCDM
chains were very well converged (planck_bao_sn H0 Rm1=0.0005, ESS=1369).

**49,643 samples irrecoverably lost. Must cold-restart.**

---

## 4. Shared Orchestration / Monitoring Assets

All monitoring and orchestration code survives locally:

| Asset | Path | Status |
|-------|------|--------|
| Pod registry | `research/global_monitor/pod_registry.yaml` | Intact (needs pod ID updates) |
| Global status script | `research/global_monitor/global_status.py` | Intact |
| Global backup script | `research/global_monitor/global_backup.py` | Intact |
| Freeze manager | `research/global_monitor/gpu_freeze_manager.py` | Intact |
| Monitor runner | `research/global_monitor/run_all_monitors.py` | Intact |
| Shell runner | `research/global_monitor/run_all_monitors.sh` | Intact |
| Hourly loop | `research/global_monitor/hourly_loop.sh` | Intact |
| RunPod API client | `research/runpod_cloud.py` | Intact |

### Historical Records (12 status snapshots, 11 backup records, 8 logs)
- `global_status_history/` — 12 snapshots from 2026-03-05 through 2026-03-06
- `backup_history/` — 11 records
- `logs/` — 8 hourly run logs

### Key Audit Reports
| Report | Date | Content |
|--------|------|---------|
| `live_chain_audit.json` | 2026-03-09 | Complete convergence state at shutdown |
| `live_chain_audit.txt` | 2026-03-09 | Human-readable version (358 lines) |
| `monday_checkin_status.txt` | 2026-03-09 | Full project status |
| `chain_status_20260309.txt` | 2026-03-09 | Chain status snapshot |

---

## 5. Convergence Diagnostics (Final State Before Loss)

The most scientifically valuable surviving data — the complete convergence
picture from the 2026-03-09 live audit:

### GPU Cohort Main (chains 2-7) — from `convergence_cohort_main.csv`

| Dataset | Rm1(H0) | Rm1(ΔN) | Rm1(τ) | ESS(H0) | ESS(ΔN) | ESS(τ) | Gates |
|---------|---------|---------|--------|---------|---------|--------|-------|
| full_tension | 0.0036 | 0.0031 | 0.0071 | 781 | 694 | 1243 | 6/8 |
| planck_only | 0.0042 | 0.0035 | 0.0090 | 569 | 547 | 609 | 5/8 |
| planck_bao_sn | 0.0081 | 0.0126 | 0.0031 | 691 | 565 | 724 | 4/8 |
| planck_bao | 0.0266 | 0.0230 | 0.0059 | 479 | 440 | 840 | 3/8 |

### CPU#1 ΔNeff — from `cpu1_diagnostics/convergence_latest.csv`

| Dataset | Rm1(H0) | Rm1(ΔN) | ESS(H0) | ESS(ΔN) |
|---------|---------|---------|---------|---------|
| full_tension | 0.004 | 0.006 | 118 | 116 |
| planck_only | 0.008 | 0.008 | 123 | 123 |
| planck_bao_sn | 0.008 | 0.006 | 143 | 118 |
| planck_bao | 0.030 | 0.025 | 260 | 243 |

### CPU#2 ΛCDM — from `cpu2_diagnostics/convergence_latest.csv`

| Dataset | Rm1(H0) | ESS(H0) |
|---------|---------|---------|
| full_tension | 0.004 | 489 |
| planck_only | 0.001 | 461 |
| planck_bao_sn | 0.001 | 1369 |
| planck_bao | 0.002 | 587 |

---

## 6. Resume vs Restart Classification

### GPU Chains: WARM RESTART

All 4 GPU datasets have:
- Early chain files (11,534 samples across 28 chains)
- Learned covmats for all 28 chains
- Complete YAML configs (input + updated)
- Checkpoints available inside the 20260304 tarball

**Strategy:** Upload snapshot to new GPU pod. Extract 20260304 checkpoints into
chain directories. Run `cobaya-run <config>.yaml --resume`. Cobaya will:
1. Load the checkpoint state
2. Use the learned covmat as proposal
3. Continue sampling from where it left off (at the 20260305 state)
4. Existing chain samples will be appended to

**Limitation:** Chains resume from the 20260305 checkpoint state, not the
20260309 state. ~126k GPU samples accumulated between 03-05 and 03-09 are lost
and must be re-accumulated. With learned covmats, this should take ~5-7 days.

### CPU#1 Chains: COLD RESTART

No chain data, no covmats, no configs survive from CPU#1.

**Strategy:** Start fresh chains using:
1. The original cobaya YAML configs (survive locally)
2. GPU covmats as the `proposal_matrix` parameter (copy from GPU snapshot)
3. This lets CPU#1 skip burn-in entirely, starting with an informed proposal

**Estimated time:** 7-10 days to reach the convergence state that was lost.

### CPU#2 Chains: COLD RESTART

Same as CPU#1. ΛCDM chains converge faster (no delta_neff dimension), so:

**Estimated time:** 5-7 days to reconverge.

---

## 7. What Survived — Complete List

**Chain data:**
- 28 GPU chain files (11,534 samples) from 20260305 snapshot
- 28 GPU chain files (2,814 samples) from 20260304 tarball (subset)

**Covmats:**
- 28 GPU covmats from 20260305 snapshot (extracted)
- 28 GPU covmats from 20260304 tarball (inside tar)

**Checkpoints:**
- 28 checkpoints inside 20260304 tarball (NOT extracted)
- 0 checkpoints in 20260305 extracted snapshot

**YAML configs:**
- 56 per-chain configs (28 input + 28 updated) from 20260305 snapshot
- 4 original base Cobaya configs
- 24 per-chain configs inside 20260304 tarball

**Convergence diagnostics:**
- GPU cohort_main convergence CSV (final state, 2026-03-09)
- GPU all-chains convergence CSV
- GPU stale convergence CSV (2026-03-05)
- CPU#1 convergence CSV (2026-03-09)
- CPU#2 convergence CSV (2026-03-09)
- Trend monitor output
- GetDist validation
- Freeze check results
- Chain means, bottlenecks, chain summary

**Audit / status reports:**
- Live chain audit (JSON + TXT, 2026-03-09)
- Monday check-in (JSON + TXT, 2026-03-09)
- 12 global status history snapshots
- 11 backup history records
- 8 hourly monitor logs
- Health check, recovery report, storage audit

**Scripts:**
- Monitor v2-v6, analysis, launch, convergence monitoring
- Global status, backup, freeze manager, monitor runner
- RunPod API client, pod registry

**Figures:**
- 16 trace plots (H0 + delta_neff for all 4 datasets, 2 vintages)

**Archives:**
- `gpu_run_snapshot_20260305_0824.tar.gz` (3.5 MB)
- `runpod_snapshot_20260304/chains.tar.gz` (502 KB)
- `runpod_snapshot_20260304/outputs.tar.gz` (51 KB)

---

## 8. What Is Definitely Gone

- **~126,321 GPU samples** accumulated between 2026-03-05 and 2026-03-09
- **All 48,820 CPU#1 chain files**, covmats, checkpoints, configs, and logs
- **All 49,643 CPU#2 chain files**, covmats, checkpoints, configs, and logs
- **5 GPU frozen packs** created 2026-03-05 and 2026-03-07 (archival, on-pod only)
- **On-pod backup tarballs** (hourly GPU backups, never synced to local)
- **Pod-side monitor logs** and convergence history beyond what was synced
- **The convergence state itself** (R-hat < 0.005 on full_tension) — must be re-achieved

---

## 9. What Is Enough to Resume vs Warm Restart vs Cold Restart

| Dataset | Pod | Chain Files | Covmats | Checkpoints | Configs | Classification |
|---------|-----|-------------|---------|-------------|---------|---------------|
| full_tension | GPU | 4,599 samples | 7 | In tarball | 7+7 | **WARM RESTART** |
| planck_only | GPU | 2,208 samples | 7 | In tarball | 7+7 | **WARM RESTART** |
| planck_bao | GPU | 2,240 samples | 7 | In tarball | 7+7 | **WARM RESTART** |
| planck_bao_sn | GPU | 2,487 samples | 7 | In tarball | 7+7 | **WARM RESTART** |
| All 4 datasets | CPU#1 | 0 | 0 | 0 | 0 | **COLD RESTART** |
| All 4 datasets | CPU#2 | 0 | 0 | 0 | 0 | **COLD RESTART** |

**Definitions:**
- **WARM RESTART:** Has covmats + configs + some chain data. Cobaya can use
  learned proposal and resume from existing chain files. Skips burn-in entirely.
- **COLD RESTART:** No chain data or covmats. Must start from scratch. Can
  borrow GPU covmats to skip burn-in (making it a "lukewarm" restart).

---

## 10. Answers

### What survived?
GPU chain files (11,534 samples), all 28 GPU covmats, all YAML configs, all
convergence diagnostics from the final audit, all monitoring scripts, and
complete audit reports. The science narrative is fully documented even though
the raw data is mostly lost.

### What is definitely gone?
~224,784 MCMC samples (95% of total). All CPU chain data. The convergence
state that took 5 days to achieve on GPU and must be re-achieved.

### What is enough to resume?
Nothing qualifies for a true "resume" (which requires the exact checkpoint state
from the moment of shutdown). The 20260309 checkpoint state is gone.

### What is enough for a warm restart?
All 4 GPU datasets. The covmats are the critical asset — they encode the
posterior shape and allow new chains to sample efficiently from step 1.
Combined with the surviving chain files, Cobaya can append new samples to
existing chains using `--resume` with the 20260304 checkpoints.

### What requires a cold restart?
All CPU#1 and CPU#2 datasets. No chain data, covmats, or configs survive.
However, GPU covmats can be provided as initial proposals to significantly
accelerate convergence (estimated 60-80% time savings vs true cold start).
