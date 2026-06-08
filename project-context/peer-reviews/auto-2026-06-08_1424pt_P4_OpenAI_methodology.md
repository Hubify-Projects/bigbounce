# P4 auto-2026-06-08_1424pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8727 chars)
**Wall time**: 438.3s

---

Referee report on “Survey-Scale Galaxy Chirality with Equivariant TTA: A −0.122σ Subsample-Mask ℓ=1 Null, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)”

Scope of review: Statistical-method validity, derivations, dimensional consistency, internal arithmetic, error propagation, clarity about null procedures, and reproducibility.

Overall assessment
The manuscript presents a large-scale catalog and an ℓ=1 dipole-null analysis with multiple cross-checks and nulls. The work is ambitious and potentially important. However, there are critical methodological inconsistencies and several statistical-metrics issues that must be resolved before this can meet PRD standards. In particular: (i) a fundamental inconsistency in the definition of the chirality field used in the MASTER pipeline (spiral-only denominator vs all-galaxy denominator), (ii) inconsistent and potentially misleading use of “σ” for a non-Gaussian null (the canonical +3.64σ residual versus an empirical MC p-value ≈ 0.03), (iii) internal arithmetic inconsistencies in reported percentages and σ-levels, and (iv) an incomplete/“in queue” analysis in a load-bearing footnote. These are essential to fix for the results to be interpretable and reproducible.

Findings

ESSENTIAL

P4-E1
- Location: Sec. IV.C (p. 4), Eq. (3); Appendix A.a/c (p. 7)
- Problem: Inconsistent definition of the asymmetry map Ap used in the core NaMaster/MASTER analysis. In Sec. IV.C (Eq. 3) and footnote 1 (pp. 4–5), Ap is defined for spirals only with denominator NCW+NCCW, and the generative null is drawn from Nspiral(p). In Appendix A.c (p. 7), the field for NaMaster is explicitly stated as Ap = (NCW − NCCW)/Ntotal with Ntotal = NCW + NCCW + NNS. That is a different field. This is a load-bearing inconsistency that directly affects Cℓ and the headline ℓ=1 result.
- Required fix: Unify the definition of Ap across the paper. State clearly and consistently which denominator is used in all power-spectrum and dipole results (spirals-only vs total). If Appendix A.c’s Ntotal denominator was actually used, you must redo footnote 1 and any generative nulls accordingly. If the spirals-only denominator was used for all results, correct Appendix A.c and any other inconsistent passages. If any results change, update all affected numbers, uncertainties, and conclusions.

P4-E2
- Location: Abstract (p. 1), Sec. IV.D (pp. 4–5), Table I (p. 4), Appendix A (p. 7), Conclusions (pp. 6–7)
- Problem: Reporting “+3.64σ” for the canonical-mask post-MASTER residual while simultaneously stating the empirical permutation pMC = 0.030 (≈ 1.9σ Gaussian-equivalent) is internally inconsistent and risks misleading readers. The “σ” is computed as z = Δ/σnull assuming approximate normality, which is contradicted by the empirical rank. Several places in the manuscript (including Table I and the Conclusions) elevate the “+3.64σ” value despite the contradictory pMC.
- Required fix: Use a single, consistent significance metric for each result. For non-Gaussian nulls or where the empirical rank p disagrees with a Gaussian z, report only the empirical p (and optionally its Gaussian-equivalent z from p). Remove or demote the “+3.64σ” label in all locations (abstract, text, tables, conclusions), and present the canonical residual significance consistently as pMC = 0.030 (≈ 1.9σ equivalent) with a clear label that it derives from permutation nulls.

P4-E3
- Location: Sec. IV.B (p. 4)
- Problem: “The 3.86× asymmetry-suppression factor from raw +2.05% to equivariant −0.53%” is inconsistent with Table II values (raw 0.5079 = +0.79%, equivariant 0.4974 = −0.26%). The stated 2.05% and −0.53% do not match any values presented in Table II and appear to be from a different definition or dataset tier not documented in the main text.
- Required fix: Recompute and report the suppression factor from numbers actually shown in Table II, or explicitly define the alternative metric (e.g., A = 2p − 1) and show its values for Catalog A and C. Ensure consistency throughout the paper. If the 2.05%/−0.53% are correct under a different definition, provide those values in a table and explain the mapping.

