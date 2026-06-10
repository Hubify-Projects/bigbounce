# P2 auto-2026-06-08_1144pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7620 chars)
**Wall time**: 432.0s

---

Referee report on “Cosmic Birefringence from a Planck-Scale Axion-Like Particle: Predictions, Constraints, and LiteBIRD Forecasts”

Scope of review: methodology rigor, statistical validity, derivations, dimensional analysis, arithmetic/internal consistency, figure/table audit, claims vs evidence. I audited all quoted scalars, equations, figures, and tables in the 6-page manuscript.

Overall assessment: The paper contains several internal inconsistencies in the theoretical derivation for Δϕ/fa and the resulting prediction for β, undefined and conflicting parameter normalizations (C, C0, Caγ, gaγ, “fphoton”), a Bayes factor computed with an ambiguous dataset and an unconventional one-sided prior, and insufficient MCMC methodology details for the quoted posteriors. Some core results (β prediction and the mapping to “effective coupling”) cannot be reproduced from the text as written. Multiple instances place σ-based and Bayes-factor evidence statements side-by-side without an explicit “not directly comparable” qualification at the point of juxtaposition, as required. These issues must be resolved before the paper can meet PRD standards.

Findings

ESSENTIAL

P2-E1 (Sec. 2.1–2.2, pp. 1–2): Contradictory Δϕ/fa scaling and β prediction
- Offending text/equations:
  - Eq. (1): “Δϕ ≈ fa θi (1 − J0(m/H0)/J0(0)) ≈ fa θi × O(1). For m/H0 ∼ 1, 1 − J0(1) ≈ 0.24 …”
  - Sec. 2.2: “the cosmological field evolution gives Δϕ/fa ∼ 10−2 … yielding β ≈ C0 θi × 5 × 10−3 rad ≈ 0.27°.”
- Problem: Eq. (1) implies Δϕ/fa ≈ 0.24 θi (i.e., O(10−1)), whereas the text immediately uses Δϕ/fa ∼ 10−2 to obtain β ≈ 0.27°. These differ by a factor ≳ 20 and lead to incompatible β predictions. No derivation is provided to justify either approximation.
- Required fix: Provide a correct, fully specified derivation or numerical integration for Δϕ/fa across radiation, matter, and dark-energy eras for m ~ H0, including initial conditions and the potential nonlinearity (1 − cos(ϕ/fa)). Report the resulting Δϕ/fa (with uncertainty) and propagate it to β with units made explicit. Remove one of the incompatible scalings and update all dependent numbers (including the “natural” 0.27° prediction) accordingly.

P2-E2 (Notation/definitions, throughout; especially Secs. 2.2, 3.2, 3.3; Table 1; Figs. 1–2): Inconsistent and undefined coupling parameters
- Offending items: simultaneous use of C, C0, Caγ, gaγ, “C aγ”, and “fphoton × C0”; Table 1 “ALP (C = 8 fixed)”; Run 2 prior “Caγ flat on [1, 30]”; Eq. (2) with gaγ = C0/fa.
- Problem: The paper uses multiple symbols for the anomaly/coupling with no clear, consistent definition or mapping to the standard axion–photon coupling gφγγ (dimension [energy]−1). “C = 8 fixed” contradicts “C0 ∼ O(1)” earlier and is not justified physically. “fphoton × C0” is undefined and dimensionally unclear. “Caγ × θi = 3.4 ± 1.1” in Sec. 3.3 appears unrelated to Eq. (5) “fphoton × C0 = 1.73 ± 0.44.”
- Required fix: Define a single, standard parameterization (e.g., L ⊃ −(1/4) gφγγ φ F F~ with gφγγ = αEM C/(2π fa)). State whether C is an anomaly coefficient (dimensionless) and what numerical normalization is used. Explicitly define Caγ and “fphoton,” or remove/replace with gφγγ and θi. Explain and justify “C = 8” (origin, literature basis) or change to a consistent O(1) value and recompute results. Ensure all reported products (e.g., Caγ × θi) map unambiguously to β = Δφ/(2 fγ) with correct units.

