# P4 INT-X-P4 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/private/tmp/P4_int.pdf` md5=077eeee9 pages=24
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (9017 chars)
**Wall time**: 144.7s

---

## Referee Report: P4

**Manuscript ID:** P4
**Title:** Survey-Scale Galaxy Chirality with Equivariant TTA: A Null Real-Space Chirality Dipole, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)
**Journal:** Physical Review D

This paper presents a comprehensive analysis of galaxy chirality using a new catalog of 8.47 million galaxies from the DESI Legacy Surveys. The primary result is a null detection of a real-space chirality dipole, which is supported by a rigorous, multi-pronged analysis designed to control for systematic effects. The authors introduce a flip-equivariant Vision Transformer pipeline and a detailed bias-hardening and systematics-auditing framework. The work is of high quality, demonstrating a sophisticated understanding of the observational and statistical challenges inherent in this type of measurement. The methodological contributions, particularly the use of equivariant test-time averaging and the detailed characterization of the monopole-mask leakage channel, are significant and set a new standard for future studies in this area.

The analysis is thorough, and the conclusions are well-supported by the evidence presented. The authors are commendably transparent about the limitations of their methods, such as the use of pseudo-labels for training and the low accuracy against independent human labels, and they correctly account for these limitations in their analysis. The distinction between parity-even and parity-odd observables is correctly maintained, and the paper's claims are appropriately scoped.

While the paper is methodologically sound and the results are significant, several points require clarification and revision before the manuscript can be accepted for publication.

---
### Findings

#### ESSENTIAL

*   **P4-E1:** Section: Abstract & Title page (p. 1)
    *   **Problem:** The paper is dated "June 28, 2026", which is a future date.
    *   **Fix:** This must be corrected to the date of submission.

#### MAJOR

*   **P4-M1:** Section: Abstract (p. 1), Appendix D (p. 20), and throughout.
    *   **Problem:** The abstract and main text present a strong exclusion of a "1.7% reference amplitude" dipole at `z ≈ -18` using a WLS template fit. However, the choice of this 1.7% amplitude is not justified where it is first introduced. The reader has to find a brief mention of "Shamir's 1.7%-4.0% reported range" on page 12 to understand its provenance. For a headline exclusion claim, the reference value must be clearly defined and justified upfront.
    *   **Fix:** In the abstract, explicitly state the origin of this reference value. For example: "...disfavors a clean cosmological dipole at the 1.7% reference amplitude (representative of the lower end of literature claims) at z ≈ -18...". In the main body, where this WLS analysis is first discussed (e.g., in the Declared Analysis Hierarchy, Sec. III.B), the 1.7% value and its justification as a meaningful astrophysical benchmark must be clearly stated and cited.

#### MINOR

*   **P4-m1:** Section: VI. Discussion (p. 13)
    *   **Problem:** The paper length (24 pages) is substantial for a null result. While the methodological detail is a key strength and largely justifies the length, the main narrative in Sections I-VI could be streamlined. Some of the more detailed numerical results and robustness checks currently in the main text might be better placed in the appendices to improve readability for a broader audience.
    *   **Fix:** The authors should consider moving some of the finer quantitative details from the main text of Section IV (Results) to the relevant appendices. For example, the detailed breakdown of z-values from the confidence-cut sweep (p. 7) or the multiple weightings for the MASTER analysis (p. 9) could be summarized in the main text with a pointer to a more detailed table or description in the appendix. This is a suggestion for improved presentation, not a requirement to remove content.

*   **P4-m2:** Section: Data Availability (p. 22)
    *   **Problem:** The text states, "A persistent archival DOI (Zenodo deposit of the versioned release) has not yet been minted...". This is acceptable for a submission under review.
    *   **Fix:** For the final camera-ready version of the manuscript, this section must be updated to include the persistent DOI for the archived data, code, and analysis artifacts. This is a reminder for the authors.

*   **P4-m3:** Section: Footnote 5 (p. 22)
    *   **Problem:** The phrasing "The +4.31σ vs. the primary +0.41σ real-space dipole are therefore not directly comparable..." is slightly awkward.
    *   **Fix:** Suggest rephrasing for clarity. For example: "The +4.31σ value and the primary +0.41σ real-space dipole significance are not directly comparable, as they are derived from different estimators measuring different observables on the same sample."

#### NIT (Cosmetic)

*   **P4-N1:** Section: Abstract (p. 1)
    *   **Problem:** Minor formatting issue in the set notation: "peq ∈ {0, 0.4, 0.5,0.6,0.7,0.8}".
    *   **Fix:** Add spaces for readability: "peq ∈ {0, 0.4, 0.5, 0.6, 0.7, 0.8}".

