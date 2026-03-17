# Track B — PBH-like / Exotic Compact Seed Phenomenology

## Model Specification

**Status:** Specification draft
**Date:** 2026-03-13
**Parent framework:** Spin-torsion bounce cosmology (Golden 2026)

---

## 1. Goal

Map the primordial power spectrum parameter space $(A_{\rm bump}, k_{\rm bump})$ to PBH abundance $f_{\rm PBH}(M)$, overlay the full suite of observational constraints, and identify whether any allowed window exists at SMBH-seed-relevant masses ($10^3\text{--}10^6\,M_\odot$).

This track does NOT predict PBH production from the bounce framework. It identifies what P(k) features would be needed IF the bounce were to produce small-scale enhancement, and checks those features against existing constraints.

## 2. Critical Distinction: PBH vs PBH-like Proxy

| Term | Meaning | Status in this work |
|------|---------|--------------------|
| **PBH (primordial black hole)** | Black hole formed from gravitational collapse of enhanced primordial density perturbations during radiation domination | Standard definition; well-studied formation channel |
| **PBH-like proxy** | ANY compact seed object that shares the same mass function phenomenology as PBHs — same mass range, same constraint landscape | Used when we want to remain agnostic about the formation mechanism |
| **Bounce-produced PBH** | PBH whose existence is caused by bounce-modified P(k) | **Not predicted** by this framework. The perturbation spectrum through the spin-torsion bounce has not been calculated. |

This track computes standard PBH phenomenology (mass functions, constraints) and notes where the bounce framework connects motivationally. The analysis is valid regardless of whether the bounce actually produces the required P(k) features.

## 3. PBH Mass Function Model

### Log-normal mass function

$$
\frac{df_{\rm PBH}}{d\ln M} = \frac{f_{\rm total}}{\sqrt{2\pi}\,\sigma_M} \exp\!\left[-\frac{(\ln M/M_c)^2}{2\sigma_M^2}\right]
$$

where:

- $M_c$ = central (peak) mass of the distribution
- $\sigma_M$ = width of the log-normal distribution
- $f_{\rm total} = \Omega_{\rm PBH}/\Omega_{\rm DM}$ = total fraction of dark matter in PBHs

### Monochromatic limit

When $\sigma_M \to 0$, this reduces to $f_{\rm PBH}(M) = f_{\rm total}\,\delta(M - M_c)$, which is the standard assumption in most constraint plots.

## 4. Model Parameters

| Parameter | Symbol | Range | Description |
|-----------|--------|-------|-------------|
| Central mass | $M_c$ | $10^{-18}\text{--}10^{10}\,M_\odot$ | Peak of PBH mass function |
| Log-normal width | $\sigma_M$ | 0.1 -- 3.0 | Width of mass distribution |
| Total DM fraction | $f_{\rm total}$ | $10^{-20}\text{--}1$ | Integrated DM fraction in PBHs |
| P(k) bump amplitude | $A_{\rm bump}$ | $10^{-3}\text{--}10^{-1}$ | Enhancement of P(k) above standard $A_s \approx 2.1 \times 10^{-9}$ |
| P(k) bump scale | $k_{\rm bump}$ | $1\text{--}10^{20}\,\mathrm{Mpc}^{-1}$ | Comoving scale of P(k) enhancement |
| P(k) bump width | $\Delta_k$ | 0.5 -- 3.0 decades | Width of enhancement in log(k) |

## 5. Constraint Sources

### Primary: PBHbounds repository

- **Source:** bradkav/PBHbounds on GitHub
- **License:** MIT
- **Format:** Machine-readable CSV/dat files with $(M, f_{\rm PBH,max})$ pairs
- **Coverage:** ~30 independent constraint channels

### Constraint channels by mass range

| Mass range ($M_\odot$) | Constraint | Type | Key reference |
|------------------------|------------|------|---------------|
| $10^{-18}\text{--}10^{-16}$ | Femtolensing | Lensing | Barnacka et al. 2012 |
| $10^{-17}\text{--}10^{-12}$ | Hawking evaporation (extragalactic gamma rays) | Evaporation | Carr et al. 2010 |
| $10^{-14}\text{--}10^{-11}$ | Voyager e+/e- | Evaporation | Boudaud & Cirelli 2019 |
| $10^{-11}\text{--}10^{-7}$ | Microlensing (HSC/Subaru) | Lensing | Niikura et al. 2019 |
| $10^{-7}\text{--}10^{-1}$ | Microlensing (EROS, OGLE) | Lensing | EROS-2; Mroz et al. 2024 |
| $1\text{--}10^3$ | GW merger rate (LIGO/Virgo) | Dynamical | Kavanagh et al. 2018 |
| $10\text{--}10^4$ | Wide binary disruption | Dynamical | Monroy-Rodriguez & Allen 2014 |
| $10^2\text{--}10^8$ | CMB spectral distortions (accretion) | Accretion | Ali-Haimoud & Kamionkowski 2017 |
| $10^3\text{--}10^{10}$ | Dynamical friction (ultra-faint dwarfs) | Dynamical | Brandt 2016 |
| $10^4\text{--}10^{10}$ | X-ray/radio from accretion | Accretion | Manshanden et al. 2019 |

### SMBH-seed-relevant mass window: $10^3\text{--}10^6\,M_\odot$

The constraints in this window come primarily from:
- CMB accretion: $f_{\rm PBH} \lesssim 10^{-3}\text{--}10^{-5}$ (mass-dependent)
- Wide binary disruption: $f_{\rm PBH} \lesssim 10^{-2}\text{--}10^{-3}$
- Dynamical friction in dwarfs: $f_{\rm PBH} \lesssim 10^{-3}\text{--}10^{-4}$

