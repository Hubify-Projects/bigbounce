# EXT20 — External Referee Round Batch Truth Audit (final pre-arXiv gate)

**Audit lead:** Opus truth-audit + synthesis (EXT20 final gate)
**Date:** 2026-06-18 (America/Los_Angeles)
**Scope:** All 6 papers. Vendor legs = Gemini 2.5-pro (cosmology), Grok 4.3 (brutal, image-rasterized), OpenAI gpt-5 (methodology, native PDF + pass-2). **Perplexity FAILED on all 6** (BadRequestError 400: content > 100KB cap) — zero citation findings produced; same tool-level failure as R40.
**Opus external referee leg (separate):** UNANIMOUS accept — P1A Minor-accept-leaning, P1B ACCEPT, P2 Accept, P3 Accept, P4 Accept, P5 Accept.
**Canonical versions audited:** P1A v1A.0.78 · P1B v1B.0.74 · P2 v1.7.69 · P3 v3.1.112 · P4 v1.0.188 · P5 v0.1.81.

**Prior context:** Internal R40 (`R40_*_TRUTH_AUDIT.md`) exhaustively ground-truthed all 6; 3 cosmetic closures applied and **verified landed on-disk this audit**:
- P1A v78 — V1/V2 review-process prose stripped (`\paperVersion v1A.0.78`, changelog L50 confirms).
- P3 v112 — NANOGrav path `nanograv_mcmc/` → `pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/` (L1334 `\artifact{}`, git-tracked).
- P5 v81 — residual V-Web→T-Web labels (L810 nomenclature note, L2900 `n_{\rm T\mbox{-}Web}`).

Protocol: every distinct EXT20 finding cross-referenced against the R40 audit; already-adjudicated → **DUPLICATE**; genuinely NEW → ground against on-disk source. Verdicts: VERIFIED-OPEN / STALE / MISLABELED / OUT-OF-SCOPE / OPINION / DUPLICATE / N-A.

---

## Per-paper finding tables

### P1A — ECH chirality no-go (v1A.0.78)
EXT20 verdicts: Grok REJECT, Gemini MAJOR-REV, OpenAI streamlined-revision. **All themes are R40 DUPLICATEs.**

| EXT20 finding | Vendor | R40 cross-ref | Verdict |
|---|---|---|---|
| Pontryagin/Holst-dual "math error" | Gemini-E1 echo | R40 Gemini-E1 MISLABELED (reviewer math error; documented false-positive class) | DUPLICATE → MISLABELED |
| Companion papers "in preparation" [2,6,23,46] not self-contained | OpenAI/Gemini/Grok | R40 OAI-E4/GEM-E2/GROK-E4 OUT-OF-SCOPE (6-paper concurrent program) | DUPLICATE → OUT-OF-SCOPE (SUBMISSION-DAY arXiv IDs) |
| 13-barriers / B8-subsumed overstated | OpenAI/Grok | R40 OAI-M8/GROK-M2 STALE (softening already in PDF) | DUPLICATE → STALE |
| Abstract stronger than body (closure/f_NL/β) | Grok | R40 GROK-E1/2/3 STALE | DUPLICATE → STALE |
| 29pp too long, streamline to ~18-20pp | OpenAI/Grok | R40 length-note OPINION | DUPLICATE → OPINION |
| Version-history prose footnotes | OpenAI-E1/E2 | **R40 V1/V2 — CLOSED in v78 (verified on-disk)** | RESOLVED |
| Perplexity citation forensics | — | call FAILED (100KB) | N-A |

**P1A: 0 VERIFIED-OPEN. 0 blockers.**

---

### P1B — MCMC companion (v1B.0.74)
EXT20: Grok REJECT, Gemini MAJOR-REV (structural), OpenAI DOI/PR4-rerun. **All R40 DUPLICATEs.**

