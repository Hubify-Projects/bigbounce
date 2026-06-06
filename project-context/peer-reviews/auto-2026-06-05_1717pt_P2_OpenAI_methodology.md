# P2 auto-2026-06-05_1717pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7805 chars)
**Wall time**: 313.6s

---

Referee report on: “Cosmic Birefringence from a Planck-Scale Axion-Like Particle: Predictions, Constraints, and LiteBIRD Forecasts”

Scope of review: methodology rigor (derivations, dimensional analysis, statistical validity, internal arithmetic/consistency), with full-page, figure, table, and reference audit.

Findings

ESSENTIAL

P2-E1
- Location: Sec. 2.1, p. 2, Eq. (1) and surrounding text
- Problem: Inconsistent and undocumented expression for the field displacement. The paper states
  “Δφ ≈ fa θi (1 − J0(m/H0)/J0(0)) ≈ fa θi × O(1). For m/H0 ∼ 1, 1 − J0(1) ≈ 0.24”
  which implies Δφ/fa ≈ 0.24 θi (order unity). But two paragraphs later (Sec. 2.2) the text uses “Δφ/fa ∼ 10^-2” to obtain β ≈ 0.27°. These are inconsistent by more than an order of magnitude. Moreover, the Bessel-form expression is not derived from the ALP background equation of motion in a ΛCDM expansion (φ̈ + 3Hφ̇ + m^2 sin(φ/fa) = 0), and the claimed “precise value depends on the cosmological integration” is not demonstrated.
- Required fix: Provide a correct, transparent derivation or a controlled numerical integration of the background ALP equation in a ΛCDM background showing Δφ(z*)→Δφ(0) for m ~ H0, with all approximations stated. Remove/justify the Bessel-function ansatz. Quantify the “cosmological integration factor” as an explicit function of m/H0 with error bars. Ensure the number used to predict β = 0.27° follows from that derivation. If Δφ/fa is O(0.1–1), explain why you adopt 10^-2 elsewhere.

P2-E2
- Location: Sec. 2.2, p. 2, Eq. (2) and subsequent sentence
- Problem: From Eq. (2) β = (C0/2fa)Δφ, together with Eq. (1) as written, would imply β ≈ (C0 θi/2) × O(0.24) ≈ O(0.1) rad, i.e., many degrees, not 0.27°. The text instead introduces “Δφ/fa ∼ 10^-2” without derivation. This is a direct contradiction between Eq. (1) and the numerical estimate used to reach β ≈ 0.27°.
- Required fix: Make the prediction chain consistent. Either correct Eq. (1) and justify Δφ/fa ≪ 1, or revise the 0.27° estimate accordingly. Provide a single, traceable numerical value for Δφ/fa used in all predictions.

P2-E3
- Location: Sec. 3.2, p. 2 (end), Eq. (5)
- Problem: “The effective photon coupling parameter: fphoton × C0 = 1.73 ± 0.44.” fphoton is undefined anywhere in the paper; dimensionality is unclear; the mapping from βcombined to this quantity is not shown; and the quoted value is not consistent with any obvious combination of Eq. (2) and the measured β. With Eq. (2), defining any “effective” parameter must be explicit and unit-consistent.
- Required fix: Define fphoton unambiguously (symbol, units, and its relation to g_{aγ} = C0/fa), derive Eq. (5) from Eq. (2) with stated assumptions (which parameters are fixed/marginalized), and verify dimensional consistency. If this quantity is not essential, remove it.

P2-E4
- Location: Sec. 3.4, p. 3
- Problem: Bayes factor computed with Savage–Dickey density ratio (SDDR) using a one-sided prior β ∈ [0°, 1°]. SDDR requires the null point to be in the interior of the prior support. With a one-sided prior, β = 0 lies on the boundary; the result is not valid. Physically, β can be positive or negative; adopting a non-negative prior biases the evidence. Also, the dataset used for ln B is not stated here (it matches βobs = 0.342 ± 0.094°, not the combined 0.242 ± 0.061° used in Sec. 3.2).
- Required fix: Recompute ln B with a two-sided prior symmetric about zero, e.g., β ∈ [−B, B], and state B. Specify clearly which likelihood (βobs and σ) is used. Provide a robustness study versus prior width. If you retain a one-sided prior for a physical reason, justify it and use a Bayes factor method valid with boundary nulls.