P4-E4
- Location: Sec. VI.A (p. 6)
- Problem: Sensitivity floor arithmetic inconsistency. You state “Fisher Poisson floor at 3σ is ∼ 0.29% full-amplitude (from σ(A/2) ≈ 0.048% at Nspiral = 3,201,160, fsky = 0.46).” Using binomial shot noise with N = 3.201 × 10^6, σ(p) ≈ 0.0279% (for p ≈ 0.5), which implies σ(A/2) = σ(p) ≈ 0.0279%, not 0.048%. Your quoted fsky = 0.46 also conflicts with fsky values used elsewhere (0.49005 or 0.659). If you are employing an effective Neff to account for pixelization/weights, it must be defined and derived.
- Required fix: Provide a transparent derivation of the Fisher/Poisson floor, define Neff and how fsky enters, and make it consistent with the data vector actually used (mask, weighting, NSIDE, etc.). Correct the 0.29% and σ(A/2) figures if needed. If the floor is empirically larger for methodological reasons (e.g., weighting, pixelization), explain clearly.

P4-E5
- Location: Sec. IV.C.a (p. 4)
- Problem: Inconsistent mapping of “0.43σ” to p = 0.30 for the real-space dipole. A Gaussian two-sided z = 0.43 corresponds to p ≈ 0.67, not 0.30. If you are using an amplitude-only (one-sided, non-negative) test statistic, a proper mapping must be shown; otherwise the σ and p are inconsistent.
- Required fix: Define the test statistic (amplitude or signed component), specify whether p is one-sided or two-sided, and ensure the reported σ and p are consistent. If you intend to report only empirical bootstrap p, then do so; avoid attaching a contradictory “σ” label.

P4-E6
- Location: Sec. IV.D, footnote 1 (pp. 4–5)
- Problem: Footnote contains “in queue”/future-work text for a load-bearing generative-null variant and predicts expected shifts. PRD does not accept “to be done” language for central analyses.
- Required fix: Remove the “in queue/expected to shift” language. Either (i) complete the Nall-trial rerun and report the results, or (ii) state explicitly that it was not used in the present analysis and remove speculative statements about its effect.

P4-E7
- Location: Data Availability (p. 9)
- Problem: Broken/unverifiable URLs due to spaced/broken strings (“galaxy- chirality- catalog”, “gala xy-chirality-v2”). PRD requires verifiable, stable links (preferably with DOIs or archived snapshots).
- Required fix: Provide working, copy-pastable URLs without spaces and with version tags/DOIs. Confirm that the released artifacts exactly reproduce the paper’s numbers (models, code, catalogs). If possible, add permanent archives (e.g., Zenodo DOIs) for code, models, and data snapshots.

MAJOR

P4-M1
- Location: Throughout significance reporting; Table I (p. 4), Table III (p. 5), Sec. IV.C–D
- Problem: Small NMC for tails and over-precise “σ” claims. Several σ-levels are quoted to 2–3 decimals (e.g., −0.122σ, +6.097σ) with NMC = 500 permutations. The sampling error in σnull and tail estimates is non-negligible at this NMC, especially for |z| > 3. Also, Table III intermixes results from different masks/nulls in one table without reiterating the caution that σ-values are not directly comparable across nulls.
- Required fix: Increase NMC substantially (≥ 5,000–10,000) for any claim above ~3σ, or report empirical p-values with appropriate resolution (e.g., p < 1/NMC). Add local reminders in captions/notes to tables where σ from different nulls appear side-by-side that they are not directly comparable.

P4-M2
- Location: Appendix C.b–c (p. 8)
- Problem: Look-elsewhere effect (LEE) handling is confusing/inconsistent. You report a direct-MC LEE pLEE ≤ 10−4 (based on a 10,000-shuffle trial) and then apply an additional Bonferroni/BH penalty across ~650 directions, reducing post-LEE significance to < 1σ. If pLEE was computed with the max-statistic across directions in each realization, it already accounts for the LEE; applying an additional penalty double-counts the look-elsewhere factor.
- Required fix: Clarify the LEE procedure. If pLEE is the global p from the max-statistic MC over directions, do not re-penalize. Report either (i) local p with Bonferroni correction to get global p, or (ii) global p from max-statistic MC. Do not combine both.

