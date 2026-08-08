# P1A R52 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.78.pdf` md5=198cb994 pages=29
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (10900 chars)
**Wall time**: 143.9s

---

**Referee Report for "Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"**

**Manuscript ID:** [Assigned by journal]
**Author:** Houston Golden
**Journal:** Physical Review D

## General Comments

This manuscript presents a broad theoretical and phenomenological assessment of minimal Einstein-Cartan-Holst (ECH) theory as a source for late-time dark energy. The author attempts to close four enumerated channels for this mechanism and presents two key results: a "perturbation-transparency" theorem for canonical scalar matter and a "structural tension" between the requirements for the dark energy mechanism and the preservation of a matter-bounce signature in the non-Gaussianity parameter `f_NL`.

The paper contains several valuable contributions. The perturbation-transparency result (Section X), which demonstrates that the Holst sector decouples from standard scalar and tensor perturbations for canonical scalar fields, is a clear and significant finding. It correctly identifies that any new ECH physics in this sector must appear in non-perturbative channels like cosmic birefringence or primordial gravitational waves. The structural tension argument (Section XIV D), highlighting the incompatibility between the large number of e-folds required for the dark-energy dilution mechanism and the survival of a primordial `f_NL` signal, is also a powerful and well-reasoned consistency check.

However, the manuscript suffers from several critical flaws that preclude its publication in the present form. The most severe issue is that the paper is not self-contained, relying on four concurrently submitted companion papers for the methods and results of every observational test it discusses. This makes a rigorous, independent evaluation of its claims impossible. Furthermore, the central "closure" argument for the dark-energy routes rests on phenomenological ansätze that are not derived from first principles, a weakness that must be more prominently reflected in the paper's main claims and conclusions. The manuscript is also overly long and its structure is difficult to follow, obscuring the most important results.

Substantial revisions are required to address these points before the manuscript can be reconsidered for publication.

## Detailed Findings

### ESSENTIAL

**P1A-E1: Lack of Self-Containment (Throughout)**
*   **Problem:** The manuscript is fundamentally not a standalone scientific article. It outsources the entirety of its observational evidence, MCMC analysis, and forecasting to four companion papers ([2], [6], [23], [46]), which are cited as "in preparation" or "posted concurrently". This includes the `f_NL` forecast, the MCMC analysis for cosmological parameters and cosmic birefringence, the galaxy spin null result, and the PTA reanalysis. A referee cannot be expected to locate and review four additional manuscripts to validate the claims of this one.
*   **Fix:** The manuscript must be revised to be self-contained. For each external result that is load-bearing for the argument, the author must include a summary of the methodology, the key results (in tables or figures), and the systematic uncertainties considered. This material could be placed in appendices if necessary, but it must be present within this manuscript. Citing "in preparation" works is unacceptable. If the papers are posted on the arXiv, the author must still provide sufficient summary here for this paper's logic to be followed and evaluated on its own merits.

**P1A-E2: Overstated Conclusions Based on Und-derived Ansätze (Abstract, Sec. IV, Sec. XV)**
*   **Problem:** The core claim of a "channel-level closure" for dark energy routes R2-R4 depends critically on what the author honestly calls a "phenomenological on-shell scaling ansatz" (p. 1, Appendix B) and a prefactor derived from "dimensional-analysis aesthetic" (p. 8). While the author's transparency is commendable, the conclusions and abstract framing are too strong for claims based on assumptions rather than derivations. The term "closure" implies a robust, model-independent result, which is not what has been achieved for the dark-energy part of the analysis.
*   **Fix:** The language in the abstract, introduction, and conclusions must be softened. The author should reframe this part of the work as an "ansatz-dependent constraint" or an "exploration of phenomenological scenarios" rather than a "closure". The abstract must state upfront that the dark-energy constraints are conditional on these specific, un-derived scaling relations.

### MAJOR

**P1A-M1: Manuscript Structure and Length (Throughout)**
*   **Problem:** At 29 pages, the paper is excessively long for its core contributions. The narrative is difficult to follow, particularly the relationship between the "Four-Route No-Go" of Section IV and the catalog of "14 barriers" in Section IX. The latter section reads as a disconnected list of arguments that are not clearly mapped onto the four primary routes being closed. This dilutes the impact of the paper's strongest results.
*   **Fix:** The manuscript requires significant restructuring. The author should streamline the main text to focus on the two most robust results: the perturbation-transparency theorem (Sec. X) and the structural tension (Sec. XIV D). The arguments from Section IX should be either directly integrated into the discussion of the four routes in Section IV to show how each barrier contributes to a specific closure, or be moved to an appendix. The recommended length for the main body of the paper is 15-18 pages.

