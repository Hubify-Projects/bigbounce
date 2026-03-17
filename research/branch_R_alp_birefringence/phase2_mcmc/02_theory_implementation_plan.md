# Phase 2: Theory Implementation Plan

**Date:** 2026-03-16
**Branch:** R Phase 2

---

## 1. Implementation Options

### Option A: Decoupled ODE + Standard CAMB (Models 1 & 2)

**Architecture:** Solve the ALP background ODE in standalone Python, independent of the Boltzmann solver. Use standard CAMB for CMB power spectra. Combine via Cobaya.

**Advantages:**
- Fast: ALP ODE takes ~10 ms per evaluation
- No modifications to CAMB required
- Reuses the existing Cobaya + CAMB pipeline exactly
- Sufficient for birefringence-only fits (Models 1 and 2)

**Limitations:**
- ALP perturbations not included in CMB spectra
- ALP contribution to background expansion not fed back to CAMB
- Not self-consistent for Model 3 (ALP-as-DE)

**Verdict: USE THIS for Phase 2a (Models 1 and 2).**

### Option B: axionCAMB or Custom CAMB Modification (Model 3)

**Architecture:** Use axionCAMB (github.com/dgrin1/axionCAMB), a modified CAMB that self-consistently evolves ultralight axion fields alongside the standard cosmological perturbations.

**Advantages:**
- Self-consistent background + perturbation evolution
- ALP dark energy properly modifies H(z), distances, CMB spectra
- Includes ALP clustering (relevant if m not much below H_0)
- Publication-quality for Model 3

**Limitations:**
- Requires installing and validating axionCAMB
- Slower per evaluation (~seconds)
- May need Cobaya wrapper modifications
- Perturbation treatment for m ~ H_0 can be numerically delicate

**Verdict: USE THIS for Phase 2b (Model 3 only). Defer until Phase 2a validates parameter space.**

## 2. Option A Code Structure (Phase 2a)

### File layout

```
research/branch_R_alp_birefringence/phase2_mcmc/
  code/
    alp_ode.py           -- ALP background ODE integrator
    alp_theory.py        -- Cobaya Theory class wrapping alp_ode
    birefringence_lk.py  -- Cobaya Likelihood class for beta measurement
    de_constraint_lk.py  -- Optional: DE density constraint likelihood
    eta_table.py         -- Precomputed eta(m/H0, theta_i) lookup table
    validate.py          -- Unit tests against Phase 1 analytic results
    plot_prefit.py       -- Generate prefit grid plots (File 5)
  configs/
    model1_lcdm_beta.yaml      -- Cobaya config: LCDM + beta_free
    model2_alp_biref.yaml      -- Cobaya config: LCDM + ALP spectator
    model3_alp_de.yaml         -- Cobaya config: ALP-DE (Phase 2b)
    model2_extended.yaml       -- Extended parameter set (Phase 2b)
```

### alp_ode.py -- Core ODE Integrator

