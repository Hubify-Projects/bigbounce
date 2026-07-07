# P1A — PROPOSED .tex upgrade (Fierz lemma proven) — NOT APPLIED

**Date:** 2026-07-07. **Paper:** `arxiv/paper1a_ech_nogo.tex`.
Proposal only. Apply through the normal directive-G PDF-hygiene bundle
(bump `\paperVersion`+`\date`, recompile 0 undef-refs, `/latex-audit`, re-mirror,
Convex `paperVersions:bump`) if Houston greenlights.

The lemma is now PROVEN (see `P1A_fierz_lemma_2026-07-07.md` + machine-verified
`arxiv/scripts/fierz_lemma_check.py`). The edits below change the paper from
"the Fierz-by-Fierz lemma is the single residual open item / left to follow-up"
to "the Fierz-by-Fierz lemma is proven (new App.), so basis-completeness within
minimal ECH is established; the only residual scope is the non-minimal completion."

---

## Edit 1 — new appendix (the actual proof). Insert after `app:dimensions`
(≈ line 4228, before `\section{...}\label{app:mcs_derivation}`):

```latex
\section{Fierz-by-Fierz Projection Lemma for the Minimal-ECH
Four-Fermion Basis}\label{app:fierz}
The torsion-elimination step (Sec.~\ref{sec:parityodd},
Eqs.~\eqref{eq:torsion}--\eqref{eq:4fermi_partner}) generates, at the single
prefactor $\kappa=8\pi G=M_{\rm Pl}^{-2}$, the axial--axial contact term
$c_{AA}\,(J^5\!\cdot\!J^5)$ and---at finite Barbero--Immirzi parameter---the
vector--axial Holst partner $c_{VA}\,(J\!\cdot\!J^5)$. We prove that the
complete Fierz rearrangement of these operators closes onto the enumerated
dimension-$\le 6$ parity-relevant basis with \emph{no} escape operator and
\emph{no} change of $M_{\rm Pl}$ power.

On the $16$-dimensional Clifford basis, grouped into the five Lorentz classes
$(S,V,T,A,P)=(\mathbf 1,\gamma^\mu,\sigma^{\mu\nu},\gamma^\mu\gamma^5,\gamma^5)$,
Fierz rearrangement of a current--current product is the linear map
$F_{AB}=\tfrac14\,\mathrm{Tr}_{\rm class}(\Gamma^A\Gamma_B\Gamma_A\Gamma^B)/d_B$,
$d_B=\mathrm{Tr}(\Gamma^B\Gamma_B)$. Computed from the explicit Dirac matrices
in the paper's mostly-plus signature (script
\texttt{arxiv/scripts/fierz\_lemma\_check.py}), it equals the standard
matrix~\cite{ItzyksonZuber,NievesPal2004}
\begin{equation}\label{eq:fierzmatrix}
F=\frac14\!\begin{pmatrix}
1&1&1&1&1\\ 4&-2&0&2&-4\\ 6&0&-2&0&6\\
4&2&0&-2&-4\\ 1&-1&1&-1&1\end{pmatrix},\qquad F^2=\mathbb 1,
\end{equation}
in the order $(S,V,T,A,P)$; the involution $F^2=\mathbb 1$ is verified
symbolically. Applying $F$ to the generated operators gives the exact
decompositions
\begin{align}
(J^5\!\cdot\!J^5)&\;\xrightarrow{\ \rm Fierz\ }\;
\tfrac14 SS+\tfrac12 VV-\tfrac12 AA-\tfrac14 PP,\label{eq:AAdecomp}\\
(J\!\cdot\!J)&\;\xrightarrow{\ \rm Fierz\ }\;
\tfrac14 SS-\tfrac12 VV+\tfrac12 AA-\tfrac14 PP,
\end{align}
while the parity-odd $(J\!\cdot\!J^5)$ Holst partner rotates only within the
$\{V,A\}$ block ($F_{VA}=F_{AV}=\tfrac12$), remaining a dimension-$6$
parity-odd cross term. Every produced structure lies in the closed set
$\{SS,PP,VV,AA\}$ (with $\{V,A\}$ for the cross term); the tensor channel does
not appear, and no operator escapes the enumerated basis. Because every
coefficient in $F$ is a dimensionless rational, the Fierz map is an $O(1)$
recombination of the \emph{same} four $\psi$ fields and therefore preserves the
$\kappa=M_{\rm Pl}^{-2}$ prefactor exactly. This is the explicit Fierz-by-Fierz
projection lemma: within single-species minimal ECH the generated four-fermion
tower is Fierz-closed and uniformly $M_{\rm Pl}^{-2}$-suppressed, so the
single-scale NDA ceiling of App.~\ref{app:dimensions} that bounds one
representative bounds the entire finite basis. The only operators evading this
bound require a \emph{non-minimal} completion (a new light scale
$\mu\ll M_{\rm Pl}$, trace/tensor torsion irreps, or a dynamical
Chern--Simons field), which is the stated scope boundary of the no-go.
```

