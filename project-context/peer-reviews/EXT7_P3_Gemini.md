# EXT7 P3 — Gemini Thinking (in-thread delta round 7; Gemini = fresh thread; P3_fresh.txt full referee prompt)
**Chat**: https://gemini.google.com/app/8f88d28fa5d8d911
**PDF**: paper3_anomaly_engine_v3.1.102.pdf (60e26e5ec3afcd56) · harvested 2026-06-13 ~03:30 PT
---
Referee Report on Paper 3 v3.1.102

Journal: Physical Review D / ApJS

Title: Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and a Native-Trained Novelty Fraction from 37.3 Million Sources and Map Patches

Author: Houston Golden (Independent Researcher)   
PDF

Date of Review: June 2026

1. Recommendation

MAJOR REVISIONS

This manuscript describes an ambitious, large-scale machine learning pipeline applying a deterministic autoencoder architecture (BIGAE) to execute unsupervised anomaly detection across seven independent astronomical archives. The scale of data processing is commendable, covering over 37 million point sources and cosmic microwave background (CMB) map patches. However, severe reproducibility issues regarding code provenance, intentional retention of pipelines with known machine learning data leakage, and misleading baseline comparisons prevent publication in its current form. The paper requires extensive architectural remediation and data re-verification before it can be accepted as a science-grade community data product.  
PDF
+ 4

2. BLOCKERS (Must Fix Before Publication)
Blocker 1: Complete Irreproducibility of eROSITA Anomaly Scores

Section/Line: §III E , Table IV Caption   
PDF
+ 1

Problem: The author explicitly discloses that the published S
BigAE
	​

 score column for the eROSITA DR1 tier is completely irreproducible. A sweep over 16 separate monotone rescalings and multiple Isolation Forest retrains failed to reconcile the published 0.259 threshold or recover the score axis. The author notes that "the production axis is unrecoverable as a matter of provenance" due to an uncommitted post-hoc code modification. Distributing a data table where a core science column cannot be algorithmically verified from raw files violates basic journal standards for catalog papers.  
PDF
+ 4

Proposed Fix: The author must completely re-score the 930,203 eROSITA sources using a frozen, version-controlled script from the recovered pipeline. If the original scores are structurally unrecoverable, the S
BigAE
	​

 column must be completely purged from the distributed catalog and replaced with a fully reproducible native score axis, or the eROSITA tier must be scaled back to a verified, binary categorical list.  
PDF

Blocker 2: Machine Learning Data Leakage and Incomplete Tabular Validation

Section/Line: §II B (Tabular-survey feature preprocessing)   
PDF

Problem: For the three tabular catalogs (eROSITA, NEOWISE, Gaia), the feature scaling normalization constants were fit on the full sample rather than strictly on the training split. This introduces downstream information leakage from the validation sets into the training normalizations, which artificially skews the absolute scale of the validation Mean Squared Error (MSE). While an internal robustness check was computed for eROSITA , the author admits that the corresponding checks for the NEOWISE and Gaia tiers "remain queued" because their feature tables only existed on local pod storage. Stating that a practice is retained simply because it is the "committed production state" is methodologically unacceptable.  
PDF
+ 4

Proposed Fix: The author must pause the manuscript submission, execute the queued robustness checks for NEOWISE and Gaia, and update the text with the results. Ideally, the normalization constants for all three photometric catalogs should be entirely refit strictly on their respective training splits to eliminate the data leakage.  
PDF
+ 1

3. MAJORS (Should Fix)
Major 1: Misleading Headline Catalog Comparisons

Section/Line: Abstract , §III A , §VI E , §VII   
PDF
+ 3

Problem: The paper frequently highlights that its DESI-only anomaly subset represents a massive "∼73× increase" over the Liang et al. single-survey benchmark. However, as revealed in the deep text of §III A, this is a highly unequal comparison. The headline 195,829 DESI count is a raw 1% cut of everything the instrument pointed a fiber at, meaning 98.7% of the identified anomalies reside on unclassified sky-fibers, secondary targets, or calibration exposures. When a strict, like-for-like science-target restriction is applied to match the benchmark's target class, the count drops to 2,468 clusters, which is actually a slight decrease (≈0.9×) relative to prior work. Featuring the 73x metric so prominently in the abstract and conclusions without adjacent qualification is misleading.  
PDF
+ 4

