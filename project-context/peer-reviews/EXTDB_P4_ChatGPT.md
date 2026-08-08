# EXTDB P4 ChatGPT — chat: https://chatgpt.com/c/6a3f8793-a020-83e8-83db-f1aca0bc19c6

Provider: ChatGPT
Model/Tier: Instant (fast, gpt-4o)
PDF: /tmp/EXTDB_P4.pdf
Submitted: 2026-06-27
Harvested: 2026-06-27
Round: EXTDB (DE-BIASED)

---

Referee Report (MNRAS / PRD / JCAP)

1. Recommendation
MAJOR REVISIONS

The paper is strong and potentially publishable, but not yet at top-journal acceptance level because several load-bearing claims depend on complicated estimator hierarchy, inconsistent significance conventions, and systematic-attribution arguments that are plausible but not fully closed.

2. BLOCKERS

B1 — The "null dipole" headline is overqualified by multiple significant residuals.
The primary HC real-space estimator is null (+0.41σ), but the paper also reports unthresholded real-space z≈4.2–4.4, MASTER ℓ=1 diagnostics of +7.28/+7.93σ, and hemisphere/systematics rejections. These are attributed to systematics, but the paper needs a cleaner decision tree: what exact evidence makes each significant channel non-cosmological, and what quantitative criterion would have changed that conclusion?

B2 — The primary HC threshold peq > 0.6 is not sufficiently justified as pre-specified.
The confidence-cut sweep shows the signal collapses at 0.6, but because peq is uncalibrated and the low-confidence tail contains the excess, the paper must prove the threshold was frozen before inspecting the dipole/systematics outcome, or treat this as a tuned robustness choice.

B3 — Classifier ground-truth accuracy is too weak for some precision claims.
The external GZ1 chirality accuracy is only 69.91% with κ=0.40, while the catalog is used for sub-percent isotropy claims. The injection floors are useful, but the paper needs a fuller propagation of asymmetric CW/CCW confusion, not just the approximate symmetric dilution mapping.

3. MAJORS

M1 — The MASTER channel is hard to interpret.
The manuscript repeatedly says MASTER is diagnostic only, yet uses it heavily to argue completeness and tension with Shamir-class amplitudes. The paper must separate "detection capability under injected clean dipoles" from "actual observed systematic-contaminated statistic."

M2 — The WLS template exclusion z≈−18 may be overstated.
The block bootstrap is much better than naive WLS, but z≈−18 remains extremely strong and depends on block-scale choices, template adequacy, and residual covariance. It should be reframed as "strongly inconsistent under this template/noise model," not a near-final exclusion unless validated with held-out simulations.

M3 — Training-label dependence on CE-ResNet is a major independence limitation.
66.5% of training labels derive from CE-ResNet, so the catalog's novelty is scale and bias audit, not independent chirality truth. This should be moved earlier and made central.

M4 — Data/reproducibility not journal-complete without immutable archive.
HuggingFace/GitHub plus a release tag is useful, but a Zenodo DOI is still pending. For a catalog paper, immutable data, code, weights, and provenance artifacts should be deposited before acceptance.

4. MINORS

m1 — The abstract is overloaded. It contains too many caveats, null conventions, and diagnostic σ values.
m2 — Significance notation remains too dense. A boxed "do not compare these rows" estimator table would help.
m3 — Some figure captions are effectively mini-methods sections — too long for journal readability.
m4 — The edge-on contamination discussion needs a concrete measured axis-ratio cross-match.
m5 — The parity-language is careful but still risks reader confusion. The paper should repeatedly distinguish projected chirality, 3D spin, parity-even ℓ=1 anisotropy, and parity-odd monopole/even-ℓ channels.

5. Strengths

1. Very large and valuable catalog: 8.47M galaxies and 3.2M spirals.
2. Strong methodological contribution: flip-equivariant TTA and explicit demonstration that raw classifier bias can create spurious dipoles.
3. Unusually transparent systematic accounting, including mask leakage, confidence cuts, null variants, injection recovery, and template fits.
4. Good caution about Shamir comparisons: amplitude-level tension is claimed, not a full matched-pipeline exclusion.
5. Public release plan with catalog tiers, weights, code, and provenance artifacts is a major plus once archived immutably.
