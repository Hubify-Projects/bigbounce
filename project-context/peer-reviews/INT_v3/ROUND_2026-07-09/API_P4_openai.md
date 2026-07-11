# INT API Review — P4 v1.0.236 — openai (gpt-5.5)
paper: P4  version: v1.0.236  model: gpt-5.5
modality: native-PDF (Files API input_file)
UTC: 2026-07-11T15:03:01.285098Z  |  latency: 102.4s  |  attempt: 1
usage: {"input_tokens": 62065, "input_tokens_details": {"cache_write_tokens": 0, "cached_tokens": 0}, "output_tokens": 2193, "output_tokens_details": {"reasoning_tokens": 516}, "total_tokens": 64258}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

1. [MAJOR] Secs. III–IV, “primary estimator” hierarchy: the manuscript repeatedly reports large, significant low-ℓ residuals in the harmonic channel (+3.64σ, +7.28σ, +7.93σ) while declaring them diagnostic and non-cosmological, but the statistical relationship between these residuals and the primary real-space null is not modeled. Stating that the σ values are “not comparable” is not sufficient; the paper needs a coherent joint statistical model or a much narrower claim restricted to the selected real-space estimator.

2. [MAJOR] Secs. IV C, VI B, VII, injection-recovery/falsification threshold: the quoted A50≈0.75% and A95∈(1.0%,1.5%] are observed-label injection thresholds, not image-level or physical chirality thresholds. The text sometimes treats them as constraints on physical cosmological dipoles. A full image-level injection through classification, confidence selection, and survey-dependent confusion is needed, or the claims must be explicitly weakened to “observed classifier-label dipoles.”

3. [MAJOR] Secs. II, VI A, Appendix B, classifier validation: 66.5% of the training labels come from CE-ResNet pseudo-labels, the independent GZ1 chirality accuracy is only 69.91% with κ=0.40, and the catalog probabilities are severely overconfident. This is a weak basis for sub-percent cosmological inference unless a spatially resolved confusion model is propagated. The leg-stratified GZ1 test is useful but insufficient to exclude RA/Dec-, depth-, seeing-, morphology-, and redshift-dependent differential CW↔CCW errors at the required level.

4. [MAJOR] Sec. IV C, confidence cut peq>0.6: the primary null appears only after excluding the low-confidence tail, while the full unthresholded sample shows a z≈4.2–4.4 real-space excess. The manuscript argues this is systematics, but the confidence cut is based on an uncalibrated network score and the selection function is not propagated into all estimators. This needs a pre-defined validation-based selection criterion, an explicit selection-function model, and a demonstration that cosmological signals would not be preferentially removed.

5. [MAJOR] Secs. IV D and Appendix D, systematics attribution: the forward model explains only ≈53% of the post-MASTER ℓ=1 residual amplitude, leaving ≈47% unresolved. The paper then asserts that the remainder is likely survey systematic and below the real-space recovery threshold. That is plausible but not demonstrated; an unexplained coherent residual in a nominally null observable cannot be dismissed without a quantitative nuisance model and posterior bound.

6. [MAJOR] Sec. IV C and Appendix A, null construction: the primary pixel-permutation null preserves the one-point distribution of Ap but does not naturally preserve the heteroscedastic binomial noise, depth correlations, morphology correlations, or survey-mask covariance. The label-shuffle cross-check helps, but the paper should make the per-galaxy/binomial null primary or demonstrate analytically and empirically that the pixel-permutation null has correct coverage for the actual estimator.

7. [MAJOR] Secs. III A, IV C, VII, inconsistent use of significances: the paper contains many σ values from incompatible procedures, and despite repeated caveats it still uses them rhetorically to support conclusions. The manuscript should remove nonessential σ claims, replace them with clearly defined likelihoods or empirical p-values, and avoid comparing harmonic-channel completeness to real-space falsification thresholds.

8. [MAJOR] Secs. V–VII, comparison with Shamir: the claimed “factor ∼3.7–8.8 tension” and z≈−7.6 “clean 1.7% dipole disfavor” are not a like-for-like comparison with Shamir’s Ganalyzer samples, cuts, redshift distributions, and estimator. The manuscript acknowledges this but still overstates the implication. The comparison should be framed as sensitivity to an idealized clean dipole only, not as tension with a specific published result.

9. [MAJOR] Secs. VI C and Introduction, physical interpretation: the connection to parity violation, Chern-Simons gravity, cosmic birefringence, and primordial chiral tensors is speculative and unsupported by a transfer function from primordial parity-violating physics to projected apparent spiral handedness. For PRD, either provide a quantitative theory mapping or substantially reduce these claims.

10. [MAJOR] Sec. IV B, global CW monopole: the catalog has a highly significant global CW/CCW imbalance, explicitly attributed to classifier/training artifact. Since a monopole is the parity-odd chirality channel, this undermines the use of the same catalog for parity-related statements unless local monopole subtraction and its uncertainty are incorporated rigorously throughout.

11. [MAJOR] Appendix D, block-bootstrap WLS “exclusion”: the z≈−7.6 statistic is not a calibrated frequentist exclusion, uses the full Catalog C field rather than the high-confidence primary sample, and does not include classifier-label uncertainty in the covariance. It should not be listed as a “primary cosmological estimator” unless converted into a properly calibrated likelihood or downgraded to a diagnostic.

12. [MAJOR] Appendix B/E, hard-argmax and flip-equivariance: flip-TTA enforces soft-probability equivariance, but the analysis uses hard argmax counts after confidence selection. The manuscript acknowledges that argmax can reintroduce nonlinear effects, especially for borderline/edge-on objects, but does not propagate this into the main error budget.

13. [MINOR] Sec. II B: the training-set accounting is confusing: 25,790 source images, 26,616 combined pool, 21,293 post-augmentation training, and 5,323 validation are described in a way that is hard to audit. Present this once in a clean table in the main text.

14. [MINOR] Sec. IV A and Appendix B: the “flip identity” QC problem affecting 2.9% of rows is concerning and should be introduced earlier and more plainly. Readers should not have to infer that some raw/equivariant probability columns are inconsistent.

15. [MINOR] Sec. IV C: the quoted best-fit dipole direction (l,b)=(293°,12°) is meaningless at 0.41σ and should be removed from the abstract and main conclusions, or clearly relegated to a diagnostic table.

16. [MINOR] Tables I–III: the decision-tree tables are repetitive and partly inconsistent in terminology. Consolidate into one concise estimator table with sample, field, mask, null, statistic, and scientific role.

17. [MINOR] Secs. IV–VII: the manuscript is excessively long and defensive, with many caveats repeated multiple times. A PRD article should be shortened and reorganized around a small number of well-defined statistical tests.

18. [MINOR] Figures 4, 7, and 8: the maps and power-spectrum plots need clearer labeling of field convention, mask, weighting, and whether the plotted quantity is Ap, fCW, pseudo-Cℓ, or MASTER-decoupled Cℓ.

19. [MINOR] Data availability: the absence of a frozen DOI/commit hash at submission is not acceptable for a reproducibility-heavy paper. The archival snapshot should exist before review, not be promised for later.

20. [MINOR] AI-assisted methodology statement: acceptable in principle, but the manuscript should emphasize reproducible code and artifacts rather than the particular AI models used, which are irrelevant to the scientific validation.

(3) The central claim is supported only in the narrow sense that the selected high-confidence classifier-label real-space dipole is consistent with null, but the broader cosmological null and exclusion claims are not yet fully supported.