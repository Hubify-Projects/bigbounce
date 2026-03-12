# RunPod Recovery Log — 2026-03-10 21:30 UTC

## Context
All 3 Paper-1 pods went down between 2026-03-09 21:15 UTC (last live audit) and
2026-03-10 21:13 UTC (health check). SSH connections refused on all pods.
Suspected billing-related shutdown. 236,622 samples across 64 chains at risk.

## Recovery Timeline

### Step 1 — Recovery log created
- Timestamp: 2026-03-10 21:30 UTC
- File: research/global_monitor/runpod_recovery_20260310_2130.md

---

### Step 2 — RunPod API Status Check
- Timestamp: 2026-03-10 21:31 UTC
- Tool: research/runpod_cloud.py (GraphQL API)
- API key: present in .env.local (prefix: rpa_L3XN...)

#### SSH Connection Tests (pre-API)
| Pod | SSH Target | Result |
|-----|-----------|--------|
| GPU validation | 195.26.233.79:38115 | Connection refused |
| CPU#1 primary | 157.157.221.30:30194 | Connection refused |
| CPU#2 secondary | 157.157.221.30:40204 | Connection refused |

#### RunPod API Results

**Account status:**
- User ID: `user_3ASjlBqOLifanwrV3Q6Xe4BHzop`
- Client balance: **$199.99** (NOT a billing issue)
- Current spend: $0.002/hr (only exited pods incurring storage)

**Pods in account (3 total — only Paper-2 pods remain):**
| Pod ID | Name | Status | Volume | Disk |
|--------|------|--------|--------|------|
| bpou58tmt95jjb | paper2-wp4-dneff | EXITED | 0 GB | 50 GB |
| mz3srzbzxxv1yj | paper2-wp5-spin | EXITED | 0 GB | 50 GB |
| uktt3hghbs1djo | paper2-p6-eb | EXITED | 0 GB | 50 GB |

**Paper-1 pod lookups:**
| Pod ID | Name | API Result |
|--------|------|-----------|
| 47htajss1ng2ig | bigbounce-gpu-validation | **NOT FOUND** (HTTP 400) |
| m4xpnxzgokd93f | bigbounce-cpu1-primary | **NOT FOUND** (HTTP 400) |
| eblghcn6u43wfk | bigbounce-cpu2-secondary | **NOT FOUND** (HTTP 400) |
| pkysk4lbaqnhm0 | paper2-p7-cnn | **NOT FOUND** (pod: null) |

**Network volumes:**
| Volume ID | Name | Size | Region |
|-----------|------|------|--------|
| 9wln8f98am | modest_plum_antlion | 20 GB | US-WA-1 |

#### CONCLUSION — STEP 2

**ALL THREE PAPER-1 PODS HAVE BEEN TERMINATED.**

They are not stopped, not exited, not paused — they are completely gone from the
RunPod account. The API returns 400/null for their pod IDs. Their /workspace
volumes are destroyed.

This was NOT caused by billing — the account has $199.99 in credit. The pods
were either:
1. Manually terminated by the operator (unlikely without memory of doing so)
2. Auto-terminated by RunPod due to inactivity policy or platform changes
3. Terminated by RunPod during maintenance

The paper2-p7-cnn pod is also gone (was ALIVE as recently as 2026-03-06).

---

### Step 3 — CANNOT RESTART (pods terminated)

Since all 3 Paper-1 pods are TERMINATED (not stopped), there is nothing to restart.
The pod containers and their /workspace volumes no longer exist on RunPod infrastructure.

**This step is BLOCKED. Moving to data loss assessment.**

---

### Step 4 — Local Data Preservation Assessment

#### What exists locally:

**A. GPU Snapshot (2026-03-05 08:24 UTC) — EARLY DATA**
- Path: `reproducibility/cosmology/archives/gpu_run_snapshot_20260305_0824/`
- Also: `gpu_run_snapshot_20260305_0824.tar.gz` (3.5 MB)
- Contents: 28 chain directories, configs, cosmology dir, monitor scripts
- Sample counts (VERY EARLY — from first ~24h of GPU run):

| Dataset | Samples in snapshot | Samples at shutdown | Recovery % |
|---------|--------------------|--------------------|------------|
| full_tension | 4,599 | ~63,531 | 7.2% |
| planck_only | 2,208 | ~25,345 | 8.7% |
| planck_bao | 4,727 | ~25,246 | 18.7% |
| planck_bao_sn | 2,487 | ~26,220 | 9.5% |
| **GPU Total** | **14,021** | **~140,342** | **10.0%** |

**B. Earlier Snapshot (2026-03-04)**
- Path: `reproducibility/cosmology/runpod_snapshot_20260304/`
- Contents: chains.tar.gz (502 KB), outputs.tar.gz (51 KB), analysis.txt
- This predates the GPU snapshot above — even fewer samples.

**C. Convergence Diagnostics (PRESERVED)**
- `convergence_cohort_main.csv` — full GPU cohort_main R-hat/ESS (from 2026-03-09 audit)
- `cpu1_diagnostics/convergence_latest.csv` — CPU#1 R-hat/ESS
- `cpu2_diagnostics/convergence_latest.csv` — CPU#2 R-hat/ESS
- `live_chain_audit.json` — complete audit data from 2026-03-09 21:15 UTC
- `live_chain_audit.txt` — human-readable version

