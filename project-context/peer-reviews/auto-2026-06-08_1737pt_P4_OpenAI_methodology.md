# P4 auto-2026-06-08_1737pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (12325 chars)
**Wall time**: 564.0s

---

Referee report on “Survey-Scale Galaxy Chirality with Equivariant TTA: A −0.122σ Subsample-Mask ℓ=1 Null, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)”

Scope of review
- Focus: methodological/statistical rigor, derivation chains, arithmetic/internal consistency, null-definition consistency, dimensional analysis, and whether headline claims are supported.
- I read the full 12-page manuscript, all tables/figures, appendices, and footnotes.
- I recomputed every quoted fraction, σ, p-value, ratio, and cross-checked consistency across sections and with displayed counts.

Overall assessment
The paper aims to present a large chirality catalog and a careful dipole-isotropy test with bias hardening. The qualitative structure is thoughtful. However, there are multiple essential inconsistencies in numerical calculations, null definitions, figure captions vs. methods (D4 vs Z2 TTA), conflicting definitions of the field A_p, incorrect/undocumented units for Cℓ, and a problematic Table III with arithmetic that does not match the reported σ values. Several load-bearing numbers (e.g., Table IV z-score, Fisher floor, “N_all/N_spiral ≈ 1.49”) are inconsistent with the rest of the manuscript. There is also residual version-history language embedded in the main text. These issues preclude publication in PRD in the current form.

Detailed findings

ESSENTIAL

P4-E1
- Location: Fig. 1 caption (page 5) and Methods §III C (pages 3–4)
- Problem: Fig. 1 caption asserts “Test-time D4 equivariant averaging (TTA)... evaluated on the eight D4 transforms... This averaging is the key methodology distinction between Catalog A (raw), Catalog B (Platt-calibrated), and Catalog C (equivariant).” However, §III C explicitly states only 2-fold flip TTA (Z2) is used in production (“We restrict to 2-fold TTA... A direct D4-TTA hold-out... validation”). The figure caption incorrectly implies D4-TTA was used to generate Catalog C and underpins the reported monopole shifts. This is a core methodological mismatch.
- Required fix: Replace Fig. 1 and its caption to reflect the actual Z2 (flip-only) TTA used operationally, or change §III C and all results to match D4-TTA if that was truly used. All numerical results that referenced the figure’s “+2.05% to −0.53%” shifts must be recomputed/relabeled using the exact TTA protocol actually applied to Catalog C.

P4-E2
- Location: Table III (page 6)
- Problem: Arithmetic inconsistency between Cℓ, σ_null, and “Significance (σ)” entries. Example: for ℓ_eff=4, Cℓ=3.210×10^6(sr), σ_null=0.804×10^6(sr), so |z| should be ~3.99, but the table lists +6.097. For ℓ_eff=9, Cℓ is negative (−0.248×10^6) but the table lists a positive significance +2.232, which is not consistent with z=C/σ≈−0.432. Multiple rows do not reconcile. The first row header is also mislabeled “canonical single-mode ℓ=1...” while the note says “subsample mask, f_sky=0.659.”
- Required fix: Recompute and correct all entries in Table III, including whether the “Significance (σ)” column reports signed z-scores or |z|; state the null explicitly (mean and std), and ensure the mask specification in the caption matches the row. If bandpowers use a non-zero null mean, show it. Provide a machine-readable supplementary table for audit.

P4-E3
- Location: Appendix A (page 9), lines defining the field; main text §IV C (page 4), footnote 1 (page 4–5)
- Problem: Inconsistent definition of A_p. The main text defines A_p=(N_CW−N_CCW)/(N_CW+N_CCW) (spirals-only denominator). Appendix A contradicts this: “Field: ... A_p = (N_CW − N_CCW)/N(p)_total.” That changes the field, the weighting, and the normalization, and directly affects Cℓ. Footnote 1 and §A(a) also mix N_all and N_spiral in ways that will change the data vector.
- Required fix: Use a single, explicit definition of A_p throughout (spirals-only denominator vs all-galaxy denominator), and propagate it consistently in all analyses, including NaMaster inputs, nulls, and generative tests. Recompute all relevant Cℓ, σ, and p-values accordingly.