P4-M3
- Location: Appendix D.a (p. 8), Appendix A.c (p. 7), text (pp. 1, 6–7)
- Problem: Ambiguous apodization description (“C 2 2◦ apodization”) and inconsistent mask references. It is unclear whether this denotes cosine-squared apodization of width 2 degrees. Also, “apodized-mask test +3.57σ on C 2 2° apodization” occurs for the canonical mask, while Appendix A mentions an apodization on the subsample mask. The interplay between masks and apodizations is hard to follow.
- Required fix: Define the apodization explicitly (function and angular scale) and consistently identify which mask each result refers to (canonical vs subsample), in one location (e.g., a short table). Ensure consistent terminology across the manuscript.

P4-M4
- Location: Table I (p. 4), Abstract (p. 1), Appendix A.c (p. 7)
- Problem: Ambiguous use of “n = 5,547,858” for the subsample mask. In Table I Nmap weighted is defined as Σp Wp with Wp = Nall(p). In the Abstract and elsewhere, “n = 5,547,858” is presented without specifying it is a weighted-sum (not a galaxy count). This invites confusion because Ncatalog spiral = 3,201,160 is the galaxy count.
- Required fix: Everywhere the value 5,547,858 appears, denote it explicitly as Nmap,weighted (sum of weights) rather than “n”. Add a footnote in the abstract or early in the text to prevent misinterpretation.

P4-M5
- Location: Table II (p. 4)
- Problem: Deviations (σ) not consistent with displayed numbers. For Catalog A: (0.5079−0.5)/0.000279 ≈ 28.3, not 28.8. For Catalog B: (0.504−0.5)/0.000279 ≈ 14.3, not 14.6. For Catalog C: (0.4974−0.5)/0.000279 ≈ −9.3 (magnitude 9.3), not 9.5. These are small but systematic mismatches.
- Required fix: Recompute “Dev. (σ)” entries directly from the tabled values or report the exact σ used for each entry to make the mapping reproducible. Correct the table.

P4-M6
- Location: Sec. IV.C (p. 4), Table III (p. 5)
- Problem: “Catalog A (raw) shows a 2.31σ real-space dipole and a +6.48σ pre-MASTER pseudo-Cℓ in the lowest bandpower.” These figures are not shown in a table/figure and differ from the 6.097σ in Table III for ℓeff = 4. It is unclear what nulls and band definitions were used for +6.48σ versus +6.097σ.
- Required fix: Add a table or figure reporting the raw Catalog A real-space dipole and pseudo-Cℓ statistics with explicit null definitions (number of MCs, binning), or reconcile with Table III values. Ensure consistency of all reported σ for Catalog A across the paper.

P4-M7
- Location: Appendix A.a (p. 7)
- Problem: Assertion “The depth weighting does not introduce a monopole–dipole coupling because the galaxy-weighted mask-mean is subtracted” is stated without derivation. In general, weighting schemes can bias low-ℓ normalization and covariance under incomplete sky coverage.
- Required fix: Provide a short derivation or a reference demonstrating that your weighting plus monopole subtraction yields an unbiased estimator for C1 under the stated null and mask, or include a simulation test comparing weighted vs unweighted estimators under the same mask.

MINOR

P4-n1
- Location: Sec. IV.B (p. 4)
- Problem: “spatially uniform across 7 equatorial coordinate slabs” is asserted but only described qualitatively.
- Required fix: Provide the per-slab numbers (in a small table in the supplement/repo) and reference them explicitly in the text.

P4-n2
- Location: Table III (p. 5)
- Problem: Several bandpowers show negative Cℓ but positive “Significance (σ)”, yet the null mean is not reported for those bins, making interpretation opaque.
- Required fix: Add the null means for each bandpower (or in a supplementary table) to make the sign of Δ and reported σ interpretable.

