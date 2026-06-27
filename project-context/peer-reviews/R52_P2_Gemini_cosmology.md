# P2 R52 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/site/public/papers/paper2_fnl_forecast_v1.7.70.pdf` md5=99e6426c pages=29
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 164.2s

---

**Referee Report for Manuscript [Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook]**

This paper presents a detailed sensitivity forecast for testing the matter bounce cosmological scenario using primordial non-Gaussianity (PNG) measurements from the upcoming SPHEREx survey and the proposed MegaMapper project. The author recasts existing forecasts for local-type PNG to the specific, non-perfectly-local bispectrum shape predicted by the quasi-dust matter bounce model (`f_NL = -35/8`). The analysis is exceptionally thorough, addressing subtle but important issues including theoretical uncertainties in the prediction, template mismatch, observational systematics, and the statistical framework for model comparison.

The primary contributions of the paper are:
1.  A resolution of a factor-of-two discrepancy in the literature regarding the predicted value of `f_NL`, which the author convincingly argues is `-35/8` in the standard Planck convention by tracing it to a missing time-ordering in one of the calculations.
2.  A novel analysis of the "polynomial null space" arising from the underdetermined nature of the bispectrum shape function, quantifying this as a new source of theoretical uncertainty (`r = 0.85 ± 0.13`).
3.  A comprehensive propagation of all identified uncertainties—including template mismatch (`r ≈ 0.84`), systematic effects (relativistic projections, PNG bias uncertainty), and theoretical ambiguities—into a consolidated forecast for SPHEREx.
4.  A detailed Bayesian model comparison to quantify the discriminating power of SPHEREx between the matter bounce and various inflationary alternatives.

The paper is well-structured, clearly written, and methodologically sound. The level of rigor and transparency is exemplary, with all assumptions clearly stated and all calculations meticulously documented. The provision of analysis scripts for reproducibility is commendable. The paper represents a significant and timely contribution to the field. I recommend publication in Physical Review D after the following minor points are addressed.

---
### Detailed Findings

#### MAJOR
**P2-M1: Potential for misinterpretation of the LSS noise weighting argument**
*   **Section/Page**: III B, page 8
*   **Problem**: The text argues that the template overlap `r` drops for LSS surveys "because noise in LSS surveys is concentrated at large scales where the bounce template departs most from the local shape." This phrasing is potentially confusing. The local template is defined by the squeezed limit, which is the limit of large scale separation. The bounce template is known to converge to the local template in this exact limit. The departure is largest for non-squeezed (e.g., equilateral or folded) configurations. The current wording could incorrectly suggest to a reader that the point-wise mismatch is largest on the largest scales. The intended argument—that the *integrated* mismatch is larger under an LSS-appropriate Fisher weighting—is physically correct but could be stated more precisely.
*   **Required fix**: Please rephrase this sentence to avoid ambiguity. A clearer statement might be: "Under realistic noise weighting for LSS surveys, which gives more weight to larger-scale modes than CMB-weighting, the integrated template mismatch across all triangle shapes is larger, causing the overlap to drop to r ≈ 0.83. While the two templates coincide in the exact squeezed limit, the contribution to the total signal-to-noise from non-squeezed configurations, where the templates differ significantly, is substantial, leading to a lower overall amplitude recovery."

#### MINOR
**P2-N1: Future dating of mission milestones**
*   **Section/Page**: Abstract, page 1
*   **Problem**: The paper is dated June 18, 2026, but refers to the SPHEREx launch in the past tense ("launched March 2025"). While this is a forecast paper, this style can be slightly jarring in an archival publication.
*   **Required fix**: This is a stylistic suggestion. Consider rephrasing to be more neutral with respect to the paper's date, for example: "We forecast tests of this prediction with SPHEREx (scheduled for launch in March 2025...)" or similar.

**P2-N2: Inconsistent symbol for PNG bias parameter**
*   **Section/Page**: Table IV caption, page 20
*   **Problem**: The caption uses the symbol `bφ` for the PNG bias parameter, whereas the main text consistently uses `b_φ`.
*   **Required fix**: Please use the consistent symbol `b_φ` in the caption for clarity.

**P2-N3: Placeholder for Zenodo DOI**
*   **Section/Page**: X, Data and Code Availability, page 24
*   **Problem**: The text contains the placeholder "(DOI inserted at submission)".
*   **Required fix**: Please ensure the final DOI for the archived data and code is inserted before publication.

#### NIT
**P2-N4: Unconventional author email address**
*   **Section/Page**: I, page 2 (footnote)
*   **Problem**: The corresponding author's email address, `houston@hubify.com`, is non-institutional. This is unusual for a publication in Physical Review D.
*   **Required fix**: No change is required on scientific grounds, but the author and editor may wish to consider if a more permanent, institutional contact is appropriate.

---
## Summary recommendation
**ACCEPT WITH MINOR CORRECTIONS**

This is an excellent paper of high quality and impact. It provides a definitive forecast for a key, testable prediction of matter bounce cosmology, while simultaneously clarifying important theoretical points and setting a high standard for methodological transparency and reproducibility. The requested revisions are minor and primarily aimed at improving clarity on one point. The work is a valuable contribution and is well-suited for publication in Physical Review D.