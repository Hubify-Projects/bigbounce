# P4 auto-2026-06-08_1632pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (9457 chars)
**Wall time**: 463.4s

---

Referee report on “Survey-Scale Galaxy Chirality with Equivariant TTA: A −0.122σ Subsample-Mask ℓ=1 Null, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)”

Scope of review
- Role: Methodology rigor. I audited statistical methods, estimator declarations, null procedures, internal arithmetic, dimensional consistency, and traceability of every load-bearing scalar in the abstract and conclusions to the body text/tables. I recomputed all σ, p-values, and ratios that can be reconstructed from the displayed numbers. I also checked for consistency between different sections, masks, and estimators; and for the distinctness of σ values derived under non-identical nulls.

Overall assessment
- The paper presents a careful, bias-aware null result for an ℓ=1 chirality dipole using a very large dataset and modern pseudo-Cℓ methodology. However, I identified several essential issues that must be fixed before the paper can be considered for publication in PRD. These include an internal inconsistency in the definition of the field used for power spectrum estimation (spiral-only denominator vs all-galaxy denominator), an explicit numerical error in Table IV (z-value), unresolved “rerun in queue” language for a load-bearing sensitivity check, and a double-counting of the look-elsewhere correction for the hemisphere scan. In addition, several numerical presentations (Table III significance column, global-fraction suppression factor) are not internally consistent with the numbers shown, and key procedural details (fsky definition/mask construction; real-space bootstrap; Fisher-floor derivation) need to be clarified and documented.

Findings

ESSENTIAL

P4-E1 (Section IV C Eq. 3 vs Appendix A, page 7): Inconsistent definition of the asymmetry field denominator
- Offending text:
  - Eq. (3), page 4: Ap = (NCW(p) − NCCW(p)) / (NCW(p) + NCCW(p)) (spirals only).
  - Appendix A, page 7: “Field: scalar (spin-0) asymmetry map Ap = (NCW(p) − NCCW(p))/N(p)total …”
- Problem: The denominator switches from “spirals only” in the main text (NCW+NCCW) to “all galaxies” (Ntotal = NCW+NCCW+NNS) in Appendix A’s NaMaster configuration. Footnote 1 in Sec. IV D also stresses consistency with the spiral trial pool. This inconsistency makes the core MASTER computation non-reproducible and could bias Cℓ.
- Required fix: Unify the definition. State explicitly which denominator is used to build the field for every reported spectrum (subsample-mask headline and canonical-mask diagnostics). If any results used Ntotal in the denominator, rerun them with the stated spiral-only denominator (or vice versa), update all affected numbers, and clearly document the choice. Ensure Table I’s “Nmap weighted” use of Nall remains strictly a weight-only map and not the field denominator.

P4-E2 (Table IV, page 5): Arithmetic error in the reported z-value
- Offending text: “Pre-MASTER pseudo-C(ℓ=1)ℓ (canonical mask) Data: 1.696×10−2; Null: (1.685±0.007)×10−2; z=+1.68.”
- Problem: z = (0.01696 − 0.01685) / 0.00007 = 0.00011 / 0.00007 ≈ 1.57, not 1.68.
- Required fix: Correct the z-value and any downstream text that references it. Recheck all entries in this table for similar rounding/propagation mistakes.

P4-E3 (Section IV B, page 4): Inconsistent “asymmetry-suppression factor” and percentages
- Offending text: “The 3.86× asymmetry-suppression factor from raw +2.05% to equivariant −0.53%...”
- Problem: Table II gives raw fCW = 0.5079 (monopole excess +0.79%) and Catalog C fCW = 0.4974 (−0.26%). If the paper means Ap = 2 fCW − 1, Catalog A Ap ≈ +1.58% and Catalog C Ap ≈ −0.53% (ratio ~ 2.98, not 3.86); if it means fCW fraction, +0.79% to −0.26% is not +2.05% to −0.53%. The stated numbers are not consistent with Table II or with Ap’s definition.
- Required fix: Specify whether you are quoting Ap (dimensionless asymmetry) or fCW−0.5. Give both raw and equivariant values using one consistent definition, and recompute the suppression factor accordingly.

