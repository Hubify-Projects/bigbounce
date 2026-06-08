# P2 auto-2026-06-08_1354pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6307 chars)
**Wall time**: 378.7s

---

Referee report on “Cosmic Birefringence from a Planck-Scale Axion-Like Particle: Predictions, Constraints, and LiteBIRD Forecasts”

I reviewed the full 6-page manuscript, including equations, table, figures, captions, and references. Below I list all issues found, classified by severity. For each, I cite the affected section/page, quote or paraphrase the specific problematic text/equation, and state the required fix.

ESSENTIAL

P2-E1 (Sec. 2.1–2.2; pp. 1–2): Inconsistent and unsupported derivation for Δφ/fa and β
- Problem: Eq. (1) states Δφ ≈ fa θi (1 − J0(m/H0)/J0(0)) ≈ fa θi × O(1), with 1 − J0(1) ≈ 0.24 for m/H0 ≈ 1. This implies Δφ/fa ≈ 0.24 θi (O(1)), which inserted into Eq. (2) gives β ≈ (C0/2) × 0.24 θi = O(0.1) rad (several degrees) for C0, θi ≈ 1. Immediately after Eq. (2), however, the text asserts “Δφ/fa ∼ 10−2 … yielding β ≈ 5×10−3 rad ≈ 0.27°.” These two estimates differ by more than an order of magnitude, and the 10−2 scaling is not derived from Eq. (1) or any explicit time integration of the field equation.
- Required fix: Provide a correct and traceable derivation for Δφ between recombination and today for m ~ H0 in a ΛCDM background. Either (i) present the explicit integration of the Klein–Gordon equation through the radiation, matter, and dark-energy eras (analytically if justified, or numerically with stated cosmological parameters), or (ii) replace Eq. (1) with a self-consistent slow-roll or WKB estimate that leads quantitatively to your adopted Δφ/fa value. State which term(s) suppress Δφ/fa to ~10−2 and quantify them. Ensure that the β prediction quoted in the abstract/conclusions follows from the derived Δφ/fa and your coupling normalization (see P2-E2).

P2-E2 (Sec. 2.2; p. 2): Coupling normalization is nonstandard/undefined and dimensionally ambiguous
- Problem: You define gaγ = C0/fa and write β = (gaγ/2) Δφ = (C0/2fa) Δφ, with C0 “from the ABJ anomaly.” In the standard convention for QCD-axion-like couplings, gaγ = (α/2π)(E/N − 1.92)/fa. If you intend a generic ALP coupling gaγ, it is fine to treat gaγ as free, but then C0 is not “the ABJ anomaly coefficient” unless it explicitly absorbs α/2π. Later you introduce “effective photon coupling fphoton × C0 = 1.73 ± 0.44” (Eq. 5) without ever defining fphoton or its units. As written, Eq. (2) and the surrounding text leave the magnitude and dimensional normalization of gaγ/C0 unclear, which directly affects the β prediction.
- Required fix: Clearly state the coupling convention at first use. If gaγ ≡ C0/fa, specify that C0 is an effective dimensionless parameter absorbing the α/2π factor (and any model-dependent E/N), and state whether C0=O(1) means O(10−3) in the QED-normalized convention. Alternatively, adopt the standard gaγ and carry α/2π explicitly. Define “fphoton” precisely (units, relation to fa and gaγ), and re-derive Eq. (5) from your likelihood, including all steps so it is reproducible and dimensionally consistent.

