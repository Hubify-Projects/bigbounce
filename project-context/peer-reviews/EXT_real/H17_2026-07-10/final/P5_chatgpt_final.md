(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

[MAJOR] §VIII B–E and Table X, “footprint-restricted primary estimand”: The control sample is not restricted with the published DESIVAST/BGS angular and radial selection mask or DESI random catalogs. The adopted “footprint” is a bespoke union of the angular projections of detected hole spheres intersected with their radial span; it is conditioned on where voids were found and does not match fibre completeness, imaging depth, target selection, or radial completeness. The manuscript explicitly acknowledges this but nevertheless describes the result as a same-selection-function estimand. The primary contrast must be recomputed with the official mask and randoms, or with per-void controls matched in redshift, sky position, and observational selection. 

h17c_P5

[MAJOR] §VIII B, the paragraph “Adjustment in lieu of a full covariate regression,” and Appendix A: No covariate-adjusted analysis is performed for the primary DESIVAST contrast. Balancing only the bright/dark program fraction does not control differences in redshift, apparent magnitude, angular size, surface brightness, morphology, inclination, classifier confidence, imaging leg, or local image quality, all of which can affect chirality-label errors and can vary with environment. The T-Web regression in §VI uses a different environment definition and parent sample and cannot validate the DESIVAST estimator. A split table and an informal systematic budget are not substitutes for a DESIVAST-specific regression, matching analysis, or inverse-probability-weighted estimate. The statement that the catalog monopole “cancels exactly” is valid only for a spatially and environmentally uniform additive bias, not for differential sensitivity or specificity.

[MAJOR] §V B and Tables X, XIII, and XIV, definition of the Bonferroni-5 primary family: The stated primary estimator—exact VoidFinder membership with the footprint-restricted control, n
void
	​

=57,081, n
nonvoid
	​

=253,276, Δf
CW
	​

=0.0018—is not one of the five rows in Table XIV. It is replaced there by the approximate k=20, unrestricted-control estimator with n
void
	​

=56,981, n
nonvoid
	​

=621,964, and Δf
CW
	​

=0.0007. The other rows also use different parents: the sphere-PIS estimators use the 678,945-object low-redshift sample, whereas the GALZONE estimators use a 145,789-object catalog-valid parent. The analysis therefore contains at least six contrasts and does not define a five-test family of measurements of one common estimand. The family, estimand, parent population, and membership rule must be made consistent before multiplicity correction or simultaneous bounds are quoted. 

h17c_P5

[MAJOR] §V B and §XV, “family-wise null” and “environment-independence bound”: Failure of five tests to reject zero after Bonferroni correction establishes only that none reaches the corrected significance threshold; it is not a family-level demonstration of equivalence or independence. A quantitative null claim requires a pre-specified equivalence margin and an equivalence test, or simultaneous confidence intervals stated without “accepting” the null. The exact primary counting-only interval already extends from −0.27 to +0.64 percentage points, while the manuscript’s widest Bonferroni interval has an absolute endpoint of approximately 1.12 percentage points. These are materially different statements from a uniform ∣Δf
CW
	​

∣≲0.9 percentage-point exclusion.

[MAJOR] Table XI and §VIII B, construction of the “≈0.9 pp effective 2σ systematic envelope”: The quadrature has no defensible statistical interpretation. It combines a two-sided counting-interval half-width with maximum shifts from alternative definitions, finite Monte Carlo extrema, and changes of target population, while assuming independence without evidence. Membership, hole-versus-maximal-sphere geometry, and sphere-PIS-versus-GALZONE differences are strongly related rather than independent Gaussian nuisance parameters. The confidence-threshold and match-radius values cited in §XI are changes in the catalog-wide f
CW
	​

, not demonstrated changes in the primary void-minus-nonvoid contrast. Even if the listed terms were combined mechanically, the resulting approximately 0.95-percentage-point quantity is a half-width; centered on the observed +0.18-percentage-point estimate, it permits a positive excursion of approximately 1.13 percentage points. The quoted 0.9-percentage-point bound therefore has neither a defined coverage probability nor the stated numerical meaning. 

h17c_P5

[MAJOR] §V and §VIII, uncertainty on the primary contrast: The two-sample binomial standard error treats every galaxy as an independent Bernoulli observation. Void galaxies are clustered within a finite number of voids, and both chirality labels and sample completeness can be correlated over imaging regions and observing programs. No void-level, sky-block, or spatially clustered uncertainty estimate is reported for the primary statistic. The analysis needs a bootstrap or jackknife over voids and independent sky regions, or a hierarchical/cluster-robust model, with the nonvoid controls resampled in corresponding spatial and redshift blocks. Until then, the quoted z
Δ
	​

, confidence interval, and sub-percent precision may be substantially too optimistic.

[MAJOR] Abstract, §XII B, and Appendix A, conversion to a 2.26-percentage-point physical-chirality bound: Dividing by 2a−1 is valid only under a nondifferential symmetric-error model with the same sensitivity and specificity in void and nonvoid samples. The manuscript has no void-stratified human-label confusion matrix, and agreement of error asymmetry across imaging-leg and confidence strata does not establish invariance across environment, redshift, morphology, or surface brightness. Moreover, the adopted 69.91% “floor” and the 91.2–96.1% accuracies reported on the confident GZ1 overlap describe different selected populations and cannot be interchanged as a calibrated transfer function. The 2.26-percentage-point number is therefore a heuristic, not an observational bound, and the recommendation that model builders use it must be removed unless environment-stratified sensitivity and specificity are measured. 

h17c_P5

[MAJOR] §VIII, RSD treatment, and the membership term in Table XI: Independently perturbing only the test galaxies along the line of sight while holding the void centers, radii, and void-defining tracer population fixed is not a simulation of redshift-space distortions. The resulting roughly 34% increase in void membership demonstrates strong asymmetric boundary scattering, not a calibrated RSD uncertainty. The maximum shift observed in 200 such realizations cannot be entered as a 2σ nuisance term. For the stated fixed-redshift-space result, this exercise should be presented only as a membership sensitivity test; an RSD uncertainty requires mocks in which the tracer catalog is distorted and the void finder is rerun, or a reconstructed-position analysis.

[MAJOR] §IV, §VII, and §IX A, T-Web corroboration and the breadth of the conclusion: The manuscript’s own random-catalog-weighted rebuild changes the void volume fraction from 17.6% to 0.75% and reassigns approximately 73% of matched galaxies, demonstrating that the canonical T-Web classes are dominated by the survey selection function and mask geometry. Hyperparameter stability around that uncorrected field is not evidence of physical environment robustness, and obtaining a null after replacing most environment labels does not validate either classifier. The canonical T-Web analysis should not be cited as corroborating evidence. Unless a selection-corrected T-Web field is validated independently, the conclusion must be restricted to the average DESIVAST binary void-versus-nonvoid classifier-label contrast; that binary contrast cannot exclude opposite or nonmonotonic effects among walls, filaments, and clusters.

[MAJOR] §II, Appendix A, and Appendix D, dependence on Paper IV and reproducibility: The per-galaxy handedness labels are load-bearing, yet the companion paper still has a placeholder arXiv identifier and the archival DOI is stated to be pending. The appendix summarizes the classifier but does not permit full assessment of training leakage, pseudo-label dependence, calibration, selection-dependent errors, or the final catalog version. Review must be coordinated with the final Paper IV manuscript, and the exact label catalog, weights, code, configuration, checksums, and primary-analysis tables must be frozen in an immutable archive at submission rather than promised for acceptance.

[MINOR] §III C–D and Table XIX, angular cross-match validation: The match-radius sensitivity table uses pre-deduplication rows, whereas the primary analysis is one row per TARGETID, and no random-coordinate or shifted-catalog estimate of the false-association rate is supplied. The radius sweep should be repeated after the same one-to-one deduplication used in the primary sample, with the ambiguity rate and expected number of chance matches reported.

[MINOR] Appendix B, toy EFT mapping: The proposed operator has no derived transfer function, normalization, or specified dimensional convention for g
ϕ
	​

, and the manuscript concedes that it is noncovariant and gauge-dependent. Consequently, the quoted coupling scaling does not follow from the data and should be removed from the main paper or retained only as explicitly non-inferential supplementary speculation.

(3) The evidence supports only an unadjusted non-detection in the classifier-labelled sample under the manuscript’s bespoke DESIVAST membership and control construction; it does not support the stronger environment-independence claim or the quoted 0.9-percentage-point classifier-label and 2.26-percentage-point physical bounds.
