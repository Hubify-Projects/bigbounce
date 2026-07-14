# Data Release Manifest — BigBounce Multi-Survey Anomaly Catalog
## Paper: Golden (2026), "A Multi-Survey Autoencoder Anomaly-Candidate Catalog: 268,319 Validated Point Sources plus 200 Archival CMB Map Patches" (Paper 3)
## Frozen: 2026-07-12 (immutable reviewable release, v3.1.157)
## Review-of-record paper: v3.1.161-apjs (local venue-fit source; no new HF tag uploaded)
## Status: PUBLIC + IMMUTABLE. Released CC-BY-4.0 on HuggingFace and pinned by commit hash.
## HuggingFace: https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog
## PINNED REVISION (immutable pointer cited in the paper): 573b5da7c75e4d33ab260bb5b0d57a2af0e15b23 (immutable git tag p3-v3.1.157)
## Inventory note: the frozen tag contains 25 files. The locally corrected RELEASE_MANIFEST.json has 27 entries because it also records two post-tag DP3-15 audit artifacts; it is not byte-identical to the tag's older manifest.
## Submission warning: the pinned tag is immutable but is not sufficient for a complete six-survey row-level package; native Planck and per-object LAMOST products are absent. The scoped ApJS table bundle was downloaded and verified locally on 2026-07-14; its exact audit record is `apjs_submission_v3.1.161/SUBMISSION_BUNDLE_MANIFEST.json`.

---

## Released Catalog Files — authoritative list is RELEASE_MANIFEST.json

The 25-file manifest inside tag `p3-v3.1.157` is authoritative for byte-level inventory and checksums at that immutable revision. The local `RELEASE_MANIFEST.json` is a corrected audit record: it fixes interpretation and tag identity and adds two post-tag DP3-15 entries, so it must not be represented as byte-identical to the tagged file.

The released parquet catalog files (as verified against the pinned revision on 2026-07-12) and their row counts:

Count interpretation after the M44 audit:

- **268,319** — validated point-source science product (DESI + SDSS + geometry-gated NEOWISE, 5-arcsec dedup).
- **268,519** — the validated point-source product plus 200 non-overlapping archival Planck cross-transfer rows; continuity count, not uniformly validated.
- **377,482** — 377,282 point-source continuity rows (including exploratory LAMOST aggregate membership) plus the same 200 archival Planck rows.

| File | Rows | SHA-256 (abbrev.) | Tier |
|------|------|-------------------|------|
| pathc_unique_objects.parquet | 378,480 | b14deb02…6138c643 | merged 8-way dedup (headline 377,482 = minus act/gaia/erosita; 378,280 = minus ACT only) |
| pathc_multi_survey_matches.parquet | 637 | 3605b16a…c85e784 | multi-survey coincidence clusters (ACT-excluded, canonical) |
| desi_dr1_anomalies.parquet | 195,829 | 0a36b8d6…f103ec65 | validated (canonical-S) |
| sdss_dr18_pathc_native.parquet | 77,905 | 5139c663…b78a31e6 | validated continuity slice (canonical-S) |
| planck_cmb_anomalies.parquet | 200 | 9dd3576f…b05a92740 | **archival cross-transfer baseline; NOT native top-200** |
| neowise_anomalies.parquet | 436 | 2740d936…6aac42da | validated raw (419 survive the 80° ecliptic-pole mask) |
| gaia_dr3_anomalies.parquet | 500 | 819c5978…7396ced | **quarantined synthetic placeholder; present but excluded from every count** |
| blocks/erosita_dr1/erosita_dr1_anomalies.parquet | 298 | 4ea1b032…4d082d2de | membership-only addendum (EXCLUDED; S_BigAE irreproducible — see warning) |
| act_dr6_anomalies.parquet | 200 | 65fa89af…e47cde72 | quarantined cross-transfer diagnostic (EXCLUDED) |

**NOT released as per-object tables (documented in the paper, deliberately not in the release):**
`lamost_dr10_pathc_native` (LAMOST DR10 is a failed-exploratory tier included only in aggregate/dedup continuity accounting, but no per-object LAMOST table is released), the native Planck top-200/checkpoint/tensor/full-score bank, and superseded staging variants (`*_no_act`, `cmb_native_anomalies`, `neowise_pathc_masked`).

Reproducibility / provenance files also released (see RELEASE_MANIFEST.json for full SHA-256 + sizes): `scripts/`-side dedup + held-out rescore (`p3_compute_to_accept/`), dedup summaries, and top-anomaly cutouts. The frozen tag also contains a legacy PTA chain/fitter, but v3.1.161 removes that cosmology demonstration and the PTA files are not part of the ApJS submission package.

---

## ApJS Machine-Readable Table Inventory — Locally Verified

All six files below were downloaded directly from immutable revision
`573b5da7c75e4d33ab260bb5b0d57a2af0e15b23` into the gitignored
`apjs_submission_v3.1.161/` directory. Their SHA-256 values, byte sizes, Parquet
row counts, and schemas match the tracked
`SUBMISSION_BUNDLE_MANIFEST.json`. At submission, attach the exact files with
units, null conventions, score definitions, selection rules, and provenance in
the machine-readable-table metadata. Do not describe the frozen tag as filling
the missing native Planck or LAMOST row-level products.

