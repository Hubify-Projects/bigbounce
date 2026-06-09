# P4 auto-2026-06-09_1042pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (9901 chars)
**Wall time**: 395.3s

---

Referee report on “Survey-Scale Galaxy Chirality with Equivariant TTA: A −0.122σ Subsample-Mask ℓ=1 Null, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)”

Scope of review
I audited the statistical methodology, estimator declarations, internal arithmetic, null procedures, and significance reporting throughout the manuscript, tables, and figures. I explicitly recomputed every quoted percentage and σ that can be derived from numbers given in the text/tables. Findings below are classified as ESSENTIAL, MAJOR, MINOR, or NIT.

ESSENTIAL findings

P4-E1 (Abstract, p.1; Sec. IV.D/Table I/Appendix D, multiple pages): Inconsistent significance metrics for the canonical-mask residual
- Offending text: “post-MASTER canonical-mask direct-MC residual is +3.64σ (z = ∆/σnull; empirical rank pMC = 0.030, i.e. ≈1.9σ Gaussian-equivalent; 500-MC...)”
- Problem: You simultaneously report a z-score of +3.64 (Gaussian p ≈ 2.7×10−4 two-sided) and an empirical rank pMC = 0.030 (≈1.9σ). These cannot both represent the same “significance” without a clear statement that the null distribution is strongly non-Gaussian and that “σ” here is merely a moment-ratio diagnostic, not a tail probability. Using “+3.64σ” throughout the paper (incl. Table I and Sec. VII.b) is misleading in the presence of pMC = 0.030.
- Required fix: Choose and enforce a single significance reporting standard for this estimator. Either (a) report only the empirical rank pMC (and its Gaussian-equivalent z if desired) and stop labeling the moment-ratio as “σ”, or (b) demonstrate (with Q–Q plots or normality tests) that the MC null is close enough to Gaussian for z = ∆/σnull to be interpreted as a tail probability. Update all instances (+3.64σ, +3.57σ, etc.) accordingly, including tables, captions, and the abstract.

P4-E2 (Table II + Sec. IV.B, p.5): Incorrect “Dev. (σ)” values for the global CW fraction
- Offending numbers: Tier A: Dev 28.8; Tier B: 14.6; Tier C: 9.5; with p and σ listed as p ± 0.000279 for all tiers.
- Recalculation (using the provided σ = 0.000279 and differences from 0.5): 
  - A: (0.5079−0.5)/0.000279 = 28.32, not 28.8.
  - B: (0.5040−0.5)/0.000279 = 14.34, not 14.6.
  - C: (0.4974−0.5)/0.000279 = −9.32 in magnitude, not 9.5.
- Required fix: Correct the Dev. column numerics and ensure the quoted uncertainties match the formula you state (σ = sqrt[p(1−p)/N] or 0.5-based approximation—be consistent and state which you actually used). If using rounded σ, do not over-report Dev to 0.1σ precision that the rounding does not support.

P4-E3 (Fig. 2 caption, p.5; Sec. IV.B, p.5): Contradictory “global CW-fraction shift” amplitudes
- Offending text: “the global CW-fraction shift from +2.05% (A) to −0.53% (C) ... (Table II).”
- Problem: Table II shows +0.79% and −0.26%, not +2.05% and −0.53%. These larger numbers are not traceable to any table/figure.
- Required fix: Replace 2.05% and −0.53% with the correct values from Table II, or provide a clear definition of a different statistic that produces 2.05% and −0.53% (and then include those values in a table).

P4-E4 (Sec. IV.C.a, p.6): p-value vs σ inconsistency for the real-space dipole
- Offending text: “amplitude significance 0.43σ (p = 0.30 from the isotropic-null bootstrap, NMC = 10,000).”
- Problem: For a Gaussian benchmark, p = 0.30 (two-sided) corresponds to |z| ≈ 1.04; one-sided p = 0.30 corresponds to z ≈ 0.52. Neither matches 0.43σ. The sidedness is not specified.
- Required fix: Specify one-sided vs two-sided p and recompute the corresponding σ, or provide the empirical calibration mapping |z| to p from the bootstrap. Ensure internal consistency between the reported σ and p.

