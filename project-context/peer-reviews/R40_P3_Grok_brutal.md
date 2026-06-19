# P3 R40 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=4a8c1172 pages=30
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 144.2s

---

**Referee Report – P3 (Round R40)**

**Paper:** Spectrally Unusual Sources at Scale… (Golden, 2026 preprint)

**Journal target:** Physical Review D

I have examined every page, figure, table, equation, caption, and the abstract against the body text. The following findings are exhaustive.

### ESSENTIAL findings (paper cannot be accepted without fixes)

**P3-E1** Abstract (p. 1) vs. §V (pp. 17–18)  
Abstract states: “the de-biased point estimate returns the single-tracer baseline \(\sigma(f_{NL})^{\rm std}=8.98\) exactly (no multi-tracer improvement at current S/N)”. Body text in §V.A and Fig. 9 shows the central value drops from 8.98 to 8.14 (6.1 % improvement) when the empirical \(\alpha_{jk}=0.19\pm0.65\) is inserted. The abstract claim is factually false.  
**Required fix:** Rewrite abstract sentence to match the calibrated body statement exactly; add explicit caveat that the 6.1 % shift lies inside the 1\(\sigma\) envelope.

**P3-E2** Abstract (p. 1) vs. §III.D & Table I (pp. 5–6)  
Abstract headline number “378,280 Path-C unique anomalies” is the post-7-way deduplication count. Table I footnote ¶ and §III.D state that the 378,280 figure already excludes the 200 Planck patches and that the raw Path-C native-retrain total before deduplication is 388,493. The abstract therefore reports a derived, post-processed number as the primary result without stating the pre-deduplication input.  
**Required fix:** Abstract must quote the pre-deduplication survey-level total and state the exact deduplication radius and algorithm.

**P3-E3** §V.B (p. 18) & Appendix C  
The Fisher forecast is performed under a fixed-bias prior \(\alpha=0.15\) while simultaneously inserting the measured (data-driven) bias \(\alpha_{jk}=0.19\pm0.65\). No propagation of the uncertainty on \(\alpha_{jk}\) into the final \(\sigma(f_{NL})\) envelope is shown. The quoted 1\(\sigma\) envelope [3.92, 8.98] therefore under-states the true uncertainty.  
**Required fix:** Either (a) marginalize over the posterior of \(\alpha_{jk}\) or (b) label the quoted interval as conditional on the point estimate \(\alpha_{jk}=0.19\) and enlarge the envelope accordingly.

**P3-E4** §II.D & §III.H (pp. 4–5, 12)  
The Path-C “native retrain” protocol is described only by reference to six external JSON files and two GitHub scripts. No self-contained description of the precise training/validation split, early-stopping rule, or learning-rate schedule for the six independent retrains is given in the text. A standalone reader cannot reproduce the headline catalog without the companion repository.  
**Required fix:** Move the minimal reproducible specification (exact epoch counts, patience values, seed list, validation-loss thresholds) into the main text or a numbered appendix.

**P3-E5** Fig. 3 (p. 8) & §III.C  
The right-hand panel shows the SDSS native-retrain distribution extending to \(S\sim10^{11}\). The caption and text claim this is “not a like-for-like comparison” because of cross-transfer vs. native scale mismatch. No quantitative rescaling or Kolmogorov–Smirnov test between the two distributions is provided, rendering the visual comparison non-interpretable.  
**Required fix:** Either remove the panel or supply a properly normalized, scale-matched comparison with a statistical test.

### MAJOR findings

**P3-M1** §I (p. 2) – “largest-scale application … of which we are aware”  
No systematic literature search or quantitative comparison table against all published autoencoder anomaly searches (Liang et al. 2023, Nicolaou et al. 2024, etc.) is supplied. The claim is unsupported.

**P3-M2** Table I (p. 9) & §III.E  
eROSITA top-298 membership list is released solely as a ranked list ordered by an unreproducible IsolationForest raw-score axis (see §III.E). No column containing the actual per-object \(S_{\rm BigAE}\) value appears in the manifest. Users cannot reconstruct the ranking.

**P3-M3** §V.A (p. 17) – Landy–Szalay estimator  
The quoted jackknife error on \(\alpha_{jk}\) uses only 30 regions. No test of jackknife stability versus bootstrap or delete-d jackknife is shown; the error bar may be under-estimated.

**P3-M4** Length  
30 pages for a catalog + methods paper exceeds typical PRD limits for incremental methodology contributions. Recommended maximum: 18–20 pages including all appendices that contain load-bearing technical detail.

### MINOR findings

**P3-m1** Multiple instances of “Path-C” and “BigAE” introduced without an explicit acronym table on first use.  
**P3-m2** Fig. 2 (p. 7) uses Mollweide projection but does not state the precise coordinate epoch (ICRS assumed but not written).  
**P3-m3** Equation (2) normalizes by \(\sigma_{\rm val}\) computed on a 20 % validation split; the exact random seed for that split is not recorded.

### NITs (cosmetic)

- Future date “June 13, 2026” on title page.  
- Inconsistent use of “z” versus “redshift” in figure labels.  
- Several figure captions repeat the same methodological caveat already stated in the main text.

**Summary recommendation: MAJOR REVISIONS**

The manuscript contains multiple factual mismatches between abstract and body, relies on unreproducible external artifacts for its headline catalog, and presents a Fisher forecast whose uncertainty budget is incomplete. These are not cosmetic issues; they directly affect the primary scientific claims. A substantially revised version that (i) makes the abstract numerically faithful to the final calibrated results, (ii) supplies a self-contained methods appendix, and (iii) corrects the Fisher error propagation could be reconsidered, but the present draft does not meet PRD standards.