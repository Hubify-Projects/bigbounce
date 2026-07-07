# INT API POST-POLISH (native-PDF) — P4 v1.0.219 — openai (gpt-5.5)
PAPER: P4  |  VERSION: v1.0.219  |  MODEL: gpt-5.5
MODALITY: native-pdf (Files API purpose=user_data + Responses input_file)
UTC: 2026-07-07T07:03:18.348659+00:00  |  latency: 65.4s
USAGE: {"input_tokens": 54019, "input_tokens_details": {"cached_tokens": 0}, "output_tokens": 2329, "output_tokens_details": {"reasoning_tokens": 1034}, "total_tokens": 56348}
PARSED VERDICT: REJECT

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: REJECT.

(2) ISSUES:
1. [MAJOR] Secs. III–IV / declared estimator hierarchy: the manuscript elevates the high-confidence real-space dipole as the primary cosmological estimator while simultaneously reporting large harmonic-channel residuals and a full-sample WLS “exclusion”; these are different samples, fields, masks, weights, and nulls, and the paper never supplies a unified likelihood or covariance model demonstrating that the null real-space result, the +7σ harmonic residuals, and the z≈−18 WLS statement are mutually consistent measurements of the same physical hypothesis.

2. [MAJOR] Secs. II, IV A, VI A / classifier validity: the catalog’s external chirality agreement is only 69.91% with κ=0.40, the softmax scores are admitted to be badly overconfident, and 66.5% of training labels are CE-ResNet pseudo-labels; this is not sufficient to support sub-percent cosmological bounds without a spatially resolved misclassification model, since even small direction-dependent classifier errors can mimic or erase a dipole.

3. [MAJOR] Sec. VI A / independence from pseudo-labels: the GZ1-human-only check is useful but not decisive at the claimed sensitivity, because it contains only ≈4.6×10^4 galaxies, has a ≈4.5× worse statistical floor than the headline sample, and cannot exclude inherited survey-correlated biases in the full pseudo-labeled catalog at the sub-percent level.

4. [MAJOR] Sec. IV C / primary null construction: the isotropic pixel-permutation null preserves the one-point distribution but destroys spatially correlated survey structure and heteroskedasticity tied to the DESI footprint; it is therefore not a valid cosmological null in the presence of the very low-ℓ survey systematics that the paper later demonstrates are present.

5. [MAJOR] Secs. IV C, VI B / injection-recovery and sensitivity floor: the injection tests appear to inject labels or pixel counts into the already-classified catalog rather than injecting signals at the image/classifier level, so they do not propagate the spatially varying classifier response, pseudo-label inheritance, edge-on contamination, or depth-dependent failure modes that dominate the systematic budget.

6. [MAJOR] Secs. IV C, VI B, VII / amplitude conventions: the manuscript repeatedly mixes fCW deviations, Ap=2(fCW−1/2), “full amplitude” A, and Shamir amplitudes; despite warnings, the comparisons remain confusing and sometimes appear to compare observed-space amplitudes with classifier-diluted or true-sky amplitudes without a rigorous transfer model.

7. [MAJOR] Sec. IV D / harmonic residual attribution: the MASTER ℓ=1 residuals are large (+7.28σ/+7.93σ in some conventions), the ℓ=2 excess is also large, and the forward model explains only ≈53% of the ℓ=1 amplitude; assigning the remaining ≈47% to survey systematics is plausible but not demonstrated, and the statement that a residual below A95 cannot be cosmological is not logically valid—it could simply be a real signal below the chosen detection threshold.

8. [MAJOR] Appendix D / WLS “clean 1.7% dipole” exclusion: the z≈−18 block-bootstrap statistic is not a calibrated exclusion significance, uses the full Catalog C rather than the high-confidence primary sample, relies on a rank-deficient nuisance design, and does not jointly marginalize classifier uncertainty, morphology, depth, and spatial covariance; it should not be a load-bearing cosmological result.

9. [MAJOR] Sec. IV C / confidence cut: the peq>0.6 selection removes roughly 70% of classified spirals and is central to eliminating the z≈4 unthresholded excess, but the manuscript does not provide an independent, pre-analysis purity/completeness optimization or show that the retained high-confidence selection has an isotropic selection function.

10. [MAJOR] Secs. IV–VII / comparison with Shamir: the manuscript claims strong amplitude-level tension with Shamir-class signals while also acknowledging different estimators, cuts, footprints, and label definitions; without a matched-footprint reanalysis or a common likelihood, the comparison should be substantially weakened.

11. [MAJOR] Secs. I, VI C / physics interpretation: the paper emphasizes relevance to parity and cosmology, but also states that the ℓ=1 chirality dipole is parity-even and that no transfer function from primordial parity-violating sectors to projected morphology is derived; the PRD-level physics claim is therefore underdeveloped relative to the observational catalog/statistics content.

12. [MINOR] Sec. III A / significance reporting: using many non-comparable σ conventions, one-sided rank p-values, moment-z values, Gaussian-equivalent values, and bootstrap z values makes the presentation difficult to audit; the manuscript should reduce the number of quoted significances and reserve σ language for a single well-defined null wherever possible.

13. [MINOR] Secs. IV–Appendices / overlong and internally defensive presentation: the manuscript contains excessive caveats, artifact paths, parenthetical qualifications, and repeated explanations that obscure the core analysis; it should be rewritten into a concise methods/results structure with appendices reserved for reproducibility details.

14. [MINOR] Data Availability / reproducibility: the repository is described as a live main branch with no frozen tag or DOI, while many claims depend on local artifact paths; a real submission requires immutable versioned data, code, model weights, checksums, and scripts sufficient to regenerate the quoted tables and figures.

15. [MINOR] Formal issues: the manuscript date is in the future, several figure/table captions are unusually long, and some terminology such as “falsification criterion,” “exclusion,” and “null” is used more strongly than the statistical analysis warrants.

(3) The narrow claim that the chosen high-confidence real-space estimator finds no significant dipole is plausibly supported, but the broader claims of sub-percent cosmological sensitivity, definitive systematics attribution, and strong tension with previous work are not yet supported.