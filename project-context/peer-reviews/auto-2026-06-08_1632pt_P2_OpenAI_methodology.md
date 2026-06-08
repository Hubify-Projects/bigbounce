# P2 auto-2026-06-08_1632pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6126 chars)
**Wall time**: 328.0s

---

Referee report on “Cosmic Birefringence from a Planck-Scale Axion-Like Particle: Predictions, Constraints, and LiteBIRD Forecasts”

Scope of review: methodology rigor (statistics, derivations, dimensional analysis, internal consistency). I read the full manuscript, checked all equations, numbers, figures, and references, and recomputed all quoted significances and ratios.

Overall assessment: The paper contains several foundational methodological inconsistencies and ambiguities that must be resolved for PRD. The most severe issues concern (i) an internally inconsistent and insufficiently justified derivation of the predicted rotation (Eq. 1 vs. subsequent order-of-magnitude estimate), (ii) an ill-posed Bayes-factor calculation that places the null hypothesis at a prior boundary, and (iii) inconsistent use/definition of the photon–axion coupling parameters (C0, C, Caγ, “fphoton × C0”), including unclear normalization with respect to the ABJ anomaly. There is also a mismatch between the Bayes factor quoted in the abstract and the dataset used to compute it, and multiple notation/citation inconsistencies. These rise to the level of essential revisions for PRD standards.

Findings

ESSENTIAL

P2-E1 (Abstract; Sec. 3.4, pp. 1 and 3): Mismatch between quoted Bayes factor and dataset/analysis
- Problem: Abstract states “β = 0.242 ± 0.061° (3.9σ). The Bayes factor … ln B = 5.17.” The combined Gaussian result 0.242 ± 0.061° implies ln B ≈ 5.98 for a flat prior on [0°, 1°]. The quoted ln B = 5.17 matches β = 0.342 ± 0.094° (Eskilt & Komatsu, 2022) or your Run 3 posterior, not the combined result in Sec. 3.2.
- Required fix: State explicitly which posterior is used for the Bayes-factor computation in both the abstract and Sec. 3.4, and recompute ln B consistently for that choice. If you intend the combined Planck+ACT summary-likelihood, replace 5.17 by ≈ 5.98 (for the same prior) or recompute with your chosen prior. If you intend the Run 3/EB-posterior, keep 5.17 but do not juxtapose it with the combined 0.242 ± 0.061° result in the abstract without clarification.

P2-E2 (Sec. 2.1–2.2, pp. 1–2): Inconsistent and insufficient derivation of Δϕ and β prediction
- Problem: Eq. (1) gives Δϕ ≈ fa θi [1 − J0(m/H0)/J0(0)] ≈ 0.24 fa θi for m ≈ H0, which implies Δϕ/fa ≈ 0.24 θi. With Eq. (2), this yields β ≈ (C0/2)(0.24 θi) ≈ 0.12 C0 θi rad, i.e., order 7° for C0 θi ∼ 1—grossly inconsistent with the stated “Δϕ/fa ∼ 10−2” and the claimed β ≈ 0.27°. The Bessel expression is introduced without derivation or citation, and the statement that “the precise value depends on the cosmological integration” contradicts the fixed numerical value of J0(1).
- Required fix: Provide a correct derivation (or a clear literature citation with equations) for Δϕ from recombination to today for m ∼ H0 in a ΛCDM background, starting from φ̈ + 3Hφ̇ + m^2 fa sin(φ/fa) = 0. Show the integral or numerical solution that leads to Δϕ/fa ∼ O(10−2) for θi ∼ O(1). Remove/replace the unjustified Bessel-formula if it is not the correct solution in ΛCDM. Ensure Eq. (1) and Eq. (2) are mutually consistent and yield the quoted β ≈ 0.27° with explicit intermediate steps.

P2-E3 (Sec. 3.2, Eq. 5, p. 2; Abstract): Undefined and dimensionally opaque “fphoton × C0 = 1.73 ± 0.44”
- Problem: The symbol fphoton is never defined. The product “fphoton × C0” is presented as “effective photon coupling,” but its dimensionality and relation to gaγ and fa are unclear, and no calculation pathway from the data to 1.73 ± 0.44 is provided.
- Required fix: Define fphoton precisely (formula and units), relate it unambiguously to gaγ, fa, and Δϕ, and show how Eq. (5) is computed from the likelihood/posterior. If this is a reparameterization, provide the mapping. If it depends on θi and m priors, state that and propagate uncertainties accordingly.

