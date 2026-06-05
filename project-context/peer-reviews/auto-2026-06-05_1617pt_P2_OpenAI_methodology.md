# P2 auto-2026-06-05_1617pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6628 chars)
**Wall time**: 340.1s

---

Referee report on “Cosmic Birefringence from a Planck-Scale Axion-Like Particle: Predictions, Constraints, and LiteBIRD Forecasts” (6 pages)

Scope of review
I evaluated the statistical methodology, derivations, dimensional consistency, internal numerical consistency, and figure/table coherence across all sections, equations, and claims. I recomputed all quoted significances and combinations from the numbers provided.

Overall assessment
The paper aims to connect an ultra-light ALP with fa ~ MPl and m ~ H0 to the isotropic CMB birefringence signal, present a simple likelihood combination of Planck and ACT measurements, run a small MCMC, and offer a LiteBIRD forecast. While the topic is timely, there are foundational methodological and derivational inconsistencies that must be resolved before the paper can meet PRD standards. Chief among these are: an internally inconsistent derivation for Δφ/fa and the predicted rotation β (O(1) vs 10^-2 tension), an undefined/dimensionally ambiguous “effective photon coupling” estimator, inconsistent notation and unexplained choice “C = 8,” and a Bayes-factor computation that does not reproduce from the stated inputs. There is also mixing of σ-levels from different estimators without explicit “not directly comparable” caveats, and independence assumptions for the Planck+ACT combination are unexamined.

Findings

ESSENTIAL

P2-E1 (Sec. 2.1 and 2.2; pp. 2)
Problem: Inconsistent prediction for the field displacement and rotation.
- Eq. (1): “Δϕ ≈ fa θi (1 − J0(m/H0)/J0(0)) ≈ fa θi × O(1). For m/H0 ∼ 1, 1 − J0(1) ≈ 0.24.”
- Eq. (2) and text: “For C0 ∼ 1, θi ∼ 1: the cosmological field evolution gives Δϕ/fa ∼ 10−2 ... yielding β ≈ 5×10−3 rad ≈ 0.27°.”
These statements cannot both be true. If Eq. (1) holds with J0(0) = 1, then Δϕ/fa ≈ 0.24 θi = O(10^-1), which with β = (C0/2)(Δϕ/fa) would imply β = O(10^-1) rad ~ 10° for O(1) inputs, not 0.27°. Conversely, Δϕ/fa ∼ 10^-2 contradicts the O(1) factor in Eq. (1).
Required fix: Provide a consistent, first-principles derivation of Δϕ from recombination to today in a realistic ΛCDM background (clearly stating approximations), and then propagate it to β. If a semi-analytic approximation is used, show the steps and justify them; if a numerical integral is used, provide the setup and result. Remove the contradictory O(1) vs 10^-2 statements. The Bessel-function expression itself requires derivation and validation (see P2-E7).

P2-E2 (Sec. 3.2; p. 2)
Problem: Undefined and dimensionally ambiguous estimator “fphoton × C0 = 1.73 ± 0.44.”
The paper defines gaγ = C0/fa. The quantity “fphoton × C0” is not defined anywhere (is it fa/C0? 1/gaγ? some rescaled unit?), carries dimensions if it involves fa, yet is quoted as a pure number without units. No derivation is provided for the numerical value 1.73 ± 0.44 from the combined β.
Required fix: Explicitly define “fphoton,” state its units, and show the algebra mapping the measured β (and the assumed/derived Δϕ) to this parameter with proper uncertainties. If this quantity depends on Δϕ/fa, then you must first provide the self-consistent Δϕ derivation (P2-E1) and then perform error propagation.

