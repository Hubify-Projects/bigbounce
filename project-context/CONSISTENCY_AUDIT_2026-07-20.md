# BigBounce Public-Surface Consistency Audit — 2026-07-20

Pre-publication consistency sweep (4-day deadline). Canonical truth = Convex
`paperVersions:current` (verified live this run). No browser tools used;
curl + repo greps + Convex HTTP only.

## Canonical truth (Convex, verified 2026-07-20)

| Paper | Version | Datestamp | Pages | md5 |
|-------|---------|-----------|-------|-----|
| P1A | v1A.0.124 | July 16, 2026 | 7 | 11172191d176dc8fc0651a1af682312d |
| P1B | v2B.0.11 | July 16, 2026 | 6 | 7c14c2a1d4fb58ed652a2231bbd7e17a |
| P2  | v1.7.125 | July 18, 2026 | 11 | 174d52d55719c5955f852d2365fdb9c8 |
| P3  | v3.2.0-r10 | July 16, 2026 | 17 | 9fb6e882068a4613132792633a9d7a60 |
| P4  | v1.0.268 | July 20, 2026 | 32 | 4e139b56b0718c70b73ae7295e4ee7b1 |
| P5  | v0.1.141-2026-07-16 | July 16, 2026 | 42 | 6a4e79b4df61bf37b25a801d19d61b62 |

All six Convex versions match the canonical set given in the brief.

## Pass/Fail matrix

| Check | P1A | P1B | P2 | P3 | P4 | P5 |
|-------|-----|-----|-----|-----|-----|-----|
| Convex version == canonical | PASS | PASS | PASS | PASS | PASS | PASS |
| LIVE versioned PDF (ct+md5) | PASS | PASS | PASS | PASS | PASS | PASS |
| LIVE alias PDF (ct+md5) | PASS | (alias=file) | PASS | PASS | PASS | PASS |
| LOCAL PDF md5 == Convex | PASS | PASS | PASS | PASS | PASS | PASS |
| PDF page-1 version+date current | PASS | PASS | PASS | PASS | PASS | PASS |
| index.md board version/readiness | PASS | PASS | PASS | PASS | PASS | PASS |
| paper-N/status.md top banner | PASS | **FAIL** | PASS | PASS | PASS | PASS |
| papers.ts version | PASS | PASS | PASS | PASS | PASS | PASS |
| papers.ts date/pp/pdfMeta | PASS | PASS | **FAIL** | PASS | **FAIL** | PASS |
| live-status.ts rendered version | PASS | PASS | PASS | PASS | PASS | PASS |
| live-status.ts base (latent) | PASS | PASS | PASS | PASS | **STALE** | **STALE** |
| readiness (62/56/80/56/80/74) | PASS | PASS | PASS | PASS | PASS | PASS |
| queue.md no stale-done OPEN | — | — | **FAIL** | — | **FAIL** | — |
| HF public artifacts resolve | — | — | — | — | PASS | — |

## PDF page-1 version/date check (per paper)

- P1A: `(Dated: July 16, 2026, 17:22 PDT (v1A.0.124))` — matches Convex. PASS
- P1B: `July 16, 2026 — v2B.0.11` — matches Convex. PASS
- P2:  `v1.7.125` / `(Dated: July 18, 2026, 12:00 AM PDT)` — matches Convex. PASS
- P3:  `Draft version July 16, 2026` / `(Dated: July 16, 2026, 17:57 PDT — v3.2.0-r10)` — matches Convex. PASS
- P4:  `Draft version July 20, 2026` / `(Dated: July 20, 2026; Version v1.0.268)` — matches Convex. PASS
- P5:  `(Dated: July 16, 2026, 16:36 PT (v0.1.141-2026-07-16))` — matches Convex. PASS

All 12 live PDF URLs (6 versioned + 6 alias) returned `content-type: application/pdf`
with md5 == Convex md5. All 6 local canonical PDFs (versioned + alias) md5 == Convex md5.

