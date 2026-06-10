# EXT1 P3 — Gemini 3.5 Thinking referee report
**Provider**: gemini.google.com web app · model **3.5 Thinking**
**Chat**: https://gemini.google.com/app/b10514f2f6e2ff2f
**PDF**: paper3_anomaly_catalog_v3.1.87.pdf (md5 acde55ca) · **Harvested**: 2026-06-10T17:25 PDT

---

Gemini said
Referee Report

Manuscript Title: Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and Native-Trained Novelty Fractions from 37.3 Million Sources and Map Patches   
PDF

Author: Houston Golden (Independent Researcher)   
PDF

Target Journal: MNRAS / Physical Review D / JCAP

Overview of the Work

This manuscript presents an ambitious, unprecedentedly large-scale application of unsupervised deep learning to astronomical anomaly detection. By deploying the BIGAE (Deterministic Autoencoder) architecture across seven major astronomical archives (DESI DR1, SDSS DR18, LAMOST DR10, eROSITA DR1, Planck CMB, Gaia DR3, and NEOWISE) , the author processes 37.3 million data points.  
PDF
+ 4

Following a rigorous "Path-C" native retraining protocol designed to clean cross-survey domain shifts , the final combined catalog yields 378,280 unique anomalies. This breaks down into 378,080 point sources and 200 Planck CMB sky regions. The author leverages this sample for downstream cosmological constraints, primarily targeting primordial non-Gaussianity (f
NL
	​

) through high-redshift quasar (QSO) tracers and evaluating matter-bounce vs. supermassive black hole binary (SMBHB) gravitational wave background signatures via a NANOGrav 15-year dataset fit.  
PDF
+ 4

Recommendation

MAJOR REVISIONS

While the technical scale, pipeline infrastructure, and transparency of this work are exemplary, several critical structural issues—most notably a confessed and irreproducible scoring axis in the eROSITA tier and unmodeled spatial selection functions in the tracer population —prevent immediate acceptance. The paper is acceptable for publication provided the author addresses the following blockers and major methodological points.  
PDF
+ 2

1. Blockers (Must Fix Before Publication)
eROSITA Anomaly Score Axis Irreproducibility

Section/Line: §III E, Paragraph 2; Table I footnotes   
PDF
+ 1

The Issue: The author explicitly states that the published eROSITA threshold axis (0.259) and individual S
BigAE
	​

 values cannot be reproduced or reconciled via any monotone rescaling of the committed raw reconstruction-score artifact. The Spearman correlation between the production scores and the raw artifact is actually negative (ρ=−0.10 across the top 5). While releasing the n=298 membership list ensures reproducibility of the raw sample itself , it completely blocks downstream meta-analyses that require continuous score-weighted stacking or threshold re-derivation.  
PDF
+ 4

Proposed Fix: This is a severe pipeline defect. The author must execute a full re-scoring sweep over the eROSITA dataset using the correct, canonical standardized anomaly score S defined in Equation 2. If computational limits prevent this, the author must withdraw the continuous S
BigAE
	​

 values for eROSITA entirely, replace Table III with verified raw reconstruction scores, and explicitly warn users in the abstract that the continuous eROSITA metric is corrupted.  
PDF
+ 1

Unmodeled Fiber-Assignment Systematics in cosmological Tracers

Section/Line: §III A, Final Paragraph; §V C   
PDF
+ 1

The Issue: The author notes that DESI fiber assignment incompleteness introduces a spatial selection function that could strongly correlate with the anomaly rate if unusual sources preferentially cluster in fiber-collision-dense regions. However, this systematic is completely ignored in the subsequent Fisher information forecasts for f
NL
	​

. Because local density modulates fiber allocation, spatial clustering artifacts will directly inject power into the angular two-point angular correlation function, artificially biasing the Landy-Szalay measurement.  
PDF
+ 2

Proposed Fix: The author must derive a first-order bounding penalty for the f
NL
	​

 Fisher forecast by assigning a systematic error σ
δ
fiber
	​

	​

 to the tracer density. The claim in Table IV item (c) that this is "inert" must be explicitly demonstrated via a mock catalog injection or an angular mask weight correction.

Validation Gate Tautology in NEOWISE Tier

Section/Line: §II D (Step 5); §III H   
PDF
+ 1

The Issue: The injection-recovery gate for NEOWISE passes with a perfect 100% efficiency. However, the text reveals that this test plants synthetic sources at ∣b
ecl
	​

∣>{85
∘
,82
∘
,80.5
∘
} and "recovers" them simply by applying the rigid catalog mask ∣b
ecl
	​

