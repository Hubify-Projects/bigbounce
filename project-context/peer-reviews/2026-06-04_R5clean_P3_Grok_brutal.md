# P3 2026-06-04_R5clean — Brutal-honesty journal referee (treating this as a real PRD submission)

**Model**: `grok-4.3`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 16.0s

---

**Referee Report: P3 (2026-06-04_R5clean)**

**Paper length**: 49 pages. PRD methods/catalog papers are typically 15–30 pages. This manuscript is substantially overlength for its incremental methodological contribution (native-retrain protocol + multi-survey deduplication on an existing autoencoder architecture). The excess is driven by repetitive before/after tables, exhaustive caveat enumeration, and extended appendices that belong in supplementary material or a data-release note.

**ESSENTIAL findings**

P3-E1. Abstract (p. 1) vs. body mismatch. The abstract states “the largest-scale application of autoencoder anomaly detection across seven astronomical archives to date” and presents the 378,280 headline as the primary result. The body repeatedly qualifies that the catalog-grade subset is ~265,000 (after excluding LAMOST exploratory tier), ACT is quarantined, Planck patches are not point sources, and the genuine novelty fraction is only 17.8 % at the top-1,000 DESI stratum. Required fix: rewrite the abstract to state exactly what the body proves (native-retrained counts after 7-way 5″ deduplication, with explicit tier stratification and the 17.8 % point estimate).

P3-E2. Over-claim of novelty. The abstract and §I repeatedly use “first multi-survey anomaly detection campaign at combined scale exceeding 37.3 million.” Prior single-survey autoencoder papers (Baron & Poznanski 2017; Liang et al. 2023; Nicolaou et al. 2026) already exist; the present work is an engineering-scale application of the same architecture plus a native-retrain protocol. Required fix: remove all “first”/“largest”/“unprecedented” language or qualify it strictly as “largest published catalog produced by this specific pipeline.”

P3-E3. fNL forecast presentation. Section V and the abstract headline a central σ(fNL) = 8.14 (7.9 % improvement) while the body states the empirical αjk = 0.19 ± 0.65 is consistent with zero at 0.29σ and the improvement is < 1σ from null under the Fisher-positivity-respecting form. The linear-extrapolation tail that exceeds the single-tracer floor is correctly flagged as unphysical, yet the headline number is still presented as the primary result. Required fix: move the empirical-α forecast to a “preliminary, consistent-with-null” status; the only robust claim is the upper bound on improvement.

P3-E4. Injection-recovery gate inconsistency. Six surveys are tracked; only three pass the formal ≥ 50 % recovery at 5σ gate. The remaining three (including LAMOST at 5.8 % continuum-dip) are retained with “informative cross-validation diagnostics.” The gate is therefore not applied uniformly. Required fix: either enforce the gate for all surveys or reclassify the failing surveys as exploratory only (as already done for LAMOST).

P3-E5. Lack of independent anomaly detector for the three dominant spectroscopic surveys. Only Gaia and eROSITA receive IsolationForest cross-validation; DESI/SDSS/LAMOST rely solely on BigAE. Required fix: apply at least one orthogonal detector (IsolationForest or VAE) to the spectroscopic samples and report overlap fractions.

**MAJOR findings**

P3-M1. Length. Reduce to ≤ 25 pages (main text + figures). Move Table I, the full taxonomy galleries, the 20-page appendix of caveats, and the PTA MCMC documentation to supplementary material or a data-release note.

P3-M2. Genuine novelty fraction buried. The 17.8 % figure (top-1,000 DESI vs. 20 catalogs) is the only defensible discovery-rate number; the 58.8 % SIMBAD-unmatched aggregate is repeatedly presented without this qualification. Required fix: state the 17.8 % figure in the abstract and §IV A as the primary novelty metric.

P3-M3. Training-sample overlap not fully closed. The 5-fold Jaccard test is performed only on the 47 k training pool, not on the full 22.5 M catalog. The 100 k OOD test is truncated at 103 k spectra. Required fix: either complete a statistically meaningful OOD test or explicitly state that in-sample stability on the training pool is the limit of the robustness claim.

P3-M4. ACT DR6 appendix. The appendix is retained solely to document a failed cross-transfer scan. It adds no scientific content and should be removed; a one-sentence statement that ACT failed both gates is sufficient.

**MINOR findings**

P3-m1. Duplicate phrasing risk. No instances of “canonical canonical-mask” or similar were found, but the repeated “Path-C unique (primary)” / “Path-C unique∥” footnote language is unnecessarily duplicated across Table I and the text.

P3-m2. Page-number references in text. Several internal cross-references still use “§VI D item (i)” style that belongs in a review log, not final prose.

P3-m3. σ(fNL) envelope notation. The paper correctly discards the linear-extrapolation tail but continues to quote the superseded 8.27 ± 2.37 number “for historical reference.” Remove it.

**NIT findings**

P3-n1. Minor typographic inconsistencies in Table I footnotes (♡/♠ symbols appear without consistent definition on first use).

P3-n2. The 49-page length includes several one-sentence paragraphs that could be merged.

## Summary recommendation
**MAJOR REVISIONS**

The manuscript reports a large-scale engineering application of an existing autoencoder pipeline together with a native-retrain protocol that successfully mitigates two identified contamination modes. However, the central cosmological claim (multi-tracer fNL improvement) is statistically consistent with null once the empirical bias-enhancement measurement is inserted, the genuine novelty fraction is only 17.8 % at the highest-score stratum, and the paper is more than double the typical PRD length for this class of work. The abstract and headline numbers do not accurately reflect what the body rigorously proves. A major revision that (i) reduces length to ≤ 25 pages, (ii) removes all overstated novelty language, (iii) presents the fNL result strictly as an upper bound consistent with no improvement, and (iv) enforces uniform gate criteria or reclassifies failing surveys as exploratory would be required before the paper could be reconsidered.