## HF public artifacts (HEAD/tree, all 200)

1. P4 overlay @ revision `911316f3…` — `apjs-release/v1.0.259-strict-primary/` resolves (MANIFEST.json etc). PASS
2. `g1-retrain-2026-07-17/` on `bamfai/galaxy-chirality-v2` — resolves; checkpoint LFS sha256 `aed109dc…` matches. PASS
3. `p4_compute_phase2_2026-07-18/` on `bamfai/galaxy-chirality-catalog` — resolves. PASS
4. Base repos `galaxy-chirality-catalog` / `galaxy-chirality-v2` — 200/200. PASS

## Discrepancy list (file/line fixes)

### D1 — paper-1/status.md P1B top banner is v2B.0.10, Convex is v2B.0.11  [FAIL]
`project-context/SSOT/paper-1/status.md:2` — top CURRENT P1B banner reads
"CURRENT P1B 2026-07-16 — v2B.0.10 closure." No v2B.0.11 banner exists anywhere
in the file (grep-confirmed). The v2B.0.11 closure (pytest-invocation command +
non-affiliation sentence) never got a status banner.
FIX: prepend a `CURRENT P1B 2026-07-16 — v2B.0.11` banner (md5
7c14c2a1d4fb58ed652a2231bbd7e17a, Convex row k5736xnxj5snq44sp86kv7je618aqt4d),
demote the v2B.0.10 line to HISTORICAL.

### D2 — papers.ts P2 date + pdfMeta narrative stale  [FAIL]
`site/src/data/papers.ts:213` — `lastUpdated: "2026-07-17"` → should be `"2026-07-18"`
(Convex datestamp + PDF page-1 both July 18).
`site/src/data/papers.ts:249` — pdfMeta says "updated Jul 17, 2026" and its
narrative describes the v1.7.123/124-era "G3 REAL COMPUTE CLOSURE … new Eq. 5 …
torsion bound." The served v1.7.125 PDF is the **July 18 dressed-metric
transmission closure** (Convex changelog: T_c(k)=1, |Δf_NL| ≤ 6.8e-8). md5 string
in pdfMeta (174d52d5…) is correct; date + closure description are stale.
FIX: date → Jul 18, 2026; narrative → dressed-metric transmission closure.

### D3 — papers.ts P4 date + page count + pdfMeta/tldr narrative stale  [FAIL]
`site/src/data/papers.ts:335` — `lastUpdated: "2026-07-17"` → should be `"2026-07-20"`
(Convex datestamp + PDF page-1 both July 20).
`site/src/data/papers.ts:380` — pdfMeta "PDF · 29 pp · v1.0.268" → page count
wrong: Convex pdfPages = 32, PDF is 32 pp → "32 pp". Narrative describes the
v1.0.266-era "two real-compute pod-campaign closures (val_acc 0.9931 / kappa
0.9733 … CE-ResNet re-provisioning gate remains open)" — superseded by the
v1.0.268 **CE-composition adjudication + honest-negative** (CE-included retrain
collapses to chance 0.5617; historical 93.69/92.10% headline not reproducible).
`site/src/data/papers.ts:336` — tldr carries the same v1.0.266-era description.
FIX: date → Jul 20; "29 pp" → "32 pp"; pdfMeta + tldr → v1.0.268 CE-composition
adjudication narrative.

### D4 — live-status.ts stale base version fields (latent, overridden — do not render)  [STALE]
`site/src/data/live-status.ts:121` — base `paper-4` `version: "v1.0.245"`
`site/src/data/live-status.ts:129` — base `paper-5` `version: "v0.1.140-2026-07-16"`
Both are overwritten by the `papers.map()` override block (paper-4 → v1.0.268 @
line 168, paper-5 → v0.1.141 @ line 201), so the RENDERED versions are correct.
The stale base values are latent drift — a refactor that drops the override would
surface them. Also `live-status.ts:170` `lastUpdatedDisplay: "July 16, 2026 · 5:30 PM PT"`
and the P4 `pendingWork`/`headline`/`summary` prose are all v1.0.266-era (Jul 17;
"val_acc 0.9931" as the headline) — narrative staleness only; version + readiness render correct.
FIX (hygiene): update base version fields to canonical; refresh lastUpdatedDisplay
+ P4 narrative to v1.0.268.

