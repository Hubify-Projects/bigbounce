# Branch R: ALP Cosmic Birefringence -- External Constraints

**Date:** 2026-03-16

---

## 1. Isocurvature Perturbations

### The issue

During inflation, the ALP acquires quantum fluctuations:

$$\delta\phi \sim \frac{H_{\rm inf}}{2\pi}$$

These become isocurvature perturbations in the ALP energy density:

$$S_\phi = \frac{\delta\rho_\phi}{\rho_\phi} - \frac{3}{4}\frac{\delta\rho_\gamma}{\rho_\gamma}$$

For small theta_i, the isocurvature fraction is:

$$\beta_{\rm iso} \equiv \frac{\mathcal{P}_S}{\mathcal{P}_S + \mathcal{P}_\zeta} \approx \left(\frac{H_{\rm inf}}{\pi f_a \theta_i}\right)^2$$

### Planck constraint

Planck 2018 constrains beta_iso < 0.038 (95% CL, uncorrelated mode).

### Implication for f_a = M_Pl

$$\beta_{\rm iso} < 0.038 \implies \frac{H_{\rm inf}}{\pi M_{\rm Pl} \theta_i} < 0.195$$

$$H_{\rm inf} < 0.195 \times \pi \times M_{\rm Pl} \times \theta_i \approx 1.5 \times 10^{18} \theta_i \text{ GeV}$$

For theta_i = 1: H_inf < 1.5 x 10^{18} GeV.

Since H_inf < 2.5 x 10^{13} GeV from the tensor-to-scalar ratio bound (r < 0.036, BICEP/Keck 2021), the isocurvature bound is automatically satisfied by many orders of magnitude:

$$\beta_{\rm iso} \sim \left(\frac{2.5 \times 10^{13}}{3.14 \times 2.4 \times 10^{18}}\right)^2 \sim (3.3 \times 10^{-6})^2 \sim 10^{-11}$$

**Verdict: NO CONSTRAINT.** The isocurvature bound is trivially satisfied for f_a ~ M_Pl.

### Caveat

If f_a << M_Pl (e.g., f_a ~ 10^{16} GeV), the bound becomes H_inf < 6 x 10^{15} GeV, which is still comfortably above the tensor-to-scalar ratio limit. Only for f_a < 10^{14} GeV would isocurvature become constraining, and such low f_a is outside our parameter range.

## 2. Dark Energy Density

### The coincidence

The ALP energy density for a frozen field (m << H at early times) is:

$$\rho_\phi = V(\phi_i) = m^2 f_a^2 (1 - \cos\theta_i) \approx \frac{1}{2} m^2 f_a^2 \theta_i^2 \quad (\text{for } \theta_i \ll \pi)$$

The critical density today:

$$\rho_{\rm crit} = 3 H_0^2 M_{\rm Pl}^2$$

For the fiducial parameters m ~ H_0, f_a ~ M_Pl, theta_i ~ 1:

$$\frac{\rho_\phi}{\rho_{\rm crit}} = \frac{m^2 f_a^2 \theta_i^2}{6 H_0^2 M_{\rm Pl}^2} \sim \frac{H_0^2 M_{\rm Pl}^2}{6 H_0^2 M_{\rm Pl}^2} = \frac{1}{6} \sim 0.17$$

This is comparable to the dark energy density Omega_Lambda ~ 0.68.

### Feature or bug?

**Feature:** The ALP with m ~ H_0 and f_a ~ M_Pl naturally has energy density of the right order for dark energy. If theta_i ~ 2:

$$\frac{\rho_\phi}{\rho_{\rm crit}} \sim \frac{4}{6} \sim 0.67 \approx \Omega_\Lambda$$

This means: **the ALP IS dark energy** at the fiducial parameters. This is not a constraint; it is a remarkable coincidence (or feature) of the model.

### Implications:

1. The ALP cannot have m >> H_0 with f_a ~ M_Pl and theta_i ~ O(1) without overproducing dark energy
2. The birefringence signal is naturally linked to the dark energy scale
3. This is precisely the string axiverse scenario of Arvanitaki et al. (2010)
4. The equation of state w_phi ~ -1 for the frozen field, transitioning toward w = 0 as it oscillates -- consistent with dark energy constraints if m ~ H_0