**P1A-M2: Ambiguity of the `α/M` Parameter (Sec. IV D, p. 14)**
*   **Problem:** The parameter `α/M` is central to the analysis of Routes 2-4, but its definition and relationship to standard parameters in the literature are confusing. It is motivated by a one-loop estimate in Eq. (7), but then used as a phenomenological parameter fitted to data in the crucial Route 4 analysis. Footnote 5 on page 14 attempts to reconcile the paper's `α/M` with the canonical ALP-photon coupling `g_aγγ`, but the explanation is convoluted and reveals a non-trivial factor of ~10 difference that depends on assumptions about the decay constant `f_a` and coupling `c_γ`.
*   **Fix:** The manuscript needs a single, clear, and self-contained section (or appendix) that defines `α/M`, derives the one-loop estimate, and explicitly shows its mapping to the canonical `g_aγγ` under stated assumptions. The current scattered presentation across the main text and footnotes is inadequate.

### MINOR

**P1A-m1: Unclear Figure 3 Parameters (p. 8)**
*   **Problem:** The caption for Figure 3 presents an "illustrative parameter-set" for the ECH model (`H_0 = 69.2 km/s/Mpc`, etc.) in comparison to a Planck-VI ACDM reference. It is not stated how this illustrative set was chosen.
*   **Fix:** The caption should clarify the origin of these parameter values. Are they a best-fit from some (un-cited) analysis, or simply a representative point chosen for plotting?

**P1A-m2: Incomparable Significance Values (Abstract, p. 1)**
*   **Problem:** The abstract quotes several significance values: `~3.6σ` (WMAP+Planck), `~2.9σ` (ACT), and `2.6-5σ` (SPHEREx forecast). While the text correctly notes that they "are not directly comparable", this juxtaposition in the abstract can still be misleading to a casual reader.
*   **Fix:** The abstract should be rephrased to avoid placing these numbers side-by-side without immediate context. For example, group the existing measurements together and then separately introduce the forecast, emphasizing the different null hypotheses and methodologies.

**P1A-m3: Future Date on Manuscript (p. 1)**
*   **Problem:** The date on the title page is "June 18, 2026", which is in the future.
*   **Fix:** This should be corrected to the date of submission.

### NIT

**P1A-N1: Redundant Phrasing (Abstract, p. 1)**
*   **Problem:** The abstract contains the phrase: "...target distinct physical mechanisms... and are described as distinct mechanism-class constraints...".
*   **Fix:** Rephrase to avoid repetition, for example: "...target distinct physical mechanisms, which are classified as separate mechanism-class constraints...".

## Summary Recommendation

**MAJOR REVISIONS**

The manuscript in its current form does not meet the standards for publication in Physical Review D. While it contains the seeds of two important results (the perturbation-transparency theorem and the `f_NL` structural tension), its primary claim of closing dark-energy channels is based on underived assumptions, and the entire work is critically dependent on external companion papers, making it impossible to verify.

For the paper to be reconsidered, the author must perform a major revision to make the manuscript self-contained by incorporating the necessary methods and results from the companion papers. The claims must be carefully re-scoped to reflect their dependence on phenomenological ansätze, and the overall structure must be significantly streamlined for clarity and impact. If these substantial issues are addressed, the revised manuscript could represent a valuable contribution to the literature on bounce cosmology and modified gravity.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated referee report, incorporating the findings from the second, more rigorous review.

================================================================
**Referee Report for "Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"**

**Manuscript ID:** [Assigned by journal]
**Author:** Houston Golden
**Journal:** Physical Review D

## General Comments

This manuscript presents a broad theoretical and phenomenological assessment of minimal Einstein-Cartan-Holst (ECH) theory as a source for late-time dark energy. The author attempts to close four enumerated channels for this mechanism and presents two key results: a "perturbation-transparency" theorem for canonical scalar matter and a "structural tension" between the requirements for the dark energy mechanism and the preservation of a matter-bounce signature in the non-Gaussianity parameter `f_NL`.

