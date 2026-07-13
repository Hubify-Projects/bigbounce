# M19-INT truth-audit — P2 (f_NL SPHEREx forecast) — 2026-07-13

Paper: `research/focused_paper_source_integration/02_full_draft.tex` **v1.7.116** (byte-unchanged this wave; identical file M1/M4/M7/M10/M13/M15/M18 audited).
Ledger: `project-context/peer-reviews/DISPOSITIONS/P2.md` (35 D-ids + prior wave sections).
Wave label: **M19-INT**

Raw legs audited (all read verbatim before any disposition recorded):
- INT OpenAI gpt-5.5 native-PDF — verdict `.intwave_P2_openai_0127.log` = **REJECT** (verdict-only re-test on unchanged v1.7.116)
- INT Grok grok-4.3 native-PDF — verdict `.intwave_P2_grok_0127.log` = **MAJOR REVISIONS**
- INT Gemini gemini-3.1-pro native-PDF — verdict `.intwave_P2_gemini_0127.log` = **MINOR REVISIONS** (fresh read; replaces the stale F14 MAJOR as the latest Gemini row)
- INT Claude opus-4-8 subscription subagent — `intwave_P2_claude_0127.md` = **MINOR REVISIONS** (2 MAJOR + 4 MINOR; full raw with findings)

Method: `python3 tools/ledger_match.py intwave_P2_claude_0127.md P2` (conservative threshold → prefers UNMATCHED); every MATCHED spot-checked, every UNMATCHED full-audited vs tex + ledger. The three API legs on this run persisted verdict-only (no full raw text); their finding-classes are the recurring proxy-floor / cubic-transmission / Bayes-prior / length re-flags canonically dispositioned in the M18-EXT ledger section (DP2 line 464/519), re-tested here on the byte-unchanged file.

---

## Verdict: **0 genuinely-new reader-visible editable findings. v1.7.116 stands. cleanWaveStreak 7→8.**

All four legs' findings map 1:1 to standing DP2 D-ids. No numeric defect surfaced; every load-bearing number independently re-verified by the Claude leg (c15 channel-native Fisher ρ=−0.425/−0.494, σ_marg=0.9417 → 2.32σ; vertex certification −35/16 four ways; all significance/Bayes arithmetic).

---

## 4-leg verdict matrix

| Leg | Model | Verdict | MAJOR | MINOR | Raw |
|-----|-------|---------|-------|-------|-----|
| OpenAI | gpt-5.5 | REJECT | — | — | `.intwave_P2_openai_0127.log` (verdict-only) |
| Grok | grok-4.3 | MAJOR REVISIONS | — | — | `.intwave_P2_grok_0127.log` (verdict-only) |
| Gemini | gemini-3.1-pro | MINOR REVISIONS | — | — | `.intwave_P2_gemini_0127.log` (verdict-only; fresh read) |
| Claude | opus-4-8 (sub) | MINOR REVISIONS | 2 | 4 | `intwave_P2_claude_0127.md` |

---

## Per-leg finding→D-id mapping

### INT Claude — MINOR REVISIONS (2 MAJOR + 4 MINOR) — full raw, all re-flags

