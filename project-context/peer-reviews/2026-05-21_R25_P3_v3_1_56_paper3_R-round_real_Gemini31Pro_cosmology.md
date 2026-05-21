# paper3 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-21_R25_P3_v3_1_56
**Wall time**: 144.1s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=68590, completion=15069, reasoning=14099, total=83659

---

## PAPER-GEM-B1: BLOCKER - Fisher Matrix Nuisance Parameter Definition Destroys $f_{NL}$ Signal
**Location:** Section 5, paragraph 2 ("including a $4n+1$-dimensional nuisance-parameter block per active tracer at each (k, z) cell...")
**Issue:** Defining the linear bias nuisance parameter $\delta b_i$ "at each $(k,z)$ cell" is a catastrophic theoretical error in EFT/bias expansion. If linear bias is a free parameter in every $k$-bin, it perfectly degenerates with the $1/k^2$ scale-dependent bias of $f_{NL}$, driving the Fisher information to zero; bias parameters are Wilson coefficients that depend on redshift, not scale.
**Fix:** Change the Fisher matrix definition to apply the nuisance parameters per redshift bin (i.e., "at each $z$ cell"), and rerun the Fisher code immediately if it actually implemented independent $k$-bin marginalization.

## PAPER-GEM-B2: BLOCKER - Internal Contradiction in Fisher Baseline
**Location:** Section 5 vs. Appendix C.1
**Issue:** Section 5 quotes the single-tracer DESI QSO baseline as $\sigma(f_{NL}) = 8.98$, but Appendix C.1 quotes the single-tracer baseline for the "canonical 5-tracer Fisher of \S 5" as $\sigma(f_{NL}) = 16.85$. These cannot both be the baseline for the exact same canonical configuration.
**Fix:** Reconcile the baseline $\sigma(f_{NL})$ values between Section 5 and Appendix C.1, ensuring both refer to the exact same survey volume, $k_{\rm max}$, and tracer density assumptions.

## PAPER-GEM-M1: MAJOR - Theoretical Mismatch in $\alpha$ Reference Baseline
**Location:** Section 5 ("An empirical bias enhancement $\alpha \equiv b_{\rm QSO\,cand}/b_{\rm full\,anomaly} - 1$")
**Issue:** The empirical $\alpha$ is measured relative to the "full anomaly" sample, but the Fisher forecast applies this $\alpha$ as an enhancement over the standard DESI QSO baseline. Because the full anomaly sample is 77% multi-band ELG/LRG, its bias is likely lower than the DESI QSO bias, meaning the empirical $\alpha$ artificially inflates the multi-tracer gain when plugged directly into the DESI QSO-anchored Fisher formula.
**Fix:** Multiply the empirical $(1+\alpha)$ by the ratio $b_{\rm full\,anomaly}/b_{\rm DESI\,QSO}$ before passing it to the Fisher forecast, or explicitly state the assumption that $b_{\rm full\,anomaly} \approx b_{\rm DESI\,QSO}$ and flag it as a known systematic risk.

## PAPER-GEM-m1: minor - Imprecise Theoretical Claim on Multi-Tracer Bias Absorption
**Location:** Section 5 ("while the linear-bias amplitude $\delta b$ is absorbed by the multi-tracer cross-correlations")
**Issue:** Multi-tracer cross-correlations cancel the stochastic cosmic variance of the matter density field; they do not "absorb" deterministic linear bias uncertainty. The $f_{NL}$ constraint survives marginalization over $\delta b(z)$ because $f_{NL}$ has a distinct $1/k^2$ shape, not because of the multi-tracer ratio.
**Fix:** Reword to clarify that multi-tracer cancels sample variance, while the $\delta b$ degeneracy is broken by the distinct $1/k^2$ scale dependence of the $f_{NL}$ signal.

## PAPER-GEM-m2: minor - 1D Gaussian Approximation for PTA Likelihood Ratio
**Location:** Section 5.1 ("Under a Gaussian posterior approximation with $\sigma_\gamma \approx 0.382$, the per-hypothesis $\Delta\chi^2$ ... is 21.31")
**Issue:** Since the exact KDE marginal posterior for $\gamma$ is already evaluated (from the 320,000-sample chain), using a 1D Gaussian approximation to compute the parameter-shift $\Delta\chi^2$ in the tails ($4.6\sigma$ away) is statistically imprecise and unnecessary.
**Fix:** Compute the 1D marginal $\Delta\chi^2$ directly from the exact KDE log-density at $\gamma=4.33$ and $\gamma=3.0$, rather than using the Gaussian $\sigma_\gamma$ approximation.
