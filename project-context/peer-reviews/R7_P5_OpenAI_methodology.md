# P5 R7 — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 44.4s

---

Referee report – methodology/statistics audit  
Manuscript: “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test …”  

----------------------------------------------------------------
FINDINGS
----------------------------------------------------------------

ESSENTIAL (must be fixed before any further consideration)

ID P5-E1  
Sec. V B, p. 4  
Problem The primary estimator and analysis path were not pre–declared; the manuscript openly states that the “choice of which classifier to report as ‘primary’ is … made post-hoc”.  Garden-of-forking-paths inflates the false-positive/false-negative rate and voids standard frequentist guarantees.  
Fix Provide a preregistered analysis plan dated prior to looking at DR1, or re-cast the entire analysis as exploratory and remove all claims of “3 σ” or “Bonferroni-controlled” significance.  A registered analysis plan must specify (i) the environment classifier, (ii) all smoothing parameters, (iii) the estimator (exact expression for σ), (iv) the look-elsewhere correction procedure, and (v) stop-criteria on all sensitivity sweeps.

ID P5-E2  
Sec. VI A/Table II, p. 5  
Problem The quoted counting-statistics floor for the void class is “∼ 5 pp”; the correct binomial 1 σ width at N = 428 is √(0.25/428)=0.0241 i.e. 2.4 pp.  All subsequent “≈ 2 σ” statements for the void class are therefore off by a factor ≃ 2.  
Fix Recompute every σ, CI and “pp” figure that inherits this error and update all text, tables, and conclusions.

ID P5-E3  
Sec. VI D/Table IV, p. 6  
Problem χ² test “χ² = 4932, 3 d.o.f., p < 10⁻¹⁰⁰⁰” is numerically impossible (double precision underflows at ≈10⁻³⁰⁸).  The p-value is wrong.  
Fix Report the exact p from a stable log-χ² routine (or quote –log₁₀ p).  All extremely small p’s must be rounded to ≥10⁻³⁰⁰ or given as ⪅10⁻³⁰⁰ with justification.

ID P5-E4  
Sec. V, Eq. (2), p. 3  
Problem The “Bonferroni σ threshold” formula uses erfc⁻¹(α/K) but the text implements erfc⁻¹(α/K)×√2 and then labels the result “σ”.  This double-counts √2.  Thresholds (e.g. 3.09 for K = 5) are therefore wrong.  
Fix Correct the analytic expression and recompute every Bonferroni line in all figures, tables, and text.

ID P5-E5  
Throughout (abstract, §§VI–VIII)  
Problem σ values derived from two incommensurable nulls are mixed without caveat:  
(a) σfrom half – a frequentist z-score;  
(b) σpred – a catalogue-monopole expectation.  
They are placed on the same axis (e.g. Fig. 3 right) as if directly comparable.  
Fix Either convert σpred into a probability under the same binomial null or stop plotting it as a “σ”.  Clarify its status (systematic expectation, not an observed z-score).

ID P5-E6  
Abstract line 14  
Problem “−2.61 σ” for the filament class cannot be reproduced from the stated numbers (p = 0.4980, N = 408 187 gives −2.556 σ).  
Fix Audit every σ in the abstract and conclusions and supply a reproducible derivation chain.

ID P5-E7  
Sec. IX A/Table XI, p. 14  
Problem Only 1 000 permutations are used for the empirical max-statistic, yet p-values are quoted to three decimals (e.g. p = 0.135).  Resolution is at best 1/1001 ≈ 0.001.  
Fix Either increase permutations to ≥100 000 or round all permutation-based p’s to two significant digits (e.g. 0.14).

ID P5-E8  
Sec. IV, p. 3  
Problem The cosmic-web classification is performed in observed redshift space; no reconstruction is applied and the anisotropic RSD contribution to the tidal tensor is ignored, yet the paper treats class labels as if RSD-safe.  
Fix Provide a quantitative RSD error budget (propagation of σv through λ-eigenvalue boundary crossings) or rerun the classifier on a reconstructed density field.

