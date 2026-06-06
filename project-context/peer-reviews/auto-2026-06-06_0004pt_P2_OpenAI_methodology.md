# P2 auto-2026-06-06_0004pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (5431 chars)
**Wall time**: 529.2s

---

Referee report (PRD methodology)

Summary of the submission
The manuscript proposes that a spectator axion-like particle (ALP) with decay constant fa ~ MPl and mass m ~ H0 naturally predicts an isotropic CMB polarization rotation β ≈ 0.27°. The author then combines two recent birefringence measurements via a Gaussian summary-likelihood to obtain β = 0.242 ± 0.061° (3.9σ from zero), quotes a Bayes factor ln B ≈ 5.17 in favor of a nonzero rotation, presents small MCMC runs for an ALP-parameter mapping, and forecasts a LiteBIRD detection at ~9σ if β ≈ 0.27°.

While the topic is timely, there are multiple methodological inconsistencies and missing derivations that, in their current state, do not meet PRD standards. The most serious are: an internal contradiction in the core theoretical prediction for the field displacement Δφ/fa (and hence β), imprecise/ambiguous coupling normalization and notation, an undefined and dimensionally-unclear “effective photon coupling” estimator, and an unclear basis for the reported Bayes factor. The combined-constraint methodology also assumes independence of datasets without quantifying possible correlations, and the MCMC evidence presented is based on sample sizes far too small for the claims made.

Findings

ESSENTIAL

P2-E1 (Sec. 2.1–2.2; pp. 1–2): Self-contradictory prediction for Δφ/fa and β
- Offending text/equations:
  - Eq. (1), p. 2: “Δφ ≈ fa θi (1 − J0(m/H0)/J0(0)) ≈ fa θi × O(1). For m/H0 ∼ 1, 1 − J0(1) ≈ 0.24…”
  - Eq. (2), p. 2 and subsequent text: “Δφ/fa ∼ 10−2 … yielding β ≈ C0 θi × 5 × 10−3 rad ≈ 0.27°.”
- Problem: Eq. (1) implies Δφ/fa ≈ 0.24 θi for m/H0 ~ 1. With β = (C0/2)(Δφ/fa), this gives β ≈ 0.12 C0 θi rad ≈ 6.9° for C0 ~ θi ~ 1, which is two orders of magnitude larger than the 0.27° “natural prediction” claimed in Sec. 2.2. The two statements cannot both be true. Moreover, the Bessel-function form is introduced without derivation and appears ad hoc for the cosmological scalar equation of motion with time-varying H(z).
- Required fix: Provide a self-consistent, derived expression for Δφ/fa from recombination to today by solving φ¨ + 3Hφ˙ + V′(φ) = 0 (with the stated potential) in a realistic ΛCDM background. Show explicitly the m/H0 dependence and the numerical value of Δφ/fa for m ≈ H0. Remove or justify the J0(m/H0) parameterization with a derivation. Then recompute the predicted β numerically and ensure it matches the claimed 0.27° if that statement is to be retained.

P2-E2 (Sec. 2.2; throughout): Ambiguous coupling normalization; inconsistent notation for ALP–photon coupling
- Offending text:
  - “gaγ = C0/fa is the ALP-photon coupling and C0 is an order-unity coefficient from the ABJ anomaly.” (p. 2)
  - MCMC priors introduce “Caγ” (p. 3), runs fix “C = 8” (Table 1), and figures label “C_aγ” (Fig. 1).
- Problem: The manuscript never states the interaction Lagrangian with its normalization. In the standard convention, L ⊃ −(α/8π)(C_aγ a/fa) F F̃, implying gaγ = α C_aγ /(2π fa); other conventions exist but must be stated. Here, gaγ is set equal to C0/fa (omitting α/2π), yet MCMC and text oscillate between C, C0, and C_aγ. This makes all inferences about “order-unity” coefficients and the mapping from β to parameter combinations ill-defined and potentially off by ~O(10–100).
- Required fix: State the precise convention for the ALP–photon coupling in the Lagrangian (include numerical factors such as α/2π). Adopt one symbol for the dimensionless anomaly coefficient and use it consistently in all equations, tables, and figures. Recompute all parameter inferences and any “order-unity” statements under that explicit convention.

