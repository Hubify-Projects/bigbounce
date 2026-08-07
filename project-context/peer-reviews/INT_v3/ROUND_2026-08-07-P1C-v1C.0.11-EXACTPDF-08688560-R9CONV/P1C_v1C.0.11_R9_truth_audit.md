# P1C v1C.0.11 — R9 correctness-convergence board truth audit (verdict-first), symbolic adjudication integration, and v1C.0.12 closure record

- **Round:** ROUND_2026-08-07-P1C-v1C.0.11-EXACTPDF-08688560-R9CONV — the R9
  correctness-convergence board on `arxiv/paper1c_nogo_survey/main.tex`, run
  against the R1 + R2 + R3 + R4 + R5 + R6 + R7 + R8 disposition ledgers
  (`INT_v3/ROUND_2026-08-06-P1C-v1C.0.3-EXACTPDF-85e53832/P1C_v1C.0.3_truth_audit.md`,
  `INT_v3/ROUND_2026-08-06-P1C-v1C.0.4-EXACTPDF-7ec5f221-R2CONF/P1C_v1C.0.4_R2_truth_audit.md`,
  `INT_v3/ROUND_2026-08-06-P1C-v1C.0.5-EXACTPDF-a770491d-R3CONF/P1C_v1C.0.5_R3_truth_audit.md`,
  `INT_v3/ROUND_2026-08-07-P1C-v1C.0.6-EXACTPDF-fc23872d-R4CONF/P1C_v1C.0.6_R4_truth_audit.md`,
  `INT_v3/ROUND_2026-08-07-P1C-v1C.0.7-EXACTPDF-f085023f-R5CONF/P1C_v1C.0.7_R5_truth_audit.md`,
  `INT_v3/ROUND_2026-08-07-P1C-v1C.0.8-EXACTPDF-385158dd-R6CONF/P1C_v1C.0.8_R6_truth_audit.md`,
  `INT_v3/ROUND_2026-08-07-P1C-v1C.0.9-EXACTPDF-b4d73f94-R7CONF/P1C_v1C.0.9_R7_truth_audit.md`,
  `INT_v3/ROUND_2026-08-07-P1C-v1C.0.10-EXACTPDF-d8b9db8e-R8CONF/P1C_v1C.0.10_R8_truth_audit.md`).
- **Exact artifact:** v1C.0.11 PDF, SHA-256
  `0868856032e2eee5f26cd207d9fe1cc9b1db2eae827eac41b70c9b2aea394b37`,
  20 pp (sha verified against the working tree before any edit).
- **Date:** 2026-08-07. Auditor: Claude (Fable 5) worker per CLAUDE.md
  directives B / H-refined / N. Rule applied: a finding that re-flags an
  R1–R8-dispositioned item is RE-FLAG unless the reviewer adds a genuinely
  new angle.

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
| Claude INT (Opus-tier subagent) | claude opus | `INT_v3/ROUND_2026-08-07-P1C-v1C.0.11-EXACTPDF-08688560-R9CONV/P1C_claude_r9_leg.md` | **MAJOR REVISION** (4 MAJOR / 11 MINOR; the leg self-classes 8 of its 15 findings correctness-grade) — includes a ~20-item verification log that independently re-derived the Route-2 contractions, the Eq. (4) integration, the Route-3 endpoints, the App. A hierarchy chain, the App. C Fierz matrix, the App. E benchmark chain, and all 25 bibliography entries, with zero numeric errors |
| Grok API | grok-4.3 | `ROUND_2026-08-07-P1C-v1C.0.11-EXACTPDF-08688560-R9CONV_P1C_Grok_brutal.md` | **REJECT** (3 ESSENTIAL / 3 MAJOR / 2 NIT, plus a pass-2 self-critique adding 3 MAJOR / 1 MINOR) |
| Gemini API | gemini-3.1-pro-preview | `ROUND_2026-08-07-P1C-v1C.0.11-EXACTPDF-08688560-R9CONV_P1C_Gemini_cosmology.md` | **MAJOR REVISIONS** (1 ESSENTIAL / 2 MAJOR / 2 MINOR / 1 NIT) |

**Failed legs (preserved as failure evidence, never counted, never hidden):**

- Perplexity leg: FAILED
  (`ROUND_2026-08-07-P1C-v1C.0.11-EXACTPDF-08688560-R9CONV_P1C_Perplexity_citations.md`
  is a failure record). Optional leg per directive I1; recorded as failed,
  never a verdict.

## The symbolic adjudication and its role in this round

Claude's MAJOR-1 and MAJOR-2 are both claims about the *mathematics* of
Sec. V — that `{O1–O6}` is linearly dependent, and that Table III's O1 row is
internally contradictory. Neither could be dispositioned by re-reading the
paper, because the paper's own released script (`dim4_parityodd_enumeration.py`)
verifies only Checks A and D and performs no rank computation. Adjudicating
them by re-arranging the identities the paper already quotes would have been
pattern-036 territory (closure fabricates its own math justification).

So the claims were referred out to an **independent symbolic computation**,
committed separately at `1130b7c5` before any closure edit was made:

- `research/theory_audit/operator_basis_adjudication_2026_08_07.py` (1102 lines)
- `research/theory_audit/operator_basis_adjudication_2026_08_07.json` (machine output, full tagged log)
- `research/theory_audit/operator_basis_adjudication_2026_08_07.md` (human-readable report)

It re-derives O1–O6 from the Cartan structure equations on an algebraically
independent 2-jet of `(e, ∂e, ∂∂e, ω, ∂ω, J⁵)`, expands all six over a common
basis of 1368 jet monomials, and reduces in exact rational arithmetic. Nothing
was taken from the paper's released script. Its headline verdict is
**PARTIALLY-CORRECT**, and it produced one correctness item **neither the
paper nor any referee raised**.

**Standing rule applied throughout this ledger:** every edit landed in
v1C.0.12 traces to a specific computed result in that JSON, cited by its
`[L##]` log tag. No result is restated in the paper that the computation did
not produce. Where the computation contradicts the referee, the referee is
falsified with the tag; where it contradicts the paper, the paper is corrected
with the tag.

Two new ID classes appear in this ledger as a result:

- **ADJ** — a genuinely-new-real correctness item originated by the
  adjudication rather than by any referee. ADJ items count toward the
  correctness-grade genuinely-new-real total exactly as GNR items do.

## Deduplicated finding ledger (canonical items, cross-leg map, verdicts, grades)

Verdict key: **GNR** = genuinely-new-real, referee-originated (real edit owed
and landed in v1C.0.12) · **ADJ** = genuinely-new-real, adjudication-originated
· **RE-FLAG** = re-flag of an R1–R8-dispositioned or disclosed item ·
**FALSIFIED** = disproved against the cited source/computation/render ·
**SCOPE-OPINION** / **OPINION** = style/venue position, dispositioned.
Grade key: **C** = correctness-grade · **P** = presentation-grade.