P2-E5
- Location: Abstract p. 1; Sec. 1 p. 1; Secs. 3.2–3.4 pp. 2–3
- Problem: Multiple σ-levels are juxtaposed from different likelihoods/procedures (3.6σ from the “Eskilt et al. joint Planck+ACT analysis,” 3.9σ from your Planck+ACT Gaussian combination, and Bayes factors from yet another dataset) without consistently stating that these are not directly comparable. Instruction 7 requires explicit qualification.
- Required fix: Every time you juxtapose a σ or ln B from a different dataset/likelihood, mark explicitly that they are not directly comparable. Alternatively, standardize on a single dataset/likelihood throughout or move the others to an appendix.

P2-E6
- Location: Sec. 3.3 and Table 1, p. 3; Figs. 1–2, pp. 4–5
- Problem: MCMC methodology is insufficiently specified and statistically underpowered for the claims made. Accepted sample counts are 720–6,840; the number of chains, thinning, warm-up, and total draws are not stated. R̂ − 1 < 0.01 is reported without specifying the number of parallel chains; with such small accepted counts, R̂ can be misleading. You also use these chains for tail quantities (e.g., evidence via SDDR relies on accurate posterior density near a boundary). The prior choices also include one-sided truncations (θi ∈ [0.01, π]) that can bias products.
- Required fix: Report the full MCMC configuration: number of parallel chains, total draws per chain, warm-up, acceptance rates, thinning, and per-parameter effective sample sizes. Increase chain lengths to achieve Neff > 5×10^3 per key parameter and stable density estimates at β ≈ 0. Provide convergence diagnostics beyond R̂ (e.g., rank plots, within/between variance, IAT). Justify or revise one-sided priors (θi, β). If MCMC is only wrapping a single Gaussian summary-likelihood in β, state that directly and consider analytic posteriors.

P2-E7
- Location: Sec. 3.3 p. 3; Fig. 1, p. 4
- Problem: Inconsistency between the text and the triangle plot. The text states “Caγ × θi = 3.4 ± 1.1,” while Fig. 1 (as labeled) shows medians roughly θi ≈ 1.33 and Caγ ≈ 13.4, whose product is ≈ 17.8, not 3.4. Additionally, Caγ, C, and C0 are used interchangeably without definition, and units are not stated.
- Required fix: Unify notation (define C, C0, Caγ, and whether α/2π is absorbed), report consistent posterior summaries in text and figures, and correct the inconsistent number. Provide units or state that all “C” parameters are dimensionless anomaly coefficients.

P2-E8
- Location: Throughout; specifically Sec. 3.1 p. 2; Abstract p. 1; References p. 6
- Problem: Missing and/or improper citations. The “Eskilt et al. joint Planck + ACT analysis” giving βobs = 0.342 ± 0.094° is not listed in the references. “Namikawa et al., 2025. In preparation” is non-citable for quantitative claims.
- Required fix: Provide full bibliographic details (journal/arXiv IDs) for all quoted numerical results. Remove “in preparation” as supporting evidence; replace with published/posted sources or rephrase.

P2-E9
- Location: Sec. 3.2 p. 2–3 (Eq. 3 and combination)
- Problem: Independence assumption for combining Planck and ACT β estimates is not justified. Calibration/systematic correlations across experiments (sky overlap, foreground modeling, EB self-calibration assumptions) can induce covariance. You later mention possible common systematics in Sec. 6, but you still report a combined 3.9σ as if errors are independent and purely statistical.
- Required fix: Provide a covariance assessment between the inputs (even a conservative correlation coefficient study) and propagate it to βcombined and σcombined. Alternatively, present a range for σcombined under plausible correlations (ρ ∈ [0, 0.5]) to show robustness, and qualify the significance accordingly.

