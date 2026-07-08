# P3 INT — full-source regression check (v3.1.144)

**Reviewer:** Claude Code INT (subscription subagent, full-source read — CLAUDE.md I1)
**Scope:** closure-wave regression check only (title reframe vs abstract vs body; count integrity). No new-finding hunt.
**File:** `pipelines/p3_anomaly_engine/paper3_draft.tex`

## Verdict: CLOSURE WAVE CLEAN — no regressions

### Title reframe (commit 5cc65eca)
- OLD (v3.1.143): `A Multi-Survey Autoencoder Anomaly Catalog: 268,519 Validated Sources`
- NEW (v3.1.144, L48): `A Multi-Survey Autoencoder Anomaly-Candidate Catalog: 268,519 Reconstruction-Outlier Sources`
The only body change in the commit is the title line + `\date` bump to July 8. "Validated Sources" is fully removed from the title; the headline noun is now "Reconstruction-Outlier Sources" (mechanism-neutral) under an "Anomaly-Candidate Catalog".

### "Anomaly-Candidate" used consistently; no leftover "Validated Sources" claim
- Grep of all non-comment lines: **zero** occurrences of "Validated Source"/"validated source" as a headline claim anywhere in the body.
- "Anomaly-Candidate" appears in the title; the abstract carries the compatible framing already present from prior versions.
- Note: v3.1.144 comment block (L71–72) says "the title's 'Validated Sources' is now immediately contextualized" — this is **stale intent-text**; the actual edit fully replaced the title noun. Comment-only, no bearing on rendered PDF. (Non-blocking; flag for tidy, not a regression.)

### Abstract ↔ title ↔ body consistency
- Abstract (L896) labels **268,519** the "validated catalog-grade subset" and explicitly a **process-volume** figure — "anomaly candidates surviving per-survey validation gates … NOT confirmed physical detections" — with like-for-like science-target benchmark **2,468** DESI clusters (≈0.92× Liang2023's 2,685). Title's "268,519 Reconstruction-Outlier Sources" is consistent: 268,519 is the validated subset; "reconstruction-outlier" is the estimator, not a physical-detection claim.
- Process-volume "read once" paragraph (L898) repeats the framing and multipliers (~141×, ~73×) as process-scale, not like-for-like — consistent with abstract.

### Count integrity — 377,482 chain + 2,468 pairing INTACT
- **377,482** full inclusive Path-C unique catalog (377,282 point-source + 200 Planck CMB patches): 23 occurrences; chain 274,353→268,519 at 5″ (recomputable via committed script) stated in abstract. No count changed in v3.1.144 (title-only diff).
- **2,468** DESI science-target benchmark: 29 occurrences, ≈0.92× the 2,685 Liang2023 benchmark, consistent everywhere.
- eROSITA (298) + former Gaia (500) excluded from every count including the inclusive 377,482 — stated consistently in abstract.

Regressions: **none**.
