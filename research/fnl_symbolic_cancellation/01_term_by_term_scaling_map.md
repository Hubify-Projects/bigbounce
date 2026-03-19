# 01: Term-by-Term Scaling Map

## Background Scalings (ε = 3/2, a = a₀η²)

| Quantity | Superhorizon (|kη| ≪ 1) | η-scaling | k-scaling |
|----------|------------------------|-----------|-----------|
| ζ_k(η) | -i/(√(2k³)·A·η³) | η⁻³ | k⁻³/² |
| ζ'_k(η) | 3i/(√(2k³)·A·η⁴) | η⁻⁴ | k⁻³/² |
| χ_k(η) | -(3/2)a²ζ'_k/k² | constant | k⁻⁷/² |
| a²(η) | η⁴ | η⁴ | — |
| P(k) | 1/(2k³A²η⁶) | η⁻⁶ | k⁻³ |

## All 6 Terms After χ Substitution (Squeezed Limit, k₁→0, k₂=k₃=k)

### Term 1: (9/4)a²ζζ'²
**Dominant perm:** ζ_{k₁}·ζ'_k·ζ'_k

| Factor | Scaling |
|--------|---------|
| a² = η⁴ | η⁴ |
| ζ_{k₁} | k₁⁻³/²·η⁻³ |
| [ζ'_k]² | k⁻³·η⁻⁸ |
| **Integrand** | k₁⁻³/²·k⁻³·**η⁻⁷** |
| **D(f_NL)** | **0** |

### Term 2: (9/4)a²ζ(∂ζ)²
**Dominant perm:** ζ_{k₁}·k²·ζ_k·ζ_k (with -k₂·k₃ ≈ k² for squeezed)

| Factor | Scaling |
|--------|---------|
| Integrand | k₁⁻³/²·k⁻¹·**η⁻⁵** |
| **D(f_NL)** | **0** (suppressed by k²η²) |

### Term 3: -3a²ζ'(∂ζ)(∂χ) → after χ-sub
**Dominant perm with χ_{k₁}:** (9/4)·η⁸·ζ'_k·ζ_k·ζ'_{k₁} (k₁² from dot product cancels 1/k₁²)

| Factor | Scaling |
|--------|---------|
| η⁸ | η⁸ |
| ζ'_k·ζ_k | k⁻³·η⁻⁷ |
| ζ'_{k₁} | k₁⁻³/²·η⁻⁴ |
| **Integrand** | k₁⁻³/²·k⁻³·**η⁻³** |
| **D(f_NL)** | **0** |

### Term 4: (9/16)a²ζ²ζ'
**Dominant perm:** ζ_{k₁}·ζ_k·ζ'_k or ζ_k·ζ_k·ζ'_{k₁}

| Factor | Scaling |
|--------|---------|
| Integrand | k₁⁻³/²·k⁻³·**η⁻⁶** |
| **D(f_NL)** | **0** |

### Term 5: (3/4)∂²ζ(∂χ)² → after χ-sub
**With χ_{k₁}:** (k·k₁) factor provides k₁², cancels 1/k₁².

| Factor | Scaling |
|--------|---------|
| Integrand | k₁⁻³/²·k⁻³·**η⁻³** |
| **D(f_NL)** | **0** |

### Term 6: (9/32)∂²ζ·χ² → after χ-sub ⚠️
**Perm (b):** ka=k₂=k, {kb,kc}={k₁,k₃=k}
-(81/128)·k²/(k₁²·k²)·η⁸·ζ_k·ζ'_{k₁}·ζ'_k = -(81/128)/k₁²·η⁸·ζ_k·ζ'_{k₁}·ζ'_k

| Factor | Scaling |
|--------|---------|
| 1/k₁² | **k₁⁻²** (UNCOMPENSATED) |
| η⁸·ζ_k·ζ'_{k₁}·ζ'_k | k₁⁻³/²·k⁻³·η⁻³ |
| **Integrand** | **k₁⁻⁷/²**·k⁻³·η⁻³ |
| **D(f_NL)** | **-2** ⚠️ DIVERGENT |

## Phase Structure (Key to Resolution)

On superhorizon, the mode functions have definite phases:
- ζ_k → imaginary (coefficient -i)
- ζ'_k → imaginary (coefficient +3i)
- χ_k → constant real (after combining two imaginary factors)

For ANY term, the product (external legs)×(integral) has:
- External: ζ*_{k₁}·ζ*_k² → imaginary × real = **imaginary**
- Integral (superhorizon): all products work out to be **imaginary**
- Product: imaginary × imaginary = **REAL**
- Therefore: **Im[ext × integral_superhorizon] = 0 for ALL terms**

The physical bispectrum B = 2·Im[ext × integral] comes ENTIRELY from the horizon-crossing region.

The k₁⁻² divergence from T6 is in the **real part** of ext×integral (superhorizon regime). It does NOT appear in Im[ext×integral] from horizon crossing.

However, at **finite η_f**, corrections to the pure superhorizon phase structure introduce leakage of the real divergence into the imaginary part — this is the source of the numerical instability.

## Summary

The divergence from T6 is **real but confined to the wrong sector** (Re, not Im). The physical bispectrum is determined by Im[ext×integral], which is finite and comes from horizon crossing. The numerical difficulty arises because float64 cannot separate the O(10²⁷) physical signal from the O(10⁴⁹) background of the real divergence.