P2-E3 (Sec. 3.4; p. 3; Abstract p. 1): Bayes factor computation inconsistent with stated posterior and priors
- Problem: You claim ln B = 5.17 “via the Savage–Dickey density ratio with a flat prior β ∈ [0°, 1°],” with variations ln B = 4.48 for [0°, 2°] and ln B = 5.86 for [0°, 0.5°]. Using your combined posterior β = 0.242 ± 0.061° (Eq. 4), the Savage–Dickey ratio for a nested null at β=0 with a uniform prior over [0°, 1°] gives B10 = π(0)/p(0|data) = 1 deg−1 / N(0; μ=0.242°, σ=0.061°) = 1 / 0.00249 ≈ 4.02×10^2, i.e., ln B ≈ 5.99, not 5.17. For [0°, 2°], ln B ≈ 5.30; for [0°, 0.5°], ln B ≈ 6.69. Your quoted values are significantly lower and do not follow from Eq. (4).
- Required fix: Recompute the Bayes factors with explicit formulas, units, and the exact posterior used (state whether you used Eq. 4 or a different posterior). Provide the numerical steps and resolve the discrepancy. If a different likelihood/posterior was used for Bayes factors, report it clearly and keep datasets/estimators consistent across sections.

P2-E4 (Abstract p. 1; Sec. 1 p. 1): Mis-citation and dataset mischaracterization
- Problem: The abstract says “βobs = 0.342 ± 0.094° from the Eskilt et al. joint Planck + ACT analysis.” The Eskilt & Komatsu (2022) paper combines WMAP and Planck; the ACT DR6 analysis is a separate work (Diego-Palazuelos & Komatsu, 2025). No “Eskilt et al. joint Planck + ACT” analysis is cited here, and the value 0.342 ± 0.094° corresponds to WMAP+Planck in Eskilt & Komatsu (2022), not a Planck+ACT joint fit.
- Required fix: Correct the abstract and body to accurately attribute βobs = 0.342 ± 0.094° to the WMAP+Planck analysis (Eskilt & Komatsu, 2022), and do not describe it as a Planck+ACT joint analysis. Ensure consistency wherever this value is referenced.

P2-E5 (Sec. 3.2; p. 3): “Effective photon coupling fphoton × C0 = 1.73 ± 0.44” is undefined and not reproducible
- Problem: Eq. (5) introduces “fphoton × C0” with a numerical constraint but no definition or derivation chain from the data. The symbol fphoton never appears elsewhere, and its units are not given. This quantity cannot be traced back to Eq. (2) or the summary-likelihood.
- Required fix: Define fphoton rigorously and show the algebra mapping the measured β to this parameter, including the assumed prior on θi and any cosmological factor entering Δφ. If this result came from the MCMC (Run 2), say so and provide the exact posterior relation. Otherwise remove Eq. (5).

P2-E6 (Sec. 3.1–3.3; pp. 2–3): Primary estimator and double-counting risk; lack of pre-declared estimator
- Problem: You compute a combined β (0.242 ± 0.061°) from Planck NPIPE + ACT assuming independence, but then for the MCMC you switch to “βobs = 0.342 ± 0.094°” from Eskilt & Komatsu (a different estimator/dataset combination). The manuscript does not pre-declare a single primary estimator nor explain why these should be mixed in one analysis stream. This opens the door to double counting or selective reporting.
- Required fix: Pre-declare and use a single primary estimator for parameter inference and model comparison, or present parallel analyses with a clear separation of datasets/estimators, explaining differences and avoiding double counting. If the Bayes factor uses Eq. (4), then MCMC and all downstream constraints should too, unless explicitly justified otherwise.

P2-E7 (Sec. 3.3; Table 1 p. 3): MCMC chain lengths/ESS insufficient for quoted precisions and Bayes factors
- Problem: Accepted samples per run are 720–6,840 with R̂ − 1 < 0.01 claimed. These sample sizes are far too small to robustly estimate posterior tails, derived quantities, or Bayes factors at the quoted precision. Reporting R̂ − 1 without stating the number of chains, warm-up, autocorrelation times, and effective sample sizes per parameter is inadequate. In particular, 720 accepted samples cannot support stable tail probabilities or SD ratios.
- Required fix: Report the number of chains, warm-up length, per-parameter ESS (bulk and tail), and integrated autocorrelation times. Increase chain lengths to at least O(50,000) post-warm samples per run (as you yourself suggest) so that ESS for all reported parameters exceeds ~10,000, and rerun all posterior summaries and Bayes factors. Provide convergence diagnostics beyond R̂ (e.g., rank plots, ESS) in the supplement.

