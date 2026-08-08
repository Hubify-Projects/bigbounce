# P4 (v1.0.223) — ChatGPT Deep Research — EXT DEEP round 2026-07-08

- Reviewer: ChatGPT (Deep Research mode selected; ran as extended reasoning, "Thought for 23s" — no clarifying-question gate presented)
- Chat URL: https://chatgpt.com/c/6a4ea707-7b90-83e8-b264-8868687e52cf
- Harvested: 2026-07-08
- PDF: /tmp/deep_P4.pdf md5 a9b8516646624412a0898f1ca91d80dd, page 1 "(Dated: July 7, 2026)", v1.0.223

## PROMPT
You are an expert referee for Physical Review D. Review the attached manuscript to the standard you would apply to a real submission. Respond with exactly: (1) VERDICT: one of ACCEPT / MINOR REVISIONS / MAJOR REVISIONS / REJECT. (2) ISSUES: a numbered list, each prefixed [MAJOR] or [MINOR], naming the specific section/claim and the concrete problem. (3) One sentence on whether the central claim is supported by the evidence presented. Be rigorous and specific; do not inflate or soften.

## RAW RESPONSE (verbatim)

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

[MAJOR] Secs. II, IV A, VI A — classifier validation is not strong enough for the claimed sub-percent cosmological null. The production labels depend heavily on CE-ResNet pseudo-labels, while the independent GZ1 validation gives only 69.91% spiral-chirality accuracy and κ = 0.40. The paper argues this mainly dilutes a real signal, but asymmetric CW/CCW errors, triage into “not spiral,” and sky-dependent confidence/morphology can also create or suppress dipoles. The GZ1-human-only null has N ≈ 4.6 × 10⁴ and the manuscript itself states it is not sensitive to the headline sub-percent regime, so it cannot validate the main null at the claimed sensitivity.

[MAJOR] Secs. III B, IV C — the primary peq > 0.6 high-confidence sample is insufficiently justified as a cosmological selection. The headline null uses only 949,584 of 3,201,160 classified spirals, while the unthresholded Catalog C sample shows a z ≈ 4.0–4.4 real-space excess. The attribution of that excess to “low-confidence systematics” is plausible but not demonstrated with a fully propagated selection function; because peq is uncalibrated and correlated with depth, morphology, and imaging quality, the confidence cut can itself erase or reshape a true sky signal.

[MAJOR] Secs. IV C–D, Appendix D — the estimator hierarchy is not statistically clean. The paper promotes the HC real-space dipole as primary, but the second “primary” WLS clean-dipole exclusion is performed on the full Catalog C canonical-mask Ap field, not the HC sample. The manuscript then treats high-significance MASTER residuals as diagnostic only. This mixture of samples, masks, nulls, weights, and post hoc role assignments prevents a single coherent likelihood-level inference.

[MAJOR] Sec. IV D, Appendix D — the harmonic residual systematic budget is not closed. The manuscript reports +3.64σ, +7.28σ, and +7.93σ harmonic-channel residuals, says monopole-mask leakage explains pre-MASTER power, but also states that monopole-only nulls reproduce only ∼12% of the post-MASTER C1 and that the imaging+morphology forward model explains only ≈53% of the ℓ = 1 residual amplitude. The remaining ≈47% is explicitly open, so the claim that it is not a cosmological loophole rests on an asserted mapping to the real-space A50/A95 floor rather than an end-to-end mock or joint systematic model.

[MAJOR] Appendix D — the z ≈ −18 “clean 1.7% dipole” disfavor is overstated. The block-bootstrap WLS statistic is repeatedly used as load-bearing evidence, but the covariance does not simultaneously marginalize classifier uncertainty, confidence selection, morphology-dependent errors, depth/PSF systematics, and template incompleteness. The paper itself notes rank deficiency, strong nuisance-template collinearity, and absence of a formal simultaneous likelihood. It should be reframed as a diagnostic template-fit result, not a decisive exclusion-level statistic.

[MAJOR] Appendix B and Data Availability — reproducibility and QA are not yet publication-grade. The paper relies on many internal artifact paths and a live repository branch rather than a frozen DOI-tagged archive. It also reports a raw/equivariant pipeline-pass mismatch affecting 2.9% of rows, with recovered flip probabilities outside [0,1] by up to 0.09. Although a flagged-row rerun is said not to change the HC dipole, this is a serious catalog-integrity issue that must be resolved or fully isolated in a frozen release before acceptance.

[MINOR] Title/abstract/introduction — the physical interpretation needs sharper limitation. The paper correctly states that the ℓ = 1 chirality dipole is parity-even and not a direct parity-violation test, but the comparison to parity-violation literature and PRD framing still risks overstating cosmological implications without a transfer function from primordial parity-violating sectors to projected apparent galaxy chirality.

[MINOR] Secs. IV–VII — the manuscript is overlong and internally repetitive. Many caveats, estimator definitions, and warnings about non-comparable σ values are repeated multiple times. The paper should be shortened and reorganized around one primary estimator, one sensitivity statement, and a compact systematic appendix.

[MINOR] Sec. V — comparison with Shamir requires more care. The amplitude-level conversion between Shamir’s reported quantities and the paper’s Ap convention is useful, but the manuscript repeatedly approaches an exclusion claim while disclaiming a matched Ganalyzer reanalysis. This comparison should be toned down unless a matched-footprint reanalysis is performed.

[MINOR] Tables V–IX — σ, rank-p, empirical p, Gaussian-equivalent σ, and recovery thresholds are hard to track. The paper should standardize notation and avoid placing incommensurable significances in visually parallel table rows without a clearer statistical model.

(3) The central null result is plausible for the pre-specified HC real-space estimator, but it is not yet fully supported at the claimed sub-percent cosmological level because classifier validation, confidence-selection effects, and unresolved harmonic residual systematics remain insufficiently controlled.

## TRUTH-AUDIT SUMMARY
- VERDICT: MAJOR REVISIONS
- 6 MAJOR — all are re-flags of already-disclosed limitations / requests for a joint likelihood the paper explicitly says is out of scope: (1) GZ1 low accuracy + sub-percent insensitivity — already disclosed (Grok-Heavy same round flagged the same GZ1 point as MINOR corroboration; paper states GZ1 corroborates not validates); (2) peq>0.6 selection function — disclosed confidence-cut caveat, dilutes-not-creates argument already in paper; (3) estimator-hierarchy "not clean" — the multi-estimator design + role assignment is pre-specified and documented (Grok also flagged density/presentation), an interpretive-preference disagreement not an error; (4) ℓ=1 ~47% unmodelled residual — IDENTICAL to Grok-Heavy's sole MAJOR, already disclosed as pod-deferred forward-model limitation with a-fortiori bound; (5) z≈−18 WLS overstated — paper already notes rank deficiency + collinearity + no simultaneous likelihood, reviewer asks to reframe (editable disclosure); (6) reproducibility/2.9% row mismatch — flagged-row rerun already shown not to change HC dipole; DOI-on-acceptance deposit is standard.
- No genuinely-new physics-correctness error. Every MAJOR is a source-cited re-flag of a disclosed scope limitation OR a request for a joint end-to-end likelihood the paper honestly declares out of scope (pattern-066 referee variance: ChatGPT structurally escalates disclosed limitations to MAJOR where Grok-Heavy same-round called the same items MINOR/1-MAJOR).