P4-E5 (Sec. IV.D footnote 1, p.6): “Rerun is in queue”/forward-looking language in the body of the paper
- Offending text: “A parallel rerun on N(p)all-trial draws is in queue ... will be reported ...”
- Problem: Accepted PRD articles must not contain to-be-done items. All supporting computations must be finalized.
- Required fix: Remove forward-looking language and present only completed results. If you need the Nall trial comparison to support a claim, perform it now and include the results; otherwise, delete the claim or qualify it without promising future updates.

P4-E6 (Table III, p.7): Sign of “Significance (σ)” entries inconsistent with measured Cℓ
- Offending numbers: For ℓeff = 9, 14, 19, 24, the measured Cℓ values are negative, yet “Significance” entries are reported as positive (+2.232, +2.626, +2.229, +2.470).
- Problem: If significance is defined as (Cmeas − ⟨Cnull⟩)/σnull, the sign should reflect the direction of deviation. If you instead report |z|, label it as absolute significance and state that convention explicitly.
- Required fix: Define the sign convention explicitly in the table caption and ensure consistency (either provide signed z or |z| with explicit labeling). If signed, fix the signs.

P4-E7 (Table IV vs. Appendix C, pp.8 and 11): Hemisphere-maximum significance inconsistency
- Offending text/numbers: Table IV: Hemisphere max|A| z = +4.42. Appendix C: “maximum asymmetry 3.05σ”.
- Problem: Two different σ values are presented for “hemisphere maximum” without clear distinction of estimator/definition. This is confusing and can be read as internally inconsistent.
- Required fix: Clarify that these are different hemisphere statistics (if so), define both unambiguously (e.g., resolution, scanning grid, weighting, null), and avoid labeling them with the same name without qualifiers. If they are intended to be the same estimator, reconcile the numbers.

P4-E8 (General, e.g., Sec. IV.C.b p.6; Table I p.4): Over-precise σ with small NMC
- Offending examples: “−0.122σ” for ℓ=1 (with NMC=500), “+3.64σ” (NMC=500), etc.
- Problem: With 500 MC realizations, the sampling error on σnull is O(3–4%). Reporting z to three decimals overstates precision. Moreover, for z near zero, MC noise can change the sign/magnitude materially.
- Required fix: Either increase NMC (≥10,000) for all headline nulls or round z to at most two decimals and, better, report the empirical pMC (and its binomial error). State the MC sampling error on pMC (e.g., for 500 MC, σp ≈ √[p(1−p)/500]).

P4-E9 (Throughout; Tables I/III juxtapose multiple σ): Cross-null σ juxtaposition requires explicit local disclaimers
- Problem: Although the abstract notes that σ from different nulls are not directly comparable, the body and tables list multiple σ side-by-side without a repeated local reminder (e.g., Table I puts +0.43σ, −0.122σ, +3.64σ in one column).
- Required fix: Add an explicit footnote to each table and at each textual juxtaposition stating “σ values are defined with different nulls and are not directly comparable,” or use p-values across the board to avoid confusion.

MAJOR findings

P4-M1 (Sec. IV.D footnote 1, p.6): Questionable “trial-count inflation factor” ⟨Nall/Nspiral⟩ ≈ 1.49
- Problem: From totals in Sec. IV.A: Nall/Nspiral = 8.4745M / 3.2012M ≈ 2.65 over the full catalog. Even allowing for mask selection, your own subsample’s weighted sum implies Nmap,weighted/Ncatalog,spiral ≈ 5.5479M / 3.2012M ≈ 1.73, not 1.49. You attribute 1.49 to a per-pixel average, but no evidence is provided.
- Required fix: Provide the exact computed ⟨Nall/Nspiral⟩ over the canonical mask with a clear definition (is it a mean of ratios or ratio of sums?), and update the quoted value accordingly. If 1.49 is correct under your definition, show the computation in the repository and cite the script/commit.

