# P3 R57 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/private/tmp/R57_P3/paper3_draft.pdf` md5=044460cc pages=31
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (3661 chars)
**Wall time**: 209.0s

---

**Referee Report for "Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and a Native-Trained Novelty Fraction from 37.3 Million Sources and Map Patches"**

This paper presents a large-scale anomaly detection analysis across seven astronomical surveys, resulting in a catalog of over 378,000 unique candidate anomalies. The work is notable for its scale, its multi-survey approach enabling cross-validation, and its careful application to cosmological questions, namely constraints on primordial non-Gaussianity (f_NL) and the stochastic gravitational-wave background. The authors are commendably transparent about the limitations of their methods, the various data quality and reproducibility issues encountered, and the proper interpretation of their statistical results. The distinction between robustly validated and exploratory components of the catalog is a particular strength.

While the paper represents a significant and valuable contribution, several revisions are required before it can be considered for publication in Physical Review D. The findings are categorized below.

---

### ESSENTIAL Revisions

**P3-E1: Artifacts in Text (Date and Internal File Paths)**
-   **Section/Page:** Abstract (p. 1), various throughout.
-   **Problem:** The paper contains several artifacts that are not appropriate for a final publication.
    1.  The date of the paper is listed as "(Dated: June 26, 2026)", a future date.
    2.  The text contains multiple internal file paths to a code repository (e.g., `pipelines/p3_anomaly_engine/ext3_b2_targettype_recount.json` on p. 9; `.../r24conf_erosita_axis_sweep.json` on p. 12; `.../ext3_fm2_planck_top200_train_overlap.json` on p. 13; `.../r23conf_dedup_audits.json` on p. 15; `.../r24conf_pod_session_batch.json` on p. 16; `.../r43_4caveats_closure/result.json` on p. 22).
-   **Required Fix:**
    1.  Correct the date to the date of submission.
    2.  Remove all internal file paths. These should be replaced with references to the appropriate table, figure, or section in the main text or a general pointer to the public data repository, not a hardcoded path to a specific JSON file. The existence of these artifacts suggests the manuscript was not sufficiently proofread.

**P3-E2: Data Leak in Preprocessing and Scoring**
-   **Section/Page:** §II B (p. 3), §III F (p. 13).
-   **Problem:** The analysis contains at least two instances of data leakage, where information from outside the training set influences the model or the final scoring.
    1.  For the tabular surveys (eROSITA, NEOWISE, Gaia), the feature scalers were fit on the full data sample, including the validation and test sets (§II B). The authors acknowledge this and perform a robustness check for eROSITA, but it remains a methodological flaw.
    2.  For the Planck CMB analysis, the final top-200 anomaly list is selected from a scoring run on the full data bank, which includes the patches used for training the native model (§III F).
-   **Required Fix:** While re-running the entire analysis is likely impractical, these issues must be more prominently flagged as a major limitation. In the main "Limitations" section (§VI C), a specific point must be added to explicitly state that data-leakage protocols were identified in the tabular-survey preprocessing and Planck scoring, and while the authors have attempted to bound the effects, the results from these specific surveys may have compromised integrity. The current framing, while honest, could be missed by a reader not focused on the minutiae of §II B.

**P3-E3: Severe Provenance and Reproducibility Issues**
-   **Section/Page:** §II B (p. 3), §III E (p. 11-12), §III G (p. 14).
-   **Problem:** Several key components of the analysis suffer from a lack of reproducibility.
    1.  The exact preprocessing script for the Gaia DR3 catalog was not recovered.
    2.  The per-object anomaly score axis for the eROSITA DR1 catalog is irreproducible from any committed artifact, likely due to an uncommitted post-processing step. The catalog is released as a membership list only.
    3.  Re-running the eROSITA pipeline on different hardware produced only a 247/298 (~83%) overlap in the top members.
-   **Required Fix:** These issues are correctly identified in the text and the affected catalog components are labeled "exploratory". This is good. However, the abstract and conclusions must more forcefully state that the Gaia and eROSITA components are not just "exploratory" but have documented, severe reproducibility and provenance failures. The current language ("carry per-object exploratory validity flags") is too soft. A stronger statement like "are subject to documented irreproducibility and should not be used for robust statistical analyses" is more appropriate for a journal of this standard.

---

### MAJOR Revisions

