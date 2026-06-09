# P2 R22prov — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8926 chars)
**Wall time**: 262.1s

---

Referee report on “Cosmic Birefringence from a Planck-Scale Axion-Like Particle: Predictions, Constraints, and LiteBIRD Forecasts”

Scope of review
I assessed the statistical methodology, derivation chains, dimensional consistency, arithmetic, and internal coherence of all quoted numbers in the abstract, body, figures, and conclusions. Below I list all issues found, each tagged with severity, location, the precise problem, and a required fix.

Findings

ESSENTIAL

P2-E1 (Sec. 3.4, p. 3): Bayes factor numbers are inconsistent with the stated inputs and with Savage–Dickey.
- Offending text: “ln B = 5.17 (… prior β ∈ [0°, 1°]); … ln B = 4.48 for β ∈ [0°, 2°] and ln B = 5.86 for β ∈ [0°, 0.5°].”
- Audit: Using the combined Gaussian posterior in Eq. (4), μ = 0.242°, σ = 0.061°. For a flat prior of width W, the Savage–Dickey expression for the Bayes factor in favor of β ≠ 0 is ln B = ln(W/(√(2π)σ)) + μ^2/(2σ^2). This gives:
  - W = 1°: ln B = ln(1/(2.5066×0.061)) + (0.242)^2/(2×0.061^2) = 1.88 + 7.87 = 9.75.
  - W = 2°: ln B = 2.57 + 7.87 = 10.44.
  - W = 0.5°: ln B = 1.18 + 7.87 = 9.05.
  Using the Eskilt et al. value 0.342 ± 0.094° yields ln B ≈ 8.05 (W = 1°). None match the paper’s 5.17, 4.48, or 5.86. Units (deg vs rad) cancel if used consistently and do not explain the discrepancy.
- Required fix: Recompute ln B with an explicit formula, state clearly which posterior (Eq. 4 or the model-independent/MCMC posterior) is used, the prior width and parameterization, and provide a reproducible calculation. Correct the quoted ln B values throughout.

P2-E2 (Sec. 5, pp. 4–5): Logical and mathematical contradiction regarding β’s dependence on θi.
- Offending text: After deriving Ωφ ≈ (1/6)(m/H0)^2(fa/MPl)^2θi^2, the paper adopts θi ≈ 0.22 to enforce Ωφ ≪ 1 and then states “the β ∼ 0.27° prediction continues to hold by the cancellation above.”
- Audit: With gaγ ∝ 1/fa and Δφ ∝ fa θi F(m/H0), β = (gaγ/2)Δφ ∝ θi F(m/H0) (fa cancels but θi does not). Reducing θi from ≈1 to 0.22 reduces β by ≈4.5, to ≈0.06°, not 0.27°. The “cancellation” removes fa, not θi.
- Required fix: Correct the statement. If the spectator condition is enforced by θi ≈ 0.22, update the predicted β accordingly, or explicitly compensate by adjusting Caγ and/or F(m/H0), and show the parameter values and calculations that restore β ≈ 0.27°. Revise the abstract and conclusions to reflect the corrected prediction under the adopted “spectator” point.

P2-E3 (Throughout: Abstract, Sec. 2.2, Sec. 7): Omitted αEM factor in the stated “scope” expression for β.
- Offending text (Abstract and Sec. 7): “β ≈ (C0 θi/2) F(m/H0) is independent of fa.”
- Audit: From Eq. (2), β = (αEM/4π) Caγ θi F(m/H0). While the scaling with fa is indeed absent, the amplitude includes the small factor αEM/4π ≈ 5.81×10^-4, crucial for any “naturalness” amplitude discussion.
- Required fix: Restore the αEM/4π factor wherever the scaling expression is used, or explicitly state “up to an overall αEM/4π factor” and keep it in all amplitude-level arguments.

P2-E4 (References: multiple places): Numerous “[?]” placeholders instead of actual citations.
- Offending locations: Introduction (Planck/ACT references), Sec. 2.2 (conventions), Sec. 3.1 (datasets), Sec. 4 (LiteBIRD performance), Sec. 6–7 (ECH gravity, related literature), and elsewhere.
- Required fix: Replace all “[?]” with full, correct references (journal, year, arXiv ID). PRD cannot accept a manuscript without a complete, accurate bibliography.

