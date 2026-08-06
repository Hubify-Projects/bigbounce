# P1C v1C.0.3 — R1 board truth audit (verdict-first) and v1C.0.4 closure record

- **Round:** ROUND_2026-08-06-P1C-v1C.0.3-EXACTPDF-85e53832 — the FIRST full
  review board on P1C (`arxiv/paper1c_nogo_survey/main.tex`).
- **Exact artifact:** v1C.0.3 PDF, SHA-256
  `85e5383298625013cc41a80b5bedfc4bc4464315e946acb1a319432b8c665863`, 16 pp.
- **Date:** 2026-08-06. Auditor: Claude (Fable 5) orchestrator, per
  CLAUDE.md directives B / H-refined / N (verdict-first truth audit; never
  fake, never fabricate, never dismiss without a source-cited verdict).

## Legs (raw receipts)

| Leg | Model | File | Verdict |
|---|---|---|---|
| Claude INT (Opus-tier subagent) | claude opus | `INT_v3/ROUND_2026-08-06-P1C-v1C.0.3-EXACTPDF-85e53832/P1C_claude_int_leg.md` | **major-revisions** (3 MAJOR / 8 MINOR) |
| Grok API | grok-4.3 | `ROUND_2026-08-06-P1C-v1C.0.3-EXACTPDF-85e53832-R4_P1C_Grok_brutal.md` | **REJECT** (3 ESSENTIAL / 3 MAJOR / 1 MINOR / 1 NIT) |
| Gemini API | gemini-3.1-pro-preview | `ROUND_2026-08-06-P1C-v1C.0.3-EXACTPDF-85e53832-R4_P1C_Gemini_cosmology.md` | **MAJOR REVISIONS** (4 ESSENTIAL / 1 MAJOR / 1 MINOR + 3 pass-2) |

**Failed legs (preserved as failure evidence, never counted, never hidden):**

- Perplexity leg: FAILED — API `insufficient_quota` 401 (raw traceback in
  `...-R4_P1C_Perplexity_citations.md`). Optional leg per directive I1; the
  round does not fail on it.
- The same-named files without `-R4` and with `-R2`/`-R3` suffixes are
  infra-failure records of earlier dispatch attempts (stale portfolio
  receipts / packet-build failures / model-fallback errors). They contain no
  reviewer content and are retained untouched as failure evidence.

## Deduplicated finding ledger (canonical items, cross-leg map, verdicts)

Verdict key: **GNR** = genuinely-new-real (real edit owed and landed in
v1C.0.4) · **RE-FLAG** = re-flag of already-tracked/disclosed content ·
**SCOPE-OPINION** = venue/style position, dispositioned · **FALSIFIED** =
disproved against the cited source line.

