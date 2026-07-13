VERDICT: REJECT

ISSUES:

[MAJOR] Abstract; §3 “Three-tier catalog structure”; §7 central catalog claim. The statement that validation establishes 268,519 “real,” “catalog-grade” anomalies is not justified. Injection–recovery measures sensitivity to selected synthetic perturbations, not the purity or astrophysical reality of the objects selected from real data. No representative labeled test set, empirical false-discovery rate, blank-sky or artifact negative control, or catalog-wide contamination estimate is provided; moreover, NEOWISE passes only a deterministic mask-geometry test, while DESI and Planck are partly scored in sample. The product may be described as a reconstruction-outlier candidate list, but not as a validated catalog of real anomalies. 

ext_P3APJS_M39

[MAJOR] §2.2, §6.4(i), and Data Availability: irreproducible source-level provenance. The manuscript states that 86.6% of released DESI identifiers are internal hashes, only about 1.31% of released rows can be re-pulled, and the original spectra and native score products needed for exact re-inference were lost. The cited public release also conflicts with the manuscript: LAMOST contributes approximately 113,000 detections to the 377,482 total, yet the manifest explicitly says that no LAMOST per-object table is released; a Gaia file remains present although the paper says no Gaia block is released; the documented merged schema does not contain several claimed per-object products; and the release metadata is internally inconsistent about the pinned commit. The catalog can therefore be counted as a frozen table, but cannot be independently regenerated or audited from its native survey inputs to the standard required for an ApJS catalog. 

ext_P3APJS_M39

 
Hugging Face
+2
Hugging Face
+2

[MAJOR] Table 2, footnote ♡, and §3.3: the SDSS contribution is defined by an arbitrary count. The 77,905-object SDSS tier is explicitly chosen to equal the historical cross-transfer count, not by a native score threshold, completeness criterion, score knee, or false-discovery target. The same native scores yield 19,253 objects at the top 1% and only 12 at S>5. Because this arbitrary continuity slice supplies nearly 78,000 detections to the 268,519 headline, the central catalog size is not a data-determined scientific result. A prespecified, survey-native selection rule must be adopted and all headline counts and downstream analyses recomputed. 

ext_P3APJS_M39

[MAJOR] §3.1, Table 3, and §6.5: the DESI “like-for-like” comparison is invalid and the source-population accounting is contradictory. Comparing 2,468 anomalies selected from a 20.3-million-row science-bit catalog with 2,685 anomalies from an approximately 250,000-spectrum study is not like-for-like merely because both contain science targets; the corresponding yields differ by roughly two orders of magnitude. More seriously, §3.1 says about 98.7% of DESI anomaly clusters lack a primary science-class bit and 86% have DESI_TARGET=0, while §3.3 later calls 98.8% of the same anomaly stream Redrock-classified galaxies and treats this as proof that they are real objects rather than sky or calibration artifacts. With only approximately 0.1% carrying secure ZWARN=0 redshifts, forced Redrock template labels do not resolve that contradiction. The DESI catalog must be rebuilt on one clearly defined, quality-controlled object denominator. 

ext_P3APJS_M39

[MAJOR] §2.2, Equations (1)–(2), §3.1, and Table 6(b): the anomaly score has no calibrated statistical meaning. S is merely a mean-and-standard-deviation rescaling of a highly non-Gaussian reconstruction-error distribution; the fact that 0.87% of DESI spectra exceed “S>5” itself demonstrates that this is not a five-sigma false-alarm threshold. The score uses unweighted MSE after aggressive 496-bin resampling and per-spectrum normalization, without inverse variances, bad-pixel masks, sky-line weights, or an explicit noise model. The reported result that the same threshold flags more than 50% of an uncurated SPARCL sweep shows severe dependence on undocumented curation and domain selection. An empirical null distribution, survey-condition stratification, and calibrated false-discovery analysis are required. 

ext_P3APJS_M39

