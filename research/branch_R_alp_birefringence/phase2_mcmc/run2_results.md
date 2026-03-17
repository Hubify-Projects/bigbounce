# Run 2 Results: Extended ALP Model (C_agamma floated)

**Date:** 2026-03-17
**Verdict:** DEGENERATE

---

## Run Configuration

| Item | Value |
|------|-------|
| Model | LCDM + spectator ALP, C_agamma sampled |
| Sampled parameters | theta_i, log10(m_a/eV), C_agamma |
| Fixed | f_a = M_Pl |
| Data | beta_obs = 0.342 +/- 0.094 deg |
| Convergence | R-1 = 0.009 (target: < 0.01) |
| Accepted samples | 6840 |
| Acceptance rate | 14.5% |

---

## Posterior Summary

| Parameter | Mean | 68% CI | 95% CI |
|-----------|------|--------|--------|
| theta_i | 1.33 | [0.27, 1.77] | -- |
| log10(m/eV) | -31.45 | [-32.62, -30.08] | -- |
| C_agamma | 13.4 | [2.7, 19.0] | [2.3, 28.2] |
| beta (deg) | 0.324 | [0.229, 0.421] | -- |
| eta | 0.87 | [0.89, 1.17] | -- |

---

## Degeneracy Analysis

### Correlations

| Pair | r |
|------|---|
| theta_i vs C_agamma | **-0.524** |
| theta_i vs log10_m | -0.173 |
| C_agamma vs log10_m | -0.228 |

The dominant correlation is theta_i vs C_agamma, with r = -0.52. This is the expected degeneracy: beta is proportional to C x theta_i (when eta ~ 1), so the data constrain the product, not the individual values.

### C x theta_i product

| Statistic | Value |
|-----------|-------|
| Mean | 12.9 |
| Median | 10.6 |
| 95% CI | [4.4, 43.9] |

The product is better constrained than either factor individually, confirming the degeneracy.

### Does birefringence constrain C_agamma independently?

**No.** The posterior 68% width (16.3) is 56% of the prior width (29). This is weak constraint at best — the data barely tighten the prior. With one data point (beta_obs), the system has one effective degree of freedom. This constrains one combination (C x theta_i x eta) but leaves the individual parameters degenerate.

### Key observation

The C_agamma posterior peaks above the SM value of 8. This does NOT mean the data prefer C > 8. It is a volume effect: the hyperbolic degeneracy C x theta_i = const allows more prior volume at large C (small theta_i) than at small C (large theta_i, bounded by pi).

---

## Comparison with Run 1 (C = 8 fixed)

| Quantity | Run 1 (C=8) | Run 2 (C free) |
|----------|-------------|----------------|
| beta (deg) | 0.336 +/- 0.107 | 0.324 +/- 0.110 |
| theta_i | 1.36 +/- 0.44 | 1.33 +/- 0.73 |
| log10_m | -31.3 +/- 0.7 | -31.4 +/- 0.8 |
| min chi2 | ~0 | ~0 |

The beta posterior is essentially unchanged. Floating C_agamma widens the theta_i posterior (naturally, since the constraint shifts to the product) but does not improve the fit.

---

## Verdict: DEGENERATE

C_agamma and theta_i are degenerate: the data constrain C x theta_i, not individually. Floating C_agamma adds a parameter without improving the fit. For the paper, **fix C_agamma = 8 (SM) and quote constraints on theta_i**. The degeneracy can be noted as: "the data constrain C x theta_i ~ 10.6; for C = 8 this gives theta_i ~ 1.3."

---

## Plots

1. `chains/run2_extended/triangle_plot.png` — Full triangle (theta_i, C, log10_m, beta)
2. `chains/run2_extended/C_vs_theta_degeneracy.png` — C vs theta_i scatter colored by beta
3. `chains/run2_extended/beta_comparison_all_models.png` — Beta posteriors for all 3 models
