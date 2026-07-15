---
license: cc-by-4.0
language:
- en
pretty_name: "DESI Legacy Galaxy Chirality Catalog (8.47M)"
size_categories:
- 1M<n<10M
task_categories:
- image-classification
- tabular-classification
tags:
- astronomy
- galaxy-morphology
- chirality
- desi-legacy
- group-equivariance
configs:
- config_name: apjs_primary_safe
  data_files:
  - split: catalog
    path: "apjs-release/v1.0.244/p4_catalog_primary_safe_v1.0.244.parquet"
- config_name: spiral_morphology_dr8
  data_files:
  - split: spiral_morphology
    path: "spiral_morphology_dr8.parquet"
---

# DESI Legacy Galaxy Chirality Catalog

This dataset accompanies Paper 4 v1.0.251, *An Observed-Label Chirality-Dipole Null in 949,584 High-Confidence DESI Spirals and an 8.5-Million-Galaxy Catalog*.

The primary high-confidence observed-label statistic is consistent with zero under fixed-occupancy label randomization (`z=0.7053169638`, one-sided empirical-rank `p=0.2246775322`). This is not a calibrated true-spin, physical-amplitude, or primordial-parity bound.

## Authoritative release

Use `apjs-release/v1.0.244/`, pinned by data commit `db11023306ab4eed1d7727670bd78e127b7af17a` and provider-receipt commit `e535b26247c892971963be6029435544cf29d19b`.

| Product | Rows | Bytes | SHA-256 | Role |
|---|---:|---:|---|---|
| `p4_catalog_primary_safe_v1.0.244.parquet` | 8,474,531 | 386,712,994 | `139b761fbeafb34306a0cec60967226c18dc84295285f8317ce3d3af3d28bdf3` | Science-facing observed-label catalog |
| `p4_catalog_raw_flip_quarantine_v1.0.244.parquet` | 249,066 | 16,665,663 | `fb98787dd4c5d1a7a0fdb64fcdacd1b02bc2080ab3716c0a803e0ccdfec03fbe` | Unsafe raw/flip reconstruction quarantine; do not use for science weights |
| `primary_label_shuffle_amps_10000.npy` | 10,000 draws | 80,128 | `f6360f4bec22669097cee3e2fad8b176291d3ecbfbfbb9a9290d0bce3d5152c0` | Retained primary fixed-occupancy null |
| `pixel_permutation_amps_10000.npy` | 10,000 draws | 80,128 | `62bb1c019231974c2a7ed5d5e43ceb77a5596e4675c82d7ff1c899e029a36492` | Distinct robustness diagnostic |

The folder also contains the schema, manifest, SHA-256 ledger, validation receipt, and executable primary-null reproducer. The older root `catalog_production.parquet` is retained for provenance and contains raw-pass columns that are not calibrated probabilities; it is not the authoritative ApJS science product.

### Safe-catalog schema

| Column | Type | Meaning |
|---|---|---|
| `object_id` | string | DR8 compound identifier, `BRICKID_OBJID` |
| `ra_deg`, `dec_deg` | float64 | ICRS coordinates in degrees |
| `class_eq` | string | Equivariant hard observed label: `CW`, `CCW`, or `NOT_SPIRAL` |
| `score_cw_eq`, `score_ccw_eq`, `score_ns_eq` | float64 | Uncalibrated equivariant ranking scores |
| `score_eq_max` | float64 | Maximum equivariant ranking score; not calibrated confidence |
| `is_spiral` | bool | `class_eq` is `CW` or `CCW` |
| `primary_hc` | bool | Declared high-confidence spiral selection |
| `raw_flip_qc_unsafe` | bool | Row belongs to the separately quarantined raw/flip diagnostic set |

## Morphology companion and executable join

`spiral_morphology_dr8.parquet` is the existing public morphology companion for every one of the 3,201,160 released CW/CCW rows. It is 105,317,121 bytes with SHA-256 `d49090fce3033c5905df359f63036fd831c4b6378c271b95afd8d86a91bd5620`. Its `BRICKID_OBJID` keys are unique, non-null, and exactly cover the safe catalog's `is_spiral == True` object IDs.

The companion exposes raw DR8 morphology fields only: `BRICKID`, `OBJID`, `TYPE`, `FRACDEV`, `SHAPEDEV_R`, `SHAPEDEV_E1`, `SHAPEDEV_E2`, `SHAPEEXP_R`, `SHAPEEXP_E1`, and `SHAPEEXP_E2`. It does not contain a precomputed axial ratio.

The versioned machine-readable join contract, schema, and validator are under `apjs-release/v1.0.251-morphology-sidecar/`.

```python
import pandas as pd
from huggingface_hub import hf_hub_download

repo = "bamfai/galaxy-chirality-catalog"
safe = pd.read_parquet(hf_hub_download(
    repo,
    "apjs-release/v1.0.244/p4_catalog_primary_safe_v1.0.244.parquet",
    repo_type="dataset",
))
morph = pd.read_parquet(hf_hub_download(
    repo, "spiral_morphology_dr8.parquet", repo_type="dataset"
))
morph["object_id"] = morph["BRICKID"].astype(str) + "_" + morph["OBJID"].astype(str)

assert not morph["object_id"].duplicated().any()
spirals = safe.loc[safe["is_spiral"]].merge(
    morph, on="object_id", how="left", validate="one_to_one", indicator=True
)
assert len(spirals) == 3_201_160
assert spirals["_merge"].eq("both").all()
```

## Metadata not released

This release does **not** provide a full-catalog redshift, imaging-leg, depth, seeing, or PSF table. Those fields must not be inferred from the stale root README, which previously advertised columns absent from the Parquet files. A 145,789-row DESI-selection artifact used elsewhere in the project is selection-specific and is not a full-catalog redshift companion. Depth/PSF brick joins and imaging-leg rules remain unresolved publication work.

## Reproducibility and citation status

- Paper source and pipeline: <https://github.com/Hubify-Projects/bigbounce/tree/main/pipelines/p2_chirality>
- Exact current PDF: <https://bigbounce.hubify.app/papers/chirality_catalog_paper_v1.0.251.pdf>
- Machine-readable release contract: `apjs-release/v1.0.244/SCHEMA.json`
- Provider receipt: `apjs-release/v1.0.244/PROVIDER_RECEIPT.json`

No arXiv identifier or Zenodo DOI has been assigned yet. Cite the manuscript title, author, version v1.0.251, and the pinned data/provider commits above until those identifiers exist.

## License

Catalog data are CC BY 4.0. Underlying DESI Legacy Imaging Surveys imagery remains subject to the survey's terms.
