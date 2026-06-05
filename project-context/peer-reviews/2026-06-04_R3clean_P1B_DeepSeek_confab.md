# P1B 2026-06-04_R3clean — Confabulation-hunter referee (reasoning mode)

**Model**: `deepseek/deepseek-r1-0528`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 42.8s

---

## Referee Report for Paper P1B

### ESSENTIAL Findings  
**P1B-E1: Internal artifact in body prose**  
- **Section**: Table I footnote (page 3)  
- **Problem**: The phrase *"Not the stale mid-burn-in diagnostic convergence gpu 20260305 stale.csv (R̂ − 1 ∈ [0.23, 0.86]), preserved as a transparency artifact only"* is a version-control artifact. Such internal bookkeeping language has no place in a published manuscript.  
- **Fix**: Remove all references to stale diagnostics, version-control filenames, or transparency artifacts. Retain only final convergence metrics.  

**P1B-E2: Untraced headline figure in conclusions**  
- **Section**: Conclusions (page 8)  
- **Problem**: The claim *"LiteBIRD is projected to achieve σ(β) ≈ 0.03°"* lacks provenance. No citation, script, or dataset supports this critical projection used to justify future significance (9σ).  
- **Fix**: Provide a traceable source (e.g., LiteBIRD collaboration paper, instrument white paper, or simulation code) for the σ(β) projection.  

---

### MAJOR Findings  
**P1B-M1: Incomplete reproducibility for MCMC results**  
- **Section**: III (page 2–3), V.B (page 6), Appendix A  
- **Problem**: The ∆Neff and H0 values (e.g., −0.020 ± 0.169, 67.68 ± 1.06) are load-bearing but lack immediate reproducibility. The GitHub repo requires users to run 4–12 hour computations to regenerate chains, with no pre-computed chains or likelihood values provided. The paper defers Bayes factors (ln B) to a nonexistent nested-sampling run, despite their relevance to model comparison.  
- **Fix**: (1) Include pre-computed chains/postprocess scripts for all headline MCMC results. (2) Either compute ln B for model comparisons or remove claims implying Bayesian evidence (e.g., "consistent with zero" is acceptable; "disfavored at Xσ" is not without ln B).  

**P1B-M2: Misleading ALP-MCMC prior range**  
- **Section**: VI (page 6–7), Appendix C  
- **Problem**: The ALP-MCMC uses θi ∈ [0.5, 2] for misalignment angle, but the spectator-consistent regime requires θi ∼ 0.1 (disclosed in Sec. VI and fn. 4). Sampling θi ∈ [0.5, 2] inflates the allowed Caγ range ([9, 51]) and obscures the ∼25× tuning needed. This contradicts the paper’s own scope restriction.  
- **Fix**: Restrict ALP-MCMC priors to the spectator-consistent regime (θi ≪ 1, e.g., θi ∈ [0.05, 0.15]) and recompute βALP constraints. Clarify that θi ∈ [0.5, 2] samples correspond to dark-energy ALPs, not spectators.  

**P1B-M3: Unqualified pipeline SNR vs. sky significance**  
- **Section**: Abstract (page 1), IV (page 5)  
- **Problem**: The pipeline-recovery SNR (20.32σ, 25.71σ) is presented alongside sky-detection σ (2.4–2.9σ) without explicit qualification in the abstract and conclusions. Though Sec. IV notes the distinction, headline readers may conflate the ∼20σ (MC bias test) with cosmological significance.  
- **Fix**: In abstract/conclusions, add "pipeline" qualifier to all >5σ SNR values (e.g., "pipeline-recovery SNR of 20.32σ"). Add a cautionary phrase: "These SNR values measure MC signal recovery, not physical sky significance."  

---

### MINOR Findings  
**P1B-m1: Ambiguous dataset attribution**  
- **Section**: Abstract footnote (page 1), VI (page 6)  
- **Problem**: The β = 0.342° ± 0.094° value is attributed to Planck PR3+WMAP9 in the abstract footnote but called "Planck PR4/NPIPE" in Sec. VI. The footnote explains the discrepancy (code repo uses PR4), but this risks reader confusion.  
- **Fix**: Standardize terminology: Use "Eskilt & Komatsu (2022) joint PR3+WMAP9 analysis" for the headline value and "updated PR4/NPIPE dataset in reproduction code" for technical details.  

**P1B-m2: Burn-in arithmetic inconsistency**  
- **Section**: III (page 3), Table I footnote  
- **Problem**: The post-burnin sample calculation (176,240 × 0.7 ≈ 123,368) is inconsistent with the text’s "123,129" (a stated arithmetic error) and GetDist-thinned "119,617." This undermines traceability.  
- **Fix**: Correct all sample counts: Report exact post-burnin counts (e.g., 123,368 for full-tension) and clarify thinning steps in Appendix A.  

**P1B-m3: Unclear "decomposition" reference**  
- **Section**: Abstract (page 1)  
- **Problem**: The abstract references a decomposition "99.3%/12%/88%/25%" with no context or explanation in the paper. This appears to be an artifact from a previous draft.  
- **Fix**: Remove the unsupported decomposition or define it (with provenance) in the body.  

---

### NIT Findings  
**P1B-N1: Redundant phrasing**  
- **Section**: III (page 3)  
- **Problem**: Duplicate phrase: "the canonical Hubble-tension result, not a YAML omission" → "canonical" is repeated unnecessarily.  
- **Fix**: Replace with: "the standard Hubble-tension result, not a YAML omission."  

**P1B-N2: Inconsistent parameter notation**  
- **Section**: V.B (page 6), Table II  
- **Problem**: Sampled parameters use mixed notation: "w0 wa" (no subscript) vs. "wpivot" (subscript).  
- **Fix**: Standardize to subscripts (w₀, wₐ, w_pivot) for all dark-energy parameters.  

---

## Summary Recommendation  
**MINOR REVISIONS**  

### Justification  
The paper provides valuable technical verification for the ECH spin-torsion program, with clearly scoped analyses and generally robust methodology. The core results—∆Neff ≈ 0 in ΛCDM, NaMaster pipeline validation, and ALP consistency—are well-supported and reproducible via the GitHub repository. However, minor revisions are essential to:  
- Eliminate internal artifacts (e.g., version-control references) and unsupported claims (LiteBIRD σ(β)).  
- Ensure immediate reproducibility of headline MCMC figures (pre-compute chains or provide likelihoods).  
- Align ALP-MCMC priors with the spectator-consistent regime to avoid overstating naturalness.  
- Clarify distinctions between pipeline-recovery and sky-detection significances in abstracts/conclusions.  
The requested fixes are tractable and will strengthen the paper’s clarity, traceability, and alignment with PRD standards. Page count (11 pages) is appropriate for the contribution.