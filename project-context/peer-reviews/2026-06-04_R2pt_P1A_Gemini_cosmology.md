# P1A 2026-06-04_R2pt — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 74.2s

---

## Referee Report: P1A

**TO:** The Editor, Physical Review D
**FROM:** Referee
**RE:** Manuscript P1A, "Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"

This manuscript presents a theoretical investigation into four potential channels through which Einstein-Cartan-Holst (ECH) gravity could source late-time dark energy. The author(s) conclude that all four channels fail at the amplitude level under a set of stated assumptions. The paper's primary contributions are (1) a detailed "channel-level" closure of these four routes, and (2) a "perturbation-transparency theorem" demonstrating that for canonical scalar matter, the Holst sector decouples from standard cosmological perturbations.

The paper contains valuable results, particularly the perturbation-transparency theorem, which provides an important clarification on the observable consequences of minimal ECH gravity. The systematic, amplitude-level analysis of the four dark-energy routes is also a useful contribution. However, the manuscript suffers from significant structural and narrative issues that must be addressed before it can be considered for publication. The central argument regarding the dark energy mechanism is confusingly presented, and the paper's framing overstates the generality of its "closure" claims. Therefore, I recommend **MAJOR REVISIONS**.

Below are my detailed findings.

---

### ESSENTIAL Revisions

**P1A-E1: Inconsistent and Unphysical Dark Energy Mechanism**
*   **Location:** Primarily Sec II.C.1, Sec XII.A, and Sec XIV.D.
*   **Problem:** The paper's narrative regarding the closure of the ECH dark-energy mechanism is inconsistent and relies on a theoretically weak foundation.
    1.  The mechanism itself is based on a phenomenological ansatz (Eq. 6) which, as the author(s) correctly state in Appendix B, has an off-shell mass dimension of +1, not the required +4 for a local Lagrangian density. This means the proposed dark energy source is not a well-defined operator in an effective field theory.
    2.  The paper presents two different arguments for the failure of this mechanism: (a) a fine-tuning argument requiring N_tot ≈ 92 e-folds of inflation (the `D_inf` factor), which itself relies on a poorly justified `(T_reh/M_GUT)^(3/2)` prefactor; and (b) a "reheating thermal-reset barrier" (Sec II.C.1, Sec XII.A), which argues that any coherent axial current from the bounce would be washed out by thermalization, setting the torsion source to zero.
    3.  The thermal-reset argument is far more physical and robust than the `D_inf` bookkeeping. If it is correct, it closes the channel completely, rendering the `N_tot` tuning and the associated "structural tension" (Sec XIV.D) moot. The paper presents the structural tension as a key finding, but it is a tension between a non-viable dark energy model and a separate cosmological prediction. This is not a meaningful tension; it is simply another reason the DE model fails.
*   **Required Fix:** The manuscript must be restructured to present a single, coherent argument. I recommend elevating the robust "reheating thermal-reset" as the primary physical reason for the failure of a coherent torsion-sourced DE component. The dimensionally-problematic nature of the operator should be stated clearly upfront in the main text (not just the appendix) as the fundamental theoretical obstacle. The `N_tot` bookkeeping and the "structural tension" should be reframed as a secondary, illustrative calculation of the tuning that *would be* required *if* the operator were well-defined and *if* the thermal reset did not occur, rather than being presented as a primary result.

**P1A-E2: Version-History and Internal-Audit Artifacts**
*   **Location:** Title block, Data and Code Availability section, References.
*   **Problem:** The manuscript contains several artifacts that are inappropriate for a published paper.
    *   Title block: "(Dated: June 2, 2026 PDT — v1A.0.44)"
    *   Data and Code Availability (Sec XV): "...alongside the v1A.0.44 entry"
    *   Reference [31]: "...Used in P1A Sec. VI to point readers to..."
*   **Required Fix:** All version numbers, future dates, and internal-use annotations must be removed from the manuscript before publication.

**P1A-E3: Overly Dense and Discursive Footnotes**
*   **Location:** Table I (footnote b), Sec VII (footnote 1), Table III (footnote ‡).
*   **Problem:** Several footnotes contain a large amount of technical detail, analysis, and status updates on work from companion papers. This information is difficult to parse and breaks the flow of the main text. Critical details of a forecast or analysis should not be buried in a multi-line footnote.
*   **Required Fix:** The content of these long footnotes must be either summarized concisely in the main text or, if the detail is essential, moved to an appendix. The footnote on the DESI `w_0w_a` chain status in Table III is particularly problematic and reads like a live progress report; it should be replaced with a static statement about what has been done and what the results are, or removed if the results are not yet final.

### MAJOR Revisions

