# P4 R-v166-c1 — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 389.5s

---

Meta-referee report — P4 (PRD submission)

Below are issues that, to the best of my reading, none of the five prior reviews identified. Each item includes a pinpoint citation, why it was missed, the specific problem, and a concrete fix.

P4-META-E1
Severity: ESSENTIAL
Section II.B Training Labels, p. 3
Why others missed it: Most prior reviews focused on estimator/null issues; none reconciled the training-label bookkeeping.
Problem: The training-label source counts do not sum to the stated total, and the quoted CE-ResNet fraction is arithmetically inconsistent. Text: “(1) GZ1: 6,637… (2) CE-ResNet: 17,153… (3) Synthetic hard negatives: 2,000… The combined training set contains 26,636 images… Note: 67.6% of training labels derive from CE-ResNet predictions.” But 6,637 + 17,153 + 2,000 = 25,790, not 26,636. Also, 17,153 / 26,636 = 64.4%, not 67.6%.
Required fix: Reconcile and tabulate all training-label sources so they sum exactly to 26,636 (or correct the total). Correct the CE-ResNet share to the precise value (and define whether the denominator excludes the synthetic negatives). Provide a one-line audit of any additional sources (the missing 846 examples).

P4-META-E2
Severity: ESSENTIAL
Data Availability, p. 13
Why others missed it: Reviewers commented on DOIs and permanence, but not URL integrity.
Problem: The published URLs are malformed with inserted spaces and a misspelled path, making them non-resolvable. Text: “https://huggingface.co/dataset s/bamfai/galaxy- chirality- catalog” (space in “datasets” and around hyphens), and “https://huggingface.co/bamfai/gala xy-chirality-v2” (space in “galaxy”).
Required fix: Correct the URLs to valid, copy-pasteable links (no embedded spaces), and, ideally, add persistent DOIs (Zenodo) for the exact versions used.

P4-META-M1
Severity: MAJOR
Figure misnumbering, Fig. 7 panel header, p. 9 (image)
Why others missed it: Requires looking closely at the embedded panel label inside the figure image.
Problem: The panel graphic itself is labeled “Fig. 11” while the caption and text refer to “FIG. 7.” This is a production-level inconsistency that will confuse citation and cross-referencing.
Required fix: Regenerate the figure with the correct internal label, or remove embedded figure numbering from the panel image.

P4-META-E3
Severity: ESSENTIAL
Appendix B.d (Bias-hardening suite) vs Fig. 6, pp. 11–12
Why others missed it: The contradiction spans a prose test definition, a summary table, and a separate figure.
Problem: The acceptance criterion for the calibration test (T7) contradicts the measured distribution, yet the test is marked PASS. Text: “T7 confidence calibration (qualitative, < 50% at confidence > 0.9)” (Appendix B.d), Table V: “T7: Calibration qualitative PASS,” while Fig. 6 states “Strongly bimodal: 73.6% at max p ≥ 0.9.”
Required fix: Either revise the stated T7 threshold to match what is being tested (and justify why 73.6% at >0.9 is acceptable), or mark T7 as failing and provide a remedial calibration (e.g., temperature scaling, ECE/Brier metrics reported).

P4-META-M2
Severity: MAJOR
Sensitivity-floor fsky inconsistency, Sec. VI.A, p. 9
Why others missed it: Prior reviews questioned the derivation but not the internal fsky mismatch.
Problem: The Fisher floor uses fsky = 0.46 without motivation, while the rest of the paper consistently quotes fsky ≈ 0.490–0.494 (binary/apodized variants). Text: “σ(A/2) ≈ 0.048% at Nspiral = 3,201,160, fsky = 0.46.”
Required fix: Use a single, documented fsky/feff,sky for the Fisher estimate (ideally the same as in the estimator being benchmarked), show the derivation explicitly, and reconcile 0.46 with the 0.49± values used elsewhere.

P4-META-M3
Severity: MAJOR
Hidden conditioning in label-shuffle nulls (spirals vs all galaxies), multiple locations (e.g., Sec. IV C–D; Table I; Appendix A.a), pp. 6–11
Why others missed it: The paper uses several similar phrases for nulls; none explicitly states whether NS galaxies are included in shuffles for a spirals-only field.
Problem: The text alternates between “global per-galaxy label-shuffle,” “per-pixel random-label permutation null,” and “depth-stratified null (labels permuted within 10 Nall(p) deciles).” Since Ap is defined on spirals only, shuffling labels across all galaxies (including NS) would change the trial pool and bias the null. There is no explicit statement that shuffles are restricted to spiral-labeled galaxies with fixed Nspiral(p).
Required fix: Define each permutation null unambiguously, stating whether labels are shuffled only among spirals and whether Nspiral(p) is held fixed. If any results used an inconsistent shuffle (including NS), rerun and update affected numbers.

