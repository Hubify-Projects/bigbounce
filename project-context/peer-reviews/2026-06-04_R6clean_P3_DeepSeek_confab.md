# P3 2026-06-04_R6clean — Confabulation-hunter referee (reasoning mode)

**Model**: `deepseek/deepseek-r1-0528`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 116.5s

---

## Referee Report: Confabulation-Hunter Review

### ESSENTIAL Revisions

**P3-E1: Abstract provenance for headline anomaly count**  
- **Section**: Abstract, page 1  
- **Problem**: The headline figure "378,280 unique anomalies" lacks explicit provenance. The abstract states this is the sum of "378,080 point-source object detections" and "200 Planck CMB map patches," but no script/JSON is cited to reproduce this decomposition from raw data.  
- **Fix**: Provide a reproducibility script in the companion repository that generates the 378,280 count from per-survey native-retrain outputs and 7-way deduplication (as described in §II D). Explicitly cite this script in the abstract or methods.

**P3-E2: σ(f_NL) forecast without qualification of error sources**  
- **Section**: V (Cosmological Applications), pages 22–23  
- **Problem**: The central forecast σ(f_NL) = 8.14 (with envelope [3.92, 8.98]) combines the empirical α = 0.19 ± 0.65 (jackknife error from angular clustering) with a Fisher pipeline assuming zero systematics. These σ values are from distinct procedures (observational vs. theoretical) but are presented as a unified constraint without qualifying their methodological differences.  
- **Fix**: Add explicit caveats: (1) The jackknife σ_α is statistical only; (2) The Fisher σ(f_NL) does not marginalize over fiber-assignment, photo-z, or foreground systematics; (3) State that the envelope reflects α uncertainty propagated through the Fisher model, not a total error budget.

**P3-E3: Version-history artifacts in body text**  
- **Section**: III E (eROSITA DR1), page 17  
- **Problem**: Text references earlier drafts ("Earlier draft tables of this paper that quoted only the IF raw score [...] were ambiguous") – this is a review-log artifact.  
- **Fix**: Remove all version-history language (e.g., "earlier draft tables," "prior version"). Present the final methodology without self-referential revisions.

**P3-E4: Novelty fraction caveat missing in abstract**  
- **Section**: Abstract, page 1  
- **Problem**: The abstract states a "genuine novelty fraction of ∼17.8%" without qualifying that this is a point estimate for the DESI top-1,000 anomalies only. The conclusion (page 3) explicitly notes the full-catalog rate is untested and the converse hypothesis (higher novelty at lower scores) is plausible.  
- **Fix**: Revise the abstract to: "a genuine novelty fraction of ∼17.8% (measured for the top-1,000 DESI anomalies; full-catalog rate untested)."

### MAJOR Revisions

**P3-M1: Inconsistent SIMBAD-unmatched aggregation**  
- **Section**: IV A, page 19; Table I  
- **Problem**: The aggregate SIMBAD-unmatched fraction (58.8%) is claimed as "weighted across all surveys," but the per-survey rates (Gaia 27%, NEOWISE 45%, LAMOST ∼50%, eROSITA 68%, SDSS 90%, DESI 99%) cannot reproduce 58.8% without weights. Weights (e.g., per-survey anomaly counts) are not provided.  
- **Fix**: Provide a table showing: (1) Per-survey anomaly count, (2) SIMBAD-unmatched count, (3) Unmatched fraction. Calculate the aggregate as ∑(unmatched_count)/∑(anomaly_count) and report weights.

**P3-M2: Reproducibility gap for 17.8% novelty fraction**  
- **Section**: IV A, page 19  
- **Problem**: The 17.8% novelty fraction (178/1,000 DESI top anomalies unmatched across 20 catalogs) lacks a script to reproduce the cross-match. The catalog list is not in the paper (only noted as "20 curated all-sky catalogs via CDS X-Match").  
- **Fix**: Provide a script in the companion repository that: (1) Lists the 20 catalogs, (2) Performs the cross-match at 5" radius, (3) Outputs the 178 unmatched sources. Reference this script in Section IV A.

**P3-M3: Arithmetic inconsistency in point-source tier split**  
- **Section**: Abstract, page 1; Introduction, page 2  
- **Problem**: The "catalog-grade" subset (∼265,000) and "LAMOST exploratory" (∼113,000) sum to ∼378,000, but the point-source tier is 378,080. The ∼2,080 discrepancy is unexplained, and the text calls the split "approximate" without quantifying the uncertainty.  
- **Fix**: Report exact counts from the "released cluster manifest" or provide a footnote with the precise partition (e.g., "265,492 catalog-grade + 112,588 LAMOST exploratory = 378,080").

**P3-M4: Page length exceeds contribution**  
- **Section**: Entire paper  
- **Problem**: At 49 pages, the paper is excessively long for a catalog descriptor. The survey-by-survey details (§III, 11 pages) could be condensed, and cosmological applications (§V, 4 pages) are speculative (α consistent with 0; f_NL forecast uncertain).  
- **Fix**: Condense §III to 5 pages (move technical details to appendices) and §V to 2 pages. Recommended maximum: 30 pages.

### MINOR Revisions

**P3-m1: Duplicate phrase "canonical"**  
- **Section**: II D, page 8; III E, page 17  
- **Problem**: Redundant use of "canonical" for thresholds (e.g., "canonical-S cut," "canonical anomaly score").  
- **Fix**: Replace with precise descriptors (e.g., "standardized-S cut," "primary score axis").

**P3-m2: Ambiguous "z" notation**  
- **Section**: II B, page 5  
- **Problem**: "z-scored" (for anomaly score standardization) risks confusion with redshift "z".  
- **Fix**: Replace "z-scored" with "standardized" or "normalized" in all instances (e.g., Eq. 2: "S(x) ≡ (MSE(x) − μ_val)/σ_val").

**P3-m3: Unvalidated assumption in Fisher forecast**  
- **Section**: V, page 22  
- **Problem**: The Fisher forecast assumes "zero observational systematics," but §V notes systematics (e.g., fiber-assignment incompleteness) could degrade constraints. This caveat is buried.  
- **Fix**: Move the systematics caveat to the Fisher result paragraph: "Forecast assumes no systematics; real constraints may weaken."

### NIT Revisions

**P3-n1: Typo in arithmetic**  
- **Section**: Introduction, page 3  
- **Problem**: "378,080/2,685 = 140.8 ≈ 141" is incorrect (378,080 ÷ 2,685 ≈ 140.82, so ≈141 is fine, but 140.8 is misstated).  
- **Fix**: Correct to "378,080/2,685 ≈ 140.8" or "≈141".

**P3-n2: Incomplete figure reference**  
- **Section**: III B, page 10  
- **Problem**: Fig. 5 references "Appendix D.1" for taxonomy galleries, but the appendix is not in the text.  
- **Fix**: Add Appendix D or cite the companion repository.

---

## Summary Recommendation  
**MAJOR REVISIONS**  

The paper presents a landmark multi-survey anomaly catalog with rigorous methodology (Path-C rebuild, deduplication) and valuable insights (LAMOST training-bias). However, core claims lack full traceability: The headline 378,280 count and 17.8% novelty fraction require reproducible scripts, and the σ(f_NL) forecast conflates statistical errors from different procedures. Version-history artifacts and inconsistent decompositions (e.g., SIMBAD-unmatched rates) undermine reproducibility. Condensing the paper to 30 pages and providing explicit provenance for all headline numbers are essential. With these revisions, the catalog will be a foundational resource.