# P3 R26conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.84.pdf` md5=2539e13c pages=25
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (4182 chars)
**Wall time**: 156.5s

---

Here is a referee report for the provided paper.

***

## Referee Report: "Spectrally Unusual Sources at Scale..." by Houston Golden

**Report ID:** PRD-2026-06-P3-R26conf

**To the Editor of Physical Review D,**

I have reviewed the manuscript "Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and Native-Trained Novelty Fractions from 37.3 Million Sources and Map Patches" by Houston Golden. The paper presents a large-scale anomaly detection campaign across seven astronomical archives, resulting in a catalog of nearly 400,000 unusual sources. The authors then use a subset of these sources to forecast constraints on primordial non-Gaussianity (fNL) and to test consistency with predictions from matter-bounce cosmology in the context of NANOGrav data.

The scope of the work is impressive, and the authors are to be commended for their transparency in documenting methodological challenges, validation failures, and residual caveats. This level of self-criticism is rare and valuable. However, the manuscript in its current form contains several issues of essential importance regarding reproducibility, clarity, and the presentation of results that preclude its publication in Physical Review D without significant revision. The cosmological applications, while interesting, are secondary to the main catalog work, and the rigor of their presentation must meet the high standards of the journal.

My detailed findings are listed below.

---

### ESSENTIAL Revisions

These issues must be addressed for the paper to be reconsidered for publication.

**P3-E1: Abstract Clarity and Internal-History Language**
*   **Location:** Abstract, Page 1
*   **Problem:** The abstract is convoluted with multiple, slightly different numbers for the same quantity and contains language referring to the paper's drafting history. For example: "...the recommended catalog-grade subset is ~ 269,000 unique entries (269,317 from a direct, independent 6-way 5" dedup... leaving the 269,117 catalog-grade point-source subset; an earlier draft quoted 264,938/264,738... which double-removes the 4,379 LAMOST detections...)".
*   **Required Fix:** The abstract must be rewritten to be a clean, concise summary of the final, canonical results. State the final, definitive numbers for the total catalog, the recommended point-source subset, etc., without the confusing arithmetic and without any reference to "earlier drafts" or internal bookkeeping. This is a summary for the reader, not a change log.

**P3-E2: Non-Reproducible eROSITA Selection**
*   **Location:** Section III E, Page 8
*   **Problem:** The authors state that the selection of the 298 eROSITA anomalies is based on a threshold (0.259) on a score axis that "could not be reconciled with the canonical S of Eq. (2)" and that "no committed score axis reproduces the production threshold." The selection is based on a "committed, reproducible selection" from a previous run, which is fundamentally not reproducible from the methods described in the paper. This fails the basic standard of scientific reproducibility.
*   **Required Fix:** The eROSITA anomaly sample cannot be presented as a primary science result of the described methodology. The authors must either (a) remove the eROSITA analysis entirely, or (b) heavily quarantine it alongside ACT DR6, with explicit statements in the abstract, main text, and conclusions that this subsample is an unreproducible artifact included only for completeness. The current framing is insufficient.

**P3-E3: Inconsistent and Incomparable σ(fNL) Definitions**
*   **Location:** Appendix C, Figure 11, Page 21
*   **Problem:** The caption for Figure 11 explicitly states that the σ(fNL) values presented (e.g., single-tracer baseline of 16.85, dense-tracer limit of 11.71) "are not on the same absolute normalization as the redshift-binned Fisher of §V, whose canonical single-tracer DESI-QSO baseline is σ(fNL)std = 8.98." Presenting sigma values from different normalization schemes side-by-side, or in a single plot, without a common, dimensionless normalization is highly misleading and unacceptable.
*   **Required Fix:** Figure 11 must be replotted. The y-axis should not be absolute σ(fNL) but a dimensionless quantity, such as "Fractional Improvement over Baseline" or σ(fNL) / σ(fNL)_baseline. Alternatively, the figure can be removed and the key point (the 15-30% degradation) stated in the text. The current presentation is an apples-to-oranges comparison that will inevitably cause confusion.

