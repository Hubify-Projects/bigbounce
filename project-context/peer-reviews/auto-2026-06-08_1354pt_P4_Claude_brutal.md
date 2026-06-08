# P4 auto-2026-06-08_1354pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (11678 chars)
**Wall time**: 439.6s

---

# Referee Report — Paper P4

**Title:** "Survey-Scale Galaxy Chirality with Equivariant TTA: A −0.122σ Subsample-Mask ℓ=1 Null, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)"

**Overall verdict at top:** This is a careful, large-scale chirality null-result analysis with several real methodological contributions (TTA equivariance, MASTER deconvolution, a generative monopole-mask leakage diagnostic). But the manuscript is written in a defensive, multi-headline style with internal-revision artifacts in the body, inconsistent reporting of significance (a +3.64σ headline that is acknowledged to be ≈1.9σ on rank), undisclosed in-queue work in a footnote, and a title that reads as a self-rebuttal. PRD will not accept it in this form.

---

## ESSENTIAL findings

**P4-E1 — Version-history / revision-log language in the body of the paper.**
Sec. IV D (p. 4): *"The canonical-mask direct-MC ℓ=1 value of +3.64σ and the local hemisphere maximum of 3.05σ **were interpreted in earlier paper versions** as mask-geometric leakage…"*
A published PRD paper does not refer to its own prior drafts. Remove all "earlier paper versions" language and rewrite as a single coherent statement of the current interpretation. There should be **no** trace in the body of the manuscript's revision history.

**P4-E2 — Unperformed work declared "in queue" in a load-bearing footnote.**
Footnote 1, p. 4: *"A parallel rerun on N(p)_all-trial draws **is in queue** for the canonical-mask sensitivity-budget recompute and is expected to shift the per-pixel inflation by ⟨N_all/N_spiral⟩ ≈ 1.49 in trial count, with a sub-0.1σ effect on the headline pre-MASTER reproduction figure…"*
This is a PRD-breaking admission. Either (a) execute the rerun and report it, or (b) prove rigorously (not "expected") that the choice does not affect the 99.3% leakage-reproduction headline number, or (c) remove the claim. A footnote acknowledging the input field was ambiguously specified and the corrected run is "in queue" is unacceptable.

**P4-E3 — The "+3.64σ" headline is acknowledged to be ≈1.9σ on the rank statistic, but is still quoted as "+3.64σ" throughout.**
Abstract: *"+3.64σ (z = ∆/σ_null moment-ratio; empirical rank p_MC = 0.030, i.e. ≈1.9σ Gaussian-equivalent; 500-MC binomial per-pixel-shuffle null)"*.
A z = +3.64 derived from a moment ratio whose rank-p is 0.030 (≈1.88σ one-sided Gaussian-equivalent) implies the null distribution is heavy-tailed; in that case the moment-ratio z is **not** a meaningful significance and quoting it as the headline number is misleading. Title contains "+3.64σ"-class wording ("Diagnostic Evidence for…Canonical-Mask Residual"); abstract leads with it; Table I quotes "+3.64". The PRD-appropriate headline is the rank-based ≈1.9σ. Either remove the +3.64σ from headline positions (title, abstract numbered claim, Table I "σ" column) and replace with the rank-based number with explicit "Gaussian-equivalent" qualifier, or justify the moment-ratio quote with an explicit normality test on the null. Until then the paper's central diagnostic claim is overstated by ~1.7σ.

**P4-E4 — Title.**
The current title is four self-rebutting clauses across two lines:
"A −0.122σ Subsample-Mask ℓ=1 Null, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)".
This is a press release, not a PRD title. Recommended maximum ~12–18 words, single declarative claim. Example: *"Null galaxy chirality dipole at 0.75% sensitivity from 3.2 million DESI Legacy spirals with equivariant test-time augmentation."*

