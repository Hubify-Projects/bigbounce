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
- Calibration (step 7, `build_calibration.py`) is a SEPARATE, bounded
  download: a two-stage PPS cluster sample over ~200 coadd groups,
  ~25 GB total — never the near-full-corpus multi-terabyte download a
  naive uniform 40,000-row draw over the zcatalog would cause. See step 7
  and `build_calibration.py`'s module docstring.
- **Public-ID-first filter rule.** The AUG-011 clean-rerun smoke test found
  that a DESI DR1 coadd file for a given `(survey, program, healpix)` group
  can contain real, unique, positive TARGETIDs that are NOT rows of the
  sealed `zall-pix-iron` zcatalog for that same group — e.g. group
  `cmx/other/2154` has 139 zcatalog rows but 284 coadd spectra. The paper's
  primary sample must contain ONLY TARGETIDs vouched for by the SHA-verified
  zcatalog; surplus coadd spectra are dropped, and dropped WITH an honest
  audit trail, never silently. **Audit-log honesty contract:** `run_scan.py`
  appends one JSON line per group to `--audit-log`
  (`{survey, program, healpix, coadd_rows, zcat_rows, kept, surplus_dropped,
  zcat_missing_from_coadd}`) for every group it scores, whether or not any
  rows were dropped, and fails closed (aborts the run) rather than shipping
  a shard for a group with zero zcatalog targetids or with more than 1% of
  its zcatalog targetids missing a coadd spectrum.

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

## 6. Export the group-targetids parquet (public-ID-first filter source)

```sh
python3 pipelines/p1_highz_tracers/clean_rerun/derive_locator_inventory.py export-group-targetids \
  --zcatalog /workspace/zall-pix-iron.fits \
  --manifest /workspace/input_manifest.json \
  --output /workspace/group_targetids.parquet
```

Streams the same SHA-verified zcatalog a second time and writes ONE Parquet
file of every real `(survey, program, healpix, targetid)` row, sorted by
`(survey, program, healpix, targetid)`, printing its SHA-256 on completion.
This ~23M-row file is the public-ID-first source of truth `run_scan.py`
filters every scored coadd against in step 9 — see §0 above for the rule it
enforces and why it exists.

## 7. Build calibration

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

## 8. Build the run contract

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

## 9. Smoke run (5 healpix groups)

```sh
python3 pipelines/p1_highz_tracers/clean_rerun/run_scan.py \
  --inventory /workspace/locator_inventory.jsonl \
  --contract /workspace/run-contract.json \
  --model best_model_47k.pt \
  --shard-dir /workspace/shards \
  --receipt-dir /workspace/receipts \
  --checkpoint /workspace/checkpoint.json \
  --coadd-cache-dir /workspace/coadd_cache \
  --group-targetids /workspace/group_targetids.parquet \
  --audit-log /workspace/scan_audit.jsonl \
  --limit 5
```

Then verify receipts:

```sh
python3 pipelines/p1_highz_tracers/clean_rerun_contract.py verify-receipts \
  --contract /workspace/run-contract.json \
  --shard-dir /workspace/shards \
  --receipt-dir /workspace/receipts
```

Confirm 5 shards, 5 receipts, `verify-receipts` reports success, 5 lines
appended to `/workspace/scan_audit.jsonl` (one per group, honestly reporting
`kept`/`surplus_dropped`/`zcat_missing_from_coadd` even when nothing was
dropped), and each downloaded coadd file was deleted from
`/workspace/coadd_cache` after scoring before proceeding to the full scan.

## 10. Full scan

Single worker:

```sh
python3 pipelines/p1_highz_tracers/clean_rerun/run_scan.py \
  --inventory /workspace/locator_inventory.jsonl \
  --contract /workspace/run-contract.json \
  --model best_model_47k.pt \
  --shard-dir /workspace/shards \
  --receipt-dir /workspace/receipts \
  --checkpoint /workspace/checkpoint.json \
  --coadd-cache-dir /workspace/coadd_cache \
  --group-targetids /workspace/group_targetids.parquet \
  --audit-log /workspace/scan_audit.jsonl
```

