# P3 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-05-29_R-direct-v1b
**Wall time**: 19.2s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=74133, completion=1677, total=75810, search_context_size=low, cost={'input_tokens_cost': 0.2224, 'output_tokens_cost': 0.02516, 'request_cost': 0.006, 'total_cost': 0.25355}

---

## PAPER-PER-B1 — Confused SPHEREx / Heinrich et al. citations

**Location:** Introduction, para 2, lines mentioning “Heinrich et al.” and “Heinrich+2024” around “…multi-tracer methodology of Heinrich et al. [Heinrich2023] (anchored to the Heinrich+2024 σfNL≈0.7 bispectrum‑only forecast…)”.

**Issue:** The text claims a “Heinrich+2024 σ(fNL)≈0.7 bispectrum-only forecast” as headline external benchmark, but the only cited work is Heinrich et al. 2023 (arXiv:2311.13082), which is a multi‑tracer SPHEREx forecast and does not present itself as that specific “2024 bispectrum‑only” benchmark or with σ(fNL)≈0.7 under that label. The year, role (“bispectrum‑only headline”), and precise σ value look like fused / projected metadata rather than a direct claim in any actual paper.

**Fix (BLOCKER):** Either (a) update the citation block to reference the exact, real paper that actually states σ(fNL)≈0.7 as a bispectrum‑only SPHEREx benchmark (correct authors, year, arXiv ID, and venue), or (b) if that work does not exist as described, remove the “Heinrich+2024 … σ≈0.7 bispectrum‑only headline” language and instead clearly say you are *adopting* σ≈0.7 from Heinrich et al. (2023) with a precise quote of what that paper really reports and under what assumptions.


## PAPER-PER-M1 — Ambiguous / likely incorrect “Münchmeyer et al. 2019 consensus σfNL≈0.4–0.9”

**Location:** Introduction, para 2, clause “…3–10× tighter than the Münchmeyer et al. [Munchmeyer2019] consensus σfNL≈0.4–0.9 for SPHEREx‑class surveys…”.

**Issue:** Munchmeyer et al. 2019 (Phys. Rev. D 100, 083508) is about kinetic SZ tomography and forecasts for local PNG with specific survey / tracer assumptions; it is not a community “consensus” document on SPHEREx‑class σ(fNL) nor does it present a 0.4–0.9 range as a named consensus benchmark. The “consensus σ≈0.4–0.9” framing overstates what that single paper represents.

**Fix (MAJOR):** Rephrase this as a direct, attributed comparison to that specific paper, e.g. “3–10× tighter than the σfNL≈0.4–0.9 forecasts found in Munchmeyer et al. (2019) for their kSZ-based configuration”, and drop the “consensus” term unless you add multiple, correctly cited SPHEREx‑class forecast papers that collectively justify that label.


## PAPER-PER-M2 — Matter‑bounce prediction sourcing incomplete / slightly misleading

**Location:** Introduction, para 2, sentence “The quasi‑matter bounce model predicts a strongly constrained local non‑Gaussianity fNL = −35/8 = −4.375 [Wands2010, Cai:2009fn, WilsonEwing2012]…”.

**Issue:** The specific fNL=−35/8 prediction is derived in Cai et al. 2009 and Wilson‑Ewing 2013; Wands (2010) is a general review on local PNG and does not itself propose that matter‑bounce value. Grouping all three equally as if each directly states fNL=−35/8 blurs their roles and over‑credits Wands 2010.

**Fix (minor):** Adjust the citation pattern and wording, e.g. “In the quasi‑matter bounce scenario, Cai et al. (2009) and Wilson‑Ewing (2013) derive a prediction fNL=−35/8, discussed in the broader context of local PNG reviews such as Wands (2010).”


## PAPER-PER-M3 — PTA reference list incompletely aligned with in‑text narrative

**Location:** §NANOGrav discussion and Appendix PTA MCMC, where NANOGrav 15‑yr, EPTA DR2, PPTA DR3 and Afzal et al. 2023 “new‑physics” paper are mentioned and treated as specific works.

**Issue:** The narrative names the NANOGrav 15‑year GWB detection paper, EPTA DR2, PPTA DR3, Afzal et al. “NANOGrav 15‑yr: search for new physics”, and the free‑spectrum KDE Zenodo pack as distinct sources, but the bibliography as shown lumps PTA citations under generic “NANOGrav2023”, “EPTA2023”, “PPTA2023”, “Afzal2023NewPhys” without precise title/year alignment visible in the tex snippet. There is risk of mismapping IDs (e.g. wrong arXiv or journal) given the many NG15‑year companion papers.

**Fix (minor):** In the .bib, ensure each PTA paper cited in text maps to the correct, specific arXiv ID/title (e.g. Agazie et al. 2023 ApJL 951 L8, Afzal et al. 2023 ApJL 951 L11, Antoniadis et al. 2023 A&A 678 A50, Reardon et al. 2023 ApJL 951 L6) and that the labels used in the tex (NANOGrav2023, Afzal2023NewPhys, EPTA2023, PPTA2023) correspond one‑to‑one to those canonical references, not to generic or mis‑year variants.


## PAPER-PER-m1 — Explicit “Heinrich+2024” shorthand should be replaced by real citation key

**Location:** Introduction and §fnl, multiple mentions of “Heinrich+2024” alongside [Heinrich2023].

**Issue:** The text uses “Heinrich+2024” as if it were a standard shorthand for a later paper, but only a 2023 Heinrich et al. arXiv/journal item is actually cited in the bibliography. This looks like an internal future‑work label rather than a real, published “2024” paper.

**Fix (nit):** Either (a) change all “Heinrich+2024” mentions to “Heinrich et al. (2023)” if they refer to the same work, or (b) add a separate, correctly specified 2024 Heinrich et al. entry to the bibliography and cite that explicitly, dropping the ambiguous “+2024” shorthand from prose.


## PAPER-PER-m2 — Overloaded use of “consensus” for σ(fNL) forecast range

**Location:** Same clause as M1 in the Introduction.

**Issue:** Describing σ(fNL)≈0.4–0.9 as a “consensus” for “SPHEREx‑class surveys” based on one or two references risks overstating the degree of community agreement; most forecasting papers speak for their own configurations, and there is no formal community statement with that numeric range.

**Fix (nit):** Replace “consensus σfNL≈0.4–0.9” with “typical σfNL≈0.4–0.9 forecasts in the literature for SPHEREx‑like surveys (e.g. Munchmeyer et al. 2019)” or similar language that clearly frames it as representative examples rather than an official consensus.
