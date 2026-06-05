# P2 auto-2026-06-05_1418pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6657 chars)
**Wall time**: 359.8s

---

Referee report on “Cosmic Birefringence from a Planck-Scale Axion-Like Particle: Predictions, Constraints, and LiteBIRD Forecasts” (6 pages)

Scope of review
I audited the statistical methodology, derivations, dimensional consistency, numerical claims, and internal consistency of figures/tables. I recomputed every quoted σ, ratio, and Bayes factor where inputs were given. Below I list all findings with severity, location, exact issue, and required fixes.

ESSENTIAL ISSUES

P2-E1 — Sec. 2.1 (pg. 1–2): Contradictory field displacement scaling
- Offending text/equations:
  • Eq. (1): “Δϕ ≈ fa θi (1 − J0(m/H0)/J0(0)) ≈ fa θi × O(1). For m/H0 ∼ 1, 1 − J0(1) ≈ 0.24…”
  • Sec. 2.2: “the cosmological field evolution gives Δϕ/fa ∼ 10−2… yielding β ≈ C0 θi × 5×10−3 rad ≈ 0.27°.”
- Problem: Eq. (1) implies Δϕ/fa ≈ 0.24 θi (O(10−1)), whereas Sec. 2.2 assumes Δϕ/fa ∼ 10−2. These are inconsistent by over an order of magnitude. If Eq. (1) holds, β ≈ (C0/2)(Δϕ/fa) ≈ 0.12 C0 θi rad ≈ 6.9° for C0 θi ≈ 1, not 0.27°. Conversely, if Δϕ/fa ∼ 10−2 is correct, Eq. (1) is wrong or irrelevant. No derivation is provided that connects the homogeneous axion EOM in an expanding background to the Bessel-function factor used in Eq. (1).
- Required fix: Provide a derivation from the background EOM ϕ¨ + 3Hϕ˙ + dV/dϕ = 0 across the radiation–matter–Λ eras (or a controlled approximation) that yields a quantitative expression for Δϕ between recombination and today, with all coefficients and cosmological dependences explicit. Replace the ad hoc J0(m/H0) expression with a derived result or a documented numerical integration. Then recompute β consistently and propagate uncertainties. Remove the “O(1)” placeholders and provide concrete numbers calibrated to ΛCDM parameters.

P2-E2 — Sec. 3.4 (pg. 3): Bayes factor computation inconsistent with stated inputs
- Offending text: “ln B = 5.17 … computed via the Savage-Dickey density ratio with a flat prior β ∈ [0°, 1°].”
- Problem: Using your combined constraint β = 0.242 ± 0.061° (Eq. 4), the Gaussian posterior density at β = 0 is p(0|data) = (1/√(2π)σ) exp(−(μ/σ)^2/2) = 0.00250 deg−1. With the stated flat prior p(β) = 1 deg−1 on [0°,1°], SDDR gives B10 = p(0|prior)/p(0|data) ≈ 1/0.00250 ≈ 400 → ln B ≈ 5.99, not 5.17. Your internal scaling with prior width (± ln 2 shifts for [0°, 0.5°] and [0°, 2°]) is self-consistent, but the base value at 1° is not consistent with Eq. (4). This is not a rounding issue (>10σ discrepancy in posterior density).
- Required fix: Show the exact numbers used (μ, σ, units) and recompute ln B. Ensure degrees are the parameterization unit for both prior and posterior densities. If a different σ or μ was used, state and justify it. If you used a one-sided prior, justify the sign restriction physically; otherwise adopt a symmetric prior β ∈ [−βmax, βmax] and report how ln B changes (it will shift by −ln 2 relative to your one-sided choice).

P2-E3 — Abstract and Sec. 3.2 (pg. 1, 2–3): Undefined “effective photon coupling fphoton × C0 = 1.73 ± 0.44”
- Offending text: “The effective photon coupling fphoton × C0 = 1.73 ± 0.44 (order-unity, no fine-tuning).”
- Problem: fphoton is not defined anywhere. No equation relates this quantity to β, Δϕ, or cosmological integrals. Units are not specified; the symbol clashes with standard g_{aγ}.
- Required fix: Define fphoton precisely (symbol, units, and relation to g_{aγ} and fa), derive it from the stated likelihood, and show how the quoted mean and uncertainty are obtained from data and model parameters (including any cosmological integral factors). If it is dimensionless, explain why; if not, include units.

