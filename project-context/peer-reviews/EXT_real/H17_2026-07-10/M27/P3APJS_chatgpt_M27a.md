# EXT P3APJS ChatGPT — M27a (informational, older sibling) (recovered orphan)

- **reviewer:** ChatGPT (Extended Thinking Pro)
- **venue prompt:** P3APJS
- **chat URL:** https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a54d585-0a38-83e8-a1c3-cd0be3d9d8d2
- **status:** harvested-recovered (orphaned by ext_submit poll timeout; landed server-side, recovered 2026-07-13)
- **verdict (raw line 1):** REJECT

---

## Raw ChatGPT response (verbatim)

VERDICT: REJECT

ISSUES:

[MAJOR] Abstract, §2.2, Table 2, and §3.3 — the headline catalog size is threshold-engineered rather than scientifically defined. The 77,905-object SDSS contribution is a fixed-size “continuity slice” chosen specifically to reproduce the obsolete cross-transfer count; the same native scores yield 19,253 objects at the stated top-1% knee and only 12 at S>5. Thus a major fraction of the claimed 268,519 validated objects enters through an arbitrary bookkeeping choice, and the headline can change by tens of thousands without any change in the data or model. A catalog-grade selection requires a pre-specified threshold calibrated to completeness and false-positive rate. 

ext_P3APJS_M27

[MAJOR] §2.4 and the three-tier structure in §3 — “validated catalog-grade” is not a defensible common label. The retained surveys clear fundamentally non-equivalent gates: DESI, SDSS, and Planck have morphology-specific injection tests; NEOWISE has only a mask-geometry test that passes by construction; and low validation MSE is treated as interchangeable with signal recovery even though reconstruction loss does not validate tail membership, purity, or astrophysical reality. The paper explicitly acknowledges the mixed validation but nevertheless combines the components under one validated headline. NEOWISE should be exploratory, and each retained tier needs a common minimum validation standard. 

ext_P3APJS_M27

[MAJOR] §2.2, §6.4(i), and Data Availability — the dominant DESI catalog is not traceable or independently reproducible at the object level. The manuscript states that 86.6% of released DESI identifiers are internal hashes, that only approximately 1.3% of released rows can be re-pulled, and that the original input linkage and native score products were lost with the compute pod. Reproducing a deduplication count from already-produced tables is not equivalent to reproducing the catalog from archival spectra. ApJS publication requires stable archive identifiers, exact input-version provenance, preprocessing metadata, production checkpoints, and the ability to recover and inspect every listed spectrum. 

ext_P3APJS_M27

[MAJOR] §2.2 and §6.4(i) — the fresh-DESI calibration failure is unresolved. The production threshold gives a 0.87% rate in the released scan but flags more than 50% of a fresh SPARCL DESI sample; the reported fresh-pull median MSE of 0.233 also exceeds the stated production S>5 threshold near MSE =0.143. Calling this a “catalog-curation effect” does not reconcile a roughly sixty-fold rate discrepancy. Until the precise curation or preprocessing operation causing this shift is identified and reproduced, the fresh-pull injection tests cannot validate the production catalog.

[MAJOR] §3.1 — most DESI entries have not been established as astrophysical point sources. Only 2,468 of 190,015 deduplicated DESI clusters match spectra carrying primary science-target bits at 1
′′
, while approximately 98.7% fall on non-primary programs and 86% have DESI_TARGET = 0. Nevertheless, all 195,829 detections are included as catalog-grade point-source anomalies. The later presence of a Redrock template class does not prove that a sky, filler, calibration, or poor-quality spectrum corresponds to a physical source; Redrock will fit templates to such spectra as well. These streams must be separated, and the primary astrophysical catalog should presently be limited to demonstrably source-associated spectra. 

ext_P3APJS_M27