**D. CPU Chain Files — ZERO LOCAL COPIES**
- CPU#1: 48,820 samples across 16 chains — **NEVER backed up locally**
- CPU#2: 49,643 samples across 16 chains — **NEVER backed up locally**
- **98,463 CPU samples are PERMANENTLY LOST**

**E. Science Results (PRESERVED)**
- `mcmc_results_2026-03-04.txt` — early cross-dataset comparison table
- All convergence metrics from the 2026-03-09 audit are in JSON/CSV locally
- Best-fit parameter values documented in audit reports

#### DATA LOSS SUMMARY

| Source | Samples at Shutdown | Locally Preserved | LOST |
|--------|--------------------|--------------------|------|
| GPU chains | ~140,342 | 14,021 (10%) | ~126,321 |
| CPU#1 chains | 48,820 | 0 | 48,820 |
| CPU#2 chains | 49,643 | 0 | 49,643 |
| **TOTAL** | **236,622** | **14,021 (5.9%)** | **~224,784** |

**~224,784 MCMC samples are irrecoverably lost.**

However, the SCIENCE is partially preserved:
- All convergence diagnostics (R-hat, ESS, drift) from the 2026-03-09 audit
- Best-fit parameter values and uncertainties
- The 14,021 early GPU chain samples with checkpoints and covmats
- Complete monitor scripts and YAML configurations

---

### Step 5 — Chain Resume Possibility Assessment

#### GPU Pod Chains
The local GPU snapshot from 2026-03-05 contains for each chain:
- `spin_torsion.1.txt` — chain samples (early)
- `spin_torsion.checkpoint` — Cobaya checkpoint file
- `spin_torsion.covmat` — learned covariance matrix
- `spin_torsion.progress` — progress file
- `spin_torsion.updated.yaml` — updated config
- `spin_torsion.input.yaml` — original config

**Classification:**
| Dataset | Chains | Local Data | Resume Status |
|---------|--------|-----------|---------------|
| full_tension | 7 (1 + ch2-7) | 14,021 early samples + checkpoints + covmats | RESUMABLE from early checkpoint on new pod |
| planck_only | 7 | Same structure | RESUMABLE from early checkpoint on new pod |
| planck_bao | 7 | Same structure | RESUMABLE from early checkpoint on new pod |
| planck_bao_sn | 7 | Same structure | RESUMABLE from early checkpoint on new pod |

Cobaya supports `--resume` from checkpoint files. The learned covariance matrices
are the most valuable asset — they dramatically speed up convergence. Even though
we'll lose ~90% of accumulated samples, the chains can resume from the 2026-03-05
state and re-converge much faster than starting from scratch.

#### CPU#1 Chains (ΔNeff model)
- **NO local chain files, checkpoints, or covmats**
- Only convergence CSVs survive
- **NOT RESUMABLE — must restart from scratch**
- Can use GPU covmats as proposal covariance (significant speedup)

#### CPU#2 Chains (ΛCDM controls)
- **NO local chain files, checkpoints, or covmats**
- Only convergence CSVs survive
- **NOT RESUMABLE — must restart from scratch**
- ΛCDM chains converge much faster anyway

---

### Steps 6-8 — BLOCKED

Cannot resume runs, restore monitoring, or perform post-recovery checks
because all pods are terminated. New pods must be provisioned.

---

## Recovery Plan — What To Do Next

### Immediate Actions (requires human operator)

1. **Log into RunPod dashboard** at runpod.io
   - Confirm pod termination in the web UI
   - Check if there are any billing events, alerts, or platform notices
   - Check if the 20GB network volume `modest_plum_antlion` contains any data

2. **Provision new GPU pod**
   - Same spec: RTX 6000 Ada (or equivalent)
   - Attach a **network volume** this time (survives pod termination)
   - Upload the local GPU snapshot from `archives/gpu_run_snapshot_20260305_0824/`
   - Resume Cobaya chains from checkpoints using `cobaya-run --resume`

3. **Provision new CPU pods (2x)**
   - Same spec: cpu5c (32 vCPU, 64GB RAM)
   - Start chains fresh using GPU-learned covariance matrices as proposal
   - Use **network volumes** to prevent future data loss

4. **Implement automated off-pod backup immediately**
   - Set up hourly SCP/rsync of chain files to local machine or cloud storage
   - Never again rely solely on pod-local storage

### What Is Preserved and Usable

- 14,021 GPU chain samples with full checkpoint/covmat files (can resume)
- All YAML configs and monitor scripts
- Complete convergence diagnostics from 2026-03-09 audit
- Best-fit parameter values and uncertainties for all datasets
- The science narrative: full_tension was at 6/8 gates, ~3.5 days from freeze

### What Is Permanently Lost

- ~126,321 GPU chain samples (accumulated 2026-03-05 to 2026-03-09)
- All 48,820 CPU#1 chain samples, checkpoints, and covmats
- All 49,643 CPU#2 chain samples, checkpoints, and covmats
- On-pod frozen packs and hourly backup tarballs
- Monitor/trend logs from the pod filesystems

---

## Lessons Learned

1. **Pod-local storage is ephemeral.** RunPod pods can be terminated without warning.
   Always use network volumes AND off-pod backups.
2. **CPU chain data was never backed up.** The backup system focused on GPU data.
   Every pod needs automated off-pod backup from day one.
3. **The $200 balance rules out billing** — this was likely auto-termination or
   manual error. Check RunPod activity logs if available.
4. **The convergence diagnostics survived** because they were pulled to local.
   This should be done for ALL data, not just metrics.
