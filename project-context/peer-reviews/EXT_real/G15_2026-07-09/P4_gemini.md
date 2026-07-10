# P4 Gemini EXT review — G15 2026-07-09

- Paper: P4 v1.0.229 (34pp), g_P4.pdf
- Reviewer: Gemini Thinking (houston@bamf.com u/1)
- URL: https://gemini.google.com/u/1/app/1c125feb2f5da482
- Verdict: **MAJOR REVISIONS** (F14 baseline: MAJOR)

## Raw response

Gemini said
Editorial Referee Report

Journal: Physical Review D

Manuscript Title: A Null Chirality Dipole in 8.5 Million DESI Galaxies from Equivariant Deep Learning

Author: Houston Golden

Overview of the Manuscript

The manuscript investigates the large-scale spatial chirality dipole of spiral galaxies utilizing a massive dataset of 8,474,531 galaxies from the DESI Legacy Imaging Surveys DR8. The author employs a Vision Transformer (ViT-Small) modified with a flip-equivariance consistency loss and test-time augmentation (TTA) to classify galaxies into clockwise (CW), counter-clockwise (CCW), and non-spiral classes.  
PDF
+ 4

The primary finding is that the real-space galaxy chirality dipole is entirely consistent with a statistically isotropic null universe (z=+0.41, p=0.31). This directly challenges several highly publicized claims in the literature (e.g., Shamir et al.) that argue for widespread cosmic parity violation and large-scale dipole alignments.  
PDF
+ 3

The paper stands out for its high standard of reproducibility, featuring a fully public repository of model weights, code, and catalog tiers. However, before this manuscript can be accepted for publication in Physical Review D, several critical scientific and methodological issues must be addressed.  
PDF
+ 1

Major Concerns
1. Unresolved 47% Post-MASTER Harmonic Residual Amplitude

Reference: Section I, Section IV D, Section VII

Classification: MAJOR

Detail: * The author presents a quantitative forward model using imaging and brick-level templates to account for the observed spherical harmonic l=1 residuals.  
PDF
+ 2

While this model successfully captures approximately 53% of the post-MASTER residual amplitude in the correct direction, the remaining ~47% is left unresolved as an explicit open item.  
PDF
+ 3

The author minimizes this issue by demonstrating that this unmodeled remainder falls below the real-space estimator's current 95% recovery threshold (A
95
	​

).  
PDF
+ 1

However, leaving nearly half of a highly significant harmonic anomaly (+3.64\sigma canonical, +7.28\sigma apodized) physically unexplained is a severe blind spot for a paper asserting a definitive null cosmological conclusion.  
PDF
+ 1

To meet the rigorous standards of PRD, the author must either close this budget using the proposed full-scale DR8-sweep morphology-purity templates or formally incorporate this systematic ignorance into a combined joint nuisance likelihood.  
PDF
+ 1

2. Pseudo-Label Inheritance and the Limitations of Independent Cross-Checks

Reference: Section II, Section VI A

Classification: MAJOR

Detail: * A substantial portion (66.5%) of the training labels used for the ViT classifier are inherited from CE-ResNet pseudo-labels.  
PDF
+ 2

As explicitly acknowledged, the primary real-space and harmonic shuffle nulls randomize the model's own outputs, meaning they are structurally incapable of isolating large-scale survey-correlated patterns inherited through these pseudo-labels.  
PDF
+ 1

The author attempts to circumvent this circularity via a model-free cross-check using Galaxy Zoo 1 human-vote labels.  
PDF
+ 1

However, filtering for confident human votes forces a precipitous drop in sample size down to N=4.60×10
4
 galaxies.  
PDF
+ 1

Because this human-only sample possesses a coarse sensitivity floor (A
50
	​

≈3.4%, A
95
	​

≈4.5%−6.8%), it lacks the statistical power to rule out sub-percent systematic structures inherited by the primary headline catalog (A
50
	​

≈0.75%).  
PDF
+ 1

The author needs to provide a clearer theoretical bound or additional tests proving that subtle, large-scale spatial biases from CE-ResNet have not left a systematic imprint that escapes the template regressions.

Minor Concerns
1. Classifier Overconfidence and Sample Selection Threshold Bias

Reference: Section IV A, Appendix B.g

Classification: MINOR

Detail: * The trained network exhibits severe probabilistic miscalibration, with a catalog-wide mean winning-class confidence of 0.951 overshadowing the actual three-class validation accuracy of 58.7%.  
PDF
+ 1

The author notes that monotone recalibration does not alter the hard argmax labels used for the dipole fit.  
PDF
+ 1

Nevertheless, because the uncalibrated confidence scores p
eq
	​

 vary alongside image depth, seeing, and footprint geography, applying a hard confidence threshold (p
eq
	​

>0.6) introduces an implicit, unmodeled spatial selection function.  
PDF
+ 1

Applying a standard calibration method, such as Platt scaling or temperature scaling, prior to sample selection rather than leaving it as a recommendation for downstream users would drastically improve the robustness of the high-confidence catalog sample.  
PDF
+ 2

2. Production-Scale Pipeline-Pass Mismatch

Reference: Section IV A, Appendix B.e

Classification: MINOR

Detail: * The catalog-wide quality control pass flags 59,515 high-confidence rows (2.9% of the catalog) due to reconstructed flip-pass probabilities falling outside the mathematically valid [0,1] range.  
PDF

The manuscript traces this anomaly to a pipeline-pass mismatch between the standalone raw inference and the equivariant production run.  
PDF
+ 1

While the author proves that filtering out these anomalous rows leaves the primary real-space dipole null-consistent and essentially unchanged (z=+0.48), the presence of such programmatic artifacts suggests minor loose ends in the data production pipeline that should be cleaned up.  
PDF
+ 1

Recommendation

MAJOR REVISIONS