P4-E4
- Location: Table III (page 6) and Fig. 4 caption (page 8)
- Problem: Reported units for Cℓ as “×10^6 (sr)”. For a dimensionless scalar field A_p, standard pseudo-Cℓ normalization renders Cℓ dimensionless in typical cosmology conventions (unless a specific convention is stated that multiplies by steradians). Units are undocumented and appear incorrect/misleading.
- Required fix: State the exact NaMaster normalization convention and whether Cℓ is dimensionless. Remove “(sr)” if incorrect, or justify with the precise convention. Align figure axis labels and table units accordingly.

P4-E5
- Location: Fig. 1 caption (page 5), §IV B/Table II (pages 3–4), Appendix A(a) last line (page 9)
- Problem: Inconsistent use of “percentage” when discussing the global monopole. Table II “Excess (%)” for Catalog C is −0.26% (i.e., f_CW−0.5), but Fig. 1 and Appendix A(a) refer to −0.53% (this corresponds to A = (N_CW−N_CCW)/N_spiral). In Fig. 1 caption, raw “+2.05%” disagrees with Table II raw “+0.79%” and with A=2(f−0.5) which would be +1.58% for f=0.5079.
- Required fix: Adopt one convention (either report the monopole as f_CW−0.5 or as A), define it clearly, and update every quoted percentage consistently across text, figures, and appendices. Correct the raw and equivariant percentage values to match the actual counts.

P4-E6
- Location: Table IV (page 6)
- Problem: z-score miscomputed for the pre-MASTER pseudo-Cℓ(ℓ=1): Data=1.696×10^−2, Null=(1.685±0.007)×10^−2. Δ=1.1×10^−4, σ=7×10^−5, z=1.57, not 1.68 as printed.
- Required fix: Correct the z-score (and any downstream text relying on 1.68σ). If there is rounding of σ_null or a different estimator of dispersion, document it and ensure internal consistency.

P4-E7
- Location: Footnote on page 4–5 (Sec. IV D, footnote 1)
- Problem: Version-history/meta language appears in the body: “The previous wording ‘Binomial(n_total, p_global_CW)’ was ambiguous...” PRD does not permit internal drafting history in the published text.
- Required fix: Remove all version-history/editorial-process language. Replace with a neutral, self-contained, final description of the generative null.

MAJOR

P4-M1
- Location: Abstract (page 1), §IV C (page 4), Table I (page 4)
- Problem: Precision and MC counts. The headline significance −0.122σ (500-MC null) is quoted to three decimals, which is not supported by the sampling uncertainty on σ_null with N_MC=500 (relative uncertainty on SD ≈ sqrt(1/(2(N−1))) ≈ 3.2%). Reporting −0.12±0.004 σ would be misleadingly precise.
- Required fix: Reduce significant figures for σ-values estimated from 500 MCs (e.g., −0.12σ). Quote uncertainties on σ or provide a bootstrap on σ_null, or increase N_MC so that the quoted precision is justified.

P4-M2
- Location: §VI A (page 7)
- Problem: Fisher/Poisson floor derivation. You state “σ(A/2) ≈ 0.048% at N_spiral=3,201,160, f_sky=0.46,” leading to a 3σ full-amplitude floor of ~0.29%. Using binomial variance, σ(f)=sqrt(p(1−p)/N)=0.0279% with no f_sky penalty; if you degrade by f_sky, σ scales as 1/sqrt(f_sky), giving ≈0.041% not 0.048%. The manuscript does not explain the extra inflation to 0.048% nor justify f_sky=0.46 (vs 0.490 or 0.659 elsewhere).
- Required fix: Provide a transparent derivation of the Fisher floor, including whether f_sky enters and why, the exact f_sky used, and reconcile with other stated f_sky values. Correct the numerical value if miscomputed.

