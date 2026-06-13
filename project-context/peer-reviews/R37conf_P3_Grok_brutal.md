# P3 R37conf — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.103.pdf` md5=566f7150 pages=29
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 82.4s

---

**Referee Report**

**Paper**: Spectrally Unusual Sources at Scale… (BigAE/Path-C anomaly catalog)

**Journal target**: Phys. Rev. D

**Date of review**: Round R37conf equivalent

I have examined every page, figure, table, equation, footnote, and caption in the rendered PDF. The following findings are exhaustive.

**P3-E1 (ESSENTIAL)**  
Section I (p. 2) and throughout: The manuscript contains >40 explicit internal pipeline paths (“pipelines/p3_anomaly_engine/…”, “r24conf_…json”, “training.log.json”, “gaia_expanded.py”, etc.). These are internal-audit artifacts, not journal content. Required fix: remove every such string; replace with descriptive prose only.

**P3-E2 (ESSENTIAL)**  
Abstract (p. 1) and §II D (p. 5): The entire analysis is built on a “Path-C native retrain” protocol whose definition, selection criteria, and validation splits are never given in self-contained form. The reader is repeatedly referred to an external “companion data repository.” This violates the standalone-reader requirement. Required fix: all load-bearing definitions must appear in the main text.

**P3-E3 (ESSENTIAL)**  
Abstract claim: “the largest-scale application of autoencoder anomaly detection across multiple astronomical archives of which we are aware.” No systematic literature comparison is supplied that justifies the superlative against Liang et al. (2023), Baron & Poznanski (2017), or any other published autoencoder survey. Required fix: either delete the claim or provide a quantitative table.

**P3-E4 (ESSENTIAL)**  
Abstract (p. 1) states a 9.4 % improvement in the single-tracer Fisher forecast. The body (§V, p. 17) shows that this number is obtained only after inserting the empirically measured bias \(\alpha_{jk}=0.19\pm0.65\). The abstract presents the 9.4 % figure without the accompanying caveat that the improvement is statistically consistent with zero at \(0.29\sigma\). This is abstract–body drift. Required fix: either remove the 9.4 % claim from the abstract or qualify it identically to the body.

**P3-E5 (ESSENTIAL)**  
Table I (p. 7) and footnotes: Multiple footnotes contain internal bookkeeping language (“Path-C native-retrained counts are the canonical results”, “cross-transfer counts are preserved as the before/after baseline”). These are not scientific footnotes. Required fix: delete.

**P3-E6 (ESSENTIAL)**  
§II C (p. 5) and §III F (p. 12): The Planck CMB tier is scored with a cross-transfer model whose validation loss is \(2.2\times10^4\) (fails both gates). The 200 patches are nevertheless retained in the headline catalog of 378 280 objects. The paper never demonstrates that these patches contribute any cosmological information once the native retrain is performed. Required fix: either remove the 200 patches from the primary catalog or prove their utility.

**P3-E7 (ESSENTIAL)**  
§V (p. 16–18): The multi-tracer \(f_{NL}\) forecast is presented as the principal cosmological result, yet the Fisher matrix is never validated against the actual survey geometry, fiber collisions, or redshift-dependent selection functions. The only systematics budget quoted is a 5 % fiber-assignment term. This is insufficient for a PRD cosmology claim. Required fix: full end-to-end Fisher validation or removal of the cosmological interpretation.

**P3-M1 (MAJOR)**  
The paper is 29 pages. The core methodological advance (native-retrain protocol + multi-survey deduplication) could be presented in ≤12 pages. The present length is dominated by internal pipeline logs and per-survey diagnostic tables that belong in a data-release paper, not a methods submission to PRD.

**P3-M2 (MAJOR)**  
Figure 3 (p. 9) and §III C: The SDSS anomaly-score distribution is shown on a log-log scale that extends to \(S\sim10^{11}\). No explanation is given for how an autoencoder trained on DESI spectra can produce reconstruction errors eleven orders of magnitude larger than the training distribution without numerical instability. Required fix: demonstrate numerical stability or truncate the axis.

**P3-M3 (MAJOR)**  
§IV A (p. 13): The claimed 17.8 % genuine-novelty fraction is a single-sample Wilson interval on 178/1000 objects. No bootstrap or jackknife uncertainty on the 18-catalog cross-match is supplied. Required fix: provide a proper uncertainty.

**P3-N1 (MINOR)**  
“(Dated: June 2026)” on the title page is chronologically impossible for a submission in 2025. Remove.

**P3-N2 (MINOR)**  
Multiple axis labels in Figs. 3, 7, 9 use inconsistent capitalization and missing units. Standardize.

**P3-N3 (NIT)**  
“BigAE” is never expanded on first use in the abstract or introduction.

**Summary recommendation**: REJECT

The manuscript is an internal project report that has been lightly reformatted rather than rewritten for journal publication. It fails the standalone-reader test on multiple essential points, contains extensive pipeline artifacts, and presents cosmological claims whose supporting systematics analysis is below PRD standards. Even after the essential fixes listed above, the paper would still require a complete rewrite and substantial shortening before it could be considered for Phys. Rev. D.