P2-E4 (Sec. 3.4, p. 3): Invalid use of Savage–Dickey ratio with a boundary prior
- Problem: You use a one-sided flat prior β ∈ [0°, 1°] (and variants [0°, 2°], [0°, 0.5°]). The null β = 0 lies at the boundary, violating the regularity conditions for the Savage–Dickey density ratio and biasing the evidence.
- Required fix: Use a proper two-sided prior that contains β = 0 in its interior (e.g., Uniform[−1°, 1°], Gaussian centered at 0, etc.) and recompute ln B. Report the sensitivity to the prior width. If you keep SDDR, justify the regularity conditions; otherwise compute the evidence via nested sampling or another reliable method.

P2-E5 (Abstract p. 1; Conclusion p. 6): Incorrect/inconsistent citation of the “joint Planck + ACT” value
- Problem: You ascribe βobs = 0.342 ± 0.094° to a “joint Planck + ACT analysis by Eskilt et al.” The cited reference is Eskilt & Komatsu (2022), which uses WMAP and Planck, not ACT. Elsewhere you also use ACT DR6 independently.
- Required fix: Correct the wording and attribution in the abstract and conclusion. If a genuine joint Planck+ACT analysis with that value exists, cite it precisely. Otherwise, attribute 0.342 ± 0.094° to WMAP+Planck EB (Eskilt & Komatsu, 2022) and keep ACT separate.

P2-E6 (Sec. 2.2, 3.3, Table 1; throughout): Inconsistent coupling notation and normalization (C0 vs C vs Caγ; missing α/2π factor)
- Problem: gaγ is defined as C0/fa (Sec. 2.2), you later refer to “C = 8 fixed” (Table 1) and “Caγ” with a flat prior (Sec. 3.3), and you also relate C0 to the ABJ anomaly as “order unity.” In standard conventions, L ⊃ −(1/4) gaγ φ F F̃ with gaγ ∝ (α/2π)(C0/fa). Your formulas and priors do not make clear whether α/(2π) is absorbed into C0, into gaγ, or ignored.
- Required fix: Adopt a single, explicit convention for the interaction Lagrangian and for gaγ (include whether α/(2π) multiplies C0). Define all symbols C0, C, Caγ, and their relationships. Align Table 1 and Sec. 3.3 notation with Sec. 2.2. If you choose a purely phenomenological gaγ = C̃/fa, state that C̃ is not the anomaly coefficient and drop the ABJ-anchored “order unity” claim or rescale accordingly.

P2-E7 (Sec. 3.2, p. 2): Independence assumption for Planck and ACT constraints not justified
- Problem: You combine Planck NPIPE and ACT DR6 as independent Gaussians without discussing possible correlations from overlapping sky, analysis choices, or common self-calibration systematics that could induce covariance in β.
- Required fix: Justify the independence assumption quantitatively or introduce a correlation coefficient and propagate it (e.g., via a bivariate Gaussian or a hierarchical model). At minimum, show how the combined result varies for plausible correlations (e.g., ρ = 0, 0.2, 0.5).

P2-E8 (Sec. 3.3, Table 1 and text, p. 3): Inadequate and internally inconsistent MCMC reporting
- Problem: Very small accepted sample sizes (720–6,840) are reported with R̂ − 1 < 0.01 and Neff ∼ 1,000. Neff cannot exceed the total number of posterior draws per parameter. The number of chains and thinning are not stated. Several quoted uncertainties (e.g., Eq. 6–8) are given to three significant digits despite limited sampling.
- Required fix: Report number of chains, total draws per chain, burn-in, thinning, and per-parameter effective sample sizes. Ensure Neff ≤ total posterior draws. Increase sampling to obtain stable tail estimates and Bayes factors (e.g., >50k posterior samples as you suggest) or down-scope claims (e.g., remove Bayes-factor estimates derived from MCMC). Round uncertainties to a precision justified by Neff.

P2-E9 (Sec. 2.2, p. 2): Unsupported “naturalness” numeric estimate leading to β ≈ 0.27°
- Problem: “Δϕ/fa ∼ 10−2 (from the ratio of field displacement to decay constant over the Hubble time)” is asserted without derivation. This is the linchpin for β ≈ 0.27°.
- Required fix: Provide an explicit analytic approximation or a numerical integration (with parameter values) demonstrating Δϕ/fa ≈ few × 10−2 for m ∼ H0, fa ∼ MPl, and θi ∼ O(1). Include the recombination-to-today integral or a plot/table that justifies the 5 × 10−3 rad benchmark for β when C0 θi ∼ 1.

