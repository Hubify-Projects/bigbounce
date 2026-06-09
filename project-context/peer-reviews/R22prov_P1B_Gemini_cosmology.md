# P1B R22prov — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (11767 chars)
**Wall time**: 171.6s

---

**Referee Report on "Technical Verification Companion to the ECH Spin-Torsion Program..."**

**Report ID:** PRD-2026-Golden-P1B

## General Comments

This manuscript presents technical verification for three separate analyses supporting a companion paper on Einstein-Cartan-Holst (ECH) cosmology. The three analyses are: (1) a standard ΛCDM+ΔNeff MCMC analysis to serve as a null test, (2) a validation of a NaMaster-based pipeline for cosmic birefringence, and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model.

The paper is structured as a technical companion, and its primary strength is the author's transparency regarding the scope and limitations of the work. The disclaimers about what is *not* being claimed (e.g., this is not a test of a torsion-modified Boltzmann code; the pipeline validation is not a sky detection) are clear and appropriate. The computational work appears to be executed correctly, and the reproducibility materials are a welcome addition.

However, the manuscript suffers from several essential and major flaws that make it unsuitable for publication in Physical Review D in its current form. The most serious issue is the inclusion of multiple placeholder citations to non-existent preprints, which is unacceptable. Additionally, there are significant issues with the framing of the primary physics case (the "spectator" ALP is shown to be mostly a non-spectator), clarity in the presentation of key results, and consistency in the datasets being discussed.

## Findings

### ESSENTIAL

**P1B-E1: Placeholder Citations (Page 12, References)**
*   **Problem:** The reference list contains multiple citations to preprints with future dates and seemingly placeholder arXiv identifiers. Specifically, references [3], [11], and [12] are cited as "arXiv preprint (2025)" with identifiers like `arXiv:2509.13654`. A manuscript submitted for peer review cannot cite non-existent, non-public work. This is a critical failure of academic practice.
*   **Fix:** The manuscript cannot be considered for publication until all cited sources are publicly available on the arXiv or in a journal. All claims and comparisons relying on these sources must be removed or be based on currently available data and papers.

**P1B-E2: Misleading "Spectator-ALP" Framing (Page 7, fn. 5; Page 10, fn. 6)**
*   **Problem:** The paper is titled and framed around a "Spectator-ALP Model". However, footnotes 5 and 6, and the associated discussion, explicitly state that the spectator condition (`Ω_a << 1`) requires significant fine-tuning (`θ_i ~ 0.1`, a ~25x tuning). The actual MCMC analysis uses a prior `θ_i ∈ [0.5, 2]`, which corresponds to the dark-energy-ALP regime where the ALP's energy density is comparable to the critical density (`Ω_a ~ 1`). Therefore, the analysis presented does not primarily test a *spectator* ALP but rather a dark-energy ALP. The framing is a significant misrepresentation of the work performed.
*   **Fix:** The paper must be reframed. The title, abstract, and all relevant sections must be revised to accurately reflect that the analysis constrains a dark-energy-class ALP. The "spectator" label should be removed or heavily qualified everywhere to state that it only applies to a small, fine-tuned corner of the parameter space which is not the focus of the MCMC.

### MAJOR

**P1B-M1: Ambiguous Birefringence Likelihood Source (Page 11, Likelihood stack)**
*   **Problem:** The "Likelihood stack" section states: "Both fits use a Gaussian summary likelihood on the published joint Planck PR4 + ACT DR6 isotropic-birefringence measurement β_obs = 0.342° ± 0.094° [2, 3]". This is incorrect. The value `β = 0.342° ± 0.094°` comes from Eskilt & Komatsu [2], which is a WMAP+Planck analysis. Reference [3] is a separate ACT DR6 analysis (which, as noted in P1B-E1, is not yet public). The text incorrectly attributes the likelihood to a joint analysis of [2] and [3].
*   **Fix:** Clarify that the MCMC is anchored to a Gaussian likelihood representing the posterior from Ref. [2] alone. Remove the reference to [3] in this context, and ensure the text is consistent throughout.

