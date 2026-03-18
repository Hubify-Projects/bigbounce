# Cross-Check: Gemini Deep Think f_NL Analysis (2026-03-17)

**Purpose:** Integrate useful results from Gemini's analysis, flag errors and unsubstantiated claims.

---

## Result 1: Quasi-Dust Epsilon Shift — CONFIRMED USEFUL

The w = -0.003 equation of state (required for n_s = 0.964) shifts epsilon from 1.500 to 1.4955, a 0.3% change.

If f_NL scales roughly with epsilon (or with powers of epsilon appearing in the cubic action vertices), this produces a shift:

$$
f_{\rm NL}(w = -0.003) \approx -4.375 \times (1 - 0.003) = -4.362
$$

The shift is 0.013 in absolute terms — negligible against MegaMapper's sigma ~ 0.5.

**Conclusion:** The quasi-dust EOS does NOT damage the f_NL prediction. The red tilt and the non-Gaussianity are compatible.

**Caveat:** The actual f_NL dependence on w may be more complex than linear in epsilon. The full calculation at w = -0.003 would involve modified mode functions (v_k equation with nu != 3/2) and modified cubic action vertices. But for |w| = 0.003, all corrections are O(w) ~ O(0.003), confirming negligibility.

---

## Result 2: Factor-of-2 is Systematic, Not Approximation — IMPORTANT UPGRADE

The algebra reveals:

Li & Brandenberger (2016): f_NL ~ -165/16 + 65/8 = -165/16 + 130/16 = **-35/16**

The numerator 35 is preserved through the near-cancellation of the two terms. This means:
- The discrepancy is NOT an approximation artifact (approximation errors don't preserve algebraic structure)
- The discrepancy IS a systematic factor of exactly 2
- Somewhere in the normalization chain, one calculation carries a factor of 2 that the other does not

**This upgrades our working hypothesis from file 03.** Previously: "Li-Brandenberger is approximate at c_s = 1." Now: "There is a systematic factor-of-2 convention or normalization difference."

The factor of 2 could sit in:
1. The f_NL definition (3/5 factor present vs absent)
2. The bispectrum normalization (|B|_NL vs standard B_zeta)
3. A symmetry factor in the cubic action or in-in integral
4. The mode function normalization

Our derivation (Paths A and B) will identify the location by computing B_zeta directly and applying the locked extraction formula (file 02).

---

## Gemini Claims Flagged as WRONG or UNSUBSTANTIATED

### Claim: "Dropped 1/2 symmetry factor in Wick contractions" — UNSUBSTANTIATED

Gemini asserts this is confirmed but provides zero algebra. The SymPy code only computes the epsilon shift, not Wick contractions. The specific mechanism for the factor of 2 is unknown until our derivation identifies it.

### Claim: "13 structural barriers" — WRONG

Our work cataloged 7 barriers across Foundations A-G (one per foundation). The number 13 does not appear in our analysis.

### Claim: Recommending "Salopek-Bond derivation" — WRONG (CRITICAL)

Our file 04 (derivation_path_A.md) discovered that the fluid-based Salopek-Bond / delta-N approach does NOT capture the growing mode of zeta. The growing mode is a scalar-field mode from phase perturbations of the oscillating field. The standard Salopek-Bond formalism gives zeta = constant on superhorizon scales, missing the growing mode entirely.

This is exactly the error that produced f_NL = 5/12 in our earlier branch_V work.

**Path A must use the scalar-field separate-universe approach, not fluid Salopek-Bond.**

### Claim: "LQC guarantees f_NL survives intact through the bounce" — UNSUBSTANTIATED

Our fnl_foundation_check identifies "bounce transfer at third order" as one of two unresolved failure points. Whether f_NL survives the LQC bounce is an open research question — the computation has not been done.

### Claim: "The f_NL integral diverges violently as a -> 0" — MISLEADING

The f_NL calculation is performed in the pre-bounce phase. The relevant behavior is the growing mode of zeta as eta -> 0^- (conformal time approaching the bounce), which causes the bispectrum integrand to grow. This is cut off by the bounce, not by a UV divergence. The issue is WHAT HAPPENS AT the bounce, not that the integral is ill-defined.

---

## Net Assessment

| Gemini Finding | Verdict | Impact on Our Program |
|---------------|---------|----------------------|
| w = -0.003 shift is 0.3% | CORRECT | Closes a vulnerability — quasi-dust is safe |
| Factor-of-2 is systematic | CORRECT (improved) | Upgrades our understanding of the discrepancy |
| "Dropped symmetry factor" | UNSUBSTANTIATED | Does not change our derivation plan |
| "13 barriers" | WRONG (should be 7) | Cosmetic error, no physics impact |
| Use Salopek-Bond | WRONG | Would repeat our branch_V error |
| LQC preserves f_NL | UNSUBSTANTIATED | Remains an open question |
| f_NL integral diverges | MISLEADING | Mischaracterizes the physics |

**Bottom line:** Two useful results (quasi-dust safety, systematic factor-of-2). Five errors or unsubstantiated claims. The derivation program (files 01-10) is unchanged — the Gemini analysis does not alter our execution plan.
