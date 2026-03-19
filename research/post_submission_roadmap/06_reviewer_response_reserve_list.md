# Reviewer Response Reserve List

**Created:** 2026-03-19
**Purpose:** Pre-assembled responses to likely referee criticisms of the focused PNG paper, with pointers to supporting evidence in the repo.

---

## Likely Criticism 1: "f_NL = -35/8 is just one paper's result (Cai et al.)"

**Reserve response:**

We independently audited the Cai et al. calculation at `research/cai_action_audit/`. Three implementation mismatches between our initial calculation and Cai's were identified and fully resolved:
- Leading vertex coefficient: epsilon^2 vs (epsilon^2 - epsilon^3/2), producing a factor-4 difference at epsilon = 3/2
- Mode function phase convention: e^{-iketa} vs e^{+iketa}, producing a sign flip
- Chi-sector structure: completely different terms and a-dependence

After correcting to Cai's conventions, the shape function A_T reproduces all three special-case limits exactly:
- Squeezed (k1 -> 0): f_NL = -35/8
- Equilateral (k1 = k2 = k3): f_NL = -255/64
- Folded (k1 = 2k2 = 2k3): f_NL = -9/4

Additionally, SymPy symbolic verification at `research/fnl_symbolic_cancellation/` independently confirmed the first four Maldacena terms sum to f_NL(T1-T4) = 35/16, matching Li-Brandenberger (2016) to 0.07%. The gradient expansion at `research/gradient_expansion_fnl_derivation/` confirms structural features (negative, O(1), local, parameter-free) from an independent formalism.

**Strength:** STRONG. Three independent verification methods converge.

---

## Likely Criticism 2: "GR projection contaminates your forecast"

**Reserve response:**

We have quantified this in detail at `research/gr_contamination_claim_hardening/` and `research/ultra_large_scale_systematics_audit/`.

GR projection effects (relativistic corrections to galaxy clustering at ultra-large scales) contribute an effective f_NL^GR ~ 1-2 to the measured signal. Our treatment:
- Full GR marginalization modeled with sigma_GR = 0.3 (optimistic) to 1.0 (conservative)
- SPHEREx significance after GR marginalization: drops from ~8 sigma to 4-6 sigma
- MegaMapper significance after GR marginalization: drops from ~12 sigma to 3-7 sigma
- The paper presents post-marginalization numbers as PRIMARY claims (not the pre-marginalization headlines)
- Bayes factor against standard inflation AFTER GR marginalization: > 329:1 (from 500K MC samples)

The bispectrum channel (SPHEREx) is less affected than the scale-dependent bias channel because GR projections primarily affect the power spectrum.

**Strength:** STRONG. Conservative treatment already in the paper.

---

## Likely Criticism 3: "Why not just use inflation with tuned f_NL?"

**Reserve response:**

Detailed at `research/inflation_mimicry_deep_comparison/` and `research/bayesian_discrimination_program/`.

To produce f_NL^local ~ -4.4 from inflation requires:
- Standard single-field slow-roll: EXCLUDED. f_NL = O(epsilon, eta) ~ 10^{-2}. Bayes factor > 10^8 against.
- Non-attractor inflation: wrong sign (produces positive f_NL for generic initial conditions) and transition-sensitive. Not a natural outcome.
- Multifield inflation: CAN produce negative O(1) f_NL, but requires 2+ tuned parameters (field-space curvature, turn rate). The Bayesian comparison penalizes this: bounce (0 parameters) vs multifield (2+ parameters) gives Bayes factor 11-57 favoring bounce across all reasonable priors.
- The Suyama-Yamaguchi inequality (tau_NL >= (6/5 f_NL)^2) provides an additional discriminator: the matter bounce saturates this bound, while multifield inflation generically violates it in the detectable direction.

The zero-parameter nature of the bounce prediction is the hardest feature to mimic. Inflation must TUNE to -35/8; the bounce PREDICTS it from dynamics alone.

