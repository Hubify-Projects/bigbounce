# P3 DESI DR1 science-target anomaly candidates v3.2.0

This clean release contains only the public-ID-rejoinable DESI DR1 candidate catalog and the
artifacts required to reproduce and audit it. It does not contain the historical Gaia,
eROSITA, LAMOST, SDSS, Planck, or mixed-survey tables.

The released cohort contains **181 candidates** selected by a one-arcsecond
positional join to main-survey DESI science targets carrying at least one of the LRG, ELG,
QSO, BGS_ANY, or MWS_ANY `DESI_TARGET` bits, followed by `ZCAT_PRIMARY == true` and
`ZWARN == 0`. These are anomaly **candidates**, not validated astrophysical detections.

Files:

- `desi_dr1_science_anomaly_candidates_v3.2.0.parquet` — released candidate table.
- `DATA_DICTIONARY.md` — field definitions and selection semantics.
- `COHORT_COUNTS.json` — existing-bitmask and stricter-cohort counts.
- `QC_REPORT.json` — machine-readable assertions and descriptive summaries.
- `PROVENANCE.json` — exact inputs, runtime, selection, and build command.
- `build_desi_science_catalog_v320.py` — exact build code.
- `RELEASE_MANIFEST.json` — SHA-256 and byte size for every payload file.

The manifest excludes itself to avoid a self-referential checksum. Historical P3 releases
remain historical and are not moved, deleted, or silently replaced by this release.