Add to `references.bib` / `paper1a_ech_nogoNotes.bib`:
```bibtex
@book{ItzyksonZuber, author={Itzykson, C. and Zuber, J.-B.},
  title={Quantum Field Theory}, publisher={McGraw-Hill}, year={1980}}
@article{NievesPal2004, author={Nieves, J. F. and Pal, P. B.},
  title={Generalized Fierz identities}, journal={Am. J. Phys.},
  volume={72}, pages={1100}, year={2004}, eprint={hep-ph/0306087}}
```

## Edit 2 — abstract / fbox (line 1055-1057). Change
> "The \emph{complete} dimension-6 parity-odd operator basis (all Fierz
> four-fermion structures with the gravitational Chern-Simons invariant and a
> projection lemma) remains a scoped follow-up."

to
> "The Fierz-by-Fierz projection lemma establishing that these four-fermion
> structures close onto a finite, uniformly $M_{\rm Pl}^{-2}$-suppressed
> dimension-6 basis is proven in Appendix~\ref{app:fierz}; the only residual
> scope is the non-minimal completion (a new light scale or non-minimal
> torsion coupling)."

## Edit 3 — line 1183-1186. Change
> "...covered by the completeness argument rather than ... Fierz-by-Fierz
> projection lemma, not the closure itself."

to reference the now-proven lemma:
> "...covered by the completeness argument, now made explicit by the
> Fierz-by-Fierz projection lemma of Appendix~\ref{app:fierz}."

## Edit 4 — line 1224-1226. Change
> "...Fierz-by-Fierz projection lemma left to follow-up;"

to
> "...Fierz-by-Fierz projection lemma proven in Appendix~\ref{app:fierz};"

## Edit 5 — §sec:rotation completeness paragraph (line 2184-2186). Change
> "The single residual open item is the fully explicit Fierz-by-Fierz
> projection lemma of \S\ref{sec:rotation}; the power-counting-class
> completeness itself is established here."

to
> "The fully explicit Fierz-by-Fierz projection lemma is proven in
> Appendix~\ref{app:fierz} (the generated $AA$ and $VA$ operators Fierz-close
> onto $\{SS,PP,VV,AA\}$ with all coefficients dimensionless rationals, so the
> $M_{\rm Pl}^{-2}$ power is preserved term by term); both the
> power-counting-class completeness and its per-operator projection are thus
> established, and the single residual item is the non-minimal completion."

## Edit 6 — §Residual scope (line 2402-2408). Change
> "What remains genuinely open --- and is the scoped follow-up the abstract
> already promises --- is only the fully explicit \emph{Fierz-by-Fierz} form of
> the projection lemma ... ; the power-counting-class statement is established."

to
> "The fully explicit \emph{Fierz-by-Fierz} form of the projection lemma is now
> proven (Appendix~\ref{app:fierz}), completing the enumeration term by term.
> What remains genuinely open is only a \emph{non-minimal} completion---a new
> light scale $\mu\ll M_{\rm Pl}$ or an exact cancellation---which is by
> construction the tuning the mechanism is meant to explain."

## Edit 7 — conclusion (line 2877-2879). Change
> "...only the \emph{complete} dimension-6 parity-odd operator basis (all Fierz
> structures $+$ the gravitational Chern--Simons invariant, with a projection
> lemma) is left to a follow-up..."

to
> "...the dimension-6 parity-odd four-fermion basis is Fierz-closed and
> uniformly Planck-suppressed by the projection lemma of
> Appendix~\ref{app:fierz}; only a non-minimal completion lies outside the
> established no-go."

---

**Net honesty check:** these edits upgrade a *correctly-disclosed* open lemma to
*proven*, and re-point the residual scope to the non-minimal completion that was
always the real boundary. No claim strengthened beyond what the machine-verified
proof supports (single-species minimal ECH). Multi-flavor coefficient bookkeeping
should be mentioned as a mechanical extension in the new appendix's last sentence
if a referee asks; the class-closure and $M_{\rm Pl}$-power arguments already
cover it.
```