ID P5-E9  
Global  
Problem All headline results rely on the un-reviewed Paper IV catalogue.  The uncertainty of the Paper IV monopole is never propagated into any σ or into the “0.0026” bias subtraction.  
Fix Propagate the quoted ±0.000279 uncertainty of the monopole through every σpred and through every monopole-subtracted statistic; revise significance claims accordingly.

----------------------------------------------------------------
MAJOR (significant but not necessarily blocking)

ID P5-M1  
Sec. VI C, Fig. 3  
Problem The density proxy is angular k=5 NN, yet the signal is compared to a 3-D monopole model.  Anisotropic selection effects on the sphere are not controlled.  
Fix Replace with a comoving-density metric (e.g. spectroscopic 5 h⁻¹ Mpc NN) or formally justify why the 2-D proxy is sufficient.

ID P5-M2  
Sec. VII, p. 8  
Problem Phase-2 sweep considers only Rs ={10,25,50} Mpc h⁻¹ and λth ={0,0.1,0.3}.  No justification for the chosen grid or for stopping at Rs = 50 Mpc h⁻¹.  
Fix Supply a convergence study or an a-priori theoretical argument that larger/smaller Rs do not change the conclusion.

ID P5-M3  
Sec. VIII E/Table IX  
Problem HEALPix pixels with <200 spirals are dropped, but this removes 50–60 % of the sky.  Possible masking bias is not quantified.  
Fix Provide a weighting-scheme or jack-knife demonstrating that exclusion of low-count pixels does not bias the void correlation test.

ID P5-M4  
Sec. XI, p. 15  
Problem Systematics section states “no test produces a >3σ residual” but the earlier text reports several |σ|≈4–5 deviations before monopole subtraction.  Statement is self-contradictory.  
Fix Clarify exactly which σ are included/excluded in the systematics audit.

ID P5-M5  
Global  
Problem p-values are scattered throughout the text but no multiple-comparison correction is applied across the dozens of redshift, density, target-class and HEALPix stratifications.  
Fix Supply a table listing every formal test, its p, and the FDR/BH-q or Šidák family correction.

ID P5-M6  
Sec. VI D  
Problem Cluster/filament bright-vs-dark “sign-flip” is claimed to be astrophysically interesting but no formal interaction test (CW ~ class×program) is performed.  
Fix Provide a χ² or logistic-interaction fit and quote the exact p-value for the interaction term.

----------------------------------------------------------------
MINOR (would improve clarity/accuracy)

ID P5-m1  
Abstract, line 6: “16.4 × 10⁶” should be written “1.64 × 10⁷”.  
ID P5-m2  
Sec. III C, p. 2: “acceptance radius is 1.0′′” – cite the fibre positioning spec or DR1 documentation.  
ID P5-m3  
Sec. V footnote: Equation for σfrom half is unreadable (missing denominator parentheses).  
ID P5-m4  
Appendix A: the toy operator breaks rotational invariance – add a clarifying sentence that this is schematic only.  
ID P5-m5  
Figures 2 & 7 share colours but not labels; add legend.  

----------------------------------------------------------------
NIT (cosmetic)

ID P5-n1  
p. 1 “∼ 16.4 × 106” – use “≈1.64×10⁷”.  
ID P5-n2  
Repeated phrase “sample-size limited” (appears 11 times); remove redundancy.  
ID P5-n3  
Internal pipeline notes (“JSON artifact above”, “seed fixed in the pipeline config”) should be moved to a data-release README, not the manuscript.  

----------------------------------------------------------------
5-PAGE STREAMLINE

The main text is 20 pages.  After removal of repeated robustness paragraphs and internal-pipeline prose the logical content fits in ≈12 pages.  I recommend a 12–14 page target.

----------------------------------------------------------------
## Summary recommendation  
MAJOR REVISIONS

The work is potentially publishable but the statistical backbone needs substantial repair: the analysis was not preregistered, key error bars are wrong, Bonferroni thresholds are mis-computed, the RSD impact on the tidal tensor is ignored, and several impossibly small p-values are quoted.  Until these essentials are fixed the headline “no environment dependence” cannot be regarded as demonstrated at the claimed sensitivity.