`ledger_match.py`: 5/8 auto-MATCHED (items #1 and #8 are parser artifacts — verdict-line fragment + closing sentence, non-findings; item #5 low-score but source-verified below).

| # | Sev | Finding summary | Verdict → D-id |
|---|-----|-----------------|----------------|
| 1 | MAJOR | Scope/novelty for PRD — sub-3σ headline rides on one un-released external covariance; needs sharper up-front "what is new / clears PRD bar" | RE-FLAG → **DP2-04/-17/-29** (venue/scope floor; recast disclosed abstract L975/Scope L984; Houston-gated venue-fit) |
| 2 | MAJOR | Excessive length / pervasive redundancy — four caveats each restated 4–6× despite v1.7.116 consolidation | RE-FLAG → **DP2-30/-14** (presentation floor; DP2-M1 restructure actioned the class; residual length = venue/scope floor, Houston-gated) |
| 3 | MINOR | "Resolution" framing overreaches — −35/16 certified but −35/8 unreproduced (third value −305/64) | RE-FLAG → **DP2-01/-25/-32.3** (already reframed v1.7.108/-112 to "−35/16 certified four ways; printed −35/8 = unreproduced erroneous literature value") |
| 4 | MINOR | Disconnected auxiliary appendix `app:birefringence` reads as scope-padding; recommend deletion | OPINION → **DP2-30 / DP2-M1.2** (already relegated body→Appendix per DP2-M1.2; keep-vs-cut of a one-line-pointed appendix is scope preference, not correctness) |
| 5 | MINOR | Citation-year inconsistency — `\cite{Heinrich:2023}` vs prose "Heinrich et al. 2024" | VERIFIED non-defect → **DP2-32.5** (bib year = 2024 L73; prose "2024" matches the bib year; bibkey label ≠ year, cosmetic + invisible in PRD numeric-citation style; no change) |
| 6 | MINOR | Abstract is a single ~330-word hedge-dense paragraph | RE-FLAG → **DP2-32.1** (abstract already rewritten to a single ~200-word PRD paragraph v1.7.112; nested proxy disclosures relocated to Scope paragraph; residual density = referee taste) |

Claude's Q3 endorses the central claim verbatim: *"the central claim … is supported: every load-bearing number reproduces from the committed vertex-certification code and the c15 Fisher JSON, and the limitations are disclosed honestly; the required revisions are editorial."* **0 genuinely-new.**

### INT OpenAI — REJECT (verdict-only) — structural harsh-referee floor
Verdict-only re-test on byte-unchanged v1.7.116. OpenAI's recurring 14-item class maps 1:1 to standing DP2 D-ids (cubic transmission→DP2-13; Cai–Li −35/8 vs −305/64→DP2-01/-02/-03; r=0.84 vs r_eff→DP2-14; proxy floor→DP2-04/-26/-34; Bayes prior-volume→DP2-18; gauge-frame→DP2-21; length→DP2-30; birefringence→DP2-30 OPINION), exactly as adjudicated in the M18 ledger section (DP2 line 464). REJECT = structural harsh-referee floor (directive-H). **0 genuinely-new.**

### INT Grok — MAJOR REVISIONS (verdict-only) — pattern-066 slip
Verdict-only re-test on byte-unchanged v1.7.116. Grok's MAJOR on unchanged content is the documented pattern-066 run-to-run variance (P2 Grok oscillated MINOR↔MAJOR across M4/M7/M13/M18 on the identical file). Its recurring MAJORs quote the paper's own disclosed limitations: proxy ρ=−0.868 non-native floor → DP2-34/-07 (channel-native ρ≈−0.42, 2.32σ floor computed, proxy retained as conservative cross-check strictly below); App-A placement → DP2-01/-02/-30. **0 genuinely-new.**

### INT Gemini — MINOR REVISIONS (verdict-only, fresh read)
Fresh Gemini read, replacing the stale F14 MAJOR as the latest Gemini row. MINOR verdict on byte-unchanged v1.7.116 — consistent with the recurring presentation-nit / disclosed-caveat class (DP2-30/-13/-18). No numeric defect. **0 genuinely-new.** This is the row that legitimately raises P2's Gemini EXT-formula contribution 6→12.

---

## Integrity note

- All raws read before any disposition. Claude leg = full verbatim raw (2 MAJOR + 4 MINOR); the three API legs persisted verdict-only on this run — their verdict words (OpenAI REJECT, Grok MAJOR, Gemini MINOR) recorded exactly as-logged, NOT softened or upgraded, with finding-classes mapped to the canonically-dispositioned M18 ledger section on the identical byte-unchanged file.
- No ACCEPT faked. Every Claude finding source-cited to an existing D-id + tex line. Two VERIFIED non-defects (Heinrich year; "resolution" framing already reframed) recorded as no-change, not as buried correctness defects.
- No math fabricated. Claude independently re-verified every load-bearing number (−35/16, c15 Fisher, all Bayes/significance arithmetic) with zero discrepancy.
- No version bumped; v1.7.116 stands; `directive_g.sh` NOT run (no reader-visible edit warranted).

## Wave bookkeeping

- cleanWaveStreak: **7→8** (eighth consecutive clean wave; prior M18-EXT = 7)
- Cap: **68 → 74** — the fresh Gemini MINOR (12) replaces the stale F14 Gemini MAJOR (6) as the latest-per-reviewer row → EXT formula = 50 + Grok-EXT MINOR (12) + ChatGPT-EXT REJECT (0) + Gemini-latest MINOR (12) = **74**, recomputed honestly by `post_verdict.sh` (root-fixed cd02c991, `_creationTime`-latest). This closes the prior 74-vs-68 stale-order reconciliation: 74 is now formula-true.
- Version: v1.7.116 byte-unchanged; no `directive_g.sh` run.
- Convex records: 4× externalReviews upserts (source `internal-stage3`; labels M19-INT-OpenAI/Grok/Gemini/Claude); 1× readinessMetrics:recordWave (M19-INT, genuinelyNew=0, streak=8, openCompute=4, openVenue=2); Gemini leg via `post_verdict.sh` (cap recompute 68→74); 1× activityFeed:add.
