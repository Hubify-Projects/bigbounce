# P3 v3.2.0-r2 selection and integrity audit

**Status: PASS**

## Selection waterfall

| Stage | Rows |
|---|---:|
| Existing main-survey science-bit matches within 1 arcsec | 2,468 |
| Removed because not `ZCAT_PRIMARY` | 20 |
| Primary rows remaining | 2,448 |
| Removed because `ZWARN != 0` | 2,267 |
| Released warning-free primary candidates | **181** |

The released cohort is 7.33% of the positional
science-bit cohort. It is a conservative redshift-quality slice, not a complete or unbiased
sample: the `ZWARN == 0` gate preferentially removes spectra with fitting problems, which are
common in an anomaly-selected population. The catalog supports reproducible object-level
follow-up; it must not be used to infer anomaly occurrence rates without modeling this selection.

## Integrity results

- All 181 public `TARGETID` values and all 18 carried DESI fields
  rejoin exactly to their recorded rows in the local public DR1 FITS.
- The released and strict checkpoint-derived `(cluster_id, targetid, fits_row)` sets are exactly
  equal (181/181); there are no missing or unexpected rows.
- Candidate ID, cluster ID, and TARGETID are unique; there are no null cells.
- Every row is main survey, carries a specified science bit, is `ZCAT_PRIMARY`, has `ZWARN=0`,
  and lies within 1 arcsec of its anomaly cluster.
- Spectral types (descriptive, not selected): {'GALAXY': 157, 'QSO': 23, 'STAR': 1}.
- Programs: {'dark': 162, 'bright': 19}.
- Sky coverage follows the DESI footprint (134 north,
  47 south); no all-sky uniformity is claimed.
- Exactly one released row has `n_detections > 1`: `P3-DESI-000030`.
  Its public target is 1.979009 arcsec
  from the canonical original DESI anomaly member; this is distinct from target-to-cluster separation.
- Separation tail: 11 rows exceed 0.1 arcsec,
  8 exceed 0.5 arcsec, and the maximum is
  0.9906 arcsec. These rows are retained under the
  predeclared 1-arcsec join and explicitly flagged by `match_quality_tier`.
- Local FITS SHA-256: `2d95ad99361039b556c402b49e0e7c84df5f00106dc5731d44476a58b128b49b`; current official checksum:
  `2d95ad99361039b556c402b49e0e7c84df5f00106dc5731d44476a58b128b49b`; match: `True`. The older May sidecar value `50031c9ba35d0181c7bfc7ffba661941b9300aaff15ee725662ab796a22999eb`
  is preserved as stale provenance and is not used for validation.
- Public source: https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/v1/zall-pix-iron.fits
- Official checksums: https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/v1/redux_iron_zcatalog_v1.sha256sum
- Live remote range parity: `PASS`; 8/
  8 exact 1 MiB HTTP 206/Content-Range/digest checks passed.

Machine-readable details, including null counts, redshift/score/separation distributions,
sky-bin coverage, exact per-field rejoin results, and remote HEAD metadata are in
`SELECTION_AUDIT.json`.
