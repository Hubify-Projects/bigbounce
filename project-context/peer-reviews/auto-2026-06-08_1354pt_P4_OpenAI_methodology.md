# P4 auto-2026-06-08_1354pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (9895 chars)
**Wall time**: 505.6s

---

Referee report on P4: “Survey-Scale Galaxy Chirality with Equivariant TTA …”

Scope of review
I assessed the paper for methodological rigor, statistical validity, internal arithmetic consistency, and clarity of estimator definitions. I recomputed the quoted σ, p-values, percentages, and ratios where possible from the numbers provided in the text and tables. Below I list specific findings with severity and required actions.

ESSENTIAL ISSUES (must be resolved for PRD)

P4-E1 (Sec. III C, Sec. IV C, Appendix A; pages 3–4, 7)
Problem: Inconsistent definition of the analyzed field A(n). In Sec. IV C, A_p is defined as (N_CW − N_CCW)/(N_CW + N_CCW) (spirals only). In Appendix A.a, the “headline dipole estimator” is described as using the monopole-subtracted CW-deficit map f_CW(n) − 0.5, while later in Appendix A.c the “Field” is stated as Ap = (N_CW − N_CCW)/N_total with N_total including NS galaxies. These definitions are not the same and will yield different Cℓ and null variances.
Required fix: Provide a single, unambiguous, equation-level definition of the exact map used for each estimator (real-space dipole, NaMaster ℓ = 1, canonical-mask bandpowers). If different fields are used for different tests, clearly label them and re-run all affected results for consistency. Remove the contradictory “/N_total” formulation if not actually used.

P4-E2 (Table II; page 4)
Problem: Internal arithmetic inconsistency in “Dev. (σ)” versus the listed uncertainties. For Tier A: (0.5079 − 0.5)/0.000279 ≈ 28.3σ, not 28.8σ as reported. For Tier B: (0.504 − 0.5)/0.000279 ≈ 14.34σ, not 14.6σ. For Tier C: (0.4974 − 0.5)/0.000279 ≈ −9.32σ in magnitude, not 9.5σ.
Required fix: Recompute the “Dev. (σ)” entries from the uncertainties actually printed in the table, or print the uncertainties used if different (e.g., using p(1 − p)/N with p ≠ 0.5 changes σ slightly). The table must be arithmetically self-consistent.

P4-E3 (Sec. IV C.b and Table III; pages 4–5)
Problem: The bandpower “Significance (σ)” entries are not reproducible from the reported Cℓ and σ_null values. Example: For ℓ_eff = 4, Cℓ × 10^6 = 3.210 and σ_null = 0.804 imply z ≈ 3.99, not +6.097. Several rows have a negative Cℓ but a positive “Significance (σ)”, which is impossible unless the null mean is negative and substantially offset (not shown).
Required fix: Add a “null mean” column for every row, or explicitly state that the significances are computed relative to non-zero (possibly negative) null means and provide those means. Adjust signs and magnitudes to be internally consistent.

P4-E4 (Abstract; page 1; Sec. IV D, Table IV; pages 4–5)
Problem: The canonical-mask post-MASTER residual is given as “+3.64σ (z = Δ/σ_null)” while also quoting an empirical rank p_MC = 0.030 (~1.9σ Gaussian equivalent) from N_MC = 500 permutations. Presenting “+3.64σ” as a headline for the same test while the rank-based p-value corresponds to ~1.9σ is misleading.
Required fix: Adopt a single significance summary per estimator. If both moment-based z and rank-based p are reported, clearly state which is primary and reconcile the interpretation. At minimum, state side-by-side that the moment-based z = +3.64 but the empirical p = 0.030 (≈ 1.9σ), and avoid implying a 3.6σ-level detection where the permutation test gives ~1.9σ.