### D5 — queue.md stale OPEN rows that are actually done/superseded  [FAIL]
`project-context/SSOT/queue.md:22` — "🔴 OPEN: exact v1.0.266 confirmation" —
superseded: paper is now v1.0.268 (v1.0.267 + v1.0.268 landed after). The live
open item is "exact v1.0.268 confirmation" (already tracked at line 2).
`project-context/SSOT/queue.md:26` — "🔴 OPEN: P4 G4 monopole-mechanism injection
(H200, after G1)" — DONE in v1.0.267 phase-2 (paper-4/status.md:33: "the G4
mechanism result over 16.9M banked ViT forward passes excludes classifier
confusion at 0.0% of the observed monopole").
`project-context/SSOT/queue.md:28` — "🔴 OPEN: P2 dressed-metric transmission
derivation" — DONE in v1.7.125 (queue.md:5 DONE row + paper-2/status.md:12).
FIX: convert these three 🔴 rows to ✅ DONE / HISTORICAL.

### D6 — index.md board header date lags its content (cosmetic)  [minor]
`project-context/SSOT/index.md:1` — board comment header "CURRENT CANONICAL BOARD
2026-07-17" but its content lists P4 v1.0.268 (a July 20 version) and P2 v1.7.125
(July 18). Versions + readiness (62/56/80/56/80/74) are all correct; only the
header timestamp is behind. FIX: header → 2026-07-20.

## Check 4 — tasks.md / plan.md materially-stale sections (LIST ONLY, do not fix)

- `project-context/tasks.md` PUB-002 — provider-policy body still describes the
  OpenAI perspective as "Codex CLI authenticated by ChatGPT subscription … Grok/
  Gemini direct-provider API legs allowed." This is SUPERSEDED by standing
  directive N / HO-007 (2026-07-16): **Codex/OpenAI PAUSED entirely**; INT =
  Claude reviewer subagent + Grok + Gemini. HO-007 at the top notes the
  supersession, but PUB-002's own text reads as the active policy.
- `project-context/tasks.md` PUB-001 — target versions are stale: "P1A v1A.0.120,
  … P3 r5, P4 portability/provenance closure" vs current v1A.0.124 / r10 /
  v1.0.268. (The 2026-07-16 progress sub-bullet is current; the headline targets are not.)
- `project-context/tasks.md` Blocked CMUX-B02 — cites a reset "2026-07-15 07:00"
  now well in the past.
- `project-context/plan.md` "Account handoff checkpoint" + step 5 — instructs
  "set `BIGBOUNCE_CODEX_SUBSCRIPTION_ENABLED=1` to restore Codex as a normal
  review leg." At odds with the standing directive-N pause (conditional/
  aspirational, but reads as near-term restore).
- `project-context/plan.md` "Current execution order" — tooling-first HubStack-
  preflight-engine framing (steps 1-2) predates the drive-to-100 R-round loop
  that has actually been running the campaign; materially behind current practice.

## Summary

- Live site (Convex-driven, per directive A) is CONSISTENT: every live PDF serves
  the correct current bytes; every rendered version string + readiness number
  matches Convex.
- Static mirrors have drift: papers.ts P2/P4 (dates, P4 page count, both
  narratives), paper-1/status.md P1B banner (v2B.0.10 vs v2B.0.11), live-status.ts
  latent base versions + P4 narrative, and three stale queue.md OPEN rows.
- tasks.md/plan.md carry superseded provider-policy (pre-directive-N Codex) and
  stale target versions — listed, not fixed.