The paper contains several valuable contributions. The perturbation-transparency result (Section X), which demonstrates that the Holst sector decouples from standard scalar and tensor perturbations for canonical scalar fields, is a clear and significant finding. It correctly identifies that any new ECH physics in this sector must appear in non-perturbative channels like cosmic birefringence or primordial gravitational waves. The structural tension argument (Section XIV D), highlighting the incompatibility between the large number of e-folds required for the dark-energy dilution mechanism and the survival of a primordial `f_NL` signal, is also a powerful and well-reasoned consistency check.

However, the manuscript suffers from several critical flaws that preclude its publication in the present form. The most severe issue is that the paper is not self-contained, relying on four concurrently submitted companion papers for the methods and results of every observational test it discusses. This makes a rigorous, independent evaluation of its claims impossible. Furthermore, the central "closure" argument for the dark-energy routes rests on phenomenological ansätze that are not derived from first principles, a weakness that must be more prominently reflected in the paper's main claims and conclusions. A detailed check also reveals a potential dimensional inconsistency in a key equation used to constrain one of the dark-energy routes. The manuscript is also overly long and its structure is difficult to follow, obscuring the most important results.

Substantial revisions are required to address these points before the manuscript can be reconsidered for publication.

## Detailed Findings

### ESSENTIAL

**P1A-E1: Lack of Self-Containment (Throughout)**
*   **Problem:** The manuscript is fundamentally not a standalone scientific article. It outsources the entirety of its observational evidence, MCMC analysis, and forecasting to four companion papers ([2], [6], [23], [46]), which are cited as "in preparation" or "posted concurrently". This includes the `f_NL` forecast, the MCMC analysis for cosmological parameters and cosmic birefringence, the galaxy spin null result, and the PTA reanalysis. A referee cannot be expected to locate and review four additional manuscripts to validate the claims of this one.
*   **Fix:** The manuscript must be revised to be self-contained. For each external result that is load-bearing for the argument, the author must include a summary of the methodology, the key results (in tables or figures), and the systematic uncertainties considered. This material could be placed in appendices if necessary, but it must be present within this manuscript. Citing "in preparation" works is unacceptable. If the papers are posted on the arXiv, the author must still provide sufficient summary here for this paper's logic to be followed and evaluated on its own merits.

**P1A-E2: Overstated Conclusions Based on Und-derived Ansätze (Abstract, Sec. IV, Sec. XV)**
*   **Problem:** The core claim of a "channel-level closure" for dark energy routes R2-R4 depends critically on what the author honestly calls a "phenomenological on-shell scaling ansatz" (p. 1, Appendix B) and a prefactor derived from "dimensional-analysis aesthetic" (p. 8). While the author's transparency is commendable, the conclusions and abstract framing are too strong for claims based on assumptions rather than derivations. The term "closure" implies a robust, model-independent result, which is not what has been achieved for the dark-energy part of the analysis.
*   **Fix:** The language in the abstract, introduction, and conclusions must be softened. The author should reframe this part of the work as an "ansatz-dependent constraint" or an "exploration of phenomenological scenarios" rather than a "closure". The abstract must state upfront that the dark-energy constraints are conditional on these specific, un-derived scaling relations.

### MAJOR

**P1A-M1: Manuscript Structure and Length (Throughout)**
*   **Problem:** At 29 pages, the paper is excessively long for its core contributions. The narrative is difficult to follow, particularly the relationship between the "Four-Route No-Go" of Section IV and the catalog of "14 barriers" in Section IX. The latter section reads as a disconnected list of arguments that are not clearly mapped onto the four primary routes being closed. This dilutes the impact of the paper's strongest results.
*   **Fix:** The manuscript requires significant restructuring. The author should streamline the main text to focus on the two most robust results: the perturbation-transparency theorem (Sec. X) and the structural tension (Sec. XIV D). The arguments from Section IX should be either directly integrated into the discussion of the four routes in Section IV to show how each barrier contributes to a specific closure, or be moved to an appendix. The recommended length for the main body of the paper is 15-18 pages.

