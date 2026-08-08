# P4 v1.0.213 De-biased EXT Re-test — CHATGPT (for record)

- **Reviewer:** ChatGPT (chatgpt.com)
- **Account:** Personal (ChatGPT Pro)
- **Model:** GPT-5 Pro Extended (Extended Thinking)
- **Timestamp:** 2026-07-05
- **Chat URL:** https://chatgpt.com/c/6a4c29e1-5130-83e8-85a4-6430233c0cc7
- **PDF:** /tmp/retest_P4_v213.pdf (974375 bytes)
- **Prompt:** standard PRD referee prompt (VERDICT / ISSUES [MAJOR|MINOR] / one-sentence central-claim)
- **(1) VERDICT line:** REJECT
- **Note:** Per directive H — ChatGPT ACCEPT is NOT part of the recalibrated gate; the calibrated referees are Grok + Gemini. ChatGPT REJECT here is the maximally-harsh LLM-referee structural floor (15 MAJOR); recorded for the record only. Each ChatGPT major must be truth-audited to a non-real verdict, not treated as a blocking ACCEPT requirement.

---

## RAW RESPONSE (verbatim)

(1) VERDICT: REJECT

(2) ISSUES:

[MAJOR] Abstract / Secs. III–IV, central estimator hierarchy: the manuscript declares a “primary” +0.41σ high-confidence real-space null while simultaneously reporting multiple high-significance harmonic and hemisphere residuals (+3.64σ, +7.28σ, +7.93σ, pLEE≤10⁻⁴) and then dismissing them as “diagnostic” by assertion; this is not an adequate statistical resolution of incompatible low-ℓ evidence, especially since the estimator, mask, weighting, field definition, MC size, and null all change across rows.

[MAJOR] Sec. IV C, confidence-threshold dependence of the primary null: the headline null depends on cutting at peq>0.6, while the unthresholded catalog gives a z≈4.2–4.4 real-space excess; the manuscript labels this excess a low-confidence systematic, but does not demonstrate with an external truth sample, image-level simulations, or a generative selection model that a real chirality signal could not preferentially appear in the excluded population.

[MAJOR] Secs. II, IV A, VI B, classifier validation: the independent GZ1 chirality accuracy is only 69.91% with κ=0.40, the three-class accuracy is 58.7%, and the catalog probabilities are explicitly overconfident; hard argmax CW/CCW counts are then treated as a precision cosmological field without a full propagation of spatially varying classification confusion, triage-to-nonspiral errors, and sky-dependent purity.

[MAJOR] Sec. VI B, injection-recovery sensitivity: the injection tests are performed at the catalog/count-map level, not by injecting into images and re-running the classifier, so they do not validate the claimed physical sensitivity to a true galaxy-handedness dipole under classifier dilution, morphology selection, seeing/depth variation, and not-spiral triage.

[MAJOR] Sec. VI A, pseudo-label independence: 66.5% of the training labels derive from CE-ResNet predictions, yet the proposed “decisive” GZ1-only check uses only 1.50×10⁴ high-confidence spirals versus 9.5×10⁵ in the headline sample and is explicitly about eight times lower in statistical power; it cannot rule out pseudo-label-inherited survey-correlated structure at the claimed headline sensitivity.

[MAJOR] Sec. IV D / Appendix D, systematics attribution: the forward model explains only about 52–54% of the canonical ℓ=1 residual amplitude and leaves ≳47% unexplained, yet the text repeatedly treats the residual as systematics-attributed and non-threatening; an unexplained coherent low-ℓ residual in the same observable class cannot simply be quarantined from the cosmological interpretation.

[MAJOR] Appendix D, WLS “z≈−18” exclusion of a clean 1.7% dipole: the quoted exclusion is a template-model-disfavor statistic under a chosen block-bootstrap error model, not a calibrated likelihood or posterior including classifier uncertainty, unmodeled systematics, pseudo-label correlations, or signal dilution; presenting it as a primary exclusion alongside the real-space null materially overstates the evidence.

