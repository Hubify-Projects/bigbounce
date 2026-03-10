# galaxy_spin_data.csv — DEPRECATED

**Status:** DEPRECATED as of 2026-03-06
**Replacement:** Galaxy Zoo DECaLS spiral catalog + Shamir (2024) aggregate counts

## Why deprecated

The file `galaxy_spin_data_DEPRECATED.csv` (formerly `galaxy_spin_data.csv`) was a 17-row
binned summary of CW/CCW galaxy counts with **unverified provenance**:

1. CW/CCW counts are suspiciously round (e.g., 25420/24580)
2. "JWST" rows claim ~1000 galaxies where the cited catalog has 195
3. "HST" totals are ~2x the published count
4. No extraction script or table reference documents how values were derived

See `research/data_audit/galaxy_spin_data_audit.md` for the full analysis.

## Replacement pipeline

The galaxy spin analysis now uses two data sources:

1. **Galaxy Zoo DECaLS** (Walmsley et al. 2022, MNRAS 509:3966)
   - DOI: 10.5281/zenodo.4573248
   - Object-level spiral galaxy catalog (~314,000 galaxies)
   - Built by: `research/data_build/build_galaxy_spin_dataset.py`
   - Output: `data/public_mirror/galaxy_zoo_decals_spins.csv`
   - Limitation: provides spiral identification, NOT CW/CCW direction

2. **Published aggregate CW/CCW counts** (Shamir 2024, arXiv:2401.09450)
   - File: `research/paper2/wp5_spin_amplitude/data/galaxy_spin_counts.csv`
   - 5 survey-level rows with verified provenance
   - Used for the hierarchical Bayesian A(z) fit

## Do not use

The deprecated file should not be used for any analysis. It remains in the
repository (renamed with `_DEPRECATED` suffix) for audit trail purposes only.