P2-E5 (Sec. 3.1–3.3, pp. 2–3): Primary estimator and dataset usage not cleanly pre-declared; mixing non-comparable β estimates without clear caveats.
- Offending text: Sec. 3.2 combines two point estimates (Planck NPIPE and ACT DR6) to form Eq. (4), while Sec. 3.3 uses the Eskilt et al. joint EB-spectrum result (βobs = 0.342 ± 0.094°) for MCMC. The text asserts agreement but does not state that these are from different estimators and analysis pipelines.
- Required fix: Up front, declare the primary estimator used for inference, and add prominent “not directly comparable” qualifiers when juxtaposing β from the summary-likelihood (point-estimate combination) with βobs from a full EB-spectrum fit. State explicitly why the two are combined/compared and what independence or correlation assumptions are being made.

P2-E6 (Sec. 3.2, p. 2; Abstract): Undefined “effective photon coupling parameter” fphoton × C0 = 1.73 ± 0.44.
- Offending text: Eq. (5) and abstract mention fphoton × C0 without a definition or derivation.
- Required fix: Provide a precise definition of fphoton (with units and dependence on θi and F(m/H0)), and the explicit mapping from β to fphoton × C0 used to obtain Eq. (5). Include the numerical inputs and propagation of uncertainties.

MAJOR

P2-M1 (Sec. 5, p. 5): Mischaracterized degree of “fine-tuning.”
- Offending text: “suppressing θi to ~√0.05 θnat ≈ 0.22 (a ~25× fine-tuning of the initial misalignment relative to the natural prior midpoint…).”
- Audit: √0.05 ≈ 0.2236, a factor of ≈4.5 reduction from unity, not 25×. If the “25×” refers to energy density reduction, the factor is ≈20, not 25, and it applies to ρ (or Ω), not θi itself. If the “natural prior midpoint” is π/2, the suppression is ~7×.
- Required fix: State clearly which quantity is being reduced (θi vs Ωϕ), and correct the factor(s) and wording.

P2-M2 (Notation consistency: multiple sections): Mixed use of C0 and Caγ for the anomaly coefficient.
- Offending locations: Abstract uses C0; body and figures use Caγ.
- Required fix: Adopt a single symbol throughout, define it exactly once, and ensure consistency across text, equations, and figures.

P2-M3 (Sec. 3.3 and Table 1, p. 3): MCMC configuration insufficiently specified and arguably underpowered for quoted inferences.
- Offending text: “Run 1: 2,160 samples … Run 3: 720 samples … R̂−1 < 0.01 … Neff ~ 1,000; … Bayes factor via SD.”
- Audit: The total number of accepted samples and per-chain lengths are not reported; 720 samples in Run 3 are not enough for reliable tail estimates, nor to support Bayes-factor computations (which depend sensitively on posterior mass near the null). It is not clear whether these are post burn-in samples per chain, how many chains were used, and what ESS for each parameter actually is. Quoted ESS “~1,000” exceeds the accepted samples for some runs as stated.
- Required fix: Report number of chains, total post burn-in draws per chain, integrated autocorrelation times, and actual ESS per parameter. Increase chain lengths to reach stable ESS > 5,000 for scalar posteriors used in Bayes factors and tail probabilities, or refrain from quoting Bayes factors from these chains.

P2-M4 (Fig. 1 vs Sec. 3.3; pp. 4 and 3): Inconsistency of β posterior values between figure and text.
- Offending items: Fig. 1 corner label shows β[deg] = 0.324 ± 0.099; text (Run 3) reports βfree = 0.344 ± 0.096°.
- Required fix: Clarify which run the figure corresponds to, and make the numerical values consistent across figure captions and text. If different datasets or priors are used, state that explicitly.

P2-M5 (Sec. 2.1, p. 2; Eq. (1)): The “∆φ/fa ≈ 0.2–1.1” range is asserted without derivation, plot, or table.
- Required fix: Provide either an analytic approximation or a plot/table of ∆φ/fa vs m/H0 for the stated θi, along with numerical-method details (solver, tolerance, initial conditions, background cosmology used). This is load-bearing for the predicted β amplitude.

P2-M6 (Sec. 2.2, p. 2): Statement of “no fine-tuning” tied to Caγ being an “integer of natural size.”
- Issue: The effective amplitude depends on the product Caγ θi F(m/H0). Given the spectator energy-density constraint pushing θi ≪ 1 (if adopted), the claim of “no fine-tuning” requires compensating choices elsewhere and should be qualified.
- Required fix: Reframe the naturalness discussion to separate the fa-cancellation from the remaining dependence on θi and Caγ, explicitly acknowledging the trade-offs if the spectator condition is enforced by small θi.