P4-E4 (Section IV D footnote 1, page 4; Appendix D preamble, page 8): “Rerun in queue” and “earlier paper versions” text
- Offending text:
  - Footnote 1: “A parallel rerun on N(p)all-trial draws is in queue… will be reported…”
  - Section IV D main text: “were interpreted in earlier paper versions…”
- Problem: This indicates unfinished analysis and versioning references in the body of the paper.
- Required fix: Complete the rerun (or remove the claim depending on its load-bearing role), incorporate final numbers, and remove all “in queue,” “earlier versions,” and similar process/provenance language from the body.

P4-E5 (Appendix C c., page 8): Double-counting the look-elsewhere effect
- Offending text: “The direct-MC look-elsewhere test (N=10,000 random-label shuffles) gives pLEE ≤ 10−4 (rejection of the random-label null); the conservative Bonferroni/BH penalty across ∼650 tested directions reduces post-LEE significance to <1σ.”
- Problem: A direct-MC pLEE that samples the maximum over the tested directions already incorporates the LEE. Applying a Bonferroni/BH family correction again is double counting.
- Required fix: Report the direct-MC pLEE as the final look-elsewhere-corrected p-value, with its resolution limits (≥1/10,000). If you also want to report a simple Bonferroni bound, label it as a crude upper bound and do not present it as a “post-LEE” correction.

P4-E6 (Table I and throughout mask descriptions, pages 4, 7): Ambiguous or implausible fsky values and mask definitions
- Offending text:
  - Table I: fsky = 0.659 (subsample mask), fsky = 0.49005 (canonical mask).
  - Appendix A: brief mask descriptions without pixel counts.
- Problem: DESI Legacy DR8 covers ~0.34 of the full sky. Reported fsky ≈ 0.49–0.66 appear too large unless fsky is defined relative to a different total area. NaMaster uses the actual full-sky mask; fsky should be the fraction of 4π steradians covered by the mask. As written, the fsky values are not verifiably correct.
- Required fix: Provide the exact mask generation procedure, the number of NSIDE=64 pixels in each mask, and the computed fsky = Nmask/Npix. If fsky is defined relative to a footprint subset (not the sphere), rename the quantity (e.g., ffootprint), and do not use it where the full-sky fraction is expected. Update any places where fsky is used in a sensitivity or Fisher argument if it was misdefined.

P4-E7 (Abstract, page 1): Misleading use of “n = 5,547,858” for the subsample mask
- Offending text: “MASTER-deconvolved … on the strict-superset subsample mask (n=5,547,858, fsky=0.659) …”
- Problem: In Table I and Appendix A, 5,547,858 is the sum of per-pixel weights Wp = Nall(p) (includes non-spirals). It is not a count of independent spiral galaxies contributing to the field. Using “n=” implies an event count.
- Required fix: Replace “n = 5,547,858” with a clear label such as “Σp Wp = 5,547,858 (sum of weights Nall),” and separately state Ncatalog,spiral. Avoid “n=” unless it is an integer number of events used in a statistic.

P4-E8 (Table III, page 5): “Significance (σ)” column not reproducible from shown numbers
- Offending text: Row ℓeff=4: Cℓ×10^6 = 3.210, σnull×10^6 = 0.804, “Significance +6.097”; rows 3–6 have negative Cℓ but positive significances.
- Problem: Without the null mean ⟨Cℓ⟩null, the displayed z-scores cannot be verified. For example, 3.210/0.804 ≈ 3.99, not 6.10, unless ⟨Cℓ⟩null is negative and sizable. Similarly, negative measured Cℓ with positive “Significance” require a negative null mean, not shown.
- Required fix: Add the null means ⟨Cℓ⟩null for each bandpower (or explicitly state the centered statistic used), and recompute all z-scores consistently. Alternatively, report empirical-rank p-values from the MC ensemble.

