# P4 auto-2026-06-08_1520pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8498 chars)
**Wall time**: 368.0s

---

Referee report on “Survey-Scale Galaxy Chirality with Equivariant TTA: A −0.122σ Subsample-Mask ℓ=1 Null, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)”

Scope of review
- Methodology rigor and internal consistency: statistical procedures, estimator declarations, null definitions, dimensional/units checks, and arithmetic consistency.
- I audited every quoted scalar in the abstract, tables, and conclusions against derivations/numbers in the body. Where precise recomputation was possible from provided numbers, I did so. Where mapping between sections was ambiguous, I identify required clarifications or recomputations.

Overall assessment
The paper presents a large-sample chirality analysis with a stated null result for an ℓ=1 dipole on specific masks, together with a careful discussion of mask–monopole leakage. The overall methodology is interesting, but there are several critical internal inconsistencies and statistical specification problems that must be resolved before the work can meet PRD standards. Most are fixable with careful revision, but several items require unambiguous, quantitative correction and, in at least one case, a rerun or re-tabulation of results to ensure that field definitions are consistent across sections.

Findings

ESSENTIAL

P4-E1 (Sec. IV.B, p. 4; Table II vs text; also Abstract, p. 1)
Problem: In Sec. IV.B you state “The 3.86× asymmetry-suppression factor from raw +2.05% to equivariant −0.53%,” but Table II lists:
- A (raw) cw fraction = 0.5079 (+0.79%), Dev = 28.8σ
- C (equivariant) = 0.4974 (−0.26%), Dev = 9.5σ
Thus, the raw excess is +0.79%, not +2.05%, and the equivariant offset is −0.26%, not −0.53%. The same 9.5σ value is used repeatedly for the Catalog C monopole but is inconsistent with the listed uncertainty (see P4-M1).
Required fix: Replace the +2.05% and −0.53% with the correct values consistent with Table II, or provide a clear, quantitative explanation (with equations and references to the exact sample/mask and weight definition) if these percentages correspond to a different statistic than cw fraction from Table II. All text references to these percentages must be corrected throughout the paper, including the methods and discussion where you interpret the “suppression factor.” If a different weighting or mask was used to compute +2.05% and −0.53%, explicitly define it and ensure that all figures/tables using those numbers are recomputed accordingly.

P4-E2 (Sec. IV.C Eq. (3), p. 4, vs. Appendix A “Field”, p. 7)
Problem: The chirality field Ap is defined inconsistently:
- Sec. IV.C Eq. (3): Ap = (NCW(p) − NCCW(p)) / (NCW(p) + NCCW(p)) (spirals-only denominator Nspiral(p)).
- Appendix A “Field: scalar (spin-0) asymmetry map Ap = (NCW − NCCW)/N(p)total.”
These are not the same field. Using Ntotal (includes NS) in the denominator changes the amplitude by a factor that varies per pixel, and can change the mask/noise properties in NaMaster. This is a critical, load-bearing definition that affects Cℓ amplitudes and their interpretation.
Required fix: Unify the definition. State explicitly which field is used in each estimator (real-space dipole fit, pseudo-Cℓ, MASTER). If any main numerical results used the Ntotal denominator, re-run/re-tabulate them using the spirals-only denominator (or vice versa), document the impact on C1 and its null distribution, and update all affected numbers and claims. The NaMaster inputs in Appendix A must precisely match Eq. (3) (or else Eq. (3) must be corrected). Ambiguity must be eliminated.

P4-E3 (Appendix A “a. Declared data vector …” and “b. Bandpower vs single-ℓ”, p. 7)
Problem: Related inconsistency: Appendix A also defines the “headline dipole estimator” off “the monopole-subtracted CW-deficit map fCW(n̂) − 0.5,” while elsewhere the field is Ap = (NCW − NCCW)/Nspiral. Note that fCW − 0.5 = (NCW/Nspiral) − 0.5 = Ap/2. A factor of two changes the reported Cℓ amplitudes and can influence the variance model if not treated consistently.
Required fix: Explicitly state which of the two equivalent normalizations you used in each analysis and ensure all amplitudes, variances, and significance values are computed consistently. If mixing fCW − 0.5 in one place and Ap elsewhere, document the conversion and verify that the reported C1 and σnull are consistent under the chosen normalization. Update the text/tables accordingly.

