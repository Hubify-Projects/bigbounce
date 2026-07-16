# P4 ApJS release-candidate schema (v1.0.244)

This is the immutable **catalog payload v1.0.244** contract bound to the
**P4 paper v1.0.245** closure. The payload filenames remain v1.0.244 because
the paper-only closure does not alter any catalog row or column.

This document is the human-readable data dictionary for the local P4 ApJS
release candidate. The executable contract is
`apjs_release_schema_v1_0_244.json`; the builder and validation tests are
`build_apjs_release_v1_0_244.py` and
`tests/test_apjs_release_v1_0_244.py`.

The current source catalog contains 8,474,531 DESI Legacy DR8 objects. Its
equivariant scores are **uncalibrated ranking scores, not probabilities**. The
paper's primary result consumes hard `class_eq` labels. No release field supports
a physical-amplitude bound, primordial-parity bound, matched-external-estimator
comparison, or formal-preregistration claim.

## Products and gates

| Product | Rows | Purpose | Science policy |
|---|---:|---|---|
| `p4_catalog_primary_safe_v1.0.244.parquet` | 8,474,531 | Science-facing observed-label catalog | Raw-pass and reconstructed flip-pass columns absent by construction |
| `p4_catalog_raw_flip_quarantine_v1.0.244.parquet` | 249,066 | Provenance-only quarantine of every catalog-wide bound violator | `do_not_use_for_science=True`; scores are uncalibrated |
| `primary_label_shuffle_amps_10000.npy` | 10,000 draws | Historical unsafe-inclusive fixed-occupancy galaxy-label randomization | Superseded primary contract; provenance only |
| `apjs_release_v1.0.259_strict/primary_strict_fixed_occupancy_amps_10000.npy` | 10,000 draws | Exact strict fixed-occupancy galaxy-label randomization; global strict-sample CW total preserved | Current primary descriptive observed-label null |
| `pixel_permutation_amps_10000.npy` | 10,000 draws | Exact retained pixel-asymmetry permutation | Robustness diagnostic only; not primary |

Exactly 59,515 of the 249,066 catalog-wide quarantined rows fall inside the
949,584-row primary HC selection. Thus the strict HC diagnostic contains
890,069 rows. The all-catalog and HC counts must not be conflated.

The local split, schema, row counts, and checksums are fail-closed gates. An
immutable public archive/DOI and human ApJS editorial review remain **OPEN**.
The generated Parquet files are local/ignored release payloads and are not
committed to GitHub.

## Science-facing columns

| Column | Type | Definition |
|---|---|---|
| `object_id` | string | Galaxy Zoo DESI / DR8 identifier |
| `ra_deg` | float64 | ICRS right ascension in degrees |
| `dec_deg` | float64 | ICRS declination in degrees |
| `class_eq` | string | Equivariant hard argmax label: `CW`, `CCW`, or `NOT_SPIRAL` |
| `score_cw_eq` | float64 | Uncalibrated CW ranking score |
| `score_ccw_eq` | float64 | Uncalibrated CCW ranking score |
| `score_ns_eq` | float64 | Uncalibrated non-spiral ranking score |
| `score_eq_max` | float64 | Maximum uncalibrated equivariant ranking score |
| `is_spiral` | bool | `class_eq in {CW, CCW}` |
| `primary_hc` | bool | Spiral hard label and `max(score_cw_eq, score_ccw_eq) > 0.6` |
| `raw_flip_qc_unsafe` | bool | Reconstructed raw/flip diagnostic exits `[0,1]` by more than `1e-3` |

The science-facing file contains no raw-pass score, reconstructed flip-pass
score, calibrated-confidence, or calibrated-probability field.

## Quarantine columns

The quarantine retains object ID, coordinates, primary-HC membership, raw-source
leg, the three raw diagnostic scores, the three reconstructed flip diagnostic
scores, maximum bound excursion, reason code, and a mandatory
`do_not_use_for_science` flag. Every row has reason code
`RAW_EQ_PIPELINE_PASS_MISMATCH_GT_1E3`.

The quarantine exists so the mismatch is auditable. Its score columns must never
be used as probabilities, likelihood weights, or calibrated classifier outputs.

## Safe filters

Current primary observed-label reproduction:

```python
primary = catalog[catalog.primary_hc & ~catalog.raw_flip_qc_unsafe]
```

Historical unsafe-inclusive selection:

```python
historical_inclusive = catalog[catalog.primary_hc]
```

The declared primary result uses the first filter. Its exact null was regenerated
under that selection and is retained in `apjs_release_v1.0.259_strict/`. The
second filter is preserved only to reproduce the earlier public release history;
it must not be described as the current primary analysis.

## Named HEALPix supports

| Stable name | Exact support | Pixels | Role |
|---|---|---:|---|
| `HC_REALSPACE_STRICT` | Primary HC rows excluding every `raw_flip_qc_unsafe` row; `N_spiral(pixel) >= 10` | 23,633 | Current primary real-space observed-label null |
| `HC_REALSPACE_INCLUSIVE` | Historical primary HC rows; `N_spiral(pixel) >= 10` | 23,682 | Superseded unsafe-inclusive provenance |
| `FULL_SPIRAL_CANONICAL` | All equivariant spiral labels; `N_spiral(pixel) >= 10` | 24,087 | Full-sample WLS and canonical harmonic diagnostics |
| `MASTER_ALL_GALAXY_FOOTPRINT` | `N_all(pixel) >= 1` | 24,297 | Apodized, weighted MASTER diagnostic |

These supports are distinct. “Canonical mask” without the stable name is
deprecated because it previously obscured the 23,682-versus-24,087 distinction.

## Minimal reproduction

After building the local release candidate:

```bash
python3 pipelines/p2_chirality/reproduce_p4_primary_null_v1_0_244.py \
  --output pipelines/p2_chirality/apjs_release_v1.0.244/PRIMARY_REPRODUCTION.json
```

The current hard gates are `N_selected=890,069`, `N_support=887,472`,
23,633 strict pixels, `A_dip=0.0046651988`, `z_moment=+0.6346509`, and
one-sided add-one upper-tail rank `p=0.2376762`. The strict fixed-occupancy
array is pinned by SHA-256
`3a03ca4b008844fd8bf16be4e1e7e918ceaf580992d9462d54233f417e32ce7d`.
The unsafe-inclusive fixed-occupancy and pixel-permutation arrays remain
separately checksummed as historical and robustness diagnostics. The script
makes no physical or primordial inference.

## Provenance

The source blob is pinned to upstream revision
`a21eb596fd10edb9af9e7a1bcefb04f87327a724`, 952,115,239 bytes, 8,474,531
rows, and SHA-256
`e8525ba5c98576f6361580e4a0aa7a86929ccc9f79b1423808774cfaaf313563`.
The builder validates the committed exact-SHA receipt plus current byte and
Parquet-row counts before its single streaming catalog pass.
