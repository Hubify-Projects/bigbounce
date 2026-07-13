VERDICT: REJECT

ISSUES:

[MAJOR] Section VIII B, “Primary estimand”: the footprint-restricted non-void control is not selection-function matched to the void sample. The manuscript explicitly defines the “footprint” as the union of projected hole discs over a radial span—not the DESIVAST/BGS completeness mask, veto mask, fibre-assignment selection, or a random-catalog estimate—yet repeatedly describes the resulting contrast as a same-selection-function comparison. No balance is demonstrated in redshift, luminosity, angular size, morphology, imaging depth, classifier confidence, or spectroscopic completeness. The primary analysis must be repeated on the catalog-valid BGS parent using the official mask/randoms and a matched, stratified, inverse-probability-weighted, or covariate-adjusted control. 

ext_P5_M31

[MAJOR] Sections V and VIII B, binomial uncertainty: the quoted standard error, p=0.43, and 95% interval assume 310,357 independent Bernoulli observations. Galaxies share voids, large-scale structures, imaging regions, spectroscopic tiles, and classifier systematics, so this independence assumption is not justified. The primary uncertainty must be obtained from spatial block jackknifes or bootstraps, with clustering at least by void and by independent sky region, and should include cosmic-variance and classifier-systematic covariance.

[MAJOR] Table XI and Eq. (4), “effective 2σ systematic envelope”: the 0.9-pp envelope has no valid coverage interpretation. It combines a 95% statistical half-width, maxima between alternative scientific definitions, global-sample f
CW
	​

 shifts, and tests performed on different parents and different estimands, while treating all terms as independent Gaussian 2σ errors. In particular, the confidence and match-radius entries in Section XI are shifts of the catalog-wide fraction rather than demonstrated shifts of the primary void/non-void contrast, and the RSD reconstruction is performed on the unrestricted—not primary—contrast. These quantities cannot be added in quadrature as written.

[MAJOR] Section V B and Table XIV, multiplicity: the declared headline estimator—exact membership with the footprint-restricted control, Δf
CW
	​

=0.0018—is not one of the five rows in the stated Bonferroni-5 family; the VoidFinder row in Table XIV is the approximate k=20, unrestricted-control estimator with Δf
CW
	​

=0.0007. The post-hoc choices of control volume, exact versus k=20 membership, any-hole versus maximal-sphere geometry, quality thresholds, and classifier path are additional analysis choices. Consequently, neither the advertised family-wise statement nor the simultaneous upper bound formally covers the selected headline result.

[MAJOR] Appendix A and Section XII B, physical de-attenuation: dividing the classifier-label bound by 2a−1 is justified only if sensitivity and specificity are equal, nondifferential, and stable between void and non-void samples. A single overall accuracy of 69.91% does not establish those conditions. The manuscript’s own void-arm validation has a roughly ±3.7-pp uncertainty in directional error asymmetry, far larger than the claimed 0.9-pp label bound. The quoted 2.26-pp physical-chirality constraint is therefore unsupported; it is also inconsistent with the manuscript’s own 1.1-pp family-wise label interval, which would already imply about 2.8 pp before propagating classifier-calibration uncertainty.

[MAJOR] Sections II, VI D, and VIII, monopole cancellation: a strictly uniform additive classifier monopole cancels algebraically, but the manuscript itself finds program-, imaging-leg-, and confidence-dependent label fractions. Cancellation therefore cannot be assumed unless those covariates are balanced between the primary void and control samples or modeled explicitly. The target-program leakage calculation uses the unrestricted non-void population of 621,964 galaxies rather than the primary footprint-restricted control of 253,276 galaxies, so it does not establish balance for the actual headline estimator.

[MAJOR] Sections VIII B–E, void membership: “exact” VoidFinder membership means an exact computation of the authors’ union-of-hole-spheres proxy, not an exact catalog-native galaxy classification. Replacing that proxy by maximal-sphere membership reassigns 36,181 of 57,081 objects and changes the contrast by 0.60 pp; this is a change of environmental estimand, not a small measurement perturbation. The V2 GALZONE analyses additionally use a substantially different 145,789-object valid parent. A single scientifically justified primary membership definition and parent sample must be fixed and validated before combining these results into one bound.

[MAJOR] Section VIII, redshift-space-distortion claim: neither the fixed-hole Gaussian displacement experiment nor the first-order profile-based displacement reruns the void finder on a reconstructed density field. They therefore do not bound the effect of RSD on the void catalog itself, its centers, merging, pruning, edge cuts, or survey mask. Moreover, the quoted 0.024-pp shift applies to the unrestricted contrast, not the primary estimator. The claim that the dominant RSD term is bounded “40 times below” the envelope should be removed unless supported by reconstructed mocks or a full reconstructed-catalog analysis.

[MAJOR] Sections IV, VII, and IX A, T-Web analysis: the canonical density field is constructed without the required angular/radial selection correction and with a zero-padded FFT on an irregular survey window. The manuscript’s own randoms-weighted rebuild changes class-volume fractions by up to 21 percentage points and changes approximately 73% of galaxy labels, demonstrating that the canonical classes primarily trace the survey selection. In addition, the 25.9-h
−1
 Mpc cell size is essentially equal to the nominal 25-h
−1
 Mpc smoothing scale, so the tidal field is poorly sampled. This analysis is not an independent robustness validation and should be redone with a validated window treatment and mocks or removed.

[MAJOR] Section XIII and Appendices A, D, and E, essential companion dependence: the chirality labels, classifier validation, and monopole provenance rely on a companion manuscript still carrying an arXiv placeholder, while the archival DOI is stated to be pending. A mutable repository tag and catalog mirror are not a substitute for an immutable submission archive containing the exact labels, weights, code, environment specification, checksums, and intermediate products. The present paper cannot receive an acceptance recommendation before coordinated review and archival availability of Paper IV and the exact analysis snapshot.

[MAJOR] Sections I, XII B, XV, and Appendix B, physical interpretation: no bounce or inflation model is shown to predict the measured observable, and Appendix B expressly introduces an ad hoc, non-covariant toy operator without a transfer function from fundamental parameters to the observed contrast. Furthermore, the primary DESIVAST statistic has no unique 25-h
−1
 Mpc smoothing scale; that scale belongs to the secondary T-Web construction. The claims that the result constrains bounce/inflation model building at that scale are therefore not derived from the analysis and should be removed or replaced by a quantitative forward model.

[MINOR] Sections III and VIII, sample definition: the matched sample includes objects spectroscopically classified as QSO while being described throughout as spirals, and the chirality-selected test population is flux-, morphology-, and classifier-selected rather than volume limited. The manuscript should quantify and preferably exclude QSO contamination and stop describing the tested galaxy sample itself as a volume-limited BGS sample.

[MINOR] Sections V–VII, permutation precision: 1,000 permutations are marginal for tail probabilities used alongside 1% family-wise thresholds, and several p-values are reported to more precision than their Monte Carlo uncertainty permits. Substantially more permutations and binomial confidence intervals on Monte Carlo p-values are needed.

[MINOR] Presentation throughout: the manuscript is excessively repetitive and uses conflicting prescriptions for the number model builders should adopt—0.9 pp, 1.1 pp, and 2.26 pp appear under different qualifications. The paper should be substantially shortened, with one primary estimator, one clearly defined uncertainty statement, and consistent separation of classifier-label, physical-chirality, counting-only, and family-wise bounds.

Only in a narrow descriptive sense: the selected classifier labels show no statistically significant raw void/non-void difference, but the stated calibrated environmental and physical-chirality bounds are not supported.
