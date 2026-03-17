# Branch U: Background Equations for Two-Field Model

**Date:** 2026-03-17
**Purpose:** Reference equations for the independent two-ALP model (U1), the only surviving candidate.

---

## Field Equations

For two independent ALPs φ_1, φ_2 with potentials V_1, V_2:

$$\ddot{\phi}_i + 3H\dot{\phi}_i + m_i^2 f_{a,i}\sin\!\left(\frac{\phi_i}{f_{a,i}}\right) = 0 \quad (i = 1, 2)$$

In angular variables θ_i = φ_i / f_{a,i}:

$$\ddot{\theta}_i + 3H\dot{\theta}_i + m_i^2\sin\theta_i = 0$$

---

## Friedmann Equation

$$H^2 = \frac{8\pi G}{3}\left[\rho_r + \rho_m + \rho_{\phi_1} + \rho_{\phi_2} + \rho_\Lambda\right]$$

where
$$\rho_{\phi_i} = \frac{1}{2}f_{a,i}^2\dot{\theta}_i^2 + m_i^2 f_{a,i}^2(1 - \cos\theta_i)$$

Note: in Model U1, ρ_Λ = 0 only if φ_2 provides all DE. In practice, φ_2 may provide partial DE with residual Λ.

---

## Birefringence

Only φ_1 couples to photons (or both couple, but φ_2 is frozen so contributes negligibly):

$$\beta = \frac{C_1\alpha_{\rm em}}{4\pi}\left[\theta_1(z_{\rm rec}) - \theta_1(z=0)\right] = \frac{C_1\alpha_{\rm em}\,\theta_{i,1}\,\eta_1}{4\pi}$$

The rolling efficiency η_1 depends on m_1 and H:
- m_1 >> H_0: η_1 → 1 (spectator regime, field fully rolled)
- m_1 ~ H_0: η_1 ~ 0.5-0.9 (partially rolled)

---

## Dark Energy from φ_2

For φ_2 to provide DE:
- m_2 ≲ H_0 (field frozen today)
- θ_{i,2} such that V_2(θ_{i,2}) = ρ_DE = 3H_0²M_Pl²(1 - Ω_m)

This gives:
$$m_2^2 f_{a,2}^2 (1 - \cos\theta_{i,2}) = \rho_{\rm DE}$$

For f_{a,2} = M_Pl:
$$m_2^2(1 - \cos\theta_{i,2}) = 3H_0^2(1 - \Omega_m) \approx 2H_0^2$$

So m_2 ~ H_0 / √(1 - cos θ_{i,2}). For θ_{i,2} ~ 1: m_2 ~ 2.2 H_0.

---

## Equation of State

$$w_{\phi_2} = \frac{\frac{1}{2}f_{a,2}^2\dot{\theta}_2^2 - V_2}{\frac{1}{2}f_{a,2}^2\dot{\theta}_2^2 + V_2}$$

For frozen field (ḃθ_2 → 0): w → -1 (cosmological constant-like).
For rolling field: w > -1 (quintessence).

The transition from w = -1 to w > -1 occurs when 3H ~ m_2, i.e., when the Hubble friction can no longer prevent rolling. For m_2 ~ H_0, this happens around z ~ 0 — the field is just starting to roll today.

---

## Parameter Count

| Parameter | Role | Fiducial |
|-----------|------|----------|
| θ_{i,1} | Birefringence amplitude | ~1.3 (from MCMC) |
| m_1 | Birefringence ALP mass | ~10^{-31} eV (spectator) |
| f_{a,1} | Decay constant | M_Pl (fixed) |
| C_1 | Anomaly coefficient | 8 (fixed, SM) |
| θ_{i,2} | DE field initial angle | ~1 (natural) |
| m_2 | DE ALP mass | ~H_0 (tuned) |
| f_{a,2} | DE decay constant | M_Pl (fixed) |

**Free parameters:** 4 (θ_{i,1}, m_1, θ_{i,2}, m_2)
**Effectively constrained:** 2 (θ_{i,1} from birefringence, m_2 from Ω_DE)
**Unconstrained:** 2 (m_1 weakly bounded, θ_{i,2} degenerate with m_2)

---

## Comparison with Spectator ALP + Λ

| Feature | Model U1 (two-ALP) | Spectator ALP + Λ |
|---------|--------------------|--------------------|
| Free params | 4 | 2 + 1 (Λ) |
| Birefringence | β = C α θ_{i,1} η_1 / (4π) | Same |
| DE | V_2(θ_{i,2}) ~ ρ_DE | Λ |
| w_DE | -1 + O(m_2²/H_0²) | -1 exactly |
| CC problem | YES (m_2 ~ H_0) | YES (Λ ~ H_0² M_Pl²) |
| New prediction | w(z) deviates from -1 at z < 1 | None |
| Testable? | DESI DR2 w(z) | Not distinguishable |

The only genuine new prediction of Model U1 vs spectator + Λ is a time-dependent equation of state w(z) ≠ -1 at z ≲ 1. This is exactly what DESI is measuring. However, the predicted deviation is tiny: δw ~ m_2²/(9H_0²) ~ O(0.01-0.1), currently below DESI sensitivity.

---

## Bottom Line

The two-field equations are straightforward. The model works. But it is spectator ALP + ultralight quintessence — a known model class with no ECH-specific content. The equations are included here for completeness, but the model does not warrant a dedicated MCMC analysis for this paper.
