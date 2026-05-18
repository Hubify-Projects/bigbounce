# P3_v3150_R12 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1400pt
**Wall time**: 179.6s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=61292, completion=4582, reasoning=3511, total=65874

---

## PAPER-DEE-B1 (BLOCKER) — Headline 378,280 unique anomalies is not traceable to a verified artifact

**Section:** Abstract, §4.3, §6.4 deferral (a), Conclusions.  
**Issue:** The paper’s primary result—the 378,280 unique-object count after 7-way deduplication—is explicitly flagged as pending recompute. The text acknowledges a 9,576‑object shortfall under the all‑pairwise assumption (387,856 vs. 378,280) and states the headline is “frozen at the previously‑reported value pending a full intra‑survey duplicate recompute.” No JSON, script, or dataset on disk currently produces the 378,280 number; the only arithmetic upper bound that can be reproduced from the given survey‑level counts and the 637 reported coincidences is 387,856.  
**Fix:** Either run the union‑find cluster manifest recompute and update the headline to a verified value, or replace the headline with the verified upper bound 387,856 and clearly label the final count as provisional.

## PAPER-DEE-B2 (MAJOR) — Single‑tracer DESI QSO baseline σ(f_NL)=8.98 has no provenance

**Section:** §5, Abstract, Conclusions.  
**Issue:** All multi‑tracer improvement percentages (7.9%, 6.1%, etc.) are computed relative to a “standard DESI QSO constraint” of σ(f_NL)=8.98. The paper does not cite a published forecast, provide a companion script, or reference an internal Fisher‑matrix artifact that yields this number. The Heinrich+2024 anchor is for SPHEREx, not DESI, so the 8.98 baseline is untraceable.  
**Fix:** Add a reference to the specific Fisher run or external publication that produces σ(f_NL)=8.98 for DESI QSO alone, or include the computation in the reproducibility package.

## PAPER-DEE-B3 (minor) — 17.8% genuine novelty fraction lacks a concrete artifact reference

**Section:** Abstract, §4.1, §6.3.  
**Issue:** The 17.8% figure is said to come from cross‑matching the top‑1,000 DESI anomalies against 20 all‑sky catalogs via CDS X‑Match, but no output file (e.g., a CSV or Parquet of the cross‑match results) or exact list of the 20 catalogs is cited. The paper mentions a “companion data release” without a specific filename.  
**Fix:** Add a footnote or data‑availability statement pointing to the exact artifact (e.g., `xmatch_top1000_desi.parquet`) and the catalog list used.

## PAPER-DEE-B4 (minor) — 141× scale increase inherits dedup uncertainty

**Section:** Abstract, Conclusions.  
**Issue:** The claim of a 141× increase over Liang et al. (378,080 / 2,685) uses the point‑source tier count 378,080, which is derived from the same unverified dedup as the headline 378,280. Until the dedup is resolved, the ratio is not reliable.  
**Fix:** Either recast the scale comparison using the verified DESI‑only count (195,829, giving 73×) or explicitly note that the 141× figure is provisional pending the dedup recompute.

## PAPER-DEE-B5 (nit) — Aggregate SIMBAD‑unmatched fraction weighting unspecified

**Section:** §4.1, Fig. 7 caption.  
**Issue:** The aggregate 58.8% SIMBAD‑unmatched fraction is described as “weighted across all surveys with SIMBAD‑matchable coordinates,” but the weighting method (e.g., by number of anomalies per survey, by sky area, or by inverse variance) is not stated. The per‑survey percentages in Table 1 cannot be combined into 58.8% without knowing the weights.  
**Fix:** State the weighting scheme explicitly (e.g., “weighted by the number of anomalies with coordinate matches in each survey”) or provide the raw counts used.

## PAPER-DEE-B6 (nit) — 37.3 million sources rounding vs. table total

**Section:** Abstract, §1.  
**Issue:** The abstract repeatedly states “37.3 million sources,” but the sum of the N_total column in Table 1 (excluding ACT) is 37,272,042, which rounds to 37.3 million only if one rounds 37.27 to 37.3. While not incorrect, the precision is inconsistent with the table’s exact sum.  
**Fix:** Either use “37.27 million” for consistency with the table, or add a footnote clarifying that 37.3 million is rounded from 37,272,042.
