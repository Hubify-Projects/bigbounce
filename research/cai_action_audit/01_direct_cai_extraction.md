# 01: Direct Extraction from Cai et al. (arXiv:0903.0631)

## Authors
Yi-Fu Cai, Wei Xue, Robert Brandenberger, Xinmin Zhang

## Background
- Matter contraction: a(t) ~ t^{2/3}, w = 0, ε = 3/2
- Scalar field ϕ driving the contraction
- Variable: ζ = comoving curvature perturbation (Eq. 2)
- z = aϕ'/H (Eq. 3), v = zζ (Eq. 4)

## Mode Functions (Eq. 23-24)

Cai's mode function for ζ:

u_k(η) = A · i[1−ik(η−η̃_B)] / [√(2k³)(η−η̃_B)³] · exp[ik(η−η̃_B)]

Setting η̃_B = 0:

**u_k(η) = A·i·(1−ikη)·e^{+ikη} / [√(2k³)·η³]**

NOTE: This uses e^{+ikη}, not e^{-ikη} like our mode function!
The factor of i makes u_k = A × (complex conjugate of our ζ_k) (up to normalization).

Stripped mode function (Eq. 24):

**X_k(η) = (1−ikη)·e^{+ikη} / η³**

So u_k = A·i·X_k/√(2k³).

## Cubic Lagrangian (Eq. 15) — CRITICAL

**In COSMIC TIME:**

L₃ = (ε²−ε³/2)a³ζζ̇² + ε²aζ(∂ζ)² − 2ε²a³ζ̇(∂ζ)(∂χ) + (ε³/2)a³ζ(∂ᵢ∂ⱼχ)² + f(ζ)δL₂/δζ

where **χ ≡ ∂⁻²ζ̇** (inverse Laplacian of cosmic-time derivative).

At ε = 3/2:
- Term 1 coefficient: (9/4 − 27/16) = **9/16** (not 9/4!)
- Term 2 coefficient: 9/4 (but Cai omits this as "secondary")
- Term 3 coefficient: −2·(9/4) = −9/2
- Term 4 coefficient: (27/16)/2 = **27/32**

## Field Redefinition (Eq. 25-28)

ζ → ζ − f(ζ) where f(ζ) is given by Eq. 16.

**CRITICAL:** For the matter bounce (growing mode), the dominant terms in f(ζ) are the LAST THREE terms of Eq. 16 (not the first two as in inflation). The field redefinition produces the "A_red" shape function (Eq. 28):

A_red = (−ε/2 + ε/8 + ε²/32)·Σk³ᵢ + (momentum-dependent terms)

At ε = 3/2: leading coefficient = −3/4 + 3/16 + 9/64 = **−27/64**

## Definition of |B|_NL (Eq. 21)

|B|_NL = (10/3) · A_T / Σk³ᵢ

where A_T is the TOTAL shape function (sum of all contributions).

## In-In Formula (Eq. 14)

⟨ζζζ⟩ = **i** ∫ ⟨[ζ³, L_int]⟩ dt'

NOTE: Uses +i (not −i), and L_int (not H_int). This is consistent with our convention since i·[ζ³, L] = −i·[ζ³, −H] gives the same result.

## Individual Contributions (Eqs. 31-33)

Cai evaluates each vertex contribution to the shape function A:

- A_{ζζ̇²} = (−ε²/12 + ε³/24) Σk³ (Eq. 31)
- A_{ζ̇∂ζ∂χ} = (ε²/(24Πk²)) × [momentum terms] (Eq. 32)
- A_{ζ(∂ᵢ∂ⱼχ)²} from Eq. 33

## Total Shape Function (Eq. 37)

A_T = (3/(256Πk²ᵢ)) × [Σk⁹ + Σk⁷k²ⱼ − 9Σk⁶k³ⱼ + 5Σk⁵k⁴ⱼ − 66Σk⁵k²ⱼk²ₖ + 9Σk⁴k³ⱼk²ₖ]

## Final Result (Eq. 38)

In the squeezed limit k₁ ≪ k₂ = k₃:

**|B|^local_NL = −35/8**

And (Eq. 39): f^local_NL ≈ −35/8 (loosely, since the shape is not exactly local).
