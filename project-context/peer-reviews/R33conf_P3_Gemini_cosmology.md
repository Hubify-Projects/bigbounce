# P3 R33conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.94.pdf` md5=f3bb1c93 pages=28
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 141.2s

---

## Referee Report: "Spectrally Unusual Sources at Scale..."

This paper presents a large-scale anomaly detection campaign across seven major astronomical surveys, resulting in a catalog of 378,280 unique anomalies. The core of the work is the application of a "Path-C" native retraining and validation protocol to mitigate artifacts arising from cross-survey model application. The paper details the methodology, presents survey-by-survey results, analyzes cross-survey coincidences, and explores secondary cosmological applications related to primordial non-Gaussianity (f_NL) and the stochastic gravitational-wave background.

The scale of the catalog and the methodological lessons learned from the multi-survey approach, particularly regarding training-set bias (LAMOST) and domain shift (SDSS), represent a significant contribution to the field of astronomical data mining. The authors are commendably transparent about the limitations of their methods, reproducibility issues (e.g., for the eROSITA score axis), and the interpretation of their results.

However, several revisions are required before the paper can be considered for publication in Physical Review D. The most critical issue is a lack of clarity and consistency between the abstract and the main text regarding a key cosmological result (the f_NL forecast). Additionally, several instances of internal version-history language must be removed, and key technical details need to be clarified for reproducibility and verification.

### ESSENTIAL Revisions

**P3-E1: Abstract-Body Inconsistency on f_NL Forecast (Pattern-045)**
*   **Section/Page:** Abstract, p. 1; Section V, p. 17.
*   **Problem:** The abstract presents the f_NL forecast in a confusing and potentially misleading sequence. It states: "the de-biased point estimate returns the single-tracer baseline (fNL)std = 8.98 exactly (no multi-tracer improvement at current S/N); inserting the noisy â into the Fisher-positivity-respecting form ... gives a central forecast σ(fNL) = 8.14". This juxtaposition implies a detection or a robust improvement, which is immediately contradicted by the parenthetical "(no multi-tracer improvement)". The main text in Section V, p. 17, correctly clarifies that the 8.14 value is an optimistic, noise-biased forecast and that "the propagated envelope [3.92, 8.98] — not the convex central value — is the appropriate summary of the present constraint," which is consistent with no improvement. The abstract, as the most visible part of the paper, must reflect the robust conclusion from the body.
*   **Required Fix:** Rewrite the f_NL portion of the abstract to match the conclusion of the main text. It should state clearly that the analysis is consistent with no multi-tracer improvement at the current signal-to-noise. The biased central forecast should be de-emphasized or removed from the abstract entirely in favor of the robust conclusion based on the de-biased estimate and the uncertainty envelope.

**P3-E2: Removal of Internal Version-History Language**
*   **Section/Page:** Abstract, p. 1; Table VI footnote, p. 23.
*   **Problem:** The manuscript contains language that refers to its own revision history, which is inappropriate for a final publication.
    1.  Abstract, p. 1: "an earlier draft quoted 264,938/264,738 from headline-minus-LAMOST subtraction arithmetic..."
    2.  Table VI footnote, p. 23: "an earlier draft listed 10.6 s, which is inconsistent with a ~100-epoch convolutional run and has been withdrawn."
*   **Required Fix:** Remove all such references to "earlier drafts," "withdrawn" values, or other internal development history from the manuscript. The paper should present the final, self-consistent results without discussing its own evolution.

**P3-E3: Incorrect Publication Date**
*   **Section/Page:** Title block, p. 1.
*   **Problem:** The paper is dated "(Dated: June 2026)".
*   **Required Fix:** Correct the date to the current submission date.

### MAJOR Revisions

**P3-M1: Missing Value for Calculation Verification**
*   **Section/Page:** Section II D, p. 4.
*   **Problem:** The text states: "For DESI DR1, µval ≈ 0.0287 (validation MSE); the measured (µval, σval) place the S > 5 catalog threshold at MSE ≈ 0.143 on the rescaled scale." The canonical score is defined in Eq. (2) as S = (MSE - µ_val) / σ_val. To verify that S=5 corresponds to MSE=0.143, the value of σ_val is required. This value is not provided.
*   **Required Fix:** State the value of σ_val for the DESI DR1 validation set alongside µ_val to make the calculation verifiable.

