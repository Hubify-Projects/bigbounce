# PROPAGATION NOTE → P1N lane

**From** `bb-LS13-p1n-essentials` · 2026-09-22
**Closes** DP1N-60, DP1N-61 (both ESSENTIAL) with derived science
**Evidence** `DERIVATION.md`, `outputs/eos_and_scales.json`, `MANIFEST.md`
**This lane did NOT edit** `main.tex`, SSOT, site data, or the disposition ledger.

---

## 0. Headline for the P1N lane

Both ESSENTIAL findings are **REAL and CONFIRMED**, but they land differently:

* **DP1N-60** — the reviewer is right that the equation of state is `w=+1`, not
  `w=-1`, and right that the repulsion-sign condition **inverts**. The paper's
  §II derivation is wrong in two places. **The paper's physical conclusion
  nevertheless survives**, because a second, independent sign error in §II
  cancels the first. §II must be **re-derived**, not reworded. **No title claim
  is withdrawn.**
* **DP1N-61** — the rebuttal does not hold at any scale the paper evaluates, and
  the cited source is misdescribed. **The "direct, quantitative rebuttal" claim
  must be WITHDRAWN** from §VII.D *and* from the abstract. This lane does not
  manufacture a replacement rebuttal.

**Readiness: must DROP from 95, not hold and not be restored.** See §5.

---

## 1. DP1N-60 — exact printable sentences for §II

Replace the sentence at `main.tex:213-224` beginning *"and it carries the same
repulsive sign at every finite $\gamma$"* through *"...the regime stated."*

### 1a. Preferred branch — corrected derivation kept, sign of the bilinear derived

Use this **only if** the P1N lane derives the sign of `⟨J_5^I J_{5I}⟩` in the
bounce configuration in-paper (Shifman–Vainshtein–Zakharov vacuum-saturation
contraction, not the square of a macroscopic polarization). Printable:

> and it carries the same repulsive sign at every finite $\gamma$. The contact
> term's contribution to the effective stress tensor is
> $\rho_{4\psi}=-\mathcal L_{4\psi}$; because Sec.~\ref{sec:theory}'s own
> parametrization fixes the magnitude of $\langle J_5^IJ_{5I}\rangle$ through a
> conserved fermion number density ($n_\psi\propto a^{-3}$, so
> $\rho_{4\psi}\propto a^{-6}$), covariant conservation against a separately
> conserved pressureless fermion fluid fixes
> $p_{4\psi}=\rho_{4\psi}=-\mathcal L_{4\psi}$ --- a stiff equation of state
> $w=+1$, not $w=-1$. This reproduces the standard
> Einstein--Cartan--Sciama--Kibble spin-fluid result
> $\varepsilon_{\rm spin}=p_{\rm spin}=-\kappa s^2/4$ for the identical
> interaction. A repulsive (halts collapse) contact interaction therefore
> requires $\rho_{4\psi}+3p_{4\psi}=-4\mathcal L_{4\psi}<0$, i.e.\
> $\mathcal L_{4\psi}>0$, i.e.\ $\langle J_5^IJ_{5I}\rangle<0$ in the
> mostly-plus convention used here. The expectation value that enters is the
> condensate contraction of the axial bilinear, not the square of a macroscopic
> polarization, and it carries that sign [derivation to be supplied in-paper];
> Eq.~\eqref{eq:4fermi}'s coefficient $-(3\kappa/16)\gamma^2/(1+\gamma^2)<0$
> then gives $\mathcal L_{4\psi}>0$ and a negative, stiff
> $\rho_{4\psi}$ --- the Einstein--Cartan bounce contribution.

### 1b. Fallback branch — bridge restated as an operator identification

Use this **if** the sign of `⟨J_5^I J_{5I}⟩` is not derived in-paper. This
withdraws the independent sign result while keeping the (untouched) operator
identification, and is fully acceptable. Printable:

> and it is the same operator: in the Einstein--Cartan limit
> Eq.~\eqref{eq:4fermi} reduces exactly to the Hehl--Datta term underlying
> Pop{\l}awski's bounce. We do not offer an independent sign-of-pressure
> argument here. For completeness we record the equation of state this term
> carries under Sec.~\ref{sec:theory}'s own parametrization: with
> $\rho_{4\psi}=-\mathcal L_{4\psi}$ and $\langle J_5^IJ_{5I}\rangle$ set by a
> conserved number density ($n_\psi\propto a^{-3}$), covariant conservation
> fixes $p_{4\psi}=\rho_{4\psi}$, a stiff $w=+1$ --- matching the standard
> Einstein--Cartan--Sciama--Kibble spin-fluid result
> $\varepsilon_{\rm spin}=p_{\rm spin}=-\kappa s^2/4$ --- so that repulsion
> requires $\rho_{4\psi}<0$. Establishing that sign requires the condensate
> contraction of the axial bilinear, which is outside the scope of this paper's
> channel-level assessment.

### 1c. Sentences that must be DELETED either way

