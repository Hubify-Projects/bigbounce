# P1B 2026-06-04_1814pt — Confabulation-hunter referee (reasoning mode)

**Model**: `deepseek/deepseek-r1-0528`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 250.3s

---

## Referee Report for Paper P1B: "Technical Verification Companion to the ECH Spin-Torsion Program"

### ESSENTIAL Revisions  
**P1B-E1**  
- **Section**: Table I footnote  
- **Issue**: Internal audit tag preserved ("Not the stale mid-burn-in diagnostic convergence gpu 20260305 stale.csv (R̂ − 1 ∈ [0.23, 0.86]), preserved as a transparency artifact only"). This is not appropriate for publication.  
- **Fix**: Remove all internal audit tags and version-specific debugging artifacts.  

**P1B-E2**  
- **Section**: Abstract, footnote a; Section VI, footnote 4  
- **Issue**: Internal review tags ("per R-upgraded-round4 GEM-m2", "per R-upgraded-round4 GEM-B1") appear in body prose. These are non-scientific artifacts.  
- **Fix**: Eliminate all internal review codes (e.g., "R-upgraded-round4", "GEM-m2", "GEM-B1") from the manuscript.  

**P1B-E3**  
- **Section**: Abstract, IV, Conclusions  
- **Issue**: Pipeline recovery SNR (20.32σ) and sky detection significance (2.4–2.9σ) presented without explicit qualification that they are on different scales (MC injection recovery vs. physical measurement). Abstract states they are distinct but does not prevent conflation.  
- **Fix**: Add bold disclaimer in Abstract: "Pipeline SNR (20.32σ) quantifies MC signal recovery, not physical sky significance (2.4–2.9σ)." Repeat in Sec. IV and Conclusions.  

**P1B-E4**  
- **Section**: III, Table I; Abstract  
- **Issue**: Load-bearing scalars (∆Nₑff = -0.020 ± 0.169, H₀ = 67.68 ± 1.06 km/s/Mpc) lack traceable code. Repository has YAML/config files but no script to reproduce posterior means/stds from chains.  
- **Fix**: Provide executable script (e.g., `compute_posteriors.py`) that ingests chains and outputs Table I values.  

---

### MAJOR Revisions  
**P1B-M1**  
- **Section**: V.B, Table II  
- **Issue**: Critical w₀/wₐ posteriors (w₀ = -0.8122 ± 0.0436, w₀ + wₐ = -1.4788 ± 0.1485) not reproducible. Repository lacks script to generate these values from chains.  
- **Fix**: Include script to compute posterior summaries from DESI DR2 w₀wₐ chains.  

**P1B-M2**  
- **Section**: IV, Abstract  
- **Issue**: NaMaster recovery value β̂ = 0.238° (bias 0.032°) for β = 0.27° injection lacks reproducibility driver. Directory `pipelines/h200_results/pod1_namaster_umap_2026-04-29/` not verified to produce this number.  
- **Fix**: Add script in repository that runs the 500 MC realizations and outputs β̂ and bias.  

**P1B-M3**  
- **Section**: VI, Abstract  
- **Issue**: ALP-MCMC results (β_ALP = 0.336° ± 0.107°, β_free = 0.344° ± 0.096°) have no reproducibility script. Sec. VI cites "3 configurations" but no code to regenerate.  
- **Fix**: Provide script to run ALP-MCMC and output posterior values.  

**P1B-M4**  
- **Section**: V.B, VII  
- **Issue**: Version-history language ("queued for v1B.0.15+", "v1B.0.17+ will fold") in body prose.  
- **Fix**: Remove all version-specific planning statements (e.g., "queued for vX.Y.Z+").  

**P1B-M5**  
- **Section**: Abstract, IV  
- **Issue**: Significance range "2.4–2.9σ" for Planck/ACT DR6 contradicts cited sources: [2] reports 3.6σ (β = 0.342° ± 0.094°), [3] reports 2.9σ. "2.4σ" is unsourced.  
- **Fix**: Correct to "2.9–3.6σ" and cite sources for bounds, or remove "2.4–2.9σ".  

---

### MINOR Revisions  
**P1B-m1**  
- **Section**: III, footnote 1  
- **Issue**: Version-history reference ("earlier draft footnote... was an arithmetic error").  
- **Fix**: Remove all references to prior drafts/errors.  

**P1B-m2**  
- **Section**: VI  
- **Issue**: Abstract reports bias 0.032° for β = 0.27° injection but omits 0.040° bias for β = 0.342° injection (Sec. VI), creating inconsistency.  
- **Fix**: Clarify in Abstract: "bias 0.032° for β = 0.27° injection; bias scales to 0.040° at β = 0.342°."  

**P1B-m3**  
- **Section**: III, Table I  
- **Issue**: Burn-in arithmetic (176,240 × 0.7 ≈ 123,368) is manually calculated, not scripted.  
- **Fix**: Add script snippet to compute burn-in samples in reproducibility docs.  

**P1B-m4**  
- **Section**: Throughout  
- **Issue**: Overuse of "spectator-ALP" (7× in Abstract, 12× in body) without abbreviation.  
- **Fix**: Define "ALP" at first use and use consistently.  

---

### NIT Revisions  
**P1B-N1**  
- **Section**: II, IV  
- **Issue**: Redundant phrasing: "Planck Commander CMB polarization map" (Abstract) vs. "Planck Commander map" (IV).  
- **Fix**: Standardize to "Planck Commander polarization map".  

**P1B-N2**  
- **Section**: I, VI  
- **Issue**: "ECH spin-torsion" vs. "ECH framework".  
- **Fix**: Use "ECH" after first full definition.  

---

## Summary Recommendation  
**MAJOR REVISIONS**  

The paper presents valuable technical verification for the ECH program but requires substantial revisions to meet reproducibility standards. Key issues include: (1) absence of scripts to regenerate load-bearing scalars (∆Nₑff, H₀, β̂, w₀/wₐ) from chains/data, (2) internal versioning/audit artifacts in body prose, (3) insufficient qualification of discordant σ scales (pipeline SNR vs. sky significance), and (4) unsourced numerical discrepancies (2.4σ claim). The 12-page length is acceptable given the focused scope, but reproducibility infrastructure must be completed. Acceptance hinges on providing executable code for all reported numbers and eliminating non-scientific artifacts.