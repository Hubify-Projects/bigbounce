# INT API Review — P4 v1.0.234 — openai (gpt-5.5)
paper: P4  version: v1.0.234  model: gpt-5.5
modality: native-PDF (Files API input_file)
UTC: 2026-07-10T22:49:56.570387Z  |  latency: 96.0s  |  attempt: 1
usage: {"input_tokens": 62052, "input_tokens_details": {"cache_write_tokens": 0, "cached_tokens": 0}, "output_tokens": 2408, "output_tokens_details": {"reasoning_tokens": 1034}, "total_tokens": 64460}
PARSED VERDICT: REJECT

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: REJECT.

(2) ISSUES:

1. [MAJOR] Abstract/Secs. III–IV — The advertised “null chirality dipole” is not established for the full catalog: the unthresholded Catalog C field gives a reported real-space excess at \(z\simeq4.0\)–\(4.3\), while the null result appears only after imposing \(p_{\rm eq}>0.6\), which removes about 70% of classified spirals; the confidence-cut selection function is not modeled physically or propagated into all estimators.

2. [MAJOR] Secs. II B, IV A, VI B, Appendix B — The classifier validation is inadequate for sub-percent cosmological claims: the independent GZ1 chirality accuracy is only 69.91% with \(\kappa=0.40\), the softmax scores are strongly overconfident, and most training labels are CE-ResNet pseudo-labels; the paper’s injection tests operate on the already-classified hard-label field rather than through the image classifier, not-spiral triage, confidence cut, depth/seeing dependence, and spatially varying confusion matrix.

3. [MAJOR] Sec. IV C — The stated “pre-registration” of \(p_{\rm eq}>0.6\) by a repository commit is not an acceptable pre-analysis registration for a physics result; since the conclusion changes qualitatively between \(p_{\rm eq}\le0.5\) and \(p_{\rm eq}>0.6\), the cut must be justified by an independent validation criterion fixed before examining dipoles, or treated as a tuned analysis choice.

4. [MAJOR] Secs. III A, IV C–D, Tables I–V — The statistical framework is internally fragmented: pixel-permutation, per-galaxy shuffle, MASTER label-shuffle, depth-stratified nulls, monopole-only simulations, and block bootstrap significances are all used with different fields, masks, weights, and samples; repeatedly stating that the resulting \(\sigma\)’s are “not comparable” does not supply a coherent likelihood or a calibrated uncertainty on the claimed cosmological observable.

5. [MAJOR] Sec. IV D and Appendix D — The significant harmonic residuals are not convincingly disposed of: the manuscript reports \(+3.64\sigma\), \(+7.28\sigma\), and \(+7.93\sigma\) low-\(\ell\) residuals, then attributes them to systematics while admitting that about 47% of the residual amplitude is unexplained; this unresolved low-\(\ell\) structure is too central to be relegated to a diagnostic channel without a quantitative systematic model.

6. [MAJOR] Secs. IV D, VI B, VII — The argument that the unexplained harmonic residual is “below the real-space recovery threshold” is not a valid exclusion or safety argument: a detection-efficiency threshold is not an upper limit, and the mapping between a masked MASTER \(\ell=1\) amplitude and the real-space dipole amplitude is not demonstrated with a common covariance model.

7. [MAJOR] Sec. IV C and Appendix A — The MASTER/pseudo-\(C_\ell\) treatment is not publication-ready: the paper uses different field normalizations (\(A_p\) versus \(A_p/2\)), different masks, different mean-subtraction conventions, no consistent shot-noise treatment, and single-mode \(\ell=1\) deconvolution on a highly patchy footprint; the resulting harmonic significances cannot be trusted as quantitative systematics diagnostics without a unified analysis.

8. [MAJOR] Secs. V–VII — The comparison to Shamir’s claimed amplitudes is overstated: the manuscript repeatedly quotes “tension” and a \(z\simeq-7.6\) clean-dipole disfavor while also acknowledging that no matched Ganalyzer reanalysis, common selection, common likelihood, or common classifier has been performed; this is at most a qualitative amplitude comparison, not a robust literature exclusion.

9. [MAJOR] Secs. I, VI C — The connection to fundamental parity violation and PRD-relevant physics is speculative: the paper correctly notes that the \(\ell=1\) observable is parity-even, yet still discusses cosmic birefringence, Chern-Simons gravity, and primordial parity-violating sectors without deriving any transfer function from those theories to projected apparent spiral handedness.

10. [MAJOR] Secs. II–IV, Appendix E — The physical observable is insufficiently controlled: apparent CW/CCW winding is not a deprojected spin vector, edge-on contamination is large, trailing-arm assumptions are not validated per object, and morphology-, redshift-, dust-, and seeing-dependent selection effects are not modeled at the image level.

11. [MAJOR] Data Availability/throughout — Reproducibility is not acceptable for a real submission: the manuscript refers to many local artifact paths, future Zenodo deposits, missing immutable hashes, and a future-dated repository state; the paper cannot rely on non-archived scripts and artifacts as evidentiary support.

12. [MINOR] Whole manuscript — The presentation is far too long, repetitive, and internally defensive; many caveats are restated multiple times, obscuring the actual estimator, sample, null hypothesis, and result.

13. [MINOR] Tables/Figures — Several tables mix samples and conventions in ways that invite misinterpretation, e.g. \(N_{\rm catalog}\) versus \(N_{\rm map}\), \(A_p\) versus \(f_{\rm CW}-0.5\), canonical versus apodized masks, and 500-MC versus \(10^4\)-permutation results.

14. [MINOR] Sec. IV B — The global CW monopole is called a classifier artifact, but its origin is not demonstrated quantitatively; for a chirality catalog, a \(9.5\sigma\) global handedness imbalance is a serious calibration failure and should not be treated as harmless background.

15. [MINOR] Acknowledgments/Data Availability — The extensive AI-assisted methodology statement and missing archival identifiers are unusual for a PRD submission and should be replaced by a conventional reproducibility statement with fixed code, data, environment, and checksums.

(3) The central claim is only weakly supported in the narrow sense that one selected high-confidence hard-label estimator is consistent with null, but the broader cosmological null/exclusion claim is not supported by the present analysis.