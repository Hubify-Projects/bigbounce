# Acceleration Log — process & tooling improvements (2026-07-10)

Two audit-and-implement rounds run during the H17 campaign day, per Houston's
"accelerate and get much more efficient" directive. Each entry: the measured
problem → the implemented fix → the effect.

## Round 1 (mid-H17)

| # | Measured problem | Fix (implemented) | Effect |
|---|---|---|---|
| 1 | Orchestrator ping-pong: each paper cycled owner→orchestrator→re-test→orchestrator→audit→orchestrator (~30–45 min of round-trips per cycle) | **Fused owner loops** — one Opus owner iterates close→INT-re-test→audit internally until 0 genuinely-new, returns once | P5 converged in 1 iteration, P4 in 2; both produced Claude INT ACCEPTs the same session |
| 2 | Re-disposition churn: reviewers re-flag the same items every wave; every audit re-wrote dispositions from scratch (biggest token cost per wave) | **Canonical disposition ledgers** — `project-context/peer-reviews/DISPOSITIONS/<P>.md`, 107 numbered entries with fingerprint keywords; audits match by fingerprint and cite `D<P>-NN` one-line, full treatment only for unmatched | H17F+H17G audits processed 49 findings with 0 full re-audits; wave audit time roughly halved |
| 3 | Directive-G by hand: every owner re-derived the 10-step bump→compile→mirror→Convex chain; slug/schema errors twice (orphan `p3`/`p5` rows left the live site stale) | **`tools/directive_g.sh <paper> <ver> "<changelog>"`** — one-shot chain with leak-gate, 0-undef compile check, byte-identical mirror discovery, Convex bump + read-back verify; canonical slug map baked in | Per-closure hygiene ~15 min → ~2 min; slug drift impossible |
| 4 | Gemini browser EXT burned ~3h failing 8 legs (silent upload throttle: chip vanishes before send, no banner) | Demoted browser-Gemini to one fresh-session attempt/day with in-place send-verification; failure mode + detection encoded in spec. **Real fix is Houston-gated: billed Gemini API key** | Stopped the recurring 3h/day loss; Gemini leg pending key |
| 5 | P5's recurring "environment-stratified confusion matrix" reviewer MAJOR was an open recipe, re-flagged every wave | **Computed it for real** — GZ1 overlap × DESI zall (22GB) × DESIVAST voids; void N=933 asymmetry −0.023 [−0.060,+0.014] vs non-void −0.005 [−0.020,+0.010], p=0.37; integrated as v0.1.118 with honest scale caveat | Last OPEN-COMPUTE item campaign-wide closed with a real measurement |
| 6 | INT script version labels hard-coded (stale labels made audits believe legs reviewed old PDFs) | `tools/int_api_review_2026-07-08.py` now reads `\paperVersion` (+ fallbacks) live from the tex | Review headers always truthful |
| 7 | Convex `sortVersions` lexicographic bug ("July 10" < "July 9") left stale "current" chips site-wide | `Date.parse`-based sort pushed via `npx convex dev --once` | Live site version chips honest |

## Round 2 (post-directive-K)

| # | Measured problem | Fix | Status |
|---|---|---|---|
| 8 | Ad-hoc browser shell blocks rewritten every wave — source of the day's real bugs (zsh word-split poller, false-READY regex, missed completed responses, 8 wasted polls on a dead chat; ~90 min lost) | **`tools/ext_submit.sh`** (proven per-reviewer submit recipes, URL-at-submit, Gemini in-place send-verify) + **`tools/ext_harvest.sh`** (union of working extraction selectors, dead-chat detection, manifest updates, verdict matrix output) | built + live-tested this session |
| 9 | Manual Convex verdict posting — 3 schema failures in one day (activityFeed `body`, externalReviews args, slug drift) | **`tools/post_verdict.sh`** — schema + slug map + cap-formula recompute baked in | built this session |
| 10 | INT re-test = 3 scattered commands with re-derived traps (ANTHROPIC_API_KEY unset; mandatory raw-save path — one unverifiable-verdict incident occurred and was corrected publicly) | **`tools/int_wave.sh <paper>`** — all three legs parallel, raw-save enforced, verdict triple printed | built + live-tested this session |
| 11 | Ledger audits spawn a full Opus agent even for 100%-re-flag raws | **`tools/ledger_match.py <raw> <paper>`** — fingerprint pre-matcher emits a draft match table; Opus adjudicates only UNMATCHED (explicitly a draft, not a replacement for judgment) | built this session |
| 12 | `directive_g.sh` validation re-run on an old version stole the Convex "current" row (same-date tie-break) | **`--verify-only` flag** — checks without re-mirroring/re-bumping | built this session |
| 13 | Browser crashes mid-flow (2×) with no recovery in the inline blocks | Auto-`$B connect`-and-retry wrapped into the round-2 scripts | built this session |

## Process rules that came out of the day (all in the canonical spec)

- **URL-at-submit** — capture the chat URL before any polling; a died agent can never orphan a submitted leg again (H16 failure mode eliminated; H17 lost zero submitted legs).
- **Every INT leg saves its raw before any verdict is recorded** — an unverifiable ACCEPT was caught, re-run (verified verdict: MAJOR), and publicly corrected on the feed.
- **Never repeat a timed-out browser call; never navigate <60s after a Gemini send.**
- **`claude -p` legs must run with `ANTHROPIC_API_KEY` unset** (subscription leg, directive I1).
- **Convex bump contract** — canonical slugs (P1U→paper-1a …), full arg schema, human-format datestamps; validations use `--verify-only`.
- **Two-clean-waves exit (directive K, Houston 2026-07-10)** — supersedes the literal 0/0/0 verdict-word bar; a genuinely-new finding resets that paper's clean count.

## Measured outcome of the day

- 8 real errors found and fixed (incl. a factor-of-2 that survived ~17 prior waves; a wrong sign in the paper's own central-claim narrative; five stale Bayes columns from a hard-coded superseded center).
- 2 verified Claude INT ACCEPTs (P4, P5), first verified EXT ACCEPT (Grok, P5), P2 Grok "accept with minor revisions", ChatGPT P5 REJECT→MAJOR.
- H17F + H17G: two consecutive 0-genuinely-new waves (49 findings, all ledger-matched) — then P2's verified re-run surfaced 8 presentation items (being closed as v1.7.112), honestly resetting P2's clean count per directive K.
- Wave cycle time: ~4–5 h (morning, ad-hoc) → ~1.5–2 h (evening, tooled), with the next wave expected under 1 h of wall-clock orchestration using the round-2 scripts.

## Standing bottlenecks (not tool-fixable)

1. **Billed Gemini API key** (Houston) — converts the throttled browser leg into an instant parallel API leg.
2. **Reviewer generation latency** (10–40 min/leg for ChatGPT/Gemini thinking modes) — irreducible; hidden by parallelism.
3. **arXiv wave-1 clicks, Cai email, human expert read** (Houston) — the only path past the measured pattern-066 verdict-word floor.