**Strength:** STRONG. Quantitative Bayes factors, prior-robust.

---

## Likely Criticism 4: "Your model is just LCDM + one parameter -- how is it different?"

**Reserve response:**

Detailed at `research/project_viable_bounce_model_pass2/`.

The Wilson-Ewing model has 0 extra fields beyond LCDM and 1 extra parameter (epsilon = 0.003, the departure from exact dust). But the key distinction:

- f_NL = -35/8 is PARAMETER-FREE. It follows from the equation of state w = 0 during contraction, not from epsilon. The prediction is the same whether epsilon = 0.001 or epsilon = 0.01. It is a kinematic consequence of matter-dominated contraction, analogous to how n_s ~ 1 follows kinematically from slow-roll inflation.

- By contrast, inflation's f_NL is slow-roll suppressed: f_NL ~ O(epsilon, eta) ~ 10^{-2}. To get f_NL ~ -4, inflation needs additional sectors with tuned parameters.

- The model's other predictions (n_s ~ 0.97, r ~ 10^{-4}) are set by epsilon and the LQC dressed-metric formalism. These are consistent with Planck but not distinctive. The distinctive prediction is f_NL = -35/8, and it comes for free.

**Strength:** MODERATE. The epsilon parameter is needed for spectral tilt, but f_NL is genuinely parameter-free.

---

## Likely Criticism 5: "What about the Li-Brandenberger discrepancy?"

**Reserve response:**

Detailed at `research/fnl_discrepancy_resolution/` and `research/cai_action_audit/`.

Li-Brandenberger (2016) report f_NL = -35/16 = -2.1875. Cai et al. (2009) report f_NL = -35/8 = -4.375. The discrepancy is a factor of 2.

Our audit diagnosed this as a convention/implementation difference in the mode function:
- Cai uses u_k proportional to zeta_k^* (complex conjugate), making the bispectrum superhorizon-dominated
- Li-Brandenberger use a different mode normalization that produces horizon-crossing dominance
- In the superhorizon-dominated regime, all six cubic action terms contribute; in the horizon-crossing regime, only Terms 1-4 contribute

