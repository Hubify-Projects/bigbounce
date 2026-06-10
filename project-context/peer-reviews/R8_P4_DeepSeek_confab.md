# P4 R8 — Confabulation-hunter referee (reasoning mode)

**Model**: `deepseek/deepseek-r1-0528`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 249.5s

---

## Referee Report: Paper P4, Round R8

### ESSENTIAL Revisions

**P4-E1: Abstract and Section IV.B (Page 4)**  
- **Problem**: The reported 9.5σ deviation for Catalog C's global CW fraction (0.4974 ± 0.0003) is inconsistent with binomial uncertainty. Given \(N_{\text{spiral}} = 3,201,160\), the binomial standard deviation is \(\sigma = \sqrt{0.5 \times 0.5 / N} \approx 0.000279\), yielding \(z = (0.4974 - 0.5) / 0.000279 \approx -9.32\sigma\), not 9.5σ. The ±0.0003 uncertainty in Table II is either incorrect or misapplied.  
- **Required Fix**: Recalculate uncertainties using exact binomial statistics. Report \(\sigma = 0.000279\) and update deviations (e.g., Catalog C: \(-9.32\sigma\)) or justify the ±0.0003 value. Ensure all tables/text match.  

**P4-E2: Section IV.D and Table IV (Page 5)**  
- **Problem**: The \(z = +1.68\sigma\) for the monopole-only null (Table IV) is inconsistent with the provided data: \((1.696 \times 10^{-2} - 1.685 \times 10^{-2}) / 0.007 \times 10^{-2} = 1.57\sigma\), not 1.68σ. This undermines the 99.3% leakage claim.  
- **Required Fix**: Correct the calculation or provide the exact null standard deviation used. Reconcile with the 99.3% amplitude recovery claim.  

### MAJOR Revisions

**P4-M1: Abstract and Section IV.C (Page 4)**  
- **Problem**: The headline dipole significances (\(-0.12\sigma\), \(+0.43\sigma\), \(+3.64\sigma\)) lack explicit provenance in scripts/data. While reproducibility scripts are cited (Data Availability), no specific script/JSON path generates these exact values (e.g., NaMaster outputs for \(-0.12\sigma\)).  
- **Required Fix**: In Section IV or Appendix A, reference a specific script (e.g., `scripts/dipole_analysis.py`) and dataset version that outputs these \(\sigma\) values. Provide a code snippet or log excerpt in the supplement.  

**P4-M2: Section VI.A (Page 6)**  
- **Problem**: The empirical threshold \(A \approx 0.75\%\) for 50%-recovery-at-3σ conflicts with the Fisher floor (0.29%). The text attributes this to "classification noise" but does not quantify the dilution factor (e.g., GZ1 accuracy 69.91% → effective \(N\) reduction).  
- **Required Fix**: Derive the threshold mathematically: show \(A_{\text{empirical}} = A_{\text{Fisher}} / f_{\text{dilution}}\) with \(f_{\text{dilution}}\) calculated from GZ1 accuracy. Update Section VI.A to resolve the discrepancy.  

**P4-M3: Section IV.D and Appendix D (Page 5, 8)**  
- **Problem**: The narrative inconsistently attributes the \(+3.64\sigma\) residual: Section IV.D calls it a "systematics-attributed canonical-mask excess," but Appendix D (e.g., "WLS template-model disfavor") implies it could be partly cosmological. This contradicts the abstract's "non-headline" framing.  
- **Required Fix**: Clarify in Section IV.D that the \(+3.64\sigma\) is definitively systematic (per cross-spectrum/density tests). Remove ambiguous language in Appendix D (e.g., "far-tail" dipole posterior).  

### MINOR Revisions

**P4-M4: Section II.B (Page 3)**  
- **Problem**: Training labels are 67.6% derived from CE-ResNet predictions, but validation metrics (69.91% accuracy) are reported against "full training set," conflating agreement with CE-ResNet vs. ground truth.  
- **Required Fix**: Report standalone validation against Galaxy Zoo 1 (without CE-ResNet labels) to isolate ground-truth performance.  

**P4-M5: Section III.A (Page 3)**  
- **Problem**: Estimator hierarchy declares "primary cosmological estimators" (i) and (ii), but Table I includes non-primary diagnostics (iii)–(vi) without visual distinction (e.g., bolding).  
- **Required Fix**: Reform Table I to group primary (i–ii) and diagnostic (iii–vi) estimators. Add a note: "Primary estimators in bold."  

### NIT Revisions

**P4-N1: Abstract and Section I**  
- **Problem**: Duplicate phrase "canonical-mask" in title ("Canonical-Mask Residual") and abstract ("canonical mask").  
- **Required Fix**: Shorten title to "Depth/Morphology-Correlated Residual" or similar.  

**P4-N2: Section IV.C (Page 4)**  
- **Problem**: "post-MASTER canonical-mask direct-MC residual is +3.64σ (empirical rank: \(p_{\text{MC}} = 0.030\))" – \(p_{\text{MC}}\) is undefined.  
- **Required Fix**: Define \(p_{\text{MC}}\) as "permutation null p-value" on first use.  

---

## Summary Recommendation  
**MAJOR REVISIONS**  

Justification: The paper reports a rigorous null dipole result (\(-0.12\sigma\)) with valuable systematic checks, but essential numerical inconsistencies (P4-E1, P4-E2) and insufficient provenance for headline figures (P4-M1) preclude acceptance. Major revisions are required to:  
- Correct statistical errors in global fraction and leakage calculations.  
- Provide explicit script/data paths for all \(\sigma\) values.  
- Resolve conflicts between the empirical/Fisher thresholds and narrative consistency on the \(+3.64\sigma\) residual.  
Minor/nit issues (e.g., table formatting, training validation) should be addressed to enhance clarity. The core science is sound, but reproducibility and numerical rigor must be elevated.