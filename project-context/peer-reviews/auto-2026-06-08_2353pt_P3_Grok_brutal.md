# P3 auto-2026-06-08_2353pt — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 117.5s

---

**Referee Report**

**Paper:** Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies… (Houston Golden)

**Journal target:** Phys. Rev. D

**Date of review:** auto-2026-06-08

I have examined every page, equation, table, figure, caption, and reference in the rendered PDF. Below are all identified deficiencies, classified strictly.

### ESSENTIAL (paper cannot be accepted without correction)

**P3-E1** Abstract (p. 1) & §V (p. 11)  
Quote: “A NANOGRAV 15-yr KDE free-spectrum MCMC yields γ = 2.567 ± 0.382; the matter-bounce prediction γ = 3.0 sits at +1.13σ…”  
The quoted posterior is obtained from the public NANOGRAV 15-yr KDE product, not from the anomaly catalog. The catalog is used only for a separate, much weaker multi-tracer f_NL exercise. The abstract therefore presents an unrelated PTA result as though it were derived from the anomaly sample.  
**Required fix:** Remove the NANOGRAV γ result from the abstract and from any claim that the anomaly catalog constrains bounce parameters. The f_NL section may remain only if reframed as a proof-of-concept with explicit statement that the present sample yields no detection.

**P3-E2** Abstract (p. 1) & §V.A (p. 11)  
Quote: “An empirical Landy–Szalay bias measurement on the 5,384 QSO-candidate sample yields α_jk = 0.19 ± 0.65 (< 1σ from null); inserting this into the Fisher-positivity-respecting form … gives a central forecast σ(f_NL) = 8.14 with 1σ envelope [3.92, 8.98] (7.9 % improvement …).”  
The quoted 7.9 % improvement is obtained by linear scaling of the 7-tracer Fisher matrix evaluated at α = 0.15. The measured α_jk is statistically consistent with zero; the improvement is therefore an upper-bound forecast, not a realized gain. No covariance between the anomaly-selected sample and the baseline tracers is propagated.  
**Required fix:** Either (a) drop the multi-tracer forecast or (b) present it strictly as a forecast under an assumed α, with the measured α shown only as a consistency check.

**P3-E3** §IV.A (p. 9) & Fig. 5  
The “genuine novelty fraction ~17.8 %” is a single-point estimate obtained by cross-matching the top-1,000 DESI anomalies against 20 catalogs. No bootstrap, jackknife, or Poisson uncertainty is reported, nor is the dependence on the arbitrary top-1,000 cut quantified.  
**Required fix:** Provide a statistically defensible uncertainty on the novelty fraction or remove the numerical claim.

**P3-E4** §II.D & Table I (p. 6)  
The Path-C “native retrain” protocol is presented as the core methodological advance, yet three of the seven surveys (LAMOST, Gaia, eROSITA) still fail the 5σ injection-recovery gate after retraining. The headline catalog numbers mix surveys that pass and fail the same validation criteria without a uniform quality flag.  
**Required fix:** Either restrict the primary catalog to the four surveys that pass both gates, or supply a per-object “validation tier” column that downstream users can cut on.

### MAJOR

**P3-M1** §I & abstract (p. 1)  
“largest-scale application of autoencoder anomaly detection across seven astronomical archives” is technically true only because no prior work attempted seven archives simultaneously. The per-survey anomaly rates (0.87 % DESI, 3.38 % SDSS, etc.) are not demonstrated to be higher than the rates obtained by the same architecture on single surveys in the cited literature (Liang et al. 2023; Baron & Poznanski 2017). The “largest” claim is therefore a statement about scope, not performance.

**P3-M2** Fig. 2 (right panel) & §III.C (p. 5)  
The SDSS DR18 anomaly-score distribution is shown on a log–log scale spanning 12 orders of magnitude. The extreme tail (S > 10^10) is populated by only three objects; no robustness test against score outliers or against the precise definition of the validation MSE is provided.

**P3-M3** §V.B (p. 12)  
The statement that the anomaly catalog “provides high-bias tracer candidates for primordial non-Gaussianity constraints via the multi-tracer technique” is unsupported. The measured α_jk is consistent with zero at < 1σ, and the sample is dominated by cool dwarfs and training artifacts in at least two surveys. No forecast of the degradation of the multi-tracer gain under realistic contamination is given.

**P3-M4** Table I footnote ¶ & §III.D (p. 6)  
The 98 % blue-excess artifact rate in the LAMOST cross-transfer catalog is acknowledged, yet the 44,075 LAMOST anomalies are still included in the headline 378,280 count. The paper offers no quantitative estimate of how many of these objects survive a color or proper-motion cut that would remove the training-bias population.

### MINOR

**P3-m1** Eq. (2) (p. 2)  
S(x) is defined with μ_val and σ_val taken from the held-out 20 % split. The text never states whether these moments are recomputed after each native retrain or frozen at the cross-transfer values. Minor inconsistency in the caption of Table I.

**P3-m2** Fig. 1 caption (p. 4)  
“319,443 detections shown” includes the quarantined ACT block. The figure therefore mixes objects that are and are not part of the final catalog; a second panel or masking is needed for clarity.

**P3-m3** References  
Ref. [12] is listed as “in press” (2026). The arXiv number is absent; readers cannot verify the claimed 1.07 % anomaly rate.

### NIT

**P3-n1** Repeated use of the phrase “Path-C native retrain” without a one-sentence definition on first use in the abstract or introduction.

**P3-n2** Page 2, line 3: “(Dated: June 2026)” — future date in a submission that is already under review.

## Summary recommendation
**MAJOR REVISIONS**

The manuscript presents a valuable large-scale anomaly catalog and a transparent description of training-set bias mitigation. However, the cosmological claims in the abstract and §V rest on a statistically null measurement of the bias-enhancement parameter α_jk and on an unrelated PTA posterior that is mis-attributed to the anomaly sample. These sections must be either removed or rewritten as explicit forecasts with all caveats stated at the same prominence as the numerical results. In addition, the headline catalog numbers mix surveys that pass and fail the authors’ own validation gates; a uniform quality tier is required before the catalog can be treated as a community data product. Until these essential and major issues are addressed, the paper does not meet the evidentiary standard of Physical Review D.