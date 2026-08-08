(1) VERDICT: REJECT

(2) ISSUES:

[MAJOR] §VIII B and §VIII E — the designated-primary control sample is not selection-function matched. The “DESIVAST footprint” is an author-constructed union of hole-sphere angular discs intersected with a radial range, not the DESIVAST/BGS completeness mask or a random-catalog estimate. The manuscript explicitly concedes that it does not match fibre assignment, imaging depth, vetoes, or radial completeness, yet elsewhere calls the resulting contrast a “same-selection-function” estimator. Because the measured effect is only 0.18 percentage points, residual differences in redshift, magnitude, morphology, apparent size, classifier confidence, and imaging conditions can be comparable to the claimed bound. The primary analysis requires a control selected with the official mask/randoms and either matched sampling, inverse-propensity weighting, or a covariate-adjusted model. 

ext_P5_M22

[MAJOR] §V B and Tables IV/XIV — the multiplicity accounting does not include the actual headline estimator. The designated primary is the exact, footprint-restricted VoidFinder contrast, Δf
CW
	​

=0.0018, whereas the Bonferroni-5 family in Table XIV contains the approximate k=20, unrestricted-control result, Δf
CW
	​

=0.0007. The exact-versus-k=20, unrestricted-versus-footprint, any-hole-versus-maximal-sphere, confidence-cut, and other choices were all inspected but are not included in the nominal five-test family. Consequently, the post-hoc Bonferroni-5 calculation does not control the full analysis tree that produced the headline result.

[MAJOR] Abstract, §V B, and §XV — “∣Δf
CW
	​

∣≤0.004” is merely the range of the five observed point estimates, not a family-wise upper bound. Non-rejection of five null hypotheses does not establish that the true effects are smaller than 0.4 percentage points. The manuscript’s own simultaneous Bonferroni intervals permit an absolute classifier-label contrast of approximately 1.12 percentage points. The abstract and conclusions must distinguish observed estimates, ordinary confidence intervals, simultaneous confidence intervals, and equivalence bounds.

[MAJOR] §VIII B and Table X — the quoted two-sample binomial errors assume independent galaxy-level Bernoulli observations. Galaxies share voids, HEALPix regions, imaging tiles, observing conditions, and classifier systematics, so the effective number of independent units need not be 57,081 and 253,276. The full-sample HEALPix diagnostic does not establish the covariance of the specific DESIVAST contrast. The primary interval and p-value require at least a block bootstrap or randomization over voids and sky regions, or a hierarchical/cluster-robust model with void and imaging-region effects.

[MAJOR] Table XI and Eq. (4) — the claimed “honest effective 2σ” systematic envelope has no valid statistical interpretation. It combines a nominal 95% counting half-width with maximum excursions from heterogeneous sensitivity variants, assumes without evidence that strongly correlated membership, geometry, footprint, and GALZONE terms are independent, and adds them in quadrature despite their not being calibrated as standard deviations. Moreover, the confidence-threshold and match-radius results cited from Table XIX are shifts in the catalog-wide f
CW
	​

, not demonstrated shifts in the primary void-minus-nonvoid contrast, so they cannot be entered as Δf
CW
	​

 uncertainties. The 0.9-percentage-point number is therefore neither a 95% interval nor a controlled systematic bound.

[MAJOR] §V B, Table XI, §XII B, and the abstract — the manuscript gives mutually inconsistent numbers for model interpretation. Section V B states that the least-constraining simultaneous family-wise bound is approximately 1.1 percentage points and is the value model builders should adopt, whereas the abstract and §XII B instead promote the 0.9-percentage-point quadrature value. Under the manuscript’s own attenuation factor, the family-wise number would map to roughly 1.12/0.3982≃2.8 percentage points, not 2.26 percentage points.

[MAJOR] §VIII A–E — the five DESIVAST rows do not constitute measurements of one common, well-defined void-membership estimand. VoidFinder “inside any hole” is an author-defined permissive proxy; the maximal-sphere alternative reassigns 36,181 of 57,081 members and moves the contrast by 0.60 percentage points. Treating V2-REVOLVER and V2-VIDE watershed voids as effective-radius spheres is not equivalent to their catalog-native, nonspherical GALZONE membership, while the GALZONE rows use a different 145,789-object parent rather than the 678,945-object low-redshift parent. These variants should be analyzed as distinct estimands, not pooled into a single robustness or simultaneous-constraint statement.

