# P1A R38conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.70.pdf` md5=4e24501f pages=28
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 108.0s

---

**Referee Report for PRD Manuscript**

**Manuscript ID:** [Assigned by journal]
**Title:** Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter
**Author:** Houston Golden

This paper presents a systematic assessment of four potential channels within Einstein-Cartan-Holst (ECH) theory as sources for late-time dark energy. The author concludes that, under a set of stated assumptions and scaling ansätze, these four minimal routes are closed. The paper's central positive result is a "perturbation-transparency" theorem, demonstrating that for canonical scalar matter, the Holst sector decouples from scalar and tensor perturbations, leaving them identical to those in standard General Relativity.

The paper contains a rigorous and valuable theoretical result in the perturbation-transparency theorem. The systematic audit of the four dark-energy routes is also a useful contribution, clarifying the assumptions required to constrain them. However, the manuscript in its current form suffers from several significant issues that preclude its publication in Physical Review D without major revisions. These include a lack of self-containment due to heavy reliance on companion papers, improper comparison of statistical significances in the abstract, and a structure that could be significantly condensed to better highlight the core contributions.

Below is a detailed list of required revisions.

---
### ESSENTIAL Revisions

**P1A-E1**
*   **Section/Page:** Abstract, page 1
*   **Problem:** The abstract juxtaposes statistical significances derived from different null hypotheses and procedures without the necessary caveats, which is highly misleading. It states: "...WMAP+Planck 1σ band βobs = 0.342° ± 0.094° (~3.6σ from β = 0, first reported by Minami & Komatsu [3] and refined by Eskilt & Komatsu [4]), and is comparable to the independent ACT DR6 follow-up β = 0.215° ± 0.074° at ~2.9σ (Diego-Palazuelos & Komatsu [5]; these significances, and the SPHEREx forecast 2.6-5σ quoted above, arise from different null procedures and are not directly comparable in a single tension table);". While a caveat is present at the end of the sentence, this is insufficient. Comparing a ~3.6σ preference for non-zero β (against the null β=0) with a ~2.9σ preference from a different experiment is not a direct comparison of consistency. The SPHEREx forecast significance (2.6-5σ) is a forecast against a different null (fNL=0) and cannot be placed in the same context. This violates the principle of comparing like with like.
*   **Fix:** The abstract must be rewritten to separate these claims clearly. Each significance value must be presented with its specific null hypothesis. Direct comparisons must be removed. For example, state the WMAP+Planck result and its significance against β=0. Separately, state the ACT result and its significance against β=0. Then, state their mutual consistency in terms of their 1σ error bars, as is correctly done for the R4 analysis in Sec. IV D (|0.342 – 0.215|/√0.094² + 0.074² ≈ 1.06). The SPHEREx forecast for fNL should be presented in a separate sentence, as it pertains to a different physical observable.

---
### MAJOR Revisions

**P1A-M1**
*   **Section/Page:** Throughout, but especially Table I (p. 4), Sec. VII (p. 15), Sec. XIII (p. 22)
*   **Problem:** The paper is not self-contained, in violation of standard journal requirements. It relies critically on results, forecasts, and MCMC analyses from companion papers [2, 6, 23, 46] that are cited as "in preparation" or "posted concurrently". Key quantitative claims, such as the SPHEREx fNL forecast (the basis for one of the two "surviving" tests), the cosmological parameter values in Table I, and the PTA reanalysis, are not derived or detailed in this manuscript. A reader cannot assess the validity of these claims without accessing and vetting several other full-length papers.
*   **Fix:** The paper must be made self-contained. For each result imported from a companion paper, the author must include a concise summary of the methodology, datasets, and key equations used to derive it. For example, for the fNL forecast, a summary of the Fisher matrix construction, tracer populations, and systematic error budget is required. For the MCMC results, the datasets, model, and priors must be specified. This material can be placed in an appendix if necessary, but it must be present within this manuscript.

**P1A-M2**
*   **Section/Page:** Section IX, "Structural Constraints on Dark-Energy Routes in Minimal ECH" (pp. 16-19)
*   **Problem:** The paper's length (28 pages) is not justified by the core new contributions. The central results are the closure of the four routes (Sec. IV) and the perturbation-transparency theorem (Sec. X). Section IX, which presents a catalog of 14 "barriers," feels padded and dilutes the focus. Many of these barriers are either qualitative (e.g., B6: Attractor-Sensitivity Dilemma, B13: Gravitational Democracy), standard results in the field, or consequences of the more fundamental arguments presented elsewhere in the paper (e.g., B8 is a consequence of B14).
*   **Fix:** Section IX should be heavily condensed. The novel, quantitative constraints should be retained and perhaps integrated into the discussion in Section IV. The more qualitative or well-known constraints should be summarized in a single paragraph or a compact table, or moved to an appendix. This would shorten the paper and sharpen its focus on the primary claims. A target length of 15-18 pages for the main body seems more appropriate.