P4-M3
- Location: §IV D, footnote 1 (page 4–5)
- Problem: “The per-pixel trial-count inflation factor ⟨N_all/N_spiral⟩ ≈ 1.49...” This contradicts the catalog-wide fractions (N_all/N_spiral ≈ 8.4745M/3.2012M ≈ 2.65). Even within the canonical mask, this factor seems implausible without explicit demonstration.
- Required fix: Compute and report the actual ⟨N_all/N_spiral⟩ within the exact canonical mask used in the generative null, using the same pixel selection and thresholds. Correct the number (likely ~2.6) or justify with measured masked values; provide a supplementary table or code pointer.

P4-M4
- Location: Appendix A (page 9), end of section (a)
- Problem: “Monopole subtraction reduces decoupled C1 from 2.30×10^−5 to 1.51×10^−5 (~34%) and increases σ from +1.85 to +3.64.” It is unclear how reducing C1 increases |z| by a factor ~2 absent a change in σ_null. This suggests either different nulls or a reporting error.
- Required fix: Clarify the exact null, mask, and σ_null used before/after monopole subtraction for these two numbers, and correct the σ if erroneous. If different nulls/masks were used, state them explicitly, and do not put the two σ values side-by-side without that context.

P4-M5
- Location: Table I caption/entries (page 4); Table III caption first row (page 6)
- Problem: Mask nomenclature confusion. The first row of Table III calls the result “canonical single-mode ℓ=1 post-MASTER result anchoring the dipole-isotropy null (subsample mask, f_sky=0.659).” “Canonical” here conflicts with “subsample mask.” Table I mixes “subsample” and “canonical” without unambiguous, consistent naming.
- Required fix: Standardize mask names (e.g., “canonical mask” for f_sky≈0.49; “subsample mask” for f_sky≈0.659) and use them consistently across all tables/figures/text. Fix the Table III row label.

P4-M6
- Location: §IV D (pages 4–5), Table IV (page 6), Appendix C (page 10)
- Problem: Hemisphere test significance inconsistencies stemming from different nulls. The main text cites “local maximum 3.05σ” (Appendix C), while Table IV lists “+4.42σ” for “Hemisphere max|A| (NSIDE_dir=8).” These should not be juxtaposed without explicit, immediate reminders that they come from different nulls (direct look-elsewhere MC vs. monopole+mask generative null).
- Required fix: In every instance where these σ values are given side-by-side or in nearby sections/tables, explicitly state the null used and that they are not directly comparable. Prefer reporting the same statistic under the same null, or avoid placing them adjacent.

P4-M7
- Location: Abstract (page 1), §VI A (page 7), Appendix E(b) (page 11)
- Problem: The falsification criterion “amplitude ≳0.75%” is derived from injection-recovery on the HC subsample (N=471,049), not the full catalog used in the main estimators. Extrapolating this threshold as a falsification bar for the whole analysis is not justified without scaling arguments or a full-sample injection test.
- Required fix: Either (a) perform an injection–recovery on the full analysis sample (or a representative subset matched in purity/pixelization) to substantiate the 0.75% threshold; or (b) qualify the falsification statement explicitly as applying to the HC subsample and give the expected scaling to the full sample.

P4-M8
- Location: Abstract (page 1), §IV D (page 5), §VII (page 8)
- Problem: Use of “n = 5,547,858” for the subsample mask risks confusion because elsewhere this “n” is the sum of pixel weights W_p = N_all(p), not a count of independent spiral galaxies. Presenting it as a simple sample size can mislead readers about statistical power.
- Required fix: Replace “n = 5,547,858” with an unambiguous label such as “N_map,weighted = 5,547,858 (sum of W_p = N_all per pixel)” wherever it appears, and avoid using “n” as shorthand for this weighted quantity.

P4-M9
- Location: §V B (page 7)
- Problem: “CE-ResNet [7] achieves cw/ccw = 0.998...” This phrasing (“cw/ccw = 0.998”) is ambiguous (is it a ratio or a fraction?). If it refers to balance, please define it, and provide the exact definition used in [7]. As written, readers cannot compare directly.
- Required fix: Define the CE-ResNet metric precisely (e.g., f_CW/(f_CW+f_CCW) = 0.499, deviation 0.2% from 50/50), or cite the exact statistic from [7] with consistent notation.

