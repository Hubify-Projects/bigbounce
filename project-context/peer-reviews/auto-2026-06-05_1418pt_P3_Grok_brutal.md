# P3 auto-2026-06-05_1418pt — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 63.8s

---

**Referee Report**

**Paper:** Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Anomaly Detections… (PRD submission)

**Classification of findings**

**P3-E1 (ESSENTIAL, Abstract + §I, p.1)**  
The abstract states the catalog “should use the 378,080 point-source tier” for downstream analyses and that the 17.8 % genuine-novelty fraction is measured on the DESI top-1,000 stratum. The body (§IV A) shows this 17.8 % is obtained only after an extended CDS X-Match against 20 external catalogs; the raw SIMBAD-unmatched fraction is 58.8 %. The abstract therefore presents a post-hoc, catalog-dependent number as the headline discovery rate without the required qualification that it is not the blind rate. Required fix: rewrite abstract and §I to state the blind unmatched fraction first and the 17.8 % figure only with explicit “after archival cross-match” language.

**P3-E2 (ESSENTIAL, §V B, p.10)**  
The Fisher forecast \(\sigma(f_{NL})=8.14\) (with \(\alpha_{jk}=0.19\)) is placed beside the single-tracer baseline 8.98 and labeled a “7.9 % improvement.” The two numbers are obtained from different null procedures (multi-tracer vs. single-tracer) and are not accompanied by the mandatory statement that they are not directly comparable. This violates PRD standards on side-by-side \(\sigma\) values. Required fix: either recompute both on identical footing or insert the explicit qualifier at every juxtaposition.

**P3-E3 (ESSENTIAL, §II D + Table I footnotes, pp.2–7)**  
The Path-C “native retrain” protocol is presented as the canonical result, yet the text repeatedly states that the cross-transfer baseline (319 k objects) is retained “as a before/after diagnostic.” The reader cannot determine which numbers are the science result and which are merely diagnostic scaffolding. The 378,280 headline number mixes six native-retrain catalogs with one cross-transfer catalog (Planck). This is an internal bookkeeping inconsistency that must be removed.

**P3-M1 (MAJOR, §III F + Appendix F, pp.6,18)**  
ACT DR6 is formally quarantined because the cross-transfer checkpoint fails both gate criteria, yet the paper still reports a 200-patch Planck tier while simultaneously claiming the ACT scan “provides a sensitivity-check artifact.” The 200 Planck patches are therefore the only CMB contribution, and the entire CMB section rests on a single failed cross-instrument test. The cosmological-utility claim for CMB anomalies is unsupported.

**P3-M2 (MAJOR, §V A, p.10)**  
The NANOGRAV 15-yr KDE posterior \(\gamma=2.567\pm0.382\) is compared with the matter-bounce prediction \(\gamma=3.0\) and labeled “+1.13\(\sigma\) (marginally consistent).” The same paragraph states the SMBHB value \(\gamma=4.33\) is “strongly disfavored.” Both statements rely on the same KDE chain; the paper never shows the joint posterior or the Bayes factor between the two models. The claim that the catalog “tests” the matter-bounce scenario is therefore overstated.

**P3-M3 (MAJOR, Fig. 2 & §III C, p.5)**  
The SDSS DR18 anomaly-score distribution spans twelve orders of magnitude (\(S\sim10^{11}\)) and is dominated by M7–T2 dwarfs that lie completely outside the DESI training manifold. The paper acknowledges this is a domain-shift artifact yet still publishes the 77,905-object SDSS tier as part of the “Path-C unique” catalog. The tier should be flagged as exploratory or removed from the headline count.

**P3-M4 (MAJOR, §IV A, p.9)**  
The 17.8 % genuine-novelty fraction is derived from a single top-1,000 stratum of one survey (DESI). No bootstrap, jackknife, or survey-to-survey variance is reported. The number cannot be treated as a robust population statistic.

**P3-N1–N4 (MINOR/NIT)**  
- Future date “June 2026” in the byline.  
- Inconsistent use of “Path-C unique” vs. “Path-C native-retrained” throughout Table I footnotes.  
- Several axis labels in Fig. 1 omit units on the color bar.  
- Reference [11] (Liang et al.) is cited for a 2,685-object catalog; the factor “141×” in the abstract is only recovered after mixing point-source and map-patch counts—needs explicit footnote.

**Summary recommendation**  
**MAJOR REVISIONS**

The manuscript attempts three distinct papers (methods catalog, cross-survey validation, cosmological application) inside a single 20-page submission. The headline 378 k catalog mixes incompatible selection functions, the CMB section rests on a failed cross-instrument test, and the \(f_{NL}\) and NANOGRAV claims are presented with side-by-side \(\sigma\) values that are not demonstrably comparable. Until the catalog definition is unified, the CMB tier is either removed or properly justified, and the cosmological forecasts are recomputed on a single statistical footing, the paper does not meet PRD standards.