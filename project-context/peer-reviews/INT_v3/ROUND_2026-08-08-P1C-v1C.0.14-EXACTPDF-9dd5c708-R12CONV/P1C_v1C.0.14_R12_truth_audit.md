# P1C v1C.0.14 — R12 correctness-convergence board truth audit (verdict-first) and v1C.0.15 closure record

- **Round:** ROUND_2026-08-08-P1C-v1C.0.14-EXACTPDF-9dd5c708-R12CONV — the R12
  correctness-convergence board on `arxiv/paper1c_nogo_survey/main.tex`, run
  against the R1–R11 disposition ledgers
  (`INT_v3/ROUND_2026-08-06-P1C-v1C.0.3-EXACTPDF-85e53832/P1C_v1C.0.3_truth_audit.md`
  through
  `INT_v3/ROUND_2026-08-07-P1C-v1C.0.13-EXACTPDF-d3aea74d-R11CONV/P1C_v1C.0.13_R11_truth_audit.md`)
  and against the released theory-audit artifacts (`research/theory_audit/*.md`,
  `*.json`).
- **Exact artifact:** v1C.0.14 PDF, SHA-256
  `9dd5c70862d3cad153143ead91f22e7fc5e410e8ac227aec24b13bd015ce17c3`,
  24 pp (sha verified by the reviewing leg before reading, and again here
  before any edit).
- **Date:** 2026-08-08 (round label follows the artifacts' own date stamps; the
  closure compile carries the machine-local date, August 7, 2026). Auditor:
  Claude (Fable 5) worker per CLAUDE.md directives B / H-refined / N. Rule
  applied: a finding that re-flags an R1–R11-dispositioned item is RE-FLAG
  unless the reviewer adds a genuinely new angle.

## Classification rule (standing since R8 — carried forward unchanged)

> every GNR item is classed CORRECTNESS-GRADE (wrong
> math/number/attribution/claim) or PRESENTATION-GRADE (length, repetition,
> layout, style). R-phase convergence = a full board with ZERO
> correctness-grade GNR; presentation-grade items route conceptually to the
> D-round stage. Integrity unchanged: every finding dispositioned with
> citations.

## Legs (raw receipts)

| Leg | Model | File | Verdict |
|---|---|---|---|
| Claude INT (Opus-tier subagent) | claude opus | `INT_v3/ROUND_2026-08-08-P1C-v1C.0.14-EXACTPDF-9dd5c708-R12CONV/P1C_claude_r12_leg.md` | **MAJOR REVISIONS** (2 MAJOR / 9 MINOR; 5 candidate findings withdrawn by the leg after 300-DPI re-render or artifact/tex cross-check). Both MAJORs trace to a single premise and both are **confirmed correct** by the independent computation below |
| Grok API | grok-4.3 | `ROUND_2026-08-08-P1C-v1C.0.14-EXACTPDF-9dd5c708-R12CONV_P1C_Grok_brutal.md` | **REJECT** (3 ESSENTIAL / 3 MAJOR / 2 NIT) — every complaint is scope, self-containment or length; none is computational, and none touches the defect this round actually found |
| Gemini API | gemini-3.1-pro-preview | `ROUND_2026-08-08-P1C-v1C.0.14-EXACTPDF-9dd5c708-R12CONV_P1C_Gemini_cosmology.md` | **ACCEPT WITH MINOR CORRECTIONS** (1 MINOR / 2 NIT; pass-2 NO_NEW) — Gemini's second ACCEPT-class verdict on P1C (after R4) and the board's third overall (Gemini R4, Claude R5, Gemini R12), and one that describes the Cartan derivations as "exact" on the exact PDF whose Cartan branch this round corrects |

**Failed legs (preserved as failure evidence, never counted, never hidden):**

- Perplexity leg: FAILED
  (`ROUND_2026-08-08-P1C-v1C.0.14-EXACTPDF-9dd5c708-R12CONV_P1C_Perplexity_citations.md`
  is a failure record). Optional leg per directive I1; recorded as failed,
  never a verdict.

## What makes this round different, and the integrity note that has to lead

R11's headline was that the paper's arithmetic was clean and its remaining
defects were disagreements between two places in the same document. R12 breaks
that pattern in the worst available direction: the reviewing leg challenged a
**load-bearing physical premise**, the challenge was adjudicated by solving the
governing equation from scratch, and **the referee was right**.

Three things must be recorded plainly, because this round changes a result one
of this repository's own released artifacts asserted.

1. **The referee was correct.** Claude MAJOR-1 and MAJOR-2 are both confirmed.
   The minimal-ECH on-shell torsion is *not* purely axial at finite γ; O4 is
   *not* identically zero on shell; O1 and O6 are *not* exact total derivatives
   on shell. The manuscript said all three, in about a dozen places, and all
   three were wrong on the Einstein–Cartan–**Holst** branch that defines this
   paper's framework.
2. **The earlier artifact assumed what it claimed to verify.**
   `research/theory_audit/operator_basis_adjudication_2026_08_07.md` §1 states
   as established fact that "the paper's on-shell Cartan torsion … is verified
   to be pure axial … This fact turns out to decide MAJOR-2." That was an
   **imposed input**, not a solved output: the module substitutes `T = κS`, which
   is totally antisymmetric by construction, and then verifies that it has no
   vector or tensor part. The Barbero–Immirzi parameter γ never enters that
   module at any point; the Holst-modified connection equation
   `Q_γ(e^[I ∧ T^J]) = J^{IJ}` was never solved. Its "explicitly curved on-shell
   configuration" is an Einstein–Cartan configuration, not an ECH one. Claude
   MAJOR-2 identified this exactly.
3. **The erratum is dated and preserves the original.** A clearly-marked
   **ADDENDUM — ERRATUM OF 2026-08-08** has been appended to that artifact's
   report. It edits nothing above it; the 2026-08-07 conclusions stand verbatim
   and the addendum scopes them, listing item by item which results are now
   restricted to the γ → ∞ branch and which are unaffected and independently
   re-confirmed at finite γ.

Per directive Q1, **none of this narration goes into the paper.** The manuscript
states only the correct physics: the solved on-shell torsion, its irrep content,
and the operator values that follow. The process record — the challenge, the
adjudication, the erratum, this ledger — lives here, in
`project-context/`, where it belongs.

## The adjudicating computation

`research/theory_audit/ech_torsion_onshell_2026_08_08.{py,json,md}` (committed
at `2d7db648`). Nothing was taken from the manuscript's scripts, from the
2026-08-07 module, or from the referee's arithmetic. The Einstein–Cartan–Holst
connection equation is set up from the action in explicit components and
**solved**; which torsion irreps survive is an output, never an input. Every
`[L##]` below is a line of that run's log, reproduced verbatim in the JSON.

**Method.** Route A varied the C-quadratic ECH action with respect to **all 24
independent contorsion components**, with no irrep ansatz `[L04]`, `[L05]`; the
minimal Dirac source entered only through the totally antisymmetric
`S^{IJK} = ¼ε^{IJKL}J⁵_L` `[L06]`; the solution is unique for every finite
nonzero γ `[L07]`. Route B dualized `Q_γ(e^[I ∧ T^J]) = J^{IJ}` to components and
solved by null space of the exact coefficient matrix `[L09]`. The two routes
agree exactly `[L14]`. Both Holst sign conventions were computed `[L46]`,
`[L47]`. All arithmetic exact-rational/symbolic.

