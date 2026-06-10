# P1A 2026-06-04_R6clean — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 30.2s

---

Referee report on P1A — “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter”

I have reviewed the manuscript exclusively from the point of view mandated by PRD methodology referees: mathematical soundness, statistical validity, internal consistency, dimensional analysis and traceability of every quantitative statement in the Abstract and Conclusions.  All page numbers below refer to the PDF pagination visible in the submission.  Findings are grouped by severity.

ESSENTIAL FINDINGS  (must be fixed before the paper can be considered)

P1A-E1  Abstract p. 1  
Problem The key quantitative claim “Ntot ≈ 92 post-bounce e-folds” is repeated throughout the paper but no derivation trace is given.  Eq. (11) defines Dinf ≡ e-3 Ntot  (dimensionaless) but nowhere is Dinf linked unambiguously to the measured dark–energy density ρΛ.  The chain of equalities (Sec. II C 1, Appendix B) openly admits it is a “phenomenological ansatz” rather than a computation.  
Required fix Provide a concrete derivation that starts from a Lagrangian term, propagates through the bounce and inflation, and outputs Ntot with a stated error bar.  Otherwise remove every instance of “Ntot ≈ 92” from the Abstract, Conclusions, Table I and Sec. XIV.

P1A-E2  Sec. II A 2, Eq. (6) and Appendix B  
Problem The primary parity-odd operator is dimension-1 off-shell but is immediately equated to a vacuum–energy density (dimension 4).  The manuscript acknowledges the mismatch yet continues to use the conversion.  This violates EFT power-counting and invalidates all subsequent amplitude estimates.  
Required fix Either (i) supply missing MPl powers so that the operator is genuinely dimension 4, or (ii) abandon the mapping to ρΛ and all downstream numerical results that rely on it.

P1A-E3  Throughout — mixing of σ significances  
Problem Null-model significances from different experiments (e.g. 3.6σ birefringence, 2.9σ ACT, 9σ LiteBIRD forecast) are repeatedly compared and algebraically combined as if they were on a common statistic without evidence they are.  In particular, Sec. XIII mixes the forecasted LiteBIRD detection significance (σ on β, internal instrument pipeline) with the Eskilt & Komatsu significance (likelihood on β from Planck+WMAP) and treats the difference in central values as a z-score.  These σ are not commensurate.  
Required fix Quote significances only in the native framework of each analysis, do not add or subtract them, and insert an explicit warning whenever different test statistics are juxtaposed.

P1A-E4  Use of unpublished “companion” work  
Problem All data analysis, MCMC chains, NaMaster validation and the claimed 109 galaxy-spin sample reside in four “companion works in preparation” [2, 6, 23, 46] that are not publicly available.  None of the numerical values in Table IV or the conclusions can therefore be verified.  
Required fix Upload the companion manuscripts to arXiv or include the relevant sections inside the current paper, and deposit the chains and code in a public repository that can be accessed now, not “upon request”.

P1A-E5  Galaxy-spin null result — estimator not pre-declared  
Problem The ViT-Small classifier, selection criteria and bias audit are said to be in a companion paper.  The present paper does not name the pre-registered estimator, the decision threshold, or the procedure for look-elsewhere correction.  
Required fix Move the full estimator definition, hyper-parameter set, and pre-analysis plan into this manuscript or cite a public DOI that predates the analysis.

P1A-E6  Eq. (15) dimensional inconsistency  
Problem The ratio ∆θone-loop /∆θobs is stated dimensionless but the numerator still carries an energy unit (H0).  A factor of c or ħ is missing; the stated 10-58 suppression therefore has no dimensional meaning.  
Required fix Rewrite Eq. (15) in homogeneous units and recompute the numerical suppression.

P1A-E7  Duplicate barrier count  
Problem Barrier 8 is declared “not logically independent” of Barrier 14 but the paper still advertises “14 barriers, 13 independent”.  The same duplication exists in the Abstract, Sec. IX and Table II.  
Required fix Remove one barrier or re-number so the counting matches.

P1A-E8  Unsupported σ8 and H0 numbers in Table IV  
Problem Values stated to ±0.008 and ±1.06 are attributed to a Cobaya run that is neither shown nor cited.  
Required fix Provide the chain corner plot, Gelman–Rubin statistics, and an online link.

P1A-E9  Mixing of Planck-suppressed and loop-suppressed amplitudes  
Problem Route-2 “one-loop graviton” combines a factor αem /4π with MPl-1 in Eq. (15) and compares it to α/M extracted from birefringence, but α/M is never shown to be derived in the same scheme.  This conflates incommensurate suppression mechanisms.  
Required fix Either compute α/M in the same loop expansion or remove the comparison.

MAJOR FINDINGS  (significant revision required)

P1A-M1  Sec. X — proof of “perturbation transparency” ignores vector and fermion modes but conclusion is advertised as “all orders”.  Needs explicit statement of domain of validity.

P1A-M2  Sec. IV Scope — paper concedes that two operators (gravitational Chern-Simons and parity-odd four-fermion) are omitted, yet still claims a no-go theorem.  Provide quantitative treatment or soften the claim.

P1A-M3  Page length — 21 pages of main text + huge appendices for what reduces to a dimensional argument.  A focused methodological letter could do this in ≤ 10 pages.

P1A-M4  LiteBIRD forecast uses β central value 0.27° without propagating Planck covariance; no Fisher matrix or noise model is shown.  Provide the forecast calculation.

P1A-M5  Several phrases duplicated: “canonical canonical-mask” (p. 15, line 4), “non-propagating algebraic” (p. 6) etc.  Clean.

P1A-M6  Uses “σ(fNL) ≈ 0.7 from Heinrich et al.” without showing how GR-projection and photometric red-shift degrade it to 1.0.  Need explicit error propagation.

MINOR FINDINGS  (should be addressed)

P1A-m1  Eq. (9) uses γ in denominator twice; once is sufficient — typographical.

P1A-m2  Footnote in Table IV cites “Cobaya v3.6.1” — current release is v3.7.  Quote the exact commit to ensure reproducibility.

P1A-m3  Reference formatting inconsistent: some journal names abbreviated, some spelled out.

P1A-m4  Signs of fNL (“−35/8”) occasionally miss the minus sign ( e.g. bottom of p. 1 ).

NITs

P1A-n1  Missing space in “Sec.XIII”.

P1A-n2  “bounce-era” sometimes hyphenated, sometimes not.

P1A-n3  Typo “pseudoscalar mass-dim +1 rather then +4” (“then”).

——————————————————————————————————————

## Summary recommendation  
MAJOR REVISIONS

The manuscript contains interesting ideas but, in its present form, fails multiple methodological requirements of PRD: core numerical claims are not derived, incompatible σ values are mixed, the main data analyses rest on unpublished companion work, and dimensional consistency is unresolved.  A thorough rewrite addressing the ESSENTIAL items listed above is necessary before the paper can be re-evaluated.