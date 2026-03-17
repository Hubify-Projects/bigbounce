# Claim Salvage Map: Paper 1 and Paper 1.2

**Date:** 2026-03-16

---

## Classification Key

- **ALIVE** -- claim stands as stated, can be developed further
- **ALIVE_BUT_REFRAME** -- underlying result is valid but the original framing overclaimed; reframe needed
- **DEAD** -- claim is false or unsupported; abandon entirely

---

## Major Claims Assessment

### 1. Direct dark-energy origin from geometry

**Original claim (Paper 1):** Dark energy emerges from quantum gravitational effects in ECH gravity.

**Verdict: DEAD**

All 7 routes (A-G) to deriving w = -1 from the ECH/PGT framework failed with structural barriers. The scaling ansatz (rho_Lambda = Xi * M_Pl^4) is a phenomenological parameterization, not a derivation. Paper 1.2 acknowledges this explicitly: "The equation of state w = -1 is assumed, not derived." The parity-odd operator is sourced by spin density, which vanishes at late times; no mechanism generates an IR-constant vacuum term.

---

### 2. Fine-tuning reduction from 10^120 to 10^5

**Original claim:** The inflationary suppression mechanism reduces fine-tuning by 115 orders of magnitude.

**Verdict: ALIVE_BUT_REFRAME**

The dimensional chain (Planck-scale parity-odd coefficient -> inflationary dilution -> observed scale) is mathematically valid as a scaling estimate. The Monte Carlo scan confirms N_tot as the controlling parameter. But this is conditional on the ansatz being correct -- and all derivation routes failed. Reframe as: "IF a parity-odd vacuum term is generated at the bounce and diluted by inflation, the residual fine-tuning is 10^5 in N_tot. Whether such a term is generated remains an open first-principles question." This is a parametric observation about any Planck-scale-to-meV scaling chain, not specific to ECH.

---

### 3. H0 tension reduction (69.2 +/- 0.8 km/s/Mpc)

**Original claim:** The ECH framework partially reduces the Hubble tension from 4.9 sigma to 2.9 sigma.

**Verdict: DEAD**

The independent Cobaya verification (176,840 samples, R-1 < 0.001) yields H0 = 67.68 +/- 1.06, consistent with Planck Lambda-CDM. The tension "reduction" in the original analysis is driven by the SH0ES H0 prior in the full-tension dataset, not by the Delta-Neff extension. Paper 1.2 Table II shows the verification clearly: without the SH0ES prior, H0 does not move. Delta-Neff = -0.020 +/- 0.169 is consistent with zero. The framework provides no mechanism to generate a specific Delta-Neff value.

---

### 4. sigma8/S8 tension reduction

**Original claim:** sigma8 = 0.785 +/- 0.016 and S8 = 0.80 +/- 0.02, reducing S8 tension to ~1 sigma.

**Verdict: DEAD**

Same as H0: the verification gives sigma8 = 0.803 +/- 0.008, S8 = 0.814 +/- 0.008, consistent with Planck Lambda-CDM. The apparent reduction was an artifact of including the DES Y3 S8 Gaussian prior in the MCMC fit (the model accommodated the prior by shifting, but the data do not prefer the extension).

---

### 5. Parity/birefringence signal

**Original claim (Paper 1):** The framework is "qualitatively consistent" with 2.4-2.9 sigma cosmic birefringence.

**Verdict: ALIVE_BUT_REFRAME**

The observed cosmic birefringence (beta = 0.242 +/- 0.061 deg, combined 3.9 sigma from Planck + ACT DR6) is real data independent of any framework. The ECH parity-odd coupling scale alpha/M ~ 10^{-21} GeV^{-1} requires f_photon ~ 1.7 (O(1), no fine-tuning) for consistency -- this is a genuine positive result. But the photon-torsion vertex is NOT derived; f_photon is a free parameter. Reframe as: "The ECH coupling scale is naturally compatible with observed birefringence if a photon-torsion vertex exists at O(1) strength. Computing this vertex is the key open calculation." This is a consistency check, not a prediction.

---

### 6. Bounce phenomenology (modified Friedmann, non-singular bounce)

**Original claim:** The spin-torsion bounce replaces the Big Bang singularity at rho_crit ~ 0.21 M_Pl^4.

**Verdict: ALIVE**

The bounce mechanism is mathematically rigorous and theoretically well-motivated. The modified Friedmann equation H^2 = (8 pi G / 3) rho(1 - rho/rho_crit) is exact for radiation. The bounce is non-singular. This is NOT affected by the DE program closure -- the bounce operates at Planck densities where torsion is dominant. However, the bounce is observationally inert (P_T ~ 10^{-64}, T(k) = 1, Delta-chi = 0). It exists but produces no observable consequences in the minimal model.