**P4-E5 — Headline mask is post-hoc and never constructed.**
Sec. III A and Sec. IV C declare the "MASTER-deconvolved single-mode pseudo-C₁ on the strict-superset subsample mask (n = 5,547,858, f_sky = 0.659)" as the **primary** cosmological estimator. Yet the paper never says how this subsample mask is constructed, why it differs from the canonical f_sky = 0.49 mask, or whether it was defined pre-registered or chosen because it gives a null. Given that the same data on the canonical mask gives +3.64σ (or +1.9σ Gaussian-equivalent) and on the subsample mask gives −0.12σ, the **choice of mask is doing the entire work of the headline**. PRD requires: (a) a quantitative definition of the subsample mask, (b) a justification of the cut that is independent of the chirality signal, and (c) evidence that this is not selection on the null. Without this, the headline "−0.122σ" is unsupported.

**P4-E6 — Training labels are dominantly CE-ResNet predictions; "independent" validation is only 69.91% accurate (κ = 0.40).**
Sec. II B + III A: 67.6% of training labels are CE-ResNet predictions; the truly independent (GZ1) check gives accuracy 69.91% with Cohen's κ = 0.40 — *moderate* agreement at best. The paper treats this as "the conservative accuracy floor" and then claims a "sub-percent sensitivity floor." With κ = 0.40 the per-galaxy chirality label is only modestly better than chance on the independent set, and the per-pixel CW/CCW difference is dominated by classifier noise rather than morphology. The paper must either (i) demonstrate that a κ = 0.40 label produces a calibrated p̂_CW field at the sub-percent monopole level (a calculation is sketched but not done rigorously), or (ii) downgrade the sub-percent sensitivity claim. As written, the sensitivity floor is not derivable from a κ = 0.40 label.

**P4-E7 — Catalog B description is internally inconsistent.**
Sec. III D: *"Catalog B (Platt-calibrated, +0.4% excess)."* Platt scaling is a monotonic logistic recalibration of probabilities; it cannot, by construction, introduce a 0.4% CW-vs-CCW class excess unless the calibration was fitted on a class-imbalanced subset. Either the +0.4% is a *residual* (not introduced by Platt), in which case rephrase, or Catalog B is not a Platt calibration. Clarify.

**P4-E8 — Table II σ-deviation column does not match the stated formula.**
Table II, p. 4 caption: *"Dev. is (f_CW − 0.5)/σ"* with σ = 0.000279.
Catalog A: (0.5079 − 0.5)/0.000279 = 28.3, table says **28.8**.
Catalog B: (0.504 − 0.5)/0.000279 = 14.34, table says **14.6**.
Catalog C: (0.4974 − 0.5)/0.000279 = −9.32 ≈ 9.5 only if you propagate to 4 decimals (0.49735 used in body). The body says 0.4974 which gives 9.32, not 9.5. Either report f_CW to a precision consistent with σ_binomial, or recompute the Dev column.

**P4-E9 — Abstract HC-cut notation is wrong.**
Abstract: *"471 049 high-confidence per-spiral after p^eq_CW > 0.9"*. A cut on p_CW > 0.9 alone would discard the entire CCW population, leaving CW-only galaxies (which would obviously bias any chirality analysis). The Appendix and Sec. VI A use "p_eq > 0.8" / "p_eq > 0.6", suggesting the actual cut is on the max equivariant class probability, not p_CW. Fix the abstract notation; this is a misleading misdescription of the selection function used in the empirical injection floor.

**P4-E10 — σ-values from non-comparable nulls are still juxtaposed throughout despite the abstract caveat.**
The abstract correctly states that σ values from different procedures are not comparable, then immediately presents −0.122σ, +0.43σ, +3.64σ side-by-side. Table I reports them in a single "σ" column. The Conclusions section juxtaposes them again. The caveat does not cancel the visual juxtaposition. Either (i) put each estimator in its own row with the null procedure inline in the σ column header, or (ii) convert all to a common reference (rank-based p-value, two-sided, with explicit FDR/LEE accounting). At minimum, never quote three different-null σ values in the same sentence without re-stating the qualifier.

---

## MAJOR findings