∣[cite
s
	​

tart]<80
∘
. Passing this gate is guaranteed by basic geometric construction ; it validates the mask code logic, but it is entirely non-diagnostic of the anomaly detector's actual sensitivity to infrared anomalies.  
PDF
+ 4

Proposed Fix: Clarify the labeling in Figure 10 and the text. The NEOWISE curve must not be juxtaposed as a parallel sensitivity metric alongside true physical injection tests like the SDSS continuum-dip analysis. Label it explicitly as a "Geometric QA Check" across all figures and tables.  
PDF
+ 4

2. Major Comments (Should Fix)
Deep Scrutiny of the 378,280 Anomalies Headline Arithmetic

The 7-way positional Friends-of-Friends (FoF) deduplication at a 5
′′
 matching radius is mathematically sound and carefully accounted for across the source text:  
PDF
+ 1

The raw sum of per-survey native detections is 388,493 (DESI: 195,829 + SDSS: 77,905 + LAMOST: 113,342 + eROSITA: 298 + Planck: 200 + Gaia: 500 + NEOWISE: 419).  
PDF

The total number of collapsed detections is exactly 10,213, which yields the headline physical object count of 388,493−10,213=378,280.  
PDF

The author's cluster-accounting reconciliation perfectly satisfies the relation:

∑(size−1)=10,213

where 637 multi-survey clusters and 9,576 intra-survey duplicates are successfully resolved.  
PDF
+ 1

The exclusion of ACT DR6 (200 patches, zero positional overlaps) cleanly shifts the input sum from 388,693 to 388,493 and the unique count from 378,480 to 378,280.  
PDF
+ 1

Required Clarification: The author must state explicitly how the spatial boundaries of heterogeneous surveys are treated during deduplication. Because NEOWISE has a broad ∼6
′′
 point spread function (PSF) , a uniform 5
′′
 matching radius acts tightly on infrared sources while remaining conservative for Gaia's sub-arcsecond astrometry. This introduces a spatial boundary effect that should be explicitly identified as an entry constraint in the final catalog format.  
PDF
+ 1

Verification of Fisher-Positivity and f
NL
	​

 Bounds

The cosmological forecasting framework in §V and §VI correctly implements the Fisher-positivity-respecting constraint equation:
  
PDF
+ 3

1/σ
2
(f
NL
	​

)=F
0
	​

+cα
2

The empirical Landy-Szalay two-point correlation on the 5,384 QSO candidates yields a jackknife central estimate of α
jk
	​

=0.19±0.65.  
PDF
+ 2

Because α
jk
	​

 is less than 1σ from a null result (α=0) , propagating the raw central value yields an over-optimistic forecast of σ(f
NL
	​

)=8.14 due to squaring noise bias (E[
α
^
2
]=α
2
+Var(
α
^
)).  
PDF
+ 4

The author properly notes that the de-biased point estimate returns an amplitude of exactly 0, which collapses the forecast back to the standard single-tracer DESI QSO baseline of σ(f
NL
	​

)
std
=8.98 (representing 0% structural improvement).  
PDF
+ 2

The asymmetric 1σ envelope of [3.92,8.98] is a mathematically valid reflection of the convex mapping from the parameter α to σ(f
NL
	​

). However, the text in the abstract and conclusions presents the "9.4% improvement" prominently. This is highly misleading given that the de-biased reality shows zero improvement. The author must rewrite these sections to emphasize the single-tracer baseline limit as the active constraint.  
PDF
+ 4

NANOGrav 15-Year MCMC Interpretation

The fitting of the power-law gravitational wave background (GWB) template to the NANOGrav 15-year ceffyl-style KDE free-spectrum likelihood is computationally solid. The recovered parameters (γ=2.567±0.382 and log
10
	​

A=−14.025±0.380) are cleanly derived.  
PDF
+ 1

The matter-bounce prediction (γ=3.0) sits at +1.13σ and is correctly labeled as marginally consistent.  
PDF
+ 1

The astrophysical SMBHB population reference index (γ=4.33) sits at +4.61σ.  
PDF
+ 1

The Savage-Dickey density ratio yields a Bayes factor B
MB/SMBHB
	​

=7.14×10
3
, signaling a "decisive" statistical preference under a flat prior.  
PDF
+ 1

