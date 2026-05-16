# P4_v1095 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-16_0130pt_P4_v1095_R14_R-round_real
**Wall time**: 291.8s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=77932, completion=8297, reasoning=7676, total=86229

---

## Adversarial Peer Review — R14 v1.0.95 (P4)

**Verdict:** No BLOCKER or MAJOR findings.  The four R13-residual closures are correctly implemented, and the convergence signal from R13 holds.  Two minor ambiguities in the abstract should be resolved before external submission.

---

### Finding PAPER-DEE-MIN1 (minor)
**Location:** Abstract, lines 6–12 (reproducing 99.3% … residual +1.68σ)
**Issue:** The phrase “reproducing 99.3% of the observed pre‑MASTER pseudo‑C₁ power” does not state which map the pseudo‑C₁ comes from.  The same paragraph later clarifies that it is the un‑monopole‑subtracted CW‑fraction map, but a reader who skims the headline alone may incorrectly associate the 99.3% with the asymmetry‑map bandpower discussed just before.  
**Fix:** Insert “on the un‑monopole‑subtracted CW‑fraction map” after “pre‑MASTER pseudo‑C₁ power” in the parenthetical sentence.

### Finding PAPER-DEE-MIN2 (minor)
**Location:** Abstract, line 13 (“~49% of the hemisphere maximum amplitude with a residual +4.42σ”)
**Issue:** The hemisphere maximum amplitude is drawn from the same monopole‑only null on the CW‑fraction map, but the abstract omits this context.  The phrase “hemisphere channel” could be taken to refer to the hemisphere asymmetry scan on the asymmetry map, which is a different observable.  
**Fix:** Add “on the same CW‑fraction map” after “hemisphere maximum amplitude” to prevent conflation with the earlier asymmetry‑map hemisphere statistic.

### Finding PAPER-DEE-NIT1 (nit)
**Location:** Abstract, lines 10–12 (null‑mean precision)
**Issue:** The abstract gives the null mean as 1.6846×10⁻²±6.8×10⁻⁵ in one sentence and 1.68×10⁻²±0.07×10⁻³ in a later sentence.  Both are consistent, but the two different roundings (6.8×10⁻⁵ vs. 7×10⁻⁵) could confuse a fast reader.  
**Fix:** Use a single representation, e.g. 1.685×10⁻²±6.8×10⁻⁵, in both places.

---

No other issues.  The corrected injection‑fit count (900), the deseamed III.C text, the LSST bibitem fix, and the softened abstract framing are all correctly evidenced and free of new regression.  The on‑disk artifacts `monopole_mask_null_results.json` and `injection_recovery_extended.json` produce the stated numbers.  The paper is ready for external review after the two minor abstract clarifications.
