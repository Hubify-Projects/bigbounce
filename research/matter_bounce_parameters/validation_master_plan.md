# Validation Master Plan

**Date:** 2026-03-23
**Purpose:** Upgrade matter-bounce forecast claims from "strong and honest" to as close to bulletproof as possible.

---

## Current State Summary

We have 6 claims at varying evidence levels:

| # | Claim | Current grade | Target grade |
|---|-------|--------------|-------------|
| 1 | f_NL = -35/8 (Planck convention) | B (90% confidence) | A (independently confirmed) |
| 2 | Template mismatch r = 0.84 ± 0.02 | A- (robust but simplified) | A (estimator-validated) |
| 3 | SPHEREx ~5.5σ (template-corrected) | C+ (downstream) | B+ (direct forecast) |
| 4 | Normalization audit (vertex match) | B (strong internal) | A (numerically closed) |
| 5 | Consistency relation f_NL(n_s) | C (scaling estimate) | B (numerically validated) |
| 6 | Bayes factors ~8-17:1 | B (correct given inputs) | B+ (upstream claims upgraded) |

**Critical risk:** Our only independent numerical attempt gave the WRONG answer (+25/16). The errors were identified but the corrected computation was never run.

---

## PHASE 1: Independent Normalization Re-Derivation

### Priority: HIGHEST

### What we need to do

Correct the three identified errors in `fnl_combined_integrand/03_compute_combined_fnl_mpmath.py` and re-run the full in-in integral evaluation with high-precision arithmetic.

### Specific tasks

1. **Start from Cai's exact cubic action** (their Eq. 15), not from our previous incorrect reconstruction
2. **Use Cai's exact mode functions** (their Eq. 23-24), not conformal-time Maldacena forms
3. **Implement both in-in formulations:**
   - Commutator: i⟨[ζ³, L_int]⟩
   - Time-ordered: -2 Im⟨ζ³ L_int⟩ with explicit permutation factors
4. **Evaluate each of the 4 vertex contributions separately** at squeezed, equilateral, and folded
5. **Compare against Cai's published values** at each step
6. **Use mpmath 50+ digit precision** to avoid numerical artifacts

### What would make it bulletproof
- Both formulations (commutator and -2 Im) give the same A_T
- Each vertex matches Cai's Eqs. 28, 31, 32, 33 individually
- Total A_T matches Eq. 37
- Squeezed limit gives -(21/8)k³ → f_NL = -35/8
- Equilateral gives -255/64
- Folded gives -9/4

### GPU/RunPod needed?
**No.** This is high-precision symbolic/numerical integration (mpmath), not GPU-parallel computation. Can run locally. If integrals are slow, RunPod CPU pod is sufficient.