P2-E3 (Sec. 3.2; p. 2): Undefined “effective photon coupling” fphoton × C0 = 1.73 ± 0.44
- Offending text: Eq. (5): “The effective photon coupling parameter: fphoton × C0 = 1.73 ± 0.44”
- Problem: fphoton is never defined anywhere in the paper. The quoted product has no stated units, and its derivation from the likelihood for β is not shown. Because β is reported in degrees but the underlying formula uses radians, the unit handling is unclear. Numerically, 1.73 is suspiciously close to (Caγ × θi)/2 from Sec. 3.3, suggesting this is not a physically meaningful coupling but a re-labeled product of internal parameters.
- Required fix: Define fphoton unambiguously, with units, from the explicitly stated Lagrangian and β = (gaγ/2) Δφ. Show the algebra connecting the β constraint to Eq. (5), including all radian/degree conversions. If this quantity is not meaningful or duplicates Sec. 3.3 results, remove it.

P2-E4 (Sec. 3.4; p. 3): Bayes factor computation unclear and dataset-inconsistent
- Offending text: “ln B = 5.17 (indicative; prior-dependent, see Sec. 3.4).”
- Problem: The reported ln B = 5.17 corresponds to using β = 0.342 ± 0.094° (z ≈ 3.64) with a flat prior β ∈ [0°,1°], via the Savage–Dickey ratio: B10 = p(β=0)/p(β=0|data). But Sec. 3.2 establishes a different combined constraint β = 0.242 ± 0.061° (z ≈ 3.97), which would yield ln B10 ≈ 6.00 for the same prior. The manuscript does not clearly state which data vector the Bayes factor is based on, yet juxtaposes both constraints in the same section.
- Required fix: State explicitly which measurement underpins the Bayes factor and show the calculation (including the prior density and the posterior density at β=0, and any truncation effects from restricted priors). If you intend to report ln B for both the combined summary-likelihood and the single-analysis value, present both numbers side-by-side and label them clearly as such.

P2-E5 (Sec. 3.2; p. 2): Independence assumption in the summary-likelihood combination is unquantified
- Offending text: “combining the measurements under the assumption of independent errors” (Eq. 3).
- Problem: Planck and ACT observe overlapping skies, and EB-based isotropic rotation estimates can share cosmic-variance components and astrophysical modeling systematics (even if instrumental systematics differ). The independence assumption may understate the combined uncertainty.
- Required fix: Provide a quantitative argument for treating the two constraints as independent (e.g., negligible cosmic-variance contribution to the β estimator and/or disjoint methods), or introduce a correlation coefficient ρ and either (i) propagate a plausible range of ρ to the combined σ, or (ii) adopt the more conservative of the two single-experiment constraints.

P2-E6 (Sec. 3.3; Table 1; p. 3): MCMC sample sizes insufficient for quoted posteriors and parameter products
- Offending text: Table 1 lists 720–6,840 “accepted samples,” with R̂ − 1 < 0.01 and Neff ~ 1,000 stated in the text; posteriors for β and Caγ × θi are quoted with two significant digits.
- Problem: These chain lengths are too short for robust tail behavior, parameter products, and model-comparison statements, particularly with potentially non-Gaussian posteriors and degeneracies. R̂ can under-diagnose non-convergence at small N and without multiple long chains. The paper nonetheless quotes precise posteriors for β and Caγ × θi and uses them qualitatively to support “naturalness.”
- Required fix: Re-run with multiple independent chains and O(5×10^4–10^5) post–burn-in samples per configuration, report acceptance rates, ESS per parameter, and R̂ per parameter. If not feasible, remove the MCMC sections and refrain from quoting numerical posteriors for ALP parameters.

P2-E7 (Sec. 3.3; p. 3): Prior on θi excludes the null and may bias inferences
- Offending text: “Priors: θi flat on [0.01, π]”
- Problem: Excluding θi = 0 by fiat builds in a nonzero rotation within the ALP model and artificially suppresses the posterior weight near zero rotation that would otherwise be present through θi ≈ 0 and/or small C_aγ. For model comparison and “naturalness” statements this matters.
- Required fix: Include θi = 0 in the prior support (e.g., θi ∈ [0, π]) and report sensitivity of inferences to the prior (linear vs. log priors where appropriate). If you impose a physical lower bound, justify it from first principles.