**P1B-M2: Confusing and Incorrect NaMaster Bias Analysis (Page 6, Sky-fraction sweep)**
*   **Problem:** The paragraph discussing the pipeline bias is confusing and contains a numerical error. It states that the bias has a "relative ~ 12% amplitude-dependent component" when going from a 0.27° injection (bias=0.032°) to a 0.342° injection (bias=0.040°). The relative change in the additive bias is `(0.040 - 0.032) / 0.032 = 0.25`, or 25%, not 12%. The subsequent paragraph correctly identifies a "~12% multiplicative under-recovery" (`(β_inj - β_rec) / β_inj`). The text conflates these two different concepts (the amplitude dependence of the additive bias vs. the fractional under-recovery) and miscalculates the former.
*   **Fix:** Rewrite this section for clarity and correctness. Distinguish clearly between the additive bias (`β_rec - β_inj`) and the multiplicative recovery factor (`β_rec / β_inj`). Correct the statement about the relative change in the bias to 25%.

**P1B-M3: Inconsistent Dataset Usage (Page 1, fn. a)**
*   **Problem:** Footnote 'a' states that the headline `β` value is from the published PR3+WMAP9 analysis in [2], but the public code used for re-analysis in the companion work was updated to use PR4/NPIPE. The paper then proceeds to use the PR3+WMAP9 headline value as the anchor for its PR4/NPIPE-based ALP analysis. This introduces an inconsistency. While the difference may be small, a technical verification paper must be precise.
*   **Fix:** The author must either (a) use a `β` value derived from a PR4/NPIPE analysis as the input for the ALP MCMC to maintain consistency, or (b) explicitly justify why using the PR3+WMAP9 value is acceptable and provide an estimate of the systematic error introduced by this mismatch.

### MINOR

**P1B-m1: Inclusion of "Ongoing" MCMC Run (Page 1, Abstract; Page 9, Conclusions)**
*   **Problem:** The abstract and conclusions include a "third Planck-only combination ongoing" or "still accumulating" in the total sample counts and discussion. This run is not converged and its results are not finalized. Including it adds confusion and inflates the scope of the completed work.
*   **Fix:** Remove all references to this unconverged, ongoing run from the abstract and summary statements. The paper should only report on finalized, "frozen" results.

**P1B-m2: Inconsistent Quoted Values (Page 4, text; Page 7, text)**
*   **Problem:** There are minor discrepancies between values quoted in the main text and in the tables. For example, on p. 4, the text quotes `H0 = 67.69` and `ΔNeff` error of `0.17`, while Table I has `H0 = 67.68` and `ΔNeff` error of `0.169`. On p. 7, the `w0` and `wa` values are rounded differently than in Table II.
*   **Fix:** Ensure all numerical values are quoted consistently throughout the manuscript.

**P1B-m3: Outdated ALP Fit Scope (Page 11, Scope statement)**
*   **Problem:** The scope statement for the ALP fit on page 11 mentions a "`C_aγ ∈ [4, 12]` benchmark sweep". However, the main results presented in the text and Figure 4 are from a more comprehensive continuous-prior run with `C_aγ ∈ [4, 60]`.
*   **Fix:** Update this scope statement to reflect the final, continuous-prior analysis that is presented as the main result.

**P1B-m4: Overly Strong Language for `w0wa` Result (Page 3, Physics interpretation)**
*   **Problem:** The text states the `w0wa` posterior "disfavors" the ΛCDM point. While the posterior mean is several sigma away, the author correctly notes that a robust Bayes factor has not been computed. In this context, "disfavors" is too strong and implies a formal model selection result.
*   **Fix:** Soften the language. State that the posterior is centered `4.3σ` (for `w0`) and `-3.6σ` (for `wa`) from the ΛCDM point, but explicitly reiterate that this does not constitute formal model evidence against ΛCDM.

### NIT

