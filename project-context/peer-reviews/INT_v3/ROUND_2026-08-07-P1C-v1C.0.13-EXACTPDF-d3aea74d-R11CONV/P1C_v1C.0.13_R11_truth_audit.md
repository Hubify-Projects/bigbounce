# P1C v1C.0.13 — R11 correctness-convergence board truth audit (verdict-first) and v1C.0.14 closure record

- **Round:** ROUND_2026-08-07-P1C-v1C.0.13-EXACTPDF-d3aea74d-R11CONV — the R11
  correctness-convergence board on `arxiv/paper1c_nogo_survey/main.tex`, run
  against the R1–R10 disposition ledgers
  (`INT_v3/ROUND_2026-08-06-P1C-v1C.0.3-EXACTPDF-85e53832/P1C_v1C.0.3_truth_audit.md`,
  `.../v1C.0.4-...-R2CONF/P1C_v1C.0.4_R2_truth_audit.md`,
  `.../v1C.0.5-...-R3CONF/P1C_v1C.0.5_R3_truth_audit.md`,
  `.../v1C.0.6-...-R4CONF/P1C_v1C.0.6_R4_truth_audit.md`,
  `.../v1C.0.7-...-R5CONF/P1C_v1C.0.7_R5_truth_audit.md`,
  `.../v1C.0.8-...-R6CONF/P1C_v1C.0.8_R6_truth_audit.md`,
  `.../v1C.0.9-...-R7CONF/P1C_v1C.0.9_R7_truth_audit.md`,
  `.../v1C.0.10-...-R8CONF/P1C_v1C.0.10_R8_truth_audit.md`,
  `.../v1C.0.11-...-R9CONV/P1C_v1C.0.11_R9_truth_audit.md`,
  `.../v1C.0.12-...-R10CONV/P1C_v1C.0.12_R10_truth_audit.md`) and against the
  released theory-audit artifacts (`research/theory_audit/*.md`, `*.json`).
- **Exact artifact:** v1C.0.13 PDF, SHA-256
  `d3aea74da62a433c186e3c809b4acadcd82453c3686aebc34fec9f5c2c15efbb`,
  23 pp (sha verified by the reviewing leg before reading, and again here
  before any edit).
- **Date:** 2026-08-07. Auditor: Claude (Fable 5) worker per CLAUDE.md
  directives B / H-refined / N. Rule applied: a finding that re-flags an
  R1–R10-dispositioned item is RE-FLAG unless the reviewer adds a genuinely
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
| Claude INT (Opus-tier subagent) | claude opus | `INT_v3/ROUND_2026-08-07-P1C-v1C.0.13-EXACTPDF-d3aea74d-R11CONV/P1C_claude_r11_leg.md` | **MAJOR REVISION** (4 MAJOR / 6 MINOR; the leg self-classes 6 findings correctness-grade) — with an explicit **zero computational errors** statement backed by a 30-item correctness ledger: the Fierz involution (all 25 entries), the Benedetti–Speziale flow integration, the O4/O5 tensor reductions, and every App. A / App. E order-of-magnitude figure reproduced independently. One discrepancy found, a rounding slip in a parenthetical |
| Grok API | grok-4.3 | `ROUND_2026-08-07-P1C-v1C.0.13-EXACTPDF-d3aea74d-R11CONV_P1C_Grok_brutal.md` | **REJECT** (4 ESSENTIAL / 3 MAJOR / 2 NIT) — complaints are scope, self-containment and length, not computation |
| Gemini API | gemini-3.1-pro-preview | `ROUND_2026-08-07-P1C-v1C.0.13-EXACTPDF-d3aea74d-R11CONV_P1C_Gemini_cosmology.md` | **MAJOR REVISIONS** (1 ESSENTIAL / 3 MAJOR / 2 MINOR / 1 NIT; pass-2 NO ADDITIONAL FINDINGS) — a regression from R10's MINOR REVISIONS, driven mostly by a text-extraction artifact (see R11-FAL-1) |

**Failed legs (preserved as failure evidence, never counted, never hidden):**

- Perplexity leg: FAILED
  (`ROUND_2026-08-07-P1C-v1C.0.13-EXACTPDF-d3aea74d-R11CONV_P1C_Perplexity_citations.md`
  is a failure record). Optional leg per directive I1; recorded as failed,
  never a verdict.

## What makes this round different

R10 was the first round in this paper's history with zero computational
errors. R11 is the second — and this time the reviewing leg quantified it:
**30 checkable displayed relations and numerical claims recomputed
independently, one discrepancy, and that one a rounding slip in a
parenthetical.** The physics of this survey is, so far as it can be checked
from the PDF alone, sound.

What R11 found instead is a new defect *class*, and it is the reason this
round produced a durable tooling change rather than only manuscript edits:
**all four MAJORs are internal-consistency defects created by iterative
editing.** In each case the paper's body is more careful than its summary
surfaces, and in each case the defect is a disagreement between two places in
the same document (or between the document and one of its own released
artifacts) rather than an error in reasoning:

- Table II says two Tier-(I); six text sites say exactly one.
- Sec. IV B asserts an NDA bound that pp. 6 and 8 explicitly disclaim.
- The abstract's universal quantifier is falsified by two of the catalog's
  own entries.
- App. C claims uniqueness for exactly the case its cited artifact declares
  non-unique.

Three of these are the *residue of the previous round's closure*. R10's
MAJOR-2 closure correctly re-homed Route 2's dark-energy leg on the operator
list, but in doing so promoted it to a tier the list cannot carry, did not
propagate the change to the six "exactly one Tier-I" surfaces, and left one
un-swept sentence still delegating the operator to the NDA bound the same
revision had just concluded does not cover it. A grep-based sweep by a human
or an agent found three of four sites; the fourth survived.

That is a mechanically detectable failure mode, and R11's durable output is
`tools/p1c_consistency_check.py` — a linter that fails loudly on exactly these
four classes. Run against the pristine v1C.0.13 source it exits 1 and fires
Rules B, C and D, independently rediscovering MAJOR-1, MAJOR-2 and MAJOR-3
with no reviewer in the loop. It is recorded here as the anti-regression
guard, and it is what makes "the R10 sweep missed a site" a bug that cannot
recur silently.

## Deduplicated finding ledger

### R11-GNR-1 [C] — Table II carries two Tier-(I) legs while six text sites assert exactly one, and the second (I) does not meet the paper's own Tier-I definition (Claude MAJOR-1)

**Legs:** Claude MAJOR-1.

