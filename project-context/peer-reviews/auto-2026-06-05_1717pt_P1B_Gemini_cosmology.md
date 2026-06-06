# P1B auto-2026-06-05_1717pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 127.8s

---

## Referee Report for "Technical Verification Companion to the ECH Spin-Torsion Program..."

This manuscript presents technical verification for three separate analyses related to the Einstein-Cartan-Holst (ECH) cosmology program detailed in a companion paper. The analyses are: (1) a `ΛCDM+ΔNeff` MCMC analysis using stock CAMB, (2) a validation of a `NaMaster` pseudo-Cℓ pipeline for cosmic birefringence, and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model.

The paper is commendable for its focus on reproducibility, with a public code repository and clear statements on the scope and limitations of each analysis. The authors are careful to distinguish between pipeline validation and sky detection, and between proxy models and full theory tests. However, the manuscript suffers from a significant structural issue that obscures its most interesting result, contains a numerical error that must be corrected, and has several points that require clarification.

### ESSENTIAL Revisions

**P1B-E1: Incorrect calculation of NaMaster pipeline bias dependence (Page 6)**
*   **Section:** IV, Page 6
*   **Problem:** The text describes the amplitude dependence of the pipeline bias. It states: "...the 0.342° injection actually gives 0.040°, a relative ~12% amplitude-dependent component)." The bias for the `β=0.27°` injection is `0.032°`, and for the `β=0.342°` injection is `0.040°`. The relative *increase* in the bias is `(0.040 - 0.032) / 0.032 = 0.25`, or 25%. The claim of `~12%` is arithmetically incorrect by more than a factor of two.
*   **Required Fix:** The author must correct this calculation and the corresponding text. The statement should be changed to reflect the 25% relative increase in bias, and the author should comment on whether this level of amplitude dependence is acceptable for the pipeline's intended use.

**P1B-E2: Paper structure buries the most significant MCMC result (Throughout)**
*   **Section:** Abstract, Title, Sections II, III, V
*   **Problem:** The paper is framed around the `ΛCDM+ΔNeff` MCMC analysis, which returns a null result (`ΔNeff` is consistent with zero). However, a separate `w0-wa` analysis, whose results are presented in Table II and discussed on pages 3 and 6, finds a `+4.3σ` departure from `w0=-1` and a `-3.6σ` departure from `wa=0`, indicating a strong preference for phantom-crossing dark energy. This is a far more significant cosmological result than the `ΔNeff` null detection. By titling the paper with `ΔNeff` and dedicating the primary MCMC section to it, the authors have buried their most impactful finding.
*   **Required Fix:** The paper must be restructured to give the `w0-wa` analysis the prominence it deserves. This includes:
    1.  Revising the title and abstract to feature the `w0-wa` result.
    2.  Creating a dedicated section for the `w0-wa` analysis, separate from the `ΔNeff` proxy test.
    3.  Clearly distinguishing the datasets and motivations for the two separate MCMC runs. The current presentation conflates them, making the paper difficult to follow.

### MAJOR Revisions

**P1B-M1: Confusing sample count in Figure 1 caption (Page 5)**
*   **Section:** IV, Figure 1
*   **Problem:** The caption for the MCMC corner plot states it shows "119,617 post-burnin samples". However, footnote 1 (on page 3) and the associated text calculate the post-burnin sample count for this chain to be `123,129`. The caption attempts to explain this by mentioning "getdist-thinned", and a footnote on page 3 adds that the figure reflects "additional getdist effective-sample weight-based thinning". This is confusing and requires the reader to connect multiple footnotes across different pages to understand the figure.
*   **Required Fix:** The caption of Figure 1 must be self-contained and clear. It should state the raw post-burnin sample count (`123,129`) and then explain that the plotted samples (`119,617`) are a thinned subset for visualization purposes, specifying the thinning method (e.g., "thinned by effective sample size weighting in getdist").