P4-n3
- Location: Appendix D.c–d (p. 8)
- Problem: Cross-spectrum notation and “σ = −2.89” are nonstandard (mixing sign with “σ”). It’s unclear whether σ denotes signed z or magnitude with separate sign.
- Required fix: Define the test statistic for cross-spectra (r or normalized cross-power), and report p-values with a sign for the correlation/anti-correlation separately (e.g., r = −0.65, p = 0.0036), avoiding “negative σ”.

P4-n4
- Location: Appendix B.d (p. 8)
- Problem: Bias-test thresholds are ad hoc and not tied to the sub-percent cosmology goals; “T6: Hemispheric null < 10%” is an odd absolute threshold.
- Required fix: Briefly justify how these thresholds relate to the target sensitivity (≥ 0.75% amplitude at 3σ) or move the bias-test thresholds to the supplement with a rationale.

P4-n5
- Location: Appendix D.f–g (p. 8)
- Problem: Very large z-values (e.g., z = −264.5; zboot ≈ −18.1) reported without sufficient detail on the covariance model and degrees of freedom in the WLS fit.
- Required fix: Provide the covariance model used (analytic/empirical), the number of spatial blocks, and degrees of freedom. Consider replacing extreme z’s with effect sizes and p-values.

P4-n6
- Location: Appendix A.c (p. 7)
- Problem: Units “Cℓ × 10^6 (sr)” may confuse readers; for a dimensionless scalar field on the sphere, Cℓ is commonly reported dimensionless (or with sr depending on convention).
- Required fix: State your convention for units of Cℓ explicitly and ensure consistency across tables and text.

P4-n7
- Location: Data Availability (p. 9)
- Problem: Release tag “v2026.04” and URLs may be time-sensitive; reproducibility depends on exact versions.
- Required fix: Add explicit commit hashes for the code and a permanent archive (Zenodo DOI) snapshot of code/models/data used to produce the paper’s results.

NIT

P4-N1
- Location: Appendix D.a and throughout
- Problem: “C 2 2◦ apodization” typography is unclear.
- Required fix: Replace with “cosine-squared apodization with 2° scale” (or your exact functional form).

P4-N2
- Location: Sec. VII.d (p. 7)
- Problem: Falsification criterion in abstract states amplitude ≳ 0.75% at σ > 5 without specifying sample size; the Conclusions add “≥ 10^7 galaxies”.
- Required fix: Harmonize the statements; specify the survey size assumptions consistently.

P4-N3
- Location: Minor rounding throughout
- Problem: Several σ and percentage values are rounded inconsistently.
- Required fix: Apply consistent rounding rules across tables and text.

P4-N4
- Location: References (pp. 10–11)
- Problem: Some references have minor inconsistencies in punctuation/journal styling.
- Required fix: Conform to PRD reference style.

Additional length comment
At 11 pages including appendices, the length is acceptable for the presented material, provided the essential/major issues above are resolved and the results are made fully consistent and reproducible. No page reduction is necessary if the revisions tighten the methodology descriptions and unify definitions.

## Summary recommendation
MAJOR REVISIONS

The paper presents a large and potentially valuable analysis, but there are essential methodological inconsistencies (most critically, the definition of the chirality field used in the MASTER pipeline) and significant issues in significance reporting (use of “σ” versus empirical p), as well as arithmetic and clarity problems, that must be corrected. Once the field definition is unified, the significance metrics are reported consistently with their nulls, the sensitivity-floor derivation is made coherent, and the data/code links are fixed, the paper could be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS

ESSENTIAL

P4-E8
- Location: Appendix A.c (p. 7); related narrative in Sec. IV.C–D
- Problem: Contradictory effect of monopole subtraction on “significance.” Appendix A.c states that monopole subtraction reduces the decoupled C1 at ℓ=1 from 2.30×10−5 to 1.51×10−5 (~34% drop) yet “increases σ from +1.85 to +3.64 (the canonical-mask number).” This runs counter to the stated leakage narrative (that subtracting the monopole should reduce spurious low-ℓ power). An increase in z while the central value drops can only occur if σnull also drops substantially; no such change in the null is shown, and the mask/field used for each number is not explicit.
- Required fix: Show, side-by-side, the measured C1, the null mean and σnull, and the resulting p/z both before and after monopole subtraction, clearly identifying the mask and chirality-field definition in each case. Explain why z increases if this is intended (e.g., due to a change in σnull). If this is a stale/mixed-number artifact, correct it.

