# P1B_v1B011 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_0830pt_P1B_v1B011_R6_R-round_real
**Wall time**: 11.1s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=13793, completion=913, total=14706

---

## PAPER-PER-B1 — BLOCKER
**Section:** Abstract, Sec. 6, bibliography citations  
**Issue:** The paper cites `Eskilt2022`, `Eskilt2022b`, `DiegoPalazuelos2022`, and `DiegoPalazuelos2025`, but the text does not provide enough bibliographic metadata to verify that these are real, correctly matched papers. Given the repeated use of these citations as load-bearing support for birefringence values, this is a citation-chain blocker until each key claim is tied to a verifiable title/arXiv-ID/journal record.  
**Fix:** Add a complete reference audit table for every cited birefringence paper: exact title, first author, venue, year, arXiv ID/DOI, and the specific quoted result.

## PAPER-PER-B2 — MAJOR
**Section:** Sec. 3, Table `verification`, Sec. 5 `crosspaper`  
**Issue:** The manuscript mixes convergence states and sample accounting in a way that is internally unstable: the same proxy run is described as having 309,789 frozen samples, a separate 114,992-sample Planck-only run, and convergence claims tied to multiple snapshots. The model-comparison block is simultaneously removed, deferred, and said to be unblocked by convergence, which makes the provenance of the reported posterior numbers unclear.  
**Fix:** Split the chain inventory into a single canonical status table with one row per chain, one frozen/ongoing label, one acceptance count, and one convergence metric source. Then state explicitly which posterior summaries are computed from which exact frozen chains.

## PAPER-PER-B3 — MAJOR
**Section:** Sec. 4 `Data Methods: CMB E-B Analysis`  
**Issue:** The NaMaster validation is presented as a pipeline check, but the text blurs physical inputs and validation assumptions: Commander is described as a foreground-cleaned CMB-only product, yet the analysis claims foreground cleaning is essential for breaking the \(\beta\)–\(\alpha\) degeneracy. That tension makes the claimed scope boundary look under-justified.  
**Fix:** State explicitly whether the validation uses a sky-realistic component-separated map or a synthetic CMB-only map, and separate the degeneracy argument from the pipeline-recovery test. If the Commander map is only a proxy, say so unambiguously and remove any implication that it tests the real degeneracy-breaking mechanism.

## PAPER-PER-B4 — minor
**Section:** Sec. 6 `Spectator-ALP Consistency Check`  
**Issue:** The birefringence numerics appear overfit to the target result: the paper gives several mutually adjusted values for \(\beta\), \(C_{a\gamma}\), \(\Delta\phi/f_a\), and the combined product, but the derivation is not shown cleanly enough to verify that the final \(0.342^\circ\) consistency is non-circular.  
**Fix:** Add a short derivation chain from the ALP equation of motion to the quoted \(\beta\) values, with intermediate numerical steps and the exact parameter choices used in the MCMC and “model-independent” fit.

## PAPER-PER-B5 — MAJOR
**Section:** Sec. 5 `Model-comparison statistics`  
**Issue:** The paper says the \(\chi^2_{\rm eff}\)/AIC/BIC/\(\ln B\) row was removed because it was not reproducible, but then continues to discuss the corresponding conclusions and future recomputation as if those statistics still support the narrative. That is a metadata-to-conclusion leak.  
**Fix:** Delete all interpretive statements that depend on the removed statistics, or replace them with a single sentence saying no model-comparison inference is being made until the recomputation is complete.

## PAPER-PER-B6 — nit
**Section:** Abstract, Sec. 3, Sec. 7  
**Issue:** Versioning and status labels are noisy and repetitive: “converged,” “frozen,” “ongoing,” “unblocked,” and multiple version numbers are repeated across several sections. This makes the paper harder to audit, not easier.  
**Fix:** Consolidate all chain/version status language into one compact status table and trim repeated status prose elsewhere.
