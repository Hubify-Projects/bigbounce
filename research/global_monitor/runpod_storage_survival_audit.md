# RunPod Storage Survival Audit — BigBounce

**Date:** 2026-03-10 21:40 UTC
**Mode:** READ-ONLY — nothing created or deleted
**Purpose:** Determine whether ANY persistent storage survived the Paper-1 pod terminations

---

## 1. Account Overview

| Field | Value |
|-------|-------|
| User ID | `user_3ASjlBqOLifanwrV3Q6Xe4BHzop` |
| Balance | **$199.98** |
| Current spend | $0.002/hr |
| Billing caused shutdown? | **NO** |

---

## 2. Complete RunPod Inventory

### Pods (3 remaining — all Paper-2, all EXITED)

| Pod ID | Name | Status | Volume | Container Disk | Network Vol? |
|--------|------|--------|--------|---------------|-------------|
| bpou58tmt95jjb | paper2-wp4-dneff | EXITED | 0 GB | 50 GB | No |
| mz3srzbzxxv1yj | paper2-wp5-spin | EXITED | 0 GB | 50 GB | No |
| uktt3hghbs1djo | paper2-p6-eb | EXITED | 0 GB | 50 GB | No |

### Terminated Pods (4 — gone from API entirely)

| Pod ID | Name | API Response | Had Network Vol? |
|--------|------|-------------|-----------------|
| 47htajss1ng2ig | bigbounce-gpu-validation | HTTP 400 (not found) | **NO** |
| m4xpnxzgokd93f | bigbounce-cpu1-primary | HTTP 400 (not found) | **NO** |
| eblghcn6u43wfk | bigbounce-cpu2-secondary | HTTP 400 (not found) | **NO** |
| pkysk4lbaqnhm0 | paper2-p7-cnn | pod: null | **NO** |

### Network Volumes (1 exists)

| Volume ID | Name | Size | Region | Associated with Paper-1? |
|-----------|------|------|--------|------------------------|
| 9wln8f98am | modest_plum_antlion | 20 GB | US-WA-1 | **NO** |

### Pod Templates (11 — all RunPod stock defaults)

No custom BigBounce templates exist. All templates are RunPod defaults
(PyTorch 2.1/2.2/2.4/2.8, Ubuntu 20/22/24, ComfyUI, etc.).

### Savings Plans

None.

---

## 3. Storage Type Analysis

### How were the Paper-1 pods created?

Evidence from `project-context/SESSION_HANDOFF_20260305.md` line 108:

> Pod creation fix: `volumeInGb: 0`, `cloudType: SECURE` (unquoted enum)

**All Paper-1 pods were created with `volumeInGb: 0`.**

This means they used **container disk only** — no persistent network volume
was attached. On RunPod:

- **Container disk** = ephemeral storage inside the pod container. Destroyed on termination.
- **Pod volume** (`volumeInGb > 0`) = persistent storage at `/workspace`. Survives stop/restart but **NOT** pod termination.
- **Network volume** = fully persistent storage. Survives pod termination. Must be explicitly created and attached.

The Paper-1 pods had:
- `volumeInGb: 0` → no pod volume
- `volumeMountPath: null` → no network volume mount
- Data stored at `/workspace` → this was container disk, not a separate volume

**When the pods were terminated, ALL of their storage was destroyed.**

### The network volume "modest_plum_antlion"

- **Never referenced** in any project file, config, script, or log
- **Never attached** to any Paper-1 or Paper-2 pod
- **Unknown origin** — may be from an earlier experiment or created by default
- **Contents unknown** — would need to attach to a new pod to inspect
- **Size:** 20 GB (too small to hold the full chain data even if it were relevant)
- **Region:** US-WA-1

---

## 4. Per-Pod Storage Verdict

| Pod | Had Network Volume? | Had Pod Volume? | Container Disk? | Storage Survived? |
|-----|--------------------|-----------------|-----------------|--------------------|
| GPU validation (47htajss1ng2ig) | **NO** | **NO** (volumeInGb=0) | Yes (destroyed) | **NO** |
| CPU#1 primary (m4xpnxzgokd93f) | **NO** | **NO** (volumeInGb=0) | Yes (destroyed) | **NO** |
| CPU#2 secondary (eblghcn6u43wfk) | **NO** | **NO** (volumeInGb=0) | Yes (destroyed) | **NO** |

---

## 5. Remote Data Recovery Paths

### Exhaustive check:

| Recovery Path | Available? | Notes |
|--------------|-----------|-------|
| Restart stopped pod | NO | Pods are terminated, not stopped |
| Recover pod volume | NO | Pods had volumeInGb=0 |
| Network volume data | NO | Volume exists but was never attached to Paper-1 |
| RunPod snapshots | NO | No snapshot feature used |
| RunPod backups | NO | No backup feature used |
| S3/GCS sync | NO | Never configured |
| Pod templates with data | NO | All templates are stock RunPod defaults |
| SSH access to inspect | NO | Pods don't exist |

**There is NO remote data recovery path for Paper-1 chain data.**

---

## 6. What DOES Still Exist Remotely

### Network volume (unknown contents)

The volume `modest_plum_antlion` (9wln8f98am, 20 GB, US-WA-1) still exists
and is accruing a small storage charge (~$0.002/hr based on current spend).

**Recommended action:** Spin up a minimal pod in US-WA-1, attach this volume,
inspect its contents. If it contains nothing useful, consider deleting it to
stop the storage charge. If it contains any BigBounce data (unlikely), preserve it.

### Exited Paper-2 pods (container disk)

The 3 Paper-2 pods are EXITED (not terminated). Their container disk data
may still be accessible if restarted. However:
- All Paper-2 data was already backed up locally
- These pods have `volumeInGb: 0` — same ephemeral storage setup
- If terminated (manually or by RunPod), their data would also be lost

**Recommended action:** Either terminate these pods to stop any charges,
or restart them briefly to verify/retrieve any data not yet backed up.

---

## 7. Summary Answers

### Are any network volumes still alive?
**YES** — one network volume (`modest_plum_antlion`, 20 GB, US-WA-1) exists.
But it was **never associated with any Paper-1 pod** and almost certainly
does not contain MCMC chain data.

### Is there any remote data recovery path left?
**NO.** The Paper-1 pods were created with `volumeInGb: 0` (no persistent
volume) and have been terminated (not just stopped). Their container disk
storage was destroyed on termination. There is no RunPod mechanism to
recover data from a terminated pod that had no persistent volume.

### Which storage objects should we preserve immediately?
1. **Network volume `9wln8f98am`** — inspect before deleting. Spin up a
   minimal pod in US-WA-1, mount it, check if it has anything useful.
2. **Paper-2 EXITED pods** — if not already fully backed up, restart
   briefly to retrieve any new data before they are also terminated.
3. **Local data** — the GPU snapshot at
   `reproducibility/cosmology/archives/gpu_run_snapshot_20260305_0824/`
   is now the ONLY surviving copy of any MCMC chain data. Back it up
   to a second location immediately (external drive, cloud storage).

---

## 8. Root Cause Note

The $199.98 balance rules out billing. Possible causes for simultaneous
termination of all 4 pods (3 Paper-1 + P7-CNN):

1. **Manual termination** — operator may have terminated accidentally
2. **RunPod auto-cleanup** — some pod types auto-terminate after inactivity
3. **RunPod platform policy** — pods running for 400+ days may hit limits
4. **Account-level action** — RunPod may have purged long-running pods

**Recommendation:** Contact RunPod support to determine the exact cause
and confirm there is no hidden recovery mechanism for terminated pods.
