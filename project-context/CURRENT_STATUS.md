# Current Status — POINTER ONLY

**This file is now a pointer to the SSOT.** Do not treat numbers here as live. Read the SSOT.

**Last refreshed: 2026-04-17** (drive-to-100 fire #7, `P-LEGACY-STATUS-CLEAN`)

## Where to read current status

| Surface | Path |
|---|---|
| Cross-paper dashboard | [`SSOT/index.md`](SSOT/index.md) |
| Paper 1 (Spin-Torsion) | [`SSOT/paper-1/status.md`](SSOT/paper-1/status.md) |
| Paper 2 (f_NL Forecast) | [`SSOT/paper-2/status.md`](SSOT/paper-2/status.md) |
| Paper 3 (Anomaly Catalog) | [`SSOT/paper-3/status.md`](SSOT/paper-3/status.md) |
| Paper 4 (Chirality Catalog) | [`SSOT/paper-4/status.md`](SSOT/paper-4/status.md) |
| Task queue (all papers) | [`SSOT/queue.md`](SSOT/queue.md) |
| Protocol + how to edit | [`SSOT/README.md`](SSOT/README.md) |

## Why this file is a pointer

Prior versions of `CURRENT_STATUS.md` carried paper %, version strings, pod hostnames, and a "next steps" list that drifted within days. The drift produced conflicting claims across `CURRENT_STATUS.md`, `wiki/entities/paper-*.md`, and the site HTML. The SSOT (`SSOT/`) exists to be the one canonical surface — this file now only points at it.

If you see a paper %, pipeline step count, or pod hostname quoted outside the SSOT, treat it as stale and cross-check against `SSOT/index.md`.

## For old links and grep patterns

The old content (Paper 2 "85 % science done", pod `sleepy_blush_crane`, "Pipeline 1 Final Status" table, H200 experiment roll-up, backup inventory, "Next Steps" list) was removed 2026-04-17 because all of those surfaces now live in the SSOT or per-pipeline docs:

- H200 experiment results → `pipelines/h200_results/` subdirs + per-paper SSOT status files
- Pipeline 1 step table → `project-context/pipeline1_tracer_purification_plan.md` + `SSOT/paper-3/status.md`
- Backup inventory → `MEMORY.md` reference entry (`reference_external_backups`)
- Next steps → `SSOT/queue.md`
- Pod status → `MEMORY.md` project entry (`project_pod_status`) + `project-context/active_pods_and_pipelines.md`

Do not re-populate this file with a status mirror. If you need a status, read the SSOT.
