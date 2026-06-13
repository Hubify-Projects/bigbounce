# P1A R37conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.68.pdf` md5=0de277bf pages=28
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (11579 chars)
**Wall time**: 171.2s

---

Here is a referee report for the provided paper.

***

**Referee Report: PRD Manuscript [Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes...]**

**To the Editor of Physical Review D,**

This manuscript undertakes a systematic investigation into whether minimal Einstein-Cartan-Holst (ECH) gravity can provide a viable mechanism for late-time cosmic acceleration. The author assesses four enumerated channels and argues for their closure based on a combination of amplitude suppression, naturalness arguments, and a catalog of 14 structural constraints. The paper also presents a noteworthy "perturbation-transparency" result, demonstrating that for canonical scalar matter, the Holst sector decouples from scalar and tensor perturbations, rendering its effects invisible to standard cosmological probes like the CMB power spectra and bispectrum.

The scope of the work is ambitious, and the author is laudably transparent about the crucial assumptions underpinning the analysis, particularly the phenomenological nature of the scaling ansatz required to connect bounce-era physics to the present-day dark energy scale. The perturbation-transparency proof is elegant and appears correct, providing a clear statement on the observational signatures (or lack thereof) of minimal ECH in the perturbative regime.

However, the manuscript in its current form has several essential and major flaws that must be addressed before it can be considered for publication in Physical Review D. The most significant issue is its repeated violation of the standalone-reader principle, relying heavily on numerical results and detailed forecasts from unpublished companion papers. Additionally, several key arguments are presented too concisely to allow for proper scientific scrutiny.

I recommend **MAJOR REVISIONS**. The core physical arguments are promising, but the paper requires substantial restructuring to meet the standards of the journal.

Below is a detailed list of required revisions.

---

### ESSENTIAL REVISIONS

1.  **P1A-E1: Reliance on Unpublished MCMC Results**
    *   **Section/Page:** Sec. IV, p. 4; Table IV, p. 26.
    *   **Problem:** The paper uses specific cosmological parameter values (e.g., `H₀ = 67.68 ± 1.06`, `ΔN_eff = -0.020 ± 0.169`) that are explicitly stated to be from an "internal MCMC analysis" detailed in an unpublished companion paper [6]. A published paper cannot be based on results that are not peer-reviewed and publicly accessible. The statement that these "should be read as internal-analysis inputs" confirms the problem.
    *   **Required Fix:** All numerical results and conclusions derived from this internal MCMC analysis must be removed. The arguments must be reformulated to be purely structural and independent of these specific values, or they must use values from a citable, published source (e.g., the latest Planck 2018 results, clearly cited as such). The paper's claims must stand on their own merit without recourse to inaccessible companion work.

2.  **P1A-E2: Future Publication Date**
    *   **Section/Page:** p. 1.
    *   **Problem:** The paper is dated "June 13, 2026".
    *   **Required Fix:** The date must be corrected to the date of submission.

### MAJOR REVISIONS

1.  **P1A-M1: Reliance on Companion Paper Forecasts**
    *   **Section/Page:** Abstract, p. 1; Table I, p. 4; Sec. VII, p. 15.
    *   **Problem:** The paper's claims about future falsifiability, particularly the `2.6-5σ` forecast for detecting `f_NL = -35/8` with SPHEREx, are imported from another unpublished companion paper [2]. While referencing a concurrent submission is permissible, the current text presents these forecasts as established facts that are central to the paper's framing.
    *   **Required Fix:** The text must be revised to clearly and consistently frame these as conditional forecasts from a companion paper. For example: "If the forecast presented in the companion work [2] is realized, SPHEREx could test...". The novel contributions of the present manuscript must be clearly delineated from the results of its companions.

