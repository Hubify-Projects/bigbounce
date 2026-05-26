# P3 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-strict-v2_P3_v3_1_62
**Wall time**: 124.0s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=69971, completion=15996, reasoning=15363, total=85967

---

## PAPER-GEM-B1 [BLOCKER]
**Section:** 5.1 & Appendix D'
**Issue:** Theoretical inversion of bouncing cosmology tensor spectral indices. The paper claims the $w=0$ matter bounce predicts a PTA spectral index $\gamma=3.0$ and explicitly contrasts this with Ekpyrotic models. This is exactly backwards: a $w=0$ matter-dominated contraction yields a scale-invariant tensor spectrum ($n_T=0 \implies \gamma=5.0$), whereas an Ekpyrotic contraction ($w \gg 1$) yields a strongly blue-tilted tensor spectrum ($n_T=2 \implies \gamma=3.0$). 
**Fix:** Correct the matter bounce prediction to $\gamma=5.0$ (which is strongly disfavored by the $\gamma=2.567$ posterior) or change the target model class to Ekpyrotic (which predicts $\gamma=3.0$ but requires a specific mechanism to generate $\fnl \sim \mathcal{O}(1)$).

## PAPER-GEM-M1 [MAJOR]
**Section:** 5
**Issue:** Mismatch in the baseline definition of the bias enhancement factor $\alpha$. The multi-tracer Fisher forecast requires $\alpha$ to be the bias enhancement of the anomaly tracers relative to the *standard DESI QSO* sample. However, the empirical Landy-Szalay measurement defines and computes $\alpha \equiv b_{\rm QSO\,cand}/b_{\rm full\,anomaly} - 1$. Unless the full anomaly sample has the exact same clustering bias as the standard QSO catalog, plugging this measured $\alpha$ directly into the Fisher forecast is mathematically invalid.
**Fix:** Recompute the empirical bias ratio relative to the standard DESI QSO catalog, or explicitly rescale the Fisher input by the measured ratio $b_{\rm full\,anomaly}/b_{\rm standard\,QSO}$.

## PAPER-GEM-M2 [MAJOR]
**Section:** 5
**Issue:** Inconsistent claim regarding $\delta s$ (magnification bias) in the multi-tracer Fisher matrix. The text states the theoretical template explicitly *omits* $\mathcal{O}(\mathcal{H}^2/k^2)$ GR projection effects, yet claims marginalizing over $\delta s$ reproduces the $\sigfnl$ floor. In a purely Newtonian template, $s$ only enters via lensing convergence ($\sim k^2$), which does not mimic the $1/k^2$ local PNG signal. The strong $\delta s$--$\fnl$ degeneracy is a direct consequence of the $(5s-2)$ prefactor on the GR Doppler/Sachs-Wolfe terms; if these terms are omitted, the Fisher matrix should not show $\delta s$ as the dominant $1/k^2$ systematic.
**Fix:** Clarify how $\delta s$ couples to $\fnl$ in the absence of GR terms, or acknowledge that the $\delta s$ dominance is an artifact of an inconsistent Fisher matrix implementation
