# P1C v1C.0.13 — INT Referee Report (Claude leg, R11 convergence board)

**Manuscript:** `arxiv/paper1c_nogo_survey/main.pdf` — "A Structural No-Go Survey of
Minimal Spin-Torsion Routes to Dark Energy and Bounce Phenomenology"
**SHA-256:** `d3aea74da62a433c186e3c809b4acadcd82453c3686aebc34fec9f5c2c15efbb` — **VERIFIED against the assigned hash before review.**
**Pages:** 23 (all read). **Version stamp (PDF metadata pdfkeywords):** v1C.0.13 (August 7, 2026)
**Date of review:** 2026-08-07
**Role:** Independent skeptical journal referee, CQG calibre. No prior exposure to this
manuscript or to any earlier review of it. Consistency sources consulted read-only:
`arxiv/main.tex` (published companion), `research/theory_audit/*.md`.
**Method note:** Every asserted printed-math error below was re-rendered at ≥300 DPI
(`pdftoppm -r 300`, pages 1, 3, 4, 6, 7, 8, 9, 10, 12, 20, 21; Fierz matrix crop at 400 DPI)
and re-read before being written down. Items that survived only in the source `.tex`
and not in the compiled PDF are labelled as such and are **not** counted as manuscript defects.

---

## VERDICT: **MAJOR REVISION**

4 MAJOR / 6 MINOR. **Zero computational errors of substance.**

I independently recomputed **30 checkable displayed relations and numerical claims**
(listed in the Correctness Ledger below) and found **exactly one** numerical
discrepancy, and that one is a rounding slip in a parenthetical, not in a result.
The Fierz involution, the Benedetti–Speziale flow integration, the O4/O5 tensor
reductions, and every order-of-magnitude figure in Appendices A and E reproduce
exactly. The physics of this survey is, so far as I can check it, sound.

The reason this is not an ACCEPT is entirely on the paper's declared weak axis:
**its self-scoping statements have drifted out of sync with its own Table II and
with one of the released artifacts it cites.** All four MAJORs are claim-scoping
or internal-consistency defects. None requires new physics, new computation, or
any weakening of a result to fix — three are resolved by making the text agree
with the table, and one by deleting a single word. But they are not cosmetic:
each is a case where the manuscript, read literally, claims more than the thing
it points at establishes, which is precisely the failure mode this survey is
otherwise unusually disciplined about avoiding.

---

## MAJOR FINDINGS

### MAJOR-1 [correctness] — Table II contains two Tier-(I) legs; six statements in the text assert there is exactly one

**Anchors.** Table II, R2 row, "Evidentiary status" column, p.12 (300 DPI verified):

> *Dark-energy* leg: **(I)** for constant Nieh–Yan coefficient (O1/O2 total
> derivatives, B7 fixes γ); **(II)** R4-class naturalness only for a dynamical ϑ_NY…

That is a second bold **(I)** in the closure table, alongside the
perturbation-transparency row. It is contradicted, verbatim, at six sites:

1. Abstract, p.1: "only the perturbation-transparency result is a Tier-I rigorous theorem".
2. Sec. III preamble, p.3: "only the perturbation-transparency theorem enters the
   closure table (Table II) as a Tier-I leg… **which is why the abstract credits
   exactly one Tier-I rigorous theorem**."
3. B14 entry, Sec. III A, p.6: "This is the catalog's **sole** Tier-I closure leg (Table II)".
4. Sec. IV C, p.11: "No leg is claimed at a level higher than this table records:
   in particular, **the only** Tier-I (rigorous) leg is the perturbation-transparency result".
5. Sec. VI, p.16: "**Only** the perturbation-transparency theorem (B14…) enters the
   closure table as a Tier-I rigorous result".
6. App. D preamble, p.21: "So that the catalog's **sole** Tier-I leg can be refereed…".

