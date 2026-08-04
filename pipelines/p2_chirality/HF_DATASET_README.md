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

> **CURRENT PUBLICATION ALIGNMENT (2026-08-04).** The currently selected Paper
> 4 manuscript is v1.0.274. The public v1.0.244 payload remains intentionally
> immutable until Houston approves the final candidate; its version must not
> be mistaken for the paper version. After approval, provider metadata,
> strict-null overlays, archive bytes, and citations will be refreshed as one
> hash-bound release. See the
> [publication and release master map](../../project-context/PUBLICATION_AND_RELEASE_MASTER_MAP_2026-08-04.md).

This dataset accompanies the current Paper IV manuscript, *An Observed-Label Chirality-Dipole Null in 890,069 Quality-Controlled High-Confidence DESI Spirals and an 8.5-Million-Galaxy Catalog*.

The declared primary high-confidence observed-label statistic excludes every row marked `raw_flip_qc_unsafe` and is consistent with zero under fixed-occupancy label randomization (`N_selected=890069`, `N_support=887472`, `z_moment=0.6346508534`, one-sided add-one rank `p=0.2376762324`). This is not a calibrated true-spin, physical-amplitude, or primordial-parity bound.

## Authoritative release

The immutable catalog bytes remain `apjs-release/v1.0.244/`, pinned by data commit `db11023306ab4eed1d7727670bd78e127b7af17a` and provider-receipt commit `e535b26247c892971963be6029435544cf29d19b`. The synchronized strict-primary analysis contract is the repository release candidate `apjs_release_v1.0.259_strict/`; its intended provider path is `apjs-release/v1.0.259-strict-primary/`. Until that overlay is published and pinned by an immutable provider revision, the public provider release is incomplete for reproducing the manuscript's declared primary result.

| Product | Rows | Bytes | SHA-256 | Role |
|---|---:|---:|---|---|
| `p4_catalog_primary_safe_v1.0.244.parquet` | 8,474,531 | 386,712,994 | `139b761fbeafb34306a0cec60967226c18dc84295285f8317ce3d3af3d28bdf3` | Science-facing observed-label catalog |
| `p4_catalog_raw_flip_quarantine_v1.0.244.parquet` | 249,066 | 16,665,663 | `fb98787dd4c5d1a7a0fdb64fcdacd1b02bc2080ab3716c0a803e0ccdfec03fbe` | Unsafe raw/flip reconstruction quarantine; do not use for science weights |
| `primary_label_shuffle_amps_10000.npy` | 10,000 draws | 80,128 | `f6360f4bec22669097cee3e2fad8b176291d3ecbfbfbb9a9290d0bce3d5152c0` | Historical unsafe-inclusive fixed-occupancy null; not the current primary |
| `primary_strict_fixed_occupancy_amps_10000.npy` | 10,000 draws | 80,128 | `3a03ca4b008844fd8bf16be4e1e7e918ceaf580992d9462d54233f417e32ce7d` | Current strict-primary fixed-occupancy null; local release candidate pending immutable provider publication |
| `pixel_permutation_amps_10000.npy` | 10,000 draws | 80,128 | `62bb1c019231974c2a7ed5d5e43ceb77a5596e4675c82d7ff1c899e029a36492` | Distinct robustness diagnostic |

The v1.0.244 folder also contains the historical schema, manifest, SHA-256 ledger, validation receipt, and unsafe-inclusive reproducer. Catalog C remains the only published science-facing catalog product, but its current science-use predicate is `primary_hc & ~raw_flip_qc_unsafe`. The strict overlay supplies the synchronized schema, exact strict null array, and executable reproducer without duplicating the 386,712,994-byte catalog. The historical Catalog A (raw) and Catalog B (Platt-calibrated) labels describe pipeline diagnostics, not released catalog tiers; no complete Catalog B payload or executable release contract is claimed. The older root `catalog_production.parquet` is retained for provenance and contains raw-pass columns that are not calibrated probabilities; it is not the authoritative ApJS science product.

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

The current DR8 class totals are 1,592,107 CW and 1,609,053 CCW, totaling 3,201,160 chirality-relevant spirals.

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
    revision="db11023306ab4eed1d7727670bd78e127b7af17a",
))
morph = pd.read_parquet(hf_hub_download(
    repo,
    "spiral_morphology_dr8.parquet",
    repo_type="dataset",
    revision="245ad7c5f1e58c627be1390dc3125cd1ce1e3dc9",
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
- Current manuscript source: <https://github.com/Hubify-Projects/bigbounce/blob/main/pipelines/p2_chirality/chirality_catalog_paper.tex>
- Machine-readable release contract: `apjs-release/v1.0.244/SCHEMA.json`
- Direct immutable machine-readable manifest: <https://huggingface.co/datasets/bamfai/galaxy-chirality-catalog/resolve/db11023306ab4eed1d7727670bd78e127b7af17a/apjs-release/v1.0.244/MANIFEST.json>
- Provider receipt: `apjs-release/v1.0.244/PROVIDER_RECEIPT.json`

No arXiv identifier, Zenodo DOI, or immutable repository tag for the current Paper IV manuscript has been assigned. Cite the manuscript title, author, and the pinned data/provider commits above until those identifiers exist.

## License

Catalog data are CC BY 4.0. Underlying DESI Legacy Imaging Surveys imagery remains subject to the survey's terms.
