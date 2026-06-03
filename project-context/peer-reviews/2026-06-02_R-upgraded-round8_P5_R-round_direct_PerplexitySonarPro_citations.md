# P5 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round8
**Wall time**: 9.5s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=42676, completion=964, total=43640, search_context_size=low, cost={'input_tokens_cost': 0.12803, 'output_tokens_cost': 0.01446, 'request_cost': 0.006, 'total_cost': 0.14849}

---

## PAPER-PER-B1 — **major**
**Section:** `\bibitem{DESIVAST2025}` and `\section{DESIVAST-anchored void cross-validation}`  
**Issue:** The paper’s narrative still overstates DESIVAST status as “peer-reviewed DR1 BGS void catalog at low z” in a way that is not safely supported by the citation chain alone. The bibliography entry is for an ApJ paper, but the manuscript leans on a catalog-level authority claim and algorithm counts that must be verified against the paper itself; the current text does not distinguish what is directly in the source paper versus what comes from local files/artifacts.  
**Fix:** Rephrase all DESIVAST claims to explicitly say “according to DESIVAST 2025” and restrict algorithm-count / hole-count / membership assertions to the cited paper or a clearly labeled internal artifact. If any of those counts are not in the paper, move them to a methods note or appendix and stop presenting them as sourced-literature facts.

## PAPER-PER-B2 — **major**
**Section:** `\section{Concurrent-literature DR1/EDR cosmic-web cross-validation}` and `\bibitem{TWebDESI2026}`  
**Issue:** The manuscript cites `arXiv:2604.02463` as a preprint and then uses it to support tracer-dependent T-Web volume fractions and survey-shell comparisons. This is plausible, but the paper text mixes “current submission,” “contemporaneous independent measurement,” and quasi-confirmatory language without clearly marking that the cited work is not peer reviewed.  
**Fix:** Keep the citation, but downgrade every use to “preprint” or “submitted work,” and remove any phrasing that implies external validation. Make the dependency explicit: the T-Web result is a contemporaneous comparison, not an established literature benchmark.

## PAPER-PER-B3 — **major**
**Section:** `\section{ASTRA EDR per-object cross-validation}` and `\bibitem{ASTRADESI2026}`  
**Issue:** The paper treats ASTRA as a published DESI EDR environment catalog while simultaneously calling it the “closest currently available substitute” for a full-DR1 VAC. That is internally consistent, but the citation chain is fragile: the text claims a Zenodo DOI plus arXiv preprint, yet the manuscript uses ASTRA-derived counts and overlap statistics as if they are already externally authoritative.  
**Fix:** Add one sentence stating that ASTRA is a preprint/early-release product used only as an auxiliary cross-check. Separate “source catalog facts” from “this-work overlap measurements” so readers do not confuse the cited paper’s claims with your derived join results.

## PAPER-PER-B4 — **minor**
**Section:** `\section{Relation to Paper IV}` / `\bibitem{golden_chirality_2026}`  
**Issue:** The manuscript cites Paper IV as “in preparation” and “internal companion artifact,” then repeatedly relies on exact numerical values from it as if they are published literature. That is citation-chain fragile but not necessarily wrong.  
**Fix:** Keep the citation, but label every Paper IV number as an internal/unpublished result imported from a companion manuscript, not as a published external reference. This needs to be explicit in the abstract, methods, and every downstream comparison.

## PAPER-PER-B5 — **minor**
**Section:** `\bibitem{Tempel2014}`  
**Issue:** The Tempel citation metadata looks structurally correct, but the manuscript’s prose says “Tempel+2014 FoF cross-validation on SDSS DR10” while the bibliography entry is a generic A&A catalog paper. The connection is fine, but the paper does not verify that the exact richness bins and sample sizes used here are actually the ones described in Tempel 2014.  
**Fix:** Add a short clause saying the multiplicity-to-environment mapping is your own operationalization on top of Tempel et al. 2014, not a direct quote of the paper’s class scheme.

## PAPER-PER-B6 — **nit**
**Section:** `\bibitem{Hahn2007}`, `\bibitem{Hoffman2012}`, `\bibitem{Cautun2014}`  
**Issue:** These are standard and look correct, but the manuscript uses them as support for a very specific V-Web implementation choice (grid size, smoothing, thresholding) that is not actually supplied by those citations alone.  
**Fix:** Leave the citations, but add a short implementation disclaimer: the cited works justify the V-Web formalism; the numerical pipeline settings are this paper’s chosen instantiation.
