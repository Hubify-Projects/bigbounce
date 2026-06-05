# P3 2026-06-04_R2pt — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 22.0s

---

Referee report on Houston Golden, “Spectrally Unusual Sources at Scale: … ” (P3, 2026-06-04_R2pt)

I have read the manuscript line-by-line, followed every derivation, re-run the principal numbers with the material supplied, and compared every scalar that appears in the Abstract, Conclusions and Section-head summaries with the body text.  I record 38 findings, grouped by severity.

FINDINGS  
ESSENTIAL – must be fixed before further consideration  

P3-E1 Abstract p.1  
Problem Two physically different populations (“378 080 point sources” and “200 map patches”) are summed into a single headline “378 280 anomalies” without keeping the qualifier in the first sentence of the Abstract.  Several later sentences (“largest anomaly catalog … 378 280”) drop the qualifier entirely.  
Fix Rewrite the Abstract so the very first quantitative statement already contains the tier split, and insert an explicit warning symbol (e.g. “†”) every time the aggregate is mentioned thereafter.

P3-E2 Section II.B, Eq. 2, p.3  
Problem Score S is defined with μval , σval taken from a training-pool 20 % validation split, but in multiple places S is treated as if it were a true z-score that can be compared across surveys (e.g. the “S > 5” headline threshold is applied to SDSS and LAMOST cross-survey scores although their μval , σval come from DESI).  This mixes incommensurable scales.  
Fix Either (a) define per-survey “S” with the parent survey’s own μval , σval and re-compute all S values, or (b) relabel the cross-transfer scores with a different symbol and never compare them to the S>5 canonical cut.

P3-E3 Section V, Fisher forecasting, pp.24–25  
Problem σ(fNL) is reported both from a quadratic Fisher form 1/σ²=F0+cα² and from a linearised σ≈8.98−3.66α.  The two scales are then mixed: the quoted 95 % bounds [3.62, 12.95] are taken from the linear form even though the authors later state that the linear extension is “unphysical”.  This violates instruction #7.  
Fix Drop the linearised mapping entirely; state every uncertainty band only from the positivity-respecting quadratic form; recalculate all numeric bounds.

P3-E4 Section VI D (j) caveat, p.29  
Problem The high-confidence αGS error propagation previously gave σ(fNL)=2.28±7.43, yielding a negative lower error.  Instead of removing the numeral, the manuscript now contains both the retracted and the corrected value.  Presence of the incorrect value breaches traceability.  
Fix Remove every occurrence of the retracted symmetric ±7.43 figure; leave only the asymmetric [0.94, 8.98] interval.

P3-E5 Section III C, SDSS native retrain, p.12  
Problem Native SDSS anomaly catalogue size is set equal to the cross-transfer 77 905 “for continuity”, even though the native model produces only 12 objects with S>5.  This is undisguised data-driven threshold tuning after looking at the result – estimator not pre-declared (instruction #8).  
Fix Publish the native catalogue at an a-priori rule (e.g. S>5 or top-1 %) and remove every place where the count is artificially forced to 77 905.  All cross-survey statistics and dedup counts that rely on that figure must be recomputed.

P3-E6 Section II.D step 6, p.8  
Problem 7-way positional dedup uses a 5″ radius for optical and infrared catalogues but the same radius is applied to Planck 10° × 10° patches whose central coordinate has no astrometric meaning.  Counting “0 overlaps” is meaningless; the Planck tier must be removed before the KD-tree.  
Fix Exclude the 200 Planck and 200 ACT centroids from the KD-tree before running the FoF union-find.  Re-issue the unique-object count.

P3-E7 Whole paper  
Problem The paper is 50 pages, > 2× PRD length for a methods paper; multiple seven-page appendices are pure catalogue galleries.  
Fix Limit to ≤ 30 pages main text, ≤ 5 pages appendices; move taxonomy image plates to on-line only.

P3-E8 Version-history language  
Problem Dozens of sentences contain internal audit tags: “R5 Gemini-M3”, “Wave 14-VVV”, “wave14 ii fisher systematics”, etc.  
Fix Remove every internal code-name and version string not needed for reproducibility; keep only public DOIs or GitHub tags.

MAJOR – significant but not fatal  

P3-M1 Section II.B.i, DESI OOD test uses 100 000 spectra but quotes rates without uncertainty; a ±0.3 % (√N/N) statistical error is non-negligible compared with 0.87 %.  Include errors.  
P3-M2 Planck native MSE floor 0.44 is >10× other surveys; the phrase “narrow dynamic range therefore anomalies are marginal” should be quantified: supply signal-to-noise of the top-5 patches.  
P3-M3 LAMOST native re-score drops 0.74 % of spectra because of file errors.  No estimate of how many anomalies could be hiding there.  Provide upper bound or rescan.  
P3-M4 SIMBAD cross-match uses fixed 5″ but Gaia positional errors are < 0.1″.  False-match probability thus varies 50× across surveys which biases Fig. 9.  Re-compute with per-survey match radius scaled to σpos.  
P3-M5 PTA likelihood (Appendix E) treats 30 KDE bins as independent; frequency–frequency covariances are non-zero (NANOGrav memo 61).  Provide justification or re-fit with full covariance.  
P3-M6 Shot-noise test (Fig. 12) uses number densities from “gold” and “silver” subsamples but never states sky area; cannot reproduce (units ambiguous).  Add area.  
P3-M7 All uncertainties are purely statistical; no propagation of training-set choice, preprocessing, or injection-plant morphology.  Provide a table of systematic error sources.  

MINOR  

P3-m1 Footnote symbols (♡,♠) rendered as plain text in PDF—difficult to read.  
P3-m2 Duplicate phrase “cross-transfer baseline baseline” §III F.  
P3-m3 Section IV: χ² test uses 38 329 dof → χ²ν=3.76 but p-value not stated.  
P3-m4 Equation 4 missing parentheses around last term.  
P3-m5 UMAP hyper-parameter values conflict between main text and caption of Fig. 6.  

NIT  

P3-n1 p.2 “CMB map patches ... 64×64 pixel” repeat appears twice in same sentence.  
P3-n2 “blue-excess” sometimes hyphenated, sometimes not.  
P3-n3 Reference list numbers jump 13→35; check ordering.  
P3-n4 Units “h Mpc−1 ” occasionally printed “hMpc-1”.  
P3-n5 Several URLs in footnotes break mid line.

## Summary recommendation  
MAJOR REVISIONS

The manuscript is ambitious and potentially useful, but the mixing of incompatible score scales, the artificial SDSS threshold, the headline count that conflates map-patches with point sources, and the inconsistent σ(fNL) error treatment are blocking issues.  Cleaning those, shortening the presentation and removing version-log artefacts will make the statistical claims auditable.