MAJOR

P2-M1 (Abstract; Sec. 4; pp. 1,3): Overclaim on falsifiability
- Offending text: “LiteBIRD… will test this prediction at 9σ significance—either confirming the signal or ruling out the ALP explanation decisively.” Similar phrasing in Sec. 4.
- Problem: A null LiteBIRD result would rule out the specific O(1) parameter corner (fa ~ MPl, m ~ H0, C~O(1), θi~O(1)) that yields β~0.27°, not “the ALP explanation” broadly. Smaller C_aγ and/or smaller θi remain viable.
- Required fix: Qualify the claim to “ruling out the Planck–scale fa, H0–scale m, and O(1) coefficient/misalignment scenario” or similar precise statement.

P2-M2 (Sec. 3.1; p. 2; References p. 6): Bibliography and attribution issues
- Offending text: “βobs = 0.342 ± 0.094° from the Eskilt et al. joint Planck + ACT analysis.”
- Problem: No bibliographic entry in the reference list corresponds to a joint Planck+ACT analysis with those numbers; the listed Eskilt & Komatsu (2022) is Planck/WMAP. Provide the exact source (journal/arXiv ID) for βobs = 0.342 ± 0.094° and for ACT DR6 (Diego-Palazuelos & Komatsu, 2025) with an accessible preprint number.
- Required fix: Correct the citations, add arXiv IDs, and ensure every quoted statistic is traceable to the specified reference.

P2-M3 (Sec. 2; pp. 1–2): Replace repeated “O(1)” placeholders with computed numbers
- Problem: The text repeatedly asserts “O(1)” factors in Eq. (2) that control the final prediction without actually computing them once a background cosmology is specified. This prevents a quantitative audit of the 0.27° claim.
- Required fix: Provide the explicit numerical integration result for Δφ/fa and the resulting prefactor in β for the fiducial ΛCDM background (and show dependence on m/H0 around unity).

P2-M4 (Sec. 3.3; Table 1; Fig. 1): Unclear definition of “C=8 fixed,” sign conventions, and priors
- Problem: The parameter C used in Run 1 is never defined; Fig. 1 uses C_aγ; the text speaks of C0. Sign conventions (β ↔ −θi, coupling signs) are not discussed.
- Required fix: Define C precisely and relate it to C_aγ and C0; specify whether negative couplings/misalignment are allowed and how sign degeneracies are treated; justify the prior ranges for C_aγ (why [1,30]? why exclude [0,1)?).

P2-M5 (Sec. 3; throughout): Units consistency for β in equations versus data
- Problem: Equations use radians; data are quoted in degrees. Some derived quantities (e.g., Eq. 5) appear to mix units implicitly.
- Required fix: State a clear rule (all inference in radians) and consistently convert degrees→radians whenever plugging data into equations. Show at least one worked example.

P2-M6 (Sec. 3.2; p. 2): Explicitly compare “σ from zero” significances and Bayes factors with a caution note
- Problem: The paper presents frequentist “z-scores” and Bayes factors in nearby text without an explicit reminder that they are not directly comparable measures of evidence.
- Required fix: Add a sentence wherever both are quoted that they are not directly comparable and serve different inferential purposes.

P2-M7 (Sec. 6; p. 5): Statement “Caγ × θi = 3.4 ± 1.1 … consistent with O(1) values”
- Problem: The product 3.4 ± 1.1 is not obviously “O(1)” under the standard normalization with α factors; its interpretation depends on the missing normalization (P2-E2). As written this is not a justified “naturalness” statement.
- Required fix: Reassess after fixing P2-E2; if still large, explain why this remains “natural” in the adopted convention.

MINOR

P2-n1 (Sec. 2.1; p. 2): Trivial J0(0) in denominator
- Offending text: “J0(m/H0)/J0(0)” with J0(0)=1.
- Required fix: Remove the denominator or explain its purpose.

P2-n2 (Sec. 3.2; p. 2): Terminology
- Offending text: “Gaussian summary-likelihood analysis”
- Required fix: Clarify that this is inverse-variance weighting of independent Gaussian constraints; optionally provide the explicit weighted-mean formula used.

