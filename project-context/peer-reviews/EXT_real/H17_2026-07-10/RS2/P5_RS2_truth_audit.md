# P5 RS2 truth-audit (v0.1.123-2026-07-12)

**Wave:** RS2 · **NOW-UTC:** 2026-07-12T08:44:21Z · **auditor:** Fable-5 orchestrator, STRICT ledger-first.

Raws read verbatim before any verdict:
- EXT Grok `RS2/P5_grok_RS2.md` = **ACCEPT** (line 1 literally `VERDICT: ACCEPT`; verified char-for-char).
- INT (run.log 2026-07-12T08:24:xxZ, v0.1.123): openai=**MAJOR** / grok=**MINOR** / gemini=**MINOR** / claude=**MINOR** (`intwave_P5_RS2.log`, `API_P5_*.md`). **P5's best-ever INT board** — no INT REJECT, three MINORs.
- ChatGPT EXT leg = **FAILED-dead** (RS2b retry in flight). Recorded as a chart GAP (`chatgpt:EXT:failed`), NOT a zero. Do NOT wait.

## Milestone
**Second Grok EXT ACCEPT on P5 — this time on the fully-corrected version (v0.1.123, RSD-relabel + sign + quadrature 0.898 done).** First Grok ACCEPT was RS1 on v0.1.120; this ACCEPT holds after the v0.1.121-123 correction wave, so it is an ACCEPT on the corrected paper, not the pre-fix one. VERIFIED from raw. Posted to activityFeed.

## Verdict-first matrix (all vendors)
| leg | channel | verdict | modality |
|-----|---------|---------|----------|
| Claude | INT | MINOR REVISIONS | full-repo subscription subagent |
| OpenAI | INT | MAJOR REVISIONS | API native-PDF |
| Grok | INT | MINOR REVISIONS | API |
| Gemini | INT | MINOR REVISIONS | API |
| Grok | EXT | **ACCEPT** | headed browser |
| ChatGPT | EXT | FAILED (dead) | — (RS2b retry in flight) |

## ledger_match pre-triage
`tools/ledger_match.py … P5` → 3/4 MATCHED, 1 UNMATCHED (finding #2). All 4 findings are Grok EXT MINORs (an ACCEPT verdict with 4 tightening suggestions).

## Per-finding adjudication (Grok EXT, all MINOR)
- **#1 (Abstract/§I/§V B post-hoc/exploratory disclosure)** → **DP5-13** (RE-FLAG-DISCLOSED). §V B `sec:primary_path` + `tab:analysis_tree` + abstract already state "exploratory / no timestamped plan predates the data." Grok asks for one more abstract sentence = presentational preference on already-disclosed content. RE-FLAG, no reset.
- **#2 (§VI D/§XI 2.1σ bright/dark filament sign-flip leakage ≲0.001 pp)** → **DP5-14** (RE-FLAG-DISCLOSED; ledger_match UNMATCHED at 0.27 — diluted keyword overlap, resolved by source). The explicit 0.81pp→~0.001pp leakage propagation and the residual-ambiguity + sign-flip sentence are ALREADY in the paper (tex comment M7 l.139, (4) l.173-174; §VI.D). Grok literally says "the explicit numerical leakage calculation already performed in the text" — asks only to surface it into the residual-ambiguity paragraph. **PROCESS-NIT on already-present content; no genuinely-new reader-visible editable finding.** No reset.
- **#3 (§VIII/Table XI/XIII ~0.9 pp quadrature envelope co-dominant term)** → **DP5-11** (RE-FLAG-DISCLOSED). §VIII gives the term list, √0.885=0.94pp, "approximately independent" peak-excursions; the 0.60pp any-hole term is flagged. Grok's "add one sentence it's the tightest of correlated estimators" = statistical-philosophy OPINION, honestly presented. RE-FLAG, no reset.
- **#4 (submission logistics: A1–A13 DOIs, pipeline tag, Paper IV cross-ref at acceptance)** → **DP5-21** (OPEN-VENUE). Paper-IV coordination + archival-DOI-at-acceptance = known venue/coordination barrier, Houston-gated, not an editable defect. RE-FLAG, no reset.

## Engagement with new content
Grok ENGAGED the corrected v0.1.123: named the DESIVAST family-wise Bonferroni-5 null, the five-estimator robustness suite, the ≈0.9pp envelope terms, and the sign-flip leakage number — all post-correction values. Its one-sentence: "The central claim … is supported by the data, the five-estimator robustness suite, and the transparent multiplicity and post-hoc disclosures." A genuine ACCEPT on the fixed paper.

## Adjudication outcome
**0 genuinely-new reader-visible editable findings.** All 4 Grok MINORs are source-cited RE-FLAGs / OPEN-VENUE / PROCESS-NIT against the existing ledger. **NO bump; v0.1.123-2026-07-12 stands. directive_g.sh not run (no edit).**

## Streak
P5 clean-wave streak: was HELD at 2 (W4-EXT). RS2 clean (0 genuinely-new) → **streak 2→3** under directive-K. Grok EXT ACCEPT on the corrected version + no genuinely-new finding.

## Cap
post_verdict recompute after Grok EXT ACCEPT: 50 + grok(accept 16.7) + chatgpt(reject 0) + gemini(minor 12) = 78.7 → **cap 74→79**.

## Integrity
No faked ACCEPT — the ACCEPT is Grok's own verbatim verdict, read from the raw. No un-sourced dismissal; every re-flag cites a §/tex line + D-id. No fabrication. ChatGPT FAILED recorded as a GAP, not synthesized. Milestone (2nd Grok ACCEPT, on corrected version) posted to activityFeed.
