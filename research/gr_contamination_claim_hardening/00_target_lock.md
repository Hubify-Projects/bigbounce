# 00: Target Lock

## Already Established Robustly
- Bounce vs tuned multifield: median BF = 425 (mock), 53 (analytic). P(BF>10) = 83-92%. ROBUST across 300k+ samples.
- Bounce prediction: f_NL = -35/8. Verified, mechanism-independent.
- Inflation mimicry penalty: kinematic (0 params) vs parametric (≥2 params).

## The Exact Caveat
Mock-based validation showed: UNMODELED GR contamination shifts recovered f_NL from -4.375 toward zero (SPHEREx: median -2.1; MegaMapper: median +1.2). This makes bounce vs standard single-field inflation INDISTINGUISHABLE when GR effects are not corrected.

## What This Pass Resolves
Whether the bounce-vs-SSFSR comparison can be RECOVERED once GR contamination is modeled as a nuisance parameter (marginalized over), rather than left unmodeled.

## Success Criteria
- **Robust resolution:** After GR marginalization, bounce vs SSFSR Bayes factor is >3 in >70% of realizations
- **Partial resolution:** BF > 3 in 50-70% of realizations (claim is conditional but defensible)
- **Unresolved but manageable:** BF > 3 in <50% but bounce-vs-tuned remains strong (conditional claim)
- **Serious blocker:** GR marginalization destroys the bounce-vs-tuned advantage too (would need rethinking)
