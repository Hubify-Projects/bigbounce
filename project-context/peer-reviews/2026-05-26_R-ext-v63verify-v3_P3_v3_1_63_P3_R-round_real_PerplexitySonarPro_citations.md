# P3 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-26_R-ext-v63verify-v3_P3_v3_1_63
**Wall time**: 10.8s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=68956, completion=936, total=69892

---

## PAPER-CIT-1 — BLOCKER
**Line/section:** Bibliography entry `Wands2010` and the claims in the Introduction / `sec:fnl`.  
**Issue:** The paper cites `Wands2010` for “local non-Gaussianity from inflation,” but the bibliography entry is only a review title, not a source for the specific matter-bounce value \(\fnl=-35/8\). The matter-bounce prediction is actually tied to `Cai:2009fn` and `WilsonEwing2012`, so the citation chain is fused and misleading.  
**Fix:** Split the claim: cite the bounce prediction only to the bounce papers, and reserve `Wands2010` for the inflationary contrast.

## PAPER-CIT-2 — MAJOR
**Line/section:** Bibliography entry `Heinrich2023` and all derived \(\sigma_{f_{\rm NL}}\) claims in `sec:fnl`.  
**Issue:** The cited arXiv paper is real and the title matches, but the paper text repeatedly attributes a “Heinrich+2024 anchor” and then layers internal Fisher results on top of it. That is not a citation error by itself, but the manuscript conflates an external forecast with internally computed numbers and treats them as if they were the same literature benchmark.  
**Fix:** Clearly separate external literature values from in-paper calculations, and remove any wording that implies the arXiv paper contains the internal Fisher variants reported here.

## PAPER-CIT-3 — MAJOR
**Line/section:** `bibitem{Cai2014}` and bounce-related passages in `sec:fnl`, `sec:bounce_implications`, `app:pta_mcmc`.  
**Issue:** The entry “Y.-F. Cai, ‘Exploring bouncing cosmologies with cosmological surveys,’ Sci. China Phys. Mech. Astron. 57, 1414 (2014)” is too generic and likely not the actual canonical source for the exact \(\gamma_{\rm GW}=3.0\) matter-bounce statement being used. The paper’s bounce discussion mixes at least three distinct claims: scalar tilt, tensor tilt, and \(f_{\rm NL}\), but the citations are not cleanly mapped to each claim.  
**Fix:** Re-audit each bounce statement against the original source papers and assign one citation per distinct prediction, not one multi-purpose citation cluster.

## PAPER-CIT-4 — minor
**Line/section:** `bibitem{Liang2023}` and Introduction / Comparison sections.  
**Issue:** The arXiv ID `2307.07664` is correct and the title is real, but the manuscript’s summary of the paper’s methodology is incomplete: it says “autoencoder coupled with a normalizing flow” and then later uses the result as a straight baseline for anomaly-rate comparisons. That is fine, but the citation chain should not imply equivalence of thresholds or outputs across different scoring systems.  
**Fix:** Add one sentence noting that the Liang result is not directly threshold-comparable because it uses a different detector pipeline and score definition.

## PAPER-CIT-5 — minor
**Line/section:** `bibitem{Planck2018}` / `Planck2018IX`, `sec:planck`, and `sec:fnl`.  
**Issue:** The bibliography entries are real, but the paper uses them for very different purposes: CMB data description, primordial non-Gaussianity constraints, and generic Gaussian-statistics claims. The manuscript makes these citations do too much work at once, which weakens forensic traceability.  
**Fix:** Separate the CMB dataset citation from the non-Gaussianity constraints citation in the text wherever possible.

## PAPER-CIT-6 — nit
**Line/section:** `bibitem{Quintin2014}` and `bibitem{Cai2014}` in the bounce/PTA discussion.  
**Issue:** The titles and journal metadata are real, but the manuscript’s wording implies that these two papers directly establish the exact PTA spectral-index mapping used later. They do not; the PTA mapping is a separate derivation and should not be attributed back to those bounce-model citations.  
**Fix:** Add an explicit bridge sentence: the bounce papers motivate the model, while the PTA likelihood and \(\gamma\) mapping come from the NANOGrav analysis section of this paper.