MINOR

P4-m1
- Location: Table II (page 4)
- Problem: Deviations in σ: for Tier A, (0.5079−0.5)/0.000279 ≈ 28.3σ (not 28.8). For Tier B, ≈14.34σ (not 14.6). For Tier C, ≈9.48σ (they list 9.5). Minor rounding inconsistencies, but please check calculation and report to ≤2 significant figures in σ when using 3–4 sig figs in inputs.
- Required fix: Recompute and round consistently.

P4-m2
- Location: §IV A (page 3) and Fig. 2 (page 6)
- Problem: The reported class counts NCW=1,592,107 and NCCW=1,609,053 imply f_CW=0.497353 and A=−0.5294%, which should be used consistently (ties back to P4-E5).
- Required fix: Ensure all references to the monopole use either f_CW−0.5=−0.2647% or A=−0.5294%, with the convention clearly stated.

P4-m3
- Location: Appendix A(b) (page 9)
- Problem: “single-multipole linear bin ... ℓ=1 row...” Please clarify if the binning scheme includes ℓ=0 or not, and confirm that ℓ=0 is excluded from the mode-coupling matrix (you state ℓ=0 is removed earlier; repeat here for clarity).
- Required fix: Add one sentence explicitly confirming ℓ=0 is excluded in both input and coupling.

P4-m4
- Location: §IV C(a) (page 4)
- Problem: “NSIDE=64 ... ~0.84 deg^2 per pixel” is correct; add the exact formula A_pix = 4π/(12 NSIDE^2) for completeness.
- Required fix: Add a parenthetical with the formula.

P4-m5
- Location: Appendix D(a) and A(c) (pages 10, 9)
- Problem: Notation “C 2 2° apodization” is unclear. Presumably cosine-squared with 2° scale.
- Required fix: Replace with “cosine-squared apodization of 2°” or standard NaMaster nomenclature.

P4-m6
- Location: §V A (page 6)
- Problem: “maximum regional asymmetry is 0.32%” lacks a precise definition (is this max |A| in a region? what region size?).
- Required fix: Define precisely what “regional asymmetry” means (HEALPix pixel scale, hemisphere, or custom regions) and the null/uncertainty basis.

NIT

P4-N1
- Location: Throughout
- Problem: Mixed typography (“cw/ccw”, “CW/CCW”), inconsistent capitalization and spacing.
- Required fix: Standardize to “CW/CCW” everywhere.

P4-N2
- Location: §B. Classifier Architecture Details (Appendix B; page 9)
- Problem: The informal tone in some places (“sign-flip of the argmax-CW-fraction shift... confirms sample-noise...”) is not ideal for PRD style.
- Required fix: Rephrase more formally and supply numeric uncertainties for those shifts.

P4-N3
- Location: Data Availability (page 11)
- Problem: Minor typos in URLs (broken across lines) may cause copy errors.
- Required fix: Provide DOIs or a single consolidated link in the arXiv/PRD ancillary files.

Bibliography checks
- Citations appear properly formatted and plausible. I did not cross-validate every arXiv ID, but spot checks are consistent. Please ensure [7]’s statistic is defined consistently as per P4-M9.

Length
- The manuscript is methods-heavy and 12 pages is acceptable for PRD if the above issues are corrected. No length reduction requested.

## Summary recommendation
MAJOR REVISIONS

Justification: The manuscript has multiple essential inconsistencies that directly affect the headline estimators and their interpretation: (i) a core mismatch between the TTA method described in the figure (D4) and the method used (Z2), (ii) an inconsistent definition of the chirality field denominator across sections/appendices, (iii) incorrect or undocumented Cℓ units, and (iv) arithmetic errors and sign inconsistencies in Table III and Table IV. Additional major issues include unclear Fisher-floor computation, an implausible N_all/N_spiral factor, and mixing of different null procedures without explicit reminders at each juxtaposition. These must be corrected and the affected results recomputed before the paper can be considered for PRD. The qualitative conclusions may well hold after correction, but PRD requires numerical and methodological consistency at a higher standard.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh pass)

ESSENTIAL