**P1B-N1: Jarring SNR Figure (Page 2, Introduction)**
*   **Problem:** The introduction quotes a pipeline SNR of "20.32σ". While this is clarified in the text and a footnote, the number is jarring and easily misinterpreted if read out of context.
*   **Fix:** Consider rephrasing in the introduction to immediately frame it as a calibration metric, for example: "The pipeline's ability to recover the mean of injected signals is established with high precision (an effective SNR of 20.32 over 500 realizations)...".

## Summary recommendation

**REJECT**

This manuscript, while showing evidence of careful computational work and a laudable commitment to transparency, is not ready for publication in Physical Review D. The presence of placeholder citations for non-existent articles is an essential, disqualifying flaw. Beyond this, the misleading framing of the central "spectator-ALP" model, which the paper's own analysis shows is not a spectator in the relevant parameter space, requires a fundamental revision of the paper's narrative and claims. Major issues of clarity in the analysis of the pipeline bias and consistency in the use of datasets further detract from the paper's quality.

The author is encouraged to address these extensive issues and may consider resubmitting the manuscript once all cited works are publicly available and the scientific narrative has been brought into alignment with the actual results of the analyses.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated review, incorporating the new findings from the second, more rigorous pass.

================================================================
**Referee Report on "Technical Verification Companion to the ECH Spin-Torsion Program..."**

**Report ID:** PRD-2026-Golden-P1B

## General Comments

This manuscript presents technical verification for three separate analyses supporting a companion paper on Einstein-Cartan-Holst (ECH) cosmology. The three analyses are: (1) a standard ΛCDM+ΔNeff MCMC analysis to serve as a null test, (2) a validation of a NaMaster-based pipeline for cosmic birefringence, and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model.

The paper is structured as a technical companion, and its primary strength is the author's transparency regarding the scope and limitations of the work. The disclaimers about what is *not* being claimed (e.g., this is not a test of a torsion-modified Boltzmann code; the pipeline validation is not a sky detection) are clear and appropriate. The computational work appears to be executed correctly, and the reproducibility materials are a welcome addition.

However, the manuscript suffers from several essential and major flaws that make it unsuitable for publication in Physical Review D in its current form. The most serious issue is the inclusion of multiple placeholder citations to non-existent preprints, which is unacceptable. Additionally, there are significant issues with the framing of the primary physics case (the "spectator" ALP is shown to be mostly a non-spectator), clarity in the presentation of key results, consistency in the datasets being discussed, and a flawed statistical calculation for a key dark energy parameter.

## Findings

### ESSENTIAL

**P1B-E1: Placeholder Citations (Page 12, References)**
*   **Problem:** The reference list contains multiple citations to preprints with future dates and seemingly placeholder arXiv identifiers. Specifically, references [3], [11], and [12] are cited as "arXiv preprint (2025)" with identifiers like `arXiv:2509.13654`. A manuscript submitted for peer review cannot cite non-existent, non-public work. This is a critical failure of academic practice.
*   **Fix:** The manuscript cannot be considered for publication until all cited sources are publicly available on the arXiv or in a journal. All claims and comparisons relying on these sources must be removed or be based on currently available data and papers.

**P1B-E2: Misleading "Spectator-ALP" Framing (Page 7, fn. 5; Page 10, fn. 6)**
*   **Problem:** The paper is titled and framed around a "Spectator-ALP Model". However, footnotes 5 and 6, and the associated discussion, explicitly state that the spectator condition (`Ω_a << 1`) requires significant fine-tuning (`θ_i ~ 0.1`, a ~25x tuning). The actual MCMC analysis uses a prior `θ_i ∈ [0.5, 2]`, which corresponds to the dark-energy-ALP regime where the ALP's energy density is comparable to the critical density (`Ω_a ~ 1`). Therefore, the analysis presented does not primarily test a *spectator* ALP but rather a dark-energy ALP. The framing is a significant misrepresentation of the work performed.
*   **Fix:** The paper must be reframed. The title, abstract, and all relevant sections must be revised to accurately reflect that the analysis constrains a dark-energy-class ALP. The "spectator" label should be removed or heavily qualified everywhere to state that it only applies to a small, fine-tuned corner of the parameter space which is not the focus of the MCMC.

