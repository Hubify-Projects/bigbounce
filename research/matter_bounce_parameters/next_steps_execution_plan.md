# Next Steps Execution Plan

**Date:** 2026-03-23
**Pod:** kqo1b4e4igycra (active, Planck maps + PolySpec ready)

---

## TIER 1 — HIGH PRIORITY (blocks paper claims)

### 1A. Combined-Integrand f_NL Computation (closes ε correction)

**What:** Evaluate ALL 4 cubic action vertices simultaneously with numerically-computed mode functions, preserving the cancellations that make the physical bispectrum finite.

**Why it's hard:** Individual vertex integrals diverge (~10⁹). The physical f_NL (~4) emerges from near-perfect cancellation. Numerical precision must be sufficient to recover a number that is ~10⁸ smaller than the individual terms.

**Method:**
1. Use the ODE-solved mode functions (already working)
2. Implement Cai's FULL cubic action (Eq. 15) — all 4 terms + field redefinition
3. Sum ALL vertex integrands at each time step BEFORE integrating (combined integrand approach)
4. Integrate the combined integrand from early time to bounce
5. Do this for ε = 3/2 first (must reproduce -35/8 or -35/16)
6. Then scan ε ∈ [1.48, 1.52] to get the exact correction

**Critical requirement:** Must use Cai's cosmic-time mode functions (e^{+ikη} phase), not the conformal-time Maldacena reconstruction that caused the 3 errors in the original attempt.

**Compute:** RunPod CPU pod. mpmath for high precision. ~2-4 hours for a full ε scan.

**Success criteria:** Reproduces the correct Cai benchmark values at ε = 3/2. Gives a smooth f_NL(ε) curve with error bars from convergence testing.

**Failure mode:** If the combined integrand still doesn't converge, the cancellation is too delicate for direct numerical evaluation. Fallback: the bounded range [1-8%] stands.

### 1B. Verify Cai Eq. 37 Polynomial from TeX Source

**What:** Resolve the discrepancy between Cai's TeX coefficients (3,1,-9,5,-66,9) and our benchmark-fitting coefficients (2,7,3,-12,-69,19). The TeX coefficients don't reproduce the benchmarks.

**Why this matters:** If we can't read Eq. 37 correctly, the template overlap r has a polynomial systematic we can't bound.

**Method:**
1. Check sum conventions in the TeX: does Σ_{i≠j≠k} mean all-distinct (6 terms) or i≠j AND j≠k (12 terms)?
2. Evaluate Cai's Eq. 37 with BOTH interpretations
3. If one matches the benchmarks, we have the actual coefficients
4. Cross-check against Eqs. 34-36 with ε = 3/2

**Compute:** Local. Pure algebra/numerics.

### 1C. Contact Yi-Fu Cai

**What:** Email Cai to confirm (a) the commutator interpretation and (b) the exact Eq. 37 coefficients.

**Why:** Fastest path to 100% closure. Cai is co-author on both papers.

**Method:** Draft a brief professional email explaining our audit findings and asking two specific questions.

**Compute:** None.

---

## TIER 2 — HIGH PRIORITY (strengthens current-data case)

### 2A. F3.3 — EB Injection Recovery (RunPod)

**What:** Inject known polarization rotation signals into Planck-like simulations and verify our EB estimator recovers them correctly.

**Method:**
1. Generate Gaussian CMB simulations (Q, U maps) using CAMB Cℓ + healpy
2. Inject known rotation β by transforming Q+iU → (Q+iU)e^{2iβ}
3. Run our EB estimator on the rotated maps
4. Verify recovered β matches injected β within calibration tolerance
5. Test at β = 0° (null), 0.1°, 0.27° (our prediction), 0.5°, 1.0°

**Compute:** RunPod CPU pod. ~2 hours for 100 simulations × 5 injection levels.

**Success criteria:** Recovered β within 10% of injected β for all levels. Null injection gives β consistent with zero.

### 2B. F3.5 — EB Frequency Robustness (RunPod)

**What:** Run the EB estimator on individual Planck frequency maps (100, 143, 217 GHz) to test whether the signal is frequency-consistent (as expected for cosmological birefringence) or frequency-dependent (suggesting foreground contamination).

**Data needed:** Planck HFI frequency maps (download to pod, ~2 GB each)

**Method:**
1. Download 100/143/217 GHz maps
2. Run EB analysis on each frequency separately
3. Compare β estimates across frequencies
4. A cosmological signal should be frequency-independent

**Compute:** RunPod CPU pod. ~4 hours for download + analysis.

