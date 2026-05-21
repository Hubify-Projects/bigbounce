# paper4 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-21_R25_P4_v1_0_122
**Wall time**: 278.8s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=89535, completion=11144, reasoning=10608, total=100679

---

## Peer Review — Provenance Audit

### Finding PAPER-PROV-MIN1
**ID:** PAPER-PROV-MIN1  
**Section:** Abstract (line 5 of abstract; “$\sim\!0.6\%$ residual amplitude”)  
**Classification:** minor  
**Issue:** The abstract reports a residual amplitude of “$\sim\!0.6\%$” for the post-TTA Catalog‑C dipole alongside $+0.43\sigma$ and $p=0.30$. The accompanying artifact `catalog_c_post_tta_dipole_summary.json` is cited as the source of the $\sigma$ and $p$ values, but it is not explicitly stated that the amplitude (or its uncertainty) is a key in that JSON. Without that confirmation, the 0.6% figure could be derived from $\sigma$ and error-bar arithmetic rather than a directly stored quantity, which slightly weakens the provenance chain.  
**Fix:** Either (a) insert a parenthetical note that the amplitude is taken from the `amplitude` field of the cited JSON, or (b) state the exact verbatim amplitude from the artifact (and perhaps its error) so that the abstract scalar is directly verified against an on-disk record.

### Finding PAPER-PROV-MIN2
**ID:** PAPER-PROV-MIN2  
**Section:** Abstract (line referencing “99.3% reproduction”)  
**Classification:** minor  
**Issue:** The fractional reproduction (99.3%) is computed from the data and null mean values displayed in Table VI. The table itself is backed by `monopole_mask_null_results.json`, but the 99.3% figure is not a direct key in that JSON; it is a ratio that must be hand-computed from the two numbers. While the arithmetic is simple and error‑free, an immutable “reproduction_fraction” field in the JSON would eliminate any possibility of a rounding or transcription discrepancy in future re‑verifications.  
**Fix:** Add a `reproduction_fraction` (or similar) key to `monopole_mask_null_results.json` so that the headline number exists as an atomic machine‑readable value.

---

**Summary:**  
No BLOCKER or MAJOR provenance gaps were found. Every load-bearing scalar in the abstract and conclusions can be traced to an explicit artifact (JSON, Parquet catalog, or reproducible script) or is a direct algebraic consequence of those artifacts. The two minor findings above concern the convenience of direct keyed storage and do not affect the scientific conclusions.
