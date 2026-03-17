# Branch R: ALP Cosmic Birefringence -- Data & Pipeline Setup

**Date:** 2026-03-16

---

## 1. Observational Data

### 1.1 Planck PR4 (NPIPE) Polarization

- **Dataset:** Planck 2020 NPIPE reprocessed maps (PR4)
- **Key reference:** Minami & Komatsu (2020), PRL 125, 221301
- **Method:** Simultaneous fit of cosmic birefringence angle beta and instrumental miscalibration angles alpha_i for each detector
- **Result:** beta = 0.35 +/- 0.14 deg (2.4 sigma with PR4 alone)
- **Multipole range:** ell = 51 -- 1500 (TB and EB cross-spectra)
- **Key insight:** The D-estimator exploits the fact that miscalibration rotates both TB and EB spectra identically across detectors, while cosmic birefringence rotates them identically across the sky

### 1.2 ACT DR6 Polarization

- **Dataset:** Atacama Cosmology Telescope Data Release 6
- **Key reference:** Eskilt et al. (2024)
- **Method:** Same D-estimator methodology applied to ACT maps
- **Result (combined):** beta = 0.35 +/- 0.09 deg (3.9 sigma with Planck + ACT)
- **Multipole range:** extends to ell ~ 4000
- **Advantage:** Higher resolution than Planck, independent systematics

### 1.3 Future Data

- **LiteBIRD** (launch ~2032): sigma(beta) ~ 0.01 deg, definitive test
- **CMB-S4** (first light ~2029): sigma(beta) ~ 0.03 deg from ground
- **Simons Observatory** (operating): sigma(beta) ~ 0.05 deg
- **BICEP Array**: complementary at large angular scales

## 2. Minami-Komatsu D-Estimator Methodology

The measurement relies on cross-correlating TB and EB spectra:

### Signal model

Cosmic birefringence rotates the CMB polarization:
$$\tilde{E}_\ell = E_\ell \cos(2\beta) - B_\ell \sin(2\beta)$$
$$\tilde{B}_\ell = E_\ell \sin(2\beta) + B_\ell \cos(2\beta)$$

This generates nonzero TB and EB spectra from the primordial EE spectrum:
$$C_\ell^{TE,\rm obs} \supset -C_\ell^{TE} \sin(2\beta)$$
$$C_\ell^{EB,\rm obs} \supset \frac{1}{2} C_\ell^{EE} \sin(4\beta) \approx 2\beta \, C_\ell^{EE}$$

### Instrumental miscalibration degeneracy

Detector polarization angle miscalibration alpha_det produces identical rotation. The D-estimator breaks this degeneracy by:
1. Using multiple detectors with independent miscalibration angles
2. Fitting beta (global) and alpha_i (per detector) simultaneously
3. The cosmic signal is coherent across detectors; miscalibration is not

### Frequency dependence

- Cosmic birefringence from ALPs is frequency-independent (it is a geometric rotation)
- Galactic foreground birefringence (Faraday rotation) scales as nu^{-2}
- Multi-frequency data separates the two

## 3. Existing Pipeline Compatibility

### Current infrastructure (from Paper 1 MCMC):

| Component | Status | Modification needed |
|-----------|--------|-------------------|
| Cobaya sampler | Operational, RunPod-deployed | Minimal -- add new likelihood |
| CAMB Boltzmann solver | Operational | May need axionCAMB for m ~ H_0 dynamics |
| Planck lite likelihood | Available | Need polarization-specific EB/TB likelihood |
| RunPod GPU cluster | Available | Same hardware, new job configs |
| Chain convergence monitoring | Operational | Reuse existing R-hat diagnostics |

### What maps directly:
- Cobaya MCMC framework (sampler, convergence diagnostics, chain management)
- RunPod deployment scripts
- Post-processing and visualization tools

### What needs modification or addition:
- New likelihood module for beta measurement
- Possibly modified CAMB for ALP field evolution
- New parameter priors for (f_a, m, theta_i, C_{agamma})

