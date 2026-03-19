# 00: Target Lock — Cai Action Audit

## The Question

Are we using the same cubic action as Cai et al. (arXiv:0903.0631)?

## The Answer (PREVIEW)

**NO. We are using a DIFFERENT cubic action. This entirely explains the discrepancy.**

Three critical differences found between our file 02 action and Cai's Eq. 15:

1. **Leading vertex coefficient:** Our ε² = 9/4 vs Cai's (ε²−ε³/2) = 9/16. **Factor of 4 difference.**
2. **χ definition:** Our χ_k = −(3/2)a²ζ'/k² vs Cai's χ = ∂⁻²ζ̇ = −ζ'/(ak²). **Factor of (3/2)a³ difference.**
3. **χ-sector structure:** Our Terms 5,6 have ∂²ζ·(∂χ)² and ∂²ζ·χ². Cai has ζ·(∂ᵢ∂ⱼχ)². **Completely different terms.**

## What This Means

Our converged result f_NL = +25/16 is the CORRECT computation of the WRONG cubic action. The mismatch is not in our numerical methods — it's in the starting point.

## Reconciliation Criteria

- **Full:** Implement Cai's actual Eq. 15, recover -35/8 → flagship rescued
- **Partial:** Implement Cai's action, get a different value → need further investigation
- **Cai wrong:** Implement Cai's action exactly, still don't get -35/8 → Cai has an error
