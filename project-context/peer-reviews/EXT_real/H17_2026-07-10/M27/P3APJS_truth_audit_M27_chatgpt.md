# Truth-audit — P3-ApJS M27-EXT ChatGPT (RECOVERED orphan) — FIRST ChatGPT read of the DAS-fixed version

- **paper:** P3-ApJS (`pipelines/p3_anomaly_engine/.../paper3_apjs.tex`), v3.1.159-apjs
- **reviewer/leg:** ChatGPT (Extended Thinking Pro), EXT
- **raw:** `M27/P3APJS_chatgpt_M27.md` — verdict line 1: `VERDICT: REJECT.` (16 MAJOR / 3 MINOR)
- **sibling:** `M27/P3APJS_chatgpt_M27a.md` (older chat `.../c/6a54d585-…`, also REJECT, also DAS-clean) — informational cross-check ONLY, no second verdict recorded.
- **provenance:** leg orphaned by an ext_submit poll-timeout; landed server-side, recovered + harvested in commit 02d68a8f. Raw read verbatim. Chat URL `.../c/6a54dc77-…` reviews the multi-survey anomaly catalog (268,519, DESI/SDSS/Planck/NEOWISE, ApJS framing) ✓ — correct paper.
- **method:** `tools/ledger_match.py P3` (10/20 auto-MATCHED) + full §3 Opus source-cited truth-audit + DP3-21 DAS signature-grep.

## CRITICAL CHECK — DP3-21 DAS FIX HELD vs ChatGPT
This is the **FIRST ChatGPT read of the DAS-fixed v3.1.159-apjs** (DP3-21 Gaia-block/LAMOST self-contradiction fixed, commit e24b42a9; prior ChatGPT reads M20 and earlier saw the pre-fix DAS).
- Signature-grep of the raw for the DP3-21 wording (Gaia block "carries feature-space scores" / LAMOST "excluded from every count" / DAS internal contradiction) = **NONE.**
- The raw's ONLY two "Data Availability" items are: (a) row-level reproducibility citing the paper's OWN 86.6%/~1.3% numbers → **DP3-15** (disclosed structural ceiling); (b) eROSITA/Gaia provenance excision → **DP3-08**. NEITHER is the DP3-21 self-contradiction.
- **DP3-21 FIX HELD against ChatGPT too** (M24 already confirmed HELD against Grok + a prior ChatGPT read).

## Verdict: 0 genuinely-new. Maximally-harsh ApJS floor (DP3-17 pattern-066 backfire).

| # | sev | finding | disposition |
|---|-----|---------|-------------|
| 1 | MAJOR | 268,519 "validated catalog-grade" threshold-engineered/quota-dependent | **DP3-06/-07** (RE-FLAG; process-volume + 2,468 benchmark + threshold families disclosed) |
| 2 | MAJOR | Validation tests don't validate the released selections | **DP3-09** (RE-FLAG; injection-recovery gate-type matrix + threshold families disclosed) |
| 3 | MAJOR | DESI population contradiction (2,468 science-target vs 98.8% Redrock) | **DP3-07/-11** (RE-FLAG; §III.C SPECTYPE composition ≠ purity; ZWARN=0 0.10% disclosed) |
| 4 | MAJOR | Row-level reproducibility absent (86.6% hashes, ~1.3% re-pullable) | **DP3-15** (OPEN-COMPUTE; paper's OWN §II.F numbers; pod-gated, does NOT reset) |
| 5 | MAJOR | Spectral preprocessing insufficiently specified / drives result | **DP3-01/-13** (RE-FLAG; within-survey ranking + preprocessing disclosed §VI) |
| 6 | MAJOR | S=5 not a 5σ event (z-transform of heavy-tailed MSE) | **DP3-09/-12** (RE-FLAG; score-comparability note; OOD-vs-production curation caveat) |
| 7 | MAJOR | SDSS mixes cross-transfer + native score axes | **DP3-14** (RE-FLAG; footnote heartsuit discloses continuity-slice vs native re-score) |
| 8 | MAJOR | Planck tier not validated (top 200, train/val overlap) | **DP3-06** (RE-FLAG; both denominators + overlap disclosed §III.F) |
| 9 | MAJOR | NEOWISE mask-tautology (100% recovery by construction) | **DP3-01/-13** (RE-FLAG; masking-geometry QA gate disclosed abstract L1027 "not a detector-sensitivity test") |
| 10 | MAJOR | eROSITA/Gaia provenance controls failed | **DP3-08** (RE-FLAG; both excised from every count, disclosed) |
| 11 | MAJOR | 58.8% novelty not established (catalog-absence ≠ novelty) | **DP3-07/-09** (RE-FLAG; SIMBAD-unmatched framing + follow-up disclosed) |
| 12 | MAJOR | 5″ dedup / cross-survey association inadequate | **DP3-11** (RE-FLAG; radius-sweep stability disclosed; single-FDR NOT claimed) |
| 13 | MAJOR | 37.3M not well-defined (36.76/36.93/37.29M) | **DP3-03/-04** (CLOSED-BY-EDIT v3.1.152 footnote-⊗ reconciliation) |
| 14 | MAJOR | §4.2 Poisson χ² dominated by footprints, no null | **DP3-10** (RE-FLAG; secondary/diagnostic, disclosed) |
| 15 | MAJOR | High-z (z≃6) candidates insufficiently verified | **DP3-11** (RE-FLAG; low-S/N Redrock candidates disclosed, effect-size ρ=0.036) |
| 16 | MAJOR | §5/App-C f_NL incoherent (samples switch; consistent with zero) | **DP3-10/-18** (RE-FLAG; secondary null demo; App C disclosed; CRITICAL RESEARCH DIRECTIVE keeps honest null) |
| — | MAJOR | §5.1 NANOGrav disconnected/overinterpreted | **DP3-10** (RE-FLAG; env-SMBHB caveat scopes "decisive") |
| 17 | MINOR | Fig 10 caption/figure mismatch | **DP3-16** (PROCESS-NIT; obsolete cross-transfer display) |
| 18 | MINOR | Figs 2–4/8 obsolete cross-transfer products | **DP3-16/-20** (PROCESS-NIT; baseline diagnostics) |
| 19 | MINOR | Organization/scope — combines catalog + failure-audit + fNL + PTA | **DP3-16** (OPINION/venue; Houston-gated) |

**ledger_match UNMATCHED (10):** verbose ApJS §-anchor restatement drives lexical scores below threshold (same as M17/M22); each Opus-adjudicated to the standing D-ids above.

## Result
0 genuinely-new editable findings; DAS FIX HELD. Grok half already counted M27 → **clean-wave streak HOLDS 2**; **cap 56 HOLDS** (Grok MAJ 6 + ChatGPT REJECT 0 + Gemini REJECT 0 = 50+6). No bump (byte-unchanged v3.1.159-apjs). directive_g.sh not run. Integrity: raw read verbatim before verdict; M27a sibling cross-checked informational-only; no ACCEPT faked; no finding dismissed without a source-cited verdict; no fabrication.
