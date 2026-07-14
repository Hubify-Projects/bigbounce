(1) VERDICT: REJECT

(2) ISSUES:

[MAJOR] Abstract, §2.4, §3, and Tables 1–2 — the designation “validated catalog-grade” is not supported by a coherent validation standard. DESI, SDSS, Planck, and NEOWISE are combined into the 268,519-object headline despite fundamentally different selection and validation procedures: SDSS contributes an explicitly arbitrary fixed-size “continuity slice,” Planck contributes a predetermined top-200, and NEOWISE passes only a masking-geometry test that is guaranteed by construction. Injection recovery for one planted morphology measures sensitivity to that morphology, not purity, false-discovery rate, or the validity of every object above an unrelated selection threshold. The manuscript’s own “mixed-validation” qualification is incompatible with repeatedly presenting the aggregate as a catalog-grade sample.

ext_P3APJS_M44

[MAJOR] §3.1 and Table 3 — the DESI science-target accounting is internally inconsistent. The stated rates of 0.75% among approximately 4.9 million GALAXY spectra and 0.037% among approximately 1.5 million QSO spectra imply roughly 37,000 anomalies in the validated-TARGETTYPE subset, yet the positional recount reports only 2,468 anomaly clusters with a primary science-class bit. The explanation that these are merely “two filter stacks on the same per-class denominator” does not reconcile the discrepancy, especially because the bitmask selection is described as broader and less quality-restricted. The 2,468-object like-for-like benchmark and the conclusion that 98.7% of the catalog is non-primary therefore require a released, row-level crosswalk demonstrating exactly how each anomaly enters or leaves each count.

ext_P3APJS_M44

[MAJOR] §3.1 and §6.4 — the dominant DESI component is not demonstrated to be a catalog of astrophysical sources. The manuscript states that approximately 98.7% of deduplicated DESI anomalies do not match a primary science-class target and that 86% have DESI_TARGET = 0; the population is described as being dominated by sky fibers, filler spectra, and calibration exposures. Sky-fiber and calibration residuals are measurements of the instrument/background, not anomalous astronomical sources, and filler/secondary programs require separate characterization. The 195,829-object DESI contribution must be decomposed by fiber role and quality flags, with sky and calibration spectra removed from the source catalog and validated as a separate instrumental-diagnostics product.

ext_P3APJS_M44

[MAJOR] §2.2 and §6.4(i) — the claimed fully out-of-sample five-fold validation is not implemented as described. The public scoring driver explicitly scores the full pool with every fold checkpoint, and the aggregator constructs each top-1% set from those full score vectors. Consequently, training-pool objects are evaluated in-sample by four of the five models rather than receiving one genuinely out-of-fold score each; the resulting Jaccard statistic is predominantly a model-ranking stability test, not a held-out validation of anomaly membership. This is especially problematic because the manuscript reports that all five proxy models fail its own validation-loss retain gate.
GitHub
+1


ext_P3APJS_M44

[MAJOR] §6.4(i) — the DESI injection-recovery gate is misaligned with the released catalog selection. The released procedure chooses the cleanest 5–30% of a fresh science-spectrum sample and sets the detection threshold to the 99th percentile within that unusually clean band. The reported threshold is 0.1183, below the 0.2327 median reconstruction MSE of the complete held-out sample, while the catalog itself is dominated by non-science spectra absent from this validation substrate. Near-unity recovery of broad, high-amplitude plants under that permissive threshold does not validate the purity or completeness of the production S>5 population; injections must be performed in a representative sample of the actual scored stream and evaluated at the exact production threshold and preprocessing state.
Hugging Face
+1


ext_P3APJS_M44

[MAJOR] §2.2, §3.3, and Data Availability — the principal DESI catalog cannot be reproduced or independently audited object by object. The release reports that 169,611 of 195,829 rows carry synthetic/hashed identifiers, only an estimated 1.31% of rows can be re-pulled through the tested public archive route, the production score normalization is not committed, and exact released scores cannot be reproduced. This also conflicts with the manuscript’s later statement that all 195,790 primary-coadd anomalies joined to the DESI redshift catalog on TARGETID. An ApJS catalog requires persistent archive identifiers, exact input provenance, preprocessing metadata, and deterministic regeneration of every released score; method-level agreement on an unrelated fresh sample is not an adequate substitute.
Hugging Face
+1


ext_P3APJS_M44

[MAJOR] §3.6 and Data Availability — the identity and provenance of the released Planck catalog are contradictory. The release manifest describes planck_cmb_anomalies.parquet as the native-retrain top-200, whereas the accompanying methods documentation states explicitly that this file is the earlier 20,000-patch cross-transfer baseline and that the native checkpoint, 200,000-patch tensor, and full native scores were lost on an exited compute node. Thus the public product cannot simultaneously be the native catalog claimed in the manuscript and the cross-transfer file described by its own reproducibility documentation. The native Planck analysis must be rerun from public maps with committed extraction coordinates, checkpoint, split, and complete score vector before any Planck entries are retained.
Hugging Face
+2
Hugging Face
+2


ext_P3APJS_M44

[MAJOR] Data Availability — the released file inventory is not self-consistent with the manuscript. The paper says that the synthetic Gaia block was removed and is not released, but the manifest lists a 500-row Gaia file; it says the LAMOST block is part of the released Path-C catalog, whereas the manifest says no per-object LAMOST table is released and even claims LAMOST is excluded from every headline count, despite the manuscript’s 377,482 count explicitly including it. The paper cites commit 573b5da…, while the manifest names f738267… as its pinned revision and the repository subsequently added a v3.1.158 series. These are not cosmetic discrepancies: they prevent a reviewer from identifying which files constitute the submitted scientific product.
Hugging Face
+3
Hugging Face
+3
Hugging Face
+3