[MAJOR] §6.4(i) — the DESI validation does not establish catalog purity. Recovery of one broad synthetic morphology on a “cleanest-5%” substrate measures sensitivity to that plant, not the false-discovery rate or physical authenticity of 195,829 real candidates; no numerical equivalence is demonstrated between the injection threshold and the production S>5 selection. The fold models used for corroboration fail the paper’s own validation-loss gate, and the 0/200 visual-artifact result concerns a non-random top-ranked subset examined with a restricted artifact checklist. An end-to-end held-out test with production-quality models, realistic instrumental residuals, multiple anomaly morphologies, and independent expert labels is required.

[MAJOR] §2.1–§2.2 and §6.3 — the anomaly score has an inadequately characterized instrumental selection function. Spectra are downsampled to 496 bins, normalized by their own median, and scored with unweighted MSE that ignores inverse variance, bad-pixel masks, spectral resolution, arm-dependent calibration, and known sky/telluric regions. The admitted ≳15σ floor for narrow lines and the 44,436 B-dominant DESI objects show that the method is strongly morphology- and instrument-dependent. Moreover, “S=5” is a standardization of a heavy-tailed MSE distribution, not a calibrated five-sigma false-alarm significance. A noise-aware comparison, exact training-sample stratification, and robustness across model families are necessary before catalog-grade claims.

[MAJOR] §3.3, Figure 4, and Table 4 — SDSS results conflate the discarded cross-transfer population with the released native population. The displayed UMAP/HDBSCAN structure and emission-line census are explicitly calculated from the cross-transfer set, while the released catalog is the native-retrained continuity slice. These analyses therefore do not characterize the published SDSS tier. In addition, the very small score–redshift correlation, ρ=0.036, does not demonstrate astrophysical origin: observed-frame wavelength coverage, S/N, magnitude, calibration residuals, and template-fitting failures can all correlate with redshift. The native set needs its own taxonomy and matched controls in redshift, S/N, magnitude, plate, and observing conditions. 

ext_P3APJS_M27

[MAJOR] §3.6 and Table 7 — the Planck tier is not a validated CMB anomaly catalog. The top 200 are a predetermined count, the model is scored on a bank that includes its training patches, and the 10
∘
×10
∘
 patches overlap so extensively that a random patch-level train/validation split is not spatially independent. Consequently, the quoted binomial held-out enrichment p-value is not calibrated. The Gaussian-bump injection after per-patch standardization is also not representative of CMB foregrounds, beams, anisotropic noise, scanning artifacts, or cosmological non-Gaussian structures. Validation requires disjoint sky regions, end-to-end Planck simulations, foreground and noise nulls, overlap-aware statistics, and release of the exact production checkpoint.

[MAJOR] §3.8 — NEOWISE cannot be included in the validated tier. Its only passing test verifies that a latitude mask removes deliberately planted sources outside that mask, so success is guaranteed and says nothing about anomaly-detector sensitivity or purity. The 43,518-source parent selection is insufficiently specified, the scaler was fitted to the full sample, the train-only-scaler robustness test remains “queued,” and the feature table needed to perform it is unavailable. The 419 objects should be labeled exploratory until the full feature product and a genuine detector validation are supplied. 

ext_P3APJS_M27

[MAJOR] §4.1 — the claimed 17.8% “genuine novelty fraction” is not established. The manuscript does not show that the DESI top-1,000 sample is composed of real source-associated targets rather than sky/filler spectra, nor does it provide sufficient matching details on coordinate provenance, epochs, proper motion, catalog-specific radii, duplicate catalogs, crowded-field controls, or manual adjudication of the 178 unmatched cases. Because Legacy Survey imaging underlies much DESI targeting, a substantial unmatched fraction may indicate blank-sky fibers, coordinate/linkage failures, or matching failures rather than new objects. The assertion that novelty must decline monotonically with score is also untested and cannot make this sample an upper bound.