**P4-M1 — Falsification criterion is a sensitivity floor, not a falsification.**
Sec. I and Sec. VII: *"A future survey detecting a chirality dipole at σ > 5 with full amplitude ≳ 0.75% … would falsify the present null."* This is just a restatement of the sensitivity floor; it does not constitute a Popperian falsification of any physical model. Rephrase as "sensitivity limit" and remove the falsification framing.

**P4-M2 — "Survey-scale" novelty claim.**
Sec. I: *"survey-scale coverage of 8.47 million galaxies (3,201,160 equivariant-classified spirals, 1.6× CE-ResNet's scale)."* 1.6× is incremental, not survey-scale-defining. Walmsley et al. (GZ DESI, ref. [9]) already reach 8.7M galaxies in the same footprint. The contribution is the equivariant TTA + bias-hardening + MASTER pipeline applied at this scale, not the scale itself. Tone down "survey-scale" and "largest" claims.

**P4-M3 — Significance of the leg-stratified detection has an implicit selection.**
Appendix C: the +3.29σ in the [0.5, 0.6) confidence bin "does not survive the sample-purity ladder." Cutting on confidence after observing the signal is a post-hoc subset cut. The paper acknowledges this and applies a 15-cell joint label-shuffle max-statistic correction (→ 2.4σ family-wise), which is the right thing — but the body text first presents +4.50σ DECaLS and +4.72σ cell-level numbers without the correction. Move the family-corrected number to the headline of that paragraph; demote the +4.50σ / +4.72σ numbers to context.

**P4-M4 — Cross-spectrum statistic units.**
Appendix D, items (b)–(c): "rℓ=2 = −0.65, σ = −2.89". The "r" is referred to as a cross-power coefficient, but its definition (Pearson, normalized cross-spectrum, partial cross-coherence?) is never given. A reader cannot reproduce r = −0.65 from the displayed quantities. Define r mathematically and state the permutation-null procedure (Nperm, what is held fixed).

**P4-M5 — Two-point chirality correlation "−2.41σ at θ ≈ 0.5°" attributed to brick boundaries without quantitative test.**
Appendix C: the −2.41σ bin is dismissed as a "brick-boundary classifier artifact" with parenthetical "confirmed by vanishing to −0.03σ in the brick-interior subsample". Show the brick-interior measurement explicitly in a table or figure; this is a critical control and is currently in a parenthetical with no Nspiral or fsky.

**P4-M6 — D₄-TTA validation sample is tiny.**
Sec. III C: a 2-fold (Z₂) TTA is used at production; D₄ validation is done on two ~2000-galaxy subsamples and shows a 21.4% argmax flip rate between Z₂ and D₄ "on borderline galaxies." A 21.4% borderline-galaxy flip rate is large; the paper argues it is offset by stable mean p_CW but does not demonstrate that the borderline population has the same spatial distribution as the rest of the catalog. If borderline galaxies are concentrated near bright stars / DR8 brick edges / low-depth regions, the 21.4% flip rate becomes a depth-correlated systematic. Add a spatial null test of the borderline-galaxy subsample.

**P4-M7 — Bias-hardening Table V T7 is "qualitative PASS."**
A binary PASS/FAIL on a qualitative inspection is not a published test result. Replace with a quantitative calibration metric (e.g., expected calibration error, reliability diagram slope) or remove from the test battery.

**P4-M8 — Comparison with Shamir is qualitatively dismissive.**
Sec. V A: *"We do not claim a frequentist exclusion of Shamir's Ganalyzer estimator: a likelihood-level exclusion requires a matched-footprint Ganalyzer reanalysis … (not performed here)."* Yet Sec. I, VI, and VII repeatedly state the present null "disfavors the Shamir ∼2–4% detection class … by a factor of ∼6–12." Without a matched-footprint reanalysis, the factor 6–12 is a comparison of incompatible pipelines and cannot be quoted as a frequentist disfavoring. Either run the Ganalyzer comparison or drop the factor.

