# P1A 2026-06-04_R3clean — Brutal-honesty journal referee (treating this as a real PRD submission)

**Model**: `grok-4.3`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 12.6s

---

**Referee Report for P1A (Physical Review D)**

**P1A-E1 (ESSENTIAL)**  
Section: Abstract (p. 1) and Sec. I (p. 3)  
Problem: The abstract states that the work “assess[es] four enumerated minimal-ECH spin-torsion channels … and find[s] that each fails at the amplitude level” and presents a “perturbation-transparency theorem” as the central result. The body (Scope paragraph, Sec. IV, Sec. IX, Sec. X, Appendix B) repeatedly qualifies that the four routes are not an operator basis, that the Jackiw–Pi term and parity-odd four-fermion partner are omitted, that the dark-energy mapping is a phenomenological on-shell ansatz of mass dimension +1 rather than +4, and that the result holds only for canonical scalar matter. The abstract therefore does not accurately summarize what the paper proves.  
Required fix: Rewrite the abstract to state only what is actually demonstrated under the listed caveats; remove any implication of a general no-go or theorem.

**P1A-E2 (ESSENTIAL)**  
Section: Abstract, Sec. I, Sec. XII, Sec. XIII, Sec. XV, and throughout  
Problem: The manuscript contains extensive references to unpublished companion papers (“Paper I(b) [6]”, “Paper II [2]”, “Paper IV [23]”, “in preparation”, “internal MCMC analysis”, “frozen accepted samples”, “new DESI DR2 w0wa chain … running”). Cosmological parameter values are explicitly labeled “internal-analysis inputs … not independently peer-reviewable values until Paper I(b) is publicly posted.” This is review-log and version-history language that has no place in a submitted manuscript.  
Required fix: Remove every reference to unpublished or internal companion works. The paper must stand alone; either incorporate the necessary results or withdraw the submission.

**P1A-E3 (ESSENTIAL)**  
Section: Sec. IX (Table II and surrounding text), Sec. X, Sec. XIV D  
Problem: Barrier 8 and Barrier 14 are presented as separate entries in the “14 mechanism-class constraints” catalog even though the text states that B8 is “the observational consequence of the perturbation-transparency theorem B14” and that the two “are not logically independent.” The abstract and Sec. IX retain the count of 14 while acknowledging the merger.  
Required fix: Correct the count to 13 logically independent constraints and remove the historical-catalog justification for double-counting.

**P1A-M1 (MAJOR)**  
Section: Sec. I A, Sec. IV (Scope paragraph), Sec. IX, Sec. XV  
Problem: The paper repeatedly frames its result as “channel-level closure” of “the four enumerated minimal-ECH dark-energy routes” while simultaneously stating that it does not claim operator-basis closure and that omitted operators (Jackiw–Pi, parity-odd four-fermion partner) are left to future work. The title and abstract do not reflect this limitation.  
Required fix: Retitle and reframe the manuscript as an analysis of four specific phenomenological routes under restrictive assumptions, not as a closure result.

**P1A-M2 (MAJOR)**  
Section: Sec. II C 1 (“Reheating thermal-reset barrier”), Appendix B  
Problem: The text contains internal audit language (“this strengthens Barrier 14 … We emphasize that this is bookkeeping, not progress”; “the 105 residual therefore inherits … order-of-magnitude status”). These sentences are review notes, not journal prose.  
Required fix: Delete all such meta-commentary.

**P1A-M3 (MAJOR)**  
Section: Sec. XIII, Sec. XIV D, Sec. XV  
Problem: The two “surviving” predictions (fNL = −35/8 and spectator-ALP birefringence β ≈ 0.27°) are explicitly stated to be “not predictions of ECH itself” and “not a distinctive ECH prediction.” Their inclusion as the positive outcome of an ECH paper is therefore misleading.  
Required fix: Remove both predictions from the abstract, conclusions, and any summary table, or relegate them to a single sentence noting that they lie outside the scope of the ECH channel analysis.

**P1A-M4 (MAJOR)**  
Section: Sec. II C 1, Appendix B  
Problem: The required number of e-folds is given as Ntot ≈ 92 in the main text and Ntot ≈ 94 in Appendix B; the discrepancy is attributed to the choice of on-shell ansatz. No uncertainty is propagated into any quoted result.  
Required fix: Adopt a single consistent value (or range) and state the systematic uncertainty explicitly.

**P1A-N1 (NIT)**  
Section: Multiple locations (e.g., p. 1, p. 4, p. 11)  
Problem: Duplicate or near-duplicate phrasing appears (“canonical canonical-mask” is not present, but repeated clauses such as “comoving wavenumbers k are constant by definition and only physical scales scale with a−1 ∝ e−N” recur verbatim).  
Required fix: Eliminate repetitions.

**P1A-N2 (NIT)**  
Section: Sec. IV B (Eq. 15 and surrounding text)  
Problem: The text discusses an earlier “silent treatment of eV · s as dimensionless” and then corrects it. This is an internal derivation note.  
Required fix: Remove the sentence describing the prior error.

**Summary recommendation**  
REJECT

The manuscript is not a self-contained submission. Its central claims rest on unpublished companion analyses whose results are labeled non-peer-reviewable, and the abstract and title materially misrepresent the heavily qualified, negative conclusions actually reached in the body. Even after removal of all companion references and correction of the double-counting and internal-audit language, the remaining content is a catalog of already-known or assumption-dependent barriers applied to four phenomenological routes. This does not constitute a publishable methods or catalog paper in Physical Review D.