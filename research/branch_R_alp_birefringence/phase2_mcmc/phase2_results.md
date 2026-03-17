# Phase 2 Verdict: ALP Birefringence Data Program

**Date:** 2026-03-17
**Verdict:** ALP_EQUIVALENT_TO_BETA

---

## What Was Done

Three MCMC runs executed and analyzed:

| Run | Model | Params | Samples | R-1 | Status |
|-----|-------|--------|---------|-----|--------|
| Run 1 | ALP (C=8 fixed) | theta_i, log10_m | 2160 | 0.0083 | CONVERGED |
| Run 2 | ALP (C free) | theta_i, log10_m, C_agamma | 6840 | 0.0091 | CONVERGED |
| Run 3 | Beta free | beta_deg | 720 | 0.0047 | CONVERGED |

All runs converged well below R-1 = 0.01. N_eff > 1000 for sampled parameters.

---

## Key Results

### 1. ALP model fits the data perfectly

| Model | beta posterior | chi2_min |
|-------|--------------|----------|
| ALP (C=8) | 0.336 +/- 0.107 deg | ~0 |
| Beta free | 0.344 +/- 0.096 deg | ~0 |
| Observed | 0.342 +/- 0.094 deg | — |

### 2. Natural parameter space

| Parameter | Posterior | Natural? |
|-----------|----------|----------|
| theta_i | 1.36 +/- 0.44 | YES (O(1)) |
| log10(m/eV) | -31.3 +/- 0.7 | YES (m > few x H_0, spectator) |
| C_agamma | fixed at 8 (SM) | YES (no BSM needed) |

### 3. Degeneracy mapped

C_agamma and theta_i are degenerate: data constrain C x theta_i ~ 10.6. Floating C does not improve the fit. The SM value C = 8 is within the posterior.

### 4. Model comparison

| Comparison | Result |
|-----------|--------|
| ALP vs null (beta=0) | Delta chi2 = 13.2 (3.6 sigma) |
| ALP vs beta_free | Delta chi2 = 0 (equivalent) |
| ALP vs beta_free (AIC) | Delta AIC = +2 (marginal penalty for extra param) |

---

## Does ALP Add Real Explanatory Value Beyond Beta?

### Statistically: NO.

With one Gaussian data point, any model that can produce beta ~ 0.34 fits equally well. The ALP model uses 2 parameters to achieve what 1 parameter (free beta) achieves. Information criteria mildly penalize the extra parameter.

### Physically: YES.

The ALP model provides:
1. A natural O(1) explanation for why beta ~ 0.3 (not 0.003 or 3)
2. A specific prediction: beta = C alpha theta_i / (4 pi) with C = 8 (SM)
3. f_a independence (robust across UV models)
4. Falsifiable structure (achromatic, isotropic, specific mass scaling)
5. LiteBIRD-testable predictions at sigma(beta) ~ 0.01 deg

### The honest assessment:

The ALP model is a physical interpretation of beta, not a better fit to beta. On current data, it is equivalent to simply measuring beta. Its value lies in the prediction: given f_a ~ M_Pl and C = 8, the model predicts theta_i ~ 1.3, which is natural. If LiteBIRD confirms beta to high precision, the ALP model becomes testable in a way that free beta never can.

---

## Verdict: ALP_EQUIVALENT_TO_BETA

The spectator ALP with f_a = M_Pl and C_agamma = 8 provides a clean, natural, zero-tuning physical interpretation of the observed cosmic birefringence. It is statistically equivalent to a free beta parameter on current data. It becomes distinguishable with next-generation CMB polarization experiments.

This is an honest result. The ALP model is not "better" than free beta — it is a physical model that naturally lands at the observed value. That is worth stating in a paper, but not overclaiming.

---

## Should We Proceed to Full Cosmology Run?

### Assessment

| Factor | Score |
|--------|-------|
| Does the birefringence-only run work? | YES |
| Is the parameter space well-behaved? | YES |
| Would Planck+BAO change the birefringence constraint? | NO (spectator decouples) |
| Would it demonstrate no conflict with standard cosmology? | YES (valuable for the paper) |
| Is it worth the compute cost (~$20 RunPod, ~25 hours)? | MARGINAL |

### Recommendation

**Run 4 (Planck+BAO) is useful for the paper but not scientifically necessary.** The spectator ALP does not affect standard cosmological parameters by definition. The joint run would demonstrate this formally and produce a full triangle plot with H_0, omega_m, etc. — useful for a publication figure but not expected to change the ALP posterior.

**Priority should be:**
1. Begin paper restructure with the Run 1 + Run 2 + Run 3 results (sufficient for the paper)
2. Run 4 on RunPod in parallel if infrastructure is available
3. Run 5 (ALP-as-DE) only if the paper explicitly needs to address the unified scenario

---

## Files

| File | Content |
|------|---------|
| `alp_ode.py` | ALP ODE solver |
| `alp_theory.py` | Cobaya Theory class (supports fixed and free C) |
| `birefringence_lk.py` | Cobaya Likelihood |
| `beta_free_theory.py` | Trivial theory for baseline model |
| `run1_full.yaml` | Run 1 config |
| `run2_extended.yaml` | Run 2 config |
| `run3_baseline.yaml` | Run 3 config |
| `run1_validation.md` | Pre-run checks |
| `run1_results.md` | Run 1 posterior |
| `run2_results.md` | Run 2 degeneracy analysis |
| `run3_comparison.md` | 3-model comparison |
| `phase2_results.md` | This file |
| `chains/run1_full/` | Run 1 chains + plots |
| `chains/run2_extended/` | Run 2 chains + plots |
| `chains/run3_baseline/` | Run 3 chains |
