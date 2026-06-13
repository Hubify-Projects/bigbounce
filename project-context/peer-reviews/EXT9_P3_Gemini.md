# EXT9 P3 — Gemini (fresh thread; recalibrated prompt; Gemini = fresh thread)
**Chat**: https://gemini.google.com/u/0/app/a2fe3164ed9dfc44
**PDF**: paper3_anomaly_catalog_v3.1.104.pdf · harvested 2026-06-13 13:37 PT
---
Gemini said
Referee Report on Paper 3 (v3.1.104)

Journal: Monthly Notices of the Royal Astronomical Society / Physical Review D (Cross-disciplinary review)

Title: Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and a Native-Trained Novelty Fraction from 37.3 Million Sources and Map Patches

Author: Houston Golden (Independent Researcher)

Executive Summary

The revised manuscript presents an ambitious, unprecedentedly large-scale application of autoencoder anomaly detection across seven major astronomical archives. By pivoting from a naive cross-transfer model to a per-survey native retraining protocol (the Path-C framework), the author has successfully decoupled genuine astrophysical anomalies from severe survey-specific systemic artifacts.  
PDF
+ 2

The scientific value of the work is anchored by its radical transparency. Rather than concealing software engineering legacy debt—such as an unrecoverable eROSITA production score axis or full-sample scaling leaks—the author explicitly quantifies, bounds, and documents these edge cases as part of the public metadata schema. This level of documentation elevates the paper from a simple data release to an instructive methodological blueprint for future wide-field AI pipelines.  
PDF
+ 4

1. Closure Verification of Prior Major Issues

Based on a thorough review of the updated text and tables, the structural blockers from the previous round have been completely resolved:

Title and Structural Framing: CLOSED. The front-loaded headline count of 378,280 unique anomalies is accurately contextualized throughout the text. The explicit point-source vs. CMB map-patch stratification (378,080 point sources + 200 Planck patches) is cleanly executed, directing downstream users to the correct object-level datasets.  
PDF
+ 4

DESI Science Class Recount & Cross-References: CLOSED. The author has systematically updated all three downstream DESI sites. The addition of Table II provides an unambiguous 4-row layout detailing exactly how the different rate denominators operate across the paper. This clarifies that ~98.7% of the raw full-stream DESI anomalies land on non-primary-class filler or sky spectra.  
PDF
+ 4

Statistical Rigor (Wilson CIs & Cramér's V): CLOSED. Wilson 95% binomial confidence intervals are correctly added to the validated-TARGETTYPE per-class breakdown. The raw spatial clustering claims have been safely re-evaluated; reporting a weak but highly significant Cramér’s V≈0.020 preserves the footprint geometry realities without over-claiming astrophysical clustering.  
PDF
+ 2

Exemplar-Set Clarification: CLOSED. The 83 Exemplar-Set anomalies in Figure 1 are now explicitly labeled as a ranked visual-display aid rather than an unbiased density-representative catalog stratum. This maintains a clean boundary with the 116-object GOLD QSO-candidate confidence tier used in the cosmological projections.  
PDF
+ 4

Repository and Data Staging: CLOSED. The public availability paths are fully articulated. The dataset is staged on Hugging Face with an explicit per-survey score_axis/membership_only schema flag to programmatically handle the structural differences between surveys.  
PDF

2. Fresh Pass Findings

This round evaluates the ship-ready text under strict production criteria, checking for internal consistency and proper contextual calibration. No new scientific blockers were identified, but the following points deserve final recognition or submission-day validation:

Methodological Innovations & Safeguards

The eROSITA Resolution: The handling of the non-reproducible 0.259 production score axis is an excellent piece of post-hoc correction. Re-releasing the tier strictly as a fixed top-298 membership list—while providing raw Isolation Forest scores (S
IF,raw
	​

) for comparative cross-validation—safeguards the integrity of the release catalog.  
PDF
+ 4

Fisher Squaring Noise Bias Capture: The cosmological forecasting section handles the Landy-Szalay angular two-point analysis with commendable discipline. Explicitly noting that the central forecast (σ(f
NL
	​

)=8.14) is optimistic due to convex squaring noise bias (E[
α
^
2
]=α
2
+Var(
α
^
)), and choosing to report the unenhanced single-tracer baseline of 8.98 as the true present constraint, insulates the paper from false detection criticisms.  
PDF
+ 3

Environmental GWB Calibration: The addition of the supermassive black hole binary (SMBHB) environmental caveat in Section V.A is highly robust. Clarifying that stellar scattering and eccentric hardening can flatten the expected gravitational wave background spectral index down to γ∼2.5–3 ensures that the decisive Savage-Dickey Bayes factor (B
MB/SMBHB
	​

=7.14×10
3
) is properly framed as a rejection of an idealized circular-orbit model, rather than an outright cosmological detection claim.  
PDF
+ 4

Minor Submission-Day Polish

Active DOI and Citation Swaps: In the final production proofs, the placeholder text pointing to upcoming Zenodo DOIs and concurrently posted companion papers should be systematically updated with active records.  
PDF

3. Final Recommendation

Verdict: ACCEPT.

The author has systematically closed every Major and Blocker item from the prior review cycles. Remaining nuances—such as the lineage-inferred Gaia feature tables or full-sample scaler normalization properties—are thoroughly and honestly caveated within the text as known limitations.  
PDF
+ 1

The paper meets the rigorous scientific standards of both the observational astrophysics and cosmological data-analysis communities. It provides an expansive, structurally validated data archive alongside vital insights into deep-learning domain shifts, making it fully ready for publication.
