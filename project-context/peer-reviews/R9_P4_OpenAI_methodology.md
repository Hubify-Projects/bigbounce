# P4 R9 — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 33.5s

---

Referee report on P4  
“Survey-Scale Galaxy Chirality with Equivariant TTA …”

I have evaluated the manuscript exclusively from the methodological/statistical-rigour perspective requested by PRD.  All line/page numbers below refer to the PDF provided; if the editors’ pagination differs, please match by section titles or quoted phrases.

FINDINGS  
ESSENTIAL = must be fixed before the paper can be considered;  
MAJOR = substantial revision strongly advised;  
MINOR = desirable improvements;  
NIT = cosmetic/typographical.

--------------------------------------------------------------------
ESSENTIAL
--------------------------------------------------------------------

P4-E1  Sect. IV C/Table I, p.4  
Problem: All headline significances (–0.122 σ, +3.64 σ, etc.) are derived from null distributions with only NMC = 500 randomisations.  For a Gaussian variable the fractional rms error on the estimated standard deviation is √2/(NMC-1) ≃ 6.3 %.  A quoted “–0.122 σ” therefore has an uncertainty of ≃0.008 σ on σ itself and ≃0.007 on the z-score, i.e. ≈6 % of the entire effect.  For the +3.64 σ canonical value the width of the null is also uncertain by ≈6 %, so the formal significance could shift by ±0.2 σ.  
Required fix: Increase all Monte-Carlo null samples to NMC ≥ 10 000, recompute σnull and every z-value that depends on it.  Update all affected text, tables and figures.

P4-E2  Sect. III A/IV C, throughout  
Problem: The “per-pixel label-shuffle” and “binomial-monopole” nulls preserve galaxy positions and therefore ignore cosmic variance of the underlying density field.  This necessarily under-estimates the variance of any large-scale statistic (Cℓ, hemisphere asymmetry, dipole fit).  No attempt is made to add a cosmic-variance term or to show that it is negligible relative to the random-label term.  
Required fix: Supply a null that includes structure (e.g. jack-knife over large sky patches or lognormal mocks matching the n(z) and selection), re-evaluate all σ and p-values, and state the combined variance formula.

P4-E3  Table I & text, p.4  
Problem: “Nmap weighted = 5 547 858 > Ncatalog spiral = 3 201 160”.  The analysis evidently counts galaxies with weights that can exceed unity (or counts galaxies multiple times), but the weighting scheme is not described.  Significance and fsky are meaningless without knowing how this duplication arises.  
Required fix: Precisely define Nmap weighted, the weighting function, and show that the weighting conserves the total effective number of galaxies.  Report the impact of weighting on shot noise.

P4-E4  Sect. VI A, p.6  
Problem: The “50 % recovery at 3 σ threshold A ≈ 0.75 %” is derived from an injection test performed on only the 471 049 “HC” galaxies, not on the 3.2 M spirals actually entering the dipole analysis.  Sensitivity and falsification criteria are therefore mis-stated.  
Required fix: Redo the injection–recovery on the full analysis sample (or demonstrate analytically that the threshold rescales trivially with N and fsky).

P4-E5  Table II, p.4  
Problem: The quoted deviations from 0.5000 do not match the numbers shown.  
• Raw tier: (0.5079-0.5000)/0.0003 = 26.3 σ, not 28.8 σ.  
• Equivariant tier: (0.5000-0.4974)/0.0003 = 8.7 σ, not 9.5 σ.  
Arithmetic inconsistencies immediately undermine confidence in every quoted σ.  
Required fix: Audit every entry in Tables I–IV and text, propagate correct errors, and supply a machine-readable notebook reproducing each scalar in the abstract and conclusions.

P4-E6  Sect. IV D, p.5  
Problem: The monopole-only leakage null is used to argue that the +3.64 σ canonical residual is “consistent with leakage”, yet the data/ null difference is +1.68 σ (Table IV), i.e. formally rejected at p ≈ 0.09.  The conclusion does not follow from the statistics.  
Required fix: Provide a quantitative goodness-of-fit test that includes the full covariance of the leakage model.  If the residual remains ≥2 σ the interpretation must be stated as an open systematic, not “explained”.

--------------------------------------------------------------------
MAJOR
--------------------------------------------------------------------

P4-M1  Sect. II B and App. B  
The training labels are 67.6 % predictions of another machine (CE-ResNet).  This couples the analysis to unknown systematics in that network, yet no systematic error term is assigned.  Provide a separate null based only on human-labelled data or include a propagated label-noise term in every σ.

P4-M2  Abstract & throughout  
The title and abstract highlight a “–0.122 σ null” as if it were a precise measurement; but any z-score this small is completely dominated by Monte-Carlo noise and cosmic variance (see E1/E2).  The language must be toned down: “consistent with isotropy within current statistical precision” is accurate; “we report a –0.122 σ null” is not.

P4-M3  Sect. III B, App. B  
Flip-equivariant loss (eq. B1) is introduced, but no ablation experiment demonstrates that it actually removes the raw 0.79 % bias.  Show before/after numbers on an independent validation set.

P4-M4  Sect. V A, p.5  
A comparison with Shamir is made without matching footprint, depth or selection.  Present a quantitative estimate of how much of the discrepancy can be attributed to those differences, or re-phrase as “qualitative”.

--------------------------------------------------------------------
MINOR
--------------------------------------------------------------------

P4-m1  Sect. IV C, p.4 “σ values … are not directly comparable…; see Table II for the mapping” – Table II does not contain such a mapping.  Add a column explicitly stating which null each σ uses.

P4-m2  Sect. IV D: “apodized-mask test (+3.57 σ … essentially unchanged)”.  Give the corresponding p-value; “essentially unchanged” is qualitative.

P4-m3  Sect. I, p.1 first paragraph: “8.47 M sources, 471  049 high-confidence per-spiral after peq CW > 0.9” → number disagrees with later statement “HC-spiral subsample (N = 471 049)” which uses peq > 0.6.  Harmonise cuts and counts.

P4-m4  Several places “canonical-mask” is repeated twice (“canonical canonical-mask”).  Remove duplication.

P4-m5  PACS codes: 98.62.Ai “Galaxies: classification, general” no longer exists in the updated Physics and Astronomy Classification Scheme.  Update or delete.

--------------------------------------------------------------------
NIT
--------------------------------------------------------------------

P4-n1  Title: the en-dash before “0.122σ” renders as a minus sign; consider re-phrasing to avoid the impression of a negative detection.

P4-n2  Many abbreviations (HC, pp-shuffle, CW/CCW) are used before definition in the abstract.  Define on first use.

P4-n3  Reference [32] is cited as 2.6 but repository shows v2.7 currently; pin the exact commit hash.

--------------------------------------------------------------------
## Summary recommendation
MAJOR REVISIONS

The manuscript contains valuable work – a public 8.5 M-object chirality catalogue and a careful attempt at bias control – but several methodological foundations are presently inadequate.  The null variance is under-sampled, cosmic variance is ignored, weighting is undocumented, and numerical inconsistencies remain in the basic σ calculations.  These affect every headline claim.  With a strengthened null simulation, corrected arithmetic, and a transparent weighting description, the paper could become a useful reference; until then it should not be accepted by PRD.