# P4 R7 — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 32.7s

---

# Referee report – methodology audit  
Tag P4 Round R7  

I list all findings that affect the statistical or methodological solidity of the manuscript.  The identifiers use the requested severity codes (E = ESSENTIAL, M = MAJOR, m = MINOR, N = NIT).

----------------------------------------------------------------------
P4-E1 Sect. IV/Abstract σ values from in-commensurable null models are placed side–by-side  
Quote: “The headline scientific result is a null ℓ = 1 chirality-dipole observable … −0.12σ … The real-space post-TTA Catalog C dipole is +0.43σ … Note: σ values … are not directly comparable across estimators.”  
Problem Even after the caveat the text repeatedly compares σ’s from five different null constructions (label shuffle, pixel shuffle, binomial, bootstrap, look-elsewhere).  In several places (e.g. §VI B, Fig. 8 caption) the numbers are interpreted jointly (“three discriminators that disfavor interpretation (i)”).  This violates requirement 7: σ’s on different scales must not be treated as additive evidence.  
Required fix For every σ that is quoted, add in-line the exact null label (e.g. “+0.43σ[pixel-shuffle]”).  Remove any sentence that combines σ’s from different nulls into a compound significance.  Where joint evidence is needed, convert each result to its two–sided p value and combine with a pre-declared meta-test (e.g. Fisher’s method).

----------------------------------------------------------------------
P4-E2 Sect. VII / Table VI Use of “moment-z” on a visibly non-Gaussian null  
Quote: “data C₁ = 6.55×10⁻⁶ vs null mean 8.0×10⁻⁷ … moment-z +4.84 … empirical-rank pMC = 0.006 (∼ 2.5σ).”  
Problem The distribution of C₁ under the 500 binomial simulations is highly skewed; nevertheless the paper continues to report “+3.64σ” by dividing by the sample s.d.  Calling this a “σ” violates the journal policy that σ implies a Gaussian reference.  
Required fix Drop the “+3.64σ” and “+4.84σ” language entirely.  Quote only the empirical two-sided pMC and, if desired, its Gaussian equivalent Φ⁻¹(1–p/2).  Revise every place where “3.64σ” is interpreted as Gaussian evidence (Sec. IV D, VI G, VIII, Conclusions, Abstract).

----------------------------------------------------------------------
P4-E3 Sect. II B / III C Circular training labels – no independent accuracy statement  
Problem 67.6 % of the training set is CE-ResNet pseudo-labels, yet the only “93.7 % accuracy” figure is measured against the same mixture.  The independent GZ1 cross-match shows only 69.9 % spiral-only accuracy (κ = 0.40).  All statistical floors (0.2 %, 0.75 %) assume an unbiased classifier.  
Required fix  
a) Re-compute the χ² and p values of every cosmological estimator after multiplying the per-pixel variance by the empirically measured dilution factor (1-2ε)² with ε derived from the 69.9 % agreement.  
b) Add an explicit disclaimer that no claim tighter than that dilution floor (≈ 0.63) can be made until an independently-labelled ≥ 10⁵ galaxy set is available.

----------------------------------------------------------------------
P4-E4 Sect. VI C Poisson variance used although authors concede spatial correlation  
Problem All significances are computed with binomial errors √[p(1–p)/N].  The same section admits that “spatial correlations … reduce the effective sample size Neff”.  No quantitative correction is applied.  
Required fix Estimate Neff with a jack-knife or block bootstrap on at least two NSIDE resolutions and propagate the ratio N/Neff into every quoted σ or p.  Supply the resulting corrected numbers in the tables and Abstract.

----------------------------------------------------------------------
P4-E5 Sect. VI C / Abstract Two incompatible “sensitivity floors” are advertised  
Problem The text simultaneously states a 0.2 % Fisher floor and a 0.75 % empirical 50 %-rec-3σ floor, sometimes calling both “minimum detectable”.  Readers cannot tell which is operative.  
Required fix Pick ONE operative threshold (strongly advised: the empirical 0.75 %) and label the 0.2 % value “ideal statistical limit (not achieved here)”.  Purge all statements that use 0.2 % as an actual experimental bound.

----------------------------------------------------------------------
P4-E6 Sect. VI D Edge-on contamination handled only by confidence cuts  
Problem 65 % (later 59 %) of b/a < 0.3 objects still receive CW/CCW labels, yet no mask cut on b/a is applied in the headline analysis.  The authors claim the dipole is invariant, but give no table of fCW vs b/a after the equivariant step.  
Required fix Add a primary analysis that removes all galaxies with b/a < 0.3 (or supply a table demonstrating that their removal changes the dipole < 0.3σ).  Propagate the reduced sample size into the reported Fisher and injection floors.

----------------------------------------------------------------------
P4-M1 Whole manuscript Length is disproportionate to contribution  
54 pages for a single-number null result is excessive.  Recommended maximum: 25 journal pages excluding appendices.

P4-M2 Sect. III F Bias-hardening thresholds are arbitrary (e.g. “must exceed 80 %”) with no justification or power study.  Provide rationale or Monte-Carlo calibration.

P4-M3 Sect. III E Per-galaxy argmax flip rate of 21 % is substantial.  No uncertainty propagation is carried into any hard-label diagnostic except an ad-hoc 1.21× multiplier.  Supply a derivation or switch all secondary plots to soft weights.

P4-M4 Sect. VI G “Template-regressed” exclusion uses a WLS fit with strong multicollinearity yet quotes > 250σ rejections.  This is ill-posed.  Present the condition number and repeat with ridge or drop ill-conditioned columns.

P4-M5 Sect. IX Reproducibility links depend on mutable HuggingFace branches.  Archive the exact Parquet and checkpoint files on Zenodo (DOI) and cite the DOI in the manuscript.

P4-m6 Sect. VI B multiple places Duplicate phrase “per-pixel-shuffle empirical” appears twice in the same sentence – delete redundancy.

P4-m7 Several footnotes refer to “Table ??”.  Update cross-references.

P4-N1 Typo Sec. IV A line 298: “sprial” → “spiral”

P4-N2 Units Table VI caption mixes sr and “×10⁶” without explicitly stating the conversion.

----------------------------------------------------------------------
## Summary recommendation  
MAJOR REVISIONS  

The authors have assembled an impressive data set and their identification of the monopole-mask leakage channel is valuable, but several methodological foundations (independent accuracy, variance inflation, σ–mixing) must be fixed before the result can be considered robust.  Addressing the ESSENTIAL points E1–E6 and the documentation issues listed as MAJOR will bring the paper to publishable methodological rigor.