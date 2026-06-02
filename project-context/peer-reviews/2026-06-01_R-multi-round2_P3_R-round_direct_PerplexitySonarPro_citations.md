# P3 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-multi-round2
**Wall time**: 24.2s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=79815, completion=1809, total=81624, search_context_size=low, cost={'input_tokens_cost': 0.23945, 'output_tokens_cost': 0.02713, 'request_cost': 0.006, 'total_cost': 0.27258}

---

## PAPER-PER-B1 — Mis-cited “Heinrich2023” primary result

**Issue (MAJOR):**  
In the intro (cosmology motivation) and §5 the paper treats “Heinrich et al. 2023” as a published SPHEREx multi‑tracer *bispectrum* forecast with headline \(\sigma_{f_{\rm NL}}\approx 0.7\), but there is no such Heinrich+ paper in the literature: the real SPHEREx non‑Gaussianity forecasts are by e.g. Munoz et al., Alvarez et al., or generic SPHEREx white papers, and no arXiv:2311.13082 / JCAP 2024 Heinrich et al. multi‑tracer bispectrum paper exists in arXiv/ADS/publisher databases. The bibliography entry is therefore a fused/fictional citation and cannot be used as an external “anchor” benchmark.

**Fix:**  
Replace “Heinrich et al. 2023 / 2024 \(\sigma_{f_{\rm NL}}\approx 0.7\)” with a real SPHEREx \(f_{\rm NL}\) forecast paper (e.g. SPHEREx collaboration forecasts) and update all text that treats Heinrich+ as a published external benchmark to instead describe it as either: (i) an internal Fisher calculation (clearly labeled as such), or (ii) anchored to the actual published SPHEREx forecast you cite, with the correct authors, year, journal, and \(\sigma_{f_{\rm NL}}\) values.  


## PAPER-PER-B2 — Mis-cited “Münchmeyer et al. 2019” SPHEREx forecast comparison

**Issue (MAJOR):**  
The paper repeatedly compares its internal Fisher \(\sigma_{f_{\rm NL}}\sim 0.07\!-\!0.12\) to a claimed “Münchmeyer et al. 2019 consensus \(\sigma_{f_{\rm NL}}\sim 0.4\!-\!0.9\) for SPHEREx‑class surveys.” Munchmeyer et al. (2019, Phys. Rev. D 100, 083508, arXiv:1810.13424) is about kSZ tomography and primordial NG constraints for CMB surveys, not a SPHEREx‑specific multi‑tracer \(f_{\rm NL}\) forecast at 0.4–0.9. No such “consensus SPHEREx \(\sigma_{f_{\rm NL}}\approx 0.4\!-\!0.9\)” appears in that paper.

**Fix:**  
Either (a) drop the explicit 0.4–0.9 numerical range and rephrase as a qualitative statement about CMB/kSZ‑based constraints citing Munchmeyer et al. correctly, or (b) replace this with a real SPHEREx \(f_{\rm NL}\) forecast reference (with correct numbers and citation) and reserve Munchmeyer et al. solely for its actual kSZ/CMB context. Make clear that any 0.4–0.9 figure is coming from the properly cited source, not from Münchmeyer et al.  


## PAPER-PER-B3 — Misuse / over-interpretation of NANOGrav HD KDE artifact as “free-spectrum likelihood”

**Issue (BLOCKER):**  
The NANOGrav analysis (Appendix PTA, §6.2) treats the 15‑yr HD‑correlated *free‑spectrum KDE* artifact (Zenodo 8060824) as a stand‑alone \(\gamma,\log_{10}A\) likelihood, constructs an \(\mathcal{L}(\gamma, A)\) by evaluating each per‑frequency KDE at an *assumed* power‑law mapping, and then reports Savage–Dickey Bayes factors “decisive against SMBHB” etc. But the NANOGrav paper explicitly states that those KDEs are *summary products from fits within specific astrophysical/HD models*, not a model‑agnostic multivariate likelihood; reinterpreting them as an independent 2D likelihood and reporting quantitative Bayes factors matter‑bounce vs SMBHB overreaches what that artifact formally supports, and the chain is not from a bounce vs SMBHB model comparison run.

**Fix:**  
Downgrade the NANOGrav section to a clearly labeled *illustrative parameter‑shift check* on \(\gamma\) using the published free‑spectrum posteriors, and remove (or push to appendix as speculative) the quoted numeric Bayes factors and “decisive” language. State explicitly that a proper model comparison would require rerunning the full NANOGrav PTA likelihood with bounce and SMBHB signal models, which is outside the scope of this paper.  


## PAPER-PER-M1 — “Quintin2014 / Cai2014 / WilsonEwing2012” linkage to \(\gamma_{\rm GW}=3\) prediction

**Issue (MAJOR):**  
The matter‑bounce gravitational‑wave spectral‑index prediction \(\gamma_{\rm GW}=3\) is attributed jointly to Quintin et al. 2014, Cai 2014 (Sci. China review), and Wilson‑Ewing 2012. In the actual literature, (a) the detailed non‑Gaussianity result \(f_{\rm NL}=-35/8\) comes from Cai et al. 2009 (JCAP 0905:011) and related Brandenberger‑group work, while (b) the precise PTA‑convention mapping \(\gamma=5-n_T\) and the statement “matter‑bounce \(\gamma=3\)” are not formulated in that way in those three specific references. The paper presents this as if each cited work explicitly states the PTA‑\(\gamma\) prediction, which it does not.

**Fix:**  
Revise the bounce‑physics paragraph to: (i) cite Cai et al. 2009 for the \(f_{\rm NL}=-35/8\) result; (ii) cite a standard PTA convention paper for \(\gamma=5-n_T\); and (iii) explain that \(\gamma=3\) is your *derived* consequence of a blue tensor tilt \(n_T=2\) in matter contraction rather than a literal statement in Quintin2014/Cai2014/Wilson‑Ewing2012. Make that derivation explicit and stop implying that the three papers themselves give \(\gamma_{\rm GW}=3.0\) in PTA notation.  


## PAPER-PER-m1 — Ambiguous / misleading use of SPHEREx white‑paper citation

**Issue (minor):**  
The SPHEREx reference is given as Doré et al. 2014 (SPHEREx white paper) and then used as if it contained specific, quantitative local \(f_{\rm NL}\) multi‑tracer forecasts at the precision discussed here. The white paper is broad and does not contain detailed multi‑tracer Fisher numbers with \(\sigma_{f_{\rm NL}}\sim 0.7\) in the way the text suggests, so treating it as the source of those exact numbers is misleading.

**Fix:**  
Clarify that Doré et al. (2014) is cited for mission concept and survey parameters only, and either (a) provide a separate, correct reference for any specific \(\sigma_{f_{\rm NL}}\) forecast used as an external benchmark, or (b) mark those numbers as derived “this work” internal Fisher results informed by SPHEREx survey specs, not pulled from the SPHEREx white paper itself.  


## PAPER-PER-n1 — Overly strong language around Jeffreys‑scale Bayes‑factor labels

**Issue (nit):**  
Where Bayes factors are quoted (e.g., “decisive on Jeffreys’ scale”), the paper uses Jeffreys‑scale adjectives (“decisive”, “strong”) as if they were objective descriptors of reality, without reminding the reader that these terms are a conventional heuristic mapping (and especially brittle for Savage–Dickey ratios built on approximated priors and KDEs).

**Fix:**  
Soften those phrases to “what Jeffreys would classify as ‘decisive’/‘strong’ evidence” or simply drop the adjective and report \(\log_{10}B\) numerically, making clear that the interpretive label is a convention rather than a firm physical statement.
