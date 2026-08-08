chat: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a50096c-33d8-83e8-ab27-e30140dd5581
reviewer: ChatGPT (Pro Extended) | paper: P5 v0.1.110 (40pp) | date: 2026-07-09 | round: CV
baseline (CA): ACCEPT (literal '(1) VERDICT: ACCEPT'; 6 minors)
verdict (from raw): MAJOR REVISIONS. REOPENED from CA ACCEPT. 4 driver items: (i) chirality-label bound calibration, (ii) make DESIVAST in-footprint control the PRIMARY result, (iii) systematic-envelope accounting, (iv) immutable reproducibility artifacts. 'central null result promising but current form overstates precision/physical interpretation.'
---RAW---
Worked for 9m 11sReferee report — MNRAS style
Manuscript: Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Void Null Test on 56,981 DESI DR1 Spirals, Paper 5 v0.1.110, dated 9 July 2026. cv_P5
Recommendation: MAJOR REVISIONS
The paper reports a potentially useful null test: within the author’s DESI × chirality matched catalogue, DESIVAST void and non-void spirals have statistically indistinguishable classifier-labelled CW fractions. The main numerical null appears internally stable across several DESIVAST definitions, and the manuscript is unusually transparent about post-hoc path selection, redshift-space scope, T-Web failure modes, and reproducibility artifacts.
However, the current manuscript is not yet publishable in MNRAS/PRD/JCAP form. The central claim is stronger than the analysis justifies in three ways: the quoted sub-percent “chirality” bound does not properly propagate chirality-label misclassification and possible environment-dependent classifier error; the primary DESIVAST control sample and void-membership definition are not yet cleanly formulated as the actual survey-volume estimand; and the quoted 0.5–0.6 percentage-point bound is internally inconsistent with the paper’s own geometry/membership systematic statements. These are fixable, but they are load-bearing.
Summary assessment
The most valuable result is the DESIVAST-anchored null: the paper reports 56,981 DESIVAST VoidFinder void spirals from 678,945 low-redshift matched spirals, with fCWvoid=0.4964f_{\rm CW}^{\rm void}=0.4964fCWvoid​=0.4964, fCWnonvoid=0.4971f_{\rm CW}^{\rm nonvoid}=0.4971fCWnonvoid​=0.4971, and ΔfCW=+0.0007\Delta f_{\rm CW}=+0.0007ΔfCW​=+0.0007, statistically indistinguishable from zero. cv_P5 The manuscript further reports that all five DESIVAST void definitions remain below the Bonferroni-5 threshold, including the two catalog-native GALZONE checks. cv_P5
The T-Web material is much weaker and should remain secondary. The paper itself shows that the T-Web void bin is only n=428n=428n=428, that its low-redshift overlap with DESIVAST is only six objects, and that the T-Web void label is not a reliable low-z void label for this application. cv_P5 cv_P5 This does not invalidate the DESIVAST null, but it means the paper should be reorganised around DESIVAST and should stop advertising the T-Web pathway as anything more than a diagnostic stress test.
BLOCKERS — must fix before publication
B1. Section XIII / Appendix A: the quoted sub-percent bound is not corrected for chirality-label dilution or environment-dependent classifier error.
Location: Appendix A, “Independent accuracy floor”; Section XIII limitation on Paper IV dependence; Section XII-B / Conclusions where the 0.5–0.6 pp “handedness split” bound is interpreted for model-builders. The classifier accuracy against GZ1 spiral chirality labels is only 69.91% with κ=0.40\kappa=0.40κ=0.40, and the manuscript says label dilution is folded into sensitivity floors, but the main DESIVAST bound is still quoted as a 0.5–0.6 pp bound on spiral chirality itself. cv_P5 The manuscript also admits that “a systematic environment-dependent re-labeling by a future classifier is not excluded” and that no environment-stratified human-label confusion matrix is available. cv_P5
Why this blocks publication: A global monopole cancels in a void/non-void difference, but classification error does not cancel unless the error matrix is identical in both environments after conditioning on redshift, size, surface brightness, imaging leg, confidence, and morphology. With a symmetric binary accuracy a≃0.699a\simeq0.699a≃0.699, an observed true-signal contrast would be attenuated by roughly 2a−1≃0.402a-1\simeq0.402a−1≃0.40. Thus an observed 0.5–0.6 pp classifier-label bound corresponds, even in the optimistic symmetric-error case, to a true-chirality bound closer to ∼1.3\sim1.3∼1.3–1.5 pp before adding environment-dependent error. If the error matrix varies with environment, the bound may be weaker or biased.
Proposed fix: Either:
Recast the headline everywhere as a bound on the classifier-labelled CW fraction, not on physical spiral chirality; or
Provide a deattenuated bound using the Paper IV confusion matrix, with an explicit uncertainty model; and
Add an environment-stratified validation using GZ1/human labels or an equivalent high-purity subset. At minimum, report void/non-void confusion matrices or CW-fraction residuals stratified by DESIVAST membership, redshift, magnitude, angular size, imaging leg, pmax⁡p_{\max}pmax​, and morphology. The human-label subset may be small, but it is essential for bounding differential classifier error.
B2. Section VIII-B/E and Table IX/XI: the primary non-void control sample is not consistently restricted to the DESIVAST survey/mask volume.
Location: Section VIII-B and Table IX define the primary non-void sample as all z≤0.24z\le0.24z≤0.24 matched spirals outside any DESIVAST hole, giving nnonvoid=621,964n_{\rm nonvoid}=621,964nnonvoid​=621,964. cv_P5 Section VIII-E later states that the non-void control is “not required to lie outside the survey mask,” then performs a footprint-restricted retabulation in which the non-void sample drops to 253,276 and the contrast changes to ΔfCW=+0.0018\Delta f_{\rm CW}=+0.0018ΔfCW​=+0.0018. cv_P5
Why this blocks publication: For a void/non-void environmental contrast, the control must be drawn from the same usable survey volume and selection function as the void sample. A non-void sample that includes galaxies outside the DESIVAST usable footprint is not the clean DESIVAST non-void population. The fact that the footprint-restricted result remains null is reassuring, but it should be the primary result, not a supporting afterthought.
Proposed fix: Redefine the primary DESIVAST estimand as:
ΔfCW=fCW(in DESIVAST usable volume, not void)−fCW(in DESIVAST usable volume, void).\Delta f_{\rm CW}= f_{\rm CW}({\rm in\ DESIVAST\ usable\ volume,\ not\ void})
- f_{\rm CW}({\rm in\ DESIVAST\ usable\ volume,\ void}).ΔfCW​=fCW​(in DESIVAST usable volume, not void)−fCW​(in DESIVAST usable volume, void).
Apply this consistently to VoidFinder, V2-REVOLVER, V2-VIDE, and the catalog-native GALZONE definitions. Retabulate Table XI with the footprint/mask-restricted complements as the primary contrasts. The current all-z≤0.24z\le0.24z≤0.24-outside-hole version can remain as a sensitivity check.
B3. Abstract / Section VIII / Section XII-B: the 0.5–0.6 pp systematic envelope is internally inconsistent.
Location: The reader’s guide states that the next-leading systematics include “geometry choice ≤ 0.6 pp” and that each is sub-dominant to the ±0.34–0.37 pp membership term. cv_P5 Section VIII-E states that switching from any-hole to maximal-sphere membership shifts ΔfCW\Delta f_{\rm CW}ΔfCW​ from +0.06 pp to −0.54 pp, i.e. about 0.6 pp. cv_P5 Section VIII-B then states that folding the ±0.34–0.37 pp membership systematic with counting widens the 2σ bound from about 0.44 pp to about 0.55–0.60 pp. cv_P5
Why this blocks publication: A 0.6 pp geometry shift is not sub-dominant to 0.34–0.37 pp; it is comparable to, or larger than, the entire quoted effective 2σ envelope. The manuscript cannot simultaneously claim that geometry is ≤0.6 pp, that this is sub-dominant to 0.34–0.37 pp, and that the final robust bound is 0.5–0.6 pp.
Proposed fix: Provide a single systematic-error table for the primary DESIVAST estimand with clear units and sign conventions. Separate:
counting-only confidence interval;
void-membership perturbation uncertainty;
any-hole versus maximal-sphere geometry uncertainty;
sphere-PIS versus catalog-native GALZONE differences;
footprint/mask restriction;
classifier-confidence cut;
match-radius variation;
chirality-label dilution.
Then quote either a conservative envelope such as the maximum absolute excursion across all accepted definitions, or a justified quadrature combination if the terms are demonstrably independent. If geometry contributes 0.6 pp, the final bound should be wider than 0.6 pp unless the authors explicitly define the bound as a family-wise null rather than an exclusion interval.
B4. Section V-B / Conclusions: the post-hoc primary-path language is still too strong for an exclusion bound.
Location: Section V-B states that no preregistered plan existed and that the primary classifier choice was post-hoc. cv_P5 The same section says that because all reported tests are null, multiplicity “works against finding a spurious signal” and “can only weaken an already-null result.” cv_P5
Why this blocks publication: That statement is true for discovery claims but not for post-hoc upper bounds. Selecting among several correlated definitions can select the tightest or most reassuring null bound. The manuscript acknowledges this in places, but still repeatedly quotes a headline 0.5–0.6 pp constraint as though it were a confirmatory primary result.
Proposed fix: Replace “primary” with “designated primary for reporting” or “exploratory primary” unless there is a timestamped analysis plan. State in the abstract and conclusions that the DR1 result is exploratory/post-hoc and that the strictly quotable result is the family-wise DESIVAST null, not a preregistered exclusion. Remove or rewrite the claim that look-elsewhere correction can only weaken an already-null result; for upper limits, it can change the strength of the claimed bound.
B5. Appendix D/E: the reproducibility claim is not complete until immutable artifacts and exact external dependency versions are available.
Location: Appendix D says all numbers regenerate from tag v0.1.110-2026-07-09 and that a DOI-minted archival snapshot accompanies journal submission, but also says the Zenodo DOI is pending and will be inserted later. cv_P5 The analysis is explicitly AI-orchestrated and relies heavily on linked artifacts A1–A30. cv_P5
Why this blocks publication: This paper’s evidentiary burden rests unusually heavily on code and artifacts. A mutable GitHub repository is not sufficient for refereeing a 40-page catalogue/statistics analysis whose primary numbers are mostly artifact-derived.
Proposed fix: Before acceptance, provide a Zenodo/Dataverse DOI with immutable source, configs, exact artifact files, hashes, environment lockfile, and a minimal reproduction script that regenerates the primary DESIVAST tables from public DESI/DESIVAST inputs. The paper should include the DOI, not “pending.” The main text should also state which results can be reproduced without private or not-yet-public companion-paper artifacts.
MAJORS — should fix
M1. Section VIII-B / XI: the primary DESIVAST contrast needs covariate-adjusted and matched-control versions.
Location: The paper gives detailed covariate regression for the T-Web secondary path, but the DESIVAST primary path mainly reports target-program splits and global systematics. cv_P5
Issue: DESIVAST void membership can correlate with redshift, angular size, brightness, morphology, imaging leg, classifier confidence, and survey footprint. Since the classifier has known imaging-leg and target-program residuals, a raw void/non-void contrast is not sufficient.
Proposed fix: Add a primary DESIVAST logistic regression or inverse-propensity-weighted analysis:
CW∼void+z+mr+R50+pmax⁡+leg+morphology+sky region,{\rm CW}\sim {\rm void}+z+m_r+R_{50}+p_{\max}+{\rm leg}+{\rm morphology}+{\rm sky\ region},CW∼void+z+mr​+R50​+pmax​+leg+morphology+sky region,
and/or construct a matched non-void control sample matched in redshift, magnitude, size, leg, and confidence. Quote the adjusted void coefficient and uncertainty as a primary robustness result.
M2. Section VIII-C/D: the “three-algorithm” claim mixes sphere-PIS and catalog-native definitions too loosely.
Location: Table XI is based on sphere-PIS effective-radius membership for all three algorithms, while Section VIII-D separately reports catalog-native GALZONE definitions for the V2 algorithms. cv_P5
Issue: The headline “three-algorithm DESIVAST” result should distinguish official catalog-native membership from the authors’ sphere approximation. The current presentation risks making a constructed sphere-PIS test appear equivalent to DESIVAST-native galaxy membership.
Proposed fix: Split the DESIVAST results into two tables: “author-constructed sphere-PIS approximations” and “catalog-native memberships.” Make the official/native rows primary wherever available. Clarify that VoidFinder any-hole membership is an approximation unless DESIVAST defines it as an official galaxy membership.
M3. Section XIII / Conclusions: fixed-redshift-space scope is correctly disclosed but still not reflected consistently in the claims.
Location: The conclusions state that all environment classes are assigned in DESI DR1 redshift coordinates and that the 0.5–0.6 pp bound is not a pure real-space constraint. cv_P5 Section VIII also describes the DESIVAST RSD test as fixed-void-geometry rather than a full reconstructed-position rerun. cv_P5
Issue: The manuscript sometimes still speaks as though it constrains “environment dependence” generally. It constrains redshift-space DESIVAST membership and classifier-labelled chirality, not real-space environment dependence.
Proposed fix: In title, abstract, and conclusions, use “redshift-space DESIVAST void/non-void” or “fixed-redshift-space void membership.” Avoid generic “environment dependence” unless immediately qualified.
M4. Section IX-A: the T-Web pathway is sufficiently compromised that it should be moved after DESIVAST or largely to an appendix.
Location: The paper itself calls T-Web “failed/diagnostic secondary,” with n=428n=428n=428 void galaxies, a +8–18 pp void-fraction discrepancy, and a randoms-weighted rebuild that reassigns about 73% of T-Web void galaxies. cv_P5 It also reports that the randoms-weighted rebuild collapses the void volume fraction by a factor of about 23. cv_P5
Issue: The narrative currently spends many pages on a classifier that the paper later says is not load-bearing. This distracts from the real DESIVAST result and makes the “headline” hard to identify.
Proposed fix: Reorder the paper: Data → chirality label validation → DESIVAST primary → DESIVAST robustness → T-Web/Tempel/ASTRA diagnostics. Move most of the T-Web implementation and selection-correction details to an appendix.
M5. Section VIII-A: the 0/6 T-Web–DESIVAST comparison is overinterpreted.
Location: Section VIII-A reports that 0/6 low-z T-Web void spirals fall in DESIVAST holes and then discusses “0% concordance,” while also correctly noting that the one-sided 95% upper bound is 39%. cv_P5
Issue: The result is useful as an illustration but too small to “quantify” purity in a meaningful way.
Proposed fix: Keep it as an anecdotal sanity check only. Remove “quantifies the T-Web void-class purity” or replace with “illustrates the likely mismatch but is not statistically constraining.”
M6. Section XII-B / Appendix B: the model-building discussion is peripheral and should be shortened.
Location: Section XII-B says no published bounce or inflation model predicts this signature and describes the bound as something future parity-violating models must respect. cv_P5 Appendix B introduces a toy EFT mapping.
Issue: The empirical paper is strongest as a catalogue-level null test. The toy EFT mapping is speculative and not needed for MNRAS unless the paper is targeted to a theory journal and the mapping is made rigorous.
Proposed fix: Move Appendix B to supplementary material or reduce it to one paragraph. Keep the main text focused on the observational null.
M7. Section XI: the structured bright/dark residual deserves a clearer quantitative bound in the DESIVAST primary sample.
Location: Table XVI reports BGS bright fCW=0.4970f_{\rm CW}=0.4970fCW​=0.4970 versus dark fCW=0.5051f_{\rm CW}=0.5051fCW​=0.5051, a 0.81 pp difference at about 1.95σ, and the paper states this does not affect the DESIVAST primary result. cv_P5
Issue: Because the claimed DESIVAST bound is of order 0.5–0.6 pp, a 0.81 pp program-conditioned residual is not negligible in scale, even if the DESIVAST sample is mostly bright.
Proposed fix: Quantitatively propagate the maximum possible leakage of the bright/dark residual into the DESIVAST void/non-void contrast using the actual program fractions in void and control samples. Report the resulting bound in pp.
M8. Section V / Tables: p-values and “σ” metrics mix one-sample, two-sample, monopole-subtracted, and look-elsewhere quantities.
Location: Tables IV, V, VIII, IX, XI, XIII and the abstract use σfrom half\sigma_{\rm from\ half}σfrom half​, zΔz_\DeltazΔ​, σpred\sigma_{\rm pred}σpred​, σvs monopole\sigma_{\rm vs\,monopole}σvsmonopole​, and empirical p-values.
Issue: The distinctions are mostly defined, but the paper is very difficult to audit because the same visual language is used for different statistics.
Proposed fix: Add a compact “statistics glossary” table early in Section V with columns: statistic, null hypothesis, denominator, one-sample/two-sample, where used, and whether it enters the headline. Use zΔz_\DeltazΔ​ only for the primary DESIVAST contrast.
MINORS — polish
m1. Title / abstract: simplify and reduce the “defensive abstract.”
The abstract is too long and reads like a response to referee concerns. Move most caveats to a “Scope and limitations” subsection. Keep the abstract to: data, primary DESIVAST estimand, null result, systematics envelope, and redshift-space caveat.
m2. Section I: avoid “headline” labels for secondary T-Web results.
The paper says the primary result is DESIVAST, but Section VI-A is still labelled “Cosmic-web environment (headline).” This should be renamed “Secondary T-Web diagnostic.”
m3. Section IV: the T-Web/V-Web nomenclature explanation is useful but too long.
Keep the footnote distinguishing T-Web from V-Web, but move implementation details and backward-compatible filenames to the reproducibility appendix.
m4. Figures 6 and 8: check figure/caption consistency.
The rendered page for Fig. 6 includes a top panel labelled “Maximal voids per pixel,” while the caption describes a chirality HEALPix scan. Fig. 8 later uses a similar maximal-void/chirality two-panel layout. Check whether Fig. 6 has the wrong top panel or an incomplete caption.
m5. Tables IX/XI: add units explicitly.
When reporting ΔfCW\Delta f_{\rm CW}ΔfCW​, use both fractional units and percentage points, e.g. +0.0007=+0.07+0.0007=+0.07+0.0007=+0.07 pp. Several sections switch between the two.
m6. Section VIII-E: “0 maximal voids per pixel” is not a mask.
The paper already cautions that this is a proxy, not a formal mask. Keep that statement, but remove language implying it directly identifies outside-coverage regions unless an official DESIVAST angular mask is used.
m7. Appendix E: typo in reference/artifact numbering.
The references section uses [1]–[14], while artifact IDs use [A1]–[A30]. On page 39/40 the transition from artifact text to references is visually confusing. Separate “References” and “Artifact map” more clearly.
m8. MNRAS style: reduce first-person process language.
Phrases such as “unmissable,” “cleanest,” “failed/diagnostic,” “honestly-quotable,” and “referee-facing” are helpful internally but too informal for journal prose. Use neutral language.
m9. MNRAS style: shorten AI-methodology language.
The AI disclosure is appropriate, but naming multiple commercial models in the acknowledgements is unnecessary for the scientific record unless required by journal policy. The important part is author responsibility and reproducibility.
m10. References [11] and [12].
I did not flag the 2604 arXiv references as invalid; they resolve to 2026 arXiv records for a DESI DR1 T-Web study and an ASTRA DESI EDR probabilistic environment catalogue, respectively. arXiv+1
Strengths
The DESIVAST primary null is scientifically useful: it uses a public DESI DR1 BGS void catalogue, a much larger void sample than the T-Web void bin, and multiple DESIVAST void definitions. cv_P5
The manuscript is unusually transparent about post-hoc analysis-path selection, multiplicity, redshift-space limitations, and the fact that the T-Web path is secondary. cv_P5
The authors provide many robustness checks: exact versus k=20k=20k=20 membership, maximal-sphere comparison, catalog-native GALZONE checks, footprint restriction, target-program splits, confidence cuts, match-radius tests, and grid/smoothing sweeps. cv_P5 cv_P5
The paper does not overclaim a positive detection; it consistently treats the result as a null/non-detection.
The data and code availability plan is strong in intent, with per-output provenance, deterministic seed, and artifact mapping; once converted into an immutable DOI archive, this will be a significant strength. cv_P5
Bottom line
I recommend major revisions. I would likely support publication after the authors (i) calibrate or explicitly limit the chirality-label bound, (ii) make the DESIVAST in-footprint control sample the primary result, (iii) repair the systematic-envelope accounting, and (iv) provide immutable reproducibility artifacts. The central null result is promising, but the current form overstates the precision and physical interpretation of the bound.