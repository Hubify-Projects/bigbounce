# P4 auto-2026-06-06_0004pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8626 chars)
**Wall time**: 263.9s

---

Referee report on “Survey-Scale Galaxy Chirality with Equivariant TTA: A −0.122σ Subsample-Mask ℓ=1 Null, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)”

Overall scope and focus
The manuscript presents a large-scale galaxy-chirality catalog and a multi-estimator dipole analysis. The primary result is an ℓ=1 null on a subsample mask and a diagnosis of monopole–mask leakage on a canonical patchy footprint. The paper is methods-driven and aligns with PRD’s methodological standards in intent. However, there are multiple internal inconsistencies and ambiguities in the statistical definitions, estimator scaling, significance reporting, and sample definitions that must be resolved. Several load-bearing scalars in the abstract and conclusions are not traceable or are inconsistent with numbers in the body. Below I list findings with severity and required fixes.

Findings

ESSENTIAL

P4-E1
- Location: Abstract (page 1), Sec. VI A (page 6), Appendix E (page 9), Table I (page 4)
- Problem: Ambiguity/inconsistency in the definition of the “high-confidence” (HC) subsample used for injection–recovery. The abstract states “471 049 high-confidence per-spiral after peqCW > 0.9” which implies an asymmetric threshold on the CW channel only. Elsewhere, HC thresholds are peq > 0.6 (N=949,584) and peq > 0.8 (N=624,660). The 471,049 sample is referenced again in Sec. VI A but never defined. Using peqCW > 0.9 is not symmetric between CW and CCW and would bias selection.
- Required fix: Precisely define the HC selection for N=471,049 (e.g., max(Peq_CW, Peq_CCW) > 0.9) and state it consistently (abstract, Sec. VI A, Table I caption/footnote, Appendix E). If the abstract’s condition is a typo, correct it. Report both CW and CCW counts passing the HC cut and confirm no handedness asymmetry is induced by the HC selection. Re-compute any HC-derived results if the symmetric criterion changes N.

P4-E2
- Location: Sec. IV D (page 4), Table IV (page 5), Appendix C.b (page 8)
- Problem: Inconsistent hemisphere asymmetry results. In Sec. IV D: “local hemisphere maximum of 3.05σ,” but Table IV reports +4.42σ for “Hemisphere max|A| (NSIDEdir=8).” Appendix C.b again states 3.05σ using 10°-increment hemispheres. These are different direction grids (∼650 vs 768 directions) but the paper does not make this explicit where the conflicting σ values are juxtaposed in the main text.
- Required fix: Present both hemisphere scans in one place with clear definitions (grid type, number of directions, masking, weighting, and null). Report both p-values and σ consistently. If Table IV corresponds to NSIDEdir=8 (768 hemispheres) and Appendix C to a 10° grid (∼650 hemispheres), say so explicitly in Sec. IV D and reconcile the publicized number in the main text. Do not mix grids without stating so; do not cite 3.05σ in the main text if Table IV is the canonical value for the adopted null.

P4-E3
- Location: Appendix A (page 7), Sec. III C (page 3), Sec. IV C (page 4)
- Problem: Factor-of-two ambiguity for the data vector used in NaMaster. Appendix A says “headline estimator uses the monopole-subtracted CW-deficit map fCW(n)−0.5,” then also defines “the asymmetry field Ap = (NCW−NCCW)/(NCW+NCCW).” Since Ap = 2 fCW − 1, fCW − 0.5 = Ap/2. It is unclear whether the pseudo-Cℓ are computed on fCW−0.5 or on Ap. This scaling directly rescales all reported Cℓ values (and any amplitude mapping).
- Required fix: State unequivocally which field is fed to NaMaster for each reported Cℓ and bandpower (Ap or fCW−0.5), and ensure all numbers (means, variances, units, Cℓ magnitudes) are consistent with that scaling. If both fields are used in different places (e.g., diagnostics vs headline), label them and do not mix them. If any table values change under the corrected convention, update them throughout.