### Constraint to impose:

$$\rho_\phi = m^2 f_a^2 (1 - \cos\theta_i) \leq \rho_{\rm crit}$$

$$m^2 f_a^2 \theta_i^2 / 2 \lesssim 3 H_0^2 M_{\rm Pl}^2 \quad (\text{for small } \theta_i)$$

This excludes the upper-right corner of the (m, f_a) plane for fixed theta_i.

## 3. Fifth Force Constraints

### Compton wavelength

$$\lambda_C = \frac{1}{m_\phi} \sim \frac{1}{H_0} \sim 4000 \text{ Mpc} \sim \text{Hubble radius}$$

### Laboratory and solar system tests

Fifth force experiments constrain new forces at scales lambda < ~1 mm to ~AU. The ALP Compton wavelength is cosmological, so:

- Eot-Wash torsion balance: constrains lambda < 0.1 mm. **No constraint.**
- Lunar laser ranging: constrains lambda < AU ~ 10^{-4} pc. **No constraint.**
- Cassini tracking: constrains PPN parameters. **No constraint** (ALP is pseudoscalar, even weaker coupling to gravity than scalar).

**Verdict: NO CONSTRAINT.** The force range is too long for any local test.

## 4. Laboratory ALP Searches

### CAST (CERN Axion Solar Telescope)

- Searches for solar axions via inverse Primakoff effect
- Current bound: g_{agamma} < 6.6 x 10^{-11} GeV^{-1} (for m < 0.02 eV)
- Our prediction: g_{agamma} ~ 3.8 x 10^{-21} GeV^{-1}
- **10 orders of magnitude below sensitivity.** No constraint.

### IAXO (International Axion Observatory)

- Projected sensitivity: g_{agamma} ~ 10^{-12} GeV^{-1}
- Still **9 orders of magnitude** above our prediction. No constraint even with next-generation experiments.

### ABRACADABRA / DMRadio

- Searches for axion dark matter via magnetic field coupling
- Sensitivity in the m ~ 10^{-14} to 10^{-6} eV range
- Our mass range (10^{-33} eV) is **20 orders of magnitude below** their band. No constraint.

### Light-shining-through-walls (ALPS-II)

- Projected: g_{agamma} ~ 2 x 10^{-11} GeV^{-1}
- **10 orders of magnitude gap.** No constraint.

**Verdict: ALL LABORATORY BOUNDS ARE IRRELEVANT.** The coupling g_{agamma} ~ 10^{-21} GeV^{-1} is completely inaccessible to any foreseeable laboratory experiment. The ONLY observable window is cosmological (CMB birefringence, and potentially LSS).

## 5. BBN Constraints

### Energy density at BBN

At BBN (T ~ 1 MeV, t ~ 1 s), the ALP field is frozen at phi_i with energy:

$$\rho_\phi(T_{\rm BBN}) = m^2 f_a^2 (1 - \cos\theta_i)$$

The radiation energy density at BBN:

$$\rho_{\rm rad}(T_{\rm BBN}) = \frac{\pi^2}{30} g_* T_{\rm BBN}^4 \sim 10^{-3} \text{ MeV}^4$$

The ALP energy:

$$\rho_\phi = m^2 f_a^2 \sim H_0^2 M_{\rm Pl}^2 \sim (10^{-33} \text{ eV})^2 (2.4 \times 10^{27} \text{ eV})^2$$
$$= 5.8 \times 10^{-12} \text{ eV}^4 \sim 6 \times 10^{-12} \text{ eV}^4$$

Converting: rho_rad(BBN) ~ 10^{-3} MeV^4 = 10^{-3} x (10^6)^4 eV^4 = 10^{21} eV^4.

$$\frac{\rho_\phi}{\rho_{\rm rad}(T_{\rm BBN})} \sim \frac{6 \times 10^{-12}}{10^{21}} \sim 6 \times 10^{-33}$$

**Verdict: COMPLETELY NEGLIGIBLE.** The ALP contributes a fraction ~10^{-33} of the energy density at BBN. No constraint from Delta N_eff or light element abundances.

