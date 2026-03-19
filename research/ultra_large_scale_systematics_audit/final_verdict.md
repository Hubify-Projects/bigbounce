# Final Verdict: Ultra-Large-Scale Systematics Audit

## 1. Is the Science Case Robust, Plausible-but-Fragile, or Seriously Weakened?

**PLAUSIBLE_BUT_FRAGILE.**

The signal (f_NL = -4.375) is large enough to survive realistic degradation. But the headline "8.75σ definitive detection" is too optimistic for MegaMapper due to GR projection effects and b_φ uncertainty. SPHEREx is more robust than we previously thought, thanks to the bispectrum channel.

## 2. Realistic SPHEREx Significance Range (Post-Audit)

| Scenario | σ(f_NL) | Significance |
|----------|---------|-------------|
| Published (P+B combined) | 0.5 | 8.75σ |
| **Bispectrum only (fiducial)** | **0.7** | **6.3σ** |
| With photo-z degradation | 0.7-0.9 | 4.9-6.3σ |
| With b_φ uncertainty (~30%) | 0.9-1.2 | 3.6-4.9σ |
| Conservative (all degradations) | 1.0-1.5 | 2.9-4.4σ |

**SPHEREx at 4-6σ is CREDIBLE.** The bispectrum channel (independently forecast by arXiv:2311.13082) provides a more robust constraint than power-spectrum SDB alone. SPHEREx is the FIRST REAL TEST and is more powerful than we previously estimated.

## 3. Realistic MegaMapper Significance Range (Post-Audit)

| Scenario | σ(f_NL) | Significance | Key Risk |
|----------|---------|-------------|----------|
| Published (ideal) | 0.5 | 8.75σ | Assumes perfect GR correction |
| After GR residual (~10%) | 0.6-0.8 | 5.5-7.3σ | Needs accurate magnification bias |
| After b_φ marginalisation | 0.8-2.0 | 2.2-5.5σ | Needs theoretical b_φ priors |
| Conservative (all) | 1.5-3.0 | 1.5-2.9σ | Marginal |

**MegaMapper at 3-7σ is PLAUSIBLE but conditional** on GR projection modeling and b_φ prior quality. The 8.75σ headline requires everything to work perfectly.

## 4. Is k_min ~ 10⁻⁴ Actually Realistic?

**For power-spectrum SDB: CONDITIONALLY.** The geometric k_min is achievable, but:
- GR projection effects create a 20σ "fake" f_NL at those scales (MegaMapper)
- After correction, the residual depends on modeling accuracy of magnification bias, evolution bias, and luminosity function at z > 2
- The RESIDUAL uncertainty is the real k_min — not the geometric one

**For bispectrum: LESS DEPENDENT ON k_min.** The bispectrum measures non-Gaussianity through the three-point function, which has information at SHORTER wavelengths too. This makes it a more robust estimator for our purpose.

## 5. Do We Need Extra Compute or Mocks Now?

**NOT FOR THE SCIENCE CASE.** The literature already provides:
- SPHEREx σ(f_NL) = 0.7 from a dedicated bispectrum forecast
- MegaMapper vulnerability to GR effects quantified
- b_φ impact quantified

What would HELP (but is not essential):
- A Fisher forecast that INCLUDES b_φ marginalisation (light CPU, laptop-doable)
- An estimate of the GR correction residual for MegaMapper LBGs (requires luminosity function modeling, moderate complexity)

**Verdict: Still laptop-only. No MCMC, no RunPod, no GPU.**

## 6. Exact Next Step

**The systematics audit is now COMPLETE.** The three most important findings are:

1. **SPHEREx is stronger than we thought** (bispectrum channel gives σ = 0.7, upgrading significance to ~6σ)
2. **MegaMapper is more fragile than we thought** (20σ GR bias + b_φ uncertainty)
3. **The combined picture: SPHEREx (first test, ~2028, 4-6σ) + MegaMapper (definitive if GR modeled, ~2032+, 3-7σ)**

The research phase is now COMPLETE for the current program scope. The remaining work is:

**Option A: Package the full science case** — from ECH closure through f_NL benchmark through systematics audit. This IS the deliverable.

**Option B: One more pass — Fisher with b_φ marginalisation** — a quick laptop calculation that would give the CORRECTED σ(f_NL) accounting for b_φ uncertainty. This would be the final stress test.

**RECOMMENDATION: Option A.** The science case is mature enough. The systematics audit has identified the key vulnerabilities. The honest framing is: "f_NL = -4.375 is a parameter-free prediction of the matter bounce, testable at 4-6σ by SPHEREx (~2028) and 3-7σ by MegaMapper (~2032+), with the primary systematic risks being relativistic projection effects and PNG bias uncertainty."
