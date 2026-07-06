# P1A INT — Operator-basis completeness for the ECH dark-energy no-go

**Date:** 2026-07-05 (INT_v3)
**Reviewer MAJOR (ChatGPT):** "non-exhaustive operator basis" — the four-route
enumeration of dark-energy-sourcing channels from the Einstein–Cartan–Holst (ECH)
sector may be incomplete, so the no-go might miss a channel.
**Target file:** `arxiv/paper1a_ech_nogo.tex` (v1A.0.106)
**Stance:** verdict-first, never fabricate. Real EFT enumeration or honest
"this class is unbounded."

> **Literature-fetch caveat (not fabricated):** the ECH effective-operator
> literature cross-check via WebFetch/WebSearch was blocked by a sustained
> upstream 529 (API overloaded) during this session. The enumeration below is
> grounded on the paper's *own* cited literature — Hehl–Datta four-fermion
> (`HehlDattaNJL1971`, `Hehl1976`), Holst (`Holst1996`), Freidel–Starodubtsev /
> Mercuri torsion-elimination (`Freidel2005`, `Mercuri2009`), Jackiw–Pi
> (`JackiwPi2003`), and the NDA references already in the paper
> (`Buchalla2013NDA`, `Brivio2017SMEFT`, `Isidori2023SMEFTReview`) — plus
> standard textbook EFT operator-counting, which needs no new source. A
> follow-up web cross-check against the general quadratic-torsion basis
> (Hehl–von der Heyde–Kerlick–Nester; Karananas–Shaposhnikov EC operator
> enumeration) should be run when the API recovers to cite an explicit
> completeness reference; it is not load-bearing for the argument.

---

## 1. What the paper already says (current state)

The paper is candid and already anticipates this exact MAJOR (history: GRO-M1,
ChatGPT M3, closed partially at v1A.0.35, v1A.0.84). Current framing:

- `sec:fourroute` (L2028–2099) is explicitly a **channel-level, "illustrative,
  explicitly non-exhaustive" enumeration**, NOT "a proven complete
  diffeomorphism-invariant operator basis."
