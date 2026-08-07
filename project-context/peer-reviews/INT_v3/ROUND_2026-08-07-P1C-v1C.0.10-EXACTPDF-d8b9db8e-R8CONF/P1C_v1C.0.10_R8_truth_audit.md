# P1C v1C.0.10 — R8 confirmation-board truth audit (verdict-first), correctness/presentation classification, and v1C.0.11 closure record

- **Round:** ROUND_2026-08-07-P1C-v1C.0.10-EXACTPDF-d8b9db8e-R8CONF — the R8
  confirmation board on `arxiv/paper1c_nogo_survey/main.tex`, run against the
  R1 + R2 + R3 + R4 + R5 + R6 + R7 disposition ledgers
  (`INT_v3/ROUND_2026-08-06-P1C-v1C.0.3-EXACTPDF-85e53832/P1C_v1C.0.3_truth_audit.md`,
  `INT_v3/ROUND_2026-08-06-P1C-v1C.0.4-EXACTPDF-7ec5f221-R2CONF/P1C_v1C.0.4_R2_truth_audit.md`,
  `INT_v3/ROUND_2026-08-06-P1C-v1C.0.5-EXACTPDF-a770491d-R3CONF/P1C_v1C.0.5_R3_truth_audit.md`,
  `INT_v3/ROUND_2026-08-07-P1C-v1C.0.6-EXACTPDF-fc23872d-R4CONF/P1C_v1C.0.6_R4_truth_audit.md`,
  `INT_v3/ROUND_2026-08-07-P1C-v1C.0.7-EXACTPDF-f085023f-R5CONF/P1C_v1C.0.7_R5_truth_audit.md`,
  `INT_v3/ROUND_2026-08-07-P1C-v1C.0.8-EXACTPDF-385158dd-R6CONF/P1C_v1C.0.8_R6_truth_audit.md`,
  `INT_v3/ROUND_2026-08-07-P1C-v1C.0.9-EXACTPDF-b4d73f94-R7CONF/P1C_v1C.0.9_R7_truth_audit.md`).
- **Exact artifact:** v1C.0.10 PDF, SHA-256
  `d8b9db8e4b2441530feba1539498d90c08fce8ba861bcbfa84ab4e268528defd`,
  20 pp (sha verified against the working tree before any edit).
- **Date:** 2026-08-07. Auditor: Claude (Fable 5) worker per CLAUDE.md
  directives B / H-refined / N. Rule applied: a finding that re-flags an
  R1–R7-dispositioned item is RE-FLAG unless the reviewer adds a genuinely
  new angle.

## Classification rule (NEW at R8 — orchestrator decision, recorded verbatim)

> every GNR item is classed CORRECTNESS-GRADE (wrong
> math/number/attribution/claim) or PRESENTATION-GRADE (length, repetition,
> layout, style). R-phase convergence = a full board with ZERO
> correctness-grade GNR; presentation-grade items route conceptually to the
> D-round stage. Integrity unchanged: every finding dispositioned with
> citations.

## Legs (raw receipts)

| Leg | Model | File | Verdict |
|---|---|---|---|
| Claude INT (Opus-tier subagent) | claude opus | `INT_v3/ROUND_2026-08-07-P1C-v1C.0.10-EXACTPDF-d8b9db8e-R8CONF/P1C_claude_r8_leg.md` | **MINOR REVISIONS** (0 MAJOR / 7 MINOR) — 18-item verification log independently recomputed every checkable displayed equation and numeric (both Route-2 contractions; the Eq. (3)/(4) integrations incl. the full BS flow; Route-3 endpoints; the complete App. E chain E1–E5; the Fierz matrix; App. D proof chain; B12 window; App. A hierarchy/e-fold chain; counts; significances; citation integrity) with zero numeric errors |
| Grok API | grok-4.3 | `ROUND_2026-08-07-P1C-v1C.0.10-EXACTPDF-d8b9db8e-R8CONF_P1C_Grok_brutal.md` | **REJECT** (5 ESSENTIAL / 4 MAJOR / 3 MINOR / 2 NIT) |
| Gemini API | gemini-3.1-pro-preview | `ROUND_2026-08-07-P1C-v1C.0.10-EXACTPDF-d8b9db8e-R8CONF_P1C_Gemini_cosmology.md` | **MAJOR REVISIONS** (2 ESSENTIAL / 1 MAJOR / 1 NIT) |

