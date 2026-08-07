# P1C v1C.0.5 — R3 confirmation-board truth audit (verdict-first) and v1C.0.6 closure record

- **Round:** ROUND_2026-08-06-P1C-v1C.0.5-EXACTPDF-a770491d-R3CONF — the R3
  confirmation board on `arxiv/paper1c_nogo_survey/main.tex`, run against the
  R1 + R2 disposition ledgers
  (`INT_v3/ROUND_2026-08-06-P1C-v1C.0.3-EXACTPDF-85e53832/P1C_v1C.0.3_truth_audit.md`,
  `INT_v3/ROUND_2026-08-06-P1C-v1C.0.4-EXACTPDF-7ec5f221-R2CONF/P1C_v1C.0.4_R2_truth_audit.md`).
- **Exact artifact:** v1C.0.5 PDF, SHA-256
  `a770491d56d1e02adb8318fd423a4886f3a479270f03b8cfb3ad1a4e8d96bb74`, 18 pp.
- **Date:** 2026-08-06. Auditor: Claude (Fable 5) orchestrator, per CLAUDE.md
  directives B / H-refined / N. Rule applied: a finding that re-flags an
  R1/R2-dispositioned item is RE-FLAG unless the reviewer adds a genuinely
  new angle.

## Legs (raw receipts)

| Leg | Model | File | Verdict |
|---|---|---|---|
| Claude INT (Opus-tier subagent) | claude opus | `INT_v3/ROUND_2026-08-06-P1C-v1C.0.5-EXACTPDF-a770491d-R3CONF/P1C_claude_r3_leg.md` | **minor-revisions** (1 MAJOR / 7 MINOR) |
| Grok API | grok-4.3 | `ROUND_2026-08-06-P1C-v1C.0.5-EXACTPDF-a770491d-R3CONF_P1C_Grok_brutal.md` | **REJECT** (3 ESSENTIAL / 3 MAJOR / 1 MINOR / 1 NIT + 3 observations) |
| Gemini API | gemini-3.1-pro-preview | `ROUND_2026-08-06-P1C-v1C.0.5-EXACTPDF-a770491d-R3CONF_P1C_Gemini_cosmology.md` | **MAJOR REVISIONS** (2 ESSENTIAL / 2 MAJOR / 1 MINOR / 2 NIT) |

**Failed legs (preserved as failure evidence, never counted, never hidden):**

- Perplexity leg: FAILED
  (`ROUND_2026-08-06-P1C-v1C.0.5-EXACTPDF-a770491d-R3CONF_P1C_Perplexity_citations.md`
  is a failure record). Optional leg per directive I1; recorded as failed,
  never a verdict.

## Deduplicated finding ledger (canonical items, cross-leg map, verdicts)

Verdict key: **GNR** = genuinely-new-real (real edit owed and landed in
v1C.0.6) · **RE-FLAG** = re-flag of an R1/R2-dispositioned or disclosed item ·
**SCOPE-OPINION** = venue/style position, dispositioned · **FALSIFIED** =
disproved against the cited source line.

### R3-GNR-1 — Completeness framing exceeded what is verified (the round's headline; adjudicated to option (b): wording downgrade)
- Legs: Claude MAJOR-1 (enumeration is finite/mechanizable; script filename
  says "enumeration" but the script does not enumerate); Grok P1C-M1 kernel
  (enumeration verification not reproduced in manuscript).
