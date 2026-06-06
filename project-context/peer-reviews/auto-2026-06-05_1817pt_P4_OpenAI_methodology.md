# P4 auto-2026-06-05_1817pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (9744 chars)
**Wall time**: 475.1s

---

Referee report (Physical Review D – Methods)

I carefully read all 10 pages, checked the arithmetic, recomputed quoted significances where possible from the numbers provided, and examined the internal consistency of the estimators, null procedures, mask definitions, and Monte Carlo configurations. Below I list all issues found, classified by severity, with page/section references, exact offending text, and required fixes.

ESSENTIAL

- ID: P4-E1
  - Location: Table III (page 5), Section IV.C–D text surrounding the table
  - Problem: The “Significance (σ)” entries in Table III are not arithmetically consistent with the displayed Cℓ and σnull values, and the table omits the null mean ⟨Cnull⟩ used to compute the z-scores. Example: for ℓeff = 4, Cℓ = 3.210×10^-6 and σnull = 0.804×10^-6 would give z ≈ 3.99 if referenced to zero mean, not +6.097 as listed; for ℓeff = 9, Cℓ = −0.248×10^-6 with σnull = 0.574×10^-6 gives z ≈ −0.43 if referenced to zero, not +2.232.
  - Required fix: Provide, in the table, the null means ⟨Cnull⟩ for each bandpower, and define the exact z-score as z = (Cmeas − ⟨Cnull⟩)/σnull. Recompute and replace all “Significance (σ)” values accordingly. If a non-Gaussian or rank-based significance is used, make that explicit and report the corresponding empirical p-values alongside.

- ID: P4-E2
  - Location: Appendix C, item c (page 8); also Section VI (page 6)
  - Problem: Conceptual confusion and double-counting of Look-Elsewhere Effect (LEE). The text presents a direct MC look-elsewhere pLEE ≤ 10^-4 for the hemisphere scan (already accounting for scanning across directions), then applies an additional Bonferroni/BH penalty “across ∼650 directions,” concluding the post-LEE significance drops below |σ| < 1. This is methodologically inconsistent: the direct-MC maximum-statistic null already incorporates the directional trials.
  - Required fix: Use one coherent LEE treatment. If you use a direct-MC maximum-statistic null, report only that pLEE (with its finite-MC uncertainty). Remove the second, redundant Bonferroni/BH penalty, or clearly demonstrate that the direct-MC did not account for the same trials (and then fix the direct-MC accordingly).

- ID: P4-E3
  - Location: Section VI.A (page 6)
  - Problem: Unjustified “Fisher Poisson floor” derivation. The paper states “Fisher Poisson floor at 3σ is ∼0.29% full-amplitude (from σ(A/2) ≈ 0.048% at Nspiral = 3,201,160, fsky = 0.46).” No derivation is provided, fsky = 0.46 is not defined elsewhere (masks elsewhere are 0.49005 and 0.659), and σ(A/2) ≈ 0.048% does not follow from the simple binomial σ(A) ≈ 1/√Nspiral ≈ 0.0559% (which would give σ(A/2) ≈ 0.028%).
  - Required fix: Provide a clear derivation of the 0.29% and 0.048% numbers, including how fsky enters the Fisher calculation for the dipole amplitude with the adopted weighting and pixelization. Reconcile the fsky = 0.46 with the previously defined masks or correct it. If this floor is not a simple binomial one but a map-level dipole-fit Fisher forecast, supply the formula, assumptions, and inputs.

- ID: P4-E4
  - Location: Abstract (page 1), Section IV.C (page 4), Table I (page 4), Appendix A (page 7)
  - Problem: Over-precision of “−0.122σ” for the primary MASTER ℓ = 1 estimator with only NMC = 500 null realizations used to estimate σnull. With 500 MC, the relative uncertainty on σnull is O(√(2/NMC)) ≈ 6%, which makes reporting −0.122σ misleadingly precise; the z-score is dominated by MC noise.
  - Required fix: Either (a) increase NMC to at least ~5,000–10,000 for the main headline estimator so that “sub-sigma” significances are meaningfully resolvable, or (b) change the presentation to “consistent with zero within MC noise” and report the finite-MC uncertainty on z (e.g., via bootstrap on σnull). Apply the same standard wherever “<1σ” values are quoted off 500 MCs.