*   **P4-N2:** Section: IV.C Dipole Analysis (p. 7)
    *   **Problem:** The sentence "The fitted dipole has amplitude 4.4 × 10⁻³ toward (l,b) = (293°, 12°)..." is missing a symbol for the amplitude.
    *   **Fix:** Specify the quantity, e.g., "The fitted dipole has an amplitude of A_dip = 4.4 × 10⁻³...".

*   **P4-N3:** Section: Abstract (p. 1)
    *   **Problem:** The explanation of why the +3.64σ and +7.93σ values are not independent detections is slightly repetitive. The sentence "both are systematics-attributed diagnostics... not two independent detection claims" is immediately followed by a parenthetical "Note: the σ values quoted... are not directly comparable...".
    *   **Fix:** Consider merging these statements for conciseness. For example: "These two values are systematics-attributed diagnostics from different null-run sizes, not independent detection claims; as with all σ values in this work arising from distinct null procedures, they are not directly comparable as detection significances but serve as diagnostic indicators."

---
## Summary recommendation

**MAJOR REVISIONS**

The paper represents a significant and high-quality contribution to the study of cosmological chirality. The methodological rigor is a credit to the author and sets a new standard for the field. The primary result—a null detection of a chirality dipole—appears robust and is supported by an exhaustive suite of systematics checks. However, the issues identified above, particularly the need to correct the date and properly justify the reference amplitude used in the headline WLS exclusion, must be addressed before publication. Once these revisions are made, the paper will be a strong candidate for publication in Physical Review D.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated review, incorporating the new findings from the second, more rigorous pass.

================================================================
## Referee Report: P4

**Manuscript ID:** P4
**Title:** Survey-Scale Galaxy Chirality with Equivariant TTA: A Null Real-Space Chirality Dipole, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)
**Journal:** Physical Review D

This paper presents a comprehensive analysis of galaxy chirality using a new catalog of 8.47 million galaxies from the DESI Legacy Surveys. The primary result is a null detection of a real-space chirality dipole, which is supported by a rigorous, multi-pronged analysis designed to control for systematic effects. The authors introduce a flip-equivariant Vision Transformer pipeline and a detailed bias-hardening and systematics-auditing framework. The work is of high quality, demonstrating a sophisticated understanding of the observational and statistical challenges inherent in this type of measurement. The methodological contributions, particularly the use of equivariant test-time averaging and the detailed characterization of the monopole-mask leakage channel, are significant and set a new standard for future studies in this area.

The analysis is thorough, and the conclusions are well-supported by the evidence presented. The authors are commendably transparent about the limitations of their methods, such as the use of pseudo-labels for training and the low accuracy against independent human labels, and they correctly account for these limitations in their analysis. The distinction between parity-even and parity-odd observables is correctly maintained, and the paper's claims are appropriately scoped.

While the paper is methodologically sound and the results are significant, several points require clarification and revision before the manuscript can be accepted for publication.

---
### Findings

#### ESSENTIAL

*   **P4-E1:** Section: Abstract & Title page (p. 1)
    *   **Problem:** The paper is dated "June 28, 2026", which is a future date.
    *   **Fix:** This must be corrected to the date of submission.

#### MAJOR

*   **P4-M1:** Section: Abstract (p. 1), Appendix D (p. 20), and throughout.
    *   **Problem:** The abstract and main text present a strong exclusion of a "1.7% reference amplitude" dipole at `z ≈ -18` using a WLS template fit. However, the choice of this 1.7% amplitude is not justified where it is first introduced. The reader has to find a brief mention of "Shamir's 1.7%-4.0% reported range" on page 12 to understand its provenance. For a headline exclusion claim, the reference value must be clearly defined and justified upfront.
    *   **Fix:** In the abstract, explicitly state the origin of this reference value. For example: "...disfavors a clean cosmological dipole at the 1.7% reference amplitude (representative of the lower end of literature claims) at z ≈ -18...". In the main body, where this WLS analysis is first discussed (e.g., in the Declared Analysis Hierarchy, Sec. III.B), the 1.7% value and its justification as a meaningful astrophysical benchmark must be clearly stated and cited.

#### MINOR

*   **P4-m1:** Section: VI. Discussion (p. 13)
    *   **Problem:** The paper length (24 pages) is substantial for a null result. While the methodological detail is a key strength and largely justifies the length, the main narrative in Sections I-VI could be streamlined. Some of the more detailed numerical results and robustness checks currently in the main text might be better placed in the appendices to improve readability for a broader audience.
    *   **Fix:** The authors should consider moving some of the finer quantitative details from the main text of Section IV (Results) to the relevant appendices. For example, the detailed breakdown of z-values from the confidence-cut sweep (p. 7) or the multiple weightings for the MASTER analysis (p. 9) could be summarized in the main text with a pointer to a more detailed table or description in the appendix. This is a suggestion for improved presentation, not a requirement to remove content.