P4-E4 (Appendix D, Abstract, and Sec. IV.D; p. 1, 5, 8)
Problem: Conversion between empirical p-values and “Gaussian-equivalent σ” is not specified consistently. The abstract states “post-MASTER canonical-mask direct-MC residual is +3.64σ (z = Δ/σnull moment-ratio; empirical rank pMC = 0.030, i.e. ≈ 1.9σ Gaussian-equivalent).” However, p = 0.030 corresponds to ≈ 2.17σ (two-sided) or ≈ 1.88σ (one-sided). You must state clearly whether a one-sided or two-sided mapping is used, and be consistent. As written, the text implies an equivalence between the z-score from a moment-ratio test (+3.64σ) and the Gaussian-equivalent σ from a rank p-value (≈1.9σ), which are not the same statistic.
Required fix: For every place a p-value is converted to “Gaussian-equivalent σ,” specify one-sided vs two-sided and use the correct mapping. Where two different null tests and statistics are being compared (z from Δ/σnull vs rank p from permutations), avoid conflating them. The abstract phrase “i.e.” must be removed or replaced with a clear statement: “corresponds to 2.17σ (two-sided Gaussian-equivalent)” (or one-sided, if you choose and justify it). Apply this consistently throughout.

P4-E5 (Sec. VI.A, p. 6)
Problem: Fisher/Poisson sensitivity floor derivation is inconsistent and undocumented. You state: “The Fisher Poisson floor at 3σ is ∼ 0.29% full-amplitude (from σ(A/2) ≈ 0.048% at Nspiral = 3,201,160, fsky = 0.46).” For a binomial with A = 2p − 1, var(A) ≈ 1/N for p ≈ 0.5, so σ(A) ≈ 1/√N ≈ 0.0559% for N = 3.20116 × 10^6; thus σ(A/2) ≈ 0.02795%. An fsky degradation by 1/√fsky with fsky = 0.46 would inflate σ(A/2) to ≈ 0.041%. Your quoted 0.048% and the implied 3σ amplitude 0.29% are not reproduced by these standard approximations, and fsky = 0.46 is not one of the masks reported elsewhere (0.49005 and 0.659). 
Required fix: Provide an explicit derivation (equations and numerical inputs) for σ(A/2) and the 3σ amplitude floor, including how fsky enters. Use a consistently defined fsky matching an actual mask used in the analysis, or justify the effective fsky if different. Correct the 0.29% number if needed. If additional degradation factors (e.g., pixel weighting, sky cuts) are included, list and quantify them. If you intend the floor for a specific estimator (e.g., canonical mask), compute it for that mask and state so.

P4-E6 (Appendix A, p. 7; throughout)
Problem: Weighting choice Wp = Nall for a spirals-only field Ap is non-standard and potentially biases coupling to survey depth/morphology. You state “The depth weighting does not introduce a monopole–dipole coupling because the galaxy-weighted mask-mean ⟨A⟩mask,gw is subtracted.” That subtraction does not by itself guarantee absence of coupling between Wp and the signal/noise (Ap has spiral-only denominator); it can change the effective noise model and mode-coupling. 
Required fix: Justify this weighting choice with a control test: recompute the key MASTER ℓ = 1 result using Wp = Nspiral(p) and also using a uniform weight (Wp = 1), and report the change in C1 and σnull. If results are stable within quoted uncertainties, state this explicitly. Otherwise, adopt the weighting consistent with the field definition, or revise claims about robustness.

P4-E7 (Sec. IV.D footnote 1, p. 4–5)
Problem: The footnote contains versioning/process language and an unresolved analysis branch: “The previous wording … was ambiguous … A parallel rerun … is in queue … expected to shift …” This is not acceptable in a final journal submission; PRD requires definitive analyses, not plans.
Required fix: Remove all “in queue” and version-history language. Decide and document the final generative-null implementation (Nspiral vs Nall) and provide the quantitative results for the adopted choice. If you also wish to present the alternative as a robustness check, include both sets of numbers with clear labeling.

P4-E8 (Conclusions, p. 6–7; Abstract, p. 1; Sec. III.A, p. 3)
Problem: Multiple σ values from different nulls appear side-by-side without an explicit “not directly comparable” reminder at every juxtaposition. While you include an overall warning in the abstract and a “Significance conventions” paragraph, you repeatedly juxtapose σ from different nulls later (e.g., Conclusions b: “σdirectcanonical = +3.64σ … real-space dipole 0.43σ … subsample-mask MASTER −0.122σ”) with no local reminder, violating the stated care.
Required fix: At every place where σ from different null definitions are compared or listed side-by-side, add an explicit phrase (e.g., “σ values arise from different null procedures and are not directly comparable”) or equivalently mark them with subscripts and remind the reader once per paragraph. Alternatively, avoid juxtaposition by moving these numbers into a table with a dedicated “null type” column (you already have Table I) and refer to that table instead of repeating σ in prose.