**Failed legs (preserved as failure evidence, never counted, never hidden):**

- Perplexity leg: FAILED
  (`ROUND_2026-08-07-P1C-v1C.0.10-EXACTPDF-d8b9db8e-R8CONF_P1C_Perplexity_citations.md`
  is a failure record). Optional leg per directive I1; recorded as failed,
  never a verdict.

## Deduplicated finding ledger (canonical items, cross-leg map, verdicts, grades)

Verdict key: **GNR** = genuinely-new-real (real edit owed and landed in
v1C.0.11) · **RE-FLAG** = re-flag of an R1–R7-dispositioned or disclosed
item · **FALSIFIED** = disproved against the cited source/computation/render.
Grade key (applies to GNR per the classification rule; recorded for re-flags
as routing information): **C** = correctness-grade · **P** = presentation-grade.

### R8-GNR-1 [C] — Benedetti–Speziale citation pointer ambiguous across [3]/[9]
- Legs: Claude MINOR-2 (sole leg).
- Verdict: **GNR, correctness-grade** (attribution precision). Verified
  against the source: v1C.0.10 `main.tex` credited "the actual
  fermion-induced perturbative running … computed by Benedetti & Speziale
  \cite{Benedetti2011}" (the JHEP paper, arXiv:1104.4028, rendered [9])
  and, a few lines later, "the actual fermion-coupled one-loop
  β-function was computed by Benedetti & Speziale
  \cite{BenedettiSpeziale2011run} (their Eq. 7)" (the proceedings,
  J. Phys. Conf. Ser. 360, 012011, arXiv:1111.0884, rendered [3]) — the
  same flow credited to two different documents, with the equation-number
  pointer therefore ambiguous. The Eq.-(7) numbering itself was verified
  to belong to the proceedings by the R1 GNR-10 source audit and
  re-verified at R4-RF-9 (ar5iv fetches); no prior round flagged the
  cross-pointer ambiguity — genuinely new.
- Closure (v1C.0.11): the display's credit line now reads "computed by
  Benedetti & Speziale; we quote it from their proceedings
  summary~\cite{BenedettiSpeziale2011run} (whose Eq.~7 is the equation
  numbering used here), companion to the full one-loop analysis of
  Ref.~\cite{Benedetti2011}". No number changed.

### R8-GNR-2 [C] — B12's γ ≈ 0.274 lacks a primary-literature citation
- Legs: Claude MINOR-7 (sole leg).
- Verdict: **GNR, correctness-grade** (citation/attribution). Verified:
  v1C.0.10 sourced the SU(2) black-hole-entropy value γ ≈ 0.274 only to
  "entropy-counting schemes established in the companion
  paper~\cite{Golden2026P1a}"; the value has a primary origin — the
  improved state counting of Ghosh & Mitra. Genuinely new (no prior round
  asked for the primary source of this specific value; distinct from the
  R7-RF-13/R6-RF-10 citation-audit family, which concerned verifying
  existing entries, not adding a missing primary).
- Closure (v1C.0.11): "$\gamma\approx0.274$ (the improved state-counting
  value of Ghosh \& Mitra~\cite{GhoshMitra2005})" with a new bib entry —
  A. Ghosh and P. Mitra, Phys. Lett. B 616, 114–117 (2005),
  arXiv:gr-qc/0411035, doi:10.1016/j.physletb.2005.05.003.
  **Never-fabricate receipt:** the DOI was resolved via the Crossref API
  before the entry was added (title "An improved estimate of black hole
  entropy in the quantum geometry approach", authors A. Ghosh / P. Mitra,
  Physics Letters B 616, 114–117 — exact match), and the arXiv abstract
  page was fetched confirming title/authors/journal-ref. The internal-
  extrapolation and scheme-dependence wording is unchanged.

