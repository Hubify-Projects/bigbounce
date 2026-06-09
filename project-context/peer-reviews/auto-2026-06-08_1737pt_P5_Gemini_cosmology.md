# P5 auto-2026-06-08_1737pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 152.9s

---

# Referee Report

**Paper ID:** P5
**Title:** Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with V-Web Cross-Check Across 791,635 DR1 Matched Spirals
**Journal:** Physical Review D

This paper investigates the relationship between spiral galaxy chirality and large-scale structure environment using data from the DESI Data Release 1, cross-matched with a galaxy chirality catalog. The primary conclusion is a null result: no statistically significant dependence of spiral handedness on environment (void, wall, filament, cluster) is found. The small, catalog-wide deviations from a perfect 50/50 split are attributed to a systematic monopole offset. The analysis is extensive, employing multiple cosmic-web classifiers (V-Web, DESIVAST, Tempel+ FoF, ASTRA) and a wide range of robustness checks.

While the technical analysis is thorough and the scope of the work is impressive, the manuscript in its current form has several essential flaws that preclude its publication in Physical Review D. The required revisions are substantial.

---

## Detailed Findings

### ESSENTIAL Revisions

**E1. Critical Dependence on Unpublished Work (Throughout)**
The entire analysis is built upon a companion paper, "Paper IV [3]", which is cited as "in preparation; manuscript in preparation" and "not yet peer reviewed". This is unacceptable.
*   **Problem:** The primary data for the analysis—the per-galaxy chirality labels {CW, CCW}—are taken directly from this unpublished source (§II, p. 2: "Paper IV provides the per-galaxy CW/CCW labels we test here; we make no independent classification."). Furthermore, a central piece of the interpretation—the catalog-wide monopole offset `Afcw = -0.0026` used to predict and explain observed deviations—is also asserted from Paper IV. A manuscript submitted to PRD must be self-contained. Reviewers and readers cannot be expected to validate results based on an inaccessible and un-vetted source.
*   **Fix:** The essential results from Paper IV must be included in this manuscript, for instance in an appendix. This would need to include a detailed description of the chirality classification methodology, the validation of the classifier, and the full derivation of the monopole offset. Alternatively, the authors must wait until Paper IV is published or publicly available on a preprint server like arXiv before this manuscript can be properly reviewed.

**E2. Use of Future Dates for Manuscript and Citations (p. 1, p. 15, p. 20)**
The manuscript itself is dated "June 2026". Several key references that provide context and cross-checks are also cited with future dates.
*   **Problem:**
    *   The manuscript date must reflect the date of submission. A future date is nonsensical and suggests the paper is a preliminary draft.
    *   References [11] (Ullah et al.) and [12] (Zapata-Zuluaga et al.) are cited as `(2026)` with `arXiv:2604...` identifiers. Scientific work must be cited based on its publication or public preprint date. Citing work that does not yet exist is not permissible.
*   **Fix:** The manuscript date must be corrected to the submission date. All citations must be to works that are publicly available at the time of review. If these papers are not yet on arXiv, the discussion relying on them must be removed or rephrased as a general statement about forthcoming work, without specific citations.

**E3. Dismissal of a >3σ Signal (p. 2, p. 7)**
The paper's headline is a null result. However, the authors' own analysis uncovers a statistically significant signal which is then downplayed.
*   **Problem:** The tracer-program stratification reveals a sign-flip between the BGS-bright (`σ = -2.80`) and LRG/ELG/QSO-dark (`σ = +2.85`) samples within the filament class. The abstract (p. 2) states the joint two-sample z-test on this difference is `|z| ≈ 3.40`. A 3.4σ effect is a detection, not a "residual structure" to be "flagged" and set aside. The paper's primary conclusion of "no environment dependence" is premature and potentially incorrect in light of this finding. The logic of prioritizing the DESIVAST-based null result (which uses a subsample, primarily BGS galaxies at z<0.24, where this effect might be different or absent) over this detection is not sufficiently justified.
*   **Fix:** The 3.4σ signal must become a central part of the paper's results and discussion. The abstract and conclusions must be rewritten to reflect that while some tests are null, a significant tracer-dependent effect is detected. The paper should then focus on interpreting this signal. Is it astrophysical, or is it a systematic related to the interplay between target selection and cosmic-web classification? The current explanation, which again relies on the unpublished Paper IV, is insufficient.

### MAJOR Revisions

