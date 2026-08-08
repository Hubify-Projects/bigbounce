# P1C v1C.0.12 — Independent Referee Report (Claude leg, R10 convergence round)

**Manuscript:** `arxiv/paper1c_nogo_survey/main.pdf` — *A Structural No-Go Survey of Minimal
Spin-Torsion Routes to Dark Energy and Bounce Phenomenology*, H. Golden, dated
August 7, 2026 (v1C.0.12), 22 pages.
**SHA-256 (verified before reading):** `c21fde9f1b69e147ae6d27aeb27ec09189530a731331a4dc8a1e6c5d83d62982` — **MATCHES** the assigned hash.
**Date of review:** 2026-08-07
**Role:** independent, skeptical journal referee at CQG calibre. No prior exposure to this
manuscript or to any prior referee report on it. Review conducted fresh from the PDF.
**Consistency sources consulted (read-only):** `research/theory_audit/operator_basis_adjudication_2026_08_07.md`,
`arxiv/scripts/dim4_parityodd_enumeration.py` (tag inventory only), repository git objects
(for the pinned-commit provenance claim). No file was modified; nothing was committed or pushed.

**Accuracy protocol observed.** Every candidate printed-math error was re-rendered at
300–400 DPI (`pdftoppm -r 300..400`) and re-read before being asserted. Four candidate
findings were raised by low-DPI text extraction and **withdrawn** after re-rendering:
(i) `ρ_crit = 3/(32π²γ³)ρ_Pl` — the printed formula carries the **√3** (p. 5), and √3 is the
value that reproduces both quoted endpoints (0.409 at γ=0.2375; 0.267 at γ=0.274);
(ii) `|t₃| ∼ m_T⁻¹` — the printed relation is **√|t₃| ∼ m_T⁻¹** (p. 4), which is what makes
`g_eff ∼ 1/(M_Pl√|t₃|) ∼ H₀/M_Pl` consistent;
(iii) `T_abc T^abc = −(8/3)κ²(J⁵·J⁵)` — printed value is **−(3/8)κ²** (p. 18), which is correct;
(iv) an apparent `ε_{0123}=+1` vs `ε^{0123}=+1` clash between Sec. V and Check D — both
print `ε^{0123}=+1`. None of these is a defect.

---

## VERDICT

**MAJOR REVISION — no computational error found; both MAJOR findings are claim-scoping
defects.** Every checkable displayed equation reproduced independently, several to three
significant figures. The manuscript's quantitative spine is sound and its self-labelling of
evidentiary tiers is unusually disciplined. What blocks acceptance as written are two places
where an asserted closure reaches beyond the computation that supports it, both of which
touch headline claims (the "13 distinct constraints" count and the "all four channels close"
statement). Both are fixable by rewording plus, for MAJOR-2, either a supporting argument or
an explicit downgrade of the Route-2 dark-energy leg.

---

## INDEPENDENT VERIFICATION PERFORMED (what I re-derived, not merely read)

Reported so the board can see the base against which the findings below are calibrated.
All of the following **PASS**:

| Object | Anchor | Result |
|---|---|---|
| `ε_{abcd}ε^{abce} = −3!δ^e_d` (mostly-plus, ε^{0123}=+1) | Check D, p. 18 | exact, brute-forced over all 4⁴ index pairs |
| `S_abc S^abc = −(3/8)(J⁵·J⁵)`; `T_abc T^abc = −(3/8)κ²(J⁵·J⁵)` | Check D, p. 18 | exact, symbolic |
| `O5 → −(3/2)κ(J⁵·J⁵)` under `T=κS` | Eq. (9)/(11), Table III | exact, symbolic (`ε^{abcd}T_{cab}J_d`) |
| `O4 ≡ 0` on pure-axial torsion; `= 0` on pure-vector; `≠ 0` only on vector×axial and tensor irreps | Table III, App. A 1 | exact, symbolic — reproduces the audit's `[L81]–[L86]` |
| `2O1 + 2O2 − O4 = 0`, i.e. `O1 = ½O4 − O2` | Eq. (11) | derived analytically from `d(e_I∧T^I) = T_I∧T^I − e_I∧e_J∧R^{IJ}` in the Eq. (10) density normalization — **the printed rational coefficients are exactly right**, including the factor 2 that a form-vs-density slip would spoil |
| `O1 = O6` (tetrad conversion) | Eq. (11) | trivially exact |
| Rank-4 / nullity-2; `{O2,O3,O4,O5}` and `{O1,O3,O4,O5}` independent; rank 2 mod total derivatives | Sec. V | consistent with the released adjudication and with the null space I derived |
| `F_c² = 1` for the printed 5×5 Fierz matrix | Eq. (C1), p. 19 | **exact identity** with the printed ½ entries — the matrix as typeset is involutory |
| Axial row → operator row `(1, ½, 0, ½, −1)` ⇒ Eq. (C2) | Eq. (C2) | consistent |
| `Q_γ Q_γ⁻¹ = 1` with `⋆² = −1` | Eq. (E1) | exact |
| `4πG = κ/2`; `−(3/2)πG = −3κ/16` | Eq. (E3)/(E4) | exact |
| `κn_ψ² ≃ 1.0×10⁻⁷⁹ eV⁴` at 100 cm⁻³; `/ρ_Λ ≃ 3.6×10⁻⁶⁹` (2.3 meV) and `3.9×10⁻⁶⁹` (2.25 meV); 3/16-corrected `1.9×10⁻⁸⁰ eV⁴ = 6.7×10⁻⁷⁰ ρ_Λ`; "≈68.4 orders" | Eq. (E5), Table II | all reproduce to 2 s.f. |
| `M_Pl⁴/ρ_Λ^obs = 8.7×10¹²²`; bare-power variant 10¹²⁴; `N_tot = 122 ln10/3 ≈ 94` | App. A | exact |
| Eq. (2) canonical: `10⁻³·10⁻⁶¹/(10⁻²·6×10⁻³) ≈ 1.7×10⁻⁶⁰`; direct contraction `≈1.7×10⁻⁶²`; `β_obs = 0.342° = 5.97×10⁻³ rad`; `α_em/4π = 5.8×10⁻⁴` | Sec. IV A | all correct, and 10⁻⁶⁰ is indeed the conservative side |
| Eq. (5): `0.3 × 1.18×10⁻⁶¹ = 3.5×10⁻⁶²` (~61 orders); `1.4×10⁻⁶ × 1.18×10⁻⁶¹ = 1.7×10⁻⁶⁷` (~67 orders); `H₀/M_Pl = 1.18×10⁻⁶¹` | Sec. IV B | exact |
| **Eq. (4) integrated**: `Δγ² = [(1−γ²)(23γ²+5)/(8π)²]·16π·(μ_UV²/2M_Pl²)` at γ=0.24, μ_UV=10¹⁶ GeV, full `M_Pl` ⇒ **`|Δγ/γ| = 1.38×10⁻⁶`** | Sec. IV B | reproduces the paper's `1.4×10⁻⁶` — this is a genuinely derived number, as claimed |
| Eq. (3) integration: `Δlnγ = 30–37/(12π²) = 0.25–0.31`; `32/(12π²)=0.270`; exponentiated `0.28–0.36`; `ln10¹⁶=36.8`, `ln10¹³=29.9` | Sec. IV B | exact |
| `\|Ω₄₄/α₄\| = (378+783γ²)/[120(1+γ²)]`, `=3.33` at γ=0.24, monotone, infimum `378/120=3.15`, `4.84` at γ=1 | Sec. IV A | algebra and numerics both correct |
| `(ρ_crit/ρ_Pl)² = 0.073–0.168` from `0.27–0.41`; `√3/(32π²γ³)` at γ=0.2375 → 0.409, at γ=0.274 → 0.267 | B12 | exact |
| `(M_Pl/H₀)² ∼ 10¹²²`; `α/M ∼ 2β_obs/M_Pl ∼ 9.8×10⁻²² GeV⁻¹`; `M_Pl(α/M) = 1.2×10⁻²`; `√(2ρ_Λ)/H₀ ∼ 0.4 M_Pl` | B1, Sec. IV C | all consistent |
| Holst term on Levi-Civita → `(1/2γ)ε^{μνρσ}R_{μνρσ}` | App. D step 4 | exact in the density normalization I derived independently |
| Dimension bookkeeping of Eq. (1): `−1+2+3 = +4`; Eq. (A1) `[L_odd]=+1`; Table III dim column (2,2,4,2,4,2) | Secs. IV A, V, App. A | internally consistent |
| Fig. 1 arrow multiplicities vs. per-barrier `[Rn]` tags (R1←3, R2←4, R3←4, R4←3) | Fig. 1 / Sec. III A | consistent |
| Entry accounting: 9 novel + 4 known + 1 structural = 14; 7 foundations + 7 branch entries = 14; five general-naturalness entries (B5–B7, B10, B13) quoted identically in Sec. III, Fig. 1 caption and Sec. VI | throughout | consistent |
| Provenance: commit `1130b7c5e3d2` exists; all six named files byte-identical at pin, at HEAD, and on disk | Data & Code Availability | **claim is true as stated** |
| Bibliography: all 25 entries correspond to real, correctly-attributed works; `0.342°±0.094°` (Eskilt–Komatsu), `0.35°±0.14°` (Minami–Komatsu), `0.215°±0.074°` (ACT DR6) and the quoted 3.6σ/2.9σ are internally consistent | Refs. [1]–[25] | no fabricated or mis-numbered reference found |
| LaTeX hygiene | `main.log` | **zero Overfull hboxes**; underfull only. No column overflow observed in any rendered page. |

