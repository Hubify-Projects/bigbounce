# P4 R9 — Confabulation-hunter referee (reasoning mode)

**Model**: `deepseek/deepseek-r1-0528`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 67.7s

---

## Referee Report: P4-R9

### ESSENTIAL REVISIONS

**P4-E1: Inadequate Monte Carlo Simulations**  
- **Section**: Table I, Section IV C, Section IV D  
- **Problem**: Key results (e.g., MASTER deconv −0.122σ, canonical MASTER +3.64σ, monopole+mask null) rely on only N=500 Monte Carlo realizations. This is insufficient for robust significance estimates (σ values), as acknowledged in the metadata ("N_MC=500 (should be ≥10000)"). The low N inflates uncertainty in σ and p-values (e.g., pMC=0.030 for +3.64σ has high error).  
- **Fix**: Increase MC realizations to ≥10,000 for all null procedures (label-shuffle, per-pixel-shuffle, binomial monopole). Recompute σ values and p-values. Explicitly state N_MC in all captions/text (e.g., Table I).  

**P4-E2: Undocumented Weighting Scheme**  
- **Section**: Table I (Nmap weighted), Section IV C  
- **Problem**: Nmap weighted (5,547,858) exceeds Ncatalog spiral (3,201,160) but lacks documentation. The paper states Nmap is "pixel-weighted galaxy count" without defining weights or methodology. This undermines reproducibility of the MASTER deconvolution (−0.122σ result).  
- **Fix**: Detail the weighting scheme (e.g., per-pixel galaxy density, completeness factor) in Section III or Appendix A. Provide a script/equation showing how Nmap is derived from raw catalog data.  

**P4-E3: Cosmic Variance Ignored in Nulls**  
- **Section**: Throughout (e.g., Table I null descriptions)  
- **Problem**: Permutation nulls (label-shuffle, per-pixel-shuffle) assume no spatial correlations, ignoring cosmic variance. This invalidates variance estimates (σ) for large-scale structure observables. Metadata explicitly flags this ("permutation null ignores cosmic variance").  
- **Fix**: Replace permutation nulls with physics-based mocks (e.g., lognormal simulations) incorporating cosmic variance. Recompute σ values for all estimators (i)–(vi). Discuss limitations in text.  

### MAJOR REVISIONS

**P4-M1: Low Injection-Recovery MC for Sensitivity Floor**  
- **Section**: Section VI A, Table I (estimator vi)  
- **Problem**: The 50%-recovery-at-3σ threshold (A=0.75%) uses only N_MC_inj=100 per amplitude and N_MC_null=1000. This is too low for reliable empirical sensitivity estimates.  
- **Fix**: Increase to N_MC_inj≥500 per amplitude and N_MC_null≥5000. Recompute the threshold and uncertainty.  

**P4-M2: Ambiguous Abstract Claim**  
- **Section**: Abstract  
- **Problem**: The abstract states the canonical-mask residual (+3.64σ) is "consistent with monopole leakage" but omits that it is attributed to systematics (Sec IV E, VI). This misrepresents the residual as fully explained by leakage, while the text notes a depth-correlated systematic.  
- **Fix**: Revise to: "The +3.64σ canonical-mask residual is attributed to systematics (depth/sampling-correlated) after disfavoring cosmological interpretations."  

**P4-M3: Version-History Artifact**  
- **Section**: Section IV D (first paragraph)  
- **Problem**: In-text reference to "earlier paper versions" ("were interpreted in earlier paper versions as mask-geometric leakage") is a version-history artifact inappropriate for publication.  
- **Fix**: Remove "earlier paper versions" and state: "Initial interpretation as mask-geometric leakage was disfavored by..."  

### MINOR REVISIONS

**P4-m1: Inconsistent σ Decimal Precision**  
- **Section**: Abstract, Section IV C, Table I  
- **Problem**: σ values inconsistently reported: −0.122σ (3 decimals) vs. +0.43σ (2 decimals). The metadata notes harmonization to −0.122σ, but +0.43σ remains under-specified.  
- **Fix**: Report all σ values with 3 decimals (e.g., +0.430σ) for consistency.  

**P4-m2: Unclear "Empirical Rank pMC"**  
- **Section**: Section IV D (canonical-mask residual)  
- **Problem**: "empirical rank pMC = 0.030" is undefined (no reference to methodology or equation).  
- **Fix**: Define pMC as the fraction of null realizations exceeding the observed value (e.g., "pMC = k/N, where k=15/500").  

**P4-m3: Duplicate Phrase**  
- **Section**: Title  
- **Problem**: Duplicate "canonical-mask" in "Canonical-Mask Residual on ... Canonical-Mask Residual".  
- **Fix**: Revise title to: "... and Diagnostic Evidence for a Depth/Morphology-Correlated Residual on 8.47 Million DESI Legacy Galaxies".  

### NITPICKS

**P4-N1: Typo in Appendix D**  
- **Section**: Appendix D (first paragraph)  
- **Problem**: "demonopole-subtracted" should be "monopole-subtracted".  
- **Fix**: Correct spelling.  

**P4-N2: Inconsistent Units in Table IV**  
- **Section**: Table IV  
- **Problem**: Pseudo-Cℓ values lack units (e.g., 1.696×10−2 vs. 1.685×10−2).  
- **Fix**: Add units (e.g., ×10−2 [sr]) for clarity.  

---

## Summary Recommendation  
**MAJOR REVISIONS**  

The paper presents a rigorous analysis of galaxy chirality with a substantial dataset (8.47M galaxies) and valuable public release. However, it cannot be accepted in its current state due to essential methodological flaws: (1) Inadequate Monte Carlo simulations (N=500) undermine all σ values; (2) Undocumented weighting for Nmap prevents reproducibility of key results; (3) Permutation nulls ignore cosmic variance, invalidating variance estimates. These issues are critical for a methods paper. Additionally, the abstract misrepresents the canonical-mask residual, and version-history artifacts appear in the text. Addressing these (including ≥10,000 MC realizations, cosmic-variance-aware nulls, and clear weighting documentation) is mandatory. Minor issues (precision, phrasing) should also be corrected.