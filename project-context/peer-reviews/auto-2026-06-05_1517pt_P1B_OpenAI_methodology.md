# P1B auto-2026-06-05_1517pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8123 chars)
**Wall time**: 336.4s

---

Referee report for “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model”

Overall assessment
The submission aims to document three verification activities: (i) a stock-CAMB ΛCDM+ΔNeff MCMC proxy, (ii) a NaMaster pseudo-Cℓ bias-injection test for EB→β recovery, and (iii) an ALP-based cosmic-birefringence consistency check. The paper is careful in scoping what is and is not being claimed, and many caveats are explicitly stated. However, for PRD methodology standards, several key reproducibility and internal-consistency issues must be fixed. In particular, datasets and likelihood versions are inconsistent across sections; one footnoted statement about results “reported in Table I” is false; EB likelihood and estimator details are insufficient for reproducing the ALP-β MCMC; and the NaMaster bias-injection results lack uncertainties and robustness checks across apodizations/purification settings. There are also smaller but nontrivial issues (prior specifications not given in-paper; ambiguous SN Ia MB–H0 degeneracy expression; minor convergence inconsistency in Table I note; one citation contains internal bookkeeping text).

Findings

ESSENTIAL

P1B-E1
- Location: Sec. V.A (p. 6), Table II (p. 4), and multiple places in text where datasets are summarized
- Problem: Dataset/likelihood inconsistencies. Sec. V.A lists “DESI 2024 DR1 BAO + DES Y3” as one of the analyzed combinations, while Table II and adjacent discussion explicitly use “DESI DR2 BAO + DES-Y5 + Pantheon+” with Planck PR4/NPIPE CamSpec TTTEEE + low-ℓ EE/TT + lensing. Elsewhere the text uses “Planck 2018 NPIPE,” which conflates PR3 and PR4 terminology. These conflicts make the w0wa results irreproducible as written.
- Required fix: Unify and precisely specify the dataset/likelihood stacks used for each reported result. For each analysis, list: data release (DR1 vs DR2), experiment and exact product (e.g., Planck PR4/NPIPE CamSpec TTTEEE vX, low-ℓ EE/TT product name), masks, multipole cuts, and any nuisance-parameter priors used. Correct all places where PR3/PR4/NPIPE are conflated and cite the appropriate PR4/NPIPE likelihood documentation rather than the PR3 parameters paper. If multiple stacks were used in different sections, declare them clearly in the abstract or methods and maintain consistent labels throughout.

P1B-E2
- Location: Footnote 1 on p. 3; Table I (p. 3)
- Problem: The footnote states: “The third (Planck-only) dataset combination (114,992 raw samples; R̂ − 1 ∼ 0.05) is … reported separately in Table I,” but Table I contains only two columns (Full-tension and Planck+BAO+SN) and does not report the Planck-only chain.
- Required fix: Either add the Planck-only results to Table I (clearly labeled as non-converged) or remove the sentence claiming they are “reported separately in Table I.”

P1B-E3
- Location: Sec. IV (pp. 5–6)
- Problem: NaMaster MC recovery is reported as “β̂ = 0.238° (pipeline-recovery SNR = 20.32)” with a bias of 0.032°, and similarly for the 0.342° injection. No statistical uncertainties are given for β̂ (e.g., σβ across 500 realizations), and the estimator used to obtain β from pseudo-Cℓ EB is not defined. Without σβ and an explicit estimator definition, the claimed “systematic floor” of 0.032–0.040° is not quantitatively justified.
- Required fix: Report β̂ ± σβ (mean and standard deviation across the 500 realizations) for each injection (0, 0.27°, 0.342°). Provide the exact β estimator used from the pseudo-Cℓ spectra (functional form, bin weights, any covariance weighting). State whether SNR = |β̂|/σβ refers to per-realization or ensemble-mean error, and provide the standard error on the mean if the “systematic floor” is inferred from ensemble averages.