P4-E9 (Appendix A, page 7): Contradictory statements on monopole subtraction effects
- Offending text: “Monopole subtraction reduces decoupled C1 at ℓ=1 from 2.30×10−5 to 1.51×10−5 (∼34%) and increases σ from +1.85 to +3.64 (the canonical-mask number).”
- Problem: It is plausible for |C1| to be reduced while z increases if σnull shrinks, but no null means/variances are given, and earlier the canonical-mask +3.64σ is explicitly quoted under “proper galaxy-weighted monopole subtraction.” This needs a fully specified before/after comparison to be credible.
- Required fix: Provide the null means ⟨C1⟩null and σnull for both pre- and post-monopole-subtraction canonical-mask runs, and show how the z-values change. Ensure consistency with Table III numbers.

MAJOR

P4-M1 (Section VI A, page 6): Fisher Poisson floor derivation missing
- Offending text: “The Fisher Poisson floor at 3σ is ∼0.29% full-amplitude (from σ(A/2)≈0.048% at Nspiral=3,201,160, fsky=0.46).”
- Problem: No derivation is provided; the stated σ(A/2) is not obviously consistent with a simple binomial estimate given the mask and pixelization. For global fCW, σ ≈ 0.028%; the larger 0.048% needs justification in the dipole context.
- Required fix: Provide a short derivation (or cite a standard result) translating shot noise into an expected uncertainty on a dipole amplitude estimate under the stated mask and pixelization. If this comes from simulation, state the procedure and include a small table/figure (can be Supplemental Material).

P4-M2 (Section IV C a., page 4): Insufficient detail on the isotropic-bootstrap dipole estimator
- Offending text: “p = 0.30 from the isotropic-null bootstrap at NMC = 10,000.”
- Problem: The bootstrap definition is unclear: what statistic is bootstrapped (dipole amplitude?), what weights are used, how is the mask handled, and is the bootstrap spatially coherent?
- Required fix: Precisely describe the bootstrap null generation, the statistic whose distribution is estimated, and how the p-value is computed (one- or two-sided). Provide a brief validation (e.g., on synthetic isotropic fields) or move details to an appendix.

P4-M3 (Throughout: Sections III A, IV C, Appendix A): Ambiguity in “canonical mask” vs “subsample mask,” “strict-superset,” and pixel thresholds
- Problem: The terminology is confusing. The “subsample mask” is described as a “strict-superset” and has larger fsky than the “canonical mask,” but not clearly defined. Pixel thresholds and inclusion criteria for each mask are not fully documented in the main text.
- Required fix: Define both masks unambiguously, including pixel thresholds, sky regions, and rationale. Provide Npix per mask at NSIDE=64 and show a small schematic or sky fraction histogram (can be Supplemental Material).

P4-M4 (Multiple locations): Mixed use of σ and empirical p-values without explicit mapping
- Example: Canonical-mask residual quoted as +3.64σ while also stating pMC=0.030 (≈1.9σ Gaussian equivalent) only in some places.
- Required fix: For every major σ claim derived from a non-Gaussian or finite-MC null, also report the empirical-rank p-value and its resolution/uncertainty. Clarify in table footnotes which σ are “moment z-scores” vs empirical.

P4-M5 (Section IV B, page 4): Unsupported claim of spatial uniformity of the global CW fraction
- Offending text: “spatially uniform across 7 equatorial coordinate slabs … all within 0.5% of 50/50.”
- Problem: No figure or table is provided in the manuscript; a pointer to an external repository is insufficient for PRD.
- Required fix: Include a table or figure (main text or Supplemental Material) showing these slab fractions and uncertainties.