P2-M7 (Sec. 3.1, p. 2): Dataset specification and independence assumptions.
- Issue: “Planck NPIPE” and “ACT DR6” β numbers are quoted without full citations and without a discussion of sky overlap or correlated systematics. Treating them as independent for Eq. (3) is asserted but not justified.
- Required fix: Provide bibliographic details for the two measurements and a brief justification for the independence assumption for the summary-likelihood combination, or include a covariance term and assess sensitivity.

P2-M8 (Sec. 7, p. 6): Novelty and literature positioning.
- Issue: The paper asserts the contribution is the “specific parameter identification (fa ∼ MPl, m ∼ H0)” and an inference framework. Prior work (e.g., Fujita et al. 2021) is mentioned but citation placeholders remain, and claims about “superior” constraints elsewhere are not backed by references and comparisons.
- Required fix: Supply full citations and explicitly position the present work relative to earlier Planck-scale ALP birefringence analyses, making clear what is new in methods and results.

MINOR

P2-m1 (Abstract and Sec. 1, pp. 1–2): All scalar claims audited.
- 0.342/0.094 = 3.64σ (stated 3.6σ) — acceptable rounding.
- Weighted combination of 0.30 ± 0.11 and 0.215 ± 0.074 yields 0.242 ± 0.061 and 3.94σ — matches Eq. (4).
- The example β calculation with Caγ = 8 and ∆φ/fa = 1.07 gives β ≈ 0.285° — consistent with 0.29°.
- Required fix: None, but keep explicit that degrees are used.

P2-m2 (Eq. 11, p. 5): Dimensional analysis and factor of 1/6.
- Audit: Ωφ = (1/2 m^2 f_a^2 θ_i^2)/(3 M_Pl^2 H_0^2) = (1/6)(m/H0)^2 (f_a/M_Pl)^2 θ_i^2 — correct.
- Required fix: None.

P2-m3 (Formatting/typos: multiple pages):
- Examples: “mθ ∼ H0” (Abstract, p. 1) — unclear symbol; likely “m ∼ H0.”
- Repetition in Sec. 2.1 (“field is frozen … begins rolling …” appears twice).
- Required fix: Correct “mθ” to “m” and clean repeated sentences.

P2-m4 (Units and symbols): Ensure every β is explicitly labeled in degrees in figures and text; make clear when intermediate calculations are in radians.

P2-m5 (Fig. 2 caption, p. 5): The caption states consistency with “βobs = 0.342 ± 0.094°”; add that this is from a different analysis pipeline than the summary-likelihood combination to avoid casual cross-comparison.

NITS

P2-n1 (Typography): Occasional spacing around the degree symbol and hyphenation artifacts (e.g., “class tuning admitted in companion Paper I(a)”) — minor polishing needed.

P2-n2 (Acknowledgments): “AI research assistants” mention is acceptable but consider specifying which tools and versions for reproducibility if they influenced computations.

P2-n3 (Overreach language): Phrases like “no fine-tuning” should be toned down or precisely defined given Sec. 5’s need to tune θi for the spectator condition.

Additional arithmetic checks performed
- LiteBIRD forecast significance: 0.27/0.03 = 9.0σ — OK.
- ACT DR6 significance from quoted number: 0.215/0.074 = 2.91σ — OK.
- Planck NPIPE significance: 0.30/0.11 = 2.73σ — OK.

Page length and scope
At 7 pages, the manuscript is compact. However, for PRD methods standards, the numerical and statistical methodology sections (ODE integration details; MCMC setup, convergence, and ESS; Bayes factor computation) require significant expansion for reproducibility and correctness.

Summary recommendation
MAJOR REVISIONS

Justification: The manuscript contains a central methodological error (β’s scaling with θi) that directly affects the headline prediction under the adopted “spectator” choice, and a substantial numerical inconsistency in the Bayes factor calculation. Additionally, the paper lacks complete citations, mixes notations, omits definitions for load-bearing parameters, and provides insufficient detail for key numerical procedures and MCMC diagnostics. These issues must be corrected and clarified before the work can be considered for publication in Physical Review D.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (second-pass audit)

ESSENTIAL

