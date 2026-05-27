# P3 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v63verify-v2_P3_v3_1_63
**Wall time**: 94.9s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=70912, completion=10235, reasoning=9615, total=81147

---

This paper is PERFECTLY CLEAN on core theoretical physics, gauge-frame distinctions, model-class boundaries, and Fisher formalism. The previous blockers regarding Fisher positivity and matter-bounce predictions have been resolved with high fidelity. I found NO BLOCKER or MAJOR issues. 

Below are three minor/nit findings regarding statistical reporting and arithmetic rounding.

## PAPER-GEM-m1 (minor): NANOGrav MCMC 68% CI vs standard deviation inconsistency
**Location:** Section 5.1 and Appendix D'
**Issue:** The reported NANOGrav spectral index is $\gamma = 2.567 \pm 0.382$, but the 68% CI is reported as $[2.304, 2.882]$. The width of this CI is $0.578$, which implies a $1\sigma$ error of $\approx 0.289$, significantly smaller than the quoted standard deviation of $0.382$. If the true $1\sigma$ error is $0.289$, the matter-bounce $\Delta\chi^2$ significance shifts from $1.13\sigma$ to $\approx 1.50\sigma$.
**Fix:** Verify the MCMC summary statistic script. Ensure the quoted $\pm$ value is either the standard deviation or the symmetrized 68% CI half-width, and make them consistent.

## PAPER-GEM-n1 (nit): Arithmetic truncation of 2.379
**Location:** Section 5
**Issue:** The text states: "linear error propagation: $\sigma_{\sigfnl} = |-3.66| \cdot 0.65 = 2.379$, rounded to $\pm 2.37$". Rounding $2.379$ to two decimal places yields $2.38$, not $2.37$.
**Fix:** Change "rounded to $\pm 2.37$" to "truncated to $\pm 2.37$" or update the value to $2.38$ throughout the text.

## PAPER-GEM-n2 (nit): Fisher positivity $\alpha=-1.084$ calculation rounding
**Location:** Section 6.4, Caveat (i)
**Issue:** The text states that using $(F_0, c) = (1/80.64, 0.0747)$ gives $\sigfnl(\alpha\!=\!-1.084) = 3.17$. However, $1/\sqrt{1/80.64 + 0.0747(-1.084)^2} = 3.159 \approx 3.16$.
**Fix:** Change $3.17$ to $3.16$ to match the exact arithmetic of the stated constants.
