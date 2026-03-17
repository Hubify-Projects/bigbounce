# 04: Dynamical Screening — Cheap Kills

**Created:** 2026-03-17
**Status:** COMPLETE

---

## Model A: Quadratic ALP Curvaton

### Can it achieve n_s ≈ 0.965?

The tilt from mass: n_σ − 1 ≈ −2m_σ²/(3H_k²)

To get n_σ − 1 = −0.035: m_σ²/H_k² ≈ 0.053, i.e., m_σ ≈ 0.23 H_k.

**H_k at CMB scale Hubble crossing during contraction:**

The CMB pivot scale k_* = 0.05 Mpc⁻¹ crosses the Hubble radius when k_* = a_k H_k. During matter contraction:

$$
H_k = \frac{2}{3|t_k|}, \quad a_k \propto |t_k|^{2/3}
$$

The Hubble rate at crossing depends on the unknown contraction history (how early the contraction began). This is the same free parameter that sets the amplitude A_s.

For a generic contraction: H_k at CMB crossing is much smaller than the Planck scale. If H_k ~ 10¹³ GeV (similar to the inflationary Hubble scale), then m_σ ~ 2 × 10¹² GeV.

**Comparison with birefringence ALP mass:** The cosmic birefringence ALP has mass m_σ ~ 10⁻³³–10⁻³⁰ eV ~ 10⁻⁶⁶–10⁻⁶³ M_Pl.

**THE BIREFRINGENCE ALP MASS IS ~75 ORDERS OF MAGNITUDE TOO SMALL.** m_σ/H_k ~ 10⁻⁷⁵. The tilt from this mass is:

$$
n_\sigma - 1 \sim -\frac{m_\sigma^2}{H_k^2} \sim -10^{-150}
$$

This is zero. The birefringence ALP cannot generate any measurable tilt.

### CHEAP KILL: The birefringence ALP and the curvaton ALP cannot be the same field.

If we want n_s = 0.965, the curvaton mass must be m ~ 0.2 H_k, which is vastly heavier than the birefringence ALP. **The ECH connection through the birefringence ALP is broken.**

A separate, heavier ALP could work as a curvaton, but it would not be the Barbero-Immirzi pseudoscalar responsible for birefringence. It would be a generic curvaton with no specific ECH motivation.

### Can it preserve acceptable f_NL?

The curvaton f_NL:

$$
f_{\rm NL}^{\rm curv} = \frac{5}{4r_{\rm dec}} - \frac{5}{3} - \frac{5}{6}\frac{r_{\rm dec}}{1}
$$

For the curvaton to dominate the curvature perturbation: r_dec must be O(1). If r_dec = 1 (curvaton completely dominates): f_NL = 5/4 − 5/3 − 5/6 ≈ −1.25.

If r_dec is small (curvaton subdominant): f_NL ≈ 5/(4r_dec) → large. For f_NL < 5 (1σ Planck): r_dec > 1/4.

**Acceptable f_NL requires r_dec > 0.25** — the curvaton must provide at least 25% of the curvature perturbation energy at decay. This is achievable but constraining.

### Does it require extreme tuning?

Two tunings:
1. **m_σ/H_k ≈ 0.23** — moderate tuning (within an order of magnitude)
2. **r_dec > 0.25** — moderate requirement on ALP lifetime and initial amplitude

**Assessment: ACHIEVABLE but with no ECH connection (birefringence ALP mass is wrong).**

### Verdict: **KILLED for ECH connection. Generic curvaton survives but is not novel.**

---

## Model B: pNGB ALP Curvaton

### Can it achieve n_s ≈ 0.965?

Same mass-induced tilt as Model A, plus self-interaction correction:

$$
n_\sigma - 1 \approx -\frac{2m_\sigma^2}{3H_k^2}\left(1 + \frac{\sigma_*^2}{6f^2}\right)
$$

The self-interaction helps if σ_*/f ~ O(1), enhancing the tilt by a factor of ~2. But the fundamental problem remains: m_σ must be ~ 0.1–0.2 H_k, which is ~75 orders of magnitude above the birefringence mass.

### Same cheap kill as Model A.

**Verdict: KILLED for the same reason. Mass scale incompatibility.**

---

## Model C: Two-Field Conversion at Bounce

### Can it achieve n_s ≈ 0.965?

The tilt comes from the isocurvature-to-curvature conversion at the bounce. This depends on the details of the two-field dynamics during the bounce, which are model-dependent.

In the Cai et al. (2009) treatment: conversion efficiency depends on the mass ratio m_σ/m_φ and the coupling g. For suitable parameters, a red tilt is achievable.

### Does it remain compatible with the bounce background?

Yes, as long as the second field is subdominant. But the conversion calculation requires tracking both fields through the bounce, which introduces dependence on bounce-specific matching conditions.

### f_NL?

Model-dependent. The no-go theorem (Quintin et al. 2015) suggests tension between tilt and non-Gaussianity in single-field models. Two-field models can evade this but at the cost of additional parameters.

### ECH connection?

WEAK. The two-field conversion is classical perturbation theory. ECH enters only through the background (which is the same as LQC). The conversion mechanism itself is not ECH-specific.

### Tuning?

Requires: specific mass ratio, coupling strength, and initial conditions for two fields. **More tuning than Model A with no ECH payoff.**

**Verdict: MIXED — achievable but over-parametrized and not ECH-specific. Already in literature (Cai & Brandenberger 2011).**

---

## Model D: Post-Bounce Isocurvature Transfer

### Can it achieve n_s ≈ 0.965?

The transfer is suppressed by α² (small conversion efficiency). To get n_s − 1 = −0.035:

$$
\alpha^2 \times (n_\sigma - 1) = -0.035
$$

If n_σ − 1 = −0.035 (from ALP mass): α² = 1 → not small, reduces to Model A.
If α² = 0.01: n_σ − 1 = −3.5 → massively blue curvaton → unphysical.

**Cannot generate sufficient tilt while remaining in the small-α regime.**

**Verdict: KILLED — double suppression makes it non-viable.**

---

## Summary

| Model | n_s ≈ 0.965? | f_NL OK? | ECH connection? | Tuning | Verdict |
|-------|-------------|---------|----------------|--------|---------|
| A: Quadratic curvaton | YES (for m ~ 0.2H) | YES (r_dec > 0.25) | **KILLED** (m incompatible with birefringence) | Moderate | Generic curvaton, not ECH-specific |
| B: pNGB curvaton | YES | YES | **KILLED** (same mass problem) | Moderate | Same as A |
| C: Two-field conversion | Maybe | Model-dependent | WEAK | High | Already in literature |
| D: Isocurvature transfer | NO | N/A | WEAK | N/A | Non-viable |

---

## The Fatal Insight

**The birefringence ALP mass (~10⁻³³ eV) and the curvaton mass needed for tilt (~10¹² GeV) are separated by ~75 orders of magnitude.**

The entire pitch of "ALP curvaton motivated by ECH" relied on identifying the curvaton with the Barbero-Immirzi pseudoscalar that also produces birefringence. This identification is **impossible** — the same field cannot have both masses.

Without this identification, the ALP curvaton is a generic curvaton with no ECH provenance. It reduces to the Cai & Brandenberger (2011) curvaton scenario, which is already in the literature.