---

## MAJOR FINDINGS

### MAJOR-1 [correctness] — The sole Tier-I leg (B14) is proved only on the zero-spin / canonical-scalar branch, yet is asserted to subsume B8 and to constrain R1. The headline "13 distinct constraints" count rests on that subsumption.

**Anchors:** Appendix D *Statement* (p. 20); Appendix D *Consequences carried into the catalog*
(p. 20); B8 entry (p. 5); B14 entry (p. 6); Table I note (p. 4); Fig. 1 caption edge label
"B8, B14" (p. 4); Sec. III ¶"We tested 7 foundation mechanism classes…" (p. 3); abstract;
Sec. VI *What is established*; Sec. VII.

Appendix D's theorem is scoped explicitly and correctly: *"Consider the classical ECH action
with an invertible tetrad, **canonical scalar matter**…"*, with the exclusion list *"…quantum
loops or anomalies, **fermion sources**, non-minimal matter, a dynamical Immirzi field, and
propagating torsion are outside this statement."* Step (1) of the proof is literally *"A
canonical scalar field has zero spin density"*, which is what drives `T^I = 0` in step (2).
Table II states the same restriction and even records that the theorem *"Excludes
propagating-torsion, **fermion-loop**, dynamical-Immirzi, non-minimal-matter sectors."*

But B8 is a statement about the **fermionic** sector: *"The spin-torsion interaction `(J⁵)²` is
parity-even … so it cannot generate tensor chirality in primordial gravitational waves;
independently confirmed by the perturbation-transparency result (B14)."* On the branch where
`(J⁵)²` exists at all, `T = κS ≠ 0` and Appendix D's hypotheses fail. B14 therefore cannot
"independently confirm" B8, and — more consequentially — **B14 does not subsume B8**: a
theorem whose hypothesis is "zero spin density" carries no information about a channel whose
defining object is a nonzero spin current. The two are logically independent statements about
disjoint matter sectors that happen to concern the same observable (tensor chirality).