## 6. Black Hole Superradiance

### Mechanism

Ultralight bosons can extract rotational energy from spinning black holes via superradiance when the Compton wavelength matches the black hole size:

$$r_g \sim \lambda_C \implies M_{\rm BH} \sim \frac{M_{\rm Pl}^2}{m_\phi}$$

### For m ~ 10^{-33} eV:

$$M_{\rm BH} \sim \frac{(2.4 \times 10^{18})^2}{10^{-33}} \text{ GeV} \sim 6 \times 10^{69} \text{ GeV} \sim 10^{46} \text{ kg} \sim 5 \times 10^{15} M_\odot$$

This is far above any known black hole mass (the most massive are ~10^{10} M_\odot).

**Verdict: NO CONSTRAINT.** Superradiance is relevant for m ~ 10^{-20} to 10^{-11} eV (stellar to supermassive BH masses). Our mass range is completely outside this window.

## 7. Astrophysical ALP Bounds

### SN 1987A

- Constrains ALP-photon coupling for m < ~10^{-9} eV via energy loss
- Bound: g_{agamma} < 5 x 10^{-12} GeV^{-1}
- Our coupling: g_{agamma} ~ 4 x 10^{-21} GeV^{-1}
- **9 orders of magnitude below.** No constraint.

### Globular cluster stars (HB stars, tip of RGB)

- Constrain g_{agamma} < ~6 x 10^{-11} GeV^{-1}
- Same story: irrelevant for our coupling.

### X-ray/gamma-ray spectral distortions (ALP-photon oscillation in magnetic fields)

- Constrain g_{agamma} in the 10^{-12} to 10^{-11} GeV^{-1} range
- Irrelevant.

## 8. Summary of Constraints

| Constraint | Bound | Our value | Status |
|------------|-------|-----------|--------|
| Isocurvature | beta_iso < 0.038 | ~10^{-11} | SAFE (by 10 orders) |
| Dark energy density | rho_phi < rho_crit | rho_phi ~ 0.1-0.7 rho_crit | FEATURE (ALP is DE) |
| Fifth force | lambda_C < 0.1 mm | lambda_C ~ Hubble | SAFE (wrong scale) |
| CAST | g_{agamma} < 7 x 10^{-11} | 4 x 10^{-21} | SAFE (by 10 orders) |
| IAXO (future) | g_{agamma} ~ 10^{-12} | 4 x 10^{-21} | SAFE (by 9 orders) |
| BBN (Delta N_eff) | rho_phi/rho_rad < ~0.1 | ~10^{-33} | SAFE (by 32 orders) |
| Superradiance | m in [10^{-20}, 10^{-11}] eV | 10^{-33} eV | SAFE (wrong mass) |
| SN 1987A | g_{agamma} < 5 x 10^{-12} | 4 x 10^{-21} | SAFE (by 9 orders) |
| HB stars | g_{agamma} < 6 x 10^{-11} | 4 x 10^{-21} | SAFE (by 10 orders) |

**Every external constraint is satisfied by enormous margins.** The only observable consequence is cosmic birefringence -- and it matches the data.

## 9. The Key Constraint: Is the ALP Dark Energy?

The one constraint that is not "safe by many orders" is the dark energy density. The ALP with m ~ H_0, f_a ~ M_Pl, theta_i ~ O(1) has rho_phi ~ rho_crit. This means:

1. The ALP must be treated as a dynamical dark energy component, not a subdominant spectator
2. Its equation of state w_phi must be consistent with dark energy constraints (w = -1.03 +/- 0.03, Planck + DESI)
3. For a frozen field: w_phi = -1 exactly, which is consistent
4. For a field that has begun rolling (m ~ H_0): w_phi slightly above -1, consistent with DESI hints of w > -1

This is the most important physics point: **the birefringence signal and dark energy are naturally unified in this model**. The same field, at the same parameter values, simultaneously explains:
- The observed cosmic birefringence angle
- The observed dark energy density
- The observed dark energy equation of state

This triple coincidence is the strongest argument for the ultralight ALP interpretation of the birefringence signal.