**P4-M9 — Edge-on contamination (65.7%) treatment relies on an unproven symmetry argument.**
Appendix E.a: the paper argues that equivariant averaging makes CW/CCW probabilities flip-symmetric for edge-on disks "whose mirror image is morphologically indistinguishable from the original." This is exactly true only if the classifier itself satisfies the equivariance pre-TTA. Sec. III B + III C show that 2-fold TTA enforces output equivariance — i.e., the symmetry is enforced by the protocol, not by the data. For edge-on disks the protocol yields a 50/50 split by construction, which adds Gaussian-distributed CW−CCW noise to each pixel. This dilution is acknowledged ("∼5–8% sensitivity penalty") but the actual variance contribution to the dipole estimator from this protocol-enforced 50/50 split is not propagated.

**P4-M10 — Section IV D footnote conflates two trial pools.**
Already flagged as E2. Additionally, the body text at the start of Sec. IV D states the realizations are drawn from "Binomial(N_spiral(p), p^global_CW)" but the previous published version (acknowledged in the footnote) used "Binomial(n_total, ...)." The fact that the paper retains the old phrasing as a correction footnote rather than just stating the current procedure cleanly is symptomatic of the revision-history-in-body problem.

**P4-M11 — Table III "Significance (σ)" column for bandpowers is unexplained.**
Table III, p. 5: ℓeff = 4 has Cℓ = 3.210, σ_null = 0.804, Significance = +6.097. From the displayed numbers, 3.210/0.804 = 3.99σ; +6.097σ requires a non-zero null mean ⟨Cℓ⟩null ≈ −1.69×10⁻⁶ that is not displayed in the table. Add a "⟨Cℓ⟩null" column or restate the significance formula in the caption. The same issue applies to rows 3–6.

**P4-M12 — Reference [19] cosmic birefringence: WMAP+Planck is not referenced via Eskilt et al. 2022 PRD precisely (verify volume/page).** I do not have a verified record to confirm 106, 063503 (2022). The author should double-check Eskilt & Komatsu's reference details; PRD will flag any incorrect arXiv/DOI mapping.

**P4-M13 — The HuggingFace catalog identifier is "bamfai/galaxy-chirality-catalog" but the author affiliation is "Independent Researcher" with email hubify.com.** Clarify the authorship/ownership relationship between the upload account and the author for institutional traceability.

---

## MINOR findings

**P4-m1 — Sec. III C "rotation-TTA probes classifier non-equivariance rather than the chirality assignment itself" is correct but the paper does not show the explicit rotation-vs-flip decomposition. Add one paragraph in App. B making the group-theoretic decomposition explicit.

**P4-m2 — Sec. IV B "The 3.86× asymmetry-suppression factor from raw +2.05% to equivariant −0.53%": 2.05/0.53 = 3.87, OK. But +2.05% raw should be the Catalog A 0.79% excess from Table II, not 2.05%. Reconcile.**

**P4-m3 — Sec. V A "30× extension" of Iye et al. (2021): Iye used ~1.27×10⁵ galaxies; 3.2×10⁶/1.27×10⁵ = 25.2, not 30×. Correct.**

**P4-m4 — Table I header "N_map weighted exceeds N_catalog spiral because W_p includes non-spiral galaxies (∼62% of the catalog)." 5,547,858/3,201,160 = 1.733; if 37.78% are spirals, expected ratio is 1/0.3778 = 2.65 if all-galaxy were on the same footprint. The discrepancy (1.73 vs 2.65) is consistent with the all-galaxy mask differing from the spiral mask, but state this explicitly.**

**P4-m5 — Abstract: "isotropic-null bootstrap, NMC = 10,000" — define what is held fixed and what is shuffled in the bootstrap (positions? labels? both?).

**P4-m6 — Sec. III B equation (1) is a sequence of layer dimensions, not an equation. Number it correctly (it is not a mathematical statement).

**P4-m7 — Sec. IV B "the spatial uniformity (all 7 equatorial coordinate slabs within 0.5% of 50/50; available in the companion data repository)." Critical-path null evidence should be in the paper, not "available in the companion repository." Add a one-row table.

