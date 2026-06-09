# P2 R22prov2 — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 471.9s

---

Meta-referee report on “Testing the Matter Bounce with Primordial Non-Gaussianity: SPHEREx Forecasts, with a MegaMapper Outlook”

This meta-review identifies blind spots not raised by the five prior reviews. I focus on end-to-end methodological consistency, hidden conditionings, estimator/observable mismatches, and oversights in how projections are mapped to the actual SPHEREx observable.

NEW FINDINGS (not raised by any of the 5 reviewers)

ID: P2-META-E1
Severity: ESSENTIAL
Section + page: Sec. II A, p. 4 (injection–recovery paragraph)
Why no other reviewer caught it: Others asked for more details of the injection–recovery but did not notice the fundamental 2D/3D observable mismatch.
Specific problem (quote the text):
“... applies a KSW-type optimal linear estimator [15] against the local template on tiled flat-sky patches covering the full sky.” and “adds isotropic Gaussian noise with the published SPHEREx photometric-z power spectra [4] as the diagonal noise covariance...”
Required fix:
Replace this CMB-style 2D flat-sky KSW test with a 3D galaxy bispectrum injection–recovery matched to the SPHEREx observable (redshift-binned 3D density field with redshift-space distortions and survey window). If you wish to keep a CMB-style KSW as a sanity check, label it clearly as a heuristic cross-check, not a validation of the SPHEREx bispectrum pipeline, and remove its numerical value (rmeasured = 0.90 ± 0.01) from the main line of evidence.

ID: P2-META-M1
Severity: MAJOR
Section + page: Sec. III B, pp. 6–7; Sec. IV, p. 7; Heinrich et al. linkage
Why no other reviewer caught it: Reviewers requested formulas for r but did not flag the missing redshift-space anisotropy (μ dependence) in the overlap.
Specific problem (quote the text):
“The 23,098 configurations result from a uniform grid in (k1, k2, k3) space...” and later using r to rescale the SPHEREx bispectrum σ(fNL).
Required fix:
Your r computation neglects the anisotropic dependence of the redshift-space galaxy bispectrum on line-of-sight angles (μ). Heinrich et al. [4] forecast σ(fNL) with a redshift-space bispectrum that depends on μ via Kaiser/RSD and bias parameters. Recompute r using the redshift-space bispectrum weight, integrating over μ (or multipoles), or explicitly justify why an isotropic k-only inner product is a good approximation for the SPHEREx redshift-space bispectrum Fisher weighting. Without this, using your isotropic r to rescale a redshift-space σ(fNL) is not justified.

ID: P2-META-M2
Severity: MAJOR
Section + page: Sec. III A, Eq. (3), p. 6; Sec. VII B, p. 12
Why no other reviewer caught it: Others noted bϕ sensitivity but not that Eq. (3) hardwires the universality assumption into “downstream weightings.”
Specific problem (quote the text):
“∆b(k, z) = 2 fNL (b1 − 1) δc / M(k, z)” and “All downstream Fisher weightings, plots, and forecasts that invoke the SDB kernel in this paper use Eqs. (3)–(4) as the canonical definition.”
Required fix:
Eq. (3) implicitly sets bϕ = 2 δc (b1−1) (universality). Later you argue bϕ is uncertain and may need to be marginalized. Any SDB-based Fisher weight or result using Eq. (3) therefore builds in an assumption you elsewhere relax. Rewrite SDB equations with a free bϕ: ∆b(k, z) = 2 fNL bϕ / M(k, z). Then clearly specify which analyses fix bϕ by universality and which marginalize it, and recompute any SDB-derived numbers accordingly.

ID: P2-META-M3
Severity: MAJOR
Section + page: Sec. III B, p. 6
Why no other reviewer caught it: Others accepted the “1 − rcos^2” heuristic; no one checked its validity conditions.
Specific problem (quote the text):
“... ‘projection noise’ is suppressed by 1 − rcos^2 ≲ 0.03 given the high shape cosine rcos > 0.97, and is therefore subdominant...”
Required fix:
This bound holds only if the template set is orthonormal under the exact noise inner product used by the estimator. In realistic bispectrum analyses, shapes are not orthonormal; leakage from partially correlated non-local shapes can add variance not bounded solely by 1 − rcos^2. Either (a) compute the full Gram (overlap) matrix of relevant shapes under the SPHEREx redshift-space inner product and propagate the resulting estimator variance inflation, or (b) remove the “1 − rcos^2” claim and qualify the statement as heuristic.