**P3-E4: Internal-History Language in Main Body**
*   **Location:** Section IV B, Page 11
*   **Problem:** The text contains the sentence: "An earlier draft quoted 38,330 pixels with χ²_red = 3.76; that artifact's pixel-selection and variance model could not be recovered from the committed analysis tree, and the figure is withdrawn in favor of the reproducible recompute above."
*   **Required Fix:** All such references to "earlier drafts," withdrawn figures, or the process of the analysis must be removed from the manuscript. The paper should present the final, validated results and methods only.

### MAJOR Revisions

These issues represent significant flaws that must be corrected.

**P3-M1: Misleading fNL Forecast Figure**
*   **Location:** Figure 9, Page 16
*   **Problem:** The main result of the fNL analysis (§V) is that the empirically measured bias enhancement `a_jk` is consistent with zero, leading to "no improvement" in the constraint on fNL. However, Figure 9 illustrates a "fixed-α = 0.15 reference Fisher forecast" which shows a 6.1% improvement. This is misleading, as it highlights a hypothetical scenario rather than the paper's actual, null result.
*   **Required Fix:** The figure should be remade to reflect the primary result of the paper. It should use the empirically measured `a_jk = 0.19 ± 0.65` and show the resulting central value and 1σ uncertainty band, which would correctly visualize the "no improvement" conclusion. Presenting a what-if scenario as the main figure for this section is inappropriate.

**P3-M2: Insufficient Discussion of Validation Failures**
*   **Location:** Section IID (page 4), Section VI C (page 16), Figure 10 (page 17)
*   **Problem:** The injection-recovery tests—a cornerstone of validation—FAIL for three of the six main surveys (LAMOST, Gaia, eROSITA). While the authors commendably report these failures, their implications are not sufficiently discussed in the main body. A reader might miss the fact that the completeness and reliability of nearly half the catalog sources are formally unquantified.
*   **Required Fix:** Add a dedicated paragraph in the main Discussion (Section VI) that explicitly addresses the scientific implications of these validation failures. It should state clearly that results from LAMOST, Gaia, and eROSITA should be treated as exploratory and may suffer from unknown selection biases or contamination, and this caveat should be mentioned in the conclusions.

**P3-M3: Use of Non-Canonical "Display Scores" in Figure**
*   **Location:** Figure 8, Page 14
*   **Problem:** The caption states: "...the burned-in 'Score' annotations are display values from that script rather than catalog-pipeline outputs...". This undermines the scientific utility of the figure. A figure in a scientific paper should present the actual data and derived quantities from the canonical analysis pipeline.
*   **Required Fix:** Regenerate the figure using the final, canonical anomaly scores (S) from the released catalog for the objects shown. The scores are a key output of this work and should be used consistently.

### MINOR Revisions

These points should be addressed to improve the paper's quality and clarity.

**P3-m1: Ambiguous "Gold" Tier Definitions**
*   **Location:** Figure 1 caption (page 2) and Section V (page 15)
*   **Problem:** The paper uses the term "gold" to refer to two different sets of objects: the "83 gold-tier anomalies" in Figure 1 and the "116-object GOLD QSO-candidate confidence tier" for the fNL forecast. This is a source of confusion.
*   **Required Fix:** Use distinct terminology for these two samples throughout the paper. For example, "Gold-tier display sample" for Figure 1 and "Gold-confidence forecast sample" for Section V.

**P3-m2: Assumption of Zero fNL Systematics**
*   **Location:** Section V, Page 15
*   **Problem:** The fNL forecast "assumes zero observational systematics (fiber-assignment, photo-z, foreground)." While a full systematics treatment is beyond the scope of a forecast, this assumption is very strong.
*   **Required Fix:** Add 1-2 sentences briefly discussing the potential impact of these systematics. For instance, mention that uncorrected systematics in the anomaly sample could mimic or mask an fNL signal by introducing spurious clustering, and that this is a key challenge for future analysis.

**P3-m3: Unsupported GR Projection Calculation**
*   **Location:** Section V, Page 15
*   **Problem:** The paper quotes a value for general-relativistic projection corrections: "|Δσ/σ| < 0.02%". This is a non-trivial calculation.
*   **Required Fix:** Add a citation to a standard paper where this calculation is performed (e.g., Yoo et al. 2009, Bonvin & Durrer 2011) or, if it is a custom calculation, provide a brief derivation in an appendix.

---

## Summary recommendation

**MAJOR REVISIONS**

