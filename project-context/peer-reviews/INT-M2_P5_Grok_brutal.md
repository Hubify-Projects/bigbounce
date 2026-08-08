# P5 INT-M2 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf` md5=503d4e5b pages=34
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 116.8s

---

**Referee Report – Physical Review D**

**Paper:** Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across the DR1 Matched-Spiral Sample (P5)

**Finding P5-E1 (ESSENTIAL)**  
Section: Abstract / first paragraph (p. 1)  
Problem: “the primary designation is declared post-hoc — no single a priori preregistered plan was filed.” The headline void-vs-non-void \(\Delta f_{\rm CW}\) result is then presented as the primary result.  
Required fix: Remove all language claiming a “primary” result or relegate the entire DESIVAST-anchored analysis to an explicitly exploratory section. No statistical claim may be labeled “primary” after the data are examined.

**Finding P5-E2 (ESSENTIAL)**  
Section: I (Introduction) and throughout (pp. 3–4 and later)  
Problem: The paper is not standalone. Every load-bearing number (\(f_{\rm CW}^{P5}=0.49719\), \(\Delta f_{\rm CW}^{P4}=-0.0026\), classifier architecture, monopole offset, etc.) is imported from “Paper IV [3] (in preparation)”. No reader can verify the central claims without an unpublished manuscript.  
Required fix: All quantitative inputs, the full classifier description, and the derivation of the monopole must be reproduced in the present manuscript (or the paper must be withdrawn until Paper IV is public and citable).

**Finding P5-E3 (ESSENTIAL)**  
Section: Abstract + Table IV (p. 9)  
Problem: The abstract states a “null” environmental result. The only void bin has \(n=428\) galaxies; the reported \(\sigma_{\rm from\,half}=-0.68\) lies well inside the \(2\sigma\) counting floor for that bin size. The paper never states the minimum detectable \(|\Delta f_{\rm CW}|\) at the adopted power.  
Required fix: Add an explicit power calculation showing the smallest \(|\Delta f_{\rm CW}|\) that could have been detected at 95 % power in the void bin; if that threshold exceeds the observed offset, the “null” claim must be withdrawn.

**Finding P5-M1 (MAJOR)**  
Section: V (Statistical Methods) and Table III (p. 8)  
Problem: Multiple families of tests (Bonferroni-5 primary, Bonferroni-9 Phase-2, descriptive) are presented side-by-side with \(\sigma\) values that are not directly comparable because the reference null and the effective \(N\) differ. No warning appears at every juxtaposition.  
Required fix: Every table and figure that mixes families must carry an explicit footnote: “\(\sigma\) values from different null constructions are not numerically comparable.”

**Finding P5-M2 (MAJOR)**  
Section: VIII (DESIVAST cross-validation) and Table XI (p. 20)  
Problem: The three DESIVAST algorithms return \(\Delta f_{\rm CW}\) values whose signs and magnitudes differ; the paper treats all three as supporting the same null. The largest \(|z_\Delta|\) is only 1.12. No effect-size or practical-significance statement accompanies the \(\chi^2\) homogeneity test.  
Required fix: Report Cramér’s \(V\) (or equivalent) for every multi-row contingency table and state the minimum detectable difference given the observed sample sizes.

**Finding P5-M3 (MAJOR)**  
Section: Abstract + §VI.A (headline result)  
Problem: The abstract claims “no environmental dependence.” The controlling statistic is a single bin (\(n=428\)) whose counting noise alone produces \(\sigma_{\rm from\,half}\approx0.68\). The paper never demonstrates that the result survives replacement of the T-Web void label by a pure random label at the same volume fraction.  
Required fix: Add a control test that assigns the same number of galaxies to “void” at random and recomputes the full analysis chain.

**Finding P5-N1 (MINOR)**  
Section: Multiple figure captions (e.g., Fig. 3, Fig. 5)  
Problem: Axis labels omit units on several derived quantities (e.g., “\(\sigma_{\rm from\,half}\)” without explicit statement that it is in units of the binomial standard deviation).  
Required fix: Add “(binomial \(\sigma\) units)” to every such axis.

**Finding P5-N2 (NIT)**  
Section: Throughout  
Problem: Repeated use of the phrase “Paper IV global \(f_{\rm CW}\)" without a one-sentence reminder of its numerical value on first use in each section.  
Required fix: Insert the numerical value at first mention in each major section.

**Finding P5-E4 (ESSENTIAL)**  
Section: Data Availability / reproducibility statements (scattered)  
Problem: No frozen release hash, DOI, or exact commit of the DESIVAST catalog, T-Web grid files, or matched-spiral catalog is provided. The text refers to “the companion data repository” without a persistent identifier.  
Required fix: Supply a citable DOI or Zenodo record containing the exact files used for every number in Tables IV, VIII, XI, and XIII.

**Finding P5-M4 (MAJOR)**  
Section: Abstract claim vs. body (p. 1 vs. §VIII)  
Problem: The abstract states the result is “robust across all five DESIVAST void-finders.” The actual comparison uses only three algorithms on the same parent catalog; two additional “catalog-native” estimators are shown only in supplementary tables. The abstract claim is stronger than the calibrated body statement.  
Required fix: Rewrite the abstract sentence to match the exact scope demonstrated in §VIII.

**Finding P5-E5 (ESSENTIAL)**  
Section: §II and §V (relation to Paper IV)  
Problem: The entire environmental-independence conclusion rests on the assumption that the Paper IV monopole offset is a pure classifier bias with no spatial variation. No test of that assumption (e.g., a position-dependent monopole map) is performed inside the present work.  
Required fix: Either perform the test or remove every sentence asserting that the observed residuals are “entirely” explained by the global monopole.

**Summary recommendation**  
**MAJOR REVISIONS**

The manuscript contains multiple fatal statistical and reproducibility defects (post-hoc primary designation, non-standalone reliance on an unpublished companion, under-powered void bin treated as a null result, missing effect-size statements, and absent persistent data identifiers). These cannot be repaired by minor editing. A substantially revised version that (i) removes all post-hoc “primary” language, (ii) reproduces every load-bearing number from Paper IV, (iii) supplies a proper power analysis for the \(n=428\) void bin, and (iv) provides citable data releases could be reconsidered, but the present draft does not meet Physical Review D standards.