P4-E5 (Sec. IV D, Table IV; page 5)
Problem: The “residual +1.68σ” for the pre-MASTER pseudo-Cℓ generative null is not reproducible from the numbers shown. Using Data = 1.696×10^−2 and Null mean ± std = (1.685 ± 0.007)×10^−2 gives z = (0.011/0.007) ≈ 1.57σ, not 1.68σ.
Required fix: Ensure the tabulated uncertainty reflects the actual standard deviation used to compute z (carry sufficient significant figures), or correct the z-value. The 99.3% reproduction ratio (1.685/1.696 = 0.9935) is fine.

P4-E6 (Sec. III A, IV C, VII.b; pages 3–4, 7)
Problem: Mixing σ-values from different null procedures without immediate, local qualification. The paper warns in the Introduction that σ values are not comparable across estimators, but elsewhere it juxtaposes “+3.64σ,” “0.43σ,” and “−0.122σ” in the same sentence (e.g., Conclusions b) without a local reminder. PRD requires extreme care to avoid reader misinterpretation.
Required fix: Whenever σ from distinct nulls appear in the same sentence/paragraph, add an explicit parenthetical “(not directly comparable; see Table I mapping)” or convert all to p-values for that comparison.

P4-E7 (Sec. VI A; page 6)
Problem: The Fisher floor derivation is insufficiently documented and includes an inconsistent f_sky. You state “Fisher Poisson floor at 3σ is ∼0.29% full-amplitude (from σ(A/2) ≈ 0.048% at N_spiral = 3,201,160, f_sky = 0.46).” Neither primary mask uses f_sky = 0.46 (canonical is 0.49005; subsample 0.659). σ(A/2) ≈ √(1/N) ≈ 0.0559% for N = 3.2M; 0.048% is not traceable from stated N and f_sky.
Required fix: Provide the exact formula and inputs used to compute σ(A/2) (including whether you are aggregating per-pixel then fitting a dipole), and correct f_sky. If 0.048% is from a weighted or effective-N calculation, show it.

P4-E8 (Sec. IV B; page 4)
Problem: Contradictory “asymmetry-suppression” factors and offsets. The text states “3.86× asymmetry-suppression factor from raw +2.05% to equivariant −0.53%,” but Table II shows raw +0.79% (not +2.05%) and equivariant −0.26% (not −0.53%). The ratio 0.79/0.26 ≈ 3.0, not 3.86.
Required fix: Correct the raw and equivariant monopole offsets to match Table II or correct Table II. Provide a single, consistent suppression factor with supporting numbers.

P4-E9 (Abstract, Table I; pages 1, 4)
Problem: Ambiguous use of n = 5,547,858 in the abstract for the “strict-superset subsample mask.” In Table I, 5,547,858 is “N_map weighted = Σ W_p” with W_p = N_all(p), not a count of objects “n” in the usual sense.
Required fix: In the abstract and main text, do not denote N_map,weighted as “n.” State it explicitly as “N_map,weighted = 5,547,858 (sum of per-pixel weights W_p = N_all)” to avoid confusion.

P4-E10 (Appendix A.a; page 7)
Problem: Statement “Monopole subtraction reduces decoupled C1 at ℓ = 1 from 2.30×10^−5 to 1.51×10^−5 (∼34%) and increases σ from +1.85 to +3.64 (the canonical-mask number).” This contradicts the earlier narrative that proper monopole subtraction should reduce mask-coupled leakage; also, the same +3.64σ is elsewhere described as the post-MASTER residual after monopole subtraction, but then you say monopole subtraction “increases σ.” This needs quantitative clarification.
Required fix: Provide both the pre- and post-monopole-subtraction C1 values, their null means and standard deviations, and explain how σ increased despite the amplitude decrease (e.g., if σ_null decreased more). Otherwise, correct the statement.

MAJOR ISSUES

P4-M1 (Sec. III A, Table I; pages 3–4)
Problem: Primary estimator declaration is present, but the precise null-generation protocol is under-specified in places. For the “isotropic bootstrap” real-space dipole p = 0.30 (N_MC = 10,000), it is unclear whether galaxy positions are fixed and labels shuffled, or if catalogs are isotropically rotated, etc. Similarly, “per-pixel shuffle” nulls appear but the unit of shuffling (within density deciles? within mask only?) varies across sections.
Required fix: For each null type in Table I, add one sentence specifying exactly what is held fixed and what is randomized. Ensure consistency with Appendix D’s “density-stratified” null.