P4-E4
- Location: Sec. IV B (page 4), Table II (page 4), Appendix A (page 7)
- Problem: “3.86× asymmetry-suppression factor from raw +2.05% to equivariant −0.53%” contradicts Table II (raw +0.79%, equivariant −0.26%) and lacks a definition for the +2.05% number. The −0.53% appears to be the galaxy-weighted mask mean ⟨A⟩mask,gw = −0.005294 in Appendix A, but the +2.05% raw counterpart is never shown.
- Required fix: Define the quantity used for both ends of that comparison (e.g., pixel-weighted mean of Ap over the mask). Provide the corresponding raw value explicitly (with mask and weighting) and reconcile with Table II, or remove the 3.86× claim. Keep monopole metrics consistent (either unweighted catalog-level fractions or explicitly mask-weighted pixel means).

P4-E5
- Location: Table III (page 5), Sec. IV D (page 4), Appendix D.b (page 8)
- Problem: Bandpower significances are reported without the corresponding null means. Several bandpowers list Cℓ < 0 with positive σ values, which is impossible to interpret without ⟨Cnull⟩. Appendix D.b then quotes single-ℓ significances (e.g., σℓ=2 = +4.73) not directly tied to Table III’s bandpowers (ℓeff bins). The paper mixes single-ℓ and bandpower statistics without clear crosswalk.
- Required fix: For every row in Table III, report ⟨Cnull⟩ and define z = (Cmeas − ⟨Cnull⟩)/σnull explicitly. State whether the rows are single-ℓ or bandpowers and ensure Appendix D uses the same binning (or else provide both with clear mapping). Recompute and correct σ signs where needed.

P4-E6
- Location: Sec. VI A (page 6)
- Problem: Unexplained fsky = 0.46 used in the Fisher-floor calculation. Elsewhere the two operative masks have fsky = 0.659 and 0.49005.
- Required fix: Define the origin of fsky = 0.46 (mask, threshold, apodization), or correct it. If it is an effective sky fraction after additional cuts, state and justify it.

P4-E7
- Location: Sec. IV D (page 4), Appendix A (page 7)
- Problem: Inconsistent and ambiguous use of ntotal/Ntotal/Nall in the generative monopole-only null. Sec. IV D: per-pixel CW drawn from Binomial(ntotal, pglobalCW) “on the canonical mask,” but Appendix A defines Wp = Nall = NCW + NCCW + NNS for weighting. For a CW/CCW binomial, ntotal must be the per-pixel spiral count (NCW + NCCW), not Nall including NS.
- Required fix: Unify notation and explicitly state that binomial draws use per-pixel spiral counts (NCW + NCCW). If the implementation used Nall, re-run the generative null with the correct Nspiral per pixel and update Table IV accordingly.

P4-E8
- Location: Abstract (page 1), Sec. IV D (page 4), Sec. VII.b (page 6)
- Problem: Mixed significance reporting for the same canonical ℓ=1 result: “+3.64σ” from moment-ratio vs empirical rank pMC = 0.030 (≈1.9σ). Presenting +3.64σ as a headline significance while the empirical rank says 1.9σ is misleading.
- Required fix: Pre-declare a single significance mapping for each estimator and adhere to it. For the canonical-mask statistic, either (a) report only the empirical rank pMC and its Gaussian-equivalent z, or (b) report both but explain the discrepancy and do not describe +3.64σ as a point significance if the rank-based p contradicts it. Adjust all mentions (abstract, body, conclusions) to be consistent.

P4-E9
- Location: Sec. IV D (page 4)
- Problem: Internal version-history language: “were interpreted in earlier paper versions as …”
- Required fix: Remove all version-history phrasing from the scientific narrative.

P4-E10
- Location: Abstract (page 1), Table I caption (page 4), Appendix A (page 7)
- Problem: Misleading use of “n = 5,547,858” in the abstract to denote the “strict-superset subsample mask,” but that value is Nmap,weighted = Σp Wp (a sum of per-pixel weights), not a count of unique galaxies. Presenting it as n is dimensionally confusing.
- Required fix: Rephrase to “Nmap,weighted = 5,547,858 (sum of per-pixel weights Wp = Nall)” and do not denote it by n in the abstract. Ensure units and interpretations are consistent wherever this quantity appears.

MAJOR

