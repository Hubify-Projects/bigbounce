# P3 auto-2026-06-05_1919pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 2406.0s

---

Here is a complete referee report for the submitted manuscript.

***

## Referee Report: "Spectrally Unusual Sources at Scale..."

**To the Editor of Physical Review D,**

I have reviewed the manuscript "Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and Native-Trained Novelty Fractions from 37.3 Million Sources and Map Patches" by Houston Golden. The paper presents a large-scale anomaly detection analysis across seven astronomical surveys, resulting in a catalog of nearly 400,000 unusual sources. The work details a "Path-C" methodology emphasizing native retraining to overcome cross-survey domain shift, provides important methodological lessons, and explores cosmological applications using the new catalog, including constraints on primordial non-Gaussianity (fNL) and consistency checks with matter-bounce cosmology.

The scale of the analysis is impressive and represents a significant contribution to the field of astronomical anomaly detection. The methodological insights, particularly the explicit demonstration of cross-transfer failure modes (e.g., for SDSS and LAMOST) and the validation of the native-retraining solution, are valuable for the community. The cosmological applications, while preliminary, demonstrate the scientific potential of the resulting catalog.

However, the manuscript requires significant revision before it can be considered for publication in Physical Review D. I have identified a numerical error in a headline cosmological result, unacceptable use of future-dated references, and several instances of unclear presentation and internal-review language that must be addressed. My detailed findings are listed below.

---

### Detailed Findings

#### ESSENTIAL

**P3-E1**
*   **Section:** Abstract (p. 1) and V.b (p. 10)
*   **Problem:** There is a numerical error in a headline cosmological result. The abstract states: "a central forecast σ(fNL) = 8.14 with 1σ envelope [3.92, 8.98] (7.9% improvement consistent with no improvement at <1σ; σ(fNL)std = 8.98 single-tracer baseline)." The main text repeats the "7.9% improvement" claim. However, a direct calculation of the fractional improvement in the constraint yields (8.98 - 8.14) / 8.98 = 0.0935, which is a **9.4%** improvement, not 7.9%. This error appears in both the abstract and the main body and must be corrected.
*   **Fix:** Recompute the percentage improvement and correct the value in the abstract and Section V.b. Verify that the interpretation (e.g., "<1σ significance") remains valid after the correction.

**P3-E2**
*   **Section:** References (p. 19)
*   **Problem:** The manuscript cites key future-dated works as if they are already published. Specifically, "[1] DESI Collaboration, 'The DESI Data Release 1,' 2025" and "[12] C. Nicolaou et al., 'Anomaly Detection in DESI Early Data Release Spectra with Astronomaly,' Mon. Not. Roy. Astron. Soc. (2026, in press)." A manuscript submitted for publication cannot rely on references that do not yet exist.
*   **Fix:** Replace these citations with the most up-to-date public references available at the time of revision (e.g., an arXiv preprint, a technical note, or a conference proceeding). If no public reference exists, the claims supported by these citations must be presented as preliminary and dependent on forthcoming data/work.

#### MAJOR

**P3-M1**
*   **Section:** Table I (p. 7)
*   **Problem:** The structure of Table I is highly confusing. The main rows of the table present anomaly counts (`Nanom`) from the initial, superseded "cross-transfer" analysis, which the paper demonstrates is flawed. The final, canonical results from the "Path-C native-retrained" analysis are only presented in a summary row at the bottom and in the footnotes. This buries the headline results and foregrounds the diagnostic/rejected ones.
*   **Fix:** Restructure Table I to be clearer. The main rows should present the final, canonical Path-C anomaly counts for each survey. The superseded cross-transfer counts should be moved to a separate column labeled "Cross-transfer baseline (diagnostic)" or removed from the table and discussed only in the text.

**P3-M2**
*   **Section:** Table IV (p. 13)
*   **Problem:** Table IV, "Path-C residual caveats," is presented as a list of bullet points in a two-column "Headline result" / "Resolution" format. This reads like an internal document or a response to a previous review rather than a formal part of a scientific paper. The content is valuable but the format is inappropriate. For example, item (j) "GS corrected: ...; prior ±7.43 dropped" is cryptic.
*   **Fix:** Rewrite the content of Table IV as a proper prose subsection within the Discussion (Section VI). Each point should be explained clearly in a full paragraph, avoiding jargon and abbreviated phrasing.

