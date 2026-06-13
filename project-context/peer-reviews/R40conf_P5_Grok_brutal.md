# P5 R40conf — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/p5_desi_chirality.pdf` md5=e6ceb5ff pages=32
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 110.9s

---

**Referee Report: P5 (DESIVAST chirality–environment null test)**

**Journal:** Physical Review D  
**Manuscript length:** 32 pages (rendered)  
**Recommendation basis:** Full reading of all rendered pages, recomputation of all quoted \(\sigma\), \(p\), \(\Delta f_{\rm CW}\), and binomial quantities from displayed counts, cross-check of every abstract scalar against body tables/equations, audit of all 8 figures and 13 tables for internal consistency and caption–body agreement, verification that every load-bearing claim is traceable without companion papers.

### ESSENTIAL findings (paper cannot be accepted without fixes)

**P5-E1 (Abstract + §I, p. 3)**  
Abstract states “the CW fraction shows no environment dependence beyond the known Paper IV catalog-wide classifier-monopole systematic of \(\approx 0.26\) pp”. The monopole offset \(\Delta f_{\rm CW} = -0.0026\) is imported from an unpublished “Paper IV [3] (in preparation)”. No numerical derivation or table in the present manuscript reproduces this value from the 8 474 531-galaxy catalog. Required fix: either publish Paper IV first or recompute and tabulate the monopole inside this work with the exact same classifier weights.

**P5-E2 (throughout, e.g. pp. 2, 4, 5, 7, 15, 17, 21)**  
Repeated internal repository strings (“pipelines/p5_desi_chirality/…”, “outputs/23_unique_parent_rebuild.json”, “§VIII F”, “R40conf”, etc.) appear in the body text and footnotes. These are version-control / internal-audit artifacts. Required fix: remove every such string; replace with a public reproducibility archive (Zenodo DOI + frozen commit hash) whose directory structure is described in ordinary prose.

**P5-E3 (§V, Eq. 1 + Table III, p. 8)**  
\(\sigma_{\rm from\,half}\) values for the four V-Web classes are presented side-by-side with the catalog-wide monopole prediction without the explicit qualifier “not directly comparable across bins of different \(N\)” at every juxtaposition. The void bin (\(n=428\)) has \(\sigma_{\rm from\,half}=-0.68\) while the filament bin has \(-2.61\); the difference is entirely a \(\sqrt{N}\) counting-statistics effect. Required fix: add the qualifier in the table caption, every figure that plots these \(\sigma\) values, and the abstract.

**P5-E4 (Abstract + §VIII A, p. 16)**  
Abstract headline number \(n=56{,}981\), \(\Delta f_{\rm CW}=0.0007\) is the DESIVAST-anchored result. The body shows this number only after the V-Web secondary path is discarded; the primary V-Web result on the same 56 981 galaxies is never tabulated. The abstract therefore reports a secondary-path number as the headline. Required fix: either change the abstract to the V-Web number or move the DESIVAST result to a clearly labeled secondary section.

### MAJOR findings

**P5-M1 (entire manuscript)**  
32-page length for a null-result methods paper exceeds PRD norms for this class of result. Recommended maximum: 12–15 pages once internal pipeline language and Paper-IV dependencies are removed.

**P5-M2 (§III C + Table I, p. 4)**  
1″ matching radius is stated to be “conservative,” yet the 99th-percentile separation is 0.30″ and the median is 0.0066″. No test is shown that the 1″ choice does not admit a non-negligible fraction of chance superpositions at the faint end. Required fix: add a random-offset contamination estimate.

**P5-M3 (§VI A + Fig. 3, p. 9)**  
The void-bin result (\(n=428\)) is stated to be “dominated by counting noise.” The paper never quantifies how large a true environmental signal could hide inside that noise (i.e., the 95 % credible interval on an injected \(\Delta f_{\rm CW}\) that would still be consistent with the observed data). Required fix: add an explicit injection-recovery or power calculation.

**P5-M4 (§VIII E + Table XI, p. 19)**  
Sky-position stratification uses HEALPix NSIDE=16 (885 occupied pixels). The “0 maximal voids per pixel” bin contains 378 511 galaxies and returns \(\sigma=-4.75\). The caption claims this is “entirely in the sky regions where DESIVAST finds no maximal voids.” No explicit footprint mask is supplied; the claim is therefore not reproducible from the released tables.

### MINOR findings

**P5-m1 (§II, p. 3)**  
Citation to “Paper IV v1.0.166” is given with an arXiv placeholder that post-dates the present manuscript. Update required.

**P5-m2 (Fig. 2 caption, p. 6)**  
Pie-chart volume fractions are given to 0.1 % but the underlying \(N_{\rm grid}=256^3\) cell count is never stated in the caption. Minor consistency fix.

**P5-m3 (§V, p. 5)**  
Jeffreys Beta(1/2,1/2) prior is used for binomial credible intervals; the paper never states whether the same prior is used for the label-shuffle Monte-Carlo or only for the analytic intervals. Clarification required.

### NITs (cosmetic)

- Inconsistent use of “pp” vs “percentage points” in figure labels.  
- Several figure axis labels omit units on redshift or separation.  
- Duplicate phrase “the the” appears once (p. 12, column 2).

### Abstract-last drift sweep (pattern-045)
Re-reading the abstract after the body: the sentence “the headline result … shows no environment dependence beyond …” is stronger than the body’s final calibrated statement, which repeatedly qualifies the result as “consistent with the counting-statistics floor of the smallest bin” and “below the Bonferroni-5 threshold after look-elsewhere correction.” The abstract therefore overstates the strength of the null.

### Summary recommendation
**MAJOR REVISIONS**

The manuscript presents a technically careful null result, but it is not presently publishable in Physical Review D. The three ESSENTIAL items (unpublished Paper IV monopole, pervasive internal pipeline strings, and side-by-side \(\sigma\) values without comparability warnings) must be corrected before any further review. In addition, the 32-page length and lack of self-contained reproducibility archive make the paper unsuitable for PRD in its current form. A substantially shortened (≤15 page), fully self-contained revision that removes all internal-audit language and supplies the missing monopole derivation would be reconsiderable.