P4-M1
- Location: Sec. IV E (page 5), Appendix D.c–f (page 8–9)
- Problem: Several diagnostics (cross-spectra rℓ, density-stratified null, WLS fits) report σ or p-values without stating the number of Monte Carlo realizations, precise null procedures, or whether masks/apodizations match the main estimator.
- Required fix: For each diagnostic, provide NMC, the null construction (permutation scope, stratum-preserving or not), and mask/apodization details. Report uncertainties on rℓ and p-values as appropriate.

P4-M2
- Location: Table III (page 5)
- Problem: “Joint χ2/dof (38 bandpowers) = 161.2/38 = 4.24” is not auditable: only 6 rows are displayed and the binning scheme for 38 bandpowers is undefined.
- Required fix: Define the full binning used to produce the 38 bandpowers and provide at least a supplementary table or figure summarizing them and the corresponding null covariance used in χ2. Alternatively, remove this χ2 summary if it is not central.

P4-M3
- Location: Sec. V A (page 5), VI B (page 6)
- Problem: Over-interpretation of “inconsistency by a factor of ∼6–12” with Shamir’s claimed ∼3% amplitudes. This claim is not quantitatively derived in the text; it mixes a 3σ detection threshold (0.75%) with someone else’s reported amplitude without a consistent estimator mapping or footprint match. Although you disclaim a formal exclusion, the “6–12” factor is not justified.
- Required fix: Either (a) provide a precise quantitative mapping that shows how a ∼3% dipole in your pipeline would manifest in your estimators (including your dilution factor g and footprint), with uncertainties; or (b) remove the “factor of ∼6–12” phrasing and keep only the qualitative statement and the “matched-footprint reanalysis required” caveat.

P4-M4
- Location: Throughout (e.g., Sec. IV C–D, Table I–III)
- Problem: Over-precision in significance values given small NMC. For example, −0.122σ from 500 MC draws is quoted to three decimals; “99.3%” replication from 500 nulls is quoted to 0.1%.
- Required fix: Round z-scores and replication fractions to reflect the sampling error from finite NMC (e.g., z = −0.12, 99.3% ± 0.5%). Where possible, add uncertainty bands on σnull and on pMC.

MINOR

P4-m1
- Location: Table II (page 4), Sec. IV B (page 4)
- Problem: The reported “Dev. (σ)” for Tier C is 9.5σ. Using N=3,201,160 and p=0.4974, σbin ≈ 0.0002795 and z ≈ 0.0026/0.0002795 = 9.32. The difference is small but should be consistent.
- Required fix: Recompute and round consistently (e.g., 9.3σ), or explain the slight discrepancy (mask-weighting vs catalog-level fraction, if that’s the cause).

P4-m2
- Location: Sec. V A (page 5), Table IV (page 5)
- Problem: “maximum regional asymmetry is 0.32%” vs Table IV’s 3.48×10−3 = 0.348% for hemisphere max|A|.
- Required fix: Harmonize the quoted maximum regional asymmetry. If 0.32% refers to a different region definition, state it.

P4-m3
- Location: Appendix A (page 7)
- Problem: Formatting of “C 2 2◦ apodization” is unclear.
- Required fix: Specify the exact apodization scheme (e.g., “cosine-squared apodization with 2° scale”) and apply consistent notation.

P4-m4
- Location: Sec. IV D (page 4), Table IV (page 5)
- Problem: The null for the hemisphere max|A| uses NSIDEdir=8, but Appendix C uses a 10° grid. The number of tested directions (∼650 vs 768) is mixed across the text (including the LEE penalty language).
- Required fix: State explicitly the direction grid used for each test and unify the LEE treatment. Using a max-statistic permutation null already accounts for the LEE; remove or clearly separate Bonferroni/BH commentary to avoid double-penalization.

P4-m5
- Location: Sec. IV C (page 4), Appendix A (page 7)
- Problem: Occasional ambiguity between Ntotal (spirals only) and Nall (spirals+NS) in denominators and weights.
- Required fix: Add a boxed notation summary (e.g., Nspiral(p) = NCW+NCCW, Nall(p) = Nspiral+NNS) and ensure all appearances use the correct symbol.

