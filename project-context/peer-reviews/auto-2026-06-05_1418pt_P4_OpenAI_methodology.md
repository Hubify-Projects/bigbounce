# P4 auto-2026-06-05_1418pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `o3-2025-04-16` [FALLBACK from gpt-5]
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (2688 chars)
**Wall time**: 135.0s

---

Referee report for “Survey-Scale Galaxy Chirality with Equivariant TTA: A −0.122 σ Subsample-Mask ℓ = 1 Null …’’  (10 pages, tag P4)

I have audited every numerical statement, equation and table in the manuscript against the text that accompanies it and against straightforward recomputations.  The study is interesting and potentially useful, but the present version does not meet PRD methodological standards.  My detailed findings follow.

------------------------------------------------------------------------
FINDINGS
------------------------------------------------------------------------

ID codes:  P4-E# = ESSENTIAL P4-M# = MAJOR P4-m# = MINOR P4-n# = NIT

P4-E1 Abstract & p. 4/Table III  
Text:  “post-MASTER canonical-mask direct-MC residual is +3.64 σ ( … pMC = 0.030, i.e. ≈ 1.9 σ Gaussian-equivalent)”.  
Problem:  The same quantity is quoted as +3.64 σ and 1.9 σ in the same sentence.  The paper later contrasts this 3.64 σ with other σ values, treating it as a 3–4 σ result.  
Fix:  Adopt ONE definition.  Either quote the moment-ratio z = Δ/σnull only (then it is 3.64 σ) or quote the rank-based significance only (then it is 1.9 σ).  Mixing them is misleading.  Make the same choice everywhere the figure “3.64 σ’’ is used.

P4-E2 p. 4/Table III and p. 5 text  
Text:  significance values > 3 σ are derived from just NMC = 500 Monte-Carlo realisations.  
Problem:  With 500 draws the sampling error on σnull itself is 1/√(2NMC) ≈ 3.2 %, corresponding to ±0.12 σ for a 3.6 σ claim — not negligible.  In addition, a Gaussian tail at 3–4 σ cannot be reliably estimated from 500 draws.  
Fix:  Increase the MC pool by at least an order of magnitude (≥ 5 000, preferably ≥ 50 000) or provide an analytic variance estimate verified by convergence tests, and update every quoted σ that depends on those draws.

P4-E3 p. 1 headline, p. 6 Appendix E  
Inconsistent size of the “high-confidence’’ subsample:  
• Abstract: “471 049 high-confidence per-spiral after peq > 0.9”  
• § VI A: injection–recovery uses N = 471 049 (same).  
• Appendix E: “HC-strict (peq > 0.8, N = 624 660)”.  
Problem:  Two incompatible definitions of the same control sample.  
Fix:  Give one unambiguous definition (threshold, N) and propagate the correct value to every place it is used (including the falsification criterion and the injection floor).

P4-E4 Throughout (e.g. p. 3 § III A, p. 6, Table I)  
σ values from different null hypotheses are juxtaposed without explicit warning in several sentences, despite the general disclaimer.  Example: “Equivariant averaging collapses the real-space dipole from 2.31 σ to 0.43 σ; MASTER deconvolution … collapses the pseudo-Cℓ to −0.122 σ.”  
Problem:  The reader inevitably compares those numbers.  
Fix:  Each time σ from two different null procedures are placed in the same sentence or paragraph add an explicit reminder (“not directly comparable’’) OR express the second figure in the same null if comparison is intended.

P4-E5 p. 2 § II B  
Training-label ground truth accuracy is only 69.9 % yet § VI A claims sub-percent sensitivity (0.75 % dipole amplitude).  The dilution factor g = 2a–1 ≈ 0.398 is mentioned but not propagated into the Fisher-limit estimate or the falsification criterion.  
Fix:  Re-derive the advertised 0.75 % sensitivity including the multiplicative 0.398 dilution and update the falsification threshold accordingly, or present an external validation demonstrating that the catalogue-wide accuracy is substantially higher than the conservative 70 %.

P4-M1 p. 3 Equation (2)  
Claim: “flip-swap correlation = 1.000”.  That is mathematically impossible once finite numerical precision is considered.  
Fix:  Quote the measured correlation to three significant figures (e.g. 0.999 7) and explain how it was evaluated.

P4-M2 p. 1 Abstract  
“99.3 % of its observed amplitude” is quoted for leakage reproduction.  Using the numbers in Table IV (1.685 vs 1.696) the ratio is 0.9935 = 99.35 %, acceptable, but the uncertainty (±0.007×10⁻²) implies ±0.4 % on this ratio.  State this uncertainty explicitly.

