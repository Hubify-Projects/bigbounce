# P1A auto-2026-06-09_1042pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (11642 chars)
**Wall time**: 189.9s

---

**Referee Report on "Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"**

**Manuscript ID:** [Fictional ID]
**Journal:** Physical Review D

This paper presents a systematic assessment of four potential channels through which minimal Einstein-Cartan-Holst (ECH) gravity could source late-time dark energy. The authors conclude that all four enumerated channels fail at the amplitude level under a set of stated assumptions. The central positive result is a "perturbation-transparency theorem," which states that for canonical scalar matter, the Holst sector decouples from scalar and tensor perturbations, rendering it invisible to standard cosmological probes like the CMB power spectra and bispectrum.

The paper contains a valuable and rigorous core result in the perturbation-transparency theorem. The systematic closure of the four routes is also a useful contribution to the literature on ECH cosmology. However, the manuscript in its current form suffers from significant structural problems, a heavy reliance on unpublished companion work, inconsistent presentation of its key quantitative claims, and several unprofessional artifacts. It requires major revisions before it can be considered for publication in Physical Review D.

## Detailed Findings

### ESSENTIAL

**P1A-E1: Incomplete Sentence in Footnote (Page 1)**
*   **Problem:** The footnote `a` on page 1, which continues on page 2, begins "This Bianchi-identity vanishing is distinct from — and should" and is left incomplete.
*   **Fix:** Complete the sentence. This is a critical clarification that is currently missing.

**P1A-E2: Internal Review Artifacts (Page 2, 16)**
*   **Problem:** The manuscript contains language referencing its own revision history, which is inappropriate for a final submission.
    *   Page 2, footnote: "Earlier versions of this manuscript erroneously identified the two; the correction preserves the headline conclusion..."
    *   Page 16, footnote 3: "An earlier version of this manuscript misidentified the Holst dual contraction with the Pontryagin density. The correction..."
*   **Fix:** Remove all such references to "earlier versions" or the paper's own evolution. The manuscript should be presented as a finished, coherent work.

**P1A-E3: Reliance on Unpublished and "Internal" Results (Page 1, 5, etc.)**
*   **Problem:** The paper's quantitative cosmological claims and observational constraints rely almost entirely on companion works that are "in preparation" or on MCMC results described as "documented internally". A published paper must be self-contained and its results verifiable.
    *   Page 1, Abstract: "ACDM+Neff MCMC verification... documented separately in companion work in preparation [6]."
    *   Page 5, "Companion paper": "Cosmological parameter values referenced in this paper... are drawn from the companion internal MCMC analysis... they are documented internally rather than as externally citable arXiv-posted numbers".
    *   This issue affects the `H_0` and `ΔN_eff` values, the `f_NL` forecast, and the galaxy spin null result.
*   **Fix:** All results essential to the paper's arguments must either be derived within the manuscript or cited from a peer-reviewed publication or a public preprint (e.g., on arXiv). Claims based on "internal" or "in preparation" work are not permissible. This may require adding new sections/appendices to this paper or waiting for the companion papers to be publicly available.

### MAJOR

**P1A-M1: Misleading Presentation of the `N_tot ≈ 92` Result (Throughout)**
*   **Problem:** The paper presents the requirement of `N_tot ≈ 92` e-folds as a central result of its dark energy analysis. However, the derivation of this number is based on a non-rigorous, "dimensional-analysis aesthetic" prefactor `(T_reh/M_GUT)^(3/2)` (Sec. VII) and a phenomenological on-shell scaling ansatz (Appendix B). The paper itself admits in Sec. XII.A and Appendix B that this calculation is merely "mathematical scaffolding" and a rough "order-of-magnitude estimate". The abstract and main text, however, present "≈ 92" as a precise, fitted value, which is inconsistent and misleading. The stronger, more physical argument for closure—the "reheating thermal-reset barrier"—is comparatively downplayed.
*   **Fix:** The paper must be restructured. The "reheating thermal-reset barrier" should be presented as the primary, robust thermodynamic argument for the closure of this dark energy channel. The `N_tot` calculation should be demoted to a secondary, illustrative estimate, and its significant theoretical uncertainties must be stated upfront in the abstract and introduction, not just in later sections and an appendix. The precision "≈ 92" should be replaced with an order-of-magnitude statement like `N_tot ~ O(100)` throughout the manuscript to reflect its true uncertainty.