**Verdict: GENUINELY-NEW-REAL, correctness-grade.**

**Not a re-flag.** The long Tier-classification re-flag chain (R1 `RF-2` →
R2-RF-5 → R3-RF-4 → R4-RF-5/RF-6 → R5-RF-1/RF-8 → R6-RF-2/RF-6/RF-7 →
R7-RF-4 → R8-RF-4/RF-6/RF-7/RF-9 → R9-RF-3/RF-4 → R10-RF-2/RF-3) concerned
whether the *stated* tiers were honest labels for the arguments behind them,
and they were — that disposition stands. R11 asks a different question:
whether the table and the text now *count* the same number of Tier-I legs.
They do not, and the discrepancy was introduced by the v1C.0.13 closure of
R10-GNR-2.

**Verified against source.** Two independent problems, both confirmed against
the exact v1C.0.13 PDF at 300 DPI and against `main.tex`:

1. **Count mismatch.** Table II's R2 row, *Evidentiary status* column,
   printed `\textbf{(I)} for constant Nieh--Yan coefficient (O1/O2 total
   derivatives, B7 fixes $\gamma$)` — a second bold **(I)**, alongside the
   perturbation-transparency row. Six sites say otherwise, verbatim: abstract
   ("only the perturbation-transparency result is a Tier-I rigorous
   theorem"); Sec. III preamble ("which is why the abstract credits **exactly
   one** Tier-I rigorous theorem"); the B14 entry ("the catalog's **sole**
   Tier-I closure leg"); Sec. IV C ("**the only** Tier-I (rigorous) leg");
   Sec. VI ("**Only** the perturbation-transparency theorem … enters the
   closure table as a Tier-I rigorous result"); App. D preamble ("the
   catalog's **sole** Tier-I leg"). Table II's own caption compounds it:
   "The table records the highest level at which each leg is claimed; no leg
   is asserted more strongly elsewhere" — the inverse of the actual
   situation, where the *table* asserted more strongly than the text.
2. **The grade itself over-reaches.** Sec. IV C defines Tier-I as "a
   deductive consequence of stated equations/identities". The claim "minimal
   Route 2 sources no dark energy" is not a statement about O1 and O2; it is
   the statement that O1/O2 *exhaust* the surviving rule-admitted
   Holst/Nieh–Yan content. That step is the spanning assertion, which the
   manuscript disclaims in six places — abstract ("That the list *spans* the
   rule-admitted operator space is asserted from the construction rules, not
   proved by exhaustive symbolic enumeration"), Sec. V, App. A 1, Sec. VI,
   and the Data & Code statement ("None of the scripts performs the
   enumeration establishing that the list spans the rule-admitted space"). A
   conclusion resting on an explicitly unproved premise cannot be Tier-I
   under this paper's own scale.

**Closure (real action, v1C.0.14) — option (a) of the reviewer's two, which is
also the option consistent with everything else in the paper:**

1. **Table II's R2 dark-energy leg REGRADED (I) → (II)**, in both branches.
   The cell now names the genuinely Tier-I ingredient as such and states the
   inherited assumption plainly: "Constant Nieh–Yan coefficient (B7 fixes γ):
   O1/O2 are exact total derivatives, a Tier-I fact about the list, but the
   step to 'R2 sources no dark energy' inherits the unproved spanning
   assertion (Sec. IV A). Dynamical ϑ_NY, outside the minimal scope: R4-class
   naturalness. No dark-energy amplitude is computed for R2."
2. **Sec. IV A rewritten at both sites.** "Minimal Route 2 therefore sources
   no dark energy, and this *is* an operator-level (Tier-I) statement about
   the list" → the operator-level input is rigorous (Tier-I) about the list,
   the conclusion needs one step more (that O1/O2 exhaust the rule-admitted
   content), that step is the spanning assertion the survey does not prove,
   so the leg is recorded at Tier-II — followed by the explicit sentence
   "The catalog's only Tier-I leg remains the perturbation-transparency
   theorem of Appendix D." And "Route 2's dark-energy leg is closed at Tier-I
   only in case (i)" → "closed at Tier-II in both cases", with the Tier-I
   ingredient named and the inheritance stated.
3. **The six count statements and the Table II caption are left as written
   and are now true.** Verified mechanically: the `tab:evidentiary_status`
   table body contains exactly one `\textbf{(I)}` marker, and the linter's
   Rule B reports 1 table marker against nine prose sites all implying 1.

**Was any strength claimed that is not now claimed? Yes, and deliberately:**
Route 2's dark-energy leg moves from Tier-I-in-case-(i) to Tier-II in both
branches. The underlying physics is unchanged — O1 and O2 are still exact
total derivatives, and that fact is still stated as rigorous. What changed is
that the *conclusion* drawn from it no longer claims a tier its premise
cannot carry.

---

### R11-GNR-2 [C] — a fourth site still delegates Eq. (1) to the single-scale NDA bound the same revision explicitly disclaims (Claude MAJOR-2)

**Legs:** Claude MAJOR-2.

**Verdict: GENUINELY-NEW-REAL, correctness-grade.**

**Not a re-flag, and specifically not a re-flag of R10-RF-3.** R10-RF-3
dispositioned Grok's "the NDA no-go is a conditional naturalness argument,
not a theorem" as a re-flag, because the paper has labelled it exactly that
since v1C.0.6 — that disposition stands. R11's finding is the opposite
direction: not that the NDA bound is over-described, but that a surviving
sentence *applies* it to an operator the same revision concluded it does not
cover. This is a closure-insufficiency item in the R10-GNR-2 lineage, and it
is the reason the guard exists.

**Verified against source.** Sec. IV B, *Ansatz vs derivation (R2/R3)*, p.10
left column (300 DPI verified): "…only the single absolute normalization
remains a bounded EFT input … **and the operator is bounded by the
single-scale NDA no-go regardless of that O(1) normalization.**" "The
operator" is Eq. (1), the R2 one-loop parity-odd operator. Contradicted three
times in the same PDF:

- p.8, Sec. IV A: "…precisely the case App. A names as able to *evade* the
  single-scale NDA bound. **We therefore do not claim the NDA bound covers
  it**".
- p.8, Sec. IV A: "…in case (ii) it is closed at Tier-II … **not by an
  amplitude bound or by the single-scale NDA argument**."
- p.6, Sec. IV head: "…its dark-energy leg is **not** closed by the
  single-scale NDA bound, which App. A states explicitly can be evaded by
  exactly such a light scale."

The v1C.0.13 revision note states of this exact defect "The false delegation
is removed." It was removed at three sites and survived at a fourth — and the
survivor sits in the summary paragraph a reader consults for Route 2's
headline status, and is the *stronger* of the two claims.

**Closure (real action, v1C.0.14):**

1. **The clause is replaced with the accurate statement:** "…and the
   *birefringence* amplitude is bounded by the explicit budget of Eq. (2)
   regardless of that O(1) normalization. (The single-scale NDA bound is
   *not* claimed to cover Eq. (1), whose H₀-scale pseudoscalar background is
   exactly the light scale App. A names as able to evade it; see Sec. IV A.)"
2. **Manuscript re-grepped for every remaining "NDA" instance** (18 hits
   outside the changelog header). One sibling found and fixed: the *Strict
   theoretical limitation* paragraph called Eq. (1) "the NDA one-loop operator
   (R2)" → "the one-loop parity-odd operator (R2)". Every other instance was
   checked individually and attaches the bound to the O1–O6 list, the
   dimension-(+1) shorthand, or App. A's ceiling — never to Eq. (1).
3. **Encoded as a permanent guard.** Linter Rule C now carries the
   `nda_covers_eq1` and `nda_operator_label` assert/disclaim pairs; a future
   edit that reintroduces either phrase while the disclaim sentence stands
   fails the check.

---

### R11-GNR-3 [C] — the abstract's universal "each closing one or more of the four routes" is falsified by B14's and B9's own entries (Claude MAJOR-3)

**Legs:** Claude MAJOR-3.

**Verdict: GENUINELY-NEW-REAL, correctness-grade.**

**Not a re-flag, and note the lineage carefully.** This exact phrase was
*introduced* as the closure of R4-GNR-10 (v1C.0.7), which replaced "each
closing a specific route" with "each closing one or more of the four routes"
to accommodate B14 then spanning all four routes. That closure was correct
for the catalog as it stood at v1C.0.7. It was invalidated by R10-GNR-1
(v1C.0.13), which narrowed B14's tag to [R2–R4, zero-spin branch] and stated
explicitly that B14 closes none of them — and the abstract was not
re-examined. R11 is the first round to check the quantifier against the
post-R10 catalog.

**Verified against source.** The abstract (p.1, 300 DPI verified) reads
"…fourteen distinct mechanism-class constraints … **each closing one or more
of the four routes** by which the ECH bounce could plausibly source a Λ-like
late-time density." Falsified by two entries:

- **B14**, p.6: "**B14 is not, and is not used as, a closure of the fermionic
  or one-loop content of any route.**" Its stated content for R2–R4 is that
  their *classical zero-spin* baseline is inert — which, since all three
  routes are *defined* by quantum or non-minimal content, closes none of them.
- **B9**, p.4: "It is **not** an independent bound on the one-loop
  amplitude… so B9 is **never used as a stand-alone closure**."

So at least two of the fourteen close no route, by the manuscript's own
careful statements. The abstract is the one place in the paper where that
carefulness lapsed, and it lapsed toward overclaiming.

**Closure (real action, v1C.0.14).** The clause is rescoped to the joint claim
the catalog actually supports, with the two exceptions named rather than
papered over: "…spanning seven foundational mechanism classes and six
observational-channel branches, which *jointly* close the four routes by
which the ECH bounce could plausibly source a Λ-like late-time density. The
entries bear on the routes with differing individual force, and two of them
(B9, B14) are explicitly *not* used as stand-alone closures of any route; the
closure claimed here is that of the catalog taken together, at
channel-amplitude granularity." The fourteen-count itself is untouched and
well defended; only the per-entry closure claim was not.

A sibling was caught in the same sweep and fixed: Sec. I's "show that each is
closed by an explicit, **individually labeled** argument" now reads "by an
explicit, labeled argument, in some cases by more than one catalog entry
acting together", so the introduction does not reintroduce a one-entry-per-
class implication the catalog does not honour.

**Encoded as a permanent guard.** Linter Rule D pairs universal per-entry
closure phrases against entries that declare themselves non-closures, and
names the offending entries.

---

### R11-GNR-4 [C] — App. C asserts Grassmann uniqueness for exactly the case its cited artifact declares non-unique (Claude MAJOR-4)

**Legs:** Claude MAJOR-4.

**Verdict: GENUINELY-NEW-REAL, correctness-grade.**

**Not a re-flag.** App. C's Fierz content has been stable since R1-GNR-1 and
was twice defended against reviewer misreads (R3-FAL-2, R5-RF-7), both traced
to the stacked-½ rasterization artifact. Those dispositions stand: the printed
matrix is correct and involutory. R11's finding is not about the matrix. It is
about a single qualifier in the prose describing what the released artifact
proved.

**Verified against the artifact, in both the report and the machine output.**
App. C (p.20, 400 DPI crop verified) read: "…an exact Grassmann-algebra
derivation of the operator row (**the unique solution for identical
fields**)". The cited artifact says the opposite:

- `research/theory_audit/fierz_adjudication_2026_08_05.md`, *Caveat* (lines
  79–82): "For a single species the five quartics obey two exact linear
  relations (rank 3) [L10], so *identical-field* rearrangement rows are **not
  unique** … The canonical **distinct-field** operator row, **which is
  unique**, is P1A's row."
- Same file, result line (27–29): uniqueness is attached to "four distinct
  fields (unique solution)".
- Machine output `fierz_adjudication_2026_08_05.json` confirms both halves
  independently of the prose report: `log_lines[6]` — "[L07] Grassmann engine
  (4 distinct anticommuting fields, exact): operator Fierz matrix solved;
  F_op == -F_c (single Grassmann exchange): True"; `log_lines[9]` — "[L10]
  Identical single-species field: span rank of {O_S,O_V,O_T,O_A,O_P} = 3;
  relation module dimension = 2; relations (coeffs on (S,V,T,A,P)):
  [['-4','-1','-2/3','1','0'], ['1','0','1/3','0','1']]".

The manuscript had transposed the qualifier: the artifact proves uniqueness
for *distinct* fields and explicitly denies it for *identical* fields; the
paper claimed it for *identical* fields. The artifact does separately confirm
(`log_lines[10]`, [L11]) that the row is a valid identical-field Grassmann
identity — so **the row is right and nothing downstream moves**:
G_s = −3κ/16 stands, and the bridge 4πG = κ/2, −(3/2)πG = −3κ/16 was
independently re-verified by the reviewing leg. But the word "unique" was
doing rhetorical work — offered as evidence that the coefficient set is
*forced* rather than convention-selected, immediately after a convention note
conceding that individual Fierz coefficients are convention-dependent.

**Closure (real action, v1C.0.14).** Corrected to the artifact's actual
result, with the rank-3 caveat carried rather than dropped: "…an exact
Grassmann-algebra derivation of the operator row: the *unique* solution on
four *distinct* anticommuting fields, and an exact identical-field Grassmann
identity. Uniqueness is a statement about the distinct-field construction only
— for a single species the five quartics obey two exact linear relations
(span rank three), so identical-field rearrangement rows are *not* unique, and
it is the declared direct-channel convention that fixes the mean-field G_s."

This is the reviewer's recommended fix and, as the leg notes, a cleaner
statement than the one it replaces. No coefficient, no number, and no
downstream conclusion changes.

---

### R11-GNR-5 [C] — "roughly 1.5 orders" is arithmetically inconsistent with the two components stated in the same sentence (Claude MINOR-1)

**Verdict: GENUINELY-NEW-REAL, correctness-grade.**

**Lineage.** The sentence was written as the closure of R10-GNR-3, which
correctly replaced a false per-factor justification ("each of which could only
suppress the estimate further") with a net-effect statement. The net effect
was mis-added.

**Verified independently.** p.7 right column (300 DPI): "…their *net* effect
being a further suppression of **roughly 1.5 orders** — the loop factor
supplies **−2.2 orders** against β(γ) ≈ 3.3's **+0.5**". Recomputed here:
log₁₀(1/16π²) = −2.1982, log₁₀(3.3) = +0.5185, sum = **−1.6797**. The two
stated components are both correct; only the sum is wrong. The sentence exists
specifically to show the arithmetic, so the arithmetic has to close.

**Closure:** "roughly 1.5 orders" → "roughly 1.7 orders". Verified in the
recompiled v1C.0.14 PDF (p.8, `pdftotext` confirms "roughly 1.7"). The
conservative direction is unaffected, no margin changes, and no downstream
number moves.

---

### R11-GNR-6 [C] — App. D's load-bearing kernel lemma is asserted rather than proved or cited (Claude MINOR-2)

**Verdict: GENUINELY-NEW-REAL, correctness-grade.** Graded correctness rather
than presentation because App. D exists specifically so that the catalog's
sole Tier-I leg "can be refereed from this manuscript" (its own preamble), and
a referee could not verify step (2) from this manuscript alone.

**Verified against source.** p.21, Proof step (2): "the zero scalar source
therefore gives e^[I ∧ T^J] = 0, **whose invertible-tetrad kernel is trivial:
T^I = 0.**" The statement is true and standard, but it was asserted with no
argument and no citation, inside the load-bearing step of the paper's only
Tier-I result.

**Independently verified before closing** (`/never-fabricate-derivation`
gate observed — the closure states a standard result and cites it, it does not
invent a derivation). The linear map T^J_{LM} ↦ δ^{[I}_{[K}T^{J]}_{LM]} on the
24-dimensional torsion space (T^J_{LM} = −T^J_{ML}, 4 × 6 = 24) was built
explicitly and its rank computed: **rank 24, kernel trivial.** The lemma
holds; the manuscript's assertion was correct, only unsupported.

**Closure:** step (2) now states the condition in frame components and cites
the standard Einstein–Cartan result rather than asserting it bare: "In frame
components this reads δ^[I_[K T^J]_LM] = 0, and for invertible tetrad the
linear map it defines on the 24 independent components T^J_LM has trivial
kernel, so T^I = 0. This is the standard algebraic-torsion property of
Einstein–Cartan theory [Hehl, von der Heyde, Kerlick & Nester, Rev. Mod. Phys.
**48**, 393 (1976)]: torsion is not an independent propagating field but is
fixed algebraically by — and vanishes with — the spin source." One new
`references.bib` entry (`Hehl1976`); the bibliography goes 25 → 26 entries and
`\cite`/`\bibitem`/`.bib` remain in exact three-way agreement.

---

### R11-GNR-7 [P] — App. D defers a "tensor-sector extension" its own Statement already claims (Claude MINOR-3)

**Verdict: GENUINELY-NEW-REAL, presentation-grade.** Verified: App. D's
*Statement* asserts "scalar equations and **tensor evolution operators**
coincide with those of general relativity at every perturbative order", while
its preamble said "The **tensor-sector extension**, the explicit second-order
Holst-term verification, and the discussion of what would break the
transparency are given in full in the companion." The reviewer's dichotomy is
the right one: either the tensor conclusion is an immediate corollary (and
nothing is deferred) or the Tier-I claim exceeds what App. D proves.

**Closure:** the first horn, stated explicitly. The preamble now reads: "Both
halves of the Statement are established here: because Steps 1–4 reduce the
action *exactly* to the Einstein–scalar action, the tensor conclusion is an
immediate corollary of the scalar one and nothing about it is deferred. What
the companion carries in addition, and what this survey does not need, is the
explicit order-by-order second-order Holst-term verification and the
discussion of what would break the transparency." The B14 catalog entry was
brought into line in the same edit ("carried self-contained in Appendix D,
scalar and tensor sectors alike").

---

### R11-GNR-8 [P] — branch→entry multiplicity never stated; the 7 + 6 → 14 arithmetic closes only implicitly (Claude MINOR-4)

**Verdict: GENUINELY-NEW-REAL, presentation-grade.** Verified: Sec. III said
"We tested 7 foundation mechanism classes … and 6 additional observational
channels" and "Each test yielded a named structural constraint" — which reads
as 13 tests → 13 constraints. The bookkeeping is in fact consistent, but the
reader has to reconstruct it from Table I and the Fig. 1 caption. Given that
"fourteen" is a headline number carried in the abstract, introduction, Fig. 1
caption, Table I caption, Sec. VI and Sec. VII, it should be arithmetically
legible in one place.

**Closure:** one explicit sentence added after the 7 + 6 statement: "the seven
foundations carry one entry each (B1–B7); Branch H carries two (B8, B14);
Branch J carries one (B9); Branches L/M carry three between them (B10–B12);
and Branches N/O carry one between them (B13). That is 7 + 2 + 1 + 3 + 1 = 14
entries across 7 + 6 = 13 tested classes and channels — the two grouped branch
pairs (L/M and N/O) are treated as single observational channels, and neither
N nor O carries a dedicated constraint of its own." Cross-checked against
Table I's Source column (B10 → Branch L, B11 → Branch L/M, B12 → Branch M,
B13 → Branch N/O) and against Fig. 1's grouping boxes; the two agree.

---

### R11-GNR-9 [P] — eight labels defined but never referenced; App. E's displays numbered but orphaned (Claude MINOR-5)

**Verdict: GENUINELY-NEW-REAL, presentation-grade.** Verified all eight:
`sec:barrier_details`, `app:contact_coeff`, `app:r1_benchmark`,
`eq:Seff_dim4`, `eq:holst_cartan_inverse_p1c`, `eq:fmt_contorsion_p1c`,
`eq:fmt_bridge_p1c`, `eq:r1_benchmark_p1c`. The last four are *all* of App. E's
numbered displays — the entire self-contained companion-input appendix
consisted of equations carrying numbers that nothing pointed at.

**Closure:** cross-referenced rather than unnumbered, since the content is
used. App. E's preamble now points at both of its subsections and all four
displays ("carried in App. E 1 as Eqs. (E1), (E2) and (E3) … carried in
App. E 2 as Eq. (E5)"); Table II's R1 row points at the benchmark display
("self-contained in App. E 2, Eq. (E5)"); Sec. V's spanning-list paragraph
points at `eq:Seff_dim4`. Verified in the rendered PDF (pages 12 and 22).

---

### R11-GNR-10 [P] — inline repository paths in the main text (Gemini M3)

**Verdict: GENUINELY-NEW-REAL, presentation-grade.** Verified: Sec. V, App. A,
App. C and App. A 1 printed `arxiv/scripts/dim4_parityodd_enumeration.py`,
`research/theory_audit/operator_basis_adjudication_2026_08_07.py` and
`arxiv/scripts/fierz_lemma_check.py` inline. Gemini's required fix is the
right one: cite scripts by functional name in the body, keep repository
locations in Data and Code Availability. R10's `/latex-audit` had noted three
raw `\texttt{}` script paths as "pre-existing"; R11 closes them.

**Closure:** every inline directory path removed. Body references now read
"the independent operator-basis adjudication script, listed with its
repository location in the Data and Code Availability statement" and
`\texttt{dim4\_parityodd\_enumeration.py}` (bare functional filename, retained
because the surrounding sentence's honesty content — "which, its filename
notwithstanding, verifies the two identities and performs no basis
enumeration" — depends on the name). App. C's `fierz_lemma_check.py` mention
became "A further released script". All six `\artifact{}` targets remain,
correctly, in the Data and Code Availability block, and all six were verified
to resolve to existing repo paths.

---

### R11-GNR-11 [P] — abstract's spanning-list description omits the zero-derivative construction qualifier (Gemini N1)

**Verdict: GENUINELY-NEW-REAL, presentation-grade.** Verified: Sec. V excludes
√−g ∇_μ J^{5μ} — which otherwise meets every listed criterion — by the
zero-additional-derivative rule, and the abstract did not carry that
qualifier. Related in kind to R10-GNR-9 (the parity-odd qualifier), and closed
the same way.

**Closure:** the abstract's spanning-list description now reads "…*algebraic*
in the sense of the zero-additional-derivative construction rule stated in the
text, exhibited under those construction rules…".

---

### R11-GNR-12 [P] — version-history prose in the Fig. 1 caption (Gemini N2)

**Verdict: GENUINELY-NEW-REAL, presentation-grade** — same class as
R10-GNR-13, which removed "as earlier versions of this list did" from Sec. V.
Verified: the Fig. 1 caption carried "The branch letters are inherited
unchanged from the historical catalog, which never assigned the letters I or
K; no branch entries have been removed" — internal review-log prose with no
value to a reader of the published paper.

**Closure:** sentence deleted. Verified in the rendered p.5.

---

### R11-GNR-13 [P] — dimension bookkeeping stated imprecisely (Gemini N3)

**Verdict: GENUINELY-NEW-REAL, presentation-grade.** Verified: Sec. IV A read
"carries dimension −1 + 2 + 3 = +4 and the action is dimensionless, as
required". Gemini is right on the field theory: the *Lagrangian density*
carries mass dimension +4, which makes the action dimensionless on integration
over d⁴x.

**Closure:** "…is a Lagrangian density of mass dimension −1 + 2 + 3 = +4, so
that the action, obtained by integrating it over d⁴x, is dimensionless, as
required."

---

### R11-GNR-14 [P] — stale Fig. 1 source comment contradicts the closed v1C.0.13 scoping (Claude MINOR-6)

**Verdict: GENUINELY-NEW-REAL, presentation-grade**, and recorded with the
reviewer's own qualification: **this was never a defect in the compiled PDF**,
and the leg explicitly did not count it against the manuscript. `main.tex`'s
TikZ block carried `%% --- B14 (Branch H) constrains all four routes
[R1--R4]; …` after R10-GNR-1 narrowed the tag; the drawn arrows and in-figure
labels were already correct (verified in the p.5 render).

**Closure:** comment rewritten to describe the actual attribution and to carry
a standing warning for the next editor of that figure ("B14 does NOT constrain
R1 (v1C.0.13 MAJOR-1); do not re-widen this tag when editing the figure").
Flagged here because it was, in the reviewer's phrase, "a live landmine for
whoever edits that figure next".

---

### R11-RF-1 — "not self-contained; load-bearing derivations imported by citation" (Grok E3; Gemini M2)

**Verdict: RE-FLAG.** This is the longest-running chain in the paper's
history: R1 `GNR-2` → R2-RF-2 → R3-RF-2 → R4-RF-1/RF-6 → R5-RF-4 → R6
critical adjudication (App. E added) → R7-RF-2/RF-9 → R8-RF-3/RF-10 →
R9-RF-1 → R10-RF-1. Closed by real action across v1C.0.4 (App. D: a
self-contained statement and proof of B14) and v1C.0.9 (App. E: the
torsion-elimination chain and R1 benchmark arithmetic carried
self-contained), and R11 strengthens App. D further under R11-GNR-6/GNR-7.

**Falsified again by this round's own opposing leg**, and more decisively than
in any prior round: the Claude leg recomputed **30 displayed relations from
the PDF alone**, including the Fierz involution (all 25 entries), the Eq. (4)
flow integration to two significant figures, the App. A hierarchy and the
App. E benchmark chain. A manuscript from which an independent referee can
reproduce thirty quantitative claims without opening the companion is not one
whose load-bearing steps are unverifiable.

Gemini M2's narrower version (R4 rests on a non-peer-reviewed companion) was
closed at R10-GNR-14 by explicit re-scoping plus the two checkable steps
stated in-text; the sentence Gemini quotes *is* that closure, and the paper
now says plainly what is not reproduced here and that the R4 leg rests on
those external derivations for anything beyond the naturalness statement made
here. Restating a disclosure as a defect is a re-flag.

### R11-RF-2 — "abstract's 61–67 orders / ≥58 orders not derived in closed form from displayed inputs" (Grok E1)

**Verdict: RE-FLAG.** Closed at R3 (v1C.0.6): the abstract, Sec. IV B and
Sec. VII all label the ~67-order endpoint as the derived integrated flow and
the ~61-order endpoint as the deliberately pessimistic chiral-count bound, and
the labels are present verbatim in the exact v1C.0.13 PDF Grok reviewed. The
identical complaint was dispositioned at R10-RF-4. Additionally falsified in
the arithmetic: the Claude leg reproduced 0.3 × 1.18×10⁻⁶¹ = 3.5×10⁻⁶² (~61
orders) and 1.4×10⁻⁶ × 1.18×10⁻⁶¹ = 1.65×10⁻⁶⁷ (~67 orders) *from the printed
inputs*, which is precisely the closed-form recomputation Grok says is
impossible.

### R11-RF-3 — "abstract's six-member spanning list claims a stronger structural result than the body establishes" (Grok E2)

**Verdict: RE-FLAG**, with one genuine residue closed elsewhere. The abstract
already carries, in the same sentence, "The list is deliberately redundant:
independent symbolic computation gives it rank four (two exact relations …),
and rank two modulo total derivatives, so it is a generating set of
recognizable invariants and not a linearly independent basis" and "That the
list *spans* the rule-admitted operator space is asserted from the
construction rules, not proved by exhaustive symbolic enumeration" — the exact
calibrated statement Grok asks for, added at R9-GNR-1/R10-GNR-6. The one thing
genuinely missing was the zero-derivative construction qualifier, which Gemini
identified precisely and which is closed as R11-GNR-11.

### R11-RF-4 — "eight of the fourteen entries are general naturalness or classification arguments, inflating the ECH-specific count" (Grok E4)

**Verdict: RE-FLAG.** The paper states this itself, in the Fig. 1 caption Grok
was looking at: "the entries differ in evidentiary status — the sole Tier-I
rigorous theorem is B14's perturbation transparency … the remainder are
structural or ansatz-level arguments of mixed individual strength, and **five
entries (B5–B7, B10, B13) are general naturalness or classification
arguments**". Sec. III's preamble says the same ("a structured map of failure
modes of mixed individual strength … not a claim that fourteen separately
decisive theorems each independently exclude the framework"), and Table II
records the per-route classification. Grok's count of eight is also not
supported: the entries it names (B5–B7, B10, B13) number five, which is the
number the paper already prints. Disclosure, not defect.

### R11-RF-5 — "23 pages is too long; reduce to ≤12 pp" (Grok M1)

**Verdict: RE-FLAG**, and recorded honestly rather than smoothed. The chain
runs R1 `GNR-3` residual → R2-RF-7 → R3-RF-7 → R4-RF-10 → R6-RF-4 →
R7-RF-11/12 → R8-RF-12 → R9-RF-6 → R10-GNR-15, where seven redundant passages
were actually cut. The target is not met and, as recorded at R10, is not
reachable without deleting catalog content — which the round directive forbids
and which would be dishonest scoping. **This round the page count rose again,
23 → 24 pp**, because four claim-scoping closures required new text. That is
reported, not hidden. Grok's second premise ("only one Tier-I result in 23
pages") is also now *more* true than when it was written, since R11-GNR-1
regrades a leg downward — the paper's response is that a survey's value is
coverage, not theorem count, which Sec. III states outright.

### R11-RF-6 — "Fig. 1 implies a tighter logical dependence than exists between B8 and B14" (Grok M2)

**Verdict: RE-FLAG.** Closed at R10-GNR-1 (v1C.0.13), which rewrote the Fig. 1
caption to state the independence explicitly ("B8 and B14 are logically
independent: B8 is a statement about the fermionic (J⁵)² sector, whereas B14's
hypotheses require zero spin density and expressly exclude fermion sources, so
neither implies the other and both are counted"), changed the in-figure R1 edge
label from "B8, B14" to "B8", and added the same statement to the Table I
caption. Grok's "required fix" (redraw with explicit independent edges or drop
the unified-closure claim) describes the edit that had already landed in the
PDF it reviewed.

### R11-RF-7 — "Route-2 α/M is an external ACT DR6 fit, not an internal prediction" (Grok M3)

**Verdict: RE-FLAG.** The paper says exactly this, twice, in the text Grok
quotes: Sec. IV A states the value is "not reproduced from the minimal ECH
field content", and Sec. IV C's R4 discussion states that "ECH supplies
neither m_θ ∼ H₀ nor the fitted α/M, relocating the CC problem" — which is the
survey's *conclusion*, not an oversight. Table II's R4 row carries the same
label. Restating the paper's own headline finding as a required fix is a
re-flag.

### R11-RF-8 — "'the companion paper' should carry the non-peer-reviewed Zenodo qualifier at every occurrence" (Grok N1)

**Verdict: RE-FLAG.** The provenance boundary is disclosed at p.16 in the Data
and Code Availability statement, and Sec. IV C states in the body that the R4
leg "rests on those external, not-yet-peer-reviewed derivations" (the
R10-GNR-14 closure). R10-GNR-12 removed exactly this kind of defensive
repetition at Grok's own earlier request (N4, "consolidate the defensive
'companion does not retain' phrasing to a single statement"). Reinstating the
qualifier at every occurrence would reverse a closure this reviewer asked for
one round ago, and would restore prose R10 cut for length in response to this
reviewer's length complaint.

### R11-RF-9 — "'none a logical consequence of another' is redundant with the body" (Grok N2)

**Verdict: RE-FLAG / declined with reason.** The clause is not cosmetic: it is
the independence claim that licenses counting fourteen distinct constraints
rather than reporting a catalog of overlapping observations, and it is exactly
the claim R10-GNR-1 had to litigate (whether B8 was subsumed by B14). The
abstract is the one place a referee checks it. The sentence carrying it was
rewritten this round anyway under R11-GNR-3, and the clause was deliberately
retained.

### R11-DEF-1 — frozen-release Zenodo DOI for this survey's own verification scripts (Gemini E1)

**Verdict: DEFERRED-GENUINE (P-round packaging)** — carried forward unchanged
from R10-DEF-1. The requirement is real, the paper already discloses that the
deposit is planned rather than done, and minting a DOI is a publish action
requiring Houston. Not closed, not dismissed. Chain: R2-SO-2 → R3-RF-6 →
R4-RF-8 → R5-GNR-2 → R6-RF-9 → R7-RF-8 → R8-RF-11 → R9-RF-9 → R10-DEF-1 →
R11-DEF-1.

### R11-FAL-1 — "the Planck-mass symbol M_Pl is overloaded to mean two values differing by √8π" (Gemini M1)

**Verdict: FALSIFIED, with receipts.** Gemini quotes Sec. II as reading "in
terms of the reduced Planck mass $M_{Pl} \equiv (8\pi G)^{-1/2}$", i.e. the
*same* symbol as the full Planck mass. It does not. The source reads
`\overline{M}_{\rm Pl}\equiv(8\pi G)^{-1/2}`, and the compiled PDF was
re-rendered at 300 DPI (page 2, right column) and read directly: the printed
symbol carries a **visible overline**, distinct from the bare `M_Pl` used in
order-of-magnitude prose. Independently corroborated by `pdftotext`, which
extracts the reduced symbol as `M Pl` (overline dropped, spacing artifact
left behind) and the full symbol as `MPl` — the two are different glyphs in
the PDF. The paper uses distinct symbols and states the relation exactly
(κ = 8π M_Pl⁻² = M̄_Pl⁻²), which is precisely the fix Gemini demands.

**This is the fifth member of the rasterization/extraction-artifact family**
(R3-FAL-2 → R5-RF-7/R5-FAL-1 → R7-FAL-1 → R8-FAL-4 → R9-FAL-4 → R11-FAL-1),
and the first in which the *reviewing vendor* rather than the reviewing leg
was the one misled. The standing ≥300 DPI re-render protocol caught it again
and should stay. Note the cost: this artifact accounts for Gemini's regression
from MINOR REVISIONS (R10) to MAJOR REVISIONS (R11), i.e. a verdict-word move
driven by a rendering bug rather than by the manuscript — a concrete instance
of the directive-H-refined rationale for not treating verdict words as the
gate.

## Candidate findings withdrawn by the reviewing leg

None this round. Unlike R8, R9 and R10 — each of which produced at least one
low-DPI false positive that the reviewing leg raised and self-withdrew — the
R11 Claude leg's 300-DPI-first method produced no withdrawn candidates. The
artifact family did fire this round, but on the Gemini leg (R11-FAL-1), which
has no equivalent re-render step. Recorded so the protocol's value is visible
on both sides of the board.

## Ledger totals

| Verdict | Count | Items |
|---|---|---|
| GNR (genuinely-new-real) | 14 | R11-GNR-1 … R11-GNR-14 |
| ADJ (adjudication-driven) | 0 | — |
| RE-FLAG | 9 | R11-RF-1 … R11-RF-9 |
| FALSIFIED | 1 | R11-FAL-1 |
| DEFERRED-GENUINE | 1 | R11-DEF-1 |
| SCOPE-OPINION | 0 | — |
| OPINION | 0 | — |
| **Total canonical items** | **25** | Claude 4 MAJOR + 6 MINOR (10) → GNR-1…GNR-9, GNR-14, all canonical. Grok 4 ESSENTIAL + 3 MAJOR + 2 NIT (9) → RF-1…RF-9, with E2's one genuine residue (the zero-derivative qualifier) merged into GNR-11. Gemini 1 ESSENTIAL + 3 MAJOR + 2 MINOR + 1 NIT (7) → DEF-1 (E1), FAL-1 (M1), RF-1 (M2, deduped with Grok E3), GNR-10 (M3), GNR-11 (N1), GNR-12 (N2), GNR-13 (N3) |

**Genuinely-new-real total: 14 (14 GNR + 0 ADJ).**

## Classification table

| Grade | Count | Items |
|---|---|---|
| **Correctness-grade GNR** | **6** | GNR-1 (Tier-(I) count + regrade), GNR-2 (residual NDA delegation), GNR-3 (abstract universal quantifier), GNR-4 (App. C uniqueness inverted vs artifact), GNR-5 (1.5 → 1.7 orders), GNR-6 (App. D kernel lemma asserted) |
| Presentation-grade GNR | 8 | GNR-7 … GNR-14 |

This matches the Claude leg's own self-classification (it classed MAJOR-1
through MAJOR-4 and MINOR-1, MINOR-2 as `[correctness]`, and MINOR-3 through
MINOR-6 as `[presentation]`), with four further presentation-grade items
originating from the Gemini leg (GNR-10, GNR-11, GNR-12, GNR-13).

## Deferred-genuine list (carried, not closed)

1. **R11-DEF-1** — frozen-release Zenodo DOI for this survey's own
   verification scripts. Owner: P-round packaging. Blocker: DOI minting is a
   publish action requiring Houston; the paper discloses the deposit as
   planned. Carried unchanged from R10-DEF-1.

## Anti-regression guard introduced this round

`tools/p1c_consistency_check.py` — a stdlib-only mechanical self-consistency
linter for `arxiv/paper1c_nogo_survey/main.tex`, written because three of this
round's four MAJORs are the *residue of the previous round's closure sweep*
and are all mechanically detectable. Four rules:

| Rule | What it checks | Which R11 MAJOR it would have caught |
|---|---|---|
| **A** | Every asserted catalog-size claim (abstract, intro, Sec. III, Fig. 1 caption, Table I caption, Sec. VI, Sec. VII, App. A) agrees with every other, and with the actual count of `\textbf{B<n> ---}` entries | R10-GNR-1's 13 → 14 recount; guards against a partial recount |
| **B** | Prose Tier-(I) count assertions ("sole" / "the only" / "exactly one" / "two") equal the counted `\textbf{(I)}` markers inside the `tab:evidentiary_status` table body | **MAJOR-1** |
| **C** | An extensible paired-phrase list: fails when a sentence asserts something a companion sentence explicitly disclaims. Seeded with `nda_covers_eq1`, `nda_operator_label`, `route2_de_nda` | **MAJOR-2** |
| **D** | A universal per-entry closure claim in the abstract fails when any catalog entry declares itself a non-closure | **MAJOR-3** |

LaTeX comments are stripped before analysis, so the ~340-line `%` changelog
header (which necessarily records superseded counts and tier claims) cannot
produce false positives. Failures name the rule, the conflicting values, and
every source line involved.

**Proof it works, recorded as evidence rather than assertion.** Run against
the pristine v1C.0.13 source (`git show HEAD:…main.tex`) it exits **1** and
fires:

- Rule B FAILED — 2 Tier-(I) markers in Table II (lines 1540, 1567) against
  nine prose sites each implying 1.
- Rule C FAILED — `nda_covers_eq1` (assert line 1384 vs disclaim line 1184)
  and `nda_operator_label` (assert line 1391 vs disclaim line 1184).
- Rule D FAILED — universal claim at line 310 against B9 (line 844) and B14
  (line 916).
- Rule A PASSED — 14 agrees everywhere, correctly.

That is MAJOR-1, MAJOR-2 and MAJOR-3 rediscovered mechanically, with no
reviewer in the loop. Against v1C.0.14 it exits **0**, all four rules PASS.

Deliberately **not** a git hook (per the round directive): it is documented in
`ops/RUNBOOK.md` and in its own SKILL-style module docstring as the check to
run before every P1C version bump and round-closure commit. Covered by
`tools/tests/test_p1c_consistency_check.py` (16 tests, synthetic pass/fail
fixtures per rule plus a real-manuscript smoke test).

**Skill-improvement note for the loop.** The generalizable lesson is that
"grep every instance and reconcile" is a closure step that silently
under-performs, and its failures are invisible until the next round's referee
finds them. Where a claim-scoping closure touches N surfaces, the durable fix
is a checker that counts them, not a more careful sweep. This pattern is
transferable to any paper carrying a headline count, a tier ladder, or an
explicit non-claim.

## Closure evidence (v1C.0.14)

- `arxiv/paper1c_nogo_survey/main.tex` — `\paperVersion` `v1C.0.13` →
  `v1C.0.14`, `\paperTimestamp` `August 7, 2026`, no printed `\date`,
  provenance in `pdfkeywords` (verified: `pdfinfo` → `Keywords: v1C.0.14
  (August 7, 2026)`).
- `arxiv/paper1c_nogo_survey/references.bib` — one entry added (`Hehl1976`,
  Rev. Mod. Phys. **48**, 393 (1976)), 25 → 26; `\cite` / `.bbl` / `.bib`
  remain in exact three-way agreement.
- 4-pass compile (`pdflatex` ×1 → `bibtex` → `pdflatex` ×3): **0 LaTeX errors,
  0 undefined references, 0 overfull hboxes** (41 underfull, badness-only
  revtex float artifacts).
- **Float regression caught and fixed inside the round.** The first
  v1C.0.14 compile produced two warnings absent from v1C.0.13 ("Float too
  large for page by 11.5 pt" and "A float is stuck") because the MAJOR-1
  regrade lengthened Table II's R2 cell. Confirmed new by compiling pristine
  v1C.0.13 from `git show HEAD:` in a clean directory (0 stuck floats, 0
  overfull, 23 pp). Fixed by condensing the R2 cell to roughly its original
  length and setting `\begin{table*}[!tb]` on `tab:evidentiary_status`. Both
  warnings now zero.
- `/latex-audit`: **PASS.** Log scan clean. Pages 1 (title block + abstract),
  5 (Fig. 1 + Table I), 10 (the NDA closure), 12 (Table II), 21 (App. C
  uniqueness correction), 22 (App. D kernel lemma + App. E cross-refs)
  rendered and visually confirmed — no column-gutter crossings, no
  right-margin overruns, no float escapes, no "(Dated:)" remnant in the title
  block, Table II placed cleanly at the top of p.12 with exactly one bold
  **(I)**. All 6 `\artifact{}` targets verified to resolve to existing repo
  paths. No `\date` overflow risk (no `\date`). Two raw `\texttt{}` paths
  remain and are now bare functional filenames rather than directory paths
  (R11-GNR-10), both wrapping at 0 overfull.
- `tools/p1c_consistency_check.py`: **4/4 rules PASS, exit 0.**
- Served PDF: **24 pp**, md5 `fa485e592afe602d7258f17606e3278a`, sha256
  `9dd5c70862d3cad153143ead91f22e7fc5e410e8ac227aec24b13bd015ce17c3`.
  Mirrored byte-identical to `site/public/papers/`, `public/papers/` and
  `site/out/papers/` as `paper1c_nogo_survey_v1C.0.14.pdf` (all md5-verified).
- `project-context/draft_paper_registry.json` — served alias bumped to
  `paper1c_nogo_survey_v1C.0.14.pdf`.
- `site/src/data/papers.ts` — P1C entry href and description updated to
  v1C.0.14.
- `site/src/data/reviewTimeline.ts` — R11 round entry added, plus a separate
  `kind: "skill-improvement"` entry for the consistency linter (newest-first).
- `project-context/SSOT/paper-1c/status.md` — R11 matrix, GNR-by-grade, the
  linter recorded as the anti-regression guard, and R12 set as the next
  correctness check.

## Convergence read

**R-phase NOT converged at R11.** Six correctness-grade GNR items were found
and closed, four of them headline-touching. The standing rule (zero
correctness-grade GNR on a full board) is not met.

Three things are worth recording honestly, because together they say something
about where this paper actually stands:

1. **Two consecutive rounds with zero computational errors**, and R11
   quantified it: 30 independent recomputations, one rounding slip. The
   arithmetic spine of this survey has been checked from the PDF alone, twice,
   by an adversarial leg that self-withdrew nothing this round.
2. **The remaining defects have changed kind.** R1–R9 produced wrong numbers,
   wrong coefficients and wrong identity chains. R10 and R11 produce
   *disagreements between two places in the same document*. That is the
   failure mode of a manuscript being revised repeatedly under pressure, not
   of a manuscript whose physics is unsettled.
3. **Three of R11's four MAJORs were created by R10's closure.** This is the
   important signal, and it is why the round's durable output is a linter
   rather than a longer checklist. A closure that touches six surfaces and
   lands on five is indistinguishable, to the closing agent, from one that
   lands on six. Only a counter can tell them apart.

Against that, R11 also moved a claim *down*: Route 2's dark-energy leg is now
Tier-II in both branches rather than Tier-I in one, and the abstract no longer
claims that every catalog entry closes a route. Both are reductions in
asserted strength, made because the paper's own definitions and its own
entries required them. That is the honest direction of travel.

R12 on the exact v1C.0.14 PDF is the next correctness-convergence check, and
it is the first round that will run against a manuscript with a mechanical
self-consistency gate in front of it. No readiness score has been computed and
no venue/Zenodo kit exists for this draft.