P2-E8 (Sec. 3.4; p. 3): Juxtaposing σ-based “significance” and Bayes factor without explicit non-comparability disclaimer
- Problem: The manuscript presents “3.9σ from zero” and “ln B = 5.17” side-by-side as if they were commensurate evidence summaries, with only “indicative; prior-dependent” as caveat.
- Required fix: At every juxtaposition of σ-based significances and Bayes factors, add an explicit statement that these are not directly comparable metrics because they answer different model-comparison questions and depend on different assumptions (Gaussian tail probability vs. prior-weighted evidence). Present them in separate subsections or add a boxed disclaimer.

P2-E9 (Sec. 3.3; Table 1 p. 3; throughout): Notation inconsistencies for coupling parameters
- Problem: The paper uses C0, C, Caγ, and gaγ inconsistently. Table 1 refers to “ALP (C = 8 fixed)” while Sec. 2.2 uses C0, and Sec. 3.3 uses Caγ with a flat prior [1, 30]. It is unclear whether C, C0, and Caγ are the same quantity or different.
- Required fix: Unify notation. Use a single symbol for the dimensionless photon-coupling coefficient and a single symbol for the dimensional coupling gaγ. Define them once, specify priors and their physical meaning/units, and use consistently across text, equations, figures, and table. Justify the choice “C=8 fixed” with a model reference or remove.

MAJOR

P2-M1 (Sec. 3.2; p. 3): Independence assumption for Planck and ACT constraints not justified
- Problem: You combine Planck NPIPE and ACT DR6 measurements via a product of independent Gaussians. However, the EB-based birefringence extractions can share sky and methodological systematics (e.g., foreground modeling, self-calibration assumptions). No assessment of possible covariance is provided.
- Required fix: Either (i) justify the independence assumption with references and a discussion of possible shared systematics, or (ii) include a correlation coefficient ρ in the combination and present robustness to ρ ∈ [0, 0.5] (or an empirically motivated range). Alternatively, avoid the combined summary and use a single dataset for the main result.

P2-M2 (Sec. 2.1; p. 2): Use of Bessel J0 without derivation or validity domain
- Problem: Eq. (1) introduces a J0(m/H0) dependence without derivation from the background expansion history. The denominator J0(0) is trivially 1, but the origin of a Bessel solution for an evolving FRW H(t) across multiple eras is not shown.
- Required fix: Derive Eq. (1) from the equation of motion in a specified background, state the approximations leading to J0(m/H0), and check its validity across matter and Λ domination. Otherwise, replace with a derivation that matches the cosmological solution actually used for inference.

P2-M3 (Sec. 3.3; p. 3; Fig. 1 p. 4; Fig. 2 p. 5): Inconsistencies between quoted posterior summaries and figure labels
- Problem: Text reports βALP = 0.336 ± 0.107° (Run 1) and βfree = 0.344 ± 0.096° (Run 3). Figure 1 (Run 2) shows “β [deg] = 0.324 ± 0.099” on the 1D panel. Figure 2 overlays three β posteriors, but exact legend-to-curve mapping and numerical values are not fully reconciled with the text.
- Required fix: Ensure every quoted posterior mean/σ in the text matches the plotted values for the corresponding run. Add a figure legend that clearly maps line styles to models, and list the numerical mean and σ in the caption for verification.

P2-M4 (Sec. 3.4; p. 3): Prior choice for Bayes factor is one-sided in β
- Problem: The prior intervals are [0°, x°], excluding negative β. Many birefringence analyses allow β ∈ (−βmax, +βmax). A one-sided prior can bias the Savage–Dickey Bayes factor for the nested β=0 null.
- Required fix: Recompute Bayes factors with a symmetric prior β ∈ [−βmax, +βmax], justify the chosen βmax, and report sensitivity to this choice. If you intend to restrict to β ≥ 0, explain why the physics/estimator excludes negative rotations.

