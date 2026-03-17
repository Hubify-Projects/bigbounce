# Track A — Early SMBH Seed Phenomenology

## Model Specification

**Status:** Specification draft
**Date:** 2026-03-13
**Parent framework:** Spin-torsion bounce cosmology (Golden 2026)

---

## 1. Goal

Determine the minimum seed black hole masses required to explain observed high-redshift SMBHs (z > 6), and explore whether bounce-motivated primordial power spectrum features at the relevant comoving scales could increase the abundance of massive early halos where direct-collapse black hole (DCBH) formation is more likely.

This track does NOT claim the bounce produces the required P(k) enhancement. It identifies what enhancement would be needed and whether it is physically reasonable.

## 2. Minimal Model Parameters

| Parameter | Symbol | Range | Description |
|-----------|--------|-------|-------------|
| Seed mass | log10(M_seed / M_sun) | 1 -- 6 | Initial BH mass at formation |
| Seed redshift | z_seed | 15 -- 30 | Redshift of seed formation |
| Eddington ratio | epsilon_growth | 0.1 -- 3.0 | Accretion rate / Eddington rate (super-Eddington allowed) |
| Duty cycle | f_duty | 0.1 -- 1.0 | Fraction of time actively accreting |
| Radiative efficiency | epsilon_rad | 0.06 -- 0.42 | Fraction of accreted rest-mass energy radiated; ~0.1 for standard thin disk |
| Observed BH mass | M_obs | Measured | Final mass at z_obs |
| Observed redshift | z_obs | Measured | Redshift of observation |

## 3. Forward Model: Salpeter Growth

The standard Salpeter (1964) exponential growth equation:

$$
M(t) = M_{\rm seed} \times \exp\!\left[\frac{1 - \varepsilon_{\rm rad}}{\varepsilon_{\rm rad}} \cdot \frac{t}{t_{\rm Edd}} \cdot f_{\rm duty}\right]
$$

where:

- $\varepsilon_{\rm rad} \approx 0.1$ is the radiative efficiency (thin-disk default)
- $t_{\rm Edd} = \sigma_T c / (4\pi G m_p) \approx 0.45\,\mathrm{Gyr}$ is the Salpeter e-folding time
- $f_{\rm duty}$ is the duty cycle (fraction of elapsed time spent accreting)

The Salpeter e-folding timescale at Eddington with $\varepsilon_{\rm rad} = 0.1$:

$$
t_{\rm Sal} = \frac{\varepsilon_{\rm rad}}{1 - \varepsilon_{\rm rad}} \cdot t_{\rm Edd} \approx 50\,\mathrm{Myr}
$$

Number of e-foldings available between z_seed and z_obs:

$$
N_e = \frac{1 - \varepsilon_{\rm rad}}{\varepsilon_{\rm rad}} \cdot \frac{\Delta t(z_{\rm seed}, z_{\rm obs})}{t_{\rm Edd}} \cdot f_{\rm duty}
$$

## 4. Minimum Seed Mass Calculation

Given an observed SMBH with mass $M_{\rm obs}$ at redshift $z_{\rm obs}$, the minimum seed mass (assuming continuous Eddington accretion, $f_{\rm duty} = 1$) is:

$$
M_{\rm seed,min} = M_{\rm obs} \times \exp\!\left[-\frac{1 - \varepsilon_{\rm rad}}{\varepsilon_{\rm rad}} \cdot \frac{\Delta t}{t_{\rm Edd}} \cdot f_{\rm duty}\right]
$$

where $\Delta t = t(z_{\rm obs}) - t(z_{\rm seed})$ is the cosmic time interval.

For realistic duty cycles ($f_{\rm duty} < 1$) or sub-Eddington accretion ($\epsilon_{\rm growth} < 1$), the required seed mass increases — sometimes dramatically. This is the "seed mass problem."

### Worked example: UHZ-1 (z = 10.1, M_BH ~ 4 x 10^7 M_sun)

- Cosmic age at z = 10.1: ~470 Myr
- Assuming z_seed = 25: t(z=25) ~ 130 Myr, so Delta_t ~ 340 Myr
- At Eddington with f_duty = 1: N_e ~ 340/50 ~ 6.8 e-folds
- M_seed,min ~ 4e7 / exp(6.8) ~ 4.5e4 M_sun
- This is already in the DCBH range, requiring non-standard seed formation

## 5. Standard Seed Channels

| Channel | Mass range (M_sun) | Formation mechanism | Abundance | Key requirement |
|---------|-------------------|---------------------|-----------|-----------------|
| **Light seeds (Pop III remnants)** | 10 -- 300 | First-generation stellar collapse | Common | Low metallicity |
| **Medium seeds (stellar mergers)** | 10^2 -- 10^4 | Runaway collisions in dense star clusters | Moderate | Dense nuclear cluster formation at high z |
| **Heavy seeds (DCBH)** | 10^4 -- 10^5 | Direct collapse of pristine gas in atomic cooling halos | Rare | Strong LW radiation + no H2 cooling + massive halo |
| **Super-heavy seeds (galaxy mergers)** | 10^5 -- 10^6 | Gas-rich galaxy mergers at high z | Very rare | Multiple massive halos in close proximity |

