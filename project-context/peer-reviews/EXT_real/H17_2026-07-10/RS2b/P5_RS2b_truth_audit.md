# P5 RS2b truth-audit — recovered ChatGPT EXT retry (v0.1.123, 2026-07-12)

STRICT ledger-first, verdict-first, source-cited. Skeptical stance; not told a convergence conclusion.

**Raw:** `RS2b/P5_chatgpt_RS2b.md` — **VERDICT: MAJOR REVISIONS** (line 1, verbatim). 12 MAJOR + 3 MINOR.
**Fills the RS2 ChatGPT dead-GAP** (recorded as a chart GAP, never faked). Re-test is of the **fully-corrected v0.1.123** (RS1 fixed the DP5-22 RSD-estimand mislabel + sign + √0.898 quadrature).
**Pre-triage:** `tools/ledger_match.py` → 12/16 MATCHED, 4 UNMATCHED (1 parser-noise + 3 real, all Opus-adjudicated below).

## Floor-crack holds; RS1 fix confirmed
ChatGPT REJECT (RS1b, pre-fix v0.1.122) → MAJOR (RS2b, corrected v0.1.123): the tier-lift is on the FIXED paper. Critically, ChatGPT engaged the corrected reconstruction block (tex l.838-850, raw l.35) and did **NOT** re-raise the DP5-22 estimand-mislabel/sign defect it independently caught in RS1 — the fix landed and is accepted by the same referee that caught it.

## Per-finding disposition (0 genuinely-new)
| # | sev | D-id | source-cited |
|---|-----|------|--------------|
| 1 | MAJOR | DP5-06 | §VIII B "Footprint ≠ selection function" tex l.3138; residual → `tab:systematic_budget` |
| 2 | MAJOR | DP5-07 (+DP5-16) | volume-limited anchor vs z≤0.24 outcome disclosed l.861-867; GALZONE valid-parent inner-join DP5-05 |
| 3 | MAJOR (UNMATCHED#4, 0.20) | DP5-19 | reviewer quotes §VIII B `\emph{Adjustment in lieu of a full covariate regression.}` l.3273-3293 (logistic/IPW form + program-split adjustment set + DR2 disclosure) |
| 4 | MAJOR | DP5-04 (+DP5-13/-16) | `tab:bonferroni5_family` §VIII D + exact-membership canonical row; post-hoc disclosed §V B |
| 5 | MAJOR | DP5-11 | §VIII term list + √0.898 quadrature, informal envelope (OPINION) |
| 6 | MAJOR | DP5-10 | CI labeled "counting-statistics-only" — OPEN-COMPUTE disclosed |
| 7 | MAJOR | DP5-08+09 | void-stratified confusion matrix l.822-828 (diff −0.018 z=−0.89 p=0.37, ±3.7pp under-powered → caveat STAYS) |
| 8 | MAJOR | DP5-08+09 | monopole cancellation scoped to catalog-wide amplitude; env-relabeling handled via stratified matrix (see #9) |
| 9 | MAJOR (UNMATCHED, 0.30) | DP5-08+09 | algebraic-cancellation claim l.873-876 correctly scoped to catalog-wide monopole, NOT per-galaxy relabeling; reviewer cites paper's own disclosed differential-error axis |
| 10 | MAJOR | DP5-12 (corrected content, re-engaged) | v0.1.123 l.838-850 correctly labels reconstruction as unrestricted-secondary + corrected sign + "primary not itself reconstructed"; ChatGPT re-flags the disclosed residual (no full nonlinear catalog re-derivation, paper concedes l.847-850) — NOT the fixed defect |
| 11 | MAJOR | DP5-14 | ~73%/~23× randoms sensitivity = paper's OWN disclosure; T-Web secondary/diagnostic |
| 12 | MAJOR | DP5-20 | App B "speculative … not a derived constraint," relegated (OPINION on non-load-bearing appendix) |
| 13 | MAJOR | DP5-21 | §I/§XIII/App A disclose public labels + coordinated submission — OPEN-VENUE, Houston-gated |
| 14 | MINOR | DP5-17 (+DP5-11) | reconciliation class, DP5-01/17 disclosed |
| 15 | MINOR (UNMATCHED, 0.12) | DP5-22 (+DP5-16) | QSO inclusion disclosed `SPECTYPE ∈ {GALAXY, QSO}` l.1358 + GALAXY-only path l.1363; match-radius 0.02pp tabulated |
| 16 | — | PARSER-NOISE | "REVISIONS ISSUES:" header fragment |

## Streak / Cap
- **Streak HOLDS 3** (was 3 after RS2 Grok EXT ACCEPT; this leg is the ChatGPT retry recovering the GAP; 0 genuinely-new; no reset).
- **Cap 79→85** — chatgpt reject→major floor-crack lifts +6: 50 + grok-ACCEPT 16.7 + chatgpt-MAJOR 6 + gemini-MINOR 12 = 84.7 → 85. `post_verdict.sh` first returned 74 (same-datestamp list-order tie-break bug kept an older ChatGPT REJECT as "latest"); corrected via true latest-by-creationTime.

## Integrity
MAJOR verdict read verbatim before any disposition; no ACCEPT faked; every disposition source-cites a tex line/artifact; no dismissal without a source-cited verdict; no math fabricated. Fingerprints added to DP5-19/-08/-09/-22/-12.
