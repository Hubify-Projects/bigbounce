# Phase 2: Data & Likelihood Plan

**Date:** 2026-03-16
**Branch:** R Phase 2

---

## 1. Core Data (Phase 2a)

### 1.1 Birefringence Measurement

**Primary measurement:**
- beta = 0.342 +/- 0.094 deg (Eskilt & Komatsu 2022, Planck PR4 + WMAP reanalysis)
- Reference: Eskilt & Komatsu, Phys. Rev. Lett. 129, 021301 (2022)
- Method: Minami-Komatsu D-estimator on Planck PR4 (NPIPE) EB cross-spectra, calibrated against WMAP

**Combined measurement (Planck + ACT):**
- beta = 0.35 +/- 0.09 deg (3.9 sigma, Eskilt et al. 2024)
- Reference: Eskilt et al., arXiv:2403.XXXXX (check latest)
- Includes ACT DR6 TB/EB data extending to ell ~ 4000

**Choice for MCMC:** Use the combined Planck + ACT result:
- beta_obs = 0.342 deg (adopt the more conservative Eskilt & Komatsu 2022 central value)
- sigma_beta = 0.094 deg
- Alternatively: beta_obs = 0.35 deg, sigma_beta = 0.09 deg (combined)

We will run with **both** values and check consistency.

### Likelihood implementation

Simple Gaussian:

$$-2\ln\mathcal{L}_\beta = \left(\frac{\beta_{\rm pred} - \beta_{\rm obs}}{\sigma_\beta}\right)^2$$

This is exact for the published measurement, which reports a Gaussian posterior on beta. If the full posterior is asymmetric, we can later upgrade to a tabulated likelihood.

### 1.2 Background Cosmology: Planck 2018

**Already in our pipeline.** The existing Cobaya configs use:
- `planck_2018_lowl.TT` -- low-ell temperature
- `planck_2018_lowl.EE` -- low-ell E-mode polarization
- `planck_NPIPE_highl_CamSpec.TTTEEE` -- high-ell TT+TE+EE
- `planck_2018_lensing.clik` -- CMB lensing

These constrain the standard 6 LCDM parameters and provide the expansion history H(z) that enters the ALP ODE.

**For Model 2 (spectator ALP):** Planck likelihoods constrain LCDM parameters independently. The ALP only affects beta, which is a separate observable. Joint fitting is needed only for correlations through shared parameters (H_0, Omega_m affect the ALP ODE via H(z)).

**For Model 3 (ALP-DE):** The ALP modifies H(z), which changes CMB distances. Planck likelihoods are essential for constraining the ALP parameters jointly with LCDM. This requires feeding the ALP-modified background to CAMB.

### 1.3 BAO Distance Measurements

**Already in our pipeline:**
- 6dFGS (z_eff = 0.106): D_V/r_d
- SDSS MGS (z_eff = 0.15): D_V/r_d
- BOSS DR12/16 LRG (z_eff = 0.38, 0.51, 0.61): D_M/r_d, D_H/r_d
- eBOSS QSO (z_eff = 1.48): D_M/r_d, D_H/r_d
- eBOSS Ly-alpha (z_eff = 2.33): D_M/r_d, D_H/r_d

**Additional (if available):**
- DESI DR1 BAO (2024): D_M/r_d, D_H/r_d at z = 0.3, 0.5, 0.7, 0.9, 1.3, 2.1
- The DESI data shows hints of w > -1 dark energy, which would be interesting for Model 3

**Purpose:** BAO constrain the expansion history H(z) and angular diameter distances. For Model 3, these directly constrain the ALP contribution to DE since a rolling ALP field gives w > -1, altering distances relative to LCDM.

## 2. Likelihood Architecture

### Phase 2a: Birefringence-only (fast)

```
Cobaya
  |
  |-- Theory: ALPBirefringence (custom, computes beta from ODE)
  |
  |-- Likelihood: BirefringenceLikelihood (Gaussian on beta)
  |
  |-- No CAMB needed (ALP ODE uses fixed LCDM background)
  |
  |-- Sampled: {theta_i, log10_m_eV}
  |-- Fixed: f_a = M_Pl, C_agamma = 8
  |-- Derived: {beta_deg, eta, Omega_a, w_a_0}
```

**Runtime:** ~1 hour total (no Boltzmann solver).

### Phase 2a+: Birefringence + Planck (medium)

