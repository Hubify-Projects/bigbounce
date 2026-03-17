# Phase 2: Model Comparison Criteria

**Date:** 2026-03-16
**Branch:** R Phase 2

---

## 1. Models Under Comparison

| Model | Label | New params | Total DOF | Description |
|-------|-------|-----------|-----------|-------------|
| 0 | LCDM (null) | 0 | 6 | Standard LCDM, beta = 0 |
| 1 | LCDM + beta_free | 1 (beta) | 7 | Phenomenological birefringence |
| 2 | LCDM + ALP-biref | 2 (theta_i, m) | 8 | Spectator ALP, f_a = M_Pl, C = 8 |
| 3 | ALP-DE + biref | 2 (theta_i, m) | 7 | ALP replaces Lambda, f_a = M_Pl, C = 8 |
| 2ext | LCDM + ALP-biref-ext | 4 (theta_i, m, f_a, C) | 10 | Spectator ALP, extended |

## 2. Success Criteria

### Model 2 (Spectator ALP) -- PRIMARY TARGET

**Strong success:**
- theta_i posterior peaks at O(1) value (not pushed to boundary)
- m posterior shows a well-defined sweet-spot band (not prior-dominated)
- Best-fit beta_pred within 1 sigma of beta_obs
- Bayesian evidence favors Model 2 over null (ln B > 2.5, "strong" on Jeffreys scale)
- No fine-tuning: the prior volume within 2 sigma of the best fit is > 10% of total prior volume

**Moderate success:**
- theta_i ~ O(1) but degeneracy with C_{a gamma} prevents tight individual constraints
- m only weakly constrained (posterior broad in log10_m)
- Best-fit beta within 2 sigma of beta_obs
- Bayesian evidence mildly positive (0 < ln B < 2.5)

**Expected outcome (from prefit):** Strong success. The spectator ALP at natural parameters (theta_i ~ 1.3, m > few H_0) gives beta ~ 0.35 deg with no tuning.

### Model 3 (ALP-DE) -- SECONDARY TARGET

**Strong success:**
- Simultaneous fit to beta AND Omega_a with natural parameters
- w_a(z=0) within Planck + DESI constraints (w = -1.0 +/- 0.1)
- Delta_chi^2 <= 2 compared to LCDM + beta_free
- ALP fully replaces Lambda with no residual tension

**Moderate success:**
- Fit requires theta_i near pi (marginally natural)
- Mild tension with beta_obs (1-2 sigma low)
- w_a slightly above -1 but within current error bars
- Delta_chi^2 ~ 2-5 (worse than Model 2 but not catastrophic)

**Expected outcome (from prefit):** Moderate success at best. The prefit analysis (File 5) shows beta_pred ~ 0.10-0.16 deg on the Omega_a = 0.68 contour, a factor ~2 below observation. This represents a persistent tension that parameter extensions may partially but not fully resolve.

## 3. Failure Criteria

### Model 2 failure indicators

- theta_i pushed to prior boundary (theta_i -> pi or theta_i -> 0)
- m unconstrained (flat posterior spanning full prior range)
- Best-fit beta > 2 sigma from beta_obs
- Bayesian evidence AGAINST ALP vs null (ln B < 0)
- Only works in a tiny region of parameter space (prior volume < 1%)

### Model 3 failure indicators

- beta_pred < 0.15 deg at ALL points with Omega_a in [0.5, 0.9] -- definitive factor-2 tension
- w_a(z=0) > -0.7 required (conflicts with SN + BAO at > 3 sigma)
- Birefringence and DE constraints point to DISJOINT parameter regions
- Delta_chi^2 > 10 compared to Model 2 (overwhelmingly worse)

## 4. Statistical Framework

### Chi-squared comparison

For nested models (0 vs 1, 1 vs 2):

$$\Delta\chi^2 = \chi^2_{\rm simpler} - \chi^2_{\rm complex}$$

with k = number of additional parameters. Threshold for "improvement":
- Delta_chi^2 > 1 per additional parameter: suggestive
- Delta_chi^2 > 4 per additional parameter: significant
- Delta_chi^2 > 9 per additional parameter: highly significant

### Bayesian model comparison

Compute the Bayesian evidence ratio (Bayes factor):

$$B_{ij} = \frac{P(D|M_i)}{P(D|M_j)} = \frac{\int L(\theta_i) \pi(\theta_i) d\theta_i}{\int L(\theta_j) \pi(\theta_j) d\theta_j}$$

Interpretation (Jeffreys scale):

| ln B | Strength |
|------|----------|
| < 0 | Favors simpler model |
| 0 - 1 | Inconclusive |
| 1 - 2.5 | Moderate |
| 2.5 - 5 | Strong |
| > 5 | Decisive |

