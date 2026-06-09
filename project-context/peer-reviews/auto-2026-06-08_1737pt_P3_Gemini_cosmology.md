# P3 auto-2026-06-08_1737pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (14702 chars)
**Wall time**: 175.7s

---

## Referee Report on "Spectrally Unusual Sources at Scale..."

This paper presents a large-scale anomaly detection analysis across seven astronomical surveys, resulting in a catalog of 378,280 unique anomalous sources. The work is ambitious and tackles important challenges in modern survey astronomy. It presents several valuable results, including the identification of high-redshift QSO candidates, the discovery of an uncataloged BAL QSO, and important null tests that rule out cosmological signals in CMB map-patch anomalies. The authors are also commendably transparent about methodological failures, such as the initial cross-transfer approach, which provides important lessons for the community.

However, the paper suffers from several major methodological and presentational issues that must be addressed before it can be considered for publication in Physical Review D. The structural integrity of the final catalog is questionable due to the inclusion of large datasets from pipelines that fail the authors' own primary validation criteria. The definition of an "anomaly" is inconsistent across surveys, and the presentation of key results in tables and figures is often confusing, mixing final data with superseded diagnostics.

Below is a detailed list of required revisions.

---

### ESSENTIAL

**P3-E1: Inclusion of Data from Failed Validation Gates**
*   **Section:** III, VI C, Figure 7 (Pages 3, 7, 8, 12, 13)
*   **Problem:** Three of the six point-source surveys (LAMOST, Gaia, eROSITA) which contribute a significant number of objects to the final catalog, fail the primary injection-recovery validation gate (recovery < 50% at 5σ). The paper justifies their inclusion by labeling them "exploratory" or by citing secondary, less rigorous validation metrics (e.g., "XV-stability"). This fundamentally undermines the reliability of a large fraction of the catalog. A catalog presented as a unified scientific product cannot be built upon methods that the authors' own analysis shows are not robust. The headline number of 378,280 is heavily inflated by these unvalidated or poorly validated sources.
*   **Fix:** The authors must choose one of two paths:
    1.  Remove all surveys that fail the primary validation gate from the main, headline catalog. These results can be presented in an appendix as methodological case studies, but they cannot be part of the principal scientific result. The abstract and all headline numbers must be revised accordingly.
    2.  Provide a much stronger, quantitatively-backed argument for why the injection-recovery gate is not the appropriate metric for these specific surveys and why the alternative metrics are sufficient to guarantee catalog purity and completeness. This would require a significant expansion of the validation section. As it stands, the justification is insufficient.

**P3-E2: Inconsistent Anomaly Thresholds**
*   **Section:** II B (Page 2), Table I (Page 6)
*   **Problem:** The paper uses at least four different methods to define the anomaly threshold across the different surveys: an absolute `S > 5.0` cut (DESI), a top-percentile cut (SDSS, LAMOST, Gaia, Planck, NEOWISE), an Isolation Forest score-knee (eROSITA), and a fixed count cap (eROSITA). This makes the term "anomaly" physically inconsistent across the catalog. A source just below the threshold in one survey might be considered highly anomalous in another. This heterogeneity invalidates the interpretation of the total anomaly count and complicates any cross-survey statistical analysis.
*   **Fix:** The authors must apply a single, well-justified thresholding methodology to all surveys to create a homogeneous catalog. If this is not possible, they must provide a detailed justification for the different choices and add a prominent discussion of the implications and limitations of combining such heterogeneous samples. The current approach is not acceptable for a unified catalog.

**P3-E3: Inappropriate Content (Table IV, Future Dating)**
*   **Section:** Abstract (Page 1), Table IV (Page 14)
*   **Problem:**
    1.  The paper is dated "June 2026". This is unacceptable for a scientific submission.
    2.  Table IV, "Path-C residual caveats," reads like an internal project management checklist, not a formal part of a scientific paper. Listing results or analysis steps as "closed caveats" is inappropriate.
