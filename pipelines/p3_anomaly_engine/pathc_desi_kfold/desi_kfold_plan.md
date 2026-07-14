# DESI 5-Fold Out-of-Sample Validation — Path-C Criterion #4

**Task ID:** `P3-PATHC-DESI-KFOLD`
**Status:** staged 2026-04-20 fire #117; launch-blocked on SDSS + LAMOST native rescores freeing the A100
**Owner:** Path-C loop agent
**Criterion gate:** stable top-1% anomaly population across folds (Jaccard overlap ≥ 0.70)

---

## Why this exists

The BigAE released with Paper 3 was trained on a single 47K-spectrum random sample of DESI DR1 and then deployed as-is across the full 22.5M DESI DR1 catalog (plus cross-transferred to SDSS/LAMOST, which Path-C is already fixing via native retrains). The 195,829 DESI DR1 anomalies (top 1%) and the 58.8% SIMBAD-novelty headline both rest on this single training run.

Houston's Path-C novelty-integrity pushback (2026-04-19) raised the question: **is the anomaly population stable, or is it an overfit artifact of this particular 47K training sample?** A 5-fold out-of-sample validation is the cleanest answer — train 5 independent models on disjoint folds, score the full DR1 catalog with each, and measure how reproducible the top-1% anomaly set is across folds.

If overlap is high (Jaccard ≥ 0.70 at top-1%), the proxy models produce stable rankings across fold-dependent training sets. Because every model scores the full pool, this is not by itself a fully out-of-sample catalog validation. If overlap is low, the paper needs to reframe the DESI numbers as strongly training-sample-conditioned.

## Concrete protocol

1. **Fold construction.** Take the existing 47K DESI training sample (same `target_ids.json` that the published BigAE was trained on so folds are directly comparable). Shuffle with `seed=20260420`. Split into 5 disjoint folds of ~9,400 spectra each.

2. **Fold training.** For each fold *f* ∈ {0, 1, 2, 3, 4}:
   - Train set: the other 4 folds (~37,600 spectra) with 90/10 train/val split *inside* those 4 folds
   - Holdout: fold *f* (~9,400 spectra) — untouched during training, used *only* for holdout-score reporting
   - Architecture: `BigAE(n_in=496, n_lat=128)` — same as the published DESI BigAE (see `sdss_native_retrain.py` L77-92 for the reference implementation)
   - Optimizer: Adam, lr=1e-3, batch_size=512
   - Training schedule: up to 40 epochs, early-stop patience=5 on the *inside-90/10* val loss
   - Gate during training: val_loss ≤ 0.30 (same gate as SDSS/LAMOST native — comparable apples-to-apples)
   - Save: `outputs/desi_kfold/fold_{f}/best.pt` + `training_log.json`

3. **Scoring.** For each fold's saved model, score the full 22.5M DESI DR1 catalog using the existing inference infrastructure (`13_desi_dr1_gpu_inference.py` pattern, DataLoader num_workers=16 pin_memory=True). Output 5 parquet files, one per fold, each with columns (source_id, ra, dec, anomaly_score).

4. **Holdout report.** For each fold, compute holdout reconstruction MSE statistics (p50, p90, p99) to confirm the model generalizes cleanly *in-distribution*. A fold whose holdout p99 is >2× the inside-val p99 flags a distribution-shift artifact that would invalidate the fold.

5. **Top-1% stability analysis.** For each fold, take the top 1% anomalies (~225,000 rows). Cross-tabulate:
   - Pairwise Jaccard overlap matrix (5×5)
   - Consensus set: sources in the top-1% of ≥ 3 of 5 folds (majority-vote "robust DESI anomalies")
   - Singleton set: sources in exactly 1 fold (fold-specific noise)
   - Ratio |consensus|/|union| — the "anomaly-population stability" number

6. **Gate:** criterion #4 PASS iff mean pairwise Jaccard ≥ 0.70 at top-1%. Interpretation:
   - Jaccard ≥ 0.70 ⇒ DESI anomaly population is robust; Paper 3 Table 1 DESI number stands unchanged
   - 0.50 ≤ Jaccard < 0.70 ⇒ partial stability; Paper 3 reports Jaccard + consensus-set count as a robustness row
   - Jaccard < 0.50 ⇒ anomaly population is training-sample-conditioned; Paper 3 switches headline to the consensus-set count

## Compute budget

- 5 BigAE training runs @ ~30 min each on A100 → ~2.5 GPU-hours
- 5 inference passes over 22.5M DESI DR1 @ ~25 min each on A100 → ~2.1 GPU-hours
- Consensus + Jaccard analysis: <5 min local CPU
- **Total pod cost: ~5 GPU-hours × $1.19/hr = ~$6 on the current A100**
- Launches *after* SDSS + LAMOST native re-scores finish (ETA ~26 / 36 h from fire #117) so the three heavy jobs don't contend for GPU
- Cumulative Path-C budget after launch: ~$62 / $400 (well under cap)

## Deliverables

- `train_desi_kfold.py` — training driver (staged this fire)
- `score_desi_kfold.py` — inference driver (staged this fire)
- `aggregate_kfold.py` — Jaccard + consensus analysis (staged this fire)
- `outputs/desi_kfold/fold_{0-4}/best.pt` — 5 trained checkpoints (post-launch)
- `outputs/desi_kfold/fold_{0-4}_scores.parquet` — 5 full-catalog scores (post-launch)
- `outputs/desi_kfold/holdout_reports.json` — per-fold holdout stats (post-launch)
- `outputs/desi_kfold/kfold_stability_summary.json` — Jaccard matrix + consensus headline (post-launch)
- Paper 3 addition: new §3.1 paragraph citing the Jaccard, OR a §pathc_caveats (v) entry if the gate misses

## Path-C criterion #4 progress ledger

| Fire | Δ% | What landed |
|---|---|---|
| #117 | 0 → 20 | This plan doc + 3 scripts staged; launch-blocked on SDSS/LAMOST freeing GPU |
| future | 20 → 60 | 5 training runs complete + holdout stats landed |
| future | 60 → 90 | 5 inference passes complete + Jaccard matrix computed |
| future | 90 → 100 | Paper 3 §3.1 stability paragraph (or §pathc_caveats (v) entry) landed + PDF recompile |
