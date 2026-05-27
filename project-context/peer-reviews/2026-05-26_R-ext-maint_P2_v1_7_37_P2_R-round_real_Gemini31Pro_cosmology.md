# P2 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-maint_P2_v1_7_37
**Wall time**: 105.4s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=33211, completion=8722, reasoning=7749, total=41933

---

## PAPER-GEM-B1
**Classification:** BLOCKER
**Section:** Abstract & Section 10 (Conclusion)
**Issue:** The paper claims LSS surveys (SPHEREx, MegaMapper) measure the "gauge-frame" $\fnl$ and not the physical CFC quantity. This violates the equivalence principle; telescopes measure physical, gauge-invariant quantities on the past lightcone. The scale-dependent bias vanishes in single-field slow-roll precisely because the physical squeezed limit vanishes (modulo standard GR projection effects). Claiming LSS measures a gauge-dependent theoretical artifact is a fundamental error.
**Fix:** Correct the text to state that LSS measures the physical frame, making the physical vanishing of single-field slow-roll $\fnl$ the actual observational baseline against which the bounce's physical $\fnl \approx -4.375$ is distinguished.

## PAPER-GEM-B2
**Classification:** BLOCKER
**Section:** 9.4 (Joint Forecast / QSFI discrimination)
**Issue:** The QSFI scaling dimension limits are completely inverted. The text claims $\mu/H = 0$ gives a "super-squeezed" divergent shape and $\mu/H = 3/2$ gives the local template. Standard QSFI theory establishes the exact opposite: the massless limit $\mu/H \to 0$ recovers the local shape, while $\mu/H \to 3/2$ suppresses the squeezed limit by $(k_3/k_1)^{3/2}$. 
**Fix:** Swap the QSFI mass limits: state that $\mu/H \to 0$ gives the local shape, and $\mu/H \to 3/2$ gives the suppressed scaling.

## PAPER-GEM-M1
**Classification:** MAJOR
**Section:** 9.5 (Caveats)
**Issue:** The text refers to "the bounce prediction $\beta = 0.27^\circ$" for cosmic birefringence. The matter bounce does not theoretically predict this specific angle; $0.27^\circ$ is simply the central value of the Eskilt & Komatsu 2022 observational fit. Presenting a post-dictive parameter accommodation of a specific experimental dataset as a theoretical prediction is a severe misrepresentation.
**Fix:** Change "the bounce prediction $\beta = 0.27^\circ$" to "bounce-motivated ALPs can accommodate the observed $\beta \approx 0.27^\circ$".

## PAPER-GEM-M2
**Classification:** MAJOR
**Section:** Appendix A.1
**Issue:** The paper accuses Li & Brandenberger (2014) of missing the second time-ordering (the $-2\text{Im}$ commutator doubling) in the in-in formalism. This is factually incorrect; L&B 2014 Eq. 3.12 explicitly includes the full commutator. Their factor-of-two difference stems from permutation counting and $B_\zeta$ normalization conventions, not a failure to include the Hermitian conjugate in the QFT integral.
**Fix:** Remove the claim that L&B computed only the single time-ordered correlator; attribute the discrepancy strictly to the Komatsu-Spergel $c=1$ vs $c=2$ normalization convention.

## PAPER-GEM-m1
**Classification:** minor
**Section:** 1 & 2.3
**Issue:** The paper repeatedly claims the $\fnl = -35/8$ prediction is "mechanism-independent", but explicitly restricts it to the "scalar-only matter-bounce class" with "no prolonged post-bounce inflation". This is a highly specific, mechanism-dependent UV-completion routing.
**Fix:** Replace "mechanism-independent" with "UV-completion insensitive within the scalar-only Wilson-Ewing class" to avoid overstating the generality of the prediction.

## PAPER-GEM-n1
**Classification:** nit
**Section:** 9.4
**Issue:** The idealized joint Fisher forecast implies an unmarginalized $\sigma_{\rm unmarg}(\fnl) \approx 0.114$ for SPHEREx SDB. This is unrealistically tight (roughly an order of magnitude better than standard literature) and implies the 6-bin Fisher matrix lacks realistic cross-bin covariance or assumes perfectly modeled ultra-large-scale modes.
**Fix:** Add a half-sentence caveat that the $\sigma_{\rm unmarg} \approx 0.114$ value assumes zero cross-bin covariance and idealized $k_{\rm min}$ access.