**Result.** Writing `T_{abc} = α ε_{abcd}J^{5d} + β(η_{ab}J⁵_c − η_{ac}J⁵_b)`:

| irrep | on shell | evidence |
|---|---|---|
| axial (4) | **nonzero** | `[L12]`, `[L16]` |
| trace-vector (4) | **nonzero for every finite nonzero γ** | `[L12]`, `[L15]` |
| tensor (16) | **identically zero** | `[L11]` |

with `β/α = s_H/(2γ)` `[L10]`, `[L13]` — and `β/α → 0` only as γ → ∞, the
Einstein–Cartan limit `[L17]`. At γ = 0.2375 the trace-vector coefficient is
`40/19 = 2.11` times the axial one `[L23]`; at γ = 0.274, `250/137 = 1.82`
`[L24]`. The manuscript's own Eq. (E2), converted to torsion, reproduces exactly
this ratio `[L19]`, `[L20]`, and its `1/γ` term is a genuine trace-vector irrep —
its totally antisymmetric part is identically zero and it carries the entire
torsion trace `[L21]`, `[L22]`.

**Operators.** `O4(bare) = ε^{μνρσ}T^I{}_{μν}T_{Iρσ} = −24αβ(J⁵·J⁵)` `[L25]` and
`O5(bare) = −6α(J⁵·J⁵)` `[L26]`. `[L25]` vindicates the manuscript's *stated
reason* precisely — O4 vanishes on a pure axial torsion and on a pure
trace-vector torsion alike, and lives entirely on the cross term — and then
falsifies its conclusion, because the ECH torsion supplies that cross term. The
referee's claimed `O4 = −192π²G²γ³/(1+γ²)²(J⁵·J⁵)` is **CONFIRMED EXACTLY**
under App. E's normalization: difference 0, ratio 1, sign included `[L43]`.

**Identity status**, on six explicitly curved on-shell ECH configurations
(γ ∈ {19/80, 1, 3} × two exact-rational axial-current seeds), with O6 computed
by an independent affine-connection route `[L48]`–`[L66]`:

- `O1 − O6 = 0` exactly, every configuration — **survives**.
- `2·O1 + 2·O2 − O4 = 0` exactly, every configuration — Nieh–Yan **survives**,
  now re-verified on shell at finite γ.
- `O1 + O2 = ½O4 ≠ 0`, every configuration — **`O1 = −O2` FAILS**; it required
  `O4 = 0`.

**Why the no-go still holds.** `O4^[4]`, and with it the surviving parts of
`O1^[4]` and `O6^[4]`, are proportional to `(J⁵·J⁵)` — literally the same
operator as `O5^[4]`, at the same `M̄_Pl^{-2}` power, with
`O4^[4]/O5^[4] = γ/(1+γ²) = 0.225` at γ = 0.2375 `[L36]`. They are covered
unchanged by App. C's Fierz-closure lemma and by the single-scale NDA ceiling.
Disposal class (i) loses O1 and O6 to class (ii); class (iii) loses O4. Nothing
acquires a new light scale. **The physics conclusion of P1C survives; the
printed mechanism does not.**

## Deduplicated finding ledger

### R12-GNR-1 [C] — the minimal-ECH on-shell torsion is not purely axial at finite γ; O4 is not identically zero and O1/O6 are not exact total derivatives on the ECH branch (Claude MAJOR-1)

**Legs:** Claude MAJOR-1.

**Verdict: GENUINELY-NEW-REAL, correctness-grade — ADJUDICATION-CONFIRMED.**

**Not a re-flag, and specifically the opposite of R9's lineage.** R9-MAJOR-2
argued that Table III's `O1 → Final = 0` was internally contradicted on shell,
and the 2026-08-07 adjudication FALSIFIED that finding — correctly, on the
branch it evaluated. R12 asks the question that adjudication never asked:
*which branch is that?* The answer is Einstein–Cartan, and the paper's framework
is Einstein–Cartan–Holst.

**Verified against source and against the solved connection equation.** The
manuscript asserted, at v1C.0.14:

- Sec. II (`main.tex:612–614`): the connection variation "gives an algebraic
  (non-dynamical) constraint fixing the torsion tensor `T^{abc}` … `T^{abc} =
  κ S^{abc}`" — stated unqualified. This is the γ → ∞ limit `[L17]`.
- Sec. V construction rule (`main.tex:1784`): "the algebraically-fixed torsion
  `T = κS`" — the phrase that propagates into the whole operator list.
- Sec. V bullet (a) (`main.tex:1950–1956`): "`O_4^{[4]} = 0` (below) gives
  `O_1^{[4]} = O_6^{[4]} = −O_2^{[4]}` exactly, so they are minus the Nieh–Yan
  total derivative and contribute zero to the equations of motion and zero to
  the vacuum energy" — **false on the ECH branch** `[L50]`, `[L53]`, `[L56]`,
  `[L59]`, `[L62]`, `[L65]`.
- Sec. V trichotomy (`main.tex:~1934`), clause (iii): "O4 on the `T = κS`
  branch, because the ε-contracted torsion-square is supported only by the
  non-axial torsion irreps" — the *reason* is exactly right `[L25]`, the
  *conclusion* inverts.
- App. A 1 (`main.tex:2406–2422`): "purely axial — its vector and tensor parts
  vanish identically — so `O_4^{[4]} ≡ 0` on shell … This *strengthens* the
  closure".
- Table III row O4 and caption (`main.tex:2437–2440`, `2458`), Check D
  (`main.tex:2503–2513`), the Verdict (`main.tex:2544–2545`), the abstract
  (`main.tex:417–421`), and Sec. IV A's Route-2 case (i).

The referee's Eq.-(E2) reading, their trace-vector claim, their `1/(2γ)` ratio,
their 2.1× dominance at the LQG γ, and their closed-form O4 are each confirmed
independently: `[L19]`–`[L24]`, `[L43]`, `[L45]`.

**Closure (real action, v1C.0.15) — option (b) of the reviewer's two, which the
reviewer themselves recommended and which is the only honest option for a paper
whose framework is ECH at γ ≈ 0.2375:**

1. **Sec. II now prints the solved ECH torsion**, as a numbered equation
   (`eq:ech_onshell_torsion`): the two-irrep form, `β/α = 1/(2γ)`, α and β
   explicitly, the tensor irrep identically zero, the γ → ∞ Einstein–Cartan
   limit named as a limit, and the 2.11 / 1.82 ratios at the two LQG γ values.
   The overall torsion sign is declared a convention and the Holst-sign
   invariance recorded `[L46]`, `[L47]`.
2. **Every downstream "`T = κS` branch" phrase re-pointed** at that equation —
   Sec. IV head, Sec. IV A case (i), Sec. V construction rule, Sec. V
   trichotomy, Sec. V bullets (a) and (b), Sec. V's on-shell-branch summary,
   App. A 1 preamble, Check A, Check D, Table III (caption and rows O1/O4/O5/O6),
   and the App. A 1 Verdict.
3. **O4's on-shell value is printed** as a numbered equation
   (`eq:o4_onshell`): `O_4^{[4]} = −24 M̄_Pl² αβ (J⁵·J⁵) = −3κγ³/(1+γ²)²
   (J⁵·J⁵)`, with the bare invariant `−192π²G²γ³/(1+γ²)²(J⁵·J⁵)` given
   alongside, and `O_4^{[4]}/O_5^{[4]} = γ/(1+γ²) ≃ 0.22` at γ = 0.2375.