P2-E4 — Fig. 1 vs. Sec. 3.3 (pg. 4 vs. pg. 3): Inconsistency in reported coupling–misalignment product
- Offending text/figure:
  • Sec. 3.3: “Caγ × θi = 3.4 ± 1.1 (Run 2, C free).”
  • Fig. 1 panel titles and 1D posteriors show medians/means approximately θi ≈ 1.33 and Caγ ≈ 13.4, implying a product ≈ 17.8, not ≈ 3.4. The β panel shows β ≈ 0.324 ± 0.099°.
- Problem: The figure and the text are numerically incompatible by a factor of ≈5 for the stated product. Either the plotted parameter named “Caγ” is not the same Caγ used in the text definition, or one of the numbers is incorrect. This undermines the main “order-unity” claim.
- Required fix: Precisely define Caγ in the caption and text, reconcile the numbers, and provide a table with the posterior means/medians and 68% intervals for θi, Caγ, Caγ×θi, log10(m/eV), and β from Run 2. If the quantity in the figure is rescaled (e.g., by fa or a cosmological integral), state it and correct the text.

P2-E5 — Sec. 3.1 and throughout (pg. 2): Mixing non-comparable significance metrics without clear caveat
- Offending text: Abstract and Secs. 3.2–3.4 place “3.9σ from zero” and “ln B = 5.17” side-by-side without explicitly stating that Gaussian “nσ from zero” and Bayes factors are not directly comparable metrics and depend on different modeling assumptions.
- Problem: Per journal standards, whenever frequentist “σ” evidence and Bayesian Bayes factors are juxtaposed, the paper must explicitly state that they are not directly comparable and depend on different priors/assumptions, every time they are compared. A parenthetical “prior-dependent” is insufficient.
- Required fix: Add explicit “not directly comparable” language adjacent to each juxtaposition (Abstract; Sec. 3.4; Conclusions), and provide a short paragraph explaining the dependence of ln B on the chosen prior, parameterization, and one-sided vs two-sided support.

P2-E6 — Sec. 3.2 (pg. 2): Independence assumption for Planck and ACT summary-likelihood
- Offending text: “combining the measurements under the assumption of independent errors” (Eq. 3).
- Problem: Planck HFI and ACT DR6 view overlapping sky and use related self-calibration techniques for birefringence estimators; their statistical errors may be partially correlated (e.g., via common polarized sky emission and foreground modeling assumptions). No justification or estimate of the correlation ρ is provided. If ρ ≠ 0, the combined σ is underestimated by a factor (1 − ρ^2)−1/2 for a two-measurement combination.
- Required fix: Justify independence with references to the pipeline covariance or, at minimum, provide a robustness check showing how βcombined and σ(βcombined) vary for ρ ∈ [0, 0.3] (or your best-estimate range). Quote a conservative result or include this uncertainty in the reported combined σ.

P2-E7 — Sec. 2.1 (pg. 1–2): Unjustified use of Bessel function J0(m/H0) in Eq. (1)
- Offending text: “Δϕ ≈ faθi (1 − J0(m/H0)/J0(0)).”
- Problem: No derivation is provided linking the homogeneous axion evolution in ΛCDM to J0 of m/H0. The appearance of J0(0) in the denominator is also gratuitous (J0(0)=1). As written, Eq. (1) neither follows from the standard slow-roll/oscillation solutions nor matches the claimed Δϕ/fa ∼ 10−2 later. The result is dimensionally fine but physically unsupported.
- Required fix: Either (a) derive Eq. (1) from first principles (including approximations and validity domain) or (b) remove it, and present instead a controlled analytic approximation (e.g., matched solutions in matter/Λ eras) or a numerical integral over the expansion history that returns Δϕ/fa as a function of m/H0 and θi, with an explicit numerical coefficient.

