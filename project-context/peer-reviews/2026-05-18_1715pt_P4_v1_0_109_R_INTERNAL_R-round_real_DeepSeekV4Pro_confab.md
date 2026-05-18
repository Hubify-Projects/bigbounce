# P4_v1_0_109_R_INTERNAL R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1715pt
**Wall time**: 407.8s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=84470, completion=12581, reasoning=12047, total=97051

---

```markdown
## PAPER-DEE-B1 — MAJOR
**Location:** Abstract, two separate clauses ~20 lines apart.  
**Issue:** The binomial per-pixel-shuffle null on the canonical mask is quoted both as “gives the legacy +1.85σ” and as “gives +3.64σ” (with apodized +3.57σ) within the same abstract. These are contradictory significance values for the identical null model; the reader cannot tell which is the actual canonical-mask residual.  
**Fix:** Remove the stale “legacy +1.85σ” phrase and keep only the corrected +3.64σ value that matches the v1.0.108 multi‑null battery. If the pre‑correction number must be preserved for provenance, label it clearly as pre‑monopole‑subtraction and move it to the main text rather than the abstract.

## PAPER-DEE-B2 — MAJOR
**Location:** Conclusions, “Canonical‑N MASTER ℓ=1 direct compute” paragraph.  
**Issue:** The conclusion still reports the old direct‑MC binomial‑null result as σ_canonical^direct = +1.85σ, while the abstract and the main‑text Monopole+Mask section have updated this residual to +3.64σ after proper monopole subtraction. The abstract itself (see B1) also states the new number. This leaves the paper’s concluding section numerically inconsistent with its own headline claim.  
**Fix:** Update the conclusion to report the corrected +3.64σ binomial‑null value (with the bootstrap null’s –0.22σ) and note that the +1.85σ value was pre‑correction.

## PAPER-DEE-M1 — minor
**Location:** Abstract, multiple headline statements.  
**Issue:** Several load‑bearing scalars (99.3% reproduction, +1.68σ and +4.42σ monopole‑only‑null residuals, +6.48σ pre‑MASTER pseudo‑Cℓ) are stated without an immediate companion‑artifact reference, unlike the cross‑spectrum, multi‑null battery, and injection‑recovery numbers which are explicitly linked to JSON artifacts. Readers auditing provenance must scan later sections to locate the source files.  
**Fix:** Add brief parenthetical artifact citations in the abstract for each of these numbers (e.g., “(companion artifact monopole_mask_null_results.json)”) to match the style used for the cross‑spectrum and other results.
```