**P4-m8 — Sec. VI A "GZ1-dilution factor g = 2a − 1 ≈ 0.398 for a = 0.6991, giving a true-underlying threshold ∼1.88%": 2(0.6991) − 1 = 0.3982. 0.75%/0.3982 = 1.88%. OK arithmetic, but the dilution model (assuming symmetric label noise) should be stated explicitly.

**P4-m9 — Sec. III D "Catalog A (raw, single-pass softmax); Catalog B (Platt-calibrated, +0.4% excess); Catalog C (equivariant production, 2-fold flip TTA)." See E7.**

**P4-m10 — App. A "Apodization: none on the canonical mask; C² 2° apodization on the subsample mask." The fact that the headline mask is apodized and the diagnostic mask is not is a significant methodological asymmetry that should be flagged in the main text, not buried in Appendix A.

**P4-m11 — Table V T2 "Rotation stability > 80%: 94.4%" — what rotation angles? "60° increments" per body, but the test definition (mean? min? max?) is not given.

**P4-m12 — "Mean classification confidence is 0.951, median 0.9997" — median ≈ 1 implies mean is dragged down by a tail; report the 10th percentile.

**P4-m13 — "headline 93.7% three-class accuracy (with augmentation active); post-hoc evaluation without augmentation yields 94.9%" — clarify which is the production number; conventionally one reports without augmentation for headline accuracy.

**P4-m14 — Sec. III A "(σ_dipole = 0.43, p = 0.30)" — should be |σ| = 0.43 (the body gives +0.43σ).

---

## NITs

**P4-n1 — "(Dated: June 2026)" — verify date for submission.

**P4-n2 — The double "Catalog C-full +4.31σ" in App. E.b — clarify what "+4.31σ" estimator this is; it is not in Table I.

**P4-n3 — Many references mix arXiv IDs with DOIs in different formats; standardize.

**P4-n4 — Reference [35] is "Zonca et al. JOSS 4, 1298 (2019)" — author list truncation should follow PRD style.

**P4-n5 — "AI tool usage" disclosure at top of references is appropriate but should be moved to the Acknowledgments section per PRD style.

**P4-n6 — "Software" list uses inconsistent citation styles (some [31], some no ref).

**P4-n7 — Phrase "primary scientific result" is used in three different places to refer to two different estimators; pick one.

**P4-n8 — Page count: 11 pages for a null result is acceptable; recommended target is ≤ 10 after title and abstract are trimmed.

---

## Summary recommendation

**REJECT** (with explicit invitation to resubmit after substantial revision).

The underlying analysis is competent and the monopole-mask leakage diagnostic is genuinely useful, but the manuscript fails PRD standards on (i) presentation of significance, where the headline +3.64σ canonical-mask number is acknowledged in the same parenthesis to be ≈1.9σ Gaussian-equivalent on rank; (ii) version-history language and an "in queue" rerun retained in the body and footnotes; (iii) a multi-clause press-release title; (iv) a primary mask that is never quantitatively defined and appears post-hoc relative to the diagnostic mask; (v) a falsification framing that is in fact only a sensitivity statement; and (vi) load-bearing numbers (Table II σ-deviations, "30×", Catalog B description, abstract HC cut) that do not reproduce from the displayed inputs. With a 30–40% rewrite — single headline, single null procedure for each row of the main table, mask construction documented, "in queue" work either done or removed, and the +3.64σ headline replaced by the rank-based number — this can become a publishable PRD null result. As submitted it is not.

---

## PASS 2 — self-critique findings (what initial review missed)

# Referee Report — Paper P4 — SECOND PASS

After re-examining the paper with the targeted checklist, I have identified the following **additional** issues not in my initial review.

---

## Additional ESSENTIAL findings