**P1A-M1: Paper Length and Structure**
*   **Location:** Primarily Sec IX.
*   **Problem:** The paper is 21 pages long, but its core, novel contributions could be presented more concisely. Section IX, "Structural Constraints on Dark-Energy Routes in Minimal ECH," presents a list of 14 "barriers." While comprehensive, this section reads like a catalog and dilutes the focus of the paper. Many of these barriers are well-known constraints in cosmology (e.g., attractor-sensitivity, Planck suppression) and are not specific novel results of this work.
*   **Required Fix:** To improve clarity and impact, the paper should be restructured. I recommend reducing Section IX to a short summary paragraph in the main text that references a new appendix containing the full, detailed list of 14 barriers. The main body of the paper should focus on a detailed exposition of its most significant contributions: the amplitude-level closure of the four specific routes (Sec IV) and the new perturbation-transparency theorem (Sec X). This would likely reduce the main paper length to a more standard ~15 pages and create a more focused narrative.

**P1A-M2: Framing of the "Closure" Claim**
*   **Location:** Abstract and Introduction (Sec I).
*   **Problem:** The paper's central claim is the "channel-level closure" of four dark energy routes. However, as established in P1A-E1, the primary mechanism under consideration is based on a dimensionally-flawed ansatz. The current framing might lead a reader to believe that general, well-defined EFT pathways have been closed, which is not the case. The work is more accurately described as an assessment of specific, phenomenologically-motivated (and ultimately unphysical) *ansatze*.
*   **Required Fix:** The abstract and introduction should be revised to more precisely frame the paper's contribution. The language should make it clear from the outset that the dark-energy mapping being tested is a specific *ansatz* that is not a controlled EFT operator. This is not to diminish the work—the systematic refutation is still valuable—but to ensure the scope of the claim is accurately represented. The current phrasing "we assess four enumerated minimal-Einstein-Cartan-Holst (ECH) spin-torsion channels" should be qualified, for example: "we assess four candidate dark-energy channels derived from a specific, phenomenological ansatz within the minimal Einstein-Cartan-Holst (ECH) framework...".

### MINOR Revisions

**P1A-m1: Justification of Prefactor in Dilution Formula**
*   **Location:** Sec II.C.1, Eq. (11).
*   **Problem:** The `(T_reh/M_GUT)^(3/2)` matching coefficient is justified on grounds of "dimensional-analysis aesthetic" and "phenomenological phase-space ansatz". This is not a rigorous derivation.
*   **Required Fix:** While the ESSENTIAL revision P1A-E1 recommends de-emphasizing this entire calculation, if it is retained in any form, this justification must be strengthened or, at a minimum, be more explicitly caveated as a toy-model parameterization with no claim to rigor.

**P1A-m2: Acknowledgement of AI Assistant**
*   **Location:** Acknowledgments.
*   **Problem:** The acknowledgement of "Claude (Anthropic) as an AI research assistant" is unconventional. While transparency is laudable, journals are still developing policies on this matter.
*   **Required Fix:** The author(s) should verify this form of acknowledgement is consistent with the journal's policy. A more standard phrasing might be to acknowledge the use of specific software tools.

### NITs (Nitpicks)

**P1A-N1: Convoluted Phrasing in Abstract**
*   **Location:** Abstract.
*   **Problem:** The sentence "Through 7 foundation studies... they are not logically independent)" is long and difficult to read.
*   **Required Fix:** Consider simplifying this sentence for clarity. For example: "We present 13 logically-independent constraints on these channels, derived from 7 foundational principles and 6 observational branches."

**P1A-N2: Future Date in Submission**
*   **Location:** Title Block.
*   **Problem:** The date is listed as "June 2, 2026".
*   **Required Fix:** Correct the date to the current submission date.

---

## Summary recommendation

**MAJOR REVISIONS**

This paper presents two valuable contributions to the study of bouncing cosmologies in the ECH framework: a systematic audit of four proposed dark-energy channels and a clean, powerful perturbation-transparency theorem. The transparency theorem, in particular, is a significant result that clarifies which observables are (and are not) affected in this class of models. However, the manuscript is undermined by a confused narrative surrounding its central claim of "closing" dark energy routes. It relies on a dimensionally-inconsistent operator and presents conflicting arguments for its failure, obscuring the most physically robust reasoning. The paper is also longer than necessary due to a lengthy catalog of constraints that could be moved to an appendix. By restructuring the narrative to be more direct about the theoretical weaknesses of the DE ansatz, elevating the most physical arguments, and streamlining the presentation, the authors can produce a much stronger and more impactful paper that highlights its genuine contributions. The work is promising but is not yet in a suitable state for publication.