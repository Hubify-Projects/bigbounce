# P3_v3140_R2 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-15_0300pt
**Wall time**: 119.5s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=58828, completion=15996, reasoning=15356, total=74824

---

This adversarial review of P3 v3.1.40 confirms that the narrative closures from the previous round (f_NL/gamma scoping, mechanism-independent language, deferred items documentation) have been successfully and rigorously integrated. The bibliography is exceptionally clean, passing the Perplexity-style audit with zero fused-arXiv-ID artifacts. 

However, the upgraded model stack caught two severe mathematical/logical contradictions introduced in the new v3.1.40 text—one in the OOD MSE normalization and one in the Fisher forecast error propagation. 

Here are the findings.

## 1. BLOCKER: Mathematical contradiction in OOD MSE normalization
**ID:** PAPER-GEM-B1
**Location:** Section 2.2, paragraph "In-sample scoring and held-out validation"
**Issue:** The text states the 100k OOD sample has a median MSE of 0.178, and that the absolute anomaly threshold is MSE ~0.143. If the threshold (0.143) is below the median (0.178), then by definition **more than 50%** of the OOD sample is flagged as anomalous. Yet the very next sentence claims "the 0.87% DESI anomaly rate is preserved on this independent OOD sample." This is mathematically impossible. Either the OOD median is 0.0178 (a typo in the text), the threshold applied to the OOD sample was a recomputed percentile rather than the absolute 0.143, or the model completely failed to generalize and the 0.87% rate is *not* preserved.
**Fix:** Correct the OOD median value if it is a typo, or clarify exactly what threshold was applied to the OOD sample to recover the 0.87% rate. If the absolute 0.143 threshold truly flags >50% of the OOD sample, the claim that the rate is preserved must be deleted and the generalization failure documented.

## 2. MAJOR: False asymmetry and math error in Fisher forecast CI
**ID:** PAPER-GEM-M1
**Location:** Section 5, paragraph 1
**Issue:** The text claims the 95% confidence interval $\alpha \in [-1.08, +1.46]$ is "not symmetric about its central value" (0.19). This is factually false: $1.46 - 0.19 = 1.27$ and $0.19 - (-1.08) = 1.27$. It is exactly symmetric. Furthermore, mapping this symmetric interval through the "linear-in-$\alpha$ Fisher scaling" ($\sigfnl \approx 8.98 - 3.66\alpha$) should yield a symmetric $\sigfnl$ interval of $[3.64, 12.93]$. Instead, the text reports a highly asymmetric interval of $[5.91, 12.9