**P1A-M2: Ambiguity of the `α/M` Parameter (Sec. IV D, p. 14)**
*   **Problem:** The parameter `α/M` is central to the analysis of Routes 2-4, but its definition and relationship to standard parameters in the literature are confusing. It is motivated by a one-loop estimate in Eq. (7), but then used as a phenomenological parameter fitted to data in the crucial Route 4 analysis. Footnote 5 on page 14 attempts to reconcile the paper's `α/M` with the canonical ALP-photon coupling `g_aγγ`, but the explanation is convoluted and reveals a non-trivial factor of ~10 difference that depends on assumptions about the decay constant `f_a` and coupling `c_γ`.
*   **Fix:** The manuscript needs a single, clear, and self-contained section (or appendix) that defines `α/M`, derives the one-loop estimate, and explicitly shows its mapping to the canonical `g_aγγ` under stated assumptions. The current scattered presentation across the main text and footnotes is inadequate.

**P1A-M3: Dimensional Inconsistency in Route 2 Operator (Eq. 14, p. 12)**
*   **Problem:** The phenomenological operator adopted to constrain Route 2 (one-loop graviton corrections) is given in Eq. (14) as a Lagrangian term `L ~ (1/M_Pl) ∫ d^4x ... ∂_μ D_NY(x) J^5μ(x)`. A Lagrangian term should be dimensionless, but the integrand does not appear to have the correct mass dimension of +4. Assuming standard dimensions for the axial current `[J^5] = +3` and derivative `[∂] = +1`, the operator has dimension `[1/M_Pl] * [∂] * [D_NY] * [J^5]`. For this to result in a Lagrangian density of dimension +4, the pseudoscalar `D_NY` would need dimension `[D_NY] = +1`. However, the overall expression is still dimensionally inconsistent. This undermines the quantitative basis for the `~10^-60` suppression factor calculated in Eq. (15).
*   **Fix:** The author must clarify the dimensional analysis of Eq. (14). This requires either correcting the form of the operator or providing a detailed derivation from the cited literature ([15], [20]) that justifies its structure and dimensional consistency. Without this, the closure of Route 2 is not quantitatively supported.

### MINOR

**P1A-m1: Unclear Figure 3 Parameters (p. 8)**
*   **Problem:** The caption for Figure 3 presents an "illustrative parameter-set" for the ECH model (`H_0 = 69.2 km/s/Mpc`, etc.) in comparison to a Planck-VI ACDM reference. It is not stated how this illustrative set was chosen.
*   **Fix:** The caption should clarify the origin of these parameter values. Are they a best-fit from some (un-cited) analysis, or simply a representative point chosen for plotting?

**P1A-m2: Incomparable Significance Values (Abstract, p. 1)**
*   **Problem:** The abstract quotes several significance values: `~3.6σ` (WMAP+Planck), `~2.9σ` (ACT), and `2.6-5σ` (SPHEREx forecast). While the text correctly notes that they "are not directly comparable", this juxtaposition in the abstract can still be misleading to a casual reader.
*   **Fix:** The abstract should be rephrased to avoid placing these numbers side-by-side without immediate context. For example, group the existing measurements together and then separately introduce the forecast, emphasizing the different null hypotheses and methodologies.

**P1A-m3: Future Date on Manuscript (p. 1)**
*   **Problem:** The date on the title page is "June 18, 2026", which is in the future.
*   **Fix:** This should be corrected to the date of submission.

### NIT

**P1A-N1: Redundant Phrasing (Abstract, p. 1)**
*   **Problem:** The abstract contains the phrase: "...target distinct physical mechanisms... and are described as distinct mechanism-class constraints...".
*   **Fix:** Rephrase to avoid repetition, for example: "...target distinct physical mechanisms, which are classified as separate mechanism-class constraints...".

## Summary Recommendation

**MAJOR REVISIONS**

The manuscript in its current form does not meet the standards for publication in Physical Review D. While it contains the seeds of two important results (the perturbation-transparency theorem and the `f_NL` structural tension), its primary claim of closing dark-energy channels is based on underived assumptions and a potentially dimensionally inconsistent operator. Furthermore, the entire work is critically dependent on external companion papers, making it impossible to verify.

For the paper to be reconsidered, the author must perform a major revision to make the manuscript self-contained by incorporating the necessary methods and results from the companion papers. The claims must be carefully re-scoped to reflect their dependence on phenomenological ansätze, and the dimensional analysis of key equations must be corrected and clarified. Finally, the overall structure must be significantly streamlined for clarity and impact. If these substantial issues are addressed, the revised manuscript could represent a valuable contribution to the literature on bounce cosmology and modified gravity.