(1) VERDICT: REJECT

(2) ISSUES:

[MAJOR] Section VIII B/E — the primary “footprint-restricted” control is not selection-function matched. The footprint is constructed from the union of projected void-hole discs and their radial span, rather than the published DESIVAST/BGS angular mask, vetoes, completeness map, or DESI random catalog. This construction does not equalize fiber assignment, imaging depth, radial completeness, or target selection between void and non-void galaxies, despite being described elsewhere as a “same-selection-function” comparison. Because the manuscript itself finds chirality-label variation with target program, imaging leg, and classifier confidence, the primary contrast must be recomputed with the actual survey mask and randoms, preferably using per-void matched controls or inverse-probability weighting. 

ext_P5_M17

[MAJOR] Sections V B and VIII B; Table XIV — the declared Bonferroni-5 family does not contain the designated primary estimator. The abstract and Section VIII B designate the exact, k-unbounded, footprint-restricted VoidFinder contrast with n
void
	​

=57,081 and n
nonvoid
	​

=253,276 as primary, whereas Table XIV uses the approximate k=20, unrestricted contrast with n
void
	​

=56,981 and n
nonvoid
	​

=621,964. Exact versus approximate membership, footprint-restricted versus unrestricted controls, and any-hole versus maximal-sphere geometry were all inspected after seeing the data but are not consistently included in the multiplicity family. The advertised “Bonferroni-5 primary null” is therefore not a closed or pre-specified family and cannot support the quoted family-wise bound.

[MAJOR] Table XI and Eq. (4) — the 0.9 percentage-point systematic bound has no valid confidence interpretation. The quadrature combines a 95% counting-statistics half-width with peak shifts between correlated analysis variants, confidence cuts, membership definitions, and geometry choices; these quantities are neither independent nor calibrated as common-σ uncertainties, and several contain their own sampling noise. Moreover, the reported quadrature is 0.948 pp and must be centered on the measured +0.181 pp contrast, giving an interval approximately [−0.77,+1.13] pp, not a symmetric ±0.9 pp exclusion about zero. The manuscript’s own simultaneous family interval already implies an absolute bound of about 1.1 pp. Consequently, even under the manuscript’s attenuation prescription, the corresponding physical scale would be about 1.1/0.398≃2.8 pp, not 2.26 pp.

[MAJOR] Sections V and VIII — the quoted binomial errors assume independent galaxies, although the sampling units are strongly clustered. Galaxies share voids, sky regions, imaging conditions, target-selection sectors, and classifier systematics; physical spin correlations may also occur within structures. A galaxy-level two-binomial standard error and unrestricted label shuffle do not estimate this covariance. The primary uncertainty should be obtained with void-level and angular-block bootstrap or jackknife estimates, supplemented by survey mocks and cluster-robust inference. Until this is done, the effective sample size and the quoted sub-percent confidence intervals are unknown.

[MAJOR] Appendix A and Sections XII–XIII — the de-attenuation from classifier labels to physical chirality is not justified. A single global accuracy and an approximately symmetric aggregate confusion matrix do not imply a common attenuation factor across void and non-void environments. The manuscript’s own void-stratified validation has a roughly ±3.7 pp 95% uncertainty in directional error asymmetry, several times larger than the claimed 0.9 pp classifier-label bound. Accuracy also varies strongly with confidence and plausibly with size, surface brightness, inclination, morphology, and redshift. A hierarchical measurement-error model or a substantially larger independently human-labelled environmental sample is required; otherwise all physical-chirality and model-building bounds must be removed.

[MAJOR] Section VIII B, “Adjustment in lieu of a full covariate regression” — the primary analysis lacks the necessary adjusted estimator. Similar bright/dark program fractions do not establish balance in redshift, apparent magnitude, size, surface brightness, morphology, inclination, classifier confidence, imaging leg, or local observing conditions. These variables can differ intrinsically between void and non-void galaxies and can affect the chirality classifier. Separate one-variable systematics splits do not replace a simultaneous regression, matching analysis, or propensity-weighted estimator. The deferred model CW∼void+z+m
r
	​

+R
50
	​

+p
max
	​

+leg+morphology+sky is required for the present submission, not merely for DR2.

