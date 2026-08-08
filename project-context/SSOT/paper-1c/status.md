# P1C status — current authoritative section

**Current candidate:** draft v1C.0.15 · 2026-08-07 ·
`arxiv/paper1c_nogo_survey/main.tex`

**Status: R12 CORRECTNESS-CONVERGENCE BOARD RUN AND TRUTH-AUDITED →
15 GENUINELY-NEW-REAL FINDINGS CLOSED (v1C.0.15): 11 CORRECTNESS-GRADE +
4 PRESENTATION-GRADE. THE ROUND'S HEADLINE IS A CORRECTION TO THE
MANUSCRIPT'S ON-SHELL TORSION: THE REFEREE CHALLENGED A LOAD-BEARING
PHYSICAL PREMISE, THE CHALLENGE WAS ADJUDICATED BY SOLVING THE
EINSTEIN–CARTAN–HOLST CONNECTION EQUATION FROM SCRATCH, AND **THE REFEREE
WAS CORRECT**. THE MINIMAL-ECH ON-SHELL TORSION IS NOT PURELY AXIAL AT
FINITE γ; O4 IS NOT IDENTICALLY ZERO; O1 AND O6 ARE NOT EXACT TOTAL
DERIVATIVES. THE PHYSICS CONCLUSION SURVIVES — EVERY AFFECTED OPERATOR
LANDS IN THE κ-SUPPRESSED FIERZ-CLOSED (J⁵·J⁵) CLASS THE PAPER ALREADY
BOUNDS. THIS ROUND ALSO OVERTURNS A RESULT ONE OF THIS REPOSITORY'S OWN
RELEASED ARTIFACTS ASSERTED; THAT ARTIFACT NOW CARRIES A DATED ERRATUM
ADDENDUM THAT SCOPES ITS CONCLUSIONS WITHOUT EDITING THEM.
R-PHASE NOT CONVERGED AT R12 — R13 on the exact v1C.0.15 PDF is REQUIRED
and is the next CORRECTNESS-CONVERGENCE CHECK.**
The R12 board ran on the exact v1C.0.14 PDF (sha `9dd5c708…`), three legs
with raw receipts.

**R12 verdict matrix (2026-08-08, exact v1C.0.14 PDF):**

| Leg | Model | Verdict |
|---|---|---|
| Claude INT (Opus-tier) | claude opus | **MAJOR REVISIONS** (2 MAJOR / 9 MINOR; 5 candidate findings withdrawn by the leg after 300-DPI re-render or artifact cross-check). Both MAJORs trace to a single premise — that the ECH torsion is purely axial — and **both are confirmed correct** by independent computation |
| Grok API | grok-4.3 | **REJECT** (3 ESSENTIAL / 3 MAJOR / 2 NIT) — every complaint is scope, self-containment or length; none is computational, and none touches the defect this round found |
| Gemini API | gemini-3.1-pro-preview | **ACCEPT WITH MINOR CORRECTIONS** (1 MINOR / 2 NIT; pass-2 NO_NEW) — Gemini's second ACCEPT-class verdict on P1C (after R4) and the board's third overall (Gemini R4, Claude R5, Gemini R12). It calls the Cartan derivations "flawless" and "exact" on the exact PDF whose Cartan branch this round corrects |
| Perplexity | (optional leg) | FAILED — failure record, never a verdict |

The verdict-first truth audit against the R1–R11 disposition ledgers and the
released theory-audit artifacts
(`project-context/peer-reviews/INT_v3/ROUND_2026-08-08-P1C-v1C.0.14-EXACTPDF-9dd5c708-R12CONV/P1C_v1C.0.14_R12_truth_audit.md`)
deduplicated the board to **24 canonical items: 15 genuinely-new-real (14 GNR
+ 1 adjudication-driven, all closed in v1C.0.15), 6 re-flags of
R1–R11-dispositioned content, 2 freshly falsified with receipts, 1
deferred-genuine** — plus the 5 candidates the reviewing leg withdrew before
the board.

**GNR by grade (all 15 closed in v1C.0.15):**

