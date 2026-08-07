# P1C status — current authoritative section

**Current candidate:** draft v1C.0.12 · 2026-08-07 ·
`arxiv/paper1c_nogo_survey/main.tex`

**Status: R9 CORRECTNESS-CONVERGENCE BOARD RUN AND TRUTH-AUDITED, WITH AN
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

v1C.0.11: 20 pp, 0 errors, 0 undefined refs, 0 overfull hboxes, compiled
clean 2026-08-07 (`arxiv/paper1c_nogo_survey/main.pdf`). Mirrored
byte-identical to `site/public/papers/paper1c_nogo_survey_v1C.0.11.pdf` and
`public/papers/paper1c_nogo_survey_v1C.0.11.pdf` (md5
`4723faef2f210e4b81c33b21d55bfdeb`, sha256 `0868856032…`, all three copies
match). Prior v1C.0.1–v1C.0.10 mirrors retained. `/latex-audit` visual pass
on the recompile: changed pages rendered at 110 DPI — title block
(v1C.0.11 stamp, August 7, 2026, p. 1), B12 with the new Ghosh–Mitra
citation (p. 5), the proceedings-summary credit line + Δln γ band with
the identification note (p. 8), the 1.2209 hierarchy quotient (p. 15) —
no overflow/overlap. New URLs both verified live for this round: the
GhoshMitra2005 DOI (10.1016/j.physletb.2005.05.003, Crossref-resolved to
the exact title/authors/volume/pages) and its arXiv abstract page
(gr-qc/0411035). Reference numbering shifted by the insertion
(Ghosh–Mitra is [5]; later entries renumber automatically).

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
10. **R9 confirmation board — THE CORRECTNESS-CONVERGENCE CHECK** (same
   three active legs, fresh, on the exact v1C.0.11 PDF sha
   `0868856032…`). Exit test per the R8 classification rule: a full
   board whose truth audit yields ZERO correctness-grade GNR converges
   the R-phase; presentation-grade items route to the D-round.
   Pre-submission checklist carries: real mechanized enumeration (or
   keep downgraded framing); ST Eq. 58 + quote verification;
   venue-length condensation + abstract compression + tier-disclaimer
   consolidation (seven instances counted at R8); mint the version DOI /
   updated archival deposit for the P1C script set at P-round (R2-SO-2 /
   R5-GNR-2 / R6-RF-9 / R7-RF-8 / R8-RF-11); refereed-companion gate for
   the cited-only companion results (R6-GNR-1 / R7-RF-9 / R8-RF-10).
11. D/P rounds (visual + packaging) only after INT/EXT convergence, per the
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