**P3-M1: Justification for SDSS Anomaly Threshold**
-   **Section/Page:** §III C (p. 10), Table I footnote ♡ (p. 8).
-   **Problem:** The headline anomaly count for SDSS DR18 (77,905 objects) is based on a "fixed-size continuity slice sized to equal the cross-transfer count". This is an arbitrary, post-hoc threshold. The physically motivated S > 5 threshold yields only 12 objects, and the statistically standard top-1% threshold yields 19,253. The choice of 77,905 is poorly justified and seems designed solely for "continuity" with a flawed baseline analysis.
-   **Required Fix:** The authors must provide a much stronger scientific justification for using the 77,905-object tier. If no such justification exists, the primary SDSS results should be reported for a standard threshold (e.g., the top-1% cut), and the 77,905-object set should be relegated to an appendix for continuity studies. Using an arbitrary threshold for a headline number is not acceptable.

**P3-M2: Overstated "PASS" Status of NEOWISE Injection Recovery**
-   **Section/Page:** §IID (p. 5), §III H (p. 14), Fig. 10 (p. 23).
-   **Problem:** The NEOWISE injection-recovery test is repeatedly labeled "PASS". However, the text explicitly states this test "passes by construction" and is a "masking-geometry sanity check... not a detector-sensitivity test". This is a crucial distinction. Grouping it with genuine sensitivity tests like SDSS and Planck under the same "PASS" label is misleading.
-   **Required Fix:** At every mention of the NEOWISE gate result, it must be qualified. For example, instead of "3 PASS", the text should read "2 PASS on sensitivity (SDSS, Planck) and 1 PASS on geometry-QA (NEOWISE)". The distinction must be clear in the abstract, main text, and Figure 10 caption to avoid misinterpretation of the validation rigor.

**P3-M3: Unclear Justification for Cosmological Systematic Error Bounds**
-   **Section/Page:** §V C (p. 19), Table V (p. 22).
-   **Problem:** The f_NL forecast relies on bounds for systematic effects that are not fully justified.
    1.  The GR projection effect bound `|Δσ/σ| < 0.02%` is described as an "internal order-of-magnitude bound from the (H/k)^2 suppression at the Fisher-weighted scales, not an external-literature value". This is insufficient for a PRD paper.
    2.  The fiber-assignment nuisance bound `|Δσ/σ| < 0.01%` is attributed to a "nuisance-Fisher block", which is a valid technique, but no details of the block's construction or priors are given.
-   **Required Fix:** Provide a more detailed derivation for these bounds in an appendix. For the GR projection bound, show the calculation (relevant scales, H(z) values) that leads to the quoted number. For the fiber nuisance, specify the parameters and priors used in the Fisher block. Without this, the claims of robustness are unsupported.

---

### MINOR Revisions

**P3-N1: Information Structure and Readability**
-   **Section/Page:** Throughout, especially p. 6-8.
-   **Problem:** Critical methodological details are often buried in extremely dense footnotes (e.g., the footnotes to Table I span three pages) or figure captions (e.g., the Figure 2 caption). This makes the paper difficult to follow and increases the risk of misinterpretation.
-   **Required Fix:** Restructure the text to move essential methodological definitions and caveats from footnotes into the main body of the text. For example, the definitions of the different catalog tiers (exploratory vs. catalog-grade) and the detailed breakdown of the SDSS thresholds should be in a dedicated subsection of the Methods or Results, not in footnotes.

**P3-N2: Ambiguity of "FAIL-with-diagnostic"**
-   **Section/Page:** §IID (p. 5), Fig. 10 (p. 23).
-   **Problem:** The term "FAIL-with-diagnostic" is used for surveys that fail the injection-recovery gate but have informative cross-validation metrics. While the intent is clear, the term itself is non-standard jargon.
-   **Required Fix:** Define this term clearly at its first use. For example: "Three surveys fail the >50% injection-recovery gate. However, for these surveys, alternative cross-validation metrics provide a quantitative measure of their stability, which we report as a diagnostic alongside the gate failure."

**P3-N3: Missing Computational Detail**
-   **Section/Page:** Table VI (p. 25).
-   **Problem:** The wall-clock training time for the native Planck CMB convolutional autoencoder is missing.
-   **Required Fix:** Provide the training time. If it was not recorded, state this explicitly and provide an estimate based on the number of epochs and hardware used.

---

### NITs

**P3-T1: Inconsistent Terminology for Anomaly Score**
-   **Section/Page:** Abstract (p. 1), §IIIE (p. 11), Table IV (p. 13).
-   **Problem:** The irreproducible eROSITA score is referred to as `S_BigAE`. This is confusing since "BigAE" is the name of the framework used for all surveys.
-   **Required Fix:** Use a more specific name, such as `S_eRASS_prod` or similar, to distinguish it from the canonical, well-defined score `S` used elsewhere. Clarify this in the text and table captions.