P4-E8
- Location: §IV A (p.3) vs §E Signal-Hunt Diagnostics (p.6) and Appendix C(a) (p.10)
- Problem: Contradictory confidence distribution. Main text states “Mean classification confidence is 0.951, median 0.9997,” implying >50% of objects have max-class probability ≳0.9997. Yet Sec. E and App. C(a) report a “1.87M-galaxy [0.5, 0.6) confidence bin.” It is impossible to have ~22% of the 8.47M sample between 0.5–0.6 if the median is 0.9997.
- Required fix: Recompute and report the actual distribution of the equivariant max-class probability used for stratification. If the stated median refers to a different score (e.g., pre-calibration, per-class rather than max-class, or a different catalog tier), name it precisely and reconcile with the 1.87M-in-bin claim. Correct all downstream stratified statistics accordingly.

P4-E9
- Location: Abstract (p.1), §IV D (p.4–5), Table III (p.6), App. D(a,f) (p.10)
- Problem: Inconsistent significance conventions. The canonical-mask post-MASTER residual is quoted as +3.64σ, but the same test lists an empirical rank pMC=0.030, which corresponds to ~1.9σ (one-sided) or ~2.2σ (two-sided), not 3.6σ. The manuscript mixes “z = Δ/σnull” and rank-based p without a clear, consistent tail convention and then translates p to “σ” inconsistently (sometimes one-sided, sometimes two-sided).
- Required fix: State unambiguously for each result whether “σ” is one- or two-sided; do not mix z-from-moments and rank p in the same sentence without translating one into the other with the stated convention. Reconcile the 3.64σ versus pMC=0.030 inconsistency or present both with a clear explanation for their discrepancy.

P4-E10
- Location: Appendix C(c) (p.10), Table IV (p.6), §VI (p.7)
- Problem: Double application of look-elsewhere correction. App. C describes a direct max-statistic Monte Carlo (which already accounts for look-elsewhere) yielding pLEE ≤ 10−4, yet the text then applies Bonferroni/BH “across ∼650 directions,” further reducing the significance “to <1σ.” This is methodologically incorrect: a direct max-statistic MC already includes the trials factor.
- Required fix: Report only the direct max-statistic MC p-value as the LEE-corrected result, or, if Bonferroni/BH is used instead, remove the direct max-statistic MC. Do not apply both. Update the quoted σ-equivalent consistently.

P4-E11
- Location: Fig. 1 caption (p.5), §III C (p.3–4), Appendix B(d), Table V (p.10)
- Problem: Group-theory/rotation inconsistency in bias tests. T2 in Table V uses “rotation stability (>80% agreement across 60° increments),” which is incompatible with the D4 group discussed elsewhere (D4 uses 90° rotations). This adds to the already-flagged Z2 vs D4 mismatch for production TTA by revealing an internal inconsistency in the validation protocol itself.
- Required fix: Specify exactly which rotation set was used in T2 (arbitrary in-plane rotations at 60° steps with resampling, or strict D4 90° steps). Align figure captions, methods, and Table V to the same protocol, and recompute T2 if necessary.

P4-E12
- Location: Table I (p.4)
- Problem: Column semantics inconsistency. The final column is labeled “σ” but mixes σ-values and p-values (e.g., row iv: “pLEE ≤ 10−4”). This obscures comparability and contradicts the table heading.
- Required fix: Use one column per statistic (e.g., “σ” and “p-value”), or standardize all rows to the same metric, with null definition stated per row.

P4-E13
- Location: Table III (p.6)
- Problem: “Joint χ2/dof (38 bandpowers) = 161.2/38” is reported while the displayed table shows only 6 rows (1 single-ℓ plus 5 bandpowers). The origin of “38 bandpowers” is not shown, and the computation basis (masks, nulls, binning) is undocumented at that granularity.
- Required fix: Provide the full 38-bandpower table in the supplement, state the exact binning used, and ensure the χ2 references that exact data vector and null covariance. If Table III is a truncated display, say so in the caption.