[MAJOR] Appendix A and §XII B — the classifier validation is insufficient for the claimed physical-chirality bound. The 69.91% CW/CCW accuracy is conditional on a true-spiral subset, while the reported three-class accuracy is only 58.7%; no environment-stratified precision, nonspiral false-positive rate, or full CW/CCW/NS confusion matrix is supplied for the selected sample. Environment-dependent contamination of the predicted-CW/CCW sample can therefore bias or dilute the contrast. The transformation by 2a−1 additionally requires equal and environment-invariant sensitivity and specificity; the void-arm error-asymmetry interval is about ±3.7 percentage points, far wider than the claimed sub-percent label bound. At present the result can only be stated for this classifier’s labels, not de-attenuated into a 2.26-percentage-point physical constraint.

[MAJOR] §§IV, IX A, and XII A — the secondary T-Web field is not a validated independent environmental measurement. The randoms-weighted rebuild changes the void volume fraction from 17.6% to 0.75% and leaves only 26.6% of matched spirals in the same class, demonstrating that the canonical labels are dominated by the survey selection function. Such a field cannot substantiate the claimed robustness or define a physical “≳25 Mpc/h” scale. That scale belongs only to the problematic T-Web construction; the primary DESIVAST void catalogs do not correspond to a single 25-Mpc/h Gaussian smoothing scale.

[MAJOR] §VIII and §XIII — the redshift-space-distortion claim is overstated. Perturbing galaxies while holding published holes fixed is a membership sensitivity test, not an RSD reconstruction, and moving galaxies and hole centers together under an assumed universal linear velocity profile without rerunning the void finder does not reproduce the real-space catalog. It therefore cannot establish that the “dominant” RSD term is only 0.024 percentage points or forty times below the envelope. The result should remain explicitly a fixed-redshift-space measurement unless the void catalog and control sample are rebuilt on reconstructed mocks and data.

[MAJOR] §XII B and Appendix B — the purported connection to parity-violating bounce or inflation physics is not established. Apparent CW/CCW is a line-of-sight observable, approximately involving the sign of L⋅
n
^
obs
	​

, whereas the proposed coupling involves L⋅
∇ρ
	​

; marginalizing only over a parity-even void/nonvoid label does not constrain that directional coupling without a transfer calculation involving the observer direction and tidal geometry. More fundamentally, for a pseudoscalar ϕ, both ∇ϕ⋅∇ρ and L⋅
∇ρ
	​

 are parity-odd, so their product in the proposed operator is parity-even, contrary to the appendix’s characterization. The coupling bound is also dimensionally undefined. Appendix B should be removed or replaced by a covariant model with a derived prediction for the measured statistic.

[MAJOR] §II, Appendix A, and Appendix D — the essential chirality labels come from a companion manuscript whose arXiv identifier remains a placeholder and whose archival DOI is not yet present. The present summary does not permit a referee to verify train/test separation, domain-shift calibration, pseudo-label provenance, or the exact version of the labels used. Review would require coordinated access to Paper IV plus an immutable commit hash and archived catalog, weights, intermediate membership table, and executable analysis environment.

[MINOR] Throughout — the manuscript is excessively long and repetitive, with primary/secondary disclaimers, caveats, and artifact descriptions repeated across the abstract, §§V–XV, and the appendices. Several statements are also internally inconsistent, including “footprint 

= selection function” versus later claims that the footprint matches selection functions, and 0.9 versus 1.1 percentage points as the recommended bound. The paper should be substantially shortened, with exploratory T-Web diagnostics and artifact maps moved to supplementary material.

(3) The central claim is supported only as a descriptive non-detection for this post-hoc, classifier-labeled sample; the advertised sub-percent systematic bound, de-attenuated physical bound, and bounce/inflation constraint are not supported.
