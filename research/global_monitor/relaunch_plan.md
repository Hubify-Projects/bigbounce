# BigBounce Recovery & Relaunch Plan

**Date:** 2026-03-10 22:30 UTC
**Status:** PLANNING ONLY — nothing launched
**Budget:** ~$1,000 RunPod credits (existing $200 balance + $800 preload)
**Based on:** local_survival_audit.md, runpod_storage_survival_audit.md

---

## 1. Workload Classification

### Per-Dataset Recovery Strategy

| Dataset | Pod | Surviving Assets | Samples (local / at death) | Classification | Priority |
|---------|-----|-----------------|---------------------------|----------------|----------|
| full_tension | GPU | 4,599 samples + 7 covmats + 7 configs | 4,599 / 63,531 | **WARM RESTART** | **P0 — HIGHEST** |
| planck_bao_sn | GPU | 2,487 samples + 7 covmats + 7 configs | 2,487 / 26,220 | **WARM RESTART** | P1 |
| planck_only | GPU | 2,208 samples + 7 covmats + 7 configs | 2,208 / 25,345 | **WARM RESTART** | P2 |
| planck_bao | GPU | 2,240 samples + 7 covmats + 7 configs | 2,240 / 25,246 | **WARM RESTART** | P3 |
| full_tension | CPU#1 | convergence CSV only | 0 / 11,880 | **SEEDED COLD START** | P1 |
| planck_bao_sn | CPU#1 | convergence CSV only | 0 / 11,739 | **SEEDED COLD START** | P2 |
| planck_only | CPU#1 | convergence CSV only | 0 / 13,205 | **SEEDED COLD START** | P2 |
| planck_bao | CPU#1 | convergence CSV only | 0 / 11,996 | **SEEDED COLD START** | P3 |
| All 4 | CPU#2 | convergence CSV only | 0 / 49,643 | **SEEDED COLD START** | P3 — OPTIONAL |

### Classification Definitions

- **WARM RESTART:** Upload surviving chain files + covmats to new pod. Cobaya
  starts with an informed proposal matrix and appends to existing chains.
  Skips burn-in entirely. Chain1 files can be discarded (were lagging 6-7x
  behind cohort_main anyway — use only chains 2-7 going forward).

- **SEEDED COLD START:** No chain files survive, but GPU covmats can be used
  as the `proposal_matrix` in a fresh Cobaya config. This gives the sampler
  an informed starting proposal, cutting burn-in from ~2,000 steps to ~100.

- **TRUE RESUME:** NOT possible for any workload. Would require checkpoint
  files from the moment of shutdown (2026-03-09). The 20260304 checkpoints
  are from a much earlier state — using them with the 20260305 chain files
  would create inconsistencies. Safer to warm-restart with covmats only.

### Key Decision: Drop Chain 1

The original chain1 across all GPU datasets was lagging 6-7x behind chains 2-7
and was inflating R-hat by 14-87x. **Recommendation: Do NOT restart chain1.**
Run 6 chains per dataset (matching cohort_main) instead of 7. This saves ~14%
compute per dataset and eliminates the convergence drag.

### Key Decision: CPU#2 ΛCDM Controls

CPU#2 (ΛCDM) provided independent verification that H0 R-hat was consistent
across models. This is valuable but not essential for the primary science result.
**Recommendation: Defer CPU#2 to Phase C.** The ΛCDM comparison can be done
post-freeze with a shorter dedicated run.

---

## 2. Hardware Recommendations

### Lead GPU Pod (canonical runs — all 4 datasets)

| Option | GPU | vCPU | RAM | Cost/hr | Rationale |
|--------|-----|------|-----|---------|-----------|
| **RECOMMENDED** | RTX 6000 Ada | ~128 | ~503 GB | $0.74 | Same GPU as original. 128 CPU cores for parallel Cobaya/CLASS. Proven performance. |
| Budget alternative | RTX A5000 | ~9 | ~50 GB | $0.16 | 4.6x cheaper but only 9 vCPU — will be 5-10x slower for CPU-bound MCMC. |
| Spot option | RTX 6000 Ada (spot) | ~128 | ~503 GB | $0.40 | 46% cheaper but risk of preemption. Acceptable IF backup system works. |