**P4-E11 — Training set arithmetic does not reconcile.**
Sec. II B states three sources with explicit counts: GZ1 (6,637) + CE-ResNet (17,153) + Synthetic (2,000) = **25,790**, but the paper claims "*The combined training set contains 26,636 images*". The discrepancy is **846 images** unaccounted for. Additionally, the claim that "*67.6% of training labels derive from CE-ResNet predictions*" does not reproduce: 17,153/25,790 = 66.5% and 17,153/26,636 = 64.4%; neither equals 67.6%. Solving for self-consistency: 67.6% × 26,636 = 18,006 ≈ CE-ResNet contribution, suggesting either the CE-ResNet count (17,153) or the total (26,636) is misstated. The discrepancy involves a load-bearing dataset characterization since this same 67.6%-from-CE-ResNet number is invoked as a key caveat ("*validation metrics partially reflect agreement with CE-ResNet rather than independent ground truth*"). Recount and reconcile.

**P4-E12 — Asymmetry-field denominator inconsistency between Sec. IV C and Appendix A.**
Sec. IV C Eq. (3) defines Aₚ = (N⁽ᵖ⁾_CW − N⁽ᵖ⁾_CCW)/(N⁽ᵖ⁾_CW + N⁽ᵖ⁾_CCW), spirals-only denominator. Appendix A explicitly states "*Field: scalar (spin-0) asymmetry map Aₚ = (N⁽ᵖ⁾_CW − N⁽ᵖ⁾_CCW)/N⁽ᵖ⁾_total*", using N_total without qualification — exactly the same notational ambiguity that the Sec. IV D footnote 1 acknowledges caused a published-revision error. I can verify the spirals-only denominator must be the one actually used: (1,592,107 − 1,609,053)/3,201,160 = −0.005294 ≈ the quoted ⟨A⟩_mask,gw = −0.005294; the all-galaxy denominator would give −0.002. So Appendix A's "N⁽ᵖ⁾_total" is sloppy and conflicts with Eq. (3). Either Eq. (3) and Appendix A must use literally identical notation, or one must be explicitly defined relative to the other. Currently a careful reader cannot determine which field NaMaster received without doing this back-calculation. This is the **same** ambiguity flagged in footnote 1, propagated into Appendix A.

---

## Additional MAJOR findings

**P4-M14 — Number of systematic anchors in Appendix D is reported inconsistently three different ways.**
- Abstract: "*a four-null battery + direct cross-spectrum*" (= 5)
- Sec. IV D: "*The five-anchor systematic analysis*" (= 5), followed by parenthetical listing **six** items: "*cross-spectrum, leg-proxy, density-stratified, boundary-distance, full-catalog injection, block-bootstrap WLS fit*"
- Appendix D itself contains **seven** subsections (a–g): apodized-mask, multipole-spectrum, leg-proxy, density-stratified, boundary-distance, joint WLS, operational conclusion
- The parenthetical "full-catalog injection" listed in Sec. IV D as one of the five/six anchors does not appear as a subsection in Appendix D at all.

These four count claims (4, 5, 6, 7) and the missing "full-catalog injection" subsection cannot all be correct. Reconcile and either remove the count claim or revise Appendix D to match.

**P4-M15 — Appendix A reveals that the −0.122σ headline depends on monopole subtraction that increases significance on the canonical mask, contradicting the body framing.**
Appendix A: "*Monopole subtraction reduces decoupled C₁ at ℓ=1 from 2.30×10⁻⁵ to 1.51×10⁻⁵ (∼34%) and **increases σ from +1.85 to +3.64** (the canonical-mask number).*" The body text (Sec. IV D, Sec. VII) attributes the residual exclusively to MASTER's incomplete inversion: "*MASTER decoupling removes the canonical-mask pseudo-Cℓ leakage*", "*residual mode-coupling that MASTER does not fully invert*". But Appendix A discloses that monopole **subtraction** is what produces the +3.64σ rather than +1.85σ — i.e., the diagnostic excess is partly an artifact of the field-construction choice. This deserves prominent main-text treatment, not a single-sentence Appendix A disclosure. If the canonical-mask C₁ before monopole subtraction is only +1.85σ (which rank-equivalent is ≈1.2σ), then the +3.64σ "diagnostic" is the result of a specific processing choice rather than an inherent feature of the data, and the systematic-interpretation argument is weakened.