**P1B-M2: Redundant and poorly placed "Cosmological Fits" section (Page 6)**
*   **Section:** V
*   **Problem:** Section V, "Cosmological Fits and Model Comparison," largely repeats results and discussions already presented in Section III and its associated tables (Table I and Table II). It lists the dataset combinations, which should have been done in Section III, and then re-states the `ΔNeff` and `w0-wa` posteriors. The section adds very little new information and disrupts the paper's flow.
*   **Required Fix:** Section V should be eliminated. Its essential content, such as the list of dataset configurations, should be merged into the relevant MCMC section(s) (per recommendation P1B-E2). The deferral of model-comparison statistics is important but can be stated once in the main MCMC section.

### MINOR Revisions

**P1B-m1: Overly dense sentence in Abstract (Page 1)**
*   **Section:** Abstract
*   **Problem:** The sentence describing the scope of the `NaMaster` validation is difficult to parse: "Scope of the validation: the test confirms the algebraic pseudo-Ce E→ B deconvolution under MASTER mode coupling, NOT the physical separation of the cosmic-rotation angle β from the instrumental-miscalibration angle α which strictly requires unrotated galactic foregrounds..."
*   **Required Fix:** Rephrase this for clarity. For example: "Scope of the validation: The test validates the algebraic deconvolution of E-B mixing in the pseudo-Cℓ formalism. It does not, however, address the physical challenge of separating the cosmic rotation angle (β) from instrumental effects (α), a degeneracy broken in other work by using galactic foregrounds."

**P1B-m2: Ambiguity in ALP fine-tuning reference point (Page 7)**
*   **Section:** VI
*   **Problem:** The text and footnotes 4 and 5 argue for a `~25x` fine-tuning of the initial misalignment angle `θi` to keep the ALP in the "spectator" regime. This is based on comparing the required `θi ~ 0.1` to a "natural prior midpoint θi ~ 0.5". However, the MCMC analysis (Appendix C) uses a uniform prior `θi ∈ [0.5, 2]`, whose midpoint is 1.25. The choice of `0.5` as the reference "midpoint" is not justified and appears inconsistent with the actual prior used.
*   **Required Fix:** The author must justify the use of `0.5` as the reference point for the tuning calculation or, preferably, re-calculate the tuning factor relative to the actual prior midpoint of 1.25.

**P1B-m3: Dataset attribution in footnote (Page 1)**
*   **Section:** Abstract, footnote 'a'
*   **Problem:** The final sentence of footnote 'a' states, "The repository README is the authoritative source for the dataset attribution in the executed pipeline." While commendable for reproducibility, the manuscript itself, as the archival record, should be the authoritative source.
*   **Required Fix:** Remove this sentence. The paper should state unambiguously which dataset combination corresponds to the headline `β = 0.342° ± 0.094°` result from Eskilt & Komatsu [2] that is used throughout the text.

### NITs (Cosmetic)

**P1B-N1: Awkward phrasing in Table I caption (Page 3)**
*   **Problem:** "Worst row is ns..."
*   **Fix:** Suggest "The parameter with the worst convergence is ns..."

**P1B-N2: Awkward phrasing in Table II (Page 4)**
*   **Problem:** The entry `(marg.-tail, +4.3σ)a` is slightly unclear.
*   **Fix:** Suggest "Departure from ΛCDM (+4.3σ, marginalized)" or similar.

**P1B-N3: Sub-section title is a note, not a title (Page 6)**
*   **Problem:** The sub-section title "a. Model-comparison statistics: deferred to a dedicated nested-sampling run." is a comment on the analysis, not a descriptive title.
*   **Fix:** Change the title to something like "Model Comparison" and move the explanatory text into the paragraph body.

## Summary recommendation
**MAJOR REVISIONS**

This manuscript provides a valuable and transparent account of verification work for a larger research program. The commitment to reproducibility is a significant strength. However, the paper in its current form cannot be accepted. The structural decision to bury the highly significant `w0-wa` phantom-crossing result in favor of a null `ΔNeff` result does a disservice to the work and to the reader. Furthermore, the arithmetical error in the NaMaster bias analysis is an essential correction. Once the paper is restructured to properly highlight its most important findings and the specified corrections are made, it will likely be suitable for publication in Physical Review D.