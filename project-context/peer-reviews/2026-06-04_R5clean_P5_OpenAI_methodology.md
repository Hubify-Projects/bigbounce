# P5 2026-06-04_R5clean — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 33.1s

---

Referee report on  
P5 – “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56 981 Void Spirals …”  
Round: 2026-06-04_R5clean  
Length: 20 pp


FINDINGS  
(ascending severity within each class)

ESSENTIAL  
P5-E1  Sec. V A, p. 5  
Problem Predicted monopole correction is treated as exact: σ_pred = 2 Δf_CW √N with Δf_CW = –0.0026 taken from Paper IV. The quoted Paper IV uncertainty (±2.79 × 10⁻⁴) is never propagated, so every σ_vs monopole, every Bonferroni threshold comparison and the claim that “all four classes fall within |σ_vs monopole|<1.15” ignore the ±11 % relative error on Δf_CW.  
Fix Carry the ±1 σ error of Δf_CW through Eq.(1) and through every downstream σ_vs monopole and Bonferroni calculation. Re-evaluate all acceptance / rejection statements with the propagated error.

P5-E2  Sec. IV, pp. 3-4  
Problem V-Web classification is performed in observed red-shift space but the paper repeatedly states that the primary headline is “RSD-immune”. No quantitative RSD budget is supplied; the finger-of-god & Kaiser terms can shift eigen-value signs near boundaries.  
Fix Either rerun the classifier on a Zel’dovich/BAO reconstructed real-space density or provide a quantitative upper bound on the fraction of galaxies that cross a λ_th boundary when σ_v/(a H) displacements are applied. Quote the resulting systematic on f_CW.

P5-E3  Sec. VI D, p. 7 & Table IV  
Problem Cluster class: observed σ = –4.66, predicted σ_pred = –3.28 (on Paper IV monopole). The 1.38 σ difference is labelled “within order-unity”, yet the same table uses a Bonferroni 3 σ cutoff elsewhere. Treating 1.38 σ as negligible is a logical inconsistency.  
Fix Either show that the 1.38 σ residual is not significant after full systematic propagation (including monopole uncertainty per E1 and RSD per E2) or withdraw the statement that the cluster deviation is completely explained by the monopole.

P5-E4  Sec. V B, p. 5  
Problem Primary estimator (DESIVAST void classification) is chosen post-hoc (“not pre-registered”). The manuscript acknowledges the fact but still treats the DESIVAST path as confirmatory.  
Fix Provide evidence (time-stamped pre-analysis plan or git log) that the DESIVAST path was defined before looking at the environment-split chirality, OR re-classify the DESIVAST result as exploratory and adjust all p-values with a multiplicity factor that includes the choice of environment classifier.

P5-E5  Abstract & Sec. VIII, p. 11  
Problem Headline “no environment dependence above 0.22 pp” mixes nine different null procedures: binomial σ, permutation p, and monopole-subtracted σ. The value 0.22 pp is read off the Phase-2 sweep max-range but is never associated with a confidence level.  
Fix Attach an explicit confidence statement (e.g. 95 % CL upper bound on |Δf_CW|) derived from a single pre-declared statistic and its null distribution; do not mix incomparable nulls in the same sentence.

P5-E6  Sec. IX A, p. 13 and Fig. 7  
Problem Tempel FoF cross-validation uses a 1″ sky-match but SDSS DR10 positions have astrometric uncertainties ≳0.2″ and the DESI Legacy photometry positions used in Paper IV are deeper. No duplicate-resolution rule is given for multiple FoF galaxies within 1″.  
Fix Specify the full cross-match logic (tie-break rule, self-match radius sensitivity) and demonstrate that the FoF-vs-V-Web concordance is stable (Δf_CW changes <0.02 pp) when the acceptance radius is varied from 0.7″ to 1.5″.

P5-E7  Whole text  
Problem Several σ values from different procedures are placed on the same numerical scale without qualification (binomial σ_from-half, empirical max-stat σ, logistic-regression z). Violates instruction #7.  
Fix Insert qualifying language every time two σ values come from different nulls or, preferably, convert all to p-values before comparison.