P2-n3 (Sec. 6; p. 5): Extraneous claims about other predictions (matter-bounce fNL = −35/8)
- Problem: Not needed for this paper and distracts from the core methodology.
- Required fix: Remove or move to a brief contextual remark without asserting quantitative forecasts unless directly supported here.

P2-n4 (Acknowledgments; p. 6): “Companion papers, submitted simultaneously”
- Problem: Ensure the present paper is self-contained; avoid depending on non-public companion analyses.
- Required fix: Verify that no essential argument relies on 2026a/2026b. If any does, move the derivations into this paper or to an accessible arXiv preprint and cite it properly.

Arithmetic and consistency checks performed
- Weighted combination of β = 0.30 ± 0.11° and 0.215 ± 0.074° yields 0.242 ± 0.061°; 0.242/0.061 = 3.97σ, consistent with the stated “3.9σ.”
- Bayes factor via Savage–Dickey with a flat prior over [0°,1°]:
  - Using β = 0.342 ± 0.094°: posterior density at 0 is ≈ 0.00564 deg−1; ln B10 = ln(1) − ln(0.00564) = 5.18 (matches 5.17).
  - Using β = 0.242 ± 0.061°: posterior density at 0 is ≈ 0.00249 deg−1; ln B10 ≈ 6.00 (not reported). The manuscript should clarify which result is being quoted.
- LiteBIRD forecast: 0.27/0.03 = 9.0σ (arithmetic ok, with the caveat of the overclaim in P2-M1).

Figures and table audit
- Table 1: “Samples” counts are far below norms for robust MCMC inference; “Converged” based on R̂ < 0.01 alone is not persuasive at these sizes.
- Fig. 1: Axes label “C_aγ” whereas text uses C or C0; notational mismatch (P2-M4).
- Fig. 2: Axis labeled β [deg]; qualitative consistency statements are plausible; however, the figure does not resolve the core theoretical inconsistency flagged in P2-E1.

Bibliography
- Eskilt & Komatsu (2022) is correctly formatted, but does not correspond to “joint Planck + ACT.” ACT DR6 (Diego-Palazuelos & Komatsu, 2025) lacks an arXiv identifier. “Namikawa et al., 2025. In preparation” is not citable for quantitative claims.

Length and scope
- The paper is short (6 pages), but given that the main theoretical prediction is currently contradictory and key statistical claims need reworking, the present length is not the main issue. After fixes, 5–7 pages should suffice.

## Summary recommendation
MAJOR REVISIONS

The manuscript addresses a timely problem, but it presently fails core PRD methodology standards. The internal contradiction in the Δφ/fa and β prediction (Eq. 1 vs. Sec. 2.2) must be resolved with a proper derivation; the coupling normalization and notation must be made consistent; the “effective photon coupling” must be defined or removed; the Bayes factor calculation must be tied unambiguously to a specified dataset; dataset independence needs justification; and the MCMC evidence should be rerun at adequate lengths or omitted. With these essential corrections and clarifications, the paper could be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

P2-E8 (Sec. 1 vs. Sec. 2.2): Inconsistent formula for β across sections
- In Sec. 1: “β = Δφ/(2 fa)”.
- In Sec. 2.2: “β = (gaγ/2) Δφ = (C0/2 fa) Δφ”.
- These are not equivalent unless C0 ≡ 1 (unstated). This is a separate inconsistency from the missing α/2π in the coupling (flagged previously). The factor-of-C0 discrepancy propagates to all “order-unity” claims and to the interpretation of figures/tables.

P2-B1 (Fig. 1 caption/body vs. plotted marginals): Product Caγ × θi numerically inconsistent with shown 1D posteriors
- Caption and Sec. 3.3 state Caγ × θi = 3.4 ± 1.1 (Run 2).
- The diagonal panels in Fig. 1 show medians roughly θi ≈ 1.33 and Caγ ≈ 13.4 (with quoted uncertainties). Their simple product is ≈ 17.8, not ≈ 3.4. Either:
  - the axis “Caγ” is not the same Caγ used in the stated product (hidden normalization), or
  - the product label/number is computed from differently normalized parameters.
- This is a direct figure–text mismatch independent of the general notation issue in the original review.

