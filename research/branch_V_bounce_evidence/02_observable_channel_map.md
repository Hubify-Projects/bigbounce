# Branch V: Observable Channel Map

**Created:** 2026-03-17

---

## Overview

This document maps every observable channel where a bounce could leave an imprint, assesses what the minimal ECH bounce predicts in each channel, and identifies what extension would be needed to produce a detectable signal.

---

## Channel 1: Scalar Power Spectrum Features

### What the minimal model predicts
- Transfer function T(k) = 1 for all k ≪ k_b (Branch K result)
- Pre-bounce spectrum passes through unmodified
- No suppression, enhancement, or oscillation from the bounce itself

### What could produce a signal
- **Large-scale suppression** (k < k_0): If the contracting phase has finite duration, modes with wavelength > contracting Hubble radius never enter and get suppressed. This produces a low-ℓ deficit in the CMB TT spectrum — which Planck *actually observes* (anomalous low quadrupole and octupole).
- **Oscillatory features**: If the equation of state w(t) is not exactly constant through the bounce, modes that cross the Hubble radius near the transition imprint oscillatory features in P(k). Period set by bounce duration.
- **Infrared cutoff**: A symmetric bounce with finite pre-contraction phase has a maximum wavelength λ_max = c × t_contraction. Modes with λ > λ_max are absent, creating a sharp IR cutoff.

### Required extension
- Non-radiation equation of state near the bounce (w ≠ 1/3 during transition)
- Finite-duration contraction (breaks the eternal past assumption)
- Spectator field with mass ~ H_bounce that modifies the effective potential

### Experimental sensitivity
- Planck TT (ℓ < 30): already hints at low-ℓ deficit (2–3σ anomaly)
- CMB-S4: improved E-mode at low ℓ
- 21cm cosmology: access to very large scales

### Assessment: **HIGH PRIORITY** — connects to existing anomaly

---

## Channel 2: Primordial Black Holes (PBH)

### What the minimal model predicts
- No enhanced scalar perturbations at any scale
- Planck-mass PBHs form generically but evaporate by t ~ t_Pl
- No PBH dark matter candidate

### What could produce a signal
- **Enhanced P(k) at small scales**: If contraction phase has w < -1/3 episode or if a spectator field amplifies curvature perturbations during the bounce, P(k) could be enhanced at k ~ 10⁵–10⁶ Mpc⁻¹, producing solar-to-asteroid mass PBHs.
- **Non-Gaussian tail enhancement**: Even modest f_NL ~ O(10) at small scales exponentially enhances PBH formation rate.

### Required extension
- Phase of ultra-slow contraction (w → -∞ limit, i.e., ekpyrotic-type episode)
- Spectator field with tachyonic instability near bounce
- Non-adiabatic pressure perturbation (entropy modes)

### Experimental sensitivity
- Microlensing (OGLE, Subaru HSC): asteroid-to-solar mass window
- GW from PBH mergers (LIGO/Virgo/KAGRA): stellar mass window
- Induced GW background (PTA, LISA): all mass windows

### Assessment: **MEDIUM PRIORITY** — requires significant new physics beyond ECH

---

## Channel 3: Induced Gravitational Waves

### What the minimal model predicts
- No enhanced scalar perturbations → no significant induced GW
- Direct tensor signal at P_T ~ 10⁻⁶⁴ (unobservable)

### What could produce a signal
- **Scalar-induced GW from bounce-amplified perturbations**: If P(k) is enhanced at any scale by the bounce or contraction dynamics, second-order induced GW are produced at that scale. The induced Ω_GW ∝ [P_ζ(k)]² can be orders of magnitude larger than the direct tensor signal.
- **Resonant amplification**: If bounce duration matches a particular scale, resonant particle production can create a peaked scalar spectrum that sources peaked induced GW.

### Required extension
- Same as Channel 2 (enhanced small-scale P(k))
- OR: Parametric resonance during reheating (preheating) — universal, but bounce geometry may set specific resonance frequencies

### Experimental sensitivity
- NANOGrav/EPTA/PPTA: nHz band (f ~ 10⁻⁸ Hz)
- LISA: mHz band (f ~ 10⁻³ Hz)
- DECIGO/BBO: deci-Hz band
- LIGO/ET: Hz–kHz band

### Assessment: **MEDIUM-HIGH PRIORITY** — PTA results already showing excess

---

## Channel 4: Primordial Non-Gaussianity

### What the minimal model predicts
- f_NL ~ 10⁻⁵⁶ from bounce dynamics (Branch K)
- Effectively zero; no measurable bispectrum contribution

### What could produce a signal
- **Matter bounce non-Gaussianity**: If the contraction has w = 0 (dust-dominated), the matter bounce scenario produces f_NL^local ≈ 5/12 with a specific shape. This is a *prediction*, not a free parameter.
- **Ekpyrotic non-Gaussianity**: If contraction has w ≫ 1, ekpyrotic models produce f_NL^equil ~ O(1–10) with distinctive equilateral shape.
- **Entropy-to-curvature conversion**: Two-field models where isocurvature perturbations convert to curvature at the bounce generically produce f_NL ~ O(1).

### Required extension
- Non-radiation contraction (w ≠ 1/3)
- Multi-field dynamics (spectator or curvaton)
- Explicit conversion mechanism at the bounce

