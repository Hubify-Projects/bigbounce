# Data Release Manifest — BigBounce Multi-Survey Anomaly Catalog
## Paper: Golden (2026), "Spectrally Unusual Sources at Scale" (Paper 3)
## Frozen: 2026-06-10 (EXT1 closure wave, pre-submission staging)
## Status: STAGED (not yet public; will flip to public on arXiv posting)
## HuggingFace: https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog
## Zenodo DOI: [TO BE MINTED AT SUBMISSION — insert here before arxiv upload]

---

## Canonical Catalog Files (hf_staging/)

| File | SHA-256 | Description |
|------|---------|-------------|
| pathc_unique_objects_no_act.parquet | e0b57f255f716845b56f398015858b1ed837c85c3b483433fa424a84ac455664 | PRIMARY: 378,280 unique anomalies (7-way 5″ dedup, ACT excluded) |
| pathc_unique_objects.parquet | b14deb02ddc374cc30a54e6013c0695d1c35cbf18cef9144245e338d6138c643 | Sensitivity check: 378,480 unique anomalies (8-way with ACT) |
| pathc_multi_survey_matches_no_act.parquet | 3605b16a939b1dc44c4cb76e96dcbb7411a6eeb5917d12567c4fbc35fc85e784 | 637 multi-survey coincidence clusters (no ACT) — CANONICAL |
| pathc_multi_survey_matches.parquet | 3605b16a939b1dc44c4cb76e96dcbb7411a6eeb5917d12567c4fbc35fc85e784 | Multi-survey coincidence clusters (with ACT sensitivity check) — **BYTE-IDENTICAL to _no_act variant**: ACT contributes zero multi-survey overlaps (§planck_act_null confirms disjoint footprints); both files staged for naming consistency only. The _no_act file is canonical. |
| cmb_native_anomalies.parquet | ec1464cdd39fd4cc51aefb3573601e9283a10336a4a74e695caa6a8327114273 | Planck CMB native retrain: 200 anomaly patches |
| gaia_dr3_anomalies.parquet | 819c59789eb1b94de4d46a62777fd125fb084b8c70f3d627b734a45af7396ced | Gaia DR3 anomalies: 500 objects (exploratory tier) |
| lamost_dr10_pathc_native.parquet | 48c0e2f5420de010923dc69c5c439aaf4cf82c9a301ef55320571bd6d9516a40 | LAMOST DR10 native retrain: 113,342 objects (exploratory tier) |
| neowise_anomalies.parquet | 2740d936a2289ab32bc925f4507a449aa14445976e916459303874386aac42da | NEOWISE raw anomalies: 436 objects (pre-ecliptic mask) |
| neowise_pathc_masked_anomalies.parquet | fdee011e2266e007f3420bc5222df322a89ca5e64f0e0e5f46507c8c7e433b1b | NEOWISE Path-C masked: 419 objects (post ecliptic-pole mask) |
| planck_cmb_anomalies.parquet | 9dd3576f8de7251b9ee2bed13e61acc66d3faa530c317ae61dfd2e6b05a92740 | Planck CMB cross-transfer baseline (200 patches; diagnostic only) |
| sdss_dr18_pathc_native.parquet | 5139c663c12f40217ea646fa8140c91f40194b42ca891912db73301ab78a31e6 | SDSS DR18 native retrain continuity slice: 77,905 objects |
| act_dr6_cross_transfer_anomalies.parquet | 9eed61687f10859dc8830acfd21f49ca5edc367a84ef953c6830b54dbde9b97f | ACT DR6 cross-transfer (quarantined; archived separately) |

## Staged from Pod (hf_staging_pod/)

| File | SHA-256 | Description |
|------|---------|-------------|
| erosita_dr1_anomalies.parquet | 4ea1b032aa8a5e51ea10fd600aec7b52f80598830e04f54f2dfa2dd4e082d2de | eROSITA DR1: 298 anomalies (membership-only canonical; score axis irreproducible — see §III.E and r24conf_erosita_axis_sweep.json) |

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
| LAMOST DR10 native | canonical-S (native rescale; top-1% slice S ≥ 0.4613) | no | exploratory tier; per-object scores released |
| Gaia DR3 | canonical-S (feature-space BigAE) | no | exploratory tier; per-object scores released |
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

DESI DR1 native-retrained anomalies (195,829 objects) are hosted separately due to size.
See companion GitHub repository: https://github.com/Hubify-Projects/bigbounce

---

## Reproducibility Notes

- All .parquet files use pandas/pyarrow schema; schema documented in companion-repo README.md.
- The 7-way dedup was run with `pathc_positional_dedup.py` (deterministic, archived at same repo).
- MCMC chain (320,000×2 float64 for NANOGrav γ/log10A) in companion repo at `wave_14_rr_nanograv_bayesian.py` outputs.
- Checksums computed with `sha256sum` on 2026-06-10 (pre-public staging snapshot).
