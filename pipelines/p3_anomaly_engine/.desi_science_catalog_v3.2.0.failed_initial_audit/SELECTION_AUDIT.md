# P3 v3.2.0 selection and integrity audit

**Status: FAIL**

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
- Candidate ID, cluster ID, and TARGETID are unique; there are no null cells.
- Every row is main survey, carries a specified science bit, is `ZCAT_PRIMARY`, has `ZWARN=0`,
  and lies within 1 arcsec of its anomaly cluster.
- Spectral types (descriptive, not selected): {'GALAXY': 157, 'QSO': 23, 'STAR': 1}.
- Programs: {'dark': 162, 'bright': 19}.
- Sky coverage follows the DESI footprint (134 north,
  47 south); no all-sky uniformity is claimed.
- Local FITS SHA-256: `2d95ad99361039b556c402b49e0e7c84df5f00106dc5731d44476a58b128b49b`; recorded upstream SHA-256:
  `50031c9ba35d0181c7bfc7ffba661941b9300aaff15ee725662ab796a22999eb`; match: `False`.
- Public source: https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/v1/zall-pix-iron.fits

Machine-readable details, including null counts, redshift/score/separation distributions,
sky-bin coverage, exact per-field rejoin results, and remote HEAD metadata are in
`SELECTION_AUDIT.json`.
