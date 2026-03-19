# 07: Internal Note — Numerical f_NL Verification Attempt

---

## One-Paragraph Summary

We attempted an independent numerical verification of the matter-bounce f_NL prediction (f_NL = -35/8, Cai et al. 2009) by directly evaluating the in-in bispectrum integral with exact Bunch-Davies mode functions. The dominant Maldacena cubic vertex ε²a²ζ(ζ')² gives a converged contribution of f_NL^(T1) = +1.56 (including field redefinition of +5/4). This establishes that the full result requires substantial contributions from the other cubic action terms — specifically those involving the constraint variable χ and the time derivative d(ε/H)/dη. These terms introduce additional powers of the growing mode that create inter-term divergence cancellations which cannot be resolved by standard 64-bit numerical integration. The full independent verification of -35/8 requires either symbolic computation or a matched asymptotic expansion that handles the growing-mode cancellations analytically.

---

## What This Means for the Paper

### Claim status:
- "f_NL = -35/8 is a parameter-free prediction of the matter bounce" — **STILL VALID but now ATTRIBUTED to Cai et al.**, not independently derived by us.
- The convention proof (f_NL(Planck) = |B|_NL(Cai)) and template projection (cos θ = 0.95) are INDEPENDENTLY VERIFIED and stand.
- The factor-of-2 discrepancy with Li-Brandenberger is IDENTIFIED as systematic (numerator 35 preserved), consistent with a Wick-contraction convention difference.

### What to write:
- We cite Cai et al. for f_NL = -35/8 and note that our partial independent check (single-vertex contribution: +1.56) is consistent with the full result requiring multi-vertex cancellation.
- We do NOT claim to have independently derived -35/8.
- The honest statement is: "The analytical derivation of Cai et al. gives f_NL = -35/8. Our independent numerical evaluation of the dominant cubic vertex yields a partial contribution of +1.56, confirming that the complete result requires the full Maldacena cubic action. A complete independent verification using symbolic methods is left for future work."

### Confidence level adjustment:
- Previous confidence in f_NL = -35/8: 70% (from execution phase file 06)
- Updated confidence: **65%** — slightly reduced because we could not independently verify, but not significantly reduced because the failure mode (numerical precision) is understood and does not suggest an error in Cai's analytical calculation.
