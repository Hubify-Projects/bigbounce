(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

[MAJOR] §VIII B/E, Table X — The designated primary control is not demonstrably selection matched to the void sample. The “footprint” is an author-constructed union of projected hole-sphere discs and a global radial span, not the DESIVAST/BGS completeness mask, veto mask, fibre-assignment selection, or a random-catalog estimate; the manuscript explicitly acknowledges this but later calls the contrast a “same-selection-function” estimator. The primary result must be recomputed using the actual angular/radial selection function or a per-void matched/IPW control, with balance diagnostics in redshift, sky position, magnitude, size, morphology, imaging leg, and classifier confidence. The near-equality of bright/dark fractions is insufficient: Table XII itself contains a 4.71-pp dark-subsample void/non-void difference, so multiplying the global bright/dark offset by the 0.12-pp difference in program mixture does not bound an environment-by-program interaction. 

ext_P5_M3b

[MAJOR] §V B, Tables X and XIV, and §XV — The estimator called “primary” is not included in the stated Bonferroni-5 primary family. Table X’s headline estimator uses exact membership and a footprint-restricted control, n
void
	​

=57,081, n
nonvoid
	​

=253,276, and Δf
CW
	​

=0.0018; Table XIV instead includes the approximate k=20, unrestricted VoidFinder estimator with n
void
	​

=56,981, n
nonvoid
	​

=621,964, and Δf
CW
	​

=0.0007. The other family members also use different parent samples, including a 145,789-object GALZONE parent. Consequently, the claimed family-wise statement does not cover the headline estimator and is not a simultaneous constraint on a common estimand. A single family with identical support, control construction, and membership conventions must be defined and retabulated.

[MAJOR] §VIII A/B/E — Void membership uncertainty is treated as a small additive systematic although it is severe exposure misclassification. Replacing the any-hole union by maximal-sphere membership removes 36,181 of 57,081 purported void galaxies, approximately 63%, while the sphere-PIS and catalog-native GALZONE definitions produce still different populations. Similar CW fractions under radically different labels do not establish robustness; they can instead reflect attenuation of a true environmental effect toward zero. The authors need a physically justified primary membership definition and an injection-recovery or latent-class analysis quantifying how membership purity and completeness affect sensitivity.

[MAJOR] Table XI and §XII B — The quoted “honest effective 2σ” 0.9-pp envelope has no valid statistical coverage. A 95% counting interval is added in quadrature to maxima from correlated analysis variants that are neither standard deviations nor draws from specified nuisance distributions. Several terms do not even measure the headline contrast: the confidence and match-radius values in §XI are shifts in the catalog-wide f
CW
	​

, the RSD value is obtained for the unrestricted rather than primary estimator, and the sphere-PIS/GALZONE comparison changes both algorithm and parent population. Moreover, §V B derives a wider 1.12-pp simultaneous half-width, contradicting the instruction that model builders use the tighter 0.9-pp value. A joint likelihood, bootstrap, or Bayesian nuisance model is required; otherwise only the counting interval and individual sensitivity variations should be reported separately.

[MAJOR] §V B and §XV — The post-hoc primary designation and statistical interpretation are not acceptable for the stated exclusion claim. Bonferroni correction controls false discoveries; failure of five tests to reject does not establish a “family-wise null,” equivalence, or an upper bound with controlled type-II error. Because DESIVAST was selected after examining multiple classifiers, controls, geometries, thresholds, and stratifications, the DR1 result must be presented as exploratory. A quantitative null claim requires a prespecified equivalence margin, power calculation, and simultaneous confidence region; a confirmatory exclusion requires an independent data set or the proposed preregistered DR2 analysis.

[MAJOR] Appendix A, §XII B, and §XIII — The conversion from classifier-labelled chirality to a 2.26-pp physical-chirality bound is unsupported. A uniform monopole cancels only if sensitivity and specificity are environment independent, whereas the void-stratified validation has only 933 objects and permits directional error asymmetries of several percentage points, much larger than the claimed 0.9-pp label bound. The calculation also combines a 69.91% “accuracy floor” with error symmetry inferred from a different 91.2%-accuracy confident subset, without propagating uncertainty in either quantity. The outcome labels come from an unpublished companion manuscript whose training-set independence and possible GZ1 overlap are not established here. Until a strictly held-out, environment-stratified confusion matrix and measurement-error model are supplied, the result can only be stated for the particular classifier labels, not physical handedness.

[MAJOR] §VIII B and Tables X–XIV — The two-sample binomial standard errors assume independent galaxies, although void galaxies are clustered within the same voids, sky regions, imaging conditions, and overlapping hole systems. Even weak within-region classifier correlations can materially inflate the uncertainty at this sample size. The duplicate-TARGETID checks performed for the secondary T-Web analysis do not address this issue. The primary inference should use cluster-robust errors or a block bootstrap/jackknife over independent voids and sufficiently large HEALPix/imaging regions, with overlapping-void membership handled explicitly.

[MAJOR] §VIII, Table XI, and §XIII — The claimed RSD bound is not an end-to-end reconstruction test. Independently perturbing galaxy distances while holding the published void catalog fixed tests only one imposed, label-independent displacement model; moving galaxies and void centers using an assumed universal profile without rerunning the void finder does not reproduce how the catalog, survey boundaries, and void hierarchy change between redshift and real space. Such perturbations cannot bound an RSD-related bias correlated with galaxy properties or chirality classification. The 0.024-pp “40× below the envelope” statement should be removed unless supported by realistic mocks in which voids are independently identified in real and redshift space; otherwise the result should remain explicitly a redshift-space-only measurement.

[MAJOR] §§IV, VI, VII, and IX A — The canonical T-Web field is not a valid physical environment reconstruction. The random-catalog-weighted rebuild changes the void volume fraction from 17.6% to 0.75% and retains the class label of only 26.6% of matched spirals, demonstrating that the original classes are dominated by the survey selection function. Hyperparameter and grid tests of that contaminated field do not establish robustness, and obtaining a null after repartitioning a sample whose chirality fraction is nearly constant is not independent validation. The selection-corrected/random-weighted reconstruction must become the sole T-Web analysis, with its own convergence and boundary tests, or the extensive canonical T-Web claims should be removed.

[MAJOR] Abstract, §XII B, §XV, and Appendix B — No forward model connects a bounce- or inflation-generated parity-violating field to the observed projected CW fraction conditional on DESIVAST membership. The primary DESIVAST analysis also has no unique 25 Mpc/h smoothing scale, so the T-Web smoothing scale cannot be assigned to its bound. Appendix B explicitly introduces a non-covariant, dimensionally incomplete toy operator with no transfer function to galaxy angular momentum. The manuscript therefore does not presently constrain a bounce or inflation model; it supplies, at most, an empirical catalog-level null test. The model-exclusion language and instruction to model builders should be removed unless a concrete, calculable model prediction is provided.

[MINOR] Throughout — Terminology and internal consistency require correction. V2-REVOLVER and V2-VIDE are two pruning prescriptions within the same watershed family and should not be called independent algorithms; “no rejection after Bonferroni correction” should replace “family-wise null”; equality of environmental fractions should not be described as parity; and Appendix A calls f
CW
	​

=0.4838 a CW excess although it is a CW deficit. Exact and k=20 memberships must also be kept distinct in every abstract, table, and conclusion.

[MINOR] Organization — The 42-page manuscript is excessively repetitive for the result presented. The invalid canonical T-Web analysis, most scan-by-scan diagnostics, the speculative EFT appendix, AI-pipeline narrative, and artifact inventories should be moved to supplementary material; the main text should focus on one properly controlled primary estimator, its validation, and a statistically interpretable uncertainty statement.

(3) No—the data support only an exploratory non-detection for the chosen classifier labels and author-defined redshift-space memberships, not the stated 0.9-pp classifier-label bound or 2.26-pp physical-chirality constraint.
