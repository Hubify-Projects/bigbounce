VERDICT: REJECT

ISSUES:

[MAJOR] Abstract; §§2.4, 3, and 7 — “validated catalog-grade subset.” The validation gates do not establish that the 268,519 entries are reliable real-source anomalies or quantify catalog purity. They measure recovery of a few synthetic perturbations under survey-specific procedures; NEOWISE has only a deterministic mask-geometry check, Planck uses artificial Gaussian bumps, and DESI is validated only for one broad-feature family. The manuscript must not state that “validation establishes that the 268,519 subset is real” without representative blind tests, contamination estimates, and completeness functions for each component. 

ext_P3APJS_M42

[MAJOR] §§2.2 and 6.4(i); Data Availability — DESI object-level reproducibility. The manuscript states that 86.6% of released DESI identifiers are internal hashes, that only approximately 1.3% of released rows can be re-pulled, and that the original spectra and native score products were lost with the compute pod. Demonstrating that the code produces a similar score distribution on different SPARCL spectra does not reproduce the membership or scores of the released 195,829-object catalog. An ApJS catalog requires stable archive identifiers, a complete parent-sample manifest, and end-to-end regeneration of every released row.

[MAJOR] §6.4(i) — DESI injection-recovery protocol. The public implementation selects injection substrates from the cleanest 5% of spectra and defines its detection threshold from the 99th percentile of a tail-excluded 5–30% “clean band,” rather than applying the catalog’s declared S>5 selection to a representative parent sample. The code history explicitly records earlier implementations giving approximately 99.5% and approximately 0% recovery before the holdout definition was altered. The resulting 99–100% recovery is therefore highly protocol-dependent and post hoc; injections must be preregistered, performed across target class, signal-to-noise, observing condition, and artifact strata, and evaluated with the actual production threshold. 
GitHub
+2
GitHub
+2

[MAJOR] §3.1 and Table 3 versus §3.3 — contradictory DESI population accounting. The manuscript reports that approximately 98.7% of DESI anomaly clusters lack a primary science-target bit and that 86% have DESI_TARGET=0, but later treats Redrock best-fit classifications for essentially the whole anomaly set as evidence that the entries are “real objects, not sky/fiber/calibration artifacts.” Redrock assigning a best-fitting SPECTYPE, particularly when only approximately 0.1% have ZWARN=0, cannot establish that a sky or filler spectrum is astrophysical. Moreover, the stated TARGETTYPE rates imply roughly 37,000 galaxy-plus-QSO anomalies, whereas the science-bit recount gives only 2,468; the explanatory footnote does not provide an auditable shared-ID reconciliation.

[MAJOR] §§3.1 and 6.5 — claimed “like-for-like” comparison with Liang et al. Comparing 2,468 anomalies from a 20.3-million-row denominator with 2,685 anomalies from approximately 250,000 spectra is not like-for-like merely because both involve science-target classes. The corresponding reported rates are approximately 0.012% and 1.07%, differing by nearly two orders of magnitude. The paper must compare matched parent selections, quality cuts, thresholds, and rates, not only absolute counts.

[MAJOR] §§2.2 and 6.4(i) — DESI holdout evidence does not validate the production catalog. The five fold models used for the Jaccard and tail-preservation checks fail the manuscript’s own validation-loss gate, with mean best validation loss approximately 1.91 versus the required 0.30, and they test only the 47,000-spectrum training pool rather than the production ensemble on the full stream. More seriously, the same S>5 rule flags more than 50% of a random uncurated SPARCL sweep versus 0.87% of the catalog input. Calling this a “curation effect” does not resolve the enormous calibration dependence; a production-model holdout spanning the actual full-stream selection is required.

[MAJOR] §3.3 and Table 2 — arbitrary SDSS catalog threshold. The 77,905-object SDSS contribution is explicitly chosen to reproduce the size of the historical cross-transfer set, not from a statistical knee, false-positive criterion, or validation result. The native top-1% set contains 19,253 objects, while the nominal S>5 cut contains only 12. Including the fixed-size 77,905 slice in the “validated” headline makes a substantial fraction of the headline count an arbitrary continuity choice; the threshold and all downstream deduplication must be redone using an independently justified selection rule.

[MAJOR] §3.8 — NEOWISE cannot be part of a validated tier. Its only passing gate inserts objects outside the ecliptic-latitude mask and then “recovers” them by applying that same mask, so success is guaranteed by construction and tests no anomaly-detector sensitivity or purity. The feature scaler was also fitted on the full sample, and the promised train-only-scaler robustness test was not performed. NEOWISE must be labeled exploratory unless a genuine held-out detector test and parent-sample systematic analysis are supplied.

[MAJOR] §3.6 and Table 7 — Planck selection, leakage, and independence. The released top 200 are selected from a bank that includes training patches, and a random 85/15 split is not a true holdout when 200,000 overlapping 10
∘
×10
∘
 patches are extracted from the same masked sky. The binomial calculation assumes independent patches despite acknowledged spatial correlation and likely train–validation image overlap. The 5σ Gaussian-bump test, added after per-patch standardization without re-standardization, is an unusually conspicuous artificial signal and does not test foregrounds, scan strategy, beams, correlated noise, or realistic CMB anomalies. A spatial block split, overlap-aware clustering, simulations, and foreground/null tests are necessary.