### R8-GNR-3 [P] — Eq. (3) integration quoted as Δγ/γ is strictly Δln γ
- Legs: Claude MINOR-3 (sole leg).
- Verdict: **GNR, presentation-grade** (orchestrator classification;
  notation precision with zero numeric consequence at the stated margins).
  Verified by recomputation: Eq. (3) is linear in γ, so the integral gives
  Δln γ = (N_F^L−N_F^R) ln(μ_GUT/μ_IR)/(12π²) ≈ 0.25–0.31; exponentiating
  the exact endpoints (0.2534, 0.3108) gives 0.29–0.36 — the reviewer's
  numbers reproduced exactly. Genuinely new (no prior round touched the
  Δln-vs-Δ identification).
- Closure (v1C.0.11): "Integrating Eq.~(3), which is linear in $\gamma$,
  gives $\Delta\ln\gamma \approx …$; … this is numerically
  $\Delta\ln\gamma \approx 0.25$–$0.31$ (…; we identify
  $\Delta\gamma/\gamma \simeq \Delta\ln\gamma$ at this order —
  exponentiating would give $0.29$–$0.36$, a distinction immaterial at
  the $\gtrsim 60$-order margins below)". The adopted conservative 0.3
  and every downstream margin unchanged.

### R8-GNR-4 [P] — App. A hierarchy quotient printed with 1.22 but quoted at the 1.2209 value
- Legs: Claude MINOR-6 (sole leg).
- Verdict: **GNR, presentation-grade** (orchestrator classification;
  numeric-input display consistency at order-of-magnitude scope).
  Verified by recomputation: (1.2209×10¹⁹ GeV / 2.25×10⁻³ eV)⁴ =
  8.67×10¹²² → "8.7×10¹²²" ✓; with 1.22 exactly, 8.64×10¹²² → "8.6".
  The printed quotient and the quoted result used different roundings of
  M_Pl. Genuinely new.
- Closure (v1C.0.11): the quotient now prints 1.2209×10¹⁹ GeV (the same
  four-decimal value App. E already uses), matching the quoted 8.7×10¹²²
  exactly. No other number changed.

### R8-FAL-1 — "Printed |Ω₄₄/α₄| carries a spurious (1+γ²) power" (Claude's headline)
- Legs: Claude MINOR-1.
- Verdict: **FALSIFIED against the exact artifact (render + recomputation).**
  The reviewer claimed the PDF prints (378+783γ²)/[120(1+γ²)²]. Receipts:
  (1) `main.tex` v1C.0.10 line ~853 reads
  `$|\Omega_{44}/\alpha_4|=(378+783\gamma^2)/[120(1+\gamma^2)]$` — one
  power; (2) the 200-DPI render of p. 6 (right column) of the exact
  d8b9db8e PDF shows the printed form with a single unsquared
  $(1+\gamma^2)$ in the denominator; (3) pdftotext of the same page agrees
  ("(378+783γ 2 )/[120(1+γ 2 )]" with no trailing superscript, in contrast
  to the adjacent Ω₄₄ definition line, which correctly extracts its
  genuine squared denominator "(1 + γ 2 )2"); (4) independent
  recomputation for this audit: with α₄ = −6/(1+γ²) and
  Ω₄₄ = −(378+783γ²)/[20(1+γ²)²], the ratio is (378+783γ²)/[120(1+γ²)] —
  exactly the printed form — evaluating to 3.33 at γ = 0.24 (printed
  "≈3.3" ✓), monotone increasing with infimum 378/120 ≈ 3.15 (printed
  "bounded below by 378/120 ≈ 3.2 for all real γ" ✓, limit 783/120 = 6.53
  as γ→∞). The reviewer's own "correct form" is the form the paper
  prints; the consistency argument offered as evidence of error is in
  fact the paper's self-consistency. Probable misread of the adjacent
  Ω₄₄ definition (which legitimately carries the squared denominator).
  **Deviation from the orchestrator's pre-classification disclosed:** the
  dispatch classed m1 correctness-grade GNR "verify by recomputation,
  fix"; the required verification was performed and shows no edit owed —
  the truth-audit verdict controls (never edit to satisfy a falsified
  finding). No edit made.

