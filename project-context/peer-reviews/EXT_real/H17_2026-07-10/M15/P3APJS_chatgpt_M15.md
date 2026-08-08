(1) VERDICT: REJECT

(2) ISSUES:

[MAJOR] Title, Abstract, §3.1, and §7 — the dominant catalog entries are not established astrophysical sources. DESI contributes 195,829 detections, approximately 73% of the input to the “validated” headline, yet the manuscript reports that only 2,468 of 190,015 deduplicated DESI clusters match a primary science-class target within 1″, approximately 98.7% do not, and 86% have DESI_TARGET = 0. Sky fibers, calibration spectra, filler observations, and empty-sky positions cannot be counted as unique astrophysical “sources” without demonstrating an associated object and excluding instrumental or reduction residuals.

[MAJOR] §2.2, §3.1, and Table 6(b) — the DESI preprocessing and training design are likely selecting domain shift and reduction behavior. The composition of the 47,000-spectrum training pool is not documented relative to the 22.5-million-spectrum stream and its large sky/filler component. Dividing every spectrum by its nonzero-bin median can be ill-conditioned for near-zero sky spectra, while unweighted MSE ignores inverse variance, masks, bad pixels, and sky-subtraction uncertainties. The fact that the same nominal threshold flags more than 50% of an uncurated SPARCL sample, versus 0.87% of the production sample, demonstrates that undocumented upstream curation dominates the selection function.

[MAJOR] §2.2 and §6.4(i) — the five-fold Jaccard result is incorrectly characterized as fully out-of-sample validation. Each fold model is trained on 37,600 objects and then scores all 47,000, so most entries in every top-1% set were used to train that model; pairwise Jaccard overlap between those full-pool rankings is therefore largely an in-sample stability calculation. Only the held-out-block scores are genuinely out of sample. Moreover, all five proxy models fail the manuscript’s own validation-loss retention gate, and agreement among related BigAE models does not establish that the selected spectra are astrophysical anomalies rather than stable systematics.

[MAJOR] §3.1, Table 3, and §6.5 — the DESI target accounting and literature comparison are not reconciled. The quoted per-class rates imply roughly 37,000 GALAXY/QSO anomalies in the validated-TARGETTYPE population, whereas the science-bit recount yields only 2,468 total matches on nominally shared class denominators. The later assertion that 195,790 entries receive Redrock classifications does not resolve this, because a template classification of a sky or residual spectrum does not establish a physical source. Calling 2,468 versus 2,685 a “like-for-like” result is also invalid: the denominators are approximately 20.3 million versus 250,000, so the comparable anomaly rates differ by nearly two orders of magnitude.

[MAJOR] §3.3, Table 2, Figure 4, and Table 4 — the SDSS catalog component is defined by an arbitrary count and is characterized using a different sample. The 77,905-object tier was chosen solely to equal the historical cross-transfer count; the native top-1% selection contains 19,253 objects and the native S>5 selection contains 12. The manuscript nevertheless puts all 77,905 into the validated headline. Its injection test uses a 99th-percentile threshold and therefore does not validate the 4.05% continuity slice. Figure 4, Table 4, and the 84%-cool-dwarf taxonomy explicitly describe the cross-transfer set, not the native-retrained release, while the score axis is described inconsistently as both native and DESI-trained. The very small score–redshift correlation, ρ=0.036, also cannot exclude instrumental effects because redshift changes where spectral features fall relative to throughput, arm boundaries, and sky lines.

[MAJOR] §2.4 and §6.4(ii) — injection recovery is being used to claim more than it measures. Recovery of one or two synthetic perturbation families on a selected “cleanest 5%” substrate measures sensitivity to those particular plants; it does not measure catalog purity, the false-positive rate, calibration of the natural anomaly tail, or whether individual detections are real. The heuristic gates have no power calculation, realistic mixture model, blinded negative control, or validation across target class, S/N, observing condition, spectrograph, and score quantile. Consequently, the statement that validation “establishes that the 268,519 subset is real” is unsupported.

[MAJOR] §3.8 — NEOWISE does not meet the stated catalog-grade standard. Its only passing test plants positions outside the mask and recovers them by applying that same mask, so success is guaranteed by construction and says nothing about anomaly-detector sensitivity. The train-only scaler robustness test is explicitly unfinished, the parent 43,518-source selection is insufficiently specified, and the 419 entries are a predetermined top-percentile set. They must not be grouped under the same “validated” label as detector-sensitivity-tested components.

[MAJOR] §3.6 and Table 7 — the Planck validation is methodologically invalid. The native top-200 is a fixed count corresponding to 0.1% of the actual 200,000-patch score bank but is repeatedly presented using the superseded 20,000-patch 1% denominator. Training and validation patches are drawn from overlapping 10° regions of one sky map rather than spatially disjoint blocks. Over-representation of validation patches in the top tail is expected when training patches reconstruct better and is not evidence of astrophysical validity. The binomial calculation assumes equal, independent placement despite overlap; the text’s suggestion that correlation inflates the effective sample size is backwards, because the independence calculation overstates it. Finally, adding the Gaussian bump after standardization and not repeating the production standardization creates an artificial variance/mean shift rather than a realistic end-to-end injection.

