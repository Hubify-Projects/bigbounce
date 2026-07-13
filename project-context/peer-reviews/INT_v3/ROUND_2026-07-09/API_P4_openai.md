# INT API Review — P4 v1.0.239 — openai (gpt-5.5)
paper: P4  version: v1.0.239  model: gpt-5.5
modality: native-PDF (Files API input_file)
UTC: 2026-07-13T07:43:08.386546Z  |  latency: 88.6s  |  attempt: 1
usage: {"input_tokens": 61937, "input_tokens_details": {"cache_write_tokens": 0, "cached_tokens": 0}, "output_tokens": 1946, "output_tokens_details": {"reasoning_tokens": 516}, "total_tokens": 63883}
PARSED VERDICT: REJECT

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: REJECT.

(2) ISSUES:

1. [MAJOR] Secs. III B, IV C, VI B, Conclusions — The “primary” null result is based on a post-classification high-confidence cut on uncalibrated network scores, while the strongest exclusion claim uses a different full-sample WLS/template estimator; the manuscript repeatedly acknowledges that these are different samples/nulls/covariances, but nevertheless combines them rhetorically into one cosmological conclusion.

2. [MAJOR] Secs. IV C–IV D, Appendix D — The harmonic channel shows highly significant residuals (+3.64σ, +7.28σ, +7.93σ depending on convention), only about half of which is forward-modeled, yet the paper asserts a null cosmological interpretation; treating these residuals as “diagnostic only” does not remove the need for a statistically coherent explanation before making cosmological exclusion statements.

3. [MAJOR] Secs. III A, IV C, IV D, VII — The paper reports many non-commensurable significances under different nulls, masks, fields, weights, sample cuts, and MC sizes, then asks the reader not to compare them; this is not an acceptable substitute for a single likelihood or clearly calibrated test statistic supporting the claimed null/exclusion.

4. [MAJOR] Secs. II, VI A, Appendix B — The classifier-label foundation is insufficient for a precision cosmological null: 66.5% of training labels are CE-ResNet pseudo-labels, the independent GZ1 chirality accuracy is only 69.91% with κ = 0.40, and the softmax probabilities are strongly miscalibrated; the manuscript does not demonstrate that spatially varying classifier confusion is controlled at the sub-percent level required by the headline claims.

5. [MAJOR] Sec. VI B — The injection-recovery calibration injects dipoles into the observed hard-label CW/CCW field, not into images or into a realistic morphology/selection/classifier pipeline; therefore the quoted A50 and A95 are not demonstrated physical sensitivity thresholds for true galaxy chirality dipoles.

6. [MAJOR] Secs. IV C, VI B, Appendix B/E — The image-level mirror-flip test does not establish sensitivity to real chirality signals, because mirror flipping enforces the equivariance protocol rather than testing whether the classifier correctly recognizes physical spiral handedness as a function of depth, morphology, redshift, seeing, and inclination.

7. [MAJOR] Secs. IV B, IV D, Appendix D — The catalog has a statistically enormous global CW/CCW monopole artifact (−9.47σ), and the manuscript demonstrates that mask leakage from such artifacts can generate low-ℓ power; this directly undermines the use of the same catalog for sub-percent dipole inference unless the systematic model is closed quantitatively, which it is not.

8. [MAJOR] Secs. IV C, V, VI C, VII — The comparison with Shamir’s claimed amplitudes is overinterpreted: the manuscript alternates between saying the result “disfavors,” “excludes,” is in “tension,” and is not a frequentist exclusion of Ganalyzer; without a matched-footprint, matched-selection reanalysis, only a limited pipeline-specific comparison is justified.

9. [MAJOR] Appendix D — The block-bootstrap WLS “z ≈ −7.6” exclusion is not a calibrated frequentist or Bayesian exclusion, uses a model-dependent covariance and full-sample field distinct from the primary HC estimator, and omits classifier-label uncertainty as a jointly marginalized nuisance; it should not be presented as a primary cosmological result.

10. [MAJOR] Secs. III B, IV C — The asserted pre-registration of the peq > 0.6 cut via a code commit is not a convincing analysis-blinding or pre-registration record for a PRD-level cosmological claim, especially given the extensive subsequent confidence-cut/systematics exploration and manuscript-level estimator hierarchy.

11. [MAJOR] Sec. IV C and Appendix A — The MASTER analysis is internally confusing: different rows use Ap, Ap/2, different mean subtractions, different masks, different weights, different MC sizes, and different single-mode/bandpower conventions; the resulting Cℓ amplitudes and significances are not presented in a sufficiently clean, reproducible statistical framework.

12. [MAJOR] Sec. VI C — The discussion of parity-violating sectors is speculative and not supported by a transfer function from primordial parity violation or Chern-Simons/birefringence physics to projected spiral-arm chirality; the claimed relevance to PRD-style fundamental-physics constraints is therefore weak.

13. [MAJOR] Secs. IV C, VI B — The stated “falsification” criterion is not a statistical upper limit, not a likelihood interval, and not propagated through the classifier/selection function; it should not be used to claim that all Shamir-scale or parity-sector signals would necessarily have been detected.

14. [MAJOR] Secs. IV D, Appendix D/E — Several important systematics are explicitly left as “open items” or “pod-deferred,” including the remaining ∼47% harmonic residual and the full per-pixel depth/PSF/morphology/confusion model; these are central, not optional, for the claimed sub-percent null.

15. [MINOR] Entire manuscript — The presentation is far too long, repetitive, and defensive for a research article; many caveats are repeated multiple times, while the actual statistical logic becomes harder rather than easier to follow.

16. [MINOR] Abstract and Conclusions — The abstract contains too many parenthetical qualifications, estimator caveats, and numerical claims; it should state a small number of clean results with one consistent convention.

17. [MINOR] Secs. II–IV — The notation for amplitudes in fCW units versus Ap units is repeatedly clarified but still remains a source of confusion; all amplitude comparisons should be standardized in one convention.

18. [MINOR] Figures 4, 7, 8, 9 — Several figures mix diagnostic and primary quantities without sufficiently prominent visual distinction; readers could easily mistake systematics-diagnostic harmonic significances for cosmological detections.

19. [MINOR] Data Availability — The archival DOI and immutable release information are not yet provided, despite many claims depending on committed artifacts; a submission should contain frozen reproducibility identifiers.

20. [MINOR] Acknowledgments — The extensive AI-assisted methodology statement is acceptable in principle, but it does not replace standard reproducibility, statistical validation, or independent verification of the analysis.

(3) The central claim of a null dipole in the selected classifier-label real-space estimator is plausibly suggested, but the broader cosmological null/exclusion claims are not adequately supported.