P4-M2 (Sec. IV C.a; page 4)
Problem: Reported 0.43σ with p = 0.30 is inconsistent if mapped via a Gaussian (z = 0.43 corresponds to p ≈ 0.67 two-sided). You ascribe p to an isotropic bootstrap; nevertheless the simultaneous reporting of “σ” and p must be consistent within that estimator unless the “σ” is defined by a different metric.
Required fix: Report either z derived from the bootstrap p, or explain that “0.43σ” is an RMS-normalized amplitude unrelated to the bootstrap quantile and remove potential ambiguity.

P4-M3 (Sec. IV D; page 5 and Appendix D)
Problem: Look-elsewhere effect treatment is confusing. Appendix C states that a direct-MC look-elsewhere test with N = 10,000 random-label shuffles yields p_LEE ≤ 10^−4 (i.e., zero exceedances), while also stating that a “conservative Bonferroni/BH penalty across ∼650 directions” reduces post-LEE significance to <1σ. If the direct-MC already built the null of the maximum statistic across scanned directions, Bonferroni/BH is a second, unnecessary penalty.
Required fix: Clarify how the look-elsewhere null was constructed. If the null was the max-statistic across directions per shuffle, then p_LEE from that max-statistic is the family-wise corrected p and no further Bonferroni is appropriate. If not, regenerate the proper max-statistic null.

P4-M4 (Sec. VI A; page 6)
Problem: The “falsification criterion” is not methodologically well posed. Stating that “a future survey detecting a chirality dipole at σ > 5 with full amplitude ≳ 0.75% would falsify the present null” conflates a method- and sample-specific sensitivity threshold (0.75% at your HC subsample) with a universal falsification amplitude.
Required fix: Rephrase to a survey- and pipeline-agnostic criterion (e.g., “at the same footprint and pipeline, a >5σ detection with amplitude significantly above our 3σ injection-recovery threshold would contradict our null; different footprints and pipelines require a matched analysis”).

P4-M5 (Terminology and notation; multiple pages)
Problem: “C 2 2° apodization” is unclear. Is this a “C2” cosine apodization of 2°? This is not standard NaMaster nomenclature.
Required fix: Define the apodization kernel explicitly (e.g., “cosine apodization with a 2° taper”) and specify the exact NaMaster function and parameters.

MINOR ISSUES

P4-n1 (Abstract vs Sec. VI A; pages 1, 6)
Problem: The “factor of ∼6–12” amplitude incompatibility with Shamir’s ∼3% signal is not derived. From your empirical 50%-recovery 3σ threshold A ≈ 0.75%, 3%/0.75% ≈ 4, not 6–12. Using the debiased “true underlying threshold ~1.88%” gives 3%/1.88% ≈ 1.6.
Required fix: Provide the explicit calculation that yields “6–12” or correct the factor to match your own thresholds.

P4-n2 (Sec. II B; page 2)
Problem: “GZ1 cross-match on 234,282 disjoint matches yields 69.91% accuracy” conflicts with earlier that only 6,637 GZ1 labels were used for training. It is not clear how many GZ1 chirality labels exist and how the cross-match sample was constructed.
Required fix: Clarify whether the 234,282 set is Galaxy Zoo DESI (GZD) not GZ1, and describe the cross-match selection and quality criteria.

P4-n3 (Sec. V B; page 6)
Problem: “CE-ResNet achieves cw/ccw = 0.998” is ambiguous (ratio vs fraction). 
Required fix: State explicitly whether this denotes cw/(cw + ccw) = 0.499 or cw/ccw = 0.998, and cite the exact metric from [7].

P4-n4 (Appendix A.a; page 7)
Problem: The mean monopole value “⟨A⟩_mask,gw = −0.005294” implies a spiral-only normalization; if “A” were defined with N_total in the denominator, this number would differ. This reinforces P4-E1 but can also be corrected by clarifying which denominator is actually used.

