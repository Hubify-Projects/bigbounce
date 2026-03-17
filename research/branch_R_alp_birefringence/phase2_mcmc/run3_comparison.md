# Run 3 Model Comparison

**Date:** 2026-03-17

---

## Models Compared

| Model | Description | Free params | Parameters |
|-------|-------------|-------------|------------|
| Null | beta = 0 | 0 | — |
| Model 0 | LCDM + beta_free | 1 | beta_deg |
| Model 2 | LCDM + ALP (C=8) | 2 | theta_i, log10_m |
| Model 2b | LCDM + ALP (C free) | 3 | theta_i, log10_m, C_agamma |

---

## Best-Fit Chi-Squared

| Model | chi2_min | k (free params) |
|-------|---------|-----------------|
| Null | 13.24 | 0 |
| Model 0 | ~0 | 1 |
| Model 2 | ~0 | 2 |
| Model 2b | ~0 | 3 |

All non-null models achieve chi2 ~ 0 because each can exactly reproduce beta_obs with appropriate parameter choices. The data is a single measurement, so any model with at least one free parameter that can map to beta achieves a perfect fit.

---

## Delta Chi-Squared vs Null

| Model | Delta chi2 | Significance |
|-------|-----------|-------------|
| Model 0 | 13.24 | 3.6 sigma |
| Model 2 | 13.24 | 3.6 sigma |
| Model 2b | 13.24 | 3.6 sigma |

All models provide identical improvement over beta = 0. The birefringence detection significance is 3.6 sigma regardless of the physical model used.

---

## Information Criteria

| Model | chi2_min | k | AIC | Delta AIC vs Model 0 |
|-------|---------|---|-----|---------------------|
| Model 0 | ~0 | 1 | 2.00 | 0.00 (reference) |
| Model 2 | ~0 | 2 | 4.00 | +2.00 |
| Model 2b | ~0 | 3 | 6.00 | +4.00 |

AIC penalizes models with more parameters when they do not improve the fit. Since all achieve chi2 ~ 0 on one data point, the simplest model (free beta) is preferred by AIC.

**BIC follows the same pattern** (with n=1: no additional penalty beyond AIC).

---

## Effective Parameter Count

This is the key insight. The data (one Gaussian measurement) provides one constraint. The models have:

| Model | Nominal params | Effective constrained params | Unconstrained params |
|-------|---------------|----------------------------|---------------------|
| Model 0 | 1 (beta) | 1 (beta) | 0 |
| Model 2 | 2 (theta_i, m) | 1 (theta_i, via beta) | 1 (m, weakly bounded) |
| Model 2b | 3 (theta_i, m, C) | 1 (C x theta_i product) | 2 (m, C/theta_i ratio) |

In every case, the data constrain exactly ONE effective combination. The extra parameters in the ALP models are either unconstrained (mass) or degenerate (C vs theta_i).

---

## Beta Posterior Comparison

All three models produce nearly identical beta posteriors:

| Model | beta mean | beta 68% CI |
|-------|-----------|-------------|
| Model 0 | 0.344 | [0.247, 0.439] |
| Model 2 | 0.336 | [0.245, 0.442] |
| Model 2b | 0.324 | [0.229, 0.421] |

The beta posteriors are visually indistinguishable (see `beta_comparison_all_models.png`). Model 2 has a slightly narrower posterior because the ALP physics imposes beta >= 0 (positive definite for theta_i > 0), which clips the negative tail that Model 0 allows. Model 2b is marginally broader because the C freedom adds parameter volume.

---

## Does ALP Provide Better, Equal, or Worse Description?

### Better? NO.
The ALP model does not fit the data better than free beta. It achieves the same chi2 with more parameters.

### Equal? YES (for beta prediction).
The ALP model exactly reproduces the free-beta posterior. It adds physical interpretation (beta comes from ALP rolling) but not statistical fit quality.

### Worse? MARGINALLY (by information criteria).
AIC penalizes the extra parameters. But this is a weak penalty — the ALP model is not significantly disfavored, just not significantly preferred.

---

## What the ALP Model Actually Provides

The ALP model does not improve the fit. What it provides is:

1. **Physical interpretation.** beta is not arbitrary — it comes from a specific field rolling with specific parameter relationships.

2. **Parameter prediction.** Given f_a = M_Pl and C = 8 (SM), the model predicts theta_i ~ 1.3. This is an O(1) natural value.

3. **Correlation structure.** The model predicts beta > 0 (positive rolling direction from theta_i > 0). Free beta allows negative values which the model does not.

4. **Falsifiability.** The model predicts specific relationships: beta is independent of f_a, scales linearly with theta_i, and saturates for m >> H_0. Free beta has no such structure.

5. **LiteBIRD testability.** If LiteBIRD measures beta precisely, the model predicts a specific theta_i (to ~0.04 rad precision with sigma_beta = 0.01 deg). Free beta just gets a better measurement.

These are not statistical advantages. They are physical advantages: the ALP model is more constrained, more predictive, and more falsifiable than free beta — it just cannot demonstrate this advantage with a single Gaussian data point.

---

## Verdict

The ALP model is statistically equivalent to free beta on current data. It is not statistically preferred, but it is physically richer. The comparison will become meaningful when:
- LiteBIRD provides sigma(beta) ~ 0.01 deg (distinguishing theta_i values)
- Anisotropic birefringence is measured (ALP predicts specific anisotropy pattern)
- Frequency dependence is tested (ALP predicts achromatic rotation)
