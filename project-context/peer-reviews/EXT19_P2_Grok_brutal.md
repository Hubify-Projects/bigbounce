# P2 EXT19 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf` md5=dbcc5834 pages=29
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 76.8s

---

**Referee Report**

**Paper:** Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook (Houston Golden)

**Journal:** Physical Review D

**Findings**

**P2-E1 (ESSENTIAL, Abstract + Sec. IV, p. 1 and p. 9)**  
Abstract states “5.2–5.5σ optimistic and 2.6–5σ realistic” and “BF ≈ 9 … up to BF ≈ 14”. These headline numbers are not accompanied by an explicit pointer to Table IV (the only place the full systematic budget is assembled). A standalone reader cannot recompute the quoted intervals from the abstract alone. Required fix: add one-sentence cross-reference in the abstract (“see Table IV and Sec. VII for the systematic budget that produces these ranges”).

**P2-E2 (ESSENTIAL, Sec. VI + Table II, pp. 12–14)**  
Bayes factors are reported for four different prior widths and two different competitor priors without a single, prominent statement that “these BF values are prior-dependent and not directly comparable across rows.” The abstract repeats the BF ≈ 9–14 range. This violates the rule that sigma/BF headlines appearing side-by-side must carry an explicit non-comparability qualifier at every juxtaposition. Required fix: add the qualifier in both abstract and Table II caption; recompute and label the “recommended” row consistently.

**P2-M1 (MAJOR, entire manuscript length)**  
The paper is 25 pages. The genuinely new technical content (null-space SVD of the degree-9 polynomial, shape-cosine stability test, and the closed-form Bayes-factor derivation) occupies roughly 6–7 pages. The remainder is exhaustive re-derivation of Cai et al. (2010), literature review, and multiple Monte-Carlo cross-checks that could be archived as supplementary material. PRD does not have a strict length limit, but a forecast recast of this type is expected to fit in ≤ 12–14 pages. Required fix: condense to a 12-page core paper + supplementary archive.

**P2-M2 (MAJOR, Sec. II.B + Fig. 1, p. 4)**  
The under-determination claim (rank-3 null space) is demonstrated only for the three benchmark triangles. No test is shown that the same three constraints remain sufficient when the triangle grid is refined to 200 bins per side (the convergence test mentioned in passing). Required fix: add one panel or table entry confirming that the SVD singular values stabilize at the finer grid.

**P2-M3 (MAJOR, Sec. VII + Table IV, p. 20)**  
The “all-combined 2.6σ” floor is obtained by adding four systematics in quadrature after the template-overlap correction. The paper never demonstrates that these four contributions are statistically independent; the text acknowledges possible correlations (“correlations between systematics can tighten or loosen”). The quoted 2.6σ is therefore an optimistic bound, not a conservative one. Required fix: either propagate a covariance matrix or relabel the number as “illustrative lower bound under the assumption of uncorrelated systematics.”

**P2-N1 (MINOR, Sec. III.B, p. 8)**  
Equation (6) gives r = 0.84 ± 0.02. The ±0.02 is the standard deviation of the 10 000-sample distribution, not a standard error on the mean. The text never states which quantity is being reported. Required fix: clarify “standard deviation across coefficient draws.”

**P2-N2 (MINOR, multiple locations)**  
The phrase “noise-weighted central value r ≈ 0.84” appears repeatedly. The weighting scheme is defined only in the caption of Table IV and in the code repository. A reader who does not download the code cannot reproduce the exact numerical weight. Required fix: one-sentence definition in the main text.

**P2-NIT1 (NIT)**  
Figure 3 caption states “SPHEREx 1σ error bar shown in blue” but the plotted bar is actually the 1σ interval on f_NL after the full systematic budget; the label is therefore slightly misleading.

**P2-NIT2 (NIT)**  
The date in the byline is “June 14, 2026.” This is a future date relative to any plausible submission; it should be removed or changed to “submitted” date.

**Summary recommendation**  
**MAJOR REVISIONS**

The manuscript contains several technically solid calculations, but the combination of (i) an over-long presentation, (ii) headline σ and BF numbers in the abstract that cannot be recomputed without the full systematic table and prior caveats, and (iii) an incompletely qualified prior dependence in the Bayesian section means the paper does not yet meet PRD’s standards for clarity and reproducibility on first read. A substantially shortened version that foregrounds the new null-space and Bayes-factor results, with explicit qualifiers on every quoted significance, would be suitable for resubmission.