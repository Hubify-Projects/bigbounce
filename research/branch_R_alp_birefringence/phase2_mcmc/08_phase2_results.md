# Phase 2: Pre-Run Assessment & Verdict

**Date:** 2026-03-16
**Branch:** R Phase 2
**Status:** PRE-RUN (analytic prefit complete, MCMC not yet executed)

---

## 1. Summary of Prefit Findings

### Model 2: Spectator ALP (birefringence only, Lambda provides DE)

The analytic formula beta = C_{a gamma} alpha theta_i eta / (4 pi) gives:

- For theta_i = 1.0, eta = 1 (m >> H_0): beta = 0.27 deg (0.9 sigma below obs)
- For theta_i = 1.3, eta = 1 (m >> H_0): beta = 0.35 deg (matches central value)
- Favored range: theta_i in [0.6, 2.0] at 2 sigma

The spectator regime requires m > few x H_0 so that the field has fully rolled (eta -> 1). In this regime:
- Omega_a << 1 (ALP energy is negligible; it has oscillated and diluted)
- w_a is irrelevant (field is oscillating, but contributes negligibly to energy budget)
- Lambda provides dark energy independently

**Prefit verdict for Model 2: EXCELLENT FIT with natural parameters. No tension.**

### Model 3: ALP as Dark Energy (simultaneously DE and birefringence)

The joint constraints are:
- Birefringence: theta_i x eta ~ 1.3
- Dark energy density: (m/H_0)^2 x (1 - cos theta_i) / 3 ~ 0.68

On the Omega_a = 0.68 contour:
- The maximum achievable beta is ~0.16 deg (at theta_i ~ 2, m ~ 1.3 H_0)
- This is a factor ~2.2 below the observed 0.35 deg
- The tension arises because DE requires m ~ H_0 (frozen field, w ~ -1), but birefringence requires large eta (significant rolling), and these two requirements oppose each other

**Prefit verdict for Model 3: FACTOR-2 TENSION between birefringence amplitude and DE density.**

### Important Correction from Prefit Analysis

The Phase 1 analysis stated that eta -> 0 for m >> H_0 due to "oscillation averaging." This is **incorrect** for the integrated quantity beta = g_{a gamma} [phi(0) - phi(rec)] / 2. For m >> H_0:

- The field has rolled from theta_i to oscillations around zero
- The net excursion is Delta_theta ~ theta_i (the oscillation amplitude at z=0 is suppressed by (H_0/m)^{3/4})
- Therefore eta -> 1 for m >> H_0, not eta -> 0

The birefringence is a MONOTONICALLY INCREASING function of m (for m < H_rec). There is no "sweet spot" that suppresses beta at large m. The mass constraint comes from the DE requirement, not from birefringence.

## 2. Central Result: Birefringence and DE are Partially Competing

The key physical insight from the prefit:

**Birefringence requires the field to ROLL (large eta). Dark energy requires the field to be FROZEN (w ~ -1).**

These are opposite dynamical requirements. A frozen field (m << H_0, w = -1, good DE) gives eta ~ 0 and no birefringence. A fully-rolled field (m >> H_0, eta ~ 1, good birefringence) has w ~ 0 and is dark matter, not dark energy.

The overlap region (m ~ H_0) gives partial rolling: moderate eta, moderate w slightly above -1. In this regime:
- beta reaches ~50% of its maximum value
- w_a ~ -0.8 to -0.95 (consistent with current constraints but will be tested by DESI)
- Omega_a ~ 0.3-0.7 (in the right ballpark)

But the product theta_i x eta on the Omega_a = 0.68 contour maxes out at ~0.6, giving beta ~ 0.16 deg -- about half of the observed value.

## 3. Verdict

### ALP_DATA_PROGRAM_READY -- for Model 2 (spectator ALP)

The spectator ALP scenario is clean, predictive, and matches the data:

| Criterion | Status |
|-----------|--------|
| Natural parameters (theta_i ~ O(1)) | YES: theta_i ~ 1.3 |
| No fine-tuning of mass | YES: any m > few H_0 works |
| Matches beta_obs within 1 sigma | YES: 0.27-0.35 deg |
| All constraints satisfied | YES: by 9-32 orders of magnitude |
| Testable by LiteBIRD | YES: sigma_beta ~ 0.01 deg |

**Full MCMC is justified and should be straightforward.** Expected deliverables:
- Posterior on (theta_i, m) with clear degeneracy structure
- Bayes factor favoring ALP over null (beta = 0) at moderate-to-strong level
- Forecast for LiteBIRD parameter improvement

