# EXT Review — P5 × ChatGPT
- paper: P5
- version: v0.1.101
- reviewer: ChatGPT
- model: Pro Extended
- timestamp: 2026-07-06T19:22:47Z
- chat_url: https://chatgpt.com/c/6a4bfefd-f528-83e8-9b84-28a6eef1f172
- pdf: /tmp/round_P5.pdf

## Raw verbatim response

(1) VERDICT: REJECT.

(2) ISSUES:

[MAJOR] Section II / Appendix A, Paper IV dependence: the analysis rests on per-galaxy CW/CCW labels from an unpublished companion manuscript, with only a summary of the classifier, training, validation, and monopole origin; the public label table is not a substitute for a peer-reviewed, fully auditable measurement model, and the paper’s own text admits the primary result remains conditional on that label set. 

round_P5

[MAJOR] Sections VIII B, XII B, central “∼0.5 pp” DESIVAST bound: the quoted bound is not a full uncertainty budget. The manuscript explicitly excludes fixed-void-geometry membership systematics, residual classifier monopole systematics, cross-match purity, and point-in-sphere membership purity from the tabulated CI, then still presents a sub-percent physical constraint. That is not an acceptable exclusion statement.

[MAJOR] Appendix A / Sections VIII–XII, classifier dilution: the classifier’s quoted independent binary accuracy floor is only 69.91%. A random symmetric error rate at this level attenuates any true chirality asymmetry by roughly 2a−1≃0.40, so an observed 0.5 pp bound would correspond to about 1.3 pp on true handedness even before environment-dependent misclassification is considered. The manuscript does not propagate this dilution into the central bound.

[MAJOR] Section II / Section VIII F, “monopole invariance” claim: the void/non-void contrast is invariant only to a strictly catalog-wide scalar offset. The manuscript itself documents imaging-leg, target-program, sky-mask, and BGS-bright/dark residual structure, so classifier error need not cancel between void and non-void samples. The primary DESIVAST contrast is not shown with a fully matched or weighted control in redshift, imaging leg, morphology, magnitude, sky position, and target-program space.

[MAJOR] Sections IV, VI, VII, IX A, secondary T-Web analysis: the T-Web classifier is built from an unweighted redshift-space DESI DR1 density field with a strong radial selection function, and the manuscript later shows that a BGS-randoms-weighted rebuild collapses the void volume fraction by about a factor of 23 and reassigns a large fraction of galaxies. This invalidates the unweighted T-Web labels as physical cosmic-web environments, so the T-Web “cross-check” is not an independent environmental validation.

[MAJOR] Sections V B and Table III, post-hoc primary path: the paper concedes no timestamped analysis plan predates the data and that the DESIVAST primary path was designated post hoc. A null result is less vulnerable than a claimed detection, but the claimed numerical upper bound is still analysis-choice dependent and must be presented as exploratory unless a single locked estimator and full systematic budget are supplied.

[MAJOR] Sections V–VIII, statistical independence: binomial and Pearson tests treat galaxies or repeated survey-program rows as effectively independent aside from a small duplicate-row check. This ignores spatial clustering, common imaging fields, shared classifier systematics, survey-mask correlations, and void-catalog membership correlations. Label shuffles do not adequately model these correlated errors.

[MAJOR] Section VIII E, DESIVAST non-void control definition: the main non-void sample includes all z≤0.24 matched spirals outside any hole, but the later footprint-restricted control is constructed from the union of hole-sphere angular discs rather than a published DESIVAST angular/radial selection mask. This is not an adequate matched control for a void/non-void environmental contrast.

[MAJOR] Sections XIII and VIII, redshift-space distortions: the paper acknowledges that all classifications are in observed redshift space and that a proper RSD treatment would require reconstructed positions, but still presents physical environment-independence and model-bound language. The redshift-space-only scope should be reflected in the title, abstract, conclusions, and bound.

[MAJOR] Section X / ASTRA cross-validation: the ASTRA and T-Web labels disagree strongly on the EDR overlap, and the overlap is small and geographically restricted. This cannot be used as meaningful classifier robustness evidence; at most it shows that two noisy, inconsistent environment partitions both fail to detect a signal in a small subsample.

[MAJOR] Section XII B / Appendix B, bounce/EFT interpretation: the manuscript states that no published bounce or inflation model predicts the tested environment-conditional signature, then introduces a speculative toy EFT mapping that is not derived from the cited theory and is admitted not to be gauge-invariant. This theoretical material does not support the observational claim and is inappropriate as a PRD-level constraint.

[MINOR] Abstract and Introduction: the abstract is far too long, contains methodological caveats, results, rebuttals to referees, and internal provenance discussion, and is not usable as a scientific abstract.

[MINOR] Terminology: “spiral galaxy handedness,” “chirality,” “spin direction,” and “projected CW/CCW label” are used interchangeably, but the measurement is an image-projection classifier label, not a direct physical spin-vector measurement.

[MINOR] Tables and narrative: many tables report raw σ
fromhalf
	​

 despite repeatedly warning that these values are not comparable across n; this presentation invites overinterpretation and should be replaced by a single consistent effect-size and uncertainty framework.

[MINOR] Reproducibility: artifact IDs point to a mutable GitHub-style repository and “DOI accompanies submission” language; a real submission should provide immutable archived data, code, exact hashes, and sufficient metadata at review time, not prospectively.

[MINOR] Scope inflation: claims such as “largest,” “properly powered,” “cleanest,” and “controlled-sample” are not consistently supported by literature comparisons or by a full systematic model and should be removed or sharply qualified.

(3) The central claim is supported only in the weak sense that the submitted pipeline finds no significant void/non-void difference in its own classifier labels; it is not supported as a robust astrophysical environment-independence result or as a reliable sub-percent physical bound.