P2-E3 (Sec. 3.4; p. 3)
Problem: Bayes factor ln B values do not reproduce from the stated inputs, and the method is under-specified.
Text: “ln B = 5.17 ... prior β ∈ [0°, 1°]. ln B = 4.48 for β ∈ [0°, 2°] and ln B = 5.86 for β ∈ [0°, 0.5°].”
From Eq. (4), β = 0.242 ± 0.061° (Gaussian). Using Savage–Dickey with a flat prior on [0°, 1°], the prior density at 0° is 1 deg^-1, and the posterior density at 0° is f(0) = [1/(√(2π)σ)] exp(−μ^2/2σ^2) ≈ (1/0.1539)×exp(−7.873) ≈ 0.00247 deg^-1, giving B10 ≈ 405 and ln B ≈ 6.00. For prior widths of 2° and 0.5°, ln B ≈ 5.31 and 6.70, respectively. The paper’s numbers (5.17, 4.48, 5.86) are inconsistent with the given μ and σ.
Required fix: Provide the exact calculation (including units handling, whether σ is in degrees or radians, and whether tails are truncated) and update the reported ln B values. Also state clearly which dataset/likelihood produced the posterior used in SDDR. If the posterior was not exactly Gaussian, show the kernel estimate at β = 0 with uncertainty. If using MCMC-derived posteriors, demonstrate sufficient effective samples in the β ~ 0 tail to make SDDR stable (or avoid SDDR and report likelihood-ratio proxies with caveats).

P2-E4 (Table 1; Sec. 3.3; p. 3)
Problem: Notation/parameter inconsistency and unjustified fixed choice.
- Table 1: “ALP (C = 8 fixed)” but earlier parameters are C0 (gaγ = C0/fa) and then later Caγ with different prior. The symbol “C” is never defined, and the choice “C = 8” is not justified.
Required fix: Use a single, consistently defined symbol for the anomaly/electromagnetic coefficient throughout (e.g., Cγ ≡ C0), define it once, and justify the “C = 8” value if used (with a concrete particle-physics model and references). Otherwise, drop the fixed value and treat it as a parameter with a physically motivated prior centered on O(1).

P2-E5 (Abstract, Sec. 1, Sec. 3.2–3.3; pp. 1–3)
Problem: σ-levels from distinct estimators/procedures are juxtaposed without explicit “not directly comparable” caveats each time.
Examples:
- Abstract: “... consistent with the 3.6σ isotropic birefringence signal (βobs = 0.342 ± 0.094° from the Eskilt et al. joint Planck + ACT analysis). ... finding β = 0.242 ± 0.061° (3.9σ from zero) ...”
- Sec. 3.2 vs 3.3: a summary-likelihood combination (Planck NPIPE+ACT) and a different joint-analysis estimator are both quoted as σ-levels.
Required fix: Each juxtaposition must explicitly state that these significances arise from different estimators/data combinations and are not directly comparable. Ideally, centralize the primary estimator you use for inference in this paper and relegate others to comparison with clear caveats.

P2-E6 (Sec. 2.1; p. 2)
Problem: The Bessel expression for Δϕ involves J0(m/H0) without derivation, and appears to be an ad-hoc stand-in for a time integral through RD/MD/ΛD. As written, it implies Δϕ/fa ~ O(1), which conflicts with later text (see P2-E1). The argument J0(m/H0) suggests a constant-H approximation, which is inappropriate over the recombination-to-today interval.
Required fix: Derive Δϕ robustly from the ALP EOM in an expanding universe (showing the time dependence of H(z)), or provide a controlled approximation with error bounds. Remove or fully justify the Bessel formula; do not present an expression that implies a contradictory scaling.

P2-E7 (Sec. 3.2; p. 2)
Problem: Assumption of independence between “Planck NPIPE” and “ACT DR6” β measurements is untested. While instrumental systematics differ, sky overlap and shared foreground modeling can induce non-zero correlation. The combined 3.9σ relies on independence.
Required fix: Quantify the plausible correlation range (e.g., via overlap fractions and shared foreground model components). Provide a sensitivity analysis: recompute the combined σ for ρ ∈ [0, 0.3]. Report the degradation; if unknown, state that 3.9σ is an upper bound under the independence assumption.

MAJOR

P2-M1 (Sec. 3.3; p. 3; Table 1)
Problem: MCMC methodology under-specified and sample sizes too small for some claims.
- Accepted samples are 720–6,840 per run. R̂ − 1 < 0.01 is quoted but the number of chains, burn-in treatment, thinning, acceptance rates, and autocorrelation times are not given. For Run 3, accepted samples (720) are less than the stated “Neff ∼ 1,000,” which is internally inconsistent.
Required fix: Report the number of chains, total draws per chain, warm-up/burn-in length, acceptance rates, autocorrelation times, and computed effective sample sizes per parameter. Ensure Neff is correctly reported for each run and that any tail/evidence claims are supported by adequate Neff. If not, remove/soften those claims (especially Bayes factors).