* *"writing the contact term's contribution to the effective stress tensor as
  $\rho_{4\psi}=-\mathcal L_{4\psi}$, $p_{4\psi}=\mathcal L_{4\psi}$ for a term
  with no explicit time derivatives"* — the pressure sign is wrong; `w=-1` is
  wrong for the configuration §II.A parametrizes.
* *"a repulsive (halts collapse) contact interaction requires
  $\rho_{4\psi}+3p_{4\psi}<0$, i.e.\ $2\mathcal L_{4\psi}<0$, i.e.\
  $\mathcal L_{4\psi}<0$"* — the condition is `-4L_4ψ < 0`, i.e. `L_4ψ > 0`.
* *"gives $\mathcal L_{4\psi}<0$ whenever $(J_5^IJ_{5I})>0$, i.e.\ whenever
  $J^5$ is normalized spacelike ... the case realized by a spin-aligned fermion
  ensemble's axial current in the nonrelativistic, high-spin-density regime"* —
  this is the second sign error; the bounce-relevant contraction is not the
  square of a macroscopic polarization.

### 1d. What does NOT change

* The abstract's *"the same contact term supplying Pop{\l}awski's bounce
  mechanism as $\gamma\to\infty$"* — operator identification, untouched.
* The title's first half, *"What Minimal Einstein--Cartan Torsion Does for the
  Bounce"* — supported by the operator identification and by the corrected
  derivation, which still yields a repulsive stiff negative-energy contribution.
* `eq:4fermi`, `eq:ech_onshell_torsion`, `α`, `β`, `β/α=2.11`, the
  `γ²/(1+γ²)=0.053` suppression, and Sec. II.A's arithmetic — all verified
  correct and untouched.

---

## 2. DP1N-61 — exact printable sentences for §VII.D and the abstract

### 2a. §VII.D — the rebuttal is WITHDRAWN

Replace `main.tex:816-836` in full. Printable:

> Pop{\l}awski himself proposes a torsion-sourced cosmological constant from the
> same spin--spin contact interaction, with the present-day vacuum energy
> density set by the QCD quark chiral condensate: with
> $\langle0|\bar\psi\psi|0\rangle\approx-(230\,{\rm MeV})^3$ and
> Shifman--Vainshtein--Zakharov vacuum saturation he obtains
> $\langle0|\rho_\Lambda|0\rangle=(\kappa/3)\langle0|\bar\psi\psi|0\rangle^2
> \approx(54\,{\rm meV})^4$~\cite{Poplawski2012}, which he presents as agreement
> with the observed density to within a small factor in energy scale. That
> mechanism is set by a \emph{vacuum expectation value}, not by a cosmic fermion
> number density, and it therefore lies outside the Route~1 channel closed here:
> Sec.~\ref{sec:theory}'s benchmark bounds
> $\kappa n_\psi^2$ at an ISM-like number density, a scale some
> $74$ orders of magnitude below the condensate, and, as
> Sec.~\ref{sec:theory} itself notes, a number density does not fix the
> renormalized composite $\langle J_5^IJ_{5I}\rangle$ or a vacuum stress tensor.
> Nor does the sign result of Eq.~\eqref{eq:Gs} bear on his proposal, since the
> condensate he uses is generated by QCD dynamics rather than by the torsion
> coupling. We therefore make no claim to rebut Pop{\l}awski's condensate-based
> proposal; Route~1 as closed here concerns a late-time $\Lambda$-like density
> sourced by a cosmic fermion number density, and that channel is closed by the
> amplitude argument.

### 2b. Sentences that must be DELETED

* *"identifying the same spin--spin contact interaction that supports his bounce
  with a present-day vacuum energy density set by the average cosmic fermion
  (baryon) spin density"* — factually wrong description of `Poplawski2012`.
* *"That proposal maps directly onto \textbf{Route~1} ... evaluated at the
  cosmic fermion number density $n_\psi$ rather than at the collapsing-star
  density that sources the bounce."* — it does not map onto Route 1.
* *"This paper's negative result is accordingly not merely a generic no-go over
  an enumerated channel list but a direct, quantitative rebuttal of
  Pop{\l}awski's own stated dark-energy mechanism, evaluated in his own proposed
  channel at his own order of magnitude."* — **unsupported; withdraw entirely.**

### 2c. Abstract — the claim must come out

At `main.tex:88-91`, delete the clause *", rebutting Pop{\l}awski's own proposed
mechanism"*. The sentence then ends *"...to a late-time $\Lambda$-like
density."* No other abstract change is required by this item.

Optionally add, in the abstract's existing limitations sentence:

> We do not address torsion-induced vacuum energy sourced by a fermion
> condensate rather than by a cosmic number density.

### 2d. If the P1N lane instead wants to keep a rebuttal (NOT recommended)

