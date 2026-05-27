# P3 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-27_R-ext-maint-v2_P3_v3_1_63
**Wall time**: 123.1s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=70874, completion=11954, reasoning=11345, total=82828

---

I have reviewed the manuscript with a specific focus on theoretical cosmology, gauge-frame distinctions, EFT consistency, and Fisher matrix limits. 

**I found NO BLOCKER or MAJOR grade issues.** The physics is exceptionally rigorous. The handling of GR projection effects as gauge-invariant theoretical contamination, the exact multi-tracer Fisher saturation limits, and the matter-bounce SIGW spectral index ($\gamma=3.0$ from $n_T=2$) are all theoretically sound and correctly scoped. 

Below are three minor/nit findings for final polish.

## PAPER-GEM-N1 (nit)
**Section:** 5 (Cosmological Applications)
**Issue:** Arithmetic rounding error in the linear error propagation. The text states: `|-3.66| \cdot 0.65 = 2.379`, rounded to `\pm 2.37`. Standard rounding of 2.379 to two decimal places is 2.38.
**Fix:** Change "rounded to $\pm 2.37$" to "rounded to $\pm 2.38$" (and update the legacy symmetric text references if strict consistency is desired, though the asymmetric bounds are correctly identified as canonical).

## PAPER-GEM-m1 (minor)
**Section:** 5.1 (NANOGrav Bounce Consistency) & 6.4 (d)
**Issue:** The text refers to a "two-axis marginalized model-comparison (Savage-Dickey on the existing chain)" for testing the matter bounce. Because the matter bounce model only fixes one parameter ($\gamma=3.0$) while leaving the amplitude $A$ free, the Savage-Dickey density ratio is strictly a 1D evaluation on the marginal $\gamma$ posterior. The marginalization over the second axis ($A$) is already implicit in the 1D $\gamma$ chain.
**Fix:** Change "two-axis marginalized model-comparison (Savage-Dickey...)" to "fully marginalized model-comparison (1D Savage-Dickey on the amplitude-marginalized chain...)".

## PAPER-GEM-N2 (nit)
**Section:** 6.4 caveat (i)
**Issue:** The text states "the exact multi-tracer Fisher information... scales as $\sigfnl^{-2} \propto \alpha^2/[(1+\alpha)^2/n_{\rm main} + 1/n_{\rm anom}]$". This formula represents the multi-tracer *gain* (the cross-power covariance contribution), not the *total* Fisher information. If it were the total information, $\sigfnl^{-2}$ would vanish at $\alpha=0$ rather than returning the single-tracer floor $F_0$.
**Fix:** Change "the exact multi-tracer Fisher information for two tracers" to "the exact multi-tracer Fisher information gain for two tracers".