The same defect propagates to the route map. B14 is tagged `[R1–R4]` (p. 6) and Fig. 1 draws
Branch H to all four routes, with the caption asserting the R1 arrow is *"driven by B8 and
B14 together"*. R1 is the NJL four-fermion contact channel; R3 is driven by chiral fermion
loops. Under Appendix D's own exclusions, B14 bears on neither.

**Why this is MAJOR rather than a wording nit.** The manuscript's headline arithmetic is
"14 historical entries → **13** distinct mechanism-class constraints, B8 subsumed by B14."
That sentence appears in the abstract, in the Table I note, in the Fig. 1 caption, in Sec. III,
in Sec. VI and in Sec. VII. If the subsumption does not hold, either the count is 14 (and the
paper's own criterion — *"no barrier is a logical consequence of another"* — is satisfied by
B8 and B14 being independent), or the paper must supply the fermion-branch extension that
would make B14 imply B8. The manuscript is elsewhere scrupulous about not over-claiming; this
is the one place where a Tier-I label is spent outside the theorem's stated domain.

**Requested action (any one of):** (a) restore B8 as a 14th distinct constraint and adjust
every count; (b) retain the subsumption but supply the nonzero-spin-branch extension of the
transparency theorem that licenses it, and say where it is proved (the companion's cited
"tensor-sector extension" is itself a *zero-spin-branch* result, so it does not serve); or
(c) keep the count but replace "subsumes" with an explicit statement that B8 and B14 close the
*same observable channel on disjoint matter branches* and are merged for presentational, not
logical, reasons — and correspondingly restrict B14's route tag from `[R1–R4]` to the branch
its hypotheses cover, redrawing the Fig. 1 edge label.

---

### MAJOR-2 [correctness] — Route 2's dark-energy closure is delegated to the Sec. V / App. A operator list, but Eq. (1) is not in that list's scope: it is a dimension-5 operator built on a light pseudoscalar the construction rule excludes.

**Anchors:** Sec. IV head, *"Route 2's dark-energy closure is not computed in that subsection;
it is inherited from the operator-list argument of Sec. V and the single-scale NDA bound of
App. A, which bound every local dimension-four parity-odd density admitted by the
minimal-coupling field content"* (p. 6); Sec. IV A, *"…the class into which Eq. (1) falls…
(The dimension-(+1) object bounded directly in App. A is the phenomenological representative
Eq. (7), not Eq. (1), which as shown below already carries dimension +4 with no deficit.)"*
(p. 7, verified at 400 DPI); Eq. (1) and its dimension count (p. 7); Sec. V *Construction
rule* (p. 12); App. A 1 ¶1 (p. 18); App. A *Residual assumption* (p. 17); Sec. VI, Sec. VII.

Three independent reasons Eq. (1) is outside the operator list's span:

1. **It is a dimension-5 operator, not a dimension-4 one.** The paper computes this itself on
   p. 7: *"the **dimension-(+5) integrand** `∂_μϑ_NY J^{5μ}` times the dimension-(−1)
   prefactor `β(γ)/M_Pl`."* Sec. V bounds *"densities of mass dimension **exactly four**"*,
   and Eq. (9) fixes each `O_n^{[4]}` so that its Wilson coefficient is **dimensionless**.
   Eq. (1)'s coefficient is `β(γ)/M_Pl`, of dimension −1. The parenthetical defence —
   Eq. (1) *"already carries dimension +4 with no deficit"* — conflates the total dimension of
   a Lagrangian **term** (necessarily +4 for any well-formed term, including every irrelevant
   operator) with the **operator** dimension that Sec. V uses as its classification key. Read
   correctly, Eq. (1) is a dimension-5 operator suppressed by one power of `M_Pl` — which is
   why it is *not* in a dimension-4 list.

