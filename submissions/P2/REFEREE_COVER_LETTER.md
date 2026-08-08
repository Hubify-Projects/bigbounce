# Cover Letter — Paper 2

**Title:** Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook
**Source:** `research/focused_paper_source_integration/02_full_draft.tex` (v1.7.98, 34 pp)
**Suggested venue:** Physical Review D
**Author:** Houston Golden (houston@hubify.com)

Dear Editor,

Please consider this manuscript. This cover letter states its contribution,
scope, and known open items honestly.

## Two concrete contributions

1. **Resolution of the eight-year Cai–Li factor-of-two literature discrepancy.**
   Cai et al. (2009) report the matter-bounce local non-Gaussianity as
   f_NL^local = −35/8; Li et al. (2017) report −35/16, in the *identical*
   f_NL = 10A/(3 Σ k_i³) normalization and the identical squeezed limit. We
   settle this in favour of **−35/16**: re-summing Cai et al.'s *own* four
   cubic-action vertices (field redefinition, ζζ̇², ζ̇∂ζ∂χ, ζ(∂ᵢ∂ⱼχ)²) at
   ε = 3/2 and taking the squeezed limit gives a clean −35/16, matching Li et
   al.'s independent general-c_s result at c_s = 1. The published −35/8 traces to
   a single spurious +(99/128) Σ k_i³ local-shaped term that entered when Cai et
   al. collapsed their (correct) order-grouped expressions into a final polynomial
   (their Eq. 37). Because both works share the same convention, this is an
   arithmetic error, not a convention difference. The correction is certified
   vertex-by-vertex, cross-checked three independent ways (per-vertex sum,
   Cai's own ε-order-grouped intermediates, and Li's general-c_s formula), and is
   reproducible from the archived symbolic notebook (Appendix A). This settles a
   discrepancy that has stood in the literature since 2009 and halves the headline
   bounce amplitude.

2. **A rigorously budgeted, explicitly conditional SPHEREx forecast.** For the
   corrected f_NL = −35/16 we quantify the template mismatch between the
   matter-bounce and local bispectrum templates (a local estimator recovers
   83–88% of the bounce signal; noise-weighted r = 0.84, validated by ℓ-space
   Fisher overlap, 200 injection-recovery realizations, and a 10,000-sample
   null-space scan), assemble a fully itemized systematic budget, and provide a
   closed-form Bayesian model comparison cross-validated against three
   10⁵-realization Monte Carlo ensembles.

## Scope statement (stated up front, no overclaim)

This is a **sensitivity recast of a single externally published forecast, not an
independent forecast.** Every quoted SPHEREx significance and Bayes factor
rescales one imported Heinrich et al. (2023) σ(f_NL^local) ≈ 0.7 baseline by the
template-mismatch factor r; no independent bispectrum Fisher matrix is
constructed here. The abstract carries this as a "Scope" banner in its first
sentence. The headline ranges are conditional sensitivity envelopes, not
internally derived measurement precisions:

- SPHEREx bispectrum significance for f_NL = −35/16: **~2.6–2.75σ optimistic**
  (template-corrected, before GR and b_φ degradation), reducing to a realistic
  **~1.3–2.75σ after the full systematic budget.** We do **not** claim a
  detection or a ≥5σ result; the erroneous −35/8 value (which would have doubled
  every significance) is retained only as a labeled literature reference.

## Disclosed limitations (load-bearing in the abstract)

1. **Single-source dependence.** Because every significance and Bayes factor is a
   rescaling of one published Fisher forecast, the quoted endpoints are not
   statistically independent confirmations. The step that would break this — an
   independent bounce-fiducial multi-tracer bispectrum Fisher re-run that does not
   reuse the Heinrich et al. covariance — is named as the necessary follow-up and
   is not claimed here.

2. **Cubic-order transmission through the bounce (assumption d).** The forecast is
   conditional on faithful third-order bispectrum transmission through the
   nonsingular bounce, verified at linear order and here **derived to a bounded
   ~10⁻³ systematic** by single-clock LQC superhorizon ζ-conservation (effective
   LQC adds no new scalar degree of freedom; transmission = 1 ± O((kη_bounce)²)).
   The one remaining model-dependence is the sign of the subleading gradient
   coefficient — a citable quantization choice, not an open computation.

3. **Additive-quadrature systematic budget.** The realistic range is a scoping
   envelope combined heuristically, not a joint-covariance forecast. The one
   degeneracy that could dominate (f_NL–GR relativistic projection) is bounded
   with a computed shape-overlap degeneracy; the fully channel-native
   noise-weighted covariance Cov_B remains the single named external input
   (one Heinrich-covariance evaluation away), and the honest conservative floor is
   disclosed as a bracket rather than a single number.

## The judgment for the referee

No genuinely-new correctness defect is outstanding. The venue/scope calls we ask
the referee to adjudicate are: **(a)** is a clearly-labeled single-source
sensitivity recast publishable as-is, or does the independent bounce-fiducial
multi-tracer Fisher re-run gate the headline envelope? And **(b)** does a forecast
conditioned on a cubic transfer that is *derived to a bounded systematic* (rather
than evaluated by explicit numerical cubic mode-function evolution) meet the PRD
bar as explicitly conditional? We present the paper as an explicitly-scoped recast
with both caveats load-bearing in the abstract, plus a self-contained,
independently-certified resolution of the Cai–Li amplitude, and ask you to weigh
whether that framing meets the bar.

## AI-use disclosure to the editor
This manuscript was prepared with the assistance of an agentic AI research pipeline built on Anthropic Claude (Opus~4 family, 2026 releases) for agent orchestration and manuscript preparation, with OpenAI GPT-5/o3, xAI Grok-4, and Google Gemini~2.5 used as cross-checking and adversarial internal-review models. The author designed the study, made all scientific and editorial judgments, verified every quantitative result against the committed computational artifacts, and takes full responsibility for the entire content, including any material produced with AI assistance. The AI tools are not authors.

Sincerely,
Houston Golden (houston@hubify.com)
