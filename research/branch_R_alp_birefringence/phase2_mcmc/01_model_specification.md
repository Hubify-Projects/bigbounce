# Phase 2: ALP Birefringence MCMC -- Model Specification

**Date:** 2026-03-16
**Branch:** R Phase 2
**Scope:** Generic Planck-scale ALP phenomenology (NOT ECH-specific)

---

## 1. Field Theory on FRW Background

### Equation of motion

The ALP field a with decay constant f_a obeys, on an FRW background:

$$\ddot{a} + 3H\dot{a} + m^2 f_a \sin\!\left(\frac{a}{f_a}\right) = 0$$

Defining the dimensionless angle theta = a / f_a:

$$\ddot{\theta} + 3H\dot{\theta} + m^2 \sin(\theta) = 0$$

where H = H(t) is determined by the full Friedmann equation including the ALP itself (for the ALP-as-DE variant) or by standard LCDM (for the spectator variant).

### Energy density and pressure

$$\rho_a = \frac{1}{2} f_a^2 \dot{\theta}^2 + m^2 f_a^2 (1 - \cos\theta)$$

$$p_a = \frac{1}{2} f_a^2 \dot{\theta}^2 - m^2 f_a^2 (1 - \cos\theta)$$

### Equation of state

$$w_a = \frac{p_a}{\rho_a} = \frac{\frac{1}{2}\dot{\theta}^2 - m^2(1-\cos\theta)}{\frac{1}{2}\dot{\theta}^2 + m^2(1-\cos\theta)}$$

Limiting behavior:
- **Frozen regime** (H >> m): theta_dot -> 0, so w_a -> -1 (cosmological constant)
- **Oscillating regime** (H << m): time-averaged <w_a> -> 0 (pressureless matter)
- **Transition** (H ~ m): w_a smoothly rises from -1 toward 0

### Continuity equation (self-consistency check)

$$\dot{\rho}_a + 3H(\rho_a + p_a) = 0$$

This is automatically satisfied by the EOM. Useful as a numerical diagnostic.

## 2. Birefringence Angle

The cosmic birefringence angle from ALP-photon coupling is:

$$\beta = \frac{g_{a\gamma}}{2}\left[\phi(z=0) - \phi(z_{\rm rec})\right] = \frac{g_{a\gamma}}{2}\,f_a\left[\theta(z=0) - \theta(z_{\rm rec})\right]$$

Substituting g_{a gamma} = C_{a gamma} alpha / (2 pi f_a):

$$\boxed{\beta = \frac{C_{a\gamma}\,\alpha}{4\pi}\left[\theta(z_{\rm rec}) - \theta(z=0)\right]}$$

Note the sign: theta(z_rec) > theta(z=0) since the field rolls toward zero, giving beta > 0.

### Rolling efficiency parametrization

Define:

$$\eta(m/H_0, \theta_i) \equiv \frac{\theta(z_{\rm rec}) - \theta(z=0)}{\theta_i}$$

Then:

$$\beta = \frac{C_{a\gamma}\,\alpha\,\theta_i}{4\pi}\,\eta(m/H_0, \theta_i)$$

For m ~ H_0 and theta_i ~ O(1): eta ~ 0.5 -- 1.0 (from numerical integration).

**Key property:** f_a cancels completely in this expression. The birefringence prediction depends only on (C_{a gamma}, alpha, theta_i, m/H_0).

## 3. Three Model Variants

### Model 1: LCDM + beta_free (phenomenological baseline)

- Standard 6 LCDM parameters
- 1 new parameter: beta (the birefringence angle, free)
- No ALP dynamics -- beta is just a number
- Purpose: establish the data-preferred beta independent of any model
- Degrees of freedom: 7 total (6 LCDM + 1)

### Model 2: LCDM + ALP-birefringence (spectator ALP)

- Standard 6 LCDM parameters (Lambda still provides DE)
- 2 new parameters: {theta_i, log10(m_a/eV)}
- Fixed: f_a = M_Pl, C_{a gamma} = 8
- ALP is a subdominant spectator that provides birefringence only
- Constraint: rho_a << rho_crit (enforced as prior)
- beta is a derived parameter computed from ALP dynamics
- Degrees of freedom: 8 total (6 LCDM + 2), but beta effectively removes one LCDM DOF (Lambda)... no: Lambda is independent since ALP is spectator
- Purpose: test whether ALP dynamics naturally predict the observed beta

