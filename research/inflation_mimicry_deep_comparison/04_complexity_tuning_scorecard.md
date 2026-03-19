# 04: Complexity / Tuning Scorecard

## Head-to-Head Comparison

| Criterion | Matter Bounce | Standard Single-Field Inflation | Non-Attractor Inflation | Best Multifield Competitor |
|-----------|--------------|-------------------------------|------------------------|---------------------------|
| **Extra fields beyond minimal** | 0 | 0 | 0 | **≥1** (curvaton/spectator) |
| **Extra potential terms tuned for f_NL** | 0 | 0 | ~2 (potential shape + transition) | **≥2** (self-coupling + decay fraction) |
| **f_NL prediction** | -35/8 (exact) | +0.015 (exact) | +5/2 (natural) → needs engineering for -4 | Continuous family → tuned to hit -4 |
| **f_NL sign** | Negative (automatic) | Positive (automatic) | **Positive** (natural) | Either (tunable) |
| **Can reach -4.375?** | **YES (automatically)** | NO | Only with engineering | Only with tuning |
| **Parameter-free for f_NL?** | **YES** | YES (but wrong value) | NO | **NO** |
| **n_s = 0.964 compatible?** | YES (1 param: ε) | YES (trivially) | PROBLEMATIC (USR disrupts scale-invariance) | YES (extra freedom allows it) |
| **r ~ 10⁻⁴ compatible?** | YES (LQC suppression) | YES (small-field) | Model-dependent | YES (extra freedom) |
| **Overall predictivity** | **HIGH** (1 free param for n_s; f_NL fixed) | HIGH (but wrong f_NL) | LOW (transition-dependent) | LOW (multiple free parameters) |

## Classification

| Model | Classification |
|-------|---------------|
| Matter Bounce | **BENCHMARK** — 0-parameter prediction for f_NL |
| Standard Single-Field Inflation | FAILS HARD — f_NL = +0.015 ≠ -4.375 |
| Non-Attractor Inflation | **MORE_ENGINEERED_THAN_BOUNCE** — natural sign is wrong (+5/2); transition-dependent; fine-tuned |
| Multifield / Self-Interacting Curvaton | **MORE_ENGINEERED_THAN_BOUNCE** — ≥2 extra parameters; can hit -4.375 but doesn't predict it |
| Rapid-Turn / Curved Field Space | **MORE_ENGINEERED_THAN_BOUNCE** — ≥3 extra ingredients (extra field, geometry, turn timing) |

## The Asymmetry

The matter bounce PREDICTS f_NL = -4.375 with zero adjustable parameters in the cubic sector. The value follows automatically from ε = 3/2 (matter contraction) and the Maldacena cubic action.

Inflation can ACCOMMODATE f_NL = -4.375 only by:
1. Adding at least one extra field or non-trivial potential feature
2. Tuning at least two continuous parameters (self-coupling strength + decay/conversion fraction)
3. Engineering the sign (standard constructions give positive f_NL)

This is the fundamental **kinematic vs parametric** asymmetry:
- **Bounce: kinematic** — the value is forced by the equation of state
- **Inflation: parametric** — the value is one point in a continuous parameter space that must be retroactively fitted

## What This Means for Bayesian Model Comparison

In Bayesian evidence (BIC/AIC/nested model comparison), a model that predicts the data with N fewer parameters has an exponential advantage in evidence:

ln(B_bounce / B_inflation) ~ (N_inflation - N_bounce) × ln(data volume) / 2

For our case: N_inflation - N_bounce ≥ 2 (at least 2 extra parameters for the multifield construction). If f_NL = -4.375 is measured, the bounce model has a LARGE Bayesian advantage over any inflationary competitor that must tune parameters to match.

This is NOT "inflation is impossible." It is "inflation pays a heavy complexity tax to reach the same place the bounce reaches for free."