P1B-E4
- Location: Sec. VI (pp. 6–7) and Appendix C (p. 9)
- Problem: The ALP-β MCMC result (βALP = 0.336° ± 0.107° for Caγ fixed) is tied to “Planck PR4 + ACT DR6 EB-spectrum likelihoods with shared calibration covariance,” but the likelihood is not specified with enough detail to reproduce (ℓ-ranges, bandpowers, masks, calibration priors and their covariance, exact code/commit used—e.g., Eskilt & Komatsu repo version).
- Required fix: Provide the precise EB likelihood definition: data vectors used, ℓ-cuts/bins, masks/apodizations, treatment of beam/pixel windows, calibration nuisance parameters and priors, covariance (and whether off-diagonal terms are used), and the commit hash/DOI of any external likelihood code relied upon. Include a table summarizing sampled parameters and priors for the ALP-chain and βfree-chain, and report ESS and R̂ for each parameter.

P1B-E5
- Location: Sec. V.A (p. 6), Table I (p. 3) and surrounding text
- Problem: The ΛCDM+ΔNeff MCMC priors are not documented in-paper. PRD methods standards require sufficient in-paper detail (not only a repository link) to reproduce the posteriors or at least to understand prior sensitivity.
- Required fix: Add a concise table listing all sampled cosmological and nuisance parameters (including ΔNeff) and their priors for each reported ΛCDM+ΔNeff chain (Full-tension and Planck+BAO+SN). If defaults were used (e.g., CAMB/Cobaya), state them explicitly. This is necessary to interpret ΔNeff posteriors and derived quantities (H0, σ8, S8).

P1B-E6
- Location: References, item [15] (p. 10)
- Problem: Contains internal bookkeeping language: “the value used at L256/L416 of P1B.” This is an internal draft pointer and should not appear in a published PRD reference list.
- Required fix: Remove internal line-number/commentary from the citation. Ensure [15] cleanly cites the published Planck PR4/NPIPE birefringence analysis with standard bibliographic fields only.

MAJOR

P1B-M1
- Location: Table I (p. 3), footnote a
- Problem: The footnote claims “all 17 sampled parameters across both frozen combinations satisfy R̂ − 1 < 3 × 10−3,” while the table entry for Planck+BAO+SN lists “Worst R̂ − 1 = 0.003,” i.e., equal to 3 × 10−3, not strictly less. Minor but inconsistent.
- Required fix: Change to “≤ 3 × 10−3” or update the reported R̂ values to be internally consistent.

P1B-M2
- Location: Secs. III, IV, V.A (pp. 2–6), Table I (p. 3)
- Problem: Mis-citation/mislabeling of Planck products. The text uses “Planck 2018 NPIPE” and mixes PR3 references with PR4/NPIPE usage (e.g., “Planck 2018 NPIPE [17]” where [17] is PR3), and CamSpec products are not cited to the appropriate releases.
- Required fix: Replace PR3 citations with the correct PR4/NPIPE references where NPIPE-based likelihoods/maps are actually used. Provide the exact high-ℓ likelihood (CamSpec PR4) citation and low-ℓ EE/TT likelihood product references.

P1B-M3
- Location: p. 4 (“MB–H0 joint-posterior offset check”)
- Problem: The degeneracy is written as “MB − 5 log10(H0) ≈ const,” which is dimensionally inconsistent (log10 requires a dimensionless argument). The standard combination is MB − 5 log10 h (h ≡ H0/100 km s−1 Mpc−1). While the difference between two settings is numerically unaffected by the additive constant, the expression as written is not correct.
- Required fix: Replace with MB − 5 log10 h and note that while an additive offset differs by 10 mag when using H0 instead of h, the differences along the degeneracy are identical; recompute and report the same 0.155 mag offset in terms of h to keep dimensional consistency.