P4-E14
- Location: Abstract (p.1), §IV C–D (p.4–6), Fig. 4 caption (p.8)
- Problem: Contradictory claims about MASTER “removing” leakage. Multiple places state MASTER “removes the leakage,” yet the canonical-mask post-MASTER residual is +3.64σ and explicitly attributed to “residual mode-coupling that MASTER does not fully invert on the patchy canonical footprint.” This sends mixed messages about what MASTER is actually doing in the pipeline.
- Required fix: Rephrase consistently: MASTER reduces pre-MASTER leakage but does not fully remove it on the canonical mask; the subsample-mask estimator is used to bypass this. Reflect that nuance uniformly, including in the abstract.

P4-E15
- Location: §II B (p.2), §III (p.3), §I/§IV A (p.2–3)
- Problem: Ambiguous/incredible cross-match dataset identity. The text claims an “independent GZ1 cross-match on 234,282 disjoint matches,” but GZ1 is an SDSS-based catalog with far fewer high-confidence chirality labels (6,637 used for training here). A ~234k cross-match to DESI DR8 chirality seems implausible without a precise description of the catalog version and matching criteria. This calls into question the “69.91%” external accuracy figure and its propagation.
- Required fix: Precisely identify the validation set (GZ1 vs Galaxy Zoo DESI vs GZ DECaLS), the matching method, and the number of matched galaxies with high-confidence chirality. If the 234,282 figure is not strictly GZ1, correct the text and recompute/relabel the 69.91% figure accordingly.

MAJOR

P4-M10
- Location: Appendix D(c) (p.10)
- Problem: Dimensionally unsupported “25% leg-induced ℓ=1 amplitude” claim. The text reports rℓ=1 correlations with leg-fraction templates (+0.65, −0.73) and then states “The summed leg-induced ℓ=1 amplitude is ∼25% of the observed canonical-mask ℓ=1 amplitude.” A correlation coefficient r is dimensionless and cannot be directly interpreted as a fraction of power/amplitude without a defined normalization and regression coefficient units. No such mapping is provided.
- Required fix: Provide the explicit regression model, the leg-template normalization, the estimated coefficients, and the predicted contribution to C1 (with uncertainties). Remove the 25% claim unless backed by a quantitative projection.

P4-M11
- Location: Appendix A(a,c) (p.9), §III C/§IV C (p.3–4)
- Problem: Weighted monopole subtraction mismatch. The field is ultimately defined on spirals (Ap), but the monopole subtraction uses a galaxy-weighted mask mean with Wp=Nall(p). This mixes denominators and could move the map’s mean away from the spirals-only monopole, biasing the ℓ=1 estimate.
- Required fix: Justify this weighting analytically (show that subtracting the Nall-weighted mean of a spirals-only field is unbiased under your mask/weighting), or switch to a spirals-only weighting for monopole subtraction and recompute the MASTER results.

P4-M12
- Location: Abstract (p.1), §VII(d) (p.8)
- Problem: Unsupported sample-size clause in the falsification criterion. The “≳0.75% at ≥10^7 galaxies” requirement is not derived in the body. The 0.75% threshold comes from the HC subsample injection (N=471k), not from the full sample; the ≥10^7 figure appears ad hoc.
- Required fix: Either derive the ≥10^7 scaling (accounting for classification noise, mask geometry, and null variance) or remove it. If retained, add a full-sample injection-recovery or a principled scaling argument to justify the number.

P4-M13
- Location: §IV C(a) and Methods (p.3–4)
- Problem: Insufficient specification of the real-space dipole fit. The paper quotes “0.43σ (p=0.30, bootstrap)” but does not specify the dipole estimator (e.g., WLS fit to Ap with Nspiral weights, HEALPix pixel selection, treatment of mask and covariance).
- Required fix: Provide the explicit estimator, weight/bias treatment, pixel selection, and bootstrap protocol. Supply code or a pseudocode box so others can reproduce the 0.43σ.

