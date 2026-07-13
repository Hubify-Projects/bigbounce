VERDICT: REJECT

ISSUES:

[MAJOR] Abstract; §§2.4, 3, and 7 — The headline designation of 268,519 entries as a “validated catalog-grade” subset is not established. Recovery of selected synthetic perturbations demonstrates sensitivity to those perturbations, not the purity, false-positive rate, or astrophysical validity of the catalog entries; the gate thresholds are heuristic, and the NEOWISE gate is explicitly guaranteed by construction. These products should be described as ranked reconstruction-outlier candidates unless representative external validation supports a catalog-grade reliability claim. 

ext_P3APJS_M20

[MAJOR] Table 2 and §3.3 — The SDSS contribution of 77,905 objects is an arbitrary fixed-size “continuity slice” chosen to reproduce the size of the failed cross-transfer selection. The same native scores yield 19,253 objects at the stated top-1% knee and only 12 at S>5; therefore, the second-largest component of the validated headline has no statistically or physically motivated selection boundary. A pre-specified native threshold must be adopted and all headline counts, cross-matches, novelty statistics, and deduplications recomputed.

[MAJOR] §§2.2 and 6.4(i); Data Availability — The DESI catalog is not reproducible at the source level. The manuscript states that 86.6% of released identifiers are internal hashes, only approximately 1.3% of released rows are re-pullable, the native score parquets were lost, and exact per-row re-inference is structurally impossible. Reproducing a deduplicated row count from an already generated table is not equivalent to reproducing acquisition, preprocessing, inference, score calibration, and selection; every catalog row needs a canonical archive identifier and recoverable input provenance.

[MAJOR] §§3.1, 3.3, and 6.4(i) — The physical composition of the dominant DESI tier is unresolved. Section 3.1 states that approximately 98.7% of deduplicated clusters lack a primary science-target bit and describes them largely as sky/filler spectra, whereas §3.3 states that 98.8% of the joined anomalies have Redrock class GALAXY and are “not sky/fiber/calibration artifacts,” while also reporting that only approximately 0.1% have secure redshifts. These statements require reconciliation through an explicit breakdown by target bits, observing program, fiber type, exposure/coadd status, ZWARN, and spectral-quality flags.

[MAJOR] §§2.2 and 6.4(i) — The DESI validation does not establish the reliability of the released 195,829-object selection. The fold models fail the manuscript’s own validation-loss retention gate, operate only on the 47,000-spectrum training pool, and do not reproduce the production-scale catalog; the OOD comparison is a model-stability test rather than a truth test. The 0/200 artifact statement is based on the highest-ranked, non-random objects and therefore cannot support a binomial contamination bound for the full catalog; a random, score-stratified audit with independent reviewers and an end-to-end held-out production rescore is required.

[MAJOR] §§2.1–2.2 — The anomaly selection function is insufficiently specified. The manuscript calls the 47,000-spectrum DESI training set “representative” without giving a reproducible sampling design across target classes, observing conditions, spectrographs, nights, calibration states, and signal-to-noise; this omission is especially serious given the demonstrated LAMOST training-distribution failure. Full-sample scaler fitting for the tabular surveys, the missing NEOWISE scaler ablation, 16-fold spectral downsampling, per-spectrum median normalization, and unweighted MSE all can change the extreme-tail ranking and require controlled ablations.

[MAJOR] §§3.6 and 4.3 — Point sources and Planck 10
∘
×10
∘
 map patches are not commensurate catalog entities and cannot be combined into a single “unique anomaly” count using a 5
′′
 friends-of-friends rule. A patch center is neither a point source nor a uniquely localized physical object, and adjacent high-ranked patches may represent the same extended structure. The Planck regions must be released and counted separately with footprints, overlap fractions, and an area-aware clustering definition.

[MAJOR] §3.6 and Table 7 — The Planck validation is inadequate. Training and scoring use the same heavily spatially correlated patch bank; the train/validation membership calculation does not provide an independent sky test; and adding a 5σ, approximately 1.25
∘
-scale Gaussian bump after per-patch standardization without re-standardization is not a realistic end-to-end CMB sensitivity test. Validation requires spatially disjoint sky blocks and realistic signal, foreground, beam, component-separation, and correlated-noise simulations, with comparisons against known compact-source and foreground masks.

[MAJOR] §4.1 — The term “genuine novelty fraction” is unsupported. Absence within 5
′′
 from 18 selected catalogs establishes only catalog non-association under that matching procedure, not discovery of a new astrophysical object; this is particularly problematic when most DESI entries are non-primary targets and may include sky, secondary, calibration, astrometric, or acquisition-linkage failures. The 178 objects require object-by-object adjudication against their DESI targeting provenance, local catalog completeness, proper motion, image artifacts, and variable positional uncertainties before they can be called genuinely novel.

