# P4 RP4-INT-v200 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p2_chirality/chirality_catalog_paper.pdf` md5=a644743f pages=25
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 193.5s

---

**Referee Report on "Survey-Scale Galaxy Chirality with Equivariant TTA..."**

This paper presents a new, large catalog of galaxy chirality labels for 8.47 million galaxies from the DESI Legacy Surveys DR8, with 3.2 million classified as spirals. The primary scientific result is a null detection of a real-space chirality dipole, consistent with statistical isotropy. The authors perform an extensive and rigorous analysis of potential systematic effects, arguing that previously reported signals in the literature may be attributable to a "monopole-mask leakage" channel, which they quantify. The paper's main contributions are the public release of the catalog and the detailed methodology for bias hardening and systematic control in such measurements.

The methodology is generally of a very high standard. The use of equivariant test-time averaging (TTA) to enforce flip-equivariance by construction is a crucial and well-executed step. The explicit declaration of an analysis hierarchy, with the real-space dipole as the primary cosmological estimator and harmonic-space quantities as systematics diagnostics, is a commendable example of analytical rigor. The "Estimator decision tree" (Table I) is an excellent feature that clarifies the logical structure of the paper's claims. The analysis of systematics, particularly in Appendix D, is thorough.

However, there are several issues that must be addressed before the paper can be considered for publication in Physical Review D. The most critical of these is a significant inconsistency in the quoted exclusion significance for a cosmological dipole, which is a primary result of the paper.

---

### Detailed Findings

#### ESSENTIAL

*   **P4-E1: Inconsistent Dipole Exclusion Significance (Abstract, Sec I, Sec III B, Appendix D, Table XI)**
    *   **Section/Page:** Abstract (p. 1), Sec. I (p. 2), Sec. III B (p. 3), Appendix D (p. 21), Table XI (p. 22).
    *   **Problem:** The abstract and main body repeatedly claim that the block-bootstrap WLS template fit disfavors a clean cosmological dipole at the 1.7% reference amplitude at `z ≈ -18`. However, a direct calculation from the numbers provided in Table XI (p. 22) shows this significance is computed against a reference amplitude `A_ref = 0.034` (3.4%), not 1.7%.
        *   Calculation from Table XI: `A_best = 4.55e-3`, `σ_boot = 1.63e-3`, `A_ref = 0.034`.
        *   `z = (A_best - A_ref) / σ_boot = (0.00455 - 0.034) / 0.00163 ≈ -18.1`. This matches the paper's `z ≈ -18` claim.
        *   However, the text (e.g., Abstract) explicitly states the test is against "the 1.7% reference amplitude (the lower end of Shamir's reported 1.7%-4.0% asymmetry range)". For a 1.7% amplitude, `A_ref = 0.017`.
        *   The significance against the claimed 1.7% amplitude is `z = (0.00455 - 0.017) / 0.00163 ≈ -7.64`.
        *   While `z ≈ -7.6` is still a very strong exclusion, it is substantially weaker than the claimed `z ≈ -18`. This discrepancy inflates a primary scientific result of the paper.
    *   **Required Fix:** The authors must correct this inconsistency throughout the manuscript. They should decide which reference amplitude (1.7%, 3.4%, or another) is the primary one being tested and ensure that the text, abstract, and tables all use this value and the corresponding, correctly calculated significance. The claim in the abstract must be revised to reflect the accurate significance for the stated reference amplitude.

*   **P4-E2: Placeholder Content in Final Manuscript**
    *   **Section/Page:** Title block (p. 1), Data Availability (p. 17, 24).
    *   **Problem:** The manuscript contains several pieces of placeholder text and future-dated information that are inappropriate for a final publication.
        1.  Dated: "June 30, 2026" (p. 1).
        2.  Email: "houston@hubify.com" appears to be a placeholder (p. 1).
        3.  Data Availability: The text "that tagged commit and DOI will be the single citable reproducibility handle for the published version, inserted here in place of this sentence at submission" (p. 24) is an internal note and must be replaced with the actual DOI.
        4.  Release tag: "v2026.04" (p. 17, 24) is a future-dated tag. This must be updated to the actual, frozen release tag corresponding to the submitted manuscript.
    *   **Required Fix:** All placeholder content must be removed and replaced with the final, correct information. The paper cannot be accepted with these notes to the author still present.