---

### 7. Lower-scale PGT bounce

**Original claim:** PGT extends the bounce to lower scales (rho_crit ~ m_T^2 M_Pl^2), potentially reaching GW detector bands.

**Verdict: DEAD**

The PGT parameter scan (Table in Paper 1.2) shows the GW signal has a minimum 10^{17} gap to any detector across the entire mass range. The mass-coupling lock (g_eff ~ m_T / M_Pl^2) kills matter coupling for light modes. The Z2 parity protection (Branch P) blocks torsion relic production at the bounce. Branch P status is MIXED, but the strongest channel (torsion relic cosmology) is gated on the energy fraction question, and even in the best case produces only exclusion constraints (lower bound on m_T), not detections.

---

### 8. Observable gravitational wave signal

**Original claim (Paper 1, implied):** The bounce produces a potentially detectable GW spectrum.

**Verdict: DEAD**

P_T ~ 2 x 10^{-64}. The gap to detection is at least 10^4 orders of magnitude at every frequency band (CMB: 10^52, PTA: 10^36, LISA: 10^20, ET/LIGO: 10^15, HF: 10^4). The PGT lower-scale bounce does not help (10^17 gap). This is structural: the dilution factor (a_b/a_0)^2 ~ 10^{-65} is insurmountable for any radiation-dominated Planck-scale bounce.

---

### 9. Galaxy-spin asymmetry

**Original claim:** Phenomenological A(z) = A0(1+z)^{-p} exp(-qz) with A0 ~ 0.003, consistent with observed Shamir (2024) dipole.

**Verdict: ALIVE_BUT_REFRAME**

The galaxy spin dipole is real observational data (Shamir 2024 and others). The parity-odd tidal torque model shows epsilon_PO ~ 0.2 is needed -- this is "moderate parity violation" and not absurd. But the connection to the ECH framework is purely phenomenological: epsilon_PO is a free parameter, not derived from alpha/M. The CNN classifier failed (random chance due to bug + synthetic data). Reframe as: "Galaxy spin asymmetry measurements provide an independent probe of cosmic parity violation; any parity-violating framework predicts a nonzero signal." This is a generic observational program, not ECH-specific.

---

### 10. Structural no-go results (14 barriers)

**Original claim (Paper 1.2):** 14 structural barriers across 5 failure modes close all routes from the spin-torsion bounce to observable consequences.

**Verdict: ALIVE**

This is the strongest positive result of the entire program. Each barrier is a standalone theorem-level result:
- Mass-coupling lock (A)
- Topological-shift duality (B)
- Scalar-tensor universality (C)
- Planck suppression (D)
- Scale separation (E)
- Attractor-sensitivity dilemma (F)
- Parameter immunity (G)
- Parity-even effective interaction (H)
- Hamiltonian phase-space conservation (J)
- UV-IR specificity dilemma (L1)
- Decoupling universality (L2)
- Vacuum amplification ceiling (M)
- Gravitational democracy (N)
- Bounce-vacuum energy decoupling (O)

These constrain future work in the field and are publishable as a comprehensive negative result.

---

### 11. w = -1 equation of state

**Original claim:** The framework predicts/accommodates w = -1 dark energy.

**Verdict: DEAD**

w = -1 is assumed, not derived. The parity-odd operator source (spin density) vanishes at late times. All 4 minimal routes and 7 extended foundations failed to derive persistence. This is the central negative result of the program.

---

## Summary Table

| Claim | Verdict | Key Issue |
|-------|---------|-----------|
| Direct DE from geometry | DEAD | All 7 derivation routes closed |
| Fine-tuning 10^120 -> 10^5 | ALIVE_BUT_REFRAME | Conditional on ansatz validity |
| H0 tension reduction | DEAD | Driven by SH0ES prior, not Delta-Neff |
| S8 tension reduction | DEAD | Driven by DES prior, not Delta-Neff |
| Parity/birefringence | ALIVE_BUT_REFRAME | Consistency check, not prediction |
| Bounce phenomenology | ALIVE | Valid but observationally inert |
| PGT lower-scale bounce | DEAD | 10^17 GW gap, Z2 blocks relics |
| Observable GW signal | DEAD | P_T ~ 10^{-64}, insurmountable |
| Galaxy-spin asymmetry | ALIVE_BUT_REFRAME | Real data, generic parity probe |
| No-go barrier catalog | ALIVE | Strongest positive result |
| w = -1 from framework | DEAD | Assumed, not derived |

**Bottom line:** 2 claims fully alive (bounce mechanism, no-go catalog), 3 alive but need reframing (fine-tuning, birefringence, galaxy spin), 6 dead (DE origin, H0, S8, PGT, GW, w=-1).
