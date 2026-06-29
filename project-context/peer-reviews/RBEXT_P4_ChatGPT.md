# RBEXT P4 ChatGPT — chat: https://chatgpt.com/c/6a42c300-1d94-83e8-8c84-9cf63525829d
VERDICT: MINOR REVISIONS

Provider: ChatGPT (default/Instant tier)
PDF: RBEXT_P4.pdf | md5: cdec310d3a1f3408777da0df5ae2d4a8
Harvested: 2026-06-29

---

1. Recommendation: MINOR REVISIONS

Strong, unusually transparent catalog/systematics paper. I would accept after targeted fixes, not require a major rewrite. The paper's primary null result is well-supported, but a few presentation and methodological loose ends must be tightened before publication.

2. BLOCKERS

None.

3. MAJORS

- Primary-vs-diagnostic hierarchy is still too complex. The manuscript repeatedly states that +0.41σ real-space HC dipole and WLS clean-dipole exclusion are primary, while +3.64σ/+7.93σ/+7.28σ MASTER results are diagnostic. This is credible, but the abstract and conclusions still overload the reader with many non-comparable σ values. Require a compact "do not compare these" table early, with one primary result box.
- Pseudo-label dependence remains an important limitation. Since 66.5% of training labels derive from CE-ResNet, the production catalog is not fully independent of prior chirality-label structure. The paper acknowledges this and proposes a GZ1-only retraining follow-up, but for a catalog paper this should be framed more explicitly as a limitation of the current release, not just future work.
- Classifier calibration/accuracy limits need stronger front-end warning. Independent GZ1 three-class accuracy is only 58.7%, chirality accuracy 69.91%, κ=0.40. The data-release section should warn users more prominently that peq is a ranking score, not a calibrated probability.
- Unthresholded z≈4.2–4.4 excess deserves clearer "why not primary" justification. Make the pre-specified threshold provenance and systematic attribution more explicit, preferably with one figure/table showing z versus confidence cut.

4. MINORS

- Abstract is too dense and risks confusing readers with distinct null conventions.
- The +3.64σ versus +7.93σ canonical MASTER distinction is still awkward; consider moving one to appendix-only.
- "Largest chirality-labeled catalog to date" should be hedged with exact comparison basis.
- Edge-on contamination discussion is partly qualitative pending axis-ratio cross-match; label it as such consistently.
- Some artifact-path references are excessive for journal prose; consolidate into reproducibility appendix.
- The Shamir comparison is fair, but "factor 4–9" should always be paired with "under this pipeline, not likelihood-level exclusion."

5. Strengths

- Very strong transparency about null definitions, estimator hierarchy, and non-comparable σ conventions.
- Excellent bias-hardening: equivariant TTA, confidence sweeps, mask/weight tests, MASTER diagnostics, block bootstrap, and nuisance-template fits.
- Valuable community catalog: 8.47M galaxies, 3.2M spirals, released probabilities/weights/scripts.
- The monopole-mask leakage demonstration is important and likely broadly useful for future chirality studies.
- The paper is unusually careful in not overclaiming the harmonic residuals as cosmological detections.