[MAJOR] §4.1 — the 17.8% “genuinely novel” fraction is not established. The analysis does not first restrict the top-1,000 DESI entries to bona fide astrophysical sources, so nonmatches at sky-fiber positions are expected and are not discoveries. DESI targets ordinarily have targeting or imaging provenance, making a substantial unmatched fraction against a list that includes DESI Legacy Imaging DR9 a warning sign for coordinate, footprint, or catalog-query failures. The manuscript gives no per-catalog footprint and depth accounting, catalog-specific matching radii, proper-motion treatment, local-density false-match control, or blinded manual adjudication. The claim that the top-stratum value is an upper bound on the full-catalog novelty fraction is also an untested monotonicity assumption.

[MAJOR] §4.3 — the 5″ friends-of-friends operation does not establish unique physical objects. It merges heterogeneous optical observations, possible empty-sky fibers, infrared sources, and CMB patch centers using one angular radius, without coordinate uncertainties, source extent, epoch propagation, proper motion, stable target identifiers, or an observation-versus-object model. Ten-degree CMB patches are regions, not point detections to be deduplicated at 5″. Repeating the same flawed entity-resolution procedure at 3″ and 7″ only measures numerical sensitivity to the chosen radius; it does not validate the 268,519 or 377,482 “unique-object” counts.

[MAJOR] §2.2, §3.6, and Data Availability — the central data product is neither independently regenerable nor consistently described. The manuscript states that 86.6% of DESI identifiers are internal hashes and only about 1.3% of released rows can be re-pulled, while the production input linkage was lost. It also states that the Planck checkpoint and patch tensor needed for a full held-out re-inference are unavailable, yet later claims that no headline result depends on a nonpublic artifact. Data Availability says LAMOST both contributes to the 377,482 count and is excluded from the released per-object tables and “every headline count.” Recomputing a total from already-selected lists is not equivalent to reproducing the selection from public survey inputs. A complete column dictionary, coordinate/identifier provenance, per-survey score definition, ensemble-combination rule, quality flags, and retrievable archive identifiers are also absent from the manuscript.

[MAJOR] Title, Abstract, Table 1, and Table 2 — the 37.3-million scale claim is misleading. The retained-native body sum is 36.758 million, the stated read/scored sum is 36.93 million—which rounds to 36.9 million, not 37.3 million—and the 37.29-million quantity counts superseded or repeated processing passes, quarantined ACT processing, and pre-excision products. Processing the same or replacement data banks multiple times does not create additional sources or patches. The title must report distinct retained inputs, not an aggregate GPU process-volume accounting.

[MAJOR] §5, Figure 9, and Appendix C — the f
NL
	​

 application is not a valid downstream inference. An angular clustering ratio for 5,384 photometric QSO candidates without a measured N(z), contamination model, completeness map, or matched selection function cannot be inserted as a three-dimensional multi-tracer bias parameter. The Fisher calculation uses a different 40,192-object redshift-binned sample, with no demonstrated mapping between that sample and the measured α. The transformation max(0,
α
^
2
−σ
α
2
	​

) and the image of a symmetric α interval under a convex function are not a posterior or confidence interval for σ(f
NL
	​

). This section requires a new analysis, not qualification of the current null result.

[MAJOR] §5.1 and Appendix E — the NANOGrav analysis is unrelated to the catalog and is insufficiently specified. No catalog observable enters the PTA fit. The manuscript does not demonstrate how the published free-spectrum posterior KDEs were converted into likelihood factors, including removal of their per-bin priors, bandwidth sensitivity, or treatment of inter-bin covariance. The reported Bayes factor is dominated by a KDE-tail density comparison between two fixed spectral indices and does not compare a bounce model against the physically relevant family of environmental, eccentric, and broken-power-law SMBHB models. It should be removed from this ApJS catalog submission.

[MINOR] §4.2 — the spatial statistics are not interpretable as anomaly-rate tests. A χ
2
 test against uniform counts in occupied pixels is invalid for the combined, highly nonuniform survey footprints, and χ
ν
2
	​

≃15.5 is not a “weak” effect. Correlations of anomaly positions with Galactic latitude or dust, without division by the corresponding parent-catalog exposure and source-density maps on a per-survey basis, are not correlations of anomaly rate.

[MINOR] §4.1/Figure 6, Figure 8, and Figure 10 — plotted quantities and denominators are internally inconsistent. The 235/400 aggregate is described as top-100 samples from three surveys even though that denominator requires four surveys and includes the subsequently removed Gaia tier; Figure 8 uses explicitly non-catalog “display scores” as anomaly examples; and Figure 10 is described as a full survey synthesis but does not plot the DESI curve and visually omits the Planck and NEOWISE results emphasized in its caption. These figures cannot be used as evidentiary support in their present form.

(3) CENTRAL CLAIM: The central claim that the manuscript delivers a validated, reproducible catalog of 268,519 unique astrophysical anomaly sources is not supported, because the dominant DESI component is not shown to consist of sources, the SDSS component is defined by an arbitrary fixed-count slice, and the released selection cannot be independently regenerated from the public survey inputs. 

ext_P3A_M15
