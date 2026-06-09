# P5 R22prov — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 441.3s

---

Meta-review (focus: blind spots none of the five referees raised)

P5-META-E1
- Severity: ESSENTIAL
- Section + page: §VI A Fig. 3 caption and Table II (pp. 6–7)
- Why others missed it: Reviewers noted parent-set ambiguities elsewhere but did not catch this explicit sum mismatch.
- Problem: The caption states “on n = 791,635 chirality-relevant matched spirals,” yet the per-class counts shown/quoted (void 428, wall 6,673, filament 408,187, cluster 397,505) sum to 812,793, not 791,635. This is not just a rounding issue: the figure and Table II are computed on the larger env-labeled superset while being described as the 791,635 set.
- Required fix: Correct the caption and text to state explicitly which parent set is used in Fig. 3/Table II, and ensure all per-class counts, totals, and σ are reported on a single, clearly identified parent set. Provide both versions (791,635 and 812,793) in an appendix if both are used elsewhere.

P5-META-E2
- Severity: ESSENTIAL
- Section + page: §VIII (first paragraph, p. 10) vs §VIII C (p. 12)
- Why others missed it: Prior reviews focused on method naming and KDTree details but not void-count consistency across sections.
- Problem (quote juxtaposition):
  - p. 10: “... 1,461 interior voids with VoidFinder, 420 with V2-REVOLVER, and 295 with V2-VIDE.”
  - p. 12: “V2-REVOLVER (n_catalog_void = 1,992 ...), V2-VIDE (n_catalog_void = 1,478 ...).”
  The reported numbers for REVOLVER/VIDE differ by factors of ~5 without explanation.
- Required fix: Clarify the definitions (e.g., “maximal voids” vs “effective voids” vs “zones” vs “holes”) and correct the counts. Provide a single table listing, for each DESIVAST algorithm: the number of catalog entries of each type you actually used in every analysis (maximal voids, interior holes, zones, etc.), with consistent terminology across the manuscript.

P5-META-E3
- Severity: ESSENTIAL
- Section + page: §VIII A (p. 11), §IV A steps 2–4 (p. 4)
- Why others missed it: No one audited the distance–unit pipeline end-to-end.
- Problem: The text asserts distances “in h−1 Mpc consistent with the DESIVAST hole catalog,” but computing χ(z) with a Planck-2018 cosmology (e.g., via Astropy) natively yields comoving distances in Mpc (not h−1 Mpc) unless explicitly rescaled. It is never stated how or where the h-scaling was applied. If χ was used directly as h−1 Mpc in point-in-sphere tests, all memberships are radially off by a factor h ≈ 0.676, which would change void/non-void assignments near boundaries.
- Required fix: Document explicitly (i) the unit returned by the cosmology routine, (ii) the exact conversion applied to obtain h−1 Mpc, and (iii) a sanity check (e.g., χ(z=0.2) value) demonstrating consistency. Re-run a small eroded/dilated-membership sensitivity (±5 h−1 Mpc) to show that any unit slip would not change conclusions.

P5-META-M1
- Severity: MAJOR
- Section + page: §V (p. 5) and throughout where σpred is compared to σobs
- Why others missed it: Reviewers asked for formulas but not the statistical validity of the comparison.
- Problem: The manuscript repeatedly states that “|σfrom half| within ∼1σ of |σpred|” indicates consistency with the monopole. σpred is a deterministic scaling (2Δf√N), not a random variable with unit-variance under a known null; comparing “closeness in sigma units” to σpred has no well-defined Type‑I error control. The meaningful test is a one-sample test of proportions versus fP5 (or a two-sample test across classes), not proximity of z-scores to a predicted z.
- Required fix: Replace the “within 1σ of σpred” language with a formally defined test. Either:
  - Use a one-sample test versus fP5 (or fP4) with explicit formula and uncertainty in fP5 propagated; or
  - Use a 4×2 homogeneity χ² (or an exact multinomial test) on {CW,CCW}×{env class} to test equality of proportions across classes directly. Report p-values with multiplicity handling where applicable.

P5-META-M2
- Severity: MAJOR
- Section + page: §V (p. 5), §VI C (p. 6–7), §XI (p. 18)
- Why others missed it: The distinction between global and stratified nulls was not examined.
- Problem: Label-shuffle permutation nulls draw labels globally, ignoring known heterogeneity of label distributions across imaging legs and target programs that the paper itself highlights. This can yield anticonservative p-values if per-leg residuals are real (as argued in the text).
- Required fix: Add stratified label-shuffle nulls that permute labels within strata (at minimum by imaging leg and target program) so the null preserves those marginals. Re-report the permutation p-values for the key scans (redshift, HEALPix, density) under the stratified null. Note any differences.

P5-META-M3
- Severity: MAJOR
- Section + page: §VI C (p. 6–7)
- Why others missed it: Focus was on agreement with monopole, not the quality of the density proxy.
- Problem: The “projected-density” quintiles use k=5 nearest neighbors among spirals on the sky. That proxy is endogenous to the chirality selection (spirals only) and is blind to line-of-sight structure; selection biases with environment (e.g., morphological completeness, target-program mix) can distort it.
- Required fix: Recompute projected-density using a parent, environment-agnostic tracer (e.g., all matched primaries or all ZWARN=0 spectroscopic galaxies) and, better, include a 3D comoving-density proxy using spectroscopic redshifts. Re-run the quintile test; report whether conclusions change.