P4-n5 (Formatting/typos; multiple)
- “strict-superset subsample mask” is not defined; please define this term when first used.
- Ensure consistent use of f_sky values: 0.49005 (canonical), 0.659 (subsample), and avoid introducing 0.46 without definition.
- Replace informal “seed = 42” with “random seed fixed to 42 for reproducibility.”

NITS

P4-N1 (Style; multiple)
Problem: Occasional heavy internal jargon (“canonical-N,” “leg-proxy ℓ = 1 partial closure”) hinders clarity.
Required fix: Add brief parenthetical explanations on first use.

P4-N2 (References; page 10)
Problem: Check that all claimed statistics (e.g., CE-ResNet cw/ccw balance) are traceable to the cited papers’ abstracts or main results. Some are paraphrased; add exact table/section pointers if possible.

P4-N3 (Length)
The paper length (11 pages) is acceptable for PRD Methods, provided the essentials above are corrected and the estimator definitions consolidated. No reduction required.

## Summary recommendation
MAJOR REVISIONS

Justification: The paper presents a potentially valuable catalog and a careful pipeline with multiple nulls, but there are several essential inconsistencies that compromise methodological clarity: (i) contradictory definitions of the analyzed field; (ii) arithmetical inconsistencies in tables and significance mappings; (iii) ambiguous mixing of σ and p across different nulls; and (iv) unclear look-elsewhere handling. These issues are fixable with careful revision and re-computation. Once corrected and clarified, the statistical conclusions (null ℓ = 1 dipole on the subsample mask; canonical-mask residual attributed to systematics) may be sound, but the present manuscript does not yet meet PRD’s standards for methodological rigor and internal consistency.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (additional to prior report)

ESSENTIAL ISSUES

P4-E11 (Sec. IV B p.4; Appendix A.a p.7; Abstract p.1)
Problem: Systematic factor-of-two convention mix-ups between “monopole offset” and “asymmetry.” The body uses both:
- cw fraction offset: fCW − 0.5 = −0.0026 (−0.26% from Table II, Tier C = 0.4974).
- asymmetry A ≡ (NCW − NCCW)/(NCW + NCCW) with mask-mean ⟨A⟩mask,gw = −0.005294 (−0.5294%).
The text in Sec. IV B claims “equivariant −0.53%,” which matches the asymmetry A, but Table II reports −0.26% relative to 0.5. These are different observables (A = 2(fCW − 0.5)). The abstract and multiple sections intermix them.
Required fix: Adopt one convention per statement and annotate explicitly (e.g., “fraction offset relative to 0.5” vs “A monopole”). Recompute all quoted “suppression factors,” mask-mean subtractions, and any quantities that depend on the monopole using a consistent, labeled definition. Cross-check that Appendix A’s ⟨A⟩mask,gw = −0.005294 exactly corresponds to the same field used in the MASTER runs.

P4-E12 (Table III p.5; Appendix A p.7)
Problem: Cℓ units appear inconsistent with the field’s dimensionality. The asymmetry field A is dimensionless, so Cℓ should carry units of A^2 (dimensionless). Table III labels columns as “Cℓ × 10^6 (sr)” and “σnull × 10^6 (sr),” implying steradian units, which is not standard for a dimensionless scalar field’s angular power spectrum in the pseudo-Cℓ formalism as implemented by NaMaster.
Required fix: State clearly the units output by your NaMaster pipeline for a scalar, dimensionless field and correct the Table III units accordingly. If a solid-angle factor convention is in use, document it and make it consistent across text and tables.

P4-E13 (Appendix D.f p.9)
Problem: Implausible z-scores and missing reproducible inputs for the WLS dipole template fits. You report z ≈ −264.5 (naive WLS), and after block-bootstrap inflation by 14.7×, z ≈ −18.1; in an extended model, z ≈ −250. These magnitudes are extreme and not reproducible from provided numbers (no mean, variance, or covariance given).
Required fix: Provide the exact point estimate, covariance (or bootstrap distribution) of Adipole, and the reference “interpretation (i) amplitude” with a precise mapping used to compute these z’s. Confirm sign conventions (negative z for a disfavored positive-amplitude hypothesis) and show a sanity check that the bootstrap variance scaling is correctly propagated. Absent this, these z-values should be removed or replaced with properly derived quantities.

