# Email to Yi-Fu Cai

---

## Short Version (recommended)

**To:** yifucai@ustc.edu.cn
**Subject:** Normalization question on arXiv:0903.0631 — Eqs. 34-36 vs Eq. 37

Dear Prof. Cai,

I am an independent researcher working on forecasts for the matter-bounce non-Gaussianity prediction with SPHEREx. In the course of a detailed normalization audit of your 2009 paper (arXiv:0903.0631), I found a structural result I would like to confirm with you.

**Finding:** Your Eqs. 34, 35, and 36 (the ε-order decomposition) sum to exactly half of Eq. 37 (the combined polynomial) at all three benchmark configurations (squeezed, equilateral, folded). The ratio is 0.5000 to machine precision.

**Our interpretation:** Eqs. 34-36 give the single time-ordered correlator ⟨ζ³ L_int⟩, while Eq. 37 gives the full commutator result i⟨[ζ³, L_int]⟩ = -2 Im⟨ζ³ L_int⟩. The factor of 2 is the standard in-in commutator factor. Therefore -35/8 is the correct Planck-convention f_NL.

**Questions:**

1. Is this interpretation correct? Was Eq. 37 intended to include both time orderings (the full commutator)?

2. We also found that the printed polynomial coefficients in Eq. 37 — (3, 1, -9, 5, -66, 9) in the basis {Σk⁹, Σ_{i≠j}k⁷k², ...} — do not reproduce the published benchmark values (-35/8 squeezed, -255/64 equilateral, -9/4 folded). The unique coefficients that do are (2, 7, 3, -12, -69, 19). Is this a known typo?

3. Do you know the behavior of f_NL for near-matter contraction (ε slightly different from 3/2)? We found the correction is bounded [1-8%] at the Planck spectral tilt but could not determine the exact coefficient due to the delicate cancellation structure of the cubic integrals.

This would help us finalize a forecast paper on SPHEREx/MegaMapper detectability of the matter-bounce signal.

Best regards,
Houston Golden
Independent Researcher
houston@hubify.com
https://bigbounce.hubify.app

---

## Technical Appendix (paste below email if desired)

**Verification details:**

At equilateral (k₁ = k₂ = k₃ = 1):
- Eqs. 34+35+36 give A_T = -1.7930 → |B|_NL = -1.9922
- Eq. 37 polynomial gives A_T = -3.5859 → |B|_NL = -3.9844 = -255/64
- Ratio: 0.5000 exactly

At squeezed (k₁ → 0, k₂ = k₃ = 1):
- Eqs. 34+35+36 give |B|_NL = -35/16 = -2.1875
- Eq. 37 polynomial gives |B|_NL = -35/8 = -4.375
- Ratio: 0.5000 exactly

Polynomial coefficient verification (exact Fraction arithmetic):
- Published (3,1,-9,5,-66,9): gives -305/64 at squeezed (wrong)
- Correct (2,7,3,-12,-69,19): gives -35/8 at squeezed, -255/64 at equilateral, -9/4 at folded (all exact)
- Uniqueness: verified by linear independence of the 6 monomial sums (determinant ≠ 0)

We tested all four possible interpretations of the notation Σ_{i≠j≠k} and confirmed the published coefficients fail under all conventions.
