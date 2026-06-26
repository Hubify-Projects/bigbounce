# EXT21 P4 Gemini — chat: https://gemini.google.com/u/1/app/e8a1fc84381ca941

Recommendation: MINOR REVISIONS

Referee Report on MNRAS Manuscript

Title: Survey-Scale Galaxy Chirality with Equivariant TTA: A Null Real-Space Chirality Dipole, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)
Author: Houston Golden

General Assessment and Summary

This manuscript addresses a long-standing and controversial topic in observational cosmology: the claimed detection of cosmic parity violation and large-scale coordinate dipoles in the apparent winding direction (chirality) of spiral galaxies. Utilizing an impressive sample of 8.47 million galaxies from the DESI Legacy Imaging Surveys DR8, the author constructs the largest chirality-labeled galaxy catalog to date. By implementing a flip-equivariant Vision Transformer architecture backed by Test-Time Augmentation (TTA), the pipeline uncovers a real-space chirality dipole that is fully consistent with a statistically isotropic null hypothesis.

The primary breakthrough of this work is methodological and diagnostic. It demonstrates with elegant clarity that previous "detections" of cosmic asymmetry are highly likely to be artifacts arising from a small, uniform classifier monopole bias interacting with the complex, patchy geometries of survey masks. This "monopole-mask leakage channel" alone accounts for 99.32% of the raw, un-deconvolved power observed at the dipole level.

The paper is exceptionally thorough, tightly argued, and sets a new standard of rigor for morphological parity analyses. I recommend publication in MNRAS after a few minor, primarily diagnostic, clarifications are addressed.

Key Strengths

- Unprecedented Scale: Analyzing 3.2 million spiral galaxies provides a massive statistical leap forward, offering roughly 1.6 times the scale of previous leading equivariant attempts like CE-ResNet.

- Enforced Equivariance: Relying on 2-fold flip TTA to mathematically guarantee flip-equivariance directly handles the structural left-right biases that historically plague human labels and naive neural networks.

- Three-Class Architectural Foresight: Introducing a dedicated NOT_SPIRAL class is highly effective. Without it, roughly 62% of the survey's ellipticals and irregular mergers would leak into and ruin the binary selection.

- The Diagnostic Battery: The eight-anchor systematic battery in Appendix D is an exemplary demonstration of observational self-critique, systematically ruling out physical interpretations of harmonic residuals via quartile sweeps, cross-spectra, and template regressions.

Points for Clarification and Minor Revisions

1. Handling of Circular Coordinates in Bias Testing

In Appendix B, the author acknowledges that the T5 metadata leakage test relies on a linear Pearson correlation against the raw RA coordinate. Because RA is inherently circular (0° ≡ 360°), a standard linear calculation can easily hide real azimuthal trends. While the author successfully neutralizes this concern by supplementing T5 with a robust low-l real Ylm map-level regression, the text should explicitly suggest or mandate the use of true circular-linear correlation metrics for future pipelines attempting to duplicate this bias suite.

2. Edge-On Galaxy Sensitivity Penalty

The classifier assigns definite CW/CCW labels to 65.7% of visually identified edge-on systems (b/a < 0.3) rather than routing them safely into NOT_SPIRAL. Thanks to the equivariant averaging, these items split symmetrically toward a safe, non-biasing ~0.5 probability, but they still dilute the sample and impose a 5–8% sensitivity penalty on the effective sample size. It would be beneficial to add a brief sentence in the discussion highlighting how incorporating a simple automated aspect-ratio cut prior to network inference could optimize computational efficiency and enhance sensitivity floors in future data releases.

3. Clear Warning on Score Calibration

The author clearly states that the catalog's soft probabilities are overconfident ranking scores rather than true frequentist probabilities (e.g., a catalog-wide mean confidence of 0.951 versus an external Galaxy Zoo 1 verification accuracy of 58.7%). While this does not impact the threshold-based cuts utilized in the paper's primary null results, these labels are slated for public community release on HuggingFace. A prominent advisory should be added to the Data Availability section explicitly warning community users that they must apply post-hoc calibration (such as Platt scaling or temperature scaling) before feeding these scores into probabilistic downstream models.

4. Text Cleanliness and Typographical Artifacts

There are minor sentence fragments and draft markers left over near the transition from Page 1 to Page 2 (e.g., the sentence fragment ending with "...would be" followed immediately by a citation boundary). The text should be polished to remove these lingering layout placeholders prior to final typesetting.

Conclusion

This paper effectively closes the door on recent claims of large-amplitude cosmic parity violation in galaxy spin distributions while mapping out the exact systematic traps that future wide-area surveys must avoid. It represents an outstanding addition to the field.
