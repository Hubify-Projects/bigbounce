# EXT POSTPOLISH 2026-07-06 — P4 — Gemini

- **Provider:** Gemini (houston@bamf.com, Ultra, /u/1/)
- **Model/effort:** 3.5 Thinking
- **Chat URL:** https://gemini.google.com/u/1/app/35222c044339191b
- **PDF:** P4_v1.0.219.pdf (md5 54118d50f6768507e4e22ec5611cf33b)
- **Harvested:** 2026-07-07
- **Parsed verdict (from response):** MAJOR REVISIONS

## Raw verbatim response

(1) VERDICT: MAJOR REVISIONS
(2) ISSUES:

[MAJOR] Section IV.D (Monopole+Mask Leakage Generative Null): The imaging-systematic forward model accounts for only 52% to 54% of the post-MASTER l=1 harmonic residual amplitude. Leaving approximately 47% of the residual amplitude open and unmodeled prevents complete systematic closure.

[MINOR] Section II.B (Training Labels): A large fraction (66.5%) of the training labels are derived from prior CE-ResNet predictions. This high dependence introduces potential propagation of inherited model-specific selection or structural biases into the training pipeline.

[MINOR] Appendix E (Morphology Systematics): While soft probabilities preserve exact flip-symmetry under the test-time averaging procedure, the subsequent non-linear hard-argmax operation breaks this linearity, leaving a potential channel where a spatially coherent argmax tie-break bias could persist on borderline objects.

(3) The central claim that the large-scale chirality dipole of spiral galaxies is consistent with null is supported by the primary real-space dipole estimators and block-bootstrap template exclusions evaluated on the pre-specified high-confidence catalog sample.
