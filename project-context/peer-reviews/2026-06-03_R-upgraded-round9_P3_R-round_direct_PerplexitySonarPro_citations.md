# P3 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-03_R-upgraded-round9
**Wall time**: 21.7s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=79585, completion=1652, total=81237, search_context_size=low, cost={'input_tokens_cost': 0.23875, 'output_tokens_cost': 0.02478, 'request_cost': 0.006, 'total_cost': 0.26953}

---

## PAPER-PER-B1 – Overstated NANOGrav Bayes-factor claim vs literature

**Location:** §5 (Cosmological Applications), §\ref{sec:nanograv}, Appendix \ref{app:pta_mcmc} (discussion of Savage–Dickey Bayes factors and “decisive” preference for matter bounce over SMBHB).

**Issue:** The paper quotes very large Bayes factors favoring a matter-bounce spectral index (γ=3) over SMBHB indices (γ≈13/3) using a custom Savage–Dickey calculation on the NG15 free-spectrum KDE product, and treats this as “decisive” discrimination. This goes well beyond NANOGrav’s own 15yr analyses, which explicitly *do not* find such a strong, model-independent exclusion of SMBHB and treat SMBHB as a natural explanation among several (cosmic strings, new physics, etc.). The claimed \(B_{\rm matter-bounce/SMBHB} \sim 7\times10^3\) is therefore not supported by the primary NG15 analysis papers and risks overstating what can be drawn from the KDE product alone.

**Fix:** Recast this section as an *illustrative, highly prior-dependent* toy application, clearly stating that (a) NANOGrav has *not* reported such decisive evidence against SMBHB, (b) the quoted Bayes factors depend strongly on the author’s chosen priors and single-dataset, 1‑/2‑parameter reduction, and (c) these numbers must not be interpreted as a robust model comparison between SMBHB and bounce scenarios. Remove “decisive” language and align with NANOGrav’s own, more cautious, conclusions.


## PAPER-PER-M1 – Mis-cited / incomplete references for GR projection-effects discussion

**Location:** §\ref{sec:pathc_caveats} caveat (e) (“GR projection effects on multi-tracer \(f_{\rm NL}\) Fisher”).

**Issue:** The text attributes the need for deterministic GR projection modelling to “Yoo et al. 2009, Bonvin & Durrer 2011, Challinor & Lewis 2011 (DiDio et al. 2013)” but there are no corresponding bibliography entries for these works; the bib only includes general cosmology / PNG references and the Foreman‑Mackey emcee paper.[4] The named GR-lightcone references are standard and should be cited accurately (e.g. Yoo+2009, Bonvin & Durrer 2011, Challinor & Lewis 2011, Di Dio+2013) with correct journal metadata.

**Fix:** Add proper bib entries for all GR-projection references named in the text, with correct authors, titles, journals, years, and arXiv IDs; ensure the in-text citations match those entries and are not just parenthetical names without corresponding bibliography records.


## PAPER-PER-M2 – “Heinrich+2024 σ₍fNL₎≈0.7” anchor not obviously traceable to cited paper

**Location:** Introduction (first page of §1) and §5 (multi-tracer Fisher discussion), where Heinrich et al. 2023/2024 is cited as giving a “bispectrum-only forecast σ_{fNL}≈0.7 for SPHEREx”.

**Issue:** The only Heinrich et al. reference described in the comment block is Heinrich 2023/2024 JCAP arXiv:2311.13082 (SPHEREx multi-tracer bispectrum). The text uses a specific σ(fNL)≈0.7 number as the “headline external benchmark” but does not show exactly where that value comes from in Heinrich et al.; without a precise table/figure mapping, it is hard for a reader to verify that 0.7 is directly supported (as opposed to being an approximate read-off from a figure or for a slightly different survey configuration).

**Fix:** Add an explicit citation to the exact table/figure/equation in Heinrich et al. that yields σ(fNL)≈0.7 for the configuration used as a benchmark, and clarify if the 0.7 is (i) an interpolated or configuration-specific value or (ii) the headline result of that paper. If it is an approximate or configuration-dependent value, state that explicitly (e.g. “≈0.7 for the fiducial SPHEREx-like configuration in Fig. X of Heinrich et al.”).


## PAPER-PER-m1 – Ambiguous reference to Foreman‑Mackey “emcee” paper

**Location:** Appendix \ref{app:pta_mcmc}, paragraph “Sampler.” Bibliography entry “Foreman-Mackey 2013” (emcee: The MCMC Hammer).

**Issue:** The description of the sampler cites emcee and attributes it to Foreman‑Mackey et al. 2013, which is correct, but the bib entry in the LaTeX fragment is slightly informal (“PASP 125, 306 (2013), arXiv:1202.3665”) and there is no explicit mention that this is the “emcee: The MCMC Hammer” paper as on arXiv:1202.3665.[4] This makes cross-checking slightly harder for readers who look for “emcee” by name.

**Fix:** Ensure the bibliography entry for Foreman‑Mackey et al. includes the full paper title “emcee: The MCMC Hammer” and the correct journal citation (Publ. Astron. Soc. Pac. 125, 306 (2013), arXiv:1202.3665), matching the arXiv and journal metadata.[4]


## PAPER-PER-m2 – Nomenclature around “Heinrich+2024” vs JCAP 2024 paper

**Location:** Version-history comment block and Introduction around references to Heinrich+2023 / Heinrich+2024.

**Issue:** The comment block describes Heinrich2023 as “JCAP 2024 arXiv:2311.13082 (SPHEREx multi-tracer bispectrum)” and then refers in the body to “Heinrich+2024” as the anchor. That JCAP paper is 2024 in volume/date but often cited as Heinrich et al. 2023 (arXiv year); this mixed “2023” vs “2024” labelling can confuse readers trying to look up the reference.

**Fix:** Standardize the citation throughout to a single year label (e.g. “Heinrich et al. (2024), JCAP, arXiv:2311.13082”) and ensure the bib entry uses that same year; in the text, avoid alternating “Heinrich+2023” and “Heinrich+2024” for the same work.


## PAPER-PER-n1 – Small arXiv-ID formatting nit

**Location:** Comment block near the top (Perplexity Sonar Pro R-round notes), where Cai:2009fn is referenced.

**Issue:** The paper consistently refers to the matter-bounce non-Gaussianity source as Cai:2009fn (JCAP 0905:011), which is standard INSPIRE-style, but there is no explicit arXiv ID (arXiv:0903.0631) in the bib entry snippet shown, making it slightly less convenient to locate for readers outside HEP/Inspire.

**Fix:** In the bibliography entry for Cai et al. 2009 (JCAP matter-bounce non-Gaussianity), add the explicit arXiv identifier (arXiv:0903.0631) alongside the JCAP citation so that both ADS/arXiv users and HEP/Inspire readers can find it unambiguously.
