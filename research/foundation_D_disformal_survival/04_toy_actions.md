# Foundation D — Toy Actions

**Date:** 2026-03-14

---

## Toy Action I: PGT 0⁻ Mode + Dirac Fermion (Baseline)

### Action

```
S_I = ∫ d⁴x √g [
    ½M_Pl² R(g)
    - ½Z(∂B)² - ½μ² B²
    + (g_eff)(∂_μ B)(ψ̄ γ^μ γ₅ ψ)
    + ψ̄(iγ^μ ∂_μ - m_f)ψ
]
```

### Effective metric analysis

The fermion equation of motion:

```
iγ^μ[∂_μ + g_eff(∂_μB)γ₅]ψ = m_f ψ
```

In a background B = B₀(t) on FRW:

```
iγ⁰[∂_t + g_eff Ḃ₀ γ₅]ψ + iγⁱ∂_i ψ = m_f ψ
```

The spatial propagation is UNMODIFIED. Only the time-derivative
receives a chiral shift. There is no disformal spatial structure.

For a plane wave ψ ~ u e^{i(Et - k·x)}:

```
Right-handed: (E + g_eff Ḃ₀)² = k² + m_f²
Left-handed:  (E - g_eff Ḃ₀)² = k² + m_f²
```

This is a CHIRAL FREQUENCY SHIFT, not a modified metric.
The group velocity dE/dk = k/E is the SAME for both chiralities.
There is NO propagation speed modification — only a frequency
(energy) shift.

### Classification

**CONFORMAL_ONLY (chiral gauge coupling).** Not even a conformal
metric — it's a gauge-like interaction that shifts energies but
not speeds.

---

## Toy Action II: PGT 0⁺ Mode + Dirac Fermion

### Action

```
S_II = ∫ d⁴x √g [
    ½M_Pl² R(g)
    - ½Z(∂φ)² - ½μ² φ²
    + (g_eff)(∂_μ φ)(ψ̄ γ^μ ψ)
    + ψ̄(iγ^μ ∂_μ - m_f)ψ
]
```

### Effective metric analysis

Field redefinition ψ → e^{-ig_eff φ}ψ removes all dependence
on φ from the fermion sector.

After redefinition:

```
S_II → ∫ d⁴x √g [
    ½M_Pl² R(g) - ½Z(∂φ)² - ½μ²φ²
    + ψ̄'(iγ^μ ∂_μ - m_f)ψ'
]
```

The fermion is COMPLETELY DECOUPLED from φ.

### Classification

**TRIVIAL.** No effective metric modification of any kind.

---

## Toy Action III: PGT with R² Terms + GW Sector

### Action

```
S_III = ∫ d⁴x √g [
    ½M_Pl² R + b₁ R² + b₂ R_μν R^μν
    + t_i T²
]
```

### Tensor perturbation equation on FRW

Linearize: g_μν = ḡ_μν + h_μν (transverse-traceless).

The R² terms modify the tensor equation:

```
[1 + 4b₁R̄/M_Pl² + 2b₂R̄/M_Pl²] ḧ_{ij}
+ ... spatial Laplacian terms ...
= 0
```

The GW speed:

```
c²_GW = [1 + 2b₂R̄/M_Pl²] / [1 + 4b₁R̄/M_Pl² + 2b₂R̄/M_Pl²]
      ≈ 1 + (2b₂ - 4b₁)R̄/M_Pl² + O(R²/M_Pl⁴)
```

For R̄ ~ H₀² ~ 10⁻⁶⁶ M_Pl²:

```
|c²_GW - 1| ~ |2b₂ - 4b₁| × 10⁻⁶⁶
```

For b_i ~ O(1): |Δc²| ~ 10⁻⁶⁶. GW170817 constraint: |Δc²| < 10⁻¹⁵.
Satisfied by 50+ orders of magnitude.

### Effective tensor metric

```
g̃^tensor_μν = (1/c²_GW)g_μν + (1 - 1/c²_GW)u_μu_ν
```

where u^μ = (1,0,0,0) in FRW comoving coordinates.

This IS a disformal structure but with coefficient ~ 10⁻⁶⁶.
Completely unobservable.

### Classification

**GENERIC_DISFORMAL.** The structure exists but is:
1. Planck-suppressed
2. Not geometry-specific (any R² theory gives this)
3. Already severely constrained by GW170817

---

## Toy Action IV: Non-Minimal Curvature-Fermion Coupling

### Action

```
S_IV = ∫ d⁴x √g [
    ½M_Pl² R(Γ)
    + t_i T²
    + ψ̄(iγ^μ D_μ(Γ) - m_f)ψ
    + (c₁/M_Pl²) R_μν(Γ) ψ̄ γ^μ i∂^ν ψ    [non-minimal coupling]
]
```

The last term is a DIMENSION-5 non-minimal coupling of the curvature
to the fermion kinetic term.

### After torsion elimination

R_μν(Γ) = R_μν(g) + (torsion-dependent terms). The torsion-dependent
part, after solving the torsion field equation, becomes:

```
R_μν(Γ) → R_μν(g) + c₂ (∂_μB)(∂_νB)/M_Pl² + ...
```

Substituting:

```
(c₁/M_Pl²)(∂_μB)(∂_νB)/M_Pl² × ψ̄ γ^μ i∂^ν ψ
= (c₁ c₂/M_Pl⁴)(∂_μB)(∂_νB)(ψ̄ γ^μ i∂^ν ψ)
```

### This IS disformal!

The structure (∂_μB)(∂_νB) × (fermion kinetic) is a disformal
effective metric for fermions:

```
g̃_μν^fermion = g_μν + (c₁c₂/M_Pl⁴)(∂_μB)(∂_νB)
```

### But: the coefficient is M_Pl⁻⁴

This is a DIMENSION-8 operator. Its effects are suppressed by:

```
|g̃ - g| ~ (c₁c₂/M_Pl⁴) × (∂B)² ~ (c₁c₂/M_Pl⁴) × (H f_a)²
```

For f_a ~ M_Pl: |g̃ - g| ~ (c₁c₂) H² / M_Pl² ~ 10⁻¹²² × c₁c₂.

Completely unobservable unless c₁c₂ ~ 10¹²² (absurd).

### Classification

**GENERIC_DISFORMAL (M_Pl⁻⁴ suppressed).** The disformal structure
EXISTS in principle but is:
1. A higher-dimensional operator (dimension-8)
2. Suppressed by M_Pl⁻⁴
3. Not specific to geometric theories (any gravitational EFT has
   such operators at dimension 8)

---

## Summary

| Toy Action | Effective metric | Conformal/Disformal | Coefficient | Observable? |
|-----------|-----------------|--------------------:|------------|------------|
| I: 0⁻ + fermion | Chiral shift only | Neither | g_eff ~ 1/M_Pl | Birefringence (generic ALP) |
| II: 0⁺ + fermion | None (removable) | N/A | 0 | No effect |
| III: R² + GW | c_GW ≠ 1 | Disformal | ~10⁻⁶⁶ | No (Planck-suppressed) |
| IV: Non-minimal | ∂B⊗∂B in g̃ | Disformal | ~10⁻¹²² | No (M_Pl⁻⁴) |

**No toy action produces an observable disformal effect from
geometric torsion/non-metricity structure.**