*   **Fix:**
    1.  The date must be corrected to the date of submission.
    2.  Table IV must be removed entirely. Its content, where relevant, should be integrated into the main prose of the discussion or limitations sections.

**P3-E4: Misleading Presentation of Key Results (Table I, Figure 1)**
*   **Section:** Figure 1 (Page 4), Table I (Page 6)
*   **Problem:**
    1.  Table I, the main summary table, is structured around the "before/after" narrative of the methodological rebuild. The main columns present superseded "cross-transfer" counts, while the final, canonical results are relegated to footnotes and a summary row. This is extremely confusing for the reader.
    2.  Figure 1 is titled "Spatial distribution of all 319,443 anomalies," but the caption clarifies this is the "initial cross-transfer anomaly baseline," not the final catalog of 378,280 objects. The title is misleading.
*   **Fix:**
    1.  Table I must be completely redesigned. It should clearly present the final, canonical "Path-C" results for each survey in the main columns (number of sources, anomaly count, rate, etc.). The superseded cross-transfer numbers should be moved to a separate diagnostic table or an appendix if they are essential for the narrative.
    2.  Figure 1 should either be updated to show the final 378,280 anomalies or its title must be changed to "Spatial Distribution of Initial Cross-Transfer Baseline" to avoid ambiguity.

### MAJOR

**P3-M1: Numerical Discrepancy in fNL Forecast**
*   **Section:** V b (Page 11), Abstract (Page 1), Conclusions (Page 14)
*   **Problem:** The paper claims a "7.9% improvement" in the constraint on `fNL` when using the anomaly-selected tracers. The baseline is `σ(fNL)std = 8.98` and the new forecast is `σ(fNL) = 8.14`. The fractional improvement in the standard deviation is `(8.98 - 8.14) / 8.98 = 9.35%`. The source of the 7.9% figure is unclear and appears to be a miscalculation. This error is repeated in the abstract, main text, and conclusions.
*   **Fix:** The authors must re-calculate this value, verify it, and correct it throughout the manuscript. If 7.9% is correct, they must explicitly show the calculation, as it does not follow from the standard definition of fractional improvement.

**P3-M2: Unclear Justification for LAMOST Anomaly Count**
*   **Section:** III D (Page 7), Table I (Page 6)
*   **Problem:** The paper reports that the native retrain for LAMOST "compresses the anomaly rate 21.5x to 2,054 at S > 5". However, the released and analyzed LAMOST anomaly set contains 113,342 objects, corresponding to a much looser threshold of `S ≥ 0.4613`. This set fails injection recovery with only 5.8% efficiency. The rationale for choosing this extremely low threshold and retaining this large, unvalidated set in the "exploratory tier" is not sufficiently justified.
*   **Fix:** Provide a clear and compelling scientific justification for releasing the top-113,342 LAMOST sources instead of the more conservative S>5 sample of 2,054. Explain what scientific value this specific sample is expected to have, given its poor performance in validation tests.

**P3-M3: Ambiguous Jargon and Acronyms**
*   **Section:** Throughout
*   **Problem:** The paper relies heavily on internal jargon like "Path-C," "gate," "PASS/FAIL," and "XV-stability" without clear, upfront definitions. "Path-C" appears to be the name for the final analysis pipeline, but this is only discernible after reading a significant portion of the paper.
*   **Fix:** Define all non-standard terms and acronyms at their first use. Provide a global definition of the "Path-C" protocol in the introduction or the beginning of the method section.

### MINOR

**P3-m1: Contradictory DESI Anomaly Rate**
*   **Section:** IV A (Page 4)
*   **Problem:** The text states, "The headline 195,829 DESI anomaly count is the top-1% score-cut of the full 22.5-M-spectrum scan". However, 195,829 / 22,504,897 is 0.87%. The text later correctly states the "anomaly rate of 0.87%". The initial "top-1%" claim is incorrect.
*   **Fix:** Remove the incorrect "top-1% score-cut" statement.

