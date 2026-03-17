# Phase 1: Background Cosmology Audit

**Date:** 2026-03-13
**Status:** AUDIT COMPLETE — equations extracted from arxiv/main.tex (v1.6.0)

---

## 1. Complete Background Equation Set

### 1a. Modified Friedmann Equation (Eq. \ref{eq:modfriedmann}, main.tex:234)

```
H² = (8πG/3) ρ [1 − ρ/ρ_c]
```

- **Status:** DERIVED — standard LQC result extended to Einstein-Cartan theory
- **Origin:** Effective equations from loop quantum cosmology (Ashtekar, Pawlowski, Singh 2006)
- **Validity:** Isotropic, homogeneous sector; assumes sharply peaked quantum state

### 1b. Critical Density (Eq. \ref{eq:rhocrit}, main.tex:238)

```
ρ_c = 3 / (8πG γ² Δ) = (√3 / 32π²γ³) ρ_Pl ≈ 0.27 ρ_Pl
```

where:
- Δ = 4√3 π γ ℓ_P² (LQG area gap)
- ρ_Pl = c⁵/(ℏG²) ≈ 5.16 × 10⁹⁶ kg/m³
- γ = 0.274 ± 0.020 (Barbero-Immirzi parameter)

**Numerical value:** ρ_c ≈ 1.39 × 10⁹⁶ kg/m³ for γ = 0.274
**Range:** ρ_c ∈ [0.22, 0.34] ρ_Pl for γ ∈ [0.254, 0.294]

### 1c. Raychaudhuri Equation (derived from differentiating 1a + continuity)

```
Ḣ = −(κ/2)(ρ_eff + P_eff)(1 − 2ρ_eff/ρ_c)
```

where κ ≡ 8πG. This follows from the time derivative of the modified Friedmann equation combined with the continuity equation ρ̇ = −3H(ρ + P).

### 1d. Continuity Equation (standard)

```
ρ̇ + 3H(ρ + P) = 0
```

Unchanged from GR. Energy-momentum conservation is preserved because the modification enters through the gravitational sector, not the matter sector.

### 1e. Conformal Time Evolution

Converting to conformal time τ (where dτ = dt/a):

```
a'' = a × [H² + Ḣ]
   = a × (κ/3) × [(ρ + 3P_eff)/2 × (1 − ρ/ρ_c) − ρ²/ρ_c]
```

where primes denote d/dτ.

### 1f. Scale Factor at the Bounce

At the bounce (H = 0, ρ = ρ_c):

```
a_bounce = a_min (set by parent BH: a_min ≈ r_g = 2GM_BH/c²)
Ḣ_bounce = −(κ/2)(ρ_c + P_c)(1 − 2) = +(κ/2)(ρ_c + P_c) > 0
```

The bounce is a minimum of a(t) with Ḣ > 0 (for ρ + P > 0).

---

## 2. Four-Fermion Contact Interaction

### 2a. Torsion Equation (Eq. \ref{eq:torsion}, main.tex:182)

```
T^{abc} = 8πG S^{abc}
```

where S^{abc} = (1/4) ψ̄ γ^[a γ^{bc}] ψ is the fermionic spin density tensor.

**Key property:** Torsion is ALGEBRAIC (not dynamical). Determined instantaneously by matter content.

### 2b. Effective Four-Fermion Interaction (Eq. \ref{eq:4fermi}, main.tex:188)

```
L_int = −(3πG_N/2) × [γ²/(γ² + 1)] × J^μ_(A) J_{Aμ}
```

where J^μ_(A) = ψ̄ γ^μ γ^5 ψ is the axial current.

**Numerical factor:** γ²/(γ² + 1) ≈ 0.070 for γ = 0.274

### 2c. Effective Equation of State Modification

At high densities (ρ ~ ρ_c), the four-fermion interaction modifies the effective EOS:

```
w_eff(ρ) = w_bare + Δw_spin(ρ)
```

**UNKNOWN:** The functional form of Δw_spin(ρ) requires computing the spin condensate ⟨J_A J_A⟩ at Planck densities. This is NOT in the current paper.

---

## 3. Parity-Odd Effective Action

### 3a. Effective Action (Eq. \ref{eq:Seff}, main.tex:198)

```
S_eff = (α/M) ∫ e_I ∧ e_J ∧ F^{IJ}[K, R̊]
```

Component form:
```
S_eff = ∫ d⁴x √(−g) (α/M) ε^{μνρσ} e^I_μ e^J_ν F_{IJρσ}
```

### 3b. Parity-Odd Coefficient (Eq. \ref{eq:oneloop}, main.tex:214)

```
α/M ~ (g²/32π²)(γ/M) ln(Λ²_UV/μ²) + δ_NY
```

**Status:** PHENOMENOLOGICAL PARAMETER — one-loop estimate provides order of magnitude
**Value:** [(α/M) M_Pl] ~ 10⁻²

### 3c. RG Flow (Eq. \ref{eq:RGflow}, main.tex:220)

```
dα/d(ln μ) ~ −(g²/16π²) × 2N_f
```

Running is weak: g²/(16π²) ~ 10⁻³. α is approximately scale-independent.

---

## 4. Inflationary Dilution

### 4a. Dilution Factor (Eq. \ref{eq:Dinf}, main.tex:292)

```
D_inf = exp[−3N_tot] × (T_reh/M_GUT)^{3/2}
```