### Experimental sensitivity
- Planck: σ(f_NL^local) ≈ 5, σ(f_NL^equil) ≈ 26
- CMB-S4 + LSS: σ(f_NL^local) ≈ 1–2
- SPHEREx: σ(f_NL^local) ≈ 0.5

### Assessment: **HIGH PRIORITY** — specific predictions exist for modified contraction phases

---

## Channel 5: Tensor Spectrum Modifications

### What the minimal model predicts
- n_T = 0 (flat), P_T ~ 10⁻⁶⁴ (unobservable)
- No B-mode signal at any frequency

### What could produce a signal
- **Blue-tilted tensors from stiff contraction**: If w > 1/3 during contraction, tensor spectrum acquires blue tilt n_T > 0 (opposite to inflation's n_T < 0). For w = 1 (kinetic-dominated): n_T = 2. This is the classic matter bounce / ekpyrotic prediction.
- **Parity-violating tensors from Chern-Simons coupling**: Adding an explicit φR̃R term (absent in minimal ECH but present if the ALP couples to gravity) produces chiral GW with Δχ ≠ 0.
- **Amplification from non-minimal coupling**: ξφ²R term with ξ ~ 1 can amplify tensor modes near the bounce.

### Required extension
- Non-radiation equation of state (w > 1/3 during contraction)
- Explicit Chern-Simons gravitational coupling
- Non-minimal curvature coupling for the ALP

### Experimental sensitivity
- LiteBIRD: σ(r) ~ 10⁻³ (CMB B-modes)
- CMB-S4: σ(r) ~ 10⁻³–10⁻⁴
- LISA/DECIGO: direct detection at mHz–deci-Hz

### Assessment: **HIGH PRIORITY** — blue tilt is a smoking gun for bouncing cosmologies

---

## Channel 6: Reheating / N_eff Modifications

### What the minimal model predicts
- Bounce is at radiation temperature T ~ 10¹⁹ GeV
- All SM degrees of freedom already in equilibrium
- N_eff = 3.044 (standard)
- No modification needed — the bounce IS a radiation-dominated event

### What could produce a signal
- **Dark radiation from torsion decay**: If propagating torsion modes exist (beyond minimal ECH), they could decay into dark radiation after the bounce, modifying N_eff.
- **Spectral distortions**: Bounce-modified perturbation spectrum at k ~ 1–10⁴ Mpc⁻¹ produces μ- and y-distortions in the CMB blackbody.
- **BBN constraints**: If contraction phase produces entropy asymmetries, baryon-to-photon ratio η could be bounce-determined.

### Required extension
- Propagating torsion (requires going beyond EC to Poincaré gauge theory)
- Enhanced P(k) at distortion scales (same extension as Channel 1)
- Pre-bounce phase with asymmetric matter content

### Experimental sensitivity
- Planck: ΔN_eff < 0.3 (2σ)
- CMB-S4: ΔN_eff < 0.06
- PIXIE/PRISTINE: μ-distortion sensitivity ~ 10⁻⁸

### Assessment: **LOW PRIORITY** — minimal model already consistent; signals require large extensions

---

## Channel 7: Large-Scale Anomalies

### What the minimal model predicts
- No specific predictions for hemispherical asymmetry, alignment of multipoles, or cold spot
- Pre-bounce spectrum is inherited without modification

### What could produce a signal
- **Topology from contraction**: If the contracting phase has compact spatial topology, the finite volume imposes a mode cutoff that could explain the low quadrupole, alignments, and lack of large-angle correlations.
- **Pre-bounce anisotropy**: If the very early contraction phase is mildly anisotropic (Bianchi I), the bounce imprints a preferred direction that could explain hemispherical asymmetry.
- **Mode coupling at bounce**: Non-linear coupling at H = 0 could correlate otherwise independent large-scale modes.

### Required extension
- Compact spatial topology (T³ or other)
- Initial anisotropy in the contraction (Bianchi I/IX instead of FRW)
- Non-linear bounce dynamics beyond linear perturbation theory

### Experimental sensitivity
- Already observed by Planck (2–3σ anomalies in multiple channels)
- No new experiment needed — the data exist

### Assessment: **HIGH PRIORITY** — existing anomalies could be explained by bounce; data already in hand

---

## Summary Matrix

| Channel | Minimal Prediction | Extension Needed | Data Status | Priority |
|---------|-------------------|-----------------|-------------|----------|
| 1. Scalar features | T(k) = 1 | Non-radiation EOS, finite contraction | Planck hints | **HIGH** |
| 2. PBH | None | Enhanced small-scale P(k) | Limits exist | MEDIUM |
| 3. Induced GW | Negligible | Enhanced P(k) | PTA excess | MED-HIGH |
| 4. Non-Gaussianity | f_NL ~ 0 | Non-radiation contraction | Planck limits | **HIGH** |
| 5. Tensor mods | n_T = 0, P_T ~ 0 | Stiff contraction, CS coupling | Future expts | **HIGH** |
| 6. Reheating/N_eff | Standard | Propagating torsion | CMB-S4 needed | LOW |
| 7. Large-scale anomalies | None specific | Topology/anisotropy | Data exist | **HIGH** |

**Top channels:** 1, 4, 5, 7 — all point to the same class of extension: **modified contraction phase (w ≠ 1/3)**.
