# RCEXT P4 ChatGPT — chat: https://chatgpt.com/c/6a42d1b8-ca48-83e8-ac92-0a64eabda9b3
VERDICT: MAJOR REVISIONS

Provider: ChatGPT (Instant/default)
PDF: RCEXT_P4.pdf (md5: 21577dac74ab920704fdfbcb3102d234)
Harvested: 2026-06-29

---

1. Recommendation: MAJOR REVISIONS

The paper is potentially publishable and scientifically valuable, but not yet at top-journal acceptance level because the primary null result depends on several fragile hierarchy/selection choices while the manuscript contains many significant diagnostic tensions that are explained as systematics rather than fully modeled.

2. BLOCKERS

None requiring rejection. The paper is unusually transparent about null conventions, catalog limitations, and systematic diagnostics, and the primary result is plausible.

3. MAJORS

Primary-estimator hierarchy feels partly post-hoc despite being "declared." The HC real-space dipole is null at +0.41σ, but the unthresholded sample shows z≈4.2–4.4, and harmonic diagnostics show +7σ-level residuals. The paper attributes these to low-confidence/systematic channels, but for publication the authors should justify why peq > 0.6 is the primary science sample with a pre-registration-level provenance, not only generator-history statements.

Pseudo-label dependence remains a serious limitation. 66.5% of training labels derive from CE-ResNet, and the independent GZ1 chirality accuracy is only 69.91%. The authors acknowledge this, but the proposed fully independent GZ1-only retraining is deferred. For a catalog/null-dipole paper, that should be performed or the headline claims should be softened.

MASTER channel inconsistency is not fully resolved. The manuscript reports +3.64σ, +7.93σ, +7.28σ, +7.13σ under related-but-different conventions. The explanations are careful, but the result reads like a forest of systematics-attributed excesses rather than a clean null analysis. A unified decision tree showing which estimator is used for which scientific claim is needed.

Classifier calibration is weak for precision cosmology. Mean confidence is 0.951 while external three-class accuracy is 58.7%. The paper says peq is only a ranking score, but then uses confidence cuts as load-bearing systematics control. More calibration/validation against independent human labels is required.

The claimed tension with Shamir is only pipeline-level. Several abstract/conclusion phrasings could be read as stronger than a likelihood-level exclusion of Ganalyzer. Require matched-footprint or substantially softer language.

4. MINORS

The abstract is overloaded with too many non-comparable σ values.
The distinction between Ap units and fCW units should be made visually in every key table/figure caption.
The "largest chirality catalog" claim should be phrased as "to our knowledge" consistently.
The edge-on contamination estimate remains qualitative; either quantify fedge or move sensitivity-penalty language to discussion.
Some artifact-path references are too internal for journal readability; consolidate into a reproducibility table.

5. Strengths

Very large catalog: 8.47M galaxies, 3.2M spirals.
Strong methodological contribution: flip-equivariant TTA and explicit demonstration that raw classifier bias can mimic dipoles.
Excellent transparency about null definitions, systematics, and estimator non-comparability.
Public-data orientation with catalog/model/code release plans.
The monopole-mask leakage analysis is valuable beyond this specific chirality application.