**P3-m2: Unprofessional Author Contact Information**
*   **Section:** Author block (Page 1)
*   **Problem:** The contact email `houston@hubify.com` appears to be associated with a marketing company, which is unprofessional for a submission to a leading physics journal.
*   **Fix:** The author should provide a standard institutional or personal email address appropriate for academic correspondence.

**P3-m3: Internal Notes in Bibliography**
*   **Section:** References (Page 19)
*   **Problem:** The bibliographic entry for Heinrich et al. [33] contains an internal note: "[publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity]". This is bookkeeping information and should not be in the final manuscript.
*   **Fix:** Remove the internal note and format the citation according to the journal's style guide (either citing the published version or the arXiv preprint).

**P3-m4: Aggressive Downsampling of Spectra**
*   **Section:** II A (Page 2)
*   **Problem:** Spectroscopic data is downsampled by a factor of 16 to 496 bins. This is a very aggressive compression that could erase information from narrow spectral features, which are often a key signature of unusual objects.
*   **Fix:** Add a sentence justifying this choice. For example, discuss the trade-off between resolution and computational cost, or demonstrate that the primary features of interest for anomaly detection are preserved at this resolution.

### NIT

**P3-N1: Confusing Figure 2 Caption**
*   **Section:** Figure 2 (Page 5)
*   **Problem:** The caption for the DESI/LAMOST panel refers to `§IID` for the training pool definition, but the SDSS caption refers to `§IIIC`. The SDSS section is `§IIIC`, but the method is in `§II`.
*   **Fix:** The SDSS caption should reference the relevant part of Section II that describes the native re-training (`§IIB` and `§IID`), and then `§IIIC` for the specific results of that re-training. The current reference is confusing.

---

## Summary recommendation

**MAJOR REVISIONS**

This paper represents a substantial effort with potentially significant scientific outcomes. The authors' transparency regarding methodological challenges is a strength. However, the work is not yet at the standard required for publication in Physical Review D. The decision to include vast amounts of data from pipelines that fail the paper's own validation tests is a critical flaw that undermines the integrity of the resulting catalog. This, combined with the use of inconsistent anomaly definitions and significant presentational issues, requires a major overhaul of the paper's structure and claims.

If the authors can construct a smaller, but methodologically robust and consistently defined, catalog and clearly separate it from the more exploratory and less reliable datasets, the paper could become a valuable contribution. The cosmological analyses, while currently showing null or marginal results, are well-motivated and would be strengthened by being applied to a more rigorously validated tracer sample.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated and more rigorous referee report.

================================================================
## Referee Report on "Spectrally Unusual Sources at Scale..."

This paper presents a large-scale anomaly detection analysis across seven astronomical surveys, resulting in a catalog of 378,280 unique anomalous sources. The work is ambitious and tackles important challenges in modern survey astronomy. It presents several valuable results, including the identification of high-redshift QSO candidates, the discovery of an uncataloged BAL QSO, and important null tests that rule out cosmological signals in CMB map-patch anomalies. The authors are also commendably transparent about methodological failures, such as the initial cross-transfer approach, which provides important lessons for the community.

However, the paper suffers from several major methodological and presentational issues that must be addressed before it can be considered for publication in Physical Review D. The structural integrity of the final catalog is questionable due to the inclusion of large datasets from pipelines that fail the authors' own primary validation criteria. The definition of an "anomaly" is inconsistent across surveys, and the presentation of key results in tables and figures is often confusing, mixing final data with superseded diagnostics. Furthermore, a key equation in the cosmological analysis is dimensionally inconsistent, and a headline result contains a significant arithmetic error.

Below is a detailed list of required revisions.

---

### ESSENTIAL

