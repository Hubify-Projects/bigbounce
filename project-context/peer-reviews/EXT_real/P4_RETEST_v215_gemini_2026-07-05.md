# P4 v1.0.215 EXT re-test — GEMINI

- Reviewer: Gemini (houston@bamf.com Ultra /u/1/, Gemini Pro)
- Date: 2026-07-05 (run 2026-07-06)
- PDF: /tmp/retest_P4_v215.pdf (976281 B)
- Chat URL: https://gemini.google.com/u/1/app/fbc6349c8f4c12e5
- Prompt: standard PRD referee prompt (verdict + [MAJOR]/[MINOR] issues + central-claim sentence)
- Verdict (verbatim from response): **MAJOR REVISIONS**

## RAW VERBATIM RESPONSE

As an AI, I do not possess personal feelings, but I can evaluate this manuscript with the rigorous, objective, and candid lens required for a submission to Physical Review D.

VERDICT
MAJOR REVISIONS

ISSUES

[MAJOR] Section IV D (Quantitative forward model of the residual amplitude): The author notes that ≈47% of the +3.64σ canonical-mask residual amplitude is not captured by the imaging and morphology templates. The author defers the creation of a full per-pixel classifier confidence-vs-depth response map to "dedicated compute" in future work. While the primary real-space dipole is conclusively null, leaving nearly half of the harmonic residual explicitly unmodelled weakens the overarching claim that the l=1 excess is fully explained by survey systematics. This remainder must be more tightly bounded or formally incorporated into a joint spatial likelihood.

[MAJOR] Appendix E (Edge-on galaxy contamination): The manuscript reveals that 15.8% of the spirals feeding the dipole analysis are actually edge-on systems mislabelled as clockwise or counter-clockwise. The author argues that Test-Time Augmentation (TTA) symmetrizes the soft probabilities for these objects. However, the author acknowledges that the hard-argmax step is non-linear and flips labels on borderline cases, which could theoretically preserve a spatially coherent directional bias. Relying primarily on a p_eq > 0.8 confidence sweep to dismiss this bias is indirect; a direct quantification of the spatial coherence of the argmax tie-break on edge-on systems is required.

[MINOR] Section IV C and Table V (Clarity and Readability): The manuscript's defensive density—specifically the rapid succession of significance values derived from distinct null conventions (e.g., +3.64σ, +7.28σ, +7.93σ)—makes the text exceptionally difficult to parse. While the author explicitly states these are not mutually comparable, presenting them in such close proximity invites the very confusion the author is trying to prevent. A streamlined presentation focusing exclusively on the primary estimators in the main text, moving the diagnostic nulls to the appendices, would greatly improve scannability.

[MINOR] Appendix D (WLS template fit conditioning): The linear dependence of the three imaging-leg fraction templates with the constant term results in a rank-deficient design matrix with a condition number of 4.5×10^16. The author mitigates this by dropping one leg to achieve a well-conditioned system. This regularization step should be formalized upfront in the primary methodology rather than described as a post-hoc conditioning audit to avoid giving the impression of an unstable foundational fit.

CENTRAL CLAIM
The central claim—that there is no observable cosmological real-space galaxy chirality dipole at the 0.75% amplitude level—is strongly supported by the evidence presented, particularly the block-bootstrap WLS exclusion and the bias-hardened equivariant pipeline.
