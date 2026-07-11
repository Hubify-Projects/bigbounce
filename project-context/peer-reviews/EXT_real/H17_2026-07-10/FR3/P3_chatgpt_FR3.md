(1) VERDICT: REJECT

(2) ISSUES:

[MAJOR] Abstract, §III opening, and Tables I–II—“validated catalog-grade” headline. The 268,519-object subset is not selected by a coherent validation criterion: DESI uses S>5, SDSS uses a fixed-size “continuity slice” chosen to reproduce an earlier count, Planck uses a fixed top-200, and NEOWISE uses a fixed top-1% followed by a mask whose “recovery” is guaranteed by construction. No common false-discovery control, purity estimate, or calibrated selection function exists. Exact reproducibility of a count is not evidence that its members are real astrophysical anomalies. 

ext_P3_FR3

[MAJOR] §III A and Table III—internally inconsistent DESI science-target accounting. The reported per-class rates imply approximately 0.0075×4.9×10
6
+0.00037×1.5×10
6
≃37,300 GALAXY/QSO anomalies, whereas the alleged like-for-like science-target count is only 2,468. The footnote states that these rates use the same per-class denominators but attributes factors of roughly 16 and 6 to an inadequately explained bitmask join. This is not a harmless definitional difference; it invalidates the central 2,468-versus-2,685 benchmark until an object-level reconciliation is supplied.

[MAJOR] §III A and the “Strengthening” paragraph on p. 15—nature of the DESI detections. The manuscript states that approximately 98.7% of DESI anomaly clusters lack a primary science-class target bit and that 86% have DESI_TARGET=0, yet later infers from Redrock template labels that 98.8% are “real … objects, not sky/fiber/calibration artifacts.” A Redrock best-fit class, particularly when only about 0.1% have secure ZWARN=0 redshifts, does not establish that a sky or filler spectrum corresponds to an astrophysical point source. Sky-fiber and calibration positions must be removed or separately classified before the catalog can be called a point-source catalog.

[MAJOR] §II B and §VI C—training-set representativeness and score construction. Only 47,000 spectra, less than 0.21% of the DESI stream, are described merely as “representative,” without sufficient stratification by target class, observing conditions, S/N, arm coverage, sky fibers, or calibration state. The score uses per-spectrum median normalization and unweighted MSE rather than inverse-variance residuals; the authors themselves acknowledge that 44,436 B-dominant objects, 22.7% of the DESI tier, may be blue-arm calibration artifacts. A retraining and robustness study with realistic noise weighting, masks, and independently drawn training pools is required.

[MAJOR] §II B, §II D, and §VI D(i)—the claimed five-fold out-of-sample validation is not actually out-of-fold. Each fold model scores the full 47,000-object pool, so 80% of the objects in each score vector were used to train that model. Pairwise Jaccard overlap of those full-pool top sets therefore does not measure stability of genuinely out-of-sample predictions. Moreover, all five proxy models fail the manuscript’s own validation-loss retention gate. The appropriate test is one out-of-fold score per object from a production-equivalent model that excluded that object, followed by stability and calibration analyses on those scores.

[MAJOR] §VI D(i) and Table VI(b)—injection recovery and the unresolved DESI domain shift. The DESI injection test uses the cleanest 5% of spectra, one favorable broad/extended synthetic morphology, and a tail-excluded 99th-percentile recovery threshold that is not demonstrated to be identical to the production S>5 cut. It measures sensitivity to that plant, not catalog purity or the validity of individual members; narrow features recover only at ≳15σ. More seriously, the same production threshold reportedly flags over 50% of a random SPARCL sweep versus 0.87% of the catalog. Calling this a “curation effect” does not explain a factor-of-60 discrepancy and indicates a severe preprocessing or sample-selection dependence that must be resolved before any validation claim.

[MAJOR] §III C, Table II footnote ♡, Table IV, and Fig. 4—arbitrary SDSS catalog definition and mixing of analyses. The 77,905-object SDSS tier is explicitly selected only to equal the historical cross-transfer count; the defensible native top-1% contains 19,253 objects and the nominal S>5 cut contains 12. This arbitrary slice supplies a large fraction of the 268,519 headline and materially changes the deduplication. In addition, Table IV and Fig. 4 describe the obsolete cross-transfer set while surrounding text alternates between cross-transfer and native populations. A physically or statistically motivated threshold must be fixed in advance and every SDSS analysis repeated on that same native catalog.

[MAJOR] §III F and Table VII—Planck validation is compromised by spatial leakage and an unrealistic injection. The autoencoder is trained and scored on the same 200,000-patch bank, and randomly splitting 10° patches from one sky does not produce independent train and validation data because the patches overlap extensively and share sky modes. The quoted binomial p=5.5×10
−4
 assumes independence and therefore cannot support the memorization claim. The 100% recovery test inserts a broad ∼1.25