P1B-M4
- Location: Sec. III paragraph “Physics interpretation (Table II)” (pp. 3–4), Table II (p. 4), and Sec. V (p. 6)
- Problem: A substantial w0wa analysis (DESI DR2 + DES-Y5 + Pantheon+ + Planck PR4/NPIPE) is presented with headline significance statements (+4.3σ in w0 and −3.6σ in wa), but this analysis is not declared in the abstract as part of the three scopes, and the methods for this chain (e.g., priors, pivot redshift zp used for wpivot, full nuisance list) are insufficiently documented in the main text.
- Required fix: Either (a) move the w0wa content to a separate paper, or (b) add it formally to the scope in the abstract and provide a short methods subsection: full likelihood stack (as actually used—see E1), all sampled parameters and priors, pivot redshift zp used to define wpivot, and a brief validation (e.g., consistency checks, ESS/R̂ table).

P1B-M5
- Location: Sec. IV (pp. 5–6)
- Problem: The stated pseudo-Cℓ-derived “systematic floor” (0.032–0.040°) is based on a single apodization (C^2, 2°) and a single purification choice (purify_b=True, purify_e=False). The bias origin is attributed to mask apodization but no sensitivity test is shown.
- Required fix: Demonstrate stability of the inferred bias under at least: (i) multiple apodization scales (e.g. 0.5°, 1°, 2°, 3°), and (ii) toggling purification choices (purify_b on/off, purify_e on/off). Report the resulting shifts and confirm the quoted “systematic floor” is robust within stated uncertainties.

P1B-M6
- Location: Sec. III “Independent cross-validation” (p. 5)
- Problem: The comparison “Our MCMC agrees at 0.5σ in H0 and 0.4σ in σ8” with Liu et al. [11] is asserted without quoting the comparison values from [11]. This hampers verification.
- Required fix: Quote the H0 and σ8 central values and uncertainties from [11], show the differences and resulting σ-levels, or remove the claim.

P1B-M7
- Location: Tables I and II (pp. 3–4)
- Problem: S8 is reported but not defined in the text. While standard (S8 = σ8 √(Ωm/0.3)), PRD methods papers should define derived parameters used in tables.
- Required fix: Add a one-line definition of S8 where first used.

MINOR

P1B-m1
- Location: Sec. IV (p. 5)
- Problem: fsky = 0.32 is quoted for the apodized mask without showing derivation.
- Required fix: Report how fsky is computed (e.g., mean of apodized mask or binary sky fraction before apodization) and/or include a small figure of the mask in an appendix.

P1B-m2
- Location: Sec. IV (p. 5)
- Problem: “ΔP = 10 μK·arcmin” is described as “ACT-noise level” at Nside=512 after degrading a Planck Commander map, but the choice’s impact on β uncertainty isn’t discussed (mask-leakage bias should be noise-independent to first order).
- Required fix: Briefly comment on noise-level dependence of the β estimator bias and clarify that bias tests are dominated by mask coupling rather than noise amplitude.

P1B-m3
- Location: Eq. (3) (p. 7)
- Problem: The expression implicitly gives β in radians; the text quotes degrees without stating the conversion step.
- Required fix: Note that β computed from αEM Cαγ/(4π) × Δφ/fa is in radians and is converted to degrees in the numerical line.

P1B-m4
- Location: Sec. VI (pp. 6–7)
- Problem: ALP MCMC total accepted samples N=9,720 across 3 configs are given with R̂<0.01, but effective sample sizes are not reported.
- Required fix: Provide min ESS per configuration (or per parameter) alongside R̂ to document how well uncertainties are resolved.

P1B-m5
- Location: p. 4 (“0.2σ” agreement with Riess MB prior)
- Problem: “agrees … at 0.2σ” is based on the chain’s σMB = 0.049 mag, not the prior’s 0.027 mag; this could be misread.
- Required fix: Clarify that 0.2σ refers to the chain’s posterior σMB and add the comparison using the Riess prior σ (|ΔMB|/0.027 ≈ 0.37σ) to avoid ambiguity.

