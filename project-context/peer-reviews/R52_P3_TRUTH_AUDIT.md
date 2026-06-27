# R52 P3 — Truth Audit (Opus judgment leg)

**Paper:** P3 v3.1.112 → HEAD v3.1.113 — "Spectrally Unusual Sources at Scale:
A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies…" (Golden)
**Canonical source:** `pipelines/p3_anomaly_engine/paper3_draft.tex` (209 KB; the
`arxiv/paper3_anomaly_catalog.tex` is a 1.9 KB *superseded stub* — do not edit).
**PDF audited by reviewers:** `site/public/papers/paper3_anomaly_catalog_v3.1.112.pdf`
md5=62d7b294, 30 pp.
**Reviewers read:** Claude/Opus (MINOR, 1 MAJOR), Grok_brutal (MAJOR),
Gemini_cosmology (ACCEPT-w-minor), OpenAI_methodology (MAJOR — *note: task brief
mislabeled this as "accept"; it is in fact 7 ESSENTIAL + 11 MAJOR + minors*),
Perplexity (CALL FAILED — 401 quota; no findings).

---

## NET VERDICT: **MINOR REVISIONS** — no BLOCKER, no genuine MAJOR.

Calibration applied: June-2026 arXiv valid; catalog-class paper, size is **not**
a defect; deliberate scoping labels / transparency notes not penalized; PDF
text-extraction (OCR) artifacts ignored. The two MAJOR-REVISIONS verdicts (Grok,
OpenAI) are inflated by (a) a PDF-OCR artifact, (b) findings the paper **already
explicitly addresses**, and (c) referee-*enhancement* requests — not false
claims. The catalog makes no over-claim that the committed artifacts contradict;
every headline number is internally consistent and the weak tiers are
candidate/exploratory-framed with per-survey validity flags.

### VERIFIED counts by tier
- **BLOCKER: 0**
- **MAJOR (genuine, science-affecting): 0**
- **MINOR (VERIFIED, actionable DO-NOW): ~13** (all prose/arithmetic; 1 optional GPU run)
- **STALE / FALSIFIED: 5**
- **OPINION / OUT-OF-SCOPE: 3**

---

## Deduped findings + verdicts

