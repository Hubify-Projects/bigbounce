# PROPOSED P2 .tex upgrade — quadrature heuristic → marginalized Fisher (NOT applied)

Target: `research/focused_paper_source_integration/02_full_draft.tex`,
`\emph{Scope of the systematic budget...}` paragraph (currently L971) and the
`tab:systematics` caption region.

## Proposed replacement text for the last two sentences of the L971 scope paragraph

Replace:

> ...This SDB degradation does not propagate to the bispectrum-only headline of
> \S\ref{sec:spherex}, which accesses additional triangle configurations that
> break the $\fnl$--$n_{\fnl}$ degeneracy; a full joint bispectrum covariance is
> the one element still combined heuristically here.

with:

> ...This SDB degradation does not propagate directly to the bispectrum-only
> headline of \S\ref{sec:spherex}, which accesses additional triangle
> configurations that partially break the $\fnl$--$n_{\fnl}$ degeneracy.
> \emph{Joint-covariance test of the bispectrum GR budget.} To move beyond the
> additive-quadrature heuristic in the one channel still combined that way, we
> note that adding a nuisance in quadrature to the noise
> ($\sigma_{\rm eff}=\sqrt{\sigma_{\rm base}^2+\sigma_{\rm GR}^2}$) is the
> $\rho=0$, independent-nuisance limit of a joint Fisher; the honest marginalized
> error for a correlated $\{\fnl,\,A_{\rm GR}\}$ pair is instead
> $\sigma_{\rm marg}(\fnl)=\sigma_{\rm base}/\sqrt{1-\rho^2}$ (inverse-Fisher
> $2\times2$). Using the paper's own directly-computed CAMB degeneracy strength
> $\rho=-0.87$ (\texttt{c8}, the sole in-repo Fisher correlation, transferred as a
> physically-motivated proxy since GR projection and scale-dependent bias act on
> the same ultra-large-scale $\fnl$ modes) inflates the baseline by $2.0\times$,
> so the conservative floor is $|\fnl|\,r/\sigma_{\rm marg}=2.1875\times0.84/1.42
> \approx 1.3\sigma$ rather than the quadrature $1.5\sigma$ --- i.e.\ the honest
> marginalized floor is ${\sim}\,14\%$ \emph{lower} than the quadrature estimate,
> confirming the reviewers' expectation that correlated nuisances loosen rather
> than tighten the budget (\texttt{c10\_joint\_covariance\_marginalization.py}).
> The one remaining ingredient for a fully self-consistent bispectrum joint
> covariance is the GR-projection response $\partial B_g/\partial A_{\rm GR}$ on
> the SPHEREx triangle set; pending that derivative, the $\rho=-0.87$ proxy is
> our best bounded joint estimate and supersedes the quadrature floor as the
> quoted conservative endpoint.

## Table `tab:systematics` — add a marginalized-Fisher row

Add after the `All combined` rows:

```latex
Joint Fisher (marg., $\rho=-0.87$) & $\sigma_{\rm marg}=0.7/\sqrt{1-0.87^2}=1.42$ & denom.\ (Fisher) & marginalized & ${\sim}\,1.3\sigma$ \\
```

and add to the caption: "The final row replaces the additive-quadrature GR floor
with the inverse-Fisher marginalized error at the paper's own measured
degeneracy $\rho=-0.87$ (\texttt{c8}); it is the honest conservative endpoint,
$\sim14\%$ below the quadrature $1.5\sigma$."

## Abstract / headline consequence

The realistic envelope lower endpoint moves from $\sim1.3$--$1.5\sigma$
(quadrature) to a marginalized $\sim1.3\sigma$ — already inside the quoted
$1.3$--$2.75\sigma$ realistic range, so NO abstract number changes; the upgrade
is a *methodological* strengthening (heuristic → marginalized) that closes the
"additive heuristic" MAJOR at the definitional level while honestly flagging the
one missing derivative.

## Do NOT apply until

- Houston sign-off on transferring the c8 $\rho=-0.87$ as a bispectrum proxy
  (it is the sibling channel, defensible but a proxy).
- Ideally, computing the actual $\partial B_g/\partial A_{\rm GR}$ to replace the
  proxy with a channel-native correlation.