P2-E10
- Location: Sec. 2.2 p. 2; Sec. 6 p. 5; Conclusion p. 6
- Problem: The central “prediction” β ≈ 0.27° is presented as sharp without an uncertainty budget. Given that β ∝ (C0 θi/2) × I(m/H0), where I is the cosmological integration factor, and θi and C0 are O(1) but unknown, the prediction must include propagated uncertainties. Claiming “no tuning” does not remove the need for a credible interval on the prediction itself.
- Required fix: Provide a quantitative prior-based prediction for β with uncertainties, e.g., adopt priors for θi and C0 (and m/H0 within the allowed window), compute the predictive distribution p(β|model), and report median and credible intervals. Compare this predictive distribution—not a single number—to data.

MAJOR

P2-M1
- Location: Notation throughout (Secs. 2–3; Table 1; Fig. 1)
- Problem: Inconsistent notation for the photon coupling: C, C0, Caγ, and g_{aγ} appear with shifting meanings and no parameter table. “ALP (C = 8 fixed)” is used in Table 1 without defining C; later “Caγ flat on [1, 30]” appears in priors; Fig. 1 axis label reads “C_{aγ}.”
- Required fix: Provide a parameter table defining all symbols, their dimensions, and relationships (e.g., g_{aγ} = C0/fa ≡ (α/2π)(E/N − 1.92)/fa if that is intended). State explicitly whether α/2π and charge sums are absorbed into C0.

P2-M2
- Location: Sec. 3.4 p. 3
- Problem: You present ln B = 5.17 as “indicative” and later give ln B for other priors. As shown by a quick recomputation, the quoted numbers match using βobs = 0.342 ± 0.094°, not the βcombined from Sec. 3.2. This inconsistency can confuse readers.
- Required fix: State clearly which β and σ feed the Bayes factor. Provide recomputed ln B values for both the individual and combined constraints or consolidate on one.

P2-M3
- Location: Sec. 3.1 p. 2
- Problem: The ACT DR6 citation is “arXiv preprint, 2025” with no identifier; the Planck NPIPE value (0.30 ± 0.11°) is attributed to Eskilt & Komatsu (2022) but that paper quotes different combinations depending on pipeline and masking choices. The paper also mentions an “Eskilt et al. joint analysis” not in the bibliography.
- Required fix: Give exact source versions (title, arXiv ID/version, table/figure references) for every quoted number so they can be checked.

P2-M4
- Location: Sec. 3.3 p. 3
- Problem: The priors for θi and β appear to be one-sided and positive, which precludes negative rotation/misalignment. This can bias posteriors for products like C × θi and Bayes factors.
- Required fix: Use symmetric priors for signed quantities or justify a physical reason for restricting to positive values; quantify the impact on posteriors and evidences.

P2-M5
- Location: Sec. 6 p. 5 (systematics)
- Problem: While systematics are briefly discussed, the analysis does not propagate any systematic error floor into the combined constraint or Bayes factor, nor is the Minami–Komatsu self-calibration assumption stress-tested against frequency-dependent effects.
- Required fix: Add a sensitivity analysis incorporating an additive systematic error term (e.g., σsys ≈ 0.1–0.3°) into the likelihood and re-evaluate βcombined, its significance, and ln B. Clearly separate statistical vs total uncertainties.

P2-M6
- Location: Sec. 4 p. 3 (LiteBIRD forecast)
- Problem: The 9σ statement is a point-estimate significance using σ(β) ≈ 0.03° and β = 0.27°, but it ignores model parameter uncertainties (θi, C0, m) and possible systematic floors in LiteBIRD’s self-calibration. 
- Required fix: Present a forecast as a distribution (e.g., expected SNR distribution from your predictive β) and discuss the impact of a nonzero systematic floor or self-calibration choices on σ(β).

MINOR

P2-m1
- Location: Sec. 2.2 p. 2
- Problem: Units switching between radians and degrees is not always explicit. The line “β ≈ C0 θi × 5×10^-3 rad ≈ 0.27°” is fine, but earlier and later expressions in degrees are not always labeled.
- Required fix: State units for β in every equation or immediately around it, and include a brief note that all intermediate theory expressions are in radians unless otherwise noted.

