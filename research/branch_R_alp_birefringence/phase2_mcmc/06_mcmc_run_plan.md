# Phase 2: MCMC Run Plan

**Date:** 2026-03-16
**Branch:** R Phase 2

---

## 1. Run Schedule

### Phase 2a: Fast Runs (birefringence-only likelihood, no Boltzmann solver)

#### Run 1: LCDM + beta_free (baseline)

- **Purpose:** Establish data-preferred beta independent of ALP model
- **Parameters:** 1 new (beta, in degrees)
- **Likelihood:** Gaussian on beta_obs = 0.342, sigma = 0.094
- **Sampler:** MCMC (trivial 1D problem, but run for pipeline validation)
- **Chains:** 4 x 10K samples
- **Runtime:** < 1 minute
- **Expected result:** beta = 0.342 +/- 0.094 deg (just recovers the input)
- **Purpose of running:** validates likelihood module, establishes baseline chi^2

#### Run 2: LCDM + ALP-biref, minimal (spectator ALP)

- **Purpose:** Map (theta_i, log10_m) posterior with fixed f_a = M_Pl, C = 8
- **Parameters:** 2 new (theta_i, log10_m_eV)
- **Theory:** ALP ODE integrator (alp_ode.py)
- **Likelihood:** Gaussian on beta_obs = 0.342, sigma = 0.094
- **Priors:** theta_i in U[0.01, pi], log10_m in U[-35, -30]
- **Chains:** 4 x 100K samples
- **Convergence:** R-1 < 0.01
- **Runtime:** ~1 hour (CPU only, no CAMB)
- **Expected result:** Banana-shaped posterior in (theta_i, m) plane; eta x theta_i ~ 1.3 contour
- **Deliverables:** Triangle plot, 1D marginalized on theta_i and m, derived beta posterior

#### Run 3: LCDM + ALP-biref, extended C_{a gamma}

- **Purpose:** Map (theta_i, C_{a gamma}) degeneracy
- **Parameters:** 3 new (theta_i, log10_m_eV, C_{a gamma})
- **Theory:** ALP ODE integrator
- **Likelihood:** Gaussian on beta
- **Priors:** theta_i in U[0.01, pi], log10_m in U[-35, -30], C in U[4, 16]
- **Chains:** 4 x 100K samples
- **Runtime:** ~2 hours
- **Expected result:** C x theta_i = const degeneracy direction; m marginally constrained
- **Deliverables:** 3D triangle plot, C vs theta_i contour

### Phase 2a+: Medium Runs (birefringence + Planck + BAO)

#### Run 4: LCDM + ALP-biref + Planck + BAO (spectator, full cosmology)

- **Purpose:** Joint constraint including standard cosmological parameters
- **Parameters:** 8 (6 LCDM + theta_i + log10_m)
- **Theory:** CAMB (standard) + ALP ODE
- **Likelihoods:**
  - Birefringence Gaussian
  - planck_2018_lowl.TT
  - planck_2018_lowl.EE
  - planck_NPIPE_highl_CamSpec.TTTEEE
  - planck_2018_lensing.clik
  - BAO (BOSS + eBOSS, existing configs)
- **Priors:** Standard LCDM + ALP priors from File 4
- **Chains:** 4 x 100K samples (after burn-in)
- **Convergence:** R-1 < 0.01
- **Hardware:** RunPod CPU pods (8 cores per chain, 4 pods)
- **Runtime:** ~20-30 hours wall time
- **Expected result:** ALP parameters largely decoupled from LCDM (since spectator ALP does not affect CMB); mild correlation through H_0 (enters eta via H(z))
- **Deliverables:** Full triangle plot with all 8 parameters, derived quantities (beta, Omega_a, w_a, H_0, S_8)

### Phase 2b: Full Runs (ALP-as-DE)

#### Run 5: ALP-DE + biref + Planck + BAO (Model 3)

- **Purpose:** Test whether ALP can simultaneously be DE and explain birefringence
- **Parameters:** 7 (5 LCDM without Lambda + theta_i + log10_m)
- **Theory:** axionCAMB or CAMB + tabulated w(z) from ALP ODE
- **Likelihoods:** Same as Run 4 + Pantheon+ SN Ia
- **Priors:** Standard LCDM (excluding Omega_Lambda) + ALP priors
- **Chains:** 4 x 200K samples
- **Hardware:** RunPod CPU pods, 4 chains
- **Runtime:** ~5-7 days wall time
- **Expected result:** Based on prefit (File 5): tension between beta and Omega_a. Posterior likely pushed to theta_i ~ 2-3, m ~ 1-2 H_0, with beta_pred ~ 0.10-0.16 deg -- below observed value.
- **Deliverables:** Full Model 3 posterior, w_a(z) reconstruction, chi^2 comparison with Model 2

