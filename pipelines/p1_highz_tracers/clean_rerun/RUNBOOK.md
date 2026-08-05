# AUG-011 pod campaign runbook: clean public-ID-first DESI DR1 rerun

Executes the fail-closed scaffold in `pipelines/p1_highz_tracers/clean_rerun_contract.py`
(never modify) against a fresh DESI DR1 `iron` scan, using the archived
`best_model_47k.pt` and `outputs/enhanced_18M/enhanced_18M_inference.py`
(never modify). See `clean_rerun_contract.md` for the manifest/calibration
shapes and `project-context/ANOMALY_SCIENCE_CLAIM_INVENTORY_2026-08-03.md`
("Restoration gate result", "Clean-rerun contract implemented") for why the
historical enhanced generation cannot be reused and why this is a fresh
scan, not a reconciliation.

Historical counts (195,829 / 249,905 `S>5` rows) are comparison labels only.
This run is never tuned or truncated to match them.

## 0. Honest scale estimates (read before provisioning)

- `zall-pix-iron.fits` zcatalog: ~27 GB (single file, one-time download).
- Full DESI DR1 `iron` healpix coadd corpus (main survey, dark+bright,
  every healpix pixel referenced by the zcatalog): multi-terabyte, spread
  across tens of thousands of `coadd-<survey>-<program>-<healpix>.fits`
  files. There is no bulk single-archive download for this — `run_scan.py`
  streams it pixel-by-pixel and deletes each coadd immediately after
  scoring, so local disk never needs to hold more than a few coadd files
  plus the running Parquet shard set at once.
- The scan is **download-bound**, not GPU-bound: the archived model is
  small (3.5 MB, 496->128 BigAE) and inference on a downsampled 496-bin
  spectrum batch is fast even on CPU. Wall-clock is dominated by DESI
  archive download throughput and per-pixel HTTP overhead across tens of
  thousands of healpix groups — budget accordingly (this is why
  `--start`/`--end` parallel workers matter far more than GPU class).
- A single A4000-class GPU (or a CPU-strong instance with several download
  threads) is sufficient; this is not a training run.
- Calibration (step 6, `build_calibration.py`) is a SEPARATE, bounded
  download: a two-stage PPS cluster sample over ~200 coadd groups,
  ~25 GB total — never the near-full-corpus multi-terabyte download a
  naive uniform 40,000-row draw over the zcatalog would cause. See step 6
  and `build_calibration.py`'s module docstring.

## 1. Provision the pod

- RunPod, A4000-class GPU or a CPU-strong instance (per §0, this is
  download-bound, not GPU-bound).
- Volume: ~200 GB (zcatalog ~27 GB + working room for a handful of
  in-flight coadds + accumulating Parquet shards + receipts/checkpoints;
  coadds are deleted immediately after scoring so the corpus itself never
  needs to fit on disk).
- Follow standing directive E (`/backup-3plus` / `/pod-backup-before-stop`):
  never single-source pod data.

## 2. Install dependencies

```sh
pip install torch astropy pyarrow numpy
```

(`pytest` only if running the offline test suite on the pod too.)

## 3. Download + SHA-verify the zcatalog

```sh
cd /workspace
curl -O https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/v1/zall-pix-iron.fits
curl -O https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/v1/redux_iron_zcatalog_v1.sha256sum
sha256sum -c redux_iron_zcatalog_v1.sha256sum
# Must report zall-pix-iron.fits: OK. If it does not, STOP — do not proceed.
shasum -a 256 zall-pix-iron.fits
# Must equal 2d95ad99361039b556c402b49e0e7c84df5f00106dc5731d44476a58b128b49b
```

## 4. Derive the locator inventory

```sh
python3 pipelines/p1_highz_tracers/clean_rerun/derive_locator_inventory.py derive-inventory \
  --zcatalog /workspace/zall-pix-iron.fits \
  --manifest pipelines/p1_highz_tracers/clean_rerun/input_manifest.draft.json \
  --output /workspace/locator_inventory.jsonl
```

Fails closed if `/workspace/zall-pix-iron.fits`'s SHA-256 does not match the
draft manifest's `catalog_sha256`.

## 5. Finalize the input manifest