P2-m2
- Location: Fig. 2 p. 5
- Problem: The figure legend includes “Observed” with a green band, but the caption does not identify which observation (which value and σ) it corresponds to.
- Required fix: Add the numerical value and reference for the “Observed” band in the caption.

P2-m3
- Location: Table 1 p. 3
- Problem: “Samples” are listed as accepted samples but no total draws are given, and no indication of the number of parallel chains is provided.
- Required fix: Clarify that these are accepted post–burn-in samples, list total draws and number of chains.

P2-m4
- Location: Abstract p. 1
- Problem: “fa ∼ MPl is the natural scale for a gravitationally coupled pseudoscalar” is a qualitative statement; some readers will expect a brief citation.
- Required fix: Add a standard reference or footnote for this heuristic (e.g., generic ALP EFT arguments).

P2-m5
- Location: Sec. 5 p. 4
- Problem: The association with the Barbero–Immirzi pseudoscalar is speculative within this paper and not used quantitatively.
- Required fix: Either move this to a short one-sentence remark with a neutral citation or to an appendix, or better, remove it to keep focus on the birefringence method.

NIT

P2-n1
- Location: Eq. (1), p. 2
- Problem: Dividing by J0(0) = 1 is redundant.
- Required fix: Remove J0(0) in the denominator.

P2-n2
- Location: References p. 6
- Problem: Some references are missing DOIs/arXiv IDs; inconsistent styles (“arXiv preprint, 2025”; “In preparation”).
- Required fix: Harmonize reference style per PRD and include DOIs/arXiv IDs where applicable.

Arithmetic checks performed

- 3.6σ from βobs = 0.342 ± 0.094°: 0.342/0.094 = 3.64σ. OK for “3.6σ”.
- Combined β from 0.30 ± 0.11° and 0.215 ± 0.074° (assuming independence): weighted mean 0.2415°, σ = 1/√(1/0.11^2 + 1/0.074^2) = 0.0614°. Significance 0.2415/0.0614 = 3.93σ. Matches text (3.9σ).
- Bayes factor via SDDR using βobs = 0.342 ± 0.094°, prior β ∈ [0°, 1°]: posterior density at 0 is 0.00564 deg^-1; prior density 1 deg^-1; ln B = ln(1/0.00564) = 5.18, matching 5.17. For βcombined = 0.242 ± 0.061°, ln B would be ≈ 6.00 with the same one-sided prior; this highlights the dataset inconsistency noted in P2-M2 and the prior issue in P2-E4.

Dimensional analysis

- L ⊃ (g_{aγ}/4) φ F F̃ implies [g_{aγ}] = mass^-1, [φ] = mass. β = (g_{aγ}/2)Δφ is dimensionless, consistent. However, the introduction of “fphoton” in Eq. (5) is dimensionally opaque (P2-E3).

Figures and tables

- Fig. 1 labels/values appear inconsistent with the text for Caγ × θi (P2-E7). Axes are labeled with units for β; provide units/definition for Caγ.
- Fig. 2 caption should state which observation the green band refers to (P2-m2).
- Table 1 lacks chain counts and total draws (P2-m3).

Bibliography

- Missing/unclear citations for quoted numbers (P2-E8). “In preparation” should not be used to support mass constraints.

Length and focus

- The paper is short (6 pages), which is appropriate for the claimed scope, but core derivations and statistical methodology need strengthening to meet PRD standards.

## Summary recommendation
MAJOR REVISIONS

Justification: The manuscript contains multiple essential methodological issues: (i) an internally inconsistent and undocumented derivation of the key displacement Δφ leading directly to the central prediction β ≈ 0.27°; (ii) an undefined “effective coupling” parameter; (iii) a Bayes factor computed with an invalid one-sided prior and inconsistent dataset usage; (iv) underpowered and underspecified MCMC with inconsistent parameter summaries; and (v) missing/unclear citations. These must be corrected and the theoretical/numerical link from model parameters to β established rigorously, with a coherent uncertainty budget and reproducible statistical pipeline, before the paper can be considered for PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eye audit)