---

## Summary recommendation

**MAJOR REVISIONS**

This is a paper of impressive scope and commendable scientific integrity. The authors have gone to great lengths to validate their results, quantify uncertainties, and be transparent about the many limitations and challenges inherent in a project of this scale. The cosmological applications are handled with appropriate rigor, particularly the careful de-biasing of the f_NL forecast. The paper provides a valuable catalog and, just as importantly, a series of crucial methodological lessons for the field.

However, the manuscript in its current form is not yet ready for publication. The presence of internal artifacts (future date, file paths) indicates a need for careful proofreading. More seriously, the work is underpinned by several components with documented data-leakage, provenance, and reproducibility failures. While the authors are honest about these, the severity of the issues requires them to be flagged more prominently and with stronger language. Furthermore, the justification for certain key choices (like the SDSS threshold) and systematic error bounds needs to be strengthened to meet the standards of Physical Review D.

I am confident that the authors can address these points. Upon successful revision, this paper will be an excellent and impactful contribution to the literature.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from a more rigorous re-examination of the paper.

---
### ESSENTIAL Revisions

**P3-E4: Missing/Misleading Validation for eROSITA Catalog**
-   **Section/Page:** Abstract (p. 1), Table I footnote § (p. 7), Table V (p. 22).
-   **Problem:** The paper repeatedly quotes an "eROSITA cross-validation stability 81.5%". However, a close reading of Table I footnote § reveals this stability metric was computed for a top-1% reference set of 9,303 objects selected by an Isolation Forest (IF) model. The actual released eROSITA catalog is a much smaller, harder top-cut of 298 objects selected by the primary BIGAE model. The stability of this released 298-object catalog under the same resampling test is never reported. The paper instead reports a 95.3% overlap between the BIGAE top-298 and the IF top-9303 (Table V), which is a cross-method comparison, not a stability test. It is therefore misleading to claim 81.5% stability for the eROSITA component in the abstract and elsewhere, as this metric does not apply to the data product being released.
-   **Required Fix:** The authors must compute and report the resampling stability for the released top-298 eROSITA catalog. If this cannot be done, they must remove the 81.5% figure from the abstract and conclusions and explicitly state in the Limitations section that the stability of the released eROSITA catalog is unquantified. This is essential for the scientific integrity of the catalog.

---

### MAJOR Revisions

**P3-M4: Ambiguous Use of "Cross-Validation"**
-   **Section/Page:** §II C (p. 4), §III E (p. 12), §III G (p. 14), Table I footnote § (p. 7).
-   **Problem:** The term "cross-validation" is used inconsistently for two different procedures, creating confusion about the validation methodology.
    1.  For DESI, it correctly refers to a standard 5-fold cross-validation test measuring Jaccard overlap.
    2.  For eROSITA and Gaia, it refers to a stability test of an Isolation Forest model's top-ranked selection under a single data reshuffle ("1%-contamination reshuffle"). This is a form of bootstrap or resampling stability analysis, not what is conventionally meant by cross-validation in the context of the first usage.
-   **Required Fix:** To improve clarity and precision, the authors must use distinct terminology. The DESI test should be referred to as "5-fold cross-validation". The eROSITA/Gaia test should be described more accurately, for example, as a "resampling stability test" or "bootstrap stability test". This change should be applied consistently throughout the manuscript, including in the abstract, to avoid misrepresenting the validation performed on the photometric surveys.

---

### MINOR Revisions

**P3-N4: Incorrect Cross-Reference in Abstract**
-   **Section/Page:** Abstract (p. 1).
-   **Problem:** The abstract contains the cross-reference `§VIE` when discussing the size benchmark. No such section exists in the paper. The discussion of the size benchmark against prior work [11] appears in the abstract itself and in the first conclusion point in §VII.
-   **Required Fix:** Remove the incorrect cross-reference `§VIE`.

**P3-N5: Incorrect Cross-Reference in Table I Footnote**
-   **Section/Page:** Table I footnote § (p. 7).
-   **Problem:** The footnote discusses the Isolation Forest cross-validation stability for Gaia and eROSITA and cites `§VID (ii)`. Section VI D (ii) is about injection-recovery synthesis. The correct discussion of the IF stability tests is found in §III E (eROSITA) and §III G (Gaia).
-   **Required Fix:** Correct the cross-reference to point to the appropriate sections (§III E and §III G).