A rebuttal at the correct scale is *possible* but is a different argument: at the
condensate the mechanism **over**-produces by `~2–3×10⁵` in density (`~21–24×` in
energy scale; this lane reproduces Popławski's own `(54 meV)⁴` to 3 s.f.). That
is a far weaker objection than the `10⁻⁶⁹` under-production currently claimed,
and it is an objection Popławski himself addresses (he proposes leptonic
contributions to lower the scale). **This lane recommends withdrawal, not
substitution**, and did not derive a replacement rebuttal. Any such argument must
be derived before it is printed.

---

## 3. Hygiene consequences (directive G)

Both edits are text-only. The directive-I6 figure-image propagation sweep is
**trivially not triggered**: `main.tex` contains **zero** `\includegraphics`
calls (verified by grep), so no numeric can be baked into a figure asset. The edits do
require the normal per-round cycle: bump `\paperVersion` + `\date`, recompile to
0 undef-refs, `/latex-audit`, three-way byte-identical PDF re-mirror, and the
Convex `paperVersions:bump` **queued** in
`project-context/CONVEX_BACKFILL_QUEUE_2026-09-21.md` (Convex disabled).

Word-count note: §2a is shorter than the text it replaces; §1a/§1b are
comparable. No venue-form consequence for CQG.

---

## 4. Ledger lines for `DISPOSITIONS/P1N.md`

* **DP1N-60** → `CONFIRMED REAL, closure derived, OPEN pending §II re-derivation`.
  Equation of state is `w=+1` (stiff), not `w=-1`; `ρ_4ψ = -L_4ψ` correct,
  `p_4ψ = +L_4ψ` wrong; `ρ+3p = -4L_4ψ`, so repulsion requires `L_4ψ > 0` — the
  condition **inverts**. A second, independent sign error (the sign assigned to
  `⟨J_5·J_5⟩` for the bounce configuration) cancels the first, so the paper's
  physical conclusion is right and its derivation is not. Title claim survives;
  §II must be re-derived. Evidence: `research/ech_contact_term_2026_09_22/`.
* **DP1N-61** → `CONFIRMED REAL, WITHDRAWAL required`. `Poplawski2012` is the
  QCD quark-condensate paper; its `ρ_Λ = (κ/3)⟨q̄q⟩² ≈ (54 meV)⁴` is reproduced
  here to 3 s.f. §VII.D evaluates `κn_ψ²` at `100 cm⁻³`, `10^73.9` in density
  away, and the gap-equation leg does not address his mechanism either. The
  "direct, quantitative rebuttal" claim is unsupported in §VII.D and in the
  abstract and must be withdrawn. Evidence: same directory.
* Note alongside both: the adversarial "57-order-of-magnitude unit error" on
  `κn_ψ²` is **re-falsified a fourth time** — `9.954×10⁻⁸⁰ eV⁴` and
  `3.884×10⁻⁶⁹` reproduce to 4 s.f. from first principles.

---

## 5. Readiness recommendation — plainly

**Readiness 95 cannot be restored toward 99, and must DROP further. Recommend
88, SIGN-OFF HOLD retained.**

Reasoning, against directive P's composition:

* **Science closure (25):** two ESSENTIAL items confirmed real on the current
  exact PDF. One requires re-deriving a mechanism paragraph that supports half
  the title; the other requires withdrawing a claim from the abstract. Neither
  is packaging. This component is not complete. → **drop**
* **Automated review convergence (25):** the CONFIRM board surfaced
  genuinely-new real findings and this lane has now confirmed both. The
  clean-wave clock for P1N **resets**; convergence cannot be claimed on the
  current text. → **drop**
* **Evidence & reproducibility (25):** unaffected and in fact improved — this
  lane adds a Q2 manifest and a self-validating script. `DP1N-58` (Zenodo DOI)
  remains the only other open item. → hold
* **Packaging & PDF hygiene (20):** unaffected; will need the normal
  directive-G cycle after the edits. → hold
* **Houston's final personal review (5):** not reached. → 0

88 is the honest floor that reflects two open ESSENTIAL science items with
written closure instructions and verified evidence, against a paper whose other
four components are sound. After both edits land, recompile clean, and a fresh
exact-version board runs on the new PDF, P1N can climb back — but it must not
re-enter sign-off on the strength of this lane alone, because §1a leaves a
sign this lane did not itself re-derive.

**What would make it worse.** If the P1N lane takes branch **1b** (bridge
restated as operator identification only) *and* the withdrawal in §2, the paper
loses one supporting argument in each half of its title. That is still a
publishable, honest paper — but the abstract's dichotomy framing should be
re-read end-to-end for overclaim before any readiness uplift.

**What would make it better.** Deriving `⟨J_5^I J_{5I}⟩`'s sign in-paper
(branch **1a**) turns DP1N-60 from a retreat into a strengthened §II that
explicitly reproduces the ECSK spin-fluid result — a net gain over `v1N.0.7`.

---

## 6. Flagged, not claimed — needs its own lane

The manuscript's Fierz row (`eq:fierz_row`) assigns the scalar channel
coefficient `+1` and calls it signature-independent; that row is what produces
`G_s = -(3κ/16)γ²/(1+γ²) < 0` and hence the NJL no-condensate result, a separate
headline claim. Its sign consistency with the vacuum-saturation contraction used
in §1.7 above was **not** checked by this lane and is **not** asserted to be
wrong. It should be checked, because if it did flip, `G_s` would flip with it.
