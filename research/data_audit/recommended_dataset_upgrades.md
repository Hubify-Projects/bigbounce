# Recommended Dataset Upgrades

Generated: 2026-03-06

## Priority 1: Galaxy Spin Data (CRITICAL)

The current `galaxy_spin_data.csv` must be replaced or properly documented.

### Option A: Galaxy Zoo DECaLS (BEST — already referenced in dataset_registry.csv)

| Property | Value |
|----------|-------|
| **Source** | Galaxy Zoo DECaLS (Walmsley et al. 2022, MNRAS 509:3966) |
| **URL** | https://zenodo.org/records/4573248 |
| **Expected size** | ~500 MB (CSV), ~314,000 galaxies |
| **Level** | Object-level (one row per galaxy) |
| **Columns** | objid, ra, dec, morphology votes including spiral arm winding direction |
| **Download** | `wget https://zenodo.org/records/4573248/files/gz_decals_auto_posteriors.csv` |
| **License** | CC-BY-4.0 |
| **Why better** | Real object-level data with per-galaxy classifications from citizen science volunteers. Can compute CW/CCW counts per redshift bin directly. Independently verifiable. Well-documented data release with DOI. |
| **Limitation** | Galaxy Zoo classifies winding direction, not physical spin. The mapping from visual winding to physical rotation is non-trivial. Low-z only (SDSS/DECaLS footprint). |

### Option B: Shamir (2022) SpArcFiRe Catalog

| Property | Value |
|----------|-------|
| **Source** | Shamir (2022), "Analysis of ~106 spiral galaxies from four telescopes" |
| **URL** | https://people.cs.ksu.edu/~lshamir/data/sparcfire/ (check availability) |
| **Expected size** | Unknown — may be available on request |
| **Level** | Object-level if available |
| **Download** | Check Shamir's data page or contact author |
| **License** | Unknown — check with author |
| **Why better** | Would provide the actual catalog behind the Shamir (2012, 2022) claims cited in the paper |
| **Limitation** | May not be publicly released as machine-readable catalog. SpArcFiRe classification accuracy is contested (Patel & Desmond 2024). |

### Option C: SDSS Object-Level Tables

| Property | Value |
|----------|-------|
| **Source** | SDSS DR17 Galaxy Zoo 2 table |
| **URL** | https://skyserver.sdss.org/dr17/ (CasJobs query) |
| **Expected size** | ~200 MB for spirals with morphology flags |
| **Level** | Object-level |
| **Download** | SQL query via CasJobs or SDSS SkyServer API |
| **License** | Public domain (SDSS data policy) |
| **Why better** | Primary data source. Can select spirals with reliable morphology flags and compute asymmetry directly. |
| **Limitation** | Requires careful selection cuts. Galaxy Zoo 2 flags available for subset. |

### Option D: Use galaxy_spin_counts.csv as-is (MINIMUM FIX)

| Property | Value |
|----------|-------|
| **Source** | Already in repo: `research/paper2/wp5_spin_amplitude/data/galaxy_spin_counts.csv` |
| **Expected size** | 1.3 KB, 5 survey-level rows |
| **Level** | Survey aggregate (one row per survey) |
| **Why better** | Honestly documented provenance. Values verified against cited paper. |
| **Limitation** | Only 5 data points — a hierarchical Bayesian fit with 5 data points and 3 free parameters is underconstrained. But at least it's honest. |

### Recommendation

**Option A (Galaxy Zoo DECaLS) is the strongest upgrade.** It is already documented in the project's `dataset_registry.csv` and was partially used in the P7 CNN track. It provides:
- Hundreds of thousands of object-level classifications
- Permanent DOI via Zenodo
- CC-BY-4.0 license
- Independent verification possible

The workflow would be:
1. Download Galaxy Zoo DECaLS catalog from Zenodo
2. Cross-match with SDSS photometric redshifts
3. Select spiral galaxies with clear CW/CCW vote majority
4. Bin by redshift
5. Fit A(z) model to these bins
6. Document every step in a Jupyter notebook

This replaces the current opaque `galaxy_spin_data.csv` with a fully reproducible pipeline from public data to fitted parameters.

---

## Priority 2: Local Data Mirrors

Currently, several public datasets exist only on RunPod pods:

| Dataset | Size | Action |
|---------|------|--------|
| Planck PR4 maps | ~13 GB | Document exact download commands. Too large to mirror in git. |
| Galaxy Zoo DECaLS | ~500 MB | Mirror to `data/public_mirror/galaxy_zoo_decals/` if used in analysis |
| SDSS imaging cutouts | ~2-5 GB | Document download script only |

### Recommended structure for mirrors:
```
data/public_mirror/
  galaxy_zoo_decals/
    README.md          # source URL, DOI, license, citation
    download.sh        # exact download command
    CHECKSUMS.txt      # SHA256 of downloaded file
    gz_decals_auto_posteriors.csv  # actual data (if <1 GB)
  planck_pr4/
    README.md
    download.sh        # commands for each FITS file
    CHECKSUMS.txt
  shamir_2024/
    README.md
    galaxy_spin_counts.csv  # the honest 5-row reconstruction
```

---

## Priority 3: Figure Data Documentation

All figure panel CSVs in `data/figures/` have good `meta.yml` files documenting schema and provenance. No upgrade needed — these are model predictions and comparison values, appropriately labeled.

The Excel spreadsheets in `public/spreadsheets/` should have a companion `README.md` explaining that they contain the same data as the CSV panel files, formatted for web visualization.
