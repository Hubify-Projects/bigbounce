# P1A RA-INT-v92 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1a_ech_nogo.pdf` md5=7488bd1c pages=36
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 141.7s

---

**Referee Report**

**Paper ID:** P1A
**Title:** Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter

This paper presents a comprehensive theoretical and phenomenological assessment of minimal Einstein-Cartan-Holst (ECH) gravity as a source for late-time dark energy. The work makes three primary claims: (1) a "channel-level closure" of four commonly discussed routes by which ECH could source dark energy; (2) a perturbation-transparency theorem for canonical scalar matter, showing that the Holst sector decouples from scalar and tensor perturbations to all orders; and (3) the identification of a structural tension between the requirements for the ECH dark-energy mechanism and the survival of an observable matter-bounce non-Gaussianity signature (`fNL`).

The analysis is exceptionally thorough, well-structured, and intellectually honest about its own limitations. The authors are careful to distinguish between rigorous results, structural arguments based on symmetries and naturalness, and estimates based on explicitly labeled phenomenological ansätze. This clarity is a major strength of the manuscript.

The perturbation-transparency theorem (Sec. X) is a rigorous and significant result. The proof, based on the vanishing of the Holst dual contraction via the first Bianchi identity on a torsion-free connection, is sound and clearly presented. This result cleanly separates the phenomenology of minimal ECH with scalar matter into standard GR for perturbations and potentially non-trivial effects in non-perturbative channels (like ALP birefringence).

The four-route closure analysis (Sec. IV) is also compelling. Each route is closed by a different but appropriate type of argument: amplitude suppression for the NJL contact term (R1), massive Planck and loop suppression for one-loop terms (R2, R3), and a well-articulated naturalness/explanatory-deficit argument for the spectator ALP scenario (R4). The supporting catalog of 14 constraints (Sec. IX) provides a powerful, systematic map of the theory's failure modes.

Finally, the structural tension argument (Sec. XIV D) is a crucial finding. The demonstration that the ~92 e-folds required for the dark energy mechanism would erase the matter-bounce `fNL` signature at observable scales effectively shows that these two phenomenological programs are mutually exclusive within this framework.

The manuscript is largely self-contained, with numerical values from companion works clearly isolated as "illustrative" and not load-bearing for the primary theoretical conclusions. The use of a dedicated table (Table III) to classify the evidentiary status of each claim is a model of transparency that should be encouraged.

While the paper is long, its length is justified by the depth and breadth of the analysis. The claims are well-supported by the internal logic and calculations. The paper represents a substantial and definitive contribution to the literature on torsion-based cosmologies. I recommend publication after a few minor points are addressed.

---
**Findings**

**ESSENTIAL**

*   None.

**MAJOR**

*   None.

**MINOR**

*   **P1A-N1 (Sec. I, p. 3): Typo in Citation Year.** The paper is dated "June 30, 2026" and cites DESI results from "2024-2025" with preprint numbers like `arXiv:2503.14738`. While this "written from the future" style is unusual, it is internally consistent. However, the reference `[10]` is cited as `(2025)`. If the paper's date is 2026, this is fine. But if the date is a placeholder to be replaced with the current date upon submission, this should be checked for consistency.
    *   **Problem:** Potentially confusing dating of references relative to the paper's own date.
    *   **Fix:** The authors should either commit to the "futuristic" dating scheme consistently or update the paper's date and reference dates to the time of submission. A brief explanatory note to the editor might be warranted if the former is chosen.

*   **P1A-N2 (Sec. IV D, p. 14, footnote 4): Clarity on field normalizations.** Footnote 4 provides a crucial clarification on the normalization of the pseudoscalar field (`φ` vs `θ`) and the decay constant `fa`. The text says "Throughout this paper there is one pseudoscalar field and two normalizations of it". This is clear, but the main text alternates between `φ` and `θ` (e.g., Appendix C uses `θ` extensively). This could still be slightly confusing.
    *   **Problem:** The relationship between `φ`, `θ`, and `fa` is critical but is explained in a footnote and the main text alternates between conventions.
    *   **Fix:** Recommend elevating the core of footnote 4 into the main text of Sec. IV D at the first introduction of the ALP operator `Lcs`. For example: "...coupling `Θμφ Κμν` (equivalently `φF F~`...). Here `φ` is the canonical dimension-1 pseudoscalar field, related to the dimensionless angle `θ` by `φ = fa θ`, where `fa` is the decay constant. We adopt this normalization..." This would improve readability and ensure this crucial point is not missed.

*   **P1A-N3 (Sec. XII A, p. 22): Clarification on "fine-tuning reduction".** The text states: "The 'fine-tuning reduction from 10^122 to 10^5' is a reparameterization as sensitivity to Ntot... not a resolution of the cosmological constant problem." This is an excellent and crucial point. However, the number `10^5` comes from the sensitivity to `ΔNtot`, where `e^(3*ΔNtot)` is the change in the suppression factor. A `ΔNtot` of 4 e-folds gives `e^12 ≈ 1.6e5`. The text should briefly show this calculation to make the origin of the `10^5` number explicit.
    *   **Problem:** The origin of the `10^5` fine-tuning score is not immediately obvious from the text.
    *   **Fix:** Add a brief parenthetical calculation, e.g., "...the residual 10^5 tracks `e^(+3ΔNtot)` for a residual uncertainty in the number of e-folds of `ΔNtot ≈ 4` (since `e^(3*4) ≈ 1.6 × 10^5`), and inherits its sensitivity..."

**NIT**

*   **P1A-T1 (Sec. XIII, p. 24): Minor phrasing.** The text says "The same ALP setup arises identically in standard GR with the same parameters, so this is not a distinctive ECH prediction." This is correct. A slightly clearer phrasing might be "...arises in standard GR when supplemented with an identical ALP field..." to emphasize the ALP is an addition to GR in that context.
    *   **Problem:** Minor ambiguity in phrasing.
    *   **Fix:** Consider rephrasing to "...in standard GR supplemented with an identical ALP sector..." or similar.

---
## Summary recommendation

**ACCEPT WITH MINOR CORRECTIONS**

This is an excellent paper. It is comprehensive, rigorous where it claims to be, and commendably transparent about its assumptions and limitations. The main results—the perturbation-transparency theorem and the channel-level closure of the minimal ECH dark-energy program—are significant and well-supported. The manuscript is a definitive statement on this topic and will be a valuable reference for the community. The required corrections are minor and intended only to further improve the already high level of clarity. I strongly recommend publication.