[MAJOR] Secs. IV C, VII, MASTER analysis: Table V, Table VI, and the text use different fields and normalizations—Ap, Ap/2, fCW, monopole-subtracted and non-subtracted maps, binary and depth-weighted masks—while drawing qualitative conclusions about leakage and residuals; this prevents a clean interpretation of the harmonic evidence.

[MAJOR] Sec. IV D, “99.32% monopole-mask leakage” claim: the quoted reproduction applies only to an undeconvolved pre-MASTER pseudo-Cℓ statistic under a different field convention, while the post-MASTER residual is much larger and only partly modeled; it does not justify attributing prior pre-MASTER literature claims or the manuscript’s own harmonic residuals to the same channel.

[MAJOR] Secs. V–VII, comparison to Shamir: the manuscript alternates between fCW units, Ap units, “asymmetry” units, and reported literature amplitudes, and states both amplitude-level tension and non-exclusion; the mapping from Shamir’s estimator and selection to this pipeline is not established, so the factor-of-4–9 tension and “would have been detected” language are not publication-ready.

[MAJOR] Sec. IV C, null construction: the primary pixel-permutation null destroys the relation between per-pixel asymmetry variance and Nspiral(p); although a label-shuffle cross-check is given, the adopted hierarchy still privileges a less physically faithful null for the headline result.

[MAJOR] Appendix E, edge-on contamination: the claim that flip-equivariance excludes directional edge-on bias is too strong because the science statistic uses hard argmax labels and the edge-on fraction, image quality, and morphology mix are sky dependent; the later caveat about argmax nonlinearity does not repair the earlier categorical assertion.

[MAJOR] Appendix C, hemisphere look-elsewhere result: a direct-MC max-statistic pLEE≤10⁻⁴ is a significant rejection of the random-label null, not evidence that “no directional hemispheric asymmetry survives”; calling it a systematic requires a fitted systematic model with residual tests, not a post hoc label.

[MAJOR] Data Availability / reproducibility: the analysis depends on numerous repository artifacts, live-branch paths, private pipeline filenames, and a promised future Zenodo DOI; for PRD review, the exact commit, immutable data release, scripts, random seeds, and all null distributions must be archived and accessible at submission.

[MAJOR] Sec. III B / Appendix A, sample inconsistency: the two “primary” claims are made on different samples—the HC peq>0.6 subset for the real-space dipole and the full Catalog C for the WLS template fit—despite the full sample being known to contain the low-confidence excess; this weakens the logical chain from estimator hierarchy to conclusion.

[MINOR] Abstract and Results: the abstract is overloaded with estimator caveats, run sizes, alternative significances, and parenthetical disclaimers; it obscures rather than clarifies the scientific claim.

[MINOR] Sec. II, data description: the parent-sample selection inherits from Galaxy Zoo DESI and DESI Legacy DR8 cross-matching, but the manuscript does not provide enough detail on duplicates, footprint holes, star/artefact contamination, or failed-coordinate matches to reproduce the survey selection function.

[MINOR] Sec. III D / Appendix B: the D4-TTA discussion reports a 21.4% argmax label change on borderline cases but does not quantify how these borderline cases project onto sky position, depth, morphology, or the low-confidence excess.

[MINOR] Tables I–III: the paper repeatedly warns that σ values are not comparable, but still places them side by side as if they form a coherent decision tree; these tables need to be rebuilt around one declared likelihood or clearly separated into exploratory diagnostics.

[MINOR] References and journal fit: the manuscript reads partly as a catalog/methods paper and partly as a cosmological-null paper; for PRD, the cosmological inference and statistical model must be strengthened substantially, or the catalog release should be redirected to a more appropriate observational/data-journal venue.

(3) The central claim of a robust survey-scale null chirality dipole is not supported by the evidence as presented, because it depends on a thresholded classifier output and a hierarchy that dismisses significant, only partially modeled low-ℓ residuals rather than incorporating them into a single calibrated inference.