**P3-M2: Ambiguous "Display Score" in Figure Caption**
*   **Section/Page:** Figure 8 Caption, p. 16.
*   **Problem:** The caption states: "the burned-in 'Score' annotations are display values from that script rather than catalog-pipeline outputs; in particular, the panel (a, b) annotations (3.2, 2.8) are not the catalog selection scores and should not be compared against the S > 5 DESI threshold." This is confusing and undermines the figure's utility. If the scores shown are not the official catalog scores, it raises questions about reproducibility and consistency. Why are the catalog scores not used? If there is a good reason, it must be explained.
*   **Required Fix:** Either replace the "display scores" with the actual, final canonical scores from the released catalog for these objects, or provide a clear and compelling justification for why a different, non-catalog score is being displayed and how it relates to the official one.

### MINOR Revisions

**P3-m1: Unnecessary Internal Process Details**
*   **Section/Page:** Section II B a, p. 3.
*   **Problem:** The text contains details about the software development and data backup process that are not relevant to the scientific content of the paper. For example: "byte-identical copies in two independent pod backups" and "the exact 20-feature production script for the published 50K-source run was not recovered from any committed backup". While the transparency is noted, this level of detail is better suited for a data release paper or technical documentation.
*   **Required Fix:** Rephrase these sections to focus on the methodological specifications themselves, rather than the process of how they were recovered or backed up. For the Gaia script, simply state that the specification is inferred from a closely related, available script, as is already done in the Data Availability section.

**P3-m2: Ambiguous Novelty Fraction Denominator in Figure**
*   **Section/Page:** Figure 6 Caption, p. 13.
*   **Problem:** The caption states the aggregate 58.8% SIMBAD-unmatched fraction is "pooled over the top-100 anomalies of four surveys... DESI and LAMOST excluded from the pooled denominator." This is a crucial detail that is easy to miss. A reader might incorrectly assume the 58.8% applies to all surveys shown in the figure.
*   **Required Fix:** Make the exclusion of DESI and LAMOST from the aggregate value more prominent in the caption, perhaps by stating it in the first sentence describing the dashed line.

**P3-m3: Awkward Summation Notation**
*   **Section/Page:** Section I, p. 2.
*   **Problem:** The text uses the notation "catalog counts appear as 378,080+200= 378,280". This is an unconventional way to present a breakdown.
*   **Required Fix:** Rephrase to something standard, e.g., "...for a total of 378,280 anomalies, consisting of 378,080 point-source detections and 200 CMB map-patch sky-regions."

### NITs (Cosmetic)

**P3-N1: Section Number as Noun**
*   **Section/Page:** Throughout, e.g., p. 2, "motivating the Path-C native-retrain rebuild (§IID)".
*   **Problem:** Using section numbers directly as nouns (e.g., "see §IID") can be stylistically jarring.
*   **Required Fix:** Consider changing to "see Sec. IID" or similar, for improved readability, though this is a journal style preference.

**P3-N2: Internal Artifact Filename**
*   **Section/Page:** Section E, p. 10.
*   **Problem:** The text mentions an internal artifact filename: "(artifact r24conf_erosita_axis_sweep.json)".
*   **Required Fix:** While pointing to reproducibility artifacts is good, this should be handled through the main data availability statement. In the text, it is better to describe the analysis (e.g., "as documented in the companion data repository") rather than citing a specific internal filename.

## Summary recommendation
**MAJOR REVISIONS**

This paper presents a valuable, large-scale anomaly catalog and important methodological insights for unsupervised learning in astronomy. The work is thorough, and the authors' commitment to transparency regarding the many caveats and limitations is a major strength. However, the lack of clarity in the abstract regarding the main cosmological forecast is a significant flaw that must be corrected. Once the abstract is brought into alignment with the more nuanced and statistically robust conclusions in the main text, and the other major/essential points are addressed, the paper will be a strong candidate for publication.