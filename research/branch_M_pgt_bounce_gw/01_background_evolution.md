# Background Evolution for the PGT Bounce

**Date:** 2026-03-16

---

## 1. Modified Friedmann Equation

The PGT bounce with a single propagating spin-0⁻ torsion mode
(Sector II, mass m_T) gives the modified Friedmann equation:

```
H² = (8πG/3) ρ (1 - ρ/ρ_crit)
```

with:

```
ρ_crit = m_T² M_Pl²
```

where m_T = M_Pl/(2√|t₃|) is the torsion mass. This has the
same FORM as the minimal EC bounce but with a tunable ρ_crit.

The Raychaudhuri equation:

```
Ḣ = -4πG ρ (1 + w)(1 - 2ρ/ρ_crit)
```

For radiation (w = 1/3):

```
Ḣ = -(16πG/3) ρ (1 - 2ρ/ρ_crit)
```

---

## 2. Radiation-Dominated Bounce

### Energy conservation

```
ρ̇ + 4Hρ = 0   →   ρ = ρ_b / (a/a_b)⁴
```

At the bounce: ρ = ρ_b = ρ_crit, H = 0.

### Exact scale factor

The solution is identical in form to the EC case:

```
a(t) = a_b (1 + 4α² t²)^{1/4}
```

where:

```
α² = (8πG/3) ρ_crit = (8π/3) m_T²
```

So α = m_T √(8π/3) ≈ 2.89 m_T.

**The bounce timescale is t_bounce ~ 1/α ~ 1/m_T.**

### Hubble parameter

```
H(t) = 2α²t / (1 + 4α²t²)
```

At t = 0: H = 0 (bounce).
At |t| ≫ 1/(2α): H → 1/(2t) (standard radiation expansion).

### Energy density

```
ρ(t) = ρ_crit / (1 + 4α²t²)
```

At t = 0: ρ = ρ_crit = m_T² M_Pl².
At late times: ρ → ρ_crit/(4α²t²) = 3M_Pl²/(32πt²) — standard
radiation.

---

## 3. Conformal Time

### Definition

```
η = ∫ dt/a(t)
```

With a(t) = a_b (1 + 4α²t²)^{1/4}:

```
dη = dt / [a_b (1 + 4α²t²)^{1/4}]
```

### Exact integral

This integral is expressible in terms of the hypergeometric function.
Using the substitution u = 2αt:

```
η = (1/a_b) ∫ du/(2α) × (1 + u²)^{-1/4}
  = 1/(2α a_b) ∫ du (1 + u²)^{-1/4}
```

The indefinite integral:

```
∫ du (1 + u²)^{-1/4} = u × ₂F₁(1/4, 1/2; 3/2; -u²)
```

For |u| ≫ 1 (far from bounce):

```
∫ du (1+u²)^{-1/4} ≈ ∫ du / u^{1/2} = 2√u   [leading behavior]
```

More precisely, for u ≫ 1:

```
η ≈ (1/(2αa_b)) × 2√(2αt) × [1 + O(1/α²t²)]
  = √(t/(α a_b²)) × √2
```

### Near-bounce expansion

For |t| ≪ 1/(2α) (near the bounce):

```
a(t) ≈ a_b [1 + α²t²]
η ≈ t/a_b [1 - α²t²/2 + ...]
```

So η ≈ t/a_b near the bounce (conformal and cosmic time are
proportional, since a ≈ a_b = const).

### Asymptotic behavior

For t → +∞ (expanding phase, standard radiation):

```
a ~ a_b (2αt)^{1/2}
η ~ ∫ dt / [a_b (2αt)^{1/2}] = √(2t/α) / a_b
```

In the standard radiation era: a = a_rad × η, so

```
a_rad = a_b × (2α)^{1/2} / √2 = a_b √α
```

giving a = a_b √α × η for large η.

---

## 4. Key Scales

### Bounce scale

```
k_b = α a_b = a_b m_T √(8π/3) ≈ 2.89 a_b m_T
```

This is the comoving wavenumber at which modes have wavelength
comparable to the bounce duration.

### Physical frequency today

```
f_b = k_b/(2π a_0) = (a_b/a_0) × α/(2π)
    = (T₀/T_b) × m_T √(8π/3) / (2π)
```

With T_b = ρ_crit^{1/4} = (m_T M_Pl)^{1/2}:

```
f_b = T₀ × m_T √(8π/3) / [(m_T M_Pl)^{1/2} × 2π]
    = T₀/(2π) × √(8π/3) × (m_T/M_Pl)^{1/2}
    ≈ 0.46 × T₀ × (m_T/M_Pl)^{1/2}
```