P4-E9
- Location: Sec. IV.D (pp. 4–5), Abstract (p. 1), Appendix A.a/c (p. 7)
- Problem: Inconsistent statements about whether the canonical-mask post-MASTER residual (+3.64σ) is computed with or without monopole subtraction. Sec. IV.D frames the canonical-mask channel as demonstrating leakage “WITHOUT monopole subtraction” to expose coupling; elsewhere (Abstract; Appendix A.a/c) the same +3.64σ number is said to be “under proper galaxy-weighted monopole subtraction.”
- Required fix: Unambiguously state for the canonical-mask post-MASTER residual which field was used (monopole-subtracted or not). If multiple variants exist, report both, with distinct values; do not attribute the same +3.64σ to both. Update text and tables accordingly.

P4-E10
- Location: Appendix E.b (p. 9) vs Sec. IV.C.a (p. 4)
- Problem: “Catalog C-full +4.31σ monopole-preserving dipole” contradicts the main-text “0.43σ real-space dipole” for Catalog C. The term “monopole-preserving dipole” is undefined, and a 10× discrepancy in |z| is unexplained.
- Required fix: Define the “monopole-preserving dipole” statistic precisely (mask, weighting, whether signed or amplitude-only, whether any per-region renormalization was applied) and reconcile the 4.31σ vs 0.43σ values. If 4.31σ is stale or refers to a different tier/field, correct or move to supplement with clear labeling.

MAJOR

P4-M8
- Location: Table III (p. 5)
- Problem: Inconsistent sign convention for “Significance (σ)”. Some bandpowers have negative Cℓ but positive “Significance (σ)”, while ℓ=1 shows a signed negative value (−0.122σ). It is unclear whether “σ” denotes a signed z-score or |z|.
- Required fix: Standardize the convention: either report signed z = (Cmeas−⟨Cnull⟩)/σnull for all rows (and include null means for each bin), or report |z| consistently and indicate the sign of Δ separately. Update the table caption to specify the convention.

P4-M9
- Location: Table I (p. 4), Table IV (p. 5)
- Problem: Mixing “σ” used for detection significance with “σ/z” used for a generative-null reproduction residual risks confusion. In Table I, estimator (v) “monopole+mask null” is listed as “+1.68” under “σ”, but this z comes from the difference between data and the monopole-only generative null (Table IV), not from a detection test under an isotropic/permutation null.
- Required fix: Separate reproduction-quality metrics from detection significances. Consider a distinct column (e.g., “reproduction z”) for the generative-null residual, and reserve “σ” for detection under the stated cosmological null. Clarify in the caption.

P4-M10
- Location: Throughout Sec. IV.D; Table I (p. 4); Appendix A.c (p. 7)
- Problem: Ambiguous/overloaded null nomenclature (“pp-shuffle”, “per-pixel random-label permutation”, “binomial per-pixel-shuffle,” “monopole-only generative null”). It is not always clear which null was used for which estimator (especially for the canonical-mask post-MASTER residual and the 99.3% pre-MASTER reproduction).
- Required fix: Provide a compact mapping table listing, for every reported σ/p (per estimator and per table/appendix reference), the exact null type (permutation vs binomial generative), the conditioning (e.g., within-density-strata or not), NMC, and mask used. Use one term consistently (define “pp-shuffle” explicitly once and reuse).

P4-M11
- Location: Appendix A.c (p. 7); Sec. IV.C–D
- Problem: Numbers quoted for C1 and σ (e.g., 2.30×10−5, 1.51×10−5, −0.122σ; +3.64σ) are given without consistently tagging which mask and which field definition (spiral-only denominator vs all-galaxy denominator; with/without monopole subtraction). This hampers reproducibility and invites misinterpretation when values are juxtaposed.
- Required fix: Every C1/σ value must be tagged in-text or in a consolidated table with: mask, field definition (denominator), monopole subtraction status, weighting, binning, and null. Where values are compared across configurations, state explicitly what changed.