P2-E7 (Sec. 2.2, p. 2): The quoted “prediction spans β ≈ 0.17–0.43° across the natural parameter range …” is arithmetically inconsistent with Eq. (2) and the ranges given just above.
- Offending text: “The prediction spans β ≈ 0.17–0.43° across the natural parameter range m/H0 ∈ [1, 3], θi ∈ [0.5, 2], Caγ ∈ [4, 12] …”
- Audit: With β = (αEM/4π) Caγ (Δϕ/fa) and Δϕ/fa = θi F(m/H0), your own Eq. (1) gives F ≈ 0.2–1.1 for θi = 1 and m/H0 ∈ [0.5, 3]. Using θi ∈ [0.5, 2] implies Δϕ/fa ∈ [0.1, 2.2]. Then:
  - βmin = (α/4π) × 4 × 0.1 = 5.81e−4 × 0.4 = 2.32e−4 rad = 0.0133°, not 0.17°.
  - βmax = (α/4π) × 12 × 2.2 = 5.81e−4 × 26.4 = 0.01535 rad = 0.879°, not 0.43°.
  Even with more conservative F ≈ 0.65 (your fiducial m = H0 case), the span is roughly 0.075°–0.60°, still incompatible with 0.17°–0.43°.
- Required fix: Recompute the β range using Eq. (2) with explicit choices for F(m/H0), θi, and Caγ. Show the calculation and tighten the range accordingly, or provide a plot of β across the stated parameter box. Correct all affected statements in the abstract and text.

P2-E8 (Fig. 1 vs Sec. 3.3, pp. 4 and 3): Internal inconsistency between the corner-plot diagonals and the stated product posterior Caγ × θi = 3.4 ± 1.1.
- Offending items: Fig. 1 diagonal labels show medians roughly θi ≈ 1.33 and Caγ ≈ 13.4, which imply a product ≳ 17, not 3.4 ± 1.1 as claimed in Eq. (8) and the caption.
- Required fix: Verify the axes, units, and parameters plotted in Fig. 1. If the figure truly corresponds to Run 2, either the product posterior in the text is wrong or the plotted marginals are from a different run or parameterization. Re-generate the figure and/or correct the numbers so that Caγ, θi, and their product are mutually consistent. State whether Caγ was treated as continuous or discrete in this run (see P2-M9).

P2-E9 (Fig. 1 vs Secs. 2 and 5; dimensional/physical consistency): The posterior on the mass in Fig. 1 contradicts the model assumptions used elsewhere.
- Offending items: Fig. 1 shows log10(m/eV) ≈ −31.4 as the posterior center. With H0 ≈ 1.5×10−33 eV, this is m/H0 ≈ 26.
- Audit: Much of the paper’s prediction logic assumes m ∼ H0 (rolling at z ∼ 1, Eq. 1 range for F, slow-roll energy-density estimate in Sec. 5). If m/H0 ≈ 26, the field would begin evolving much earlier; Δϕ/fa and Ωϕ(z = 0) must be recomputed in that regime. The spectator-energy-density discussion using Eq. (11) also changes in character once m ≫ H0 (oscillatory regime, matter-like redshifting).
- Required fix: Reconcile the mass posterior with the narrative:
  - Either constrain the analysis to m/H0 ≈ O(1) and show posteriors consistent with that regime, or
  - Update Secs. 2 and 5 to reflect the m ≫ H0 posterior: provide Δϕ/fa(m, θi) and Ωϕ(z = 0) in the oscillatory regime and revise the β prediction and “spectator” discussion accordingly.

P2-E10 (Sec. 3.4, p. 3): Prior domain for β in the Savage–Dickey Bayes factor is one-sided, but β is a signed quantity in CMB analyses.
- Offending text: “computed … with a flat prior β ∈ [0°, 1°] (and variations to [0°, 2°], [0°, 0.5°]).”
- Audit: Standard isotropic-birefringence analyses allow β ∈ (−∞, +∞) (practically, a compact symmetric interval in degrees or radians). Using a one-sided prior at the boundary alters the SD ratio; for a symmetric prior β ∈ [−W, W], the prior density at β = 0 is 1/(2W), i.e., ln B increases by ln 2 relative to a [0, W] prior. This is independent of the already-flagged numerical errors in P2-E1.
- Required fix: Justify a one-sided prior physically, or adopt a symmetric prior β ∈ [−W, W]. Recompute ln B, and specify the parameterization (degrees vs radians) and normalization explicitly.

P2-E11 (Secs. 3.1–3.2, pp. 2): Missing sign-convention harmonization between Planck and ACT before combining β.
- Issue: Planck and ACT papers do not necessarily adopt the same EB sign convention for β. Combining measurements without documenting the sign mapping risks an effective sign flip in one dataset.
- Required fix: Cite the original Planck and ACT sign conventions, state the mapping you use, and show the transformed numbers prior to the combination in Eq. (3).

