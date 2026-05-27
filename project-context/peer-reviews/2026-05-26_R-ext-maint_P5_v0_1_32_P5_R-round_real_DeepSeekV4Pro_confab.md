# P5 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-maint_P5_v0_1_32
**Wall time**: 208.9s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=27881, completion=9734, reasoning=8548, total=37615

---

## PAPER-DEE-B1 — BLOCKER
**Section:** §VII.E (Tempel cross-validation) / Abstract  
**Issue:** The claimed filament-class concordance of **0.026 pp** between V-Web and Tempel cannot be reproduced from the displayed values. Table III gives Tempel `filament_like` \(f_{\rm CW}=0.4982\); Table II gives V-Web filament \(f_{\rm CW}=0.4980\). Their difference is \(0.0002 = 0.02\) pp, **not** 0.026 pp. The abstract and body both quote 0.026 pp as the load-bearing cross-validation metric.  
**Fix:** Recompute the concordance from the raw unrounded values to at least 4 decimal places and ensure the displayed table precision supports the reported difference, or correct the text to the table-consistent value.

## PAPER-DEE-B2 — BLOCKER
**Section:** §VIII (Phase 2 sensitivity sweep), paragraph reporting largest \(|\sigma|\)  
**Issue:** The text states “The largest single-cell \(|\sigma_{\rm from\,half}|\) … is 11.32 (filament at \(R_s=10,\;\lambda_{\rm th}=0,\;n=3{,}696{,}152\)).” The entire chirality-relevant matched-spiral sample size is \(N=791{,}635\). A single environment class **cannot** contain 3.7 million galaxies that have CW/CCW labels. The quoted \(n\) is either the raw galaxy count in that V-Web class (no chirality labels) or a data-processing error; in either case the reported \(\sigma\) is meaningless because it mixes total counts with a chirality fraction derived from a much smaller labeled subset.  
**Fix:** Restrict the Phase 2 \(|\sigma|\) calculation to only the matched-spiral subsample with valid chirality labels. Recompute and re-report the maximum \(|\sigma|\) and the corresponding \(n\). If the originally quoted \(n\) came from a different denominator, delete the sentence.

## PAPER-DEE-M1 — MAJOR
**Section:** §VI.A (Results, cosmic-web environment), paragraph after Table II  
**Issue:** The predicted monopole \(\sigma_{\rm pred}\) for the filament class is miscalculated. The text gives \(\Delta f_{\rm CW}=-0.0026\) and \(n_{\rm filament}=408{,}187\). Eq. (1) yields \(\sigma_{\rm pred}=2\Delta f_{\rm CW}\sqrt{N} = 2(-0.0026)\sqrt{408{,}187} \approx -3.32\), yet the paper states “\(\sigma_{\rm pred}({\rm filament})\approx-3.16\)”. The cluster prediction (\(\approx-3.28\)) is arithmetically consistent, so the filament value appears to be a typo.  
**Fix:** Correct \(-3.16\) to the proper value (\(\approx-3.32\)) or explain which alternative \(N\)/\(f_{\rm CW}\) was used.

## PAPER-DEE-M2 — MAJOR
**Section:** Abstract / §VI.A (void-bin sensitivity floor)  
**Issue:** The abstract states that the systematic floor is “\(\sim\!0.2\) pp” from the Paper IV monopole offset, but the referenced \(\Delta f_{\rm CW}\) is \(-0.0026 = 0.26\) pp. Rounding this to “0.2 pp” obscures the actual systematic and is not derivable from the cited value. The “\(\sim\!5\) pp” counting-statistics floor for the void bin is a reasonable estimate, but the “0.2 pp” phrasing risks being misinterpreted as a precise systematic uncertainty.  
**Fix:** Replace “\(\sim\!0.2\) pp” with the exact offset (0.26 pp) or explicitly note that it is rounded from Paper IV’s \(\Delta f_{\rm CW}=-0.0026\) for readability.

## PAPER-DEE-N1 — minor
**Section:** Abstract / §VIII (Tempel cross-validation sample size)  
**Issue:** The abstract describes the Tempel filament-like bin as “only \(\sim\!14\)k galaxies”, but Table III lists \(n=14{,}317\) for filament-like. The number is precise; using “\(\sim\!14\)k” when the exact value is already known and displayed is a loose summary that may confuse readers who cross-check.  
**Fix:** Quote the exact sample size (\(14{,}317\)) if precision is needed, or keep the approximate form but state it as “14 k” without the tilde.

## PAPER-DEE-N2 — minor
**Section:** §VII.E (Tempel concordance per class)  
**Issue:** The concordance metric is defined as \(|f_{\rm CW}^{\rm Tempel}-f_{\rm CW}^{\rm V-Web}|\) in percentage points, but the paper does not display the raw unrounded \(f_{\rm CW}\) values at more than 4 decimals. The filament-like concordance of 0.026 pp (see B1) and other small differences are therefore not independently reproducible from the printed tables.  
**Fix:** Provide the \(f_{\rm CW}\) values to at least 5 decimals in a footnote or the artifact, and ensure the table rounds consistently with the reported differences.
