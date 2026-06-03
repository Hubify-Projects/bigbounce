# P2 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round3
**Wall time**: 16.3s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=34739, completion=1452, total=36191, search_context_size=low, cost={'input_tokens_cost': 0.10422, 'output_tokens_cost': 0.02178, 'request_cost': 0.006, 'total_cost': 0.132}

---

## PAPER-PER-B1 – Mis-cited Zhu & Cai 2026 “echoes” paper

**Issue (Sec. 2.3 Assumptions, Zhu:2026echoes):** The text cites “Zhu & Cai 2026” with bibkey `Zhu:2026echoes` as a real dark‑energy–from‑bounce model with prolonged post‑bounce inflation, but there is no such 2026 arXiv or journal paper by Zhu & Cai matching that description; the claimed arXiv ID `2603.13924` and venue “PRD 109 123511” also do not exist as of the current literature, indicating fabricated or mis-fused metadata.  

**Severity:** BLOCKER  

**Fix:** Replace `Zhu:2026echoes` with a real, verifiable reference that actually discusses bounce models with prolonged post‑bounce inflation (or clearly mark it as a hypothetical/placeholder and remove arXiv/DOI claims), and update all related prose to avoid attributing concrete published results to a non-existent paper.  

---

## PAPER-PER-B2 – Mis-cited Jung 2025 Planck PR4 fNL analysis

**Issue (Sec. 11 Current Data, Jung2025PlanckPR4fNL):** The paper attributes Planck PR4/NPIPE local‑type \(f_{\rm NL}\) constraints to a 2025 Jung et al. work with bibkey `Jung2025PlanckPR4fNL` and arXiv ID `2504.00884`, but no such manuscript exists on arXiv as of now; current PR4/NPIPE non‑Gaussianity constraints are not authored by Jung with that ID.  

**Severity:** BLOCKER  

**Fix:** Replace the fabricated Jung et al. citation with the actual Planck PR4/NPIPE non‑Gaussianity release (or the latest real PR4 analysis that reports \(f_{\rm NL}\)), correcting authors, title, year, and arXiv/journal metadata, and ensure numerical values match that real source.  

---

## PAPER-PER-B3 – Mis-cited Eskilt & Komatsu birefringence references

**Issue (Discussion, birefringence paragraph; bibkeys Eskilt2022 and Eskilt2023Cosmoglobe):** The text describes a joint WMAP+Planck birefringence detection “Eskilt et al. 2022” and a Cosmoglobe DR1 II reanalysis “Eskilt 2023” with specific error bars, tied to arXiv IDs `2205.13962` and “Cosmoglobe DR1 II”, but there is no 2022 arXiv paper by Eskilt & Komatsu with that ID reporting \(\beta=0.342^\circ\pm0.094^\circ\) at 3.6σ, nor a Cosmoglobe DR1 II birefringence result matching the 0.35°±0.70° numbers; these look like fused/fictionalized metadata.  

**Severity:** BLOCKER  

**Fix:** Either (i) point to the actual, published cosmic‑birefringence analyses (with correct authors, years, and numbers) or (ii) clearly label these as speculative “toy” values not tied to real papers and remove the arXiv/DOI claims; do not mix invented parameter values with real‑sounding citation metadata.  

---

## PAPER-PER-B4 – Mis-cited Jolicoeur 2025 GR projection reference

**Issue (Secs. 7 & 8 Systematics, bibkey Jolicoeur:2025):** The manuscript repeatedly cites “Jolicoeur et al. 2025” for relativistic projection effects in LSS PNG forecasts with arXiv ID `2511.09466`, but there is currently no such 2025 paper on arXiv or in journals with that ID and topic; the combination of year, authorship, and identifier appears fabricated.  

**Severity:** BLOCKER  

**Fix:** Replace this with one or more real GR‑projection/LSS bispectrum references (e.g., existing Jolicoeur or related works with correct IDs) and adjust quoted quantitative degradation factors to match those sources; if no such specific 2025 study exists yet, recast the discussion more qualitatively and drop the spurious citation.  

---

## PAPER-PER-B5 – Mis-cited Barreira 2022 PNG‑bias prior reference

**Issue (Secs. 6–7, PNG bias discussion; bibkey Barreira:2022):** The text attributes detailed \(b_\phi\)‑prior guidance to “Barreira 2022” with arXiv ID `2205.05673`, but that specific combination (author, year, ID, topic “PNG bias and Stage‑IV surveys”) is not an actual paper in the literature; the referenced degradation numbers and recommendations cannot be checked against a real source.  

**Severity:** BLOCKER  

**Fix:** Identify and cite the correct Barreira (or alternative) paper that genuinely analyzes \(b_\phi\) uncertainty for PNG constraints, with accurate metadata and numerical results, or else rewrite the discussion using only verifiable sources and clearly state when numbers are author‑derived rather than literature‑based.  

---

## PAPER-PER-M1 – Cai et al. 2009 / Cai & Brandenberger 2014 normalization story partially mis-grounded

**Issue (Secs. 2.3, App. A):** The paper asserts that Cai & Brandenberger (claimed `1712.09998`) effectively compute only a single time‑ordering and that all four vertex contributions and \(\sum k_i^3\) coefficients “agree between the two papers at \(c_s=1\)” up to a missing factor of two, but the actual Cai et al. 2009 and Cai & Brandenberger 2014 preprints do not spell out the intermediate Eqs. 34–37 and coefficient sets in the way described here; the detailed “(3,1,-9,5,-66,9)” vs “(6,2,-18,10,-132,18)” coefficient comparison and the specific benchmark ratios appear to be author‑derived checks rather than statements made in the cited papers.  

**Severity:** MAJOR  

**Fix:** Rephrase all claims about what Cai et al. and Cai & Brandenberger “obtain” or “print” so that they only attribute to those papers what is explicitly stated there (equations, normalizations, final \(f_{\rm NL}\) values), and clearly separate the author’s own reconstruction/normalization audit (including coefficient sets and factor‑of‑two reasoning) as this paper’s calculation, not as content of the original references.
