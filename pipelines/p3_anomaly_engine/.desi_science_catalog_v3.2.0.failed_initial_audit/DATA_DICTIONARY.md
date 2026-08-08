# P3 DESI DR1 candidate catalog data dictionary

The final cohort requires main-survey science-target bits, a positional match within 1 arcsec,
`ZCAT_PRIMARY == true`, and `ZWARN == 0`. No `SPECTYPE` or redshift cut is applied.

| Column | Storage type | Meaning |
|---|---|---|
| `candidate_id` | `object` | Stable release-local identifier P3-DESI-000001, ordered by cluster_id. |
| `fits_row` | `int64` | Public DESI zcatalog field or preserved original cluster metadata. |
| `cluster_table_row` | `int64` | Public DESI zcatalog field or preserved original cluster metadata. |
| `match_separation_arcsec` | `float64` | Great-circle separation between DESI target and anomaly-cluster mean. |
| `targetid` | `int64` | Public DESI TARGETID from DR1 zall-pix-iron. |
| `target_ra` | `float64` | Public DESI target right ascension (ICRS degrees). |
| `target_dec` | `float64` | Public DESI target declination (ICRS degrees). |
| `survey` | `object` | Public DESI zcatalog field or preserved original cluster metadata. |
| `program` | `object` | Public DESI zcatalog field or preserved original cluster metadata. |
| `desi_target` | `int64` | Raw DESI_TARGET bitmask from the public zcatalog. |
| `bgs_target` | `int64` | Public DESI zcatalog field or preserved original cluster metadata. |
| `mws_target` | `int64` | Public DESI zcatalog field or preserved original cluster metadata. |
| `scnd_target` | `int64` | Public DESI zcatalog field or preserved original cluster metadata. |
| `z` | `float64` | Redrock redshift estimate; candidate metadata, not a validation label. |
| `zwarn` | `int64` | Redrock warning bitmask; final cohort requires zero. |
| `spectype` | `object` | Redrock best-fit spectral type; not used to select the final cohort. |
| `deltachi2` | `float64` | Public DESI zcatalog field or preserved original cluster metadata. |
| `coadd_fiberstatus` | `int32` | Public DESI zcatalog field or preserved original cluster metadata. |
| `main_nspec` | `int16` | Public DESI zcatalog field or preserved original cluster metadata. |
| `main_primary` | `bool` | Public DESI zcatalog field or preserved original cluster metadata. |
| `zcat_nspec` | `int16` | Public DESI zcatalog field or preserved original cluster metadata. |
| `zcat_primary` | `bool` | DESI global primary redshift-row flag; final cohort requires true. |
| `cluster_id` | `int64` | Original Path-C positional cluster identifier. |
| `n_detections` | `int64` | Public DESI zcatalog field or preserved original cluster metadata. |
| `n_surveys` | `int64` | Public DESI zcatalog field or preserved original cluster metadata. |
| `survey_list` | `object` | Public DESI zcatalog field or preserved original cluster metadata. |
| `cluster_ra_deg` | `float64` | Mean right ascension of the original anomaly cluster (ICRS degrees). |
| `cluster_dec_deg` | `float64` | Mean declination of the original anomaly cluster (ICRS degrees). |
| `cluster_best_score` | `float64` | Public DESI zcatalog field or preserved original cluster metadata. |
| `member_ids` | `object` | Public DESI zcatalog field or preserved original cluster metadata. |
| `best_survey` | `object` | Public DESI zcatalog field or preserved original cluster metadata. |
| `desi_source_row` | `int64` | Public DESI zcatalog field or preserved original cluster metadata. |
| `original_internal_tid` | `int64` | Original internal anomaly-stream identifier; not a public DESI TARGETID. |
| `original_ra_deg` | `float64` | Public DESI zcatalog field or preserved original cluster metadata. |
| `original_dec_deg` | `float64` | Public DESI zcatalog field or preserved original cluster metadata. |
| `original_score` | `float64` | Original robust multiband anomaly score. |
| `original_worst_band` | `object` | Band producing the largest original residual. |
| `original_residual_b` | `float64` | Original B-band residual summary. |
| `original_residual_r` | `float64` | Original R-band residual summary. |
| `original_residual_z` | `float64` | Original Z-band residual summary. |
| `science_target_class` | `object` | Decoded selected DESI science bits: LRG, ELG, QSO, BGS_ANY, MWS_ANY. |
