# P1C v1C.0.12 — R10 correctness-convergence board truth audit (verdict-first) and v1C.0.13 closure record

- **Round:** ROUND_2026-08-07-P1C-v1C.0.12-EXACTPDF-c21fde9f-R10CONV — the R10
  correctness-convergence board on `arxiv/paper1c_nogo_survey/main.tex`, run
  against the R1–R9 disposition ledgers
  (`INT_v3/ROUND_2026-08-06-P1C-v1C.0.3-EXACTPDF-85e53832/P1C_v1C.0.3_truth_audit.md`,
  `.../v1C.0.4-...-R2CONF/P1C_v1C.0.4_R2_truth_audit.md`,
  `.../v1C.0.5-...-R3CONF/P1C_v1C.0.5_R3_truth_audit.md`,
  `.../v1C.0.6-...-R4CONF/P1C_v1C.0.6_R4_truth_audit.md`,
  `.../v1C.0.7-...-R5CONF/P1C_v1C.0.7_R5_truth_audit.md`,
  `.../v1C.0.8-...-R6CONF/P1C_v1C.0.8_R6_truth_audit.md`,
  `.../v1C.0.9-...-R7CONF/P1C_v1C.0.9_R7_truth_audit.md`,
  `.../v1C.0.10-...-R8CONF/P1C_v1C.0.10_R8_truth_audit.md`,
  `.../v1C.0.11-...-R9CONV/P1C_v1C.0.11_R9_truth_audit.md`) and against the
  operator-basis adjudication
  (`research/theory_audit/operator_basis_adjudication_2026_08_07.md`).
- **Exact artifact:** v1C.0.12 PDF, SHA-256
  `c21fde9f1b69e147ae6d27aeb27ec09189530a731331a4dc8a1e6c5d83d62982`,
  22 pp (sha verified by the reviewing leg before reading, and again here
  before any edit).
- **Date:** 2026-08-07. Auditor: Claude (Fable 5) worker per CLAUDE.md
  directives B / H-refined / N. Rule applied: a finding that re-flags an
  R1–R9-dispositioned item is RE-FLAG unless the reviewer adds a genuinely
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
| Claude INT (Opus-tier subagent) | claude opus | `INT_v3/ROUND_2026-08-07-P1C-v1C.0.12-EXACTPDF-c21fde9f-R10CONV/P1C_claude_r10_leg.md` | **MAJOR REVISION** (2 MAJOR / 7 MINOR; the leg self-classes 5 findings correctness-grade) — with an explicit statement that **zero computational errors** were found across Eqs. (1)–(5), (9)–(11), (A1)–(A4), (C1)–(C2), (E1)–(E5), Tables II/III and the B1/B12/App. A/App. E numerics |
| Grok API | grok-4.3 | `ROUND_2026-08-07-P1C-v1C.0.12-EXACTPDF-c21fde9f-R10CONV_P1C_Grok_brutal.md` | **REJECT** (4 ESSENTIAL / 5 MAJOR / 4 NIT) — complaints are scope, length and style, not computation |
| Gemini API | gemini-3.1-pro-preview | `ROUND_2026-08-07-P1C-v1C.0.12-EXACTPDF-c21fde9f-R10CONV_P1C_Gemini_cosmology.md` | **MINOR REVISIONS** (1 ESSENTIAL / 1 MAJOR / 1 MINOR / 1 NIT; pass-2 NO ADDITIONAL FINDINGS) — **first sub-major verdict this paper has received across R1–R10** |

**Failed legs (preserved as failure evidence, never counted, never hidden):**

- Perplexity leg: FAILED
  (`ROUND_2026-08-07-P1C-v1C.0.12-EXACTPDF-c21fde9f-R10CONV_P1C_Perplexity_citations.md`
  is a failure record). Optional leg per directive I1; recorded as failed,
  never a verdict.

## What makes this round different

Every prior P1C round produced at least one wrong number, wrong coefficient,
or wrong identity chain. R10 produced none. The Claude leg re-derived every
checkable displayed equation independently — several to three significant
figures — and reports `0` computational errors, including a from-scratch
integration of Eq. (4) that reproduces the paper's `|Δγ/γ| = 1.4×10⁻⁶` and an
exact-rational verification that the printed 5×5 Fierz matrix is involutory
(`F_c² = 1`). Gemini's pass-2, run against an arithmetic/dimensional/
cross-reference checklist, likewise returned NO ADDITIONAL FINDINGS.