ID: P2-META-M4
Severity: MAJOR
Section + page: Sec. III B, pp. 6–7; Sec. IV, p. 7
Why no other reviewer caught it: Others focused on the absence of a formula for r, but not on whether the same r applies across distinct observables.
Specific problem (quote the text):
“We validated the overlap at three independent levels: (i) ℓ-space Fisher overlap using fiducial Cℓ ... (ii) Monte Carlo injection recovery ... SPHEREx Gaussian noise covariance ... (iii) literature search ...”
Required fix:
You mix three different inner products/observables to justify a single r that is then used to rescale the SPHEREx redshift-space bispectrum σ(fNL). CMB ℓ-space overlap, 2D KSW injection (P2-META-E1), and a 3D redshift-space bispectrum Fisher all induce different weightings. Provide one r computed and validated in the same observable/weighting used by Heinrich et al. (redshift-space bispectrum). Keep the others as qualitative cross-checks, not as quantitative validation.

ID: P2-META-M5
Severity: MAJOR
Section + page: Sec. II A, pp. 3–4; footnote 1
Why no other reviewer caught it: Others questioned reproducibility of the null-space sampling but not how it couples to the weight actually used by SPHEREx.
Specific problem (quote the text):
“... multiple coefficient sets reproduce all published benchmark values exactly... The amplitude recovery factor is r = 0.85 ± 0.13 (range: 0.55–1.14)... dominated by extreme null-space directions...”
Required fix:
The null-space sampling is performed under an implicit, isotropic k-only weight. If the SPHEREx bispectrum weight emphasizes redshift-space anisotropic configurations differently, the null-space directions that inflate/deflate r may not be the same. Recompute the null-space-induced spread in r using the SPHEREx redshift-space bispectrum weight (including μ dependence) and report the resulting spread. This directly affects the systematic error budget on r used to rescale σ(fNL).

ID: P2-META-m1
Severity: MINOR
Section + page: Sec. II A, p. 3; Table I, p. 4
Why no other reviewer caught it: Others focused on the factor-of-two and normalization, not on the “folded” kinematics itself.
Specific problem (quote the text):
“Folded (k1 = 2k2 = 2k3).”
Required fix:
Clarify that this is a colinear/degenerate “folded” limit (k1 = k2 + k3), with k1 = 2k2 = 2k3 implying k2 = k3 and k1 = k2 + k3. Many readers expect the “folded” label for the k1 = k2 = k3/2 case; add one sentence to avoid ambiguity and confirm that you use the degenerate colinear folded configuration.

ID: P2-META-m2
Severity: MINOR
Section + page: Sec. II C, p. 5
Why no other reviewer caught it: Others addressed the “divergent Hankel index” language; this is a more precise variant.
Specific problem (quote the text):
“... a semi-analytic estimate based on the superhorizon approximation for mode functions near the LQC bounce shows that the bounce contribution to fNL is suppressed by (k ηbounce)^2 ∼ 10−4...”
Required fix:
Provide a short derivation or a citation with an explicit equation showing how (k ηbounce)^2 enters and how ηbounce is defined and normalized. As stated, this is a non-trivial claim that needs either a reference to a worked example or a brief appendix derivation to be reproducible.

ID: P2-META-m3
Severity: MINOR
Section + page: Sec. II A, Eq. (1)–(2), p. 3
Why no other reviewer caught it: Others flagged dimensional ambiguity in Eq. (2); this notes a second, related ambiguity.
Specific problem (quote the text):
“AT (k1, k2, k3) = 3/(256 k1^2 k2^2 k3^2) P(k1, k2, k3), ... BNL = (10/3) P AT_i ki^3 → −35/8 as k1/k → 0.”
Required fix:
After you correct Eq. (2) as requested by other reviewers, include a one-line dimensional check explaining how a k^3-dimensionful AT combines with Σ k_i^3 (or product) to produce a dimensionless squeezed-limit fNL. This clarifies normalization and helps future readers reproduce the −35/8 limit.

ID: P2-META-N1
Severity: NIT
Section + page: Sec. IV, Fig. 2 caption, p. 8
Why no other reviewer caught it: Others flagged unlabeled axes in several figures but not the missing survey choice in this specific caption.
Specific problem (quote the text):
“Detection significance for fNL = −35/8 across survey configurations. Error bars show optimistic-to-conservative ranges...”
Required fix:
State explicitly whether the bars include μ-averaged redshift-space effects, and which degradations are included in each bar (template mismatch included or not, GR/bϕ/photo-z included or not). This avoids confusion with the systematic budget and links the plot to a concrete scenario.

Meta-review recommendation
MAJOR REVISIONS

Union of blockers across all six reviews: There are multiple essential issues (Bayes factor inconsistencies; normalization/“convention” contradiction; fabricated/inexact references; presence of version-history/internal file paths; unsupported GR-degradation mapping; and, from this meta-review, the 2D KSW injection on a 3D galaxy observable and missing redshift-space anisotropy in the r calculation). My confidence that the paper would survive external (non-bigbounce) peer review without addressing these is low. If the authors (i) replace the 2D KSW injection by a 3D redshift-space bispectrum injection, (ii) recompute r with the correct redshift-space weighting, (iii) present a consistent Bayes factor table with transparent priors and σ, (iv) resolve the normalization/commutator issue consistently, and (v) clean the bibliography and provenance artifacts, then the core idea remains compelling and likely publishable.