P2-M5 (Sec. 4; p. 3): LiteBIRD forecast uses a single amplitude without uncertainty propagation
- Problem: The 9σ forecast is computed as 0.27/0.03, but the 0.27° “prediction” is not quantified with a model uncertainty that follows from the priors/posterior on (θi, m, gaγ). No systematics component is propagated, despite discussing calibration caveats in the Discussion.
- Required fix: Propagate the prior/posterior uncertainty on model parameters to a predictive distribution for β and then to a forecasted significance distribution for LiteBIRD. Quote the median and credible interval for significance and discuss the impact of plausible systematics (e.g., a floor at ~0.02°–0.03°).

P2-M6 (Abstract p. 1; Sec. 6 p. 5): Overstatement of “no fine-tuning” without coupling normalization clarity
- Problem: Claims of “no fine-tuning” rest on setting C0 and θi to O(1). Without a clear, standard-normalized definition of gaγ (see P2-E2), the naturalness statement is not substantiated.
- Required fix: Either qualify the claim to “for the adopted coupling convention and priors” or provide a mapping to standard gaγ units (GeV−1) and show that the required gaγ is within well-motivated ranges given existing constraints.

MINOR

P2-m1 (Sec. 3.2; Eq. 3 p. 3): Units and normalization in the Gaussian likelihood
- Problem: The likelihood L(β) is written in continuous form but β is in degrees. This is fine if consistent, but it should be stated explicitly to avoid unit errors, especially when used for the Savage–Dickey ratio.
- Required fix: State explicitly that β is in degrees throughout Sec. 3, and that all Gaussian densities are computed in degree units.

P2-m2 (Sec. 3.3; p. 3): Priors not fully justified
- Problem: θi prior is flat on [0.01, π], excluding β=0-compatible θi=0 and over-weighting large angles; Caγ prior is flat on [1, 30] (units unclear).
- Required fix: Justify these priors physically and test sensitivity (e.g., re-run with θi ∈ [0, π] and with alternative priors). Clarify units for Caγ.

P2-m3 (Sec. 6; p. 5): Mixing of significance statements and qualitative systematics caveats
- Problem: The text alternates between σ-based claims and qualitative caveats without quantifying potential systematic shifts.
- Required fix: Add an explicit bound or estimate for systematic error budgets relevant to current analyses, and show how a representative systematic (e.g., 0.1°) would alter your combined constraint and Bayes factor.

P2-m4 (References; p. 6): “In preparation” citation and arXiv-less entry
- Problem: “Namikawa et al., 2025. In preparation” and “Diego-Palazuelos and Komatsu, 2025. arXiv preprint” lack identifiers. While acceptable for context, they should not be used for load-bearing results.
- Required fix: Provide arXiv numbers if available, or clearly mark them as non-load-bearing context references.

P2-m5 (Typographic/notation nits; multiple pages)
- Problems: Mixed symbols for the same quantities (C vs. C0 vs. Caγ), occasional spacing artifacts (e.g., “β ̸= 0”), and minor ambiguities such as “ϕFF˜”.
- Required fix: Standardize symbols and typography. Define all symbols upon first use and ensure consistent use in figures, table, and equations.

NITS

P2-n1 (Sec. 2; p. 2): “J0(0)” in denominator
- Problem: Writing J0(0) in the denominator is unnecessary since J0(0)=1.
- Required fix: Simplify Eq. (1) to Δφ ≈ fa θi [1 − J0(m/H0)] if you keep this form.

P2-n2 (Sec. 5; p. 4): Qualitative ECH gravity motivation
- Problem: The aside about the Holst action/Barbero–Immirzi field is fine but not needed for the methods paper and may distract.
- Required fix: Consider moving this motivation to an appendix or trimming to one sentence.

Arithmetic audits and cross-checks performed

- σ-based significances:
  - 0.342/0.094 = 3.64σ (abstract “3.6σ” is consistent).
  - 0.30/0.11 = 2.73σ; 0.215/0.074 = 2.91σ (Sec. 3.1 numbers consistent with text).
  - Combined β = 0.242° with σ = 1/sqrt(1/0.11^2 + 1/0.074^2) ≈ 0.0614°, significance 0.242/0.0614 ≈ 3.97σ (text says 3.9σ; acceptable rounding).
  - Forecast: 0.27/0.03 = 9 (Eq. 10 is correct arithmetically; see P2-M5 regarding uncertainty propagation).
