# P3 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-05-29_R-direct-v1
**Wall time**: 26.8s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=74133, completion=1842, total=75975, search_context_size=low, cost={'input_tokens_cost': 0.2224, 'output_tokens_cost': 0.02763, 'request_cost': 0.006, 'total_cost': 0.25603}

---

## PAPER-PER-B1 — Incorrect Heinrich et al. reference and claims

**Section:** Introduction, para starting “The quasi-matter bounce model predicts… Heinrich et al. [Heinrich2023] (anchored to the Heinrich+2024 σfNL ≈ 0.7 … internal Fisher … 0.07–0.12 … 3–10× tighter than Münchmeyer et al. consensus 0.4–0.9).  

**Issue:** The cited paper “Heinrich et al. 2023” (arXiv:2311.13082, *“Measuring \(f_{\rm NL}\) with the SPHEREx Multi-Tracer Redshift Space Bispectrum”*) indeed forecasts SPHEREx constraints, but:
- There is no separate “Heinrich+2024 σfNL ≈ 0.7” paper; 0.7 is the main result of that same 2023 paper, not of a later 2024 work.  
- The claimed “internal Fisher diagnostic computation gives σfNL ≈ 0.07–0.12 … 3–10× tighter than the Münchmeyer et al. consensus σfNL ≈ 0.4–0.9” is not in Heinrich et al.; those numbers are this paper’s own internal calculation, but the sentence is written in a way that can be read as if Heinrich+ reported them.  
- Münchmeyer et al. (arXiv:1810.13424) give SPHEREx-like σ(fNL) forecasts of order 0.4–0.5; the “0.4–0.9” range is not directly quoted as such in that paper.

**Fix:**  
Rephrase to: (1) attribute σfNL ≈ 0.7 clearly to Heinrich et al. (2023) itself, not to a non‑existent 2024 paper; (2) explicitly label σfNL ≈ 0.07–0.12 as this work’s *internal* Fisher experiment, not something from Heinrich et al.; (3) if a “0.4–0.9” consensus range is kept, make clear it is an approximate summary of the literature, not a direct citation, or replace with the explicit values actually quoted in Münchmeyer et al.


## PAPER-PER-M1 — Mis-citation / mischaracterization of SPHEREx sensitivity in conclusions

**Section:** Conclusions, bullet 5 (“Projected to SPHEREx survey parameters…the preliminary forecast yields 3–5σ detection significance for the matter-bounce prediction…” citing Heinrich et al. 2023 and SPHEREx 2014).  

**Issue:** Heinrich et al. (arXiv:2311.13082) gives a Fisher σ(fNL) forecast, but does not itself phrase this as a “3–5σ detection of fNL = –35/8” nor as a “range reflecting uncertainty in the systematic degradation budget”; that translation is the author’s own combination of σ ≈ 0.7 with the matter‑bounce amplitude. As written, it is ambiguous whether the 3–5σ range comes from Heinrich et al. or from this paper’s extrapolation.

**Fix:**  
Clarify that the 3–5σ figure is *this work’s* interpretation: e.g. “Using the σ(fNL) ≈ 0.7 forecast of Heinrich et al. (2023) and assuming fNL = –35/8, our own back‑of‑the‑envelope translation corresponds to ≈3–5σ, depending on assumed systematics,” and remove any implication that Heinrich et al. explicitly state this significance range.


## PAPER-PER-M2 — Ambiguous NANOGrav reference and KDE likelihood description

**Section:** Sec. 5 (Cosmological Applications), NANOGrav paragraph; Appendix “PTA MCMC documentation.”  

**Issue:** The paper refers to a “NANOGrav 15-year HD-correlated free-spectrum KDE likelihood release [NANOGrav2023] (Zenodo 10.5281/zenodo.8060824)” and attributes to it a specific KDE-based free-spectrum product. The main NANOGrav 15‑yr paper (Agazie et al. 2023, ApJL 951 L8, arXiv:2306.16213) does not itself present KDE files; separate Zenodo entries exist for free‑spectrum products, but those are typically in “NANOGrav Collaboration” data notes with distinct titles. As written, the single [NANOGrav2023] entry conflates the journal paper with the specific KDE data package (and gives no proper title / authors for the latter).

**Fix:**  
Split this into two citations: one to the main NANOGrav 15‑yr detection paper (Agazie et al., “The NANOGrav 15-year Data Set: Evidence for a Gravitational-wave Background”) and one to the specific Zenodo KDE free-spectrum dataset, with its correct title and collaboration author (e.g. “NANOGrav Collaboration, ‘KDE representations of GWB free spectra,’ Zenodo 10.5281/zenodo.8060824”). Adjust text to make clear the KDE likelihood is from the dataset, not the main paper.


## PAPER-PER-m1 — Incomplete / inaccurate citation for LAMOST DR10

**Section:** Introduction, first paragraph; bibliography entry “LAMOST_DR10”.  

**Issue:** The paper cites “A.-L. Luo et al., ‘The LAMOST Data Release 10,’ Research in Astronomy and Astrophysics, 2024.” At time of writing, official LAMOST DR10 documentation is typically in the form of collaboration data‑release papers or online documentation; there is a Luo et al. series for earlier releases (e.g., DR5, DR7), but I do not find a peer‑reviewed “LAMOST Data Release 10” article in RAA by Luo et al. with that exact title and year. This looks like a projected or inferred reference rather than a verified published paper.

**Fix:**  
Replace with a correct, existing citation: either the latest published LAMOST data‑release paper that actually exists (with accurate title, year, journal) plus a URL/documentation reference for DR10, or, if DR10 is only documented online, cite the official DR10 web documentation instead of a fabricated Luo et al. RAA article. Ensure the bib entry’s title, authors, and venue match a real, locatable source.


## PAPER-PER-m2 — Gaia DR3 citation missing correct primary reference

**Section:** Introduction; bibliography “GaiaDR3”.  

**Issue:** The paper describes “Gaia Data Release 3, Astron. Astrophys. 674, A1 (2023)” but does not give an explicit author string in the bib entry snippet (just “Gaia Collaboration”). The canonical DR3 primary paper is “Gaia Collaboration (Vallenari et al.) 2023, A&A 674, A1, ‘Gaia Data Release 3. Summary of the content and survey properties’.” Omitting “Vallenari et al.” is not strictly incorrect but diverges from the standard form used by the mission and most of the literature.

**Fix:**  
Tighten the bib entry to the standard: “Gaia Collaboration, Vallenari, A., et al., ‘Gaia Data Release 3. Summary of the content and survey properties,’ A&A 674, A1 (2023),” so that readers can locate it unambiguously, matching usual citation practice for Gaia DR3.


## PAPER-PER-n1 — Minor: ambiguous use of “Heinrich+2024” label

**Section:** Introduction and Sec. 5 discussion of σ(fNL) forecasts.  

**Issue:** The text repeatedly refers to “Heinrich+2024 σfNL ≈ 0.7” as the “headline external benchmark,” but the actual cited arXiv entry is the 2023 paper (arXiv:2311.13082), and there is no separate 2024 journal article with different content. Using “+2024” suggests a distinct later work and can confuse readers checking the bibliography.

**Fix:**  
Standardize to “Heinrich et al. (2023)” everywhere and, if you want to emphasize publication year vs. arXiv year, add the actual journal publication year explicitly once (e.g. “Heinrich et al. 2023, published 2024”), making sure it matches the real journal record.