```
Cobaya
  |
  |-- Theory: CAMB (standard, for CMB spectra)
  |            + ALPBirefringence (custom, for beta)
  |
  |-- Likelihoods:
  |     BirefringenceLikelihood (Gaussian on beta)
  |     planck_2018_lowl.TT
  |     planck_2018_lowl.EE
  |     planck_NPIPE_highl_CamSpec.TTTEEE
  |     planck_2018_lensing.clik
  |     bao.sdss_dr16_baoplus_*
  |
  |-- Sampled: {ombh2, omch2, theta_MC, tau, logA, ns, theta_i, log10_m_eV}
  |-- Derived: {H0, sigma8, S8, beta_deg, Omega_a, w_a_0}
```

**Runtime:** ~25 hours (8 cores, RunPod).

This is the recommended production run for Model 2. It captures correlations between LCDM parameters and ALP parameters through the shared expansion history.

### Phase 2b: ALP-DE + Planck (full)

```
Cobaya
  |
  |-- Theory: axionCAMB (or CAMB + tabulated w(z))
  |
  |-- Likelihoods: same as Phase 2a+ PLUS
  |     Pantheon+ SN Ia (constrains w at low z)
  |     DESI DR1 BAO (if available)
  |
  |-- Sampled: {ombh2, omch2, theta_MC, tau, logA, ns, theta_i, log10_m_eV}
  |     NOTE: no Omega_Lambda parameter -- ALP replaces it
  |-- Derived: {H0, sigma8, S8, beta_deg, Omega_a, w_a_0, w_a_05}
```

**Runtime:** ~150 hours (8 cores, RunPod).

## 3. Optional Data (Phase 2b+)

### 3.1 ACT DR6 TB/EB Power Spectra (direct)

Instead of using the compressed beta measurement, one could fit directly to the TB and EB power spectra from ACT DR6. This would:
- Probe scale-dependent birefringence (sensitive to m_a)
- Provide tighter constraints
- Be the gold standard for publication

**Status:** Requires the ACT DR6 TB/EB likelihood module (may need to write or obtain from ACT collaboration).

### 3.2 SPT-3G Polarization

- SPT-3G has measured TE/EE to high precision
- TB/EB constraints from SPT-3G would be independent of Planck/ACT
- Not yet released as a standalone beta measurement (as of 2026)

### 3.3 Pantheon+ Type Ia Supernovae

- Constrains w(z) at z < 2
- Important for Model 3 to verify ALP DE equation of state
- Already available as a Cobaya likelihood module

### 3.4 DESI DR2 BAO (when available)

- Improved BAO measurements at multiple redshifts
- DESI DR1 hinted at w > -1, relevant for ALP-DE

## 4. Systematic Considerations

### 4.1 Instrumental Miscalibration

The D-estimator methodology already accounts for detector polarization angle miscalibration. The published beta measurement has this systematic folded in. No additional treatment needed at our level.

### 4.2 Galactic Foreground Birefringence

Galactic Faraday rotation produces frequency-dependent polarization rotation (propto nu^{-2}). The multi-frequency analysis in Eskilt et al. separates this from the frequency-independent cosmic signal. We treat the published beta as foreground-cleaned.

### 4.3 Frequency Dependence of ALP Signal

ALP birefringence is frequency-independent (geometric rotation). This is a prediction: any frequency dependence in beta would rule out the ALP interpretation. Current data is consistent with frequency independence.

### 4.4 Scale Dependence

For m << H_rec: birefringence is uniform (scale-independent). The measured beta is an ell-averaged quantity.

For m ~ H_rec or larger: birefringence becomes scale-dependent. The measurement at ell ~ 50-1500 averages over the scale dependence. For our mass range (m ~ H_0 << H_rec), this is not an issue.

## 5. Data Summary Table

| Dataset | Observable | Implementation | Phase |
|---------|-----------|----------------|-------|
| Birefringence (Planck+ACT) | beta = 0.342 +/- 0.094 deg | Gaussian likelihood | 2a |
| Planck 2018 TT/TE/EE/lensing | CMB power spectra | Existing Cobaya modules | 2a+ |
| BOSS/eBOSS BAO | D_M/r_d, D_H/r_d | Existing Cobaya modules | 2a+ |
| Pantheon+ SN Ia | distance moduli | Cobaya module | 2b |
| DESI DR1 BAO | D_M/r_d, D_H/r_d | Cobaya module (if available) | 2b |
| ACT DR6 TB/EB spectra | C_l^{TB}, C_l^{EB} | Custom likelihood (TBD) | 2b+ |
