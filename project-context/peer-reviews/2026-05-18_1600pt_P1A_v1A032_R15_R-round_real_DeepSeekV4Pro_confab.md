# P1A_v1A032_R15 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1600pt
**Wall time**: 208.8s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=27282, completion=11960, reasoning=11279, total=39242

---

# Adversarial Peer Review: P1A v1A.0.32 — Provenance & Arithmetic Audit

**Overall verdict:** 1 MAJOR finding (arithmetic error in a headline scalar). No BLOCKERs. The paper is otherwise cross‑referenced appropriately; all other load‑bearing numbers are either sourced from companion papers, standard cosmology, or reproducible from displayed values.

---

## PAPER-DEE-M1 (MAJOR) — Incorrect exponent in the bounce‑era physical‑scale mapping (Abstract & Sec. 14.4)

**Location:** Abstract (lines ~40–50) and Section 14.4 (“Structural Tension …”).  
**Issue:** The paper states that a SPHEREx‑accessible comoving wavenumber \(k_{\rm SPHEREx}\sim 10^{-1}\,h/{\rm Mpc}\) is pushed to a bounce‑era physical scale  
\[
k_{\rm bounce}^{\rm phys} \sim k_{\rm SPHEREx}^{\rm phys}\, e^{N_{\rm tot}-N_{\rm exit}} \sim e^{32}\,k_{\rm SPHEREx}^{\rm phys},
\]  
with \(N_{\rm tot}\approx 92\) and \(N_{\rm exit}\approx 60\) (the “relative e‑fold differential between bounce and CMB horizon‑exit”).  

The correct scaling from today’s physical wavenumber to the bounce physical wavenumber is  
\[
k_{\rm bounce}^{\rm phys} = \frac{k}{a_{\rm bounce}} = \frac{k}{a_0 e^{-N_{\rm tot}}} = k_{\rm today}^{\rm phys}\, e^{N_{\rm tot}} \sim e^{92}\,k_{\rm SPHEREx}^{\rm phys},
\]  
because comoving \(k\) is constant and \(a_{\rm bounce}/a_0 = e^{-N_{\rm tot}}\). The exponent \(N_{\rm tot}-N_{\rm exit}\) would be appropriate only if \(k_{\rm SPHEREx}^{\rm phys}\) were the physical wavenumber at horizon exit, which it is not. The displayed value \(e^{32}\) is therefore off by a factor of \(e^{60}\sim 10^{26}\).  

**Fix:** Replace \(e^{N_{\rm tot}-N_{\rm exit}}\) with \(e^{N_{\rm tot}}\) (and the numerical example \(e^{32}\) with \(e^{92}\sim 10^{40}\)). The qualitative conclusion (mode is deep inside the inflationary subhorizon) is unaffected, but the arithmetic must be corrected to avoid propagating a factor‑of‑\(10^{26}\) error in a load‑bearing scalar.

---

**Remaining numbers:** All other headline figures (\(\fnl=-35/8\), \(\beta\approx 0.27^\circ\), \(H_0=67.68\pm 1.06\), \(\Delta N_{\rm eff}\approx 0\), \(N_{\rm tot}\approx 92\), etc.) are either cross‑referenced to companion papers with documented MCMC/analysis pipelines, derived from standard cosmological parameters with arithmetic shown, or are order‑of‑magnitude estimates whose provenance is explicitly stated. No further load‑bearing math errors were detected.
