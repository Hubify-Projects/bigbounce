# P1A RC-INT — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1a_ech_nogo.pdf` md5=94ce8f5c pages=32
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (11263 chars)
**Wall time**: 169.7s

---

**Referee Report on "Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"**

This manuscript investigates the possibility of sourcing late-time dark energy from minimal Einstein-Cartan-Holst (ECH) gravity. It presents two main sets of results: (1) a "channel-level closure" of four enumerated routes by which ECH could generate dark energy, based on a catalog of 14 constraints; and (2) a "perturbation-transparency" theorem for canonical scalar matter in ECH, showing that the Holst sector decouples from scalar and tensor perturbations.

The perturbation-transparency result is a clear, rigorous, and useful contribution to the literature. The derivation is sound and clarifies the conditions under which ECH phenomenology is identical to General Relativity at the perturbative level.

However, the main thrust of the paper—the closure of the dark-energy routes—is built on a foundation that does not meet the standards of a first-principles theoretical argument. The authors are commendably transparent that their dark-energy mapping relies on a "phenomenological on-shell scaling ansatz" which is not derived from a controlled effective field theory. While the subsequent analysis of amplitude suppression and naturalness within this framework is detailed, the conditional nature of the entire exercise significantly lessens its impact. It is more an exploration of a specific phenomenological model's failures than a general no-go theorem.

Furthermore, the paper's argument relies critically on numerous companion papers that are either "in preparation" or "posted concurrently," making a complete and independent verification of all supporting claims impossible for a referee. While the authors attempt to wall off the core logical claims as self-contained, the frequent citation of these external works for numerical values, forecasts, and data analysis pipelines blurs this line.

The manuscript is also excessively long (32 pages) for its primary, rigorously-established contribution. The 14-barrier catalog, while systematic, contains many arguments that are either standard naturalness considerations or heuristic in nature, and it inflates the paper's length without adding commensurate rigor.

For these reasons, the manuscript requires major revisions before it can be considered for publication in Physical Review D. The authors should restructure the paper to foreground the rigorous perturbation-transparency result and clearly demarcate it from the more speculative, ansatz-dependent analysis of the dark-energy channels.

## Detailed Findings

### ESSENTIAL

**P1A-E1: Foundational Ansatz.** (Sec I.a, p.3; Sec IV, p.11; Appendix B, p.25)
*   **Problem:** The central claim of closing dark-energy routes rests on a "phenomenological on-shell scaling ansatz" (Eq. B2) that connects a dimensionally-improper operator (Eq. 6, with mass dimension +1) to the dark energy density. The authors explicitly and correctly state this is "not a controlled EFT result" and "not a derivation." This foundational weakness undermines the entire dark-energy "closure" argument. As it stands, the paper does not *prove* a closure but rather demonstrates that a particular, non-rigorous phenomenological model is highly constrained.
*   **Fix:** The paper must be fundamentally restructured. The abstract, introduction, and conclusions must be rewritten to reflect that the dark-energy analysis is an exploration of a specific phenomenological model, not a general no-go result for ECH. The title itself is arguably too strong. The rigorous, unconditional perturbation-transparency theorem should be presented as the primary result of the paper.

**P1A-E2: Reliance on Unavailable Companion Papers.** (Throughout, e.g., Sec I.b, p.3; Sec IV, p.4; Table II, p.7)
*   **Problem:** The paper is not self-contained. It repeatedly cites companion papers ([2], [6], [23], [46]) that are "in preparation" or "posted concurrently" for crucial context and numerical values, including MCMC results, Fisher forecasts, and data analysis validation. While presented as "illustrative," these values are used to frame the entire observational context of the work (e.g., the viability of the "surviving" predictions). A paper submitted to PRD must be reviewable on its own merits.
*   **Fix:** All arguments must be made self-contained. Any result, value, or method imported from a companion paper must be derived or explained in sufficient detail within this manuscript (perhaps in appendices) for a referee to verify it. Placeholder citations to "in preparation" works for load-bearing claims are unacceptable. The authors must either incorporate the necessary material or remove the claims that depend on it.

