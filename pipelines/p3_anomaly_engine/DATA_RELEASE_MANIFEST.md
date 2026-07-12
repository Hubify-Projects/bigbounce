# Data Release Manifest — BigBounce Multi-Survey Anomaly Catalog
## Paper: Golden (2026), "A Multi-Survey Autoencoder Anomaly Catalog: 268,519 Validated Sources from a Native-Trained Scan of 37.3 Million Spectra and Map Patches" (Paper 3)
## Frozen: 2026-07-12 (immutable reviewable release, v3.1.157)
## Status: PUBLIC + IMMUTABLE. Released CC-BY-4.0 on HuggingFace and pinned by commit hash.
## HuggingFace: https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog
## PINNED REVISION (immutable pointer cited in the paper): 573b5da7c75e4d33ab260bb5b0d57a2af0e15b23 (immutable git tag p3-v3.1.157)
## Authoritative machine-readable manifest: RELEASE_MANIFEST.json (in the HF repo AND pipelines/p3_anomaly_engine/RELEASE_MANIFEST.json) — 25 files, per-file SHA-256 + byte sizes + row counts, all verified against the paper's headline numbers (377,482 / 378,280 / 268,519 / 637).
## Zenodo DOI: optional archival snapshot, may be minted at journal acceptance (Houston-gated). The pinned HF revision above is already immutable and sufficient for review.

---

## Released Catalog Files — authoritative list is RELEASE_MANIFEST.json

**`RELEASE_MANIFEST.json` (in this directory AND in the HF repo at the pinned revision) is the single authoritative, machine-readable file list.** It enumerates EXACTLY the 25 files released on HuggingFace with per-file SHA-256, byte size, and row count — verify downloads against it. This human-readable summary is a convenience overview only; where it and the JSON ever disagree, the JSON at the pinned revision wins.

The released parquet catalog files (as verified against the pinned revision on 2026-07-12) and their row counts:

| File | Rows | SHA-256 (abbrev.) | Tier |
|------|------|-------------------|------|
| pathc_unique_objects.parquet | 378,480 | b14deb02…6138c643 | merged 8-way dedup (headline 377,482 = minus act/gaia/erosita; 378,280 = minus ACT only) |
| pathc_multi_survey_matches.parquet | 637 | 3605b16a…c85e784 | multi-survey coincidence clusters (ACT-excluded, canonical) |
| desi_dr1_anomalies.parquet | 195,829 | 0a36b8d6…f103ec65 | validated (canonical-S) |
| sdss_dr18_pathc_native.parquet | 77,905 | 5139c663…b78a31e6 | validated continuity slice (canonical-S) |
| planck_cmb_anomalies.parquet | 200 | 9dd3576f…b05a92740 | validated (raw per-patch MSE axis) |
| neowise_anomalies.parquet | 436 | 2740d936…6aac42da | validated raw (419 survive the 80° ecliptic-pole mask) |
| gaia_dr3_anomalies.parquet | 500 | 819c5978…7396ced | exploratory (EXCLUDED from 377,482) |
| blocks/erosita_dr1/erosita_dr1_anomalies.parquet | 298 | 4ea1b032…4d082d2de | membership-only addendum (EXCLUDED; S_BigAE irreproducible — see warning) |
| act_dr6_anomalies.parquet | 200 | 65fa89af…e47cde72 | quarantined cross-transfer diagnostic (EXCLUDED) |

**NOT released as per-object tables (documented in the paper, deliberately not in the release):**
`lamost_dr10_pathc_native` (LAMOST DR10 is a failed-exploratory tier — injection-recovery FAIL, §III.F — excluded from every headline count and from the released per-object tables) and superseded staging variants (`*_no_act` parquet duplicates, `cmb_native_anomalies`, `neowise_pathc_masked`). These appeared in a pre-submission staging draft of this file that predated the frozen release; the frozen `RELEASE_MANIFEST.json` is authoritative.

Reproducibility / provenance files also released (see RELEASE_MANIFEST.json for full SHA-256 + sizes): `scripts/`-side dedup + held-out rescore (`p3_compute_to_accept/`), the NANOGrav real-KDE emcee chain + fitter (`pta_real_kde_2026-05-01/`), dedup summaries, and top-anomaly cutouts.

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
| LAMOST DR10 native | canonical-S (native rescale; top-1% slice S ≥ 0.4613) | n/a | failed-exploratory tier (injection-recovery FAIL); **NOT released as a per-object table**, excluded from every headline count |
| Gaia DR3 | canonical-S (feature-space BigAE) | no | exploratory tier; per-object scores released (excluded from the 377,482 headline) |
| NEOWISE | canonical-S (post ecliptic-pole mask) | no | per-object scores released |
| Planck CMB native | raw per-patch reconstruction MSE (survey-specific axis, NOT canonical-S) | no | 200 patches ranked by raw MSE |
| eROSITA DR1 | NONE — S_BigAE axis irreproducible (see warning above) | **yes** | n=298 membership list only; ranked by committed raw score |

---

## Gaia DR3 Feature Columns (20 features — lineage-inferred)

The Gaia DR3 anomaly table uses 20 astrometric/variability features from the published 50K-source
run. The exact 20-feature production preprocessing script was NOT recovered from pod backups.
The feature list is lineage-inferred from the 21-feature successor run (`gaia_expanded.py`).
Features (robust median/IQR-scaled; NaN→0, ±∞ clipped to ±5):

1. ra, dec (positional — 2 features)
2. parallax, parallax_error (astrometric — 2)
3. pmra, pmdec, pmra_error, pmdec_error (proper motion — 4)
4. phot_g_mean_flux, phot_bp_mean_flux, phot_rp_mean_flux (photometry — 3)
5. phot_g_mean_mag, bp_rp, bp_g (colors — 3)
6. radial_velocity, radial_velocity_error (RV — 2)
7. astrometric_excess_noise, astrometric_sigma5d_max (astrometry quality — 2)
8. ipd_frac_multi_peak (image parameter — 1)
9. ruwe (astrometric quality — 1)

*Note: exact column selection may differ from the 21-feature successor by one dropped feature.
Downstream users should verify against the gaia_expanded.py script for the closest lineage.*

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
- MCMC chain (320,000×2 float64 for NANOGrav γ/log10A) in companion repo at `wave_14_rr_nanograv_bayesian.py` outputs.
- Checksums (SHA-256) for the released files were recomputed against the pinned HuggingFace revision `573b5da7c75e4d33ab260bb5b0d57a2af0e15b23 (immutable git tag p3-v3.1.157)` on 2026-07-12 and frozen into `RELEASE_MANIFEST.json` (`manifest_frozen_utc`). The abbreviated hashes in the table above are drawn from that frozen JSON; use the JSON for full-length values.