MAJOR

P4-M1 (Table II, p. 4; Sec. IV.B, p. 4; Data Availability, p. 9)
Problem: The listed uncertainties (±0.000279) imply devs:
- A (raw): (0.5079 − 0.5)/0.0002796 ≈ +28.3σ (table says +28.8σ).
- B (calibrated): (0.504 − 0.5)/0.0002796 ≈ +14.3σ (table says +14.6σ).
- C (equivariant): (0.4974 − 0.5)/0.0002796 ≈ −9.3σ (paper uses “9.5σ” in text).
Discrepancies are small but systematic across rows and repeated in prose. If the σ used for Dev differs from the printed ±0.000279 (e.g., a slightly different N or a non-binomial variance), the table must show the exact uncertainties used.
Required fix: Recompute and correct the Dev values using the uncertainty actually used, or update the uncertainty column to match. Ensure that all occurrences of “9.5σ” for the Catalog C monopole are adjusted to the correct value given the adopted σ. State explicitly whether the binomial σ used p(1 − p)/N or 0.25/N and ensure consistency across tiers.

P4-M2 (Table IV vs text; Sec. IV.D, p. 5)
Problem: Table IV shows Data 1.696×10−2 and Null (1.685 ± 0.007)×10−2 for the pre-MASTER pseudo-C(ℓ=1)ℓ, with z = +1.68. The difference implied by the displayed numbers is (1.696 − 1.685)/0.007 = 0.011/0.007 ≈ 1.57, not 1.68. The hemisphere z in the same table also depends sensitively on the shown uncertainties.
Required fix: Provide sufficient significant figures to make the z reproducible from the displayed numbers, or correct the z. If the standard deviation is actually 0.0065×10−2, print it as such. The table should be self-auditable.

P4-M3 (Appendix A “Apodization,” p. 7; Appendix D a, p. 8)
Problem: The notation “C 2 2° apodization” is unclear (formatting artifact?). NaMaster supports C2 apodization with a given apodization scale in degrees. As written, it is ambiguous to the reader.
Required fix: Clarify the apodization method and parameter(s) explicitly, e.g., “NaMaster mask apodization method = ‘C2’ with apodization scale θapod = 2°.” Ensure the same appears consistently in Appendix A and the main text where apodization robustness is claimed.

P4-M4 (Sec. IV.C, p. 4; Table III, p. 5)
Problem: Table III lists bandpower Cℓ values, many negative, with positive “Significance (σ)” values but no null means, making the σ unverifiable. If the σ column is (Cmeas − ⟨Cnull⟩)/σnull, the table must include ⟨Cnull⟩ (or state it explicitly for each bin) to allow auditing; as written, one cannot check that +6.097σ at ℓeff = 4 is consistent with the given Cℓ.
Required fix: Add a column for ⟨Cnull⟩ per bandpower (or a single number if it is zero), or include a footnote specifying the null mean values used for each bin so the σ can be recomputed from the table.

P4-M5 (Sec. IV.C.a, p. 4; Sec. III.A, p. 3)
Problem: Real-space dipole fit reports “0.43σ (p = 0.30 from the isotropic-null bootstrap at NMC = 10,000).” If the σ is Gaussian-equivalent, z ≈ 0.43 corresponds to two-sided p ≈ 0.67, not 0.30. It is fine if the p-value is from a non-Gaussian bootstrap null, but the current presentation is confusing.
Required fix: Specify explicitly how σ and p are computed and related. If σ is the z-score from a different summary (e.g., moment-ratio) while p is the bootstrap exceedance probability of the amplitude, state that plainly (“σ and p derive from different statistics under different nulls and are not directly comparable”). Consider reporting either p or σ for each estimator consistently to avoid confusion.

