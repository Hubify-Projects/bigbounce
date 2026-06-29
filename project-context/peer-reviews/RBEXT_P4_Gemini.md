# RBEXT P4 Gemini — chat: https://gemini.google.com/u/0/app/789839870afb892b
VERDICT: MINOR REVISIONS

Provider: Gemini (Flash regular tier)
PDF: RBEXT_P4.pdf | md5: cdec310d3a1f3408777da0df5ae2d4a8
Harvested: 2026-06-29

---

Recommendation: MINOR REVISIONS

General Assessment: This manuscript presents a highly rigorous, survey-scale analysis of spiral galaxy chirality using 8.47 million galaxies (3.2 million spirals) from DESI Legacy Imaging Surveys DR8. The author uses a flip-equivariant ViT with TTA to produce a massive, bias-hardened chirality catalog. The primary cosmological result is a robust null detection of a real-space chirality dipole. The paper identifies and quantifies the "monopole-mask leakage channel" — a small uniform classifier monopole coupling with a patchy survey footprint to generate spurious l=1 angular power spectrum signal, successfully explaining prior literature claims as survey systematics.

Key Strengths

- Scale and Methodology: 3.2 million spirals represents ~25× expansion over previous critical analyses. Dedicated NOT_SPIRAL class eliminates elliptical/irregular leakage.
- Systematics Battery: Eight-anchor systematic suite (Appendix D) sets a high standard for robustness in morphological cosmology.
- Explanatory Power: Generative null experiment reproducing 99.32% of pre-MASTER l=1 power from monopole leakage provides clean falsification of prior literature claims.

Specific Points for Revision

1. Circular Metric Clarification (Metadata Leakage)
In Appendix B.d, Test 5 evaluates linear Pearson correlation against raw RA coordinate. RA is circular (0°≡360°) and linear r might understate azimuthal coupling. Compute a circular-linear correlation coefficient (e.g., Mardia's Rxv²) for T5 directly to make the baseline battery self-contained.

2. Soft-Probability Calibration
The text warns that max-class probabilities are not probabilistically calibrated (95.1% mean confidence vs. 58.7% external accuracy). Provide the calibration coefficients (e.g., temperature parameter T for Platt/temperature scaling) in the repository or appendix.

3. Framing of the True-Amplitude Mapping (Sec. VI.B.b)
The true underlying threshold of ∼1.88% is mapped from A_50 using GZ1-dilution factor g=2a−1. The GZ1 confusion matrix shows asymmetric accuracy (67.4% CW vs. 72.4% CCW) and ~19% triage rate to NOT_SPIRAL. Add a sentence explicitly confirming whether this asymmetry introduces a directional bias or merely acts as a uniform dampener.

4. Minor Typographical/Formatting Notes
- Page 3, Section III.A.b, bullet 1: small typo "rank -p=0.31" should be "rank-p = 0.31".
- Figure 8: text labels show σl=1 = +3.63 and σl=2 = +4.73, while surrounding text references canonical-mask residual of +3.64σ. Reconcile in the caption.
