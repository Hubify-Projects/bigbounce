#!/bin/bash
# AUG-011 phase 3: sealed S>8 sample -> enrichment -> SIMBAD/NED -> WISE -> taxonomy.
set -euo pipefail
cd /workspace
R=/workspace/bigbounce/pipelines/p1_highz_tracers
LOG=/workspace/phase3.log
mark() { echo "== $(date -u +%FT%TZ) $1" | tee -a "$LOG"; }
mark "build sealed sample (S>8)"
python3 "$R/clean_rerun/build_flagship_sample.py" --contract /workspace/run-contract.json \
  --shard-dir /workspace/shards --receipt-dir /workspace/receipts --summary /workspace/summary.json \
  --score-threshold 8.0 --output-sample /workspace/flagship_sample_s8.parquet \
  --output-manifest /workspace/flagship_sample_s8_manifest.json 2>&1 | tail -5 | tee -a "$LOG"
mark "enrich sample (per-band SNR + latents, mse cross-check gate)"
python3 "$R/clean_rerun/enrich_flagship_sample.py" --sample /workspace/flagship_sample_s8.parquet \
  --sample-manifest /workspace/flagship_sample_s8_manifest.json --contract /workspace/run-contract.json \
  --model /workspace/bigbounce/best_model_47k.pt --zcatalog /workspace/zall-pix-iron.fits \
  --coadd-cache-dir /workspace/enrich_cache --shard-dir /workspace/shards \
  --checkpoint /workspace/enrich_checkpoint.json --audit-log /workspace/enrich_audit.jsonl \
  --output /workspace/flagship_sample_s8_enriched.parquet \
  --manifest-output /workspace/flagship_enriched_manifest.json 2>&1 | tail -6 | tee -a "$LOG"
mark "SIMBAD/NED crossmatch"
python3 "$R/clean_rerun/crossmatch_flagship.py" --input-sample /workspace/flagship_sample_s8.parquet \
  --input-manifest /workspace/flagship_sample_s8_manifest.json --zcatalog /workspace/zall-pix-iron.fits \
  --checkpoint-dir /workspace/crossmatch_ckpt --output-matched /workspace/flagship_crossmatch_matched.parquet \
  --output-unmatched /workspace/flagship_crossmatch_unmatched.parquet \
  --output-manifest /workspace/flagship_crossmatch_manifest.json 2>&1 | tail -5 | tee -a "$LOG"
mark "WISE photometry join"
python3 "$R/clean_rerun/wise_join_flagship.py" --input-enriched /workspace/flagship_sample_s8_enriched.parquet \
  --input-enriched-manifest /workspace/flagship_enriched_manifest.json --checkpoint /workspace/wise_checkpoint.json \
  --output /workspace/flagship_wise.parquet --output-manifest /workspace/flagship_wise_manifest.json 2>&1 | tail -5 | tee -a "$LOG"
mark "taxonomy (descriptive families, Q1 labels)"
python3 "$R/clean_rerun/taxonomy_flagship.py" --input-unmatched /workspace/flagship_crossmatch_unmatched.parquet \
  --input-crossmatch-manifest /workspace/flagship_crossmatch_manifest.json \
  --output-results /workspace/flagship_taxonomy.json --output-manifest /workspace/flagship_taxonomy_manifest.json 2>&1 | tail -5 | tee -a "$LOG"
mark "PHASE3-DONE"; touch /workspace/PHASE3_DONE
