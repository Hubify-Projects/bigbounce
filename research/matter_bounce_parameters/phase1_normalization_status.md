# Phase 1 Normalization Status — LOCKED

**Date:** 2026-03-23
**Status:** SUBSTANTIALLY COMPLETE

---

## Canonical Value

**f_NL = -35/8 = -4.375** (Planck convention)

## Confidence: 92%

## Why -35/8 is canonical

1. Cai et al. (2009) Eq. 37 produces -35/8 in the squeezed limit via the verified polynomial.
2. Cai's Eq. 20 explicitly states the Planck convention: ζ = ζ_g + (3/5) f_NL ζ_g².
3. The polynomial reproduces all three published benchmark values exactly (squeezed, equilateral, folded).

## Why -35/16 survives only as the single-ordering value

Li et al. (2017) obtain -35/16. Our Phase 1 audit established:

1. **All 4 individual vertex contributions match exactly** between Cai and Li at c_s = 1 (verified to 6 significant figures).
2. **Cai's ε-order decomposition (Eqs. 34+35+36) sums to exactly -35/16** — this is the single time-ordered correlator ⟨ζ³ L_int⟩.
3. **Cai's Eq. 37 = 2 × (Eqs. 34+35+36)** — the factor of 2 is the in-in commutator factor: i⟨[ζ³, L]⟩ = -2 Im⟨ζ³ L⟩.
4. The full bispectrum (both time orderings) is what Planck measures. So -35/8 is the physical Planck-convention value.
5. Li's -35/16 is the single-ordering piece, consistent with their `-2 Im` formula applied differently.

## What is proven vs inferred

| Statement | Status |
|-----------|--------|
| Polynomial reproduces 3 benchmarks | PROVEN (algebraic) |
| 4 vertices match Cai ↔ Li at c_s=1 | PROVEN (numerical, 6 digits) |
| Eqs. 34-36 sum to -35/16 | PROVEN (numerical, exact ratio 0.5000) |
| Eq. 37 = 2 × (Eqs. 34-36) | PROVEN (numerical, all 3 configs) |
| The factor of 2 is the commutator | STRONGLY INFERRED (standard QFT; Cai does not state explicitly) |
| -35/8 is Planck convention | STRONGLY INFERRED (Eq. 20 is explicit; mapping to |B|_NL is direct) |
| Independent numerical in-in confirmation | NOT YET DONE (prior attempt failed due to 3 errors, not re-run) |

## What could raise confidence beyond 92%

In priority order:
1. Contact Yi-Fu Cai to confirm the commutator interpretation (fastest)
2. Correct the 3 errors in fnl_combined_integrand/ and re-run the mpmath evaluation
3. Find another group's independent numerical evaluation in the literature
4. Full from-scratch in-in integral using Cai's cosmic-time mode functions

## Downstream use

For all current-data extraction and forecast work:
- **Use -35/8 as canonical.** Do not hedge between -35/8 and -35/16.
- **Keep -35/16 in appendix tables** for transparency, labeled "single-ordering convention."
- **Do not describe -35/8 as "independently confirmed."** Use "canonical, supported by normalization audit at 92% confidence."
