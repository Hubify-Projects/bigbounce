# P3 EXT20 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=62d7b294 pages=30
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (2815 chars)
**Wall time**: 173.4s

---

## Referee Report for Manuscript P3

**To the Editor of Physical Review D,**

This manuscript presents a large-scale, multi-survey catalog of astronomical anomalies detected using an autoencoder framework. The authors apply their method to 37.3 million sources from seven astronomical archives (DESI, SDSS, LAMOST, eROSITA, Planck, Gaia, NEOWISE), producing a final catalog of 378,280 unique anomalies. The paper details the methodology, including a "Path-C" native-retraining protocol designed to overcome cross-survey domain shifts, and presents several validation tests. The catalog is then applied to two cosmological problems: constraining primordial non-Gaussianity (fNL) and testing consistency with matter-bounce models via NANOGrav data.

The scale of the undertaking is impressive, and the resulting catalog is a potentially valuable community resource. The authors are commendably transparent about numerous methodological challenges, limitations, and outright failures for certain survey-specific tiers of the catalog. This level of self-criticism is laudable.

However, the manuscript suffers from several significant issues in its current form, including two essential-level reproducibility failures and major problems with methodological clarity and presentation. These issues must be thoroughly addressed before the paper can be considered for publication in Physical Review D.

Below is a detailed list of required revisions.

---

### ESSENTIAL Revisions

These issues must be resolved for the paper to be publishable.

*   **ID: P3-E1**
    *   **Section/Page:** §IIB (p. 3), §VID (p. 20), Acknowledgments (p. 23)
    *   **Problem:** The paper states multiple times that the exact preprocessing script for the Gaia DR3 data was not recovered and that the specification is "lineage-inferred" from a successor script. This is a critical failure of scientific provenance. A core data product of this paper—the Gaia anomaly list—is not reproducible from its stated inputs.
    *   **Required Fix:** The authors must add a dedicated paragraph in the main text (e.g., in the Gaia results section §IIG or the Limitations §VIC) explicitly stating the consequences of this failure. This includes a statement that the Gaia anomaly ranks and scores cannot be independently reproduced and should be treated as a static, one-off data product. The abstract's description of the Gaia tier should also reflect this limitation more strongly.

*   **ID: P3-E2**
    *   **Section/Page:** Abstract (p. 1), §IIIE (p. 11), §IIIF (p. 12)
    *   **Problem:** The paper reports that the anomaly score axis for the eROSITA tier is "unrecoverable as a matter of provenance" and that "no committed score axis reproduces the production threshold." The only reproducible product is the static top-298 membership list. This is another severe reproducibility failure.
    *   **Required Fix:** While the paper is transparent about this, the implications must be made even clearer. The authors must state explicitly that any downstream scientific analysis that requires eROSITA anomaly *scores* (e.g., score-weighted stacking, analysis of the score distribution, selection of a different threshold) is impossible with this data product. This limitation is significant enough to warrant a more prominent warning in the main eROSITA results section (§IIIE).

### MAJOR Revisions

These represent significant flaws that require substantial revision.

*   **ID: P3-M1**
    *   **Section/Page:** §IIB (p. 3)
    *   **Problem:** The feature scalers for the tabular surveys (eROSITA, NEOWISE, Gaia) were fit on the full dataset, not just the training split. This constitutes data leakage from the validation set into the training process. The paper's own robustness check for eROSITA reveals a ~15-17% membership churn in the extreme tail, which is a non-negligible effect.
    *   **Required Fix:** The claim that "per-survey rates and within-survey rankings are robust to the scaler choice" (p. 4) is too strong. This claim must be qualified with the measured ~15-17% instability. The authors should explicitly state that the reported rankings for these surveys carry this quantified uncertainty. The recommendation for future work is correct, but the impact on the present work must be accurately reported.