[MAJOR] §2.2 and §6.4(i): the held-out tests do not validate the production catalog. The five fold models used for the main Jaccard and tail-preservation arguments all fail the manuscript’s own validation-loss retention gate, and the two reported checks are derived from the same score vectors. Random spectrum-level folds also do not demonstrate independence with respect to repeated objects, observing nights, fibers, tiles, or calibration states. The 0/200 visual-artifact result concerns a selected top-ranked subset inspected under a narrow artifact definition and cannot bound contamination in 195,829 entries. Production-model inference is needed on object- and exposure-disjoint held-out data, with independent blinded review of a representative sample across score and target strata. 

ext_P3APJS_M39

[MAJOR] §2.4 Step 5, §6.4(ii), and Figure 10: the injection tests do not form a common validation protocol. Broad DESI spikes, SDSS/LAMOST continuum dips, eROSITA latent perturbations, Planck Gaussian bumps added after patch standardization, and a NEOWISE coordinate-mask test probe different quantities, with incompatible definitions of “5σ.” Their recovery thresholds are also not generally the thresholds used to define the published tiers. No artifact injections, realistic known-object benchmarks, S/N and wavelength stratification, or false-positive tests are supplied. In addition, Figure 10 and §6.4(ii) still state that only SDSS and Planck pass detector-sensitivity testing, whereas the abstract and later DESI text describe DESI as an additional detector-sensitivity pass; the load-bearing validation summary is internally inconsistent. 

ext_P3APJS_M39

[MAJOR] §3.6 and Table 7: the Planck analysis has spatial leakage and an invalid interpretation of its held-out count. The 200,000 ten-degree patches are drawn from a single sky map with no demonstrated non-overlap or block separation, yet training and validation are randomly split and the full bank, including training patches, is ranked. An excess of validation patches in the high-error tail is exactly what can occur when a model reconstructs its training patches better; it does not rule out memorization. The quoted binomial probability assumes independent patches despite acknowledged spatial correlation. Furthermore, the retained 200 patches are 0.1% of the native 200,000-patch bank, not 1%, and deduplicating ten-degree sky regions against point sources using a five-arcsecond center separation is physically meaningless. A spatially blocked analysis with non-overlapping patches, foreground/component-map cross-validation, and region-level association rules is required. 

ext_P3APJS_M39

[MAJOR] §3.8: NEOWISE cannot be included in the “validated catalog-grade” tier. Its sole passing gate is a mask test designed so that the planted polar-cap objects must fail the mask; this validates a conditional statement in the masking code, not the autoencoder. Detector sensitivity, contamination, repeatability under a train-only scaler, and robustness of the top 1% membership have not been measured, and the origin and selection function of the 43,518-source parent sample are not adequately specified. NEOWISE should remain exploratory until detector-level validation is completed. 

ext_P3APJS_M39

[MAJOR] §4.1 and Figure 6: “17.8% genuine novelty” is an unsupported interpretation of catalog non-matches. Absence within a fixed-radius match to 18 catalogs is not evidence that an astrophysical object is genuinely novel. The analysis does not condition on each catalog’s footprint, depth, epoch, proper motion, blending, positional covariance, or local source density, and no likelihood-ratio matching or coverage-corrected control is shown. Because the DESI anomaly population is dominated by sky/filler and non-primary fibers, a missing imaging counterpart may simply indicate that no source was targeted. The result must be called a catalog-unmatched fraction and restricted to secure astrophysical source spectra before any discovery-rate claim is made. 

ext_P3APJS_M39

[MAJOR] §4.3: the five-arcsecond deduplication does not define physical objects consistently across the retained surveys. One radius is applied to subarcsecond optical astrometry, WISE-derived sources, repeated spectra, and ten-degree Planck patches, without per-source uncertainties, proper-motion propagation, or association probabilities. The RA-shift control is acknowledged not to preserve footprint geometry, so it cannot support the claimed random-coincidence bound. The 637 coincidences are therefore candidate positional associations, not cross-survey validation, and the “unique-object” terminology is inappropriate for the CMB stratum. 

