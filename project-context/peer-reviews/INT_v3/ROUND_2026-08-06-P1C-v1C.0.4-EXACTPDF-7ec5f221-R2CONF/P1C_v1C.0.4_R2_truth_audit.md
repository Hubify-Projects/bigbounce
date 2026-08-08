# P1C v1C.0.4 — R2 confirmation-board truth audit (verdict-first) and v1C.0.5 closure record

- **Round:** ROUND_2026-08-06-P1C-v1C.0.4-EXACTPDF-7ec5f221-R2CONF — the R2
  confirmation board on `arxiv/paper1c_nogo_survey/main.tex`, run against the
  R1 disposition ledger
  (`INT_v3/ROUND_2026-08-06-P1C-v1C.0.3-EXACTPDF-85e53832/P1C_v1C.0.3_truth_audit.md`).
- **Exact artifact:** v1C.0.4 PDF, SHA-256
  `7ec5f2218fa26eaf03252142e3576ccd0e76797327f90765f138b242cc6e8055`, 17 pp.
- **Date:** 2026-08-06. Auditor: Claude (Fable 5) orchestrator, per CLAUDE.md
  directives B / H-refined / N. Rule applied: a finding that re-flags an
  R1-dispositioned item is RE-FLAG, not genuinely-new.

## Legs (raw receipts)

| Leg | Model | File | Verdict |
|---|---|---|---|
| Claude INT (Opus-tier subagent) | claude opus | `INT_v3/ROUND_2026-08-06-P1C-v1C.0.4-EXACTPDF-7ec5f221-R2CONF/P1C_claude_r2_leg.md` | **minor-revisions** (1 MAJOR / 4 MINOR) |
| Grok API | grok-4.3 | `ROUND_2026-08-06-P1C-v1C.0.4-EXACTPDF-7ec5f221-R2CONF_P1C_Grok_brutal.md` | **REJECT** (3 ESSENTIAL / 3 MAJOR / 2 MINOR + 3 observations) |
| Gemini API | gemini-3.1-pro-preview | `ROUND_2026-08-06-P1C-v1C.0.4-EXACTPDF-7ec5f221-R2CONF_P1C_Gemini_cosmology.md` | **MAJOR REVISIONS** (2 ESSENTIAL / 1 MAJOR / 2 MINOR / 1 NIT + pass-2: 1 MAJOR, 1 MINOR) |

**Failed legs (preserved as failure evidence, never counted, never hidden):**

- Perplexity leg: FAILED
  (`ROUND_2026-08-06-P1C-v1C.0.4-EXACTPDF-7ec5f221-R2CONF_P1C_Perplexity_citations.md`
  is a failure record). Optional leg per directive I1; recorded as failed,
  never a verdict.

## Deduplicated finding ledger (canonical items, cross-leg map, verdicts)

Verdict key: **GNR** = genuinely-new-real (real edit owed and landed in
v1C.0.5) · **RE-FLAG** = re-flag of an R1-dispositioned or disclosed item ·
**SCOPE-OPINION** = venue/style/packaging position, dispositioned ·
**FALSIFIED** = disproved against the cited source line.