The physical f_NL is -35/8 (Cai's convention), which is the superhorizon-dominated result appropriate for local-type non-Gaussianity.

Even if Li-Brandenberger's -35/16 were correct:
- SPHEREx at sigma = 1.0 still detects at 2.2 sigma
- MegaMapper at sigma = 0.5 still detects at 4.4 sigma
- The Bayes factor against standard inflation remains > 10^6

The paper acknowledges both values and presents forecasts for both. The science case survives either way.

**Strength:** STRONG. Full audit trail, forecasts for both values.

---

## Likely Criticism 6: "ECH is in the title of your other paper -- is this ECH-specific?"

**Reserve response:**

Detailed at `research/ech_bispectrum_gate/` and `research/ech_tensor_gate/`.

No. The focused PNG paper is explicitly NOT about ECH-specific signatures. The ECH bounce is perturbation-transparent: for scalar field matter, zero spin -> zero torsion -> Holst term is topological -> no perturbation-level corrections at any order. This is a mathematical identity, not an approximation.

The f_NL = -35/8 prediction is generic to ANY matter bounce with:
- Standard GR during contraction
- Bunch-Davies vacuum
- Single canonical scalar field
- w = 0 equation of state

ECH (and LQC) provide the bounce mechanism that resolves the singularity. The observable comes from the contraction dynamics, which are classical and model-independent. The focused PNG paper claims this generality explicitly.

**Strength:** STRONG. The paper makes no ECH-specificity claim.

---

## Likely Criticism 7: "Where's the LQC bounce transfer at third order?"

**Reserve response:**

Detailed at `research/lqc_specific_openings_audit/02_lqc_specific_openings.md`.

Observable modes have k/k_LQC ~ 10^{-56}. The bounce lasts approximately one Planck time. A mode that is 10^{56} times larger than the bounce scale experiences the bounce as an instantaneous event. The correction to f_NL from the bounce transfer is of order (k/k_LQC)^2 ~ 10^{-112}, which is zero to any measurable precision.

More precisely: the f_NL is generated during the contraction phase (when modes are superhorizon and the universe is matter-dominated). The bounce merely maps pre-bounce superhorizon modes to post-bounce superhorizon modes. For k << k_LQC, the mapping is trivially T_3(k) = 1 + O(k/k_LQC)^2.

The power spectrum transfer through the LQC bounce HAS been computed (Wilson-Ewing 2013, arXiv:2405.12296) and is indeed T_2(k) ~ 1 for superhorizon modes. The bispectrum transfer inherits this property.

We acknowledge this as an uncomputed but almost certainly trivial quantity. A full third-order LQC perturbation calculation is a multi-month effort that would confirm T_3 = 1 to 10^{-112} precision -- not a productive use of resources.

**Strength:** MODERATE. Physically compelling argument but not formally proven.

---

## Likely Criticism 8: "SPHEREx won't actually achieve sigma(f_NL) ~ 1"

**Reserve response:**

Detailed at `research/forecast_hardening_program/` and `research/survey_realism_reconciliation/`.

We present a degradation analysis covering the full range:

| Scenario | sigma(f_NL) | Significance | Assumption |
|----------|-------------|-------------|------------|
| SPHEREx design | 0.5 | 8.75 sigma | Perfect multi-tracer |
| SPHEREx realistic | 1.0 | 4.4 sigma | Moderate photo-z degradation |
| SPHEREx conservative | 2.0 | 2.2 sigma | Significant photo-z issues |
| SPHEREx pessimistic | 3.0 | 1.5 sigma | Severe degradation |

The paper uses the REALISTIC scenario (sigma = 1.0, 4.4 sigma) as the primary claim, not the design goal. Even in the conservative scenario (sigma = 2.0), the detection is at 2.2 sigma -- marginal but non-trivial.

The bispectrum channel from SPHEREx (Dore et al. 2014, arXiv:2311.13082) provides an alternative to scale-dependent bias. The bispectrum sigma is ~0.7, potentially better than the power spectrum SDB approach, because it is less affected by large-scale systematics.

Additionally: even if SPHEREx underperforms, MegaMapper (if built) provides a follow-up at 3-7 sigma with spectroscopic redshifts (no photo-z degradation). The two-survey strategy provides resilience against single-survey failure.

**Strength:** STRONG. Conservative numbers already in the paper. Two-survey strategy.

---

## Quick Response Work Needed (if requested by referee)

| Task | Effort | Likelihood Needed |
|------|--------|------------------|
| Explicit mode-coupling calculation through LQC bounce | ~1 week computational | LOW (OOM argument should suffice) |
| Updated forecast with specific SPHEREx data release parameters | ~1 day | MEDIUM (if SPHEREx publishes updated specs) |
| Comparison table with Planck 2024 f_NL constraints | Already in draft | HIGH (referees expect this) |
| Extended Fisher scan over (b1, sigma_z, k_min, N_tracer) | ~2-3 days | MEDIUM |
| Explicit Suyama-Yamaguchi check for Wilson-Ewing model | ~1 day | LOW |
| Supplementary appendix with full shape function derivation | ~2-3 days (compilation) | MEDIUM |

---

## Response Strategy

**Principle:** Never argue. Agree with the concern, point to existing quantitative analysis, and show the paper already addresses it.

- If the referee says "your number might be wrong": point to the 3-method verification chain.
- If the referee says "your forecast might be optimistic": point to the degradation analysis and conservative primary claims.
- If the referee says "inflation can do this too": point to the Bayes factors and the zero-parameter argument.
- If the referee says "you haven't proven X": agree, state it as a limitation, and cite the OOM argument showing it does not affect the conclusions.

**Never claim more than the evidence supports.** The paper's strength is its honesty: clear caveats, conservative primary claims, explicit degradation analysis. Preserve this in the referee response.