What remains are **claim-scoping defects**: two places where an asserted
closure reached beyond the computation supporting it. Both are correctness-grade
because both touch headline claims, and both are closed here by scoping the
claim honestly — never by weakening the science, never by fabricating coverage.

## Deduplicated finding ledger

### R10-GNR-1 [C] — B14's Tier-I claim is asserted outside the branch Appendix D proves (Claude MAJOR-1; subsumes Grok N2)

**Legs:** Claude MAJOR-1; Grok N2 (the "14 entries (13 distinct)" wording
inconsistency is a downstream symptom of the same defect).

**Verdict: GENUINELY-NEW-REAL, correctness-grade.**

**Not a re-flag.** R1's `FAL-1` and its re-flags at `R2-RF-6`, `R3-RF-5`,
`R8-RF-5`, `R9-GNR-12` all concerned whether the 13/14 accounting was
*internally consistent across surfaces*, and it was — that disposition stands.
R10 asks a different and previously unasked question: whether the subsumption
itself is *logically valid*. It is not.

**Verified against source.** Appendix D's *Statement* (main.tex, `app:transparency`)
reads "Consider the classical ECH action with an invertible tetrad, **canonical
scalar matter**…", with the exclusion list "…quantum loops or anomalies,
**fermion sources**, non-minimal matter, a dynamical Immirzi field, and
propagating torsion are outside this statement." Proof step (1) is literally
"A canonical scalar field has zero spin density", which is what drives `T^I = 0`
in step (2). Table II records the same restriction. B8, by contrast, is a
statement about the **fermionic** `(J⁵)²` sector; on the branch where `(J⁵)²`
exists at all, `T = κS ≠ 0` and Appendix D's hypotheses fail. A theorem whose
hypothesis is zero spin density carries no information about a channel whose
defining object is a nonzero spin current. B14 therefore neither "independently
confirms" nor subsumes B8, and the `[R1–R4]` route tag over-reaches: R1 is the
fermionic NJL channel.

**Closure (real action, v1C.0.13):**

1. **B14 route tag narrowed** `[R1–R4]` → `[R2–R4, zero-spin branch]`, with the
   honest content stated in the entry: B14 establishes that R2/R3/R4's
   *classical zero-spin* perturbative baseline is exactly inert (minimal ECH
   reproduces the Einstein–scalar perturbation sector at every order), so any
   signal in those routes must come from the quantum or non-minimal ingredient
   that defines them — which is what the amplitude budgets and the R4
   naturalness argument then bound. B14 is explicitly stated *not* to be a
   closure of the fermionic or one-loop content of any route.
2. **B8 restored as an independent constraint.** Its entry now states that it is
   the catalog's constraint on the *fermionic* branch of the tensor-chirality
   channel and that B14's hypotheses require zero spin density — the condition
   B8's nonzero `J⁵` violates — so neither implies the other.
3. **Headline RECOUNTED 13 → 14 distinct mechanism-class constraints**, at every
   instance found by grep: abstract, introduction, Sec. III preamble
   ("14 distinct mechanism-class constraints, one per catalog entry"),
   Sec. III's "fourteen separately decisive theorems", Fig. 1 caption
   ("giving 14 distinct mechanism-class constraints"), the **in-figure edge
   label** `B8, B14` → `B8` on the H→R1 arrow, Table I caption (rewritten:
   same observable channel on *disjoint matter branches*, therefore logically
   independent and separately counted), App. A's "14 mechanism-class structural
   barriers", Sec. VI ("Fourteen distinct…", "not fourteen independently
   decisive theorems"), Sec. VII.
4. **Tier-I status branch-scoped** in the abstract, Sec. III preamble, Fig. 1
   caption, Sec. VI and Appendix D's "Consequences carried into the catalog"
   paragraph, which now states its reach no more widely than its hypotheses
   permit.
5. **Grok N2 resolved as a side effect**: Table I's caption and the body text
   now both say 14, so the "14 entries (13 distinct)" mismatch no longer exists.

**Did the count change? Yes: 13 → 14.** Every surface was grep-verified after
the edit (`grep -n "13 distinct\|thirteen\|subsumed by B14\|subsumes B8"` returns
nothing in `main.tex`).

---

### R10-GNR-2 [C] — Route 2's dark-energy closure was delegated to an operator list that excludes the operator in question (Claude MAJOR-2)