### Methods for computing Bayes factor

1. **Savage-Dickey density ratio** (for nested models): B = p(beta=0|data, M2) / p(beta=0|prior, M2). Fast, requires only the posterior samples.

2. **Harmonic mean estimator:** Simple but unreliable (high variance). Use as a cross-check only.

3. **PolyChord nested sampler:** Gold standard for evidence computation. Run a separate PolyChord analysis if the MCMC results warrant publication.

### AIC / BIC (supplementary)

$$\text{AIC} = -2\ln L_{\max} + 2k$$
$$\text{BIC} = -2\ln L_{\max} + k\ln N$$

where k = number of parameters, N = number of data points. Prefer the model with lower AIC/BIC. Note: for the birefringence-only likelihood (N=1), BIC penalizes extra parameters heavily.

## 5. Key Diagnostics

### For each model, report:

| Quantity | Description |
|----------|-------------|
| chi^2_min | Best-fit chi-squared |
| chi^2_red | Reduced chi-squared (chi^2 / DOF) |
| beta_pred (best fit) | Predicted birefringence at best-fit parameters |
| beta_pred (68% CL) | Credible interval on predicted beta |
| Omega_a (best fit) | ALP energy fraction (Model 3) |
| w_a(z=0) (best fit) | ALP equation of state (Model 3) |
| ln B vs null | Bayesian evidence vs beta = 0 |
| Delta_AIC vs LCDM | AIC difference |
| Prior volume fraction | Fraction of prior volume within 2 sigma |

### Tension metrics

If Models 2 and 3 give different preferred parameters:

$$T = \frac{|\bar{\theta}_2 - \bar{\theta}_3|}{\sqrt{\sigma_2^2 + \sigma_3^2}}$$

where theta is any shared parameter. T > 2 indicates significant tension.

### Goodness of fit

Since the birefringence likelihood is a single Gaussian measurement:
- chi^2_min should be ~ 0 for models that can fit the data
- chi^2_min >> 1 indicates a model that cannot reach the observed beta value

For the full Planck + BAO + beta likelihood:
- chi^2_red should be close to 1
- Compare to LCDM chi^2 (from existing Paper 1 chains)

## 6. Forecasting: LiteBIRD Sensitivity

If the current analysis is promising, forecast the improvement from LiteBIRD (sigma_beta ~ 0.01 deg):

1. Generate mock data at best-fit beta
2. Rerun MCMC with sigma_beta = 0.01 (replacing 0.094)
3. Compare posterior widths
4. Determine whether theta_i and m can be individually constrained (breaking the degeneracy)

Expected improvement: sigma_beta shrinks by ~10x. For Model 2, this would constrain theta_i to ~10% (currently ~50%). The mass constraint depends on how much of the viable region is in the eta ~ 1 plateau (where m drops out).

## 7. Decision Tree

```
Run 2 (ALP-biref, birefringence only)
  |
  |-- beta_pred consistent with obs?
  |     |
  |     YES --> Run 4 (add Planck + BAO)
  |     |         |
  |     |         |-- Parameters stable? Fit good?
  |     |               |
  |     |               YES --> Run 5 (ALP-DE)
  |     |               |         |
  |     |               |         |-- Omega_a and beta simultaneously OK?
  |     |               |               |
  |     |               |               YES --> PUBLISH (ALP unification paper)
  |     |               |               |
  |     |               |               NO --> PUBLISH (spectator ALP paper)
  |     |               |               |       Note DE tension in discussion
  |     |               |
  |     |               NO --> Debug. Check ODE integration.
  |     |
  |     NO --> Check prefit. Likely implementation error.
  |            Phase 1 analytics guarantee beta ~ 0.27 for fiducial params.
```

## 8. Publication Decision

**Publish if:**
- Model 2 provides a clear, natural explanation of beta_obs with O(1) parameters
- The C x theta_i degeneracy is clearly mapped
- Bayes factor favors ALP over null by at least moderate evidence
- Forecast shows LiteBIRD can decisively test the model

**Do NOT publish (yet) if:**
- Results are entirely prior-dominated (data contributes negligible constraining power)
- Only the trivially recoverable beta_free result is obtained (no physical insight beyond "beta is nonzero")
- Numerical issues in ODE integration create artifacts in the posterior

**Paper framing (most likely outcome):**
"An ultralight ALP with f_a ~ M_Pl and SM anomaly coupling naturally predicts cosmic birefringence beta = 0.27-0.35 deg, consistent with the 3.9-sigma detection. The MCMC analysis constrains theta_i = X +/- Y and identifies the viable mass window. If the ALP also serves as dark energy, a factor-2 tension with the birefringence amplitude emerges, suggesting the two roles require separate mechanisms or extended particle content."