| # | Finding (merged) | Raisers | Verdict | Evidence | Tier / disposition |
|---|---|---|---|---|---|
| A | **DESI injection-recovery never run for the anchor survey (~52%)** | Claude M1; OpenAI E6(part) | **VERIFIED gap — already explicitly caveated** | Abstract L567 + §VID(ii) L1119 both state verbatim "DESI injection-recovery was not executed; its catalog robustness rests on the two Jaccard metrics" (J̄_CV=0.862 PASS, OOD J̄=0.732 PASS). No false claim. | MINOR. Min-fix present. Strengthen = run it (DO-NOW, reproducible; see §DESI adjudication). Non-blocking. |
| B | **"catalog-grade" 269,317 tier includes injection-FAIL tiers** (eROSITA, Gaia) + geometry-only NEOWISE | OpenAI E1/E2/E6 | **PARTIALLY-VERIFIED (clarity)**; NEOWISE-decomp part FALSIFIED | L724: catalog-grade tier = DESI+SDSS+**eROSITA**+Planck+**Gaia**+NEOWISE (6-way dedup). eROSITA (1.2%) & Gaia (5.2%) fail the 5σ gate (L567). NEOWISE geometry-QA distinction *is* stated repeatedly (L567/716/887/1119) → that sub-claim FALSIFIED. | MINOR-clarity. DO-NOW: one clause in abstract + Table I caption that the 6-way "catalog-grade" number folds in two per-object injection-FAIL components flagged exploratory at object level. |
| C | **DESI GALAXY Wilson 95% CI ±0.02% is wrong** | OpenAI E3 | **VERIFIED (arithmetic)** | L797: "GALAXY 0.75% ± 0.02% on ~4.9×10⁶". Correct half-width 1.96·√(0.0075·0.9925/4.9e6)=7.6×10⁻⁵ ≈ **±0.008%** (overstated ~2.6×). QSO ±0.003% is correct. Scientifically immaterial (20× ratio robust) but a real stated error. | MINOR-arithmetic. DO-NOW token edit: ±0.02% → ±0.008%. |
| D | **Cramér's V display omits the √** | OpenAI E4 | **STALE / FALSIFIED** | L950 already shows `V = √(χ²/(N(k−1))) = √(376,713/(378,280×24,047)) ≈ 0.0064` — √ correctly applied. Changelog L84: fixed in R39conf. OpenAI read OCR-broken √ glyph. | No action. |
| E | **"largest-scale" superlative unsupported** | Grok E1; OpenAI E7 | **PARTIALLY-VERIFIED → mostly OPINION** | Already hedged "of which we are aware", anchored to Liang2023, with §comparison (L1128) and 141×/100×/73× quantified. | MINOR/opinion. Optional DO-NOW: tighten to "largest by total sources processed in a single framework"; comparison table = enhancement, not required. |
| F | **378,280 dedup + "≲10 random coincidences" / "~2.3–2.75" not reproducible from text** | Grok E3; OpenAI M4/M9 | **PARTIALLY-VERIFIED (presentation)** | Headline IS reproducible (Claude re-derived 388,493−10,213=378,280; 6-/7-way dedup artifact `r24conf_pod_session_batch.json`). The *random-coincidence* scalars are asserted without a shown calc. | MINOR. DO-NOW: add a back-of-envelope footnote (areal densities × overlap area × πr²); optional dedup pseudocode. |
| G | **f_NL numbers juxtaposed without "not comparable" qualifier** (8.98 de-biased vs 6.1% fixed-α; 8.98 vs 16.85 norm) | Grok E2; OpenAI M10/n9; Claude m5 | **PARTIALLY-VERIFIED → largely already-addressed** | L1037 explicitly: 16.85 is "on a different internal normalization and is not comparable… only relative quantities transfer"; envelope labeled "translated band, not a 68% probabilistic interval". Abstract quotes only the empirical leg. Residual: one cross-ref where 9.4% and the Appendix-C 6.1%/16.85 reappear. | MINOR-clarity. DO-NOW cheap. |
| H | **Fisher coefficient c=0.0747 (5-α refit) undocumented** | OpenAI M1 | **VERIFIED (presentation)** | L1117/L1037 state "c=0.0747 (verified positive via 5-α refit)" but tabulate no (α,σ) points and cite no artifact. Artifact exists: `fisher_full/fisher_result.json`. Drives σ(f_NL)=8.14 headline → must be auditable. | MINOR→MAJOR-presentation. DO-NOW: list the 5 (α, σ) pairs + `\artifact{…fisher_result.json}` in caveat (i). |
| I | **S thresholds incommensurable across surveys — add explicit note** | Grok M2 | **PARTIALLY-VERIFIED → mostly addressed** | Eq 2 is survey-specific by construction; Table I caption L689 already explains the two threshold families + per-survey cuts at length. | MINOR. DO-NOW: one global "S thresholds are survey-specific and not directly comparable" one-liner. |
| J | **Fisher uses fixed α=0.15; measured-bias sensitivity never propagated** | Grok M3 | **FALSIFIED / already-done** | The *primary* forecast already uses the **measured** α with full ±0.65 propagation into the envelope [3.92, 8.98] (L1037); fixed-α=0.15 is explicitly demoted to "retained for reference… empirical α supersedes it". The exact ask is the headline. | No action. |
| K | **Pre-retrain LAMOST tier released to science without stability test** | Grok M1 | **FALSIFIED** | Pre-retrain LAMOST is the *training-bias artifact* (the paper's central lesson), **excluded** from the 269,117 catalog-grade subset (L565), retained only as methodological lesson (L724/L1082). No science result rests on it. | No action. |
| L | **RA-only cross-match null is not geometry-preserving** | OpenAI M3 | **VERIFIED (method, minor)** | Paper already labels it "a heuristic control" and cautions, but still compares observed 4 vs 2.75 in main text. | MINOR. DO-NOW: relegate the numeric comparison to a methods note, or add a geometry-preserving (random-rotation) null. |
| M | **NEOWISE polar-cap 2.6× excess lacks z/p significance** | OpenAI M5 | **VERIFIED (minor)** | L887 gives ratio only. n=436, p0=0.0152, k=17 → z≈4.0 (p≈6×10⁻⁵), trivially computable. | MINOR. DO-NOW: add z/p. |
| N | **DESI B-dominant "calibration-suspect" asserted w/o diagnostic** | OpenAI M6 | **VERIFIED (minor) — already hedged** | L1091 limitation (3) already flags "calibration-suspect; confirmation via photometric color selection is needed". | MINOR. DO-NOW: rephrase as explicit hypothesis (minimal) or add a color sanity check. |
| O | **Planck 48/200 binomial p ignores patch correlation** | OpenAI M11 | **VERIFIED (minor)** | Paper notes "may be mildly correlated" but still quotes p≈4×10⁻⁴. | MINOR. DO-NOW: effective-N (spatial-jackknife) correction, or drop the p-value and keep the qualitative statement. |
| P | **Reduce to ≤25 pp; move cosmology/MCMC to SI** | OpenAI M7 | **OUT-OF-SCOPE / OPINION** | Catalog-class paper; calibration directive: size is not a defect. f_NL + NANOGrav legs are core to the bounce program (the paper's raison d'être). | No action. |
| Q | **Surface eROSITA/Gaia reproducibility caveats in Conclusions; fix Table I footnote ‖/§** | Gemini m1/m2; Claude m4 | **VERIFIED (presentation)** | eROSITA score axis irreproducible (membership-only) and Gaia preprocessing lineage-inferred (L625) — flagged in body but not in the self-contained Conclusions; Table I footnote ‖ has no text and § reads garbled (likely typeset/OCR). | MINOR. DO-NOW: add one Conclusions clause; verify/repair Table I footnotes. |
| R | **Date "June 18/19, 2026" is a placeholder** | Grok N1 | **OPINION / expected** | `\date{June 19, 2026}` (HEAD v3.1.113, L56); reviewers saw v3.1.112=June 18. Pre-submission working date is intentional. | Replace with arXiv date at submission. No action now. |
| S | Misc minors: novelty single-stratum (Claude m1 — already caveated L1091(6)); NEOWISE-top saturation foregrounding (Claude m2); Planck "standard practice" wording (Gemini m3/OpenAI n11); figure font legibility (Grok N2/OpenAI n6 — D-round); "score-knee" definition (OpenAI n2); Fig 3 second threshold line (OpenAI E9) | various | **MOSTLY-VERIFIED (cosmetic/clarity)** | Honest framing already present for most; font/figure items belong to the D-round. | Optional MINOR / D-round. |

---

## Truth-audit of the Grok MAJOR (each reason individually)

Grok's overall **MAJOR REVISIONS does not hold.** Reason-by-reason:

- **E1 (largest-scale superlative):** already hedged + anchored + §comparison →
  MINOR/opinion (finding E). Not major.
- **E2 (f_NL numbers not comparable):** non-comparability **explicitly stated**
  at the load-bearing site L1037; abstract doesn't juxtapose them → minor
  clarity (finding G). Not major.
- **E3 (378,280 not reproducible from text):** headline **is** reproducible
  (Claude re-derived); only the random-coincidence scalars need a shown calc →
  MINOR presentation (finding F). Not major.
- **M1 (pre-retrain LAMOST released):** **FALSIFIED** — pre-retrain LAMOST is the
  bias artifact, excluded from catalog-grade, retained only as the lesson
  (finding K).
- **M2 (S incommensurable):** Eq 2 survey-specific by construction + Table I
  caption already explains families → mostly addressed, one-liner add (finding I).
- **M3 (fixed-α, no sensitivity):** **FALSIFIED** — measured α with ±0.65
  propagation IS the primary forecast (finding J).
- **N1 (date), N2 (fonts):** placeholder / D-round.

**Net Grok: downgrade MAJOR → MINOR.** Zero genuine major; two of three "MAJORs"
are FALSIFIED against committed text.

---

## Adjudication — the Claude-leg MAJOR (DESI injection-recovery, ~52% anchor)

**Verdict: VERIFIED gap, but the explicit completeness caveat already exists in
the paper → correctly MINOR, not a blocker.**

- The gap supports **no false claim**: DESI is candidate-framed and carries **two
  genuine stability gates** (5-fold CV Jaccard 0.862 ≥0.70 PASS; production-vs-
  control OOD Jaccard 0.732 ≥0.50 PASS, ceiling 0.874) — and is the *only* survey
  with an independent OOD-holdout (103k unseen SPARCL spectra, L643). Limitation
  (2) (L1091) and §VID(ii) (L1119) already state catalog completeness for the
  DESI sensitivity axis is unquantified.
- Claude's own *alternative* fix ("state explicitly why DESI sensitivity is left
  unquantified") is **already satisfied** verbatim in the abstract (L567) and
  §VID(ii) (L1119).

**Is it DO-NOW or TRULY-BLOCKED?** → **DO-NOW (reproducible), but optional /
non-blocking.** The injection harness is committed
(`injection_recovery_continuum.py`, `injection_recovery_spectra.py`,
`make_injection_recovery_figure.py`, `pathc_injection_recovery/*.json` for the six
sibling tiers), and the DESI 5-fold CV retrain machinery already retrains fresh
BigAEs on the 47k pool — so a DESI continuum-dip + emission-line injection-recovery
run on the native checkpoint, reported on the Fig. 10 axis, is reproducible from
committed code (a GPU job, not blocked by missing data/hardware). It is **not**
arXiv-blocking because the minimum-acceptable closure (explicit caveat + two
Jaccard gates + unique OOD holdout) is already in place.

**Recommended closure:** run the DESI injection-recovery (DO-NOW, GPU worker) and
add the curve to Fig. 10 + a row to the gate tally; **if not run this cycle**, the
existing explicit caveat stands as the accepted closure — no text is false.

---

## CLOSURE PLAN (each VERIFIED finding → exact edit + tier)

All DO-NOW unless marked. None blocks arXiv. Hand to a Sonnet worker for the prose
items; the one GPU item to a worker+GPU.

1. **(C) GALAXY CI — MINOR/arithmetic — DO-NOW.** §IIIA L797: `0.75\% \pm 0.02\%`
   → `0.75\% \pm 0.008\%` (recompute & state Wilson; QSO ±0.003% unchanged).
2. **(B) catalog-grade label — MINOR/clarity — DO-NOW.** Abstract (L565) + Table I
   caption (L689): add a clause — "the 6-way 'catalog-grade' tier (269,317)
   incorporates the eROSITA (membership-only) and Gaia tiers, which fail the 5σ
   injection-recovery gate and carry per-object *exploratory* validity flags;
   NEOWISE's gate is geometry-QA, not detector-sensitivity." (Do not change the
   number; clarify the label.)
