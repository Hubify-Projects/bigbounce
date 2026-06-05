# P2 2026-06-04_R2pt — Confabulation-hunter referee (reasoning mode)

**Model**: `deepseek/deepseek-r1-0528`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 208.8s

---

## Referee Report for Paper P2  

### ESSENTIAL Revisions  
- **P2-E1**: Abstract and Sec. II.C (p. 2, 5)  
  **Problem**: The decomposition "99.3%/12%/88%/25%" referenced in the instructions is absent from the abstract, conclusions, and provided text. This critical decomposition is load-bearing for the systematic budget but lacks provenance or definition.  
  **Required Fix**: Define and source this decomposition explicitly. Provide a table or equation showing how these percentages combine (e.g., total systematic error budget) and cite computational artifacts (script/JSON) that reproduce them.  

- **P2-E2**: Abstract and Sec. III.B (p. 1, 6–7)  
  **Problem**: Template-mismatch uncertainty (r = 0.84 ± 0.02) is central to the significance forecast (3–5σ), but no reproducible source (script/dataset) is provided for the 10,000-sample null-space scan or Fisher overlap calculations. The claim that "r = 0.84 ± 0.02 spans all weighting schemes" is unsupported.  
  **Required Fix**: Release code/JSON for the null-space scan (`phase3_fisher_overlap.json`), Fisher weighting schemes, and injection-recovery tests. Specify input parameters (e.g., k-grid, SVD tolerance) to enable independent replication.  

- **P2-E3**: Abstract and Sec. VI (p. 1, 9–11)  
  **Problem**: Bayes factors (BF ≈ 10–17) derive from Monte Carlo ensembles (3×10⁵ realizations) cited as "04b_fast_ensemble.py" etc., but these scripts are inaccessible. The closed-form Bayes factor (Eq. 7) assumes a uniform competitor prior, but the text notes prior sensitivity (e.g., BF drops to ≈4 for a curvaton-natural prior). This prior-dependence is not transparent in the abstract.  
  **Required Fix**: Release all ensemble scripts and priors. Justify prior ranges (e.g., why [−15, +15] for "broad multifield") and show BF distributions. Clarify prior assumptions in the abstract.  

- **P2-E4**: Throughout (e.g., p. 1, 3, 5)  
  **Problem**: Internal versioning tags (e.g., "v1.7.43", "corrected v1.7.35 R-next-c-MAJ-1") and audit artifacts (e.g., "App. A establishes that the Cai convention is correct") appear in body prose. These are inappropriate for a final submission.  
  **Required Fix**: Remove all version history, audit tags, and review-log artifacts (e.g., "R42 Gemini 3.1-Pro P2 BLOCKER B-3").  

### MAJOR Revisions  
- **P2-M1**: Abstract and Sec. IV (p. 1, 8)  
  **Problem**: The headline σ(fNL) ≈ 0.7 for SPHEREx is sourced to Heinrich et al. (2024) but applied to fNL = −4.375 without verifying Fisher-matrix linearity at non-zero fiducial fNL. The 5.2–5.5σ "optimistic" claim requires this assumption, which is not validated.  
  **Required Fix**: Recompute the Fisher matrix at fNL = −4.375 or quantify the error from fiducial shift. Adjust significance if degradation exceeds 5%.  

- **P2-M2**: Sec. II.C and VII (p. 5, 12–14)  
  **Problem**: The ϵ-correction uncertainty (1–8%) and κ₁ range (5.6–80) are stated but not propagated jointly into fNL uncertainty. The systematic budget (Sec. VII) treats them as independent, potentially underestimating errors.  
  **Required Fix**: Perform joint uncertainty propagation (e.g., Monte Carlo over ϵ and κ₁). Show how fNL = −35/8 varies within the ϵ–κ₁ parameter space.  

- **P2-M3**: Sec. III.B and VII (p. 7, 13)  
  **Problem**: The scale-dependent bias (SDB) channel’s σ(fNL) is highly sensitive to bϕ prior width (Fig. 5), but the bispectrum channel’s robustness to bϕ marginalization is asserted without evidence. The abstract’s 3–5σ range assumes bϕ universality, but relaxing this degrades σ(fNL) by 20–50%.  
  **Required Fix**: Quantify bispectrum σ(fNL) degradation when bϕ is marginalized per tracer bin (cf. Barreira 2022). Update the systematic budget accordingly.  

- **P2-M4**: Sec. IX.D (p. 18)  
  **Problem**: Claims of nfNL = 0 as a bounce discriminator are unsupported. The joint (fNL, nfNL) Fisher forecast (σ(nfNL) = 0.086) is deferred to a "companion artifact" and lacks provenance.  
  **Required Fix**: Release Fisher inputs (redshift bins, k_min(z), n̄(z)) or integrate the analysis into the main text. Clarify how nfNL breaks degeneracies with inflationary models.  

### MINOR Revisions  
- **P2-m1**: Abstract and Sec. II (p. 1, 4)  
  **Problem**: The polynomial-coefficient null space (c₁–c₆) introduces ±0.13 scatter in r, but the abstract cites this as "∼15% relative scatter" without showing arithmetic: 0.13/0.85 ≈ 15.3% is correct, but the range r = 0.55–1.14 implies asymmetric uncertainty.  
  **Required Fix**: Report asymmetric errors (e.g., r = 0.85^{+0.29}_{−0.30}) or justify the symmetric ±0.13.  

- **P2-m2**: Sec. VI (p. 10)  
  **Problem**: The Bayes factor BF ≈ 10–17 is presented as a headline, but Table II shows it drops to ≈4–7 for a curvaton-natural prior. This prior-sensitivity is buried in prose, not the abstract.  
  **Required Fix**: Highlight prior-dependence in the abstract (e.g., "BF ∼ 10–17 under broad priors, but ∼4–7 for natural curvaton models").  

- **P2-m3**: Sec. VIII.B (p. 16)  
  **Problem**: The fNL–ns consistency relation (Eq. 9) uses ns = 0.9649 from Planck but does not propagate observational error in ns to fNL uncertainty.  
  **Required Fix**: Add ns uncertainty (σ_ns ≈ 0.0042) to Eq. 9 and show fNL bounds.  

### NIT Revisions  
- **P2-n1**: Sec. II.A (p. 3)  
  **Problem**: The monomial basis for P(k₁,k₂,k₃) is defined but not explicitly mapped to Cai et al.’s operators (e.g., "partitions (9,0,0), (7,2,0)").  
  **Required Fix**: Add a table mapping monomials (e.g., kᵢ⁹) to vertex operators (e.g., L_redef).  

- **P2-n2**: Sec. IV (p. 8)  
  **Problem**: "Anomaly-detected QSO candidates" are invoked for multi-tracer gains but lack DESI/SDSS references or quantitative impact.  
  **Required Fix**: Cite Baron & Poznanski (2017) and Liang et al. (2023) and quantify the σ(fNL) improvement (e.g., "∼10–20%").  

---  
### Summary Recommendation  
**MAJOR REVISIONS**  

Justification: The paper presents a timely forecast for SPHEREx to test the matter-bounce fNL = −35/8, but critical elements lack reproducibility or provenance. Essential revisions include (1) releasing code/artifacts for the null-space scan and Bayes factor ensembles, (2) removing internal versioning tags, and (3) clarifying the undefined "99.3%/12%/88%/25%" decomposition. Major revisions are needed to address statistical oversights, including unvalidated Fisher-matrix linearity, unpropagated ϵ–κ₁ uncertainties, and marginalized bϕ impacts. The 23-page length is acceptable, but the systematic budget requires tightening to support the 3–5σ headline claim.