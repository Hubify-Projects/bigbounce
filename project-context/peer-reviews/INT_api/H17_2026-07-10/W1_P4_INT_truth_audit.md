# W1-INT truth-audit addendum — P4 (chirality catalog) — 2026-07-11

Paper: `pipelines/p2_chirality/chirality_catalog_paper.tex` **v1.0.235** (no change this wave).
Ledger: `project-context/peer-reviews/DISPOSITIONS/P4.md` (21 D-ids).
Raw legs audited:
- INT Claude-subagent — `INT_api/H17_2026-07-10/intwave_P4_claude_1931.md` (MINOR REVISIONS)
- INT OpenAI gpt-5.5 native-PDF — `INT_v3/ROUND_2026-07-09/API_P4_openai.md` (REJECT)
- INT Grok grok-4.3 native-PDF — `INT_v3/ROUND_2026-07-09/API_P4_grok.md` (MAJOR REVISIONS)

Method: `python3 tools/ledger_match.py <raw> P4` on each (conservative threshold →
prefers UNMATCHED). Every MATCHED spot-checked; every UNMATCHED full-audited vs
tex + `EXT_real/H17_2026-07-10/P4_truth_audit.md` + `DISPOSITIONS/P4.md`.

## Verdict: 0 genuinely-new editable findings. v1.0.235 stands. cleanWaveStreak = 3.

Disposition anchors re-verified intact against current v1.0.235:
`sec:prereg` L713, `tab:primary_callout` L824, `sec:monopole_mask_null` L1005,
`sec:pseudolabel_independence` L1073, `sec:sensitivity` L1078,
`sec:parity_translation` L1177, `tab:wls_fit` L1414.

### INT Claude — MINOR (2 UNMATCHED)
| # | finding | verdict → D-id |
|---|---------|----------------|
| 2 | ~47% harmonic residual, physical origin unresolved | RE-FLAG → **DP4-17** (OPEN-COMPUTE, disclosed) |
| 3 | spatially-resolved confusion matrix absent | RE-FLAG → **DP4-15** (OPEN-COMPUTE, disclosed) |
| 5 | p_eq>0.6 outcome-adjacent cut | RE-FLAG → **DP4-07** (disclosed, prereg L713) |
| 1 (UNM) | "REVISIONS (2) ISSUES" | PARSER NOISE — verdict-header fragment, not a finding |
| 4 (UNM) | presentation density / length (37pp) | OPINION → **DP4-13** (style/consolidation, non-editable) |
Claude self-states: "zero genuinely-new correctness defects; every number recomputed matches the committed artifacts." Its own MINORs are labelled disclosed-and-answered.

### INT OpenAI — REJECT (10 UNMATCHED) — identical 1:1 structure to DP4-20
| # | finding | verdict → D-id |
|---|---------|----------------|
| 1 (UNM) | HC subsample ~30%, cut may suppress real signal | RE-FLAG → **DP4-07** |
| 3 (UNM) | classifier validation inadequate (69.91% GZ1 acc, 66.5% pseudo-labels, miscalibration) | RE-FLAG → **DP4-15 + DP4-08** |
| 9 (UNM) | flip-identity QC affects 2.9% / 59,515 HC rows | RE-FLAG → **DP4-08** (disclosed, excl. changes nothing) |
| 10 (UNM) | parity-even/odd/monopole language conflation, speculative CS link | RE-FLAG → **DP4-12** (already hedged, no transfer fn) |
| 11 (UNM) | excessively long, artifact-path assertions | OPINION → **DP4-21 / DP4-13** |
| 12 (UNM) | abstract too many diagnostics | OPINION → **DP4-13** |
| 13 (UNM) | dipole direction on null result should be omitted | RE-FLAG → **DP4-10** |
| 14 (UNM) | tables mix normalizations/fields/nulls | OPINION → **DP4-13** |
| 16 (UNM) | figs 4/7/8/9 diagnostic-vs-primary separation | RE-FLAG → **DP4-03 family** (disclosed, captions state systematics) |
| 17 (UNM) | training/validation description confusing | OPINION → **DP4-08 / DP4-15** |
MATCHED (#2/4/5/6/7/8/15) → DP4-09/06/17/16/14/11/21 respectively — all disclosed. 0 genuinely-new.

### INT Grok — MAJOR (4 UNMATCHED)
| # | finding | verdict → D-id |
|---|---------|----------------|
| 3 | 47% unmodeled harmonic amplitude | RE-FLAG → **DP4-17** |
| 4 | HC dipole vs full-catalog WLS incommensurable | RE-FLAG → **DP4-01 / DP4-13** (disclosed, primary_callout caption L824 warns rows not comparable) |
| 1 (UNM) | "REVISIONS ==== RAW RESPONSE" | PARSER NOISE |
| 2 (UNM) | "(2) ISSUES:" | PARSER NOISE |
| 5 (UNM) | 66.5% pseudo-labels + GZ1-human 21×-smaller sample | RE-FLAG → **DP4-08 / DP4-15** (DP4-18 backfire fingerprint) |
| 6 (UNM) | Shamir amplitude tension without matched Ganalyzer | RE-FLAG → **DP4-11** (explicitly disclosed, L1005) |
0 genuinely-new.

## Integrity note
No FALSIFIED/OPINION dismissal was used to bury a correctness defect: every UNMATCHED
item is either (a) a raw-file verdict-header fragment the parser split into a pseudo-finding,
or (b) a source-cited re-flag of content the paper already discloses (OPEN-COMPUTE limitations
DP4-15/16/17, referee-variance re-flags DP4-07/08/10/11/12/13). The load-bearing Shamir
factor-of-2 (DP4-01) remains CLOSED-BY-EDIT and verified. No fabrication, no fake ACCEPT,
no severity-steering.
