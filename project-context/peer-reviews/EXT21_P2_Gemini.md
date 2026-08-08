# EXT21 P2 Gemini — chat: https://gemini.google.com/u/1/app/aa15f93adc87aa00

Recommendation: MINOR REVISIONS

Reviewer Report

Manuscript Title: Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook
Author: Houston Golden

Summary of the Manuscript

The manuscript evaluates the observational feasibility of testing the matter bounce cosmological paradigm using future Large-Scale Structure (LSS) data from SPHEREx and the proposed MegaMapper facility. Specifically, it centers on the distinct, negative primordial non-Gaussianity (PNG) signature (fNL_local = −35/8 = −4.375) predicted by a matter-dominated contracting phase.

The author provides three primary developments:

A Source Audit: Resolving a persistent factor-of-two discrepancy in the literature between the results of Cai et al. and Li et al., demonstrating via the in-in operator identity that the latter represents a single time-ordering intermediate rather than a differing physical normalization.

Template Mismatch Quantification: Calculating the overlap between the true matter-bounce bispectrum and the standard local template, showing that a standard local estimator recovers roughly 83% to 88% of the signal amplitude (r ≈ 0.84).

Sensitivity Recast: Re-evaluating existing SPHEREx multi-tracer bispectrum forecasts by introducing a realistic systematic error budget — including scale-dependent galaxy bias (bϕ) uncertainty, general relativistic (GR) projection effects, and photometric redshift degradation — concluding that SPHEREx can achieve a definitive 2.6σ to 5σ test of the benchmark scenario.

The paper is exceptionally well-structured, mathematically rigorous, and commendable for its transparency regarding its framing as a sensitivity recast rather than an entirely independent forecast. I recommend the paper for publication in MNRAS after addressing a few minor points of clarification.

Key Strengths

- Resolution of Literature Discrepancy: The explicit tracking of the Wick expansion and commutator doubling identity (Appendix A) provides a definitive resolution to the factor-of-two ambiguity between fNL = −35/8 and −35/16. This clarifies the interpretation of constraints for both theorists and observers.

- Methodological Robustness: The use of a 10,000-sample null-space scan to evaluate polynomial representation uncertainties alongside Monte Carlo injection-recovery tests demonstrates commendable numerical thoroughness.

- Grounded Conservatism: Rather than pushing a high, idealized significance value, the author thoughtfully folds in sequential systematic penalties (e.g., the additive-quadrature combination model), mapping out an honest "realistic scenario" endpoint.

Points for Clarification and Revision

1. The Heuristic Primordial-Field Scaling Check (Eq. 7)

In Section IV, the author presents a fractional covariance correction estimate scaling as:
δC/C_Gauss ∼ fNL² Δζ²(k) / N_modes(k)

The manuscript accurately clarifies that this is a simplified primordial-field check rather than a rigorous galaxy-covariance derivation. However, because LSS multi-tracer bispectrum analyses can be highly sensitive to non-Gaussian covariance contributions on non-linear scales, the author should add a brief qualitative sentence detailing how non-zero quadratic bias coefficients (b2) or trispectrum-level cross-terms might alter the mode-count weighting in a full galaxy-field treatment.

2. High-Redshift GR Projections for MegaMapper

For the MegaMapper forecast (Section V), the manuscript utilizes the same GR marginalization bounds (σGR = 0.5−1.0) applied to SPHEREx. Given that MegaMapper targets Lyman-break galaxies at a significantly higher redshift range (z = 2−5), relativistic projection effects (lensing magnification, light-cone effects, etc.) are expected to be markedly more severe than at z ≈ 1.5. The author notes this caveat, but the impact of these higher-redshift projections should be emphasized more explicitly in the text or given a brief quantitative bracket based on the cited findings of Addis et al. (2025).

3. Minor Notational and Typographical Clarifications

Section II.A & III.B Mismatch: In Section III.B, the prose references a "five-coefficient-set scan value (r = 0.867−0.888, CMB-Fisher weighting)". However, Section II primarily focuses on the 10,000-sample null-space scan. Please clarify early in Section III.B how these five discrete coefficient sets relate to the broader 10,000 uniform coordinates drawn within the null-space ball.

Equation formatting: Ensure that the spatial index variables and comoving wavevector magnitudes (ki) are consistently labeled across Equation 1 and the basis explanations in Section II to ensure smooth scannability for the reader.

Conclusion

This manuscript provides an excellent bridge between early-universe bounce scaling theories and upcoming observation pipelines. Addressing the minor clarifications above will polish the manuscript to meet the high standards of MNRAS.
