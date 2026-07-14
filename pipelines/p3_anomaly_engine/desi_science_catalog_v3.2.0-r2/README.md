# P3 DESI DR1 science-target anomaly candidates v3.2.0-r2

This clean release contains only the public-ID-rejoinable DESI DR1 candidate catalog and the
artifacts required to reproduce and audit it. It does not contain the historical Gaia,
eROSITA, LAMOST, SDSS, Planck, or mixed-survey tables.

The released cohort contains **181 candidates** selected by a one-arcsecond
positional join to main-survey DESI science targets carrying at least one of the LRG, ELG,
QSO, BGS_ANY, or MWS_ANY `DESI_TARGET` bits, followed by `ZCAT_PRIMARY == true` and
`ZWARN == 0`. These are anomaly **candidates**, not validated astrophysical detections.
Rows are also labeled by `match_quality_tier`: separations at or below 0.1 arcsec are
coordinate-consistent, while the disclosed 0.1--1 arcsec tail remains available for users
who accept the predeclared one-arcsecond positional join.

Exactly one released row has `n_detections > 1`: `P3-DESI-000030` (cluster
`71390`, `n_detections=2`). Its public target is
`1.979009` arcsec from the canonical original
DESI anomaly member. The release stores this value in
`original_member_separation_arcsec`; it is distinct from the target-to-cluster separation.

## Immutable inputs

- Path-C clusters: `https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog/resolve/cdaaa03a72c69d86f011be128d93f261dc5b39a8/pathc_unique_objects.parquet`
  SHA-256: `b14deb02ddc374cc30a54e6013c0695d1c35cbf18cef9144245e338d6138c643`
- Historical DESI anomaly rows: `https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog/resolve/cdaaa03a72c69d86f011be128d93f261dc5b39a8/desi_dr1_anomalies.parquet`
  SHA-256: `0a36b8d6dfb8086c2c417885c99689d7a75b416dad1b030db56477baf103ec65`
- Public DESI DR1 zcatalog: `https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/v1/zall-pix-iron.fits`  
  SHA-256: `2d95ad99361039b556c402b49e0e7c84df5f00106dc5731d44476a58b128b49b`

The two historical inputs are pinned at annotated tag `p3-v3.1.161`, which peels to
commit `cdaaa03a72c69d86f011be128d93f261dc5b39a8`. The DESI checksum was recomputed locally and matched the current
official checksum file at `https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/v1/redux_iron_zcatalog_v1.sha256sum`.

The historical dataset and this candidate-catalog data/documentation are distributed under
CC BY 4.0. The bundled Python scripts retain their repository license. The exact historical
model is not reconstructed here: frozen upstream documentation identifies the DESI score as
canonical-S output from a DESI-trained BigAE autoencoder, and this release carries that score
only as uncalibrated ranking metadata.

## Reproduce and validate

```sh
curl -fL -o pathc_unique_objects.parquet https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog/resolve/cdaaa03a72c69d86f011be128d93f261dc5b39a8/pathc_unique_objects.parquet
curl -fL -o desi_dr1_anomalies.parquet https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog/resolve/cdaaa03a72c69d86f011be128d93f261dc5b39a8/desi_dr1_anomalies.parquet
curl -fL -o zall-pix-iron.fits https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/v1/zall-pix-iron.fits
FITS_SHA256=2d95ad99361039b556c402b49e0e7c84df5f00106dc5731d44476a58b128b49b
python3 build_desi_science_catalog_v320_r2.py   --clusters pathc_unique_objects.parquet   --anomalies desi_dr1_anomalies.parquet   --fits zall-pix-iron.fits   --output-dir desi_science_catalog_v3.2.0-r2   --chunk-rows 200000   --fits-sha256 "$FITS_SHA256"
python3 validate_desi_science_catalog_v320_r2.py   --release-dir desi_science_catalog_v3.2.0-r2   --fits zall-pix-iron.fits   --clusters pathc_unique_objects.parquet   --parts-dir .desi_science_catalog_v3.2.0-r2.build/match_parts
```

`--parts-dir` may be omitted when the checkpoint remains beside the release: the validator
portably derives `.RELEASE_DIR.name.build/match_parts` from `--release-dir`. The explicit form
also supports moved checkpoints. Verify the historical inputs with:

```sh
printf '%s  %s\n' \
  b14deb02ddc374cc30a54e6013c0695d1c35cbf18cef9144245e338d6138c643 pathc_unique_objects.parquet \
  0a36b8d6dfb8086c2c417885c99689d7a75b416dad1b030db56477baf103ec65 desi_dr1_anomalies.parquet \
  | sha256sum -c -
```

Files:

- `desi_dr1_science_anomaly_candidates_v3.2.0-r2.parquet` — released candidate table.
- `DATA_DICTIONARY.md` — field definitions and selection semantics.
- `COHORT_COUNTS.json` — existing-bitmask and stricter-cohort counts.
- `QC_REPORT.json` — machine-readable assertions and descriptive summaries.
- `SELECTION_AUDIT.json` / `SELECTION_AUDIT.md` — independent rejoin, waterfall,
  distribution, separation-tail, null, duplicate, and provenance audit (added by the
  bundled validation script before publication).
- `PROVENANCE.json` — exact inputs, runtime, selection, and build command.
- `build_desi_science_catalog_v320_r2.py` — exact build code.
- `validate_desi_science_catalog_v320_r2.py` — exact independent validation code.
- `RELEASE_MANIFEST.json` — SHA-256 and byte size for every payload file.

The manifest excludes itself to avoid a self-referential checksum. Historical P3 releases
remain historical and are not moved, deleted, or silently replaced by this release.
