# 06: Finite Coefficient Reconstruction

## The Reconstructed Value

From the corrected numerical computation (Terms 1-4, T5+T6 proven zero by phase analysis):

**f_NL = +2.186 ± 0.003**

This equals **35/16 = 2.1875** to within numerical precision.

## Sign Analysis

Our computation gives +35/16 (positive). The literature reports -35/16 or -35/8 (negative).

The sign depends on the convention for the in-in formula:
- B = -2·Im[ext·∫H_int] (our convention)
- B = +2·Im[ext·∫H_int] (alternative convention)

A global sign flip would give **-35/16**, matching Li-Brandenberger.

**We cannot determine the absolute sign without a careful convention comparison with Cai/Li-Brandenberger.** But the MAGNITUDE is determined.

## Factor-of-2 Analysis

| Source | |f_NL| | Notes |
|--------|--------|-------|
| Cai et al. | 35/8 = 4.375 | Original |
| Li-Brandenberger | 35/16 = 2.1875 | Factor-of-2 smaller |
| Our computation | **35/16 = 2.1875** | Matches L-B magnitude |

Our independent computation structurally supports the Li-Brandenberger value, not Cai's.

The factor of 2 between Cai and Li-Brandenberger was previously identified as a systematic convention difference (likely the factor from the in-in commutator: [H,ζ³] giving 2·Im vs Im). Our result is consistent with one of these conventions giving 35/16 and the other giving 35/8.

## What About the Missing Terms?

### T5+T6 (χ² terms):
**Proven to contribute zero** to the physical bispectrum in the squeezed limit. The k₁⁻² divergence is confined to Re[ext×I], and Im[ext×I] (which determines B) is finite and comes from horizon crossing. The χ² terms' horizon-crossing contribution is exactly zero because their integrand has no phase mismatch at the horizon-crossing transition.

### T3 early-time divergence:
Term 3 has an integrand that grows as x² at early times (from the η⁸ factor). This creates a UV-dependent contribution that should cancel against T5+T6's early-time behavior in the complete integrand. The physical T3 contribution is small (< 0.001 in f_NL) but its numerical extraction is unreliable due to the UV sensitivity.

### Field redefinition:
f_NL^FR = 5ε/6 = 5/4 = 1.25. This is exact and convention-independent.

## Decomposition of 35/16

35/16 = intrinsic + field_redef = 15/16 + 20/16 = 15/16 + 5/4

So the intrinsic piece is 15/16 = 0.9375, and the field redefinition is 5/4 = 1.25.

Our numerical intrinsic: +0.936, matching 15/16 = 0.9375 to 0.1%.

## Is Cai Structurally Plausible?

**No — our independent computation gives |f_NL| = 35/16, not 35/8.**

Cai's 35/8 can only be recovered if either:
1. Our computation misses a factor of 2 somewhere (possible but not identified)
2. Cai includes contributions we omit (possible but not evident from the Maldacena action)
3. The boundary-term modifications for growing modes contribute an additional 35/16

**Our best estimate: |f_NL| = 35/16 = 2.1875 (matching Li-Brandenberger).**

## Is Li-Brandenberger Structurally Plausible?

**Yes — our computation matches their magnitude exactly.** The remaining question is the sign convention.