2.  **P1A-M2: Confusing Dimensional Analysis of the Parity-Odd Operator**
    *   **Section/Page:** Sec. II C, p. 7.
    *   **Problem:** The main text's discussion of the mass dimension of the parity-odd operator in Eq. (6) is confusing. The operator, as written, has a mass dimension of +1 for the Lagrangian density, not the required +4. While Appendix B clarifies this is a known feature of the phenomenological ansatz, a reader of the main text is left with a confusing and seemingly incorrect dimensional argument.
    *   **Required Fix:** The main text in Section II C must be rewritten for clarity. It should state upfront that the operator is not a standard dimension-4 EFT operator and immediately direct the reader to Appendix B for a full discussion of its dimensional status and the nature of the on-shell scaling ansatz. This is a crucial caveat that must not be buried in an appendix.

3.  **P1A-M3: Insufficient Justification for Structural "Barriers"**
    *   **Section/Page:** Sec. IX, pp. 16-17.
    *   **Problem:** This section presents a catalog of 13 "logically-independent" barriers to the ECH dark-energy mechanism. While this is a potentially valuable contribution, the arguments are presented with extreme brevity, making them impossible to critically assess. For instance, Barrier 12 introduces a GW ceiling with a quadratic scaling, `Ω_GW ∝ (ρ_crit/ρ_Pl)²`, which is presented as an ansatz without derivation. The entire section reads as a list of claims rather than a rigorous demonstration.
    *   **Required Fix:** This section must be substantially expanded. For each barrier, the author must provide a clear, self-contained derivation or a much more detailed physical justification. Alternatively, if these are summaries of existing constraints, they must be clearly attributed with specific citations to the original derivations. Barriers that are new to this work must be proven with the rigor expected of a PRD article, possibly in an appendix if the derivation is lengthy.

4.  **P1A-M4: Unjustified Prefactor in Dilution Formula**
    *   **Section/Page:** Sec. II C 1, p. 8.
    *   **Problem:** The inflationary dilution factor in Eq. (11) includes a term `(T_reh/M_GUT)^(3/2)`. The physical justification for the `3/2` exponent rests on a vague "parity-odd density-of-states factor" and is explicitly labeled a "phenomenological phase-space ansatz". This is a weak link in the quantitative argument that determines the required number of e-folds, `N_tot ≈ 92`.
    *   **Required Fix:** The author must either provide a more rigorous derivation for this factor or, failing that, must explicitly analyze the sensitivity of the paper's conclusions (especially the value of `N_tot` and the structural tension with `f_NL`) to O(1) variations in this prefactor. The current hand-wavy justification is insufficient.

### MINOR REVISIONS

1.  **P1A-m1: Internal Versioning in Dateline**
    *   **Section/Page:** p. 1.
    *   **Problem:** The dateline includes an internal version number ("v1A.0.68").
    *   **Required Fix:** This should be removed for publication.

2.  **P1A-m2: Redundant Figure**
    *   **Section/Page:** p. 22.
    *   **Problem:** Figure 6 presents the same forecast information as Figure 4, making it largely redundant.
    *   **Required Fix:** The author should consider removing Figure 6 and referring back to Figure 4 in the text.

3.  **P1A-m3: Potentially Confusing Definition of `ρ_Λ`**
    *   **Section/Page:** Sec. II C, p. 7.
    *   **Problem:** The relation `ρ_Λ = Λ_eff M_Pl² = Ξ M_Pl⁴` could be confusing. While correct under the convention `M_Pl = G^{-1/2}`, it conflates the cosmological constant `Λ_eff` with the dimensionless parameter `Ξ`.
    *   **Required Fix:** For clarity, rewrite this as: "The effective cosmological constant `Λ_eff` is related to the vacuum energy density by `ρ_Λ = Λ_eff M_Pl²`. We parameterize this density as `ρ_Λ = Ξ M_Pl⁴`, which defines the dimensionless parameter `Ξ`."