Parallel pod workers (disjoint inventory slices; each worker needs its own
`--shard-dir`/`--receipt-dir`/`--checkpoint`/`--coadd-cache-dir`, or a
shared `--shard-dir`/`--receipt-dir` with per-worker checkpoints — prefer
separate checkpoints per worker to avoid `record-receipt`'s "receipt bound
to a different contract" / concurrent-write races on one checkpoint file;
give each worker its own `--audit-log` too, e.g. `scan_audit_w0.jsonl`, so
concurrent appends never interleave-corrupt one file):

```sh
# worker 0
python3 pipelines/p1_highz_tracers/clean_rerun/run_scan.py \
  --inventory /workspace/locator_inventory.jsonl --contract /workspace/run-contract.json \
  --model best_model_47k.pt --shard-dir /workspace/shards --receipt-dir /workspace/receipts \
  --checkpoint /workspace/checkpoint_w0.json --coadd-cache-dir /workspace/coadd_cache_w0 \
  --group-targetids /workspace/group_targetids.parquet --audit-log /workspace/scan_audit_w0.jsonl \
  --start 0 --end 5000

# worker 1
python3 pipelines/p1_highz_tracers/clean_rerun/run_scan.py \
  --inventory /workspace/locator_inventory.jsonl --contract /workspace/run-contract.json \
  --model best_model_47k.pt --shard-dir /workspace/shards --receipt-dir /workspace/receipts \
  --checkpoint /workspace/checkpoint_w1.json --coadd-cache-dir /workspace/coadd_cache_w1 \
  --group-targetids /workspace/group_targetids.parquet --audit-log /workspace/scan_audit_w1.jsonl \
  --start 5000 --end 10000
# ...and so on, one range per worker.
```

Restarting a worker with the same `--checkpoint` path resumes automatically
(already-recorded shards are skipped).

## 11. Backup-3plus every ~2h (standing directive E — ALWAYS, not just before stop)

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
(`/pod-backup-before-stop`). Include every worker's `--audit-log` file in
the mirrored set — the audit trail is as load-bearing as the shards/receipts.

## 12. Verify receipts (full corpus)

```sh
python3 pipelines/p1_highz_tracers/clean_rerun_contract.py verify-receipts \
  --contract /workspace/run-contract.json \
  --shard-dir /workspace/shards \
  --receipt-dir /workspace/receipts
```

Re-run after every backup checkpoint and again once the scan is declared
complete.

## 13. Summarize after dedup

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

## 14. Compare generations

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
- If the calibration stability gate in step 7 fails, do not loosen the 5x
  bound to force a seal — investigate the download/scoring path first (see
  `build_calibration.py`'s module docstring for what a failure there
  usually means).