*   **P4-m2:** Section: Data Availability (p. 22)
    *   **Problem:** The text states, "A persistent archival DOI (Zenodo deposit of the versioned release) has not yet been minted...". This is acceptable for a submission under review.
    *   **Fix:** For the final camera-ready version of the manuscript, this section must be updated to include the persistent DOI for the archived data, code, and analysis artifacts. This is a reminder for the authors.

*   **P4-m3:** Section: Footnote 5 (p. 22)
    *   **Problem:** The phrasing "The +4.31σ vs. the primary +0.41σ real-space dipole are therefore not directly comparable..." is slightly awkward.
    *   **Fix:** Suggest rephrasing for clarity. For example: "The +4.31σ value and the primary +0.41σ real-space dipole significance are not directly comparable, as they are derived from different estimators measuring different observables on the same sample."

*   **P4-m4:** Section: IV.C, Table II (p. 7)
    *   **Problem:** In Table II, the entry for Tier B (calibrated) has an inconsistent uncertainty. The value is given as `0.50400(27)`, implying `σ = 0.00027`. However, the table caption states that uncertainties are binomial, and a binomial calculation for `N = 3,201,160` and `f ≈ 0.5` yields `σ ≈ 0.000279`. The reported uncertainty appears to be off by a factor of 10 (likely a typo for `(279)`). Furthermore, the `Dev. (σ)` value of `+14.6` is not fully consistent with either uncertainty value.
    *   **Fix:** Please correct the uncertainty for the Tier B row in Table II and ensure the corresponding `Dev. (σ)` value is calculated consistently. If a non-binomial uncertainty was used, this should be explicitly stated and justified.

*   **P4-m5:** Section: Abstract (p. 1)
    *   **Problem:** The abstract contains an incorrect cross-reference. It states, "...a pre-specified selection threshold... Sec. IIIB...". The description of the confidence-cut sweep is in Section IV.C, not III.B.
    *   **Fix:** Please correct the cross-reference to point to Section IV.C.

*   **P4-m6:** Section: IV.C, Figure 6 caption (p. 9)
    *   **Problem:** The caption for Figure 6 refers to systematics cross-checks in `§E`. There is no Section E in the paper.
    *   **Fix:** Please correct this cross-reference to point to the appropriate section(s) where the systematics checks are described (e.g., Section III.B, Appendix C, Appendix D).

#### NIT (Cosmetic)

*   **P4-N1:** Section: Abstract (p. 1)
    *   **Problem:** Minor formatting issue in the set notation: "peq ∈ {0, 0.4, 0.5,0.6,0.7,0.8}".
    *   **Fix:** Add spaces for readability: "peq ∈ {0, 0.4, 0.5, 0.6, 0.7, 0.8}".

*   **P4-N2:** Section: IV.C Dipole Analysis (p. 7)
    *   **Problem:** The sentence "The fitted dipole has amplitude 4.4 × 10⁻³ toward (l,b) = (293°, 12°)..." is missing a symbol for the amplitude.
    *   **Fix:** Specify the quantity, e.g., "The fitted dipole has an amplitude of A_dip = 4.4 × 10⁻³...".

*   **P4-N3:** Section: Abstract (p. 1)
    *   **Problem:** The explanation of why the +3.64σ and +7.93σ values are not independent detections is slightly repetitive. The sentence "both are systematics-attributed diagnostics... not two independent detection claims" is immediately followed by a parenthetical "Note: the σ values quoted... are not directly comparable...".
    *   **Fix:** Consider merging these statements for conciseness. For example: "These two values are systematics-attributed diagnostics from different null-run sizes, not independent detection claims; as with all σ values in this work arising from distinct null procedures, they are not directly comparable as detection significances but serve as diagnostic indicators."

*   **P4-N4:** Section: Appendix E, Footnote 5 (p. 22)
    *   **Problem:** The footnote contains a typo in a cross-reference: "...canonical +3.64σ result (Sec. D, NMC = 500, seed 42)".
    *   **Fix:** This should be corrected to "Sec. IV.D".

---
## Summary recommendation

**MAJOR REVISIONS**

The paper represents a significant and high-quality contribution to the study of cosmological chirality. The methodological rigor is a credit to the author and sets a new standard for the field. The primary result—a null detection of a chirality dipole—appears robust and is supported by an exhaustive suite of systematics checks. However, the issues identified above, particularly the need to correct the date and properly justify the reference amplitude used in the headline WLS exclusion, must be addressed before publication. The additional minor corrections to arithmetic and cross-references will further improve the manuscript's clarity and precision. Once these revisions are made, the paper will be a strong candidate for publication in Physical Review D.