P4-M2 (Sec. VI.A, p.8; Abstract, p.1): A95 ≈ 1.5–2% falsification criterion lacks direct support in the main text
- Problem: You state A50 ≈ 0.75% with some injection details, but A95 ≈ 1.5–2% is not shown as a curve/table and the dependence on fsky, noise, and label accuracy is not presented.
- Required fix: Add a figure/table showing P(>3σ) vs injected A with uncertainty bands, clearly marking A50 and A95 under the exact null used (and the estimator used). Include NMC counts for each amplitude and the binomial error bars on the recovery fraction.

P4-M3 (Appendix A, p.10): Ambiguous apodization notation
- Offending text: “C 2 2° apodization” / “C
2 2
◦ apodization”.
- Problem: Not a standard notation. It likely means cosine-squared apodization with 2° scale, but as written it is unclear.
- Required fix: Replace with an unambiguous description, e.g., “cosine-squared apodization with apodization scale θapo = 2°.”

P4-M4 (Appendix C, p.11): Confusing look-elsewhere treatment
- Offending text: “direct-MC look-elsewhere test ... gives pLEE ≤ 10−4 (rejection) ...; the conservative Bonferroni/BH penalty across ~650 tested directions reduces post-LEE significance to < 1σ.”
- Problem: A “direct-MC look-elsewhere test” already accounts for the LEE if the max-statistic is recomputed in each shuffle. Applying an additional Bonferroni/BH penalty is then double-counting. Conversely, if the direct-MC was not a max-statistic across directions, then it is not a LEE test.
- Required fix: Precisely define the LEE correction: if pLEE is derived from the distribution of the maximum over directions in each shuffle, do not then apply Bonferroni/BH again; simply report pLEE and its error. If not, recompute pLEE with the correct max-statistic null and remove the extra penalty.

P4-M5 (Appendix D.f, p.12): Unrealistic “z ≈ −264.5” and “zboot ≈ −18.1”
- Problem: Reporting hundreds-of-σ tail values from a WLS fit is not meaningful and distracts from the substantive result. These numbers stem from underestimating covariance (hence the later bootstrap inflation).
- Required fix: Do not quote extreme σ values. Report parameter estimates with uncertainties derived from a validated covariance (e.g., block bootstrap), and, if desired, provide a likelihood ratio Δχ2 interpreted with appropriate dof. Remove far-tail σ.

P4-M6 (Figures/Tables referencing “post-MASTER canonical-mask residual” vs “pre-MASTER”): Occasional ambiguity about pre- vs post-MASTER status
- Problem: In Sec. IV.D and Fig. 8 caption you discuss pre-MASTER reproduction (99.3%) and then call the “post-MASTER residual +3.64σ.” Elsewhere the +3.64σ is described as “direct-MC NaMaster at ℓ=1 on the canonical mask,” which is post-MASTER; elsewhere the pre-MASTER pseudo-Cℓ is also discussed with σ. This is easy to misread.
- Required fix: For each σ, explicitly tag “pre-MASTER” or “post-MASTER” and ensure the same estimator and mask are compared like-for-like when discussing changes due to MASTER.

MINOR findings

P4-m1 (Sec. IV.A, p.4): Rounded fractions
- NCW=1,592,107; NCCW=1,609,053; Nspiral=3,201,160; NNS=5,273,371; Total=8,474,531. Spiral fraction 3,201,160/8,474,531 = 37.78% (ok). NS fraction 62.21% (you report 62.23%). Suggest aligning rounding across the paragraph.

P4-m2 (Sec. IV.B, p.5): “3.86× asymmetry-suppression factor”
- Problem: Using the corrected numbers in Table II, the suppression factor from +0.79% to −0.26% is ~3.0, not 3.86.
- Required fix: Update the factor to match corrected values or remove the claim.

P4-m3 (Sec. VI, p.8): “maximum regional asymmetry is 0.32%”
- Problem: No figure/table demonstrating this metric or how “region” is defined (pixel, HEALPix order, hemisphere?).
- Required fix: Define the region and estimator, or provide a reference to the appendix/plot in the repository showing this calculation.

