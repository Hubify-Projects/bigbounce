# P3 INT (Claude Code full-source leg) — v3.1.137 — ROUND 2026-07-05

**Reviewer:** Claude Code INT leg (Houston subscription; NOT Anthropic API), full repo + source + data as ground truth.
**Paper:** `pipelines/p3_anomaly_engine/paper3_draft.tex` (v3.1.137, `\date{July 5, 2026}`, tex:56).
**Method:** Verified every numerical claim in the new detection-significance demonstration against a fresh re-run of the committed script from repo root, against the committed JSON, and against direct parquet inspection. Cross-checked standing claims (268,519 process-volume, eROSITA/LAMOST reproducibility, §V framing).

## VERDICT: **ACCEPT** (with 2 MINOR polish items)

**Central claim — the multi-survey anomaly catalog — is SUPPORTED.** The validated 268,519-object headline is machine-reproducible end-to-end from committed per-survey lists (274,353→268,519, verified below), the process-volume vs like-for-like (2,468) distinction is stated up front and repeated, and every tier's failure mode / reproducibility gap is disclosed with a named artifact.

---

## Verification of the NEW detection-significance result (§sec:sdss, tex:1094–1099)

Re-ran `scripts/sdss_qso_hiz_enrichment.py` from repo root — output is **byte-for-byte identical** to committed `outputs/sdss_qso_hiz_enrichment.json`. Every number in the paragraph traces to the parquet:

| Paper claim (tex:1098) | Script/JSON | Parquet re-check | Match |
|---|---|---|---|
| 77,905 native anomalies | 77,905 | parquet rows = 77,905 | ✔ |
| 76.3% QSO / 19.2% GALAXY / 4.5% STAR | 0.7633 / 0.1921 / 0.0446 | class_fractions | ✔ |
| 59,462 QSOs | 59,462 | df[class==QSO] | ✔ |
| median z = 2.31 | 2.3073 | ✔ | ✔ |
| 67.3% at z>2; 1,150 at z>4; 198 at z>6 | 40,020(=67.3%) / 1,150 / 198 | ✔ | ✔ |
| median score 0.197 vs 0.142 | 0.19653 / 0.14152 | ✔ | ✔ |
| Mann–Whitney p = 1.0×10⁻¹⁰³ | 1.05e-103 | ✔ | ✔ |
| Spearman ρ = +0.036, p = 9.6×10⁻¹⁹, N=59,462 | +0.03624 / 9.59e-19 | ✔ | ✔ |

- Parquet min anomaly_score = **0.10604** = the S≥0.1060 continuity-slice threshold quoted in Table footnote �heartsuit and §sec:sdss; score max 13.77, consistent with "compresses same objects to S<14" (tex:1077). This is the **native re-score slice**, not the cross-transfer set — so the 76.3/19.2/4.5 class split IS correctly computed on the native tier (distinct from the emission-line taxonomy of Table tab:sdss_classes, which the caption tex:1118 correctly flags is computed on the cross-transfer set — no conflation).

**Honest framing is intact:**
- Small Spearman effect size is stated explicitly as an "honest limitation" — "the effect size is *small* (ρ=+0.036)… the score–z correlation is not itself a strong monotone relation" (tex:1098). Not overclaimed.
- DESI score-vs-z test explicitly deferred as pod/HuggingFace-bound (`desi_zall.parquet`, ~28.4M rows, not in repo) — tex:1098. Honest.
- The 2.15× external enrichment factor **is present in the JSON but deliberately OMITTED from the paper**, with the script's own note stating the factor is "prior-dependent" and only the internal control is "decisive." Correct conservative choice — the paper leans only on the fully self-contained internal control. **No overclaim.**

The new result is **correctly and honestly implemented.** The logical claim — "redshift-blind sky/fiber/calibration artifacts cannot produce a score that rises with QSO redshift, so the detector preferentially ranks genuinely rare high-z quasars" — is sound and directly rebuts the recurring RS24 "artifacts-not-astrophysical" major.

## Verification of standing claims

1. **268,519 process-volume headline** — re-read `reproduce_headline_dedup.json`: `total_validated_survey_level_detections=274,353`, `VALIDATED_HEADLINE_unique=268,519`, `pointsource=268,319`. Matches abstract (tex:49, 838) and §pathc (tex:949, 1267) exactly. The process-volume caveat ("candidates that survive per-survey gates… NOT a count of confirmed detections") leads the headline paragraph (tex:838) and repeats in the abstract — the standing Directive-A/EXT concern is fully addressed. ✔
2. **eROSITA reproducibility disclosure** (tex:1147, 1150) — the "membership-is-canonical" framing is honest: production 0.259 score axis irreproducible across 16 monotone rescalings + 3 IF retrains (non-monotone raw, ρ=−0.10), but the n=298 membership = committed raw top-298 (S_raw≥3.4119) is a scale-invariant reproducible recipe. Downstream consequence (no reproducible score axis) is explicitly stated. Excellent disclosure, no gap. ✔
3. **LAMOST** (tex:1011, 951) — transparent FAIL: 98% blue-excess training-bias artifact, 5.8% injection-recovery FAIL, contributes ZERO to the 268,519 headline (enters only the 377,780 inclusive total). Repeatedly flagged against misreading. ✔
4. **Gaia** (tex:1172, 1452) — synthetic-placeholder tier fully *excised* (source_id = ⌊5e18+i⌋ fingerprint), zero contribution to any count. Honest and self-caught. ✔
5. **§V cosmological framing** — presented as a methodological demonstration, not a bounce detection claim (consistent with repo research stance). ✔

## Issues

**[MINOR-1]** §sec:sdss (tex:1098) reports "67.3% at z>2" for the QSO population. 40,020/59,462 = 67.30% ✔ — correct, but the abstract-level reader could misread it as 67.3% of the *whole* 77,905 catalog. Consider "67.3% of the anomaly-selected QSOs at z>2" for zero ambiguity. Cosmetic only; the local sentence already scopes it to "the 59,462 anomaly-selected QSOs."

**[MINOR-2]** The committed enrichment JSON carries the 2.15× external factor and binomial p=8.3e-119. Since the paper deliberately (and correctly) omits the external-baseline block, consider a one-line comment in the paper or the script header noting the external block is *intentionally not cited in-text* — so a future editor doesn't "helpfully" promote the prior-dependent 2.15× into the manuscript and reintroduce an overclaim. Provenance hygiene, not a paper defect.

## No REAL problems found that EXT would miss
- No code-vs-paper number mismatch (re-run == committed JSON == parquet, exact).
- No overclaim beyond committed data (2.15× correctly suppressed; DESI test honestly deferred; small ρ stated).
- No undisclosed reproducibility gap (eROSITA axis / Gaia synthetic / LAMOST fail / SDSS three-threshold denominator all disclosed with named artifacts).

**Recommendation:** ACCEPT. The new detection-significance demonstration is a genuine, honestly-scoped, fully-reproducible strengthening of the central catalog claim.