### 2C. F3 NaMaster Upgrade

**What:** Replace the naive pseudo-Cℓ with NaMaster's purified estimator for better E/B separation.

**Why:** Our current β = 0.167° uses naive fsky correction. NaMaster provides proper E/B purification and mask deconvolution, which could change the estimate.

**Compute:** RunPod CPU pod. NaMaster already installed. ~1 hour.

---

## TIER 3 — MEDIUM PRIORITY (extends empirical case)

### 3A. F1.3 — Bispectrum Injection/Recovery

**What:** Generate Gaussian CMB simulations with known f_NL injection and test whether our recast methodology correctly recovers the amplitude.

**Method:**
1. Generate Gaussian CMB realizations from CAMB Cℓ (no f_NL)
2. Add local-type non-Gaussianity using the standard ζ = ζ_G + (3/5)f_NL ζ_G² prescription
3. Run healpy anafast to get power spectrum + simple bispectrum proxy
4. Verify that the recast methodology (r × f_NL / σ) correctly predicts the recovered amplitude

**Limitation:** Without the full Planck bispectrum estimator, this is a surrogate validation, not a true estimator-level test.

**Compute:** Local or RunPod CPU. ~2 hours.

### 3B. F2.1 — DESI Catalog Acquisition

**What:** Download DESI DR1 spectroscopic catalog and build the baseline QSO tracer sample.

**Data:** DESI DR1 from data.desi.lbl.gov. ~5 GB for QSO catalog.

**Method:**
1. Download QSO target files
2. Apply quality cuts (ZWARN, DELTACHI2)
3. Compute n(z), sky coverage, contamination estimates
4. Estimate baseline PNG sensitivity from Fisher formula

**Compute:** RunPod CPU pod (for download bandwidth). ~3 hours.

### 3C. PolySpec Fisher Template Overlap (more rigorous)

**What:** Use PolySpec's internal Fisher matrix machinery to compute the template overlap more rigorously than our simplified Fisher calculation.

**Method:**
1. Re-clone PolySpec on the pod
2. Set up fiducial Cℓ from CAMB
3. Implement the bounce template as a custom shape in PolySpec's framework
4. Compute Fisher information for both local and bounce templates
5. Extract the rigorous overlap factor

**Compute:** RunPod CPU pod. ~4 hours including setup.

---

## TIER 4 — LOWER PRIORITY (paper polish + extended analysis)

### 4A. Generate Publication Figures

**What:** Produce final paper-quality figures incorporating all revised numbers:
- Shape function with ε-correction uncertainty band
- Template overlap with ℓ-space validation overlaid
- Forecast comparison with honest uncertainty ranges
- EB power spectrum from Planck SMICA

### 4B. Claim Hygiene Audit

**What:** After Tier 1-2 work is complete, do a final pass across all pages and papers to ensure every number is consistent with the validated results.

### 4C. F2.2+ — Enhanced Tracer Pipeline

**What:** Build the ML-enhanced tracer selection pipeline for PNG. This is the longest-lead-time item and depends on DESI catalog acquisition (3B).

---

## Execution Calendar

| Session | Tasks | Pod needed? |
|---------|-------|-------------|
| Next | 1A (combined integrand) + 1B (polynomial verify) | YES — RunPod CPU |
| Next | 2A (EB injection) + 2C (NaMaster upgrade) | YES — same pod |
| After | 1C (email Cai) + 3B (DESI download) | Email + RunPod |
| After | 2B (frequency robustness) + 3C (PolySpec Fisher) | RunPod |
| After | 3A (bispectrum injection) + 4A (figures) | Local + RunPod |
| Final | 4B (claim hygiene) + paper revision | Local |

---

## What Would Change If 1A Succeeds

If the combined-integrand computation reproduces -35/8 at ε = 3/2 AND gives a smooth f_NL(ε) curve:

1. **Normalization confidence → 98%+** (first independent numerical confirmation)
2. **ε correction → exact coefficient** (not a bounded range)
3. **Consistency relation → single value** (not a range)
4. **SPHEREx significance → precise number** (not a range)
5. **Paper upgrade:** "independently confirmed" replaces "supported by audit"

If it reproduces -35/16 instead:
1. The canonical value shifts to -35/16
2. All forecasts halve in significance
3. The paper still works — it just has a different canonical number
4. The template mismatch r is UNCHANGED (it's about the shape, not the amplitude)

If it fails to converge:
1. The bounded range [1-8%] stands
2. The paper quotes the range honestly
3. No worse than current state