P4-META-M4
Severity: MAJOR
Cross-spectrum definition and units (rℓ) and negative “σ,” Appendix D.g, p. 13
Why others missed it: It’s an unusual statistic tucked in a long appendix; the sign misuse is subtle.
Problem: The paper reports “direct cross-spectrum C(Ap×ntotal) at ℓ = 2 gives r = −0.65 with σ = −2.89.” A correlation coefficient rℓ requires a definition (e.g., Cℓ^XY / sqrt(Cℓ^XX Cℓ^YY)); with negative auto-bandpowers in Table III, ρℓ may be ill-defined. Also, a “σ” should not be negative—if it is a standardized z, say so and keep the sign convention clear.
Required fix: Define rℓ precisely (including noise de-biasing and handling of negative auto-powers), ensure units are consistent, and report |z| with a separate sign for direction if desired. Provide the null distribution used to compute the z and clarify sidedness.

P4-META-M5
Severity: MAJOR
Monte Carlo sample sizes underpowered for quoted pMC and A95 claims, multiple locations (e.g., Table I row (iii), Sec. VI.A), pp. 4, 9
Why others missed it: Reviewers noted absent A95 plots but not the implications of small N for tail accuracy.
Problem: Key claims rest on N = 500 permutations (pMC = 15/500 = 0.030 → “≈ 1.9σ”) and NMC,inj = 100 per amplitude for injection–recovery. Such small N yields coarse p resolution (Δp ≈ 0.002) and poor tail accuracy, especially problematic when contrasting moment-ratio “+3.64σ” to empirical rank “≈1.9σ.”
Required fix: Increase permutations/injections by at least an order of magnitude (e.g., N ≥ 10,000 for harmonic-space pMC; NMC,inj ≥ 1,000 per amplitude), re-estimate pMC with confidence intervals, and provide a proper Pdet vs A curve to substantiate A95.

P4-META-M6
Severity: MAJOR
Weighting-field/observable mismatch in NaMaster setup, Appendix A.a, p. 11; Sec. IV C, p. 6
Why others missed it: The weighting choice was noted, but not the conceptual unit mismatch.
Problem: The asymmetry field is defined on spirals only, Ap = (NCW − NCCW)/Nspiral, yet the NaMaster weight map uses Wp = Nall (spirals + non-spirals). This mixes a depth proxy for a different sample with heteroskedastic noise in Ap tied to Nspiral, which can couple to survey structure in nontrivial ways (as evidenced by +7.28σ vs +9.78σ sensitivity to Wp). The conceptual inconsistency is not addressed.
Required fix: Justify and test the weighting choice rigorously: present results with Wp = Nspiral, Wp = Nall, and uniform weights; quantify how each changes C1 and its null width; and adopt a pre-registered, physically consistent choice (ideally Wp ∝ Nspiral for an Ap field) for headline diagnostics.

P4-META-m1
Severity: MINOR
Cross-reference mismatch in the Abstract: duplicate “at z ≈ −18,” p. 1
Why others missed it: Likely skimmed as stylistic; it reads as a duplicated phrase.
Problem: Abstract states “… disfavors a clean cosmological dipole at the 1.7% reference amplitude at z ≈ −18 (Appendix D).” The trailing “at” repeats awkwardly and risks confusion with redshift in the same clause.
Required fix: Edit to “disfavors a clean cosmological dipole at the 1.7% reference amplitude (test statistic z ≈ −18; Appendix D).”

P4-META-m2
Severity: MINOR
Ambiguous use of “per-spiral” in the Abstract HC count, p. 1
Why others missed it: Others flagged threshold asymmetry but not this wording.
Problem: Abstract: “471 049 high-confidence per-spiral after peq_CW > 0.9.” “Per-spiral” is unclear, and the criterion is asymmetric (only CW). The body later uses symmetric cuts on max(peq_CW, peq_CCW).
Required fix: Replace with “471,049 high-confidence spirals with max(peq_CW, peq_CCW) > 0.9” and ensure that this exact criterion and N are shown in Fig. 6.

P4-META-N1
Severity: NIT
Appendix A.c vs D.a: apodized fsky values never consolidated in one place, pp. 11–12
Why others missed it: They noted inconsistencies but not the presentation gap.
Problem: Different apodized sky fractions (0.488, 0.482, 0.452, 0.420) are scattered across sections without a single definitive table mapping mask/weight/apodization → (fsky, feff,sky).
Required fix: Add a compact table listing geometric fsky and feff,sky for each mask/weight/apodization combination used by any estimator, and cite it consistently.

Meta-review recommendation
MAJOR REVISIONS

Given the union of all six reviews, there are multiple essential and major blockers: inconsistent catalog statistics/figures, unverifiable significance tables, ambiguous nulls, version-history language, broken reproduction links, and several new arithmetic and methodological inconsistencies (training-label accounting, calibration test contradiction, fsky drift in the Fisher floor, null-definition ambiguity for NS vs spirals, weighting/observable mismatch, underpowered MC for pMC and A95). My assessment is that the blocker count is high (≥12 distinct essentials/majors across reviews), and without a thorough rewrite and re-analysis on several points, the paper would likely not survive external peer review. With a careful, comprehensive fix pass — unifying definitions, recomputing all load-bearing numbers, removing provenance clutter, and strengthening the null and injection procedures — the core claim (real-space dipole consistent with null; quantified monopole–mask leakage) could be publishable. My confidence the work can be rehabilitated is moderate, contingent on addressing the above with full numerical transparency.