# P3_v3153_R15 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1600pt
**Wall time**: 143.8s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=66990, completion=15996, reasoning=15357, total=82986

---

**Adversarial Peer Review: Cosmology & Theoretical Physics Focus**
**Target:** HUBIFY-2026-003 (v3.1.53)
**Reviewer:** Gemini-3.1-Pro

Below are the findings from a targeted adversarial audit of the theoretical physics, statistical mechanics, and mathematical consistency of the manuscript. 

### PAPER-GEM-B1: BLOCKER - Invalid Linear Error Propagation Across a Stationary Point
**Location:** Section 5 (Cosmological Applications), Lines ~350-360
**Issue:** The manuscript quotes a "symmetric headline" error of $\sigma(f_{\rm NL}) = 8.27 \pm 2.37$, derived via linear error propagation ($\sigma_f = |f'|\sigma_\alpha = |-3.66| \times 0.65$). This is mathematically invalid. The true Fisher mapping $1/\sigma(f_{\rm NL})^2 = F_0 + c\alpha^2$ is an even function with a stationary point at $\alpha=0$. Because the $1\sigma$ interval $\alpha \in [-0.46, 0.84]$ crosses this stationary point, the first derivative vanishes and changes sign within the $1\sigma$ bound, making linear propagation ($\Delta f \approx f' \Delta x$) catastrophically fail. A secant-line slope of $-3.66$ cannot be used to propagate an error distribution that spans across the parabola's vertex.
**Fix:** Completely remove the $8.27 \pm 2.37$ linear-propagation artifact and the $-3.66$ secant-line slope. Quote only the exact, positivity-respecting asymmetric envelope $[3.92, 8.98]$ mapped directly from the $\alpha$ posterior.

### PAPER-GEM-B2: BLOCKER - Scale-Dependent Bias Nuisance Parameter Destroys $f_{\rm NL}$
**Location:** Section 5, Lines ~410-415 ("including a $4n+1$-dimensional nuisance-parameter block per active tracer at each ($k$, $z$) cell, with parameters [$f_{\rm NL}$, $\delta b_i$, $\delta s_i$...]")
**Issue:** Introducing a free linear bias nuisance parameter $\delta b_i$ at *each* $k$-cell explicitly models an arbitrary scale-dependent bias. Because primordial non-Gaussianity manifests strictly as a scale-dependent bias ($\Delta b \propto f_{\rm NL}/k^2$), marginalizing over a free $\delta b_i(k)$ at every wavenumber perfectly absorbs the $f_{\rm NL}$ signal, rendering the true marginalized constraint infinite (or entirely prior-dominated). Multi-tracer cancels sample variance, but it cannot break a degeneracy where the bias of *every* tracer has arbitrary, independent $k$-dependence.
**Fix:** Change the nuisance block definition from "at each ($k$, $z$)
