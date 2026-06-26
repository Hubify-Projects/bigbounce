# EXT22 P4 gemini — chat: https://gemini.google.com/u/0/app/e2529a7a0978085a

Recommendation: MINOR REVISIONS

General Summary
This paper presents the largest galaxy chirality catalog to date, consisting of approximately 8.47 million galaxies (including 3.2 million spiral galaxies) selected from the DESI Legacy Imaging Surveys DR8. The author employs a Vision Transformer (ViT-Small) pipeline combined with flip-equivariant test-time averaging (TTA) and an equivariance consistency loss to classify galaxies into clockwise (CW), counter-clockwise (CCW), and non-spiral classes.
The primary cosmological result is a real-space chirality dipole measurement that is fully consistent with a null signal (zmom = +0.41, p = 0.31). This stands in stark contrast to several prominent claims in previous literature that reported significant large-scale asymmetries. Crucially, the paper identifies and formalizes a "monopole-mask leakage channel," demonstrating that a minor uniform classifier bias (a global monopole) interacting with a complex, patchy survey footprint can artificially generate highly significant pseudo-Cl power at the l = 1 mode. The paper is exceptionally rigorous, highly transparent regarding its systematic controls, and provides open-source access to the catalog, model weights, and full reproducibility pipelines.

Strengths

Unprecedented Scale and Open Data Collaboration: At 8.47 million galaxies and 3.2 million classified spirals, this work scales up previous chirality studies by orders of magnitude. The public release of the catalog tiers, model weights, and exact reproducibility scripts on HuggingFace/GitHub is an exemplary open-science practice.

Methodological Safeguards Against Spurious Signals: The integration of flip-equivariant test-time averaging (TTA) and a specialized cross-entropy loss with an equivariance penalty provides a robust architectural defense against native network chiral biases. This successfully collapses a raw spurious dipole of +2.31σ down to a null-consistent +0.41σ.

Exemplary Systematic Auditing: The author does not simply gloss over harmonic residuals; instead, they build a comprehensive 8-anchor systematic battery (Appendix D) spanning quality-quartile stratifications, leg-proxy cross-power, and spatial-coherence block-bootstrapping. The generative null model demonstrating that the monopole-mask leakage accounts for 99.32% of the pre-MASTER l=1 power provides an elegant physical resolution to historical literature conflicts.

Blockers
None. The paper is scientifically sound, and the numerical conclusions are tightly bound to the presented data and code artifacts.

Majors
None. No substantial scientific rework or additional cosmological estimators are required.

Minors

1. Table VIII Layout and Alignment
In Section Appendix B (Page 18), Table VIII ("Bias-hardening test results") appears to have text-stacking and alignment issues within the "Result" column for the rows corresponding to tests T1 through T6. Ensure that each test row (especially T5 and T6) has its respective scalar result clearly separated and horizontally aligned with its threshold column in the final typeset version to maximize scannability.

2. Minor Discrepancy in Confidence Bin Text
There is a minor rounding inconsistency regarding the reported significance of the low-confidence systematic tail:
In Section IV.E (Page 12), the text cites a "+3.30 signal in the 1.87M-galaxy [0.5,0.6) confidence bin".
In Appendix C (Page 19), the text cites the same feature as "+3.290".
Please harmonize these values to a consistent decimal precision throughout the text.

3. Typographical Error on Page 10
In Section IV.D (Page 10, left column), there is a slight duplicate-word typo in the text block: "...the mean-of-ratios/ratio-of-means distinction does oes not arise for this statistic."
Please correct this to "...does not arise..." during final copyediting.