P2-E8 — Sec. 3.3 and Table 1 (pg. 3): Likelihood used for MCMC not specified; datasets mixed inconsistently
- Offending text: “For the MCMC parameter estimation (Sec. 3.3), we use the Eskilt et al. joint analysis value βobs = 0.342 ± 0.094°,” while Sec. 3.2 combined result is βcombined = 0.242 ± 0.061°.
- Problem: It is unclear what likelihood is used in Runs 1–3. Are you sampling ALP parameters with a Gaussian summary-likelihood in β centered at βobs = 0.342 ± 0.094°? If so, why is there a separate Gaussian combination (Eq. 4) at 0.242 ± 0.061°? The paper mixes constraints derived from different datasets/procedures without a clear data model, and then plots posteriors (Fig. 1) that cannot be verified.
- Required fix: Explicitly define the likelihood(s) used in each run, including data inputs (Planck-only; ACT-only; joint; or Gaussian summary of one number), parameter-to-observable mapping β(θi, m, C… ), and any priors. Avoid switching between βcombined (from two separate point estimates) and βobs (from a different joint EB fit) unless you show a principled joint-likelihood that unifies them or clearly separate the analyses.

P2-E9 — Sec. 3.4 (pg. 3): One-sided prior on β without physical justification
- Offending text: “flat prior β ∈ [0°, 1°].”
- Problem: The isotropic birefringence angle is a signed rotation; standard analyses allow β ∈ (−∞, ∞) or symmetric compact intervals. A one-sided prior is not justified and affects the Bayes factor by ln 2 relative to a symmetric choice. This choice interacts with your “combined” Gaussian likelihood that is almost 4σ away from zero.
- Required fix: Use a symmetric prior β ∈ [−βmax, βmax] and report ln B for at least two βmax values (e.g., 0.5°, 1°, 2°), or provide a compelling physical justification for restricting β ≥ 0 with references, and quantify the effect on ln B. State explicitly the prior-measure dependence of SDDR.

MAJOR ISSUES

P2-M1 — Sec. 3.3 and Table 1 (pg. 3): MCMC sample sizes insufficient for claimed precision; R̂ alone is inadequate
- Offending text: “accepted samples 720–6,840… R̂ − 1 < 0.01 confirms adequate mixing…”
- Problem: With 3–4 parameters and evident degeneracies (Fig. 1), 720–2,160 samples are inadequate for robust posterior mean/σ at the 0.1σ level, and inappropriate for Bayes-factor estimates. R̂ < 0.01 with such small chains is not a reliability guarantee. Effective sample sizes (Neff ∼ 1,000 reported vaguely) are not shown per parameter.
- Required fix: Run longer chains (Neff ≥ 5,000 per parameter), report effective sample sizes per parameter and potential scale reduction with split-R̂, and verify stability of posterior summaries across independent seeds and thinning choices. If Bayes factors are to be reported from MCMC, use robust evidence estimators with uncertainty (e.g., thermodynamic integration, stepping-stone) or avoid evidence claims from short chains.

P2-M2 — Sec. 2–3 (pg. 1–3): Ambiguous parameter definitions and symbols
- Offending text: “C0” (anomaly coefficient), “C” (fixed to 8 in Run 1), and “Caγ” (prior [1,30]) are used interchangably; “fphoton” undefined.
- Problem: Notation shifts across sections without definitions. “C=8 fixed” contradicts “C0 is an order-unity coefficient” and lacks motivation. Caγ vs C0 vs g_{aγ} are not cleanly related.
- Required fix: Provide a table of symbols with clear definitions, units, and relations (e.g., g_{aγ}=C0/fa; specify if Caγ ≡ C0, or a rescaled coupling). Justify any fixed choices (e.g., C=8) with a model or literature reference.

P2-M3 — Sec. 3.2 (pg. 2–3): Independence and calibration systematics not propagated into the combined constraint
- Offending text: “The combined constraint is βcombined = 0.242 ± 0.061° (3.9σ from zero).”
- Problem: Beyond statistical correlation (P2-E6), you acknowledge systematic calibration uncertainties (Sec. 6) at the 0.1–0.3° level that can bias isotropic β. These are not propagated into the combined error budget, rendering 3.9σ potentially overstated.
- Required fix: Add a systematic error term consistent with the quoted calibration systematics (e.g., nuisance-parameter marginalization, or inflate σ with a conservative systematic floor), show how βcombined and its significance change, and report a total uncertainty.

P2-M4 — Sec. 4 (pg. 3): Overstatement of falsifiability
- Offending text: “If LiteBIRD measures β = 0 ± 0.03°, the ALP explanation is excluded at 9σ.”
- Problem: A null β at 0.03° excludes the specific parameter combination predicting β ≈ 0.27°, not the general ALP explanation with differing C0, θi, or cosmology. The paper itself treats C and θi as free and “order-unity”.
- Required fix: Rephrase to “this specific parameterization/predicted amplitude” rather than “the ALP explanation,” and quantify how much of the prior volume in (C0, θi, m/fa) would be ruled out by β = 0 ± 0.03°.

