# P3 2026-06-04_1814pt — Confabulation-hunter referee (reasoning mode)

**Model**: `deepseek/deepseek-r1-0528`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 331.8s

---

## Referee Report for Paper P3

### ESSENTIAL Revisions

- **P3-E1**: Version-history artifacts in body prose  
  - **Section**: Throughout (e.g., Abstract: "v3.1.73"; II B: "R15 GEM-B1 closure", "v3.1.68 closure"; V: "v3.1.46", "v3.1.70"; VI D: "v3.1.67")  
  - **Problem**: Internal version tags (e.g., "v3.1.73", "R15 GEM-B1 closure") and review-log artifacts appear in the body text. These are not appropriate for publication and undermine the paper's professionalism.  
  - **Fix**: Remove all versioning tags, closure notes, and internal audit references (e.g., "v3.1.73" → ""; "R15 GEM-B1 closure" → "we revised").  

- **P3-E2**: Misleading novelty fraction in abstract  
  - **Section**: Abstract (page 1)  
  - **Problem**: The abstract claims a "genuine novelty fraction of ∼17.8%" without clarifying this is measured *only* on the top 1,000 DESI anomalies, not the full catalog. The paper explicitly states the full-catalog rate is "empirically untested" (Abstract, page 1) and could be higher or lower.  
  - **Fix**: Revise to: "a genuine novelty fraction of ∼17.8% *for the top 1,000 DESI anomalies* (full catalog untested)".  

- **P3-E3**: Unqualified σ values from different procedures  
  - **Section**: V (Cosmological Applications, pages 3–4)  
  - **Problem**: The jackknife σ for α (α = 0.19 ± 0.65) and the Fisher-derived σ(f_NL) envelope [3.92, 8.98] are presented together without clarifying they originate from distinct statistical procedures (angular clustering vs. Fisher matrix). This risks conflating uncertainties from fundamentally different methods.  
  - **Fix**: Explicitly state: "The 1σ envelope for σ(f_NL) is derived from propagating the jackknife uncertainty in α through the Fisher-positivity-respecting model, not from direct measurement."  

- **P3-E4**: Inconsistent deduplication arithmetic  
  - **Section**: IV C (page 8) and II D (page 6)  
  - **Problem**: The paper states the 378,280 headline arises from 388,493 survey detections minus 10,213 duplicates (637 multi-survey + 9,576 intra-survey). However, 388,493 - 378,280 = 10,213 is inconsistent: 388,493 - 378,280 = 10,213, but 637 + 9,576 = 10,213. **Resolution**: Arithmetic is correct as per VI D (a), but the contradiction with earlier deferrals (e.g., "pending union-find recompute") must be resolved.  
  - **Fix**: Remove references to deferred recalculations; state the final deduplication counts confidently.  

### MAJOR Revisions

- **P3-M1**: Paper exceeds recommended length  
  - **Section**: Entire paper (50 pages)  
  - **Problem**: At 50 pages, the paper exceeds PRD's typical 15–30 pp range for methods/catalog papers. The catalog description is verbose, with redundant methodological asides (e.g., VI D caveats).  
  - **Fix**: Condense to ≤30 pp by:  
    (a) Moving technical caveats (VI D) to an appendix.  
    (b) Removing duplicated content (e.g., cross-validation in II B and VI D).  
    (c) Streamlining survey-by-survey results (Section III).  

- **P3-M2**: Untraceable "0.87%" DESI anomaly rate  
  - **Section**: Abstract, II B (page 2), Table I  
  - **Problem**: The 0.87% DESI anomaly rate (195,829 / 22.5M) relies on a curated catalog and fixed S > 5 threshold. The OOD validation shows this threshold would flag >50% of a random sample, confirming the rate is not intrinsic. The paper acknowledges this but still presents 0.87% as a headline figure.  
  - **Fix**: Reposition 0.87% as a catalog-specific metric (not universal). Add: "This rate reflects DESI DR1's spectroscopic curation; absolute thresholds require per-survey calibration."  

- **P3-M3**: Unvalidated LAMOST anomaly set  
  - **Section**: III D (page 5), Table I  
  - **Problem**: The LAMOST native retrain reduces anomalies from 44,075 to 113,342 but retains a 98% blue-excess bias (Fig. 7). The paper labels this a "methodological lesson" but still includes these anomalies in the headline catalog (378,280) without sufficient validation.  
  - **Fix**: Remove LAMOST anomalies from the "catalog-grade" subset or add bold caveats: "LAMOST anomalies exhibit instrumental bias and should not be used for science without reclassification."  

### MINOR Revisions

- **P3-m1**: Confusing eROSITA threshold disclosure  
  - **Section**: Table I footnote, III E (page 6)  
  - **Problem**: eROSITA's threshold (S > 0.259) is buried in a footnote and Section III E, while other surveys have thresholds in Table I's main body.  
  - **Fix**: Move eROSITA's threshold to Table I's "Threshold" column for consistency.  

- **P3-m2**: Undefined "Path-C" in abstract  
  - **Section**: Abstract (page 1)  
  - **Problem**: "Path-C" is used in the abstract without definition, assuming familiarity with the methodology section.  
  - **Fix**: Add: "using a rebuild protocol (Path-C) with per-survey native retraining."  

- **P3-m3**: Duplicate cross-validation description  
  - **Section**: II B (page 2) and VI D (i) (page 10)  
  - **Problem**: The 5-fold cross-validation (J̄ = 0.862) is described verbatim in II B and VI D.  
  - **Fix**: Describe once in II B; reference it in VI D.  

### NITPICKS

- **P3-n1**: Inconsistent total source count  
  - **Section**: Abstract ("37.3 million") vs. Table I (37,272,042)  
  - **Problem**: Abstract rounds 37,272,042 to "37.3 million," but Table I uses exact figures.  
  - **Fix**: Use "37.3 million" consistently or add "≈" in Table I.  

- **P3-n2**: Redundant "canonical" usage  
  - **Section**: Throughout (e.g., "canonical anomaly score," "canonical unique-anomaly count")  
  - **Problem**: Overuse of "canonical" is repetitive and unnecessary.  
  - **Fix**: Replace with "defined" or "standardized" where possible.  

---

## Summary Recommendation  
**MAJOR REVISIONS**  

The paper presents a valuable multi-survey anomaly catalog (378,280 objects) with rigorous validation protocols. However, it requires major revisions due to:  
1. **Excessive length** (50 pp vs. PRD's 15–30 pp standard),  
2. **Version-control artifacts** in prose (e.g., "v3.1.73"),  
3. **Inadequate traceability** for key numbers (e.g., 0.87% DESI rate depends on curation),  
4. **Unqualified uncertainty propagation** (σ values from jackknife/Fisher mixed without clarification).  
Addressing ESSENTIAL fixes (versioning, novelty fraction scope, σ qualifications) and condensing the paper are critical for acceptance. The catalog itself is robust, but the presentation must align with PRD's standards for reproducibility and conciseness.