P2-E3 (Sec. 3.4, p. 3; Abstract p. 1): Bayes factor dataset ambiguity and one-sided prior
- Offending text: “ln B = 5.17 … computed via Savage-Dickey … prior β ∈ [0°, 1°]. … ln B = 4.48 for [0°, 2°], ln B = 5.86 for [0°, 0.5°].”
- Problem: The stated ln B = 5.17 matches a Gaussian posterior with β = 0.342 ± 0.094° (Eskilt joint analysis), not the summary-likelihood combined constraint in Eq. (4) (0.242 ± 0.061° would give ln B ≈ 5.99). The dataset/posterior used for SD ratio is not specified. Additionally, a one-sided prior β ∈ [0°, …] is unconventional for a signed rotation and inflates ln B by ln 2 relative to a symmetric prior. The paper elsewhere juxtaposes 3.6σ, 3.9σ, and ln B without an explicit “not directly comparable” qualifier at the point of juxtaposition (e.g., Abstract).
- Required fix: Specify exactly which posterior underlies the SD ratio and recompute ln B consistently for that posterior. Justify the one-sided prior; alternatively, use a symmetric prior β ∈ [−βmax, βmax] and report sensitivity to prior width. At every location where σ-based detection significances and Bayes factors are presented side-by-side, add an explicit statement that they are not directly comparable.

P2-E4 (Sec. 3.3, Table 1, p. 3; Fig. 1): MCMC methodology inadequate to support quoted posteriors
- Offending items: “Samples: 720–6840 accepted; R̂ − 1 < 0.01; Neff ∼ 1000;” no chain count, warm-up, autocorrelation, thinning, or likelihood definition for the ALP model is provided.
- Problem: The sample sizes are far below norms for tail and evidence estimation, yet posteriors with two significant digits are reported, and convergence is claimed from R̂ − 1 values without specifying number of chains, chain lengths, warmup, and autocorrelation times. The ALP likelihood mapping from parameters (m, θi, coupling) to β is not specified beyond a schematic; no numerical implementation or priors on nuisance/systematics are documented.
- Required fix: Provide full MCMC details: number of chains, total iterations, warm-up, acceptance rates, autocorrelation times, effective sample sizes for all parameters, and diagnostics plots. Define the likelihood used to connect parameters to β, including the cosmological integration and any approximations. Increase the chain lengths to achieve robust Neff (≥ 10^4 for key parameters) and re-report posteriors with justified precision.

P2-E5 (Sec. 3.2, p. 2; Eq. 3–4): Independence assumption in summary-likelihood combination unsubstantiated
- Offending text: “combining the measurements under the assumption of independent errors.”
- Problem: The Planck and ACT birefringence estimators may have non-negligible correlations (overlapping sky, similar self-calibration assumptions, foreground models). Without a covariance estimate, the 3.9σ combined significance could be overstated.
- Required fix: Provide a justification for treating the two measurements as independent (e.g., disjoint sky, pipeline independence), or include an estimated correlation coefficient and propagate it to βcombined and σ(β). At minimum, present sensitivity of βcombined and its significance to plausible correlation values (e.g., ρ = 0.2–0.5).

P2-E6 (Sec. 2.1, p. 1–2): Unmotivated Bessel expression for Δϕ and missing derivation
- Offending text: Eq. (1) with Bessel J0(m/H0) and the comment that “the precise value depends on the cosmological integration.”
- Problem: No derivation is provided for the Bessel form or why J0(0) appears; the equation lacks the explicit dependence on the expansion history and initial conditions. As written, it suggests Δϕ/fa ≈ 0.24 θi for m/H0 = 1, which contradicts the later 10−2 estimate (see P2-E1).
- Required fix: Either provide a complete derivation (with assumptions) for Eq. (1), or replace Eq. (1) with a rigorous integral expression and a numerical evaluation in ΛCDM for m ~ H0, including uncertainties. Use that result consistently throughout.

P2-E7 (Sec. 3.2, p. 2; Eq. 5): “Effective photon coupling fphoton × C0 = 1.73 ± 0.44” is undefined
- Offending text: Eq. (5) and surrounding sentence.
- Problem: “fphoton” is not defined anywhere; dimensionality is unclear; the mapping from β to this product is not shown. Its numerical value conflicts by a factor ~2 with “Caγ × θi = 3.4 ± 1.1” (Sec. 3.3), suggesting an unarticulated factor of 1/2 or an “O(1)” cosmological integral has been folded in without documentation.
- Required fix: Define “fphoton” precisely (units, relation to fa and gφγγ), show the algebra that maps βcombined to this parameter (including any factors of 1/2 and Δϕ/fa), and align it with the quantity inferred in Sec. 3.3. If they are different quantities, rename and clarify both and explain their relation.