#### Run 6: ALP-DE + extended (C, f_a free)

- **Purpose:** Explore whether extended parameter space can resolve Model 3 tension
- **Parameters:** 9 (5 LCDM + theta_i + log10_m + log10_f_a + C)
- **Theory:** axionCAMB
- **Likelihoods:** Same as Run 5
- **Chains:** 4 x 200K samples
- **Runtime:** ~7-10 days
- **Expected result:** If beta and Omega_a can be simultaneously matched with C > 12 and f_a < M_Pl, this will show up as a viable region
- **Deliverables:** Determine whether the DE + birefringence tension can be resolved

## 2. Cobaya Configuration Templates

### Run 2 Config (model2_alp_biref.yaml)

```yaml
# ALP birefringence: spectator model, birefringence-only likelihood
# Branch R Phase 2, Run 2

theory:
  alp_birefringence.ALPBirefringence:
    python_path: ./code
    f_a_GeV: 2.435e18  # M_Pl
    C_agamma: 8.0       # SM

likelihood:
  birefringence.BirefringenceLikelihood:
    python_path: ./code
    beta_obs: 0.342
    sigma_beta: 0.094

sampler:
  mcmc:
    burn_in: 0.3
    max_tries: 40d
    Rminus1_stop: 0.01
    Rminus1_cl_stop: 0.15
    learn_proposal: true
    proposal_scale: 2.4
    drag: false

params:
  theta_i:
    prior: {min: 0.01, max: 3.14159}
    ref: {dist: norm, loc: 1.3, scale: 0.3}
    proposal: 0.2
    latex: \theta_i

  log10_m_eV:
    prior: {min: -35, max: -30}
    ref: {dist: norm, loc: -32.5, scale: 0.5}
    proposal: 0.3
    latex: \log_{10}(m_a/\mathrm{eV})

  # Derived parameters
  beta_deg:
    latex: \beta\;[\mathrm{deg}]
  eta:
    latex: \eta
  Omega_a:
    latex: \Omega_a
  w_a_0:
    latex: w_a(z{=}0)

output: chains/run2_alp_biref/alp
```

### Run 4 Config (model2_planck_bao.yaml)

```yaml
# ALP birefringence + Planck + BAO: spectator model, full cosmology
# Branch R Phase 2, Run 4

theory:
  camb:
    path: null
    extra_args:
      lens_potential_accuracy: 1
      num_massive_neutrinos: 1
      theta_H0_range: [40, 100]
  alp_birefringence.ALPBirefringence:
    python_path: ./code
    f_a_GeV: 2.435e18
    C_agamma: 8.0

likelihood:
  birefringence.BirefringenceLikelihood:
    python_path: ./code
    beta_obs: 0.342
    sigma_beta: 0.094
  planck_2018_lowl.TT:
  planck_2018_lowl.EE:
  planck_NPIPE_highl_CamSpec.TTTEEE:
  planck_2018_lensing.clik:
  bao.sixdf_2011_bao:
  bao.sdss_dr7_mgs:
  bao.sdss_dr16_baoplus_lrg:
  bao.sdss_dr16_baoplus_qso:
  bao.sdss_dr16_baoplus_lyauto:
  bao.sdss_dr16_baoplus_lyxqso:

sampler:
  mcmc:
    burn_in: 0.3
    max_tries: 40d
    Rminus1_stop: 0.01
    Rminus1_cl_stop: 0.2
    learn_proposal: true
    learn_proposal_Rminus1_max: 30
    proposal_scale: 2.4
    oversample_power: 0.4
    drag: true

params:
  # Standard LCDM
  logA:
    prior: {min: 1.61, max: 3.91}
    ref: {dist: norm, loc: 3.044, scale: 0.014}
    proposal: 0.001
    latex: \log(10^{10} A_s)
    drop: true
  As:
    value: "lambda logA: 1e-10*np.exp(logA)"
    latex: A_s
  ns:
    prior: {min: 0.8, max: 1.2}
    ref: {dist: norm, loc: 0.9649, scale: 0.0042}
    proposal: 0.002
    latex: n_s
  theta_MC_100:
    prior: {min: 0.5, max: 10}
    ref: {dist: norm, loc: 1.04092, scale: 0.00031}
    proposal: 0.0002
    latex: 100\theta_{MC}
    drop: true
    renames: theta
  cosmomc_theta:
    value: "lambda theta_MC_100: 1.e-2*theta_MC_100"
    derived: false
  H0:
    latex: H_0 \; [\mathrm{km/s/Mpc}]
    min: 40
    max: 100
  ombh2:
    prior: {min: 0.005, max: 0.1}
    ref: {dist: norm, loc: 0.02237, scale: 0.00015}
    proposal: 0.0001
    latex: \Omega_b h^2
  omch2:
    prior: {min: 0.001, max: 0.99}
    ref: {dist: norm, loc: 0.1200, scale: 0.0012}
    proposal: 0.0005
    latex: \Omega_c h^2
  tau:
    prior: {min: 0.01, max: 0.8}
    ref: {dist: norm, loc: 0.054, scale: 0.007}
    proposal: 0.003
    latex: \tau_\mathrm{reio}

  # ALP parameters
  theta_i:
    prior: {min: 0.01, max: 3.14159}
    ref: {dist: norm, loc: 1.3, scale: 0.3}
    proposal: 0.2
    latex: \theta_i
  log10_m_eV:
    prior: {min: -35, max: -30}
    ref: {dist: norm, loc: -32.5, scale: 0.5}
    proposal: 0.3
    latex: \log_{10}(m_a/\mathrm{eV})

  # Derived
  sigma8:
    latex: \sigma_8
  S8:
    derived: "lambda sigma8, omegam: sigma8*np.sqrt(omegam/0.3)"
    latex: S_8
  omegam:
    latex: \Omega_m
  age:
    latex: '{\rm{Age}}/\mathrm{Gyr}'
  beta_deg:
    latex: \beta\;[\mathrm{deg}]
  eta:
    latex: \eta
  Omega_a:
    latex: \Omega_a
  w_a_0:
    latex: w_a(z{=}0)

output: chains/run4_alp_planck_bao/alp
```