**P4-M16 — Look-elsewhere correction is applied on top of a max-stat MC null, which is double-counting if the MC was max-stat.**
Appendix C: "*The direct-MC look-elsewhere test (N=10,000 random-label shuffles) gives p_LEE ≤ 10⁻⁴ (rejection of the random-label null); the conservative Bonferroni/BH penalty across ∼650 tested directions reduces post-LEE significance to <1σ.*" Table I row (iv) names this "hemisphere LEE (MC)" / "max-stat MC". If the MC is genuinely a max-statistic null (max over hemispheres on each random-label realization), then it already accounts for the trials and the additional Bonferroni penalty is double-counting. If the MC is per-direction (not max-stat), then naming it "max-stat MC" in Table I is incorrect and the Bonferroni is appropriate. The paper cannot have both: the same null cannot simultaneously be max-stat AND require external multiplicity correction. Clarify which it is and remove the inconsistent claim.

**P4-M17 — Fisher-floor f_sky = 0.46 does not match any other quoted f_sky in the paper.**
Sec. VI A: "*The Fisher Poisson floor at 3σ is ∼0.29% full-amplitude (from σ(A/2) ≈ 0.048% at N_spiral = 3,201,160, f_sky = 0.46).*" Elsewhere the paper uses f_sky = 0.659 (subsample mask), 0.49005 (canonical mask), 0.482 (apodized canonical). 0.46 is not derivable from these and is not otherwise defined. Either state which mask produces 0.46 or recompute the Fisher floor with a documented f_sky.

**P4-M18 — Real-space dipole p = 0.30 is inconsistent with σ = 0.43 under any standard Gaussian convention.**
Sec. IV C: "*the fitted dipole has amplitude significance 0.43σ (p = 0.30 from the isotropic-null bootstrap at N_MC = 10,000)*". For a standard Gaussian one-sided test, σ = 0.43 → p = 0.33; two-sided → p = 0.67. Neither is 0.30. The mismatch implies the bootstrap null is non-Gaussian (which the paper does not state). Either justify with the empirical CDF or convert both to a single null framework. The pattern is identical to the +3.64σ / p_MC = 0.030 (≈1.9σ) mismatch the abstract acknowledges for the canonical residual but does not acknowledge for the real-space dipole — yet here we have the same inconsistency on the **primary cosmological estimator**. The σ value reported throughout (+0.43) is, by the same logic the paper uses for +3.64σ, a moment-ratio statistic and should be reported alongside the rank-based p.

---

## Additional MINOR findings

**P4-m15 — Table III significance column for bandpowers requires an undisplayed ⟨C_ℓ⟩_null.**
The ℓ=1 row significance −0.122 = (1.494 − 1.546)/0.429 works because ⟨C_null⟩ = 1.546 is displayed in the body text. For rows 2–6, only Cℓ and σ_null are shown; the significance values are only consistent if ⟨C_null⟩ is roughly −1.55 to −1.70 across all bandpowers — a *negative* null mean for a power spectrum, which is unusual and demands explanation. Add a ⟨C_ℓ⟩_null column to Table III and explain its sign.

**P4-m16 — Table IV residual significance arithmetic.**
Pre-MASTER pseudo-C₁: data = 1.696×10⁻², null = (1.685±0.007)×10⁻². (1.696 − 1.685)/0.007 = 0.011/0.007 = **1.57**, table says **+1.68**. Difference is ≳ 7%, larger than rounding to three significant figures justifies. Either quote more decimals (e.g., 1.6843 vs 1.696, σ = 0.0066 → z = 1.77) or recompute. Similar issue for the hemisphere row: (3.48 − 1.69)/0.41 = 4.37, paper says +4.42.