- ID: P4-E5
  - Location: Abstract (page 1), Section IV.D (page 4), Conclusions b (page 6)
  - Problem: Side-by-side juxtaposition of σ values derived from different nulls without a local reminder they are not directly comparable, violating the paper’s own stated convention. For example, in Conclusions b: “+3.64σ … 0.43σ … −0.122σ” appears in one sentence without an explicit qualifier at that juxtaposition.
  - Required fix: At every such juxtaposition, annotate the null/procedure used (e.g., “+3.64σ (canonical post-MASTER, per-pixel-permutation null), 0.43σ (real-space, isotropic bootstrap), −0.122σ (subsample-mask MASTER, permutation null) — not directly comparable”). Alternatively, harmonize to p-values for cross-estimator comparisons.

- ID: P4-E6
  - Location: Table IV (page 5), Section IV.D
  - Problem: The z-value for the pre-MASTER pseudo-Cℓ(ℓ = 1) statistic is inconsistent with the displayed numbers. Data: 1.696×10^-2; Null: (1.685 ± 0.007)×10^-2. z should be (0.011×10^-2)/(0.007×10^-2) ≈ 1.57, not +1.68 as listed.
  - Required fix: Recompute and correct z, or provide more precise numbers (with sufficient significant digits) for the null mean and σ to support +1.68.

- ID: P4-E7
  - Location: Section IV.C, item a (page 4), Table I (page 4)
  - Problem: Inconsistent reporting of the real-space dipole test: “significance 0.43σ (p = 0.30, isotropic-null bootstrap, NMC = 10,000).” A Gaussian z = 0.43 would correspond to a two-sided p ≈ 0.67, not 0.30. If p = 0.30 is from an empirical rank and z = 0.43 is from a moment-based estimate on the same bootstrap, this must be stated.
  - Required fix: Report both statistics consistently from the same null and clarify which is primary. If p is empirical-rank and z is moment-based, label them explicitly and do not imply equivalence. Alternatively, report only empirical p.

- ID: P4-E8
  - Location: Section IV.D (page 4), Appendix A (page 7)
  - Problem: The canonical-mask post-MASTER ℓ = 1 result of +3.64σ is central to the systematics discussion but is not tabulated with its C1 value, σnull, and null mean. Only the z is stated.
  - Required fix: Add a table row explicitly for the canonical-mask post-MASTER ℓ = 1 result, showing C1, ⟨Cnull⟩, σnull, z, mask, fsky, null type, and NMC.

- ID: P4-E9
  - Location: Section VI (page 6)
  - Problem: “+6.48σ pre-MASTER pseudo-Cℓ in the lowest bandpower” (Catalog A) is asserted but no figure/table provides that value; Table III shows +6.097 for ℓeff = 4 (and for equivariant Catalog C post-MASTER), not 6.48 for Catalog A pre-MASTER.
  - Required fix: Provide a table/figure listing the pre-MASTER bandpowers (and their nulls) for Catalog A, including the “+6.48σ” claim, or correct/remove the value.

- ID: P4-E10
  - Location: Table III (page 5), caption and column headers; also Section IV.C and Appendix A
  - Problem: Ambiguity in the units and definition of Cℓ. The table labels “Cℓ × 10^6 (sr)” but other parts report C1 without units; negative bandpowers are listed while “Significance (σ)” is positive even when Cℓ is negative (see P4-E1).
  - Required fix: Define precisely the field normalization and units (e.g., scalar spin-0 with Cℓ having units of field^2·sr), and ensure consistent units across the text/tables. If negative deconvolved Cℓ are possible (unbiased estimators), state that explicitly. Ensure the sign of z follows the sign of Cmeas − ⟨Cnull⟩.

