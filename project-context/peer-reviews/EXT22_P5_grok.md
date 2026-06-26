# EXT22 P5 grok — chat: https://grok.com/c/14cd22f6-3501-4dc6-a1b4-ed10e8263970

Referee Report: MNRAS / PRD / JCAP
Paper: Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across the DR1 Matched-Spiral Sample
Author: Houston Golden
Date of report: June 2026

Recommendation
MINOR REVISIONS

The paper presents a high-quality, rigorously executed null result on environment-dependent spiral chirality in DESI DR1. The primary DESIVAST-anchored analysis (n_void = 56,981) and supporting T-Web / Tempel / ASTRA cross-checks are statistically sound, with excellent reproducibility provisions. No substantial scientific rework is required. The manuscript is suitable for MNRAS/PRD/JCAP after addressing a small number of clarity and emphasis points.

BLOCKERS
None.

MAJORS
None. All load-bearing claims (null on Δf_CW, invariance under monopole shift, robustness across classifiers and hyperparameters) are supported by explicit tables, permutation tests (N_MC = 1,000), Bonferroni/LEE corrections, and committed artifacts. The post-hoc primary-path declaration is explicitly bounded by the full analysis-tree declaration (Table II) and multiplicity control; this is handled transparently and does not rise to MAJOR.

MINORS

Primary-path declaration visibility (Abstract / §I / §VB). The explicit post-hoc designation of the DESIVAST-anchored void cross-check as primary, together with the full analysis-tree declaration and garden-of-forking-paths bounding, is already present and correctly conservative. For maximal referee/reader clarity, add one short sentence in the abstract or opening of §I reiterating that "the primary path was selected post-hoc but is pre-declared here with the complete analysis tree (Table II) and Bonferroni-5 family control." This is a transparency polish item, not a methodological flaw.

RSD caveat phrasing (§XIII and §VIII). The paper correctly flags that the headline null is a fixed-redshift-space result and supplies both the scalar σ_v/(aH) ≲ 5 Mpc/h bound and the order-of-magnitude boundary-crossing estimate (~3–5% of cells). Consider one additional clause in the limitations paragraph or abstract footnote to the effect that "the scalar bound is indicative; the dominant channel is anisotropic and is not fully propagated here." This strengthens an already careful caveat without requiring new calculation.

Minor textual / series-context items. A few sentences referencing "Paper IV (in preparation)" or companion preprints could be tightened for standalone readability (e.g., brief parenthetical scope note on the monopole offset provenance). These are submission-day polish items.

No other methodological, statistical, or reproducibility concerns. The reproducibility checklist, deterministic seeding, per-output provenance JSON, and GitHub artifact mapping (A1–A30) are exemplary.

Strengths (≥3)

Statistical and robustness framework. The combination of Jeffreys binomial credible intervals, label-shuffle permutation nulls (N_MC = 1,000), explicit monopole-referenced residuals (Eq. 1), Phase-2 (R_s, λ_th) hyperparameter sweep, and multi-classifier cross-validation (DESIVAST three-algorithm + Tempel FoF + ASTRA probabilistic + concurrent T-Web literature) constitutes best-practice rigour for a large-scale null test. The omnibus 4×2 homogeneity tests, within-class density stratification, and tracer-program splits are all cleanly executed and correctly interpreted.

Primary-path clarity and scoping. The explicit declaration that DESIVAST (n ≈ 57k) is primary while T-Web (small void bin) is secondary, together with the full analysis-tree table and Bonferroni family definitions, is a model of transparent post-hoc path selection. The paper correctly anchors the headline on the properly powered, peer-reviewed void catalog rather than the counting-statistics-limited T-Web void class.

Reproducibility and data provenance. The committed GitHub repository (tag v0.1.83-2026-06-19), deterministic seed (20260515), per-output provenance JSON, exact contingency tables for χ² recomputation (Appendix B), and Hugging Face catalog mirror set a gold standard. Every numeric claim in the manuscript is regenerable from the released artifacts. This level of transparency is rare and should be highlighted as a strength.

Conservative interpretation and limitations handling. The paper correctly frames the result as an observational upper bound on future bounce-chirality models at the ≳25 Mpc/h scale rather than a blanket "no signal exists" claim. The RSD redshift-space caveat, selection-function notes, and toy EFT appendix (explicitly labelled schematic/guide, not derived constraint) are all appropriately scoped. The bright/dark program residual is analysed rather than ignored.

Overall Assessment
This is a clean, well-controlled null result that meaningfully extends the Paper IV global parity-mixture bound into the environmental domain. The methodology is sound, the statistical treatment is careful, cross-checks are extensive, and reproducibility provisions are outstanding. With the minor clarifications above, the paper will make a strong contribution to the DESI cosmology and galaxy-evolution literature. I recommend MINOR REVISIONS; the revisions are textual/emphasis only and do not require re-analysis or new computations.