P2-M2 (Sec. 3.3; p. 3)
Problem: Priors need physical justification and careful handling of periodicity.
- θi flat on [0.01, π] ignores periodicity and symmetry (θ ~ −θ) of the misalignment angle across [-π, π], and excludes a neighborhood of 0. Caγ flat on [1, 30] is very broad and inconsistent with earlier “order-unity” language. No motivation is provided.
Required fix: Use a prior respecting the periodic nature of θ (e.g., uniform on [−π, π] or appropriate wrapped distribution), justify excluding small angles if done. Provide a physics-based prior for Cγ (order-unity centered, with rationale, or a log-uniform span if truly agnostic), and explore prior sensitivity for the product Cγ × θi.

P2-M3 (Sec. 4; p. 3)
Problem: LiteBIRD “9σ” forecast treats the theory prediction as noiseless. The paper does not present a predictive distribution for β given priors on θi and Cγ or uncertainties in Δϕ/fa.
Required fix: Provide a prior-predictive range for β from your model (including uncertainties in Δϕ/fa once P2-E1 is resolved). Then present the forecast significance distribution (or expected Bayes factor) rather than a single 0.27°/0.03° ratio.

P2-M4 (Sec. 3.2 and 3.3; pp. 2–3)
Problem: Mixing datasets/estimators across sections without a unified primary analysis pathway.
- The summary-likelihood uses Planck NPIPE and ACT DR6 point estimates (β = 0.30 ± 0.11°, 0.215 ± 0.074°), giving β = 0.242 ± 0.061°. The MCMC uses βobs = 0.342 ± 0.094° from a different joint EB procedure. This is acceptable if clearly segregated, but the paper shifts between them.
Required fix: Declare one primary estimator/dataset for the paper’s inference, and treat the other for cross-checks only, with a clear explanation of why the central values differ and explicit statements of non-comparability (see P2-E5).

P2-M5 (Sec. 5; p. 4)
Problem: The connection to ECH gravity/Barbero–Immirzi is speculative and not used in the analysis.
Required fix: Either provide a concrete derivation that impacts the parameter priors or move this discussion to a brief outlook paragraph stating it plays no role in the present inference.

MINOR

P2-N1 (Sec. 2.1; p. 2)
Problem: Notational oddity and avoidable confusion in Eq. (1): “J0(m/H0)/J0(0).”
Since J0(0) = 1, this should be written as 1 − J0(m/H0).
Required fix: Simplify Eq. (1) accordingly (subject to resolving P2-E1/E6).

P2-N2 (Fig. 1; p. 4)
Problem: Axis labels/units and interval annotations are not fully specified in the text reproduction (e.g., β [deg], log10(m/eV)). Ensure consistency with stated priors and ranges.
Required fix: Confirm all figure axes include units, and list the central values and 68% credible intervals in the caption or body.

P2-N3 (Sec. 2.2; p. 2)
Problem: Numerical rounding: “5×10^-3 rad ≈ 0.27°.” 5×10^-3 rad = 0.2865°. This is harmless but should be rounded consistently when used as a headline prediction.
Required fix: Use consistent rounding (e.g., 0.29°) or update the radian value to match 0.27°.

P2-N4 (References; p. 6)
Problem: “In preparation” (Namikawa et al., 2025) and “Companion paper, submitted simultaneously, 2026a/2026b” are not citable sources for quantitative claims.
Required fix: Replace with public arXiv identifiers or published references, or rephrase to avoid relying on non-public results.

P2-N5 (Acknowledgments; p. 6)
Problem: “Computations were performed on consumer hardware using Python, NumPy, and SciPy. ... use of AI research assistants ...” is not standard for PRD and adds no methodological content.
Required fix: Optional: streamline acknowledgments to conventional content.

Recomputations and internal checks

