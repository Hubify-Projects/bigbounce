# P1A R40 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1a_ech_nogo.pdf` md5=f1eab008 pages=29
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 177.9s

---

# Referee Report for "Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"

## Summary of the Paper
This manuscript investigates four potential channels through which Einstein-Cartan-Holst (ECH) gravity could source late-time dark energy. The authors conclude that all four channels are closed under a set of stated assumptions. Three routes (NJL, one-loop EA, Immirzi running) are found to be amplitude-suppressed. The fourth (parity-odd CMB coupling) is closed by a naturalness objection, as it re-imports the cosmological constant fine-tuning problem. The paper's central positive result is a "perturbation-transparency" theorem: for canonical scalar matter, the Holst sector decouples from all scalar and tensor perturbation equations of motion. The authors also identify a structural tension between the ECH dark-energy mechanism and a key prediction of matter-bounce models (`f_NL = -35/8`), arguing the former would erase the latter. The paper frames its conclusions as a "channel-level closure" rather than a complete operator-level no-go theorem.

## General Comments
The paper presents a systematic and ambitious analysis of the phenomenological viability of minimal ECH as a source for dark energy. The approach of enumerating routes and closing them via a catalog of "barriers" is well-structured and provides a clear logical flow. The authors are commendably transparent about the central weakness of the dark-energy mapping: its reliance on a phenomenological, dimensionally-inconsistent scaling ansatz, which is explicitly acknowledged throughout the text and in Appendix B. The perturbation-transparency result is a potentially significant finding for the field.

However, the manuscript suffers from two essential flaws that preclude its publication in the present form. First, the proof of the central perturbation-transparency theorem appears to contain a mathematical error regarding the behavior of the Holst term. Second, the paper is not self-contained and relies critically on multiple companion papers that are "in preparation" or "posted concurrently," rendering many of its observational claims and supporting analyses unverifiable.

A major revision is required to address these points. If they can be satisfactorily resolved, the paper would represent a valuable contribution to the literature on modified gravity and bouncing cosmologies.

---
## Detailed Findings

### ESSENTIAL Revisions

**P1A-E1: Mathematical Error in the Proof of the Perturbation-Transparency Result**
-   **Section/Page**: Sec. X.B (p. 19), Sec. X.D (p. 20)
-   **Problem**: The proof of the main theoretical result rests on the claim that the Holst dual contraction, `ε^μνρσ R_μνρσ`, "vanishes identically on the Levi-Civita connection (T = 0) by the first (algebraic) Bianchi identity `R_μ[νρσ] = 0`". This claim is repeated in Eq. (23). This appears to be incorrect. The quantity `ε^μνρσ R_μνρσ` is the Pontryagin density, which is a well-known topological invariant. It is a total derivative, but it is not identically zero pointwise on a general curved manifold. The conclusion that the Holst term does not affect the classical equations of motion is correct *because* it is a total derivative, but the justification provided ("vanishes identically") is wrong. The manuscript itself seems confused on this point, with footnote 8 (p. 20) acknowledging a previous misidentification, yet the incorrect "identically zero" language persists in the main proof. Footnote 7 (p. 20) makes the even stronger, and likely incorrect, claim that the Nieh-Yan density `NY|T=0 = d(0) = 0` pointwise.
-   **Required Fix**: The authors must correct the proof in Sec. X.B and Sec. X.D. The argument should be rephrased to state that for a torsion-free connection (`T=0`), the Holst term becomes the Nieh-Yan density, which is a total derivative. As such, it does not contribute to the variational equations of motion at any order in perturbation theory. All claims of "pointwise vanishing" or the term being "identically zero" must be removed and replaced with the correct "total derivative" argument. This correction must be applied consistently throughout the manuscript, including in the abstract and conclusions.

**P1A-E2: Lack of Self-Containedness and Reliance on Unavailable Companion Papers**
-   **Section/Page**: Throughout, e.g., Sec. I (p. 4), Sec. III.B (p. 10), Sec. V (p. 15), References [2, 6, 23, 46].
-   **Problem**: The paper's arguments and conclusions rely heavily on numerical results, data analyses, and forecasts from at least four companion papers that are cited as "in preparation" or "posted concurrently on arXiv". This includes:
    -   The `f_NL = -35/8` forecast and its significance (Ref. [2]).
    -   All MCMC-derived cosmological parameter values, pipeline validation, and ALP parameter fitting (Ref. [6]).
    -   The confirmed null result for galaxy spin asymmetry (Ref. [23]).
    -   The NANOGrav reanalysis providing the `γ_PTA` value (Ref. [46]).
    A manuscript submitted for peer review must be verifiable on its own merits. Citing unavailable work for load-bearing claims is not acceptable practice for PRD.