## 3. Hardware & Cost

### RunPod Configuration

Based on existing Paper 1 infrastructure:

| Run | Instance type | Cores | Chains | Wall time | Cost (~) |
|-----|-------------|-------|--------|-----------|----------|
| Run 1 | Local laptop | 4 | 4 | 1 min | $0 |
| Run 2 | Local laptop | 4 | 4 | 1 hr | $0 |
| Run 3 | Local laptop | 4 | 4 | 2 hr | $0 |
| Run 4 | RunPod CPU (4x) | 8/pod | 4 | 25 hr | ~$20 |
| Run 5 | RunPod CPU (4x) | 8/pod | 4 | 150 hr | ~$120 |
| Run 6 | RunPod CPU (4x) | 8/pod | 4 | 200 hr | ~$160 |

**Total estimated cost:** ~$300 for the full program.

### Deployment

Reuse the existing RunPod deployment scripts from Paper 1:
1. Spin up CPU pods with Cobaya + CAMB pre-installed
2. Upload ALP likelihood/theory modules
3. Upload Cobaya configs
4. Launch chains in parallel
5. Monitor convergence via existing mcmc_monitor scripts
6. Download chains for post-processing

## 4. Convergence Diagnostics

Same as Paper 1 pipeline:

| Diagnostic | Target | Tool |
|-----------|--------|------|
| Gelman-Rubin R-1 | < 0.01 | GetDist |
| Effective sample size N_eff | > 1000 per param | GetDist |
| Mean acceptance rate | 20-40% | Cobaya logs |
| Chain visual inspection | No obvious stuck regions | Manual |
| Burn-in fraction | 30% discarded | Cobaya config |

## 5. Post-Processing

### Immediate outputs (automated)

1. **Triangle plots** via GetDist: all sampled + derived parameters
2. **1D marginalized posteriors** with 68% and 95% credible intervals
3. **2D contour plots**: theta_i vs C_{a gamma}, theta_i vs log10_m, beta vs Omega_a
4. **Best-fit chi^2** and model comparison statistics

### Analysis deliverables

1. **Bayes factor** computation: ALP model vs null (beta = 0) and vs beta_free
   - Method: Savage-Dickey density ratio (for nested models) or harmonic mean estimator
   - Or: run PolyChord for evidence computation
2. **Parameter constraints table** for paper
3. **w_a(z) reconstruction** from Model 3 posterior
4. **Forecast for LiteBIRD** -- how much the posteriors tighten with sigma(beta) ~ 0.01 deg

## 6. Run Priority

| Priority | Run | Rationale |
|----------|-----|-----------|
| 1 (immediate) | Run 2 | Core result: ALP parameter posterior from birefringence |
| 2 (immediate) | Run 3 | Degeneracy mapping: C vs theta_i |
| 3 (next) | Run 4 | Full cosmology joint fit |
| 4 (if warranted) | Run 5 | ALP-as-DE test (prefit suggests tension) |
| 5 (if warranted) | Run 6 | Extended parameters to resolve tension |

Start Runs 2 and 3 locally. Deploy Run 4 to RunPod. Runs 5-6 only after assessing Run 4 results.