MAJOR

P2-M1 (Fig. 1 vs. Sec. 3.3, p. 4 vs. p. 3): Possible inconsistency between triangle-plot annotations and Eq. (8)
- Problem: Eq. (8) gives Caγ × θi = 3.4 ± 1.1. The diagonal summaries in Fig. 1 appear (from the on-plot numbers) to show marginal means consistent with θi ∼ O(1), but the Caγ summary looks closer to 1.3 or 13 (the figure text is ambiguous at current resolution). If Caγ ≈ 13 and θi ≈ 1.3, the product would be ≫ 3.4.
- Required fix: Ensure the figure’s annotated 1D marginal summaries numerically match the text. If the product quoted in Eq. (8) comes from a derived posterior, show its 1D marginal in the figure or a supplemental figure.

P2-M2 (Table 1, p. 3): Undefined constant “C = 8 fixed”
- Problem: Table 1 lists “ALP (C = 8 fixed)” but C is not defined anywhere. This is critical to interpreting Runs 1–2.
- Required fix: Define C precisely in the theory section, explain its physical origin, and justify the value 8 (and its relation to C0 or Caγ).

P2-M3 (Sec. 3.4, p. 3): Prior choice for β and sign conventions
- Problem: β can be positive or negative. Using a one-sided prior biases parameter inferences and Bayes factors.
- Required fix: Adopt a symmetric prior centered at 0 or explicitly justify a one-sided prior physically. Recompute inferences accordingly.

P2-M4 (Sec. 3.2, p. 2): “Combined constraint is 3.9σ from zero” without noting different null-procedure context elsewhere
- Problem: You present frequentist-like “σ from zero” figures and also a Bayes factor; these are not directly comparable. In some places (Abstract + Sec. 3–4) they appear adjacent without a caveat.
- Required fix: Where both appear, add a brief statement that σ-level and Bayes factor quantify different notions of evidence and are not directly comparable.

P2-M5 (Sec. 6, p. 5): Overreach in “decisive exclusion” claim
- Problem: “If LiteBIRD measures β = 0 ± 0.03°, the ALP explanation is excluded at 9σ.” Zero rotation excludes an ALP explanation of the birefringence signal but does not exclude the ALP model class if θi or gaγ are small within prior support.
- Required fix: Rephrase to “would exclude the O(1) θi, O(1) C0 prediction for this model at 9σ, and disfavor the ALP explanation of the current birefringence hints.”

P2-M6 (Refs., p. 6): “In preparation” references and incomplete citation
- Problem: “Namikawa et al., 2025. In preparation.” and “Diego-Palazuelos and Komatsu, 2025. arXiv preprint” lack arXiv identifiers and should not be used for quantitative comparisons without accessible documentation.
- Required fix: Provide stable arXiv/journal references or remove quantitative claims that rely on unpublished work.

MINOR

P2-m1 (Sec. 2.1, p. 1): J0(0) in denominator
- Problem: Writing J0(m/H0)/J0(0) is gratuitous since J0(0) = 1.
- Required fix: Simplify or remove the ratio; if retained, explain the origin of the Bessel form.

P2-m2 (Fig. 2 caption and Sec. 3.3, pp. 5 and 3): Numerical consistency check
- Problem: Fig. 2 shows β posteriors peaking near 0.33–0.35°, while the combined summary-likelihood is 0.242°. The caption states consistency across all three models and with βobs = 0.342 ± 0.094°. This is true for Run 1/2/3 but not for the combined summary-likelihood in Sec. 3.2.
- Required fix: Clarify in the caption/body that Fig. 2 pertains to the MCMC runs (not the combined summary-likelihood) to avoid confusion.

P2-m3 (Sec. 3.2, p. 2): Independence statement
- Problem: “We use two independent birefringence measurements…” is a strong assertion.
- Required fix: Qualify with “treated as independent; see Sec. 3.2 for discussion of possible correlations.”

NITS

P2-n1 (Sec. 2.2, p. 2): Wording “from the ratio of field displacement to decay constant over the Hubble time”
- Fix: Replace with precise equations/derivation (addressed by P2-E9).

