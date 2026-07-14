---
license: cc-by-4.0
tags:
  - astronomy
  - anomaly-detection
  - autoencoder
  - multi-survey
pretty_name: BigBounce Multi-Survey Autoencoder Anomaly Catalog (Paper 3)
---

# BigBounce — Multi-Survey Autoencoder Anomaly Catalog (Paper 3)

**Corrected release description.** This dataset backs Golden (2026), Paper 3 —
*A Multi-Survey Autoencoder Anomaly-Candidate Catalog*. It is released
**CC-BY-4.0**. The corrected submission release is frozen at the immutable tag
`p3-v3.1.161`. The frozen inventory is heterogeneous and
is not a complete six-survey, independently rerunnable per-object product.
Consumers should verify downloaded files against
[`RELEASE_MANIFEST.json`](./RELEASE_MANIFEST.json) (per-file SHA-256 + row
counts) and observe the provenance restrictions below.

- **Paper versions:** v3.1.157 (deprecated PRD development variant) / v3.1.161-apjs (review-of-record)
- **Author:** Houston Golden &lt;houston@hubify.com&gt;
- **Code / model weights:** https://github.com/Hubify-Projects/bigbounce
- **Release state:** the corrected manifest, README, machine-readable-table
  manifest, and revised provenance audit files are published at
  `p3-v3.1.161`. This is not a complete six-survey row-level submission package:
  native Planck and per-object LAMOST products remain absent.

## Count interpretation

| Quantity | Value | Source |
|---|---|---|
| Validated point-source science product | **268,319** | DESI + SDSS + geometry-gated NEOWISE after 5″ dedup |
| Point sources + archival Planck continuity count | **268,519** | `scripts/reproduce_headline_dedup.py`; appends 200 non-overlapping released Planck cross-transfer rows |
| Inclusive continuity set (ACT-excluded) | 378,280 | `pathc_unique_objects.parquet`, rows with `survey_list` excluding `act_dr6`; includes quarantined Gaia and membership-only eROSITA |
| Filtered continuity set | **377,482** | 377,282 point-source continuity rows (including failed-exploratory LAMOST aggregate membership) + 200 archival Planck rows; excludes ACT/Gaia/eROSITA |
| Multi-survey coincidence clusters | 637 | `pathc_multi_survey_matches.parquet` |

**Recompute 377,482:** load `pathc_unique_objects.parquet` (378,480 rows) and
count rows whose `survey_list` contains none of `act_dr6`, `gaia_dr3`,
`erosita_dr1` → 377,482. Excise only `act_dr6` → 378,280 inclusive.

**Recompute 268,519:** run `scripts/reproduce_headline_dedup.py` (in the
companion GitHub repo) against DESI, SDSS, NEOWISE, and the released Planck
file. The script returns 268,519 because it appends 200 archival Planck map
patches with no point-source overlaps. Subtract those 200 rows to obtain the
validated 268,319 point-source product.

## Contents & schema

### Merged catalog
- `pathc_unique_objects.parquet` — **378,480** unique objects (8-way 5″
  positional dedup). Columns: `cluster_id, n_detections, n_surveys,
  survey_list, ra_mean, dec_mean, best_score, member_ids, best_survey`. The
  `survey_list` column is authoritative for tier derivation (see count
  table above).
- `pathc_multi_survey_matches.parquet` — **637** multi-survey coincidence
  clusters (canonical, ACT-excluded).

### Released per-survey blocks
- `desi_dr1_anomalies.parquet` — **195,829** (canonical-S per-object scores).
- `sdss_dr18_pathc_native.parquet` — **77,905** continuity slice (canonical-S).
- `planck_cmb_anomalies.parquet` — **200** patches from the original
  20,000-patch **cross-transfer** scan (`patch_idx < 20,000`; observed released
  score range 0.306–62.999). This is an archival diagnostic, **not** the native
  200,000-patch top-200 and not a validated CMB science tier.
- `neowise_anomalies.parquet` — **436** raw (419 survive the 80° ecliptic-pole
  mask used in the headline dedup); canonical-S.

### Excluded / quarantined tiers (NOT in the 377,482 continuity count)
- `gaia_dr3_anomalies.parquet` — **500**, quarantined synthetic-placeholder
  fallback from `gaia_expanded.py`, not real Gaia DR3 data. Exclude from all
  counts and science use.
- `blocks/erosita_dr1/erosita_dr1_anomalies.parquet` — **298**, membership-list
  only. **`S_BigAE` axis is irreproducible** (could not be reconciled with the
  committed raw-score artifact on 16 monotone rescalings + 3 IsolationForest
  retrains). Use the n=298 membership list ranked by committed raw score;
  do **not** use `S_BigAE` as a continuous science axis.
- `act_dr6_anomalies.parquet` — **200**, quarantined cross-transfer diagnostic.

### Products not released per object

- **LAMOST DR10:** no per-object table is present. Its failed-exploratory
  contribution appears only in aggregate/dedup continuity accounting, so the
  377,282 point-source continuity set cannot be reconstructed from a released
  LAMOST per-survey table.