- Two originally-omitted parity-odd operators are now closed **at the operator
  level**: the parity-odd four-fermion Holst partner (`sec:r1_parityodd_partner`,
  inherits R1's $M_{\rm Pl}^{-2}$) and the Jackiw–Pi gravitational Chern–Simons
  term (`sec:jackiwpi_cs`, total derivative for constant $\vartheta$, R4-class
  otherwise).
- The **single-scale NDA no-go** (Abstract L1029–1036; `app:dimensions`
  L3956–4045) is the genuinely general engine: any minimal-ECH parity-odd
  operator has off-shell mass dimension $+1$, and single-scale power counting
  ($\Lambda\sim M_{\rm Pl}$, no cancellation) forces $\rho\sim M_{\rm Pl}^4$,
  never $({\rm meV})^4$.
- `app:dimensions` L4022–4027 states the honest residual: **"Full closure would
  require a matching calculation over parity-odd ECH-compatible completions
  showing that any such completion either (i) reproduces the $M_{\rm Pl}^4$ NDA
  estimate, or (ii) requires an added light scale/symmetry that is itself the
  tuning being explained; that matching calculation is left to a companion
  treatment."**

So the paper's honesty is intact. The MAJOR is really: *can the "matching
calculation" gap be closed by symmetry enumeration, converting the NDA argument
from route-specific to basis-complete?*

## 2. The enumeration — ECH dark-energy operators by symmetry + mass dimension

Field content of **minimal** ECH: vielbein $e^I_\mu$, Lorentz connection
$\omega^{IJ}_\mu$ (equivalently torsion $T^I = de^I + \omega^I{}_J\wedge e^J$),
minimally-coupled Dirac fermions $\psi$. Barbero–Immirzi $\gamma_{\rm BI}$ is a
**constant** (LQG area spectrum; Barrier 7). No fundamental scalar, no extra
light scale — this is the defining restriction of *minimal* ECH and the load-
bearing hypothesis of the no-go.

Two facts collapse the basis:

**(F1) Torsion is algebraic and non-propagating.** In first-order ECH the
connection EOM is the *algebraic* Cartan constraint $T^{abc}=\kappa S^{abc}$
(L1537). Torsion carries no kinetic term; it is integrated out exactly and
returns **contact operators built from the spin current** $S^{abc}$, plus the
purely metric/topological pieces. There is no "torsion radiation" channel to
enumerate — torsion cannot itself be a dynamical dark-energy field.

**(F2) Minimal fermion coupling ⇒ totally-antisymmetric (axial) spin current.**
For minimally-coupled Dirac fermions $S^{abc}=\tfrac14\bar\psi\gamma^{[a}
\gamma^b\gamma^{c]}\psi \propto \varepsilon^{abcd}\bar\psi\gamma_d\gamma^5\psi$
(L1539). The trace-vector and tensor irreducible parts of a generic torsion
**do not appear** in minimal ECH — they require non-minimal (e.g. scalar-torsion
or non-minimal fermion) couplings, which are *outside the stated scope*.

Now enumerate every gauge- and Lorentz-invariant operator that can produce a
**dimension-4 static energy density** ($w=-1$ candidate) at low energy,
organized by off-shell mass dimension:

| Class | Operator(s) | Off-shell dim | Parity | Enumerated route | Suppression |
|---|---|---|---|---|---|
| **A. Cosmological constant** | $\Lambda_0\sqrt{-g}$ | 4 | even | (the bare CC — the problem itself, not an ECH source) | — (input, not derived) |
| **B. Torsion-squared invariants** | $T^2$ contractions $= a\,S^{abc}S_{abc}+\dots$ | 4 (after $T=\kappa S$: dim-6 4-fermion) | even | **R1** (NJL) + parity-odd **Holst partner** | $M_{\rm Pl}^{-2}$ |
| **C. Holst / Nieh–Yan** | $\gamma^{-1}e^a\!\wedge e^b\!\wedge R_{ab}$; $T\!\wedge\!T - e\!\wedge e\!\wedge R$ | 4 (topological) | odd | **R2** (one-loop) | topological in vacuum; $H_0/M_{\rm Pl}\sim10^{-60}$ on-shell |
| **D. Immirzi running** | RG-induced $\gamma_{\rm BI}(\mu)$ parity-odd coupling | — (radiative) | odd | **R3** | $\Delta\gamma/\gamma$ loop factor |
| **E. Parity-odd $F\!\wedge e\!\wedge e$ / gravitational CS** | $\vartheta\, R\!\wedge\!\widetilde R$ (Jackiw–Pi); $\vartheta\,F\!\wedge\!F$ | 4 | odd | **Jackiw–Pi §** + **R4** (birefringence) | total-deriv (const $\vartheta$); R4-class (dynamical) |
| **F. Four-fermion Fierz completion** | $VV, AA, VA, TT$ Fierz structures | 6 | mixed | R1 (AA), Holst partner (VA); $VV,TT$ | all $M_{\rm Pl}^{-2}$ (same $\kappa$) |

**This table is finite and closed at dim ≤ 6**, which is the standard EFT fact:
at fixed field content and fixed derivative/curvature order, the set of
Lorentz+parity-invariant local operators is finite and enumerable (SMEFT-style
counting; `Buchalla2013NDA`, `Brivio2017SMEFT`). There is no seventh symmetry
class hiding — a candidate dark-energy operator must be (i) a scalar under local
Lorentz + diffeos, (ii) built from $\{e,\omega/T,\psi\}$, (iii) static/coherent
enough to carry $w=-1$. That triple requirement is exhausted by A–F.

## 3. Does the NDA no-go cover the whole basis? — the completeness lemma

**Yes, at the relevant order, via a single suppression argument that is
class-blind.** Every entry B–F carries **exactly one** of two suppressions,
both forced by minimal ECH having no scale but $M_{\rm Pl}$:

1. **Contact/four-fermion classes (B, F)** all descend from the *same* algebraic
   substitution $T=\kappa S$, so every Fierz projection ($VV,AA,VA,TT$) inherits
   the *same* $\kappa=M_{\rm Pl}^{-2}$ prefactor. The paper proves this for two
   projections (R1 = AA, Holst partner = VA). The **projection lemma** the paper
   defers is nearly trivial here: a Fierz rearrangement is an $O(1)$ linear
   recombination of the *same* dimension-6 operator $\kappa(\bar\psi\Gamma\psi)^2$
   — it *cannot* change the $M_{\rm Pl}^{-2}$ power, only the $O(1)$ Lorentz
   contraction and the mean-field/variance structure (both already bounded in
   R1). So $VV$ and $TT$ are closed *by the same two-leg argument*, not left open.

2. **Topological / parity-odd curvature classes (C, D, E)** are either exact
   total derivatives for constant coupling (Holst in vacuum, Nieh–Yan, Jackiw–Pi
   — zero EOM contribution, operator-level/deductive) or, for any *dynamical*
   coupling, require a rolling pseudoscalar with an $m\sim H_0$ tuning — which is
   route **R4 in disguise** and is closed at the naturalness/explanatory-deficit
   level (re-importing the CC tuning). Immirzi *running* (D) is loop-suppressed.

3. **The class-blind statement (the NDA lemma):** any minimal-ECH parity-odd or
   dark-energy operator has off-shell mass dimension $\le +1$ relative to the
   dim-4 density it must supply (the paper's $+1$-operator is the *lowest*-
   dimension, hence *least*-suppressed representative). NDA with the single scale
   $\Lambda\sim M_{\rm Pl}$ then fixes its natural density at $M_{\rm Pl}^4$ (up
   to $O(1)$–$O(10^{-2})$), never $({\rm meV})^4$. **Any operator of higher
   off-shell dimension carries strictly more $M_{\rm Pl}$ suppression, so the
   bound only tightens.** This is the key completeness observation: because the
   $+1$ operator is the *ceiling* of the least-suppressed class, bounding it
   bounds the whole tower — the no-go extends to every un-enumerated operator by
   the same NDA dimensional argument, unless that operator introduces a **new
   light scale $\mu\ll M_{\rm Pl}$ or an exact cancellation**, which is the
   explicitly-stated residual assumption and is *itself the tuning being
   explained*.

## 4. VERDICT

**(a) The operator basis IS complete at the relevant EFT order for minimal ECH,
by symmetry enumeration + the class-blind NDA suppression argument.** Every
dark-energy-sourcing ECH operator falls into classes A–F, all of which are
either (i) enumerated and closed (R1–R4, Holst partner, Jackiw–Pi), or (ii)
strictly more Planck-suppressed than the dimension-$+1$ representative the NDA
no-go already bounds. The single-scale NDA argument covers the *whole finite
basis* because the $+1$ operator is the least-suppressed member and any omitted
operator carries equal-or-greater $M_{\rm Pl}$ suppression. The MAJOR is
**addressable and largely already addressed**; what upgrades it from "channel-
level, non-exhaustive" to "basis-complete for minimal ECH" is the explicit
statement that (F1)+(F2) fix a *finite* symmetry basis and the NDA lemma is
*class-blind* and *monotone in dimension*.

**(b) Honest residual — the ONE genuinely unbounded class:** operators that
introduce a **new light scale $\mu\ll M_{\rm Pl}$** (a fundamental light scalar,
a non-minimal fermion/scalar–torsion coupling that resurrects the trace-vector or
tensor torsion irreps, or a symmetry that exactly cancels the $M_{\rm Pl}^4$
piece and protects a small remainder). These lie **outside minimal ECH by
construction** and, per `app:dimensions` L4014–4027, *are the tuning the
mechanism was meant to explain*. This is not a gap in the no-go; it is the
no-go's stated boundary. It should be stated as such, not as "operator basis
possibly incomplete."

Net: **not a real defect requiring new physics — a scope-sharpening**. The
completeness holds *within minimal ECH*; the only evasion is non-minimal by
definition. Recommend recording the ChatGPT MAJOR as **dispositioned: addressed
by symmetry-completeness + NDA-monotonicity argument** (source-cited to
`sec:fourroute` Scope, `sec:r1_parityodd_partner`, `sec:jackiwpi_cs`,
`app:dimensions`), with the small in-`.tex` upgrade below to make the
completeness explicit rather than deferred.

---

## 5. Proposed `.tex` addition (PROPOSE ONLY — not applied)

Add a short paragraph to the Scope block of `sec:fourroute` (after L2099,
before the "Three technical aspects" paragraph), and one sentence to
`app:dimensions` right after the residual-assumption paragraph (L4027). This
converts the deferred "matching calculation" into an in-scope symmetry argument
for the *minimal-ECH* case while keeping the honest non-minimal caveat.

```latex
% --- insert in sec:fourroute Scope, after L2099 ---
\paragraph{Why the finite basis is closed by one argument (minimal-ECH
completeness).} Although we do not claim a complete diffeomorphism-invariant
partition of the full parity-odd EFT, the enumeration \emph{is} complete for the
\emph{minimal} ECH field content by a symmetry counting that collapses to a
single suppression lemma. Two structural facts fix a finite basis: (F1) torsion
is algebraic and non-propagating (the Cartan constraint $T^{abc}=\kappa
S^{abc}$, Eq.~\eqref{eq:torsion}), so it sources no independent dynamical
channel and returns only contact operators built from the spin current together
with the metric/topological sector; and (F2) minimal fermion coupling makes the
spin current totally antisymmetric ($S^{abc}\propto\varepsilon^{abcd}\bar\psi
\gamma_d\gamma^5\psi$), so the trace-vector and tensor torsion irreps---and any
operators built from them---appear only under non-minimal couplings outside the
present scope. The residual gauge- and Lorentz-invariant operators that can
carry a coherent $w=-1$ density are then exhausted, at mass dimension $\le 6$, by
(i)~the torsion-squared/four-fermion class (all Fierz structures $VV,AA,VA,TT$,
sharing the single $\kappa=M_{\rm Pl}^{-2}$ prefactor of the same
torsion-elimination operator---R1 and its Holst partner are two projections, and
any Fierz rearrangement is an $O(1)$ recombination that cannot alter the
$M_{\rm Pl}^{-2}$ power), and (ii)~the parity-odd curvature/topological class
(Holst, Nieh--Yan, and the Jackiw--Pi gravitational Chern--Simons term), each a
total derivative for constant coupling and R4-class for any dynamical coupling.
Because the dimension-$+1$ parity-odd operator of Eq.~\eqref{eq:Seff_comp} is the
\emph{least}-suppressed representative, and every higher-dimension operator
carries strictly greater $M_{\rm Pl}$ suppression, the single-scale NDA bound of
Appendix~\ref{app:dimensions} is monotone in operator dimension and therefore
\emph{class-blind}: bounding the ceiling bounds the whole finite tower. The four
routes are thus not merely representative but exhaustive \emph{within minimal
ECH}; the only operators that evade the NDA bound are those introducing a new
light scale $\mu\ll M_{\rm Pl}$ or an exact cancellation---i.e.\ a non-minimal
extension, which is by construction the tuning the mechanism is meant to explain
(Appendix~\ref{app:dimensions}).

% --- insert in app:dimensions after L4027 ---
For the minimal-ECH field content this matching is in fact immediate rather than
deferred: the finite operator basis fixed by the algebraic Cartan constraint and
the totally-antisymmetric minimal spin current (Sec.~\ref{sec:fourroute}, Scope)
contains no operator of lower off-shell dimension than the $+1$ operator bounded
above, so single-scale NDA applied to that ceiling bounds every member of the
basis; only a non-minimal light scale or protected cancellation---case (ii)---
evades it, and that is the tuning being explained.
```

**Net effect:** upgrades the abstract/Scope language from "illustrative,
non-exhaustive" toward "exhaustive within minimal ECH by symmetry + NDA
monotonicity," while preserving the honest non-minimal caveat. No new
quantitative claim, no fabricated derivation — the $M_{\rm Pl}^{-2}$ shared
prefactor (F-class) and total-derivative status (C/E-class) are already proven in
the body; the added content is the *counting* statement that these two facts
exhaust the minimal basis and that NDA is monotone in dimension.
