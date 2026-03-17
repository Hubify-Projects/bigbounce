# MCMC Run 1 Implementation Plan

**Date:** 2026-03-17
**Model:** LCDM + spectator ALP birefringence (Model 2)

---

## 1. Model Definition

LCDM background + one spectator ALP with:
- theta_i: initial misalignment angle (sampled)
- log10_m_eV: log10(m_a / eV) (sampled)
- f_a = M_Pl = 2.435e18 GeV (fixed)
- C_{agamma} = 8 (fixed)

The ALP does not affect the background cosmology (spectator). It only produces birefringence.

---

## 2. Files to Implement

All files go in `reproducibility/cosmology/alp_birefringence/`:

### File 1: `alp_ode.py`

**Purpose:** Integrate the ALP equation of motion on an LCDM background to compute the rolling efficiency eta(m/H_0, theta_i).

**What it must compute:**

1. Set up LCDM background: H(z) = H_0 sqrt(Omega_m (1+z)^3 + Omega_Lambda)
   - Use fiducial Omega_m = 0.315, H_0 = 67.36 km/s/Mpc

2. Integrate the ALP EOM in conformal time tau:
   ```
   phi'' + 2 a H phi' + a^2 m^2 f_a sin(phi/f_a) = 0
   ```
   where primes are d/d(tau) and a is the scale factor.

   Equivalently, in terms of theta = phi/f_a and using cosmic time t:
   ```
   theta_ddot + 3 H(t) theta_dot + m^2 sin(theta) = 0
   ```

3. Initial conditions at z_init = 3000 (well before recombination):
   - theta(z_init) = theta_i
   - theta_dot(z_init) = 0 (Hubble friction has frozen the field)

4. Integrate from z_init to z = 0 using scipy.integrate.solve_ivp (RK45 or DOP853).

5. Compute:
   - theta_rec = theta(z = 1089.8) (at recombination)
   - theta_0 = theta(z = 0) (today)
   - eta = (theta_rec - theta_0) / theta_i
   - beta_rad = C * alpha_em * (theta_rec - theta_0) / (4 * pi)
   - beta_deg = beta_rad * 180 / pi

6. Also compute derived quantities:
   - Omega_a = rho_a / rho_crit where rho_a = m^2 f_a^2 (1 - cos theta_0) + f_a^2 theta_dot_0^2 / 2
   - w_a = (KE - PE) / (KE + PE)

**Interface:**
```python
def compute_alp_birefringence(theta_i, log10_m_eV, f_a_GeV=2.435e18, C_agamma=8.0,
                               Omega_m=0.315, H0_km_s_Mpc=67.36):
    """
    Returns dict with keys:
        'beta_deg': birefringence angle in degrees
        'eta': rolling efficiency
        'theta_rec': field value at recombination
        'theta_0': field value today
        'Omega_a': ALP energy density fraction today
        'w_a_0': ALP equation of state today
    """
```

**Validation:**
- For m >> H_0 (e.g. log10_m = -30): eta -> 1, beta -> C alpha theta_i / (4 pi) = 0.27 deg for theta_i = 1
- For m << H_0 (e.g. log10_m = -36): eta -> 0, beta -> 0
- For m = H_0 (log10_m ~ -33.1): eta ~ 0.2, beta ~ 0.05 deg for theta_i = 1

### File 2: `alp_theory.py`

**Purpose:** Cobaya Theory class that wraps `alp_ode.py`.

**What it must expose:**

```python
from cobaya.theory import Theory

class ALPBirefringence(Theory):
    """Cobaya Theory provider for spectator ALP birefringence."""

    # Class-level parameters
    f_a_GeV: float = 2.435e18
    C_agamma: float = 8.0

    def initialize(self):
        """Pre-compute any lookup tables if desired."""
        pass

    def get_requirements(self):
        """No requirements from other theories (spectator model)."""
        return {}

    def calculate(self, state, want_derived=True, **params_values):
        """Compute birefringence from theta_i and log10_m_eV."""
        theta_i = params_values['theta_i']
        log10_m_eV = params_values['log10_m_eV']

        result = compute_alp_birefringence(theta_i, log10_m_eV,
                                            self.f_a_GeV, self.C_agamma)

        state['beta_deg'] = result['beta_deg']
        state['eta'] = result['eta']
        state['Omega_a'] = result['Omega_a']
        state['w_a_0'] = result['w_a_0']

    def get_beta_deg(self):
        return self.current_state['beta_deg']

    def get_can_provide(self):
        return ['beta_deg', 'eta', 'Omega_a', 'w_a_0']

    def get_derived(self):
        return {
            'beta_deg': self.current_state['beta_deg'],
            'eta': self.current_state['eta'],
            'Omega_a': self.current_state['Omega_a'],
            'w_a_0': self.current_state['w_a_0'],
        }
```

### File 3: `birefringence_lk.py`