P2-E8 (Table 1 and Sec. 3.3, p. 3): Unjustified choice “C = 8 fixed” and prior “Caγ ∈ [1, 30]”
- Offending text: Table 1 “ALP (C = 8 fixed)”; Priors paragraph.
- Problem: No physical or literature basis is given for C = 8. It conflicts with prior statements “C0 is order unity,” and it crucially sets the amplitude of β. The free-parameter prior “Caγ ∈ [1, 30]” is also unsupported.
- Required fix: Justify the normalization and value of C (cite standard anomaly coefficients and how C maps to gφγγ). If the intention is to approximate E/N for a QCD-like axion, state so and use consistent normalization; otherwise, adopt a physically motivated prior centered on O(1). Re-run inferences accordingly.

P2-E9 (Abstract p. 1; Sec. 4 p. 3): LiteBIRD 9σ forecast lacks methodological caveats
- Offending text: “σ(β) ≈ 0.03° … test this prediction at 9σ significance—either confirming … or ruling out … decisively.”
- Problem: The 0.03° figure depends critically on instrument polarization-angle calibration and the adopted self-calibration strategy; this is acknowledged later (Sec. 6) but not in the Abstract or Sec. 4 where the 9σ claim is made.
- Required fix: In Abstract and Sec. 4, explicitly state that the 9σ forecast assumes the stated LiteBIRD noise/systematics budget and a validated self-calibration method with negligible residual angle systematics. Provide a citation and clarify whether the 0.03° is statistical only or includes systematics.

P2-E10 (Units; multiple locations): Mixed degrees and radians without explicit conversion
- Offending items: Eq. (2) evaluates β in radians, then states “≈ 0.27°”; later priors and Bayes factors are in degrees.
- Problem: Unit switches are not annotated; this can cause confusion, especially in Eq. (2) and in the Bayes factor where densities depend on units.
- Required fix: State clearly when β is in radians vs degrees. In all likelihoods and priors used for inference and Bayes factors, specify units and ensure densities are computed consistently.

P2-E11 (Abstract p. 1; Sec. 6 p. 5): Overclaim of “no fine-tuning” relies on inconsistent Δϕ/fa
- Offending text: “This setup naturally produces β ≈ 0.27° … without any fine-tuning.”; “All input parameters … at their natural scales. No tuning is required.”
- Problem: Given the inconsistency between Δϕ/fa ≈ 0.24 θi from Eq. (1) and Δϕ/fa ∼ 10−2 used to obtain 0.27°, the “natural” prediction claim is not substantiated. Depending on the correct Δϕ/fa, obtaining β ∼ 0.27° may require θi C0 or other factors to be small.
- Required fix: Once Δϕ/fa is consistently derived, reassess whether β ≈ 0.27° follows without tuning and quantify the dependence on θi and C (or gφγγ). If mild tuning is required, state it.

MAJOR

P2-M1 (Figs. 1–2, pp. 4–5): Missing details on contours and likelihoods plotted
- Problem: The confidence levels associated with the shaded contours in Fig. 1 (e.g., 68/95%) are not stated. For Fig. 2, the plotted curves are not fully specified (kernel density estimation bandwidths, posterior source).
- Required fix: Add to captions: the confidence levels for contours; which posterior each curve corresponds to; kernel choices; and the datasets/priors used.

P2-M2 (Sec. 3.2, p. 2; Eq. 4): Combined β significance vs. Eskilt joint estimate juxtaposed without warning
- Problem: The paper quotes both 0.242 ± 0.061° (3.9σ) from a two-point combination and 0.342 ± 0.094° (3.6σ) from a joint EB analysis. These are derived from different estimators and are not directly comparable, yet are discussed side-by-side in the Abstract and body without explicit caution at those points.
- Required fix: Explicitly state at each juxtaposition that these estimates are based on different pipelines/assumptions and are not directly comparable. Prefer one estimator as primary and demote the other to a cross-check.