[MAJOR] Section VIII and Table XI — the stated 0.02 pp redshift-space-distortion systematic is not established. Displacing galaxies and already-published void centers and radii with a first-order velocity profile, without rerunning VoidFinder or the watershed algorithms on the reconstructed density field, cannot capture changes in void topology, centers, radii, merging, pruning, or edge classification. The fixed-geometry Gaussian perturbation likewise does not represent coherent Kaiser and nonlinear finger-of-god effects. The 0.02 pp shift may characterize that particular fixed-catalog transformation, but it cannot be entered as the total RSD uncertainty. The defensible result is strictly an observed-redshift-space statistic unless the void catalogs are reconstructed and regenerated.

[MAJOR] Sections IV, IX A, and XII — the canonical T-Web classification is demonstrably dominated by the DESI selection function. The construction uses a global mean density despite a reported factor of approximately 640 radial variation, while the random-catalog-weighted rebuild changes the environment label of about 73% of matched spirals and changes the void volume fraction by a factor of about 23. This is not a perturbative robustness test; it shows that the canonical T-Web labels do not reliably represent the physical cosmic web. Obtaining the same chirality null under radically different, selection-driven partitions is not meaningful independent validation. The canonical T-Web results should be removed from the evidentiary chain or rebuilt from the outset with validated angular and radial selection corrections and mocks.

[MAJOR] Sections VIII C–E and Table XIV — the five “void definitions” do not measure a common estimand. Effective-radius point-in-sphere approximations are not the catalog-native watershed memberships for V2-REVOLVER or V2-VIDE, and the GALZONE rows use a much smaller and different valid parent sample. For VoidFinder, replacing the any-hole union by the maximal sphere reassigns 36,181 of 57,081 galaxies and shifts the estimated contrast by 0.60 pp. Such variants are alternative physical definitions with materially different populations, not independent small systematic perturbations to be pooled in one family. The analysis should use official catalog-native memberships wherever available and a single physically justified VoidFinder membership obtained by rerunning or faithfully reproducing the catalog algorithm.

[MAJOR] Sections II, XII B, and Appendix B — the claimed connection to bounce or inflation physics is not demonstrated. The manuscript states that no published bounce or inflation model predicts the measured environmental observable. Appendix B then introduces an explicitly non-covariant toy operator with unspecified normalization and no transfer calculation from the proposed coupling to galaxy-spin chirality. The asserted coupling scaling is therefore dimensional speculation, not a derived constraint. Appendix B and the statements that the result constrains a “bounce-chirality coupling class” should be removed unless a concrete model, transfer function, and galaxy-formation mapping are supplied.

[MAJOR] Sections II, XIII, and Appendix A — the load-bearing chirality labels depend on an unavailable companion submission. Paper IV still has a placeholder arXiv identifier, and the permanent archival DOI is stated to be pending. The present author’s summary of classifier training and validation is not a substitute for independent review of the underlying catalog paper, label provenance, weights, and frozen artifacts. This manuscript could only be evaluated through coordinated co-review with Paper IV and a permanent, immutable data-and-code archive available during review.

[MAJOR] Abstract, Sections XII and XV — non-rejection is repeatedly overstated as environment independence. Bonferroni-corrected failure to reject does not establish equality, and the primary experiment tests only a low-redshift binary void-versus-composite-non-void contrast, not general dependence across walls, filaments, and clusters. A defensible formulation would report the estimator and its properly constructed confidence interval as a non-detection. A claim of practical equivalence would require a scientifically motivated equivalence margin and an explicit equivalence test.

[MINOR] Section III and the primary matching recipe — objects with SPECTYPE=QSO are retained in a spiral-galaxy analysis. The manuscript should report their number in the CW/CCW and primary DESIVAST samples and repeat the analysis after restricting strictly to spectroscopic galaxies.

[MINOR] Presentation and reproducibility — the manuscript is excessively long and internally repetitive. The same primary caveats, “headline” designation, RSD qualification, and monopole discussion recur throughout the abstract, main text, limitations, conclusions, and Appendix A. The paper should be reduced substantially, with audit trails, artifact maps, extended T-Web diagnostics, and AI-pipeline details moved to supplemental material; all placeholder identifiers must be resolved before submission.

(3) The central claim is supported only as a descriptive non-detection of a hard-label CW-fraction difference in the particular redshift-space samples analyzed; the general environment-independence claim and the advertised 0.9 pp classifier-label and 2.26 pp physical bounds are not supported.
