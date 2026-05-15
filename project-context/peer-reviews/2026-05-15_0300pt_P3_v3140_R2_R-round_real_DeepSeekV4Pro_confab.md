# P3_v3140_R2 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-15_0300pt
**Wall time**: 186.2s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=55236, completion=6509, reasoning=5984, total=61745

---

## PAPER-DEE-B1 — MAJOR: headline deduplication arithmetic internally contradictory
- **Location:** §4.3 cross-matches (states 637 multi-survey coincidences, all pairwise), §Path-C Caveats (deferred item a notes 10,213 implied duplicates). The canonical 378,280 unique count implies 388,493 − 378,280 = 10,213 duplicates. If all coincidences are pairwise, 637 coincidences would account for only 637 duplicates, not 10,213. The paper acknowledges the mismatch but still quotes 378,280 as the canonical catalogue size.
- **Fix:** Either recompute the union‑find cluster manifest to reconcile the counts before using 378,280 as a headline, or remove the contradictory 637 figure (which itself cannot be reproduced from the described dedup) and state the cluster‑level dedup summary explicitly.

## PAPER-DEE-B2 — MAJOR: 17.8% genuine‑novelty fraction lacks a traceable data artifact
- **Location:** Abstract and §4.1 “Archival cross‑match and genuine novelty fraction”. The 17.8% (178/1,000) novelty fraction is a load‑bearing discovery metric, yet no file (e.g., a list of the 178 novel objects or an X‑Match session log) is cited. The paper says only that a cross‑match against 20 catalogues was performed “via CDS X‑Match”.
- **Fix:** Provide a supplementary table or parquet of the 178 candidate novel sources with their cross‑match statuses, or at minimum a reproducibility script that re‑runs the CDS X‑Match query and recovers the same result.

## PAPER-DEE-B3 — minor: σ(f_NL) = 8.27 ± 2.37 forecast not linked to a specific output file
- **Location:** Abstract, §5, Conclusions. The central 8.27 value is said to come from “inserting the empirical central value into the Fisher pipeline”. The paper provides artefacts for the α measurement and the systematics‑marginalized Fisher, but no direct output file (e.g., `fisher_with_alpha_empirical.json`) is referenced for this headline forecast.
- **Fix:** Either deposit the exact Fisher‑run output that yields 8.27 with the given α, or state explicitly that the number is obtained by linear interpretation of Appendix B’s sensitivity table, and cite that derivation.