---

### R9-GNR-1 [C] — `{O1–O6}` is called a "basis" but is linearly dependent

- Legs: Claude MAJOR-1 (sole leg raising it as a rank claim; Grok D1 touches
  the adjacent script-cross-reference issue only).
- Verdict: **GNR, correctness-grade** — reviewer-correct on the structural
  claim, incorrect on the literal coefficients.
  - Rank: computed rank of the 6×1368 exact-rational coefficient matrix is
    **4**, nullity **2** `[L28]`, `[L29]`; confirmed independently by an
    exact-integer Gram certificate `[L34]` and by a separate 6×8 evaluation
    matrix from random exact-rational Einstein–Cartan configurations `[L58]`.
    So "six-member basis" is not defensible. **Reviewer-correct.**
  - `O1 ≡ O6`: exact, off shell `[L59]` and on shell `[L93]`. Certified by a
    completely independent route — the affine connection from the tetrad
    postulate, its own Riemann tensor from `Γ` alone, lowered with
    `g = ηee`; all 256 components match for three independent random
    exact-rational configurations, and the Γ-route `O6` equals the tetrad-form
    `O1` exactly (`−2162/147`, `21170/441`, `4588/441`, differences all 0)
    `[L49]`–`[L57]`. **Reviewer-correct.**
  - The referee's literal relation `O1 = O4 − O2`: **FALSE** `[L60]`. The
    residual is exactly `(−1/2)·O4` `[L61]`. The true relation is
    `O2 = ½·O4 − O1`, equivalently **`O1 = ½O4 − O2`**, residual identically
    zero `[L62]`, `[L63]`, cross-checked against the strict 4-form
    normalization `[L65]`. The referee's `1:1:1` coefficients carry a factor-2
    slip on O4 — traceable to the fact that **the paper never fixed the
    form-vs-density normalization of "NY"** in Eq. (8) or Table III `[L66]`.
    The paper's own omission caused the referee's error; both are fixed.
  - Rank modulo total derivatives: **2** `[L39]`, `[L40]`, `[L41]`.
  - The referee's proposed independent subset `{O2,O3,O4,O5}` is indeed
    independent, rank 4 `[L35]`.
  - Robustness of the verdict to a reading ambiguity: if `O6` were built from
    the Levi-Civita curvature `R̊` instead, `O6 = 0` identically `[L104]` and
    the rank of the remaining five is still 4 `[L105]`, `[L106]`. **Rank is 4
    under both readings**, so no part of this disposition rests on resolving
    that ambiguity.
- Closure (v1C.0.12): Sec. V retitled "The Operator-List Argument"; every
  `{O1–O6}` surface — abstract (`main.tex` abstract block), Sec. I intro,
  Contributions, Sec. V head, Sec. V construction rule, Sec. VI scope,
  Sec. VII conclusions, App. A 1 head — now reads **spanning list /
  generating set**, never "basis", with the redundancy stated as deliberate
  and the reason given (each entry is a separately *recognizable* invariant).
  A new subsection *"The list is a spanning list, not a basis"* states the
  rank-4/nullity-2 result and displays both relations as
  Eq.~\eqref{eq:dim4_relations}:
  `O1 − O6 = 0` and `2·O1 + 2·O2 − O4 = 0` (equivalently `O1 = ½O4 − O2`),
  together with the rank-2-modulo-total-derivatives statement and the maximal
  independent subsets. Eq. (8)'s Nieh–Yan entry is now fixed explicitly in the
  density normalization, new Eq.~\eqref{eq:ny_norm}
  `NY ≡ ∂_μ(ε^{μνρσ} e_{Iν} T^I_{ρσ})`, with a sentence stating *why* the
  normalization must be pinned. Eq. (8)'s `ε` is now declared as the spacetime
  Levi-Civita symbol with `ε^{0123}=+1`, `R` as the torsionful curvature, and
  the two schematic entries O1 and O5 are written out as their unique admitted
  contractions in the following prose (with the reason `ε_{IJKL}` is
  inadmissible for O1). **The completeness claim is re-worded to exactly what
  the computation supports**: the list is asserted to *span* the rule-admitted
  space; independence is explicitly not claimed. The adjudication script is
  cited via `\artifact{}` at the relations block.

### R9-ADJ-1 [C] — Table III's O1/O6 "Final = 0" is right, but its stated reason is branch-restricted

- Legs: none. **Adjudication-originated** (`§5` of the adjudication report),
  surfaced while falsifying Claude MAJOR-2 (see R9-FAL-1).
- Verdict: **ADJ, correctness-grade.** Check A was independently reproduced —
  a generic Riemann with pair antisymmetry plus the first Bianchi identity
  (20 free components remaining) gives `ε^{μνρσ}R_{μνρσ} = 0` `[L70]` — but
  that Bianchi identity is the **torsion-free** one, precisely what
  `T = κS ≠ 0` violates `[L71]`. On an explicit Levi-Civita configuration all
  of O1, O2, O4, O5, O6 vanish and only O3 survives `[L72]`, `[L73]`, `[L74]`.
  On shell O1 is **not** pointwise zero (`91/405` in the computed curved
  on-shell configuration) `[L91]`, `[L92]`. So "vanishes (Bianchi, Check A)"
  is correct **only on the torsion-free branch**. The *outcome* `Final = 0`
  survives (see R9-FAL-1); the *reason* as printed does not.
- Closure (v1C.0.12): Table III's O1 row Fate column now reads
  `0 at T=0 (Bianchi, Check A); −NY at T=κS`, Final `0 (EOM)`; the O6 row
  reads `= O1 exactly (tetrad conversion); same fate`, Final `0 (EOM)`.
  Check A's prose in App. A 1 now states explicitly that the branch
  restriction is not cosmetic and gives the off-branch disposal. Sec. V
  bullet (a) carries the same qualifier. The abstract's trichotomy is
  re-scoped so "identically vanishing by the algebraic Bianchi identity" is
  bound to the torsion-free branch, with the `T = κS` branch behaviour stated.

### R9-ADJ-2 [C] — Table III's O4 row, its caption, and the App. A 1 `O4^[4] = O5^[4]` chain are wrong as printed

- Legs: none. **Adjudication-originated; neither the paper nor any referee
  raised it.** This is the round's structural finding.