P4-E14 (Table III p.5; text p.5)
Problem: “Joint χ2/dof (38 bandpowers) = 161.2/38 = 4.24” is not reproducible or auditable from the presented subset of bandpowers. Table III shows one ℓ = 1 line plus five low-ℓ bandpowers; the 38 bandpowers used for χ2 are neither listed nor summarized (means/σ/DoF and binning scheme).
Required fix: List or provide in a supplement the full 38 bandpowers, their null means and variances, and the exact χ2 construction (whitened by diagonal σ only vs full covariance). Otherwise, do not quote the 38-dof χ2 result in the main text.

P4-E15 (Appendix A.a–c p.7; Sec. IV C p.4–5)
Problem: Potential bias/variance inconsistency from mixing Ap defined on spirals with a NaMaster weight Wp = Nall (all galaxies). You form the scalar field from spirals only (NCW, NCCW) but weight/mask it by total counts including NS. That choice can change the effective noise model and the null variance relative to a spiral-only weight Wp = Nspiral.
Required fix: Justify this weighting choice with a sensitivity test: rerun key NaMaster results (ℓ = 1 on the subsample mask and canonical residual) with Wp = Nspiral and compare C1 and σnull. Report any differences. If the choice is material, standardize on one approach and propagate changes.

P4-E16 (Appendix C.b–c p.8; Table I p.4)
Problem: Hemisphere look-elsewhere reporting lacks precise trial accounting and sidedness. You state testing “all hemisphere-pairs at 10° increments” but do not specify the exact number of hemisphere centers scanned; Table I reports pLEE ≤ 10−4 with N = 10,000 shuffles, while the text later applies an additional Bonferroni/BH penalty. Also, “≤ 10−4” is imprecise for zero exceedances; and one-/two-sided handling is unstated.
Required fix: Specify the exact scan grid size and how the max-statistic was constructed per shuffle. Report the finite-sample FWER p-value as (r + 1)/(N + 1) with r exceedances (and indicate if one- or two-sided), and remove any redundant second penalty if the null already uses the maximum statistic.

MAJOR ISSUES

P4-M6 (Sec. IV D p.5, footnote 1)
Problem: The claim that switching the generative null to Nall-trial draws would change the headline pre-MASTER reproduction by “sub-0.1σ” is unsupported. Trial-pool size directly sets per-pixel binomial variance and can impact leakage-driven pseudo-Cℓ amplitudes.
Required fix: Perform and report the Nall-trial generative null, and compare the pre-MASTER pseudo-C(ℓ=1) reproduction and σ with Nspiral-trial. Do not rely on an a priori “expected” effect here.

P4-M7 (Appendix D.a p.8)
Problem: The apodized-mask robustness test (“+3.57σ at fsky = 0.482”) lacks the underlying numbers (C1, null mean, σnull). The magnitude and direction of any change are not auditable.
Required fix: Provide the apodized-mask ℓ = 1 C1 value, null mean, σnull, and the exact apodization function/parameters (see also P4-M5 in the prior report) so the +3.57σ can be independently checked.

P4-M8 (Sec. VII.a p.6; Sec. IV D p.5)
Problem: Overstated generalization: “The prior literature’s pre-MASTER dipole-detection claims are therefore explained at the percent level by this leakage channel under our DESI/ViT-Small pipeline.” This asserts an explanation across surveys/pipelines without a matched-footprint/matched-method replication.
Required fix: Soften to a qualified statement (e.g., “we demonstrate a mechanism that can produce similar pre-MASTER excess under our pipeline and footprint; explaining prior claims requires matched-footprint/method tests we have not performed here”) or provide such a replication.