P2-E9 (Sec. 3.4): One-sided prior on β in Bayes factor is unjustified and biases evidence upward
- The SD-ratio calculation uses β ∈ [0°, 1°]. Physical β can be positive or negative; a symmetric prior (e.g., β ∈ [−1°, 1°]) is the natural choice absent external sign information.
- Switching from [0°,1°] to [−1°,1°] halves the prior density at β=0 and reduces ln B by ln 2 ≈ 0.693. This is distinct from the prior-range tests already listed; it concerns prior parity/symmetry, which is not discussed.

P2-E10 (Sec. 3.4): Unit ambiguity infects the Savage–Dickey Bayes factor
- The paper mixes radians (theory) and degrees (data plots) and never fixes the unit used for probability densities in the SD ratio. Because SD uses absolute densities p(β=0), changing units rescales densities by the Jacobian.
- If one computes with “per radian” instead of “per degree,” ln B shifts by ln(180/π) ≈ 1.144. The manuscript must explicitly define the parameterization and unit used for both prior and posterior densities in the Bayes-factor calculation.

P2-M8 (Sec. 3.3; Table 1; Figs. 1–2): Reproducibility details missing
- The sampler type (Metropolis-Hastings? HMC? ensemble?), number of chains, burn-in, thinning, proposal/covariance updates, target acceptance, random seeds, and exact data vector used are not reported. Only total “accepted samples” and a single scalar R̂ are given.
- Without these, the MCMC results cannot be independently reproduced or audited.

P2-M9 (Sec. 3.3): Prior-sensitivity on key posteriors not assessed
- Results (e.g., Caγ × θi, βALP) are presented without showing sensitivity to the chosen hard bounds log10(m/eV) ∈ [−35, −30], Caγ ∈ [1, 30], θi ∈ [0.01, π]. Given the broad mass prior and the direct degeneracy between Caγ and θi, the quoted posteriors could change materially under modest prior variations. A prior-sensitivity analysis (e.g., varying bounds, alternative priors) is needed.

P2-M10 (Sec. 2; Sec. 6): No quantitative test of cosmology dependence
- The prediction relies on the scalar’s evolution in a ΛCDM background (H(z)). No sensitivity to cosmological parameters (Ωm, h, w, etc.) is shown, yet the text claims the result is broadly robust and “independent of bounce cosmology.” Provide a calculation or scan showing how Δφ/fa (and thus β) shifts under plausible variations in ΛCDM parameters.

P2-B2 (Fig. 2 vs. Sec. 3.2–3.3): Dataset labeling ambiguity
- Fig. 2 compares posteriors and overlays an “Observed” green band at βobs = 0.342 ± 0.094°. Elsewhere the paper emphasizes the combined Planck+ACT summary-likelihood (0.242 ± 0.061°) as the headline constraint. The figure does not indicate why the combined constraint is not also shown or how the plotted curves relate to the different data choices. Add explicit labels in the figure or caption to avoid confusion.

P2-E11 (Sec. 3.2; Eq. 3): Likelihood normalization and unit choice not fixed
- The Gaussian likelihood normalization 1/√(2πσi^2) implies densities per unit of β. Nowhere is the unit fixed (degrees vs radians) for Eq. (3). This matters because the same densities are later used for the SD ratio (absolute density at β=0), compounding the ambiguity noted in P2-E10.

P2-F1 (Abstract): Claims not fully supported by body after unit/normalization clarifications
- The abstract’s “effective photon coupling fphoton × C0 = 1.73 ± 0.44” is not derived anywhere (beyond what was already flagged in the initial review). After fixing the coupling normalization and β-units used in the likelihood, this number will likely change; the abstract should be updated only after a clear, unit-consistent derivation is added.

P2-G1 (Sec. 6): Novelty/positioning claim not substantiated
- “Our contribution is … the inference framework demonstrating internal consistency.” No comparison is provided to existing inference frameworks in the cited literature (e.g., full-spectrum EB fits with explicit ALP mapping). If this is claimed as a contribution, the paper should benchmark against at least one prior analysis to demonstrate what is new.

Explanation
These items are in addition to, and do not repeat, the issues in the initial report. They arise from cross-checks of arithmetic/units in figures and equations, unit sensitivity of the Savage–Dickey evidence, figure–text numerical mismatches, and missing reproducibility and sensitivity analyses expected by PRD.