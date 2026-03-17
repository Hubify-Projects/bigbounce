# Run 1 Validation Report

**Date:** 2026-03-17
**Status:** ALL CHECKS PASSED

---

## 1. ODE Solver Validation (`alp_ode.py`)

### Limiting behavior

| Test | Input | Expected | Actual | Status |
|------|-------|----------|--------|--------|
| Full rolling (m >> H0) | theta_i=1, log10_m=-30 | beta ~ 0.27, eta ~ 1 | beta=0.2660, eta=0.9993 | PASS |
| Frozen (m << H0) | theta_i=1, log10_m=-36 | beta ~ 0, eta ~ 0 | beta~0, eta~0 | PASS |
| Intermediate (m ~ H0) | theta_i=1, log10_m=-33 | beta ~ 0.01-0.05, eta ~ 0.05 | beta=0.0148, eta=0.0555 | PASS |
| Match observed | theta_i=1.3, log10_m=-30 | beta ~ 0.35 | beta=0.3458 | PASS |

### Scaling with theta_i (m >> H0)

| theta_i | beta (deg) | beta/theta_i | Status |
|---------|-----------|-------------|--------|
| 0.5 | 0.1330 | 0.2660 | Linear (PASS) |
| 1.0 | 0.2660 | 0.2660 | Linear (PASS) |
| 1.5 | 0.3991 | 0.2661 | Linear (PASS) |
| 2.0 | 0.5324 | 0.2662 | ~Linear (PASS) |
| 3.0 | 0.7994 | 0.2665 | ~Linear (PASS) |

Analytic prediction: beta/theta_i = C * alpha / (4 pi) = 8 * (1/137) / (4 pi) = 0.004651 rad = 0.2665 deg. **Matches to 0.2%.**

### Mass scan (theta_i = 1)

| log10_m | eta | beta (deg) | Omega_a | w_a | Status |
|---------|-----|-----------|---------|-----|--------|
| -36 | 0.00000 | 0.00000 | 7.4e-8 | -1.000 | PASS (frozen) |
| -35 | 0.00001 | 0.00000 | 7.4e-6 | -1.000 | PASS |
| -34 | 0.00056 | 0.00015 | 7.4e-4 | -0.999 | PASS |
| -33 | 0.0555 | 0.0148 | 0.068 | -0.945 | PASS |
| -32.5 | 0.491 | 0.131 | 0.310 | -0.316 | PASS (transition) |
| -32 | 0.989 | 0.263 | 0.129 | +0.984 | PASS (oscillating) |
| -31 | 0.999 | 0.266 | 0.134 | +0.987 | PASS (full rolling) |
| -30 | 0.999 | 0.266 | 0.133 | +0.485 | PASS |

Transition from frozen to rolling occurs at log10_m ~ -32.5 to -32, as expected (m/H0 ~ 3-30).

### Numerical stability

- No integration failures across the full parameter range
- rtol = 1e-10, atol = 1e-12 (conservative)
- Timing: 20.7 ms per evaluation (adequate for MCMC)

---

## 2. Cobaya Integration Validation

### Theory class (`alp_theory.py`)

- `get_can_support_params` correctly declares theta_i, log10_m_eV
- `get_can_provide_params` correctly declares beta_deg, eta, Omega_a, w_a_0
- `calculate()` returns True on success, fills state dict
- Cobaya `evaluate` sampler runs without error

### Likelihood class (`birefringence_lk.py`)

- Returns correct log-likelihood: -0.5 * ((beta - 0.342) / 0.094)^2
- At beta = 0.342: logL = 0 (maximum)
- At beta = 0: logL = -6.62 (chi2 = 13.24)
- Correctly retrieves beta_deg from Theory provider

### End-to-end test

- Cobaya `evaluate` sampler at reference point (theta_i=1.67, log10_m=-32.36):
  - beta = 0.311 deg
  - chi2 = 0.108
  - All derived parameters computed correctly

---

## 3. MCMC Test Run Validation

- 2 chains, 5000 max samples
- Converged at R-1 = 0.024 after 880 accepted samples
- Acceptance rate: 23% (healthy)
- theta_i = 1.39 +/- 0.46 (sensible)
- beta_deg = 0.335 +/- 0.115 (encompasses observed value)

**No numerical instabilities observed.**

---

## Verdict: VALIDATION_PASSED

All implementation checks pass. Proceed to full run.
