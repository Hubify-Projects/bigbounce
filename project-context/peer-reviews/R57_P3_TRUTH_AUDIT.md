# R57 P3 — Truth Audit (hardened, de-biased re-review)

**Paper:** P3 — multi-survey anomaly engine (`pipelines/p3_anomaly_engine/paper3_draft.tex`)
**PDF:** `/tmp/R57_P3/paper3_draft.pdf` md5=044460cc pages=31
**Compile:** 4×pdflatex, 0 undefined refs, 0 overfull boxes (any size), stable 31 pp.
**Reviewers:** Grok-4.3, OpenAI gpt-5, Gemini-2.5-pro (3/4 OK; Perplexity quota-failed, non-blocking) + own Opus read.
**Date:** 2026-06-26

---

## SPECIAL TASK — R56 disclosure-footnote clip fix VERIFICATION

**R56 fix:** the Table I (`tab:survey_summary`) 6-note disclosure block was moved
OUT of the `table*` float into a body `flushleft`/`footnotesize` block (src
L731–750), because inside the float it overflowed 676pt and was silently clipped
off the page — suppressing the Gaia/eROSITA/LAMOST-FAIL/IsolationForest/Planck
honest-reporting caveats.

**VERDICT: VERIFIED — RENDERS IN FULL.** Rendered-PDF evidence (pdftotext per page
+ pdftoppm 110dpi pages 5–8):

| Footnote | Symbol | Rendered? | Evidence phrase (in PDF text) |
|---|---|---|---|
| IsolationForest XV-stability (eROSITA+Gaia) | §S | YES (p6–8) | "IsolationForest cross-validation"; "81.5%"; "41.0%"; "284 of 298"; "95.3%" |
| Gaia reliability warning | ⋆ | YES (p8) | "Reliability warning"; "training-sample-conditioned"; "treated as exploratory" |
| SDSS three-threshold disclosure | ♡ | YES (p7–8) | "three-threshold disclosure"; "19,253"; "S>5 ... 12" |
| Planck rate bookkeeping | ◇ | YES (p8) | "Planck rate bookkeeping"; "0.10%" |
| eROSITA membership-only | # | YES (p8) | "membership-only tier"; "non-reproducible ... 16 monotone rescalings" |
| LAMOST transparent FAIL | ♠ | YES (p8) | "transparent FAIL"; "5.8%"; "methodological lesson"; "consult DESI ... PASS continuum-dip 5σ at 64%" (footnote completes) |

