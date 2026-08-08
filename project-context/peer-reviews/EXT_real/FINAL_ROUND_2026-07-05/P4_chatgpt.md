# P4 — ChatGPT (Pro Extended) — FINAL ROUND
- paper: P4 (galaxy chirality catalog)
- version: v1.0.217
- model: ChatGPT Pro Extended (chatgpt.com)
- timestamp: 2026-07-07T02:20:00Z
- chat_url: https://chatgpt.com/c/6a4c60d2-3b38-83e8-b53d-ec11f2b37d5f

## RAW VERBATIM RESPONSE

(1) VERDICT: REJECT 

final_P4

(2) ISSUES:

[MAJOR] Sec. IV C, primary “real-space dipole consistent with null” claim: the result changes from a significant unthresholded real-space excess, z ≈ 4.2–4.4 at Ap = 0.57%, to z = 0.41 only after imposing peq > 0.6, which removes about 70% of the classified spirals; the manuscript asserts this cut was pre-specified and systematics-motivated, but the evidence presented does not establish that the discarded population can be excluded from the survey-scale inference rather than being part of the measured sky signal.

[MAJOR] Secs. III B, IV C, VI B, declared estimator hierarchy: the paper treats the high-confidence subset as the primary cosmological estimator while simultaneously advertising an 8.47M-galaxy / 3.2M-spiral survey-scale catalog; the central scientific conclusion should either be explicitly restricted to the peq > 0.6 subset or the full-sample significant excess must be modeled and included in the inference.

[MAJOR] Secs. III A, IV C–D, Tables II–VI: the significance accounting is not publishable in its present form; the manuscript reports many σ values from incompatible nulls, sample cuts, fields, masks, weighting conventions, and MC sizes, then repeatedly states they are not comparable, but still uses them rhetorically to support a coherent scientific conclusion.

[MAJOR] Sec. IV C, null construction for the primary dipole: the pixel-permutation null destroys spatial correlations in survey depth, PSF, footprint, extinction, morphology, and classifier accuracy, precisely the correlations the manuscript later shows are important; therefore the quoted z = 0.41 and p = 0.31 do not constitute a calibrated cosmological null test.

[MAJOR] Secs. II, IV A, Appendix B, classifier validation: the chirality classifier has only 69.91% independent GZ1 chirality agreement, strong softmax overconfidence, mild CW/CCW asymmetry, and 66.5% CE-ResNet-derived training labels; this is inadequate for a sub-percent dipole claim unless the spatial dependence of the full confusion matrix is measured and propagated.

[MAJOR] Sec. VI B, injection-recovery sensitivity floor: the injections are applied at the catalog/count-map level, not through the image classifier, so they do not test whether a real sky dipole would survive image-level selection, confidence cuts, edge-on triage, morphology-dependent misclassification, or depth-dependent classifier response; the A50 ≈ 0.75% and A95 ∈ (1.0%, 1.5%] claims are therefore estimator-level, not survey-level, sensitivities.

[MAJOR] Sec. VI A, “decisive rebuttal” using GZ1-only labels: the GZ1-only test has only N ≈ 46,000 and an explicitly much poorer statistical floor than the headline sample, so it cannot decisively rule out sub-percent pseudo-label-inherited large-scale structure; calling it decisive overstates what the test can support.

[MAJOR] Secs. IV D, Appendix D, harmonic residual attribution: the manuscript admits that the imaging/morphology forward model explains only about 52–54% of the ℓ = 1 residual amplitude and leaves roughly 47% open, yet still attributes the residual to survey systematics; this is plausible but not demonstrated at the standard required for dismissing a low-ℓ residual.

[MAJOR] Sec. IV D and Conclusions, monopole-mask leakage claim: reproducing 99.32% of the pre-MASTER pseudo-Cℓ power with an un-subtracted monopole is largely a demonstration of a known cut-sky leakage effect, while the post-MASTER residual is not similarly explained; the manuscript overuses the pre-MASTER result to support conclusions about the physically relevant residuals.

[MAJOR] Appendix D, block-bootstrap WLS “z ≈ −18” clean-dipole disfavor: this number depends on a particular template basis, bootstrap block scale, nuisance treatment, and hard-label catalog, and the manuscript itself says it is not a calibrated detection significance; it should not be presented as a primary exclusion-strength result without a full likelihood or coverage validation.

[MAJOR] Appendix D, WLS nuisance model: the design matrix is rank-deficient before dropping a leg template, several nuisance coefficients are individually meaningless, and the morphology/depth/confidence channels are not jointly marginalized in one formal model; the resulting “clean 1.7% dipole” comparison is not robust enough for the claimed amplitude-level exclusion.

[MAJOR] Sec. IV A and Appendix E, hard-argmax use after equivariant soft-probability averaging: the argument that flip equivariance prevents edge-on or ambiguous objects from biasing the dipole is made for soft probabilities, but the primary estimator uses hard CW/CCW argmax counts; the nonlinear argmax step can reintroduce spatially coherent tie-breaking biases and is not sufficiently bounded.

[MAJOR] Sec. V, comparison with Shamir: the manuscript repeatedly frames the result as strong tension with Shamir-class amplitudes while acknowledging that no matched-footprint Ganalyzer reanalysis is performed; the comparison is not a valid likelihood-level or estimator-level refutation and should be substantially weakened.

[MAJOR] Data Availability and reproducibility: many decisive results are referenced only as local artifact paths or a live main branch, with no frozen archival DOI, no immutable release, and no complete external reproducibility package; this is insufficient for a quantitative catalog/statistics paper making sub-percent claims.

[MINOR] Sec. I and Sec. VI C, physics framing: the manuscript alternates between parity, chirality, axial-vector isotropy breaking, and projected apparent arm winding; the distinction is eventually stated, but the title, abstract, and conclusions still invite overinterpretation as a direct parity-violation constraint.

[MINOR] Secs. III–VII, presentation: the manuscript is far too long, repetitive, and defensive for PRD; many caveats are repeated several times, while the actual statistical model remains fragmented across tables, appendices, and artifact names.

[MINOR] Tables V–VI and related text: field normalizations change between Ap, Ap/2, fCW − 0.5, monopole-subtracted, and non-monopole-subtracted maps; even when stated, this makes the numerical comparisons unnecessarily opaque and error-prone.

[MINOR] Appendix B, bias-hardening tests: several tests are weak sanity checks with loose thresholds, not evidence for sub-percent systematics control; they should not be described as a bias-hardening suite without quantitative power against the relevant failure modes.

(3) The central claim is not supported by the evidence presented: the manuscript supports at most a null result for a selected high-confidence catalog under an incomplete null model, while the full-sample excess, classifier-induced selection effects, and unresolved harmonic residual prevent the advertised survey-scale null/dipole-exclusion claim from being established.