[MAJOR] §4.3 — The cross-survey association method is not catalog grade. A uniform 5
′′
 friends-of-friends radius ignores sub-arcsecond optical astrometry, NEOWISE blending and proper motion, differing observation epochs, source-density variation, and survey-specific covariance; stability of the total count over 3–7 arcsec does not establish that individual associations are correct. The 637 associations should be regenerated with probabilistic matching and accompanied by identifiers, separations, epochs, uncertainties, multiplicities, and association probabilities.

[MAJOR] §§3.1 and 6.5 — The claimed “like-for-like” comparison with the 2,685-object DESI EDR catalog is not like-for-like. The manuscript compares 2,468 detections obtained from a 20.3-million-row bitmask denominator with 2,685 detections from an approximately 250,000-spectrum study, using different preprocessing, thresholds, target definitions, and quality cuts; equality of absolute counts under denominators differing by roughly two orders of magnitude is not a performance benchmark. The comparison must be made on a common input sample or through matched rates and completeness/purity tests.

[MAJOR] §§3.3 and 6.2; Figure 4 and Table 4 — The SDSS astrophysical characterization is largely derived from the failed DESI-to-SDSS cross-transfer set, while the released headline tier is a native-model fixed-size slice. HDBSCAN clusters, the 84% cool-dwarf fraction, and the emission-line taxonomy therefore do not characterize the published native catalog unless membership correspondence is explicitly demonstrated. The clustering and taxonomy must be rerun on the final native selection and validated against external labels; moreover, ρ=0.036 is too small to establish that redshift-dependent instrumental or selection effects are absent.

[MAJOR] §5, Figure 9, and Appendix C — The f
NL
	​

 application is not a valid downstream constraint. The 5,384 QSO candidates lack a defined redshift distribution and spectroscopic confirmation; an angular clustering ratio relative to the full anomaly population is not automatically the three-dimensional linear-bias ratio required by the Fisher calculation; and the bias is measured on a different sample from the 40,192 redshift-binned forecast tracers. The fitted F
0
	​

+cα
2
 mapping, clipped “envelope,” and mutually inconsistent absolute Fisher normalizations do not substitute for a documented multi-tracer likelihood with masks, n(z), contamination, shot noise, covariance, and nuisance marginalization.

[MAJOR] §5.1 and Appendix E — The NANOGrav analysis is disconnected from the catalog and overinterpreted. The manuscript does not derive the asserted mapping from the stated bounce model to a PTA spectral index of exactly γ=3, and a fixed-slope comparison cannot discriminate a bounce background from the broader family of environmentally modified SMBHB spectra. Estimating a Bayes factor from a KDE density approximately 4.6σ into the posterior tail also requires bandwidth, boundary, Monte Carlo, and likelihood-compression sensitivity tests that are not reported; this analysis should be removed or submitted separately.

[MAJOR] §§3.5 and 3.7; Data Availability — The provenance failures are too serious for the present release to serve as an archival catalog. One survey silently fell back to synthetic Gaia data, the eROSITA production score axis is unrecoverable, major DESI linkage artifacts were lost, the Planck checkpoint and training tensor are unavailable, and the LAMOST per-object release status is contradictory. A new fail-closed pipeline run, independently audited manifest, and immutable release containing every final input, identifier, checkpoint, scaler, score vector, threshold, and table are necessary.

[MAJOR] Abstract, Tables 1–2, Figure 10, §6.4(ii), and Data Availability — Numerous internal accounting contradictions remain. DESI is called a detector-sensitivity PASS in the abstract and tier table but omitted from the stated “two detector-sensitivity PASS” synthesis and Figure 10; LAMOST both contributes to the 377,482 headline and is said to be excluded from every headline count or released per-object table; Gaia is described as removed while Gaia score products are still mentioned; and 36.76, 36.93, and 37.29 million are each used as versions of the scan volume. One authoritative manifest and one consistent set of tables must replace the overlapping historical and production accountings.

[MINOR] Figures 1, 5, 8, and 10 — Several figures do not display the evidence needed for their associated claims. Figure 1 force-includes selected exemplars; Figure 5 shows an optical saturated-source image rather than the NEOWISE measurements that generated the anomaly score; Figure 8 contains “display” scores and re-rendered reconstructions that are explicitly not catalog outputs; and Figure 10 omits the dominant DESI detector-sensitivity result. Scientific figures should use traceable catalog values, uncertainties, source identifiers, and final-model outputs.

[MINOR] Title, abstract, Introduction, and Conclusions — The manuscript is excessively repetitive and obscures the final data product beneath historical baselines, caveats, local repository paths, and multiple incompatible headline counts. The claims of “largest,” “validated,” “real,” “confirmed,” and “genuine novelty” should be restricted or removed, the cosmology material separated, and the paper rewritten around a concise final selection function, validation protocol, schema, and reproducibility statement.

No—the manuscript supports the existence of a large ranked set of reconstruction outliers, but not the claim that 268,519 heterogeneous entries constitute a reproducible, uniformly validated, catalog-grade anomaly sample.