### Expected failure modes
- Mode function phase convention error (the #1 historical failure)
- Time-ordering vs commutator permutation factor mismatch
- Conformal time vs cosmic time integration variable confusion
- Superhorizon approximation giving different answer than exact integral

### Evidence grade on success: A (independently confirmed)
### Evidence grade on failure: The claim drops to C or D (serious problem)

---

## PHASE 2: General-ε Mode Functions and Consistency Relation

### Priority: HIGH

### What we need to do

Compute f_NL for general ε (not just ε = 3/2) by solving the mode equation with non-integer Hankel index and re-evaluating the cubic integrals.

### Specific tasks

1. **Solve the Mukhanov-Sasaki equation for general ε:**
   - a(η) ∝ |η|^{2/(2ε-1)}, giving mode function index ν = 1/2 + 2/(2ε-1)
   - For ε = 3/2: ν = 3/2 (elementary Hankel, simple polynomial × exponential)
   - For ε ≠ 3/2: ν is non-integer → Hankel functions H_ν^{(1,2)}

2. **Numerically evaluate the Cai integrals with Hankel mode functions:**
   - Use mpmath's besselj/bessely or hankel1/hankel2 for arbitrary ν
   - Compute each vertex integral as a function of ε
   - Extract f_NL(ε) over a grid: ε ∈ [1.48, 1.52]

3. **From the numerical f_NL(ε), extract:**
   - df_NL/dε at ε = 3/2 (the coefficient c₁)
   - Validity range of linear approximation
   - Whether f_NL(ε) is monotone, non-monotone, or has structure

4. **Convert to the consistency relation:**
   - ε = 3(1+w)/2, w = (n_s - 1)/12 at leading order
   - f_NL(n_s) = f_NL(3/2) + c₁ × (n_s - 1)/8

### GPU/RunPod needed?
**Likely yes** for the full numerical integration with Hankel functions, which involves oscillatory integrands and may need adaptive quadrature. A RunPod CPU pod with mpmath would be ideal. Not GPU — this is precision arithmetic, not parallelism.

### Expected failure modes
- Hankel function oscillatory integrals may not converge without careful contour deformation
- The cubic action coefficients themselves may depend on ε in ways not captured by the polynomial form
- The relationship between ε and the polynomial structure (degree-9 terms) may be more complex than linear

### Evidence grade on success: B+ (numerically validated, not full closed-form derivation)
### Evidence grade on failure: Current estimate stands at C (no worse, we already said "estimated")

---

## PHASE 3: Direct Template-Overlap Validation

### Priority: MEDIUM-HIGH

### What we need to do

Validate r = 0.84 using a more realistic bispectrum estimator framework, not just shape inner products.

### Specific tasks

1. **Check for public bispectrum estimator code:**
   - Planck bispectrum code (not public — the full pipeline is internal to ESA)
   - `PolyBin` (public Python binned bispectrum estimator by Philcox)
   - Modal estimator implementations
   - Any public local-template recovery pipeline

2. **If usable code exists:**
   - Inject the matter-bounce bispectrum (via the verified polynomial)
   - Run the local-template estimator on the injected signal
   - Measure recovered amplitude vs input amplitude
   - This gives the "real" r from an actual estimator

3. **If no usable code exists:**
   - Build a faithful surrogate:
     - Generate a set of ℓ-space bispectra b_{ℓ₁ℓ₂ℓ₃} from the k-space shape
     - Apply the KSW-like optimal estimator with CMB C_ℓ weighting
     - Compute recovery factor
   - Document exactly how this differs from Planck pipeline

4. **Cross-validate against our current result:**
   - Does the estimator-level r agree with the shape-inner-product r?
   - If they disagree, which is more relevant for forecasting?

### GPU/RunPod needed?
**Possibly** — if we build a full ℓ-space estimator, the bispectrum sums can be large (ℓ_max ~ 2000 means ~10⁹ triangles). A CPU pod with parallelization would help. Not GPU.

### Expected failure modes
- ℓ-space projection (Gaunt integrals) may change the effective overlap
- The CMB transfer function modifies the k-space shape before it reaches the estimator
- Real estimators include noise, masking, and foreground marginalization that affect r

### Evidence grade on success: A (estimator-validated)
### Evidence grade on failure: Current A- stands (simplified but robust internal result)

---

## PHASE 4: Direct Forecast Upgrade

### Priority: MEDIUM

### What we need to do

Move beyond σ_bounce = σ_local / r arithmetic toward a direct bounce-template Fisher forecast.

### Specific tasks

1. **Compute the signal-to-noise for the bounce template directly:**
   - (S/N)² = Σ B_bounce² / (C_{ℓ1} C_{ℓ2} C_{ℓ3})
   - Compare this to the local-template (S/N)²
   - The ratio gives a more rigorous σ_bounce

2. **Use Heinrich et al. (2023) SPHEREx specifications:**
   - Galaxy number density n(z)
   - Bias b(z)
   - Survey volume
   - ℓ-range or k-range

3. **Compute both:**
   - Local-template Fisher σ (should match their 0.7)
   - Bounce-template Fisher σ (the new result)

### GPU/RunPod needed?
**No** for the Fisher matrix computation itself (it's a sum, not an MCMC). If the sum over triangles is large, a CPU pod helps but is not essential.

### Expected failure modes
- We may not have the exact survey specifications to reproduce Heinrich et al.
- The bounce-template Fisher may require different survey-window assumptions
- If we can't reproduce σ = 0.7 for the local template, the bounce-template result is unreliable

### Evidence grade on success: B+ (direct forecast with controlled assumptions)
### Evidence grade if limited: C+ remains (downstream of inherited forecast)

---

## PHASE 5: Claim Hygiene

### Priority: AFTER PHASES 1-4

### What to do
- Re-grade every claim based on Phase 1-4 outcomes
- Draft exact paper and website patch recommendations
- Do NOT edit until patches are reviewed

---

## Execution Priority

```
PHASE 1 (normalization)  ←← START HERE, blocks everything else
  ↓
PHASE 2 (general ε)      can start in parallel if Phase 1 is clean
  ↓
PHASE 3 (estimator r)    independent of Phase 2
  ↓
PHASE 4 (direct forecast) needs Phases 1 + 3
  ↓
PHASE 5 (claim hygiene)   after all above
```

### Realistic timeline
- Phase 1: 1-2 sessions (local computation, mpmath)
- Phase 2: 1-2 sessions (may need RunPod for Hankel integrals)
- Phase 3: 1-3 sessions (depends on public estimator availability)
- Phase 4: 1 session (Fisher matrix computation)
- Phase 5: 1 session (editing)

### What happens if Phase 1 FAILS
If the independent re-derivation does NOT reproduce -35/8:
- f_NL claim drops to grade C or D
- Template mismatch r is still valid (it's about the shape, independent of the amplitude)
- SPHEREx significance becomes uncertain
- Paper 2 would need major revision or withdrawal of the specific prediction
- The honest path: publish the shape characterization + template mismatch as the primary contribution, with the normalization as a clearly flagged open question

This is why Phase 1 is the absolute priority.
