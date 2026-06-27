# P1A R53 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/private/tmp/R53_P1A/paper1a_ech_nogo.pdf` md5=1996d408 pages=29
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 136.3s

---

**Referee Report for PRD Manuscript**

**Manuscript ID:** [Assigned by system, e.g., CZ12345]
**Title:** Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter
**Author:** Houston Golden

This paper presents a phenomenological assessment of four specific channels within Einstein-Cartan-Holst (ECH) gravity as potential sources for late-time dark energy. The author argues for a "channel-level closure" of these routes, meaning they are either amplitude-suppressed, parity-even, or require fine-tuning that re-introduces the cosmological constant problem. The paper's central positive results are a "perturbation-transparency" theorem for canonical scalar matter in ECH and the identification of a structural tension between the conditions required for ECH-driven dark energy and the survival of a matter-bounce signature in the non-Gaussianity parameter `f_NL`.

The work is ambitious and synthesizes a wide range of theoretical and observational concepts. The perturbation-transparency result is clean and potentially significant. The structural tension argument is a strong internal consistency check. However, the central "closure" or "no-go" claim regarding dark energy is conditional on a phenomenological scaling ansatz that is not derived from the underlying theory. This significantly weakens the conclusion from a theorem to a conditional constraint. Furthermore, the paper relies heavily on results and detailed analyses from companion papers cited as "in preparation," which prevents a full, self-contained assessment of its claims. These issues require major revisions before the manuscript can be considered for publication in Physical Review D.

---
### Detailed Findings

#### ESSENTIAL REVISIONS

**P1A-E1: Conditional Nature of the Main "No-Go" Result**
*   **Location:** Abstract (p. 1), Sec. I (p. 3), Sec. IV (p. 10), Appendix B (p. 26).
*   **Problem:** The paper's primary claim—the closure of four minimal ECH dark-energy routes—is critically dependent on a "phenomenological on-shell scaling ansatz" (explicitly stated in the abstract and detailed in Appendix B). This ansatz, `ρ_bounce ~ (α/M) M_Pl^4`, is required to promote a dimension `+1` operator to a dimension `+4` energy density. The paper is commendably transparent about this being an ansatz, not a derivation. However, this fundamentally changes the nature of the result. A "no-go" or "closure" based on an assumption is not a theorem; it is a constraint within a specific, assumed phenomenological model. The framing throughout the paper, especially the title and abstract, should more strongly reflect this conditional nature.
*   **Fix:**
    1.  The title should be revised to reflect the conditional, ansatz-dependent nature of the closure argument. For example, "Conditional Constraints on..." or "Ansatz-Dependent Closure of...".
    2.  The abstract's opening sentence should be rephrased. Instead of "We assess... and find that each is constrained," it should read something like, "Under a specific phenomenological scaling ansatz, we assess... and find that each is constrained."
    3.  The conclusions (Sec. XV) must reiterate that the dark-energy closure part of the argument is not a general proof but holds only if the scaling ansatz is valid.

**P1A-E2: Reliance on "In Preparation" Companion Papers**
*   **Location:** Throughout the paper, e.g., Abstract (p. 1, refs [1], [2], [5]), Sec. I (p. 3, ref [2], [6]), Sec. IV (p. 4, ref [6]), Sec. XV (p. 25, ref [2]).
*   **Problem:** The manuscript is not self-contained. It makes numerous load-bearing claims that are justified only by citation to companion papers listed as "in preparation" or posted concurrently. This includes:
    *   The detailed `f_NL = -35/8` SPHEREx Fisher forecast ([2]).
    *   The MCMC analysis providing the cosmological parameters used (`H_0`, `ΔN_eff`) and the `ACDM+ΔN_eff` verification ([6]).
    *   The spectator-ALP parameter fitting and NaMaster pipeline validation ([6]).
    *   The galaxy chirality analysis and null result ([23], also listed as a concurrent companion).
    A manuscript submitted to PRD must be verifiable on its own merits. Key evidence cannot be located in papers that are not yet available or have not undergone peer review.
*   **Fix:** The manuscript must be made self-contained.
    1.  For any result essential to the main argument (e.g., the MCMC-derived parameters, the core methodology of the `f_NL` forecast), a summary of the method and results must be included in an appendix of the present paper.
    2.  Alternatively, publication of this manuscript should be delayed until the essential companion papers are accepted for publication or are available on the arXiv in a final, citable form. Citing works as "in preparation" for central results is not acceptable.

