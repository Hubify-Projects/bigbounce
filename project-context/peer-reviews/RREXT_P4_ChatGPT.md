# RREXT P4 ChatGPT
VERDICT: MINOR REVISIONS

Provider: ChatGPT (default)
PDF: RREXT_P4.pdf (md5: b585cc9c3021e03a8293c3f6fe2ed490)
Chat: https://chatgpt.com/c/6a4437ea-764c-83e8-beae-8607412fd989
Harvested: 2026-06-30
RCEXT baseline: MAJOR REVISIONS (IMPROVED to MINOR REVISIONS)

Thought for 11s1. Recommendation: MINOR REVISIONS
This is a strong, unusually careful observational/systematics paper. The central scientific claim is appropriately conservative: the high-confidence real-space chirality dipole is null, while harmonic-channel low-ℓ residuals are treated as diagnostics of survey/classifier systematics rather than cosmological detections. The paper’s value is not merely the catalog scale, but the explicit demonstration that small classifier monopoles plus a patchy footprint can mimic dipole-like harmonic power. That is publishable in a top journal, provided the remaining interpretive overstatements and clarity issues are tightened. RREXT_P4
2. BLOCKERS
None.
I do not see a fatal flaw requiring rejection or a complete reanalysis before the paper can be considered. The primary null result is not based on the systematics-contaminated MASTER residuals; it is anchored on the high-confidence real-space estimator and a template-fit comparison. The authors are also appropriately explicit that the pseudo-Cℓ residuals are systematics-attributed diagnostics, not cosmological detections.
3. MAJORS
Major 1 — The pseudo-label dependence is still the main vulnerability.
The paper states that 66.5% of training labels derive from CE-ResNet predictions, and that the independent GZ1 chirality accuracy is only 69.91% with κ = 0.40. This is honestly disclosed, but it remains the most important limitation. The paper argues that inherited survey-correlated structure would be exposed by template/cross-spectrum diagnostics, yet the fully independent GZ1-only retraining/full-catalog re-inference is deferred.
This does not block publication, but the conclusion should be softened wherever it implies that pseudo-label inheritance is fully bounded. A top-journal version should phrase the result as: “under this bias-hardened ViT/TTA catalog and the available external-template diagnostics,” rather than as a fully independent galaxy-chirality measurement. The deferred GZ1-only retrain should be elevated from “future work” to an explicitly named validation needed for complete pseudo-label independence.
Major 2 — The multiple σ conventions remain cognitively hazardous.
The manuscript repeatedly warns that the σ values are not comparable, but the abstract and conclusions still contain many numerical significances in close succession: +0.41σ, z = 0.58, +3.64σ, +7.28σ, +7.93σ, z ≈ −18, harmonic z ≈ 68–218, etc. The paper is technically clear, but a reader could still mistakenly infer an internal contradiction or a hidden detection.
I recommend a stricter rewrite of the abstract and conclusions: lead with only the two primary results, then put all harmonic residual σ values in one short diagnostic sentence. The Table I decision tree is excellent; the abstract should mirror it even more aggressively.
Major 3 — The “exclusion” language for the Shamir-scale signal is sometimes too strong.
The paper is careful to say that a matched Ganalyzer reanalysis is needed for a likelihood-level exclusion. However, phrases such as “disfavors a clean cosmological dipole at z ≈ −18” and “inconsistent in amplitude by a factor of ∼4–9” can read stronger than the methodological comparison supports, because the classifier, selection function, chirality definition, and nuisance model differ from the prior literature.
Suggested revision: consistently call this an amplitude-level tension under the present pipeline, not an exclusion of Shamir’s estimator. The current text often says this, but it should be enforced everywhere, especially in the abstract, conclusions, and comparison section.
Major 4 — The edge-on contamination argument is overconfident.
The appendix states that equivariance excludes directional bias from edge-on leakage because flip-symmetric morphologies should have zero expected CW−CCW asymmetry. This is plausible in expectation for idealized flip-symmetric objects, but real edge-on systems can correlate with depth, PSF, inclination-dependent detectability, dust lanes, and hard-argmax selection boundaries. The stated 65.7% edge-on CW/CCW assignment rate is large enough that the argument should be softened.
The paper should either provide the promised axis-ratio cross-match or avoid saying directional bias is “excluded.” A safer phrasing is that equivariant TTA strongly suppresses the leading flip-asymmetric edge-on bias, while the residual effect is expected mainly to dilute sensitivity and should be empirically checked with b/a and morphology templates.
Major 5 — The low-confidence full-sample excess deserves a clearer scientific disposition.
The unthresholded sample shows a real-space dipole excess at z ≈ 4.2–4.4, collapsing to null above peq > 0.6. The paper attributes this to the low-confidence tail and handles it as a diagnostic. That is reasonable, but because the low-confidence result is numerically strong, the reader needs a more explicit “why this is not the primary sample” explanation in the main text.
The authors should add a compact paragraph stating that peq > 0.6 was fixed as the production high-confidence selection before the dipole result, that peq is a rank score not a calibrated probability, and that the full confidence sweep is the guard against threshold cherry-picking. Much of this is already present, but it should be consolidated in one highly visible place.
4. MINORS
Abstract is too overloaded. It currently reads more like a rebuttal dossier than an abstract. It should be shortened and structured around: catalog, primary real-space null, leakage demonstration, harmonic residual attribution, falsification threshold.
Data availability should distinguish live branch vs immutable archive more cleanly. The statement that the live main branch reflects the current version is useful, but the citable scientific result should depend only on the frozen tag/DOI. Since Zenodo DOI deferral is normal pre-submission, this is not a defect, but the final version must remove any ambiguity.
The globa
