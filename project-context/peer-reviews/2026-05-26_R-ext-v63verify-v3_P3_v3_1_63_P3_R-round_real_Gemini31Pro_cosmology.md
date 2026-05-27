# P3 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v63verify-v3_P3_v3_1_63
**Wall time**: 34.3s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=70942, completion=3747, reasoning=3232, total=74689

---

I have reviewed the manuscript with a specific focus on theoretical cosmology, gauge-frame distinctions, GR projection effects, model-class boundaries, and multi-tracer Fisher scaling. 

You have systematically closed the theoretical physics loopholes flagged in previous rounds. The GR projection effects are correctly classified as gauge-invariant theoretical contamination rather than observational systematics. The matter-bounce model is rigorously scoped to the $w=0$ scalar-only class, preventing EFT consistency-relation violations. The Fisher positivity resolution correctly identifies the exact multi-tracer shot-noise scaling limit. The NANOGrav KDE likelihood math is exact.

I find **0 BLOCKERs** and **0 MAJORs**. The paper is theoretically clean. I provide two terminology nits below for your final polish.

## GEM-NIT-1: Savage-Dickey terminology for disjoint points
**Location:** Section 5.1, paragraph 2 ("Parameter-shift likelihood ratio...") and Section 6.4 caveat (d).
**Issue:** The text states "The proper quantitative comparison requires the 2D joint likelihood evaluation (Savage-Dickey on the existing chain)" to compare the matter-bounce ($\gamma=3.0$) and SMBHB ($\gamma=4.33$) candidates. The Savage-Dickey density ratio is strictly defined for nested models (comparing a free parameter space to a restricted subspace). Comparing two disjoint fixed points in the same parameter space is simply a direct evaluation of the joint posterior/likelihood ratio at those coordinates, not a Savage-Dickey ratio.
**Fix:** Change "Savage-Dickey on the existing chain" to "direct evaluation of the joint 2D likelihood ratio on the existing chain".

## GEM-NIT-2: GR projection scaling notation
**Location:** Section 5, paragraph 6 ("Furthermore, the theoretical template...") and Section 6.4 caveat (e).
**Issue:** The text denotes the general-relativistic projection corrections as $\mathcal{O}(\mathcal{H}^2/k^2)$. While mathematically equivalent, the standard cosmological perturbation theory notation for these terms (which mimic the $\Delta b \propto f_{\rm NL} (\mathcal{H}/k)^2$ local PNG bias) is $\mathcal{O}((\mathcal{H}/k)^2)$. 
**Fix:** Change $\mathcal{O}(\mathcal{H}^2/k^2)$ to $\mathcal{O}((\mathcal{H}/k)^2)$ to perfectly match standard literature notation.