#### MAJOR

*   **P4-M1: Unclear Definition of `canonical-N`**
    *   **Section/Page:** Sec. III B (p. 3).
    *   **Problem:** The text refers to a "(iii) canonical-N direct-MC NaMaster" estimator. The term "canonical-N" is not defined and appears to be a typo or an internal shorthand.
    *   **Required Fix:** Clarify what "canonical-N" means. If it is a typo for "canonical", correct it. If it has a specific meaning (e.g., related to a specific mask or weighting), define it explicitly.

*   **P4-M2: Effect Size for Harmonic-Channel Residuals**
    *   **Section/Page:** Abstract (p. 1), Sec. IV C/D (p. 10-11), Table IV (p. 12).
    *   **Problem:** The paper reports high-significance residuals in the harmonic channel (e.g., `+7.28σ`, `+7.93σ`). While correctly identified as systematics, the significance (`z` or `σ`) alone does not convey the physical magnitude of the effect. The paper's core argument is that these systematics are small in amplitude but appear significant due to the large dataset.
    *   **Required Fix:** For every reported high-significance systematic, the authors should also report the effect size in physical units (e.g., the raw `C_1` value or the corresponding RMS asymmetry amplitude in percent). This is crucial for putting the statistical significance into physical context and reinforcing the paper's argument. For example, next to "+7.28σ", also state the amplitude of the systematic itself.

#### MINOR

*   **P4-N1: Duplicate Phrase**
    *   **Section/Page:** Abstract (p. 1).
    *   **Problem:** The phrase "canonical unapodized" appears twice in close succession: "...a 500-MC direct run on the canonical unapodized mask; the 10^4-permutation canonical unapodized row in Table III...".
    *   **Required Fix:** Rephrase to avoid the repetition. For example: "...a 500-MC direct run on the canonical unapodized mask; the corresponding 10^4-permutation row in Table III...".

*   **P4-N2: Ambiguity in `A_ref` Source**
    *   **Section/Page:** Abstract (p. 1), Sec. I (p. 2).
    *   **Problem:** The text cites Shamir [1, 3] for the "1.7%-4.0% asymmetry range". It would be helpful to clarify if this range refers to per-bin asymmetry, a fitted dipole amplitude, or another quantity, as the definition of "asymmetry" can vary between analyses.
    *   **Required Fix:** Briefly clarify the definition of the asymmetry from the cited works to ensure the comparison is on a like-for-like basis. For example: "...Shamir's reported 1.7%-4.0% fitted dipole amplitude range...".

*   **P4-N3: Figure 9 Caption Clarity**
    *   **Section/Page:** Figure 9 caption (p. 17).
    *   **Problem:** The caption mentions an observed significance of `obs. σ = 7.21` from the `c9b` artifact, but notes this is not the "paper-canonical" value of `+7.28σ`. This could be confusing for a reader.
    *   **Required Fix:** Simplify the caption to only use the canonical value for clarity. State: "The observed significance in this channel is `σ = +7.28` (vertical line), a value attributed to systematics." The distinction between the 500-MC null and the 10^3-injection-background null is a minor detail that detracts from the figure's main point.

#### NIT

*   **P4-T1: Abbreviation `pp`**
    *   **Section/Page:** Sec. VII (p. 16), Table V caption (p. 12).
    *   **Problem:** The abbreviation "pp" is used for "percentage points". While common in some fields, it is less so in physics journals.
    *   **Required Fix:** Spell out "percentage points" or use the `%` symbol as appropriate to avoid ambiguity.

---

### Summary recommendation

**MAJOR REVISIONS**

This is a strong, methods-focused paper with a significant data product and a rigorous approach to systematics. The quality of the analysis is high, and the conclusions appear well-supported, pending the essential correction noted below. The paper would be a valuable contribution to the literature and the community.

However, the paper cannot be accepted in its current form due to the **ESSENTIAL** finding **P4-E1**. The discrepancy between the claimed and calculated significance of a primary scientific result (the WLS dipole exclusion) is a critical flaw that must be rectified. The presence of placeholder text (**P4-E2**) is also unacceptable for a final publication.

Assuming the authors can satisfactorily address these essential points and the major/minor points listed above, the paper should be suitable for publication in Physical Review D.