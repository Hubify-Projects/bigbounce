(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

[MAJOR] Section VIII B/E, primary footprint-restricted contrast: The non-void control is not demonstrably selection-function matched to the void sample. The adopted “footprint” is an author-constructed union of projected hole-sphere discs intersected with a radial span, not the published DESIVAST/BGS completeness mask, veto mask, fiber-assignment model, or random catalog. The manuscript acknowledges this limitation but elsewhere calls the estimator “same-selection-function” and states that the selection functions are matched directly. Because chirality-label fractions vary with target program, classifier confidence, imaging leg, and sky region, the primary contrast may retain redshift-, imaging-, morphology-, and completeness-dependent confounding. The primary analysis must be repeated using the official survey mask and randoms, or with a non-void control explicitly matched or weighted in redshift, sky position, imaging depth, apparent magnitude, size, morphology, target program, and classifier confidence. 

ext_P5_M6

[MAJOR] Section V B and Tables IV/XIV, definition of the Bonferroni-5 primary family: The actual headline estimator—exact membership, footprint-restricted control, n
void
	​

=57,081, Δf
CW
	​

=0.0018—is absent from Table XIV. That table instead includes the approximate k=20, unrestricted VoidFinder estimator with n
void
	​

=56,981 and Δf
CW
	​

=0.0007. The other family members also use different parents, including a 678,945-object low-z parent for sphere tests and a 145,789-object GALZONE parent for catalog-native tests. Thus, the manuscript does not consistently define the five estimands to which its headline family-wise statement applies. Moreover, Bonferroni correction over five variants does not correct the post-hoc selection of DESIVAST, the footprint restriction, and the five-member family from the much larger analysis tree. The present result must be described as exploratory, and the family, estimand, and simultaneous confidence construction must be made internally consistent.

[MAJOR] Table XI and Eq. (4), claimed 0.9 percentage-point systematic envelope: This is not a statistically calibrated 2σ or 95% interval. The quadrature combines a counting-confidence half-width, maxima from sensitivity variations, absolute point estimates, and shifts measured on different samples and different estimands, while assuming independence without justification. Several entries are not systematics on the primary contrast at all: the confidence and match-radius terms are largely shifts in the overall f
CW
	​

, and the RSD reconstruction was applied to the unrestricted rather than the primary footprint-restricted estimator. The “sphere-PIS versus GALZONE” entry of 0.37 pp is also an absolute GALZONE contrast rather than the actual between-method change, which is approximately 0.18–0.20 pp for the tabulated V2 cases. The primary counting interval alone has a half-width of approximately 0.45–0.46 pp, not the quoted 0.44 pp taken from the unrestricted sensitivity estimator. A coherent nuisance model, mock-based coverage study, or unified bootstrap is required; otherwise Table XI must be presented only as an informal sensitivity summary, not an exclusion bound.

[MAJOR] Sections V and VIII, independence and uncertainty model: The two-sample binomial standard error treats all galaxy labels as independent. Void galaxies are clustered within common voids and survey regions, while classifier errors and imaging systematics can be spatially correlated. The individual-galaxy label shuffles used elsewhere destroy precisely this correlation and therefore do not establish exchangeability for the primary test. The primary uncertainty should be recomputed with void-level and angular-block resampling, a spatial jackknife, or a hierarchical/cluster-robust model; the non-void sample should be blocked on the same spatial scale. Until this is done, the effective sample size and the quoted upper limits are uncertain.

[MAJOR] Appendix A and Section XII B, conversion to a 2.26-pp physical-chirality bound: Overall classification accuracy a=0.6991 does not by itself imply an attenuation factor 2a−1. The relevant factor is determined by the environment-specific sensitivity and specificity—equivalently the Youden coefficient—and must be stable across void and non-void samples. Symmetry inferred from a different, high-confidence GZ1 subset with 91–96% accuracy cannot simply be transferred to the 69.91% “floor” sample. The manuscript’s own void-arm error-asymmetry interval is about ±3.7 pp, much wider than the claimed classifier-label bound. In addition, projected image winding is not automatically the sign of the three-dimensional angular momentum without assumptions about trailing versus leading arms and the near side of each disk. The 2.26-pp number should therefore be removed as a bound or replaced by a latent-class/error-matrix analysis with uncertainty propagated on the relevant low-z, void/non-void population.

[MAJOR] Section II and Section VIII F, “algebraic invariance” to the classifier monopole: A common additive offset cancels in a difference, but general classifier systematics do not. Environment-dependent error rates, multiplicative attenuation, threshold effects, and differing distributions of magnitude, size, inclination, morphology, redshift, confidence, and imaging provenance can all produce or suppress a void/non-void contrast. The confidence, target-program, and outside-footprint results already demonstrate that the label fraction is not perfectly uniform across observational strata. The current small GZ1 void validation does not exclude differential bias at the sub-percent scale. The manuscript must restrict the invariance claim to a spatially and covariate-independent additive offset and directly test the primary contrast with matched covariates or human-label validation.

[MAJOR] Section VIII, RSD robustness and the claimed 0.024-pp bound: Adding independent Gaussian line-of-sight perturbations while holding the void catalog fixed is not a reconstruction of redshift-space distortions; it is a random membership-noise experiment, and its tendency to preserve a null contrast does not bound a coherent, property-dependent RSD bias. The subsequent first-order profile displacement does not rerun the void finder on a reconstructed tracer field, and it is evaluated on the unrestricted rather than the headline footprint-restricted estimator. Consequently, the 0.024-pp shift cannot be described as a bound on the dominant RSD systematic or as being “40 times below” the primary envelope. Either retain the result explicitly as a redshift-space measurement or perform an end-to-end mock-calibrated reconstruction in which tracers, selection, void finding, and the primary control definition are all re-evaluated.

[MAJOR] Sections IV, VII, and IX A, T-Web secondary analysis: The canonical T-Web field is dominated by the DESI radial and angular selection function: the randoms-weighted rebuild changes the void volume fraction from 17.6% to 0.75% and leaves only 26.6% of matched spirals in the same class. This is not a small robustness variation but evidence that the original classes do not represent a controlled physical environment estimator. In addition, R
s
	​

=25h
−1
Mpc is sampled by a 25.9h
−1
Mpc grid cell, making the nominal smoothing only marginally resolved, while the masked zero-padded FFT introduces boundary sensitivity. The preservation of a chirality null under radically different, partly selection-driven partitions does not validate the physical T-Web result. The T-Web analysis should be rebuilt with appropriate DESI randoms, a converged grid, and survey-window treatment, or removed from the physical interpretation; in particular, the DESIVAST primary result cannot be advertised as a constraint specifically at a 25h
−1
Mpc T-Web smoothing scale.

[MAJOR] Section XIII and Appendix A, dependence on companion Paper IV: The scientific observable is entirely inherited from a concurrently submitted, not-yet-final classifier catalog. The present appendix is insufficient to assess training/test leakage, duplicate-object leakage, calibration, domain shift from SDSS/GZ1 to Legacy imaging, and environment-dependent confusion matrices. Acceptance would require coordinated review of Paper IV, a frozen version of the catalog and weights, final identifiers rather than placeholders, and an archival snapshot with hashes sufficient to reproduce the exact labels used here. The primary result must then be regenerated against that frozen release.

[MAJOR] Section XII B and Appendix B, bounce/inflation interpretation: No forward model is supplied that maps a bounce- or inflation-generated parity-violating field into a low-redshift, projected spiral-winding contrast conditioned on DESIVAST membership. The proposed toy operator is explicitly non-covariant, its coupling normalization and dimensions are not defined sufficiently to infer a constraint, and no transfer function connects it to the measured statistic. Therefore the data do not presently constrain a bounce or inflation parameter space. Appendix B and statements that “model-builders should use” a particular numerical bound should be removed, or replaced by a concrete model calculation including galaxy-spin formation, projection, classifier response, and survey selection.

[MINOR] Catalog and numerical consistency throughout Sections V and VIII: Reconcile the stated 1,489 interior VoidFinder voids with the later 3,765 “maximal voids,” use the exact 57,081-object membership consistently once it is available rather than retaining the known-incomplete k=20 result in headline tables, and distinguish interval half-widths from maximum absolute interval endpoints—the quantities listed as 0.77, 0.63, 0.50, 1.12, and 0.86 pp in Section V B are endpoint bounds, not half-widths. All headline counts, confidence intervals, and family definitions require a single arithmetic audit.

[MINOR] Sections III, XII, and XV, sample definition and presentation: A manuscript about physical spiral chirality should either exclude SPECTYPE==QSO objects or quantify their incidence in the chirality-relevant and primary low-z samples. The text should consistently say “no detectable environment-dependent label-fraction difference” rather than “consistent with parity,” because the environmental contrast is not itself a global parity test. The manuscript is also substantially overlong and repetitive; the non-load-bearing T-Web diagnostics, repeated caveats, and speculative EFT discussion should be condensed or moved to supplementary material.

(3) The tabulated counts support a descriptive non-detection of a void/non-void classifier-label difference, but they do not yet support the advertised 0.9-pp classifier-label limit, 2.26-pp physical-chirality bound, or bounce/inflation constraint.
