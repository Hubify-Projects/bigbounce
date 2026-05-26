# P4 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v132verify_P4_v1_0_132
**Wall time**: 152.3s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=100767, completion=15996, reasoning=15358, total=116763

---

## PAPER-GEM-B1: Unphysical Generative Null Leakage Amplitude
**Class:** BLOCKER
**Section:** IV.D (Table V)
**Issue:** Table V computes the pre-MASTER pseudo-$C_1$ on the "un-monopole-subtracted CW-fraction map" (mean $\sim 0.5$). The resulting $C_1 \sim 10^{-2}$ is entirely the mode-coupling of the isotropic, parity-even $0.5$ background with the mask dipole. It has nothing to do with the parity-violating $0.0026$ classifier bias. Prior literature (e.g., Shamir) fits the asymmetry $A_p$ (mean $\sim 0.005$), which removes the $0.5$ background. Claiming this $10^{-2}$ leakage explains the literature's systematic artificially inflates the true bias leakage by $\sim 40,000\times$.
**Fix:** Subtract $0.5$ from the CW-fraction map before computing the generative null pseudo-$C_1$, and report the true leakage of the $0.0026$ bias.

## PAPER-GEM-B2: Subsample Mask Null is Noise-Drowning, Not Systematic Removal
**Class:** BLOCKER
**Section:** IV.C & VII (Mask discrepancy)
**Issue:** The canonical mask ($N \ge 10$ cut) yields a $+3.64\sigma$ residual, while the subsample mask (a superset including $N < 10$ pixels) yields $-0.12\sigma$. The paper claims the subsample mask "bypasses the leakage channel". Physically, adding highly noisy $N < 10$ pixels at the survey edges increases the true pixel-weighted noise floor $N_\ell = \Omega_{pix} \sum \sigma_i^2$. The subsample mask is not bypassing the large-scale depth systematic; it is simply drowning it in the un-modeled shot noise of the $N < 10$ pixels, while the text incorrectly relies on the uniform noise approximation $4\pi f_{sky}/N$.
**Fix:** Compute the exact pixel-weighted noise floor $N_\ell$ for the subsample mask. Do not claim the subsample mask "bypasses" the systematic unless the decoupled $C_1$ amplitude (not just the $\sigma$) is shown to be stable.

## PAPER-GEM-B3: Contradiction in Primary Observable Definition
**Class:** BLOCKER
**Section:** IV.C vs Table II
**Issue:** Direct contradiction in the primary observable definition. Section IV.C defines $A_p = (N_{CW} - N_{CCW}) / (N_{CW} + N_{CCW})$, which uses hard argmax counts. Table II claims the load-bearing $\ell=1$ MASTER uses a "soft $p_{CW}$-weighted" map