**P3-E1: Inclusion of Data from Failed Validation Gates**
*   **Section:** III, VI C, Figure 7 (Pages 3, 7, 8, 12, 13)
*   **Problem:** Three of the six point-source surveys (LAMOST, Gaia, eROSITA) which contribute a significant number of objects to the final catalog, fail the primary injection-recovery validation gate (recovery < 50% at 5σ). The paper justifies their inclusion by labeling them "exploratory" or by citing secondary, less rigorous validation metrics (e.g., "XV-stability"). This fundamentally undermines the reliability of a large fraction of the catalog. A catalog presented as a unified scientific product cannot be built upon methods that the authors' own analysis shows are not robust. The headline number of 378,280 is heavily inflated by these unvalidated or poorly validated sources.
*   **Fix:** The authors must choose one of two paths:
    1.  Remove all surveys that fail the primary validation gate from the main, headline catalog. These results can be presented in an appendix as methodological case studies, but they cannot be part of the principal scientific result. The abstract and all headline numbers must be revised accordingly.
    2.  Provide a much stronger, quantitatively-backed argument for why the injection-recovery gate is not the appropriate metric for these specific surveys and why the alternative metrics are sufficient to guarantee catalog purity and completeness. This would require a significant expansion of the validation section. As it stands, the justification is insufficient.

**P3-E2: Inconsistent Anomaly Thresholds**
*   **Section:** II B (Page 2), Table I (Page 6)
*   **Problem:** The paper uses at least four different methods to define the anomaly threshold across the different surveys: an absolute `S > 5.0` cut (DESI), a top-percentile cut (SDSS, LAMOST, Gaia, Planck, NEOWISE), an Isolation Forest score-knee (eROSITA), and a fixed count cap (eROSITA). This makes the term "anomaly" physically inconsistent across the catalog. A source just below the threshold in one survey might be considered highly anomalous in another. This heterogeneity invalidates the interpretation of the total anomaly count and complicates any cross-survey statistical analysis.
*   **Fix:** The authors must apply a single, well-justified thresholding methodology to all surveys to create a homogeneous catalog. If this is not possible, they must provide a detailed justification for the different choices and add a prominent discussion of the implications and limitations of combining such heterogeneous samples. The current approach is not acceptable for a unified catalog.

**P3-E3: Inappropriate Content (Table IV, Future Dating)**
*   **Section:** Abstract (Page 1), Table IV (Page 14)
*   **Problem:**
    1.  The paper is dated "June 2026". This is unacceptable for a scientific submission.
    2.  Table IV, "Path-C residual caveats," reads like an internal project management checklist, not a formal part of a scientific paper. Listing results or analysis steps as "closed caveats" is inappropriate.
*   **Fix:**
    1.  The date must be corrected to the date of submission.
    2.  Table IV must be removed entirely. Its content, where relevant, should be integrated into the main prose of the discussion or limitations sections.

**P3-E4: Misleading Presentation of Key Results (Table I, Figure 1)**
*   **Section:** Figure 1 (Page 4), Table I (Page 6)
*   **Problem:**
    1.  Table I, the main summary table, is structured around the "before/after" narrative of the methodological rebuild. The main columns present superseded "cross-transfer" counts, while the final, canonical results are relegated to footnotes and a summary row. This is extremely confusing for the reader.
    2.  Figure 1 is titled "Spatial distribution of all 319,443 anomalies," but the caption clarifies this is the "initial cross-transfer anomaly baseline," not the final catalog of 378,280 objects. The title is misleading.
*   **Fix:**
    1.  Table I must be completely redesigned. It should clearly present the final, canonical "Path-C" results for each survey in the main columns (number of sources, anomaly count, rate, etc.). The superseded cross-transfer numbers should be moved to a separate diagnostic table or an appendix if they are essential for the narrative.
    2.  Figure 1 should either be updated to show the final 378,280 anomalies or its title must be changed to "Spatial Distribution of Initial Cross-Transfer Baseline" to avoid ambiguity.

