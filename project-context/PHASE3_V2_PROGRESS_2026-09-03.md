# Phase-3 v2 (science-target-only rerun) — progress log, 2026-09-03

Context: `project-context/ANOMALY_SAMPLE_CONTAMINATION_2026-09-03.md` found
the v1 S>8 sample (`flagship_sample_s8.parquet`, 3,810 rows) is 84.8% sky
fibers (negative TARGETID / OBJTYPE=SKY). Code fix landed on main
(`a0ecb4d8`): `build_flagship_sample.py --science-targets-only --zcatalog …`
+ `gates/check_sample_provenance.py`, 33/33 tests. This log tracks the v2
science-target-only rerun on pod `8ofv5d4ynu7hku`.

## Pod state at session start (2026-09-03 ~16:05Z)

- `/workspace/bigbounce` on pod is a **files-only copy, not a git clone**
  (`git status` there fails — "not a git repository"). Pod copy of
  `build_flagship_sample.py` was STALE (no `--science-targets-only` flag,
  no `gates/` dir).
- Fixed: `scp`'d the current `build_flagship_sample.py` and
  `gates/check_sample_provenance.py` from local main to the pod path.
  Confirmed `--help` now shows `--science-targets-only`/`--zcatalog`.
- v1 phase-3 outputs remain untouched at `/workspace/flagship_*` (labelled
  SAMPLE-V1-CONTAMINATED, already landed+backed-up per
  `project-context/PHASE3_LANDING_2026-09-03.md`).
- New tool added this session: `pipelines/p1_highz_tracers/clean_rerun/
  sky_fraction_by_score.py` — reuses `build_flagship_sample.py`'s dedup +
  `load_science_target_flags` zcatalog join to compute sky/non-science
  fraction by `anomaly_score` bin ([3,4) [4,5) [5,6) [6,8) [8,10) [10,max]),
  writes JSON + PNG. scp'd to pod; pod had no `matplotlib` — installed.

## Step 2 — science-only summary + sky-fraction curve

- Launched (detached, `setsid nohup`) on pod ~16:07Z:
  `build_flagship_sample.py --describe --science-targets-only --zcatalog
  /workspace/zall-pix-iron.fits ... > /workspace/phase3_v2/describe_science.log`
  PID 79216. Streams all verified shards (dedup) + a 27GB zcatalog stream
  for the science-target join — expect this to take a while (zcatalog I/O
  bound, similar to the v1 finding scan which took ~15-20 min per full
  zcatalog pass in the earlier read-only check).
- STATUS: RUNNING as of last check (~16:09Z). Poll:
  `ssh -p 8489 root@205.196.17.124 "tail -30 /workspace/phase3_v2/describe_science.log; ps aux | grep build_flagship"`

## Resume instructions if this session stops before step 2 finishes

1. Poll the command above. If the process is gone and the log has no
   `Traceback`/`Error`, the describe output IS the science-only threshold
   table — copy it into `results_2026-08-07/phase3_v2/science_target_summary.md`.
2. If the process died, relaunch the exact command in
   `pipelines/p1_highz_tracers/clean_rerun/pod/` style (see above) — it is
   idempotent (read-only, no state file).
3. Next: run `sky_fraction_by_score.py` on the pod (already scp'd,
   matplotlib installed) pointed at the same contract/shard-dir/receipt-dir/
   summary/zcatalog, writing to
   `/workspace/phase3_v2/sky_fraction_by_score.{json,png}`; pull both back.
4. Then choose the deep-characterisation threshold from the PRE-DECLARED
   grid {3,4,5,6,8,10} on the SCIENCE-ONLY distribution (never S>8 by
   default) — pick the smallest grid point that still yields "a few hundred
   to ~1,000" objects; document the choice + rationale in
   `science_target_summary.md`.
5. Continue per the assigned step list (build sample at chosen threshold →
   provenance gate → enrichment → crossmatch → WISE → taxonomy, all under
   `/workspace/phase3_v2/`).

## Unattended v2 chain launched (2026-09-03 ~16:12Z)

- Deployed `pipelines/p1_highz_tracers/clean_rerun/pod/pod_phase3_v2.sh`
  (idempotent, stage markers, resumable) to the pod and launched detached:
  `setsid nohup .../pod_phase3_v2.sh > /workspace/phase3_v2/phase3_v2_stdout.log
  2>&1 < /dev/null &` — wrapper PID 79542, running bash PID 79545.
- Threshold-choice rule (pre-declared, encoded in the script): from grid
  `{3,4,5,6,8,10}`, take the largest threshold whose science-only post-dedup
  count is >= 300; if that count exceeds 1,500, step to the next-larger grid
  point unless it would drop below 300. Written to
  `/workspace/phase3_v2/threshold_choice.json` at stage 3.
- Stage 1 correctly detected the already-running describe pass (PID 79216)
  and is waiting on it rather than relaunching.
- Markers: `/workspace/phase3_v2/STAGE_{01_DESCRIBE,02_SKY_FRACTION,
  03_CHOOSE_THRESHOLD_AND_BUILD,04_ENRICH,05_CROSSMATCH,06_WISE,
  07_TAXONOMY,08_PACK_SHARDS}_DONE`; log `/workspace/phase3_v2/phase3_v2.log`;
  terminal markers `/workspace/PHASE3_V2_DONE` / `/workspace/PHASE3_V2_FAILED`.