*   **ID: P3-M2**
    *   **Section/Page:** Throughout, especially §III (p. 6), Fig. 2 caption (p. 7), Table I (p. 9)
    *   **Problem:** The presentation of anomaly counts is extremely confusing. The text and tables weave between the initial cross-transfer baseline (e.g., 319,443 total), the sum of per-survey native-retrained tallies (388,493), and the final deduplicated unique-object catalog (378,280). The structure of Table I and the caption of Figure 2 are particularly convoluted and difficult to parse.
    *   **Required Fix:** The authors must substantially revise the presentation of these numbers.
        1.  Table I should be restructured with distinct, clearly labeled columns for "Initial Cross-Transfer" and "Final Path-C Native" counts for each survey.
        2.  A flowchart or diagram should be added to the Methods section (§IID) visually explaining the data flow: from the initial per-survey source counts, to the cross-transfer scan, to the native retrains, to the sum of native catalogs, and finally to the deduplicated unique catalog. This would greatly improve clarity.

*   **ID: P3-M3**
    *   **Section/Page:** §IIIH (p. 13), §VID(ii) (p. 20), Fig. 10 (p. 22)
    *   **Problem:** The NEOWISE injection-recovery test is labeled "PASS" alongside genuine detector sensitivity tests for other surveys. However, the text correctly clarifies that this test "passes by construction" and is merely a "masking-geometry sanity check," not a test of sensitivity to finding new sources. This labeling is misleading.
    *   **Required Fix:** A test that passes by construction is not a validation test in the same sense as the others. The authors must use a distinct label for this result throughout the paper, such as "PASS (QA)" or "GEOMETRY-VALIDATED". In Figure 10, the NEOWISE result should be plotted with a different line style or symbol to visually distinguish it from the true sensitivity tests.

*   **ID: P3-M4**
    *   **Section/Page:** Appendix C, Fig. 11 (p. 25)
    *   **Problem:** Figure 11, which shows the shot-noise sensitivity of the fNL forecast, uses an internal normalization for σ(fNL) that is explicitly stated to be non-comparable to the primary forecast in the main text (§V). Presenting absolute σ(fNL) values on the y-axis is therefore confusing and potentially misleading, despite the caption's warning.
    *   **Required Fix:** To avoid any ambiguity, the y-axis of Figure 11 should be changed from the absolute σ(fNL) to a relative quantity whose interpretation is independent of the baseline normalization, such as "Fractional Improvement in σ(fNL)" or "σ(fNL) / σ(fNL, single-tracer)". This makes the physical point of the plot (the degradation due to shot noise) clear without requiring the reader to parse complex normalization notes.

### MINOR Revisions

These issues should be addressed to improve the quality of the manuscript.

*   **ID: P3-m1**
    *   **Section/Page:** §V (p. 18), Fig. 9 (p. 19)
    *   **Problem:** The primary cosmological result is that the empirically measured tracer bias is consistent with null, leading to no multi-tracer improvement for fNL. However, Figure 9 and Appendix C are dedicated to a fixed-bias forecast (a=0.15) that *does* show a hypothetical improvement. This gives undue prominence to a scenario that is not supported by the paper's own analysis.
    *   **Required Fix:** De-emphasize the fixed-bias scenario. Move Figure 9 into Appendix C with the rest of the fixed-bias discussion. The main text should focus squarely on the primary, empirically-derived null result.

*   **ID: P3-m2**
    *   **Section/Page:** §V C (p. 18)
    *   **Problem:** The paper bounds the impact of general-relativistic projection corrections on the fNL forecast as an "internal order-of-magnitude bound," which is not sufficiently rigorous for PRD.
    *   **Required Fix:** Strengthen this bound by providing a brief, explicit calculation referencing the standard literature (e.g., Bonvin & Durrer, 2011; Challinor & Lewis, 2011, which are already cited as [39, 40]) to show how the effect scales with k and why it is sub-percent for the Fisher-weighted scales relevant to the analysis.

*   **ID: P3-m3**
    *   **Section/Page:** Fig. 10 (p. 22)
    *   **Problem:** As a supplement to the fix for P3-M3, the NEOWISE curve in Figure 10 should be made visually distinct from the other curves to reflect its nature as a QA check rather than a sensitivity test.
    *   **Required Fix:** Use a different line style (e.g., dashed or dotted) and/or a different marker for the NEOWISE data in Figure 10. Add a note to the legend clarifying the distinction.