### R2-GNR-1 — B10 classified as both "ECH-specific calculation" and "not an ECH-specific calculation"
- Legs: Claude MAJOR-1 (sole leg; cross-checked true against the PDF).
- Verdict: **GNR** (the round's headline; internal self-contradiction in the
  paper's central classification apparatus). Sec. III preamble and Sec. VI
  list B10 among the "general naturalness or classification arguments ...
  rather than sharp ECH-specific calculations," and B10's own entry tag says
  "(General naturalness argument.)" — yet the *Constraint classification*
  list defined "Novel results (Barriers 1, 2, 3, 4, 8, 10, 11, 12, 14)" as
  "ECH-specific calculations not immediate consequences of prior
  literature." The contradiction is inherited verbatim from the frozen
  monolith (`arxiv/paper1_unified.tex` line ~3590 has the identical
  descriptor; B10's tag at line ~3766 identically says general naturalness).
- Closure (v1C.0.5): the Novel-results descriptor now decouples novelty
  (provenance: first formulated within the ECH analysis) from
  ECH-specificity: "eight of the nine are ECH-specific calculations, while
  B10 is a general naturalness dilemma first articulated in this catalog in
  the ECH-bridge context," with an explicit consistency pointer to the
  preamble, B10's entry tag, and Sec.~VI. B10 stays in the Novel list (it
  *is* first-formulated-here), and all four surfaces now agree on the
  predicate. No counting changes (Novel 9 + Known 4 + Structural 1 = 14
  unchanged).

### R2-GNR-2 — O4 schematic ε_{IJKL}T^{IJ}T^{KL} does not typecheck
- Legs: Claude MINOR-1.
- Verdict: **GNR**. The torsion two-form T^I carries ONE internal index
  (component tensor T^{abc} = κS^{abc}, Sec. II); no two-internal-index
  T^{IJ} is defined anywhere, so the printed invariant cannot be contracted
  as shown. The broken schematic is inherited verbatim from the monolith
  (lines ~1886, ~4828) — the monolith's "actual form" is the same
  non-parsing expression, so a correctly-indexed schematic of the same
  operator is owed (never a new operator).
- Closure (v1C.0.5): O4 re-indexed in Eq. (8) and Table III to the parsing
  component form ε^{μνρσ}T^{I}{}_{μν}T_{Iρσ} — i.e. the single-internal-
  contraction invariant T_I∧T^I, the torsion piece of the Nieh–Yan identity
  d(e_I∧T^I) = T_I∧T^I − e_I∧e_J∧R^{IJ} that the paper already quotes
  [NiehYan1982] — with a one-sentence definition added after Eq. (8) stating
  the single-internal-index structure. The fate column ("→ κ²(J⁵·J⁵), Fierz
  basis" — a Fierz-class upper bound at the κ² power) is unchanged; a
  numerical spot-check performed for this audit (scratchpad `o4check.py`,
  `o4check2.py`) confirms the ε-contracted quadratic in the axial-dual
  torsion is bounded by (indeed lands inside, with coefficient ≤ O(1)) the
  κ²(J⁵·J⁵) Fierz class claimed, so the no-go direction of the tabulated
  fate is safe. Check D's verified identity S_{abc}S^{abc} = −(3/8)(J⁵·J⁵)
  is untouched.

### R2-GNR-3 — App. C cross-reference drops the γ²/(1+γ²) factor in G_s
- Legs: Claude MINOR-2; Gemini P1C-N2 (dedupe — same defect, same fix).
- Verdict: **GNR**. App. C said the Fierz chain gives "the mean-field
  scalar-channel coupling G_s = −3κ/16 quoted in Sec. II," but Sec. II
  quotes −(3κ/16)[γ²/(1+γ²)](J⁵)². Source of truth: published P1A
  (`arxiv/paper1a_ech_nogo.tex`), whose gap-equation convention takes
  G_s = −3κ/16 deliberately *without* the finite-Holst factor because
  γ²/(1+γ²) < 1 "can only reduce the coupling" (P1A Eq. minimal_contact and
  fierz_scalar_bridge; abstract states the omission explicitly).
- Closure (v1C.0.5): App. C now states the Fierz rearrangement supplies only
  the γ-independent channel factor −3κ/16 (the companion's gap-equation
  convention, conservative, equivalently the γ→∞ limit), while the
  γ²/(1+γ²) prefactor of the Sec. II operator arises from the Cartan
  torsion elimination, not the Fierz step — cited to P1A. This was a defect
  *introduced by the R1 GNR-1 closure* (the scalar-bridge sentence was added
  in v1C.0.4), hence genuinely new at R2.

### R2-GNR-4 — Table II R1 row's "∼70 orders below ρ_Λ" had no anchor in this manuscript
- Legs: Claude MINOR-3.
- Verdict: **GNR**. The figure was imported without derivation or pointer;
  moreover published P1A's own Table II states the sharper "68.45 orders"
  via the coefficient-one benchmark κn_ψ²/ρ_Λ ≃ 3.6×10⁻⁶⁹ (n_ψ/100 cm⁻³)²
  (P1A lines ~1210, ~2695–2706, ~3392), so "∼70" was also a loose rounding
  of the published companion value.
- Closure (v1C.0.5): Table II R1 cell now carries the P1A-published
  benchmark and scaling — κn_ψ²/ρ_Λ ≃ 3.6×10⁻⁶⁹ (n_ψ/100 cm⁻³)², i.e. ≈68
  orders below ρ_Λ even at a deliberately elevated ISM-like normalization —
  cited to [1]. Aligned with, not invented beyond, the published companion.

### R2-GNR-5 — Provenance of the 0.27 lower edge of ρ_crit/ρ_Pl ≃ 0.27–0.41
- Legs: Claude MINOR-4.
- Verdict: **GNR**. Ashtekar–Singh quote the canonical ρ_c ≈ 0.41 ρ_Pl at
  γ = 0.2375 only; 0.27 is an internal extrapolation. Published P1A
  establishes exactly this (P1A eq:rhocrit paragraph, lines ~2110–2120:
  "0.27 ... is an internal extrapolation across counting schemes (not a
  value quoted in Ref. [Ashtekar2011]) ... scheme-dependent range rather
  than a published LQC range"; closure history: P1A PER-m1).
- Closure (v1C.0.5): B12 now states both endpoints' provenance — 0.41 =
  Ashtekar–Singh canonical at γ = 0.2375 [4]; 0.27 = SU(2)
  black-hole-entropy γ ≈ 0.274 substituted into the same
  ρ_crit = √3/(32π²γ³) ρ_Pl formula, an internal extrapolation established
  in the companion [1], not a value quoted in [4]; window labeled
  scheme-dependent. Carried verbatim-faithful from P1A; the derived
  Ω_GW ≲ 0.07–0.17 band is unchanged (0.27² = 0.073, 0.41² = 0.168, both
  legs verified).

### R2-GNR-6 — Table III "Fate" column reads as dimensionally inconsistent without the bare-invariant note
- Legs: Gemini P1C-N3 and pass-2 m1 (same item, flagged twice by the same
  leg).
- Verdict: **GNR** (caption-locality clarity). The body text above the table
  already states that the Fate column records the bare-invariant reduction
  and that restoring prefactors gives O4 = O5 = κ(J⁵·J⁵) via M_Pl²κ² = κ —
  but the caption did not, so a table-only reader sees a dim-4 operator with
  a κ²(J⁵·J⁵) fate.
- Closure (v1C.0.5): caption now states "The 'Fate' column records the
  reduction of the *bare* invariant, prior to multiplication by the
  prefactor; restoring the prefactor, the two genuine dimension-4 densities
  O4 and O5 both land on κ(J⁵·J⁵) [M_Pl²κ² = κ; see text]." Content carried
  from the paper's own adjacent text; nothing new.

### R2-GNR-7 — Eq. (2) denominator reads as a double division (angle AND R4 coupling)
- Legs: Gemini pass-2 P1C-M2.
- Verdict: **GNR as a clarity/labeling defect; the demanded margin change is
  NOT owed.** Gemini's description of the printed formula is correct: the
  denominator carries both β_obs and M_Pl(α/M) while the LHS is labeled
  Δθ_one-loop/Δθ_obs, and the direct angle-to-angle contraction
  (α_em/4π)(H₀/M_Pl)/β_obs ≈ 2×10⁻⁶² indeed differs by two orders. But the
  direction is *conservative*: the printed ~10⁻⁶⁰ claims LESS suppression
  than Gemini's corrected 10⁻⁶², so the quoted margin ("≈60, conservatively
  ≥58") holds a fortiori under either contraction — Gemini's own note
  concedes correcting it "only strengthens the author's qualitative
  conclusion." The contraction-ordering freedom of this Tier-III ansatz was
  already disclosed ("canonical evaluation of the displayed contraction ...
  an alternative ordering ... yields a deliberately loose ~10⁻³³ upper
  bound"), and the Claude R2 leg independently verified the printed
  evaluation as dimensionless and internally consistent. What was owed and
  missing: an explicit statement of what each denominator factor does.
- Closure (v1C.0.5): a passage now states each denominator factor's role
  explicitly — the ratio normalizes the one-loop amplitude both by the
  observed angle and by the dimensionless R4-fitted coupling strength
  M_Pl(α/M) ~ 10⁻² (the fitted-coupling benchmark, the weaker/conservative
  normalization) — and displays the direct angle-only contraction
  ≈ 2×10⁻⁶² ("two additional orders of suppression"), so the quoted ~10⁻⁶⁰
  is identified as the conservative side of the bookkeeping choice and "the
  closure holds a fortiori under either contraction." All downstream margins
  (≈60 / ≥58) unchanged at every surface — no number was weakened or
  strengthened, only explained.

### R2-RF-1 — Version string "(v1C.0.4)" on the title page
- Legs: Grok P1C-E1; Gemini P1C-E2.
- Verdict: **RE-FLAG** of R1 SO-1 (dispositioned): the (Dated: ... vX.Y.Z)
  stamp is required by standing directive G on every served draft and is
  stripped at P-round submission packaging. No in-draft edit owed.

### R2-RF-2 — "Not self-contained; companion imports; withdraw or reproduce everything"
- Legs: Grok P1C-E2; Gemini P1C-E1 (incl. the Zenodo-sequencing demand).
- Verdict: **RE-FLAG** of R1 GNR-2's closure + disposition: the sole
  Tier-I leg (B14) is stated and proved self-contained in App. D as of
  v1C.0.4; the remaining imports (Cartan elimination, R4 derivation) are
  honestly cited to a public immutable archive (Zenodo DOI
  10.5281/zenodo.21481838) with explicit "not peer reviewed" disclosure, and
  reproducing all of P1A would duplicate a published companion. The
  companion-sequencing demand (publish P1A first) is a publishing-phase
  matter (directive P), not a manuscript defect.

### R2-RF-3 — "Abstract margins never recomputed in this text"
- Legs: Grok P1C-E3.
- Verdict: **RE-FLAG** of R1 FAL-2 (falsified there with line citations):
  the body displays the complete Route-2 arithmetic chain (Eq. (2) with all
  numeric inputs) and the Route-3 integration inputs; the Claude R2 leg
  independently reproduced every displayed number from the in-paper inputs
  (verification log items 1–3).

### R2-RF-4 — "Embed the full enumeration or retract the completeness claim"
- Legs: Grok P1C-M2 (verbatim recurrence of R1 Grok E3).
- Verdict: **RE-FLAG** of R1 RF-1: completeness is asserted from stated
  construction rules and disclosed as not established by exhaustive
  enumeration at every surface; the released script is honestly scoped to
  the two reduction identities. The "script post-dates the paper version"
  sub-claim is addressed by the immutable commit pin (R1 GNR-9,
  9b92721d5d7e) stated in Data & Code Availability.

### R2-RF-5 — "Budgets are order-of-magnitude estimates; display hidden O(1)s; sensitivity analysis"
- Legs: Grok P1C-M3.
- Verdict: **RE-FLAG** of R1 RF-2 / disclosed Tier-III status: R2/R3 are
  explicitly labeled "(III) Ansatz-level ... exploratory, not load-bearing"
  in Table II and text; the O(1) Immirzi-rational coefficient IS displayed
  (|Ω₄₄/α₄| ≈ 3.3 at γ ≈ 0.24, O(1)–O(5) across γ ≲ O(1)) with the
  robustness statement that even a 10¹⁰ inflation leaves ≳48 orders.

### R2-RF-6 — "B8 is a redundant node; merge or flag subsumed entries"
- Legs: Grok P1C-N2.
- Verdict: **RE-FLAG** of R1 FAL-1: the requested flagging already exists
  identically at every surface (abstract, Sec. III, Table I caption, Fig. 1
  caption, conclusions); the 13-distinct/14-historical accounting is
  uniform (verified again by the Claude R2 leg's consistency log).

### R2-RF-7 — "17 pp; CQG survey norm 8–10 pp; no new first-principles calculation"
- Legs: Grok additional observation.
- Verdict: **RE-FLAG** of R1 GNR-3's recorded residual: venue-length
  condensation is standing D/P-round work; "no new calculation" is the
  paper's own honest framing (survey/consolidation with amplitude-budget
  closures), per the R1 disposition.

### R2-RF-8 — "B5–B7, B13 general arguments inflate the catalog"
- Legs: Grok additional observation.
- Verdict: **RE-FLAG** of disclosed content: the Sec. III preamble and
  Sec. VI say exactly this themselves ("general naturalness or
  classification arguments that apply to broad classes ... of mixed
  individual strength"); inclusion is the stated design (systematic
  coverage), with strength never overclaimed.

### R2-RF-9 — "theory_audit internal-bookkeeping paths in the published text"
- Legs: Gemini P1C-N1.
- Verdict: **RE-FLAG** of R1 SO-1 (paths kernel): repo-relative committed
  artifact paths are the lab's reproducibility standard and published-P1A
  precedent, additionally commit-pinned (R1 GNR-9). No edit owed at
  R-round; naming cosmetics can be revisited at P-round packaging.

### R2-SO-1 — "Replace the three-tier taxonomy with standard mathematical language"
- Legs: Grok P1C-M1.
- Verdict: **SCOPE-OPINION.** The tier scale is explicitly defined
  (Sec. IV, "Evidentiary status of each leg": Tier I = deductive
  consequence of stated equations within bounded scope; Tier II =
  structural argument not turning on a fitted number; Tier III =
  ansatz-level dimensional estimate), applied uniformly in Table II, and
  exists precisely so rigor is NOT overclaimed — replacing "Tier-III
  ansatz-level estimate" with "theorem/lemma" vocabulary would overstate,
  not clarify. Terminology preference, dispositioned.

### R2-SO-2 — "Mint a separate Zenodo DOI for this paper's own scripts"
- Legs: Gemini P1C-M1.
- Verdict: **SCOPE-OPINION (venue/packaging; deferred-genuine).** A
  reasonable archival-practice request, but it is a P-round packaging
  action (external deposit), not a manuscript defect: Data & Code
  Availability honestly states exactly what is commit-pinned (this paper's
  scripts, immutable commit 9b92721d5d7e) and what is DOI-archived (the
  companion + its scripts, 10.5281/zenodo.21481838). Recorded on the
  pre-submission checklist: mint a version DOI for the P1C script set at
  P-round, matching the companion's standard.

### R2-FAL-1 — "No clear decision procedure for the three evidentiary labels"
- Legs: Grok P1C-N1.
- Verdict: **FALSIFIED.** The decision rubric is printed in Sec. IV
  ("Evidentiary status of each leg" paragraph): each tier is defined by an
  explicit criterion (deductive consequence within bounded scope /
  qualitative-structural not turning on a fitted number / amplitude budget
  under an explicitly-labeled ansatz), and every Table II cell states which
  criterion the leg meets and why. Source: v1C.0.4 PDF p. 8–9; `main.tex`
  (v1C.0.4) lines ~957–975.

### R2-FAL-2 — "Several arXiv preprints' DOIs are 'concept DOI' placeholders"
- Legs: Grok additional observation.
- Verdict: **FALSIFIED.** No arXiv-preprint entry carries a concept-DOI
  placeholder. The only concept DOIs appear parenthetically in the two
  Zenodo companion entries ([1], [13]), which are Zenodo deposits (explicitly
  disclosed "not an arXiv preprint and not peer reviewed") and whose primary
  citation is the immutable *version* DOI (10.5281/zenodo.21481838,
  10.5281/zenodo.21481842). Source: `references.bib` lines 112, 121;
  rendered bibliography p. 17–18.

## Ledger totals

| Verdict | Count | Items |
|---|---|---|
| GENUINELY-NEW-REAL (closed in v1C.0.5) | **7** | R2-GNR-1 … R2-GNR-7 |
| RE-FLAG (R1-dispositioned / disclosed; source-cited) | 9 | R2-RF-1 … R2-RF-9 |
| SCOPE-OPINION (venue/packaging; dispositioned) | 2 | R2-SO-1, R2-SO-2 |
| FALSIFIED (source-cited) | 2 | R2-FAL-1, R2-FAL-2 |
| **Total canonical items** | **20** | (Claude MINOR-2 ≡ Gemini N2; Gemini N3 ≡ pass-2 m1; Grok E1 ≡ Gemini E2; Grok E2 ≡ Gemini E1) |

Deferred-genuine (pre-submission checklist additions this round):
1. Mint a version DOI for the P1C script set at P-round packaging (R2-SO-2).
2. (Carried from R1) ST Eq. (58) + verbatim-quote verification against the
   published CQG PDF; venue-length condensation (D/P rounds).

## Closure evidence (v1C.0.5)

- All 7 GNR closures landed in `arxiv/paper1c_nogo_survey/main.tex`
  (\paperVersion v1C.0.5, dated 2026-08-06). Correction sources: published
  P1A `arxiv/paper1a_ech_nogo.tex` (G_s gap-equation convention; 3.6×10⁻⁶⁹
  benchmark; 0.27–0.41 scheme provenance), the frozen monolith
  `arxiv/paper1_unified.tex` (B10/O4 inheritance verified), the Nieh–Yan
  identity already cited in-paper [NiehYan1982], and direct arithmetic from
  the paper's own displayed inputs (Eq. (2) direct contraction ≈ 2×10⁻⁶²).
  Nothing invented; no margin, count, or headline number changed.
- Compile: pdflatex 4-pass, **0 errors / 0 undefined references / 0 overfull
  hboxes**, 18 pages.
- /latex-audit visual pass: all 18 pages rendered at 110 DPI and inspected —
  title block shows v1C.0.5, Sec. III classification, B12 window, Eq. (2)
  passage, Table II R1 row, Eq. (8) + definitional sentence, Table III +
  caption, App. C bridge all render clean; no column overflow, no overlap.
  No new URLs added; all cited artifact paths previously verified to resolve
  (Claude R2 leg repository-artifacts check).
- Mirrors byte-identical (md5 `36312efb1737119e22c5581da2980f02`):
  `arxiv/paper1c_nogo_survey/main.pdf` =
  `site/public/papers/paper1c_nogo_survey_v1C.0.5.pdf` =
  `public/papers/paper1c_nogo_survey_v1C.0.5.pdf`.
  SHA-256 `a770491d56d1e02adb8318fd423a4886f3a479270f03b8cfb3ad1a4e8d96bb74`.
- Site: `site/src/data/papers.ts` supportingLinks href → v1C.0.5 (+ honest
  description); `site/src/data/reviewTimeline.ts` R2 round entry (failed
  Perplexity leg disclosed); `project-context/draft_paper_registry.json`
  served_aliases → v1C.0.5. `npx next build` passes (see docs commit).

## Convergence read (directive H-refined)

R2 surfaced **7 genuinely-new-real findings** (target: 0). The paper is
therefore **NOT converged**: an **R3 confirmation board on the exact
v1C.0.5 PDF (sha `a770491d…`)** is required, with all active legs re-run
fresh and the exit test again 0 genuinely-new-real. Context for calibration,
not for verdict-softening: 5 of the 7 were single-leg minor-grade
consistency/traceability items, 1 (R2-GNR-3) was introduced by an R1
closure, and 1 (R2-GNR-7) was a conservative-direction labeling defect —
but the count is the count, and the gate is honest.
