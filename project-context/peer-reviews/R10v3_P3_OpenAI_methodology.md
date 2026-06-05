# P3 R10v3 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `o3-2025-04-16`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high
**Wall time**: 77.9s

---

Referee report on “Spectrally Unusual Sources at Scale: A Multi-Survey Catalog …” (20-page v3.1.75 submission to Phys. Rev. D)

I have audited every scalar, equation, ratio and figure in the paper for internal arithmetic, statistical validity and methodological transparency.  Findings are grouped by severity.

-------------------------------------------------------------------------------
ESSENTIAL (must be fixed before the manuscript can be considered)
-------------------------------------------------------------------------------

P3-E1   Sec. V, p. 10.  Fisher forecast arithmetic error  
  • Text: “inserting this into the Fisher-positivity-respecting form 1/σ(fNL)² = F₀ + c α² … gives … σ(fNL)=8.14 … (7.9 % improvement consistent with no improvement).”  
  • Problem: With the published F₀ = 1/8.982 = 0.1113 and c = 0.0747 the insertion α = 0.19 gives  
     1/σ² = 0.1113 + 0.00270 = 0.1140 ⇒ σ = √(1/0.1140)=2.96, not 8.14.  
    If, instead, σ is intended in the same units as the baseline σ_std = 8.98, then F₀ must be 1/σ² = 1/8.982² = 0.0124, not 0.1113.  The published numbers are mutually incompatible and the quoted 7.9 % improvement should be ≈1 %.  
  • Fix: Re-derive the Fisher block, state unambiguously whether F₀ = 1/σ or 1/σ², recalculate σ(fNL) and the percentage improvement, and update every place where the 7.9 % figure is quoted.

P3-E2   Abstract & Sec. V, p. 10.  Confusion of σ units propagates throughout  
  • The baseline “single-tracer σ(fNL)_std = 8.98” is dimensionally inconsistent with F₀ = 1/8.982 used in Eq. (…)  (see E1).  Every downstream envelope (e.g. “[3.92, 8.98]”) inherits the same error.  
  • Fix: Propagate the corrected Fisher algebra globally (abstract, conclusions, Table IV, Fig. 8, Appendix C).

P3-E3   Sec. IV A, p. 9.  “Genuine novelty fraction = 17.8 % … SIMBAD-unmatched = 58.8 %” juxtaposed without warning  
  • The paper requires, per journal policy, an explicit statement each time heterogeneous “novelty” metrics are placed side-by-side that they are not directly comparable (§8 of the review instructions).  The first paragraph of IV A does this correctly, but the abstract and Fig. 5 caption juxtapose the two percentages with no disclaimer.  
  • Fix: add the same explanatory caveat in the abstract and wherever the two figures appear together.

P3-E4   Sec. II D, p. 3.  Training-sample leakage  
  • The DESI DR1 autoencoder is scored on the 47 000 spectra that were used for training.  Although k-fold Jaccard is provided, this still violates standard unsupervised OOD protocol and the leakage is not disclosed in the abstract.  
  • Fix: (i) state prominently in abstract and method that the production DESI scores include the training set; (ii) supply an OOD σ(fNL) forecast using the 103 k hold-out set or re-score the full catalog with a model that was not trained on it.

P3-E5   Sec. III C, p. 5.  SDSS threshold S ≥ 0.1060 (top-1 %) is only 0.11 σ above the mean  
  • At such a low threshold >10 % of the training distribution are by definition “anomalous”.  This contradicts the claim that the detector isolates outliers and undermines the cross-survey comparison.  
  • Fix: justify statistically why 0.11 σ constitutes an anomaly or raise the cut to a demonstrably out-of-distribution regime (e.g. S ≥ 3 or percentile ≥ 99.9).

P3-E6   Multiple sections.  Version-history language inside main text  
  • “v3 native-PDF cross-vendor review”, “v3.1.75”, “R7”, “R8”, “Path-C-final” appear in body and figure captions.  
  • Fix: remove all internal revision tags; journal policy forbids exposing the review history to the archival record.

-------------------------------------------------------------------------------
MAJOR (significant revision requested)
-------------------------------------------------------------------------------

P3-M1   Abstract & Sec. II B.  Number rounding mismatch  
  • 0.87 % of 22 504 897 should be 195 793, not 195 829 (36 objects difference).  Check all later re-uses.  

P3-M2   Table I, footnote ♡, p. 7.  Three incompatible SDSS anomaly counts (77 905, 19 253, 12) are all labelled “headline” at different points.  
  • Provide one clearly defined catalog count; relegate exploratory cuts to appendix.

P3-M3   Sec. III D, p. 6.  “LAMOST native 113 342 … retained as exploratory tier” but the same objects are included in the 378 280 headline unique count.  
  • Either exclude exploratory tiers from the headline or create two clearly separated catalog products.

P3-M4   Fig. 7, p. 13.  The same “FAIL” label is applied to surveys that meet none of the gate criteria (LAMOST 5.8 %, Gaia 5.2 %) and to emission-line variants that were never part of the official gate.  The legend is misleading.  
  • Replot with separate symbols for gate-tests and informal diagnostic variants.

P3-M5   Sec. V A, p. 11.  Bayes factors quoted without prior specification  
  • The prior on γ is said to be flat in [0,7], but the choice on log₁₀A is not given.  Provide full prior listing and numerical evidence for Savage–Dickey ratios.

P3-M6   Whole manuscript.  Page count is excessive for a catalog description; many paragraphs repeat the same caveats verbatim.  
  • Recommend ≤ 15 journal pages; move appendices F and most of §VI D to Supplementary Material.

-------------------------------------------------------------------------------
MINOR (should be addressed, but not publication-blocking)
-------------------------------------------------------------------------------

P3-m1  Abstract.  “seven retained archives … ACT DR6 quarantined” – but ACT figures are still shown in Fig. 1 caption (“8 archives”).  Remove ACT from graphics or mark it “quarantined”.

P3-m2  Table III, p. 8.  Declination column mis-labelled “Dec” but numbers are negative latitudes (should be degrees).  Add units.

P3-m3  Sec. III E, p. 6.  “top-1” should read “top-1 %”.

P3-m4  Eq. (2), p. 2.  The σ_val symbol is not defined until later in the paragraph; add definition immediately after Eq. (2).

P3-m5  Appendix E, p. 15.  The symbol “ρ_i” is undefined.

-------------------------------------------------------------------------------
NIT (cosmetic / typographical)
-------------------------------------------------------------------------------

P3-n1  Multiple pages.  “cross-transfer” is hyphenated and un-hyphenated inconsistently.  
P3-n2  Page 10: “positivity-respecting” appears twice in one sentence.  
P3-n3  References [33] and [34] year mismatch (2024 in body, 2023 in bibkey).

-------------------------------------------------------------------------------
## Summary recommendation
MAJOR REVISIONS

The manuscript presents an impressive multi-survey anomaly compendium, but the core statistical claims (Fisher forecast, improvement percentages) contain algebraic inconsistencies; several catalog thresholds are ad hoc or internally contradictory; and revision-history artifacts remain in the main text.  These essential issues must be resolved and the numerical results recomputed before the paper can be considered for publication in Physical Review D.