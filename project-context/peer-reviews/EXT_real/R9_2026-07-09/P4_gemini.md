Gemini said

Referee Report for Physical Review D

Manuscript Title: A Null Chirality Dipole in 8.5 Million DESI Galaxies from Equivariant Deep Learning Author: Houston Golden 
Recommendation: Accept with Minor Revisions  
PDF
+ 1

Overview and General Comments

The manuscript presents a rigorous observational measurement of the large-scale chirality dipole of spiral galaxies using a dataset of 8,474,531 galaxy images from the DESI Legacy Imaging Surveys DR8. The author leverages a Vision Transformer with test-time equivariant averaging (TTA) to classify galaxies into clockwise (CW), counter-clockwise (CCW), and non-spiral classes. The primary real-space dipole estimator yields a null result, with a measured significance of +0.41 standard deviations against an isotropic pixel-permutation null. Furthermore, a block-bootstrap weighted least squares (WLS) template fit disfavors a clean cosmological dipole at a 1.7% reference amplitude.  
PDF
+ 4

This is a highly significant contribution to observational cosmology. The author systematically and convincingly dismantles previous claims of parity-violating dipoles in galaxy spin directions (e.g., Shamir 2012, 2020, 2022), demonstrating that such claims are highly susceptible to monopole-mask leakage. The methodology is sound, the dataset is the largest of its kind to date, and the systematic bias-hardening suite is exemplary. I recommend the manuscript for publication in Physical Review D following attention to a few minor clarifications regarding the presentation of the unmodeled harmonic residuals and the calibration of the classifier.  
PDF
+ 3

Major Strengths

Methodological Rigor (Equivariant TTA): The implementation of 2-fold flip test-time averaging (TTA) is a standout feature of the pipeline. The author shows that without this forced equivariance, a raw classifier CW excess of merely 0.79% couples with survey depth to produce an artificial 2.31 standard deviation real-space dipole. The TTA collapses this spurious signal to a null 0.41 standard deviations, underscoring the necessity of equivariant post-processing in morphological parity studies.  
PDF
+ 2

Monopole-Mask Leakage Identification: The author provides a vital service to the community by formalizing the generative monopole-only null. The demonstration that a simple binomial-monopole realization reproduces 99.32% of the raw pre-MASTER l=1 power definitively isolates the artifact that has likely driven previous false detections in the literature.  
PDF
+ 2

Model-Independent Verification: To rebut potential concerns that the null result is inherited from the CE-ResNet pseudo-labels used in training, the author performs a model-free cross-check using solely human votes from Galaxy Zoo 1. This test, utilizing 46,017 confident DESI-matched spirals, returns a clean null of -0.54 standard deviations, proving the null is not a learned artifact.  
PDF

Handling of Systematics (8-Anchor Battery): The author transparently reports a residual in the post-MASTER canonical mask l=1 channel. Instead of hiding this, they deploy a thorough 8-anchor systematic battery to prove it behaves like a survey-correlated artifact (depth, point spread function, morphology) rather than a clean primordial dipole.  
PDF
+ 1

Areas for Minor Revision & Clarification

The Unmodeled Harmonic Residual: * The forward model accounts for approximately 54% of the observed harmonic residual amplitude using imaging and morphology templates.  
PDF
+ 1

The remaining 47% is explicitly left unmodeled.  
PDF

While the author successfully bounds the cosmological content of this remainder by noting it falls below the real-space 50%-recovery floor, relying on this boundary argument feels slightly incomplete.  
PDF

The author acknowledges that fully attributing this remainder requires a per-pixel classifier confidence-vs-depth response map, which is deferred to future work. A brief expansion in the discussion on how future spectroscopic cross-matches (e.g., DESI Year 1) might help close this remaining 47% gap would strengthen the manuscript.  
PDF
+ 1

Softmax Calibration Caveats: * The manuscript accurately diagnoses the Vision Transformer as "strongly overconfident," noting that the mean winning-class confidence exceeds the realized three-class accuracy.  
PDF
+ 1

The author correctly argues that this miscalibration does not bias the real-space dipole because the estimator relies on hard counts thresholded at p
eq
	​

>0.6.  
PDF

However, for the dataset to serve as a community resource, the author should explicitly warn users who might attempt to use the raw probabilities as frequentist likelihoods in downstream models. The author briefly mentions Platt scaling in the Data Availability section, but a stronger warning in the main text is warranted.  
PDF

Clarity of Null Hierarchies: * The manuscript juggles multiple estimators, significance conventions, and null procedures (e.g., pixel-permutation, label-shuffle, block-bootstrap).  
PDF
+ 2

Table I is an excellent addition that maps these claims effectively.  
PDF
+ 1

To further aid readability, the author should ensure that every time a significance is cited in the abstract or conclusion, it is explicitly paired with the specific null it was tested against, to prevent readers from falsely comparing incommensurable values.  
PDF

Conclusion

This manuscript is an exhaustive, methodologically sound, and highly necessary correction to the literature surrounding cosmic parity violation in galaxy morphology. The use of equivariant deep learning to eliminate directional bias sets a new standard for the field. I recommend acceptance following the minor clarifications noted above.

--- MANIFEST: P4 (v1.0.224) | Gemini Pro | native PDF | chat 0fc5ad905d386372 | verdict minor-revisions ('Accept with Minor Revisions') | 2026-07-09
