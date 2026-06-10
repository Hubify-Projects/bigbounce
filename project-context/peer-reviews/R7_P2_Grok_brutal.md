# P2 R7 — Brutal-honesty journal referee (treating this as a real PRD submission)

**Model**: `grok-4.3`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 14.0s

---

**Referee Report for P2 (Physical Review D)**

**P2-E1 (ESSENTIAL)**  
Section: Appendix A.2 (near end of paper, ~p. 19)  
Problem: Internal review-log artifact appears in body prose: “cross-model peer-review concern (R42 Gemini 3.1-Pro P2 BLOCKER B-3)”.  
Required fix: Delete the parenthetical tag and any similar review-process language.  

**P2-E2 (ESSENTIAL)**  
Section: Entire manuscript (22 pages)  
Problem: Paper length greatly exceeds the actual incremental contribution (a template-overlap audit plus recast of existing Heinrich et al. 2024 forecasts, plus prior-sensitivity scans). No new observable, no new estimator, and no new derivation of the bispectrum is presented.  
Required fix: Shorten to ≤12 pages. Remove all redundant Monte-Carlo validation text, four-corner prior grids already summarized in Table II, and repeated “headline” restatements.  

**P2-E3 (ESSENTIAL)**  
Section: Abstract (first paragraph) and §IV (p. 7–8)  
Problem: Abstract states “the bispectrum-only 5.2–5.5σ is the headline forecast of this paper” while simultaneously reporting the post-systematic range as 3–5σ; the two numbers are drawn from different Fisher matrices (single-bin bispectrum vs. multi-bin SDB) without explicit qualification that they are not on the same scale.  
Required fix: State a single, consistently qualified detection significance that reflects the full systematic budget applied to the observable actually used for the headline claim.  

**P2-M1 (MAJOR)**  
Section: Abstract and §VI (p. 9–11)  
Problem: Bayes-factor range “BF ∼ 10–17” is presented as the headline envelope, yet the text repeatedly states that the recommended physically motivated prior (σ_theory = 1.0) yields only BF ∼ 10 and that any realistic theoretical uncertainty on f_NL monotonically lowers the factor. The upper bound is therefore an artifact of an unmotivated delta-function prior.  
Required fix: Quote only the BF obtained with the recommended prior; move the delta-prior maximum to a sensitivity table or delete it.  

**P2-M2 (MAJOR)**  
Section: §II C and Appendix A (p. 5–6, 18–20)  
Problem: The paper asserts that the Cai et al. convention is “correct” on the basis of an operator-algebra identity while simultaneously tabulating both conventions and noting that the Li & Brandenberger value halves all significances. This is an unresolved normalization ambiguity, not a settled fact.  
Required fix: Present the detection significance under both normalizations on equal footing or adopt one convention and state the consequence of the other as a pure systematic.  

**P2-M3 (MAJOR)**  
Section: §IV and §V (p. 7–9)  
Problem: MegaMapper forecasts are labeled “speculative motivation, not firm forecasts” yet are given the same prominence and numerical ranges as the SPHEREx results.  
Required fix: Move all MegaMapper numbers to a short “outlook” paragraph or delete them.  

**P2-N1 (MINOR)**  
Section: Abstract  
Problem: Phrase “we quantify for the first time the template mismatch” is used without a literature search establishing absence of prior overlap calculations.  
Required fix: Replace with “we quantify the template mismatch”.  

**P2-N2 (MINOR)**  
Section: §II A (p. 3)  
Problem: Repeated use of “underdetermined polynomial coefficients c1–c6” and “null-space scan” language that is already summarized in one sentence.  
Required fix: Condense to a single statement of the ±0.13 scatter in r.  

**P2-NIT1 (NIT)**  
Section: Data availability statement  
Problem: Version tag “paper2-v1.7.40” and GitHub path are unnecessary for a published paper.  
Required fix: Replace with a stable DOI or remove the tag.  

## Summary recommendation  
**MAJOR REVISIONS**

The manuscript contains an internal review artifact that must be removed, presents detection significances drawn from inconsistent Fisher matrices without clear qualification, and inflates a 12-page technical note into a 22-page paper by repeated restatement of the same prior-sensitivity results and speculative MegaMapper projections. Once the artifact is excised, the length is cut by roughly half, and a single consistently qualified significance (reflecting the full systematic budget on the bispectrum channel) is adopted, the paper could become a concise, publishable forecast note. Until those changes are made it is not acceptable.