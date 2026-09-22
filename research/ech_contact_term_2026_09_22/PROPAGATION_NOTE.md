# PROPAGATION NOTE → P1N lane

**From** `bb-LS13-p1n-essentials` · 2026-09-22
**Closes** DP1N-60, DP1N-61 (both ESSENTIAL) with derived science
**Evidence** `DERIVATION.md`, `outputs/eos_and_scales.json`, `MANIFEST.md`
**This lane did NOT edit** `main.tex`, SSOT, site data, or the disposition ledger.

---

## 0. Headline for the P1N lane

Both ESSENTIAL findings are **REAL and CONFIRMED**, and both cost the paper a
claim:

* **DP1N-60** — the reviewer is right that the equation of state is `w=+1`, not
  `w=-1`, and right that the repulsion-sign condition **inverts**. Worse than
  the reviewer stated: with the manuscript's *own* stated configuration
  (spin-aligned Dirac ensemble, spacelike `J⁵`, mostly-plus) the corrected
  equation of state makes the contact term gravitationally **attractive** — which
  is the published Kerlick (1975) / O'Connell (1977) ECSK result for the Dirac
  field. §II's *"carries the same repulsive sign at every finite γ"* is
  **unsupported and must be withdrawn**. The `γ→∞` operator identification is
  untouched and the title need not change if §II retreats to it.
* **DP1N-61** — the rebuttal does not hold at any scale the paper evaluates, and
  the cited source is misdescribed. The **"direct, quantitative rebuttal" claim
  must be WITHDRAWN** from §VII.D *and* from the abstract. This lane does not
  manufacture a replacement rebuttal.

**Readiness: must DROP from 95, not hold and not be restored. Recommend 85.**
See §5.

> **Correction recorded.** An earlier draft of this note argued that a second
> sign error in §II cancelled the first, so that the paper's conclusion survived
> intact. A blind-adjudication leg surfaced the Kerlick/O'Connell result and that
> reading is now withdrawn. The recommendation moved from 88 to 85 as a result.

## 1. DP1N-60 — exact printable sentences for §II

Replace the sentence at `main.tex:213-224` beginning *"and it carries the same
repulsive sign at every finite $\gamma$"* through *"...the regime stated."*

### 1a. Required branch — sign argument withdrawn, operator identification kept

Replace the sentence at `main.tex:213-224` beginning *"and it carries the same
repulsive sign at every finite $\gamma$"* through *"...the regime stated."*
Printable:

> and it is the same operator: in the Einstein--Cartan limit
> Eq.~\eqref{eq:4fermi} reduces exactly to the Hehl--Datta term underlying
> Pop{\l}awski's bounce. We do not offer an independent sign-of-pressure
> argument here, and we do not claim to establish that minimal ECH torsion
> supplies the repulsive branch of that bounce at finite $\gamma$. For
> completeness we record the equation of state this term carries under the
> parametrization used below: with $\rho_{4\psi}=-\mathcal L_{4\psi}$ and
> $\langle J_5^IJ_{5I}\rangle$ set by a conserved number density
> ($n_\psi\propto a^{-3}$, so $\rho_{4\psi}\propto a^{-6}$), covariant
> conservation against a separately conserved pressureless fermion fluid fixes
> $p_{4\psi}=\rho_{4\psi}$ --- a stiff equation of state $w=+1$, matching the
> standard Einstein--Cartan--Sciama--Kibble spin-fluid result
> $\varepsilon_{\rm spin}=p_{\rm spin}=-\kappa s^2/4$ --- so that a repulsive
> contribution requires $\rho_{4\psi}+3p_{4\psi}=-4\mathcal L_{4\psi}<0$, i.e.\
> $\mathcal L_{4\psi}>0$. Whether the medium expectation value
> $\langle J_5^IJ_{5I}\rangle$ realizes that branch is configuration dependent
> and remains contested for the Dirac field, whose totally antisymmetric spin
> density gives an \emph{attractive} contact
> interaction~\cite{Kerlick1975,OConnell1977} while a semiclassical Weyssenhoff
> spin fluid gives a repulsive one; settling it is outside this paper's
> channel-level scope.

Two `references.bib` entries are needed:

```bibtex
@article{Kerlick1975,
  author = {Kerlick, G. D.},
  title = {Cosmology and particle pair production via gravitational
           spin-spin interaction in the Einstein--Cartan--Sciama--Kibble
           theory of gravity},
  journal = {Phys. Rev. D}, volume = {12}, pages = {3004}, year = {1975},
  doi = {10.1103/PhysRevD.12.3004}
}
@article{OConnell1977,
  author = {O'Connell, R. F.},
  title = {Attractive spin-spin contact interactions in the
           Einstein--Cartan--Sciama--Kibble torsion theory of gravitation},
  journal = {Phys. Rev. D}, volume = {16}, pages = {1247}, year = {1977},
  doi = {10.1103/PhysRevD.16.1247}
}
```

### 1b. Branch that would RESTORE the stronger claim (optional, real work)

