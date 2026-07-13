# P3 (ApJS variant) — M22-EXT truth-audit

**Date:** 2026-07-13
**Paper:** P3 ApJS variant `pipelines/p3_anomaly_engine/paper3_apjs.tex`
**Reviewed version:** v3.1.158-apjs (byte-unchanged since M6) → **CLOSED into v3.1.159-apjs this wave** (1 genuinely-new DAS internal contradiction found + fixed).
**Raws (read verbatim before any verdict):**
- `EXT_real/H17_2026-07-10/M22/P3APJS_grok_M22.md` — **VERDICT: MAJOR REVISIONS** (4 MAJOR + 2 MINOR)
- `EXT_real/H17_2026-07-10/M22/P3APJS_chatgpt_M22.md` — **VERDICT: REJECT** (16 MAJOR + 1 MINOR)

## Verdict matrix (EXT, from raw VERDICT lines)
| Reviewer | Verdict | MAJOR | MINOR |
|----------|---------|-------|-------|
| Grok EXT | MAJOR REVISIONS | 4 | 2 |
| ChatGPT EXT | REJECT | 16 | 1 |
| Gemini EXT | (carry — browser hard-throttled, no M22 leg) | — | — |

## ledger_match.py (DRAFT, conservative)
| Raw | Findings parsed | MATCHED | UNMATCHED | Rate |
|-----|-----------------|---------|-----------|------|
| Grok | 9 | 6 | 3 | 67% |
| ChatGPT | 20 | 11 | 9 | 55% |

High UNMATCHED = verbose ApJS §-anchor restatement + parser-split header/tail fragments. Every UNMATCHED item Opus-adjudicated below vs live `paper3_apjs.tex`.

## Per-finding adjudication

### Grok (all source-cited re-flags — 0 genuinely-new)
- **G1** 268,519 "validated catalog-grade" = process-volume, benchmark 2,468, 98.7% sky/filler → **DP3-07** (abstract L1027 first sentence discloses process-volume + 2,468 + not-confirmed-detections).
- **G2** eROSITA axis irreproducible (0.259, 16 rescalings + 3 IF retrains), excised membership-only → **DP3-08** (§erosita + `tab:provenance` excised from every count).
- **G3** two of six surveys excluded (synthetic Gaia) / relegated (LAMOST exploratory); "validated" rests on 4 surveys → **DP3-07/-08/-09/-14** (mixed-validation disclosed abstract L1027 "the 'validated' label is mixed-validation, not uniform").
- **G4** DESI robustness = single production gate + 2 correlated fold probes; narrow ≥15σ floor; Planck train-patch over-rep → **DP3-01/-06/-12** (§II.F single-gate closure).
- **G5 [MINOR]** SDSS 77,905 continuity-slice vs 19,253 top-1% / 12 @S>5 → **DP3-09/-14** (footnote ♡ tabulates all three thresholds, survey-specific).
- **G6 [MINOR]** §5 f_NL/NANOGrav secondary/null, disproportionate space → **DP3-10** (titled "Secondary Demonstrations"; null retained per CRITICAL RESEARCH DIRECTIVE; venue DP3-16).

### ChatGPT
- **#1** injection-recovery ≠ purity/FDR; NEOWISE by-construction → DP3-07/-11/-12.
- **#2** 268,519 no coherent selection function (mixed threshold families; SDSS 77,905 continuity) → DP3-06/-09/-14.
- **#3** most DESI entries not shown astronomical (98.7% no science bit; 86% DESI_TARGET=0) → DP3-07/-11.
- **#4** DESI target bookkeeping inconsistent (37k vs 2,468; 98.8% GALAXY ≠ purity) → DP3-07/-11 (§III.C SPECTYPE composition + ZWARN=0 0.10% both disclosed).
- **#5** "like-for-like" Liang not like-for-like (20.3M vs 250k EDR; 0.012% vs 1.07%) → DP3-07 (denominators disclosed §III.C/§VI.E).
- **#6** DESI not object-level reproducible (86.6% hashes, ~1.3% re-pullable, pod-lost) → **DP3-15** OPEN-COMPUTE pod-gated (paper's OWN §II.F numbers; does NOT reset).
- **#7** CV mischaracterized out-of-sample (47k pool; folds fail val_loss gate mean 1.91) → DP3-01.
- **#8** injection-recovery not end-to-end (cleanest 5% substrate; no full-stream failure modes / negative control) → DP3-01/-12 (curation caveat (b)).
- **#9** Planck under-validated (train/val patches in bank; post-standardization bumps) → DP3-06.
- **#10** 10° CMB patches not point-detections; 5″ dedup invalid → DP3-06/-11 (disclosed as sky regions).
- **#11** 5″ FoF not catalog-grade unique count (no per-survey covariance / LR) → DP3-09/-11 (radius-sweep stability disclosed; no single-FDR claim).
- **#12** NEOWISE not validated tier (mask-by-construction; full-sample scaler) → DP3-01/-13 (masking-geometry QA gate disclosed abstract L1027).
- **#13** 17.8% novelty unsupported (catalog-nonmatch only) → DP3-07/-09/-11 (SIMBAD-unmatched framing; follow-up spectroscopy disclosed §DAS).
- **#14** 377,482 includes ~113k LAMOST failed detector → DP3-07/-14 (LAMOST failed-exploratory tier disclosed abstract L1027 + §lamost). NOTE: the DAS-sentence portion of the LAMOST claim is the DP3-21 fix (see #15).
- **#15 → GENUINELY-NEW → DP3-21 → FIXED v3.1.159-apjs.** See below.
- **#16** provenance/audit gap too serious for archival (Gaia synthetic, eROSITA/DESI/Planck lost, LAMOST contradictory) → DP3-08/-15 (paper's OWN disclosures). The Gaia+LAMOST DAS-sentence internal contradiction it names IS the DP3-21 fix.
- **f_NL #17** forecast not supported (angular ≠ absolute bias; incompatible F₀/α tables) → DP3-10/-19 (secondary null; App C disclosed).
- **NANOGrav** "not an application / KDE not timing-likelihood" → DP3-10 (env-SMBHB caveat scopes "decisive").
- **SDSS ρ=0.036** overinterpreted → DP3-12 (effect-size disclosed).
- **catalog-documentation-not-ApJS-schema** → DP3-20 (RELEASE_MANIFEST schema-flag table, CLOSED-BY-RELEASE).
- **[MINOR] 37.3M** conflation (36.76/36.93/37.29M) → DP3-03/-04 (footnote-⊗ reconciliation v3.1.152).

