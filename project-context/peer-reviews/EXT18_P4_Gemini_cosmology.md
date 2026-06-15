# P4 EXT18 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p2_chirality/chirality_catalog_paper.pdf` md5=c47abc18 pages=23
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (3940 chars)
**Wall time**: 227.1s

---

**Referee Report on "Survey-Scale Galaxy Chirality with Equivariant TTA..."**

This paper presents a comprehensive analysis of galaxy chirality on a large dataset of 8.47 million galaxies from the DESI Legacy Surveys, resulting in a new catalog of 3.2 million spiral galaxies with chirality labels. The primary methodological contribution is the use of a flip-equivariant Vision Transformer pipeline with Test-Time Averaging (TTA) to mitigate classifier biases. The main scientific result is a null detection of a real-space chirality dipole, with a sensitivity that places strong constraints on previous claims of a significant dipole signal. The authors perform an exceptionally thorough systematics analysis, identifying and quantifying a "monopole-mask leakage" channel and attributing residual signals in the harmonic-space power spectrum to coherent, low-multipole systematics rather than a cosmological signal.

The paper is well-structured, the methodology is clearly explained, and the conclusions are robustly supported by a multi-pronged analysis that includes a declared estimator hierarchy, numerous null tests, and a detailed audit of potential systematic effects. The proactive and careful distinction between significance values derived from different null procedures is a model of good practice. The work represents a significant contribution to the field, both in its scientific result and in the rigorous methodology it establishes for future studies of this kind.

The paper is recommended for publication in Physical Review D after addressing the following points.

---
### Findings

#### MAJOR

*   **P4-M1: Section V.A, page 12 — Inaccurate description of previous results.**
    *   **Problem:** The text states: "...the 0.41σ HC (peq > 0.6) simple dipole is well below the 2-4σ dipoles reported by Shamir [1, 3, 4]." This appears to confuse the significance (σ) of the reported dipoles with their amplitude (%). The introduction (page 2) correctly refers to Shamir's results as being at the "~ 2-4% level" or "~ 5-20%" amplitude. The comparison should be between the amplitude of the dipole measured in this work (e.g., the WLS best-fit of 0.32% or the simple dipole of 0.44%) and the amplitude reported by Shamir. Comparing significance values is not meaningful as they depend on sample size and error analysis.
    *   **Required Fix:** Correct the sentence to compare amplitudes, not sigmas. For example: "...the measured dipole amplitude (e.g., 0.32% from the WLS fit) is well below the 2-4% amplitude dipoles reported by Shamir [1, 3, 4]."

*   **P4-M2: Section Data Availability, page 21 — Incomplete/Provisional Reproducibility Information.**
    *   **Problem:** The Data Availability section refers to a future date ("June 2026") and an internal-looking versioning scheme ("v1.0.185 lineage"). For publication, all reproducibility artifacts must be tied to a permanent, public, and frozen state. The statement "An immutable archival snapshot... will be deposited to Zenodo at journal submission" is the correct plan, but the paper should be updated with the final DOI and release information before publication.
    *   **Required Fix:** Before publication, replace the placeholder date and versioning scheme with the final, persistent DOI for the archival snapshot (e.g., from Zenodo) and the corresponding public release tag for the code and catalog.

#### MINOR

*   **P4-m1: Abstract, page 1 — Future Date.**
    *   **Problem:** The paper is dated "June 13, 2026".
    *   **Required Fix:** Update the date to the current submission date.

*   **P4-m2: Section VI.A, page 12 — Typo in Fisher Forecast Equation.**
    *   **Problem:** The Fisher forecast derivation for σ(A) appears to contain a typo. The text gives `σ(Α) = sqrt(3) / N_spiral`. The correct expression should be `σ(Α) = sqrt(3 / N_spiral)`. The numerical result (`9.7 × 10⁻⁴`) is correct for the `sqrt(3 / N_spiral)` expression, confirming the equation itself is mistyped.
    *   **Required Fix:** Correct the equation to `σ(Α) = sqrt(3 / N_spiral)`.

*   **P4-m3: Section IV.A, page 5 — Unsupported Qualitative Claim.**
    *   **Problem:** The text states: "The spiral fraction is consistent with magnitude-limited survey expectations." This is a reasonable claim, but it is presented without a supporting number or citation.
    *   **Required Fix:** Either provide a quantitative comparison (e.g., "Our 37.8% spiral fraction is consistent with the X% found in...") or add a citation to a paper that establishes the expected fraction for a similar survey.

#### NIT (Nitpicks)