**Verdict:** Use **RTX 6000 Ada on-demand** ($0.74/hr). Cobaya MCMC with
CLASS/CAMB is CPU-bound — the 128 vCPU is what matters, not GPU VRAM. The
$0.74/hr premium over a $0.16 A5000 buys ~14x more CPU cores, cutting total
wall-clock time by ~5-10x. Total cost is lower because runtime is shorter.

### CPU Pod (ΔNeff independent verification)

| Option | Type | vCPU | RAM | Cost/hr |
|--------|------|------|-----|---------|
| **RECOMMENDED** | cpu5c | 32 | 64 GB | ~$0.19 |

Same as original. 32 vCPU handles 16 chains (4 datasets × 4 chains) well.

### Consolidation Decision

**Do NOT consolidate** GPU and CPU workloads onto a single pod. Reasons:
1. GPU pod runs the ΔNeff spin-torsion model (7 parameters)
2. CPU#1 runs the same ΔNeff model but independently — cross-check
3. Keeping them separate ensures truly independent chains
4. If one pod fails, the other's data survives

### Reduce Scope: Which Runs Are Essential?

| Run | Essential? | Reason |
|-----|-----------|--------|
| GPU all 4 datasets | **YES** | Primary science results. All 4 needed for cross-dataset table. |
| CPU#1 ΔNeff | **YES** | Independent verification of GPU results. Required for paper. |
| CPU#2 ΛCDM | **DEFER** | Nice-to-have comparison. Can run a shorter focused run later. |

---

## 3. Storage Architecture (MANDATORY)

The root cause of data loss was `volumeInGb: 0` — container-only storage.
**This must never happen again.**

### Three-Layer Storage Design

```
Layer 1: Network Volume (RunPod)
├── Survives pod termination
├── ~$0.07/hr for 100 GB ($50/mo)
├── Mounted at /workspace (replaces container disk)
└── ALL chain data lives here

Layer 2: On-Pod Snapshots (hourly)
├── Automated tarball of chains/ every hour
├── Stored on the same network volume in /workspace/backups/
├── Rotated: keep last 24 hourly + last 7 daily
└── Script: existing global_backup.py (fix tar --warning flag)

Layer 3: Off-Pod Sync (every 6 hours)
├── rsync/scp from pod to local machine
├── Target: reproducibility/cosmology/live_sync_<pod>/
├── Runs from local cron or launchd
├── Keeps last 7 days of chain snapshots
└── SHA256SUMS generated on each sync
```

### Network Volume Specification

| Volume | Size | Region | Purpose | Monthly Cost |
|--------|------|--------|---------|-------------|
| bigbounce-gpu-vol | 100 GB | US-TX-3 or US-OR-1 | GPU chains + backups | ~$50 |
| bigbounce-cpu1-vol | 50 GB | same region | CPU#1 chains | ~$25 |

**Create network volumes BEFORE creating pods.** Attach at pod creation time.

### Off-Pod Sync Script (new — to be created)

```bash
#!/bin/bash
# Run from local machine via cron every 6 hours
# 0 */6 * * * /path/to/bigbounce/scripts/offpod_sync.sh

PODS=("gpu:HOST:PORT" "cpu1:HOST:PORT")
LOCAL_BASE="reproducibility/cosmology/live_sync"
TIMESTAMP=$(date -u +%Y%m%d_%H%M)

for spec in "${PODS[@]}"; do
    IFS=: read -r name host port <<< "$spec"
    rsync -avz --timeout=120 \
        -e "ssh -i ~/.ssh/id_ed25519 -p $port" \
        root@$host:/workspace/bigbounce/reproducibility/chains/ \
        "$LOCAL_BASE/${name}/${TIMESTAMP}/"
    # Generate checksums
    cd "$LOCAL_BASE/${name}/${TIMESTAMP}/"
    find . -name "*.txt" -exec sha256sum {} \; > SHA256SUMS.txt
done
```

### Monitoring & Alerts

| Check | Frequency | Action on Failure |
|-------|-----------|-------------------|
| Pod alive (SSH test) | Every 30 min | Email/Slack alert |
| Chain files writing | Every hour | Alert if no writes in 2 hours |
| Disk usage | Every hour | Alert if > 70% |
| Off-pod sync success | Every 6 hours | Alert if sync fails |
| RunPod balance | Daily | Alert if < $100 |

### Checksums & Manifests

After every off-pod sync:
- Generate `SHA256SUMS.txt` for all `.txt` chain files
- Generate `MANIFEST.md` with sample counts per chain
- Store in the sync directory alongside chain files

