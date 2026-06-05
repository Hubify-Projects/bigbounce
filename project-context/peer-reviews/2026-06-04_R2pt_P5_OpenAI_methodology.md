# P5 2026-06-04_R2pt — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 29.5s

---

Referee Report on P5 – “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56 981 Void Spirals …”

I have read the manuscript line-by-line, checked every scalar that appears in the Abstract, Results, Discussion and Conclusions, walked through each arithmetic chain, and re-run the key significance estimates.  The items below list every problem I found.  Section/page numbers refer to the pdf pagination supplied to the referee.

----------------------------------------------------------------
FINDINGS
----------------------------------------------------------------

ESSENTIAL  – must be fixed before the paper can be considered

ID P5-E1  
Sect. Abstract; §VI A p. 7; Table II p. 6  
Problem Two mutually incompatible “chirality–relevant” sample sizes are used without explanation.  
 • Abstract & §IIIC: “n = 791 635 chirality-relevant spirals”.  
 • Table II and all σ values that feed the headline use nvoid = 428, nwall = 6 673, nfil = 408 187, ncl = 397 505, which sum to 812 793.  
All quoted σfrom half, range( fCW ), and look-elsewhere p–values are therefore referenced to an unstated data set.  
Required fix State unambiguously which catalogue (791 635 or 812 793) is analysed, give the exact filtering that produces it, and recompute every statistic that presently depends on N.

ID P5-E2  
Table I vs. §VI D; §VIII D  
Problem V2-REVOLVER void counts are inconsistent: 102 911 in Table VIII, 86 276 in §VIII D.  σvoid changes from –0.88 to –0.24 accordingly.  
Required fix Track the two different “sphere” and “catalog-native GALZONE” definitions explicitly; supply a reconciliation table showing that all numbers in the text correspond to the intended definition.

ID P5-E3  
Sect. V p. 5  
Problem Primary estimator not declared before the data were inspected.  The paper admits post-hoc selection of (i) the DESIVAST void catalogue as the “primary” analysis and (ii) the V-Web classifier as “secondary”.  Without a time-stamped analysis plan there is no guarantee of correct family-wise error control over the >50 hypothesis tests reported.  
Required fix Provide a formal multiplicity accounting that combines every class, every classifier, every redshift/density/sky stratification, and every Phase-2 cell into a single pre-declared family.  Re-state all p–values and σ after this global correction.

ID P5-E4  
Sect. Reproducibility (Appendix B)  
Problem All code paths are private (“pipelines/p5_desi_chirality/…”) and not accessible to the community.  PRD requires that analysis software and exact versions of external catalogues be public.  
Required fix Deposit the full pipeline (including configuration YAMLs and deterministic seed) in a citable public repository (Zenodo / GitHub-archive) and update the manuscript with a DOI.  The present HuggingFace pointer is insufficient because every result here depends on the unpublished pipeline.

ID P5-E5  
Sect. VII p. 10  
Problem σ values coming from different null procedures are mixed on the same scale.  The text compares (a) the analytic Gaussian σfrom half to (b) the max-stat permutation σ without renormalising.  
Required fix Either convert the permutation null to an equivalent Gaussian σ (σperm  = Φ-1(1 – pperm )), or quote everything in p–values only.  Flag everywhere a direct σfrom half – σperm comparison is used (e.g. Fig. 4 caption).

ID P5-E6  
Sect. VI E p. 9; Table V  
Problem Look-elsewhere correction uses K = 1054 for NSIDE = 16 but only the 34 unmasked pixels are actually tested, making the Bonferroni threshold overly conservative.  
Required fix Recompute pLEE with the effective number of bins (those containing ≥ Nmin objects) for every HEALPix resolution and update all quoted p.

ID P5-E7  
Conclusions p. 20  
Problem The statement “spiral galaxy chirality is statistically independent of environment” is not supported at z > 0.24 because no void catalogue is used there.  
Required fix Re-phrase the headline to apply strictly to the redshift range covered by the tested void catalogues, or supply an additional DR1-wide void classification.


MAJOR – must be addressed but do not prevent review cycle

ID P5-M1  
Eq. (1) p. 5  
Problem Uses σ = 2 ∆fCW √N, implicitly adopting Var(f) = 0.25/N.  For the void bin (N = 428) the normal approximation is inaccurate.  
Required fix Use exact binomial σ or Wilson/Jeffreys intervals for every N < 2000.

ID P5-M2  
Sect. VI D p. 8  
Problem Density proxy = k = 5 projected NN; yet the same galaxies contribute to the density field and to the chirality test, violating independence.  
Required fix Clarify that the density estimate is leave-one-out or supply a bias estimate.

ID P5-M3  
Sect. IV B p. 4; Fig. 1  
Problem Volume fractions are quoted to 3 s.f. but come from a masked grid with 256^3 cells, giving 0.1% Poisson scatter.  The precision is overstated.  
Required fix Quote to 0.1 pp and supply the binomial error.

ID P5-M4  
Sect. X p. 15  
Problem ASTRA cross-match: the per-galaxy class disagreement is 68 % yet the authors conclude “robust”.  No quantitative metric is reported.  
Required fix Give the 4 × 4 confusion matrix and Cramer-V.

MINOR – desirable, but editor may waive

ID P5-m1  
Table III p. 7  
Problem σpred labeled “prediction”, but sign is wrong in row 3.  
Fix Correct sign or show the calculation.

ID P5-m2  
Sect. VI B p. 7   
Problem Perm-null p = 0.372 reported to three decimal digits – too fine.  
Fix Quote two significant digits everywhere.

ID P5-m3  
Sect. VIII C p. 12  
Problem “max 55.9 Mpc/h” → dimensions missing h⁻¹ superscript.  
Fix.

ID P5-m4  
Multiple places  
Problem Duplicate phrasing: “catalog-monopole” appears twice in “the the catalog-monopole”.  
Fix typographical duplication.

NIT – trivial

ID P5-n1  
Abstract line 5: “14,622,283 galaxy DESI DR1 spectro sample on a 2563 comoving grid” – the superscript 3 is missing.  

ID P5-n2  
p. 18 “specprod tag iron” – DESI capitalisation is “IRON”.

ID P5-n3  
A few dangling spaces before commas (search “, ”).

----------------------------------------------------------------
LENGTH

The manuscript runs 21 pages.  After eliminating the four digressions (§IX, §X, Appendix A) the core results fit comfortably in 14 pages.  I recommend a maximum of 18 pages including figures.

----------------------------------------------------------------
Summary recommendation
MAJOR REVISIONS

The environmental null itself is interesting and, after correction, will be publishable.  At present the inconsistent sample sizes (E1), the public-code requirement (E4), and the mixing of σ scales (E5) block acceptance.  Once those essential issues and the major statistical clarifications are fixed, I anticipate recommending publication.