## 4. Likelihood Modifications

### Option A: Direct beta likelihood (simplest, recommended for Phase 1)

Since beta = C_{agamma} alpha theta_i / (4 pi) is independent of f_a (in the m ~ H_0 regime), the simplest approach:

```python
# Pseudocode for Cobaya likelihood
class ALPBirefringenceLikelihood:
    """
    Gaussian likelihood on the birefringence angle.
    """
    beta_obs = 0.35  # degrees
    sigma_beta = 0.09  # degrees

    def logp(self, C_agamma, theta_i, m_phi, f_a):
        # Compute predicted beta
        alpha_em = 1.0 / 137.036

        # Field excursion fraction eta(m/H0)
        eta = self.compute_eta(m_phi, f_a, theta_i)

        # beta = (C_agamma * alpha / (4*pi)) * theta_i * eta
        beta_pred = (C_agamma * alpha_em * theta_i * eta) / (4 * np.pi)
        beta_pred_deg = np.degrees(beta_pred)

        # Gaussian likelihood
        chi2 = ((beta_pred_deg - self.beta_obs) / self.sigma_beta)**2
        return -0.5 * chi2

    def compute_eta(self, m_phi, f_a, theta_i):
        """
        Field excursion fraction: Delta_phi / (f_a * theta_i)
        eta = 1 for m >> H0 (full excursion before today)
        eta ~ 0 for m << H0 (still frozen)
        eta ~ O(1) for m ~ H0
        Requires numerical integration of EOM.
        """
        pass  # Implement via ODE solver or lookup table
```

### Option B: Full Boltzmann integration (Phase 2)

For precision work and to capture:
- Scale-dependent birefringence (if m not much less than H_rec)
- Impact on CMB power spectra (EE, TE shifts)
- Correlation with other cosmological parameters

This requires **axionCAMB** or equivalent:
- Modified CAMB that evolves the ALP field self-consistently
- Computes the rotation angle as a function of multipole ell
- Handles the transition from frozen to rolling regime

**axionCAMB:** https://github.com/dgrin1/axionCAMB
- Well-tested for ultralight axions
- Includes perturbation evolution
- Compatible with Cobaya via CambCalculator wrapper

## 5. Pipeline Architecture (Phase 1)

```
Cobaya MCMC
  |
  |-- Parameters: {theta_i, C_agamma, m_phi}
  |     (f_a fixed at M_Pl for Phase 1)
  |
  |-- Theory:
  |     beta(theta_i, C_agamma, m_phi) via analytic formula + eta lookup
  |
  |-- Likelihood:
  |     L(beta_obs | beta_pred) = Gaussian(0.35, 0.09)
  |
  |-- Sampler: MCMC (4+ chains, R-1 < 0.01)
  |
  |-- Output: posteriors on (theta_i, C_agamma, m_phi)
```

## 6. Data Access Checklist

- [ ] Planck PR4/NPIPE polarization maps (publicly available via PLA)
- [ ] ACT DR6 polarization maps (publicly available)
- [ ] Minami-Komatsu beta measurement covariance (from published papers)
- [ ] Eskilt et al. combined Planck+ACT beta posterior (from published papers)
- [ ] axionCAMB installation and validation (GitHub)
- [ ] Cobaya ALP likelihood module (write new)

## 7. Validation Tests

Before running production MCMC:

1. **Analytic limit:** Verify that for m = H_0, theta_i = 1, C_{agamma} = 8, the code returns beta ~ 0.27 deg
2. **f_a independence:** Verify beta is constant as f_a varies (with m ~ H_0 and Delta_phi ~ f_a theta_i)
3. **Mass dependence:** Verify beta -> 0 for m << H_0 and m >> H_0
4. **Comparison to literature:** Cross-check against Fujita, Murai, Nakagawa & Obata (2021) Table 1
5. **Chain convergence:** Verify R-hat < 0.01 with standard diagnostics
