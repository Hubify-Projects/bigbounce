VERDICT: MAJOR REVISIONS. 

r9_P4

Overall assessment

This is an ambitious and technically sophisticated observational analysis built around an exceptionally large chirality catalog (~8.5 million DESI galaxies, 3.2 million classified spirals) with extensive methodological development, multiple null tests, systematic investigations, injection–recovery studies, and public-release plans. The central observational result—a null real-space dipole—is clearly stated and generally supported by the primary estimator.

However, from the perspective of Physical Review D, several aspects of the statistical methodology, presentation, and interpretation remain insufficiently resolved before publication. The manuscript is strongest as a careful null measurement and catalog paper; it is weakest where it attempts to reconcile numerous secondary diagnostics that remain significantly non-null.

Major issues
1. The paper relies on a post hoc estimator hierarchy to resolve internally inconsistent diagnostics.

The manuscript explicitly designates the real-space estimator as "primary" while classifying the harmonic-channel measurements (+3.6σ to +7.9σ) as "diagnostic only." Although this is stated repeatedly, the justification is largely conceptual rather than statistical.

A referee would expect a more formal demonstration

--- [continuation] ---

VERDICT: major-revisions

CENTRAL CLAIM: The headline result is that the high-confidence DESI chirality catalog shows no real-space cosmological chirality dipole, and that claim is broadly supported, but the manuscript still overstates the strength of exclusion while leaving non-primary harmonic residuals and classifier/systematics modeling insufficiently formalized. 

r9_P4

ISSUES:

The estimator hierarchy in Sec. III B / Tables I–III is not yet rigorous enough: the paper declares the real-space dipole primary and harmonic residuals diagnostic, but the choice needs a clearer pre-analysis rationale rather than repeated assertion.

Sec. IV C–D reports large non-primary harmonic residuals (+3.64, +7.28, +7.93σ) while the primary estimator is +0.41σ; the manuscript explains this as systematics, but the statistical relationship between these observables is not formalized enough.

The block-bootstrap WLS “z≈−18” exclusion in Sec. III B, Sec. IV D, and Appendix D is too rhetorically strong; it should be framed as a model-dependent template-disfavor statistic, not as near-decisive exclusion significance.

The classifier validation is a major weakness: Appendix B reports only 69.91% independent GZ1 chirality accuracy and strong overconfidence, so the paper needs a clearer uncertainty propagation from label noise into all headline amplitude limits.

The CE-ResNet pseudo-label dependence is disclosed in Sec. II and VI A, and the GZ1-only test is useful, but the GZ1-only sample is much smaller and not sensitive to the sub-percent regime, so it cannot fully discharge pseudo-label inheritance concerns.

The confidence cut peq > 0.6 is plausibly justified in Sec. IV C, but “pre-registration” based on a committed script is not equivalent to a blinded analysis plan; soften that language.

The unthresholded Catalog C real-space excess at z≈4.2–4.4 in Sec. IV C deserves more compact, quantitative systematics modeling, not only attribution to the low-confidence tail.

Sec. IV D says the imaging/morphology forward model explains only ~52–54% of the ℓ=1 residual and leaves ~47% open; that disclosure is adequate, but the abstract and conclusions should not sound more closed than the actual residual budget.

Several σ values use distinct nulls and are repeatedly warned as non-comparable, but the paper still places them side-by-side in ways likely to confuse readers; reduce or reorganize these diagnostics.

The injection–recovery thresholds in Sec. VI B are important, but A50 and A95 are based on coarse grids and limited injections; the falsification criterion should reflect that uncertainty more conservatively.

The comparison to Shamir in Sec. V and VII is mostly fair because it avoids claiming a formal Ganalyzer exclusion, but “7–18× tension” should be made visibly pipeline-dependent wherever stated.

Appendix D’s nuisance-template regression has rank-deficiency in the leg templates; the manuscript handles this technically, but the main text should not rely on the raw WLS table without a simpler explanation of what is actually identifiable.

The manuscript is overlong and repetitive for PRD; much of the repeated caveat language should be consolidated into one clean statistical framework.

Figures 4, 7, 8, and 9 are useful, but the captions are overloaded with interpretation; separate visual description from inference.

The Data Availability section promises public artifacts and future DOI/tagging; before acceptance the exact frozen repository, catalog version, scripts, and checksums must be archived and cited.

The claim that the catalog is the “largest chirality-labeled galaxy catalog to date” appears plausible, but should be phrased with a citation-qualified “to our knowledge” consistently.

The parity-violation discussion in Sec. VI C is appropriately cautious, but PRD readers will expect the parity-even versus parity-odd distinction to be stated earlier and more cleanly.

Minor: notation alternates among fCW deviation, Ap, dipole amplitude A, and percent units; this needs a single upfront conversion table.

FINAL VERDICT: major-revisions.

--- MANIFEST ---
paper: P4 (v1.0.224) | reviewer: ChatGPT (GPT-5) | modality: native PDF upload 34MB
chat: https://chatgpt.com/c/6a4f4fd1-0e70-83e8-a7b9-7a2de02349f0
verdict: major-revisions | date: 2026-07-09 | note: continued once for full issues
