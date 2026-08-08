# INT API Review — P4 v1.0.223 — openai (gpt-5.5)
paper: P4  version: v1.0.223  model: gpt-5.5
modality: native-PDF (Files API input_file)
UTC: 2026-07-10T06:46:03.219377Z  |  latency: 79.1s  |  attempt: 2
usage: {"input_tokens": 59732, "input_tokens_details": {"cache_write_tokens": 0, "cached_tokens": 58112}, "output_tokens": 2214, "output_tokens_details": {"reasoning_tokens": 818}, "total_tokens": 61946}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

1. [MAJOR] Secs. II, IV C, VI B — The quoted sub-percent “sensitivity” is calibrated on injected hard-label CW/CCW catalog fields, not on images passed through the classifier, not-spiral triage, confidence selection, and depth-/morphology-dependent confusion. With an external chirality accuracy of only 69.91% and substantial not-spiral/edge-on leakage, the manuscript cannot presently translate the observed-label null into a physical chirality-dipole bound at the advertised precision without an image-level or at least spatially conditioned confusion-transfer calibration.

2. [MAJOR] Secs. III B, IV C — The primary result depends on the peq > 0.6 high-confidence cut, while the unthresholded catalog shows a z ≃ 4.2–4.4 real-space excess. The manuscript argues this away as a low-confidence systematic, but the confidence score is explicitly uncalibrated and spatially survey-dependent; a post-hoc git-commit “pre-registration” is not a substitute for a demonstrated selection-function model. The paper must show that the HC selection does not itself remove or attenuate a real dipole in a direction-/depth-dependent way.

3. [MAJOR] Secs. III A, IV C, IV D, Table V — The statistical framework is fragmented into many non-commensurable nulls, z-values, and p-values. The manuscript repeatedly states that they are not comparable, yet still uses them jointly to support a cosmological conclusion. A coherent likelihood or at least one clearly defined primary hypothesis test with a valid null including survey systematics is required.

4. [MAJOR] Secs. III B, IV D, Appendix D — The “z ≈ −18” block-bootstrap WLS template disfavor is not a calibrated frequentist exclusion, is performed on a different sample from the primary HC dipole, and uses a simplified block bootstrap that does not propagate classifier-label uncertainty or the HC selection. It should not be listed as a “primary cosmological estimator” or used rhetorically as an exclusion of a 1.7% dipole unless replaced by a proper joint nuisance likelihood.

5. [MAJOR] Secs. IV C–IV D, Appendix A — The harmonic channel contains large residuals (+3.64σ, +7.28σ, +7.93σ depending on convention), and only about 53% of the post-MASTER residual amplitude is forward-modeled. The remaining ∼47% is declared “below the real-space recovery threshold,” but this does not demonstrate it is non-cosmological or harmless, especially since it is at exactly the low-ℓ scale relevant to the claimed observable. The systematic attribution remains qualitative rather than quantitatively marginalized.

6. [MAJOR] Secs. II, VI A — The training set is dominated by CE-ResNet pseudo-labels, while the “independent” GZ1-human-only cross-check has N ≃ 4.6 × 10^4 and a sensitivity floor of several percent. This cross-check can only rule out very large inherited dipoles and does not validate the headline sub-percent null against pseudo-label-inherited survey structure.

7. [MAJOR] Secs. IV C, VI B — The pixel-permutation and label-shuffle nulls are inadequate as cosmological nulls because they destroy spatial correlations and assume labels are exchangeable with respect to depth, seeing, morphology, imaging leg, and footprint. These nulls can diagnose random-label noise but cannot by themselves bound position-dependent classifier bias, which is precisely the dominant concern.

8. [MAJOR] Secs. IV B, VI C — The manuscript mixes parity language and isotropy-breaking language in a potentially misleading way. It correctly notes that the ℓ = 1 chirality dipole is parity-even, but then repeatedly frames the result in relation to parity-violating sectors. The physical connection to primordial parity violation is speculative without a transfer function and should be sharply downgraded.

9. [MAJOR] Secs. IV C, V, VII — The comparison with Shamir is not statistically well defined. The manuscript alternates between fCW-deviation units and Ap units and gives amplitude-level “7–18× tension” while conceding that no matched Ganalyzer reanalysis has been performed. This should be reduced to a qualitative methodological comparison unless a matched-footprint, matched-estimator analysis is supplied.

10. [MAJOR] Appendix B — The classifier validation is insufficient for the stated scientific use. The catalog is strongly overconfident, D4 TTA changes argmax labels in 21.4% of borderline cases, and the GZ1 confusion matrix gives only moderate agreement. These facts are not compatible with treating the classifier as a precision chirality instrument without a spatially resolved calibration model.

11. [MINOR] Throughout — The manuscript is excessively long, repetitive, and internally self-justifying. Many caveats are repeated multiple times, while the actual statistical logic is obscured. It should be substantially shortened and reorganized around one primary estimator, one null hypothesis, and one systematic-error budget.

12. [MINOR] Tables I–III, V, IX — The table structure is confusing and sometimes redundant. The manuscript should separate “results,” “diagnostics,” and “calibrations” cleanly and avoid placing non-comparable σ-values in adjacent summary tables.

13. [MINOR] Sec. IV A, Appendix B, Data Availability — The flip-identity QC issue affecting 2.9% of rows is concerning and should be moved from caveat/provenance language into the main catalog-validation section, with a clear statement of which columns are reliable for external users.

14. [MINOR] Data Availability — The absence of an immutable DOI/tagged archival release at submission is not acceptable for a data- and artifact-heavy claim. The exact code, catalog version, model weights, masks, null arrays, and random seeds used for the submitted manuscript must be frozen.

15. [MINOR] Figures 4, 7, 8, 9 — Several figures are visually dense or use different field conventions without sufficient visual labeling. The figures should state directly whether the plotted quantity is fCW, Ap, pseudo-Cℓ, MASTER-decoupled Cℓ, or an injected-amplitude recovery statistic.

(3) The central claim is supported only in the narrow sense that the authors’ selected high-confidence observed-label catalog shows no significant real-space dipole under their permutation null, but the broader physical/cosmological sub-percent null and exclusion claims are not yet adequately supported.