**P1A-E3: Juxtaposition of Significance Values.** (Abstract, p.1; Sec XV, p.24)
*   **Problem:** The abstract and conclusions quote several significance values for cosmic birefringence (e.g., ~3.6σ from Minami & Komatsu, ~2.9σ from Diego-Palazuelos & Komatsu) and for the SPHEREx fNL forecast (2.6-5σ). While the abstract contains a parenthetical clause that these are "not directly comparable," this is insufficient. Such comparisons can be easily misinterpreted. The conclusion (p. 24) computes a ~0.73σ "model-discrimination test" significance for LiteBIRD vs. Planck, which is good, but this level of care should be applied everywhere.
*   **Fix:** At *every* point where sigma values derived from different experiments, datasets, or null hypotheses are presented together, a clear and explicit statement must be included in the main text (not just a brief parenthetical) explaining why they are not directly comparable and what the valid comparison is (if any).

### MAJOR

**P1A-M1: Paper Length and Structure.** (Whole paper)
*   **Problem:** At 32 pages, the paper is unjustifiably long for its core, rigorous results. The 14-barrier catalog (Sec. IX) is a primary contributor to the length, but many of these "barriers" are qualitative, heuristic, or standard naturalness arguments that do not require such extensive cataloging. The truly novel results are the transparency theorem and the specific application of the thermal-reset argument.
*   **Fix:** The paper should be significantly shortened and restructured. I recommend a maximum length of 15-18 pages.
    1.  Create a new, concise section presenting the Perturbation-Transparency Theorem and its proof as the main result.
    2.  Condense the analysis of the four dark-energy routes into a single, brief section that clearly states the foundational ansatz and then summarizes the resulting constraints (amplitude, thermal washout, naturalness) without the lengthy 14-barrier formalism.
    3.  Move detailed derivations of secondary points and the full barrier list (if deemed essential) to appendices.
    4.  Remove redundant figures (e.g., Fig. 7 is a near-duplicate of Fig. 4).

**P1A-M2: Uncomputed Quantitative Claims.** (e.g., Sec II.C.1, p.9)
*   **Problem:** The paper makes several strong claims about physical processes without providing the corresponding calculation. For example, the crucial "Reheating thermal-reset barrier" argument (p. 9) rests on the inequality Γ_wash(T_reh) > H(T_reh). While the argument is physically plausible, the paper states that a "full Boltzmann calculation... is left to a follow-up" and that the condition is an assumption, not a result of the present analysis.
*   **Fix:** For every such physical argument, the authors must either provide an order-of-magnitude calculation within the paper to substantiate the claim or explicitly label it as a working assumption in the abstract and conclusions. Simply stating the inequality and deferring the calculation is insufficient for a load-bearing argument.

### MINOR

**P1A-N1: Inconsistent H0 Value.** (Fig 3 caption, p.29 vs Table V, p.26)
*   **Problem:** The caption of Figure 3 uses a benchmark value of H0 = 69.2 km/s/Mpc for the "spin-torsion" model. However, the main parameter table (Table V) and the companion paper analysis (Table II) report the adopted value as H0 = 67.68 ± 1.06 km/s/Mpc. The caption explains this is a "deliberately high illustrative value," but this creates confusion.
*   **Fix:** Use the paper's consistently adopted MCMC-derived value for H0 in the figure to avoid confusion, or make the caption's explanation much more prominent. The current approach makes the ~2-3% deviation in the plot seem more significant than it is.

**P1A-N2: Redundant Figures.** (Fig 4, p.30 and Fig 7, p.32)
*   **Problem:** Figure 7 ("Detection Significance Forecast") is a simplified version of Figure 4 ("Observational Detection Timeline") and presents the same forecast data for the uncorrelated (ρ=0) case. It is redundant.
*   **Fix:** Remove Figure 7 and refer only to Figure 4.

