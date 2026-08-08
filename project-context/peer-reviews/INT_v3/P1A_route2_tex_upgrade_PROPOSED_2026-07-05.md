# PROPOSED P1A .tex upgrade — Route 2 ansatz → one-loop-grounded (NOT YET APPLIED)

Target: `arxiv/paper1a_ech_nogo.tex`, `sec:r2_oneloop` (currently ~L2363–2502),
paper v1A.0.108. Do NOT apply until Houston / truth-audit signs off.
Companion evidence: `INT_v3/P1A_route2_derivation_2026-07-05.md`.

## What changes and why

Current text (L2419–2422) says the coefficient "structure" is a free EFT ansatz:
> "the natural EFT operator built from the Nieh–Yan pseudoscalar and the chiral
> current at the M_Pl⁻¹ α_em/(4π) scale; no published calculation currently
> derives this exact coefficient structure … uses it strictly as an upper-bound
> EFT ansatz."

The Shapiro–Teixeira 2014 extraction (verified, INT_v3 doc) lets us upgrade this
to **one-loop-grounded**: the loop factor `1/(16π²)`, the O(1) Immirzi rational
coefficient, and the `κ²=M_Pl⁻²` Planck suppression are all now fixed by a real
one-loop computation (ST Eqs. 36–37, 41, 42, 46). Only the *absolute
normalization* remains unfixed, and ST themselves explain why (no RG fixed
point; coupled Riccati flow not perturbatively solvable in closed form).

## Proposed replacement for the paragraph at L2417–2438

Replace the sentence beginning "The form is the natural EFT operator …" through
"…insensitive to the O(1) ambiguity in β(γ)." with:

> The coefficient structure of Eq.~\eqref{eq:oneloop_parity_odd} is
> \emph{grounded in the explicit one-loop computation} of Shapiro \&
> Teixeira~\cite{ShapiroTeixeira2014}, who renormalize on-shell
> Einstein--Cartan${+}$Holst gravity with external vector and axial fermion
> currents. The parity-odd, Immirzi-dependent current coupling they renormalize
> is $\lambda_4=\gamma\,\kappa^2\,(W\!\cdot\!J)$ (their Eq.~37,
> $\kappa^2=16\pi G=M_{\rm Pl}^{-2}$), with classical coefficient
> $\alpha_4=-6/(1+\gamma^2)$ and one-loop divergence coefficients
> $\Omega_{44}=81\gamma^4/[16(1+\gamma^2)^2]$,
> $\Omega_{24}=81\gamma^2/[40(1+\gamma^2)^2]$ (their Eqs.~41--42). Their master
> renormalization-group equation $d\lambda/dt=-\sigma/(4\pi)^2$ (their Eq.~46)
> carries \emph{exactly} the $1/(16\pi^2)$ loop factor already written in
> Eq.~\eqref{eq:oneloop_parity_odd}. Three features of the Route-2 budget are
> therefore fixed by a published one-loop result rather than adopted: (i) the
> loop factor $1/(16\pi^2)$; (ii) the coefficient
> $\beta(\gamma)$ is an $\mathcal{O}(1)$ rational function of the Immirzi
> parameter [the $\alpha_4$/$\Omega_{4x}$ family, e.g.\
> $\Omega_{44}/\alpha_4=27\gamma^4/(32(1+\gamma^2))$, which is
> $\mathcal{O}(1)$ for $\gamma\!\sim\!\mathcal{O}(1)$], not a free
> normalization; and (iii) the explicit $\kappa^2=M_{\rm Pl}^{-2}$ on every
> renormalized charge, i.e.\ the Planck suppression in the prefactor
> $\beta(\gamma)/M_{\rm Pl}$. What the one-loop analysis does \emph{not} fix is
> the single \emph{absolute} normalization: Shapiro \& Teixeira show the coupled
> flow for $\lambda_4(t)$ and $\gamma(t)$ (their Eqs.~51,~58) is a Riccati system
> whose particular-solution roots are complex for real $\gamma$, so the system
> \emph{has no renormalization-group fixed point} and they were "unable to solve
> it in a completely satisfactory way." A fully-derived Route-2 amplitude would
> require a UV boundary condition plus a controlled solution of that
> non-perturbative flow (or a dedicated matching calculation for the exact
> $\partial_\mu\vartheta_{\rm NY}J^{5\mu}$ operator). We therefore treat the
> \emph{absolute} $\beta(\gamma)$ normalization as a bounded EFT input while the
> loop factor, Immirzi-rational coefficient, and Planck suppression are
> one-loop-grounded. Because the closure below retains $\gtrsim 60$ orders of
> margin, it is insensitive to this residual $\mathcal{O}(1)$ normalization.

## Proposed edit to the "Ansatz vs derivation (R2/R3)" summary (~L2617–2620)

Change "R2's amplitude coefficient remains a \emph{conservative upper bound from
a chiral-count EFT scaling ansatz}" to:

> R2's amplitude coefficient is now \emph{one-loop-grounded}: its loop factor
> $1/(16\pi^2)$, $\mathcal{O}(1)$ Immirzi-rational coefficient, and
> $\kappa^2=M_{\rm Pl}^{-2}$ Planck suppression are fixed by the Shapiro \&
> Teixeira~\cite{ShapiroTeixeira2014} one-loop renormalization of the
> Holst${+}$fermion sector (their Eqs.~41--42, 46); only the single absolute
> normalization remains a bounded EFT input, because that sector's coupled RG
> flow has no fixed point and is not perturbatively solvable in closed form.

## Mandatory bundle actions if applied (per CLAUDE.md Directive G)

1. Bump `\paperVersion` v1A.0.108 → v1A.0.109; update `\date`/`\paperTimestamp`.
2. Add a top-of-file `%` changelog line documenting the R2 one-loop grounding.
3. Recompile (0 undef-refs) + `/latex-audit` (watch the long displayed
   equations / new paragraph for column overflow).
4. Re-mirror PDF to all served paths byte-identical; Convex `paperVersions:bump`
   with real md5/pages; three-way md5 check.
5. `reviewTimeline.ts` skill-improvement entry (Route-2 ansatz→one-loop-grounded).

## Integrity guardrail

This is a genuine grounding, NOT a fabricated derivation: every cited ST
coefficient is verbatim from the PDF, and the honest limit ("no fixed point,
absolute normalization not fixed") is ST's own stated conclusion. Do not
overstate it as "derived to a number" the way R3 is.
