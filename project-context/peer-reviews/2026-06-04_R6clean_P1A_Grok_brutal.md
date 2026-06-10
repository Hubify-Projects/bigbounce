# P1A 2026-06-04_R6clean — Brutal-honesty journal referee (treating this as a real PRD submission)

**Model**: `grok-4.3`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 14.4s

---

**Referee Report**

**P1A-B1 (ESSENTIAL)**  
Section: Abstract (p. 1)  
Problem: The abstract opens with a claim of assessing “four enumerated minimal-ECH spin-torsion channels” and reporting “13 logically-independent mechanism-class constraints,” yet immediately qualifies that the routes “are not proven to be a complete diffeomorphism-invariant operator basis,” that the dark-energy mapping “rests on a phenomenological on-shell scaling ansatz whose off-shell mass dimension is +1 rather than +4,” and that the result is only “channel-level” rather than operator-level. The abstract therefore does not accurately summarize what the body proves; it advertises a closure result while embedding the decisive limitations inside the same paragraph.  
Required fix: Rewrite the abstract to state, in the first two sentences, that the paper demonstrates the failure of four specific phenomenological routes under an explicit on-shell scaling ansatz and lists known obstructions; remove all numerical counts of “barriers” and “branches” from the abstract.

**P1A-B2 (ESSENTIAL)**  
Section: Abstract and Sec. I (pp. 1, 3)  
Problem: The manuscript repeatedly states that key numerical results (H0 = 67.68 ± 1.06, ∆Neff ≈ 0, SPHEREx forecasts at 3–5σ, etc.) are taken from “companion work in preparation [6]” or “Paper I(b) [6]” that “are documented internally rather than as externally citable arXiv-posted numbers.” The present text is therefore not self-contained; the central amplitude-closure claim rests on unpublished MCMC chains.  
Required fix: Either include the relevant MCMC chains, convergence diagnostics, and likelihoods as appendices or supplementary material, or remove all quantitative cosmological-parameter statements that depend on the unpublished analysis.

**P1A-B3 (ESSENTIAL)**  
Section: Throughout (e.g., Sec. IX, Table II, Sec. XIV D)  
Problem: The paper presents 14 “mechanism-class constraints,” yet explicitly notes that Barrier 8 is “subsumed by B14” and that several others (Barriers 5–7, 9, 13) are “known results” or “structural/philosophical observations” included only for completeness. The headline count of 13–14 independent barriers is therefore inflated; the actual new ECH-specific content is a much smaller subset.  
Required fix: Provide a single, clearly labeled table or list that distinguishes (a) genuinely new calculations from (b) standard Planck-suppression or attractor arguments already in the literature. Remove the inflated numerical count from the abstract, introduction, and conclusions.

**P1A-B4 (MAJOR)**  
Section: Sec. II C 1 and Appendix B (pp. 6–7, 19)  
Problem: The dark-energy identification ρΛ = Ξ MPl^4 is repeatedly labeled a “phenomenological on-shell scaling ansatz” whose off-shell dimension is +1. The entire amplitude-closure argument and the quoted Ntot ≈ 92 figure rest on this ansatz. No derivation is supplied, and the text acknowledges that the missing mass-dimension factors “do not arise from off-shell EFT counting.”  
Required fix: Either derive the required dimension-+4 operator from a controlled EFT expansion (including all necessary powers of MPl in the coefficient) or reframe the paper as an exploration of the consequences of an explicit phenomenological ansatz rather than a “closure” result.

**P1A-B5 (MAJOR)**  
Section: Paper length and structure (21 pages)  
Problem: The manuscript is 21 pages long, yet its central result is a negative statement: four enumerated phenomenological routes fail at the amplitude level under a set of already-known obstructions plus one basic observation (torsion vanishes for canonical scalars). The length is driven by repetitive barrier lists, multiple tables, and extensive hedging language rather than by new derivations.  
Required fix: Reduce to a concise Letter or short article (≤ 8–10 pages) that states the four routes, the single new observation (perturbation transparency), and the amplitude estimates. All “foundations,” “branches,” and philosophical barriers should be removed or relegated to a short supplementary note.

**P1A-B6 (MAJOR)**  
Section: Sec. X (pp. 14–15)  
Problem: The “perturbation-transparency theorem” is presented as the central positive result, yet its proof consists of five elementary steps: canonical scalars have zero spin density, torsion vanishes, the connection reduces to Levi-Civita, the Holst term becomes the Pontryagin density, and a total derivative does not affect equations of motion. This is a direct consequence of the algebraic Cartan equation and was already implicit in Hehl et al. (1976) and subsequent ECH literature.  
Required fix: Either demonstrate that the result is new at the level claimed or relegate it to a brief remark rather than a numbered “theorem.”

**P1A-B7 (MINOR)**  
Section: Sec. IV Scope paragraph and abstract (pp. 1, 8)  
Problem: The text repeatedly emphasizes that the Jackiw–Pi term and the parity-odd four-fermion partner are “excluded from the enumeration” and “left to a follow-up operator-level analysis.” This qualification appears in the abstract, introduction, and Sec. IV, creating unnecessary repetition.  
Required fix: State the scope limitation once, in a single dedicated paragraph, and remove all duplicate phrasing.

**P1A-B8 (NIT)**  
Section: Multiple locations (e.g., pp. 3, 5, 12, 15)  
Problem: The manuscript contains numerous forward references to “companion works in preparation” and internal labels (“Paper I(b)”, “Paper II”, “Paper IV”). While not strictly version-history language, this pattern makes the text read like an internal project log rather than a standalone journal article.  
Required fix: Minimize such references; retain only those that are indispensable and move the remainder to a single footnote.

**P1A-B9 (NIT)**  
Section: Sec. II A 2 and Appendix B (pp. 5, 19)  
Problem: The text states that the (Treh/MGUT)3/2 prefactor “is the dimensional-analysis-aesthetic estimate from naive scaling” and “is not calculated from a thermal partition function.” This is an honest admission but is buried inside a long paragraph.  
Required fix: Move the admission to a single, prominent sentence in the main text.

**Summary recommendation**  
MAJOR REVISIONS

The manuscript presents a channel-level negative result whose core ingredients are standard Planck suppression, the algebraic nature of torsion, and an explicit phenomenological ansatz whose mass dimension is acknowledged to be incorrect. The 21-page length, the inflated count of “independent barriers,” the heavy dependence on unpublished companion papers for all quantitative claims, and an abstract that simultaneously advertises and undermines its own conclusions together render the paper unsuitable for publication in its current form. A drastically shortened, self-contained version that states the four routes, the single elementary observation about scalar perturbations, and the amplitude estimates without narrative inflation could be reconsidered, but the present submission requires major surgery.