# P3 auto-2026-06-08_2353pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (3991 chars)
**Wall time**: 151.7s

---

Here is a referee report for the submitted paper.

---

## Referee Report: "Spectrally Unusual Sources at Scale..."

This paper presents a large-scale anomaly detection study across seven major astronomical surveys, resulting in a catalog of over 378,000 unique anomalous sources. The authors apply a unified autoencoder framework (BIGAE), develop a robust "Path-C" validation protocol involving native retraining for each survey, and perform extensive validation including cross-validation, out-of-distribution tests, and injection-recovery simulations. The work has two primary motivations: the discovery of rare astrophysical objects and the identification of high-bias tracers to improve constraints on primordial non-Gaussianity (fNL).

The scale of the analysis is impressive, and the methodological rigor is exceptionally high. The authors are transparent about limitations, failure modes (e.g., the LAMOST training bias, the quarantined ACT data), and the interpretation of their results (e.g., the distinction between database coverage and genuine novelty). The resulting catalog and the cosmological forecasts represent a significant contribution. The paper is well-written and detailed.

However, there are several issues that must be addressed before the paper can be considered for publication in Physical Review D. The most critical is a numerical inconsistency in one of the headline cosmological results. I recommend **MAJOR REVISIONS**.

### ESSENTIAL Revisions

**P3-E1**
- **Section**: Abstract (p. 1), Section V.b (p. 11), Section VI.C (p. 12), Section VII (p. 14)
- **Problem**: There is a persistent numerical discrepancy in the quoted improvement for the fNL forecast. The paper repeatedly states a "7.9% improvement" over the single-tracer baseline. However, the provided values for the standard deviation of fNL do not support this number. The baseline is given as σ(fNL)std = 8.98, and the new central forecast is σ(fNL) = 8.14. A standard calculation of the fractional improvement in the constraint yields (8.98 - 8.14) / 8.98 ≈ 9.35%. The 7.9% figure is not derivable from the provided numbers and appears to be incorrect. This is a critical error as it affects a key result highlighted in the abstract, main text, and conclusions.
- **Required Fix**: The authors must either:
    1. Correct the percentage to ~9.4% throughout the manuscript (abstract, p. 11, p. 12, conclusions).
    2. Provide a clear, explicit derivation for how the 7.9% figure is calculated if it relies on a non-standard definition of "improvement" (e.g., related to variance or some other quantity). The current text provides no such justification.

### MAJOR Revisions

**P3-M1**
- **Section**: III (p. 3), Table I (p. 6)
- **Problem**: The main summary table (Table I) is confusingly structured. The primary rows for each survey report the anomaly counts from the initial, superseded "cross-transfer" scan. The final, canonical "Path-C" native-retrained counts—which are the main scientific result of the paper—are relegated to a dense footnote and a single summary row at the bottom. This presentation obscures the final results and forces the reader to piece together the most important information from the caption.
- **Required Fix**: Restructure Table I to present the final, canonical Path-C anomaly counts for each survey in the main table rows. The "N_anom" column should contain the final numbers used in the deduplicated total (e.g., 113,342 for LAMOST, the re-scored number for SDSS, etc.). The initial cross-transfer counts are valuable as a "before/after" diagnostic and should be moved to a separate column labeled "N_anom (cross-transfer)" or to a separate, clearly labeled table in an appendix. The primary results of the paper must be presented with maximum clarity in the main summary table.

### MINOR Revisions

**P3-m1**
- **Section**: II.B (p. 2)
- **Problem**: The paper uses a heterogeneous set of anomaly thresholds across the different surveys (e.g., absolute S > 5, top-1% percentile, IsolationForest knee). While the footnotes in Table I describe these choices, the justification is scattered. A more consolidated discussion in the main methods section would improve clarity.
- **Required Fix**: In Section II.B, add a paragraph explaining the rationale for choosing different thresholding strategies for different surveys. For example, why was an absolute MSE-based cut (S > 5) suitable for DESI/SDSS but a percentile cut was preferred for LAMOST/Gaia? This would strengthen the methodological description.

**P3-m2**
- **Section**: References (p. 19)
- **Problem**: Reference [33] contains an internal note: "[publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity]". This is internal bookkeeping and is not appropriate for a final publication.
- **Required Fix**: Remove the explanatory note from the reference. The citation should be formatted consistently with the journal's style guide.

**P3-m3**
- **Section**: V.A (p. 11)
- **Problem**: The paper states that the fNL forecast "assumes zero observational systematics". While this is mentioned in the limitations section, this is a very strong assumption for a precision cosmology forecast and should be stated more prominently alongside the main result itself.
- **Required Fix**: In Section V.b, when presenting the final σ(fNL) = 8.14 forecast, reiterate that this is an idealized forecast that does not yet include modeling of observational systematics like fiber assignment completeness or photometric redshift errors.

### NITs (Cosmetic)

