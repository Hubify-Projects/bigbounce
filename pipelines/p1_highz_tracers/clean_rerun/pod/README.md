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

## pod_phase3_v2.sh — science-target-only rerun (2026-09-03)

Supersedes `pod_phase3.sh`'s sample-build step: the v1 S>8 sample was found
84.8% sky fibers (`project-context/ANOMALY_SAMPLE_CONTAMINATION_2026-09-03.md`).
`pod_phase3_v2.sh` is unattended and idempotent — stage markers under
`/workspace/phase3_v2/STAGE_*_DONE` let it resume after any interruption
without redoing completed work; a full log is appended to
`/workspace/phase3_v2/phase3_v2.log`.

Stages: (1) wait-for/run the science-only `--describe` pass ->
`science_target_summary.json`; (2) `sky_fraction_by_score.py` diagnostic;
(3) apply the **pre-declared threshold rule** — from grid `{3,4,5,6,8,10}`,
take the largest threshold with science-only count >= 300; if that count
exceeds 1,500, step to the next-larger grid point unless it would drop below
300 — build the sample with `--science-targets-only --zcatalog`, then run
`gates/check_sample_provenance.py` (abort on FAIL); (4)-(7) enrichment ->
SIMBAD/NED crossmatch -> WISE join -> taxonomy, same commands/flags/contract
as `pod_phase3.sh` but entirely under `/workspace/phase3_v2/`; (8) pack
`enrich_shards/` into <=9,000-file tar parts with `PACKED_SHA256SUMS.json`.

On success: `/workspace/PHASE3_V2_DONE`. On failure: `/workspace/PHASE3_V2_FAILED`
names the failing stage. Launch detached exactly like v1:

```
setsid nohup /workspace/bigbounce/pipelines/p1_highz_tracers/clean_rerun/pod/pod_phase3_v2.sh \
  > /workspace/phase3_v2/phase3_v2_stdout.log 2>&1 < /dev/null &
```
