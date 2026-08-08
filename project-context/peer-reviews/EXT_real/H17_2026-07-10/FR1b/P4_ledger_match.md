# ledger_match DRAFT — P4 — P4_chatgpt_FR1b.md

> DRAFT for the Opus truth-auditor, NOT a replacement. Conservative threshold (prefers UNMATCHED over a false match). Every UNMATCHED finding — and every low-score MATCHED — still needs a human/Opus source-cited disposition per §3.
>
> ledger: `project-context/peer-reviews/DISPOSITIONS/P4.md` (21 D-ids)  |  findings parsed: 14  |  threshold: 0.3

| # | sev | finding (first 120 chars) | best match | score | status |
|---|-----|---------------------------|-----------|-------|--------|
| 1 | MAJOR | Sections III B and IV C, definition of the “primary” sample: the p eq ​ >0.6 cut retains only 949,584 of 3,201,160 class | DP4-07 | 0.49 | MATCHED |
| 2 | MAJOR | Section II B and Appendix B, classifier validation: 66.5% of the training labels are CE-ResNet pseudo-labels, while the  | DP4-15 | 0.38 | MATCHED |
| 3 | MAJOR | Sections V and VI B and Appendix D, comparison with a 1.7% physical dipole: the claimed z≃−7.6 disfavor is inconsistent  | DP4-01 | 0.67 | MATCHED |
| 4 | MAJOR | Section IV C, primary null distribution: randomly permuting A p ​ among pixels assumes exchangeability, although Var(A p | DP4-15 | 0.46 | MATCHED |
| 5 | MAJOR | Appendix D, block-bootstrap WLS “exclusion”: Figure 10 explicitly shows a bootstrap distribution around the observed est | DP4-01 | 0.49 | MATCHED |
| 6 | MAJOR | Sections IV C–IV D, unresolved non-null structure: the unthresholded catalog gives a z≃4.2−4.4 real-space dipole, while  | DP4-17 | 0.58 | MATCHED |
| 7 | MAJOR | Section IV D, use of A 50 ​ and A 95 ​ : a recovery-probability threshold is not an upper limit on a real signal or syst | DP4-17 | 0.29 | **UNMATCHED** |
| 8 | MAJOR | Table V, Appendix A, and Section VII, MASTER estimator inconsistency: the manuscript alternates between a “canonical” +3 | DP4-16 | 0.14 | **UNMATCHED** |
| 9 | MAJOR | Section III D and Appendix B, equivariance of the quantity actually analyzed: Equation (2) guarantees Z 2 ​ equivariance | DP4-08 | 0.66 | MATCHED |
| 10 | MAJOR | Section VI A, GZ1-human-only cross-check: the 46,017-object sample has an estimated A 50 ​ of several percent and theref | DP4-09 | 0.12 | **UNMATCHED** |
| 11 | MAJOR | Data Availability and the preregistration/reproducibility claims: the manuscript relies on numerous external JSON arrays | DP4-21 | 0.50 | MATCHED |
| 12 | MINOR | Section VI C, theoretical interpretation: the manuscript states that cosmic-birefringence and Chern–Simons scenarios wou | DP4-12 | 0.45 | MATCHED |
| 13 | MINOR | Title and abstract, sample size: “in 8.5 million DESI galaxies” is misleading because the primary estimator uses 949,584 | DP4-13 | 0.47 | MATCHED |
| 14 | MINOR | Section VI B and Table VIII, Monte Carlo precision: 100 injections per amplitude and a 0.5-percentage-point grid near th | DP4-07 | 0.27 | **UNMATCHED** |

**Match rate: 10/14 = 71% MATCHED, 4 UNMATCHED.**

Exit 2 — 4 finding(s) need a full §3 truth-audit (genuinely-new candidates or too-weak fingerprint overlap).