**P1A-M2: Bloated and Repetitive Structure (Sec. IX, etc.)**
*   **Problem:** The paper is excessively repetitive in its caveats (e.g., "channel-level, not operator-level"). The list of "13 logically-independent barriers" in Sec. IX is bloated. Several barriers are either standard problems in cosmology not specific to ECH (e.g., Barrier 6: Attractor-Sensitivity Dilemma), restatements of arguments made elsewhere (e.g., Barrier 8 is part of the Route 1 closure), or philosophical rather than technical (e.g., Barrier 9: Liouville Conservation). This section obscures the paper's core arguments.
*   **Fix:** Drastically condense Sec. IX and Table II. Merge related or redundant barriers and remove those that are not novel or specific to the ECH model being tested. The goal should be a concise summary of the key structural problems, which would improve the paper's readability and impact. The overall page count should be reduced.

**P1A-M3: Unjustified Conclusions on `w_0-w_a` Models (Sec. XI)**
*   **Problem:** In Sec. XI, the authors discuss and dismiss a "hybrid dark-energy loophole" involving late-time dynamical dark energy (CPL `w_0-w_a` models). They state this is a "theoretical-structure conclusion, not a quantitative posterior-preference rejection" because their "MCMC analysis... hosts zero free-w_0w_a samples". It is inappropriate to draw conclusions about a class of models without actually testing them against data.
*   **Fix:** The conclusions of this section must be softened. The authors can state that adding a generic `w_0-w_a` component is not predicted by their ECH framework, but they cannot claim to have assessed or rejected these models without a proper data analysis. The section should be reframed as an observation about the model's lack of predictivity for late-time dynamics.

### MINOR

**P1A-m1: Contradictory Figure Caption (Fig. 1, Page 4)**
*   **Problem:** In Figure 1, the "Ekpyrotic" mechanism is marked with "produces ECH; permitted" but also has a red dashed arrow pointing to a box that says "structurally closed (this paper)". This is contradictory. If the paper closes it, it should not be "permitted".
*   **Fix:** Clarify the status of the Ekpyrotic route in both the figure and the caption. If the paper's arguments apply to and close this route, the "permitted" label should be removed.

**P1A-m2: Incomplete Barrier Argument (Barrier 12, Page 15)**
*   **Problem:** Barrier 12 ("Vacuum Amplification Ceiling") calculates the total energy density in gravitational waves at the bounce, `Ω_GW`, but correctly notes that a quantitative comparison to PTA data requires propagating this signal to the present day. Without this calculation, the "barrier" is just an upper bound and does not function as a constraint.
*   **Fix:** Either perform the required calculation to turn this into a genuine constraint or re-label it as a "potential signature" or "future test" rather than a "barrier".

**P1A-m3: Confusing Statistical Discussion (Sec. XV, Page 20)**
*   **Problem:** The discussion of the spectator-ALP birefringence test in the Conclusions is convoluted. It mixes a naive S/N calculation ("~9σ") with the correct, more subtle model-discrimination test ("≈ 0.73σ") against the existing central value. The presentation makes it difficult for the reader to grasp the key takeaway.
*   **Fix:** Rewrite this paragraph for clarity. State directly that the relevant test is not a simple detection but a measurement of the parameter `β` to distinguish between a null value, the benchmark value (0.27°), and the current experimental central value (~0.34°). Clearly state the expected significance for the relevant hypothesis test.