---

## 4. Budget Model

### Recommended Scenario: GPU + CPU#1 (Phase A+B)

| Item | $/hr | $/day | Days | Total |
|------|------|-------|------|-------|
| RTX 6000 Ada (GPU) | $0.74 | $17.76 | 12 | $213.12 |
| cpu5c (CPU#1) | $0.19 | $4.56 | 12 | $54.72 |
| Network vol 100GB (GPU) | $0.07 | $1.68 | 30 | $50.40 |
| Network vol 50GB (CPU#1) | $0.035 | $0.84 | 30 | $25.20 |
| **Subtotal** | | | | **$343.44** |

### What $1,000 Buys

| Scenario | Daily Burn | Days of Runtime | Science Outcome |
|----------|-----------|-----------------|-----------------|
| GPU + CPU#1 + vols | $24.84 | **40 days** | Full recovery of all 4 datasets + independent verification |
| GPU only + vol | $19.44 | **51 days** | All 4 datasets, no independent verification |
| GPU full_tension only + vol | $19.44 | **51 days** | Single most important result only |
| Budget (A5000 + cpu3c) | $11.04 | **90 days** | Full recovery but ~3x slower |

### Estimated Time to Key Milestones

| Milestone | GPU (RTX 6000 Ada) | GPU (RTX A5000) |
|-----------|-------------------|-----------------|
| full_tension freeze (ESS > 2000) | **~7-10 days** | ~25-35 days |
| planck_bao_sn freeze | ~8-12 days | ~30-40 days |
| planck_only freeze | ~10-14 days | ~35-50 days |
| planck_bao freeze | ~3-4 weeks | ~8-12 weeks |
| CPU#1 full_tension converged | ~10-14 days | N/A |

**Rationale for time estimates:**
- Original run: full_tension reached 6/8 gates in ~5 days with ~62k cohort_main samples
- Warm restart with covmats skips burn-in but needs to re-accumulate ~160k+ samples
  for ESS(H0) > 2000 and ESS(ΔNeff) > 2000
- Original sampling rate was ~200 samples/hr/chain (full_tension) on RTX 6000 Ada
- 6 chains × 200 samp/hr = 1,200 samp/hr → 160k samples ≈ 133 hours ≈ 5.5 days
- Add ~2 days for new burn-in stabilization → **~7-10 days**

### Cost to Reach full_tension Science Freeze

| Hardware | Time | Compute Cost | Storage Cost | Total |
|----------|------|-------------|-------------|-------|
| RTX 6000 Ada | 8 days | $142 | $5 | **$147** |
| RTX A5000 | 30 days | $115 | $17 | **$132** |

A5000 is slightly cheaper in total but takes 3.75x longer. For an urgent
recovery, the RTX 6000 Ada is clearly better.

---

## 5. Phased Relaunch Plan

### Phase A: Primary Science Recovery (Days 1-12)
**Goal:** Recover full_tension to science freeze + restart all GPU datasets

**Day 0 — Infrastructure Setup (before ANY compute)**
1. Create network volume `bigbounce-gpu-vol` (100 GB) in target region
2. Create GPU pod (RTX 6000 Ada) attached to this volume
3. Wait for pod boot + SSH availability
4. Install Cobaya + CAMB + CLASS + dependencies
5. Clone bigbounce repo to /workspace
6. Upload GPU snapshot: `archives/gpu_run_snapshot_20260305_0824/`
7. Verify all covmats, configs, and chain files are intact on pod
8. Set up off-pod sync cron on local machine
9. **DO NOT START CHAINS YET**

**Day 0 — Data Staging**
1. For each dataset (full_tension, planck_only, planck_bao, planck_bao_sn):
   - Create chain directories: `chains/{dataset}_chain{2..7}/`
   - Copy surviving chain files (`spin_torsion.1.txt`) into place
   - Copy surviving covmats (`spin_torsion.covmat`) into place
   - Copy updated YAML configs into place
   - Modify configs: set `proposal_matrix` to point to covmat
   - Set `resume: True` in Cobaya config
   - **Drop chain1** — do not create chain1 directories
2. Run a single-step test for full_tension_chain2:
   ```bash
   cobaya-run chains/full_tension_chain2/spin_torsion.updated.yaml --resume -f
   ```
   Verify it appends to existing chain file, not overwrites

**Day 0 — Launch Chains (priority order)**
1. Start full_tension chains 2-7 (6 processes)
2. Start planck_bao_sn chains 2-7 (6 processes)
3. Start planck_only chains 2-7 (6 processes)
4. Start planck_bao chains 2-7 (6 processes)
5. Total: 24 Cobaya processes (reduced from 32 — no chain1s)
6. Deploy mcmc_monitor_v6.py
7. Deploy freeze manager
8. Verify all 24 chains are writing within 30 minutes
9. Run first off-pod sync

**Days 1-7 — Monitor + Full Tension Push**
- Monitor convergence daily
- Off-pod sync every 6 hours
- Expected: full_tension R-hat stays < 0.01 (was already there)
- ESS should grow linearly: ~1,200 samples/hr → ~28,800/day
- full_tension ESS(H0) target: 2,000 → need ~160k total samples
- Starting from 4,599 → need ~155k more → **~5.4 days**
- Allow ~2 days margin for stabilization → **Day 7-10: freeze check**

**Days 7-12 — Science Freeze Evaluation**
- Run freeze gate check on full_tension
- If 8/8 gates pass: FREEZE full_tension (create immutable archive)
- Continue other datasets toward their freeze targets
- Begin Phase B

### Phase B: Independent Verification (Days 5-20)
**Goal:** CPU#1 ΔNeff chains for cross-validation

**Day 5 — CPU#1 Setup (overlap with Phase A)**
1. Create network volume `bigbounce-cpu1-vol` (50 GB)
2. Create CPU pod (cpu5c, 32 vCPU, 64 GB)
3. Install dependencies
4. Copy GPU covmats to CPU#1 as initial proposal matrices
5. Create 4 × 4 = 16 chain configs (seeded with GPU covmats)
6. Launch 16 Cobaya processes
7. Deploy monitor + off-pod sync

**Days 5-20 — CPU#1 Convergence**
- CPU#1 chains start cold but with informed proposals
- Expected convergence: ~10-14 days for R-hat < 0.01
- ESS targets are lower for verification (ESS > 500 sufficient)
- Cross-check GPU and CPU#1 posteriors once both have > 5,000 samples

### Phase C: ΛCDM Controls (Optional, Days 14+)
**Goal:** CPU#2 ΛCDM comparison if budget allows

**Only if:**
- full_tension is frozen or near-frozen
- Budget remaining > $300
- CPU#1 is running stably

**Setup:**
1. Create CPU#2 pod (cpu5c) with network volume
2. Run ΛCDM chains (no delta_neff parameter)
3. ΛCDM converges ~2-3x faster — expect < 7 days

**Alternative:** Skip CPU#2 entirely. Use the CPU#2 convergence CSV from
the 2026-03-09 audit as documented evidence of ΛCDM agreement. The paper
can cite "independent ΛCDM chains confirmed H0 R-hat < 0.005 before
pod termination" with the convergence data as supplementary material.

---

## 6. Detailed Recovery Procedures Per Dataset

### full_tension (P0 — highest priority)

**Pre-crash state (2026-03-09):**
- 6/8 freeze gates passing
- Rm1(H0) = 0.0036, Rm1(ΔNeff) = 0.0031, Rm1(τ) = 0.0071 — all R-hat PASS
- ESS(H0) = 781, ESS(ΔNeff) = 694 — need 2,000 each (BLOCKING)
- ESS(τ) = 1,243 — PASS
- Drift < 0.01σ — PASS
- 62,080 cohort_main samples (chains 2-7)

**Local surviving data:**
- 4,599 samples across 7 chains (chain1: 240, chains 2-7: 752-896 each)
- 7 covmats, 7 updated YAMLs, 7 input YAMLs

**Recovery strategy:**
1. Upload chains 2-7 files + covmats to new pod
2. Discard chain1 (240 samples, was dragging R-hat)
3. Set `resume: True` + `proposal_matrix: spin_torsion.covmat`
4. Cobaya appends to existing chain files from sample 752-896 onward
5. R-hat will initially be high (only ~600-900 samples per chain)
6. Should re-converge within ~3-4 days (covmat ensures efficient sampling)
7. ESS grows linearly; target ~7-10 days to freeze

**Expected timeline:** 7-10 days to full science freeze

### planck_bao_sn (P1)

**Pre-crash state:** 4/8 gates. Rm1(ΔNeff) = 0.0126 just above 0.01 target.
**Local data:** 2,487 samples, 7 covmats
**Strategy:** Same warm restart. ΔNeff R-hat was close to passing; should
clear within 2-3 days. ESS is the longer blocker (~8-12 days).
**Timeline:** 8-12 days

### planck_only (P2)

**Pre-crash state:** 5/8 gates. All R-hat passing. ESS 3.5x short.
**Local data:** 2,208 samples, 7 covmats
**Strategy:** Warm restart. R-hat should re-converge quickly.
**Timeline:** 10-14 days

### planck_bao (P3)

**Pre-crash state:** 3/8 gates. R-hat(H0) = 0.027, R-hat(ΔNeff) = 0.023.
**Local data:** 2,240 samples, 7 covmats
**Strategy:** Warm restart. This was the slowest-converging dataset.
**Timeline:** 3-4 weeks (R-hat still needs significant improvement)

---

## 7. Pre-Launch Checklist

Before creating any pod:

- [ ] Preload RunPod credits to ~$1,000 total
- [ ] Create network volume(s) — verify they show in API
- [ ] Prepare local upload bundle:
  - [ ] Extract and verify all covmats from GPU snapshot
  - [ ] Prepare per-chain YAML configs (drop chain1, update paths)
  - [ ] Prepare launch script
  - [ ] Prepare monitor deployment package
- [ ] Set up local off-pod sync cron (write and test the script)
- [ ] Set up RunPod balance alert (check balance via API daily)
- [ ] Verify `runpod_cloud.py` can create pods with network volumes
  - [ ] Update `create_pod()` to accept `networkVolumeId` parameter
- [ ] Update `pod_registry.yaml` template for new pod IDs
- [ ] Decide: terminate the 3 remaining Paper-2 EXITED pods to stop
  their ~$0.002/hr storage charge? (saves ~$1.44/mo)

---

## 8. Risk Mitigation

| Risk | Mitigation |
|------|-----------|
| Pod termination (again) | Network volumes survive termination. Off-pod sync every 6 hours. |
| Spot preemption | Use on-demand for Phase A. Consider spot only for Phase C. |
| Chain corruption on restart | Test single chain first. Verify appends, not overwrites. |
| Budget overrun | Daily cost monitoring. Kill CPU pods first if budget tight. |
| Cobaya resume incompatibility | If `--resume` fails with old chain files, start fresh chains seeded with covmats. Only ~2-3 extra days. |
| Network volume full | 100 GB is 2x the GPU pod's previous usage (46% of unknown disk). Monitor. |
| Local machine offline | Off-pod sync fails silently. Add health check. Keep network volume as primary safety net. |

---

## 9. Recommendations — Final Answers

### Single Best Recovery Strategy

**GPU RTX 6000 Ada (on-demand) with 100 GB network volume. Warm restart all
4 datasets using surviving covmats. Drop chain1. Run 6 chains per dataset
(24 total). Add CPU#1 pod on day 5 for independent verification.**

Cost: ~$270 for 12 days of compute + storage. Gives 40 days of runway on $1,000.

### Safest Storage/Backup Design

Three layers:
1. **Network volume** (survives pod termination) — $50-75/month
2. **On-pod hourly tarballs** (survives process crashes) — free
3. **Off-pod rsync every 6 hours** (survives RunPod outages) — free

Plus: SHA256 checksums on every sync, MANIFEST.md with sample counts,
daily RunPod balance check via API.

### Exact First Pod to Relaunch

1. **Create:** Network volume `bigbounce-gpu-vol`, 100 GB, in US-TX-3 or US-OR-1
2. **Create:** GPU pod — RTX 6000 Ada, on-demand, attached to `bigbounce-gpu-vol`
3. **Image:** `runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04`
4. **First chain to test:** full_tension_chain2 (warm restart)
5. **After verification:** launch all 24 chains

### Should We Focus Primarily on full_tension First?

**YES — emphatically.**

full_tension was at 6/8 freeze gates with R-hat fully converged. It only
needed more samples for ESS. It is the paper's most important result
(uses all available data: Planck + BAO + SN + H0 prior + S8 prior).
It should be the first dataset launched, the first monitored, and the
first frozen. All other datasets should run in parallel but are secondary.

If budget were extremely tight ($200), the strategy would be: run ONLY
full_tension on an RTX A5000 ($0.16/hr × 30 days = $115) and use the
surviving convergence diagnostics as supplementary evidence for the other
datasets. But with $1,000, we can afford to run everything.
