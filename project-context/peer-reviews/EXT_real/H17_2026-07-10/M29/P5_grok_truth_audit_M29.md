# P5 Grok EXT truth-audit — M29 (2026-07-13)

**Raw:** `M29/P5_grok_M29.md` (read verbatim) · screenshot `M29/P5_grok_M29.png`
**Verdict:** MINOR REVISIONS (0 MAJOR / 6 MINOR)
**Version reviewed:** v0.1.127 — FIRST external read AFTER the DP5-26 artifact-range fix.

**Provenance:** verdict word MINOR REVISIONS confirmed line 1; closing (line 11) credits
the central null "supported by the data, multi-algorithm null tests, permutation
framework, and systematic controls." All 6 findings are MINOR — the MAJOR band from M28
(pre-fix) softened this read (pattern-066 in-MINOR variance, not new content).

## CRITICAL CHECK — DP5-26 artifact-range item

**ABSENT.** `grep -niE "artifact|\[A[0-9]|A1--|A32|A34|numbering"` over the M29 raw returns
NONE. The v0.1.127 edit (three `[A1]--[A32]` → `[A1]--[A34]` + caption enumeration) removed
the reader-visible stale range; the fresh EXT read does not re-flag it. **DP5-26 fix HELD.**
→ P5 clean-wave streak advances 0→1.

## ledger_match + Opus adjudication (5 findings + 1 scaffold)

| # | sev | disposition | verdict |
|---|-----|-------------|---------|
| 1 | MINOR | scaffold-header parse artifact ("REVISIONS ISSUES:") — NOT a finding | — |
| 2 | MINOR | DP5-13 (post-hoc primary designation, exploratory) | RE-FLAG-DISCLOSED (§V B l.1668; abstract l.729-730) |
| 3 | MINOR | DP5-12 (RSD FoG bounded not removed; first-order Zel'dovich) | RE-FLAG-DISCLOSED (CLOSED-BY-COMPUTE first-order v0.1.122; small-scale FoG residual explicitly disclosed §XIII; \|Δf_CW\|≲0.03pp ≈40× under envelope) |
| 4 | MINOR | DP5-17 (no-published-bounce-model claim wants lit qualifier/citation) | RE-FLAG-DISCLOSED (§I lit-grounding search summary; disclosed limitation of an empirical-constraint framing) |
| 5 | MINOR | DP5-14 (tracer-program bright/dark ∼2.1σ sign-flip; Paper-IV per-leg propagation) | RE-FLAG-DISCLOSED (§VI D + §VIII; ∼0.001pp leak into DESIVAST primary already shown) |
| 6 | MINOR | DP5-11 (§VIII.F monopole reconciliation f_CW^P5=0.49719) + DP5-08 (σ_pred covariance) | RE-FLAG-DISCLOSED (§VIII F Table XVI reconciliation; monopole enters σ_pred only, non-load-bearing) |

**0 genuinely-new findings.** Every substantive item fingerprint-matches a standing DP5
disposition; #1 is a parser scaffold header. **DP5-26 fix HELD (artifact-range absent).**
No bump (v0.1.127 stands). directive_g.sh NOT run.
**Clean-wave streak 0→1.**
Cap HOLDS 74 (Grok MIN 12 + ChatGPT MAJ 6 + Gemini MAJ 6 = 50+24; post_verdict.sh recomputed).

Integrity: no faked accept, no un-sourced dismissal, no fabrication.
