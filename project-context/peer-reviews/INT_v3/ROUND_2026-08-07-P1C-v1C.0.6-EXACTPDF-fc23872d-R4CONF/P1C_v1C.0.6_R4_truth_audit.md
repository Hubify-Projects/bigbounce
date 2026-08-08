# P1C v1C.0.6 — R4 confirmation-board truth audit (verdict-first) and v1C.0.7 closure record

- **Round:** ROUND_2026-08-07-P1C-v1C.0.6-EXACTPDF-fc23872d-R4CONF — the R4
  confirmation board on `arxiv/paper1c_nogo_survey/main.tex`, run against the
  R1 + R2 + R3 disposition ledgers
  (`INT_v3/ROUND_2026-08-06-P1C-v1C.0.3-EXACTPDF-85e53832/P1C_v1C.0.3_truth_audit.md`,
  `INT_v3/ROUND_2026-08-06-P1C-v1C.0.4-EXACTPDF-7ec5f221-R2CONF/P1C_v1C.0.4_R2_truth_audit.md`,
  `INT_v3/ROUND_2026-08-06-P1C-v1C.0.5-EXACTPDF-a770491d-R3CONF/P1C_v1C.0.5_R3_truth_audit.md`).
- **Exact artifact:** v1C.0.6 PDF, SHA-256
  `fc23872dec25b16acfae57c84df40c56a357555aab777185f03efb1e5586f7ce`,
  18 pp (verified against the served mirror and each leg header).
- **Date:** 2026-08-06. Auditor: Claude (Fable 5) worker per CLAUDE.md
  directives B / H-refined / N. Rule applied: a finding that re-flags an
  R1/R2/R3-dispositioned item is RE-FLAG unless the reviewer adds a genuinely
  new angle.

## Legs (raw receipts)

| Leg | Model | File | Verdict |
|---|---|---|---|
| Claude INT (Opus-tier subagent) | claude opus | `INT_v3/ROUND_2026-08-07-P1C-v1C.0.6-EXACTPDF-fc23872d-R4CONF/P1C_claude_r4_leg.md` | **minor-revisions** (0 MAJOR / 8 MINOR) |
| Grok API | grok-4.3 | `ROUND_2026-08-07-P1C-v1C.0.6-EXACTPDF-fc23872d-R4CONF_P1C_Grok_brutal.md` | **REJECT** (3 ESSENTIAL / 3 MAJOR / 2 MINOR / 1 NIT) |
| Gemini API | gemini-3.1-pro-preview | `ROUND_2026-08-07-P1C-v1C.0.6-EXACTPDF-fc23872d-R4CONF_P1C_Gemini_cosmology.md` | **ACCEPT WITH MINOR CORRECTIONS** (1 MAJOR / 2 MINOR / 1 NIT) — the board's first ACCEPT-class verdict on P1C |

**Failed legs (preserved as failure evidence, never counted, never hidden):**

- Perplexity leg: FAILED — API `insufficient_quota` 401
  (`ROUND_2026-08-07-P1C-v1C.0.6-EXACTPDF-fc23872d-R4CONF_P1C_Perplexity_citations.md`
  is a failure record). Optional leg per directive I1; recorded as failed,
  never a verdict.

## Deduplicated finding ledger (canonical items, cross-leg map, verdicts)

Verdict key: **GNR** = genuinely-new-real (real edit owed and landed in
v1C.0.7) · **RE-FLAG** = re-flag of an R1/R2/R3-dispositioned or disclosed
item · **FALSIFIED** = disproved against the cited source line.

### R4-GNR-1 — Table II R3 row attaches the Benedetti–Speziale name to the chiral-count bound
- Legs: Claude m1 (sole leg; verified true against the source: `main.tex`
  Table II R3 cell read "the chiral-asymmetry beta-function bound
  (Benedetti--Speziale) is a Tier-III ... upper bound, deliberately loose"
  while the body, §IV.B, defines the deliberately-loose bound as the
  chiral-count EFT ansatz Eq. (3) motivated by Date–Kaul–Sengupta, with the
  Benedetti–Speziale flow the distinct Eq. (4) that yields the *derived*
  1.4×10⁻⁶ primary estimate).