P4-M12
- Location: Appendix D.c (p. 8)
- Problem: Claim “The summed leg-induced ℓ=1 amplitude is ∼25% of the observed canonical-mask ℓ=1 amplitude” lacks a derivation. Cross-correlation coefficients rℓ do not directly translate to fractional contributions to auto-power without a defined template-regression framework.
- Required fix: Provide a quantitative derivation (e.g., from a joint template regression or power-spectrum decomposition) showing how the quoted rℓ map to a 25% contribution, including units/conventions. Otherwise, soften to a qualitative statement.

MINOR

P4-n8
- Location: Sec. IV.D/Table IV (p. 5) vs Appendix C.c (p. 8)
- Problem: Hemisphere scan discretization mismatch. Table IV cites “NSIDEdir = 8” for the max-hemisphere statistic, while Appendix C.c describes scanning “all hemisphere-pairs at 10° increments.” The global p-value is sensitive to the search grid.
- Required fix: Use a single hemisphere-scan protocol (either HEALPix-based NSIDEdir or fixed-angle grid), state it once, and recompute/report pLEE consistently. If both were run, report both and clarify which underpins each quoted pLEE.

P4-n9
- Location: Abstract (p. 1), Sec. VI.B (p. 6)
- Problem: Unexplained “factor ∼ 6–12” inconsistency with Shamir’s ∼3% amplitude claims. The basis for this factor is not shown (amplitude ratio? significance ratio? accounting for dilution g?).
- Required fix: Provide the explicit calculation (including any dilution factors and null mapping) for the 6–12 factor or remove the claim.

P4-n10
- Location: Appendix B.a (p. 7), Sec. IV.B (p. 4)
- Problem: The link between the training confusion-matrix asymmetry (CW recall 93.8% vs CCW 92.6%, 1.2 pp) and the observed raw CW monopole excess (0.79%) is asserted but not quantified.
- Required fix: Provide a simple calculation showing the expected monopole offset from the measured recall asymmetry given class prevalences, or rephrase as a hypothesis.

P4-n11
- Location: Sec. III.C (p. 3)
- Problem: “Flip-swap correlation = 1.000” is reported without methodological details (sample size, exact metric, numerical precision). Since this appears exactly unity, readers may infer it is enforced rather than measured.
- Required fix: Specify whether this equality is by construction (due to TTA protocol/symmetry loss) or an empirical correlation, and state N and numerical precision if empirical.

P4-n12
- Location: Appendix D.f (p. 8); general throughout
- Problem: Mixed “A” vs “fCW” reporting without a central definition can confuse readers (e.g., “Abest_dipole = 4.55×10−3 (0.23% in fCW units)” relies on A = 2fCW − 1).
- Required fix: Define A = 2fCW − 1 once in the main text and, where both units are shown, provide both values consistently or pick one convention.

P4-n13
- Location: Sec. IV.D/Table IV (p. 5) text
- Problem: Notation “pseudo-C(ℓ=1)ℓ” is non-standard and confusing.
- Required fix: Replace with “pseudo-Cℓ at ℓ=1” consistently.

NIT

P4-N5
- Location: Sec. II.A (p. 2)
- Problem: Typo “unique dr8 id identifiers.”
- Required fix: Use “unique DR8 identifiers” (or “unique dr8_id values”).

P4-N6
- Location: Throughout
- Problem: Inconsistent typography/spacing in symbols and units (e.g., stray spaces in “C 2 2◦”, inconsistent degree-symbol spacing, times symbol formatting like “3.2×106”).
- Required fix: Normalize typesetting for units/symbols and scientific notation.

Explanation
These are issues not covered in the initial review. They focus on newly identified arithmetic/sign-convention inconsistencies, contradictory descriptions of monopole subtraction effects and hemisphere-scan methods, unclear null nomenclature, and several clarity/reproducibility gaps that bear directly on interpretability.