**P1A-M3**
*   **Section/Page:** Abstract (p. 1) and Section XIV D (p. 23)
*   **Problem:** The abstract presents the "structural tension" between the dark-energy mechanism (requiring Ntot ≈ 92) and the matter-bounce fNL signature as a key finding. The argument is that Ntot ≈ 92 e-folds of inflation would erase the pre-inflationary fNL signal. While the physical reasoning is sound, this is a well-understood feature of bouncing cosmologies with a subsequent inflationary phase. It is a consistency check or a constraint, but presenting it as a primary result of this specific ECH analysis is an overstatement. The core result is the closure of the ECH dark-energy routes themselves; this tension is a consequence for any model that tries to unify this specific bounce with dark energy via inflationary dilution.
*   **Fix:** Re-scope this finding in the abstract and main text. Frame it clearly as a general constraint on any model attempting to link a pre-inflationary bounce signal (like the matter-bounce fNL) to a dark energy component diluted by a long period of inflation, rather than a specific structural failure of ECH itself. The primary finding should remain the closure of the four ECH routes.

---
### MINOR Revisions

**P1A-m1**
*   **Section/Page:** Section IV D, page 13, footnote 4
*   **Problem:** The footnote explaining the normalization of the ALP field φ vs. the dimensionless angle θ is helpful but convoluted. It addresses a potential dimensional ambiguity but could be clearer. The distinction between the paper's `a/M` and the canonical `g_aγ` is also buried in footnote 5 on page 14.
*   **Fix:** Consolidate and clarify this discussion. In the main text of Sec. IV D, define the ALP-photon coupling Lagrangian using a single, standard convention (e.g., `-(g_aγ/4) φ F F_tilde`). Then, explicitly state the mapping between `g_aγ` and the paper's phenomenological parameter `a/M`, including all factors of `f_a`, etc. This avoids confusion and makes the connection to the broader ALP literature transparent.

**P1A-m2**
*   **Section/Page:** Section X, page 19
*   **Problem:** The proof of the perturbation-transparency result is elegant and correct. However, its presentation is extremely dense. The five steps are listed in less than half a column. Given that this is the main positive theoretical result of the paper, it deserves a more pedagogical treatment.
*   **Fix:** Expand the proof in Section X B. Write out the key equations for each step (e.g., the explicit form of the spin density for a scalar field being zero, the Cartan equation `T ~ S`, the definition of the Holst term). This would add perhaps half a page but would significantly increase the clarity and impact of this important result.

**P1A-m3**
*   **Section/Page:** Data and Code Availability, page 25
*   **Problem:** The paper states, "a Zenodo-archived release will pin all artifacts to the submitted-version snapshot." For a paper to be considered reproducible upon publication, this DOI should be provided with the final version of the manuscript.
*   **Fix:** The author should generate the Zenodo DOI and add it to this section before publication. A statement like "The final data and code release is archived at [DOI]" is required.

**P1A-m4**
*   **Section/Page:** Figure 5, page 18
*   **Problem:** The bottom panel, "Dark Energy Fine-Tuning Comparison," is illustrative but potentially misleading. The "Fine-Tuning Score" for "Spin-Torsion (this work)" is given as 10⁵. As the text in Sec. XII A clarifies, this is a "reparameterization of the cosmological-constant problem as sensitivity to N_tot, not a resolution." The visual representation, however, might suggest to a casual reader that the model has "solved" the fine-tuning problem down to 1 part in 10⁵.
*   **Fix:** Add a prominent disclaimer to the figure caption itself, stating explicitly that the 10⁵ value represents a reparameterization of the fine-tuning into the parameter N_tot and is not a solution to the cosmological constant problem.

---
### NITs (Cosmetic)

**P1A-N1**
*   **Section/Page:** Abstract, page 1
*   **Problem:** The phrase "The two predictions discussed below as 'surviving' are accordingly not predictions of ECH itself..." is slightly awkward.
*   **Fix:** Suggest rephrasing to: "The two 'surviving' predictions discussed below are therefore not specific to ECH, but are rather general tests of the broader matter-bounce and spectator-ALP scenarios..."

**P1A-N2**
*   **Section/Page:** Section IV, page 11, paragraph 1
*   **Problem:** The sentence "The qualitative closure statement that Route 2 lies below the observed birefringence amplitude by ≥ 30 orders of magnitude survives any reasonable dimensional reconciliation" is verbose.
*   **Fix:** Suggest simplifying to: "The conclusion that the Route 2 amplitude is suppressed by dozens of orders of magnitude is robust to the choice of dimensional analysis."

---
## Summary recommendation

**MAJOR REVISIONS**

This manuscript presents a valuable and rigorous perturbation-transparency theorem for ECH gravity with scalar matter and performs a useful, systematic closure of four minimal dark-energy routes within that framework. These are worthy contributions. However, the paper cannot be accepted in its current state. The heavy reliance on companion papers for key results makes the work unverifiable and not self-contained. Furthermore, the abstract contains misleading comparisons of statistical significances that must be corrected. If the author can address these major issues by integrating the necessary supporting material from the companion papers and revising the presentation to be statistically sound and more focused, the manuscript would likely be suitable for publication in Physical Review D.