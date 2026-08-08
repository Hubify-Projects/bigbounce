# P3 DESI DR1 candidate catalog data dictionary

The final cohort requires main-survey science-target bits, a positional match within 1 arcsec,
`ZCAT_PRIMARY == true`, and `ZWARN == 0`. No `SPECTYPE` or redshift cut is applied.

| Column | Storage type | Meaning |
|---|---|---|
| `candidate_id` | `object` | Stable release-local identifier P3-DESI-000001, ordered by cluster_id. |
| `fits_row` | `int64` | Zero-based row number in the DESI DR1 zall-pix-iron ZCATALOG extension used for exact rejoin auditing. |
| `cluster_table_row` | `int64` | Zero-based row number in the committed Path-C cluster table; an internal reproducibility key. |
| `match_separation_arcsec` | `float64` | Great-circle separation between the DESI target coordinate and anomaly-cluster mean, in arcseconds. |
| `match_quality_tier` | `object` | Coordinate-consistent (<=0.1 arcsec) or within-1arcsec (>0.1 and <=1 arcsec); both satisfy the declared join. |
| `original_member_separation_arcsec` | `float64` | Great-circle separation between the recovered public DESI target and the canonical original DESI anomaly-member coordinate, in arcseconds; distinct from target-to-cluster match_separation_arcsec. |
| `targetid` | `int64` | Public DESI TARGETID from DR1 zall-pix-iron; the primary public rejoin key. |
| `target_ra` | `float64` | Public DESI target right ascension (ICRS degrees). |
| `target_dec` | `float64` | Public DESI target declination (ICRS degrees). |
| `survey` | `object` | DESI observing survey label; the final cohort requires main. |
| `program` | `object` | DESI observing program label (bright or dark in this release). |
| `desi_target` | `int64` | Raw DESI_TARGET bitmask from the public zcatalog. |
| `bgs_target` | `int64` | Raw BGS_TARGET bitmask from the public zcatalog. |
| `mws_target` | `int64` | Raw MWS_TARGET bitmask from the public zcatalog. |
| `scnd_target` | `int64` | Raw SCND_TARGET bitmask from the public zcatalog. |
| `z` | `float64` | Redrock redshift estimate; candidate metadata, not a validation label. |
| `zwarn` | `int64` | Redrock warning bitmask; final cohort requires zero. |
| `spectype` | `object` | Redrock best-fit spectral type; descriptive only and not a selection cut. |
| `deltachi2` | `float64` | Redrock best-versus-next-best template chi-square separation. |
| `coadd_fiberstatus` | `int32` | Bitwise OR of DESI fiber-status flags contributing to the coadd; zero for all released rows. |
| `main_nspec` | `int16` | Number of main-survey spectra associated with the target in the zcatalog. |
| `main_primary` | `bool` | Primary-within-main-survey flag; true for all released rows but not an independent final gate. |
| `zcat_nspec` | `int16` | Number of spectra associated with the target across the zcatalog grouping. |
| `zcat_primary` | `bool` | DESI global primary redshift-row flag; final cohort requires true. |
| `cluster_id` | `int64` | Original Path-C positional cluster identifier. |
| `n_detections` | `int64` | Number of original anomaly-table members in the positional cluster. |
| `n_surveys` | `int64` | Number of distinct historical input surveys represented in the cluster. |
| `survey_list` | `object` | Comma-separated historical survey membership for the cluster; retained only as audit provenance. |
| `cluster_ra_deg` | `float64` | Mean right ascension of the original anomaly cluster (ICRS degrees). |
| `cluster_dec_deg` | `float64` | Mean declination of the original anomaly cluster (ICRS degrees). |
| `cluster_best_score` | `float64` | Maximum original anomaly score among all members of the cluster. |
| `member_ids` | `object` | Pipe-separated legacy row identifiers for original cluster members; not public archive identifiers. |
| `best_survey` | `object` | Historical survey supplying cluster_best_score. |
| `desi_source_row` | `int64` | Zero-based row in the committed DESI anomaly table selected as the canonical DESI cluster member. |
| `original_internal_tid` | `int64` | Legacy anomaly-stream identifier mixing public-looking values and internal hashes; negative values are expected for some hashes. Never use as a public DESI key; use targetid. |
| `original_ra_deg` | `float64` | Right ascension carried by the canonical original DESI anomaly member (ICRS degrees). |
| `original_dec_deg` | `float64` | Declination carried by the canonical original DESI anomaly member (ICRS degrees). |
| `original_score` | `float64` | Original robust multiband anomaly score. |
| `original_worst_band` | `object` | Band producing the largest original residual. |
| `original_residual_b` | `float64` | Original B-band residual summary. |
| `original_residual_r` | `float64` | Original R-band residual summary. |
| `original_residual_z` | `float64` | Original Z-band residual summary. |
| `science_target_class` | `object` | Decoded selected DESI science bits: LRG, ELG, QSO, BGS_ANY, MWS_ANY. |