```sh
python3 pipelines/p1_highz_tracers/clean_rerun/derive_locator_inventory.py finalize-manifest \
  --draft pipelines/p1_highz_tracers/clean_rerun/input_manifest.draft.json \
  --inventory /workspace/locator_inventory.jsonl \
  --output /workspace/input_manifest.json
```

`input_manifest.json` now has a real `locator_inventory_sha256` and will
pass `clean_rerun_contract.py`'s `require_sha()` check. Never hand-edit that
field.

## 6. Build calibration

```sh
python3 pipelines/p1_highz_tracers/clean_rerun/build_calibration.py \
  --zcatalog /workspace/zall-pix-iron.fits \
  --manifest /workspace/input_manifest.json \
  --model best_model_47k.pt \
  --coadd-cache-dir /workspace/calibration_coadd_cache \
  --training-manifest-output /workspace/training_manifest.json \
  --validation-manifest-output /workspace/validation_manifest.json \
  --output /workspace/calibration.json
```

Draws a **bounded two-stage PPS (probability-proportional-to-size) cluster
sample** (seed `20260804`, `--n-groups` default 200, `--n-rows` default
40,000): pass 1 streams the zcatalog to count rows per `(survey, program,
healpix)` group; stage 2 selects 200 distinct groups with probability
proportional to group size; stage 3 allocates the 40,000-row budget across
those 200 groups (largest-remainder rounding) and, after a second bounded
pass 2 collects row indices for only those 200 groups, samples each
group's allocated rows with the same RNG; a final seeded permutation splits
the 40,000 rows into the first 20,000 (fit) and last 20,000 (held-out
validation). **This replaces the original naive design that drew 40,000
uniform row indices directly from the zcatalog** — a uniform draw over the
~23M-row zcatalog hits roughly two-thirds of all ~35,000 coadd groups
(~24,000 distinct coadd downloads, multi-terabyte); the two-stage cluster
sample instead expects to download only the ~200 selected coadds
(~25 GB total). Both halves are drawn from the same 200-group pixel
population by construction, so the stability gate below is a
within-pixel-population compatibility check, not a cross-pixel
generalization check.

Scores both halves through the archived inference path, and refuses to
seal (non-zero exit, `CalibrationError`) if the held-out validation mean
drifts more than 5x the fit-set standard error from the fit mean. See the
module docstring in `build_calibration.py` for the full design rationale,
including the design-effect note on why this 5x gate is conservative in
the fail-closed direction only under cluster sampling.

## 7. Build the run contract

```sh
python3 pipelines/p1_highz_tracers/clean_rerun_contract.py build-contract \
  --model best_model_47k.pt \
  --inference-code pipelines/p1_highz_tracers/outputs/enhanced_18M/enhanced_18M_inference.py \
  --input-manifest /workspace/input_manifest.json \
  --calibration /workspace/calibration.json \
  --output /workspace/run-contract.json
```

Binds the model SHA-256 + architecture, the inference-code SHA-256, the
sealed input manifest, and the sealed calibration into one contract. Every
downstream step re-verifies against this file.

## 8. Smoke run (5 healpix groups)

```sh
python3 pipelines/p1_highz_tracers/clean_rerun/run_scan.py \
  --inventory /workspace/locator_inventory.jsonl \
  --contract /workspace/run-contract.json \
  --model best_model_47k.pt \
  --shard-dir /workspace/shards \
  --receipt-dir /workspace/receipts \
  --checkpoint /workspace/checkpoint.json \
  --coadd-cache-dir /workspace/coadd_cache \
  --limit 5
```

Then verify receipts:

```sh
python3 pipelines/p1_highz_tracers/clean_rerun_contract.py verify-receipts \
  --contract /workspace/run-contract.json \
  --shard-dir /workspace/shards \
  --receipt-dir /workspace/receipts
```

Confirm 5 shards, 5 receipts, `verify-receipts` reports success, and each
downloaded coadd file was deleted from `/workspace/coadd_cache` after
scoring before proceeding to the full scan.

## 9. Full scan

Single worker:

```sh
python3 pipelines/p1_highz_tracers/clean_rerun/run_scan.py \
  --inventory /workspace/locator_inventory.jsonl \
  --contract /workspace/run-contract.json \
  --model best_model_47k.pt \
  --shard-dir /workspace/shards \
  --receipt-dir /workspace/receipts \
  --checkpoint /workspace/checkpoint.json \
  --coadd-cache-dir /workspace/coadd_cache
```

