# RBEXT P2 Gemini — chat: https://gemini.google.com/u/0/app/fe85f1b423e072d6
VERDICT: MINOR REVISIONS

Provider: Gemini (Flash regular tier)
PDF: RBEXT_P2.pdf | md5: 291b9956a032c5a57e12896a128e7f40
Harvested: 2026-06-29

---

Recommendation: MINOR REVISIONS

Reviewer Report

Summary: This manuscript provides a timely and detailed sensitivity recast of SPHEREx and the proposed MegaMapper facility to test the primordial non-Gaussianity signature of the quasi-dust matter bounce scenario. The paper resolves a notable factor-of-two discrepancy in historical literature between Cai et al. and Li et al., quantifies the template mismatch (r ≈ 0.84), and demonstrates that SPHEREx can test the benchmark fNL = −35/8 at a realistic 2.6σ–5.5σ significance level.

Key Merits

- Clarification of Literature Discrepancies: The rigorous demonstration that the fNL = −35/16 vs. −35/8 discrepancy stems from an incomplete single-time-ordering intermediate step.
- Methodological Rigor on Mismatch: Multi-pronged exploration of template overlap r (uniform polynomial sampling, Fisher grid evaluations, 200 flat-sky injection-recovery realizations), shape cosine r_cos > 0.97.
- Transparent Systematics Bookkeeping: Meticulously separates idealized/optimistic forecast bounds from realistic scoping envelopes.

Comments and Points for Clarification

1. Additive-Quadrature Systematic Heuristic vs. Joint-Covariance
The 2.6σ–5.5σ window is a scoping sensitivity envelope via additive-quadrature heuristic, not a self-consistent joint multi-tracer marginalized Fisher matrix. The paper would benefit from a brief paragraph discussing the expected direction or signs of cross-bin covariance terms within the multi-tracer bispectrum workspace.

2. Mass-Function Universality and bϕ Marginalization
The text highlights potential 20%–50% widening of σ(fNL) if UMF relation is abandoned in favor of independent bϕ marginalization per tracer bin. Expand on whether upcoming autoencoder-selected anomaly sub-samples can break the bϕ–fNL degeneracy without hard UMF priors.

3. Framing of MegaMapper Sensitivities
State whether relativistic projection effects (which bias fNL by up to ∼200σ at z>2 per Addis et al. 2025) are expected to act symmetrically on the exclusion arithmetic if MegaMapper observes a null result.

Technical and Typographical Corrections

- Page 1, Column 1: "...value fNLinf ≈ 0.015 at ng 0.9649..." — "ng" appears to be a typo for "ns".
- Page 7, Column 2: Ensure variables are uniformly typeset in standard LaTeX italic formats.
- Page 22, Figure 6 Caption: "Opservational Decision Thresholds" should read "Observational Decision Thresholds".
