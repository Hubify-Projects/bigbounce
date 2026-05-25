# P3 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-25_R-ext_P3_v3_1_62
**Wall time**: 84.4s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=69946, completion=10293, reasoning=9409, total=80239

---

## PAPER-GEM-B1 [BLOCKER]
**Location:** Section 5.1 & Appendix D'
**Issue:** The paper fits a $\gamma=3.0$ ($\Omega_{\rm GW} \propto f^2$) matter-bounce GWB to NANOGrav at $A \sim 10^{-14}$. A blue-tilted spectrum anchored at $\Omega_{\rm GW}(f_{\rm yr}) \sim 10^{-9}$ will grow to $\Omega_{\rm GW} \sim 10^{11}$ at BBN/LIGO scales unless a sharp UV cutoff mechanism is invoked, violently violating the $\Delta N_{\rm eff}$ bound ($\Omega_{\rm GW} \lesssim 10^{-5}$). Claiming consistency with NANOGrav without checking the BBN UV-completion boundary is a fatal theoretical omission.
**Fix:** Compute the integrated $\Omega_{\rm GW}$ up to the BBN scale; either explicitly specify the physical UV cutoff scale required in the matter-bounce EFT or retract the $\gamma=3.0$ viability claim.

## PAPER-GEM-B2 [BLOCKER]
**Location:** Section 5 (Cosmological Applications)
**Issue:** The empirical bias enhancement $\alpha$ is measured internally between anomaly subsets ($b_{\rm QSO\_cand}/b_{\rm full\_anomaly} - 1$), but is plugged directly into a Fisher forecast that defines $\alpha$ as the enhancement over the *external* standard DESI QSO baseline. This reference-frame mismatch mathematically invalidates the $\sigma(f_{\rm NL}) = 8.14$ forecast.
**Fix:** Recompute the empirical $\alpha$ by cross-correlating the anomaly tracers directly against the standard DESI DR1 QSO catalog, or explicitly rescale the internal bias ratio by the measured bias of the full anomaly pool relative to DESI QSOs.

## PAPER-GEM-M1 [MAJOR]
**Location:** Section 5 & Section 6.4 caveat (i)/(j)
**Issue:** The Fisher-positivity-respecting form $1/\sigma^2 = F_0 + c\alpha^2$ assumes the multi-tracer information is symmetric in $\alpha$. This is only true for $\alpha \ll 1$; at large $\alpha$ (e.g., the $\alpha=3.86$ upper bound), the sample variance denominator scales as $(1+\alpha)^2$, heavily breaking the $\alpha \leftrightarrow -\alpha$ symmetry and suppressing the information gain. The $c\alpha^2$ approximation catastrophically overestimates the constraint at large $\alpha$.
**Fix:** Discard the $F_0 + c\alpha^2$ approximation for the high-confidence subset; evaluate the exact multi-tracer Fisher matrix at the bounds of the $\alpha$ confidence interval.

## PAPER-GEM-M2 [MAJOR]
**Location:** Section 5 (Cosmological Applications)
**Issue:** The text asserts GR projection effects (Doppler, Sachs-Wolfe) "must be deterministically subtracted from the template, not marginalized over." While the theoretical terms are deterministic, their amplitudes depend on the tracer's magnification bias $s$ and evolution bias $b_e$, whose empirical uncertainties must be marginalized over to prevent artificially tight $f_{\rm NL}$ posteriors.
**Fix:** Correct the text to state that while the GR projection terms must be deterministically included in the template, the uncertainties in the coupling coefficients ($s$, $b_e$) must be marginalized over.

## PAPER-GEM-m1 [minor]
**Location:** Section 5.1 & Appendix D'
**Issue:** The paper defers a "Savage-Dickey" computation to compare the $\gamma=3.0$ and $\gamma=4.33$ models. The Savage-Dickey density ratio applies exclusively to nested models (evaluating a marginal posterior at a specific parameter value relative to its prior); comparing two disjoint fixed parameter values requires a standard Bayes factor or posterior density ratio, not Savage-Dickey.
**Fix:** Remove the term "Savage-Dickey" and refer simply to a marginalized Bayes factor or posterior odds ratio.