- ID: P4-E11
  - Location: Section IV.D (page 4), first paragraph
  - Problem: Version-history language: “were interpreted in earlier paper versions as …” PRD does not permit internal version history in the body.
  - Required fix: Remove all references to “earlier paper versions,” “earlier drafts,” etc., and restate neutrally.

MAJOR

- ID: P4-M1
  - Location: Table II (page 4)
  - Problem: “Dev. (σ)” values are inconsistent with the provided fractions and N (binomial σ). For Catalog C, (0.4974−0.5)/0.000279 ≈ −9.3, not 9.5 (and the sign should be negative). For Tier A, 0.0079/0.000279 ≈ 28.3, not 28.8. For Tier B, 0.0040/0.000279 ≈ 14.3, not 14.6.
  - Required fix: Recompute and correct the deviations (with sign), and standardize significant figures. State explicitly that σ is the binomial σ = √[p(1−p)/Nspiral], and whether p = 0.5 or p = fCW is used in σ.

- ID: P4-M2
  - Location: Appendix A, item a (page 7)
  - Problem: The weighting Wp = N(p)all (including NS) is adopted for the NaMaster field. If NS fraction varies across the sky (it does), this weighting could couple morphology systematics into the chirality asymmetry map.
  - Required fix: Provide a sensitivity analysis showing the stability of C1 to alternate weightings (e.g., Wp = (N(p)CW + N(p)CCW), uniform Wp, depth-corrected weights), and quantify any changes.

- ID: P4-M3
  - Location: Section II.B (page 2), Section III.B (page 3), Section IV.A (page 3), Section VI.A (page 6)
  - Problem: The dilution factor g = 2a − 1 uses a = 0.6991 from a 234,282-object cross-match, but the independence of this validation set from the training/CE-ResNet pseudo-labels is only asserted. No uncertainty on a is given, nor propagation to the amplitude threshold (~1.88%).
  - Required fix: Document the selection and independence of the 234k cross-match sample, give the statistical uncertainty on a, and propagate that uncertainty to g and the “true-underlying threshold” amplitude.

- ID: P4-M4
  - Location: Appendix E.a (page 9)
  - Problem: “65.7% of b/a<0.3 objects receive CW/CCW” lacks methodological detail (how b/a was obtained; sample size; selection; uncertainty).
  - Required fix: Provide the data source for b/a, sample size, selection criteria, and statistical uncertainty. If this is derived from DESI Legacy photometry, cite the exact columns and cuts.

- ID: P4-M5
  - Location: Conclusions d (page 6)
  - Problem: “A future survey detecting a chirality dipole at σ > 5 with amplitude ≳ 0.75% at ≥10^7 galaxies would falsify the present null.” The “≥10^7” requirement is not derived anywhere.
  - Required fix: Provide a quantitative forecast linking N, fsky, noise model, and detection threshold that yields ≥10^7, or remove/soften the claim.

- ID: P4-M6
  - Location: Appendix A (page 7), Appendix D.a (page 8)
  - Problem: “C^2 2°” (apodization) is not precisely defined: what is the exact apodization kernel and convention in NaMaster?
  - Required fix: Specify the apodization operator used (e.g., nmt.mask_apodization with apotype='C2' and apodization scale = 2 degrees), and report the resultant fsky change explicitly.

- ID: P4-M7
  - Location: Section VI.A (page 6)
  - Problem: Injection-recovery reporting lacks binomial uncertainty: P(σ > 3) = 0.55 at A = 0.75% with NMC,inj = 100 implies a ±~0.05 statistical uncertainty.
  - Required fix: Report binomial error bars (or credible intervals) on these recovery probabilities, and provide the amplitude grid resolution used.

MINOR

- ID: P4-m1
  - Location: Section IV.A (page 3)
  - Problem: The class fractions (18.78%, 18.99%, 62.23%) sum to 100.00% only to within rounding. Provide consistent rounding (two decimals) and confirm they sum to 100.00%.
  - Required fix: Round consistently and/or add a note on rounding.

