# Cover Letter — Paper 5

**Title area:** Spiral galaxy chirality vs. large-scale-structure environment: a DESI DR1 / DESIVAST null
**Source:** `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`
**Suggested venue:** Physical Review D (or ApJ / MNRAS)

Dear Editor,

Please consider this manuscript. This cover letter states its contribution,
scope, and structural dependency plainly.

## Contribution
The paper cross-matches the 8.47M-galaxy chirality catalog (per-galaxy public
`class_eq` labels) against the DESI DR1 redshift catalog to test whether spiral
galaxy handedness is statistically independent of large-scale-structure
environment. Its primary result is a **void/non-void null**: the
DESIVAST-anchored contrast Δf_CW = +0.0007 (SE ≈ 0.0022) on 56,981 void spirals,
robust across all five DESIVAST void-finders (|Δf_CW| ≤ 0.004, |z_Δ| ≤ 1.25). A
secondary T-Web tidal cosmic-web classification on 14.6M DR1 galaxies provides a
supporting cross-check.

## Scope statement
This is an **environmental-independence null** — a bounded upper limit set by the
void sample size, not a detection. The headline Δf_CW result is algebraically
invariant under any catalog-wide monopole shift, so it is **self-contained with
respect to the catalog's overall calibration**: it does not depend on the
monopole amplitude or its uncertainty. The DESIVAST void path is the single
primary estimand; the T-Web path is explicitly secondary.

## Disclosed limitations (stated up front)
1. **Structural dependency on the in-preparation Paper IV.** The classifier
   architecture, training, parity-equivariance validation, and the origin of the
   catalog monopole are documented in the same-author Paper IV, currently *in
   preparation*. The abstract states this and provides a self-contained
   Appendix A summary. While the *headline Δf_CW null* is algebraically
   independent of Paper IV (monopole-invariant), a referee cannot fully vet the
   raw per-galaxy label integrity and parity-equivariance without Paper IV.
2. **T-Web in redshift space.** The secondary T-Web classification is performed in
   observed redshift space; RSD boundary-leakage is bounded by a scalar
   displacement heuristic rather than full Zel'dovich/BAO reconstruction, and
   rigorous deprojection is deferred — disclosed as a secondary-analysis caveat.
3. **Underpowered secondary bins** (e.g. the T-Web void bin, n=428) and a ~2.1σ
   filament bright/dark sign-flip attributed to BGS selection, both flagged
   in-text as diagnostics, not signals.

## The judgment for the referee
The specific question an LLM referee raised — and the one a human referee is best
placed to adjudicate — is a **structural/venue call: should publication be
contingent on the acceptance and availability of the in-preparation Paper IV, or
does the monopole-invariant self-contained headline null (with the Appendix A
classifier summary) stand on its own for a standalone article?** This dependency
clears naturally when Paper IV publishes. We ask you to judge whether the
algebraic monopole-invariance and the self-contained summary are sufficient for
the null to stand now, or whether the companion should be co-submitted or
in-hand first.

No genuinely-new correctness defect is outstanding.

Sincerely,
Houston Golden (houston@hubify.com)
