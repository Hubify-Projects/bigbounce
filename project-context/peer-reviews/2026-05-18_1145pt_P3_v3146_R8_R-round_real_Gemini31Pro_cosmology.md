# P3_v3146_R8 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1145pt
**Wall time**: 165.2s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=62406, completion=15777, reasoning=14524, total=78183

---

## PAPER-GEM-B1: Fisher Information Positivity Violation for $\alpha < 0$
**Classification:** BLOCKER
**Location:** Section 5 (Cosmological Applications)

**Issue:** The linear scaling $\sigma(f_{\rm NL}) = 8.98 - 3.66\alpha$ is physically invalid for $\alpha < 0$. In a multi-tracer Fisher forecast, information scales with the bias difference $(b_1-b_2)^2 \propto \alpha^2$. Adding a tracer with a different bias (e.g., $\alpha = -1.08$) increases sample variance cancellation, which must *decrease* $\sigma(f_{\rm NL})$. The linear formula incorrectly predicts $\sigma(f_{\rm NL}) = 12.95 > 8.98$, violating the fundamental theorem that adding data cannot degrade an unmarginalized constraint. 

**Fix:** Replace the linear scaling with the exact $\sigma(f_{\rm NL}) \propto 1/\sqrt{F_{\rm base} + c\alpha^2}$ relation, which correctly bounds $\sigma(f_{\rm NL}) \le 8.98$ for all $\alpha \neq 0$.

## PAPER-GEM-B2: Negative Fisher Forecast Error Bar
**Classification:** BLOCKER
**Location:** Section 5 (Cosmological Applications)

**Issue:** The high-confidence subset forecast is reported as $\sigma(f_{\rm NL})^{\rm GS} = 2.28 \pm 7.43$. This implies a $1\sigma$ lower bound of $-5.15$ for the Fisher forecast error. A covariance matrix must be positive definite; an error bar cannot be negative. This mathematical impossibility occurs because linear error propagation ($\sigma_{\sigma} = |-3.66| \times 2.03$) breaks down catastrophically when the uncertainty on $\alpha$ is large enough to cross the $b=0$ pole.

**Fix:** Report the asymmetric confidence interval for $\sigma(f_{\rm NL})$ by mapping the $\alpha$ posterior through the exact non-linear Fisher matrix, and remove the mathematically invalid $\pm 7.43$ notation.

## PAPER-GEM-B3: 5-fold Jaccard Contradiction in Caveat (i)
**Classification:** BLOCKER
**Location:** Section 6.4, Caveat (i)

**Issue:** The text states each fold "scores the remaining 20% (9,400 held-out spectra)... where each spectrum is scored by a model that never saw it". It then immediately claims 399 objects appear in the top-1% of *all five folds*. If a spectrum is only scored in its one held-out fold, it can only appear in one fold's top-1% set, making an intersection of 5 mathematically impossible. (The text in Section 2.2 was fixed to state the full pool is scored, but Caveat (i) still contains the contradiction).

**Fix:** Update Section 6.4 Caveat (i) to match Section 2.2, explicitly stating the full 47,000-spectrum pool was scored by each fold's checkpoint to generate the overlap statistics.

## PAPER-GEM-M1: GR Projection Effects in Multi-Tracer
**Classification:** MAJOR
**Location:** Section 5 (Cosmological Applications)

**Issue:** The text claims GR projection effects "perfectly mimic local-PNG scale-dependent bias at large scales and must be deterministically subtracted... not marginalized over". This is false in a multi-tracer context. GR effects depend on magnification bias $s$ and evolution bias $b_e$, while $f_{\rm NL}$ depends on $(b-p)$. This distinct tracer dependence allows multi-tracer methods to break the degeneracy and marginalize over them.

**Fix:** Soften the claim. State that GR projection effects are degenerate with local PNG for a single tracer, but multi-tracer analysis can distinguish them via their different dependence on $s$ and $b_e$.

## PAPER-GEM-M2: Savage-Dickey Misapplication
**Classification:** MAJOR
**Location:** Section 5 and Appendix D'

**Issue:** The text states that comparing the matter-bounce ($\gamma=3.0$) and SMBHB ($\gamma=4.33$) fixed points requires "Savage-Dickey on the existing chain". The Savage-Dickey density ratio is used to compute Bayes factors for nested models (e.g., fixed $\gamma$ vs free $\gamma$). Comparing two fixed points in the same parameter space only requires the ratio of their marginal posterior densities.

**Fix:** Remove references to Savage-Dickey for this specific comparison; state that the Bayes factor between two fixed points is simply the ratio of their posterior densities.

## PAPER-GEM-m1: Sign Error in NANOGrav Free-Spectrum Template
**Classification:** minor
**Location:** Appendix D'

**Issue:** There is a sign error in the matter-bounce template formula: $\log_{10}\rho_i = \frac{1}{2}[\dots - \log_{10}T_{\rm obs}]$. Because the NANOGrav free spectrum parameter $\rho_i$ relates to the PSD via $\rho_i^2 = S(f_i) T_{\rm obs}$, the correct logarithmic expansion is $\log_{10}\rho_i = \frac{1}{2}[\log_{10}S(f_i) + \log_{10}T_{\rm obs}]$. The minus sign is analytically incorrect (though likely a text typo given the accurate recovered amplitude).

**Fix:** Change $-\log_{10}T_{\rm obs}$ to $+\log_{10}T_{\rm obs}$ in the $\log_{10}\rho_i$ equation.
