# P3 R35conf — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.99.pdf` md5=1e97ec59 pages=28
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 74.1s

---

**Referee Report**

**Paper**: Spectrally Unusual Sources at Scale... (BigAE anomaly catalog)

**Journal target**: Phys. Rev. D

**Recommendation**: REJECT

**P3-E1 (ESSENTIAL, p. 1)**  
Quote: “an earlier draft quoted 264,938/264,738 from headline-minus-LAMOST subtraction arithmetic”  
Internal draft-history language has no place in a submission. Required fix: delete every sentence containing “earlier draft,” “R-round,” “superseded,” or equivalent bookkeeping.

**P3-E2 (ESSENTIAL, p. 1 & p. 5)**  
Abstract states “378,280 Path-C Unique Anomalies” and “378,080 point-source + 200 Planck.” Body text gives 378,280, then 378,080 + 200 after 7-way deduplication, then 269,317 after further cuts. These numbers are not reconciled. Recompute the exact headline number from the final deduplication table and state it once, consistently, in both abstract and §III.

**P3-E3 (ESSENTIAL, throughout)**  
Hundreds of internal pipeline strings (“pipelines/p3_anomaly_engine/…”, “r24conf_…json”, “pod_runs/…”, “ext3_fm1_…”) appear in the main text and captions. A PRD paper must be self-contained; these belong only in a reproducibility manifest.

**P3-E4 (ESSENTIAL, §V & Fig. 9)**  
Single-tracer and multi-tracer \(\sigma(f_{NL})\) values (8.98 vs 8.14) are placed side-by-side without the explicit qualifier “not directly comparable” at every juxtaposition. The paper itself states the 9.4 % improvement is “a central-value forecast pending higher-S/N follow-up, not a detection.” This must appear in the abstract and every results paragraph.

**P3-E5 (ESSENTIAL, abstract vs §IV A)**  
Abstract claims “genuine novelty fraction of 178/1,000 ≈ 17.8 %.” Body correctly notes this is a single-sample point estimate against a heterogeneous set of 18 catalogs and that SIMBAD-unmatched fractions are database-coverage measures, not discovery rates. The abstract sentence is stronger than the calibrated body statement.

**P3-M1 (MAJOR, p. 1 & §I)**  
“largest-scale application … of which we are aware” is not supported by a systematic comparison table against all published autoencoder anomaly searches on comparable public archives. The 100× claim versus Liang et al. mixes full-stream vs science-target-only denominators.

**P3-M2 (MAJOR, §II B & Table I)**  
Per-survey anomaly thresholds are chosen by a mixture of fixed \(S>5\), top-percentile, and fixed-membership-list rules with no unified false-positive-rate calibration across surveys. The resulting catalog-grade tier therefore has survey-dependent purity; this must be quantified or the claim of a single “catalog-grade tier” withdrawn.

**P3-M3 (MAJOR, Fig. 7 & §IV B)**  
Spatial uniformity test reports \(\chi^2 = 376{,}713\) on 24{,}048 pixels but supplies no effect-size or practical-significance statement. The Poisson null is rejected, yet the paper concludes “no evidence for first-order Galactic latitude or dust correlation.” The two statements are not reconciled.

**P3-M4 (MAJOR, §V & Appendix C)**  
The Fisher forecast uses a fixed bias prior \(\alpha_{jk}=0.15\) that is superseded by the empirical measurement \(\alpha_{jk}=0.19\pm0.65\). The paper presents both numbers without a single preferred forecast; readers cannot know which value to adopt.

**P3-N1 (MINOR, multiple pages)**  
Repeated use of “Path-C” and “native retrain” as proper nouns without a one-sentence definition on first use.

**P3-N2 (MINOR, Table I caption)**  
“ACT DR6 is formally quarantined” appears only in a footnote; the same statement must be in the table header or main text.

**P3-NIT1–NIT4**  
Minor typographic issues (inconsistent use of en-dash vs hyphen in coordinate ranges, missing units on one axis label in Fig. 3 right panel, two instances of “canonical canonical,” stray footnote markers).

**Summary recommendation**  
REJECT

The manuscript contains multiple instances of internal draft language, unreconciled headline numbers, and an excessive volume of project-specific pipeline references that render it unsuitable for Physical Review D in its current form. Even after those cosmetic and archival problems are removed, the statistical calibration of the anomaly tier, the handling of cross-survey selection functions, and the over-statement of the \(f_{NL}\) forecast relative to the paper’s own caveats would still require a major re-analysis and rewrite. The work is closer to a catalog release note than a self-contained PRD methods paper.