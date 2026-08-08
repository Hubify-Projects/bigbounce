# P1C v1C.0.8 — R6 confirmation-board truth audit (verdict-first) and v1C.0.9 closure record

- **Round:** ROUND_2026-08-07-P1C-v1C.0.8-EXACTPDF-385158dd-R6CONF — the R6
  confirmation board on `arxiv/paper1c_nogo_survey/main.tex`, run against the
  R1 + R2 + R3 + R4 + R5 disposition ledgers
  (`INT_v3/ROUND_2026-08-06-P1C-v1C.0.3-EXACTPDF-85e53832/P1C_v1C.0.3_truth_audit.md`,
  `INT_v3/ROUND_2026-08-06-P1C-v1C.0.4-EXACTPDF-7ec5f221-R2CONF/P1C_v1C.0.4_R2_truth_audit.md`,
  `INT_v3/ROUND_2026-08-06-P1C-v1C.0.5-EXACTPDF-a770491d-R3CONF/P1C_v1C.0.5_R3_truth_audit.md`,
  `INT_v3/ROUND_2026-08-07-P1C-v1C.0.6-EXACTPDF-fc23872d-R4CONF/P1C_v1C.0.6_R4_truth_audit.md`,
  `INT_v3/ROUND_2026-08-07-P1C-v1C.0.7-EXACTPDF-f085023f-R5CONF/P1C_v1C.0.7_R5_truth_audit.md`).
- **Exact artifact:** v1C.0.8 PDF, SHA-256
  `385158dd6351a515d1d0d73bdbbd7cc3b61ed1df90b88f067bed54d40778c575`,
  18 pp (sha verified against the working tree before any edit).
- **Date:** 2026-08-06 (round dir label 2026-08-07). Auditor: Claude
  (Fable 5) worker per CLAUDE.md directives B / H-refined / N. Rule
  applied: a finding that re-flags an R1–R5-dispositioned item is RE-FLAG
  unless the reviewer adds a genuinely new angle.

## Legs (raw receipts)

| Leg | Model | File | Verdict |
|---|---|---|---|
| Claude INT (Opus-tier subagent) | claude opus | `INT_v3/ROUND_2026-08-07-P1C-v1C.0.8-EXACTPDF-385158dd-R6CONF/P1C_claude_r6_leg.md` | **MINOR REVISIONS** (1 MAJOR / 8 MINOR) — independent verification log again reproduced every load-bearing number (Route-3 1.38×10⁻⁶; R1 3.5×10⁻⁶⁹/3.8×10⁻⁶⁹; Eq.(2) 1.7×10⁻⁶⁰/1.7×10⁻⁶²; hierarchy 8.6×10¹²²; Fierz chain; counts) |
| Grok API | grok-4.3 | `ROUND_2026-08-07-P1C-v1C.0.8-EXACTPDF-385158dd-R6CONF_P1C_Grok_brutal.md` | **REJECT** (4 ESSENTIAL / 4 MAJOR / 4 MINOR-NIT) |
| Gemini API | gemini-3.1-pro-preview | `ROUND_2026-08-07-P1C-v1C.0.8-EXACTPDF-385158dd-R6CONF_P1C_Gemini_cosmology.md` | **MAJOR REVISIONS** (1 ESSENTIAL / 2 MAJOR incl. pass-2 / 4 MINOR-NIT incl. pass-2) |

**Failed legs (preserved as failure evidence, never counted, never hidden):**

- Perplexity leg: FAILED
  (`ROUND_2026-08-07-P1C-v1C.0.8-EXACTPDF-385158dd-R6CONF_P1C_Perplexity_citations.md`
  is a failure record). Optional leg per directive I1; recorded as failed,
  never a verdict.

## Critical adjudication — the companion-dependency MAJORs (Claude M1, Gemini M1, kernels of Grok E2/E4)

