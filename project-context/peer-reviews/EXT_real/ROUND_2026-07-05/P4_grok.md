# EXT Review — P4 × Grok
- paper: P4
- version: v1.0.212
- reviewer: Grok
- model: Expert
- timestamp: 2026-07-06T19:16:37Z
- chat_url: https://grok.com/c/74e596b0-fb9c-497b-92b8-5c3c7ed7b995
- pdf: /tmp/round_P4.pdf

## Raw verbatim response

Thought for 48s

VERDICT: MINOR REVISIONS

ISSUES:

[MAJOR] Sec. IV D and Appendix D (eight-anchor battery and forward model): The imaging + per-galaxy DR8 morphology (b/a, fracdev, shape r) templates explain only ≈53% of the post-MASTER canonical ℓ=1 residual amplitude (predicted |a₁| = 3.75×10⁻³ vs. observed 6.95×10⁻³, cos θ ≈ +0.83). The remaining ≳47% is explicitly left open (possible classifier confidence-vs-depth map or higher-order structure) without a dedicated test injecting the residual map into the real-space dipole estimator or regressing Aₚ against mean p_eq per pixel. This leaves an incomplete systematics budget for the harmonic channel, even though the primary claim does not rest on it.
[MINOR] Sec. II B (Training Labels) and III B (Declared Analysis Hierarchy): 66.5% of training labels come from CE-ResNet pseudo-labels. The GZ1-only submodel cross-check yields a clean null (z = −0.04σ), but on a much smaller HC sample (N ≈ 1.5×10⁴). The main-text bound on maximum inherited coherent dipole power consistent with both the template-regression anchors and the reduced-N GZ1-only result should be stated quantitatively rather than qualitatively.
[MINOR] Sec. IV C (Dipole Analysis, confidence-cut rationale): The p_eq > 0.6 HC selection is described as pre-specified in the generator script and shown to be stable, but no commit hash, script excerpt, or supplementary file is referenced to allow independent verification of the pre-registration. This is a minor but necessary transparency fix for a cut that defines the primary sample.
[MINOR] Abstract, Sec. I, and Sec. IV (significance reporting): Multiple σ/z values from incommensurable null procedures (+0.41σ moment-z vs. +3.64σ / +7.28σ / z ≈ −18 block-bootstrap) are presented with disclaimers, yet the density still creates high risk of misreading harmonic-channel numbers as independent detections. A single consolidated “Primary Results” callout box or table that isolates the two load-bearing claims (real-space HC dipole and template-fit exclusion) would improve clarity.
[MINOR] Sec. V A (Comparison with Shamir): The amplitude-level tension (factor ∼4–9) is correctly caveated as non-frequentist. Adding one sentence that cross-references the real-space injection-recovery floor (A₅₀ ≈ 0.75%) to the expected significance for an injected Shamir-scale signal under the present estimator would make the comparison fully self-contained.

Central claim assessment: The central claim that the high-confidence (p_eq > 0.6) real-space chirality dipole on 949,584 spirals is consistent with null (+0.41σ, rank-p = 0.31) and that a clean 1.7% cosmological dipole is strongly disfavored (z ≈ −18) by the block-bootstrap WLS template fit on the canonical mask is supported by the evidence from the primary estimators, the full suite of robustness checks, and the empirical injection-recovery calibration.