2. **`ϑ_NY` is not in the admitted field content.** Sec. V's construction rule admits exactly
   *"the tetrad `e^I_μ` (with the invariant tensors `ε` and `η`), the curvature two-form of the
   torsionful connection, the algebraically-fixed torsion `T = κS`, and the minimal axial
   current `J⁵`"*. A dimension-(+1) pseudoscalar `ϑ_NY(x)` is none of these. App. A 1 is even
   more explicit: *"No new light scale `μ ≪ M_Pl`, **no dynamical Immirzi field**, no
   propagating torsion, and no non-minimal (trace/tensor) torsion irreps are admitted, as these
   lie outside the stated minimal scope."* `ϑ_NY` is precisely the Mercuri-type promoted
   pseudoscalar the paper cites [8] for and elsewhere places outside scope.

3. **It carries an extra derivative.** The rule requires densities *"formed at zero additional
   derivative order (no derivatives beyond those internal to `R` and `T`)"*. `∂_μϑ_NY` is an
   additional derivative on a field that is itself not admitted.

Worse, the manuscript assigns `ϑ_NY` a cosmological background `⟨∂_μϑ_NY⟩ ∼ H₀²` *"evolving on
the Hubble time"* (p. 7) — i.e. a field with mass `≲ H₀`. That is exactly the *"new light scale
`μ ≪ M_Pl`"* which App. A names as the one thing that **evades** the single-scale NDA bound
(*"A non-minimal UV completion introducing a new light scale `μ ≪ M_Pl` … could evade the
estimate"*). So the operator whose dark-energy closure is being delegated to the NDA bound is
built on the very structure the NDA bound declares outside its reach. The delegation is not
merely unsupported; it points the wrong way.

**Consequence.** Sec. VI (*"Two of those channels (R2, R3) are closed here at the
amplitude-budget level"*) and Sec. VII (*"all four enumerated channels close"*) rest, for
Route 2's **dark-energy** leg, on this inheritance. Sec. IV A is explicit that no dark-energy
amplitude is computed for Route 2 anywhere in the manuscript. As written, Route 2's dark-energy
closure has no supporting computation in this paper.

**Requested action (any one of):** (a) supply the bound directly — extend the enumeration to
dimension-5 parity-odd operators containing one light pseudoscalar, or give a separate NDA
argument for `(β(γ)/M_Pl)∂_μϑ_NY J^{5μ}` against `ρ_Λ` (this looks straightforward and would be
the strongest fix); (b) drop the delegation and state plainly that Route 2 is closed **only**
against the birefringence channel in this survey, with the dark-energy leg deferred — and
correct Sec. VI/VII's "all four channels close" accordingly; or (c) if `ϑ_NY` is meant to be a
composite of the minimal fields rather than an independent pseudoscalar, define it as such
explicitly, and reconcile that definition with its assigned mass dimension +1, its Hubble-scale
background, and App. A 1's exclusion of a dynamical Immirzi field.

---

## MINOR FINDINGS

**MINOR-1 [correctness] — "each of which could only suppress the estimate further" is false for `β(γ)`.**
Sec. IV A, Eq. (2) discussion (p. 7): *"the one-loop factor `1/16π²` and the O(1) coefficient
`β(γ)`, **each of which could only suppress the estimate further**, are conservatively
dropped."* By the paper's own characterization two paragraphs earlier, `β(γ)` sits in the
`α₄/Ω₄ₓ` family with `|Ω₄₄/α₄| ≈ 3.3` at γ≈0.24, *"O(3)–O(5) across γ ≲ O(1)"*, and *"bounded
below by 378/120 ≈ 3.2 for all real γ"* — I confirm the ratio is monotone in γ² with infimum
3.15 and value 4.84 at γ=1. A factor >1 dropped from a numerator **raises** the estimate; it
cannot "only suppress" it. The *combined* omission is still net-conservative (the `1/16π²`
supplies −2.2 orders against `β(γ)`'s +0.5), so the ≥58-order margin and every downstream
number are unaffected — but the per-factor justification as printed is wrong and should read,
e.g., "whose net effect is a further suppression of roughly 1.5 orders."

**MINOR-2 [presentation] — residual "basis" language contradicts the paper's own corrected terminology.**
The manuscript now insists, correctly and in several places, that `{O1–O6}` is *"a spanning
list, not a basis"* / *"a generating set"*. But "basis" survives for the same object at:
`main.tex:1515` (*"already a member of the basis below"*, PDF p. 12), `1527`/`1529`
(*"Shorthand and its relation to the **basis**… representative of the dimension-4 **basis**"*,
p. 12), `2008`/`2012` (*"the finite operator **basis** fixed by the algebraic Cartan
constraint… bounds every member of the **basis**"*, p. 17), `2057`/`2060` (*"an operator-**basis**
closure… we exhibit that **basis**"*, p. 17). A referee reading only Sec. V will be told both
things. (Fierz-sector uses of "basis" at `1287`, `1674`, `2142`, `2292`, `2295`, `2311`, `2336`
are legitimate — the Clifford/`{SS,VV,AA,PP}` set genuinely is a basis — and should be left
alone; only the `{O1–O6}` occurrences need changing.)

**MINOR-3 [presentation] — tautological parenthetical.**
App. A, `main.tex:2016–2017` (PDF p. 17): *"Inflationary dilution (`𝒟_inf ∼ e^{−3N_tot}`, with
`𝒟_inf ≡ e^{−3N_tot}`) then yields…"* — the parenthetical restates its own antecedent, once
with `∼` and once with `≡`. Delete one.

**MINOR-4 [presentation] — the metric signature is cross-referenced to a section that does not state it.**
Sec. V, note under Eq. (9) (p. 12): *"`ε^{0123} = +1` (**mostly-plus signature, Sec. II**)"*,
and Check D (p. 18) repeats *"the Lorentzian (mostly-plus, `ε^{0123}=+1`) contraction"*. But
Sec. II (`main.tex:412`) says only *"Signs, signature, and index conventions follow the
companion paper's setup [1]"* — the string "mostly-plus" occurs nowhere in Sec. II. Since the
signature is load-bearing for `ε_{abcd}ε^{abce} = −3!δ^e_d` and hence for the `−3/8` and `−3/2`
coefficients, and since the manuscript's stated aim is that a referee can verify the
quantitative claims *"from this manuscript alone"*, Sec. II should state `η = diag(−,+,+,+)`
and `ε^{0123}=+1` outright.

**MINOR-5 [correctness] — citation [8] is mis-scoped in one sentence.**
Sec. IV A opening (p. 6): *"…with the Holst sector developing running couplings analyzed via
renormalization-group methods in Einstein–Cartan + Holst gravity [2, 8]."* Ref. [8] is
Mercuri, *Peccei–Quinn mechanism in gravity and the nature of the Barbero–Immirzi parameter*,
PRL **103**, 081302 (2009) — a classical construction, not an RG analysis. The manuscript
itself says so two sentences later (*"those works establish the classical structure of the
Holst term coupled to fermions, the Nieh–Yan invariant, and the one-loop running of the Holst
sector"* — where only [2] supports the last clause) and again on p. 8 (*"not a result extracted
from Mercuri [8]…"*). Drop [8] from the RG citation, or move it to the classical-structure
clause where it belongs.

**MINOR-6 [correctness] — B9's route tag `[R2]` is not motivated by its content.**
B9 (p. 5) is tagged `[R2]` — the one-loop graviton-sector correction route — but its statement
is *"Phase-space volume conservation prevents irreversible selection among post-bounce states,
closing the 'vacuum selection at the bounce' class: the time-symmetric bounce selects no net
dark-energy state."* Nothing in that argument engages a one-loop Holst-sector amplitude; it is
a statement about bounce-epoch state selection. Fig. 1 accordingly draws Branch J → R2. Either
justify the assignment in one clause, or retag. (Contrast B3 and B4, whose `[R2]` tags are at
least readable as constraints on the same one-loop/Planck-suppressed channel.)

**MINOR-7 [presentation] — the abstract's unqualified "parity-odd densities" is walked back in Sec. V.**
The abstract describes `{O1–O6}` as *"local, gauge-invariant, diffeomorphism-covariant
**parity-odd** densities of mass dimension exactly four"* and then says every member is *"a
Fierz-closed four-fermion contact term suppressed by `M_Pl^{−2}`"* — but the only member with
nonzero content, O5, reduces on shell to `−(3/2)κ(J⁵·J⁵)`, which Sec. V correctly identifies as
**parity-even** (*"the parity-odd label belongs to the pre-reduction ε-contracted densities"*,
p. 13; also B8). The Sec. V qualifier is right; the abstract should carry a two-word version of
it so the reader is not surprised at p. 13. The same applies to the Sec. VI/VII restatements.

---

## SCOPE-HONESTY ASSESSMENT (summary)

Outside the two MAJOR items, the manuscript's scope discipline is **strong and, in places,
exemplary**: the three-tier evidentiary table (Table II) is honest and is respected by the
prose; Sec. VI's *"What is not established"* correctly names the non-enumerated escape classes
(derivative four-fermion terms, higher curvature–torsion mixings, multi-species chiral
structures, dynamical-Immirzi completions, non-minimal torsion irreps); Sec. III pre-emptively
downgrades five of its own entries to "general naturalness or classification arguments" and one
(B9) to "explicitly heuristic"; the rule-based completeness of the operator list is repeatedly
flagged as *asserted, not proved by exhaustive enumeration* — including in the abstract, which
is rare and correct; the released script is explicitly described as verifying two identities and
performing *no* basis enumeration (I confirmed the script prints exactly two check tags,
`[CHECK A]` and `[CHECK D]`); B12 explicitly refuses to convert its bound into a NANOGrav
exclusion; the birefringence measurements are explicitly labelled *"statistical indications
rather than established detections"*; the companion's non-peer-reviewed status is stated in
Sec. I and in Refs. [1] and [14]. Route 3's `1.4×10⁻⁶` is correctly presented as a **derived**
integrated result — I reproduced it — and the manuscript resists the temptation to promote it
beyond that.

## CITATION INTEGRITY

No defect beyond MINOR-5. All 25 references correspond to real, correctly-attributed works with
correct journal/volume/page/arXiv data as far as I can check. Quoted numerical inputs
(`0.342°±0.094°`, `0.35°±0.14°`, `0.215°±0.074°`, `γ=0.2375`, `γ≈0.274`, `ρ_crit≈0.41ρ_Pl`) are
consistent with their cited sources and with each other. The Shapiro–Teixeira equation numbers
are given with an explicit *"arXiv version"* caveat where version-dependent — good practice.
The pinned-commit provenance claim (`1130b7c5e3d2`, *"whose copies of all six files are
identical to the current repository head"*) is **verified true**: all six files are
byte-identical at the pin, at HEAD, and on disk. The acknowledgment that an archival deposit
of this survey's own scripts is *planned* rather than done is honest and should be closed
before publication.

## PRESENTATION BLOCKERS

**None.** `main.log` reports zero Overfull hboxes; no column overflow, no escaped multi-column
content, no unbreakable path collision was visible in any of the pages I rendered at 250–400
DPI. Table III, Table II and Fig. 1 all fit their columns cleanly. Underfull hboxes are present
but are cosmetic.

---

## FINDINGS TALLY

- **MAJOR: 2** — both `[correctness]`.
- **MINOR: 7** — `[correctness]` ×3 (MINOR-1, -5, -6), `[presentation]` ×4 (MINOR-2, -3, -4, -7).
- **Correctness-grade findings total: 5.**
- **Displayed equations independently re-derived and confirmed correct: 0 errors found** across
  Eqs. (1)–(5), (9)–(11), (A1)–(A4), (C1)–(C2), (E1)–(E5), Table II and Table III entries, and
  the B1/B12/App. A/App. E numerics. Four low-DPI false positives raised and withdrawn after
  re-rendering (listed in the header).