Essential

P2-E11
- Location: Sec. 1, p. 1 (end of first paragraph after “ϕ F F˜”)
- Problem: Inconsistent coupling normalization. The introduction states β = Δϕ/(2 fa), implicitly setting C0 = 1, whereas Sec. 2.2 (Eq. 2) uses the general result β = (gaγ/2)Δϕ = (C0/2 fa)Δϕ. This inconsistency propagates into later numerical statements and obscures how C0 enters all predictions.
- Required fix: Adopt a single, explicit normalization for the photon coupling throughout. Replace the Sec. 1 expression by β = (C0/2 fa)Δϕ (or clearly state you set C0 = 1 only for that paragraph). Add a one-line Lagrangian definition so dimensions are unambiguous.

P2-E12
- Location: Sec. 3.3, p. 3 (paragraph discussing sample sizes and Neff)
- Problem: Internal inconsistency between accepted sample counts and effective sample sizes. You report accepted samples as low as 720 (Run 3), yet state “Neff ∼ 1,000.” Neff cannot exceed the number of post–burn-in draws. This undermines the credibility of tail estimates and any SDDR-based evidence statements derived from these chains.
- Required fix: Report per-parameter Neff for each run and ensure Neff ≤ number of post–burn-in draws. If Neff < 1,000 for any key parameter, extend the chains until Neff thresholds are met (see also P2-E6), and recompute all tail-sensitive quantities.

P2-E13
- Location: Sec. 3.3, p. 3 (Priors); implicit in all β inferences
- Problem: Prior excludes zero coupling and enforces positive rotation. Caγ is truncated to [1, 30], θi to [0.01, π], and in Sec. 3.4 β’s prior is one-sided and non-negative. This jointly precludes small or negative β and can inflate the apparent evidence for β ≠ 0 by construction.
- Required fix: Permit Caγ to include zero (e.g., Caγ ∈ [0, 30]) and use a sign-symmetric prior for θi (e.g., θi ∈ [−π, π]) or alternatively for β. Recompute posteriors and Bayes factors under these unbiased priors and report sensitivity.

P2-E14
- Location: Sec. 3.4, p. 3 (Bayes factor via SDDR)
- Problem: Units of β in the prior and posterior densities are not stated. SDDR requires densities with respect to a specific measure; changing between degrees and radians changes the numerical value of the density at the null and hence ln B.
- Required fix: State explicitly the parameterization and units used for β in both the prior and posterior (recommend radians). Provide ln B computed in that measure.

P2-E15
- Location: Sec. 3.1, p. 2; Sec. 3.2, p. 2–3
- Problem: Sign convention alignment for β across Planck and ACT is not documented. Combining summary estimates requires the same polarization angle sign convention and EB phase convention. This is a common pitfall in birefringence combinations.
- Required fix: State the sign conventions used in the cited Planck and ACT analyses and confirm they match your convention. If a conversion is needed, document and apply it before combining.

P2-E16
- Location: Sec. 3.3, p. 3 and overall MCMC methodology
- Problem: Missing forward model from parameters to β used inside the MCMC. The sampler explores (m, θi, Caγ), but the paper never specifies the deterministic or numerical mapping β(m, θi, Caγ) it evaluates at each draw. Without an explicit Δϕ(m, θi) model (or a stated constant surrogate), the MCMC is not reproducible and its validity cannot be assessed.
- Required fix: Specify the exact forward model used in the sampler, with equations and/or code: is Δϕ/fa taken from a numerical ΛCDM integration, an analytic approximation, or a constant (e.g., 10^-2)? Provide the dependence on m/H0 and θi, and rerun the chains if this was not implemented consistently.

P2-E17
- Location: Fig. 1 (diagonal panels) vs. Sec. 2.1–2.2
- Problem: The posterior for log10(m/eV) shown in Fig. 1 peaks around −31.4, i.e., m ≈ 4 × 10^-32 eV ≈ 27 H0, not “m ∼ H0” as used in the analytic estimate (e.g., J0(1) in Eq. (1)). If m/H0 ≫ 1, the field dynamics and the “cosmological integration factor” differ substantially from the m/H0 ≈ 1 case used to motivate β ≈ 0.27°.
- Required fix: Quantify I(m/H0) across the posterior range and update the predictive β accordingly. Reconcile the m posterior with the assumed regime used in Sec. 2 (or adjust priors to reflect the intended regime).

