# P4 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v132verify_P4_v1_0_132
**Wall time**: 193.9s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=95375, completion=8962, reasoning=7534, total=104337

---

## PAPER-DEE-B1 — BLOCKER
**Location:** L1 comment header (TeX source, lines 1–2)  
**Issue:** The v1.0.132 closure note claims the L1 `%`-comment header was rewritten to match the v1.0.129 reframed title, but the header still reads “No Evidence for Large-Scale Parity Violation in Galaxy Morphology: A Survey-Scale Chirality Catalog of 8.47 Million Galaxies”. This directly contradicts the paper’s own parity‑even/axial‑vector framing and will propagate into arXiv metadata (title extraction from the first TeX line).  
**Fix:** Replace the L1 comment header with the actual `\title{}` text (the long v1.0.129 reframed title) or a neutral short form that does not mention parity violation.

## PAPER-DEE-B2 — MAJOR
**Location:** Table I footnote b (post‑MASTER monopole‑only null, N=500 vs N=10,000)  
**Issue:** The footnote states “null std 1.13e-6 (vs 1.19e‑7 at N=500, stable to 5%)”. The N=500 null std is 1.19 × 10⁻⁶, not 1.19 × 10⁻⁷; the exponent is off by a factor of 10. This is a typographical error that could mislead a reader checking the arithmetic.  
**Fix:** Correct “1.19e‑7” → “1.19e‑6”.

## PAPER-DEE-B3 — minor
**Location:** Abstract, line “the MASTER-deconvolved single-mode pseudo‑C₁ … yields −0.12σ”  
**Issue:** The quantity reported is the *decoupled* C₁ (after MASTER inversion), not a pseudo‑C₁. Calling it “pseudo‑C₁” is technically incorrect and may confuse readers familiar with the standard pseudo‑Cℓ vs. decoupled Cℓ distinction.  
**Fix:** Replace “pseudo‑C₁” with “decoupled C₁” or “MASTER‑deconvolved C₁”.

## PAPER-DEE-B4 — minor
**Location:** Abstract, “the post-MASTER canonical-mask direct-MC residual is +3.64σ … the corrected +3.64σ replaces it as the canonical canonical-mask number”  
**Issue:** The phrase “canonical canonical-mask number” is a stutter; it should read “canonical canonical‑mask value” or simply “the canonical‑mask number”.  
**Fix:** Delete the duplicated “canonical”.

## PAPER-DEE-B5 — nit
**Location:** Abstract, “the 0.75–1.5% range across strict-HC pipeline variants”  
**Issue:** The abstract does not cite the specific artifacts that define the 1.5% upper bound (the strict‑HC sweep without per‑pixel‑count filter). While the sensitivity section later provides the references, a reader of the abstract alone cannot verify the provenance of the 1.5% endpoint.  
**Fix:** Add a parenthetical “(see Sec. \ref{sec:sensitivity} for artifact paths)” or move the range statement to the sensitivity section.

## PAPER-DEE-B6 — nit
**Location:** Conclusions, “the post-MASTER monopole-only N=500 null … accounts for ~12% of the post-MASTER canonical C₁ (data 6.55e-6 vs null mean 8.0e-7)”  
**Issue:** The ratio 8.0 × 10⁻⁷ / 6.55 × 10⁻⁶ = 0.122, which rounds to 12%. However, the null mean is given as 8.0 × 10⁻⁷ in the text but the companion artifact `master_decoupled_monopole_null.json` reports 8.01 × 10⁻⁷ (as stated in the footnote). Using 8.01 × 10⁻⁷ gives 12.2%, still ~12%, but the rounding is inconsistent with the precision of the input.  
**Fix:** Either quote the null mean as 8.01 × 10⁻⁷ to match the artifact, or state “≈12%” to acknowledge the rounding.
