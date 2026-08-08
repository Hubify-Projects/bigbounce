# P4 DP4-E2E-RETEST-v1.0.238 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/site/public/papers/chirality_catalog_paper.pdf` md5=03f03e2a pages=35
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 142.7s

---

**Referee Report – PRD**

**Paper:** “A Null Chirality Dipole in 8.5 Million DESI Galaxies from Equivariant Deep Learning”  
**ID:** P4

### ESSENTIAL findings (must be fixed or paper is unpublishable)

**P4-E1 (Abstract + §I, p. 1)**  
Abstract states “8.5 Million DESI Galaxies” and “yielding \(N_{\rm spiral}=3{,}201{,}160\) spirals”. Body text (p. 6, Table II) gives exactly 8,474,531 galaxies after QA and 3,201,160 spirals. The rounded title/abstract figure is not reproduced from the displayed numbers; the precise figure is 8.47 M.  
*Fix:* Replace every occurrence of the rounded “8.5 Million” with the exact QA’d number that appears in the tables.

**P4-E2 (Table II + Table I, pp. 6–7)**  
Nine distinct \(\sigma\) or \(z\) values from non-equivalent nulls (pixel-permutation, label-shuffle, block-bootstrap, MASTER \(\ell=1\), monopole-only, hemisphere LEE, injection-recovery) are placed in adjacent rows/columns. The parenthetical “not directly comparable” appears only once in the caption. Instruction 7 requires the qualifier at every juxtaposition.  
*Fix:* Insert the explicit qualifier on every row that reports a different null family, or move all non-primary estimators to a separate “systematics diagnostics” table.

**P4-E3 (Abstract, p. 1)**  
Abstract claims the real-space dipole is “consistent with null” at “+0.41\(\sigma\) (\(p=0.31\))”. This number is computed only on the \(p_{\rm eq}>0.6\) subsample (\(N=949{,}584\)). The same paragraph simultaneously cites the block-bootstrap WLS result on the full Catalog C (\(N=3.2\) M). The two numbers are not the same estimator on the same sample. The abstract therefore reports a stronger claim than the body’s final calibrated statement.  
*Fix:* Abstract must state the precise sample and null used for the headline +0.41\(\sigma\) figure and must not juxtapose it with the full-catalog WLS result.

**P4-E4 (§IV C, p. 9–10; Fig. 4)**  
The per-pixel \(A_p\) map and the real-space dipole fit both use the canonical mask \(N_{\rm spiral}(p)\ge10\). The text never states whether the quoted +0.41\(\sigma\) changes when the mask threshold is varied by \(\pm1\) pixel. This is a load-bearing robustness test that is missing.

### MAJOR findings

**P4-M1 (Overall length)**  
35-page manuscript (metadata) presenting a single null result. PRD standards for a methods/null-result paper of this type are ~18–22 pages including appendices. The present length is driven by eight-anchor systematics tables and repeated provenance strings rather than new physics.

**P4-M2 (§II B, p. 2)**  
66.5 % of training labels are CE-ResNet pseudo-labels. The GZ1 cross-match is performed only on the final catalog, not on the training split itself. The paper therefore cannot demonstrate that the dominant training source is free of the very survey systematics it later claims to have removed.

**P4-M3 (Fig. 7, p. 13)**  
Left panel (Catalog A) shows a visually obvious dipole; right panel (Catalog C) does not. The caption states the difference is “a 2\(\sigma\) ‘detection’ vs clean null”. No quantitative test of the visual impression (e.g., dipole amplitude on the raw single-pass map) is supplied.

**P4-M4 (Table VIII, p. 21)**  
Injection-recovery thresholds \(A_{50}\approx0.75\%\), \(A_{95}\in(1.0\%,1.5\%)\) are quoted only for the \(\theta\)-uniform draw. The area-uniform draw (primary convention) yields different numbers (text on p. 20). The table does not state which convention is used.

### MINOR findings

**P4-m1** Duplicate phrase “canonical canonical-mask” appears in the running text (p. 12).  
**P4-m2** Multiple figure captions contain the internal path string “pipelines/p2_chirality/…” (Figs. 2, 4, 7). These should be moved to a reproducibility footnote.  
**P4-m3** Equation (3) defines \(A_p\) but the text repeatedly writes “\(A=2(f_{\rm CW}-1/2)\)” without re-stating the per-pixel subscript, creating an ambiguous notation.

### NITs
- Title uses “8.5 Million” while every table uses 8,474,531.  
- Several axis labels in Fig. 8 omit units on the power-spectrum panel.  
- Reference list contains one arXiv ID that post-dates the stated submission date (internal bookkeeping).

## Summary recommendation
**REJECT**

The manuscript contains at least four ESSENTIAL violations of PRD standards: (1) headline numbers in the abstract that are not reproduced from the body on the identical sample+null combination, (2) multiple non-equivalent \(\sigma\) values placed side-by-side without the required comparability qualifier at every instance, (3) an untested mask-threshold robustness check on the primary result, and (4) a 35-page length driven by internal provenance strings rather than physics. These are not cosmetic; they directly affect whether a reader can trust the central claim that a “clean 1.7 % dipole is disfavored.” The paper must be shortened by a factor of ~1.6 and the statistical presentation made unambiguous before resubmission.