# P1B 2026-06-04_R5clean — Brutal-honesty journal referee (treating this as a real PRD submission)

**Model**: `grok-4.3`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 11.1s

---

**Referee Report: P1B**

**P1B-E1 (ESSENTIAL)**  
Section: Abstract (p. 1) and throughout (e.g., Sec. III, p. 3; Appendix A, p. 9)  
Problem: Multiple instances of version-history language, internal audit tags, and review-log artifacts remain despite the stated “R5: all known artifacts stripped.” Examples include “iter2” chain references with exact UTC timestamps (“2026-05-18 07:53 UTC”), “earlier count erroneously quoted,” “a concern was raised that…,” “queued” (Appendix A: “and is queued”), repository tags (“paper1b-v1B.0.36”), and convergence-log prose (“R̂ − 1 = 0.00820 at N = 128,385”).  
Required fix: Remove every such phrase, timestamp, version tag, and reviewer-response narrative from the body, footnotes, and appendices. Replace with static, journal-appropriate statements only.

**P1B-E2 (ESSENTIAL)**  
Section: Abstract (p. 1) and Sec. VI (p. 6–7)  
Problem: The abstract states that the spectator-ALP analysis shows consistency with the published β = 0.342° ± 0.094° (3.6σ). The body (including fn. 4 and the explicit “∼25× misalignment tuning” disclosure) demonstrates that the spectator-consistent corner requires θᵢ ∼ 0.1, which is a substantial fine-tuning relative to the scanned prior midpoint. The abstract therefore does not honestly represent what the body proves.  
Required fix: Rewrite the abstract to state explicitly that the consistency holds only after a ∼25× fine-tuning of the misalignment angle and that the result is not an ECH-specific prediction.

**P1B-M1 (MAJOR)**  
Section: Entire manuscript; length statement (cover page)  
Problem: The paper is 10 pages. PRD methods/catalog papers are typically 15–30 pages. The actual scientific content is three heavily caveated null-consistency tests plus pipeline validation; the contribution does not justify even the lower end of the normal PRD length range.  
Required fix: Either expand substantially with new technical content or withdraw and resubmit to a shorter-format journal (e.g., Phys. Rev. Research or a methods note).

**P1B-M2 (MAJOR)**  
Section: Title, abstract, and Sec. I (p. 2)  
Problem: The title and framing present the work as part of the “ECH Spin-Torsion Program,” yet the body repeatedly states that none of the three analyses tests the ECH theory module itself (“NOT a spin-torsion theory module,” “not a distinctive ECH prediction,” “stock CAMB… carries no torsion modifications”). The title is therefore misleading.  
Required fix: Change the title to reflect that the paper contains only standard-ΛCDM proxy tests and pipeline validation unrelated to torsion modifications.

**P1B-M3 (MAJOR)**  
Section: Sec. V B (p. 6) and Sec. VII (p. 8)  
Problem: The manuscript repeatedly defers model-comparison statistics (AIC, BIC, ln B) to a “follow-up nested-sampling analysis” that is described as “queued.” No such analysis is provided, yet the paper still presents quintom-B claims at +4.3σ / −3.6σ.  
Required fix: Either perform and include the nested-sampling evidence calculation or remove all statements about quintom-B preference and σ-level departures from ΛCDM.

**P1B-m1 (MINOR)**  
Section: Sec. IV (p. 5) and Sec. VI (p. 6)  
Problem: Pipeline SNR values (20.32σ, 25.71σ) are reported alongside the published sky-detection significance (2.4–2.9σ). Although the text attempts to distinguish them, the numerical juxtaposition invites misreading.  
Required fix: Move all pipeline-SNR numbers to a dedicated “validation only” table or appendix and remove them from the main narrative.

**P1B-n1 (NIT)**  
Section: Table I caption and multiple footnotes  
Problem: Minor typographic inconsistencies (e.g., “a” footnote marker placement, repeated “the the” constructions in footnotes).  
Required fix: Standard proofreading pass.

**P1B-n2 (NIT)**  
Section: Appendix C (p. 9)  
Problem: The prior range θᵢ ∈ [0.5, 2] is retained while the spectator-consistent result is stated to lie at θᵢ ∼ 0.1. The tension between the sampled prior and the claimed spectator regime is noted only in footnotes.  
Required fix: Add a single clarifying sentence in the main text of Sec. VI.

## Summary recommendation
**MAJOR REVISIONS**

The manuscript is a short, heavily caveated technical companion whose central analyses are explicitly stated to be neither tests of the ECH framework nor competitive cosmological measurements. In its present form it contains multiple internal review artifacts, version-history language, and an abstract that does not accurately reflect the fine-tuning required for the ALP consistency claim. These are not cosmetic issues; they affect whether the paper meets PRD standards for a methods submission. A substantially revised version that removes all audit language, corrects the abstract, and either expands the technical content or is redirected to a shorter-format journal would be required before further consideration.