P4-M6 (Appendix A “Seed: numpy.random.seed(42),” p. 7; multiple sections)
Problem: Several key permutation/MCMC/null results rely on relatively small MC sizes (N = 500 for MASTER-null and generative nulls; N = 10,000 for hemisphere LEE), and many of your quoted significances rely on those. You also fix a single seed (42) in Appendix A.
Required fix: Provide a brief robustness statement (or supplement) demonstrating that the main null results (ℓ = 1 deconvolved −0.122σ; canonical residual +3.64σ and pMC ≈ 0.030) are stable under independent MC seeds and that increasing NMC does not change qualitative conclusions. Alternatively, justify why N = 500 is sufficient for the quoted precision (e.g., show that the fractional uncertainty on σnull is small compared to the effect sizes reported; for the null result, emphasize that −0.122σ is well within MC noise).

MINOR

P4-m1 (Sec. IV.A, p. 4)
Problem: Percentages in Catalog C statistics are consistent with your totals (verified), but quoting 18.78% and 18.99% to two decimals while reporting a “mean classification confidence 0.951” gives an impression of precision not consistently justified across metrics.
Required fix: Either standardize the significant-figures policy (e.g., 2–3 s.f. for percentages and proportions) or add uncertainties where appropriate (binomial for class fractions).

P4-m2 (Sec. V.B, p. 6)
Problem: “CE-ResNet [7] achieves cw/ccw = 0.998” is ambiguous; it is not clear if this is the ratio cw/(cw + ccw) ≈ 0.499, or cw/ccw ≈ 0.998. The latter would imply a 0.2% deviation from parity, likely not what is meant.
Required fix: Clarify the statistic being reported from CE-ResNet (e.g., “cw fraction among spirals: 0.499 ± …”; or “cw/ccw ratio = 0.998”), and include the context (sample/mask) to avoid misinterpretation.

P4-m3 (Appendix C.c, p. 8)
Problem: The Bonferroni/BH “∼ 650 directions” appears without details of the grid used for hemisphere centers.
Required fix: Specify the sampling scheme (e.g., HEALPix NSIDE for the hemisphere centers) so the count 650 can be reproduced.

P4-m4 (Throughout; e.g., Sec. IV.D and Appendix D)
Problem: Occasional use of “signal-hunt,” “headline,” “non-headline,” and process language detracts from scientific tone appropriate for PRD.
Required fix: Replace with neutral, technical language (e.g., “diagnostic,” “primary estimator,” “secondary check,” etc.).

P4-m5 (Data Availability, p. 9)
Problem: You note the released labels carry a measured bias residual of 0.26% and also state “9.5σ.” Given the Table II correction (P4-M1), ensure consistency in both fraction and σ here as well.
Required fix: Align the stated σ here with the corrected value from Table II.

NITS

P4-N1 (Sec. III.B Eq. (1), p. 3)
Problem: Present “(1)” as an equation with textual layers; but as it is non-load-bearing, no issue except formatting.
Required fix: None strictly required; optional to move to Appendix B only.

P4-N2 (References, p. 10–11)
Problem: Spot-checks find references consistent, but minor stylistic inconsistencies exist (e.g., some DOIs included, some not; capitalization of journal titles).
Required fix: Align reference formatting with PRD style guide.

P4-N3 (Typos/formatting)
- “C 2 2°” apodization (see P4-M3)
- Occasional doubled spaces and line-break artifacts in the footnotes and Appendix A.
Required fix: Clean formatting.

Length
At 11 pages, the paper is not egregiously long for the scope (new catalog + multiple estimators + systematic suite). However, parts of Sec. IV.D and Appendix D repeat the same narrative. A tighter presentation could reduce length by ~1–2 pages without loss of content. Not mandatory.

## Summary recommendation
MAJOR REVISIONS

Justification: The central scientific claim (null ℓ = 1 dipole on the subsample mask; quantifiable mask–monopole leakage on the canonical mask) appears plausible and potentially important. However, there are essential internal inconsistencies in field definitions (spiral-only vs all-galaxy denominators; Ap vs fCW − 0.5), contradictory percentage and σ values (Table II vs text; Fisher floor derivation), and a conflation/misalignment of p-values and “Gaussian-equivalent σ” for different test statistics. These must be corrected and, where necessary, re-run to ensure that the reported Cℓ and significance values are computed consistently from a single, clearly defined field with a documented weighting scheme. With these issues resolved and the statistics clarified, the paper could be suitable for PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh pass)

ESSENTIAL