3. **(H) c=0.0747 — MINOR→MAJOR-presentation — DO-NOW.** §pathc_caveats (i) L1117:
   tabulate the five (α, σ(f_NL)) refit points + add
   `\artifact{pipelines/p3_anomaly_engine/fisher_full/fisher_result.json}` (verify
   the JSON holds the 5 points; if absent, emit them from the refit script).
4. **(F) random-coincidence derivation — MINOR — DO-NOW.** §IVA: add a footnote
   computing "≲10" and the "~2.3 / ~2.75" expectations from per-survey areal
   densities × common-footprint overlap area × π(5″)²; or relegate to a methods
   note without the numeric.
5. **(M) NEOWISE polar-cap z/p — MINOR — DO-NOW.** §IIIH L887: append
   "binomial z≈4.0, p≈6×10⁻⁵ (n=436, p₀=0.0152, k=17)".
6. **(Q) Conclusions caveats + Table I footnotes — MINOR — DO-NOW.** §VII: add one
   sentence that Gaia (lineage-inferred preprocessing) and eROSITA
   (membership-only, irreproducible score axis) are exploratory/membership-only.
   Table I: supply the missing ‖ footnote text and de-garble the § footnote.
7. **(G) f_NL cross-ref — MINOR/clarity — DO-NOW.** §V / Appendix C: one line where
   9.4% (empirical) and 6.1%/16.85 (fixed-α / shot-noise norm) co-occur —
   "(different normalization/forecast; not directly comparable; see §VB)".
