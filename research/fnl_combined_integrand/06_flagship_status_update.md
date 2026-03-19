# 06: Flagship Status Update

## Status: SERIOUSLY_THREATENED

The combined-integrand computation converges to f_NL = +25/16 = +1.5625, with Terms 3-6 contributing ZERO to the physical bispectrum. This contradicts Cai (-35/8) and Li-Brandenberger (-35/16) in both sign and magnitude.

## What This Means

If correct, the matter bounce produces f_NL ≈ +1.56, dominated by the field redefinition (+5/4). This is:
- Comparable to slow-roll inflation's f_NL ≈ (5/12)(1-n_s) ≈ 0.02 (but larger due to ε=3/2)
- NOT a distinctive signature — the matter bounce looks like a generic single-field model
- NOT detectable as a discriminator vs ΛCDM+inflation by MegaMapper or SPHEREx

## The Critical Caveat

Our Maldacena cubic action (from file 02) was reconstructed from memory, not verified line-by-line against Maldacena (2003) or Cai et al. (2009). If terms are missing, have wrong signs, or have wrong coefficients, the full answer could differ substantially.

The most likely missing piece: Cai et al. may use a DIFFERENT cubic action derivation (directly from the scalar field action, not via the ADM/Maldacena route). The ADM-derived action and the direct derivation should agree, but they might organize the terms differently or include additional contributions from:
- Second-order lapse/shift constraints
- Boundary terms from integration by parts
- Different field redefinition prescriptions

## What Remains True

1. T1 (dominant Maldacena vertex) gives +0.311 intrinsic — VERIFIED
2. Field redefinition gives +5/4 = 1.25 — EXACT
3. T3-T6 contribute zero to Im[ext×I] in the superhorizon limit — PROVEN
4. The convention equivalence f_NL = |B|_NL in squeezed limit — PROVEN
5. Template projection cos(θ) ≈ 0.95 — ESTABLISHED (independent of amplitude)

## Path Forward

The ONLY way to resolve the discrepancy is to compare our cubic action with Cai's. This requires:
1. Reading arXiv:0903.0631 (Cai, Chen, Namjoo, Sasaki, Wang, Wands 2009)
2. Identifying their cubic interaction Hamiltonian (their Eq. 23-27)
3. Comparing term-by-term with our file 02
4. Finding the missing or different terms
5. Re-running the combined-integrand computation with the correct action

If the correct action gives f_NL ≈ -35/8 → flagship rescued at full strength
If the correct action gives f_NL ≈ -35/16 → flagship alive at reduced strength
If the correct action confirms +25/16 → flagship collapses for f_NL discriminator
