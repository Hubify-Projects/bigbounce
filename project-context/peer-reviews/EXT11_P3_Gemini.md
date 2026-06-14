# EXT11 Harvest — P3 — Gemini

- Provider: Gemini
- Model/Effort: 2.5 Thinking (Solves complex problems)
- Chat URL: https://gemini.google.com/u/0/app/0caba47ff4592563
- PDF md5: 17c9296b (paper3_anomaly_catalog_v3.1.107_17c9296b.pdf)
- Harvested: 2026-06-13 16:58 PDT

---

## Headline Verdict: MINOR REVISIONS

The author has made commendable progress in tracking down the specific implementation metrics flagged in the previous round, and the extreme candor regarding pipeline recovery is refreshing. However, the closures have effectively transformed several unquantified uncertainties into explicit, documented method flaws — most notably around data leakage, missing source code, and unrecoverable score axes.

While the paper is incredibly transparent and well-bounded, it cannot be accepted as a standard peer-reviewed community catalog release while its "recommended catalog-grade" tier contains internal logical contradictions and structural reproducibility breaks. A swift round of clean-up and textual harmonization is required before public dissemination.

## Status of Prior Items (EXT10 Review Follow-up)

**DESI Anomaly Threshold Selection:** Resolved. The transition from an ambiguous percentile schema to a rigid, absolute canonical-S cut at S>5.0 (representing 0.87% of the 22.5M spectra) has been successfully implemented across the text, tables, and figures.

**Catalog-Grade Tiering:** Partially Resolved. The abstract and primary text now clearly separate the stable, cross-validated "catalog-grade" objects from explicitly exploratory data blocks like the systematic-plagued LAMOST data. However, this tiering introduces a secondary logical contradiction detailed below.

**NANOGrav Prior Sensitivity:** Resolved. Table IX provides an excellent, mathematically sound prior-reweighting matrix spanning multiple flat intervals ([0,7], [0,5], [1,6], and [2,5]). This successfully proves that the matter-bounce density ratio remains substantially favored (B_{MB/free} ≈ 3.2) regardless of the assumed parameter boundary limits.

## New Substantive Issues & Contradictions

### 1. Methodological Data Leakage in Preprocessing

The newly added text in Section II.B reveals that feature-scaling normalizations for the tabular catalog surveys (eROSITA, NEOWISE, and Gaia) were calculated over their entire data populations rather than strictly within their random training sets.

This approach causes validation-set and extreme-tail information to bleed into the normalization constants.

The author's bounded robustness check confirms that re-fitting the scalers properly on the training pool alone alters the sample domain enough to cause a 15% to 17% churn in extreme-tail membership.

Retaining these flawed scalers simply because they represent the historic "committed production state" is a significant methodological flaw for an active data release. The author must explicitly warn downstream users in the abstract that individual extreme-tail entries carry a quantified 15% membership instability due to this preprocessing choice.

### 2. Pipeline Code Provenance and Broken Score Axes

The manuscript explicitly notes that major technical components of the underlying discovery pipeline have been permanently lost or corrupted:
- The original 20-feature production preprocessing script for the Gaia DR3 run was not recovered from any backup and is merely "lineage-inferred" from successor code.
- Worse, the primary anomaly score axis (S_{BigAE}) for the eROSITA catalog cannot be reproduced or mathematically reconciled across any of the 16 tested monotone rescalings.

Downstream users are explicitly blocked from executing basic statistical procedures like threshold re-derivation, score-weighted stacking, or structural outlier re-isolation. Releasing a catalog where individual data row values are fundamentally decoupled from the script architecture severely limits its scientific utility.

### 3. Logical Contradiction in Target Tier Definitions

There is a direct logical contradiction between how the "catalog-grade" subset is defined versus how it is constructed:

- Section I states that the recommended catalog-grade point-source subset (269,117 unique entries) is exclusively derived from surveys that "pass injection-recovery and native-retrain validation."
- However, Section II.D, Section VI.D, and Figure 10 explicitly show that eROSITA and Gaia failed their respective validation gates at 5σ, yielding miserable recovery rates of just 1.2% and 5.2%.

Despite these definitive failures, both datasets are still included in the final "catalog-grade" recommended subset list. The author must either remove eROSITA and Gaia from the catalog-grade tier or rewrite the selection definition to accurately reflect that failed surveys are being force-included.

### 4. Overly Optimistic Sensitivity Shorthand

The manuscript frequently relies on a text shorthand asserting that "3 surveys PASS" the injection-recovery gates (SDSS, Planck, and NEOWISE). However, Section III.H and Section VI.D clarify that the NEOWISE test merely plants synthetic entries behind a spatial coordinates boundary line and checks if the fixed pipeline mask drops them.

As the author notes, passing this test is guaranteed by construction. It functions as an engineering sanity check on masking geometry, not an operational test of the autoencoder detector's sensitivity to anomalous infrared variations.

Lumping this trivial geometric filter in with the genuine machine-learning detector passes of SDSS and Planck inflates the apparent reliability of the framework. The text and abstract must be revised to state that only 2 surveys passed genuine detector-sensitivity gates.
