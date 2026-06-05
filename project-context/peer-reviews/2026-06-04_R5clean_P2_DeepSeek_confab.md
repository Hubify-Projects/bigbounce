# P2 2026-06-04_R5clean — Confabulation-hunter referee (reasoning mode)

**Model**: `deepseek/deepseek-r1-0528`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 222.6s

---

## Referee Report: Confabulation-Hunter Findings

### ESSENTIAL Findings

- **P2-E1: Abstract, page 1**  
  **Problem**: The claim "σ(f_NL^local) ≈ 0.7" (Heinrich et al. 2024) is used to derive the headline 5.2–5.5σ significance, but the paper does not provide traceable access to the underlying Fisher matrix or scripts reproducing this σ value. The forecast relies on recasting Heinrich et al.'s result without independent validation or accessible code.  
  **Fix**: Provide a publicly accessible script or dataset that reproduces the σ(f_NL^local) = 0.7 forecast using SPHEREx specifications (e.g., via GitHub repository). If reuse is intentional, explicitly state that no new Fisher calculation was performed and cite Heinrich et al.'s code if available.

- **P2-E2: Section II, "Null-space scan"**  
  **Problem**: The 10,000-sample null-space scan for polynomial coefficients (c₁–c₆) reports r = 0.85 ± 0.13 and r_cos > 0.97 but does not link to the script generating these numbers. The scan parameters (e.g., SVD tolerance, ball radius 50) are described, but the code is not provided for verification.  
  **Fix**: Release the scan script (e.g., Python/MATLAB) in the companion repository with explicit documentation of normalization and convergence tests for the uniform sampling.

- **P2-E3: Section III.B, Eq. 6**  
  **Problem**: The amplitude recovery factor r = 0.84 ± 0.02 (noise-weighted) is critical for the 5.2–5.5σ significance but lacks provenance. The validation methods (ℓ-space Fisher, injection-recovery, literature search) are described, but no script or dataset reproduces the r-value arithmetic.  
  **Fix**: Provide code to compute r under all weighting schemes (CMB Fisher, LSS, SPHEREx-like) and confirm the range r ∈ [0.829, 0.876] from first principles.

- **P2-E4: Section VI, Bayesian comparison**  
  **Problem**: The Bayes factors (BF ∼ 10–17) derive from 3×10⁵ Monte Carlo realizations, but no code or data for the ensembles is provided. The analytic formula (Eq. 7) is given, but its implementation (e.g., prior sampling, marginalization over σ_GR) is not traceable.  
  **Fix**: Release scripts for the Monte Carlo ensembles and BF calculation, including input distributions for σ(f_NL), b_ϕ, and GR systematics.

---

### MAJOR Findings

- **P2-M1: Abstract, "template-corrected significance ∼3–5σ"**  
  **Problem**: The systematic budget (noise-weighted shape mismatch, ϵ-correction, polynomial scatter, etc.) degrades 5.2–5.5σ to 3–5σ, but the step-by-step arithmetic (e.g., how each systematic contributes to σ-inflation) is not reproducible from displayed values alone.  
  **Fix**: Tabulate individual systematic contributions to σ(f_NL) (e.g., GR degradation factor, b_ϕ marginalization impact) so the 3–5σ envelope is traceable.

- **P2-M2: Section II.C, ϵ-correction uncertainty**  
  **Problem**: The ϵ-correction uncertainty (1–8%) for f_NL is stated, but no script or data quantifies its propagation to the detection significance. The range f_NL ∈ [−4.35, −4.02] is not derived from a visible computation.  
  **Fix**: Provide code calculating f_NL shifts from w = −0.003 and explicit cubic-action integrals with mode functions.

- **P2-M3: Section IV, SPHEREx bispectrum forecast**  
  **Problem**: The degradation to σ(f_NL) from b_ϕ marginalization (O(20–50%)) is estimated but not reproduced from a Fisher matrix. The claim "σ(f_NL) widens by O(20–50%)" lacks numerical backing.  
  **Fix**: Show the Fisher matrix with/without b_ϕ universality and release the code for marginalization.

- **P2-M4: Section V, MegaMapper forecast**  
  **Problem**: The 3–7σ range for MegaMapper is speculative and cites no reproducible forecast. The "conservative σ(f_NL) = 1.5" (Fig. 4) is asserted without derivation.  
  **Fix**: Provide a toy Fisher code or sensitivity scaling tool to justify the 3–7σ envelope under varying systematics.

---

### MINOR Findings

- **P2-N1: Section II, Table I**  
  **Problem**: The B_NL values at benchmark configurations (squeezed, equilateral, folded) match Cai et al. but are not independently computed in the provided code. The repository lacks a script for B_NL evaluation.  
  **Fix**: Add a script to compute B_NL for arbitrary (k₁, k₂, k₃) using the polynomial basis.

- **P2-N2: Section III.B, injection-recovery test**  
  **Problem**: The injection-recovery test (r_meas = 0.90 ± 0.01) uses simulated noise but does not specify the random seed or noise covariance parameters.  
  **Fix**: Document noise parameters and seed in the repository for reproducibility.

- **P2-N3: Section VII, GR degradation**  
  **Problem**: The GR-induced bias σ_GR ∈ [0, 1.0] is parameterized, but no script generates the degradation curves in Fig. 4.  
  **Fix**: Release code for σ(f_NL) vs. k_min and GR marginalization.

- **P2-N4: Appendix A, convention factor**  
  **Problem**: The factor-of-two convention discrepancy (Cai vs. Li & Brandenberger) is resolved analytically, but the symbolic-algebra notebook ("appendix A1 wick doubling.py") is not included in the provided repository.  
  **Fix**: Ensure the notebook is present and runnable.

---

### NIT Findings

- **P2-T1: Abstract, "r ∈ [0.829, 0.876]"**  
  **Problem**: The values 0.829 and 0.876 appear without units or explicit reference to a dataset (though context implies they are unitless overlaps).  
  **Fix**: Clarify "shape overlap r" in the abstract.

- **P2-T2: Section II, "radius 50"**  
  **Problem**: The null-space scan uses a ball radius of 50 (Euclidean norm), but the text does not specify if this is dimensionless or physical.  
  **Fix**: Note that coefficients are dimensionless and radius is in coefficient space.

---

## Summary Recommendation  
**MAJOR REVISIONS**  

The paper presents a compelling forecast for SPHEREx and MegaMapper constraints on bounce cosmology. However, **key numerical results lack traceable provenance**: (1) The σ(f_NL) = 0.7 from Heinrich et al. is not independently validated or accessible. (2) Core metrics (r = 0.84 ± 0.02, BF ∼ 10–17) derive from unreleased scripts for null-space scans, Fisher overlaps, and Bayesian ensembles. (3) Systematic budgets (e.g., GR degradation, b_ϕ marginalization) are described but not reproducible. Addressing these is essential for a methods paper. Revise by releasing all code/data for claimed numbers and clarifying arithmetic dependencies. The page count (22pp) is appropriate, and no version-history artifacts or duplicate phrases were found.