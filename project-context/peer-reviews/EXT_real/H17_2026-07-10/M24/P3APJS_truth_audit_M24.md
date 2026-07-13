# P3 (ApJS variant) — M24-EXT truth-audit

**Date:** 2026-07-13
**Paper:** P3 ApJS variant `pipelines/p3_anomaly_engine/paper3_apjs.tex`
**Reviewed version:** v3.1.159-apjs — **FIRST EXT read after the DP3-21 DAS self-consistency fix** (commit `e24b42a9`, v3.1.158-apjs→v3.1.159-apjs).
**Raws (read verbatim before any verdict):**
- `EXT_real/H17_2026-07-10/M24/P3APJS_grok_M24.md` — **VERDICT: MAJOR REVISIONS** (4 MAJOR + 2 MINOR)
- `EXT_real/H17_2026-07-10/M24/P3APJS_chatgpt_M24.md` — **VERDICT: REJECT** (16 MAJOR + 2 MINOR)

## CRITICAL CHECK — did the DP3-21 DAS fix hold? → **HELD**
The DP3-21 fix (v3.1.159-apjs) corrected the Data-Availability sentence's internal
self-contradiction: (a) it no longer claims "the Gaia DR3 exploratory block carries
per-object feature-space scores" (§sec:gaia says Gaia is excised from every count);
(b) it no longer says LAMOST is "excluded from … every headline count" (LAMOST's
113,342 IS in the inclusive 377,482 total).

**Signature grep of both M24 raws for the DP3-21 contradiction ("Gaia block carries
scores" / "LAMOST excluded from every count" / DAS internal contradiction):**
- Grok M24: NO DAS-contradiction signature (no `feature-space score`, no
  `excluded from every count`, no `contradict`).
- ChatGPT M24: the ONLY "Data Availability" hit is item #4 (L7) — the DP3-15
  reproducibility ceiling citing the paper's OWN disclosed 86.6%/~1.3% numbers, NOT
  the DP3-21 Gaia/LAMOST self-contradiction.

**Neither leg re-flags the DP3-21 inconsistency.** The fix landed. → **DAS-fix HELD;
P3 clean-wave streak 0 → 1.**

## Verdict matrix (EXT, from raw VERDICT lines)
| Reviewer | Verdict | MAJOR | MINOR |
|----------|---------|-------|-------|
| Grok EXT | MAJOR REVISIONS | 4 | 2 |
| ChatGPT EXT | REJECT | 16 | 2 |
| Gemini EXT | (carry — no M24 leg, browser hard-throttled) | — | — |

## ledger_match.py (DRAFT, conservative)
| Raw | Findings parsed | MATCHED | UNMATCHED | Rate |
|-----|-----------------|---------|-----------|------|
| Grok | 66* | 4 | 62 | verbose sidebar-history + ApJS §-anchor restatement inflate UNMATCHED |
| ChatGPT | 20 | 9 | 11 | verbose ApJS §-anchor restatement |

*Grok raw includes the full Grok project sidebar-history transcript; the parser split
it into 66 pseudo-findings. The 4 MAJOR + 2 MINOR real findings are adjudicated below.
Every UNMATCHED item Opus-adjudicated vs live `paper3_apjs.tex` — identical
disclosed-content set to M17/M20/M22.

## Per-finding adjudication

### Grok (4 MAJOR + 2 MINOR — all source-cited re-flags, 0 genuinely-new)
- **G1 [MAJOR]** Abstract/§1/§3 "validated catalog-grade 268,519" mixed with NEOWISE
  419 that fails the injection gate → **DP3-07** (process-volume + mixed-validation
  disclosed abstract first sentence) + **DP3-09** (heterogeneous per-survey gates).
- **G2 [MAJOR]** §2.4/§3.5/§3.7 eROSITA 0.259 axis irreproducible + synthetic-Gaia
  membership-only release → **DP3-08** (excised from every count, §erosita/§gaia +
  `tab:provenance`) + **DP3-15** (pod-lost provenance, disclosed).
- **G3 [MAJOR]** §3.1/Table 3 DESI 195,829 only ~1.3% (2,468) on science-target
  spectra; overstates yield vs Liang → **DP3-07** (2,468 like-for-like benchmark
  disclosed; 98.7% sky/filler §I reader's guide).
- **G4 [MAJOR]** §2.2/§6.4(i) injection-recovery only for broad class (99–100% @5σ);
  narrow ≥15σ floor not propagated to per-object flags → **DP3-01/-12** (single
  production gate + narrow-line floor disclosed §II.F + `tab:caveats`).
- **G5 [MINOR]** defensive/repetitive text, "process-volume", "read before Table 2"
  → **DP3-16** (honest disclosures retained per CRITICAL RESEARCH DIRECTIVE; venue
  presentation OPINION — PROCESS-NIT, no reset).
- **G6 [MINOR]** §5 multi-tracer f_NL + NANOGrav secondary null demos dilute focus,
  remove/appendix → **DP3-10** (titled "Secondary Demonstrations"; null retained per
  CRITICAL RESEARCH DIRECTIVE) + **DP3-16** (venue, Houston-gated).

### ChatGPT (16 MAJOR + 2 MINOR — same disclosed-content set as H17G/M17/M20/M22 REJECT)
- **#1** 268,519 not source-level; DESI 98.7% non-primary spectra → **DP3-07/-11**.
- **#2** DESI science-target accounting unresolved (36,750 implied vs 2,468 recount)
  → **DP3-07/-11** (SPECTYPE composition + ZWARN=0 0.10% disclosed §III.C).
- **#3** Liang "like-for-like" invalid (2,468/20.3M vs 2,685/250k) → **DP3-07**.
- **#4** DESI not reproducible end-to-end (86.6% hashes, ~1.3% re-pullable, pod-lost)
  → **DP3-15** OPEN-COMPUTE pod-gated (paper's OWN §II.F numbers; does NOT reset).
- **#5** validation ≠ purity/per-entry validity (k-fold fail val_loss gate; correlated
  folds) → **DP3-01/-12**.
- **#6** anomaly score not noise-controlled (unweighted MSE; >50% SPARCL flag; ~44k
  B-dominant artifacts) → **DP3-12/-13** (curation caveat (b); disclosed).
- **#7** SDSS 77,905 arbitrary fixed-size continuity slice (19,253 top-1%, 12 @S>5)
  → **DP3-09/-14** (footnote ♡ L1182 tabulates all three thresholds).
- **#8** SDSS characterization from failed cross-transfer set not native release
  → **DP3-14** (membership-overlap disclosed gap; native re-score is the released tier).
- **#9** Planck memorization/overlapping-patch binomial invalid → **DP3-06**.
- **#10** NEOWISE mask-by-construction tautology, no detector validation → **DP3-08/-09**
  (masking-geometry QA gate disclosed; heterogeneous gate matrix).
- **#11** combined headline no coherent selection function (sums absolute + fixed-size
  + top-N; LAMOST fails; 5″ optical×10° CMB merge) → **DP3-07/-09** (union of
  per-survey gated sets, no single-FDR claim; disclosed by design). *Note: the LAMOST
  reference here is the failed-exploratory-tier disclosure, NOT the DP3-21 DAS
  contradiction — ChatGPT does not re-raise the "excluded from every count" DAS wording.*