**P3-N1**
- **Section**: Abstract (p. 1)
- **Problem**: The phrase "single-sample point estimate at the top-1,000 score stratum; full-catalog rate empirically untested" is slightly verbose and could be tightened for clarity.
- **Required Fix**: Consider revising to something like: "...a genuine novelty fraction of ~17.8% (a point estimate from the top-1,000 DESI anomalies)."

**P3-N2**
- **Section**: IID (p. 3), VID (p. 13)
- **Problem**: The injection-recovery results are a key part of the validation, but the results are described in prose and summarized in a complex figure (Fig. 7). A simple summary table might improve scannability.
- **Required Fix**: Consider adding a small table that lists the six surveys tested, the type of injection, the recovery rate at 5σ, and the final gate status (PASS / FAIL-with-diagnostic). This would complement Figure 7 and the text.

---

## Summary recommendation

**MAJOR REVISIONS**

This is a high-quality, comprehensive, and methodologically rigorous paper that presents a valuable, large-scale anomaly catalog and its first cosmological applications. The work is of a high standard suitable for publication in Physical Review D. However, the identified numerical error in a headline result is an essential issue that must be fixed. Furthermore, the confusing presentation of the main summary table (Table I) significantly hinders the clarity of the paper's primary results. Once these issues, particularly the essential and major points, are thoroughly addressed, the paper will be a strong candidate for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated referee report, incorporating findings from a more rigorous second review.

---

### ADDITIONAL FINDINGS (Second Review)

A deeper, more rigorous review of the manuscript has uncovered several additional issues, including two critical errors in the cosmological analysis that must be addressed. These are in addition to the points raised in the initial report.

### ESSENTIAL Revisions (New)

**P3-E2**
- **Section**: Abstract (p. 1), Section V.b (p. 11)
- **Problem**: The 1-sigma uncertainty envelope reported for the primordial non-Gaussianity forecast, σ(fNL) ∈ [3.92, 8.98], is incorrectly constructed and statistically misleading. The lower bound (3.92) is correctly derived from the +1σ value of the bias parameter `a`. However, the upper bound (8.98) is simply the single-tracer baseline value, corresponding to `a=0`. The correct upper bound should be derived from the -1σ value of the bias parameter (`a` = 0.19 - 0.65 = -0.46). Using the paper's own formula and numbers, this yields σ(fNL) ≈ 5.93. The currently reported interval incorrectly implies that the 1σ uncertainty on the bias parameter can only lead to an *improvement* in the constraint, which is unphysical.
- **Required Fix**: The authors must re-calculate the 1-sigma envelope for σ(fNL) using the full ±1σ range of the empirically measured bias parameter `a`. The corrected, symmetric (in `a`) uncertainty interval must be reported in the abstract and Section V.b.

**P3-E3**
- **Section**: Appendix C (p. 15), Figure 8 Caption (p. 15)
- **Problem**: The analysis of shot-noise degradation for the fNL forecast is arithmetically inconsistent. Appendix C states that a 15% Fisher-info penalty results in σ(fNL) = 12.56, which is described as a "+1.27% change" over the baseline of 12.72. This is arithmetically impossible (12.72 * 1.0127 ≈ 12.88). Furthermore, the expected scaling is σ_new = σ_old / sqrt(1 - penalty), which would give 12.72 / sqrt(0.85) ≈ 13.79. The numbers presented in the text and figure caption do not follow from the stated premises and are internally contradictory.
- **Required Fix**: The entire calculation in Appendix C must be reviewed and corrected. The text, percentages, and final σ(fNL) values must be made arithmetically consistent with the standard definition of a Fisher information penalty. The caption of Figure 8 must also be updated with the corrected values.

### MINOR Revisions (New)

**P3-m4**
- **Section**: Abstract (p. 1)
- **Problem**: The abstract defines a "recommended catalog-grade subset" of `~265,000` unique objects. However, a simple sum of the native-retrained anomaly counts for the specified surveys (DESI + SDSS + eROSITA + Gaia + NEOWISE) is 274,951. The ~10k difference is presumably due to positional deduplication within this specific subset, but this is not stated.
- **Required Fix**: Briefly clarify the origin of the `~265,000` number. For example, "...subset is ~265,000 unique objects (after internal deduplication)...".

**P3-m5**
- **Section**: Appendix E, Eq. E1 (p. 16)
- **Problem**: The physical and dimensional consistency of the NANOGrav power-law model (Eq. E1) is not immediately clear from its presentation. It appears to be a term in a log-likelihood function rather than a direct equation for spectral power, which could confuse non-specialist readers.
- **Required Fix**: Add a brief clarifying phrase or a direct citation to the specific equation in the source paper [18] from which this model is adapted. For example, "The log-likelihood term for the power P_i in frequency bin i is modeled as...".

**P3-m6**
- **Section**: VI.C (p. 12)
- **Problem**: The text contains a broken internal cross-reference. It refers to "§VID (v))" for details on IsolationForest cross-validation. This subsection does not exist in the manuscript.
- **Required Fix**: Correct the cross-reference to point to the appropriate location where this information is provided (e.g., the footnote in Table I or another part of the text).