# Session handoff / running log — 2026-09-02 (orchestrator: Fable 5.1, medium)

Running log; finalized at session end. Canonical truth stays in `SSOT/`.

## Routing re-plan (directive N-AMENDED, commit b3c5efd9, applied ~19:55Z)
Lanes were launched under the v5 prompt's "Opus for science" rule. Houston's
N-AMENDED correction arrived via a peer session and was verified in `CLAUDE.md`
before acting. Re-plan:
- KEPT on Opus (in flight, science computation; treated as the 1 Fable-class
  slot + 2 Opus slots): ledger #1 second-method f_NL derivation (contested
  math), A2 transmission computation, A3 multi-channel computation.
- STOPPED and RE-ISSUED as Sonnet (~20 min of partial work reused from disk):
  ECH Note merge (P1A→P1C), P4′ fold (P5→P4 + ledger #5 script), endorser
  outreach + portal kits.
- Sonnet from the start: repo reconciliation, INTENT/lineage, backup
  verification. Haiku/monitor: pod phase-3 watcher.
- Going forward: every Agent call carries an explicit model; ≤2 Opus, ≤1
  Fable concurrent; Sonnet unlimited.

## Lane ledger (updated as lanes land)
| Lane | Model | Status | Receipt |
|---|---|---|---|
| Repo reconciliation (both repos) | sonnet | DONE | f4478028, 2d93d0e4, a657dbb0, f5f2c845; scistack 55b065e; hubify recovery branch deleted (7d45ecc7, pure-deletion snapshot); ours-merge fb3311ee; origin+upstream both at fb3311ee |
| INTENT.md + PAPER_LINEAGE decisions | sonnet | DONE | 3c9c3684 |
| Backup verification sweep | sonnet | DONE | 7d2acdda — B2/HF/local/Zenodo/Convex/RunPod all PASS; gaps: Convex P4 title count stale (890,069 vs 949,584), no P1C Convex row |
| Ledger #1 f_NL second method | opus (fable-class) | DONE — VERDICT OTHER: f_NL=(5ε−35)/8 → −55/16; P2′ BLOCKED | d7dac953; ledger 8d08af2b |
| f_NL three-value reconciliation (in-in from scratch) | fable | running | — |
| A2 transmission coefficient | opus | DONE — linear-transfer half: T=(1−ρ)/2, 0<T≤1/2; LQC 1/4, non-LQC 0.196, Quintin-type 0.165; P2 assumption (d) unsupported; bounce's own cubic term OPEN | ea1da739 (swept), 9c7f50c0; ledger 868fd46d |
| A3 multi-channel + NANOGrav reclaim | opus | DONE — PTA reproduced, PBH new, reach table, 4-pp skeleton | d7dac953 (swept), 9a1c1e2e; ledger 86a2300c |
| ECH Note merge (P1N v1N.0.1) | sonnet (re-issued) | DONE — 6 pp, 0 undef, 0 overfull, consistency 4/4, sha 2287537b | 51d8af1b; board R1 dispatched (Grok/Gemini API; Claude leg queued for an Opus slot) |
| P4′ + ledger #5 (P4P v4P.0.1) | sonnet (re-issued) | DONE — 6 pp, 0 undef, 0 overfull, md5 d3e6f077; exclusion: A_95^obs≈0.98% excludes alignment fraction >0.98%, 2–20× below Longo/Shamir claims; Popławski gives only a qualitative axis | ac065a61; board R1 running (Grok/Gemini API + Claude Opus leg) |
| Endorser outreach + portal kits | sonnet (re-issued) | DONE — 4 codes × 5-6 endorsers; CQG 'Note' ≤2500 words → submit as CQG Paper; JCAP needs arXiv ID first → PRD-L primary | a4ee4ac4; DOI note fix 86a2300c |
| Hubify reconciliation + lab surfaces + repro import | sonnet | DONE — surfaces on Track A/B/C; `hubify repro-import` CLI + 7 tests; dry-run 3 programs/52 experiments/0 errors; topology: hubify.com runs on scintillating-cow-269 (bigbounce prod-tier), documented; parity check waits on bigbounce Convex migration; HUBIFY_TOKEN push step blocked | hubify b8338b46, ece557b7, 50d3dfd3, 8a3d90b2 (pushed); bigbounce 9ece5591 |
| Pod 8ofv5d4ynu7hku phase 3 | monitor | 747 shards at 20:02Z (~3/min → many hours) |
| Site reframe + Convex migration + deploy | sonnet | DONE — Track A/B/C live at bigbounce.hubify.app, flat /papers kept, P1N/P4P v0.1 registered in Convex, stale 'programs/six packages' copy fixed, headed QA PASS, freshness gate PASS | 6 commits on origin/main; project-context/SITE_REFRAME_2026-09-02.md | PHASE3_DONE watch armed |

## Blockers recorded
- `HUBIFY_TOKEN`: not in hubify `.env.local`, not in Keychain; the You.md
  encrypted vault (`~/.you/secret-vault/env-vault-2026-08-21T1804Z.tar.enc`)
  needs Houston's passphrase; `hubify auth login` is interactive. → click-list.
- launchd `com.bigbounce.cron-tick` (hourly) and `com.bigbounce.loopwatchdog`
  (15 min) are Codex-driven review-loop drivers (`codex exec`, gpt-5.6-sol,
  CODEX_ENABLED=1 by default) — forbidden under directive N and a review-as-
  product loop under R2. Both were dying on TCC (exit 78 / EPERM) but retried
  every fire. **Unloaded 2026-09-02 ~20:35Z via `launchctl bootout`; plists kept
  in ~/Library/LaunchAgents (reversible).** `com.bigbounce.caffeinate` left
  loaded. Click-list: confirm permanent retirement (delete plists) or ask for a
  Claude-native watcher instead.
- Reproducibility manifests: 6 new manifests today needed schema-v1 conformance
  (paper-code enum predates A2/A3/P1N/P4P); Sonnet worker fixing with additive
  enum extensions; 61 manifests total.
