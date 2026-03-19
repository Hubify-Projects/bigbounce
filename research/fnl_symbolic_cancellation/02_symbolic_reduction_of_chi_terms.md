# 02: Symbolic Reduction of χ-Terms

## The Constraint

∇²χ = (3/2)a²ζ'

In Fourier: χ_k = -(3/2)a²ζ'_k/k² = -(3/2)η⁴ζ'_k/k² (with a₀ = 1)

## χ-Substituted Terms

### Term 3: -3a²ζ'(∂ᵢζ)(∂ᵢχ)

Fourier (generic momenta k_a, k_b, k_c summing to zero):

L₃^{T3} = 3a² · (k_b · k_c) · ζ'_{ka} · ζ_{kb} · χ_{kc}

After χ substitution (χ_{kc} = -(3/2)η⁴ζ'_{kc}/k_c²):

L₃^{T3} = -(9/2) · (k_b · k_c)/k_c² · η⁸ · ζ'_{ka} · ζ_{kb} · ζ'_{kc}

**Squeezed limit with χ carrying k₁** (ka=k, kb=k, kc=k₁):
- k_b · k_c = k · k₁ = -k₁²/2
- Factor: -(9/2)·(-k₁²/2)/k₁² = +9/4
- Result: (9/4) · η⁸ · ζ'_k · ζ_k · ζ'_{k₁} → **FINITE** (k₁² cancels 1/k₁²)

### Term 5: (3/4)∂²ζ(∂χ)²

Fourier: (3/4) · k_a² · (k_b · k_c) · ζ_{ka} · χ_{kb} · χ_{kc}

After double χ substitution:

L₃^{T5} = (27/16) · k_a² · (k_b · k_c)/(k_b² · k_c²) · η⁸ · ζ_{ka} · ζ'_{kb} · ζ'_{kc}

(using χ_{kb}χ_{kc} = (9/4)η⁸ζ'_{kb}ζ'_{kc}/(k_b²k_c²))

**Squeezed limit with χ_{k₁}** (ka=k, kb=k₁, kc=k):
- k_b · k_c = k₁ · k = -k₁²/2
- Factor: (27/16) · k² · (-k₁²/2)/(k₁² · k²) = -27/32
- Result: -(27/32) · η⁸ · ζ_k · ζ'_{k₁} · ζ'_k → **FINITE**

### Term 6: (9/32)∂²ζ · χ²  ⚠️

Fourier: (9/32) · (-k_a²) · ζ_{ka} · χ_{kb} · χ_{kc}

After double χ substitution:

L₃^{T6} = -(81/128) · k_a²/(k_b² · k_c²) · η⁸ · ζ_{ka} · ζ'_{kb} · ζ'_{kc}

**Squeezed limit with χ_{k₁}** (ka=k, kb=k₁, kc=k):
- Factor: -(81/128) · k²/(k₁² · k²) = -(81/128)/k₁²
- Result: -(81/128)/k₁² · η⁸ · ζ_k · ζ'_{k₁} · ζ'_k → **DIVERGENT as k₁⁻²**

**No dot product (k_b · k_c) in the numerator.** The χ² vertex connects two χ fields WITHOUT spatial derivatives — unlike (∂χ)² which has derivatives providing the compensating k² factor.

## Combining T5 + T6 for fixed permutation

For the permutation ka=k, kb=k₁, kc=k:

T5+T6 = [-(27/32) - (81/128)/k₁²] · η⁸ · ζ_k · ζ'_{k₁} · ζ'_k

The -27/32 piece is finite. The -81/(128k₁²) piece diverges.

## Can Integration by Parts Help?

The χ² in Term 6 can be related to (∂χ)² via:

|∇χ|² = -χ · ∇²χ + ∇·(χ∇χ) = -(3/2)a² · χ · ζ' + boundary

So: χ² = ??? — this doesn't directly convert χ² into (∂χ)² without introducing new structures.

Integration by parts in TIME:
d/dη(something involving χ²ζ) might relate T6 to T5 or T4, but the time derivatives of a² = η⁴ produce additional terms.

**Conclusion:** Simple algebraic manipulation does not eliminate the k₁⁻² divergence from T6. The resolution lies outside the standard cubic action — specifically in the boundary terms of the in-in formalism for growing modes.
