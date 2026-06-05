# P3 2026-06-04_R3clean — Confabulation-hunter referee (reasoning mode)

**Model**: `deepseek/deepseek-r1-0528`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 225.3s

---

## Referee Report for Paper P3  

### ESSENTIAL Revisions  
**P3-E1: Abstract & Section IV.A (p.19)**: Genuine novelty fraction misrepresented.  
- **Problem**: The abstract states "a genuine novelty fraction of ∼17.8% (objects absent from all major catalogs)", but Section IV.A clarifies this is a single-sample estimate for the DESI *top-1,000* anomalies only. The paper explicitly notes the full-catalog rate is untested and the converse hypothesis (higher novelty at lower scores) is plausible.  
- **Fix**: Revise abstract to: "∼17.8% (measured for the top-1,000 DESI anomalies only; full-catalog rate untested)".  

**P3-E2: Section V (p.21)**: σ(f<sub>NL</sub>) values from different procedures presented without qualification.  
- **Problem**: The empirical σ(f<sub>NL</sub>) = 8.14 (central) and [3.92, 8.98] (1σ envelope) from Landy-Szalay are juxtaposed with Fisher-forecast σ(f<sub>NL</sub>) values without clarifying their distinct statistical bases. The envelope crosses the single-tracer floor (σ=8.98), which is non-Gaussian.  
- **Fix**: Add: "Empirical σ(f<sub>NL</sub>) intervals reflect non-Gaussian uncertainty propagation from α; they are not directly comparable to Fisher forecasts."  

**P3-E3: Section VI.D (p.29)**: Version-history language in body prose.  
- **Problem**: "an earlier draft of §VI D (g) flagged this as an internal inconsistency" (artifact of review process).  
- **Fix**: Remove all version-specific references.  

---

### MAJOR Revisions  
**P3-M1: Table I & Section IV.A (p.19)**: Inconsistent SIMBAD-unmatched aggregation.  
- **Problem**: Aggregate SIMBAD-unmatched rate (58.8%) weights DESI at 99% (top 10k only) but uses full DESI anomaly count (195,829) in the denominator. This conflates coverage for top-10k with the full sample.  
- **Fix**: Recompute aggregate using only the DESI top-10k subset OR disclose: "DESI rate based on top 10k; aggregate assumes same fraction for full sample."  

**P3-M2: Abstract & Section IV.C (p.20)**: ~265,000 catalog-grade objects lacks traceability.  
- **Problem**: The abstract cites "~265,000 unique objects" as the catalog-grade subset (DESI+SDSS+eROSITA+Gaia+NEOWISE), but this is derived from 378,080 (point-source tier) minus ~113,000 (LAMOST). The exact value depends on deduplication geometry, yet no script/JSON derives 265,000.  
- **Fix**: Provide a script in the release (`pipelines/p3_deduplication/split_catalog_grade.py`) that outputs the exact count from `pathc_multi_survey_matches.parquet`.  

**P3-M3: Section V (p.21)**: Unqualified central σ(f<sub>NL</sub>) = 8.14.  
- **Problem**: The central σ(f<sub>NL</sub>) = 8.14 (from α=0.19) is reported without emphasizing that α=0.19±0.65 is consistent with *zero* (0.29σ), making the "improvement" statistically insignificant.  
- **Fix**: State: "Central σ(f<sub>NL</sub>) = 8.14 assumes α=0.19, but α=0 is within 0.29σ; thus, no significant improvement is yet confirmed."  

**P3-M4: Throughout**: Excessive length (50pp vs. PRD standard 15-30pp).  
- **Problem**: Paper is 50 pages (excluding appendices), exceeding PRD norms for methods/catalog papers. Cosmological applications (§V, 4pp) and appendices (14pp) could be condensed.  
- **Fix**: Shorten to ≤30pp by:  
  - Moving injection-recovery details (Fig. 11) to supplement.  
  - Condensing Appendix D (image galleries) to 2pp with representative panels only.  
  - Cutting redundant methodology descriptions (e.g., §II.C).  

**P3-M5: Section IV.A (p.19)**: Overstated novelty implications.  
- **Problem**: The 17.8% novelty fraction for DESI top-1,000 is presented as a headline result, but the paper notes it may not represent the full catalog (and could be higher/lower). The abstract does not emphasize this limitation.  
- **Fix**: Add to abstract: "This fraction is measured for high-scoring anomalies only; the full-catalog rate is unconstrained."  

---

### MINOR Revisions  
**P3-m1: Table I**: Footnotes obscure critical thresholds.  
- **Problem**: Footnotes ♡ and ♠ define per-survey thresholds (e.g., SDSS uses top-1% at S≥0.1060, not S>5), but this is buried.  
- **Fix**: Add a column "Threshold" to Table I listing criteria (e.g., "S>5", "Top-1%").  

**P3-m2: Section II.B (p.5)**: Incomplete OOD validation disclosure.  
- **Problem**: The out-of-distribution (OOD) test uses 100k DESI spectra, but no script is cited for the MSE distribution (median=0.178, p99=44.85).  
- **Fix**: Reference companion artifact `r42/results/B10_ood_results_100k.json` in text.  

**P3-m3: Section III.E (p.15)**: eROSITA footprint bias unquantified.  
- **Problem**: Anomalies cluster near LMC due to depth variations, but no correction is applied.  
- **Fix**: Add: "Spatial clustering correlates with exposure depth; future work will weight by exposure time."  

**P3-m4: Abstract**: "Load-bearing" is informal.  
- **Problem**: The term "load-bearing scalar" is colloquial.  
- **Fix**: Replace with "primary" or "key".  

---

### NITPICKS  
**P3-N1: Section III.C (p.12)**: "Canonical" overused.  
- **Problem**: "Canonical" appears 32 times (e.g., "canonical score", "canonical dedup").  
- **Fix**: Replace with "standard" or "primary" where possible.  

**P3-N2: Figure 5**: Axis labels ambiguous.  
- **Problem**: Panels list "AE" (Z-arm sub-score) without clarifying it is not the total anomaly score S.  
- **Fix**: Label axes: "Z-arm sub-score (r<sub>Z</sub>)" and add: "Not total anomaly score S."  

**P3-N3: Section VII (p.32)**: Repetitive conclusion.  
- **Problem**: Conclusions (§VII) restate results verbatim from §III–V.  
- **Fix**: Condense to 1pp highlighting implications only.  

---

## Summary Recommendation  
**MAJOR REVISIONS**  

Justification: The paper presents a landmark multi-survey anomaly catalog (378,280 objects) with rigorous validation and cosmological applications. However, it requires major revisions to address: (1) statistical misrepresentations (e.g., novelty fraction scope, σ(f<sub>NL</sub>) qualification), (2) traceability gaps in key numbers (e.g., 265,000 catalog-grade objects), (3) version-history artifacts, and (4) length (50pp vs. PRD 15-30pp standard). The core methodology and catalog construction are sound, but the presentation must be tightened, inconsistencies resolved, and claims tempered to reflect empirical uncertainties (e.g., α=0.19±0.65). Upon revision, this will be a high-impact contribution.