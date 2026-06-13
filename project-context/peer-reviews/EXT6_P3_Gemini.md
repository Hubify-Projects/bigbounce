# EXT6 P3 — Gemini Thinking (in-thread delta round 6; FRESH THREAD)
**Chat**: https://gemini.google.com/u/0/app/2b33106610ec2401
**PDF**: paper3_anomaly_catalog_v3.1.100.pdf (39c00ff6) · harvested 2026-06-12 19:59 PT
**Note**: Fresh thread — first response. Serving model: Gemini Thinking (2.5 Pro, confirmed via UI "Thinking" dropdown).

---

Gemini said
Referee Report

Journal: Monthly Notices of the Royal Astronomical Society (MNRAS)

Manuscript Title: Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and a Native-Trained Novelty Fraction from 37.3 Million Sources and Map Patches Manuscript Version: Paper 3 v3.1.100 (pipelines/p3_anomaly_engine/paper3_draft.tex)

1. Recommendation

MAJOR REVISIONS

The authors present an ambitious, large-scale framework (p3_anomaly_engine) to isolate anomalous objects across multiple imaging and photometric surveys, cataloging 378,280 "Path-C" anomalies from a parent sample of 37.3 million sources. The scale of this work is impressive, and the introduction of a pixel-and-catalog hybrid "Native-Trained Novelty Fraction" is highly innovative.

However, the manuscript currently suffers from a critical conceptual issue regarding its anomaly rate and contamination control. An anomaly fraction of ∼1.01% (378,280/37,300,000) is astronomically high for true physical or spectral peculiarities. Without a rigorous, quantitative assessment separating instrumental/processing artifacts from astrophysical anomalies, the catalog risks limited utility for downstream statistical analysis. The manuscript requires structural changes, clearer mathematical definitions, and systematic validation before it can be recommended for publication.

2. BLOCKERS (Must fix before publication)
Blocker 1: Artifact Contamination and Selection Function

Location: Section 4.2 (Source Selection) and Section 5.1 (Catalog Statistics)

The Issue: A detection rate of over 378,000 anomalies suggests the sample is significantly contaminated by data artifacts (e.g., diffraction spikes, cosmic ray residuals, satellite trails, optical ghosts, and cross-matching edge-cases near chip boundaries). The paper does not provide a quantitative purity versus completeness metric for the "Path-C" sample.

Proposed Fix: The authors must perform a visual inspection or high-fidelity automated verification on a representative, randomly selected subset (minimum N=1,000) of the Path-C anomalies. They must explicitly calculate the fraction of true astrophysical anomalies versus pipeline/instrumental artifacts and include a table breaking down these contamination modes. If the artifact fraction exceeds a few percent, a secondary filtering step must be implemented to clean the public catalog.

Blocker 2: Mathematical Formalization of "Path-C" and "Novelty Fraction"

Location: Section 3.2 (Pipeline Architecture)

The Issue: The text references "Path-C" extensively as the source of these unique anomalies, but it reads more like an internal software tracking label than a reproducible scientific methodology. The precise algorithmic logic, threshold cuts, and features feeding into Path-C are missing.

Proposed Fix: Provide a clear, self-contained algorithmic flowchart or a step-by-step mathematical definition of the Path-C filtering sequence. Define exactly how the "Native-Trained Novelty Fraction" (η
novel
	​

) is computed from the underlying loss function or latent space density of the network. Write out the explicit equation for η
novel
	​

 to replace the qualitative prose.

3. MAJORS (Should fix)
Major 1: Cross-Survey Flux Calibration and Systematics

Location: Section 2.3 (Data Heterogeneity and Cross-Matching)

The Issue: Combining photometry and map patches across heterogeneous surveys introduces systematic offsets due to varying filter transmission curves, aperture definitions, and varying seeing conditions. The paper states that these are absorbed by the network, but unmodeled systematic variations across the sky can easily mimic spectral anomalies.

Proposed Fix: Provide a diagnostic plot showing the spatial distribution of the anomaly density in Galactic coordinates. If there are clear imprints of survey footprints, chip geometries, or dust extinction boundaries (E(B−V)), the authors must apply a correction or introduce a penalty term to the novelty score to desensitize it to spatial survey boundaries.

Major 2: Training Set Leakage and Bias

Location: Section 3.4 (Self-Supervised Training Regime)

The Issue: The native-trained model utilizes map patches extracted from the same parent dataset. It is unclear how the authors prevent the model from treating common local background fluctuations (e.g., diffuse interstellar bands, cirrus, or varying sky backgrounds) as global anomalies, or conversely, over-fitting to clusters of real anomalies.

Proposed Fix: Clarify the exact train/validation/test split mechanism. Demonstrate via a control sample (e.g., injecting known standard stars or simulated synthetically altered spectra/patches) that the novelty fraction responds linearly to anomalous features and remains flat for normal sources across different background density fields.

4. MINORS (Polish)
Minor 1: Inconsistent Notation for Novelty Metrics

Location: Section 3.5 vs. Section 5.2

The Issue: The manuscript interchangeably uses η
N
	​

, f
novelty
	​

, and NF to describe the Novelty Fraction.

Proposed Fix: Harmonize the notation throughout the paper. I suggest sticking strictly to η
novel
	​

 for clarity.

Minor 2: Astrometric Tolerance Thresholds

Location: Section 2.4 (Cross-Matching Protocol)

The Issue: The authors state that cross-matching between survey catalogs utilizes a "dynamic matching radius," but they do not list the absolute floor or ceiling values used for this radius. Mismatched coordinates are a prime source of false "spectrally unusual" objects.

Proposed Fix: Explicitly state the minimum and maximum astrometric matching tolerances (in arcseconds) used in the text.

5. Strengths

Computational Scale: Processing 37.3 million sources and associated map patches through a unified multi-survey pipeline represents a powerful application of modern machine learning to wide-field astronomical datasets.

Multi-Modal Architecture: The decision to combine raw image/map patches directly with processed catalog photometry prevents the information loss typical of pipelines that rely purely on summary statistics.

Extensive Catalog Resource: Once properly calibrated and purged of instrumental artifacts, this catalog of hundreds of thousands of unusual objects will serve as an invaluable resource for targeted follow-up spectroscopy using facilities like DESI, SDSS-V, or 4MOST.