P4-M6 (Section II B, page 3): Unclear methodology for the “234,282 disjoint matches” accuracy estimate
- Offending text: “The independent GZ1 cross-match on 234,282 disjoint matches yields spiral-chirality accuracy 69.91%…”
- Problem: The construction of this cross-match is not described, and 234k “disjoint matches” substantially exceeds the count of high-confidence GZ1 chirality labels cited earlier.
- Required fix: Describe the cross-match set, matching criteria, whether labels were harmonized (e.g., per-GZ1 task), and any filtering used to ensure independence from training. Provide a breakdown of label noise/confusion matrix, ideally with an ECE or reliability metric.

P4-M7 (Appendix E a., page 9): Edge-on contamination percentage lacks evidence in the paper
- Offending text: “65.7% of b/a<0.3 … receive CW/CCW … reduction in effective sample size by ∼10–15%.”
- Problem: No table/figure demonstrates this incidence or its impact on Neff.
- Required fix: Include a table showing the distribution of axis ratios vs class labels and quantify the effect on sensitivity (main text or Supplemental).

P4-M8 (Section V B, page 6): Ambiguity in “CE-ResNet achieves cw/ccw = 0.998”
- Problem: The metric “cw/ccw = 0.998” is unclear (ratio of counts? fCW?).
- Required fix: Define exactly what 0.998 denotes (e.g., fCW/(1−fCW) or fCW) and give a citation to the precise number in Jia et al. or compute it under a matched footprint.

P4-M9 (Appendix D c.–f., page 8): Cross-spectrum “rℓ=1,2” definition and significance
- Problem: Correlation coefficients rℓ with quoted σ-values require a clear definition and null procedure.
- Required fix: Define rℓ, specify the null generation and test statistic, and report empirical p-values.

P4-M10 (Table III and Appendix A, pages 5, 7): Unclear bandpower binning and χ2/dof
- Offending text: “Joint χ2/dof (38 bandpowers) — 161.2/38 = 4.24.”
- Problem: The origin of “38 bandpowers” is not described (binning scheme, lmax), and the χ2 computation relative to what covariance (diagonal from MC? full?) is not specified.
- Required fix: Document the binning (edges), the covariance used, and how χ2 is computed. Provide the null means to make the table auditable.

P4-M11 (Multiple places): Clarify mapping of Ap mean to fraction offsets
- Problem: The paper mixes statements in terms of fCW−0.5 and Ap. Readers can easily misinterpret signs and magnitudes (e.g., −0.26% in Table II vs −0.53% in Appendix A).
- Required fix: Introduce an explicit note that Ap = 2(fCW − 0.5), and whenever percentages are given, specify whether they refer to Ap or to (fCW − 0.5). Consider a small conversion line in captions/tables.

MINOR

P4-N1 (Table II, page 4): “Dev. (σ)” values do not divide to the stated σ using the listed uncertainty
- Offending data: For A: (0.5079−0.5)/0.000279 ≈ 28.32, not 28.8; for B: 14.34 vs 14.6; for C: 9.32 vs 9.5.
- Required fix: Recompute deviations with the same σ used to produce the displayed error bars, or state that σ was recomputed per tier (and show the per-tier σ used).

P4-N2 (Section VII d. and VI C, pages 7, 6): “Falsification criterion” wording
- Problem: “A future survey detecting … would falsify the present null” is overbroad; the current result is a measurement under a specific pipeline and footprint.
- Required fix: Rephrase to: “would be inconsistent with the present null under an analysis of comparable or better sensitivity on a matched or wider footprint” (or similar).

P4-N3 (Appendix A, page 7): Formatting of “C2 2◦ apodization”
- Required fix: Clarify this is cosine-squared apodization with 2° scale (write “cosine-squared, 2° apodization”).

P4-N4 (Data availability, page 9): Broken/oddly spaced links
- Offending text: “https://huggingface.co/dataset s/bamfai/galaxy- chirality- catalog”
- Required fix: Provide clean, copyable URLs without spaces.