| Role | Exact file | Rows | Exact columns / schema boundary |
|---|---|---:|---|
| Validated DESI point sources | `desi_dr1_anomalies.parquet` | 195,829 | `tid, ra, dec, score, worst, rB, rR, rZ` |
| Validated SDSS continuity slice | `sdss_dr18_pathc_native.parquet` | 77,905 | `plate, mjd, fiberid, ra, dec, z, class, anomaly_score`; fixed-size continuity slice, not a uniform threshold |
| Geometry-gated NEOWISE | `neowise_anomalies.parquet` | 436 raw / 419 retained | `source_id, ra, dec, n_epochs, time_span`, W1/W2 variability features, `anomaly_score`; include the ecliptic-mask flag/definition |
| Merged continuity table | `pathc_unique_objects.parquet` | 378,480 | `cluster_id, n_detections, n_surveys, survey_list, ra_mean, dec_mean, best_score, member_ids, best_survey`; heterogeneous tiers must remain identifiable |
| Cross-survey coincidences | `pathc_multi_survey_matches.parquet` | 637 | same merged schema; 5-arcsec union, ACT excluded |
| Archival CMB diagnostic | `planck_cmb_anomalies.parquet` | 200 | `patch_idx, ra, dec, anomaly_score`; label as cross-transfer, not native |

The 298-row eROSITA membership list is an optional diagnostic MTR with an
explicit non-comparable-score warning. The synthetic Gaia and quarantined ACT
tables are provenance exhibits only. No LAMOST per-object or native Planck MTR
can be included unless those products are independently recovered and audited.

---

## eROSITA Score-Axis Warning

The `S_BigAE` column in `erosita_dr1_anomalies.parquet` carries scores from the production run
whose axis (threshold 0.259) could NOT be reconciled with the committed raw-score artifact on any
of 16 monotone rescalings + 3 IsolationForest retrains (Spearman ρ = −0.10 in top-5, ruling out
the entire monotone class). **Do not use S_BigAE as a continuous science data product.**
The committed, reproducible eROSITA selection is the **n=298 membership list** (ranked by the
committed raw score, minimum released score = rank-298 raw threshold 3.4119).
Audit artifact: `r24conf_erosita_axis_sweep.json`.

---

## Per-Survey Score-Schema Flags (score_axis / membership_only)

Not every released block carries the same score schema. Downstream consumers MUST check
this table before treating any score column as a continuous, cross-survey-comparable axis
(added at v3.1.91 per EXT2 NB1; the paper's Data Availability statement points here):

| Survey block | score_axis | membership_only | Notes |
|---|---|---|---|
| DESI DR1 | canonical-S (Eq. score, DESI-trained BigAE) | no | per-object scores released |
| SDSS DR18 native | canonical-S (native rescale; continuity slice S ≥ 0.1060) | no | per-object scores released |
| LAMOST DR10 native | canonical-S (native rescale; top-1% slice S ≥ 0.4613) | n/a | failed-exploratory; **NOT released as a per-object table**; enters aggregate 377,282 point-source continuity count only |
| Gaia DR3 | INVALID synthetic-placeholder axis | n/a | quarantined historical file; excluded from every count and science use |
| NEOWISE | canonical-S (post ecliptic-pole mask) | no | per-object scores released |
| Planck CMB released | cross-transfer reconstruction score | no | 200 archival rows from patch_idx < 20,000; **not the unavailable native 200k-bank top-200** |
| eROSITA DR1 | NONE — S_BigAE axis irreproducible (see warning above) | **yes** | n=298 membership list only; ranked by committed raw score |

---

## Gaia DR3 quarantine

Do not interpret `gaia_dr3_anomalies.parquet` as Gaia DR3 data. The provenance audit identifies it as the synthetic fallback generated by `gaia_expanded.py`; its sequential fallback identifiers, duplicates, and nonphysical magnitudes are incompatible with a real Gaia catalog. The file remains only because the immutable tag cannot be rewritten. It is excluded from every reported count and should be ignored by downstream users.

---

## DESI DR1 Anomaly Files

DESI DR1 native-retrained anomalies (195,829 objects) ARE included in the release as
`desi_dr1_anomalies.parquet` (10.5 MB; SHA-256 `0a36b8d6…f103ec65`) at the pinned revision.
The \BigAE{} model weights and training code are in the companion GitHub repository:
https://github.com/Hubify-Projects/bigbounce

---

## Reproducibility Notes

- All .parquet files use pandas/pyarrow schema; schema documented in companion-repo README.md.
- The 7-way dedup was run with `pathc_positional_dedup.py` (deterministic, archived at same repo).
- Legacy PTA chain remains in the frozen inventory for provenance but is outside the v3.1.161 paper and submission package.
- Checksums (SHA-256) for the released files were recomputed against the pinned HuggingFace revision `573b5da7c75e4d33ab260bb5b0d57a2af0e15b23 (immutable git tag p3-v3.1.157)` on 2026-07-12 and frozen into `RELEASE_MANIFEST.json` (`manifest_frozen_utc`). The abbreviated hashes in the table above are drawn from that frozen JSON; use the JSON for full-length values.