The five prior rounds dispositioned the wholesale "absorb everything or
withdraw" demand as a RE-FLAG (R1 GNR-2 / R2-RF-2 / R3-RF-2 / R4-RF-1 /
R5-RF-4): the sole Tier-I leg (B14) is self-contained in App. D, and
reproducing the whole companion would duplicate it. R6 sharpened the
demand into something new and **bounded**: Claude M1 identifies the
specific *load-bearing Tier-II inputs* still resting on the unrefereed
Zenodo companion — the torsion-elimination normalization and the
−3κ/16 contact coefficient, and the R1 benchmark κn_ψ²/ρ_Λ ≈ 3.6×10⁻⁶⁹
— and offers the closable fork "(b) reproduce the load-bearing
derivations in an appendix here"; Gemini M1 asks for exactly the same
thing for the R1 benchmark ("a brief, self-contained derivation …
in a new Appendix").

**Adjudication: partially RE-FLAG (the wholesale demand and the
companion-sequencing kernel remain dispositioned), GNR for the bounded
in-appendix core.** Both named derivations are compact in the companion
source and can be carried faithfully — exactly the R1/B14 App-D
precedent. **Closed (v1C.0.9) as new Appendix E**, extracted verbatim-
faithful from `arxiv/paper1a_ech_nogo.tex` (the P1A companion source):

1. *App. E.1 — torsion elimination and the contact coefficient* (from
   P1A `sec:theory`, lines ~1791–1874): the bivector dual
   Q_γ = ⋆ + γ⁻¹𝟙 with inverse [γ²/(1+γ²)](γ⁻¹𝟙 − ⋆) (exists for
   1+γ² > 0 — the same operator as App. D Step 2); the algebraic sourced
   Cartan equation; the FMT contorsion solution (FMT Eq. 17); the FMT
   back-substitution L_int = −(3/2)πG[γ²/(1+γ²)]J₅² (FMT Eq. 23); the
   normalization bridge 4πG = κ/2, −(3/2)πG = −3κ/16; hence
   L_4ψ = −(3κ/16)[γ²/(1+γ²)](J⁵·J⁵), with the γ→∞ Einstein–Cartan
   limit giving the gap-equation convention G_s = −3κ/16 of App. C.
2. *App. E.2 — the R1 finite-density benchmark* (from P1A
   `sec:r1_njl`, lines ~2655–2711): ρ_4f ≡ κn_ψ² = 8πn_ψ²/M_Pl²;
   with ħc = 1.9733×10⁻⁵ eV·cm and M_Pl = 1.2209×10²⁸ eV,
   κn_ψ² ≃ 1.0×10⁻⁷⁹ (n_ψ/100 cm⁻³)² eV⁴ and κn_ψ²/ρ_Λ ≃ 3.6×10⁻⁶⁹ at
   the companion's ρ_Λ ≈ (2.3 meV)⁴; the 3/16-weighted value
   1.9×10⁻⁸⁰ eV⁴ = 6.7×10⁻⁷⁰ ρ_Λ; the (2.25 meV)⁴ → 3.9×10⁻⁶⁹
   cross-normalization (R4-GNR-3); and the companion's own scope
   honesty (elevated normalization; no composite/EOS inference).
   Recomputation receipt for this audit: 100 cm⁻³ = 7.684×10⁻¹³ eV³,
   κ = 1.686×10⁻⁵⁵ eV⁻², κn_ψ² = 9.96×10⁻⁸⁰ eV⁴, /2.8×10⁻¹¹ = 3.6×10⁻⁶⁹ ✓.

Credit is explicit ("Following the same faithful-extraction convention
as Appendix D … nothing below is new to this survey; the derivations
follow the companion, which in turn follows Freidel, Minic, and
Takeuchi"). Nothing invented. The companion results **too long to carry
faithfully** — the mean-field NJL gap-equation analysis, the
tensor-sector extension / second-order Holst verification of B14, and
the R4 spectator-ALP consistency check — are dispositioned
**deferred-genuine (refereed-companion gate)**, with honest wording now
in Sec. I: they are used only with explicit not-peer-reviewed labeling
and their refereeing is part of the companion's own publication path.
Cross-references updated: Sec. I relation paragraph, Sec. II
elimination paragraph, Table II R1 cell, App. C convention note.

## Deduplicated finding ledger (canonical items, cross-leg map, verdicts)

Verdict key: **GNR** = genuinely-new-real (real edit owed and landed in
v1C.0.9) · **RE-FLAG** = re-flag of an R1–R5-dispositioned or disclosed
item · **FALSIFIED** = disproved against the cited source/computation.

### R6-GNR-1 — Load-bearing Tier-II companion inputs not refereeable from this manuscript (bounded in-appendix core)
- Legs: Claude M1; Gemini M1; the R1-benchmark/self-containment kernels
  of Grok E2 and E4.
- Verdict: **GNR for the bounded core; RE-FLAG for the wholesale
  demand** — see the critical-adjudication section above.
- Closure (v1C.0.9): new Appendix E (E.1 contact coefficient, E.2 R1
  benchmark), faithful extraction from the P1A source with explicit
  credit; deferred-genuine wording for the too-long pieces in Sec. I.

### R6-GNR-2 — Eq. (2) as printed is a false equality (LHS label omits the second normalization)
- Legs: Gemini pass-2 M2; Claude m5 (motivation-placement kernel).
- Verdict: **GNR (closure-insufficiency of R2-GNR-7, a genuinely new
  angle).** R2-GNR-7 closed the double-division ambiguity with
  explanatory text but left the display's LHS as
  Δθ_one-loop/Δθ_obs while the RHS divides additionally by
  M_Pl(α/M) — as an equation, false as written; Gemini's fix offer
  ("the LHS must be written as Δθ/(Δθ_obs · M_Pl α/M)") is exact.
- Closure (v1C.0.9): Eq. (2) LHS now reads
  Δθ_one-loop/(β_obs [M_Pl(α/M)]), with the bookkeeping motivation
  stated at the display (Claude m5's ask): the double normalization
  states suppression relative to the fitted-coupling benchmark, the
  weaker/conservative normalization. The later duplicate explanation
  trimmed; the direct angle-only contraction (2×10⁻⁶²) retained; all
  margins unchanged (≈60 / ≥58 / ≳48 at every surface).

### R6-GNR-3 — ∇·J⁵ disposal overlooks the gravitational chiral anomaly
- Legs: Claude m2 (sole leg).
- Verdict: **GNR** (technically incorrect sentence, genuinely new — no
  prior round touched the anomaly content of the R2-GNR/R1 GNR-12
  disposal). The v1C.0.8 text claimed anomalous content introduces FF̃
  "only once electromagnetic fields are added"; the
  Kimura–Delbourgo–Salam gravitational contribution
  ∇_μJ^{5μ} ⊃ c_grav ε^{μνρσ}R_{μναβ}R_{ρσ}^{αβ} is present within the
  minimal field content. The closure is unaffected: RR̃ is exactly O3
  (Pontryagin), already in the basis and disposed as an exact total
  derivative.
- Closure (v1C.0.9): sentence corrected to route the gravitational
  anomaly content to O3 explicitly, with the coefficient left as "a
  known pure-number coefficient" (never-fabricate: no numeric quoted
  without a verified source) and two real references added
  (Kimura, Prog. Theor. Phys. 42, 1191 (1969); Delbourgo–Salam,
  Phys. Lett. B 40, 381 (1972)); FF̃ still correctly requires
  non-minimal field content.

### R6-GNR-4 — Frozen-artifact pin carries a known content divergence
- Legs: Claude m4 (sole leg).
- Verdict: **GNR** (new angle on the R3-GNR-1/R4-GNR-7/R5-GNR-1
  footnote lineage: a frozen-artifact claim should not carry a known
  drift when a matching pin exists). Verified for this audit:
  all four cited artifacts are bit-identical between commit
  `c80b7487b01fe54da0ea410c81a1d25a25815e25` (= HEAD at edit time, on
  `origin/main`) and the working tree (`git diff` empty; `git ls-tree`
  receipts in the round log).
- Closure (v1C.0.9): Data & Code pin moved to `c80b7487b01f` with the
  in-text statement "whose copies of all four files are identical to
  the current repository head"; the drift footnote retired (no longer
  true, hence no longer carried — honesty by fact, not by narration,
  per Q1).

### R6-GNR-5 — β_obs used without detection-significance context
- Legs: Claude m6 (sole leg).
- Verdict: **GNR** (genuinely new; no prior round flagged detection
  status). Recomputed: 0.342/0.094 = 3.64σ; 0.215/0.074 = 2.9σ.
- Closure (v1C.0.9): Sec. IV C now states both are statistical
  indications rather than established detections (≈3.6σ / ≈2.9σ) and
  that a smaller or vanishing true signal only widens the Eq. (2)
  margin.

### R6-GNR-6 — Fig. 1 caption's attribution sentence remains hard to map onto the drawing
- Legs: Claude m7; Grok m4 (dedupe — both target the caption's
  attribution prose; Grok quotes the confusing "otherwise not resolved
  at box granularity" clause).
- Verdict: **GNR** (closure-insufficiency of R4-GNR-6's caption text —
  the in-figure labels exist, but the caption sentence describing them
  was itself the obstacle; two fresh legs stumbled on it).
- Closure (v1C.0.9): caption rewritten plainly — the edge labels give
  the attribution directly: upper Branch-H→R1 arrow = B8 and B14
  (label "B8, B14"); lower fan to R2/R3/R4 = B14 alone (label "B14");
  the meta-commentary clause removed.

### R6-GNR-7 — `theory_audit` directory tag in formal prose + "the two … listed above" ambiguity
- Legs: Gemini N2; Gemini N3 (same passage, one closure).
- Verdict: **GNR** (the phrasing was introduced by the R5-GNR-1
  closure — genuinely new at R6; distinct from the R2-RF-9 artifact-
  *paths* disposition, which stands: the monospace \artifact links
  remain).
- Closure (v1C.0.9): "the third and fourth files listed above (the
  independent Fierz-adjudication script and its human-readable
  report)" — directory-name adjective removed, the two/four ambiguity
  resolved.

### R6-GNR-8 — M_Pl²κ² = κ used as an exact identity at full-mass-convention sites; headline numerics not convention-tagged
- Legs: Claude m3 (sole leg).
- Verdict: **GNR as a bounded tagging defect; RE-FLAG for the general
  mixed-bookkeeping complaint** (R3-GNR-2 closed the κ definition and
  the §II site-by-site disclosure; the genuinely new angle is the two
  App-A1/Table-III sites that use M_Pl²κ² = κ as if exact, and the
  untagged Route-3 numeric).
- Closure (v1C.0.9): both sites now read "exact in the reduced-mass
  convention κ = M̄_Pl⁻² … order-of-magnitude at the full mass"; the
  Route-3 1.4×10⁻⁶ tagged "(evaluated with the full M_Pl …, per the
  Sec. II convention)". No number changed (the Claude leg itself
  verified each numeric individually harmless).