P4-m4 (Appendix A.a, p.10): Dimensional clarity
- You use a galaxy-weighted mask Wp = Nall(p). While fine, explicitly state that the mean-subtracted Ap removes the ℓ=0 coupling in the deconvolved estimate, and that Nmap,weighted is a sum of weights (count), not a galaxy count in an independent data vector, to avoid confusion.

P4-m5 (Appendix B, p.11): Bias-test thresholds
- The acceptance thresholds for T1–T8 are ad hoc. It would help to briefly justify their levels given the 0.75% sensitivity target (e.g., show that failures at those levels would bias the dipole by ≥A50).

NITs

P4-N1 (Throughout): Typographical/notation issues
- Examples: “C
2
2
◦ apodization,” inconsistent hyphenation (“subsample mask” vs “subsample-mask”), sporadic spacing in in-line math (e.g., f
eq
CW).
- Fix: Clean up typesetting.

P4-N2 (Header, p.1): Dated “(Dated: June 2026)”
- PRD will assign dates; not an issue per se, but you can remove to avoid confusion.

P4-N3 (Appendix headings, p.10+): Some appendix captions are long with repeated qualifiers; consider tightening for readability.

Length and focus
For a methods-driven null result, 14 pages is on the long side, especially given several diagnostic sub-analyses that are secondary to the headline null. A concise version focused on:
- clear declaration of the two primary estimators,
- the monopole+mask leakage demonstration,
- the canonical-mask residual diagnostics (just the decisive ones),
- and the injection-recovery curve (A50/A95),
could likely fit in ≲11 pages without loss of scientific content.

## Summary recommendation
MAJOR REVISIONS

The core methodology is promising and the primary null estimator appears sound, but there are multiple essential issues with internal numerical consistency and, most importantly, inconsistent significance reporting for the canonical-mask residual (+3.64 “σ” vs pMC = 0.030) that must be corrected. Additional major clarifications are needed on look-elsewhere handling, apodization notation, the trial-count inflation factor, and the A95 falsification criterion. Once these are addressed and the internal arithmetic/presentation is tightened, the paper could be suitable for PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh pass)

ESSENTIAL

P4-E10 (Sec. III.C vs Fig. 2 caption; method used for Catalog C): D4 vs Z2 TTA inconsistency
- Offending text: Sec. III.C: “We restrict to 2-fold TTA (original + horizontal flip) rather than the full D4 group... Catalog C is the recommended tier...”; Fig. 2 caption: “Test-time D4 equivariant averaging (TTA). For each input... eight D4 transforms... This averaging is the key methodology distinction between Catalog A/B and Catalog C.”
- Problem: The body says Z2-only was used for production; the caption asserts D4 TTA was used and was the “key” step producing Catalog C. These cannot both be true.
- Required fix: State unambiguously which TTA group was used to produce Catalog C and all headline numbers (Z2 or D4). If Z2 was used, change Fig. 2 (and any text) accordingly; if D4 was used, update Sec. III.C and all places that say Z2. If both were tried at different points, clearly separate what produced which result and quantify any differences.

P4-E11 (Definition of asymmetry field Ap; Sec. IV.C eq. (3) vs Appendix A.a vs Appendix A.c): Denominator inconsistency (spirals-only vs all galaxies)
- Offending text: Sec. IV.C (eq. 3) and footnote in Sec. IV.D: Ap = (NCW − NCCW)/(NCW + NCCW) (spirals only). Appendix A.a: repeats spirals-only definition. Appendix A.c: “Field: scalar (spin-0) asymmetry map Ap = (NCW − NCCW)/Ntotal”.
- Problem: Two contradictory definitions of the analysis field are given within Appendix A itself and conflict with the main text. Using Ntotal rather than Nspiral changes amplitudes, variances, and mode-coupling. It is impossible to reproduce headline Cℓ and z without a single, consistent definition.
- Required fix: Choose one definition (spirals-only or all-galaxies normalization), apply it consistently throughout, and recompute any numbers that depended on the other. Explicitly state which definition is used for each estimator in Tables I/III/IV and figures.