4.  **P1A-m4: Standalone-Reader Issue with Galaxy Spin Result**
    *   **Section/Page:** Sec. III B, p. 10.
    *   **Problem:** The null result for galaxy spin asymmetry is stated as a fact, but the analysis is contained entirely within the companion paper [23].
    *   **Required Fix:** Rephrase to make the dependence clear, e.g., "Consistent with the null dipole significance reported in the companion analysis of [23], the minimal ECH framework...".

---
## Summary recommendation

**MAJOR REVISIONS**

The manuscript presents a valuable and thorough theoretical investigation with potentially significant consequences for a class of modified gravity models. The core results are interesting and the author's transparency regarding assumptions is a strength. However, the paper is currently undermined by its heavy reliance on unpublished companion works and a lack of sufficient rigor in the presentation of several key arguments. If the author can make the paper self-contained and substantially bolster the justification for its central claims as detailed above, it could become a strong candidate for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated referee report, incorporating the findings from the second, more detailed review.

***

**Referee Report: PRD Manuscript [Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes...]**

**To the Editor of Physical Review D,**

This manuscript undertakes a systematic investigation into whether minimal Einstein-Cartan-Holst (ECH) gravity can provide a viable mechanism for late-time cosmic acceleration. The author assesses four enumerated channels and argues for their closure based on a combination of amplitude suppression, naturalness arguments, and a catalog of 14 structural constraints. The paper also presents a noteworthy "perturbation-transparency" result, demonstrating that for canonical scalar matter, the Holst sector decouples from scalar and tensor perturbations, rendering its effects invisible to standard cosmological probes like the CMB power spectra and bispectrum.

The scope of the work is ambitious, and the author is laudably transparent about the crucial assumptions underpinning the analysis, particularly the phenomenological nature of the scaling ansatz required to connect bounce-era physics to the present-day dark energy scale. The perturbation-transparency proof is elegant and appears correct, providing a clear statement on the observational signatures (or lack thereof) of minimal ECH in the perturbative regime.

However, the manuscript in its current form has several essential and major flaws that must be addressed before it can be considered for publication in Physical Review D. The most significant issue is its repeated violation of the standalone-reader principle, relying heavily on numerical results and detailed forecasts from unpublished companion papers. Additionally, several key arguments are presented too concisely, or with dimensional inconsistencies, to allow for proper scientific scrutiny.

I recommend **MAJOR REVISIONS**. The core physical arguments are promising, but the paper requires substantial restructuring and correction to meet the standards of the journal.

Below is a detailed list of required revisions.

---

### ESSENTIAL REVISIONS

1.  **P1A-E1: Reliance on Unpublished MCMC Results**
    *   **Section/Page:** Sec. IV, p. 4; Table IV, p. 26.
    *   **Problem:** The paper uses specific cosmological parameter values (e.g., `H₀ = 67.68 ± 1.06`, `ΔN_eff = -0.020 ± 0.169`) that are explicitly stated to be from an "internal MCMC analysis" detailed in an unpublished companion paper [6]. A published paper cannot be based on results that are not peer-reviewed and publicly accessible. The statement that these "should be read as internal-analysis inputs" confirms the problem.
    *   **Required Fix:** All numerical results and conclusions derived from this internal MCMC analysis must be removed. The arguments must be reformulated to be purely structural and independent of these specific values, or they must use values from a citable, published source (e.g., the latest Planck 2018 results, clearly cited as such). The paper's claims must stand on their own merit without recourse to inaccessible companion work.

2.  **P1A-E2: Future Publication Date**
    *   **Section/Page:** p. 1.
    *   **Problem:** The paper is dated "June 13, 2026".
    *   **Required Fix:** The date must be corrected to the date of submission.

### MAJOR REVISIONS