Sec. IV A, p.8 supplies the third leg of the contradiction: "Minimal Route 2
therefore sources no dark energy, and this *is* an operator-level (Tier-I)
statement about the list", and "Route 2's dark-energy leg is closed at Tier-I only
in case (i)". Table II's caption meanwhile promises "The table records the highest
level at which each leg is claimed; no leg is asserted more strongly elsewhere" —
the inverse of the actual situation, where the *table* asserts more strongly than
the text.

**Second, independent problem with the same (I).** Even taken alone, the Tier-(I)
grading of R2's dark-energy leg does not meet the paper's own Tier-I definition
(Sec. IV C: "a deductive consequence of stated equations/identities"). The claim
"minimal Route 2 sources no dark energy" is not a statement about O1 and O2; it is
a statement that O1/O2 are *all* the surviving Holst/Nieh–Yan content. That step
is the spanning assertion, which the manuscript itself disclaims in six places —
abstract p.1 ("That the list *spans* the rule-admitted operator space is asserted
from the construction rules, not proved by exhaustive symbolic enumeration"),
Sec. V p.13–14, App. A1 p.18, Sec. VI p.16, and the Data & Code statement p.16
("None of the scripts performs the enumeration establishing that the list spans
the rule-admitted space"). A conclusion resting on an explicitly unproved premise
cannot be Tier-I under this paper's own scale.

**Assessment.** This is a regression introduced by the v1C.0.13 MAJOR-2 closure.
The closure correctly stopped delegating R2's dark-energy leg to the NDA bound,
but in re-homing it on the operator list it promoted it to a tier the list cannot
carry, and did not propagate the change to the six "exactly one Tier-I" surfaces.

**Required.** Either (a) regrade the R2 dark-energy leg to (II) with the O1/O2
total-derivative fact cited as its structural content — my recommendation, and
consistent with everything else in the paper — or (b) keep (I) but scope it
narrowly to "O1 and O2 are exact total derivatives" (which *is* Tier-I), state
plainly that the step from that to "minimal Route 2 sources no dark energy"
inherits the unproved spanning assertion, and repair all six "only/sole/exactly
one Tier-I" statements plus the Table II caption. Do not leave the count
ambiguous; the abstract stakes a headline on it.

---

### MAJOR-2 [correctness] — Residual claim that the single-scale NDA bound covers Eq. (1), directly contradicting Sec. IV A

**Anchor.** Sec. IV B, "Ansatz vs derivation (R2/R3)" paragraph, p.10, left column,
lines 34–38 of the column (300 DPI verified):

> …only the single absolute normalization remains a bounded EFT input, because the
> Shapiro–Teixeira λ₄–γ flow has no fixed point and is not perturbatively solvable
> in closed form, **and the operator is bounded by the single-scale NDA no-go
> regardless of that O(1) normalization.**

"The operator" is Eq. (1), the R2 one-loop parity-odd operator. This is flatly
contradicted twice on p.8 and once on p.6 (all 300 DPI verified):

- p.8, Sec. IV A: "Its Hubble-scale background ⟨∂_μϑ_NY⟩ ∼ H₀² moreover makes ϑ_NY
  a new light scale μ ≪ M_Pl — precisely the case App. A names as able to *evade*
  the single-scale NDA bound. **We therefore do not claim the NDA bound covers it**".
- p.8, Sec. IV A: "…in case (ii) it is closed at Tier-II, by the same naturalness
  objection that closes R4, and **not by an amplitude bound or by the single-scale
  NDA argument**."
- p.6, Sec. IV head: "…so its dark-energy leg is **not** closed by the single-scale
  NDA bound, which App. A states explicitly can be evaded by exactly such a light scale."

The v1C.0.13 revision note states of this exact defect: "The false delegation is
removed." It is removed at three sites and survives at a fourth. Because the
surviving instance sits in the summary paragraph a reader consults for the
headline status of R2 — and because it is the *stronger* of the two claims — this
is the version a skimming referee will carry away.

**Required.** Delete the clause, or replace with the accurate statement: "…and the
*birefringence* amplitude is bounded by the explicit budget of Eq. (2) regardless
of that O(1) normalization." Then grep the whole manuscript for every remaining
sentence that attaches "NDA" or "single-scale bound" to Eq. (1) rather than to the
O1–O6 list.

---

### MAJOR-3 [correctness] — Abstract asserts all fourteen constraints close routes; two entries state in the body that they close nothing

**Anchor.** Abstract, p.1 (300 DPI verified):

> …we catalog fourteen distinct mechanism-class constraints — one per catalog
> entry, none a logical consequence of another — spanning seven foundational
> mechanism classes and six observational-channel branches, **each closing one or
> more of the four routes** by which the ECH bounce could plausibly source a Λ-like
> late-time density.

The universal quantifier is falsified by the paper's own entries:

- **B14**, p.6: "**B14 is not, and is not used as, a closure of the fermionic or
  one-loop content of any route.**" Its stated content for R2–R4 is that their
  *classical zero-spin* baseline is inert — which, since all three routes are
  *defined* by quantum or non-minimal content, closes none of them. The
  v1C.0.13 note is explicit that B14 "removes those routes' CLASSICAL zero-spin
  perturbative baseline, not their quantum/fermionic content."
- **B9**, p.4: "It is **not** an independent bound on the one-loop amplitude…
  so B9 is **never used as a stand-alone closure**."

So at least two of the fourteen do not close any route, by the manuscript's own
careful statements. The abstract is the one place in the paper where this
carefulness lapses, and it lapses in the direction of overclaiming — the
specific failure mode Sec. III's preamble, Sec. VI, and Table II were all written
to prevent.

**Required.** Rescope the abstract clause to what the body supports, e.g.
"…each bearing on one or more of the four routes" or "…which jointly close the
four routes by which…". The fourteen-count itself is fine and well defended; only
the per-entry closure claim is not.

---

### MAJOR-4 [correctness] — App. C asserts uniqueness for exactly the case its cited artifact declares non-unique

**Anchor.** App. C, p.20 (400 DPI crop verified):

> This coefficient set is independently verified by explicit 4×4 Dirac-matrix
> construction in both metric signatures and an exact Grassmann-algebra derivation
> of the operator row (**the unique solution for identical fields**); see the
> released verification artifact and its report listed in the Data and Code
> Availability statement.

The cited artifact is `research/theory_audit/fierz_adjudication_2026_08_05.md`,
listed at p.16. Its closing **Caveat** section (lines 79–82) states the opposite:

> For a single species the five quartics obey two exact linear relations (rank 3)
> [L10], so *identical-field* rearrangement rows are **not unique** — the declared
> direct-channel convention is what fixes the mean-field G_s. The canonical
> **distinct-field** operator row, **which is unique**, is P1A's row.

And the artifact's own result line (27–29) attaches uniqueness to the distinct-field
construction: "Operator (anticommuting) axial row, derived by the exact Grassmann
engine on **four distinct fields (unique solution)**".

The manuscript has transposed the qualifier: the artifact proves uniqueness for
*distinct* fields and explicitly denies it for *identical* fields; the paper claims
it for *identical* fields. The artifact does confirm (line 44) that the row is "a
valid identical-field Grassmann identity" — so the row is right, and nothing
downstream moves: G_s = −3κ/16 is correct (I verified the bridge 4πG = κ/2,
−(3/2)πG = −3κ/16 independently), and the artifact confirms the
convention-independent content of the lemma "holds in every tested convention".

But the word "unique" is doing rhetorical work here — it is offered as evidence
that the coefficient set is *forced* rather than convention-selected, immediately
after a convention note conceding that "Individual Fierz coefficients are
convention-dependent". A referee checking whether the paper's claims exceed its
released artifacts finds, at this one site, that they do.

**Required.** Change to "…the unique solution for four distinct fields, and an
exact identical-field Grassmann identity", which is what the artifact establishes,
and is if anything a cleaner statement. Optionally carry the artifact's rank-3
caveat, since the paper is elsewhere scrupulous about exactly this kind of
non-uniqueness.

---

## MINOR FINDINGS

### MINOR-1 [correctness] — "roughly 1.5 orders" is inconsistent with the two components stated in the same sentence

p.7, right column (300 DPI verified):

> …the one-loop factor 1/16π² and the O(1) coefficient β(γ) are conservatively
> dropped, their *net* effect being a further suppression of **roughly 1.5 orders**
> — the loop factor supplies **−2.2 orders** against β(γ) ≈ 3.3's **+0.5**…

−2.2 + 0.5 = −1.7, not −1.5. Exactly: log₁₀(1/16π²) = −2.198, log₁₀(3.3) = +0.519,
sum −1.679. The stated components are both correct; only the sum is wrong. Since the
sentence exists specifically to show the arithmetic, quote 1.7. (Conservative
direction is unaffected and no margin changes.)

### MINOR-2 [correctness] — App. D Step 2 asserts the kernel lemma it needs, rather than proving it

p.21, Proof step (2): "the zero scalar source therefore gives e^[I ∧ T^J] = 0,
**whose invertible-tetrad kernel is trivial: T^I = 0.**"

The triviality of the kernel of T ↦ e^[I ∧ T^J] at invertible tetrad is a standard
Einstein–Cartan lemma, but it is asserted, not shown — and it is the load-bearing
step of the manuscript's *sole* Tier-I result, inside an appendix whose entire
stated purpose (p.21) is "So that the catalog's sole Tier-I leg can be refereed
from this manuscript." A referee cannot verify the Tier-I claim from this
manuscript alone as long as this step is a citation-free assertion. Supply the
two-line index argument (decompose T^I into irreps, note the wedge map is injective
on each for invertible e), or cite it explicitly.

### MINOR-3 [presentation] — App. D defers a "tensor-sector extension" that its own Statement already claims

The Statement (p.21) asserts "scalar equations and **tensor evolution operators**
coincide with those of general relativity at every perturbative order". The
appendix preamble says "The **tensor-sector extension**, the explicit second-order
Holst-term verification, and the discussion of what would break the transparency
are given in full in the companion."

If the reduced action is exactly the Einstein–scalar action (which Steps 1–4
establish), the tensor conclusion is an immediate corollary and nothing is
deferred. If something genuinely is deferred, then the Tier-I claim as stated
exceeds what App. D proves. State which — one clause resolves it, and given that
this is the paper's only Tier-I leg, the ambiguity is worth removing.

### MINOR-4 [presentation] — Branch→entry multiplicity is never stated, and the 7+6→14 arithmetic closes only implicitly

p.3 states "We tested 7 foundation mechanism classes… and 6 additional
observational channels (Branches H, J, L, M, N, O…)" and "**Each test yielded a
named structural constraint**" — which reads as 13 tests → 13 constraints. The
count reaches 14 only because Branch H carries two entries, which the parenthetical
does flag. But Table I (p.5) additionally assigns B11 to "Branch L/M" and B13 to
"Branches N/O", so branches L, M, N, O carry four entries between them and neither
N nor O has a dedicated constraint. The bookkeeping is in fact consistent
(7 + 2 + 1 + 1 + 1 + 1 + 1 = 14), but the reader has to reconstruct it from the
table. Add one sentence giving the multiplicity explicitly. Given that "fourteen"
is a headline number carried in the abstract, intro, Fig. 1 caption, Table I
caption, Sec. VI and Sec. VII, it should be arithmetically legible in one place.

### MINOR-5 [presentation] — Eight labels defined but never referenced; App. E's displays are numbered but orphaned

`sec:barrier_details`, `app:contact_coeff`, `app:r1_benchmark`, `eq:Seff_dim4`,
`eq:holst_cartan_inverse_p1c`, `eq:fmt_contorsion_p1c`, `eq:fmt_bridge_p1c`,
`eq:r1_benchmark_p1c`. The last four are all of App. E's numbered displays —
i.e. the entire self-contained companion-input appendix consists of equations that
carry numbers but are never pointed at from anywhere. Either cross-reference them
from Sec. II and Table II (where their content is used) or unnumber them.

### MINOR-6 [presentation] — Stale source comment contradicts the closed v1C.0.13 scoping (source only, not printed)

`main.tex:687`, inside the Fig. 1 TikZ block:
`%% --- B14 (Branch H) constrains all four routes [R1--R4]; …`

The v1C.0.13 closure narrowed B14's tag to [R2–R4, zero-spin branch], and the
drawn arrows and in-figure labels are correct (H→R1 labelled "B8"; H→R2/R3/R4
labelled "B14" — verified in the p.5 render). **This is not a defect in the
compiled PDF** and I do not count it against the manuscript. Flagging it only
because it is a live landmine for whoever edits that figure next.

---

## CORRECTNESS LEDGER — 30 relations independently recomputed

Verified correct (✓ = reproduced by independent calculation, not by reading the paper's own justification):

**Conventions / tensor algebra.** ε_abcd ε^abce = −3!δ^e_d consistent with mostly-plus
and ε^0123 = +1 ✓ · S_abc S^abc = −(3/8)(J⁵·J⁵) ✓ · T_abc T^abc = −(3/8)κ²(J⁵·J⁵) ✓ ·
O5 → −(3/2)κ(J⁵·J⁵) ✓ (rederived from ε^μνρσ ε_ρμνd via cyclic reordering) ·
O4 ≡ 0 under purely axial Cartan torsion ✓ (rederived via ε^ρσμν ε^λ_dμν contraction;
both surviving terms vanish by ε contracted on a repeated index) · O4 = 0 on the pure
vector part ✓ · torsion irrep count 4+4+16 = 24 ✓ · Q_γ⁻¹ = [γ²/(1+γ²)](γ⁻¹𝟙 − ⋆) ✓
by direct multiplication using ⋆² = −𝟙.

**Fierz sector (App. C).** F_c² = 𝟙 — **all 25 entries checked individually** ✓ ·
axial row (−1, −½, 0, −½, +1) ✓ · F_op = −F_c → (1, ½, 0, ½, −1) ✓ ·
(J⁵·J⁵) → SS + ½VV + ½AA − PP ✓ · (F_c)_AS = −1, (F_op)_AS = +1, G_s = −3κ/16 ✓ ·
bridge 4πG = κ/2 and −(3/2)πG = −3κ/16 ✓. All agree with the cited adjudication artifact.

**Route 2.** |Ω₄₄/α₄| = (378+783γ²)/[120(1+γ²)] ✓ (from the printed Ω₄₄, Ω₂₄, α₄) ·
= 3.334 at γ = 0.24 ✓ · monotone in γ², floor 378/120 = 3.15 ✓, O(3)–O(5) for γ ≲ O(1) ✓ ·
Eq. (1) dimension count −1+2+3 = +4 ✓ · Δθ ∼ (α_em/4π)(H₀²/M_Pl)H₀⁻¹ = (α_em/4π)(H₀/M_Pl) ✓ ·
α_em/4π = 5.81×10⁻⁴ ✓ · β_obs = 0.342° = 5.97×10⁻³ rad ✓ · Eq. (2) both algebraic lines ✓ ·
10⁻³·10⁻⁶¹/(10⁻²·6×10⁻³) = 1.7×10⁻⁶⁰ ✓ · direct contraction 1.7×10⁻⁶² ✓, "two additional
orders" ✓ · robustness 58 − 10 = 48 ✓.

**Route 3.** Eq. (4) integrated from μ_UV = 10¹⁶ GeV: with γ² = 0.0576, prefactor
μ²/(4πM_Pl²), Δγ² = 0.2372(μ_UV/M_Pl)² = 1.59×10⁻⁷, **|Δγ/γ| = 1.38×10⁻⁶** ✓ —
independently reproduces the paper's 1.4×10⁻⁶ · γ² = 1 is UV-attractive (dβ/dγ² = −28c < 0) ✓ ·
Δlnγ = 0.25–0.31 ✓, 32/(12π²) = 0.270 ✓, exponentiated 0.29–0.36 ✓ · ln10¹⁶ = 36.8,
ln10¹³ = 29.9 ✓ · H₀/M_Pl = 1.18×10⁻⁶¹ ✓ · 0.3 × 1.18×10⁻⁶¹ = 3.5×10⁻⁶² (∼61 orders) ✓ ·
1.4×10⁻⁶ × 1.18×10⁻⁶¹ = 1.65×10⁻⁶⁷ (∼67 orders) ✓ · 61 − 10 = 51 ✓.

**Appendix A.** B1: (M_Pl/H₀)² ∼ 10¹²², residual (H₀/M_Pl)² ∼ 10⁻¹²² ✓ (correctly
un-inverted) · M_Pl⁴/ρ_Λ = (1.2209×10²⁸ eV)⁴/(2.25×10⁻³ eV)⁴ = **8.669×10¹²²** ≈ 8.7×10¹²² ✓ ·
bare powers of ten → 10¹²⁴ ✓ · N_tot = 122 ln10/3 = 93.6 ≈ 94 ✓ · Case II
(α/M)·M_Pl = 1.22×10⁻² ∼ 10⁻² ✓.

**Appendix E.** κn_ψ² = 8πn_ψ²/M_Pl² with n_ψ = 100 cm⁻³ and ħc = 1.9733×10⁻⁵ eV·cm:
**9.957×10⁻⁸⁰ eV⁴** ≈ 1.0×10⁻⁷⁹ ✓ · /ρ_Λ(2.3 meV) = 3.56×10⁻⁶⁹ ≈ 3.6×10⁻⁶⁹ ✓, 68.45
orders ≈ "68.4" ✓ · ×(3/16) → 1.87×10⁻⁸⁰ ≈ 1.9×10⁻⁸⁰ and 6.7×10⁻⁷⁰ ✓ ·
/ρ_Λ(2.25 meV) = 3.885×10⁻⁶⁹ ≈ 3.9×10⁻⁶⁹ ✓.

**Discrepancies found: 1** (MINOR-1, the 1.5-vs-1.7 orders parenthetical).

---

## CITATION AND PRODUCTION INTEGRITY — clean

- 25 `\cite` keys, 25 `\bibitem`, 25 `references.bib` entries; the three sets are
  identical. **Zero** cited-but-missing, **zero** in-bbl-but-uncited, **zero** unused.
- **Zero** undefined references, **zero** undefined citations, **zero** multiply-defined
  labels, **zero** missing characters, **zero** LaTeX warnings, **zero** refs to
  nonexistent labels.
- **Zero overfull hboxes** — none at any size. 48 underfull hboxes (badness-only,
  revtex float artifacts); none produces a visible defect in the 11 pages I rendered.
- 4 benign pdfTeX duplicate-destination warnings (revtex4-2 + `float` package
  interaction on figure.1/table.1/table.2/table.3).
- 13 BibTeX warnings, all from `DiegoPalazuelos2025` having no `journal` field — correct
  by design, disclosed in the entry's `note` as an arXiv preprint.
- Bibliographic data plausible throughout: all 19 arXiv IDs and 24 DOIs pairwise
  distinct; no placeholders; no duplicate works under different keys. `Benedetti2011`
  (1104.4028, JHEP) vs `BenedettiSpeziale2011run` (1111.0884, J. Phys. Conf. Ser.)
  confirmed genuinely distinct companion papers, correctly used for distinct purposes
  (full analysis vs the Eq.-7 numbering the paper quotes).
- Title block correctly carries no `\date`; version/timestamp live in PDF metadata only.
- Artifact links: 6 `\artifact{}` targets plus a commit pin
  (`1130b7c5e3d2`) and a Zenodo DOI. Not fetched in this review (out of scope for
  the referee leg); the provenance boundary between the Zenodo deposit and the pinned
  commit is stated clearly and honestly at p.16.

---

## ASSESSMENT AGAINST THE ARTIFACT TRAIL

I checked every claim the paper attaches to `operator_basis_adjudication_2026_08_07`
and `fierz_adjudication_2026_08_05` against what those artifacts actually computed.

**Tracking correctly:** rank four, nullity two, the two exact relations O1 = O6 and
O1 = ½O4 − O2, rank two modulo total derivatives, "spanning list, not a linearly
independent basis", O4 ≡ 0 on shell under purely axial torsion, O1 = −O2 on the
T = κS branch with the Bianchi reason correctly branch-restricted to T = 0, O5 →
−(3/2)κ(J⁵·J⁵), G_s = −3κ/16. Table III's Fate/Final columns match the adjudication's
corrected findings. The disclaimer that no script performs the spanning enumeration
is stated at five separate sites and matches the artifacts' own scope statements.
This part of the manuscript is exemplary: I could not find a single place where the
operator-list prose outruns the operator-list computation.

**Not tracking:** the identical-field uniqueness claim (MAJOR-4).

**Note for the record, not a finding against this manuscript:** five artifacts in
`research/theory_audit/` (`dimensional_consistency_report.md`, `model_limit_checks.md`,
`fine_tuning_assessment.md`, `theory_validation_summary.md`,
`parameter_chain_inventory.md`) are dated 2026-03-12, describe a different
manuscript's derivation chain, and are **not cited anywhere in P1C**. I confirmed by
grep that no number or caveat from them is used in P1C. Correct handling — recorded
here only so a later reviewer does not mistake their absence for an omission.

---

## SUMMARY FOR THE BOARD

This manuscript is in materially better computational shape than its verdict
suggests. Thirty independent recomputations produced one rounding slip. The
operator-list argument is honestly scoped, the Fierz sector is correct and matches
its adjudication artifact, the Benedetti–Speziale integration reproduces to two
significant figures, and the appendices' arithmetic is exact. Production quality is
clean — zero overfull boxes, zero undefined references, a fully reconciled bibliography.

What holds it at MAJOR REVISION is a scoping-consistency problem concentrated in
the seams left by the previous revision. The v1C.0.13 MAJOR-2 closure re-homed
Route 2's dark-energy leg on the operator list; in doing so it (a) created a second
Tier-I entry in a table the text six times says has only one, (b) graded that entry
above what the admittedly-unproved spanning assertion can carry, and (c) left one
un-swept sentence still delegating the operator to the NDA bound the same revision
had just concluded does not cover it. Add the abstract's untrue universal
"each closing one or more of the four routes", and the uniqueness word in App. C
that inverts its own cited artifact, and the pattern is consistent: the body of
this paper is more careful than its summary surfaces.

None of the four MAJORs requires retracting or weakening a result. All are
repairable by making the summary statements say what the body already says — which
is the direction that makes the paper *more* defensible, not less. I would expect a
single revision cycle to clear all ten items, and I would expect to recommend
acceptance on that revision.

**Recommendation: MAJOR REVISION.** Re-review required on the Tier-I accounting
(MAJOR-1) and the NDA sweep (MAJOR-2); the remainder are verifiable by inspection.

---

*Report prepared without reference to any prior review of this manuscript. All
printed-math assertions re-rendered at ≥300 DPI before being recorded, per the
standing accuracy requirement for this manuscript. No files were modified; no
commits made.*