P4-E12 (Pixel-count threshold for the canonical mask; Sec. IV.C vs Fig. 5 caption vs Appendix A.c): Threshold inconsistency (≥5 vs >10 vs ≥10 spirals)
- Offending text: Sec. IV.C: “pixels containing > 10 spiral galaxies”; Fig. 5 caption: “headline ℓ = 1 analysis ... requires Nspiral(p) ≥ 5 per pixel”; Appendix A.c: “canonical Catalog C mask (pixels with ≥10 spirals)”.
- Problem: Three different thresholds are stated for the same mask. This directly affects fsky, the weighting, and the reported σ.
- Required fix: Specify one threshold, update all mentions, and recompute fsky, Nmap, and σ accordingly. If different thresholds were used for different analyses, label them distinctly (e.g., “Mask10” vs “Mask5”) and keep them consistent in text, tables, and captions.

P4-E13 (Data vector used for ℓ = 1; Appendix A.a vs Sec. IV.C): fCW(n) − 0.5 vs Ap field ambiguity
- Offending text: Appendix A.a: “headline dipole estimator ... uses the monopole-subtracted CW-deficit map fCW(n) − 0.5 on the subsample mask ... The asymmetry field is Ap = (NCW − NCCW)/(NCW + NCCW) (spirals only).”
- Problem: It is unclear whether the ℓ = 1 MASTER result is computed from fCW(n) − 0.5 or from Ap(n). These are different fields with different noise properties and window-function couplings.
- Required fix: Clearly state which field feeds the MASTER computation for the headline ℓ = 1 result and for the canonical-mask diagnostic, and make the definition consistent with P4-E11.

P4-E14 (Table III, p.7): Incomplete presentation of “Joint χ2/dof (38 bandpowers)”
- Offending text: Table III reports “Joint χ2/dof (38 bandpowers) — 161.2/38 = 4.24,” while the table only lists 6 rows of bandpowers.
- Problem: The joint χ2 value cannot be verified from the displayed entries; readers cannot see the 38 bandpowers referred to.
- Required fix: Either include the full 38-bandpower table in the manuscript/appendix or provide a repository reference with the exact vector and covariance used to compute χ2. Otherwise, remove or restate the χ2 claim.

P4-E15 (Units/normalization of pseudo-Cℓ; Tables III/IV; Fig. 8): Inconsistent or missing units
- Offending text: Table III labels “Cℓ × 10^6 (sr)”; Table IV lists “Pre-MASTER pseudo-C(ℓ=1)ℓ = 1.696×10−2” with no units; Fig. 8 axis has no explicit units.
- Problem: Pseudo-Cℓ of a dimensionless field should carry units of sr. Units/normalizations differ across tables/figures and are not stated consistently.
- Required fix: Add and unify the units for every Cℓ (pseudo and deconvolved) wherever reported, and state any normalization factors (e.g., ×10^6) in axes/captions.

P4-E16 (Appendix A.c, p.10): Counterintuitive effect of monopole subtraction on “σ”
- Offending text: “Monopole subtraction reduces decoupled C1 at ℓ = 1 from 2.30×10−5 to 1.51×10−5 (~34%) and increases σ from +1.85 to +3.64 (the canonical-mask number).”
- Problem: If monopole leakage inflates C1, subtracting the monopole should reduce both amplitude and its “significance,” unless the null variance changes dramatically. The text does not explain why σ increases when the measured C1 decreases, nor does it state whether the null changed between the two computations.
- Required fix: Show the corresponding null means and σnull for both cases and explain why σ increases after monopole subtraction. If different nulls were used, state this explicitly and avoid comparing σ across incomparable nulls.

MAJOR

P4-M7 (Sec. IV.C.a, real-space dipole): Insufficient estimator specification for reproducibility
- Problem: The “simple dipole” fit lacks key details: exact mask applied, pixel or galaxy weighting in the fit, whether the dipole is fit to Ap or fCW − 0.5, treatment of incomplete sky (e.g., template marginalization), and the precise bootstrap procedure (block size, resampling unit).
- Required fix: Provide the explicit estimator (formula or code reference), weighting scheme, mask, and bootstrap protocol sufficient to reproduce the 0.43σ, p = 0.30 result.