Block flows naturally across pages 5→8 as body text and terminates cleanly. The
two phrases that returned [0] on first grep ("non-reproducible on any of 16
monotone", "treated as exploratory") were pdftotext line-wrap artifacts — confirmed
present via loosened match. **No clipping, no overfull, fix holds.** This fix is
load-bearing: it pre-empts several reviewer "undisclosed caveat" findings below.

---

## Findings adjudication

### FALSE POSITIVES (calibration filter — genuine FP, not severity-defaulted)

- **OpenAI P3-M4 (Cramér's V formula typeset wrong):** FALSIFIED. Source L979 reads
  `V = \sqrt{\chi^2/(N\cdot(k-1))} = \sqrt{376{,}713/(378{,}280\times24{,}048)} ≈ 0.0064`
  — sqrt correctly wraps the full fraction in both the formula and the
  substitution. OCR misread. Arithmetic verified: √(376713/9.097e9)=0.00644≈0.0064.
  Already fixed in R39conf (v3.1.106). Do not reopen.
- **Grok P3-E1 ("Dated: June 26 2026" template artifact):** FALSIFIED. Intentional
  revtex compile date, not a placeholder.
- **Gemini P3-N4 (abstract cross-ref §VIE "no such section"):** FALSIFIED.
  `\ref{sec:comparison}` resolves to §VI E = "Comparison with Prior Work" (L1157) —
  the correct target for the size benchmark. Section exists; ref correct.
- **Gemini P3-N5 (Table I footnote § cites §VID, wrong section):** FALSIFIED.
  `\ref{sec:pathc_caveats}` resolves to §VI D = "Path-C Rebuild Residual Caveats"
  (L1122); item (ii) holds the IF/XV-stability caveat. Ref correct.

### ALREADY-DISCLOSED (honest-reporting pre-empts the finding; not a defect)

These are real reviewer concerns that the paper's own (now-rendering) disclosures
already address — they convert to OPINION/editorial, not internal inconsistencies:

- **Grok P3-E4 / OpenAI M1 (failing surveys in "catalog-grade" tier):** Gaia/eROSITA
  carry per-object exploratory validity flags; LAMOST is a labeled FAIL. Disclosed
  in abstract (L582) + Table I footnotes ⋆/#/♠. Honest reporting.
- **OpenAI M5 / Gemini M2 (NEOWISE PASS = geometry-only):** Abstract L582 already
  says "NEOWISE mask-geometry 100% — a masking-geometry sanity check that passes by
  construction, not a detector-sensitivity test." Disclosed.
- **OpenAI M9 / Grok M3 (eROSITA 0.03% "rate"):** footnote # already states "should
  not be interpreted as an independent measurement of the X-ray anomaly frequency."
  Editorial ask (replace cell with "—") is style, not error.
- **Gemini P3-E4 (eROSITA 81.5% stability is on IF top-9303, not released top-298):**
  footnote § already states the 9,303 set is "distinct from the 298-source published
  catalog headline" and the 284/298=95.3% overlap is "a descriptive internal-
  consistency statistic ... not independent cross-method confirmation." Disclosed.
- **OpenAI E11 (37.3M "processed" counts Planck as 20k not native 200k):** footnote ◇
  discloses the 2×10⁵-patch native bank and the 0.10% re-basis. Basis choice
  disclosed; 180k/37.3M = 0.48%, immaterial to the "largest" claim.
- **Grok E2 / OpenAI M6 ("largest ... of which we are aware"):** hedged + anchored to
  the Liang2023 benchmark in-text (§VI E). PRD-style editorial ask for a comparison
  table; not an unbacked-number defect.
- **OpenAI E10 (LAMOST 113,342 vs 108,963 post-dedup):** abstract "~113,000"
  approximate; footnote ♠ gives both exact figures. Rounding, disclosed.

### GENUINE — but NOT a verified DO-NOW closure

- **OpenAI M9-pass2 (§IV.B "the anomaly **rate** shows no correlation with Galactic
  latitude (Spearman r=0.0005, p=0.92)"):** the word "rate" is imprecise — a Spearman
  correlation against latitude is a per-object/per-pixel score quantity, not a
  counts-per-area rate. Genuine MINOR wording-precision concern (internal-terminology).
  HOWEVER the underlying number is NOT in any committed artifact
  (`r24conf_pod_session_batch.json` contains only score-reproduction Spearman values),
  so I cannot verify whether the correct word is "score" or "per-pixel count" without
  fabricating. Per the no-fabricate gate, **left OPEN** (MINOR), not closed. Result is
  a null either way → non-material to any positive claim.

---

## R54/R55/R56 prior-fix integrity (verified intact, not reopened)

- **R56 (footnote clip):** VERIFIED rendering — see Special Task above.
- **R54 (Table IX unbacked-number fabrication):** intact. Table IX Savage-Dickey
  chain is internally self-consistent: B_MB/free=3.23, B_SMBHB/free=4.52×10⁻⁴,
  B_MB/SMBHB=3.23/4.52e-4=7146≈7.14×10³, log₁₀=3.85 ✓; γ=3.0 at +1.13σ ✓; γ=4.33
  at +4.61σ ✓. No unbacked numbers reappeared.
- **R39conf Cramér's V sqrt fix:** intact (see FP above).

## Table number spot-check (vs committed artifacts) — all backed

| Number | Source | Committed artifact | Match |
|---|---|---|---|
| 378,280 unique / 269,317 catalog-grade | Table I, abstract | `r24conf_pod_session_batch.json` | ✓ |
| 2,468 science-class / 190,015 clusters | §III.A, Table II | `ext3_b2_targettype_recount.json` | ✓ |
| 77,905 @ S≥0.1060 / 19,253 @ 0.2051 | footnote ♡ | `pathc_sdss_native_rescore_summary.json` | ✓ |
| 298 headline / 930,203 cat / 0.259 knee | footnote #/§ | `r24conf_erosita_axis_sweep.json`, `ext3_fm1_erosita_scaler_refit.json` | ✓ |
| 113,342 / 11,334,161 pool / 2,054 @S>5 / 5.8% | footnote ♠ | `pathc_lamost_native_rescore_summary.json` | ✓ |

No fabricated/unbacked numbers found (R54-class clean).

---

## Closures this round

**NONE.** No NEW verified DO-NOW finding. The single genuine novel item (latitude
"rate" wording) is unverifiable from committed artifacts and is left OPEN per the
no-fabricate gate. All other reviewer items are vendor false-positives or already
disclosed by the paper's (now-rendering) honest-reporting footnotes.

## Convergence statement

P3 R57 CONVERGES. The R56 disclosure-footnote fix is VERIFIED rendering in the
compiled PDF (all 6 caveats visible, no clipping, 0 overfull, 0 undef, 31 pp).
Three independent native-PDF reviewers (Grok REJECT, OpenAI MAJOR-REV, Gemini
MAJOR-REV) surfaced ZERO new verified defects: their headline items are either
false positives (Cramér OCR misread, two correct cross-refs read as wrong, the
intentional compile date) or concerns the paper already discloses honestly — which
is precisely what the R56 fix restored to the page. Table spot-checks (5 tables)
all trace to committed artifacts; R54/R55/R56 fixes intact. One open MINOR
(latitude "rate" vs "score" wording) remains, non-material (null result) and
deferred pending the source computation rather than a fabricated fix. No
severity-defaulting applied; no false-positive closed; no verdict skipped.
