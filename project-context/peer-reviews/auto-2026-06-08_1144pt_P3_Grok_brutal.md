# P3 auto-2026-06-08_1144pt — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 68.7s

---

**Referee Report — Physical Review D**

**Paper identifier:** P3 (multi-survey BigAE anomaly catalog)

**Overall assessment:** The manuscript presents a large-scale application of autoencoders to seven surveys but fails to meet PRD standards for methodological rigor, catalog cleanliness, and honest framing of results. The headline catalog is dominated by training artifacts and domain-shift failures; cosmological forecasts are statistically insignificant; and several load-bearing claims are unsupported or internally inconsistent.

**ESSENTIAL findings (paper cannot be accepted without fixes)**

- **P3-E1 (Abstract, p. 1; §III D, p. 3)**: Abstract states “378,280 Path-C Unique Anomalies” as the primary deliverable. Body shows this number is obtained only after (a) discarding the entire LAMOST native-retrain tier (113 k objects) as an “exploratory” artifact and (b) applying a 7-way 5″ deduplication that collapses 10 213 duplicates. The abstract does not disclose that >30 % of the input cross-transfer detections are known training-bias artifacts. Required fix: rewrite abstract to state the effective clean point-source sample size after all documented rejections.

- **P3-E2 (Abstract, p. 1; §III D, p. 3; Table I)**: Abstract claims “largest-scale application.” The only quantitative comparison offered is to Liang et al. (250 k spectra). No comparison is made to the full DESI EDR + DR1 releases already processed by other groups, nor to the cumulative SDSS + LAMOST public anomaly searches. The claim is unsupported.

- **P3-E3 (§III D, p. 3; §VI A, p. 12)**: 98 % of the LAMOST cross-transfer anomalies are identified as blue-excess training artifacts. The native-retrain still yields only 5.8 % injection-recovery at 5σ and is labeled FAIL. Retaining any LAMOST objects in the “Path-C unique” headline (even after rate compression) violates the paper’s own gate criteria. Required fix: remove all LAMOST objects from the primary catalog or relegate the entire survey to an appendix.

- **P3-E4 (§V B, p. 10; Appendix C)**: The Fisher forecast improvement is quoted as 7.9 % (central value 8.14 vs. 8.98). This is <1σ once the empirical \(\alpha_{jk}=0.19\pm0.65\) uncertainty is propagated. The text never states “not statistically significant” at every juxtaposition of the two numbers. Required fix: add explicit qualification or remove the improvement claim.

- **P3-E5 (Table I, p. 7; §III F, p. 4)**: Planck CMB tier uses a fixed top-1 % cut (200 patches) while all other surveys use either \(S>5\) or survey-specific percentiles. The two families are not commensurate; the table presents them as a single total. This is an apples-to-oranges aggregation.

**MAJOR findings (significant revision required)**

- **P3-M1 (§II D, p. 3)**: Path-C “native retrain” protocol is presented as the core methodology, yet five of the seven surveys still rely on cross-transfer scores for their headline counts. The reader cannot reconstruct which objects come from which protocol without Table I footnotes that are themselves contradictory.

- **P3-M2 (Fig. 2 right panel, p. 5; §III C, p. 5)**: SDSS DR18 scores span twelve orders of magnitude after cross-transfer. The native-retrain compresses the dynamic range but the paper never shows the before/after score distribution for the same objects. Domain-shift calibration failure is therefore not quantified.

- **P3-M3 (§IV A, p. 9)**: “Genuine novelty fraction ~17.8 %” is derived from a single top-1 000 subsample cross-matched against 20 catalogs. No bootstrap or jackknife uncertainty is reported. The number is presented as a discovery-rate figure when it is only an archival-completeness diagnostic.

- **P3-M4 (Fig. 7, p. 13)**: Injection-recovery curves show three surveys fail the 5\(\sigma\) gate. The caption does not state that these failures are the reason the corresponding native retrains were never executed. The figure is therefore misleading as a “validation” plot.

- **P3-M5 (length)**: 20 pages for a data-release paper whose primary new result is a catalog whose majority subsets are either artifacts or already-known populations. PRD typically expects ≤12–14 pages for such contributions.

**MINOR / NIT findings**

- **P3-m1 (p. 1)**: “(Dated: June 2026)” is a future date; harmless but should be corrected.
- **P3-m2 (Eq. 2, p. 2)**: Definition of \(S(\mathbf{x})\) uses validation-set \(\mu_\text{val},\sigma_\text{val}\). The text never states whether these are recomputed after each native retrain or held fixed from the DESI model.
- **P3-m3 (Table II, p. 8)**: “Uncatalogued” class (52.7 %) is the largest bin; its physical interpretation is left entirely to the reader.
- **P3-m4**: Multiple instances of “Path-C unique (primary)” in Table I footnotes are typographically awkward but not scientifically fatal.

**Summary recommendation**

**REJECT**

The manuscript’s central deliverable—a clean, multi-survey anomaly catalog suitable for cosmological or astrophysical follow-up—is not supported by the data products shown. The majority of objects in the largest single-survey subset (LAMOST) are acknowledged training artifacts; the Planck CMB tier uses an incommensurate selection; and the only quantitative cosmological result (\(f_\text{NL}\) forecast) is <1\(\sigma\). The paper would require a complete re-analysis with uniform, documented gates applied to every survey and a drastically shortened presentation focused on the subset that actually passes those gates. Until that is done, the work does not meet Physical Review D standards.