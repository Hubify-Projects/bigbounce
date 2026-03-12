# Parameter Chain Inventory — Spin-Torsion → Dark Energy

**Date:** 2026-03-12
**Source:** arxiv/main.tex (Secs. 2–4), paper/02-theoretical-framework.md

---

## Derivation Chain Overview

```
Einstein-Cartan-Holst Action (Eq. 1)
  → Torsion activation by fermionic spin (Eq. 3)
    → Four-fermion contact interaction (Eq. 4)
      → Parity-odd effective action at one loop (Eq. 7)
        → Parity-odd coefficient α/M (Eq. 10)
          → Inflationary dilution D_inf (Eq. 13)
            → Present-day vacuum energy ρ_Λ (Eq. 14)
```

## Equation Inventory

### Eq. 1 — Einstein-Cartan-Holst Action (main.tex:157)
```
S_ECH = (1/16πG) ∫ d⁴x e [e^μ_a e^ν_b R^{ab}_{μν} + (1/γ) ε^{abcd} e_a^μ e_b^ν R_{cdμν} + (1/4) T^{abc} T_{abc}] + S_matter
```

### Eq. 2 — Barbero-Immirzi parameter (main.tex:164)
```
γ = 0.274 ± 0.020
```

### Eq. 3 — Torsion from spin density (main.tex:181)
```
T^{abc} = 8πG · S^{abc}
```
where `S^{abc} = (1/4) ψ̄ γ^[a γ^{bc}] ψ`

### Eq. 4 — Four-fermion interaction (main.tex:187)
```
L_int = -(3πG_N/2) × [γ²/(γ²+1)] × J_{(A)μ} J^μ_{(A)}
```
where `J^μ_{(A)} = ψ̄ γ^μ γ^5 ψ`

### Eq. 5 — Holst term in first-order form (main.tex:193)
```
S_Holst = (M_Pl²/γ) ∫ e_I ∧ e_J ∧ R^{IJ}(ω)
```

### Eq. 6 — Parity-odd effective action (main.tex:197)
```
S_eff = (α/M) ∫ e_I ∧ e_J ∧ F^{IJ}[K, R̊]
```

### Eq. 7 — Component form (main.tex:201)
```
S_eff = ∫ d⁴x √(-g) (α/M) ε^{μνρσ} e^I_μ e^J_ν F_{IJρσ}
```

### Eq. 8 — Effective cosmological constant (main.tex:270)
```
Λ_eff = Ξ · M_Pl² + c_ω ω²
```
where `Ξ ≡ [(α/M) · M_Pl] · D_inf`

### Eq. 9 — Vacuum energy density (main.tex:280)
```
ρ_Λ = [(α/M) · M_Pl] × D_inf × M_Pl⁴ ≈ (2.3 meV)⁴
```

### Eq. 10 — One-loop coefficient estimate (main.tex:213)
```
α/M ~ (g²/32π²) × (γ/M) × ln(Λ_UV²/μ²) + δ_NY
```

### Eq. 11 — Inflationary dilution factor (main.tex:291)
```
D_inf = exp(-3 N_tot) × (T_reh / M_GUT)^{3/2}
```

### Eq. 12 — Modified Friedmann (bounce) (main.tex:233)
```
H² = (8πG/3) ρ [1 - ρ/ρ_crit]
```

### Eq. 13 — Critical bounce density (main.tex:237)
```
ρ_crit = (√3 / 32π²γ³) ρ_Pl ≈ 0.27 ρ_Pl
```

---

## Complete Parameter Inventory

| Parameter | Symbol | Definition | Units | Value/Range | Source |
|-----------|--------|------------|-------|-------------|--------|
| Barbero-Immirzi parameter | γ | LQG area-spectrum quantization | dimensionless | 0.274 ± 0.020 | **Derived** (BH entropy) |
| BI suppression factor | γ²/(γ²+1) | Torsion-fermion coupling modifier | dimensionless | 0.070 ± 0.010 | **Derived** from γ |
| Newton's constant | G_N | Gravitational coupling | m³ kg⁻¹ s⁻² | 6.674×10⁻¹¹ | **Observed** |
| Planck mass | M_Pl | √(ℏc/G) | GeV | 1.221×10¹⁹ | **Derived** from G |
| Area-gap mass | M | √γ · M_Pl (LQG area gap scale) | GeV | ~6.4×10¹⁸ | **Derived** from γ, M_Pl |
| Parity-odd coefficient | α/M | Effective coupling of parity-odd operator | GeV⁻¹ | ~10⁻²¹ | **Phenomenological** (one-loop motivated) |
| Dimensionless parity-odd factor | (α/M)·M_Pl | Loop suppression factor | dimensionless | ~10⁻² | **Phenomenological** |
| Axial-torsion Yukawa coupling | g | Effective dimensionless coupling at area-gap scale | dimensionless | O(1) | **Derived** (order-of-magnitude) |
| UV cutoff | Λ_UV | LQG area-gap mass | GeV | ~√γ · M_Pl | **Assumed** (LQG motivated) |
| Renormalization scale | μ | Running scale | GeV | variable | **Free** (scheme-dependent) |
| Nieh-Yan finite part | δ_NY | Scheme-dependent counterterm | GeV⁻¹ | unknown | **Unknown** (scheme-dependent) |
| Total inflationary e-folds | N_tot | Total inflation duration | dimensionless | ~92 | **Fitted** (to match ρ_Λ) |
| Observable e-folds | N_obs | CMB-observable inflation | dimensionless | 55–60 | **Observed** (CMB) |
| Reheating temperature | T_reh | Post-inflation thermalization | GeV | ~10¹⁵ | **Assumed** (GUT-scale) |
| GUT scale | M_GUT | Grand unification energy | GeV | ~10¹⁶ | **Assumed** (standard) |
| Inflationary dilution factor | D_inf | exp(-3N_tot)·(T_reh/M_GUT)^{3/2} | dimensionless | ~10⁻¹²¹ | **Derived** from N_tot, T_reh, M_GUT |
| Dimensionless suppression | Ξ | [(α/M)·M_Pl]·D_inf | dimensionless | ~10⁻¹²³ | **Derived** |
| Observed vacuum energy | ρ_Λ | Dark energy density | GeV⁴ | 3×10⁻⁴⁷ | **Observed** |
| Cosmic vorticity | ω₀ | Present-day rotation rate | s⁻¹ | < 1.1×10⁻²⁸ | **Bounded** (CMB) |
| Vorticity coupling | c_ω | Convention factor | dimensionless | -1 | **Derived** (1+3 formalism) |
| Galaxy spin amplitude | A₀ | Parity asymmetry amplitude | dimensionless | ~0.003 | **Fitted** (galaxy data) |
| Fermion species count | N_f | Number of species at scale μ | dimensionless | variable | **Known** (SM content) |

## Classification Summary

| Category | Count | Parameters |
|----------|-------|------------|
| **First-principles derived** | 7 | γ, γ²/(γ²+1), M, g (order), ρ_crit, c_ω, Ξ (from inputs) |
| **Observed / measured** | 4 | G_N, M_Pl, ρ_Λ, N_obs |
| **Phenomenological (theory-motivated)** | 2 | α/M, (α/M)·M_Pl |
| **Fitted to data** | 2 | N_tot, A₀ |
| **Assumed** | 3 | T_reh, M_GUT, Λ_UV |
| **Unknown / scheme-dependent** | 2 | δ_NY, μ |
| **Bounded by observation** | 1 | ω₀ |
