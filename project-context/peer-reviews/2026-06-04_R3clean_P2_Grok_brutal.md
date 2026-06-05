# P2 2026-06-04_R3clean — Brutal-honesty journal referee (treating this as a real PRD submission)

**Model**: `grok-4.3`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 17.2s

---

**Referee Report: P2**

**Paper:** Testing the Matter Bounce with Primordial Non-Gaussianity: SPHEREx Forecasts, with a MegaMapper Outlook  
**Round:** 2026-06-04_R3clean  
**Length:** 22 pages

### ESSENTIAL findings

**P2-E1** Abstract (p. 1)  
Problem: The abstract states the headline post-systematic significance as ∼3–5σ (bispectrum-only) while burying the convention-sensitivity paragraph that halves all quoted numbers to ∼1.5–2.5σ if the Li & Brandenberger normalization is adopted. The abstract therefore does not honestly represent what the body proves under the full range of published conventions.  
Required fix: Rewrite the abstract to lead with the convention ambiguity and report both the Cai and Li–Brandenberger significances on equal footing; delete the claim that “the convention sensitivity should be resolved before SPHEREx data are interpreted” as a post-hoc hedge.

**P2-E2** Abstract & §II C (pp. 1, 5–6)  
Problem: The paper asserts that the Cai et al. value fNL = −35/8 is the correct Planck-convention normalization on the basis of an operator-algebra identity and a 0.5000 ratio check, yet simultaneously concedes that the Li & Brandenberger value halves every detection significance. No independent re-derivation of the four oscillatory integrals is performed.  
Required fix: Either (a) perform a complete, self-contained re-derivation of the in-in bispectrum or (b) present the entire forecast as conditional on an unresolved normalization choice whose resolution changes the result from a ≥3σ claim to a <3σ claim.

**P2-E3** §VI & Table II (pp. 10–12)  
Problem: Bayes factors are quoted as BF ∼10–17 (headline envelope) while the text demonstrates that the result is monotonically sensitive to the bounce prior width, the competitor prior width, and the GR marginalization parameter σGR. The recommended “headline” σtheory = 1.0 case is itself an arbitrary choice among several equally plausible widths.  
Required fix: Remove all numerical BF ranges from the abstract and conclusion; replace with a statement that the Bayes factor is prior-dependent and ranges from O(1) to O(10) under published theoretical uncertainties.

**P2-E4** §IV & §VII (pp. 8–9, 13)  
Problem: The 5.2–5.5σ optimistic figure is obtained by applying the Heinrich et al. Fisher matrix (computed at fNL = 0) directly at the bounce fiducial without re-derivation. The text acknowledges this is a “leading-order linearization” assumption but still presents the number as the headline forecast.  
Required fix: Either recompute the multi-tracer bispectrum Fisher matrix at the bounce fiducial or downgrade the significance claim to an order-of-magnitude estimate only.

### MAJOR findings

**P2-M1** Abstract & §V (pp. 1, 9)  
Problem: MegaMapper projections are presented as “3–7σ realistic” despite the instrument having “no finalized instrument design, no confirmed site, and no approved funding.” The text itself labels these “speculative motivation, not firm forecasts.”  
Required fix: Move all MegaMapper numerical projections to a short speculative paragraph or appendix; delete them from the abstract.

**P2-M2** §II B & §III B (pp. 3–4, 7)  
Problem: The claim that “no prior quantification of this overlap exists for the matter-bounce bispectrum (2009–2024)” is an unsupported literature-search assertion used to justify novelty.  
Required fix: Provide an explicit, citable literature search or remove the “first time” phrasing.

**P2-M3** §II C (pp. 5–6)  
Problem: The fNL = −35/8 prediction is conditional on six assumptions, two of which (faithful cubic-order transmission and negligible fermion torsion) are unverified at the required order. The text acknowledges this but still presents the value as a “minimally parameterized” benchmark.  
Required fix: State explicitly in the abstract and conclusion that the numerical forecasts apply only inside the Wilson-Ewing scalar-only subclass satisfying all six assumptions.

**P2-M4** Paper length (entire manuscript)  
Problem: 22 pages for a forecast recast that relies on published Fisher matrices, performs no new survey simulation, and whose central numerical result is convention-dependent. The contribution does not justify the length.  
Required fix: Shorten to ≤14 pages by moving the full null-space scan, all Monte-Carlo validation tables, the four-corner prior grid, and the GR-degradation scenarios to appendices or a companion note.

### MINOR findings

**P2-m1** §II A (p. 3)  
Problem: The statement that the six-monomial basis is “fixed by the Cai-physics-restricted vertex structure, not by purely abstract S3 symmetry” is repeated almost verbatim in two consecutive paragraphs.  
Required fix: Remove the duplicate sentence.

**P2-m2** §VI (p. 10)  
Problem: The parenthetical remark “(a rhetorical ‘>6 × 105’ figure appeared in an older draft…)” is review-log prose that should not appear in the body.  
Required fix: Delete the parenthetical.

**P2-m3** §IX D (p. 16)  
Problem: The joint (fNL, nfNL) Fisher significance of ∼9.9σ is presented as an “idealized-Fisher self-consistency check” while the Fisher inputs themselves are deferred to a companion artifact.  
Required fix: Remove the numerical 9.9σ claim until the companion artifact is public.

### NIT findings

**P2-n1** Throughout  
Problem: Inconsistent use of “bounce” vs. “matter bounce” vs. “quasi-dust matter bounce” without a single defining sentence early in the introduction.  
Required fix: Add one clarifying sentence in §I.

**P2-n2** Fig. 2 caption (p. 9)  
Problem: Caption refers to “multi-tracer, photo-z, bias, and GR systematics” but the figure itself shows only two curves.  
Required fix: Update caption or figure.

## Summary recommendation
**MAJOR REVISIONS**

The manuscript’s central claim—that SPHEREx can test the matter-bounce prediction at 3–5σ—is not robust under the published normalization ambiguity, relies on an unverified Fisher-matrix transfer, and is conditional on six assumptions two of which remain unverified at cubic order. The Bayes-factor results are prior-dependent at the level that changes the interpretation from “evidence” to “inconclusive.” The paper is also substantially over-length for a recast forecast. These issues require major revision before the work can be considered for Physical Review D.