P4-M8 (Permutation/shuffle nulls): Ambiguous definitions across sections
- Offending text: Variants such as “per-pixel random-label permutation,” “per-pixel-shuffle null,” “binomial-monopole realizations,” and “density-stratified null” appear without a single, precise definition of each.
- Problem: It is unclear, for each estimator, whether labels are permuted within pixels, across the footprint, within density strata, or replaced by binomial draws, and which counts (Nspiral vs Nall) are preserved. This affects tail probabilities and z.
- Required fix: Add a concise table mapping each estimator to its exact null procedure, including which counts are held fixed, which are randomized, and whether shuffles are constrained within strata. Cite repository scripts/commits implementing each.

P4-M9 (Abstract/Sec. VI.A, HC subsample definition for injection-recovery): Ambiguity in thresholding rule
- Offending text: Abstract: “471 049 high-confidence per-spiral after peqCW > 0.9”; Sec. VI.A: “HC-spiral subsample (N = 471,049)” without restating the rule; elsewhere HC cuts are defined with max-class probability peq > 0.6 and peq > 0.8.
- Problem: Using peqCW > 0.9 selects only high-confidence CW, not CCW, unless both peqCW and peqCCW were symmetrically applied. The phrase “per-spiral” is unclear. The injection-recovery threshold A50 depends on this selection.
- Required fix: Define the HC subsample used for injection-recovery precisely (is it max(PCW, PCCW) > 0.9? or PCW > 0.9 OR PCCW > 0.9?), and ensure this definition is used consistently in text/figures. Recompute A50/A95 if needed.

MINOR

P4-m6 (Rounding consistency): fsky rounding mismatch
- Offending text: Table III uses “fsky = 0.491” (caption), elsewhere “0.49005”.
- Required fix: Use a consistent rounding convention for fsky across the paper; if different masks are used, label them distinctly.

P4-m7 (Terminology): “ViT − Small-Small” vs “ViT-Small”
- Offending text: Fig. 1 caption: “ViT − Small-Small classifier”; body: “ViT-Small encoder”.
- Required fix: Standardize the model name.

P4-m8 (Appendix C.e, p-values to σ): Sidedness not specified
- Offending text: “family-corrected p-value is 0.0086 (≈ 2.4σ family-wise)”.
- Problem: p = 0.0086 corresponds to ≈ 2.63σ two-sided (or 2.40σ one-sided). Sidedness is not stated.
- Required fix: Specify one- vs two-sided and adjust σ accordingly.

P4-m9 (Reporting limit for nulls): Zero-exceedance p-values
- Offending text: Table I “pLEE ≤ 10−4”; Appendix C: NMC = 10,000.
- Required fix: Report the estimator as p̂ = 0/10,000 with a confidence interval (e.g., Clopper–Pearson 95% CI) rather than a hard “≤ 10−4” bound.

P4-m10 (Abstract claim referencing A50/A95): Cross-reference to figure/table missing
- Offending text: Abstract gives A50 and A95; main text mentions A50 briefly, but there is no figure/table showing the full recovery curve (already noted in P4-M2 for A95; this minor note is about the abstract’s forward reference).
- Required fix: Add explicit pointers in the abstract to the figure/table presenting the injection-recovery curve once added.

NOTATIONAL/STYLE NITS

P4-N4 (Fig./text typography): Spacing/notation glitches
- Examples: “V iT − Small-Small”, stray math-mode spacing (f eq CW), hyphenation inconsistencies (subsample-mask vs subsample mask).
- Fix: Clean up typesetting for consistency.

Explanation
This fresh pass focused on method-definition consistency, field normalization, mask thresholds, and units. The Z2 vs D4 TTA conflict (P4-E10), the Ap denominator contradiction (P4-E11), and the mask-threshold mismatch (P4-E12) are new and material issues that affect reproducibility and potentially the numerical results. Additional clarity is needed on which data vector feeds the ℓ = 1 estimate (P4-E13), how many bandpowers underlie the reported χ2 (P4-E14), and on units (P4-E15). Several procedural specifications for nulls, dipole fitting, and HC selection require tightening (P4-M7–M9).