# Pod-side orchestration scripts (AUG-011 campaign, as actually run)

These are the exact scripts that drove the 2026-08-05 → 08-07 clean DESI DR1
scan on RunPod pod `tc291bka0r6fl3` (A4000, 200 GB volume, $0.17/hr) and the
2026-08-07 phase-3 launch. They are committed as reusable lab infrastructure
and as provenance for the reproducibility manifests; paths assume the pod
layout (`/workspace`, repo subtree at `/workspace/bigbounce`).

| Script | Role |
|---|---|
| (phase-1 sealing) | the exact phase-1 chain is documented step-by-step in `../RUNBOOK.md` §3–8 (its pod script was not preserved; the RUNBOOK commands are the canonical form) |
| `pod_full_scan.sh` | launches N range-partitioned `run_scan.py` workers (N=12 used) |
| `pod_babysitter_v4.sh` | **the correct supervisor**: identifies workers by `/proc/<pid>/exe` (PyTorch renames worker `comm` to `pt_main_thread`, which broke every comm-based check — see SSOT/queue history), dedups per range, relaunches dead workers, writes `SCAN_ALL_DONE` |
| `pod_backup_loop.sh` | 2-hourly B2 sync of shards/receipts + HF upload of receipts/state (needs HF_TOKEN, B2_* env) |
| `pod_cleanup_relaunch.sh` | kill-all + relaunch template; the fail-closed reconcile step is described in its header (verify each shard's receipt sha/size/rows, drop bad pairs, rebuild checkpoints from receipts) |
| `pod_phase3.sh` | sealed S>8 sample → enrichment → SIMBAD/NED → WISE → taxonomy chain |
| `measure.sh` | accurate live counts (exe-based) |

Lessons encoded: never `pkill -f` a pattern that appears in your own SSH
command line; never trust `comm` for torch workers; make skipped groups
audited-and-retried rather than fatal; mint the preflight receipt AFTER the
last commit/push of a dispatch, never before.