ext_P3APJS_M39

[MAJOR] §3.3, Figures 3–4, and Table 4: canonical SDSS results are conflated with a historical failure set. The native continuity slice and the DESI-to-SDSS cross-transfer sample both contain 77,905 entries only because the native slice was deliberately sized to match the earlier count. The UMAP/HDBSCAN clusters, 84% cool-dwarf fraction, emission-line taxonomy, extreme 10
11
 scores, and several figures refer to the cross-transfer membership, whereas adjacent prose makes claims about the native catalog. Their membership overlap is not reported. All scientific characterization must be recomputed on the actual native-selected objects, and the failed transfer set should be confined to a methods appendix. 

ext_P3APJS_M39

[MAJOR] Title, abstract, Tables 1–2, and §7: the scale claims aggregate incompatible quantities. The manuscript gives 36.76 million, 36.93 million, and 37.29 million under different accounting conventions and obtains “37.3 million” partly by counting historical processing passes, superseded patch banks, quarantined data, and excised feature-table reads rather than unique astronomical inputs. The title also describes spectra and map patches although the accounting includes tabular X-ray and infrared catalogs. Likewise, 377,482 combines a known-failed LAMOST tier with point sources and 200 extended CMB regions selected using predetermined ranks. These are useful bookkeeping totals but not a homogeneous anomaly-catalog size or a defensible basis for “largest catalog” multipliers. 

ext_P3APJS_M39

[MAJOR] §5, Figure 9, and Appendix C: the f
NL
	​

 forecast is not internally or statistically valid. An angular clustering amplitude for 5,384 photometric QSO candidates, measured without a modeled redshift distribution, completeness mask, stellar-contamination model, or scale-dependent bias treatment, cannot calibrate the three-dimensional multitracer bias used in the Fisher analysis. The bias sample is also different from the 40,192 tracers used in Figure 9. Mathematically, the main 1/σ
2
=F
0
	​

+cα
2
 prescription gives σ(f
NL
	​

)≃5.67 at α=0.5, whereas Appendix Table 9 gives 7.15 from an incompatible linear scaling; Figure 11 then adopts another absolute normalization, 16.85 rather than 8.98. This section requires a complete independent reanalysis and should not appear as a result of the present catalog paper. 

ext_P3APJS_M39

[MAJOR] §5.1 and Appendix E: the NANOGrav analysis is unrelated to the catalog and does not establish a matter-bounce test. No anomaly-catalog quantity enters the PTA likelihood. The analysis multiplies marginal free-spectrum KDEs, omits information not encoded in that factorization, and estimates the γ=4.33 density far in a KDE tail without bandwidth, finite-chain, or alternative-likelihood uncertainty on the quoted Bayes factor. More fundamentally, fitting a free-amplitude power law with fixed γ=3 is not a matter-bounce model prediction unless the PTA-band transfer function and amplitude are derived; that derivation is absent. This material should be removed and, if pursued, submitted as a separate PTA paper using a full model likelihood. 

ext_P3APJS_M39

[MINOR] Abstract, figures, and manuscript organization. The abstract is exceptionally long and repeats the process-volume caveat, while much of the paper and several principal figures emphasize superseded, failed, quarantined, or removed tiers: Figure 2 includes ACT and synthetic Gaia, Figures 3–4 show transfer failures, Figure 8 prints non-catalog display scores, and Figure 10 omits the newly asserted DESI validation curve. The final validated candidate set should be the visual and narrative focus, and the manuscript should be substantially shortened after the scientific issues are resolved. 

ext_P3APJS_M39

The central claim is not supported: the work demonstrates a large and heterogeneous collection of reconstruction outliers, but not a reproducible, uniformly validated catalog of 268,519 real astronomical anomalies.
