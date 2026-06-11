# EXT3 P1B — Gemini in-thread delta review (round 3)
**Provider**: gemini.google.com · 3.5 Thinking
**Chat**: https://gemini.google.com/app/2ba6d99c84794eb7
**PDF**: paper1b_mcmc_companion_v1B.0.57.pdf · **Harvested**: 2026-06-11 ~02:50 PT

---

Gemini said
Referee Report

Journal: Monthly Notices of the Royal Astronomical Society (MNRAS)

Manuscript Title: Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔN
eff
	​

 MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model

Author: Houston Golden

Manuscript Version: v1B.0.57

1. Closure Verification

Following a comprehensive review of the updated manuscript (v1B.0.57), the verification status of the core issues identified in previous iterations is as follows:

Original Major Findings

MAJOR 1: Unquantified Systematic Pairing Bias (Planck NPIPE high-ℓ + 2018 low-ℓ/lensing mismatch) STATUS: NOT ADDRESSED. The text in Section III remains identical to the previous version. The author explicitly states that a release-pairing swap test has not been executed and that any systematic bias induced on the headline parameters (ΔN
eff
	​

,H
0
	​

,S
8
	​

) remains unquantified at the quoted precision. While acceptable as an explicitly labeled limitation, it remains an open systematic gap.  
PDF
+ 1

MAJOR 2: Retention of the Un-converged, Accumulating Planck-Only Chain STATUS: NOT ADDRESSED. The manuscript continues to track the live, un-converged Planck-only chain (
R
^
−1∼0.05, 114,992 raw samples) in the abstract narrative , Section III , and Conclusions. This run remains excluded from all summary statistics and tables, serving only as a status indicator rather than active technical verification material.  
PDF
+ 4

Tracking and Documentation Upgrades

CLOSED: The raw sample discrepancy has been resolved by directly auditing the sample logs, correcting the total from 176,840 to 176,240, and accurately syncing all secondary parameter estimation files.  
PDF
+ 1

CLOSED: The column-index permutation export bug within parameter_summary.json has been thoroughly documented via an explicit verification warning note in the text and corrected via parameter_summary_CORRECTED.json.  
PDF
+ 1

CLOSED: Narrative drafting markers have been expunged in favor of direct physical coordinates and grid-scan trajectories.  
PDF

2. Fresh Pass (New Findings)
Majors (Should Fix)
Sec. III.e (Page 4) & Table II (Page 17) — Covariance Neglect in Overlapping Supernova Catalog Likelihoods

Context: The author discloses that the iter2 MCMC likelihood stack combines both the DES-SN5YR and Pantheon+ collections as independent, factorized likelihood expressions. The text notes that these catalogs share roughly 20% of their core supernova events, which are subject to different Malmquist-bias corrections by the respective teams.  
PDF
+ 3

Critique: Multiplying overlapping datasets as simple independent likelihood factors without a cross-survey joint covariance matrix represents a notable statistical error. It double-counts the shared 20% sample, artificially deflating the posterior parameter widths (σ
w
0
	​

	​

,σ
w
a
	​

	​

) and altering the trajectory of the combined constraints. Because the primary cosmological conclusion of this paper relies on a highly sensitive tail departure from the standard model (+4.3σ for w
0
	​

 and −3.6σ for w
a
	​

), an uncorrected overlap directly undermines the precision of the claimed tension significance.  
PDF
+ 2

Proposed Fix: The author should perform a validation rerun of the iter2 chain with a clean dataset selection: either remove the duplicate 20% event overlap from one catalog or drop one of the duplicate supernova likelihoods entirely to prove whether the dark energy parameter tension holds up under independent sampling conditions.

Minors (Cosmetic & Polish)
Appendix C (Page 14, Configuration iii) — Typographical Error

Context: The subsection header contains a text glitch: "Configuration (iii) - model-independent firee fit".  
PDF

Proposed Fix: Correct the typo "firee" to "free" to read "model-independent free fit".

Table II (Page 17) — Typographical Glitches and Formatting Artifacts

Context: Table II contains several minor text extraction/typesetting anomalies:

The row header for the Hubble constant contains a duplicate entry: Standard cosmology: $H_{0}$ $I_{0}[km~s^{-1}Mpc^{-1}]$.  
PDF
+ 1

The "vs ACDM" column for w
a
	​

 reads: -3.60 from 0 (marg.-tailfn; . a).  
PDF
+ 1

The goodness-of-fit row contains a Cyrillic character artifact in the CMB channel label: Xомв instead of XCMB.  
PDF
+ 1

The total χ
2
 notation points to a superscript note e (14037.4±5.6
e
), but the table footnotes block directly beneath uses an un-alphabetized layout sequence starting with note b.  
PDF
+ 1

Proposed Fix: Clean the table strings to remove the stray $I_0$ text, correct the formatting to (marg.-tail; fn. a), change Xомв to standard Latin characters, and sequentially re-index the table footnotes (a, b, c, d).

3. Recommendation

MAJOR REVISIONS

Trajectory Assessment: The manuscript has steadily progressed toward full technical reproducibility through highly transparent data-bug disclosures and strict chain synchronization; however, the explicit introduction of a non-independent product likelihood across overlapping supernova catalogs introduces a statistical flaw that risks overstating the model's dark-energy extension significance, requiring a targeted parameter re-evaluation before acceptance.




Thinking

