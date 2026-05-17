# P3_v3143 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-17_1030pt_P3_v3143_R5_R-round_real
**Wall time**: 22.4s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=58877, completion=1515, total=60392

---

## PAPER-PER-B1 – Mis-cited Heinrich et al. forecast (arXiv/id missing)

**Issue (Sec. Introduction, fnl paragraph):** The text repeatedly refers to “Heinrich et al.” and “Heinrich+2024” for a SPHEREx bispectrum-only forecast with \(\sigma_{f_{\rm NL}}\approx 0.7\), but the bibliography does not contain any Heinrich et al. 2023/2024 SPHEREx forecast entry (only Heinrich et al. 2023 on a different topic is cited implicitly in the narrative). This makes the “Heinrich+2024 \(\sigma_{f_{\rm NL}}\approx 0.7\)” anchor effectively uncited and unverifiable. [1]

**Fix:** Add the correct Heinrich et al. SPHEREx multi‑tracer/bispectrum forecast paper with full metadata (authors, title, year, arXiv ID or journal) to the bibliography, and explicitly cite it wherever “Heinrich+2024 \(\sigma_{f_{\rm NL}}\approx 0.7\)” is mentioned.

---

## PAPER-PER-B2 – SPHEREx 2014 citation okay but mis-framed

**Issue (Introduction, SPHEREx description):** The SPHEREx reference is given as “SPHEREx2014” and the bib entry is effectively the 2014 white paper by Doré et al. on “Cosmology with the SPHEREX All‑Sky Spectral Survey” (arXiv:1412.4872), which indeed exists with that title and author list. [1] However, the text calls it “SPHEREx satellite” and “SPHEREx 2014 \(\sigma_{f_{\rm NL}}\approx 0.7\) forecast” as if that specific paper contained the detailed multi‑tracer \(\sigma_{f_{\rm NL}}\approx 0.7\) numbers being used as “headline external benchmark,” whereas the 2014 white paper is more general and does not present the Heinrich‑style forecasts the text attributes to it.

**Fix:** Keep citing Doré et al. (2014) for the mission description but move all specific \(\sigma_{f_{\rm NL}}\approx 0.7\) claims to the correct Heinrich‑et‑al. forecast paper; restrict the SPHEREx 2014 citation to hardware/mission overview wording.

---

## PAPER-PER-M1 – Liang et al. 2023 reference mostly correct, but rate comparison under-specified

**Issue (Abstract; Intro; survey comparison):** The paper cites “Liang et al. 2023” and correctly describes it as using an autoencoder+normalizing flow on DESI EDR with 2,685 anomalies from ~250,000 BGS spectra (1.07% outlier rate), which matches the arXiv entry “Outlier Detection in the DESI Bright Galaxy Survey” (Liang et al., 2023, arXiv:2307.07664). [2] However, the manuscript frames its DESI DR1 anomaly fraction and absolute counts as “consistent” or “a \(\sim 73\times\) increase over the same Liang baseline” without clarifying that Liang’s rate is for BGS only while this paper is mixing all DESI DR1 target classes; that’s technically a methodology/selection mismatch attributed to Liang’s paper.

**Fix:** Explicitly state that Liang et al. work on the BGS subset of DESI EDR, not the full DR1 target mix, and qualify all rate/ratio language as “approximate, cross‑selection” rather than “like-for-like” so that Liang et al. are not misrepresented.

---

## PAPER-PER-M2 – Missing/implicit arXiv IDs for some key bounce/PTA references

**Issue (Cosmology sections & PTA appendix):** The text cites several bounce and PTA papers by author/year only (e.g. Wands 2010, Cai et al. 2009, Quintin 2014, Cai 2014, Afzal et al. 2023 “New Physics”) and then bases quantitative statements on them (e.g. \(\fnl=-35/8\), \(\gamma_{\rm GW}=3\) prediction, NG15 new‑physics template space), but no explicit arXiv IDs or journal references are given in the provided bibliography for some of these, making it hard to verify the exact source versions being used. The NANOGrav new‑physics paper in particular is unambiguously arXiv:2306.16219. [3]

**Fix:** For each bounce/PTA reference that underpins a concrete numerical claim (Wands 2010, Cai et al. 2009, Quintin 2014, Cai 2014, Afzal 2023), add explicit arXiv identifiers (and journal references where available) in the bibliography so a reader can quickly confirm the quoted \(\fnl\), \(\gamma\), and model assumptions.

---

## PAPER-PER-m3 – SPHEREx white-paper authorship and venue slightly incomplete

**Issue (Bibliography: SPHEREx entry):** The SPHEREx white paper is currently represented only by a mnemonic key “SPHEREx2014” and minimal metadata; the actual arXiv record lists Olivier Doré as first author with an explicit author list and arXiv:1412.4872 plus DOI 10.48550/arXiv.1412.4872. [1] The current bib entry omits the DOI and may omit parts of the author list or treat it as “SPHEREx Collaboration.”

**Fix:** Update the SPHEREx 2014 bib entry to match the arXiv metadata: full first‑author name (“O. Doré et al.” or “O. Doré for the SPHEREx Collaboration”), title “Cosmology with the SPHEREX All‑Sky Spectral Survey,” arXiv:1412.4872, and DOI.

---

## PAPER-PER-n1 – Minor: unclear whether “Liang2023” bib entry includes arXiv ID

**Issue (Bibliography: Liang2023):** The in‑text cite “Liang et al. 2023” clearly refers to arXiv:2307.07664, “Outlier Detection in the DESI Bright Galaxy Survey,” which has not yet appeared in a journal as of its arXiv entry. [2] The provided bibkey “Liang2023” is used, but no explicit arXiv ID or DOI is shown in the excerpt, so it is ambiguous whether the bibliography will show “arXiv:2307.07664” or just the title.

**Fix:** Ensure the Liang2023 bib entry explicitly includes “arXiv:2307.07664” and the correct title and author list from arXiv so that readers can verify the methodology and numbers being quoted.