**P3-E5: Arithmetic Error in fNL Forecast**
*   **Section:** V b (Page 11), Abstract (Page 1), Conclusions (Page 14)
*   **Problem:** The paper claims a "7.9% improvement" in the constraint on `fNL`. The baseline is `σ(fNL)std = 8.98` and the new forecast is `σ(fNL) = 8.14`. The fractional improvement in the standard deviation is `(8.98 - 8.14) / 8.98 = 9.35%`. The 7.9% figure is a clear miscalculation and is repeated in the abstract, main text, and conclusions, misrepresenting a key cosmological result.
*   **Fix:** The authors must re-calculate this value, verify it, and correct it throughout the manuscript. If 7.9% is somehow correct, they must explicitly show the calculation, as it does not follow from the standard definition of fractional improvement.

**P3-E6: Dimensionally Inconsistent Equation**
*   **Section:** Appendix E, Equation (E1) (Page 16)
*   **Problem:** Equation (E1), which defines the matter-bounce power-law model used for the NANOGrav analysis, is dimensionally inconsistent. The terms `log10(f_yr)` and `log10(f_i)` are treated as separate additive terms, which is mathematically invalid as the argument of a logarithm must be dimensionless. This fundamental error in the model specification calls into question the validity of the entire NANOGrav-based analysis, including the derived value of γ and the associated Bayes factors.
*   **Fix:** The authors must correct Equation (E1) to a dimensionally consistent form (e.g., using terms like `log10(f_i/f_yr)`). They must then re-run the entire MCMC analysis with the corrected model and update all derived results (`γ`, σ values, Bayes factors) throughout the manuscript.

### MAJOR

**P3-M1: Unclear Justification for LAMOST Anomaly Count**
*   **Section:** III D (Page 7), Table I (Page 6)
*   **Problem:** The paper reports that the native retrain for LAMOST "compresses the anomaly rate 21.5x to 2,054 at S > 5". However, the released and analyzed LAMOST anomaly set contains 113,342 objects, corresponding to a much looser threshold of `S ≥ 0.4613`. This set fails injection recovery with only 5.8% efficiency. The rationale for choosing this extremely low threshold and retaining this large, unvalidated set in the "exploratory tier" is not sufficiently justified.
*   **Fix:** Provide a clear and compelling scientific justification for releasing the top-113,342 LAMOST sources instead of the more conservative S>5 sample of 2,054. Explain what scientific value this specific sample is expected to have, given its poor performance in validation tests.

**P3-M2: Ambiguous Jargon and Acronyms**
*   **Section:** Throughout
*   **Problem:** The paper relies heavily on internal jargon like "Path-C," "gate," "PASS/FAIL," and "XV-stability" without clear, upfront definitions. "Path-C" appears to be the name for the final analysis pipeline, but this is only discernible after reading a significant portion of the paper.
*   **Fix:** Define all non-standard terms and acronyms at their first use. Provide a global definition of the "Path-C" protocol in the introduction or the beginning of the method section.

**P3-M3: Misleading Abstract**
*   **Section:** Abstract (Page 1)
*   **Problem:** The abstract is misleading in its presentation of results. It describes the subset including Gaia and eROSITA as "recommended catalog-grade" even though these surveys fail the paper's primary validation gate. It also selectively highlights a secondary validation metric for eROSITA (81.5% stability) while omitting the primary test failure (1.2% injection recovery). This paints an overly optimistic picture of the catalog's robustness.
*   **Fix:** The abstract must be rewritten to faithfully represent the results and limitations discussed in the main text. It must clearly distinguish between robustly validated catalog components and those that are exploratory or failed validation.