## GENUINELY-NEW finding (1) — DP3-21

**ChatGPT #15 (verbatim):** "The Data Availability section says LAMOST is excluded from the released per-object tables and 'every headline count,' although the 377,482 headline explicitly includes it; it also mentions a Gaia block carrying scores despite repeated statements that Gaia was removed from the catalog."

**Verified against live `paper3_apjs.tex` (NOT assumed):**
- DAS (L1700) literally said: *"the Gaia DR3 exploratory block carries per-object feature-space scores"* — a RELEASED scored block.
- §III.G `\label{sec:gaia}` says: *"The Gaia DR3 tier has been removed from this catalog and from every count … its 500 synthetic entries are removed from the released catalog product."* → **DIRECT CONTRADICTION.**
- DAS (L1700) also said LAMOST *"excluded from both the released per-object tables and every headline count."*
- §lamost says the *"top-113,342 native slice … is the released LAMOST anomaly set"*; survey-summary (L1222) sum 195,829+77,905+**113,342**+200+419 = 387,695 → dedup **377,482** → LAMOST IS in the 377,482 inclusive headline. → **CONTRADICTION.**

Internal DAS-vs-body inconsistency, NOT the disclosed-provenance class. M20 mapped ChatGPT #15 to provenance DP3-08/-15 only and MISSED the DAS sentence's own contradiction. Reader-visible + editable → **genuinely-new**.

**Fix (minimal, no number changed) — BOTH variants:**
- LAMOST: "the released LAMOST DR10 block carries per-object canonical-S scores but is a failed-exploratory tier (injection-recovery FAIL, §lamost) — it is included in the inclusive 377,482 total but *excluded* from the 268,519 validated catalog-grade headline."
- Gaia: "the synthetic Gaia DR3 tier (500 objects) is *excised* — removed from the released catalog product and from every count (§sec:gaia), so no Gaia block is released."

Every count identical (268,519 / 377,482 / 195,829 / 77,905 / 113,342 / 200 / 419 / 298 / 500).

**Directive-G hygiene:** recompile TinyTeX latexmk, 0 undef-refs, 41pp; bump v3.1.158-apjs→**v3.1.159-apjs**, `\date` **July 13, 2026**; re-mirror byte-identical PDF **md5 `b7b8f8a56efa5b7096c13449e6110cf2`** to `public/papers/paper3_apjs_v3.1.159.pdf` + `site/public/papers/paper3_apjs_v3.1.159.pdf` (3-way md5 match). PDF-verified: page-1 "July 13, 2026"; "no Gaia block is released" + "Gaia DR3 tier (500 objects) is excised" PRESENT; old "feature-space scores" line GONE (grep count 0). Draft variant fixed lockstep (v3.1.159).

## Streak + cap
- **1 genuinely-new → clean-wave streak 8 → 0** (directive-K reset; fix actioned this wave; clock restarts on next clean re-test of v3.1.159-apjs).
- **Cap HOLDS 56:** EXT verdict words unchanged vs M20 — Grok MAJOR (6) + ChatGPT REJECT (0) + Gemini REJECT/carry (0) = 50 + 6 = 56. The DP3-21 fix is a self-consistency correction, not a claim change.

## Integrity attestation
Both raws read verbatim before any disposition; no ACCEPT faked; the 1 genuinely-new finding VERIFIED against live `paper3_apjs.tex` before editing; every re-flag source-cited to a D-id + §-anchor + verified against live tex; DP3-15 OPEN-COMPUTE pod-gated (paper's own numbers → no reset); DP3-20 immutable-release DISSOLVED; no un-sourced dismissal; no math/number fabricated; the only edit is a wording correction removing a genuine internal contradiction — zero count changed.
