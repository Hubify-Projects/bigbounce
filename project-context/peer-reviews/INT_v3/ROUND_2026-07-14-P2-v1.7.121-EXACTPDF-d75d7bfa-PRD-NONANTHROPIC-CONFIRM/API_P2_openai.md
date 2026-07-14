# INT API Review — P2 v1.7.121 — openai (gpt-5.5)
paper: P2  version: v1.7.121  model: gpt-5.5
provenance: commit=36badcbdf498123413031aa0a9504127d48f2054  pdf=research/focused_paper_source_integration/02_full_draft.pdf  sha256=d75d7bfa2f7b8b9ba006137ed7b3da3f099475ba60f1db4886168750866f127e
packet: key=2dafae7c5fd20c8878c27ae99d32bfc9e19001e3594bf3092cdbc1d2766615c1  profile=PRD-RESEARCH
modality: native-PDF (Files API input_file)
UTC: 2026-07-14T19:06:17.404323Z  |  latency: 74.9s  |  attempt: 1
usage: {"input_tokens": 15917, "input_tokens_details": {"cache_write_tokens": 0, "cached_tokens": 0}, "output_tokens": 2773, "output_tokens_details": {"reasoning_tokens": 1552}, "total_tokens": 18690}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS.

(2) ISSUES:

1. [MAJOR] Appendix B / central correction claim: the manuscript’s main result is a correction of the published matter-bounce amplitude, but the analytic derivation is still not presented in a sufficiently self-contained way for a PRD article; the reader is asked to trust code and compressed tables rather than being shown the explicit mapping from the four cubic vertices to Eq. (3), including all normalization factors, ordered-sum multiplicities, and the conversion to the local \(f_{\rm NL}\) convention used later for LSS.

2. [MAJOR] Appendix B / Cai–Li discrepancy: the manuscript states that Cai et al.’s printed polynomial and Li et al.’s printed total polynomial both squeezed-reduce to \(-305/64\), while Li et al.’s closed-form formula gives \(-35/16\); this is a serious literature-level inconsistency, and the paper must more carefully document which equations are being compared, whether the definitions of \(A\), \(A_T\), \(B_{\rm NL}\), \(c_s\), and \(f_{\rm NL}\) are identical, and why Li et al.’s Eq. (5.1) should be considered an independent confirmation rather than another convention-dependent expression.

3. [MAJOR] Secs. III–IV / SPHEREx mapping: the quoted \(2.61\)–\(2.63\sigma\) mapping from the published Heinrich et al. scalar uncertainty \(\sigma(f_{\rm NL}^{\rm local})\simeq0.7\) using a flat-grid recovery factor \(r\) is not a statistically controlled forecast; a scalar published error bar cannot generally be reweighted into a different primordial shape without the survey covariance, triangle weights, nuisance model, and estimator response, so these numbers should either be removed from the abstract/conclusion or demoted much more strongly to a non-forecast illustrative calculation.

4. [MAJOR] Secs. II B–II C / bounce transmission: the observational interpretation depends on faithful cubic-order transfer through the nonsingular bounce, but only linear transfer is cited as established; because nonlinear transfer can in principle change the bispectrum amplitude and shape, the paper must not present the late-time \(f_{\rm NL}=-35/16\) prediction as a testable model prediction without either performing the third-order bounce calculation or making the conditional nature dominant in the title, abstract, and conclusions.

5. [MAJOR] Secs. III A and VII / bias-response treatment: Eq. (5) assumes the standard universal-mass-function response \(\Delta b\propto 2 f_{\rm NL}(b_1-1)\delta_c/M\), while the later nuisance ladder treats \(b_\phi\) as fixed, prior-constrained, or free; the parameterization connecting Eq. (5) to \(b_\phi\), the degeneracy structure with \(f_{\rm NL}\), and the origin of the \(0.42\sigma\) free-\(b_\phi\) residual significance must be explicitly derived.

6. [MAJOR] Secs. IV and VII / surrogate covariance: the in-house Fisher calculations omit non-Gaussian covariance, Fingers-of-God damping, higher-order bias terms, photometric-redshift outliers, and the external per-triangle covariance, yet quote significances to two decimal places; either provide a reproducible validation against Heinrich et al.’s actual forecast machinery or round and reframe these results as qualitative nuisance-sensitivity diagnostics only.

7. [MINOR] Eq. (1)–Eq. (4) / notation: the notation \(P\) for the degree-nine polynomial is potentially confusing because \(P_\zeta\) and \(P_\Phi\) are also discussed; the manuscript should use a distinct symbol, e.g. \({\cal P}_9\), throughout.

8. [MINOR] Appendix B / Table IV: the table says the expressions are evaluated at \(\epsilon=3/2\), but the entries still contain explicit \(\epsilon\); this should be corrected by either displaying the general-\(\epsilon\) expressions or the actually substituted rational coefficients.

9. [MINOR] Appendix B / sum conventions: the distinction between ordered six-term sums and distinct three-term \((5,2,2)\) sums is crucial and should be defined once in a formal notation block before Eq. (3), then used consistently in Eq. (B4) and Tables IV–V.

10. [MINOR] Sec. III / \(f_{\rm NL}\) convention: the LSS scale-dependent-bias formula uses the standard potential convention for local PNG; the paper should explicitly show that the matter-bounce \(B_{\rm NL}\) convention used in Cai/Li maps without an extra \(3/5\), sign, or growth-factor conversion into the \(f_{\rm NL}\) appearing in Eq. (5).

11. [MINOR] Data and code availability: for a paper whose main claim is an exact algebraic correction of the literature, the code and symbolic artifacts should be archived with an immutable DOI at submission rather than deferred to “camera-ready packaging.”

12. [MINOR] Presentation / scope: the title and abstract currently give substantial prominence to SPHEREx mapping, although the robust result is the contraction-phase amplitude; the manuscript would be clearer and more defensible if the observational material were shortened or moved to an explicitly optional phenomenology section.

(3) The central algebraic claim that the contraction-phase four-vertex sum gives \(f_{\rm NL}^{\rm local}=-35/16\) appears plausible and partially supported, but it is not yet documented self-containedly enough, and the observational SPHEREx implications are not supported at forecast level.