### GNR-1 — Printed Eq. (B1) does not compose into Eq. (B2) and contradicts the released script
- Legs: Claude MAJOR-1; Gemini #5.
- Verdict: **GNR** (the round's headline). The v1C.0.3 App-B matrix was the
  frozen monolith's variant (axial row ¼(4,2,0,−2,−4)); composing it with the
  stated F_op = −F_c yields −SS − ½VV + ½AA + PP, which is false, and the
  released `arxiv/scripts/fierz_lemma_check.py` asserts the axial c-number
  row (−1,−½,0,−½,1) — the OTHER convention. Ground truth: the independent
  adjudication `research/theory_audit/fierz_adjudication_2026_08_05.{py,json,md}`
  — its computed c-number matrix in the (axial=phys, tensor=full) basis is an
  EXACT MATCH to published P1A's tabulated F_c (log line [L12]), and the exact
  Grassmann engine gives the unique operator row (1,½,0,½,−1) = Eq. (B2)
  ([L08], [L15]). Eq. (B2) itself was already correct (adjudication [L11];
  independently re-verified by the Claude leg's own Grassmann computation).
- Closure: Eq. (B1) replaced with the adjudication-computed published-P1A
  matrix ¼[[1,1,½,−1,1],[4,−2,0,−2,−4],[12,0,−2,0,12],[−4,−2,0,−2,4],
  [1,−1,½,1,1]] with the row/column semantics, the Nieves–Pal phase statement,
  the explicit axial-row composition ¼(−4,−2,0,−2,4) → (1,½,0,½,−1), and the
  scalar bridge (F_c)_AS = −1 → (F_op)_AS = +1 → G_s = −3κ/16, all carried
  verbatim-faithful from `arxiv/paper1a_ech_nogo.tex` (App. fierz, Eq.
  fierzmatrix / fierz_scalar_bridge). The chain B1 → (−F_c) → B2 now composes
  and matches the released script. No downstream number changed (B2 and
  G_s = −3κ/16 were already the adjudicated values in v1C.0.3).

### GNR-2 — Sole Tier-I theorem not refereeable from this manuscript (standalone-reader violation)
- Legs: Claude MAJOR-2; Grok E1 (ESSENTIAL); Gemini #2 (ESSENTIAL).
- Verdict: **GNR** (structural). The B14 perturbation-transparency theorem —
  the survey's only Tier-I leg — lived entirely in the companion.
- Closure: new Appendix D carries the theorem statement and 4-step proof
  self-contained, faithfully from published P1A `sec:transparency`
  (statement, zero-spin-density → T=0 via the invertible bivector operator
  (1+γ²>0), Levi-Civita reduction, Holst-dual Bianchi vanishing — the same
  identity P1C's Check A verifies symbolically). Scope exclusions carried
  verbatim. Attribution explicit: "nothing below is new to this survey."
  The remaining companion imports (torsion-elimination derivation, Jackiw–Pi
  closure) stay honestly cited, not silently reproduced: the companion is a
  public immutable archive (Zenodo DOI 10.5281/zenodo.21481838, now also
  linked in Data & Code Availability), not an inaccessible source. The demand
  to reproduce EVERY companion derivation in-paper is dispositioned as
  satisfied for the load-bearing Tier-I leg and reframed-honest for the rest
  (fabricating fresh derivations is prohibited; carrying the full P1A would
  duplicate a published paper).

### GNR-3 — Contribution sharpness + condensation (hedging repetition)
- Legs: Claude MAJOR-3, MINOR-3; Grok M2 (kernel), N2 (NIT), length
  observation; Gemini general comments.
- Verdict: **GNR** (editorial, directive Q1). The ≈60/≥58 margin statement
  appeared ≥8×, the completeness disclaimer ≥5×, the R2 ansatz-status
  disclaimer ≥4×, "companion does not retain" 4×.
- Closure: explicit "Contributions" paragraph added to Sec. I (the four
  publishable units: taxonomy+tiering, O1–O6 closure, integrated R3 bound,
  one-loop-grounded R2 budget); R2 consolidated to ONE authoritative
  robustness statement (labeled as such) and ONE evidentiary-status
  statement; R3 duplicate margin sentences removed; Sec-IV "does not retain"
  repetition now points at Sec. I; conclusions' duplicated completeness
  parenthetical replaced with a pointer. Grok M2's abstract-overstatement
  kernel is covered by this + GNR-4 (the abstract already carried, and
  keeps, the explicit only-one-Tier-I disclosure). Residual (recorded, not
  hidden): a full ~12-pp CQG condensation remains venue-packaging work for
  the D/P rounds; v1C.0.4 is 17 pp because the self-containment closures
  (GNR-2) add more than the condensation removes.

### GNR-4 — Abstract/section text conflated the R2 closure metric with the dark-energy density
- Legs: Gemini #1 (ESSENTIAL); Claude MINOR-1; the real kernel of Grok E2.
- Verdict: **GNR**. Eq. (2) closes R2 against the observed birefringence
  amplitude; the abstract said "against the observed dark-energy density"
  for both routes.
- Closure: abstract, Sec. IV opening, Sec. VI "What is established," and
  conclusions now state the per-route metric: R2 ≈60 (≥58) orders vs the
  observed birefringence amplitude; R3 61–67 orders vs the observed
  dark-energy density.

### GNR-5 — Tier-I phrasing drift (abstract vs Sec. III / Sec. VI)
- Legs: Gemini #6.
- Verdict: **GNR** (minor consistency). Sec. III/VI called both the
  torsion-elimination derivation and B14 "Tier-I rigorous results," while
  the abstract and Table II credit exactly one Tier-I closure leg.
- Closure: both passages now distinguish first-principles *derivation*
  (torsion elimination, companion content) from Tier-I *closure leg* (B14
  only), with explicit pointers to Table II.

### GNR-6 — Displayed cosmological-constant-hierarchy arithmetic wrong as rounded
- Legs: Gemini P13-A1; Claude MINOR-8.
- Verdict: **GNR**. The displayed `10^{19 GeV×4}/(10⁻³ eV)⁴ ~ 10¹²²` is
  false as written (rounded exponents give 10¹²⁴; exact values give
  8.7×10¹²² ≈ 10¹²³).
- Closure: display rewritten with exact inputs
  (1.22×10¹⁹ GeV)⁴/(2.25×10⁻³ eV)⁴ ≈ 8.7×10¹²² ≈ 10¹²³, a parenthetical
  noting the bare-power-of-ten pitfall, and an explicit rounding-convention
  sentence (10¹²² adopted in the dilution bookkeeping; the choice shifts
  N_tot by ln10/3 ≈ 0.8 e-folds, inside the quoted 92–94 spread).

### GNR-7 — Fig. 1 contradicted the B14 scope claim
- Legs: Gemini P4-B1.
- Verdict: **GNR**. Text and Table I give B14 scope [R1–R4]; Fig. 1 drew
  Branch H → R1 only.
- Closure: three arrows added (H → R2, R3, R4) at a lower drop so they stay
  visually distinct; caption updated to explain H's four arrows (B14) vs
  co-resident B8 (R1 only). Rendered and visually verified.

### GNR-8 — Dimensionally broken inline substitution ∂ϑ_NY ~ H
- Legs: Gemini P6-C1.
- Verdict: **GNR**. The text assigns ∂ϑ_NY dimension +2, then substituted
  the dimension-+1 value H ~ 10⁻³³ eV.
- Closure: substitution corrected to the dimension-consistent background
  value ∂ϑ_NY ~ H₀² ~ 10⁻⁶⁶ eV² (pseudoscalar of dimension +1, Hubble-scale
  amplitude, evolving on the Hubble time). The displayed dimensionless ratio
  Eq. (2) was already consistent (verified by the Claude leg) and is
  unchanged.

### GNR-9 — No frozen commit hash / DOI in Data & Code Availability
- Legs: Gemini #4 (ESSENTIAL).
- Verdict: **GNR** (real reproducibility improvement; P1A precedent).
- Closure: scripts pinned to immutable repository commit
  `9b92721d5d7eb6601ebf48c49379318238b7100b` (the commit containing the
  exact cited files), plus the companion's archival deposit DOI
  10.5281/zenodo.21481838 (CC-BY-4.0).

### GNR-10 — Quoted Shapiro–Teixeira Ω coefficients are mistranscriptions (source-verified this round)
- Legs: Claude MINOR-5 (asked for a source audit; specifically flagged the
  Ω₂₄ γ² vs Ω₄₄ γ⁴ asymmetry for transcription check).
- Verdict: **GNR** — the audit was performed against the ar5iv render of
  arXiv:1402.4854 and found the v1C.0.3 values wrong. Source Eq. (42):
  Ω₂₄ = −81γ²/(1+γ²)² and Ω₄₄ = −(378+783γ²)/[20(1+γ²)²]; the paper had
  quoted Ω₄₄ = 81γ⁴/[16(1+γ²)²] and Ω₂₄ = 81γ²/[40(1+γ²)²] (garbled from
  neighboring entries Ω₂₂/Ω₃₄/Ω₁₃). Verified correct as quoted: λ₄ = γκ̃²(W·J)
  (Eq. 37), α₄ = −6/(1+γ²) (Eq. 41), the 1/(4π)² master-RG loop factor
  (Eq. 46), and Eq. (51) as the λ₄ flow driven by the Ω₄₄/Ω₂₄/Ω₃₄ family.
  Benedetti–Speziale Eq. (7) verified exact against arXiv:1111.0884
  (β_{γ²} = −(γ²−1)μ²κ̃²(23γ²+5)/(8π)², UV-attractive γ²=1 fixed point,
  divergent four-fermion coupling caveat).
- Closure: both Ω values corrected to the source; the illustrative ratio
  recomputed |Ω₄₄/α₄| = (378+783γ²)/[120(1+γ²)] ≈ 3.3 at γ ≈ 0.24 (replacing
  the stale 27γ⁴/[32(1+γ²)] ≈ 2.5×10⁻³) — which *strengthens* the "O(1)
  rational coefficient" claim. Margins unaffected (β(γ) enters only as an
  O(1) input; the closure carries ≥58 orders).
- Residual (recorded): ST Eq. (58) and the verbatim "unable to solve it in a
  completely satisfactory way" quotation could not be verified this round —
  the ar5iv render truncates after Eq. (51). DEFERRED-GENUINE: pre-submission
  quoted-equation audit against the published CQG PDF for Eq. 58 + quote.

### GNR-11 — α/M symbol collision (two roles, two M's)
- Legs: Claude MINOR-2.
- Verdict: **GNR** (clarity). Closure: third convention flag added to
  Sec. II stating the two roles explicitly, that every numerical occurrence
  uses the single R4-fitted anchor 10⁻²¹ GeV⁻¹, and that only the fitted
  combination enters any quantitative statement; β(γ)-vs-β disambiguation
  restated there once.

### GNR-12 — Fate of √−g ∇_μJ^{5μ} unstated
- Legs: Claude MINOR-4.
- Verdict: **GNR**. The zero-derivative construction rule silently excludes
  a gauge-invariant dimension-exactly-4 parity-odd density.
- Closure: explicit disposal added to Sec. V (exact total derivative
  ∂_μ(√−g J^{5μ}) — standard identity, zero EOM/vacuum contribution, anomaly
  content introduces FF̃ only outside minimal field content).

### GNR-13 — Two-thirds-column footnote
- Legs: Claude MINOR-6.
- Verdict: **GNR** (presentation). Closure: footnote 1 promoted to new
  Appendix B ("Parity Classification of the Route-2 Operator"), lightly
  condensed; Route-2 text now carries a one-sentence pointer.

### GNR-14 — Four-significant-figure agreement claim on a two-figure value
- Legs: Claude MINOR-7.
- Verdict: **GNR**. Closure: precision claim dropped ("in agreement with a
  frozen-coefficient analytic estimate"); the quoted 1.4×10⁻⁶ is unchanged
  (independently reproduced by the Claude leg).

### GNR-15 — Internal-bookkeeping parenthetical ("no Checks B or C ... artifact-matching")
- Legs: Gemini #3 (the page-14 kernel).
- Verdict: **GNR** (wording). Closure: condensed to plain language — the
  script's output tags label the two identities; the script contains no
  other checks. (The rest of Gemini #3 is dispositioned under SO-1 below.)

### RF-1 — "Embed the full enumeration or retract the completeness claim"
- Legs: Grok E3 (ESSENTIAL).
- Verdict: **RE-FLAG of disclosed limitation.** The paper states —
  abstract, Sec. V construction-rule paragraph, Sec. VI scope, App. A1 —
  that completeness is asserted from the construction rules and NOT proved
  by exhaustive symbolic enumeration, and that the released script verifies
  the two reduction identities only. No exhaustive enumeration exists to
  embed, and fabricating one is prohibited; retracting a claim the paper
  already scopes honestly is not owed. The Q1 condensation keeps one
  authoritative statement per surface.

### RF-2 — "Reclassify the R2/R3 closures as exploratory bounds, not no-go theorems"
- Legs: Grok M1.
- Verdict: **RE-FLAG of disclosed content.** v1C.0.3 already classified R2
  as "(III) Ansatz-level ... exploratory, not load-bearing" and R3 as
  "(II)+(III)" in Table II, with the same status stated in Sec. IV text and
  Sec. VI. The requested reclassification is the paper's existing
  classification. (Grok M2's residual kernel — sharpen the abstract's
  overall framing — is closed under GNR-3/GNR-4.)

### SO-1 — Version tag in \date, committed-artifact paths in Data & Code Availability
- Legs: Grok N1 (MINOR); Gemini #3 (page-1 and paths kernels).
- Verdict: **SCOPE-OPINION** (venue style). The `(Dated: ... vX.Y.Z)` stamp
  and served-draft version chips are required by standing directive G for
  every served draft (page 1 must show version+date); they are stripped at
  P-round submission packaging, which this draft has not reached.
  Repo-relative committed artifact paths in Data & Code Availability are the
  lab's reproducibility standard and P1A (published) precedent; GNR-9
  additionally pins them to an immutable commit. Disposition recorded; no
  in-draft edit owed at the R-round stage.

### FAL-1 — "B8/B14 double-listing is an internal inconsistency in the claimed total"
- Legs: Grok M3 (MAJOR).
- Verdict: **FALSIFIED.** The counting is uniform at every surface of the
  exact PDF: abstract ("thirteen distinct mechanism-class constraints —
  fourteen historical catalog entries, one subsumed by another"), Sec. III
  opening ("13 distinct mechanism-class constraints (14 historical entries,
  with B8 subsumed by B14)"), Table I caption ("14 catalogue entries (13
  distinct...); ... listed separately to preserve the historical
  mechanism-class catalog, but should not be counted as a separate
  mechanism-class constraint"), Fig. 1 caption, and the conclusions. Listing
  B8 as a historical entry while excluding it from the distinct count is the
  stated accounting, not a contradiction of it. Source: `main.tex` (v1C.0.3)
  abstract lines ~73–75, Sec. III lines ~245–247, Table I caption lines
  ~360–367, Fig. 1 caption lines ~343–356. (v1C.0.4 additionally fixes the
  *figure arrow* defect — GNR-7 — which is a different, real finding.)

### FAL-2 — "The body never recomputes the 58–60-order number; no table or appendix shows the arithmetic"
- Legs: Grok E2 (ESSENTIAL).
- Verdict: **FALSIFIED as stated.** The body displays the complete
  arithmetic chain for the Route-2 ratio: Eq. (2) with the explicit numeric
  evaluation α_em/4π ≈ 5×10⁻⁴ (5.8×10⁻⁴), H₀/M_Pl ~ 10⁻⁶¹,
  M_Pl·(α/M) ~ 10⁻², β_obs = 0.342° = 5.97×10⁻³ rad, ratio
  10⁻³·10⁻⁶¹/(10⁻²·6×10⁻³) ≈ 10⁻⁶⁰ — source: `main.tex` (v1C.0.3) lines
  ~650–670 — and the Route-3 integration inputs (κ̃² = 16πG,
  μ_UV = 10¹⁶ GeV, γ ≈ 0.24 → 1.4×10⁻⁶) in Sec. IV B; the Claude leg
  independently reproduced both numbers from the displayed inputs. The
  legitimate kernel inside E2 — the abstract attributed the R2 margin to the
  wrong observable — is real and closed as GNR-4.

## Ledger totals

| Verdict | Count | Items |
|---|---|---|
| GENUINELY-NEW-REAL (closed in v1C.0.4) | **15** | GNR-1 … GNR-15 |
| RE-FLAG (source-cited disposition) | 2 | RF-1, RF-2 |
| SCOPE-OPINION (venue; dispositioned) | 1 | SO-1 |
| FALSIFIED (source-cited) | 2 | FAL-1, FAL-2 |
| **Total canonical items** | **20** | (Grok M2 dedupes into GNR-3/GNR-4) |

Deferred-genuine (pre-submission checklist, not open board findings):
1. ST Eq. (58) + "unable to solve … satisfactory way" verbatim-quote
   verification against the published CQG PDF (render truncation blocked it
   this round; all other ST/BS quoted equations now source-verified).
2. Venue-length condensation toward the ~12-pp CQG norm (D/P-round work).

## Closure evidence (v1C.0.4)

- All 15 GNR closures landed in `arxiv/paper1c_nogo_survey/main.tex`
  (\paperVersion v1C.0.4, dated 2026-08-06). Corrected math sources:
  Fierz — `research/theory_audit/fierz_adjudication_2026_08_05.{py,json,md}`
  ([L08], [L12], [L15], [L16]) and published P1A `arxiv/paper1a_ech_nogo.tex`
  App. fierz; B14 — P1A `sec:transparency` (carried faithfully, attributed);
  ST/BS coefficients — arXiv:1402.4854 Eqs. 37/41/42/46/51 and
  arXiv:1111.0884 Eq. 7 (fetched renders); hierarchy arithmetic — direct
  computation from the paper's own fixed inputs. Nothing invented.
- Compile: pdflatex 4-pass, **0 errors / 0 undefined references / 0 overfull
  hboxes**, 17 pages.
- /latex-audit visual pass: all 17 pages rendered at 110 DPI; title block,
  Fig. 1 (new arrows verified), Tables I–III, App. C matrix, App. D theorem
  inspected — no column overflow, no overlap. All embedded GitHub URLs
  resolve to existing repo files; commit-pin URL is the real HEAD at edit
  time.
- Mirrors byte-identical (md5 `6c9a8a2cd1f80c6a5d8dc55042e64b79`):
  `arxiv/paper1c_nogo_survey/main.pdf` =
  `site/public/papers/paper1c_nogo_survey_v1C.0.4.pdf` =
  `public/papers/paper1c_nogo_survey_v1C.0.4.pdf`.
  SHA-256 `7ec5f2218fa26eaf03252142e3576ccd0e76797327f90765f138b242cc6e8055`.
- Site: `site/src/data/papers.ts` supportingLinks href → v1C.0.4 (+ honest
  description); `site/src/data/reviewTimeline.ts` round entry (failed legs
  disclosed); `project-context/draft_paper_registry.json` served_aliases →
  v1C.0.4. `npx next build` passes (see closure commit).

## Next gate

R2 **confirmation board** on the exact v1C.0.4 PDF (sha `7ec5f221…`): all
three active legs re-run fresh; exit test per directive H-refined is 0
genuinely-new-real findings.