1.  **P1A-M1: Reliance on Companion Paper Forecasts**
    *   **Section/Page:** Abstract, p. 1; Table I, p. 4; Sec. VII, p. 15.
    *   **Problem:** The paper's claims about future falsifiability, particularly the `2.6-5σ` forecast for detecting `f_NL = -35/8` with SPHEREx, are imported from another unpublished companion paper [2]. While referencing a concurrent submission is permissible, the current text presents these forecasts as established facts that are central to the paper's framing.
    *   **Required Fix:** The text must be revised to clearly and consistently frame these as conditional forecasts from a companion paper. For example: "If the forecast presented in the companion work [2] is realized, SPHEREx could test...". The novel contributions of the present manuscript must be clearly delineated from the results of its companions.

2.  **P1A-M2: Confusing Dimensional Analysis of the Parity-Odd Operator**
    *   **Section/Page:** Sec. II C, p. 7.
    *   **Problem:** The main text's discussion of the mass dimension of the parity-odd operator in Eq. (6) is confusing. The operator, as written, has a mass dimension of +1 for the Lagrangian density, not the required +4. While Appendix B clarifies this is a known feature of the phenomenological ansatz, a reader of the main text is left with a confusing and seemingly incorrect dimensional argument.
    *   **Required Fix:** The main text in Section II C must be rewritten for clarity. It should state upfront that the operator is not a standard dimension-4 EFT operator and immediately direct the reader to Appendix B for a full discussion of its dimensional status and the nature of the on-shell scaling ansatz. This is a crucial caveat that must not be buried in an appendix.

3.  **P1A-M3: Insufficient Justification for Structural "Barriers"**
    *   **Section/Page:** Sec. IX, pp. 16-17.
    *   **Problem:** This section presents a catalog of 13 "logically-independent" barriers to the ECH dark-energy mechanism. While this is a potentially valuable contribution, the arguments are presented with extreme brevity, making them impossible to critically assess. For instance, Barrier 12 introduces a GW ceiling with a quadratic scaling, `Ω_GW ∝ (ρ_crit/ρ_Pl)²`, which is presented as an ansatz without derivation. The entire section reads as a list of claims rather than a rigorous demonstration.
    *   **Required Fix:** This section must be substantially expanded. For each barrier, the author must provide a clear, self-contained derivation or a much more detailed physical justification. Alternatively, if these are summaries of existing constraints, they must be clearly attributed with specific citations to the original derivations. Barriers that are new to this work must be proven with the rigor expected of a PRD article, possibly in an appendix if the derivation is lengthy.

4.  **P1A-M4: Unjustified Prefactor in Dilution Formula**
    *   **Section/Page:** Sec. II C 1, p. 8.
    *   **Problem:** The inflationary dilution factor in Eq. (11) includes a term `(T_reh/M_GUT)^(3/2)`. The physical justification for the `3/2` exponent rests on a vague "parity-odd density-of-states factor" and is explicitly labeled a "phenomenological phase-space ansatz". This is a weak link in the quantitative argument that determines the required number of e-folds, `N_tot ≈ 92`.
    *   **Required Fix:** The author must either provide a more rigorous derivation for this factor or, failing that, must explicitly analyze the sensitivity of the paper's conclusions (especially the value of `N_tot` and the structural tension with `f_NL`) to O(1) variations in this prefactor. The current hand-wavy justification is insufficient.

5.  **P1A-M5: Unsupported Forecast Significance Range**
    *   **Section/Page:** Abstract, p. 1; Footnote on p. 4; Footnote on p. 15.
    *   **Problem:** The paper repeatedly quotes a "2.6-5σ" realistic forecast for SPHEREx detection of `f_NL`. However, the numbers provided in the footnotes (`f_NL = -4.375`, `σ(f_NL) ≈ 1.0`) only support a significance of ~4.4σ. The lower bound of 2.6σ is not derived or explained, making the quoted range an unsupported numerical claim.
    *   **Required Fix:** The author must provide a clear derivation for the full `2.6-5σ` range or revise the claim to match the numbers that are actually presented (i.e., ~4.4σ), while still noting its origin in a companion work.

