# INT API Review — P3APJS v3.1.161-apjs — openai (gpt-5.5)
paper: P3APJS  version: v3.1.161-apjs  model: gpt-5.5
provenance: commit=913f5033  pdf=pipelines/p3_anomaly_engine/paper3_apjs.pdf  sha256=ef7065b05badbdfe8bbeaf44f04895bccbc06354044a63c1651a4a8e5d5b56d1
modality: native-PDF (Files API input_file)
UTC: 2026-07-14T09:24:52.096420Z  |  latency: 45.7s  |  attempt: 1
usage: {"input_tokens": 47049, "input_tokens_details": {"cache_write_tokens": 0, "cached_tokens": 0}, "output_tokens": 2293, "output_tokens_details": {"reasoning_tokens": 799}, "total_tokens": 49342}
PARSED VERDICT: REJECT

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: REJECT.

(2) ISSUES:

1. [MAJOR] Title/Abstract/§3/Table 1/Table 2 — The headline “multi-survey anomaly-candidate catalog” is not a coherent, validated catalog product: the reported counts mix validated DESI/SDSS rows, geometry-only NEOWISE rows, failed/exploratory LAMOST aggregate counts, archival failed Planck cross-transfer patches, excised eROSITA rows, and quarantined synthetic Gaia rows.

2. [MAJOR] Abstract/§3/§6 — The central count of 268,319 “validated point-source” candidates is not adequately supported as a validated science catalog: DESI is dominated by non-primary sky/filler spectra, SDSS uses a fixed-size continuity slice rather than a physically motivated native anomaly threshold, and NEOWISE passes only a mask-geometry QA test, not detector-sensitivity validation.

3. [MAJOR] §3.1/Table 3 — The DESI headline is scientifically misleading: only 2,468 deduplicated anomaly clusters match primary science-class targets, while ∼98.7% of DESI clusters are on sky/filler/non-primary spectra; presenting 195,829 DESI anomalies as a major scientific point-source tier overstates the astrophysical content of the catalog.

4. [MAJOR] §2.2/§3.3/Table 2 — The SDSS 77,905-row contribution is not an anomaly threshold result but a fixed-size continuity slice; the native top-1% is 19,253 and strict S > 5 gives only 12 sources. Including the 77,905 slice in the “validated” point-source product is not scientifically justified.

5. [MAJOR] §3.8/Fig. 9 — NEOWISE validation is inadequate for inclusion in a validated science tier: the claimed 100% “recovery” is guaranteed by applying the same ecliptic mask used to define the selection and does not test anomaly-detector sensitivity, purity, or astrophysical reliability.

6. [MAJOR] §3.4/Data Availability — LAMOST is described as a 98% blue-excess training-bias failure with 5.8% injection recovery and no released per-object table, yet its ∼113,000 objects enter the 377,282/377,482 continuity accounting. This is not an ApJS-quality released catalog component.

7. [MAJOR] §3.6/Data Availability — The Planck situation is unacceptable for a catalog paper: the released 200-row table is explicitly the failed cross-transfer baseline, while the supposedly validated native top-200 table, checkpoint, tensor, and score bank are unavailable. The manuscript cannot claim a validated Planck product.

8. [MAJOR] §3.5/Table 5 — The eROSITA score axis is irreproducible, the detector-sensitivity gate fails at 1.2%, and the tier is reduced to a membership-only addendum. This is properly excluded from counts, but its presence further demonstrates that the frozen release is not a clean multi-survey anomaly catalog.

9. [MAJOR] §3.7/Data Availability — The frozen release contains a synthetic Gaia placeholder file. Even though quarantined in the text, the presence of synthetic data in a public astronomical catalog release is a serious provenance failure and would require a corrected release before publication.

10. [MAJOR] §2.2/§2.4/§5.4 — Reproducibility is insufficient: most DESI released identifiers cannot be rejoined to public spectra, exact released-row rescoring is structurally impossible, raw native score parquets are lost, the native Planck products are absent, and LAMOST row-level data are absent. This falls below ApJS data-product standards.

11. [MAJOR] §2.2/§5.4 — The DESI validation evidence is weaker than claimed: the k-fold models are short-trained proxy models that fail the manuscript’s own validation-loss retain gate, the Jaccard and tail-preservation checks are correlated diagnostics from the same score vectors, and the injection-recovery result validates mainly broad/extended residuals rather than the full anomaly population.

12. [MAJOR] §2.2/Table 2/Fig. 3 — The score definitions and thresholds are heterogeneous and sometimes incompatible: canonical S has exceptions, SDSS and LAMOST cross-transfer/native scales are mixed, Planck uses raw MSE, eROSITA uses an irreproducible score-knee axis, and several figures/tables compare or display scores that are not commensurate.

13. [MAJOR] §4.1/§6 — The novelty claims are not established for the released catalog: the only genuine novelty estimate is 178/1,000 for the DESI top-1,000 stratum, explicitly not survey-wide; SIMBAD-unmatched fractions are database-coverage diagnostics and should not be used as discovery-rate evidence.

14. [MAJOR] §3.2/§3.3/§6 — The high-redshift QSO and BAL QSO claims are insufficiently validated for catalog-level scientific emphasis: redshifts are Redrock template fits for anomalous spectra, many have poor/uncertain pipeline reliability, and the manuscript repeatedly notes that visual inspection or re-observation is required.

15. [MAJOR] Data Availability — The reviewed frozen tag is acknowledged to have an incorrect/obsolete manifest, missing key products, and no corrected v3.1.161 release tag. A local “corrected interpretation” is not a substitute for a complete, immutable, citable ApJS data release.

16. [MAJOR] Overall — The manuscript reads as a post-hoc audit of a heterogeneous and partly failed pipeline rather than a clean survey catalog paper: many central products are “continuity,” “archival,” “exploratory,” “quarantined,” or “membership-only,” which is incompatible with the title and abstract framing.

17. [MINOR] Figures 3, 4, and 8 — Several figure captions refer to cross-transfer score axes, display-only scores, or non-catalog scores; these are confusing and risk misinterpretation by catalog users.

18. [MINOR] §4.2 — The spatial χ² analysis is dominated by survey footprint geometry and is correctly caveated, but it adds little scientifically and should not be presented as a meaningful spatial-uniformity test without selection-function modeling.

19. [MINOR] §2.2 — Full-sample feature scaling for tabular surveys leaks validation-set information into preprocessing; although partially bounded for eROSITA, this should not be part of a production catalog pipeline.

20. [MINOR] Writing/organization — The manuscript is excessively caveated and internally repetitive, making it difficult to determine what the actual released, science-usable product is; a publication-quality version would need a much shorter, unambiguous inventory-first structure.

(3) The central claim is not supported: the released product is too heterogeneous, incomplete, partly irreproducible, and weakly validated to constitute an appropriate ApJS multi-survey anomaly catalog in its present form.