-   **Required Fix**: The manuscript must be made self-contained. The authors have two options:
    1.  Incorporate the essential methods and results from the companion papers into the present manuscript, perhaps in appendices. This would include, at minimum, a summary of the MCMC setup and posteriors, the galaxy spin analysis method and null result, and the Fisher forecast methodology for `f_NL`.
    2.  Drastically rewrite the paper to be a purely theoretical investigation. All claims based on the specific numerical results from the companion papers would have to be removed or rephrased in a qualitative, illustrative way that does not depend on the unavailable work. The current framing, which presents these results as key pieces of evidence, is untenable.

### MAJOR Revisions

**P1A-M1: Unsubstantiated Claims Based on Internal, Uncitable MCMC Results**
-   **Section/Page**: Sec. I (p. 4), Table IV (p. 27)
-   **Problem**: The paper states that "Cosmological parameter values referenced in this paper... are drawn from the companion internal MCMC analysis... they are documented internally rather than as externally citable arXiv-posted numbers". This is a direct consequence of P1A-E2 but warrants a separate flag. The paper cannot use uncitable internal numbers to support any of its claims, such as consistency with `ΛCDM` for `H_0` or the value for `ΔN_eff`.
-   **Required Fix**: Remove all claims based on these internal MCMC results. If the authors wish to make claims about cosmological parameter consistency, they must either include the full, reproducible analysis in this paper or cite a publicly available, peer-reviewed analysis.

**P1A-M2: Ambiguity in the Core Dark-Energy Mechanism**
-   **Section/Page**: Sec. II.A.2 (p. 6-7), Appendix B (p. 26)
-   **Problem**: The entire dark-energy component of the paper rests on a "phenomenological on-shell scaling ansatz" that is required to fix the mass dimension of the parity-odd operator (Eq. 6). The paper is admirably honest about this, but it remains a profound weakness. The physical justification for the `(T_reh/M_GUT)^(3/2)` factor in Eq. (11) is described as a "dimensional-analysis aesthetic" and is not derived.
-   **Required Fix**: While a full derivation may be beyond the scope, the authors should provide a more robust physical motivation for their scaling relations. For instance, can the phase-space argument for the `(T_reh/M_GUT)^(3/2)` factor be elaborated upon? As it stands, the dark-energy claims are built on a foundation that is explicitly acknowledged to be an un-derived ansatz, which significantly weakens the conclusions about "closure". The authors should consider toning down the language of "closure" to reflect its conditionality on this ansatz.

### MINOR Revisions

**P1A-N1: Juxtaposition of Significance Values**
-   **Section/Page**: Abstract (p. 1)
-   **Problem**: The abstract lists several `σ` values (`~3.6σ`, `~2.9σ`, `2.6-5σ`) and correctly notes that they "are not directly comparable".
-   **Required Fix**: This good practice should be maintained everywhere such values are compared. For example, in the main text where these values are discussed, the same caveat should appear each time to prevent misinterpretation by the reader.

**P1A-N2: Redundant Figure**
-   **Section/Page**: Figure 6 (p. 22)
-   **Problem**: Figure 6 appears to be a less-detailed duplicate of the information already presented in Figure 4 (p. 15). It shows the same significance forecast tracks but omits the milestone annotations and the discussion of the correlation coefficient `ρ`.
-   **Required Fix**: The authors should consider removing Figure 6 and referring back to Figure 4 in the text of Sec. XII.B to avoid redundancy.

**P1A-N3: Verifiability of Quoted Numbers**
-   **Section/Page**: Sec. X.G (p. 20)
-   **Problem**: The paper quotes the matter-bounce prediction for the PTA spectral index as `γ_PTA = 3.0`. This corresponds to a scale-invariant spectrum of scalar perturbations sourcing the gravitational waves.
-   **Required Fix**: Please provide a specific citation for this value in the context of matter-bounce models.

**P1A-N4: Clarification of Parity-Odd Labeling**
-   **Section/Page**: Sec. IV.B (p. 12)
-   **Problem**: The section is titled "closed by parity-odd coefficient", but footnote 3 correctly explains that the operator in Eq. (14) is intrinsically parity-even, and the parity violation arises from a background expectation value. This could be confusing.
-   **Required Fix**: Consider rephrasing the section heading or adding a brief clarification in the main text to reflect that the phenomenology is parity-violating, even if the operator itself is not. For example: "Route 2 (...): closed by suppression of its parity-violating phenomenology".

### NITs (Cosmetic)

**P1A-T1: Dating of Manuscript**
-   **Section/Page**: p. 1
-   **Problem**: The date is listed as "June 13, 2026".
-   **Required Fix**: Correct the date to the submission date.

---
## Summary Recommendation

**MAJOR REVISIONS**

This paper presents a valuable and systematic, if conditional, no-go analysis for a class of modified gravity models. The perturbation-transparency result is novel and important. However, the essential flaws identified—the mathematical error in the proof of this key result and the complete lack of self-containedness due to reliance on unavailable companion papers—make it unsuitable for publication in its current form. The authors must rigorously correct their central proof and make the paper's evidence verifiable by either incorporating the missing analyses or removing the claims based upon them. If these fundamental issues are addressed, the revised manuscript has the potential to be a strong contribution to the field.