P4-m6
- Location: Sec. IV C (page 4)
- Problem: The isotropic-bootstrap dipole p=0.30 is stated without a definition of the bootstrap (resampling unit, with/without replacement, weighting).
- Required fix: Define the bootstrap procedure (galaxy-level vs pixel-level, stratified or not, number of resamples, exact test statistic).

P4-m7
- Location: Sec. IV E (page 5)
- Problem: Cross-spectrum C(Ap × ntotal) at ℓ=2 gives r = −0.65 with σ = −2.89 without stating NMC or the null definition for r.
- Required fix: Provide NMC, null procedure, and mask/apodization.

P4-m8
- Location: Data Availability (page 9)
- Problem: Broken URLs from line breaks/hyphenation (e.g., “dataset s/bamfai/galaxy- chirality- catalog”).
- Required fix: Provide validated, copyable URLs in the final version.

P4-m9
- Location: Sec. III B (page 3), Appendix B (page 7)
- Problem: The flip-consistency loss with λ = 0.5 is introduced without sensitivity analysis or justification.
- Required fix: Briefly justify the choice or report the robustness to a reasonable range of λ.

NIT

P4-n1
- Location: Throughout
- Problem: Inconsistent capitalization (“cw/ccw” vs “CW/CCW”), occasional spacing/hyphenation artifacts.
- Required fix: Standardize capitalization and fix typographical artifacts.

P4-n2
- Location: Sec. IV D (page 4), Appendix C.c (page 8)
- Problem: LEE discussion risks double-penalizing by combining a max-statistic permutation pLEE with a Bonferroni/BH factor.
- Required fix: Clarify that the max-statistic pLEE already accounts for trials; if Bonferroni/BH is mentioned, make it explicit that applying both is conservative and not used for primary conclusions.

P4-n3
- Location: Sec. VII (page 6)
- Problem: The falsification criterion (“σ > 5 with amplitude ≳ 0.75%”) blends significance and amplitude thresholds tied to the current pipeline’s sensitivity floor.
- Required fix: Rephrase to indicate this is a pipeline-dependent benchmark, not a universal falsification of the cosmological null.

P4-n4
- Location: Sec. II B (page 2), V B (page 5)
- Problem: CE-ResNet “cw/ccw = 0.998” phrasing is unclear (ratio or fraction?).
- Required fix: State explicitly whether this is the CW fraction (≈0.499) or the CW/CCW ratio.

P4-n5
- Location: Appendix B.d (page 7–8)
- Problem: D4-TTA validation statements mix argmax label flips and mean-p differences; the message is qualitative.
- Required fix: Consider adding a short quantitative metric (e.g., mean absolute difference in Peq across D4, with CI) for completeness.

Length and scope
The manuscript is 10 pages with multiple appendices. Given the methodological focus, this is acceptable. However, once the essential corrections are made (especially clarifying definitions and unifying significance/reporting), some repetition can likely be trimmed. I do not recommend a strict page cap, but a tighter, crisper presentation would help after revisions.

## Summary recommendation
MAJOR REVISIONS

The paper presents a potentially important negative result with substantial methodological effort, but there are multiple essential inconsistencies in definitions (HC subsample), estimator scaling (Ap vs fCW−0.5), significance reporting (3.64σ vs pMC=0.030), mask fractions (fsky=0.46 vs 0.659/0.490), and hemisphere-scan results (3.05σ vs 4.42σ) that must be reconciled. Table III’s bandpower significances are not auditable without null means. These are fixable issues, but the paper cannot be accepted at PRD’s standards without addressing them comprehensively and consistently across the abstract, body, tables, and appendices.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

ESSENTIAL

P4-E11
- Location: Appendix A (page 7) vs Eq. (3) (page 4)
- Problem: Inconsistent definition of the asymmetry field denominator. Earlier (Eq. 3) Ap = (NCW − NCCW)/(NCW + NCCW), spirals only. Appendix A first repeats this, but later (Appendix A.c, “Field”) defines Ap = (NCW − NCCW)/N(p)total, which includes NS. This changes amplitudes and units of all reported Cℓ and cross-spectra.
- Required fix: Unify the field definition across the paper. If Ap is spirals-only, ensure all NaMaster and diagnostic fields use Nspiral(p) in the denominator and correct any results that used Nall(p). If you intend to use the “CW-deficit” field fCW − 0.5 instead, state so and keep the scaling consistent everywhere.

