# 00: Numerical Target Lock

---

## What Number Must Come Out

The Python script must output a SINGLE dimensionless number:

$$
f_{\rm NL} = f_{\rm NL}^{\rm intrinsic} + f_{\rm NL}^{\rm FR}
$$

where:
- f_NL^intrinsic = the in-in integral contribution (what we compute numerically)
- f_NL^FR = 5ε/6 = 5/4 = 1.25 (field redefinition, exact, no numerical evaluation needed)

---

## The Three Possible Outcomes

| Outcome | f_NL^intrinsic | f_NL total | Status |
|---------|---------------|------------|--------|
| Matches Cai et al. | -45/8 = -5.625 | -35/8 = -4.375 | Flagship confirmed |
| Matches Li-Brandenberger | -45/16 = -2.8125 | -35/16 = -2.1875 | Flagship weakened, still alive |
| Something else | ??? | ??? | New result — investigate |

---

## Extraction Formula (Planck Convention)

In the squeezed limit k₁ → 0, k₂ = k₃ = k:

$$
f_{\rm NL} = \frac{5}{12} \frac{B_\zeta(k_1, k, k)}{P_\zeta(k_1) P_\zeta(k)}
$$

This was PROVEN equivalent to Cai's |B|_NL in the squeezed limit (file 04 of execution phase).

---

## What the Script Must Do

1. Define exact Bunch-Davies mode functions g_k(η) and g'_k(η) for ν = 3/2
2. Construct the integrand for the dominant cubic vertex (9/4)M²_Pl a² ζ ζ'²
3. Evaluate the in-in time integral numerically (complex contour via iε prescription)
4. Sum all three permutations in the squeezed limit
5. Include the field redefinition contribution (+5/4)
6. Take the ratio B/(P·P) to extract f_NL
7. VERIFY that the result is independent of η_f (the late-time cutoff)

---

## Convergence Criteria

- The integral must converge to 4+ significant figures
- f_NL must be independent of η_f to within 0.1%
- f_NL must be independent of the squeeze ratio k₁/k to within 1% for k₁/k < 0.01
- The UV cutoff (early time) must not affect the result beyond 0.01%

---

## Success Condition

The script produces a number. That number either:
- Matches -35/8 to within numerical precision → Cai confirmed
- Matches -35/16 to within numerical precision → Li-Brandenberger confirmed
- Matches neither → new result, requires investigation

There is no "failure" mode except numerical instability. If the code crashes or doesn't converge, the code must be fixed, not the question abandoned.