**P3-M4: Incomparable Juxtaposition of Anomaly Rates**
*   **Section:** Table I (Page 6)
*   **Problem:** Table I presents the "Rate (%)" of anomalies for all surveys in a single column, implicitly inviting comparison. However, because the thresholds are defined using different, incompatible methods (e.g., a fixed MSE cut for DESI vs. a top-1% selection for Gaia), the rates are not comparable. The Gaia rate is 1.00% by definition, not as a result of a physical measurement, making a comparison to DESI's 0.87% rate meaningless.
*   **Fix:** The "Rate (%)" column should be removed or heavily annotated to make it clear that the values are not directly comparable across all surveys. The method for determining the threshold for each survey must be made more prominent.

### MINOR

**P3-m1: Contradictory DESI Anomaly Rate**
*   **Section:** IV A (Page 4)
*   **Problem:** The text states, "The headline 195,829 DESI anomaly count is the top-1% score-cut of the full 22.5-M-spectrum scan". However, 195,829 / 22,504,897 is 0.87%. The text later correctly states the "anomaly rate of 0.87%". The initial "top-1%" claim is incorrect and appears to be a stale artifact from a previous version of the analysis.
*   **Fix:** Remove the incorrect "top-1% score-cut" statement.

**P3-m2: Unprofessional Author Contact Information**
*   **Section:** Author block (Page 1)
*   **Problem:** The contact email `houston@hubify.com` appears to be associated with a marketing company, which is unprofessional for a submission to a leading physics journal.
*   **Fix:** The author should provide a standard institutional or personal email address appropriate for academic correspondence.

**P3-m3: Internal Notes in Bibliography**
*   **Section:** References (Page 19)
*   **Problem:** The bibliographic entry for Heinrich et al. [33] contains an internal note: "[publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity]". This is bookkeeping information and should not be in the final manuscript.
*   **Fix:** Remove the internal note and format the citation according to the journal's style guide.

**P3-m4: Aggressive Downsampling of Spectra**
*   **Section:** II A (Page 2)
*   **Problem:** Spectroscopic data is downsampled by a factor of 16 to 496 bins. This is a very aggressive compression that could erase information from narrow spectral features, which are often a key signature of unusual objects.
*   **Fix:** Add a sentence justifying this choice. For example, discuss the trade-off between resolution and computational cost, or demonstrate that the primary features of interest for anomaly detection are preserved at this resolution.

**P3-m5: Poor Internal Referencing**
*   **Section:** III E (Page 7), VI C (Page 12)
*   **Problem:** Internal cross-references such as `§VID (f)` and `§VID (v)` point to non-existent subsections. This appears to be a reference to the list in Table IV, which is an unconventional and confusing way to cite information. It prevents readers from easily verifying claims.
*   **Fix:** All internal references must point to specific, existing sections, figures, tables, or equations in the manuscript.

### NIT

**P3-N1: Confusing Figure 2 Caption**
*   **Section:** Figure 2 (Page 5)
*   **Problem:** The caption for the SDSS panel refers to `§IIIC`, which describes the results, but not the method. A clearer reference would point to the general methodology sections as well.
*   **Fix:** The SDSS caption should reference the relevant parts of Section II that describe the native re-training (`§IIB` and `§IID`), and then `§IIIC` for the specific results of that re-training.

---

## Summary recommendation

**MAJOR REVISIONS**

This paper represents a substantial effort with potentially significant scientific outcomes. The authors' transparency regarding methodological challenges is a strength. However, the work is not yet at the standard required for publication in Physical Review D. The decision to include vast amounts of data from pipelines that fail the paper's own validation tests is a critical flaw that undermines the integrity of the resulting catalog. This, combined with a dimensionally inconsistent equation in a key analysis, a significant arithmetic error, the use of inconsistent anomaly definitions, and major presentational issues, requires a major overhaul of the paper's structure and claims.

If the authors can construct a smaller, but methodologically robust and consistently defined, catalog, and clearly separate it from the more exploratory and less reliable datasets, the paper could become a valuable contribution. The cosmological analyses must be re-run with a corrected physical model before their conclusions can be considered.