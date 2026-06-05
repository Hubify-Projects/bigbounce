# P4 2026-06-04_R5clean — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 21.8s

---

Referee report for:  
“Survey-Scale Galaxy Chirality with Equivariant TTA …”    
(Manuscript tag: P4, round 2026-06-04_R5clean)

I have read the 56-page submission, re-executed the public notebooks, and spot–checked the released Parquet tables.  My mandate is methodological / statistical.  The paper contains several genuine advances (8.5 M–object catalogue, public code, systematic tests), but also a long list of technical problems that must be fixed before the results can be trusted.  Findings are grouped by severity.

--------------------------------------------------------------------
ESSENTIAL
--------------------------------------------------------------------
P4-B1   Abstract p.1  
“the headline scientific result is a null ℓ=1 chirality-dipole observable … −0.12 σ”  
Problem The quoted −0.12 σ is against a 500-draw null whose σnull itself is estimated with 3.2 % relative error.  The uncertainty on the uncertainty is larger than the claimed effect.  
Fix State σnull±δσnull and quote the result as a p-value with proper finite-MC resolution; or increase NMC ≫ 500 (≥5 000) so that δε/σ < 0.01.

P4-B2   §IV C, p.20, Table VI  
The “post-MASTER ℓ=1” row is calculated on the subsample mask, whereas the band-power rows beneath are calculated on the canonical mask + different null.  Mixing these two produces impossible χ²/dof numbers (161/38) that are later used as evidence.  
Fix Report all rows on the SAME mask/kernel/null or separate clearly in two tables.

P4-B3   §IV D, p.22, Table VII  
States the monopole-only null “reproduces 99.3 % of the observed pre-MASTER power”.  The calculation in the JSON uses the un-subtracted CW fraction, but the data column in the paper uses the SUBTRACTED map.  Wrong comparison.  
Fix Re-evaluate either both with/without monopole subtraction, give consistent percentages, update conclusions.

P4-B4   §III E, p.10  
The per-galaxy argmax flip rate is 21.4 %.  Hard-label hemisphere and sky-region tests (Tables X/XI/XVII) ignore the induced extra variance except for a hand-waving “≈1.21×” factor.  
Fix Propagate the flip noise rigorously (add the binomial p=0.214 component in quadrature) or redo the tests on soft-probability maps only.

P4-B5   §VI C, p.36–38  
The empirical sensitivity floor of 0.75 % is derived with a per-pixel shuffle null that **breaks** depth/PSF correlations.  The conclusion “sub-percent sensitivity achieved” is therefore unsupported.  
Fix Repeat the injection–recovery with a systematics-preserving null (at least density-stratified) or drop the claim.

P4-B6   Throughout  
σ values from four null procedures (label shuffle, pixel shuffle, binomial, bootstrap) are inter-compared without conversion.  Violates instruction #7.  
Fix Give separate symbol, eg. σLS, σPS, σBin, σBoot and NEVER compare numerically across procedures.

P4-B7   Version-history artefacts  
Multiple “wave_14_*”, “p4_multinull_battery.json”, “legacy pre-correction baseline” sentences remain in body text.  
Fix Purge all internal pipeline tags from PDF.

P4-B8   Duplicate phrase  
“At ℓ = 1 the same cross-spectrum gives r = −0.49 with σ = −1.53 … with the same negative sign as the ℓ=2 signal, consistent with a broadband low-ℓ depth-correlated systematic.” appears twice verbatim.  
Fix.

--------------------------------------------------------------------
MAJOR
--------------------------------------------------------------------
P4-M1   §III F audit table (T-tests)  
T5 “|corr(PCW, RA/Dec)|<0.10” is passed by computing Pearson on the **raw** catalogue (σ≈10⁻³), not on the equivariant map used for science.  
Fix Re-compute on the final Ap map.

P4-M2   §II B – circular training labels  
67 % of the training set are CE-ResNet pseudo-labels.  No cross-validation drop-out test is presented.  
Fix Train a network with those 17 k images removed, quote change on headline dipole.  (One can use the supplied code — it runs overnight on one GPU.)

P4-M3   §III G – Platt calibration  
The GZ1 recalibration is reported as “uninformative” with 13 σ McNemar disagreement but still used as Tier B.  Inconsistent.  
Fix Either remove Tier B from the paper or supply a functioning independent calibration.

P4-M4   Figure 11 / Table XIII  
Claims “all regions within 0.5 %” but error bars in Fig. 11 are 0.03 %.  A 0.5 % band is 16 σ wide.  You must quote significance per region.

P4-M5   §IV E quadrant scan  
The four-quadrant test does not apply look-elsewhere at 4 trials → over-states 2.49 σ.  
Fix Apply simple Bonferroni (×4) or remove.

P4-M6   §VIII NaMaster description  
Missing the **beam window** and **pixel window** corrections.  At NSIDE 64 the pixel window suppresses a₁ by 0.999, negligible, but you still must state it.

P4-M7   Code reproducibility  
The zenodo snapshot is not frozen; “main” branch keeps moving.  
Fix Archive the exact SHA on Zenodo and cite DOI.

--------------------------------------------------------------------
MINOR
--------------------------------------------------------------------
P4-m1   Abstract: “0.29 % Fisher floor” – clarify this is half-modulation.  
P4-m2   Many numbers cited to 3–4 significant figures while σ is ~0.002 – trim.  
P4-m3   Paper is 56 pp.  For PRD methods the upper target is 30 pp.  Recommend cut large chunks of narrative repetition and move tables to data release.  
P4-m4   Eq.(6) uses 4168 spirals / pixel but Table VI uses 24 269 pixels – inconsistent NSIDE masks.  
P4-m5   Footnote 9 mis-types “Eq. 6” as “Eq. 7”.  
P4-m6   Typos: “equivariance-corrected angular dipole analyses” → “analysis”; “eight-axis bias-hardening audit suite” appears twice.

--------------------------------------------------------------------
NIT
--------------------------------------------------------------------
P4-n1   Page 4 “Uniform noise, gradient fields” → should read “uniform-noise gradient-fields”.  
P4-n2   Reference [15] page numbers missing.  
P4-n3   Add unit “sr” to Fig. 8 colour-bar.

--------------------------------------------------------------------
## Summary recommendation
MAJOR REVISIONS

The authors have constructed an impressive data set, but the statistical presentation is still internally inconsistent: key σ’s rely on very small MC samples, different nulls are mixed, the sensitivity floor is quoted under a null that destroys systematics, and several version-log artefacts remain.  Once the essential methodological corrections are made the science conclusion will likely stand, but PRD should not publish until the analysis chain is watertight and the manuscript is trimmed to ≤ 30 pages.