**P1A-m4: Redundant Figure (Fig. 6, Page 18)**
*   **Problem:** Figure 6 is a near-identical copy of Figure 4, showing the same forecast plots.
*   **Fix:** Remove Figure 6 to avoid redundancy.

### NIT

**P1A-N1: Future Date (Page 1)**
*   **Problem:** The paper is dated "June 9, 2026 PDT".
*   **Fix:** Use the current date of submission.

## Summary recommendation

**MAJOR REVISIONS**

This manuscript presents a valuable "no-go" analysis for a class of ECH dark energy models and introduces an important perturbation-transparency theorem. These core contributions are of interest to the cosmology community. However, the paper is not yet at the standard required for publication in Physical Review D. The misleading emphasis on a poorly-derived quantitative result (`N_tot ≈ 92`), the unacceptable reliance on unverifiable "internal" and "in preparation" companion work, and the presence of unprofessional artifacts are significant flaws. The paper also suffers from a bloated structure that obscures its sharpest arguments. If the authors can substantially restructure the manuscript to address these major issues, a revised version could be a strong candidate for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated referee report, incorporating the findings from the second, more rigorous review.

================================================================
**Referee Report on "Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"**

**Manuscript ID:** [Fictional ID]
**Journal:** Physical Review D

This paper presents a systematic assessment of four potential channels through which minimal Einstein-Cartan-Holst (ECH) gravity could source late-time dark energy. The authors conclude that all four enumerated channels fail at the amplitude level under a set of stated assumptions. The central positive result is a "perturbation-transparency theorem," which states that for canonical scalar matter, the Holst sector decouples from scalar and tensor perturbations, rendering it invisible to standard cosmological probes like the CMB power spectra and bispectrum.

The paper contains a valuable and rigorous core result in the perturbation-transparency theorem. The systematic closure of the four routes is also a useful contribution to the literature on ECH cosmology. However, the manuscript in its current form suffers from significant structural problems, a heavy reliance on unpublished companion work, inconsistent presentation of its key quantitative claims, several technical errors, and some unprofessional artifacts. It requires major revisions before it can be considered for publication in Physical Review D.

## Detailed Findings

### ESSENTIAL

**P1A-E1: Incomplete Sentence in Footnote (Page 1)**
*   **Problem:** The footnote `a` on page 1, which continues on page 2, begins "This Bianchi-identity vanishing is distinct from — and should" and is left incomplete.
*   **Fix:** Complete the sentence. This is a critical clarification that is currently missing.

**P1A-E2: Internal Review Artifacts (Page 2, 16)**
*   **Problem:** The manuscript contains language referencing its own revision history, which is inappropriate for a final submission.
    *   Page 2, footnote: "Earlier versions of this manuscript erroneously identified the two; the correction preserves the headline conclusion..."
    *   Page 16, footnote 3: "An earlier version of this manuscript misidentified the Holst dual contraction with the Pontryagin density. The correction..."
*   **Fix:** Remove all such references to "earlier versions" or the paper's own evolution. The manuscript should be presented as a finished, coherent work.

**P1A-E3: Reliance on Unpublished and "Internal" Results (Page 1, 5, etc.)**
*   **Problem:** The paper's quantitative cosmological claims and observational constraints rely almost entirely on companion works that are "in preparation" or on MCMC results described as "documented internally". A published paper must be self-contained and its results verifiable.
    *   Page 1, Abstract: "ACDM+Neff MCMC verification... documented separately in companion work in preparation [6]."
    *   Page 5, "Companion paper": "Cosmological parameter values referenced in this paper... are drawn from the companion internal MCMC analysis... they are documented internally rather than as externally citable arXiv-posted numbers".
    *   This issue affects the `H_0` and `ΔN_eff` values, the `f_NL` forecast, and the galaxy spin null result.