4. **The "strictly stronger disposal" claim is withdrawn.** O4 now shares O5's
   disposal.
5. **O1 = O6 = −O2 + ½O4** is printed wherever the old `O1 = O6 = −O2` was, with
   the total-derivative part and the contact-term remainder distinguished. Table
   III's O1 and O6 Final entries move from `0 (EOM)` to `½O_4^{[4]}`.
6. **Disposal classes restated** in Sec. V and in the App. A 1 Verdict:
   (i) = {O2, O3}; (ii) = {O5, O4, and the O1 = O6 remainder}; (iii) = {O1, O6
   on the torsion-free branch}.
7. **What survives is stated as surviving**: `O1 = O6` and the Nieh–Yan relation
   are unchanged, and Sec. V's rank/null-space paragraph is untouched because
   both were re-verified at finite γ `[L49]`–`[L66]`.

**Was any strength claimed that is not now claimed? Yes, and deliberately.** The
survey previously claimed one operator with nonzero vacuum-energy content and a
disposal *stronger* than Planck suppression for another. It now claims two
operators in the Planck-suppressed Fierz-closed class plus a contact remainder
on a third and fourth. That is a strictly weaker set of claims, made because the
connection equation requires it. The final conclusion — no `(meV)⁴` vacuum
energy without a new light scale — is unchanged, and is now reached on the
branch the framework actually sits on.

---

### R12-GNR-2 [C] — the released artifact cited as verifying "O4 ≡ 0 on shell" evaluated an Einstein–Cartan configuration, and the manuscript reported it as an ECH on-shell verification (Claude MAJOR-2)

**Legs:** Claude MAJOR-2.

**Verdict: GENUINELY-NEW-REAL, correctness-grade — ADJUDICATION-CONFIRMED.**

**Not a re-flag.** No prior round examined what the 2026-08-07 module's on-shell
branch actually was. R11 cited that artifact approvingly (R11-GNR-4 used it to
correct App. C's Fierz-uniqueness claim, and that use remains valid — the Fierz
content is a different module).

**Verified against the artifact, in both the report and the machine output.**
The referee's characterization is exact. `operator_basis_adjudication_2026_08_07.md`
§1: "The paper's on-shell Cartan torsion `T^{abc} = κS^{abc} = (κ/4)ε^{abcd}J⁵_d`
is verified to be **pure axial** … **This fact turns out to decide MAJOR-2**."
Substituting a totally antisymmetric tensor and then checking that it is totally
antisymmetric is a tautology. γ appears nowhere in that module. Its §5 "curved
on-shell configuration" `[L90]`–`[L94]` solves the Cartan equation for ω given
`T = κS`, which is the Einstein–Cartan constraint. The manuscript then promoted
that verification twice: App. A 1 (`main.tex:2414–2418`) and Data & Code
Availability (`main.tex:2158–2166`), the latter stating the artifact establishes
"that the ε-contracted torsion-square O4 vanishes identically under the purely
axial Cartan torsion".

The referee also verified, and this audit re-verified, that the artifact's
*integrity* is not in question: the six cited files were byte-identical between
the pinned commit `1130b7c5e3d2` and HEAD at review time, and
`dim4_parityodd_enumeration.py` contains exactly `[CHECK A]` and `[CHECK D]` and
no enumeration. The defect was in what the computation was *said to establish*.

**Closure (real action, v1C.0.15):**

