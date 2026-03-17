# Phase 2 — Curvature Integral Balance

**Date:** 2026-03-15

---

## Purpose

Quantify each era's contribution to I_R = ∫ d⁴x √g R and determine
the balance conclusively.

---

## Setup

Assume compact spatial topology (3-torus with comoving volume V_c = L³).
All integrals are over proper time t with √g = a³(t).

The integral:
```
I_R = V_c × ∫ dt a³(t) R(t)
```

We work in natural units (ℏ = c = 1, G = 1/M_Pl²). Define:

```
J(era) ≡ ∫_era dt a³(t) R(t)
```

so that I_R = V_c × Σ_era J(era).

---

## Era-by-Era Computation

### 1. Bounce Epoch (|t| < τ_bounce ~ t_Pl)

From the bounce curvature profile:
```
R_bounce ~ 32π ρ²/(M_Pl² ρ_crit) ~ M_Pl²    at peak
a(t) ≈ a_min
Duration: Δt ~ t_Pl = 1/M_Pl
```

```
J_bounce ~ a_min³ × M_Pl² × (1/M_Pl) = a_min³ × M_Pl
```

### 2. Radiation Era (t_Pl < t < t_eq)

Standard radiation: R = 0 (trace of stress-energy vanishes for
radiation). The bounce-modified correction R ~ ρ²/ρ_crit is
negligible for ρ ≪ ρ_crit.

```
J_radiation ≈ 0
```

### 3. Matter Era (t_eq < t < t_Λ)

Matter domination: a(t) ∝ t^{2/3}, H = 2/(3t), R = 4/(3t²).

Parametrize: a(t) = a_eq (t/t_eq)^{2/3}.

```
J_matter = a_eq³ ∫_{t_eq}^{t_Λ} dt (t/t_eq)² × 4/(3t²)
         = a_eq³ × (4/3) / t_eq² × ∫_{t_eq}^{t_Λ} dt
         = a_eq³ × (4/3) × (t_Λ - t_eq) / t_eq²
```

Numerical values:
- t_eq ~ 5 × 10⁴ yr ~ 10¹² s ~ 10⁵⁵ t_Pl
- t_Λ ~ 10¹⁰ yr ~ 10¹⁷ s ~ 10⁶⁰ t_Pl
- a_eq: from radiation scaling a ∝ t^{1/2} from bounce to equality:
  a_eq = a_min × (t_eq/t_Pl)^{1/2} = a_min × 10^{55/2} ≈ a_min × 10^{27.5}

```
J_matter ≈ (a_min × 10^{27.5})³ × (4/3) × 10⁶⁰ t_Pl / (10⁵⁵ t_Pl)²
         = a_min³ × 10^{82.5} × (4/3) × 10⁶⁰ / 10^{110} × M_Pl
         = a_min³ × (4/3) × 10^{32.5} × M_Pl
```

**J_matter ~ a_min³ × 10^{32.5} × M_Pl**

### 4. Dark Energy Era (t > t_Λ)

De Sitter: R = 12H_Λ², a(t) = a_Λ exp[H_Λ(t - t_Λ)].

```
J_Λ = a_Λ³ × 12H_Λ² × ∫_{t_Λ}^{T} dt exp[3H_Λ(t - t_Λ)]
    = a_Λ³ × 12H_Λ² × [exp(3H_Λ(T - t_Λ)) - 1] / (3H_Λ)
    = 4 a_Λ³ H_Λ × [exp(3H_Λ(T - t_Λ)) - 1]
```

**This diverges exponentially as T → ∞.**

For finite future cutoff at T - t_Λ = N/H_Λ (N e-folds of expansion):
```
J_Λ ~ 4 a_Λ³ H_Λ × e^{3N}
```

After just N = 100 e-folds: e^{300} ~ 10^{130}.

With a_Λ = a_min × (t_eq/t_Pl)^{1/2} × (t_Λ/t_eq)^{2/3}:
- a_Λ ~ a_min × 10^{27.5} × (10⁶⁰/10⁵⁵)^{2/3} ~ a_min × 10^{27.5} × 10^{10/3}
- a_Λ ~ a_min × 10^{31}

```
J_Λ ~ 4 × (a_min × 10^{31})³ × H_Λ × e^{3N}
     = 4 × a_min³ × 10^{93} × H_Λ × e^{3N}
```

With H_Λ ~ 10⁻⁶⁰ M_Pl:
```
J_Λ ~ 4 × a_min³ × 10^{33} × M_Pl × e^{3N}
```