Parallel pod workers (disjoint inventory slices; each worker needs its own
`--shard-dir`/`--receipt-dir`/`--checkpoint`/`--coadd-cache-dir`, or a
shared `--shard-dir`/`--receipt-dir` with per-worker checkpoints — prefer
separate checkpoints per worker to avoid `record-receipt`'s "receipt bound
to a different contract" / concurrent-write races on one checkpoint file):

```sh
# worker 0
python3 pipelines/p1_highz_tracers/clean_rerun/run_scan.py \
  --inventory /workspace/locator_inventory.jsonl --contract /workspace/run-contract.json \
  --model best_model_47k.pt --shard-dir /workspace/shards --receipt-dir /workspace/receipts \
  --checkpoint /workspace/checkpoint_w0.json --coadd-cache-dir /workspace/coadd_cache_w0 \
  --start 0 --end 5000

# worker 1
python3 pipelines/p1_highz_tracers/clean_rerun/run_scan.py \
  --inventory /workspace/locator_inventory.jsonl --contract /workspace/run-contract.json \
  --model best_model_47k.pt --shard-dir /workspace/shards --receipt-dir /workspace/receipts \
  --checkpoint /workspace/checkpoint_w1.json --coadd-cache-dir /workspace/coadd_cache_w1 \
  --start 5000 --end 10000
# ...and so on, one range per worker.
```

Restarting a worker with the same `--checkpoint` path resumes automatically
(already-recorded shards are skipped).

## 10. Backup-3plus every ~2h (standing directive E — ALWAYS, not just before stop)

Every ~2h of scan wall-clock, mirror the growing shard/receipt/checkpoint
set to 3+ locations:

```sh
# 1. local pull (from your workstation)
rsync -avz pod:/workspace/shards/     ./local-backup/aug-011/shards/
rsync -avz pod:/workspace/receipts/   ./local-backup/aug-011/receipts/
rsync -avz pod:/workspace/checkpoint*.json ./local-backup/aug-011/

# 2. HuggingFace (bamfai org repo)
huggingface-cli upload bamfai/bigbounce-aug-011-clean-rerun \
  ./local-backup/aug-011 . --repo-type dataset

# 3. Backblaze B2
b2 sync ./local-backup/aug-011 b2://<bucket>/aug-011-clean-rerun/
```

Never stop the pod without confirming all 3 locations are current
(`/pod-backup-before-stop`).

## 11. Verify receipts (full corpus)

```sh
python3 pipelines/p1_highz_tracers/clean_rerun_contract.py verify-receipts \
  --contract /workspace/run-contract.json \
  --shard-dir /workspace/shards \
  --receipt-dir /workspace/receipts
```

Re-run after every backup checkpoint and again once the scan is declared
complete.

## 12. Summarize after dedup

```sh
python3 pipelines/p1_highz_tracers/clean_rerun_contract.py summarize-after-dedup \
  --contract /workspace/run-contract.json \
  --shard-dir /workspace/shards \
  --receipt-dir /workspace/receipts \
  --sqlite /workspace/dedup.sqlite \
  --output /workspace/summary.json
```

Streams every verified shard through SQLite, keeps the **last** row per
`targetid` in lexical shard-then-row order, and only then counts rows above
`selection_threshold` (5.0). `--sqlite` must point to a path that does not
already exist.

## 13. Compare generations

```sh
python3 pipelines/p1_highz_tracers/clean_rerun_contract.py compare-generations \
  --new-summary /workspace/summary.json \
  --output /workspace/comparison.json
```

Produces a comparison record against the two historical generation labels.
This is explicitly a comparison, never a reconciliation or validation of
either historical count, and the new run is never tuned or truncated to
match them.

## Recovery notes

- Every step re-verifies its inputs by SHA-256 before doing anything; a
  corrupted/incomplete download or a mismatched model/inference-code file
  on the pod fails closed with a clear error rather than silently scoring
  with the wrong artifact.
- `run_scan.py` resume is automatic per-checkpoint: rerun the exact same
  command after any interruption (OOM, network drop, spot-instance
  preemption) and already-recorded shards are skipped.
- If the calibration stability gate in step 6 fails, do not loosen the 5x
  bound to force a seal — investigate the download/scoring path first (see
  `build_calibration.py`'s module docstring for what a failure there
  usually means).