1. **Erratum written, dated, non-destructive.** `ADDENDUM — ERRATUM OF
   2026-08-08` appended to `operator_basis_adjudication_2026_08_07.md`. It edits
   nothing above it. It states what was imposed rather than derived, lists the
   conclusions now scoped to γ → ∞ (the pure-axial premise, `O4 = 0`,
   `O4 = 0 ⟹ O1 = −O2`, Table III's `Final = 0` for O1, the replacement text for
   Table III's O4 row, the "this strengthens the no-go" sentence — **withdrawn** —
   and §7's net on-shell picture), and lists what is unaffected and
   independently re-confirmed at finite γ (rank 4, nullity 2, both null vectors,
   `O1 = O6` including the Γ route, the density-normalization cross-check, the
   subset ranks, the rank-modulo-total-derivatives result, the Levi-Civita-`R̊`
   reading, the ε-free square identities, and "what P1C must change" items 1–3).
2. **New module released and cited.**
   `research/theory_audit/ech_torsion_onshell_2026_08_08.{py,json,md}` is added
   to Data & Code Availability via the `\artifact{}` convention (files 7 and 8),
   with a description of what it actually does: solves the Holst-modified
   connection equation at finite γ, varying with respect to all 24 contorsion
   components with no irrep ansatz, cross-checked against an independent
   differential-form route, returning the irrep content, the closed forms for O4
   and O5, and O1–O6 on six curved on-shell ECH configurations at
   γ ∈ {19/80, 1, 3}.
3. **App. A 1's artifact citation rewritten** to describe the on-shell solve
   rather than the Einstein–Cartan evaluation; Check D's confirmation sentence
   now names both modules and says "six explicitly curved on-shell
   Einstein–Cartan–Holst configurations".
4. **Data & Code provenance restated truthfully.** The 2026-08-07 report is no
   longer byte-identical to commit `1130b7c5e3d2` (it carries the addendum), and
   the two new files postdate that commit. The paragraph now pins the **first
   five** files at `1130b7c5e3d2` as byte-identical to head, and states that the
   operator-list adjudication report and the two on-shell torsion files postdate
   that commit and are available at the repository head; the provenance-boundary
   sentence is widened from "third through sixth" to "third through eighth".
   Verified: five of six previously-pinned files still hash-match the pinned
   commit; the sixth is the erratum'd report.

---

### R12-ADJ-1 [C] — Sec. II's `T = κS` and App. E's Eq. (E2) fix the same object in normalizations differing by a factor two (adjudication-driven; raised by neither party)

**Legs:** none. Surfaced by the adjudicating computation `[L27]`–`[L30]`,
`[L44]`, `[L45]`.

**Verdict: GENUINELY-NEW-REAL (adjudication-driven), correctness-grade.**

**Verified.** The module anchored the matter-coupling normalization two ways and
they disagree by exactly 2 in torsion amplitude (4 in any quadratic-in-`T`
density):

- READING-I, the App. E / Freidel–Minic–Takeuchi anchor: require the
  eliminated-torsion operator to equal Eq. (E4),
  `L_4ψ = −(3κ/16)[γ²/(1+γ²)](J⁵·J⁵)`. Back-substitution of the solved
  contorsion gives `L_int = −3γ²κλ²/[16(γ²+s_H²)](J⁵·J⁵)` `[L27]`, fixing
  `λ = ±1` `[L28]`.
- READING-II, the Sec. II literal anchor: require `T^{abc} → κS^{abc}` as
  γ → ∞. Fixes `λ = −1/2` `[L29]`.
- `λ_I/λ_II = 2` `[L30]`.

This is diagnosable from the manuscript alone: under READING-II, O5's printed
fate `−(3/2)κ(J⁵·J⁵)` comes out exactly in the γ → ∞ limit `[L39]`, whereas
READING-I gives `−3κ` there `[L33]`. So Sec. V, Table III and App. A 1 were
using READING-II while App. E used READING-I — and the referee, reading Eq. (E2)
directly, used READING-I `[L45]`.

**Closure (real action, v1C.0.15) — one normalization, stated, and it is
App. E's.** The survey now normalizes torsion by Eq. (E2) throughout. The reasons
are recorded here rather than argued in the paper:

- Eq. (E2) is the paper's **only derived** on-shell torsion — it is the
  Freidel–Minic–Takeuchi solution of the connection equation, quoted verbatim
  from the literature, and its back-substitution reproduces Eq. (E4), the
  survey's load-bearing contact coefficient. Sec. II's `T = κS` was a schematic
  assertion with no external anchor.
- It is the normalization in which the independently solved connection equation
  reproduces Eq. (E2)'s structure exactly `[L20]`, and in which the referee's
  O4 is confirmed with difference 0 and ratio 1 `[L43]`.

Concretely: Sec. II's unqualified `T^{abc} = κS^{abc}` is replaced by the solved
torsion with α and β in Eq. (E2)'s normalization; App. E states outright that
Eq. (E2) fixes the torsion normalization used throughout, converts it to
Eq. (`eq:ech_onshell_torsion`), identifies the `1/γ` term as the trace-vector
irrep (not an axial piece in another basis, and not a normalization artifact —
`[L22]`, `[L10]`, `[L13]`), and gives the γ → ∞ purely axial limit
`T_{abc} → (κ/2)ε_{abcd}J^{5d}`. Downstream, O5's reduction becomes
`−3κ[γ²/(1+γ²)](J⁵·J⁵)` `[L33]` in Sec. V bullet (b), App. A 1, Table III and
Check D, and Sec. II's convention note is updated from "the −3/8 and −3/2
coefficients" to "the −3/8 and −3 coefficients". Check D's ε-free square is
restated in the **normalization-independent** form `T_{abc}T^{abc} = −6α²(J⁵·J⁵)`,
a one-line application of the paper's own printed contraction identity
`ε_{abcd}ε^{abce} = −3!δ^e_d`, so no number there depends on the choice;
`S_{abc}S^{abc} = −(3/8)(J⁵·J⁵)` is a statement about the spin current and is
unchanged.

`/never-fabricate-derivation` gate observed: every number introduced above is
traceable to a tagged log line of the released module, and the single
non-quoted step (the generic ε-free square) is an application of an identity
already printed in the manuscript, not a new derivation.

---

### R12-GNR-3 [C] — App. C's scope paragraph says trace-vector irreps "appear only when the minimal coupling assumption is relaxed"; that is false (Claude MAJOR-1's third internal contradiction)

**Legs:** Claude MAJOR-1 (third contradiction), confirmed by `[L11]`, `[L15]`.

**Verdict: GENUINELY-NEW-REAL, correctness-grade.**

**Verified against source.** App. C (`main.tex:2693–2695`) excluded from the
lemma's reach "non-minimal torsion irreps (trace-vector and tensor irreps) that
appear only when the minimal coupling assumption is relaxed", and App. A 1
(`main.tex:2384–2386`) asserted that "no non-minimal (trace/tensor) torsion
irreps are admitted". The computation splits the two cleanly: the **tensor**
irrep is identically zero on shell under minimal coupling `[L11]` — so the
exclusion is right for the tensor — while the **trace-vector** irrep is
generated by the Holst term under strictly minimal coupling at every finite
nonzero γ `[L15]`. The referee is right that the three statements cannot all be
true.

**Closure (real action, v1C.0.15).** App. C's scope paragraph now excludes "the
tensor torsion irrep, which is identically absent from the minimally-coupled
on-shell torsion and appears only when the minimal-coupling assumption is
relaxed", and adds the positive statement: the trace-vector irrep *is* generated
under minimal coupling by the Holst term and is **inside** the lemma's reach,
entering the operator list through O4, whose on-shell value is the same
Fierz-closed `(J⁵·J⁵)` structure the lemma covers at the same `M_Pl^{-2}` power.
The Fierz-evasion sentence earlier in App. C ("trace/tensor torsion irreps")
becomes "the tensor torsion irrep". App. A 1's assumption list is rewritten to
state that the irrep content is an **output** of the connection equation rather
than an assumption. The App. A 1 Verdict's excluded-classes list likewise drops
"non-minimal torsion irreps" in favour of "the tensor torsion irrep".

---

### R12-GNR-4 [C] — "Levi-Civita *symbol*" printed alongside the Lorentzian *tensor* contraction identity (Claude MINOR-1)

**Verdict: GENUINELY-NEW-REAL, correctness-grade** (graded above the leg's own
`[presentation]` tag: the printed statement is wrong as written, and the sign of
two load-bearing coefficients depends on it).

**Verified.** Sec. II (`main.tex:~557`) and Eq. (9) (`main.tex:~1849`) both said
"Levi-Civita **symbol** … `ε^{0123} = +1`" while quoting
`ε_{abcd}ε^{abce} = −3!δ^e_d`. For a metric-independent symbol with
`ε_{0123} = ε^{0123} = +1` the contraction is `+3!δ^e_d`; the `−3!` is the
Lorentzian **tensor** identity, which requires `ε_{0123} = −1`. The adjudicating
module verified the identity in exactly that normalization `[L01]`, `[L02]`, and
the 2026-08-07 module had already flagged the ambiguity in passing.

**Closure:** both sites now read "Levi-Civita **tensor** … `ε^{0123} = +1`,
equivalently `ε_{0123} = −1`". No coefficient moves; the intended convention was
always the one the identity encodes.

---

### R12-GNR-5 [C] — the paper's stated explanation for the Nieh–Yan factor of two does not account for it, and the conversion is not given (Claude MINOR-2)

**Verdict: GENUINELY-NEW-REAL, correctness-grade** (the printed *explanation* is
wrong, not merely terse).

**Verified.** Sec. V quotes `d(e_I∧T^I) = T_I∧T^I − e_I∧e_J∧R^{IJ}` (1 : 1 : 1) a
few lines before Eq. (11) gives `2·O1 + 2·O2 − O4 = 0` (1 : 1 : ½ on O4), and
attributed the discrepancy to "the form-versus-density normalization of the
Nieh–Yan entry". The referee is right that rescaling O2 alone cannot produce a
*relative* factor two between the O4 and O1 terms; the source is the wedge
combinatorics of `T∧T` versus `e∧e∧R` in the form→density conversion. The
2026-08-07 module records the conversion as
`d(e_I∧T^I)_dens = ¼O4 − ½O1` `[L65]`.

**Closure:** the conversion is now printed in one line. With
`A ≡ ε^{μνρσ}e^I_μ e^J_ν R_{IJρσ}` and `B ≡ ε^{μνρσ}T^I{}_{μν}T_{Iρσ}` (the bare
invariants underlying O1 and O4), the strict form-to-density conversion gives
`[d(e_I∧T^I)]_dens = ¼B − ½A`, whereas Eq. (`eq:ny_norm`) defines
`NY = ½B − A`, twice that — and the relative factor between the two terms is
wedge combinatorics, not a rescaling of NY alone. A reader can now reproduce
Eq. (11) from the quoted identity. (`NY = ½B − A` is Eq. (11) rearranged; the
`¼B − ½A` half is the artifact's `[L65]`.)

---

### R12-GNR-6 [C] — mixed barred/unbarred Planck mass inside a displayed identity declared exact (Claude MINOR-3)

**Verdict: GENUINELY-NEW-REAL, correctness-grade.** Verified: App. A 1 printed
"The identity `M_Pl² κ² = κ` [exact in the reduced-mass convention
`κ = M̄_Pl^{-2}`…]" — exact only with the barred mass, which the display wrote
unbarred. The reviewing leg separately confirmed at 300 DPI that Sec. II's
reduced-mass definition does carry its overline correctly (its withdrawn
candidate W-5), so this was the one residual instance.

**Closure:** the display now reads `M̄_Pl² κ² = κ`, and its role is stated: it is
what converts the bare ε-contracted square into Eq. (`eq:o4_onshell`).

---

### R12-GNR-7 [C] — "six observational-channel branches" is a label count, not a constrained-channel count, and the qualifier never reached the abstract (Claude MINOR-4)

**Verdict: GENUINELY-NEW-REAL, correctness-grade (scope).** Verified: Sec. III
discloses it plainly — "the two grouped branch pairs (L/M and N/O) are treated
as single observational channels, and **neither N nor O carries a dedicated
constraint of its own**" (`main.tex:701–704`, the R11-GNR-8 closure) — while the
abstract, Sec. I, Sec. VI and Sec. VII repeat the headline six without it. The
14-entry count is honestly derived and unaffected; only the branch headline was
inflated.

**Closure:** the abstract now reads "six observational-channel branches (grouped
into four constrained observational channels, since L/M and N/O are treated in
pairs and neither N nor O carries a dedicated constraint of its own)". The
qualifier is placed where a referee checks the count.