**P1A-N3: Calculation of fNL Significance.** (Abstract, p.1; Footnote 6, p.16)
*   **Problem:** The abstract quotes a "2.6-5σ" realistic significance for the SPHEREx fNL forecast. Footnote 6 on page 16 explains this range comes from two regimes, one with σ(fNL) ≈ 0.7 (ideal) and one with σ(fNL) ≈ 1.0 (degraded). For fNL = -35/8 = -4.375, these give significances of -4.375/0.7 ≈ 6.25σ and -4.375/1.0 ≈ 4.38σ. The footnote mentions a template-overlap correction r ≈ 0.84, which would reduce the 6.25σ to ~5.25σ. This accounts for the upper end of the range. It is unclear how the lower end of 2.6σ is derived.
*   **Fix:** The footnote must provide a clear, step-by-step calculation for how both the 2.6σ and 5σ values are obtained from the raw sensitivity numbers.

### NIT

**P1A-T1: Futuristic Date.** (p.1)
*   **Problem:** The date on the paper is "June 29, 2026".
*   **Fix:** Replace with the current submission date.

**P1A-T2: Typo in fNL value.** (Table V, p.26)
*   **Problem:** Table V lists "fNL = -35/8 = -4.375". The value is correct, but the second equals sign should be an approximation sign (≈) or the precision should be increased, as the fraction is exact. A minor point, but precision is key.
*   **Fix:** Change to "-35/8 = -4.375". (Correction: -35/8 is exactly -4.375. The formatting is fine. Retracting this nit.)

## Summary recommendation

**MAJOR REVISIONS**

The manuscript in its current form is not acceptable for publication in Physical Review D. It combines a rigorous, valuable result (the perturbation-transparency theorem) with a much longer, speculative analysis based on an underived phenomenological ansatz. The paper's length is excessive, and its reliance on unavailable companion works makes it impossible to fully vet. I recommend that the authors perform a major revision to (1) restructure the paper to clearly separate the rigorous theorem from the conditional model exploration, (2) significantly shorten the manuscript by condensing the barrier-catalog formalism, and (3) make the paper fully self-contained by incorporating all necessary derivations and methods from the companion papers. If these substantial changes are made, the revised manuscript may be suitable for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated review, incorporating the findings from the second, more detailed pass.

================================================================
**Referee Report on "Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"**

This manuscript investigates the possibility of sourcing late-time dark energy from minimal Einstein-Cartan-Holst (ECH) gravity. It presents two main sets of results: (1) a "channel-level closure" of four enumerated routes by which ECH could generate dark energy, based on a catalog of 14 constraints; and (2) a "perturbation-transparency" theorem for canonical scalar matter in ECH, showing that the Holst sector decouples from scalar and tensor perturbations.

The perturbation-transparency result is a clear, rigorous, and useful contribution to the literature. The derivation is sound and clarifies the conditions under which ECH phenomenology is identical to General Relativity at the perturbative level.

However, the main thrust of the paper—the closure of the dark-energy routes—is built on a foundation that does not meet the standards of a first-principles theoretical argument. The authors are commendably transparent that their dark-energy mapping relies on a "phenomenological on-shell scaling ansatz" which is not derived from a controlled effective field theory. While the subsequent analysis of amplitude suppression and naturalness within this framework is detailed, the conditional nature of the entire exercise significantly lessens its impact. It is more an exploration of a specific phenomenological model's failures than a general no-go theorem.

Furthermore, the paper's argument relies critically on numerous companion papers that are either "in preparation" or "posted concurrently," making a complete and independent verification of all supporting claims impossible for a referee. While the authors attempt to wall off the core logical claims as self-contained, the frequent citation of these external works for numerical values, forecasts, and data analysis pipelines blurs this line.

The manuscript is also excessively long (32 pages) for its primary, rigorously-established contribution. The 14-barrier catalog, while systematic, contains many arguments that are either standard naturalness considerations or heuristic in nature, and it inflates the paper's length without adding commensurate rigor.