P4-N5 (Typos/phrasing, multiple pages): Minor readability issues
- Examples: “strict-superset subsample mask,” repeated hyphenation artifacts from PDF line breaks (“p eq,” “C 2 2◦”).
- Required fix: Clean up phrasing and typographical artifacts.

Additional checks
- Abstract-to-body traceability: Most headline numbers are traceable: Nspiral = 3,201,160; 8.47M sources; +0.43σ dipole with p=0.30; ℓ=1 MASTER −0.122σ from given numbers; pMC=0.030 maps to ~1.9σ (stated). The 99.3% reproduction factor matches 0.01685/0.01696 ≈ 0.9935. However, the erroneous z in Table IV and the inconsistent “+2.05% to −0.53%” statement must be corrected.
- Distinctness of σ from different nulls: The paper cautions in the abstract and Sec. IV that σ values are null-specific. Ensure this caveat is repeated in captions where σ are juxtaposed (Tables I and III); after revisions, recheck.

Recommended maximum page count
- The length (11 pages) is acceptable for PRD if the above corrections are implemented. If further expansions (e.g., added derivations/figures) push the length significantly, consider moving some diagnostics (e.g., confidence-stratified tables) to Supplemental Material, retaining the core methodological clarifications in the main text.

## Summary recommendation
MAJOR REVISIONS

Justification: The manuscript presents an important, careful null test with sophisticated bias controls. However, there are essential internal inconsistencies (field definition in the MASTER analysis, a numerical error in Table IV, and incomplete “rerun in queue” language), a mishandled look-elsewhere correction, and several instances where reported significances cannot be audited from the displayed numbers (Table III, mask fsky definitions). These must be corrected, with clearer documentation of masks, nulls, and estimator construction, before the paper can meet PRD methodological standards.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (fresh-pass audit)

ESSENTIAL

P4-E10 (Appendix A a.–c., page 7): Factor-of-two mismatch in field definition (fCW−0.5 vs Ap)
- Offending text:
  - a.: “the monopole-subtracted CW-deficit map fCW(n) − 0.5 on the subsample mask…”
  - a./c.: “The asymmetry field is Ap = (NCW − NCCW)/(NCW + NCCW) (spirals only).”
- Problem: These are different by a factor of 2 (Ap = 2[fCW − 0.5]). The paper treats them interchangeably in the NaMaster configuration narrative, but Cℓ amplitudes scale as the square of any field rescaling. Without an explicit, single convention and statement of the corresponding rescaling applied to all reported Cℓ, the MASTER outputs are not auditable.
- Required fix: Choose a single data-vector definition (either Ap or fCW−0.5), state it once, and ensure every reported Cℓ and z uses that choice (with units consistent). If both were used in different runs, label them distinctly, apply the correct rescalings, and update all affected numbers.

P4-E11 (Section II B, page 3): Training-set size arithmetic error and downstream percentage inconsistency
- Offending text: “We assemble training labels from three sources: (1) 6,637; (2) 17,153; (3) 2,000 … The combined training set contains 26,636 images.”
- Problem: 6,637 + 17,153 + 2,000 = 25,790, not 26,636. The stated “67.6% of training labels derive from CE-ResNet” also then misaligns (67.6% of 26,636 ≈ 18,016; not 17,153).
- Required fix: Correct the component counts and total, and recompute the CE-ResNet fraction. Propagate any changes to subsequent percentages (e.g., “67.6%”) and to the train/validation split sizes, if stated elsewhere.

P4-E12 (Abstract; Section VI A; Appendix E b.): Ambiguous/incorrect definition of the “high-confidence” (HC) subsample used for injection tests
- Offending text:
  - Abstract: “471 049 high-confidence per-spiral after peqCW > 0.9.”
  - VI A: “empirical injection-recovery sweep on the HC-spiral subsample (N = 471,049) …”
  - Appendix E b.: HC-broad (peq > 0.6, N = 949,584); HC-strict (peq > 0.8, N = 624,660).