- ID: P4-m2
  - Location: Throughout (e.g., Table I page 4; Table III caption page 5; Appendix A page 7)
  - Problem: Inconsistent fsky values for the same mask: canonical mask is reported as 0.49005, 0.490, and 0.491 in different places.
  - Required fix: Use one consistent value (with an uncertainty if needed) and define it once; propagate consistently.

- ID: P4-m3
  - Location: Appendix A (page 7)
  - Problem: Ambiguous wording: “increases σ from +1.85 to +3.64” refers to z-scores, not σ (standard deviation).
  - Required fix: Replace “σ” with “z” or “significance” to avoid confusion.

- ID: P4-m4
  - Location: Section V.B (page 5)
  - Problem: “CE-ResNet achieves cw/ccw = 0.998” is ambiguous (ratio? fraction?). 
  - Required fix: Clarify the metric (e.g., global CW fraction 0.499, or CW/CCW count ratio 0.998).

- ID: P4-m5
  - Location: Appendix A, D (pages 7–8)
  - Problem: Typesetting artifacts like “C 2 2 ◦” and stray spaces in superscripts.
  - Required fix: Correct LaTeX to render “C^2 (2°)” or the NaMaster API equivalent without spacing artifacts.

- ID: P4-m6
  - Location: Table I (page 4)
  - Problem: Null labels (“pp-shuffle”) are shorthand not defined in the main text.
  - Required fix: Define “per-pixel shuffle” explicitly in Methods, and standardize the nomenclature across the paper.

- ID: P4-m7
  - Location: Appendix D.f (page 9)
  - Problem: Reporting “z ≈ −264.5” and “zboot ≈ −18.1” is unusual; magnitude is what matters for disfavouring interpretation (i), sign reflects the direction of residuals relative to a model choice.
  - Required fix: Report |z| and briefly explain the sign convention.

- ID: P4-m8
  - Location: Table II (page 4)
  - Problem: For Tier C, Dev. (σ) lacks sign even though Excess is negative.
  - Required fix: Include the sign for Dev. (σ) to be consistent with Excess.

- ID: P4-m9
  - Location: Section III.A (page 3) and Appendix A (page 7)
  - Problem: “subsample mask (strict-superset)” vs “canonical mask” are used repeatedly with high importance; no figure shows both footprints.
  - Required fix: Add a small figure showing the two masks and their overlap, or provide a URL to a static PNG in the repository.

NIT

- ID: P4-N1
  - Location: Throughout
  - Problem: Inconsistent capitalization: “cw/ccw” vs “CW/CCW.”
  - Required fix: Standardize to “CW/CCW.”

- ID: P4-N2
  - Location: References (page 10)
  - Problem: Minor typesetting artifacts in author names (e.g., “G´eron”).
  - Required fix: Ensure proper LaTeX accent encoding or plain ASCII per PRD style.

- ID: P4-N3
  - Location: Appendix B (page 7)
  - Problem: Mathematical symbols like “|∆⟨pCW⟩|” are jammed; spacing could be improved.
  - Required fix: Adjust LaTeX spacing.

- ID: P4-N4
  - Location: Throughout
  - Problem: Hyphenation inconsistencies: “post-MASTER,” “pre-MASTER,” etc.
  - Required fix: Standardize across the manuscript.

- ID: P4-N5
  - Location: Appendix A (page 7)
  - Problem: Mixed capitalization “NaMaster/pymaster.”
  - Required fix: Use “NaMaster (pymaster)” consistently.

- ID: P4-N6
  - Location: Data Availability (page 9)
  - Problem: Informal phrasing around the seed (“seed = 42”) is fine for code but less so in PRD.
  - Required fix: Keep the seed in Methods/Appendix but avoid colloquial tone.

- ID: P4-N7
  - Location: Data Availability (page 9)
  - Problem: “v2026.04” release tag included; acceptable, but PRD prefers archival DOI/Zenodo.
  - Required fix: Consider archiving the code/data with a DOI; cite that DOI.

- ID: P4-N8
  - Location: Section VI.A (page 6)
  - Problem: “A ≈ 0.75% (full amplitude)” could be made explicit as “dipole full amplitude in fCW units.”
  - Required fix: Clarify units/definition inline.