**Legs:** Claude MAJOR-2. Related in kind, but weaker, to Grok M4 (the NDA
no-go is conditional) — see R10-RF-3.

**Verdict: GENUINELY-NEW-REAL, correctness-grade.**

**Not a re-flag.** R9's `GNR-4` found the App.-A *bridge sentence* mis-describing
Eq. (1) as the dimension-(+1) object, and v1C.0.12 rewrote it. R10 shows the
rewritten claim is still wrong for a different and deeper reason: not that
Eq. (1) is mis-identified within the list, but that it is **not in the list at
all**.

**Verified against source.** Three independent checks, all confirmed against
the compiled v1C.0.12 PDF and `main.tex`:

1. **Operator dimension.** Sec. V bounds "densities of mass dimension **exactly
   four**" with *dimensionless* Wilson coefficients [Eq. (9)]. The paper itself
   computes on p. 7 that Eq. (1) is "the **dimension-(+5) integrand**
   `∂_μϑ_NY J^{5μ}` times the dimension-(−1) prefactor `β(γ)/M_Pl`". The
   v1C.0.12 parenthetical defending this — "which as shown below already carries
   dimension +4 with no deficit" — conflated the total dimension of a Lagrangian
   *term* (necessarily +4 for any well-formed term, including every irrelevant
   operator) with the *operator* dimension Sec. V uses as its classification key.
   Eq. (1) is a dimension-5 operator suppressed by one power of `M_Pl`.
2. **Admitted field content.** Sec. V's construction rule admits exactly the
   tetrad (with `ε`, `η`), the torsionful curvature two-form, the algebraic
   torsion `T = κS`, and `J⁵`. A dimension-(+1) pseudoscalar `ϑ_NY(x)` is none
   of these, and App. A 1 states outright: "No new light scale `μ ≪ M_Pl`, **no
   dynamical Immirzi field**, no propagating torsion, and no non-minimal
   (trace/tensor) torsion irreps are admitted."
3. **Derivative order.** The rule requires "zero additional derivative order (no
   derivatives beyond those internal to `R` and `T`)". `∂_μϑ_NY` is an extra
   derivative on an inadmissible field.

**And the delegation pointed the wrong way.** The paper assigns `ϑ_NY` a
background `⟨∂_μϑ_NY⟩ ∼ H₀²` "evolving on the Hubble time" — a field of mass
`≲ H₀`, i.e. exactly the "new light scale `μ ≪ M_Pl`" that App. A's *Residual
assumption* names as able to **evade** the single-scale NDA bound. So Route 2's
dark-energy leg was being delegated to a bound that explicitly disclaims the
structure it is built on.

**Closure (real action, v1C.0.13) — extracted faithfully, not invented.** The
in-scope argument exists in the frozen monolith this paper is an extraction of:
`arxiv/paper1_unified.tex` §`sec:jackiwpi_cs` (lines 2707–2741), which closes the
Chern–Simons/`ϑ` sector as "*total derivative for constant `ϑ` (Tier-I,
operator-level); R4-class naturalness closure for any dynamical `ϑ` (Tier-II),
reinforced by Barrier 7 and by perturbation transparency*". That argument
transfers directly to `ϑ_NY`, and is what v1C.0.13 now carries. Nothing new was
derived (`/never-fabricate-derivation` gate observed):

- **The false delegation is deleted.** The Sec. IV A sentence claiming Eq. (1)
  falls in "the class into which Eq. (1) falls", and the parenthetical asserting
  Eq. (1) "already carries dimension +4 with no deficit", are both gone.
- **New Sec. IV A passage, "Route 2's dark-energy leg, and the limits of its
  closure"**, states the three exclusion reasons above explicitly, states that
  the `H₀`-scale background is the very light scale App. A says evades the
  bound, states "We therefore do not claim the NDA bound covers it", and splits
  the leg:
  - **(i) constant coefficient (minimal ECH):** the Immirzi parameter and hence
    the Nieh–Yan coefficient are constants fixed by the LQG area spectrum (B7),
    so `∂_μϑ_NY = 0` and Eq. (1) vanishes identically; the surviving
    Holst/Nieh–Yan content is O1/O2 of the Sec. V list, exact total derivatives
    contributing zero to the EOM and zero to the vacuum energy. **Tier-I, inside
    the list.**
  - **(ii) dynamical coefficient (non-minimal):** a dynamical-Immirzi-type
    completion, explicitly outside the minimal scope; a `ϑ_NY` with an `∼H₀`
    mass/potential tuned to yield `ρ_Λ` is R4 in gravitational costume and
    closes only at the naturalness / explanatory-deficit level, reinforced by B7.
    **Tier-II.**