*   **P4-N1: Section I, page 2 — Awkward phrasing.**
    *   **Problem:** The sentence "Claims of such a signal have appeared intermittently in the literature. Shamir (2012) [4] reported a 2-4σ dipole..." has the same issue as P4-M1, using "σ" where amplitude is likely meant. While this is in the context of summarizing prior work, it perpetuates the potential for confusion.
    *   **Required Fix:** Rephrase to clarify that the reported significance corresponded to a certain amplitude, e.g., "...reported a dipole with per-bin asymmetry amplitudes of ~ 5-20%...". (The text does this correctly in the next sentence, but the first mention is ambiguous).

---
## Summary recommendation

**MAJOR REVISIONS**

The paper presents a high-quality, rigorous analysis and a significant null result. The methodological framework for bias hardening and systematic control is exemplary. The core scientific conclusions are well-supported. However, the major issues identified (P4-M1, P4-M2) must be addressed before the paper can be accepted. The inaccurate comparison to previous work must be corrected to ensure the paper's claims are precisely stated, and the data availability section must be finalized to meet the standards of reproducibility expected for a publication of this nature. Once these revisions are made, the paper will be a strong candidate for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the second part of the referee report, based on a more rigorous re-examination of the paper.

================================================================
### Additional Findings from Second Review

A deeper, more rigorous review of the manuscript has revealed several additional issues, primarily concerning numerical consistency and clarity. While the core conclusions of the paper remain robust, addressing these points will significantly improve the precision and reproducibility of the work.

#### MAJOR

*   **P4-M3: Section IV.D, page 10 — Inconsistent/Incorrect unit for null scatter.**
    *   **Problem:** The text describes the scatter of the monopole-only null reproduction: "The monopole-only null reproduces 99.32% of the observed pre-MASTER pseudo-C(l=1) power (±0.40 pp per-realization null scatter, N = 500...)." The unit "pp" stands for "percentage points". However, a direct calculation using the values from Table IV (`σ_null` = 0.0068e-2, `C_data` = 1.6961e-2) shows that the standard deviation of the *ratio* `C_null / C_data` is `0.0068e-2 / 1.6961e-2 ≈ 0.40`, or 40%. Using "pp" implies a scatter of 0.0040, which is a factor of 100 smaller. This is a significant error that misrepresents the variance of the generative null.
    *   **Required Fix:** Correct the unit to be consistent with the calculation. Replace "±0.40 pp" with "a per-realization fractional scatter of ±0.40 (40%)".

#### MINOR

*   **P4-m4: Multiple Locations — Inconsistent value for apodized MASTER significance.**
    *   **Problem:** The significance of the l=1 residual on the apodized footprint is quoted as **+7.28σ** in the Abstract (p. 1), Section IV.C (p. 9), and Conclusion (a) (p. 14). However, Table III (p. 11), which presents the definitive results from the 10⁴-permutation run, reports this value as **+7.31σ**. The text explicitly states that the +7.28σ value is from an earlier 500-MC run. For consistency and to reflect the highest-precision result, all mentions should be harmonized.
    *   **Required Fix:** Update all instances of the apodized MASTER l=1 significance (abstract, main text, conclusions) to the +7.31σ value from the 10⁴-permutation run presented in Table III, or explicitly state in each case that the quoted value is from the smaller 500-MC run for a specific reason (e.g., continuity with a specific artifact). The former is strongly preferred.

*   **P4-m5: Table III, page 11 — Minor numerical inconsistency.**
    *   **Problem:** For the "canonical, unapod." row at l=1, the provided values are C_data = 7.27e-6, <C_b>_null = 0.57e-6, and σ_null = 0.84e-6. The reported significance is z = +7.93. A direct calculation gives z = (7.27 - 0.57) / 0.84 = 6.7 / 0.84 ≈ 7.98. While the difference is small, it points to a minor inconsistency from either rounding or the use of slightly different underlying numbers.
    *   **Required Fix:** Please re-calculate and/or verify the numbers in this row of Table III to ensure they are fully consistent.

#### NIT (Nitpicks)

*   **P4-N2: Figure 1 Caption, page 3 — Unsupported quantitative claim.**
    *   **Problem:** The caption states: "...without an explicit NOT_SPIRAL class, ~62% of the parent sample would leak into the spiral classification." While plausible, this specific number is not derived or justified anywhere in the main text. It appears to be an assertion about the hypothetical behavior of a different classifier.
    *   **Required Fix:** Either remove this specific number or add a sentence to the main text (e.g., in Section IV.A) explaining how it was estimated.

*   **P4-N3: Figure 8, page 10 — Typo in figure annotation.**
    *   **Problem:** The annotation for the l=1 data point in the plot reads "+3.63σ". The caption and main text consistently refer to this value as +3.64σ.
    *   **Required Fix:** Correct the annotation in Figure 8 to "+3.64σ".

================================================================