- Verdict: **GNR.** The R1 RF-1 / R2-RF-4 disposition ("completeness is
  disclosed as asserted, not proved") stands, but Claude adds two genuinely
  new angles: (i) the claim-adjacent *naming* — "The
  Operator-Basis-Completeness Argument" as section title / contributions
  phrase — advertises more than the disclosed status; (ii) the released
  script `arxiv/scripts/dim4_parityodd_enumeration.py` carries a filename
  and docstring that overclaim ("checks that make the enumeration ...
  rigorous rather than asserted") while performing no enumeration.
- **Adjudication of the (a)-vs-(b) fork (per directive Q1 /
  never-fabricate):** option (a) — actually mechanizing the enumeration —
  was examined and REJECTED for this round. Reasons, recorded honestly:
  the paper's construction rule is partially self-referential ("mass
  dimension exactly four after the explicit M_Pl² promotions of
  Eq. (8)"), so a mechanical enumerator must first formalize which
  promotions are admitted; and the literal rule admits mixed monomial
  content classes at naive dimension 4 (e.g. ε-contracted R·T·T at
  2+1+1 and T⁴ at 1+1+1+1, with physical torsion [T]=+1) whose
  membership/vanishing/reduction is not adjudicated by the printed
  six-member list — under T=κS they reduce to *further*-suppressed
  four-fermion/curvature-current structures, so the no-go direction is
  safe, but a correct enumerator must derive that, which is real
  derivation work (the reviewer's own estimate: days), not a bounded
  mechanical script extension. Shipping a rushed enumerator that asserts
  completeness would be pattern-036 territory (fabricated proof
  artifact). **Chosen: (b)** — downgrade every claim surface to exactly
  what the script verifies, and record the real mechanized enumeration
  as a deferred-genuine pre-submission item.
- Closure (v1C.0.6): Sec. V retitled "The Operator-Basis Argument";
  "operator-basis-completeness argument" replaced by "operator-basis
  argument" at every surface (Sec. I ×3, Sec. VI, conclusions, Data & Code
  Availability), each first-use carrying the explicit rule-asserted
  disclosure; contributions item (ii) now states "(completeness of the
  basis is asserted from the stated construction rule, not proved)";
  App. A1 "enumerate" verbs downgraded to "exhibit" (3 sites); the
  main-text pointer now reads "(which, its filename notwithstanding,
  verifies the two identities and performs no basis enumeration)". The
  released script's docstring and VERDICT output block were edited
  (REAL committed change, same closure commit) to state the honest
  scope: it verifies Checks A and D only; completeness rests on the
  paper's construction rule; no enumeration performed. The script was
  re-run after the edit: both identities still verified, exit 0. The
  filename itself is retained because the Data & Code commit-pin
  (9b92721d5d7e, R1 GNR-9) immutably references it; the Data & Code text
  already stated (v1C.0.5) "None of the scripts performs the basis
  enumeration," and v1C.0.6 adds the pin-drift disclosure "(a later
  revision clarifies the first script's descriptive text only; the
  checks performed and their pass/fail results are identical)".
- Deferred-genuine (pre-submission checklist): implement the real
  mechanized enumeration (formalized promotion clause; mixed R·T·T / T⁴
  classes adjudicated; output cited in-paper) — or keep the downgraded
  framing at submission. Never claim enumeration without the artifact.

### R3-GNR-2 — κ = 8πG = M_Pl⁻² with full-Planck-mass numerics is a strict algebraic contradiction
- Legs: Claude MINOR-3; Gemini P1C-E1 (dedupe — same defect); Grok P1C-N2
  kernel (κ̃/κ mixing; the requested clarifying note already existed in
  Sec. II's first convention flag, so Grok's item folds here for the
  strict-equality kernel only).
- Verdict: **GNR** (two independent legs; genuinely new — no prior round
  flagged it). With M_Pl the full Planck mass (G^{-1/2}), M_Pl⁻² = G and
  "8πG = M_Pl⁻²" is false; the paper defined the full mass two paragraphs
  later. Also true (Claude's sub-finding, verified by recomputation for
  this audit): usage is mixed — κn_ψ²/ρ_Λ reproduces 3.6–3.9×10⁻⁶⁹ only
  with the exact κ=8πG (reduced-mass form; full-mass κ gives 1.5×10⁻⁷⁰),
  while the App. A hierarchy 8.7×10¹²² uses the full mass.
- Closure (v1C.0.6): Sec. II now defines κ ≡ 8πG *exactly*, equal to
  M̄_Pl⁻² with the reduced mass M̄_Pl ≡ (8πG)^{-1/2} ≃ 2.44×10¹⁸ GeV,
  and declares κ ∼ M_Pl⁻² (full mass) an explicit factor-8π
  order-of-magnitude abuse (exactly κ = 8π M_Pl⁻²), never a definition.
  The second convention flag now states the mixed usage site-by-site
  (Table II R1 benchmark = exact κ; App. A hierarchy = full mass; each
  order-of-magnitude only). Every strict "κ=8πG=M_Pl⁻²" /
  "κ=M_Pl⁻²" equality at a full-mass site softened to "∼" (abstract
  Sec. I, App. A1 Cartan line, App. C ×3). No number changed.

