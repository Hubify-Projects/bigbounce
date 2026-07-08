(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

[MAJOR] Sections III B/IV C/VI B: The declared “primary” null rests on the peq > 0.6 high-confidence cut, but the manuscript also reports a z≈4.0–4.4 unthresholded real-space dipole and significant harmonic residuals; the argument that these are entirely low-confidence systematics is plausible but not yet demonstrated by an independent selection-function model, so the null conclusion is conditional on a post-selection classifier regime rather than the full catalog. 

cw_P4

[MAJOR] Sections II/Appendix B/VI A: The classifier validation is insufficient for a PRD-level cosmological inference: external GZ1 chirality accuracy is only 69.91% with κ=0.40, 66.5% of training labels derive from CE-ResNet pseudo-labels, and the GZ1-human-only cross-check has an acknowledged A50≈3.4% sensitivity, far weaker than the claimed sub-percent headline sensitivity. 

cw_P4

[MAJOR] Sections IV C–IV D/Appendix D: The manuscript repeatedly reports large harmonic-channel excesses (+3.64σ, +7.28σ, +7.93σ, ℓ=2 > ℓ=1) and then classifies them as diagnostic systematics, but the forward model accounts for only ≈52–54% of the ℓ=1 residual and explicitly leaves ≈47% open; this is not a closed systematic budget. 

cw_P4

[MAJOR] Sections III A/IV C/Table V/VII: The significance conventions are fragmented across pixel-permutation, label-shuffle, rank-p, moment-z, MASTER, and block-bootstrap definitions; although the manuscript warns that they are not comparable, it still uses them rhetorically together to support the same conclusion, which makes the statistical interpretation of the central claim underdefined.

[MAJOR] Section IV C/Appendix D: The z≈−18 “exclusion” of a clean 1.7% dipole is not a calibrated likelihood exclusion; it is a block-bootstrap template-model-disfavor statistic on a different sample and field than the primary HC real-space estimator, with classifier-label uncertainty and full confidence/depth/morphology covariance not jointly marginalized.

[MAJOR] Sections IV B/IV C/Data Availability: The catalog has a statistically significant global CW-fraction monopole of −9.47σ, a documented raw/equivariant pipeline-pass mismatch affecting 2.9% of rows, and a retained QC-flagged population; the manuscript argues these do not affect the dipole, but a PRD submission needs a simpler, quantitative propagation of these defects into the final dipole amplitude and uncertainty.

[MAJOR] Sections V/VII: The comparison with Shamir is too strong in places: the manuscript says it does not claim a frequentist exclusion, but phrases such as “would have been detected here,” “unmissable,” and “disfavors the Shamir detection class” overstate what follows without a matched Ganalyzer reanalysis on the same footprint and cuts.

[MAJOR] Data Availability/throughout: The analysis relies heavily on many repository artifacts, commit hashes, scripts, JSON files, and “pod-deferred” computations that are not included as an immutable archival record in the submitted manuscript; for PRD review, the exact catalog, masks, null arrays, and scripts supporting every quoted σ and p-value must be frozen and directly reproducible.

[MINOR] Title/abstract/introduction: The title and opening framing should avoid implying a direct parity-violation test, because the manuscript later states that the ℓ=1 observable is parity-even and only constrains an isotropy-breaking axial-vector channel.

[MINOR] Tables I–IX/Sections III–VII: The paper is overlong and internally repetitive, repeatedly restating the estimator hierarchy and caveats; the main text should be shortened and the diagnostics moved to appendices with one consolidated statistical summary table.

[MINOR] Appendix B: The D4-TTA discussion reports a 21.4% argmax label flip rate on borderline galaxies; this should be presented earlier as a limitation of hard-label dipole estimation, not buried as a classifier-stability detail.

[MINOR] Figures 4, 7, 8, 9: Several figure captions mix field definitions, estimator conventions, and σ caveats; the captions should state only the plotted quantity and refer to a single methods table for significance definitions.

(3) The central claim of no robust high-confidence real-space chirality dipole is directionally supported, but the stronger claim of a survey-scale sub-percent cosmological null is not yet fully supported because classifier systematics, selection effects, and harmonic residuals are not closed in a unified statistical model.

--- HARVEST META: chat=https://chatgpt.com/c/6a4db9c8-395c-83e8-8e05-6a917bc54d08 | model=ChatGPT Pro (High) | 2026-07-08 ---
