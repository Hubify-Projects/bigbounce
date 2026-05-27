# P4 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v138verify-v2_P4_v1_0_138
**Wall time**: 124.0s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=106919, completion=15996, reasoning=15358, total=122915

---

# Peer Review Report

**Paper:** Survey-Scale Galaxy Chirality with Equivariant TTA
**Reviewer:** Gemini-3.1-Pro (Adversarial Cosmology-Physics Review)
**Status:** 1 BLOCKER, 3 MAJOR, 1 minor

## PAPER-GEM-B1: Mathematically impossible Bernoulli variance inflation (BLOCKER)
**Location:** Section III.E (Test-Time Equivariant Averaging), paragraph "Hard-label variance widening..."
**Issue:** The paper derives a variance inflation factor of $\approx 1.29\times$ (or empirical $1.21\times$) for the hard-label binomial variance due to the $21.4\%$ argmax-flip rate. This is mathematically impossible. The observed hard label $x_{\rm obs}$ is a Bernoulli random variable with mean $p_{\rm obs} \approx 0.5$. The maximum possible variance of *any* Bernoulli variable is $0.25$. The standard binomial variance formula $\sigma^2 = p_{\rm obs}(1-p_{\rm obs})/N$ already perfectly and fully captures the flip noise. The derivation erroneously adds the flip variance $p_{\rm flip}(1-p_{\rm flip})$ to the true variance $p(1-p)$ without applying the required $(1-2p_{\rm flip})^2$ shrinkage factor to the true variance, resulting in a single-trial variance of $\sim 0.418$, which violates the laws of probability.
**Fix:** Remove the entire hard-label variance widening derivation and the $1.21\times$ inflation factor applied to hard-binned diagnostics. Use the standard binomial error $\sqrt{p_{\rm obs}(1-p_{\rm obs})/N}$, which is exact.

## PAPER-GEM-M1: Missed parity-odd theoretical consistency relation (MAJOR)
**Location:** Section VI.D (Monopole+Mask Leakage Generative Null), "Direct cross-spectrum diagnostic"
**Issue:** The paper correctly identifies the $\ell=2$ cross-spectrum $C_\ell^{An}$ between chirality $A$ and density $n$ as evidence of a depth-correlated systematic, but misses the rigorous theoretical proof this observable provides. The cross-spectrum between a pseudoscalar ($A$) and a scalar ($n$) is strictly parity-odd. A non-zero $C_\ell^{An}$ requires parity violation. The classifier's global CW deficit ($\epsilon < 0$) is a parity-odd monopole. If the $\ell \ge 1$ anisotropy is purely the depth-modulation of this monopole ($A(\hat n) \approx \epsilon \delta n(\hat n)$), the cross-correlation coefficient must theoretically be $r_\ell \approx \text{sgn}(\epsilon) = -1$. The observed $r_{\ell=1}=-0.49$ and $r_{\ell=2}=-0.65$ perfectly satisfy this parity-odd consistency relation, proving the $\ell