P4-M3 p. 4/Table I  
Nmap weighted = 5 547 858 (sum of all galaxies in the mask) is labelled “exceeds Ncatalog,spiral because it includes non-spirals (∼62 %)”.  5.55 M/8.47 M = 0.66, not 1.62.  Either the weighting scheme discards many objects or the description is incomplete.  
Fix:  Clarify precisely which objects are counted in Nmap weighted, and why only 65 % of the full catalogue enter the weight map.

P4-M4 p. 7 Appendix A  
The text states that the monopole is subtracted before field construction “so ℓ = 0 is removed from the input field, and the MASTER matrix does NOT include ℓ = 0”.  However the derivation of the coupling matrix in MASTER assumes the full set of modes.  Provide a short derivation or citation showing that removing ℓ = 0 prior to deconvolution does not bias the ℓ = 1 estimator (or redo the deconvolution with the standard prescription).

P4-m1 Title & multiple places  
“subsample-mask” and “canonical-mask” appear in several variants (“strict-superset subsample mask”, “canonical-N MASTER”, “canonical-canonical mask once) creating confusion.  
Fix:  Standardise the terminology and eliminate the duplicate phrase.

P4-m2 p. 3 § III C  
Only horizontal flips are used “because in-plane rotations do not change chirality”.  A 90° rotation followed by a reflection does.  The justification is incomplete.  Provide a short statement quantifying the residual rotation-equivariance error and its impact on the dipole estimator.

P4-m3 p. 6 § VI  
Look-elsewhere correction is said to use ∼ 650 directions without giving the HEALPix NSIDE or step size.  State the grid explicitly so that others can reproduce the LEE factor.

P4-n1 p. 5, caption Table III  
“canonical‐N” should read “canonical-mask” for consistency.

P4-n2 References  
Check arXiv identifiers: e.g. Ref. [20] cites arXiv:2305.02268 but Cosmoglobe DR1 is arXiv:2305.02267.

------------------------------------------------------------------------
## Summary recommendation
MAJOR REVISIONS

The manuscript contains several internal inconsistencies (most critically E1, E2, E3, E4, E5) and relies on Monte-Carlo sample sizes that are inadequate for the claimed ≥ 3 σ significance levels.  These must be corrected before the analysis can be trusted and before the paper can be considered for publication in PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS  
(tagging continues the sequence of the first report)

----------------------------------------------------------------
ESSENTIAL
----------------------------------------------------------------
P4-E6 Table III significance arithmetic  
The quoted significances do not follow σ = (Cℓ – ⟨Cℓ⟩null)/σnull for the numbers in the same row.  
• ℓeff = 4: 3.210/0.804 = 3.99 σ, table prints +6.097 σ.  
• ℓeff = 9: –0.248/0.574 = –0.43 σ, table prints +2.232 σ.  
• ℓeff = 14: –0.387/0.446 = –0.87 σ, table prints +2.626 σ.  
• ℓeff = 19 and 24 show the same sign flip.  
All subsequent text (e.g. § IV D “ℓ = 2 > ℓ = 1 broadband structure”) uses those erroneous σ’s.  Re-compute every significance in Table III, propagate the corrected values wherever they are cited, and revise the interpretation that depends on the over-stated low-ℓ excess.

P4-E7 Contradictory units for Cℓ between Tables III and IV  
Table III gives Cℓ in 10⁻⁶ sr, while Table IV quotes the pre-MASTER pseudo-Cℓ (same observable) as 1.696 × 10⁻² with no unit.  A factor ≈10⁴ jump is physically impossible for a single deconvolution step.  Specify consistent units everywhere and show the conversion that links the two tables, otherwise the leakage-channel claim cannot be verified.

----------------------------------------------------------------
MAJOR
----------------------------------------------------------------
P4-M5 Fisher-floor arithmetic (§ VI A)  
From σ(A/2) ≈ 0.048 % the 3 σ floor is 3 × 0.048 % = 0.14 %, yet the text states “∼ 0.29 %”.  Either the base σ is double what is printed or the 0.29 % figure is a leftover from an earlier draft.  Correct the calculation and adjust the discussion of the sensitivity floor.

P4-M6 Gaussian p–σ conversion error (abstract and § IV D)  
pMC = 0.030 corresponds to 2.17 σ (two-sided Gaussian), not 1.9 σ.  The mis-conversion appears in the abstract, p. 4, and Appendix D.  Fix the mapping consistently or quote p only.

----------------------------------------------------------------
MINOR
----------------------------------------------------------------
P4-m4 Loss-function dimensionality (Appendix B eq. (B1))  
The cross-entropy term LCE is in nats, the consistency term is a squared Euclidean norm of probabilities (dimensionless).  Combining them without a scale factor makes λ = 0.5 unit-dependent.  State explicitly that LCE is converted to a dimensionless average (e.g. divided by ln Nclasses) or justify numerically that the mixture is well-behaved.

----------------------------------------------------------------
With these additional issues the manuscript requires another full technical revision before the results can be trusted.