- `run_scan.py`'s public-ID-first filter (step 9/10) fails closed and aborts
  the run if a group has zero zcatalog targetids, or if more than 1% of a
  group's zcatalog targetids have no spectrum in the coadd — do not loosen
  that 1% bound to push past a failure; investigate whether
  `--group-targetids` was built from the same zcatalog as `--inventory`
  first (see §0's public-ID-first filter rule).

## PHASE 3. Flagship candidate sample, cross-match, and taxonomy

Runs once step 13 (`summarize-after-dedup`) has produced `/workspace/summary.json`
for the completed, receipt-verified full scan. See
`project-context/ANOMALY_FLAGSHIP_MANUSCRIPT_ARCHITECTURE_2026-08-05.md` §2
for what these deliverables are for and §5 for the dependency gates they
close. Tooling: `build_flagship_sample.py`, `crossmatch_flagship.py`,
`taxonomy_flagship.py` in this directory; offline tests in
`pipelines/p1_highz_tracers/tests/test_flagship_phase3.py`.

Install the phase-3-only dependencies (in addition to §2's `torch astropy
pyarrow numpy`):

```sh
pip install astroquery scikit-learn umap-learn
```

### 15. Describe the post-dedup score distribution (no sample emitted yet)

```sh
python3 pipelines/p1_highz_tracers/clean_rerun/build_flagship_sample.py \
  --contract /workspace/run-contract.json \
  --shard-dir /workspace/shards \
  --receipt-dir /workspace/receipts \
  --summary /workspace/summary.json \
  --describe
```

Fails closed if receipts don't verify or if `/workspace/summary.json`'s
`contract_sha256` does not match `/workspace/run-contract.json`. Prints
quantiles and counts/fractions above the candidate thresholds 3/4/5/6/8/10
sigma. **This output is how `--score-threshold` for step 16 gets decided —
never copy the historical `anomaly_score > 3.0` cut or tune the threshold to
reproduce the historical 2,145-row count** (per the flagship architecture
doc's §2b instruction and this repo's Standing Directive Q1).

### 16. Build the sealed flagship sample

```sh
python3 pipelines/p1_highz_tracers/clean_rerun/build_flagship_sample.py \
  --contract /workspace/run-contract.json \
  --shard-dir /workspace/shards \
  --receipt-dir /workspace/receipts \
  --summary /workspace/summary.json \
  --score-threshold <DECIDED_FROM_STEP_15> \
  --output-sample /workspace/flagship_sample.parquet \
  --output-manifest /workspace/flagship_sample_manifest.json
```

Optional configured quality filters (repeatable): `--exclude-survey cmx`,
`--exclude-program other`, etc. — see `build_flagship_sample.py`'s
docstring for why the historical `max_snr > 0.5` filter is NOT ported
(the new shard schema has no SNR column). The emitted manifest records the
exact rule, thresholds, row count, parent generation id, and full
shard-receipt binding.

### 16b. Enrich the flagship sample (phase-3b: per-band SNR + latents)

```sh
python3 pipelines/p1_highz_tracers/clean_rerun/enrich_flagship_sample.py \
  --sample /workspace/flagship_sample.parquet \
  --sample-manifest /workspace/flagship_sample_manifest.json \
  --contract /workspace/run-contract.json \
  --model best_model_47k.pt \
  --zcatalog /workspace/zall-pix-iron.fits \
  --coadd-cache-dir /workspace/enrich_coadd_cache \
  --shard-dir /workspace/enrich_shards \
  --checkpoint /workspace/enrich_checkpoint.json \
  --audit-log /workspace/enrich_audit.jsonl \
  --output /workspace/flagship_sample_enriched.parquet \
  --manifest-output /workspace/flagship_sample_enriched_manifest.json
```

Step 16's sample carries only `targetid`/`anomaly_score`/`mean_mse`/`survey`/
`program`/`healpix`, by design (`run_scan.py`'s narrow shard schema — see
that script's own docstring). For the SELECTED sample only (thousands of
rows, not the full ~28M-spectrum corpus), this step recovers the richer
per-object features the historical `enhanced_18M_inference.py` pipeline
computed: per-band residuals (`rB`/`rR`/`rZ`), `worst_band`,
`peak_residual_wavelength`, `residual_kurtosis`, `median_coadd_snr_{b,r,z}`,
redrock columns when available (`z`/`zerr`/`zwarn`/`spectype`/`subtype`/
`deltachi2` — carried at their documented defaults since, like `run_scan.py`,
this step never downloads a separate redrock file), FIBERMAP photometry, and
the 128-dim BigAE latent vector as `latent_000..latent_127`. It re-downloads
each needed coadd exactly once per `(survey, program, healpix)` group the
sample touches, scores it through the SAME archived, contract-bound
`process_healpix()` (imported unmodified — never copied or re-derived),
keeps ONLY the sample's targetids, and deletes the coadd immediately after
scoring, exactly like `run_scan.py`.

**Cross-check gate.** For every enriched row, the recomputed per-spectrum
mean MSE must reproduce that targetid's `mean_mse` from step 16's sample to
within 1e-6 relative tolerance — proof the enrichment used bit-identical
arithmetic to the original scan, not a re-implementation that merely looks
similar. Any mismatch fails the run closed and lists every offending
targetid in `--audit-log`; no `--output`/`--manifest-output` is written
until zero offenders remain.

**Fault barrier + resume**, exactly like `run_scan.py`: a failed group
(archive outage, partial download, scoring error) is skipped with an audit
line rather than aborting the whole run, and the run exits nonzero (3) if
any group was skipped — rerun the identical command to retry only the
skipped groups (`--checkpoint`-bound to this exact sample + contract SHA, so
already-completed groups are never re-downloaded). The FINAL merged
`--output` is written ONLY once every group in the sample has a completed,
checkpointed shard.

### 16c. WISE photometry join (phase-3c: IR colors for taxonomy)

```sh
python3 pipelines/p1_highz_tracers/clean_rerun/wise_join_flagship.py \
  --input-enriched /workspace/flagship_sample_enriched.parquet \
  --input-enriched-manifest /workspace/flagship_sample_enriched_manifest.json \
  --checkpoint /workspace/wise_join_checkpoint.json \
  --output /workspace/flagship_wise.parquet \
  --output-manifest /workspace/flagship_wise_manifest.json
```

Step 16b's enriched output carries `target_ra`/`target_dec` straight through
from the archived FIBERMAP columns, so this step needs no zcatalog re-join.
For each enriched-sample row it cone-searches the AllWISE catalog
(`II/328/allwise`) via `astroquery.vizier.Vizier` — the SAME VizieR catalog
the historical `neowise_crossmatch.py`/`neowise_crossmatch_silver.py`
queried by hand (raw `requests` against the VizieR TAP endpoint) for
`w1w2_color`/`agn_ir_color`; only the client library changed (astroquery),
matching the precedent step 17's SIMBAD/NED port already set. Default cone
radius is 3 arcsec; when a cone search returns more than one AllWISE
candidate, the nearest one by angular separation is kept. Fails closed if
the enriched sample's SHA-256 doesn't match its manifest. Resumable: rerun
the identical command to pick up from `--checkpoint`'s per-targetid JSON
checkpoint (default: checkpoint + print progress every 50 queries, 1.0s
sleep between queries — tune with `--checkpoint-every`/`--rate-limit-sleep`).
For a bounded smoke run first, add `--limit 20`.

Output: a Parquet keyed by `targetid` with `w1`/`w2`/`w1_w2`
(`w1 - w2` color) /`match_separation_arcsec`/`match_flag`; unmatched rows
carry `match_flag=False` and null `w1`/`w2`/`w1_w2`/
`match_separation_arcsec` rather than a fabricated color. This output is
directly usable as `taxonomy_flagship.py`'s `--extra-features` (a Parquet
keyed by `targetid` with extra numeric feature columns) — e.g. add
`w1_w2` (and/or `w1`/`w2` individually) to step 18's `--feature-columns` to
cluster on IR color once this step has run, the new-generation analog of
the historical "IR-bright AGN candidate" (`W1-W2 > 0.8`, Stern+2012) family.

### 17. Cross-match the flagship sample against SIMBAD/NED

```sh
python3 pipelines/p1_highz_tracers/clean_rerun/crossmatch_flagship.py \
  --input-sample /workspace/flagship_sample.parquet \
  --input-manifest /workspace/flagship_sample_manifest.json \
  --zcatalog /workspace/zall-pix-iron.fits \
  --checkpoint-dir /workspace/crossmatch_checkpoints \
  --output-matched /workspace/flagship_matched.parquet \
  --output-unmatched /workspace/flagship_unmatched.parquet \
  --output-manifest /workspace/flagship_crossmatch_manifest.json
```

Fails closed if the sample's SHA-256 doesn't match its manifest, or if
`--zcatalog`'s SHA-256 doesn't match the manifest's bound `catalog_sha256`
(i.e. it is not the exact zcatalog the sample's targetids came from).
Recovers RA/Dec by streaming that same zcatalog in bounded chunks (the new
shard schema has no ra/dec columns). Resumable: re-running the identical
command picks up from `--checkpoint-dir`'s per-service JSON checkpoints
(default: checkpoint + print progress every 50 queries, 1.0s sleep between
queries per service — tune with `--checkpoint-every`/`--rate-limit-sleep`).
For a bounded smoke run first, add `--limit 20`.

### 18. Build the candidate-family taxonomy on the unmatched subset

```sh
python3 pipelines/p1_highz_tracers/clean_rerun/taxonomy_flagship.py \
  --input-unmatched /workspace/flagship_unmatched.parquet \
  --input-crossmatch-manifest /workspace/flagship_crossmatch_manifest.json \
  --output-results /workspace/flagship_taxonomy_results.json \
  --output-manifest /workspace/flagship_taxonomy_manifest.json
```

Fails closed if the unmatched table's SHA-256 doesn't match the crossmatch
manifest. Ports the historical clustering METHOD (PCA -> UMAP -> HDBSCAN[leaf]
-> kNN noise reassignment -> descriptor-identity family merge) but — read
`taxonomy_flagship.py`'s module docstring before trusting the family labels —
the new shard schema carries no latent vectors, WISE colors, spectype, or
line IDs, so labels are GENERIC score-tier + provenance descriptors only
("candidate family", never an astrophysical class name), per Standing
Directive Q1. If a companion feature-extraction step for the new generation
is ever built, pass it via `--extra-features` (a Parquet keyed by
`targetid`) to enrich labeling without touching the clustering pipeline.
**That companion step now exists (step 16b, `enrich_flagship_sample.py`)**:
pass its `--output` (`flagship_sample_enriched.parquet`) as
`--extra-features` here — e.g. `--feature-columns
anomaly_score,ra,dec,rB,rR,rZ,median_coadd_snr_b,median_coadd_snr_r,median_coadd_snr_z,latent_000,...,latent_127`
— to cluster on real per-band SNR and/or BigAE latents instead of
`anomaly_score`/`ra`/`dec` alone. This still does not license astrophysical
class-name labels (spectype/WISE-color-based labeling per Standing Directive
Q1 needs the redrock/photometry columns too, and step 16b's `spectype`/`z`
stay at their documented defaults since no redrock file is downloaded); it
does make the taxonomy's cluster GEOMETRY meaningfully richer.

**Step 16c (`wise_join_flagship.py`) now supplies the WISE-color half of
that gap.** Its output (`flagship_wise.parquet`) is also `targetid`-keyed and
can be passed as `--extra-features` (or joined into the same feature Parquet
as step 16b's output before passing it here) to add `w1_w2` — e.g.
`--feature-columns anomaly_score,ra,dec,w1_w2` — to the clustering feature
set. `w1_w2` alone is still a color diagnostic, not a family label:
Standing Directive Q1 labeling still requires GENERIC descriptors here
(score tier + provenance), never an astrophysical class name, even once IR
color is available as a feature.

### Recovery notes (phase 3)

- All four phase-3 tools re-verify their upstream SHA-256 bindings before
  doing anything (receipts, contract-summary binding, sample-manifest
  binding, zcatalog binding) — a stale or swapped intermediate artifact
  fails closed with a clear error instead of silently producing a
  provenance-inconsistent sample/enrichment/crossmatch/taxonomy.
- `enrich_flagship_sample.py` (step 16b) resume is automatic per
  `--checkpoint`: rerun the exact same command after any interruption and
  already-completed `(survey, program, healpix)` groups are never
  re-downloaded; its MSE cross-check gate re-runs from the cached per-group
  shards on every incarnation (no network needed) and still fails closed on
  any offender.
- `crossmatch_flagship.py` resume is automatic per `--checkpoint-dir`: rerun
  the exact same command after any interruption and already-queried
  targetids are skipped for that service.
- `wise_join_flagship.py` (step 16c) resume is automatic per `--checkpoint`:
  rerun the exact same command after any interruption (network drop, AllWISE
  outage) and already-queried targetids are skipped; a query that raised
  before being checkpointed is retried on the next incarnation.
- Run the offline test suite before trusting a fresh phase-3 change:
  `python3 -m pytest pipelines/p1_highz_tracers/tests/ -q`.

### 19. Known-object recovery benchmark (ledger #8)

Answers `project-context/NEXT_SCIENCE_LEDGER.md` row 8: does the flagship
catalogue recover published "unusual object" classes above the base rate an
untargeted cut would give? Runs once step 16b (`enrich_flagship_sample.py`)
has produced a `target_ra`/`target_dec`-bearing sample for BOTH the S>5
catalogue and the S>8 deep sample (step 16's raw `flagship_sample.parquet`
has no ra/dec — see `benchmark_known_object_recovery.py`'s docstring).
Tooling: `benchmark_known_object_recovery.py` in this directory; offline
tests in `pipelines/p1_highz_tracers/tests/test_recovery_benchmark.py`.

Stage 1 — fetch reference "unusual object" classes from VizieR (network
required; run from a host that can reach `vizier.cds.unistra.fr`'s query
endpoint, not just its TCP port — verified to be the working combination
from Houston's machine, not from every sandbox):

```sh
python3 pipelines/p1_highz_tracers/clean_rerun/benchmark_known_object_recovery.py \
  --fetch-references \
  --reference-cache-dir /path/outside/repo/reference_catalogs \
  --row-limit 200000
```

Stage 2 — cross-match against the full S>5 and S>8 samples (edit
`catalogs_config_example.json`'s `path`/`catalog_total_at_threshold` to the
real `flagship_sample_enriched.parquet` paths and counts once phase 3 has
completed and the S>5 sample has been ra/dec-joined; the S>5 raw sample
needs a coordinate join like `crossmatch_flagship.py`'s or a run through
`enrich_flagship_sample.py`):

```sh
python3 pipelines/p1_highz_tracers/clean_rerun/benchmark_known_object_recovery.py \
  --crossmatch \
  --reference-cache-dir /path/outside/repo/reference_catalogs \
  --catalogs-config pipelines/p1_highz_tracers/clean_rerun/catalogs_config_example.json \
  --locator-inventory pipelines/p1_highz_tracers/clean_rerun/sealed_2026-08-05/locator_inventory.jsonl \
  --radius-arcsec 1.5 \
  --out-dir pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3/recovery_benchmark
```

Fails closed if a required column is missing from a catalogue, or if the
locator inventory is absent/empty; never fabricates a matched-row count.
A class that could not be fetched (no network, bad VizieR ID, no known
catalogue ID) is recorded `status: "unavailable"`/`"no_catalog_id_known"`
with the raw error, and is simply excluded from the cross-match rather than
faked. Per ledger #8's exit rule: >=1 class with recovery enrichment > 10x
over the catalogue's base rate and >=5 matches is a "confirmed class"
signal (`is_closed_loop_candidate: true` in the output JSON) worth writing
up as a paper section; otherwise the catalogue's own honest recovery table
stands as the headline result for a data-release framing.

A PREVIEW run (2026-09-02, before phase 3 completed) is committed at
`results_2026-08-07/phase3/recovery_benchmark_preview/` against the
57/3810-group PARTIAL S>8 enrichment bundle
(HF `phase3/2026-08-26/partial-enrichment-s8/`) — it returned 0 fetched
reference classes because this build's environment could not reach
VizieR's query endpoint (see that run's manifest for the exact per-class
error); it demonstrates the pipeline mechanics end-to-end on real (not
synthetic) catalogue data, not a real recovery result. Re-run stage 1 from
a networked host, then re-run stage 2 against the full phase-3 outputs, to
get the real answer to ledger item #8.
