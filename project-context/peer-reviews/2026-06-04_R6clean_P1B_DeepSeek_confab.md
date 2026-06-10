# P1B 2026-06-04_R6clean — Confabulation-hunter referee (reasoning mode)

**Model**: `deepseek/deepseek-r1-0528`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 274.5s

---

## Referee Report

### ESSENTIAL Findings  
*(Paper cannot be accepted without these fixes)*  

- **P1B-E1** (Abstract, page 1; Conclusions, page 7):  
  - **Problem**: The abstract and conclusions claim ∆N<sub>eff</sub> = −0.020 ± 0.169 (full-tension) and +0.065 ± 0.17 (Planck+BAO+SN), but no traceable source (script/data) is provided for these critical values. The reproducibility repository lacks pre-computed MCMC chains, and the paper instructs users to regenerate chains via `reproduce_cosmology.sh` (Appendix A), which is not feasible for verification without computational resources.  
  - **Required Fix**: Provide frozen posterior samples (e.g., as CSV/HDF5) in the repository for both dataset combinations. Label chains clearly to match Table I results.  

- **P1B-E2** (Section VI, page 6; Conclusions, page 7):  
  - **Problem**: The ALP-MCMC result β<sub>ALP</sub> = 0.336° ± 0.107° (C<sub>aγ</sub> = 8) and β<sub>free</sub> = 0.344° ± 0.096° are presented without provenance. The repository lacks ALP-MCMC chains, and the 9,720-sample run is described only in prose (no scripts/configurations for ALP trajectory scans).  
  - **Required Fix**: Include ALP-MCMC chains and driver scripts (e.g., Cobaya YAML for β-free fit, numerical integration code for Δϕ/f<sub>a</sub> trajectories) in the repository.  

- **P1B-E3** (Section IV, page 5; Abstract, page 1):  
  - **Problem**: The NaMaster recovery bias Δβ̂ = 0.032° (for β = 0.27° injected) and SNR=20.32 are critical pipeline-validation figures, but the repository only lists driver scripts—no output spectra, mask, or MC seeds are provided. The paper states, "Full driver script, mask, MC seeds, and binning specification are in pipelines/h200..." but this path is inaccessible.  
  - **Required Fix**: Upload all NaMaster artifacts (mask, spectra, MC seeds) to GitHub. Add a notebook to regenerate Eq. (1) (β̂ = 0.238°) from inputs.  

---

### MAJOR Findings  
*(Significant revision required)*  

- **P1B-M1** (Section III, page 3; Table I footnote):  
  - **Problem**: Sample-count inconsistency: Abstract cites 309,189 raw samples, but Table I footnote states 176,240 (full-tension) + 132,949 (Planck+BAO+SN) = 309,189 samples. Later, Section III claims 119,617 post-burnin samples for Fig. 1 (176,240 × 0.7 ≈ 123,368 expected). Arithmetic disagrees: 123,368 ≠ 119,617.  
  - **Required Fix**: Reconcile sample counts. Clarify burn-in removal (30% of each chain? 30% of total?). Provide exact post-burnin counts for both chains.  

- **P1B-M2** (Section VI, page 6):  
  - **Problem**: The spectator-ALP "natural" parameter range (C<sub>aγ</sub> ∈ [4,12], m/H<sub>0</sub> ∈ [1,3], θ<sub>i</sub> ∈ [0.5,2]) yields β ≈ 0.17–0.43° but omits the backreaction tuning (θ<sub>i</sub> ∼ 0.1 requires 25× fine-tuning). This is buried in fn.4; the load-bearing β ≈ 0.27° (midpoint) misrepresents naturalness.  
  - **Required Fix**: Disclose tuning prominently in Section VI body. Quantify prior volume for θ<sub>i</sub> ∼ 0.1 vs. θ<sub>i</sub> ∼ 0.5. Update β envelope to reflect spectator-consistent sub-range.  

- **P1B-M3** (Section V.B, page 6; Table II caption):  
  - **Problem**: Table II (DESI DR2 w<sub>0</sub>w<sub>a</sub> posterior) reports χ<sup>2</sup> decomposition (e.g., χ<sup>2</sup><sub>BAO</sub> = 10.6 ± 1.8), but no script or method is given for computing per-likelihood χ<sup>2</sup> from MCMC samples. Reproducibility is infeasible.  
  - **Required Fix**: Add Cobaya YAML configuration for the w<sub>0</sub>w<sub>a</sub> run to the repository. Include a script to compute χ<sup>2</sup> decomposition from chains.  

---

### MINOR Findings  
*(Should be addressed; paper can proceed with editor discretion)*  

- **P1B-m1** (Abstract, page 1; Section III, page 3):  
  - **Problem**: ∆N<sub>eff</sub> errors inconsistently rounded: full-tension uses ±0.169 (3 decimals), Planck+BAO+SN uses ±0.17 (2 decimals). Table I repeats this.  
  - **Required Fix**: Standardize errors to 2 decimals (e.g., −0.02 ± 0.17 and +0.07 ± 0.17) or report full precision.  

- **P1B-m2** (Section IV, page 5):  
  - **Problem**: The pipeline-recovery bias for β = 0.342° is initially called "stable" at 0.032° but later corrected to 0.040° in prose. This undermines the bias characterization.  
  - **Required Fix**: Report all injection biases in a table (β = 0°, 0.27°, 0.342°). State explicitly: "Bias scales mildly with amplitude."  

- **P1B-m3** (Appendix A, page 8):  
  - **Problem**: The repository claims to include "four Cobaya YAML configurations" but omits the w<sub>0</sub>w<sub>a</sub> configuration (Sec. V/Table II).  
  - **Required Fix**: Add the w<sub>0</sub>w<sub>a</sub> YAML to the repository.  

---

### NIT Findings  
*(Very minor; fix if time permits)*  

- **P1B-N1** (Section I, page 2):  
  - **Problem**: Duplicate phrase: "companion paper, this volume" repeated in cross-paper citations.  
  - **Required Fix**: Remove duplicates; use [1], [4], etc., consistently.  

- **P1B-N2** (Table I, page 3):  
  - **Problem**: Units for H<sub>0</sub> ("km s<sup>−1</sup> Mpc<sup>−1</sup>") missing in the table; only in abstract.  
  - **Required Fix**: Add units to Table I header.  

---

## Summary recommendation  
**MAJOR REVISIONS**  

The paper documents critical verification analyses for the ECH spin-torsion program but suffers from severe reproducibility gaps. Load-bearing numbers (∆N<sub>eff</sub>, H<sub>0</sub>, β<sub>ALP</sub>, NaMaster bias) lack traceable data/scripts, and sample-count inconsistencies undermine confidence. The ALP naturalness claim is misleading without quantifying fine-tuning. While the scope limitations (e.g., stock CAMB ≠ torsion theory) are well-defined, the absence of frozen chains, ALP-MCMC outputs, and NaMaster artifacts prevents independent verification. Major revisions must address ESSENTIAL/MAJOR issues by providing complete datasets, reconciling sample counts, and disclosing ALP tuning. The 10-page length is acceptable given the three analyses.