- **#12** 17.8% novelty not genuine (top-1,000 stratum; sky/filler unmatched) → **DP3-07/-09/-11**.
- **#13 [MINOR]** §4.2–4.3 spatial/random-coincidence not selection-function controlled
  → **DP3-07/-09** (RA-shift + footprint caveats disclosed §IV).
- **#14** §5/App C f_NL forecast not supported (α=0.19±0.65; incompatible 8.98/16.85
  normalizations) → **DP3-10** (secondary null) + **DP3-19** (already-audited
  normalization-inconsistency = distinct non-comparable reference models, disclosed).
- **#15** §5.1/App E NANOGrav unrelated, Savage-Dickey not full likelihood → **DP3-10**
  (env-SMBHB caveat scopes "decisive").
- **#16 [MINOR]** not self-contained for ApJS (definitions dispersed) → **DP3-16/-20**
  (RELEASE_MANIFEST schema; presentation OPINION, PROCESS-NIT, no reset).

## Streak + cap
- **DP3-21 DAS fix HELD (neither leg re-flags it) → 0 genuinely-new → clean-wave
  streak 0 → 1** (first clean re-read of v3.1.159-apjs; directive-K clock restarts).
- **Cap HOLDS 56:** EXT verdict words unchanged vs M22 — Grok MAJOR (6) + ChatGPT
  REJECT (0) + Gemini REJECT/carry (0) = 50 + 6 = 56.

## Integrity attestation
Both raws read verbatim before any disposition; the DP3-21 DAS-fix check performed by
signature-grep of both raws + Opus read (HELD — no re-flag); every finding source-cited
to a standing D-id + §-anchor verified against live `paper3_apjs.tex`; DP3-15
OPEN-COMPUTE pod-gated (paper's own numbers → no reset); DP3-20 immutable-release
DISSOLVED; no ACCEPT faked, no finding dismissed without a source-cited verdict, no
math/number fabricated; no edit this wave (v3.1.159-apjs stands; directive_g.sh NOT run).
