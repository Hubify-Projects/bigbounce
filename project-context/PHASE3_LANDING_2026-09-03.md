# Phase-3 landing receipt — 2026-09-03

**SAMPLE-V1 (provenance under review: possible sky-fiber contamination — negative
TARGETIDs).** 3,232/3,810 rows (84.8%) of `flagship_sample_s8_enriched.parquet`
carry negative `targetid` — DESI convention reserves negative TARGETIDs for
sky/non-astrophysical fibers. Coordinator is verifying; pod 8ofv5d4ynu7hku is
**held running** (not stopped) pending the verdict. No ledger #8 paper-vs-release
decision is made here.

## Source

Pod `8ofv5d4ynu7hku` (`root@205.196.17.124:8489`), `/workspace/`. Phase-3 chain
completed 2026-09-03T15:18Z (`PHASE3_DONE`, 0 errors in `phase3.log`).

## Artifacts (18 files landed)

| File | Bytes | SHA-256 |
|---|---|---|
| flagship_sample_s8.parquet | 84,536 | see PACKED_SHA256SUMS.json |
| flagship_sample_s8_manifest.json | 5,926,454 | " |
| flagship_sample_s8_enriched.parquet | 3,563,254 | " |
| flagship_enriched_manifest.json | 4,517 | " |
| flagship_crossmatch_matched.parquet | 8,278 | " |
| flagship_crossmatch_unmatched.parquet | 132,352 | " |
| flagship_crossmatch_manifest.json | 1,366 | " |
| flagship_wise.parquet | 22,237 | " |
| flagship_wise_manifest.json | 1,139 | " |
| flagship_taxonomy.json | 1,740,322 | " |
| flagship_taxonomy_manifest.json | 975 | " |
| enrich_audit.jsonl | 378,662 | " |
| enrich_checkpoint.json | 497,766 | " |
| logs/phase3.log, phase3_stdout.log, bootstrap.log | 1,153 / 1,153 / 12,451,051 | " |
| enrich_shards_part1.tar (packed 3,128 shard files, 172 MB) | 175,523,840 | `83f89ef4e306b91c27eb05ef87d2eb78ad2eb99f55dc6223cf16aca1e583e417` (re-verified pod == local) |

Full per-file SHA-256 manifest: `PACKED_SHA256SUMS.json` in each of the three
locations below (17 hashed at land time + the tar re-verified separately).

## Enrichment manifest binding (flagship_enriched_manifest.json)

- `contract_sha256`: `6699d09ff886f74dab6608bd70a70b73b7a34afabc436d365c69f16a95ac5edf`
- `input_sample_sha256`: `b5144115aba9ba18201496d166f2e501ba7657759ca56539aa548dd731090fae`
- `model_sha256`: `f5266ba48f476bca2f1b12610e0e81322caaa955af70ab83f0b05bf763885f07`
- `inference_code_sha256`: `3e7efb243fa5cc4e7e06c5ce8e13f011e1173d2cc44aecd8df47e0c67c0ab996`
- groups: 3,128 completed / 0 skipped / 3,128 total
- MSE cross-check: 0 offenders / 3,810 rows checked, tolerance 1e-6 — PASSED
- Row count verified in-parquet: 3,810 rows, matches manifest

## Three-location backup verification (backup-3plus)

1. **Git (repo)** — small artifacts (all parquet/json/jsonl/logs, NOT the tar)
   committed to `pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3/`
   at commit `0c2b3114`.
2. **Local disk** — `~/Desktop/CODE_YOU/bigbounce_datasets/aug-011-clean-rerun/phase3/2026-09-03/`
   — 18 files including `enrich_shards_part1.tar`; tar SHA-256 re-verified against
   pod source (`83f89ef4e3...`, match).
3. **HuggingFace** — `bamfai/bigbounce-aug-011-clean-rerun` (dataset repo),
   `phase3/2026-09-03/` — 18/18 files confirmed present via `list_repo_files`,
   sizes match local.
4. **Backblaze B2** — bucket `bigbounce`, key prefix
   `aug-011-clean-rerun/phase3/2026-09-03/` — 18/18 files confirmed present via
   `list_objects_v2`, sizes byte-identical to local.

All 4 locations (git counts as a 4th for the small artifacts; tar is on 3:
local+HF+B2) confirmed consistent. Pod NOT stopped (coordinator hold).
