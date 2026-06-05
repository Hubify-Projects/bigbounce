# P4 2026-06-04_R5clean — Confabulation-hunter referee (reasoning mode)

**Model**: `deepseek/deepseek-r1-0528`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 179.2s

---

## Referee Report for P4: Confabulation-Hunter Review (Round 2026-06-04_R5clean)

### ESSENTIAL Revisions  
**P4-E1: Abstract/Conclusions: Untraced 99.3%/12%/88%/25% decomposition**  
- **§IV D (p.21), Table VIII**: The decomposition chain (99.3% pre-MASTER leakage → 12% post-MASTER monopole contribution → 88% residual → 25% leg-proxy) lacks consolidated provenance. While 99.3% is calculated in Table VII (1.6846e-2 / 1.696e-2), the 12% (8.0e-7 / 6.55e-6) and 25% are only qualitatively attributed. No JSON/script computes the full decomposition end-to-end.  
- **Fix**: Provide a single script (`decompose_leakage_residual.py`) outputting a JSON with all percentages derived from primary artifacts (e.g., `monopole_mask_null_results.json`, `master_decoupled_monopole_null.json`).  

**P4-E2: Abstract: Untraced 0.75% sensitivity threshold**  
- **§VI C (p.36), Table XVI**: The ≥0.75% empirical 50%-recovery-3σ threshold is claimed but relies on `pipelines/p2_chirality/outputs/canonical_provenance/wave_14_nn_injection_recovery.json` (N=100 injections). This artifact is not provided in the data availability statement (§IX).  
- **Fix**: Deposit the injection-recovery JSON at the HuggingFace repository with a DOI. Cross-link it explicitly in Table XVI.  

**P4-E3: §IV C (p.18): Unvalidated σ collapse (6.48σ → -0.12σ)**  
- **Table VI**: The raw pseudo-Cℓ (ℓ∈[2,6]) drops from +6.48σ to -0.12σ after MASTER. The calculation assumes a Poisson shot-noise denominator N_spiral=3.2M, but the correction ratio (N_tot/N_spiral=2.65) is not independently verified.  
- **Fix**: Add a script (`validate_shot_noise.py`) recomputing Cℓ with both N_tot and N_spiral denominators, confirming the 2.65× correction factor.  

### MAJOR Revisions  
**P4-M1: §III E (p.11): Unsupported D4-TTA invariance claim**  
- **Table II (row vii)**: Claims |Δ⟨p_CW⟩| < 0.0016 under D4-TTA but cites two disjoint holdouts (N=1,558 and N=1,988). No statistical test (e.g., paired t-test) justifies pooling these.  
- **Fix**: Re-run D4-TTA on a single N≥3,000 holdout; report p-value for ⟨p_CW⟩_Z2 vs. ⟨p_CW⟩_D4.  

**P4-M2: §IV B (p.15): Inconsistent monopole significance**  
- **Table V**: Catalog C global asymmetry is -0.26% (9.5σ from binomial), but a bootstrap gives 28.80σ for Catalog A. The transition is attributed to TTA but lacks per-galaxy flip-pair analysis.  
- **Fix**: Add a table showing per-galaxy (p_CW^orig, p_CW^flip) for 10^4 galaxies to quantify TTA’s effect on the monopole.  

**P4-M3: §VI C (p.36): Unjustified 0.75% vs. 0.29% sensitivity gap**  
- **Table IX**: The empirical 50%-rec-3σ threshold (0.75%) is 2.5× higher than the Fisher floor (0.29%). No systematic (e.g., depth-correlated noise) is quantified to explain this gap.  
- **Fix**: Add a depth-stratified injection test to isolate systematics-driven variance.  

**P4-M4: Paper Length**  
- 56 pages exceeds PRD’s 15-30pp guideline for methods papers. The bias-hardening suite (§III F) and systematics tables (Table XI) are verbose.  
- **Fix**: Condense to ≤40pp by moving training details (§III C) to a supplement and compressing Tables IV, X, XI.  

### MINOR Revisions  
**P4-m1: §I (p.3): "canonical canonical-mask" duplication**  
- **Title, Abstract**: "Canonical-Mask Residual" appears twice in the title; "canonical canonical-mask" in text.  
- **Fix**: Remove duplicates: "Survey-Scale Galaxy Chirality [...] and Diagnostic Evidence for a Depth/Morphology-Correlated Residual".  

**P4-m2: §IV D (p.21): Version-history artifact**  
- **Table VII footnote**: References a superseded "smoke result at N=25".  
- **Fix**: Remove historical references; state "N=500 binomial realizations" without legacy context.  

**P4-m3: §II B (p.4): Ambiguous label sourcing**  
- **§II B**: 67.6% of training labels derive from CE-ResNet, but the independent GZ1 agreement (69.91%) is not reconciled with circularity concerns.  
- **Fix**: Clarify in text: "CE-ResNet labels dominate training but GZ1 validation shows no overfitting (κ=0.40)".  

### NIT Revisions  
**P4-n1: §IV C (p.17): "σ" without null specification**  
- **Text**: "ℓ=2 > ℓ=1 broadband structure" cites σ values without referencing Table II’s null mappings.  
- **Fix**: Append "(per binomial null)" to each σ mention in §IV D.  

**P4-n2: §V (p.32): Redundant Shamir comparisons**  
- **§V A**: Repeats "not a likelihood-level exclusion" 3×.  
- **Fix**: Consolidate to one statement: "Amplitude inconsistency under different pipelines does not refute Shamir’s estimator; a matched-footprint reanalysis is required."  

---

## Summary Recommendation  
**MAJOR REVISIONS**  

Justification: The paper reports a significant null result but requires major revisions to address confabulation risks. Essential fixes include providing artifacts for the 99.3%/12%/88%/25% decomposition and the 0.75% sensitivity threshold. Major revisions are needed to validate the D4-TTA invariance claim, justify sensitivity gaps, and condense length. The core science is robust, but provenance gaps (e.g., missing injection-recovery JSON) and unverified arithmetic (e.g., shot-noise correction) undermine reproducibility. Addressing these will align the paper with PRD’s standards for computational cosmology.