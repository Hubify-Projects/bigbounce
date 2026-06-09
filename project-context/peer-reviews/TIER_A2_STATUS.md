# TIER A + A2 closure status (as of 2026-06-08 17:48pt, post-13 closures)

After 17 autoloop fires + 13 paper-level version bumps (12 META closures + 3
figure-addition rounds), this is the closure scoreboard for the
`HOUSTON_DECISION_PACKAGE.md` TIER A + A2 queue.

## Closures shipped (15 bumps; 12 META closures + 3 figure rounds)

| # | Item | Paper | Closure | Status | Verification |
|---|------|-------|---------|--------|--------------|
| #1 | T-Web/V-Web mislabel | P5 | v0.1.46 | ✅ CLOSED | ledger STUCK fire 16 |
| #2 | dedup heterogeneity | P3 | v3.1.76 | ✅ CLOSED | ledger STUCK |
| #3 | binomial null trial-count | P4 | v1.0.160 | ✅ CLOSED | ledger STUCK |
| #4 | wpivot definition | P1B | v1B.0.43 | ✅ CLOSED | ledger STUCK |
| #A1 | P1A Holst→Pontryagin (catastrophic) | P1A | v1A.0.45 | ✅ CLOSED | ledger STUCK + pattern-040 sweep clean |
| #A2 | P4 v1.0.160 footnote regression | P4 | v1.0.161 | ✅ CLOSED | ledger STUCK fire 16 |
| #A2-4 | P1B βALP=0.336° bound | P1B | v1B.0.44 | ✅ CLOSED | ledger STUCK fire 15+16 |
| #A2-5 | P1B SNR-on-mean vs per-realization | P1B | v1B.0.45 | ✅ CLOSED | ledger pending fire 17 |
| #A2-6 | P3 γ-CI dual-summary | P3 | v3.1.77 | ✅ CLOSED | ledger STUCK fire 15+16 |
| #A2-7 | P5 range terminology | P5 | v0.1.47 | ✅ CLOSED | ledger STUCK fire 15+16 |
| #A2-8 | P3 42hr wall-clock | P3 | v3.1.78 | ✅ CLOSED | ledger pending fire 17 |
| #A2-9 | P3 22.5M-vs-6.5M | P3 | v3.1.78 | ✅ CLOSED | ledger pending fire 17 |
| #A6 | P1A "without fine-tuning" contradiction | P1A | v1A.0.46 | ✅ CLOSED | ledger STUCK + pattern-040 sweep clean |
| — | P4 figures (4 added back) | P4 | v1.0.162 | ✅ SHIPPED | (no META anchor) |
| — | P1B figures (2 added) | P1B | v1B.0.46 | ✅ SHIPPED | (no META anchor) |
| — | P1A figures (2 added) | P1A | v1A.0.47 | ✅ SHIPPED | (no META anchor) |

## Remaining queue (still UNCLOSED)

| # | Item | Paper | Effort | Status |
|---|------|-------|--------|--------|
| #A3 | P2 f_a cancellation in β formula | P2 | ~2h text | **pre-drafted** in TIER_A2_P2_ALP_DRAFT_FIXES.md |
| #A4 | P2 spectator vs Ω_φ ≈ 0.17 | P2 | ~2h text | **pre-drafted** in TIER_A2_P2_ALP_DRAFT_FIXES.md |
| #5 | P4 cross-match audit | P4 | VERIFIED RESIDUAL (fire 12) | no fix needed |
| #6 | P4 post-MASTER leakage rerun | P4 | 1-day MC on pod | compute-bound |
| #A2-1 | P1A αem/(4π) coupling family | P1A | ~2h text + math | from fire 14 |
| #A2-2 | P1A θ propagating field ontology | P1A | ~1d structural | from fire 14 |
| #A2-3 | P1A "cubic axial-current operator" | P1A | ~1h text | from fire 14 |
| #A2-10 | P1B χ²±5.6 weighted-sample mean GOF | P1B | ~30min text | from fire 14 |
| #A2-11 | P2 Bayes factor one-sided prior | P2 | ~30min text | from fire 14 |
| #A2-12 | P3 per-element MSE without inverse-variance | P3 | ~2h text + retrain | from fire 14 |
| #A2-13 | P3 eROSITA threshold inconsistency | P3 | ~30min text | from fire 14 |
| #A2-14 | P3 SIMBAD 0.2% at random-coincidence floor | P3 | ~30min text | from fire 14 |
| #A2-15 | P5 radial selection function n(z) | P5 | ~2h text + rerun | from fire 14 |
| #A2-16 | P5 DESIVAST non-void definition | P5 | ~30min text | from fire 14 |

Plus fire 15 + fire 16 NEW ESS findings (14 + 14 from those rounds, not yet
queued).

## Pattern catalog status

| Pattern | Status | Detection |
|---------|--------|-----------|
| pattern-040 | DRAFT, ACTIVE | tools/v3_pattern040_cross_section_check.py — sweep-clean across all 6 |
| pattern-041 | DRAFT | tools/v3_pattern041_audit.py — heuristic, 75% verification rate |
| Tautological-by-construction (fire 16 P4-META-E2) | candidate | new pattern-040 rule (regex needs $-math-mode fix) |
| Weight-variance count-basis mismatch | candidate | new pattern-040 rule (regex needs tuning) |

## Tool inventory (14 tools)

```
ACTIVE:
  v3_review_autoloop.sh           hourly cron driver
  v3_native_pdf_review.py         per-reviewer call (5 vendors)
  v3_meta_review.py               gpt-5-pro meta-reviewer
  v3_review_synthesis.py          per-paper synthesis
  v3_meta_content_diff.py         pair-wise round NEW/RECURRING/CLOSED
  v3_persistence_tracker_v2.py    multi-round LOAD-BEARING
  v3_pattern040_cross_section_check.py  mechanical contradiction detector
  v3_pattern040_all_papers.sh     6-paper sweep
  v3_closure_verification.py      anchor-phrase scan post-closure
  v3_fire_closeout.sh             unified 4-step closeout wrapper
  v3_bundled_paper_bump.mjs       data-driven Convex bump
  v3_autoloop_log_entry.py        NEW THIS FIRE — auto-generates AUTOLOOP_LOG entry

DRAFT:
  v3_pattern041_audit.py          arithmetic hallucination heuristic

DEPRECATED:
  v3_persistence_tracker.py (v1)  keyword fingerprinting false-converged
```

## Convex state

```
1A: v1A.0.47 / 2026-06-08
1B: v1B.0.46 / 2026-06-08
2:  v1.7.43 / 2026-06-03  ← only paper without recent META closure work
3:  v3.1.78 / 2026-06-08
4:  v1.0.162 / 2026-06-08
5:  v0.1.47-2026-06-08 / 2026-06-08
```