### ALP_DATA_PROGRAM_NEEDS_REWORK -- for Model 3 (ALP-as-DE)

The ALP-as-DE scenario has a quantitative tension:

| Criterion | Status |
|-----------|--------|
| beta and Omega_a simultaneously satisfied | NO: factor ~2 tension |
| Natural parameters | MARGINAL: needs theta_i ~ 2-3, C > 12 |
| w_a consistent with data | MARGINAL: w ~ -0.8 to -0.95 |
| No fine-tuning | NO: requires extended BSM sector |

**MCMC for Model 3 is still worth running** to quantify the tension precisely, but the prefit strongly suggests it will not produce a compelling fit with minimal parameters. The extended parameter space (C > 8, f_a < M_Pl) may partially resolve the tension but at the cost of introducing model-dependent assumptions.

## 4. Recommended Path Forward

### Immediate (this week):

1. Implement `alp_ode.py` and validate against Phase 1 analytics
2. Generate the eta(m/H_0, theta_i) lookup table and confirm the prefit analysis numerically
3. Run the prefit grid scan (theta_i vs m/H_0) with beta and Omega_a contours overlaid
4. Run MCMC Runs 2 and 3 locally (birefringence-only, ~hours)

### Short term (next week):

5. Deploy Run 4 to RunPod (spectator ALP + Planck + BAO)
6. Post-process: triangle plots, parameter constraints, Bayes factor
7. Draft paper section on spectator ALP birefringence

### Medium term (if warranted):

8. Deploy Run 5 to RunPod (ALP-DE, expect tension)
9. Assess whether extended parameters (Run 6) can resolve the tension
10. Write up complete model comparison

## 5. Impact Assessment

### If Model 2 succeeds (expected):

The paper can make the following claims:
- "An ultralight ALP with Planck-scale decay constant and SM anomaly coupling predicts beta = 0.27 deg, within 1 sigma of the 3.9-sigma observed cosmic birefringence"
- "The prediction is UV-insensitive (independent of f_a) and requires only O(1) initial misalignment"
- "MCMC analysis constrains theta_i = 1.3 +/- X and identifies the viable mass window m > Y H_0"
- "This represents the most economical explanation of the birefringence signal"
- "LiteBIRD will test this prediction at the 0.01-deg level within a decade"

### If Model 3 tension persists (expected):

The paper should honestly report:
- "If the ALP also serves as dark energy, the birefringence amplitude is reduced by a factor ~2 due to the competing requirements of field rolling (for beta) and freezing (for w ~ -1)"
- "Resolving this tension requires either an extended charged sector (C > 12) or treating birefringence and dark energy as phenomenologically separate"
- "This tension is a prediction: future precision measurements of both beta and w(z) will definitively test the unification hypothesis"

### Broader significance:

Regardless of the DE question, the spectator ALP result is publishable and significant:
- It is the ONLY observational handle identified in the entire Branch A-G + R research program
- It connects Planck-scale physics to a measurable CMB observable
- It is falsifiable by next-generation experiments
- It motivates a targeted experimental program (LiteBIRD, CMB-S4)

## 6. Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| ODE integration error | Low | High | Validate against analytics; cross-check with axionCAMB |
| Prior dominates posterior | Medium | Medium | Run prior-sensitivity tests; compute information gain |
| Degeneracy prevents useful constraints | Medium | Low | Expected: C x theta_i is degenerate. Focus on the product. |
| MCMC convergence issues | Low | Medium | Use proven Cobaya infrastructure; monitor R-hat |
| beta measurement shifts with new data | Medium | High | Frame results in terms of current data; forecast for LiteBIRD |

## 7. Bottom Line

**Model 2 (spectator ALP): READY FOR MCMC. Expected to succeed.**

**Model 3 (ALP-as-DE): WORTH RUNNING but expected to show factor-2 tension. The birefringence and DE roles partially compete.**

The Phase 1 conclusion that "the ALP IS dark energy" at the same parameters that give the right birefringence is qualitatively correct (the energy scales coincide) but quantitatively incomplete. When the field dynamics are properly accounted for, the DE requirement (m ~ H_0, w ~ -1) suppresses the rolling efficiency eta, reducing the predicted beta by a factor ~2 below the spectator-ALP prediction.

This is an honest and important finding. It means the birefringence signal, if confirmed, points to an ALP that is either (a) a spectator with Lambda still providing DE, or (b) a more complex dark-energy-plus-birefringence model requiring extended particle content. Both scenarios are physically interesting and testable.
