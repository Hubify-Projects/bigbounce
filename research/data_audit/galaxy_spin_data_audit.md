# Galaxy Spin Data Audit

Generated: 2026-03-06
Status: **CRITICAL — REQUIRES ACTION**

## Executive Summary

The file `reproducibility/galaxy_spins/galaxy_spin_data.csv` is **NOT a raw per-galaxy catalog, NOT a released derived catalog, and NOT a faithful extraction from published tables**. It is a **17-row binned summary with fabricated-looking round numbers** that cannot be traced to any specific published data source.

The paper (arxiv/main.tex) correctly labels galaxy spin asymmetry as "A Contested Anomaly" (Sec 3.3) and acknowledges null results from independent reanalyses. This intellectual honesty is good. But the underlying data file used for the hierarchical Bayesian fit does not match the standards the paper implies.

---

## File Analysis

### File: `reproducibility/galaxy_spins/galaxy_spin_data.csv`

**Row count**: 17 data rows (+ 1 header)
**Columns**: `z_bin_center, z_bin_width, N_cw, N_ccw, survey_id, b_weight, psf_quality_flag`
**Each row represents**: One redshift bin with aggregate CW/CCW galaxy counts
**Level**: BIN-LEVEL (not object-level, not image-level)

**Breakdown by "survey"**:
| Survey | Rows | z range | Total galaxies implied |
|--------|------|---------|----------------------|
| SDSS | 10 | 0.05-0.95 | 162,340 |
| HST | 5 | 0.3-1.1 | 21,400 |
| JWST | 3 | 1.5-2.5 | 1,900 |
| **Total** | **18** | | **185,640** |

### Problem 1: Round numbers suggest manual construction

The CW/CCW counts are suspiciously round:
- 25420 / 24580 (z=0.05)
- 18960 / 18240 (z=0.15)
- 15230 / 14770 (z=0.25)

Real binned galaxy counts from survey pipelines are never this round. These look like they were constructed to produce a desired asymmetry pattern, not extracted from actual catalogs.

### Problem 2: JWST data does not exist in this form

Rows 17-18 claim JWST data at z=2.0 and z=2.5 with counts of:
- z=2.0: 360 CW / 240 CCW (N=600)
- z=2.5: 280 CW / 120 CCW (N=400)

But Shamir (2024, arXiv:2401.09450) — the only published JWST galaxy spin paper — reports a total of **195 classified spiral galaxies** in the JWST JADES GOODS-South field. There is no z=2.0 or z=2.5 bin with 600 or 400 galaxies in any published JWST spin catalog.

### Problem 3: HST bins don't match published counts

Shamir (2020) reports **11,528 total HST classified spirals**. The CSV claims 21,400 total across HST bins — roughly 2x the published count.

### Problem 4: SDSS totals are plausible but unverifiable

The 162,340 total across SDSS bins is in the right ballpark (Shamir 2012 reports ~62k, Shamir 2022 reports larger samples). But the specific per-bin breakdown cannot be verified against any published table.

### Problem 5: No extraction documentation

There is no script, no notebook, no log file documenting how these values were derived from published data. The `reproduce_spins.sh` script runs the Stan fit on this file but does not generate the file itself.

### Problem 6: Identical duplicate exists

`data/galaxy_spin_bins_example.csv` is byte-for-byte identical (same SHA256). Having two undocumented copies of a problematic file increases confusion.

---

## Comparison with galaxy_spin_counts.csv (Paper 2)

The Paper 2 file `research/paper2/wp5_spin_amplitude/data/galaxy_spin_counts.csv` handles the same type of data **correctly**:

1. Clear header: "Reconstructed from Published Tables"
2. Cites specific paper: Shamir (2024), arXiv:2401.09450
3. References specific tables: "Table 1", "text Sec 2"
4. Notes: "NOT from a downloadable machine-readable catalog"
5. Values match what the cited paper actually reports

This demonstrates the project knows how to document reconstructed data properly. `galaxy_spin_data.csv` simply doesn't meet the same standard.

---

## Is galaxy_spin_data.csv acceptable as-is?

**NO.**

1. The data cannot be independently verified or reproduced
2. The JWST bins contain counts that contradict the cited source
3. The round numbers suggest manual construction rather than extraction
4. There is no extraction documentation

**However**: The paper itself handles this reasonably well:
- Section 3.3 is titled "A Contested Anomaly"
- It acknowledges Patel & Desmond (2024) and Philcox (2025) null results
- Table 2 caption says "All entries are global dipole amplitudes from the respective authors' analyses"
- The paper treats galaxy spin as a "hypothetical signature requiring confirmation"

The scientific framing is honest, but the data artifact is not. The file creates a false impression that there is a well-documented, reproducible dataset behind the analysis when there isn't.

---

## Does "tens of thousands of galaxy spin datapoints" hold up?

Searching the paper text: **The paper does NOT make this claim.** It references specific sample sizes from cited papers (e.g., "SDSS DR7" with 61,945 from Shamir 2012). The paper is careful about quantities.

However, the `galaxy_spin_data.csv` file implies 185,640 total classified galaxies across its bins, which is misleading given that the counts don't correspond to any published dataset.

---

## Recommended Actions

1. **Rename** `galaxy_spin_data.csv` to `galaxy_spin_bins_ILLUSTRATIVE.csv` and add a header comment explaining it is an illustrative/approximate reconstruction
2. **Replace** the fitting analysis with one based on the honest `galaxy_spin_counts.csv` from Paper 2 (survey-level aggregate counts)
3. **Or better**: Use the actual published summary statistics directly from Shamir (2012, 2022, 2024) and cite table numbers
4. **Delete** the duplicate `data/galaxy_spin_bins_example.csv` or make it a symlink with clear documentation
5. **Add** a data provenance README to `reproducibility/galaxy_spins/` explaining exactly what the file contains and how it was created
