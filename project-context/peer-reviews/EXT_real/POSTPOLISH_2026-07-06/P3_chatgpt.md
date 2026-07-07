# EXT POSTPOLISH 2026-07-06 — P3 — ChatGPT

- **Provider:** ChatGPT (Pro), Big Bounce Book project
- **Model/effort:** Pro Extended
- **Chat URL:** https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a4ca89a-201c-83e8-8af7-e17485eaebe8
- **PDF:** P3_v3.1.140.pdf (md5 55459a5f46ec48754a74db448f1e7657)
- **Harvested:** 2026-07-07
- **Thought for:** 8m 8s
- **Parsed verdict (from response):** REJECT

## Raw verbatim response

(1) VERDICT: REJECT.
(2) ISSUES:

[MAJOR] Abstract/Conclusions, claim of "268,519 validated sources": the validated set includes heterogeneous objects and sky regions, not all "sources," and one component, NEOWISE, has only a masking-geometry QA gate that "passes by construction," not a detector-sensitivity validation; Planck is also a CMB map-patch tier, not a point-source catalog. This makes the headline terminology materially misleading.

[MAJOR] Section III/whole catalog, validation standard: the manuscript's own tiering shows that LAMOST fails injection recovery, eROSITA fails injection recovery and has an irreproducible score axis, Gaia was synthetic and removed, ACT is quarantined, NEOWISE is not detector-validated, and Planck is selected partly in-sample. This leaves the claimed multi-survey "validated catalog-grade" product much narrower and less secure than the title and abstract imply.

[MAJOR] Section III A, DESI headline: approximately 98.7% of raw DESI anomaly clusters are on sky-fiber, filler, or non-primary-science spectra, and the like-for-like science-target count is only 2,468, about 0.92× the cited prior benchmark rather than a major catalog-size advance. The paper acknowledges this but still foregrounds process-volume multipliers, which are not scientifically comparable.

[MAJOR] Section II B/Table I, inconsistent thresholding: DESI uses S > 5, SDSS uses a fixed-size "continuity slice," LAMOST uses top 1%, Planck and NEOWISE use fixed top-1% selections, and eROSITA uses a top-298 membership list with an unrecovered score axis. These choices prevent a coherent statistical interpretation of anomaly rates across surveys.

[MAJOR] Section III C, SDSS result: the SDSS headline count of 77,905 is explicitly a fixed-size continuity slice chosen to match the cross-transfer count, while the native S > 5 count is only 12 and the top-1% set is 19,253. Treating 77,905 as a catalog-grade component inflates the headline without a physically or statistically justified threshold.

[MAJOR] Section III E, eROSITA provenance: the production score threshold cannot be reproduced from committed artifacts, the production scores are non-monotone with the committed raw score, and injection recovery is 1.2%. A membership list alone may be worth releasing as an exploratory artifact, but it is not adequate for a PRD-level validated anomaly catalog or any score-dependent inference.

[MAJOR] Section III F, Planck CMB tier: the 200 Planck anomalies are selected from a scored bank that includes training patches, use raw MSE rather than the paper's canonical S definition, and are map patches rather than astrophysical sources. The held-out enrichment argument does not substitute for a held-out re-score of the trained model and is further weakened by spatial correlations.

[MAJOR] Section IV A, novelty claim: the only deep archival novelty estimate is 178/1,000 for the DESI top-1,000 against 18 catalogs, while the full-catalog novelty fraction is explicitly untested. The manuscript should not generalize this single top-stratum point estimate to the catalog as a whole.

[MAJOR] Section IV B, spatial analysis: the χ² non-uniformity test is admitted to be dominated by survey footprint geometry, and the absence of Galactic-latitude/dust correlation is not a sufficient control because the input surveys avoid the Galactic plane. The spatial analysis therefore does not establish astrophysical purity of the anomalies.

[MAJOR] Section V, fNL application: the empirical bias measurement is α = 0.19 ± 0.65, only 0.29σ from null, and the de-biased estimate gives no improvement over the single-tracer baseline. The cosmological section is therefore not a result at PRD significance level and should be removed or reduced to a non-claiming appendix.

[MAJOR] Section V A, NANOGrav application: fitting a power-law spectral index to a KDE free-spectrum likelihood and contrasting γ = 3.0 with an idealized γ = 4.33 SMBHB reference does not establish evidence for bounce cosmology, especially because the manuscript itself notes environmentally modified SMBHB models can yield γ ∼ 2.5–3. The Bayes-factor language is too strong for the model space actually tested.

[MAJOR] Reproducibility/data availability: the paper repeatedly relies on companion repository artifacts and states that the catalog, model weights, Zenodo DOI, and staged data "will be" public with arXiv posting. A real PRD submission cannot rest on unreleased artifacts for its central numerical claims.

[MAJOR] Section II B, preprocessing leakage and scaler provenance: full-sample scalers are used for eROSITA/NEOWISE, Gaia preprocessing was not recovered, and only eROSITA receives a bounded refit check. This is a serious provenance and leakage problem for an anomaly-ranking paper.

[MAJOR] Section VI D/Table V, validation gates: the validation thresholds are described as heuristic engineering thresholds, not statistically pre-registered or power-calibrated criteria. Several headline pass/fail classifications, especially SDSS at 64% versus a 50% gate, are therefore not robust enough for the claimed catalog grade.

[MINOR] Title/abstract: "Native-Trained Scan" is inaccurate as a blanket description because the manuscript preserves cross-transfer baselines, uses continuity slices motivated by cross-transfer counts, and quarantines/removes several tiers.

[MINOR] Section III/Table I: the table and footnotes are excessively complex and internally distracting; the reader must track multiple denominators, thresholds, caveats, removed tiers, and exploratory tiers to understand a single count.

[MINOR] Section III B: the z ≈ 6 QSO candidates rely on Redrock template fits at low continuum S/N and are explicitly unconfirmed. They should be presented only as follow-up candidates, not as a major scientific payoff.

[MINOR] Figures 3, 4, and 8: several plotted scores are on obsolete, cross-transfer, or display-only axes. These figures risk misleading readers unless rebuilt exclusively with final catalog score definitions.

[MINOR] Section VI B: the text still frames SDSS transfer-learning model dependence as a "feature," while the accepted Path-C narrative says native retrains replace cross-transfer results. This conceptual tension should be resolved.

[MINOR] References/context: the manuscript is written partly as an audit log and repository manifest rather than a physics paper; much of the pipeline-forensics material should be moved to supplementary documentation if the paper is resubmitted elsewhere.

(3) The central claim is not supported by the evidence presented: the manuscript does demonstrate a large, partly reproducible anomaly-detection pipeline, but it does not establish a coherent, detector-validated, scientifically interpretable 268,519-source catalog at the standard required for Physical Review D.
