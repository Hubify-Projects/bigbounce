# P1B R53 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/private/tmp/R53_P1B/paper1b_mcmc_companion.pdf` md5=9a4aa5f5 pages=21
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 146.3s

---

## Referee Report for Manuscript [P1B]

**Title:** Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model

### Summary of the Manuscript

This manuscript presents three distinct technical analyses intended as verification material for a broader research program on Einstein-Cartan-Holst (ECH) cosmology. The analyses are:
1.  A Markov Chain Monte Carlo (MCMC) analysis of the ΛCDM model extended with a variable effective number of relativistic species (ΔNeff), using stock CAMB. This is framed as a null-consistency test and finds no evidence for ΔNeff ≠ 0, nor a resolution to the Hubble tension.
2.  A Monte Carlo validation of a NaMaster-based pseudo-C_l pipeline for measuring cosmic birefringence (the E-B power spectrum). The authors quantify the pipeline's recovery bias on synthetic, foreground-free skies.
3.  A consistency check of the observed cosmic birefringence signal with a spectator axion-like particle (ALP) model. The analysis shows that the signal can be accommodated within the model, but this requires fine-tuning of the initial misalignment angle to maintain spectator status and/or a non-minimal photon-axion coupling.

The paper is positioned as a companion paper providing technical validation, not as a discovery paper. The authors are commendably careful in scoping their claims and provide extensive detail on their methodology and data provenance.

### General Assessment

The work presented is methodologically sound, and the analyses appear to be performed with a high degree of rigor and transparency. The authors' efforts in providing detailed reproducibility materials are exemplary. The distinction between pipeline validation, consistency checks, and new physical constraints is, for the most part, clearly articulated and maintained.

However, the manuscript's structure, combining three disparate topics, makes for a challenging read. Its density, with critical details often relegated to lengthy footnotes, hinders clarity. While the technical work is of high quality, the presentation requires significant revision to meet the publication standards of Physical Review D. The primary concerns relate to the presentation of certain statistical results, the overall structure and readability, and ensuring that the crucial caveats receive the same prominence as the headline numbers.

### List of Findings

#### ESSENTIAL

*   **P1B-E1: Abstract-Body Consistency and Prominence of Caveats**
    *   **Location:** Abstract (Page 1) and Section VI (Page 12).
    *   **Problem:** The abstract correctly mentions the fine-tuning required for the spectator-ALP model. However, the body of the paper (Sec. VI, fn. 6, and the main text) reveals the severity of this tuning (~25x in the initial angle `θi`) and the required non-minimal coupling (`Cay` ≈ 8-10, exceeding standard benchmarks). While mentioned, the abstract could more forcefully state that accommodating the signal within a *spectator* framework is unnatural from a model-building/prior-volume perspective. The current phrasing, "the spectator-safe... subset is tuned," is technically correct but might understate the case.
    *   **Required Fix:** Revise the abstract to state more explicitly that accommodating the observed birefringence with a *spectator* ALP is disfavored due to significant fine-tuning of initial conditions and requires a non-minimal photon coupling. For example: "...the spectator-safe (Ωa < 0.01) subset requires significant fine-tuning of the initial misalignment angle (a ~25-fold reduction from the natural scale) and a non-minimal photon coupling (Cay > 8), indicating the model accommodates the signal but does not naturally predict it." This ensures the main takeaway is not just "consistency" but "consistency at a price."

#### MAJOR

*   **P1B-M1: Presentation of `w0wa` Tail-Distance Statistics**
    *   **Location:** Section V.C (Page 12), Table II (Page 6).
    *   **Problem:** Table II and the associated text report posterior-tail distances for the `w0wa` parameters in units of "σ" (e.g., `+4.3σ` for `w0`). As the authors correctly note in footnote `a` of Table II, this is an *extrapolation* because the ΛCDM point is unsampled. Using the "σ" notation is highly misleading, as it implies a Gaussian tension or a well-defined frequentist p-value, neither of which is appropriate for an extrapolated distance from a non-Gaussian MCMC posterior tail. This practice risks misinterpretation by readers, despite the caveats.
    *   **Required Fix:** Remove the "σ" notation for these extrapolated distances. Instead, state the distance in units of the marginalized 1D posterior width, `σ_w0`, and explicitly state it is an extrapolation. For example, change "(marg.-tail, +4.3σ)" to "displaced by +4.3 times the marginal posterior width (extrapolated)". This is more precise and less prone to misinterpretation.

*   **P1B-M2: Manuscript Structure and Readability**
    *   **Location:** Entire manuscript.
    *   **Problem:** The paper combines three separate, complex analyses. While they are thematically linked to the ECH program, their juxtaposition feels disjointed. The manuscript is extremely dense, with a heavy reliance on long, detailed footnotes (e.g., fn. 1, 3, 4, 6) that contain essential context. This forces the reader to jump constantly between the main text and the notes, disrupting the narrative flow and making the paper difficult to digest.
    *   **Required Fix:** Restructure the paper to improve readability.
        1.  Consider moving the most detailed technical discussions from footnotes into appendices. For example, the full sample-count reconciliation in footnote 1 (Page 3) and the detailed definition of the pipeline SNR in footnote 4 (Page 10) are better suited for an appendix on MCMC and pipeline specifics, respectively.
        2.  In the introduction, provide a more explicit roadmap that not only lists the three analyses but also explains *why* they are being presented together in this specific companion paper and how they logically connect, beyond simply being "technical verification."