### Model 3: ALP-DE + birefringence (ALP replaces Lambda)

- 5 LCDM parameters (Lambda REMOVED)
- 2 new parameters: {theta_i, log10(m_a/eV)}
- Fixed: f_a = M_Pl, C_{a gamma} = 8
- ALP provides BOTH dark energy AND birefringence
- Omega_a is a derived parameter (must match Omega_DE ~ 0.68)
- w_a(z) is a derived function (must be close to -1 at low z)
- Degrees of freedom: 7 total (5 LCDM + 2), same count as LCDM + beta_free
- Purpose: test whether a single field simultaneously explains DE and birefringence
- **Requires** modified background evolution (Option B implementation)

### Model comparison table

| Model | New params | Total DOF | beta | DE | Implementation |
|-------|-----------|-----------|------|-----|----------------|
| 1. LCDM + beta_free | beta | 7 | free | Lambda | Trivial |
| 2. LCDM + ALP-biref | theta_i, log(m) | 8 | derived | Lambda | Option A |
| 3. ALP-DE + biref | theta_i, log(m) | 7 | derived | ALP | Option B |

## 4. Parameter Sets

### Minimal parameter set (Models 2 & 3)

| Parameter | Symbol | Type | Notes |
|-----------|--------|------|-------|
| Initial misalignment | theta_i | sampled | O(1) natural |
| ALP mass | log10(m_a/eV) | sampled | DE regime: ~ -33 |
| Decay constant | f_a | fixed = M_Pl | f_a drops out of beta |
| Anomaly coefficient | C_{a gamma} | fixed = 8 | SM value |

### Extended parameter set (future)

| Parameter | Symbol | Type | Notes |
|-----------|--------|------|-------|
| theta_i | sampled | same | |
| log10(m_a/eV) | sampled | same | |
| log10(f_a/GeV) | sampled | allows sub/super-Planckian |
| C_{a gamma} | sampled | allows BSM charged matter |

### Standard LCDM parameters (all models)

| Parameter | Symbol | Reference value |
|-----------|--------|----------------|
| Baryon density | omega_b h^2 | 0.02237 |
| CDM density | omega_c h^2 | 0.1200 |
| Acoustic scale | 100 theta_MC | 1.04092 |
| Optical depth | tau | 0.054 |
| Scalar amplitude | ln(10^10 A_s) | 3.044 |
| Scalar tilt | n_s | 0.9649 |

## 5. Derived Quantities

For each point in parameter space, compute:

| Quantity | Formula | Purpose |
|----------|---------|---------|
| beta (deg) | C_{a gamma} alpha theta_i eta / (4 pi) x (180/pi) | Compare to data |
| Omega_a | rho_a / (3 H_0^2 M_Pl^2) | DE fraction (Model 3) |
| w_a(z=0) | from EOM integration | DE EOS |
| w_a(z=0.5) | from EOM integration | DESI comparison |
| g_{a gamma} | C_{a gamma} alpha / (2 pi f_a) | Coupling strength |
| rho_a / rho_crit | m^2 f_a^2 (1 - cos theta_i) / rho_crit | Energy budget |

## 6. Numerical Integration Specification

The ALP EOM theta'' + 3H theta' + m^2 sin(theta) = 0 must be integrated from z_init = 1200 (well before recombination, z_rec ~ 1090) to z = 0.

### Independent variable

Use ln(a) = -ln(1+z) as the time variable (converts second-order ODE to a system):

$$\frac{d\theta}{d\ln a} = \Pi$$

$$\frac{d\Pi}{d\ln a} = -\left(3 + \frac{\dot{H}}{H^2}\right)\Pi - \frac{m^2}{H^2}\sin(\theta)$$

where H(a) is from the background cosmology and H_dot/H^2 = -(3/2)(1 + w_eff(a)) with w_eff from the matter/radiation/DE content.

### Initial conditions at z_init = 1200

- theta(z_init) = theta_i (frozen, since H(z_init) >> m for m ~ H_0)
- Pi(z_init) = 0 (negligible velocity in frozen regime)

### Background cosmology

For Models 1 and 2: use standard LCDM Friedmann equation.

For Model 3: H^2 includes rho_a self-consistently. This requires coupled integration of the ALP + Friedmann system.

### Output

- theta(z=0) and theta(z_rec = 1090) for computing beta
- rho_a(z=0) for computing Omega_a
- w_a(z) at selected redshifts for DE diagnostics