### R3-GNR-3 — Abstract/conclusions labeled the whole 61–67-order span "derived"
- Legs: Claude MINOR-2 (sole leg; verified true against the PDF: the body
  itself labels the 61-order endpoint "a deliberately pessimistic upper
  bound ... not a precisely derived value").
- Verdict: **GNR** (labeling honesty; genuinely new — R1 GNR-4 fixed the
  per-route metric, not the endpoint provenance).
- Closure (v1C.0.6): abstract now reads "…61–67 orders … below the
  observed dark-energy density (the ∼67-order endpoint from the derived
  integrated flow, the ∼61-order endpoint from a deliberately pessimistic
  chiral-count bound)"; conclusions now read "bounded between a derived
  integrated renormalization-group-flow estimate (∼67 orders) and a
  deliberately pessimistic chiral-count bound (∼61 orders)". Sec. IV B
  already carried the correct labels; Sec. VI's neutral wording untouched.

### R3-GNR-4 — α_em/(4π) rounding inconsistency in the Route-2 arithmetic
- Legs: Claude MINOR-5 ("≈5×10⁻⁴ rounds the wrong way"); Gemini P1C-M1
  (dedupe — text defines 5×10⁻⁴ then substitutes 10⁻³ twice).
- Verdict: **GNR** (clarity defect, two legs). Recomputation for this
  audit: 5.8×10⁻⁴ rounds to 6×10⁻⁴, and the displayed substitutions do
  use 10⁻³; rounding *up* to 10⁻³ overestimates the numerator, i.e. the
  conservative direction for a suppression claim.
- Closure (v1C.0.6): passage now reads "α_em/(4π) ≈ 6×10⁻⁴ (more
  precisely 5.8×10⁻⁴), rounded *up* to 10⁻³ in the explicit
  order-of-magnitude substitutions below — an overestimate of the
  numerator and hence conservative for the suppression claim". All
  displayed arithmetic (10⁻⁶⁰, 2×10⁻⁶²) unchanged and now internally
  consistent with its stated rounding.

### R3-GNR-5 — Table III Fate column still misleads a table-only reader (R2-GNR-6 caption closure judged insufficient by a fresh leg)
- Legs: Gemini P1C-M2 (explicitly acknowledges the caption explains the
  discrepancy, and finds the presentation still undermines the text's
  O4 = O5 conclusion).
- Verdict: **GNR** (closure-insufficiency is genuinely new information:
  the R2 fix was caption-only; a fresh reader still misread the column).
- Closure (v1C.0.6): a sixth column "Final (×prefactor)" added to
  Table III — O1: 0; O2/O3: 0 (EOM); O4: κ(J⁵·J⁵); O5: κ(J⁵·J⁵); O6: 0 —
  so the table itself shows the two genuine dimension-4 densities landing
  on the same operator; caption updated ("Fate (bare)" / "Final"
  semantics). Rendered and visually verified (p. 16, no overflow).

### R3-GNR-6 — R4 anchor α/M ∼ 10⁻²¹ GeV⁻¹ had no in-paper algebraic origin
- Legs: Gemini P1C-N1 (standalone-reader test; asks for a 1–2-sentence
  origin, not the full companion derivation).
- Verdict: **GNR** (bounded, satisfiable without reproducing the
  companion; distinct from the R2-RF-2 wholesale self-containment
  re-flag because the ask is a two-sentence summary).
- Closure (v1C.0.6): carried verbatim-faithful from the companion's
  published derivation (P1A `sec:r4_birefringence`, Eq. `beta_bound`):
  β = (α/2M)Δφ_rec→today (rotation = half the coupling times the
  coherent excursion), Δφ ∼ √(2ρ_θ)/m_θ ∼ M_Pl for a frozen
  (m_θ ≲ H₀) spectator carrying ρ_θ ∼ ρ_Λ, so α/M ∼ 2β_obs/M_Pl ∼
  10⁻²¹ GeV⁻¹. Numerics verified for this audit: √(2ρ_Λ)/H₀ ≈ 5×10¹⁸
  GeV ≈ M_Pl; 2·(6×10⁻³)/1.22×10¹⁹ ≈ 10⁻²¹ GeV⁻¹. Nothing invented.

### R3-GNR-7 — "Integrand carries dimension −1+2+3=+4" while the prefactor sits outside the integral
- Legs: Gemini P1C-N2 (nit; correct as read — Eq. (1) writes
  β(γ)/M_Pl outside ∫d⁴x, so the literal integrand ∂ϑJ⁵ is dim +5).
