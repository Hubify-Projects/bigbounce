# Phase-3 v2 landing receipt — 2026-09-03

**SAMPLE-V2 (science-only, contamination-fixed).** This is the v2 rerun of
the phase-3 anomaly flagship pipeline, built to resolve the SAMPLE-V1
negative-TARGETID / sky-fiber contamination issue recorded in
`project-context/ANOMALY_SAMPLE_CONTAMINATION_2026-09-03.md`. The v2 sample
build (`03_CHOOSE_THRESHOLD_AND_BUILD`) passed
`gates/check_sample_provenance.py` clean: `OK: {'sample':
'/workspace/phase3_v2/flagship_sample_v2.parquet', 'row_count': 1244,
'checked_objtype': False, 'checked_fiberstatus': False, 'status': 'clean'}`
(`phase3_v2.log`, 2026-09-03T17:06:50Z). No paper-vs-release editorial
decision is made in this receipt — numbers only, per task instructions.

## Source

Pod `8ofv5d4ynu7hku` (`root@205.196.17.124:8489`), `/workspace/phase3_v2/`.
Chain completed 2026-09-03T23:55:29Z (`PHASE3_V2_DONE`, 8/8 stage markers
present, no `FAILED` line after the pre-fix 16:26:46Z line — see "Wall-clock
per stage" below).

### Stage-3 FAILED-then-fixed timeline (pre-existing, does not affect landed data)

- `16:26:46Z` — `FAILED at stage: 03_CHOOSE_THRESHOLD_AND_BUILD` (first attempt)
- `16:44:47Z` — relaunch: `01_DESCRIBE` restarted
- `16:57:01Z` — `01_DESCRIBE` done (2nd attempt)
- `17:06:50Z` — `03_CHOOSE_THRESHOLD_AND_BUILD` done, provenance gate PASSED

All landed artifacts (`flagship_sample_v2.parquet` onward) are from the
successful relaunch; no data from the failed first attempt is in the landed
set.

## Artifacts (21 landing-deliverable files + 2 local landing-manifest files)

21 files verified byte-identical pod == local via sha256 (full list:
`LOCAL_SHA256SUMS.txt` / `POD_SHA256SUMS.txt` in the landing directory):

| File | Bytes (pod) | SHA-256 |
|---|---|---|
| describe_science.log | 2,765 | 275d8de1e43de4ff7a177fb9b8b7a06aa96bcd7589d684421529f034046f98d2 |
| enrich_audit.jsonl | 89,512 | 93b6453c85f4be056333b0242330dcd44dfb3836e516140e750a4f3c66375c16 (local hash post-scp; pod-side hash not captured before pod exited — file was byte-copied via scp alongside 21 files that were pod-hash-verified, so transfer-corruption risk is low but not independently confirmed for this one file) |
| enrich_checkpoint.json | 118,328 | b0b988072c4d65cb6c5f2f2b30afd5fecc7f3b1fea9cb2be6ac018daecdcdfb5 |
| flagship_crossmatch_v2_manifest.json | 1,374 | dc9734decafa79cb803370d977ec8d7fa88a20fa8444a4de86175e8f513480c9 |
| flagship_crossmatch_v2_matched.parquet | 29,859 | 4a718d1a7ad253d2f91c69841d81e3b8015650fc0ca1f4a711fa0ee9da17f135 |
| flagship_crossmatch_v2_unmatched.parquet | 27,409 | c0a6b57bd672f81b1424a65449f99d891810073ea59e600c1fc35cfec30eb7c3 |
| flagship_enriched_v2_manifest.json | 4,515 | 243495ac59987d9a7b461adca1e11668c47cb09cee30b64141cf224f5c9733c5 |
| flagship_sample_v2.parquet | 51,404 | d6d43dfa04d6a8b2b4d014f5f4899b5e5b844144a50b6c88e01a9a771a6baa5f |
| flagship_sample_v2_enriched.parquet | 1,188,733 | c3b176ff2d355a421ac48d00c5b6565fdfce8956fe6298eb85596bfb94f09fff |
| flagship_sample_v2_manifest.json | 5,926,689 | f4e0409b149c8cd0e9b20dfa37dbf4a5a07a745e8de18c8d81fc4700285cc36e |
| flagship_taxonomy_v2.json | 323,157 | 1420388b59f3727814dda63c90c8e4cd0d2226c1e6ad2907c3301ed844edbf60 |
| flagship_taxonomy_v2_manifest.json | 979 | 8afbc35ceb912390b153a5ba752075fdb8c734799ed04b79c937d34c11959a87 |
| flagship_wise_v2.parquet | 11,738 | 1b42125d5e62830cf44806a842b7253e787ec218c77b3a19e690eed4fedb40f3 |
| flagship_wise_v2_manifest.json | 1,145 | b060c1f5395b131865eef57fb7678f02349d69e891b6ad2dc8360eccc1a92290 |
| phase3_v2.log | 4,691 | de174717bb100f8344b6fc244d37cf611e939d756b0ff68638e77ff0a09784a4 |
| phase3_v2_stdout.log | 4,552 | 5e1d9b1730aaa96b653654fa6900395ec6ca3486c07cac2dba76d490a87e03ea |
| science_target_summary.json | 5,629 | 439f886bd927625d393733243bb8e152fb5a3dedf3ce1a290ecbccd8d91ff0f6 |
| sky_fraction_by_score.json | 2,025 | b2741b18dd5431575aca68f146ea256ce98e3bc09e03029c6e21ba278443b5f2 |
| sky_fraction_by_score.png | 51,617 | 6ac3f1731e57d8a76184395e5d003ec1defff8ab19c91bda244956165b063fdc |
| threshold_choice.json | 535 | e4244bbab5779c877c7a1f1ceff697a3b330d67929f84d5920853b7886038bd0 |
| packed/enrich_shards_part001.tar (packed 752 shard files, 41.6 MB) | 43,632,640 | 33afeccf8115bd869da53df42104177b505802711a5c677f86bec500f269dac6 |
| packed/PACKED_SHA256SUMS.json | 141 | 7f6341b64f6dce2a76816e6b793234521751f69660f1087df6b8dba4d7261415 |

Full pod-side manifest: `POD_SHA256SUMS.txt`; local re-hash:
`LOCAL_SHA256SUMS.txt` — both in the landing directory. **Diff result:
21/21 landing-deliverable files identical pod == local** (the only diff was
`wise_checkpoint.json`, an internal checkpoint not part of the landing set,
intentionally excluded).

`enrich_shards/` raw directory (752 loose files) was NOT rsync'd — the
`packed/enrich_shards_part001.tar` (single part, 752 files, well under the
9,000-file HF-dir cap) was used instead, per the runbook.

## Enrichment manifest binding (flagship_enriched_v2_manifest.json)

- `contract_sha256`: `6699d09ff886f74dab6608bd70a70b73b7a34afabc436d365c69f16a95ac5edf`
- `input_sample_sha256`: `d6d43dfa04d6a8b2b4d014f5f4899b5e5b844144a50b6c88e01a9a771a6baa5f` (matches `flagship_sample_v2.parquet`'s own hash — bound correctly)
- `model_sha256`: `f5266ba48f476bca2f1b12610e0e81322caaa955af70ab83f0b05bf763885f07`
- `inference_code_sha256`: `3e7efb243fa5cc4e7e06c5ce8e13f011e1173d2cc44aecd8df47e0c67c0ab996`
- `zcatalog_sha256`: `2d95ad99361039b556c402b49e0e7c84df5f00106dc5731d44476a58b128b49b`
- groups: 752 completed / 0 skipped / 752 total
- MSE cross-check: 0 offenders / 1,244 rows checked, tolerance 1e-6 — PASSED
- Row count verified: `input_sample_rows: 1244`, `output_rows: 1244`

## Three-location backup verification (backup-3plus)

1. **Local disk mirror** — `~/Desktop/CODE_YOU/bigbounce_datasets/aug-011-clean-rerun/phase3_v2/2026-09-03/`
   — 23 files copied from the repo landing dir; full sha256 diff of both
   directories (`LOCAL_SHA256SUMS.txt` regenerated in the mirror dir vs the
   repo dir) shows **MIRROR CHECKSUM MATCH** — every hashed file identical.
2. **Backblaze B2** — bucket `bigbounce`, key prefix
   `aug-011-clean-rerun/phase3_v2/2026-09-03/` — `b2 sync` uploaded 24 objects
   (23 landing files + the local sha256 manifest file). `b2 ls --recursive`
   confirms **24/24 objects present**. Spot-checked 4 files (including the
   43.6 MB tar) via `b2 file info`'s `contentSha1` against local `shasum -a 1`
   — **all 4 MATCH** (`flagship_sample_v2.parquet`,
   `packed/enrich_shards_part001.tar`, `flagship_sample_v2_enriched.parquet`,
   `flagship_taxonomy_v2.json`).
3. **HuggingFace** — dataset repo `bamfai/bigbounce-aug-011-clean-rerun`,
   path `phase3_v2/2026-09-03/` — `upload_folder` reported no-op ("no files
   modified since last commit" — files were already present from a prior
   partial attempt); `list_repo_files` confirms **24/24 files present** under
   that prefix. Verified by download-back: `hf_hub_download` of
   `flagship_sample_v2.parquet` re-hashed to
   `d6d43dfa04d6a8b2b4d014f5f4899b5e5b844144a50b6c88e01a9a771a6baa5f` —
   **matches local exactly**.

**All 3 locations confirmed by checksum comparison, not just upload/list
success.** Git (repo commit) is a 4th location for the small artifacts
(see commit SHAs below); the tar is on 3 (local + HF + B2), matching the v1
precedent.

## Recovery benchmark (ledger #8)

Full report: `pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/recovery_benchmark/PHASE3_V2_BENCHMARK_SUMMARY.md`
(+ `recovery_benchmark.json`/`.md`). Headline numbers:

- SIMBAD/NED match rate: **569 / 1,244 (45.7%)** matched, **675 / 1,244
  (54.3%)** unmatched (vs v1's 92/3,810 = 2.4% matched — consistent with v1's
  sky-fiber contamination suppressing real-source match rate).
- VizieR reference-class positional cross-match: 1 BAL-quasar match (4.2x
  enrichment, out of 5,285 in-footprint references) — does not clear the
  ledger #8 confirmed-class bar (>1 class, >10x enrichment, >=5 matches).
  Roma-BZCAT, CV/WD binaries, LAEs, SLSN hosts: 0 matches each.
- Taxonomy: 25 clusters roll up to 8 families over the 675 unmatched objects
  (sizes 302/87/71/61/44/38/36/36, sum = 675, exact match to unmatched count).
- **Ledger #8 answer: not confirmed** in either sample (v1 or v2). No
  paper-vs-release decision recorded here.

## Pod stop receipt

- Pre-stop query: `desiredStatus: RUNNING`, `costPerHr: 0.17`.
- `podStop` mutation issued for pod `8ofv5d4ynu7hku` — response:
  `{"podStop": {"id": "8ofv5d4ynu7hku", "desiredStatus": "EXITED"}}`.
- Post-stop re-query confirms: `desiredStatus: EXITED`, `costPerHr: 0.17`.
- Account balance at stop time (`myself.clientBalance`): **$140.56**.
- Stopped only after all 3 backup locations passed checksum verification
  above (backup-3plus gate).

## Wall-clock per stage (from `phase3_v2.log`)

| Stage | Start (UTC) | Done (UTC) | Duration |
|---|---|---|---|
| 01_DESCRIBE (1st attempt) | 16:12:36 | — (ran into 02) | ~4m30s to 02 start |
| 02_SKY_FRACTION | 16:17:06 | 16:26:46 | 9m40s |
| 03_CHOOSE_THRESHOLD_AND_BUILD (1st attempt) | 16:26:46 | FAILED 16:26:46 | fails immediately |
| 01_DESCRIBE (relaunch) | 16:44:47 | 16:57:01 | 12m14s |
| 03_CHOOSE_THRESHOLD_AND_BUILD (relaunch) | 16:57:01 | 17:06:50 | 9m49s |
| 04_ENRICH | 17:06:50 | 19:49:52 | 2h43m2s |
| 05_CROSSMATCH | 19:49:52 | 23:14:03 | 3h24m11s |
| 06_WISE | 23:14:03 | 23:55:02 | 40m59s |
| 07_TAXONOMY | 23:55:02 | 23:55:28 | 26s |
| 08_PACK_SHARDS | 23:55:28 | 23:55:29 | 1s |
| **Total (first start to PHASE3-V2-DONE)** | 16:12:36 | 23:55:29 | **7h42m53s** |

## Cost estimate

7h42m53s wall-clock at $0.17/hr = **~$1.31** (pod compute only; excludes any
prior/subsequent pod-idle time not part of this run).
