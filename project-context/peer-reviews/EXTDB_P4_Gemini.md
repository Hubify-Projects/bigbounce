# EXTDB P4 Gemini — chat: https://gemini.google.com/u/0/app/99985cc1227c98c8

Provider: Gemini
Model/Tier: Flash (regular)
PDF: /tmp/EXTDB_P4.pdf
Submitted: 2026-06-27
Harvested: 2026-06-27
Round: EXTDB (DE-BIASED)

---

Referee Report (MNRAS / PRD / JCAP)

1. Recommendation
MINOR REVISIONS

2. Summary and Strengths
This paper presents a rigorous and impressively scaled analysis of a new morphological chirality catalog containing 8.47 million galaxies (including 3.20 million spirals) from the DESI Legacy Imaging Surveys DR8. The author constructs a pipeline using a Vision Transformer (ViT-Small) and integrates a horizontal-flip test-time equivariant averaging procedure (TTA) to handle instrumental and classification biases.

The primary scientific outcome is a real-space chirality dipole measurement that is fully consistent with a null isotropic distribution. This provides a highly valuable baseline that systematically challenges previous claims of order-percent dipoles in the literature (e.g., Shamir et al.).

Strengths meriting publication in MNRAS:
1. Unprecedented Scale: At 3.20 million spirals, it stands as the largest publicly released chirality catalog to date, improving statistics by a factor of 1.6× over the previous benchmark (CE-ResNet).
2. Rigorous Bias Hardening: The inclusion of an explicit multi-axis bias-hardening audit suite (8 distinct check benchmarks) represents an outstanding methodology template for future morphological cosmology studies.
3. Methodological Clarity on Artifacts: The author successfully unmasks a massive pitfall in pseudo-Cl harmonic analyses by proving that a tiny uniform classification monopole couples to survey geometry to simulate highly significant, yet entirely spurious, dipole modes.

3. BLOCKERS
None. The scientific execution is robust, and the public release of full code, reproducibility scripts, and model weights meets the highest modern astronomical standards.

4. MAJORS
None. The core cosmological conclusions are securely anchored across multiple real-space and harmonic estimators with extensive statistical tests.

5. MINORS

m1 — Inconsistent Notation Reporting Convention for l=1 Bandpower.
The text quotes the canonical unapodized 10^4 permutation value as +7.93σ, but the primary tracking summary in Table I defines this canonical MASTER diagnostic as +3.64. Section VII clarifies that +3.64σ represents the 500-MC direct run while Table III provides the 10^4 permutation value (+7.93σ), but introducing these mismatched values without localized explanation causes layout confusion. Revision: Standardize or multi-index the values explicitly in Table I.

m2 — Understating Azimuthal Coupling due to Circular Coordinate Metrics.
The bias hardening suite test T5 (Metadata leakage) relies on linear Pearson correlation against the Right Ascension coordinate. Because RA is circular (0°≡360°), a linear r is mathematically blind to phase-wrapping discontinuities. Leaving a compromised baseline test labeled as "passed" is visually misleading. Revision: Amend Table VIII to footnote the structural limitation of the T5 metric, or replace with a directional statistics circular-linear correlation metric.

m3 — Asymmetric Triage of Edge-on Disc Contamination.
65.7% of visually identified edge-on systems (b/a < 0.3) mistakenly receive a definitive CW/CCW spiral classification. The author argues that equivariant averaging enforces flip-symmetric soft probabilities, but if the CE-ResNet pseudo-label training data contains an asymmetric winding bias for edge-on profiles, the symmetric misclassification assumption (g=2a−1) breaks down. Revision: Add a brief clarifying sentence explicitly bounding this caveat until the proposed cross-match with full DESI Legacy photometric axis-ratio catalogs is executed.

m4 — Layout Clarification for Figure 6 Inset.
Figure 6's right-hand panel contains an un-captioned inset plotting "CW fraction vs Confidence" without explicit description. Revision: Add a single sentence to the Figure 6 caption defining the axis parameters and error bars shown.