- Verdict: **GNR** (wording).
- Closure (v1C.0.6): rephrased to "the full term — the dimension-(+5)
  integrand ∂_μϑ_NY J^{5μ} times the dimension-(−1) prefactor
  β(γ)/M_Pl written outside the integral in Eq. (1) — carries dimension
  −1+2+3 = +4 and the action is dimensionless."

### R3-GNR-8 — Ref. [12] bibliography rendering defect (partial closure of Claude MINOR-7)
- Legs: Claude MINOR-7.
- Verdict: **GNR for the Ref. [12] kernel** ("arXiv preprint␣␣(2025)",
  double space, no journal — caused by a stray `journal = {arXiv
  preprint}` field). Closure (v1C.0.6): field removed from
  `references.bib`; entry now renders "…data release 6, (2025),
  arXiv:2509.13654 [astro-ph.CO]" (verified in the recompiled PDF).
  **Residuals dispositioned, not hidden:** (i) the [1]/[13] in-entry
  provenance annotations are the deliberate not-peer-reviewed honesty
  disclosures (load-bearing for the R2-FAL-2 disposition) — relocation
  is P-round packaging cosmetics; (ii) an Itzykson–Zuber
  chapter/appendix pinpoint was NOT added because the precise locus
  could not be verified against the source this round
  (never-fabricate); the load-bearing convention is already pinned to
  Nieves–Pal (AJP 72, 1100 — a paper wholly about these conventions)
  and independently machine-verified by the released adjudication
  script.

### R3-RF-1 — Version string "(v1C.0.5)" on the title page
- Legs: Grok P1C-E1; Gemini P1C-N3.
- Verdict: **RE-FLAG** of R1 SO-1 / R2-RF-1: the (Dated: … vX.Y.Z) stamp
  is required by standing directive G on every served draft; stripped at
  P-round submission packaging. No in-draft edit owed.

### R3-RF-2 — "Not self-contained; companion imports; absorb everything or withdraw"
- Legs: Grok P1C-E2; Claude MINOR-4 (Zenodo-only companion refs [1], [13]).
- Verdict: **RE-FLAG** of R1 GNR-2 / R2-RF-2: the sole Tier-I leg (B14) is
  self-contained in App. D since v1C.0.4; remaining imports are honestly
  cited to a public immutable archive (DOI 10.5281/zenodo.21481838) with
  explicit not-peer-reviewed disclosure. Claude MINOR-4's constructive
  sub-ask (arXiv-post the companion / fold the tensor-sector statement
  into App. D) is companion-sequencing work — a publishing-phase matter
  (directive P), recorded on the publishing checklist, not a manuscript
  defect of this survey. Note: Gemini's version of the standalone-reader
  concern this round was the *bounded* anchor ask, closed as R3-GNR-6.

### R3-RF-3 — "Abstract headline numbers never recomputed from displayed inputs"
- Legs: Grok P1C-E3.
- Verdict: **RE-FLAG** of R1 FAL-2 / R2-RF-3 (falsified there with line
  citations): the body displays the complete Route-2 arithmetic chain
  (Eq. (2) with all numeric inputs, both contractions evaluated) and the
  Route-3 integration inputs; the Claude R3 leg *again* independently
  reproduced every displayed number (its checks record: 9.4×10⁻⁶¹
  canonical, 1.1×10⁻⁶² direct, 1.38×10⁻⁶ flow, 8.64×10¹²² hierarchy).

### R3-RF-4 — "Downgrade the abstract's 'structural no-go' framing (Tier-III budgets, imported Tier-I)"
- Legs: Grok P1C-M2.
- Verdict: **RE-FLAG** of R1 RF-2 / R2-RF-5: the abstract itself states
  "only the perturbation-transparency result is a Tier-I rigorous
  theorem, and the survey is a channel-level, not operator-level,
  closure"; Table II labels R2/R3 Tier-III explicitly. The requested
  downgrade is the paper's existing disclosure.

### R3-RF-5 — "B8 subsumed yet drawn/counted; 13-vs-14 inconsistent"
- Legs: Grok P1C-M3.
- Verdict: **RE-FLAG** of R1 FAL-1 / R2-RF-6 (falsified in R1 with five
  surface citations; the Claude R3 leg's consistency check again found
  "no mismatches" across abstract/Sec. III/Table I/Fig. 1/Table II).
  Historical-entry-plus-distinct-count is the stated accounting.

