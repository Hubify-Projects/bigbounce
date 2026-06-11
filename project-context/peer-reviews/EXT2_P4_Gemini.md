# EXT2 P4 — Gemini in-thread delta review
**Provider**: gemini.google.com · 3.5 Thinking
**Chat**: https://gemini.google.com/app/8340abb820aada09
**PDF**: chirality_catalog_paper_v173.pdf · **Harvested**: 2026-06-10 ~21:30 PDT
**Mode**: same-thread re-review (closure verification + fresh pass + updated verdict)

---

Show code
Gemini said
Referee Report

Journal: Monthly Notices of the Royal Astronomical Society (MNRAS)

Manuscript Title: Survey-Scale Galaxy Chirality with Equivariant TTA: A Null Real-Space Chirality Dipole, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)

Author: Houston Golden (Independent Researcher)

Manuscript Version: v1.0.173 (June 10, 2026)   
PDF

1. Closure Verification

Following a thorough truth-audit of the revised manuscript (v1.0.173), the status of the major and minor issues raised in the previous evaluation is detailed below:

Block-Bootstrap Scale Selection (NSIDE=8) Sensitivity: CLOSED The author has added Footnote 3 on Page 18, which directly documents an NSIDE∈{4,8,16} block-scale sensitivity sweep. The results confirm that the headline template-exclusion statistic remains robust and stable (z=−16.9, −18.4, and −19.4, respectively) across the scales matching the physical imaging systematics.  
PDF
+ 4

T7 Calibration Proxy Inversion Intuition: CLOSED The text on Page 16 has been expanded to explain that galaxies changing their argmax labels under a horizontal flip are borderline objects whose post-TTA soft probabilities are naturally suppressed toward ∼0.5. This structural explanation clarifies why their raw flip-swap errors distort the spiral-only subset metrics, validating the proxy's usage.  
PDF

Out-of-the-Box Calibration Warning: CLOSED The author has integrated an explicit data-usage warning in the Data Availability section on Page 20, cautioning community users that the raw p
eq
	​

 values are optimized as ranking scores rather than frequentist probabilities, and explicitly recommending Platt or temperature scaling for downstream probabilistic workflows.  
PDF

Figure 1 Broken Symlink: CLOSED Figure 1 has been successfully restored to a complete three-panel layout. Panel (c) now correctly details the NOT_SPIRAL morphological classes (ellipticals, mergers, and edge-on systems), resolving the missing visual baseline.  
PDF
+ 4

MASTER z-Score Deficit & Null Monopole Mapping: CLOSED The author added Section III.A to explicitly map out the distinct significance frameworks used throughout the text. Furthermore, Section IV.D now incorporates the post-MASTER decoupled monopole-only null score (σ=+4.84, ∼12% power reproduction), properly separating it from the 99.32% pre-MASTER geometric mask leakage channel.  
PDF
+ 4

2. Fresh Pass (New Findings)
Majors

Section II.B (Page 2) & Appendix B (Page 16) — Dataset Splitting and Partitioning Math Ambiguity * Issue: The text states that the model uses a random 80/20 train/validation split resulting in n
train
	​

=21,293 and n
val
	​

=5,323 images from a source total of 25,790 images. It is noted that the 826-image difference is entirely due to flip-augmentation duplicates added to the training split. However, if the validation split is completely un-augmented, then 5,323 is exactly 20.00% of the post-augmented pool (26,616) , meaning the unique source images were initially split as 20,467 training (79.36%) and 5,323 validation (20.64%). While data leakage is absent since the unique image IDs remain strictly disjoint, calling this an "80/20 split" of the original manifest is mathematically confusing to a reader trying to duplicate the script's behavior.  
PDF
+ 3

Proposed Fix: Rephrase the text to clarify that a ∼79.4/20.6 split was performed on the unique source images, which subsequently yielded an exact 80/20 distribution of final data array indices after the training set was expanded via flip-augmentation.

Minors

Section IV.A (Page 4) — Truncation Discrepancy in Global Class Fractions * Issue: The author reports the Catalog C composition as CW: 1,592,107 (18.78%), CCW: 1,609,053 (18.99%), and Non-Spiral: 5,273,371 (62.23%) out of a total of 8,474,531 galaxies. Direct division yields 1,592,107/8,474,531=18.787%. Standard statistical rounding rules require this to be printed as 18.79%. The current text appears to have manually rounded down the CW fraction to force the three printed percentages to sum to exactly 100.00%.  
PDF

Proposed Fix: Adjust the CW fraction to 18.79% (accepting a standard total sum of 100.01%) or carry the global breakdown to three decimal places to maintain strict numerical precision.

Table III (Page 11) — Truncated Decimal Arithmetic Mismatch * Issue: In the "canonical, unapodized" block for the ℓ=1 band row, the table lists C
b
data
	​

×10
6
=7.27, ⟨C
b
	​

⟩
null
	​

×10
6
=0.57, and σ
null
	​

×10
6
=0.84, while reporting a significance of +7.93. Performing direct arithmetic with these printed, truncated numbers yields (7.27−0.57)/0.84=7.976. The slight difference (+7.93 vs. 7.98) indicates that the table's z-score was correctly computed from the un-truncated data vectors, but it creates a visual calculation error for the reader.  
PDF

Proposed Fix: Add a single sentence to the Table III caption explicitly noting that the reported z and p values are evaluated directly from full float precision storage arrays rather than the rounded decimals printed in the rows.  
PDF
+ 1

3. Recommendation

ACCEPT.

The manuscript has dramatically improved in structural transparency, data traceability, and statistical clarity, resolving every critical open item from the previous review cycle and establishing an exceptionally high bar for reproducibility in cosmological morphology surveys.




Thinking