For these reasons, the manuscript requires major revisions before it can be considered for publication in Physical Review D. The authors should restructure the paper to foreground the rigorous perturbation-transparency result and clearly demarcate it from the more speculative, ansatz-dependent analysis of the dark-energy channels.

## Detailed Findings

### ESSENTIAL

**P1A-E1: Foundational Ansatz.** (Sec I.a, p.3; Sec IV, p.11; Appendix B, p.25)
*   **Problem:** The central claim of closing dark-energy routes rests on a "phenomenological on-shell scaling ansatz" (Eq. B2) that connects a dimensionally-improper operator (Eq. 6, with mass dimension +1) to the dark energy density. The authors explicitly and correctly state this is "not a controlled EFT result" and "not a derivation." This foundational weakness undermines the entire dark-energy "closure" argument. As it stands, the paper does not *prove* a closure but rather demonstrates that a particular, non-rigorous phenomenological model is highly constrained.
*   **Fix:** The paper must be fundamentally restructured. The abstract, introduction, and conclusions must be rewritten to reflect that the dark-energy analysis is an exploration of a specific phenomenological model, not a general no-go result for ECH. The title itself is arguably too strong. The rigorous, unconditional perturbation-transparency theorem should be presented as the primary result of the paper.

**P1A-E2: Reliance on Unavailable Companion Papers.** (Throughout, e.g., Sec I.b, p.3; Sec IV, p.4; Table II, p.7)
*   **Problem:** The paper is not self-contained. It repeatedly cites companion papers ([2], [6], [23], [46]) that are "in preparation" or "posted concurrently" for crucial context and numerical values, including MCMC results, Fisher forecasts, and data analysis validation. While presented as "illustrative," these values are used to frame the entire observational context of the work (e.g., the viability of the "surviving" predictions). A paper submitted to PRD must be reviewable on its own merits.
*   **Fix:** All arguments must be made self-contained. Any result, value, or method imported from a companion paper must be derived or explained in sufficient detail within this manuscript (perhaps in appendices) for a referee to verify it. Placeholder citations to "in preparation" works for load-bearing claims are unacceptable. The authors must either incorporate the necessary material or remove the claims that depend on it.

**P1A-E3: Juxtaposition of Significance Values.** (Abstract, p.1; Sec XV, p.24)
*   **Problem:** The abstract and conclusions quote several significance values (e.g., ~3.6σ, ~2.9σ, 2.6-5σ) derived from different experiments, datasets, and null hypotheses. While the abstract contains a brief parenthetical disclaimer and the body text is often careful to qualify these comparisons (e.g., on p.14), juxtaposing them so closely in the abstract risks misinterpretation by readers who do not study the full text. The careful calculation of the ~0.73σ "model-discrimination test" significance for LiteBIRD vs. Planck (p. 24) is an example of the clarity that should be applied everywhere.
*   **Fix:** Ensure that at *every* point of comparison, especially in the abstract, the context is made clear. For instance, instead of just "not directly comparable," briefly state *why* (e.g., "derived against different nulls (zero vs. ΛCDM)").

### MAJOR

**P1A-M1: Paper Length and Structure.** (Whole paper)
*   **Problem:** At 32 pages, the paper is unjustifiably long for its core, rigorous results. The 14-barrier catalog (Sec. IX) is a primary contributor to the length, but many of these "barriers" are qualitative, heuristic, or standard naturalness arguments that do not require such extensive cataloging. The truly novel results are the transparency theorem and the specific application of the thermal-reset argument.
*   **Fix:** The paper should be significantly shortened and restructured. I recommend a maximum length of 15-18 pages.
    1.  Create a new, concise section presenting the Perturbation-Transparency Theorem and its proof as the main result.
    2.  Condense the analysis of the four dark-energy routes into a single, brief section that clearly states the foundational ansatz and then summarizes the resulting constraints (amplitude, thermal washout, naturalness) without the lengthy 14-barrier formalism.
    3.  Move detailed derivations of secondary points and the full barrier list (if deemed essential) to appendices.
    4.  Remove redundant figures (e.g., Fig. 7 is a near-duplicate of Fig. 4).

