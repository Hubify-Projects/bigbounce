# P1B R26conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1b_mcmc_companion_v1B.0.53.pdf` md5=86261d4b pages=16
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (8839 chars)
**Wall time**: 167.3s

---

**Referee Report on "Technical Verification Companion to the ECH Spin-Torsion Program:..."**

This manuscript presents three technical analyses related to the Einstein-Cartan-Holst (ECH) spin-torsion cosmology program: (1) a stock-CAMB MCMC analysis of the ΛCDM+ΔNeff model as a null-consistency test, (2) a Monte Carlo validation of a NaMaster pseudo-Cℓ pipeline for cosmic birefringence, and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model.

The analyses are, for the most part, technically sound and the authors are commendably careful in scoping their claims. The distinction between pipeline validation and sky detection, and between model accommodation and prediction, is clearly and correctly articulated. The detailed calculations, particularly the robustness checks in the NaMaster and ALP sections, add confidence to the results.

However, the manuscript in its current form is not suitable for publication in Physical Review D. It contains numerous internal review artifacts, reads in places like a research log rather than a final scientific paper, and has a major deficiency in its data availability policy that hinders reproducibility. Significant revisions are required to bring it up to the journal's standards.

---
### Detailed Findings

#### ESSENTIAL

**P1B-E1: Removal of Internal Review Artifacts and "Process" Language**
*   **Location:** Throughout the manuscript.
*   **Problem:** The paper is littered with language that describes the process of the analysis, including corrections from previous internal versions. This is inappropriate for a formal publication, which should present the final, polished result.
    *   **Page 4, Table I Caption:** "Correction note: an earlier version quoted the Planck+BAO+SN S8 marginal as 0.831 ± 0.018; the ±0.018 width could not be traced to any committed analysis, and a direct GetDist pass over the frozen chains gives 0.827±0.010 (132,949 samples), which replaces it in the table."
    *   **Page 7, Fig 3 Caption:** "...per-realization σβ was not recorded in the original canonical fsky = 0.32 artifact, so that point is plotted with the mean only; a dedicated 500-MC rerun (fn. 3) measures σβ = 0.046° at this point."
    *   **Page 8, Footnote:** "...quoted in an earlier draft of this footnote."
    *   **Page 9, Sec. VI:** "...an earlier draft quoted [0.2, 1.1] with Δφ/fa ≈ 0.65 at m = H0 — those values do not reproduce from the committed integration and are corrected here)."
    *   **Page 10, Sec. VI:** "Correction note: an earlier draft paired Δφ/fa ≈ 1.0–1.07 with m ≈ 1.8-2 H0; ... and the mass pairings are corrected throughout against the released grid scan."
    *   **Page 10, Sec. VI:** "...an earlier draft quoted [0.17,0.43]° from a joint-trajectory scan for which no artifact survives, and that range is superseded by the committed grid scan."
    *   **Page 14, Appendix C:** "Correction note: an earlier draft described the model-dependent fits as 'three benchmark configurations...'; no archived chain matches that description, and the configuration list below replaces it with the committed truth."
*   **Required Fix:** All such "process" language, correction notes, and references to "earlier drafts" or superseded results must be removed. The text should be rewritten to present only the final, correct, and committed results and methods.

**P1B-E2: Removal of Internal Audit Table**
*   **Location:** Page 15, Table IV.
*   **Problem:** Table IV, "Claims classification for this companion paper," appears to be an internal project management or audit tool. It has no place in a scientific publication and is highly unconventional.
*   **Required Fix:** Remove Table IV entirely.

**P1B-E3: Data Availability of MCMC Chains**
*   **Location:** Page 13, Appendix A.
*   **Problem:** The manuscript states: "What is NOT included. - MCMC chains are not pre-computed (regenerate via reproduce_cosmology.sh, ~4-12h per config on 4 CPU cores)." While providing the code to regenerate the chains is necessary, it is not sufficient. The final MCMC chains that were used to generate the plots and tables in the paper are a primary data product. Standard practice in modern cosmology requires these chains to be made publicly available to ensure full reproducibility and allow for independent verification and further analysis by the community.
*   **Required Fix:** The final, converged MCMC chains used for all results in the paper must be made publicly available, for example, through the provided GitHub repository or a service like Zenodo. The "Data and Code Availability" section should be updated to reflect this.

#### MAJOR

**P1B-M1: Clarity of w-w_a Results Presentation**
*   **Location:** Page 3, 5, 9.
*   **Problem:** The results of the w₀-wₐ analysis are significant and interesting, showing a >4σ departure for w₀ from the ΛCDM value. However, the discussion is somewhat fragmented across the text. The crucial caveat that this is a "marginal-tail posterior-extrapolation departure" and not a robust Bayes factor is correctly made but could be integrated more centrally with the main claim.
*   **Required Fix:** Consolidate the presentation of the w₀-wₐ results. When first presenting the >4σ departure, immediately include the crucial caveats about the lack of a proper model comparison (deferred nested sampling) and the nature of the "marginal-tail" significance. This will prevent any potential misinterpretation by the reader.

