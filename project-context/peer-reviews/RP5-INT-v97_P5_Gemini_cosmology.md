# P5 RP5-INT-v97 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf` md5=9b3aad7a pages=35
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 141.7s

---

## Referee Report: P5

**Manuscript Title:** Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Void Null Test on 56,981 DESI DR1 Spirals, with a Secondary Tidal-Tensor Cross-Check
**Author:** Houston Golden
**Manuscript ID:** P5

This manuscript presents a detailed statistical analysis searching for a correlation between the chirality (handedness) of spiral galaxies and their large-scale structure environment. Using a large sample of galaxies from the DESI Data Release 1, cross-matched with a chirality catalog, the author performs a primary null test using the DESIVAST void catalog and a secondary cross-check using a T-Web tidal-tensor classifier. The main conclusion is a null result: no statistically significant evidence for environment-dependent chirality is found, beyond a previously identified, catalog-wide systematic monopole offset.

The analysis is remarkably thorough, featuring an extensive set of robustness tests, cross-validations against multiple classifiers and data cuts, and a high degree of transparency. The work is computationally and statistically sophisticated. However, there are several essential and major issues that must be addressed before the manuscript can be considered for publication in Physical Review D.

---
### ESSENTIAL REVISIONS

**P5-E1: Reliance on "in preparation" manuscript for core inputs.**
*   **Location:** Abstract (p.1), Introduction (p.3), Section II (p.3), Appendix A (p.31), and throughout.
*   **Problem:** The entire analysis rests on two crucial inputs from "Paper IV [3] (in preparation)": (1) the per-galaxy chirality labels (CW/CCW), and (2) the catalog-wide monopole offset (Δfcw = -0.0026), which is used as the reference for all residual environmental tests. While Appendix A provides a helpful summary of the methodology from Paper IV, it is not a substitute for a peer-reviewed publication. The validity of every statistical test in this manuscript hinges on the correctness and robustness of the classifier and monopole derivation presented in a non-peer-reviewed source. This is particularly critical for a null result, where understanding and trusting the systematic error floor (the monopole) is paramount. A manuscript submitted to PRD must be self-contained and its foundational claims verifiable from the peer-reviewed literature or from the manuscript itself.
*   **Fix:** The paper cannot be published in its current form. The author must either:
    a) Wait for Paper IV to be accepted and published (or at least publicly available on a preprint server like arXiv with sufficient detail for independent assessment) and update the citation accordingly. This is the strongly preferred option.
    b) Integrate the entirety of the relevant methodology from Paper IV (classifier architecture, training data, validation procedures, accuracy assessment, and the full derivation of the monopole systematic) into the present manuscript, likely as a comprehensive appendix, so that this work can be evaluated on its own merits.

---
### MAJOR REVISIONS

**P5-M1: Overly long and dense abstract.**
*   **Location:** Abstract (p.1).
*   **Problem:** The abstract is exceptionally long (over 600 words) and reads more like an executive summary or the paper's introduction. It is saturated with a large number of numerical results, statistical tests, and sub-analyses that, while comprehensive, obscure the main headline result. An abstract should concisely state the objective, methods, primary results, and conclusion. The level of detail provided is excessive for an abstract and hinders immediate comprehension of the paper's core contribution.
*   **Fix:** Condense the abstract to focus on the primary question, the main dataset (DESI DR1 x chirality catalog), the primary method (DESIVAST void cross-check), the headline result (a statistically significant null result for environment-dependent chirality, consistent with a known catalog-wide monopole), and the key quantitative upper limit derived. Details of secondary cross-checks (T-Web, Phase 2 sweep, etc.) and their specific p-values should be moved to the main body. A target length of ~250-300 words is standard and appropriate for PRD.

**P5-M2: Ambiguous scope and treatment of Redshift-Space Distortions (RSD).**
*   **Location:** Abstract (p.3), Section VIII (p.17), Section XIII (p.30).
*   **Problem:** The paper correctly states its results are in "fixed redshift space" and acknowledges that RSD affects the cosmic-web classification. The discussion in Sec. XIII is insightful, correctly identifying that anisotropic eigenvalue deformation is the dominant effect for a tidal-tensor classifier, not just a scalar displacement. However, the paper then concludes the effect is "sub-dominant at the current ~10⁻³ precision" based on an order-of-magnitude estimate, not a full calculation using a real-space reconstruction. For the primary DESIVAST analysis, it argues the result is "RSD-bounded" and provides a Monte Carlo test on galaxy positions. While this test is a good step, it only tests the sensitivity to position shifts within a *fixed* void geometry, not the change in the void geometry itself under RSD. The lack of a re-classification using reconstructed real-space positions is a significant limitation for a precision null test.
*   **Fix:**
    a) The abstract's claim of a "fixed-redshift-space statement" should be accompanied by a brief mention of the unquantified systematic from RSD.
    b) The conclusion that the RSD effect is "sub-dominant" in Sec. XIII should be rephrased more cautiously, as it is based on an order-of-magnitude estimate. State clearly that a full RSD-corrected analysis is required to definitively rule out RSD-induced systematics at this level of precision.
    c) The main conclusion should be qualified to state that the null result holds *under the assumption that RSD effects do not systematically alter the environmental classification in a way that would mask or mimic a chirality signal*.