The seed mass problem: for the most massive high-z SMBHs, even DCBH seeds require sustained near-Eddington accretion. Any mechanism that increases the abundance of rare, massive early halos makes DCBH formation more likely.

## 6. Framework Connection

### The legitimate pathway

Bounce --> modified P(k) at small scales --> enhanced abundance of massive early halos --> increased DCBH formation sites --> more massive SMBH seeds

### What the framework actually predicts

The spin-torsion bounce occurs at $\rho_{\rm crit} \approx 0.27\,\rho_{\rm Pl}$, modifying perturbation evolution at Planck-scale densities. However:

- **N_tot = 92 (fitted value):** Bounce features are pushed to comoving scales $k \sim 10^{13}\,\mathrm{Mpc}^{-1}$, far below the SMBH-relevant scales ($k \sim 10^5\text{--}10^6\,\mathrm{Mpc}^{-1}$). At the canonical e-fold count, bounce features do NOT affect SMBH formation.

- **N_tot uncertainty:** The total e-fold count is constrained only from above (by the observed CMB spectrum) and below (by solving the horizon problem, N > ~60). Values between 60 and 92 would shift bounce features to larger comoving scales. For features at $k \sim 10^5\,\mathrm{Mpc}^{-1}$, one needs $N_{\rm tot} \approx 60\text{--}70$, which is within the physically allowed range but is NOT the fitted value.

- **LQC precedent:** Loop quantum cosmology calculations (Agullo et al. 2013, Ashtekar & Gupt 2017, Wilson-Ewing 2013) show that bounces CAN modify P(k), but results are model-dependent. Some models show suppression at large scales; enhancement at small scales depends on the pre-bounce state.

- **The perturbation spectrum through the spin-torsion bounce has NOT been calculated.** This is the key missing calculation.

### Honesty classification

| Element | Status |
|---------|--------|
| Salpeter growth equation | Standard, well-established |
| Minimum seed mass for high-z SMBHs | Derived from observations + standard physics |
| DCBH formation in rare massive halos | Established astrophysical mechanism |
| P(k) enhancement increasing halo abundance | Standard cosmological calculation |
| Bounce producing P(k) enhancement at SMBH scales | **Speculative** — not calculated, not predicted at canonical N_tot |
| Bounce at rho_crit = 0.27 rho_Pl | From parent framework (Golden 2026) |
| N_tot = 92 | Fitted in parent framework |

## 7. What This Track Will and Will Not Do

**Will do:**
- Compute minimum seed masses for all observed high-z SMBHs with published mass estimates
- Map the (M_seed, z_seed, f_duty, epsilon_growth) parameter space for each object
- Quantify how much P(k) enhancement at $k \sim 10^5\text{--}10^6\,\mathrm{Mpc}^{-1}$ would increase massive halo abundance
- Identify the enhancement amplitude needed to alleviate the seed mass problem
- Compare to PBH constraints at the same scales (joint with Track B)

**Will NOT do:**
- Calculate the perturbation spectrum through the bounce (deferred to future work)
- Claim the framework predicts SMBH seed enhancement
- Invoke direct torsion effects at astrophysical densities ($\sim 10^{-83}$ suppression)

## 8. Outputs

### 8.1 Minimum Seed Mass Plot
- x-axis: z_obs (observed redshift)
- y-axis: M_seed,min (minimum seed mass in M_sun)
- Contours for different (f_duty, epsilon_growth) combinations
- Overlay: observed (M_BH, z) data points with error bars
- Horizontal bands for light / medium / heavy seed channels

### 8.2 Growth Time Consistency Diagram
- For each observed SMBH: the (M_seed, z_seed) pairs consistent with reaching M_obs by z_obs
- Color-coded by required epsilon_growth
- Highlights objects requiring super-Eddington growth or unrealistically early seeds

### 8.3 Seed Channel Comparison Table
- For each observed high-z SMBH: which seed channels can explain it?
- Required assumptions (f_duty, epsilon_growth, z_seed) for each channel
- Flag objects where only heavy seeds or super-Eddington growth works

### 8.4 P(k) Enhancement Impact Figure (conditional)
- IF computing halo mass function modification: show the fractional increase in massive halo abundance as a function of A_bump at $k \sim 10^5\,\mathrm{Mpc}^{-1}$

## 9. Implementation Plan

### Directory structure

```
track_A_smBH_seeds/
  model_spec.md          <-- this file
  README.md              <-- summary and quick-start
  src/
    salpeter_growth.py   <-- forward model
    min_seed_mass.py     <-- inverse: M_obs -> M_seed,min
    halo_abundance.py    <-- Press-Schechter with modified P(k) (optional)
    cosmology_utils.py   <-- t(z), D(z), sigma(M) utilities
  data/
    high_z_smbh.csv      <-- compiled (M_BH, z, source) from literature
  notebooks/
    01_seed_mass_survey.ipynb
    02_growth_constraints.ipynb
    03_halo_enhancement.ipynb  (optional)
  figures/
    (generated outputs)
```

### Dependencies
- numpy, scipy, matplotlib
- astropy (for cosmological calculations)
- colossus (optional, for halo mass functions)
- No proprietary data required

### Estimated effort
- Core seed mass calculation: 1--2 days
- Literature data compilation: 1 day
- Halo abundance modification (optional): 2--3 days
- Figures and write-up: 1--2 days
