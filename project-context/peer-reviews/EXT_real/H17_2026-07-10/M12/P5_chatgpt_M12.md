(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

[MAJOR] §V B, §VIII B–D, and Tables X, XIII, XIV — the primary estimand is not consistently defined. The headline estimator is the exact, footprint-restricted VoidFinder contrast with n
void
	​

=57,081 and n
nonvoid
	​

=253,276, but the purported Bonferroni-5 primary family substitutes an unrestricted, approximate k=20 VoidFinder contrast and combines it with sphere-PIS and GALZONE rows having different parent samples and control definitions. In particular, the sphere-PIS rows use the full z≤0.24 parent of 678,945 galaxies, whereas the GALZONE rows use a 145,789-object catalog-valid parent. These are different target populations, not five measurements of one common estimand, so neither the “uniform family null” nor the simultaneous 1.1-percentage-point bound has the stated interpretation. All variants must be recomputed on a common parent, common survey mask, common control construction, and common exact matching convention. 

ext_P5_M12

[MAJOR] §VIII B/E and the “same-selection-function” claim — the control sample is not selection-function matched. The manuscript correctly admits that its “footprint” is merely the union of hole-sphere angular discs intersected with a radial span, not the DESIVAST/BGS completeness mask, veto mask, fiber-assignment selection, or random catalog. It nevertheless later describes this estimator as “same-selection-function” and says it directly matches the void and control selection functions. Those statements are contradictory. The primary analysis requires the official DESIVAST/BGS mask and randoms, or a prespecified matched/weighted control balancing redshift, sky position, imaging leg, magnitude, size, morphology, classifier confidence, and targeting completeness.

[MAJOR] §VIII, Table XI, Abstract, and §XII B — the quoted “honest effective 2σ systematic envelope” of 0.9 percentage points is not a statistically valid confidence bound. Equation (4) combines a two-sided 95% statistical half-width with peak excursions from correlated alternative definitions, analysis choices, and perturbations, none of which is shown to be an independent zero-mean random uncertainty with a known distribution. Quadrature is therefore unjustified, and the resulting number has neither demonstrated frequentist coverage nor a defined Bayesian interpretation. It is also tighter than the manuscript’s own 1.1-percentage-point simultaneous Bonferroni bound. The authors should instead construct an explicit nuisance-parameter or hierarchical measurement model, perform a coverage-tested bootstrap/injection analysis, or report the separate sensitivity range and simultaneous statistical intervals without calling their quadrature a 2σ exclusion.

[MAJOR] §VIII RSD, membership, and geometry tests — stability of a null statistic after membership scrambling does not bound attenuation of a real signal. The fixed-geometry Monte Carlo changes roughly 34% of the void membership, and the any-hole versus maximal-sphere comparison removes 36,181 of 57,081 void assignments, yet the authors infer robustness because the observed contrast remains near zero. Under an observed null, large nondifferential membership errors will naturally leave the contrast near zero while potentially washing out a genuine physical void/non-void difference. These tests therefore demonstrate stability of the measured null, not sensitivity to an underlying signal. An injection-recovery study with known chirality contrasts and calibrated void-membership purity/completeness is required before any physical upper bound can be quoted.

[MAJOR] §VIII and §XIII — the RSD reconstruction does not establish the claimed real-space robustness. Moving galaxies and published void centers/radii through an assumed universal outflow profile, without rerunning VoidFinder or the watershed algorithms on a reconstructed tracer density field, cannot capture RSD-induced changes in void discovery, merging, center estimation, radius estimation, or catalog selection. Calling the resulting 0.024-percentage-point shift a bound on the “dominant coherent void-outflow RSD term” is too strong. The result may be reported as a fixed-catalog perturbation test, but a real-space constraint requires reconstruction followed by complete void-catalog regeneration and injection-recovery validation.

[MAJOR] Appendix A, §XII B, and the Abstract — the de-attenuated 2.26-percentage-point physical-chirality bound is unsupported. Dividing by 2a−1 is valid only for nondifferential, approximately symmetric binary misclassification with environment-independent sensitivity and specificity. A single catalog-wide 69.91% “accuracy floor” does not establish these conditions, and the manuscript’s own void-stratified error-asymmetry interval has a half-width of approximately 3.7 percentage points, far larger than the claimed sub-percent label-space constraint. The analysis also omits attenuation from environment-label errors, projected-orientation effects, CW/CCW-versus-NS selection, and sample incompleteness. The instruction that “model-builders should use” 2.26 percentage points must be removed unless a joint chirality-label and environment-label measurement-error model is supplied.

[MAJOR] Appendix A and §XIII — the classifier validation is not independently assessable. Paper IV is unpublished in the submission, has a placeholder arXiv identifier, and supplies the per-galaxy labels on which the entire analysis rests. The manuscript does not establish that the GZ1 accuracy and confusion-matrix samples exclude all objects used in training or pseudo-label construction; because GZ1 labels are explicitly part of the training set, this must be demonstrated with a strictly held-out object- and sky-disjoint test set. The claim of exact flip-swap equivariance must also be reconciled with the reported 2.9% “flip identity violators” that are retained. Coordinated review of Paper IV and an immutable archived catalog/code release are prerequisites for acceptance.

[MAJOR] §III, §VIII, and §XIII — the analyzed spiral sample is not volume limited, contrary to repeated motivation of the primary path. DESIVAST may be constructed from a volume-limited BGS tracer sample, but the tested chirality catalog is explicitly flux limited at approximately r≤17.8. Therefore the matched test galaxies remain strongly redshift-, luminosity-, surface-brightness-, size-, and morphology-dependent within z≤0.24. Calling the primary analysis “volume-limited” or claiming that this construction largely removes selection mixing is not justified. A magnitude-complete subsample or a validated weighting/matching analysis is necessary.

[MAJOR] §IV, §VI, §VII, and §IX A — the canonical T-Web field is not a credible physical cosmic-web reconstruction. It is built from a heterogeneous, strongly redshift-dependent mixture of DESI tracers without the appropriate angular/radial random-catalog correction, in a thin masked footprint with zero-padded Fourier operations. The manuscript’s own BGS-randoms-weighted rebuild changes approximately 73% of matched-galaxy class assignments and reduces the void volume fraction by a factor of about 23. This shows that the canonical classes predominantly encode survey selection rather than environment. The canonical T-Web results and their (R
s
	​

,λ
th
	​

) sweep cannot be presented as robustness evidence; the analysis should be rebuilt using tracer-appropriate randoms and completeness weights, or removed from the scientific argument.

[MAJOR] §V B — post-hoc designation and multiplicity are not resolved by the stated Bonferroni-5 correction. The DESIVAST path, membership rule, footprint rule, and reporting hierarchy were chosen after examining multiple classifiers and dozens of stratifications. Bonferroni correction within a subsequently selected five-row family does not account for this analysis-path selection. The authors are commendably explicit that the study is exploratory, but the manuscript nevertheless uses confirmatory language such as “family-wise bound,” “exclusion,” and “must satisfy.” The DR1 result should be presented as an exploratory effect estimate with sensitivity analyses; confirmatory coverage requires a frozen analysis on an independent release.

[MAJOR] §VIII C–E and the title — “three-algorithm” robustness overstates independence and mixes official and nonofficial memberships. V2-REVOLVER and V2-VIDE are two pruning prescriptions applied to the same watershed construction, not independent void-finding families. Moreover, the sphere-PIS classifications for the watershed catalogs are author-defined effective-radius approximations rather than catalog-native membership, and the primary VoidFinder any-hole union is explicitly described as permissive. The paper should distinguish two algorithmic families, privilege official catalog-native membership where available, and avoid treating highly correlated geometry variants as independent confirmations.

[MINOR] §III C and Table XIX — the angular cross-match needs a stricter ambiguity analysis. Given the shared Legacy Survey provenance, source identifiers such as release/brick/object identifiers should be used where possible, or at minimum a mutual one-to-one match should be required. The authors should report the number of multiple candidates, the estimated chance-match rate, the number of chirality objects associated with more than one TARGETID, and a sensitivity test excluding SPECTYPE=QSO. A pre-deduplication match-radius sweep does not address these ambiguities.

[MINOR] §V–VII — several secondary significance calculations use an estimated monopole without consistently propagating its covariance. Subtracting σ
pred
	​

 from binwise z-scores is not equivalent to a formal test when the monopole is estimated from the same catalog and shares objects with the bins. The appropriate analyses are multinomial/homogeneity tests, logistic models, or permutations centered on the observed global rate; the informal residual-σ thresholding should be removed or clearly labeled descriptive.

[MINOR] §XII B, §XV, and Appendix B — the theoretical interpretation is disconnected from the primary observable. The approximately 25 h
−1
 Mpc smoothing scale belongs to the secondary T-Web calculation, whereas the primary DESIVAST estimator uses voids spanning a distribution of effective sizes and no unique smoothing scale. No cited bounce or inflation model predicts the tested observable, and Appendix B’s operator is explicitly noncovariant and not derived from the data. The manuscript should not state that the primary bound constrains models specifically at the T-Web smoothing scale; the toy-EFT appendix should be removed or relegated to supplementary discussion.

[MINOR] Throughout — the manuscript is excessively long and internally repetitive, with important terminology used inconsistently. “Parity null,” “environment independence,” “same-selection-function,” “exact membership,” “primary,” and “family-wise bound” are repeatedly used for nonidentical statements. The main paper should be substantially shortened, the exploratory primary estimator defined once, and the numerous audit trails, alternative scans, AI-workflow discussion, and speculative model mapping moved to supplemental material.

(3) The central claim is supported only in the narrow sense that no statistically significant association is detected between the observed classifier labels and the analyzed environment labels; the advertised 0.9-percentage-point classifier-space bound and 2.26-percentage-point physical-chirality bound are not supported by the present analysis.
