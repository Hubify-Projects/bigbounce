# P3 R26conf — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.84.pdf` md5=2539e13c pages=25
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 124.6s

---

**Referee Report — P3 (BigBounce anomaly catalog)**

**P3-E1 (ESSENTIAL, p. 1, col. 1, ¶3)**  
Text: “an earlier draft quoted 264,938/264,738 from headline-minus-LAMOST subtraction arithmetic”.  
This is explicit version-history / internal-audit language inside the submitted manuscript. Required fix: delete every sentence containing “earlier draft”, “R26conf”, “superseded”, or similar bookkeeping.  

**P3-E2 (ESSENTIAL, throughout)**  
The manuscript is 25 pages (including 12 figures, 7 tables, 4 appendices). PRD methods/catalog papers of this type are expected to be ≤12–14 pages. The present length is driven by repetitive per-survey narrative and exhaustive gate-by-gate diagnostics that belong in a data-release paper or Zenodo supplement, not the primary journal article.  

**P3-E3 (ESSENTIAL, abstract + §V)**  
Abstract states a “central forecast \(\sigma(f_{\rm NL})=8.14\) with \(1\sigma\) envelope \([3.92,8.98]\)”. The body (§V, Fig. 9) shows this number is obtained only after (a) adopting a fixed \(\alpha=0.15\) prior that is not the maximum-likelihood value and (b) discarding the convex-mapping bias correction that would return the single-tracer baseline. The two numbers are therefore not directly comparable; the paper never states this qualification at every juxtaposition.  

**P3-E4 (ESSENTIAL, §II.D + Table I footnotes)**  
The headline 378,280 count is produced by a six-step “Path-C rebuild” whose final step is a 7-way 5″ deduplication whose completeness is asserted but never quantified against an external truth table. The 200 Planck patches are retained in the headline despite failing both native-retrain gates; they are later declared “quarantined” only in Appendix F. This is an inconsistent definition of the primary sample.  

**P3-M1 (MAJOR, §IV.A)**  
The claimed “genuine novelty fraction ∼17.8 %” is computed from a single 1,000-object CDS X-Match against 20 catalogs. No bootstrap or jackknife uncertainty on the false-match rate is reported, and the 5″ matching radius is never varied. The 17.8 % figure is therefore not reproducible from the information given.  

**P3-M2 (MAJOR, Fig. 3 right panel + §III.C)**  
The SDSS DR18 anomaly-score distribution is shown on a log–log scale spanning >10 orders of magnitude; the extreme tail (\(S>10^{10}\)) is attributed to “ultra-cool dwarfs”. No quantitative test (e.g., proper-motion or parallax cut) is supplied to demonstrate that these objects are not simply the cross-transfer failure mode the authors themselves diagnose on p. 3.  

**P3-M3 (MAJOR, §V.A)**  
The Landy–Szalay measurement on the 5,384 QSO-candidate subsample yields \(\alpha_{\rm jk}=0.19\pm0.65\). The paper presents this as “<1\(\sigma\) from null” while simultaneously using the same sample for a Fisher forecast that assumes the central value 0.19. The tension between the two statements is never reconciled.  

**P3-N1 (MINOR, Table I)**  
The eROSITA row uses a fixed top-298 selection whose numerical value (0.259) is not the 99th percentile of the production-run score distribution; the caption never states this.  

**P3-N2 (MINOR, Eq. 2)**  
The anomaly score is defined with a validation-set \(\mu_{\rm val},\sigma_{\rm val}\). No table lists these per-survey constants, preventing exact reproduction of any published \(S\) value.  

**P3-NIT1–NIT4**  
Minor axis-label omissions (Fig. 7 bottom-right), inconsistent use of “Path-C” vs. “native retrain”, one duplicated phrase (“canonical canonical-mask” in an earlier internal version that survived into footnote ♣), and the gratuitous “Dated: June 2026” line on the title page.

**Summary recommendation**  
**MAJOR REVISIONS**

The manuscript contains multiple internal-audit artifacts, an over-length presentation, and at least three load-bearing numerical claims whose derivation is either inconsistent or incompletely documented. Until the version-history language is excised, the sample definition is made unambiguous, the Fisher-forecast caveats are stated at every comparison, and the paper is condensed to a length appropriate for PRD, it does not meet the journal’s standards.