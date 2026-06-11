# P3 R29 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.88.pdf` md5=bbc52726 pages=26
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 170.4s

---

## Referee Report: "Spectrally Unusual Sources at Scale..."

This paper presents a large-scale search for anomalous astronomical sources across seven major surveys using an autoencoder framework. The authors construct a catalog of over 378,000 unique anomalies, perform extensive internal validation and cross-survey analysis, and explore cosmological applications using the new catalog as a source of high-bias tracers for primordial non-Gaussianity and for consistency checks with NANOGrav results.

The work is impressive in its scale, methodological rigor, and transparency. The authors are commendably forthright about the limitations of their analysis, the validation failures for certain survey subsets, and the null results of their cosmological applications. The paper is well-structured, and the level of detail provided for reproducibility is generally excellent.

However, several revisions are required before the paper can be considered for publication in Physical Review D. The findings are categorized below.

### ESSENTIAL

**P3-E1: Removal of Internal Versioning and Draft-History Language**
*   **Location:** Abstract (p. 1), Section IV B (p. 12)
*   **Problem:** The manuscript contains language referring to previous versions or internal development artifacts. This is inappropriate for a final publication.
    *   Abstract: "an earlier draft quoted 264,938/264,738 from headline-minus-LAMOST subtraction arithmetic, which double-removes the 4,379 LAMOST detections..."
    *   Section IV B: "An earlier draft quoted 38,330 pixels with x²ᵥ = 3.76; that artifact's pixel-selection and variance model could not be recovered from the committed analysis tree, and the figure is withdrawn in favor of the reproducible recompute above."
*   **Fix:** Remove all such sentences. The paper should present the final, self-contained results without reference to its own development history.

**P3-E2: Incorrect Submission Date**
*   **Location:** Title block (p. 1)
*   **Problem:** The paper is dated "June 2026".
*   **Fix:** Correct the date to the actual submission date.

### MAJOR

**P3-M1: Clarification of Contradictory Validation Metric**
*   **Location:** Section III E (p. 8)
*   **Problem:** The text describes the eROSITA validation as "XV-stability 81.5% (gate FAIL at 5σ subspace injection, but highest XV-stability of any Path-C survey)." This statement is confusing and appears contradictory. If the result constitutes a gate failure, it is unclear how it can also be the "highest" or what that implies. The reader is left wondering if the gate threshold is poorly chosen or if all other surveys performed even more poorly on this specific, non-standard metric.
*   **Fix:** The authors must clarify this point. Explain why the 81.5% result fails the gate (i.e., state the threshold). Then, explain the context of it being the "highest" value. If this "XV-stability" metric is not one of the formal gates defined in Section II D, it should be presented separately and its relevance justified. The current phrasing undermines the credibility of the validation framework.

### MINOR

**P3-m1: Abstract Emphasis on Cosmological Result**
*   **Location:** Abstract (p. 1) and Section V (p. 15) / Section VII (p. 19)
*   **Problem:** The abstract states the fNL forecast as: "the de-biased point estimate returns the single-tracer baseline ... the central forecast (fNL)σ = 8.14 ... the central 9.4% improvement is a noise-driven forecast pending higher-S/N follow-up, not a detection." While technically correct, this phrasing leads with an optimistic "central forecast" and "9.4% improvement" that the body of the paper rigorously demonstrates is not a statistically significant result. The main conclusion, correctly stated in Section VII, is that the de-biased estimate "returns the single-tracer baseline exactly (no improvement at current S/N)".
*   **Fix:** Rephrase the abstract to align with the more sober conclusion in the main text. It should lead with the de-biased null result and then explain that the central-value improvement is a statistically insignificant, noise-driven artifact of the calculation at current S/N.

**P3-m2: Removal of Internal Jargon and Bookkeeping Notes**
*   **Location:** Section II B (p. 3), Section III B (p. 6), Section VI D (p. 18)
*   **Problem:** The paper contains minor instances of internal jargon or bookkeeping notes that are not relevant to the reader.
    *   p. 3: "...byte-identical copies in two independent pod backups..."
    *   p. 6: "...printed as "AE" for legacy compatibility..."
    *   p. 18: "...the headline "3 PASS" shorthand always carries this decomposition where it appears."
*   **Fix:** Rephrase these sentences to be clear to an external audience without using internal shorthand or referring to data backup strategies. For example, instead of "AE for legacy compatibility," simply define the `rz` symbol and use it consistently.

### NIT

**P3-N1: Table I Footnote Marker**
*   **Location:** Table I (p. 9)
*   **Problem:** The footnote marker '§' on the eROSITA DR1 anomaly count (298) appears misplaced. The corresponding footnote text discusses Isolation Forest cross-validation for both Gaia and eROSITA, but the marker is only on the eROSITA line.
*   **Fix:** Review the placement of this footnote marker to ensure it correctly applies to all intended entries.

## Summary recommendation

**MAJOR REVISIONS**

This is a high-quality, comprehensive paper that represents a significant effort in the area of anomaly detection. The scientific analysis is rigorous, and the authors' commitment to transparency is exemplary. The cosmological applications are well-executed and their null results are interpreted with appropriate caution. The paper is a strong candidate for publication in PRD.

However, the ESSENTIAL revisions to remove internal versioning language and correct the date are non-negotiable for a professional publication. The MAJOR revision is required to clarify a confusing and seemingly contradictory validation claim that could undermine confidence in the results. Once these points are addressed, the paper should be suitable for publication after a final check.