# P2 2026-06-04_R4fixed — Confabulation-hunter referee (reasoning mode)

**Model**: `deepseek/deepseek-r1-0528`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 191.8s

---

## Referee Report for PAPER P2: "Testing the Matter Bounce with Primordial Non-Gaussianity: SPHEREx Forecasts, with a MegaMapper Outlook"  

### ESSENTIAL Revisions  
**P2-E1: Abstract (convention ambiguity)**  
- **Problem**: The abstract states detection significance halves under Li & Brandenberger normalization but does not resolve the ambiguity: "the convention sensitivity should be resolved before SPHEREx data are interpreted." This is critical as it reduces the headline 3–5σ to 1.5–2.5σ.  
- **Fix**: Resolve the convention ambiguity decisively in the main text (as attempted in Appendix A) and state which convention is observationally correct for SPHEREx. If unresolved, present both scenarios equally in forecasts.  

**P2-E2: Section II (version-history artifact)**  
- **Problem**: Body text includes revision notes: "the abstract previously gave only the central ∼ 2.6σ; the upper-bound [...] is reported here for completeness" (Sec. II). This is an internal audit artifact.  
- **Fix**: Remove all version-history language (e.g., "previously gave," "now reported here").  

**P2-E3: Section VI (version-history artifact)**  
- **Problem**: Text references retired content: "The prior conclusion-paragraph figure ‘> 6×105’ was an aggregation error retired in §VI." This is a review-log artifact.  
- **Fix**: Delete all references to retired/updated figures or text from earlier drafts.  

**P2-E4: Section IV (σ(fNL) fiducial dependence)**  
- **Problem**: The forecast uses σ(fNL)≈0.7 (Heinrich et al. 2024) computed at fNL=0, but applied at fNL=−4.375. The paper notes this relies on a "leading-order linearization" and defers re-derivation to a "post-arXiv TODO" (Sec. IV), undermining reproducibility.  
- **Fix**: Recompute the Fisher matrix at fNL=−4.375 or provide a robustness test showing the error is negligible.  

### MAJOR Revisions  
**P2-M1: Abstract and Sec. III B (template overlap provenance)**  
- **Problem**: The template mismatch factor (r=0.84±0.02) is load-bearing for the 3–5σ forecast but lacks a reproducible source: "validated via ℓ-space Fisher overlap, 200 injection-recovery realizations, and a 10,000-sample null-space scan" (Abstract). No code/data is provided.  
- **Fix**: Share scripts for the null-space scan (c1–c6 coefficients), Fisher overlap, and injection-recovery tests in a public repository.  

**P2-M2: Abstract and Sec. VI (Bayes factor provenance)**  
- **Problem**: The Bayes factor (BF∼10–17) is derived from 3×105 Monte Carlo realizations but lacks traceable inputs: "validated across three independent ensembles... with framework-specific priors" (Abstract). No code/ensembles are provided.  
- **Fix**: Release code for Bayesian comparison (including prior definitions and likelihood functions) and ensemble datasets.  

**P2-M3: Abstract and Sec. VI (prior sensitivity)**  
- **Problem**: The BF∼10–17 range spans delta/Gaussian bounce priors and competitor priors, but the abstract emphasizes the maximum (delta prior, BF∼17) while the baseline (Gaussian σ=1.0, BF∼10) is physically recommended.  
- **Fix**: Highlight the baseline BF∼10 prominently in the abstract and clarify that BF∼17 is an optimistic prior-dependent bound.  

**P2-M4: Sec. II (polynomial coefficient ambiguity)**  
- **Problem**: The underdetermined c1–c6 coefficients introduce ∼15% scatter in r (amplitude recovery), but the null-space scan details (e.g., SVD constraints, scan volume) are insufficient to reproduce r=0.85±0.13.  
- **Fix**: Specify scan parameters (e.g., radius=50 justification, monomial basis normalization) and provide coefficient sets.  

### MINOR Revisions  
**P2-m1: Abstract (fNL ratio rounding)**  
- **Problem**: |fNL<sup>bounce</sup>|/|fNL<sup>inf</sup>|≈290 is approximate; exact is 4.375/0.015≈291.67.  
- **Fix**: Note the exact value and rounding in the abstract.  

**P2-m2: Sec. IV (adopted forecast clarity)**  
- **Problem**: σ(fNL)≈0.7 is from Heinrich et al. (2024) but not explicitly flagged as adopted (not recomputed).  
- **Fix**: State clearly: "adopting Heinrich et al. (2024) bispectrum forecast σ(fNL<sup>local</sup>)=0.7."  

**P2-m3: Sec. II (footnote placement)**  
- **Problem**: Footnote 1 interrupts sentence flow: "The coefficients printed in Eq. (37) of [7]—(3, 1, −9, 5, −66, 9)— are..." (mid-sentence).  
- **Fix**: Move the footnote marker to the end of the sentence.  

### NITPICKS  
**P2-N1: Sec. IX D (acronym clarity)**  
- **Problem**: "SDB" (scale-dependent bias) is used without definition in Sec. IX D.  
- **Fix**: Define at first use (Sec. III A).  

**P2-N2: Sec. II (redundant phrasing)**  
- **Problem**: Duplicate phrasing: "underdetermined polynomial coefficients" (Abstract) and "underdetermined c1–c6 benchmark" (Sec. II).  
- **Fix**: Use consistent terminology (e.g., "underdetermined coefficients c1–c6").  

**P2-N3: Appendix A (convention notation)**  
- **Problem**: "c=1" and "c=2" conventions (Appendix A) lack explicit ties to Planck/Komatsu-Spergel.  
- **Fix**: Label conventions as "Planck (c=2)" and "alternative (c=1)" throughout.  

---  
## Summary recommendation  
MAJOR REVISIONS  

**Justification**: The paper provides a timely forecast for SPHEREx/MegaMapper tests of the matter bounce. However, version-history artifacts (E1–E3) and unresolved convention ambiguity (E1) impede clarity. Reproducibility is compromised by missing code/data for key results (template overlap r, Bayes factors; M1–M2). The σ(fNL) forecast relies on an untested fiducial approximation (E4), and prior sensitivity in Bayes factors is underemphasized (M3). Essential/major revisions are required to ensure robustness and reproducibility. The 22-page length is acceptable for a methods paper.