| EXT20 finding | Vendor | R40 cross-ref | Verdict |
|---|---|---|---|
| Restructure interleaved ΛCDM vs w0wa MCMC (P1B-M1) | Gemini | New phrasing of R40 W0WA-σ region; w0wa walled off from abstract + headline Table I | OPINION (structural preference, non-load-bearing) |
| ECH coupling "inserted by hand, not derived" → REJECT | Grok | R40 ECH-DERIVATION STALE/MISLABELED (paper's own thesis: generic ALP check, not ECH-distinctive) | DUPLICATE → MISLABELED |
| Frozen-chain DOIs "pending" | OpenAI/Grok | R40 DOI-PENDING OUT-OF-SCOPE | DUPLICATE → SUBMISSION-DAY |
| Re-run frozen chains PR4-consistent low-ℓ EE / add column | OpenAI | R40 SN-CTRL / NaMaster-extras MISLABELED/OPINION (non-load-bearing diagnostic) | DUPLICATE → OPINION |
| Promote inverse-variance estimator / rename χ²→S(β) | OpenAI/Gemini | R40 WEIGHTED-EST MISLABELED (legit preference, not defect) | DUPLICATE → OPINION |
| "each other's" grammatical ambiguity (MINOR) | Gemini | copyedit, rendered-PDF | OPINION |
| Perplexity | — | FAILED | N-A |

**P1B: 0 VERIFIED-OPEN. 0 blockers.**

---

### P2 — SPHEREx f_NL sensitivity recast (v1.7.69)
EXT20: Grok REJECT, Gemini MAJOR-REV (**one NEW specific Table IV claim**), OpenAI MAJOR-REV.

| EXT20 finding | Vendor | R40 cross-ref | Verdict |
|---|---|---|---|
| **P2-M1: Table IV e-correction row "≤0.1σ" understates by ~4× — should be ~0.4σ** | Gemini (NEW; R40 Gemini was ACCEPT-minor) | NOT in R40 | **VERIFIED-OPEN → TRIVIAL-MICRO** (see below) |
| "sensitivity recast not independent forecast" / Fisher not recomputed | OpenAI/Grok | R40 known recast category error | DUPLICATE → MISLABELED |
| BF rests on single σ_theory=1.0 prior | Grok-M2 | R40: BF labeled "illustrative, not definitive" (L575); prior-width grid present | DUPLICATE → OPINION |
| Zenodo DOI / artifact manifest "at submission" | OpenAI-E1/E10 | R40 E1 OUT-OF-SCOPE | DUPLICATE → SUBMISSION-DAY |
| 29pp too long for a recast | OpenAI/Grok | R40 length OPINION | DUPLICATE → OPINION |
| Abstract buries 2.6σ floor / remove BF numbers | Grok-E1/E3 | R40 STALE/OPINION (floor in abstract ≥3×) | DUPLICATE → STALE |
| Perplexity | — | FAILED | N-A |

**P2-M1 verification (NEW, ground-truthed on-disk):**
- Table IV row at `02_full_draft.tex:956` reads `$\epsilon$-correction … $\lesssim 0.1\sigma$ effect`.
- Paper's OWN derivation (L987): conservative endpoint shift `κ_ε|Δε| ≈ 80×0.0045 ≈ 0.36` in f_NL.
- Significance impact: `|Δf_NL|·r/σ = 0.36×0.84/0.7 = 0.43σ`. Gemini's ~0.4σ is **arithmetically correct**; the table's `≤0.1σ` understates ~4×.
- **BUT non-load-bearing:** L987/L993 explicitly state this shift is "well inside the recommended σ_theory=1.0 bounce prior" and "no Bayes-factor conclusion in Sec. VIII hinges on it." Headline 5.2–5.5σ / 2.6–5σ ranges do not flow through this cell.
- **Classification: TRIVIAL-MICRO** (single-cell internal-consistency fix; the row's stated `≤0.1σ` contradicts the paper's own 0.36-f_NL / ~0.4σ text two lines below). Not a blocker; optional fold-in.

**P2: 1 VERIFIED-OPEN (TRIVIAL-MICRO, non-load-bearing). 0 blockers.**

---

### P3 — Multi-survey anomaly catalog (v3.1.112)
EXT20: Grok REJECT, Gemini MAJOR-REV, OpenAI MAJOR-REV. **All R40 DUPLICATEs.**

| EXT20 finding | Vendor | R40 cross-ref | Verdict |
|---|---|---|---|
| Planck top-200 includes 152/200 training patches | OpenAI/Grok | R40 E6 STALE (§III F over-representation check + p≈4e-4 diagnostic + tier labeled) | DUPLICATE → STALE |
| eROSITA/Gaia reproducibility "essential failures" | Gemini/OpenAI | R40 E2/E4 STALE-disclosure (membership-only; script not recovered, disclosed L1153) | DUPLICATE → STALE/OUT-OF-SCOPE |
| ~15-17% scaler instability claim too strong | Gemini | R40 within disclosed caveats; retrain = post-arXiv | DUPLICATE → OPINION/OUT-OF-SCOPE |
| Zenodo DOI placeholder | OpenAI-E3 | R40 OUT-OF-SCOPE | DUPLICATE → SUBMISSION-DAY |
| 30pp too long for null catalog | Grok | R40 OPINION | DUPLICATE → OPINION |
| NANOGrav chain path | — | **R40 closed in v112 (verified on-disk L1334)** | RESOLVED |
| Perplexity | — | FAILED | N-A |

**P3: 0 VERIFIED-OPEN. 0 blockers.**

---

### P4 — Survey-scale galaxy chirality (v1.0.188, FROZEN)
EXT20: Grok REJECT, Gemini MAJOR-REV (date/versioning), OpenAI MAJOR-REV. **All R40 DUPLICATEs.**

| EXT20 finding | Vendor | R40 cross-ref | Verdict |
|---|---|---|---|
| Future-date "June 13 2026" + HF tag v2026.04 + DOI not minted (P4-E1) | Gemini/Grok/OpenAI | R40 data-availability cluster OUT-OF-SCOPE (mints at submission) | DUPLICATE → SUBMISSION-DAY |
| σ-juxtaposition (+0.41σ vs z=0.70; +3.64σ vs +7.93σ) | Grok/OpenAI | R40 STALE (qualifiers already in abstract L348 + captions) | DUPLICATE → STALE |
| pLEE≤10⁻⁴ vs "<1σ" look-elsewhere inconsistency | OpenAI | R40 E1 STALE/MISLABELED (principled MC vs heuristic Bonferroni, reconciled) | DUPLICATE → STALE |
| N=949,584 abstract rounding | Gemini-MINOR | rounding-style nit | OPINION |
| 23pp too long, internal language | Grok | R40 OPINION | DUPLICATE → OPINION |
| Perplexity | — | FAILED | N-A |

**P4: 0 VERIFIED-OPEN. 0 blockers.** (Future-date + DOI = standing SUBMISSION-DAY stamp step.)

---

### P5 — DESI spiral-chirality environment (v0.1.81)
EXT20: Grok REJECT, Gemini MAJOR-REV, OpenAI MAJOR-REV. **One referee-flagged χ² rounding (new specific) + R40 DUPLICATEs.**

| EXT20 finding | Vendor | R40 cross-ref | Verdict |
|---|---|---|---|
| **χ²=4932 vs recompute 4933 (rounding), flagged "l.3551"** | referee/OpenAI-adjacent | NOT explicit in R40 | **VERIFIED-OPEN → TRIVIAL-MICRO** (see below) |
| Paper IV (P4) "in preparation" — not self-contained | OpenAI/Gemini/Grok | R40 E2-paperIV VERIFIED-OPEN (program-level; resolves when P4 posts to arXiv) | DUPLICATE → SUBMISSION-DAY (P4→P5 arXiv-linkage) |
| χ[h⁻¹Mpc] h-conversion "alternative convention confusing" | OpenAI | R40 E1-h FALSIFIED (auditor inverted identity; paper correct L829-842) | DUPLICATE → FALSIFIED |
| Tidal-tensor sign / title-footnote convention | Gemini | R40 E2-sign MISLABELED (Gemini's own derivation: "appears correct") | DUPLICATE → MISLABELED |
| 32pp too long for a null; restructure DESIVAST-first | OpenAI/Gemini/Grok | R40 M-length OPINION | DUPLICATE → OPINION |
| Future-date "June 13 2026" | Gemini/Grok | R40 N1-date STALE (past date; restamp refreshes) | DUPLICATE → STALE/SUBMISSION-DAY |
| V-Web/T-Web residual labels | — | **R40 closed in v81 (verified on-disk L810/L2900)** | RESOLVED |
| Perplexity | — | FAILED | N-A |

**P5 χ² verification (recomputed from committed table cells):**
- `p5_desi_chirality.tex:3551` (+ L592, L1615, L3510 + table) all print `$\chi^2 = 4932$`.
- Recompute from the exact integer cells of `tab:contingency_classProgram` (Filament 394181/13759, Cluster 392342/4234, Wall 6413/252, Void 420/8; N=811,609):
  **χ² = 4932.51 → rounds to 4933.** Referee is correct; the paper truncates/floors to 4932.
- Cramér's V = √(χ²/N) = 0.0780 — **unaffected** (same to 3 dp either way). log₁₀p ≈ −1069 unaffected.
- **Classification: TRIVIAL-MICRO** — pure round-half-up vs floor at 4 prose sites + the table caption. Non-load-bearing (conclusion is "highly significant association," V=0.078 robust). Optional 1-token fix.

**P5: 1 VERIFIED-OPEN (TRIVIAL-MICRO, non-load-bearing) + 1 SUBMISSION-DAY (P4 arXiv link). 0 blockers.**

---

## Final verdict ladder

| Paper | Internal R40 | EXT20 vendor legs (Grok/Gemini/OpenAI) | EXT20 Opus referee | EXT20 audited disposition |
|---|---|---|---|---|
| P1A | ACCEPT (3 cosmetics closed v78) | REJECT / MAJOR / streamline → all DUPLICATE-STALE/OOS | Minor-accept-leaning | **ACCEPT — 0 open** |
| P1B | ACCEPT (0 closures) | REJECT / MAJOR / DOI → all DUPLICATE | ACCEPT | **ACCEPT — 0 open** |
| P2 | ACCEPT (0 closures) | REJECT / MAJOR / MAJOR → DUP + 1 NEW micro | Accept | **ACCEPT — 1 TRIVIAL-MICRO** |
| P3 | ACCEPT (path fix v112) | REJECT / MAJOR / MAJOR → all DUPLICATE | Accept | **ACCEPT — 0 open** |
| P4 | ACCEPT (frozen) | REJECT / MAJOR / MAJOR → all DUPLICATE-STALE/OOS | Accept | **ACCEPT — 0 open** |
| P5 | ACCEPT (label fix v81) | REJECT / MAJOR / MAJOR → DUP + 1 NEW micro | Accept | **ACCEPT — 1 TRIVIAL-MICRO + 1 SUBMISSION-DAY** |

**Grok REJECT across all 6 is the constant EXT20 noise floor** — each REJECT rests on a single mischaracterization already FALSIFIED/STALE in R40 (P1A barriers, P1B ECH-derivation, P2 recast-scope, P3/P4/P5 length+internal-language). No Grok REJECT survives grounding.

## Blocker check

**ZERO blockers survive across all 6 papers.** Every EXT20 ESSENTIAL/MAJOR finding resolves to DUPLICATE (already R40-adjudicated), STALE, MISLABELED, OPINION, or SUBMISSION-DAY (Zenodo DOI mint + date stamp + P4→P5 arXiv-ID linkage, all performed AT submission, downstream of arXiv freeze). Only 2 genuinely-new VERIFIED-OPEN items exist, both TRIVIAL-MICRO and non-load-bearing.

## TRIVIAL-MICRO fixes (optional fold-in)

1. **P2** — `research/focused_paper_source_integration/02_full_draft.tex:956`
   Table IV e-correction effect cell `$\lesssim 0.1\sigma$ effect` → `$\lesssim 0.4\sigma$ effect`
   (paper's own L987 gives κ_ε|Δε|≈0.36 → 0.36·0.84/0.7≈0.43σ; current cell contradicts its own text two lines below; non-load-bearing, σ_theory=1.0 prior dominates).

2. **P5** — `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` lines **592, 1615, 3510, 3551** (+ table caption line 3551 region)
   `\chi^2 = 4932` → `\chi^2 = 4933` (exact recompute from committed cells = 4932.51; round-half-up). Cramér's V=0.078 and log₁₀p≈−1069 unchanged. Apply at ALL sites for consistency — referee cited only l.3551 but 4 prose sites + table carry it.

Each is a one-token consistency edit; if folded in, restamp P2→v1.7.70 / P5→v0.1.82 and add an EXT20 `/reviews` timeline entry per standing site-sync directive.

## SUBMISSION-DAY items (not arXiv-blocking)
- All 6: mint Zenodo DOI + stamp actual submission date (P4 HF tag v2026.04 → frozen tag).
- P5↔P4: replace "Paper IV (in preparation)" with live arXiv ID once P4 posts.

---

## ARXIV-READY: YES