- Bayes factor: With β = 0.242°, σ = 0.061°, Savage–Dickey with a flat prior on [0°, 1°] gives ln B ≈ 5.99 (inconsistent with quoted 5.17; see P2-E3).
- Figure/Table consistency: Table 1 lists small accepted sample sizes; Fig. 1 shows β = 0.324 ± 0.099 for Run 2; text gives different values for Runs 1 and 3. Needs alignment (P2-M3).

Length
- At 6 pages, the manuscript is not too long; however, given the number of methodological clarifications required, adding a brief appendix with the Δφ derivation and MCMC diagnostics would be appropriate.

## Summary recommendation
MAJOR REVISIONS

The core results are potentially interesting, but several essential methodological issues must be corrected before PRD can consider publication. Chief among them are the inconsistent and unsupported Δφ/fa derivation leading to the β prediction, the ambiguous coupling normalization, the numerically inconsistent Bayes factor, mixing of estimators without a pre-declared primary analysis, and insufficient MCMC sampling. Addressing these will require substantial revisions, additional derivations, clearer definitions, and reruns of the inference with adequate chain lengths and properly documented diagnostics.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS AFTER SECOND-PASS AUDIT

ESSENTIAL

P2-E10 (Sec. 3.3 text vs. Fig. 1; pp. 3–4): Arithmetic inconsistency for Caγ × θi
- Problem: The text states “Caγ × θi = 3.4 ± 1.1” (Run 2), but Fig. 1’s 1D marginals display roughly θi ≈ 1.33 and Caγ ≈ 13.4, whose product is ≈ 17.8, not 3.4. This cannot be reconciled without a hidden rescaling or redefinition of Caγ in the product.
- Required fix: Define precisely what quantity is plotted in Fig. 1 as “Caγ” and what is multiplied by θi in Eq. (8). If the “product” actually includes normalization factors (e.g., α/2π, 1/2, or fa/MPl), write the full expression and units. Update either the text or the figure so that the displayed posteriors numerically reproduce the quoted product mean and uncertainty.

P2-E11 (Sec. 3.4; p. 3): Savage–Dickey at a boundary point (β = 0 with one-sided prior) is not valid as stated
- Problem: You compute Bayes factors using the Savage–Dickey density ratio with a one-sided uniform prior β ∈ [0°, βmax]. In that case, the null value β = 0 lies on the boundary of the prior support. The standard Savage–Dickey identity assumes the null value is in the interior of the prior support; at a boundary, the identity generally does not hold without correction.
- Required fix: Recompute evidences using a symmetric prior β ∈ [−βmax, +βmax] (see also your P2-M4), or use a method valid at boundaries (e.g., thermodynamic integration, bridge sampling, or nested sampling). State the method explicitly and provide numeric steps so the results are reproducible.

MAJOR

P2-M7 (Sec. 3.3; Fig. 1; pp. 3–4): Posterior mass scale inconsistent with “m ∼ H0” claim; quantify and discuss
- Problem: Fig. 1 indicates log10(m/eV) ≈ −31.4. With H0 ≈ 1.5 × 10−33 eV (log10 H0 ≈ −32.82), this corresponds to m/H0 ≈ 10^(−31.4 + 32.82) ≈ 26–28, i.e., m ≫ H0 by more than an order of magnitude. This contradicts the repeated “m ∼ H0” narrative and affects when the field starts rolling (z at onset).
- Required fix: Quantify m/H0 from your posterior, show the implied z at which H(z) = m in ΛCDM, and reconcile with the repeated “m ∼ H0” assumption that underpins the Δφ estimate. If your inference prefers m ≫ H0, discuss implications for Δφ and β.

