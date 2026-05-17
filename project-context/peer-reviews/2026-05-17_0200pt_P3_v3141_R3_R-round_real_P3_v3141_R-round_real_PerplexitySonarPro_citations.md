# P3_v3141 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-17_0200pt_P3_v3141_R3_R-round_real
**Wall time**: 11.3s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=58184, completion=988, total=59172

---

# Findings

## PAPER-PER-B1 — BLOCKER
**Line/section:** Abstract; `\S\ref{sec:fnl}`; `\S\ref{sec:limitations}`.  
**Issue:** The paper’s own cosmology numbers are internally inconsistent. The abstract/Section 5 now claim a symmetric `\sigma(f_{\rm NL}) = 8.27 \pm 2.37`, but the limitations section still says the correct uncertainty envelope is asymmetric `[5.91, 12.92]`, and elsewhere the paper keeps mixing a legacy fixed-`α = 0.15` forecast (`8.43`, `6.1%`) with the empirical forecast (`8.27`, `7.9%`).  
**Fix:** Pick one canonical forecast path and remove the others from the main text; if legacy numbers remain, quarantine them in a clearly labeled historical note and do not reuse them as live results.

## PAPER-PER-B2 — MAJOR
**Line/section:** `\S\ref{sec:crossmatches}`; Table `tab:survey_summary`; `\S\ref{sec:pathc_caveats}`.  
**Issue:** Dedup arithmetic is not closed. The paper claims `388,493 -> 378,280` after 7-way dedup, but the cross-match section separately reports only `637` multi-survey coincidences and explicitly says no triples exist, which does not reconcile with the implied `10,213` duplicate detections.  
**Fix:** Publish a cluster manifest with per-cluster multiplicity and a full union-find accounting table, or stop claiming the dedup total is fully reconciled.

## PAPER-PER-B3 — MAJOR
**Line/section:** Abstract; `\S\ref{sec:training}`; `\S\ref{sec:pathc_caveats}`.  
**Issue:** The DESI OOD normalization claim is not airtight. The paper says the `S > 5` cut corresponds to `MSE ≈ 0.143`, while the OOD sample median is `0.178`, then simultaneously says the `0.87%` anomaly rate is preserved on OOD data. That preservation is not demonstrated in the text and remains flagged as unresolved.  
**Fix:** Report the OOD rate using the same score units as the production catalog, or explicitly recompute the OOD threshold in native OOD units and show the rate there.

## PAPER-PER-B4 — MAJOR
**Line/section:** `\S\ref{sec:fnl}`; Table `tab:sensitivity`; Appendix `app:sensitivity`.  
**Issue:** The `\alpha`-dependent `f_{\rm NL}` forecast is still mathematically muddled. The paper says `\alpha_{jk} = 0.19 \pm 0.65`, then uses it to derive `\sigma(f_{\rm NL}) = 8.27 \pm 2.37`, while the sensitivity table still anchors `\sigma(f_{\rm NL}) = 8.43` at `\alpha = 0.15`; these are not reconciled cleanly and the propagation formula changes across sections.  
**Fix:** Recompute the sensitivity table from the empirical `\alpha` pipeline only, update all dependent values, and delete the old fixed-`α` table if it is no longer the active result.

## PAPER-PER-B5 — major
**Line/section:** `\S\ref{sec:comparison}`; `\S\ref{sec:limitations}`; abstract.  
**Issue:** The Liang comparison framing is overstated and unstable. The paper alternates between comparing its `378,280` aggregate against Liang’s `2,685` DESI EDR anomalies and comparing a DESI-only `195,829` subset against the same baseline, while also noting the comparison is not like-for-like because the scope and methodology differ.  
**Fix:** State one comparison axis only, preferably DESI-vs-DESI, and keep the aggregate 141x claim out of the headline unless the scope mismatch is explicitly labeled non-comparable.

## PAPER-PER-M6 — minor
**Line/section:** Bib entry `Liang2023`; throughout bibliography and citations.  
**Issue:** The citation metadata are partially fused. The arXiv record for Liang et al. is real and the title is correct, but the bibliography entry mixes journal-style data with a bare arXiv record in a way that should be normalized for auditability.  
**Fix:** Use the exact arXiv metadata or the final journal metadata consistently, not a hybrid record.
