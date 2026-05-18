# P3_v3145_R7 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1100pt
**Wall time**: 12.7s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=59707, completion=977, total=60684

---

## PAPER-PER-B1 — BLOCKER

**Section:** Abstract; bib `Heinrich2023`  
**Issue:** The citation metadata is fused. The paper cites `Heinrich2023` as a SPHEREx multi-tracer bispectrum forecast, but the arXiv match is `2311.13082`, whose real title is exactly **“Measuring \(f_{\mathrm{NL}}\) with the SPHEREx Multi-tracer Redshift Space Bispectrum”** and authors are Chen Heinrich, Olivier Dore, Elisabeth Krause [1].  
**Fix:** Replace every “Heinrich+2024”/mismatched title variant with the real title and correct arXiv ID `2311.13082`; keep the author list aligned with the arXiv record [1].

## PAPER-PER-B2 — BLOCKER

**Section:** `\bibitem{NANOGrav2023}` and `\bibitem{Afzal2023NewPhys}`  
**Issue:** The bibliography collapses distinct NANOGrav papers but misstates the specific claims. `2306.16219` is **“The NANOGrav 15-year Data Set: Search for Signals from New Physics”**, while the 15-year evidence paper is a different article; the text also mixes those results with a separate “HD-correlated free-spectrum KDE” analysis [3].  
**Fix:** Split the references so the evidence paper and the new-physics paper are distinct, and cite the correct paper for each claim. Do not attribute the KDE posterior or the “evidence for a GWB” phrasing to the new-physics paper [3].

## PAPER-PER-B3 — MAJOR

**Section:** `\bibitem{Heinrich2023}`, intro/cosmology sections  
**Issue:** The bibliography says `Heinrich2023` is a 2024 JCAP paper with arXiv `2311.13082`, but the paper text repeatedly treats it as a 2024/2023 “Heinrich+2024” anchor and as if it provides the exact forecast numbers used here; the arXiv record itself gives only the bispectrum forecast and `σ_fNL = 0.7` baseline [1].  
**Fix:** Standardize the citation to the real paper metadata and limit the attributed result to what the paper actually states: the bispectrum forecast and the stated `σ_fNL = 0.7` result [1].

## PAPER-PER-B4 — MAJOR

**Section:** `\bibitem{ACT_DR6}`; ACT discussion/appendix  
**Issue:** The ACT reference is fused to a specific DR6 lensing power-spectrum paper, but the manuscript uses it as if it were a generic ACT DR6 survey release. That title does not match the way the paper describes the cited dataset/use case [2].  
**Fix:** Either cite ACT data-release documentation or explicitly say you are using that specific ACT DR6 lensing paper as the proxy reference. Right now the bibliography title and the paper’s use of ACT are not the same thing [2].

## PAPER-PER-B5 — minor

**Section:** `\bibitem{LAMOST_DR10}`, `\bibitem{SDSS_DR18}`, `\bibitem{eROSITA_DR1}`, `\bibitem{GaiaDR3}`  
**Issue:** These bibliography entries are incomplete or overcompressed relative to the claims in the text. For example, `SDSS_DR18` is cited as a 2023 ApJS article, but the paper treats it as a data release document with survey-wide targeting/spectroscopy scope; similar issues apply to the others where the exact venue/title is not fully specified [4].  
**Fix:** Expand the bib entries to the authoritative survey-release papers or official release docs, and make the title/venue match the specific claim each entry supports [4].

## PAPER-PER-B6 — nit

**Section:** `\bibitem{Liang2023}`  
**Issue:** The arXiv ID is correct (`2307.07664`), and the title is real, but the paper text overstates it as “largest prior single-survey spectroscopic anomaly catalog” in a way that depends on the manuscript’s own disputed counting logic, not on the citation itself [0].  
**Fix:** Keep the citation, but rephrase the comparison as a manuscript claim rather than something directly established by Liang et al. If you need the comparison, define the baseline metric precisely before citing it [0].
