# EXT22 P4 grok — chat: https://grok.com/c/f109d36c-34f2-49bf-a556-f91d2b9d92f8

Referee Report: MNRAS / PRD / JCAP
Paper: Survey-Scale Galaxy Chirality with Equivariant TTA: A Null Real-Space Chirality Dipole, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)
Author: Houston Golden
Date of report: June 2026

Recommendation: MINOR REVISIONS

1. Recommendation
MINOR REVISIONS. The manuscript presents a substantial, well-executed observational result: the largest publicly released chirality-labeled galaxy catalog to date (8.47 million galaxies, 3.20 million spirals) together with a rigorously controlled null measurement of the real-space chirality dipole. The primary estimators (high-confidence real-space dipole at +0.41σ and block-bootstrap WLS template exclusion of a clean 1.7% dipole at z ≈ −18) are cleanly separated from secondary harmonic diagnostics, which are correctly identified as systematics-attributed. The work demonstrates the critical importance of flip-equivariant test-time averaging (TTA) and provides a quantified monopole–mask leakage channel plus an eight-anchor systematic battery. No load-bearing claim lacks support, no critical control is missing, and reproducibility artifacts are declared. The paper is therefore publishable after minor polishing and clarification. It does not require substantial scientific rework.

2. BLOCKERS
None.

3. MAJORS
None.

4. MINORS (all readily addressable)

Clarify primary vs. diagnostic estimator footing (Sec. III B and IV C). The text already states that rows (i) and (iv) of Table I are not on the same statistical footing, but a single explicit sentence in Sec. IV C (or a footnote to Table I) reiterating that the +7.28σ MASTER value is a systematics diagnostic on the patchy weighted footprint while the cosmological statements rest exclusively on the HC real-space dipole and template fit would eliminate any residual reader confusion.

Explicitly flag the CE-ResNet pseudo-label dependence (Sec. II B). The manuscript correctly notes that 66.5% of training labels derive from CE-ResNet and that label-shuffle/per-pixel permutation nulls therefore do not test independence from survey-correlated structure inherited via pseudo-labels. Adding one short sentence in Sec. II B or the opening of Sec. IV D ("This limitation is addressed by the template-regression and leg-proxy cross-power tests reported in Appendix D") would make the scoping fully transparent at first reading.

Minor numerical/notation consistency. In the injection-recovery section (VI A) the text correctly distinguishes the real-space A50 ≈ 0.75% / A95 ∈ (1.0%, 1.5%] falsification boundary from the harmonic-channel completeness (P(≥3σ) ≥ 0.999 at Ap = 0.75%). A parenthetical reminder in the caption of Table V or Fig. 9 that these thresholds are estimator- and null-specific (and not interchangeable) would be helpful.

Edge-on contamination discussion (Appendix E). The 65.7% spiral-labeling rate for b/a < 0.3 objects is quantified; the derived 5–8% sensitivity penalty is reasonable. A one-sentence statement that the equivariant TTA mitigates but does not eliminate this contamination (already implicit) would suffice.

Typographical / extraction artifacts. A few equation renderings in the provided PDF text extraction show minor LaTeX artifacts. These are not present in the underlying manuscript and require no action; no visibly incorrect rendered mathematics appears in the scientific content.

All other points (global CW-fraction monopole, confidence-stratified washout, generative monopole-only null reproducing 99.32% of pre-MASTER power, quality-quartile stratification, leg-proxy cross-spectrum, boundary-distance variance, etc.) are already handled at a level appropriate for MNRAS/PRD/JCAP.

5. Strengths (≥3)

Unprecedented scale + public resource. The 8.47 million galaxy catalog (3.20 million spirals) with raw, calibrated, and equivariant probabilities, sky coordinates, and quality flags is released on Hugging Face (CC-BY-4.0) together with model weights and reproducibility scripts. This alone constitutes a major community asset for future isotropy, morphology, and systematics studies.

Methodological rigor in bias hardening. The flip-equivariant 2-fold TTA procedure (Eq. 2) demonstrably collapses a raw 2.31σ real-space dipole artifact (Catalog A) to a null-consistent +0.41σ (Catalog C, p_eq > 0.6). The D4-TTA hold-out, flip-swap correlation = 1.000, and eight-bias-test battery (Table VIII) provide concrete validation that future chirality analyses must adopt equivalent post-processing.

Clear estimator hierarchy and leakage quantification. The manuscript explicitly declares the real-space HC dipole + block-bootstrap WLS template fit as primary cosmological estimators and relegates the MASTER channel to a systematics diagnostic. The controlled N = 500 binomial-monopole generative null that reproduces 99.32% of the raw pre-MASTER ℓ = 1 power, together with the post-MASTER residual analysis and eight-anchor battery (Appendix D), gives a transparent, quantitative account of the monopole–mask leakage channel.

Honest sensitivity scoping and falsification criterion. Empirical injection-recovery on the HC-broad subsample yields a well-defined 50%-recovery-at-3σ threshold (A50 ≈ 0.75%) and a bracketed 95%-recovery falsification boundary (A95 ∈ (1.0%, 1.5%)). The paper correctly distinguishes this real-space boundary from the separate harmonic-channel completeness and does not over-claim a formal likelihood exclusion of Shamir-class signals. This conservative framing is exactly what the community needs.

Constructive engagement with prior literature. The comparison with Shamir (2012–2022) and CE-ResNet (Jia et al. 2023) is balanced: it highlights the factor ~6–12 amplitude discrepancy under the present pipeline while explicitly noting that a matched-footprint Ganalyzer reanalysis would be required for a formal statistical exclusion. The methodological critique (lack of comparable bias audit in earlier work) is evidence-based rather than rhetorical.

Summary
This is a high-quality, methodologically careful null result that advances both the observational catalog and the analysis standards for galaxy chirality/isotropy studies. The primary scientific conclusions are robustly supported by multiple independent estimators and an extensive systematics audit. Minor revisions are requested only for added reader clarity on scoping and estimator hierarchy; no new observations, re-analyses, or major rewrites are required. I recommend acceptance after these straightforward clarifications.
