# P3 R40conf — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/paper3_anomaly_catalog.pdf` md5=d1258558 pages=29
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 117.0s

---

**Referee Report – Physical Review D**

**Paper:** Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies… (Houston Golden, dated June 13, 2026)

**Finding P3-E1 (ESSENTIAL)**  
Section: Title + abstract (p. 1)  
Problem: Title and abstract headline the number 378,280 as the primary catalog size, yet the body (Table I, p. 6 and footnote ¶) states that this figure is obtained only after a 7-way 5″ deduplication performed on an internal “Path-C” pipeline whose code and intermediate products are not supplied. The cross-transfer baseline (319,443) is the only number that can be recomputed from the per-survey columns without external artifacts.  
Required fix: Replace headline number with the fully reproducible cross-transfer count or supply a frozen, self-contained manifest that allows exact recomputation of the 378,280 figure from public data releases.

**Finding P3-E2 (ESSENTIAL)**  
Section: Abstract (p. 1) + §V (p. 17–18)  
Problem: Abstract states “a central 9.4 % improvement” on \(\sigma(f_{\rm NL})\). The body (§V, p. 18) shows this improvement appears only under the fixed-bias-prior assumption \(\alpha=0.15\); the empirically measured bias \(\alpha_{jk}=0.19\pm0.65\) yields zero improvement (0.29\(\sigma\)). The abstract claim is therefore stronger than, and ordered differently from, the final calibrated body statement.  
Required fix: Rewrite abstract sentence to match the body’s final statement that the multi-tracer gain is statistically consistent with zero at current S/N.

**Finding P3-E3 (ESSENTIAL)**  
Section: Abstract + §I (p. 2) + §VI (p. 19)  
Problem: Paper repeatedly calls the work “the largest-scale application of autoencoder anomaly detection across multiple astronomical archives of which we are aware.” No quantitative comparison table or citation to the actual scale of Liang et al. (2023), Baron & Poznanski (2017), or other published autoencoder searches is supplied. The claim is therefore unsupported.  
Required fix: Either remove the superlative or provide a side-by-side table of survey sizes, model parameter counts, and anomaly yields against all cited prior works.

**Finding P3-E4 (ESSENTIAL)**  
Section: §II D (p. 5) and every per-survey subsection  
Problem: All headline anomaly counts after native retraining rest on six ad-hoc “gate” criteria (val-loss, injection-recovery, Jaccard, etc.) whose numerical thresholds are chosen after inspection of the same data. No pre-registered analysis plan or blinded threshold selection is documented.  
Required fix: Either pre-register the gate thresholds or downgrade all catalog-grade counts to exploratory.

**Finding P3-E5 (ESSENTIAL)**  
Section: §III D (p. 9) + Fig. 3 (p. 10)  
Problem: The LAMOST anomaly distribution is shown on a different native-retrain scale from DESI; the paper states the two \(S\) axes “are not directly comparable.” Yet the abstract and Table I headline both surveys together without repeating this caveat at every juxtaposition.  
Required fix: Add the explicit qualifier “not directly comparable” to every figure, table row, and abstract sentence that places DESI and LAMOST \(S\) values side-by-side.

**Finding P3-M1 (MAJOR)**  
Section: Data Availability paragraph (p. 22)  
Problem: The reproducibility claim rests on “pipelines/p3_anomaly_engine/…” paths and a companion repository whose commit hashes pre-date the stated paper version and whose 20-feature Gaia preprocessing script was “not recovered.” No frozen DOI or exact release tag is supplied.  
Required fix: Provide a single, version-stamped tarball or Zenodo DOI containing every script, seed, and mask used to produce the numbers in Table I.

**Finding P3-M2 (MAJOR)**  
Section: §V A (p. 18) + Fig. 9 (p. 19)  
Problem: The Fisher forecast improvement is shown only for the 7-bin binned case under a fixed \(\alpha=0.15\). No unbinned or full-covariance forecast is presented, nor is the degradation under the empirically measured \(\alpha_{jk}\) uncertainty propagated.  
Required fix: Supply the full unbinned Fisher matrix and the degradation curve versus \(\alpha\) uncertainty.

**Finding P3-M3 (MAJOR)**  
Section: §IV B (p. 14) + Fig. 7 (p. 16)  
Problem: The spatial uniformity test yields \(\chi^2=15.7\) (24 048 pixels). The paper attributes the entire excess to footprint geometry but supplies neither a survey-selection-function map nor a quantitative model of the expected \(\chi^2\) under realistic target selection.  
Required fix: Provide a forward-modelled selection function and the corresponding null \(\chi^2\) distribution.

**Finding P3-N1 (MINOR)**  
Section: Title page  
Problem: Submission date “June 13, 2026” is in the future.  
Required fix: Correct to actual submission date.

**Finding P3-N2 (MINOR)**  
Section: Throughout (e.g., p. 3, 5, 6)  
Problem: Internal pipeline paths (“pipelines/p3_anomaly_engine/…”) and project codenames (“Path-C”) appear in the main text.  
Required fix: Move all such strings to footnotes or an appendix.

**Finding P3-N3 (NIT)**  
Section: Fig. 1 caption (p. 3)  
Problem: Caption states “83 Exemplar-Set anomalies” but the figure itself is not shown in the supplied render; the numerical claim cannot be visually audited.  
Required fix: Ensure every figure referenced in a caption is present and legible.

**Summary recommendation**  
REJECT

The manuscript presents an interesting large-scale catalog but fails multiple PRD standards on first read: headline numbers rest on unreproducible internal pipelines, the abstract contains claims stronger than the final calibrated body statements, superlatives are unsupported, gate thresholds are post-hoc, and the cosmological application rests on a 0.29\(\sigma\) “improvement” that disappears under the measured bias. These are not cosmetic issues; they are foundational to the paper’s central claims. A major re-write that removes all non-reproducible numbers, aligns every abstract sentence with the body’s final caveats, and supplies a self-contained reproducibility package would be required before the work could be considered for Physical Review D.