### R8-FAL-2 — "Numerical targets never stated inside this document" (Grok M2)
- Legs: Grok M2.
- Verdict: **FALSIFIED against the exact PDF.** The birefringence inputs
  are printed with central values and errors in Sec. IV C (0.342°±0.094°
  ≈3.6σ WMAP+Planck; 0.35°±0.14° Eskilt–Komatsu; 0.215°±0.074° ≈2.9σ ACT
  DR6) and the dark-energy target is printed as ρ_Λ,obs ≈ (2.25 meV)⁴
  (with the (2.3 meV)⁴ convention cross-noted in Sec. II and App. E.2);
  H₀/M_Pl ≈ 1.2×10⁻⁶¹ is printed in the Route-2 chain, and the Claude R8
  leg's verification-log items 1, 5, 6 and 12 independently reproduced
  the 58–67-order margins from these in-paper inputs alone. The
  propagate-through-Eqs.-(1)–(4) demand is the R7-RF-2/R2-RF-5 displayed-
  arithmetic family, dispositioned there (kernel re-flag).

### R8-FAL-3 — "Commit hash for the Fierz-adjudication script not supplied" (Grok m3)
- Legs: Grok m3.
- Verdict: **FALSIFIED against the exact PDF.** P. 13 (Data and Code
  Availability) prints: "These exact files are frozen at immutable
  repository commit c80b7487b01f, whose copies of all four files are
  identical to the current repository head" — the pin covers all four
  listed artifacts including the Fierz-adjudication script and its
  report (`main.tex` lines ~1645–1649; R6-GNR-4 closure with git-receipt
  verification in the R6 ledger).

### R8-FAL-4 — "Script filenames written with spaces in the main text/appendices" (Gemini N1)
- Legs: Gemini N1.
- Verdict: **FALSIFIED against the render — text-extraction artifact.**
  The tex sources every site as `\texttt{arxiv/scripts/dim4\_parityodd\_enumeration.py}`
  (underscores; lines ~1467, ~1922) and the 200-DPI render of p. 12 shows
  `arxiv/scripts/dim4_parityodd_enumeration.py` with underscores clearly
  typeset; pdftotext drops the cmtt underscore glyph, extracting "dim4
  parityodd enumeration.py" — exactly the reviewer's quoted string. The
  Data-and-Code block extracts correctly because the `\artifact` macro
  sets paths via `\nolinkurl`, whose font encodes the underscore
  differently. Same extraction-artifact family as R3-FAL-2 / R5-FAL-1 /
  R7-FAL-1 (fourth in the series). No edit owed (the rendered PDF and
  the repository filenames agree).

### R8-RF-1 — Version string/date on the title page
- Legs: Grok E1; Gemini M1.
- Verdict: **RE-FLAG** [P] of R1 SO-1 / R2-RF-1 / R3-RF-1 / R4-RF-7 /
  R5-RF-5 / R6-RF-1 / R7-RF-1: the (Dated: … vX.Y.Z) stamp is required by
  standing directive G on every served draft; stripped at P-round
  packaging.

### R8-RF-2 — "Headline suppression numbers never recomputed from displayed inputs; imported from the companion"
- Legs: Grok E2.
- Verdict: **RE-FLAG** of R7-RF-2 / R6-RF-3 / R1 FAL-2 family, with the
  same partial falsification carried: the Route-2 chain is displayed
  in-body with both contractions evaluated and (since v1C.0.10) the
  explicit numerator display; the Route-3 integration is displayed in
  Sec. IV B; the R1 benchmark is self-contained in App. E.2; the Claude
  R8 leg reproduced every endpoint from in-paper inputs (log items 1, 3,
  5). Residual imports are the R6-dispositioned deferred-genuine set.