### MAJOR

**P1B-M1: Ambiguous Birefringence Likelihood Source (Page 11, Likelihood stack)**
*   **Problem:** The "Likelihood stack" section states: "Both fits use a Gaussian summary likelihood on the published joint Planck PR4 + ACT DR6 isotropic-birefringence measurement β_obs = 0.342° ± 0.094° [2, 3]". This is incorrect. The value `β = 0.342° ± 0.094°` comes from Eskilt & Komatsu [2], which is a WMAP+Planck analysis. Reference [3] is a separate ACT DR6 analysis (which, as noted in P1B-E1, is not yet public). The text incorrectly attributes the likelihood to a joint analysis of [2] and [3].
*   **Fix:** Clarify that the MCMC is anchored to a Gaussian likelihood representing the posterior from Ref. [2] alone. Remove the reference to [3] in this context, and ensure the text is consistent throughout.

**P1B-M2: Confusing and Incorrect NaMaster Bias Analysis (Page 6, Sky-fraction sweep)**
*   **Problem:** The paragraph discussing the pipeline bias is confusing and contains a numerical error. It states that the bias has a "relative ~ 12% amplitude-dependent component" when going from a 0.27° injection (bias=0.032°) to a 0.342° injection (bias=0.040°). The relative change in the additive bias is `(0.040 - 0.032) / 0.032 = 0.25`, or 25%, not 12%. The subsequent paragraph correctly identifies a "~12% multiplicative under-recovery" (`(β_inj - β_rec) / β_inj`). The text conflates these two different concepts (the amplitude dependence of the additive bias vs. the fractional under-recovery) and miscalculates the former.
*   **Fix:** Rewrite this section for clarity and correctness. Distinguish clearly between the additive bias (`β_rec - β_inj`) and the multiplicative recovery factor (`β_rec / β_inj`). Correct the statement about the relative change in the bias to 25%.

**P1B-M3: Inconsistent Dataset Usage (Page 1, fn. a)**
*   **Problem:** Footnote 'a' states that the headline `β` value is from the published PR3+WMAP9 analysis in [2], but the public code used for re-analysis in the companion work was updated to use PR4/NPIPE. The paper then proceeds to use the PR3+WMAP9 headline value as the anchor for its PR4/NPIPE-based ALP analysis. This introduces an inconsistency. While the difference may be small, a technical verification paper must be precise.
*   **Fix:** The author must either (a) use a `β` value derived from a PR4/NPIPE analysis as the input for the ALP MCMC to maintain consistency, or (b) explicitly justify why using the PR3+WMAP9 value is acceptable and provide an estimate of the systematic error introduced by this mismatch.

**P1B-M4: Flawed `wpivot` Calculation (Page 4, fn. b)**
*   **Problem:** The footnote in Table II describing the calculation of the pivot redshift `z_p` and the variance of `w_pivot` is arithmetically and conceptually flawed. The definition given for the pivot scale, `a_p = 1 - Cov(w_0, w_a)/Var(w_a)`, appears to have a sign error compared to the standard definition. Furthermore, the formula for the variance of `w_pivot` assumes `w_0` and `w_a` are uncorrelated, which contradicts the purpose of defining a pivot scale in the first place. This undermines the quantitative claims made about `w_pivot` being consistent with -1.
*   **Fix:** The entire calculation and discussion of `w_pivot` must be re-evaluated using standard, correct statistical definitions. The text and table footnote must be corrected to reflect a valid calculation.

### MINOR

**P1B-m1: Inclusion of "Ongoing" MCMC Run (Page 1, Abstract; Page 9, Conclusions)**
*   **Problem:** The abstract and conclusions include a "third Planck-only combination ongoing" or "still accumulating" in the total sample counts and discussion. This run is not converged and its results are not finalized. Including it adds confusion and inflates the scope of the completed work.
*   **Fix:** Remove all references to this unconverged, ongoing run from the abstract and summary statements. The paper should only report on finalized, "frozen" results.

