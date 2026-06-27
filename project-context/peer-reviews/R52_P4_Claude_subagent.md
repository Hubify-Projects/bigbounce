# R52 — P4 (Galaxy Chirality Catalog) — Claude/Opus External Referee Report

**Recommendation: ACCEPT**

Paper: P4 v1.0.188 — "Survey-Scale Galaxy Chirality with Equivariant TTA: A Null
Real-Space Chirality Dipole, a Quantifiable Monopole-Mask Leakage Channel, and
Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on
8.47 Million DESI Legacy Galaxies."
PDF reviewed end-to-end, all 22 pages (body + Appendices A–E + refs).

This is the Claude/Opus leg of internal round R52, a fresh adversarial pass
following the 2026-06-21 external 99→92 rollback. The paper has been
heavily restructured since prior rounds and is now exceptionally careful. I
applied genuine fresh eyes, truth-audited the load-bearing claims and the
cross-referenced numerics, and find no new BLOCKER or MAJOR. The verdict is
ACCEPT with a short list of optional polish-tier MINORS.

---

## 1. BLOCKERS

None.

I specifically tried to break the three load-bearing claims and could not:

- **Primary null (HC real-space dipole +0.41σ, p=0.31, N=949,584).** Supported
  by isotropic-bootstrap null, an independent per-galaxy label-shuffle null
  (z=0.70), an independent uniform-weight LSQ reimplementation (z=0.55), and a
  2×3 robustness panel across fit weighting and mask threshold. Reproducible
  from committed artifacts (`canonical_provenance/*` JSONs, `run_dipole_catalog_c.py`).
- **WLS exclusion of a clean 1.7% dipole at z≈−18.** The naive WLS z≈−264 is
  explicitly superseded by an NSIDE=8 block-bootstrap (σ inflated 14.7×), and a
  block-scale sensitivity sweep (NSIDE∈{4,8,16} → z=−16.9/−18.4/−19.4) shows the
  exclusion is robust to the bootstrap block choice. This is the correct
  conservative move, not over-claiming.
- **+3.64σ / +7.28σ MASTER residual attributed to systematics, not signal.**
  Explicitly declared NON-primary and supported by the eight-anchor battery of
  Appendix D (apodization robustness, multipole coherence, quartile washout,
  leg-proxy cross-power, density-stratified null, boundary-distance variance,
  nuisance-marginalized WLS, direct cross-spectrum). The ℓ=2>ℓ=1 broadband
  structure is genuinely incompatible with a clean ℓ=1 dipole.

Numerics cross-checked and internally consistent: +3.64σ (500-MC canonical
unapod) vs +7.93σ (10⁴-perm canonical unapod, Table III) vs +7.28σ/+7.31σ
(apodized 500-MC / 10⁴-perm); f_CW^HC=0.4974±0.000279 ↔ +0.41σ; Catalog C
monopole −9.47σ (Table II) ↔ "−9.5σ" in text; A_best=4.55×10⁻³ ↔ z=−18.1 vs
A_ref=0.034 (Table X). All conventions are labeled per-row and per-paragraph.

---

## 2. MAJORS

None.

The most credible MAJOR-candidate I evaluated — and ultimately downgraded — is
the **CE-ResNet training-label dependence** (66.5% of training labels are
CE-ResNet pseudo-labels; could the null be "null by construction"?). I downgraded
it because: (i) the result is a NULL, so the relevant failure mode is a *false*
null, which is bounded by the injection-recovery floor plus the confusion-matrix
dilution mapping to a ~1.88% true-amplitude threshold; (ii) the falsification
boundary is correctly stated in *observed-space* amplitude with cross-pipeline
comparison explicitly flagged as requiring matched Ganalyzer reanalysis; (iii)
the paper openly declares the limitation and anchors independence on the GZ1
cross-match (κ=0.40, 69.91% chirality accuracy on 234,282 disjoint galaxies) and
the Appendix-D template/cross-spectrum diagnostics. It is honestly scoped, so it
lands as a MINOR (see 3.2), not a MAJOR.

---

## 3. MINORS

