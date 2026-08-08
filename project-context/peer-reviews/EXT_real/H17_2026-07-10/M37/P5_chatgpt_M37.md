(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

[MAJOR] Section VIII B/E, “footprint-restricted” primary control: the adopted footprint is the union of void-hole angular discs intersected with a global radial span, not the published DESIVAST/BGS completeness mask or a random-catalog representation of the selection function. The manuscript explicitly acknowledges that this construction does not match fibre assignment, imaging depth, vetoes, or radial completeness, yet later describes the samples as having matched selection functions. The primary contrast therefore remains vulnerable to survey-selection differences; it must be recomputed using the official mask/randoms or a per-void matched/IPW control with redshift and angular-selection balance demonstrated. Table XII’s program-balance check uses the unrestricted 621,964-galaxy control, not the 253,276-galaxy primary control, so it does not close this problem. 

ext_P5_M37

[MAJOR] Section V B, Section VIII B, Tables X and XIV, multiplicity definition: the designated headline estimator is the exact, footprint-restricted VoidFinder contrast with n
void
	​

=57,081 and Δf
CW
	​

=0.0018, but Table XIV’s VoidFinder member is the approximate k=20, unrestricted contrast with n
void
	​

=56,981 and Δf
CW
	​

=0.0007. Thus the stated Bonferroni-5 family and its simultaneous interval do not actually contain the estimator advertised as primary. The estimand, membership rule, parent population, and five-member family must be fixed consistently and all family-wise statistics recomputed; Bonferroni correction over five subsequently selected variants also does not correct the post-hoc choice from the much larger analysis tree.

[MAJOR] Sections VIII C–E, definition of the five “void estimators”: the point-in-effective-radius-sphere construction for the nonspherical REVOLVER and VIDE watershed voids is an author-created approximation rather than the catalog-native membership, while the VoidFinder union of all component holes is explicitly a permissive proxy. These approximations are mixed with official GALZONE memberships evaluated on a different 145,789-object parent and then treated as commensurate robustness measurements. The 0.60-percentage-point change between the any-hole and maximal-sphere definitions is larger than the measured headline contrast and shows that membership convention is scientifically consequential. The primary family should use official per-galaxy memberships on a common valid parent, or the heterogeneous estimators must be reported separately without a single combined precision claim.

[MAJOR] Table XI and Eq. (4), “honest effective 2σ systematic envelope”: adding a two-sided counting interval and peak shifts from alternative analysis choices in quadrature is not a statistically defined confidence interval. The listed terms are correlated, are not calibrated one-standard-deviation uncertainties, and often contain ordinary sampling fluctuations; geometry, membership, sphere-versus-GALZONE, footprint, and RSD variations also overlap conceptually. Moreover, the confidence and match-radius results shown in Section XI are full-sample f
CW
	​

 shifts rather than demonstrated shifts of the primary contrast, and the RSD number was computed for the unrestricted estimator. The resulting 0.9-pp number has no stated coverage and conflicts with the manuscript’s own approximately 1.1-pp Bonferroni simultaneous bound. A nuisance-parameter model, spatial bootstrap, or simulation-based coverage study is required; otherwise the counting interval and sensitivity shifts must be reported separately.

[MAJOR] Sections V and VIII B, uncertainty model: the quoted standard error treats hundreds of thousands of galaxy labels as independent Bernoulli trials. Galaxies share voids, imaging conditions, sky regions, target-selection histories, and classifier systematics, so galaxy-level binomial errors can understate the uncertainty at the sub-percent scale. The label-shuffle tests do not solve this because they destroy the spatially correlated structure whose contribution must be estimated. The primary analysis needs void-level and angular-block jackknives or bootstraps, a clustered sandwich estimator, or a hierarchical model with void/sky random effects.

[MAJOR] Sections II, VIII F, XI, and Appendix A, claimed cancellation of classifier bias: a literal constant additive monopole cancels from a two-sample difference, but the manuscript itself finds dependence on target program, imaging leg, and confidence. Classification performance can also depend on apparent size, magnitude, inclination, surface brightness, and morphology, none of which is shown to be balanced between the primary void and control samples. The covariate regression performed for the secondary T-Web labels is not a substitute for an adjusted primary DESIVAST analysis. The paper therefore establishes, at most, a difference in classifier-assigned labels under an unverified nondifferential-error assumption, not environment independence of galaxy chirality.

[MAJOR] Abstract, Section XII B, and Appendix A, physical-chirality de-attenuation: the conversion 1/(2a−1) is valid only for known, symmetric, nondifferential CW/CCW error rates. A global “accuracy floor” is insufficient to determine this attenuation, and its uncertainty is not propagated. The manuscript’s own void-specific validation has a roughly ±3.7-pp uncertainty in error asymmetry, far wider than the claimed 0.9-pp label-level bound, so it cannot validate the required assumption at the relevant precision. The 2.26-pp physical bound should be removed or replaced by a latent-class/error-matrix analysis using environment-specific sensitivity and specificity.

[MAJOR] Section VIII, redshift-space-distortion treatment: perturbing galaxy distances while holding a redshift-space void catalog fixed tests only boundary sensitivity, while displacing published holes and galaxies together without reconstructing the tracer field and rerunning the void finder cannot capture changes in void detection, radii, merging, topology, or survey-edge classification. Consequently, the quoted 0.024-pp shift does not bound the redshift-to-real-space uncertainty and should not enter Table XI as an RSD systematic. Either retain a strictly fixed-redshift-space result with no real-space interpretation or perform a complete reconstruction followed by a new void-catalog construction.

[MAJOR] Sections I, XII B, XV, and Appendix B, theory interpretation: the primary DESIVAST estimator is not an observable defined at the T-Web smoothing scale R
s
	​

=25Mpc/h; that scale belongs only to the secondary, selection-sensitive T-Web analysis. No transfer calculation maps projected spiral winding, void membership, and classifier errors to a bounce- or inflation-sector parity-violating parameter. The statement that any such model must satisfy a bound at “≳25Mpc/h” is therefore unsupported. The noncovariant toy operator in Appendix B does not repair this and should be removed or clearly separated as speculation unless a quantitative, gauge-consistent forward model is supplied.

[MAJOR] Section XIII and Appendices A/D, essential companion-paper dependency: the per-galaxy outcome labels and their calibration are the indispensable measurement input, yet Paper IV still has an arXiv placeholder and the archival DOI is pending. A movable repository tag is not an immutable archival record. The manuscript cannot be accepted before Paper IV is supplied for coordinated review, the exact catalog/weights and all analysis artifacts are version-locked by commit hash and archival DOI, and the final identifiers replace all placeholders.

[MINOR] Sections IV, VI, and IX, status of the canonical T-Web analysis: the random-catalog-weighted rebuild changes approximately 73% of matched-galaxy environment labels and reduces the void volume fraction by a factor of about 23. This demonstrates that the canonical T-Web field is dominated by the survey selection function rather than providing an independent physical environment classification. It should be substantially condensed or replaced by the completeness-weighted construction and must not support the quoted physical scale or robustness claims.

[MINOR] Figures 6 and 9 and sample-denominator reporting: Figure 6(a) is labelled “maximal voids per pixel,” although its 3,303-pixel denominator and 50–734 range correspond to the matched-spiral sky scan, not the later DESIVAST maximal-void map. Figure 9 labels the T-Web sample as 791,635 galaxies while its four displayed class counts sum to 812,793 row-level entries. All figures and tables must distinguish unique galaxies, repeated survey-program rows, approximate memberships, and exact memberships consistently.

[MINOR] Abstract and Conclusions, interpretation of non-rejection: phrases such as “the null holds,” “environment independence,” and “leaving no room” overstate what a post-hoc non-detection establishes. The result should be phrased as an exploratory absence of a detected classifier-label contrast, accompanied by the exact asymmetric confidence intervals and, if the authors wish to claim practical equivalence, a prespecified equivalence margin and formal equivalence test.

(3) Only partially: the data support a qualitative non-detection of a void/non-void difference in the classifier-assigned labels, but they do not presently support the advertised 0.9-pp systematic envelope or the 2.26-pp physical-chirality bound.