- Weighted combination of Planck NPIPE (0.30 ± 0.11°) and ACT DR6 (0.215 ± 0.074°) under independence:
w1 = 1/0.11^2 = 82.645; w2 = 1/0.074^2 = 182.60; mean = 0.244°, σ = 0.0614°, significance = 0.244/0.0614 = 3.97σ. The paper’s 0.242 ± 0.061° and “3.9σ” are close; please standardize to consistent rounding.
- Eskilt et al. joint value 0.342 ± 0.094° gives 3.64σ; consistent with the quoted 3.6σ.
- Bayes factor using SDDR with a flat prior width of 1° and the combined Gaussian posterior (0.242°, 0.061°): ln B ≈ 6.00 (see P2-E3).
- “9σ” forecast: 0.27°/0.03° = 9, but this ignores model-prediction uncertainty (see P2-M3).

Length
At 6 pages, the paper is concise. However, to meet PRD standards, Section 2 must include a correct derivation (or numerical computation) of Δϕ and its mapping to β, and Section 3 must provide complete methodological details for the inference. These additions may slightly increase length; that is appropriate.

## Summary recommendation
MAJOR REVISIONS

The paper contains several essential methodological and derivational inconsistencies that preclude acceptance in its current form. Most critically, the field-displacement and rotation predictions are internally contradictory (O(1) vs 10^-2 for Δϕ/fa), the “effective photon coupling” estimator is undefined/dimensionally ambiguous, and the Bayes-factor computation does not reproduce from the stated inputs. There are also notation inconsistencies, unexamined independence assumptions in the data combination, and under-specified MCMC methodology. These issues are fixable but require substantial revision, including a correct derivation of Δϕ in ΛCDM, consistent notation and parameter definitions with physical justification, transparent and reproducible calculations for all quoted scalars, and explicit caveats wherever σ-levels from distinct procedures are compared.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

P2-E8 (Secs. 1 vs 2.2; units/definitions; Classes C and D)
Problem: Inconsistent and nonstandard definition of the axion–photon coupling in the β mapping.
- Sec. 1 uses β = Δφ/(2 fa) (implicitly setting g_{aγ} = 1/fa).
- Sec. 2.2 switches to β = (g_{aγ}/2) Δφ with g_{aγ} ≡ C0/fa.
- Standard convention is L ⊃ −(1/4) g_{aγ} φ F F̃ with g_{aγ} = (α/2π)(C_{aγ}/fa), i.e., an explicit α/2π factor. The manuscript’s g_{aγ} = C0/fa omits α/2π entirely.
Impact: This missing α/2π (~1/860) changes the required amplitude by orders of magnitude and directly affects whether “order-unity” inputs yield β ~ 0.3°. If the author intends to absorb α/2π into C0, this must be stated unambiguously (and then “order unity” would be O(10^−3) in the standard normalization). As written, the coupling normalization is inconsistent across sections and with the literature.
Required fix: Choose a single, standard normalization for g_{aγ}; state it once; use it everywhere. If using g_{aγ} = (α/2π)(C_{aγ}/fa), re-derive all β predictions, priors, and posteriors (including the “C free” prior range) accordingly, and reconcile the “order-unity” language with the α/2π factor.

P2-E9 (Secs. 1 vs 2.2; Classes C and F)
Problem: Two inequivalent β formulas are presented without reconciliation.
- Intro: β = Δφ/(2 fa).
- Sec. 2.2: β = (C0/2 fa) Δφ.
These cannot both be the operative definition. The abstract and conclusions rely on “order-unity C0,” but the introduction’s formula effectively sets C0 = 1 by definition.
Required fix: Use one β mapping consistently. If C0 is to be treated as a free/physical parameter, the introduction must also include it; otherwise explain why C0 = 1 is assumed there and not later.

P2-E10 (Sec. 2.1; Classes C and H)
Problem: Onset of rolling redshift misstated and criterion incomplete.
- Text: “...begins rolling at z ∼ O(1) when H(z) ∼ m.”
- The slow-roll breakdown occurs near 3H ≈ m (not H ≈ m). For m ≈ H0, ΛCDM gives H(z=1) ≈ 2–2.5 H0, so 3H(z=1) ≫ m; the field would still be overdamped at z ~ 1. Onset would be closer to z ≲ 0.3 (model-dependent).
Required fix: State the correct criterion (e.g., 3H ≈ m), compute the implied onset redshift for m ~ H0 in ΛCDM, and quantify the dependence on m/H0. This also feeds back into Δφ and β.