**P3-M3**
*   **Section:** Throughout (e.g., Abstract, §III.D, §III.G)
*   **Problem:** The catalogs for three surveys (LAMOST, Gaia, eROSITA) are acknowledged to fail the paper's own injection-recovery validation gates. While the author is transparent about this, the decision to include these "failed" catalogs in the main data release, even as "exploratory tiers," is questionable and weakens the overall rigor of the final product. The abstract correctly recommends a "catalog-grade subset," but the paper could do more to firewall these less reliable results.
*   **Fix:** Strengthen the justification for releasing these catalogs. Throughout the paper, be more explicit and consistent in warning the reader about the limitations of these specific sub-catalogs. Consider moving the detailed analysis of the failed-validation surveys to an appendix to clearly separate them from the robust, "PASS"-grade catalogs.

**P3-M4**
*   **Section:** References (p. 19), Table I (p. 7)
*   **Problem:** The manuscript contains internal bookkeeping language not suitable for publication.
    1.  Reference [33]: The entry includes the note "[publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity]".
    2.  Table I, footnote `¶`: The text includes "The earlier 'strict subset' framing is replaced with this exact 284/298 = 95.3% overlap."
*   **Fix:** Remove all such internal-facing comments, version history notes, and review-process artifacts from the manuscript. The text should be written for the final reader, not for the author or a reviewer.

#### MINOR

**P3-m1**
*   **Section:** VI.D (i) (p. 12)
*   **Problem:** The first paragraph of this subsection is a non-sequitur. It begins by discussing the "DESI in-sample training-test overlap" and the Jaccard stability results, but then abruptly pivots to the mathematical form of the Fisher forecast for fNL ("Fisher positivity-respecting form..."). These are two completely unrelated topics.
*   **Fix:** Separate these two points into distinct, logically-cohesive paragraphs or list items.

**P3-m2**
*   **Section:** II.D (p. 3), Table III (p. 8)
*   **Problem:** Several phrases are unclear or use undefined jargon.
    1.  §II.D: "production-vs-5-seed-control Jaccard". The term "5-seed-control" is not defined.
    2.  Table III caption: "IF raw scores are not a parallel catalog axis". The meaning of this phrase is obscure.
*   **Fix:** Define "5-seed-control" or rephrase to be understandable (e.g., "Jaccard index between the production model and an ensemble of five models trained with different random seeds"). Rephrase the Table III caption to clearly explain the relationship between the two reported scores.

**P3-m3**
*   **Section:** Figure 1 (p. 4)
*   **Problem:** The figure shows the "Cross-transfer baseline map," which is a diagnostic result from a superseded analysis. While useful for illustrating the "before" state, the caption and title could be clearer that this does not represent the spatial distribution of the final, canonical catalog.
*   **Fix:** Add a sentence to the beginning of the caption explicitly stating this, for example: "This figure shows the spatial distribution of the initial cross-transfer anomaly set, which is preserved as a diagnostic. It does not represent the final 378,280 unique anomalies from the Path-C rebuild."

**P3-m4**
*   **Section:** V.c (p. 10)
*   **Problem:** The text claims that GR projection corrections contribute "|Δσ/σ| < 0.02% at kmax = 0.2 h Mpc⁻¹" and cites §VID(e). However, Table IV on p. 13 is §VID, and item (e) simply states the result without derivation or a reference to a standard calculation. For a PRD paper, this claim should be substantiated.
*   **Fix:** Provide a brief justification for this number, either with a back-of-the-envelope calculation or by citing a standard reference that computes the magnitude of these effects (e.g., Yoo et al. 2009, Bonvin & Durrer 2011, Challinor & Lewis 2011).

#### NIT

**P3-N1**
*   **Section:** Title page (p. 1)
*   **Problem:** The paper is dated "June 2026".
*   **Fix:** Correct the date to the month and year of submission.

---

### Summary recommendation

**MAJOR REVISIONS**

This manuscript presents a scientifically valuable and large-scale effort in anomaly detection with clear potential for astrophysical and cosmological discovery. The core methodology is sound, and the author's transparency regarding methodological failures and limitations is commendable. However, the work is marred by a significant numerical error in a headline result, the use of improper future-dated references, and several instances of poor presentation that obscure the paper's strengths. These issues, particularly the first two, are critical and must be thoroughly addressed. Once these revisions are made, the paper will represent a strong and important contribution suitable for publication in Physical Review D.