- Problem: “peqCW > 0.9” would select only CW with P>0.9 (excluding CCW), which is not a balanced HC spiral set. The HC counts elsewhere (peq > 0.6/0.8 for max over CW/CCW) suggest the intended criterion is max(peq_CW, peq_CCW) > threshold. The abstract’s phrasing is misleading and, as written, implies a different sample than used.
- Required fix: Define the HC criterion unambiguously (e.g., max(peq_CW, peq_CCW) > 0.9), confirm that N = 471,049 corresponds to that criterion on the footprint/mask used for injection tests, and align all HC sample mentions across abstract, body, and appendices.

MAJOR

P4-M12 (Section VI A, page 6): Inconsistent fsky used in Fisher-floor statement
- Offending text: “σ(A/2)≈0.048% at Nspiral = 3,201,160, fsky = 0.46”
- Problem: Neither principal mask elsewhere is fsky ≈ 0.46 (canonical 0.49005; subsample 0.659). Using a third, unstated mask fraction looks like a stale number and obscures the derivation.
- Required fix: Use the actual mask employed for the Fisher estimate, state its Npix and fsky explicitly, and show the derivation (or simulation procedure) that yields σ(A/2) ≈ 0.048%. If this was from an older mask, recompute for the current mask.

P4-M13 (Section VI, opening paragraph): Unsupported numeric claims for Catalog A significance
- Offending text: “Catalog A shows … +6.48σ pre-MASTER pseudo-Cℓ in the lowest bandpower…”
- Problem: No table/figure presents the numeric ingredients needed to audit “+6.48σ.” It is a central cautionary number but not traceable.
- Required fix: Provide the measured value, null mean, and null σ (or an empirical-rank p) for this Catalog A statement (main text or Appendix/Supplement), or remove the specific z-value.

P4-M14 (Sec. IV D footnote 1, page 4): Implausible trial-pool inflation factor without supporting calculation
- Offending text: “⟨Nall/Nspiral⟩ ≈ 1.49 propagates directly into the binomial variance…”
- Problem: Catalog-wide, Nall/Nspiral ≈ 8.47M/3.20M ≈ 2.65. While the subsample/canonical masks can change this ratio, 1.49 is unexpectedly small and no computation over the actual mask is shown.
- Required fix: Report the exact Nall and Nspiral on the mask used for this statement (canonical or subsample), and provide the measured ⟨Nall/Nspiral⟩ with uncertainty (or histogram). If 1.49 was from an earlier mask/version, recompute and update.

P4-M15 (Abstract; multiple locations): One-sided vs two-sided mapping of p-values to “Gaussian-equivalent σ” is inconsistent/unspecified
- Offending text: “pMC = 0.030, i.e. ≈ 1.9σ Gaussian-equivalent.” Also Appendix E e.: “family-corrected p-value is 0.0086 (≈ 2.4σ family-wise).”
- Problem: p = 0.030 maps to ≈ 2.17σ two-sided or ≈ 1.88σ one-sided; p = 0.0086 maps to ≈ 2.64σ two-sided or ≈ 2.41σ one-sided. The manuscript sometimes uses signed z-scores and sometimes maps p to “σ” without specifying one- vs two-sided tests.
- Required fix: State explicitly whether Gaussian-equivalent σ are one- or two-sided for all p-to-σ mappings, and use that convention consistently. Add the empirical-rank p alongside any “σ” for finite-MC nulls.

P4-M16 (Section IV E; Appendix C a.): Unsupported “maximum regional asymmetry 0.32%” and quartile claims
- Offending text: “our maximum regional asymmetry is 0.32%,” and “absence of monotonic peq quality-quartile scaling…”
- Problem: No table/figure in the paper supports these numbers; pointing to an external repository is not sufficient for PRD.
- Required fix: Include a concise table/figure (main text or Supplemental) showing regional asymmetry estimates with uncertainties and the quartile-by-quartile results referred to in the text.

