VERDICT: MAJOR REVISIONS

ISSUES:

[MAJOR] §VIII B/E, “footprint-restricted” primary estimand: The control is not selection-function matched. The adopted “footprint” is an author-constructed union of void-hole angular discs intersected with their radial span, rather than the published DESIVAST/BGS completeness mask or a DESI-random-catalog estimate. It is also endogenous to the detected voids. The manuscript acknowledges this limitation but later states that the restriction “matches the void and control selection functions directly,” which is incorrect. The primary contrast must be recomputed with the official mask/randoms or with per-void angular-and-redshift-matched controls. 

ext_P5_M14

[MAJOR] §VIII B/XI, primary confounder adjustment: No covariate-adjusted estimate is actually supplied for the DESIVAST headline result; the manuscript explicitly substitutes program splits and a collection of sensitivity checks for the required regression or matching analysis. Void and non-void spirals may differ in redshift, magnitude, angular size, morphology, inclination, imaging depth, classifier confidence, and imaging leg, all of which can affect classification errors. A logistic, inverse-probability-weighted, or matched-control analysis—with balance diagnostics and a robust confidence interval for the void coefficient—is necessary before interpreting the raw fraction difference as environmental.

[MAJOR] §V B and Tables IV/XIV, post-hoc primary designation and multiplicity: The primary estimator was selected after examination of the data. More importantly, the exact footprint-restricted headline estimator, n
void
	​

=57,081 versus n
nonvoid
	​

=253,276, is not one of the five estimators in Table XIV; that table instead uses the unrestricted k=20 VoidFinder result. The GALZONE rows also use a different 145,789-object parent. Consequently, the stated Bonferroni-5 family does not cover the actual headline estimator and combines different target populations and estimands rather than five replications of one test. The DR1 result must be presented as exploratory, with the complete selection procedure included in the inferential accounting, or confirmed using a genuinely pre-specified independent dataset.

[MAJOR] §VIII B, Table XI, and Eq. (4), claimed “effective 2σ” envelope: The 0.9-percentage-point envelope has no calibrated frequentist or Bayesian coverage. It combines a counting-statistics 95% half-width, maximum shifts under alternative definitions, control-population changes, and model-dependent perturbations in quadrature, implicitly treating them as independent, zero-mean Gaussian uncertainties with a common confidence interpretation. Several terms are strongly correlated and some are alternative estimands, not random errors. Even accepting the quoted 0.94-pp half-width, centering it on the measured +0.181 pp gives an upper absolute endpoint of approximately 1.13 pp, not 0.9 pp; this is consistent with the manuscript’s own approximately 1.1-pp simultaneous-family result. The advertised 0.9-pp exclusion must therefore be withdrawn or replaced by a statistically defined uncertainty construction.

[MAJOR] §V and §VIII, independence and cosmic-variance assumptions: The two-sample binomial errors treat tens of thousands of galaxies as independent Bernoulli trials. Galaxies share voids, large-scale structures, imaging fields, observing conditions, and classifier systematics, while physical spin correlations can also produce overdispersion. Global label shuffling destroys precisely these correlations and may yield an anticonservative null. The analysis needs cluster-robust or hierarchical inference, spatial block permutations, bootstrap resampling by independent void/void complex and survey region, and leave-one-void-out tests; the number of distinct voids contributing galaxies and their leverage distribution should be reported.

[MAJOR] Appendix A, §XII B, and the abstract, de-attenuated 2.26-pp physical bound: Dividing by 2a−1 is justified only for a known, symmetric, non-differential misclassification process. The quoted 69.91% accuracy is a global “floor,” not a calibrated accuracy for the primary void and non-void samples, and its uncertainty is not propagated. The manuscript’s own void-stratified GZ1 test has an error-asymmetry interval with a roughly 3.7-pp half-width, far larger than the claimed sub-percent label constraint, so it cannot exclude differential classification error at the relevant scale. Without an environment-specific errors-in-variables model, the result is only a bound on the particular classifier labels; the statement that model builders should use 2.26 pp is unsupported.

