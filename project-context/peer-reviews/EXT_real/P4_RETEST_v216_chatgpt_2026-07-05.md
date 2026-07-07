# P4 RETEST — v1.0.216 — ChatGPT EXT (RECORD-ONLY per gate H)

- **Reviewer:** ChatGPT (Pro Extended / Extended Thinking, personal account, Houston)
- **Date:** 2026-07-05
- **Paper:** P4 (Galaxy Chirality and Environment) v1.0.216
- **PDF:** /tmp/retest_P4_v216.pdf (983360 bytes)
- **Chat (fresh):** https://chatgpt.com/c/6a4c439c-c400-83e8-9b0a-baed3b910a88
- **Screenshot:** P4_RETEST_v216_chatgpt_2026-07-05.png
- **Prompt:** PRD referee, exact (1)VERDICT / (2)ISSUES [MAJOR]/[MINOR] / (3) central-claim sentence
- **VERDICT (verbatim from "(1) VERDICT:" line):** REJECT
- **Gate status:** RECORD-ONLY. Per standing directive H (2026-07-01), ChatGPT's literal verdict is NOT part of the convergence gate; it oscillated reject↔major-revisions across RS5-8 on unchanged content (structural harsh-referee floor). Convergence = Grok+Gemini ACCEPT/accept-track + every ChatGPT MAJOR truth-audited non-real. This REJECT is the expected maximally-harsh referee floor; each MAJOR must be dispositioned in the truth-audit (not by this browser leg).

## Raw verbatim response

(1) VERDICT: REJECT

(2) ISSUES:

[MAJOR] Secs. III.B–IV.C / primary high-confidence dipole claim: the headline null is obtained only after selecting peq > 0.6, which discards about 70% of classified spirals, while the unthresholded catalog gives a significant real-space excess z ≈ 4.2–4.4; the manuscript's assertion that the cut is "pre-specified" by a code commit is not an adequate substitute for a blinded analysis protocol, and the text itself motivates the cut by removal of the systematic-dominated tail.

[MAJOR] Secs. II.B, IV.A, Appendix B / classifier validity: the classifier has only 69.91% independent GZ1 spiral-chirality accuracy and 58.7% three-class accuracy, yet the paper makes sub-percent anisotropy claims using hard argmax labels; the dilution treatment g = 2a − 1 assumes symmetric, spatially independent errors and does not address morphology-, depth-, seeing-, or footprint-dependent misclassification, which is precisely the dominant systematic class identified later.

[MAJOR] Secs. IV.C–IV.D, Appendix D / inconsistent estimator hierarchy: the manuscript reports mutually discordant results across estimators—HC real-space +0.41σ, unthresholded real-space ≈4σ, MASTER +7.28/+7.93σ, canonical direct-MC +3.64σ, and post-MASTER monopole-null residual ≈+5σ—then declares the non-null channels "diagnostic" without a joint likelihood or quantitative rule established independently of the outcomes; this is not a statistically controlled basis for a cosmological null claim.

[MAJOR] Sec. IV.D / systematics attribution of the harmonic residual: the forward model accounts for only about 52–54% of the observed ℓ = 1 residual and explicitly leaves ≈47% unexplained, yet the text concludes that the residual is survey-systematic rather than cosmological; the evidence supports "unexplained residual with partial correlation to survey templates," not the stronger attribution claimed.

[MAJOR] Appendix D / z ≈ −18 "clean 1.7% dipole" disfavor: the block-bootstrap WLS statistic is presented as a primary exclusion-like result, but it is based on a template fit to classifier-derived labels with known spatial systematics, does not propagate per-galaxy classification uncertainty into the bootstrap covariance, and is explicitly described elsewhere as not a calibrated detection significance; it should not be used as a load-bearing PRD-level exclusion or disfavor statistic.

[MAJOR] Sec. VI.A / pseudo-label independence: because 66.5% of training labels come from CE-ResNet, the production catalog is not independent of the comparison catalog; the GZ1-human-only cross-check uses only 46,017 galaxies, has far lower sensitivity than the headline sample, and cannot rule out pseudo-label-inherited large-scale structure in the full DESI catalog at the claimed sub-percent level.

[MAJOR] Secs. IV.C, VI.B / injection-recovery calibration: injections are performed at the catalog/map-label level, not through image simulation, classifier inference, HC selection, and map-making end-to-end; therefore the quoted A50 and A95 thresholds calibrate the estimator conditional on the produced labels, not the complete measurement pipeline or its dominant classifier-selection systematics.

[MAJOR] Appendix A / MASTER analysis conventions: the manuscript mixes Ap, Ap/2, fCW − 0.5, weighted and unweighted masks, canonical and apodized footprints, 500-MC and 10⁴-permutation nulls, shot-noise-debiased and non-debiased interpretations, while repeatedly warning that the numbers are not comparable; a PRD submission needs a single declared data vector and likelihood for each claim, not a collection of incommensurable diagnostics.

[MAJOR] Data Availability / reproducibility: the paper depends on numerous repository artifact paths, live-main-branch files, unstated exact hashes for many results, and a future Zenodo DOI "to be deposited"; this is insufficient for reproducing a large observational claim at review time.

[MINOR] Sec. III.D and Appendix B / equivariance claims: flip-swap correlation = 1.000 is a consequence of the TTA averaging definition, not an empirical validation of the learned classifier; the manuscript sometimes treats it rhetorically as bias-hardening evidence beyond an implementation check.

[MINOR] Appendix B / QC mismatch: the recovered flip-pass probabilities are outside [0,1] for 2.9% of rows and 6.3% of the HC sample is flagged; the text says removal does not change the HC dipole, but this pipeline inconsistency should be resolved before publication, not treated as a side note.

[MINOR] Secs. I, V, VII / comparison with Shamir: the manuscript repeatedly states amplitude-level tension with Shamir while also conceding no matched Ganalyzer reanalysis was performed; the comparison should be reduced to a qualitative motivation unless analyzed with matched selection, footprint, redshift, and estimator.

[MINOR] Sec. VI.C / physics interpretation: the paper admits the ℓ = 1 projected chirality dipole is parity-even and no transfer function to primordial parity-violating sectors is derived; the PRD motivation should be narrowed accordingly, because the current analysis is primarily an observational catalog/systematics study rather than a direct test of parity-violating physics.

[MINOR] Presentation throughout: the manuscript is overburdened with internal artifact names, implementation notes, caveats, and repeated explanations of incomparable σ values; it needs substantial condensation and a clearer statistical analysis plan before it can be evaluated as a physics result.

(3) The central claim is supported only in the narrow conditional sense that the selected peq > 0.6 real-space estimator is null, but the broader claim of a robust survey-scale/cosmological null and disfavoring of Shamir-scale dipoles is not supported by the evidence presented.

## Orchestrator note

ChatGPT = **REJECT** (record-only). This is the expected structural harsh-referee floor (pattern H). Nearly all 9 MAJORs re-flag content that is disclosed/handled in v216 (peq>0.6 pre-registration commit 94113e5; g=2a−1 dilution as a conservative floor; diagnostic-vs-cosmological separation; 52-54% forward-model coverage explicitly disclosed with the A_50≈0.75% real-space exclusion bound; GZ1-human-only independent cross-check). No genuinely-new real finding evident on face; each MAJOR requires source-cited truth-audit disposition (patterns 061-064) — NOT closed by this browser leg. Notably ChatGPT and Grok cite the SAME facts (52-54% coverage, 69.91% GZ1 accuracy, injection-recovery grid) but Grok rates them [MINOR]/supported and ChatGPT rates them [MAJOR]/reject — textbook referee-variance divergence (pattern 066).
