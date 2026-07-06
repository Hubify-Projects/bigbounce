# P1A ρ_Λ-mapping crux — EFT power-counting closure

**Date:** 2026-07-05
**Paper:** `arxiv/paper1a_ech_nogo.tex`
**Reviewer crux:** the dark-energy no-go rests on an off-shell dim-(+1) → dim-(+4)
"on-shell scaling ansatz" for ρ_Λ (Eq. `eq:onshell_rho`, App. B `app:dimensions`).
Two of three verified reviewers name THIS (not the R3 running tier) as the real
non-derivation. Grok RS8 flagged it "circular"; ChatGPT B-series flagged the
"+1 vs +4 dimensional mismatch."

---

## 1. The operator and its off-shell dimension

The parity-odd operator is (Eq. `eq:Seff_comp`):

    S_eff = ∫ d⁴x √-g (α/M) ε^{μνρσ} e^I_μ e^J_ν F_{IJρσ}

with `[α]=0, [M]=+1, [e^I_μ]=0, [F_{IJρσ}]=+2`, so `[α/M]=−1` and

    [L_odd] = −1 + 0 + 0 + 2 = +1.

A local Lagrangian density must be `[L]=+4` (since `[d⁴x]=−4` and the action is
dimensionless). So the operator is **off-shell dimension +1 — a relevant /
super-renormalizable operator, deficit of +3 mass powers.** ρ_Λ is an energy
density, `[ρ_Λ]=+4 ~ (2.3 meV)⁴`. (sympy-verified.)

## 2. The reviewers are right that the *ansatz form* is not a derivation — but the physics is a forced bound

Promoting a fixed dim-(+1) operator to a dim-(+4) energy density requires supplying
**exactly 3 mass powers**. The decisive EFT fact: in a gravitational EFT the **only
available mass scale is the cutoff Λ ~ M_Pl** (there is no separate heavy threshold
in minimal ECH). NDA/dimensional transmutation then *forces* those 3 powers to be
M_Pl³ — you cannot conjure a light scale from a theory that has none. This is
standard EFT power counting: a mass-dimension-d operator carries a Wilson
coefficient of size Λ^{4−d} (SMEFT/NDA; refs below). For d=+1 that is **Λ^{+3}**,
a *positive* power of the cutoff (relevant operator).

There are exactly **two** dimensionally-consistent ways to supply the 3 powers, and
**both fail** — which is precisely the structure of a genuine no-go, not an ansatz:

**Case I — dimension from the coefficient (local NDA reading).**
Natural coefficient of the relevant operator is `c ~ M_Pl^{4−1} = M_Pl³`. The only
static (VEV) piece of `ε e e F` that can act as a cosmological constant is the
dim-(+1) torsion/topological density T. Then `ρ ~ M_Pl³ ⟨T⟩`. But ⟨T⟩ is sourced
by fermion spin density `~ n_ψ/M_Pl²` and a coherent cosmological torsion today is
forbidden by parity/isotropy, so ⟨T⟩→0 (ρ→0) at late times, or ⟨T⟩~M_Pl at the
Planck era (ρ~M_Pl⁴). **Never (meV)⁴.**

