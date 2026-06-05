# P5 2026-06-04_R4fixed — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 38.0s

---

Referee Report on P5  
Round: 2026-06-04_R4fixed  
Length: 21 pp  

I have audited the manuscript for statistical‐method validity, derivation integrity, dimensional consistency, arithmetic correctness, error propagation and scalar traceability, following the assignment brief.  Findings are listed below.

────────────────────────────────────────  
FINDINGS  
────────────────────────────────────────  

ESSENTIAL  
P5-E1   Section VII A (pp. 9-10)  
Problem The authors claim that the largest Phase-2 sweep range (0.22 pp) “is below the wall- and void-class counting-statistics floors … so no (R s , λ th ) cell shows an inter-class range that exceeds the dominant per-class measurement uncertainty.”  
The counting-statistics σ for the cluster/filament classes at n≈4×10 5 is 0.079 pp, therefore a 0.22 pp difference is 2.8 σ for those classes and does exceed the respective floors.  
Required fix Re-evaluate the Phase-2 conclusion with the correct σ for all four classes; supply the corresponding p-values.  If the 0.22 pp range is significant for the large-n classes the headline “no environment dependence” must be re-phrased or the discrepancy otherwise explained.

P5-E2   Abstract & §VI A  
Problem Cluster class deviation −4.66 σ is dismissed as “tracking the catalog-wide monopole”, yet the residual after monopole subtraction (Table X) is still −1.11 σ, which is compatible, but the abstract continues to quote the raw −4.66 σ without context.  
Required fix Either quote only monopole-subtracted significances in the abstract/conclusions, or state explicitly that the quoted σ are with respect to 0.5 and therefore include the known classifier bias.  Current wording overstates significance.

P5-E3   Throughout (e.g. pp. 3, 7, 8, 11, 13)  
Problem Internal version-history language, file-path stubs and review-log artefacts (e.g. “pipelines/p5_desi_chirality/results/…”, “v1.7.37”, “internal companion artifact”) appear in the prose.  PRD does not allow such internal notes.  
Required fix Remove all repository paths, SHA lines, audit tags and change-log comments from the camera-ready text.  Retain only external, citable URLs or DOIs.

P5-E4   §V B (Pre-registration)  
Problem The “primary” estimator (DESIVAST void) was selected post-hoc after inspecting several classifiers.  No multiplicity correction is applied between the primary and the numerous secondary diagnostic paths.  
Required fix Supply a transparent family-wise error-rate accounting across all environment definitions tested, or re-structure the analysis into one pre-declared primary test and clearly labelled exploratory follow-ups.

P5-E5   §IX B / §XI  
Problem σ values from different null procedures (binomial half-test vs monopole-subtracted residual) are plotted on the same axes and compared directly (e.g. Fig. 3, Fig. 7) without specifying that they are on different reference scales.  
Required fix Label which σ refers to which null and never plot them on the same scale without conversion.

P5-E6   Data provenance  
Problem The entire analysis depends on the Paper IV chirality catalogue, which is “not yet peer-reviewed.”  Unless the catalogue itself is publicly archived with immutable checksum, the present paper is not reproducible.  
Required fix Deposit the exact catalogue revision (e.g. the Huggingface snapshot) in a DOI-minted repository and cite it in the reference list.

MAJOR  
P5-M1   §VII A (counting-statistics floor)  
Provide explicit derivation of the stated 0.08 pp, 0.6 pp, 2.4 pp floors and show the algebra that maps them to the sweep ranges.  A reader must be able to verify the numbers without running code.

P5-M2   §VI D (within-class density split)  
The χ² contingency p-value is reported as p < 10 −1000 .  This is beyond double precision and meaningless.  Quote p ≈ 10 −300  or “p ≪ 10 −10 ”.

P5-M3   §V (label-shuffle null)  
The permutation test is seeded with a hard-coded integer.  State whether that seed was chosen before looking at the results; otherwise supply the full permutation distribution or a randomisation protocol.

P5-M4   §VIII A  
0/6 overlap between V-Web void and DESIVAST void is used qualitatively, but a quantitative impurity estimate requires an exact confidence interval.  Give the Clopper-Pearson bound for the true concordance fraction at N=6.

P5-M5   Tables II, VI, VIII  
Too many significant digits are printed (e.g. 0.4980, 0.0007).  Round to the precision allowed by sampling error.

P5-M6   Appendix A  
The toy EFT operator is speculative and not gauge invariant (authors admit).  It should be clearly separated from results (perhaps moved to a short discussion paragraph) and introduced as conjecture, not as part of the methodological chain.

MINOR  
P5-m1   §III D Table I  
“p50 separation 0.0066′′” – supply uncertainty or rounding.

P5-m2   §IV A step 8  
Poisson equation sign convention not specified; include it.

P5-m3   §V A Eq. (2)  
Write erfc −1 argument with parentheses; as printed it is ambiguous.

P5-m4   §VI B  
Logistic-regression coefficient 0.0059 has no units (per unit z?).  State units and standard error.

P5-m5   §VI E Figure 4 colour bar  
Colour scale saturates at |σ|≈3 but the max plotted is 4.13.  Rescale or note clipping.

P5-m6   References  
Ref. [12] Zenodo DOI is incomplete (needs https://doi.org/…).

NIT  
P5-n1 Duplicate phrase “catalog catalog-wide” on p. 2.  
P5-n2 “look-elsewhere correction” sometimes abbreviated “LEE” before definition.  
P5-n3 Mixed UTF-8 primes (′′) and ASCII quotes ("), standardise.  
P5-n4 Repeated footnote text “houston@hubify.com” appears in each section header – move to author block only.

────────────────────────────────────────  

## Summary recommendation  
MAJOR REVISIONS  

The analysis is generally careful and technically interesting, but several methodological mis-statements (E1, E2, E5) and the absence of a fully pre-declared primary test (E4) undermine the headline claim.  Internal audit paths, version strings and un-citable artefacts (E3) must be removed before publication.  With these issues corrected and a rigorous, unified significance accounting, the work will be publishable.