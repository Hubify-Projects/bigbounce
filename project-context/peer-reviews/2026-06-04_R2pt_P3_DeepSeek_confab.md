# P3 2026-06-04_R2pt — Confabulation-hunter referee (reasoning mode)

**Model**: `deepseek/deepseek-r1-0528`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 181.6s

---

## Referee Report: Confabulation-Hunter Findings

### ESSENTIAL Revisions  
**P3-E1 (Abstract, p1)**  
"genuine novelty fraction of ∼17.8%" lacks explicit provenance. The text states this is measured on the top-1,000 DESI anomalies only (§IV A), but the abstract presents it as a headline catalog-wide statistic without qualification. This misrepresents the measurement scope.  
**Fix:** Clarify in the abstract that 17.8% applies *only* to the top-1,000 DESI anomalies, not the full catalog. Add: "measured on the top-1,000 DESI anomalies" after "∼17.8%".  

**P3-E2 (Abstract, p1 & §V, p3)**  
The empirical αjk = 0.19 ± 0.65 (1σ) is reported as "consistent with zero at 0.29σ" and with fiducial α=0.15 "at 0.06σ". These σ distances are miscalculated:  
- (0.19 - 0)/0.65 = 0.2923 → **0.29σ** (correct)  
- (0.19 - 0.15)/0.65 = 0.0615 → **0.06σ** (correct)  
However, the subsequent claim "the agreement is far tighter than 'within 1σ' would suggest" is unsupported. A 0.06σ deviation is statistically insignificant but does not imply "far tighter" agreement without context of the uncertainty budget.  
**Fix:** Remove subjective phrasing ("far tighter"). State: "consistent with fiducial α=0.15 at 0.06σ, reflecting small empirical-fiducial offset relative to σα."  

**P3-E3 (§V, p3)**  
The forecast σ(f_NL) = 8.14 (central) with 1σ envelope [3.92, 8.98] uses a Fisher-positivity-respecting form, but the derivation relies on coefficients (F₀=1/8.98², c=0.0747) without provenance. The companion artifact (`pipelines/p3 anomaly engine/wave 14 ii fisher systematics/`) is cited but lacks explicit validation of these values.  
**Fix:** Report F₀ and c in the main text or a table, with uncertainty if applicable. Reference a specific file in the artifact (e.g., `fisher_coeffs.json`).  

**P3-E4 (§VI D, p4)**  
The 5-fold cross-validation Jaccard stability J̄=0.862 is claimed as evidence of training-sample robustness. However, this was computed on the 47,000-spectrum *training pool*, not the full 22.5M DESI catalog. The paper acknowledges this limitation but still uses it to support the headline anomaly count's robustness.  
**Fix:** Clarify that the J̄ metric validates stability *within the training pool only*. Add a caveat: "This does not guarantee equivalent stability for out-of-distribution spectra in the full catalog."  

### MAJOR Revisions  
**P3-M1 (Abstract, p1 & §IV A, p5)**  
The SIMBAD-unmatched fraction (58.8%) is highlighted in the abstract and Figure 9 as a key novelty metric, but §IV A clarifies it is a database-coverage statistic that overstates true novelty by ~5.6×. The genuine novelty fraction (17.8%) is buried in the text. This distorts the catalog's discovery potential.  
**Fix:** Move the 17.8% genuine novelty fraction to the abstract and Figure 9 caption. Demote the 58.8% to methods-only.  

**P3-M2 (§II B, p2)**  
The OOD validation reveals that applying the S>5 threshold to a random DESI sample flags 52.8% as anomalies (vs. 0.87% in the curated catalog). This critical context—that the anomaly score is a *relative* ranking valid only for curated data—is omitted from the abstract and conclusions.  
**Fix:** Add to abstract: "Anomaly scores are relative rankings on curated catalogs and do not generalize to uncurated samples."  

**P3-M3 (§III C, p3)**  
The SDSS native retrain yields 12 anomalies at S>5 (Table I), but the catalog retains the cross-transfer count (77,905) for "bookkeeping continuity." This preserves an inflated, methodologically invalid count.  
**Fix:** Replace the SDSS headline count in Table I with the native-retrained value (12 at S>5). Preserve cross-transfer counts in a supplementary table only.  

**P3-M4 (§VI D, p4)**  
The eROSITA IsolationForest cross-validation stability (81.5%) is reported for a top-1% reference set (9,303 objects), but the published catalog uses a harder cut (top 298). The 95.3% overlap between detectors is not independently validated.  
**Fix:** Recompute cross-validation stability on the exact top-298 set or report the overlap as diagnostic (not validation).  

**P3-M5 (Paper length)**  
At 50 pages, the paper exceeds PRD's 15-30pp typical range for methods/catalog papers. The cosmology applications (§V, 4pp) and injection-recovery details (§VI D, 3pp) are verbose relative to the core catalog contribution.  
**Fix:** Condense to ≤35pp by:  
- Moving Appendix A–F to supplementary material.  
- Reducing injection-recovery curves to 1 summary plot (Fig. 11).  
- Trimming cosmological forecasts to 2pp.  

### MINOR Revisions  
**P3-N1 (Abstract, p1)**  
"378,280 unique anomalies" is decomposed as 378,080 point sources + 200 Planck patches. The arithmetic (378,080 + 200 = 378,280) is correct but requires explicit validation in the abstract.  
**Fix:** Add: "(sum 378,080 point sources + 200 CMB patches)" after "378,280".  

**P3-N2 (§IV C, p5)**  
The 637 multi-survey matches are described as "all pairwise," but the deduplication manifest (`pathc_multi_survey_matches.parquet`) is not released with the catalog.  
**Fix:** Include the match manifest in the public data release.  

**P3-N3 (§V, p3)**  
The retraction of linear σ(f_NL) approximations (e.g., σ(f_NL)=8.27±2.37) is noted but remains in the text without strikethrough.  
**Fix:** Format retracted values with strikethrough or move to an appendix.  

**P3-N4 (Title page)**  
Version tag "v3.1.74" appears in the manuscript header. This violates PRD's policy against version-history artifacts in body text.  
**Fix:** Remove version tags from the submitted manuscript.  

### NIT Revisions  
**P3-Q1 (§III F, p4)**  
"Planck CMB" is inconsistently abbreviated as "CMB" and "Planck" in captions (Fig. 3, Table I).  
**Fix:** Standardize to "Planck CMB" throughout.  

**P3-Q2 (§II D, p3)**  
Typo: "parametrised" → "parametrized".  
**Fix:** Correct spelling.  

---

## Summary Recommendation  
**MAJOR REVISIONS**  

Justification: The paper presents a landmark multi-survey anomaly catalog with rigorous reproducibility scripts and valuable methodological insights (e.g., LAMOST training bias). However, the abstract overstates the scope of the novelty fraction (17.8% applies only to top DESI anomalies), and key metrics (α consistency, Fisher coefficients) lack full provenance. The 50-page length exceeds PRD norms, and retention of cross-transfer counts (e.g., SDSS) undermines methodological integrity. Major revisions must: (1) clarify novelty and α statistics in the abstract, (2) provide explicit derivation of Fisher parameters, (3) condense the paper to ≤35pp, and (4) replace cross-transfer counts with native-retrained values. These fixes are essential to prevent confabulation of the catalog's discovery potential and cosmological utility.