The manuscript presents a substantial and potentially valuable contribution by assembling the largest multi-survey anomaly catalog to date. The authors' commitment to transparency regarding methodological failures is a major strength. However, the paper is currently undermined by several essential flaws in reproducibility (the eROSITA selection), clarity (the abstract and figures), and statistical rigor (the comparison of incomparable σ(fNL) values). These issues prevent the paper from meeting the standards of Physical Review D. If the authors can thoroughly address the ESSENTIAL and MAJOR points listed above—in particular by rectifying the reproducibility of the eROSITA sample, clarifying the abstract, and ensuring all figures and comparisons are presented in a consistent and non-misleading way—a revised version could be suitable for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from a second, more detailed review of the manuscript.

***

### NEW FINDINGS (Second Pass Review)

This second pass review was conducted to identify more subtle issues that may have been missed in the initial report. The following points are new and should be addressed in addition to those in the first report.

### ESSENTIAL Revisions

**P3-E5: Unverified and Potentially Incorrect NANOGrav Likelihood Equation**
*   **Location:** Appendix E, Equation E1, Page 21
*   **Problem:** The log-likelihood equation (E1) used for the NANOGrav analysis does not appear to match standard formulations for a power-law gravitational-wave background in pulsar timing data. Furthermore, a naive reading of the equation suggests it is dimensionally inconsistent, as it takes the logarithm of dimensionful quantities like frequency (`f_yr`, `f_i`) and time (`T_obs`) without appropriate reference scales. While this can be an abuse of notation, the combination of terms does not obviously resolve to the expected dimensionless power-law form. The credibility of the entire NANOGrav-related result (`γ` measurement, Bayes factors, and consistency with matter-bounce) rests on this equation being correct.
*   **Required Fix:** The authors must provide a rigorous justification for Equation E1. This should take the form of either (a) a full derivation in the appendix, starting from the standard definition of the power spectrum of timing residuals, or (b) a direct citation to the specific paper or software documentation (e.g., for the `ceffyl` package mentioned) that defines and validates this exact formula. Without this, the result is not reproducible or verifiable.

### MINOR Revisions

**P3-m4: Incorrect Cross-Reference in Abstract**
*   **Location:** Abstract, Page 1
*   **Problem:** The abstract states that the size benchmark for the catalog is anchored to a prior work, with a reference to §VI. Section VI (Discussion) does not contain this comparison. The comparison is made in Section VII (Conclusions).
*   **Required Fix:** Correct the cross-reference in the abstract to point to Section VII.

**P3-m5: Imprecise Cross-Reference in Abstract**
*   **Location:** Abstract, Page 1
*   **Problem:** The abstract refers to §II for the definition of the "SDSS component is the 77,905-object native continuity slice". Section II describes the general methodology, but the specific definition of this slice is located in a footnote to Table I and discussed in Section III C.
*   **Required Fix:** Make the cross-reference more precise or remove it if it is not essential for the abstract.

**P3-m6: Incorrect Cross-Reference in Methodology**
*   **Location:** Section II D, Page 4
*   **Problem:** The text states that the initial cross-transfer scan is "preserved in Table I and §VIA". Section VI A discusses the LAMOST training bias and does not contain the relevant diagnostic information.
*   **Required Fix:** Correct the cross-reference to point only to Table I, which contains the "before/after" counts.

**P3-m7: Incorrect Cross-Reference in Table I**
*   **Location:** Table I, Footnote §, Page 7
*   **Problem:** The footnote refers to §VID(ii) for details on the IsolationForest cross-validation stability. Section VID(ii) discusses injection-recovery synthesis, not Isolation Forest stability. The stability results are mentioned in other sections (e.g., III E, III G) but not where the reference points.
*   **Required Fix:** Correct or remove the incorrect cross-reference.

### NOTEWORTHY Points (for author consideration)

**P3-N1: Overly Long Title**
*   **Location:** Title, Page 1
*   **Problem:** The title is exceptionally long and includes specific numbers that are detailed in the abstract. A more concise title would improve the paper's impact and discoverability.
*   **Recommendation:** Consider shortening the title to something more direct, for example: "A Multi-Survey Catalog of 378,000 Spectrally Unusual Sources from 37 Million Objects".

**P3-N2: Typographical Error in Date**
*   **Location:** Page 1
*   **Problem:** The paper is dated "June 2026".
*   **Recommendation:** Correct the date to the year of submission.