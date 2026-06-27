# P1A R55 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/private/tmp/R55_P1A/paper1a_ech_nogo.pdf` md5=304331a0 pages=29
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 277.8s

---

**Referee Report**

**P1A-E1**  
**Section:** Abstract (p. 1) + Sec. IV (pp. 10–13) + Sec. IX (p. 16)  
**Problem:** Abstract states “14 constraints map minimal-ECH route space” and “f_NL = −35/8” as a central result. Body shows the 14 entries are a mixture of 13 logically independent barriers plus one observational consequence (B14) of the perturbation-transparency theorem; the f_NL value is imported from Ref. [1] and is explicitly labeled “not a distinctive ECH prediction.” No derivation of either number appears in the present manuscript.  
**Required fix:** Remove both numerical claims from the abstract or supply self-contained derivations.

**P1A-E2**  
**Section:** Abstract (p. 1) + Sec. I (p. 3) + multiple cross-references to “Paper I(b)” and “in preparation [6]”  
**Problem:** Abstract and introduction present MCMC posteriors (H_0 = 67.68 ± 1.06, ΔN_eff ≈ 0), Fisher forecasts, and ALP parameter fits as supporting evidence. All numerical values and convergence diagnostics are stated to reside in an unpublished companion. The manuscript therefore fails the standalone-reader test.  
**Required fix:** Either embed the necessary MCMC tables/figures or excise all load-bearing numerical results that are not reproducible from the present text.

**P1A-E3**  
**Section:** Sec. IV D (p. 13) + Sec. IV caption (p. 10)  
**Problem:** Route 4 is declared “not closed by amplitude mismatch but by an explanatory-deficit / cosmological-constant fine-tuning objection.” The abstract nevertheless lists it among the “four enumerated minimal-ECH dark-energy routes” that are “closed.” The two statements are contradictory.  
**Required fix:** Correct the abstract or reclassify Route 4.

**P1A-M1**  
**Section:** Sec. X (pp. 20–21) + Fig. 1 (p. 5)  
**Problem:** The “perturbation-transparency” theorem is proved only for canonical scalar matter under the explicit on-shell scaling ansatz of Appendix B. The abstract and Sec. X present it as a general result for “scalar matter.” The limitation is not flagged at the same prominence as the claim.  
**Required fix:** Add a one-sentence caveat in the abstract and in the statement of the theorem.

**P1A-M2**  
**Section:** Sec. II C 1 (p. 8) + Eq. (11)  
**Problem:** The exponential factor exp(−3N_tot) is matched to an order-of-magnitude argument rather than derived from a thermal partition function or first-principles dilution calculation. The text acknowledges this is “aesthetic” yet uses the numerical value N_tot ≈ 92 as a hard barrier.  
**Required fix:** Either promote the matching to a controlled calculation or label the N_tot = 92 figure as an ansatz throughout.

**P1A-M3**  
**Section:** Table I (p. 4) + footnote a  
**Problem:** Footnote states that the 2.6–5σ range for f_NL “reflects two forecast regimes” under different systematics treatments. The table header presents a single headline significance without repeating the “not directly comparable” qualifier.  
**Required fix:** Add the explicit qualifier to every cell that mixes the two pipelines.

**P1A-M4**  
**Section:** Sec. XIII (p. 23) + Fig. 4 (p. 16)  
**Problem:** The LiteBIRD and SPHEREx forecasts are presented as “ECH-independent class tests.” The text simultaneously states that both forecasts assume the same cross-correlation coefficient ρ between f_NL and β that is only justified inside the ECH framework. This circularity is not quantified.  
**Required fix:** Supply the numerical degradation in significance when ρ is varied over its prior range.

**P1A-N1**  
**Section:** Title page (p. 1)  
**Problem:** Date “June 19, 2026” appears on a manuscript submitted for review in 2025.  
**Required fix:** Correct to the actual submission date.

**P1A-N2**  
**Section:** Multiple figure captions (e.g., Fig. 5, p. 18)  
**Problem:** Axis labels use unreduced Planck mass while the text body switches between reduced and unreduced conventions without a visible conversion factor on the plot.  
**Required fix:** Add an explicit note or rescale the axis.

**P1A-N3**  
**Section:** Bibliography entries citing “in preparation [2,6]”  
**Problem:** Several load-bearing numerical results are attributed to works that do not yet exist in citable form.  
**Required fix:** Replace with arXiv numbers or remove the citations.

**Summary recommendation**  
**REJECT**

The manuscript’s central claims—closure of four dark-energy routes at the quoted significance and the numerical values of f_NL and β_obs—are either imported from unpublished companions or rest on ansätze whose uncertainties are not propagated into the headline statements. The paper is not self-contained, contains internal contradictions on the status of Route 4, and mixes incompatible statistical pipelines without consistent qualification. These are first-read rejection criteria for Physical Review D.