- **Correctness-grade (11)** — R12-GNR-1 (on-shell torsion irreps, O4 ≠ 0,
  O1 = O6 not total derivatives), R12-GNR-2 (the cited artifact evaluated an
  Einstein–Cartan configuration and was reported as an ECH verification),
  R12-ADJ-1 (Sec. II vs App. E torsion normalizations differed by a factor
  two — raised by neither party, surfaced by the adjudication),
  R12-GNR-3 (App. C's "trace-vector irreps appear only when minimal coupling
  is relaxed" is false), R12-GNR-4 (Levi-Civita "symbol" printed with the
  Lorentzian tensor identity), R12-GNR-5 (the stated explanation for the
  Nieh–Yan factor of two does not account for it), R12-GNR-6 (`M_Pl` printed
  inside an identity exact only for `M̄_Pl`), R12-GNR-7 (six branches vs four
  constrained channels, qualifier absent from the abstract), R12-GNR-8
  (abstract's 61–67 orders carried by an unlabelled Tier-III scaling
  relation), R12-GNR-9 (Table II's "exploratory, not load-bearing" vs the
  abstract's headline), R12-GNR-10 (abstract's flat "none a logical
  consequence of another"). Four of these are graded **above** the reviewing
  leg's own `[presentation]`/`[scope]` tags, deliberately and auditably, per
  the standing rule that a wrong claim is correctness-grade.
- **Presentation-grade (4)** — R12-GNR-11 (Case I referent), R12-GNR-12
  (Shapiro–Teixeira arXiv-version note), R12-GNR-13 (abstract sentence
  split, Gemini N1), R12-GNR-14 (density-symbol gloss, Gemini N2).

**The round's headline, stated once and precisely.** The adjudicating module
`research/theory_audit/ech_torsion_onshell_2026_08_08.{py,json,md}` (commit
`2d7db648`) sets up the first-order ECH action in explicit components and
**solves** the connection equation — varying with respect to all 24
independent contorsion components with no irrep ansatz, cross-checked against
an independent differential-form route, under both Holst sign conventions,
in exact symbolic arithmetic. The on-shell torsion is

> `T_{abc} = α ε_{abcd}J^{5d} + β(η_{ab}J⁵_c − η_{ac}J⁵_b)`,  `β/α = 1/(2γ)`

with the **axial (4) and trace-vector (4) irreps both nonzero** at every
finite nonzero γ and the **tensor (16) irrep identically zero**. Pure
axiality is the γ → ∞ Einstein–Cartan limit only; at γ = 0.2375 the
trace-vector coefficient is **2.11×** the axial one (1.82× at γ = 0.274), so
the non-axial piece is the larger of the two. Consequences landed in
v1C.0.15:

- `O4(bare) = −24αβ(J⁵·J⁵) = −192π²G²γ³/(1+γ²)²(J⁵·J⁵)`, i.e.
  `O4^[4] = −3κγ³/(1+γ²)²(J⁵·J⁵)` — **not zero**. The paper's "strictly
  stronger disposal" claim is **withdrawn**. The referee's independently
  claimed value is confirmed *exactly* (difference 0, ratio 1, sign
  included) in App. E's normalization.
- `O1^[4] = O6^[4] = −O2^[4] + ½O4^[4]` on shell — O1 and O6 are a total
  derivative **plus** a contact term, not exact total derivatives.
- `O1 = O6` and the Nieh–Yan relation `2O1 + 2O2 − O4 = 0` **survive**,
  re-verified at finite γ on six explicitly curved on-shell ECH
  configurations (γ ∈ {19/80, 1, 3}); `O1 = −O2` **fails** — it required
  `O4 = 0`.
- **The no-go holds.** O1, O4 and O6 join O5 in the κ-suppressed
  Fierz-closed `(J⁵·J⁵)` class, at the same `M̄_Pl^{-2}` power, with
  `O4^[4]/O5^[4] = γ/(1+γ²) ≈ 0.22`. No new light scale appears; the "no
  (meV)⁴ vacuum energy without a new light scale" conclusion is unchanged.
  Disposal class (i) loses O1 and O6 to class (ii); class (iii) loses O4.

**Convention fixed in the same round.** Sec. II's `T = κS` and App. E's
Eq. (E2) fixed the same object in normalizations differing by a factor two in
torsion amplitude (four in any quadratic-in-`T` density). The survey now uses
**one** normalization throughout — **App. E's, i.e. Eq. (E2)**, the
Freidel–Minic–Takeuchi solution of the connection equation — stated as such
in both Sec. II and App. E. It is chosen because it is the paper's only
*derived* on-shell torsion and the normalization in which the independently
solved connection equation and the referee's O4 both land exactly.
Consequently O5 reduces to `−3κ[γ²/(1+γ²)](J⁵·J⁵)`, and Check D's ε-free
square is restated in the normalization-independent form
`T_{abc}T^{abc} = −6α²(J⁵·J⁵)`.

**Integrity note — recorded here, and deliberately kept out of the paper.**
This round changes a result `operator_basis_adjudication_2026_08_07.md`
asserted. That artifact's premise — "the paper's on-shell Cartan torsion … is
verified to be pure axial" — was an **imposed input**, not a solved output:
the module substitutes a totally antisymmetric tensor and then verifies it is
totally antisymmetric, and γ never enters it, so its "curved on-shell
configuration" is Einstein–Cartan, not Einstein–Cartan–Holst. A dated
**ADDENDUM — ERRATUM OF 2026-08-08** is appended to that report; it edits
nothing above it, scopes the affected conclusions item by item, and lists
what is unaffected and independently re-confirmed at finite γ (rank 4,
nullity 2, both null vectors, `O1 = O6` including the Γ route, the
density-normalization cross-check, the subset ranks, the Fierz results).
Per directive Q1 **no mistake-narration goes into the manuscript**: the paper
states only the correct physics; the process record lives in
`project-context/`.

**Durable lesson.** A released verification artifact can be internally
correct and still carry a premise it never solved for. Two rules: (1)
re-derive the premise from the governing equation rather than inheriting it —
the mechanically detectable tell here was that γ, the one parameter
distinguishing ECH from EC, appeared nowhere in a module whose conclusions
were reported as ECH results; (2) erratum by dated addendum, never by edit,
so the original text and its provenance survive. Also recorded: the
mechanical self-consistency linter passed 4/4 on v1C.0.14 — correctly, since
the manuscript was self-consistent. Its four claims about torsion irreps, O4,
O1/O6 and App. C's scope all agreed with each other. They were agreed and
wrong. A self-consistency linter is the right tool for the R10/R11 failure
mode and structurally the wrong tool for this one.

**Falsified with receipts (2).** Grok M2's "the two-order conservative
allowance is unquantified and unreferenced" — the two orders are the explicit
computed difference between two index-contraction orderings both printed in
the text (`1.7×10⁻⁶⁰` vs `≈2×10⁻⁶²`), with the paper adopting the *less*
favourable and saying so; both reproduced by this round's opposing leg. Grok
N1's "Table II mixes three tiers without repeating the label on every row" —
verified at the exact PDF, p. 12: all five rows open with their own bold tier
marker.

**Deferred-genuine (1).** R12-DEF-1, the frozen-release Zenodo DOI for this
survey's own verification scripts — now **eight** files rather than six.
Carried unchanged from R11-DEF-1; a P-round packaging item requiring Houston.

**Closure evidence (v1C.0.15).** 4-pass compile: **0 LaTeX errors, 0
undefined references, 0 overfull hboxes**, 25 pp (24 → 25; the correction
required new text, reported rather than smoothed). Two float regressions
introduced by the correction were caught and fixed inside the round (Table III
overflowing its full-width float by 28.5 pt; Table II becoming too large for
the page by 22 pt), both confirmed new against a pristine v1C.0.14 compile.
`/latex-audit`: **PASS** — pages 1, 2, 3, 13, 15, 17, 21, 22 rendered and
visually confirmed; all **8** `\artifact{}` targets resolve.
`tools/p1c_consistency_check.py`: **4/4 rules PASS, exit 0**. Served PDF md5
`3a46b8c270906e0b943d7c0082f36922`, sha256
`f3e29c45df35f7ac358d8f4e6a854d1b9f79fa20c71a725922732db82bd967d4`, mirrored
byte-identical to `site/public/papers/`, `public/papers/` and
`site/out/papers/` as `paper1c_nogo_survey_v1C.0.15.pdf` (all four copies
md5-match). `draft_paper_registry.json`, `site/src/data/papers.ts` and
`site/src/data/reviewTimeline.ts` (R12 round entry + a `skill-improvement`
entry for the solve-don't-inherit / erratum-by-addendum lesson) updated in
the same bundle; `cd site && npx next build` PASS.

**Next gate: R13** on the exact v1C.0.15 PDF — the first round that will
review an on-shell operator disposal derived from the solved connection
equation rather than from a substituted ansatz. No readiness percentage is
computed or claimed.

---

## Prior round — R11 (closed as v1C.0.14)

**Status: R11 CORRECTNESS-CONVERGENCE BOARD RUN AND TRUTH-AUDITED →
14 GENUINELY-NEW-REAL FINDINGS CLOSED (v1C.0.14): 6 CORRECTNESS-GRADE +
8 PRESENTATION-GRADE. ZERO COMPUTATIONAL ERRORS FOR THE SECOND
CONSECUTIVE ROUND, THIS TIME QUANTIFIED — 30 DISPLAYED RELATIONS
RECOMPUTED INDEPENDENTLY, ONE ROUNDING SLIP. ALL FOUR MAJORS WERE
INTERNAL-CONSISTENCY DEFECTS LEFT IN THE SEAMS OF THE v1C.0.13 REVISION
AND ARE CLOSED BY MAKING THE DOCUMENT AGREE WITH ITSELF AND WITH ITS OWN
ARTIFACTS — NEVER BY WEAKENING A RESULT OR INVENTING COVERAGE. A
MECHANICAL SELF-CONSISTENCY LINTER (`tools/p1c_consistency_check.py`) IS
THE ROUND'S DURABLE OUTPUT AND THE STANDING ANTI-REGRESSION GUARD.
R-PHASE NOT CONVERGED AT R11 — R12 on the exact v1C.0.14 PDF is REQUIRED
and is the next CORRECTNESS-CONVERGENCE CHECK.**
The R11 board ran on the exact v1C.0.13 PDF (sha `d3aea74d…`), three legs
with raw receipts.

**R11 verdict matrix (2026-08-07, exact v1C.0.13 PDF):**

| Leg | Model | Verdict |
|---|---|---|
| Claude INT (Opus-tier) | claude opus | **MAJOR REVISION** (4 MAJOR / 6 MINOR; leg self-classes 6 correctness-grade) — with **ZERO computational errors** across a 30-item correctness ledger: the Fierz involution (all 25 entries), the Benedetti–Speziale flow integration, the O4/O5 tensor reductions and every App. A / App. E order-of-magnitude figure, each independently recomputed. One discrepancy, a rounding slip in a parenthetical. All four MAJORs are internal-consistency defects, not math |
| Grok API | grok-4.3 | **REJECT** (4 ESSENTIAL / 3 MAJOR / 2 NIT) — complaints are scope, self-containment and length, not computation |
| Gemini API | gemini-3.1-pro-preview | **MAJOR REVISIONS** (1 ESSENTIAL / 3 MAJOR / 2 MINOR / 1 NIT; pass-2 NO ADDITIONAL FINDINGS) — a regression from R10's MINOR REVISIONS driven mostly by a text-extraction artifact (see *Falsified with receipts*) |
| Perplexity | (optional leg) | FAILED — failure record, never a verdict |

The verdict-first truth audit against the R1–R10 disposition ledgers and the
released theory-audit artifacts
(`project-context/peer-reviews/INT_v3/ROUND_2026-08-07-P1C-v1C.0.13-EXACTPDF-d3aea74d-R11CONV/P1C_v1C.0.13_R11_truth_audit.md`)
deduplicated the board to **25 canonical items: 14 genuinely-new-real (all
closed in v1C.0.14), 9 re-flags of R1–R10-dispositioned content, 1 freshly
falsified with receipts, 1 deferred-genuine.**

**GNR by grade (all 14 closed in v1C.0.14):**

- **Correctness-grade (6)** — R11-GNR-1 (Table II's second Tier-(I) leg vs
  six "exactly one" text sites, and the regrade), R11-GNR-2 (residual NDA
  delegation at a fourth site), R11-GNR-3 (abstract's universal per-entry
  closure claim), R11-GNR-4 (App. C Grassmann uniqueness inverted relative to
  its own cited artifact), R11-GNR-5 (1.5 → 1.7 orders arithmetic),
  R11-GNR-6 (App. D's kernel lemma asserted rather than proved or cited).
  This matches the reviewing leg's own self-classification exactly.
- **Presentation-grade (8)** — R11-GNR-7 … R11-GNR-14.

**The defining feature of this round: all four MAJORs are
internal-consistency defects, and three of them are the residue of R10's own
closure sweep.** R10 correctly re-homed Route 2's dark-energy leg on the
operator list; in doing so it promoted the leg to a tier the list cannot
carry, did not propagate the change to the six "exactly one Tier-I"
surfaces, and left one un-swept sentence still delegating the operator to the
NDA bound the same revision had just concluded does not cover it. This is a
mechanically detectable failure mode, and it is why the round's durable
output is a linter rather than a longer checklist.

**MAJOR-1 — Table II carried two Tier-(I) legs while six text sites assert
exactly one, and the second (I) failed the paper's own Tier-I definition.**
Table II's R2 row printed a second bold **(I)** ("for constant Nieh–Yan
coefficient"), contradicted verbatim at six sites (abstract; Sec. III
preamble's "exactly one Tier-I rigorous theorem"; the B14 entry's "sole
Tier-I closure leg"; Sec. IV C's "the only Tier-I (rigorous) leg"; Sec. VI;
App. D's preamble) — and by Table II's own caption, "no leg is asserted more
strongly elsewhere". Independently, the grade over-reached: Sec. IV C defines
Tier-I as "a deductive consequence of stated equations/identities", but
"minimal Route 2 sources no dark energy" is not a statement about O1/O2 — it
is the statement that O1/O2 *exhaust* the rule-admitted content, i.e. the
spanning assertion the paper disclaims in six places as asserted-not-proved.
**Closure:** Table II's R2 dark-energy leg **REGRADED (I) → (II)** in both
branches, with the genuinely Tier-I ingredient (O1 and O2 are exact total
derivatives) named as such and the inherited assumption stated plainly;
Sec. IV A's "this *is* an operator-level (Tier-I) statement" and "closed at
Tier-I only in case (i)" rewritten to match, and followed by the explicit
sentence that the catalog's only Tier-I leg remains the
perturbation-transparency theorem. Verified mechanically: the
`tab:evidentiary_status` body now contains exactly one `\textbf{(I)}` marker
against nine prose sites each implying 1. **Route 2's dark-energy leg is
therefore stated at reduced strength — Tier-II in both branches rather than
Tier-I in one — because the paper's own definitions required it.**

**MAJOR-2 — a fourth site still delegated Eq. (1) to the single-scale NDA
bound the same revision explicitly disclaims.** Sec. IV B's summary paragraph
read "…and the operator is bounded by the single-scale NDA no-go regardless
of that O(1) normalization", flatly contradicting p.6 ("its dark-energy leg
is **not** closed by the single-scale NDA bound") and p.8 twice ("We
therefore do not claim the NDA bound covers it"; "…*not* by an amplitude
bound or by the single-scale NDA argument"). The v1C.0.13 note says "The
false delegation is removed"; it was removed at three sites and survived at
the fourth — the one a skimming referee consults for Route 2's headline
status, and the stronger of the two claims. **Closure:** clause replaced with
the accurate statement (the *birefringence* amplitude is bounded by the
explicit budget of Eq. (2), with the non-claim restated inline), then the
whole manuscript re-grepped for "NDA" — one sibling found and fixed ("the NDA
one-loop operator (R2)" → "the one-loop parity-odd operator (R2)"), every
other instance verified to attach the bound to the O1–O6 list or App. A's
ceiling, never to Eq. (1). Encoded permanently as linter Rule C.

**MAJOR-3 — the abstract's universal "each closing one or more of the four
routes" is falsified by two of the catalog's own entries.** B14: "B14 is not,
and is not used as, a closure of the fermionic or one-loop content of any
route." B9: "…so B9 is **never used as a stand-alone closure**." Note the
lineage: the phrase was *introduced* as the R4-GNR-10 closure (v1C.0.7), when
B14 still spanned all four routes; R10-GNR-1 narrowed B14's tag and stated it
closes none of them, and the abstract was not re-examined. **Closure:**
restated to the joint claim the catalog supports, naming the two non-closure
entries rather than papering over them. A sibling was caught in the same
sweep — Sec. I's "each is closed by an explicit, *individually labeled*
argument" now allows for more than one entry acting together. Encoded
permanently as linter Rule D.

**MAJOR-4 — App. C asserted Grassmann uniqueness for exactly the case its
cited artifact declares non-unique.** App. C read "an exact Grassmann-algebra
derivation of the operator row (the unique solution for **identical**
fields)". The cited artifact
(`research/theory_audit/fierz_adjudication_2026_08_05.{md,json}`) proves the
opposite in both its report and its machine output: `[L07]` attaches
uniqueness to **four distinct anticommuting fields**, and `[L10]` records
that for a single identical species the five quartics have span rank 3 with a
2-dimensional relation module — so identical-field rearrangement rows are
**not** unique. The paper had transposed the qualifier. **Closure:** corrected
to the artifact's actual result with the rank-3 caveat carried. Nothing
downstream moves — the row is separately confirmed by the artifact ([L11]) as
a valid identical-field Grassmann identity, and **G_s = −3κ/16 stands**,
independently re-verified by the reviewing leg via the bridge 4πG = κ/2.

**Arithmetic (MINOR-1, correctness-grade).** "Roughly 1.5 orders" was
inconsistent with the two components printed in the same sentence:
log₁₀(1/16π²) = −2.1982 against log₁₀(3.3) = +0.5185 sums to **−1.68**, not
−1.5. Both components were already correct; only the sum was wrong. Corrected
to **1.7** and verified in the recompiled PDF. The sentence exists
specifically to show the arithmetic, and the conservative direction, the
margins and every downstream number are unaffected.

**Other correctness closure (MINOR-2).** App. D's proof step (2) asserted
"whose invertible-tetrad kernel is trivial: T^I = 0" with no argument and no
citation — inside the load-bearing step of the paper's *only* Tier-I result,
in an appendix whose stated purpose is that the leg "can be refereed from
this manuscript". Independently verified before closing (the linear map
T^J_LM ↦ δ^[I_[K T^J]_LM] on the 24-dimensional torsion space was built
explicitly; **rank 24, kernel trivial**), then closed by stating the
condition in frame components and citing the standard Einstein–Cartan result
(Hehl, von der Heyde, Kerlick & Nester, Rev. Mod. Phys. **48**, 393 (1976)) —
a citation, not an invented derivation (`/never-fabricate-derivation`
observed). Bibliography 25 → 26 entries, `\cite` / `.bbl` / `.bib` still in
exact three-way agreement.

**Presentation closures (8).** App. D no longer "defers" a tensor-sector
extension its own Statement claims (the tensor conclusion is an immediate
corollary of the reduced action being exactly the Einstein–scalar action);
the branch→entry multiplicity is stated explicitly so 7 + 2 + 1 + 3 + 1 = 14
across 7 + 6 = 13 tested classes is legible in one place; eight orphaned
labels cross-referenced, including all four of App. E's previously
unreferenced numbered displays; inline repository paths removed from the main
text (they remain, correctly, in Data and Code Availability — Gemini M3, and
the "three pre-existing raw `\texttt{}` script paths" R10's latex-audit had
carried); the abstract's spanning-list "algebraic / zero-derivative"
qualifier added (Gemini N1, which is also Grok E2's one genuine residue);
Fig. 1 caption version-history prose removed (Gemini N2); the
Lagrangian-density dimension wording made field-theoretically precise
(Gemini N3); and a stale Fig. 1 source comment corrected, now carrying a
standing warning against re-widening B14's route tag.

**Falsified with receipts.** Gemini M1 (MAJOR) claimed the Planck-mass symbol
is overloaded, quoting Sec. II as "the reduced Planck mass $M_{Pl} \equiv
(8\pi G)^{-1/2}$". It is not: the source reads `\overline{M}_{\rm Pl}`, and
page 2 was re-rendered at **300 DPI** and read directly — the printed reduced
symbol carries a **visible overline**, distinct from the bare `M_Pl` used in
order-of-magnitude prose. Corroborated by `pdftotext`, which extracts the two
as `M Pl` (overline dropped, spacing artifact left behind) and `MPl`. The
paper already does exactly what Gemini demands and states the relation
exactly (κ = 8π M_Pl⁻² = M̄_Pl⁻²). **This is the fifth member of the
rasterization/extraction-artifact family** (R3-FAL-2 → R5-RF-7/FAL-1 →
R7-FAL-1 → R8-FAL-4 → R9-FAL-4 → R11-FAL-1) and the first in which the
*reviewing vendor*, rather than the reviewing leg, was misled — it accounts
for Gemini's verdict-word regression from MINOR REVISIONS to MAJOR REVISIONS,
a concrete instance of the directive-H-refined rationale for not treating
verdict words as the gate. The ≥300-DPI protocol stays.

**Re-flags (9, all source-cited).** Grok E3 + Gemini M2 (not self-contained)
→ the R1→R10 chain closed by App. D (v1C.0.4) and App. E (v1C.0.9), and
falsified again this round by the opposing leg's 30 recomputations *from the
PDF alone*; Grok E1 (61–67 orders not derived) → closed at R3, and the leg
reproduced both endpoints from the printed inputs; Grok E2 (abstract
overstates the spanning list) → the calibrated statement is already in the
same abstract sentence, with the one genuine residue closed as GNR-11;
Grok E4 (eight entries are general arguments) → the Fig. 1 caption already
says five entries are, and names them; Grok M1 (≤12 pp) → the R1→R10-GNR-15
chain, where real condensation was applied; Grok M2 (Fig. 1 implies tighter
dependence) → closed at R10-GNR-1, which is the edit in the PDF Grok
reviewed; Grok M3 (α/M is an external fit) → the paper's own headline
conclusion, stated twice; Grok N1 (qualify "the companion paper" everywhere)
→ would reverse the R10-GNR-12 consolidation this reviewer requested one
round ago; Grok N2 ("none a logical consequence of another" is redundant) →
declined with reason, that clause is the independence claim licensing the
count of fourteen.

**Deferred-genuine (carried, not closed):** the frozen-release Zenodo DOI for
this survey's own verification scripts (Gemini E1), unchanged from R10-DEF-1.
Real requirement, already disclosed in the paper as planned; DOI minting is
P-round packaging work requiring Houston.

**Self-withdrawn by the reviewing leg: none this round.** Unlike R8, R9 and
R10 — each of which produced at least one low-DPI false positive the leg
raised and self-withdrew — the R11 Claude leg's 300-DPI-first method produced
no withdrawn candidates. The artifact family fired instead on the Gemini leg,
which has no equivalent re-render step.

**NEW STANDING ANTI-REGRESSION GUARD — `tools/p1c_consistency_check.py`.**
A stdlib-only mechanical self-consistency linter for `main.tex`, written
because three of this round's four MAJORs are the residue of the previous
round's closure sweep and all are mechanically detectable. Four rules:
**(A)** every asserted catalog-size claim agrees with every other and with
the actual count of `\textbf{B<n> ---}` entries; **(B)** prose Tier-(I) count
assertions ("sole" / "the only" / "exactly one" / "two") equal the counted
`\textbf{(I)}` markers inside the `tab:evidentiary_status` body; **(C)** an
extensible assert/disclaim paired-phrase list fails when a sentence asserts
something a companion sentence explicitly disclaims (seeded with
`nda_covers_eq1`, `nda_operator_label`, `route2_de_nda`); **(D)** a universal
per-entry closure claim fails when any catalog entry declares itself a
non-closure. LaTeX comments are stripped first, so the `%` changelog header
cannot produce false positives. **Proof it works, recorded as evidence:**
run against the pristine v1C.0.13 source it exits **1** and fires Rules B, C
and D — i.e. it independently rediscovers MAJOR-1, MAJOR-2 and MAJOR-3 with
no reviewer in the loop — while Rule A correctly passes. Against v1C.0.14 it
exits **0**, 4/4 rules PASS. Deliberately **not** a git hook: documented in
`ops/RUNBOOK.md` and in its own SKILL-style module docstring as the check to
run before every P1C version bump and round-closure commit; covered by
`tools/tests/test_p1c_consistency_check.py` (16 tests). **The generalizable
lesson for the loop: "grep every instance and reconcile" silently
under-performs, and its failures stay invisible until the next round's
referee finds them. Where a claim-scoping closure touches N surfaces, the
durable fix is a checker that counts them, not a more careful sweep.**

v1C.0.14: **24 pp, 0 errors / 0 undef / 0 overfull** (41 underfull,
badness-only), `/latex-audit` **PASS** (pages 1, 5, 10, 12, 21, 22 rendered
and visually confirmed; all 6 `\artifact{}` paths resolve; no "(Dated:)"
remnant; Table II placed cleanly at the top of p.12 with exactly one bold
**(I)**), linter **4/4 PASS**, mirrors byte-identical across
`site/public/papers/`, `public/papers/` and `site/out/papers/` (md5
`fa485e592afe602d7258f17606e3278a`, SHA-256 `9dd5c70862d3cad1…`),
`npx next build` passes. **A float regression was caught and fixed inside the
round:** the first v1C.0.14 compile produced "Float too large for page" and
"A float is stuck" warnings absent from v1C.0.13 (confirmed new by compiling
pristine v1C.0.13 from `git show HEAD:` in a clean directory), caused by the
MAJOR-1 regrade lengthening Table II's R2 cell; fixed by condensing the cell
and setting `[!tb]` placement. **Page count 23 → 24 pp**, because four
claim-scoping closures required new text — reported, not smoothed over.
Grok's ~10–12 pp target remains unmet and unreachable without deleting
catalog content.

**Convergence read (directive H-refined + the R8 classification rule): R11
surfaced 14 genuinely-new-real findings against a target of 0, of which 6
are correctness-grade. The correctness-convergence gate is NOT met, so
THE R-PHASE IS NOT CONVERGED AT R11.** Three things are worth recording
honestly. (1) **Two consecutive rounds with zero computational errors**, and
R11 quantified it: 30 independent recomputations, one rounding slip. The
arithmetic spine has now been checked from the PDF alone, twice, by an
adversarial leg. (2) **The remaining defects have changed kind** — R1–R9
produced wrong numbers, coefficients and identity chains; R10 and R11 produce
disagreements between two places in the same document. That is the failure
mode of a manuscript revised repeatedly under pressure, not of one whose
physics is unsettled. (3) **Three of R11's four MAJORs were created by R10's
closure**, which is the signal that drove the linter: a closure touching six
surfaces and landing on five is indistinguishable, to the closing agent, from
one that lands on six — only a counter can tell them apart. Against that, R11
moved two claims *down*: Route 2's dark-energy leg is now Tier-II in both
branches, and the abstract no longer claims every entry closes a route. Both
reductions were required by the paper's own definitions and entries.
**R12 on the exact v1C.0.14 PDF is the next correctness-convergence check**,
all active legs re-run fresh (Claude INT + Grok API + Gemini API per
directives N/M-AMENDED; Perplexity optional), exit test = **zero
correctness-grade genuinely-new-real findings**, and it is the first round
that will run against a manuscript with a mechanical self-consistency gate in
front of it. Residual presentation-grade items route to the D-round. GNR
count trend: 15 → 7 → 8 → 10 → 6 → 9 → 7 → 4 → 16 → 15 → **14** (6
correctness-grade). No readiness score has been computed and no venue/Zenodo
kit exists for this draft.

Prior-round record follows.

**Status at R10 (superseded): R10 CORRECTNESS-CONVERGENCE BOARD RUN AND TRUTH-AUDITED →
15 GENUINELY-NEW-REAL FINDINGS CLOSED (v1C.0.13): 5 CORRECTNESS-GRADE +
10 PRESENTATION-GRADE. ZERO COMPUTATIONAL ERRORS FOUND BY ANY LEG — a
first for this paper. BOTH MAJORS WERE CLAIM-SCOPING DEFECTS AND ARE
CLOSED BY SCOPING, NEVER BY WEAKENING THE SCIENCE OR FABRICATING
COVERAGE. R-PHASE NOT CONVERGED AT R10 — R11 on the exact v1C.0.13 PDF
is REQUIRED and is the next CORRECTNESS-CONVERGENCE CHECK.**
The R10 board ran on the exact v1C.0.12 PDF (sha `c21fde9f…`), three legs
with raw receipts.

**R10 verdict matrix (2026-08-07, exact v1C.0.12 PDF):**

| Leg | Model | Verdict |
|---|---|---|
| Claude INT (Opus-tier) | claude opus | **MAJOR REVISION** (2 MAJOR / 7 MINOR; leg self-classes 5 correctness-grade) — but with **ZERO computational errors** across Eqs. (1)–(5), (9)–(11), (A1)–(A4), (C1)–(C2), (E1)–(E5), Tables II/III and the B1/B12/App. A/App. E numerics, independently re-derived; both MAJORs are claim-scoping, not math |
| Grok API | grok-4.3 | **REJECT** (4 ESSENTIAL / 5 MAJOR / 4 NIT) — complaints are scope, length and style, not computation |
| Gemini API | gemini-3.1-pro-preview | **MINOR REVISIONS** (1 ESSENTIAL / 1 MAJOR / 1 MINOR / 1 NIT; pass-2 NO ADDITIONAL FINDINGS) — **the first sub-major verdict this paper has received across R1–R10** |
| Perplexity | (optional leg) | FAILED — failure record, never a verdict |

The verdict-first truth audit against the R1–R9 disposition ledgers and the
operator-basis adjudication
(`project-context/peer-reviews/INT_v3/ROUND_2026-08-07-P1C-v1C.0.12-EXACTPDF-c21fde9f-R10CONV/P1C_v1C.0.12_R10_truth_audit.md`)
deduplicated the board to **21 canonical items: 15 genuinely-new-real (all
closed in v1C.0.13), 4 re-flags of R1–R9-dispositioned content, 1 freshly
falsified with receipts, 1 deferred-genuine.**

**GNR by grade (all 15 closed in v1C.0.13):**

- **Correctness-grade (5)** — R10-GNR-1 (B14 Tier-I scope + headline
  recount), R10-GNR-2 (Route-2 dimension basis), R10-GNR-3 (β(γ)
  suppression claim), R10-GNR-4 (Mercuri RG citation), R10-GNR-5 (B9 route
  tag). This matches the reviewing leg's own self-classification exactly.
- **Presentation-grade (10)** — R10-GNR-6 … R10-GNR-15.

**MAJOR-1 — B14's Tier-I claim was asserted outside the branch App. D
proves; the headline count depended on it.** App. D's statement is scoped to
*canonical scalar matter* and its exclusion list rules out *fermion sources*;
proof step (1) is "A canonical scalar field has zero spin density". B8 is a
statement about the **fermionic** `(J⁵)²` sector, where `T = κS ≠ 0` and
App. D's hypotheses fail — so B14 could not "independently confirm" or
subsume B8, and its `[R1–R4]` tag over-reached (R1 is the fermionic NJL
channel). Not a re-flag: R1's `FAL-1` and its R2/R3/R8/R9 re-flags all
concerned whether the 13/14 accounting was *internally consistent* (it was);
R10 asks whether the subsumption is *logically valid* (it is not).
**Closure:** B14's tag narrowed `[R1–R4]` → `[R2–R4, zero-spin branch]` with
the honest content stated (it removes those routes' *classical zero-spin*
perturbative baseline, not their quantum or fermionic content); B8 restored
as an independent constraint; **the headline count RECOUNTED 13 → 14
distinct mechanism-class constraints at every instance** — abstract,
introduction, Sec. III preamble, Fig. 1 caption, the **in-figure edge label**
`B8, B14` → `B8` on the H→R1 arrow, Table I caption (rewritten to
"disjoint matter branches, therefore logically independent"), App. A,
Sec. VI, Sec. VII; Tier-I status branch-scoped in five places including
App. D's own consequences paragraph. Grep-verified: `13 distinct`,
`thirteen`, `subsumed by B14`, `subsumes B8` all return nothing in
`main.tex`. This also resolves Grok N2's "14 entries (13 distinct)" wording
inconsistency.

**MAJOR-2 — Route 2's dark-energy closure was delegated to an operator list
that excludes the operator in question.** Eq. (1) is a **dimension-5**
operator (the paper itself prints "the dimension-(+5) integrand
`∂_μϑ_NY J^{5μ}` times the dimension-(−1) prefactor `β(γ)/M_Pl`"), built on
a pseudoscalar `ϑ_NY` that is **not** among Sec. V's admitted building
blocks, and carrying an **extra derivative** the zero-derivative rule
excludes — three independent reasons it lies outside the dimension-4 list.
Worse, its assigned background `⟨∂_μϑ_NY⟩ ∼ H₀²` makes `ϑ_NY` precisely the
"new light scale `μ ≪ M_Pl`" that App. A's *Residual assumption* names as
able to **evade** the single-scale NDA bound: the delegation pointed the
wrong way. Not a re-flag: R9's `GNR-4` fixed a bridge sentence that
mis-*identified* Eq. (1) within the list; R10 shows it is not in the list at
all. **Closure — extracted faithfully, not invented.** The in-scope argument
exists in the frozen monolith this paper is an extraction of
(`arxiv/paper1_unified.tex` §`sec:jackiwpi_cs`: "total derivative for
constant `ϑ` (Tier-I, operator-level); R4-class naturalness closure for any
dynamical `ϑ` (Tier-II), reinforced by Barrier 7"). The false delegation and
the defending parenthetical are deleted; a new Sec. IV A passage states the
three exclusion reasons, states "We therefore do not claim the NDA bound
covers it", and splits the leg: **(i) constant coefficient (minimal ECH)** —
γ and hence the Nieh–Yan coefficient are constants fixed by the LQG area
spectrum (B7), `∂_μϑ_NY = 0`, the operator vanishes, and the surviving
Holst/Nieh–Yan content is O1/O2, exact total derivatives → **Tier-I, inside
the list**; **(ii) dynamical coefficient** — a non-minimal
dynamical-Immirzi completion, R4 in gravitational costume, closed only at
the naturalness / explanatory-deficit level → **Tier-II**. Propagated to
Sec. IV head, Table II's R2 row, the tiered-closure paragraph, Sec. VI and
Sec. VII, whose "all four enumerated channels close" sentence is now
re-scoped by closure mode.
**Route 2's dark-energy strength was REDUCED, and the paper says so:** "No
dark-energy amplitude is computed for Route 2 anywhere in this survey, and
none is claimed."

**Other correctness closures:** the β(γ) "each of which could only suppress
the estimate further" claim corrected to the net effect (≈1.5 orders,
dropped as a *pair*; the `1/16π²` supplies −2.2 orders against β(γ)'s +0.5)
— no downstream number moves, the ≥58-order margin is unaffected
(R10-GNR-3); Mercuri [8] dropped from the "analyzed via
renormalization-group methods" citation and moved to an explicit
classical-structure clause (R10-GNR-4); B9's `[R2]` tag motivated as a
vacuum-*selection* constraint rather than an amplitude bound, and explicitly
stated not to be one (R10-GNR-5).

**Presentation closures:** remaining `{O1–O6}` "basis" → "spanning list" at
the four sites named (Fierz-sector "basis" left alone — that set genuinely
*is* a basis); tautological `𝒟_inf` parenthetical; Sec. II now states
`η = diag(−,+,+,+)` and `ε^{0123} = +1` outright with the contraction
identity they fix; abstract's parity-odd label qualified; **version/date
stamp removed from the printed title block** (Grok E1/N1 — no `\date` is
issued at all, since an empty `\date{}` still renders "(Dated:)"; provenance
moved to `pdfkeywords`, verified `Keywords: v1C.0.13 (August 7, 2026)`);
β(γ) defined at first use (Grok N3); defensive "companion does not retain"
phrasing consolidated to one statement in Sec. I (Grok N4); Gemini's
version-history prose removed; R4 standalone-reader gap closed by stating
its two checkable steps in-text and re-scoping the rest explicitly.

**Directive-G note (recorded, not hidden):** for this paper only, directive
G's page-1 verification ("page 1 shows new version+date") is replaced by
PDF-metadata verification, because a journal referee must not see a
version-control string in the title block. `\paperVersion` and
`\paperTimestamp` are still bumped in the `.tex` exactly as directive G
requires.

**Length (Grok M5) — real condensation applied, and the outcome reported
honestly.** Seven redundant passages were condensed (companion-relation
block, two spanning-assertion restatements, the Sec. IV head preamble, three
consecutive restatements of the same Route-2 birefringence conclusion, the
Sec. V "To clarify the mass-dimension bookkeeping" sentence, the Sec. VI
stress-test restatement, and App. A 1's duplicate redundancy statement). **No
barrier entry, table row, equation, derivation, appendix or citation was
deleted.** Net page count **22 → 23 pp**: the condensation recovered roughly
a page and the MAJOR-2 closure spent slightly more than that on required new
content. Grok's ~10–12 pp target is not met and is not reachable without
deleting catalog content, which would be dishonest scoping.

**Falsified with receipts.** Gemini NIT 4 ("Ref. [13] carries a
simulated/placeholder arXiv ID") is **FALSIFIED**: `arXiv:2509.13654` is the
real ACT DR6 record (Diego-Palazuelos & Komatsu), verified against the live
arXiv listing during R7 — title, authors, `0.215° ± 0.074°` and `2.9σ` all
matched exactly. The same "2026 dates are anachronistic" inference was made
and falsified at R6.

**Deferred-genuine (carried, not closed):** the frozen-release Zenodo DOI for
this survey's own verification scripts (Gemini MAJOR 2). Real requirement,
already disclosed in the paper as planned; DOI minting is P-round packaging
work requiring Houston.

**Self-withdrawn by the reviewing leg** (recorded so the board can
distinguish "checked and clean" from "not checked"; never counted): four
candidate findings raised from low-DPI text extraction and withdrawn after
re-rendering at 300–400 DPI — the missing `√3` in `ρ_crit`, `|t₃|` vs
`√|t₃| ∼ m_T⁻¹`, `−(8/3)κ²` vs the printed `−(3/8)κ²`, and an apparent
`ε_{0123}` / `ε^{0123}` clash. None is a defect. Third consecutive round
(R8/R9/R10) in which a rasterization artifact produced a candidate finding;
the ≥300-DPI accuracy protocol stays.

v1C.0.13: **23 pp, 0 errors / 0 undef / 0 overfull**, `/latex-audit` **PASS**
(pages 1, 5, 8, 9, 12, 19 rendered at 110 DPI and visually confirmed; all 6
`\artifact{}` paths resolve; no "(Dated:)" remnant), mirrors byte-identical
across `site/public/papers/`, `public/papers/` and `site/out/papers/` (md5
`c5957263410453ba7b3fb96a0678138d`, SHA-256 `d3aea74da62a433c…`),
`npx next build` passes.

**Convergence read (directive H-refined + the R8 classification rule): R10
surfaced 15 genuinely-new-real findings against a target of 0, of which 5
are correctness-grade. The correctness-convergence gate is NOT met, so
THE R-PHASE IS NOT CONVERGED AT R10.** Two signals are nonetheless worth
recording, both firsts for this paper: (1) **zero computational errors** —
for the first time across R1–R10 no leg found a wrong number, coefficient or
identity chain, and the reviewing leg said so explicitly after re-deriving
the quantitative spine independently; (2) **Gemini returned MINOR
REVISIONS**, the first sub-major verdict. Against that, R10's two MAJORs are
the kind of defect that only surfaces once the arithmetic is clean:
over-reaching *claims* rather than wrong *computations*. Closing them
narrowed one Tier-I claim and reduced one route's asserted closure strength
— the honest direction of travel. **R11 on the exact v1C.0.13 PDF is the
next correctness-convergence check**, all active legs re-run fresh (Claude
INT + Grok API + Gemini API per directives N/M-AMENDED; Perplexity
optional), exit test = **zero correctness-grade genuinely-new-real
findings**. Residual presentation-grade items route to the D-round. GNR
count trend: 15 → 7 → 8 → 10 → 6 → 9 → 7 → 4 → 16 → **15** (5
correctness-grade, down from 10).


**Status at R9 (superseded): R9 CORRECTNESS-CONVERGENCE BOARD RUN AND TRUTH-AUDITED, WITH AN
INDEPENDENT SYMBOLIC ADJUDICATION → 16 GENUINELY-NEW-REAL FINDINGS CLOSED
(v1C.0.12): 10 CORRECTNESS-GRADE + 6 PRESENTATION-GRADE. R-PHASE NOT
CONVERGED AT R9 — a STRUCTURAL correctness item was found and fixed, so
R10 on the exact v1C.0.12 PDF is REQUIRED and is the next
CORRECTNESS-CONVERGENCE CHECK.**
The R9 board ran on the exact v1C.0.11 PDF (sha `0868856032…`), three legs
with raw receipts, plus a referred-out symbolic computation.

**R9 verdict matrix (2026-08-07, exact v1C.0.11 PDF):**

| Leg | Model | Verdict |
|---|---|---|
| Claude INT (Opus-tier) | claude opus | **MAJOR REVISION** (4 MAJOR / 11 MINOR; leg self-classes 8 of 15 correctness-grade) — ~20-item verification log independently re-derived the Route-2 contractions, the Eq. (4) integration, the Route-3 endpoints, the App. A hierarchy chain, the App. C Fierz matrix, the App. E benchmark chain, and all 25 bibliography entries, with zero numeric or citation errors |
| Grok API | grok-4.3 | **REJECT** (3 ESSENTIAL / 3 MAJOR / 2 NIT + pass-2: 3 MAJOR / 1 MINOR) |
| Gemini API | gemini-3.1-pro-preview | **MAJOR REVISIONS** (1 ESSENTIAL / 2 MAJOR / 2 MINOR / 1 NIT) |
| Perplexity | (optional leg) | FAILED — failure record, never a verdict |

**The adjudication (what made this round different).** Claude's MAJOR-1
(`{O1–O6}` is linearly dependent) and MAJOR-2 (Table III's O1 row is
internally contradictory) are claims about the *mathematics* of Sec. V and
could not be dispositioned by re-reading the paper — the released script
verifies Checks A and D only and computes no rank. Adjudicating them by
re-arranging the paper's own quoted identities would have been pattern-036
territory. They were referred out to an **independent symbolic computation**,
committed at `1130b7c5` *before* any closure edit:
`research/theory_audit/operator_basis_adjudication_2026_08_07.{py,json,md}`
— O1–O6 re-derived from the Cartan structure equations on an algebraically
independent 2-jet, expanded over 1368 jet monomials, reduced in exact
rational arithmetic. Headline verdict **PARTIALLY-CORRECT**. Every v1C.0.12
edit to Sec. V / Table III / App. A 1 is cited to a specific `[L##]` tag of
that run's JSON log; no result is restated in the paper that the computation
did not produce.

The verdict-first truth audit against the R1–R8 disposition ledgers
(`project-context/peer-reviews/INT_v3/ROUND_2026-08-07-P1C-v1C.0.11-EXACTPDF-08688560-R9CONV/P1C_v1C.0.11_R9_truth_audit.md`)
deduplicated the board to **33 canonical items: 16 genuinely-new-real
(14 referee-originated + 2 adjudication-originated, all closed in v1C.0.12),
11 re-flags of R1–R8-dispositioned content (five with partial
falsifications), 4 freshly falsified with receipts, 1 scope-opinion
deferred, 1 opinion dispositioned.**

**GNR by grade (all 16 closed in v1C.0.12; zero margin, count, or headline
changes):**

- **Correctness-grade (10)** — R9-GNR-1, 2, 3, 4, 6, 8, 10, 12 and
  R9-ADJ-1, R9-ADJ-2.
- **Presentation-grade (6)** — R9-GNR-5, 7, 9, 11, 13, 14. Closed in-round
  rather than deferred, because each was a one-line edit adjacent to a
  correctness edit already being made.

**The three adjudication-driven changes:**

1. **R9-GNR-1 [C] — Sec. V re-framed: `{O1–O6}` is a SPANNING / GENERATING
   list, not a basis.** Computed rank **4**, nullity **2** `[L28]`/`[L29]`
   (Gram certificate `[L34]`, independent numeric evaluation matrix `[L58]`);
   rank **2 modulo total derivatives** `[L40]`. Both exact relations are now
   stated in the paper: `O1 − O6 = 0` `[L31]`/`[L59]` (certified by an
   independent Γ-route Riemann construction, all 256 components, three
   configurations `[L49]`–`[L57]`) and `2·O1 + 2·O2 − O4 = 0`, equivalently
   `O1 = ½O4 − O2` `[L30]`/`[L62]`/`[L63]`. The referee's literal
   `O1 = O4 − O2` is **wrong by a factor 2 on O4** `[L60]`/`[L61]` — caused
   by the paper never fixing the NY form-vs-density normalization `[L66]`,
   now fixed explicitly as `NY ≡ ∂_μ(ε^{μνρσ}e_{Iν}T^I_{ρσ})`. The
   completeness argument is re-worded to exactly what the computation
   supports: the list **spans** the rule-admitted space; independence is not
   claimed. Rank is 4 under both admissible O6 readings `[L104]`–`[L106]`.
2. **R9-ADJ-1 [C] — Table III O1 row: `Final = 0` STAYS; the reason becomes
   branch-scoped.** Check A reproduced `[L70]`, but it uses the
   **torsion-free** first Bianchi identity, which `T = κS ≠ 0` violates
   `[L71]`; O1 is not pointwise zero on shell `[L91]`/`[L92]`. Row now reads
   `0 at T=0 (Bianchi, Check A); −NY at T=κS` → `0 (EOM)`; O6 mirrors it;
   the abstract's trichotomy is scoped to match.
3. **R9-ADJ-2 [C] — NEW correctness item found by the adjudication, raised
   by neither party: Table III's O4 row, its caption, and the App. A 1
   `O4^[4] = O5^[4]` chain were wrong as printed.** `O4 ≡ 0` on shell
   `[L78]`/`[L81]`, confirmed in a genuine curved on-shell Einstein–Cartan
   configuration `[L90]`/`[L94]`: `T_I∧T^I` is supported only by the
   non-axial torsion irreps `[L82]`–`[L86]` and minimal Cartan torsion is
   verified pure axial `[L09]`. Root cause: **Check D's identity concerns the
   ε-free square `T_abc T^abc`** `[L87]`, a different invariant from the
   ε-contracted O4 of Eq. (8) `[L86]`; the paper applied it to the wrong
   contraction. All five affected sites corrected (row, caption, App. A 1
   chain, Check D prose, Sec. V bullet (b)), plus the downstream class
   statements. **This STRENGTHENS the no-go** — an operator contributing
   nothing at all is a stronger disposal than one contributing a
   Planck-suppressed contact term `[L89]` — and the physics conclusion is
   unchanged.

**Other correctness closures:** Route-3's "61–67 orders" now has a displayed
mass-dimension scaling relation with the reference budget defined as
`ρ_Λ,obs` and labelled Tier-III (R9-GNR-3), and the Hubble symbol is `H0`
uniformly with the reason stated (R9-GNR-2); the App.-A bridge no longer
mis-describes Eq. (1) as the dimension-(+1) operator, and Sec. IV now states
once that Sec. IV A closes the *birefringence* channel while Route 2's
dark-energy closure is inherited from Sec. V / App. A (R9-GNR-4); "natural
coefficient ∼ M_Pl⁴" → "natural *density* scale" at three sites (R9-GNR-6);
Eq. (3)'s false structural-consistency claim withdrawn in favour of the
numerical bound (R9-GNR-8); App. D Step 4's dropped Holst `γ⁻¹` restored
(R9-GNR-10); B11/B13/B4 logical independence now argued rather than asserted,
keeping the count at 13 (R9-GNR-12).

**Falsifications with receipts.** Claude MAJOR-2's "internal contradiction"
is **FALSIFIED** `[L98]`/`[L99]`: with `O4 = 0`, Nieh–Yan gives `O1 = −O2`
exactly `[L95]`/`[L97]`, an exact total derivative → 0 EOM / 0 vacuum
energy, so `Final = 0` survives — the referee named the right row for the
wrong reason, and the fix he requested would have introduced a new error.
Grok C1 (Eq. (2) "over-suppressed by one M_Pl") falsified — the LHS is a
double normalization stated in the following three lines, and both displayed
lines were independently verified consistent. Grok N2 (Eq. (2) typesetting
slip) falsified — `10⁻⁶⁴/6×10⁻⁵ = 1.67×10⁻⁶⁰`, correct as printed. Grok J1
("3.6 vs 3.9×10⁻⁶⁹ never reconciled") falsified — reconciled explicitly in
two printed places. Gemini N1 ("gauge-invariaut") falsified as a text-
extraction artifact; `pdftotext` on p. 10 returns "gauge-invariant" — the
**fifth** such artifact in the R3/R5/R7/R8 series.

**Self-withdrawn by the reviewing leg before filing** (recorded so the board
can distinguish "checked and clean" from "not checked"; never counted): the
B1 torsion-coupling exponent (260-DPI re-render shows `√|t3| ∼ m_T⁻¹`,
correct as printed) and the Fig. 1 barrier→route arrow counts (400 DPI gives
R1=3, R2=4, R3=4, R4=3 = 14, matching Sec. III A exactly).

v1C.0.12: 22 pp, 0 errors / 0 undef / 0 overfull, `/latex-audit` visual pass
on pages 1, 9, 13, 15, 18, all 6 `\artifact{}` paths resolving, immutable pin
advanced `c80b7487b01f` → `1130b7c5e3d2`, mirrors byte-identical (md5
`0323f962…`, SHA-256 `c21fde9f1b…`), `npx next build` passes.

**Convergence read (directive H-refined + the R8 classification rule): R9
surfaced 16 genuinely-new-real findings against a target of 0, of which 10
are correctness-grade. Neither the literal 0-GNR gate nor the
correctness-convergence gate is met, so the paper is NOT converged and
THE R-PHASE IS NOT CONVERGED AT R9.** R8 closed with 2 correctness-grade
GNR and named R9 the correctness-convergence check; R9 returned 10,
including a **structural item (R9-ADJ-2) that had survived nine boards,
three referee legs per board, and the paper's own released verification
script** — found only because two referee claims were referred out to an
independent symbolic computation instead of being adjudicated from the
paper's prose. That is the round's process lesson: a claim about the paper's
mathematics cannot be dispositioned from the paper's own prose. **R10 on the
exact v1C.0.12 PDF is the next correctness-convergence check**, all active
legs re-run fresh (Claude INT + Grok API + Gemini API per directives
N/M-AMENDED; Perplexity optional), exit test = **zero correctness-grade
genuinely-new-real findings, counting adjudication-originated items exactly
as referee-originated ones**. Residual presentation-grade items route to the
D-round. GNR count trend: 15 → 7 → 8 → 10 → 6 → 9 → 7 → 4 → **16**; the
jump is a measurement improvement, not a regression — the paper did not get
worse, the instrument got sharper.

Prior-round record follows.

**Status at R8 (superseded): R8 CONFIRMATION BOARD RUN AND TRUTH-AUDITED →
4 GENUINELY-NEW-REAL FINDINGS CLOSED (v1C.0.11): 2 CORRECTNESS-GRADE +
2 PRESENTATION-GRADE under the classification rule introduced that round.**
The R8 confirmation board ran on the exact v1C.0.10 PDF (sha `d8b9db8e…`),
three legs with raw receipts.

**Classification rule (NEW at R8 — orchestrator decision, recorded verbatim
in the audit doc):** "every GNR item is classed CORRECTNESS-GRADE (wrong
math/number/attribution/claim) or PRESENTATION-GRADE (length, repetition,
layout, style). R-phase convergence = a full board with ZERO
correctness-grade GNR; presentation-grade items route conceptually to the
D-round stage. Integrity unchanged: every finding dispositioned with
citations."

**R8 verdict matrix (2026-08-07, exact v1C.0.10 PDF):**

| Leg | Model | Verdict |
|---|---|---|
| Claude INT (Opus-tier) | claude opus | **MINOR REVISIONS** (0 MAJOR / 7 MINOR) — 18-item verification log independently recomputed EVERY checkable displayed equation and numeric (both Route-2 contractions; the full BS integration; Route-3 endpoints; the complete App. E chain E1–E5; the Fierz matrix; the App. D proof chain; B12 window; App. A hierarchy/e-folds; counts; significances; citation integrity) — zero numeric errors found |
| Grok API | grok-4.3 | **REJECT** |
| Gemini API | gemini-3.1-pro-preview | **MAJOR REVISIONS** |
| Perplexity | (optional leg) | FAILED — failure record, never a verdict |

The verdict-first truth audit against the R1–R7 disposition ledgers
(`project-context/peer-reviews/INT_v3/ROUND_2026-08-07-P1C-v1C.0.10-EXACTPDF-d8b9db8e-R8CONF/P1C_v1C.0.10_R8_truth_audit.md`)
deduplicated the board to **20 canonical items: 4 genuinely-new-real
(closed in v1C.0.11), 12 re-flags of R1–R7-dispositioned content (four with
partial falsifications, one re-falsified), 4 freshly falsified with
receipts.**

**GNR by grade (all closed in v1C.0.11; zero margin, count, or headline
changes):**

- **Correctness-grade (2):** (1) the Benedetti–Speziale citation pointer
  harmonized — the same flow was credited to the JHEP paper [9] a few
  lines before the "(their Eq. 7)" pointer bound to the proceedings [3];
  the credit line now names the proceedings as the source of the equation
  numbering, companion to the full JHEP analysis (Claude m2). (2) B12's
  SU(2) black-hole-entropy value γ ≈ 0.274 now cites the primary
  Ghosh–Mitra state-counting — Phys. Lett. B 616, 114 (2005),
  gr-qc/0411035, **Crossref-verified before the bib entry was added** —
  alongside the companion, so the scheme-dependence claim is externally
  checkable (Claude m7).
- **Presentation-grade (2):** (3) the Eq. (3) integration relabeled
  Δln γ (the equation is linear in γ), with the identification
  Δγ/γ ≃ Δln γ stated and the exponentiated band (0.29–0.36) noted
  immaterial at the ≳60-order margins (Claude m3). (4) the App. A
  hierarchy quotient prints 1.2209×10¹⁹ GeV, matching the quoted
  8.7×10¹²² exactly (1.22 exactly gives 8.6×10¹²²; Claude m6).

**The round's headline falsification:** Claude MINOR-1 — the claim that
the printed |Ω₄₄/α₄| carries a spurious (1+γ²)² power contradicting the
paper's own ≈3.3 numeric — was **FALSIFIED against the exact artifact**:
the 200-DPI render of p. 6 shows the printed form is
(378+783γ²)/[120(1+γ²)], the correct one-power form; recomputation gives
3.33 at γ = 0.24 (printed "≈3.3" ✓) and infimum 378/120 (printed bound ✓)
— the reviewer's own "correct form" is what the paper prints (probable
misread of the adjacent Ω₄₄ definition, which legitimately carries the
squared denominator). The orchestrator's dispatch had pre-classed this
correctness-grade GNR "verify by recomputation, fix"; the verification
was performed and the truth-audit verdict controls — no edit owed, none
made. Also falsified with receipts: Grok M2 (the numerical targets
0.342°±0.094°, 0.215°±0.074°, (2.25 meV)⁴, H₀/M_Pl ≈ 1.2×10⁻⁶¹ are all
printed and propagated in-body), Grok m3 (the c80b7487b01f pin on p. 13
covers all four scripts including the Fierz-adjudication script), and
Gemini N1 (the "filename spaces" are a pdftotext extraction artifact —
the render shows underscores at every site; fourth
extraction-artifact falsification in the series after R3/R5/R7).
Re-flags: version stamp (directive G; Grok E1 + Gemini M1),
headline-recompute/standalone/absorb-or-withdraw family (Grok E2/E3/n1;
Tier-I half re-falsified against the compiled App. D), abstract-vs-tier
rhetoric (Grok E4/M4), the 13-distinct count (Grok E5 — partially
falsified: abstract, Table I caption, and Sec. III all print the
B8-subsumed disclosure and disclaim a thirteen-separately-decisive
reading), enumeration demand (Grok M1 — the downgraded framing IS the
existing text), M_Pl-convention conversions (Grok M3 — displayed at both
import sites), B9 table flag + caption-clause duplication (Grok m1/n2 —
Table-II taxonomy disposition; the requested main-text statement already
exists in Sec. IV), loop-factor justification (Grok m2 — grounded in ST
Eq. 46, printed), **Route-4 companion dependency (Gemini E1 — RE-FLAG of
the R6-GNR-1/R7-RF-9 deferred-genuine disposition behind the
refereed-companion gate; coverage verified per orchestrator request)**,
**mint-the-DOI-now (Gemini E2 — RE-FLAG of R5-GNR-2/R6-RF-9/R7-RF-8;
external Houston-gated side effect executed at P-round packaging;
coverage verified)**, and abstract length + tier-disclaimer repetition
(Claude m4/m5 — the R7-RF-11 family, now explicitly routed to the
D-round as presentation-grade). v1C.0.11: 20 pp, 0 errors / 0 undef /
0 overfull, visual audit pass on changed pages (1, 5, 8, 15), mirrors
byte-identical (md5 `4723faef…`, SHA-256 `0868856032…`).
**Convergence read (directive H-refined + R8 classification): R8
surfaced 4 genuinely-new-real findings against a target of 0, so the
paper is NOT converged. R9 on the exact v1C.0.11 PDF (sha `0868856032…`)
IS the correctness-convergence check: a full board whose truth audit
yields ZERO correctness-grade GNR converges the R-phase, with residual
presentation-grade items routed to the D-round per the classification
rule. Both of R8's correctness-grade items were citation-precision
fixes, not physics corrections; the board's sharpest correctness claims
were all falsified with receipts; the GNR count is trending
15 → 7 → 8 → 10 → 6 → 9 → 7 → 4.**
Prior-round record follows. The R7 confirmation board ran on
the exact v1C.0.9 PDF (sha `b4d73f94…`), three legs with raw receipts.

**R7 verdict matrix (2026-08-06, exact v1C.0.9 PDF, round dir label 2026-08-07):**

| Leg | Model | Verdict |
|---|---|---|
| Claude INT (Opus-tier) | claude opus | **MINOR REVISIONS** (0 MAJOR / 8 MINOR) — 15-item verification log independently recomputed EVERY displayed equation and numeric (both Route-2 contractions; the full BS flow integration to 1.38×10⁻⁶; the ST ratio; B12 endpoints; the App. A hierarchy/e-fold chain; the Fierz involution by direct multiplication; the complete App. E chain E1–E5; counts; significances; citation spot-checks) — zero numeric errors found |
| Grok API | grok-4.3 | **REJECT** |
| Gemini API | gemini-3.1-pro-preview | **MAJOR REVISIONS** |
| Perplexity | (optional leg) | FAILED — failure record, never a verdict |

The verdict-first truth audit against the R1–R6 disposition ledgers
(`project-context/peer-reviews/INT_v3/ROUND_2026-08-07-P1C-v1C.0.9-EXACTPDF-b4d73f94-R7CONF/P1C_v1C.0.9_R7_truth_audit.md`)
deduplicated the board to **21 canonical items: 7 genuinely-new-real
(closed in v1C.0.10), 13 re-flags of R1–R6-dispositioned content (two with
partial falsifications — the two load-bearing Tier-II inputs Grok demands
are in App. E of the very PDF under review, and the R4 anchor's algebraic
origin has been in-paper since v1C.0.6; one re-falsified — the Tier-I
standalone claim, disproved against the compiled App. D proof; one closed
by verification — the ACT DR6 citation checked against the live arXiv
record: title, authors, 0.215°±0.074°, 2.9σ, exact match), 1 freshly
falsified with receipts** (Gemini N2's "space before the colon" in App. A —
the tex has no space and the 300-DPI render shows only the standard italic
correction; pdftotext inserts the spurious space at the italic-to-upright
transition, the same extraction-artifact family as the R3/R5
stacked-fraction misreads). All 7 closures are wording/notation/
presentation-grade; **zero numeric, margin, count, or headline changes**:
(1) the B1 tuning ratio was literally INVERTED — δm_T²/m_T² with radiative
δm_T² ∼ M_Pl² and m_T ∼ H₀ evaluates to 10⁺¹²², not 10⁻¹²² (inherited
verbatim from the frozen monolith line 3714) — now stated as a
cancellation to one part in (M_Pl/H₀)² ∼ 10¹²² with the residual
m_T²/δm_T² ∼ 10⁻¹²²; (2) the Sec. V closure item (b) no longer calls
κ²(J⁵·J⁵) "parity-odd" (its Fierz image is parity-even per the paper's
own B8/App. B; the parity-odd label routed to the pre-reduction
ε-contracted densities); (3) the |Ω₄₄/α₄| range floor corrected
O(1)–O(5) → O(3)–O(5) (the printed formula is bounded below by
378/120 ≈ 3.2 for all real γ — a strengthening); (4) the Route-2 one-loop
numerator, previously asserted in prose, exhibited as an explicit
unnumbered intermediate display assembling (α_em/4π)(H₀/M_Pl) from the
stated ingredients (∂ϑ ∼ H₀², /M_Pl, Hubble-time accumulation; dropped
conservative 1/16π² and β(γ) factors named; unnumbered so no downstream
renumbering); (5) the 3.6σ/2.9σ values qualified as obtained from
different datasets and distinct null procedures and not directly
comparable as statistical weights (closure-insufficiency of the R6
significance sentence — Gemini E1); (6) the Fig. 1 caption now states the
entries' mixed evidentiary status (sole Tier-I theorem B14; five general
naturalness/classification entries; Table II pointer) — the bounded
kernel of Grok M3, whose wholesale tier-segregated redraw is a re-flag;
(7) the Data & Code artifact block set footnotesize with unbreakable
boxes so neither `theory_audit` path breaks mid-filename, and the
App. E.2 whitespace gap closed by the reflow. Re-flags: version stamp +
future-date kernel (re-falsified against the calendar), wholesale
absorb-or-withdraw, Tier-I-standalone (re-falsified), sensitivity-table
demand, Fig. 1 redraw, abstract endpoint pointer, concept-DOI claim
(falsified in R2), mint-the-DOI-now (deferred-genuine, Houston-gated),
R4-derivation self-containment, `theory_audit` paths, abstract length,
App-A consolidation (D/P-round), ACT DR6 citation check (closed by
verification). v1C.0.10: 20 pp, 0 errors / 0 undef / 0 overfull, visual
audit pass on changed pages (1, 4, 5, 7, 9, 12, 13, 19, 20), mirrors
byte-identical (md5 `049ca009…`, SHA-256 `d8b9db8e…`).
**Convergence read (directive H-refined): R7 surfaced 7 genuinely-new-real
findings against a target of 0, so the paper is NOT converged and an R8
confirmation board on the exact v1C.0.10 PDF (sha `d8b9db8e…`) is
required.** (Calibration context, not verdict-softening: the Claude leg's
second 0-MAJOR report verified every recomputable equation with zero
numeric errors; all 7 GNR items are wording/notation/presentation-grade;
6 of 7 are single-leg items; 2 are closure-insufficiencies of earlier
fixes; the GNR count is trending 15 → 7 → 8 → 10 → 6 → 9 → 7.)
Prior-round record follows. The R6 confirmation board ran on
the exact v1C.0.8 PDF (sha `385158dd…`), three legs with raw receipts.

**R6 verdict matrix (2026-08-06, exact v1C.0.8 PDF, round dir label 2026-08-07):**

| Leg | Model | Verdict |
|---|---|---|
| Claude INT (Opus-tier) | claude opus | **MINOR REVISIONS** (1 MAJOR / 8 MINOR) — verification log again independently reproduced every load-bearing number (Route-3 1.38×10⁻⁶; R1 3.5/3.8×10⁻⁶⁹; Eq. (2) both contractions; hierarchy; Fierz chain; counts) |
| Grok API | grok-4.3 | **REJECT** |
| Gemini API | gemini-3.1-pro-preview | **MAJOR REVISIONS** |
| Perplexity | (optional leg) | FAILED — failure record, never a verdict |

The verdict-first truth audit against the R1–R5 disposition ledgers
(`project-context/peer-reviews/INT_v3/ROUND_2026-08-07-P1C-v1C.0.8-EXACTPDF-385158dd-R6CONF/P1C_v1C.0.8_R6_truth_audit.md`)
deduplicated the board to **21 canonical items: 9 genuinely-new-real
(closed in v1C.0.9), 10 re-flags of R1–R5-dispositioned content (one with a
partial falsification — Grok attributed the Route-2/3 one-loop inputs to
the unrefereed companion [1] when they are imported from published
Shapiro–Teixeira and Benedetti–Speziale [2]/[3]), 2 freshly falsified with
receipts** (Grok M4's "App. D only cites the theorem" — the full statement
and 4-step proof have been carried self-contained since v1C.0.4; Gemini
N4's "2026 dates are typos for 2024" — the current date is 2026-08-06).
**Headline closure — the boards' five-round companion-dependency demand
finally produced a bounded closable core (Claude M1 + Gemini M1) and was
closed as new Appendix E**: the Cartan/Freidel–Minic–Takeuchi
torsion-elimination chain fixing the −(3κ/16)[γ²/(1+γ²)] contact
coefficient (bivector inverse, FMT Eq. 17 contorsion, Eq. 23
back-substitution, 4πG = κ/2 bridge) and the R1 finite-density benchmark
arithmetic (κn_ψ² ≃ 1.0×10⁻⁷⁹ eV⁴ at 100 cm⁻³; 3.6×10⁻⁶⁹ of ρ_Λ at the
companion's (2.3 meV)⁴ normalization; 3/16-weighted value included), both
carried by faithful extraction from the P1A source
(`arxiv/paper1a_ech_nogo.tex` `sec:theory` + `sec:r1_njl`) with explicit
credit — the App-D/B14 precedent; nothing invented. The companion pieces
too long to carry (NJL gap analysis, tensor-sector B14 extension, R4
spectator check) are dispositioned deferred-genuine behind the
refereed-companion gate with honest not-peer-reviewed wording in Sec. I.
The other 8 closures, all bounded, zero margin/count/headline changes:
Eq. (2) LHS corrected to the double-normalized budget ratio its RHS
displays (Gemini pass-2 M2 + Claude m5; motivation now at the display;
both contractions still evaluated); the ∇·J⁵ disposal now routes the
gravitational Kimura–Delbourgo–Salam RR̃ anomaly content (present within
minimal field content) to O3 where it dies as a total derivative (Claude
m2; two real refs added; coefficient deliberately not quoted —
never-fabricate); the Data & Code pin moved to `c80b7487b01f` whose
artifact copies are verified identical to head (git-diff receipts),
retiring the R3-era drift footnote (Claude m4); the `theory_audit` prose
tag removed and the third/fourth-files archive boundary stated (Gemini
N2+N3); a β_obs detection-significance sentence (3.6σ WMAP+Planck / 2.9σ
ACT DR6; a smaller true signal only widens the margin — Claude m6); the
Fig. 1 caption attribution restated plainly via the in-figure edge labels
(Claude m7 + Grok m4); M_Pl²κ² = κ tagged exact-for-reduced-mass at both
App-A1/Table-III sites and the Route-3 1.4×10⁻⁶ tagged full-M_Pl (Claude
m3); the α_em Thomson-limit convention stated (Grok m3). Re-flags:
version stamp (directive G), abstract-tier framing, wholesale
absorb-or-withdraw, venue length/abstract length, novelty accounting,
O(1)-normalization labels, taxonomy vocabulary, abstract arithmetic trace,
mint-the-DOI-now (deferred-genuine, Houston-gated), journal-version
equation-number checks (deferred-genuine). v1C.0.9: 20 pp, 0 errors /
0 undef / 0 overfull, visual audit pass on changed pages (1, 2, 4, 6–9,
10, 11, 13, 16, 18–20), mirrors byte-identical (md5 `eab47932…`, SHA-256
`b4d73f94…`).
**Convergence read (directive H-refined): R6 surfaced 9 genuinely-new-real
findings against a target of 0, so the paper is NOT converged and an R7
confirmation board on the exact v1C.0.9 PDF (sha `b4d73f94…`) is
required.** (Calibration context, not verdict-softening: the one
MAJOR-grade closure resolves the boards' longest-running structural demand
by faithful extraction; 6 of 9 are single-leg wording/tagging/caption
items; 2 are closure-insufficiencies of earlier fixes; the only
physics-content correction leaves the closure unchanged because RR̃ = O3;
the GNR count is trending 15 → 7 → 8 → 10 → 6 → 9, with the R6 rise driven
by the newly-closable companion-dependency core rather than regressions.)
Prior-round record follows. The R5 confirmation board ran on
the exact v1C.0.7 PDF (sha `f085023f…`), three legs with raw receipts.

**R5 verdict matrix (2026-08-06, exact v1C.0.7 PDF, round dir label 2026-08-07):**

| Leg | Model | Verdict |
|---|---|---|
| Claude INT (Opus-tier) | claude opus | **ACCEPT** (0 MAJOR / 3 MINOR) — the Claude leg's FIRST ACCEPT on P1C, with a 17-item verification log independently reproducing every load-bearing number |
| Grok API | grok-4.3 | **REJECT** |
| Gemini API | gemini-3.1-pro-preview | **MAJOR REVISIONS** (ACCEPT→MAJOR flip vs R4 on unchanged-scope content; both named technical items falsified below) |
| Perplexity | (optional leg) | FAILED — failure record, never a verdict |

The verdict-first truth audit against the R1+R2+R3+R4 disposition ledgers
(`project-context/peer-reviews/INT_v3/ROUND_2026-08-07-P1C-v1C.0.7-EXACTPDF-f085023f-R5CONF/P1C_v1C.0.7_R5_truth_audit.md`)
deduplicated the board to **16 canonical items: 6 genuinely-new-real
(closed in v1C.0.8), 8 re-flags of R1–R4-dispositioned content (including
Gemini's repeated Fierz (F_c)₁₃ = 1 claim, recorded as a RE-FLAG of
R3-FAL-2 and re-falsified fresh with recomputation receipts), 1 freshly
falsified (the slash-fraction NIT), 1 opinion**. All 6 closures are bounded citation/wording/provenance-grade;
**zero numeric, margin, count, or headline changes**: (1) β_obs =
0.342°±0.094° re-attributed to its actual source — Eskilt–Komatsu
WMAP+Planck (PRD 106, 063503) — with the Minami–Komatsu Planck-2018 first
extraction (0.35°±0.14°, PRL 125, 221301) cited separately; (2) the
30–37 chiral-count lever-arm endpoints both motivated by explicit μ_IR
choices (1 GeV → ln 10¹⁶ ≈ 36.8; 1 TeV collider-probed cut → ln 10¹³ ≈ 30,
recomputed); (3) the unreconstructible ~10⁻³³ alternative-ordering figure
REMOVED per never-fabricate (labeled loose/unused; no derivation exists in
this paper or the frozen monolith — the qualitative ordering-freedom
disclosure is retained without the number); (4) Data & Code process-prose
neutralized per directive Q1 — no revision/date narration, "adjudicates" →
"verifies", archive boundary restated structurally; (5) a planned
pre-publication archival deposit for this survey's own scripts stated
in-text (actual DOI minting = P-round, deferred-genuine; the citation-form
half of Gemini's ESSENTIAL is closed — all four scripts were already
repo-relative \artifact links pinned to immutable commit `9b92721d5d7e`);
(6) Fig. 1 R4 node label harmonized to "naturalness / expl. deficit"
(matches Table I / Sec. IV C / Sec. VI). **Gemini's MAJOR — the claimed
Fierz (1,3) typo "breaking F_c² = 𝟙" — was adjudicated by recomputation:**
the matrix was transcribed from the compiled PDF (180 DPI render; the
(1,3) entry prints a stacked ½, identical typography in rows 1 and 5) and
the exact-rational product F_c² reproduces the identity on all 25 entries;
Gemini's 22/16 arises only by substituting (1,3)=1, confirming a
rasterization misread — same root cause as the R3 falsification of the
same claim. Gemini's slash-fraction NIT falsified by the same render.
Grok's five ESSENTIALs and two MAJORs are all re-flags of R1–R4
dispositions (self-containment, abstract-margin recomputation, version
stamp, enumeration, conditional-closure framing — each source-cited in the
audit); Grok's grammar nit on the abstract's absolute construction is
dispositioned OPINION. v1C.0.8: 18 pp, 0 errors / 0 undef / 0 overfull,
visual audit pass on changed pages (1, 4, 7, 8, 13), mirrors
byte-identical (md5 `992c02a2…`, SHA-256 `385158dd…`).
**Convergence read (directive H-refined): R5 surfaced 6 genuinely-new-real
findings against a target of 0, so the paper is NOT converged and an R6
confirmation board on the exact v1C.0.8 PDF (sha `385158dd…`) is
required.** (Calibration context, not verdict-softening: the Claude leg
flipped to ACCEPT — the board's second ACCEPT-class verdict after Gemini's
R4 ACCEPT; all 6 items citation/wording/provenance-grade; both of
Gemini's named technical items were falsified by computation; the GNR
count is trending 15 → 7 → 8 → 10 → 6.) Prior-round record follows. The R4 confirmation board ran on
the exact v1C.0.6 PDF (sha `fc23872d…`), three legs with raw receipts.

**R4 verdict matrix (2026-08-06/07, exact v1C.0.6 PDF):**

| Leg | Model | Verdict |
|---|---|---|
| Claude INT (Opus-tier) | claude opus | **minor-revisions** (0 MAJOR / 8 MINOR) |
| Grok API | grok-4.3 | **REJECT** |
| Gemini API | gemini-3.1-pro-preview | **ACCEPT WITH MINOR CORRECTIONS** — Gemini's FIRST ACCEPT-class verdict on P1C (MAJOR→ACCEPT flip) |
| Perplexity | (optional leg) | FAILED (quota) — failure record, never a verdict |

The verdict-first truth audit against the R1+R2+R3 disposition ledgers
(`project-context/peer-reviews/INT_v3/ROUND_2026-08-07-P1C-v1C.0.6-EXACTPDF-fc23872d-R4CONF/P1C_v1C.0.6_R4_truth_audit.md`)
deduplicated the board to **21 canonical items: 10 genuinely-new-real
(closed in v1C.0.7), 10 re-flags of R1/R2/R3-dispositioned content, 1
falsified with source citation** (Gemini's floating-paths nit — the paths
are monospace hyperlinked \artifact links in a set-off block). All 10
closures are wording/attribution/provenance-grade; **zero numeric, margin,
count, or headline changes**: (1) Table II R3 row re-attributed — the
deliberately-loose bound is the DKS-motivated chiral-count ansatz, not
Benedetti–Speziale, whose integrated flow is the separate far-smaller
derived estimate; (2) §V.a "R2–R3 are Tier-III" aligned with Table II's
(II)+(III) records via an amplitude-vs-structural-leg clause; (3) the R1
benchmark mantissa dispute (Claude m3: recomputed 3.9×10⁻⁶⁹ vs quoted
3.6×10⁻⁶⁹) **adjudicated with recomputation receipts — BOTH values
correct**, a ρ_Λ-normalization difference (P1A's published (2.3 meV)⁴ vs
this survey's App-A (2.25 meV)⁴; κn_ψ² = 9.954×10⁻⁸⁰ eV⁴ reproduces P1A's
own 3.5571×10⁻⁶⁹/68.45-order ledger exactly), so the 3.6 quote is
faithful to the cited P1A anchor and the §II convention flag now states
both inputs (≈68 orders either way); (4) Fig. 1 Branch-H arrows labeled
per-barrier in the drawing (B8/B14 vs B14 fan); (5) branch-letter gaps
disclosed (I, K never assigned — verified against the frozen monolith);
(6) Gemini's MAJOR Zenodo-timeline contradiction closed by stating the
archive boundary explicitly (the 2026-08-05 adjudication artifacts
post-date the 2026-07-22 deposit and live at pinned commit `9b92721d5d7e`
only — contents verified by git ls-tree); (7) the version-history
parenthetical moved to a footnote (disclosure preserved); (8) App-C
inline audit-report tag relocated to Data & Code Availability (.md report
now listed); (9) acknowledgments rephrased to builds-on-published-work
form with citations + no-endorsement sentence; (10) abstract "each
closing a specific route" → "one or more of the four routes" (B14 spans
all four). Re-verified this round though only re-flagged: ST/BS one-loop
coefficient transcriptions vs fresh ar5iv fetches of arXiv:1402.4854
(Eqs. 41–42: α₄, Ω₄₄, Ω₂₄) and arXiv:1111.0884 (Eq. 7: 23γ²+5) — all
exact. v1C.0.7: 18 pp, 0 errors / 0 undef / 0 overfull, visual audit
pass, mirrors byte-identical (md5 `a75934be…`, SHA-256 `f085023f…`).
**Convergence read (directive H-refined): R4 surfaced 10 genuinely-new-real
findings against a target of 0, so the paper is NOT converged and an R5
confirmation board on the exact v1C.0.7 PDF (sha `f085023f…`) is
required.** (Calibration context, not verdict-softening: first ACCEPT-class
verdict on the board; Claude's first 0-MAJOR report; all 10 items
wording/attribution/provenance-grade; the only MAJOR-labeled item was
administrative.) Prior-round record follows. The R3 confirmation board ran 2026-08-06 on
the exact v1C.0.5 PDF (sha `a770491d…`), three legs with raw receipts:
**Claude Opus INT minor-revisions (1 MAJOR / 7 MINOR) · Grok grok-4.3
REJECT · Gemini gemini-3.1-pro-preview MAJOR REVISIONS**. The Perplexity leg
FAILED — recorded as failed, never a verdict. The verdict-first truth audit
against the R1+R2 disposition ledgers
(`project-context/peer-reviews/INT_v3/ROUND_2026-08-06-P1C-v1C.0.5-EXACTPDF-a770491d-R3CONF/P1C_v1C.0.5_R3_truth_audit.md`)
deduplicated the board to 20 canonical items: **8 genuinely-new-real (closed
in v1C.0.6), 8 re-flags of R1/R2-dispositioned content, 1 scope-opinion, 3
falsified with recomputation receipts** (Claude's Ω₄₄/α₄-exponent claim —
the PDF prints the first-power denominator and recomputation confirms it;
Gemini's Fierz (F_c)₁₃=1 claim — the matrix prints ½ and F² = 𝟙 verifies on
all 25 entries, a stacked-fraction extraction artifact; Grok's
no-operator-table claim — Table III exists). The 8 closures, headline
first: (1) the completeness framing exceeded what the released script
verifies — adjudicated to the honest **wording downgrade (option b)** per
never-fabricate: Sec V retitled "The Operator-Basis Argument", every
"completeness argument" surface downgraded with the rule-asserted
disclosure, App-A1 "enumerate" → "exhibit", and the released script's
overclaiming docstring/output corrected in the same commit (re-run: both
identities pass); option (a) — actually mechanizing the enumeration — was
examined and rejected for this round because the literal construction rule
admits mixed R·T·T / T⁴ classes whose adjudication is real derivation work
(days), not a bounded script extension; the mechanized enumeration is
recorded as deferred-genuine, never claimed without the artifact. (2)
Strict κ = 8πG = M_Pl⁻² contradiction (two legs) resolved: κ ≡ 8πG exactly
(= reduced-mass M̄_Pl⁻²), full-mass κ ∼ M_Pl⁻² declared an explicit 8π
order-of-magnitude abuse, mixed-usage note added (Table-II R1 benchmark =
exact κ; App-A hierarchy = full mass). (3) Abstract/conclusions 61–67-order
endpoints labeled honestly (67 = derived integrated flow; 61 = deliberately
pessimistic chiral-count bound). (4) α_em/4π rounding stated explicitly
(5.8×10⁻⁴ rounded UP to 10⁻³ — conservative direction). (5) Table III gains
a "Final (×prefactor)" column so the table itself shows O4 = O5 →
κ(J⁵·J⁵) (the R2 caption-only fix was judged insufficient by a fresh leg).
(6) R4 anchor α/M ∼ 10⁻²¹ GeV⁻¹ given its two-sentence algebraic origin
carried from P1A (β = (α/2M)Δφ, Δφ ∼ √(2ρ_θ)/m_θ ∼ M_Pl). (7)
Integrand-dimension phrasing fixed (prefactor outside the integral). (8)
Ref. [12] rendering fixed. v1C.0.6: 18 pp, 0 errors / 0 undef / 0
overfull, visual audit pass, mirrors byte-identical (md5 `a0dac49c…`,
SHA-256 `fc23872d…`). **Convergence read (directive H-refined): R3
surfaced 8 genuinely-new-real findings against a target of 0, so the paper
is NOT converged and an R4 confirmation board on the exact v1C.0.6 PDF
(sha `fc23872d…`) is required.** (Calibration context, not
verdict-softening: 1 of 8 was MAJOR-grade and resolved by an honest
wording downgrade; 1 was a two-leg definitional error; 1 was an
insufficiency of an R2 closure; 5 were single-leg minor/nit-grade labeling
or formatting items.) Prior-round record follows. The R2 confirmation board ran 2026-08-06 on
the exact v1C.0.4 PDF (sha `7ec5f221…`), three legs with raw receipts:
**Claude Opus INT minor-revisions (1 MAJOR / 4 MINOR) · Grok grok-4.3
REJECT · Gemini gemini-3.1-pro-preview MAJOR REVISIONS**. The Perplexity leg
FAILED — recorded as failed, never a verdict. The verdict-first truth audit
against the R1 disposition ledger
(`project-context/peer-reviews/INT_v3/ROUND_2026-08-06-P1C-v1C.0.4-EXACTPDF-7ec5f221-R2CONF/P1C_v1C.0.4_R2_truth_audit.md`)
deduplicated the board to 20 canonical items: **7 genuinely-new-real (closed
in v1C.0.5), 9 re-flags of R1-dispositioned/disclosed content, 2
scope/venue opinions (tier-taxonomy wording; per-paper Zenodo DOI minting →
P-round checklist), 2 falsified with source citations** (no-tier-rubric —
the rubric is printed in Sec. IV; concept-DOI-placeholder — version DOIs are
primary and the entries are Zenodo deposits, not arXiv preprints). The 7
closures: (1) B10 classification self-contradiction resolved (novelty =
provenance label decoupled from ECH-specificity; preamble/list/entry/Sec-VI
now agree); (2) O4 torsion-square schematic re-indexed from the
non-typechecking ε_{IJKL}T^{IJ}T^{KL} to the parsing Nieh–Yan component
form ε^{μνρσ}T^I_{μν}T_{Iρσ} (T carries ONE internal index); (3) App-C
G_s = −3κ/16 cross-reference reconciled with Sec II's γ²/(1+γ²) contact
operator per P1A's gap-equation convention (defect introduced by the R1
closure); (4) Table-II R1 suppression anchored to P1A's published
κn_ψ²/ρ_Λ ≃ 3.6×10⁻⁶⁹ (n/100 cm⁻³)² benchmark (≈68 orders, replacing the
unanchored "∼70"); (5) LQC-window provenance: 0.41 = Ashtekar–Singh
canonical at γ=0.2375, 0.27 = P1A's SU(2)-entropy scheme extrapolation, not
a published value; (6) Table-III caption now states the Fate column is the
bare-invariant reduction (restoring prefactors, O4 = O5 → κ(J⁵·J⁵)); (7)
Eq. (2) denominator roles stated explicitly — the direct angle-only
contraction gives ≈2×10⁻⁶² (two MORE orders), so the quoted ~10⁻⁶⁰ (≥58) is
the conservative side; margins unchanged everywhere. **Convergence read
(directive H-refined): R2 surfaced 7 genuinely-new-real findings against a
target of 0, so the paper is NOT converged and an R3 confirmation board on
the exact v1C.0.5 PDF (sha `a770491d…`) is required.** (Calibration
context, not verdict-softening: 5 of 7 were single-leg minor-grade
consistency/traceability items, 1 was introduced by an R1 closure, 1 was a
conservative-direction labeling defect.) Prior-round record follows. The R1
board ran 2026-08-06 on the exact
v1C.0.3 PDF (sha `85e53832…`), three legs with raw receipts: **Claude Opus
INT major-revisions (3 MAJOR / 8 MINOR) · Grok grok-4.3 REJECT · Gemini
gemini-3.1-pro-preview MAJOR REVISIONS**. The Perplexity leg FAILED (API
quota) and earlier R2/R3 dispatch attempts were infra failures (stale
portfolio receipts) — failure records preserved, never counted. The
verdict-first truth audit
(`project-context/peer-reviews/INT_v3/ROUND_2026-08-06-P1C-v1C.0.3-EXACTPDF-85e53832/P1C_v1C.0.3_truth_audit.md`)
deduplicated the board to 20 canonical items: **15 genuinely-new-real
(closed in v1C.0.4), 2 re-flags of disclosed content, 1 scope/venue
opinion, 2 falsified with source citations**. Headline closures: printed
Fierz matrix (B1) replaced with the adjudication-computed published-P1A
matrix so the displayed B1 → (−F_c) → B2 chain composes and matches
`fierz_lemma_check.py` (adjudication [L12]/[L15]); the B14 Tier-I theorem
is now stated and proved self-contained in-paper (new App. D, carried
faithfully from P1A `sec:transparency`); Shapiro–Teixeira Ω₂₄/Ω₄₄
transcriptions corrected against the arXiv source (Eq. 42) with the
|Ω₄₄/α₄| illustrative ratio recomputed (≈3.3 at γ≈0.24); per-route closure
metrics stated honestly everywhere (R2 vs observed birefringence
amplitude, R3 vs observed dark-energy density); Fig. 1 B14→R2/R3/R4
arrows; hierarchy display fixed to exact values (8.7×10¹²² ≈ 10¹²³) with a
rounding-convention sentence; dimension-consistent ∂ϑ_NY ~ H₀²
substitution; footnote 1 promoted to App. B; Contributions paragraph +
Q1 hedging consolidation; frozen-commit pin + companion DOI in Data & Code
Availability. Deferred-genuine (pre-submission checklist): ST Eq. 58 +
"unable to solve" verbatim-quote verification (source render truncated;
every other quoted ST/BS equation now source-verified); venue-length
condensation (D/P rounds). Prior-round context follows. The
2026-08-05 internal referee read-through of v1C.0.1 (exact-PDF-bound, sha
847fb143;
`project-context/peer-reviews/INT_v3/ROUND_2026-08-05-P1C-v1C.0.1-EXACTPDF-847fb143-INTERNAL-READTHROUGH/`)
returned 9 MAJOR + 11 MINOR, verdict major-revisions. All 20 findings are
dispositioned in the round's `CLOSURE_NOTES_v1C.0.2.md`; the closures landed
as v1C.0.2 (figure/list rebuild to 0 overfull boxes, Fierz
convention/discrepancy note, kappa-vs-imported-kappa~ convention split,
41→61-order fix, B14→Branch H assignment propagated, division-of-content
paragraph vs published P1A, R2/R3 reframed as historical-route amplitude
budgets). The v1C.0.2 convention note's deferred item — reconciling the
monolith's App-B Fierz coefficients against the published-P1A/
`fierz_lemma_check.py` convention — is now resolved: independent adjudication
(`research/theory_audit/fierz_adjudication_2026_08_05.{py,json,md}`, commit
`7f1449b5`) found the published-P1A coefficients (operator row
SS + ½VV + ½AA − PP, G_s = −3κ/16) correct under both metric signatures, and
the monolith's App-B variant (¼SS+½VV−½AA−¼PP, G_s = −3κ/64) internally
inconsistent (spurious ¼ factors; G_s 4× too small). v1C.0.3 adopts the
adjudicated coefficients in Eq.~(B2) and Appendix B's convention note, citing
the verification artifact; no downstream P1C equation used the monolith's
−3κ/64 value (P1C's Sec.~II already stated −3κ/16), so no other correction
was required. No readiness percentage is claimed — zero INT/EXT board
rounds, zero convergence evidence, zero packaging/venue work; do not read it
against the 6-candidate readiness contract until real board gates have run.

## What this is

"A Structural No-Go Survey of Minimal Spin-Torsion Routes to Dark Energy and
Bounce Phenomenology." A systematic survey of 7 foundation mechanism classes
(A-G) and 6 observational branches (H, J, L, M, N, O), collapsing to 13
distinct mechanism-class constraints across 14 catalog entries, closing four
candidate dark-energy routes (R1-R4). Companion to P1A: cites P1A's
torsion-elimination (Route 1) and zero-spin-branch transparency results
rather than re-deriving them.

## Provenance

Extraction, not new derivation. Source: `arxiv/paper1_unified.tex`
`sec:barriers` (the frozen 6,898-line pre-split P1U draft — table
`tab:barriers`, TikZ figure `fig:barrier_map`, per-barrier `\item[B1]`...`[B14]`
prose), retired from the reader-visible paper at the 2026-07-14 P1 split
(`project-context/peer-reviews/INT_v3/ROUND_2026-07-13-M44-NONANTHROPIC/P1_SPLIT_CLOSURE.md`)
because M44 non-Anthropic external review found P1U's broad four-route
rhetoric outran what was tightly derived — the closure cut rather than
relabeled, but the barrier content itself was never invalidated and
`paper1_unified.tex` was explicitly not edited. Ancestor derivation:
`research/paper1_salvage_alp/01_salvage_map.md`, `05_claims_table.md`,
`final_verdict.md` (2026-03-17). A standalone source write-up also exists at
`research/focused_paper_source_integration/paper3_barriers_ech_transparency.tex`/`.pdf`.

Decision record: `project-context/PAPER_LINEAGE_2026-08-05.md` Sec. 4(a) and
its "Decision record — 2026-08-05" (agent-executed under Houston's explicit
full delegation, item 1: "No-go survey paper: RESURRECT"). Extraction is a
pure-contribution reframe under directive Q1 — the paper's thesis is the
no-go survey itself, not a narration of the P1 split.

## Registry

`project-context/paper_registry.json` → `companion_manuscripts.P1C`.
`tex_path`/`pdf_path` both under `arxiv/paper1c_nogo_survey/`. Not one of the
six campaign-roster papers (P1A, P1B, P2, P3, P4, P5) tracked in the
readiness contract table.

## Compile state

v1C.0.15: **25 pp, 0 errors, 0 undefined refs, 0 overfull hboxes** (45
underfull, badness-only revtex float artifacts), 4-pass compile clean
2026-08-07 (`arxiv/paper1c_nogo_survey/main.pdf`). Mirrored byte-identical to
`site/public/papers/paper1c_nogo_survey_v1C.0.15.pdf`,
`public/papers/paper1c_nogo_survey_v1C.0.15.pdf` and
`site/out/papers/paper1c_nogo_survey_v1C.0.15.pdf` (md5
`3a46b8c270906e0b943d7c0082f36922`, sha256
`f3e29c45df35f7ac358d8f4e6a854d1b9f79fa20c71a725922732db82bd967d4`, all
four copies match). Prior v1C.0.1–v1C.0.14 mirrors retained. The
pre-existing `Warning--missing journal in DiegoPalazuelos2025` bibtex
diagnostic is unchanged from v1C.0.14 and is not introduced by this round.
Two float regressions created by the R12 correction were caught and fixed
inside the round, both confirmed new against a pristine v1C.0.14 compile:
Table III overflowed its full-width float by 28.5 pt once the O4/O5 cells
carried γ-dependent values (fixed by compacting the rational expressions,
abbreviating `(J⁵)² ≡ J⁵·J⁵` in the table body with a caption note, and
setting `\footnotesize` on the tabular), and Table II became "too large for
page by 22 pt" and stuck once the R2 cell lengthened (fixed by moving the
R12-GNR-9 reconciliation sentence out of the cell and into Sec. IV A prose).
`/latex-audit`: **PASS.** Log scan clean; pages 1 (title block + abstract),
2 and 3 (conventions + the new on-shell torsion equation), 13 (Table II), 15
(Sec. V collapse bullets + the new O4 equation), 17 (Data & Code artifact
block), 21 (Table III) and 22 (App. C scope) rendered at 130 DPI and
visually confirmed — no column-gutter crossings, no right-margin overruns,
no float escapes. All **8** `\artifact{}` targets resolve to existing repo
paths. No `\date` overflow risk: there is no `\date` call (an empty
`\date{}` still renders "(Dated:)" in revtex4-2), and the title block
carries no version or date string — draft provenance lives in the PDF
metadata (`pdfinfo` → `Keywords: v1C.0.15 (August 7, 2026)`). Two raw
`\texttt{}` filenames remain and are bare functional filenames rather than
directory paths (the R11-GNR-10 disposition), both wrapping at 0 overfull.
`tools/p1c_consistency_check.py`: **4/4 rules PASS, exit 0**, run before the
version bump and again after every table fix.

Note: v1C.0.15 adds two numbered equations in Sec. II and Sec. V
(`eq:ech_onshell_torsion`, `eq:o4_onshell`), so equation numbering downstream
of Sec. II shifts by one relative to v1C.0.14. Every cross-reference in the
source is `\eqref`-driven and no hard-coded equation number exists (verified
by grep), but reviewer reports written against v1C.0.14 equation numbers must
be read with that offset in mind.

## What has NOT happened (explicit, so nobody assumes otherwise)

- ~~No INT review round~~ R1 INT board DONE 2026-08-06 (Claude
  major-revisions / Grok REJECT / Gemini MAJOR; truth-audited; 15
  genuinely-new-real closed as v1C.0.4). R2 confirmation board DONE
  2026-08-06 (Claude minor-revisions / Grok REJECT / Gemini MAJOR;
  Perplexity FAILED; 7 genuinely-new-real closed as v1C.0.5) — R2 was NOT
  clean, so there is still zero convergence evidence; R3 required.
- No EXT review round (ChatGPT/Grok/Gemini browser sweep)
- No readiness percentage computed or claimed
- No Convex `paperVersions` row, no `rRounds`/`externalReviews` entries
  (P1C is a draft outside the 6-paper roster; site surfaces update via
  static `papers.ts`/`reviewTimeline.ts` for now)
- No Zenodo DOI, no venue kit, no arXiv submission prep
- Not added to `papers[]` in `site/src/data/papers.ts` (would imply the
  version-chip/PDF-mirror/publication-path machinery every roster paper
  carries); surfaced instead as a `bounce-theory` program `supportingLinks`
  entry labeled "In preparation," matching the P1B-MCMC-companion precedent
  (commit `cbe93641`)

## Next gates (in order)

1. ~~Internal read-through~~ DONE 2026-08-05 (9 MAJOR + 11 MINOR, all
   dispositioned; closures landed as v1C.0.2 — see
   `ROUND_2026-08-05-P1C-v1C.0.1-EXACTPDF-847fb143-INTERNAL-READTHROUGH/CLOSURE_NOTES_v1C.0.2.md`)
2. ~~First full INT board~~ DONE 2026-08-06 (R1 on the exact v1C.0.3 PDF:
   Grok REJECT / Gemini MAJOR / Claude major-revisions; truth audit +
   15 genuinely-new-real closures landed as v1C.0.4 — see
   `ROUND_2026-08-06-P1C-v1C.0.3-EXACTPDF-85e53832/P1C_v1C.0.3_truth_audit.md`)
3. ~~R2 confirmation board~~ DONE 2026-08-06 (on the exact v1C.0.4 PDF sha
   `7ec5f221…`: Claude minor-revisions / Grok REJECT / Gemini MAJOR /
   Perplexity FAILED; truth audit + 7 genuinely-new-real closures landed as
   v1C.0.5 — see
   `ROUND_2026-08-06-P1C-v1C.0.4-EXACTPDF-7ec5f221-R2CONF/P1C_v1C.0.4_R2_truth_audit.md`).
   R2 was NOT clean (7 genuinely-new-real vs a target of 0) → convergence
   NOT reached.
4. ~~R3 confirmation board~~ DONE 2026-08-06 (on the exact v1C.0.5 PDF sha
   `a770491d…`: Claude minor-revisions / Grok REJECT / Gemini MAJOR /
   Perplexity FAILED; 8 genuinely-new-real closed as v1C.0.6). NOT clean.
5. ~~R4 confirmation board~~ DONE 2026-08-06/07 (on the exact v1C.0.6 PDF
   sha `fc23872d…`: Claude minor-revisions 0 MAJOR / Grok REJECT / Gemini
   **ACCEPT WITH MINOR CORRECTIONS** (first ACCEPT) / Perplexity FAILED;
   10 genuinely-new-real closed as v1C.0.7 — see
   `ROUND_2026-08-07-P1C-v1C.0.6-EXACTPDF-fc23872d-R4CONF/P1C_v1C.0.6_R4_truth_audit.md`).
   R4 was NOT clean (10 genuinely-new-real vs a target of 0) → convergence
   NOT reached.
6. ~~R5 confirmation board~~ DONE 2026-08-06 (on the exact v1C.0.7 PDF
   sha `f085023f…`: Claude **ACCEPT** (0 MAJOR / 3 MINOR — first Claude
   ACCEPT) / Grok REJECT / Gemini MAJOR (both named technical items
   falsified by recomputation) / Perplexity FAILED; 6 genuinely-new-real
   closed as v1C.0.8 — see
   `ROUND_2026-08-07-P1C-v1C.0.7-EXACTPDF-f085023f-R5CONF/P1C_v1C.0.7_R5_truth_audit.md`).
   R5 was NOT clean (6 genuinely-new-real vs a target of 0) → convergence
   NOT reached.
7. ~~R6 confirmation board~~ DONE 2026-08-06 (on the exact v1C.0.8 PDF
   sha `385158dd…`: Claude MINOR REVISIONS (1 MAJOR / 8 MINOR) / Grok
   REJECT / Gemini MAJOR / Perplexity FAILED; 9 genuinely-new-real closed
   as v1C.0.9 — headline: new App. E carries the contact-coefficient
   derivation and R1 benchmark self-contained by faithful extraction from
   the P1A source; see
   `ROUND_2026-08-07-P1C-v1C.0.8-EXACTPDF-385158dd-R6CONF/P1C_v1C.0.8_R6_truth_audit.md`).
   R6 was NOT clean (9 genuinely-new-real vs a target of 0) → convergence
   NOT reached.
8. ~~R7 confirmation board~~ DONE 2026-08-06/07 (on the exact v1C.0.9 PDF
   sha `b4d73f94…`: Claude MINOR REVISIONS (0 MAJOR / 8 MINOR) / Grok
   REJECT / Gemini MAJOR / Perplexity FAILED; 7 genuinely-new-real closed
   as v1C.0.10 — see
   `ROUND_2026-08-07-P1C-v1C.0.9-EXACTPDF-b4d73f94-R7CONF/P1C_v1C.0.9_R7_truth_audit.md`).
   R7 was NOT clean (7 genuinely-new-real vs a target of 0) → convergence
   NOT reached.
9. ~~R8 confirmation board~~ DONE 2026-08-07 (on the exact v1C.0.10 PDF
   sha `d8b9db8e…`: Claude MINOR REVISIONS (0 MAJOR / 7 MINOR) / Grok
   REJECT / Gemini MAJOR / Perplexity FAILED; correctness/presentation
   classification introduced; 4 genuinely-new-real closed as v1C.0.11
   (2 correctness-grade citation-precision + 2 presentation-grade
   notation/display); Claude's headline formula finding + Grok M2/m3 +
   Gemini N1 all falsified with receipts — see
   `ROUND_2026-08-07-P1C-v1C.0.10-EXACTPDF-d8b9db8e-R8CONF/P1C_v1C.0.10_R8_truth_audit.md`).
   R8 was NOT clean (4 genuinely-new-real vs a target of 0) → convergence
   NOT reached under the literal gate.
10. ~~R9 correctness-convergence board~~ DONE 2026-08-07 (exact v1C.0.11 PDF
   sha `08688560…`; closures landed as v1C.0.12). NOT clean.
11. ~~R10 correctness-convergence board~~ DONE 2026-08-07 (exact v1C.0.12 PDF
   sha `c21fde9f…`; closures landed as v1C.0.13). NOT clean.
12. ~~R11 correctness-convergence board~~ DONE 2026-08-07 (exact v1C.0.13 PDF
   sha `d3aea74d…`: Claude MAJOR REVISION 4 MAJOR / 6 MINOR with zero
   computational errors across 30 recomputed relations / Grok REJECT /
   Gemini MAJOR REVISIONS / Perplexity FAILED; 14 genuinely-new-real closed
   as v1C.0.14, 6 correctness-grade; `tools/p1c_consistency_check.py`
   introduced as the anti-regression guard — see
   `ROUND_2026-08-07-P1C-v1C.0.13-EXACTPDF-d3aea74d-R11CONV/P1C_v1C.0.13_R11_truth_audit.md`).
   NOT clean.
13. ~~R12 correctness-convergence board~~ DONE 2026-08-08 (exact v1C.0.14 PDF
   sha `9dd5c708…`: Claude MAJOR REVISIONS 2 MAJOR / 9 MINOR + 5 withdrawn /
   Grok REJECT / Gemini **ACCEPT WITH MINOR CORRECTIONS** / Perplexity
   FAILED; 15 genuinely-new-real closed as v1C.0.15, 11 correctness-grade;
   the on-shell ECH torsion corrected after both MAJORs were confirmed by an
   independent solve of the connection equation, and the 2026-08-07
   operator-basis artifact given a dated erratum addendum — see
   `ROUND_2026-08-08-P1C-v1C.0.14-EXACTPDF-9dd5c708-R12CONV/P1C_v1C.0.14_R12_truth_audit.md`).
   NOT clean, and the defect class regressed from internal-consistency to a
   wrong physical premise.
14. **R13 correctness-convergence board — NEXT** (same three active legs,
   fresh, on the exact v1C.0.15 PDF sha `f3e29c45…`). Exit test per the R8
   classification rule: a full board whose truth audit yields ZERO
   correctness-grade GNR converges the R-phase; presentation-grade items
   route to the D-round. R13 is the first board to review an on-shell
   operator disposal derived from the solved connection equation rather than
   from a substituted ansatz, so the operator-list sections
   (Sec. II Eq. (1), Sec. V, App. A 1, Table III, App. C, App. E) are the
   priority read. Pre-submission checklist carries: real mechanized
   enumeration (or keep downgraded framing); ST Eq. 58 + quote verification;
   venue-length condensation (24 → 25 pp at R12, target still unmet); mint
   the version DOI / updated archival deposit for the P1C script set — now
   **eight** files — at P-round (R2-SO-2 / R5-GNR-2 / R6-RF-9 / R7-RF-8 /
   R8-RF-11 / R11-DEF-1 / R12-DEF-1); refereed-companion gate for the
   cited-only companion results (R6-GNR-1 / R7-RF-9 / R8-RF-10).
15. D/P rounds (visual + packaging) only after INT/EXT convergence, per the
   standard readiness ladder (R-rounds converge -> 96 -> D-round -> 98 ->
   P-round -> 99 -> Houston sign-off -> 100)

Deferred item from the read-through closure — RESOLVED 2026-08-06: the
Fierz-convention reconciliation between the monolith's App-B presentation
and the released `fierz_lemma_check.py`/published-P1A Nieves–Pal convention
is adjudicated in favor of published P1A (see Status above and
`research/theory_audit/fierz_adjudication_2026_08_05.md`); v1C.0.3's
Eq.~(B2) and convention note now state and cite the adjudicated identity
directly, no unresolved alternative presented. Until the INT board runs,
this file should not grow a readiness number or a "converged" claim.