ext_P3APJS_M44

[MAJOR] §3.3, Table 4, and §6.2 — the SDSS native and cross-transfer populations are conflated. The validated headline includes 77,905 native-rescored objects selected solely so that their number equals the earlier cross-transfer count; the physically motivated native top-1% contains 19,253 objects and the nominal S>5 cut contains only 12. Meanwhile, the UMAP/HDBSCAN clusters and emission-line taxonomy are explicitly computed from the cross-transfer population, not necessarily from the released native slice. The manuscript does not report the membership overlap between these equal-sized but differently scored samples or recompute the scientific classifications on the actual released tier, so those results cannot be attributed to the claimed native catalog.

ext_P3APJS_M44

[MAJOR] §4.1 — the claimed 17.8% “genuine novelty fraction” is not established. Absence from 18 heterogeneous catalogs means only that no counterpart was returned under the adopted matching procedure; it does not establish a new astrophysical source. This is particularly serious because the parent DESI anomaly list is overwhelmingly composed of non-primary fibers, for which a blank position or instrumental residual naturally lacks a catalog counterpart. A defensible novelty analysis must be restricted to confirmed source-bearing targets, apply per-catalog footprint and depth masks, quantify proper-motion and positional uncertainties, inspect a statistically representative sample, and use “no catalog counterpart” rather than “genuinely novel” until physical sources are confirmed.

ext_P3APJS_M44

[MAJOR] §2.2 and §6.3 — the anomaly selection function is insufficiently characterized for a survey catalog. Spectra are normalized by their own nonzero-bin median, which can become unstable for low-continuum and sky spectra, and scored with unweighted MSE without inverse-variance weighting or a demonstrated bad-pixel/sky-line mask. The standardized score S is computed from the mean and standard deviation of a highly non-Gaussian reconstruction-error distribution, so “5σ” is not a calibrated statistical significance. No false-discovery rate, precision estimate, repeat-observation reliability, representative random visual audit, independent architecture, or completeness curve at the actual catalog thresholds is provided.

ext_P3APJS_M44

[MAJOR] §3.6 and §4.3 — point sources and CMB sky regions are combined through a physically meaningless deduplication operation. A Planck entry represents a roughly 10
∘
×10
∘
 map patch, whereas the optical and infrared entries are point-source detections; comparing their patch-center coordinates with a 5-arcsec point-source matching radius cannot test whether they represent the same physical anomaly. Their reported zero overlap is therefore expected by construction, and the aggregate “unique-object” count conflates incompatible scientific entities. The Planck patches must be a separate regional catalog with an angular-overlap definition appropriate to their footprints and must not enter the point-source deduplication or headline object count.

ext_P3APJS_M44

[MAJOR] §3.4 and Conclusions — the failed LAMOST tier should not be part of an inclusive science-catalog headline. The manuscript identifies 98% of the population as a blue-excess training artifact and reports only 5.8% recovery at the designated injection level, yet approximately 113,000 LAMOST entries are still included in the advertised 377,482 total. A known failed detector output can be valuable as a methodological diagnostic, but it should be released separately and excluded from every catalog-size or discovery statement.

ext_P3APJS_M44

[MAJOR] §4.2–4.3 — the spatial and cross-match significance calculations do not model the relevant selection functions. The HEALPix χ
2
 test assumes uniform counts over occupied pixels despite sharply varying survey footprints; the DESI–SDSS null uses RA shifts that do not preserve boundaries or angular-density structure; the NEOWISE polar-cap test assumes a uniform parent source density; and the Planck binomial calculation treats spatially overlapping patches as independent. These calculations cannot support claims of astrophysical clustering, negligible chance coincidence, or validation without survey-specific random catalogs, completeness maps, and block-resampling or rotation-based nulls.

ext_P3APJS_M44

[MAJOR] §5–5.1 — the cosmological applications are unsupported and outside the evidentiary scope of the catalog paper. The measured multi-tracer bias enhancement is consistent with zero, the de-biased estimate gives exactly no improvement, the forecast uses an imposed quadratic mapping and mutually incompatible absolute Fisher normalizations, and the 40,192 forecast-tracer sample is not the 5,384-object sample on which the bias was measured. The NANOGrav calculation is essentially unrelated to the anomaly catalog and evaluates fixed spectral-index references through a factorized KDE free-spectrum approximation rather than the timing likelihood. Both sections should be removed and, if pursued, subjected to independent analyses in dedicated papers.

ext_P3APJS_M44

[MINOR] Title, Abstract, Tables 1–3, and Conclusions — the presentation is excessively repetitive and obscures rather than resolves the provenance problems. The manuscript cycles among 36.76, 36.93, 37.27, and 37.29 million processed inputs; several obsolete cross-transfer figures remain prominent; the abstract is approximately two pages; and long internal file paths replace concise methodological descriptions. A future submission would need a substantially shorter title and abstract, one authoritative count/provenance table, removal of superseded analyses, and a clean separation among validated science products, exploratory products, and failed diagnostics.

ext_P3APJS_M44

(3) CENTRAL CLAIM: No—the arithmetic deduplication may be reproducible for some supplied tables, but the claim that 268,519 entries constitute a validated, catalog-grade anomaly sample is not supported because the dominant tiers lack representative purity validation, exact end-to-end provenance, and a self-consistent released data product.
