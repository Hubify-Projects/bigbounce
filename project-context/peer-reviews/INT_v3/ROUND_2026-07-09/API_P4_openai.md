# INT API Review — P4 v1.0.223 — openai (gpt-5.5)
paper: P4  version: v1.0.223  model: gpt-5.5
modality: native-PDF (Files API input_file)
UTC: 2026-07-10T07:39:04.349919Z  |  latency: 81.1s  |  attempt: 1
usage: {"input_tokens": 59974, "input_tokens_details": {"cache_write_tokens": 0, "cached_tokens": 0}, "output_tokens": 2158, "output_tokens_details": {"reasoning_tokens": 516}, "total_tokens": 62132}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

1. [MAJOR] Secs. III B, IV C, VI B, VII — The primary scientific claim is not consistently defined: the headline null uses the high-confidence peq > 0.6 real-space estimator, while the “clean 1.7% dipole disfavored at z ≈ −7.6” uses a different full-sample WLS/template estimator with a different selection function and an acknowledged non-frequentist bootstrap statistic; these should not both be presented as coequal “primary” cosmological constraints without a single unified likelihood or clearly separated claims.

2. [MAJOR] Secs. II, IV A, VI A, VI B — The physical interpretation of the dipole sensitivity is not established because injection-recovery is performed on observed hard labels, not through the image classifier, non-spiral triage, confidence selection, or spatially varying confusion matrix; therefore the quoted A50 ≈ 0.75% and A95 ∈ (1.0%, 1.5%] are only thresholds for the catalog label field, not for true galaxy chirality or cosmological spin/morphology signals.

3. [MAJOR] Secs. II, VI A, Appendix B — The classifier validation is insufficient for sub-percent cosmological inference: 66.5% of training labels are CE-ResNet pseudo-labels, the independent GZ1 chirality accuracy is only 69.91% with κ = 0.40, and the fully human GZ1-only cross-check has A50 ≈ 3.4% and A95 ≈ 4.5–6.8%, so it cannot validate the sub-percent null or exclude inherited large-scale pseudo-label structure at the claimed sensitivity.

4. [MAJOR] Secs. IV C–IV D, VII, Appendix D — The manuscript reports large harmonic residuals, including +7.28σ and +7.93σ diagnostics, and then attributes them to systematics although the forward model accounts for only ≈53% of the residual amplitude; this unresolved ≈47% remainder cannot simply be declared irrelevant without a quantitative joint model showing that it cannot project onto the real-space dipole estimator or mimic the template being constrained.

5. [MAJOR] Secs. III A, IV C, IV D, Table V, VII — The treatment of significances is confusing and potentially misleading: multiple incommensurable z values are repeatedly juxtaposed, the canonical MASTER result changes from +3.64σ to +7.93σ depending on null/run convention, and the text retains both for “continuity”; a PRD publication requires one declared statistic per claim, with all alternative diagnostics clearly demoted and not used rhetorically.

6. [MAJOR] Secs. IV C, VI B, Appendix D — The “exclusion” or “disfavor” of Shamir-scale amplitudes is not a calibrated frequentist or Bayesian exclusion and is not based on Shamir’s estimator, selection, labeling method, or footprint; the manuscript should substantially weaken all exclusion language and restrict itself to a sensitivity comparison under the present catalog-label estimator unless a matched reanalysis is performed.

7. [MAJOR] Secs. IV A, Appendix B — The catalog probabilities are severely miscalibrated, with top-label confidence ≈0.951 versus external accuracies of 0.587 three-class and 0.699 chirality; since peq defines the primary sample, monotone recalibration invariance of hard labels is not sufficient to rule out spatially varying selection bias from confidence, depth, morphology, or imaging leg.

8. [MAJOR] Secs. IV C, Appendix E — The low-confidence tail gives a z ≈ 4.0–4.3 real-space excess and the unthresholded full sample has a detectable dipole-like signal; the decision to discard this population may be reasonable, but the manuscript needs a pre-analysis, externally validated purity/completeness justification rather than relying primarily on an asserted commit hash and post hoc systematics attribution.

9. [MAJOR] Secs. IV D, Appendix D — The “eight-anchor” systematic battery is largely qualitative and ad hoc: several anchors are only suggestive, some use small null ensembles, the cross-spectrum evidence is based on 200 realizations, and no joint nuisance covariance or posterior is provided; it does not meet the standard needed to convert a high-significance residual into a quantitatively controlled systematic.

10. [MAJOR] Sec. VI C — The connection to parity-violating sectors is overstated: the manuscript itself states that the ℓ = 1 chirality dipole is parity-even and that no transfer function from primordial parity violation to projected galaxy morphology is derived, so claims about constraining cosmic birefringence, Chern-Simons gravity, or early-universe parity-violating scenarios should be removed or reduced to speculative motivation.

11. [MAJOR] Data Availability / reproducibility — The submission relies heavily on artifact paths, live repository state, non-frozen branches, and future Zenodo deposits; for a real submission, all scripts, catalogs, exact commits, checksums, null arrays, and trained weights needed to reproduce the quoted numbers must be archived immutably before review.

12. [MINOR] Overall presentation — The manuscript is excessively long, repetitive, and self-justifying, with many caveats repeated verbatim; it should be substantially shortened and reorganized around a small number of well-defined estimators, nulls, and claims.

13. [MINOR] Tables I–III and V — The decision-tree and significance-convention tables are useful but redundant and sometimes inconsistent in terminology; consolidate them into one clear estimator/claim/null table.

14. [MINOR] Sec. IV B — The global CW fraction differs from 0.5 at −9.47σ and is called a classifier artifact; this conclusion should be supported by an explicit external handedness-symmetric validation or local renormalization test, not only by slab uniformity.

15. [MINOR] Sec. IV C — The quoted dipole direction (l, b) = (293°, 12°) is statistically meaningless at 0.41σ and should either be removed from the abstract/main conclusions or explicitly placed only in a diagnostic table.

16. [MINOR] Sec. VI B — The notation for amplitudes A, Ap, fCW deviations, “full amplitude,” and Shamir asymmetries is clearer than in many papers but still repeatedly re-explained; define once and use consistently.

17. [MINOR] Appendix B — The flip-identity QC issue, affecting 2.9% of rows and 6.3% of the HC sample, should be summarized in the main data-quality section rather than buried in the appendix/data availability.

18. [MINOR] Appendix D — The WLS design is rank-deficient with exactly collinear leg templates; although the authors argue the dipole subspace is stable, the main text should not quote nuisance coefficients from a singular design matrix.

19. [MINOR] Figures 4, 7, 8, 9 — Several figures mix diagnostic and primary quantities; captions should explicitly state whether the plotted field is full sample or HC, Ap or fCW, pre-MASTER or post-MASTER, and whether the displayed significance is primary or diagnostic.

20. [MINOR] Abstract — The abstract is too dense and contains too many caveats, numerical diagnostics, and internal methodological distinctions; it should state the catalog, primary estimator, primary null result, and principal limitations succinctly.

(3) The central claim that the selected high-confidence catalog-label real-space dipole is consistent with zero is supported, but the broader sub-percent physical/cosmological exclusion claims are not yet supported to PRD publication standard.