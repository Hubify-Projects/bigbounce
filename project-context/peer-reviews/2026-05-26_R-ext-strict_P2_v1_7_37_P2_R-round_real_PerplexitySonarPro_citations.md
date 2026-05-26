# P2 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-26_R-ext-strict_P2_v1_7_37
**Wall time**: 10.9s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=33729, completion=968, total=34697

---

## PAPER-PER-B1 — BLOCKER

**Section:** title/abstract/body metadata, all over the manuscript.

The manuscript is contaminated with audit-trail and AI-vendor/version-history prose that belongs in internal notes, not a journal submission: e.g. `v1.7.37`, `R-next-*`, `OpenAI`, `Grok`, `Gemini`, `ChatGPT`, `Perplexity`, `truth-audit`, `queued`, `next pod cycle`, and similar live-edit commentary. This is publication-incompatible and must be purged everywhere, including comments, appendix notes, acknowledgments, and any figure/table captions.

**Fix:** Strip all version-control, vendor, and review-log language from the body and appendices. Keep only scientific content and a clean, single manuscript version string if the journal requires one.

## PAPER-PER-B2 — BLOCKER

**Section:** Abstract; Introduction; Sec. “Current Data and Consistency Relation”; Conclusion.

The paper overclaims closure in multiple places without the full joint nuisance-marginalized treatment it itself admits is deferred. Phrases like “definitive verification,” “tested at \(3\)–\(5\sigma\),” and the strong “disfavors” language are not justified when the manuscript repeatedly says the Fisher inputs, GR treatment, and \(b_\phi\) marginalization are incomplete or only partially modeled.

**Fix:** Downgrade all closure language to conditional forecasts and explicitly separate headline idealized results from post-systematic, partially modeled estimates. If the claim depends on a joint nuisance-marginalized fit, state that the fit is not yet performed.

## PAPER-PER-B3 — MAJOR

**Section:** Sec. “Inflation Mimicry and Bayesian Comparison”; Table `tab:bayes`; Appendix A.2.

The Bayes-factor presentation is internally unstable and mixes headline, sensitivity, and “closure” claims in a way that is not publication-safe. The manuscript itself shows multiple incompatible envelopes and prior choices, and the table/caption hierarchy makes it too easy to read the broad-grid numbers as a definitive model-selection result.

**Fix:** Declare one primary competitor prior and one primary bounce prior, then relegate the others to diagnostics. Remove “headline envelope” language unless the prior grid is explicitly pre-registered and the table is framed as a sensitivity study, not evidence of decisive model selection.

## PAPER-PER-B4 — MAJOR

**Section:** Sec. “SPHEREx Forecast”; Sec. “Systematics and Robustness”; Sec. “Decision Thresholds”.

The manuscript violates its own analysis hierarchy by mixing a bispectrum forecast, an SDB Fisher forecast, and a joint \((\fnl,n_{\fnl})\) SDB analysis as if they were directly comparable. It also reports different significance numbers for the same physical signal depending on which branch of the analysis is being emphasized, without a single declared primary observable and null model.

**Fix:** Choose one primary cosmological null and one systematics-preserving null, then state which observable owns the headline forecast. Everything else should be explicitly labeled a diagnostic or cross-check, not co-equal evidence.

## PAPER-PER-B5 — MAJOR

**Section:** Sec. “The Matter-Bounce Bispectrum Benchmark”; Appendix A.1.

The citation forensics are not clean enough for publication as written: the manuscript cites and interprets several papers in ways that appear fused or overextended, especially around the Cai vs. Li–Brandenberger factor-of-two story, and the title/venue metadata is not demonstrated from the cited sources themselves. The paper also asserts exact agreement on benchmark values and “operator-algebra closure” while simultaneously admitting it does not independently re-derive the full in-in integrals.

**Fix:** Verify every cited claim against the actual source text, not just secondary summaries, and separate “published in paper X” from “inferred by us.” If the full derivation is not reproduced, say so plainly and avoid stating that the citation chain is conclusively closed.

## PAPER-PER-B6 — minor

**Section:** Data and Code Availability; Conclusion.

The manuscript contains a stale release tag mismatch: it advertises `v1.7.26-paper2` in the availability section while the body is labeled `v1.7.37`. That is not a scientific blocker by itself, but it is exactly the kind of version-history inconsistency that undermines traceability.

**Fix:** Replace all internal release tags with one current, externally visible version identifier. If the paper is being submitted, remove repository branch names and keep only the public archive location and immutable tag.