### R3-RF-6 — "Commit hash post-dates the paper version; supply a Zenodo DOI"
- Legs: Grok P1C-N1.
- Verdict: **RE-FLAG** of R2-RF-4 (pin sub-claim) + R2-SO-2 (per-paper
  DOI = P-round packaging, already on the pre-submission checklist).
  The pin is to the commit containing the exact cited files (R1 GNR-9);
  v1C.0.6 additionally discloses the single later docstring-only
  revision (see R3-GNR-1).

### R3-RF-7 — "18 pp vs CQG norm; hedging density; abstract reads as a compliance document"
- Legs: Grok additional observation 1; Claude MINOR-6.
- Verdict: **RE-FLAG** of R1 GNR-3 recorded residual / R2-RF-7:
  venue-length condensation and hedging-density reduction are standing
  D/P-round work, already on the checklist. No new angle.

### R3-RF-8 — "General naturalness arguments (B5–B7, B10, B13) inflate the catalog"
- Legs: Grok additional observation 2.
- Verdict: **RE-FLAG** of R2-RF-8: the paper says exactly this itself
  (Sec. VI: "five entries … are general naturalness or classification
  arguments rather than ECH-specific calculations"); inclusion is the
  stated systematic-coverage design. Grok concedes "correctly labeled."

### R3-SO-1 — "No effect-size / practical-significance qualifier on the suppression ratios"
- Legs: Grok additional observation 3.
- Verdict: **SCOPE-OPINION.** The suppression ratios ARE the effect
  sizes: each is a dimensionless amplitude ratio against a named
  observable (birefringence amplitude / ρ_Λ), with conservatism
  allowances stated inline. No further qualifier is identified that
  would not duplicate the existing evidentiary-status apparatus.
  Dispositioned.

### R3-FAL-1 — "Printed |Ω₄₄/α₄| formula has a squared denominator, inconsistent with its inputs"
- Legs: Claude MINOR-1.
- Verdict: **FALSIFIED against the exact PDF.** The served v1C.0.5 PDF
  prints |Ω₄₄/α₄| = (378+783γ²)/[120(1+γ²)] — FIRST power (PDF text
  layer, p. 6: "(378+783γ 2 )/[120(1+γ 2 )]"; `main.tex` line ~692).
  Recomputation from the paper's stated inputs, performed for this
  audit: α₄ = −6/(1+γ²), Ω₄₄ = −(378+783γ²)/[20(1+γ²)²] ⇒ ratio =
  (378+783γ²)/[20(1+γ²)²] · (1+γ²)/6 = (378+783γ²)/[120(1+γ²)]; at
  γ = 0.24: 423.09/126.91 = 3.334 ≈ 3.3 as printed (the reviewer's
  hypothetical squared form gives 3.15). The printed formula and value
  are exactly the recomputation; the reviewer misread the exponent.
  No edit owed; work shown here per the round directive.

### R3-FAL-2 — "Fierz matrix (F_c)₁₃ printed as 1 breaks F_c² = 𝟙"
- Legs: Gemini P1C-E2.
- Verdict: **FALSIFIED against the exact PDF/source.** Eq. (C1) prints
  (F_c)₁₃ = ¼·(½) — `main.tex` Eq. `fierzmatrix` row 1 is
  (1, 1, ½, −1, 1) with the tfrac{1}{2} entry — precisely the value
  Gemini demands. Numerical involution check performed for this audit
  (exact rationals): F_c² = 𝟙 on all 25 entries. The Claude R3 leg's
  independent spot-check of entries (1,1), (1,2), (3,3) also passed.
  Root cause of the misread: text-extraction/rasterization collapses
  the stacked ½ glyph (pdftotext renders row 1 as "1 1 12 −1 1"). No
  edit owed.

### R3-FAL-3 — "No table of all possible dimension-4 parity-odd operators is supplied"
- Legs: Grok P1C-M1 (as literally stated).
- Verdict: **FALSIFIED as stated.** Table III (`tab:dim4_parityodd`,
  p. 16) lists all six rule-admitted densities with bare dimension,
  schematic form, prefactor, and fate, alongside the explicit
  definitions Eq. (8) — a journal-readable listing in the manuscript.
  The legitimate kernel inside M1 (the *completeness* of that listing
  is asserted, not machine-verified) is real and closed under R3-GNR-1.

## Ledger totals

| Verdict | Count | Items |
|---|---|---|
| GENUINELY-NEW-REAL (closed in v1C.0.6) | **8** | R3-GNR-1 … R3-GNR-8 |
| RE-FLAG (R1/R2-dispositioned / disclosed; source-cited) | 8 | R3-RF-1 … R3-RF-8 |
| SCOPE-OPINION (dispositioned) | 1 | R3-SO-1 |
| FALSIFIED (source-cited) | 3 | R3-FAL-1 … R3-FAL-3 |
| **Total canonical items** | **20** | (Claude MINOR-3 ≡ Gemini E1; Claude MINOR-5 ≡ Gemini M1; Grok E1 ≡ Gemini N3; Grok M1 splits FAL-3 + GNR-1 kernel; Grok N2 folds into GNR-2) |

Deferred-genuine (pre-submission checklist, this round):
1. Real mechanized operator-basis enumeration per R3-GNR-1's adjudication
   (formalized promotion clause; mixed R·T·T / T⁴ classes adjudicated;
   committed script + cited output) — or retain the downgraded framing at
   submission. Never claim enumeration without the artifact.
2. (Carried) P1C script-set version DOI at P-round (R2-SO-2); ST Eq. (58)
   + verbatim-quote verification vs the published CQG PDF; venue-length
   condensation (D/P rounds); companion arXiv-sequencing (directive P;
   re-noted by R3-RF-2).

## Closure evidence (v1C.0.6)

- All 8 GNR closures landed in `arxiv/paper1c_nogo_survey/main.tex`
  (\paperVersion v1C.0.6, dated 2026-08-06) + `references.bib` (Ref. [12]
  field) + `arxiv/scripts/dim4_parityodd_enumeration.py` (docstring/output
  honesty; re-run verified: both identities pass, exit 0). Correction
  sources: published P1A `arxiv/paper1a_ech_nogo.tex`
  (`sec:r4_birefringence` Eq. `beta_bound` for the anchor origin), the
  paper's own stated inputs (κ/M̄_Pl algebra; α_em rounding; endpoint
  provenance already labeled in Sec. IV B), and direct recomputation
  recorded above. Nothing invented; no margin, count, or headline number
  changed.