8. **(I) S-threshold note — MINOR — DO-NOW.** Add once near first multi-survey S
   comparison: "S thresholds are survey-specific (Eq. 2 normalization) and not
   directly comparable across surveys."
9. **(L) RA-only null — MINOR/method — DO-NOW.** §IVC: relegate the 4-vs-2.75
   numeric to a methods note, or add a random-rotation footprint-preserving null.
10. **(O) Planck patch correlation — MINOR — DO-NOW.** §IIIF: add an effective-N
    (spatial-jackknife) corrected significance, or drop the binomial p and keep
    the qualitative over-representation statement.
11. **(N) B-dominant — MINOR — DO-NOW.** §IIIA: rephrase "calibration-suspect" as
    an explicit hypothesis needing color follow-up (or add a quick color check).
12. **(E) superlative — MINOR/opinion — DO-NOW (optional).** Abstract/Conclusions:
    "largest by total sources processed in a single framework" in place of the
    bare absolute.
13. **(A) DESI injection-recovery — MINOR — DO-NOW (GPU, optional/non-blocking).**
    Run continuum-dip + emission-line injection-recovery on the DESI native
    checkpoint via the committed harness; add the curve to Fig. 10 + a tally row.
    *If not run this cycle, the existing explicit caveat is the accepted closure.*

**No action (FALSIFIED/STALE/OPINION):** D (Cramér's V — already correct),
J (measured-α already propagated), K (LAMOST already excluded), NEOWISE-PASS
conflation (already decomposed), P (page-reduction — out of scope), R (date —
pre-submission placeholder).

**Same-commit hygiene:** per the standing review-round site-sync directive, add an
R52 entry to `site/src/data/reviewTimeline.ts` and update
`project-context/SSOT/paper-3/status.md` in the closure bundle.

---

*Audited by the Opus truth-audit leg, internal round R52, 2026-06-26. Verdict-first
anti-fabrication gate: no ACCEPT faked; no finding closed without cited evidence;
no false positive "fixed". Net: MINOR REVISIONS, 0 blocker, 0 genuine major.*
