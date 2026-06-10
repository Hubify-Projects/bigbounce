# P3 R27conf — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.86.pdf` md5=31284b90 pages=26
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 80.3s

---

**Referee Report**

**Paper:** Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies… (arXiv preprint, June 2026)

**Journal:** Physical Review D

**Classification of findings**

**P3-E1 (ESSENTIAL)**  
Section I, p. 1 (first paragraph after abstract): “an earlier draft quoted 264,938/264,738 from headline-minus-LAMOST subtraction arithmetic”  
This is explicit version-history / internal-audit language that has no place in a submitted manuscript. Required fix: delete the sentence entirely and any similar phrases (“earlier draft”, “R27conf”, round tags, etc.).

**P3-E2 (ESSENTIAL)**  
Abstract, p. 1 and §V, p. 14–15: The multi-tracer Fisher improvement is presented as “9.4 %” (8.14 vs 8.98) while the text simultaneously states it is “exactly (no improvement)” and “not a detection” at <1σ. The abstract must not highlight a central-value shift that the body explicitly disclaims as statistically meaningless. Required fix: remove the 9.4 % figure from the abstract or qualify it with the same “<1σ, no improvement” language used in the body.

**P3-M1 (MAJOR)**  
Abstract length and content. The abstract is ~650 words and functions as a second executive summary rather than a concise statement of what is proved. PRD abstracts are expected to be ~150–250 words. Required fix: condense to the core result (catalog size, method, one headline novelty fraction with CI, and the explicit statement that no cosmological detection is claimed).

**P3-M2 (MAJOR)**  
§II and §III together occupy ~12 pages of per-survey engineering detail (native-retrain logs, exact patience settings, 5-fold Jaccard numbers, injection-recovery tables). This level of pipeline bookkeeping belongs in a companion data-release paper or repository, not the primary PRD article. Recommended maximum length for the methods/results core: 12–14 pages.

**P3-M3 (MAJOR)**  
Figure 3 (right panel) and §III C: The SDSS DR18 score distribution is shown on a log–log scale that extends to S ~ 10^11. The caption and text correctly note this is a cross-transfer artifact, yet the figure is still presented as a primary result. The visual impression of a 10-order-of-magnitude tail is misleading without a side-by-side native-retrain panel. Required fix: either remove the panel or add an explicit “cross-transfer only; native retrain cuts tail at S < 14” inset.

**P3-N1 (MINOR)**  
Table I footnote † and the Path-C vs cross-transfer distinction are defined only after the table. Move the definition to the table caption or the first sentence of §III.

**P3-N2 (MINOR)**  
Several axis labels in Figs. 1, 3, 7 use “Anomaly Score S” without reminding the reader on every panel that S is the per-survey z-scored MSE (Eq. 2). Add a one-line reminder in the caption of each multi-panel figure.

**P3-NIT1 (NIT)**  
Minor typographic: “Path-C” is inconsistently hyphenated in a few places; standardize.

**Summary recommendation: MAJOR REVISIONS**

The manuscript contains at least two clear violations of submission standards (internal draft language and an abstract that advertises a result the body disclaims). In addition, the paper is substantially over-length for the incremental methodological advance it actually demonstrates. Once the internal-audit text is removed, the abstract is rewritten to match the body’s conservative conclusions, and the pipeline-log sections are moved to supplementary material or a data-release note, the work could be reconsidered as a catalog/data-release paper. In its present form it does not meet PRD standards.