P4-E12
- Location: Table IV (page 5)
- Problem: Arithmetic mismatch in the z-score for the pre-MASTER pseudo-C(ℓ=1)ℓ statistic. Using the table’s own numbers: z = (1.696 − 1.685)/0.007 = 1.57, not +1.68.
- Required fix: Recompute and correct the reported z, and propagate any dependent text that cites +1.68σ.

P4-E13
- Location: Appendix E.b (page 9)
- Problem: Stale/undefined estimator. “Catalog C-full +4.31σ monopole-preserving dipole” is introduced without prior definition of the “monopole-preserving” dipole estimator and directly contradicts the main-text Catalog C real-space dipole of +0.43σ.
- Required fix: Define the “monopole-preserving dipole” estimator (mask, weighting, null) and explain how it differs from the main dipole fit; reconcile why Catalog C yields +0.43σ in the main text but +4.31σ here. If this is an outdated number or a different pipeline, remove or move to diagnostics with full specification.

P4-E14
- Location: Sec. IV E (page 5), Appendix D.c (page 8)
- Problem: Dimensional inconsistency in the cross-spectrum C(Ap × ntotal). Ap is dimensionless; ntotal is a count field. The cross-power then has arbitrary units and varies with depth normalization. The correlation coefficient rℓ is quoted, but the underlying normalization and null for r are not stated here, and using unnormalized counts risks depth leakage by construction.
- Required fix: Use a normalized depth template (e.g., ñ = (ntotal − ⟨ntotal⟩)/⟨ntotal⟩), or explicitly state the normalization used to render the cross-spectrum dimensionless. Provide NMC, the null procedure for rℓ, and confirm mask/apodization match the auto-spectrum.

P4-E15
- Location: Sec. IV C.b (page 4) vs Appendix A (page 7)
- Problem: Order-of-magnitude mismatch for ℓ=1 amplitudes without a scaling crosswalk. Sec. IV C.b (subsample mask) reports C1 = 1.494×10−6; Appendix A (canonical-mask context) reports 1.51×10−5 after monopole subtraction. This ≈10× discrepancy is larger than the Ap vs fCW−0.5 factor-of-4 and is not explained by mask choice or binning in the text.
- Required fix: Provide a clear crosswalk showing, for the same field definition and units, the ℓ=1 amplitudes on the different masks, and quantify how field scaling (Ap vs fCW−0.5), mask, and apodization change C1. If different nulls/binnings are used, state them side-by-side.

P4-E16
- Location: Sec. VI A (page 6)
- Problem: Arithmetic inconsistency in the Fisher-floor calculation. The stated σ(A/2) ≈ 0.048% given Nspiral = 3,201,160 and fsky = 0.46 does not match binomial expectations. With Nspiral alone, σ(A/2) ≈ 0.028%; with N_eff ≈ fsky·Nspiral = 1.47M, σ(A/2) ≈ 0.041%. The quoted 0.048% implies N_eff ≈ 1.09M (f_eff ≈ 0.34), inconsistent with fsky = 0.46.
- Required fix: Recompute σ(A/2) from the stated N and fsky (or remove fsky from this real-space estimate if not applicable), and adjust the 3σ floor accordingly. State precisely how fsky enters this Fisher estimate or drop fsky if it shouldn’t.

MAJOR

P4-M5
- Location: Table II (page 4)
- Problem: Additional arithmetic inconsistencies beyond P4-m1. Using σbin = sqrt(p(1−p)/N) with N=3,201,160: Tier A z = (0.5079−0.5)/0.0002795 ≈ 28.3 (paper: 28.8). Tier B z = (0.5040−0.5)/0.0002795 ≈ 14.3 (paper: 14.6).
- Required fix: Recompute and round consistently. If a different σbin was used (mask-weighted N, effective N), specify it in the caption and apply it to all tiers.

