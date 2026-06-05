# P4 2026-06-04_R2pt — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 28.0s

---

Referee report ‒ Methodology / statistical-rigour audit  
Manuscript: “Survey-Scale Galaxy Chirality …” (P4) Round: 2026-06-04_R2pt  

I have read the 56-page submission, the embedded code paths, and the released artefacts.  Below I list all methodology problems I found, classified by severity.  Line/section numbers refer to the PDF delivered with tag paper4-v1.0.153.

------------------------------------------------------------------
ESSENTIAL (paper cannot be accepted without correction)
------------------------------------------------------------------

P4-E1   §III A, p.7 Non-pre-registered estimator  
 The “declared analysis hierarchy” (i)–(vi) was frozen only after catalogue results existed (v1.0.76).  This violates the requirement that the primary estimator be specified before looking at the data.  
 Fix:  State explicitly that the work is exploratory; remove all “load-bearing” language, or provide a time-stamped, independent pre-registration predating any look at the real data.

P4-E2   Throughout Multiple σ scales inter-compared  
 Different nulls (pixel-shuffle, label-shuffle, binomial-monopole, bootstrap) are routinely quoted in σ units and qualitatively compared (e.g. Abstract lines 11–17; Conclusions §VII).  This mixes incommensurable variances.  
 Fix:  Every σ value must be labelled in the text and in figures with its null class; remove all direct comparisons across nulls or re-express them in p values.

P4-E3   §IV C, Table VI & caption Gaussian moment-z applied to non-Gaussian MC  
 After MASTER, the ℓ=1 null distribution is empirical.  You nevertheless transform the moment (C1-μ)/σ into “−0.122 σ” and use Gaussian p≈0.45.  This is invalid without a goodness-of-fit test of normality.  
 Fix:  Quote only the empirical rank pMC; drop the “−0.122 σ” language or justify normality with a 1-KS test.

P4-E4   §IV D, p.26 & Table VII 500 Monte-Carlo realisations claimed to give 0.4 % precision  
 The leakage null uses N=500 realisations but a 4.8σ tail probability is then quoted.  Tail resolution with 500 draws is ±0.002; the quoted +4.84σ (p≈1.3×10-6) is below MC resolution.  
 Fix:  Increase the MC to ≥50 000 or switch to an analytic variance.

P4-E5   Entire manuscript Internal version-control paths and audit artefacts left in prose  
 >30 occurrences of “pipelines/…/results.json”, “wave_14_nn”, etc.  PRD requires a clean narrative.  
 Fix:  Remove all file-system references from the paper; keep them only in the data-release README.

P4-E6   §VI C, p.36-37 Confusion of half-modulation vs. full amplitude  
 The Fisher floor is derived for A/2 but immediately compared with MC floors quoted for full A, producing inconsistent numbers (0.14 %, 0.2 %, 0.29 %, 0.75 %).  
 Fix:  Use a single amplitude convention throughout; recompute all quoted limits.

P4-E7   §III E, p.10 21 % argmax flip rate ignored in hard-label analyses  
 Hard-label dipole tables (Table X, XVI, XVII) treat labels as error-free.  A 21 % random flip adds 21 %/√N fractional noise and alters every σ.  
 Fix:  Propagate flip noise into every hard-label uncertainty or switch to probability-weighted maps exclusively.

P4-E8   §IV E, Table X & XI Look-elsewhere correction mis-applied  
 Bonferroni factor calculated with “∼15” bins but applied to >75 dependent bins (RA×Dec×confidence).  The resulting “family-wise 2.4σ” is not conservative.  
 Fix:  Re-compute the trials factor with the actual number of tested cells or adopt the max-statistic MC throughout.

P4-E9   Length: 56 pages vs PRD 30-page guidance  
 Much of §II, §III and every code-path footnote is implementation detail better suited to a data-release note.  
 Fix:  Reduce to ≤32 journal pages; move pipeline dumps to online supplementary material.

------------------------------------------------------------------
MAJOR (significant revision required)
------------------------------------------------------------------

P4-M1   Abstract, lines 8-15 Claims a “null ℓ=1 dipole on the analysis subsample mask” while quoting +3.64σ in the same paragraph without specifying different nulls.  
 Fix:  Explicitly state which number is the scientific result and relegate the +3.64σ to a systematics section.

P4-M2   §III F, Table IV Bias tests T2,T4 performed on training split, not on blind data.  
 Fix:  Re-run orientation and perturbation audits on a hold-out of ≥20 000 galaxies unseen during any hyper-parameter tuning.

P4-M3   §VI D, edge-on fraction still 59 % mis-classified as spirals after TTA.  The impact on σ has not been quantified.  
 Fix:  Provide a dipole analysis with all b/a<0.3 galaxies removed; quote the change in the headline σ.

P4-M4   Footnote chains inside captions run to 400+ words, rendering text unreadable.  
 Fix:  Move all long methodological digressions to an appendix.

P4-M5   MASTER configuration (App. VIII) – C1 noise term incorrectly set to 4πfsky/Nspiral without 1/2 factor for variance of a difference of two counts.  
 Fix:  Recompute Cℓ errors with proper shot-noise subtraction.

P4-M6   Sensitivity “falsification criterion” (≥0.75 %, 5σ) ignores 21 % flip noise and 59 % edge-on dilution.  
 Fix:  Derive criterion after including all catalogued systematics or drop the paragraph.

P4-M7   Text repeatedly mixes point-estimate z with empirical-rank p (e.g. “+4.84σ, p=0.006”).  
 Fix:  State either z OR p, not both, unless they are consistent (|Φ⁻¹(p)|≈z to <0.1σ).

P4-M8   Figures 8-13 use different colour scales for the same quantity; legends missing units.  
 Fix:  Harmonise plotting conventions, add sr units to all power‐spectrum axes.

------------------------------------------------------------------
MINOR (should be addressed, editor may decide)
------------------------------------------------------------------

P4-m1   Several duplicate phrases: “canonical canonical-mask”, “pre-MASTER raw pseudo-Cℓ at ℓ = 1” appears twice.  
P4-m2   Many numbers given to 5–6 significant figures (e.g. 0.49735); two are enough.  
P4-m3   Footnote b, Table II: extremely long narrative footnote hampers reading.  
P4-m4   Describe the CE-ResNet overlap in the main text, not only in a footnote.  
P4-m5   The block-bootstrap uses only 1 000 resamples; consider ≥10 000.  
P4-m6   Equation (6) missing factor √fsky in denominator.  
P4-m7   Figures lack north-arrow / coordinate grid.  
P4-m8   “Statistically unambiguous” phrase in §III E is over-statement for 69 % accuracy.

------------------------------------------------------------------
NIT (editorial / typographic)
------------------------------------------------------------------

P4-n1   “p = 0.30 (one-tailed convention is the natural one)” – remove editorialising.  
P4-n2   Occasional ASCII ligatures (ﬂ) rendered as “fi”.  
P4-n3   PACS numbers obsolete – use APS Physics Subject Headings.  
P4-n4   Reference [31] LSST appears twice with different years.

------------------------------------------------------------------
## Summary recommendation  
MAJOR REVISIONS  

The work is potentially publishable after substantial corrections: unify statistical methodology, remove internal artefact paths, pre-register or re-phrase the estimator hierarchy, recompute significances with adequate Monte-Carlo size, and shorten to <32 pages.  At present the multiple σ definitions, non-Gaussian tail estimates, and internal code debris render the manuscript unfit for publication.