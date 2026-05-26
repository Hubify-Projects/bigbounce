# P3 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v63verify_P3_v3_1_63
**Wall time**: 144.5s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=70991, completion=15996, reasoning=15361, total=86987

---

## PAPER-PHYS-MAJOR-1: Contradictory physical mechanisms for matter-bounce $\gamma=3.0$ prediction
**Location:** Changelog (L34) vs Appendix D' (L1078)
**Issue:** The text asserts two mutually exclusive physical origins for the $\gamma=3.0$ PTA prediction. The changelog attributes it to primordial blue-tilted tensors ($n_T=2$) via $k^2H^2$ mode-amplification, while Appendix D' attributes it to scalar-induced gravitational waves (SIGWs) from a scale-invariant scalar spectrum. Furthermore, a standard $w=0$ matter bounce yields a scale-invariant primordial tensor spectrum ($n_T=0 \implies \gamma=5$); an $n_T=2$ primordial tilt requires an ekpyrotic ($w \gg 1$) contraction. 
**Fix:** Reconcile the text to cite a single, physically consistent mechanism for the $\gamma=3.0$ prediction, ensuring the assumed equation of state $w$ matches the cited tensor tilt or SIGW source.

## PAPER-PHYS-MAJOR-2: Unphysical Fisher bound quoted in main text despite appendix proof of invalidity
**Location:** Section 5 (L665) and §pathc_caveats(i)
**Issue:** Section 5 quotes a $1\sigma$ lower bound of $\sigfnl^{\rm GS} = 0.94$ at $\alpha=3.86$ derived from the empirical $F_0 + c\alpha^2$ approximation. However, caveat (i) explicitly proves this approximation breaks down and unphysically overestimates the constraint for $\alpha \gtrsim 3.1$ due to the exact multi-tracer formula's shot-noise saturation transition. You cannot quote a headline bound that your own appendix proves is mathematically invalid.
**Fix:** Replace the $0.94$ bound in Section 5 with the value computed from the exact saturating multi-tracer Fisher formula provided in caveat (i), rather than deferring the correct arithmetic while quoting a known-broken bound.

## PAPER-PHYS-MAJOR-3: Stale text contradicts abstract on canonical credible interval
**Location:** Section 5 (L615) vs Abstract
**Issue:** The abstract explicitly states the local-linear approximation $8.27 \pm 2.37$ is REMOVED from the headline because it "catastrophically fails" at the $\alpha=0$ stationary point, declaring the positivity-respecting $[3.92, 8.98]$ envelope as canonical. However, Section 5 contains a stale sentence stating: "we retract that envelope and quote the symmetric $\pm 2.37$ ($1\sigma$) / $\pm 4.65$ (95%) form as the canonical credible interval," directly contradicting the abstract and the subsequent paragraph.
**Fix:** Delete the stale sentence in Section 5
