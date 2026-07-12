VERDICT: MAJOR REVISIONS

ISSUES:

[MAJOR] Section VIII B, “primary estimand”: the purported same-footprint control is not based on the published DESIVAST/BGS selection mask or random catalog, but on an author-constructed union of void-hole angular discs and a radial span; the manuscript itself concedes that this does not match fiber completeness, imaging depth, vetoes, or radial selection. The resulting contrast is therefore “inside holes versus other galaxies in a data-derived geometric support,” not a demonstrated void-versus-non-void comparison under a common selection function. The primary analysis must be repeated using the official valid-volume mask/randoms or a per-void angular-and-redshift-matched control. 

ext_P5_RS2b

[MAJOR] Sections VIII B and VIII D, population definition: the VoidFinder analysis starts from all 678,945 matched objects at z≤0.24, whereas the catalog-native GALZONE analyses use only a 145,789-object valid BGS parent. Merely imposing the DESIVAST redshift limit does not reproduce the volume-limited tracer selection or valid survey volume. The five rows therefore estimate materially different population contrasts, and they cannot be interpreted as interchangeable measurements of one common physical parameter without a harmonized parent sample.

[MAJOR] Section VIII B, “adjustment in lieu of a full covariate regression”: no acceptable adjustment is actually performed for the primary result. Similar bright/dark fractions and a collection of one-dimensional systematics checks are not substitutes for controlling redshift, angular completeness, imaging leg, magnitude, angular size, surface brightness, morphology, inclination, classifier confidence, and local crowding. This is particularly important because the manuscript finds a large inside/outside-footprint change in the classifier monopole. A covariate-balanced, stratified, regression, matching, or inverse-probability-weighted primary estimate is required.

[MAJOR] Section V B and Table XIV, multiplicity claim: the exact footprint-restricted estimator designated as primary is not one of the five estimators in the advertised Bonferroni-5 table; the listed VoidFinder member is instead the approximate k=20, unrestricted-control result. Moreover, the family combines sphere approximations and catalog-native memberships with different control populations. The phrase “family-wise null” is also statistically misleading: Bonferroni non-rejection does not establish equivalence or independence. A single estimand should be fixed, and any affirmative bound should use a prespecified equivalence margin and simultaneous confidence interval.

[MAJOR] Table XI and Sections VIII B/XII, systematic envelope: the quoted ≃0.9 percentage-point “effective 2σ” bound has no valid coverage interpretation. It combines a 95% statistical half-width with maxima from heterogeneous sensitivity exercises, assumes approximate independence although the terms reuse the same galaxies and void catalogs, and treats differences between distinct scientific estimands as random errors. In addition, the confidence-threshold and match-radius entries are derived from shifts in the catalog-wide f
CW
	​

 in Table XIX, not from recomputed shifts in the primary void/non-void Δf
CW
	​

. The envelope must either be replaced by a principled nuisance-parameter or resampling analysis or described only as an informal sensitivity range.

[MAJOR] Section V and the primary two-sample tests: the reported standard errors treat tens of thousands of galaxy labels as independent Bernoulli draws. Galaxies share voids, sky regions, imaging conditions, reduction artifacts, and potentially intrinsic spin correlations, so ordinary binomial errors can substantially overstate the effective sample size. The primary intervals and tests need void-level and sky-region block bootstrap/jackknife estimates, or a hierarchical/cluster-robust model; the HEALPix diagnostics elsewhere do not validate the galaxy-level binomial variance for this contrast.

[MAJOR] Appendix A and Section XII B, classifier-to-physics conversion: dividing the label-space bound by 2a−1 is justified only under nondifferential, environment-independent, symmetric misclassification and comparable CW/CCW-to-NS selection. The manuscript combines a 69.91% accuracy floor from one population with error symmetry measured in a much more accurate, selected GZ1 subset, while its own void-arm calibration allows directional-error differences of several percentage points—far above the claimed sub-percent bound. Environment-dependent selection into the CW/CCW subset is also not tested. The 2.26 percentage-point physical-chirality limit is therefore unsupported and should be removed unless an environment-stratified confusion/selection model is supplied.