- **Native Planck:** the native 200,000-patch top-200 table, checkpoint, input
  tensor, and full score bank are absent. Native-run summary artifacts support
  the analysis-level validation, but no native row-level product is public.

## ApJS machine-readable submission package (v3.1.161 verified local bundle)

The six scoped tables below were downloaded from the immutable revision into
`apjs_submission_v3.1.161/` and verified on 2026-07-14 against their Parquet
metadata and frozen SHA-256 values. The tracked
`apjs_submission_v3.1.161/SUBMISSION_BUNDLE_MANIFEST.json` records exact byte
sizes, rows, schemas, hashes, roles, and exclusions. The Parquet payloads are
gitignored; the immutable tag remains their public source. At journal
submission, attach these files with units, null conventions, score definitions,
selection tier, and provenance metadata.

| Submission role | Exact file | Rows | Required column metadata |
|---|---|---:|---|
| Validated DESI point sources | `desi_dr1_anomalies.parquet` | 195,829 | `tid`, `ra`, `dec`, `score`, `worst`, `rB`, `rR`, `rZ` |
| Validated SDSS continuity slice | `sdss_dr18_pathc_native.parquet` | 77,905 | `plate`, `mjd`, `fiberid`, `ra`, `dec`, `z`, `class`, `anomaly_score`; state the fixed-size continuity selection |
| Geometry-gated NEOWISE sources | `neowise_anomalies.parquet` | 436 raw / 419 retained | `source_id`, coordinates, epoch/time-span fields, W1/W2 variability features, `anomaly_score`; state the ecliptic mask |
| Merged continuity catalog | `pathc_unique_objects.parquet` | 378,480 | `cluster_id`, `n_detections`, `n_surveys`, `survey_list`, `ra_mean`, `dec_mean`, `best_score`, `member_ids`, `best_survey`; carry tier/quarantine interpretation from this README |
| Cross-survey coincidences | `pathc_multi_survey_matches.parquet` | 637 | same merged schema; define the 5-arcsec union and ACT exclusion |
| Archival CMB diagnostic | `planck_cmb_anomalies.parquet` | 200 | `patch_idx`, `ra`, `dec`, `anomaly_score`; label cross-transfer and non-native in table title and metadata |

The eROSITA 298-row membership list may accompany the submission only as a
clearly labeled diagnostic table with its `anomaly_score` non-comparability
warning. The synthetic Gaia and quarantined ACT tables are provenance exhibits,
not science tables. No submission metadata may imply that the absent LAMOST
per-object or native Planck products are present.

### Reproducibility / provenance
- `p3_compute_to_accept/` — `sixway_dedup.py`, `sixway_dedup_artifact.{csv,json}`,
  `held_out_rescore.py` + result — the six-way dedup + held-out rescore stack.
- `pta_real_kde_2026-05-01/` — legacy out-of-scope artifact retained in the
  frozen inventory; it is not part of the v3.1.161 ApJS paper or submission
  table package.
- `pathc_dedup_summary{,_no_act}.json` — dedup summaries.
- `r42_results/` — DESI OOD MSE plus legacy out-of-scope Bayesian JSON.
- `cutouts/` — 827 top-anomaly image cutouts (128px).

## Per-survey score-schema flags

Not every block carries the same score schema. Check before treating any score
column as a continuous cross-survey axis:

| Survey | score_axis | membership_only |
|---|---|---|
| DESI DR1 | canonical-S | no |
| SDSS DR18 | canonical-S (native rescale) | no |
| NEOWISE | canonical-S (post ecliptic-pole mask) | no |
| Gaia DR3 | INVALID synthetic-placeholder axis | n/a — quarantined |
| Planck CMB released | cross-transfer reconstruction score | no — archival diagnostic |
| eROSITA DR1 | NONE — `S_BigAE` irreproducible | **yes** |

LAMOST has no released per-object block. The unavailable native Planck run must
not be inferred from the released cross-transfer Planck rows.

## Verification

```python
import pandas as pd, hashlib, json
m = json.load(open("RELEASE_MANIFEST.json"))
for f in m["files"]:
    got = hashlib.sha256(open(f["path"], "rb").read()).hexdigest()
    assert got == f["sha256"], f["path"]
d = pd.read_parquet("pathc_unique_objects.parquet")
excl = {"act_dr6", "gaia_dr3", "erosita_dr1"}
headline = d[d.survey_list.apply(lambda s: not (set(s) & excl))]
assert len(headline) == 377482
```

This verifies the filtered **continuity** count, not a uniformly validated
catalog. It does not supply the missing LAMOST per-object table or native
Planck row-level artifacts.

## Citation

Golden, H. 2026, *A Multi-Survey Autoencoder Anomaly-Candidate Catalog*, Paper 3
(in preparation). Dataset: https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog
Code: https://github.com/Hubify-Projects/bigbounce