**P5-M3: Justification for "primary" vs. "secondary" analysis paths.**
*   **Location:** Abstract (p.1), Section V B (p.7).
*   **Problem:** The paper declares the DESIVAST-anchored analysis as "primary" and the T-Web analysis as "secondary" on a "post-hoc" basis. While the transparency is commendable, the justification provided relies on the properties of the DESIVAST sample (larger void sample, cleaner, from a peer-reviewed source catalog). However, the T-Web analysis is arguably more comprehensive, as it covers the full redshift range and all four cosmic-web environments, not just voids. The post-hoc choice, even if well-justified, can be perceived as cherry-picking the cleanest null result to headline.
*   **Fix:** The author should strengthen the a priori justification for the DESIVAST path being primary. For instance, it could be argued that testing for parity violation in voids is the most theoretically motivated scenario (e.g., lowest density, least non-linear evolution). Alternatively, present both analyses on a more equal footing in the abstract and introduction, highlighting that both consistently yield a null result but have different strengths, weaknesses, and systematic limitations. The "post-hoc" declaration should be removed if a stronger a priori case can be made.

---
### MINOR REVISIONS

**P5-m1: Use of internal paper tags.**
*   **Location:** Abstract (p.1, footnote), p.3 ("P5 internal matched-sample value"), p.32 ("P5 matched-spiral catalog monopole").
*   **Problem:** The paper uses the tag "P5" in several places, which appears to be an internal designator for this manuscript. This is inappropriate for a published paper.
*   **Fix:** Remove all instances of "P5" from the text and replace with a descriptive phrase like "this work's" or "the internal". For example, "the internal matched-sample value".

**P5-m2: Clarity on the bright-vs-dark sample systematic.**
*   **Location:** Robustness (p.2), Section VI A (p.8), Section VI D (p.13).
*   **Problem:** The paper finds a ~2σ difference in `fcw` between the "bright" (BGS) and "dark" (LRG/ELG/QSO) samples and attributes this to "BGS-selection-function-conditioned imaging-leg systematics". This is a key systematic effect, and the discussion is spread across several sections. The argument that this is a systematic and not a genuine astrophysical effect could be made more clearly and centrally.
*   **Fix:** Consolidate the discussion of the bright-vs-dark sample difference into a single, clearly-argued subsection. Explicitly state why this is interpreted as a known systematic propagated from the imaging data, and how the primary DESIVAST analysis (which is mostly BGS-bright) is designed to be insensitive to it.

**P5-m3: Toy EFT model in Appendix B.**
*   **Location:** Appendix B (p.32).
*   **Problem:** The appendix presents a "toy EFT mapping" to connect the observational bound to a physical operator. The author is commendably clear that this is a toy model and not a derived constraint. However, the specific operator form `gφ (∇iφ) (∇²ρ/ρbg) (L · ∇̂ρ)` is novel and not derived from any cited literature. Presenting such a specific, non-standard operator, even as a toy, could be misleading or be misinterpreted as a derived result.
*   **Fix:** To avoid misinterpretation, the author should either:
    a) Generalize the discussion to be purely schematic (e.g., `Δfcw ~ g * O_parity-odd(ρ, L)`), without writing down a specific operator form.
    b) If the operator is retained, add even stronger caveats that its specific form is purely illustrative of the necessary symmetries and has not been derived from a fundamental theory.

---
### NIT-PICKS

**P5-N1: Incorrect date.**
*   **Location:** Abstract (p.1).
*   **Problem:** The paper is dated "June 30, 2026".
*   **Fix:** Change the date to the current submission date.

**P5-N2: Confusing parenthetical.**
*   **Location:** Section VIII E (p.20).
*   **Problem:** The sentence "...quoted in the Table XI sign convention Δfcw = f_cw^non-void - f_cw^void (the committed artifact stores the opposite-signed f_void – f_non-void values)..." contains a parenthetical about an internal data storage detail. This is confusing and irrelevant to the reader.
*   **Fix:** Remove the parenthetical statement. The sign convention defined in the table header is sufficient.

**P5-N3: Awkward phrasing in abstract.**
*   **Location:** Abstract (p.1).
*   **Problem:** The phrasing "this primary designation is declared post-hoc — no single a priori preregistered plan was filed..." is very transparent but also defensive and awkwardly phrased for an abstract.
*   **Fix:** Rephrase to be more direct and confident. For example: "The primary analysis path, a cross-check against the DESIVAST void catalog, is chosen for its large and clean void sample. The robustness of the null result across all tested void-finders and alternative analysis paths validates this choice."

---
## Summary recommendation
**MAJOR REVISIONS**

## Justification
The paper presents a comprehensive and statistically rigorous null test for the environmental dependence of spiral galaxy chirality. The analysis is exceptionally thorough, with numerous cross-checks, robustness tests, and a high degree of transparency. The work has the potential to be an important contribution, providing a strong observational constraint on parity-violating physics.

However, the manuscript in its current form has one essential flaw and several major issues. The most critical issue is its reliance on a companion paper (Paper IV) that is still "in preparation" for its foundational data and systematic corrections. A paper in Physical Review D must be self-contained and its claims verifiable. Additionally, the abstract is excessively long, the treatment of redshift-space distortions requires more robust justification, and the framing of the primary analysis path could be improved.

The author has clearly performed a great deal of careful work. If the essential and major issues listed above are addressed, the revised manuscript would likely be suitable for publication.