P4-E9 (Sec. IV.D, p. 5; Table IV vs. body text)
Problem: Contradictory hemisphere maxima. Sec. IV.D cites “local hemisphere maximum of 3.05σ,” while Table IV reports “Hemisphere max|A| (NSIDEdir = 8)” z = +4.42σ. Appendix C.c separately reports a 3.05σ maximum from a 10°-grid scan. These are different hemisphere samplings but are presented in Sec. IV.D as if referring to the same diagnostic.
Required fix: Disambiguate and label the hemisphere tests consistently in Sec. IV.D (e.g., “NSIDEdir=8: 4.42σ; 10°-grid: 3.05σ”). State explicitly which is used where, and avoid mixing the two values in the same narrative. If you intend one of them as the primary diagnostic, say so.

P4-E10 (Sec. II.B, p. 2; Appendix B.a, p. 7)
Problem: Training-set composition is arithmetically inconsistent.
- Listed components: GZ1 = 6,637; CE-ResNet = 17,153; synthetic negatives = 2,000. Sum = 25,790.
- Stated combined training set = 26,636 (diff = +846 unaccounted).
- Stated “67.6% of training labels derive from CE-ResNet predictions”; but 17,153/26,636 ≈ 64.4%, not 67.6%.
Required fix: Provide a reconciled accounting of the training set (counts by source that sum to 26,636 if that is the true total, including any overlaps, augmentations, or additional sources). Correct the CE-ResNet fraction or the totals accordingly.

P4-E11 (Abstract, p. 1; Sec. VI.A, p. 6; Appendix E.b, p. 9)
Problem: Ambiguous high-confidence (HC) threshold definition. Abstract: “471,049 high-confidence per-spiral after peq CW > 0.9” suggests a one-class (CW-only) threshold. Elsewhere (Appendix E.b) HC cuts are defined on the “equivariant max-class probability” (i.e., max(peq_CW, peq_CCW) > threshold).
Required fix: Standardize the HC definition throughout. If HC means max(peq_CW, peq_CCW) > 0.9, state this explicitly in the abstract and methods. If any results used a one-sided class threshold, report them separately.

P4-E12 (Table III, p. 5; Appendix A, p. 7)
Problem: Units on Cℓ are inconsistent. Table III labels “Cℓ × 10^6 (sr)”, implying steradian units. For a dimensionless scalar field Ap, NaMaster returns dimensionless Cℓ (no sr). If a nonstandard normalization was used that introduces units, it must be documented.
Required fix: Correct the Cℓ units to dimensionless, or document the exact normalization that leads to sr, and make it consistent in Appendix A (data-vector definition) and Table III.

MAJOR

P4-M7 (Abstract, p. 1; Table I, p. 4)
Problem: Ambiguous use of n in the abstract. “strict-superset subsample mask (n = 5,547,858, fsky = 0.659)” refers (per Table I) to Nmap weighted = Σp Wp with Wp = Nall(p), not the number of spirals or the number of pixels. As written, “n” looks like a sample size.
Required fix: Replace “n = 5,547,858” with an explicit label (“Σp Nall(p) over the subsample mask = 5,547,858”) or drop “n” here. Ensure the meaning of this weighted count is clear anywhere it is used.

P4-M8 (Table III, p. 5)
Problem: “Joint χ^2/dof (38 bandpowers) = 161.2/38 = 4.24” is presented in a table that otherwise lists only 1 single-ℓ row plus 5 bandpowers. The 38 bandpowers used for the χ^2 are not shown, nor are their null means (also needed for verification; cf. P4-M4).
Required fix: Either provide the full 38-bandpower list (with Cmeas, ⟨Cnull⟩, σnull per bin) in a table or the supplement, or move the joint χ^2 result to text with a pointer to where the 38-bin spectrum is documented. As-is, it is not auditable.

P4-M9 (Abstract, p. 1; Appendix D.g, p. 9; multiple places)
Problem: Mixed sign conventions for “σ”/z. Some places report signed significances (e.g., rℓ=2 = −0.65 with “σ = −2.89”), elsewhere absolute z is printed as positive even when Cℓ is negative (Table III). This is confusing and prevents uniform interpretation.
Required fix: Adopt a consistent convention: either report signed z everywhere and explain the sign, or report |z| and discuss the sign of the underlying estimator separately. Apply consistently across text, tables, and appendices.

