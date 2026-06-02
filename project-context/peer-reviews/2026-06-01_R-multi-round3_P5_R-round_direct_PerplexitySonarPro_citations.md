# P5 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-multi-round3
**Wall time**: 7.1s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=33364, completion=991, total=34355, search_context_size=low, cost={'input_tokens_cost': 0.10009, 'output_tokens_cost': 0.01486, 'request_cost': 0.006, 'total_cost': 0.12096}

---

## Finding 1 — **PAPER-PER-B1** — **MAJOR**
**Line/section:** Bibliography: `\bibitem{DESIVAST2025}` and §`sec:tweb_compare` / abstract robustness claims.  
**Issue:** The DESIVAST citation is internally fused with a likely wrong venue/arXiv pair. The paper text calls it *ApJ 982, 38 (2025)* and `arXiv:2411.00148`; that metadata needs direct verification against arXiv/ADS/publisher because this is exactly the kind of title/venue fusion that often drifts in LLM-generated bibliographies.  
**Fix:** Re-verify the title, author list, journal venue, year, and arXiv ID against ADS or the publisher record, then replace the bibitem with the exact canonical metadata.

## Finding 2 — **PAPER-PER-B2** — **MAJOR**
**Line/section:** Bibliography: `\bibitem{TWebDESI2026}` and §`sec:tweb_compare`.  
**Issue:** This citation is high-risk: the manuscript asserts a submitted MNRAS DESI DR1 T-Web paper with `arXiv:2604.02463`, and the author list/title must be checked against arXiv and the paper’s actual metadata. If any one of title, authors, or arXiv ID is off, the whole “independent contemporaneous DR1 cosmic-web analysis” comparison becomes citation-fused.  
**Fix:** Verify the arXiv record directly and make the bibitem match it character-for-character, including author order and exact title capitalization/subtitle.

## Finding 3 — **PAPER-PER-B3** — **MAJOR**
**Line/section:** Bibliography: `\bibitem{ASTRADESI2026}` and §`sec:tweb_compare` / `sec:astra_per_object`.  
**Issue:** Same failure mode: the paper leans on ASTRA as a published/citable external DESI EDR environment catalog, but the bibitem is only a bare arXiv entry. That is acceptable only if the title and authors are exact; otherwise this is a fabricated-or-fused reference contaminating multiple claims about EDR overlap and BGS-anchored calibration.  
**Fix:** Verify the arXiv metadata and ensure the citation uses the exact published/preprint title, full author list, and correct arXiv identifier.

## Finding 4 — **PAPER-PER-B4** — **MAJOR**
**Line/section:** Bibliography: `\bibitem{Shamir2022DESI}` and Discussion §`Comparison to Shamir~2022 DESI Legacy`.  
**Issue:** The manuscript cites Shamir 2022 as *MNRAS 516, 2281 (2022), arXiv:2208.13866* and uses it as an amplitude benchmark. That specific bibliographic pairing must be checked; if the journal page, title, or arXiv mapping is off, the paper’s comparison claims are built on a broken citation.  
**Fix:** Verify against arXiv and the publisher record, then correct the bibitem and any downstream comparison language to the verified metadata.

## Finding 5 — **PAPER-PER-B5** — **minor**
**Line/section:** §`sec:data`, `\url{https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/}` and related `zall-pix-iron.fits` provenance.  
**Issue:** The text treats `iron` as a DR1 spectroscopic-reduction tag and implicitly equates it with the canonical DR1 zall catalog path. That may be right, but the provenance is underspecified and easy to misread as a file-name invention if the exact DR1 directory structure is not confirmed in the paper.  
**Fix:** Add one short sentence citing the DESI DR1 release docs or archive path conventions to show that the filename/path is canonical, not script-specific.

## Finding 6 — **PAPER-PER-B6** — **nit**
**Line/section:** Multiple bibliographic in-text assertions, especially `Hahn2007`, `Hoffman2012`, `Cautun2014`, `Planck2018cosmoparams`.  
**Issue:** The manuscript relies on standard cosmic-web citations, but the review target is citation forensics: these entries should still be spot-checked for exact article titles/venues/arXiv IDs. Nothing here looks blocker-grade from the paper text alone, but this is where fused metadata errors often hide.  
**Fix:** Do a final metadata audit against ADS/arXiv for all core method citations and normalize the bibitems to canonical records.