```python
"""
ALP background evolution on LCDM cosmology.

Solves: theta'' + 3H theta' + m^2 sin(theta) = 0
in terms of ln(a), from z=1200 to z=0.

Returns: theta(z_rec), theta(z=0), rho_a(z=0), w_a(z=0)
"""
import numpy as np
from scipy.integrate import solve_ivp

# Physical constants
H0_eV = 1.44e-33  # H_0 in eV (h=0.674)
M_Pl_GeV = 2.435e18  # Reduced Planck mass

def hubble_lcdm(a, H0, Omega_m, Omega_r):
    """LCDM Hubble parameter H(a)/H_0."""
    Omega_L = 1.0 - Omega_m - Omega_r
    return H0 * np.sqrt(Omega_r / a**4 + Omega_m / a**3 + Omega_L)

def solve_alp(theta_i, log10_m_eV, H0=H0_eV, Omega_m=0.315, Omega_r=9.1e-5):
    """
    Integrate the ALP EOM from z=1200 to z=0.

    Parameters
    ----------
    theta_i : float
        Initial misalignment angle (radians)
    log10_m_eV : float
        log10(m_a / eV)
    H0 : float
        Hubble constant in eV
    Omega_m : float
        Matter density parameter
    Omega_r : float
        Radiation density parameter

    Returns
    -------
    dict with keys:
        'theta_rec': theta at z=1090
        'theta_0': theta at z=0
        'delta_theta': theta_rec - theta_0
        'eta': delta_theta / theta_i
        'beta_rad': birefringence in radians (for C_agamma=8)
        'beta_deg': birefringence in degrees
        'Omega_a': ALP energy fraction today
        'w_a_0': ALP equation of state at z=0
    """
    m = 10**log10_m_eV  # ALP mass in eV

    # ln(a) ranges: a_init = 1/(1+1200), a_final = 1
    lna_init = -np.log(1201)
    lna_rec = -np.log(1091)
    lna_final = 0.0

    def rhs(lna, y):
        theta, Pi = y
        a = np.exp(lna)
        H = hubble_lcdm(a, H0, Omega_m, Omega_r)
        # d(H^2)/d(ln a) / (2 H^2) = H_dot / H^2
        # For LCDM: H_dot/H^2 = -(1/2)(3 Omega_m/a^3 + 4 Omega_r/a^4) / (H/H0)^2
        Hsq_over_H0sq = (H / H0)**2
        Hdot_over_Hsq = -0.5 * (3*Omega_m/a**3 + 4*Omega_r/a**4) / Hsq_over_H0sq
        dtheta = Pi
        dPi = -(3 + Hdot_over_Hsq) * Pi - (m / H)**2 * np.sin(theta)
        return [dtheta, dPi]

    # Solve
    sol = solve_ivp(rhs, [lna_init, lna_final], [theta_i, 0.0],
                    method='RK45', rtol=1e-10, atol=1e-12,
                    dense_output=True)

    theta_rec = sol.sol(lna_rec)[0]
    theta_0 = sol.sol(lna_final)[0]
    Pi_0 = sol.sol(lna_final)[1]
    delta_theta = theta_rec - theta_0
    eta = delta_theta / theta_i if theta_i != 0 else 0.0

    # Birefringence (C_agamma=8, alpha=1/137)
    alpha_em = 1.0 / 137.036
    C_agamma = 8.0
    beta_rad = C_agamma * alpha_em * delta_theta / (4 * np.pi)
    beta_deg = np.degrees(beta_rad)

    # Energy density today
    f_a = M_Pl_GeV  # GeV
    H_0_now = hubble_lcdm(1.0, H0, Omega_m, Omega_r)
    rho_a = 0.5 * (f_a * H_0_now * Pi_0)**2 + m**2 * f_a**2 * (1 - np.cos(theta_0))
    # This needs unit conversion -- simplified here
    # Omega_a = (m/H0)^2 * (1 - cos(theta_0)) / 3  (for f_a = M_Pl, kinetic ~ 0)
    Omega_a = (m / H0)**2 * (1 - np.cos(theta_0)) / 3.0

    # Equation of state today
    KE = 0.5 * Pi_0**2 * H_0_now**2  # ~ (d theta/dt)^2 in natural units
    PE = m**2 * (1 - np.cos(theta_0))
    w_a_0 = (KE - PE) / (KE + PE) if (KE + PE) > 0 else -1.0

    return {
        'theta_rec': theta_rec,
        'theta_0': theta_0,
        'delta_theta': delta_theta,
        'eta': eta,
        'beta_rad': beta_rad,
        'beta_deg': beta_deg,
        'Omega_a': Omega_a,
        'w_a_0': w_a_0,
    }
```

### alp_theory.py -- Cobaya Theory Wrapper

```python
"""Cobaya Theory class for ALP birefringence."""
from cobaya.theory import Theory

class ALPBirefringence(Theory):
    # Fixed parameters (can be overridden in yaml)
    f_a_GeV: float = 2.435e18  # M_Pl
    C_agamma: float = 8.0       # SM

    def initialize(self):
        from .alp_ode import solve_alp
        self._solve = solve_alp

    def calculate(self, state, want_derived=True, **params_values):
        theta_i = params_values['theta_i']
        log10_m = params_values['log10_m_eV']

        result = self._solve(theta_i, log10_m)

        state['beta_deg'] = result['beta_deg']
        state['Omega_a'] = result['Omega_a']
        state['w_a_0'] = result['w_a_0']
        state['eta'] = result['eta']

    def get_beta_deg(self):
        return self.current_state['beta_deg']

    def get_can_provide(self):
        return ['beta_deg', 'Omega_a', 'w_a_0', 'eta']
```

### birefringence_lk.py -- Cobaya Likelihood