These are among the WEAKER constraints in the full PBH mass spectrum, which is relevant for Track C (joint analysis).

## 6. Connection to P(k)

### From P(k) to PBH abundance

The fraction of horizon patches collapsing to PBHs at mass scale $M$ is:

$$
\beta(M) \approx \mathrm{erfc}\!\left(\frac{\delta_c}{\sqrt{2}\,\sigma(M)}\right)
$$

where:

- $\delta_c \approx 0.45$ is the threshold overdensity for PBH formation (radiation domination)
- $\sigma^2(M)$ is the variance of the density field smoothed at scale $R(M)$:

$$
\sigma^2(M) = \int_0^\infty \frac{dk}{k}\,\mathcal{P}(k)\,W^2(kR)
$$

- $W(kR)$ is a window function (typically top-hat or Gaussian)
- $R(M) = (3M/(4\pi\rho))^{1/3}$ is the comoving smoothing scale

### From beta(M) to f_PBH(M)

$$
f_{\rm PBH}(M) = \frac{\beta(M)}{\beta_{\rm eq}} \approx 1.4 \times 10^8 \left(\frac{M}{M_\odot}\right)^{-1/2} \beta(M)
$$

### Required P(k) enhancement

For PBH formation at mass $M$, one needs $\sigma(M) \gtrsim \delta_c/3 \sim 0.15$, requiring:

$$
\mathcal{P}(k_{\rm bump}) \sim 10^{-2}
$$

This is an enhancement of $\sim 10^7$ above the CMB-measured amplitude $A_s \approx 2.1 \times 10^{-9}$. This is a very large enhancement and is NOT generically expected from bounce cosmologies.

## 7. Framework Connection

### What the bounce framework provides

- A bounce at $\rho_{\rm crit} \approx 0.27\,\rho_{\rm Pl}$ that modifies perturbation evolution
- A physical mechanism (spin-torsion coupling) distinct from LQC

### What it does NOT provide

- A calculated perturbation spectrum through the bounce
- A prediction for P(k) enhancement at any specific scale
- A prediction for PBH formation

### LQC precedent (honest assessment)

Loop quantum cosmology calculations that have computed P(k) through the bounce generally find:

- **Large-scale suppression** of power (Agullo et al. 2013, Ashtekar & Gupt 2017) — this is the opposite of what PBH formation needs
- **Oscillatory features** superimposed on the standard spectrum (Wilson-Ewing 2013) — could in principle produce local enhancements, but at very specific scales
- **Model dependence** on the pre-bounce quantum state — results vary significantly with the choice of vacuum state

The framework connection is therefore **motivational, not calculational**. The bounce provides a reason to explore modified P(k) at small scales, but does not predict the modification.

## 8. Honest Assessment

| Claim | Status |
|-------|--------|
| PBH constraints as a function of mass | **Well-established** (from PBHbounds) |
| PBH mass function phenomenology | **Standard** (Press-Schechter formalism) |
| P(k) -> beta(M) -> f_PBH(M) pipeline | **Standard** cosmological calculation |
| The bounce produces P(k) enhancement | **Not calculated, not predicted** |
| LQC bounces generally enhance small-scale P(k) | **Not supported** — most LQC results show large-scale suppression |
| The $10^3\text{--}10^6\,M_\odot$ window has relatively weak PBH constraints | **True** — this is an observational fact independent of the framework |

## 9. Outputs

### 9.1 $f_{\rm PBH}(M)$ Constraint Overlay
- x-axis: $M/M_\odot$ (log scale, $10^{-18}$ to $10^{10}$)
- y-axis: $f_{\rm PBH}$ (log scale, $10^{-10}$ to 1)
- All constraint channels from PBHbounds, color-coded by type
- Highlight the $10^3\text{--}10^6\,M_\odot$ SMBH seed window
- Data source: PBHbounds (MIT license)

### 9.2 Allowed $(M_c, f_{\rm total})$ Region
- For monochromatic and log-normal mass functions
- Shade the region NOT excluded by any constraint
- Overlay the SMBH seed mass requirements from Track A

### 9.3 Required P(k) Bump
- For each target $(M_c, f_{\rm total})$: compute the required $(A_{\rm bump}, k_{\rm bump})$
- Overlay CMB spectral distortion constraints (FIRAS, PIXIE projections)
- Show how much enhancement above $A_s$ is needed

## 10. Implementation Plan

### Directory structure

```
track_B_pbh_like_seeds/
  model_spec.md              <-- this file
  README.md                  <-- summary and quick-start
  src/
    pbh_mass_function.py     <-- log-normal f_PBH(M)
    pk_to_beta.py            <-- P(k) -> sigma(M) -> beta(M) -> f_PBH(M)
    constraint_loader.py     <-- parse PBHbounds data files
    spectral_distortion.py   <-- mu-distortion from enhanced P(k)
  data/
    PBHbounds/               <-- clone of bradkav/PBHbounds (MIT license)
  notebooks/
    01_constraint_landscape.ipynb
    02_pk_to_fpbh.ipynb
    03_smbh_window.ipynb
  figures/
    (generated outputs)
```

### Dependencies
- numpy, scipy, matplotlib
- PBHbounds data (MIT license, machine-readable)
- No proprietary data required

### Estimated effort
- Constraint overlay figure: 1 day (mostly formatting PBHbounds data)
- P(k) -> f_PBH pipeline: 2 days
- Spectral distortion cross-check: 1 day
- Figures and write-up: 1--2 days