- ID: P4-N9
  - Location: Footnote on title page (page 1)
  - Problem: Ensure the asterisk footnote for email is typeset per PRD style.

Additional length comment
- The paper is dense but not excessively long (10 pages including appendices). No page reduction is required provided the essential corrections are made and clarifying tables/figures are added (one small mask-figure and one corrected table).

Bibliography cross-check
- Years, arXiv IDs, and journal names appear plausible for all cited works. No obvious bibliographic errors detected (final copyedit will handle style).

Abstract vs body consistency audit
- Most headline scalars in the abstract trace to the body. Exceptions that must be corrected: (i) the Fisher floor (0.29%) derivation and fsky = 0.46 need justification (P4-E3); (ii) the +3.64σ canonical ℓ = 1 result must be explicitly tabled (P4-E8); (iii) the real-space dipole 0.43σ vs p = 0.30 inconsistency (P4-E7).

Figures and tables audit
- Table I: broadly consistent; add explicit null names and NMC for each, and include the canonical ℓ = 1 row as per P4-E8.
- Table II: deviance numbers need correction/signs (P4-M1).
- Table III: fundamental inconsistencies (P4-E1, P4-E10).
- Table IV: small arithmetic inconsistency (P4-E6).

## Summary recommendation
MAJOR REVISIONS

The manuscript has a solid methodological focus and presents a careful negative-result analysis with extensive systematics checks. However, there are several essential issues in the statistical reporting that must be corrected before this can meet PRD standards: inconsistent z-scores in Table III; unclear/incorrect LEE handling; an unsubstantiated Fisher-floor derivation with an undefined fsky; over-precision of sub-sigma claims with only 500 MC nulls; inconsistent reporting of p and z; and missing tabulation of a load-bearing canonical ℓ = 1 result. Addressing these, along with the major clarity items and minor fixes listed, will materially improve rigor and reproducibility.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS ONLY (fresh-eyes pass)

ESSENTIAL

- ID: P4-E12
  - Location: Section II.B (page 2)
  - Problem: Training-label counts don’t add up. Listed sources sum to 25,790 (6,637 + 17,153 + 2,000), but the text states “combined training set contains 26,636 images.” The stated fraction “67.6% of training labels derive from CE-ResNet predictions” is also inconsistent: 17,153/26,636 ≈ 64.4%, not 67.6%.
  - Required fix: Reconcile the training-label totals by source (and disclose any additional sources or duplicates removed). Update the CE-ResNet fraction consistently with the corrected totals, and report uncertainties or ranges if applicable.

- ID: P4-E13
  - Location: Section IV.B (page 4)
  - Problem: Inconsistent “monopole” magnitudes and suppression-factor narrative. The text claims a “3.86× asymmetry-suppression factor from raw +2.05% to equivariant −0.53%,” but Table II gives +0.79% (Catalog A) and −0.26% (Catalog C). The numbers 2.05% and 0.53% appear to be in A = 2fCW − 1 units (percent), whereas Table II reports “Excess (%)” in fCW − 0.5 units. This is a unit/definition mix-up presented as a single comparison.
  - Required fix: State explicitly which quantity is being reported each time (A in “A-units” vs. fCW-0.5 in “fCW-units”) and convert consistently. Recompute the suppression factor from matched units and correct the example values (or revise the sentence to avoid cross-unit comparison).

- ID: P4-E14
  - Location: Appendix A (page 7), item a vs item c; also Section IV.C, Eq. (3)
  - Problem: Internal inconsistency in the definition of the asymmetry field Ap. In Section IV.C, Eq. (3), Ap = (NCW − NCCW)/(NCW + NCCW). In Appendix A.a, the same spirals-only denominator is stated. But Appendix A.c defines the field with denominator “N(p)total” without clarifying if that includes NS, and gives a mask-mean ⟨A⟩mask,gw = −0.005294 that numerically corresponds to 2(fCW−0.5), i.e., the spirals-only normalization. These two lines in Appendix A contradict each other.
  - Required fix: Unify the definition of the analysis field Ap across the entire paper (spirals-only denominator vs. all-classes denominator) and correct Appendix A.c accordingly. Explicitly define “Ntotal” and ensure all quoted means (e.g., −0.005294) and bandpowers correspond to that consistent field definition.

