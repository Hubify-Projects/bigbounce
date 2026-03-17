# Effective Late-Time Sector Specification

**Date:** 2026-03-17
**Status:** Canonical spec for salvaged Paper 1

---

## 1. Field Content

One real pseudoscalar field phi(x) with mass dimension [phi] = +1.

The angular variable is theta = phi / f_a, with theta in [0, 2 pi).

---

## 2. Lagrangian

$$\mathcal{L}_{\rm ALP} = -\frac{1}{2}(\partial_\mu \phi)^2 - V(\phi) + \mathcal{L}_{\rm coupling}$$

**Potential:**
$$V(\phi) = m_a^2 f_a^2 \left[1 - \cos\!\left(\frac{\phi}{f_a}\right)\right]$$

For small field excursions (theta << 1), this reduces to the quadratic potential V ~ m_a^2 phi^2 / 2.

**Photon coupling:**
$$\mathcal{L}_{\rm coupling} = -\frac{g_{a\gamma}}{4}\,\phi\,F_{\mu\nu}\tilde{F}^{\mu\nu} = g_{a\gamma}\,\phi\,\mathbf{E}\cdot\mathbf{B}$$

where
$$g_{a\gamma} = \frac{C_{a\gamma}\,\alpha_{\rm em}}{2\pi\,f_a}$$

---

## 3. Parameters

| Parameter | Symbol | Fiducial value | Status |
|-----------|--------|---------------|--------|
| Decay constant | f_a | M_Pl = 2.435 x 10^{18} GeV | Fixed (natural scale in ECH) |
| ALP mass | m_a | ~ H_0 ~ 10^{-33} eV | Free (sampled in MCMC) |
| Anomaly coefficient | C_{agamma} | 8 (SM fermion content) | Fixed at fiducial; extended runs float it |
| Initial misalignment | theta_i | O(1) | Free (sampled in MCMC) |

**Derived quantities:**
| Quantity | Formula | Fiducial value |
|----------|---------|---------------|
| Photon coupling | g_{agamma} = C alpha / (2 pi f_a) | 3.8 x 10^{-21} GeV^{-1} |
| Birefringence | beta = C alpha theta_i eta / (4 pi) | 0.27 deg (theta_i = 1, eta = 1) |
| ALP energy density | rho_a = m^2 f_a^2 (1 - cos theta_i) | ~ rho_crit for m ~ H_0, theta_i ~ 1 |
| Rolling efficiency | eta(m/H_0, theta_i) | Numerically integrated |

---

## 4. Coupling to Photons

The ALP-photon coupling arises from the chiral anomaly (ABJ triangle) with the ALP playing the role of the pseudoscalar current. For SM fermions:

$$C_{a\gamma} = 2\sum_f N_c^{(f)} Q_f^2 = 2\left[3\left(\frac{4}{9} + \frac{1}{9} + \frac{1}{9}\right) \times 3 \text{ generations} + 1 \times 3 \text{ leptons}\right] = 8$$

This is the minimal (SM-only) value. Extended charged sectors give larger C_{agamma}.

---

## 5. Role in Birefringence

The ALP sources cosmic birefringence through the phi F F-tilde coupling. As phi evolves from its initial value phi_i = f_a theta_i to its value today phi_0, CMB photons propagating through the evolving phi field accumulate a polarization rotation:

$$\beta = \frac{g_{a\gamma}}{2}\left[\phi(z_{\rm rec}) - \phi(z=0)\right] = \frac{C_{a\gamma}\,\alpha_{\rm em}}{4\pi}\left[\theta(z_{\rm rec}) - \theta(z=0)\right]$$

**Key feature:** f_a cancels exactly in the birefringence formula. The prediction depends only on:
- C_{agamma} (fixed by particle content)
- alpha_em (measured)
- theta_i (free, O(1) natural)
- eta(m/H_0) (the rolling efficiency, computed numerically)

For the spectator regime (m >> H_0, field fully rolled): eta -> 1, and

$$\boxed{\beta = \frac{C_{a\gamma}\,\alpha_{\rm em}\,\theta_i}{4\pi} \approx 0.27^\circ \times \theta_i}$$

---

## 6. Relationship to Lambda / Separate DE

**The ALP is NOT dark energy in this model.**

| Statement | Status |
|-----------|--------|
| The ALP provides cosmic birefringence | CLAIMED |
| The ALP IS dark energy | NOT CLAIMED |
| Dark energy is a separate cosmological constant Lambda | ASSUMED |
| The ALP contributes negligible energy density today | REQUIRED (spectator regime) |
| m >> H_0 ensures the field has rolled to zero | REQUIRED for eta ~ 1 |
| Lambda is unexplained (standard CC problem) | ACKNOWLEDGED |

The spectator regime requires m > few x H_0. In this regime:
- The field has oscillated and its energy density has redshifted as a^{-3} (behaving as dark matter, not dark energy)
- Omega_a << 0.01 today
- The background cosmology is standard LCDM + Lambda
- The ALP affects ONLY polarization, not expansion

**Why not ALP-as-DE?** The Phase 2 prefit (Branch R) showed a factor-2 tension: on the Omega_a = 0.68 contour, the maximum achievable beta is ~0.16 deg, below the observed 0.35 deg. Birefringence demands rolling (large eta) while DE demands freezing (w ~ -1, small eta). These requirements push in opposite directions. See 05_quick_prefit.md for the full analysis.

---

## 7. What Is Claimed

1. The ECH framework's parity-odd sector motivates an ALP with f_a ~ M_Pl
2. With SM anomaly coefficient C = 8 and theta_i ~ O(1), the predicted birefringence is beta ~ 0.27 deg
3. This is consistent with the observed 0.35 +/- 0.09 deg within 1 sigma
4. The prediction is robust: independent of f_a, weakly dependent on m (for m > few H_0)
5. MCMC constraints on (theta_i, m_a) are presented
6. LiteBIRD (sigma_beta ~ 0.01 deg) will provide a decisive test

---

## 8. What Is Explicitly NOT Claimed

1. The ALP is NOT uniquely derived from ECH. Any Planck-scale ALP with SM coupling gives the same prediction. ECH provides ONE possible UV motivation.
2. The ALP does NOT explain dark energy. Lambda is separate and unexplained.
3. The mass m ~ H_0 is NOT predicted. It is a free parameter subject to the cosmological constant problem.
4. The initial misalignment theta_i is NOT predicted. It is a free parameter (O(1) is natural but not derived).
5. The one-loop photon-torsion vertex has NOT been computed. The ALP-photon coupling is assumed, not derived from ECH.
6. No galaxy spin asymmetry is predicted by this model.
7. No H_0 or sigma_8 tension resolution is predicted by this model.

---

## 9. Constraint Summary

| Bound | Value | Margin |
|-------|-------|--------|
| CAST (helioscope) | g < 6.6 x 10^{-11} GeV^{-1} | 10^{10} above model |
| SN1987A | g < 5 x 10^{-12} GeV^{-1} | 10^{9} above model |
| Black hole superradiance | excludes 6 x 10^{-13} < m < 2 x 10^{-11} eV | model mass is below this |
| CMB spectral distortion | no constraint for m < 10^{-28} eV | model is below |
| Isocurvature (Planck) | requires f_a < 10^{19} GeV for m ~ H_0 | f_a = M_Pl is marginal |
| Dark matter overproduction | theta_i < 2.4 for f_a = M_Pl, m = H_0 | theta_i = 1.3 is safe |

**All laboratory, astrophysical, and cosmological bounds are satisfied.**
