# Branch R: ALP Cosmic Birefringence -- Parameter Scan Design

**Date:** 2026-03-16

---

## 1. Parameter Space

### Free parameters:

| Parameter | Symbol | Prior | Range | Fiducial |
|-----------|--------|-------|-------|----------|
| Decay constant | log10(f_a / GeV) | Uniform | [16, 19] | 18.39 (M_Pl) |
| ALP mass | log10(m_phi / eV) | Uniform | [-34, -28] | -32.8 (~H_0) |
| Misalignment angle | theta_i | Uniform | [0, pi] | 1.0 |
| Anomaly coefficient | C_{agamma} | Uniform | [6, 14] | 8 (SM) |

### Derived parameters:

| Parameter | Formula |
|-----------|---------|
| g_{agamma} | C_{agamma} alpha / (2 pi f_a) |
| eta(m/H_0) | Numerical from EOM integration |
| beta | C_{agamma} alpha theta_i eta / (4 pi) |
| rho_phi / rho_crit | m^2 f_a^2 theta_i^2 / (2 rho_crit) |

## 2. Likelihood

### Primary observable: birefringence angle beta

$$-2 \ln L = \left(\frac{\beta_{\rm pred} - \beta_{\rm obs}}{\sigma_\beta}\right)^2$$

with beta_obs = 0.35 deg, sigma_beta = 0.09 deg.

### Secondary constraints (as priors or additional likelihoods):

| Constraint | Implementation |
|------------|---------------|
| rho_phi < rho_crit | Hard prior: m^2 f_a^2 theta_i^2 / 2 < 3 H_0^2 M_Pl^2 |
| Isocurvature | Gaussian prior on H_inf: sigma(beta_iso) < Planck bound |
| Stability | theta_i < pi (field starts on the correct side of the potential) |

## 3. Degeneracy Structure

The key analytic result beta = C_{agamma} alpha theta_i / (4 pi) (valid for m ~ H_0) reveals:

### Exact degeneracy: C_{agamma} x theta_i = const

For m in the sweet spot (m ~ H_0), beta depends only on the product C_{agamma} theta_i:

$$\beta = \frac{\alpha}{4\pi} \times (C_{a\gamma} \theta_i)$$

This means:
- C_{agamma} = 8, theta_i = 1.3 gives same beta as C_{agamma} = 10, theta_i = 1.04
- The data constrains only the product, not the individual parameters
- Breaking this degeneracy requires independent information (e.g., from particle physics model or cosmological perturbations)

### f_a independence (in the sweet-spot regime)

beta is completely independent of f_a when Delta_phi = f_a theta_i. The MCMC will show a flat posterior in f_a within the mass sweet spot.

### Mass dependence through eta(m/H_0)

The field excursion fraction eta breaks the simplicity:

| m / H_0 | eta | Physical regime |
|---------|-----|----------------|
| 0.01 | ~0 | Frozen today, no birefringence |
| 0.1 | ~0.05 | Barely rolling |
| 0.5 | ~0.3 | Beginning transition |
| 1 | ~0.7 | Sweet spot |
| 3 | ~1.0 | Full excursion, beginning oscillation |
| 10 | ~0 (averaged) | Oscillating, averaged Delta_phi ~ 0 |

**Note:** The eta values above are schematic. Precise values require numerical integration of the EOM on the full expansion history. This is a key deliverable for the Phase 1 pipeline.

## 4. MCMC Configuration

### Sampler settings (Cobaya):

```yaml
sampler:
  mcmc:
    burn_in: 0.3
    max_tries: 10000
    Rminus1_stop: 0.01
    Rminus1_cl_stop: 0.15
    learn_proposal: true
    proposal_scale: 2.4
    covmat: null  # Start fresh, no prior covariance

params:
  log_fa:
    prior:
      min: 16
      max: 19
    ref: 18.39
    proposal: 0.5
    latex: \log_{10}(f_a/\mathrm{GeV})

  log_m:
    prior:
      min: -34
      max: -28
    ref: -32.8
    proposal: 0.5
    latex: \log_{10}(m_\phi/\mathrm{eV})

  theta_i:
    prior:
      min: 0.01
      max: 3.14159
    ref: 1.0
    proposal: 0.3
    latex: \theta_i

  C_agamma:
    prior:
      min: 6
      max: 14
    ref: 8
    proposal: 1.0
    latex: C_{a\gamma}

theory:
  alp_birefringence:
    python_path: ./theory

likelihood:
  birefringence:
    python_path: ./likelihood
    beta_obs: 0.35
    sigma_beta: 0.09
```

### Chain configuration:
- **Chains:** 8 (for robust R-hat convergence)
- **Target samples:** 50,000 per chain (after burn-in)
- **Expected runtime:** ~1 hour on CPU (no Boltzmann solver needed for Phase 1)
- **Convergence criterion:** R-1 < 0.01

## 5. Expected Posterior Structure

### 1D marginals:

- **theta_i:** Peaked near 1.3, broad due to C_{agamma} degeneracy
- **C_{agamma}:** Peaked near 10-11 (if theta_i ~ 1), broad
- **log_m:** Band around log10(m/eV) ~ [-33.5, -32.0] (sweet spot)
- **log_fa:** Flat (unconstrained by beta alone)

### 2D correlations:

- **C_{agamma} vs theta_i:** Strong negative correlation (banana-shaped contour along C_{agamma} theta_i ~ 10.5)
- **log_m vs theta_i:** Curved correlation (lower m needs higher theta_i to compensate reduced eta)
- **log_fa vs anything:** Uncorrelated (flat)

### Triangle plot expectations:

The posterior will be highly non-Gaussian due to:
1. The multiplicative degeneracy C_{agamma} x theta_i
2. The nonlinear eta(m/H_0) mapping
3. Prior boundaries (theta_i < pi, C_{agamma} > 0)

This motivates nested sampling as a cross-check (PolyChord or MultiNest via Cobaya).

## 6. Phase 1 vs Phase 2

### Phase 1 (this scan): Direct beta likelihood
- Use analytic formula + eta lookup table
- Fast: minutes to hours on CPU
- Sufficient to map degeneracies and identify favored regions

### Phase 2 (future): Full CMB likelihood
- Use axionCAMB for self-consistent field evolution
- Fit to Planck + ACT power spectra (TT, TE, EE, BB, TB, EB)
- Simultaneously constrain ALP parameters and standard cosmology
- Slow: days on GPU cluster
- Required for publication-quality constraints

## 7. Output Deliverables

1. Posterior samples in GetDist-compatible format
2. Triangle plot: (theta_i, C_{agamma}, log_m, log_fa)
3. 1D marginalized constraint on beta
4. 2D contour: C_{agamma} vs theta_i (showing degeneracy direction)
5. 1D profile: beta(m) showing the sweet-spot mass range
6. Model comparison: Bayes factor vs beta = 0 (null hypothesis)