**P1A-E3: Abstract-Body Mismatch (Abstract-Last Drift Sweep)**
*   **Location:** Abstract (p. 1) vs. Body.
*   **Problem:** The abstract presents a list of claims, but their relative weight and certainty as established in the body are not perfectly reflected.
    1.  The abstract states R1-R3 "are amplitude-suppressed under explicitly-labeled scaling ansätze". The body shows R1 (NJL) closure is a standard result not dependent on a new ansatz, while R2/R3 depend on EFT ansätze for their coefficients. This distinction is lost.
    2.  The abstract presents the `f_NL = -35/8` and `β ≈ 0.27°` predictions as key "surviving" observables. While the body correctly qualifies them as non-ECH predictions, the abstract could be misread as suggesting these are positive predictions *of the framework being tested*. The framing "The two predictions discussed below as 'surviving' are accordingly not predictions of ECH itself" is good, but this nuance could be made even clearer from the outset.
*   **Fix:**
    1.  Reword the abstract to clearly separate the closure of R1 (standard derivation) from the ansatz-dependent closure of R2-R3.
    2.  Strengthen the language in the abstract to emphasize that the "surviving" predictions are class-level tests for broader scenarios (matter bounce, GR+ALP) that are simply *not ruled out* by this paper's analysis of minimal ECH, rather than being positive outcomes of it.

#### MAJOR REVISIONS

**P1A-M1: Unjustified Quantitative Claims and Terminology**
*   **Location:** Sec. I (p. 3), Sec. IV (p. 10), Sec. IX (p. 16).
*   **Problem:** The paper introduces non-standard terminology like "channel-level closure" and "amplitude-budget granularity" without clear, rigorous definitions. While the intent is understandable (to distinguish from a full operator-level proof), these terms risk being ambiguous. Furthermore, the 14 "barriers" in Sec. IX are a mix of rigorous calculations, known theoretical problems, and heuristic arguments. They are not all on the same logical footing.
*   **Fix:**
    1.  Provide a concise, formal definition of "channel-level closure" and "amplitude-budget granularity" in the introduction.
    2.  In Sec. IX and Table II, classify the barriers more explicitly based on their nature (e.g., "Derived Constraint," "Heuristic Argument," "Known Fine-Tuning Problem"). For example, Barrier 9 (Liouville Conservation) is described as a "heuristic closure," which is honest but highlights the mixed nature of the list. This structure should be made more transparent.

**P1A-M2: Structural Tension Argument (`N_tot` vs. `f_NL`)**
*   **Location:** Abstract (p. 1), Sec. XIV D (p. 24).
*   **Problem:** The argument that the `N_tot ≈ 92` e-folds required for the DE mechanism would erase the `f_NL = -35/8` signal is powerful and appears physically sound. However, the calculation is presented at a bookkeeping level. A quantitative transfer function that tracks the relative amplitude of the matter-bounce contraction modes versus the vacuum-inflationary modes as a function of `N_tot - N_exit` is needed to make this definitive. The paper defers this to a companion forecast paper ([2]).
*   **Fix:** While the full forecast can remain in the companion paper, a more detailed calculation should be presented in an appendix here. This should include the standard expressions for the bispectrum from both sources and show explicitly how the inflationary contribution comes to dominate when the physical wavelength at the bounce is deep inside the horizon. This would make the argument self-contained and much stronger.

**P1A-M3: Scope of the "Perturbation-Transparency" Result**
*   **Location:** Abstract (p. 1), Sec. X (p. 20).
*   **Problem:** The paper presents a "perturbation-transparency result" as a central finding. The proof in Sec. X is clean and correct *for canonical scalar field matter*. The abstract and conclusions state this limitation. However, the physical relevance should be discussed more. Standard Model matter is fermionic. While scalar fields (like the inflaton) are central to cosmology, a result that holds only for scalars and not for fermions in a theory whose main non-triviality (torsion) comes from fermions is a major restriction.
*   **Fix:** Add a paragraph in the Discussion (Sec. XII) or Implications (Sec. X.F) explicitly addressing the implications of this result for a universe containing Standard Model fermions. It should clarify that any observable ECH-torsion effects in perturbations *must* come from the fermion sector, thereby focusing attention on where to look for such effects in more complete models.

