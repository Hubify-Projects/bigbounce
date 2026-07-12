---
license: cc-by-4.0
tags:
  - astronomy
  - anomaly-detection
  - autoencoder
  - multi-survey
  - cosmology
pretty_name: BigBounce Multi-Survey Autoencoder Anomaly Catalog (Paper 3)
---

# BigBounce — Multi-Survey Autoencoder Anomaly Catalog (Paper 3)

**Immutable reviewable release.** This dataset is the frozen, independently
runnable data product backing Golden (2026), Paper 3 — *A Multi-Survey
Autoencoder Anomaly Catalog*. It is released **CC-BY-4.0** and the exact
revision cited in the paper's Data Availability statement is pinned by commit
hash. Consumers should verify downloaded files against
[`RELEASE_MANIFEST.json`](./RELEASE_MANIFEST.json) (per-file SHA-256 + row
counts).

- **Paper versions:** v3.1.157 (PRD variant) / v3.1.157-apjs (ApJS variant)
- **Author:** Houston Golden &lt;houston@hubify.com&gt;
- **Code / model weights:** https://github.com/Hubify-Projects/bigbounce
- **Zenodo DOI:** minted at journal acceptance (optional citable-snapshot
  upgrade; the pinned HF revision is already immutable).

## Headline numbers (all reproducible from this release)

| Quantity | Value | Source |
|---|---|---|
| Validated catalog-grade subset | **268,519** | `scripts/reproduce_headline_dedup.py` (4-way 5″ dedup of DESI+SDSS+Planck+NEOWISE validated lists) |
| Validated point-source tier | 268,319 | as above |
| Headline set (inclusive, ACT-excluded) | 378,280 | `pathc_unique_objects.parquet`, rows with `survey_list` excluding `act_dr6` |
| Headline set (Gaia+eROSITA also excised) | **377,482** | `pathc_unique_objects.parquet`, rows excluding `act_dr6`/`gaia_dr3`/`erosita_dr1` |
| Multi-survey coincidence clusters | 637 | `pathc_multi_survey_matches.parquet` |

**Recompute 377,482:** load `pathc_unique_objects.parquet` (378,480 rows) and
count rows whose `survey_list` contains none of `act_dr6`, `gaia_dr3`,
`erosita_dr1` → 377,482. Excise only `act_dr6` → 378,280 inclusive.

**Recompute 268,519:** run `scripts/reproduce_headline_dedup.py` (in the
companion GitHub repo) against the released validated per-survey tables.

## Contents & schema

### Merged catalog
- `pathc_unique_objects.parquet` — **378,480** unique objects (8-way 5″
  positional dedup). Columns: `cluster_id, n_detections, n_surveys,
  survey_list, ra_mean, dec_mean, best_score, member_ids, best_survey`. The
  `survey_list` column is authoritative for tier derivation (see headline
  table above).
- `pathc_multi_survey_matches.parquet` — **637** multi-survey coincidence
  clusters (canonical, ACT-excluded).

### Per-survey native-retrained blocks
- `desi_dr1_anomalies.parquet` — **195,829** (canonical-S per-object scores).
- `sdss_dr18_pathc_native.parquet` — **77,905** continuity slice (canonical-S).
- `planck_cmb_anomalies.parquet` — **200** patches (ranked by raw per-patch
  reconstruction MSE; survey-specific axis, **NOT** canonical-S).
- `neowise_anomalies.parquet` — **436** raw (419 survive the 80° ecliptic-pole
  mask used in the headline dedup); canonical-S.

### Excluded / exploratory tiers (NOT in the 377,482 headline)
- `gaia_dr3_anomalies.parquet` — **500**, exploratory tier.
- `blocks/erosita_dr1/erosita_dr1_anomalies.parquet` — **298**, membership-list
  only. **`S_BigAE` axis is irreproducible** (could not be reconciled with the
  committed raw-score artifact on 16 monotone rescalings + 3 IsolationForest
  retrains). Use the n=298 membership list ranked by committed raw score;
  do **not** use `S_BigAE` as a continuous science axis.
- `act_dr6_anomalies.parquet` — **200**, quarantined cross-transfer diagnostic.

### Reproducibility / provenance
- `p3_compute_to_accept/` — `sixway_dedup.py`, `sixway_dedup_artifact.{csv,json}`,
  `held_out_rescore.py` + result — the six-way dedup + held-out rescore stack.
- `pta_real_kde_2026-05-01/` — NANOGrav 15-yr HD-correlated free-spectrum
  real-KDE emcee fit: `chain_real_freespec.npy` (320,000×2 chain, burn-in
  removed), `emcee_freespec.py`, `results.json`, `gamma_posterior.png`.
- `pathc_dedup_summary{,_no_act}.json` — dedup summaries.
- `r42_results/` — DESI OOD MSE + NANOGrav Bayesian JSON.
- `cutouts/` — 827 top-anomaly image cutouts (128px).

## Per-survey score-schema flags

Not every block carries the same score schema. Check before treating any score
column as a continuous cross-survey axis:

| Survey | score_axis | membership_only |
|---|---|---|
| DESI DR1 | canonical-S | no |
| SDSS DR18 | canonical-S (native rescale) | no |
| NEOWISE | canonical-S (post ecliptic-pole mask) | no |
| Gaia DR3 | canonical-S (feature-space) | no (exploratory) |
| Planck CMB | raw per-patch reconstruction MSE | no |
| eROSITA DR1 | NONE — `S_BigAE` irreproducible | **yes** |

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

## Citation

Golden, H. 2026, *A Multi-Survey Autoencoder Anomaly Catalog*, Paper 3
(in preparation). Dataset: https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog
Code: https://github.com/Hubify-Projects/bigbounce
