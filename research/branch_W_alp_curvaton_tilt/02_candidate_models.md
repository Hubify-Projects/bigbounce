# 02: Candidate Curvaton Models

**Created:** 2026-03-17
**Status:** COMPLETE

---

## Model A: Spectator ALP Curvaton with Quadratic Potential

### Action

$$
S_\sigma = -\int d^4x\,\sqrt{-g}\left[\frac{1}{2}(\partial\sigma)^2 + \frac{1}{2}m_\sigma^2 \sigma^2\right]
$$

where σ is the ALP (Barbero-Immirzi pseudoscalar), with mass m_σ.

The ALP also couples to photons via the Chern-Simons term (responsible for birefringence):

$$
S_{\sigma\gamma} = -\frac{g_{\sigma\gamma}}{4}\int d^4x\,\sqrt{-g}\,\sigma\, F_{\mu\nu}\tilde{F}^{\mu\nu}
$$

### When fluctuations are generated

During dust-dominated contraction: the ALP is a light spectator field (m_σ ≪ H). Its quantum vacuum fluctuations exit the Hubble radius and freeze out with nearly scale-invariant amplitude.

The ALP mode equation on the contracting background:

$$
\delta\sigma_k'' + \left(k^2 - \frac{a''}{a} + a^2 m_\sigma^2\right)\delta\sigma_k = 0
$$

For dust contraction: a''/a = 2/η² (same as z''/z for the inflaton). For a light field (a²m² ≪ k² during sub-Hubble evolution), the spectrum of δσ is:

$$
P_{\delta\sigma}(k) = \frac{H_k^2}{4\pi^2} \left[1 + O\left(\frac{m_\sigma^2}{H_k^2}\right)\right]
$$

where H_k is the Hubble rate when mode k crosses the Hubble radius during contraction.

### When curvature conversion happens

After the bounce, during radiation expansion:
1. The ALP oscillates when H drops below m_σ
2. ALP energy density ρ_σ ∝ a⁻³ (pressureless oscillations) grows relative to radiation ρ_r ∝ a⁻⁴
3. When ρ_σ/ρ_r becomes significant, the ALP's isocurvature perturbations are converted to curvature perturbations
4. The ALP eventually decays (via σFF̃ coupling) and reheats radiation

The curvature perturbation after ALP decay:

$$
\zeta = r_{\rm dec}\,\frac{\delta\sigma_*}{\sigma_*}
$$

where r_dec = 3ρ_σ/(4ρ_r + 3ρ_σ) at decay and σ_* is the background ALP field value.

### Biggest theoretical risk

**The ALP mass m_σ is constrained by birefringence observations** to be m_σ ~ 10⁻³³–10⁻³⁰ eV. For the curvaton mechanism to work, m_σ must simultaneously:
- Be small enough to be "light" during contraction (m_σ ≪ H at Hubble crossing)
- Be large enough to generate the observed tilt: n_s − 1 ≈ −2m_σ²/H_k²

These may be incompatible. If m_σ/H_k is too small, the tilt is negligible.

---

## Model B: Spectator ALP with Shallow pNGB Potential

### Action

$$
S_\sigma = -\int d^4x\,\sqrt{-g}\left[\frac{1}{2}(\partial\sigma)^2 + \Lambda^4\left(1 - \cos\frac{\sigma}{f}\right)\right]
$$

where f is the ALP decay constant and Λ⁴ = m_σ²f² sets the mass scale.

### Key difference from Model A

The potential is periodic and flat near σ = 0. For σ ≪ f, this reduces to Model A. But for σ ~ f, the potential has significant nonlinearity:

$$
V(\sigma) \approx \frac{1}{2}m_\sigma^2\sigma^2 - \frac{m_\sigma^2}{24f^2}\sigma^4 + \cdots
$$

The quartic correction modifies the spectral tilt:

