# P5 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-03_R-upgraded-round9
**Wall time**: 7.8s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=42590, completion=701, total=43291, search_context_size=low, cost={'input_tokens_cost': 0.12777, 'output_tokens_cost': 0.01052, 'request_cost': 0.006, 'total_cost': 0.14428}

---

## PAPER-PER-M1

**MAJOR** — `Abstract`, `§DESIVAST-anchored void cross-validation`, `bibitem{DESIVAST2025}`. The paper flips between **Rincón et al. 2025** and a DESI-void release claim, but the cited source is real and the metadata in the text is now internally consistent; no blocker here. The issue is that the manuscript still presents DESIVAST as both a void catalog and a broader DR1 environment anchor in ways that blur scope.

Fix: Keep DESIVAST described strictly as a **void catalog** and remove any wording that implies it is a general full-DR1 cosmic-web classifier. Anchor the primary claim only to the void/non-void cross-check.

## PAPER-PER-M2

**MAJOR** — `Intro`, `Discussion`, `bibitem{TWebDESI2026}`. The arXiv ID **2604.02463** and the cited title/authors are a real preprint match; the bib metadata is not fabricated. However, the manuscript’s wording oscillates between “submitted to MNRAS,” “preprint,” and “concurrent literature,” which is fine, but it should not imply peer review.

Fix: Standardize the citation language to **preprint** everywhere and remove any residual phrasing that could be read as published or peer-reviewed validation.

## PAPER-PER-M3

**minor** — `§Data`, `§Introduction`, `bibitem{Shamir2022DESI}`. The Shamir 2022 citation is correctly identified as **MNRAS 516, 2281 (2022)** with **arXiv:2208.13866**; the earlier confabulated title is gone. No metadata regression remains in the cited bibliography entry.

Fix: None required beyond keeping the correct title/venue pairing unchanged.

## PAPER-PER-M4

**minor** — `§V-Web cosmic-web classification`, `§Discussion`, `bibitem{Hahn2007}`, `bibitem{Hoffman2012}`, `bibitem{Cautun2014}`. These are real papers and the author/venue/arXiv metadata are broadly correct; no fused metadata detected. The only issue is stylistic: the manuscript uses these foundational references as if they establish the exact pipeline configuration used here, which they do not.

Fix: Clarify that these citations support the **general V-Web formalism**, not the specific implementation choices in this paper.

## PAPER-PER-M5

**minor** — `§Relation to Paper IV`, `bibitem{golden_chirality_2026}`, `bibitem{golden_fnl_2026}`. These are internal companion artifacts with no arXiv IDs yet, and the manuscript labels them as such. That is acceptable, but they are not externally verifiable literature and should not be treated like normal references.

Fix: Keep the “internal companion artifact; no arXiv identifier yet” labeling explicit wherever these are first cited.

## PAPER-PER-M6

**nit** — `§Limitations`, `§appendix`. The bibliography and in-text cites for Alexander & Yunes 2009 and Lue et al. 1999 are real and correctly paired to the cited operator discussion. No citation-chain forensic error found.

Fix: None.
