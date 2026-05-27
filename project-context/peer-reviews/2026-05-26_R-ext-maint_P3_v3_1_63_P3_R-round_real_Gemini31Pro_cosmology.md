# P3 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-maint_P3_v3_1_63
**Wall time**: 122.8s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=70886, completion=15996, reasoning=15358, total=86882

---

## PAPER-GEM-B1: BLOCKER
**Location:** Appendix D' (Bounce-physics connection) and v3.1.63 Changelog
**Issue:** Fundamental theoretical contradiction regarding the matter-bounce PTA prediction. The changelog defends $\gamma=3$ via primordial "$n_T=2$ blue-tilted tensors", which is the Ekpyrotic ($w \gg 1$) prediction, whereas a matter bounce ($w=0$) yields scale-invariant primordial tensors ($n_T=0 \implies \gamma=5$). Conversely, Appendix D' claims $\gamma=3$ arises from "scalar-induced gravitational waves" (SIGWs), but a scale-invariant scalar spectrum ($n_s=1$) induces $\Omega_{\rm GW} \propto f^0$ ($\gamma=5$) in the radiation era, not $f^2$ ($\gamma=3$). 
**Fix:** Correct the matter-bounce prediction to $\gamma=5$ (or properly specify the Ekpyrotic/SIGW spectral index derivation without conflating the two) and re-evaluate the NANOGrav consistency claim.

## PAPER-GEM-B2: BLOCKER
**Location:** Abstract and Section 5 (Wave 14-KKKK high-confidence forecast)
**Issue:** The abstract and Section 5 quote a $+1\sigma$ lower bound of $\sigfnl = 0.94$ for the Gold+Silver subset, derived from the empirical Taylor expansion $1/\sigfnl^2 = F_0 + c\alpha^2$. As acknowledged in caveat (i), this expansion unphysically drives $\sigfnl \to 0$ at large $\alpha$, ignoring the $(1+\alpha)^2/n_{\rm main}$ shot-noise denominator of the exact multi-tracer Fisher formula which forces an asymptotic floor. Quoting a headline constraint from a known-broken approximation that violates the exact Fisher shot-noise limit is invalid.
**Fix:** Replace the empirical $F_0 + c\alpha^2$ mapping with the exact multi-tracer Fisher formula $\sigfnl^{-2} = F_0 + C \frac{\alpha^2}{(1+\alpha)^2/n_{\rm main} + 1/n_{\rm anom}}$ for all headline credible intervals.

## PAPER-GEM-B3: BLOCKER
**Location:** Section 2.2 (In-sample scoring and held-out validation)
**Issue:** Mathematical contradiction in the OOD validation. The text claims a 100k random SPARCL sample of DESI DR1 has >50% of spectra exceeding the MSE=0.143 threshold, while the 22.5M-spectrum "curated" catalog has only 0.87% exceeding it. Since 22.5M constitutes the vast majority of the ~26M total DESI DR1 spectra, it is mathematically impossible for a true random sample of DR1 to have a >50% failure rate unless