P5-META-M4
- Severity: MAJOR
- Section + page: §IX A (p. 14–15)
- Why others missed it: They focused on nomenclature and tightening factor but not the estimator bias.
- Problem: In the z-shell correction, the per-shell mean density is computed “over occupied-footprint cells only.” This estimator is biased when the footprint completeness varies within the shell; in LSS work, the selection function is normally estimated via random catalogs. No random-based correction or validation is shown.
- Required fix: Re-estimate per-shell mean density using a random catalog matching the angular/radial selection, or, at minimum, verify with a HEALPix–weighted estimator that varying mask completeness does not bias the shell means. Provide a short robustness check comparing the random-based and “occupied-cells-only” means.

P5-META-M5
- Severity: MAJOR
- Section + page: Global; missing analysis
- Why others missed it: Attention centered on monopole and program splits, not astrophysical covariates.
- Problem: No control for key covariates known to co-vary with environment and chirality classification quality (stellar mass/luminosity, size/resolution, inclination/axis ratio). Without matching or regression, a real environment effect could be masked (or a residual could be selection-induced).
- Required fix: Add a matched or reweighted comparison across environment classes that equalizes at least redshift, size (e.g., Petrosian radius or PSF-normalized size), axis ratio/inclination proxy, and luminosity. Alternatively, include these covariates in a logistic regression of CW as outcome with environment indicators and report adjusted environment coefficients.

P5-META-M6
- Severity: MAJOR
- Section + page: §V A (p. 5) and §VI A/Table II (pp. 6–7)
- Why others missed it: The paper uses “range” descriptively; no one asked for a formal test at the class level.
- Problem: The canonical run’s 1.98 pp “range” across classes is presented without a formal homogeneity test on the same parent set. The Phase‑2 sweep includes a per-cell permutation, but the headline canonical configuration does not provide a permutation-based significance for the inter-class range (or an overall 4×2 χ²).
- Required fix: Add a single omnibus test of equal CW fraction across {void, wall, filament, cluster} for the canonical configuration, either via a 4×2 χ² or via a permutation null that preserves per-class Ns. Report p and a look-elsewhere correction only if you also scan hyperparameters.

P5-META-M7
- Severity: MAJOR
- Section + page: §IX C (p. 16–17) and §XII C (p. 18)
- Why others missed it: They critiqued “independence” phrasing and length; none flagged the apples-to-oranges logic.
- Problem: The comparison to Shamir (2022) claims the present null “leaves no room” for Shamir’s few‑percent amplitude. Shamir’s claim is a global sky asymmetry, not an environment-conditional effect; “no environment dependence” does not falsify a global anisotropy.
- Required fix: Soften this comparison; state explicitly that your null concerns environment-conditional differences and does not adjudicate prior claims of global parity asymmetry measured under different selection, footprint, and methodology.

P5-META-m1
- Severity: MINOR
- Section + page: §IX A (p. 14), code citation
- Why others missed it: Focus was on reproducibility broadly, not this specific citation style.
- Problem: The text cites a local script path “scripts/16 cosmic web zshell corrected.py”. This is not an archival, citable artifact.
- Required fix: Replace by a DOI/versioned repository reference and name the exact script(s) and commit hash used.

P5-META-m2
- Severity: MINOR
- Section + page: §V (p. 5), intervals terminology
- Why others missed it: Considered too minor.
- Problem: The paper calls Jeffreys 95% intervals “exact binomial 95% credible intervals.” Jeffreys intervals are Bayesian credible intervals with a Beta(1/2,1/2) prior, not “exact” in a frequentist sense.
- Required fix: Rename consistently as “Jeffreys 95% credible intervals” or “Jeffreys Bayesian intervals.”

P5-META-m3
- Severity: MINOR
- Section + page: §VI B (p. 6)
- Why others missed it: The regression was only a side remark.
- Problem: The logistic regression result is given as a coefficient (0.0059) without units, scaling, or standard error/p-value. “No significant intercept (0.000652)” is also ambiguous.
- Required fix: Report coefficient, standard error, z/p-value, and the scaling of z (e.g., per unit redshift). Alternatively, remove the regression claim or move it to supplementary material with full details.

P5-META-m4
- Severity: MINOR
- Section + page: §V (p. 5), §VII A (p. 9–10)
- Why others missed it: They discussed thresholds but not the appropriate uncertainty for the “range” statistic.
- Problem: The inter-class “range” is compared to per-class 1σ values; strictly, one should compare pairwise differences with combined uncertainties (√(σi²+σj²)) or bootstrap the range distribution.
- Required fix: Provide a bootstrap CI for the inter-class range under the null, or (preferably) use a single homogeneity test as in P5-META-M6 and relegate “range” to descriptive use.

P5-META-m5
- Severity: MINOR
- Section + page: §III D (p. 3)
- Why others missed it: Considered tangential.
- Problem: The matched-catalog duplicates are resolved “on the chirality side by nearest-separation winner,” but no analogous deduplication is described for DESI targets beyond using zall-pix coadds. Ambiguous multi-associations on the DESI side can, in edge cases, double-count environment labels.
- Required fix: State explicitly the deduplication rule for DESI TARGETIDs (e.g., unique TARGETID per row in zall-pix-iron) and confirm there are no many-to-one matches remaining after the 1″ join.

## Meta-review recommendation
MAJOR REVISIONS

Given the union of all six reviews, there are multiple essential and major blockers: parent-set mismatches in headline figures/tables, contradictory DESIVAST void counts, undocumented unit handling for comoving distances vs h−1 Mpc, statistically ill-defined “σpred proximity” logic, unstratified permutation nulls despite known per-leg residuals, and missing covariate-controlled tests. I count at least 6–8 true blockers that must be addressed for PRD standards. My confidence is moderate that, after these corrections and with a tighter, fully reproducible presentation, the paper could pass external peer review; however, the dependency on an unreviewed companion catalog and several internal inconsistencies must be resolved first.