- Verdict: **ADJ, correctness-grade.**
  - v1C.0.11 Table III listed O4 with Fate (bare) `→ κ²(J⁵·J⁵), Fierz basis`
    and Final `κ(J⁵·J⁵)`; the caption repeated it ("the two genuine
    dimension-4 densities O4 and O5 landing on the same operator
    κ(J⁵·J⁵)"); App. A 1 asserted the chain
    `O4^[4] = M_Pl²·κ²(J⁵·J⁵) = κ(J⁵·J⁵) = O5^[4]`; and Sec. V collapse
    bullet (b) inherited the same conflation.
  - Computed: **`O4 ≡ 0` on shell** `[L78]`, `[L81]`, confirmed in a genuine
    *curved* on-shell Einstein–Cartan configuration built by solving the
    Cartan equation for `ω` at `T = κS ≠ 0` (max `|T^I_{μν}| = 121/972`)
    `[L90]`, `[L94]`.
  - Reason, computed: `O4 = T_I∧T^I` is supported only by the **non-axial**
    torsion irreps — zero on the pure vector irrep `[L83]`, zero on the pure
    axial irrep `[L84]`, nonzero only on the tensor irrep and on
    vector×axial cross terms `[L82]`, `[L85]`, `[L86]`. Minimal-ECH Cartan
    torsion is verified **pure axial** (vector part zero, tensor part zero)
    `[L09]`. Hence `O4 ≡ 0`.
  - Root cause identified: Check D proves
    `S_abc S^abc = −(3/8)(J⁵·J⁵)` — reproduced exactly here as
    `T_abc T^abc = −(3/8)κ²(J⁵·J⁵)` `[L87]` — but that is the **ε-free,
    parity-even** square `T_abc T^abc`, a *different invariant* from
    `O4 = ε^{μνρσ}T^I_{μν}T_{Iρσ}` as defined in Eq. (8) `[L86]`. The paper
    applied Check D's identity to the wrong contraction.
  - O5, by contrast, reproduces its Table III fate exactly:
    `O5 → (−3/2)·κ(J⁵·J⁵)` `[L79]`, `[L80]`, `[L88]`.
  - **This STRENGTHENS the no-go.** An operator contributing nothing at all is
    a strictly stronger disposal than one contributing a Planck-suppressed
    contact term `[L89]`. The physics conclusion is unchanged: the net
    on-shell picture is that every member is an exact total derivative (O2,
    O3, and O1 = O6 = −O2) or identically zero (O4), with a single operator
    carrying nonzero vacuum-energy content, `O5^[4] = (−3/2)κ(J⁵·J⁵)` —
    Planck-suppressed and inside the Fierz-closed basis `[L88]`, `[L100]`.
- Closure (v1C.0.12), all three printed sites plus the two prose sites that
  inherit the conflation:
  1. **Table III row O4** — Fate now `0 (pure-axial T; needs non-axial irreps)`,
     Final `0`.
  2. **Table III caption** — the "two genuine dimension-4 densities O4 and O5
     landing on the same operator" sentence is deleted and replaced by the
     computed picture (exactly one entry, O5, carries vacuum-energy content,
     at `−(3/2)κ(J⁵·J⁵)`; O4 vanishes identically; O1 = O6 is 0 on the
     torsion-free branch and `−O2` on the `T = κS` branch).
  3. **App. A 1 `O4^[4] = O5^[4]` chain** — replaced by the irrep-support
     argument, with the `M_Pl²κ² = κ` identity retained only where it is
     actually needed and explicitly flagged as *not* what disposes of O4.
  4. **App. A 1 Check D** — retitled and rewritten to attribute the identity
     to the ε-free square `T_abc T^abc`, to state that it is a different
     invariant from O4 and does not dispose of it, and to give what Check D
     *does* establish (the O5 reduction).
  5. **Sec. V collapse bullet (b)** — same correction; the O4 sentence now
     states pure-axial vanishing, and the Fierz reduction is attributed to O5
     alone.
  Downstream class statements updated for consistency: Sec. V's three-way
  collapse sentence, App. A 1's Verdict paragraph, and the abstract's
  trichotomy. Table III's O5 row and the App. A 1 text now also carry the
  exact rational factor `−3/2` `[L79]`, `[L80]`, which the computation
  produced and v1C.0.11 had left implicit. Adjudication script cited via
  `\artifact{}` at both the App. A 1 and Data-and-Code sites.

### R9-FAL-1 [C] — "Table III's O1 row is an internal contradiction" — FALSIFIED

- Legs: Claude MAJOR-2.
- The claim: by Nieh–Yan `O1 = O4 − O2 → κ(J⁵·J⁵) − 0`, so Table III "reads
  `0 = κ(J⁵·J⁵) − 0`, an internal contradiction between two of its own rows."
- Verdict: **FALSIFIED**, source-cited to the computation. The inference
  presumes `O4 → κ(J⁵·J⁵) ≠ 0` on shell. It does not: `O4 ≡ 0` `[L78]`,
  `[L81]`, `[L94]` (see R9-ADJ-2). With `O4 = 0` the verified Nieh–Yan
  relation gives `O1 = −O2` exactly — confirmed numerically, `O1 + O2 = 0`
  `[L95]`, `[L97]`. So on shell O1 **is** minus the Nieh–Yan total
  derivative: not pointwise zero `[L92]`, but contributing **zero to the
  equations of motion and zero to the vacuum energy** — exactly the status
  Table III itself assigns rows O2 and O3 ("`0` (EOM)"). **Table III's
  `Final = 0` for O1 therefore survives** `[L98]`, and the referee's
  "internal contradiction" is falsified `[L99]`, `[L114]`.
- No edit owed *to this claim*. The referee's requested fix — "add
  `→ κ(J⁵·J⁵) via Nieh–Yan when T = κS` to the O1 row" — would have
  introduced a new error into Table III, and was not applied. What *was*
  applied is the separate, adjudication-originated correction to the row's
  stated **reason** (R9-ADJ-1). Recorded here so the distinction is not lost:
  the referee identified the right row for the wrong reason.

### R9-GNR-2 [C] — Route-3: `H` vs `H0` inconsistency

- Legs: Claude MAJOR-3, point 3.
- Verdict: **GNR, correctness-grade.** Verified against the exact PDF:
  Sec. IV B wrote the suppression factor as `(Δγ/γ)·(H/M_Pl)` with an
  unspecified epoch, while the paragraph one column earlier wrote
  `(Δγ/γ)·(H0/M_Pl)`. At the bounce `H/M_Pl = O(1)`, so as printed the two
  statements differ by ~61 orders. Genuinely new — no R1–R8 item touches the
  Hubble symbol.
- Closure (v1C.0.12): the symbol is `H0` uniformly, and a sentence now states
  explicitly why (`H0`, not a bounce-epoch `H`, is the correct insertion,
  because the claim is about the late-time dark-energy channel).

### R9-GNR-3 [C] — Route-3: no displayed density relation; the reference budget is undefined

- Legs: Claude MAJOR-3, points 1 and 2.
- Verdict: **GNR, correctness-grade**, with a partial falsification recorded
  under R9-RF-2. The blanket claim "the 61–67 headline is never derived" is a
  long-running re-flag lineage (R5-RF-3 → R6-RF-8 → R7-RF-6 → R8-FAL-2), and
  the referee's own verification log confirms the arithmetic reproduces:
  `0.3 × 1.18×10⁻⁶¹ → 61` orders and `1.4×10⁻⁶ × 1.18×10⁻⁶¹ → 67` orders.
  But two sub-claims are genuinely new and correct on inspection of the exact
  PDF: (i) unlike Routes 1, 2 and 4, Route 3 had **no displayed expression**
  for its contribution to `ρ_Λ`; and (ii) the phrase "the dimensionless
  parity-odd amplitude budget associated with a dark-energy-scale source" is
  **defined nowhere in the manuscript**, so the first sentence stated a
  suppression relative to an undefined quantity while the second stated one
  relative to `ρ_Λ,obs`. Those are different denominators and the step between
  them was never made. Real, and owed.
- Closure (v1C.0.12): a displayed mass-dimension scaling relation is added,
  Eq.~\eqref{eq:r3_density}, `ρ_R3/ρ_Λ,obs ∼ (Δγ/γ)(H0/M_Pl)`, with the
  reference budget named explicitly as `ρ_Λ,obs ≈ (2.25 meV)⁴` and the
  saturation of the single inverse Planck power by `H0` stated. Both numeric
  endpoints are now evaluated inline from the displayed relation. The
  evidentiary status is labelled in place: a Tier-III mass-dimension scaling
  relation, **not** a derived stress-tensor matching — and the paper says so,
  restating that it does not supply and does not claim the cosmological stress
  tensor a genuine mapping would require. No margin, count, or headline number
  changed.

### R9-GNR-4 [C] — Route-2: the App.-A bridge sentence mis-describes Eq. (1)

- Legs: Claude MAJOR-4.
- Verdict: **GNR, correctness-grade**, with a partial falsification of the
  surrounding framing claim. The framing half of MAJOR-4 ("Route 2 is
  presented as a dark-energy closure") is largely **falsified against the
  printed text**: v1C.0.11 already stated the per-route metric at the head of
  Sec. IV ("for Route 2 the budget is evaluated against the *observed
  birefringence amplitude*, for Route 3 against the *observed dark-energy
  density*"), and the abstract already said Route 2 "closes against the
  observed birefringence amplitude" — this is the landed closure of R1-GNR-4.
  What is genuinely new and genuinely wrong is the bridging sentence: it
  called Eq. (1) "the off-shell dimension-(+1) parity-odd operator", when the
  paper takes pains elsewhere to show Eq. (1) carries dimension
  `−1 + 2 + 3 = +4` with no deficit at all. The dimension-(+1) object is
  Eq. (6)/(7), the phenomenological representative. A category error in a
  load-bearing bridge sentence. Real, and owed.
- Closure (v1C.0.12): the bridge sentence is rewritten — Route 2's
  *dark-energy* closure is now stated as inherited from the Sec. V
  operator-list argument and the App. A single-scale NDA bound, with a
  parenthetical making explicit that the dimension-(+1) object bounded
  directly in App. A is Eq. (6), not Eq. (1). A scoping paragraph is added at
  the head of Sec. IV stating the division of labour once: Sec. IV A closes
  the *birefringence* channel; Route 2's dark-energy closure is inherited;
  Route 3 is bounded directly against `ρ_Λ,obs`.

### R9-GNR-5 [P] — "dimensionless coefficient … multiplied by the Planck mass to a single negative power"

- Legs: Claude MINOR-1.
- Verdict: **GNR, presentation-grade.** Correct as stated: a dimensionless
  coefficient multiplied by `M_Pl⁻¹` is not dimensionless. The next sentence
  already got the bookkeeping right, so this is a wording slip, not a
  dimensional error in the physics.
- Closure (v1C.0.12): reworded — the prefactor is `α_em/(4π)`, a dimensionless
  loop factor, times a single inverse power of the Planck mass; the product
  carries mass dimension `−1` and is not itself dimensionless.

### R9-GNR-6 [C] — "natural coefficient ∼ `M_Pl⁴`" contradicts the dimensionless-`c_n` contract

- Legs: Claude MINOR-2.
- Verdict: **GNR, correctness-grade.** By the paper's own construction
  (Sec. V: each `c_n O_n^[4]` is a bona-fide dimension-4 density with `c_n` a
  dimensionless rational), `M_Pl⁴` is the natural **density / vacuum-energy
  scale**, not the coefficient. As printed the phrase contradicted the
  contract the same paragraph establishes. Recurred in the Table III caption,
  in App. A 1's Check D paragraph, and in App. A 1's Verdict paragraph.
- Closure (v1C.0.12): all occurrences reworded to "natural *density* scale
  ∼ `M_Pl⁴` … carried by a dimensionless Wilson coefficient".

### R9-GNR-7 [P] — Sec. V bullet (b) retargets the parity cross-reference to the wrong appendix

- Legs: Claude MINOR-3.
- Verdict: **GNR, presentation-grade**, and a **closure-insufficiency of
  R7-GNR-2** (a genuinely new angle). R7-GNR-2 correctly stopped Sec. V(b)
  from labelling the parity-even Fierz image "parity-odd"; its closure added
  "itself parity-even (Appendix~\ref{app:parity})". But App. B classifies only
  the Route-2 operator `∂_μϑ_NY J^{5μ}` and says nothing about `(J⁵)²`; the
  statement that a Lorentz-scalar product of two axial currents is P-even
  lives in B8 (Sec. III A). The R7 fix pointed at the wrong target.
- Closure (v1C.0.12): the cross-reference is retargeted to B8, Sec. III, with
  the reason given inline.

### R9-GNR-8 [C] — Eq. (3) is claimed "structurally consistent" with the Benedetti–Speziale flow

- Legs: Claude MINOR-4.
- Verdict: **GNR, correctness-grade.** Verified against the printed
  equations: Eq. (3), `dγ/d ln μ = (N_F^L − N_F^R)γ/12π²`, has its only fixed
  point at `γ = 0`, has **no** fixed point at `γ² = 1`, and is purely
  logarithmic where Eq. (4) is power-suppressed by `μ²κ̃²`. The two flows are
  structurally incompatible; only the numerical inequality
  `0.3 ≫ 1.4×10⁻⁶` is defensible.
- Closure (v1C.0.12): the structural-consistency claim is withdrawn and
  replaced by an explicit statement of how the two flows differ, followed by
  the one thing that is defensible and the only thing used — the numerical
  bound. No number changed.

### R9-GNR-9 [P] — "genuine dimension-4" carries three senses within two columns

- Legs: Claude MINOR-5.
- Verdict: **GNR, presentation-grade.** Terminology collision, correctly
  diagnosed.
- Closure (v1C.0.12): the term is defined once, at Eq. (9), and reserved for
  the promoted operators `O_n^[4]` — *all six* of which carry mass dimension
  exactly `+4` — with the two competing senses explicitly excluded. The
  worst-offending instance ("the two genuine dimension-4 densities O4 and
  O5") is removed by R9-ADJ-2's rewrite anyway.

### R9-GNR-10 [C] — App. D Step 4 drops the Holst `γ⁻¹` prefactor

- Legs: Claude MINOR-6.
- Verdict: **GNR, correctness-grade** (immaterial to the theorem, as the
  referee notes). The Holst term carries the explicit `γ⁻¹` introduced in
  Sec. II; the printed reduction to `½ε^{μνρσ}R_{μνρσ}(Γ̊)` dropped it, so as
  written the reduction was not an equality. The expression vanishes
  identically, so App. D's theorem is unaffected.
- Closure (v1C.0.12): the prefactor is restored,
  `(1/2γ)ε^{μνρσ}R_{μνρσ}(Γ̊)`, with the Sec. II convention cited.

### R9-GNR-11 [P] — "parity-odd/dark-energy channels" reads as classifying all four routes parity-odd

- Legs: Claude MINOR-7.
- Verdict: **GNR, presentation-grade.** The slash is disjunctive, but B8 and
  Sec. V both establish that R1's operator `(J⁵)²` is parity-**even**, so a
  referee should not have to infer it.
- Closure (v1C.0.12): both instances (abstract, Sec. IV C) now read "parity-odd
  **or** dark-energy channels".

### R9-GNR-12 [C] — the "13 distinct" criterion is applied rigorously to exactly one pair

- Legs: Claude MINOR-8.
- Verdict: **GNR, correctness-grade**, and a genuinely new angle on a
  re-flagged family. R8-RF-5 dispositioned the blanket "'13 distinct' is not
  supported" claim; MINOR-8 instead names a **specific pair never
  adjudicated** — B11 (Decoupling Universality) and B13 (Gravitational
  Democracy) — and observes that Sec. III's criterion ("no barrier is a
  logical consequence of another") is argued at length only for B8 vs B14.
  The observation is fair and the remedy is cheap.
- Closure (v1C.0.12): an explicit independence argument is added to B13 —
  B11 concerns universality across the *gauge* sector and says nothing about
  relative couplings among fermion species; B13 concerns democracy across the
  *matter* sector and permits a channel-selective gauge sector; neither
  implies the other, and neither is implied by B4, which fixes the coupling's
  *magnitude* but not its *universality*. The count is unchanged at 13, and is
  now supported by an argument rather than by fiat.

### R9-GNR-13 [P] — Ref. [13] carries no peer-review status label

- Legs: Claude MINOR-10.
- Verdict: **GNR, presentation-grade.** Verified: Refs. [1] and [14] are
  scrupulously labelled "not an arXiv preprint and not peer reviewed", while
  Diego-Palazuelos & Komatsu (arXiv:2509.13654) carried neither a journal
  reference nor a status label. Asymmetric standard. (R7-RF-13 verified the
  reference *exists* via live arXiv fetch; it did not address labelling —
  genuinely new.)
- Closure (v1C.0.12): `references.bib` entry gains
  `note = "arXiv preprint; no journal reference at time of writing."`

### R9-GNR-14 [P] — the O(10¹⁰) robustness claim is asymmetric between routes

- Legs: Claude MINOR-11.
- Verdict: **GNR, presentation-grade.** Sec. VI claimed robustness to
  `O(1)–O(10¹⁰)` rescalings for both R2 and R3, but the explicit `10¹⁰` stress
  test was displayed only for Route 2 (`≳48` orders). The Route-3 analogue is
  true and one line long.
- Closure (v1C.0.12): Sec. VI now states both — the displayed Route-2 test
  leaving `≳48` orders, and the same inflation on Route 3's pessimistic lower
  endpoint leaving `≳51` orders.

---

### R9-SO-1 [P] — rename `dim4_parityodd_enumeration.py` (deferred-genuine)

- Legs: Claude MINOR-9; Grok D1 (pass-2).
- Verdict: **SCOPE-OPINION, deferred-genuine (P-round packaging).** The
  substance is agreed and already disclosed: the referee read the 218-line
  script, confirmed it contains exactly `[CHECK A]` and `[CHECK D]` and
  performs no enumeration, and confirmed the paper discloses this three times.
  Grok's stronger form — that the cross-reference is "self-contradictory" — is
  **partially falsified**: the paper states the discrepancy explicitly at
  every citation site, which is the opposite of a hidden contradiction. The
  honest fix (rename the file) cannot land in this round without invalidating
  the pinned immutable commit that four other artifact links resolve against;
  it belongs to the archival deposit. Added to the deferred-genuine list.
- Also recorded: the referee independently verified all four (now six)
  Data-and-Code artifacts exist and that commit `c80b7487` matches its quoted
  short SHA.

### R9-RF-1 — companion results are load-bearing and unrefereeable

- Legs: Grok E1 (ESSENTIAL); Gemini M1 (MAJOR).
- Verdict: **RE-FLAG** of R6-GNR-1 (which landed App. E) / R7-RF-2 / R8-RF-3 /
  R8-RF-10, with a **partial falsification**: Grok's specific demand names the
  `−(3κ/16)[γ²/(1+γ²)]` contact coefficient and the `3.6×10⁻⁶⁹` benchmark as
  un-reproduced, and both are carried self-contained in App. E since
  v1C.0.9 — this round's Claude leg independently recomputed the entire App. E
  chain (`κn_ψ² = 9.96×10⁻⁸⁰ eV⁴` vs quoted `1.0×10⁻⁷⁹`; `3.56×10⁻⁶⁹` vs
  quoted `3.6×10⁻⁶⁹`; `Q_γ Q_γ⁻¹ = 1`; Eq. (E4) matching the Sec. II
  coefficient) with zero errors. The residual cited-only items (NJL gap
  equation, tensor-sector extension, R4 spectator-ALP check) are labelled
  not-peer-reviewed in place, per directive P (companion sequencing is
  publishing-phase, not a manuscript defect). RE-FLAG confirmed.

### R9-RF-2 — abstract's numbers are never recomputed from displayed inputs

- Legs: Grok E2 (ESSENTIAL).
- Verdict: **RE-FLAG** of R1-FAL-2 / R2-RF-3 / R3-RF-3 / R8-FAL-2, with a
  **partial falsification** on this round's own evidence: the Claude leg
  independently reproduced both Route-3 endpoints and the Route-2 budget from
  inputs displayed in the PDF alone. The one real gap Grok's family of claims
  pointed at — no *displayed equation* for Route 3's `ρ_Λ` contribution — is
  split out and closed as R9-GNR-3. RE-FLAG confirmed for the remainder.

### R9-RF-3 — abstract overstates the evidentiary status of R2/R3

- Legs: Grok E3 (ESSENTIAL).
- Verdict: **RE-FLAG** of R5-RF-1 / R8-RF-4, with a **partial falsification**:
  the abstract already carries the explicit three-tier evidentiary
  classification, already states "only the perturbation-transparency result is
  a Tier-I rigorous theorem", and already says "Neither route is presented as
  a viable mapping … this survey closes them as bounded amplitude budgets".
  RE-FLAG confirmed.

### R9-RF-4 — reclassify Table I into three explicit tiers

- Legs: Grok M1 (MAJOR).
- Verdict: **RE-FLAG** of R3-RF-8 / R8-RF-5, **falsified in part**: the
  requested three-tier table already exists as Table II
  (`tab:evidentiary_status`), and B9's heuristic status and the five
  general-naturalness entries are labelled as such in the catalog text.
  RE-FLAG confirmed.

### R9-RF-5 — Fig. 1 caption lacks a tier legend

- Legs: Grok M2 (MAJOR).
- Verdict: **RE-FLAG** of R7-GNR-6 (which added the evidentiary-status
  statement to the caption) / R7-RF-5 (redraw tier-segregated). The remaining
  ask is a per-arrow tier legend, a D-round visual item. RE-FLAG confirmed.

### R9-RF-6 — 20 pages is too long for CQG

- Legs: Grok M3 (MAJOR).
- Verdict: **RE-FLAG** of R2-RF-7 / R3-RF-7 / R6-RF-4; venue-length
  condensation is on the deferred-genuine list. SCOPE position, not a defect.
  RE-FLAG confirmed.

### R9-RF-7 — the novelty quantification is unsupported

- Legs: Grok G1 (pass-2 MAJOR).
- Verdict: **RE-FLAG** of R6-RF-5. The paper's parenthetical already scopes
  the nine-novel count as "not a rigor or specificity claim". RE-FLAG
  confirmed.

### R9-RF-8 — `3.6×10⁻⁶⁹` vs `3.9×10⁻⁶⁹` "never reconciled or flagged"

- Legs: Grok J1 (pass-2 MAJOR).
- Verdict: **RE-FLAG** of R4-GNR-3 (adjudicated then: both values correct
  under different `ρ_Λ` normalizations), with the specific sub-claim
  **FALSIFIED against the printed text** — v1C.0.11 reconciles the two values
  explicitly in *two* places (Sec. II and App. E), each stating the
  normalization and "identical at the order-of-magnitude precision". The
  discrepancy is neither unflagged nor unreconciled. RE-FLAG confirmed, no
  edit owed.

### R9-RF-9 — deposit the code under a frozen DOI now

- Legs: Gemini E1 (ESSENTIAL).
- Verdict: **RE-FLAG** of R2-SO-2 / R5-GNR-2 / R6-RF-9 / R7-RF-7 / R7-RF-8 /
  R8-RF-11. Deferred-genuine; per directive P the archival deposit is a
  publishing-phase step, not a manuscript defect, and the scripts are in the
  interim pinned to an immutable commit whose contents were verified identical
  to head this round. RE-FLAG confirmed.

### R9-RF-10 — internal audit tags in the artifact file paths; `arxiv/` directory name

- Legs: Gemini M2 (MAJOR); Gemini m2 (MINOR).
- Verdict: **RE-FLAG** of R2-RF-9 / R6-GNR-7 / R7-RF-10. The prose tags were
  removed at R6-GNR-7; what remains are the literal committed filenames, which
  must match the repository for the links to resolve. Renaming both the
  `research/theory_audit/` files and the `arxiv/` directory is the same
  P-round packaging action as R9-SO-1 and rides with it. RE-FLAG confirmed.

### R9-RF-11 — remove the internal version tag from the date line

- Legs: Gemini m1 (MINOR).
- Verdict: **RE-FLAG** of R1-SO-1 / R2-RF-1 / R3-RF-1 / R4-RF-7 / R5-RF-5 /
  R6-RF-1 / R7-RF-1 / R8-RF-1. The `\date{... (\paperVersion)}` stamp is
  mandated by directive G for every in-flight round and is stripped at
  submission packaging. RE-FLAG confirmed.

---

### R9-FAL-2 — Eq. (2) is "over-suppressed by one power of `M_Pl`"

- Legs: Grok C1 (pass-2 MAJOR).
- Verdict: **FALSIFIED**, and a re-flag of R8-RF-9 / R6-GNR-2 / R2-GNR-7. The
  LHS is a *double* normalization — by the observed angle **and** by the
  dimensionless strength `M_Pl(α/M) ∼ 10⁻²` of the R4-fitted coupling — which
  v1C.0.11 states explicitly in the three lines following the equation. The
  two displayed lines are mutually consistent: this round's Claude leg
  independently verified `1/[M_Pl(α/M)] = M/(α M_Pl)` and reproduced the
  numerical evaluation `1.7×10⁻⁶⁰` plus the alternative contraction
  `1.7×10⁻⁶²`. No `M_Pl` is redundant. No edit owed.

### R9-FAL-3 — Eq. (2)'s numerical substitution contains a typesetting slip

- Legs: Grok N2 (NIT).
- Verdict: **FALSIFIED.** The printed substitution is
  `10⁻³·10⁻⁶¹/(10⁻²·6×10⁻³) ≈ 10⁻⁶⁰`; evaluating,
  `10⁻⁶⁴ / 6×10⁻⁵ = 1.67×10⁻⁶⁰`. Correct as printed, and Grok's own text
  concedes it "evaluates correctly". No slip exists. No edit owed.

### R9-FAL-4 — "gauge-invariaut" typo in Sec. V

- Legs: Gemini N1 (NIT).
- Verdict: **FALSIFIED — text-extraction artifact.** `main.tex` contains no
  such string, and `pdftotext` on page 10 of the exact v1C.0.11 PDF returns
  "gauge-invariant" at every occurrence. This is the same failure family as
  R3-FAL-2 → R5-RF-7 / R5-FAL-1 → R7-FAL-1 → R8-FAL-4: a reviewer's PDF
  ingestion pipeline mis-rendering glyphs and reporting the artifact as a
  manuscript defect. No edit owed.

### R9-OP-1 — "the companion paper" phrasing is repetitive

- Legs: Grok N1 (NIT).
- Verdict: **OPINION**, presentation-grade style position. Dispositioned; the
  repetition is load-bearing attribution hygiene that other legs have
  repeatedly credited. No edit owed.

---

## Candidate findings withdrawn by the reviewing leg itself

Recorded per the leg's own request, so the board can distinguish "checked and
clean" from "not checked". Both were self-withdrawn by the Claude leg after
re-rendering at high DPI, **before** the report was filed — they were never
live findings and are not counted in any total:

1. **B1 torsion-coupling exponent (p. 4).** Low-DPI text extraction rendered
   the relation as `|t3| ∼ m_T⁻¹`, dimensionally inhomogeneous with the
   displayed `g_eff ∼ 1/(M_Pl√|t3|) ∼ H0/M_Pl`. Re-rendered at 260 DPI, the
   printed relation is `√|t3| ∼ m_T⁻¹`, giving
   `g_eff ∼ m_T/M_Pl = H0/M_Pl ∼ 10⁻⁶¹` — correct as printed. Withdrawn.
2. **Fig. 1 barrier→route arrows (p. 4).** At low resolution R3 appeared to be
   missing its Branch L/M arrow. At 400 DPI the counts are R1 = 3, R2 = 4,
   R3 = 4, R4 = 3 (14 total), matching the class-level bracket assignments of
   Sec. III A exactly. Figure and text agree. Withdrawn.

Both are further instances of the extraction/rasterization artifact family
(see R9-FAL-4). The leg's method note — re-render at 200–400 DPI before
asserting any math claim — is the mitigation, and it worked.

## Ledger totals

| Verdict | Count | Items |
|---|---|---|
| GENUINELY-NEW-REAL, referee-originated (closed in v1C.0.12) | **14** | R9-GNR-1 … R9-GNR-14 |
| GENUINELY-NEW-REAL, adjudication-originated (closed in v1C.0.12) | **2** | R9-ADJ-1, R9-ADJ-2 |
| RE-FLAG (of an R1–R8 disposition or a disclosed limitation) | 11 | R9-RF-1 … R9-RF-11 |
| FALSIFIED (source- or computation-cited) | 4 | R9-FAL-1 … R9-FAL-4 |
| SCOPE-OPINION (deferred-genuine) | 1 | R9-SO-1 |
| OPINION (dispositioned) | 1 | R9-OP-1 |
| **Total canonical items** | **33** | Dedupe notes: Grok E1 + Gemini M1 → R9-RF-1; Gemini M2 + m2 → R9-RF-10; Claude MINOR-9 + Grok D1 → R9-SO-1. Claude MAJOR-2 splits into R9-FAL-1 (the claim, falsified) and R9-ADJ-1 (the real defect the adjudication found underneath it). Claude MAJOR-3 splits into R9-GNR-2, R9-GNR-3, and the re-flagged remainder R9-RF-2. Claude MAJOR-4 splits into R9-GNR-4 and a partial falsification recorded in place. |

**Genuinely-new-real total: 16 (14 GNR + 2 ADJ).**

## Classification table (all findings, by grade)

| Item | Legs | Verdict | Grade | Disposition |
|---|---|---|---|---|
| R9-GNR-1 | Claude M1 | GNR | C | Spanning-list re-frame; both relations displayed; NY normalization fixed |
| R9-ADJ-1 | adjudication | ADJ | C | Table III O1/O6 reason branch-scoped; abstract trichotomy scoped |
| R9-ADJ-2 | adjudication | ADJ | C | Table III O4 row + caption + App. A 1 chain + Check D + Sec. V(b) corrected |
| R9-FAL-1 | Claude M2 | FALSIFIED | C | "Internal contradiction" disproved; `Final = 0` stands; no edit to the claim |
| R9-GNR-2 | Claude M3.3 | GNR | C | `H` → `H0` uniform, with reason stated |
| R9-GNR-3 | Claude M3.1–2 | GNR | C | Displayed Eq. for `ρ_R3/ρ_Λ,obs`; reference budget defined; Tier-III labelled |
| R9-GNR-4 | Claude M4 | GNR | C | App.-A bridge corrected; Sec. IV scoping paragraph added |
| R9-GNR-5 | Claude m1 | GNR | P | Prefactor dimensional wording |
| R9-GNR-6 | Claude m2 | GNR | C | "natural coefficient" → "natural density scale" (3 sites) |
| R9-GNR-7 | Claude m3 | GNR | P | Parity cross-reference retargeted to B8 |
| R9-GNR-8 | Claude m4 | GNR | C | Structural-consistency claim withdrawn; numerical bound retained |
| R9-GNR-9 | Claude m5 | GNR | P | "genuine dimension-4" defined once and reserved |
| R9-GNR-10 | Claude m6 | GNR | C | App. D Step 4 `γ⁻¹` restored |
| R9-GNR-11 | Claude m7 | GNR | P | "parity-odd **or** dark-energy channels" |
| R9-GNR-12 | Claude m8 | GNR | C | B11/B13/B4 independence argued explicitly |
| R9-GNR-13 | Claude m10 | GNR | P | Ref. [13] preprint status label |
| R9-GNR-14 | Claude m11 | GNR | P | Route-3 `10¹⁰` stress-test analogue stated |
| R9-SO-1 | Claude m9, Grok D1 | SCOPE-OPINION | P | Script rename deferred to archival deposit |
| R9-RF-1 | Grok E1, Gemini M1 | RE-FLAG + partial FAL | C | App. E already self-contained; recomputed clean this round |
| R9-RF-2 | Grok E2 | RE-FLAG + partial FAL | C | Endpoints reproduced from displayed inputs; real gap split to R9-GNR-3 |
| R9-RF-3 | Grok E3 | RE-FLAG + partial FAL | P | Abstract already carries the tier classification |
| R9-RF-4 | Grok M1 | RE-FLAG + partial FAL | P | Table II *is* the three-tier table |
| R9-RF-5 | Grok M2 | RE-FLAG | P | Per-arrow tier legend → D-round |
| R9-RF-6 | Grok M3 | RE-FLAG | P | Venue-length condensation (deferred-genuine) |
| R9-RF-7 | Grok G1 | RE-FLAG | P | Novelty count already scoped as non-rigor claim |
| R9-RF-8 | Grok J1 | RE-FLAG + FAL | C | Reconciled in two printed places |
| R9-RF-9 | Gemini E1 | RE-FLAG | P | Zenodo deposit = publishing phase (directive P) |
| R9-RF-10 | Gemini M2, m2 | RE-FLAG | P | Filenames must match repo; rename rides with R9-SO-1 |
| R9-RF-11 | Gemini m1 | RE-FLAG | P | Version stamp mandated by directive G until submission |
| R9-FAL-2 | Grok C1 | FALSIFIED | C | Double normalization stated; both lines verified consistent |
| R9-FAL-3 | Grok N2 | FALSIFIED | P | Substitution evaluates correctly as printed |
| R9-FAL-4 | Gemini N1 | FALSIFIED | P | Extraction artifact; PDF prints "gauge-invariant" |
| R9-OP-1 | Grok N1 | OPINION | P | Attribution-hygiene repetition retained |

**Genuinely-new-real by grade: 10 correctness-grade (R9-GNR-1, 2, 3, 4, 6, 8,
10, 12 + R9-ADJ-1, R9-ADJ-2) · 6 presentation-grade (R9-GNR-5, 7, 9, 11, 13,
14).** All 16 closed in v1C.0.12; the presentation-grade six were closed in
this round rather than deferred, because each was a one-line edit adjacent to
a correctness edit already being made.

## Deferred-genuine list (carried forward, updated)

1. Mint a separate Zenodo DOI for this survey's own verification scripts
   (R2-SO-2 → R9-RF-9). Publishing-phase per directive P.
2. Refereed-companion gate: the cited-only companion results (NJL gap
   equation, tensor-sector transparency extension, R4 spectator-ALP check)
   ride on the companion's own publication path (R9-RF-1).
3. Real mechanized enumeration establishing that the list **spans** the
   rule-admitted space (R3-GNR-1 → R9-GNR-1). *Narrowed this round*: the
   adjudication settled the rank and the relations, so what remains deferred
   is strictly the spanning claim, not independence.
4. Shapiro–Teixeira Eq. 58 verbatim-quote check.
5. Venue-length condensation to ≤ 12 pp (R9-RF-6).
6. **NEW —** rename `dim4_parityodd_enumeration.py` →
   `dim4_parityodd_identities.py` and de-tag the `research/theory_audit/`
   filenames and the `arxiv/` directory in the archival deposit, repinning all
   `\artifact{}` links in the same action (R9-SO-1, R9-RF-10). Cannot land
   in-round without invalidating the immutable pin.

## Closure evidence (v1C.0.12)

- Landed in `arxiv/paper1c_nogo_survey/main.tex` and
  `arxiv/paper1c_nogo_survey/references.bib`: all 16 genuinely-new-real items
  above, `\paperVersion` bumped to `v1C.0.12`, `\paperTimestamp` / `\date`
  at 2026-08-07. Every Sec. V / Table III / App. A 1 correction is cited to a
  specific `[L##]` tag of
  `research/theory_audit/operator_basis_adjudication_2026_08_07.json`; the
  adjudication script and report are added to the Data-and-Code statement via
  the repo's `\artifact{}` convention, and the immutable pin is advanced from
  `c80b7487b01f` to `1130b7c5e3d2` (verified: all six artifact files exist at
  that tree and are byte-identical to repository head). Nothing invented; the
  physics conclusion, every margin, every count, and every headline number are
  unchanged — the O4 correction *strengthens* the disposal without moving a
  number.
- Compile: `pdflatex` 4-pass (with `bibtex`), **0 errors / 0 undefined
  references / 0 overfull hboxes**, 22 pages.
- `/latex-audit` visual pass: pages 1, 9, 13, 15, 18 rendered at 110 DPI and
  inspected (title block with the new version stamp; the new Route-3
  Eq. (5); the new Sec. V relations block Eq. (11); the Data-and-Code block
  with six artifact paths; the full-width Table III). No column overflow, no
  gutter crossing, no overlap. All 6 `\artifact{}` paths resolve to existing
  files in the working tree; 0 raw `\texttt{}` path-overflow risks beyond the
  three pre-existing short in-prose script names; 0 `\date` overflow risk.
  Two overfull hboxes introduced mid-round were fixed before the final
  compile (Eq. (8)'s widened component forms were moved to following prose;
  the two longest artifact paths were set at `\scriptsize`).
- Mirrors byte-identical (md5 `0323f962935798b1159b8c5d02ce2571`, SHA-256
  `c21fde9f1b69e147ae6d27aeb27ec09189530a731331a4dc8a1e6c5d83d62982`):
  `arxiv/paper1c_nogo_survey/main.pdf` =
  `site/public/papers/paper1c_nogo_survey_v1C.0.12.pdf` =
  `public/papers/paper1c_nogo_survey_v1C.0.12.pdf`.
- Site: `site/src/data/papers.ts` (href + description),
  `site/src/data/reviewTimeline.ts` (R9 entry, newest-first),
  `project-context/draft_paper_registry.json` (`served_aliases`) updated;
  `cd site && npx next build` passes.

## Convergence read (directive H-refined + the R8 classification rule)

R9 surfaced **16 genuinely-new-real findings** (target: 0), of which **10 are
correctness-grade** and 6 presentation-grade. The literal 0-GNR gate is not
met and the correctness-convergence gate is not met, so the paper is **NOT
converged** and **the R-phase is NOT converged at R9**.

The composition is what matters, and it is worse than R8's on purpose:

- R8 closed with 2 correctness-grade GNR and named R9 "the correctness-
  convergence check". R9 returned **10**, including a **structural item** —
  R9-ADJ-2 — that had survived nine boards, three referee legs per board, and
  the paper's own released verification script. It was found only because
  Claude's MAJOR-1/MAJOR-2 were referred out to an independent symbolic
  computation instead of being adjudicated by re-reading the paper.
- That is the round's real lesson, and it is a process finding as much as a
  paper finding: **a claim about the paper's mathematics cannot be
  dispositioned from the paper's own prose.** The two referee claims that
  triggered the referral came back one REVIEWER-CORRECT-in-structure (with
  the literal coefficients wrong) and one REVIEWER-INCORRECT — and the
  computation run to settle them produced a third defect neither party saw.
- Calibration context, offered for reading the verdict words and never for
  softening a count: the Claude leg's ~20-item verification log independently
  re-derived every recomputable equation and all 25 bibliography entries with
  **zero** numeric or citation errors, and reported "no blocking presentation
  defects found"; Grok's REJECT rests entirely on the companion-dependency,
  abstract-recomputation, evidentiary-status, tier-table, and page-length
  families, every one of which is a re-flag of an R1–R8 disposition; Gemini's
  MAJOR REVISIONS rests on the Zenodo deposit and the companion gate, both
  publishing-phase per directive P. Of the three legs' 24 raw findings, the
  Claude leg supplied 15 of the 16 genuinely-new-real items and Grok and
  Gemini supplied one between them (the Ref.-[13] label came from Claude too;
  Gemini's sole new item, the typo, was an extraction artifact).

**Next gate: an R10 confirmation board on the exact v1C.0.12 PDF, and R10 is
the correctness-convergence check.** All active legs re-run fresh (Claude INT
Opus-tier + Grok API + Gemini API, per directive N/M-AMENDED; Perplexity
optional). The exit test is **zero correctness-grade genuinely-new-real
findings** — counting adjudication-originated items exactly as referee-
originated ones. A board that meets it converges the R-phase, with residual
presentation-grade items routed to the D-round. Any correctness-grade item,
from any source including a referred-out computation, forces a closure and a
further confirmation round.

Integrity unchanged and absolute: every finding on that board still gets a
source-cited disposition; every falsification still cites the render, the
printed text, or the computed tag that disproves it; no ACCEPT is ever faked;
no derivation is ever fabricated to close an item. But the count is the count,
and the gate is honest.