**Physical origin:** Contorsion K_{ab} ∝ a⁻³ dilutes during inflation.

### 4b. Dark Energy Scale (Eq. \ref{eq:rhoLambda}, main.tex:301)

```
ρ_Λ = [(α/M) M_Pl] × D_inf × M_Pl⁴ ≈ (2.3 meV)⁴
```

Requires N_tot ≈ 92 e-folds.

### 4c. Inflationary Suppression Factor

```
Ξ ≡ [(α/M) M_Pl] × D_inf ~ 10⁻² × 10⁻¹²¹ ~ 10⁻¹²³
```

---

## 5. Generalized Friedmann Equation (with rotation)

### 5a. Full Constraint (Eq. \ref{eq:genfriedmann}, main.tex:258)

```
H² = (8πG/3)ρ + Λ/3 + (1/3)(σ² − ω²) − k/a²
```

### 5b. Effective Cosmological Constant (Eq. \ref{eq:Leff_full}, main.tex:271)

```
Λ_eff = Ξ M_Pl² + c_ω ω²
```

**Crucial constraint:** |c_ω ω²|/H₀² < 2.5 × 10⁻²¹ (Planck CMB isotropy).
Rotation is COMPLETELY NEGLIGIBLE for background expansion.

---

## 6. Parameter Table

| Parameter | Symbol | Value | Status |
|-----------|--------|-------|--------|
| Barbero-Immirzi | γ | 0.274 ± 0.020 | Fixed (LQG) |
| Critical density | ρ_c | 0.27 ρ_Pl | Derived |
| Parity-odd coefficient | (α/M) M_Pl | ~10⁻² | Phenomenological |
| Total e-folds | N_tot | 92 | Fitted |
| Dilution factor | D_inf | ~10⁻¹²¹ | Derived |
| Reheating temperature | T_reh | ~10¹⁵ GeV | Assumed |
| GUT scale | M_GUT | ~10¹⁶ GeV | Assumed |
| Vorticity | ω₀ | <10⁻²⁸ s⁻¹ | Observational bound |
| Vorticity coefficient | c_ω | −1 | Derived |

---

## 7. Bounce Solution Continuity Check

### Pre-bounce contraction (ρ increasing toward ρ_c)

```
H < 0, Ḣ > 0 (for ρ approaching ρ_c from below)
a(t) decreasing, ρ increasing via continuity equation
EOS: w = w_bare (torsion effects negligible for ρ ≪ ρ_c)
```

**Status:** WELL-DEFINED. Standard contracting FLRW with modified Friedmann equation.

### Bounce phase (ρ ≈ ρ_c)

```
H = 0 at ρ = ρ_c
Ḣ = +(κ/2)(ρ_c + P_c) > 0 (bounce condition)
a(t) = a_min, turning point
EOS: w_eff = w_bare + Δw_spin(ρ_c) — UNKNOWN CORRECTION
```

**Status:** WELL-DEFINED in form, but Δw_spin(ρ_c) is not computed.
The bounce itself is guaranteed by H² = 0 at ρ = ρ_c with Ḣ > 0.

### Post-bounce expansion (ρ decreasing from ρ_c)

```
H > 0, increasing initially (Ḣ > 0 while ρ > ρ_c/2)
Then Ḣ → 0 as slow-roll inflation begins
a(t) increasing, ρ decreasing
EOS: transitions from w_eff(ρ_c) to w_inflation ≈ −1
```

**Status:** WELL-DEFINED in principle. The transition from bounce to slow-roll requires specifying the inflaton potential V(φ).

### Inflation onset

```
Requires: ρ_inflaton = V(φ) dominates over kinetic + spin condensate
Onset: when V(φ) > (1/2)φ̇² and slow-roll conditions ε₁ ≪ 1 are met
```

**Status:** ASSUMED to occur. Not derived from first principles within the framework.
Standard slow-roll inflation (e.g., Starobinsky R²) is grafted on after the bounce.

---

## 8. What Is Missing for Perturbation Theory

| Missing piece | Why it matters | Difficulty |
|--------------|----------------|------------|
| Spin condensate ⟨J_A J_A⟩(ρ) | Determines w_eff(ρ) and hence a(τ) through the bounce | HIGH — requires Planck-density QCD/fermion physics |
| Inflaton potential V(φ) | Determines bounce-to-inflation transition | MEDIUM — can parameterize |
| a(τ) numerical solution | Needed for z''/z | MEDIUM — standard ODE once w_eff is specified |
| Connection of ρ to conformal time τ | Needed for mode evolution | MEDIUM — follows from a(τ) |
| Parity-odd condensate dynamics Φ(τ) | Determines tensor chirality | HIGH — not derived |

---

## 9. Assumptions Used in Current Paper

1. **Isotropic bounce:** The modified Friedmann equation assumes exact FLRW symmetry at the bounce. Real BH interiors have anisotropy.
2. **Sharply peaked quantum state:** The effective equation H² = (8πG/3)ρ(1 − ρ/ρ_c) assumes the quantum state is peaked on the classical trajectory.
3. **Smooth connection to inflation:** The paper assumes the bounce connects to slow-roll without specifying the detailed dynamics.
4. **w = −1 at late times:** The diluted parity-odd residual is assumed to act as a true cosmological constant. Not derived.
5. **Torsion remains algebraic:** The parity-odd action contains ∂K terms that could promote torsion to dynamical, but this is argued to be suppressed by α/M ~ 10⁻²¹ GeV⁻¹.
