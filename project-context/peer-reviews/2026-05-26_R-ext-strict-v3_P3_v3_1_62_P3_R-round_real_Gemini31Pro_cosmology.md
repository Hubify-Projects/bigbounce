# P3 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-strict-v3_P3_v3_1_62
**Wall time**: 123.1s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=69994, completion=15996, reasoning=15356, total=85990

---

# Cosmology-Physics Adversarial Review: "Multi-Survey Spectral Anomaly Detection" (v3.1.62)

## PAPER-GEM-B1: Unphysical Fisher Information Extrapolation at Large $\alpha$
**Class:** BLOCKER
**Location:** Section 5 (Cosmological Applications), Gold+Silver subset forecast ($\alpha=3.86$)
**Issue:** The Fisher-positivity-respecting form $1/\sigfnl^2 = F_0 + c\alpha^2$ is a small-$\alpha$ Taylor expansion that violates multi-tracer shot-noise saturation when extrapolated to $\alpha=3.86$. The exact multi-tracer Fisher information scales as $\alpha^2 / [ (1+\alpha)^2/n_{\rm main} + 1/n_{\rm anom} ]$; while $1/n_{\rm anom}$ dominates at small $\alpha$, at $\alpha=3.86$ the $(1+\alpha)^2/n_{\rm main}$ term becomes comparable (since $n_{\rm main}/n_{\rm anom} \sim 17$, $(1+3.86)^2/17 \sim 1.4$), increasing the denominator by $\sim 2.4\times$. The unbounded $c\alpha^2$ form ignores this saturation, artificially shrinking the lower bound to $\sigfnl=0.94$.
**Fix:** Replace the $c\alpha^2$ extrapolation with the exact multi-tracer Fisher formula that retains the $(1+\alpha)^2/n_{\rm main}$ shot-noise denominator to correctly saturate the $\sigfnl$ lower bound.

## PAPER-GEM-B2: Incorrect Matter-Bounce Tensor Spectral Index ($\gamma$)
**Class:** BLOCKER
**Location:** Section 5.1 (NANOGrav Bounce Consistency) & Appendix D'
**Issue:** The claim that a "scale-invariant scalar power spectrum at $w_{\rm eff}=0$ matter domination" induces a GWB with $\gamma = 3.0$ is theoretically incorrect. A scale-invariant spectrum ($n_s=1, n_T=0$) yields a scale-invariant fractional energy density $\Omega_{\rm GW}(f) \propto f^0$ for modes re-entering during radiation domination, which corresponds to $\gamma = 5$ (since $\gamma = 5 - \beta$ for $\Omega_{\rm GW} \propto f^\beta$). The $\gamma = 3$ ($\Omega_{\rm GW} \propto f^2$) slope corresponds to a strongly blue-tilted tensor spectrum ($n_T=2$), such as the ekpyrotic ($w \gg 1$) prediction, not the $w=0$ matter bounce.
**Fix:** Correct the matter-bounce $\gamma$ prediction to 5 (which would strongly disfavor it against the NANOGrav posterior mean of 2.567), or clarify that $\gamma=3$ requires an ekpyrotic contracting phase rather
