# P5 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-maint_P5_v0_1_32
**Wall time**: 109.9s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=29182, completion=6268, reasoning=5178, total=35450

---

Convergence does not hold.

## PAPER-GPT-B1 — BLOCKER

**Section:** Abstract; §III.D; §VI.A/Table “CW fraction per cosmic-web environment”; DESIVAST residual paragraph  
**Issue:** Central sample arithmetic is impossible. The V-Web class counts sum to **812,793** (`428+6673+408187+397505`), not the advertised **791,635** chirality-relevant spirals; later text admits an 812,793 “superset,” while the abstract/table still claim the headline is on 791,635. Additional subgroup counts are impossible/inconsistent, e.g. filament bright `n=416,701` exceeds the headline filament total `408,187`, and the systematics BGS-vs-dark statement contradicts the earlier bright/dark split.  
**Fix:** Freeze one canonical analysis sample, state its exact cuts once, and recompute every headline table, abstract number, subgroup decomposition, σ, and systematic split on that same sample.

## PAPER-GPT-B2 — BLOCKER

**Section:** Abstract; §VIII/Table “Phase 2 sensitivity sweep”  
**Issue:** The Phase-2 robustness claim contradicts the canonical table. The canonical `(R_s=25, λ_th=0)` V-Web table has a four-class CW-fraction range `0.5034−0.4836=0.0198 = 1.98 pp`, but the Phase-2 table lists the same cell as `0.165 pp` and claims the max over all cells is `0.220 pp`. Also the Phase-2 “largest bin” `n=3,696,152` exceeds the matched-primary and chirality-relevant parent samples.  
**Fix:** Recompute the Phase-2 sweep on the same CW/CCW matched sample and clarify whether tiny classes are excluded; otherwise remove the “max 0.22 pp across four classes” claim.

## PAPER-GPT-M1 — MAJOR

**Section:** §IV V-Web classification; §VII.F T-Web comparison; Limitations  
**Issue:** The implemented classifier is not V-Web: it solves Poisson from the density field and diagonalizes the tidal Hessian, i.e. T-Web, not velocity-shear V-Web. More seriously, the density field is built from the observed DESI survey without an explicit radial/angular selection-function correction, random catalog normalization, or non-periodic masked Poisson treatment; FFT on an irregular 18.8% footprint induces boundary/shell artifacts that the paper itself later observes.  
**Fix:** Rename the method T-Web or implement an actual velocity-shear V-Web; rebuild the density field using randoms/selection-function correction and validated mask/boundary handling on mocks, or demote this classifier and make DESIVAST/ASTRA the canonical environment assignment.

## PAPER-GPT-M2 — MAJOR

**Section:** §V Statistical methods; §VI–§VII interpretation  
**Issue:** The environmental-dependence test is not formulated as a proper hypothesis test. Per-bin `σ_from_half` and ad hoc comparison to `σ_pred` do not test class-to-class dependence after marginalizing over the global chirality monopole, imaging leg, DESI program, redshift, and environment-class uncertainty. The “within order unity” and “candidate if |σobs−σpred|>3” rules are arbitrary and under-propagate the Paper-IV monopole/systematic uncertainty.  
**Fix:** Fit a binomial/logistic or contingency-table model with a global monopole nuisance parameter and environment coefficients, marginalizing/profile-likelihood over systematics; report likelihood-ratio/Bayes-factor/χ² results and upper limits on class contrasts.

## PAPER-GPT-M3 — MAJOR

**Section:** §VII.F DESIVAST-anchored void classifier  
**Issue:** The DESIVAST point-in-sphere membership uses `k=20` nearest hole centers and asserts this is sufficient from the maximum hole radius. That is not guaranteed: a containing sphere need not be among the 20 nearest centers if many smaller non-containing centers are closer. This can misclassify void membership and directly affects the strongest DESIVAST null evidence.  
**Fix:** Query all centers within the maximum radius with `query_ball_point`/spatial indexing, then apply each sphere’s own radius; for watershed catalogs, prefer catalog-native GALZONE membership over effective-radius sphere approximations.

## PAPER-GPT-M4 — MAJOR

**Section:** Conclusions, “Mapping to a physical operator”  
**Issue:** The EFT bound is dimensionally and statistically underderived. `g_φ(∇φ)(∇ρ/ρ_bg)(L·z)` lacks a specified normalization/field dimension, `∇ρ/ρ_bg` carries inverse-length units, the proportionality between the operator and `Δf_CW` is unspecified, and the quoted bound `|g_φ∇φ/H0|≲10^{-2}/⟨|Δρ/ρ_bg|⟩` is not a derived likelihood constraint.  
**Fix:** Either remove the numerical coupling bound or present a defined EFT normalization, transfer function from operator to chirality fraction, density-gradient scale, and marginalized statistical limit.
