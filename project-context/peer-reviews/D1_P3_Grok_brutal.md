# P3 D1 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=62d7b294 pages=30
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 401.3s

---

**Referee Report**

**Paper:** Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies… (P3)

**Journal target:** Physical Review D

**Date of review:** based on rendered pages 1–25+

**Classification of findings**

**P3-E1 (ESSENTIAL, Abstract + §I, p. 1–2)**  
Abstract states “the largest-scale application of autoencoder anomaly detection across multiple astronomical archives of which we are aware” and quotes 378 280 / 269 317 headline numbers. Body never supplies a quantitative comparison table against the prior single-survey benchmark (Liang et al. 2023, 2 685 anomalies) or any other published multi-survey anomaly search. The claim is therefore unsupported. Required fix: either remove the superlative or insert a side-by-side table with literature numbers and identical selection criteria.

**P3-E2 (ESSENTIAL, Abstract + §V, p. 1 & 18)**  
Abstract and §V present a Fisher forecast \(\sigma(f_{NL})=8.14\) (1\(\sigma\) envelope [3.92, 8.98]) obtained after inserting the measured bias \(\alpha_{jk}=0.19\pm0.65\). The text simultaneously states “no multi-tracer improvement at current S/N”. These two statements are placed in immediate juxtaposition without the explicit qualifier required by PRD policy on multi-tracer forecasts. The abstract therefore over-states the result.

**P3-E3 (ESSENTIAL, §IIID + Table I footnotes, p. 5–9)**  
Three surveys (L AMOST, Gaia, eROSITA) fail the 5\(\sigma\) injection-recovery gate after native retraining; the paper nevertheless retains them in the “catalog-grade” tier after ad-hoc masking or percentile cuts. No quantitative demonstration is given that the retained objects are free of the same training-set artifact that caused the gate failure. This is a fatal validation gap.

**P3-E4 (ESSENTIAL, §IVB + Fig. 6, p. 14)**  
The 17.8 % “genuine novelty fraction” is derived from a single 1 000-object archival cross-match against 18 catalogs. The paper never shows that the same fraction is recovered when the identical exercise is repeated on a control sample of ordinary (non-anomaly) sources drawn from the same surveys. The number is therefore an upper bound on database incompleteness, not a discovery rate.

**P3-M1 (MAJOR, §II + §IIID, p. 3–5)**  
The entire Path-C “native-retrain” protocol is described only by reference to companion repository scripts and JSON logs. No equation or pseudocode for the six-step rebuild is supplied in the manuscript. A standalone reader cannot reproduce the catalog without external files.

**P3-M2 (MAJOR, Fig. 3 & 4, p. 8–11)**  
UMAP + HDBSCAN embeddings are shown for SDSS and DESI anomaly sets, yet no quantitative stability metric (adjusted Rand index across random seeds, trustworthiness, or silhouette score) is reported. Visual “cluster separation” is asserted without statistical support.

**P3-M3 (MAJOR, §VA, p. 18)**  
The NANOGRAV 15-yr KDE analysis yields \(\gamma=2.567\pm0.382\) and is compared with the matter-bounce prediction \(\gamma=3.0\). The Savage-Dickey Bayes factor is quoted only under a flat prior; the paper acknowledges the result is “prior-sensitive by construction” but still presents it as a “marginally consistent” test. This is an over-interpretation.

**P3-N1 (MINOR, throughout)**  
Dozens of internal repository paths, JSON filenames, and “committed at” timestamps appear in the text and footnotes. These are production artifacts, not scientific content, and should be moved to a reproducibility statement or removed.

**P3-N2 (MINOR, Table I, p. 9)**  
The table mixes three different selection thresholds (fixed \(S>5\), fixed-size continuity slice, top-298) without a single consistent column header. Readability is impaired.

**P3-NIT1 (NIT, p. 1)**  
Running header date “June 18, 2026” is a future placeholder; it should be removed or replaced by the actual submission date.

**Summary recommendation: REJECT**

The manuscript attempts to deliver both a 30-page methods paper and a 378 k-object catalog release in a single document. The validation chain contains multiple unclosed loops (failed injection-recovery gates, missing control-sample tests, reliance on unreproduced companion scripts). Cosmological forecasts are presented with internal contradictions that violate PRD standards on multi-tracer claims. The paper is also substantially longer than the incremental methodological advance it demonstrates. A focused, self-contained methods paper of \(\leq\)12 pages that rigorously closes the validation gaps, or a pure catalog data-release note, would be the appropriate format. In its current form the work does not meet the acceptance threshold of Physical Review D.