P2-M5 — Sec. 3.1 (pg. 2): Reliance on unpublished or in-preparation references
- Offending text: “Diego-Palazuelos and Komatsu, 2025: arXiv preprint… Namikawa et al., 2025: arXiv e-prints, in preparation.”
- Problem: Critical numerical inputs (ACT DR6 birefringence) and comparisons are cited to unpublished or “in preparation” sources without arXiv identifiers; this prevents verification.
- Required fix: Cite stable arXiv numbers or published versions for all numerical inputs used in your inference. If not available, either remove the results dependent on them or clearly mark them as provisional and provide a sensitivity analysis using published alternatives.

P2-M6 — Sec. 2.2 (pg. 2): Dimensional analysis and numerical conversion
- Offending text: “β ≈ C0 θi × 5×10−3 rad ≈ 0.27°.”
- Problem: 5×10−3 rad converts to 0.2865°, not 0.27°. While small, the paper claims precision at the 0.01–0.02° level elsewhere; consistent conversions matter.
- Required fix: Use consistent conversions and quote appropriately rounded numbers (0.29° if using 5×10−3 rad), or use the derived coefficient from a proper Δϕ computation per P2-E1.

P2-M7 — Sec. 5 (pg. 4): Speculative ECH/Barbero–Immirzi motivation encroaches on results
- Offending text: The ECH gravity discussion and “14-barrier catalog” pointer.
- Problem: This is qualitative and not used in any derivation. It distracts from the methods paper and suggests a scale choice (fa ∼ MPl) without providing a derivation.
- Required fix: Either provide a concrete derivation connecting that framework to the coupling and potential used here or move this text to a brief footnote, clarifying it is not used in the analysis.

MINOR ISSUES

P2-n1 — Abstract (pg. 1): “3.6σ isotropic birefringence signal” traceability
- Issue: You quote βobs = 0.342 ± 0.094° (3.64σ) and attribute to “Eskilt et al. joint Planck + ACT analysis.” Please give the exact citation (journal, arXiv number) and ensure consistency with the values used later (you later use βobs = 0.342 ± 0.094° in Sec. 3.3).
- Fix: Add full citation and confirm numbers match that source’s abstract/tables.

P2-n2 — Sec. 3.3 (pg. 3) and Fig. 2 (pg. 5): Clarify why βALP = 0.336 ± 0.107° is broader than βobs = 0.342 ± 0.094°
- Issue: If your MCMC likelihood is a Gaussian summary in β around βobs, the posterior on β inferred through the ALP model should not be broader unless the model mapping or priors add variance. Not explained.
- Fix: Explain the source of widening (e.g., marginalization over cosmological integral uncertainty), and quantify.

P2-n3 — Table 1 (pg. 3): “Samples” ambiguous
- Issue: Are these accepted samples post–burn-in? Total draws? Across how many chains? What is the thinning?
- Fix: Provide full MCMC diagnostics: number of chains, total draws, burn-in, thinning, per-parameter Neff, and split-R̂.

P2-n4 — Fig. 1 and Fig. 2 captions (pgs. 4–5): Add dataset/likelihood provenance
- Issue: The reader cannot tell whether the plotted posteriors correspond to the “βobs” likelihood or the “βcombined” likelihood.
- Fix: State explicitly the likelihood and priors used in the plotted runs in the captions.

P2-n5 — Bibliography (pg. 6): Incomplete entries
- Issue: Missing arXiv identifiers for 2025 references; “in preparation” citation not acceptable for quantitative comparison.
- Fix: Update with full arXiv IDs or remove.

P2-n6 — Typographic/notation consistency
- Issue: Use of C, C0, Caγ varies; J0(0) divisor is unnecessary; repeated “order-unity” phrasing.
- Fix: Clean notation and streamline wording.

NITS

P2-N1 — Eq. (1) (pg. 2): J0(0)
- Cosmetic: J0(0)=1; the denominator is superfluous.
- Fix: Remove “/J0(0)”.

P2-N2 — Abstract and Sec. 6 (pg. 1, 5): Overuse of “no fine-tuning,” “natural”
- Cosmetic: These are qualitative claims and do not substitute for a derivation.
- Fix: Reduce rhetorical phrasing, favor quantitative statements.