[MAJOR] §4.3 — the deduplication and cross-survey significance claims are not adequately supported. A 10
∘
 CMB patch is not the same type of entity as a point source and cannot meaningfully be deduplicated against point sources at 5
′′
; the Planck regions should be a separate product rather than added to a “unique-object” count. For the point-source catalogs, the claim of fewer than ten random coincidences is extrapolated largely from a non-geometry-preserving DESI–SDSS RA-shift control, while the large DESI–LAMOST and SDSS–LAMOST terms are not demonstrated with actual overlap masks. Pair-specific rotation or random-catalog nulls, astrometric uncertainties, proper motion, and a full survey-pair match matrix are required before stating that 637 coincidences exceed chance by >60×. 

ext_P3APJS_M27

[MAJOR] §3.5, §3.7, and the AI-assisted-methodology statement — the documented provenance failures require an independent integrity audit. A synthetic Gaia fallback entered the pipeline as purported survey data, and the eROSITA production score axis cannot be reproduced from any committed transformation. Excluding these tiers is necessary but does not by itself establish the integrity of the retained tiers, especially given the missing DESI linkage, unavailable NEOWISE feature table, and missing Planck checkpoint. Row-level archive provenance and independent spot checks must be provided for every retained survey rather than relying solely on author-generated audit JSON files.

[MAJOR] §5, Appendix C, and §5.1 — the cosmological applications should be removed from this catalog paper or completely reworked. The f
NL
	​

 forecast is built on an unvalidated QSO-candidate selection, a bias measurement consistent with zero, and an ad hoc clipped transformation of 
α
^
2
 that is neither a likelihood nor a posterior interval; two incompatible absolute Fisher normalizations are also presented. The stated GOLD criterion is a strict subset of the stated SILVER criterion, yet their counts are added without defining mutually exclusive tiers. The NANOGrav analysis is unrelated to the anomaly catalog and converts a factorized KDE free-spectrum approximation into strong point-template Bayes-factor language without covariance or KDE-tail robustness. Neither analysis supports the catalog claim, and both substantially obscure the paper’s actual contribution. 

ext_P3APJS_M27

[MAJOR] Title, Abstract, Tables 1–2, and Data Availability — the basic processing denominator and released product are not presented to catalog-publication standard. The manuscript variously reports 36.758 million retained-native inputs, 36.93 million read/scored inputs, 37.272 million Path-C process inputs, and 37.292 million cross-transfer-inclusive inputs as variants of “37.3 million”; 36.93 million does not round to 37.3 million, and the latter number includes historical, quarantined, or excised processing despite the title’s “native-trained scan” wording. One exact denominator and one canonical set of survey products are needed. The paper must also include a complete column dictionary, units, null conventions, source identifiers, quality flags, selection definitions, per-survey completeness/purity information, and a genuinely archival release containing all required checkpoints and intermediate products.

[MINOR] Figures 2–4, 8, and 10 — several figures document obsolete or non-catalog quantities rather than the released result. Figure 10’s caption describes Planck and NEOWISE validation, but the displayed curves omit them and also omit the headline DESI injection result; Figure 8 uses explicitly non-catalog display scores; and three prominent figures emphasize historical cross-transfer outputs. Replace these with native-catalog score distributions, actual released spectra and identifiers, representative failure cases, and complete validation curves. 

ext_P3APJS_M27

[MINOR] Throughout — the manuscript is excessively repetitive and uses overstrong terminology. Statements such as “validation establishes that the subset is real,” “catalog-grade,” “genuine novelty,” and “decisive” recur despite the stated caveats, while long internal path names and audit history dominate the scientific narrative. The paper needs substantial compression, a neutral distinction between candidates and confirmed objects, and relocation of pipeline-path details to a reproducibility appendix or repository.

The central claim is not supported: the manuscript documents a large anomaly-ranking exercise, but it does not establish a reproducible, objectively selected, uniformly validated catalog of 268,519 astrophysical anomalies.

