# Minimal Phenomenological P(k) Feature Model

**Date:** 2026-03-13
**Purpose:** Define the simplest P(k) feature model for the window analysis

---

## 1. Model Definition

The enhanced primordial scalar power spectrum:

**P_R(k) = A_s × (k/k_pivot)^{n_s − 1} × [1 + A_bump × exp(−(ln(k/k_*))² / (2Δ²))]**

where:
- A_s = 2.1 × 10⁻⁹ (standard scalar amplitude, Planck 2018)
- n_s = 0.965 (scalar spectral index, Planck 2018)
- k_pivot = 0.05 Mpc⁻¹

### Feature parameters (ALL purely phenomenological):

| Parameter | Symbol | Range | Status |
|-----------|--------|-------|--------|
| Feature scale | log₁₀(k_* / Mpc⁻¹) | 1 to 18 | **PROXY** — not derived from framework |
| Feature amplitude | log₁₀(A_bump) | 0 to 8 | **PROXY** — not derived from framework |
| Feature width | Δ | 0.5 to 3 (in ln k) | **PROXY** — fiducial Δ = 1 |

### What the parameters mean physically:

- **k_***: The comoving scale at which the bounce-to-inflation transition imprints its strongest feature. In LQC, this is set by a_bounce × H_bounce and the number of pre-observable e-folds.

- **A_bump**: The fractional enhancement above the standard nearly-scale-invariant spectrum. A_bump = 1 means the feature doubles the power; A_bump = 10⁷ puts P_R at the PBH threshold (~10⁻²).

- **Δ**: The width of the feature in e-folds of wavenumber. Δ = 1 means the feature spans ~1 decade in k. LQC calculations typically find Δ ~ 0.5–2 depending on the bounce model.

---

## 2. Observable Effects

### A. PBH Formation (k_* > 10⁴ Mpc⁻¹)

Enhanced P(k) at small scales can produce PBHs via gravitational collapse during radiation domination.

**Mapping:** P_R(k_*) → σ(M) → β(M) → f_PBH(M)

- Smoothed variance: σ²(M) ≈ (16/81) × P_R(k_*) × W_eff × Δ_eff
- Collapse fraction: β(M) = erfc(δ_c / (√2 σ)) / 2, with δ_c ≈ 0.45
- Present abundance: f_PBH ≈ 1.3 × 10⁸ × (M/M_☉)^{−1/2} × β(M)
- PBH mass: M/M_☉ ≈ 33 × (k_*/10⁶ Mpc⁻¹)^{−2}

The steep dependence of β on σ means the PBH abundance is an extremely sensitive function of P_R. The threshold for significant PBH production is P_R ~ 10⁻².

### B. Enhanced Halo Formation (k_* ~ 1–10⁴ Mpc⁻¹)

Enhanced P(k) at intermediate scales increases the variance σ(M_halo) at halo mass scales, boosting the number of massive halos at high redshift. This provides more sites for DCBH formation.

**Effect is indirect:** More halos → more DCBH formation sites → more SMBH seeds. Does not require PBH-level enhancement.

### C. μ-Distortion (k_* ~ 1–10⁴ Mpc⁻¹)

Dissipation of enhanced perturbations at z ~ 5 × 10⁴ to 2 × 10⁶ produces spectral distortions.

**Constraint:** μ ≈ 2.27 × ∫ [P_R(k) − P_R^{standard}(k)] × W_μ(k) × dk/k < 9 × 10⁻⁵ (FIRAS)

This constrains features at k < ~10⁴ Mpc⁻¹ only.

---

## 3. Parameter Status Classification

| Parameter | Derivable from framework? | What would be needed? |
|-----------|---------------------------|----------------------|
| k_* | IN PRINCIPLE YES | Full perturbation calculation through spin-torsion bounce + knowledge of N_tot |
| A_bump | IN PRINCIPLE YES | Same perturbation calculation |
| Δ | IN PRINCIPLE YES | Same perturbation calculation |

**Current status of the perturbation calculation: NOT DONE.**

The LQC literature (Agullo+, Wilson-Ewing, Zhu+) provides results for the standard LQC bounce. The spin-torsion variant differs in two ways:
1. Four-fermion contact interaction modifies the equation of state near the bounce
2. Parity-odd operator breaks tensor perturbation symmetry (potential 2nd-order scalar sourcing)

Neither effect has been calculated for perturbation evolution.

---

## 4. What the Framework DOES Constrain

Even without the full perturbation calculation, the framework constrains one thing:

**The comoving scale of the feature, given N_tot:**

k_* = k_pivot × exp(N_tot − N_pivot)

With N_tot = 92 (from the dark energy constraint): k_* ≈ 6 × 10¹⁴ Mpc⁻¹

This is the framework's ONLY current prediction for the feature location. It places the feature at sub-asteroid-mass PBH scales, completely irrelevant for SMBH seeds.

---

## 5. Honest Framing

This P(k) feature model is a **phenomenological scanning tool**, not a framework prediction. It parameterizes the unknown result of the perturbation calculation to determine:

1. What P(k) features the observations allow
2. What P(k) features would be useful for early SMBH seeds
3. Whether any overlap exists between (1) and (2)
4. Whether the framework's predicted feature scale (k_* ~ 10¹⁵ Mpc⁻¹) falls in the allowed region

The model becomes a framework prediction ONLY after the perturbation calculation is completed and k_*, A_bump, Δ are derived rather than scanned.
