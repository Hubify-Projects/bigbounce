# P5 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round4
**Wall time**: 8.8s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=42073, completion=921, total=42994, search_context_size=low, cost={'input_tokens_cost': 0.12622, 'output_tokens_cost': 0.01382, 'request_cost': 0.006, 'total_cost': 0.14603}

---

## PAPER-FOR-1 — **BLOCKER**  
**Section:** `\bibitem{DESIVAST2025}` and every in-text DESIVAST citation  
**Issue:** The bibliography metadata for DESIVAST is still fused/incorrect: the paper text names `Rincon et al. 2025, ApJ 982, 38`, but the draft header/comments show prior confusion about author tagging, and the current item still needs explicit verification against arXiv/ADS/publisher because this citation is load-bearing for the paper’s “primary analysis” claim.  
**Fix:** Re-check the arXiv entry `2411.00148` and ADS record line-by-line, then lock the exact author list, title casing, journal venue, volume, page/article number, and DOI in the bibitem. Do not keep any internal draft commentary about prior metadata corrections in the submission version.

## PAPER-FOR-2 — **MAJOR**  
**Section:** `\bibitem{TWebDESI2026}` and `\S\ref{sec:tweb_concurrent}`  
**Issue:** The paper states `arXiv:2604.02463`, title, authors, and “submitted to MNRAS” status, but this is a classic fused-metadata risk point and the manuscript uses it for comparative claims about V-Web vs T-Web volume fractions. One wrong arXiv ID or title/author mismatch would contaminate multiple downstream assertions.  
**Fix:** Verify the arXiv record and the publisher/preprint metadata directly, then ensure the bibitem and prose match exactly. If the paper is still a preprint, keep it labeled as such consistently everywhere and remove any language that implies external validation.

## PAPER-FOR-3 — **MAJOR**  
**Section:** `\bibitem{ASTRADESI2026}`, `\S\ref{sec:tweb_concurrent}`, `\S\ref{sec:astra_per_object}`  
**Issue:** The ASTRA citation is used as a key external comparator, but the manuscript mixes title, conference-like scope, Zenodo identifier, arXiv ID, and catalog description. That is a high-risk place for title/ID/author fusion, especially because the paper makes strong claims about EDR scope and per-object overlap.  
**Fix:** Verify the arXiv and ADS records directly and make the bibitem a one-to-one copy of the real metadata. If the Zenodo artifact is supplementary rather than the publication itself, label it explicitly as such and avoid implying the DOI/Zenodo record is the same object as the paper.

## PAPER-FOR-4 — **MAJOR**  
**Section:** `\bibitem{Shamir2022DESI}` and `\S\ref{sec:discussion}`  
**Issue:** The draft claims the title/venue/arXiv/DOI metadata are verified, but this is exactly the sort of citation that has already been confabulated in prior iterations. Because the discussion uses it to benchmark amplitude claims, any metadata error is consequential.  
**Fix:** Confirm the arXiv page and publisher record independently, then keep only the exact title, journal, volume, page, DOI, and arXiv ID that appear there. Remove any redundant prose about prior correction history from the final manuscript.

## PAPER-FOR-5 — **minor**  
**Section:** `\bibitem{Hahn2007}`, `\bibitem{Hoffman2012}`, `\bibitem{Cautun2014}`  
**Issue:** The cosmic-web method citations are plausible, but the manuscript gives no explicit evidence that the author lists and journal metadata were checked against ADS/publisher sites in this round. These are foundational citations for the V-Web pipeline.  
**Fix:** Do a direct metadata audit and ensure the bibitems exactly match the published records. If any author list is truncated, make it journal-compliant and consistent across text and bibliography.

## PAPER-FOR-6 — **minor**  
**Section:** `\bibitem{Planck2018cosmoparams}`  
**Issue:** The Planck citation is standard, but the manuscript uses it operationally for comoving-distance conversion, so a wrong article number or collaboration label would be easy to miss.  
**Fix:** Verify the arXiv and A&A metadata once more and ensure the citation is the exact “VI. Cosmological parameters” record, not a nearby Planck 2018 paper.