P2-M3 (Sec. 2.2, p. 2): “O(1)” cosmological factor left unspecified
- Problem: Eq. (2) uses “≈ C0 θi/2 × O(1).” Without a defined integral or numerical value (with uncertainty), the prediction cannot be reproduced.
- Required fix: Replace “O(1)” with an explicit function I(m, cosmology) and provide its numerical value (with uncertainty) for the fiducial cosmology and mass prior, then propagate to β.

P2-M4 (Sec. 3.3, p. 3): Prior choices for log10(m/eV) and θi not justified
- Problem: Flat priors θi ∈ [0.01, π] and log10(m/eV) ∈ [−35, −30] are asserted without motivation. For m ~ H0, the choice of prior window impacts β predictions and posteriors.
- Required fix: Justify the prior ranges physically and via literature. Provide sensitivity of the posteriors to reasonable prior variations.

P2-M5 (Sec. 6, p. 5): “Sharp falsifiability” claim lacks predictive distribution
- Problem: The model “predicts” β ≈ 0.27° while admitting unknown θi and anomaly normalization. There is no prior-predictive distribution shown for β under the stated priors.
- Required fix: Present the prior-predictive distribution of β (given priors on θi, m, and coupling), report its mean/median and credible interval, and then discuss LiteBIRD forecast power relative to that distribution rather than a single nominal value.

MINOR

P2-m1 (Sec. 3.4, p. 3): SD ratio implementation details missing
- Required fix: State explicitly whether the posterior used in SD is truncated to the same prior bounds and how truncation normalization is handled.

P2-m2 (Sec. 3.3, p. 3): Numerical precision vs. Neff
- Problem: Reporting βALP = 0.336 ± 0.107° with small chains invites overprecision.
- Required fix: Round uncertainties and central values to reflect effective sample sizes (and rerun with longer chains per P2-E4).

P2-m3 (Sec. 1, p. 1; citations): “ACT DR6 analysis confirmed the signal at comparable significance”
- Required fix: Provide the exact ACT DR6 value and uncertainty with a complete citation (arXiv ID). “arXiv preprint, 2025” is insufficient; include an identifier or clearly mark as “in prep.” and avoid relying on it for key numbers.

P2-m4 (Throughout): Define H0 numerically and units
- Required fix: State H0 value/unit used when introducing m ∼ H0 (e.g., H0 ≈ 1.5 × 10−33 eV).

P2-m5 (Sec. 7, p. 6): “No external funding” and “consumer hardware” statements
- Required fix: These are not required for PRD and can be omitted unless journal policy requests them.

NITS

P2-n1 (Eq. 1, p. 2): J0(0) = 1
- Required fix: Remove the redundant division by J0(0) to avoid confusion.

P2-n2 (Notation, various): Use consistent symbols for the same quantity
- Required fix: Harmonize β vs. α if you prefer one; avoid switching symbols in prose.

P2-n3 (Typography, multiple): En dashes vs minus signs in fNL = −35/8 and R̂ − 1
- Required fix: Ensure consistent typographic minus signs.

Arithmetic and consistency checks performed

- Weighted combination of β = 0.30 ± 0.11° and 0.215 ± 0.074° gives 0.2416 ± 0.0614°, significance 3.94σ. Eq. (4) is arithmetically consistent.
- Bayes factor ln B with β = 0.342 ± 0.094° and prior width 1° gives ln B ≈ 5.18; reported 5.17 is consistent. With β = 0.242 ± 0.061°, ln B ≈ 5.99 (not reported). The manuscript must specify which posterior was used (P2-E3).
- 5 × 10−3 rad = 0.2865°, close to 0.27°, but the stated Δϕ/fa ∼ 10−2 contradicts Eq. (1) (P2-E1).
- “9σ” forecast: 0.27°/0.03° = 9.0 is arithmetically correct.

Length and scope

At 6 pages, the paper is compact. The issue is not length but methodological rigor and internal consistency. Once the essential issues are addressed, the length appears appropriate.

Summary recommendation
MAJOR REVISIONS

