# P5 2026-06-04_R3clean — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 43.8s

---

Referee report on  
“Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56 ,981 Void Spirals with V-Web Cross-Check Across 791 ,635 DR1 Matched Spirals” (P5, 2026-06-04_R3clean)

----------------------------------------------------------------
FINDINGS
----------------------------------------------------------------

P5-E1  (ESSENTIAL)  
Section V B, p. 5 “Primary vs. secondary analysis paths”  
Problem The paper explicitly states that the DESIVAST analysis was chosen as the “primary” path only after all possible classifiers had been inspected: “The choice of which classifier to report as ‘primary’ is therefore made post-hoc… .”  The principal estimator is therefore not pre–declared, violating PRD’s reproducibility standard and the requirement in the CfA instructions for a pre-specified primary statistic.  
Fix Either (i) file and cite a time-stamped preregistration that predates any look at the DR1 data, or (ii) drop the claim of a single primary analysis and treat all classifiers on an equal, exploratory footing with a global multiplicity correction across them.  In the latter case re-state the headline as an exploratory null only.

P5-E2  (ESSENTIAL)  
Throughout; first invoked Abstract, second paragraph  
Problem All chirality figures rely on Paper IV, which is “not yet peer-reviewed”.  The present manuscript treats the Paper IV catalog and its quoted monopole (∆fCW = −0.0026) as truth with zero error: the monopole is subtracted, used to predict σpred, and drives the environmental conclusions, yet its own systematic and statistical uncertainties are nowhere propagated.  
Fix Publish, or at least supply to the editors, a refereed version of Paper IV with an uncertainty budget on ∆fCW, then propagate that uncertainty through every place σpred or fCW–f̄CW is used.  Until this is done none of the derived significances are defensible.

P5-E3  (ESSENTIAL)  
Eq. (1), p. 5 and all residual tests that depend on it  
Problem σpred is treated as deterministic, even though ∆fCW has measurement uncertainty (cf. E2) and σpred ∝ √N so inherits counting-error too.  Consequently comparisons like |σobs − σpred| < 1 are overstated.  
Fix Carry the full propagated error on σpred into every residual test; give a credible interval, not a single value, and re-evaluate which classes still pass |σobs − σpred| < 3 after that.

P5-E4  (ESSENTIAL)  
Section XI (“Systematics”) & elsewhere  
Problem Several σ values coming from distinct null procedures (exact-binomial, permutation, two-sample z-test, HEALPix max-stat) are quoted on the same “σ” scale and compared directly (e.g. “the strongest residual at 3.4σ is comparable to the 4.7σ cluster signal”).  These statistics have different reference distributions and are not commensurable.  
Fix Either express all test statistics in p-value space or keep the σ notation but convert every non-Gaussian null to an equivalent normal-variance via Φ-1(p/2).  Make it explicit each time which underlying null is being used.

P5-E5  (ESSENTIAL)  
Section IV, RSD treatment, pp. 10–11  
Problem The tidal field is constructed in observed redshift space but the environment classes are interpreted physically.  The manuscript admits that no quantitative redshift-space distortion (RSD) correction or error propagation is attempted: “we explicitly do not quantify the propagated uncertainty … we defer to a companion follow-up.”  Without that quantification the claim of environment-independence is uncontrolled.  
Fix Provide either (i) a Zel’dovich/BAO reconstructed re-run showing the same fCW results, or (ii) a quantitative bound on the class-flip rate from RSD with the bound propagated into ∆fCW uncertainties.  Qualitative hand-waving is not sufficient.

P5-M1  (MAJOR)  
Eq. for σfrom half, p. 4  
Problem Typeset as σfrom half ≡ (nCW − 0.5 N)/(0.5 N) → denominator missing √N.  
Fix Correct formula everywhere and audit that code actually used the correct normalisation (the numerical examples are consistent, but the printed equation is wrong).

P5-M2  (MAJOR)  
Section VI D, density-quartile follow-up  
Problem The text states “cluster Q3 σ = −0.37 is statistically null after Bonferroni-4 correction” but Table IV shows σ = −0.37 with n = 99 ,526; the one-sided p ≈ 0.71 even before correction.  Bonferroni discussion is irrelevant, signalling confusion in the significance bookkeeping.  
Fix Remove Bonferroni language for obviously non-significant bins and re-check all tables for similar mis-statements.

P5-M3  (MAJOR)  
Internal development artefacts  
Problem Dozens of absolute file paths, git SHA blobs, and pipeline filenames (e.g. “pipelines/p5_desi_chirality/env_finder/...”) remain in the body text.  These violate the journal’s blindness policy and are useless to readers without repository access.  
Fix Replace with DOIs or public Zenodo links; move implementation details to a supplementary README.

P5-M4  (MAJOR)  
Multiplicity control  
Problem Only within-classifier Bonferroni factors are applied.  The paper tests >40 distinct environment stratifications (V-Web nine-cell sweep, DESIVAST three algorithms, Tempel, ASTRA, density, redshift, tracer splits, sky maps).  A global look-elsewhere correction across all of them is not attempted, yet the abstract still quotes individual σ values.  
Fix Provide a complete hypothesis tree with a pre-defined family-wise error budget or Markov-chain a posteriori adjustment.

P5-M5  (MAJOR)  
Dependence on companion papers for notation and context (Papers II & III) without supplying those manuscripts to the referees.  
Fix Either append those sections as auxiliary material or remove all dependence.

P5-m6  (MINOR)  
Abstract “Phase 2 … never exceeds 0.22 percentage points (max 0.0022)” duplicates the same number in two units; keep one.  

P5-m7  (MINOR)  
Duplicate phrase “canonical canonical-mask” on p. ? line ?.  Remove repetition.

P5-m8  (MINOR)  
The 95 % Jeffreys CI for the void bin (n = 428) is quoted as [0.435, 0.530] once and [0.441, 0.528] elsewhere.  Pick one.

P5-n1  (NIT)  
Footnote marker “∗ houston@hubify.com” sits in the title block: PRD style wants it after the author name only.

P5-n2  (NIT)  
In Table VI “max across sweep” row lacks units.

P5-n3  (NIT)  
ArXiv identifier “2604.02463” is impossible (future); label as “expected”.

P5-n4  (NIT)  
Spurious leading zeros in some p-values (“p < 10−1000”); scientific notation already conveys the extremity.

----------------------------------------------------------------
Summary recommendation
MAJOR REVISIONS

The manuscript is methodologically interesting and could become a useful reference, but the statistical chain of custody is not yet acceptable for PRD.  The post-hoc choice of the “primary” estimator, the unpropagated dependence on the un-reviewed Paper IV monopole, the missing RSD error budget, and the mixing of incommensurable σ scales must all be fixed before the headline null can be considered reliable.  A focused revision addressing every ESSENTIAL and MAJOR item above is required.