#### MINOR REVISIONS

**P1A-m1: Future Date on Manuscript**
*   **Location:** Page 1.
*   **Problem:** The manuscript is dated "June 19, 2026". This is presumably a placeholder or a typo.
*   **Fix:** Correct the date to the actual submission date.

**P1A-m2: Ambiguity in `σ` Significance for SPHEREx `f_NL` Forecast**
*   **Location:** Abstract (p. 1), footnote 6 (p. 15), Fig. 4 caption (p. 16).
*   **Problem:** The paper quotes a "2.6-5σ" realistic significance for the SPHEREx `f_NL` forecast. The range is quite large. Footnote 6 explains it reflects two regimes based on the level of systematic degradation (`σ(f_NL) ≈ 0.7` vs. `σ(f_NL) ≈ 1.0`). While the explanation is present, presenting such a wide range in the abstract is slightly jarring.
*   **Fix:** In the abstract, either provide a single, conservatively degraded number (e.g., `~2.6σ`) and mention the potential for higher significance in the body, or briefly state the source of the range (e.g., "at 2.6-5σ significance, depending on final systematic uncertainties").

**P1A-m3: Figure 5 Fine-Tuning Comparison**
*   **Location:** Figure 5 (p. 18).
*   **Problem:** The bottom panel compares the "Fine-Tuning Score" of different models. The `10^5` score for "Spin-Torsion" is based on the reparameterization of the CC problem into a sensitivity to `N_tot`. While the caption and body are clear this does not *solve* the problem, comparing this `10^5` (a sensitivity to an initial condition) with `10^120` (a ratio of physical scales) is an apples-to-oranges comparison.
*   **Fix:** The figure is illustrative, but the caption should be strengthened to state explicitly that the "scores" are not directly comparable as they measure different types of fine-tuning (e.g., "parameter fine-tuning vs. initial-condition sensitivity").

**P1A-m4: Data Availability Section**
*   **Location:** Page 26.
*   **Problem:** The link provided (`https://github.com/Hubify-Projects/bigbounce/tree/main/reproducibility`) is good. However, the text mentions "a Zenodo-archived release will pin all artifacts to the submitted-version snapshot." For publication, this should not be a future action.
*   **Fix:** The authors should create the Zenodo archive and provide the DOI in the manuscript before publication. The phrase "will pin" should be changed to "are pinned at [DOI]".

#### NIT-PICKS

**P1A-N1: Redundant Phrasing in Footnote**
*   **Location:** Page 6, footnote 2.
*   **Problem:** The footnote contains the phrase "the displayed T^abc T_abc in Eq. (1) is not an independent kinetic term but the on-shell Hehl-Datta shorthand...". The main text immediately above the footnote marker says almost the exact same thing.
*   **Fix:** Condense the footnote or the main text to avoid repetition.

**P1A-N2: Citation Formatting**
*   **Location:** Bibliography (p. 28-29).
*   **Problem:** Some recent preprints are cited with `arXiv preprint (2025)` or `(2026)`. While this may be an attempt to anticipate the publication year, it is non-standard.
*   **Fix:** Use the year the preprint first appeared on the arXiv. For example, ref [5] `arXiv:2509.13654` should be `(2025)`. This is correct. Ref [44] `arXiv:2603.13924` should be `(2026)`. This is a future date. It should be the year of submission. Please standardize all dates to the actual preprint appearance year.

---
### Summary recommendation

**MAJOR REVISIONS**

This manuscript contains several valuable contributions, most notably the perturbation-transparency theorem for scalar matter in ECH and the structural tension argument against simultaneously generating dark energy and a matter-bounce `f_NL` signature. These results are well-argued and of interest to the cosmology community. However, the paper's central claim of a "no-go" for ECH-driven dark energy is substantially weakened by its reliance on a non-derived phenomenological ansatz. Furthermore, the work is not self-contained, depending critically on companion papers that are not yet available for review.

To meet the standards of Physical Review D, the authors must: (1) Reframe the manuscript to more accurately reflect the conditional, ansatz-dependent nature of the dark-energy closure claims. (2) Make the paper self-contained by either incorporating the essential methods and results from the "in preparation" works into appendices or by waiting to publish until those works are publicly archived and citable. After these essential and major revisions are addressed, the manuscript could represent a solid contribution to the theoretical cosmology literature.