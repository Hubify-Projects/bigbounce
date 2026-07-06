# EXT Review — P5 × Grok
- paper: P5
- version: v0.1.101
- reviewer: Grok
- model: Expert
- timestamp: 2026-07-06T19:18:11Z
- chat_url: https://grok.com/c/631e2d33-8e7f-4894-87bf-f3e72e20f5f2
- pdf: /tmp/round_P5.pdf

## Raw verbatim response

Thought for 46s

VERDICT: MINOR REVISIONS

ISSUES:

[MINOR] §V B (and abstract): The DESIVAST-anchored path is explicitly designated primary post-hoc ("no timestamped plan predates the data") even while claiming three result-independent a priori grounds; the analysis-tree table (Table III) and Bonferroni-5 family are transparent, but the abstract and §I do not clearly caveat that the tightest quoted bound (∼0.5–0.6 pp effective 2σ after fixed-void-geometry systematic) derives from the post-hoc choice among five correlated DESIVAST estimators. This weakens interpretability of the "primary" headline null.
[MINOR] §II and Appendix A: The manuscript is presented as largely self-contained via Table I and the classifier summary, yet the parity-equivariant ViT-Small architecture, Z₂ TTA implementation, training-set composition, and exact origin of the −0.0026 monopole remain dependent on the in-preparation Paper IV; public HuggingFace catalog access is cited but the end-to-end reproducibility chain for the per-galaxy class_eq labels (and thus the invariant ∆f_CW contrast) is incomplete without that prior work or a committed code release at submission.
[MINOR] §VIII A and §IX C: The T-Web void vs. DESIVAST overlap purity diagnostic uses only n=6 galaxies ("0/6 T-Web 'void' spirals fall inside any of the 101,863 DESIVAST VoidFinder holes"); this sample is too small to support even an illustrative constraint and should be explicitly labeled as such or removed, as it risks giving a false impression of quantitative cross-check strength.
[MINOR] Abstract / first-page summary and §VIII: The effective 2σ bound after folding in the ±0.34–0.37 pp fixed-void-geometry membership systematic is quoted without defining its construction (Monte Carlo on σ_v/(aH) = 5 Mpc/h perturbations under fixed void centers/radii) or distinguishing it from the pure counting-statistics SE(∆) = 0.0022; readers scanning only the headline require this precision to evaluate the claimed upper limit.

Central claim supported? Yes: every reported path (five DESIVAST estimators as Bonferroni-5 primary family plus nine-cell T-Web Phase-2 sweep, redshift/density/sky-position/tracer-program stratifications, and external cross-checks) returns null results for environment-dependent chirality after explicit monopole subtraction, with all residuals inside counting statistics or the documented selection-function residuals; the evidence therefore supports the stated bounded upper limit at current DESI DR1 sensitivity.
