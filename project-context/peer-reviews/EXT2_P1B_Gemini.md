# EXT2 P1B — Gemini in-thread delta review
**Provider**: gemini.google.com · 3.5 Thinking
**Chat**: https://gemini.google.com/app/2ba6d99c84794eb7
**PDF**: paper1b_mcmc_companion_v1B.0.56.pdf · **Harvested**: 2026-06-10 ~21:30 PDT
**Mode**: same-thread re-review (closure verification + fresh pass + updated verdict)

---

Gemini said
Referee Report

Journal: Monthly Notices of the Royal Astronomical Society (MNRAS)

Manuscript Title: Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔN
eff
	​

 MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model

Author: Houston Golden

Manuscript Version: v1B.0.56 (Revised)

1. Closure Verification

Following the evaluation of the revised manuscript (v1B.0.56) against the previous referee findings, the verification status of the major items is as follows:

MAJOR 1: Unquantified Systematic Pairing Bias (Planck NPIPE high-ℓ + 2018 low-ℓ/lensing mixture) STATUS: NOT ADDRESSED. The text in Section III remains unmodified. It explicitly states that a release-pairing swap test with PR4-consistent low-ℓ and lensing counterparts was not performed, leaving any pairing-induced systematic bias on the headline parameters unquantified at the quoted precision.  
PDF
+ 1

MAJOR 2: Status of the Accumulating Planck-Only Chain STATUS: NOT ADDRESSED. The author continues to reference a live, un-converged Planck-only chain (
R
^
−1∼0.05, 114,992 raw samples) across the abstract , body text , and conclusions. It remains explicitly excluded from all summary metrics and tables.  
PDF
+ 4

Note on Polishing Closures

The author has successfully addressed several tracking and transparency limitations highlighted in previous rounds:

CLOSED: Narrative drafting artifacts ("an earlier draft stated...") have been removed from the body and replaced with verified coordinates from the physical parameter grid scan.  
PDF

CLOSED: A clear pedagogical section ("Canonical estimator choice") has been added to Section IV to justify the selection of the unweighted baseline over the inverse-variance-weighted pipeline configuration.  
PDF

CLOSED: The severe column-permutation export bug inside the public parameter_summary.json file has been fully disclosed, documented, and corrected with a verified mapping file.  
PDF
+ 1

2. Fresh Pass (New Findings)
Majors (Should Fix)
Sec. III, Page 4, Paragraph (e) — Statistical Velocity Inflation via Naive SN Catalog Product Likelihood

Context: The author adds an explicit paragraph disclosing that the iter2 MCMC likelihood stack treats the DES-SN5YR and Pantheon+ catalogs as completely independent factors. The text explicitly notes that these catalogs share an approximate 20% supernova event overlap with unique Malmquist-bias corrections and that multiplying them without a cross-survey joint covariance matrix double-weights these shared events.  
PDF
+ 4

Critique: While this disclosure is highly commendable from a transparency standpoint, merely stating a severe violation of statistical independence is insufficient for a peer-reviewed technical verification paper. Multiplying these overlapping likelihood factors artificially shrinks the apparent posterior widths (σ
w
0
	​

	​

, σ
w
a
	​

	​

) and shifts the best-fit point along the supernova distance-modulus degeneracy direction. Because the core cosmological headline of this paper rests on a highly subtle +4.3σ / −3.6σ marginalized tail departure from the standard cosmological constant (ΛCDM) model, an unphysical double-counting of data points directly undermines the statistical validity of that claimed tension.  
PDF
+ 3

Proposed Fix: The author must rerun the iter2 configuration after applying a clean data-selection cut: either remove the overlapping 20% sample from one of the catalogs, or drop one of the duplicate SN likelihood factors entirely to confirm if the canonical quintom-B landscape signature  remains robust under rigorous independent sampling conditions.  
PDF
+ 1

Minors (Cosmetic & Polish)
Appendix C, Page 14, Configuration (iii) — Text Typographical Error

Context: The text introduces the third configuration as: "Configuration (iii) - model-independent firee fit".  
PDF

Proposed Fix: Correct the typographical error "firee" to "free" or "β
free
	​

" to match the surrounding mathematical notation.  
PDF

Table II, Page 17 — Parameter Label Mangling

Context: In the standard cosmology section of Table II, the row label for the Hubble constant contains an uncorrected character glitch: "H
0
	​

 I
0
	​

[km s
−1
Mpc
−1
]".  
PDF

Proposed Fix: Strip the stray "I
0
	​

" string from the row header to restore clean formatting.  
PDF

Table II, Page 17 — Footnote Indexing and Notation Alignment

Context: 1. The "vs ACDM" column for the time-varying dark energy equation of state (w
a
	​

) contains the garbled string entry: -3.60 from 0 (marg.-tailfn; . a).
2. The total χ
2
 row points to a superscript note e (14037.4±5.6
e
). However, the footnotes block directly beneath the table is indexed out of linear sequence using the letters b , e , and d, while note c is entirely absent.  
PDF
+ 4

Proposed Fix: 1. Fix the typesetting text string to read (marg.-tail; fn. a).
2. Sort and re-index the table footnote markers sequentially (a, b, c, d) to ensure accurate alignment with the markdown source labels.  
PDF
+ 3

3. Recommendation

MAJOR REVISIONS

Trajectory Assessment: The manuscript has moved significantly closer to technical completeness through exceptional transparency upgrades, one-sided ΔN
eff
	​

 boundary definitions , and public data-bug closures ; however, it has simultaneously introduced a critical statistical vulnerability by combining overlapping supernova data catalogs as a simple naive product likelihood, which artificially influences its core dark energy tension signatures and necessitates a targeted parameter re-evaluation.  
PDF
+ 4




Thinking

