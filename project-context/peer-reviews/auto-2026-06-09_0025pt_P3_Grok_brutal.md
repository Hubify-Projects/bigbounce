# P3 auto-2026-06-09_0025pt — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 1758.0s

---

**Referee Report**

**P3-E1 (ESSENTIAL)**  
Section I (p. 1) & abstract: “We present the largest-scale application of autoencoder anomaly detection across seven astronomical archives… 378,280 Path-C Unique Anomalies”.  
The claim is not supported. The headline number is obtained only after (a) a heavily biased cross-transfer run on LAMOST that inflates the count by ~98 % blue-excess artifacts and (b) a post-hoc native-retrain + 7-way deduplication whose net compression is only 2.6 %. No prior single-survey catalog is shown to be smaller by the stated factor of 141 once identical selection and deduplication are applied. Required fix: remove or qualify the “largest-scale” and “141×” statements; supply a table comparing effective unique-object yields under uniform criteria.

**P3-E2 (ESSENTIAL)**  
Abstract & §IV A (p. 9): “genuine novelty fraction of ~17.8 % (single-sample point estimate at the top-1,000 score stratum; full-catalog rate empirically untested)”.  
A single-sample point estimate on 1 000 objects is presented as the discovery-rate headline while the text simultaneously states the full-catalog rate is untested. This is internally contradictory and violates PRD standards for quantitative claims. Required fix: either (i) compute and report the full-catalog archival cross-match rate with the same 20-catalog CDS X-Match pipeline or (ii) remove the 17.8 % figure from the abstract and all summary tables.

**P3-E3 (ESSENTIAL)**  
§III D (p. 6) & Table I: 98 % of the LAMOST cross-transfer anomalies are blue-excess training artifacts; the native-retrain still yields only 5.8 % injection-recovery at 5σ.  
The catalog nevertheless lists 44 075 LAMOST objects in the “Path-C unique” headline. No quantitative demonstration is given that the residual 5.8 % recovery rate is sufficient to claim astrophysical anomalies rather than residual training-set mismatch. Required fix: move all LAMOST objects to an explicitly labeled “exploratory / artifact-contaminated” tier and recompute every global statistic excluding them.

**P3-E4 (ESSENTIAL)**  
§IV D (p. 10) & abstract: Planck × ACT cross-correlation is reported as “null” and used to argue that CMB-map anomalies are “dominated by survey-specific systematics”.  
The two maps were scored with entirely different autoencoder architectures (fully-connected vs. convolutional) and different native-retrain protocols; the null result is therefore expected a priori and cannot be interpreted as evidence against a cosmological origin. The paper never states the architectures are incomparable. Required fix: either withdraw the cosmological interpretation or supply a controlled same-architecture cross-correlation test.

**P3-M1 (MAJOR)**  
Abstract & §V A: empirical Landy–Szalay bias measurement yields \(\alpha_{jk}=0.19\pm0.65\) (<1σ from null) and is inserted into the Fisher forecast to claim a 7.9 % improvement on \(\sigma(f_{NL})\).  
The measured \(\alpha\) is statistically consistent with zero; the improvement is therefore a central-value forecast pending higher-S/N data, not a demonstrated result. The abstract presents it as a achieved improvement. Required fix: rephrase all abstract and summary claims to “projected improvement under the measured bias-enhancement factor”.

**P3-M2 (MAJOR)**  
Fig. 2 (right) & §III C: SDSS DR18 scores span twelve orders of magnitude because the DESI-trained model is applied outside its training distribution.  
The paper correctly identifies this as domain shift, yet still includes the 77 905 SDSS objects in the primary catalog without a domain-shift correction or separate scoring. The resulting anomaly ranking is not comparable to the native DESI ranking. Required fix: publish SDSS anomalies under an explicitly separate “transfer-learning” flag and do not combine them with native-retrain counts for any global statistic.

**P3-M3 (MAJOR)**  
Table I footnote & §II D: ACT DR6 is “formally quarantined” (both gate criteria fail) yet the 200-patch cross-transfer block is retained in the baseline map (Fig. 1).  
The figure caption and all spatial-distribution claims therefore include a known-failure data set. Required fix: remove the ACT points from every figure and table that presents “Path-C unique” results, or label them as a methodological diagnostic only.

**P3-N1 (MINOR)**  
Multiple instances of “Path-C” and “native-retrain” terminology are introduced without a single consolidated definition paragraph. Readers must reconstruct the protocol from §II D and footnotes. Required fix: add a one-paragraph “Path-C protocol summary” box in §II.

**P3-N2 (NIT)**  
Fig. 1 caption states “319,443 detections shown” while the abstract headline is 378,280. The difference is explained only in footnotes; a parenthetical in the caption would eliminate confusion.

**Summary recommendation**  
REJECT

The manuscript presents a large catalog whose headline numbers are dominated by known training artifacts (LAMOST), domain-shift inflation (SDSS), and a formally quarantined data set (ACT). The single quantitative novelty claim (17.8 %) is explicitly labeled “empirically untested” for the full catalog, and the cosmological interpretation of the Planck–ACT null test rests on an apples-to-oranges architecture comparison that the text never flags. These are not cosmetic issues; they are foundational to the paper’s central claims of scale, novelty, and cosmological utility. Until the artifact-dominated subsets are removed or unambiguously tiered, the 17.8 % novelty fraction is measured on the full sample, and the cross-architecture CMB comparison is either withdrawn or properly controlled, the paper does not meet Physical Review D standards for a methods or catalog contribution.