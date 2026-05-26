# P1A R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-26_R-ext-strict_P1A_v1A_0_35
**Wall time**: 13.2s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=30436, completion=917, total=31353

---

## PAPER-PER-B1 — BLOCKER
**Section:** Abstract, Sec. 4, Sec. 12, Appendix B  
**Issue:** Citation forensics fail on the core Holst/parity-odd literature chain. The manuscript attributes “one-loop” parity-odd Holst/Immirzi results to **Mercuri 2009 / Mercuri & Capozziello 2014** and a “Freidel et al. 2005” fermionic Holst coupling, but the cited claims are fused and internally inconsistent: the paper alternates between a one-loop anomaly story and a classical Holst/Nieh–Yan rewrite without a clean source boundary.  
**Fix:** Replace the mixed provenance with a line-by-line source map: one claim per citation, one paper per result, and verify arXiv/journal metadata before submission. If the result is not directly stated in the cited paper, rewrite it as your own derivation or remove it.

## PAPER-PER-B2 — BLOCKER
**Section:** Abstract, Sec. 2.3, Sec. 4.2, Sec. 12  
**Issue:** The manuscript repeatedly claims a quantitative observational birefringence signal from “Planck/ACT DR6” and ties it to specific ALP parameters, but the paper does not establish that the cited observational papers actually support the exact numerical value and interpretation being used here. The same passage also mixes a measured central value, a fitted model value, and a theoretical benchmark as if they were the same quantity.  
**Fix:** Verify the exact measured angle, uncertainty, and statistical interpretation from each cited observational paper, then separate: measured signal, model-fit benchmark, and theory target. Do not state that the literature “consistency” proves your inferred parameter relation unless the cited paper explicitly does so.

## PAPER-PER-M1 — MAJOR
**Section:** Intro, Sec. 4, Sec. 9, Appendix B  
**Issue:** Multiple paragraphs contain audit-trail / version-history contamination in the manuscript body: “v1A.0.34,” “R23,” “closure,” “queued,” “truth-audit,” “vendor,” “prompt-meta error,” and reviewer-history prose. This is not journal-style content and will be treated as non-scientific manuscript noise.  
**Fix:** Purge all version-control, vendor-round, and meta-review narration from the body, abstract, and appendix. Keep only scientific claims and standard provenance in acknowledgments or a separate internal changelog not included in submission.

## PAPER-PER-M2 — MAJOR
**Section:** Abstract, Sec. 4.4, Sec. 12, Sec. 14  
**Issue:** The manuscript overclaims “closure,” “definitively erased,” “no-go,” and “exhaustive” status without a clean operator-basis proof or a jointly nuisance-marginalized fit. It explicitly admits missing operators and non-complete basis coverage, so the language exceeds the demonstrated scope.  
**Fix:** Downgrade all absolute closure language to “channel-level exclusion under the stated four-route basis.” Add a compact scope statement distinguishing what is proven, what is assumed, and what remains open.

## PAPER-PER-M3 — MAJOR
**Section:** Sec. 9, Table of barriers; Sec. 10  
**Issue:** The manuscript says 14 barriers are “13 logically-independent” because B8 is subsumed by B14, yet later still treats them as if both independently close the same observational channel. That is an internal counting inconsistency, not just wording.  
**Fix:** Decide one accounting scheme and use it everywhere: either 13 independent plus 1 historical duplicate, or 14 catalog entries with explicit non-independence. Update the abstract, tables, and conclusions to match.

## PAPER-PER-n1 — nit
**Section:** Appendix A, Appendix B, Sec. 4.2  
**Issue:** Several cited-paper metadata items are likely wrong or at least unverified in the manuscript itself: journal venues, arXiv IDs, and author-year pairings are used without a reference audit table. This is especially risky where multiple distinct papers are conflated into one claim chain.  
**Fix:** Add a bibliography audit appendix with: exact title, authors, journal, year, arXiv ID, and the specific sentence supported. Correct any fused metadata before submission.
