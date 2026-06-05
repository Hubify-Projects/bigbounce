# P5 2026-06-04_R2pt — Confabulation-hunter referee (reasoning mode)

**Model**: `deepseek/deepseek-r1-0528`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 314.6s

---

## Referee Report for Paper P5

### ESSENTIAL Revisions

- **P5-E1**: Header  
  **Problem**: The header includes version-history language: "(Dated: June 4, 2026 — v0.1.45-2026-06-04)". This is an internal development artifact inappropriate for a submission.  
  **Fix**: Remove all versioning tags and commit history from the manuscript body.

- **P5-E2**: Abstract and §VI A (Cosmic-web σ values)  
  **Problem**: σ values from binomial tests (e.g., filament: −2.61σ, cluster: −4.66σ) are presented alongside label-shuffle permutation nulls (e.g., HEALPix scans: p = 0.61/0.135/0.413) without clarifying that these σ scales are methodologically distinct. Binomial σ assumes Gaussianity, while permutation σ is empirical. This risks conflating statistical scales.  
  **Fix**: Explicitly qualify all σ values by their null procedure (e.g., "binomial σ" vs. "permutation σ") and add a cautionary footnote in the abstract and §V about cross-method comparability.

---

### MAJOR Revisions

- **P5-M1**: Abstract and §V B (Primary analysis path)  
  **Problem**: The primary result (DESIVAST-anchored void cross-check, §VIII) was selected post-hoc from 5+ classifiers/stratifications without pre-registration or family-wise error control. This "garden of forking paths" inflates false-positive risk. The Bonferroni adjustment in §V B only covers DESIVAST estimators, but secondary paths (e.g., V-Web filament bright/dark sign-flip, |z| ≈ 3.4σ) are reported as "real" without multiplicity correction.  
  **Fix**: Pre-register the DESIVAST path as primary in the introduction (not retroactively in §V B). Apply a unified family-wise correction (e.g., Bonferroni-Holm) to *all* test statistics (including bright/dark sign-flip and Tempel cross-validation). Reassess significance of the 3.4σ filament sign-flip after full correction.

- **P5-M2**: §III B and Data Availability  
  **Problem**: Critical scalars (e.g., DESI DR1 input rows: 16,361,731; ZWARN=0 filtered: 14,622,283) lack traceable provenance. The cited script (`02_fetch_desi_dr1.py`) is inaccessible (internal path without public repo/dataset). Similarly, headline values (e.g., V-Web void n=428) cannot be reproduced from displayed data alone.  
  **Fix**: Publish all data and scripts in a DOI-archived repository (e.g., Zenodo). Provide direct URLs to:  
  (a) DESI DR1 zall catalog snapshot with SHA-256,  
  (b) CSV/JSON for Table I/VIII/XII,  
  (c) Phase 2 sweep outputs (§VII).  
  Anchor *all* scalars in abstract/results to these public artifacts.

- **P5-M3**: Abstract and §XIII (Limitations: RSD)  
  **Problem**: The scalar displacement heuristic (σ_v /(aH) ≲ 5 Mpc/h vs. R_s=25 Mpc/h) is used to dismiss redshift-space distortions (RSD) but ignores anisotropic tidal tensor deformation. The claimed "sub-percent" RSD contamination (∼0.2 pp) is unquantified and contradicts the Phase 2 sweep range (0.22 pp), which is sensitive to this effect.  
  **Fix**: Quantify RSD impact via Zel’dovich reconstruction cross-check on a 256³ subgrid. Report max |Δf_CW| between real- and redshift-space classifications. If unavailable, state RSD as a major systematic limitation in the abstract.

- **P5-M4**: §VIII F (P4-monopole residual analysis)  
  **Problem**: The catalog-wide monopole offset (Δf_CW = −0.0026 from Paper IV) is propagated as σ_pred = 2 · Δf_CW · √N, but Paper IV is unpublished and its uncertainty is not propagated. The residual analysis (σ_obs − σ_pred) assumes Δf_CW is error-free.  
  **Fix**: Propagate Paper IV’s monopole uncertainty (e.g., ±0.000279 from Paper IV abstract) into σ_pred. Show how σ_obs − σ_pred changes when Δf_CW varies over its 1σ interval.

---

### MINOR Revisions

- **P5-m1**: §VI A and Table II  
  **Problem**: Void sample size (n=428) has a 95% binomial CI [0.435, 0.530], which includes parity (0.5) but also excludes the cluster fraction (0.4963). The narrative dismisses it as "statistical noise" without showing the CI overlaps other classes.  
  **Fix**: Add 95% CIs to Table II/Fig. 2 and state explicitly: "Void CI overlaps all other classes and parity."

- **P5-m2**: §IX B (Concurrent T-Web validation)  
  **Problem**: The T-Web comparison (Ref. [11]) uses tracer-dependent volume fractions, but V-Web fractions are tracer-agnostic. The 8–18 pp void-fraction discrepancy is attributed to "survey-shell systematic" without quantitative support.  
  **Fix**: Add a table comparing V-Web vs. T-Web volume fractions *for the same tracer subset* (e.g., BGS-only). Estimate the shell-artifact contribution via a DESI mask convolution simulation.

- **P5-m3**: §X (ASTRA cross-validation)  
  **Problem**: The ASTRA EDR cross-match (n=25,186) is underpowered vs. primary analysis (n∼791k), yet conclusions are equated. The V-Web/ASTRA label disagreement (e.g., void: 11.9% vs. 0.244%) is noted but not reconciled.  
  **Fix**: Clarify that ASTRA is a consistency check on a small subsample, not an independent validation. Discuss classifier discordance in a footnote.

---

### NIT Revisions

- **P5-n1**: Abstract  
  **Problem**: "the decomposition 99.3%/12%/88%/25% adds up consistently" – these values do not appear in the paper. Likely a relic from a template.  
  **Fix**: Remove the phrase or replace with actual values (e.g., V-Web volume fractions: 24.4%/41.3%/33.3%/1.0%).

- **P5-n2**: §III A  
  **Problem**: "canonical canonical-mask" appears in text (duplicate phrase).  
  **Fix**: Remove one "canonical".

- **P5-n3**: §IV A  
  **Problem**: Poisson equation in k-space (Step 8) omits the −4πG factor (standard in Hahn et al. 2007).  
  **Fix**: Correct to Φ(k) = −4πG δ_k / k² (comoving units).

---

## Summary recommendation
**MAJOR REVISIONS**

The paper presents a rigorous null test of environment-dependent chirality, but critical issues undermine its reproducibility and statistical validity. The post-hoc choice of primary analysis inflates false-positive risk, while inaccessible data/scripts prevent verification of headline numbers (e.g., n=428 void galaxies). RSD systematics are dismissed without quantification, and dependence on an unpublished companion paper (Paper IV) propagates unconstrained uncertainties. The core conclusion—no chirality dependence at DESI DR1 sensitivity—is plausible, but requires: (1) pre-registration of the analysis path, (2) full public data/code release, (3) RSD cross-checks, and (4) propagation of Paper IV's monopole errors. Addressing these is essential before reconsideration.