---

### R12-GNR-8 [C] — the abstract's "61–67 orders below the observed dark-energy density" is carried by a Tier-III scaling relation and the abstract does not say so (Claude MINOR-5)

**Verdict: GENUINELY-NEW-REAL, correctness-grade (scope).** Verified: the body is
scrupulous — Eq. (5) is labelled "a Tier-III mass-dimension scaling relation, not
a derived stress-tensor matching — we do not supply the cosmological stress
tensor that a genuine mapping would require, and none is claimed" — while the
abstract described the bound as an "integrated one-loop renormalization-group
flow that leaves the contribution 61–67 orders … below". The flow supplies only
`Δγ/γ`; the step to a `ρ_Λ` ratio is the ansatz.

**Closure:** one clause added to the abstract: "The flow itself supplies
`Δγ/γ`; the step from that to a `ρ_Λ` ratio is an explicitly labeled Tier-III
mass-dimension scaling relation, not a derived stress-tensor matching."

---

### R12-GNR-9 [C] — Table II calls the R2 birefringence leg "exploratory, not load-bearing" while the abstract headlines its margin (Claude MINOR-6)

**Verdict: GENUINELY-NEW-REAL, correctness-grade** (an internal-consistency
defect, the R11 class).

**Verified.** Table II's R2 row said "exploratory, not load-bearing"; the
abstract says the leg "closes against the observed birefringence amplitude with
roughly sixty orders of magnitude (conservatively ≥ 58) of suppression margin",
and Sec. VII repeats it. Both registers are defensible in isolation; read
together a referee cannot tell which is meant.

**Closure:** reconciled in one sentence, placed in Sec. IV A next to the
robustness statement rather than in the table (the table cell is length-critical
— see the float note below): Table II labels the leg ansatz-level and
exploratory because the *precise size* of the margin rests on the scaling
ansatz, whereas what the abstract's headline uses is only that the budget sits
many orders below the observed amplitude, a conclusion the paper's own 48-order
stress test shows is insensitive to the ansatz. Table II's cell now reads
"exploratory in its precise size, not in its sign (Sec. IV A)".

---

### R12-GNR-10 [C] — the abstract's flat "none a logical consequence of another" is asserted for all 91 catalog pairs and demonstrated for two (Claude MINOR-8)

**Verdict: GENUINELY-NEW-REAL, correctness-grade (scope).** Verified: the
abstract and Sec. III make the claim globally; only (B8, B14) and (B11, B13) get
an argument. Sec. III's own hedge ("they do not assert that the barriers rest on
disjoint assumptions") is good but weaker than the abstract's flat claim.