[MAJOR] Sections II and VIII F, “monopole cancellation”: an exactly constant additive label offset cancels algebraically, but the manuscript itself demonstrates spatial and target-program variation in f
CW
	​

. Such differential classifier errors do not cancel when void and control samples have different redshift, morphology, image quality, or angular distributions. The current arguments establish invariance only to an artificial scalar-offset model, not to the relevant environment-correlated measurement bias.

[MAJOR] Section VIII, RSD robustness: random line-of-sight perturbations with fixed published holes and the subsequent first-order displacement of galaxies and holes do not bound the effect of redshift-space distortions on a void catalog whose centers, radii, merging, and inclusion are themselves inferred in redshift space. The void finder is never rerun, and membership changes by roughly 25–34%, which may attenuate a real contrast even when the measured null remains stable. The reported 0.02 percentage-point RSD term should not enter a quantitative error budget without reconstruction followed by full catalog regeneration or a validated injection-recovery calculation.

[MAJOR] Sections IV, VII, and IX A, T-Web analysis: the random-catalog-weighted rebuild changes approximately 73% of matched-galaxy class assignments and reduces the void volume fraction by about a factor of 23, demonstrating that the canonical T-Web field is dominated by the survey selection function. A null obtained after applying several radically different or weakly related labels is not evidence that the original labels trace physical environment. The canonical T-Web results, Phase-2 sweep, and cross-catalog concordance should either be replaced by a properly selection-corrected analysis with a validated mask or reduced to a brief diagnostic that carries no physical robustness claim.

[MAJOR] Appendix B and Sections XII B/XV, fundamental-physics interpretation: no bounce or inflation model is shown to predict the measured observable, and no projection is derived from a local spin/environment interaction to apparent sky-plane CW/CCW counts. The proposed operator is explicitly non-covariant and, for the stated pseudoscalar ϕ, both ∇ϕ⋅∇ρ and 
L
^
⋅
∇ρ
	​

 are parity odd, making their product parity even rather than establishing the claimed parity-violating interaction. The toy EFT appendix and model-exclusion language should be removed or replaced by a consistent, dimensionally and symmetry-complete calculation.

[MAJOR] Sections II, XIII, and Appendices A/D/E, dependency and reproducibility: the essential chirality labels, training validation, and provenance belong to an unresolved companion submission with an arXiv placeholder, while the archival DOI is also pending. A referee cannot independently validate the principal measurement input from the present manuscript alone. Review and any acceptance must be contingent on simultaneous access to the final Paper IV manuscript, immutable label catalog, trained weights, exact commit, and archived intermediate tables used for the primary contrast.

[MINOR] Sections VIII B, XII B, and XV contain inconsistent quantitative summaries: the superseded 0.5–0.6 percentage-point language remains alongside the 0.9 percentage-point envelope; the counting-only discussion sometimes uses the unrestricted k=20 interval rather than the declared exact-footprint interval; and the “all five” family is variously attributed to Tables XIII and XIV. All headline numbers and estimator labels must be reconciled.

[MINOR] Sections III/XI: objects with DESI SPECTYPE=QSO are included in a sample repeatedly described as spirals, but no galaxy-only sensitivity result is given. Match-radius and confidence tests should also be reported for the primary Δf
CW
	​

, rather than only for the catalog-wide CW fraction.

[MINOR] Presentation throughout: the manuscript is substantially overlong and repetitive, includes unresolved citation/DOI placeholders and stale drafting language, and contains figure/caption and artifact-numbering inconsistencies, including an A1–A32 description for a table extending through A34. The secondary material should be sharply condensed after the primary estimator and its limitations are made coherent.

The central claim is supported only as an unadjusted descriptive non-detection in the chosen classifier-labelled samples, not as evidence of physical environment independence or as the quoted 0.9- or 2.26-percentage-point bound.
