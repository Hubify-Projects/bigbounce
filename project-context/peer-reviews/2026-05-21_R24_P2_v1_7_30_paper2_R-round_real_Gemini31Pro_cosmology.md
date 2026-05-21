# paper2 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-21_R24_P2_v1_7_30
**Wall time**: 137.5s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=30542, completion=15996, reasoning=15356, total=46538

---

Here is the adversarial review of the manuscript, focusing on theoretical physics, EFT boundaries, and cosmological observables.

## PAPER-GEM-B1: BLOCKER - QSFI scaling dimension and physical limits are inverted
**Section:** 8.4 (Discussion)
**Issue:** The QSFI squeezed-limit scaling relative to the local template is incorrectly stated as $(k_3/k_1)^{\Delta - 3/2}$. The correct relative scaling is $(k_3/k_1)^\Delta$ (since the local template scales as $k_3^0$ relative to $1/(k_1^3 k_3^3)$). Because of this $-3/2$ exponent error, the text completely inverts the physical limits: $\mu/H=0$ ($\Delta=0$) produces the exact local shape, not a "super-squeezed / long-mode-divergent shape", while $\mu/H \to 3/2$ ($\Delta \to 3/2$) produces a suppressed equilateral-like scaling, not the local template. 
**Fix:** Correct the relative scaling to $(k_3/k_1)^\Delta$ and swap the descriptions of the $\mu/H=0$ and $\mu/H=3/2$ limits to correctly reflect the standard QSFI literature (Chen & Wang 2009).

## PAPER-GEM-M1: MAJOR - Suyama-Yamaguchi saturation incorrectly tied to template overlap
**Section:** 8.4 (Discussion)
**Issue:** The text claims the matter bounce does not saturate the Suyama-Yamaguchi (SY) inequality $\tau_{\rm NL} \geq (6\fnl/5)^2$ because its bispectrum is not exactly local (template overlap $r < 1$). This is a theoretical error: the SY equality $\tau_{\rm NL} = (6\fnl/5)^2$ holds in the squeezed/collapsed limits for *any* single-source superhorizon mechanism (which the scalar-only matter bounce is), completely independent of the global shape overlap $r$ at folded/equilateral configurations. 
**Fix:** State that the single-field matter bounce saturates the SY inequality yielding $\tau_{\rm NL} \approx 27.56$, and remove the claim that $r < 1$ prevents saturation.

## PAPER-GEM-M2: MAJOR - Gauge-frame vs physical-frame observational inversion
**Section:** Abstract
**Issue:** The text claims that telescopes "measure the conventional Planck/local-template $\fnl$ in the gauge frame, not the CFC physical-frame quantity directly". This is conceptually backwards: telescopes observe the physical sky (which inherently includes all GR projection effects, corresponding to the physical frame). The "gauge-frame" $\fnl$ is not measured directly; it is inferred only after theoretically modeling and subtracting these GR projection effects from the physical measurement.
**Fix:** Clarify that the on-sky observable is the physical one, and the gauge-frame
