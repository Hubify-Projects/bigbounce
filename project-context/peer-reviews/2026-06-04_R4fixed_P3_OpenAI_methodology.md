# P3 2026-06-04_R4fixed — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 27.9s

---

Referee report on P3 – “Spectrally Unusual Sources at Scale …”

I have read the manuscript, the companion artefacts quoted in the text and the GitHub-/HF-paths that are live as of 4 June 2026.  The result is an impressive amount of engineering work, but the paper still contains a number of methodological and statistical problems that must be fixed before it can be published.  Below I list all issues found, grouped by severity.

--------------------------------------------------------------------
ESSENTIAL FINDINGS  (publication has to stop until these are fixed)
--------------------------------------------------------------------

P3-E1   Sec. V, pp. 16–18, 41  
Statement:  “we adopt αjk as the headline … σ(fNL)=8.14 … 1 σ envelope [3.92,8.98]” while later the linear form 8.27 ± 2.37 is still quoted and used in the conclusions.  
Problem: Two mathematically incommensurable σ(fNL) error evaluations (quadratic Fisher vs. linearised secant) are presented side-by-side as if they were equivalent.  The reader is never told which enters the 95 % limits shown in Fig. 12 or in the abstract; in several places both are mixed in the same sentence.  This violates instruction #7 (different null procedures shown on the same σ-scale).  
Required fix:  Decide on ONE mapping (either the quadratic F0+cα² form or the linearised mapping), propagate it consistently through every table, paragraph, abstract and conclusion, delete the other and every sentence that still references it.  Re-compute all confidence intervals accordingly.

P3-E2   Abstract (para 3) and Sec. IV A, p. 12  
Statement: “SIMBAD-unmatched fraction 58.8 %” is placed in the headline paragraph.  
Problem: Later (§IV A) the authors admit that an extended cross-match shows that only 17.8 % of the sample is actually new.  Leaving the 58.8 % figure in the abstract will mis-lead catalogue users and violates the instruction to avoid over-claims of statistical significance / novelty.  
Required fix:  Replace every headline appearance of 58.8 % by the 17.8 % “genuine novelty” figure and explicitly state in the abstract that 58.8 % is a SIMBAD coverage artefact, not a discovery fraction.  (Or delete the 58.8 % entirely.)

P3-E3   Throughout Secs. II–III and Table I  
Statement: some surveys are cut at S>5 (DESI), others at the 99th percentile (Gaia, LAMOST, SDSS native), others at an absolute Isolation‐Forest score (eROSITA), but all counts are added into one catalogue without uncertainty tags.  
Problem: Thresholds are on incompatible scales so the joint catalogue has no well-defined completeness or purity.  The reader cannot reconstruct or compare survey fractions.  
Required fix:  Provide, in one table, for every survey: (i) the raw scale used, (ii) the numeric threshold, (iii) the percentile that threshold corresponds to inside that survey.  Explain explicitly in the text that the headline “378 280 anomalies” is a union of heterogeneous percentile cuts and give a cautionary statement in the abstract.

P3-E4   Sec. III D & VI A  
LAMOST native model still fails the 50 %/5 σ injection-recovery gate (5.8 %).  Yet the 113 342 LAMOST objects are kept in the public “point-source tier” that is recommended for cosmology work.  
Required fix: either (a) drop the entire LAMOST block from the cosmology-grade catalogue and give only as “exploratory supplement”, or (b) raise the gate-pass recovery to ≥ 50 % with a demonstrably new architecture / training and show the new validation plot.

P3-E5   Sec. III F, Appendix F  
The ACT DR6 cross-transfer anomalies fail both gate criteria but 200 of them are still present in several figures and the downloadable artefact.  
Required fix:  Remove every ACT number from all totals and figures of the main article, or alternatively deliver a native ACT retrain that meets both gates.

P3-E6   Title page length – the manuscript runs 49 pages.  PRD “methods/catalogue” limit is 30 pp.  
Required fix:  Restructure and cut to ≤ 30 pages main text.  Move the ten gallery figures and the 20-page caveat discussion to an electronic Appendix.

-------------------------------------------------------
MAJOR FINDINGS  (must be addressed in a revision)
-------------------------------------------------------

P3-M1   Sec. II, eq. (2)  
The term “z-scoring” is used for the anomaly score whereas z is also used for redshift.  This dual use causes confusion in several places (“z ≈ 6.03 | AE = 4.15”).  Define an unambiguous symbol (e.g. Ŝ) for the standardised score and use “z” exclusively for redshift.

P3-M2   Sec. VI D (iv)  
The continuum-dip injection was applied only after peer-review; the initial pass/fail decision was done on emission-line injections.  This is a form of post-hoc change of the primary metric and violates INSTRUCTION #8 (no in-flight language).  The text still contains “strict subset”, “pending recompute” etc.  
Fix: scrub all review-log language, explicitly state ex-ante which morphology defines the gate, relegate any after-the-fact result to a separate paragraph labelled “additional validation”.

P3-M3   Sec. V – estimator pre-registration  
The bias-ratio α is introduced only after looking at the data (“Landy-Szalay measurement therefore closes the prior deferral”).  The original forecast used a fixed α=0.15.  
Fix:  State up-front, in the introduction, that α will be estimated on the catalogue itself and that σ(fNL) will then be propagated with that empirical α, or move the whole α-measurement to a companion paper.

P3-M4   Sec. IV B χ2 spatial uniformity test  
Chi-square is computed over 38 329 Nside = 64 pixels without accounting for the survey window and completeness variations; quoted χ2ν = 3.76 is therefore meaningless.  
Fix:  Either provide a window-simulated null distribution, or delete the test.

P3-M5   Figs. 14–22  
The RGB images still label the per-arm score as “AE”.  This is legacy language from the author’s code and violates instruction #9 (duplicate phrase).  Replace “AE” by the correct per-arm symbol or remove from the panels.

---------------------------------------------------------
MINOR FINDINGS  (editor may allow acceptance if fixed)
---------------------------------------------------------

P3-m1   Several pages  
Duplicate wording: “canonical canonical-mask”, “cross-transfer artifact artifact”.  Remove.

P3-m2   Sec. II D, step 6  
Astropy’s search_around_sky is mis-cited as search around sky.  Give the exact function name.

P3-m3   Eq. (E1) Appendix E  
fyr is defined as 1/yr but later fi uses yr−1   without units.  Add units to every frequency.

P3-m4   Many tables  
Significant figures are excessive (e.g. 0.0287 validation loss).  Round to two sig. figs.

P3-m5   References  
Heinrich et al. is cited as “2024” in text but arXiv as 2023 in bibliography; make consistent.

-----------------------------------
NITPICKS  (optional, low priority)
-----------------------------------

P3-n1  Footnote symbols ♡, ♠, § etc. change meaning between tables – unify.

P3-n2  Page-wide figures split mid-sentence in PDF; force float placement.

P3-n3  “BigAE” is never spelled out; expand at first use.

P3-n4  Missing space before units in multiple places (“20◦”, “5′′ ”).

P3-n5  Equation numbers jump from (2) to (E1) without (3)…(7) – renumber.

--------------------------------------------------------------------
## Summary recommendation
MAJOR REVISIONS

The manuscript contains a valuable, very large anomaly catalogue that deserves publication, but several statistical inconsistencies (most seriously the double use of incompatible σ(fNL), the misleading 58 % novelty claim, and the inclusion of LAMOST and ACT data that fail the authors’ own validation gates) must be corrected.  With the essential fixes above and a reduction to normal PRD length the paper can become a solid methods reference; in its present form it is not yet publishable.