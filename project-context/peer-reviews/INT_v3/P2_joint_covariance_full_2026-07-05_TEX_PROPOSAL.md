# PROPOSED P2 .tex edit (NOT applied) — channel-native ∂B/∂A_GR probe

Closes the RS27 Grok+Gemini systematic-budget MAJOR by upgrading the
proxy-scope sentence in `sec:systematics` (currently ending L1006) from
"deferred here" to a computed-and-bounded statement. No headline number changes;
the proxy 1.3σ stays, now flanked by an in-repo shape-overlap bound and the
exact external-data gate.

## Edit target

File: `research/focused_paper_source_integration/02_full_draft.tex`, L1006,
the sentence beginning "We do not overclaim this as a fully self-consistent
bispectrum marginalization:" through the paragraph end.

## OLD (verbatim, current)

> We do not overclaim this as a fully self-consistent bispectrum
> marginalization: the $\rho=-0.868$ is imported from the sibling power-spectrum
> (SDB) channel as a \emph{proxy}, and the one ingredient still needed to make it
> channel-native is the GR-projection bispectrum response
> $\partial B_g/\partial A_{\rm GR}$ on the SPHEREx triangle set (the direct
> cross-Fisher term, deferred here). Pending that derivative, the $\rho=-0.868$
> proxy is our best bounded joint estimate and supersedes the additive-quadrature
> floor as the quoted conservative endpoint, moving it from $1.5\sigma$ to a
> marginalized ${\sim}\,1.3\sigma$.

## NEW (proposed)

> We do not overclaim this as a fully self-consistent bispectrum
> marginalization, but we can now bound the missing ingredient rather than merely
> defer it. Writing the estimator as $B_g = \fnl\,S_{\rm local} + A_{\rm GR}\,
> S_{\rm GR}$, the required response $\partial B_g/\partial A_{\rm GR} = S_{\rm GR}$
> is the GR-projection template shape, which we construct on the paper's own
> $23{,}098$-triangle grid (the standard relativistic-projection squeezed kernel,
> Verde--Matarrese/Bartolo--Bruni class; \texttt{c12\_gr\_projection\_dBdAgr\_probe.py}).
> Its uniform- and $k^2$-weighted shape overlap with $S_{\rm local}$ is strong,
> $|\rho|\approx0.95$ --- \emph{at least} as degenerate as the $\rho=-0.868$
> proxy, confirming the reviewers' expectation that GR projection and local
> $\fnl$ are strongly correlated. The channel-native marginalized error
> $\sigma_{\rm marg}(\fnl)=\sigma_{\rm base}/\sqrt{1-\rho^2}$ nonetheless cannot
> be pinned in-repo, because the operative $\rho$ is a \emph{noise-weighted}
> Fisher overlap $F_{\fnl A_{\rm GR}}=\sum_{\rm tri}(\partial B/\partial\fnl)
> (\partial B/\partial A_{\rm GR})/{\rm Cov}_B$ requiring the SPHEREx multi-tracer
> galaxy-bispectrum covariance ${\rm Cov}_B(k_1,k_2,k_3)$ on the triangle set
> (Heinrich \etal~\cite{Heinrich:2023}), of which only the scalar
> $\sigma(\fnl^{\rm local})=0.7$ is imported here (the per-triangle covariance is
> external); the weighting-scheme spread in the paper's own $r$ ($0.55$--$1.14$)
> shows this measure choice moves $\rho$ at the $O(1)$ level. The honest budget is
> therefore \emph{bracketed} $\sigma_{\rm marg}\!\approx\!0.8$--$1.3\sigma$: the
> $\rho=-0.868$ proxy (${\sim}\,1.3\sigma$) is the mild upper edge, the in-repo
> $|\rho|\approx0.95$ shape overlap the lower ($\approx0.8\sigma$), both below the
> additive-quadrature $1.5\sigma$. We adopt the proxy $\rho=-0.868$ as the quoted
> conservative endpoint (best-available, source-cited, and now shown \emph{not} to
> be an underestimate); the direct channel-native marginalization is closed by one
> script once ${\rm Cov}_B$ is available (all other ingredients ---
> $\partial B/\partial A_{\rm GR}$, $S_{\rm local}$, triangle grid, $r=0.84$,
> $\sigma_{\rm base}=0.7$ --- are in-repo).

## Notes for whoever applies this

- `Heinrich:2023` is already in `focused_paper_refs.bib` (cited throughout).
- No numeric headline changes: 1.3σ proxy floor retained; the new content is the
  bounding band (0.8–1.3σ) + the explicit external-data gate. The realistic
  1.3–2.75σ abstract envelope is UNCHANGED (1.3σ lower edge preserved).
- Per directive G, applying this = same-bundle: bump `\paperVersion`
  (v1.7.93 → v1.7.94 patch) + `\date`/`\paperTimestamp` to today; recompile
  (0 undef-refs); re-mirror PDF to all served paths byte-identical; Convex
  `paperVersions:bump` with real md5/pages; three-way md5 check.
- Commit the new script `scripts/c12_gr_projection_dBdAgr_probe.py` +
  `outputs/c12_gr_projection_dBdAgr_probe.json` + this writeup +
  `P2_joint_covariance_full_2026-07-05.md` in the same bundle.
- Per CLAUDE.md review-round site-sync: add a `reviewTimeline.ts` entry for the
  RS27 P2 budget-MAJOR closure.