P2-N3 — Acknowledgments (pg. 6)
- Cosmetic: “Computation performed on consumer hardware…” is nonessential.
- Fix: Optional removal.

Length and scope
For the stated contribution, 6 pages would be appropriate if the central derivation and statistical synthesis were rigorous and internally consistent. As it stands, multiple core derivations and calculations require substantial revision; the current draft reads more as a sketch than a PRD-ready analysis.

Summary recommendation
REJECT

Rationale: The manuscript contains fundamental inconsistencies in the core theoretical prediction (Δϕ/fa scaling: Eq. 1 vs. Sec. 2.2), a materially incorrect Bayes factor computation relative to the stated inputs, undefined or ambiguously defined key parameters (e.g., fphoton, C/C0/Caγ), and a serious mismatch between text and figure values for the coupling–misalignment product. The combined-data analysis assumes independence without justification and does not propagate known systematics. The MCMC analyses are underpowered and lack a clearly specified likelihood. These issues are methodological and conceptual, not cosmetic; addressing them will require re-deriving the central result, re-running the inference with a specified likelihood and adequate sampling, and clarifying notation and data usage throughout.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (second-pass audit)

ESSENTIAL ISSUES

P2-E10 — “Spectator” energy-density inconsistency (Sec. 2.1–2.2; throughout)
- Issue: For fa ∼ MPl, m ∼ H0, and θi ∼ O(1), the axion’s potential energy scale is ρϕ ∼ m^2 f_a^2 (1 − cos θi) ≈ H0^2 MPl^2 × O(1), which is of order the present critical density. Numerically, with H0 ≈ 1.5×10^−33 eV and MPl ≈ 2.4×10^27 eV, m^2 f_a^2 ≈ 1.3×10^−11 eV^4, comparable to ρΛ ≈ (2.3 meV)^4 ≈ 2.6×10^−11 eV^4. Thus, for θi ∼ 1, the field is generically a non-negligible dark-energy-like component, not a “spectator.” Its dynamics should back-react on H(a) and w(a), affecting distances and CMB/BAO fits.
- Required fix: Quantify Ωϕ(a) and wϕ(a) for your parameter choices, include the field’s contribution in the background expansion when computing Δϕ, and check against current constraints on (w0, wa). If you truly intend a spectator, restrict θi or C0 (or m/fa) such that Ωϕ ≪ 1 today, and state this explicitly.

P2-E11 — Degree–radian inconsistency between model and likelihood (Secs. 2.2, 3.2–3.4)
- Issue: Equations and text derive β in radians (e.g., “5×10^−3 rad”), but all likelihoods and quoted measurements are in degrees (Eq. 3; Eqs. 4, 6–7). The paper never states the conversion applied when mapping the model β(θi, m, C0, …) to the Gaussian likelihoods in degrees.
- Required fix: State the unit convention explicitly and include the conversion β[deg] = (180/π) β[rad] in the model-to-data map. Recompute any numbers that relied on an implicit or inconsistent unit assumption (this also affects the SDDR density values in Sec. 3.4).

P2-E12 — SDDR Bayes factor evaluated at a prior boundary (Sec. 3.4)
- Issue: With a one-sided prior β ∈ [0°, βmax], the null point β = 0 sits on the boundary of parameter space. The Savage–Dickey density ratio in its simple form assumes an interior point; using it at a boundary requires care (the posterior is a truncated Gaussian, and densities differ by a factor of two relative to the two-sided case when μ/σ ≫ 1).
- Required fix: Either (i) adopt a symmetric prior β ∈ [−βmax, βmax] and report the resulting ln B (preferred), or (ii) derive and present the correct boundary-aware SDDR for the truncated posterior, showing how it differs from the two-sided result. Quote uncertainties from numerical evaluation.

MAJOR ISSUES

P2-M7 — Cosmology dependence of Δϕ not propagated (Secs. 2.1–2.2; 3.2; 4)
- Issue: You state the Δϕ (and hence β) prediction depends on the matter and dark-energy eras, yet no uncertainty from ΛCDM parameters (Ωm, ΩΛ, H0) is propagated into Δϕ/fa or the 9σ forecast. Even a few-percent change in H(a) over z ≲ 2 can shift Δϕ at the level relevant for 0.03° forecasts.
- Required fix: Propagate Planck/BAO posteriors on (Ωm, H0, ΩΛ) through your Δϕ computation (analytic or numeric) and include this as a modeling uncertainty in β. Update the LiteBIRD significance range accordingly.