**P1B-m2: Inconsistent Quoted Values (Page 4, text; Page 7, text)**
*   **Problem:** There are minor discrepancies between values quoted in the main text and in the tables. For example, on p. 4, the text quotes `H0 = 67.69` and `ΔNeff` error of `0.17`, while Table I has `H0 = 67.68` and `ΔNeff` error of `0.169`. On p. 7, the `w0` and `wa` values are rounded differently than in Table II.
*   **Fix:** Ensure all numerical values are quoted consistently throughout the manuscript.

**P1B-m3: Outdated ALP Fit Scope (Page 11, Scope statement)**
*   **Problem:** The scope statement for the ALP fit on page 11 mentions a "`C_aγ ∈ [4, 12]` benchmark sweep". However, the main results presented in the text and Figure 4 are from a more comprehensive continuous-prior run with `C_aγ ∈ [4, 60]`.
*   **Fix:** Update this scope statement to reflect the final, continuous-prior analysis that is presented as the main result.

**P1B-m4: Overly Strong Language for `w0wa` Result (Page 3, Physics interpretation)**
*   **Problem:** The text states the `w0wa` posterior "disfavors" the ΛCDM point. While the posterior mean is several sigma away, the author correctly notes that a robust Bayes factor has not been computed. In this context, "disfavors" is too strong and implies a formal model selection result.
*   **Fix:** Soften the language. State that the posterior is centered `4.3σ` (for `w0`) and `-3.6σ` (for `wa`) from the ΛCDM point, but explicitly reiterate that this does not constitute formal model evidence against ΛCDM.

**P1B-m5: Unclear Error Bars in Figure 3 (Page 6)**
*   **Problem:** The error bars on the recovered `β` points in Figure 3 are ambiguous. They are visually too large to be the standard error on the mean of 500 realizations and are likely the per-realization standard deviation.
*   **Fix:** The caption should explicitly state what the error bars represent (e.g., "error bars show the standard deviation of the 500 MC realizations") to avoid misinterpretation of the pipeline's calibration precision.

**P1B-m6: Stale Number in Figure 4 Caption (Page 9)**
*   **Problem:** The caption for Figure 4 quotes the recovered rotation as `β = 0.324° ± 0.099°`, while the main text on page 8 reports it as `β = 0.326° ± 0.099°`.
*   **Fix:** Correct this minor inconsistency.

**P1B-m7: Unquantified Null Test Result (Page 6)**
*   **Problem:** The text mentions a null check for the NaMaster pipeline ("for β = 0, recovery is consistent with zero (null check)"), but does not provide the recovered value and its uncertainty.
*   **Fix:** For a verification paper, this number should be explicitly reported (e.g., "For an injected signal of β=0, the pipeline recovers β = X ± Y").

### NIT

**P1B-N1: Jarring SNR Figure (Page 2, Introduction)**
*   **Problem:** The introduction quotes a pipeline SNR of "20.32σ". While this is clarified in the text and a footnote, the number is jarring and easily misinterpreted if read out of context.
*   **Fix:** Consider rephrasing in the introduction to immediately frame it as a calibration metric, for example: "The pipeline's ability to recover the mean of injected signals is established with high precision (an effective SNR of 20.32 over 500 realizations)...".

## Summary recommendation

**REJECT**

This manuscript, while showing evidence of careful computational work and a laudable commitment to transparency, is not ready for publication in Physical Review D. The presence of placeholder citations for non-existent articles is an essential, disqualifying flaw. Beyond this, the misleading framing of the central "spectator-ALP" model, which the paper's own analysis shows is not a spectator in the relevant parameter space, requires a fundamental revision of the paper's narrative and claims. Major issues of clarity in the analysis of the pipeline bias, consistency in the use of datasets, and a flawed statistical calculation further detract from the paper's quality.

The author is encouraged to address these extensive issues and may consider resubmitting the manuscript once all cited works are publicly available and the scientific narrative has been brought into alignment with the actual results of the analyses.