# RCEXT P2 Gemini — chat: https://gemini.google.com/u/0/app/c6cef9faaee510f4
VERDICT: MINOR REVISIONS

Provider: Gemini (Flash/regular)
PDF: RCEXT_P2.pdf (md5: 291b9956a032c5a57e12896a128e7f40)
Harvested: 2026-06-29

---

Recommendation: MINOR REVISIONS

1. Summary

The manuscript presents a comprehensive sensitivity recast of upcoming galaxy survey constraints—primarily from the SPHEREx mission and the proposed Stage-V MegaMapper facility—to test the specific primordial non-Gaussianity (PNG) prediction of the quasi-dust matter bounce scenario (fNL_local = −35/8 = −4.375). The author addresses a persistent factor-of-two normalization discrepancy in the literature between Cai et al. and Li et al., clarifying through symbolic in-in operator algebra that the full commutator doubling yields −35/8 under the standard Planck convention. The work systematically explores the template mismatch between the matter-bounce bispectrum shape and a pure local template, finding a robust noise-weighted amplitude recovery factor of r≈0.84. This mismatch degrades the optimistic SPHEREx multi-tracer bispectrum detection significance from a naive 6.25σ down to a template-corrected range of 5.2–5.5σ, with a realistic envelope of 2.6–5.5σ incorporating systematic budget. Overall, the paper provides a transparent and highly rigorous "recast" methodology. It merits publication in MNRAS after addressing the minor points below.

2. Blockers

None. The paper is well-structured, highly mathematically consistent, and the author has made all accompanying analysis scripts and metadata public via GitHub for replication.

3. Majors

3.1 Clarification on the Additive Quadrature Combined Systematic Bounds: The author establishes a "realistic scoping sensitivity envelope" of 2.6–5.5σ after accounting for the systematic budget. It is noted that these systematics are combined additively in quadrature as a transparent scoping heuristic rather than through a joint multi-tracer marginalized Fisher matrix. The paper lacks a definitive discussion on how a joint bispectrum Fisher matrix over these nuisances could shift the 2.6σ conservative floor. The author should add a brief qualitative discussion or caveat regarding the potential structure of the missing joint bispectrum cross-covariance matrix elements.

4. Minors

4.1 Parameterization Shift in the Overlap Scan: In Section III.B, the author notes an index-labeling choice where k1 is held fixed as the hard reference scale and k3 is treated as the long (squeezed) mode. This explicitly interchanges the index roles relative to the benchmark configuration layout in Section II. Although BNL is permutation-symmetric, adding a small clarifying footnote or explicit parenthetical reminder inside the caption of Figure 1 or Table I would improve legibility.

4.2 Uniform Logarithmic Grid Sampling: The manuscript notes that the uniform logarithmic grid over 23,098 triangle configurations undersamples the extreme squeezed limit where the matter-bounce signal is strongest. The author should explicitly state whether an equivalent squeezed-enhanced sampling density was verified for the LSS noise-weighted schemes to confirm that the LSS overlap remains robustly bounded within the quoted ±0.02 spread.

4.3 Typographical and Math Token Extraction Issues: On page 1, source [7], "at ng 0.9649" appears to be a misprint for "ns=0.9649". "fNI" is typed instead of "fNL" in one location. In Section VII.C, the acronym "OGR" is introduced without prior definition.

5. Strengths

Resolution of the Cai-Li Discrepancy: The explicit source-to-source normalization audit and symbolic execution of the −2Im commutator identity in Appendix A clears up a long-standing factor-of-two ambiguity in the bouncing cosmology literature.

Rigorous Null-Space Robustness Check: The author comprehensively samples 10,000 valid coefficient sets within a 3D null space, validating that the shape cosine remains r_cos > 0.97 across variations over an order of magnitude in scan volume, providing exceptional theoretical robustness.

Balanced and Candid Framing: The paper is exceptionally grounded, explicitly highlights that MegaMapper is currently unapproved and unfunded, and openly frames its own analysis as a sensitive recast dependent on an external baseline forecast.
