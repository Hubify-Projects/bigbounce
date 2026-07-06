# P2 .tex proposal — non-local tail projection (PROPOSED, not applied)

Closes the "local-template does not model the non-local tails" MAJOR by adding an
explicit LOCAL/EQUIL/ORTHOGONAL projection + the bounded δr correction to
`sec:template`. No headline number changes. Apply with directive-G PDF hygiene
(bump `\paperVersion`+`\date`, recompile 0 undef-refs, re-mirror, Convex bump).

## Insert location

In `02_full_draft.tex`, immediately AFTER the paragraph ending
"...Either bound confirms the projection noise is subdominant to the other
systematics in our budget." (the `1-r_cos^2` projection-noise paragraph in
`sec:template`, ~line 806 region).

## Proposed paragraph (verbatim to insert)

```latex
\par \emph{Standard-basis template decomposition (non-local tails).} The shape
cosine $r_{\cos}$ above compares the bounce bispectrum only to the local template;
a referee may ask whether the residual $1-r_{\cos}^2$ carries recoverable
equilateral or orthogonal signal that a local-only estimator misses. We therefore
project the physical bounce bispectrum $B_{\rm bounce}(k_1,k_2,k_3)=\BNL(k)\,
S_{\rm local}(k)$ onto the standard separable template basis --- local,
equilateral, and orthogonal~\cite{Senatore:2010} --- on the identical
$23{,}098$-triangle grid. Under uniform, CMB-Fisher ($w\propto k^2$), and LSS
($w\propto k$) weighting the bounce–local cosine is $|r_{\cos}|=0.985$--$0.986$ in
all cases (reproducing the headline $0.985$), while the joint projection onto
$\mathrm{span}\{{\rm local},{\rm equil},{\rm ortho}\}$ raises the recovered
Fisher-norm fraction by at most $0.004$ above the local-only value, i.e.\ a joint
multi-template estimator would recover only $\delta r\lesssim 0.002$ more amplitude
than the local-only estimator ($<0.3\%$ of the headline $r=0.84$, well within the
$\pm0.02$ uncertainty). The apparently large bounce–orthogonal cosine
($0.75$--$0.94$) is not independent non-local content: the orthogonal template is
itself defined as $-3\,S_{\rm local}+\dots$ and is strongly collinear with the
local template, so the joint fit --- which removes this collinearity --- confirms
the genuinely non-local (equilateral $+$ orthogonal-relative-to-local) content of
the residual is negligible. The non-local tails at intermediate and folded
configurations are thus geometrically bounded and do not bias the local-template
recast (reproduction: \texttt{c11\_nonlocal\_template\_projection.py},
\texttt{c11\_nonlocal\_template\_projection.json}; Data and Code Availability).
```

## Bib entry to confirm/add

`\cite{Senatore:2010}` = Senatore, Smith & Zaldarriaga, "Non-Gaussianities in
Single Field Inflation and their Optimal Limits from the WMAP 5-year Data,"
JCAP 01 (2010) 028, arXiv:0905.3746 — the standard equilateral/orthogonal
separable-template reference. If a different NG-template citation is already used
in the paper (e.g. Planck NG), reuse that key instead of adding a new one.

## Abstract / scope touch (optional, one clause)

In the existing template-mismatch scope sentence, the phrase "non-local tails
absorbed into envelope" may be upgraded to "non-local tails shown geometrically
bounded ($\delta r\lesssim0.002$; Sec.~\ref{sec:template})" so the disclosure
points at the new quantitative bound rather than an assertion.
```