**Purpose:** Cobaya Likelihood class for cosmic birefringence measurement.

**What it must evaluate:**

```python
from cobaya.likelihood import Likelihood

class BirefringenceLikelihood(Likelihood):
    """Gaussian likelihood on observed birefringence angle."""

    beta_obs: float = 0.342  # degrees (Eskilt et al. 2025 combined)
    sigma_beta: float = 0.094  # degrees

    def initialize(self):
        pass

    def get_requirements(self):
        return {'beta_deg': None}

    def logp(self, **params_values):
        beta_pred = self.provider.get_param('beta_deg')
        chi2 = ((beta_pred - self.beta_obs) / self.sigma_beta) ** 2
        return -0.5 * chi2
```

### File 4: `run2_config.yaml`

Cobaya configuration for Run 2 (from Branch R Phase 2 File 6, already written).
Copy from `research/branch_R_alp_birefringence/phase2_mcmc/06_mcmc_run_plan.md` Run 2 config section.

### File 5: `validate_alp.py`

**Purpose:** Quick validation script to test the ODE integrator before MCMC.

**Tests:**
1. Reproduce the Phase 2 prefit table (eta vs m/H_0 for several theta_i values)
2. Verify beta -> 0.27 deg for theta_i = 1, m >> H_0
3. Verify beta -> 0 for m << H_0
4. Verify Omega_a ~ 0.68 for m ~ 1.5 H_0, theta_i ~ 1.3
5. Plot beta(m/H_0) for theta_i = 0.5, 1.0, 2.0
6. Time a single evaluation (must be < 0.1 sec for MCMC to be feasible)

### File 6: `plot_results.py`

**Purpose:** Post-processing script for MCMC chains.

**Outputs:**
1. Triangle plot: theta_i vs log10_m_eV (with beta_deg and eta as derived)
2. 1D marginalized posteriors for theta_i, log10_m_eV, beta_deg
3. Best-fit values and 68%/95% credible intervals
4. Comparison overlay: predicted vs observed beta
5. Bayes factor: ALP model vs null (beta = 0)

---

## 3. Run Order

### Step 1: Implement and validate (local, ~2 hours)

1. Write `alp_ode.py`
2. Write `validate_alp.py`
3. Run validation. Fix any issues.
4. Confirm single evaluation < 0.1 sec.

### Step 2: Write Cobaya classes (local, ~1 hour)

5. Write `alp_theory.py`
6. Write `birefringence_lk.py`
7. Write `run2_config.yaml`
8. Test with Cobaya's `cobaya-run --test` to verify configuration loads

### Step 3: Quick local MCMC (local, ~1 hour)

9. Run 4 chains x 10K samples (quick convergence check)
10. Check: chains mix, acceptance rate 20-40%, R-1 decreasing
11. If stable, proceed to full run

### Step 4: Full local MCMC (local, ~1-3 hours)

12. Run 4 chains x 100K samples
13. Target R-1 < 0.01
14. Monitor with existing mcmc_monitor scripts

### Step 5: Post-processing (local, ~30 min)

15. Run `plot_results.py`
16. Generate triangle plot and summary statistics
17. Compute Bayes factor via Savage-Dickey

### Step 6: Sanity check results

18. Verify theta_i posterior peaks near 1.0-1.5
19. Verify log10_m posterior is broad (birefringence-only run has weak mass constraint)
20. Verify derived beta_deg posterior encompasses observed value
21. Verify no pathological features (multimodality, rails against prior edges)

---

## 4. Expected Results

From the Phase 2 prefit analysis:

| Parameter | Expected posterior |
|-----------|-------------------|
| theta_i | Broad, peaked ~1.3, 95% CI [0.4, 2.6] |
| log10_m_eV | Mostly unconstrained for m > few H_0; lower bound from eta requirement |
| beta_deg (derived) | 0.34 +/- 0.09 (mirrors data) |
| eta (derived) | ~1 for most of posterior (m > few H_0) |

The banana-shaped degeneracy eta x theta_i ~ const will be visible in the 2D posterior.

---

## 5. What This Run Does NOT Do

- Does NOT include Planck CMB likelihood (that's Run 4)
- Does NOT test ALP-as-DE (that's Run 5)
- Does NOT float C_{agamma} (that's Run 3)
- Does NOT include BAO or SN data
- Does NOT modify the background cosmology (LCDM assumed)

This is a pure birefringence-constraint run. It answers: "What (theta_i, m_a) values are consistent with the observed beta?"

---

## 6. Success Criteria

| Criterion | Target |
|-----------|--------|
| R-1 convergence | < 0.01 |
| N_eff per parameter | > 1000 |
| Acceptance rate | 20-40% |
| Runtime | < 3 hours local |
| beta_deg posterior includes observed value | YES |
| No pathological features | YES |

If all criteria pass, this run produces the first ALP constraint figure for the salvaged Paper 1.