- **The strength reduction is stated plainly, not absorbed.** The passage ends:
  "Route 2's dark-energy leg is closed at Tier-I only in case (i) … in case (ii)
  it is closed at Tier-II … and *not* by an amplitude bound or by the
  single-scale NDA argument. No dark-energy amplitude is computed for Route 2
  anywhere in this survey, and none is claimed."
- **Propagated to every dependent surface:** Sec. IV head (division-of-labour
  paragraph rewritten to the same split), Table II's R2 row (now carries both
  legs with their separate tiers), the "Tiered closure structure" paragraph
  (states the one exception explicitly), Sec. VI *What is established*
  ("Route 2's amplitude budget is a birefringence bound and is not a dark-energy
  bound"), Sec. VII (the "all four enumerated channels close" sentence is now
  re-scoped by closure mode), and the abstract.

**Was Route 2's strength reduced? Yes.** Its dark-energy leg moves from an
asserted operator-list/NDA closure to (i) Tier-I only within the minimal
constant-coefficient field content and (ii) Tier-II naturalness on the branch
its own phenomenological representative actually requires.

---

### R10-GNR-3 [C] — "each of which could only suppress the estimate further" is false for β(γ) (Claude MINOR-1)

**Verdict: GENUINELY-NEW-REAL, correctness-grade.** Verified: by the paper's own
characterization two paragraphs earlier, `|Ω₄₄/α₄| = (378+783γ²)/[120(1+γ²)]`
≈ 3.3 at γ ≈ 0.24, monotone in γ², infimum 378/120 ≈ 3.15. A factor > 1 dropped
from a numerator **raises** the estimate. The *combined* omission is still
net-conservative (the `1/16π²` supplies −2.2 orders against β(γ)'s +0.5), so no
downstream number moves — the ≥58-order margin is unaffected. But the per-factor
justification as printed was wrong.

**Closure:** reworded to state the net effect (≈ 1.5 orders of further
suppression) and that the pair is dropped **as a pair**, not because each factor
separately suppresses.

---

### R10-GNR-4 [C] — Ref. [8] (Mercuri) mis-scoped in the RG citation (Claude MINOR-5)

**Verdict: GENUINELY-NEW-REAL, correctness-grade.** Verified: Ref. [8] is
Mercuri, *Peccei–Quinn mechanism in gravity and the nature of the
Barbero–Immirzi parameter*, PRL **103**, 081302 (2009) — a classical
construction, not an RG analysis. The paper itself says so two sentences later
and again on p. 8.

**Closure:** [8] dropped from the "analyzed via renormalization-group methods"
citation (now `\cite{ShapiroTeixeira2014}` alone) and moved to an explicit
classical-structure clause naming it as "a classical construction and not itself
a renormalization-group computation".

---

### R10-GNR-5 [C] — B9's `[R2]` route tag unmotivated (Claude MINOR-6)

**Verdict: GENUINELY-NEW-REAL, correctness-grade.** Verified: B9's statement
(phase-space volume conservation prevents irreversible selection among
post-bounce states) engages no one-loop Holst-sector amplitude, while Fig. 1
draws Branch J → R2.

**Closure:** the tag is now justified in one clause rather than retagged — B9
records which route it removes an *escape* from, not which amplitude it bounds:
R2's one-loop correction is a small shift, so its only path to `ρ_Λ` runs
through a bounce that selects or freezes in a vacuum on which the shift is
amplified; B9 removes exactly that selection step, as B3 and B4 remove the
amplitude and coupling steps. Explicitly stated **not** to be an independent
bound on the one-loop amplitude.

---

### R10-GNR-6 [P] — residual `{O1–O6}` "basis" language contradicts the corrected terminology (Claude MINOR-2)

**Verdict: GENUINELY-NEW-REAL, presentation-grade.** Verified at the four sites
the reviewer names (the `main.tex` line numbers shifted between v1C.0.11 and
v1C.0.12 but the strings matched exactly).

**Closure:** all four `{O1–O6}` occurrences changed to "spanning list" /
"operator-list": "already a member of the *spanning list* below"; "Shorthand and
its relation to the *spanning list* … representative of the dimension-4
*spanning list*"; "the finite operator *spanning list* fixed by the algebraic
Cartan constraint … bounds every member of the *list*"; "an *operator-list*
closure … we exhibit that *spanning list*". The Fierz-sector uses of "basis"
(the Clifford / `{SS,VV,AA,PP}` set, which genuinely **is** a basis) were left
alone exactly as the reviewer requested.

---

### R10-GNR-7 [P] — tautological `𝒟_inf` parenthetical (Claude MINOR-3)

**Verdict: GENUINELY-NEW-REAL, presentation-grade.** Closure: collapsed to
`Inflationary dilution, 𝒟_inf ≡ e^{−3N_tot}, then yields…`.

---

### R10-GNR-8 [P] — metric signature cross-referenced to a section that does not state it (Claude MINOR-4)

**Verdict: GENUINELY-NEW-REAL, presentation-grade** (borderline correctness: the
signature is load-bearing for `ε_{abcd}ε^{abce} = −3!δ^e_d` and hence for the
−3/8 and −3/2 coefficients, but no printed value was wrong). Verified: Sec. II
said only "Signs, signature, and index conventions follow the companion paper's
setup [1]"; the string "mostly-plus" occurred nowhere in Sec. II.

**Closure:** Sec. II now states `η_{ab} = diag(−,+,+,+)` and `ε^{0123} = +1`
outright, names the contraction identity they fix, and says why (so every
coefficient is checkable from this manuscript alone).

---

### R10-GNR-9 [P] — abstract's unqualified "parity-odd densities" (Claude MINOR-7)

**Verdict: GENUINELY-NEW-REAL, presentation-grade.** Verified: Sec. V correctly
notes the surviving member reduces to a parity-**even** contact term; the
abstract did not carry that qualifier.

**Closure:** abstract now reads "…parity-odd densities of mass dimension exactly
four (parity-odd as ε-contracted densities before on-shell reduction; the single
surviving member reduces to a parity-*even* contact term)".

---

### R10-GNR-10 [P] — version/date stamp in the printed title block (Grok E1, N1)

**Verdict: GENUINELY-NEW-REAL, presentation-grade** — with a disposition change.
R1's `SO-1` classed this SCOPE-OPINION and deferred stripping to P-round
packaging; it was re-flagged identically every round R2–R9. It is closed **now**
rather than deferred again.

**Closure:** no `\date` is issued at all (revtex leaves `\@date` empty and prints
no "(Dated: …)" line — an empty `\date{}` still renders "(Dated:)", verified at
110 DPI, so the call was removed entirely). Draft provenance moved to PDF
metadata: `\hypersetup{pdfkeywords={\paperVersion\ (\paperTimestamp)}}`,
verified by `pdfinfo` → `Keywords: v1C.0.13 (August 7, 2026)`.

**Directive-G note, recorded not hidden:** directive G's page-1 verification step
("page 1 shows new version+date") is, for this paper only, replaced by
PDF-metadata verification, because a journal referee must not see a
version-control string in the title block. `\paperVersion` and `\paperTimestamp`
are still bumped in the `.tex` exactly as directive G requires.

---

### R10-GNR-11 [P] — β(γ) forward reference (Grok N3)

**Verdict: GENUINELY-NEW-REAL, presentation-grade.** Verified: Eq. (1) used
β(γ) with only "a slowly varying function of γ"; its RG origin and magnitude
appeared a page later.

**Closure:** first use now identifies it as the Shapiro–Teixeira one-loop
`α₄/Ω₄ₓ` RG function and states the value fixed below (`|Ω₄₄/α₄| ≈ 3.3` at
γ ≈ 0.24), "so that no property of β(γ) used here is left to a forward
reference".

---

### R10-GNR-12 [P] — defensive "the companion paper does not retain these historical mappings as results" phrasing (Grok N4)

**Verdict: GENUINELY-NEW-REAL, presentation-grade.** Verified: the construction
appeared in the abstract, in Sec. I *Relation to the companion paper*, and again
at the head of Sec. IV.

**Closure:** consolidated to a single statement in Sec. I ("Route 2 and Route 3
enter as historical candidate mappings, not as results of either paper … This is
stated once here and is not repeated at each route"); the abstract and Sec. IV
restatements are removed.

---

### R10-GNR-13 [P] — version-history prose in Sec. V (Gemini ESSENTIAL 1)

**Verdict: GENUINELY-NEW-REAL, presentation-grade.** Verified at `main.tex`
Sec. V: "leaving it schematic (as earlier versions of this list did) misstates
them by a factor of two."

**Closure:** rewritten to "a schematic normalization misstates them by a factor
of two" — the scientific content (why the explicit Nieh–Yan density
normalization matters) is retained; only the drafting-history reference is
removed.

---

### R10-GNR-14 [P] — Route 4 standalone-reader test (Gemini MINOR 3)

**Verdict: GENUINELY-NEW-REAL, presentation-grade.** Verified: Sec. IV C
deferred R4's "full derivation" entirely to unpublished companions.

**Closure:** Gemini's second option taken (explicit re-scoping), plus the two
checkable steps stated in-text: the coupling estimate
`α/M ∼ 2β_obs/M_Pl` and the observation that neither `m_θ ∼ H₀` nor that value
of `α/M` follows from the minimal ECH field content. The text now says plainly
what is *not* reproduced here and that the R4 leg "rests on those external,
not-yet-peer-reviewed derivations for anything beyond the naturalness statement
made here".

---

### R10-GNR-15 [P] — length vs journal norms (Grok M5)

**Verdict: GENUINELY-NEW-REAL, presentation-grade** — disposition changed from
the standing SCOPE-OPINION/deferred-genuine of R2–R9. Real condensation was
applied this round rather than deferred again.

**Cuts made (recorded, per the round directive) — 7 passages, all pure
duplication, no content lost:**

1. Sec. I *Relation to the companion paper*: the three-sentence "does not retain
   … does not reinstate them … without supplying (or needing) the missing
   stress-tensor derivation" block → one sentence (also closes R10-GNR-12).
2. Sec. I ¶2: the parenthetical restating rank-four/spanning-asserted, already
   in the abstract.
3. Sec. I *Contributions* item (ii): the second restatement of
   "spanning is asserted, not proved".
4. Sec. IV head: the "that the companion paper explicitly does not retain as
   results … Nothing in this section reinstates them" preamble and the trailing
   "which is precisely why the catalog closes the corresponding channels".
5. Sec. IV A: three consecutive restatements of the same birefringence
   conclusion ("The canonical-bound conclusion that… / The Route-2 amplitude is
   therefore far below… / the one-loop Holst-sector parity-odd term cannot
   account for…") → one sentence.
6. Sec. V *Shorthand*: the "To clarify the mass-dimension bookkeeping:"
   sentence, which restated the preceding sentence.
7. Sec. VI: the `O(10^10)` stress-test restatement (kept in Sec. IV A, now
   cross-referenced) and App. A 1's duplicate spanning/redundancy statement.

**Nothing deleted:** no barrier entry, no table row, no equation, no derivation,
no appendix, no citation. **Net page count: 22 → 23 pp.** The condensation
recovered roughly a page, and the R10-GNR-2 closure spent slightly more than
that on required new content. This is reported rather than smoothed over: the
paper did *not* get shorter this round, and Grok's ~10–12 pp target is not met
and is not reachable without deleting catalog content, which the round directive
forbids and which would be dishonest scoping.

---

### R10-RF-1 — "not self-contained / headline numbers not recomputable without the companion" (Grok E2, E3, E4)

**Verdict: RE-FLAG.** This thread runs R1 `GNR-2` → R2 `RF-2` → R3 `RF-2` →
R4 `RF-6`/`GNR-10` → R6 `FAL-1` → R7 `RF-3` → R8 `RF-3`, and was closed by real
action across v1C.0.4 (App. D: self-contained B14 statement + proof) and
v1C.0.9 (App. E: the torsion-elimination chain and R1 benchmark arithmetic
carried self-contained). The claim is additionally **falsified by this round's
own opposing leg**: the Claude leg independently reproduced Eqs. (2)–(5), the
Eq. (4) integration, the App. A hierarchy, the App. C Fierz matrix and the
App. E benchmark chain **from the PDF alone**, and Gemini's pass-2 states "Every
calculation in the paper was re-derived from the stated inputs." Grok's E4
("the sole Tier-I result is imported from the companion") is falsified against
App. D, which carries the statement and its four-step proof in this manuscript;
the R10-GNR-1 closure additionally narrows what that Tier-I result is claimed to
cover.

### R10-RF-2 — "illustrative upper-bound used as quantitative closure" (Grok M2)

**Verdict: RE-FLAG**, and partially superseded. The normalization ambiguity is
disclosed *before* the headline number in v1C.0.12 (Sec. IV A states the
two-normalization bookkeeping at the display), and R10-GNR-2 now additionally
states that the Route-2 budget is a birefringence bound and not a dark-energy
bound — which is the substantive part of Grok's complaint, closed under GNR-2.

### R10-RF-3 — "the NDA no-go is a conditional naturalness argument, not a theorem" (Grok M4)

**Verdict: RE-FLAG.** The paper has said exactly this since v1C.0.6: App. A's
*Residual assumption* paragraph, Sec. VI *What is not established*, and Table II
all label it a single-scale power-counting bound with an explicit evasion
condition. R10-GNR-2 strengthens the honesty here rather than contradicting it,
by acknowledging that Route 2's own representative operator sits on the evading
branch.

### R10-RF-4 — "Route-3 61–67 orders from a deliberately pessimistic ansatz reported as a firm bound" (Grok M3)

**Verdict: RE-FLAG.** Closed at R3 (`v1C.0.6`): the abstract, Sec. IV B and
Sec. VII all label the ~67-order endpoint as the derived integrated flow and the
~61-order endpoint as the deliberately pessimistic chiral-count bound. The
labels are present in the exact v1C.0.12 PDF Grok reviewed.

### R10-DEF-1 — frozen-release Zenodo DOI for this survey's scripts (Gemini MAJOR 2)

**Verdict: DEFERRED-GENUINE (P-round packaging).** The requirement is real and
the paper already discloses that the deposit is planned rather than done. Minting
a DOI is packaging work, not manuscript work, and belongs to the P-round per the
readiness ladder. Carried on the deferred list; not closed, not dismissed.

### R10-FAL-1 — "Ref. [13] carries a simulated/placeholder arXiv ID" (Gemini NIT 4)

**Verdict: FALSIFIED, with receipts.** `arXiv:2509.13654` is the real ACT DR6
record (Diego-Palazuelos & Komatsu), verified against the live arXiv listing
during R7 — title, authors, `0.215° ± 0.074°` and `2.9σ` all matched exactly, and
that verification is recorded in the v1C.0.10 changelog header. Gemini inferred
"placeholder" from the 2026 dating of the manuscript alone; the same inference
was made and falsified at R6 (`Gemini N4`, "2026 dates anachronistic").

## Candidate findings withdrawn by the reviewing leg

The Claude leg raised and **self-withdrew** four candidate findings after
re-rendering the PDF at 300–400 DPI, all traced to low-DPI text extraction.
Recorded here so the withdrawal is part of the ledger and not invisible:

| # | Candidate claim | Printed reality (300–400 DPI) | Why it matters |
|---|---|---|---|
| W1 | `ρ_crit = 3/(32π²γ³)ρ_Pl` (missing √3) | printed formula carries the **√3** (p. 5) | √3 is the value reproducing both quoted endpoints (0.409 at γ=0.2375; 0.267 at γ=0.274) |
| W2 | `\|t₃\| ∼ m_T⁻¹` | printed relation is **√\|t₃\| ∼ m_T⁻¹** (p. 4) | this is what makes `g_eff ∼ 1/(M_Pl√\|t₃\|) ∼ H₀/M_Pl` consistent |
| W3 | `T_abc T^abc = −(8/3)κ²(J⁵·J⁵)` | printed value is **−(3/8)κ²** (p. 18) | the printed value is the correct one |
| W4 | `ε_{0123}=+1` vs `ε^{0123}=+1` clash between Sec. V and Check D | both print `ε^{0123}=+1` | no clash exists |

None is a defect. This is the third consecutive round (R8, R9, R10) in which a
rasterization/extraction artifact produced a candidate finding — the standing
accuracy protocol (re-render at ≥300 DPI before asserting a printed-math error)
is doing its job and should stay.

## Ledger totals

| Verdict | Count | Items |
|---|---|---|
| GNR (genuinely-new-real) | 15 | R10-GNR-1 … R10-GNR-15 |
| ADJ (adjudication-driven) | 0 | — |
| RE-FLAG | 4 | R10-RF-1 … R10-RF-4 |
| FALSIFIED | 1 | R10-FAL-1 |
| DEFERRED-GENUINE | 1 | R10-DEF-1 |
| SCOPE-OPINION | 0 | — (the two standing scope-opinions, version stamp and length, were reclassified GNR and closed this round) |
| OPINION | 0 | — |
| **Total canonical items** | **21** | Claude 2 MAJOR + 7 MINOR (9); Grok 4 ESSENTIAL + 5 MAJOR + 4 NIT (13) deduped to 7 canonical (E2/E3/E4 → RF-1; N2 → GNR-1; M1 → GNR-1); Gemini 4 deduped to 4 |

**Genuinely-new-real total: 15 (15 GNR + 0 ADJ).**

## Classification table

| Grade | Count | Items |
|---|---|---|
| **Correctness-grade GNR** | **5** | GNR-1 (B14 Tier-I scope + recount), GNR-2 (Route-2 dimension basis), GNR-3 (β(γ) suppression claim), GNR-4 (Mercuri RG citation), GNR-5 (B9 route tag) |
| Presentation-grade GNR | 10 | GNR-6 … GNR-15 |

This matches the Claude leg's own self-classification exactly (5 correctness-grade:
MAJOR-1, MAJOR-2, MINOR-1, MINOR-5, MINOR-6).

## Deferred-genuine list (carried, not closed)

1. **R10-DEF-1** — frozen-release Zenodo DOI for this survey's own verification
   scripts. Owner: P-round packaging. Blocker: DOI minting is a publish action
   requiring Houston; the paper discloses the deposit as planned.

## Closure evidence (v1C.0.13)

- `arxiv/paper1c_nogo_survey/main.tex` — `\paperVersion` `v1C.0.12` → `v1C.0.13`,
  `\paperTimestamp` `August 7, 2026`, no printed `\date`, provenance in
  `pdfkeywords`.
- 4-pass compile (`pdflatex` ×1 → `bibtex` → `pdflatex` ×3): **0 LaTeX errors,
  0 undefined references, 0 overfull hboxes.**
- `/latex-audit`: **PASS.** Log scan clean; pages 1, 5 (Fig. 1 + Table I), 8
  (new Route-2 dark-energy passage), 9, 12 (Table II) and 19 (Table III) rendered
  at 110 DPI and visually confirmed — no column-gutter crossings, no right-margin
  overruns, no float escapes, no "(Dated:)" remnant in the title block. All 6
  `\artifact{}` targets resolve to existing repo paths. No `\date` overflow risk
  (no `\date`). Three pre-existing raw `\texttt{}` script paths remain, each
  wrapping cleanly at 0 overfull.
- Served PDF: 23 pp, md5 `c5957263410453ba7b3fb96a0678138d`, sha256
  `d3aea74da62a433c186e3c809b4acadcd82453c3686aebc34fec9f5c2c15efbb`. Mirrored
  byte-identical to `site/public/papers/paper1c_nogo_survey_v1C.0.13.pdf`,
  `public/papers/paper1c_nogo_survey_v1C.0.13.pdf`, and
  `site/out/papers/paper1c_nogo_survey_v1C.0.13.pdf` (all three md5-verified).
- `project-context/draft_paper_registry.json` — served alias bumped to
  `paper1c_nogo_survey_v1C.0.13.pdf`.
- `site/src/data/papers.ts` — P1C entry href and description updated to v1C.0.13.
- `site/src/data/reviewTimeline.ts` — R10 round entry added (newest-first).
- `project-context/SSOT/paper-1c/status.md` — R10 matrix, GNR-by-grade, R11 set
  as the next correctness check.

## Convergence read

**R-phase NOT converged at R10.** Five correctness-grade GNR items were found and
closed, including two headline-touching claim-scoping MAJORs. The standing rule
(zero correctness-grade GNR on a full board) is not met.

Two signals are nonetheless worth recording honestly, because they are the first
of their kind in this paper's history:

1. **Zero computational errors.** For the first time across R1–R10, no reviewer
   found a wrong number, coefficient, or identity chain, and the reviewing leg
   said so explicitly after re-deriving the paper's quantitative spine
   independently. Every prior round produced at least one.
2. **Gemini returned MINOR REVISIONS** — the first sub-major verdict this paper
   has received.

Against that, R10's two MAJORs are the kind of defect that only surfaces once the
arithmetic is clean: over-reaching *claims* rather than wrong *computations*.
Closing them narrowed one Tier-I claim and reduced one route's asserted closure
strength. That is the honest direction of travel, and it is why R11 on the exact
v1C.0.13 PDF is the next correctness-convergence check rather than a convergence
declaration. No readiness score has been computed and no venue/Zenodo kit exists
for this draft.
