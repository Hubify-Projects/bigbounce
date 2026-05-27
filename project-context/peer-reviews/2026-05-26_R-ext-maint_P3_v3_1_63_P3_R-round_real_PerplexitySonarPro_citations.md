# P3 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-26_R-ext-maint_P3_v3_1_63
**Wall time**: 11.6s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=68909, completion=1066, total=69975

---

## PAPER-B1 — MAJOR

**Section:** Intro / bibliography around `\cite{Wands2010,Cai:2009fn,WilsonEwing2012}`

**Issue:** The paper treats `Cai:2009fn` and `WilsonEwing2012` as supporting the specific claim that the matter-bounce prediction is \(f_{\rm NL}=-35/8\), but the provided bibliography is metadata-only and I could only verify `WilsonEwing2012` as a real paper titled *The Matter Bounce Scenario in Loop Quantum Cosmology*; the arXiv record does not itself state the \(-35/8\) value in the abstract. `Cai:2009fn` is not checked here, so the claim is presently under-verified and may be oversold in the prose.

**Fix:** Replace the claim with the exact, source-grounded statement from the cited papers, or add the specific section/page reference where \(-35/8\) is derived. If the value comes from a different paper, cite that paper directly.

## PAPER-B2 — MAJOR

**Section:** Cosmological applications / references to `Heinrich2023`

**Issue:** `Heinrich2023` is bib-metadata fused from the wrong year/venue form. The paper cites `Heinrich2023` as “JCAP 2024, 074 (2024), arXiv:2311.13082,” and the arXiv record confirms the title and authors, but the year/key formatting is inconsistent with the actual publication metadata shown on arXiv.

**Fix:** Normalize the citation to the actual bibliographic record: *Measuring \(f_{\mathrm{NL}}\) with the SPHEREx Multi-tracer Redshift Space Bispectrum*, arXiv:2311.13082, published in JCAP 2024, 074. Use the journal reference exactly as indexed by the publisher/INSPIRE.

## PAPER-B3 — MAJOR

**Section:** `\bibitem{PPTA2023}` and PTA discussion

**Issue:** The bibliography entry for `PPTA2023` is not consistent with the arXiv record. The arXiv page shows the title *Search for an isotropic gravitational-wave background with the Parkes Pulsar Timing Array*, authors led by Daniel J. Reardon, and an ApJL journal reference; the paper text uses it as a generic PTA citation, but the metadata in the bibliography is too thin and risks misidentification in downstream citation graphs.

**Fix:** Expand the entry to the full standard metadata format, including the correct author list lead, arXiv ID `2306.16215`, and journal reference `Astrophys. J. Lett. 951, L6 (2023)`.

## PAPER-B4 — minor

**Section:** `\bibitem{NANOGrav2023}` / `\bibitem{Afzal2023NewPhys}` / PTA appendix

**Issue:** The bibliography key `NANOGrav2023` is used for *The NANOGrav 15-year Data Set: Search for Signals from New Physics* (arXiv:2306.16219), which is correct, but the prose around it repeatedly implies this is the same object as the free-spectrum KDE release used in the MCMC appendix. That is a citation-chain ambiguity: the paper cites the new-physics search, while the appendix actually relies on the separate KDE data product.

**Fix:** Split the citation chain. Cite the NANOGrav paper for model context, and separately cite the KDE/Zenodo data product for the likelihood input.

## PAPER-B5 — minor

**Section:** `\bibitem{Liang2023}` / Introduction and comparison text

**Issue:** The bibliographic record for Liang et al. is real and the arXiv ID `2307.07664` is correct, but the manuscript repeatedly treats the DESI EDR study as if it were on the Bright Galaxy Survey only while citing the paper as a general DESI outlier benchmark. The arXiv abstract confirms BGS-specific scope, so the prose is too broad in places.

**Fix:** Tighten the wording everywhere Liang et al. are used: say “DESI Bright Galaxy Survey” or “BGS” rather than generic “DESI EDR anomaly detection.”

## PAPER-B6 — nit

**Section:** Abstract / bibliography around `Cai:2014` and `Quintin2014`

**Issue:** The paper mixes several bounce-cosmology citations as if they jointly establish the PTA spectral index and the \(-35/8\) local non-Gaussianity claim. That is a citation-chain compression, not a metadata error, but it makes the provenance hard to audit.

**Fix:** Separate the claims by citation: one set for the matter-bounce background prediction, one for the local \(f_{\rm NL}\) result, and one for the PTA spectral-index mapping.
