# Paper-1 MCMC Clean Restart: Storage Architecture

**Date:** 2026-03-10
**Author:** Houston Golden
**Status:** Design document — ready for implementation

---

## Motivation

Previous RunPod pods were launched with container-only storage (`volumeInGb=0`) and no
network volumes attached. When those pods were terminated, ALL chain data was permanently
lost — approximately **224,784 MCMC samples** across 64 chains. There is no recovery path;
the samples are gone.

This storage design ensures that outcome is structurally impossible going forward. The
primary defense is a **RunPod Network Volume**, which persists independently of any pod
lifecycle. Even if a pod is terminated, destroyed, or fails to restart, the volume and all
data on it survive intact.

---

## 1. Network Volume

| Property | Value |
|----------|-------|
| **Name** | `bigbounce-paper1-canonical` |
| **Size** | 75 GB |
| **Region** | Same datacenter as pod (US-TX-3 or similar high-availability) |
| **Mount path** | `/workspace` (RunPod default for network volumes) |
| **Cost** | ~$5.25/month ($0.07/GB/month x 75 GB) |

### Size Rationale

- Chain files grow ~1 KB per sample
- 32 chains x ~50,000 target samples = ~1.6 GB of chain data
- Git repo is ~500 MB
- Backups, logs, covariance matrices, and snapshots add overhead
- 75 GB provides ~40x headroom, which is more than sufficient
- Chose 75 GB over 100 GB to save on storage costs (~$1.75/month difference)

### Why Network Volume

- **Survives pod stop** — data is untouched when a pod is stopped
- **Survives pod restart** — data is untouched when a pod is restarted
- **Survives pod termination** — data persists even if the pod is destroyed
- A new pod can be created and attached to the same volume at any time
- This is the PRIMARY defense against data loss

---

## 2. Directory Structure

```
/workspace/
├── bigbounce/                    # Git repo clone
│   ├── reproducibility/
│   │   └── cosmology/
│   │       ├── canonical_run_001/   # CLEAN CANONICAL RUN
│   │       │   ├── MANIFEST.md
│   │       │   ├── SHA256SUMS.txt
│   │       │   ├── run_config.yaml
│   │       │   ├── dneff/           # ΔNeff model chains
│   │       │   │   ├── full_tension/
│   │       │   │   │   ├── chain_01/
│   │       │   │   │   ├── chain_02/
│   │       │   │   │   ├── chain_03/
│   │       │   │   │   └── chain_04/
│   │       │   │   ├── planck_only/
│   │       │   │   ├── planck_bao/
│   │       │   │   └── planck_bao_sn/
│   │       │   └── lcdm/            # ΛCDM control chains
│   │       │       ├── full_tension/
│   │       │       ├── planck_only/
│   │       │       ├── planck_bao/
│   │       │       └── planck_bao_sn/
│   │       └── warm_start_assets/   # Old covmats (reference only)
│   │           └── gpu_20260305_covmats/
│   └── ...
├── backups/
│   ├── hourly/                  # Hourly chain snapshots (on-volume)
│   │   └── YYYY-MM-DD_HHMM/
│   ├── snapshots/               # Daily full snapshots
│   │   └── snapshot_YYYY-MM-DD/
│   └── manifests/               # Per-snapshot manifests
│       └── manifest_YYYY-MM-DD_HHMM.json
└── logs/
    ├── cobaya/                  # Cobaya stdout/stderr per chain
    ├── monitor/                 # Monitor script logs
    └── backup/                  # Backup script logs
```

### Key Conventions

- **`canonical_run_001/`** is the single authoritative run directory. No stale or exploratory
  runs live alongside it. If a second canonical attempt is ever needed, it becomes
  `canonical_run_002/` and the first is preserved for comparison.
- **`warm_start_assets/`** holds covariance matrices from previous GPU runs. These are
  reference-only and are never overwritten by the current run.