Proposed Fix: Revise the abstract and the final conclusions to explicitly state alongside the 73x figure that on a true like-for-like science target basis, the catalog yields ≈0.9× the size of prior single-survey catalogs.  
PDF
+ 1

Major 2: Conflated Metrics in Injection-Recovery Gates

Section/Line: Abstract , §II D (Step 5) , §VI D (ii) , FIG. 10   
PDF
+ 4

Problem: The manuscript summarizes its validation framework by stating that "Three injection-recovery gates: 3 PASS... and 3 FAIL-with-diagnostic". However, the text reveals that the NEOWISE 100% pass metric was achieved by planting synthetic sources outside an ecliptic boundary and "recovering" them via the application of a fixed spatial mask. The author acknowledges that this "passes by construction" and is a masking-geometry quality assurance check rather than an actual test of the anomaly detector's signal sensitivity. Grouping a guaranteed geometric sanity check alongside statistical signal-detection tests (like the SDSS and Planck continuum plants) overstates the performance of the machine learning pipeline.  
PDF
+ 4

Proposed Fix: Disentangle the tallies. The abstract and text should state that the pipeline passes 2 out of 5 core detector-sensitivity gates (SDSS and Planck), while passing 1 structural masking QA check by construction.  
PDF
+ 1

4. MINORS (Polish)
Minor 1: Missing Gaia Preprocessing Script Provenance

Section/Line: §II B , §III G   
PDF
+ 2

Problem: The author notes that the exact 20-feature production script for the published Gaia run was lost from backup pod environments and its structure is "lineage-inferred" from a 21-feature successor script . This limits the immediate out-of-the-box reproducibility of the Gaia anomaly rankings.  
PDF
+ 2

Proposed Fix: Add a brief warning note to the online repository's data manifest instructing future researchers on how to safely emulate this specific feature lineage.  
PDF

Minor 2: Explicit Cautious Framing of Equation 1

Section/Line: §II A , §VI C (Limitation 7)   
PDF
+ 1

Problem: Equation 1 defines a standard, unweighted mean-squared reconstruction error (MSE) . As listed later in the limitations section, this lack of inverse-variance noise weighting means low Signal-to-Noise Ratio (SNR) regions contribute noise residuals on an equal footing with bright, high-S/N science features.  
PDF
+ 1

Proposed Fix: Insert a single sentence immediately beneath Equation 1 in Section II.A explicitly noting that the metric is unweighted by inverse variance, preparing the reader for the subsequent noise-stratification discussions.  
PDF

5. Strengths

Despite the necessary revisions outlined above, this manuscript exhibits several clear strengths that make it highly valuable to the community once repaired:

Unprecedented Multi-Survey Scale: The paper demonstrates massive technical proficiency in successfully deploying the deterministic autoencoder architecture across 37.3 million highly heterogeneous astronomical datasets spanning optical spectroscopy, X-ray photometry, and microwave sky maps.  
PDF
+ 4

Exemplary Architectural Transparency: The author avoids the common machine learning pitfall of hiding technical defects. The detailed documentation and retention of the 98% blue-excess LAMOST training bias artifact and the complete quarantine of the ACT DR6 cross-transfer scan provide excellent methodological lessons for future large-scale AI campaigns.  
PDF
+ 4

Rigorous Structural Cross-Validation: For the main anchor survey (DESI), the author enforces highly stringent internal validation metrics, utilizing a 5-fold held-out cross-validation Jaccard overlap (
J
=0.862) alongside an independent out-of-sample NOIRLab SPARCL test to confirm that the extreme-tail anomaly rankings are stable and robust against model-seeding variations.  
PDF
+ 2