*   **Fix:** All results essential to the paper's arguments must either be derived within the manuscript or cited from a peer-reviewed publication or a public preprint (e.g., on arXiv). Claims based on "internal" or "in preparation" work are not permissible. This may require adding new sections/appendices to this paper or waiting for the companion papers to be publicly available.

### MAJOR

**P1A-M1: Misleading Presentation of the `N_tot ≈ 92` Result (Throughout)**
*   **Problem:** The paper presents the requirement of `N_tot ≈ 92` e-folds as a central result of its dark energy analysis. However, the derivation of this number is based on a non-rigorous, "dimensional-analysis aesthetic" prefactor `(T_reh/M_GUT)^(3/2)` (Sec. VII) and a phenomenological on-shell scaling ansatz (Appendix B). The paper itself admits in Sec. XII.A and Appendix B that this calculation is merely "mathematical scaffolding" and a rough "order-of-magnitude estimate". The abstract and main text, however, present "≈ 92" as a precise, fitted value, which is inconsistent and misleading. The stronger, more physical argument for closure—the "reheating thermal-reset barrier"—is comparatively downplayed.
*   **Fix:** The paper must be restructured. The "reheating thermal-reset barrier" should be presented as the primary, robust thermodynamic argument for the closure of this dark energy channel. The `N_tot` calculation should be demoted to a secondary, illustrative estimate, and its significant theoretical uncertainties must be stated upfront in the abstract and introduction, not just in later sections and an appendix. The precision "≈ 92" should be replaced with an order-of-magnitude statement like `N_tot ~ O(100)` throughout the manuscript to reflect its true uncertainty.

**P1A-M2: Bloated and Repetitive Structure (Sec. IX, etc.)**
*   **Problem:** The paper is excessively repetitive in its caveats (e.g., "channel-level, not operator-level"). The list of "13 logically-independent barriers" in Sec. IX is bloated. Several barriers are either standard problems in cosmology not specific to ECH (e.g., Barrier 6: Attractor-Sensitivity Dilemma), restatements of arguments made elsewhere (e.g., Barrier 8 is part of the Route 1 closure), or philosophical rather than technical (e.g., Barrier 9: Liouville Conservation). This section obscures the paper's core arguments.
*   **Fix:** Drastically condense Sec. IX and Table II. Merge related or redundant barriers and remove those that are not novel or specific to the ECH model being tested. The goal should be a concise summary of the key structural problems, which would improve the paper's readability and impact. The overall page count should be reduced.

**P1A-M3: Unjustified Conclusions on `w_0-w_a` Models (Sec. XI)**
*   **Problem:** In Sec. XI, the authors discuss and dismiss a "hybrid dark-energy loophole" involving late-time dynamical dark energy (CPL `w_0-w_a` models). They state this is a "theoretical-structure conclusion, not a quantitative posterior-preference rejection" because their "MCMC analysis... hosts zero free-w_0w_a samples". It is inappropriate to draw conclusions about a class of models without actually testing them against data.
*   **Fix:** The conclusions of this section must be softened. The authors can state that adding a generic `w_0-w_a` component is not predicted by their ECH framework, but they cannot claim to have assessed or rejected these models without a proper data analysis. The section should be reframed as an observation about the model's lack of predictivity for late-time dynamics.

**P1A-M4: Dimensional Inconsistency in Key Equation (Page 10)**
*   **Problem:** Equation (17), which gives the birefringence angle `β` for the spectator ALP (Route 4), is dimensionally incorrect. The right-hand side has units of `[mass]⁻¹`, while the angle `β` on the left-hand side must be dimensionless. This appears to be a typo, likely `m_θ` in the denominator instead of `m_θ²`.
*   **Fix:** This is a critical error that undermines the entire quantitative argument for the closure of Route 4. The equation must be corrected. The subsequent numerical calculation, which inverts this equation to connect the observed `β` to a required energy density `ρ_θ`, must be re-derived and verified using the corrected formula.