P2-n2 (Acknowledgments, p. 6): “consumer hardware” and “AI research assistants”
- Fix: Optional to remove; not relevant for PRD scientific content.

P2-n3 (Typographic): Mixed use of “birefringence rotation angle” and “rotation angle”
- Fix: Standardize terminology.

Arithmetic checks performed

- Combined β from Planck NPIPE (0.30 ± 0.11°) and ACT DR6 (0.215 ± 0.074°): β = 0.2415 ± 0.0614°, significance 3.93σ. Your 0.242 ± 0.061° (3.9σ) is correct.
- Individual significances: 0.30/0.11 = 2.73σ; 0.215/0.074 = 2.91σ. Stated values are consistent.
- “3.6σ” for 0.342 ± 0.094°: 0.342/0.094 = 3.64σ. OK.
- LiteBIRD forecast: 0.27/0.03 = 9.0σ. OK.
- Bayes factor using β = 0.342 ± 0.094° and Uniform[0°, 1°]: SDDR ln B ≈ 5.18 (matches your 5.17). Using the combined 0.242 ± 0.061° would give ln B ≈ 5.98 for the same prior.

Dimensional/notation checks

- Interaction normalization: Please resolve whether gaγ = C0/fa or gaγ = (α/2π)(C0/fa) is used. Current text suggests the former while invoking ABJ anomaly for C0 “order unity,” which is inconsistent with standard axion-photon coupling conventions unless α/(2π) is absorbed elsewhere.

Length and scope

- The paper is concise (6 pages). However, the core “prediction” needs an explicit derivation or a clear, correct citation with equations. Consider adding 0.5–1 page for the derivation and a short appendix or figure with the numerical evolution check.

Summary recommendation
MAJOR REVISIONS

Rationale: The manuscript contains multiple essential methodological issues: an internally inconsistent and weakly justified prediction for Δϕ/fa and β; an invalid Bayes-factor computation using a boundary prior; inconsistent and undefined coupling notations/normalizations; and a mismatch between the quoted Bayes factor and the dataset used. These must be corrected for PRD. With a rigorous derivation (or proper citation) of Δϕ, a consistent statistical treatment, unified notation, and corrected citations, the paper could meet PRD standards.

---

## PASS 2 — self-critique findings (what initial review missed)

Additional findings (fresh-eye pass)

ESSENTIAL

P2-E10 (Sec. 3.4; Abstract): Bayes-factor scaling with prior width is internally inconsistent
- Problem: You report ln B = 5.17 for β ∼ Uniform[0°,1°], ln B = 4.48 for [0°,2°], and ln B = 5.86 for [0°,0.5°]. For SDDR with a flat prior on β (even if one-sided), ln B should change as +ln w when the prior width w increases: doubling w should increase ln B by ln 2 ≈ 0.693. Your numbers show the opposite trend for [0°,2°] (they decrease by ≈ 0.69) and the same erroneous sign for [0°,0.5°] (they increase by ≈ 0.69 when w halves).
- Required fix: Identify and correct the sign/normalization mistake in the evidence calculation. If you are quoting ln B for the null vs. alternative (rather than alternative vs. null), state that explicitly and keep the sign consistent throughout. Preferably, avoid boundary priors (see P2-E4 in the initial report) and recompute with a symmetric prior so the expected ln B shift with ln w is unambiguous.

P2-E11 (Intro, p. 1 vs. Sec. 2.2): Inconsistent normalization for the rotation formula
- Problem: The Introduction states β = Δϕ/(2fa). Later (Eq. 2) you use β = (C0/2fa) Δϕ and tie C0 to the ABJ anomaly. These are inequivalent definitions and change all subsequent “order-unity” inferences for the coupling.
- Required fix: Use one consistent interaction convention everywhere. If C0 is included, include it already in the Introduction (and throughout), or explicitly state that the Intro is written for C0 = 1 and restore C0 in later equations by rescaling.

MAJOR

P2-M7 (Sec. 4; Fig. 2 caption; Discussion): Forecast does not specify treatment of absolute angle degeneracy/self-calibration
- Problem: The 9σ LiteBIRD claim assumes the instrument can measure absolute polarization orientation (i.e., does not fully self-calibrate EB to zero). You briefly note “depending on the self-calibration strategy,” but the 9σ number is quoted as if unconditional.
- Required fix: State explicitly which calibration scenario the 0.03° forecast corresponds to, how the Minami–Komatsu approach (or external calibrators) breaks the degeneracy, and include a sensitivity band showing forecasted σ(β) under plausible calibration/systematics assumptions. If self-calibration is applied, make clear that an isotropic β is unobservable.