- **Chain subdirectories** (`chain_01/`, `chain_02/`, etc.) each contain the Cobaya output
  files for a single MCMC chain: `.txt` chain samples, `.covmat` proposal covariance,
  `.updated.yaml` runtime config, and `.checkpoint` state.

---

## 3. Backup Architecture (3-Layer)

Three independent backup layers ensure that no single failure mode can cause data loss.

### Layer 1: On-Volume Hourly Tarballs

| Property | Value |
|----------|-------|
| **Frequency** | Every hour |
| **What** | All chain `.txt` files and `.covmat` files |
| **Where** | `/workspace/backups/hourly/YYYY-MM-DD_HHMM/` |
| **Retention** | Last 48 hours (auto-prune older) |
| **Script** | `backup_hourly.sh` |

Implementation notes:
- Use `tar czf` to compress chain files into a single archive per snapshot
- Include a `sample_counts.txt` file listing line counts per chain file
- Prune directories older than 48 hours at the end of each backup cycle
- Log all actions to `/workspace/logs/backup/`

### Layer 2: Daily Snapshots

| Property | Value |
|----------|-------|
| **Frequency** | Once per day |
| **What** | Full snapshot of `canonical_run_001/` |
| **Where** | `/workspace/backups/snapshots/snapshot_YYYY-MM-DD/` |
| **Retention** | Last 7 days |
| **Artifacts** | `SHA256SUMS.txt`, `MANIFEST.json` |

Implementation notes:
- Copy (not move) the entire `canonical_run_001/` directory
- Generate `SHA256SUMS.txt` covering all chain files in the snapshot
- Generate `MANIFEST.json` with run metadata: chain counts, sample counts per dataset,
  convergence diagnostics summary, timestamp, hardware info
- Prune snapshots older than 7 days

### Layer 3: Off-Pod Sync to Local Machine

| Property | Value |
|----------|-------|
| **Frequency** | Every 6 hours + on convergence milestones |
| **What** | Chain files, covmats, convergence data |
| **Where (local)** | `/Users/houstongolden/Desktop/CODE_2026/bigbounce/reproducibility/cosmology/canonical_run_001_sync/` |
| **Transport** | rsync over SSH with key authentication |
| **Runs on** | LOCAL machine as a cron job |

Implementation notes:
- The sync script runs on the local machine, pulling from the pod — this means the pod
  does not need outbound access or credentials for the local machine
- Use `rsync -avz --progress` with SSH key auth
- Also trigger a sync whenever a convergence milestone is reached (e.g., R-hat crosses
  a threshold like 0.01 or 0.005)
- Keep a local sync log at the target directory

### Why Three Layers

| Failure Mode | Layer 1 | Layer 2 | Layer 3 |
|-------------|---------|---------|---------|
| Chain file corruption | Restore from hourly tarball | Restore from daily snapshot | Restore from local copy |
| Accidental file deletion | Restore from hourly tarball | Restore from daily snapshot | Restore from local copy |
| Network volume failure | Lost | Lost | **Local copy survives** |
| Pod termination | Volume survives | Volume survives | Local copy survives |
| RunPod account issue | Lost | Lost | **Local copy survives** |

---

## 4. Safety Alerts

### 4.1 Low Balance Alert

- Check RunPod account balance every hour (via RunPod API)
- **Warning** if balance < $50 (approximately 6 days of A6000 runtime)
- **Critical** if balance < $20 (approximately 2.5 days of runtime)
- Alert method: write warning to `/workspace/logs/monitor/balance_alerts.log` and create
  `/workspace/ALERT_LOW_BALANCE` flag file

### 4.2 Pod Unreachable Alert

- Attempt SSH connection to pod every 15 minutes (from local machine)
- If SSH fails 3 consecutive times (45 minutes of unreachability), create alert
- Alert method: write to local log and create
  `/Users/houstongolden/Desktop/CODE_2026/bigbounce/research/global_monitor/ALERT_POD_UNREACHABLE`
  flag file on local machine

