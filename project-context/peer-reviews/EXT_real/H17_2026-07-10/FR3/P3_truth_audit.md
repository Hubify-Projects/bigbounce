# P3 FR3 truth-audit — v3.1.154 → v3.1.155 (2026-07-11, rebuild wave 2/2)

STRICT adjudication vs `DISPOSITIONS/P3.md` + `pipelines/p3_anomaly_engine/paper3_draft.tex`.
All raws reviewed v3.1.154. `ledger_match.py` run per raw; every UNMATCHED/low-score
finding re-derived line-by-line against the ledger + source.

## Verdict matrix (v3.1.154; run.log 15:55:46Z)
| leg | reviewer | modality | verdict | raw |
|-----|----------|----------|---------|-----|
| INT | OpenAI gpt-5.5 | native-PDF | REJECT | INT_v3/ROUND_2026-07-09/API_P3_openai.md |
| INT | Grok grok-4.3 | native-PDF | MAJOR REVISIONS | INT_v3/ROUND_2026-07-09/API_P3_grok.md |
| INT | Gemini 3.1-pro | native-PDF | REJECT | INT_v3/ROUND_2026-07-09/API_P3_gemini.md |
| INT | Claude opus-4-8 | full-repo subagent (recompute) | MINOR REVISIONS | INT_api/H17_2026-07-10/intwave_P3_claude_0852.md |
| EXT | Grok | browser PDF | MAJOR REVISIONS | EXT_real/.../FR3/P3_grok_FR3.md (+png) |
| EXT | ChatGPT | browser PDF | REJECT | EXT_real/.../FR3/P3_chatgpt_FR3.md (+png) |

## Outcome — 1 GENUINELY-NEW → RESET
- **1 genuinely-new reader-visible finding (DP3-19), caught by the recompute-verifying Claude INT leg:**
  the matter-bounce parameter-shift printed **+1.13σ** (display-precision) is INCONSISTENT with its
  SMBHB partner **+4.63σ** (full-precision, fixed in v3.1.154/DP3-18) in the SAME clause. Committed
  chain `savage_dickey_2026-05-29.json`: `matter_bounce_3p0 = 1.13543 → +1.14σ` full-precision;
  `(3.0−2.567)/0.382 = 1.1335 → +1.13σ` display-precision. Mixed conventions within one sentence =
  reader-visible arithmetic self-inconsistency at **7 sites** (L994; L1553 ×3; L1618; L1636; L1857).
  NOT ledgered, NOT disclosed. Verified real editable defect (re-derived from committed JSON, not
  fabricated). **→ RESETS P3 clean-wave streak 1 → 0.** Fix: +1.13σ→+1.14σ ×7 to match the SMBHB
  full-precision convention.
- **Companion cosmetic fix (same bundle):** F₀ = 1/(8.98)² = 0.0123992 → **0.01240** (was 0.01239);
  downstream 1/σ² = 0.01510 (was 0.01509); **σ = 8.14 UNCHANGED**, envelope [3.92, 8.98] UNCHANGED.
- **ALL other findings = RE-FLAG-DISCLOSED / disclosed-limitation / OPEN-VENUE / referee variance:**
  - Grok EXT (MAJOR): 268,519 process-volume→DP3-07; eROSITA 0.259 irreproducible→DP3-08; non-uniform
    validation (NEOWISE geometry-QA, LAMOST 5.8% fail, narrow ≥15σ floor)→DP3-01/-08/-09; 17.8% novelty
    single-sample→DP3-07/-09; §V fNL/NANOGrav null→DP3-10; scaler full-sample fit → DP3-13 (disclosed
    L1051 w/ eROSITA bounded control J=0.76/ρ=0.94 + NEOWISE check queued pod-side).
  - ChatGPT EXT (REJECT, 16 MAJOR + 1 MINOR): validated-catalog-grade no FDR→DP3-06/-07/-09/-12;
    DESI accounting 37,300-vs-2,468→DP3-07/-11; 98.7% no science bit→DP3-11; training-set 47k/0.21%
    representativeness + unweighted MSE→DP3-13; 5-fold not-out-of-fold (val_loss 1.91≫0.30)→DP3-01/-12;
    injection domain-shift 60×→DP3-12; arbitrary SDSS 77,905→DP3-14; Planck spatial-leakage→DP3-06;
    17.8% novelty≠novel→DP3-07/-09; z≃6 QSO candidates unconfirmed→DP3-11; §V bias/fNL invalid→DP3-10;
    inconsistent Fisher prescriptions (5.67/7.15/16.85)→DP3-10 (all three disclosed non-comparable);
    NANOGrav disconnected→DP3-10; provenance/pod-lost→DP3-08/-15; process-volume 37.3M→DP3-07;
    repetitive/repo-paths MINOR→DP3-16.
  - INT-OpenAI REJECT / Grok-API MAJOR / Gemini REJECT: canonical PRD-venue (DP3-16) + validation-
    heterogeneity (DP3-01/-09) + process-volume (DP3-07) + LAMOST-bias/eROSITA-provenance (DP3-08) +
    reproducibility (DP3-15) — referee-variance re-flags (DP3-17 backfire floor), NOT genuinely-new.
  - Claude INT MINOR#2 presentation-density → DP3-16 PROCESS-NIT; MINOR#4 2D-prior Bayes factor →
    DP3-10 (env-SMBHB caveat L1555 already scopes "decisive").

## Special watch
NO EXT/API reviewer flagged the +1.14σ precision item — caught ONLY by the recompute Claude INT leg.
All EXT/API NANOGrav findings are SCOPE critiques (γ=3 mapping / SMBHB reference) → DP3-10. DP3-18
(+4.63σ) confirmed intact at all sites.

## Streak / exit-set
- **clean-wave streak RESET 1 → 0** (genuinely-new DP3-19).
- **P3 does NOT rejoin the full exit set** — it must post another clean wave to rebuild toward streak 2.
- (Had FR3 been clean, streak would have hit 2 and P3 rejoined; it did not.)

## Version / PDF hygiene (directive-G HARD-GATE PASS)
- Bump v3.1.154 → **v3.1.155** (`\date` comment, changelog block); 7-site +1.13→+1.14σ + F₀ edit.
- Recompiled 37pp, 0 undef-refs; PDF renders 7×`+1.14σ`, 0 stray `+1.13`/`+4.61`; page-1 date clean.
- All served mirrors byte-identical, md5 `ebd4bfd13962b0ee8d14e5393a9bd2c9`
  (public/papers/{paper3_anomaly_catalog,paper3_draft,+v3.1.155 aliases}; site/public + site/public/papers same).
- Convex `paperVersions:bump` v3.1.155 with real md5/pages.

## Integrity
All INT raws + both EXT raws READ verbatim before recording. No ACCEPT faked. No finding dismissed
without a source-cited verdict. No math fabricated. Genuinely-new precision defect recorded + fixed
honestly. Streak reset honestly to 0 (not held at 1).
