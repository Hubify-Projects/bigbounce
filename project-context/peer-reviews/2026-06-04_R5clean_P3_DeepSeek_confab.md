# P3 2026-06-04_R5clean — Confabulation-hunter referee (reasoning mode)

**Model**: `deepseek/deepseek-r1-0528`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 229.9s

---

## Referee Report: Paper P3

### ESSENTIAL Revisions

- **P3-E1: Abstract & §II D, page 2 (Table I)**  
  **Problem:** Cross-transfer baseline total of 319,443 anomalies (Table I) is inconsistent with the sum of per-survey counts (195,829 + 77,905 + 44,075 + 298 + 200 + 500 + 436 = 319,243). The discrepancy of 200 anomalies is resolved only by an implicit inclusion of ACT DR6 (quarantined), which is not listed in the per-survey block. This violates reproducibility standards.  
  **Fix:** Explicitly list ACT DR6 in Table I as a quarantined survey with 200 anomalies, or adjust the total to 319,243 and clarify that ACT is excluded from all aggregates. Provide a script that sums the per-survey counts to the headline total.

- **P3-E2: Abstract & §IV A, page 4**  
  **Problem:** The genuine novelty fraction (17.8% for DESI top-1,000) lacks provenance. The 20 catalogs used for cross-matching are not enumerated, and no script/dataset is referenced to reproduce this number. The claim "genuine novelty fraction" is unsupported without accessible cross-matching code.  
  **Fix:** List all 20 catalogs in a table or appendix and release the cross-matching script (e.g., CDS X-Match parameters) as part of the reproducibility package.

- **P3-E3: §V, pages 3–4**  
  **Problem:** The σ(f<sub>NL</sub>) forecasts (central σ(f<sub>NL</sub>) = 8.14, linear approximation σ(f<sub>NL</sub>) = 8.27 ± 2.37) are presented without scripts for the Landy-Szalay α measurement or Fisher pipeline. The jackknife covariance and Fisher mapping (1/σ(f<sub>NL</sub>)<sup>2</sup> = F<sub>0</sub> + cα<sup>2</sup>) are not reproducible.  
  **Fix:** Release scripts for the angular two-point analysis, jackknife realizations, and Fisher pipeline. Provide input files (e.g., randoms, bias ratios) and document all equations in a reproducibility notebook.

- **P3-E4: Header & §II D, page 1**  
  **Problem:** Version-control artifacts ("ROUND: 2026-06-04_R5clean", "CHANGES SINCE LAST ROUND: R5: all load-bearing queued in-flight language stripped") appear in the body. These are internal workflow tags inappropriate for publication.  
  **Fix:** Remove all version-history language (e.g., "R5", "in-flight") from the paper body and header. Retain only scientific content.

---

### MAJOR Revisions

- **P3-M1: Entire paper**  
  **Problem:** Paper length (49 pages) exceeds PRD standards for methods/catalog papers (15–30 pp). The cosmological applications (§V) and appendices are disproportionately long relative to the core catalog description.  
  **Fix:** Condense to ≤30 pages by:  
  (1) Moving non-essential content (e.g., Appendix E PTA details, §VI D caveat catalog) to a supplement or technical note.  
  (2) Removing redundant text (e.g., duplicate tier-stratification explanations in Abstract/§III).  
  (3) Streamlining cosmological forecasts (§V) to focus on catalog-derived results.

- **P3-M2: Abstract & §III, pages 1–2**  
  **Problem:** The decomposition of the point-source tier into "catalog-grade" (∼265,000) and "LAMOST exploratory" (∼113,000) objects is ambiguous. The sum (∼378,000) matches the point-source tier (378,080), but the paper states this split is approximate and file-dependent, yet no script is provided to extract exact counts from "pathc_multi_survey_matches.parquet".  
  **Fix:** Release a script that outputs the exact catalog-grade/LAMOST split from the parquet file. Clarify in the abstract that these are approximate figures pending user-defined thresholds.

- **P3-M3: §II D & Table I, page 2**  
  **Problem:** Cross-validation stability metrics for Gaia (41.0%) and eROSITA (81.5%) are cited as diagnostics but lack reproducible methods. The IsolationForest implementation (nest=100, contamination=0.01) and reshuffling protocol are not scripted.  
  **Fix:** Release scripts for the IsolationForest cross-validation, including random-seed management and thresholding logic. Document these in the reproducibility package.

---

### MINOR Revisions

- **P3-M4: §IV A, page 4**  
  **Problem:** The SIMBAD-unmatched fraction (58.8%) is misrepresented as a "genuine novelty" metric in the abstract, while §IV A clarifies it is a database-coverage diagnostic (true novelty is 17.8%). This risks misinterpretation.  
  **Fix:** Replace "genuine novelty fractions" in the abstract with "SIMBAD-unmatched fractions" and add a footnote clarifying that true novelty requires extended cross-matching (§IV A).

- **P3-M5: §V, page 3**  
  **Problem:** The high-confidence subset σ(f<sub>NL</sub>) forecast (σ(f<sub>NL</sub>)<sub>GS</sub> = 1.95) uses an undefined "Gold+Silver" sample. The selection criteria (e.g., "P > 0.9 candidate-confidence cuts") are not reproducible.  
  **Fix:** Define the Gold+Silver sample in a table or appendix and release the selection script.

- **P3-M6: §II B, page 2**  
  **Problem:** The anomaly score thresholding policy varies by survey (absolute S > 5 for DESI/SDSS vs. top-1% for LAMOST/Gaia). This is justified but buried in Table I footnotes.  
  **Fix:** Summarize threshold policies in a central table or §II B subsection for clarity.

---

### NIT Revisions

- **P3-N1: Abstract & §I, page 1**  
  **Problem:** The phrase "Path-C native-retrain" is overused (6 times in abstract) and sounds internal.  
  **Fix:** Replace with "per-survey retraining" after first use and define "Path-C" once in §II D.

- **P3-N2: §III, pages 2–3**  
  **Problem:** Figure 5 labels "AE" scores inconsistently (Z-arm sub-score vs. total S). This caused confusion in the referee's initial read.  
  **Fix:** Standardize labels to "r<sub>Z</sub>" for Z-arm scores and "S" for total scores in all figures.

- **P3-N3: §VI D, page 5**  
  **Problem:** The term "gate PASS/FAIL" is colloquial.  
  **Fix:** Replace with "meets/fails validation criteria" in §II D and §VI D.

---

## Summary recommendation  
MAJOR REVISIONS  

**Justification:** The catalog (378,280 anomalies) is a significant contribution to anomaly detection in multi-survey astrophysics. However, the paper cannot be accepted in its current state due to critical reproducibility gaps (E1–E4), excessive length (M1), and ambiguous decompositions (M2). The core issue is insufficient traceability: key numbers (novelty fraction, α measurement, catalog splits) lack scripts/datasets for independent verification. Cosmological forecasts (§V) are compelling but rely on unreproducible inputs. Major revisions must address provenance, reduce length to ≤30 pp, and clarify tier stratifications. Essential fixes to Table I and version-history language are non-negotiable. With these revisions, the paper will meet PRD standards.