### 4.3 Chain Stall Alert

- Monitor file modification times on all chain `.txt` files
- **Warning** if any single chain file has not been modified in >2 hours
- **Critical** if ALL chain files have stalled for >1 hour
- Check by comparing `stat -c %Y` (modification epoch) against current time
- Alert method: write to `/workspace/logs/monitor/chain_stall_alerts.log` and create
  `/workspace/ALERT_CHAIN_STALL` flag file

### 4.4 Disk Space Alert

- Check network volume usage with `df -h /workspace` every hour
- **Warning** if usage > 80%
- **Critical** if usage > 90% — pause non-essential backups (Layer 1 hourly tarballs)
  to prevent the volume from filling completely
- Alert method: write to `/workspace/logs/monitor/disk_alerts.log` and create
  `/workspace/ALERT_DISK_SPACE` flag file

---

## 5. Integrity Checks

### 5.1 SHA256 Checksums

- Generate SHA256 checksums for all chain files after each hourly backup
- Store in `/workspace/backups/manifests/sha256_YYYY-MM-DD_HHMM.txt`
- After each Layer 3 sync, compare checksums between on-pod and off-pod copies
- Any mismatch triggers an immediate re-sync and alert

### 5.2 MANIFEST.md

Updated daily (and on convergence milestones) with:

- **Run ID** and start timestamp
- **Hardware specs**: pod ID, GPU type (e.g., NVIDIA A6000), vCPUs, RAM
- **Chain inventory**: number of chains per model per dataset combination
- **Sample counts**: current sample count per chain file
- **Convergence diagnostics**: latest R-hat values per parameter, effective sample sizes
- **Backup status**: timestamp of last successful Layer 1, Layer 2, and Layer 3 backup
- **Volume health**: current disk usage, any active alerts

---

## 6. Network Volume Persistence Summary

This is the most important section of this document.

```
Pod stopped     → Network volume persists → Data safe
Pod restarted   → Network volume persists → Data safe
Pod terminated  → Network volume persists → Data safe
Pod destroyed   → Network volume persists → Data safe
New pod created → Attach same volume      → Data available immediately
```

The network volume exists independently of any pod. It is a standalone storage resource
in RunPod's infrastructure. Deleting a pod does NOT delete an attached network volume
(unless the user explicitly deletes the volume itself).

**The only ways to lose data on a network volume are:**
1. Explicitly deleting the network volume through the RunPod dashboard or API
2. A RunPod infrastructure failure affecting the underlying storage (extremely rare)
3. Accidentally overwriting or deleting files on the volume

Risks 1 and 3 are mitigated by Layer 3 off-pod sync. Risk 2 is mitigated by both
Layer 3 off-pod sync and RunPod's own storage redundancy.

---

## 7. Implementation Checklist

- [ ] Create network volume `bigbounce-paper1-canonical` (75 GB, US-TX-3)
- [ ] Create new pod with network volume attached at `/workspace`
- [ ] Clone bigbounce repo to `/workspace/bigbounce/`
- [ ] Create directory structure as specified in Section 2
- [ ] Set up `backup_hourly.sh` with cron (Layer 1)
- [ ] Set up daily snapshot script with cron (Layer 2)
- [ ] Set up local rsync cron job on MacBook (Layer 3)
- [ ] Set up monitoring scripts for all four alert types (Section 4)
- [ ] Write initial `MANIFEST.md` in `canonical_run_001/`
- [ ] Generate baseline `SHA256SUMS.txt`
- [ ] Verify SSH key auth works from local machine to pod
- [ ] Run a short test chain (100 samples) to validate the full pipeline
- [ ] Confirm hourly backup fires and prunes correctly
- [ ] Confirm off-pod sync completes successfully
- [ ] Begin canonical MCMC run

---

*This design was created in response to the permanent loss of ~224,784 MCMC samples
on 2026-03-05 due to container-only storage with no network volume. That failure mode
is eliminated by this architecture.*