**M1. Post-Hoc Analysis Path Selection (p. 5)**
The authors explicitly state that the choice of the DESIVAST analysis as "primary" and the V-Web analysis as "secondary" was made "post-hoc".
*   **Problem:** This is an admission of exploring a "garden of forking paths". While the transparency is laudable, it undermines the statistical validity of the conclusions. When multiple, independent analyses are performed, the choice of which one to headline cannot be made after seeing the results, unless a rigorous multiple-testing correction is applied to all reported significance values. The justification provided for the choice is reasonable (DESIVAST has a cleaner, larger void sample), but the choice remains post-hoc.
*   **Fix:** The authors must reframe the paper to present all analyses (V-Web, DESIVAST, Tempel+, ASTRA) on a more equal footing as a suite of consistency checks. The abstract and conclusion should synthesize the results from all paths, including the 3.4σ detection from the V-Web analysis and the strong nulls from the DESIVAST analysis. The narrative of a single "primary" path should be abandoned.

**M2. Non-Rigorous Theoretical Appendix (p. 19)**
Appendix A attempts to map the observational bound to an effective-field-theory (EFT) operator, but the treatment is not rigorous.
*   **Problem:** The proposed operator, `L_parity ∝ (L·z)`, explicitly and unphysically breaks rotational invariance. The author acknowledges this and other issues (like gauge invariance) but proceeds with the "toy" model. For a journal like PRD, theoretical appendices must meet a high standard of rigor. A schematic, coordinate-dependent operator is not sufficient.
*   **Fix:** This appendix should either be made rigorous by constructing a proper rotationally and gauge-invariant pseudoscalar operator from the physical quantities involved (e.g., `L · ∇ρ`), or it should be removed entirely. In its current form, it detracts from the quality of the observational work.

### MINOR Revisions

**MN1. Incorrect/Incomplete Table Entry (p. 6, Table III)**
*   **Problem:** In Table III, the final column `|σ_obs - σ_pred|` is missing the sign for quintiles 3 and 4. The value for quintile 3 should be -1.87, not 1.87.
*   **Fix:** Correct the values in the table to include the proper sign, or consistently use absolute values and label the column accordingly.

**MN2. Overstated Claim of RSD Immunity (p. 10)**
*   **Problem:** The text claims the DESIVAST analysis is "essentially RSD-immune". This is an overstatement. While it is less sensitive to redshift-space distortions (RSDs) than the tidal-tensor field calculation, peculiar velocities can still move galaxies across void boundaries.
*   **Fix:** Rephrase to be more precise, e.g., "The DESIVAST void membership test is significantly more robust to RSDs than the tidal-tensor classification because..." and provide the brief justification that follows.

**MN3. Sign Error in Table (p. 12, Table VIII)**
*   **Problem:** In Table VIII, the `Afcw` for the VoidFinder algorithm is listed as `+0.0007`. Based on the `f_cw` values in the same row (`f_void`=0.4964, `f_non-void`=0.4971), the difference should be `0.4964 - 0.4971 = -0.0007`.
*   **Fix:** Correct the sign of `Afcw` in the table.

**MN4. Internal Review Artifact (p. 14)**
*   **Problem:** The text contains the phrase "0.026 pp (✓ within spec)". The checkmark and "within spec" are clearly artifacts from an internal review process.
*   **Fix:** Remove this internal notation.

### NITs (Cosmetic)

**N1. Figure Placement (p. 10, p. 16)**
*   **Problem:** Figure 5 is discussed on page 8 but appears on page 10. Figure 7 is discussed on page 15 but appears on page 16.
*   **Fix:** Adjust figure placement to be closer to the first point of reference in the text.

---

## Summary recommendation

**REJECT**

The paper presents an extensive and potentially important analysis of a timely dataset. The level of detail in the robustness checks is commendable. However, the manuscript is critically flawed in its current form. The reliance on an unpublished companion paper for its core data and interpretation (E1), the unacceptable use of future dates (E2), and the improper handling of a significant (>3σ) detection (E3) are all essential issues that make the paper unsuitable for publication.

A future resubmission could be considered only after these fundamental problems are addressed. Specifically, the material from Paper IV must be made available and verifiable, all dates and citations must be corrected, and the 3.4σ detection must be treated as a primary result, with the abstract and conclusions rewritten accordingly. The methodological issue of post-hoc analysis selection (M1) would also need to be reframed. Given the scale of these required changes, the manuscript needs to be rejected at this time.