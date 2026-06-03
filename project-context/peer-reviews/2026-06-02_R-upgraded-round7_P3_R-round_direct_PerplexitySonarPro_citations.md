# P3 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round7
**Wall time**: 18.5s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=79642, completion=1549, total=81191, search_context_size=low, cost={'input_tokens_cost': 0.23893, 'output_tokens_cost': 0.02324, 'request_cost': 0.006, 'total_cost': 0.26816}

---

## PAPER-PER-B1 — Mis-cited “Heinrich2023” anchor forecast

**Section:** Intro, cosmology paragraph (near “Heinrich \etal~\cite{Heinrich2023} … Heinrich+2024 σ_fNL ≈ 0.7”).  

**Issue:** The paper treats “Heinrich2023” as a JCAP paper with a “Heinrich+2024” σ_fNL ≈ 0.7 bispectrum-only SPHEREx forecast, but the real paper is Heinrich, Doré & Krause “Measuring \(f_{\rm NL}\) with the SPHEREx Multi-tracer Redshift Space Bispectrum” JCAP 02 (2024) 074, arXiv:2311.13082, i.e. 2024, not 2023, and there is no separate “Heinrich+2024” paper.[1]  

**Fix:** Rename the citation key to something like `Heinrich2024` and adjust all prose to refer to a 2024 JCAP paper (and drop the “Heinrich+2024” phrasing unless there really is a second, distinct work).


## PAPER-PER-B2 — Mis-framed “Münchmeyer et al. 2019 consensus” comparison

**Section:** Intro, cosmology paragraph (internal Fisher σ_fNL ≈ 0.07–0.12 “3–10× tighter than the Münchmeyer et al. consensus σ_fNL ≈ 0.4–0.9 for SPHEREx-class surveys”).  

**Issue:** Munchmeyer et al. 2019 (Phys. Rev. D 100, 083508, arXiv:1810.13424) forecasts constraints from kSZ tomography with a CMB Stage‑4–like experiment, not SPHEREx-like galaxy surveys.[2] The phrasing “consensus σ_fNL ≈ 0.4–0.9 for SPHEREx-class surveys” incorrectly attributes a SPHEREx-specific consensus bound to this paper.  

**Fix:** Rephrase to attribute correctly, e.g. “tighter than representative Stage‑4 / LSS forecasts such as Munchmeyer et al. (2019)” or replace with an actually SPHEREx-specific forecast if you want a SPHEREx comparison.


## PAPER-PER-M1 — Matter-bounce reference set incomplete / slightly off

**Section:** Intro and §5/§App PTA paragraphs citing Wands2010, Cai:2009fn, Quintin2014, Cai2014, WilsonEwing2012 as the core matter-bounce \(f_{\rm NL}=-35/8\), \(n_T=2\) set.  

**Issue:** The primary non‑Gaussianity calculation with \(f_{\rm NL}=-35/8\) in a matter bounce is indeed Cai et al. JCAP 05 (2009) 011, arXiv:0903.0631, which you cite as `Cai:2009fn` and use correctly.[3]  Wands 2010 is a general NG review, Cai 2014 is a review, and Quintin 2014 / Wilson‑Ewing 2013 are specific model developments; none of these introduce the \(-35/8\) value or the precise PTA \(\gamma=3\) mapping.  

**Fix:** Make `Cai:2009fn` the explicit primary source for \(f_{\rm NL}=-35/8\) and for the blue \(n_T=2\) / \(\gamma=3\) mapping, and rephrase the other bounce citations as “for reviews / related bounce implementations” rather than as if they jointly established the specific numerical predictions.


## PAPER-PER-M2 — NANOGrav data / likelihood citation chain only partially explicit

**Section:** NANOGrav paragraph (“NANOGrav 15-year HD-correlated free-spectrum KDE likelihood release (Zenodo 10.5281/zenodo.8060824)”).  

**Issue:** The primary NANOGrav 15‑yr GWB detection paper is Agazie et al., ApJL 951 L8 (2023), arXiv:2306.16213, and the free‑spectrum KDE likelihood is indeed on Zenodo under DOI 10.5281/zenodo.8060824, credited to the NANOGrav collaboration.[4][5] The text cites NANOGrav generally but never gives an explicit bib entry for the main 15‑yr paper, and it is ambiguous whether the bib includes an entry pointing specifically at the Zenodo free‑spectrum artifact.  

**Fix:** Ensure the bibliography has (i) a standard `NANOGrav2023` entry for Agazie et al. ApJL 951 L8 (2023), and (ii) a separate data/Zenodo entry keyed to the 10.5281/zenodo.8060824 free‑spectrum KDE chain, which is what is actually used for the KDE likelihood analysis.


## PAPER-PER-m1 — SPHEREx mission reference slightly off

**Section:** Intro (“SPHEREx satellite~\cite{SPHEREx2014}”).  

**Issue:** The main SPHEREx mission white paper is Doré et al., “Cosmology with the SPHEREx All-Sky Spectral Survey”, arXiv:1412.4872, often cited as 2014, but there was no 2014 refereed journal SPHEREx paper; the official mission paper appears in 2016 ApJ or SPIE proceedings depending on version.[6] If your bib entry claims a specific journal volume/year mismatched to 2014, that would be fused metadata. I can’t see the `.bib` here, so this is a risk flag rather than a confirmed clash.  

**Fix:** Check your `SPHEREx2014` bib entry against arXiv:1412.4872 and the actual published venue; ensure year, journal, and authors match exactly, or just treat it explicitly as “arXiv:1412.4872 (2014)” without an invented journal citation.


## PAPER-PER-n1 — Minor bounce/PTA naming consistency nit

**Section:** NANOGrav section and cosmology discussion.  

**Issue:** You refer to “Heinrich+2024 σ_fNL ≈ 0.7 bispectrum-only forecast as the headline external benchmark” and separately to the PTA “new‑physics companion paper Afzal et al. 2023 NewPhys” in the appendix text, but only the Heinrich paper is actually central to your f_NL forecast, and Afzal et al. (NANOGrav new‑physics constraints) is not explicitly cited with a standard bib key. This is a consistency/documentation nit rather than a scientific error.  

**Fix:** Normalize nomenclature: call the SPHEREx paper “Heinrich et al. (2024)” consistently, and add an explicit bib entry for Afzal et al. (NANOGrav 15‑yr new-physics paper) if you want to reference it as the multi‑model comparison, or remove the shorthand “Afzal2023NewPhys” text if not needed.