For N = 100: J_Λ ~ a_min³ × 10^{163} × M_Pl.

---

## Balance Sheet

| Era | J contribution (units of a_min³ M_Pl) | Relative |
|-----|---------------------------------------|----------|
| Bounce | 1 | 1 |
| Radiation | ~0 | 0 |
| Matter | ~10^{32.5} | 10^{32.5} |
| DE (N=10) | ~10^{46} | 10^{46} |
| DE (N=100) | ~10^{163} | 10^{163} |
| DE (N→∞) | ∞ | ∞ |

---

## Analysis

### The bounce is negligible

The bounce contributes a fraction:

```
J_bounce / J_matter ~ 10⁻³²
```

The bounce is 32 orders of magnitude below the matter era alone.
Including dark energy makes it infinitely worse.

### The integral is dominated by the FUTURE

If the universe accelerates forever, I_R diverges. The constraint
∫√g R = χ₀ (finite) is INCONSISTENT with eternal de Sitter expansion.

This means either:
1. The universe does NOT accelerate forever (future recollapse), or
2. The constraint must be modified (cutoff, weighting), or
3. The constraint is not viable.

### If the universe recollapses

If Λ_eff eventually becomes negative (or if the universe has a finite
future), I_R is finite. In this case, I_R is dominated by the era
with the LARGEST a³(t) R(t) product — which is the turnaround point
(maximum expansion, where a is largest and R may still be nonzero).

Even in a recollapsing universe, the bounce at a_min contributes
negligibly compared to the era near a_max.

---

## The Structural Problem

### Why the bounce always loses

The curvature integral I_R = ∫ a³ R dt is a VOLUME-WEIGHTED curvature
integral. The weighting factor a³ EXPONENTIALLY favors late times
(when a is large) over early times (when a is small).

The bounce has:
- LARGE R (~ M_Pl²)
- TINY a³ (~ a_min³)
- TINY Δt (~ t_Pl)

The matter/DE eras have:
- SMALL R (~ H²)
- ENORMOUS a³ (~ a_min³ × 10^{90+})
- LONG Δt (~ 10⁶⁰ t_Pl)

The product a³ × R × Δt is always dominated by late times because
the a³ growth (exponential during inflation/DE, power-law during
matter) overwhelms the R decrease.

### Quantitatively

```
(a³R Δt)_bounce / (a³R Δt)_matter
~ (a_min³ × M_Pl² × t_Pl) / (a_eq³ × H_eq² × t_Λ)
~ (a_min³ × M_Pl) / (a_min³ × 10^{82.5} × 10⁻¹¹⁰ × 10⁶⁰ × M_Pl)
~ 1 / 10^{32.5}
```

The bounce is ALWAYS subdominant by ~10³² in the volume-weighted
curvature integral.

### Could a different weighting help?

If instead of ∫√g R we used a CURVATURE-WEIGHTED integral like
∫√g R² or ∫√g |R|^p with p > 1, the bounce would be enhanced
relative to late times:

```
∫ a³ R² dt:
  Bounce: a_min³ × M_Pl⁴ × t_Pl ~ a_min³ × M_Pl³
  Matter: a_eq³ × H⁴ × t ~ a_min³ × 10^{82.5} × 10⁻²²⁰ × 10⁶⁰ × M_Pl³
        ~ a_min³ × 10⁻⁷⁷·⁵ × M_Pl³
```

With R²: **the bounce DOMINATES by 10^{77.5}!**

But: ∫√g R² is a HIGHER-CURVATURE integral. Constraining ∫√g R² = χ₀
is not the same as constraining ∫√g R = χ₀. The physical meaning
is different, and the modified Einstein equations from varying such
an action would involve fourth-order derivatives (Ostrogradski
instabilities).

**The linear curvature constraint (∫√g R = χ₀) is volume-dominated.
Higher-curvature constraints (∫√g R² = χ₀) are bounce-dominated
but pathological.**

---

## Conclusion

The global curvature constraint ∫√g R = χ₀ is:

1. **DIVERGENT** if the universe accelerates forever
2. **DOMINATED by late-time evolution** (not the bounce) if the
   universe recollapses
3. **INSENSITIVE to bounce physics** by a factor of ~10³² relative
   to the matter era alone

The bounce curvature pulse, despite being enormous (R ~ M_Pl²), is
confined to such a tiny spacetime volume (a_min³ × t_Pl) that its
contribution to the integrated curvature is negligible.

**The curvature constraint cannot link bounce physics to the
late-time cosmological constant.**