P4-M9 (Appendix E.d p.9 vs Sec. IV C p.4)
Problem: Threshold-sweep robustness phrasing is potentially misleading. You state that varying the per-pixel minimum from 5 to 50 shows “<0.5σ variation in the headline ℓ = 1 MASTER result,” while the headline result is −0.122σ. A ±0.5σ swing around −0.122σ implies sign and magnitude can change substantially under threshold choices.
Required fix: Report robustness in terms of C1 amplitude and its uncertainty, not only z-units. Provide a plot/table of C1 and σnull vs threshold so readers can assess stability.

P4-M10 (Appendix D.g p.9)
Problem: Notation misuse: “direct cross-spectrum rℓ=2 = −0.65 with σ = −2.89” mixes a correlation coefficient with a z-score and uses a negative “σ.” σ should be non-negative; the signed test statistic should be denoted z (or t).
Required fix: Rephrase as “rℓ=2 = −0.65; z = −2.89 against permutation null (two-sided p = …)” and provide the permutation-derived p-value.

MINOR ISSUES

P4-n6 (Sec. IV A p.4)
Problem: Percentages vs counts slight mismatch. 3,201,160/8,474,531 ≈ 37.77%, not 37.78% as printed. If rounding, consider standardizing to two decimals or report the exact fraction with consistent rounding.

P4-n7 (Appendix B.a p.7; Sec. IV A p.4)
Problem: “Mean classification confidence is 0.951, median 0.9997” is underspecified. Confidence = max softmax after Z2-TTA? Before/after Platt calibration? On which subset (all classes vs spirals only)?
Required fix: Define “confidence” precisely and specify the population over which means/medians are computed.

P4-n8 (Appendix C.c p.8; Table I p.4)
Problem: For N = 10,000 shuffles with zero exceedances, the proper finite-sample bound is p < 1/(N + 1) ≈ 9.99 × 10−5, not “≤ 10−4.” Please use the (r + 1)/(N + 1) convention.

P4-n9 (Sec. IV D p.5; Abstract p.1)
Problem: The mapping from permutation pMC = 0.030 to “≈ 1.9σ Gaussian-equivalent” is ambiguous with respect to one- vs two-sided mapping. Two-sided 0.030 corresponds to z ≈ 2.17, while one-sided 0.030 corresponds to z ≈ 1.88.
Required fix: State explicitly whether Gaussian-equivalent σ are one- or two-sided throughout and standardize on one convention.

P4-n10 (Table IV p.5)
Problem: “NSIDEdir = 8” is non-standard notation. If you mean the directional search grid for hemisphere tests at HEALPix NSIDE = 8, please state “HEALPix NSIDE = 8 grid of directions” for clarity.

P4-n11 (Sec. IV D.d p.5)
Problem: The density-stratified null reports null mean = 3.44 × 10−6 and std = 3.07 × 10−6 with z = +3.80 but does not display the corresponding data C1. Back-solving gives C1,data ≈ 15.13 × 10−6. Please print C1,data so the z can be verified directly.

P4-n12 (Appendix A.b p.7)
Problem: The binning description uses NaMaster API names verbatim. For readability, also state in plain language that ℓ = 1 is treated as a single multipole bin (nlb = 1) up to ℓmax = 191.

P4-n13 (Sec. V B p.6)
Problem: The comparison to CE-ResNet mixes ratio and fraction conventions (see also prior P4-n3). Ensure both pipelines are compared using the same metric (e.g., cw fraction relative to 0.5 or A) and cite the exact section/table in [7] that reports the CE-ResNet balance.

Rationale for additional pass
These new findings primarily address:
- A: Arithmetic/convention inconsistencies not previously called out (P4-E11, P4-n9, P4-n11).
- C: Dimensional consistency and unit labeling for Cℓ (P4-E12).
- I: Appendix/main-text mismatches and non-reproducible extreme z-scores (P4-E13, P4-E14, P4-M7).
- E: Null-procedure clarity for LEE and weighting choices (P4-E15, P4-E16).
- F/H: Overstated claims and hedged language without quantitative backing (P4-M8, P4-M9, P4-M10, P4-n7–n10).

Addressing these will materially improve methodological rigor and reproducibility.