P2-M8 (Sec. 3.3): One-sided prior on a periodic misalignment angle biases results
- Problem: θi is periodic on [−π, π] (or [0, 2π)), yet you adopt θi ∈ [0.01, π], excluding half of the physically allowed phase space and forcing the sign of β for fixed coupling sign. This interacts with your one-sided β prior and with the “naturalness” interpretation.
- Required fix: Use a symmetric prior over a full 2π range (or justify a restricted physical domain with a model argument), and report the impact on β and Caγ × θi. At minimum, add a robustness check with θi ∈ [−π, π].

P2-M9 (Sec. 2.1, p. 1): Rolling redshift inconsistent with m ≈ H0
- Problem: You state the field “begins rolling at z ∼ O(1) when H(z) ∼ m.” For m ≈ H0 in ΛCDM, H(z = 1)/H0 ≈ 1.9–2.0, so H(z) ≈ m is only satisfied near z ≈ 0, not z ∼ 1.
- Required fix: Correct the statement (e.g., “begins rolling at z ≲ 0.3 for m ≈ H0”) or show the precise zroll(m/H0) relation you use in your numerical evolution.

MINOR

P2-m4 (Sec. 3.3; Fig. 1 caption and panels): Unquantified claim that the Caγ–θi degeneracy “does not affect the birefringence prediction”
- Problem: The caption asserts the degeneracy does not affect β, but no quantitative demonstration is shown (e.g., by plotting the derived β posterior in the same triangle, or by reporting corr(β, Caγ), corr(β, θi)).
- Required fix: Add the 1D posterior for β from Run 2 to Fig. 1 or to the supplement and/or provide correlation coefficients showing that the degeneracy is largely along constant Caγ × θi and leaves β well determined.

P2-m5 (Abstract; Sec. 3.1): Dataset labeling inconsistency
- Problem: The abstract refers to “Planck HFI,” Sec. 3.1 to “Planck NPIPE,” and the citation is Eskilt & Komatsu (2022). Clarify whether the Planck number used is PR4/NPIPE-based EB (as in Eskilt & Komatsu, 2022) and standardize the dataset naming to avoid implying use of a different Planck pipeline.
- Required fix: Use a single descriptor (e.g., “Planck PR4/NPIPE EB (Eskilt & Komatsu 2022)”) consistently in abstract, body, and captions.

P2-m6 (Throughout): Units and conventions for H0 and natural units are not stated
- Problem: You mix particle-physics units (m in eV) with cosmology notation (H0) without stating c = ħ = 1 and the conversion used for H0 in eV.
- Required fix: Add a brief conventions paragraph (e.g., “We use c = ħ = 1; H0 = 1.5 × 10−33 eV for H0 = 67.4 km s−1 Mpc−1”) so that m ∼ H0 is quantitatively well-defined.

P2-m7 (Sec. 3.2): Likelihood vs. posterior language
- Problem: Eq. (3) is labeled as a likelihood, but the combined estimate in Eq. (4) is presented as a posterior summary without specifying a prior. While a flat prior in β is implicit, the wording can confuse readers given the Bayes-factor discussion.
- Required fix: State the prior used (e.g., flat, broad) for producing Eq. (4), or label Eq. (4) explicitly as the inverse-variance–weighted estimator from the Gaussian likelihood.

NITS

P2-n4 (Sec. 1–3): Standardize “Planck+ACT joint” vs. “combined summary-likelihood”
- Fix: Reserve “joint” for analyses that fit both datasets simultaneously in a single pipeline. For your Eq. (4) combination, use “combined (assumed-independent) summary-likelihood” consistently in abstract, text, and captions.

Explanation
These issues were not covered in my initial review. They include a sign/normalization error in the Bayes-factor prior-scaling, an internal inconsistency in the rotation normalization between Intro and theory sections, incomplete specification of the LiteBIRD forecast assumptions, a biased prior choice for a periodic angle, an inaccurate statement about the onset of rolling for m ≈ H0, and several consistency/clarity items around datasets, units, and figure-caption claims. Addressing them will materially improve rigor and reproducibility.