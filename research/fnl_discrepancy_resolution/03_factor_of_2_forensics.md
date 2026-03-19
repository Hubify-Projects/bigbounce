# 03: Factor-of-2 Forensics

## Current Situation

We cannot isolate a clean "factor of 2" because our computation is incomplete — we only have Term 1 reliably computed. The factor-of-2 between Cai (-35/8) and Li-Brandenberger (-35/16) might be:

### Hypothesis A: Permutation counting
The vertex ζ(ζ')² has 3 permutations. If one reference counts 3 and the other counts 6 (including the trivial swap of the two ζ' legs), this gives a factor of 2.
**Assessment:** Plausible but hard to verify without the papers in hand.

### Hypothesis B: Commutator factor
The in-in formula gives B = 2·Im[F]. If one reference omits the factor of 2 from the commutator:
B = Im[F] instead of 2·Im[F]
**Assessment:** This is the most commonly cited source of the factor-of-2 in the literature.

### Hypothesis C: f_NL definition
If Cai defines f_NL = (5/6)·B/(P²) while the Planck convention uses (5/12)·B/(P²), there's a factor of 2.
Wait: (5/6)/(5/12) = 2. So:
- Cai with (5/6): f_NL = -35/8
- Same B with (5/12): f_NL = -35/16
**Assessment:** Plausible. Some early bounce papers use the CMB convention where f_NL = (5/6)·(B/(P·P)), while later papers use the LSS convention (5/12).

### Hypothesis D: Template normalization
The local template ζ = ζ_G + (3/5)f_NL ζ_G² vs ζ = ζ_G + f_NL ζ_G²:
If Cai defines without the 3/5 factor, their f_NL is (5/3)× the Planck convention.
5/3 ≈ 1.67, not 2. **Not this.**

### Most Likely Source

**Hypothesis C (extraction formula factor of 2)** is the most likely. This has been flagged in the bounce bispectrum literature before: some papers use (10/3) in their |B|_NL definition where others use (5/3), producing exactly the factor of 2.

From our convention proof (file 03/04 of execution phase):
f_NL(Planck) = (5/3)·A_T / k³ in the squeezed limit
|B|_NL(Cai) = (10/3)·A_T / (k₁³+2k³)

In the squeezed limit k₁→0: |B|_NL = (10/3)·A_T/(2k³) = (5/3)·A_T/k³ = f_NL

So f_NL = |B|_NL in the squeezed limit. This was PROVEN.

If this proof is correct, the factor of 2 must sit ELSEWHERE — perhaps in how Cai normalizes A_T vs how L-B normalize it.

### Conclusion
The factor-of-2 cannot be definitively resolved without computing all 6 terms. Our single-term result (+1.56 from T1) is consistent with ALL three possibilities (-35/8, -35/16, or something else) once the unknown T3-T6 contributions are included.
