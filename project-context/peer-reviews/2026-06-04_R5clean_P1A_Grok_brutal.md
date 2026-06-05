# P1A 2026-06-04_R5clean — Brutal-honesty journal referee (treating this as a real PRD submission)

**Model**: `grok-4.3`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 12.2s

---

**Referee Report: P1A (Round 2026-06-04_R5clean)**

**P1A-E1 (Abstract, p. 1; Sec. I, p. 3; Sec. IX, p. 12)**  
Problem: The abstract states “we report 13 logically-independent mechanism-class constraints (the prior count of 14 retained Barrier 8 as the observational consequence of the perturbation-transparency theorem Barrier 14; merged here under the perturbation-transparency umbrella since they are not logically independent)”. The body repeatedly toggles between “14 constraints” and “13 logically-independent” with B8/B14 subsumption language.  
Required fix: Remove all internal counting footnotes and self-referential merger language from the abstract and introduction. State a single, fixed number of independent constraints that the manuscript itself proves without reference to prior catalog versions.

**P1A-E2 (Abstract, p. 1; Sec. I, p. 3; Sec. IV, p. 8; Sec. XIV E, p. 18)**  
Problem: The abstract and introduction claim “channel-level closure of the four enumerated minimal-ECH dark-energy routes at amplitude-budget granularity”. The body explicitly states that the Jackiw–Pi term and the parity-odd four-fermion partner are omitted and “their explicit closure is left to a follow-up operator-level analysis”. The abstract therefore misrepresents the scope actually proved.  
Required fix: Rewrite the abstract to state only what is proved in this manuscript: a channel-level amplitude assessment of four specific enumerated routes under a phenomenological on-shell scaling ansatz, with two named operators left unclosed.

**P1A-E3 (Abstract, p. 1; Sec. I, p. 4; Sec. XII A, p. 15; Sec. XIV D, p. 17)**  
Problem: The manuscript repeatedly cites “companion work in preparation [2,6]”, “Paper I(b) [6]”, “Paper II [2]”, “Paper III [46]”, “Paper IV [23]”, and “frozen MCMC samples” whose numerical results (H0 = 67.68 ± 1.06, ∆Neff, Fisher forecasts, etc.) are required to support the central claims. These are internal review artifacts and non-citable references.  
Required fix: Remove every citation to unpublished companion papers. Either make this manuscript self-contained or withdraw it until the supporting calculations are publicly available.

**P1A-E4 (Sec. II C 1, p. 7; Sec. XII A, p. 15; Appendix B, p. 19)**  
Problem: The dark-energy mapping rests on the explicit phenomenological on-shell scaling ansatz ρΛ = Ξ MPl4 with off-shell mass dimension +1 (Eq. 6). The text acknowledges this is “not a derivation” and that the genuine hierarchy is ~120 orders of magnitude. The abstract nevertheless presents the result as a “structural conclusion” of the ECH framework.  
Required fix: State in the abstract and conclusion that the dark-energy identification is an external ansatz, not a consequence of the minimal ECH action.

**P1A-M1 (Sec. I, p. 3; Sec. IV, p. 8; Sec. IX, p. 12)**  
Problem: The manuscript contains multiple instances of version-history and internal-audit language (“earlier versions”, “prior analysis that compared…”, “this manuscript”, “the entries in this section are retained as parameterization-of-fine-tuning diagnostics”).  
Required fix: Excise all such language. The submitted text must read as a finished journal article.

**P1A-M2 (Sec. XIII, p. 16; Sec. XIV D, p. 17)**  
Problem: The two “surviving” predictions (fNL = −35/8 and β ≈ 0.27°) are explicitly stated to be “not predictions of ECH itself” and “not a distinctive ECH prediction”. Their inclusion as headline results after a channel-level closure therefore inflates the claimed contribution.  
Required fix: Move both items to a short “related tests in the broader bounce literature” paragraph and remove them from the abstract and executive summary.

**P1A-M3 (Sec. X, p. 14; Sec. XIV D, p. 17)**  
Problem: The structural tension between Ntot ≈ 92 and erasure of the matter-bounce bispectrum is presented as an independent consistency check, yet the four-route amplitude closure has already ruled out the dark-energy mechanism. The tension argument is therefore redundant and relies on the same unpublished SPHEREx forecast.  
Required fix: Delete the structural-tension subsection or reduce it to one sentence noting that the matter-bounce bispectrum test lies outside the scope of the ECH dark-energy ansatz.

**P1A-NIT1 (Throughout)**  
Problem: Repetitive hedging phrases (“under the stated assumptions”, “phenomenological ansatz”, “not a derivation”, “channel-level rather than operator-level”) appear in nearly every section.  
Required fix: Consolidate into a single, prominent “Scope and Limitations” paragraph; remove the repeated qualifiers from the body.

**P1A-NIT2 (Sec. II A 2, p. 6; Appendix B, p. 19)**  
Problem: The text contains minor internal inconsistencies in the numerical value of Ntot (92 vs. 94) arising from the choice of ansatz in Eq. (B2).  
Required fix: Adopt one consistent value and state the OOM uncertainty explicitly.

**Summary recommendation**  
REJECT

The manuscript is not a self-contained journal article. Its central claim of “channel-level closure” is repeatedly undermined by explicit statements that two relevant operators are omitted, that the dark-energy mapping is an external phenomenological ansatz, and that all quantitative supporting results reside in unpublished companion papers. The text is further compromised by pervasive internal-audit and version-history language. These defects are structural and cannot be repaired by minor revision.