P2-E11 (Fig. 1 vs Sec. 3.3; Classes B and J)
Problem: Figure–text mismatch and likely stale numbers.
- Fig. 1 (Run 2, C free) diagonal panel shows β [deg] = 0.324 ± 0.099.
- Text reports βALP = 0.336 ± 0.107 (Run 1) and βfree = 0.344 ± 0.096 (Run 3), but gives no β for Run 2 in the body. The figure’s β and uncertainties do not match either Eq. (6) or Eq. (7).
Required fix: Report the Run 2 β posterior in the text and ensure the numbers plotted in Fig. 1 match the values quoted in Sec. 3.3. If the figure used an older chain or different binning/kernel, regenerate or annotate accordingly.

P2-M6 (Fig. 1; prior sensitivity; Classes B and F)
Problem: Posterior of log10(m/eV) appears prior-limited but this is not discussed.
- Fig. 1 shows log10(m/eV) ≈ −31.4 with a long tail to the prior edge (−35), suggesting sensitivity to the chosen [−35, −30] top-hat prior.
Required fix: Quantify prior sensitivity: repeat Run 2 with widened mass priors (e.g., [−37, −28]) and report how β, Caγ × θi, and Δφ/fa posteriors shift. If the posterior mass is prior-dominated, state this clearly and avoid over-interpreting m constraints.

P2-M7 (Secs. 3.3–3.4; Classes A and H)
Problem: Over-precise evidence quoting despite admitted tail instability.
- The paper acknowledges small Neff and unstable tails, yet reports ln B to two decimals (5.17, 4.48, 5.86). With Neff at most O(10^3) and SDDR relying on density at β = 0 (a tail point), two-decimal precision is not justified.
Required fix: Either (a) compute ln B with a method robust to tails (e.g., thermodynamic integration or nested sampling) and report uncertainties, or (b) downweight the claim to a simple likelihood-ratio proxy with clear caveats, and avoid quoting ln B beyond one significant figure.

P2-M8 (Sec. 3.2; Classes A and E)
Problem: Summary combination does not propagate calibration-angle and shared-model uncertainties.
- Eq. (3) treats the two point estimates as independent Gaussians with fixed variances. However, both experiments’ self-calibration procedures entail residual calibration-angle and foreground-model uncertainties that are not folded into σi. The Discussion acknowledges possible systematics but the combination treats σi as complete.
Required fix: Inflate σi by published calibration-angle posteriors (or add a nuisance variance term) and show sensitivity of the combined significance to this augmentation. If not possible, explicitly state that 3.9σ is conditional on the experiments’ quoted statistical errors only and may overstate the joint significance.

P2-N6 (Global; Classes C and H)
Problem: Inconsistent and unstated angle units.
- Equations in Sec. 2 work in radians (e.g., “5×10^−3 rad”), while likelihoods and posteriors (Secs. 3.2–3.3) are in degrees. The unit convention is never declared, and conversions are not always explicit.
Required fix: Declare a global convention at the start (e.g., theory in radians, data/plots in degrees) and insert explicit conversions where needed, especially in any calculation (like SDDR) that uses densities at specific β values.

P2-N7 (Sec. 1, Abstract; Class F)
Problem: Abstract/intro claim “Combined, the evidence exceeds 3.5σ” is unsourced and method-ambiguous.
- The paper later presents two different combinations (summary-likelihood giving ~3.9σ and Eskilt et al. joint EB giving 3.6σ). The abstract’s “>3.5σ” claim needs to specify which combination and assumptions (independence, systematics) it refers to.
Required fix: Attribute each σ to its specific estimator/dataset and add a “not directly comparable” qualifier when juxtaposed (beyond fixes already requested for P2-E5).

P2-E12 (Implicit modeling; Classes C and H)
Problem: If the standard α/2π factor is restored in g_{aγ}, “order-unity” C0 is insufficient to reach β ~ 0.3° unless Δφ/fa is O(10^−1–1) and/or C0 is large (≳30–50), which conflicts with some stated priors and “no fine-tuning” language.
Required fix: After fixing the coupling normalization (P2-E8), show the quantitative space of {Δφ/fa, C_{aγ}} that yields β ≈ 0.27°, and reconcile it with the chosen priors and the “naturalness” narrative. If large anomaly coefficients are required, justify them with a concrete model or relax the “order-unity” claim.

These issues are in addition to (and do not duplicate) those already identified in the initial review.