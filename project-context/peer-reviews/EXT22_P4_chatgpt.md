# EXT22 P4 chatgpt — chat: https://chatgpt.com/c/6a3e68bf-4728-83e8-88da-d1faa56a5f7a

Referee Report — MNRAS / PRD / JCAP Style

1. Recommendation: MINOR REVISIONS
The revised manuscript is scientifically publishable after a small set of clarity and reproducibility fixes. I do not see a blocker requiring new analysis, nor a missing critical control that would justify major revisions. The paper is unusually transparent about estimator hierarchy, null definitions, harmonic-channel systematics, confidence-threshold dependence, and the distinction between primary cosmological estimators and diagnostic residuals.
The main result — a high-confidence real-space chirality dipole consistent with null, plus a quantitative demonstration that raw harmonic/hemisphere residuals are systematics-dominated — is adequately supported. The remaining issues are mostly about making the already-complicated statistical story harder to misread.

2. BLOCKERS
None.
I found no publication-blocking scientific defect, missing critical control, or non-reproducibility issue that requires substantial rework before acceptance.

3. MAJORS

M1. Clarify the estimator hierarchy even more aggressively in the abstract and conclusions
Location: Abstract; Sec. III A–B; Sec. IV C–D; Table I; Conclusions.
Issue: The manuscript already explains that the reported σ values come from distinct null procedures, but the abstract still contains many headline numbers in close succession: +0.41σ, z = 0.70, z ≈ −18, +3.64σ, ≈1.9σ Gaussian-equivalent, +7.28σ, +7.93σ, A50, A95, and harmonic completeness. A careful reader can follow this, but a casual reader could still misinterpret diagnostic harmonic residuals as competing detections.
Fix: Add one compact "reader key" near the end of the abstract or immediately after Table I:
Primary cosmological claim: HC real-space dipole null and WLS clean-dipole exclusion.
Diagnostic-only: MASTER, hemisphere, monopole-mask, and harmonic-completeness quantities.
No σ value should be compared across rows unless the same field, mask, weight, and null are used.

M2. Freeze the archival reproducibility handle before final acceptance
Location: Data Availability, p. 22.
Issue: The paper says the Zenodo DOI "will be deposited" at journal submission, while the code, catalog, and model are already linked through HuggingFace/GitHub. For MNRAS/PRD/JCAP reproducibility standards, the accepted version should have a frozen DOI or equivalent immutable archive.
Fix: Before publication, replace the future-tense Zenodo statement with the actual DOI and include the frozen release tag/commit for: catalog, model weights, code, primary dipole script, injection-recovery scripts, MASTER null artifacts, and WLS/bootstrap artifacts.

M3. State the provenance of the primary confidence cut in Methods, not only in Results
Location: Sec. III B; Sec. IV C; Fig. 6; Table I.
Issue: The primary result uses the HC threshold p_eq > 0.6, while the unthresholded sample shows a visible z ≈ 4.2–4.4 excess that is later attributed to the low-confidence tail.
Fix: In Sec. III B, add a short explicit sentence: "The p_eq > 0.6 HC sample is the declared primary production sample used by the generator script before interpreting the full-sample low-confidence-tail excess; the unthresholded and alternate-threshold results are reported only as diagnostic sensitivity/systematics sweeps."

M4. Tighten wording around "sub-percent sensitivity"
Location: Abstract; Sec. VI A; Conclusions.
Issue: The observed-space injection-recovery threshold A50 ≈ 0.75% is well documented, but Sec. VI A also notes that the conservative GZ1 accuracy floor maps this to a true-amplitude scale of order ∼1.88% under a symmetric-error approximation.
Fix: Wherever "sub-percent sensitivity" appears, specify "observed-space / catalog-space dipole amplitude" or "under the classifier-diluted observed Ap convention."

4. MINORS

m1. Reduce repeated caveat density in the abstract.
The abstract is scientifically careful but overloaded. Consider moving some repeated "not directly comparable" explanations into a boxed convention paragraph after the abstract.

m2. Make amplitude conventions visually unavoidable.
Location: Sec. IV C; Table V; Table VI; Fig. 4; Fig. 7; Conclusions.
Add a small convention box defining Ap = (NCW − NCCW)/(NCW + NCCW) = 2(fCW − 0.5) and state that injected full-amplitude A equals the Ap-dipole amplitude under the adopted injection convention.

m3. Table III / Table IV normalization warning should be repeated in nearby prose.
Location: Sec. IV D; Tables III–IV.
Add one sentence in the main text before Table IV saying the numerical Cl values in Tables III and IV are intentionally not comparable because they use different field definitions.

m4. Soften "all 8 tests pass" language.
Location: Appendix B; Table VIII.
Suggested wording: "All eight implementation/sanity checks meet their stated thresholds, with the scoped caveats for T1, T5, and T7 described above."

m5. Clarify the edge-on contamination estimate.
Location: Appendix E.
Move the caveat about the qualitative 10–15% dilution into the first paragraph of Appendix E so readers do not treat it as a final measured value.

m6. Keep p-value conventions uniform.
Location: Appendix C; Table III caption.
For finite Monte Carlo nulls, use either p=(k+1)/(N+1) everywhere or explicitly state when p ≤ 10^−4 means "zero exceedances in 10,000 draws."

m7. Data Availability should mention exact filtering for the primary sample.
Add a one-line reproducibility recipe for the primary sample: "Primary HC sample: Catalog C, equivariant spirals only, winning-class confidence p_eq > 0.6, canonical mask N_spiral(p) ≥ 10, with/without QC flip-identity flag as specified."

5. Strengths

Scientifically conservative conclusion. The paper does not overclaim a detection; it treats the real-space null and systematics-attributed harmonic residuals separately.

Large and useful public resource. The 8.47M-galaxy catalog, including 3.2M spiral classifications, model weights, probabilities, confidence scores, and reproducibility artifacts, is a valuable community product.

Strong bias-hardening methodology. The flip-equivariant TTA design is well motivated, and the raw-vs-equivariant comparison clearly demonstrates how small classifier biases can masquerade as cosmological chirality signals.

Good estimator hierarchy. The paper explicitly distinguishes primary cosmological estimators from secondary diagnostics and does not rely on the MASTER residual as an independent cosmological null.

Comprehensive systematics audit. The manuscript includes confidence sweeps, mask/threshold sweeps, depth-stratified nulls, leg-proxy tests, cross-spectra, WLS nuisance marginalization, and block-bootstrap covariance checks.

Careful comparison to prior work. The paper appropriately avoids claiming a formal likelihood-level exclusion of Shamir/Ganalyzer results without a matched-footprint reanalysis.

Transparent limitations. The manuscript openly discusses pseudo-label dependence on CE-ResNet, classifier overconfidence, GZ1 agreement limits, edge-on contamination, and unminted archival DOI status.

Final verdict
MINOR REVISIONS. The scientific result is credible and publication-worthy. The required changes are mainly to simplify interpretation, lock down archival reproducibility, and prevent misuse of non-comparable σ values.