### MINOR

**P1A-m1: Contradictory Figure Caption (Fig. 1, Page 4)**
*   **Problem:** In Figure 1, the "Ekpyrotic" mechanism is marked with "produces ECH; permitted" but also has a red dashed arrow pointing to a box that says "structurally closed (this paper)". This is contradictory. If the paper closes it, it should not be "permitted".
*   **Fix:** Clarify the status of the Ekpyrotic route in both the figure and the caption. If the paper's arguments apply to and close this route, the "permitted" label should be removed.

**P1A-m2: Incomplete Barrier Argument (Barrier 12, Page 15)**
*   **Problem:** Barrier 12 ("Vacuum Amplification Ceiling") calculates the total energy density in gravitational waves at the bounce, `Ω_GW`, but correctly notes that a quantitative comparison to PTA data requires propagating this signal to the present day. Without this calculation, the "barrier" is just an upper bound and does not function as a constraint.
*   **Fix:** Either perform the required calculation to turn this into a genuine constraint or re-label it as a "potential signature" or "future test" rather than a "barrier".

**P1A-m3: Confusing Statistical Discussion (Sec. XV, Page 20)**
*   **Problem:** The discussion of the spectator-ALP birefringence test in the Conclusions is convoluted. It mixes a naive S/N calculation ("~9σ") with the correct, more subtle model-discrimination test ("≈ 0.73σ") against the existing central value. The presentation makes it difficult for the reader to grasp the key takeaway.
*   **Fix:** Rewrite this paragraph for clarity. State directly that the relevant test is not a simple detection but a measurement of the parameter `β` to distinguish between a null value, the benchmark value (0.27°), and the current experimental central value (~0.34°). Clearly state the expected significance for the relevant hypothesis test.

**P1A-m4: Redundant Figure (Fig. 6, Page 18)**
*   **Problem:** Figure 6 is a near-identical copy of Figure 4, showing the same forecast plots.
*   **Fix:** Remove Figure 6 to avoid redundancy.

**P1A-m5: Incorrect Internal Cross-Reference (Page 1)**
*   **Problem:** The abstract claims missing operators are acknowledged in "Sec. IV and Sec. XI". The reference to Sec. XI is incorrect; the acknowledgment appears only in Sec. IV.
*   **Fix:** Correct the cross-reference.

**P1A-m6: Broken Appendix (Page 21)**
*   **Problem:** Appendix A, "Complete Parameter Summary," is an empty section with only a title. It appears to be a formatting error.
*   **Fix:** Either populate the appendix with the intended summary or remove the section entirely.

**P1A-m7: Minor Dimensional Inconsistency (Page 6)**
*   **Problem:** Equation (10) for `Λ_eff` is dimensionally inconsistent: `[mass]⁴ = [mass]⁴ + [mass]²`. The rotational term `c_ω ω²` is missing a factor with units of `[mass]²` (e.g., `M_Pl²`).
*   **Fix:** Correct the equation, even if the term is argued to be negligible.

### NIT

**P1A-N1: Future Date (Page 1)**
*   **Problem:** The paper is dated "June 9, 2026 PDT".
*   **Fix:** Use the current date of submission.

## Summary recommendation

**MAJOR REVISIONS**

This manuscript presents a valuable "no-go" analysis for a class of ECH dark energy models and introduces an important perturbation-transparency theorem. These core contributions are of interest to the cosmology community. However, the paper is not yet at the standard required for publication in Physical Review D. The misleading emphasis on a poorly-derived quantitative result (`N_tot ≈ 92`), the unacceptable reliance on unverifiable "internal" and "in preparation" companion work, a critical dimensional error in a key equation (Eq. 17), and the presence of unprofessional artifacts are significant flaws. The paper also suffers from a bloated structure that obscures its sharpest arguments. If the authors can substantially restructure the manuscript to address these major issues, a revised version could be a strong candidate for publication.