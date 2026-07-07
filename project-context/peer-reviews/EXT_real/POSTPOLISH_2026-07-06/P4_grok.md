# EXT POSTPOLISH 2026-07-06 — P4 — Grok

- **Provider:** Grok, BigBounce - Papers project
- **Model/effort:** Expert
- **Chat URL:** https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=78799fa9-cd87-4a5a-8413-79d63752bccc
- **PDF:** P4_v1.0.219.pdf (md5 54118d50f6768507e4e22ec5611cf33b)
- **Harvested:** 2026-07-07
- **Thought for:** 49s
- **Parsed verdict (from response):** MINOR REVISIONS

## Raw verbatim response

VERDICT: MINOR REVISIONS
ISSUES:

[MINOR] Abstract and Sec. I (Introduction): The harmonic-channel residuals (+3.64σ canonical-mask, +7.28σ apodized) are reported with numerical prominence before the explicit statement that they are "systematics diagnostic, not an independent cosmological null." This risks misreading by readers scanning for detections. Move the numerical harmonic values out of the abstract and first two paragraphs of the introduction; retain only the two primary results (real-space +0.41σ and template-fit z≈−18) in the opening summary, with a cross-reference to the declared hierarchy in Table I.

[MINOR] Sec. IV D (Monopole+Mask Leakage) and Appendix D (eight-anchor battery): The imaging+DR8-morphology forward model accounts for only ~52–54% of the observed |a₁| = 6.95×10⁻³ residual amplitude (cos θ ≈ +0.83 alignment). While the real-space bound (residual maps to A_p ≈ 0.695% < A₅₀ = 0.75%) and anchors (ℓ=2 > ℓ=1, quartile washout, depth anti-alignment r_ℓ=2 = −0.65) are presented, the text does not explicitly propagate the unmodeled ~47% fraction through the WLS covariance or an injection test on the residual map itself to derive a quantitative upper limit on any cosmological dipole component still allowed by all anchors simultaneously. Add this one-paragraph closure.

[MINOR] Sec. VI A (Pseudo-label independence): The GZ1-human-label-only dipole test (z = −0.54σ, N_HC^spiral ≈ 46 017) is correctly identified as decisive because it removes the learned model entirely. However, its statistical power is ~4.5× weaker than the headline HC sample; the text should report the injection-recovery A₅₀/A₉₅ that this specific test would have achieved on the same estimator, to make transparent that it corroborates but does not independently tighten the main bound.

[MINOR] Sec. II B and Data Availability: 66.5% of training labels are CE-ResNet pseudo-labels. While the human-label cross-check and template-regression anchors address inheritance, the final Data Availability statement (referenced on p. 29 but truncated in the provided manuscript) must contain an explicit, immutable release plan: catalog C (Parquet), model weights, exact training manifest, and all pipeline scripts (including the 94113e5 commit that freezes the p_eq > 0.6 cut) with a DOI or tagged GitHub/Zenodo release. This is required for a PRD null-result claim that relies on a partially pseudo-labeled classifier.

[MINOR] Table I and Sec. III B (Declared Analysis Hierarchy): The table is already the single load-bearing map, but its caption does not restate that only the two rows marked PRIMARY carry cosmological weight and that every σ value in diagnostic rows is computed against a distinct null chosen for systematics characterization, not detection. Add one sentence to the caption to eliminate any possibility that a reader treats the harmonic numbers as competing measurements.

The central claim—that the real-space chirality dipole on the pre-specified high-confidence subsample is consistent with null at sub-percent sensitivity and that a clean 1.7% cosmological dipole is strongly disfavored—is supported by the primary estimator (+0.41σ, p=0.31), the block-bootstrap WLS template fit (z≈−18), the injection-recovery calibration, and the explicit bounding of any cosmological content in the harmonic residual.