Only if the P1N lane derives `⟨J_5^I J_{5I}⟩`'s sign in-paper for the bounce
configuration and it comes out negative in mostly-plus, may §II reinstate a
repulsion claim — and it must then explicitly engage Kerlick/O'Connell rather
than pass over them. This lane did **not** derive that sign and does not
assert it. **Do not print a repulsion claim without that derivation.**

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
  this configuration, fed through the *corrected* equation of state, yields
  `ρ_4ψ > 0` and therefore **attraction**, i.e. the opposite of what §II
  concludes from it, and matches Kerlick/O'Connell for the Dirac field. It
  cannot be kept as a premise of a repulsion claim.
* *"it carries the same repulsive sign at every finite $\gamma$"* — withdraw.
  The `γ→∞` operator identification is what survives, and it is a separate,
  algebraic statement.

### 1d. What does NOT change

* The abstract's *"the same contact term supplying Pop{\l}awski's bounce
  mechanism as $\gamma\to\infty$"* — operator identification, untouched.
* The title *"What Minimal Einstein--Cartan Torsion Does for the Bounce and
  Cannot Do for Dark Energy"* — the first half is carried by the operator
  identification and by §II.A's finite-density benchmark, both untouched. The
  title need not change; the abstract must stop claiming a *repulsive sign*
  result. **Re-read the abstract's "positive/negative dichotomy" framing
  end-to-end for overclaim once §II retreats.**
* `eq:4fermi`, `eq:ech_onshell_torsion`, `α`, `β`, `β/α=2.11`, the
  `γ²/(1+γ²)=0.053` suppression, and Sec. II.A's arithmetic — all verified
  correct and untouched.
* The perturbation-transparency theorem (the paper's sole Tier-I rigorous
  result), the 14-barrier catalog, the operator list, and the amplitude
  closures — untouched by this item.

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

* **DP1N-60** → `CONFIRMED REAL, closure derived, WITHDRAWAL required`.
  Equation of state is `w=+1` (stiff), not `w=-1`; `ρ_4ψ = -L_4ψ` correct,
  `p_4ψ = +L_4ψ` wrong; `ρ+3p = -4L_4ψ`, so repulsion requires `L_4ψ > 0` — the
  condition **inverts**. Taken with the manuscript's own stated configuration
  (spin-aligned Dirac ensemble, spacelike `J⁵`), the corrected EOS gives a
  positive stiff `ρ_4ψ` and therefore **attraction** — the published Kerlick
  (PRD 12, 3004, 1975) / O'Connell (PRD 16, 1247, 1977) ECSK result for the
  Dirac field. §II's "carries the same repulsive sign at every finite γ" is
  unsupported and must be withdrawn; the `γ→∞` operator identification stands.
  Verified by two independent derivations (this lane + a blind adjudicator given
  neither conclusion nor method). Evidence:
  `research/ech_contact_term_2026_09_22/`.
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
85, SIGN-OFF HOLD retained.**

Reasoning, against directive P's composition:

* **Science closure (25):** two ESSENTIAL items confirmed real on the current
  exact PDF. Both require *withdrawing* a printed claim — one from §II (the
  repulsive-sign bridge), one from §VII.D **and the abstract** (the Popławski
  rebuttal). Neither is packaging; neither is a reword. → **drop hard**
* **Automated review convergence (25):** the CONFIRM board surfaced
  genuinely-new real findings and this lane confirms both, with a third
  independent leg agreeing. P1N's clean-wave clock **resets**; convergence
  cannot be claimed on the current text. → **drop**
* **Evidence & reproducibility (25):** unaffected, and improved — this lane adds
  a Q2 manifest and a self-validating script. `DP1N-58` (Zenodo DOI) remains the
  only other open item. → hold
* **Packaging & PDF hygiene (20):** unaffected; needs the normal directive-G
  cycle after the edits. → hold
* **Houston's final personal review (5):** not reached. → 0

**85, not 88.** An earlier draft of this note recommended 88 on the reading that
§II's conclusion survived through compensating errors. The blind-adjudication
leg surfaced Kerlick/O'Connell and that reading is withdrawn: §II now loses a
claim rather than merely a derivation, so the science-closure component takes a
larger hit. 85 is the honest floor for a paper whose Tier-I theorem, barrier
catalog, operator list and amplitude closures are all sound, but which must
retract one supporting claim in each half of its title framing.

**This is not a collapse.** Nothing here touches the perturbation-transparency
theorem, the 14-barrier catalog, the operator-list argument, §II.A's benchmark,
or the amplitude closures. P1N remains a publishable, honest paper after both
withdrawals — a *narrower* one. After the edits land, recompile clean, and a
fresh exact-version board runs on the new PDF, P1N can climb back.

**What would raise it further.** Deriving `⟨J_5^I J_{5I}⟩`'s sign in-paper
(branch §1b) and engaging Kerlick/O'Connell explicitly would turn DP1N-60 from a
retraction into a strengthened §II that reproduces the ECSK spin-fluid result and
takes a defensible position on a known open tension. That is real new science and
should be scoped as its own lane, not bolted onto a text edit.

## 6. Flagged, not claimed — needs its own lane

The manuscript's Fierz row (`eq:fierz_row`) assigns the scalar channel
coefficient `+1` and calls it signature-independent; that row is what produces
`G_s = -(3κ/16)γ²/(1+γ²) < 0` and hence the NJL no-condensate result, a separate
headline claim. Its sign consistency with the vacuum-saturation contraction used
in §1.7 above was **not** checked by this lane and is **not** asserted to be
wrong. It should be checked, because if it did flip, `G_s` would flip with it.