$$
n_\sigma - 1 = -2\frac{m_\sigma^2}{H_k^2} + \frac{V''''\sigma_*^2}{3H_k^2 V''} + \cdots
$$

For σ_* ~ f, the self-interaction correction can be comparable to the mass correction, providing additional tilt.

### When fluctuations are generated

Same as Model A: during dust contraction.

### When curvature conversion happens

Same as Model A: ALP oscillation + decay in the expanding radiation phase.

### Biggest theoretical risk

**Isocurvature non-Gaussianity.** The nonlinear potential generates non-Gaussian ALP fluctuations, which convert to non-Gaussian curvature perturbations. The curvaton f_NL in this model:

$$
f_{\rm NL}^{\rm curv} \sim \frac{5}{4r_{\rm dec}} - \frac{5}{3} + \frac{5}{6}\frac{V'''}{V''}\frac{\sigma_*}{r_{\rm dec}}
$$

The self-interaction term can push f_NL to unacceptable values.

---

## Model C: Two-Field Bounce + Curvaton Conversion

### Setup

Two scalar fields:
- φ: inflaton-like field driving the dust contraction (V(φ) = ½m_φ²φ² → effective dust)
- σ: ALP curvaton (light spectator)

Both fields are present during contraction. The bounce is driven by the ECH ρ² correction from the total energy density.

### Action

$$
S = -\int d^4x\,\sqrt{-g}\left[\frac{1}{2}(\partial\phi)^2 + V(\phi) + \frac{1}{2}(\partial\sigma)^2 + U(\sigma) + g\,\phi^2\sigma^2\right]
$$

The last term is an optional interaction that can transfer energy between the two fields.

### When curvature conversion happens

**At the bounce itself.** If the two fields have different effective equations of state near the bounce (φ becomes stiff while σ remains light), the isocurvature perturbation $S_{φσ}$ converts to curvature ζ during the non-adiabatic bounce transition.

This is the mechanism proposed by Cai et al. (2009) for entropy-to-curvature conversion.

### Biggest theoretical risk

**The conversion efficiency is bounce-model-dependent.** The amount of tilt generated depends sensitively on how the fields interact during the bounce — exactly the regime where we have no ECH-specific perturbation corrections (Part A result). The conversion is computed using classical two-field perturbation theory, which is standard and not ECH-specific.

---

## Model D: ALP Isocurvature-to-Curvature Conversion After the Bounce

### Setup

The ALP is not a curvaton (it never dominates the energy density). Instead, it generates a correlated isocurvature perturbation that is partially converted to curvature by the ALP's coupling to radiation (via σFF̃).

### Mechanism

1. During contraction: ALP acquires fluctuations δσ (same as Models A/B)
2. Through the bounce: δσ passes through as an isocurvature mode (ζ_σ independent of ζ_φ)
3. After the bounce: the σFF̃ coupling causes ALP oscillations to damp into photons
4. This damping transfers ALP perturbations into photon number perturbations
5. The photon perturbation contribution modifies the total ζ

### Spectral tilt

The tilt comes from the ALP spectrum's k-dependence (same as Models A/B). The conversion is approximately:

$$
\zeta_{\rm total} = \zeta_{\rm bounce} + \alpha\,\frac{\delta\sigma_*}{\sigma_*}
$$

where α ≪ 1 (small conversion). The total spectrum:

$$
n_s - 1 = \alpha^2(n_\sigma - 1) / (1 + \alpha^2)
$$

This gives a red tilt if n_σ < 1, but suppressed by α².

### Biggest theoretical risk

**Double suppression.** The tilt is suppressed by both (m_σ/H)² and α². Achieving n_s − 1 = −0.035 requires either large α (meaning the ALP dominates — reduces to Model A) or large m_σ/H (meaning the ALP isn't light — inconsistent with spectator assumption).

---

## Summary

| Model | Tilt source | f_NL risk | ECH connection | Simplicity |
|-------|-----------|----------|----------------|------------|
| A: Quadratic curvaton | m_σ²/H² | 5/(4r_dec) − 5/3 | ALP = BI pseudoscalar | HIGH |
| B: pNGB curvaton | m_σ²/H² + self-interaction | Enhanced by V''' | ALP = BI pseudoscalar | MEDIUM |
| C: Two-field conversion | Bounce-phase entropy conversion | Model-dependent | Weak (classical 2-field) | LOW |
| D: Post-bounce isocurvature | Suppressed ALP transfer | Small (small α) | ALP = BI pseudoscalar | MEDIUM |