Given the core inconsistencies in the Δϕ/fa derivation and β prediction, undefined/conflicting coupling normalizations, ambiguous Bayes factor computation and prior choice, and insufficient MCMC methodology disclosure for the quoted posteriors, the manuscript does not yet meet PRD methodological standards. Substantial revisions with corrected derivations, clarified parameterization and priors, reproducible inference details, and consistent evidence reporting are required. If these are resolved and the numerical results updated accordingly, the paper could then be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (second-pass audit)

P2-E12 (Sec. 2.2; global): Nonstandard axion-photon normalization silently assumed; prediction off by ~3 orders of magnitude under standard convention
- Issue: The paper takes gaγ = C0/fa and β = (gaγ/2) Δφ, effectively using L ⊃ −(1/4)(C0/fa) φ F F~. In the standard axion convention, gφγγ = (αEM/2π)(C/fa), so β = (αEM/4π) (C Δφ/fa). For fa ≈ MPl and a representative Δφ/fa ≈ 10−2, the standard prediction is β ≈ (α/4π)×10−2 ≈ 5.8×10−6 rad ≈ 0.00033°, not 0.27°. The manuscript’s 0.27° “natural” value relies on dropping the α/2π suppression (equivalently, setting C0 ≈ 2π/α ≈ 860 by fiat), while still calling C0 “order unity.”
- Why it matters: This is not a notation quibble; it changes the predicted rotation by ~2π/α ≈ 860. The central claim that a Planck-scale ALP “naturally” gives β ≈ 0.3° hinges entirely on this nonstandard normalization.
- Required fix: Adopt a single, explicit coupling convention. If you intend L ⊃ −(α/8π)(C/fa) φ F F~, carry α/2π consistently through Eq. (2) and all inferences, and update every number (β prediction, “effective coupling,” posteriors). If you intentionally use a nonstandard direct 1/fa coupling, state this up front, quantify how it differs from the standard by 2π/α, and justify it physically (with citations). Reassess the “no fine-tuning” claim under the standard normalization.

P2-E13 (Fig. 1 vs text, Sec. 3.3): Product Caγ × θi quoted in text conflicts with values visible in the figure by a factor ~5
- Observation: From Fig. 1 overlays: θi ≈ 1.33 and Caγ ≈ 13.4 (median annotations). Their product is ≈ 17.8, but the text states “Caγ × θi = 3.4 ± 1.1.” This discrepancy is far larger than uncertainties.
- Likely cause: A hidden normalization/factor (e.g., α/2π, 1/2, or an “O(1)” cosmological integral) has been folded into one of these quantities without being stated, or the figure label Caγ is not the same Caγ used in the text.
- Required fix: Define unambiguously what Caγ is in the figure and in the text; show the exact mapping between plotted parameters and the “product” reported. If a normalization factor is included, state it explicitly and correct all occurrences. Replot Fig. 1 if necessary.

P2-E14 (Sec. 2.1 vs Fig. 1): Posterior mass scale implies rolling begins at z ≫ 1, contradicting the narrative “begins rolling at z ∼ 1”
- Observation: Fig. 1 shows log10(m/eV) ≈ −31.4 ± 1.5. Using H0 ≈ 1.5 × 10−33 eV, the posterior median has m/H0 ≈ 27. Solving H(zroll) = m for ΛCDM (Ωm ≈ 0.315, ΩΛ ≈ 0.685) gives zroll ≈ [(m/H0)^2 − ΩΛ]1/3 / Ωm1/3 − 1 ≈ 12, not O(1).
- Problem: The text repeatedly asserts “m ∼ H0 … begins rolling at z ∼ 1.” The posterior (as shown) actually favors m ≫ H0 (rolls well before z = 1), and this is neither acknowledged nor reconciled.
- Required fix: Report the inferred distribution of zroll from the posterior and update the narrative accordingly. If you intend to force m/H0 ≈ 1, constrain the prior accordingly and rerun. Otherwise, revise the “rolling at z ∼ 1” statements.

P2-E15 (Sec. 3.3; Table 1): Effective sample size vs accepted samples inconsistent
- Observation: You report “accepted samples 720–6,840” and also “Neff ∼ 1,000.” For Run 3 (720 accepted), Neff cannot exceed the total post-warmup draws per parameter. The relationship between “accepted,” total iterations, thinning, and Neff is not specified, so this is unverifiable and likely inconsistent for at least one run.
- Required fix: Provide, for each run: number of chains, total iterations, warm-up, acceptance rate, autocorrelation time, and per-parameter Neff. Ensure Neff ≤ total post-warmup draws (post-thinning) and correct any overstatements.

