# P3 2026-06-04_R4fixed — Confabulation-hunter referee (reasoning mode)

**Model**: `deepseek/deepseek-r1-0528`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 126.3s

---

## Referee Report for P3

### ESSENTIAL Findings
None

### MAJOR Findings
None

### MINOR Findings
**P3-M1: Excessive paper length**  
- Section: Entire paper (49 pages)  
- Problem: Paper length (49 pages) exceeds PRD typical range (15-30pp) for methods/catalog papers without commensurate novel methodological complexity.  
- Fix: Reduce to 30pp by moving technical details (e.g., injection-recovery curves, UMAP/HDBSCAN parameters) to appendices or supplementary material.  

**P3-M2: Ambiguous "catalog-grade" approximation**  
- Section: Abstract (p1) and §IV.C (p20)  
- Problem: Abstract cites "~265,000" catalog-grade and "~113,000" exploratory objects without quantifying uncertainty or cross-survey overlap error. Text states split is "approximate" but does not specify tolerance (e.g., ±X%).  
- Fix: Explicitly state uncertainty (e.g., "±5,000") and add footnote: "Exact partition depends on deduplication geometry; see `pathc_multi_survey_matches.parquet`."  

**P3-M3: SIMBAD-unmatched vs. genuine novelty conflation risk**  
- Section: §IV.A (p18-19) and Conclusions (p31)  
- Problem: Headline "58.8% SIMBAD-unmatched" (Fig 9) is highlighted without equal prominence to the true novelty fraction ("17.8%"). This could mislead readers into overstating discovery rates.  
- Fix: In Abstract and Conclusions, add: "NOTE: SIMBAD-unmatched fraction (58.8%) overstates true novelty; extended archival matching confirms 17.8% genuine novelty in DESI top-1,000."  

### NIT Findings  
**P3-N1: Incomplete Table I ACT exclusion note**  
- Section: Table I (p15)  
- Problem: Table header "Path-C unique∥ (primary)" implies ACT exclusion but does not explicitly quantify the subtraction (200 patches).  
- Fix: Revise header to: "Path-C unique (primary, ACT-excluded)" and add footnote: "Excluding ACT DR6 removes 200 patches; cross-transfer baseline included ACT for comparison only."  

**P3-N2: Fisher linear approximation retention**  
- Section: §V (p22) and §VI.D(i) (p27)  
- Problem: The invalid linear approximation σ(f_NL) ≈ 8.98 - 3.66α is retained post-superseding for "reference," creating redundancy.  
- Fix: Remove linear approximation values; state: "Local-linear approximation invalid at α=0; superseded by positivity-respecting envelope."  

**P3-N3: Redundant "before/after" emphasis**  
- Section: §II.D (p8) and Table I footnotes  
- Problem: 4 instances of "preserved as before/after diagnostic" distract from primary Path-C results.  
- Fix: Reduce to single definitive statement: "Cross-transfer counts preserved for methodological comparison only; superseded by Path-C native counts."  

**P3-N4: Duplicate phrase "gate PASS"**  
- Section: §III.F (p17)  
- Problem: Repetitive phrasing: "criterion (a) PASS" / "criterion (b) PASS" / "gate PASS" in Planck CMB description.  
- Fix: Replace with: "Planck native retrain satisfied criterion (b)" and remove "gate PASS."  

**P3-N5: Inconsistent anomaly score notation**  
- Section: Fig 5 caption (p12) and Table III (p17)  
- Problem: Fig 5 labels Z-arm sub-score as "AE" (legacy term), while Table III uses "S_BigAE" without explicit linkage to Eq 2.  
- Fix: Standardize to "r_Z" (sub-score) and "S" (canonical score) per Eq 2; add notation key to Fig 5 caption.  

---

## Summary recommendation  
**ACCEPT WITH MINOR CORRECTIONS**  

Justification: The paper presents a rigorous, large-scale multi-survey anomaly catalog with significant methodological advances (e.g., Path-C rebuild, cross-validation). Load-bearing scalars (378,280 anomalies, 17.8% novelty fraction) are traceable via reproducibility scripts, and arithmetic consistency is verified. Cosmological applications are appropriately qualified. Minor revisions are required to: (1) reduce length to journal standards, (2) clarify approximation uncertainties in catalog partitions, (3) prevent misinterpretation of SIMBAD-unmatched rates, and (4) remove redundant/ambiguous phrasing. No essential confabulations or irreproducible results were found.