[MAJOR] §§2.1–2.2 — insufficiently defined spectroscopic selection function. Spectra are downsampled to 496 bins, normalized by their own median, and scored with unweighted MSE, but the treatment of inverse variance, masks, bad pixels, missing arms, resolution differences, sky subtraction, and calibration flags is not specified at catalog-production depth. The 47,000-spectrum DESI training sample is called “representative” without a reproducible stratification over programs, target classes, nights, fibers, signal-to-noise, and observing conditions. Standardizing a non-Gaussian MSE distribution by its mean and standard deviation also does not make S=5 a five-sigma false-alarm threshold.

[MAJOR] §4.1 — “genuine novelty fraction” of 17.8%. Absence within 5
′′
 from a collection of catalogs is not equivalent to astrophysical novelty. Several listed catalogs have limited footprints or heterogeneous depth, and the analysis does not model local coverage, masks, proper motion, deblending failures, coordinate errors, or catalog-specific completeness. Because the DESI top stratum is not restricted to confirmed science targets and the manuscript reports that most DESI anomalies are sky/filler spectra, unmatched positions may represent blank-sky fibers or failed linkage rather than new sources. The claim must be renamed a coverage-aware “catalog-unmatched candidate fraction” and validated object by object on a representative sample.

[MAJOR] §4.3 — positional deduplication and cross-survey matches. A uniform 5
′′
 friends-of-friends radius ignores survey-specific astrometric uncertainties, source morphology, epoch-dependent proper motion, and WISE blending. Treating centers of 10
∘
 Planck patches as if they were point sources in the same union-find operation is physically meaningless. The random-coincidence estimate is based largely on an RA-shift control that the authors acknowledge does not preserve the footprints, and no pairwise match table, separation distribution, or geometry-preserving null is presented for the 637 claimed coincidences.

[MAJOR] Data Availability — public release contradicts the manuscript. At review time, the release manifest explicitly states that the LAMOST per-object table is not released, although LAMOST contributes approximately 113,000 detections to the 377,482 total and the manuscript says that its scored block is released. Conversely, the manifest lists a Gaia parquet although the manuscript says the synthetic Gaia block was removed and no Gaia block is released. The public manifest also currently names a different pinned hash from the hash printed in the PDF. Filtering a precomputed merged table reproduces an arithmetic count but does not independently reconstruct the catalog from its survey inputs; the immutable revision, file inventory, hashes, and manuscript must be made exactly consistent. 
Hugging Face
+2
Hugging Face
+2

[MAJOR] §5 — multi-tracer f
NL
	​

 demonstration. The Landy–Szalay angular-amplitude ratio is not a linear-bias ratio unless the candidate and reference samples have matched redshift kernels and selection functions; here the 5,384 QSO-candidate sample has no redshift cut and is compared with a heterogeneous anomaly population. The Fisher figure then uses a different 40,192-object redshift-binned sample. The coefficient c, covariance, survey volumes, redshift distributions, number densities, and full Fisher matrices are not adequately specified, while the estimator max(0,
α
^
2
−σ
α
2
	​

) and endpoint-mapped “envelope” are not a probabilistic uncertainty treatment. Appendix C’s linear-in-α scaling is also inconsistent with the main text’s α
2
 form.

[MAJOR] §5.1 — unsupported mapping of matter bounce physics to PTA γ=3. In the manuscript’s own PTA convention, Ω
GW
	​

∝f
5−γ
, so γ=3 corresponds to Ω
GW
	​

∝f
2
. No derivation is given showing that the stated scalar-only w=0 matter-bounce model produces this present-day nanohertz slope after transfer through the bounce and subsequent expansion. Citation [19] concerns particle production and reheating, while citation [20] discusses approximately scale-invariant primordial tensor spectra rather than establishing the asserted PTA value. The physical mapping must be derived before any bounce-consistency or Bayes-factor claim is admissible. 
arXiv
+1

[MAJOR] §5.1 and Appendix E — interpretation of the NANOGrav Bayes factor. The ratio of posterior KDE densities at two fixed spectral indices under a factorized free-spectrum approximation is a comparison between two phenomenological fixed-slope power laws, not evidence between complete matter-bounce and SMBHB population models. It neglects the physical spectral curvature, population and environmental parameters, inter-bin information beyond the product representation, and sensitivity of an extreme-tail KDE density to bandwidth and finite sampling. The term “decisive” should be removed unless full model evidences and robustness to likelihood construction and KDE choices are demonstrated.

[MINOR] Figures 2–4, 8, and 10; manuscript organization. Main-text figures mix obsolete cross-transfer results, quarantined ACT, excised synthetic Gaia, and display-only scores with released native results. Figure 10’s caption discusses Planck and NEOWISE while its displayed legend contains SDSS, LAMOST, eROSITA, and historical Gaia curves, and it omits the load-bearing DESI curve. The repeated audit-history prose and three different scan-volume totals obscure rather than clarify the catalog; failed tiers and cosmological demonstrations should be separated from a concise native-catalog paper.

No—the arithmetic count can be reproduced from derivative tables, but the central claim that 268,519 entries constitute a uniformly validated, object-level reproducible anomaly catalog is not supported.
