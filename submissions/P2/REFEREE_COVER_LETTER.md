# Cover Letter — Paper 2

**Title area:** A SPHEREx sensitivity recast for the matter-bounce local-type non-Gaussianity f_NL
**Source:** `research/focused_paper_source_integration/02_full_draft.tex`
**Suggested venue:** Physical Review D

Dear Editor,

Please consider this manuscript. This cover letter states its contribution,
scope, and known open items honestly.

## Contribution
The paper forecasts the discriminating power of SPHEREx (and the proposed
MegaMapper) for the matter-bounce local-type non-Gaussianity prediction
f_NL^local, via scale-dependent bias and the galaxy bispectrum. Its concrete
deliverables are: a source-level audit of the matter-bounce f_NL prediction; an
explicit template-mismatch quantification (a local estimator recovers 83–88% of
the bounce signal; r ≈ 0.84 noise-weighted, validated by ℓ-space Fisher overlap,
200 injection-recovery realizations, and a 10,000-sample null-space scan); a
fully itemized systematic budget; and a closed-form Bayesian comparison
cross-validated against three 10⁵-realization Monte Carlo ensembles.

## Scope statement
This is a **sensitivity recast of a single externally published forecast, not an
independent forecast.** Every quoted SPHEREx significance and Bayes factor
rescales one imported Heinrich et al. (2023) σ(f_NL^local) ≈ 0.7 baseline by the
template-mismatch factor r; no independent bispectrum Fisher matrix is
constructed here. The abstract carries this as a "Scope" banner up front. The
headline ranges are conditional sensitivity envelopes, not internally derived
measurement precisions.

## Disclosed limitations (stated up front)
1. **The Cai–Li factor-of-two is a GENUINE, unresolved literature discrepancy.**
   Cai et al. report f_NL = −35/8; Li et al. report −35/16, in the identical
   normalization and squeezed limit. We audited both source calculations, found
   their shape-function polynomials agree coefficient-for-coefficient at c_s=1,
   and located the discrepancy in the local-limit reduction / permutation
   bookkeeping — but a full four-vertex in-in re-derivation (attempted; see
   below) confirms it **cannot be settled from the published work.** We therefore
   headline the forecast as an amplitude-conditional range across both published
   values, f_NL ∈ [−35/16, −35/8], with realistic significance ~1.3–5.5σ. We do
   NOT headline the optimistic Cai-only values while the factor-of-two is open.
2. **The cubic-transmission conditional (the single weakest link).** The forecast
   is conditional on assumption (d) — faithful third-order bispectrum
   transmission through the bounce — verified only at linear order. A full Path-Z
   in-in computation was attempted; it established scale-independence of the
   growing-mode transfer (shape preservation) but did **not** converge on
   amplitude (the normalization diverged across background depths). f_NL = −35/8
   honestly remains conditional; the non-convergent numbers were NOT folded into
   the paper.
3. **Additive-quadrature systematic budget**, combined heuristically with a joint
   SDB Fisher cross-check bounding its direction.

## The judgment for the referee
The venue/scope calls LLM referees flag but cannot adjudicate are: **(a) is a
clearly-labeled single-source sensitivity recast publishable as-is, or does the
independent bounce-fiducial multi-tracer Fisher re-run gate the headline
envelope? And (b) does a forecast conditioned on an unverified — though
shape-supported — cubic transfer belong in PRD now as explicitly conditional, or
must a converged cubic in-in computation gate submission?** We present the paper
as an explicitly-scoped recast with both caveats load-bearing in the abstract,
and ask you to weigh whether that framing meets the bar.

No genuinely-new correctness defect is outstanding; prior "arithmetic mismatches"
were traced to PDF-font extraction artifacts, not errors.

Sincerely,
Houston Golden (houston@hubify.com)