P4-M14
- Location: Appendix D(f) (p.10–11)
- Problem: Implausible WLS significances (z ≈ −264.5; bootstrap-inflated |z| ≈ 18.1). These magnitudes suggest a severely underestimated covariance (e.g., ignoring spatial correlations, using per-pixel iid noise) or a units mismatch. Even after block bootstrap, |z| ≈ 18 remains unrealistically large for this data vector.
- Required fix: Rework the spatial covariance model (e.g., Gaussian-process likelihood or MASTER-derived covariance) and recompute the WLS significance. If the WLS channel is strictly diagnostic, remove σ-values and present only parameter estimates with robust uncertainties.

P4-M15
- Location: Appendix D(d) (p.10) vs Table III (p.6)
- Problem: Density-stratified null numbers inconsistent with Table III magnitudes. The density-stratified null reports ⟨C1⟩=3.44×10−6 with std 3.07×10−6 and σdata=+3.80. Table III’s decoupled single-ℓ result is C1=1.494×10−6 (subsample mask). These orders don’t reconcile unless they are different masks/fields; this is not stated.
- Required fix: State the exact field, mask, and null used for the density-stratified test and align magnitudes with Table III, or explain why they differ.

MINOR

P4-m7
- Location: Table III caption (p.6)
- Problem: “Rows 2–5 are bandpowers” but five bandpower rows are displayed (ℓeff=4,9,14,19,24). The caption count does not match the display.
- Required fix: Correct the caption to reflect the actual number of displayed bandpowers.

P4-m8
- Location: Appendix B(d), Table V (p.10)
- Problem: Ambiguous definition for T7 “confidence calibration (qualitative, <50% at confidence >0.9).” This does not map to a standard calibration metric (ECE, reliability AUC, Brier).
- Required fix: Replace with a quantitative calibration metric (e.g., ECE with binning scheme), report its value with uncertainty, and define the acceptance criterion.

P4-m9
- Location: §VI A (p.7)
- Problem: Injection–recovery probabilities lack error bars given small NMC (NMC,inj=100 per amplitude). For P(σ>3)=0.55, the binomial 1σ uncertainty is ≈±0.05.
- Required fix: Report uncertainties on recovery fractions or increase NMC to reduce Monte Carlo error.

P4-m10
- Location: Appendix D(f) (p.10)
- Problem: Units toggling between A-units and fCW-units is not explicit. “Abest_dipole = 4.55×10−3 (0.23% in fCW units)” is only interpretable if you state A=2(fCW−0.5) and which unit is used in regression.
- Required fix: State the relation and units explicitly where the numerical value is first presented; ensure consistency throughout.

P4-m11
- Location: §IV D footnote and elsewhere (p.4–5)
- Problem: References to internal code paths (“scripts/monopole_null_generative.py”) in the prose are nonstandard for PRD.
- Required fix: Move implementation details and links to the code repository into a data/software availability section and keep the main text self-contained.

P4-m12
- Location: §E. Morphology Systematics (p.11)
- Problem: “Edge-on... reduces effective sample size by ∼10–15%” is asserted without showing the fraction of edge-on disks and how this translates to sensitivity loss.
- Required fix: Provide counts (or an estimate) of b/a<0.3 systems in the sample and show the computation leading to a 10–15% Neff reduction.

NITS

P4-N4
- Location: Throughout
- Problem: Inconsistent hyphenation and capitalization (“subsample-mask” vs “subsample mask”; “NOT” in all caps).
- Required fix: Normalize terminology and avoid emphatic all-caps per PRD style.

P4-N5
- Location: §VI B, §VII and elsewhere
- Problem: Occasional rhetorical/colloquial phrasing (“the present null disfavors... by a factor of ∼6–12”, “We urge all future studies...”) without quantitative context at that spot.
- Required fix: Tighten language to PRD style and, where possible, include a brief quantitative pointer (e.g., cite the exact amplitude comparison and threshold with uncertainties).

Explanation
I focused on fresh inconsistencies not covered in the first report, with emphasis on arithmetic checks, caption–body mismatches, significance conventions, and internal logic. The most consequential new items are P4-E8 (confidence distribution inconsistency), P4-E9/P4-E10 (significance and LEE methodology), P4-E11 (rotation-group mismatch in validation), and P4-M14 (unrealistic WLS z-scores). These materially affect interpretation and reproducibility.