### R8-RF-3 — "Standalone-reader test fails; Tier-I imported by citation; make self-contained or withdraw"
- Legs: Grok E3; Grok n1 (parenthetical-reminder kernel).
- Verdict: **RE-FLAG** of the R1 GNR-2 family as narrowed by R6-GNR-1 /
  R6-RF-3 / R7-RF-3 (the Tier-I half is additionally **re-falsified**:
  Appendix D has carried the full B14 statement and 4-step proof
  self-contained since v1C.0.4; the R8 Claude leg's log item 16 again
  verified the proof chain in the compiled artifact). Sec. I carries the
  honest not-peer-reviewed wording for the deferred-genuine residuals.

### R8-RF-4 — "Abstract advertises decisive closures while Table II records Tier-III; rewrite to the actual status"
- Legs: Grok E4; Grok M4.
- Verdict: **RE-FLAG** of R6-RF-2 / R5-RF-1 / R3-RF-4 / R1 RF-2: the
  abstract itself prints the demanded qualification ("only the
  perturbation-transparency result is a Tier-I rigorous theorem, and the
  survey is a channel-level, not operator-level, closure") and every
  quantitative claim carries its per-route metric and endpoint labels.
  M4's "one Tier-I result (by citation)" kernel is the R8-RF-3
  re-falsified item (App. D is in-paper).

### R8-RF-5 — "'13 distinct' not supported; B8 subsumed; count claims must be corrected"
- Legs: Grok E5.
- Verdict: **RE-FLAG** of R6-RF-5 / R2-GNR-1's landed decoupling, with a
  **partial falsification**: the abstract prints "fourteen historical
  catalog entries, one subsumed by another"; Table I's caption prints
  "(13 distinct mechanism-class constraints; B8 subsumed by B14)" with
  the do-not-double-count instruction; and Sec. III states the definition
  is "coverage of the route space, not a claim that thirteen separately
  decisive [theorems]" — precisely the correction demanded. The Fig.-1
  channel-structure-only statement is the R7-GNR-6 closure, present in
  the reviewed caption. The Claude R8 leg verified count consistency at
  every surface (log item 17).

### R8-RF-6 — "Operator-basis completeness asserted by construction rule; embed the enumeration or downgrade"
- Legs: Grok M1.
- Verdict: **RE-FLAG** of R3-GNR-1's adjudication (carried at R6/R7),
  with a **partial falsification**: the demanded fallback wording is the
  paper's existing text — "Completeness of the resulting six-member list
  is asserted from that construction rule, not established by an
  exhaustive symbolic enumeration" (Sec. V and App. A1, both explicit;
  the script's non-enumeration status is itself disclosed at both
  sites). The real mechanized enumeration remains on the deferred-genuine
  pre-submission checklist.

### R8-RF-7 — "Reduced-vs-full M_Pl conversion not displayed for imported coefficients"
- Legs: Grok M3.
- Verdict: **RE-FLAG** of R3-GNR-2 / R6-GNR-8: the imported convention is
  displayed at both import sites (κ̃² ≡ 16πG at ST Eq.-37 quotation and at
  Eq. (4), each tagged "the imported convention fixed in Sec. II"), Sec.
  II states the reduced-vs-full distinction is immaterial at the quoted
  order-of-magnitude scope (2.44×10¹⁸ vs 1.22×10¹⁹ GeV), and the two
  M_Pl²κ² = κ sites carry the exact-in-reduced-convention tags landed at
  R6-GNR-8. The Claude R8 leg's dimensional audit (log items 2, 13)
  found the bookkeeping clean.

