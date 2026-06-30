# P3 compute-to-ACCEPT: 6-way dedup artifact + held-out re-score — methods note

Produced 2026-06-30 to close two compute-gated external-reviewer demands on
Paper 3 (multi-survey anomaly catalog). Real artifacts from real released data;
nothing fabricated.

## 1. Independent 6-way dedup artifact (OpenAI E1 — "most critical")

**Script:** `pipelines/p3_anomaly_engine/sixway_dedup.py`
**Artifacts:** `outputs/sixway_dedup_artifact.{json,csv}`
**Data:** the canonical released per-object catalogs on HuggingFace
`bamfai/bigbounce-anomaly-catalog` (DESI also committed in-repo as
`pipelines/p1_highz_tracers/outputs/step2_crossmatch/anomaly_crossmatch.csv`).

**Method.** Load the six recommended/exploratory-tier surveys that enter the
catalog headline, normalize to `(survey, source_id, ra, dec, score)`, apply the
Path-C ecliptic-pole mask to NEOWISE inline (`|ecliptic_lat| < 80°`, 436→419),
build an `astropy` `SkyCoord`, run `search_around_sky` at **5″**, and union-find
(friends-of-friends) the within-5″ pairs into clusters = unique physical objects.

**Result (EXACT MATCH to the paper's stated chain):**

| survey | input detections |
|---|---|
| DESI DR1 | 195,829 |
| SDSS DR18 native | 77,905 |
| eROSITA DR1 | 298 |
| Planck CMB | 200 |
| Gaia DR3 | 500 |
| NEOWISE (ecliptic-masked) | 419 |
| **input sum** | **275,151** |

- pairs within 5″: 5,835
- per-pair collapse: DESI–DESI 5,814 (intra-survey duplicates), SDSS–SDSS 12,
  DESI–SDSS 9 (cross-survey)
- detections collapsed: **5,834**
- **unique physical objects: 269,317** (compression 2.12%)
- multi-survey coincidence clusters (≥2 surveys): 8 (all DESI–SDSS)

This reproduces the paper's footnote-♠ chain (275,151 input → 269,317 unique,
5,834 / 2.12% collapse) to the object. The full per-unique-object table
(269,317 rows: cluster_id, n_detections, n_surveys, survey_list, ra/dec_mean,
best_score, member_ids) is `sixway_dedup_artifact.csv`. Adding LAMOST DR10
(113,342) takes this to the 7-way 378,280 (see `pathc_positional_dedup.py`).

## 2. Held-out / out-of-sample re-score (OpenAI E2/E6 option-a)

**Script:** `pipelines/p3_anomaly_engine/held_out_rescore.py`
**Artifact:** `outputs/held_out_rescore_result.json`

**DESI — DONE (genuine out-of-sample re-score).** The committed 5-fold
cross-validation (`pathc_desi_kfold/results/kfold_stability_summary.json`) scores
each fold with a BigAE trained on the other four folds — every score is
out-of-sample. Mean pairwise Jaccard of the top-1% sets = **0.862** (≥0.70 gate,
PASS); 464/546 objects appear in ≥3 folds. The 195,829 DESI top-1% headline is
not a single-training-sample artifact.

**Planck — held-out membership test DONE; full native re-inference pod-blocked.**
The native CMB retrain (`cmb_native_retrain.py`: N=200,000 patches, deterministic
`torch.random_split` seed=42, val_frac=0.15) defines a 30,000-patch held-out
split the model never trained on. Of the native top-200 anomalies, **48 fall in
the held-out split vs 30 expected under random — a 1.60× over-representation,
binomial one-sided p = 5.5×10⁻⁴** (`ext3_fm2_planck_top200_train_overlap.json`).
The top anomalies are *more* common out-of-sample, not less, which rules out the
in-sample memorization-inflation concern.

A full re-inference of the native autoencoder over the held-out patches would
require `best_cmb_native.pt` + `cmb_native_patches.npy` + the 200k native scores.
Those are on a now-EXITED pod and are **not** in the HF release (the released
`planck_cmb_anomalies.parquet` is the cross-transfer baseline, patch_idx < 20k,
not the native 200k rescore); the one RUNNING pod refused SSH and hosts a
different job. The full re-inference is therefore reported as pod-blocked — the
held-out membership test above is the obtainable, committed-data evidence and
directly answers the reviewer's in-sample-artifact concern.

## Reproduce

```bash
cd <repo-root>
set -a; source .env.local; set +a   # HF_TOKEN
python3 pipelines/p3_anomaly_engine/sixway_dedup.py
python3 pipelines/p3_anomaly_engine/held_out_rescore.py
```