#### MINOR

**P1B-m1: Clarification of Likelihood in ALP analysis**
*   **Location:** Page 11 and 14.
*   **Problem:** The analysis fits the ALP model to a Gaussian summary of the Eskilt & Komatsu (2022) posterior for β ("beta_obs: 0.342, sigma_beta: 0.094"). While this is a valid approach for a consistency check, it is an important limitation compared to a full analysis on the EB power spectra. This is mentioned in Appendix C but should be stated more prominently in the main text.
*   **Required Fix:** In Section VI, when introducing the MCMC analysis of the ALP model, explicitly state that the likelihood used is a Gaussian approximation of the published posterior on β, not a direct likelihood from the CMB power spectra.

**P1B-m2: Justification for NaMaster Unweighted Fit**
*   **Location:** Page 8, Sec. IV.
*   **Problem:** The robustness battery reveals that ~80% of the pipeline bias comes from using an unweighted χ² template fit. The paper then carries the full bias forward as a systematic floor. While this is a conservative choice, the motivation for using an unweighted fit as the default in the first place is not discussed.
*   **Required Fix:** Briefly add a sentence explaining the motivation for choosing the unweighted fit as the canonical pipeline configuration, given that the inverse-variance weighted fit is shown to be significantly less biased.

---
## Summary recommendation

**MAJOR REVISIONS**

The paper contains valuable and carefully executed technical work. The authors' diligence in scoping their claims and performing robustness checks is a significant strength. However, the manuscript is not yet in a publishable state. The pervasive internal-review language and the lack of public MCMC chains are critical issues that must be addressed. Once the manuscript is rewritten to present a clean, final scientific result and the data products are made available to the community, it will represent a solid contribution to the literature.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated referee report, incorporating the findings from the second, more rigorous review.

================================================================
**Referee Report on "Technical Verification Companion to the ECH Spin-Torsion Program:..."**

This manuscript presents three technical analyses related to the Einstein-Cartan-Holst (ECH) spin-torsion cosmology program: (1) a stock-CAMB MCMC analysis of the ΛCDM+ΔNeff model as a null-consistency test, (2) a Monte Carlo validation of a NaMaster pseudo-Cℓ pipeline for cosmic birefringence, and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model.

The analyses are, for the most part, technically sound and the authors are commendably careful in scoping their claims. The distinction between pipeline validation and sky detection, and between model accommodation and prediction, is clearly and correctly articulated. The detailed calculations, particularly the robustness checks in the NaMaster and ALP sections, add confidence to the results. The internal arithmetic and cross-referencing are of a very high standard.

However, the manuscript in its current form is not suitable for publication in Physical Review D. It contains numerous internal review artifacts, reads in places like a research log rather than a final scientific paper, and has a major deficiency in its data availability policy that hinders reproducibility. Significant revisions are required to bring it up to the journal's standards.

---
### Detailed Findings

#### ESSENTIAL

**P1B-E1: Removal of Internal Review Artifacts and "Process" Language**
*   **Location:** Throughout the manuscript.
*   **Problem:** The paper is littered with language that describes the process of the analysis, including corrections from previous internal versions. This is inappropriate for a formal publication, which should present the final, polished result.
    *   **Page 4, Table I Caption:** "Correction note: an earlier version quoted..."
    *   **Page 7, Fig 3 Caption:** "...per-realization σβ was not recorded in the original canonical fsky = 0.32 artifact..."
    *   **Page 8, Footnote:** "...quoted in an earlier draft of this footnote."
    *   **Page 9, Sec. VI:** "...an earlier draft quoted ... those values do not reproduce ... and are corrected here)."
    *   **Page 10, Sec. VI:** "Correction note: an earlier draft paired..."
    *   **Page 10, Sec. VI:** "...an earlier draft quoted ... that range is superseded by the committed grid scan."
    *   **Page 14, Appendix C:** "Correction note: an earlier draft described..."
*   **Required Fix:** All such "process" language, correction notes, and references to "earlier drafts" or superseded results must be removed. The text should be rewritten to present only the final, correct, and committed results and methods.

**P1B-E2: Removal of Internal Audit Table**
*   **Location:** Page 15, Table IV.
*   **Problem:** Table IV, "Claims classification for this companion paper," appears to be an internal project management or audit tool. It has no place in a scientific publication and is highly unconventional.
*   **Required Fix:** Remove Table IV entirely.