6.  **P1A-M6: Misleading Figure Labeling**
    *   **Section/Page:** Figure 2, p. 6.
    *   **Problem:** Figure 2, which illustrates the energy density hierarchy, incorrectly labels the "Parity-odd vacuum energy" at the bounce as `ρ_vac = M_Pl⁴`. According to the paper's own model (e.g., Eq. B2), this energy scale is suppressed by a factor of `(α/M)M_Pl ~ 10⁻²`, making the actual energy density `~10⁻² M_Pl⁴`. The current label is off by two orders of magnitude and misrepresents the core mechanism.
    *   **Required Fix:** The label in Figure 2 must be corrected to accurately reflect the energy scale of the parity-odd sector, for example, by labeling it `ρ_vac ~ (α/M) M_Pl⁴` or `ρ_vac ~ 10⁻² M_Pl⁴`.

7.  **P1A-M7: Dimensional Inconsistency in One-Loop Operator**
    *   **Section/Page:** Equation (14), p. 12.
    *   **Problem:** The phenomenological one-loop operator in Eq. (14) appears to be dimensionally inconsistent. The Lagrangian density derived from the expression `(1/M_Pl) ∂_μ ϑ_NY J⁵μ` does not have the required mass dimension of +4 under standard field dimension assignments. The text is ambiguous about the dimensionality of the "Nieh-Yan pseudoscalar" `ϑ_NY`.
    *   **Required Fix:** The author must clarify the definition and mass dimension of `ϑ_NY` and ensure that Eq. (14) is dimensionally correct. If it is a non-standard operator, its dimensional properties must be explicitly justified in the main text, not just alluded to.

### MINOR REVISIONS

1.  **P1A-m1: Internal Versioning in Dateline**
    *   **Section/Page:** p. 1.
    *   **Problem:** The dateline includes an internal version number ("v1A.0.68").
    *   **Required Fix:** This should be removed for publication.

2.  **P1A-m2: Redundant Figure**
    *   **Section/Page:** p. 22.
    *   **Problem:** Figure 6 presents the same forecast information as Figure 4, making it largely redundant.
    *   **Required Fix:** The author should consider removing Figure 6 and referring back to Figure 4 in the text.

3.  **P1A-m3: Potentially Confusing Definition of `ρ_Λ`**
    *   **Section/Page:** Sec. II C, p. 7.
    *   **Problem:** The relation `ρ_Λ = Λ_eff M_Pl² = Ξ M_Pl⁴` could be confusing. While correct under the convention `M_Pl = G^{-1/2}`, it conflates the cosmological constant `Λ_eff` with the dimensionless parameter `Ξ`.
    *   **Required Fix:** For clarity, rewrite this as: "The effective cosmological constant `Λ_eff` is related to the vacuum energy density by `ρ_Λ = Λ_eff M_Pl²`. We parameterize this density as `ρ_Λ = Ξ M_Pl⁴`, which defines the dimensionless parameter `Ξ`."

4.  **P1A-m4: Standalone-Reader Issue with Galaxy Spin Result**
    *   **Section/Page:** Sec. III B, p. 10.
    *   **Problem:** The null result for galaxy spin asymmetry is stated as a fact, but the analysis is contained entirely within the companion paper [23].
    *   **Required Fix:** Rephrase to make the dependence clear, e.g., "Consistent with the null dipole significance reported in the companion analysis of [23], the minimal ECH framework...".

---
## Summary recommendation

**MAJOR REVISIONS**

The manuscript presents a valuable and thorough theoretical investigation with potentially significant consequences for a class of modified gravity models. The core results are interesting and the author's transparency regarding assumptions is a strength. However, the paper is currently undermined by its heavy reliance on unpublished companion works, a lack of sufficient rigor in the presentation of several key arguments, and newly identified issues with dimensional consistency and figure accuracy. If the author can make the paper self-contained and substantially bolster the justification for its central claims as detailed above, it could become a strong candidate for publication.