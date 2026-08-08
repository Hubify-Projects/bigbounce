# P4 R40 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p2_chirality/chirality_catalog_paper.pdf` md5=c47abc18 pages=23
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 146.3s

---

**Referee Report – P4 (PRD)**

**P4-E1**  
**Abstract (p. 1) + Sec. IV C (p. 7)**  
The abstract states the primary result as “+0.41σ (moment-z … p = 0.31, 10⁴ isotropic-bootstrap realizations)” while immediately juxtaposing it with “z = 0.70 (per-galaxy label-shuffle null)”. These two σ values are produced by wholly different null constructions and are not numerically commensurate. The abstract contains no explicit “not directly comparable” qualifier at the point of juxtaposition.  
**Required fix:** Insert the explicit qualifier in the abstract sentence itself (and at every subsequent side-by-side listing of distinct-null σ values).  

**P4-E2**  
**Abstract (p. 1)**  
Abstract claims “the largest chirality-labeled galaxy catalog to date: 8,474,531”. Body (p. 5) confirms the number after quality cuts, but no literature comparison table or citation demonstrates that every prior published catalog is smaller once identical selection criteria are applied. Unsupported superlative.  
**Required fix:** Either remove “largest” or supply a one-column comparison table with explicit selection functions.  

**P4-E3**  
**Abstract (p. 1) + Sec. IV D (p. 9)**  
Abstract asserts the MASTER ℓ = 1 residual is “+3.64σ”. Table III (p. 11) shows this value only for the canonical unapodized mask under the 10⁴-permutation null; the apodized value is +7.31σ. The abstract therefore reports the smaller of two non-interchangeable numbers without stating which mask or which null.  
**Required fix:** Quote the exact mask + null combination used for the headline number.  

**P4-E4**  
**Sec. III A (p. 3) + Table I (p. 5)**  
Table I caption states “the σ values … are not directly comparable across rows”. Yet rows (i) and (iii) are placed immediately adjacent with no repeated qualifier in the table itself. Violates the “at every juxtaposition” rule.  
**Required fix:** Add the qualifier to every table/figure that lists multiple null procedures.  

**P4-M1**  
**Abstract (p. 1) + Sec. VI A (p. 12)**  
Abstract gives the 50 %-recovery threshold as A₅₀ ≈ 0.75 %. Body text (p. 13) shows this number is obtained only on the HC-broad subsample (N = 949 584) under per-pixel-shuffle nulls; the full-sample Fisher floor is 0.29 %. The abstract therefore quotes the more conservative number without the sample-size caveat.  
**Required fix:** State the exact subsample and null procedure in the abstract sentence.  

**P4-M2**  
**Fig. 4 (p. 8) + Sec. IV C (p. 7)**  
Color scale of the Mollweide map is labeled in units of (N_CW – N_CCW)/(N_CW + N_CCW) but the caption claims the map shows A_p. These are numerically identical only after multiplication by 2; the figure therefore mislabels its own color bar.  
**Required fix:** Correct axis label or rescale the map.  

**P4-M3**  
**Sec. II B (p. 2) + Appendix B (p. 17)**  
Training set contains 66.5 % CE-ResNet pseudo-labels. The independent GZ1 cross-match accuracy is quoted as 69.91 % (Cohen’s κ = 0.40). No propagation of this label-noise floor into the final dipole uncertainty is performed.  
**Required fix:** Add a quantitative label-noise systematic budget.  

**P4-M4**  
**Sec. IV D (p. 9) + Table IV (p. 11)**  
The monopole-only generative null reproduces 99.32 % of the pre-MASTER power. The post-MASTER residual is therefore attributed to “non-primary systematics”. No numerical test shows that the residual cannot be produced by a 0.68 % residual monopole leakage after MASTER.  
**Required fix:** Supply the leakage tolerance calculation.  

**P4-N1**  
**p. 1 (title page)**  
“(Dated: June 13, 2026)” is a future date. Cosmetic but inconsistent with a live submission.  

**P4-N2**  
**Multiple locations**  
Repeated phrase “not directly comparable as detection significances; they are diagnostic indicators only” appears verbatim at least four times. Minor stylistic redundancy.  

**P4-N3**  
**Fig. 9 caption (p. 15)**  
States “obs. σ ≈ 7.28” while the plotted point is the canonical +7.28σ value already shown in Table III. Redundant annotation.  

**Summary recommendation**  
**MAJOR REVISIONS**

The manuscript presents a technically elaborate null-result analysis whose central claim (a sub-percent real-space dipole consistent with systematics) is only as strong as the reader’s ability to compare the heterogeneous null ensembles. The repeated failure to qualify every numerical juxtaposition of distinct null procedures, the unsupported “largest catalog” claim, the unlabeled color-bar mismatch in Fig. 4, and the missing label-noise propagation constitute essential or major obstacles to acceptance in PRD. A revised manuscript that (i) inserts the required qualifiers at every numerical comparison, (ii) supplies the missing literature-size table and label-noise budget, and (iii) corrects the figure label would be re-reviewable; in its present form the paper does not meet PRD standards for unambiguous statistical reporting.