**P1B-E3: Data Availability of MCMC Chains**
*   **Location:** Page 13, Appendix A.
*   **Problem:** The manuscript states: "What is NOT included. - MCMC chains are not pre-computed (regenerate via reproduce_cosmology.sh, ~4-12h per config on 4 CPU cores)." While providing the code to regenerate the chains is necessary, it is not sufficient. The final MCMC chains that were used to generate the plots and tables in the paper are a primary data product. Standard practice in modern cosmology requires these chains to be made publicly available to ensure full reproducibility and allow for independent verification and further analysis by the community.
*   **Required Fix:** The final, converged MCMC chains used for all results in the paper must be made publicly available, for example, through the provided GitHub repository or a service like Zenodo. The "Data and Code Availability" section should be updated to reflect this.

#### MAJOR

**P1B-M1: Clarity of w-w_a Results Presentation**
*   **Location:** Page 3, 5, 9.
*   **Problem:** The results of the w₀-wₐ analysis are significant and interesting, showing a >4σ departure for w₀ from the ΛCDM value. However, the discussion is somewhat fragmented across the text. The crucial caveat that this is a "marginal-tail posterior-extrapolation departure" and not a robust Bayes factor is correctly made but could be integrated more centrally with the main claim.
*   **Required Fix:** Consolidate the presentation of the w₀-wₐ results. When first presenting the >4σ departure, immediately include the crucial caveats about the lack of a proper model comparison (deferred nested sampling) and the nature of the "marginal-tail" significance. This will prevent any potential misinterpretation by the reader.

#### MINOR

**P1B-m1: Clarification of Likelihood in ALP analysis**
*   **Location:** Page 11 and 14.
*   **Problem:** The analysis fits the ALP model to a Gaussian summary of the Eskilt & Komatsu (2022) posterior for β ("beta_obs: 0.342, sigma_beta: 0.094"). While this is a valid approach for a consistency check, it is an important limitation compared to a full analysis on the EB power spectra. This is mentioned in Appendix C but should be stated more prominently in the main text.
*   **Required Fix:** In Section VI, when introducing the MCMC analysis of the ALP model, explicitly state that the likelihood used is a Gaussian approximation of the published posterior on β, not a direct likelihood from the CMB power spectra.

**P1B-m2: Justification for NaMaster Unweighted Fit**
*   **Location:** Page 8, Sec. IV.
*   **Problem:** The robustness battery reveals that ~80% of the pipeline bias comes from using an unweighted χ² template fit. The paper then carries the full bias forward as a systematic floor. While this is a conservative choice, the motivation for using an unweighted fit as the default in the first place is not discussed.
*   **Required Fix:** Briefly add a sentence explaining the motivation for choosing the unweighted fit as the canonical pipeline configuration, given that the inverse-variance weighted fit is shown to be significantly less biased.

**P1B-m3: Ambiguous Sample Count in Abstract**
*   **Location:** Page 1, Abstract, (1).
*   **Problem:** The abstract states "309,189 frozen samples...". This is the *raw* sample count before burn-in removal. All scientific results are derived from the post-burn-in samples. Quoting the raw number in the abstract is slightly misleading and less informative than quoting the post-burn-in count.
*   **Required Fix:** In the abstract, either quote the total post-burn-in sample count (`216,432`) or remove the sample count entirely. The current raw count is not the most relevant number for the abstract.

**P1B-m4: Inconsistent Use of "ECH" in Title/Abstract vs. Body**
*   **Location:** Title, Abstract, and Body.
*   **Problem:** The title frames the paper as a "Companion to the ECH Spin-Torsion Program," but the body repeatedly and correctly emphasizes that none of the tests are direct tests of ECH. The framing in the title feels like a slight overstatement of the paper's direct relevance.
*   **Required Fix:** This is a suggestion for the author's consideration, not a strict requirement. Consider softening the title to better reflect that the work is *motivated* by ECH but does not directly test it. For example: "Technical Verifications for Cosmological Models with Torsion-Motivated Signatures:..." The current abstract and body are sufficiently clear on this point that this is not an essential change.

#### NEGLIGIBLE

**P1B-N1: Minor Typo in Footnote 3**
*   **Location:** Page 7, Footnote 3.
*   **Problem:** The footnote text describes the scaling of the template-fit SNR with sky fraction as `SNR ∝ f_sky`, but the numbers provided are consistent with the correct `SNR ∝ sqrt(f_sky)` scaling.
*   **Required Fix:** Correct the scaling relation in the footnote to `SNR ∝ sqrt(f_sky)` and update the formula shown in the parenthetical, e.g., `20.32*sqrt(fsky/0.32)`.

---
## Summary recommendation

**MAJOR REVISIONS**

The paper contains valuable and carefully executed technical work. The authors' diligence in scoping their claims and performing robustness checks is a significant strength. However, the manuscript is not yet in a publishable state. The pervasive internal-review language and the lack of public MCMC chains are critical issues that must be addressed. Once the manuscript is rewritten to present a clean, final scientific result and the data products are made available to the community, it will represent a solid contribution to the literature.