P1B-m6
- Location: Conclusions (p. 8)
- Problem: “LiteBIRD … σ(β) ≈ 0.03°; for β = 0.27°: ~9σ.” If the headline used βobs = 0.342°, the significance would be ~11.4σ.
- Required fix: Add a parenthetical noting the range of σ-levels for β between 0.27°–0.34°.

NIT

P1B-n1
- Location: Sec. IV (p. 5)
- Problem: “C2 apodization at 2° scale” is terse; commonly written as “C^2 apodization.”
- Required fix: Rephrase as “C^2 apodization with 2° scale.”

P1B-n2
- Location: Acknowledgments (p. 8)
- Problem: Mention of using AI assistance (“Claude”) may be okay, but PRD style generally does not include tool endorsements in Acknowledgments unless required by policy.
- Required fix: Optional: remove or move to an author’s note if PRD style requests.

P1B-n3
- Location: Throughout
- Problem: Some long dashes and colloquial phrases (“canonical,” “centered well into quintom-B territory”).
- Required fix: Light edit for formal tone.

Arithmetic and dimensional checks performed
- Abstract ΛCDM+ΔNeff numbers match Table I and body text.
- NaMaster bias values: 0.27° − 0.238° = 0.032°; 0.342° − 0.302° = 0.040° (correct). However, σβ is not shown (see P1B-E3).
- Inverse-variance combination (0.30±0.11) and (0.215±0.074) gives 0.2415±0.0614°, significance ~3.93σ (reported as 3.9σ; correct).
- ALP birefringence scaling: α/(4π) ≈ 5.8×10−4; β(rad) = (α Cαγ/4π) Δφ/fa. For Cαγ=8 and Δφ/fa=1.07, β ≈ 0.00497 rad = 0.285° (reported 0.29°; correct).
- Required Cαγ Δφ/fa for β=0.342°: 0.342° = 5.966×10−3 rad; divide by 5.8×10−4 gives ≈10.3 (reported 10.3; correct). Range Cαγ ≈ 10.3/[Δφ/fa] ∈ [9.36, 51.5] for Δφ/fa ∈ [1.1, 0.2] (reported ≈[9, 51]; consistent).
- Table II significances: |w0+1|/σw0 = 0.1878/0.0436 ≈ 4.31σ; |wa|/σwa = 0.6666/0.1864 ≈ 3.58σ; wpivot deviation 0.0344/0.0301 ≈ 1.14σ (matches text).
- Burn-in and sample counts: 176,240×0.7 + 132,949×0.7 ≈ 216,432 post-burn-in; consistent with footnote arithmetic.

Scope/claim juxtaposition
- The paper generally distinguishes incomparable σ’s (pipeline SNR vs published sky σ), but the w0wa analysis is not declared in the abstract and is inconsistent in dataset specification (see P1B-E1, P1B-M4).

Length
- For the stated verification scope, 10 pages are acceptable. If the w0wa analysis is retained, add a concise methods subsection without expanding the overall length beyond ~12 pages total.

Summary recommendation
MAJOR REVISIONS

Justification: The manuscript is careful about scope and contains correct arithmetic for many headline numbers. However, essential reproducibility and internal-consistency problems remain: inconsistent and partially incorrect dataset/likelihood attributions; a false statement that a Planck-only chain is “reported in Table I”; insufficient specification and uncertainty reporting for the NaMaster β recovery; and inadequate detail on the EB likelihood used in the ALP MCMC. These are fixable, but they must be addressed for PRD publication. The additional w0wa result must be either fully documented (datasets, priors, pivot, nuisance list) and folded into the declared scope or removed.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (fresh-eyes pass)

ESSENTIAL

[P1B-E7]
- Location: Sec. IV, “Foreground and noise model.”
- Problem: Incorrect Q/U rotation formula. The text states the injection “rotate Q+iU via e^{2iβ(Q + iU)} before adding noise.” This is dimensionally wrong; Q+iU should not appear in the exponent.
- Required fix: Correct to (Q + iU)' = e^{2iβ} (Q + iU) and explicitly state that β is in radians in the rotation operator.

