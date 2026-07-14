# P1 exact-PDF round summary

## P1A v1A.0.116

**Disposition: not publication-ready; major technical revision.** The contact coefficient, Fierz matrix/sign, natural-unit conversion, late-density suppression, and classical canonical-scalar transparency theorem survive. The advertised independent NJL magnitude closure does not. The paper mixes unreduced `M_P` with `kappa=1/M_P^2` (missing `8pi`), uses a gap equation high by two for its declared `G_s(psibar psi)^2`, and hides the `N_fN_c=9`, `gamma=0.274` maximizing inputs behind “single species.” Corrected worst-case magnitudes are about 1.96 scalar and 3.92 axial. The unsupported one-point-current-to-`w=-1` inference must also be removed or derived.

Bounded closure contract:

1. Use one Planck convention everywhere and correct the gap equation/script/results.
2. Remove the false magnitude-subcritical leg; retain the declared repulsive scalar-channel result only within its Fierz/mean-field convention.
3. Publish the full scan inputs/table and commit-pin artifacts.
4. Remove/derive the composite equation-of-state claim; repair conventions, tensor-mode wording, and provenance.
5. Recompile and obtain a fresh exact-PDF multi-model review before changing readiness.

## P1B v1B.0.105

**Disposition: not publication-ready; major revision (reject-and-resubmit if binary).** The stock-CAMB null arithmetic, truncation procedure, sample counts, estimator normalization, figure label, prior-predictive 11.597%/6.137%, and raw 44.047%/13.382%/0.3275% chain cuts reproduce. Two new blockers remain. The 13% “posterior mass/prior cost” normalizes a fixed-background surrogate over many non-spectator samples, so it is only a surrogate validity fraction unless the likelihood is made background-consistent. The NaMaster fit center-samples unbinned theory against broad decoupled bandpowers; a correctly windowed-theory rerun is required before interpreting the ~12% bias or 0.040-degree floor. Table IV and `b22f8cc9` provenance are also stale/mixed.

Bounded closure contract:

1. Relabel 44%/13% as surrogate-chain validity diagnostics or rerun a background-consistent ALP likelihood.
2. Apply the identical NaMaster bandpower/window operator to theory and rerun the synthetic recovery/robustness battery.
3. Regenerate Table IV from one committed script with declared mean/median and ESS marker/estimator.
4. Replace `b22f8cc9` with an exact release snapshot; fill companion arXiv and dataset DOI metadata at submission.
5. Repair c15 convergence, minimal-ECH torsion, SNR, and synthetic-floor wording, then obtain a fresh exact-PDF round.

## Cross-model lesson

The direct API reviewers caught P1A's Planck convention but missed its gap-equation normalization; the subscription Codex audit independently derived both. Conversely, several direct-vendor “essential” findings were visual/source misreads. On P1B, only the exact-artifact Codex leg found the bandpower-template mismatch, surrogate-posterior normalization issue, and mixed Table IV statistics. The acceleration improvement is clear: use native/raster PDF review for breadth, then require at least one commit-aware model to execute the actual algebra and artifact reductions before readiness can advance.