- ID: P4-E15
  - Location: Section V.A (page 5), Appendix C.c (page 8), Table IV (page 5)
  - Problem: Hemisphere-scan significances appear contradictory across sections with different nulls but no local clarification. Section V.A reports “maximum regional asymmetry is 0.32%,” Appendix C.c quotes a hemisphere maximum of 3.05σ (with a direct-MC LEE), while Table IV reports 3.48×10^-3 (0.348%) and z = +4.42 for a different monopole-only null. These are not cross-referenced locally, making the reader think they conflict.
  - Required fix: At each mention of these hemisphere results, annotate the exact null and statistic used (e.g., “max-hemisphere under per-pixel label-shuffle LEE, vs. monopole+mask null without LEE”), and provide a single summary paragraph explicitly reconciling the 0.32% vs 0.348% and 3.05σ vs 4.42σ numbers.

- ID: P4-E16
  - Location: Appendix C.c (page 8)
  - Problem: Finite-MC p-value reporting is not statistically correct. The text states “direct-MC look-elsewhere pLEE ≤ 10^-4” with N = 10,000 shuffles. With zero exceedances, the standard finite-MC estimate is p̂ = (k+1)/(N+1) = 1/10001 ≈ 1.0×10^-4 (and this estimate has a known uncertainty).
  - Required fix: Report p̂ = (k+1)/(N+1) with a binomial or Clopper–Pearson interval (or a Bayesian credible interval) to reflect finite-MC uncertainty. Avoid stating “≤ 10^-4” without qualification.

- ID: P4-E17
  - Location: Abstract (page 1), Section IV.D (page 4)
  - Problem: Ambiguous p-to-z mapping. “pMC = 0.030, i.e. ≈ 1.9σ Gaussian-equivalent” is ambiguous: 0.030 corresponds to z ≈ 2.17 (two-sided) or z ≈ 1.88 (one-sided). The sidedness is nowhere specified.
  - Required fix: Specify whether p-values are one- or two-sided and use one convention consistently. If mixing conventions (e.g., rank-based p and moment-based z), say so explicitly at the point of use.

- ID: P4-E18
  - Location: Abstract (page 1), Section IV.C (page 4), caption/Table III (page 5)
  - Problem: Nomenclature error: “MASTER-deconvolved single-mode pseudo-C1.” After MASTER deconvolution, the estimator is no longer “pseudo-Cℓ.” Using “pseudo-Cℓ” post-deconvolution is misleading.
  - Required fix: Replace “pseudo-C1” with “decoupled C1” or “MASTER-deconvolved C1” wherever applicable.

MAJOR

- ID: P4-M8
  - Location: Section VI.A (page 6), Appendix A (page 7), Table II (page 4)
  - Problem: Inconsistent amplitude units for “A” vs “fCW” across the injection–recovery threshold, monopole means, and mask-mean subtraction. The paper alternates between A-units (A = 2fCW − 1) and fCW-units (“Excess (%)” in Table II) without always stating which is used. This impacts the interpretation of the 0.75% injection threshold, the reported ⟨A⟩mask,gw = −0.5294%, and the “−0.26%” Catalog C excess.
  - Required fix: Declare a single canonical amplitude convention for all percentages in the paper, or explicitly annotate each occurrence as “A-units (percent of A)” or “fCW-units (percent of fCW − 0.5).” Recompute and restate the key amplitude claims (including the 0.75% threshold and any “percent” monopole values) under the chosen convention.

- ID: P4-M9
  - Location: Table IV (page 5), Appendix C.c (page 8)
  - Problem: Sign reporting for z-scores is inconsistent or confusing for correlation diagnostics (e.g., “σ = −2.89,” negative σ). The magnitude is what carries the detection strength; the sign reflects an arbitrary template orientation.
  - Required fix: Report |z| for detection strength and, if retaining signed z, give a one-line note on the sign convention (e.g., sign indicates anti-alignment with the template). Apply this consistently to all reported z-scores in cross-spectra and regressions.