P2-E12 (Sec. 5, p. 5): Unsupported claim about parameter-space allowance in ΛCDM.
- Offending text: “reinterpreting the ALP as a dark-energy-like component contributing Ωϕ ∼ 0.17 … allowed under ΛCDM at the ∼10% level by current constraints …”
- Audit: Planck 2018+BAO constrain the present-day dark-energy density and equation-of-state at percent-to-few-percent level; an explicit 17% shift in ΩDE requires re-fitting the expansion history. No citation or re-fit is provided.
- Required fix: Provide up-to-date constraints and a quantitative demonstration (or a reference) that Ωϕ ≈ 0.17 as a DE-like component is allowed, including w(z) assumptions; otherwise, remove or qualify the claim.

MAJOR

P2-M9 (Sec. 3.3 and Fig. 1, p. 3–4): Treatment of the anomaly coefficient Caγ as continuous vs integer is unspecified and methodologically important.
- Issue: The text calls Caγ an “integer” and uses a flat prior on [1, 30] (Run 2), but it is unclear whether the MCMC samples Caγ as a discrete parameter, a continuous proxy, or an integer-rounded variable. The corner plot shows continuous posteriors.
- Required fix: State explicitly how Caγ is treated in inference (discrete vs continuous), how proposals are made, and how integer constraints are enforced. If continuous, rephrase claims about “integer” and discuss implications.

P2-M10 (Abstract, Secs. 1 and 5): Unsubstantiated claim that “fa ∼ MPl is required by EFT consistency” conflicts with option (b) in Sec. 5.
- Issue: The abstract asserts EFT consistency requires fa ∼ MPl for a gravitationally coupled pseudoscalar. No references are provided, and Sec. 5 explicitly lists lowering fa as an option. These two statements are in tension.
- Required fix: Provide concrete citations (e.g., WGC/grav-instanton bounds) that quantitatively enforce fa ≳ O(MPl) for the model at hand, including assumptions, or soften/remove the claim and align the abstract with Sec. 5.

P2-M11 (Sec. 3.3, p. 3): The “Run 1/Run 3” results are effectively tautological with the chosen Gaussian β inputs, but this is not disclosed as a limitation.
- Issue: Using a single-number Gaussian summary for β as the likelihood and then reporting βpost ≈ βobs is expected. Presenting this as a substantive model check without caveats overstates the inference content.
- Required fix: Add a clear statement that these runs test only the mapping from ALP parameters to β within a Gaussian β-likelihood, not the raw EB spectra, and that the agreement is therefore largely by construction.

MINOR

P2-m6 (Priors; Sec. 3.3, p. 3): Ambiguity in the “θi flat on [0.01, π]” prior.
- Issue: Is θi uniform in angle (radians), uniform in cos θ, or another measure motivated by random initial phases? The naturalness discussion depends on this choice.
- Required fix: Specify the prior measure for θi and justify it physically.

P2-m7 (Notation; throughout): F(m/H0) is used repeatedly without a formal definition.
- Issue: F is introduced informally as Δϕ/(fa θi), but no equation, plot, or reference is provided.
- Required fix: Define F(m/H0) precisely, and provide either an analytic approximation or a numerical table/figure.

P2-m8 (Planck mass convention; Sec. 5): Specify whether MPl is the reduced Planck mass.
- Issue: Eq. (11) and the Friedmann factor 3 MPl^2 H0^2 imply the reduced Planck mass, but this should be stated to avoid 8πG vs G ambiguities.
- Required fix: Define MPl at first use and maintain consistency.

P2-m9 (Units; priors and figures): Clarify units everywhere θi and β appear.
- Issue: θi prior limits appear to be in radians; β is reported in degrees; Fig. axes mix units without explicit labels for all panels.
- Required fix: Label units in every figure axis and explicitly state unit conversions wherever numerical values are quoted from equations defined in radians.

P2-m10 (Dataset naming; Sec. 3.1): “Planck NPIPE” vs “Planck HFI” usage.
- Issue: The text alternates between NPIPE/HFI without precise citation, which may refer to different processing/cleaning approaches.
- Required fix: Standardize nomenclature and provide exact references to the specific Planck release/analysis used for β.

Explanation for new findings
This second pass focused on cross-checking figure numerics against text claims and recomputing ranges implied by your own equations and stated parameter intervals. The most significant newly identified issues are (i) the β-range arithmetic error (P2-E7), (ii) internal inconsistencies between Fig. 1 and the stated posteriors (P2-E8), and (iii) the mass posterior in Fig. 1 being far from the m ∼ H0 regime assumed in multiple sections (P2-E9). These materially affect the paper’s conclusions and must be addressed for PRD-level rigor.