(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

[MAJOR] §VIII B/E, “footprint-restricted primary estimand”: the footprint is an author-constructed union of void-hole angular discs intersected with a radial span, explicitly not the published DESIVAST/BGS completeness mask or a random-catalog selection function. It therefore does not ensure comparable redshift, imaging depth, fibre completeness, magnitude, size, inclination, morphology, or classifier-confidence distributions between void and non-void galaxies. The later description of this estimator as “same-selection-function” directly contradicts the manuscript’s own caveat. The primary result must be recomputed using the official survey mask/randoms and a redshift- and imaging-matched control, inverse-probability weighting, or a prespecified covariate-adjusted model, with quantitative balance diagnostics. 

ext_P5_M25

[MAJOR] §V B, Tables IV and XIV, and §XV, multiplicity bookkeeping: the primary estimator is designated after examining the data, and the advertised Bonferroni-5 family is not consistently defined. The headline estimator is the exact, footprint-restricted, k-unbounded VoidFinder contrast, whereas Table XIV includes the unrestricted k=20 VoidFinder contrast; maximal-sphere membership, exact-versus-k=20 membership, footprint construction, confidence cuts, and other analysis choices add further trials. Consequently, K=5 does not cover the actual selection process, and the quoted simultaneous bound is not a valid post-selection confidence statement. A genuinely held-out or preregistered analysis is needed, or all bounds must be labelled exploratory and corrected over the full analysis tree. 

ext_P5_M25

[MAJOR] §VIII B and Table X, uncertainty estimation: the two-sample binomial standard error treats all galaxies as independent Bernoulli trials. Galaxies share voids, large-scale structures, imaging conditions, sky calibration, and potentially correlated spin or classifier residuals; the effective independent units may be closer to voids or sky regions than to individual galaxies. Label shuffling does not reproduce spatially correlated classification errors. The primary confidence interval and every derived upper limit must be recomputed with void-clustered resampling, spatial block bootstrap or jackknife, and preferably survey mocks carrying the angular selection and classifier systematics. 

ext_P5_M25

[MAJOR] Table XI and Eq. (4), “effective 2σ” envelope: the quadrature sum combines a nominal 95% statistical half-width with deterministic shifts produced by alternative definitions and stress tests. These quantities are not demonstrated to be independent, Gaussian, zero-mean, or even estimates of the same nuisance parameters; membership, geometry, sphere-versus-GALZONE, and RSD terms are substantially overlapping. The resulting 0.9 percentage-point number has no demonstrated frequentist coverage or Bayesian credibility. The authors must construct a covariance-aware nuisance model or calibrated injection/mocking analysis; otherwise the shifts should be reported only as a non-probabilistic sensitivity range, not an exclusion bound. 

ext_P5_M25

[MAJOR] §VIII C–D and Table XIV, heterogeneous estimands: the five “void definitions” do not operate on a common target population or common support. The sphere-PIS analyses use the 678,945-object low-redshift sample, while the GALZONE contrasts use a 145,789-object catalog-valid parent; moreover, effective-radius spheres are not equivalent to the irregular watershed zones, and the VoidFinder any-hole union is an author-defined permissive proxy. Agreement of null p-values across these rows is not evidence for algorithmic robustness of a single estimand. The analysis should use official memberships and masks on a common valid population, or present the estimates separately without deriving a joint physical bound.

[MAJOR] Appendix A and §§XII B–XIII, de-attenuated “physical-chirality” bound: dividing by 2a−1 is valid only for a binary classifier with symmetric, non-differential sensitivity and specificity operating identically in both environments. Here the sample is selected through a three-class CW/CCW/NS classifier, hard argmax labels, environment-dependent morphology and confidence distributions, and possible non-spiral contamination. The void-stratified GZ1 validation has only 933 void objects and a directional-error-asymmetry interval of approximately ±3.7 percentage points, far wider than the claimed sub-percent labelled bound. The 2.26 percentage-point physical limit is therefore unsupported; it requires an environment-stratified confusion model, uncertain sensitivity/specificity, selection into the spiral sample, and end-to-end signal injection and recovery. 

ext_P5_M25

[MAJOR] §II and §VIII F, classifier-monopole cancellation: a spatially uniform additive label offset cancels algebraically in a difference, but environment-dependent sensitivity, specificity, thresholding, or contamination does not. The manuscript itself reports confidence-, target-program-, and sky-dependent residuals, while the void and control populations are not shown to be distributionally matched. Thus the primary statistic may be independent of the numerical value of the Paper IV monopole, but it is not independent of Paper IV’s classification systematics. The claim must be narrowed accordingly and supported by direct differential-error calibration.

[MAJOR] §§XII B and XV and Appendix B, observable-to-theory mapping: apparent clockwise/counterclockwise winding is a two-dimensional, line-of-sight-dependent image property, not directly the sign of an intrinsic angular-momentum pseudoscalar. The mapping omits viewing geometry, the leading-versus-trailing-arm ambiguity, inclination selection, and the relation between the observer’s line of sight and the local density gradient. In addition, the primary DESIVAST analysis spans heterogeneous void sizes and is not a measurement at a unique 25Mpc/h smoothing scale. The bounce/inflation and toy-EFT claims should be removed unless a quantitative transfer function from a specified physical model to this projected observable is supplied. 

ext_P5_M25

[MAJOR] §§IV and IX A, secondary T-Web reconstruction: the canonical field uses a global mean density in a strongly redshift-dependent survey, a zero-padded thin survey volume, no initial random-catalog correction, and 25.9Mpc/h cells for R
s
	​

=25Mpc/h. The manuscript’s own random-weighted rebuild changes roughly 73% of galaxy labels and reduces the void volume fraction by a factor of about 23, demonstrating that the canonical classes largely trace the selection function. This analysis cannot be cited as physical corroboration; it should either be removed from the evidence chain or replaced by the properly random-weighted, adequately resolved reconstruction with full convergence and window-function tests. 

ext_P5_M25

[MAJOR] §VIII and Table XI, RSD uncertainty: the quoted 0.02 percentage-point reconstruction shift does not represent the full RSD uncertainty because the void catalog is not rerun on the reconstructed density field. The fixed-geometry Gaussian perturbation and the coherent profile displacement test address different, incomplete pieces of the problem and cannot be treated as independent calibrated nuisance terms. The paper should remain explicitly a redshift-space measurement, or provide end-to-end reconstructed mocks in which the tracer catalog, void finding, membership, and chirality estimator are all rerun.

[MAJOR] §XIII and Appendices D–E, provenance and reproducibility: the central CW/CCW labels depend on a concurrently submitted, unrefereed companion paper; the manuscript contains placeholder arXiv and DOI fields and states that the archival snapshot will be minted only later. Moreover, the currently exposed model card identifies Paper IV v1.0.128, whereas the dataset card identifies v1.0.123, rather than one unambiguous revision tied to this manuscript. 
Hugging Face
+1
 Acceptance requires coordinated review of Paper IV and a DOI-pinned snapshot containing the exact label catalog, weights, code, configuration, intermediate membership tables, and checksums used for every reported number.

[MAJOR] §§I, XII B, and XV, PRD significance and scope: the manuscript explicitly states that no bounce or inflation model predicts the tested environmental signal, while the only proposed theoretical mapping is acknowledged to be non-covariant and heuristic. As written, the bounce/inflation framing does not follow from the empirical analysis and overstates the physics reach of a catalog-level null test. The authors must either motivate and test a quantitatively specified model or reframe the work as an astronomical systematics and catalog analysis without claiming a constraint on bounce-versus-inflation physics.

[MINOR] §III C, cross-match validation: because both catalogs inherit Legacy Survey astrometry, matching should preferentially use the shared Tractor identifiers rather than nearest-neighbour sky position. At the claimed sub-percent precision, the authors should report a shifted-coordinate false-match test, resolve all one-to-many cases explicitly, and repeat the primary analysis with SPECTYPE restricted to GALAXY rather than retaining spectroscopic QSOs.

[MINOR] Statistical terminology throughout: “consistent with parity” should be replaced by “no detected difference in classifier-labelled CW fractions,” because the primary null is f
CW
void
	​

=f
CW
nonvoid
	​

, not f
CW
	​

=1/2. Failure to reject this null does not establish environmental independence, and the sign convention Δf
CW
	​

=f
CW
nonvoid
	​

−f
CW
void
	​

 should be stated identically in the abstract, tables, and conclusions.

[MINOR] Presentation: the manuscript is substantially overlong and repeatedly restates the same caveats and null result. The speculative EFT appendix, extensive internal-pipeline narration, and most secondary T-Web diagnostics should be removed or moved to supplementary material; the main text should focus on one clearly defined estimator, its control construction, covariance, classifier calibration, and reproducible robustness tests.

(3) The raw counts support only an exploratory non-detection of a difference in classifier-assigned labels; the claimed 0.9 percentage-point classifier-label bound, 2.26 percentage-point physical bound, and bounce/inflation interpretation are not supported by the present analysis.