**Closure:** the abstract is softened to the claim the paper actually supports:
"one per catalog entry; the entries are not restatements of one another, and for
the pairs most at risk of subsumption (B8/B14 and B11/B13) the independence is
argued explicitly in the text". The 14-count and the joint-closure claim
(R11-GNR-3's closure) are untouched.

---

### R12-GNR-11 [P] — silent change of referent between Eq. (A1) and Case I (Claude MINOR-7)

**Verdict: GENUINELY-NEW-REAL, presentation-grade** — the leg's own note is that
"the arithmetic is right; the referent changes without notice". Eq. (A1)
establishes `[ε e e F] = +2`; Case I then takes `c ∼ M_Pl^{4−1} = M_Pl³`, the NDA
coefficient for a dimension-1 operator (the static torsion density inside
`ε e e F`).

**Closure:** the referent is named: "The relevant operator here is the
dimension-(+1) static piece inside `ε e e F`, not the dimension-(+2) contraction
itself; its natural coefficient is `c ∼ M_Pl^{4−1} = M_Pl³`".

---

### R12-GNR-12 [P] — the Shapiro–Teixeira coefficients are cited from "their Eq. 42, arXiv version", flagging a divergence without naming it (Claude MINOR-9)

**Verdict: GENUINELY-NEW-REAL, presentation-grade.** Verified: the parenthetical
tells a reader that an arXiv-vs-published difference may exist in the source of a
load-bearing O(1) coefficient without saying what it is. The leg verified the
internal algebra completely (`|Ω_44/α_4| = 3.33` at γ = 0.24, infimum 3.15, 4.84
at γ = 1) but could not check the values against the published CQG version.

**Closure — stated at exactly the confidence we have, and no further.** The
parenthetical now reads: "their Eq. 42; we quote the arXiv version of that
reference, which is the version we were able to consult, and no discrepancy with
the published version is known to us". No claim is made about the published
version's content.

---

### R12-GNR-13 [P] — the abstract's spanning-list sentence is one 80-word nested period (Gemini N1)

**Verdict: GENUINELY-NEW-REAL, presentation-grade.** Verified: the sentence ran
from "We further present an operator-list argument" through the entire
construction rule, the parity qualifier and the closure trichotomy.

**Closure:** split into four sentences — the object, its parity status, the
closure statement, and the branch detail — with no content dropped. The
zero-derivative construction qualifier (R11-GNR-11) and the redundancy/rank
sentences are retained verbatim.

---

### R12-GNR-14 [P] — proliferating density sub/superscripts in App. A (Gemini N2)

**Verdict: GENUINELY-NEW-REAL, presentation-grade**, and recorded with Gemini's
own qualification that "the current usage is technically unambiguous". Verified:
`ρ_Λ^{bounce}`, `ρ_bounce` and `ρ_Λ^{obs}` appear in close succession; the
paper's bookkeeping paragraph already distinguishes them but only after the
fact.

**Closure:** a one-line gloss added ahead of that paragraph naming all three
symbols as distinct quantities. No symbol is renamed — renaming would break the
Eq. (A2) reference and the `10^122` hierarchy chain.

---

### R12-RF-1 — "the abstract overstates the two amplitude-budget closures; the margins are imported one-loop estimates, not new derivations" (Grok E1)

**Verdict: RE-FLAG.** Chain: R3 (v1C.0.6) → R10-RF-4 → R11-RF-2 → R12-RF-1. The
abstract, Sec. IV B and Sec. VII already label the ~67-order endpoint as the
derived integrated flow and the ~61-order endpoint as the deliberately
pessimistic chiral-count bound, and Sec. IV states that the loop factor and
β(γ) are imported from published work "rather than adopted". Falsified again in
the arithmetic by this round's own opposing leg, which reproduced both endpoints
from the printed inputs (`0.3 × 1.18×10^{-61} = 3.5×10^{-62}`;
`1.4×10^{-6} × 1.18×10^{-61} = 1.7×10^{-67}`). Grok's requested qualifier is a
restatement of labels already present. One genuine residue — that the *step* from
`Δγ/γ` to a `ρ_Λ` ratio is Tier-III — was identified precisely by the Claude leg
and is closed as R12-GNR-8.

### R12-RF-2 — "the paper is not standalone; core results are imported from an unpublished companion" (Grok E2)

**Verdict: RE-FLAG.** The longest-running chain in this paper's history: R1
`GNR-2` → R2-RF-2 → R3-RF-2 → R4-RF-1/RF-6 → R5-RF-4 → R6 (App. E added) →
R7-RF-2/RF-9 → R8-RF-3/RF-10 → R9-RF-1 → R10-RF-1 → R11-RF-1 → R12-RF-2. App. D
carries B14's statement and proof self-contained; App. E carries the
torsion-elimination chain, the contact coefficient and the R1 benchmark. Grok
names four items as unverifiable — torsion elimination, the coefficient
`−3κ/16[γ²/(1+γ²)]`, the Fierz-closed basis, and B14 — and all four are carried
in this manuscript, in Apps. C, D and E. Falsified again by the opposing leg,
which verified `Q_γ Q_γ^{-1} = 1` by direct multiplication, reproduced FMT's
Eq. (23) from Eq. (E2) under `L_int = ½S·C`, checked Eq. (E3), and verified the
full Fierz involution from the printed matrix. This round strengthens App. E
further (the normalization statement and irrep identification of R12-ADJ-1).

### R12-RF-3 — "eight of the fourteen entries are general naturalness arguments; relabel and reduce the headline claim" (Grok E3)

**Verdict: RE-FLAG.** Chain: R11-RF-4 → R12-RF-3. The paper states this itself,
in the Fig. 1 caption Grok is reading: "five entries (B5–B7, B10, B13) are
general naturalness or classification arguments", with Sec. III's preamble and
Table II carrying the same disclosure. Grok's count of eight is also not
supported by the entries it names (B5–B7, B10–B13 is seven, and B11/B12 are
ECH-specific parameter-window entries); the paper's printed five is the honest
number. Disclosure restated as defect.

### R12-RF-4 — "24 pages is excessive; condense to ≤15" (Grok M1)

**Verdict: RE-FLAG**, and recorded honestly rather than smoothed. Chain: R1
`GNR-3` residual → R2-RF-7 → R3-RF-7 → R4-RF-10 → R6-RF-4 → R7-RF-11/12 →
R8-RF-12 → R9-RF-6 → R10-GNR-15 (seven redundant passages actually cut) →
R11-RF-5 → R12-RF-4. **This round the page count rose again, 24 → 25 pp**,
because the on-shell correction required new text: a numbered torsion equation,
a numbered O4 equation, the irrep discussion in Sec. II and App. E, and the
App. C split. That is reported, not hidden. The target is not reachable without
deleting catalog content, which the round directive forbids. Grok's specific
suggestion — move "the operator-list verification scripts and the full symbolic
output" to a repository supplement — describes the arrangement that already
exists: no script and no symbolic output is printed in the manuscript; all six
(now eight) live in the repository and are cited by path.

### R12-RF-5 — "the spanning-list completeness claim rests on an incomplete enumeration" (Grok M3)

**Verdict: RE-FLAG.** Chain: R9-GNR-1 → R10-GNR-6 → R11-RF-3 → R12-RF-5. Grok's
"required fix" is "either an exhaustive symbolic enumeration or an explicit
statement that completeness is conjectural and Tier-II". The second is what the
paper prints, in six places, including the abstract ("That the list *spans* the
rule-admitted operator space is asserted from the construction rules, not proved
by exhaustive symbolic enumeration") and the Data & Code statement ("None of the
scripts performs the enumeration establishing that the list spans the
rule-admitted space"). Grok also notes the list is rank-4 and linearly
dependent — which is the paper's own printed result, added at R9.

### R12-RF-6 — "add a per-section notation box for the (α, M) symbol pair" (Grok N2)

**Verdict: RE-FLAG / declined with reason.** The overload is disclosed once, in
the Sec. II convention flags (added v1C.0.4), which state that only the fitted
combination `α/M` — never α or M separately — enters any quantitative statement,
"so no conclusion depends on resolving the two roles". Repeating a notation box
at the head of every major section would reinstate exactly the defensive
repetition R10-GNR-12 removed at this reviewer's own earlier request, and would
add length this reviewer complains about in the same report (R12-RF-4).

### R12-DEF-1 — frozen-release Zenodo DOI for this survey's own verification scripts (Gemini P1C-M1)

**Verdict: DEFERRED-GENUINE (P-round packaging)** — carried forward unchanged.
Chain: R2-SO-2 → R3-RF-6 → R4-RF-8 → R5-GNR-2 → R6-RF-9 → R7-RF-8 → R8-RF-11 →
R9-RF-9 → R10-DEF-1 → R11-DEF-1 → R12-DEF-1. The requirement is real, the paper
already discloses that the deposit is planned rather than done, and minting a
DOI is a publish action requiring Houston. Not closed, not dismissed. Note that
this round *adds* two files to the deposit's eventual scope.

### R12-FAL-1 — "the two-order 'conservative allowance' for unmodeled higher-order corrections is unquantified and unreferenced" (Grok M2)

**Verdict: FALSIFIED, with receipts.** Grok describes the two orders as "an
unquantified conservative allowance … for unmodeled higher-order corrections".
They are nothing of the kind: they are the explicit difference between two
index-contraction orderings of the same budget, both computed in the text —
Eq. (2) evaluates to `1.7×10^{-60}` and the direct contraction
`(α_em/4π)(H_0/M_Pl)/β_obs ≈ 10^{-3}·10^{-61}/(6×10^{-3}) ≈ 2×10^{-62}` — and the
paper adopts the **less** favourable of the two and says so ("the quoted
`∼10^{-60}` is therefore the conservative side of this bookkeeping choice").
Both values were reproduced independently by this round's opposing leg. The
paper's actual robustness allowance is separately quantified and stated: ten
orders of coefficient inflation still leaves ≳48 orders of margin.

### R12-FAL-2 — "Table II mixes three evidentiary tiers in a single column without repeating the tier label on every row" (Grok N1)

**Verdict: FALSIFIED.** Verified against the exact v1C.0.14 PDF, p. 12: every one
of the five rows of the *Evidentiary status* column opens with its own bold tier
marker — **(I) Rigorous**, **(II)+(III)**, **(III) Ansatz-level** (with a second
explicit **(II)** for the dark-energy leg), **(II)+(III)**, **(II) Structural**.
The label is repeated on every row already, which is precisely the fix requested.

## Candidate findings withdrawn by the reviewing leg

Five, all recorded by the leg itself under its accuracy protocol and all
verified here. Four are the low-DPI extraction-artifact family the standing
≥300 DPI re-render protocol exists to catch; the fifth is a genuine downgrade.

| ID | Candidate | Why withdrawn |
|---|---|---|
| **W-1** | "`ρ_crit = 3/(32π²γ³)ρ_Pl` is wrong; the LQC formula carries a `√3`" | `pdftotext` displaced the radical to the previous line. Re-rendered p. 6 at 300 DPI: the radical **is** printed. `√3/(32π²γ³)` gives 0.409 at γ = 0.2375 and 0.267 at γ = 0.274, reproducing *both* quoted endpoints. No error. |
| **W-2** | "B1's `g_eff ∼ 1/(M_Pl\|t_3\|)` is dimensionally inconsistent" | `pdftotext` dropped the radicals, leaving stray `p` glyphs. Re-rendered p. 4 at 300 DPI: the text reads `g_eff ∼ 1/(M_Pl√\|t_3\|)` with `√\|t_3\| ∼ m_T^{-1}`, giving `m_T/M_Pl = H_0/M_Pl` correctly. No error. |
| **W-3** | "Eq. (11) contradicts the Nieh–Yan identity quoted three lines above it" | Checked against the 2026-08-07 module: the null vector `[2,2,0,−1,0,0]` is an exact-rational result over a 1368-monomial jet basis, cross-checked against `d(e_I∧T^I)_dens = ¼O4 − ½O1`. The relative factor 2 is genuine form→density combinatorics. **Downgraded** MAJOR → MINOR-2 (the *explanation* is imprecise), closed as R12-GNR-5. |
| **W-4** | "Table III's O4 row asserts a nonzero `κ(J⁵·J⁵)` fate contradicting the `O4 ≡ 0` prose" | Real in v1C.0.11 and closed at R9; re-rendered Table III on p. 20 at 300 DPI shows v1C.0.14 already carries the corrected row. Withdrawn. (The surviving defect is R12-GNR-1, a different one — and it moves that row again.) |
| **W-5** | "Sec. II conflates reduced and full Planck mass" | `pdftotext` drops the overline. Re-rendered p. 2 at 300 DPI: `M̄_Pl ≡ (8πG)^{-1/2}` carries its overline, with unbarred `M_Pl ≡ G^{-1/2}` used only in order-of-magnitude prose. No error — one residual in-display instance retained as MINOR-3 and closed as R12-GNR-6. |

Recorded because the leg's 300-DPI-first method is the reason two of this
round's candidate MAJORs did not reach the board, and because the same family
(R3-FAL-2 → R5-RF-7/FAL-1 → R7-FAL-1 → R8-FAL-4 → R9-FAL-4 → R11-FAL-1) has now
fired in eleven rounds.

## Ledger totals

| Verdict | Count | Items |
|---|---|---|
| GNR (genuinely-new-real) | 14 | R12-GNR-1 … R12-GNR-14 |
| ADJ (adjudication-driven) | 1 | R12-ADJ-1 |
| RE-FLAG | 6 | R12-RF-1 … R12-RF-6 |
| FALSIFIED | 2 | R12-FAL-1, R12-FAL-2 |
| DEFERRED-GENUINE | 1 | R12-DEF-1 |
| SCOPE-OPINION / OPINION | 0 | — |
| WITHDRAWN (by the leg, pre-board) | 5 | W-1 … W-5 |
| **Total canonical items** | **24** | Claude 2 MAJOR + 9 MINOR (11) → GNR-1, GNR-2, GNR-3 (MAJOR-1's third contradiction), GNR-4 … GNR-12. Grok 3 ESSENTIAL + 3 MAJOR + 2 NIT (8) → RF-1 (E1), RF-2 (E2), RF-3 (E3), RF-4 (M1), FAL-1 (M2), RF-5 (M3), FAL-2 (N1), RF-6 (N2). Gemini 1 MINOR + 2 NIT (3) → DEF-1 (M1), GNR-13 (N1), GNR-14 (N2). Plus ADJ-1, raised by neither party. |

**Genuinely-new-real total: 15 (14 GNR + 1 ADJ).**

## Classification table

| Grade | Count | Items |
|---|---|---|
| **Correctness-grade GNR** | **11** | GNR-1 (on-shell torsion irreps / O4 / O1 = O6), GNR-2 (artifact branch scope), ADJ-1 (Sec. II vs App. E normalization), GNR-3 (App. C trace-vector claim), GNR-4 (Levi-Civita symbol vs tensor), GNR-5 (Nieh–Yan conversion explanation), GNR-6 (`M̄_Pl` in an exact identity), GNR-7 (branch-vs-channel count), GNR-8 (Tier-III qualifier on 61–67 orders), GNR-9 (Table II vs abstract registers), GNR-10 (abstract independence claim) |
| Presentation-grade GNR | 4 | GNR-11 (Case I referent), GNR-12 (Shapiro–Teixeira arXiv note), GNR-13 (abstract sentence split), GNR-14 (density notation gloss) |

This is a **promotion** relative to the Claude leg's own tags on four items:
the leg classed MINOR-1, MINOR-2, MINOR-3 as `[presentation]` and MINOR-4,
MINOR-5, MINOR-8 as `[scope]`. Under the standing rule ("wrong
math/number/attribution/claim" = correctness-grade), a wrong convention name
attached to a sign-fixing identity, a wrong explanation for a printed
coefficient, an "exact" identity printed with the wrong symbol, and three
abstract claims wider than the body supports are all correctness-grade. Graded
up deliberately, and recorded so the grading is auditable rather than
convenient.

## Deferred-genuine list (carried, not closed)

1. **R12-DEF-1** — frozen-release Zenodo DOI for this survey's own verification
   scripts, now eight files rather than six. Owner: P-round packaging. Blocker:
   DOI minting is a publish action requiring Houston; the paper discloses the
   deposit as planned. Carried unchanged from R11-DEF-1.

## Process lesson (durable, and the reason this round is worth reading)

**A released verification artifact can be internally correct and still carry an
imposed premise it never solved for.** The 2026-08-07 module is a good module:
its rank, null space, Γ-route certification and Fierz results are all correct and
all re-confirmed here at finite γ. What it did not do was solve the equation
whose solution it reported. It substituted the answer and verified a tautology,
and because the substitution was stated as a verified fact — "is verified to be
pure axial" — three subsequent rounds, the manuscript, and a prior truth audit
all inherited it.

Two rules come out of this, and they generalize past this paper:

1. **Re-derive the premise, don't inherit it.** When a downstream claim rests on
   an artifact's premise rather than its computation, the premise is what needs
   checking. The operative test is whether the governing parameter of the
   framework appears anywhere in the module. Here γ — the Barbero–Immirzi
   parameter, the one parameter that distinguishes Einstein–Cartan–Holst from
   Einstein–Cartan — appeared nowhere in a module whose conclusions were reported
   as ECH results. That absence was mechanically detectable and nobody looked.
2. **Erratum by addendum, never by edit.** When a re-derivation overturns a prior
   artifact, append a dated addendum that scopes the original conclusions
   item by item and leave the original text untouched. The 2026-08-07 report's
   conclusions are still readable exactly as they were released, alongside a
   precise statement of which are now restricted to γ → ∞ and which stand. A
   silently corrected artifact would have destroyed the provenance that makes
   this ledger checkable.

And one observation about the board itself: the round's decisive finding came
from the leg that adjudicated a challenge **by solving the underlying equation
from scratch** — 24 free contorsion components, no irrep ansatz, two independent
routes, both Holst sign conventions. The two API legs, one of which returned the
paper's first ACCEPT-tier verdict and described the Cartan derivations as
"exact", did not touch it. Verdict words continue to be diagnostic feedback and
not a gate (directive H-refined), and this round is the sharpest instance of that
in the program's history: **the ACCEPT and the REJECT were both reviewing a
manuscript with a wrong on-shell torsion, and neither found it.**

## Closure evidence (v1C.0.15)

- `arxiv/paper1c_nogo_survey/main.tex` — `\paperVersion` `v1C.0.14` →
  `v1C.0.15`, `\paperTimestamp` `August 7, 2026` (machine-local date of the
  closure compile), no printed `\date`, provenance in `pdfkeywords` (verified:
  `pdfinfo` → `Keywords: v1C.0.15 (August 7, 2026)`). A v1C.0.15 changelog block
  is appended to the source header.
- Two new numbered equations: `eq:ech_onshell_torsion` (Sec. II) and
  `eq:o4_onshell` (Sec. V). Equation numbering downstream of Sec. II shifts by
  one; every cross-reference in the manuscript is `\eqref`-driven and no
  hard-coded equation number exists in the source (verified by grep).
- `research/theory_audit/operator_basis_adjudication_2026_08_07.md` — dated
  erratum addendum appended; nothing above it edited.
- `research/theory_audit/ech_torsion_onshell_2026_08_08.{py,json,md}` — the
  adjudicating module, cited in Data & Code Availability via `\artifact{}`.
- `references.bib` — unchanged, 26 entries; `\cite` / `.bbl` / `.bib` remain in
  exact three-way agreement.
- 4-pass compile (`pdflatex` ×1 → `bibtex` → `pdflatex` ×3): **0 LaTeX errors,
  0 undefined references, 0 overfull hboxes** (45 underfull, badness-only revtex
  float artifacts). The pre-existing `Warning--missing journal in
  DiegoPalazuelos2025` bibtex diagnostic is unchanged from v1C.0.14 and is not
  introduced by this round.
- **Two float regressions caught and fixed inside the round**, both confirmed
  new by compiling pristine v1C.0.14 from `git show HEAD:` in a clean directory
  (0 overfull, 24 pp): (a) Table III overflowed its full-width float by 28.5 pt
  once the O4/O5 cells carried γ-dependent values — fixed by compacting the
  rational expressions, abbreviating `(J⁵)² ≡ J⁵·J⁵` in the table body with a
  caption note, and setting `\footnotesize` on the tabular; (b) Table II became
  "too large for page by 22 pt" and stuck once the R2 cell lengthened — fixed by
  moving R12-GNR-9's reconciliation sentence out of the cell and into Sec. IV A
  prose, which is where a reader wants it anyway. Both warnings now zero.
- `/latex-audit`: **PASS.** Log scan clean. Pages 1 (title block + abstract), 2
  and 3 (conventions + the new torsion equation), 13 (Table II), 15 (Sec. V
  collapse bullets + the new O4 equation), 17 (Data & Code artifact block), 21
  (Table III), 22 (App. C scope) rendered at 130 DPI and visually confirmed — no
  column-gutter crossings, no right-margin overruns, no float escapes, no
  "(Dated:)" remnant. All **8** `\artifact{}` targets verified to resolve to
  existing repository paths. No `\date` overflow risk (no `\date`). Two raw
  `\texttt{}` filenames remain and are bare functional filenames, not directory
  paths (the R11-GNR-10 disposition), both wrapping at 0 overfull.
- `tools/p1c_consistency_check.py`: **4/4 rules PASS, exit 0** — run before the
  version bump and again after every table fix, per its own docstring and
  `ops/RUNBOOK.md`. Rules A–D are unaffected by this round's edits: the
  constraint count stays 14, Table II still carries exactly one `\textbf{(I)}`
  marker against nine prose sites, no assert/disclaim pair fires, and the
  abstract's closure claim is still the R11-GNR-3 joint form.
- Served PDF: **25 pp**, md5 `3a46b8c270906e0b943d7c0082f36922`, sha256
  `f3e29c45df35f7ac358d8f4e6a854d1b9f79fa20c71a725922732db82bd967d4`. Mirrored
  **byte-identical** (md5-verified, all four copies match) to
  `site/public/papers/`, `public/papers/` and `site/out/papers/` as
  `paper1c_nogo_survey_v1C.0.15.pdf`.
- `project-context/draft_paper_registry.json` — served alias bumped to
  `paper1c_nogo_survey_v1C.0.15.pdf`.
- `site/src/data/papers.ts` — P1C entry href and description updated to
  v1C.0.15.
- `site/src/data/reviewTimeline.ts` — R12 round entry added, plus a separate
  `kind: "skill-improvement"` entry for the solve-don't-inherit /
  erratum-by-addendum protocol lesson (newest-first).
- `cd site && npx next build` — **PASS**, 61 static pages generated, no errors.
- `project-context/SSOT/paper-1c/status.md` — R12 matrix including Gemini's
  ACCEPT, GNR by grade, the on-shell torsion correction as the round's headline,
  and R13 set as the next correctness check.

## Convergence read

**R-phase NOT converged at R12.** Eleven correctness-grade GNR items were found
and closed, two of them load-bearing physical claims, and the round overturned a
result one of this repository's own released artifacts asserted. The standing
rule (zero correctness-grade GNR on a full board) is not met, and it is not
close.

Four things are worth recording honestly:

1. **The defect class regressed, and that is the real news.** R10 and R11
   produced only internal-consistency defects — the manuscript disagreeing with
   itself. R12 found a wrong physical premise underneath the section the paper
   itself calls "the primary physical foundation of the no-go". Two rounds of
   "zero computational errors" measured what could be checked *from the PDF*;
   they could not have caught a premise that was wrong in the PDF and in the
   artifact and in the prior audit simultaneously.
2. **The mechanical guard did not fire, and could not have.**
   `tools/p1c_consistency_check.py` passed 4/4 on v1C.0.14. That is correct
   behaviour: the manuscript was self-consistent. Its four claims about torsion
   irreps, O4, O1/O6 and App. C's scope all agreed with each other. They were
   agreed and wrong. A self-consistency linter is the right tool for the R10/R11
   failure mode and structurally the wrong tool for this one.
3. **The verdict words were maximally uninformative this round.** Gemini
   returned an ACCEPT-tier verdict and called the Cartan derivations "flawless"
   and "exact"; Grok returned REJECT on length and self-containment.
   Neither engaged the operator-list branch question. The one leg that did found
   the round's only real findings. Recorded as the sharpest available evidence
   for directive H-refined.
4. **The correction weakens the claims and the conclusion survives.** O4 moves
   from "identically zero — a strictly stronger disposal" to a Planck-suppressed
   Fierz-closed contact term; O1 and O6 move from exact total derivatives to
   total derivative plus contact term. Every one lands in the disposal class the
   paper already establishes and bounds, at the same `M̄_Pl^{-2}` power, with an
   O(1) ratio to O5. No new light scale appears anywhere. The survey's
   conclusion is now stated on the branch its framework actually occupies.

R13 on the exact v1C.0.15 PDF is the next correctness-convergence check, and it
is the first round that will review an on-shell operator disposal derived from
the solved connection equation rather than from a substituted ansatz. No
readiness score has been computed and no venue/Zenodo kit exists for this draft.
