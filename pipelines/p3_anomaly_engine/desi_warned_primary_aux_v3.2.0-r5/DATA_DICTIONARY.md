# P3 warned-primary auxiliary data dictionary

**Secondary/non-primary/not physically validated.** Every row is a global-primary
DESI positional match with nonzero `ZWARN`; none belongs to the 181-row primary catalog.

| Column | Storage type | Meaning |
|---|---|---|
| `candidate_id` | `object` | Stable auxiliary-only ID ordered by cluster_id; prefix P3-DESI-WARNED prevents confusion with the primary catalog. |
| `auxiliary_status` | `object` | Constant label declaring this row secondary, warning-bearing, non-primary, and not physically validated. |
| `primary_catalog_member` | `bool` | Always false; the 181-row ZWARN=0 catalog is the primary product. |
| `fits_row` | `int64` | Zero-based row in the exact DESI DR1 zall-pix-iron ZCATALOG extension. |
| `cluster_table_row` | `int64` | Zero-based row in the immutable Path-C cluster table. |
| `match_separation_arcsec` | `float64` | Great-circle target-to-cluster separation in arcseconds; required <=1. |
| `match_quality_tier` | `object` | Coordinate-consistent <=0.1 arcsec or positional >0.1 and <=1 arcsec. |
| `original_member_separation_arcsec` | `float64` | Target-to-canonical-original-member separation; not a selection cut. |
| `targetid` | `int64` | Public DESI DR1 TARGETID. |
| `target_ra` | `float64` | Public target ICRS right ascension in degrees. |
| `target_dec` | `float64` | Public target ICRS declination in degrees. |
| `survey` | `object` | DESI survey label; main for this cohort. |
| `program` | `object` | DESI observing program. |
| `desi_target` | `int64` | Raw DESI_TARGET mask. |
| `bgs_target` | `int64` | Raw BGS_TARGET mask. |
| `mws_target` | `int64` | Raw MWS_TARGET mask. |
| `scnd_target` | `int64` | Raw SCND_TARGET mask. |
| `z` | `float64` | Redrock redshift metadata; not a validation label. |
| `zwarn` | `int64` | Nonzero Redrock warning mask that caused exclusion from the primary catalog. |
| `zwarn_hex` | `object` | ZWARN rendered as an unsigned 64-bit hexadecimal string. |
| `zwarn_decoded_bits` | `object` | Pipe-separated exact set bits: LITTLE_COVERAGE, SMALL_DELTA_CHI2, and/or POORDATA. |
| `spectype` | `object` | Redrock best-fit spectral type; descriptive only. |
| `deltachi2` | `float64` | Redrock best-versus-next-best chi-square separation. |
| `coadd_fiberstatus` | `int32` | Bitwise OR of contributing DESI fiber-status flags. |
| `main_nspec` | `int16` | Number of main-survey spectra for the target. |
| `main_primary` | `bool` | Primary-within-main-survey flag. |
| `zcat_nspec` | `int16` | Number of spectra in the global zcatalog grouping. |
| `zcat_primary` | `bool` | Global primary redshift-row flag; required true. |
| `cluster_id` | `int64` | Stable historical positional-cluster identifier. |
| `n_detections` | `int64` | Number of historical members in the cluster. |
| `n_surveys` | `int64` | Number of historical surveys in the cluster. |
| `survey_list` | `object` | Comma-separated historical survey membership. |
| `cluster_ra_deg` | `float64` | Historical cluster ICRS mean right ascension. |
| `cluster_dec_deg` | `float64` | Historical cluster ICRS mean declination. |
| `cluster_best_score` | `float64` | Maximum historical score in the cluster. |
| `member_ids` | `object` | Pipe-separated legacy member row identifiers; not public archive IDs. |
| `best_survey` | `object` | Historical survey supplying cluster_best_score. |
| `desi_source_row` | `int64` | Row of the canonical DESI member in the immutable anomaly table. |
| `original_internal_tid` | `int64` | Legacy mixed/hash identifier; never use as a public key. |
| `original_ra_deg` | `float64` | Canonical historical DESI member ICRS right ascension. |
| `original_dec_deg` | `float64` | Canonical historical DESI member ICRS declination. |
| `original_score` | `float64` | Frozen historical canonical-S score; uncalibrated ranking metadata only. |
| `original_worst_band` | `object` | Historical band with the largest residual summary. |
| `original_residual_b` | `float64` | Historical B-band residual summary. |
| `original_residual_r` | `float64` | Historical R-band residual summary. |
| `original_residual_z` | `float64` | Historical Z-band residual summary. |
| `science_target_class` | `object` | Decoded selected DESI science bits. |