[P1B-E8]
- Location: Appendix A vs. Sec. VI and Appendix C.
- Problem: Reproducibility/code availability mismatch. Appendix A says “No CMB polarization map analysis code is provided beyond the NaMaster driver script,” yet Sec. VI and App. C report an ALP MCMC using “Planck PR4 + ACT DR6 EB-spectrum likelihoods with shared calibration covariance.”
- Required fix: Provide the EB likelihood code (or exact external package/commit hash/DOI) and a minimal driver to reproduce the ALP-β MCMC, or explicitly state that the ALP MCMC chains are provided but the likelihood code is not public and cannot be reproduced. PRD typically requires sufficient in-paper detail or accessible code.

[P1B-E9]
- Location: Abstract footnote “a” (p. 2) and Sec. VI text relying on repo README for dataset attribution.
- Problem: Dataset specification delegated to an external README (“the repository README is the authoritative source”). For PRD methods, dataset/likelihood versioning must be unambiguously specified in-paper.
- Required fix: Move the dataset/likelihood attribution from the README into the manuscript: list exact products, ℓ-cuts, masks, calibration parameters, and the commit hash/date of any external likelihood code used (e.g., the Eskilt & Komatsu repository).

[P1B-E10]
- Location: Sec. IV, end of the NaMaster paragraph spanning pp. 5–6.
- Problem: Arithmetic inconsistency in the stated relative bias change. The bias increases from 0.032° to 0.040° between the 0.27° and 0.342° injections. The text calls this a “∼12% amplitude-dependent component,” but 0.008/0.032 = 25% (or 0.008/0.040 = 20%).
- Required fix: Recompute and report the correct relative change (20–25% depending on the chosen baseline), or define precisely how the percentage is computed.

MAJOR

[P1B-M8]
- Location: Table II, “Age [Gyr] 13.763 ± 0.019” for the w0wa chain.
- Problem: Implausibly tight age uncertainty for a w0wa extension (±0.019 Gyr ≈ 0.14%), tighter than typical ΛCDM Planck-era constraints. With w0 and wa free, the age is usually less well constrained unless additional strong priors/assumptions are applied.
- Required fix: Justify this precision (show which data/priors break degeneracies), document the age calculation (integration formula and cosmological parameter dependencies), and verify that no inadvertent constraints (e.g., fixed H0 or hidden priors) are tightening the age. If an error is found, correct the value.

[P1B-M9]
- Location: Sec. IV, “Beam and pixel window,” and “Pipeline configuration.”
- Problem: Ambiguity/inconsistency in beam treatment for the Commander CMB polarization map. The text assumes a 5-arcmin Gaussian beam at 143 GHz and applies b_ℓ^Planck w_ℓ^pix, but the Commander CMB map is a component-separated, multi-frequency product with its own effective beam. It is unclear whether the input map is beam-deconvolved or at what effective beam the product is delivered.
- Required fix: Specify the exact Commander polarization map file used, its delivered effective beam, whether beam deconvolution has already been applied, and the exact beam function passed to NaMaster. If a 5' 143 GHz beam is not appropriate for the CMB-only map, correct the analysis or justify the approximation.

[P1B-M10]
- Location: Sec. VI, paragraph beginning “MCMC parameter estimation.—Dedicated MCMC sampling…”
- Problem: βfree chain description is internally inconsistent. It states βfree = 0.344° ± 0.096° and also that this comes from “9,720 accepted samples across the 3 ALP-MCMC configurations” with Caγ fixed to {4,8,12}, which is irrelevant for a model-independent βfree fit.
- Required fix: Report the βfree chain as a separate, single configuration with its own N, ESS, R̂, priors, and likelihood details. Do not pool sample counts from the Caγ-fixed ALP configurations into βfree.

