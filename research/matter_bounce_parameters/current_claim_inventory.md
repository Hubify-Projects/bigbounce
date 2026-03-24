# Current Claim Inventory

**Date:** 2026-03-23
**Purpose:** Exhaustive list of every matter-bounce claim, where it appears, and its evidence grade.

---

## Claim 1: f_NL = -35/8 = -4.375 (Planck convention)

**Evidence grade: B** (strong but not independently confirmed)

| Evidence for | Status |
|-------------|--------|
| Cai et al. (2009) original derivation | Published, 200+ citations, no errata |
| Our algebraic polynomial verification | Reproduces all 3 benchmark values exactly |
| Vertex-by-vertex match with Li et al. at c_s=1 | 4/4 vertices match to 6 significant figures |
| Factor-of-2 traced to permutation accounting | Structural argument, not fully closed |
| Gradient expansion confirms sign, magnitude, shape | Independent method, same numerical bottleneck |

| Evidence against / uncertainty | Status |
|-------------------------------|--------|
| Our independent mpmath evaluation gave +25/16 (WRONG) | Attributed to 3 implementation errors in cubic action |
| Those 3 errors have NOT been verified as the full explanation | The "rescue" was algebraic, not numerical re-evaluation |
| No independent group has published a reproduction of -35/8 | Li et al. is the only other computation (gives -35/16) |
| Gradient expansion cannot resolve -35/8 vs -35/16 | Same bottleneck |

**Where it appears:**
- Paper 2: abstract, Eq. 2, Sec 2.1, Sec 2.3, throughout
- Paper 1: summary table (line 102), Sec 6 (line 710)
- Website: index.html (6 places), paper.html (4), explained.html (4), glossary.html (3), articles/ (20+), activity.html (3), dossier (5+)

---

## Claim 2: Template mismatch r = 0.84 ± 0.02

**Evidence grade: A-** (strong and reproducible, but uses simplified framework)

| Evidence for | Status |
|-------------|--------|
| Computed via numerical integration over verified Cai polynomial | Correct for the polynomial used |
| Stable across 10 weighting schemes | Range [0.82, 0.88] |
| Insensitive to squeezed cutoffs | Δr < 0.0002 |
| Coefficient sensitivity ±0.01 | 5 valid polynomial sets tested |
| Region decomposition shows mismatch is shape-intrinsic | Folded limit drives it (B_NL = -2.25 vs -4.375) |

| Limitations | Status |
|-------------|--------|
| Uses simplified shape inner product, not actual Planck/survey pipeline | No external validation |
| Polynomial is underdetermined (3 constraints, 6 coefficients) | Adds ±0.01 systematic |
| Weighting functions are idealized, not survey-specific transfer functions | Could shift r by ~0.02 |
| Does not account for ℓ-by-ℓ CMB bispectrum estimator structure | Planck modal estimator would be definitive |

**Where it appears:**
- Paper 2: abstract, Sec 3.2 (Eq. 4), Sec 4, throughout
- Website: index.html (6 places), paper.html (4), explained.html (2), glossary.html (2), figures.html (1), data-explorer.html (1 dataset), contributions.html (1)

---

## Claim 3: SPHEREx significance ~5.5σ (template-corrected)

**Evidence grade: C+** (downstream consequence of Claims 1 + 2 + inherited forecast)

| Component | Source | Grade |
|-----------|--------|-------|
| f_NL = -4.375 | Cai et al. + our audit | B |
| r = 0.876 (CMB Fisher) | Our computation | A- |
| σ(f_NL) = 0.7 | Heinrich et al. 2023 (inherited) | External |
| 5.5 = 4.375 × 0.876 / 0.7 | Arithmetic | Exact |

**Key vulnerability:** The inherited σ = 0.7 is from Heinrich et al.'s bispectrum forecast which assumes the LOCAL template. A bounce-specific Fisher forecast would give a different σ. We did NOT compute a bounce-specific Fisher matrix.

**Where it appears:**
- Paper 2: abstract, Sec 4, Fig 2
- Website: index.html (stat card), paper.html, explained.html (3), glossary.html (2), timeline.html, articles/ (2+)

---

## Claim 4: Normalization audit (90% confidence, vertex match)

**Evidence grade: B** (strong internal analysis, not externally validated)

| What we showed | Status |
|---------------|--------|
| 4 vertex Σk³ coefficients match exactly | Numerically verified |
| Factor-of-2 is in momentum-dependent polynomial | Demonstrated via squeezed-limit A_T comparison |
| Cai's convention matches Planck definition | Eq. (20) explicitly states ζ = ζ_g + (3/5)f_NL ζ_g² |

| What we did NOT show | Status |
|--------------------|--------|
| Independent re-evaluation of the full Cai in-in integral | NOT DONE (our attempt gave +25/16 due to errors) |
| Explicit tracing of permutation factor in Wick contractions | Structural argument only |
| Contact with Cai to confirm | NOT DONE |

---

## Claim 5: Consistency relation f_NL(n_s) = -4.375 - 0.73(n_s - 1)

**Evidence grade: C** (scaling estimate, not a derivation)

| What we have | Status |
|-------------|--------|
| ε scaling of cubic action prefactors | Correct for explicit ε factors |
| δε = -0.0045 for w = -0.003 | Exact |
| Coefficient c₁ ≈ 2 estimated from scaling | ESTIMATE, not derived |

| What we need | Status |
|-------------|--------|
| General-ε mode functions (non-integer Hankel) | NOT computed |
| Re-evaluation of Cai integrals with general ε | NOT done |
| Full polynomial structure change with ε | NOT captured |

---

## Claim 6: Bayes factors ~8-17:1 (bounce vs tuned multifield)

**Evidence grade: B** (Monte Carlo computation is correct given inputs)

Depends on: Claims 1-3 as inputs, plus prior choices.
Paper 2 already has extensive sensitivity analysis and honest caveats.
This claim is downstream — its credibility tracks Claims 1-3.

---

## CRITICAL ANOMALY: fnl_combined_integrand result

**The only independent numerical attempt to evaluate the in-in integral gave f_NL = +25/16 = +1.5625.** This is opposite in sign and different in magnitude from -35/8.

The bispectrum_rescue identified 3 errors in that computation:
1. Wrong cubic action coefficient (ε² = 9/4 instead of ε²-ε³/2 = 9/16)
2. Wrong mode function phase (e^{-ikη} instead of e^{+ikη})
3. Wrong χ definition (∇²χ = (3/2)a²ζ' instead of χ = ∂⁻²ζ̇)

**These errors were identified but NOT corrected and re-run.** The "rescue" verified Cai's polynomial algebraically but did not produce a corrected numerical evaluation. Therefore:

- We have NEVER independently computed f_NL = -35/8 from scratch
- Our confidence rests on: Cai being right + convention resolution + structural arguments
- A corrected numerical re-evaluation is the single highest-priority validation task