**P1A-M2: Uncomputed Quantitative Claims.** (e.g., Sec II.C.1, p.9)
*   **Problem:** The paper makes several strong claims about physical processes without providing the corresponding calculation. For example, the crucial "Reheating thermal-reset barrier" argument (p. 9) rests on the inequality Γ_wash(T_reh) > H(T_reh). While the argument is physically plausible, the paper states that a "full Boltzmann calculation... is left to a follow-up" and that the condition is an assumption, not a result of the present analysis.
*   **Fix:** For every such physical argument, the authors must either provide an order-of-magnitude calculation within the paper to substantiate the claim or explicitly label it as a working assumption in the abstract and conclusions. Simply stating the inequality and deferring the calculation is insufficient for a load-bearing argument.

**P1A-M3: Incorrect Cross-Reference.** (p.11)
*   **Problem:** On page 11, the first sentence of Sec. IV states, "The structural-incompatibility result (Sec. X) is established by ruling out...". However, Section X details the Perturbation-Transparency result. The main "structural tension" argument that pits the dark energy mechanism against the `fNL` prediction is in Section XIV D. The broader set of constraints that constitute the "four-route no-go" are cataloged in Section IX and applied throughout Section IV. The reference to Sec. X is misleading.
*   **Fix:** Correct the cross-reference to point to the appropriate sections (e.g., Sec. IX and Sec. XIV D).

### MINOR

**P1A-N1: Inconsistent H0 Value.** (Fig 3 caption, p.29 vs Table V, p.26)
*   **Problem:** The caption of Figure 3 uses a benchmark value of H0 = 69.2 km/s/Mpc for the "spin-torsion" model. However, the main parameter table (Table V) and the companion paper analysis (Table II) report the adopted value as H0 = 67.68 ± 1.06 km/s/Mpc. The caption explains this is a "deliberately high illustrative value," but this creates confusion.
*   **Fix:** Use the paper's consistently adopted MCMC-derived value for H0 in the figure to avoid confusion, or make the caption's explanation much more prominent. The current approach makes the ~2-3% deviation in the plot seem more significant than it is.

**P1A-N2: Redundant Figures.** (Fig 4, p.30 and Fig 7, p.32)
*   **Problem:** Figure 7 ("Detection Significance Forecast") is a simplified version of Figure 4 ("Observational Detection Timeline") and presents the same forecast data for the uncorrelated (ρ=0) case. It is redundant.
*   **Fix:** Remove Figure 7 and refer only to Figure 4.

**P1A-N3: Calculation of fNL Significance.** (Abstract, p.1; Footnote 6, p.16)
*   **Problem:** The abstract quotes a "2.6-5σ" realistic significance for the SPHEREx fNL forecast. Footnote 6 on page 16 explains the upper end of this range but not the lower end, stating that the full derivation is in a companion paper. This makes the claim unverifiable.
*   **Fix:** The footnote must provide a clear, step-by-step calculation for how both the 2.6σ and 5σ values are obtained from the raw sensitivity numbers, or the range must be removed and replaced with a single, derivable value.

### NIT

**P1A-T1: Futuristic Date.** (p.1)
*   **Problem:** The date on the paper is "June 29, 2026".
*   **Fix:** Replace with the current submission date.

## Summary recommendation

**MAJOR REVISIONS**

The manuscript in its current form is not acceptable for publication in Physical Review D. It combines a rigorous, valuable result (the perturbation-transparency theorem) with a much longer, speculative analysis based on an underived phenomenological ansatz. The paper's length is excessive, and its reliance on unavailable companion works makes it impossible to fully vet. I recommend that the authors perform a major revision to (1) restructure the paper to clearly separate the rigorous theorem from the conditional model exploration, (2) significantly shorten the manuscript by condensing the barrier-catalog formalism, and (3) make the paper fully self-contained by incorporating all necessary derivations and methods from the companion papers. If these substantial changes are made, the revised manuscript may be suitable for publication.