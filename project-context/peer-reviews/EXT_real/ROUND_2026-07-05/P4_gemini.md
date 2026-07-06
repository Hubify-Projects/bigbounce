# EXT Review — P4 × Gemini
- paper: P4
- version: v1.0.212
- reviewer: Gemini
- model: 3 Pro (Ultra)
- timestamp: 2026-07-06T19:14:16Z
- chat_url: https://gemini.google.com/u/1/app/2002e23492ec7acc
- pdf: /tmp/round_P4.pdf

## Raw verbatim response

As an AI evaluating this manuscript against the rigorous peer-review standards of Physical Review D, I have analyzed the methodology, statistical claims, and systematic controls presented in the text. Here is the evaluation:

VERDICT: MINOR REVISIONS

ISSUES:

[MAJOR] Section IV.D / Appendix D (Systematic Forward Model): The forward-modeling of the l=1 systematic residual using imaging and morphology templates (source density, depth, PSF, etc.) successfully accounts for approximately 52% to 54% of the observed amplitude. While the manuscript transparently acknowledges that the remaining ~47% is an "explicit open item" not captured by these templates, leaning heavily on the "systematics-attributed" label for the entire harmonic diagnostic risks overstating the completeness of the systematic model. The text should more explicitly emphasize that the unidentified ~47% variance limits the absolute closure of the harmonic diagnostic channel, even if the primary real-space estimator remains clean.  
PDF
+ 1

[MAJOR] Section VI.A (Pseudo-label independence): The author addresses the potential inheritance of survey-correlated bias from CE-ResNet pseudo-labels (which make up 66.5% of the training data ) by running a GZ1-only sub-model. However, this sub-model utilizes a significantly reduced sample of 1.5×10
4
 high-confidence spirals compared to the main pipeline's 9.5×10
5
, inflating the statistical floor by a factor of roughly 7.9. While the author correctly bounds the theoretical maximum inherited dipole , a full-catalog re-inference using the GZ1-only model at the headline sample size  would transform a theoretical bound into a definitive empirical proof.  
PDF
+ 4

[MINOR] Section IV.A (Catalog Statistics): The manuscript identifies that the ViT-Small classifier is strongly overconfident, boasting a mean classification confidence of 0.951 against an external GZ1 three-class accuracy of 58.7%. The author justifies that the primary dipole estimator consumes hard argmax counts, meaning probabilistic miscalibration cannot directly bias the dipole amplitude. However, because the high-confidence sample selection relies strictly on a p
eq
	​

>0.6 threshold, the severe miscalibration does heavily dictate the spatial sampling and sample density. Applying temperature scaling or Platt scaling to the probabilities prior to the threshold cuts (as suggested for downstream users ) would result in a more physically meaningful purity-completeness tradeoff.  
PDF
+ 4

[MINOR] General Presentation & Structure: The manuscript utilizes highly dense, nested parentheticals and frequently repeats defensive caveats—such as reminding the reader that σ values derived from distinct null procedures are not directly comparable. This disrupts narrative flow. These warnings should be streamlined into a single, prominent methodology section regarding significance conventions, rather than reiterated inside the results.  
PDF
+ 4

CENTRAL CLAIM SUPPORT: The central claim of a null real-space chirality dipole at a sub-percent sensitivity floor is robustly and convincingly supported by the multi-tier systematic battery and the mathematically guaranteed flip-equivariant test-time averaging.  
PDF
+ 2
