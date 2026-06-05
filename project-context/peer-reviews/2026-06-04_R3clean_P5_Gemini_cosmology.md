# P5 2026-06-04_R3clean — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 63.6s

---

## Referee Report on Paper P5

**Paper:** Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with V-Web Cross-Check Across 791,635 DR1 Matched Spirals
**Round:** 2026-06-04_R3clean

This paper presents a detailed statistical analysis testing for a correlation between the observed chirality of spiral galaxies and their large-scale structure environment, as defined by cosmic voids, walls, filaments, and clusters. The analysis uses a large galaxy chirality catalog (from a companion paper, "Paper IV") cross-matched with the DESI Data Release 1. The primary analysis is anchored on the public DESIVAST void catalog, with a supporting analysis using a V-Web tidal-tensor classification. The headline result is a null detection of any environmental dependence beyond a catalog-wide monopole bias inherited from the input chirality catalog. The analysis is exceptionally thorough, with numerous robustness checks, cross-validations against different classifiers, and a careful treatment of systematics.

While the statistical methodology is rigorous and the author's transparency regarding analysis choices is commendable, there are several issues that require significant revision before the paper can be considered for publication.

---
### Findings

#### ESSENTIAL

*   **P5-E1: Critical dependence on un-peer-reviewed companion work.**
    *   **Location:** Abstract, Sec. I, Sec. II, and throughout.
    *   **Problem:** The entire analysis is critically dependent on inputs from "Paper IV" [3], which is cited as a "companion work, not yet peer-reviewed" or "in preparation". These inputs include the fundamental 8.47M-galaxy chirality catalog and, crucially, the measurement of a catalog-wide monopole offset (∆fCW ≈ −0.0026) which is used to explain the most significant statistical deviations observed in this work. The conclusions of the present paper (P5) are therefore entirely contingent on the validity, methods, and results of an unavailable and un-reviewed manuscript. It is not possible to properly evaluate P5 without access to and confidence in the results of P5.
    *   **Required Fix:** For this paper to be publishable, Paper IV must be made available to the editor and referee. Ideally, Paper IV should be accepted for publication or, at a minimum, be publicly available on a preprint server (e.g., arXiv) so that its methods and results can be scrutinized. The dependency should be clearly stated, and the status of Paper IV must be updated from "in preparation".

#### MAJOR

*   **P5-M1: Inclusion of local file paths and internal pipeline artifacts in the main text.**
    *   **Location:** Throughout the paper. Examples include:
        *   Page 3, Sec III B: "...the fetch + filter driver is pipelines/ p5_desi_chirality/scripts/02_fetch_desi_dr1.py..."
        *   Page 4, Sec V: "Drivers: pipelines/p5_desi_chirality/scripts/ 07_analysis_healpix.py ... and pipelines/p5_desi_chirality/scripts/09_ systematics.py"
        *   Page 17, Sec X: "The cross-match pipeline is at pipelines/p5_desi_chirality/ scripts/15_astra_per_object_crossmatch.py; the result summary at pipelines/p5_desi_chirality/ results/analysis_astra_per_object/summary.json."
    *   **Problem:** The manuscript text is littered with direct references to the author's local file structure and script names. This is unprofessional for a formal publication and makes the paper read like an internal technical note rather than a scientific article. While reproducibility is important, this information belongs in a dedicated code availability statement or appendix, not in the main narrative prose.
    *   **Required Fix:** Remove all such file paths and script names from the main body of the text. Consolidate all information regarding code and data provenance into a dedicated "Data and Code Availability" section or appendix, as is standard practice.

*   **P5-M2: Understatement of Redshift-Space Distortion (RSD) impact on the V-Web analysis.**
    *   **Location:** Sec. XIII (Limitations), p. 18-19.
    *   **Problem:** The author correctly identifies that the V-Web analysis is performed in redshift space and is subject to RSDs. The "Order-of-magnitude boundary-crossing estimate" suggests that 3-5% of galaxies could have their environmental class changed by RSDs. This is a significant fraction that could potentially impact the results. While the author commendably discloses this caveat, the V-Web analysis is still presented as a strong "supporting cross-check". Given the magnitude of the potential systematic, its supporting role is weakened.
    *   **Required Fix:** The text should be revised to more strongly emphasize that the V-Web analysis is illustrative and subject to a significant, unquantified systematic from RSDs. The contrast with the primary DESIVAST analysis, which is argued to be largely RSD-immune, should be sharpened. This will strengthen the paper's core argument by clarifying why the DESIVAST result is the reliable one and the V-Web result is treated with caution.

#### MINOR

*   **P5-m1: Formulation of the toy EFT operator breaks rotational invariance.**
    *   **Location:** Appendix A, p. 19.
    *   **Problem:** The toy operator is written with a term (L̂ · ẑ), which explicitly breaks rotational invariance by picking a preferred direction ẑ. The author correctly points this out in the subsequent "Rotational-invariance and gauge-invariance caveat" and suggests it is shorthand for a properly invariant scalar like L̂ · ∇ρ. However, presenting a formally incorrect operator in the equation itself is confusing and should be avoided.
    *   **Required Fix:** Rewrite the operator in Eq. (A) to be manifestly rotationally invariant from the start (e.g., using L̂ · ∇ρ or another suitable contraction). The explanatory text can then elaborate on the physical meaning of this term.

*   **P5-m2: Lack of specificity on gauge-invariance in the toy EFT operator.**
    *   **Location:** Appendix A, p. 20.
    *   **Problem:** The author correctly notes that the quantities used in the toy operator (like the density field ρ) are not manifestly gauge-invariant. The discussion is good but could be slightly more precise for a theoretical audience.
    *   **Required Fix:** Briefly mention the types of gauge-invariant quantities that would be required in a full, rigorous treatment (e.g., "a fully gauge-invariant formulation would require promoting ∇iρ/ρbg to a gauge-invariant quantity such as the density contrast on comoving hypersurfaces, δ_com..."). This adds precision without requiring a full derivation.

#### NIT

*   **P5-N1: Use of internal paper identifier in the text.**
    *   **Location:** Page 12, Sec. VIII F; Page 13, Table X.
    *   **Problem:** The text refers to the "P5 matched-spiral catalog monopole" and uses "fCW P5" in tables. "P5" appears to be an internal identifier for this paper. This is non-standard and should be rephrased for an external audience.
    *   **Required Fix:** Replace phrases like "P5 matched-spiral catalog monopole" with "the matched-spiral catalog monopole derived in this work" or similar.

*   **P5-N2: Use of a specific future date in the title block.**
    *   **Location:** Page 1, title block.
    *   **Problem:** The date is given as "(Dated: June 4, 2026)". While this is likely a placeholder, specific future dates are not standard.
    *   **Required Fix:** Replace the specific date with the month and year of submission, or simply the current year, as per the journal's style guide.

---
## Summary recommendation

**MAJOR REVISIONS**

This is a high-quality, statistically rigorous paper that performs an important and comprehensive null test for the environmental dependence of galaxy chirality. The author's approach is methodical and transparent, particularly in the handling of multiple analysis paths and the clear designation of a primary result. The robustness of the headline null result is well-established through an impressive suite of cross-checks. However, the paper in its current form has two major obstacles to publication: its critical reliance on an un-peer-reviewed companion paper (P5-E1) and significant presentational issues where internal file paths are mixed with scientific prose (P5-M1). Once these are addressed, along with a clarification of the RSD impact on the secondary analysis, the paper will represent a strong and valuable contribution to the literature.