P2-M8 — Asymmetric/biased priors on θi and Caγ (Sec. 3.3)
- Issue: Priors place θi ∈ [0.01, π] (forbidding negative misalignment) and Caγ ∈ [1, 30] (forbidding small/zero coupling). Combined with a one-sided β prior, these choices preclude negative β and structurally favor nonzero rotation.
- Required fix: Use symmetry-respecting priors, e.g., θi ∈ [−π, π] with a circular measure, and allow Caγ ≥ 0 (or a symmetric prior on Caγ’s sign if it can be negative depending on conventions). Reassess posteriors and Bayes factors under these less informative choices, and quantify sensitivity to prior ranges.

P2-M9 — Mass posterior vs. “m ∼ H0” narrative tension (Fig. 1; Sec. 3.3; Sec. 2.1)
- Issue: Fig. 1 shows log10(m/eV) ≈ −31.4 with O(1) dex uncertainty, implying m/H0 ∼ 20–60 at the posterior center, i.e., the field would start rolling earlier than z ∼ 1. The main text repeatedly frames m ∼ H0 with zroll ∼ O(1), but this central value suggests otherwise.
- Required fix: Report and discuss the posterior of m/H0 explicitly, including the inferred z at which H(z) ≈ m. Reconcile this with the statement “begins rolling at z ∼ O(1)” or revise the narrative.

MINOR ISSUES

P2-m7 — Figure 2 vs. body text mismatch in what is being compared (pg. 5 vs. Sec. 3.2)
- Issue: Fig. 2 compares three posteriors centered near β ≈ 0.33–0.35°, matching the “βobs” likelihood, but the paper’s highlighted combined result is βcombined = 0.242 ± 0.061°. The figure does not visualize this combined constraint, yet the caption/body states all are “consistent with each other and with the observed value.”
- Fix: Clarify in the caption and text that Fig. 2 uses the βobs likelihood only, and add a panel/curve for the “combined” likelihood if you wish to compare with that result. Otherwise, avoid conflating the two.

P2-m8 — Lagrangian normalization not specified (Secs. 2.2; 6)
- Issue: The factor-of-two in β = (gaγ/2) Δϕ depends on the operator normalization. Standard conventions often use L ⊃ −(gaγ/4) ϕ Fμν F̃μν. Without stating the exact normalization, factors of 2 can migrate between β and gaγ, feeding directly into the “effective coupling” numbers.
- Fix: Write the exact interaction term used, including numerical factors, and trace how it leads to β = (gaγ/2) Δϕ in your convention. Align symbol definitions with the literature mapping gaγ = (α/2πfa)(E/N − 1.92) if relevant, or explain deviations.

P2-m9 — “Consistent with” claims not quantified (Abstract; Sec. 6)
- Issue: Statements like “matches the combined Planck + ACT measurement at 1σ” are not directly quantified in-text. For example, 0.27° vs. 0.242 ± 0.061° is a 0.46σ offset; 0.27° vs. 0.342 ± 0.094° is a 0.77σ offset.
- Fix: Add the explicit normalized residuals (Δ/σ) when using “consistent with” language.

P2-m10 — Small rounding inconsistency in “3.9σ” vs. exact ratio (Sec. 3.2)
- Issue: 0.242/0.061 = 3.97σ (≈ 4.0σ), not 3.9σ. Minor, but the paper emphasizes numerical precision elsewhere.
- Fix: Harmonize rounding (e.g., “4.0σ”) or state more significant figures consistently.

P2-m11 — Units missing on Caγ axis in Fig. 1 (pg. 4)
- Issue: The Caγ axis is unitless in the figure, but if Caγ represents a rescaled photon coupling, units or the rescaling definition should be shown to avoid confusing it with gaγ.
- Fix: Add units or an explicit definition in the caption.

NO OTHER DUPLICATES WITH INITIAL REPORT

These items are new relative to the first review and focus on energy-budget self-consistency, unit rigor between model and likelihood, boundary effects in Bayes-factor computation, prior choices that structurally bias β > 0, tension between the mass posterior and the stated “m ∼ H0” narrative, and additional figure-text and normalization clarifications.