*   **P1B-M3: Uncomputed/Unclear Quantitative Claims**
    *   **Location:** Section VI (Page 14).
    *   **Problem:** The text states, "Even the lower end [of required `Cay`] exceeds the standard KSVZ/DFSZ benchmark range, which predicts `Cay ~ O(1)`." While this is a standard result, the paper would be strengthened by citing a canonical review or original paper for this benchmark range.
    *   **Required Fix:** Add a citation to a standard reference for the `Cay ~ O(1)` KSVZ/DFSZ benchmark.

#### MINOR

*   **P1B-m1: Clarification of `w0wa` Systematic**
    *   **Location:** Section IV (Physics interpretation paragraph, Page 4) and Section V.C (Page 12).
    *   **Problem:** The paper correctly identifies the use of a product likelihood for two overlapping supernova datasets (DES-SN5YR and Pantheon+) as a systematic. It states the bias is "a small inward pull." While a full joint covariance is outside the scope, it would be helpful to estimate the potential magnitude of this effect, even if just to confirm it is sub-dominant to the statistical uncertainties. The authors cite Vincenzi et al. [16], which is good, but a sentence summarizing that work's conclusion on the size of the effect would make this paper more self-contained.
    *   **Required Fix:** Add a sentence quantifying, at least by order of magnitude, the expected impact of the overlapping SN samples on the `w0wa` posteriors, citing the relevant findings from Ref. [16].

*   **P1B-m2: Ambiguity in NaMaster Pipeline Scope**
    *   **Location:** Abstract (Page 1) and Section IV (Page 8).
    *   **Problem:** The abstract states the validation test confirms "algebraic pseudo-C_l E-B deconvolution under MASTER [2] mode coupling, NOT the physical separation of the cosmic-rotation angle β from the instrumental-miscalibration angle α". This is an excellent and crucial clarification. However, the text in Section IV does not explicitly mention the `α` angle degeneracy.
    *   **Required Fix:** Briefly reiterate in the main text of Section IV (e.g., in the "Scope note") that this validation on synthetic, foreground-free skies cannot address the `β-α` degeneracy, which is a dominant systematic in real-world measurements. This reinforces the abstract's important scope limitation.

*   **P1B-m3: Table V "Claims Classification"**
    *   **Location:** Table V (Page 20).
    *   **Problem:** This table is highly unconventional for a physics journal article and reads more like an internal project management tool. While the intent of transparently tracking claims is laudable, its format is jarring.
    *   **Required Fix:** Reformat this information into a more conventional summary paragraph in the reproducibility appendix. For example: "The principal quantitative results of this paper are summarized as follows: The ΔNeff posterior means are [-0.020 ± 0.169 (full-tension), ...]. These values were verified internally against the frozen MCMC chains committed at [version/DOI]. The NaMaster pipeline bias was verified against the committed pipeline artifacts. The model-comparison statistics (ΔAIC, etc.) are explicitly not reported and are deferred to future work."

#### NIT

*   **P1B-N1: Awkward Phrasing**
    *   **Location:** Abstract (Page 1).
    *   **Problem:** The phrase "...and are not directly comparable to each other's published sky significances" is slightly awkward.
    *   **Required Fix:** Suggest rephrasing to "...and are not directly comparable to the significances of published sky measurements."

*   **P1B-N2: Informal Filename in Footnote**
    *   **Location:** Footnote 1 (Page 3).
    *   **Problem:** The text refers to a file `COUNT_EXPLANATION.md`. This is too informal for a PRD publication.
    *   **Required Fix:** Change to "...documented in the reproducibility repository."

*   **P1B-N3: Typo/Spacing**
    *   **Location:** Section IV (Page 8, "Mask" paragraph).
    *   **Problem:** The sentence "...which is the quantity this validation is designed to characterize." is missing a period.
    *   **Required Fix:** Add a period at the end of the sentence.

*   **P1B-N4: Citation Style**
    *   **Location:** Abstract (Page 1).
    *   **Problem:** The abstract cites "Paper I(a) [1]". It is unusual to have citations in the abstract.
    *   **Required Fix:** While sometimes permitted, consider removing the citation from the abstract and ensuring the first mention in the main text is properly cited.

### Summary Recommendation

**MAJOR REVISIONS**

This manuscript contains high-quality, rigorous technical work that serves as a valuable validation companion for a larger research program. The authors' commitment to transparency and reproducibility is commendable. However, the paper in its current form is hindered by significant presentational issues, including a disjointed structure, overly dense text with critical information in footnotes, and the use of potentially misleading statistical notation for the `w0wa` results. The revisions outlined above, particularly regarding the structure, readability, and the careful framing of statistical claims, are necessary to bring the manuscript up to the high standards of clarity and accessibility expected for publication in Physical Review D. The underlying science is sound; the communication of that science needs substantial improvement.