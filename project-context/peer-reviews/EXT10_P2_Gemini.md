# EXT10 Harvest — P2 — Gemini
- Provider: Gemini
- Model/Effort: 3.5 Thinking (Solves complex problems)
- Chat URL: https://gemini.google.com/u/0/app/44f57cfa1ebd1ad7
- PDF md5: 406af9f8
- Harvested: 2026-06-13 15:16 PDT

---

## Referee Report

**Journal:** MNRAS / Physical Review D / JCAP
**Manuscript Title:** Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook
**Author:** Houston Golden

---

**1. Recommendation: MINOR REVISIONS**

The manuscript provides an exceptionally thorough, timely, and computationally validated sensitivity recast testing the matter bounce paradigm against upcoming large-scale structure (LSS) datasets. By auditing legacy bispectrum calculations and rigorously computing template mismatches under realistic noise-weighting schemes, the paper bridges first-principles early-universe theory with concrete on-sky observables. The manuscript is highly well-structured and stands out for its exemplary dedication to open science via archived reproducibility pipelines. It requires only minor, targeted text adjustments and clarifications before publication.

---

**2. Strengths**

- **Rigorous Template Mismatch Validation:** Rather than relying on simple shape-similarity heuristics, the author cross-validates the local-to-bounce template overlap across three distinct layers: an ℓ-space Fisher validation, 200 explicit Monte Carlo injection-recovery realizations using an optimal KSW-type linear estimator, and an exhaustive 10,000-sample null-space scan of underdetermined polynomial coefficients.

- **Definitive Normalization Audit:** The paper masterfully resolves a long-standing factor-of-two discrepancy in the literature between Cai et al. (fNL=−35/8) and Li et al. (fNL=−35/16). By applying the standard in-in commutator identity symbolically, the author elegantly proves that the smaller value is merely an incomplete single-time-ordering intermediate, stabilizing the physical baseline prediction.

- **Transparent and Conservative Systematic Budgeting:** Systematics such as relativistic projection effects, photometric redshift smear, and primordial non-Gaussianity (PNG) galaxy bias (bϕ) uncertainties are explicitly modeled and stacked in quadrature. This avoids overly optimistic headlines and provides a highly realistic forecast envelope.

- **Exemplary Open Science Practices:** The full integration of analysis code, Monte Carlo evaluation scripts, and structural JSON artifacts in a public repository ensures the work is fully reproducible and verifiable by the community.

---

**3. Specific Scrutiny**

**A. The fNL=−35/8=−4.375 Prediction**
The prediction is strictly conditional on a narrow, restricted bounce class—specifically the Wilson-Ewing class, which assumes no prolonged post-bounce inflation, negligible fermion-sourced torsion during contraction, and faithful third-order bispectrum transmission through the bounce boundary. The text is highly commended for its candor in detailing these structural dependencies.

**B. SPHEREx Fisher Forecast & Effective Uncertainty Boundaries**
The value 0.36 does not represent the baseline Fisher uncertainty σ(fNL); rather, it is the systematic shift in the absolute value of the predicted fNL induced by the conservative endpoint of the ϵ-correction (κϵ|Δϵ|≈80×0.0045≈0.36). The underlying Fisher baseline inherited from the galaxy bispectrum channel is actually σ(fNL)=0.7. When accounting for cumulative systematics stacked in quadrature, the effective uncertainty inflates to an effective σeff range of 1.35 to 1.41. This accurately and robustly sustains the realistic final headline detection significance of 2.6–5σ.

**C. Externalized Survey Anchor (Heinrich et al.)**
The paper externalizes its baseline multi-tracer bispectrum sensitivity from Heinrich et al. (σ(fNL)≈0.7 for bispectrum only, and ≈0.5 when combined with the power spectrum). The formal peer-reviewed publication date is 2024 (Phys. Rev. D 109, 123511). The manuscript correctly navigates this timeline in its bibliography and prose.

**D. Continuous-GR-Recovery Marginalization (c9k)**
The automated continuous marginal-likelihood integration over a uniform GR contamination prior (σGR∼U[0,1]) yields a stable Bayes Factor of BF=6.0 against the narrow tuned competitor. The calibration check beautifully demonstrates that the discrete stress-test scenario of σGR=0.5 successfully captures a 23% inflation of the effective survey uncertainty (σeff/0.7=0.86/0.7≈1.23).

---

**4. Blockers (Must Fix)**

**Section IX.D / Summary Table Clarity:** In Section IX.D, the paper introduces a subordinate, separate joint Fisher analysis mapping the scale-dependent bias (SDB) channel over six redshift bins to constrain the running index nfNL. This auxiliary analysis yields a significantly weaker, highly degenerate measurement significance for fNL (0.6σ to 1.4σ). To prevent readers from confusing these subordinate results with the primary headline bispectrum recast (2.6–5σ), the author must insert a clarifying sentence or explicit sub-labeling in the text ensuring that the distinct statistical estimators and separate data dimensions are clearly demarcated.

---

**5. Majors (Should Fix)**

**Section VII.B (bϕ Prior Justification):** The systematic budget assumes a baseline 20% Gaussian prior on the linear PNG galaxy bias parameter. The author should add 2–3 sentences explicitly expanding on the physical or simulation-driven justifications for assuming a 20% baseline constraint under upcoming survey conditions.

---

**6. Minors (Polish)**

- **Prose Reference Synchronization:** In Section VI.C (line 363-364), the text refers to the "Heinrich et al. 2024 forecast", but switches to "Heinrich+2023" in other descriptive shorthand summaries. Ensure the text uniformly aligns its shorthand prose references with the official 2024 PRD publication date.

- **Table IV Label alignment:** In Table IV, the row tracking the cumulative stacking of the 30% bϕ widening scenario is truncated or contains a minor formatting artifact in its descriptive "Acts on" text segment. Ensure the string alignments cleanly render without visual clipping.
