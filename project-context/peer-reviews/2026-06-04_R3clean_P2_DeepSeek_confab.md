# P2 2026-06-04_R3clean — Confabulation-hunter referee (reasoning mode)

**Model**: `deepseek/deepseek-r1-0528`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 209.5s

---

## Referee Report for P2: "Testing the Matter Bounce with Primordial Non-Gaussianity: SPHEREx Forecasts, with a MegaMapper Outlook"  

### ESSENTIAL REVISIONS  
**P2-E1: Abstract (p. 1) & Sec. VII (p. 13)**: **Untraced systematic budget degrading σ(f_NL)**  
- **Problem**: The headline 3–5σ detection claim (abstract: "template-corrected significance ∼ 3–5σ after the combined systematic budget") lacks quantitative provenance. The budget components (noise-weighted shape mismatch, ϵ-correction, null-space scatter, photo-z degradation, PNG bias, b_ϕ marginalization, GR projection) are listed but lack:  
  (i) Individual contributions to σ(f_NL) degradation (e.g., how much each factor widens σ),  
  (ii) Aggregation method (e.g., root-sum-square or Monte Carlo),  
  (iii) Script/JSON input for systematic parameters (e.g., σ_GR ∈ [0, 1.0], b_ϕ prior width).  
- **Fix**: Provide a table or equation quantifying each systematic's contribution to σ(f_NL) and release the systematic parameter inputs (e.g., via GitHub JSON). Specify the error-propagation formalism.  

**P2-E2: Abstract (p. 1) & Sec. II (p. 4)**: **Unreproducible null-space scatter in r**  
- **Problem**: The ±0.13 scatter in amplitude recovery factor r (abstract: "polynomial-coefficient null-space amplitude scatter ±0.13 absolute in r") is claimed from a "10,000-sample null-space scan" but lacks:  
  (i) Script/code to reproduce the scan,  
  (ii) Input basis for monomial coefficients c₁–c₆,  
  (iii) Fisher-weighting scheme details for r.  
- **Fix**: Release the null-space scan code and coefficient basis; document Fisher-weighting in a reproducible script (e.g., Python/JSON).  

**P2-E3: Sec. VI (p. 10)**: **Version-history artifact**  
- **Problem**: Prose references outdated drafts: "a rhetorical '>6×10^5' figure appeared in an older draft conclusion paragraph; the canonical realization count is 3×10^5". This is internal revision debris.  
- **Fix**: Remove all version-history language.  

### MAJOR REVISIONS  
**P2-M1: Abstract (p. 1) & Sec. III B (p. 6)**: **Inconsistent template-mismatch quantification**  
- **Problem**: The abstract cites "r ∈ [0.829, 0.876]" for template recovery, but Sec. III B states "r = 0.84 ± 0.02" (i.e., [0.82, 0.86]), creating ambiguity. The provenance of the range endpoints (0.829, 0.876) is unclear.  
- **Fix**: Reconcile values; clarify if 0.829–0.876 is the min–max across weighting schemes or a confidence interval. Release the weighting-scheme inputs (e.g., k-cutoffs, noise models).  

**P2-M2: Sec. IV (p. 7) & Sec. VII (p. 12)**: **Unvalidated σ(f_NL) degradation from b_ϕ**  
- **Problem**: The 20–50% degradation in σ(f_NL) due to b_ϕ marginalization (Sec. VII) lacks:  
  (i) Fisher matrix calculations showing how σ(f_NL) widens with b_ϕ prior width,  
  (ii) Connection to Heinrich et al. [4] bispectrum forecast (which assumes fixed b_ϕ).  
- **Fix**: Show the b_ϕ-marginalized Fisher matrix; provide code to reproduce Fig. 5 (σ(f_NL) vs. b_ϕ prior).  

**P2-M3: Sec. IX D (p. 16)**: **Unsupported 6× sharper σ(f_NL) claim**  
- **Problem**: The joint (f_NL, n_fNL) Fisher analysis claims σ_unmarg(f_NL) ≈ 0.114 (6.1× sharper than σ = 0.7), but:  
  (i) No Fisher matrix or binning details are provided,  
  (ii) The companion artifact with Fisher inputs is "deferred", making it untraceable.  
- **Fix**: Include the 6-bin Fisher matrix or release the companion artifact concurrently.  

### MINOR REVISIONS  
**P2-m1: Abstract (p. 1)**: **Ambiguous Bayes factor prior dependence**  
- **Problem**: The BF ≈ 10–17 range is not clearly mapped to prior choices in the abstract. Readers must extract this from Sec. VI/Table II.  
- **Fix**: Specify in the abstract: "BF ∼ 10 (recommended σ_theory=1.0 Gaussian bounce prior vs. broad multifield [−15,15]) up to BF ∼ 17 (delta bounce prior vs. same competitor)".  

**P2-m2: Sec. II (p. 3)**: **Underdetermined polynomial basis not justified**  
- **Problem**: The choice of 6 monomials for the degree-9 polynomial P(k₁,k₂,k₃) is attributed to "Cai-physics-restricted subset" but lacks a mathematical proof (e.g., symmetry constraints).  
- **Fix**: Cite Cai et al. [7] Eq. 37 explicitly or show the orbit-space reduction.  

**P2-m3: Sec. VIII A (p. 15)**: **Unreproduced Planck recast**  
- **Problem**: The recast Planck constraint f_NL^bounce = −0.1 ± 5.7 uses a CMB Fisher r=0.876 but lacks code for the Fisher overlap calculation.  
- **Fix**: Release the ℓ-space Fisher script used for r.  

### NITPICKS  
**P2-N1: Sec. II C (p. 5)**: **Typo ("in- visible")**  
- **Fix**: Correct "in- visible" to "invisible".  

**P2-N2: Sec. VI (p. 10)**: **Redundant phrase ("aggregate (a rhetorical...")**  
- **Fix**: Remove parenthetical: "(a rhetorical '>6×10^5' figure appeared...").  

**P2-N3: Sec. III A (p. 6)**: **Duplicate "P" in equation numbering**  
- **Fix**: Remove extra "P" in "Eqs. (3)–(4)".  

---  
## Summary recommendation  
**MAJOR REVISIONS**  

Justification: The paper presents a timely forecast for SPHEREx to test the matter-bounce f_NL = −35/8. The core methodology (template mismatch, Bayesian comparison) is innovative, and the GitHub commitment enhances reproducibility. However, the headline 3–5σ significance lacks a traceable systematic budget (P2-E1), and key numerical claims (null-space scatter, b_ϕ degradation) are unsupported by released scripts/data (P2-E2, P2-M2). The version-history artifact (P2-E3) further undermines professionalism. Addressing these is essential for acceptance. The page count (22pp) is appropriate given the scope.