### R6-GNR-9 — α_em convention unstated in the Route-2 arithmetic
- Legs: Grok m3 (sole leg).
- Verdict: **GNR-nit** (bounded; R3-GNR-4 fixed the rounding but never
  stated which α_em). Closure (v1C.0.9): "using the Thomson-limit
  fine-structure constant α_em ≃ 1/137; a running α_em(μ) evaluated at
  any higher scale differs by an O(1) factor immaterial at these
  margins" (α_em(M_Z) ≈ 1/128; ratio 1.07 — O(1), inside the stated
  conservatism allowance).

### R6-RF-1 — Version string/date on the title page
- Legs: Grok E1; Gemini N1.
- Verdict: **RE-FLAG** of R1 SO-1 / R2-RF-1 / R3-RF-1 / R4-RF-7 /
  R5-RF-5: the (Dated: … vX.Y.Z) stamp is required by standing
  directive G on every served draft; stripped at P-round packaging.

### R6-RF-2 — "Abstract asserts closures stronger than the body's tiers; rewrite to the weakest tier"
- Legs: Grok E3.
- Verdict: **RE-FLAG** of R1 RF-2 / R3-RF-4 / R5-RF-1: the abstract
  itself prints the demanded qualification ("only the
  perturbation-transparency result is a Tier-I rigorous theorem, and
  the survey is a channel-level, not operator-level, closure"), and
  every quantitative claim carries its per-route metric and endpoint
  labels (R1 GNR-4, R3-GNR-3 closures).

### R6-RF-3 — "Not self-contained; make independent of [1] or withdraw"
- Legs: Grok E4; Grok E2 (the "cannot recompute any quoted orders"
  overstatement); Claude M1's venue fork (a).
- Verdict: **RE-FLAG** of the R1 GNR-2 family — now further narrowed by
  the R6-GNR-1 closure: B14 self-contained since v1C.0.4 (App. D), the
  contact coefficient and R1 benchmark self-contained as of v1C.0.9
  (App. E), the Route-2/Route-3 arithmetic chains displayed in-body
  since R1 (falsified family R1 FAL-2 / R5-RF-3; the Claude R6 leg
  again reproduced every displayed number). Residual imports are
  deferred-genuine behind the refereed-companion gate with honest
  in-paper wording (Sec. I). Companion sequencing remains directive-P
  publishing-phase work.

### R6-RF-4 — Venue length ("condense to ≤8–10 pp"); abstract length/density
- Legs: Grok M1; Claude m1.
- Verdict: **RE-FLAG** of R1 GNR-3 residual / R2-RF-7 / R3-RF-7 /
  R4-RF-10: venue-length condensation and abstract compression are
  standing D/P-round work on the pre-submission checklist. (Note: the
  R6-GNR-1 closure adds pages in the honest direction — self-
  containment was the boards' higher-priority demand.)

### R6-RF-5 — "Novelty accounting: several barriers are re-packaged literature"
- Legs: Grok M2.
- Verdict: **RE-FLAG** of R2-RF-8 / R3-RF-8 / R2-GNR-1's landed
  decoupling: the Sec. III classification states exactly which entries
  are general arguments (B5–B7, B10, B13 named; B9 heuristic), novelty
  is defined as a provenance label with the eight-of-nine caveat, and
  Sec. VI repeats the accounting.

### R6-RF-6 — "Margins rest on an uncomputed O(1) normalization and imported one-loop results; label as imported from [1]"
- Legs: Grok M3.
- Verdict: **RE-FLAG** of R2-RF-5 / R5-RF-2 for the disclosed-status
  kernel (Tier-III labels + the ≥48-order robustness statement), plus
  a **partial FALSIFICATION**: the one-loop inputs are imported from
  the *published* Shapiro–Teixeira (CQG 31, 185002 (2014), Eqs. 37,
  41–42, 46, 51) and Benedetti–Speziale (J. Phys. Conf. Ser. 360,
  012011 (2012), Eq. 7) — refs [2]/[3], not the unrefereed companion
  [1] — and the demanded "not re-derived here" labeling is the paper's
  existing text ("grounded in the explicit one-loop computation …
  What the one-loop analysis does not fix is the single absolute
  normalization … treated as a bounded EFT input").

### R6-RF-7 — "Evidentiary column mixes incommensurable categories; adopt a single taxonomy"
- Legs: Grok m2.
- Verdict: **RE-FLAG** of R2-SO-1: the three-tier scale is explicitly
  defined (Sec. IV "Evidentiary status of each leg") and uniformly
  applied; replacing it with theorem/lemma vocabulary would overstate.

### R6-RF-8 — "Abstract's ~67-order endpoint needs a one-line arithmetic trace"
- Legs: Grok m1.
- Verdict: **RE-FLAG** of the R1 FAL-2 falsified family / R3-GNR-3's
  landed endpoint labels: the body displays the full integration
  inputs and propagation (Sec. IV B), the abstract states both
  endpoints' provenance, and the Claude R6 leg independently
  reproduced 1.38×10⁻⁶ and the 61/67 margins from in-paper inputs.
  Abstracts do not carry arithmetic chains.

### R6-RF-9 — "Mint the survey's own Zenodo DOI now; a promise is not acceptable"
- Legs: Gemini E1.
- Verdict: **RE-FLAG** of R2-SO-2 / R3-RF-6 / R4-RF-8 / R5-GNR-2's
  disposition: the deposit is an external, Houston-gated side effect
  executed at P-round packaging; fabricating a DOI in-paper is
  prohibited. Carried deferred-genuine, unchanged. The in-paper
  statement remains the honest "planned prior to publication".

### R6-RF-10 — "Confirm every imported equation number against the journal versions"
- Legs: Claude m8 (explicitly a due-diligence request).
- Verdict: **RE-FLAG** of R1 GNR-10's completed source audit + its
  recorded residual (ST Eq. 58 + verbatim quote vs the published CQG
  PDF — ar5iv render truncates), carried deferred-genuine on the
  pre-submission checklist; R4-RF-9 re-verified the quoted Eqs. 41/42/7
  against fresh ar5iv fetches, and the paper itself flags the one
  "arXiv version" numbering.

### R6-FAL-1 — "The sole Tier-I result is proved in the companion; the present text only cites it"
- Legs: Grok M4.
- Verdict: **FALSIFIED against the exact PDF.** Appendix D has carried
  the full theorem statement and 4-step proof self-contained since
  v1C.0.4 (R1 GNR-2 closure) — compiled v1C.0.8 p. 17–18; `main.tex`
  `app:transparency` (statement, zero-spin → T=0 via the invertible
  bivector operator, Levi-Civita reduction, Bianchi vanishing, scope
  exclusions). The Claude R6 leg independently verified the proof
  logic ("Sound within stated scope"). No edit owed.

### R6-FAL-2 — "August 2026 dates are anachronistic typos for 2024"
- Legs: Gemini pass-2 N4.
- Verdict: **FALSIFIED against the calendar.** The review date is
  2026-08-06; the manuscript date and the "2026 releases" acknowledgment
  are current, not futuristic. (Reviewer knowledge-cutoff artifact.)
  No edit owed.

## Ledger totals

| Verdict | Count | Items |
|---|---|---|
| GENUINELY-NEW-REAL (closed in v1C.0.9) | **9** | R6-GNR-1 … R6-GNR-9 |
| RE-FLAG (R1–R5-dispositioned / disclosed; source-cited; one with partial falsification) | 10 | R6-RF-1 … R6-RF-10 |
| FALSIFIED (fresh; source-cited) | 2 | R6-FAL-1, R6-FAL-2 |
| **Total canonical items** | **21** | (Claude M1 ≡ Gemini M1 ≡ kernels of Grok E2/E4 → GNR-1; Gemini M2 ≡ Claude m5 → GNR-2; Claude m7 ≡ Grok m4 → GNR-6; Gemini N2 ≡ N3 → GNR-7; Grok E1 ≡ Gemini N1 → RF-1; Grok M1 ≡ Claude m1 → RF-4) |

Deferred-genuine (pre-submission checklist, carried/updated):
1. Mint the archival deposit / version DOI for the P1C script set at
   P-round (R2-SO-2 / R6-RF-9). External side-effect, Houston-gated.
2. Refereed-companion gate: the companion-only results (NJL gap
   analysis, tensor-sector B14 extension, R4 spectator check) carry
   honest not-peer-reviewed wording until the companion is refereed
   (R6-GNR-1 disposition); companion arXiv-sequencing per directive P.
3. (Carried unchanged) Real mechanized operator-basis enumeration per
   R3-GNR-1's adjudication — or retain the downgraded framing at
   submission; ST Eq. (58) + verbatim-quote check vs the published CQG
   PDF (R6-RF-10); venue-length condensation (D/P rounds).

## Closure evidence (v1C.0.9)

- All 9 GNR closures landed in `arxiv/paper1c_nogo_survey/main.tex`
  (\paperVersion v1C.0.9, dated 2026-08-06) + `references.bib`
  (Kimura1969, DelbourgoSalam1972 — real standard citations for the
  gravitational chiral anomaly). Correction sources: the P1A companion
  source `arxiv/paper1a_ech_nogo.tex` (`sec:theory` lines ~1791–1874;
  `sec:r1_njl` lines ~2655–2711 — App. E carried verbatim-faithful with
  credit); Gemini's own exact fix offer for the Eq. (2) LHS; the
  standard Kimura–Delbourgo–Salam result (coefficient deliberately not
  quoted numerically — never-fabricate); `git diff`/`git ls-tree`
  receipts for the c80b7487b01f repin; direct recomputation
  (3.64σ/2.9σ; α_em(M_Z)/α_em ≈ 1.07; benchmark 9.96×10⁻⁸⁰ eV⁴ →
  3.6×10⁻⁶⁹). Nothing invented; no margin, count, or headline number
  changed.
- Compile: pdflatex 4-pass (with bibtex), **0 errors / 0 undefined
  references / 0 overfull hboxes**, 20 pages (App. E adds ~2 pp — the
  honest direction: self-containment outranked venue length per the
  boards' own priority).
- /latex-audit visual pass: changed pages rendered at 110 DPI — p. 1
  (title v1C.0.9), p. 2 (Sec. I companion paragraph), p. 4 (Fig. 1
  caption), p. 6–7 (Eq. (2) corrected LHS + Thomson-limit note), p. 8
  (Route-3 full-M_Pl tag), p. 9 (β_obs significance), p. 10 (Table II
  R1 App-E pointer), p. 11 (∇·J⁵ gravitational-anomaly routing), p. 13
  (Data & Code repin, no footnote, third/fourth-files boundary), p. 16
  (Table III tagged caption), p. 18–19 (new App. E, Eqs. E1–E5),
  p. 19–20 (references [1]–[24] incl. Kimura/Delbourgo–Salam) — no
  column overflow, no overlap. The one new URL (the c80b7487b01f
  commit tree) resolves: the commit is HEAD of `origin/main` at edit
  time.
- Mirrors byte-identical (md5 `eab47932a69723802f3644d45b4965f5`):
  `arxiv/paper1c_nogo_survey/main.pdf` =
  `site/public/papers/paper1c_nogo_survey_v1C.0.9.pdf` =
  `public/papers/paper1c_nogo_survey_v1C.0.9.pdf`.
  SHA-256 `b4d73f94621035ebf5f2e724e714c2f19283835748c7c577905a4e02cf890c47`.
- Site: `site/src/data/papers.ts` supportingLinks href → v1C.0.9 (+ honest
  description); `site/src/data/reviewTimeline.ts` R6 round entry (failed
  Perplexity leg disclosed); `project-context/draft_paper_registry.json`
  served_aliases → v1C.0.9. `npx next build` passes (see docs commit).

## Convergence read (directive H-refined)

R6 surfaced **9 genuinely-new-real findings** (target: 0). The paper is
therefore **NOT converged**: an **R7 confirmation board on the exact
v1C.0.9 PDF (sha `b4d73f94…`)** is required, with all active legs re-run
fresh and the exit test again 0 genuinely-new-real. Context for
calibration, not verdict-softening: the round's one MAJOR-grade closure
(App. E) resolves the boards' longest-running structural demand by
faithful extraction rather than new derivation; 6 of the 9 are
single-leg wording/tagging/caption items; 2 are closure-insufficiencies
of earlier fixes (Eq. (2) LHS; Fig. 1 caption); the only physics-content
correction (the gravitational anomaly routing) leaves the closure
unchanged because RR̃ = O3; and two fresh falsifications (Grok's
App-D-only-cited claim, Gemini's 2026-date claim) were disproved with
receipts. But the count is the count, and the gate is honest.