- ID: P4-M10
  - Location: Appendix A (page 7), “Monopole subtraction reduces decoupled C1 … increases σ from +1.85 to +3.64”
  - Problem: The supporting C1 numbers for the canonical-mask post-MASTER case (leading to +3.64) are not shown elsewhere, and the 10× difference in C1 scale between the subsample-mask (1.494×10^-6) and canonical-mask text (≈1.5×10^-5) can’t be audited without a canonical-mask table row.
  - Required fix: Add a canonical-mask ℓ = 1 table row with C1, ⟨Cnull⟩, σnull, z, mask, fsky, null type, NMC (this complements P4-E8 but is specific to reconciling the Appendix A values).

- ID: P4-M11
  - Location: Table III (page 5), caption footnote “Joint χ2/dof (38 bandpowers) = 161.2/38”
  - Problem: The χ2 computation lacks the necessary details to be reproducible: which bandpowers (list or ℓ-range), what covariance (diagonal from MC? full covariance?), and what binning (single-ℓ or grouped)?
  - Required fix: Specify the bandpower set used for the χ2 tally, the covariance estimator (including whether off-diagonals are included and how many MCs built it), and the binning scheme.

MINOR

- ID: P4-m10
  - Location: Data Availability (page 9)
  - Problem: Repository URLs include stray spaces or broken tokens (“dataset s/…”, “galaxy- chirality- catalog”, “gala xy-chirality-v2”), which renders them invalid.
  - Required fix: Correct all URLs (no spaces, exact repository paths). Consider providing short, permanent links or DOIs.

- ID: P4-m11
  - Location: Table I (page 4), estimator (i); Section IV.C.a (page 4)
  - Problem: The real-space dipole row lists “Mask: none,” but the method uses a HEALPix footprint with a >10-spirals pixel threshold. “None” can be misread as full-sky coverage.
  - Required fix: Replace “none” with an explicit description (e.g., “footprint pixels with ≥10 spirals at NSIDE=64; fsky ≈ [value]”).

- ID: P4-m12
  - Location: Appendix B.d (page 7), Table V
  - Problem: The calibration test T7 is ambiguous: “qualitative, < 50% at confidence > 0.9” is unclear (what quantity is <50%?).
  - Required fix: Define the calibration metric precisely (e.g., expected calibration error or reliability curve criterion) and restate the threshold and outcome in quantitative terms.

- ID: P4-m13
  - Location: Section V.A (page 5) vs Table IV (page 5)
  - Problem: “maximum regional asymmetry is 0.32%” vs Table IV’s hemisphere max|A| = 3.48×10^-3 (0.348%). The small but noticeable mismatch invites confusion.
  - Required fix: Use one value consistently (preferably the precise 0.348%), or explain the rounding and whether the two numbers refer to identical scans.

NO OTHER CLASSES OF NEW ISSUES FOUND

- Arithmetic: Additional inconsistencies beyond those already flagged are limited to the training-label totals (P4-E12), the monopole percentages/suppression-factor (P4-E13), and the hemisphere 0.32% vs 0.348% (P4-m13).
- Figure-caption vs body-claim: No figures were provided; no new findings here.
- Equation dimensional consistency: Equations are dimensionless or probabilities; no unit-mismatch beyond the A vs fCW convention problem (P4-M8).
- Internal cross-references: No new broken refs found beyond items already flagged.
- Null comparability: Additional local juxtapositions are captured in P4-E15 and P4-E17.
- Abstract faithfulness: New issues centered on p-to-z mapping and canonical ℓ=1 tabulation are covered by P4-E17 and P4-M10.
- Unsupported novelty claims: None new beyond prior pass.
- Unquantified hedges: None newly detected.
- Appendix vs main mismatch: The Ap denominator contradiction (P4-E14) is new and material.
- Stale numbers: The 0.32% vs 0.348% and the 2.05% vs 0.79%/0.53% indicate likely stale or cross-unit numbers; both are now flagged.