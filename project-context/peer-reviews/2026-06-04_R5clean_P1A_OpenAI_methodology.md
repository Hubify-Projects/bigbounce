# P1A 2026-06-04_R5clean — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 20.7s

---

Referee report on P1A  
Round 2026-06-04_R5clean – Methodology/rigor assessment for Physical Review D  

----------------------------------------------------------------  
FINDINGS  

P1A-E1  
Section II A / pp.5-6  
Problem  
Eq. (6) carries mass–dimension +1, yet the manuscript proceeds to equate the on-shell value of this operator with ρΛ (mass–dimension +4) through the “phenomenological scaling ansatz” of Eq. (B2).  All subsequent numerical statements (Ξ, Ntot≈92, the claimed 10-5 fine-tuning relief, etc.) depend on this dimensional jump. No controlled EFT derivation, loop computation, or matching calculation is supplied.  
Required fix  
Either (i) supply a derivation that produces a bona-fide dimension-4 operator (e.g. show explicitly that three additional powers of MPl are generated after integrating out heavy modes) together with a calculable coefficient and uncertainty; or (ii) remove every quantitative claim that relies on Eq. (B2) (including the 13 “barriers” that invoke the scaling) and rewrite the paper as a conceptual note with no numerical statements.

P1A-E2  
Abstract + Sec. IV Scope / pp.1 & 8  
Problem  
The manuscript claims “channel-level closure of the four enumerated minimal-ECH dark-energy routes”, yet it explicitly omits two parity-odd operators (Jackiw–Pi gravitational Chern–Simons R∧R̃ and the γBI2 /(γBI2+1) ·8πG axial four-fermion) and several dimension-6 torsion operators.  Claiming closure while leaving recognised channels un-analysed is an over-statement.  
Required fix  
Either (a) analyse the missing operators quantitatively, or (b) weaken every statement of “closure” to “closure of the specific four routes treated here” and insert a conspicuous caveat in abstract and conclusions.

P1A-E3  
Throughout (e.g. Sec. II B, Sec. XII A)  
Problem  
Core numerical results (H0 , σ8 , ∆Neff posteriors; NaMaster validation; ALP parameter fits) are said to live in companion papers [6], [2], [46] that are “in preparation”.  None of the chains, likelihoods, or test statistics are available to the referee or the reader, so the internal arithmetic cannot be audited.  
Required fix  
Before publication deposit the full companion material (chains, likelihood files, covariance matrices, codes) on a public repository or in an Appendix and cite a DOI.  The present manuscript must be reviewable stand-alone.

P1A-E4  
Sec. IV B (Route 2) / p.9  
Problem  
Dimensionless ratio Δθone-loop/Δθobs is “∼10-58 –10-60” but the numerator originally lacked a factor MPl.  The author adds it post-hoc in prose.  No explicit formula or uncertainty propagation is provided.  
Required fix  
Write the full algebra with units carried through, quote the numerical value with its propagated uncertainty, and show that the conclusion (≳30 orders suppression) is insensitive to regularisation choice.

P1A-E5  
Sec. XI (Hybrid loophole) / p.15  
Problem  
Seven “loophole” models are dismissed without any calculation (“was never implemented computationally”).  Yet the dismissal is used to support the closure claim.  
Required fix  
Either drop Sec. XI entirely or provide at least order-of-magnitude quantitative tests for each loophole.

P1A-E6  
Sec. III A + XIII / p.7 & 16  
Problem  
σ values from different null models are treated on the same footing: a projected LiteBIRD error σ(β)=0.03° is compared to the already-measured βobs=0.342°±0.094° as if LiteBIRD will yield a 9 σ detection, ignoring the existing 0.094° uncertainty.  This mixes different procedures and over-claims significance.  
Required fix  
Rewrite the comparison using the correct formula for significance of an update on an existing measurement: σcombined² = σPlanck² ⊕ σLiteBIRD².  Re-evaluate the forecasted significance.

P1A-E7  
Data/Code availability statement / p.18  
Problem  
The GitHub repository quoted returns 404 at time of review.  
Required fix  
Provide a working permanent link (e.g. Zenodo DOI) containing all scripts and data required to rerun every figure and number.

P1A-E8  
Statistics / Sec. VI-VII  
Problem  
No evidence that a primary estimator (e.g. for galaxy-spin dipole or birefringence amplitude) was pre-registered before the data were examined, raising a risk of post-selection bias.  
Required fix  
Explain which estimator was fixed a priori and point to a dated repository commit or lab-notebook entry; otherwise flag the results as exploratory and adjust significance claims.

P1A-M1  
Sec. II C 1   (Inflationary dilution)  
Problem  
Key factor (Treh /MGUT)3/2 asserted “from dimensional-analysis aesthetics”; no derivation, error bar or citation.  
Required fix  
Provide a calculation (thermal phase-space integral) or give a conservative uncertainty and propagate it through to the Ntot figure.

P1A-M2  
Sec. V (Galaxy spin data)  
Problem  
Refers entirely to Paper IV [23] for methods, accuracy, sample size, bias tests.  None are summarised here, so reproducibility is impossible from this manuscript alone.  
Required fix  
Add a concise but complete description of catalogue selection, classifier performance, null-test suite, and the final dipole estimator value with uncertainty.

P1A-M3  
Eq. (17) / p.10  
Problem  
Rotation angle β formula assumes ρθ dominated by a coherently oscillating scalar; stochastic ALP field or mis-alignment regime changes the relation.  
Required fix  
State the regime explicitly and discuss robustness.

P1A-M4  
Duplicate phrases & artefacts  
Problem  
Multiple instances of internal project codes “hUBIFY-2026-00X”, “IMPLEMENTATION MAP.md”, “∆Neff tension closure attributable to ECH” inside main text.  
Required fix  
Strip all internal management tags.

P1A-M5  
Version-history language  
Problem  
Phrases like “this paragraph replaces the single-paragraph forward reference of earlier versions” remain.  
Required fix  
Remove.

P1A-MINOR6  
Abstract line 10  
Problem  
Duplication “are accordingly not predictions of ECH itself, but bounce-class and GR+ALP-class observables” (repeats the same idea twice).  
Required fix  
Delete redundancy.

P1A-NIT1  
Typos: “phys kbounce ”, missing spaces around superscripts, inconsistent equation punctuation.  
Required fix  
Proof-read.

----------------------------------------------------------------  
## Summary recommendation  
MAJOR REVISIONS  

The manuscript addresses an interesting question (whether minimal Einstein–Cartan–Holst gravity can source dark energy) but the current version relies on undocumented companion material, an un-derived scaling ansatz that violates dimensional analysis, and over-statements of “closure” while omitting known operators.  Key numerical results cannot be checked, several statistical comparisons mix incomparable σ values, and internal project artefacts remain.  A rigorous derivation (or removal) of the scaling relation, public release of all supporting calculations, and accurate statistical treatment are required before the work can be judged on its scientific merits.