Major

P2-M7
- Location: Sec. 3.3, p. 3 (Priors)
- Problem: The mass prior log10(m/eV) ∈ [−35, −30] spans m/H0 ≈ 0.007–700 (for H0 ≈ 1.5 × 10^-33 eV). This contradicts the text’s premise “m ∼ H0” and mixes qualitatively distinct dynamical regimes (field begins rolling today vs. long before matter–Λ equality), directly affecting Δϕ and β.
- Required fix: Justify this wide prior physically or restrict it to the intended “m ∼ H0” regime. Provide sensitivity of results to the prior range and show how the predictive Δϕ/fa varies across it.

P2-M8
- Location: Figs. 1–2 vs. body text (Sec. 3.3, p. 3)
- Problem: Figure–text mismatch for reported β from the extended run. Fig. 1 displays β [deg] = 0.324 ± 0.099 for Run 2, but Sec. 3.3 only quotes βALP (Run 1) and βfree (Run 3), omitting the Run 2 β value from the text. This impedes verification of claims like “All three are consistent with each other,” and obscures which number underlies Fig. 2’s “Model 2b.”
- Required fix: Report in-text the Run 2 β posterior mean and uncertainty (matching Fig. 1) and ensure Fig. 2 curves are labeled with the corresponding numerical summaries.

Minor

P2-m6
- Location: Sec. 1, p. 1; Sec. 3.4, p. 3
- Problem: Units for β are not stated where formulae are first given (Sec. 1) and where priors/densities are defined (Sec. 3.4). Given later usage in degrees in plots and text, this invites ambiguity.
- Required fix: State explicitly that theoretical angles are in radians unless noted, and specify units at every place where β appears in a prior/posterior density.

P2-m7
- Location: Sec. 1 (Abstract claim), Sec. 3.1
- Problem: The sentence “Combined, the evidence exceeds 3.5σ” in Sec. 1 is a free-standing assertion with no immediate pointer to the dataset/likelihood used. Later, a specific combination yields 3.9σ from two summary estimates; the abstract also quotes 3.6σ from a different joint analysis.
- Required fix: Add immediate parenthetical citations/numbers to each σ claim in Sec. 1 and cross-reference Sec. 3.2 for the 3.9σ combination, explicitly noting the null-procedure differences.

P2-m8
- Location: Sec. 3.3, p. 3; Fig. 1
- Problem: The statement “the degeneracy between Caγ and θi is visible but does not affect the birefringence prediction” is qualitative; in fact β ∝ Caγ θi. Without quantifying the product’s posterior being prior- or data-dominated, this reads as an unsupported hedge.
- Required fix: Quantify the posterior of Caγ θi (with symmetric priors; see P2-E13), report its prior-to-posterior KLD or Bayesian complexity to demonstrate data dominance, or soften the claim.

P2-m9
- Location: Sec. 3.1, p. 2
- Problem: The value of H0 used when mapping the mass prior to m/H0 is never stated. Since several arguments hinge on “m ∼ H0,” this numeric anchor is needed for reproducibility.
- Required fix: State the numerical H0 used (e.g., in eV, s^-1, or km s^-1 Mpc^-1 and its conversion).

Nit

P2-n3
- Location: Eq. (3), p. 2
- Problem: The index set of the product in L(β) is implicit. While obvious to practitioners, it would aid reproducibility to spell out i ∈ {Planck, ACT}.
- Required fix: Add a brief note under Eq. (3) clarifying the product is over the Planck and ACT summary measurements used in Sec. 3.1.

Explanation
These issues were not covered in the initial review and arise from a second-pass audit focusing on arithmetic/internal consistency, figure-to-text alignment, dimensional/units discipline (especially for evidences), prior design impacts, and explicit specification of the forward model used in MCMC.