- Compile: pdflatex 4-pass (with bibtex), **0 errors / 0 undefined
  references / 0 overfull hboxes**, 18 pages.
- /latex-audit visual pass: all 18 pages rendered at 110 DPI; pages 1
  (title v1C.0.6 + abstract), 2 (κ convention), 6 (Route-2 arithmetic +
  Ω ratio), 8 (anchor origin), 12 (Sec. VI/VII), 14–15 (App. A1), 16
  (Table III new column + Fierz matrix) inspected — no column overflow,
  no overlap. GitHub URL check: all repo-mapped URLs resolve; the three
  Data & Code artifact paths exist on disk.
- Mirrors byte-identical (md5 `a0dac49ca1ccba861b92f9bfda471615`):
  `arxiv/paper1c_nogo_survey/main.pdf` =
  `site/public/papers/paper1c_nogo_survey_v1C.0.6.pdf` =
  `public/papers/paper1c_nogo_survey_v1C.0.6.pdf`.
  SHA-256 `fc23872dec25b16acfae57c84df40c56a357555aab777185f03efb1e5586f7ce`.
- Site: `site/src/data/papers.ts` supportingLinks href → v1C.0.6 (+ honest
  description); `site/src/data/reviewTimeline.ts` R3 round entry (failed
  Perplexity leg disclosed); `project-context/draft_paper_registry.json`
  served_aliases → v1C.0.6. `npx next build` passes (see docs commit).

## Convergence read (directive H-refined)

R3 surfaced **8 genuinely-new-real findings** (target: 0). The paper is
therefore **NOT converged**: an **R4 confirmation board on the exact
v1C.0.6 PDF (sha `fc23872d…`)** is required, with all active legs re-run
fresh and the exit test again 0 genuinely-new-real. Context for
calibration, not verdict-softening: 1 of the 8 was MAJOR-grade (the
completeness-framing downgrade, resolved honestly per never-fabricate),
1 was a two-leg definitional error (κ convention), 1 was an
insufficiency of an R2 closure (Table III), and 5 were single-leg
minor/nit-grade labeling or formatting items — but the count is the
count, and the gate is honest.