[MAJOR] §VIII, VoidFinder membership and redshift-space-distortion treatment: The any-hole union is an author-defined permissive proxy rather than an official per-galaxy VoidFinder membership, and the maximal-sphere alternative changes the contrast by 0.60 pp, already comparable to the claimed bound. Independently perturbing already redshift-space galaxy distances with Gaussian offsets is not an unbiased real-space reconstruction and can double-count existing distortions. Likewise, moving galaxies and published holes together without reconstructing the tracer density and rerunning VoidFinder does not bound changes in the void catalog itself. The 0.024-pp shift cannot be represented as a rigorous upper bound on the dominant RSD systematic; either retain a strictly fixed-redshift-space result or perform a consistent reconstruction followed by a complete void-finder rerun.

[MAJOR] §IV and §IX A, secondary T-Web classification: The canonical T-Web field is constructed from unweighted galaxy counts with a global mean despite a strongly varying radial and angular selection function. The manuscript’s own randoms-weighted rebuild changes approximately 73% of matched-galaxy class assignments and reduces the void volume fraction by a factor of about 23. This demonstrates that the canonical classes substantially trace the survey window rather than a stable physical environment. Hyperparameter sweeps of that uncorrected field do not establish physical robustness. The T-Web analysis should be rebuilt from tracer-appropriate random catalogs with controlled boundary conditions or removed from the principal conclusions and reduced to an appendix diagnostic.

[MAJOR] §I, §XII B, and Appendix B, fundamental-physics interpretation: No concrete bounce or inflation model is shown to predict the measured statistic, and the primary DESIVAST void estimator does not possess the single 25h
−1
Mpc smoothing scale attributed to the claimed model constraint. In addition, for the stated pseudoscalar ϕ, both ∇ϕ⋅∇ρ and 
L
^
⋅
∇ρ
	​

 are parity odd, so their product in the proposed toy operator is parity even, contrary to the text. The data measure projected arm-winding labels rather than 
L
^
 directly, and no calibrated kinematic/trailing-arm transfer function is supplied. Appendix B and the bounce/inflation exclusion language should be removed unless replaced by a covariant model and an explicit model-to-observable calculation.

[MAJOR] §II, §XIII, and Appendices A/D, dependence on Paper IV: The per-galaxy labels, classifier validation, monopole interpretation, and relevant confusion matrices depend on a concurrently submitted manuscript whose arXiv identifier remains a placeholder, while the archival DOI is also pending. These inputs are central even though a spatially uniform additive offset cancels in a simple contrast. The present manuscript cannot be accepted until Paper IV is available for coordinated review and the exact catalog, weights, code, intermediate memberships, configuration, and immutable archive identifiers are publicly frozen and independently reproducible.

[MAJOR] Abstract, §XII C, and Conclusions, inconsistent exclusion statements: The claim that the analysis leaves “no room” for a 2–4-pp physical asymmetry is inconsistent with the manuscript’s own attenuation argument. With attenuation near 0.40, a 2-pp physical contrast would appear as approximately 0.8 pp in the labels, which is not excluded by either the stated 0.9-pp envelope or the more defensible approximately 1.1-pp simultaneous scale. The lower end of the cited Shamir amplitude therefore remains open under the manuscript’s own assumptions. All such comparative and “model-builder” statements must be recalculated after the statistical bound is corrected.

[MINOR] §III and §VIII, sample definition: A spiral-galaxy analysis should normally restrict the spectroscopic counterpart to SPECTYPE==GALAXY, or explicitly quantify low-redshift QSO/interloper contamination and demonstrate that it is irrelevant. The matched chirality sample is flux limited even though the DESIVAST tracer catalog is volume limited; repeated descriptions of the analyzed spirals as a “volume-limited BGS sample” should be corrected. A complete sample-flow table and void/non-void distributions in redshift, magnitude, size, morphology, confidence, and survey leg should be added.

[MINOR] Presentation throughout: The 42-page manuscript is highly repetitive and repeatedly uses advocacy terms such as “honest,” “clean,” “load-bearing,” and “strictly quotable.” The main paper should be substantially shortened, alternative T-Web configurations and artifact maps moved to supplementary material, and all parent-sample, membership, sign-convention, scale, and bound statements made consistent across the abstract, tables, discussion, and conclusions.

The central qualitative claim of no detected void-versus-non-void difference in the reported classifier labels is supported by the tabulated counts, but the quantitative 0.9-pp classifier bound, the 2.26-pp physical bound, and the claimed bounce/inflation interpretation are not.
