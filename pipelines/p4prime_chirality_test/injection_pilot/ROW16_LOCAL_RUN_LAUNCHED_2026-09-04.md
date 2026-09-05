# Row 16 step (ii) — N=20,000 local run launched (2026-09-04)

## Status
Detached local run started 2026-09-04 21:00:51 local time, PID **58537**
(`row16_local/pid`). Resumes the prior lane's inference from checkpoint:
10640/20000 pairs already on disk (`scale20k_pairs.parquet`), 9360 of the
remaining ~9500 download attempts had failed in that prior attempt — a
pattern consistent with legacysurvey.org rate-limiting after ~10.5k
sequential cutout requests, not random flakiness (fail count was 1 at
10504/20000 done, then jumped to 9360 by run end).

## Hardening applied before relaunch
`run_injection_scale20k.py::get_image` now retries each cutout download up
to 4x with backoff (1.5s, 3s, 4.5s) and adds a 0.15s delay after each
successful fetch, to avoid repeating the same rate-limit wall. No change to
the resume logic, output schema, or inference math.

## Pipeline (`run_row16_local.sh`)
sample (skip, already done) -> inference (resume from 10640/20000, local
MPS) -> analysis (`analyze_injection_scale20k.py`: f in {0, 0.5, 1, 2, 5}%
x 10 seeds, 500-sample bootstrap) -> figure
(`gen_fig_scale20k_injection.py`). Idempotent via
`row16_local/STAGE_{SAMPLE,INFERENCE,ANALYSIS,FIGURE}_DONE` markers; the
inference stage additionally hard-fails (does not mark done) unless the
output parquet reaches all 20000 rows, so a repeat of the download-failure
tail will not be silently accepted as complete.

## Projected wall-clock
The N=5000 (Row13) run on the same local MPS device: 2666.7s = 44.5 min for
5000 pairs, 0 failed (~1.88 img/s steady state). Remaining work here is
20000 - 10640 = 9360 pairs. At the same ~1.7-1.9 img/s throughput measured
in the prior N=20000 attempt's healthy phase (before the rate-limit tail),
**projected additional wall-clock ~80-95 min**, i.e. completion in roughly
1.5-2 hours from launch, assuming the retry/backoff hardening holds off
another rate-limit wall. If throttling recurs, remaining time could extend
toward the original attempt's own worst-case ETA (~2.5-3 h for the full
20000 from a cold start). Analysis + figure stages are seconds, not
minutes, once inference completes.

## Markers to check
- `row16_local/run.log` — full stage log
- `row16_local/STAGE_SAMPLE_DONE`, `STAGE_INFERENCE_DONE`,
  `STAGE_ANALYSIS_DONE`, `STAGE_FIGURE_DONE`
- `row16_local/ROW16_DONE` / `row16_local/ROW16_FAILED` — terminal markers
- `row16_local/pid` — launched PID (58537)