### Numerical evaluation

Using T₀ = 2.725 K = 2.35 × 10⁻⁴ eV = 5.69 × 10¹⁰ Hz (frequency
equivalent):

```
f_b ≈ 0.46 × 5.69 × 10¹⁰ × (m_T/M_Pl)^{1/2}  Hz
    ≈ 2.6 × 10¹⁰ × (m_T/M_Pl)^{1/2}  Hz
```

| m_T (GeV) | f_b (Hz) | Band |
|-----------|---------|------|
| 10⁷ | 2.4 × 10⁴ | LIGO |
| 10⁵ | 2.4 × 10³ | LIGO |
| 10³ | 2.4 × 10² | LIGO |
| 10 | 24 | LIGO/ET |
| 10⁻¹ | 2.4 | ET |
| 10⁻³ | 0.24 | Decihertz |
| 10⁻⁵ | 0.024 | LISA upper |
| 10⁻⁷ | 2.4 × 10⁻³ | LISA |
| 10⁻⁹ | 2.4 × 10⁻⁴ | LISA |

---

## 5. Effective Potential for Tensor Modes

The tensor perturbation equation in conformal time:

```
h_k'' + (k² - a''/a) h_k = 0
```

where prime is d/dη.

### Computing a''/a

From a(t) = a_b(1 + 4α²t²)^{1/4}:

```
ȧ = a_b × 2α²t / (1 + 4α²t²)^{3/4}

ä = a_b × 2α² × [(1 + 4α²t²) - 6α²t²] / (1 + 4α²t²)^{7/4}
  = a_b × 2α² × (1 - 2α²t²) / (1 + 4α²t²)^{7/4}
```

Converting to conformal time (using dt = a dη):

```
a' = da/dη = ȧ × a = a_b² × 2α²t / (1 + 4α²t²)^{1/2}

a'' = d(a')/dη = d(a')/dt × a
```

More directly, the effective potential:

```
a''/a = a²(ä/a + H²) = a² × [ä/a + (ȧ/a)²]
```

```
ä/a = 2α²(1 - 2α²t²) / (1 + 4α²t²)²

H² = 4α⁴t² / (1 + 4α²t²)²
```

Therefore:

```
a''/a = a² × [2α²(1 - 2α²t²) + 4α⁴t²] / (1 + 4α²t²)²
      = a² × 2α² / (1 + 4α²t²)²
      = a_b² × 2α² / (1 + 4α²t²)^{3/2}
```

### Properties of the potential

At t = 0 (bounce):
```
(a''/a)|_{bounce} = 2α² a_b² = 2 × (8π/3) m_T² a_b²
```

This is a positive peak (potential barrier). The height is
proportional to m_T² a_b².

For |t| → ∞:
```
a''/a → 2α² a_b² / (4α²t²)^{3/2} = a_b² / (4α t³)  →  0
```

The potential decays as 1/t³ — faster than the 1/η² decay of the
de Sitter effective potential.

### Barrier width

The potential drops to half its peak value when:

```
(1 + 4α²t²)^{3/2} = 2
1 + 4α²t² = 2^{2/3} ≈ 1.587
t_{1/2} = 1/(2α) × √(2^{2/3} - 1) ≈ 0.383/α
```

In conformal time (using η ≈ t/a_b near bounce):

```
η_{1/2} ≈ 0.383/(α a_b) = 0.383/k_b
```

**The barrier has width Δη ~ 1/k_b in conformal time.** This means
modes with k ≫ k_b pass through adiabatically (no particle
production) while modes with k ≲ k_b interact strongly with the
barrier.

---

## 6. Parametric Dependence

All background quantities depend on m_T through the combination α = m_T √(8π/3):

| Quantity | Expression | m_T dependence |
|----------|-----------|---------------|
| Bounce timescale | 1/α | ~ 1/m_T |
| Bounce Hubble peak | α | ~ m_T |
| Critical density | α² M_Pl²/8πG | ~ m_T² M_Pl² |
| Bounce temperature | (m_T M_Pl)^{1/2} | ~ m_T^{1/2} |
| Bounce scale k_b | α a_b | ~ m_T a_b |
| Feature frequency f_b | ~ (m_T/M_Pl)^{1/2} × T₀ | ~ m_T^{1/2} |
| Potential height | 2α² a_b² | ~ m_T² a_b² |
| Potential width | 1/k_b | ~ 1/(m_T a_b) |

**The entire background is a one-parameter family parameterized
by m_T.** Choosing m_T fixes the bounce scale, frequency, and
GW spectrum shape (up to the overall amplitude normalization from
a_b).