### R8-RF-8 — B9 typographic flag in Table I; caption clause duplicated into main text
- Legs: Grok m1; Grok n2.
- Verdict: **RE-FLAG** [P] of R6-RF-7 / R2-SO-1 (single-taxonomy
  disposition: per-leg evidentiary tiering is Table II's job; Sec. III
  labels B9 "heuristic" in prose at three sites, and Sec. VI counts it
  explicitly as "an explicitly heuristic closure"). The n2 ask (put the
  channel-structure-only clause in the main text as well) is satisfied by
  existing text: Sec. IV's "Evidentiary status of each leg" and Table
  II's caption carry exactly that content.

### R8-RF-9 — "α_em/(4π) outside the integral; O(1) loop-factor assumption never justified"
- Legs: Grok m2.
- Verdict: **RE-FLAG** of R7-GNR-4's closure + R2-RF-5 family, with a
  **partial falsification**: the loop factor is not an assumption — "Their
  master renormalization-group equation dλ/dt = −σ/(4π)² (their Eq. 46)
  carries exactly the 1/(16π²) loop factor already written in Eq. (1)"
  (p. 6, printed), and the numerator display names the conservatively
  dropped factors.

### R8-RF-10 — Route-4 closure depends on the unrefereed companion; provide the derivation or drop R4
- Legs: Gemini E1.
- Verdict: **RE-FLAG** of R7-RF-9 / R6-GNR-1's disposition (deferred-
  genuine behind the refereed-companion gate), with the same partial
  falsification carried: the two-sentence algebraic origin of the R4
  anchor (β = (α/2M)Δφ, Δφ ∼ √(2ρ_θ)/m_θ ∼ M_Pl ⇒ α/M ∼ 2β_obs/M_Pl ∼
  10⁻²¹ GeV⁻¹) has been in-paper since v1C.0.6 (Sec. IV C of the reviewed
  PDF), sufficient for the naturalness/explanatory-deficit closure R4
  actually claims (Tier-II objection, not an amplitude exclusion — Table
  II records exactly this). The full spectator-ALP consistency check is
  the R6-dispositioned too-long-to-carry companion content behind honest
  scope wording. Orchestrator coverage check requested and performed:
  covered by R6-GNR-1 (deferred-genuine list item 2) and R7-RF-9 —
  **RE-FLAG confirmed.**

### R8-RF-11 — "A planned DOI is insufficient; mint the frozen-release DOI during review"
- Legs: Gemini E2.
- Verdict: **RE-FLAG** of R5-GNR-2 / R6-RF-9 / R7-RF-8's disposition: the
  deposit is an external, Houston-gated side effect executed at P-round
  packaging; fabricating a DOI in-paper is prohibited. Carried
  deferred-genuine, unchanged; the in-paper statement remains the honest
  "planned prior to publication". Orchestrator coverage check requested
  and performed: covered by R5-GNR-2's deposit-half disposition and the
  R6/R7 carries — **RE-FLAG confirmed.**

### R8-RF-12 — Abstract length/density; tier-disclaimer repetition across ≥7 surfaces
- Legs: Claude MINOR-4; Claude MINOR-5.
- Verdict: **RE-FLAG** [P] of R1 GNR-3 residual / R2-RF-7 / R3-RF-7 /
  R4-RF-10 / R6-RF-4 / R7-RF-11: venue-length condensation, abstract
  compression, and hedging-density consolidation are standing D/P-round
  work on the pre-submission checklist. Under the new classification rule
  these route explicitly to the D-round stage (presentation-grade);
  MINOR-5's sharpened instance count (seven near-verbatim tier
  disclaimers) is recorded on the checklist for the D-round editor.

## Ledger totals