MAJOR  
P5-M1  Sec. III D, Table I  
Problem Stated “p50 separation 0.0066″” is below GAIA DR3 astrometric errors and is suspiciously small; implies almost every spiral sits within 0.007″ of a DR1 target – unphysical. Likely unit typo (arcmin?)  
Fix Audit the cross-match code and report the correct median separation with units.

P5-M2  Sec. V A, p. 5  
Problem Bonferroni thresholds computed with erfc⁻¹ use K but some scans (density quintile, HEALPix) have strong bin-to-bin covariance; a Šidák or Holm step-down is required or an empirical permutation across all bins.  
Fix Provide an empirical family-wise error calibration for each scan (“max|σ| over all bins under 1000 shuffles”) and base all LEE claims on that.

P5-M3  Sec. VIII A, p. 10  
Problem KDTree search limited to k=20 nearest void spheres can miss the true containing sphere for galaxies in crowded regions; no completeness test.  
Fix Demonstrate (on a random 1 % subset) that increasing k to 100 leaves n_void unchanged to <0.2 %.

P5-M4  Eq.(2), p. 5  
Problem erfc⁻¹ argument uses α/K but text says α is already two-sided per-bin. Double-count of two-sided leads to  √2 error in |σ|_Bonf.  
Fix Re-derive Eq.(2) explicitly for two-sided tests and update all quoted thresholds.

P5-M5  Sec. VIII E, Table IX  
Problem HEALPix bins with <100 spirals are silently dropped; this introduces a data-dependent mask that correlates N with the statistic.  
Fix Quote the number of dropped pixels for each threshold and show by permutation that the selection does not bias the correlation coefficient r.

P5-M6  Sec. VII, Fig. 5  
Problem Heat-map range “max 0.22 pp” is read visually; table of exact ranges per cell is not supplied.  
Fix Add a table with the nine (R_s, λ_th) cells and exact max/min f_CW and σ values.

P5-M7  Appendix A  
Problem Operator L_parity mixes comoving-gauge δ and Eulerian L̂ without specifying gauge; statements about “order-of-magnitude bound” are therefore not reproducible.  
Fix Either provide a fully gauge-invariant definition or move Appendix A to a clearly speculative note outside the quantitative conclusions.

P5-M8  Typo duplicates  
Text contains “catalog-monopole- subtraction” and “catalog-monopole signature signature”.  
Fix duplicates.


MINOR  
P5-m1  Abstract  
The sentence “The test is bounce-model agnostic.” is marketing; remove or move to Introduction.  
P5-m2  Sec. VI B  
Logistic regression coefficient “0.0059” has no uncertainty and units are unclear (per unit z?). Report β±σ_β.  
P5-m3  Unlimited precision numbers such as p < 10⁻¹⁰⁰⁰ exceed double precision; give as p ≈ 0.  
P5-m4  Sec. III C  
State explicitly that DESI and chirality coordinates are both ICRS; otherwise a 0.5″ match may be inconsistent.  
P5-m5  Sec. VIII C  
Spell “membership” consistently; appears once as “memeberhsip”.

NIT  
P5-n1  p. 2 “survery-edge” → “survey-edge”.  
P5-n2  Fig. 3 y-label clipped in PDF.  
P5-n3  Caption Fig. 6: “maximal-voids” → “maximal voids”.  
P5-n4  Equation numbers skip from (1) to (3).  
P5-n5  Provide a citation for astropy SkyCoord.match_to_catalog_sky.


Overall length (20 pp) is acceptable for a methods paper once the redundant narrative in Secs. XI-XII (≈3 pp) is trimmed; recommended maximum 17 pp after fixing.


## Summary recommendation  
MAJOR REVISIONS

The manuscript presents a valuable, carefully crafted data set and an extensive set of null tests, but several methodological issues (un-propagated monopole uncertainty, un-quantified RSD, post-hoc choice of primary statistic, inconsistent multiple-testing treatment) must be corrected before the conclusions can be regarded as secure. Addressing the essential items E1–E7 and the major statistical points M1–M8 should bring the analysis to PRD methodological standards.