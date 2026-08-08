# P4 (v1.0.222) — ChatGPT Pro (thinking/High) — EXT FULL8 2026-07-08

Verdict (verbatim from '(1) VERDICT:'): MAJOR REVISIONS

## RAW RESPONSE

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

[MAJOR] Section IV C / primary dipole claim: the headline null is based on the peq > 0.6 high-confidence subsample, while the unthresholded catalog gives a reported z ≈ 4.2–4.4 real-space excess; the manuscript attributes this entirely to low-confidence systematics, but the primary null therefore applies only to a selected 30% subsample, not to the full 3.2M-spiral catalog claimed in the title/abstract. 

full8_P4

[MAJOR] Sections II, IV A, VI A / classifier validity: the classifier has only 69.91% independent GZ1 spiral-chirality accuracy, κ = 0.40, and is trained 66.5% on CE-ResNet pseudo-labels; the paper’s validation and softmax confidence are therefore insufficient to support “catalog-grade” chirality labels or sub-percent physical isotropy constraints without a full label-error likelihood.

[MAJOR] Section VI A / pseudo-label independence: the GZ1-human-only cross-check is presented as “decisive,” but the manuscript itself states its N ≈ 4.6×10⁴ sample has A50 ≈ 3.4% and A95 ≈ 4.5–6.8%, far weaker than the headline sub-percent sensitivity; it cannot exclude inherited pseudo-label dipoles at the claimed science sensitivity.

[MAJOR] Sections III B, IV D, Appendix D / “clean 1.7% dipole disfavored at z ≈ −18”: this statistic is not a calibrated exclusion significance; it comes from a block-bootstrap WLS template model with acknowledged nuisance-template limitations, classifier-label uncertainty outside the bootstrap covariance, and no simultaneous likelihood over classifier confidence, depth, morphology, and dipole amplitude.

[MAJOR] Sections IV C–IV D / harmonic residuals: the manuscript reports highly significant MASTER residuals (+7.28, +7.93, and +3.64 under different conventions) but classifies them as systematics while the forward model explains only about 53% of the ℓ = 1 amplitude; the remaining ≈47% is explicitly open, so the systematics attribution is not quantitatively closed.

[MAJOR] Section IV D / residual-amplitude reasoning: the statement that a 0.695% harmonic residual would be “undetectable” in real space yet “excluded at 95% recovery” is statistically incorrect; being below A95 means the estimator would not reliably recover such a signal, not that such a signal is excluded.

[MAJOR] Sections VI B, VII / sensitivity and falsification: A50 and A95 are injection-recovery detection-completeness thresholds, not confidence intervals or upper limits; using them as a falsification boundary for physical models overstates what the analysis establishes.

[MAJOR] Appendix A / MASTER analysis conventions: Table V mixes different footprints, weights, field normalizations, null sizes, and mean-subtraction conventions, and retains mutually different +3.64 and +7.93 canonical values; saying these are “not comparable” is not enough for a PRD-quality statistical presentation.

[MAJOR] Section VI C / PRD relevance and parity framing: the paper concedes that the ℓ = 1 chirality dipole is parity-even and that no transfer function to primordial parity-violating sectors is derived, so the connection to fundamental parity-violation physics is too weak for the current framing.

[MINOR] Data Availability / reproducibility: the manuscript cites mutable repository paths and promises a future DOI/tag; acceptance should require an immutable archival release containing the exact catalog, model, scripts, random seeds, masks, and null distributions used for every quoted number.

(3) The central claim is supported only in the narrow sense that the preselected high-confidence real-space estimator is consistent with null, but the broader claims of a full-catalog null, sub-percent physical constraint, Shamir-scale exclusion/tension, and complete systematics attribution are not yet supported by the evidence presented.