P2-M8 (Sec. 2.1; p. 1–2): Onset-of-rolling redshift zroll not derived; m–z mapping missing
- Problem: The text asserts “begins rolling at z ∼ O(1) when H(z) ∼ m” but provides no mapping from m/H0 to z in ΛCDM. For example, to have z ≈ 1 requires m/H0 ≈ √(Ωm(1+z)^3 + ΩΛ) ≈ 1.8 for Planck ΛCDM; m ≈ H0 instead implies z ≈ 0.
- Required fix: Provide the formula zroll(m/H0) in ΛCDM and use it consistently in your Δφ computation/forecast. Update the narrative so it reflects the actual posterior-preferred m/H0 and the corresponding zroll.

P2-M9 (Fig. 2 vs. Table 1/Run labels; p. 5 vs. p. 3): Legend-to-run mapping inconsistent
- Problem: Table 1 names Run 1 = “ALP (C=8 fixed)”, Run 2 = “ALP (C free)”, Run 3 = “β free”, whereas the Fig. 2 legend refers to “Model 2: ALP (C=8)”, “Model 2b: ALP (C free)”, and “Model 0: beta free.” This mismatches the run numbering and risks misinterpretation.
- Required fix: Use a single, consistent run/label mapping across Table 1, text, and figures. Include the numerical posterior means/σ for each curve in the Fig. 2 caption to prevent ambiguity.

P2-M10 (Sec. 2.2, Sec. 3.3, Table 1; pp. 2–3): Fixed C = 8 assumption numerically conflicts with “C0 ∼ 1” naturalness claims
- Problem: The body repeatedly invokes “C0 ∼ O(1)” naturalness, but Table 1 and Fig. 2 employ a fixed “C = 8” in one run. This introduces an implicit factor-of-8 change in β for the same Δφ/fa, materially affecting your “no fine-tuning” narrative.
- Required fix: Either justify C = 8 from a concrete UV model with proper normalization (and discuss how “O(1)” maps to “8” in that convention), or remove C = 8 from the mainline analysis. In all cases, align the coupling normalization with a consistent convention (see also P2-E2 from the first report) and propagate it through figures and text.

MINOR

P2-m6 (Sec. 2.1; p. 2): Misleading statement about 1 − J0(1) “depending on cosmological integration”
- Problem: You write “For m/H0 ∼ 1, 1 − J0(1) ≈ 0.24; the precise value depends on the cosmological integration through the matter and dark-energy eras.” The value 1 − J0(1) is fixed; dependence on expansion history would enter through m/H0(t) or an explicit time integral, not through J0(1) itself.
- Required fix: Clarify that variation arises from m/H0 and the full time integration, not from the numerical value J0(1) per se. Better: replace the heuristic J0 form with the actual ΛCDM time integral (see also P2-M2 from the first report).

P2-m7 (Units across sections; Eq. 2 vs. Sec. 3): Radians vs. degrees not signposted
- Problem: Eq. (2) presents β in radians, while the likelihood and posterior sections use degrees. The unit switch is not explicitly called out near the transition, increasing the risk of silent unit mistakes (potentially relevant to your Bayes factor discrepancy).
- Required fix: State explicitly where β is in radians and where it is in degrees; add a one-line reminder before using degree-based likelihoods and in Sec. 3.4’s Bayes-factor computation.

P2-m8 (Sec. 6; p. 5): Minor conceptual imprecision describing the Minami–Komatsu method
- Problem: You state the method “depends on the instrumental polarization angles being constant across the focal plane.” The method fits per-detector miscalibration angles; it requires stable, characterizable angles, not that they be identical across the focal plane.
- Required fix: Rephrase to reflect that per-detector angles are fitted jointly with β under specified foreground and systematics models; remove the “constant across the focal plane” phrasing.

EXPLANATION

These findings are new relative to the initial report. They focus on second-pass checks that often surface late-stage issues: arithmetic consistency between plotted marginals and quoted products (P2-E10), boundary-violation in the Bayes-factor method (P2-E11), mass-scale consistency with the narrative and its cosmological implications (P2-M7, P2-M8), figure/run labeling mismatches (P2-M9), and a numeric inconsistency in the coupling naturalness storyline (P2-M10), plus several unit/concept clarifications (P2-m6–m8).