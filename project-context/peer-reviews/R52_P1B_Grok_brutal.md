# P1B R52 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/public/papers/paper1b_mcmc_companion.pdf` md5=a29137f5 pages=21
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 63.6s

---

**Referee Report for P1B (Round R52)**

**P1B-E1 (ESSENTIAL)**  
Section: Abstract-equivalent opening paragraph (p. 1) and §III scope statement (p. 3)  
Problem: The lead claim states that the \(\Lambda\)CDM+\(\Delta N_{\rm eff}\) run “find[s] \(\Delta N_{\rm eff}\) consistent with zero (−0.020±0.169 …)”. The body (Table I, p. 19) shows these numbers come from two frozen chains whose 95 % one-sided upper limits are 0.31 and 0.40 after post-processing; the quoted central value is the mean of a truncated posterior that explicitly discards the negative tail. No such truncation is stated in the opening paragraph.  
Required fix: Either remove the numerical claim from the lead paragraph or insert the explicit truncation statement and the one-sided nature of the limit at first use.

**P1B-E2 (ESSENTIAL)**  
Section: §IV, “Scope note” (p. 6) and Fig. 3 caption (p. 7)  
Problem: The NaMaster pipeline-recovery bias \(\Delta\hat\beta=-0.032^\circ\) to \(-0.040^\circ\) is presented immediately adjacent to the published 3.6\(\sigma\) sky-measurement significance (0.342°±0.094°) without the mandatory qualifier “not directly comparable” at every juxtaposition. Instruction 7 is therefore triggered.  
Required fix: Insert the explicit non-comparability statement in both the text and every figure caption that places the two numbers on the same page.

**P1B-E3 (ESSENTIAL)**  
Section: §VI, “Note (spectator-status caveat)” (p. 10) and abstract-equivalent text (p. 1)  
Problem: The birefringence signal \(\beta\approx0.27^\circ\) is repeatedly labelled “not a distinctive ECH prediction”. The abstract-equivalent paragraph nevertheless presents the spectator-ALP calculation as part of the “ECH Spin-Torsion Program” verification. This is a direct violation of the standalone-reader test (instruction 18) and of the requirement that the abstract accurately summarize what the paper proves.  
Required fix: Either excise the ALP section from the lead summary or re-title the paper so that the ECH framework is not advertised as producing the birefringence signal.

**P1B-M1 (MAJOR)**  
Section: §I “Scope of this paper” (p. 2) and repeated scope statements throughout  
Problem: The manuscript consists of three explicitly negative results (“not a spin-torsion theory module”, “not a competitive sky detection”, “not a distinctive ECH prediction”). The positive content is limited to pipeline-validation numbers already known to be sub-dominant to the published sky uncertainty. At 21 pages this exceeds any reasonable page limit for the claimed incremental contribution.  
Required fix: Reduce to a 6–8 page technical note or withdraw.

**P1B-M2 (MAJOR)**  
Section: Table I footnote a and §III (p. 3–4)  
Problem: The one-sided 95 % upper limits on \(\Delta N_{\rm eff}\) are obtained only after an ad-hoc re-normalisation of the posterior that discards the \(\Delta N_{\rm eff}<0\) tail. No justification is given for why a physically allowed negative tail is removed before quoting the limit.  
Required fix: Provide a physically motivated reason or revert to the two-sided interval.

**P1B-M3 (MAJOR)**  
Section: Data Availability paragraph (p. 15) and Appendix A  
Problem: The reproducibility manifest lists HuggingFace dataset URLs whose DOIs are still “pending”. Several commit hashes pre-date the stated paper version v1B.0.74. This violates provenance-surface audit (instruction 16).  
Required fix: Supply frozen DOIs and commit hashes that match the exact version of every number quoted in the text.

**P1B-N1 (MINOR)**  
Section: Multiple figure captions (Figs. 1–4)  
Problem: Axis labels omit units on derived quantities (e.g., \(\Delta\phi/f_a\) in Fig. 4).  
Required fix: Add units.

**P1B-N2 (NIT)**  
Section: Running headers and date line (p. 1)  
Problem: Date “June 14, 2026” is in the future relative to any plausible submission. Cosmetic.

**Summary recommendation**  
**MAJOR REVISIONS**  

The manuscript is a 21-page collection of null results and pipeline checks whose positive scientific payload is minimal once every self-imposed scope limitation is respected. The repeated juxtaposition of pipeline bias with published sky significances without the required non-comparability qualifier, the unadvertised posterior truncation in the lead claim, the advertising of a spectator-ALP result as part of an “ECH Spin-Torsion Program” while simultaneously disclaiming any ECH derivation, and the absence of frozen reproducibility artifacts together constitute multiple ESSENTIAL violations. The paper cannot be accepted in its present form; at minimum a major contraction to a short technical note plus the fixes above would be required.