P2-E16 (Sec. 3.3; priors): One-sided θi and positive Caγ priors force β > 0, biasing evidence and posteriors
- Observation: θi ∈ [0.01, π] and Caγ ∈ [1, 30] (both nonnegative) imply β ≥ 0 under your mapping, mirroring the one-sided β prior used in the Bayes factor. This compounds prior-induced evidence inflation and prevents testing the sign of rotation.
- Required fix: Use symmetric sign priors (e.g., θi ∈ [−π, π] and/or allow Caγ to be signed, or equivalently adopt a signed β in the mapping) and report sensitivity of posteriors and ln B to these choices. Justify any one-sided restriction physically if retained.

P2-M6 (Sec. 6; novelty): Claimed “contribution” overlaps published results without a clear, supported novelty statement
- Observation: You state the contribution is the “specific parameter identification (fa ∼ MPl, m ∼ H0)” and an “inference framework demonstrating internal consistency.” Fujita et al. (2021) already studied Planck-scale ALPs and β ∼ 0.3°, including m ∼ H0 dark-energy-scale masses. Your inference framework has unresolved inconsistencies (this and prior report).
- Required fix: Precisely delimit what is new relative to Fujita et al. 2021 and related works (e.g., any new dataset combination methodology, priors, or parameter mappings), or soften the novelty claim.

P2-M7 (Fig. 2 vs priors; Secs. 3.3–3.4): Sign handling inconsistent between plotted “β free” and one-sided priors used for ALP and Bayes factor
- Observation: Fig. 2 shows curves over β ∈ [−0.1°, 0.8°] and includes a “Model 0: beta free” curve that appears two-sided, while the ALP runs and Bayes factor employ one-sided priors for β (and for the underlying parameters, per P2-E16).
- Required fix: State explicitly which priors generated each curve in Fig. 2 and align sign conventions across analyses. If different, explain why and how that affects comparability.

P2-m6 (Abstract/Sec. 3.3/Refs): Missing citation for the “Eskilt et al. joint Planck + ACT analysis” used for βobs = 0.342 ± 0.094°
- Observation: The manuscript relies on a “joint Planck + ACT” βobs but the references list only Eskilt & Komatsu (2022, WMAP+Planck). No bibliographic entry (journal/arXiv ID) is given for the joint Planck+ACT analysis.
- Required fix: Provide a complete citation (authors, year, arXiv ID/DOI) for the joint analysis or clearly mark it “in prep.” and avoid relying on it for primary numerical claims.

P2-m7 (Sec. 2.1): Self-contradictory phrasing around 1 − J0(1)
- Observation: The text states “For m/H0 ∼ 1, 1 − J0(1) ≈ 0.24; the precise value depends on the cosmological integration…” The value 1 − J0(1) is a pure number (≈ 0.235) and does not depend on cosmology. If the intent is that a different integral, not equal to 1 − J0(1), depends on cosmology, this needs to be clarified.
- Required fix: Correct the statement to distinguish the mathematical constant from any cosmology-dependent integral, or remove the Bessel form per P2-E6 from the first review.

P2-m8 (Sec. 4; Abstract): “decisively rule out the ALP explanation” overreach given free θi and coupling
- Observation: Even if LiteBIRD finds β = 0 ± 0.03°, broad classes of ALP models (including your own with smaller θi×C) remain viable. Without a prior-predictive distribution (see P2-M5 in the first review), “decisively rule out” is too strong.
- Required fix: Rephrase to specify what subset of parameter space would be excluded (e.g., θi×C above some threshold), and quantify that region under your stated priors.

Explanation for omissions from first-pass
- These issues emerged from a stricter arithmetic/figure-to-text reconciliation (P2-E13, E15), a normalization check against the standard axion literature (P2-E12), a consistency check between posterior medians and the narrative (P2-E14), and a sign-prior audit across figures and evidence claims (P2-E16, M7). They were not fully exposed in the initial review’s broader coupling-notation and MCMC-details critiques.