- Verdict: **GNR** (attribution conflation; genuinely new — no prior round
  flagged this row's provenance).
- Closure (v1C.0.7): row now reads "the chiral-count ansatz bound (motivated
  by Date--Kaul--Sengupta~\cite{DateKaulSengupta2009}) is a Tier-III
  order-of-magnitude upper bound, deliberately loose and non-load-bearing
  (≳60 orders of margin); the integrated Benedetti--Speziale flow gives the
  far smaller derived primary estimate (Sec. IV)."

### R4-GNR-2 — §V.a "R2–R3 are Tier-III" contradicts Table II's (II)+(III) records
- Legs: Claude m2 (sole leg; verified: §V.a sentence vs Table II R3/R1
  "(II)+(III)" cells under a caption stating the table records "the highest
  level at which each leg is claimed").
- Verdict: **GNR** (internal tier-wording misalignment).
- Closure (v1C.0.7): sentence now reads "R2 is a Tier-III ansatz-level
  estimate, and the R1/R3 *amplitude* legs are likewise Tier-III (their
  structural components --- the parity-even mean-field fact for R1 and the
  mass-dimension lock for R3 --- are the Tier-II entries
  Table II records alongside them)".

### R4-GNR-3 — R1 benchmark mantissa: reviewer recomputes 3.9×10⁻⁶⁹ vs the quoted 3.6×10⁻⁶⁹ (ADJUDICATED WITH RECEIPTS)
- Legs: Claude m3.
- **Adjudication (recomputation performed for this audit):** BOTH values are
  correct; they differ only in the ρ_Λ normalization, and the quote is a
  FAITHFUL transcription of the published companion.
  - κn_ψ² recomputed from the printed inputs (κ = 8πG exactly = M̄_Pl⁻²,
    n_ψ = 100 cm⁻³, ħc = 1.9733×10⁻⁵ eV·cm, M_Pl = 1.2209×10²⁸ eV):
    κn_ψ² = 9.9549×10⁻⁸⁰ eV⁴ — matching P1A's own printed
    9.9542×10⁻⁸⁰ eV⁴ (P1A `arxiv/paper1a_ech_nogo.tex` line ~4281).
  - With P1A's stated normalization ρ_Λ ≈ (2.3 meV)⁴ ≈ 2.8×10⁻¹¹ eV⁴
    (P1A line ~2704: "the canonical ρ_Λ ≈ (2.3 meV)⁴ ... used throughout
    this paper"): ratio = 3.557×10⁻⁶⁹ → quoted 3.6×10⁻⁶⁹ ✓ (P1A's own
    comment block records "3.5571e-69 ..., 68.45 orders", line ~785).
  - With this survey's App-A input ρ_Λ = (2.25 meV)⁴ = 2.563×10⁻¹¹ eV⁴:
    ratio = 3.884×10⁻⁶⁹ → the reviewer's 3.9×10⁻⁶⁹ ✓.
  - Orders below ρ_Λ: 68.45 vs 68.41 — identical at the stated
    order-of-magnitude precision. P1A v1A.0.127 states 3.6×10⁻⁶⁹ at four
    surfaces (lines ~1211, ~2696, ~4026, plus Table II "68.45 orders");
    P1C cites P1A as the anchor, so the honest fix is to keep the faithful
    quote and state the normalization — NOT to change the mantissa.
- Verdict: **GNR as a clarity defect only** (the §II convention flag named
  the κ input but not the ρ_Λ input, while the paper itself uses
  (2.25 meV)⁴ in App. A — a genuinely new site-by-site disclosure gap).
  No transcription error exists.
- Closure (v1C.0.7): the §II convention flag now states the benchmark is
  the companion's published value computed with exact κ = 8πG *and* the
  companion's ρ_Λ ≈ (2.3 meV)⁴ ≈ 2.8×10⁻¹¹ eV⁴, and that under the
  (2.25 meV)⁴ App-A input the same κn_ψ² evaluates to 3.9×10⁻⁶⁹ —
  identical at order-of-magnitude precision (≈68 orders either way).
  No number changed anywhere else.

### R4-GNR-4 — Branch letters skip I and K with no comment
- Legs: Claude m4.
- Verdict: **GNR** (reader-inference defect in a paper that advertises a
  preserved historical catalog). Verified against the frozen monolith
  (`arxiv/paper1_unified.tex` lines ~1495, ~3584): the historical catalog
  itself runs H, J, L, M, N, O — the letters I and K were never assigned,
  and no branch entries were removed.
- Closure (v1C.0.7): Fig. 1 caption now states "The branch letters are
  inherited unchanged from the historical catalog, which never assigned
  the letters I or K; no branch entries have been removed."

### R4-GNR-5 — Acknowledgments phrasing implies involvement/endorsement
- Legs: Claude m6.
- Verdict: **GNR** (standard journal-practice defect; "We acknowledge the
  foundational contributions of [named researchers]" reads as personal
  participation).
- Closure (v1C.0.7): rephrased to builds-on-published-work form with
  citations — Popławski~\cite{Poplawski2010} (entry added to
  `references.bib`, copied verbatim from the P1A bibliography),
  Mercuri~\cite{Mercuri2009}, Freidel–Minic–Takeuchi~\cite{Freidel2005},
  Shapiro–Teixeira~\cite{ShapiroTeixeira2014},
  Benedetti–Speziale~\cite{BenedettiSpeziale2011run} — closing with "None
  of the named researchers was involved in this work, and no endorsement
  is implied."

### R4-GNR-6 — Fig. 1 drawing cannot carry the B8-vs-B14 arrow attribution its caption asserts
- Legs: Claude m8.
- Verdict: **GNR** (closure-insufficiency of R1 GNR-7, a genuinely new
  angle: R1 added the missing H→R2/R3/R4 arrows and the caption text, but
  the drawing itself left the per-barrier attribution unresolved at box
  granularity).
- Closure (v1C.0.7): in-figure labels added to the TikZ source — "B8, B14"
  on the upper Branch-H→R1 leg, "B14" on the lower three-route fan — and
  the caption now says the labels record the per-barrier attribution
  otherwise not resolved at box granularity. Rendered and visually
  verified (p. 4, no overlap).

### R4-GNR-7 — Zenodo-deposit timeline vs the 2026-08-05 adjudication artifacts (Gemini's MAJOR)
- Legs: Gemini #1 (MAJOR).
- Verdict: **GNR** (real provenance-clarity defect). Fact-checked for this
  audit: the pinned commit `9b92721d5d7e` DOES contain all cited files
  including `research/theory_audit/fierz_adjudication_2026_08_05.{py,md}`
  (verified by `git ls-tree`), and the Zenodo deposit
  (10.5281/zenodo.21481838) is dated 2026 July 22 — so the Aug-5
  artifacts cannot be, and are not claimed to be, inside it; but the
  v1C.0.6 text left the archive boundary implicit, permitting Gemini's
  paradox reading.
- Closure (v1C.0.7): Data & Code Availability now states the boundary
  explicitly — the companion paper and the companion's own verification
  scripts are in the Zenodo deposit (deposited 2026 July 22), whereas the
  2026-08-05 adjudication artifacts post-date that deposit and are
  available at the pinned repository commit only.

### R4-GNR-8 — Version-history parenthetical in the main text
- Legs: Gemini #2; Claude m7 (audit-trail-prose kernel; dedupe).
- Verdict: **GNR** (the "(a later revision clarifies ...)" parenthetical
  was introduced by the R3-GNR-1 closure — genuinely new at R4. The
  disclosure itself is load-bearing (pin-drift honesty, R3 decision) and
  is preserved, not deleted.)
- Closure (v1C.0.7): moved verbatim-faithful to a footnote exactly as
  Gemini's required fix offers ("If ... necessary for a reproducibility
  audit trail, move it to a footnote"). Renders as a bottom-of-column
  footnote on p. 13 (visually verified).

### R4-GNR-9 — Inline audit-report filepath in Appendix C prose
- Legs: Gemini #3.
- Verdict: **GNR** (bounded presentation defect).
- Closure (v1C.0.7): the "(report: research/theory_audit/....md)" inline
  tag removed from App. C; the .md report is now listed as the fourth
  artifact in Data & Code Availability ("with the fourth file its
  human-readable report"), exactly as Gemini's fix requests; App. C now
  points to "the released verification artifact and its report listed in
  the Data and Code Availability statement."

### R4-GNR-10 — Abstract's "each closing a specific route" vs B14 spanning all four routes
- Legs: Claude m7 (the related-nit kernel; verified true — B14 is tagged
  [R1–R4] everywhere else).
- Verdict: **GNR** (single-word-scale honesty alignment).
- Closure (v1C.0.7): abstract now reads "each closing one or more of the
  four routes by which ...".

### R4-RF-1 — "Not self-contained; companion imports; merge or reproduce everything"
- Legs: Grok P1C-E1.
- Verdict: **RE-FLAG** of R1 GNR-2 / R2-RF-2 / R3-RF-2: the sole Tier-I
  leg (B14) is self-contained in App. D since v1C.0.4; remaining imports
  are honestly cited to a public immutable archive with explicit
  not-peer-reviewed disclosure; companion sequencing is directive-P
  publishing-phase work.

### R4-RF-2 — "Abstract margins never recomputed from first principles in this manuscript"
- Legs: Grok P1C-E2.
- Verdict: **RE-FLAG** of R1 FAL-2 / R2-RF-3 / R3-RF-3 (falsified in R1
  with line citations): the body displays the complete Route-2 arithmetic
  chain and Route-3 integration inputs; the Claude R4 leg *again*
  independently reproduced every displayed number (verification log items
  1–5: 1.7×10⁻⁶⁰, 2×10⁻⁶², 1.38×10⁻⁶, 0.409/0.267, 8.6×10¹²²).

### R4-RF-3 — "13 distinct vs 14 entries is inconsistent on the page"
- Legs: Grok P1C-E3; Grok P1C-NIT1 (folds in).
- Verdict: **RE-FLAG** of R1 FAL-1 / R2-RF-6 / R3-RF-5 (falsified in R1
  with five surface citations); the Claude R4 leg's structural
  cross-consistency check (log item 12) again found the counting uniform
  at every surface.

### R4-RF-4 — "Enumeration by fiat; downgrade to conjectured finite basis"
- Legs: Grok P1C-M1.
- Verdict: **RE-FLAG** of R1 RF-1 / R2-RF-4 / R3-GNR-1's landed closure:
  the demanded downgrade already exists in v1C.0.6 — completeness is
  stated as "asserted from the stated construction rule, not proved" at
  every surface, and the released script is honestly scoped to the two
  reduction identities. The real mechanized enumeration remains on the
  deferred-genuine pre-submission checklist (R3 adjudication).

### R4-RF-5 — "Circular; reclassify R2/R3 as exploratory upper bounds, not closures"
- Legs: Grok P1C-M2.
- Verdict: **RE-FLAG** of R1 RF-2 / R2-RF-5 / R3-RF-4: Table II and text
  already classify R2 as "(III) Ansatz-level ... exploratory, not
  load-bearing" and the paper's own framing states the missing
  stress-tensor derivation is neither supplied nor needed for an
  amplitude budget.

### R4-RF-6 — "Tier-III legs advertised as structural closures in the headline"
- Legs: Grok P1C-M3.
- Verdict: **RE-FLAG** of R1 RF-2 / R3-RF-4 family: the abstract itself
  states "only the perturbation-transparency result is a Tier-I rigorous
  theorem, and the survey is a channel-level, not operator-level,
  closure"; the evidentiary gap Grok wants quantified is exactly what
  Table II tabulates.

### R4-RF-7 — Version string/date on the title page
- Legs: Grok P1C-N1.
- Verdict: **RE-FLAG** of R1 SO-1 / R2-RF-1 / R3-RF-1: the
  (Dated: ... vX.Y.Z) stamp is required by standing directive G on every
  served draft; stripped at P-round submission packaging.

### R4-RF-8 — "Repo links/commit hashes are not archival references; use DOIs"
- Legs: Grok P1C-N2.
- Verdict: **RE-FLAG** of R1 SO-1 (paths kernel) / R2-RF-9 + R2-SO-2:
  committed repo-relative artifact paths are the lab's reproducibility
  standard and published-P1A precedent, already commit-pinned; the
  per-paper script-set DOI is on the P-round packaging checklist. (The
  paths already live in the Data Availability statement, which is what
  Grok's fix requests.)

### R4-RF-9 — "Imported ST/BS coefficients not independently verifiable from this manuscript; spot-check the sources"
- Legs: Claude m5 (explicitly "a due-diligence request, not an error
  claim").
- Verdict: **RE-FLAG** of R1 GNR-10's completed source audit — and the
  spot-check was REPEATED for this audit anyway, against fresh ar5iv
  fetches: ST arXiv:1402.4854 Eq. (41) α₄ = −6/(1+γ²) ✓, Eq. (42)
  Ω₄₄ = −(378+783γ²)/[20(1+γ²)²] ✓ and Ω₂₄ = −81γ²/(1+γ²)² ✓; BS
  arXiv:1111.0884 Eq. (7) β_{γ²} = −(γ²−1)μ²κ²/(8π)²·(23γ²+5) ✓ —
  all exactly as transcribed in v1C.0.6/v1C.0.7. Carried
  deferred-genuine item unchanged: ST Eq. (58) + verbatim-quote check
  against the published CQG PDF (ar5iv render truncates).

### R4-RF-10 — Abstract length / residual referee-response hedging prose
- Legs: Claude m7 (general condensation kernel).
- Verdict: **RE-FLAG** of R1 GNR-3 residual / R2-RF-7 / R3-RF-7:
  venue-length condensation and hedging-density reduction are standing
  D/P-round work on the pre-submission checklist. The two bounded m7
  kernels that were genuinely new were closed above (R4-GNR-8 audit-trail
  footnote; R4-GNR-10 abstract route wording).

### R4-FAL-1 — "Repository paths are dropped into the text as floating lines"
- Legs: Gemini #4 (NIT).
- Verdict: **FALSIFIED as stated.** The paths are typeset via the
  \artifact macro (`main.tex` line ~129:
  `\providecommand{\artifact}[1]{\href{\repoBase/#1}{\nolinkurl{#1}}}`) —
  monospace, hyperlinked — inside a set-off `center` block, i.e. already
  in the "monospace font ... clearly separate[d] from the surrounding
  prose" form the fix requests (rendered p. 13, visually verified). No
  edit owed beyond the R4-GNR-9 list addition.

## Ledger totals

| Verdict | Count | Items |
|---|---|---|
| GENUINELY-NEW-REAL (closed in v1C.0.7) | **10** | R4-GNR-1 … R4-GNR-10 |
| RE-FLAG (R1/R2/R3-dispositioned / disclosed; source-cited) | 10 | R4-RF-1 … R4-RF-10 |
| FALSIFIED (source-cited) | 1 | R4-FAL-1 |
| **Total canonical items** | **21** | (Gemini #2 ≡ Claude m7 audit-trail kernel; Grok NIT1 folds into RF-3; Claude m7 splits RF-10 + GNR-8 + GNR-10) |

Deferred-genuine (pre-submission checklist, carried unchanged):
1. Real mechanized operator-basis enumeration per R3-GNR-1's adjudication —
   or retain the downgraded framing at submission.
2. ST Eq. (58) + verbatim-quote verification vs the published CQG PDF;
   P1C script-set version DOI at P-round (R2-SO-2); venue-length
   condensation (D/P rounds); companion arXiv-sequencing (directive P).

## Closure evidence (v1C.0.7)

- All 10 GNR closures landed in `arxiv/paper1c_nogo_survey/main.tex`
  (\paperVersion v1C.0.7, dated 2026-08-06) + `references.bib`
  (Poplawski2010 entry, copied verbatim from the P1A bibliography).
  Correction sources: published P1A `arxiv/paper1a_ech_nogo.tex`
  (ρ_Λ ≈ (2.3 meV)⁴ normalization statement, printed κn_ψ² value, comment
  ledger 3.5571e-69/68.45), the frozen monolith `arxiv/paper1_unified.tex`
  (branch letters verified never-assigned), `git ls-tree 9b92721d5d7e`
  (pinned-commit contents), the ar5iv renders of arXiv:1402.4854 and
  arXiv:1111.0884 (coefficient re-verification), and direct recomputation
  recorded above. Nothing invented; no margin, count, or headline number
  changed.
- Compile: pdflatex 4-pass (with bibtex), **0 errors / 0 undefined
  references / 0 overfull hboxes**, 18 pages.
- /latex-audit visual pass: all 18 pages rendered at 110 DPI; pages 1
  (title v1C.0.7 + corrected abstract), 2 (benchmark-normalization flag),
  4 (Fig. 1 arrow labels + caption), 9 (§V.a tier wording), 10 (Table II
  R3 row), 13 (Data & Code provenance boundary, footnote, artifact list,
  acknowledgments), 16–17 (App. C) inspected — no column overflow, no
  overlap; the new footnote renders at the column foot of p. 13.
- Mirrors byte-identical (md5 `a75934be584614d515c5c08952d477bd`):
  `arxiv/paper1c_nogo_survey/main.pdf` =
  `site/public/papers/paper1c_nogo_survey_v1C.0.7.pdf` =
  `public/papers/paper1c_nogo_survey_v1C.0.7.pdf`.
  SHA-256 `f085023fea37f4d1fa053fc30d04d5006c23f5998e8edebe683900a955048397`.
- Site: `site/src/data/papers.ts` supportingLinks href → v1C.0.7 (+ honest
  description); `site/src/data/reviewTimeline.ts` R4 round entry (failed
  Perplexity leg disclosed); `project-context/draft_paper_registry.json`
  served_aliases → v1C.0.7. `npx next build` passes (see docs commit).

## Convergence read (directive H-refined)

R4 surfaced **10 genuinely-new-real findings** (target: 0). The paper is
therefore **NOT converged**: an **R5 confirmation board on the exact
v1C.0.7 PDF (sha `f085023f…`)** is required, with all active legs re-run
fresh and the exit test again 0 genuinely-new-real. Context for
calibration, not verdict-softening: the round produced the board's first
ACCEPT-class verdict (Gemini) and the Claude leg's first 0-MAJOR report;
all 10 GNR items are wording/attribution/provenance-grade (1 was
Gemini-MAJOR-labeled but administrative — the archive-timeline boundary);
zero numeric, margin, count, or headline changes were owed or made; and
the one disputed number (3.6 vs 3.9 ×10⁻⁶⁹) was adjudicated with
recomputation receipts as a normalization difference, both values
correct. But the count is the count, and the gate is honest.
