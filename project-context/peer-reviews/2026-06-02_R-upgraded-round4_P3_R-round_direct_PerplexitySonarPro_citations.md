# P3 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round4
**Wall time**: 15.2s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=79646, completion=925, total=80571, search_context_size=low, cost={'input_tokens_cost': 0.23894, 'output_tokens_cost': 0.01388, 'request_cost': 0.006, 'total_cost': 0.25881}

---

## PAPER-PER-B1 — Mis-cited Cai 2009 matter-bounce paper

**Issue (Introduction, cosmology paragraph):** The paper cites `Cai:2009fn` as “Cai/Xue/Brandenberger/Zhang 2009 JCAP” with the matter‑bounce non‑Gaussianity prediction \(f_{\rm NL}=-35/8\), but arXiv:0903.0631 is titled “Non‑Gaussianity in a matter bounce” by Y‑F Cai, W. Xue, R. Brandenberger, X. Zhang and is JCAP 0905:011, not just “Cai:2009fn (Cai/Xue/Brandenberger/Zhang 2009 JCAP)” without full metadata.[1]  

**Fix:** In the bib entry and text, give the correct full reference (journal, volume, page) and ensure the arXiv ID and author list for Cai et al. 2009 JCAP 0905:011 (“Non‑Gaussianity in a matter bounce”) are explicit and consistent everywhere.

---

## PAPER-PER-M1 — Heinrich et al. 2023/2024 metadata inconsistency

**Issue (Sec. 1, cosmology paragraph and multiple later references):** The manuscript alternates between “Heinrich et al. 2023” and “Heinrich+2024” while anchoring to a single SPHEREx multi‑tracer bispectrum paper with \(\sigma_{f_{\rm NL}}\approx 0.7\), but the real paper is Heinrich et al., JCAP 2024 (arXiv:2311.13082), not a 2023 journal publication.[2]  

**Fix:** Normalize all references to this work as “Heinrich et al. (2024), JCAP, arXiv:2311.13082” (or equivalent) and remove the mixed 2023/2024 dating so the bib metadata matches the actual publication.

---

## PAPER-PER-M2 — SPHEREx white paper citation details

**Issue (Introduction, SPHEREx forecast):** The SPHEREx citation is given generically as “SPHEREx 2014” and “SPHEREx satellite” without clear bibliographic detail, but the canonical source is the Doré et al. 2014 SPHEREx mission white paper (arXiv:1412.4872).[3]  

**Fix:** Update the SPHEREx reference to “Doré et al. (2014), ‘Cosmology with the SPHEREx All‑Sky Spectral Survey’, arXiv:1412.4872” and ensure the bib entry carries the correct author list, title, year, and arXiv ID.

---

## PAPER-PER-m1 — NANOGrav KDE dataset citation precision

**Issue (Sec. 5 & Appendix PTA-MCMC):** The NANOGrav KDE free‑spectrum dataset is cited only by Zenodo DOI “8060824” without mentioning that it is the NG15 GWB free‑spectrum KDE release accompanying Agazie et al. 2023 ApJL 951 L8.[4]  

**Fix:** Clarify in the text and bib that the Zenodo DOI corresponds to the NANOGrav 15‑year free‑spectrum KDE data product associated with Agazie et al. (2023, ApJL 951 L8) and add a standard paper citation for that journal article alongside the dataset DOI.

---

## PAPER-PER-n1 — Sesana 2016 citation wording

**Issue (Sec. 5, PTA spectral index discussion):** The SMBHB spectral index is attributed to “Sesana 2016, Burke-Spolaor 2019” but the actual Sesana et al. 2016 paper is about selection bias in dynamically measured SMBH samples (MNRAS 463 L6) and not a primary PTA spectral‑index derivation.[5]  

**Fix:** Either (a) rephrase to say these works are used for *amplitude/astrophysical population priors* rather than for the spectral‑index prediction, or (b) replace/add a citation to a PTA‑specific SMBHB background modeling paper that explicitly gives the \(\gamma=13/3\) spectral index.
