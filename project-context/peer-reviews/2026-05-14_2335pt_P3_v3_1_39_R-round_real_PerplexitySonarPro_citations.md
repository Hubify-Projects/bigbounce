# P3_v3_1_39 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-14_2335pt
**Wall time**: 10.9s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=56785, completion=761, total=57546

---

## PAPER-PER-B1

**BLOCKER** — `\bibitem{Heinrich2023}` is fused metadata. The cited paper is **“Measuring \(f_{\mathrm{NL}}\) with the SPHEREx Multi-tracer Redshift Space Bispectrum”** and the correct arXiv ID is **2311.13082**; the text repeatedly treats it as a 2024 paper and misstates the benchmark as an “external headline” plus a different pipeline provenance. Fix the bibliography entry to match the real title, authors, arXiv ID, and publication status, and stop attributing the 0.7 forecast to a different paper lineage. 

## PAPER-PER-B2

**MAJOR** — `\bibitem{ACT_DR6}` has a title/venue mismatch. The arXiv record for **2306.16214** is the EPTA paper, while **2306.16215** is the PPTA paper; the ACT citation in this draft is not the real ACT-DR6 bibliographic identity, and the paper itself uses that reference to justify CMB cross-transfer failure. Fix the bibliography so the ACT claim points to the correct ACT DR6 publication and ensure the cited paper actually contains the DR6 result being described. 

## PAPER-PER-B3

**MAJOR** — `\bibitem{NANOGrav2023}` is not an adequate citation for the NANOGrav free-spectrum KDE release used here. The draft cites a 2023 “evidence for a gravitational-wave background” paper, but the analysis is specifically built on a **Zenodo KDE free-spectrum data product**, not the headline detection paper alone. Fix the reference chain: cite the actual NANOGrav KDE data release and keep the discovery paper separate, or the method provenance is unsupported. 

## PAPER-PER-B4

**MAJOR** — the bibliography and in-text framing around **SPHEREx** are internally inconsistent. `\bibitem{SPHEREx2014}` correctly maps to **arXiv:1412.4872**, but the paper also repeatedly treats later SPHEREx \( \sigma_{f_{\mathrm{NL}}} \) forecasts as if they were grounded in that 2014 concept paper, while the actual \(0.7\) forecast is from **2311.13082**. Fix the narrative so the 2014 paper is only the mission concept citation and the forecast citation is the 2023 Heinrich paper. 

## PAPER-PER-B5

**minor** — `\bibitem{SDSS_DR18}` is likely misnamed/misattributed in venue wording. The cited title is **“The Eighteenth Data Release of the Sloan Digital Sky Survey: Targeting and Spectroscopy”** with 2023 ApJS details, but the text uses it as if it were a definitive source for all DR18 catalog properties and sample sizes. Tighten the wording to “data release paper” and avoid overclaiming that this citation alone validates every DR18 count used in the draft. 

## PAPER-PER-B6

**nit** — the LAMOST, eROSITA, Gaia, NEOWISE, Planck, and Liang references are not checked against the journal records in the text, but the draft’s internal citation chain is already strained by multiple fused or overextended references. The main fix is editorial: run a full bib audit and ensure each in-text quantitative claim maps to a paper that actually reports it, rather than a neighboring paper or a later reinterpretation. 