### NIT-PICKS

*   **ID: P3-N1:** The date on page 1 is a future date ("June 18, 2026"). This should be corrected.
*   **ID: P3-N2:** On page 2, the section reference "§II A-§IID" contains a space and should be "§IIA-§IID".
*   **ID: P3-N3:** On page 5, the ecliptic latitude mask "becl < 80°" should be written as "|b_ecl| < 80°" to be unambiguous.

---

## Summary recommendation

**MAJOR REVISIONS**

This manuscript reports on a very significant effort to create a large and novel anomaly catalog. The scientific potential is high, and the authors' transparency regarding the catalog's many warts and caveats is a major strength. However, the paper is marred by critical, acknowledged failures in scientific provenance for the Gaia and eROSITA tiers, which are not yet framed with sufficient gravity. Furthermore, major revisions are needed to clarify the complex data flow and anomaly counts, to correct a methodologically flawed data-leakage step, and to avoid misleading labeling of validation tests.

The work is substantial and likely publishable in PRD after these issues are addressed. The authors have already done most of the hard work of identifying the problems; they now need to revise the manuscript to present those problems and their consequences with the clarity and rigor that the journal requires.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from a second, more rigorous review of the manuscript.

---
### ADDITIONAL FINDINGS (Second Pass)

*   **ID: P3-m5**
    *   **Section/Page:** §III A (p. 7)
    *   **Problem:** An arithmetic error exists in a reported statistical uncertainty. The paper reports the per-class anomaly rate for GALAXY-type spectra as "0.75% ± 0.02% (Wilson 95% binomial CIs)". A re-calculation of the Wilson score interval for the given rate (0.75%) and sample size (~4.9 million) yields a 95% confidence interval of approximately [0.742%, 0.758%], corresponding to an uncertainty of ±0.008%. The reported uncertainty of ±0.02% is more than double the correct value. In contrast, the uncertainty for the QSO rate on the next line is calculated correctly.
    *   **Required Fix:** The authors must re-calculate the Wilson 95% confidence interval for the GALAXY anomaly rate and correct the reported uncertainty in the text.

*   **ID: P3-m6**
    *   **Section/Page:** Table V (p. 21)
    *   **Problem:** The cross-reference in Table V, row (g) is incorrect and confusing. The row summarizes the DESI 5-fold Jaccard stability result ("J = 0.862 >= 0.70 gate"). The "Resolution" column cites "§III E; Table I footnotes". However, the Jaccard stability analysis is detailed in §VID(i). Section §IIIE and the Table I footnotes discuss anomaly *thresholds*, which are a separate topic. The table entry appears to conflate two distinct validation checks.
    *   **Required Fix:** Correct the reference in the "Resolution" column for row (g) to point to the correct section, §VID(i).

*   **ID: P3-N4**
    *   **Section/Page:** §IID (p. 5), Fig. 6 caption (p. 14)
    *   **Problem:** The manuscript contains a recurring typographical error in a section reference. On page 5, the text refers to the cross-transfer verification baseline being preserved in "§VIA". In the caption for Figure 6 on page 14, the LAMOST training-bias artifact is also referenced as being in "§VIA". There is no Section VI.A in the manuscript; the section is simply numbered VI. The intended reference is almost certainly to Section VI.A, "The LAMOST Training-Bias Lesson".
    *   **Required Fix:** Correct all instances of the reference "§VIA" to "§VI.A".

*   **ID: P3-N5**
    *   **Section/Page:** Table V (p. 21)
    *   **Problem:** The cross-reference in Table V, row (b) is too vague. The row describes the DESI out-of-distribution (OOD) validation result, and the "Resolution" column states it was "reconciled in §II". Section II is the entire methods section. The specific discussion of the OOD reconciliation and the "catalog-curation effect" appears at the end of §II.C.
    *   **Required Fix:** Make the reference in the "Resolution" column for row (b) more specific, pointing to the relevant paragraph in §II.C.