```python
"""Gaussian likelihood on cosmic birefringence angle."""
from cobaya.likelihood import Likelihood
import numpy as np

class BirefringenceLikelihood(Likelihood):
    beta_obs: float = 0.342    # degrees (Eskilt & Komatsu 2022)
    sigma_beta: float = 0.094  # degrees (1-sigma)

    def initialize(self):
        pass

    def get_requirements(self):
        return {'beta_deg': None}

    def logp(self, **params_values):
        beta_pred = self.provider.get_result('beta_deg')
        chi2 = ((beta_pred - self.beta_obs) / self.sigma_beta)**2
        return -0.5 * chi2
```

## 3. Option B Architecture (Phase 2b, Model 3)

For the ALP-as-DE variant, the ALP must be integrated self-consistently with the background Friedmann equation. Two sub-options:

### Sub-option B1: Custom Background Integrator

- Solve the coupled system {theta, Pi, a} simultaneously
- Feed H(z) to CAMB as a tabulated function (using CAMB's dark energy w(z) interface)
- Advantages: full control, transparent
- Disadvantages: CAMB distance/CMB calculations may not be perfectly consistent if ALP perturbations are ignored

### Sub-option B2: axionCAMB

- Full integration of ALP field + perturbations inside the Boltzmann solver
- Plug into Cobaya via standard CAMB interface with extra axion parameters
- Advantages: fully self-consistent, handles perturbations
- Disadvantages: installation overhead, less transparent

**Recommendation:** Start with B1 for speed, validate against B2 for the final result.

### CAMB w(z) interface for B1

CAMB supports tabulated w(z) for dark energy via the `DarkEnergyFluid` class:

```python
# In CAMB setup:
pars = camb.CAMBparams()
pars.DarkEnergy = camb.dark_energy.DarkEnergyFluid(w=-1.0)  # or tabulated
# For ALP: compute w_a(z) from ODE, pass as tabulated w(z)
```

This approach captures the modified expansion history while keeping the CAMB machinery for CMB computation.

## 4. Validation Plan

Before any MCMC run:

| Test | Expected result | Tolerance |
|------|----------------|-----------|
| m = H_0, theta_i = 1, C = 8 | beta ~ 0.27 deg | +/- 0.02 deg |
| m = H_0, theta_i = 1.3, C = 8 | beta ~ 0.35 deg | +/- 0.02 deg |
| m = 0.01 H_0 (frozen) | beta ~ 0 | < 0.01 deg |
| m = 100 H_0 (oscillating) | beta ~ 0 (averaged) | < 0.05 deg |
| f_a = 0.1 M_Pl vs M_Pl | beta unchanged | < 1% |
| theta_i = pi (top of potential) | beta = C alpha pi / (4 pi) ~ 0.83 deg | +/- 0.05 deg |
| Omega_a for m=H_0, theta_i=1 | ~ 0.15 | +/- 0.05 |
| w_a for m=H_0, theta_i=1 | close to -1 | w_a > -1.1 |

## 5. Computational Cost Estimate

### Option A (Phase 2a)

| Component | Time per eval | Evaluations | Total |
|-----------|-------------|-------------|-------|
| ALP ODE | ~10 ms | 400K | ~1 hr |
| CAMB (if needed) | ~2 s | 0 (not needed for Model 2 with beta-only likelihood) | 0 |
| Beta likelihood | ~0.1 ms | 400K | ~40 s |
| **Total (Model 2, beta-only)** | | | **~1 hr** |
| **Total (Model 2, + Planck lk)** | | | **~200 hrs (need CAMB)** |

For Models 1 and 2 with birefringence-only likelihood: the MCMC is extremely fast since no Boltzmann solver is called. The entire run finishes in about 1 hour on a single CPU core.

For Model 2 with Planck likelihood added: need CAMB at each step. Use the existing RunPod infrastructure (~8 CPU cores), estimated ~25 hrs wall time for 4 chains x 100K samples.

### Option B (Phase 2b)

| Component | Time per eval | Evaluations | Total |
|-----------|-------------|-------------|-------|
| axionCAMB | ~5 s | 800K | ~1100 hrs |
| Planck + BAO likelihood | ~0.5 s | 800K | ~110 hrs |
| **Total (Model 3)** | | | **~150 hrs (8 cores)** |

This is feasible on RunPod over ~1 week. Comparable to the Paper 1 MCMC runs.

## 6. Phase 2a Deliverables

1. `alp_ode.py` -- validated ALP ODE integrator
2. `eta_table.py` -- precomputed eta(m/H_0) for fast lookup
3. `birefringence_lk.py` -- Cobaya likelihood module
4. `model2_alp_biref.yaml` -- production Cobaya config
5. Validation report showing agreement with Phase 1 analytics
6. Prefit grid scan (theta_i vs m/H_0) with beta contours