P4-M6
- Location: Appendix A (page 7), Table III caption (page 5)
- Problem: Cℓ units ambiguous/inconsistent. Table III labels “Cℓ × 10^6 (sr)” while the field Ap is dimensionless. For a dimensionless scalar field, Cℓ is dimensionless (or quoted in “sr” only if using a specific harmonic normalization). The mix of “×10^6” and “(sr)” without a stated convention is unclear.
- Required fix: State the harmonic convention (Healpix/spherical harmonics normalization) and the resulting Cℓ units. Either remove “(sr)” or justify it; ensure all Cℓ values and σnull use the same unit convention.

MINOR

P4-m10
- Location: Appendix A.b (page 7), Sec. III C (page 3)
- Problem: Over-precision claim “flip-swap correlation = 1.000.” Given finite precision and stochastic training, this is unlikely to be exactly 1.000 absent a provable algebraic constraint.
- Required fix: Report with realistic precision (e.g., 0.9999±…) and define how the correlation was computed (sample, confidence weighting).

P4-m11
- Location: Sec. IV B (page 4), Appendix A (page 7)
- Problem: The “MASTER decoupling removes the canonical-mask pseudo-Cℓ leakage” phrasing is too strong given the persistent +3.64σ post-MASTER canonical residual. While you later qualify this by using the subsample mask for the headline null, the sentence as written suggests full removal.
- Required fix: Rephrase to “substantially reduces” or explicitly limit the statement to the subsample-mask estimator; avoid implying complete removal on the canonical footprint.

P4-m12
- Location: Sec. IV C.b (page 4), Appendix A (page 7)
- Problem: The subsample-mask ℓ=1 result is provided with full numerical detail, but the corresponding canonical-mask post-MASTER ℓ=1 amplitude (not just σ) is missing from the main text; only Appendix A gives a number (1.51×10−5) without null stats.
- Required fix: Add the canonical-mask post-MASTER ℓ=1 amplitude and its null mean/σnull in the main text or Table III (clearly labeled as canonical vs subsample), enabling a direct comparison of amplitudes as well as significances.

P4-m13
- Location: Appendix C.b (page 8)
- Problem: NGP/SGP hemisphere “σiso = +0.47 / +2.02” are given without null details (resampling unit, NMC, mask, weighting), unlike the main hemisphere max-stat tests.
- Required fix: Provide the null construction and NMC for these hemisphere splits, or move these to a qualitative note if not formally tested.

P4-m14
- Location: Table I (page 4)
- Problem: For consistency and auditability, Nmap,weighted is reported for the subsample-mask estimator but omitted for the canonical-mask estimator.
- Required fix: Add Nmap,weighted for the canonical mask (sum of Wp = Nall over masked pixels) to Table I and clarify if the same Wp definition is used for both masks.

NIT

P4-n6
- Location: Appendix D.f (page 9)
- Problem: The z-scores used to “disfavor interpretation (i)” are defined idiosyncratically (e.g., z ≈ −264.5 “from the naive WLS posterior”, then z ≈ −18.1 after block-bootstrap). This z is not the usual (Cmeas − ⟨Cnull⟩)/σnull but rather a comparison to a fixed reference amplitude; this redefinition is not clearly stated in the main text and risks confusing readers.
- Required fix: Explicitly define this alternative z as zref = (Aref − Â)/σ(Â), keep it out of sections that use the standard null-based z, and avoid mixing these different z definitions without an upfront warning.

P4-n7
- Location: Appendix A (page 7), Appendix D.a (page 8)
- Problem: Mask apodization usage is scattered: Appendix A states no apodization on the canonical mask; Appendix D.a reports a canonical apodization test. While not contradictory, the narrative could better delineate “analysis configuration” vs “stress-test configuration.”
- Required fix: Add a one-sentence clarifier that the canonical-mask headline NaMaster runs used a binary mask, and apodization was used only for a robustness stress test reported in Appendix D.

Explanation
These additions focus on arithmetic mismatches (notably Table IV), an internal contradiction in the field definition used for NaMaster (denominator inconsistency), an undefined “monopole-preserving dipole” estimator appearing only in an appendix with a 4.31σ claim, unit/dimensional ambiguities for Cℓ and cross-spectra, and missing crosswalks between amplitudes reported under different masks/field scalings. They also tighten a few over-precision/overstatement issues and request null-spec details for hemisphere splits.