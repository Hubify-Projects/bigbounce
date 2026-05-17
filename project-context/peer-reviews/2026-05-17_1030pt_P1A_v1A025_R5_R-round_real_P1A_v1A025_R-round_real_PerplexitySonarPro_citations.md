# P1A_v1A025 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-17_1030pt_P1A_v1A025_R5_R-round_real
**Wall time**: 10.5s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=27694, completion=746, total=28440

---

## PAPER-PER-B1 — BLOCKER

**Section:** Abstract / Sec. 4 / Sec. 12 / Sec. 15  
**Issue:** The paper cites a large number of external works, but the bibliography is not shown, and the in-text claims about arXiv IDs/titles/authors/venues are not verifiable from the source alone. That is a citation-forensics blocker because the task explicitly requires checking whether cited papers actually say what is claimed and whether metadata are fused or correct.  
**Fix:** Provide the full reference list and verify every cited item against arXiv/publisher/ADS records before submission; flag any citation whose title, arXiv ID, authors, or venue do not match exactly.

## PAPER-PER-B2 — MAJOR

**Section:** Abstract; Sec. 4.2 / Route 2  
**Issue:** The manuscript alternates between claiming Route 2 is “closed” and admitting it was previously “deferred,” but the text still contains internal status churn and cross-version references that look like unresolved patch notes rather than final prose. That weakens the closure claim and creates regression risk in the audit trail.  
**Fix:** Replace all version-history prose with a single final status statement, and remove any language implying the route was ever still deferred in the current version.

## PAPER-PER-B3 — MAJOR

**Section:** Abstract; Sec. 2.4; Sec. 12; Sec. 15  
**Issue:** The \(0.73\sigma\) LiteBIRD-vs-Planck/ACT tension is computed correctly in one place, but the manuscript still carries multiple nearby statements that invite the naive \(0.27/0.03\) interpretation. That is a consistency hazard in an adversarial referee read.  
**Fix:** Keep only one explicit comparison formula and state unambiguously that the model-discrimination significance uses the combined uncertainty, not the LiteBIRD forecast alone.

## PAPER-PER-B4 — MAJOR

**Section:** Sec. 1; Sec. 4; Sec. 10; Sec. 13  
**Issue:** The propagation-tail / e-fold discussion is repeated in multiple forms, and some phrasing still risks reintroducing the old “\(e^{N_{\rm tot}}\sim e^{30}\)” style of confusion by mixing physical and comoving scaling in the same sentence. The intended closure is not cleanly isolated.  
**Fix:** Consolidate the e-fold argument into one canonical derivation, then delete all duplicate or semi-equivalent restatements elsewhere in the paper.

## PAPER-PER-B5 — minor

**Section:** Sec. 9; Table 1; Appendix B  
**Issue:** The manuscript explicitly says B8 and B14 are not logically independent, but they are still counted in the historical 14-entry catalog. That is acceptable, but it should be labeled more sharply to avoid apparent double counting.  
**Fix:** Add one sentence stating that the catalog has 14 historical entries but only 13 independent barriers, with B8 subsumed by B14.

## PAPER-PER-B6 — nit

**Section:** Abstract; Sec. 4.4; Sec. 15  
**Issue:** The prose is overloaded with internal versioning, adversarial-review metadata, and execution-trace language. It reads like an audit log rather than a paper, which will irritate referees even if the physics is sound.  
**Fix:** Strip the meta-review language from the manuscript body and keep only the final scientific claims.