**P4-m17 — "Factor of ∼6–12" disfavoring of Shamir is not derivable.**
Abstract / Sec. I: "*inconsistent in amplitude with Shamir's claimed ∼3% signal by a factor of ∼6–12 under the present pipeline*". 3%/0.75% = 4 (empirical floor), 3%/0.29% = 10.3 (Fisher). Neither bound gives 6, and the upper bound only reaches 12 if one uses 0.25% (smaller than the quoted floor). Show the derivation or replace with "*by a factor of ∼4–10*" from documented bounds.

**P4-m18 — Sec. III B layer-dimension line is presented as Eq. (1).**
"LayerNorm → 384→512 (GELU, d=0.3) → 512→256 (GELU, d=0.2) → 256→3 (softmax)" is a layer description, not an equation. Either renumber as a figure/listing or render with proper math notation (no equals sign justifies an equation number).

**P4-m19 — "30× extension" of Iye et al. (2021) does not arithmetically reproduce.**
Sec. V A: 3.2×10⁶/1.27×10⁵ = 25.2, not 30. Same arithmetic error as P4-m3 (initial review), but I realize now the comparison is to Iye's *re-examination* sample, not Shamir's original. Iye et al. used Shamir's SDSS catalog (∼1.27×10⁵). Same ratio. Correct to "∼25×".

**P4-m20 — Hemisphere MC null in Table IV uses N_SIDE_dir = 8 without justification.**
N_SIDE = 8 corresponds to 768 directions on the sphere, but the Bonferroni in Appendix C uses "∼650 tested directions." If 650 ≠ 768, what defines the tested subset (mask-overlap > some threshold)? Document.

**P4-m21 — Appendix E.b "Catalog C-full +4.31σ monopole-preserving dipole" is not in Table I or Sec. IV C.**
This +4.31σ value (a Catalog C real-space dipole *without* monopole subtraction) appears in Appendix E.b only and is presented in contrast to the headline +0.43σ. If the only way to recover the +0.43σ null is to subtract the monopole, that should be in Table I and Sec. III A as part of the declared estimator hierarchy. The current presentation hides the monopole-subtraction step from the headline.

**P4-m22 — Sec. V A "0.32% maximum regional asymmetry" — region undefined.**
Could refer to pixel-level, hemisphere, RA-quadrant, or per-imaging-leg maximum. With reported pixel-level σ noise far above 0.32% per pixel, this number is almost certainly a smoothed-scale or pre-computed-region maximum. Define the smoothing scale.

---

## Additional NITS

**P4-n9 — Sec. III A "(σ_dipole = 0.43, p = 0.30)" — no σ sign convention. Body uses "+0.43σ"; the abbreviated form should match.**

**P4-n10 — App. A "(pymaster 2.6)" — pymaster versioning: NaMaster releases use semver; verify 2.6 is the correct released tag at submission date (June 2026).**

**P4-n11 — App. C "results available in the companion data repository" appears twice; identify the file path within the repository for each.**

**P4-n12 — Footnote 1 spans pages 4–5 and is longer than the body paragraph it annotates; rewrite as a paragraph in Sec. IV D rather than a footnote.**

**P4-n13 — App. A C_2 apodization: the subscript notation "C²" appears in body (Sec. IV) but should be the standard NaMaster C2 apodization scheme — verify formatting.**

**P4-n14 — App. B "T_0 = 10, T_mult = 2" — cosine warm-restart parameters need a unit (epochs?); state.**

---

## Updated bottom-line recommendation

The new findings reinforce my initial **REJECT (resubmit after substantial revision)** verdict and strengthen it. The arithmetic errors in the training-set count (P4-E11), the still-ambiguous field denominator now propagated into Appendix A (P4-E12), the disclosure-buried-in-appendix that monopole subtraction is doing significant work on the +3.64σ headline (P4-M15), and the LEE double-counting (P4-M16) are each independently sufficient to warrant rejection. Combined with the issues from the first pass — most importantly the post-hoc subsample mask anchoring the headline (P4-E5), the +3.64σ vs ≈1.9σ-Gaussian-equivalent inconsistency (P4-E3), and the "in queue" rerun (P4-E2) — the paper requires a major rewrite. The author should run all numerical claims through a single calculation script and reconcile every quoted value before resubmission.