[P1B-M11]
- Location: Appendix B heading (p. 9) vs. Table III (p. 10).
- Problem: Appendix B (“Claims Classification”) appears empty; the claims classification actually appears as Table III on the next page without an explicit link back to Appendix B.
- Required fix: Move Table III into Appendix B or add an explicit cross-reference so Appendix B actually contains the promised content.

[P1B-M12]
- Location: Conclusions (p. 8), line “GetDist posteriors … as an empirical test of the quintom-B scenario [12].”
- Problem: Mis-citation. Reference [12] is a DESI DR2 BAO paper, not a quintom review. The correct background on quintom is [22].
- Required fix: Replace [12] with [22] (Quintom Cosmology review) or otherwise correct the citation.

MINOR

[P1B-m7]
- Location: Table I footnote a.
- Problem: Footnote states “references to ‘k = 7’ elsewhere in this paper…,” but no such references appear elsewhere.
- Required fix: Remove or adjust the footnote to avoid referencing content that does not exist in this manuscript.

[P1B-m8]
- Location: Throughout; Table I footnote a vs. MB usage in Sec. III/IV.
- Problem: Inconsistent notation for the SNIa absolute magnitude: “Mb” (footnote) vs. “MB” (main text).
- Required fix: Standardize to a single symbol (MB) throughout.

[P1B-m9]
- Location: Appendix A (“MCMC chains are not pre-computed…”) vs. “HuggingFace datasets” list item 3 (“ALP parameter MCMC chains”).
- Problem: Apparent contradiction about availability of MCMC chains.
- Required fix: Clarify which chains are provided (e.g., ALP chains available on HuggingFace; cosmology chains not included) and ensure the wording in Appendix A reflects this precisely.

[P1B-m10]
- Location: Sec. IV, “Beam and pixel window.”
- Problem: Notation “beam=b_Planck_ℓ w_pix_ℓ” is unclear and may be misread as a single quantity rather than separate beam and pixel windows.
- Required fix: State explicitly whether NaMaster was given separate beam and pixel windows or their product, and provide the exact beam/pixel window functions or references to their definitions.

[P1B-m11]
- Location: Conclusions (p. 8), NaMaster summary.
- Problem: “SNR consistent with the ACT-noise floor” is vague. Since SNR depends on noise level and mask, this statement is not informative without context.
- Required fix: Briefly note the σβ scaling with noise level for your estimator and that the bias test is dominated by mask-induced mode coupling (i.e., largely noise-independent), to avoid misinterpretation.

[P1B-m12]
- Location: Footnote 2 (p. 3), Λstrong expression.
- Problem: Wording confusion: “inverse Barbero–Immirzi parameter γBI” is mentioned, but Λstrong ∼ MPl/√γBI uses γBI (not its inverse) as written.
- Required fix: Clarify whether γBI or 1/γBI is meant in the scaling and ensure consistent nomenclature.

[P1B-m13]
- Location: Sec. VI, Eq. (3) context.
- Problem: Units not stated when switching from radians to degrees in the numerical evaluation line.
- Required fix: Add a note that β is computed in radians from αEM Cαγ/(4π) × Δφ/fa and then converted to degrees.

NIT

[P1B-n4]
- Location: Sec. VI, long parenthetical describing βfree and ALP configurations.
- Problem: Readability. A multi-layer parenthetical blurs distinctions between βfree and ALP runs.
- Required fix: Split into two or three sentences, clearly separating the βfree fit from the Caγ-fixed ALP configurations and their respective sample counts.

[P1B-n5]
- Location: Sec. IV, apodization description.
- Problem: Style/nomenclature. “C2 apodization at 2° scale” is nonstandard phrasing.
- Required fix: Use the standard “C^2 apodization with 2° scale.”

Explanation
These findings arose from a second-pass audit focused on arithmetic checks, dimensional consistency, internal cross-references, and appendix/main-text alignment. They are additive to, and do not duplicate, issues already raised in the initial review.