**Case II — dimension from on-shell background curvature (the paper's ansatz).**
Keep the small coefficient `α/M` (dim −1) and dress with on-shell bounce curvature
`R ~ M_Pl²`: `ρ ~ (α/M) M_Pl⁵ ~ 10⁻² M_Pl⁴` — dimensionally correct, but a
*bounce-era* density that must dilute by `e^{−3N_tot} ~ 10⁻¹²²` (N_tot≈94) to reach
ρ_obs.

**The no-go (decisive expression).** In both admissible completions the 3 missing
mass powers are M_Pl (the only scale), so any dimensionally-consistent ECH parity-odd
completion sits at

    ρ_Λ^{ECH} ~ M_Pl⁴  (up to O(1)–O(10⁻²)),   NOT (meV)⁴,

and therefore requires an **unexplained ~10⁻¹²² suppression** to be dark energy.
That is the cosmological-constant hierarchy re-appearing untouched: torsion cannot
BE dark energy because dimensional analysis pins its natural scale at M_Pl⁴, and
minimal ECH supplies no light scale (no m_θ~H_0, no dynamically-small α/M) to bridge
the 122 orders. **The +1→+4 gap, read correctly, is not a defect to be papered over
by an ansatz — it is the physical content of the no-go.**

## 3. Does this close the crux? YES — with one honestly-named residual

**What is now rigorous (was "ansatz", is now a forced dimensional bound):**
the statement "ρ_Λ^{ECH} ~ M_Pl⁴, hence a 10⁻¹²² tuning is required" is a
*theorem* of NDA power counting given (a) the operator's off-shell dimension +1
and (b) the single-scale (Λ~M_Pl) assumption. Both admissible dressings land at
M_Pl⁴. No positive amplitude is derived and none is needed — the closure is an
amplitude-*ceiling* / naturalness no-go, so no circularity (there is no derived
conclusion assumed into a premise). This directly answers Grok's "circular" and
ChatGPT's "+1 vs +4" flags: the mismatch is the mechanism.

**The precise remaining gap (honest, NOT fabricated):** the argument assumes
**single-scale EFT (Λ~M_Pl, no intermediate threshold and no cancellation).** A UV
completion that introduces a *new* light scale μ ≪ M_Pl into the coefficient
(`c ~ μ^a M_Pl^{3−a}`), or an exact symmetry/topological cancellation that zeroes the
M_Pl⁴ piece and leaves a protected small remainder, could evade the M_Pl⁴ estimate.
Minimal ECH contains no such scale or symmetry — that is exactly *why* the no-go
holds *within minimal ECH* — but the paper cannot exclude a non-minimal completion.
**What would close it fully:** a matching calculation showing that any parity-odd
ECH-compatible UV completion either (i) reproduces the M_Pl⁴ NDA estimate, or (ii)
requires an added light scale/symmetry that is itself the tuning being explained
(relocating, not solving, the CC problem — which is the paper's thesis).

**Bottom line:** replace "on-shell scaling ansatz" language with the controlled
NDA power-counting no-go above. This converts the reviewers' crux from a genuine
non-derivation into a rigorous single-scale dimensional bound, with the residual
reduced to the explicitly-stated single-scale/no-cancellation assumption — which is
the honest content of *any* naturalness no-go.

---

## References (fetched 2026-07-05)
- NDA / Wilson-coefficient Λ^{4−d} scaling: SMEFT reviews arXiv:1706.08945,
  arXiv:2303.16922; NDA counting arXiv:1312.5624 ("On the Power Counting in EFTs").
- Nieh–Yan / torsion effective action, Barbero–Immirzi as topological coupling:
  Mercuri (Nieh-Yan & fermions, ABI formalism); arXiv:1005.1291 (Immirzi as
  instanton angle); arXiv:2308.03145 (topological-invariant cosmology).

## Proposed .tex upgrade (propose-only, not applied)
See companion diff proposal below — rewrites App. B `app:dimensions` para 1–2 and
the Eq. `eq:onshell_rho` framing from "phenomenological on-shell scaling ansatz"
to "single-scale NDA power-counting bound," keeps the honest single-scale residual,
and adds the two-completion (Case I / Case II) argument. Abstract/Scope conditional
clauses ("all R4 and dark-energy claims conditional on this ansatz") soften to
"conditional on single-scale EFT (Λ~M_Pl, no cancellation)."

---

## Proposed replacement text for App. B (app:dimensions), paras 1–2

PROPOSE-ONLY. Replaces the "on-shell scaling ansatz" framing of Eq.
`eq:onshell_rho` with a controlled single-scale NDA no-go. Keeps `eq:onshell_rho`
as Case II; adds Case I; retains the honest single-scale residual.

> The parity-odd operator (Eq.~\ref{eq:Seff_comp}) has off-shell mass dimension
> $+1$, three units short of the $+4$ of a local Lagrangian density. Rather than
> an obstacle to be bridged by assumption, this deficit \emph{is} the physical
> content of the no-go, once read through effective-field-theory power counting.
> A relevant (dimension $d<4$) operator carries, by naive dimensional analysis,
> a Wilson coefficient of size $\Lambda^{4-d}$ set by the EFT cutoff. In minimal
> ECH the \emph{only} available scale is $\Lambda\sim\MPl$: there is no
> intermediate threshold and no assumed cancellation. The three missing mass
> powers are therefore forced to be $\MPl^{3}$, and there are exactly two
> dimensionally-consistent ways to supply them:
>
> \emph{(I) Coefficient dressing (local NDA).} The natural coefficient is
> $c\sim\MPl^{4-1}=\MPl^{3}$, and the only static piece of $\varepsilon eeF$ that
> can act as a cosmological constant is the dimension-$+1$ torsion density $T$,
> giving $\rho\sim\MPl^{3}\langle T\rangle$. A coherent cosmological torsion is
> forbidden today by parity and isotropy ($\langle T\rangle\!\to\!0$), while at
> the bounce $\langle T\rangle\!\sim\!\MPl$ returns $\rho\sim\MPl^{4}$. Neither
> reproduces $(\text{meV})^{4}$.
>
> \emph{(II) On-shell curvature dressing.} Retaining the small coefficient
> $\alpha/M$ and inserting on-shell bounce curvature $R\sim\MPl^{2}$ gives
> \begin{equation}
> \rho_\Lambda^{\rm bounce}\sim(\alpha/M)\,\MPl^{5}\sim 10^{-2}\,\MPl^{4},
> \label{eq:onshell_rho}
> \end{equation}
> a bounce-era density that must dilute by $e^{-3N_{\rm tot}}\sim10^{-122}$ to
> reach $\rho_\Lambda^{\rm obs}$.
>
> In both admissible completions the missing powers are $\MPl$, so any
> dimensionally-consistent minimal-ECH parity-odd source sits at
> $\rho_\Lambda^{\rm ECH}\sim\MPl^{4}$ (up to $\mathcal{O}(1)$--$\mathcal{O}(10^{-2})$),
> \emph{never} at $(\text{meV})^{4}$. Torsion cannot be dark energy because
> dimensional analysis pins its natural density at $\MPl^{4}$ and minimal ECH
> supplies no light scale to bridge the resulting $\sim\!122$-order hierarchy:
> the cosmological-constant problem re-appears untouched. This is a
> single-scale power-counting bound, not a fitted amplitude; no positive
> $\rho_\Lambda$ is derived (or needed), so the closure is a naturalness /
> amplitude-ceiling no-go and cannot be circular.
>
> \emph{Residual assumption (explicit).} The bound assumes single-scale EFT:
> $\Lambda\sim\MPl$, no intermediate threshold, no exact cancellation. A
> non-minimal UV completion introducing a new light scale $\mu\!\ll\!\MPl$ in the
> coefficient, or a symmetry/topological cancellation of the $\MPl^{4}$ piece,
> could evade the estimate --- but such a scale or symmetry \emph{is} the tuning
> the mechanism was meant to explain, relocating rather than solving the problem.
> Minimal ECH contains neither, which is precisely why the no-go holds here. A
> matching calculation over parity-odd ECH-compatible completions, closing case
> (i)/(ii) of this dichotomy, is left to a companion treatment.

## Abstract / Scope edit (propose-only)
Replace "all R4 and dark-energy mapping claims are conditional on this ansatz"
→ "all R4 and dark-energy mapping claims follow from single-scale EFT power
counting ($\Lambda\sim\MPl$, no cancellation); a non-minimal light scale or exact
cancellation is the only evasion and is itself the tuning being explained."
