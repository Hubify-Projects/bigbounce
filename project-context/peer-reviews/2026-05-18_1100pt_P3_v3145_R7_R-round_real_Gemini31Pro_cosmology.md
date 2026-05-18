# P3_v3145_R7 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1100pt
**Wall time**: 135.2s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=61009, completion=15996, reasoning=15361, total=77005

---

This R7 adversarial review verifies the v3.1.45 updates, focusing on theoretical physics consistency, convergent regressions, and the completeness of the deferral list. The tier separation in the abstract is now excellently scoped and internally consistent. However, the Fisher CI arithmetic fix introduced new truncation errors, and a promised verification table remains missing.

## PAPER-GEM-M1: MAJOR
**Location:** Section 5 (Fisher CI arithmetic) and Abstract
**Issue:** The Fisher $\sigma(f_{\rm NL})$ arithmetic contains truncation errors and internal contradictions that break the linear mapping $\sigma(f_{\rm NL}) = 8.98 - 3.66\alpha$. At $\alpha = 0.19$, the central value is $8.28$, not $8.27$. The propagated error $3.66 \times 0.65 = 2.379$ rounds to $2.38$, not $2.37$. Furthermore, the text claims the 95% CI is $[3.64, 12.93]$ while simultaneously claiming this equals $8.27 \mp 4.663$ (which actually yields $3.61$ for the lower bound). Using the exact $\alpha$ bounds $[-1.084, 1.464]$ yields a 95% CI of $[3.62, 12.95]$.
**Fix:** Update the central value to $8.28 \pm 2.38$ and the 95% CI to $[3.62, 12.95]$ to restore exact arithmetic consistency with the $8.98 - 3.66\alpha$ mapping.

## PAPER-GEM-M2: MAJOR
**Location:** Section 6.4, caveat (i)
**Issue:** The text claims a 103,000-spectrum holdout was scored through the production BigAE and five control retrains (6 models total) in "5.1 s wall". This implies an inference throughput of $\sim 121,000$ spectra/s, which contradicts the benchmarked DESI H200 throughput of 1,142 spectra/s (Table 2 and Section 2.3) by two orders of magnitude.
**Fix:** Correct "5.1 s wall" to "5.1 minutes wall" (or the true execution time) to align with the documented hardware inference throughput.

## PAPER-GEM-M3: MAJOR
**Location:** Table 1 footnote $\S$ and Section 6.4 deferral (f)
**Issue:** Missing Deliverable. The text states the BigAE-vs-IF exact empirical intersection count is "queued for the v3.1.44 verification table". This is version 3.1.45, but the table is still missing and the text still refers to it as queued for the
