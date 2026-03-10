# Galaxy Spin Data Adequacy Report

Generated: 2026-03-06
Auditor: Automated validation pipeline

## Executive Summary

The current galaxy-spin data pipeline is **scientifically adequate for Paper 1's claims**, provided the paper correctly frames the analysis as using published aggregate survey counts and does not claim object-level chirality classification. The pipeline is now fully transparent, reproducible, and honest about its limitations.

---

## 1. Data Sources

### Source A: Galaxy Zoo DECaLS Spiral Catalog (object-level)
- **File:** `data/public_mirror/galaxy_zoo_decals_spins.csv`
- **Source:** Walmsley et al. (2022), MNRAS 509:3966
- **DOI:** 10.5281/zenodo.4573248
- **License:** CC-BY-4.0
- **Total spiral galaxies:** 18,979 (vote_fraction >= 0.6)
- **Redshift range:** 0.0000 - 0.1500 (low-z SDSS/DECaLS footprint)
- **Columns:** galaxy_id, ra, dec, redshift, spiral_vote_fraction, winding_tight/medium/loose, survey_source
- **Checksum:** SHA-256 verified for source parquet file

### Source B: Published Aggregate CW/CCW Counts (for A(z) fit)
- **File:** `research/paper2/wp5_spin_amplitude/data/galaxy_spin_counts.csv`
- **Source:** Shamir (2024), arXiv:2401.09450, Tables 1-3
- **Rows:** 5 survey-level aggregates
- **Total galaxies:** 215,515
- **Surveys:** SDSS DR7, Pan-STARRS, HST, DECaLS, JWST JADES

| Survey | N_CW | N_CCW | N_total | A_obs | z_range |
|--------|------|-------|---------|-------|---------|
| JWST JADES | 87 | 108 | 195 | 0.108 | 0.0-6.0 |
| SDSS DR7 | 30,628 | 31,317 | 61,945 | 0.011 | 0.0-0.3 |
| Pan-STARRS | 33,498 | 34,589 | 68,087 | 0.016 | 0.0-0.3 |
| HST | 5,646 | 5,882 | 11,528 | 0.020 | 0.0-1.0 |
| DECaLS | 36,284 | 37,476 | 73,760 | 0.016 | 0.0-0.3 |

---

## 2. Strengths

1. **Fully reproducible pipeline.** The Galaxy Zoo DECaLS catalog is built from a permanent Zenodo DOI with SHA-256 checksums. Any third party can run `build_galaxy_spin_dataset.py` and get identical results.

2. **Honest provenance.** Every data value traces to a specific published source with table/section references. The deprecated fabricated data file has been removed from all active code paths.

3. **215,515 total galaxies.** The aggregate counts span 5 major surveys, providing a broad observational base for the asymmetry claim.

4. **Paper framing is correct.** Section 3.3 is titled "A Contested Anomaly," acknowledges null results (Patel & Desmond 2024, Philcox 2025), and treats the signal as "a hypothetical signature requiring confirmation."

5. **Object-level spiral catalog available.** The 18,979-galaxy GZ DECaLS catalog provides verifiable object-level data, even though it lacks CW/CCW direction.

6. **Stan model correctly uses published counts.** The `load_spin_data()` function reads from verified aggregate counts with documented column mapping.

---

## 3. Limitations

1. **5 data points for 3 parameters.** The A(z) fit has 5 survey-level bins and 3 free parameters (A0, p, q) plus 5 survey offsets and 5 label-noise parameters. This is formally underconstrained without strong priors. The hierarchical structure with informative priors (A0 ~ U[0, 0.02], eps ~ Beta(2,20)) helps, but reviewers may question the statistical power.

2. **No per-bin redshift breakdown.** The old (deprecated) dataset had 17 redshift bins; the replacement has 5 survey-level aggregates. The A(z) redshift evolution is poorly constrained with only one data point at z > 0.3 (HST at z_mid = 0.5) and one at z > 1 (JWST at z_mid = 3.0 with only 195 galaxies).

3. **Galaxy Zoo DECaLS does not include CW/CCW.** The decision tree classifies spiral winding tightness (tight/medium/loose), not chirality (clockwise/anticlockwise). This means the object-level catalog cannot independently verify the aggregate CW/CCW counts.

4. **GZ DECaLS covers z < 0.15 only.** The spiral catalog has a narrow redshift range (median z = 0.08), providing no coverage of the z > 0.3 regime where the A(z) evolution is most interesting.

5. **Contested signal.** The galaxy spin asymmetry itself is observationally contested, with independent reanalyses finding null results. The paper correctly acknowledges this.

---

## 4. What Reviewers Might Criticize

1. **"You're fitting 3 parameters to 5 data points with 13 total free parameters."** The hierarchical model has A0, p, q, 5 delta, 5 eps = 13 parameters for 5 data points. Response: the hierarchical structure and informative priors regularize the fit. But the effective number of parameters is low due to the priors.

2. **"The redshift evolution A(z) is not meaningfully constrained."** With 3 surveys at z ~ 0.15, one at z ~ 0.5, and one at z ~ 3.0, the shape of A(z) is driven by the prior more than the data. Response: the paper presents A(z) as phenomenological parameterization, not a precise measurement.

3. **"You claim an object-level catalog but it doesn't have CW/CCW."** Response: the GZ DECaLS catalog demonstrates the pipeline's ability to handle real data, and CW/CCW classification is identified as future work.

4. **"The deprecated data had 185,640 galaxies in 17 bins; the replacement has 215,515 in 5 bins. Isn't this a downgrade?"** Response: the old data was fabricated with round numbers and unverifiable provenance. Fewer honest data points are better than many dishonest ones.

---

## 5. Scientific Adequacy Assessment

### Is the dataset adequate for the paper's claims?

**YES, with caveats.**

The paper's galaxy spin section (Sec 3.3) makes the following claims:
- Galaxy spin asymmetry is a **contested anomaly** — adequately supported
- Published surveys report dipole amplitudes A ~ 0.003-0.02 — verified from cited papers
- A hierarchical Bayesian fit yields A(z) shown in Figure 2 — reproducible from the Stan model
- Independent reanalyses find null results — correctly cited
- The framework survives a null outcome — correctly argued

The paper does **not** claim:
- A definitive detection of galaxy spin asymmetry
- Object-level chirality classification from this work
- That the A(z) curve is precisely measured

The current dataset supports these claims. The key requirement is that the paper explicitly states:
1. The A(z) fit uses **published aggregate CW/CCW counts** from Shamir
2. The fit has **5 survey-level data points** (not 17 redshift bins)
3. Object-level CW/CCW classification is **future work**

### Recommendation

The galaxy spin section is scientifically defensible as currently framed. The honest data upgrade strengthens the paper's reproducibility posture despite having fewer data points than the deprecated version.

---

## 6. Pipeline Validation Checks

| Check | Result |
|-------|--------|
| Old `galaxy_spin_data.csv` removed from active code | PASS |
| Old file renamed to `_DEPRECATED` | PASS |
| No active code references old file | PASS |
| Paper text updated | PASS |
| GZ DECaLS pipeline downloads and runs | PASS |
| GZ DECaLS output is object-level (18,979 rows) | PASS |
| SHA-256 checksum file exists | PASS |
| Stan fit loads correct data file | PASS |
| Stan data path resolves correctly | PASS (bug fixed during audit) |
| Stan model receives 5 data points | PASS |
| BibTeX entries added (Walmsley2022, Shamir2024) | PASS |
| dataset_catalog.json updated | PASS |
| CW/CCW limitation documented | PASS |