∘
 Gaussian bump after patch standardization without re-standardizing, making it a conspicuous distribution shift rather than a realistic CMB anomaly. Validation requires spatially disjoint blocks or simulations, half-mission/noise splits, foreground and point-source controls, and a calibrated false-positive analysis.

[MAJOR] §IV A—“genuine novelty fraction” of 17.8%. Absence within 5 arcsec from 18 catalogs does not establish that an entry is a genuinely novel astrophysical object. The calculation does not adequately treat catalog coverage, local source density, survey-dependent astrometry, proper motion, extended sources, or the possibility that the DESI coordinate is a sky/filler position. Because the parent DESI anomaly stream is overwhelmingly non-primary-target spectra, the target-type composition of the top 1,000 must be reported first. The Wilson interval quantifies only binomial sampling error and omits these much larger systematic uncertainties.

[MAJOR] §III B—twelve claimed z≃6 QSO candidates. These redshifts are Redrock fits to precisely the low-S/N outliers for which catastrophic template solutions are expected, yet the manuscript provides no quantitative line fits, likelihood comparison with low-redshift interlopers, ZWARN/quality information, expert spectral grading, or independent spectroscopy. Compact imaging morphology is not redshift confirmation. The objects may be listed as unconfirmed candidates, but the present evidence does not support a scientific high-redshift-QSO result.

[MAJOR] §V—empirical bias measurement and f
NL
	​

 forecast. An angular clustering-amplitude ratio cannot be interpreted as a three-dimensional linear-bias enhancement without the two samples’ redshift distributions, projection kernels, completeness maps, and matched selection functions. The 5,384 objects have no redshift cut and are unconfirmed QSO candidates, while the “full anomaly” comparison population has a different and poorly defined composition. Consequently α
jk
	​

=0.19±0.65 is not a calibrated tracer-bias measurement, and inserting it into an empirical one-parameter Fisher fit does not yield a defensible f
NL
	​

 forecast.

[MAJOR] §V, Appendix C, Table IX, and Fig. 11—mutually inconsistent Fisher prescriptions. The main text adopts 1/σ
2
=F
0
	​

+cα
2
, which gives σ(f
NL
	​

)≃5.67 at α=0.5, whereas Table IX’s linear scaling gives 7.15 at the same value. Figure 11 then uses an unrelated single-tracer normalization of 16.85 instead of 8.98. The clipped “envelope” and max(0,
α
^
2
−σ
α
2
	​

) construction are not a posterior interval or a principled estimator. These are substantive mathematical inconsistencies, not merely alternative plotting conventions, and the forecast must be recomputed from one documented likelihood/Fisher model.

[MAJOR] §V A and Appendix E—NANOGrav analysis is disconnected and does not test a specified bounce model. This section uses none of the anomaly catalog and therefore is not a downstream catalog application. It multiplies per-bin KDE approximations while discarding inter-bin covariance, derives a large Bayes-factor ratio from a far-tail KDE density without bandwidth or tail-sampling robustness tests, and compares only a fixed spectral slope with a free amplitude. The manuscript does not derive the full PTA-band spectrum and amplitude predicted by a concrete bounce model, so agreement with γ=3 is not evidence for that model. This analysis should be removed or submitted separately after a full likelihood and model calculation.

[MAJOR] §III E, §III G, §VI D, and Data Availability—provenance and reproducibility are not yet adequate for peer review. One production score axis is unrecoverable, a purported Gaia tier was later found to be synthetic fallback data, DESI native score products needed for full re-inference are reportedly on an exited pod, and the Planck checkpoint/tensor used for key tests is also unavailable. The public catalog, immutable DOI, hashes, weights, and executable stack are promised for later rather than supplied to the referee. Given the admitted provenance failures, an accessible frozen release and an independent end-to-end recomputation are prerequisites, not post-acceptance commitments.

[MAJOR] Title, Abstract, Tables I–II, and Conclusions—misleading process-volume accounting and category mixing. The “37.3 million” figure combines different processing passes and includes inputs associated with excised or quarantined components; 36.93 million is described as being “rounded up” to 37.3 million, while 37.29 million counts a wider cross-transfer-inclusive process volume rather than unique sources. Reprocessing the same data is not an additional astronomical source. The headline also combines point-source detections with 10° CMB sky patches and compares full-instrument-stream counts against science-target catalogs. The title and scale claims must instead report unique retained inputs and scientifically comparable catalog sizes.

[MINOR] Organization and presentation throughout. The manuscript is highly repetitive, alternates among native, cross-transfer, historical, exploratory, and validated populations, uses inconsistent “six-/seven-/eight-way” dedup terminology, and retains figures whose burned-in scores or populations are explicitly non-catalog quantities. A substantial rewrite with one authoritative flow diagram, one threshold table, and removal of obsolete analyses would be required even after the scientific problems are addressed.

(3) No—the central claim that 268,519 entries constitute a validated, catalog-grade set of real astronomical anomalies is not supported by the present selection definitions, internal bookkeeping, validation tests, or reproducibility record.