| Verdict | Count | Items |
|---|---|---|
| GENUINELY-NEW-REAL (closed in v1C.0.11) | **4** | R8-GNR-1 [C], R8-GNR-2 [C], R8-GNR-3 [P], R8-GNR-4 [P] |
| — correctness-grade GNR | 2 | R8-GNR-1, R8-GNR-2 (both citation/attribution-precision; no physics or number changed) |
| — presentation-grade GNR | 2 | R8-GNR-3, R8-GNR-4 (notation/display consistency; closed anyway in v1C.0.11) |
| RE-FLAG (R1–R7-dispositioned / disclosed; source-cited; four with partial falsification, one re-falsified) | 12 | R8-RF-1 … R8-RF-12 |
| FALSIFIED (fresh; source-cited receipts) | 4 | R8-FAL-1 (Claude m1, render + recomputation), R8-FAL-2 (Grok M2), R8-FAL-3 (Grok m3), R8-FAL-4 (Gemini N1, extraction artifact) |
| **Total canonical items** | **20** | (Grok E1 ≡ Gemini M1 → RF-1; Grok E3 ≡ n1 → RF-3; Grok E4 ≡ M4 → RF-4; Grok m1 ≡ n2 → RF-8; Claude m4 ≡ m5 → RF-12; Claude's 7 minors → GNR-1/2/3/4 + FAL-1 + RF-12×2) |

## Classification table (all findings, by grade)

| Item | Legs | Verdict | Grade | Disposition |
|---|---|---|---|---|
| R8-GNR-1 | Claude m2 | GNR | **C** | Closed v1C.0.11 (BS pointer bound to proceedings) |
| R8-GNR-2 | Claude m7 | GNR | **C** | Closed v1C.0.11 (Ghosh–Mitra primary citation, Crossref-verified) |
| R8-GNR-3 | Claude m3 | GNR | **P** | Closed v1C.0.11 (Δln γ relabel) |
| R8-GNR-4 | Claude m6 | GNR | **P** | Closed v1C.0.11 (1.2209 quotient) |
| R8-FAL-1 | Claude m1 | FALSIFIED | (C-class claim) | Render + recomputation; no edit owed |
| R8-FAL-2 | Grok M2 | FALSIFIED | (C-class claim) | Inputs printed in-body |
| R8-FAL-3 | Grok m3 | FALSIFIED | (C-class claim) | Pin printed on p. 13 |
| R8-FAL-4 | Gemini N1 | FALSIFIED | (P-class claim) | Extraction artifact; render shows underscores |
| R8-RF-1 | Grok E1, Gemini M1 | RE-FLAG | P | Directive-G stamp; P-round strip |
| R8-RF-2 | Grok E2 | RE-FLAG | C-family | R7-RF-2 carried |
| R8-RF-3 | Grok E3, n1 | RE-FLAG | C-family | R6-RF-3 carried; Tier-I half re-falsified |
| R8-RF-4 | Grok E4, M4 | RE-FLAG | P | R6-RF-2 carried |
| R8-RF-5 | Grok E5 | RE-FLAG | C-family | Partial falsification (disclosures printed) |
| R8-RF-6 | Grok M1 | RE-FLAG | C-family | Downgraded framing already in-paper |
| R8-RF-7 | Grok M3 | RE-FLAG | C-family | Conversions displayed |
| R8-RF-8 | Grok m1, n2 | RE-FLAG | P | Table-II taxonomy disposition |
| R8-RF-9 | Grok m2 | RE-FLAG | C-family | Loop factor grounded in ST Eq. 46 |
| R8-RF-10 | Gemini E1 | RE-FLAG | C-family | Deferred-genuine, refereed-companion gate (coverage verified) |
| R8-RF-11 | Gemini E2 | RE-FLAG | C-family | Deferred-genuine, P-round/Zenodo gate (coverage verified) |
| R8-RF-12 | Claude m4, m5 | RE-FLAG | P | D-round routing (explicit under the new rule) |

Deferred-genuine (pre-submission checklist, carried/updated):
1. Mint the archival deposit / version DOI for the P1C script set at
   P-round (R2-SO-2 / R5-GNR-2 / R6-RF-9 / R7-RF-8 / R8-RF-11). External
   side-effect, Houston-gated.
2. Refereed-companion gate (R6-GNR-1 disposition; R7-RF-9 / R8-RF-10):
   NJL gap analysis, tensor-sector B14 extension, R4 spectator check
   carry honest not-peer-reviewed wording until the companion is
   refereed; companion arXiv-sequencing per directive P.
3. (Carried) Real mechanized operator-basis enumeration per R3-GNR-1's
   adjudication — or retain the downgraded framing at submission;
   ST Eq. (58) + verbatim-quote check vs the published CQG PDF;
   venue-length condensation + abstract compression + tier-disclaimer
   consolidation (seven instances counted at R8) + App-A consolidation
   (D/P rounds; R7-RF-11/12, R8-RF-12).

## Closure evidence (v1C.0.11)

- All 4 GNR closures landed in `arxiv/paper1c_nogo_survey/main.tex`
  (\paperVersion v1C.0.11, dated 2026-08-07) + `references.bib`
  (GhoshMitra2005 — Crossref-verified before addition). Correction
  sources: the R1/R4 source-audit lineage binding Eq. 7 to the
  proceedings; the Crossref record and arXiv abstract page for
  Ghosh–Mitra; direct recomputation of the Δln γ band and its
  exponentiation (0.29–0.36); direct recomputation of the hierarchy
  quotient at both roundings (8.67 vs 8.64×10¹²²). Nothing invented; no
  margin, count, or headline number changed. Reference numbering shifted
  by the insertion (Ghosh–Mitra is [5]; subsequent entries renumber
  automatically).
- Compile: pdflatex 4-pass (with bibtex), **0 errors / 0 undefined
  references / 0 overfull hboxes**, 20 pages.
- /latex-audit visual pass: changed pages rendered at 110 DPI — p. 1
  (title v1C.0.11, August 7, 2026), p. 5 (B12 with the Ghosh–Mitra
  citation, no overflow), p. 8 (proceedings-summary credit line;
  Δln γ band + identification note, clean two-column render), p. 15
  (1.2209 quotient) — no column overflow, no overlap. New URLs: the
  GhoshMitra2005 DOI (Crossref-resolved) and eprint (arXiv abstract page
  fetched) both verified live for this audit.
- Mirrors byte-identical (md5 `4723faef2f210e4b81c33b21d55bfdeb`):
  `arxiv/paper1c_nogo_survey/main.pdf` =
  `site/public/papers/paper1c_nogo_survey_v1C.0.11.pdf` =
  `public/papers/paper1c_nogo_survey_v1C.0.11.pdf`.
  SHA-256 `0868856032e2eee5f26cd207d9fe1cc9b1db2eae827eac41b70c9b2aea394b37`.
- Site: `site/src/data/papers.ts` supportingLinks href → v1C.0.11
  (+ honest description incl. the classification rule);
  `site/src/data/reviewTimeline.ts` R8 round entry (failed Perplexity
  leg disclosed); `project-context/draft_paper_registry.json`
  served_aliases → v1C.0.11. `npx next build` passes (see docs commit).

## Convergence read (directive H-refined + R8 classification rule)

R8 surfaced **4 genuinely-new-real findings** (target: 0), so the
literal 0-GNR gate is not met and the paper is **NOT converged**. Under
the R8 classification rule the composition matters: **2 of the 4 are
correctness-grade** (both citation/attribution-precision fixes — no
equation, number, margin, or physics claim changed) and 2 are
presentation-grade (closed anyway). The board's sharpest
correctness-grade *claims* — the spurious-power formula error, the
missing inputs, the missing pin, the space-corrupted filenames — were
all **falsified with receipts** (render, recomputation, printed text,
Crossref). An **R9 confirmation board on the exact v1C.0.11 PDF (sha
`0868856032…`)** is required and is the **correctness-convergence
check**: a full board whose truth audit yields ZERO correctness-grade
GNR converges the R-phase, with any residual presentation-grade items
routed to the D-round stage per the classification rule. Integrity
unchanged: every finding on that board still gets a source-cited
disposition, and any correctness-grade GNR still forces a closure and a
further confirmation round.