P4-M17 (Appendix E b., page 9): Undefined “monopole-preserving dipole” estimator
- Offending text: “Catalog C-full +4.31σ monopole-preserving dipole collapses to +0.62σ …”
- Problem: The manuscript does not define the “monopole-preserving” dipole fit procedure, its null, or its relation to the headline, demonopole-subtracted analyses.
- Required fix: Define this estimator (data vector, weights, fit, null), or avoid introducing a new estimator name. If retained, provide enough detail to reproduce the +4.31σ number.

P4-M18 (Multiple places): “Equatorial coordinate slabs” not defined
- Offending text: “spatially uniform across 7 equatorial coordinate slabs…”
- Problem: It is unclear whether “slabs” are in RA, Dec, or both; bin boundaries and counts are not specified.
- Required fix: Define the slab scheme (coordinate axis, edges, per-slab N), and include the slab fractions with uncertainties (main or Supplemental).

MINOR

P4-N6 (Conclusions, page 7): Misrendered “≥107 galaxies”
- Offending text: “≥107 galaxies”
- Problem: This reads as “greater than or equal to 107” rather than 10^7.
- Required fix: Write “≥10^7 galaxies.”

P4-N7 (Table IV, page 5): Hemisphere-max z-value rounding inconsistency
- Offending text: “Hemisphere max|A| … (1.69±0.41)×10−3 → z = +4.42.”
- Problem: (3.48−1.69)/0.41 ≈ 4.37, not 4.42. Small, but the table should be internally exact given the displayed digits.
- Required fix: Recompute with the internal (pre-rounded) values and/or harmonize significant digits so the displayed z matches the displayed inputs.

P4-N8 (Table IV vs Table III): Units missing/inconsistent for Cℓ
- Offending text: Table IV lists pseudo-Cℓ values (e.g., 1.696×10−2) without units; Table III reports Cℓ in “×10^6 (sr)”.
- Problem: The same class of statistic should carry consistent units (or a clear statement that Table IV is a different, unitless pre-MASTER pseudo-Cℓ normalization).
- Required fix: Add units to Table IV and reconcile any normalization differences with Table III, or explain the difference in definitions.

P4-N9 (Appendix B d., Table V): Calibration test T7 unclear
- Offending text: “T7: Calibration qualitative PASS; result ‘< 50% at confidence > 0.9’.”
- Problem: The phrasing is ambiguous and does not correspond to a standard calibration metric (e.g., ECE, reliability curves).
- Required fix: Either define the qualitative criterion precisely or replace with a standard calibration summary (ECE value or a brief reliability curve description).

P4-N10 (Appendix C c., page 8): Number of hemisphere directions scanned
- Offending text: “across ∼650 tested directions,” combined with “NSIDEdir = 8.”
- Problem: NSIDE=8 corresponds to 768 HEALPix pixel centers. If a subset was used, state the exact number and the sampling scheme.
- Required fix: Clarify the number of hemisphere centers tested and how they were chosen; if 768 were scanned, update “∼650.”

P4-N11 (Various): One-off numeric claims without in-paper backing
- Examples: “per-cell +4.72σ,” “mean per-galaxy PCW stable to |Δ⟨pCW⟩| < 0.0016,” etc., are not tied to a figure/table in the paper.
- Required fix: Either gather these into a small supplemental table/figure or tone down/remove the exact σ where they’re not audited in-paper.

Explanation
This fresh pass focused on new arithmetic inconsistencies (notably the training-set size and factor-of-two field-definition ambiguity), missing units/definitions (Table IV), ambiguous/high-confidence subset definition in the abstract, mismatched fsky in the Fisher-floor statement, and several unsupported numeric claims lacking an in-paper audit trail. These were not explicitly covered in the initial review and will materially improve the paper’s methodological clarity and reproducibility once addressed.