# P4 2026-06-04_R6clean — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 77.0s

---

## Referee Report: Survey-Scale Galaxy Chirality with Equivariant TTA

**Manuscript ID:** [Assigned by editor]
**Title:** Survey-Scale Galaxy Chirality with Equivariant TTA: A −0.12σ Subsample-Mask ℓ=1 Null, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)
**Author(s):** Houston Golden

This paper presents a detailed analysis of galaxy chirality using a large dataset of 3.2 million spiral galaxies from the DESI Legacy Surveys. The primary scientific result is a null detection of a chirality dipole at the ℓ=1 multipole, placing a strong constraint on cosmological anisotropy. The authors perform an exceptionally thorough systematics analysis, demonstrating that previous claims of a signal can be explained by a quantifiable leakage channel where a small classifier monopole couples to the survey mask geometry. A residual +3.64σ signal found on a specific "canonical" mask is convincingly shown to be the result of a depth/morphology-correlated systematic, not a primordial signal.

The methodology is robust, and the paper's careful distinction between parity-even (isotropy) and parity-odd (parity violation) observables is a crucial and welcome clarification for this field of research. The scientific conclusions are well-supported by the evidence. However, the manuscript in its current form is excessively long, which significantly hinders its readability and impact. A major restructuring is required before it can be considered for publication.

### Findings

#### ESSENTIAL

No findings are classified as essential, as the core scientific methodology and conclusions are sound. The major revision concerning the paper's length must be addressed for the paper to be publishable.

#### MAJOR

**P4-M1: Paper Length and Structure**
*   **Location:** Entire manuscript.
*   **Problem:** The paper is 54 pages long, with a main text of approximately 45 pages. This is excessive for a PRD publication. The core scientific contributions—a null dipole result and a detailed characterization of a key systematic—are buried in a large number of secondary checks and detailed explanations. This significantly hinders readability and obscures the primary impact of the work.
*   **Fix:** The paper must be substantially restructured and shortened. The recommended target length is 15-20 pages for the main text.
    *   The main text should focus on the primary narrative: (1) Introduction, (2) Data and Core Methodology (TTA), (3) Main Results (the null dipole on the subsample mask, the detection of the +3.64σ residual on the canonical mask), (4) Interpretation of the Residual (the multi-null battery and cross-spectrum results), (5) Discussion of the result's implications (comparison to prior work, theoretical context), and (6) Conclusions.
    *   The following sections should be moved to appendices or significantly condensed: Detailed Bias Hardening Suite description (Sec. III.F), Two-Point Correlation Function (Sec. IV.F), detailed Signal-Hunt Diagnostics (Sec. IV.E, I, J, K), detailed Sensitivity Floor derivation (Sec. VI.C), and the Mask Robustness sweep (Sec. VI.F).
    *   This restructuring will make the paper's significant contributions much clearer and more accessible to the reader.

#### MINOR

**P4-m1: Future Date**
*   **Location:** Page 1, Title block.
*   **Problem:** The date of the paper is listed as "June 4, 2026 PDT", which is in the future.
*   **Fix:** Correct the date to the current submission date.

**P4-m2: Inconsistent Notation for Multipole Moment**
*   **Location:** Throughout the manuscript.
*   **Problem:** The paper uses both `l` and `ℓ` to denote the spherical harmonic multipole moment. For example, the abstract uses `ℓ = 1` and `l=1` in the same paragraph.
*   **Fix:** Use a single, consistent symbol throughout the paper. The standard in cosmology and for PRD is `ℓ`.

**P4-m3: Clarification of "Canonical-Mask" vs "Subsample-Mask"**
*   **Location:** Abstract, Sec IV.C, Conclusions.
*   **Problem:** The paper presents two key results on two different masks: a null on the "subsample-mask" (fsky=0.659) and a +3.64σ residual on the "canonical-mask" (fsky=0.49005). While the "Declared Analysis Hierarchy" (Sec III.A) and other sections clarify the authors' intent, the motivation for this choice could be made clearer upfront for the reader.
*   **Fix:** In the abstract, briefly state *why* the subsample mask is the primary one for the cosmological test (e.g., "on our largest, most contiguous sky mask designed to minimize mask-edge systematics..."). This will help the reader immediately understand why the -0.12σ result is the headline, despite the presence of a +3.64σ signal on a different, diagnostic mask.

**P4-m4: Scope of Parity-Even Claim**
*   **Location:** Abstract, Sec VI.G.
*   **Problem:** The paper correctly and importantly states that the `ℓ=1` dipole of a pseudoscalar field is a parity-EVEN, axial-vector quantity that tests for isotropy, not parity violation. This is a critical distinction.
*   **Fix:** To further reinforce this crucial point for readers who may only skim the abstract, I suggest adding a brief parenthetical clarification after the parity-EVEN statement, e.g., "...it is NOT a direct parity-violation test (the parity-odd analog requires...); it is a test for a preferred direction (anisotropy) in the universe." The current text is already good, but this small addition would strengthen the message.

#### NIT (Typos and Formatting)

**P4-n1: Typographical and Formatting Errors**
*   **Location:** Various.
*   **Problem:** Several minor typographical and formatting errors are present.
*   **Fix:** Please proofread the manuscript carefully and correct the following (and any other) errors:
    *   Abstract, p. 1: "471 049" should be "471,049".
    *   p. 3, col 2: "3.2×106-spiral catalogue" should be "3.2 × 10^6-spiral catalogue" or similar standard notation.
    *   p. 9, Table II, footnote c: "primary primary channel" should be "primary channel".
    *   p. 21, Table VII, Statistic column: "Pre-MASTER pseudo-C(l=1)l" appears to have a stray "l" at the end.
    *   p. 29, Table XI caption: The union symbol "U" is rendered as "U". Please use the correct LaTeX command `\cup`.
    *   p. 41, Sec VI.D.0.c: A cross-reference appears as "§??". This needs to be corrected.
    *   p. 48, Sec VIII.b: "Bandpower US single-l" should be "Bandpower vs single-l".
    *   p. 52, Fig 10 caption: "(the see Sec. IV D)." is grammatically awkward. Rephrase to "(see Sec. IV D)".
    *   p. 53, Fig 11 title: The title "Fig. 11: Raw vs Equivariant..." is redundant with the figure number and caption below it. Please remove the in-figure title.

## Summary recommendation
**MAJOR REVISIONS**

The paper presents a high-quality, thorough, and impactful analysis that provides a definitive null result for the galaxy chirality dipole at unprecedented sensitivity. The methodological contributions, particularly the detailed systematics treatment and the clarification of the observable's physical nature (isotropy vs. parity), are of great value to the community. The primary reason for the "Major Revisions" recommendation is the manuscript's excessive length, which makes it difficult to parse and lessens its impact. A significant restructuring to a more concise main paper with detailed supporting information moved to appendices is necessary. Once this is addressed, the paper will be an excellent candidate for publication in Physical Review D.