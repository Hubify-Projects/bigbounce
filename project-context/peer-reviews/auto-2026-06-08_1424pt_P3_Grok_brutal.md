# P3 auto-2026-06-08_1424pt — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 67.4s

---

**Referee Report**

**Paper:** P3 (Houston Golden, “Spectrally Unusual Sources at Scale…”, Phys. Rev. D submission)

**Findings**

**P3-E1 (ESSENTIAL)**  
Section V.A, p. 10; abstract.  
The headline Fisher forecast \(\sigma(f_{\rm NL})=8.14\) (7.9 % improvement over single-tracer baseline 8.98) is obtained with \(\alpha_{jk}=0.19\pm0.65\) (<1\(\sigma\) from null). The paper states the result is “consistent with no improvement at <1\(\sigma\)”. Placing a sub-\(\sigma\) constraint in the abstract and calling it a “cosmological application” violates PRD standards for significance claims.  
**Fix:** Remove all quantitative \(f_{\rm NL}\) forecasts from abstract and Section V; retain only as an illustrative upper-limit exercise with explicit “null result” language.

**P3-E2 (ESSENTIAL)**  
Section III.D, p. 3; Table I footnote ‡.  
98 % of the LAMOST DR10 “anomalies” are blue-excess training artifacts; the native retrain still yields only 5.8 % injection-recovery at 5\(\sigma\). The catalog tier is nevertheless released as an “exploratory” sample. This directly contradicts the claim that the catalog contains “genuine novelty”.  
**Fix:** Relegate the entire LAMOST tier to an appendix labeled “training-bias diagnostic; not science-grade”; do not count the 44 075 objects toward the headline 378 280.

**P3-E3 (ESSENTIAL)**  
Section II.D & III.F, pp. 2–3; Table I.  
ACT DR6 is formally quarantined (cross-transfer val_loss \(\approx2\times10^4\)) and contributes zero objects, yet the abstract and Table I still list seven surveys and quote a total processed volume that includes the quarantined block. This is a material misrepresentation of the actual data set used.  
**Fix:** Remove ACT DR6 from all summary statistics and from the abstract sentence “across seven astronomical archives”.

**P3-M1 (MAJOR)**  
Abstract; Section I, p. 1.  
“largest-scale application … 37.3 million sources” is asserted without a quantitative comparison to the prior single-survey catalogs cited ([11], [12]). The only scaling argument given is a factor ~141 relative to Liang et al.; no table or text compares total compute, sky coverage, or anomaly yield against contemporaneous multi-survey efforts.  
**Fix:** Provide an explicit comparison table (or retract the “largest” claim).

**P3-M2 (MAJOR)**  
Section IV.A, p. 9; Fig. 5.  
The 17.8 % “genuine novelty fraction” is derived from a single-sample CDS X-Match of the top-1 000 DESI objects. No bootstrap, no alternative matching radius, and no NED+VIzIER cross-check on the same objects are shown. The number is therefore not robust.  
**Fix:** Replace with a multi-catalog, multi-radius assessment or downgrade to “illustrative”.

**P3-M3 (MAJOR)**  
Section V.B, p. 10; Eq. (2) and surrounding text.  
The canonical anomaly score \(S\) is survey-specific (different \(\mu_{\rm val},\sigma_{\rm val}\) per archive) yet is treated as commensurate when objects are merged into the 378 280 catalog. No cross-survey score calibration is demonstrated.  
**Fix:** Either publish per-survey ranked lists only or supply an explicit homogenization step with validation.

**P3-N1 (MINOR)**  
Fig. 2 caption, p. 5.  
The right-hand panel y-axis label “Prob. density” is plotted on a log scale that spans 14 orders of magnitude; the lowest bin is empty yet the curve is drawn through it. Cosmetic but visually misleading.  
**Fix:** Truncate axis or mark empty bins.

**P3-N2 (NIT)**  
Page 1 header: “Dated: June 2026”. Future date in a submitted manuscript is an anachronism; remove.

**Summary recommendation**  
**MAJOR REVISIONS**

The manuscript presents a technically ambitious multi-survey anomaly search whose core methodological contribution is undermined by three non-negotiable problems: (1) an unsubstantiated cosmological claim resting on a <1\(\sigma\) result, (2) inclusion of a known 98 % artifact population (LAMOST) in the headline catalog, and (3) an inaccurate survey count that incorporates a quarantined data set. Until these are corrected the paper does not meet PRD standards for quantitative claims and data-product integrity. The remaining issues (overstated novelty, lack of score homogenization, single-sample novelty fraction) are also serious but secondary to the above.