**3.1 — ℓ=2 cross-spectrum discriminator rests on a thin, heavy-tailed null.**
(Sec IV D / Appendix D, discriminator (c).) The cross-spectrum anti-alignment
r_{ℓ=2}=−0.65 is quoted as σ=−2.89 against a 200-realization permutation null,
with the 1000-realization rerun "deferred to future work" — yet the paper's own
Table III caption warns the low-ℓ permutation null is heavy-tailed relative to
Gaussian (so the Gaussian-equivalent σ overstates). This is the weakest of the
eight anchors and is cited as one of three main-text systematic discriminators.
Recommend running the deferred 1000-realization null and quoting the empirical
rank-p rather than the Gaussian-equivalent. (Non-load-bearing: the primary null
and WLS exclusion do not depend on it.)

**3.2 — Direct CE-ResNet-independence check of the null is not performed.**
(Sec II / Appendix B.) Independence from CE-ResNet-inherited structure is argued
via κ and template diagnostics, but the real-space dipole is never measured on a
CE-ResNet-independent label set. A clean direct check would be to run the dipole
estimator on the 234,282 GZ1-classified galaxies. Caveat acknowledged in-paper:
this subset gives ~2× the sensitivity floor, so it cannot reach the Shamir 1.7%
class — worth stating explicitly if added.

**3.3 — Injection-recovery grid is coarse and label-level.** (Sec VI A /
Table V.) N_MC,inj=100 means A_50≈0.75% is "quoted at tested-grid precision, not
a two-decimal measurement," and injections are imposed at the per-pixel
probability level (estimator floor), not by re-running the classifier on
dipole-imprinted images. Both are correctly scoped in-text. The deferred
finer-grid recovery curve would convert A_50/A_95 from a bracket to a
measurement — worth doing for the data release this paper anchors.

**3.4 — g=2a−1 dilution mapping assumes symmetric misclassification.**
(Sec VI A.) Table IX shows mildly asymmetric chirality accuracy (CW 67.4% vs
CCW 72.4%); the ~1.88% true-amplitude figure is flagged as "approximate
symmetric-error mapping." Quoting an asymmetric-error band would tighten the
interpretive bridge.

**3.5 — Abstract caveat density (editorial).** The abstract carries four
distinct "Note:" paragraphs disambiguating null procedures/conventions. The
rigor is correct and necessary, but first-read accessibility would improve by
migrating one or two to Sec III A while keeping the headline numbers + the
falsification criterion in the abstract.

---

## 4. STRENGTHS

- **Largest chirality-labeled galaxy catalog to date** (8,474,531 galaxies /
  3,201,160 spirals), publicly released with per-galaxy weights, three tiers,
  confidence flags, and — critically — the committed null-distribution arrays and
  generator scripts. Reproducibility is exemplary; every σ in the paper traces to
  a named `canonical_provenance/*.json` artifact.

- **Flip-equivariant TTA as a constructive bias control** is a genuinely useful
  methodological contribution: the Catalog A→C comparison (2.31σ→0.41σ real-space;
  +6.48σ pre-MASTER pseudo-C_ℓ collapsing) cleanly demonstrates how sub-percent
  classifier bias × non-uniform survey depth manufactures a "significant" spurious
  dipole. This is a transferable lesson for all future photometric chirality work.

- **Disciplined, honest separation of distinct null procedures and significance
  conventions**, with a declared estimator hierarchy, an eight-anchor systematic
  battery (Appendix D), and a WLS↔NaMaster mask-equivalence audit (Table XI).
  This is model referee-defensive practice and directly answers the kind of
  "+0.41σ vs +7.28σ" confusion that drove prior external rounds.

- **Correct conservative statistics throughout**: block-bootstrap with a
  block-scale sensitivity check supersedes the inflated naive WLS z; the
  sensitivity floor is set by injection-recovery rather than asserted; the
  falsification criterion is stated in observed-space amplitude with an explicit
  cross-pipeline (Ganalyzer) caveat — the paper refuses to over-claim a
  likelihood-level exclusion of Shamir's class.

- **Independent GZ1 cross-match** (234,282 disjoint galaxies, full confusion
  matrix Table IX) is provided as an external-label anchor with honestly reported
  moderate agreement (κ=0.40), and the classifier's known overconfidence
  (mean conf 0.951 vs 58.7% three-class accuracy) is disclosed rather than buried.

---

*Verdict basis: this is a clean, heavily-caveated null-result catalog paper whose
load-bearing claims survive truth-audit against committed artifacts. Fresh
adversarial eyes surface only optional polish-tier MINORS. Consistent with P4's
frozen-ACCEPT status across prior rounds.*
