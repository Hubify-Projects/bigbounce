# P4 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v133verify_P4_v1_0_133
**Wall time**: 196.1s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=95914, completion=9217, reasoning=8552, total=105131

---

## PAPER-DEE-B1 — Canonical‑$N$ MASTER $\ell{=}1$ direct‑compute paragraph contains arithmetic that contradicts its own stated $\sigma$

**Location:** §Conclusions, “Canonical‑$N$ MASTER $\ell{=}1$ direct compute” paragraph (immediately before the three‑estimator table).  
**Issue:** The paragraph displays $C_1^{\rm decoupled}=2.298\times10^{-5}$, null mean $8.004\times10^{-6}$, null std $8.097\times10^{-6}$, and claims $\sigma_{\rm canonical}^{\rm direct}=+3.64\sigma$. The computation $(2.298\times10^{-5}-8.004\times10^{-6})/8.097\times10^{-6} = 1.85$, not $3.64$. These numbers correspond to the uncorrected (legacy pre‑correction) baseline, which yields $+1.85\sigma$; the proper‑monopole‑subtracted analysis that gives $+3.64\sigma$ uses different values ($C_1=1.51\times10^{-5}$, null mean $3.12\times10^{-6}$, null std $3.31\times10^{-6}$). The manuscript therefore provides a self‑contained arithmetic refutation of its headline $+3.64\sigma$ if the reader trusts only the numbers shown in that paragraph.  
**Fix:** Replace the displayed numbers with the corrected triplet from `p4_multinull_battery.json` (or the NaMaster‑config section) and recompute $\sigma$; if the intent is to show the legacy baseline, relabel it explicitly and state its correct $\sigma$ ($+1.85$), then separately present the corrected $+3.64$ result.

## PAPER-DEE-M1 — Canonical‑mask $f_{\rm sky}$ is inconsistent between the main text and the conclusions table

**Location:** Main‑text definitions ($f_{\rm sky}=0.49005$, 24 087 pixels) vs. the three‑$\ell{=}1$‑estimators table in the Conclusions ($f_{\rm sky}=0.494$, 24 269 pixels for the canonical‑$N$ direct‑MC row).  
**Issue:** The canonical mask is consistently described elsewhere as having $f_{\rm sky}=0.49005$ and $N_{\rm pix}=24\,087$ (e.g., abstract, monopole‑mask‑null table, NaMaster‑config section). The conclusions table gives a different sky fraction ($0.494$) and pixel count ($24\,269$) for what is presented as the same estimator. No explanation is offered for this shift, which is significant for a mask‑edge‑sensitive diagnostic and violates the expectation that a “canonical” quantity is defined uniquely.  
**Fix:** Reconcile the numbers — either correct the table to $f_{\rm sky}=0.49005$ and $24\,087$ (or document that the direct‑MC run used a slightly different pixel‑count threshold) and state why the difference is harmless.