Critique: The report must strongly caution the author against over-interpreting this result. The standard γ=4.33 index for SMBHB systems is a population-average value derived under idealized circular, unperturbed environments. Environmental effects (e.g., stellar scattering, eccentric binaries) drastically flatten the expected spectrum in the lowest frequency NANOGrav bins. The author must explicitly add a paragraph in §V A highlighting that an environmental-flattened SMBHB model could easily mimic the observed γ∼2.5 slope, meaning this fit cannot be definitively claimed as exclusive support for a matter-bounce cosmology.  
PDF
+ 1

3. Minor Comments and Typographical Polishes
Missing Preprocessing Lineage for Gaia DR3

Section/Line: §II B (Paragraph 3)   
PDF

Comment: The author openly acknowledges that the exact 20-feature production script for the 50,000-source Gaia run was not recovered from committed backups, and its parameters are instead inferred from a 21-feature successor script (gaia_expanded.py). To preserve catalog-grade integrity, the author should explicitly state in the data repository manifest which columns of the Gaia DR3 catalog were ingested to form these 20 features.  
PDF

Clarity of the Multi-Catalog Identification Rate vs. SIMBAD Novelty

Section/Line: §IV A; Figure 6   
PDF
+ 1

Comment: The global SIMBAD-unmatched fraction of 58.8% significantly overstates catalog novelty because wide-field photometric catalogs are rarely ingested into SIMBAD at the individual source level. The deep CDS X-Match sweep of the top-1,000 DESI anomalies against 20 curated all-sky catalogs reveals that 82.2% are known archival sources, yielding a genuine novelty fraction of 17.8%. The text balances this beautifully , but Figure 6's title ("Fraction of anomalies absent from SIMBAD") should be appended with a subtitle pointing directly to the 17.8% genuine novelty baseline to prevent casual readers from misquoting the 58.8% metric.  
PDF
+ 4

4. Key Strengths of the Manuscript

Despite the required revisions, this manuscript represents a major step forward in astronomical data mining:

Scale and Scope: Processing over 37 million unique inputs across spectroscopic, photometric, and microwave regimes establishes a massive benchmark for multi-survey unsupervised machine learning in astrophysics.  
PDF
+ 2

Methodological Transparency: The candid disclosure of pipeline issues—such as the 98% training-bias artifact in the initial cross-transfer LAMOST scan , the structural failures of the ACT cross-transfer gate , and historical text/arithmetic corrections —is an exceptional demonstration of open science and algorithmic reproducibility.  
PDF
+ 4

Successful Domain Mitigation: The "Path-C" rebuild framework convincingly demonstrates how native autoencoder retraining suppresses severe cross-transfer rate inflation (e.g., compressing the false SDSS anomaly tail by a factor of ~6500).  
PDF
+ 3

Astrophysical Discovery Potential: The isolation of 12 highly compelling high-redshift (z=6.0−6.23) quasar candidates exhibiting clean Gunn-Peterson troughs validates the BIGAE latent space as a powerful engine for targeting rare cosmic populations.  
PDF

5. Summary Matrix of Code & Artifact Audits

To ensure strict compliance with journal transparency rules, the following verification checklist reflects on-disk configuration parameters reported in the draft:

Target Survey / Audit Domain	Primary Technical Metric	Code / Script Lineage	Verification Status
DESI DR1	

J
=0.862≥0.70 Jaccard Pass  
PDF
+ 2

	

In-sample 5-fold CV split  
PDF

	

VERIFIED  
PDF
+ 2


SDSS DR18	

Val loss 0.0311; 64% Injection Pass  
PDF
+ 1

	

training_log.json (Patience 5)  
PDF
+ 1

	

VERIFIED  
PDF
+ 1


LAMOST DR10	

21.5x Rate Compression under Native Retrain  
PDF
+ 1

	

recovered_pod_scripts/  
PDF

	

VERIFIED  
PDF
+ 1


eROSITA DR1	

Top-298 Cap on Axis Knee  
PDF

	

r24conf_erosita_axis_sweep.json  
PDF

	

CRITICAL FAULT (Axis corrupted)  
PDF


Planck CMB	

Val loss 0.4437; 100% Injection Pass  
PDF

	

cmb_native_retrain.py  
PDF

	

VERIFIED  
PDF


ACT DR6	

Val loss ≈2.2×10
4
 (Quarantined)  
PDF
+ 2

	

Appendix F Methodological Record  
PDF

	

VERIFIED CLOSURE  
PDF
+ 1

Note: The v3.1.71 cross-vendor review round containing 13 historical findings has been thoroughly audited against the current text. All 13 items are confirmed STALE and have been cleanly resolved via explicit author disclosures and empirical recomputations in the final text. No additional cross-vendor compliance items remain open.  
PDF
+ 3




Thinking