P4-M10 (Appendix C.c, p. 8; Table I, p. 4)
Problem: Finite-MC-resolution handling for extreme p-values is not specified. You report pLEE ≤ 10^−4 from 10,000 shuffles (implying zero exceedances). Best practice is to quote (k+1)/(N+1) and/or to state “no exceedances observed; p < 1/(N+1) = 9.99×10^−5.” Also, the phrase “rejection” is used for this p but then immediately down-weighted by LEE corrections, adding to confusion.
Required fix: State the finite-MC resolution rule used; if k = 0, report p < 1/(N+1) (and optionally a one-sided vs two-sided mapping). Avoid the term “rejection” here; instead state the bound and then discuss LEE correction.

P4-M11 (Throughout; e.g., Table I “null type,” Sec. III.A, Sec. IV.C–D, Appendix A)
Problem: Null-procedure taxonomy is underspecified and sometimes conflated: “pp-shuffle,” “per-pixel random-label permutation,” “isotropic-null bootstrap,” “binomial generative null,” “direct-MC,” etc. It is often unclear whether shuffles preserve per-pixel Nspiral(p), whether labels are permuted within pixels or over the footprint, whether weights Wp are held fixed, and what summary statistic is compared (amplitude, Cℓ, z, etc.).
Required fix: Add a concise methods subsection enumerating each null type with an unambiguous algorithm:
- what is randomized (labels vs positions),
- what is preserved (per-pixel counts, mask, weights),
- which summary statistic is computed,
- whether the test is one- or two-sided,
- and how σnull is estimated (analytic vs empirical).
Then ensure every σ/p reported cites one of these defined nulls by name.

MINOR

P4-m6 (Sec. IV.A, p. 4)
Problem: Minor rounding inconsistency in Catalog C class fractions. CCW fraction reported as 18.99%; 1,609,053 / 8,474,531 ≈ 18.976% (18.98% to two decimals). Not material, but contributes to an uneven significant-figures policy (see P4-m1).
Required fix: Harmonize rounding/significant figures across class-percentage summaries.

P4-m7 (Sec. IV.C/Table III vs Appendix A, p. 5, 7)
Problem: fsky for the canonical mask appears as 0.49005 (Table I) but 0.491 in the Table III heading text. Small, but stale-number inconsistencies recur (also noted elsewhere).
Required fix: Use a single value (preferably 0.49005) consistently, or round consistently to three decimals everywhere.

P4-m8 (Appendix B.d, Table V, p. 8)
Problem: T7 “Confidence calibration (qualitative, < 50% at confidence > 0.9)” is unclear: what statistic is “< 50%,” and what is being calibrated? This invites misinterpretation.
Required fix: Define the calibration metric (e.g., fraction of objects with max-class peq > 0.9 among which the predicted class agrees with an external label; or ECE/MCE), and report a quantitative value with uncertainty if available.

P4-m9 (Sec. IV.B, p. 4; Sec. IV.D heading text)
Problem: Occasional mixing of Ap vs fCW − 0.5 language when quoting percentages (distinct from the field-definition issue in P4-E2/E3). Example: mask-mean ⟨A⟩mask,gw = −0.005294 corresponds to a −0.53% Ap offset, which equals −0.26% in fCW − 0.5 units. Some prose uses “percent” without stating which normalization.
Required fix: Whenever reporting a “percent” offset, specify whether it is in Ap units (percent of full-range asymmetry) or in fCW − 0.5 units (CW fraction offset), and keep this consistent in the narrative.

P4-m10 (Appendix C.c, p. 8)
Problem: “∼650 directions” used for Bonferroni/BH LEE correction lacks specification (grid definition). This is distinct from the NSIDEdir=8 grid used elsewhere.
Required fix: State the hemisphere-center sampling scheme (e.g., HEALPix NSIDE = X for centers; or 10° latitude/longitude grid) so the count is reproducible.

NO FIGURE FINDINGS
There are no figures in the provided text; thus B (caption vs body) is not applicable here.

Explanation
This second pass focused on fresh inconsistencies not already identified: contradictory hemisphere-significance values from different grids; training-set arithmetic; ambiguous HC thresholding; incorrect or undocumented Cℓ units; ambiguous use of “n” for a weighted count; a non-auditable joint χ^2 with 38 unseen bandpowers; mixed sign conventions for z; finite-MC-resolution handling; and additional clarity gaps in null-procedure definitions and percentage normalizations. These items materially affect clarity, auditability, and in a few cases the numerical interpretation of key diagnostics, and should be addressed alongside the issues raised in the initial review.